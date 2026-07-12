/* build-search-index.mjs — build-time inverted index for verse search (H5).
 *
 * The runtime verse search used to fetch all 66 books of the current version
 * (several MB) and scan linearly on every query — fine on broadband, sluggish
 * on phones. This emits a compact token → verse-id index for the DEFAULT
 * version (BSB), chunked by the token's first letter so a query downloads one
 * small file instead of the whole Bible. Non-indexed versions keep the legacy
 * book-loop scan (search.js falls back automatically).
 *
 * Output: dist/assets/search-index/BSB/<a-z|0>.json
 *   { "v": 1, "version": "BSB", "tokens": { "love": [id, Δ, Δ, …], … } }
 * Verse ids are (bookIdx << 16) | (ch << 8) | v — bookIdx in data/bible/
 * books.json order (the same order core.js bookOrder uses) — delta-encoded
 * ascending. Decoder: assets/js/search-index.js. Keep the two in sync.
 *
 * Run via npm run build (imported at the end of tools/build-assets.mjs).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DIST = path.join(ROOT, 'dist');
const VERSION = 'BSB';

const books = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/bible/books.json'), 'utf8'));

const postings = new Map();   // token → number[] (ascending verse ids; per-token dedupe)

books.forEach((book, bookIdx) => {
  const file = path.join(ROOT, 'data/bible', VERSION, `${book.id}.json`);
  if (!fs.existsSync(file)) return;
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  const chapters = data.chapters || {};
  for (const ch of Object.keys(chapters)) {
    for (const v of Object.keys(chapters[ch])) {
      const id = (bookIdx << 16) | (parseInt(ch, 10) << 8) | parseInt(v, 10);
      const text = String(chapters[ch][v])
        .replace(/<[^>]+>/g, ' ')
        .toLowerCase()
        .replace(/[‘’]/g, "'");
      const seen = new Set();
      for (const raw of text.split(/[^a-z']+/)) {
        const tok = raw.replace(/^'+|'+$/g, '');
        if (tok.length < 2 || seen.has(tok)) continue;
        seen.add(tok);
        let list = postings.get(tok);
        if (!list) postings.set(tok, (list = []));
        list.push(id);   // books/chapters/verses iterate in ascending order
      }
    }
  }
});

// Chunk by first letter; delta-encode each posting list.
const chunks = new Map();
for (const [tok, ids] of postings) {
  const key = /^[a-z]/.test(tok) ? tok[0] : '0';
  let chunk = chunks.get(key);
  if (!chunk) chunks.set(key, (chunk = {}));
  const deltas = new Array(ids.length);
  let prev = 0;
  for (let i = 0; i < ids.length; i++) { deltas[i] = ids[i] - prev; prev = ids[i]; }
  chunk[tok] = deltas;
}

const outDir = path.join(DIST, 'assets/search-index', VERSION);
fs.mkdirSync(outDir, { recursive: true });
let total = 0;
for (const [key, tokens] of chunks) {
  const json = JSON.stringify({ v: 1, version: VERSION, tokens });
  fs.writeFileSync(path.join(outDir, `${key}.json`), json);
  total += json.length;
}
console.log(`[search-index] ${VERSION}: ${postings.size} tokens, ${chunks.size} chunks, ${(total / 1024 / 1024).toFixed(1)} MB raw`);
