# 🎬 Claudia Plessl — zwei Vorstellungsvideos

Beide Filme basieren auf der am **7. November 2026** geprüften [Live-Website](https://claudiaplessl.at/). Sie enthalten Claudias echtes Porträt, deutsche Bildschirmtexte, das Original-Logo und die leise Instrumentalmusik „Casa in Ordine“ aus dem bestehenden Projekt. Keine neue Sprecherstimme, kein Avatar und kein KI-verändertes Gesicht.

| Variante | Lokale Ausgabedatei im übergeordneten Projektordner | Bildwelt |
| --- | --- | --- |
| 🌿 Editorial | `plessl-introduction-480p.mp4` | Wohn- und Ordnungsbilder der Website |
| ✨ Alibaba Wan 3.0 | `plessl-introduction-wan-480p.mp4` | Neue Wan-Innenraumaufnahme, echtes Porträt und lokal montierte Texte |

**Technik:** jeweils 30,000 Sekunden, 480×854 Hochformat, 30 fps, H.264, AAC-Stereo. Claudia ist von 5 bis 12 Sekunden zu sehen. Musik: −25,4 LUFS integriert, mit sanfter Ein- und Ausblendung. [Review und Prüfgrenzen](REVIEW.md).

## 📂 Quellen und lokale Medien

- [Story und Szenenzeiten](STORYBOARD.md), [Regiebrief](SPEC.md), [Bildquellen und Prüfsummen](asset-sources.json).
- Originalbilder und Schriftdateien liegen unter `assets/`; Schriftlizenzen sind beigefügt.
- `assets/music-soft.wav` und `assets/wan-room.mp4` bleiben lokal und werden nicht öffentlich mit Git veröffentlicht. Für einen neuen Checkout müssen diese Dateien aus der autorisierten lokalen Medienablage ergänzt werden.
- Musikquelle: vorhandener Nutzertrack `/home/nuc8/05_development/55_laulau/casa_in_ordine.mp3`, Ausschnitt ab 106,3 Sekunden, 30 Sekunden.
- Wan-Job und Rohdaten: `../outputs/plessl-introduction/wan-job/`. Eine 20-sekündige 480p-Anfrage wurde mit gemeldeten USD 0,85 abgerechnet. Claudia wurde nicht an das Modell gesendet.
- Fertige Videos, Rohdaten, Prüfbilder und Audio bleiben lokal; dieser Ordner enthält die bearbeitbaren Quellen.

## 🛠️ Vorschau und Rendern

Node.js 22, FFmpeg und die lokal vorhandenen Medien sind erforderlich. Die Projektbefehle verwenden HyperFrames **0.9.20**.

```bash
npm run check
npm run dev
```

Die Variante ist im Variablenfeld `variant` als `editorial` oder `wan` wählbar. Standard ist `editorial`. Die Vorschau lässt sich auch in der [HyperFrames Desktop-App](https://hyperframes.studio/studio/download?os=linux&src=cli) bearbeiten.

```bash
npm run render -- --quality delivery --strict --variables '{"variant":"editorial"}' -o ../plessl-introduction-480p.mp4
npm run render -- --quality delivery --strict --variables '{"variant":"wan"}' -o ../outputs/plessl-introduction/wan-export-before-portrait-fix.mp4
bash finish_wan.sh
```

Die letzte Montage sichert das unveränderte Porträt-Zeitfenster aus dem geprüften Editorial-Film im Wan-Ergebnis. Der direkte Wan-Renderer hatte diese Szene in der Ausgabe ausgelassen; die Vorschau allein genügte deshalb nicht als Kontrolle. Nach jedem neuen Export: Gesicht und Name bei 8 Sekunden prüfen, Dauer und beide Streams mit `ffprobe` kontrollieren und den vollständigen Film mit FFmpeg decodieren.

`build_source.py` erzeugt die fünf Szenendateien und den Master aus dem Regiebrief. Nach einer bewussten Neugenerierung sind die Master-Übergänge mit dem lokalen `motion-doctrine`-Werkzeug erneut aus `ledger.json` zu stempeln; der bereits gestempelte Master ist im Repository enthalten.
