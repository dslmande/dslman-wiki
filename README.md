# dsl-man.de – Wiki-Inhalte

Vollständiger Export des Confluence-Cloud-Wikis `diysynth.wiki.dsl-man.de`
als Markdown, als Grundlage für die neue Website.

## Aufbau

```
content/<space>/<seite>/index.md      Seiteninhalt als Markdown + YAML-Frontmatter
content/<space>/<seite>/assets/       Anhänge dieser Seite (Bilder, PDFs, FPD, ZIP …)
raw/                                  Roh-Export der Confluence-API (verlustfreie Quelle)
tools/                                Export- und Konvertierungsskripte
```

Die Ordnerhierarchie entspricht der Seitenhierarchie in Confluence; die
Startseite eines Space ist das `index.md` des Space-Ordners. Blogposts liegen
unter `<space>/blog/<datum>-<titel>/`.

Jede Seite trägt im Frontmatter `title`, `space`, `type`, `created`, `updated`,
`confluence_id` und `confluence_url` – damit lässt sich jederzeit auf das
Original zurückverfolgen. `raw/url-map.csv` bildet alte Confluence-URLs auf die
neuen Pfade ab (Grundlage für spätere 301-Weiterleitungen).

## Export wiederholen

```bash
python3 tools/cf_fetch.py      # Roh-Export der API nach raw/
python3 tools/cf_assets.py     # Anhänge herunterladen (überspringt Vorhandenes)
python3 tools/cf_convert.py    # Markdown neu erzeugen (--keep behält Assets)
```

Der Export braucht keine Zugangsdaten: das Wiki ist anonym lesbar. Seiten mit
Leseeinschränkung sind daher **nicht** enthalten – siehe `raw/convert-report.txt`,
Abschnitt „Nicht aufgeloeste Links“.

## Stand

Siehe `raw/convert-report.txt` für unbekannte Makros, nicht auflösbare Links und
fehlende Anhänge nach dem letzten Lauf.
