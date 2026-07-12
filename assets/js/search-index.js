/* search-index.js — client for the build-time verse search index (H5).
 *
 * tools/build-search-index.mjs emits /assets/search-index/<VERSION>/<a-z|0>.json
 * chunks of { token: [firstId, Δ, Δ, …] } with verse ids encoded
 * (bookIdx << 16) | (ch << 8) | v in data/bible/books.json order — the same
 * order core.js bookOrder uses. A query word downloads one letter chunk
 * (~100 KB) instead of the whole Bible; matching unions every token that
 * CONTAINS the word, preserving the legacy scan's substring semantics
 * ("love" still hits "loved" and "beloved").
 *
 * searchIndexLookup resolves null when it can't serve the query — version not
 * indexed, chunk fetch failed (offline / dev server without dist) — and the
 * caller (search.js) falls back to the legacy 66-book loop.
 */
'use strict';

import { _resolve } from './core.js';

var INDEXED_VERSIONS = { BSB: 1 };
var _chunks = Object.create(null);   // "BSB/l" → Promise<tokens|null>

function _loadChunk(version, letter) {
  var key = version + '/' + letter;
  if (_chunks[key]) return _chunks[key];
  _chunks[key] = fetch(_resolve('../search-index/' + version + '/' + letter + '.json'))
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (data) { return (data && data.tokens) || null; })
    .catch(function () { _chunks[key] = null; return null; });
  return _chunks[key];
}

function _decode(deltas) {
  var ids = new Array(deltas.length);
  var acc = 0;
  for (var i = 0; i < deltas.length; i++) { acc += deltas[i]; ids[i] = acc; }
  return ids;
}

export function decodeVerseId(id) {
  return { bookIdx: id >> 16, ch: (id >> 8) & 0xff, v: id & 0xff };
}

// One word → { verseId: bestMatchWeight } across every token containing it.
// Weights: exact token 4, token starts with the word 2, substring 1.
function _wordMatches(version, word) {
  var letter = /^[a-z]/.test(word) ? word[0] : '0';
  return _loadChunk(version, letter).then(function (tokens) {
    if (!tokens) return null;
    var hits = Object.create(null);
    for (var tok in tokens) {
      if (tok.indexOf(word) === -1) continue;
      var w = tok === word ? 4 : (tok.indexOf(word) === 0 ? 2 : 1);
      var ids = _decode(tokens[tok]);
      for (var i = 0; i < ids.length; i++) {
        if (!(hits[ids[i]] >= w)) hits[ids[i]] = w;
      }
    }
    return hits;
  });
}

// words: lowercase, length ≥ 2, apostrophes normalized (’ → ').
// allowedBookIdx: Set of book indexes (testament/book filter), or null for all.
// Resolves [{id, bookIdx, ch, v, weight}] sorted by weight desc, or null when
// the index can't serve this query.
export function searchIndexLookup(version, words, allowedBookIdx) {
  if (!INDEXED_VERSIONS[version]) return Promise.resolve(null);
  if (!words.length) return Promise.resolve(null);
  return Promise.all(words.map(function (w) { return _wordMatches(version, w); }))
    .then(function (maps) {
      for (var m = 0; m < maps.length; m++) if (!maps[m]) return null;   // fallback
      // AND-intersect: a verse must match every word; weight = sum.
      var out = [];
      var first = maps[0];
      for (var idStr in first) {
        var weight = first[idStr];
        var ok = true;
        for (var j = 1; j < maps.length; j++) {
          var w2 = maps[j][idStr];
          if (!w2) { ok = false; break; }
          weight += w2;
        }
        if (!ok) continue;
        var id = +idStr;
        if (allowedBookIdx && !allowedBookIdx.has(id >> 16)) continue;
        var d = decodeVerseId(id);
        out.push({ id: id, bookIdx: d.bookIdx, ch: d.ch, v: d.v, weight: weight });
      }
      out.sort(function (a, b) { return b.weight - a.weight || a.id - b.id; });
      return out;
    });
}
