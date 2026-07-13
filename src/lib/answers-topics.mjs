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

// Curated openers for the modern-question topics: pure text-match ranking
// surfaces wrong-sense hits ("green or red depression" — mildew in walls,
// Leviticus 14) above the verses every pastor would actually name. Pinned
// refs lead the page (validated against the BSB before use); text matches
// fill the rest.
const PINNED = {
  anxiety:     ['Philippians 4:6', '1 Peter 5:7', 'Psalms 94:19', 'Matthew 6:34', 'John 14:27'],
  worry:       ['Matthew 6:25', 'Matthew 6:34', 'Philippians 4:6', '1 Peter 5:7', 'Luke 12:25'],
  depression:  ['Psalms 42:11', 'Psalms 34:18', 'Isaiah 41:10', 'Psalms 40:1', 'Matthew 11:28'],
  loneliness:  ['Genesis 2:18', 'Psalms 68:6', 'Hebrews 13:5', 'Psalms 25:16', 'Isaiah 41:10'],
  stress:      ['Matthew 11:28', 'Philippians 4:6', 'Psalms 55:22', 'John 14:27', 'Isaiah 26:3'],
  fear:        ['Isaiah 41:10', '2 Timothy 1:7', 'Psalms 34:4', 'Joshua 1:9', '1 John 4:18'],
  temptation:  ['1 Corinthians 10:13', 'James 1:12', 'Hebrews 4:15', 'Matthew 26:41'],
  patience:    ['James 1:3', 'Romans 12:12', 'Galatians 6:9', 'Psalms 27:14'],
  healing:     ['Psalms 147:3', 'James 5:16', 'Jeremiah 17:14', '1 Peter 2:24'],
  forgiveness: ['1 John 1:9', 'Ephesians 4:32', 'Colossians 3:13', 'Matthew 6:14'],
};

function rankWithPins(slug, refs, canon, max) {
  const pins = (PINNED[slug] || []).filter(r => canon.has(r));
  const pinSet = new Set(pins);
  const rest = [...refs.entries()]
    .filter(([r]) => !pinSet.has(r))
    .sort((a, b) => b[1] - a[1] || canon.get(a[0]) - canon.get(b[0]))
    .map(([r]) => r);
  return [...pins, ...rest].slice(0, max);
}
const MIN_GENERATED = 3;   // fewer text matches than this → no page
const MAX_GENERATED = 40;  // cap a generated topic's verse list

let _cache = null;

export function buildAnswerTopics() {
  if (_cache) return _cache;
  const nave = JSON.parse(fs.readFileSync('./data/topical/nave.json', 'utf8'));
  const books = JSON.parse(fs.readFileSync('./data/bible/books.json', 'utf8'));

  // One pass over the BSB: stem → ordered list of "Book Ch:V" refs.
  const postings = new Map();
  const canon = new Map();   // ref → canonical sequence, for rank tie-breaks
  for (const book of books) {
    const file = `./data/bible/BSB/${book.id}.json`;
    if (!fs.existsSync(file)) continue;
    const chapters = JSON.parse(fs.readFileSync(file, 'utf8')).chapters || {};
    for (const ch of Object.keys(chapters)) {
      for (const v of Object.keys(chapters[ch])) {
        const ref = `${book.name} ${ch}:${v}`;
        canon.set(ref, canon.size);
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

  // ref → weight: verses hit by the word itself outrank synonym-only hits.
  const refsForWord = (word) => {
    const out = new Map();
    const add = (alt, w) => {
      const list = postings.get(stem(alt));
      if (list) for (const r of list) { if (!(out.get(r) >= w)) out.set(r, w); }
    };
    add(word, 2);
    for (const syn of SYNONYMS[word] || []) add(syn, 1);
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
    let refs = null;   // Map ref → summed weight across words (AND)
    for (const w of words) {
      const m = refsForWord(w);
      if (refs === null) { refs = m; continue; }
      const next = new Map();
      for (const [r, w0] of refs) { const w1 = m.get(r); if (w1) next.set(r, w0 + w1); }
      refs = next;
      if (!refs.size) break;
    }
    if (!refs || refs.size < MIN_GENERATED) continue;
    // Curated pins first, then strongest matches (direct-word hits above
    // synonym-only), canonical order within a weight band.
    topics.push({ slug: e.slug, title: e.title, verses: rankWithPins(e.slug, refs, canon, MAX_GENERATED), generated: true });
  }

  // The synonym table names the modern questions people actually type
  // (depression, loneliness, stress, worry…) — most aren't Nave heads at
  // all. Any key without a topic gets a generated page too (adjective
  // variants excluded; their noun form owns the page).
  const VARIANT_KEYS = new Set(['anxious', 'afraid', 'wealth']);
  const have = new Set(topics.map(t => t.slug));
  for (const key of Object.keys(SYNONYMS)) {
    if (have.has(key) || VARIANT_KEYS.has(key)) continue;
    const refs = refsForWord(key);
    if (refs.size < MIN_GENERATED) continue;
    topics.push({ slug: key, title: key.toUpperCase(), verses: rankWithPins(key, refs, canon, MAX_GENERATED), generated: true });
  }

  _cache = topics;
  return topics;
}
