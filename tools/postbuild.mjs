/**
 * publicDir zeigt auf content/, damit die Anhänge direkt neben ihren Seiten
 * ausgeliefert werden. Dabei landen auch die Markdown-Quellen in dist/ – die
 * räumen wir hier wieder weg.
 */
import { readdir, rm } from 'node:fs/promises';
import path from 'node:path';

const dist = path.resolve('dist');
let removed = 0;

async function clean(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) await clean(full);
    else if (entry.name === 'index.md') { await rm(full); removed++; }
  }
}

await clean(dist);
console.log(`postbuild: ${removed} Markdown-Quellen aus dist/ entfernt`);
