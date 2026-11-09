# Bachelorarbeit VWL – KI-Automatisierung und Verteilung in Deutschland

> Welche Auswirkungen kann fortschreitende KI-Automatisierung auf die Einkommens- und
> Vermögensverteilung in Deutschland haben, und wann stößt die lohnbasierte
> Einkommenssicherung an ihre Grenzen?

Arbeitsumgebung für die Recherche mit OpenAI Codex (App, IDE-Erweiterung oder CLI).

## Prinzip: kleiner Kontext, Wissen bei Bedarf
| Ebene | Datei(en) | Wann geladen |
|---|---|---|
| Grundregeln + Wegweiser | `AGENTS.md` | automatisch in jeder Sitzung |
| Arbeitsabläufe | `.agents/skills/*/SKILL.md` | nur Name/Beschreibung vorab, Inhalt bei Bedarf |
| Fachkontext | `kontext/*.md` | nur wenn AGENTS.md darauf verweist |
| Gedächtnis | `status/STAND.md`, `forschung/SACKGASSEN.md` | zu Beginn jeder Sitzung |
| Ergebnisse | `forschung/FORSCHUNGSLOG.md`, `forschung/ergebnisse/` | gezielt pro Teilfrage |
| Quellen | `quellen/literatur.bib`, `quellen/notizen/<key>.md`, `quellen/pdf/` | gezielt pro Quelle |

## Einrichtung
1. Repo klonen: `git clone <URL>` und Ordner in der Codex-App / VS Code öffnen
   (bzw. `codex` im Wurzelordner starten). Immer aus dem Wurzelordner arbeiten,
   sonst findet Codex `AGENTS.md` nicht vollständig.
2. Beim ersten Start das Projekt als vertrauenswürdig („trusted“) bestätigen, sonst wird
   `.codex/config.toml` (Live-Websuche) ignoriert.
3. Prüfen, ob die Skills erkannt werden (in der Skill-Liste bzw. per `$` im Eingabefeld).
   Falls nicht: Codex aktualisieren; Speicherort der Projekt-Skills in der aktuellen Doku
   prüfen (<https://developers.openai.com/codex/skills>).
4. Für das Zitat-Prüfskript: Python 3 und poppler-utils (`pdftotext`, `pdfinfo`).
   - macOS: `brew install poppler`
   - Ubuntu/Debian: `sudo apt install poppler-utils`
   - Windows: poppler-Binaries installieren und in den PATH aufnehmen, oder WSL nutzen
5. `kontext/projekt.md` → Abschnitt „Offene Rahmendaten“ ausfüllen.

## Arbeitsablauf (eine Aufgabe pro Sitzung)
```
Neue Sitzung
 → Codex liest STAND.md + SACKGASSEN.md
 → Aufgabe, z. B.: "Nutze $literaturrecherche für TF3-arbeitsmarkt-de.
                    Max. 10 Treffer, bevorzugt Peer-Review und IAB/DIW/ZEW."
 → PDFs der ausgewählten Quellen nach quellen/pdf/<key>.pdf legen
 → "Nutze $quelle-exzerpieren für <key>."
 → Ergebnisse landen in FORSCHUNGSLOG.md und forschung/ergebnisse/
 → Sitzung beenden: "Aktualisiere STAND.md."
```
Lange Chats vermeiden: Lieber neue Sitzung starten – das Gedächtnis steckt in den Dateien.

## Wörtliche Zitate
Zitate werden als `zitat`-Block mit PDF-Pfad und Seitenzahl notiert (siehe
`.agents/skills/zitat-verbatim/SKILL.md`) und maschinell gegen das PDF geprüft:

```bash
python3 scripts/check_quotes.py
```
Status: `OK`, `SEITE FALSCH`, `NICHT GEFUNDEN`, `KEIN PDF`, `FEHLER`.
Nur `OK`-Zitate dürfen in die Arbeit. Grenzen: Gescannte PDFs ohne Textebene können nicht
geprüft werden (vorher OCR, z. B. mit `ocrmypdf`); das Skript vereinheitlicht Leerraum,
Silbentrennung, Ligaturen sowie Varianten von Anführungszeichen und Strichen.

## Urheberrecht und Prüfungsrecht
- PDFs sind per `.gitignore` vom Repo ausgeschlossen. Ist das Repo privat, kann die Zeile
  entfernt werden; Volltexte nicht öffentlich hochladen.
- KI-Einsatz vorher mit den Regeln der Hochschule und der Betreuung abgleichen und ggf.
  in der Eigenständigkeitserklärung angeben. Die Git-Historie und
  `status/entscheidungen.md` dokumentieren den Arbeitsprozess.
