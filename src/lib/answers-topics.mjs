// answers-topics.mjs — the single source for /answers/ topic lists, shared by
// the [slug] page and the letter index.
//
// Nave's Topical Bible ships 5,322 heads but ~650 are verse-less stubs
// (ANXIETY, ABETTING, …) — including some of the most-asked topics. For those,
// this module generates a verse list at build time by scanning the BSB text
// with the SAME matching the runtime search uses: light stemming plus the
// curated synonym table (assets/js/search-synonyms.js). Generated topics are
// flagged so the page can label its source honestly ("matched from the
// Berean Standard Bible text" vs "Nave's Topical Bible").
import fs from 'node:fs';
import { SYNONYMS } from '../../assets/js/search-synonyms.js';

// Keep in sync with stemWord in assets/js/search-index.js.
function stem(w) {
  if (w.length > 4 && /ies$/.test(w)) return w.slice(0, -3) + 'y';
  let s = w.replace(/(ing|ed|es|ly|s)$/, '');
  if (s.length < 3) s = w;
  return s.replace(/e$/, '');
}

const STOP = new Set(['the', 'and', 'of', 'in', 'to', 'for', 'with', 'a', 'an', 'or']);
const MIN_GENERATED = 3;   // fewer text matches than this → no page
const MAX_GENERATED = 40;  // cap a generated topic's verse list

let _cache = null;

export function buildAnswerTopics() {
  if (_cache) return _cache;
  const nave = JSON.parse(fs.readFileSync('./data/topical/nave.json', 'utf8'));
  const books = JSON.parse(fs.readFileSync('./data/bible/books.json', 'utf8'));

  // One pass over the BSB: stem → ordered list of "Book Ch:V" refs.
  const postings = new Map();
  for (const book of books) {
    const file = `./data/bible/BSB/${book.id}.json`;
    if (!fs.existsSync(file)) continue;
    const chapters = JSON.parse(fs.readFileSync(file, 'utf8')).chapters || {};
    for (const ch of Object.keys(chapters)) {
      for (const v of Object.keys(chapters[ch])) {
        const ref = `${book.name} ${ch}:${v}`;
        const text = String(chapters[ch][v]).replace(/<[^>]+>/g, ' ').toLowerCase().replace(/[‘’]/g, "'");
        const seen = new Set();
        for (const raw of text.split(/[^a-z']+/)) {
          const tok = raw.replace(/^'+|'+$/g, '');
          if (tok.length < 3) continue;
          const st = stem(tok);
          if (seen.has(st)) continue;
          seen.add(st);
          let list = postings.get(st);
          if (!list) postings.set(st, (list = []));
          list.push(ref);
        }
      }
    }
  }

  const refsForWord = (word) => {
    const alts = [word, ...(SYNONYMS[word] || [])];
    const out = new Set();
    for (const alt of alts) {
      const list = postings.get(stem(alt));
      if (list) for (const r of list) out.add(r);
    }
    return out;
  };

  const topics = [];
  for (const e of nave) {
    if ((e.verses || []).length > 0) {
      topics.push({ slug: e.slug, title: e.title, verses: e.verses, generated: false });
      continue;
    }
    // Verse-less stub: generate from the text. Multi-word titles AND their
    // significant words ("ABEL-SHITTIM" → abel ∧ shittim).
    const words = e.title.toLowerCase().split(/[^a-z]+/).filter(w => w.length >= 3 && !STOP.has(w));
    if (!words.length) continue;
    let refs = null;
    for (const w of words) {
      const set = refsForWord(w);
      refs = refs === null ? set : new Set([...refs].filter(r => set.has(r)));
      if (!refs.size) break;
    }
    if (!refs || refs.size < MIN_GENERATED) continue;
    topics.push({ slug: e.slug, title: e.title, verses: [...refs].slice(0, MAX_GENERATED), generated: true });
  }

  _cache = topics;
  return topics;
}
