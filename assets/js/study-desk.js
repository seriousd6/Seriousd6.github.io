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
 *    -era-powers.py). Leaflet is lazy-loaded (self-hosted vendor copy) ONLY when a map is shown — it is not
 *   on the reader page otherwise; _ensureLeaflet waits for the stylesheet too, or the map
 *   panes are unpositioned and render blank.
 * VERIFY: Open /read/, load Romans 1, "📖 Study" → "Where & when" shows "Written from Corinth
 *   …", the Roman Empire shaded, Rome/Jerusalem landmark dots, and a powers legend — even
 *   though Romans 1 names no place. Load Matthew 4 → Roman-era map with Capernaum/Nazareth.
 *   Collapse a section → it stays collapsed after navigating chapters.
 */

import { _resolve,
  loadInterlinear, loadStrongs, loadCrossRefs, loadEchoes, loadLexicon, loadCommentary, parseRef, WORD_URL,
  COMMENTARY_SOURCES, getCommentarySource, decorateCatena, loadMktAll, decorateMkt, loadBook, MAPS_URL
} from './core.js';
import { wireRefLinks } from './wire.js';
import { renderEchoCardsGrouped } from './parallels.js';

var _PARA_URL   = _resolve('../../data/paragraphs/');
var _PLACES_URL = _resolve('../../data/maps/places.json');
var _CTX_URL    = _resolve('../../data/study/book-context.json');
var _BPLACE_URL = _resolve('../../data/study/book-places.json');
var _POWERS_URL = _resolve('../../data/study/era-powers.json');
var _JOURNEY_URL = _resolve('../../data/study/journeys.json');
var _REFS_URL    = _resolve('../../data/strongs/refs/');
var _INTRO_URL   = _resolve('../../data/books/introductions/');
var _SYNTH_URL   = _resolve('../../data/synthesis/');
var _THEO_URL    = _resolve('../../data/study/theological-terms.json');  // Strong's code → weight (SD-T3)
var _TIMELINE_URL = _resolve('../../timeline/');             // timeline page (?era=id)
var _BP_URL      = _resolve('../../biblepedia/');            // article reader page (?a=slug)
var _BP_IDX_URL  = _resolve('../../data/biblepedia/index.json');
var _BP_ART_URL  = _resolve('../../data/biblepedia/articles/');

// Leaflet basemap config — mirrors maps.js so the desk map looks like the maps page.
var _TILE_URL  = 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';
var _TILE_ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>';

var _btn = null, _deskEl = null, _bodyEl = null, _observer = null;
var _open = false;
var _curKey = null;          // "bookId:ch" last rendered
var _paraCache = Object.create(null);
var _placesCache = null, _ctxCache = null, _bplaceCache = null, _powersCache = null, _journeyCache = null, _theoCache = null;
var _placeMaps = [];         // [{map, bounds}] — every Leaflet instance in the desk (destroy on re-render)
var _leafletPromise = null;

// Range scope: which verses the aggregating sections cover. Reset to the full chapter on
// every chapter change; narrowed by the range control without a full re-render.
var _rangeFrom = 1, _rangeTo = 0, _maxV = 0;

// Snapshot each section computed, so "Export study sheet" can assemble Markdown without
// recomputing.
var _lastData = { ref: '', outline: [], speakers: [], keywords: [], places: [], powers: [], context: null, xrefs: [], echoes: [], biblepedia: [] };

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
function _loadTheo()      { return _loadJSON(_THEO_URL,   function(){return _theoCache;},   function(v){_theoCache=v;}); }
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

// Biblepedia: one shared index (term + brief + key_refs per entry), articles fetched on demand.
// The index is ~1.7 MB so it's loaded once and cached for the session; per-article intros are
// fetched lazily only when a card is expanded (a chapter can key dozens of articles).
var _bpIdxCache = null, _bpArtCache = Object.create(null);
function _loadBPIndex() {
  if (_bpIdxCache) return Promise.resolve(_bpIdxCache);
  return fetch(_BP_IDX_URL).then(function (r) { return r.ok ? r.json() : []; })
    .then(function (d) { _bpIdxCache = Array.isArray(d) ? d : []; return _bpIdxCache; })
    .catch(function () { _bpIdxCache = []; return _bpIdxCache; });
}
function _loadBPArticle(id) {
  if (_bpArtCache[id]) return Promise.resolve(_bpArtCache[id]);
  return fetch(_BP_ART_URL + id + '.json').then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { _bpArtCache[id] = d || {}; return _bpArtCache[id]; })
    .catch(function () { _bpArtCache[id] = {}; return {}; });
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
  c[id] = on ? 1 : 0;   // store the explicit choice (incl. expand=0) so default-collapsed sections honour a user expand
  try { localStorage.setItem(_COLLAPSE_KEY, JSON.stringify(c)); } catch (e) {}
}
// defaultCollapsed applies only when the user has no stored preference for this section (e.g.
// the heavy Encyclopedia starts closed so its 1.7MB index isn't fetched until asked for).
function _sectionShell(id, title, defaultCollapsed) {
  var stored = _collapsedMap();
  var isC = Object.prototype.hasOwnProperty.call(stored, id) ? !!stored[id] : !!defaultCollapsed;
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
      // The Encyclopedia index is deferred until first expand (see _fillBiblepedia).
      if (!open && body.id === 'sd-biblepedia' && _bpPending && _bpLoadedKey !== _bpPending.key) {
        _bpLoad(_bpPending.bookId, _bpPending.ch, _bpPending.key);
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
    _lastData.outline.push({ range: range, text: h.text, startV: start });
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
      // Remember the chosen section so the Synthesis binder tab reopens it (SD-T1).
      _bladeCtx.section = {
        startV: b.getAttribute('data-v'),
        range: b.getAttribute('data-range'),
        label: b.getAttribute('data-label')
      };
      openBlade('section-synthesis', {
        bookId: nav.bookId, bookName: nav.bookName || nav.bookId, ch: nav.ch,
        startV: b.getAttribute('data-v'),
        range: b.getAttribute('data-range'),
        label: b.getAttribute('data-label')
      }, '✦ ' + (b.getAttribute('data-label') || 'Synthesis'));
    });
  });
}
// Speaker key → Biblepedia article id, so each speaker badge can carry a who-they-were detail and
// link to the full article. Curated (verified slugs) for the known speaker vocabulary; an unknown
// speaker key falls back to its own slug (covers Moses/David/etc.) and simply stays un-linked if
// no such article exists. Narration/role voices have no person article.
var _SPEAKER_BP = {
  jesus: 'jesus-christ', god: 'god', john: 'john', peter: 'peter', paul: 'paul',
  pharisees: 'pharisees', scribes: 'scribes', sadducees: 'sadducees',
  pilate: 'pilate', herod: 'herod', angels: 'angel', disciples: 'apostles',
  mary: 'mary', martha: 'martha', satan: 'satan', serpent: 'serpent', job: 'job'
};
var _SPEAKER_NOART = { narrative: 1, crowd: 1, questioner: 1, psalmist: 1, teacher: 1, wisdom: 1 };
function _speakerBpId(spk) {
  if (_SPEAKER_NOART[spk]) return null;
  if (_SPEAKER_BP[spk]) return _SPEAKER_BP[spk];
  return String(spk).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

// The narrator IS the book's traditional author. Books whose author is genuinely unknown/anonymous
// (compiled or attributed only by uncertain tradition) link instead to a dedicated "Authorship of …"
// Biblepedia article that explains why the author is unknown and what the tradition holds.
var _BOOK_AUTHOR_ANON = {
  esther: 'authorship-of-esther', job: 'authorship-of-job', hebrews: 'authorship-of-hebrews',
  '1kings': 'authorship-of-kings', '2kings': 'authorship-of-kings', '2samuel': 'authorship-of-samuel'
};
// Named author → person-article slug. Keys are the cleaned, lower-cased author string from
// book-context.json (parentheticals / co-authors stripped first by _resolveBookAuthor).
var _AUTHOR_SLUG = {
  'paul': 'paul', 'moses': 'moses', 'peter': 'peter', 'john the apostle': 'john', 'john': 'john',
  'samuel': 'samuel', 'ezra': 'ezra', 'solomon': 'solomon', 'david': 'david', 'jeremiah': 'jeremiah',
  'isaiah': 'isaiah', 'matthew': 'matthew', 'john mark': 'mark', 'mark': 'mark', 'luke': 'luke',
  'james': 'james', 'jude': 'jude', 'joshua': 'joshua', 'daniel': 'daniel', 'ezekiel': 'ezekiel',
  'nehemiah': 'nehemiah', 'amos': 'amos', 'hosea': 'hosea', 'joel': 'joel', 'jonah': 'jonah',
  'micah': 'micah', 'nahum': 'nahum', 'habakkuk': 'habakkuk', 'zephaniah': 'zephaniah',
  'haggai': 'haggai', 'zechariah': 'zechariah', 'malachi': 'malachi', 'obadiah': 'obadiah'
};
// → { name, id }. name is the badge suffix ("Narration — {name}"); id is the article to link.
function _resolveBookAuthor(bookId, ctx) {
  if (_BOOK_AUTHOR_ANON[bookId]) return { name: 'author unknown', id: _BOOK_AUTHOR_ANON[bookId] };
  var raw = (ctx && ctx.author) || '';
  // Drop parentheticals, then take the first author before a list separator or "and".
  var cleaned = raw.replace(/\s*\([^)]*\)/g, '').split(/[;,]| and /i)[0].trim();
  var slug = _AUTHOR_SLUG[cleaned.toLowerCase()];
  var name = cleaned.replace(/\s+the\s+apostle$/i, '');   // "John the apostle" → "John"
  return { name: name, id: slug || null };
}

// INTENT: Show WHO speaks in the passage as badges — a single voice gets a "speaking throughout"
//   badge with a one-line bio from its Biblepedia article; multiple voices each get a badge with
//   the verse ranges they speak. Tapping a badge jumps to the full Biblepedia article.
// CHANGE? Speaker→article map is _SPEAKER_BP; bios come from data/biblepedia/articles/{id}.json
//   (.intro, trimmed by _previewFromHtml) — fetched per speaker (small, cached), NOT via the
//   1.7MB index, so this stays cheap. If paragraph data adds a new speaker key, add it to
//   _SPEAKER_BP (or _SPEAKER_NOART) or it falls back to a slug guess.
// VERIFY: Study John 17 (Jesus throughout) → one "Jesus" badge, "speaking throughout", a bio line,
//   click → /biblepedia/?a=jesus-christ. Study a dialogue chapter → a badge per speaker with ranges.
function _fillSpeakers(breaks, maxV, bookId) {
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
  var single = order.length < 2;
  host.innerHTML = '<p class="study-empty">Loading…</p>';
  // Book-context gives us the traditional author, so the narrator badge can read "Narration — Paul"
  // and link to that author (or, for anonymous books, to an "Authorship of …" article).
  _loadCtx().then(function (all) {
    if (!host.isConnected) return;
    var ctx = (all || {})[bookId] || {};
    // Resolve each speaker → { label, articleId } before fetching, so badges render complete.
    var resolved = order.map(function (spk) {
      if (spk === 'narrative') {
        var au = _resolveBookAuthor(bookId, ctx);
        return { label: au.name ? ('Narration — ' + au.name) : 'Narration', articleId: au.id };
      }
      return { label: _speakerLabel(spk), articleId: _speakerBpId(spk) };
    });
    return Promise.all(resolved.map(function (r) {
      if (!r.articleId) return Promise.resolve(null);
      return _loadBPArticle(r.articleId)
        .then(function (art) { return (art && art.intro) ? { id: r.articleId, intro: art.intro } : null; })
        .catch(function () { return null; });
    })).then(function (arts) {
      if (!host.isConnected) return;
      host.innerHTML = '<div class="study-speakers' + (single ? ' study-speakers--single' : '') + '">' + order.map(function (spk, i) {
        var label = resolved[i].label;
        var where = single ? 'speaking throughout' : ('vv. ' + bySpeaker[spk].join(', '));
        _lastData.speakers.push({ label: label, ranges: single ? 'throughout' : bySpeaker[spk].join(', ') });
        var found = arts[i];
        var chipCls = 'reader-speaker-chip ' + _speakerClass(spk);
        var chip = found
          ? '<a class="' + chipCls + ' study-speaker__link" href="' + _esc(_BP_URL + '?a=' + encodeURIComponent(found.id)) + '">' + _esc(label) + ' ↗</a>'
          : '<span class="' + chipCls + '">' + _esc(label) + '</span>';
        var bio = '';
        if (found) {
          var pv = _previewFromHtml(found.intro, 1, 30);
          if (pv.text) bio = '<p class="study-speaker__detail">' + _esc(pv.text) + (pv.truncated ? ' …' : '') + '</p>';
        }
        return '<div class="study-speaker">' +
          '<div class="study-speaker__head">' + chip +
            '<span class="study-speaker__ranges">' + _esc(where) + '</span></div>' +
          bio + '</div>';
      }).join('') + '</div>';
    });
  });
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
    _bladeCtx.word = { code: code, lang: lang };   // remember for the Word binder tab (SD-T1)
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
        _lastData.keywords.push({ code: code, lang: lang, lemma: entry.lemma || '', translit: entry.translit || '', gloss: gloss, count: counts[code].count });
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
// INTENT: Load Leaflet (CSS + JS, self-hosted) on first map use. The reader page does NOT ship
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
      link.href = '/assets/vendor/leaflet/leaflet.css';
      link.onload = function () { link.dataset.loaded = '1'; cssReady = true; maybe(); };
      link.onerror = function () { cssReady = true; maybe(); };  // proceed; tiles may still paint
      document.head.appendChild(link);
    } else {
      link.addEventListener('load', function () { cssReady = true; maybe(); });
      cssReady = true;  // already in DOM, assume usable
    }
    var s = document.createElement('script');
    s.id = 'sd-leaflet-js'; s.src = '/assets/vendor/leaflet/leaflet.js';
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
// hostEl lets the Places binder tab (_renderPlaceTimeBlade) render the same annotated maps into
// its own blade body; with no host it falls back to the (now removed) section element, a no-op.
function _fillMaps(bookId, bookName, ch, key, hostEl) {
  var host = hostEl || document.getElementById('sd-maps');
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

// ── Encyclopedia (Biblepedia) ───────────────────────────────────────────────
// Articles for which the current passage (book + chapter, narrowed by the range scope) is a
// listed key reference. The section is just a launcher showing the count; the cards live in a
// blade so the full intro text has room to breathe. Matching uses parseRef on each entry's
// key_refs — the same curated "key references" the encyclopedia ships — so we surface the
// articles a reader most needs here without a full per-verse concordance.
function _bpMatches(idx, bookId, ch) {
  if (!Array.isArray(idx)) return [];
  var out = [];
  idx.forEach(function (a) {
    if (!a || a.has_article === false) return;          // only entries with a readable article
    var refs = a.key_refs || [], hits = [];
    for (var i = 0; i < refs.length; i++) {
      var p = parseRef(refs[i]);
      if (p && p.bookId === bookId && p.ch === ch && _inRange(p.v)) hits.push(p.display || refs[i]);
    }
    if (hits.length) out.push({ id: a.id, term: a.term, category: a.category, brief: a.brief || '', refs: hits });
  });
  // Group by kind (people → places → events → concepts → …), then alphabetical within a kind.
  var order = { people: 0, places: 1, events: 2, event: 2, concepts: 3, concept: 3, names: 4, father: 5, commentator: 6 };
  out.sort(function (a, b) {
    var ca = order[a.category] != null ? order[a.category] : 9;
    var cb = order[b.category] != null ? order[b.category] : 9;
    if (ca !== cb) return ca - cb;
    return String(a.term).localeCompare(String(b.term));
  });
  return out;
}

// Context of the last passage offered to the Encyclopedia, and the key it was actually loaded
// for — so an expand can fire the deferred load and re-expands don't re-scan the same chapter.
var _bpPending = null, _bpLoadedKey = null;

// Write the live article count into the collapsed section's header so it reads "Biblepedia (27)".
function _setBPCount(n) {
  var t = _bodyEl && _bodyEl.querySelector('[data-sec="sd-biblepedia"] .study-sec-title');
  if (t) t.textContent = n ? 'Biblepedia (' + n + ')' : 'Biblepedia';
}

// Called on every chapter/range change. The 1.7MB index is NOT touched while the section is
// collapsed — we only stash the context and show a hint; _wireToggles fires _bpLoad on first
// expand. While expanded, refilling (e.g. a range change) re-runs the load with the new scope.
function _fillBiblepedia(bookId, ch, key) {
  var host = document.getElementById('sd-biblepedia');
  if (!host) return;
  _bpPending = { bookId: bookId, ch: ch, key: key };
  _setBPCount(0);
  if (host.hidden) {
    _bpLoadedKey = null;                 // content is wiped; force a reload when next expanded
    _lastData.biblepedia = [];
    host.innerHTML = '<p class="study-empty">Expand to find Biblepedia articles for this passage.</p>';
    return;
  }
  _bpLoad(bookId, ch, key);
}

function _bpLoad(bookId, ch, key) {
  var host = document.getElementById('sd-biblepedia');
  if (!host) return;
  _lastData.biblepedia = [];
  host.innerHTML = '<p class="study-empty">Loading…</p>';
  _loadBPIndex().then(function (idx) {
    if (_curKey !== key || !host.isConnected) return;
    var matches = _bpMatches(idx, bookId, ch);
    _lastData.biblepedia = matches;
    _bpLoadedKey = key;
    _setBPCount(matches.length);
    if (!matches.length) { host.innerHTML = '<p class="study-empty">No Biblepedia articles for this range.</p>'; return; }
    var n = matches.length;
    host.innerHTML =
      '<p class="study-sec-note">' + n + ' article' + (n === 1 ? '' : 's') + ' key to this passage.</p>' +
      '<button type="button" class="study-bookbtn" id="sd-bp-open">Read ' + n + ' article' + (n === 1 ? '' : 's') + ' as cards →</button>';
    var btn = document.getElementById('sd-bp-open');
    if (btn) btn.addEventListener('click', function () {
      openBlade('biblepedia', { articles: matches, ref: _lastData.ref }, 'Biblepedia');
    });
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
  if (d.biblepedia && d.biblepedia.length) { L.push('## Biblepedia articles'); d.biblepedia.forEach(function (b) { L.push('- **' + b.term + '**' + (b.category ? ' (' + b.category + ')' : '') + (b.refs && b.refs.length ? ' — ' + b.refs.join(', ') : '')); }); L.push(''); }
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
  // "Where & when" maps moved to the Places tab (_renderPlaceTimeBlade) — built on demand there.
  _fillConnections(bookId, bookName, ch, key);
  _fillBiblepedia(bookId, ch, key);
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
  _bladeCtx = { word: null, section: null };   // new passage → forget the last tab selection
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
      // "Where & when" map now lives in the Places binder tab (_renderPlaceTimeBlade), not here.
      _sectionShell('sd-connections', 'Connections') +
      _sectionShell('sd-biblepedia', 'Biblepedia', true) +   // default-collapsed: defer the heavy index
      _sectionShell('sd-notes', 'Notes');

    var bookBtn = document.getElementById('sd-book-btn');
    if (bookBtn) bookBtn.addEventListener('click', function () {
      openBlade('book-details', { bookId: nav.bookId, bookName: bookName }, bookName);
    });
    _wireToggles();
    _wireRange(nav.bookId, bookName, nav.ch, key);
    _fillOutline(chData && chData.headings, _maxV);
    _fillSpeakers(chData && chData.breaks, _maxV, nav.bookId);
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

// P11: the desk's stylesheet (reader-study.css) is split out of reader.css
// and loads on the first open, so plain reading never parses it. The link is
// injected before the drawer reveals; a fallback timer keeps a broken fetch
// from wedging the button.
var _cssReady = null;
function _ensureStudyCss() {
  if (_cssReady) return _cssReady;
  _cssReady = new Promise(function (resolve) {
    var l = document.createElement('link');
    l.rel = 'stylesheet';
    l.href = '/assets/css/reader-study.css';
    l.onload = l.onerror = function () { resolve(); };
    document.head.appendChild(l);
    setTimeout(resolve, 500);
  });
  return _cssReady;
}

function _setOpen(on) {
  if (on && !_cssReady) {
    // First open: let the stylesheet land, then run the real open.
    _ensureStudyCss().then(function () { _setOpen(on); });
    return;
  }
  _open = on;
  var layout = document.querySelector('.reader-layout');
  if (layout) layout.classList.toggle('reader-layout--study-open', on);
  if (_btn) {
    _btn.classList.toggle('reader-study-btn--on', on);
    _btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  }
  if (on) { _armObserver(); _render(); } else { _disarmObserver(); _destroyMaps(); _closeBlades(); }
}

// Escape backs out of the study surface: pop the top blade first (same as the breadcrumb
// Back ‹), or close the whole desk when no blade is open. Registered once in initStudyDesk;
// no-ops unless the desk is open, so it never swallows Escape elsewhere on the reader.
function _onKeydown(e) {
  if (e.key !== 'Escape' || !_open) return;
  if (_bladeStack.length) { e.preventDefault(); _bladeBack(); }
  else { e.preventDefault(); _setOpen(false); if (_btn) _btn.focus(); }
}

function _buildDesk() {
  var desk = document.createElement('aside');
  desk.id = 'reader-study-desk';
  desk.className = 'reader-study-desk';
  desk.setAttribute('aria-label', 'Passage study');
  // Layout: [binder rail | main]. The rail is a flex sibling (never scrolls); `main` is the
  // scroll container holding the head, the section body, and the blade overlay (which is
  // absolute within `main`, so it covers head+body but leaves the rail visible → you can
  // switch tools while a blade is open).
  desk.innerHTML =
    '<div class="study-rail" role="tablist" aria-label="Study tools" aria-orientation="vertical">' +
      _TOOLS.map(function (t, i) {
        return '<button type="button" class="study-rail__tab' + (i === 0 ? ' study-rail__tab--active' : '') + '"' +
          ' role="tab" data-tool="' + t.type + '" id="sd-tab-' + t.type + '" aria-controls="sd-blade-body"' +
          ' aria-selected="' + (i === 0 ? 'true' : 'false') + '" tabindex="' + (i === 0 ? '0' : '-1') + '"' +
          ' title="' + _esc(t.full || t.label) + '">' +
          '<span class="study-rail__icon" aria-hidden="true">' + t.icon + '</span>' +
          '<span class="study-rail__label">' + _esc(t.label) + '</span>' +
        '</button>';
      }).join('') +
    '</div>' +
    '<div class="study-desk__main">' +
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
      '</div>' +
    '</div>';
  _bodyEl = desk.querySelector('.study-desk__body');
  desk.querySelector('.study-desk__close').addEventListener('click', function () { _setOpen(false); });
  desk.querySelector('.study-blade__back').addEventListener('click', _bladeBack);
  desk.querySelector('.study-blade__close').addEventListener('click', _closeBlades);
  // Binder-tab rail: each divider switches the top-level tool (SD-T1).
  var rail = desk.querySelector('.study-rail');
  rail.querySelectorAll('.study-rail__tab').forEach(function (tab) {
    tab.addEventListener('click', function () { openTool(tab.getAttribute('data-tool')); });
  });
  rail.addEventListener('keydown', _onRailKeydown);
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

// ── Binder tabs (SD-T1) ─────────────────────────────────────────────────────
// INTENT: Make every blade reachable directly via a "school binder divider" rail on the
//   desk, instead of only by drilling into a section. Two navigation axes: the rail switches
//   the TOP-LEVEL tool (openTool resets the blade stack to that tool); the breadcrumb still
//   walks DEPTH within a tool. _bladeCtx remembers the last word/section so switching tabs
//   keeps your place. New tools appear in the rail automatically once added to _TOOLS.
// CHANGE? Add a tool = push to _TOOLS (type must match a _BLADES key) + give it defaultParams
//   built from the current passage + _bladeCtx. The first entry ('passage') is special — it
//   closes blades back to the section list. Rail markup/wiring is in _buildDesk; active state
//   is synced from _renderTopBlade / _closeBlades via _syncActiveTool.
// VERIFY: Open the desk → a left rail lists Passage · Synthesis · Word · Encyc. · Book; click
//   each to open its blade; arrow keys move between tabs; the active tab is highlighted.
var _bladeCtx = { word: null, section: null };   // {code,lang} · {startV,range,label}

var _TOOLS = [
  { type: 'passage', label: 'Passage', icon: '📋' },   // returns to the section list
  { type: 'section-synthesis', label: 'Synth', full: 'Synthesis', icon: '✦', scope: 'section',
    from: 'the Outline section',
    defaultParams: function () {
      var nav = window._readerNavState; if (!nav || !nav.bookId) return null;
      var sec = _bladeCtx.section || _lastData.outline[0]; if (!sec) return null;
      return { bookId: nav.bookId, bookName: nav.bookName || nav.bookId, ch: nav.ch,
               startV: sec.startV, range: sec.range, label: sec.label || sec.text };
    } },
  { type: 'commentary', label: 'Comm.', full: 'Commentary', icon: '🗒️', scope: 'section',
    from: 'the Outline section',
    defaultParams: function () { return _sectionToolParams({ source: _commDefaultSource() }); } },
  { type: 'witnesses', label: 'Voices', icon: '☁️', scope: 'section',
    from: 'the Outline section',
    defaultParams: function () { return _sectionToolParams({ source: 'cow' }); } },   // locked to Cloud of Witnesses — Church Fathers
  { type: 'word-study', label: 'Word', icon: '🔤', scope: 'word',
    from: 'the Key words section (or tap a word in the passage)',
    defaultParams: function () {
      var w = _bladeCtx.word || _lastData.keywords[0];
      if (!w || !w.code) return null;
      return { code: w.code, lang: w.lang };
    } },
  { type: 'crossversion', label: 'Vers.', full: 'Versions', icon: '⇄', scope: 'word',
    from: 'the Key words section (or tap a word in the passage)',
    defaultParams: function () {
      var w = _bladeCtx.word || _lastData.keywords[0];
      if (!w || !w.code) return null;
      return { code: w.code, lang: w.lang };
    } },
  { type: 'placetime', label: 'Places', icon: '🗺️', scope: 'passage',
    from: 'the Where & when section',
    defaultParams: function () { return { ref: _lastData.ref }; } },
  { type: 'biblepedia', label: 'Pedia', full: 'Biblepedia', icon: '📚', scope: 'passage',
    from: 'the Biblepedia section',
    defaultParams: function () { return { articles: _lastData.biblepedia || [], ref: _lastData.ref }; } },
  { type: 'book-details', label: 'Book', icon: '📖', scope: 'book',
    from: 'the “About book” button',
    defaultParams: function () {
      var nav = window._readerNavState; if (!nav || !nav.bookId) return null;
      return { bookId: nav.bookId, bookName: nav.bookName || nav.bookId };
    } }
];
function _toolFor(type) { for (var i = 0; i < _TOOLS.length; i++) if (_TOOLS[i].type === type) return _TOOLS[i]; return null; }
function _toolTitle(type, params, tool) {
  if (type === 'section-synthesis') return '✦ ' + (params.label || 'Synthesis');
  if (type === 'commentary' || type === 'witnesses') return _commTitle(type, params.label);
  if (type === 'word-study') return params.code || (tool && tool.label) || 'Word';
  if (type === 'crossversion') return 'Versions: ' + (params.code || 'word');
  if (type === 'placetime') return 'Places & time';
  if (type === 'book-details') return params.bookName || (tool && tool.label) || 'Book';
  if (type === 'biblepedia') return 'Biblepedia';
  return (tool && tool.label) || type;
}
// Section-scoped tools (Synthesis/Commentary/Witnesses) share the same launch context: the
// pericope remembered in _bladeCtx.section (or the first Outline heading). `extra` carries
// tool-specific params (e.g. the chosen commentary source).
function _sectionToolParams(extra) {
  var nav = window._readerNavState; if (!nav || !nav.bookId) return null;
  var sec = _bladeCtx.section || _lastData.outline[0]; if (!sec) return null;
  var p = { bookId: nav.bookId, bookName: nav.bookName || nav.bookId, ch: nav.ch,
            startV: sec.startV, range: sec.range, label: sec.label || sec.text };
  if (extra) for (var k in extra) p[k] = extra[k];
  return p;
}
// The Commentary tab never offers 'cow' (the raw Church-Father voices) — that's the dedicated,
// locked Voices tab. Its picker is the rest of COMMENTARY_SOURCES (cow-synthesis, mkt). The
// default opens at the reader's current source, mapping 'cow' → its synthesis.
function _commDefaultSource() { var s = getCommentarySource(); return s === 'cow' ? 'cow-synthesis' : s; }
function _commSources() { return COMMENTARY_SOURCES.filter(function (s) { return s.id !== 'cow'; }); }
function _commTitle(type, secLabel) {
  var base = type === 'witnesses' ? '☁️ Voices' : '🗒️ Commentary';
  return secLabel ? base + ' · ' + secLabel : base;
}

// Lateral switch to a top-level tool: reset the blade stack to just that tool. When the tool
// has no context yet (e.g. no word/section computed), show a prompt in the overlay instead.
function openTool(type) {
  if (!_deskEl) return;
  if (type === 'passage') { _closeBlades(); _syncActiveTool('passage'); return; }
  var tool = _toolFor(type);
  if (!tool || !_BLADES[type]) return;
  var params = tool.defaultParams ? tool.defaultParams() : {};
  if (params == null) { _openToolPrompt(type, tool); return; }
  _bladeStack = [{ type: type, params: params, title: _toolTitle(type, params, tool) }];
  _renderTopBlade();
}
// The desk element itself is overflow:hidden — .study-desk__main is the real
// scroll container (and the blade overlay's offset parent). Resetting scroll
// anywhere else is a no-op, which is exactly the bug that let a scrolled-down
// desk show stale passage content beneath a freshly opened blade.
function _deskMain() {
  return _deskEl && _deskEl.querySelector('.study-desk__main');
}
var _passageScroll = 0;   // reading position in the passage list, restored on blade close
function _enterBladeMode() {
  var main = _deskMain();
  if (_deskEl && !_deskEl.classList.contains('reader-study-desk--blade') && main) {
    _passageScroll = main.scrollTop;   // remember where the user was reading
  }
  _deskEl.classList.add('reader-study-desk--blade');
  if (main) main.scrollTop = 0;        // align the inset:0 overlay with the viewport
  if (_deskEl) _deskEl.scrollTop = 0;
}
// Open the overlay for a context-less tool with a hint about where to launch it from.
function _openToolPrompt(type, tool) {
  _bladeStack = [];
  _enterBladeMode();
  var crumbsEl = _deskEl.querySelector('.study-blade__crumbs');
  if (crumbsEl) crumbsEl.innerHTML =
    '<span class="study-blade__crumb" aria-current="page">' + _esc(tool.label) + '</span>';
  var body = document.getElementById('sd-blade-body');
  if (body) body.innerHTML = '<p class="study-empty">Nothing to show yet. Open <strong>' +
    _esc(tool.label) + '</strong> from ' + _esc(tool.from || 'the passage sections') +
    ' — it will appear here.</p>';
  _syncActiveTool(type);
}
function _syncActiveTool(type) {
  if (!_deskEl) return;
  _deskEl.querySelectorAll('.study-rail__tab').forEach(function (tab) {
    var on = tab.getAttribute('data-tool') === type;
    tab.setAttribute('aria-selected', on ? 'true' : 'false');
    tab.classList.toggle('study-rail__tab--active', on);
  });
}
// Roving focus for the vertical tablist (arrows + Home/End); activation is via Enter/Space
// (native button click → openTool), per the manual-activation tabs pattern.
function _onRailKeydown(e) {
  var tabs = Array.prototype.slice.call(e.currentTarget.querySelectorAll('.study-rail__tab'));
  var idx = tabs.indexOf(document.activeElement);
  if (idx < 0) return;
  var next;
  if (e.key === 'ArrowDown' || e.key === 'ArrowRight') next = (idx + 1) % tabs.length;
  else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') next = (idx - 1 + tabs.length) % tabs.length;
  else if (e.key === 'Home') next = 0;
  else if (e.key === 'End') next = tabs.length - 1;
  else return;
  e.preventDefault();
  tabs.forEach(function (t) { t.tabIndex = -1; });
  tabs[next].tabIndex = 0; tabs[next].focus();
}

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
  _destroyMaps();   // tear down any Leaflet maps the Places blade built (only blade that makes them)
  if (_deskEl) _deskEl.classList.remove('reader-study-desk--blade');
  var b = document.getElementById('sd-blade-body');
  if (b) b.innerHTML = '';
  var main = _deskMain();
  if (main) main.scrollTop = _passageScroll;   // resume where the user was reading
  _syncActiveTool('passage');   // back to the section list → "Passage" divider active
}
function _renderTopBlade() {
  var body = document.getElementById('sd-blade-body');
  var crumbsEl = _deskEl && _deskEl.querySelector('.study-blade__crumbs');
  if (!body) return;
  _destroyMaps();   // leaving/replacing a blade: drop the Places blade's maps so they don't leak
  _enterBladeMode();
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
  _syncActiveTool(_bladeStack.length ? _bladeStack[0].type : 'passage');   // root tool = active divider
  var top = _bladeStack[_bladeStack.length - 1];
  body.innerHTML = '<p class="study-empty">Loading…</p>';
  // Replacing one blade with another: the blade body keeps its own scroll
  // offset across innerHTML swaps, so start the new tool at its top.
  var scroller = body.closest('.study-blade__body') || body;
  scroller.scrollTop = 0;
  _BLADES[top.type](top.params, body);
}

// ── Word-study blade ───────────────────────────────────────────────────────
function _refChip(r) { return '<a class="ref study-word__ref" data-ref="' + _esc(r) + '">' + _esc(r) + '</a>'; }
var _WORD_HINT_KEY = 'bsw_studyword_hint';
function _wordNoteHtml() {
  var dismissed; try { dismissed = localStorage.getItem(_WORD_HINT_KEY) === '1'; } catch (e) { dismissed = false; }
  if (dismissed) return '';
  return '<div class="study-word-note" id="sd-word-note">' +
    '<span>💡 Tap any word in the passage to study it here.</span>' +
    '<button type="button" class="study-word-note__x" aria-label="Dismiss tip">✕</button></div>';
}
function _wireWordNote(scope) {
  var x = scope.querySelector('.study-word-note__x');
  if (x) x.addEventListener('click', function () {
    try { localStorage.setItem(_WORD_HINT_KEY, '1'); } catch (e) {}
    var n = document.getElementById('sd-word-note'); if (n) n.remove();
  });
}

// Theological "starter" chips (SD-T3): the passage's repeated content words (already aggregated
// into _lastData.keywords by _fillKeywords) ranked theological-first via theological-terms.json,
// else by frequency. Each chip opens that word — a quick entry point + a hint of the key terms.
function _fillWordStarters(lang, activeCode) {
  var host = document.getElementById('sd-word-starters');
  if (!host) return;
  var kws = (_lastData.keywords || []).filter(function (k) { return k && k.code; });
  if (!kws.length) { host.innerHTML = ''; return; }
  _loadTheo().then(function (theo) {
    if (!host.isConnected) return;
    theo = theo || {};
    var ranked = kws.slice().sort(function (a, b) {
      var wa = theo[a.code] || 0, wb = theo[b.code] || 0;
      if (wb !== wa) return wb - wa;            // theological weight first
      return (b.count || 0) - (a.count || 0);   // then frequency
    });
    var theoOnly = ranked.filter(function (k) { return theo[k.code]; });
    var pick = (theoOnly.length ? theoOnly : ranked).slice(0, 8);
    if (!pick.length) { host.innerHTML = ''; return; }
    host.innerHTML = '<p class="study-sec-note">' +
      (theoOnly.length ? 'Key theological words here — tap to study:' : 'Key words here — tap to study:') + '</p>' +
      '<div class="study-word-chips">' + pick.map(function (k) {
        var on = String(k.code) === String(activeCode);
        // Always show the English equivalent: prefer the gloss ("love"), fall back to the
        // transliteration ("agapē") so no badge is ever original-script-only.
        var eng = k.gloss || k.translit || '';
        return '<button type="button" class="study-word-chip' + (on ? ' study-word-chip--active' : '') +
          '" data-code="' + _esc(k.code) + '" data-lang="' + _esc(k.lang || lang) + '">' +
          '<span class="study-word-chip__lemma">' + _esc(k.lemma || k.code) + '</span>' +
          (eng ? '<span class="study-word-chip__gloss">' + _esc(eng) + '</span>' : '') +
        '</button>';
      }).join('') + '</div>';
    host.querySelectorAll('.study-word-chip').forEach(function (chip) {
      chip.addEventListener('click', function () { showWord(chip.getAttribute('data-code'), chip.getAttribute('data-lang')); });
    });
  });
}

// Reactive entry point (SD-T3): open or LIVE-UPDATE the Word tab for a Strong's code. Used by the
// starter chips and by tapping a word in the reader (interlinear) when the desk is open.
function showWord(code, lang) {
  if (!_deskEl || !code) return;
  lang = lang || (code.charAt(0) === 'H' ? 'hebrew' : 'greek');
  _bladeCtx.word = { code: code, lang: lang };
  var top = _bladeStack[_bladeStack.length - 1];
  if (top && top.type === 'word-study') { top.params = { code: code, lang: lang }; top.title = code; }
  else { _bladeStack = [{ type: 'word-study', params: { code: code, lang: lang }, title: code }]; }
  _renderTopBlade();
}

function _renderWordStudyBlade(params, body) {
  var code = params.code;
  var lang = params.lang || (code && code.charAt(0) === 'H' ? 'hebrew' : 'greek');
  body.innerHTML = _wordNoteHtml() +
    '<div class="study-word-starters" id="sd-word-starters"></div>' +
    '<div class="study-word-detail" id="sd-word-detail">' +
    (code ? '<p class="study-empty">Loading…</p>'
          : '<p class="study-empty">Pick a starter word above, or tap any word in the passage.</p>') +
    '</div>';
  _wireWordNote(body);
  _fillWordStarters(lang, code);
  if (code) _fillWordDetail(code, lang, document.getElementById('sd-word-detail'));
}

function _fillWordDetail(code, lang, host) {
  if (!host) return;
  var lexType = (lang === 'hebrew') ? 'bdb' : 'thayer';
  Promise.all([
    loadStrongs(lang).catch(function () { return {}; }),
    loadLexicon(lexType).catch(function () { return {}; }),
    _loadRefs(code)
  ]).then(function (res) {
    if (!host.isConnected) return;
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

    host.innerHTML = html;
    var more = document.getElementById('sd-word-more');
    if (more) more.addEventListener('click', function () {
      document.getElementById('sd-word-all').innerHTML = refs.map(_refChip).join('');
      more.remove();
      wireRefLinks(host);
    });
    wireRefLinks(host);
  }).catch(function () { host.innerHTML = '<p class="study-empty">Could not load this word.</p>'; });
}

// ── Book-details blade ─────────────────────────────────────────────────────
// Each book-detail section (Setting, Purpose, Themes, …) is a collapsible <details>, open by
// default so the article reads normally but can be folded away to scan the headings.
function _bookSec(title, content) {
  return content
    ? '<details class="study-book__sec" open>' +
        '<summary class="study-book__sechead"><span class="study-book__chev" aria-hidden="true">▾</span><h4>' + _esc(title) + '</h4></summary>' +
        '<div class="study-book__secbody">' + content + '</div>' +
      '</details>'
    : '';
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

// Horizontal chip row of the chapter's outline sections — lets the summary blades (Synthesis;
// later Commentary/Witnesses) swap pericopes IN PLACE instead of going Back to the desk (SD-T2).
function _sectionChips(activeStartV) {
  var out = _lastData.outline || [];
  if (out.length < 2) return '';   // nothing to switch between
  return '<div class="study-secswitch" role="tablist" aria-label="Sections">' +
    out.map(function (o) {
      var on = String(o.startV) === String(activeStartV);
      return '<button type="button" class="study-secswitch__chip' + (on ? ' study-secswitch__chip--active' : '') +
        '" role="tab" aria-selected="' + (on ? 'true' : 'false') + '"' +
        ' data-startv="' + _esc(String(o.startV)) + '" data-range="' + _esc(o.range) + '" data-label="' + _esc(o.text) + '">' +
        '<span class="study-secswitch__range">' + _esc(o.range) + '</span>' +
        '<span class="study-secswitch__label">' + _esc(o.text) + '</span>' +
      '</button>';
    }).join('') + '</div>';
}
function _wireSectionChips(scope, onPick) {
  scope.querySelectorAll('.study-secswitch__chip').forEach(function (chip) {
    chip.addEventListener('click', function () {
      if (chip.getAttribute('aria-selected') === 'true') return;   // already showing
      onPick({ startV: chip.getAttribute('data-startv'), range: chip.getAttribute('data-range'), label: chip.getAttribute('data-label') });
    });
  });
}

function _renderSectionSynthesisBlade(params, body) {
  var bookId = params.bookId, ch = params.ch, startV = params.startV;
  // Section switcher pinned at the top (SD-T2): pick another pericope without leaving the blade.
  body.innerHTML = _sectionChips(startV) +
    '<div class="study-synth-content"><p class="study-empty">Loading…</p></div>';
  _wireSectionChips(body, function (sec) {
    _bladeCtx.section = sec;
    var top = _bladeStack[_bladeStack.length - 1];
    if (top) {
      top.params = { bookId: bookId, bookName: params.bookName, ch: ch, startV: sec.startV, range: sec.range, label: sec.label };
      top.title = '✦ ' + (sec.label || 'Synthesis');
    }
    _renderTopBlade();   // re-render chips (new active) + content + breadcrumb in place
  });
  var content = body.querySelector('.study-synth-content');
  _loadSynthesis(bookId, ch).then(function (data) {
    if (!content.isConnected) return;
    var sec = _findSynthSection(data, startV);
    if (!sec) {
      content.innerHTML = '<p class="study-empty">No section synthesis for this passage yet.' +
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
    content.innerHTML = html;
    wireRefLinks(content);
    var refsEl = content.querySelector('.study-synth__refs');
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

// ── Biblepedia blade ────────────────────────────────────────────────────────
// INTENT: The passage's Biblepedia terms ordered GENERAL → SPECIFIC and in reading order: concepts
//   that run through the whole passage first, then few-verse concepts filed where they're first
//   introduced, then single-verse concepts near their verse (see _renderBiblepediaBlade for the
//   tiering). Each card is a mini-article: term + kind + verse badges (intro verse highlighted,
//   the rest reference badges) + a short preview (first ~2 sentences / 200 words) ending "…" with a
//   "Read the full article →" link; previews are real article text fetched per card
//   (data/biblepedia/articles/{id}.json .intro), cached.
// CHANGE? Opened from the "Biblepedia" section launcher (_fillBiblepedia) with params.articles
//   pre-computed by _bpMatches (each carries .refs = matched verse displays); verses parsed via
//   parseRef. Preview length via _previewFromHtml; full link → /biblepedia/?a={id}.
var _BP_CAT_LABELS = {
  people: 'Person', places: 'Place', events: 'Event', event: 'Event',
  concepts: 'Concept', concept: 'Concept', names: 'Name', father: 'Church Father', commentator: 'Commentator'
};
function _bpCatLabel(c) { return _BP_CAT_LABELS[c] || (c ? c.charAt(0).toUpperCase() + c.slice(1) : ''); }

// Plain-text preview from intro HTML: first `maxSentences` sentences, hard-capped at `maxWords`.
// Returns {text, truncated} so the caller can append an ellipsis only when something was cut.
function _previewFromHtml(html, maxSentences, maxWords) {
  var tmp = document.createElement('div');
  tmp.innerHTML = html || '';
  var text = (tmp.textContent || '').replace(/\s+/g, ' ').trim();
  if (!text) return { text: '', truncated: false };
  var sentences = text.match(/[^.!?]+[.!?]+(?:["'’”)\]]+)?/g) || [text];
  var picked = sentences.slice(0, maxSentences).join(' ').trim();
  var truncated = sentences.length > maxSentences;
  var words = picked.split(/\s+/);
  if (words.length > maxWords) { picked = words.slice(0, maxWords).join(' '); truncated = true; }
  if (picked.length < text.length) truncated = true;
  return { text: picked, truncated: truncated };
}

// One card per article. `vs` is the sorted list of verses (within the passage) the article
// touches: the first is where the reader is "introduced" to it, the rest are later references.
function _bpCardHtml(a) {
  var vs = a._vs || [];
  var badges = vs.map(function (v, i) {
    var intro = (i === 0);
    return '<button type="button" class="study-bp-ref' + (intro ? ' study-bp-ref--intro' : '') +
      '" data-v="' + v + '" title="' + (intro ? 'Introduced at v' + v : 'Referenced at v' + v) + '">v' + v + '</button>';
  }).join('');
  return '<div class="study-bp-card" data-id="' + _esc(a.id) + '">' +
    '<div class="study-bp-card__sum">' +
      '<span class="study-bp-card__term">' + _esc(a.term) + '</span>' +
      (a.category ? '<span class="study-bp-card__cat study-bp-card__cat--' + _esc(a.category) + '">' + _esc(_bpCatLabel(a.category)) + '</span>' : '') +
    '</div>' +
    (badges ? '<div class="study-bp-card__refs" aria-label="Verses in this passage">' + badges + '</div>' : '') +
    '<div class="study-bp-card__lazy"><p class="study-bp-card__preview study-bp-card__preview--load">' + _esc(a.brief || 'Loading…') + '</p></div>' +
  '</div>';
}

// INTENT: Order the passage's articles general → specific, in the sequence the reader meets them.
//   Three tiers: (0) concepts that run THROUGH the passage (3+ verses spanning most of the range)
//   come first; (1) concepts spanning a FEW verses, filed at the verse that introduces them, with
//   reference badges for where they recur; (2) single-verse concepts, filed at their verse. Within
//   every tier the sort is by first-appearance verse, so the column reads top-to-bottom in reading
//   order. Each card carries verse badges (the intro verse highlighted) that scroll the reader.
// CHANGE? Tier thresholds use the live reader range (_rangeFrom/_rangeTo). Verses come from
//   parseRef over a.refs (the in-range hits from _bpMatches). Tier headers show only when more than
//   one tier is populated, so a one-verse passage isn't cluttered.
// VERIFY: Study desk on John 1 → Biblepedia → "Word/Logos" type concepts head the list under
//   "Throughout the passage"; verse-local names sit lower under "Verse by verse", each near its verse.
var _BP_TIER_LABELS = ['Throughout the passage', 'Across several verses', 'Verse by verse'];
function _renderBiblepediaBlade(params, body) {
  var arts = params.articles || [];
  if (!arts.length) { body.innerHTML = '<p class="study-empty">No Biblepedia articles for this passage.</p>'; return; }

  var briefById = Object.create(null);
  var rows = arts.map(function (a) {
    briefById[a.id] = a.brief || '';
    var seen = Object.create(null), vs = [];
    (a.refs || []).forEach(function (r) {
      var p = parseRef(r);
      if (p && p.v != null && !seen[p.v]) { seen[p.v] = 1; vs.push(p.v); }
    });
    vs.sort(function (x, y) { return x - y; });
    a._vs = vs;
    return { a: a, vs: vs };
  });

  // Tier thresholds relative to the actual passage range; fall back to the matched span if the
  // range globals aren't meaningfully set.
  var lo = _rangeFrom, hi = _rangeTo;
  if (!(hi >= lo && hi > 0)) {
    lo = Infinity; hi = 0;
    rows.forEach(function (r) { r.vs.forEach(function (v) { if (v < lo) lo = v; if (v > hi) hi = v; }); });
    if (!(hi >= lo)) { lo = 1; hi = 1; }
  }
  var range = hi - lo + 1;
  rows.forEach(function (r) {
    var vs = r.vs;
    r.firstV = vs.length ? vs[0] : 9999;
    r.count = vs.length;
    var span = vs.length ? (vs[vs.length - 1] - vs[0] + 1) : 0;
    var spanRatio = range > 1 ? span / range : 1;
    r.tier = (r.count >= 3 && spanRatio >= 0.6) ? 0 : (r.count >= 2 ? 1 : 2);
  });
  rows.sort(function (x, y) {
    if (x.tier !== y.tier) return x.tier - y.tier;          // general (broad) before specific
    if (x.firstV !== y.firstV) return x.firstV - y.firstV;  // then in reading order
    if (x.count !== y.count) return y.count - x.count;      // more-pervasive first on ties
    return String(x.a.term).localeCompare(String(y.a.term));
  });

  var tiersPresent = Object.create(null);
  rows.forEach(function (r) { tiersPresent[r.tier] = 1; });
  var showHeaders = Object.keys(tiersPresent).length > 1;

  var html = '<div class="study-bp">' +
    '<p class="study-bp__intro">' + arts.length + ' Biblepedia article' + (arts.length === 1 ? '' : 's') +
      ' for <strong>' + _esc(params.ref || 'this passage') + '</strong> — general to specific, in reading order.</p>';
  var lastTier = -1;
  rows.forEach(function (r) {
    if (showHeaders && r.tier !== lastTier) {
      html += '<h4 class="study-bp-tier">' + _BP_TIER_LABELS[r.tier] + '</h4>';
      lastTier = r.tier;
    }
    html += _bpCardHtml(r.a);
  });
  html += '</div>';
  body.innerHTML = html;
  wireRefLinks(body);

  // Verse badges scroll the reader to the verse.
  body.querySelectorAll('.study-bp-ref').forEach(function (b) {
    b.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); _scrollToVerse(b.getAttribute('data-v')); });
  });
  // Each card resolves its own intro → 2-sentence / 200-word preview + "Read the full article →".
  body.querySelectorAll('.study-bp-card').forEach(function (card) {
    var id = card.getAttribute('data-id');
    _fillBPCard(id, card.querySelector('.study-bp-card__lazy'), briefById[id]);
  });
}

function _fillBPCard(id, host, brief) {
  if (!host) return;
  var more = '<a class="study-bp-card__more" target="_blank" rel="noopener" href="' +
    _esc(_BP_URL + '?a=' + encodeURIComponent(id)) + '">Read the full article →</a>';
  _loadBPArticle(id).then(function (art) {
    if (!host.isConnected) return;
    var pv = _previewFromHtml((art && art.intro) || '', 2, 200);
    var text = pv.text || brief || '';
    host.innerHTML = text
      ? '<p class="study-bp-card__preview">' + _esc(text) + (pv.truncated ? ' …' : '') + '</p>' + more
      : '<p class="study-empty">No introduction available.</p>' + more;
  }).catch(function () {
    if (!host.isConnected) return;
    host.innerHTML = (brief ? '<p class="study-bp-card__preview">' + _esc(brief) + ' …</p>' : '<p class="study-empty">Could not load this article.</p>') + more;
  });
}

// ── Commentary / Voices blade (section-scoped) ──────────────────────────────
// INTENT: Read the historic-church commentary for a pericope WITHOUT leaving the desk. One
//   renderer backs two binder tabs: "Voices" is LOCKED to Cloud of Witnesses — Church Fathers
//   (the raw multi-voice catena, no picker); "Commentary" offers the rest of COMMENTARY_SOURCES
//   (the COW synthesis, MKT cards) via a source selector — the raw 'cow' is intentionally absent
//   there because it has its own Voices tab. Both share the SD-T2 section chips. The full text
//   already lives in core.js's commentary layer — this just scopes + renders it (decorateCatena
//   for 'cow', decorateMkt for 'mkt', plain HTML for the syntheses), per verse in the range.
// CHANGE? Voices is keyed by type 'witnesses' (source forced to 'cow', picker suppressed).
//   Commentary picker = _commSources() (COMMENTARY_SOURCES minus 'cow'). Data via
//   loadCommentary/loadMktAll (per-chapter {ch:{v:html}}); range parsed from params.range.
// VERIFY: Study desk → Voices tab → collapsible Father voices per verse, NO source dropdown;
//   Commentary tab → dropdown lists Synthesis + MKT only (no "Church Fathers"); section chips
//   swap the pericope without a Back trip.
function _commSrcMeta(id) { for (var i = 0; i < COMMENTARY_SOURCES.length; i++) if (COMMENTARY_SOURCES[i].id === id) return COMMENTARY_SOURCES[i]; return null; }
function _commSourceRow(source) {
  return '<div class="study-comm-srcrow"><label class="study-comm-srclabel">Source</label>' +
    '<select class="study-comm-src" aria-label="Commentary source">' +
    _commSources().map(function (s) {
      return '<option value="' + _esc(s.id) + '"' + (s.id === source ? ' selected' : '') + '>' + _esc(s.label) + '</option>';
    }).join('') + '</select></div>';
}
function _renderCommentaryBlade(params, body) {
  var top = _bladeStack[_bladeStack.length - 1];
  var type = top ? top.type : 'commentary';
  var isVoices = (type === 'witnesses');                 // Voices = locked to Cloud of Witnesses (cow)
  var startV = params.startV;
  var source = isVoices ? 'cow' : (params.source || _commDefaultSource());
  // Section switcher pinned at the top (SD-T2); Commentary also gets a source selector; content below.
  body.innerHTML = _sectionChips(startV) +
    (isVoices ? '<p class="study-sec-note study-comm-locked">Cloud of Witnesses — Church Fathers</p>' : _commSourceRow(source)) +
    '<div class="study-comm-content"><p class="study-empty">Loading…</p></div>';
  _wireSectionChips(body, function (sec) {
    _bladeCtx.section = sec;
    var t = _bladeStack[_bladeStack.length - 1];
    if (t) {
      t.params = Object.assign({}, t.params, { startV: sec.startV, range: sec.range, label: sec.label });
      t.title = _commTitle(t.type, sec.label);
    }
    _renderTopBlade();   // re-render chips (new active) + source row + content in place
  });
  var sel = body.querySelector('.study-comm-src');
  if (sel) sel.addEventListener('change', function () {
    var t = _bladeStack[_bladeStack.length - 1];
    if (t) t.params.source = sel.value;   // local to the blade — does NOT change the reader's source
    _fillCommentaryContent(Object.assign({}, params, { source: sel.value }), body.querySelector('.study-comm-content'));
  });
  _fillCommentaryContent(Object.assign({}, params, { source: source }), body.querySelector('.study-comm-content'));
}
function _fillCommentaryContent(params, host) {
  if (!host) return;
  var bookId = params.bookId, ch = params.ch, source = params.source;
  var m = /^(\d+)(?:[–-](\d+))?/.exec(String(params.range || params.startV));
  var lo = m ? parseInt(m[1], 10) : parseInt(params.startV, 10), hi = (m && m[2]) ? parseInt(m[2], 10) : lo;
  host.innerHTML = '<p class="study-empty">Loading…</p>';
  var meta = _commSrcMeta(source);
  var loader = source === 'mkt'
    ? loadMktAll(bookId, ch).then(function (ds) { return { mkt: ds }; })
    : loadCommentary(bookId, source, ch).then(function (d) { return { data: d }; });
  loader.then(function (res) {
    if (!host.isConnected) return;
    var blocks = '', any = false;
    for (var v = lo; v <= hi; v++) {
      var vhtml = '';
      if (source === 'mkt') {
        var ds = res.mkt || [];
        var parts = ds.map(function (d) { return (d && d[String(ch)] && d[String(ch)][String(v)]) || null; });
        if (parts.some(function (x) { return x; })) vhtml = decorateMkt(parts);
      } else {
        var raw = res.data && res.data[String(ch)] && res.data[String(ch)][String(v)];
        if (raw) vhtml = (source === 'cow') ? decorateCatena(raw) : raw;
      }
      if (!vhtml) continue;
      any = true;
      // Each verse is an independently collapsible <details> (open by default) so a reader
      // can fold away verses they've finished and keep the rail short. The verse-number button
      // sits in the summary but stops propagation so tapping it scrolls the reader instead of
      // toggling the disclosure.
      blocks += '<details class="study-comm-v" open>' +
        '<summary class="study-comm-v__head">' +
          '<span class="study-comm-v__chev" aria-hidden="true">▾</span>' +
          '<button type="button" class="study-comm-v__num" data-v="' + v + '">v' + v + '</button>' +
        '</summary>' +
        '<div class="study-comm-v__body">' + vhtml + '</div></details>';
    }
    host.innerHTML = any
      ? '<div class="study-comm" data-src="' + _esc(source) + '">' + blocks + '</div>' +
        (meta && meta.isAI ? '<p class="study-sec-note study-comm-ai">✦ AI-assisted — see <a href="' + _esc(_resolve('../../about/')) + '">/about/</a> for methods.</p>' : '')
      : '<p class="study-empty">No ' + _esc((meta && meta.label) || 'commentary') + ' for vv. ' + lo + (hi > lo ? '–' + hi : '') + ' yet.</p>';
    host.querySelectorAll('.study-comm-v__num').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); _scrollToVerse(b.getAttribute('data-v')); }); });
    wireRefLinks(host);
  }).catch(function () { if (host.isConnected) host.innerHTML = '<p class="study-empty">Could not load commentary.</p>'; });
}

// ── Cross-version word blade (scope:'word') ─────────────────────────────────
// INTENT: Show how the original-language word in focus is carried across the major English
//   translations. There is NO per-word alignment for KJV/BSB/WEB/ASV (only the interlinear's
//   own base gloss is word-aligned), so rather than fake a word-to-word mapping, we surface the
//   honest thing: each verse in this passage where the word occurs, shown across the four
//   versions for side-by-side comparison, with the interlinear's gloss as the anchor.
// CHANGE? Occurrences are detected from the loaded interlinear (data[ch][v] tokens whose .s ===
//   code), range-scoped. Version text via loadBook(ver, bookId) → chapters[ch][v]. Uses
//   _bladeCtx.word so the tab follows whatever word you last studied.
// VERIFY: Study a Greek/Hebrew key word → Versions tab → the verses carrying it appear, each with
//   KJV/BSB/WEB/ASV stacked; verse refs scroll the reader.
// loadBook() understands the MKT tier ids (data/translation/draft/{tier}) too, so the three
// MKT renderings sit alongside the public-domain versions; missing drafts just .catch → null.
var _CV_VERSIONS = [['KJV', 'KJV'], ['BSB', 'BSB'], ['WEB', 'WEB'], ['ASV', 'ASV'],
  ['MKT-L', 'MKT-L'], ['MKT-M', 'MKT-M'], ['MKT-T', 'MKT-T']];
function _renderCrossVersionBlade(params, body) {
  var code = params.code;
  var lang = params.lang || (code && code.charAt(0) === 'H' ? 'hebrew' : 'greek');
  var nav = window._readerNavState || {};
  if (!code || !nav.bookId) { body.innerHTML = '<p class="study-empty">Pick a word first — open one from the Key words section or tap a word in the passage.</p>'; return; }
  body.innerHTML = '<p class="study-empty">Loading…</p>';
  Promise.all([loadInterlinear(nav.bookId), loadStrongs(lang).catch(function () { return {}; })]).then(function (res) {
    if (!body.isConnected) return;
    var inter = res[0] || {}, dict = res[1] || {};
    var chData = inter[String(nav.ch)] || {};
    var verses = [], seen = Object.create(null);
    Object.keys(chData).forEach(function (vk) {
      var v = parseInt(vk, 10);
      if (!_inRange(v)) return;
      (chData[vk] || []).forEach(function (tok) {
        if (tok && tok.s === code && !seen[v]) { seen[v] = 1; verses.push(v); }
      });
    });
    verses.sort(function (a, b) { return a - b; });
    var entry = dict[code] || {};
    var header = '<div class="study-cv__head">' +
      '<span class="study-cv__lemma">' + _esc(entry.lemma || code) + '</span>' +
      (entry.translit ? '<span class="study-cv__translit">' + _esc(entry.translit) + '</span>' : '') +
      '<span class="study-word__code">' + _esc(code) + '</span></div>' +
      (entry.gloss ? '<p class="study-cv__gloss">' + _esc(entry.gloss) + '</p>' : '') +
      '<p class="study-sec-note">These translations aren’t word-aligned, so each verse where ' +
        _esc(entry.lemma || code) + ' occurs in this passage is shown across versions to compare.</p>';
    if (!verses.length) { body.innerHTML = header + '<p class="study-empty">No occurrence of this word in the current range.</p>'; return; }
    verses = verses.slice(0, 8);
    body.innerHTML = header + '<div class="study-cv" id="sd-cv-list"><p class="study-empty">Loading versions…</p></div>';
    var host = document.getElementById('sd-cv-list');
    Promise.all(_CV_VERSIONS.map(function (vr) { return loadBook(vr[0], nav.bookId).catch(function () { return null; }); })).then(function (books) {
      if (!host || !host.isConnected) return;
      var html = verses.map(function (v) {
        var rows = _CV_VERSIONS.map(function (vr, i) {
          var chx = books[i] && books[i][String(nav.ch)];
          var txt = chx && chx[String(v)];
          if (!txt) return '';
          return '<div class="study-cv__row"><span class="study-cv__ver">' + _esc(vr[1]) + '</span>' +
            '<span class="study-cv__txt">' + _esc(txt) + '</span></div>';
        }).join('');
        return '<div class="study-cv__verse">' +
          '<button type="button" class="study-cv__vnum" data-v="' + v + '">' + _esc(nav.bookName || nav.bookId) + ' ' + nav.ch + ':' + v + '</button>' +
          (rows || '<p class="study-empty">Version text unavailable.</p>') + '</div>';
      }).join('');
      host.innerHTML = html;
      host.querySelectorAll('.study-cv__vnum').forEach(function (b) { b.addEventListener('click', function () { _scrollToVerse(b.getAttribute('data-v')); }); });
    });
  }).catch(function () { if (body.isConnected) body.innerHTML = '<p class="study-empty">Could not load.</p>'; });
}

// ── Place & time blade (scope:'passage') ────────────────────────────────────
// INTENT: A focused launcher for the passage's geography + period: the places named in the
//   in-scope verses (each with a deep-link into the full /maps/ view and its controlling power)
//   and the period(s) the passage belongs to (deep-linking the /timeline/). Complements the
//   "Where & when" section (which draws the annotated map) with quick jumps out to the dedicated
//   tools. Computes places itself (range-scoped _detectPlaces) so it's independent of whether the
//   section's Leaflet map has finished building.
// CHANGE? Places via _loadPlaces + _detectPlaces; period via _passagePeriods (events index) with
//   the book's settingEra as a fallback. Map link: /maps/?focus=lat,lon,zoom; period link:
//   /timeline/?era=id. Controller computed from _powersAt at the period's t.
// VERIFY: Study Matthew 4 → Places tab → Capernaum/Nazareth listed with "Open in map ▸"; When
//   shows "Life of Christ" linking the timeline. Romans 1 (no place) → graceful note + period.
function _renderPlaceTimeBlade(params, body) {
  var nav = window._readerNavState || {};
  // Two parts: the annotated "Where & when" map(s) (moved here from the section list), then quick
  // deep-link lists for the passage's places and period.
  body.innerHTML =
    '<div class="study-pt">' +
      '<div class="study-pt__maps" id="sd-pt-maps"><p class="study-empty">Loading map…</p></div>' +
      '<div class="study-pt__lists" id="sd-pt-lists"><p class="study-empty">Loading…</p></div>' +
    '</div>';
  _fillMaps(nav.bookId, nav.bookName || nav.bookId, nav.ch, _curKey, document.getElementById('sd-pt-maps'));
  _fillPlaceTimeLists(nav, document.getElementById('sd-pt-lists'));
}
function _fillPlaceTimeLists(nav, body) {
  if (!body) return;
  Promise.all([_loadPlaces(), _loadPowers(), _loadCtx()]).then(function (res) {
    if (!body.isConnected) return;
    var allPlaces = res[0] || [], powers = res[1] || {}, ctx = (res[2] || {})[nav.bookId] || null;
    var detected = _detectPlaces(allPlaces);                  // [{place, verses}] range-scoped
    var periods = _passagePeriods(powers, nav.bookId, nav.ch);
    if (!periods.length && ctx) periods = [{ era: ctx.settingEra, t: ctx.settingT, year: '', book: true }];
    var powersAtT = (periods.length && periods[0].t != null) ? _powersAt(powers, periods[0].t) : [];

    var html = '';
    html += '<div class="study-pt__sec"><h4>Places in this passage</h4>';
    if (detected.length) {
      html += '<div class="study-pt__places">' + detected.map(function (d) {
        var p = d.place;
        var ctrl = (p.lat != null && p.lon != null) ? _controllerOf(p.lat, p.lon, powersAtT) : null;
        var focus = (p.lat != null && p.lon != null) ? (MAPS_URL + '?focus=' + p.lat + ',' + p.lon + ',9') : null;
        return '<div class="study-pt__place">' +
          '<div class="study-pt__pname">' + _esc(p.name) + (ctrl ? '<span class="study-pt__under">under ' + _esc(ctrl) + '</span>' : '') + '</div>' +
          (p.desc ? '<p class="study-pt__pdesc">' + _esc(p.desc) + '</p>' : '') +
          '<div class="study-pt__plinks">' +
            (d.verses && d.verses.length ? '<button type="button" class="study-pt__vbtn" data-v="' + d.verses[0] + '">v' + d.verses.join(', ') + '</button>' : '') +
            (focus ? '<a class="study-pt__map" target="_blank" rel="noopener" href="' + _esc(focus) + '">Open in map ▸</a>' : '') +
          '</div></div>';
      }).join('') + '</div>';
    } else {
      html += '<p class="study-empty">This passage names no specific location — the map above shows the book’s geographic setting.</p>';
    }
    html += '</div>';

    html += '<div class="study-pt__sec"><h4>When</h4>';
    if (periods.length && periods[0].era) {
      html += '<div class="study-pt__periods">' + periods.map(function (pr) {
        var link = _TIMELINE_URL + '?era=' + encodeURIComponent(pr.era);
        return '<a class="study-pt__period" href="' + _esc(link) + '">' +
          '<span class="study-era-dot" style="background:' + _esc(_eraColor(powers, pr.era)) + '"></span>' +
          '<span class="study-pt__era">' + _esc(pr.era) + (pr.year ? ' · ' + _esc(pr.year) : '') + (pr.book ? ' (book setting)' : '') + '</span>' +
          '<span class="study-pt__go">timeline ▸</span></a>';
      }).join('') + '</div>';
    } else {
      html += '<p class="study-empty">No dated period detected for this passage.</p>';
    }
    // (Author/written/setting already appear in the map header above, so not repeated here.)
    html += '</div>';

    body.innerHTML = html;
    body.querySelectorAll('.study-pt__vbtn').forEach(function (b) { b.addEventListener('click', function () { _scrollToVerse(b.getAttribute('data-v')); }); });
  }).catch(function () { if (body.isConnected) body.innerHTML = '<p class="study-empty">Could not load.</p>'; });
}

_BLADES['word-study'] = _renderWordStudyBlade;
_BLADES['book-details'] = _renderBookDetailsBlade;
_BLADES['section-synthesis'] = _renderSectionSynthesisBlade;
_BLADES['biblepedia'] = _renderBiblepediaBlade;
_BLADES['commentary'] = _renderCommentaryBlade;
_BLADES['witnesses'] = _renderCommentaryBlade;
_BLADES['crossversion'] = _renderCrossVersionBlade;
_BLADES['placetime'] = _renderPlaceTimeBlade;

export function initStudyDesk() {
  var browseBar = document.querySelector('.reader-browse-bar');
  var layout = document.querySelector('.reader-layout');
  if (!browseBar || !layout || document.getElementById('reader-study-btn')) return;

  _btn = document.createElement('button');
  _btn.id = 'reader-study-btn';
  _btn.className = 'reader-study-btn';
  _btn.type = 'button';
  _btn.textContent = 'Study';
  _btn.title = 'Open the passage study desk';
  _btn.setAttribute('aria-pressed', 'false');
  // The Study Desk opener lives in the 📖 Study Tools popover (fall back to inline).
  var hint  = browseBar.querySelector('.reader-browse-hint');
  var stPop = document.getElementById('reader-studytools-popover');
  if (stPop) stPop.appendChild(_btn);
  else       browseBar.insertBefore(_btn, hint || null);
  _btn.addEventListener('click', function () { _setOpen(!_open); });
  document.addEventListener('keydown', _onKeydown);

  _deskEl = _buildDesk();
  layout.appendChild(_deskEl);

  // Reactive word-study bridge for the reader (SD-T3). interlinear.js calls these globals so it
  // need not import this module. open() reveals the desk; showWord() drives the Word tab;
  // wordTabActive() lets a reader word-tap live-update the blade instead of a popover.
  window.bswStudyDesk = {
    isOpen: function () { return _open; },
    open: function () { if (!_open && _btn) _btn.click(); },
    showWord: showWord,
    wordTabActive: function () {
      return _open && _bladeStack.length > 0 && _bladeStack[_bladeStack.length - 1].type === 'word-study';
    }
  };
}
