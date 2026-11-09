---
name: quelle-exzerpieren
description: Verwenden, wenn ein Volltext (PDF in quellen/pdf/) gelesen und in eine strukturierte Notiz in quellen/notizen/ überführt werden soll.
---
# Quelle exzerpieren

1. Prüfen, ob `quellen/notizen/<key>.md` schon existiert. Wenn ja: nur ergänzen.
2. PDF vollständig lesen (`pdftotext -raw quellen/pdf/<key>.pdf -`). Bei langen Texten
   abschnittsweise; Einleitung, Daten/Methode, Ergebnisse und Fazit haben Vorrang.
3. Notiz anlegen nach Vorlage `quellen/notizen/_VORLAGE.md`.
4. Jede inhaltliche Aussage mit Seitenzahl (gedruckte Seite) versehen.
5. Wörtliche Zitate nur nach Skill `$zitat-verbatim`, anschließend
   `python3 scripts/check_quotes.py quellen/notizen/<key>.md` ausführen.
6. Zahlen exakt übernehmen: Wert, Einheit, Bezugsjahr, Definition, Tabelle/Abbildung.
7. Abschnitt „Kritische Einordnung“: Grenzen laut Autoren + eigene Einschätzung, getrennt
   gekennzeichnet (`[LAUT AUTOREN]` / `[EIGENE EINSCHÄTZUNG]`).
8. Kurzfazit (max. 3 Sätze) und betroffene Teilfragen in `forschung/FORSCHUNGSLOG.md`
   eintragen (`$forschungslog`).

Danach wird das PDF nicht erneut vollständig gelesen; weitere Arbeit erfolgt mit der Notiz.
