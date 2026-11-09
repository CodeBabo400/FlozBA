---
name: daten-recherche
description: Verwenden, wenn Kennzahlen für Deutschland benötigt werden (z. B. Gini, Lohnquote, Vermögensanteile, Beitragssätze, Beschäftigung, Rentenfinanzen).
---
# Daten-Recherche

1. `kontext/datenquellen.md` lesen und die zuständige amtliche/institutionelle Quelle wählen.
2. Zahl direkt beim Herausgeber suchen (Destatis-Tabelle, Bundesbank-Veröffentlichung,
   DRV-Bericht usw.), nicht über Presseartikel.
3. Für jede Zahl erfassen:
   - Wert und Einheit
   - Bezugsjahr bzw. -zeitraum, Stand/Veröffentlichungsdatum
   - Definition (z. B. Gini verfügbare Äquivalenzeinkommen, Personen; Lohnquote unbereinigt)
   - Fundstelle: Tabellennummer/Code, Seite, URL, Abrufdatum
4. Unterscheiden sich Werte zwischen Quellen (z. B. SOEP vs. EU-SILC): beide notieren und
   die methodische Ursache benennen, nicht einen Wert „auswählen“.
5. Ablage: in `forschung/ergebnisse/<teilfrage>.md` unter „Daten“ und Eintrag im
   `FORSCHUNGSLOG.md`.
6. Eigene Berechnungen (z. B. Veränderungsraten, Szenarien) als `[EIGENE BERECHNUNG]`
   kennzeichnen, Rechenweg und Eingangswerte angeben; Skripte in `scripts/` ablegen.
