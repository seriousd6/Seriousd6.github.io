/* sections.js — Topical / section-title search for the reader lookup bar.
 *
 * Searches the editorial section titles in data/sections-index.json (built by
 * scripts/build-section-index.py) plus a curated nickname map in
 * data/sections-aliases.json. A query like "parables", "parable of the sower",
 * or "beatitudes" resolves to the matching passages.
 *
 * Public API (used by reader.js doLookup):
 *   loadSectionData()                         → Promise (lazy fetch, cached)
 *   resolveAlias(query)                       → [refString,…] | null
 *   runSectionSearch(query, el, navigate)     → render results/suggestions into `el`,
 *                                               wiring clicks to navigate(refString)
 */
'use strict';

import { _resolve, escHtml } from './core.js';

var _IDX_URL   = _resolve('../../data/sections-index.json');
var _ALIAS_URL = _resolve('../../data/sections-aliases.json');
var _BODY_URL  = _resolve('../../data/sections-body.json');

var _sections  = null;   // array from sections-index.json
var _aliases   = null;   // { normalizedPhrase → { title, refs } }
var _body      = null;   // parallel-to-_sections array of body-keyword strings (Explore only)
var _ready     = null;   // shared load promise (index + aliases)
var _bodyReady = null;   // shared load promise (body keywords) — Explore only

// Normalize a query/title the same way on both sides so matching is stable.
function _norm(s) {
  return (s || '').toLowerCase()
    .replace(/[‘’'`".,!?;:()]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

// INTENT: Lazy-load the section index + alias map exactly once; resolve to empty
//   structures on failure so callers never reject (topical search just finds nothing).
// CHANGE? Both files are also precached in sw.js + listed in the offline manifest's
//   'bible' group; if you rename them, update those too.
// VERIFY: First topical query triggers one fetch each of sections-index.json /
//   sections-aliases.json; later queries hit the cache (no new requests).
export function loadSectionData() {
  if (_ready) return _ready;
  _ready = Promise.all([
    fetch(_IDX_URL).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; }),
    fetch(_ALIAS_URL).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })
  ]).then(function (res) {
    _sections = (res[0] && res[0].sections) || [];
    _aliases  = (res[1] && res[1].aliases)  || {};
    return true;
  });
  return _ready;
}

export function resolveAlias(query) {
  var a = _aliases && _aliases[_norm(query)];
  return a && a.refs ? a.refs.slice() : null;
}

// INTENT: Lazy-load the parallel body-keyword file (~1.3 MB) ONLY when Explore does a body
//   search — the reader's title search never calls this, so the reader stays lean.
// CHANGE? _body is index-aligned with _sections; both come from build-section-index.py. If the
//   build stops emitting them in the same order, body matches would map to the wrong section.
// VERIFY: First Explore section search fetches sections-body.json once; the reader lookup bar
//   never requests it.
export function loadSectionBody() {
  if (_bodyReady) return _bodyReady;
  _bodyReady = Promise.all([
    loadSectionData(),
    fetch(_BODY_URL).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })
  ]).then(function (res) { _body = (res[1] && res[1].body) || []; return true; });
  return _bodyReady;
}

function _key(s) { return s.book + '|' + s.ch + '|' + s.startV; }

// Explore-only: title/alias matches PLUS fuzzy body-text matches. Body match = every query
// token (≥3 chars) appears as a substring in the section's verse-keyword string (so "sow"
// also finds "sower"/"sowed"). Title matches rank first; body-only matches follow.
// Returns { title: [...], body: [...] }. Call loadSectionBody() first.
export function searchSectionsFull(query) {
  var titleHits = searchSections(query);
  var seen = {};
  titleHits.forEach(function (s) { seen[_key(s)] = true; });

  var toks = _norm(query).split(' ').filter(function (t) { return t.length >= 3; });
  var bodyHits = [];
  if (_body && _sections && toks.length) {
    for (var i = 0; i < _sections.length; i++) {
      var s = _sections[i];
      if (seen[_key(s)]) continue;
      var b = _body[i] || '';
      if (toks.every(function (t) { return b.indexOf(t) !== -1; })) bodyHits.push(s);
    }
  }
  return { title: titleHits, body: bodyHits };
}

// Score a section against a normalized query. Lower = better; -1 = no match.
function _score(sec, q) {
  var t = _norm(sec.title);
  if (t === q) return 0;
  if (t.indexOf(q) === 0) return 1;
  if (t.indexOf(q) !== -1) return 2;
  if (t.split(' ').some(function (w) { return w.indexOf(q) === 0; })) return 3;
  // category match: query names a group/tag (e.g. "parables", "miracles")
  var cats = [sec.group].concat(sec.tags || []);
  for (var i = 0; i < cats.length; i++) {
    var c = _norm(cats[i]);
    if (c === q || c.indexOf(q) !== -1 || (q.length >= 4 && q.indexOf(c) !== -1)) return 4;
  }
  // multi-word: every token present somewhere in the title
  var toks = q.split(' ').filter(Boolean);
  if (toks.length > 1 && toks.every(function (tok) { return t.indexOf(tok) !== -1; })) return 5;
  return -1;
}

// Data-only search: returns the matching section entries (ranked, all matches).
// Used by reader.js (renders into the lookup panel) and search.js (Explore "Sections").
export function searchSections(query) {
  var q = _norm(query);
  if (!q || !_sections) return [];
  var scored = [];
  for (var i = 0; i < _sections.length; i++) {
    var sc = _score(_sections[i], q);
    if (sc >= 0) scored.push({ s: _sections[i], sc: sc, i: i });
  }
  // index already in canonical order → stable sort keeps canonical tiebreak
  scored.sort(function (a, b) { return a.sc !== b.sc ? a.sc - b.sc : a.i - b.i; });
  return scored.map(function (o) { return o.s; });
}

// INTENT: Render all matches grouped by topic into `el`; clicking an item calls
//   navigate(ref) which the reader turns into a normal passage lookup. On no match,
//   show suggestion chips (the category groups) that re-run the search.
// CHANGE? Group order follows first-appearance in the (canonical) results. If the
//   sections-index schema changes (group/ref/title fields), update here.
// VERIFY: Type "parables" in the reader bar → a "Parables (20)" group lists every
//   parable; clicking "The Parable of the Sower" loads Mark 4:1-9.
export function runSectionSearch(query, el, navigate) {
  if (!el) return;
  el.innerHTML = '<p class="reader-hint">Searching sections…</p>';
  loadSectionData().then(function () {
    var matches = searchSections(query);
    if (!matches.length) { _renderSuggestions(el, navigate, query); return; }

    // group preserving canonical order of first appearance
    var order = [], byGroup = {};
    matches.forEach(function (s) {
      var g = s.group || 'Other Sections';
      if (!byGroup[g]) { byGroup[g] = []; order.push(g); }
      byGroup[g].push(s);
    });

    var html = '<div class="reader-sections">' +
      '<p class="reader-sec-summary">' + matches.length + ' section' + (matches.length !== 1 ? 's' : '') +
        ' for “' + escHtml(query) + '”</p>';
    order.forEach(function (g) {
      var items = byGroup[g];
      html += '<div class="reader-sec-group">' +
        '<div class="reader-sec-group__head">' + escHtml(g) + ' <span class="reader-sec-group__count">(' + items.length + ')</span></div>';
      items.forEach(function (s) {
        html += '<button type="button" class="reader-sec-item" data-ref="' + escHtml(s.ref) + '">' +
          '<span class="reader-sec-item__title">' + escHtml(s.title) + '</span>' +
          '<span class="reader-sec-item__ref">' + escHtml(s.ref) + '</span>' +
        '</button>';
      });
      html += '</div>';
    });
    html += '<p class="reader-sec-note">Section titles are editorial aids, not part of the inspired text.</p>' +
      '</div>';
    el.innerHTML = html;
    el.querySelectorAll('.reader-sec-item[data-ref]').forEach(function (btn) {
      btn.addEventListener('click', function () { navigate(btn.dataset.ref); });
    });
  });
}

function _renderSuggestions(el, navigate, query) {
  // Distinct category groups present in the corpus, as clickable starting points.
  var groups = [];
  var seen = {};
  (_sections || []).forEach(function (s) {
    var g = s.group;
    if (g && g !== 'Other Sections' && !seen[g]) { seen[g] = true; groups.push(g); }
  });
  var html = '<div class="reader-sections">' +
    '<p class="reader-sec-summary">No sections found for “' + escHtml(query) + '”.</p>' +
    '<p class="reader-sec-suggest-label">Try a category:</p>' +
    '<div class="reader-sec-chips">' +
    groups.map(function (g) {
      return '<button type="button" class="reader-sec-chip" data-q="' + escHtml(g) + '">' + escHtml(g) + '</button>';
    }).join('') +
    '</div>' +
    '<p class="reader-sec-suggest-label">…or a passage like “Parable of the Sower”, “Beatitudes”, “David and Goliath”.</p>' +
    '</div>';
  el.innerHTML = html;
  // Chips re-run the search for that category (capture navigate in closure).
  el.querySelectorAll('.reader-sec-chip[data-q]').forEach(function (btn) {
    btn.addEventListener('click', function () { runSectionSearch(btn.dataset.q, el, navigate); });
  });
}
