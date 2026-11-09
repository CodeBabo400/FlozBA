---
name: literaturrecherche
description: Verwenden, wenn wissenschaftliche Literatur zu einer Teilfrage (TF1–TF8) gesucht, gesichtet oder bewertet werden soll.
---
# Literaturrecherche

## Vorher
1. `forschung/SACKGASSEN.md` auf bereits verworfene Quellen und Suchwege prüfen.
2. `forschung/ergebnisse/<teilfrage>.md` lesen (falls vorhanden), um Doppelarbeit zu vermeiden.
3. In `quellen/literatur.bib` prüfen, ob Quellen schon erfasst sind.

## Suche
1. Teilfrage in 3–6 Suchbegriffe zerlegen, jeweils deutsch UND englisch
   (z. B. „Automatisierung Lohnquote Deutschland“ / „automation labor share Germany“).
2. Bevorzugte Orte: Google Scholar, EconBiz, RePEc/IDEAS, SSRN, NBER, IZA Discussion Papers,
   IAB-Forschungsberichte, DIW Wochenbericht, ifo, ZEW, Bundesbank-Monatsberichte,
   Sachverständigenrat, OECD iLibrary, Destatis.
3. Schneeballprinzip: Literaturverzeichnisse zentraler Studien auswerten (rückwärts) und
   „cited by“ prüfen (vorwärts).

## Pro Treffer erfassen (Tabelle im Chat ausgeben)
| Autor(en) | Jahr | Titel | Venue | Typ | Begutachtet | DOI/URL | Daten/Methode | Relevanz (1 Satz) | Status |
Status: `[VOLLTEXT]` / `[NUR ABSTRACT]` / `[NICHT VERIFIZIERT]`.

## Verifikation
- DOI über `https://doi.org/<DOI>` auflösen und Titel/Autoren/Jahr abgleichen.
- Kein DOI: stabile URL des Verlags/Instituts, nicht eine Drittseite.
- Nicht verifizierbar → NICHT in die `.bib` übernehmen; in `SACKGASSEN.md` notieren.

## Danach
1. Nutzer zeigt, welche Treffer übernommen werden. Erst dann BibTeX-Eintrag in
   `quellen/literatur.bib` (Key-Format siehe `kontext/zitierstil.md`).
2. Für übernommene Quellen Nutzer bitten, das PDF als `quellen/pdf/<key>.pdf` abzulegen.
3. Ergebnis der Recherche mit `$forschungslog` dokumentieren (inkl. Suchbegriffe und Datum,
   damit die Suche reproduzierbar ist).

## Verboten
- Quellen aus dem Gedächtnis nennen, ohne sie in dieser Sitzung gefunden zu haben.
- Inhalte eines Papers nur aus dem Titel ableiten.
