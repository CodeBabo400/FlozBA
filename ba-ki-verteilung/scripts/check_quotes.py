#!/usr/bin/env python3
"""
Prüft, ob wörtliche Zitate verbatim im zugehörigen PDF stehen.

Zitate werden in Markdown-Dateien als Codeblock mit der Sprache `zitat` notiert:

    ```zitat
    key: muster2021roboter
    pdf: quellen/pdf/muster2021roboter.pdf
    seite: 12          # gedruckte Seitenzahl (für die Zitation)
    pdf_seite: 14      # Seite im PDF-Viewer (für die Prüfung)
    ---
    Hier steht der Text exakt wie im Original […] mit Auslassungen.
    ```

Prüfung:
- Text der angegebenen PDF-Seite wird mit `pdftotext` extrahiert (poppler-utils).
- Nur Extraktionsartefakte werden normalisiert: Leerraum/Zeilenumbrüche, Silbentrennung am
  Zeilenende, Ligaturen (NFKC), weiche Trennstriche, Varianten von Anführungszeichen,
  Apostrophen und Gedankenstrichen. Wortlaut, Groß-/Kleinschreibung und Satzzeichen
  werden NICHT angeglichen.
- `[…]` bzw. `[...]` = Auslassung: die Teile müssen in dieser Reihenfolge auf der Seite stehen.
- `[sic]` wird ignoriert. Andere `[eckige Einfügungen]` gelten als Lücke und werden gemeldet.
- Steht das Zitat nicht auf `pdf_seite`, wird das ganze PDF durchsucht und die
  tatsächliche Seite gemeldet (falsche Seitenangabe = Fehler).

Aufruf:
    python3 scripts/check_quotes.py                # alle .md in quellen/notizen, forschung, kapitel
                                                   # (Dateien mit "_" am Anfang = Vorlagen, übersprungen)
    python3 scripts/check_quotes.py quellen/notizen/muster2021roboter.md

Exit-Code 0 = alle Zitate bestätigt, 1 = mindestens ein Problem.
"""
from __future__ import annotations

import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK_RE = re.compile(r"```zitat\s*\n(.*?)\n```", re.DOTALL)
OMISSION_RE = re.compile(r"\[\s*(?:…|\.\.\.)\s*\]")
SIC_RE = re.compile(r"\[\s*sic!?\s*\]", re.IGNORECASE)
INSERT_RE = re.compile(r"\[[^\]]*\]")

CHAR_MAP = {
    "­": "",  # weicher Trennstrich
    "„": '"', "“": '"', "”": '"', "«": '"', "»": '"', "‟": '"',
    "‚": "'", "‘": "'", "’": "'", "‹": "'", "›": "'", "´": "'", "`": "'",
    "–": "-", "—": "-", "−": "-", "‐": "-", "‑": "-",
    " ": " ", " ": " ", " ": " ",
}


def normalize(text: str, join_hyphen: bool) -> str:
    text = unicodedata.normalize("NFKC", text)
    for a, b in CHAR_MAP.items():
        text = text.replace(a, b)
    # Silbentrennung am Zeilenende: "Arbeits-\nmarkt" -> "Arbeitsmarkt" bzw. "KI-Automatisierung"
    text = re.sub(r"-\s*\n\s*", "" if join_hyphen else "-", text)
    return re.sub(r"\s+", " ", text).strip()


def pdf_text(pdf: Path, page: int | None = None) -> str:
    cmd = ["pdftotext", "-raw"]
    if page is not None:
        cmd += ["-f", str(page), "-l", str(page)]
    cmd += [str(pdf), "-"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(res.stderr.strip() or "pdftotext fehlgeschlagen")
    return res.stdout


def pdf_pages(pdf: Path) -> int:
    res = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
    m = re.search(r"^Pages:\s+(\d+)", res.stdout, re.MULTILINE)
    return int(m.group(1)) if m else 0


def segments(quote: str) -> tuple[list[str], list[str]]:
    quote = SIC_RE.sub("", quote)
    quote = OMISSION_RE.sub("\x00", quote)
    inserts = INSERT_RE.findall(quote)
    quote = INSERT_RE.sub("\x00", quote)
    segs = [c.strip() for c in quote.split("\x00") if c.strip()]
    return segs, inserts


def found_in(page_text: str, segs: list[str]) -> bool:
    for join in (True, False):
        hay = normalize(page_text, join)
        pos = 0
        ok = True
        for s in segs:
            needle = normalize(s, True)
            idx = hay.find(needle, pos)
            if idx < 0:
                ok = False
                break
            pos = idx + len(needle)
        if ok:
            return True
    return False


def parse_block(raw: str) -> tuple[dict, str]:
    if "\n---\n" not in raw:
        raise ValueError("Trennlinie '---' zwischen Kopf und Zitattext fehlt")
    head, body = raw.split("\n---\n", 1)
    meta = {}
    for line in head.splitlines():
        line = line.split("#", 1)[0].strip()
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, body.strip()


def check_file(md: Path) -> list[tuple[str, str, str]]:
    results = []
    text = md.read_text(encoding="utf-8")
    for n, m in enumerate(BLOCK_RE.finditer(text), 1):
        label = f"{md.relative_to(ROOT)} #{n}"
        try:
            meta, quote = parse_block(m.group(1))
        except ValueError as e:
            results.append(("FEHLER", label, str(e)))
            continue
        missing = [k for k in ("key", "pdf", "seite", "pdf_seite") if not meta.get(k)]
        if missing:
            results.append(("FEHLER", label, f"Pflichtfelder fehlen: {', '.join(missing)}"))
            continue
        pdf = ROOT / meta["pdf"]
        if not pdf.exists():
            results.append(("KEIN PDF", label, f"{meta['pdf']} nicht vorhanden – Zitat ungeprüft"))
            continue
        try:
            page = int(meta["pdf_seite"])
        except ValueError:
            results.append(("FEHLER", label, "pdf_seite ist keine Zahl"))
            continue
        segs, inserts = segments(quote)
        if not segs:
            results.append(("FEHLER", label, "leerer Zitattext"))
            continue
        note = f" (Einfügungen als Lücke behandelt: {', '.join(inserts)})" if inserts else ""
        try:
            if found_in(pdf_text(pdf, page), segs):
                results.append(("OK", label, f"{meta['key']}, S. {meta['seite']}{note}"))
                continue
            hits = [p for p in range(1, pdf_pages(pdf) + 1) if found_in(pdf_text(pdf, p), segs)]
        except RuntimeError as e:
            results.append(("FEHLER", label, f"PDF nicht lesbar: {e}"))
            continue
        if hits:
            results.append(("SEITE FALSCH", label,
                            f"nicht auf pdf_seite {page}, aber auf PDF-Seite(n) {hits} – Seitenangabe korrigieren"))
        else:
            results.append(("NICHT GEFUNDEN", label,
                            "Wortlaut nicht im PDF – Zitat ist NICHT verbatim oder PDF ist ein Scan ohne Textebene"))
    return results


def main(argv: list[str]) -> int:
    scan_dirs = ["quellen/notizen", "forschung", "kapitel"]
    files = [Path(a).resolve() for a in argv] if argv else [
        p for d in scan_dirs for p in (ROOT / d).rglob("*.md") if not p.name.startswith("_")
    ]
    results = []
    for f in sorted(files):
        results += check_file(f)
    if not results:
        print("Keine ```zitat-Blöcke gefunden.")
        return 0
    width = max(len(r[0]) for r in results)
    for status, label, msg in results:
        print(f"{status:<{width}}  {label}  {msg}")
    bad = [r for r in results if r[0] != "OK"]
    print(f"\n{len(results) - len(bad)} von {len(results)} Zitaten bestätigt.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
