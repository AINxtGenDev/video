# Review — Vorstellungsvideo

## Entscheidung und Bildkontrolle

Die gewählte Erzählung verbindet ein Wohnmotiv mit Claudia als realer Ansprechpartnerin, den Leistungen Ordnung/Gestaltung und einer klaren Kontaktaufforderung. Ablauf-Erklärfilm und Website-Rundgang wurden nicht gebaut. Das Originalporträt erscheint sieben Sekunden lang groß und mit vollständig sichtbarem Gesicht; es wurde nicht an Wan übermittelt.

Die fünf Szenen wurden auf Beat- und Telefon-Kontaktbögen geprüft, die vier Schnitte jeweils in fünf Zwischenbildern. Ein unabhängiger Review-Agent fand auf den gelieferten Editorial-Kontaktbögen keine P0/P1-Probleme. Die Wan-Variante wurde zusätzlich anhand eigener Szenenbilder geprüft. Die Ansicht bei 28 und 29,75 Sekunden enthält lesbare Domain und KI-Innenraumkennzeichnung.

## Messungen und Grenzen

- Beide Varianten bestanden den vollständigen HyperFrames-Check: keine Fehler oder Warnungen nach der Kontrastkorrektur.
- Ein Info-Fund zur seitlichen Begrenzung der Porträtszene bleibt absichtlich: Der Szenenträger verlässt beim Schnitt kurz den beschnittenen Bühnenbereich. Der bestätigte Schnitt und die Textpositionen sind davon nicht beeinträchtigt.
- Alle vier Nahtstellen bestanden Richtung, Geschwindigkeit und Null-Überlappung. Der lokale Adapter des älteren Prüfskripts bindet das unveränderte Master-Skript nach dem Laden der Unterkompositionen neu und sucht anschließend die Master-Zeitleiste auf. Ohne diese Anpassung maß der alte Preview-Seek-Pfad statische, noch nicht gebundene Master-Ziele. Der globale Skill wurde nicht verändert. System-Chrome wurde verwendet; keine Änderung der Host-Sicherheitskonfiguration.
- Musikquelle ist der vorhandene Nutzertrack „Casa in Ordine“, auf −25 LUFS Zielwert vorbereitet, mit Ein- und Ausblendung. Die Lautheit und Tonspur werden im Export gemessen. Musik wurde nicht angehört; dies ist keine gehörte Qualitätsprüfung.
- Die abschließende Dateiprüfung fand im direkten Wan-Export eine fehlende Porträtszene, obwohl die Vorschau sie zeigte. Der Auslieferungsfilm übernimmt deshalb exakt das Zeitfenster 5–12 s aus dem geprüften Editorial-Export; die Wan-Abschnitte und seine unveränderte Musikspur bleiben erhalten. `finish_wan.sh` dokumentiert die reproduzierbare Montage. Alle 210 Porträtbilder wurden gegen die Editorial-Sequenz verglichen: SSIM 0,998318 nach der zusätzlichen H.264-Kodierung. Das endgültige Wan-Porträt wurde erneut visuell geprüft.
- Beide endgültigen MP4-Dateien sind exakt 30,000 s lang, 480×854, 30 fps und 900 Bilder, mit H.264 und einer AAC-Stereospur bei 48 kHz. Vollständige Decoderläufe bestanden. Die Musikmessung ergab −25,4 LUFS integriert, −13 dBTP und kein Clipping.
- Die Wan-Bildwelt zeigt wiederholt denselben Wohnraum. Sie ist dadurch weniger spezifisch für Stauraum als das Ordnungsbild der Editorial-Variante. Für eine spätere Fassung wäre eine eigene, freigegebene Stauraumaufnahme die sinnvollste Ergänzung.
- Kundenreferenzen und Vorher-Nachher-Ergebnisse werden nicht behauptet. Die Innenraummotive sind als KI-generiert gekennzeichnet.

## Auslieferung

Die abschließenden MP4-Messungen und Prüfsummen stehen lokal unter `../outputs/plessl-introduction/`. Die endgültigen technischen Ergebnisse werden zusätzlich in `../session.md` festgehalten. Die Videos, Musikdatei, Wan-Rohdaten und Prüfarbeitsdateien bleiben außerhalb der öffentlichen Git-Veröffentlichung.
