import { getPages } from '../lib/wiki.js';

/** Kompakter Suchindex: Titel, Space, URL, Textanfang. */
export async function GET() {
  const pages = await getPages();
  const index = pages.map((page) => {
    const text = (page.entry.body || '')
      .replace(/```[\s\S]*?```/g, ' ')
      .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
      .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
      .replace(/[#>*_`|\\-]+/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
    return {
      t: page.title,
      p: page.entry.data.space || page.spaceSlug,
      u: page.url,
      b: text.slice(0, 1500).toLowerCase(),
      s: text.slice(0, 120) + '…',
    };
  });
  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json' },
  });
}
