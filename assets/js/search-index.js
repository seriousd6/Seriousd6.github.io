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

// Light stemmer (A3): enough to connect a query's inflection to the text's
// ("loving" ↔ "loved" ↔ "love") without a real morphology pass. Suffix
// strip + trailing-e drop; short words pass through.
export function stemWord(w) {
  if (w.length > 4 && /ies$/.test(w)) return w.slice(0, -3) + 'y';
  var s = w.replace(/(ing|ed|es|ly|s)$/, '');
  if (s.length < 3) s = w;
  return s.replace(/e$/, '');
}

// One word → { verseId: bestMatchWeight } across every token containing it
// or sharing its stem. Weights: exact 4, stem match 3, prefix 2, substring 1.
function _wordMatches(version, word) {
  var letter = /^[a-z]/.test(word) ? word[0] : '0';
  var qStem = stemWord(word);
  return _loadChunk(version, letter).then(function (tokens) {
    if (!tokens) return null;
    var hits = Object.create(null);
    for (var tok in tokens) {
      var w;
      if (tok === word) w = 4;
      else if (stemWord(tok) === qStem) w = 3;
      else if (tok.indexOf(word) === 0) w = 2;
      else if (tok.indexOf(word) !== -1) w = 1;
      else continue;
      var ids = _decode(tokens[tok]);
      for (var i = 0; i < ids.length; i++) {
        if (!(hits[ids[i]] >= w)) hits[ids[i]] = w;
      }
    }
    return hits;
  });
}

// groups: one entry per query word, each an array of alternatives
// [{ w: 'anxiety', syn: false }, { w: 'worry', syn: true }, …] — lowercase,
// length ≥ 2, apostrophes normalized (’ → '). Alternatives OR within a
// group (synonym weights halved); groups AND across.
// allowedBookIdx: Set of book indexes (testament/book filter), or null.
// Resolves [{id, bookIdx, ch, v, weight}] sorted by weight desc, or null
// when the index can't serve this query.
export function searchIndexLookup(version, groups, allowedBookIdx) {
  if (!INDEXED_VERSIONS[version]) return Promise.resolve(null);
  if (!groups.length) return Promise.resolve(null);

  function groupMatches(group) {
    return Promise.all(group.map(function (alt) { return _wordMatches(version, alt.w); }))
      .then(function (maps) {
        if (!maps[0]) return null;   // the primary word's chunk must load
        var merged = Object.create(null);
        maps.forEach(function (m, i) {
          if (!m) return;
          var syn = group[i].syn;
          for (var idStr in m) {
            var w = syn ? Math.max(1, Math.round(m[idStr] / 2)) : m[idStr];
            if (!(merged[idStr] >= w)) merged[idStr] = w;
          }
        });
        return merged;
      });
  }

  return Promise.all(groups.map(groupMatches))
    .then(function (maps) {
      for (var m = 0; m < maps.length; m++) if (!maps[m]) return null;   // fallback
      // AND-intersect: a verse must match every group; weight = sum.
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
