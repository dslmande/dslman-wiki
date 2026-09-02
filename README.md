# dsl-man.de – Wiki-Inhalte

Vollständiger Export des Confluence-Cloud-Wikis `diysynth.wiki.dsl-man.de`
als Markdown, als Grundlage für die neue Website.

## Aufbau

```
content/<space>/<seite>/index.md      Seiteninhalt als Markdown + YAML-Frontmatter
content/<space>/<seite>/assets/       Anhänge dieser Seite (Bilder, PDFs, FPD, ZIP …)
src/                                  Astro-Website (Layouts, Navigation, Suche)
raw/                                  Roh-Export der Confluence-API (verlustfreie Quelle)
tools/                                Export-, Konvertierungs- und Build-Skripte
```

## Website (Astro)

```bash
npm install
npm run dev      # Vorschau auf http://localhost:4321
npm run build    # statische Site nach dist/
```

`publicDir` zeigt auf `content/`: die Anhänge werden unverändert neben ihren
Seiten ausgeliefert, statt durch die Bildpipeline zu laufen – bei 4177 Dateien
macht das den Unterschied zwischen Sekunden und Stunden Buildzeit.
`tools/remark-wiki-links.mjs` übersetzt beim Rendern die dateibezogenen
Verweise aus dem Export (`../seite/index.md`, `assets/bild.jpg`) in Site-URLs;
die Markdown-Dateien selbst bleiben dadurch unangetastet und bleiben auch in
GitHub oder jedem Editor benutzbar.

Die Ordnerhierarchie entspricht der Seitenhierarchie in Confluence; die
Startseite eines Space ist das `index.md` des Space-Ordners. Blogposts liegen
unter `<space>/blog/<datum>-<titel>/`.

Jede Seite trägt im Frontmatter `title`, `space`, `type`, `created`, `updated`,
`confluence_id` und `confluence_url` – damit lässt sich jederzeit auf das
Original zurückverfolgen. `raw/url-map.csv` bildet alte Confluence-URLs auf die
neuen Pfade ab (Grundlage für spätere 301-Weiterleitungen).

## Export wiederholen

```bash
python3 tools/cf_fetch.py        # Roh-Export der API nach raw/
python3 tools/cf_assets.py       # Anhänge herunterladen (überspringt Vorhandenes)
python3 tools/optimize_images.py # Bilder auf Webgröße rechnen (Originale sichern)
python3 tools/cf_convert.py      # Markdown neu erzeugen (--keep behält Assets)
python3 tools/cf_check.py        # prüft, ob alle Verweise auf echte Dateien zeigen
```

Der Export läuft ohne Zugangsdaten, weil das Wiki anonym lesbar ist – dabei
bleiben Seiten mit Leseeinschränkung allerdings **unsichtbar**. Für einen
vollständigen Export ein API-Token hinterlegen
(id.atlassian.com → Sicherheit → API-Token):

```bash
export CONFLUENCE_EMAIL="Patrick@dsl-man.de"
export CONFLUENCE_TOKEN="…"
```

## Bilder

`tools/optimize_images.py` rechnet Bilder auf max. 2000 px und JPEG-Qualität 75
(hier: 5,17 GB → 1,73 GB) und wandelt HEIC nach JPEG. Die unveränderten
Originale liegen außerhalb des Repos unter `../dslman-wiki-originale`; ein
erneuter Lauf rechnet immer von dort, damit sich kein Qualitätsverlust
aufsummiert. Eine stärkere Stufe ist also jederzeit gefahrlos möglich (Werte
`MAXPX` und `QUALITY` im Skript).

## Stand des letzten Laufs

- 506 Seiten (470 Seiten + 36 Blogposts) aus 22 Spaces
- 4177 Anhänge, alle heruntergeladen
- 4959 interne Verweise aufgelöst, 4 Ziele fehlen (waren schon in Confluence tot)
- 17 Anhänge hingen an Seiten, die anonym nicht sichtbar sind → `content/_verwaiste-anhaenge/`

Details in `raw/convert-report.txt`.
