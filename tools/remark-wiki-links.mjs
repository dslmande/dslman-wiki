/**
 * Übersetzt die aus Confluence exportierten, dateibezogenen Verweise in
 * Site-URLs:
 *
 *   ../andere-seite/index.md  ->  /space/andere-seite/
 *   assets/bild.jpg           ->  /space/seite/assets/bild.jpg
 *
 * Läuft als remark-Plugin, also bevor Astro relative Bildpfade als lokale
 * Assets einsammelt: absolute Pfade reicht Astro unverändert durch, sodass die
 * 4177 Anhänge direkt aus content/ ausgeliefert werden statt durch die
 * Bildpipeline zu laufen.
 */
import path from 'node:path';

const CONTENT = path.resolve('content');

function walk(node, fn) {
  fn(node);
  for (const child of node.children ?? []) walk(child, fn);
}

function isExternal(url) {
  return !url || /^([a-z]+:|\/\/|\/|#)/i.test(url);
}

export function remarkWikiLinks() {
  return (tree, file) => {
    const filePath = file?.history?.[0] ?? file?.path;
    if (!filePath) return;
    const pageDir = path.dirname(path.relative(CONTENT, filePath));

    const resolve = (url) => {
      const [rawTarget, hash] = url.split('#');
      const target = decodeURI(rawTarget);
      let abs = '/' + path.posix.normalize(path.posix.join(pageDir, target));
      abs = abs.replace(/\/index\.md$/, '/').replace(/\.md$/, '/');
      return encodeURI(abs) + (hash ? '#' + hash : '');
    };

    walk(tree, (node) => {
      if ((node.type === 'link' || node.type === 'image' || node.type === 'definition')
          && !isExternal(node.url)) {
        node.url = resolve(node.url);
      }
      // Bilder und Links, die als reines HTML im Markdown stehen
      if (node.type === 'html' && node.value) {
        node.value = node.value.replace(
          /(<(?:img|a)\b[^>]*?\s(?:src|href)=")([^"]+)(")/gi,
          (m, pre, url, post) => (isExternal(url) ? m : pre + resolve(url) + post));
      }
    });
  };
}
