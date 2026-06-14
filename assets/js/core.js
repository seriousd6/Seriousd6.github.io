/* core.js — Path resolution, URL constants, caches, book/version data loaders,
 * cross-reference, commentary, parallels, Strong's, lexicon, and Bible-ready
 * coordination for the ES-module system.
 *
 * This module is imported by every other JS module. It owns:
 *   - All URL/path constants (so changing a data directory only requires edits here)
 *   - All in-memory fetch caches (keyed by version+book or similar)
 *   - The "Bible-ready" event system (fires once versions + books metadata is loaded)
 *   - The "version changed" event system (fires when the user switches translation)
 *   - Shared helper functions used across modules (escHtml, parseRef, etc.)
 *
 * Import from here; never hardcode paths or IDs in page modules.
 */
'use strict';

// ── Path auto-detection ────────────────────────────────────────────────────
// _resolve() converts a relative path to an absolute URL anchored at this
// file's own location. This lets the site work from any subdirectory without
// hardcoding the root — important for GitHub Pages where the repo name becomes
// part of the URL.
var _src = import.meta.url;

function _resolve(rel) {
  return new URL(rel, _src).href;
}

export { _resolve };

// ── URL constants ─────────────────────────────────────────────────────────
// All data and page roots are declared here so every module uses the same paths.
// Change a folder name once here; all modules update automatically.
export var DATA_ROOT        = _resolve('../../data/bible');        // versioned Bible text JSON per book
export var CROSSREFS_ROOT   = _resolve('../../data/crossrefs');    // cross-reference JSON per book
export var COMMENTARY_ROOT  = _resolve('../../data/commentary');   // commentary JSON per book/source
export var PARALLELS_ROOT   = _resolve('../../data/parallels');    // parallel passage data
export var ECHOES_ROOT      = _resolve('../../data/echoes');         // OT→NT echo/allusion/typology data per book
export var VERSIONS_URL     = _resolve('../../data/versions/versions.json'); // list of available translations
export var BOOKS_URL        = _resolve('../../data/bible/books.json');       // book metadata (names, abbrevs, testament)
export var SEARCH_URL       = _resolve('../../search/');
export var READER_URL       = _resolve('../../read/');
export var MAPS_URL         = _resolve('../../maps/');
export var LIB_READER_URL   = _resolve('../../library/read/');
export var VERSE_STUDY_URL  = _resolve('../../verse-study/');
export var COMPARE_URL      = _resolve('../../compare/');
export var WORD_URL         = _resolve('../../translation/workshop/'); // word/?s= redirects here
export var STORAGE_KEY      = 'bsw_version';   // localStorage key for the user's chosen Bible version

// ── Map cross-references ───────────────────────────────────────────────────
// Human-readable labels for each map (keyed by map id from maps.js MAPS array).
export var MAP_LABELS = {
  'holy-land':           'Holy Land (NT)',
  'paul-journeys':       "Paul's Journeys",
  'exodus':              'The Exodus',
  'divided-kingdom':     'Divided Kingdom',
  'ancient-near-east':   'Ancient Near East',
  'patriarchal-journeys':'Patriarchal Journeys',
  'conquest':            'Conquest of Canaan',
  'twelve-tribes':       'Twelve Tribes',
  'judges':              'Time of the Judges',
  'david-kingdom':       "David's Kingdom",
  'solomon-kingdom':     "Solomon's Kingdom",
  'invasions':           'Assyrian & Babylonian Invasions',
  'return-exile':        'Return from Exile',
  'seven-churches':      'Seven Churches'
};

// Bible book id → relevant map ids (ordered most-to-least relevant).
export var BOOK_MAP_LINKS = {
  'genesis':        ['patriarchal-journeys','ancient-near-east'],
  'exodus':         ['exodus','ancient-near-east'],
  'leviticus':      ['exodus'],
  'numbers':        ['exodus','twelve-tribes'],
  'deuteronomy':    ['exodus','conquest'],
  'joshua':         ['conquest','twelve-tribes'],
  'judges':         ['judges','twelve-tribes'],
  'ruth':           ['judges','twelve-tribes'],
  '1samuel':        ['judges','david-kingdom'],
  '2samuel':        ['david-kingdom'],
  '1kings':         ['david-kingdom','solomon-kingdom','divided-kingdom'],
  '2kings':         ['divided-kingdom','invasions'],
  '1chronicles':    ['david-kingdom','solomon-kingdom'],
  '2chronicles':    ['solomon-kingdom','divided-kingdom','invasions'],
  'ezra':           ['return-exile'],
  'nehemiah':       ['return-exile'],
  'esther':         ['return-exile','ancient-near-east'],
  'job':            ['ancient-near-east'],
  'psalms':         ['david-kingdom','holy-land'],
  'proverbs':       ['solomon-kingdom'],
  'ecclesiastes':   ['solomon-kingdom'],
  'songofsolomon':  ['holy-land'],
  'isaiah':         ['divided-kingdom','invasions','ancient-near-east'],
  'jeremiah':       ['invasions','divided-kingdom'],
  'lamentations':   ['invasions'],
  'ezekiel':        ['invasions','return-exile'],
  'daniel':         ['invasions','ancient-near-east'],
  'hosea':          ['divided-kingdom'],
  'joel':           ['divided-kingdom'],
  'amos':           ['divided-kingdom'],
  'obadiah':        ['divided-kingdom'],
  'jonah':          ['ancient-near-east','invasions'],
  'micah':          ['divided-kingdom'],
  'nahum':          ['invasions'],
  'habakkuk':       ['invasions'],
  'zephaniah':      ['divided-kingdom'],
  'haggai':         ['return-exile'],
  'zechariah':      ['return-exile'],
  'malachi':        ['return-exile'],
  'matthew':        ['holy-land'],
  'mark':           ['holy-land'],
  'luke':           ['holy-land'],
  'john':           ['holy-land'],
  'acts':           ['holy-land','paul-journeys'],
  'romans':         ['paul-journeys'],
  '1corinthians':   ['paul-journeys'],
  '2corinthians':   ['paul-journeys'],
  'galatians':      ['paul-journeys'],
  'ephesians':      ['paul-journeys','seven-churches'],
  'philippians':    ['paul-journeys'],
  'colossians':     ['paul-journeys'],
  '1thessalonians': ['paul-journeys'],
  '2thessalonians': ['paul-journeys'],
  '1timothy':       ['paul-journeys'],
  '2timothy':       ['paul-journeys'],
  'titus':          ['paul-journeys'],
  'philemon':       ['paul-journeys'],
  'hebrews':        ['holy-land','exodus','conquest'],
  'james':          ['holy-land'],
  '1peter':         ['paul-journeys','holy-land'],
  '2peter':         ['holy-land'],
  '1john':          ['seven-churches','holy-land'],
  '2john':          ['seven-churches'],
  '3john':          ['seven-churches'],
  'jude':           ['holy-land'],
  'revelation':     ['seven-churches','holy-land']
};

// Timeline era id → relevant map ids.
export var ERA_MAP_LINKS = {
  'creation':       [],
  'patriarchs':     ['ancient-near-east','patriarchal-journeys'],
  'exodus':         ['exodus','ancient-near-east'],
  'conquest':       ['conquest','twelve-tribes','judges'],
  'monarchy':       ['david-kingdom','solomon-kingdom','divided-kingdom','invasions'],
  'exile':          ['invasions','return-exile'],
  'intertestamental':['return-exile','ancient-near-east'],
  'gospels':        ['holy-land'],
  'church':         ['holy-land','paul-journeys','seven-churches'],
  'consummation':   ['seven-churches']
};
export var DEFAULT_VER      = 'BSB';           // fallback version if nothing is stored
export var COMPARE_KEY      = 'bsw_compare';   // localStorage key for the compare-mode version
export var NOTES_KEY        = 'bsw_notes';     // localStorage key for personal verse notes/highlights
export var NOTES_URL        = _resolve('../../notes/');
export var BOOKMARKS_KEY    = 'bsw_bookmarks'; // localStorage key for bookmarked verses
export var BOOKMARKS_URL    = _resolve('../../bookmarks/');
export var STRONGS_ROOT     = _resolve('../../data/strongs');      // Strong's Greek/Hebrew JSON
export var TOPICS_ROOT      = _resolve('../../topics/');
export var SW_URL           = _resolve('../../sw.js');             // service worker for PWA/offline
export var MANIFEST_URL     = _resolve('../../manifest.json');
export var SITE_ROOT        = _resolve('../../');
export var INTERLINEAR_ROOT = _resolve('../../data/interlinear'); // interlinear text per book
export var BDB_URL          = _resolve('../../data/strongs/bdb.json');    // Brown-Driver-Briggs Hebrew lexicon
export var THAYER_URL       = _resolve('../../data/strongs/thayer.json'); // Thayer's Greek lexicon
export var SMITH_IDX_URL    = _resolve('../../data/smith/index.json');    // Smith's Bible Dictionary index
export var SMITH_ENTRY_URL  = _resolve('../../data/smith/');              // individual entry JSON files
export var ISBE_IDX_URL     = _resolve('../../data/isbe/index.json');     // ISBE index
export var ISBE_ENTRY_URL   = _resolve('../../data/isbe/');               // individual ISBE entry files
export var HITCH_IDX_URL    = _resolve('../../data/hitchcock/index.json');// Hitchcock's Bible Names index
export var TORREY_URL       = _resolve('../../data/torrey/torrey.json');  // Torrey's New Topical Textbook
export var TORREY_VIDX_ROOT = _resolve('../../data/torrey/verse-index'); // per-book verse→topic index
export var LIB_DOCS_BASE    = _resolve('../../data/library/docs');        // library document JSON files
export var LIB_INDEX_URL    = _resolve('../../data/library/index.json'); // library document manifest
export var LIB_SEARCH_URL   = _resolve('../../data/library/search-index.json'); // full-text library passage index
export var TOPICS_INDEX_URL = _resolve('../../data/topics-index.json');           // study guide topic page index

// ── Library abbreviation map ──────────────────────────────────────────────
// Maps short codes used in ref strings (e.g. "wcf 3") to document slugs
// used in the library file system. Add new documents here when they are added
// to data/library/docs/.
export var LIB_ABBREV_MAP = {
  'wcf':  'westminster-confession',
  'wsc':  'westminster-shorter-catechism',
  'wlc':  'westminster-larger-catechism',
  'hc':   'heidelberg-catechism',
  'belg': 'belgic-confession',
  'cod':  'canons-of-dort',
  'lbc':  'london-baptist-confession',
  'ac':   'augsburg-confession',
  '39a':  '39-articles',
  'apos': 'apostles-creed',
  'nic':  'nicene-creed',
  'ath':  'athanasian-creed',
  'ign':  'ignatius',
  'just': 'justin-martyr',
  'iren': 'irenaeus',
  'tert': 'tertullian',
  'atha': 'athanasius',
  'chry': 'chrysostom',
  'aug':  'augustine',
  'gnaz': 'gregory-nazianzus'
};

// Maps document slugs to human-readable display names for Church Fathers.
export var FATHER_SLUGS = {
  'ignatius':          'Ignatius of Antioch',
  'justin-martyr':     'Justin Martyr',
  'irenaeus':          'Irenaeus of Lyons',
  'tertullian':        'Tertullian',
  'athanasius':        'Athanasius of Alexandria',
  'chrysostom':        'John Chrysostom',
  'augustine':         'Augustine of Hippo',
  'gregory-nazianzus': 'Gregory of Nazianzus'
};

// ── In-memory caches ──────────────────────────────────────────────────────
// All fetch caches are keyed objects; a null value means the fetch failed (don't retry).
// Using Object.create(null) avoids prototype pollution from book IDs like "constructor".
export var bookCache        = Object.create(null); // key: "VERSION:bookId" → chapters object
export var crossRefCache    = Object.create(null); // key: bookId → cross-ref object
// INTENT: Commentary cache keyed by "{srcId}/{bookId}"; value is the full
//   chapter-keyed commentary object for that book. Never evicted. A session
//   reading 20 chapters across 5 sources accumulates up to 100 entries.
// CHANGE? If commentary data format changes, clear this cache by reassigning
//   commentaryCache = Object.create(null) at the call site before re-fetching.
// VERIFY: Switch commentary source twice in the reader; the Network tab should
//   show only 2 fetches total (one per srcId×bookId pair), not one per chapter.
export var commentaryCache  = Object.create(null); // key: "source:bookId" → commentary object
export var parallelsCache   = Object.create(null); // key: bookId → parallels object
export var echoesCache      = Object.create(null); // key: bookId → echoes object
export var strongsCache     = Object.create(null); // key: "greek"|"hebrew" → dictionary object
export var interlinearCache = Object.create(null); // key: bookId → interlinear object
export var libDocCache      = Object.create(null); // key: docId → document object
export var libIndexCache    = null;                // single library manifest object
export var _lexCache        = Object.create(null); // key: "bdb"|"thayer" → lexicon object

// Smith's Bible Dictionary — split into index (terms list) and per-slug entry files.
export var _smithData = null; export var _smithMap = null; export var _smithByLetter = null;
export var _smithLoading = null; export var _smithEntryCache = {};
// ISBE — International Standard Bible Encyclopaedia (James Orr ed., 1915)
export var _isbeData = null; export var _isbeMap = null; export var _isbeByLetter = null;
export var _isbeLoading = null; export var _isbeEntryCache = {};
// Hitchcock's Bible Names — same pattern as Smith's.
export var _hitchData = null; export var _hitchMap = null; export var _hitchByLetter = null;
export var _hitchLoading = null;
// Torrey's New Topical Textbook — single JSON + per-book verse index files.
export var _torreyData = null; export var _torreyMap = null; export var _torreyByLetter = null;
export var _torreyLoading = null; export var _torreyVidxCache = {};

// metaVersions: array of version objects loaded from versions.json.
// metaBooks: array of book objects (id, name, abbrevs, testament) loaded from books.json.
// bookLookup: name/abbrev → book ID map built from metaBooks; used by normalizeBook().
// bookOrder: bookId → integer index map for canonical sort order (Genesis=0, Revelation=65).
export var metaVersions = null;
export var metaBooks    = null;
export var bookLookup   = null;
export var bookOrder    = null;

// ── Bible-ready coordination ──────────────────────────────────────────────
// Modules that need metaBooks/metaVersions to be populated before they run
// call onBibleReady(fn). app.js calls _fireBibleReady() after loadVersions()
// and loadBooks() both resolve. Any callbacks registered after that point
// fire immediately.
var _bibleReadyCallbacks = [];
var _bibleReady = false;

export function onBibleReady(fn) {
  if (_bibleReady) { fn(); } else { _bibleReadyCallbacks.push(fn); }
}

// Called once by app.js after metadata finishes loading.
export function _fireBibleReady() {
  _bibleReady = true;
  _bibleReadyCallbacks.forEach(function(fn) { fn(); });
}

// ── Version-change callback registry ─────────────────────────────────────
// Modules that need to react when the user switches Bible translation register
// a callback here. app.js fires _fireVersionChange() from the version picker's
// change event. Example uses: re-loading inline verses, updating the modal.
var _versionChangeCallbacks = [];

export function onVersionChange(fn) {
  _versionChangeCallbacks.push(fn);
}

// CHANGE? Current subscribers registered via onVersionChange (all via app.js at startup):
//   wire.js:updateInlineVerses — reloads all .bsw-verse inline embeds
//   reader.js:doLookup — re-fetches the current chapter in the new version
//   app.js:syncModalVersionPicker — updates the version selector inside the verse modal
//   daily.js — refreshes devotional verse text
//   If you add a new subscriber, append it here; if you remove one from app.js, remove it here
//   so future editors know the bus is smaller than it appears.
export function _fireVersionChange(id) {
  _versionChangeCallbacks.forEach(function(fn) { fn(id); });
}

// ── Open-modal registration ───────────────────────────────────────────────
// modal.js registers its openModal function here so wire.js can call it
// without creating a circular import (wire.js ← core.js ← modal.js would cycle).
// wire.js calls callOpenModal(); core.js dispatches to whatever is registered.
var _openModalFn = null;

export function registerOpenModal(fn) { _openModalFn = fn; }
export function callOpenModal(parsed) { if (_openModalFn) _openModalFn(parsed); }

// ── Schedule-show registration (tooltip) ─────────────────────────────────
// Same pattern as above: tooltip.js registers scheduleShow here so wire.js
// can trigger the hover tooltip without a circular import.
var _scheduleShowFn = null;

export function registerScheduleShow(fn) { _scheduleShowFn = fn; }
export function callScheduleShow(el, parsed) { if (_scheduleShowFn) _scheduleShowFn(el, parsed); }

// ── Version helpers ───────────────────────────────────────────────────────
// getVersion: reads the active translation from localStorage; falls back to DEFAULT_VER.
// Used everywhere a Bible text fetch is needed.
export function getVersion() {
  return localStorage.getItem(STORAGE_KEY) || DEFAULT_VER;
}

// setVersion: persists the chosen version, updates the picker UI, and fires
// version-change callbacks so inline verses and the modal re-load.
// VERIFY: In the version picker (any page), switch from KJV to ESV — the #bible-version
//   select should immediately show ESV, all .bsw-verse inline embeds should reload with
//   ESV text within ~500ms, and reopening the verse modal should show ESV in the version bar.
export function setVersion(id) {
  localStorage.setItem(STORAGE_KEY, id);
  var picker = document.getElementById('bible-version');
  if (picker) picker.value = id;
  _fireVersionChange(id);
}

// ── Theme ─────────────────────────────────────────────────────────────────
// Applies a data-theme attribute on <html> so CSS custom properties switch.
// Respects prefers-color-scheme if the user hasn't manually chosen a theme.
// localStorage key: bsw_theme.
var THEME_KEY = 'bsw_theme';

function _themeApply(theme) {
  document.documentElement.setAttribute('data-theme', theme);
}

export function initTheme() {
  var saved = localStorage.getItem(THEME_KEY);
  if (saved) { _themeApply(saved); return; }
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    _themeApply('dark');
  }
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
    if (!localStorage.getItem(THEME_KEY)) _themeApply(e.matches ? 'dark' : 'light');
  });
}

// _runStorageMigrations is in storage.js — re-exported from there.

// ── loadVersions / loadBooks ──────────────────────────────────────────────
// loadVersions: fetches versions.json and caches it in metaVersions.
// Returns the cached value immediately on subsequent calls.
export function loadVersions() {
  if (metaVersions) return Promise.resolve(metaVersions);
  // cache: 'no-cache' bypasses both the HTTP cache and the SW data cache so
  // newly-added translations appear immediately without requiring a SW cache bust.
  return fetch(VERSIONS_URL, { cache: 'no-cache' })
    .then(function (r) { return r.json(); })
    .then(function (data) { metaVersions = data; return data; })
    .catch(function () {
      // Degrade gracefully: allow the site to function with just KJV.
      metaVersions = [{ id: 'KJV', name: 'King James Version', tier: 1 }];
      return metaVersions;
    });
}

// loadBooks: fetches books.json and builds bookLookup and bookOrder maps.
// Must succeed before any reference parsing or search can work.
export function loadBooks() {
  if (metaBooks) return Promise.resolve(metaBooks);
  return fetch(BOOKS_URL)
    .then(function (r) { return r.json(); })
    .then(function (data) {
      metaBooks  = data;
      bookLookup = Object.create(null);
      bookOrder  = Object.create(null);
      data.forEach(function (book, idx) {
        // Index by full name, no-space name, ID, and all declared abbreviations.
        bookLookup[book.name.toLowerCase()] = book.id;
        bookLookup[book.name.toLowerCase().replace(/\s+/g, '')] = book.id;
        bookLookup[book.id] = book.id;
        (book.abbrevs || []).forEach(function (a) {
          bookLookup[a.toLowerCase()] = book.id;
        });
        bookOrder[book.id] = idx; // canonical position (0-based)
      });
      return data;
    })
    .catch(function () {
      metaBooks  = [];
      bookLookup = Object.create(null);
      return [];
    });
}

// populateVersionPicker: fills the #bible-version <select> with options from metaVersions.
// Called after loadVersions() resolves. Preserves the user's stored selection.
// INTENT: Renders only versions with actual data files; stub:true versions have empty
//   data/bible/{id}/ directories and would produce 404s on every book load.
// CHANGE? If data files are added for a stub version, remove its "stub": true field in
//   data/versions/versions.json to make it appear here and in all version-aware code.
// VERIFY: Open the version picker — AKJV, DBY, GNV, WEBBE, YLT should not appear.
export function populateVersionPicker() {
  var picker = document.getElementById('bible-version');
  if (!picker || !metaVersions) return;
  var current = getVersion();
  picker.innerHTML = '';
  metaVersions.forEach(function (v) {
    if (v.group === 'apocrypha') return;  // excluded from main reader
    if (v.stub) return;                   // no data files yet — would 404 on every load
    var opt = document.createElement('option');
    opt.value       = v.id;
    opt.textContent = v.id;
    opt.title       = v.name;
    picker.appendChild(opt);
  });
  picker.value = current;
  if (!picker.value) picker.selectedIndex = 0;
}

// wireVersionPicker: attaches the change handler to #bible-version so selecting
// a different translation calls setVersion() and triggers version-change callbacks.
export function wireVersionPicker() {
  var picker = document.getElementById('bible-version');
  if (!picker) return;
  picker.addEventListener('change', function () {
    setVersion(picker.value);
  });
}

// ── normalizeBook / parseRef / parseLibraryRef / parseMultiRef ────────────
// normalizeBook: converts any book name, abbreviation, or ID into the canonical
// book ID (e.g. "gen", "Genesis", "GEN" all → "GEN"). Returns null if unrecognized.
// Requires bookLookup to be populated (i.e. loadBooks() must have resolved).
export function normalizeBook(raw) {
  if (!bookLookup) return null;
  var s = raw.trim().toLowerCase();
  return bookLookup[s] || bookLookup[s.replace(/\s+/g, '')] || null;
}

// parseRef: parses a string like "John 3:16" or "Rev 1:1-3" into a structured
// object with bookId, chapter, verse, end chapter/verse, and a canonical display string.
// Returns null if the string is not a valid Bible reference.
// Used by wireRefLinks, handleSearchInput, the tooltip, and the modal.
export function parseRef(str) {
  if (!str) return null;
  str = str.trim().replace(/[–—]/g, '-');
  var m = str.match(
    /^((?:[1-4]\s+)?(?:[A-Za-z]+\s+)*[A-Za-z]+)\s+(\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$/
  );
  if (!m) return null;

  var bookId = normalizeBook(m[1]);
  if (!bookId) return null;

  var ch   = parseInt(m[2], 10);
  var v    = parseInt(m[3], 10);
  var endCh = m[4] ? parseInt(m[4], 10) : ch;
  var endV  = m[5] ? parseInt(m[5], 10) : v;

  // Handle cross-chapter ranges written as "John 3:36-4:1" style (endV < v).
  var crossChInferred = m[5] && !m[4] && endV < v;
  if (crossChInferred) endCh = ch + 1;

  var bookData = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
  var bookName = bookData ? bookData.name : m[1];

  var display = bookName + ' ' + ch + ':' + v;
  if (m[5]) {
    display += '–' + (m[4] ? m[4] + ':' : (crossChInferred ? endCh + ':' : '')) + m[5];
  }

  return { bookId: bookId, bookName: bookName, ch: ch, v: v,
           endCh: endCh, endV: endV, display: display, raw: str };
}

// parseLibraryRef: parses a library shortcode like "wcf 3" into a structured
// object with docId and section number. Returns null if the abbreviation is not
// in LIB_ABBREV_MAP. Used to link inline library references from topic pages.
export function parseLibraryRef(str) {
  if (!str) return null;
  var m = str.trim().match(/^([A-Za-z0-9]+)\s+(\d+)$/);
  if (!m) return null;
  var key   = m[1].toLowerCase();
  var docId = LIB_ABBREV_MAP[key];
  if (!docId) return null;
  return { docId: docId, abbrev: m[1].toUpperCase(), section: m[2] };
}

// INTENT: Parses a comma/semicolon-delimited reference list with carry-over state
//   (curBookId, curCh). Each segment that lacks a book name inherits the book from
//   the previous segment; each segment lacking a chapter inherits the current chapter.
//   This means "John 3:16, 17; Rom 5:1" correctly resolves to John 3:16, John 3:17,
//   and Romans 5:1 — but ONLY because segments are processed strictly left-to-right.
//   Out-of-order or pre-shuffled segment arrays will silently produce wrong book/chapter
//   assignments. The BARE_RE branch (bare verse number like "17") silently skips the
//   segment if curBookId or curCh is null, producing a shorter results array than
//   expected — callers must supply defaultBookId when the context book is known.
// CHANGE? If the segment-splitting regex changes (currently /[,;]/), the carry-over
//   logic must also be re-validated; semicolons and commas have identical semantics here.
//   Called by: reader.js cross-reference panel, wire.js tooltip inline expansion.
// VERIFY: In the console: parseMultiRef('John 3:16, 17; Rom 5:1') should return
//   3 objects — bookId:'john' ch:3 v:16, bookId:'john' ch:3 v:17, bookId:'rom' ch:5 v:1.
export function parseMultiRef(str, defaultBookId) {
  if (!str || !metaBooks) return [];
  str = str.trim().replace(/[–—]/g, '-');

  var FULL_RE        = /^((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+)*)\s+(\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$/;
  var FULL_CH_RE     = /^((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+)*)\s+(\d+)$/;
  var FULL_CH_RNG_RE = /^((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+)*)\s+(\d+)-(\d+)$/;
  var CH_RE          = /^(\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$/;
  var BARE_RE        = /^(\d+)(?:-(?:(\d+):)?(\d+))?$/;

  var curBookId   = defaultBookId || null;
  var curBookName = null;
  var curCh       = null;

  if (curBookId) {
    var db = metaBooks.find(function (b) { return b.id === curBookId; });
    if (db) curBookName = db.name;
  }

  var results  = [];
  var segments = str.split(/[,;]/);

  for (var i = 0; i < segments.length; i++) {
    var seg = segments[i].trim().replace(/\s*:\s*/g, ':').replace(/\s*-\s*/g, '-');
    if (!seg) continue;
    var m2, bk, ch, v, endCh, endV, disp;

    if ((m2 = seg.match(FULL_RE))) {
      var bid = normalizeBook(m2[1]);
      if (!bid) continue;
      bk    = metaBooks.find(function (b) { return b.id === bid; });
      ch    = parseInt(m2[2], 10); v = parseInt(m2[3], 10);
      endCh = m2[4] ? parseInt(m2[4], 10) : ch;
      endV  = m2[5] ? parseInt(m2[5], 10) : v;
      disp  = (bk ? bk.name : m2[1]) + ' ' + ch + ':' + v;
      if (m2[5]) disp += '–' + (m2[4] ? m2[4] + ':' : '') + m2[5];
      curBookId = bid; curBookName = bk ? bk.name : m2[1]; curCh = ch;
      results.push({ bookId: curBookId, bookName: curBookName, ch: ch, v: v, endCh: endCh, endV: endV, display: disp });

    } else if ((m2 = seg.match(FULL_CH_RE))) {
      var bid2 = normalizeBook(m2[1]);
      if (!bid2) continue;
      bk   = metaBooks.find(function (b) { return b.id === bid2; });
      ch   = parseInt(m2[2], 10);
      disp = (bk ? bk.name : m2[1]) + ' ' + ch;
      curBookId = bid2; curBookName = bk ? bk.name : m2[1]; curCh = ch;
      results.push({ bookId: curBookId, bookName: curBookName, ch: ch, v: 1, endCh: ch, endV: 9999, display: disp, wholeChapter: true });

    } else if ((m2 = seg.match(FULL_CH_RNG_RE))) {
      var bid3 = normalizeBook(m2[1]);
      if (!bid3) continue;
      bk    = metaBooks.find(function (b) { return b.id === bid3; });
      ch    = parseInt(m2[2], 10); endCh = parseInt(m2[3], 10);
      disp  = (bk ? bk.name : m2[1]) + ' ' + ch + '–' + endCh;
      curBookId = bid3; curBookName = bk ? bk.name : m2[1]; curCh = ch;
      results.push({ bookId: curBookId, bookName: curBookName, ch: ch, v: 1, endCh: endCh, endV: 9999, display: disp, wholeChapter: true });

    } else if ((m2 = seg.match(CH_RE))) {
      if (!curBookId) continue;
      ch    = parseInt(m2[1], 10); v = parseInt(m2[2], 10);
      endCh = m2[3] ? parseInt(m2[3], 10) : ch;
      endV  = m2[4] ? parseInt(m2[4], 10) : v;
      disp  = curBookName + ' ' + ch + ':' + v;
      if (m2[4]) disp += '–' + (m2[3] ? m2[3] + ':' : '') + m2[4];
      curCh = ch;
      results.push({ bookId: curBookId, bookName: curBookName, ch: ch, v: v, endCh: endCh, endV: endV, display: disp });

    } else if ((m2 = seg.match(BARE_RE))) {
      if (!curBookId || curCh === null) continue;
      v     = parseInt(m2[1], 10);
      endCh = m2[2] ? parseInt(m2[2], 10) : curCh;
      endV  = m2[3] ? parseInt(m2[3], 10) : v;
      disp  = curBookName + ' ' + curCh + ':' + v;
      if (m2[3]) disp += '–' + (m2[2] ? m2[2] + ':' : '') + m2[3];
      results.push({ bookId: curBookId, bookName: curBookName, ch: curCh, v: v, endCh: endCh, endV: endV, display: disp });
    }
  }
  return results;
}

// ── loadBook ──────────────────────────────────────────────────────────────
// Fetches a single book's text for the given version from data/bible/<VERSION>/<bookId>.json.
// Returns a promise resolving to the chapters object ({ "1": { "1": "text", … }, … }).
// Results are cached in bookCache keyed by "version:bookId"; a null cached value
// means the fetch previously failed (book doesn't exist for that version).
// MKT versions store tier name in their versions.json entry.
// Files live at data/translation/draft/<tier>/<bookId>.json with the schema
// {"ch": {"v": "text"}} — no outer wrapper — so we return data directly.
var _MKT_TIER = { 'MKT-L': 'literal', 'MKT-M': 'mediating', 'MKT-T': 'thought' };
var _MKT_ROOT = _resolve('../../data/translation/draft');

export function loadBook(version, bookId) {
  var key = version + ':' + bookId;
  if (key in bookCache) {
    return bookCache[key]
      ? Promise.resolve(bookCache[key])
      : Promise.reject(new Error('cached miss'));
  }
  var tier = _MKT_TIER[version];
  var url = tier
    ? _MKT_ROOT + '/' + tier + '/' + bookId + '.json'
    : DATA_ROOT + '/' + version + '/' + bookId + '.json';
  return fetch(url)
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      // MKT files are raw {ch:{v:text}}; standard files wrap chapters under data.chapters
      bookCache[key] = tier ? data : (data.chapters || null);
      return bookCache[key];
    })
    .catch(function (err) {
      bookCache[key] = null;
      throw err;
    });
}

// ── loadCrossRefs ─────────────────────────────────────────────────────────
// Fetches cross-reference data for a book from data/crossrefs/<bookId>.json.
// Returns null if the file doesn't exist or is empty.
// INTENT: Stores the in-flight Promise immediately so concurrent callers (up to 176 for
//   Psalm 119) share a single fetch instead of each firing a separate HTTP request.
//   Once the fetch resolves the cache entry is replaced with the plain data value so
//   Promise.resolve() returns synchronously on subsequent calls.
// CHANGE? crossRefCache is exported and read by reader.js — do not change the key format
//   (bookId string) or the resolved value shape (object keyed by "ch:v" or null).
// VERIFY: Load /read/?ref=Psalms+119 with DevTools Network open; filter by "crossrefs".
//   Exactly 1 request to crossrefs/psalms.json should appear, not 176.
export function loadCrossRefs(bookId) {
  if (bookId in crossRefCache) return Promise.resolve(crossRefCache[bookId]);
  var url = CROSSREFS_ROOT + '/' + bookId + '.json';
  // Store the promise immediately so concurrent callers reuse it (stampede prevention).
  crossRefCache[bookId] = fetch(url)
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      crossRefCache[bookId] = (data && Object.keys(data).length) ? data : null;
      return crossRefCache[bookId];
    })
    .catch(function () { crossRefCache[bookId] = null; return null; });
  return crossRefCache[bookId];
}

// ── loadParallels ─────────────────────────────────────────────────────────────
// INTENT: Loads synoptic parallel passage data for a book from data/parallels/<bookId>.json.
//   Schema: { "ch": { "v": [{end, label, type, refs:[{passage, label}]}] } }
//   Resolves null when the file is absent; callers skip injection silently.
// VERIFY: Navigate to Matthew 3 — Network tab should show one fetch to data/parallels/matthew.json;
//   navigating again to the same chapter should not re-fetch.
export function loadParallels(bookId) {
  if (bookId in parallelsCache) return Promise.resolve(parallelsCache[bookId]);
  var url = PARALLELS_ROOT + '/' + bookId + '.json';
  parallelsCache[bookId] = fetch(url)
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      parallelsCache[bookId] = (data && Object.keys(data).length) ? data : null;
      return parallelsCache[bookId];
    })
    .catch(function () { parallelsCache[bookId] = null; return null; });
  return parallelsCache[bookId];
}

// ── loadEchoes ────────────────────────────────────────────────────────────────
// INTENT: Loads OT→NT echo/allusion/typology data for a book from data/echoes/<bookId>.json.
//   Schema: { "ch": { "v": [{type, target, note}] } } — same structural pattern as crossrefs.
//   Resolves null (not a rejection) when the file is absent so callers can hide the section cleanly.
// CHANGE? echoesCache is keyed by bookId string. If the data file layout changes, update
//   ECHOES_ROOT here and vsExtractEchoes/vsRenderEchoList in verse-study.js.
// VERIFY: Open verse-study for John 1:29 — Network tab should show exactly one fetch to
//   data/echoes/john.json; repeat navigation to the same verse should show no re-fetch.
export function loadEchoes(bookId) {
  if (bookId in echoesCache) return Promise.resolve(echoesCache[bookId]);
  var url = ECHOES_ROOT + '/' + bookId + '.json';
  echoesCache[bookId] = fetch(url)
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      echoesCache[bookId] = (data && Object.keys(data).length) ? data : null;
      return echoesCache[bookId];
    })
    .catch(function () { echoesCache[bookId] = null; return null; });
  return echoesCache[bookId];
}

// ── ATTRIBUTION ──────────────────────────────────────────────────────────────
// Copyright / attribution strings displayed under rendered Bible text.
// Centralised here so adding a new version only requires one edit.
export var ATTRIBUTION = {
  'KJV':   'King James Version (1611) — Public Domain',
  'BSB':   'Berean Standard Bible — Copyright © 2022 by Bible Hub. Used by permission. All rights reserved worldwide.',
  'WEB':   'World English Bible — Public Domain',
  'ASV':   'American Standard Version (1901) — Public Domain',
  'MKT-L': 'Modern Kingdom Translation — Literal Tier. AI-assisted from Hebrew/Greek interlinear; overseen by David Seis. See <a href="/about/">About</a> for methods.',
  'MKT-M': 'Modern Kingdom Translation — Mediating Tier. AI-assisted from Hebrew/Greek interlinear; overseen by David Seis. See <a href="/about/">About</a> for methods.',
  'MKT-T': 'Modern Kingdom Translation — Thought Tier. AI-assisted from Hebrew/Greek interlinear; overseen by David Seis. See <a href="/about/">About</a> for methods.'
};

// ── COMMENTARY_SOURCES / loadCommentary ──────────────────────────────────
// Defines the available commentary sources. The default source (mhcc) lives at
// data/commentary/<bookId>.json; all others live at data/commentary/<source>/<bookId>.json.
// Users can switch sources via the verse modal.
export var COMMENTARY_SOURCES = [
  // 'Cloud of Witnesses' is the project name for this patristic layer; the internal
  // id is 'cow' (data path data/commentary/cow/, decorateCatena guard). The attr
  // keeps honest credit to the underlying texts — Catena Aurea for the Gospels,
  // plus Church Fathers and Reformers covering the full Bible.
  { id: 'cow',  label: 'Cloud of Witnesses — Church Fathers', attr: "Cloud of Witnesses — a great cloud of witnesses (Heb 12:1), the historic church on every verse across the whole Bible. Primary text: Catena Aurea, Thomas Aquinas's chain of patristic comment (tr. J.H. Newman, 1841); supplemented by Chrysostom, Augustine, Calvin, Wesley, and many others. Public Domain." },
  // 'cow-synthesis' distils ALL the Cloud-of-Witnesses voices on a verse into one ~500-word
  // grounded summary (one HTML blob per verse, NOT the multi-voice format — so it renders plain,
  // not via decorateCatena, whose guard is `=== 'cow'`). Data: data/commentary/cow-synthesis/{book}/{ch}.json.
  { id: 'cow-synthesis', label: 'Cloud of Witnesses — Synthesis', attr: 'Cloud of Witnesses — Synthesis. An AI-assisted distillation of the historic church’s voices (see the Cloud of Witnesses source) into one summary per verse. Grounded in the public-domain texts listed there; see /about/ for methods. AI-assisted.', isAI: true },
  // 'mkt' is a composite: three sub-sources loaded in parallel and shown as expandable cards.
  // The actual data lives at mkt-original/, mkt-context/, mkt-christ/ — 'mkt' has no folder.
  { id: 'mkt', label: 'MKT Commentary', attr: 'MKT Commentary. AI-assisted; see /about/ for methods and prompts.', isAI: true }
];

// Active commentary source — always read from localStorage so changes made in
// one module (modal, verse-study) are immediately visible in all others.
export function getCommentarySource() {
  try {
    var src = localStorage.getItem('bsw_comm_src') || 'cow';
    // Migrate old split mkt-* IDs to the unified 'mkt' entry
    if (src === 'mkt-original' || src === 'mkt-context' || src === 'mkt-christ') return 'mkt';
    // Migrate old 'catena' id → 'cow'; migrate removed single-source commentaries (folded into Cloud of Witnesses)
    if (src === 'catena' || src === 'mhcc' || src === 'mhc' || src === 'ellicott' || src === 'jfb' ||
        src === 'clarke' || src === 'calvin' || src === 'barnes' || src === 'rwp' ||
        src === 'wesley') return 'cow';
    return src;
  } catch (e) { return 'cow'; }
}
export function setCommentarySource(id) {
  try { localStorage.setItem('bsw_comm_src', id); } catch (e) {}
}

// INTENT: Fetch commentary for the ACTIVE CHAPTER only — data/commentary/{src}/{book}/{ch}.json
//   (mhcc: data/commentary/{book}/{ch}.json) — instead of the whole book. A verse tap used to
//   pull the entire book file (Psalms + Cloud of Witnesses = 14 MB!); now it costs ~tens of KB.
//   The per-chapter file is {v:html}; we wrap it back to the {ch:{v:html}} shape every caller
//   (_extractCommHtml, comm-mode, MKT) already indexes via data[ch], so no caller logic changed.
// CHANGE? Files are produced by scripts/split-commentary.py and (for cow) cow-merge.py. If a
//   per-chapter file is absent we fall back to the whole-book file, so un-split sources still
//   work. commentaryCache key is now source:bookId:ch. Callers must pass ch (parsed.ch).
// VERIFY: Open Psalms 119 → DevTools Network shows commentary/.../psalms/119.json (~tens of KB),
//   not psalms.json (MB). Switch sources → each fetches its own per-chapter file once.
export function loadCommentary(bookId, source, ch) {
  source = source || getCommentarySource();
  var base = source === 'mhcc'
    ? COMMENTARY_ROOT + '/' + bookId
    : COMMENTARY_ROOT + '/' + source + '/' + bookId;
  var key = source + ':' + bookId + (ch != null ? ':' + ch : '');
  if (key in commentaryCache) return Promise.resolve(commentaryCache[key]);

  function fetchWholeBook() {
    return fetch(base + '.json')
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (data) {
        commentaryCache[key] = (data && Object.keys(data).length) ? data : null;
        return commentaryCache[key];
      })
      .catch(function () { commentaryCache[key] = null; return null; });
  }
  if (ch == null) return fetchWholeBook();   // legacy/whole-book callers

  return fetch(base + '/' + ch + '.json')
    .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
    .then(function (data) {
      var wrapped = (data && Object.keys(data).length) ? (function () { var o = {}; o[String(ch)] = data; return o; })() : null;
      commentaryCache[key] = wrapped;
      return wrapped;
    })
    .catch(function () { return fetchWholeBook(); });   // per-chapter missing → whole-book fallback
}

// ── MKT Commentary — multi-card loader + renderer ─────────────────────────
// INTENT: 'mkt' is a composite of three sub-sources (original, context, christ) shown as
//   three expandable <details> cards. loadMktAll fetches all three in parallel; decorateMkt
//   renders already-extracted per-verse HTML blobs into the card layout. Callers extract
//   per-verse HTML from each dataset using the normal _extractCommHtml helper, then pass
//   the three html strings here.
// CHANGE? If a fourth MKT track is added, append it to MKT_TRACKS and add a parameter to
//   decorateMkt. If the card HTML structure changes, update .mkt-card CSS in style.css.
// VERIFY: Open a verse with MKT Commentary selected → three cards labelled Original Language,
//   Historical Context, Christ in Every Verse appear; all start collapsed.
var MKT_TRACKS = [
  { id: 'mkt-original', title: 'Original Language' },
  { id: 'mkt-context',  title: 'Historical Context' },
  { id: 'mkt-christ',   title: 'Christ in Every Verse' }
];
export function loadMktAll(bookId, ch) {
  return Promise.all(MKT_TRACKS.map(function (t) { return loadCommentary(bookId, t.id, ch); }));
}
export function decorateMkt(htmls) {
  // htmls is an array of [origHtml, contextHtml, christHtml], any may be null
  return MKT_TRACKS.map(function (t, i) {
    var html = htmls[i];
    var openAttr = '';
    var body = html
      ? '<div class="mkt-card__body">' + html + '</div>'
      : '<div class="mkt-card__body mkt-card__body--empty"><p>No commentary for this verse.</p></div>';
    return '<details class="mkt-card"' + openAttr + '>' +
           '<summary class="mkt-card__head"><span class="mkt-card__title">' + escHtml(t.title) + '</span></summary>' +
           body + '</details>';
  }).join('');
}

// ── Cloud of Witnesses voice metadata + decorator ────────────────────────
// INTENT: The 'cow' source stacks many Church-Father voices per pericope.
//   decorateCatena() rewrites each "<p><strong>Name:</strong> …</p>" voice emitted
//   by cow-merge.py into a collapsible <details> carrying name + tradition + period
//   badges, canonicalising the (sometimes abbreviated) source name via CATENA_FATHERS.
//   It is applied at every cow render site (modal commentary, reader side-panel,
//   reader inline grid, verse-study).
// CHANGE? If cow-merge.py introduces a NEW Father tag, add its lowercased form to
//   a row below — otherwise it renders name-only (no badges), which is the safe
//   fallback. If cow-merge.py's per-voice markup changes from
//   "<p><strong>Name:</strong> body</p>", update _CATENA_VOICE_RE to match.
// VERIFY: Open any verse → switch source to Cloud of Witnesses; each voice has a ▸
//   disclosure toggle and two badges (tradition, period); collapsing one hides only
//   its body. An unrecognised Father shows its name with no badge.
// Rows: [displayName, tradition, period, [raw variant tags, lowercased]]
var _CATENA_ROWS = [
  // Greek (Eastern) Fathers
  ['John Chrysostom','Greek','c. 349–407',['chrysostom']],
  ['Pseudo-Chrysostom','Greek','5th c.',['pseudo-chrysostom','pseudo-chys']],
  ['Origen','Greek','c. 185–253',['origen']],
  ['Pseudo-Origen','Greek','',['pseudo-origen']],
  ['Cyril of Jerusalem','Greek','c. 313–386',['cyril of jerusalem']],
  ['Cyril of Alexandria','Greek','c. 376–444',['cyril','cyril of alexandria']],
  ['Basil the Great','Greek','c. 330–379',['basil']],
  ['Pseudo-Basil','Greek','',['pseudo-basil']],
  ['Eusebius of Caesarea','Greek','c. 263–339',['eusebius']],
  ['Gregory of Nyssa','Greek','c. 335–395',['gregory of nyssa']],
  ['Gregory Nazianzen','Greek','c. 329–390',['gregory nazianzen']],
  ['Athanasius','Greek','c. 296–373',['athan','pseudo-athan']],
  ['Theophylact','Greek (Byzantine)','c. 1055–1107',['theophylact']],
  ['Titus of Bostra','Greek','d. c. 378',['titus bost','titus bostrensis']],
  ['John of Damascus','Greek','c. 675–749',['damascene']],
  ['Theodotus of Ancyra','Greek','d. c. 446',['theodotus']],
  ['Theodoret of Cyrrhus','Greek','c. 393–457',['theodoret','theodoret of cyrrhus']],
  ['Dionysius the Areopagite','Greek','c. 500',['dionys','dionysius ar']],
  ['Epiphanius','Greek','c. 310–403',['epiphan']],
  ['Gennadius','Greek','d. 471',['gennadius']],
  ['Nemesius of Emesa','Greek','fl. c. 390',['nemesius']],
  ['Maximus','Greek','',['maxim']],
  ['Isidore of Pelusium','Greek','d. c. 450',['isidore peleus']],
  ['Greek Exposition','Greek','',['greek ex']],
  // Latin (Western) Fathers
  ['Augustine of Hippo','Latin','354–430',['augustine']],
  ['Pseudo-Augustine','Latin','',['pseudo-augustine']],
  ['Jerome','Latin','c. 347–420',['jerome']],
  ['Pseudo-Jerome','Latin','',['pseudo-jerome']],
  ['Hilary of Poitiers','Latin','c. 310–367',['hilary','hil']],
  ['Gregory the Great','Latin','c. 540–604',['gregory']],
  ['Ambrose of Milan','Latin','c. 339–397',['ambrose']],
  ['Leo the Great','Latin','c. 400–461',['leo']],
  ['Tertullian','Latin','c. 155–220',['tertullian']],
  ['Cyprian of Carthage','Latin','c. 210–258',['cyprian']],
  ['Victorinus of Pettau','Latin','d. c. 304',['victorinus']],
  ['Peter Chrysologus','Latin','c. 380–450',['chrysol','chrysologus']],
  ['Isidore of Seville','Latin','c. 560–636',['isidore']],
  // Medieval (Western) compilers
  ['Bede','Medieval','c. 673–735',['bede']],
  ['Alcuin of York','Medieval','c. 735–804',['alcuin']],
  ['Rabanus Maurus','Medieval','c. 780–856',['raban','rabanus']],
  ['Remigius of Auxerre','Medieval','c. 841–908',['remigius']],
  ['Haymo of Halberstadt','Medieval','d. 853',['haymo']],
  ['Glossa Ordinaria','Medieval','12th c.',['gloss']],
  ['Petrus Alfonsi','Medieval','12th c.',['petrus alfonsus']],
  // Conciliar
  ['Council of Ephesus','Council','431',['the council of ephesus']],
  // Post-Reformation commentators
  ['John Gill','Reformed','1697–1771',['john gill','gill']],
  ['Keil and Delitzsch','Lutheran','1866–1891',['keil','keil and delitzsch','kd','keil-delitzsch']],
  ['John Lightfoot','Reformed','1602–1675',['john lightfoot','lightfoot']],
  ['Matthew Henry','Reformed','1662–1714',['matthew henry']],
  ['Albert Barnes','Reformed','1798–1870',['albert barnes','barnes']],
  ['Adam Clarke','Methodist','1762–1832',['adam clarke','clarke']],
  ['Charles Ellicott','Anglican','1819–1905',['charles ellicott','ellicott']],
  ['Jamieson, Fausset and Brown','Reformed','1871',['jamieson, fausset and brown','jfb','jamieson']],
  ['A.T. Robertson','Baptist','1863–1934',['a.t. robertson','robertson']],
  ['John Calvin','Reformed','1509–1564',['john calvin','calvin']],
  ['John Wesley','Methodist','1703–1791',['john wesley','wesley']],
  ['C.H. Spurgeon','Reformed','1834–1892',['c.h. spurgeon','spurgeon']],
  ['Martin Luther','Lutheran','1483–1546',['martin luther','luther']]
];
export var CATENA_FATHERS = (function () {
  var m = Object.create(null);
  _CATENA_ROWS.forEach(function (r) {
    r[3].forEach(function (v) { m[v] = { display: r[0], tradition: r[1], period: r[2] }; });
  });
  return m;
})();
function _catenaTradClass(t) {
  if (t === 'Greek' || t === 'Greek (Byzantine)') return 'greek';
  if (t === 'Latin') return 'latin';
  if (t === 'Medieval') return 'medieval';
  if (t === 'Council') return 'ecumenical';
  if (t === 'Reformed') return 'reformed';
  if (t === 'Lutheran') return 'lutheran';
  if (t === 'Methodist') return 'methodist';
  if (t === 'Anglican') return 'anglican';
  if (t === 'Baptist') return 'baptist';
  return 'other';
}
// Each known Father's name links to their Biblepedia article at {biblepedia}?a={slug}.
// The slug must match the article filename produced by scripts/cow-father-articles.py
// — keep _cowSlug identical to that script's slugify (lowercase, non-alnum→'-').
var _COW_BP_URL = _resolve('../../biblepedia/');
export function cowSlug(name) {
  return String(name).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}
var _CATENA_VOICE_RE = /<p><strong>([^:<]+):<\/strong>\s*([\s\S]*?)<\/p>/g;
// INTENT: Rewrite each "<p><strong>Name:</strong> body</p>" voice into a collapsible
//   <details> carrying tradition/period badges. data-voice holds the cowSlug so the
//   voice filter (buildCatenaFilter) can show/hide by slug without re-parsing HTML.
// CHANGE? If voice HTML structure changes here, update buildCatenaFilter's querySelector
//   and the .catena-voice[data-voice] CSS rule in style.css.
// VERIFY: Open any verse with Cloud of Witnesses ('cow') → voices show collapsible cards with name + badges.
export function decorateCatena(html) {
  if (!html || html.indexOf('<strong>') < 0) return html;
  return html.replace(_CATENA_VOICE_RE, function (_m, name, body) {
    var meta = CATENA_FATHERS[name.trim().toLowerCase()];
    var display = meta ? meta.display : name.trim();
    var slug = cowSlug(display);
    // Known Fathers get a clickable name → their Biblepedia entry; unknown raw tags
    // (e.g. a malformed "Pseudo-") render as plain text since they have no article.
    var head = meta
      ? '<a class="cv-name" target="_blank" rel="noopener" href="' + _COW_BP_URL +
        '?a=' + cowSlug(meta.display) + '">' + escHtml(display) + '</a>'
      : '<span class="cv-name">' + escHtml(display) + '</span>';
    if (meta && meta.tradition)
      head += '<span class="cv-badge cv-' + _catenaTradClass(meta.tradition) + '">' +
              escHtml(meta.tradition) + '</span>';
    if (meta && meta.period)
      head += '<span class="cv-badge cv-period">' + escHtml(meta.period) + '</span>';
    return '<details class="catena-voice" data-voice="' + escHtml(slug) + '"><summary class="cv-head">' + head +
           '</summary><div class="cv-body"><p>' + body + '</p></div></details>';
  });
}

// INTENT: Build a voice-filter chip bar above a rendered catena block. Voices toggled
//   off are hidden via CSS (.catena-voice--hidden). Hidden state persists across verse
//   navigation within a session (module-level Set) so a user who hides Keil & Delitzsch
//   sees it hidden on the next verse too. Filter only renders when ≥2 voices are present.
// CHANGE? If decorateCatena's data-voice attr or .cv-name selector changes, update
//   the querySelectorAll calls below. Chip styles live in style.css (.catena-filter*).
// VERIFY: Open a verse with 3+ voices → filter chips appear; toggle one off → that
//   voice disappears; navigate to next verse → the same voice stays hidden.
// Exclusions are a GLOBAL, persisted preference (localStorage 'bsw_cow_hidden'): hiding a
// Father applies to every verse and every render site, now and after reload.
var _COW_HIDDEN_KEY = 'bsw_cow_hidden';
var _hiddenCatenaVoices = (function () {
  try { return new Set(JSON.parse(localStorage.getItem(_COW_HIDDEN_KEY) || '[]')); }
  catch (e) { return new Set(); }
})();
function _saveHiddenCatena() {
  try { localStorage.setItem(_COW_HIDDEN_KEY, JSON.stringify(Array.prototype.slice.call(_hiddenCatenaVoices))); } catch (e) {}
}
// Apply the current hidden set to EVERY catena voice on the page and sync EVERY chip, so
// toggling one Father updates all rendered verses (e.g. the inline grid) at once.
function _applyCatenaHiddenGlobally() {
  document.querySelectorAll('.catena-voice[data-voice]').forEach(function (el) {
    el.classList.toggle('catena-voice--hidden', _hiddenCatenaVoices.has(el.dataset.voice));
  });
  document.querySelectorAll('.catena-filter__chip[data-voice]').forEach(function (chip) {
    var hidden = _hiddenCatenaVoices.has(chip.dataset.voice);
    chip.classList.toggle('catena-filter__chip--off', hidden);
    chip.setAttribute('aria-pressed', String(!hidden));
  });
}
export function buildCatenaFilter(container) {
  if (!container) return;
  var voiceEls = container.querySelectorAll('.catena-voice[data-voice]');
  if (voiceEls.length < 2) return;

  var voices = [];
  var seen = Object.create(null);
  voiceEls.forEach(function (el) {
    var slug = el.dataset.voice;
    if (slug && !seen[slug]) {
      seen[slug] = true;
      var nameEl = el.querySelector('.cv-name');
      voices.push({ slug: slug, label: nameEl ? nameEl.textContent.trim() : slug });
    }
  });
  if (voices.length < 2) return;

  var bar = document.createElement('div');
  bar.className = 'catena-filter';
  bar.setAttribute('aria-label', 'Filter voices');

  voices.forEach(function (v) {
    var chip = document.createElement('button');
    chip.type = 'button';
    chip.textContent = v.label;
    chip.dataset.voice = v.slug;
    var isHidden = _hiddenCatenaVoices.has(v.slug);
    chip.className = 'catena-filter__chip' + (isHidden ? ' catena-filter__chip--off' : '');
    chip.setAttribute('aria-pressed', String(!isHidden));
    chip.addEventListener('click', function () {
      var nowHidden = !_hiddenCatenaVoices.has(v.slug);
      if (nowHidden) _hiddenCatenaVoices.add(v.slug);
      else           _hiddenCatenaVoices.delete(v.slug);
      _saveHiddenCatena();
      _applyCatenaHiddenGlobally();   // update all verses + all chip bars on the page
    });
    bar.appendChild(chip);
  });

  // INTENT: Expand/collapse-all toggle sits at the right end of the filter bar.
  //   Voices start closed (no `open` attr in decorateCatena), so the button's initial
  //   label is "Expand all". It toggles the `open` attr on all non-hidden voices within
  //   this container only — it's a local display convenience, not a persisted preference.
  // CHANGE? If the container scope changes (e.g. multi-verse grid), update the
  //   querySelectorAll selector here. The button's `aria-expanded` mirrors the expand state.
  // VERIFY: Cloud of Witnesses panel → voices all closed; click "Expand all" → all open;
  //   click "Collapse all" → all closed. Chip filters still work independently.
  var toggleBtn = document.createElement('button');
  toggleBtn.type = 'button';
  toggleBtn.className = 'catena-filter__toggle';
  toggleBtn.textContent = 'Expand all';
  toggleBtn.setAttribute('aria-expanded', 'false');
  toggleBtn.addEventListener('click', function () {
    var expanding = toggleBtn.getAttribute('aria-expanded') === 'false';
    container.querySelectorAll('.catena-voice:not(.catena-voice--hidden)').forEach(function (el) {
      if (expanding) el.setAttribute('open', '');
      else           el.removeAttribute('open');
    });
    toggleBtn.setAttribute('aria-expanded', String(expanding));
    toggleBtn.textContent = expanding ? 'Collapse all' : 'Expand all';
  });
  bar.appendChild(toggleBtn);

  // Apply persisted hidden state to freshly rendered voices
  _hiddenCatenaVoices.forEach(function (slug) {
    container.querySelectorAll('.catena-voice[data-voice="' + slug + '"]').forEach(function (el) {
      el.classList.add('catena-voice--hidden');
    });
  });

  var first = container.querySelector('.catena-voice');
  if (first) container.insertBefore(bar, first);
}

// UX-16: the .cv-name link lives inside the voice's <summary>, so a plain click would
//   BOTH open the Biblepedia article and toggle the <details>. A delegated capture-phase
//   listener cancels the click's default action (which includes the summary toggle) and
//   opens the article in a new tab itself, so following the link never collapses the voice.
// CHANGE? Targets `a.cv-name` produced by decorateCatena above; if that class/structure
//   changes, update the selector. One listener covers every render site (modal, reader
//   panel, reader grid, verse-study) since they all inject decorateCatena output.
// VERIFY: Open a Gospel verse → Cloud of Witnesses; click a Father name — the article opens
//   in a new tab and the voice's expanded/collapsed state is unchanged.
if (typeof document !== 'undefined') {
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a.cv-name');
    if (!a) return;
    e.preventDefault();
    window.open(a.href, '_blank', 'noopener');
  });
}

// ── parseCrossRefEntry / crossRefScore / computeTextSimilarity ────────────
// parseCrossRefEntry: normalises a cross-ref entry which may be a string,
// a [ref, votes] array, or an {r, v} object into a consistent {ref, votes} shape.
export function parseCrossRefEntry(entry) {
  if (typeof entry === 'string') return { ref: entry, votes: 1 };
  if (Array.isArray(entry))     return { ref: entry[0] || '', votes: entry[1] || 1 };
  if (entry && typeof entry === 'object') return { ref: entry.r || '', votes: entry.v || 1 };
  return { ref: String(entry), votes: 1 };
}

// crossRefScore: converts raw vote count to a 0-100 relevance percentage
// (25 votes = 100%). Displayed as a confidence indicator in the cross-ref panel.
export function crossRefScore(entry) {
  return Math.min(100, Math.round(((entry.votes || 1) / 25) * 100));
}

// computeTextSimilarity: Jaccard-style word overlap score (0-100) between two
// strings, after removing stop words and short tokens. Used as a fallback
// relevance signal when a verse doesn't contain the exact search phrase.
export function computeTextSimilarity(textA, textB) {
  var STOP = {
    the:1,a:1,an:1,and:1,or:1,but:1,in:1,of:1,to:1,is:1,was:1,
    he:1,she:1,it:1,that:1,this:1,his:1,her:1,their:1,for:1,with:1,
    by:1,at:1,from:1,are:1,were:1,be:1,has:1,have:1,had:1,not:1,
    on:1,as:1,so:1,if:1,then:1,which:1,who:1,whom:1,shall:1,said:1,
    them:1,they:1,we:1,you:1,my:1,your:1,our:1,him:1,us:1,me:1,
    i:1,will:1,unto:1,thee:1,thou:1,thy:1,ye:1,hath:1,doth:1
  };
  function wordSet(t) {
    var s = Object.create(null);
    t.toLowerCase().replace(/[^a-z\s]/g, '').split(/\s+/).forEach(function (w) {
      if (w.length >= 3 && !STOP[w]) s[w] = 1;
    });
    return s;
  }
  var sA = wordSet(textA), sB = wordSet(textB);
  var inter = 0, union = 0;
  var seen  = Object.create(null);
  function tally(w) {
    if (seen[w]) return; seen[w] = 1;
    var inA = !!sA[w], inB = !!sB[w];
    if (inA && inB) inter++;
    union++;
  }
  Object.keys(sA).forEach(tally);
  Object.keys(sB).forEach(tally);
  return union ? Math.round((inter / union) * 100) : 0;
}

// ── _scoreResult / _canonicalKey / _compareCanonical ─────────────────────
// _scoreResult: primary relevance score for search results (0-100).
// Exact phrase match → 100.
// Multi-word query where all words appear → 80.
// Multi-word query where some words appear → 20–79 proportional to match count.
// Single word with no exact match → Jaccard similarity fallback.
export function _scoreResult(text, query) {
  var tl = text.toLowerCase();
  var ql = query.toLowerCase().trim();
  if (tl.indexOf(ql) !== -1) return 100;
  var words = ql.split(/\s+/).filter(Boolean);
  if (words.length > 1) {
    var matched = words.filter(function (w) { return tl.indexOf(w) !== -1; }).length;
    if (matched === words.length) return 80;
    if (matched > 0) return Math.round(20 + 60 * matched / words.length);
    return 0;
  }
  return computeTextSimilarity(query, text);
}

// _canonicalKey: returns [bookIndex, ch, v] for sorting refs in Bible order.
export function _canonicalKey(refStr) {
  var p = parseRef(refStr);
  if (!p) return [999, 0, 0];
  var idx = (bookOrder && p.bookId in bookOrder) ? bookOrder[p.bookId] : 999;
  return [idx, p.ch, p.v];
}

// _compareCanonical: comparator for Array.sort() that orders cross-ref entries
// from Genesis to Revelation, then by chapter, then by verse.
export function _compareCanonical(a, b) {
  var ka = _canonicalKey(a.ref), kb = _canonicalKey(b.ref);
  return ka[0] - kb[0] || ka[1] - kb[1] || ka[2] - kb[2];
}

// ── resolveVerses ─────────────────────────────────────────────────────────
// INTENT: Accepts a parsed ref and a version ID; returns a Promise of verse
//   objects ({ref, chapter, verse, text}). Loads the entire book JSON via
//   loadBook() which caches the result in bookCache — so the first call per
//   book/version fetches the file; all subsequent chapter lookups within that
//   book are synchronous cache hits with no additional network activity.
// CHANGE? If the bible data format changes (e.g. {c, v, text} → {chapter,
//   verse, t}), update both the fetch path in loadBook() and the verse-object
//   shape consumed by reader.js, compare.js, and the verse modal.
// VERIFY: Look up "John 3" in the reader; DevTools Network should show exactly
//   one fetch for John's book JSON. Then look up "John 4" — no new fetch.
export function resolveVerses(parsedRef, versionId) {
  var bookId   = parsedRef.bookId;
  var ch       = parsedRef.ch;
  var v        = parsedRef.v;
  var endCh    = parsedRef.endCh;
  var endV     = parsedRef.endV;
  var bookName = parsedRef.bookName;

  return loadBook(versionId, bookId).then(function (chapters) {
    if (!chapters) return null;
    var results = [];

    for (var c = ch; c <= endCh; c++) {
      var chData = chapters[String(c)];
      if (!chData) continue;
      var startV = (c === ch)    ? v    : 1;
      var stopV  = (c === endCh) ? endV : 9999;

      Object.keys(chData)
        .map(Number)
        .filter(function (n) { return n >= startV && n <= stopV; })
        .sort(function (a, b) { return a - b; })
        .forEach(function (vNum) {
          results.push({
            ref:     bookName + ' ' + c + ':' + vNum,
            chapter: c,
            verse:   vNum,
            text:    chData[String(vNum)]
          });
        });

      if (c === endCh && ch === endCh) {
        results.chapterMaxV = Math.max.apply(null, Object.keys(chData).map(Number));
      }
    }
    return results.length ? results : null;
  });
}

// ── Strong's / Lexicon / Interlinear loaders ──────────────────────────────
// loadStrongs: fetches data/strongs/greek.json or data/strongs/hebrew.json.
// Returns the full dictionary object keyed by Strong's number (e.g. "G1722").
export function loadStrongs(testament) {
  if (strongsCache[testament]) return Promise.resolve(strongsCache[testament]);
  var url = STRONGS_ROOT + '/' + testament + '.json';
  return fetch(url)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) { strongsCache[testament] = data; return data; });
}

// loadLexicon: fetches BDB (Hebrew) or Thayer (Greek) extended lexicon entries.
// type must be 'bdb' or 'thayer'.
export function loadLexicon(type) {
  if (_lexCache[type]) return Promise.resolve(_lexCache[type]);
  var url = type === 'bdb' ? BDB_URL : THAYER_URL;
  return fetch(url)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) { _lexCache[type] = data; return data; });
}

// loadInterlinear: fetches the interlinear word data for a given book.
// Returns null if the file doesn't exist (not all books have interlinear data).
// INTENT: Stores the in-flight Promise in interlinearCache immediately so concurrent callers
//   (e.g. word.js firing 27–39 fetches at once) share a single fetch per book, not N fetches.
//   The cache entry is replaced with the resolved data once the fetch settles.
// CHANGE? If interlinearCache key format changes, also update the `!== undefined` guard.
//   word.js reads this cache indirectly by calling loadInterlinear per book in batches.
// VERIFY: Open DevTools → Network → filter 'interlinear'. Load a word lookup (e.g. G3056).
//   Each book file should appear exactly once even though multiple calls may fire concurrently.
export function loadInterlinear(bookId) {
  if (interlinearCache[bookId] !== undefined) return Promise.resolve(interlinearCache[bookId]);
  var url = INTERLINEAR_ROOT + '/' + bookId + '.json';
  return (interlinearCache[bookId] = fetch(url)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (data) { interlinearCache[bookId] = data; return data; })
    .catch(function () { interlinearCache[bookId] = null; return null; }));
}

// ── Smith's Bible Dictionary loaders ─────────────────────────────────────
// _smithLoad: fetches data/smith/index.json (all terms) and builds lookup maps.
// Returns a single shared promise so multiple callers don't trigger duplicate fetches.
export function _smithLoad() {
  if (_smithLoading) return _smithLoading;
  _smithLoading = fetch(SMITH_IDX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      _smithData     = data;
      _smithMap      = {};       // id → entry
      _smithByLetter = {};       // first letter → entries array (for A-Z browse)
      data.forEach(function (e) {
        _smithMap[e.id] = e;
        var letter = e.term.charAt(0).toUpperCase();
        if (!_smithByLetter[letter]) _smithByLetter[letter] = [];
        _smithByLetter[letter].push(e);
      });
    });
  return _smithLoading;
}

// _smithLoadEntry: fetches the full article for a single Smith's entry by slug.
export function _smithLoadEntry(slug) {
  if (_smithEntryCache[slug]) return Promise.resolve(_smithEntryCache[slug]);
  return fetch(SMITH_ENTRY_URL + slug + '.json')
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (d) { _smithEntryCache[slug] = d; return d; });
}

// ── ISBE loaders ─────────────────────────────────────────────────────────
// INTENT: mirrors _smithLoad / _smithLoadEntry — single shared promise prevents duplicate fetches.
// CHANGE? If ISBE_IDX_URL or ISBE_ENTRY_URL paths change, update the constants above and
//   the ISBE_VIDX_URL in library.js; also re-run scripts/fetch-isbe.py.
// VERIFY: Open dictionary page; ISBE filter chip appears and A-Z entries load on click.
export function _isbeLoad() {
  if (_isbeLoading) return _isbeLoading;
  _isbeLoading = fetch(ISBE_IDX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      _isbeData     = data;
      _isbeMap      = {};
      _isbeByLetter = {};
      data.forEach(function (e) {
        _isbeMap[e.id] = e;
        var letter = e.term.charAt(0).toUpperCase();
        if (!_isbeByLetter[letter]) _isbeByLetter[letter] = [];
        _isbeByLetter[letter].push(e);
      });
    });
  return _isbeLoading;
}

export function _isbeLoadEntry(slug) {
  if (_isbeEntryCache[slug]) return Promise.resolve(_isbeEntryCache[slug]);
  return fetch(ISBE_ENTRY_URL + slug + '.json')
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (d) { _isbeEntryCache[slug] = d; return d; });
}

// ── Hitchcock's Bible Names loader ────────────────────────────────────────
// Same structure as Smith's — index + letter map for A-Z browse.
export function _hitchLoad() {
  if (_hitchLoading) return _hitchLoading;
  _hitchLoading = fetch(HITCH_IDX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      _hitchData     = data;
      _hitchMap      = {};
      _hitchByLetter = {};
      data.forEach(function (e) {
        _hitchMap[e.id] = e;
        var letter = e.term.charAt(0).toUpperCase();
        if (!_hitchByLetter[letter]) _hitchByLetter[letter] = [];
        _hitchByLetter[letter].push(e);
      });
    });
  return _hitchLoading;
}

// ── Torrey's New Topical Textbook loaders ─────────────────────────────────
// _torreyLoad: fetches the full Torrey JSON (all topics + verse lists).
// _torreyLoadVidx: fetches the per-book verse index so the verse modal can
// quickly find which Torrey topics mention a given verse.
export function _torreyLoad() {
  if (_torreyLoading) return _torreyLoading;
  _torreyLoading = fetch(TORREY_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      _torreyData     = data;
      _torreyMap      = {};       // slug → topic
      _torreyByLetter = {};       // first letter → topics array
      data.forEach(function (t) {
        _torreyMap[t.slug] = t;
        var letter = t.title.charAt(0).toUpperCase();
        if (!_torreyByLetter[letter]) _torreyByLetter[letter] = [];
        _torreyByLetter[letter].push(t);
      });
    });
  return _torreyLoading;
}

export function _torreyLoadVidx(bookId) {
  if (_torreyVidxCache[bookId] !== undefined) return Promise.resolve(_torreyVidxCache[bookId]);
  return fetch(TORREY_VIDX_ROOT + '/' + bookId + '.json')
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { _torreyVidxCache[bookId] = d || {}; return _torreyVidxCache[bookId]; })
    .catch(function () { _torreyVidxCache[bookId] = {}; return {}; });
}

// _torreyTopicsForVerse: returns all Torrey topics that cite the given parsed ref.
// Requires both _torreyLoad() and the verse's book index to be loaded.
export function _torreyTopicsForVerse(parsed) {
  if (!parsed || !parsed.bookId || !parsed.v) return Promise.resolve([]);
  return Promise.all([_torreyLoad(), _torreyLoadVidx(parsed.bookId)]).then(function () {
    var key   = parsed.ch + ':' + parsed.v;
    var vidx  = _torreyVidxCache[parsed.bookId] || {};
    var slugs = vidx[key] || [];
    return slugs.map(function (s) { return _torreyMap && _torreyMap[s]; }).filter(Boolean);
  });
}

// ── Library doc loader ────────────────────────────────────────────────────
// _loadLibDoc: fetches a single library document (confession, catechism, etc.)
// from data/library/docs/<docId>.json. Cached by docId.
export function _loadLibDoc(docId) {
  if (libDocCache[docId]) return Promise.resolve(libDocCache[docId]);
  var url = LIB_DOCS_BASE + '/' + docId + '.json';
  return fetch(url)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (d) { libDocCache[docId] = d; return d; });
}

// _loadLibIndex: fetches data/library/index.json — the manifest of all
// available library documents (id, title, type, sections count, etc.).
export function _loadLibIndex() {
  if (libIndexCache) return Promise.resolve(libIndexCache);
  return fetch(LIB_INDEX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (d) { libIndexCache = d; return d; });
}

var _libSearchCache = null;
// _loadLibSearch: fetches data/library/search-index.json — passage-level full-text
// for every library document, used by the omni-search explore tab.
export function _loadLibSearch() {
  if (_libSearchCache) return Promise.resolve(_libSearchCache);
  return fetch(LIB_SEARCH_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (d) { _libSearchCache = d; return d; });
}

// ── escHtml (shared utility) ──────────────────────────────────────────────
// Escapes a string for safe insertion into HTML innerHTML.
// Use this whenever displaying user-supplied or data-derived text in HTML context.
export function escHtml(s) {
  if (s == null) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// ── _setOGMeta ────────────────────────────────────────────────────────────
// Updates Open Graph and description meta tags for pages that render content
// dynamically (reader, verse-study). Helps share links include useful previews.
export function _setOGMeta(title, desc, url) {
  function _set(sel, attr, val) {
    var el = document.querySelector(sel);
    if (el) el.setAttribute(attr, val);
  }
  _set('meta[property="og:title"]',       'content', title);
  _set('meta[property="og:description"]', 'content', desc);
  _set('meta[property="og:url"]',         'content', url || window.location.href);
  _set('meta[name="description"]',        'content', desc);
}
