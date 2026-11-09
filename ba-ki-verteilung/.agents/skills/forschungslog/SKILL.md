---
name: forschungslog
description: Verwenden, wenn ein Ergebnis, eine Entscheidung, ein Fehler oder eine Sackgasse dokumentiert werden soll, sowie am Ende jeder Arbeitssitzung.
---
# Forschungslog führen

Ziel: Der Stand muss in einer neuen Sitzung ohne Chatverlauf rekonstruierbar sein, und
Fehler dürfen sich nicht wiederholen.

## Wohin gehört was?
| Inhalt | Datei | Form |
|---|---|---|
| Neue Erkenntnis mit Beleg | `forschung/FORSCHUNGSLOG.md` | Eintrag nach Vorlage unten (anhängen, nie löschen) |
| Verdichtetes Ergebnis je Teilfrage | `forschung/ergebnisse/<TF-Kürzel>.md` | wird überarbeitet, bleibt aktuell |
| Irrweg, toter Link, unbrauchbare/falsche Quelle, fehlgeschlagenes Zitat, falsche Annahme | `forschung/SACKGASSEN.md` | Eintrag mit Ursache und Lehre |
| Grundsatzentscheidung (Abgrenzung, Methode, Zitierstil) | `status/entscheidungen.md` | Datum, Entscheidung, Begründung |
| Aktueller Stand, nächste Schritte | `status/STAND.md` | überschreiben, max. 20 Zeilen |

## Vorlage FORSCHUNGSLOG-Eintrag
```
### JJJJ-MM-TT – <TF-Kürzel> – <Kurztitel>
- Erkenntnis: <1–3 Sätze, sachlich>
- Beleg: <bibkey>, S. <x> | Status: [VOLLTEXT]/[NUR ABSTRACT]/[SEKUNDÄR …]
- Gegenbefund/Einschränkung: <falls vorhanden, sonst „keiner gefunden“>
- Sicherheit: hoch / mittel / gering – <Begründung in einem Halbsatz>
- Offene Frage: <falls vorhanden>
```

## Vorlage SACKGASSEN-Eintrag
```
### JJJJ-MM-TT – <Kurztitel>
- Was wurde versucht: …
- Warum gescheitert: …
- Lehre / künftig stattdessen: …
```

## Regeln
- Einträge im FORSCHUNGSLOG und in SACKGASSEN werden nur angehängt, nie gelöscht.
  Korrekturen als neuer Eintrag mit Verweis („korrigiert Eintrag vom …“).
- Keine Erkenntnis ohne Belegzeile. Eigene Schlussfolgerungen als
  `[EIGENE SCHLUSSFOLGERUNG]` kennzeichnen.
- Wörtliche Zitate nur als geprüfter `zitat`-Block (`$zitat-verbatim`).
