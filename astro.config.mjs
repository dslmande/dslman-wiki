// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { remarkWikiLinks } from './tools/remark-wiki-links.mjs';
import { rehypeMedia } from './tools/rehype-media.mjs';

export default defineConfig({
  site: 'https://dsl-man.de',
  // Die Anhänge liegen neben ihren Seiten in content/ und werden von dort
  // unverändert ausgeliefert. tools/postbuild.mjs räumt die mitkopierten
  // Markdown-Quellen anschließend wieder aus dist/.
  publicDir: './content',
  trailingSlash: 'always',
  build: { format: 'directory' },
  integrations: [sitemap()],
  markdown: {
    remarkPlugins: [remarkWikiLinks],
    rehypePlugins: [rehypeMedia],
    shikiConfig: { themes: { light: 'github-light', dark: 'github-dark' } },
  },
});
