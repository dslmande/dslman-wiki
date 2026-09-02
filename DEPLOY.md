# Veröffentlichen

`npm run build` erzeugt die fertige Site in `dist/` – reine statische Dateien,
kein Node auf dem Server nötig. Der Ordner ist rund 3 GB groß, weil alle
Anhänge mitgehen.

## Auf den eigenen Server (Apache, wie bisher unter dsl-man.de)

```bash
npm run build
rsync -av --delete dist/ benutzer@server:/pfad/zum/webroot/
```

Die Seiten liegen als `<pfad>/index.html` – Apache liefert sie ohne weitere
Konfiguration aus. Sinnvoll sind noch:

```apache
ErrorDocument 404 /404.html
# Anhänge dürfen lange im Cache bleiben, HTML nicht
<FilesMatch "\.(jpg|jpeg|png|gif|svg|pdf|zip|fpd|hex|syx)$">
  Header set Cache-Control "public, max-age=31536000, immutable"
</FilesMatch>
```

## Alternativ: Cloudflare Pages / Netlify

Repository verbinden, Build-Befehl `npm run build`, Ausgabeverzeichnis `dist`.
Beide haben allerdings Größenbeschränkungen pro Deployment (Cloudflare Pages:
25 MB je Datei, 20 000 Dateien) – mit 4177 Anhängen passt das, sollte aber vor
dem Umstieg geprüft werden.

## Alte Confluence-Adressen weiterleiten

`raw/url-map.csv` enthält für jede Seite die alte Confluence-URL und den neuen
Pfad. Daraus lassen sich 301-Weiterleitungen erzeugen, sobald feststeht, wohin
`dsl-man.de` zeigt – zum Beispiel als `.htaccess`-Regeln oder als
`_redirects`-Datei. Solange das alte Wiki noch läuft, sind beide Adressen
parallel erreichbar; die Weiterleitungen brauchst du erst beim Abschalten.
