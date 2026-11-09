---
name: zitat-verbatim
description: Verwenden, sobald ein wörtliches Zitat aus einer Quelle notiert, in eine Notiz übernommen, in einem Text verwendet oder überprüft werden soll.
---
# Wörtliche Zitate – verbatim aufnehmen und prüfen

## Grundsatz
Ein wörtliches Zitat entsteht ausschließlich durch Kopieren aus dem geöffneten Volltext
(PDF in `quellen/pdf/` oder Originaldokument). Niemals aus dem Gedächtnis, aus einem
Abstract, aus Suchergebnis-Snippets, aus einer Sekundärquelle oder durch Rückübersetzung.

## Ablauf
1. Liegt das PDF in `quellen/pdf/<key>.pdf`? Wenn nein: Nutzer bitten, es abzulegen.
   Bis dahin KEIN wörtliches Zitat, höchstens eine Paraphrase mit `[NUR ABSTRACT]` o. Ä.
2. Text der Seite extrahieren: `pdftotext -f N -l N -raw quellen/pdf/<key>.pdf -`
3. Passage exakt übernehmen. Nur erlaubte Eingriffe:
   - Auslassung `[…]`
   - Einfügung `[…Text…]` (sparsam, nur zur grammatischen Einbettung)
   - `[sic]` bei Fehlern im Original
   - Silbentrennungen am Zeilenende zusammenführen (kein Eingriff in den Wortlaut)
4. Zwei Seitenangaben erfassen:
   - `seite` = gedruckte Seitenzahl (für die Zitation)
   - `pdf_seite` = Seitennummer im PDF (für die Prüfung)
5. Zitat in `quellen/notizen/<key>.md` unter „Wörtliche Zitate“ als Block notieren:

   ````
   ```zitat
   key: <key>
   pdf: quellen/pdf/<key>.pdf
   seite: <gedruckte Seite>
   pdf_seite: <PDF-Seite>
   ---
   <exakter Text>
   ```
   ````
   Darunter in einer Zeile: wofür das Zitat gebraucht wird (Teilfrage-Kürzel).
6. Prüfen: `python3 scripts/check_quotes.py quellen/notizen/<key>.md`
   - `OK` → Zitat gilt als verifiziert.
   - `SEITE FALSCH` → Seitenangabe korrigieren, erneut prüfen.
   - `NICHT GEFUNDEN` → Zitat nicht verwenden. Mit dem Volltext neu abgleichen. Bei einem
     Scan ohne Textebene: Nutzer informieren, Zitat als `[MANUELL PRÜFEN]` markieren.
   - `KEIN PDF` → wie Schritt 1.
7. Ein fehlgeschlagenes Zitat mit Ursache in `forschung/SACKGASSEN.md` vermerken.

## Verwendung im Text
Nur Zitate mit Status `OK` dürfen in `forschung/ergebnisse/` oder `kapitel/` übernommen
werden – dort als derselbe `zitat`-Block (dann prüft das Skript auch diese Stelle mit).

## Verboten
- Glätten, Modernisieren, Korrigieren oder Übersetzen des Wortlauts.
- Anführungszeichen um eine Paraphrase.
- Zitate „sinngemäß wörtlich“.
