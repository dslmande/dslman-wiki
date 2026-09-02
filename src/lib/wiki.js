import { getCollection } from 'astro:content';

/** Normalisiert die Loader-ID auf den Seitenpfad ("space/seite", Space: "space"). */
function toPath(id) {
  return String(id).replace(/\/index$/, '').replace(/^index$/, '').replace(/^\/+|\/+$/g, '');
}

let cache;

/** Alle Wiki-Seiten mit Pfad, Segmenten und URL. */
export async function getPages() {
  if (cache) return cache;
  const entries = await getCollection('wiki');
  cache = entries
    .map((entry) => {
      const path = toPath(entry.id);
      const segments = path ? path.split('/') : [];
      return {
        entry,
        path,
        segments,
        url: '/' + (path ? path + '/' : ''),
        depth: segments.length,
        spaceSlug: segments[0] ?? '',
        title: entry.data.title,
      };
    })
    .sort((a, b) => a.path.localeCompare(b.path));
  return cache;
}

/** Ein Space je oberster Ebene, mit seiner Startseite und Seitenzahl. */
export async function getSpaces() {
  const pages = await getPages();
  const spaces = new Map();
  for (const page of pages) {
    if (!page.spaceSlug) continue;
    let space = spaces.get(page.spaceSlug);
    if (!space) {
      space = { slug: page.spaceSlug, url: `/${page.spaceSlug}/`, pages: [], home: null };
      spaces.set(page.spaceSlug, space);
    }
    space.pages.push(page);
    if (page.depth === 1) space.home = page;
  }
  for (const space of spaces.values()) {
    space.name = space.home?.entry.data.space || space.home?.title || space.slug;
    space.count = space.pages.length;
    space.updated = space.pages
      .map((p) => p.entry.data.updated || '')
      .sort()
      .at(-1);
  }
  return [...spaces.values()].sort((a, b) => a.name.localeCompare(b.name));
}

/** Baumstruktur der Seiten eines Space (ohne dessen Startseite). */
export async function getSpaceTree(spaceSlug) {
  const pages = await getPages();
  const inSpace = pages.filter((p) => p.spaceSlug === spaceSlug && p.depth > 1);
  const nodes = new Map(inSpace.map((p) => [p.path, { page: p, children: [] }]));
  const roots = [];
  for (const node of nodes.values()) {
    const parentPath = node.page.segments.slice(0, -1).join('/');
    const parent = nodes.get(parentPath);
    (parent ? parent.children : roots).push(node);
  }
  const sortTree = (list) => {
    list.sort((a, b) => a.page.title.localeCompare(b.page.title));
    list.forEach((n) => sortTree(n.children));
    return list;
  };
  return sortTree(roots);
}

/** Breadcrumb-Kette von der Startseite bis zur aktuellen Seite. */
export async function getTrail(page) {
  const pages = await getPages();
  const byPath = new Map(pages.map((p) => [p.path, p]));
  const trail = [];
  for (let i = 1; i <= page.segments.length; i++) {
    const found = byPath.get(page.segments.slice(0, i).join('/'));
    if (found) trail.push(found);
  }
  return trail;
}

/** Direkte Unterseiten – für die Kachelliste am Seitenende. */
export async function getChildren(page) {
  const pages = await getPages();
  return pages.filter(
    (p) => p.depth === page.depth + 1 && p.path.startsWith(page.path + '/'));
}
