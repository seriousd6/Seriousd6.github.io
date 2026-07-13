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

// Damerau-ish edit distance capped at 2 — enough for "did you mean".
function _editDist(a, b) {
  if (Math.abs(a.length - b.length) > 2) return 3;
  var prev = [], cur = [];
  for (var j = 0; j <= b.length; j++) prev[j] = j;
  for (var i = 1; i <= a.length; i++) {
    cur = [i];
    var rowMin = i;
    for (var k = 1; k <= b.length; k++) {
      var cost = a[i - 1] === b[k - 1] ? 0 : 1;
      cur[k] = Math.min(prev[k] + 1, cur[k - 1] + 1, prev[k - 1] + cost);
      if (i > 1 && k > 1 && a[i - 1] === b[k - 2] && a[i - 2] === b[k - 1]) {
        cur[k] = Math.min(cur[k], prev[k - 1]);   // transposition ≈ 1 via substitution row
      }
      if (cur[k] < rowMin) rowMin = cur[k];
    }
    if (rowMin > 2) return 3;   // row minimum exceeds cap — bail
    prev = cur;
  }
  return prev[b.length];
}

// One word → { verseId: bestMatchWeight } across every token containing it
// or sharing its stem. Weights: exact 4, stem match 3, prefix 2, substring 1.
// Typo fallback: a word with NO matches at all retries as its closest token
// (edit distance ≤ 2, same first letter) and reports the correction via
// hits._corrected so the UI can say "showing results for …".
function _wordMatches(version, word) {
  var letter = /^[a-z]/.test(word) ? word[0] : '0';
  var qStem = stemWord(word);
  return _loadChunk(version, letter).then(function (tokens) {
    if (!tokens) return null;
    function collect(target, tStem) {
      var out = Object.create(null);
      var any = false;
      for (var tok in tokens) {
        var w;
        if (tok === target) w = 4;
        else if (stemWord(tok) === tStem) w = 3;
        else if (tok.indexOf(target) === 0) w = 2;
        else if (tok.indexOf(target) !== -1) w = 1;
        else continue;
        any = true;
        var ids = _decode(tokens[tok]);
        for (var i = 0; i < ids.length; i++) {
          if (!(out[ids[i]] >= w)) out[ids[i]] = w;
        }
      }
      return any ? out : null;
    }
    var hits = collect(word, qStem);
    if (hits) return hits;
    if (word.length < 4) return Object.create(null);
    // No token matched anywhere — assume a typo and take the closest token.
    var best = null, bestD = 3, bestN = 0;
    for (var tok2 in tokens) {
      var d = _editDist(word, tok2);
      var n = tokens[tok2].length;
      if (d < bestD || (d === bestD && n > bestN)) { best = tok2; bestD = d; bestN = n; }
    }
    if (!best || bestD > 2) return Object.create(null);
    var corrected = collect(best, stemWord(best)) || Object.create(null);
    corrected._corrected = best;
    return corrected;
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
        var corrections = [];
        maps.forEach(function (m, i) {
          if (!m) return;
          if (m._corrected && !group[i].syn) corrections.push({ from: group[i].w, to: m._corrected });
          var syn = group[i].syn;
          for (var idStr in m) {
            if (idStr === '_corrected') continue;
            var w = syn ? Math.max(1, Math.round(m[idStr] / 2)) : m[idStr];
            if (!(merged[idStr] >= w)) merged[idStr] = w;
          }
        });
        return { map: merged, corrections: corrections };
      });
  }

  return Promise.all(groups.map(groupMatches))
    .then(function (results) {
      var corrections = [];
      for (var m = 0; m < results.length; m++) {
        if (!results[m]) return null;   // fallback
        corrections = corrections.concat(results[m].corrections);
      }
      // AND-intersect: a verse must match every group; weight = sum.
      var out = [];
      var first = results[0].map;
      for (var idStr in first) {
        var weight = first[idStr];
        var ok = true;
        for (var j = 1; j < results.length; j++) {
          var w2 = results[j].map[idStr];
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
      out.corrections = corrections;   // "did you mean" info for the UI
      return out;
    });
}
