/*
 * study-desk.js — reader-anchored Passage Study Desk.
 *
 * Toggling "📖 Study" opens a right-hand panel (~50% on desktop, a drawer on mobile) that
 * breaks down the passage currently in the reader — composed entirely from existing data,
 * no new authoring. The desk is the primary study surface: study comes to you, scoped to
 * the passage, instead of flinging you to a separate single-verse page.
 *
 * Sections (each COLLAPSIBLE; collapsed state persisted in localStorage bsw_study_collapsed):
 *   • Outline      — pericope headings from data/paragraphs/{book}.json; click → scroll.
 *   • Speakers     — who speaks across the chapter (paragraph breaks[].speaker), with ranges.
 *   • Key words    — repeated original-language terms in the range (interlinear + Strong's).
 *   • Where & when — an ALWAYS-AVAILABLE book-context map (even with no passage location data):
 *                    the book's composition (author / when / where written), the regional
 *                    powers of its period (empire polygons interpolated at the era's timeline
 *                    position), the landmarks the book discusses, and the passage's own places
 *                    highlighted. If a passage spans multiple eras (via the event index) one
 *                    annotated map is rendered per period.
 *   • Connections  — aggregated cross-references + OT→NT echoes; echoes use the reader's exact
 *                    collapsible card UI, grouped + annotated per verse.
 *   • Notes        — passage-scoped notes (localStorage) + "Export study sheet" (Markdown).
 *   • Range scope  — restrict the aggregating sections to a verse sub-range of the chapter.
 *
 * DATA: data/paragraphs, data/interlinear, data/strongs, data/maps/places.json, data/crossrefs,
 *   data/echoes (via core.js loaders), plus three study-context files:
 *     data/study/book-context.json  — per-book author/when/where-written + settingEra/settingT
 *     data/study/book-places.json   — per-book landmark place ids (generated from the text)
 *     data/study/era-powers.json    — eras + empire polygons/opacity-stages + event→ref index
 *   (regenerate the latter three via scripts/generate-book-context.py / -book-places.py /
 *    -era-powers.py). Leaflet is lazy-loaded from unpkg ONLY when a map is shown — it is not
 *   on the reader page otherwise; _ensureLeaflet waits for the stylesheet too, or the map
 *   panes are unpositioned and render blank.
 * VERIFY: Open /read/, load Romans 1, "📖 Study" → "Where & when" shows "Written from Corinth
 *   …", the Roman Empire shaded, Rome/Jerusalem landmark dots, and a powers legend — even
 *   though Romans 1 names no place. Load Matthew 4 → Roman-era map with Capernaum/Nazareth.
 *   Collapse a section → it stays collapsed after navigating chapters.
 */

import {
  loadInterlinear, loadStrongs, loadCrossRefs, loadEchoes, loadLexicon, loadCommentary, parseRef, WORD_URL
} from './core.js';
import { wireRefLinks } from './wire.js';
import { renderEchoCardsGrouped } from './parallels.js';

var _PARA_URL   = new URL('../../data/paragraphs/', import.meta.url).href;
var _PLACES_URL = new URL('../../data/maps/places.json', import.meta.url).href;
var _CTX_URL    = new URL('../../data/study/book-context.json', import.meta.url).href;
var _BPLACE_URL = new URL('../../data/study/book-places.json', import.meta.url).href;
var _POWERS_URL = new URL('../../data/study/era-powers.json', import.meta.url).href;
var _JOURNEY_URL = new URL('../../data/study/journeys.json', import.meta.url).href;
var _REFS_URL    = new URL('../../data/strongs/refs/', import.meta.url).href;
var _INTRO_URL   = new URL('../../data/books/introductions/', import.meta.url).href;
var _SYNTH_URL   = new URL('../../data/synthesis/', import.meta.url).href;

// Leaflet basemap config — mirrors maps.js so the desk map looks like the maps page.
var _TILE_URL  = 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';
var _TILE_ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>';

var _btn = null, _deskEl = null, _bodyEl = null, _observer = null;
var _open = false;
var _curKey = null;          // "bookId:ch" last rendered
var _paraCache = Object.create(null);
var _placesCache = null, _ctxCache = null, _bplaceCache = null, _powersCache = null, _journeyCache = null;
var _placeMaps = [];         // [{map, bounds}] — every Leaflet instance in the desk (destroy on re-render)
var _leafletPromise = null;

// Range scope: which verses the aggregating sections cover. Reset to the full chapter on
// every chapter change; narrowed by the range control without a full re-render.
var _rangeFrom = 1, _rangeTo = 0, _maxV = 0;

// Snapshot each section computed, so "Export study sheet" can assemble Markdown without
// recomputing.
var _lastData = { ref: '', outline: [], speakers: [], keywords: [], places: [], powers: [], context: null, xrefs: [], echoes: [] };

var _COLLAPSE_KEY = 'bsw_study_collapsed';

var _SPEAKER_LABELS = {
  narrative: 'Narrator', jesus: 'Jesus', god: 'God', john: 'John', peter: 'Peter',
  paul: 'Paul', crowd: 'The Crowd', disciples: 'Disciples', pharisees: 'Pharisees',
  scribes: 'Scribes', sadducees: 'Sadducees', pilate: 'Pilate', herod: 'Herod',
  angels: 'Angels', questioner: 'Questioner', mary: 'Mary', martha: 'Martha',
  satan: 'Satan', serpent: 'The Serpent', job: 'Job', psalmist: 'The Psalmist',
  wisdom: 'Lady Wisdom', teacher: 'The Teacher'
};
function _speakerLabel(s) { return _SPEAKER_LABELS[s] || (s ? s.charAt(0).toUpperCase() + s.slice(1) : 'Narrator'); }
function _speakerClass(s) {
  if (s === 'jesus') return 'reader-speaker-chip--jesus';
  if (s === 'god')   return 'reader-speaker-chip--god';
  return 'reader-speaker-chip--named';
}
function _esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
  return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

// ── small data loaders ─────────────────────────────────────────────────────
function _loadJSON(url, getCache, setCache) {
  var c = getCache();
  if (c) return Promise.resolve(c);
  return fetch(url).then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { setCache(d || {}); return getCache(); })
    .catch(function () { setCache({}); return getCache(); });
}
function _loadPara(bookId) {
  if (_paraCache[bookId]) return Promise.resolve(_paraCache[bookId]);
  return fetch(_PARA_URL + bookId + '.json').then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { _paraCache[bookId] = d || {}; return _paraCache[bookId]; })
    .catch(function () { _paraCache[bookId] = {}; return {}; });
}
function _loadPlaces()    { return _loadJSON(_PLACES_URL, function(){return _placesCache;}, function(v){_placesCache=Array.isArray(v)?v:[];}); }
function _loadCtx()       { return _loadJSON(_CTX_URL,    function(){return _ctxCache;},    function(v){_ctxCache=v;}); }
function _loadBookPlaces(){ return _loadJSON(_BPLACE_URL, function(){return _bplaceCache;}, function(v){_bplaceCache=v;}); }
function _loadPowers()    { return _loadJSON(_POWERS_URL, function(){return _powersCache;}, function(v){_powersCache=v;}); }
function _loadJourneys()  { return _loadJSON(_JOURNEY_URL, function(){return _journeyCache;}, function(v){_journeyCache=v;}); }

var _refsCache = Object.create(null), _introCache = Object.create(null);
function _loadRefs(code) {
  var k = code.toLowerCase();
  if (_refsCache[k]) return Promise.resolve(_refsCache[k]);
  return fetch(_REFS_URL + k + '.json').then(function (r) { return r.ok ? r.json() : {}; })
    .then(function (d) { _refsCache[k] = d || {}; return _refsCache[k]; })
    .catch(function () { _refsCache[k] = {}; return {}; });
}
function _loadIntro(bookId) {
  if (_introCache[bookId]) return Promise.resolve(_introCache[bookId]);
  return fetch(_INTRO_URL + bookId + '.json').then(function (r) { return r.ok ? r.json() : {}; })
    .then(function (d) { _introCache[bookId] = d || {}; return _introCache[bookId]; })
    .catch(function () { _introCache[bookId] = {}; return {}; });
}
var _synthCache = Object.create(null);
function _loadSynthesis(bookId, ch) {
  var k = bookId + ':' + ch;
  if (_synthCache[k]) return Promise.resolve(_synthCache[k]);
  return fetch(_SYNTH_URL + bookId + '/' + ch + '.json').then(function (r) { return r.ok ? r.json() : {}; })
    .then(function (d) { _synthCache[k] = d || {}; return _synthCache[k]; })
    .catch(function () { _synthCache[k] = {}; return {}; });
}

// ── verse helpers ──────────────────────────────────────────────────────────
function _maxVerse() {
  var max = 0;
  document.querySelectorAll('#reader-results .reader-verse[data-v]').forEach(function (el) {
    if (el.closest('.reader-compare-cell')) return;
    var v = parseInt(el.getAttribute('data-v'), 10);
    if (v > max) max = v;
  });
  return max;
}
function _inRange(v) { return v >= _rangeFrom && v <= _rangeTo; }
function _scrollToVerse(v) {
  var el = document.querySelector('#reader-results .reader-verse[data-v="' + v + '"]:not(.reader-compare-cell)');
  if (el) {
    el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    el.classList.add('reader-verse--study-flash');
    setTimeout(function () { el.classList.remove('reader-verse--study-flash'); }, 1400);
  }
}

// ── collapsible section shell ──────────────────────────────────────────────
// INTENT: Every section is a collapsible panel whose open/closed state survives navigation
//   (persisted per section id in localStorage bsw_study_collapsed). Async fillers target the
//   inner body div by id; the shell renders even before its content arrives.
// CHANGE? Body ids (sd-outline … sd-notes) are the contract between _render and the fillers.
//   Toggle wiring lives in _wireToggles; expanding sd-maps must invalidateSize() the maps
//   (they may have initialised while hidden, i.e. zero-size).
// VERIFY: Collapse "Key words", navigate to another chapter — it stays collapsed.
function _collapsedMap() { try { return JSON.parse(localStorage.getItem(_COLLAPSE_KEY) || '{}') || {}; } catch (e) { return {}; } }
function _setCollapsed(id, on) {
  var c = _collapsedMap();
  if (on) c[id] = 1; else delete c[id];
  try { localStorage.setItem(_COLLAPSE_KEY, JSON.stringify(c)); } catch (e) {}
}
function _sectionShell(id, title) {
  var isC = !!_collapsedMap()[id];
  return '<section class="study-section" data-sec="' + id + '">' +
    '<button type="button" class="study-sec-toggle" aria-expanded="' + (isC ? 'false' : 'true') + '" aria-controls="' + id + '">' +
      '<span class="study-sec-chevron" aria-hidden="true">▾</span>' +
      '<span class="study-sec-title">' + _esc(title) + '</span></button>' +
    '<div class="study-sec-body" id="' + id + '"' + (isC ? ' hidden' : '') + '></div></section>';
}
function _wireToggles() {
  _bodyEl.querySelectorAll('.study-sec-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var sec = btn.closest('.study-section');
      var body = sec && sec.querySelector('.study-sec-body');
      if (!body) return;
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      body.hidden = open;
      _setCollapsed(body.id, open);
      // A Leaflet map sized while hidden renders blank; re-measure + re-fit on reveal.
      if (!open && body.id === 'sd-maps') {
        _placeMaps.forEach(function (pm) {
          if (!pm.map) return;
          pm.map.invalidateSize();
          if (pm.bounds) { try { pm.map.fitBounds(pm.bounds, { padding: [24, 24], maxZoom: 9 }); } catch (e) {} }
        });
      }
    });
  });
}

// ── Outline + Speakers ─────────────────────────────────────────────────────
function _fillOutline(headings, maxV) {
  var host = document.getElementById('sd-outline');
  _lastData.outline = [];
  if (!host) return;
  if (!headings || !headings.length) { host.innerHTML = '<p class="study-empty">No outline for this chapter.</p>'; return; }
  var nav = window._readerNavState || {};
  var rows = headings.map(function (h, i) {
    var start = h.before;
    var end = (i + 1 < headings.length) ? headings[i + 1].before - 1 : (maxV || start);
    var range = end > start ? (start + '–' + end) : String(start);
    _lastData.outline.push({ range: range, text: h.text });
    // Each row = a scroll-to button + a ✦ "section synthesis" button that opens the blade.
    return '<div class="study-outline__row">' +
      '<button type="button" class="study-outline__go" data-v="' + start + '">' +
        '<span class="study-outline__range">' + range + '</span>' +
        '<span class="study-outline__title">' + _esc(h.text) + '</span></button>' +
      '<button type="button" class="study-outline__synth" title="Section synthesis" aria-label="Section synthesis"' +
        ' data-v="' + start + '" data-range="' + _esc(range) + '" data-label="' + _esc(h.text) + '">✦</button>' +
      '</div>';
  }).join('');
  host.innerHTML = '<div class="study-outline">' + rows + '</div>';
  host.querySelectorAll('.study-outline__go').forEach(function (b) {
    b.addEventListener('click', function () { _scrollToVerse(b.getAttribute('data-v')); });
  });
  host.querySelectorAll('.study-outline__synth').forEach(function (b) {
    b.addEventListener('click', function () {
      openBlade('section-synthesis', {
        bookId: nav.bookId, bookName: nav.bookName || nav.bookId, ch: nav.ch,
        startV: b.getAttribute('data-v'),
        range: b.getAttribute('data-range'),
        label: b.getAttribute('data-label')
      }, '✦ ' + (b.getAttribute('data-label') || 'Synthesis'));
    });
  });
}
function _fillSpeakers(breaks, maxV) {
  var host = document.getElementById('sd-speakers');
  _lastData.speakers = [];
  if (!host) return;
  if (!breaks || !breaks.length) { host.innerHTML = '<p class="study-empty">No speaker data.</p>'; return; }
  var bySpeaker = Object.create(null), order = [];
  breaks.forEach(function (b, i) {
    var spk = b.speaker || 'narrative';
    var start = b.v;
    var end = (i + 1 < breaks.length) ? breaks[i + 1].v - 1 : (maxV || start);
    var range = end > start ? (start + '–' + end) : String(start);
    if (!bySpeaker[spk]) { bySpeaker[spk] = []; order.push(spk); }
    bySpeaker[spk].push(range);
  });
  if (order.length < 2) { host.innerHTML = '<p class="study-empty">One voice throughout.</p>'; return; }
  host.innerHTML = '<div class="study-speakers">' + order.map(function (spk) {
    _lastData.speakers.push({ label: _speakerLabel(spk), ranges: bySpeaker[spk].join(', ') });
    return '<div class="study-speaker">' +
      '<span class="reader-speaker-chip ' + _speakerClass(spk) + '">' + _esc(_speakerLabel(spk)) + '</span>' +
      '<span class="study-speaker__ranges">' + bySpeaker[spk].map(_esc).join(', ') + '</span></div>';
  }).join('') + '</div>';
}

// ── Key-word usage (interlinear + Strong's aggregation) ────────────────────
// INTENT: Only VERBS, NOUNS, and CONCEPTS are surfaced — grammatical function words (articles,
//   particles, prepositions, conjunctions, pronouns, the Hebrew object marker, etc.) are
//   dropped. The Strong's `deriv`/`def` text reliably self-describes function words ("the
//   definite article", "a primary particle/preposition", "relative pronoun"); _KW_EXCLUDE
//   catches the high-frequency ones whose deriv carries no such marker (e.g. G3756 οὐ, H3588 כִּי).
// CHANGE? If new function words slip through, add their codes to _KW_EXCLUDE or a phrase to
//   _KW_FN_RX. Keeping the copula (εἰμί/הָיָה) is deliberate — it is a verb.
// VERIFY: John 1 key words → λόγος/word, φῶς/light, etc. — no "the/and/in".
var _KW_EXCLUDE = new Set([
  // Greek articles, particles, conjunctions, prepositions, pronouns, negatives
  'G3588', 'G2532', 'G1161', 'G1063', 'G3756', 'G3361', 'G1722', 'G1519', 'G1537', 'G1909',
  'G4314', 'G2596', 'G3326', 'G575', 'G1223', 'G3767', 'G3754', 'G5613', 'G235', 'G3739',
  'G846', 'G3778', 'G1565', 'G2228', 'G3303', 'G5037', 'G4771', 'G1473', 'G2249', 'G5210',
  'G5100', 'G5101', 'G1487', 'G1437', 'G302', 'G1438', 'G3588',
  // Hebrew object marker, particles, prepositions, pronouns, quantifiers
  'H853', 'H834', 'H3605', 'H4480', 'H5921', 'H413', 'H3588', 'H518', 'H3808', 'H1571',
  'H3651', 'H2088', 'H1931', 'H859', 'H589', 'H5704', 'H5973', 'H4994', 'H6258', 'H3651',
  'H9999', 'H1961'  // H1961 הָיָה ("to be") excluded as low-content copula in aggregation
]);
var _KW_FN_RX = /\b(definite article|primary particle|primitive particle|particle of|primary preposition|primitive preposition|used as a preposition|relative pronoun|demonstrative pronoun|personal pronoun|primary pronoun|reflexive pronoun|interrogative pronoun|conjunction)\b/i;
// Scan ONLY `deriv` (what the word *is*), not `def` — `def` often *mentions* "the article"
// descriptively (e.g. H430 Elohim, H3220 sea), which would wrongly drop real nouns.
function _isFunctionWord(code, entry) {
  if (_KW_EXCLUDE.has(code)) return true;
  return _KW_FN_RX.test(((entry && entry.deriv) || '').toLowerCase());
}

// One collapsible key-word card: gloss row → expand for a definition preview + a button that
// opens the full word-study blade (lexicon + every occurrence) layered over the desk.
function _keywordCard(code, entry, gloss, count, lang) {
  var card = document.createElement('div');
  card.className = 'study-kw';
  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'study-kw__toggle';
  btn.setAttribute('aria-expanded', 'false');
  btn.innerHTML =
    '<span class="study-kw__chevron" aria-hidden="true">▾</span>' +
    '<span class="study-kw__lemma">' + _esc(entry.lemma || code) + '</span>' +
    (entry.translit ? '<span class="study-kw__translit">' + _esc(entry.translit) + '</span>' : '') +
    '<span class="study-kw__gloss">' + _esc(gloss) + '</span>' +
    '<span class="study-kw__count">×' + count + '</span>';
  var body = document.createElement('div');
  body.className = 'study-kw__body';
  body.hidden = true;
  body.innerHTML =
    (entry.def ? '<p class="study-kw__def">' + _esc(entry.def) + '</p>' : '') +
    (entry.deriv ? '<p class="study-kw__deriv">' + _esc(entry.deriv) + '</p>' : '') +
    '<button type="button" class="study-kw__open">Open word study (' + _esc(code) + ') →</button>';
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', open ? 'false' : 'true');
    body.hidden = open;
    card.classList.toggle('study-kw--open', !open);
  });
  var openBtn = body.querySelector('.study-kw__open');
  if (openBtn) openBtn.addEventListener('click', function () {
    openBlade('word-study', { code: code, lang: lang }, entry.lemma || code);
  });
  card.appendChild(btn); card.appendChild(body);
  return card;
}

function _fillKeywords(bookId, ch, key) {
  var host = document.getElementById('sd-keywords');
  if (!host) return;
  _lastData.keywords = [];
  host.innerHTML = '<p class="study-empty">Loading…</p>';
  loadInterlinear(bookId).then(function (data) {
    if (_curKey !== key || !host.isConnected) return;
    var chData = data && data[String(ch)];
    if (!chData) { host.innerHTML = '<p class="study-empty">No original-language data for this book.</p>'; return; }
    var counts = Object.create(null), lang = null;
    Object.keys(chData).forEach(function (vKey) {
      if (!_inRange(parseInt(vKey, 10))) return;
      (chData[vKey] || []).forEach(function (tok) {
        if (!tok || !tok.s) return;
        if (!lang) lang = (tok.s.charAt(0) === 'H') ? 'hebrew' : 'greek';
        if (!counts[tok.s]) counts[tok.s] = { count: 0, text: tok.text || '' };
        counts[tok.s].count++;
      });
    });
    var repeated = Object.keys(counts).filter(function (c) { return counts[c].count >= 2; });
    if (!repeated.length) { host.innerHTML = '<p class="study-empty">No repeated terms in this range.</p>'; return; }
    loadStrongs(lang || 'greek').then(function (dict) {
      if (_curKey !== key || !host.isConnected) return;
      var content = repeated.filter(function (code) { return !_isFunctionWord(code, dict && dict[code]); })
        .sort(function (a, b) { return counts[b].count - counts[a].count; }).slice(0, 25);
      if (!content.length) { host.innerHTML = '<p class="study-empty">No repeated content words in this range.</p>'; return; }
      host.innerHTML = '<p class="study-sec-note">' + (lang === 'hebrew' ? 'Hebrew' : 'Greek') +
        ' verbs, nouns &amp; concepts repeated here — tap to expand</p><div class="study-keywords"></div>';
      var wrap = host.querySelector('.study-keywords');
      content.forEach(function (code) {
        var entry = (dict && dict[code]) || {};
        var gloss = entry.gloss || counts[code].text || '';
        _lastData.keywords.push({ lemma: entry.lemma || '', translit: entry.translit || '', gloss: gloss, count: counts[code].count });
        wrap.appendChild(_keywordCard(code, entry, gloss, counts[code].count, lang));
      });
    });
  }).catch(function () { if (host.isConnected) host.innerHTML = '<p class="study-empty">Could not load.</p>'; });
}

// ── Place detection ────────────────────────────────────────────────────────
var _GENERIC_ALIASES = new Set([
  'the city', 'holy city', 'city of palms', 'the sea', 'the river', 'the lake',
  'the mount', 'the mountain', 'the wilderness', 'the valley', 'the desert',
  'the plain', 'the brook', 'the land', 'the gate', 'the well', 'the pool'
]);
var _termRegexCache = Object.create(null);
function _termRegex(term) {
  if (_termRegexCache[term]) return _termRegexCache[term];
  var rx = new RegExp('\\b' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b');
  _termRegexCache[term] = rx; return rx;
}
function _placeTerms(p) {
  return [p.name].concat((p.aliases || []).filter(function (a) { return !_GENERIC_ALIASES.has(a.toLowerCase()); }));
}
// Places named in the in-scope verses (case-sensitive word-boundary match). [{place, verses}]
function _detectPlaces(places) {
  var verses = [];
  document.querySelectorAll('#reader-results .reader-verse[data-v]').forEach(function (el) {
    if (el.closest('.reader-compare-cell')) return;
    var v = parseInt(el.getAttribute('data-v'), 10);
    if (!_inRange(v)) return;
    verses.push({ v: v, text: el.textContent || '' });
  });
  var found = [];
  places.forEach(function (p) {
    var terms = _placeTerms(p), hits = [];
    verses.forEach(function (vo) {
      if (terms.some(function (t) { return _termRegex(t).test(vo.text); })) hits.push(vo.v);
    });
    if (hits.length) found.push({ place: p, verses: hits });
  });
  return found;
}

// ── Regional powers (empire polygons) ──────────────────────────────────────
function _lerp(a, b, f) { return a + (b - a) * f; }
function _stageValue(stages, t) {
  if (!stages || !stages.length) return 0;
  if (t <= stages[0].t) return stages[0].o || 0;
  var last = stages[stages.length - 1];
  if (t >= last.t) return last.o || 0;
  for (var i = 0; i < stages.length - 1; i++) {
    var s0 = stages[i], s1 = stages[i + 1];
    if (t >= s0.t && t <= s1.t) return _lerp(s0.o || 0, s1.o || 0, (t - s0.t) / (s1.t - s0.t));
  }
  return 0;
}
// Empires "present" at timeline position t → [{label,color,coords,o}], strongest first.
function _powersAt(powers, t) {
  var out = [];
  (powers && powers.empires || []).forEach(function (emp) {
    var o = _stageValue(emp.stages, t);
    if (o > 0.04) out.push({ label: emp.label, color: emp.color, coords: emp.coords, o: o });
  });
  out.sort(function (a, b) { return b.o - a.o; });
  return out;
}
// Ray-casting point-in-polygon; coords are [[lat,lon],…].
function _pointInPoly(lat, lon, coords) {
  var inside = false;
  for (var i = 0, j = coords.length - 1; i < coords.length; j = i++) {
    var yi = coords[i][0], xi = coords[i][1], yj = coords[j][0], xj = coords[j][1];
    if (((yi > lat) !== (yj > lat)) && (lon < (xj - xi) * (lat - yi) / (yj - yi) + xi)) inside = !inside;
  }
  return inside;
}
// Which present power most tightly controls a point (highest opacity polygon containing it).
function _controllerOf(lat, lon, powersAtT) {
  var best = null;
  powersAtT.forEach(function (p) {
    if (_pointInPoly(lat, lon, p.coords) && (!best || p.o > best.o)) best = p;
  });
  return best ? best.label : null;
}

// ── Period detection from the event index ──────────────────────────────────
function _parseRefHead(s) {
  var m = /^([1-3]?\s?[A-Za-z][A-Za-z ]+?)\s+(\d+)(?::(\d+))?/.exec(String(s).trim());
  if (!m) return null;
  return { book: m[1].replace(/\s+/g, '').toLowerCase(), ch: parseInt(m[2], 10), v: m[3] ? parseInt(m[3], 10) : null };
}
// INTENT: Distinct time-periods a passage belongs to, from events whose PRIMARY ref (refs[0],
//   the event's own setting — not a cross-citation) falls in this chapter+range. Returns
//   [{era, t, year}] sorted by t; empty when no event is set here (caller then uses the
//   book's settingEra as a single fallback period). Primary-ref matching prevents a passage
//   that is merely *quoted* by an event (e.g. Isaiah cited in a Gospel event) from being
//   mis-dated to the quoting event's era.
// CHANGE? Reads era-powers.json events[].refs. settingT per era comes from book-context.json
//   for the fallback; the event's own t is used when matched.
// VERIFY: Genesis 12 → [Patriarchs]; Matthew 4 → [Life of Christ]; Romans 1 → [] (fallback to
//   The Early Church via book-context).
function _passagePeriods(powers, bookId, ch) {
  var byEra = Object.create(null), order = [];
  (powers && powers.events || []).forEach(function (ev) {
    var refs = ev.refs || [];
    if (!refs.length) return;
    var p = _parseRefHead(refs[0]);
    if (!p || p.book !== bookId || p.ch !== ch) return;
    if (p.v != null && !_inRange(p.v)) return;
    if (!byEra[ev.era]) { byEra[ev.era] = { era: ev.era, t: ev.t, year: ev.year, ts: [ev.t] }; order.push(ev.era); }
    else byEra[ev.era].ts.push(ev.t);
  });
  return order.map(function (era) {
    var e = byEra[era];
    e.t = e.ts.reduce(function (a, b) { return a + b; }, 0) / e.ts.length;  // mean t in this era
    return e;
  }).sort(function (a, b) { return a.t - b.t; });
}

// ── Leaflet lazy-load (waits for CSS too) ──────────────────────────────────
// INTENT: Load Leaflet (CSS + JS) from unpkg on first map use. The reader page does NOT ship
//   Leaflet. Critically resolves only after BOTH the stylesheet and script load — resolving on
//   the script alone leaves the map panes unpositioned (blank tiles), which is the "map isn't
//   rendering at all" bug. Caches the in-flight promise.
// CHANGE? Pin (leaflet@1.9.4) must match maps/index.html. If you bump it, change both URLs.
// VERIFY: First map in the desk → Network shows leaflet.css + leaflet.js once; the map tiles
//   actually paint. Switching chapters does not re-fetch them.
function _ensureLeaflet() {
  if (window.L) return Promise.resolve(window.L);
  if (_leafletPromise) return _leafletPromise;
  _leafletPromise = new Promise(function (resolve, reject) {
    var cssReady = false, jsReady = false, done = false;
    function maybe() { if (cssReady && jsReady && !done) { done = true; resolve(window.L); } }
    var link = document.getElementById('sd-leaflet-css');
    if (link && link.dataset.loaded) { cssReady = true; }
    else if (!link) {
      link = document.createElement('link');
      link.id = 'sd-leaflet-css'; link.rel = 'stylesheet';
      link.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css'; link.crossOrigin = '';
      link.onload = function () { link.dataset.loaded = '1'; cssReady = true; maybe(); };
      link.onerror = function () { cssReady = true; maybe(); };  // proceed; tiles may still paint
      document.head.appendChild(link);
    } else {
      link.addEventListener('load', function () { cssReady = true; maybe(); });
      cssReady = true;  // already in DOM, assume usable
    }
    var s = document.createElement('script');
    s.id = 'sd-leaflet-js'; s.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'; s.crossOrigin = '';
    s.onload = function () { jsReady = true; maybe(); };
    s.onerror = function () { _leafletPromise = null; reject(new Error('leaflet load failed')); };
    document.head.appendChild(s);
    // Safety: if CSS onload never fires (cached without event in some browsers), proceed.
    setTimeout(function () { cssReady = true; maybe(); }, 1500);
  });
  return _leafletPromise;
}
function _destroyMaps() {
  _placeMaps.forEach(function (pm) { try { pm.map.remove(); } catch (e) {} });
  _placeMaps = [];
}
function _centroid(coords) {
  var la = 0, lo = 0;
  coords.forEach(function (c) { la += c[0]; lo += c[1]; });
  return [la / coords.length, lo / coords.length];
}

// ── "Where & when" — book-context + regional-powers + landmark maps ────────
function _fillMaps(bookId, bookName, ch, key) {
  var host = document.getElementById('sd-maps');
  if (!host) return;
  _lastData.places = []; _lastData.powers = []; _lastData.context = null;
  host.innerHTML = '<p class="study-empty">Loading…</p>';
  Promise.all([_loadPlaces(), _loadCtx(), _loadBookPlaces(), _loadPowers(), _loadJourneys()]).then(function (res) {
    if (_curKey !== key || !host.isConnected) return;
    var places = res[0] || [], ctxAll = res[1] || {}, bplaceAll = res[2] || {}, powers = res[3] || {}, journeys = res[4] || {};
    var ctx = ctxAll[bookId] || null;
    var byId = Object.create(null);
    places.forEach(function (p) { byId[p.id] = p; });

    var detected = _detectPlaces(places);                 // passage places (range-scoped)
    var detectedIds = Object.create(null);
    detected.forEach(function (d) { detectedIds[d.place.id] = d.verses; });

    // Book landmarks (whole-book context), top 12, excluding ones already in the passage.
    var landmarks = (bplaceAll[bookId] || []).filter(function (h) { return !detectedIds[h.id] && byId[h.id]; }).slice(0, 12);

    // Periods: events set in this passage → one map each; else the book's setting era.
    var periods = _passagePeriods(powers, bookId, ch);
    if (!periods.length && ctx) periods = [{ era: ctx.settingEra, t: ctx.settingT, year: '', book: true }];
    if (!periods.length) periods = [{ era: null, t: null, year: '', book: true }];

    _lastData.context = ctx;

    // Composition header (always available — this is the "even with no location data" case).
    var html = '';
    if (ctx) {
      var w = ctx.writtenWhere;
      var sent = (ctx.sentTo && ctx.sentTo.length) ? ctx.sentTo.map(function (s) { return _esc(s.name); }).join(', ') : '';
      var conf = w ? _confTag(ctx.whereConfidence) : '';
      html += '<div class="study-ctx">' +
        '<div class="study-ctx__row"><span class="study-ctx__k">Author</span><span class="study-ctx__v">' + _esc(ctx.author) + '</span></div>' +
        '<div class="study-ctx__row"><span class="study-ctx__k">Written</span><span class="study-ctx__v">' + _esc(ctx.writtenWhen) + (w ? ' · ' + _esc(w.name) + conf : '') + '</span></div>' +
        (sent ? '<div class="study-ctx__row"><span class="study-ctx__k">Sent to</span><span class="study-ctx__v">' + sent + '</span></div>' : '') +
        '<div class="study-ctx__row"><span class="study-ctx__k">Setting</span><span class="study-ctx__v">' + _esc(ctx.settingEra) + '</span></div>' +
        (ctx.note ? '<p class="study-ctx__note">' + _esc(ctx.note) + '</p>' : '') +
        '</div>';
    }

    periods.forEach(function (p, idx) {
      var powersAtT = (p.t != null) ? _powersAt(powers, p.t) : [];
      if (idx === 0) _lastData.powers = powersAtT.map(function (x) { return x.label; });
      var annot = p.era
        ? ('<span class="study-era-dot" style="background:' + _esc(_eraColor(powers, p.era)) + '"></span>' +
           _esc(p.era) + (p.year ? ' · ' + _esc(p.year) : '') + (p.book ? ' (book setting)' : ''))
        : 'Map';
      var legend = powersAtT.length
        ? '<div class="study-powers">' + powersAtT.map(function (pw) {
            return '<span class="study-power"><span class="study-power__sw" style="background:' + _esc(pw.color) + '"></span>' + _esc(pw.label) + '</span>';
          }).join('') + '</div>'
        : '';
      // Journeys legend (Pauline epistles), only on the primary map.
      var jLegend = '';
      if (idx === 0 && ctx && ctx.journeys && ctx.journeys.length && journeys.paul) {
        var js = (journeys.paul.journeys || []).filter(function (j) { return ctx.journeys.indexOf(j.id) >= 0; });
        if (js.length) jLegend = '<div class="study-journeys">' + js.map(function (j) {
          return '<span class="study-journey"><span class="study-journey__line" style="background:' + _esc(j.color) + '"></span>' + _esc(j.label) + '</span>';
        }).join('') + '</div>';
      }
      html += '<div class="study-period">' +
        (periods.length > 1 ? '<h4 class="study-period__head">Period ' + (idx + 1) + '</h4>' : '') +
        '<div class="study-period__annot">' + annot + '</div>' +
        '<div class="study-map" id="sd-map-' + idx + '" role="img" aria-label="Map of regional powers and places"></div>' +
        legend + jLegend + '</div>';
    });

    host.innerHTML = html || '<p class="study-empty">No context available.</p>';

    _ensureLeaflet().then(function (L) {
      if (_curKey !== key || !host.isConnected) return;
      _destroyMaps();
      periods.forEach(function (p, idx) {
        _buildPeriodMap(L, idx, p, ctx, detected, landmarks, byId, powers, journeys);
      });
    }).catch(function () {
      host.querySelectorAll('.study-map').forEach(function (c) {
        c.outerHTML = '<p class="study-empty">Map unavailable (offline?).</p>';
      });
    });
  });
}

// Place-of-writing confidence → a small qualifier chip, so an inferred site isn't shown as fact.
var _CONF_LABEL = { explicit: 'stated', strong: 'strong tradition', probable: 'probable', uncertain: 'uncertain' };
function _confTag(conf) {
  var label = _CONF_LABEL[conf];
  if (!label || conf === 'explicit') return label ? ' <span class="study-conf study-conf--explicit">' + label + '</span>' : '';
  return ' <span class="study-conf study-conf--' + _esc(conf) + '">' + _esc(label) + '</span>';
}

function _eraColor(powers, era) {
  var e = (powers && powers.eras || []).find(function (x) { return x.id === era; });
  return e ? e.color : '#8c6a00';
}

function _buildPeriodMap(L, idx, period, ctx, detected, landmarks, byId, powers, journeys) {
  var container = document.getElementById('sd-map-' + idx);
  if (!container) return;
  var map = L.map(container, { zoomControl: true, attributionControl: true, scrollWheelZoom: false });
  L.tileLayer(_TILE_URL, { maxZoom: 19, attribution: _TILE_ATTR }).addTo(map);

  var powersAtT = (period.t != null) ? _powersAt(powers, period.t) : [];
  // Regional-power polygons (shaded "spheres of influence"), with a centred label.
  powersAtT.forEach(function (pw) {
    var fo = Math.min(pw.o, 0.4);
    L.polygon(pw.coords, {
      color: pw.color, weight: 1, fillColor: pw.color, fillOpacity: fo,
      opacity: Math.min(fo + 0.1, 0.5), dashArray: '5 4', interactive: false
    }).addTo(map);
    L.marker(_centroid(pw.coords), {
      interactive: false, keyboard: false,
      icon: L.divIcon({ className: 'study-power-label', html: '<span>' + _esc(pw.label) + '</span>', iconSize: [1, 1], iconAnchor: [0, 0] })
    }).addTo(map);
  });

  var latlngs = [];

  // Writer's journeys leading up to this letter (Pauline epistles) — drawn under the place
  // dots so the route reads as background. Waypoints are small dots with name tooltips.
  if (idx === 0 && ctx && ctx.journeys && ctx.journeys.length && journeys && journeys.paul) {
    var jmap = Object.create(null);
    (journeys.paul.journeys || []).forEach(function (j) { jmap[j.id] = j; });
    ctx.journeys.forEach(function (jid) {
      var j = jmap[jid];
      if (!j) return;
      var pts = j.path.map(function (p) { return [p[1], p[2]]; });
      L.polyline(pts, { color: j.color, weight: 2.5, opacity: 0.8 }).addTo(map);
      j.path.forEach(function (p) {
        L.circleMarker([p[1], p[2]], { radius: 3, color: j.color, weight: 1, fillColor: '#ffffff', fillOpacity: 1 })
          .bindTooltip(p[0], { direction: 'top', offset: [0, -4] }).addTo(map);
        latlngs.push([p[1], p[2]]);
      });
    });
  }

  function addDot(place, opts) {
    var ctrl = _controllerOf(place.lat, place.lon, powersAtT);
    var m = L.circleMarker([place.lat, place.lon], {
      radius: opts.radius, color: '#ffffff', weight: 2, fillColor: opts.fill, fillOpacity: 0.95
    });
    // HTML tooltip (like the maps page): name + scope/controller, then the place's one-line
    // significance from places.json `desc` so a hover is actually informative.
    var label = '<strong>' + _esc(place.name) + '</strong>' +
      (opts.verses ? ' · v' + opts.verses.join(', ') : '') +
      (ctrl ? ' · under ' + _esc(ctrl) : '') +
      (place.desc ? '<br><span class="study-map-tip__desc">' + _esc(place.desc) + '</span>' : '');
    m.bindTooltip(label, { permanent: false, direction: 'top', offset: [0, -6], className: 'study-map-tip' });
    m.addTo(map);
    latlngs.push([place.lat, place.lon]);
    if (idx === 0 && opts.verses) _lastData.places.push({ name: place.name, verses: opts.verses.slice(), under: ctrl });
  }
  // Passage places (gold, prominent).
  detected.forEach(function (d) { addDot(d.place, { radius: 6, fill: '#8c6a00', verses: d.verses }); });
  // Book landmarks (muted, smaller) for context.
  landmarks.forEach(function (h) { var p = byId[h.id]; if (p) addDot(p, { radius: 4, fill: '#b9a06a' }); });

  // Recipients — where the letter is addressed (Crete for Titus, the seven churches for
  // Revelation, etc.) — as distinct ✉ markers, only on the primary map.
  if (idx === 0 && ctx && ctx.sentTo) {
    ctx.sentTo.forEach(function (s) {
      L.marker([s.lat, s.lon], {
        icon: L.divIcon({ className: 'study-sent-marker', html: '✉', iconSize: [18, 18], iconAnchor: [9, 9] })
      }).bindTooltip('Sent to: ' + s.name, { direction: 'top', offset: [0, -8] }).addTo(map);
      latlngs.push([s.lat, s.lon]);
    });
  }

  // Place of writing — only on the first/primary map, as a distinct ✍ marker.
  if (idx === 0 && ctx && ctx.writtenWhere) {
    var w = ctx.writtenWhere;
    var cLabel = _CONF_LABEL[ctx.whereConfidence];
    var wTip = 'Written: ' + w.name + (cLabel && ctx.whereConfidence !== 'explicit' ? ' (' + cLabel + ')' : '');
    L.marker([w.lat, w.lon], {
      icon: L.divIcon({ className: 'study-write-marker', html: '✍', iconSize: [20, 20], iconAnchor: [10, 10] })
    }).bindTooltip(wTip, { direction: 'top', offset: [0, -8] }).addTo(map);
    latlngs.push([w.lat, w.lon]);
  }

  var bounds = null;
  if (latlngs.length === 1) { map.setView(latlngs[0], 7); }
  else if (latlngs.length > 1) { bounds = L.latLngBounds(latlngs); map.fitBounds(bounds, { padding: [24, 24], maxZoom: 9 }); }
  else if (powersAtT.length) { bounds = L.latLngBounds([].concat.apply([], powersAtT.map(function (p) { return p.coords; }))); map.fitBounds(bounds, { padding: [10, 10] }); }
  else { map.setView([31.5, 35.0], 6); }   // Holy Land default

  // The container was just inserted (and may have been hidden); settle size then re-fit.
  requestAnimationFrame(function () {
    map.invalidateSize();
    if (bounds) { try { map.fitBounds(bounds, { padding: [24, 24], maxZoom: 9 }); } catch (e) {} }
  });
  setTimeout(function () { map.invalidateSize(); }, 250);

  _placeMaps.push({ map: map, bounds: bounds });
}

// ── Connections (cross-refs + echoes mirroring the reader) ─────────────────
function _fillConnections(bookId, bookName, ch, key) {
  var host = document.getElementById('sd-connections');
  if (!host) return;
  _lastData.xrefs = []; _lastData.echoes = [];
  host.innerHTML = '<p class="study-empty">Loading…</p>';
  Promise.all([loadCrossRefs(bookId), loadEchoes(bookId)]).then(function (res) {
    if (_curKey !== key || !host.isConnected) return;
    var xrefData = res[0], echoData = res[1];
    host.innerHTML = '';

    // Cross-references: merge weights across the range, keep the strongest ~12.
    var xrefWeights = Object.create(null);
    var chX = xrefData && xrefData[String(ch)];
    if (chX) Object.keys(chX).forEach(function (vKey) {
      if (!_inRange(parseInt(vKey, 10))) return;
      (chX[vKey] || []).forEach(function (pair) { xrefWeights[pair[0]] = (xrefWeights[pair[0]] || 0) + (pair[1] || 1); });
    });
    var topX = Object.keys(xrefWeights).sort(function (a, b) { return xrefWeights[b] - xrefWeights[a]; }).slice(0, 12);
    if (topX.length) {
      _lastData.xrefs = topX.slice();
      var grp = document.createElement('div');
      grp.className = 'study-conn__group';
      grp.innerHTML = '<h4 class="study-conn__head">Cross-references</h4><div class="study-conn__refs">' +
        topX.map(function (t) { return '<a class="ref study-conn__ref" data-ref="' + _esc(t) + '">' + _esc(t) + '</a>'; }).join('') + '</div>';
      host.appendChild(grp);
    }

    // Echoes: the reader's exact collapsible cards, grouped + annotated per verse.
    var entries = [];
    var chE = echoData && echoData[String(ch)];
    if (chE) Object.keys(chE).forEach(function (vKey) {
      var v = parseInt(vKey, 10);
      if (!_inRange(v)) return;
      (chE[vKey] || []).forEach(function (e) {
        entries.push({ book: bookName, ch: ch, v: v, entry: e });
        _lastData.echoes.push((e.target || '') + (e.note ? ' — ' + e.note : ''));
      });
    });
    if (entries.length) {
      var eg = document.createElement('div');
      eg.className = 'study-conn__group';
      eg.innerHTML = '<h4 class="study-conn__head">Echoes &amp; allusions</h4>';
      host.appendChild(eg);
      renderEchoCardsGrouped(entries, eg);
    }

    if (!host.children.length) host.innerHTML = '<p class="study-empty">No connections for this range.</p>';
    wireRefLinks(host);
  }).catch(function () { if (host.isConnected) host.innerHTML = '<p class="study-empty">Could not load.</p>'; });
}

// ── Notes + export ─────────────────────────────────────────────────────────
function _notesKey(bookId, ch) { return 'bsw_study_notes_' + bookId + '_' + ch; }
function _fillNotes(bookId, ch) {
  var host = document.getElementById('sd-notes');
  if (!host) return;
  var k = _notesKey(bookId, ch), saved = '';
  try { saved = localStorage.getItem(k) || ''; } catch (e) {}
  host.innerHTML = '<textarea class="study-notes" id="sd-notes-ta" placeholder="Your notes on this passage…"></textarea>' +
    '<div class="study-export-row"><button type="button" class="study-export-btn" id="sd-export-btn">⬇ Export study sheet</button></div>';
  var ta = document.getElementById('sd-notes-ta');
  ta.value = saved;
  ta.addEventListener('input', function () { try { localStorage.setItem(k, ta.value); } catch (e) {} });
  var exp = document.getElementById('sd-export-btn');
  if (exp) exp.addEventListener('click', function () { _exportSheet(ta.value); });
}
function _buildSheet(notes) {
  var L = [], d = _lastData;
  L.push('# ' + (d.ref || 'Passage') + ' — Study Sheet', '');
  if (d.context) {
    var c = d.context;
    L.push('## Context');
    L.push('- **Author:** ' + c.author);
    L.push('- **Written:** ' + c.writtenWhen + (c.writtenWhere ? ' (' + c.writtenWhere.name + ')' : ''));
    if (c.sentTo && c.sentTo.length) L.push('- **Sent to:** ' + c.sentTo.map(function (s) { return s.name; }).join(', '));
    L.push('- **Setting:** ' + c.settingEra);
    if (c.note) L.push('- ' + c.note);
    L.push('');
  }
  if (d.powers.length) { L.push('## Regional powers of the period'); L.push(d.powers.join('; ')); L.push(''); }
  if (d.outline.length) { L.push('## Outline'); d.outline.forEach(function (o) { L.push('- **' + o.range + '** ' + o.text); }); L.push(''); }
  if (d.speakers.length) { L.push('## Speakers'); d.speakers.forEach(function (s) { L.push('- **' + s.label + '** — ' + s.ranges); }); L.push(''); }
  if (d.keywords.length) { L.push('## Key words'); d.keywords.forEach(function (w) { L.push('- ' + (w.lemma || '') + (w.translit ? ' (' + w.translit + ')' : '') + ' — ' + (w.gloss || '') + ' ×' + w.count); }); L.push(''); }
  if (d.places.length) { L.push('## Places'); d.places.forEach(function (p) { L.push('- ' + p.name + ' (v' + p.verses.join(', ') + ')' + (p.under ? ' — under ' + p.under : '')); }); L.push(''); }
  if (d.xrefs.length) { L.push('## Cross-references'); L.push(d.xrefs.join('; ')); L.push(''); }
  if (d.echoes.length) { L.push('## Echoes & allusions'); d.echoes.forEach(function (e) { L.push('- ' + e); }); L.push(''); }
  if (notes && notes.trim()) { L.push('## Notes'); L.push(notes.trim()); L.push(''); }
  return L.join('\n');
}
function _exportSheet(notes) {
  var md = _buildSheet(notes);
  var slug = (_lastData.ref || 'passage').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  var blob = new Blob([md], { type: 'text/markdown' });
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url; a.download = (slug || 'passage') + '-study.md';
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
}

// ── Range scope control ────────────────────────────────────────────────────
function _buildRangeControl() {
  var opts = function (sel) {
    var s = '';
    for (var i = 1; i <= _maxV; i++) s += '<option value="' + i + '"' + (i === sel ? ' selected' : '') + '>' + i + '</option>';
    return s;
  };
  return '<div class="study-range">' +
    '<span class="study-range__label">Scope</span>' +
    '<select class="study-range__sel" id="sd-range-from" aria-label="From verse">' + opts(_rangeFrom) + '</select>' +
    '<span class="study-range__dash">–</span>' +
    '<select class="study-range__sel" id="sd-range-to" aria-label="To verse">' + opts(_rangeTo) + '</select>' +
    '<button type="button" class="study-range__reset" id="sd-range-reset" title="Whole chapter">Whole ch.</button>' +
    '</div>';
}
function _wireRange(bookId, bookName, ch, key) {
  var from = document.getElementById('sd-range-from'), to = document.getElementById('sd-range-to'), reset = document.getElementById('sd-range-reset');
  function apply() {
    _rangeFrom = parseInt(from.value, 10) || 1;
    _rangeTo = parseInt(to.value, 10) || _maxV;
    if (_rangeFrom > _rangeTo) { _rangeTo = _rangeFrom; to.value = String(_rangeTo); }
    _refillScoped(bookId, bookName, ch, key);
  }
  if (from) from.addEventListener('change', apply);
  if (to) to.addEventListener('change', apply);
  if (reset) reset.addEventListener('click', function () {
    _rangeFrom = 1; _rangeTo = _maxV;
    if (from) from.value = '1'; if (to) to.value = String(_maxV);
    _refillScoped(bookId, bookName, ch, key);
  });
}
function _refillScoped(bookId, bookName, ch, key) {
  _destroyMaps();
  _fillKeywords(bookId, ch, key);
  _fillMaps(bookId, bookName, ch, key);
  _fillConnections(bookId, bookName, ch, key);
}

// ── Main render ────────────────────────────────────────────────────────────
function _render() {
  if (!_open || !_bodyEl) return;
  _destroyMaps();
  _closeBlades();   // the passage context changed; any open drill-down no longer applies
  var nav = window._readerNavState;
  if (!nav || !nav.bookId) {
    _bodyEl.innerHTML = '<p class="study-empty">Load a passage to study it.</p>';
    _setHeader('Passage Study');
    return;
  }
  var key = nav.bookId + ':' + nav.ch;
  _curKey = key;
  var bookName = nav.bookName || nav.bookId;
  var ref = bookName + ' ' + nav.ch;
  _lastData.ref = ref;
  _setHeader(ref);

  _maxV = _maxVerse() || 1;
  _rangeFrom = 1; _rangeTo = _maxV;

  _loadPara(nav.bookId).then(function (data) {
    if (_curKey !== key) return;
    var chData = data && data[String(nav.ch)];

    _bodyEl.innerHTML =
      '<button type="button" class="study-bookbtn" id="sd-book-btn">📖 About ' + _esc(bookName) + ' — book details →</button>' +
      (_maxV > 1 ? _buildRangeControl() : '') +
      _sectionShell('sd-outline', 'Outline') +
      _sectionShell('sd-speakers', 'Speakers') +
      _sectionShell('sd-keywords', 'Key words') +
      _sectionShell('sd-maps', 'Where & when') +
      _sectionShell('sd-connections', 'Connections') +
      _sectionShell('sd-notes', 'Notes');

    var bookBtn = document.getElementById('sd-book-btn');
    if (bookBtn) bookBtn.addEventListener('click', function () {
      openBlade('book-details', { bookId: nav.bookId, bookName: bookName }, bookName);
    });
    _wireToggles();
    _wireRange(nav.bookId, bookName, nav.ch, key);
    _fillOutline(chData && chData.headings, _maxV);
    _fillSpeakers(chData && chData.breaks, _maxV);
    _fillNotes(nav.bookId, nav.ch);
    _refillScoped(nav.bookId, bookName, nav.ch, key);
  });
}

function _setHeader(text) {
  var h = _deskEl && _deskEl.querySelector('.study-desk__ref');
  if (h) h.textContent = text;
}

var _obsTimer = null;
function _armObserver() {
  if (_observer) return;
  var results = document.getElementById('reader-results');
  if (!results) return;
  _observer = new MutationObserver(function () {
    if (!_open) return;
    clearTimeout(_obsTimer);
    _obsTimer = setTimeout(function () {
      if (!_open) return;
      var nav = window._readerNavState;
      var key = nav && nav.bookId ? (nav.bookId + ':' + nav.ch) : null;
      if (key !== _curKey) _render();   // only on a genuine chapter change
    }, 140);
  });
  _observer.observe(results, { childList: true });
}
function _disarmObserver() { if (_observer) { _observer.disconnect(); _observer = null; } }

function _setOpen(on) {
  _open = on;
  var layout = document.querySelector('.reader-layout');
  if (layout) layout.classList.toggle('reader-layout--study-open', on);
  if (_btn) {
    _btn.classList.toggle('reader-study-btn--on', on);
    _btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  }
  if (on) { _armObserver(); _render(); } else { _disarmObserver(); _destroyMaps(); _closeBlades(); }
}

function _buildDesk() {
  var desk = document.createElement('aside');
  desk.id = 'reader-study-desk';
  desk.className = 'reader-study-desk';
  desk.setAttribute('aria-label', 'Passage study');
  desk.innerHTML =
    '<div class="study-desk__head">' +
      '<span class="study-desk__title">Passage Study</span>' +
      '<span class="study-desk__ref"></span>' +
      '<button class="study-desk__close" type="button" aria-label="Close study desk">✕</button>' +
    '</div>' +
    '<div class="study-desk__body"></div>' +
    '<div class="study-blade" id="sd-blade">' +
      '<div class="study-blade__head">' +
        '<button class="study-blade__back" type="button" aria-label="Back">‹</button>' +
        '<nav class="study-blade__crumbs" aria-label="Breadcrumb"></nav>' +
        '<button class="study-blade__close" type="button" aria-label="Close pane">✕</button>' +
      '</div>' +
      '<div class="study-blade__body" id="sd-blade-body"></div>' +
    '</div>';
  _bodyEl = desk.querySelector('.study-desk__body');
  desk.querySelector('.study-desk__close').addEventListener('click', function () { _setOpen(false); });
  desk.querySelector('.study-blade__back').addEventListener('click', _bladeBack);
  desk.querySelector('.study-blade__close').addEventListener('click', _closeBlades);
  return desk;
}

// ════════════════════════════════════════════════════════════════════════════
// Blade stack — Azure-style drill-down panes layered over the desk. openBlade()
// pushes a pane; the TOP of the stack renders into #sd-blade-body, a breadcrumb
// walks back, and blades may open further blades. Cleared on chapter change / close.
// INTENT: Scale the study surface to deeper tools (word study, book details, later
//   commentary/fathers/biblepedia) without cramming the section list — each tool is a
//   registered render fn, not a rewrite of the desk.
// CHANGE? Register a tool by adding to _BLADES (type → render(params, bodyEl)). The overlay
//   (#sd-blade) is built in _buildDesk and covers the desk (sticky/fixed desk = containing
//   block for the absolute overlay). _closeBlades() must be called whenever the passage
//   context changes (see _render, _setOpen).
// VERIFY: Click a key word → word-study blade slides in, breadcrumb "Passage › λόγος", Back
//   returns to the sections; navigating chapters closes blades.
var _bladeStack = [];
var _BLADES = Object.create(null);

function openBlade(type, params, title) {
  if (!_BLADES[type] || !_deskEl) return;
  _bladeStack.push({ type: type, params: params || {}, title: title || type });
  _renderTopBlade();
}
function _bladeBack() { _bladeStack.pop(); if (_bladeStack.length) _renderTopBlade(); else _closeBlades(); }
function _bladeTo(level) {
  if (level <= 0) { _closeBlades(); return; }
  _bladeStack = _bladeStack.slice(0, level);
  if (_bladeStack.length) _renderTopBlade(); else _closeBlades();
}
function _closeBlades() {
  _bladeStack = [];
  if (_deskEl) _deskEl.classList.remove('reader-study-desk--blade');
  var b = document.getElementById('sd-blade-body');
  if (b) b.innerHTML = '';
}
function _renderTopBlade() {
  var body = document.getElementById('sd-blade-body');
  var crumbsEl = _deskEl && _deskEl.querySelector('.study-blade__crumbs');
  if (!body) return;
  _deskEl.classList.add('reader-study-desk--blade');
  if (_deskEl) _deskEl.scrollTop = 0;   // overlay aligns to the desk's visible top
  var crumbs = '<button type="button" class="study-blade__crumb" data-lvl="0">Passage</button>';
  _bladeStack.forEach(function (b2, i) {
    crumbs += '<span class="study-blade__sep" aria-hidden="true">›</span>' +
      '<button type="button" class="study-blade__crumb" data-lvl="' + (i + 1) + '"' +
      (i === _bladeStack.length - 1 ? ' aria-current="page"' : '') + '>' + _esc(b2.title) + '</button>';
  });
  if (crumbsEl) {
    crumbsEl.innerHTML = crumbs;
    crumbsEl.querySelectorAll('.study-blade__crumb').forEach(function (c) {
      c.addEventListener('click', function () { _bladeTo(parseInt(c.getAttribute('data-lvl'), 10)); });
    });
  }
  var top = _bladeStack[_bladeStack.length - 1];
  body.innerHTML = '<p class="study-empty">Loading…</p>';
  _BLADES[top.type](top.params, body);
}

// ── Word-study blade ───────────────────────────────────────────────────────
function _refChip(r) { return '<a class="ref study-word__ref" data-ref="' + _esc(r) + '">' + _esc(r) + '</a>'; }
function _renderWordStudyBlade(params, body) {
  var code = params.code;
  var lang = params.lang || (code && code.charAt(0) === 'H' ? 'hebrew' : 'greek');
  var lexType = (lang === 'hebrew') ? 'bdb' : 'thayer';
  Promise.all([
    loadStrongs(lang).catch(function () { return {}; }),
    loadLexicon(lexType).catch(function () { return {}; }),
    _loadRefs(code)
  ]).then(function (res) {
    var dict = res[0] || {}, lex = res[1] || {}, refsData = res[2] || {};
    var s = dict[code] || {}, lx = lex[code] || {};
    var lemma = s.lemma || lx.lemma || refsData.lemma || code;
    var translit = s.translit || lx.translit || refsData.translit || '';
    var gloss = s.gloss || refsData.gloss || '';
    var def = lx.long_def || lx.short_def || s.def || '';
    var refs = refsData.refs || [];
    var nav = window._readerNavState || {};
    var here = refs.filter(function (r) { var p = parseRef(r); return p && p.bookId === nav.bookId && String(p.ch) === String(nav.ch); });

    var html = '<div class="study-word">' +
      '<div class="study-word__lemma">' + _esc(lemma) + '</div>' +
      '<div class="study-word__sub">' +
        (translit ? '<span class="study-word__translit">' + _esc(translit) + '</span>' : '') +
        (lx.pronounce ? '<span class="study-word__pron">' + _esc(lx.pronounce) + '</span>' : '') +
        '<span class="study-word__code">' + _esc(code) + '</span></div>' +
      (gloss ? '<p class="study-word__gloss">' + _esc(gloss) + '</p>' : '') +
      (def ? '<div class="study-word__block"><h4>Definition</h4><p>' + _esc(def) + '</p></div>' : '') +
      (s.deriv ? '<p class="study-word__deriv">' + _esc(s.deriv) + '</p>' : '') +
      '</div>';

    html += '<div class="study-word__block"><h4>In this passage' + (here.length ? ' (' + here.length + ')' : '') + '</h4>' +
      (here.length ? '<div class="study-word__refs">' + here.map(_refChip).join('') + '</div>'
                   : '<p class="study-empty">No occurrences in this chapter.</p>') + '</div>';

    html += '<div class="study-word__block"><h4>All occurrences (' + (refsData.count || refs.length) + ')</h4>' +
      '<div class="study-word__refs" id="sd-word-all">' + refs.slice(0, 40).map(_refChip).join('') + '</div>' +
      (refs.length > 40 ? '<button type="button" class="study-word__more" id="sd-word-more">Show all ' + refs.length + '</button>' : '') + '</div>';

    html += '<a class="study-word__ext" target="_blank" rel="noopener" href="' +
      _esc(WORD_URL + '?s=' + encodeURIComponent(code)) + '">Open in Translation Workshop →</a>';

    body.innerHTML = html;
    var more = document.getElementById('sd-word-more');
    if (more) more.addEventListener('click', function () {
      document.getElementById('sd-word-all').innerHTML = refs.map(_refChip).join('');
      more.remove();
      wireRefLinks(body);
    });
    wireRefLinks(body);
  }).catch(function () { body.innerHTML = '<p class="study-empty">Could not load this word.</p>'; });
}

// ── Book-details blade ─────────────────────────────────────────────────────
function _bookSec(title, content) {
  return content ? '<div class="study-book__sec"><h4>' + _esc(title) + '</h4>' + content + '</div>' : '';
}
function _renderBookDetailsBlade(params, body) {
  var bookId = params.bookId;
  Promise.all([_loadIntro(bookId), _loadCtx()]).then(function (res) {
    var intro = res[0] || {}, ctx = (res[1] || {})[bookId] || null;
    var html = '<div class="study-book">';
    html += '<div class="study-book__title">' + _esc(intro.title || params.bookName || bookId) + '</div>';

    // Composition meta — intro fields, enriched with our book-context (powers/era, recipients).
    var rows = '';
    function row(k, v) { return v ? '<div class="study-ctx__row"><span class="study-ctx__k">' + _esc(k) + '</span><span class="study-ctx__v">' + v + '</span></div>' : ''; }
    rows += row('Author', _esc(intro.author || (ctx && ctx.author) || ''));
    rows += row('Date', _esc(intro.date || (ctx && ctx.writtenWhen) || ''));
    if (ctx && ctx.writtenWhere) rows += row('Written', _esc(ctx.writtenWhere.name) + _confTag(ctx.whereConfidence));
    if (ctx && ctx.sentTo && ctx.sentTo.length) rows += row('Sent to', ctx.sentTo.map(function (s) { return _esc(s.name); }).join(', '));
    if (ctx) rows += row('Setting era', _esc(ctx.settingEra));
    if (rows) html += '<div class="study-ctx">' + rows + '</div>';

    html += _bookSec('Setting', intro.setting ? '<p>' + _esc(intro.setting) + '</p>' : '');
    html += _bookSec('Purpose', intro.purpose ? '<p>' + _esc(intro.purpose) + '</p>' : '');
    if (intro.themes && intro.themes.length)
      html += _bookSec('Themes', '<ul class="study-book__list">' + intro.themes.map(function (t) { return '<li>' + _esc(t) + '</li>'; }).join('') + '</ul>');
    if (intro.outline && intro.outline.length)
      html += _bookSec('Outline', '<div class="study-book__outline">' + intro.outline.map(function (o) {
        return '<div class="study-book__orow"><span class="study-book__ochap">' + _esc(o.chapters || '') + '</span><span>' + _esc(o.label || '') + '</span></div>';
      }).join('') + '</div>');
    if (intro.key_verses && intro.key_verses.length)
      html += _bookSec('Key verses', intro.key_verses.map(function (k) {
        return '<div class="study-book__kv"><a class="ref" data-ref="' + _esc(k.ref) + '">' + _esc(k.ref) + '</a>' +
          (k.note ? '<span class="study-book__kvnote">' + _esc(k.note) + '</span>' : '') + '</div>';
      }).join(''));
    else if (intro.key_verse)
      html += _bookSec('Key verse', '<a class="ref" data-ref="' + _esc(intro.key_verse) + '">' + _esc(intro.key_verse) + '</a>');
    if (intro.key_people && intro.key_people.length)
      html += _bookSec('Key people', intro.key_people.map(function (p) {
        return '<div class="study-book__person"><strong>' + _esc(p.name) + '</strong>' + (p.role ? ' — ' + _esc(p.role) : '') + '</div>';
      }).join(''));
    html += _bookSec('Historical context', intro.context ? '<p>' + _esc(intro.context) + '</p>' : '');
    html += _bookSec('Christ connection', intro.christ_connection ? '<p>' + _esc(intro.christ_connection) + '</p>' : '');
    if (intro.themes_detail && intro.themes_detail.length)
      html += _bookSec('Themes in depth', intro.themes_detail.map(function (t) {
        return '<div class="study-book__td"><h5>' + _esc(t.title || '') + '</h5><p>' + _esc(t.text || '') + '</p></div>';
      }).join(''));

    if (!intro.title && !ctx) html += '<p class="study-empty">No details available for this book.</p>';
    html += '</div>';
    body.innerHTML = html;
    wireRefLinks(body);
  }).catch(function () { body.innerHTML = '<p class="study-empty">Could not load book details.</p>'; });
}

// ── Section-synthesis blade ────────────────────────────────────────────────
// INTENT: For a detected pericope, present the generated multi-domain synthesis (historical
//   context / literary structure / theological application / Christology + an integrative
//   summary) drawn across all commentary layers. Overlapping material (key terms, connections,
//   the fathers' full voices) is REFERENCED from the existing layers, not regenerated here.
// CHANGE? Data: data/synthesis/{book}/{ch}.json keyed by pericope start verse (see
//   scripts that generate it). Opened from the Outline rows (_fillOutline). Pilot coverage: John 1.
// VERIFY: Study desk → Outline → John 1 Prologue row → ✦ opens a blade with the four domain
//   cards and a "From the cloud of witnesses" reference listing the voices for vv.1–18.
// Find the synthesis section whose verse range CONTAINS the clicked heading's start verse.
// Synthesis units are literary pericopes (e.g. the whole Prologue 1–18) which may be COARSER
// than the reader's paragraph headings (1–13, 14–18) — so any heading row inside the range
// opens the same synthesis, decoupling synthesis granularity from heading granularity.
function _findSynthSection(data, startV) {
  startV = parseInt(startV, 10);
  var hit = null;
  Object.keys(data || {}).forEach(function (k) {
    var lo = parseInt(k, 10);
    var m = /(\d+)(?:-(\d+))?/.exec(String((data[k] && data[k].range) || k));
    var hi = (m && m[2]) ? parseInt(m[2], 10) : lo;
    if (startV >= lo && startV <= hi) hit = data[k];
  });
  return hit;
}

function _renderSectionSynthesisBlade(params, body) {
  var bookId = params.bookId, ch = params.ch, startV = params.startV;
  _loadSynthesis(bookId, ch).then(function (data) {
    if (!body.isConnected) return;
    var sec = _findSynthSection(data, startV);
    if (!sec) {
      body.innerHTML = '<p class="study-empty">No section synthesis for this passage yet.' +
        '<br><span class="study-sec-note">Pilot coverage: John 1.</span></p>';
      return;
    }
    var ref = (params.bookName || bookId) + ' ' + ch + ':' + (sec.range || startV);
    var html = '<div class="study-synth">' +
      '<div class="study-synth__label">' + _esc(sec.pericope_label || params.label || '') + '</div>' +
      '<div class="study-synth__ref">' + _esc(ref) +
        ' <span class="study-conf study-conf--probable">AI-assisted</span></div>' +
      (sec.synthesis ? '<div class="study-synth__intro">' + sec.synthesis + '</div>' : '');
    [['historical_context', 'Historical context'],
     ['literary_structure', 'Literary structure'],
     ['theological_application', 'Theological application'],
     ['christology', 'Christology']].forEach(function (d) {
      if (!sec[d[0]]) return;
      html += '<details class="study-synth__domain"><summary>' + _esc(d[1]) + '</summary>' +
        '<div class="study-synth__domain-body">' + sec[d[0]] + '</div></details>';
    });
    html += '<details class="study-synth__refs"><summary>From the cloud of witnesses (vv. ' +
      _esc(sec.range || startV) + ')</summary>' +
      '<div class="study-synth__refs-body" id="sd-synth-voices"><p class="study-empty">Loading…</p></div></details>';
    html += '</div>';
    body.innerHTML = html;
    wireRefLinks(body);

    var refsEl = body.querySelector('.study-synth__refs');
    var loaded = false;
    if (refsEl) refsEl.addEventListener('toggle', function () {
      if (!refsEl.open || loaded) return;
      loaded = true;
      _fillSynthVoices(bookId, ch, sec.range || String(startV));
    });
  });
}

// Reference panel: which voices the synthesis draws on across the range (names only, lightweight —
// the full text lives in the Cloud of Witnesses commentary source, which this references).
function _fillSynthVoices(bookId, ch, range) {
  var host = document.getElementById('sd-synth-voices');
  if (!host) return;
  var m = /^(\d+)(?:-(\d+))?/.exec(String(range));
  var lo = m ? parseInt(m[1], 10) : 1, hi = (m && m[2]) ? parseInt(m[2], 10) : lo;
  loadCommentary(bookId, 'cow', ch).then(function (data) {
    if (!host.isConnected) return;
    var chData = data && data[String(ch)];
    if (!chData) { host.innerHTML = '<p class="study-empty">No voices for this range.</p>'; return; }
    var names = Object.create(null);
    for (var v = lo; v <= hi; v++) {
      var h = chData[String(v)];
      if (!h) continue;
      var rx = /<strong>([^:<]+):<\/strong>/g, mm;
      while ((mm = rx.exec(h))) names[mm[1]] = 1;
    }
    var list = Object.keys(names);
    host.innerHTML = list.length
      ? '<p class="study-sec-note">Drawn from these voices across vv. ' + _esc(range) + ':</p>' +
        '<div class="study-synth__voices">' + list.map(function (n) {
          return '<span class="study-synth__voice-chip">' + _esc(n) + '</span>';
        }).join('') + '</div>' +
        '<p class="study-sec-note">Open the <strong>Cloud of Witnesses</strong> commentary on any verse to read them in full.</p>'
      : '<p class="study-empty">No voices for this range.</p>';
  }).catch(function () { host.innerHTML = '<p class="study-empty">Could not load voices.</p>'; });
}

_BLADES['word-study'] = _renderWordStudyBlade;
_BLADES['book-details'] = _renderBookDetailsBlade;
_BLADES['section-synthesis'] = _renderSectionSynthesisBlade;

export function initStudyDesk() {
  var browseBar = document.querySelector('.reader-browse-bar');
  var layout = document.querySelector('.reader-layout');
  if (!browseBar || !layout || document.getElementById('reader-study-btn')) return;

  _btn = document.createElement('button');
  _btn.id = 'reader-study-btn';
  _btn.className = 'reader-study-btn';
  _btn.type = 'button';
  _btn.textContent = '📖 Study';
  _btn.title = 'Open the passage study desk';
  _btn.setAttribute('aria-pressed', 'false');
  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(_btn, hint || null);
  _btn.addEventListener('click', function () { _setOpen(!_open); });

  _deskEl = _buildDesk();
  layout.appendChild(_deskEl);
}
