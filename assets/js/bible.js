/* bible.js — Internal verse lookup, tooltip, and modal
 * Exposes window.BibleUI = { init, getVersion, setVersion, openModal }
 *
 * GitHub Pages compatible: paths are resolved relative to this script's own
 * URL so the site works at any subdirectory depth with zero configuration.
 */
(function () {
  'use strict';

  // ── Path auto-detection ───────────────────────────────────────────────────
  // document.currentScript is set during synchronous execution of a classic
  // <script> tag. Capture it before any async code runs.
  var _src = (document.currentScript && document.currentScript.src) || '';

  function _resolve(rel) {
    return _src ? new URL(rel, _src).href : rel;
  }

  var DATA_ROOT        = _resolve('../../data/bible');
  var CROSSREFS_ROOT   = _resolve('../../data/crossrefs');
  var COMMENTARY_ROOT  = _resolve('../../data/commentary');
  var PARALLELS_ROOT   = _resolve('../../data/parallels');
  var VERSIONS_URL     = _resolve('../../data/versions/versions.json');
  var BOOKS_URL        = _resolve('../../data/bible/books.json');
  var SEARCH_URL       = _resolve('../../search/');
  var READER_URL       = _resolve('../../read/');
  var VERSE_STUDY_URL  = _resolve('../../verse-study/');
  var COMPARE_URL      = _resolve('../../compare/');
  var WORD_URL         = _resolve('../../word/');
  var STORAGE_KEY      = 'bsw_version';
  var DEFAULT_VER      = 'BSB';
  var COMPARE_KEY      = 'bsw_compare'; // secondary version ID, '' = disabled
  var NOTES_KEY        = 'bsw_notes';      // personal notes & highlights
  var NOTES_URL        = _resolve('../../notes/');
  var BOOKMARKS_KEY    = 'bsw_bookmarks';  // bookmarked verse ref strings
  var BOOKMARKS_URL    = _resolve('../../bookmarks/');
  var STRONGS_ROOT     = _resolve('../../data/strongs');
  var TOPICS_ROOT      = _resolve('../../topics/');
  var SW_URL           = _resolve('../../sw.js');
  var MANIFEST_URL     = _resolve('../../manifest.json');
  var SITE_ROOT        = _resolve('../../');
  var INTERLINEAR_ROOT = _resolve('../../data/interlinear');
  var LIB_DOCS_BASE    = _resolve('../../data/library/docs');
  var LIB_INDEX_URL    = _resolve('../../data/library/index.json');

  // Library abbreviation → doc slug (must match data/library/docs/{slug}.json)
  var LIB_ABBREV_MAP = {
    // Confessions & creeds
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
    // Church Fathers
    'ign':  'ignatius',
    'jm':   'justin-martyr',
    'iren': 'irenaeus',
    'tert': 'tertullian',
    'atha': 'athanasius',
    'chrys':'chrysostom',
    'aug':  'augustine',
    'gnaz': 'gregory-nazianzus'
  };

  // ── In-memory caches ──────────────────────────────────────────────────────
  // key "{VERSION}:{bookId}" → chapters object {"1":{"1":"text",...},...}
  var bookCache     = Object.create(null);
  // key "{bookId}" → cross-ref object {"ch":{"v":["ref",...]},...} or null
  var crossRefCache = Object.create(null);
  // key "{bookId}" → commentary object {"ch":{"startV":"html",...},...} or null
  var commentaryCache = Object.create(null);
  // key "{bookId}" → parallel passage data {"ch":{"v":[{...}]}} or null
  var parallelsCache  = Object.create(null);
  // 'greek'|'hebrew' → Strong's dict object  /  bookId → interlinear data or null
  var strongsCache     = Object.create(null);
  var interlinearCache = Object.create(null);
  var libDocCache      = Object.create(null);  // docId → doc JSON
  var libIndexCache    = null;                  // Array from data/library/index.json
  var metaVersions = null;   // Array of version objects from versions.json
  var metaBooks    = null;   // Array of book objects from books.json
  var bookLookup   = null;   // Map: normalized string → bookId
  var bookOrder    = null;   // Map: bookId → canonical index (0-based)

  // ── Public API ────────────────────────────────────────────────────────────
  window.BibleUI = {
    init: init,
    getVersion: getVersion,
    setVersion: setVersion,
    openModal: openModal,
    openReader: function (bookId, ch, v) {
      var bkData = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
      var bkName = bkData ? bkData.name : bookId;
      var ref = bkName + ' ' + (ch || 1) + (v ? ':' + v : '');
      window.location.href = READER_URL + '?ref=' + encodeURIComponent(ref);
    }
  };

  // ── Version helpers ───────────────────────────────────────────────────────
  function getVersion() {
    return localStorage.getItem(STORAGE_KEY) || DEFAULT_VER;
  }

  function setVersion(id) {
    localStorage.setItem(STORAGE_KEY, id);
    var picker = document.getElementById('bible-version');
    if (picker) picker.value = id;
    // If modal is open, re-render with new version
    if (_modalEl && _backdropEl && !_backdropEl.classList.contains('bsw-modal-backdrop--hidden')) {
      var ref = _modalEl._parsedRef;
      if (ref) renderModal(ref, id);
    }
    updateInlineVerses(id);
    // Re-run search if on the search page
    var searchInput = document.getElementById('bsw-search-input');
    if (searchInput && searchInput.value.trim().length >= 4) {
      handleSearchInput(searchInput.value.trim());
    }
    // Re-run reader lookup if on the reader page
    if (_readerLookupFn && document.getElementById('reader-results')) {
      _readerLookupFn();
    }
    // Re-render verse study focal verse if on the verse study page
    if (_verseStudyUpdateFn) _verseStudyUpdateFn(id);
    // Re-render word deep dive occurrences if on the word page
    if (_wdRerenderFn) _wdRerenderFn(id);
  }

  // ── Notes & highlights helpers ────────────────────────────────────────────
  function getNotes() {
    try { return JSON.parse(localStorage.getItem(NOTES_KEY) || '{}'); }
    catch (e) { return {}; }
  }
  function getNote(refStr) {
    return getNotes()[refStr] || null;
  }
  function saveNote(refStr, data) {
    var all = getNotes();
    if (data === null || (data && !data.highlight && !data.note)) {
      delete all[refStr];
    } else {
      all[refStr] = data;
    }
    localStorage.setItem(NOTES_KEY, JSON.stringify(all));
  }
  function toggleHighlight(refStr) {
    var n = getNote(refStr) || {};
    n.highlight = !n.highlight;
    saveNote(refStr, n);
    return n.highlight;
  }

  // ── Notes v2 — verse-range-aware, timestamped ─────────────────────────────
  var NOTES_V2_KEY = 'bsw_notes_v2';
  var _notesV2Counter = 0;

  function _getNotesV2() {
    try { return JSON.parse(localStorage.getItem(NOTES_V2_KEY) || '[]'); }
    catch (e) { return []; }
  }
  function _saveNotesV2(arr) { localStorage.setItem(NOTES_V2_KEY, JSON.stringify(arr)); }

  function _migrateOldNotes() {
    if (localStorage.getItem(NOTES_V2_KEY + '_migrated')) return;
    var old = getNotes();
    var migrated = _getNotesV2();
    var now = Date.now();
    Object.keys(old).forEach(function (refStr) {
      var d = old[refStr];
      if (!d || !d.note) return;
      var p = parseRef(refStr);
      if (!p) return;
      migrated.push({ id: 'n_' + now + '_' + (_notesV2Counter++), bookId: p.bookId,
        ch: +p.ch, v: +p.v, endCh: null, endV: null,
        display: p.display || refStr, text: d.note, created: now, updated: now });
    });
    _saveNotesV2(migrated);
    localStorage.setItem(NOTES_V2_KEY + '_migrated', '1');
  }

  function createNoteV2(parsed, text) {
    var arr = _getNotesV2();
    var note = { id: 'n_' + Date.now() + '_' + (_notesV2Counter++),
      bookId: parsed.bookId, ch: +parsed.ch, v: +parsed.v,
      endCh: parsed.endCh ? +parsed.endCh : null, endV: parsed.endV ? +parsed.endV : null,
      display: parsed.display || (parsed.bookName + ' ' + parsed.ch + ':' + parsed.v),
      text: text, created: Date.now(), updated: Date.now() };
    arr.push(note);
    _saveNotesV2(arr);
    return note;
  }
  function updateNoteV2(id, text) {
    var arr = _getNotesV2();
    arr.forEach(function (n) { if (n.id === id) { n.text = text; n.updated = Date.now(); } });
    _saveNotesV2(arr);
  }
  function deleteNoteV2(id) { _saveNotesV2(_getNotesV2().filter(function (n) { return n.id !== id; })); }
  function getNotesForVerse(bookId, ch, v) {
    return _getNotesV2().filter(function (note) {
      if (note.bookId !== bookId) return false;
      if (!note.endCh && !note.endV) return note.ch === +ch && note.v === +v;
      var pos = +ch * 1000 + +v, start = note.ch * 1000 + note.v,
          end = (note.endCh || note.ch) * 1000 + (note.endV || note.v);
      return pos >= start && pos <= end;
    });
  }
  function hasNotesForVerse(bookId, ch, v) { return getNotesForVerse(bookId, ch, v).length > 0; }
  function _noteRelTime(ts) {
    var d = Date.now() - ts;
    if (d < 60000)     return 'just now';
    if (d < 3600000)   return Math.floor(d / 60000)    + 'm ago';
    if (d < 86400000)  return Math.floor(d / 3600000)  + 'h ago';
    if (d < 604800000) return Math.floor(d / 86400000) + 'd ago';
    return new Date(ts).toLocaleDateString();
  }

  // ── Bookmark helpers ──────────────────────────────────────────────────────
  function getBookmarks() {
    try { return JSON.parse(localStorage.getItem(BOOKMARKS_KEY) || '[]'); }
    catch (e) { return []; }
  }
  function isBookmarked(refStr) {
    return getBookmarks().indexOf(refStr) !== -1;
  }
  function toggleBookmark(refStr) {
    var list = getBookmarks();
    var idx  = list.indexOf(refStr);
    if (idx === -1) {
      list.unshift(refStr); // newest first
    } else {
      list.splice(idx, 1);
    }
    localStorage.setItem(BOOKMARKS_KEY, JSON.stringify(list));
    return idx === -1; // true = now bookmarked
  }

  // ── PWA: manifest + service worker ───────────────────────────────────────
  function initPWA() {
    // Inject <link rel="manifest"> if not already in the page
    if (!document.querySelector('link[rel="manifest"]')) {
      var link = document.createElement('link');
      link.rel = 'manifest';
      link.href = MANIFEST_URL;
      document.head.appendChild(link);
    }
    // Inject theme-color meta if not already present
    if (!document.querySelector('meta[name="theme-color"]')) {
      var meta = document.createElement('meta');
      meta.name = 'theme-color';
      meta.content = '#5c3d1e';
      document.head.appendChild(meta);
    }

    if (!('serviceWorker' in navigator)) return;

    navigator.serviceWorker.register(SW_URL).then(function (reg) {
      // When the SW becomes active, send the background pre-cache request
      function triggerPrecache(sw) {
        if (!sw || !metaBooks || !metaVersions) return;
        sw.postMessage({
          type: 'PRECACHE_BIBLE',
          base: SITE_ROOT,
          books: metaBooks.map(function (b) { return b.id; }),
          versions: metaVersions.map(function (v) { return v.id; }),
        });
      }

      // SW may already be active (returning visit) or still installing
      if (reg.active) {
        triggerPrecache(reg.active);
      } else {
        navigator.serviceWorker.ready.then(function (r) { triggerPrecache(r.active); });
      }

      // When a new SW is waiting, auto-update on next navigation
      reg.addEventListener('updatefound', function () {
        var incoming = reg.installing;
        incoming.addEventListener('statechange', function () {
          if (incoming.state === 'installed' && navigator.serviceWorker.controller) {
            incoming.postMessage({ type: 'SKIP_WAITING' });
          }
        });
      });
    }).catch(function (err) {
      console.warn('[BibleUI] SW registration failed:', err);
    });
  }

  // ── Init ──────────────────────────────────────────────────────────────────
  function init() {
    initPWA();
    _migrateOldNotes();
    Promise.all([loadVersions(), loadBooks()]).then(function () {
      populateVersionPicker();
      buildTooltipDOM();
      buildModalDOM();
      wireRefLinks();
      wireVersionPicker();
      buildSearchDOM();
      if (document.getElementById('reader-results')) {
        initReaderPage();
        initParallelToggle();
        initCompareToggle();
        initInterlinearToggle();
        initBookInfoToggle();
        initSidebarToggle();
        initWideToggle();
        initSplitToggle();
      }
      if (document.getElementById('vs-sections-container')) {
        initVerseStudyPage();
      }
      if (document.getElementById('wd-header')) {
        initWordPage();
      }
      autoTagRefs();
      wireInlineVerses();
      if (document.getElementById('daily-plan-select')) {
        initDailyPage();
      } else if (document.getElementById('home-plans-widget')) {
        initPlansHomeWidget();
      }
      if (document.getElementById('mem-list')) {
        initMemorizePage();
      }
      if (document.getElementById('topical-list')) {
        initTopicalPage();
      }
      if (document.getElementById('dict-list')) {
        initDictionaryPage();
      }
      // Defer term-map load and auto-tagging until browser is idle
      var _runTag = function () { runAutoTagTerms(); };
      if (typeof requestIdleCallback !== 'undefined') {
        requestIdleCallback(_runTag, { timeout: 3000 });
      } else {
        setTimeout(_runTag, 1200);
      }
    }).catch(function (err) {
      console.error('[BibleUI] init failed:', err);
    });
  }

  // ── Metadata loaders ──────────────────────────────────────────────────────
  function loadVersions() {
    if (metaVersions) return Promise.resolve(metaVersions);
    return fetch(VERSIONS_URL, { cache: 'no-cache' })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        metaVersions = data;
        return data;
      })
      .catch(function () {
        metaVersions = [{ id: 'KJV', name: 'King James Version', tier: 1 }];
        return metaVersions;
      });
  }

  function loadBooks() {
    if (metaBooks) return Promise.resolve(metaBooks);
    return fetch(BOOKS_URL)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        metaBooks = data;
        bookLookup = Object.create(null);
        bookOrder  = Object.create(null);
        data.forEach(function (book, idx) {
          // canonical name (lower, no spaces)
          bookLookup[book.name.toLowerCase()] = book.id;
          bookLookup[book.name.toLowerCase().replace(/\s+/g, '')] = book.id;
          // self-reference by id
          bookLookup[book.id] = book.id;
          // each abbreviation (case-insensitive)
          book.abbrevs.forEach(function (a) {
            bookLookup[a.toLowerCase()] = book.id;
          });
          // canonical position for sorting cross-refs
          bookOrder[book.id] = idx;
        });
        return data;
      })
      .catch(function () {
        metaBooks = [];
        bookLookup = Object.create(null);
        return [];
      });
  }

  // ── Version picker ────────────────────────────────────────────────────────
  function populateVersionPicker() {
    var picker = document.getElementById('bible-version');
    if (!picker || !metaVersions) return;
    var current = getVersion();
    picker.innerHTML = '';
    metaVersions.forEach(function (v) {
      var opt = document.createElement('option');
      opt.value = v.id;
      opt.textContent = v.id;
      opt.title = v.name;
      picker.appendChild(opt);
    });
    picker.value = current;
    if (!picker.value) picker.selectedIndex = 0;
  }

  function wireVersionPicker() {
    var picker = document.getElementById('bible-version');
    if (!picker) return;
    picker.addEventListener('change', function () {
      setVersion(picker.value);
    });
  }

  // ── Reference parser ──────────────────────────────────────────────────────
  function normalizeBook(raw) {
    if (!bookLookup) return null;
    var s = raw.trim().toLowerCase();
    return bookLookup[s] || bookLookup[s.replace(/\s+/g, '')] || null;
  }

  function parseRef(str) {
    if (!str) return null;
    // Normalize typographic dashes so "John 3:16–21" and "Gen 1:1—2:3" parse
    // identically to hyphen-separated forms.
    str = str.trim().replace(/[–—]/g, '-');
    // Pattern: [digit(s) ] word(s)  ch : v  [-  [endCh:] endV]
    // Handles: "John 3:16", "1 Cor 13:4-7", "Gen 1:1-2:3", "Revelation 1:1-3"
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

    // Artifact in source data: cross-chapter ranges stored without the end-chapter
    // (e.g. "Gen 29:31-21" instead of "Gen 29:31-30:21"). Infer next chapter.
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

  // Parses a library document reference such as "WCF 4", "WSC 1", "HC 26".
  // Returns { docId, abbrev, section } or null.
  function parseLibraryRef(str) {
    if (!str) return null;
    var m = str.trim().match(/^([A-Za-z0-9]+)\s+(\d+)$/);
    if (!m) return null;
    var key   = m[1].toLowerCase();
    var docId = LIB_ABBREV_MAP[key];
    if (!docId) return null;
    return { docId: docId, abbrev: m[1].toUpperCase(), section: m[2] };
  }

  // Parses a comma-separated multi-reference string into an array of ref objects.
  // Each segment may be a full ref (Gen 1:1), a ch:v ref (2:10-12), or a bare
  // verse/range (3-5) that inherits the current book and chapter context.
  // defaultBookId seeds the initial book context (e.g. the current reader book).
  //
  //   "Gen 1:1, 3-5, 2:10-12, Num 1:1-5"
  //   → Genesis 1:1 | Genesis 1:3–5 | Genesis 2:10–12 | Numbers 1:1–5
  function parseMultiRef(str, defaultBookId) {
    if (!str || !metaBooks) return [];
    str = str.trim().replace(/[–—]/g, '-');

    var FULL_RE    = /^((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+)*)\s+(\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$/;
    var FULL_CH_RE = /^((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+)*)\s+(\d+)$/; // book + chapter only
    var CH_RE      = /^(\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$/;
    var BARE_RE    = /^(\d+)(?:-(?:(\d+):)?(\d+))?$/;

    var curBookId   = defaultBookId || null;
    var curBookName = null;
    var curCh       = null;

    if (curBookId) {
      var db = metaBooks.find(function (b) { return b.id === curBookId; });
      if (db) curBookName = db.name;
    }

    var results = [];
    // Accept both comma and semicolon as segment separators
    var segments = str.split(/[,;]/);

    for (var i = 0; i < segments.length; i++) {
      // Collapse stray whitespace around : and - so "2 :1-5" → "2:1-5"
      var seg = segments[i].trim().replace(/\s*:\s*/g, ':').replace(/\s*-\s*/g, '-');
      if (!seg) continue;
      var m, bk, ch, v, endCh, endV, disp;

      if ((m = seg.match(FULL_RE))) {
        var bid = normalizeBook(m[1]);
        if (!bid) continue;
        bk    = metaBooks.find(function (b) { return b.id === bid; });
        ch    = parseInt(m[2], 10);
        v     = parseInt(m[3], 10);
        endCh = m[4] ? parseInt(m[4], 10) : ch;
        endV  = m[5] ? parseInt(m[5], 10) : v;
        disp  = (bk ? bk.name : m[1]) + ' ' + ch + ':' + v;
        if (m[5]) disp += '–' + (m[4] ? m[4] + ':' : '') + m[5];
        curBookId   = bid;
        curBookName = bk ? bk.name : m[1];
        curCh       = ch;
        results.push({ bookId: curBookId, bookName: curBookName,
                       ch: ch, v: v, endCh: endCh, endV: endV, display: disp });

      } else if ((m = seg.match(FULL_CH_RE))) {
        // Whole chapter: "Gen 1" or "Revelation 22"
        var bid = normalizeBook(m[1]);
        if (!bid) continue;
        bk    = metaBooks.find(function (b) { return b.id === bid; });
        ch    = parseInt(m[2], 10);
        disp  = (bk ? bk.name : m[1]) + ' ' + ch;
        curBookId   = bid;
        curBookName = bk ? bk.name : m[1];
        curCh       = ch;
        results.push({ bookId: curBookId, bookName: curBookName,
                       ch: ch, v: 1, endCh: ch, endV: 9999, display: disp, wholeChapter: true });

      } else if ((m = seg.match(CH_RE))) {
        if (!curBookId) continue;
        ch    = parseInt(m[1], 10);
        v     = parseInt(m[2], 10);
        endCh = m[3] ? parseInt(m[3], 10) : ch;
        endV  = m[4] ? parseInt(m[4], 10) : v;
        disp  = curBookName + ' ' + ch + ':' + v;
        if (m[4]) disp += '–' + (m[3] ? m[3] + ':' : '') + m[4];
        curCh = ch;
        results.push({ bookId: curBookId, bookName: curBookName,
                       ch: ch, v: v, endCh: endCh, endV: endV, display: disp });

      } else if ((m = seg.match(BARE_RE))) {
        if (!curBookId || curCh === null) continue;
        v     = parseInt(m[1], 10);
        endCh = m[2] ? parseInt(m[2], 10) : curCh;
        endV  = m[3] ? parseInt(m[3], 10) : v;
        disp  = curBookName + ' ' + curCh + ':' + v;
        if (m[3]) disp += '–' + (m[2] ? m[2] + ':' : '') + m[3];
        results.push({ bookId: curBookId, bookName: curBookName,
                       ch: curCh, v: v, endCh: endCh, endV: endV, display: disp });
      }
    }
    return results;
  }

  // ── Book data loader ──────────────────────────────────────────────────────
  function loadBook(versionId, bookId) {
    var key = versionId + ':' + bookId;
    if (key in bookCache) {
      return bookCache[key]
        ? Promise.resolve(bookCache[key])
        : Promise.reject(new Error('cached miss'));
    }
    var url = DATA_ROOT + '/' + versionId + '/' + bookId + '.json';
    return fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) {
        bookCache[key] = data.chapters || null;
        return bookCache[key];
      })
      .catch(function (err) {
        bookCache[key] = null;
        throw err;
      });
  }

  // ── Cross-reference loader ────────────────────────────────────────────────
  function loadCrossRefs(bookId) {
    if (bookId in crossRefCache) {
      return Promise.resolve(crossRefCache[bookId]);
    }
    var url = CROSSREFS_ROOT + '/' + bookId + '.json';
    return fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) {
        crossRefCache[bookId] = (data && Object.keys(data).length) ? data : null;
        return crossRefCache[bookId];
      })
      .catch(function () {
        crossRefCache[bookId] = null;
        return null;
      });
  }

  // Commentary source definitions
  var COMMENTARY_SOURCES = [
    { id: 'mhcc',   label: 'Matthew Henry Concise',    attr: 'Matthew Henry\'s Concise Commentary (Public Domain)' },
    { id: 'jfb',    label: 'Jamieson-Fausset-Brown',   attr: 'Jamieson-Fausset-Brown Bible Commentary (Public Domain)' },
    { id: 'clarke', label: "Adam Clarke's Commentary", attr: "Adam Clarke's Commentary on the Bible (Public Domain)" },
    { id: 'calvin', label: "Calvin's Commentaries",    attr: "Calvin's Collected Commentaries (Public Domain)" },
    { id: 'barnes', label: "Barnes' Notes (NT)",       attr: "Barnes' Notes on the Bible (Public Domain)" },
  ];
  var _commentarySource = localStorage.getItem('bsw_comm_src') || 'mhcc';

  function _commAttr(source) {
    var s = COMMENTARY_SOURCES.find(function (x) { return x.id === source; });
    return s ? s.attr : source;
  }

  function loadCommentary(bookId, source) {
    source = source || _commentarySource;
    // mhcc lives at the legacy flat path; other sources use data/commentary/{source}/
    var url = source === 'mhcc'
      ? COMMENTARY_ROOT + '/' + bookId + '.json'
      : COMMENTARY_ROOT + '/' + source + '/' + bookId + '.json';
    var key = source + ':' + bookId;
    if (key in commentaryCache) return Promise.resolve(commentaryCache[key]);
    return fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) {
        commentaryCache[key] = (data && Object.keys(data).length) ? data : null;
        return commentaryCache[key];
      })
      .catch(function () {
        commentaryCache[key] = null;
        return null;
      });
  }

  // ── Cross-reference utilities ─────────────────────────────────────────────

  // Parse one entry from a cross-ref array. Handles three formats:
  //   old format  → plain string "Genesis 1:1"
  //   new format  → 2-element array ["Genesis 1:1", votes]
  //   object form → {r: "Genesis 1:1", v: votes}
  function parseCrossRefEntry(entry) {
    if (typeof entry === 'string') return { ref: entry, votes: 1 };
    if (Array.isArray(entry))     return { ref: entry[0] || '', votes: entry[1] || 1 };
    if (entry && typeof entry === 'object') return { ref: entry.r || '', votes: entry.v || 1 };
    return { ref: String(entry), votes: 1 };
  }

  // Relevance score 0–100 based on community vote count.
  // At 25 votes a ref is considered highly confirmed (100%).
  function crossRefScore(entry) {
    return Math.min(100, Math.round(((entry.votes || 1) / 25) * 100));
  }

  // Compute Jaccard word-overlap similarity between two verse texts (0–100).
  // Ignores stop words and tokens shorter than 3 characters.
  // Use this when you have both the source verse text and a loaded cross-ref
  // verse text and want a content-based relevance signal.
  function computeTextSimilarity(textA, textB) {
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

  // Canonical sort key for a ref string: [bookIndex, chapter, verse].
  // Unknown refs sort to the end.
  function _canonicalKey(refStr) {
    var p = parseRef(refStr);
    if (!p) return [999, 0, 0];
    var idx = (bookOrder && p.bookId in bookOrder) ? bookOrder[p.bookId] : 999;
    return [idx, p.ch, p.v];
  }

  // Comparator for cross-ref entry objects: sorts by canonical Bible order.
  function _compareCanonical(a, b) {
    var ka = _canonicalKey(a.ref), kb = _canonicalKey(b.ref);
    return ka[0] - kb[0] || ka[1] - kb[1] || ka[2] - kb[2];
  }

  function resolveVerses(parsedRef, versionId) {
    var bookId = parsedRef.bookId;
    var ch = parsedRef.ch, v = parsedRef.v;
    var endCh = parsedRef.endCh, endV = parsedRef.endV;
    var bookName = parsedRef.bookName;

    return loadBook(versionId, bookId).then(function (chapters) {
      if (!chapters) return null;
      var results = [];

      for (var c = ch; c <= endCh; c++) {
        var chData = chapters[String(c)];
        if (!chData) continue;
        var startV = (c === ch) ? v : 1;
        var stopV  = (c === endCh) ? endV : 9999;

        Object.keys(chData)
          .map(Number)
          .filter(function (n) { return n >= startV && n <= stopV; })
          .sort(function (a, b) { return a - b; })
          .forEach(function (vNum) {
            results.push({
              ref: bookName + ' ' + c + ':' + vNum,
              chapter: c,
              verse: vNum,
              text: chData[String(vNum)]
            });
          });

        // Attach the real last verse of the chapter so nav can clamp ranges.
        if (c === endCh && ch === endCh) {
          results.chapterMaxV = Math.max.apply(null, Object.keys(chData).map(Number));
        }
      }
      return results.length ? results : null;
    });
  }

  // ── Tooltip ───────────────────────────────────────────────────────────────
  var _tooltipEl   = null;
  var _showTimer   = null;
  var _hideTimer   = null;

  function buildTooltipDOM() {
    if (document.getElementById('bsw-tooltip')) {
      _tooltipEl = document.getElementById('bsw-tooltip');
      return;
    }
    var el = document.createElement('div');
    el.id = 'bsw-tooltip';
    el.className = 'bsw-tooltip';
    el.setAttribute('role', 'tooltip');
    el.setAttribute('aria-hidden', 'true');
    el.innerHTML =
      '<div class="bsw-tooltip__ref"></div>' +
      '<div class="bsw-tooltip__text"></div>';
    document.body.appendChild(el);
    _tooltipEl = el;

    el.addEventListener('mouseenter', function () { cancelHide(); });
    el.addEventListener('mouseleave', function () { scheduleHide(); });
  }

  function scheduleShow(anchorEl, parsed) {
    cancelHide();
    cancelShow();
    _showTimer = setTimeout(function () { showTooltip(anchorEl, parsed); }, 300);
  }

  function cancelShow() {
    if (_showTimer) { clearTimeout(_showTimer); _showTimer = null; }
  }

  function scheduleHide() {
    cancelShow();
    _hideTimer = setTimeout(function () { hideTooltip(); }, 200);
  }

  function cancelHide() {
    if (_hideTimer) { clearTimeout(_hideTimer); _hideTimer = null; }
  }

  function showTooltip(anchorEl, parsed) {
    if (!_tooltipEl) return;
    var version = getVersion();

    _tooltipEl.querySelector('.bsw-tooltip__ref').textContent =
      parsed.display + ' · ' + version;
    _tooltipEl.querySelector('.bsw-tooltip__text').textContent = 'Loading…';
    _tooltipEl.classList.add('bsw-tooltip--visible');
    _tooltipEl.setAttribute('aria-hidden', 'false');
    // Chapter refs need a wider tooltip to show the opening verses preview.
    _tooltipEl.classList.toggle('bsw-tooltip--chapter', !!parsed.wholeChapter);
    positionTooltip(anchorEl);

    resolveVerses(parsed, version)
      .then(function (verses) {
        if (!_tooltipEl.classList.contains('bsw-tooltip--visible')) return;
        if (!verses || !verses.length) {
          _tooltipEl.querySelector('.bsw-tooltip__text').textContent = 'Verse not found.';
          return;
        }
        var preview;
        if (parsed.wholeChapter && parsed.endCh !== parsed.ch) {
          // Multi-chapter range (e.g. Ch. 1–3): show first verse of each chapter.
          var parts = [];
          for (var c = parsed.ch; c <= parsed.endCh; c++) {
            var cv = verses.filter(function (vr) { return vr.chapter === c; })[0];
            if (cv) parts.push('Ch.' + c + ': ' + cv.text);
          }
          preview = parts.join('  ');
          if (preview.length > 240) preview = preview.slice(0, 237) + '…';
        } else if (parsed.wholeChapter) {
          // Single chapter: show first 2 verses.
          preview = verses.slice(0, 2).map(function (vr) {
            return vr.verse + '. ' + vr.text;
          }).join('  ');
          if (preview.length > 220) preview = preview.slice(0, 217) + '…';
        } else {
          preview = verses[0].text;
          if (preview.length > 120) preview = preview.slice(0, 117) + '…';
        }
        _tooltipEl.querySelector('.bsw-tooltip__text').textContent = preview;
        positionTooltip(anchorEl);
      })
      .catch(function () {
        if (_tooltipEl.classList.contains('bsw-tooltip--visible')) {
          _tooltipEl.querySelector('.bsw-tooltip__text').textContent = 'Click to view this passage';
        }
      });
  }

  function hideTooltip() {
    if (!_tooltipEl) return;
    _tooltipEl.classList.remove('bsw-tooltip--visible');
    _tooltipEl.setAttribute('aria-hidden', 'true');
  }

  function positionTooltip(anchorEl) {
    if (!_tooltipEl) return;
    var rect  = anchorEl.getBoundingClientRect();
    var tt    = _tooltipEl.getBoundingClientRect();
    var gap   = 8;
    var top   = rect.bottom + gap;
    var left  = rect.left;

    if (top + tt.height > window.innerHeight - 16) {
      top = rect.top - tt.height - gap;
      _tooltipEl.classList.add('bsw-tooltip--above');
    } else {
      _tooltipEl.classList.remove('bsw-tooltip--above');
    }
    left = Math.max(16, Math.min(left, window.innerWidth - tt.width - 16));

    _tooltipEl.style.top  = top + 'px';
    _tooltipEl.style.left = left + 'px';
  }

  // ── Modal ─────────────────────────────────────────────────────────────────
  var _backdropEl  = null;
  var _modalEl     = null;
  var _lastFocused = null;

  // ── Word Deep Dive state ──────────────────────────────────────────────────
  var _wdRerenderFn = null; // set by initWordPage; called on version change

  // ── Verse Study state ─────────────────────────────────────────────────────
  var _verseStudyUpdateFn = null; // set by initVerseStudyPage; called on version change
  var _vsCurrentRef       = null; // parsed ref of the currently-displayed focal verse

  // ── Reader state ──────────────────────────────────────────────────────────
  var _readerLookupFn  = null; // set by initReaderLookup; called on version change
  var _readerNavState  = null; // { bookId, bookName, ch, maxCh[, verseStart, verseEnd, atChEnd] }
  var _readerGroups    = [];   // [{ref, el}] — tracks last-rendered groups for parallel injection

  // ── Search ────────────────────────────────────────────────────────────────
  var _searchDebounce   = null;
  var _searchGeneration = 0;

  var ATTRIBUTION = {
    'KJV': 'King James Version (1611) — Public Domain',
    'BSB': 'Berean Standard Bible — Copyright © 2022 by Bible Hub. Used by permission. All rights reserved worldwide.',
    'WEB': 'World English Bible — Public Domain',
    'ASV': 'American Standard Version (1901) — Public Domain'
  };

  function buildModalDOM() {
    if (document.getElementById('bsw-modal-backdrop')) {
      _backdropEl = document.getElementById('bsw-modal-backdrop');
      _modalEl    = document.getElementById('bsw-modal');
      return;
    }

    var backdrop = document.createElement('div');
    backdrop.id = 'bsw-modal-backdrop';
    backdrop.className = 'bsw-modal-backdrop bsw-modal-backdrop--hidden';
    backdrop.setAttribute('aria-hidden', 'true');

    var modal = document.createElement('div');
    modal.id = 'bsw-modal';
    modal.className = 'bsw-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-labelledby', 'bsw-modal-title');
    modal.innerHTML =
      '<div class="bsw-modal__header">' +
        '<h2 class="bsw-modal__title" id="bsw-modal-title"></h2>' +
        '<a class="bsw-modal__read-ch" href="#">Read chapter</a>' +
        '<a class="bsw-modal__verse-study-link" href="#" hidden>Verse Study ↗</a>' +
        '<a class="bsw-modal__compare-link" href="#" hidden>All translations ↗</a>' +
        '<button class="bsw-modal__memory-btn bsw-modal__compare-link" hidden aria-label="Add to memory">☆ Memorize</button>' +
        '<button class="bsw-modal__close" aria-label="Close verse viewer">✕</button>' +
      '</div>' +
      '<div class="bsw-modal__version-bar">' +
        '<label for="bsw-modal-version">Version:</label>' +
        '<select id="bsw-modal-version"></select>' +
      '</div>' +
      '<div class="bsw-modal__tabs" role="tablist">' +
        '<button class="bsw-modal__tab bsw-modal__tab--active" data-tab="verse" role="tab" aria-selected="true">Verse</button>' +
        '<button class="bsw-modal__tab" data-tab="notes" role="tab" aria-selected="false">Notes</button>' +
        '<button class="bsw-modal__tab" data-tab="commentary" role="tab" aria-selected="false">Commentary</button>' +
        '<button class="bsw-modal__tab" data-tab="wordstudy" role="tab" aria-selected="false">Word Study</button>' +
        '<button class="bsw-modal__tab" data-tab="topics" role="tab" aria-selected="false">Topics</button>' +
        '<button class="bsw-modal__tab" data-tab="confessions" role="tab" aria-selected="false">Confessions</button>' +
        '<button class="bsw-modal__tab" data-tab="dictionary" role="tab" aria-selected="false">Dictionary</button>' +
      '</div>' +
      // Verse panel (full-width; cross-refs injected as inline footnotes)
      '<div class="bsw-modal__split">' +
        '<div class="bsw-modal__verse-col">' +
          '<div class="bsw-modal__body" aria-live="polite"></div>' +
          '<div class="bsw-modal__attribution"></div>' +
        '</div>' +
      '</div>' +
      // Notes panel (hidden until tab click)
      '<div class="bsw-modal__notes-panel" hidden></div>' +
      // Commentary panel (hidden until tab click)
      '<div class="bsw-modal__commentary-panel" hidden></div>' +
      // Word Study panel (hidden until tab click)
      '<div class="bsw-modal__wordstudy-panel" hidden></div>' +
      // Topics panel (hidden until tab click)
      '<div class="bsw-modal__topics-panel" hidden></div>' +
      // Confessions panel (hidden until tab click)
      '<div class="bsw-modal__confessions-panel" hidden></div>' +
      // Dictionary panel (hidden until tab click)
      '<div class="bsw-modal__dictionary-panel" hidden></div>' +
      '';

    backdrop.appendChild(modal);
    document.body.appendChild(backdrop);

    _backdropEl = backdrop;
    _modalEl    = modal;

    modal.querySelector('.bsw-modal__close').addEventListener('click', hideModal);
    modal.querySelector('.bsw-modal__memory-btn').addEventListener('click', function () {
      var ref = this._memRef;
      if (!ref) return;
      if (_memHas(ref)) { _memRemove(ref); } else { _memAdd(ref); }
      _memRefreshModalBtn(ref);
    });
    backdrop.addEventListener('click', function (e) {
      if (e.target === backdrop) hideModal();
    });
    modal.querySelector('#bsw-modal-version').addEventListener('change', function () {
      var ref = _modalEl._parsedRef;
      if (ref) renderModal(ref, this.value);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' &&
          _backdropEl && !_backdropEl.classList.contains('bsw-modal-backdrop--hidden')) {
        hideModal();
      }
    });

    // Tab switching
    modal.querySelector('.bsw-modal__tabs').addEventListener('click', function (e) {
      var btn = e.target.closest('.bsw-modal__tab');
      if (!btn) return;
      var tab = btn.getAttribute('data-tab');
      modal.querySelectorAll('.bsw-modal__tab').forEach(function (b) {
        var active = b === btn;
        b.classList.toggle('bsw-modal__tab--active', active);
        b.setAttribute('aria-selected', active ? 'true' : 'false');
      });
      var splitEl   = modal.querySelector('.bsw-modal__split');
      var notesEl   = modal.querySelector('.bsw-modal__notes-panel');
      var commEl    = modal.querySelector('.bsw-modal__commentary-panel');
      var wsEl      = modal.querySelector('.bsw-modal__wordstudy-panel');
      var topicsEl  = modal.querySelector('.bsw-modal__topics-panel');
      var confEl    = modal.querySelector('.bsw-modal__confessions-panel');
      var dictEl    = modal.querySelector('.bsw-modal__dictionary-panel');
      var allPanels = [splitEl, notesEl, commEl, wsEl, topicsEl, confEl, dictEl];
      allPanels.forEach(function (p) { if (p) p.setAttribute('hidden', ''); });
      if (tab === 'verse') {
        if (splitEl) splitEl.removeAttribute('hidden');
      } else if (tab === 'notes') {
        if (notesEl) {
          notesEl.removeAttribute('hidden');
          _renderNotesPanel(_modalEl._parsedRef, notesEl);
        }
      } else if (tab === 'commentary') {
        if (commEl) {
          commEl.removeAttribute('hidden');
          if (!commEl._commentaryLoaded) renderCommentary(_modalEl._parsedRef, commEl);
        }
      } else if (tab === 'wordstudy') {
        if (wsEl) {
          wsEl.removeAttribute('hidden');
          if (!wsEl._wsLoaded) renderModalWordStudy(_modalEl._parsedRef, wsEl);
        }
      } else if (tab === 'topics') {
        if (topicsEl) {
          topicsEl.removeAttribute('hidden');
          if (!topicsEl._topicsLoaded) renderModalTopics(_modalEl._parsedRef, topicsEl);
        }
      } else if (tab === 'confessions') {
        if (confEl) {
          confEl.removeAttribute('hidden');
          if (!confEl._confLoaded) renderModalConfessions(_modalEl._parsedRef, confEl);
        }
      } else if (tab === 'dictionary') {
        if (dictEl) {
          dictEl.removeAttribute('hidden');
          if (!dictEl._dictLoaded) renderModalDictionary(_modalEl._parsedRef, dictEl);
        }
      }
    });
  }

  function syncModalVersionPicker() {
    var sel = document.getElementById('bsw-modal-version');
    if (!sel || !metaVersions) return;
    if (sel.options.length === metaVersions.length) return;
    var current = getVersion();
    sel.innerHTML = '';
    metaVersions.forEach(function (v) {
      var opt = document.createElement('option');
      opt.value = v.id;
      opt.textContent = v.id;
      opt.title = v.name;
      sel.appendChild(opt);
    });
    sel.value = current;
    if (!sel.value) sel.selectedIndex = 0;
  }

  function openModal(parsed) {
    if (!_modalEl || !_backdropEl) buildModalDOM();
    _lastFocused = document.activeElement;

    syncModalVersionPicker();

    _backdropEl.classList.remove('bsw-modal-backdrop--hidden');
    _backdropEl.setAttribute('aria-hidden', 'false');

    var versionSel = document.getElementById('bsw-modal-version');
    var version = (versionSel && versionSel.value) ? versionSel.value : getVersion();

    renderModal(parsed, version).then(function () {
      var closeBtn = _modalEl.querySelector('.bsw-modal__close');
      if (closeBtn) closeBtn.focus();
    });

    _modalEl.addEventListener('keydown', trapFocus);
    document.body.style.overflow = 'hidden';
  }

  function renderModal(parsed, versionId) {
    _modalEl._parsedRef = parsed;

    // Reset to Verse tab whenever a new ref is rendered
    var bodyEl  = _modalEl.querySelector('.bsw-modal__body');
    var attrElR = _modalEl.querySelector('.bsw-modal__attribution');
    _modalEl.querySelectorAll('.bsw-modal__tab').forEach(function (b) {
      var isVerse = b.getAttribute('data-tab') === 'verse';
      b.classList.toggle('bsw-modal__tab--active', isVerse);
      b.setAttribute('aria-selected', isVerse ? 'true' : 'false');
    });
    _refreshModalNotesBadge(parsed);
    var splitEl  = _modalEl.querySelector('.bsw-modal__split');
    var notesEl  = _modalEl.querySelector('.bsw-modal__notes-panel');
    var commEl   = _modalEl.querySelector('.bsw-modal__commentary-panel');
    var wsEl     = _modalEl.querySelector('.bsw-modal__wordstudy-panel');
    if (bodyEl)  bodyEl.removeAttribute('hidden');
    if (attrElR) attrElR.removeAttribute('hidden');
    if (splitEl) splitEl.removeAttribute('hidden');
    if (notesEl) { notesEl.setAttribute('hidden', ''); notesEl.innerHTML = ''; }
    if (commEl)  { commEl.setAttribute('hidden', '');  commEl._commentaryLoaded = false; }
    if (wsEl)    { wsEl.setAttribute('hidden', '');    wsEl._wsLoaded = false; }
    var topicsEl2 = _modalEl.querySelector('.bsw-modal__topics-panel');
    if (topicsEl2) { topicsEl2.setAttribute('hidden', ''); topicsEl2._topicsLoaded = false; }
    var confEl = _modalEl.querySelector('.bsw-modal__confessions-panel');
    if (confEl)  { confEl.setAttribute('hidden', '');  confEl._confLoaded = false; }
    var dictPanelEl = _modalEl.querySelector('.bsw-modal__dictionary-panel');
    if (dictPanelEl) { dictPanelEl.setAttribute('hidden', ''); dictPanelEl._dictLoaded = false; }

    var title  = _modalEl.querySelector('.bsw-modal__title');
    var body   = _modalEl.querySelector('.bsw-modal__body');
    var attr   = _modalEl.querySelector('.bsw-modal__attribution');
    var vSel   = document.getElementById('bsw-modal-version');

    title.textContent = parsed.display;
    if (vSel) vSel.value = versionId;
    body.innerHTML = '<div class="bsw-modal__loading">Loading…</div>';
    attr.textContent = '';

    var readCh = _modalEl.querySelector('.bsw-modal__read-ch');
    if (readCh) {
      if (parsed.wholeChapter && parsed.endCh !== parsed.ch) {
        // Multi-chapter: header link goes to the first chapter; individual
        // chapter links in the body handle the rest.
        readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch);
        readCh.textContent = 'Open in Reader ↗';
      } else if (parsed.wholeChapter) {
        readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch);
        readCh.textContent = 'Read chapter ↗';
      } else {
        readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch);
        readCh.textContent = 'Read chapter ↗';
      }
    }

    // Verse Study + All Translations links: only for single-verse refs
    var vsLink  = _modalEl.querySelector('.bsw-modal__verse-study-link');
    var cmpLink = _modalEl.querySelector('.bsw-modal__compare-link');
    var isSingleVerse = !parsed.wholeChapter && parsed.ch === parsed.endCh && parsed.v === parsed.endV;
    var singleRef = encodeURIComponent(parsed.bookName + ' ' + parsed.ch + ':' + parsed.v);
    if (vsLink) {
      if (isSingleVerse) {
        vsLink.href = VERSE_STUDY_URL + '?ref=' + singleRef;
        vsLink.removeAttribute('hidden');
      } else {
        vsLink.setAttribute('hidden', '');
      }
    }
    if (cmpLink) {
      if (isSingleVerse) {
        cmpLink.href = COMPARE_URL + '?ref=' + singleRef;
        cmpLink.removeAttribute('hidden');
      } else {
        cmpLink.setAttribute('hidden', '');
      }
    }
    var memBtn = _modalEl.querySelector('.bsw-modal__memory-btn');
    if (memBtn) {
      if (isSingleVerse) {
        var memRef = parsed.bookName + ' ' + parsed.ch + ':' + parsed.v;
        memBtn._memRef = memRef;
        memBtn.textContent = _memHas(memRef) ? '⭐ Memorizing' : '☆ Memorize';
        memBtn.classList.toggle('bsw-modal__memory-btn--active', _memHas(memRef));
        memBtn.removeAttribute('hidden');
      } else {
        memBtn.setAttribute('hidden', '');
      }
    }

    return resolveVerses(parsed, versionId)
      .then(function (verses) {
        if (!verses || !verses.length) {
          body.innerHTML = '<p class="bsw-modal__error">Verse not found in ' +
            escHtml(versionId) + '.</p>';
          return;
        }

        var html = '';
        if (parsed.wholeChapter && parsed.endCh !== parsed.ch) {
          // Multi-chapter range: one collapsible section per chapter showing
          // the first 2 verses, each with its own "Read Chapter N" link.
          for (var c = parsed.ch; c <= parsed.endCh; c++) {
            var chVerses = verses.filter(function (vr) { return vr.chapter === c; });
            var chRef2   = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + c);
            html += '<div class="bsw-modal__chapter-section">';
            html += '<div class="bsw-modal__chapter-label">' +
              escHtml(parsed.bookName) + ' ' + c +
              '<a class="bsw-modal__chapter-read" href="' + chRef2 + '">' +
              'Read chapter ↗</a></div>';
            chVerses.slice(0, 2).forEach(function (vr) {
              html += '<div class="bsw-modal__verse" data-ch="' + c + '" data-v="' + vr.verse + '">' +
                '<sup class="bsw-modal__verse-num">' + vr.verse + '</sup>' +
                '<span class="bsw-modal__verse-text">' + escHtml(vr.text) + '</span>' +
                '</div>';
            });
            html += '</div>';
          }
        } else if (parsed.wholeChapter) {
          // Single chapter: first 5 verses + "…and N more" footer.
          var PREVIEW_LIMIT = 5;
          var shown = verses.slice(0, PREVIEW_LIMIT);
          var remaining = verses.length - shown.length;
          html = shown.map(function (vr) {
            return '<div class="bsw-modal__verse" data-ch="' + parsed.ch + '" data-v="' + vr.verse + '">' +
              '<sup class="bsw-modal__verse-num">' + vr.verse + '</sup>' +
              '<span class="bsw-modal__verse-text">' + escHtml(vr.text) + '</span>' +
              '</div>';
          }).join('');
          if (remaining > 0) {
            var chRef = parsed.bookName + ' ' + parsed.ch;
            html +=
              '<div class="bsw-modal__chapter-more">' +
              '…and ' + remaining + ' more verse' + (remaining === 1 ? '' : 's') +
              ' — <a class="bsw-modal__chapter-more-link"' +
              ' href="' + READER_URL + '?ref=' + encodeURIComponent(chRef) + '">' +
              'Read full chapter in Reader ↗</a>' +
              '</div>';
          }
        } else {
          // Normal verse ref: show all verses.
          html = verses.map(function (vr) {
            return '<div class="bsw-modal__verse" data-ch="' + (vr.chapter || parsed.ch) + '" data-v="' + vr.verse + '">' +
              '<sup class="bsw-modal__verse-num">' + vr.verse + '</sup>' +
              '<span class="bsw-modal__verse-text">' + escHtml(vr.text) + '</span>' +
              '</div>';
          }).join('');
        }
        body.innerHTML = html;
        attr.textContent = ATTRIBUTION[versionId] || '';
        _injectModalFootnotes(parsed, body);
        // Tag proper nouns / theological terms in verse text
        if (_termMap2) { body._termsTagged = false; autoTagTerms(body); }
      })
      .catch(function () {
        body.innerHTML =
          '<p class="bsw-modal__error">Could not load ' + escHtml(versionId) + ' data.</p>';
      });
  }

  // ── Modal inline footnote injection ──────────────────────────────────────
  // Injects superscript footnote markers (1–5) after each verse's text span,
  // matching the reader behaviour, replacing the old right-column panel.
  function _injectModalFootnotes(parsed, bodyEl) {
    if (!parsed || !bodyEl) return;
    loadCrossRefs(parsed.bookId).then(function (data) {
      if (!data) return;
      var verseEls = bodyEl.querySelectorAll('.bsw-modal__verse[data-ch][data-v]');
      verseEls.forEach(function (verseEl) {
        var c    = +verseEl.getAttribute('data-ch');
        var v    = +verseEl.getAttribute('data-v');
        var chData = data[String(c)];
        if (!chData) return;
        var rawRefs = chData[String(v)];
        if (!rawRefs || !rawRefs.length) return;

        var entries = rawRefs.map(parseCrossRefEntry);
        entries.sort(function (a, b) { return b.votes - a.votes; });
        entries = entries.slice(0, XREF_CHAPTER_LIMIT);
        entries.sort(_compareCanonical);

        entries.forEach(function (entry, i) {
          var p = parseRef(entry.ref);
          if (!p) return;
          var sup = document.createElement('sup');
          sup.className = 'bsw-modal__xref-note';
          sup.setAttribute('data-ref', entry.ref);
          sup.setAttribute('aria-label', 'Cross-reference: ' + entry.ref);
          sup.setAttribute('tabindex', '0');
          sup.setAttribute('role', 'button');
          sup.textContent = String(i + 1);
          wireRefEl(sup, p);
          verseEl.appendChild(sup);
        });
      });
    }).catch(function () {});
  }

  // ── Cross-references panel renderer ──────────────────────────────────────
  // isSingle=true  → show ALL refs for the verse, sorted by canonical order.
  // isSingle=false → show only the top XREF_CHAPTER_LIMIT refs per verse
  //                  (ranked by community votes), then sorted canonically.
  var XREF_CHAPTER_LIMIT = 5;

  function renderCrossRefs(parsed, container) {
    if (!parsed) { container.innerHTML = '<p class="bsw-modal__xrefs-empty">No reference selected.</p>'; return; }
    container._xrefLoaded = true;
    container.innerHTML = '<p class="bsw-modal__loading">Loading cross-references…</p>';

    var isSingle = !parsed.wholeChapter && (parsed.ch === parsed.endCh) && (parsed.v === parsed.endV);

    loadCrossRefs(parsed.bookId).then(function (data) {
      if (!data) {
        container.innerHTML = '<p class="bsw-modal__xrefs-empty">No cross-references available for this book.</p>';
        return;
      }

      // Gather refs for the verse range
      var groups = [];
      for (var c = parsed.ch; c <= Math.min(parsed.endCh, parsed.ch + 4); c++) {
        var chData = data[String(c)];
        if (!chData) continue;
        var startV = (c === parsed.ch) ? parsed.v : 1;
        var stopV  = (c === parsed.endCh) ? Math.min(parsed.endV, 9999) : 9999;
        var keys   = Object.keys(chData).map(Number)
          .filter(function (n) { return n >= startV && n <= stopV; })
          .sort(function (a, b) { return a - b; });

        keys.forEach(function (vNum) {
          var rawRefs = chData[String(vNum)];
          if (!rawRefs || !rawRefs.length) return;

          // Parse entries — supports old string[], new [ref,votes][], and {r,v}[]
          var entries = rawRefs.map(parseCrossRefEntry);

          if (!isSingle) {
            // Chapter/range mode: rank by votes descending, keep top N
            entries.sort(function (a, b) { return b.votes - a.votes; });
            entries = entries.slice(0, XREF_CHAPTER_LIMIT);
          }

          // Always display sorted by canonical Bible order (book → ch → v)
          entries.sort(_compareCanonical);
          groups.push({ ch: c, v: vNum, entries: entries });
        });
      }

      if (!groups.length) {
        container.innerHTML = '<p class="bsw-modal__xrefs-empty">No cross-references found for this passage.</p>';
        return;
      }

      // Only show relevance tiers if at least one entry has real vote data (> 1)
      var hasScores = groups.some(function (g) {
        return g.entries.some(function (e) { return e.votes > 1; });
      });

      var html = '';
      groups.forEach(function (g) {
        if (!isSingle) {
          html += '<div class="bsw-modal__xref-verse-label">' +
            escHtml(parsed.bookName) + ' ' + g.ch + ':' + g.v + '</div>';
        }
        html += '<div class="bsw-modal__xref-list">';
        g.entries.forEach(function (entry) {
          var tierClass = '';
          if (hasScores) {
            tierClass = entry.votes >= 15 ? ' bsw-xref--high' :
                        entry.votes >= 6  ? ' bsw-xref--med'  : ' bsw-xref--low';
          }
          html += '<a class="bsw-modal__xref-link' + tierClass + '"' +
            ' data-ref="' + escHtml(entry.ref) + '"' +
            ' role="button" tabindex="0">' +
            escHtml(entry.ref) + '</a>';
        });
        html += '</div>';
      });

      container.innerHTML = html;

      // Wire each cross-ref link for hover tooltip + click-to-modal
      container.querySelectorAll('.bsw-modal__xref-link').forEach(function (el) {
        var p = parseRef(el.getAttribute('data-ref'));
        if (p) wireRefEl(el, p);
      });
    }).catch(function () {
      container.innerHTML = '<p class="bsw-modal__xrefs-empty">Could not load cross-reference data.</p>';
    });
  }

  function _buildCommPicker(currentSrc) {
    var opts = COMMENTARY_SOURCES.map(function (s) {
      return '<option value="' + s.id + '"' + (s.id === currentSrc ? ' selected' : '') + '>' + s.label + '</option>';
    }).join('');
    return '<div class="bsw-modal__comm-picker">' +
      '<label class="bsw-modal__comm-label">Source:</label>' +
      '<select class="bsw-modal__comm-select">' + opts + '</select>' +
      '</div>';
  }

  function _extractCommHtml(data, parsed, source) {
    if (!data) return null;
    var chData = data[String(parsed.ch)];
    if (!chData) return null;
    var sectionKeys = Object.keys(chData).map(Number).sort(function (a, b) { return a - b; });
    var html = '';
    var endV  = parsed.wholeChapter ? 9999 : parsed.endV;
    var startV = parsed.v;
    if (parsed.wholeChapter) {
      sectionKeys.forEach(function (v) {
        html += '<div class="bsw-modal__commentary-section">' + chData[String(v)] + '</div>';
      });
    } else {
      var foundV = null;
      for (var v = startV; v >= 1; v--) {
        if (chData[String(v)]) { foundV = v; break; }
      }
      if (foundV !== null) {
        html = '<div class="bsw-modal__commentary-section">' + chData[String(foundV)] + '</div>';
        sectionKeys.forEach(function (v) {
          if (v > startV && v <= endV && chData[String(v)]) {
            html += '<div class="bsw-modal__commentary-section">' + chData[String(v)] + '</div>';
          }
        });
      }
    }
    return html || null;
  }

  // ── Modal Notes-tab badge ────────────────────────────────────────────────
  function _refreshModalNotesBadge(parsed) {
    if (!_modalEl || !parsed) return;
    var noteBtn = _modalEl.querySelector('.bsw-modal__tab[data-tab="notes"]');
    if (!noteBtn) return;
    var count = getNotesForVerse(parsed.bookId, parsed.ch, parsed.v).length;
    var badge = noteBtn.querySelector('.bsw-modal__tab-badge');
    if (count > 0) {
      if (!badge) {
        badge = document.createElement('span');
        badge.className = 'bsw-modal__tab-badge';
        noteBtn.appendChild(badge);
      }
      badge.textContent = String(count);
    } else {
      if (badge) badge.remove();
    }
  }

  // ── Shared notes panel ───────────────────────────────────────────────────
  // Renders existing notes for `parsed` and a compose area into `container`.
  // Returns a `refresh()` function that rebuilds in place.
  function _renderNotesPanel(parsed, container) {
    if (!parsed) { container.innerHTML = '<p class="bsw-note-empty">No reference selected.</p>'; return function(){}; }

    function buildNoteItem(note) {
      var div = document.createElement('div');
      div.className = 'bsw-note-item';
      div.setAttribute('data-note-id', note.id);

      var body = document.createElement('div');
      body.className = 'bsw-note-body';
      body.textContent = note.text;
      div.appendChild(body);

      var meta = document.createElement('div');
      meta.className = 'bsw-note-meta';
      var rangeLabel = note.display !== parsed.display
        ? '<span class="bsw-note-range">' + escHtml(note.display) + '</span> · ' : '';
      meta.innerHTML = rangeLabel + '<span class="bsw-note-time">' + _noteRelTime(note.created) + '</span>';
      div.appendChild(meta);

      var actions = document.createElement('div');
      actions.className = 'bsw-note-actions';

      var editBtn = document.createElement('button');
      editBtn.className = 'bsw-note-action-btn';
      editBtn.textContent = 'Edit';
      var delBtn = document.createElement('button');
      delBtn.className = 'bsw-note-action-btn bsw-note-action-btn--del';
      delBtn.textContent = 'Delete';
      actions.appendChild(editBtn);
      actions.appendChild(delBtn);
      div.appendChild(actions);

      // Inline edit area
      var editArea = document.createElement('div');
      editArea.className = 'bsw-note-edit-area';
      editArea.hidden = true;
      var ta = document.createElement('textarea');
      ta.className = 'bsw-note-textarea';
      ta.value = note.text;
      var saveBtn = document.createElement('button');
      saveBtn.className = 'vs-context-btn';
      saveBtn.textContent = 'Save';
      var cancelBtn = document.createElement('button');
      cancelBtn.className = 'bsw-note-action-btn';
      cancelBtn.textContent = 'Cancel';
      var editBtnRow = document.createElement('div');
      editBtnRow.className = 'bsw-note-edit-btns';
      editBtnRow.appendChild(saveBtn);
      editBtnRow.appendChild(cancelBtn);
      editArea.appendChild(ta);
      editArea.appendChild(editBtnRow);
      div.appendChild(editArea);

      editBtn.addEventListener('click', function () {
        editArea.hidden = false;
        body.hidden = true;
        meta.hidden = true;
        actions.hidden = true;
        ta.focus();
      });
      cancelBtn.addEventListener('click', function () {
        editArea.hidden = true;
        body.hidden = false;
        meta.hidden = false;
        actions.hidden = false;
        ta.value = note.text;
      });
      saveBtn.addEventListener('click', function () {
        var t = ta.value.trim();
        if (!t) return;
        updateNoteV2(note.id, t);
        body.textContent = t;
        note.text = t;
        editArea.hidden = true;
        body.hidden = false;
        meta.hidden = false;
        actions.hidden = false;
      });
      delBtn.addEventListener('click', function () {
        deleteNoteV2(note.id);
        div.remove();
        _refreshModalNotesBadge(parsed);
      });

      return div;
    }

    function _innerRefresh() {
      container.innerHTML = '';
      var notes = getNotesForVerse(parsed.bookId, parsed.ch, parsed.v);

      if (notes.length) {
        var list = document.createElement('div');
        list.className = 'bsw-note-list';
        notes.forEach(function (n) { list.appendChild(buildNoteItem(n)); });
        container.appendChild(list);
      } else {
        var empty = document.createElement('p');
        empty.className = 'bsw-note-empty';
        empty.textContent = 'No notes yet for ' + (parsed.display || 'this verse') + '.';
        container.appendChild(empty);
      }

      // Compose area
      var compose = document.createElement('div');
      compose.className = 'bsw-note-compose';
      var cta = document.createElement('textarea');
      cta.className = 'bsw-note-textarea';
      cta.placeholder = 'Add a note for ' + (parsed.display || 'this verse') + '…';
      var footer = document.createElement('div');
      footer.className = 'bsw-note-compose-footer';
      var refTag = document.createElement('span');
      refTag.className = 'bsw-note-ref-tag';
      refTag.textContent = parsed.display || '';
      var addBtn = document.createElement('button');
      addBtn.className = 'vs-context-btn';
      addBtn.textContent = 'Save note';
      footer.appendChild(refTag);
      footer.appendChild(addBtn);
      compose.appendChild(cta);
      compose.appendChild(footer);
      container.appendChild(compose);

      addBtn.addEventListener('click', function () {
        var t = cta.value.trim();
        if (!t) return;
        createNoteV2(parsed, t);
        cta.value = '';
        refresh();
      });
    }

    function refresh() {
      _refreshModalNotesBadge(parsed);
      _innerRefresh();
    }

    refresh();
    return refresh;
  }

  function renderCommentary(parsed, container) {
    if (!parsed) {
      container.innerHTML = '<p class="bsw-modal__commentary-empty">No reference selected.</p>';
      return;
    }
    container._commentaryLoaded = true;

    function loadAndRender(src) {
      var bodyEl = container.querySelector('.bsw-modal__comm-body');
      if (bodyEl) bodyEl.innerHTML = '<p class="bsw-modal__loading">Loading commentary…</p>';

      loadCommentary(parsed.bookId, src).then(function (data) {
        var html = _extractCommHtml(data, parsed, src);
        var body = container.querySelector('.bsw-modal__comm-body');
        if (!body) return;
        if (!html) {
          body.innerHTML = '<p class="bsw-modal__commentary-empty">No commentary found for this verse.</p>';
          return;
        }
        body.innerHTML = html +
          '<p class="bsw-modal__commentary-attr">' + _commAttr(src) + '</p>';
        wireRefLinks(body);
      }).catch(function () {
        var body = container.querySelector('.bsw-modal__comm-body');
        if (body) body.innerHTML = '<p class="bsw-modal__commentary-empty">Could not load commentary.</p>';
      });
    }

    // Build picker + body skeleton
    container.innerHTML = _buildCommPicker(_commentarySource) +
      '<div class="bsw-modal__comm-body"><p class="bsw-modal__loading">Loading commentary…</p></div>';

    // Wire source picker
    var sel = container.querySelector('.bsw-modal__comm-select');
    sel.addEventListener('change', function () {
      _commentarySource = sel.value;
      localStorage.setItem('bsw_comm_src', _commentarySource);
      loadAndRender(_commentarySource);
    });

    loadAndRender(_commentarySource);
  }

  function hideModal() {
    if (!_backdropEl) return;
    _backdropEl.classList.add('bsw-modal-backdrop--hidden');
    _backdropEl.setAttribute('aria-hidden', 'true');
    if (_modalEl) _modalEl.removeEventListener('keydown', trapFocus);
    document.body.style.overflow = '';
    if (_lastFocused) { try { _lastFocused.focus(); } catch (e) {} _lastFocused = null; }
  }

  function trapFocus(e) {
    if (e.key !== 'Tab') return;
    var focusable = Array.prototype.slice.call(
      _modalEl.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      )
    ).filter(function (el) { return !el.disabled && el.offsetParent !== null; });
    if (!focusable.length) return;
    var first = focusable[0];
    var last  = focusable[focusable.length - 1];
    if (e.shiftKey) {
      if (document.activeElement === first) { e.preventDefault(); last.focus(); }
    } else {
      if (document.activeElement === last)  { e.preventDefault(); first.focus(); }
    }
  }

  // ── Search: inject nav button and wire search page ───────────────────────
  function buildSearchDOM() {
    // Inject "Search" button before the version picker in the header
    var vp = document.querySelector('.version-picker');
    if (vp && !document.getElementById('bsw-search-btn')) {
      var btn = document.createElement('button');
      btn.id = 'bsw-search-btn';
      btn.className = 'bsw-search-btn';
      btn.setAttribute('aria-label', 'Search verses (Ctrl+K)');
      btn.textContent = 'Search';
      vp.parentNode.insertBefore(btn, vp);
      btn.addEventListener('click', function () {
        var inp = document.getElementById('bsw-search-input');
        if (inp) { inp.focus(); inp.select(); } else { window.location.href = SEARCH_URL; }
      });
    }

    // Ctrl+K / Cmd+K — navigate to search page or focus input if already there
    document.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        var inp = document.getElementById('bsw-search-input');
        if (inp) { inp.focus(); inp.select(); } else { window.location.href = SEARCH_URL; }
      }
    });

    // If this is the search page, wire up the input
    var pageInput = document.getElementById('bsw-search-input');
    if (pageInput) initSearchPage(pageInput);
  }

  // Called only when on search/index.html
  function initSearchPage(input) {
    input.focus();

    var modeBtns    = document.querySelectorAll('.search-mode-btn');
    var currentMode = 'text';

    function setMode(mode) {
      currentMode = mode;
      modeBtns.forEach(function (btn) {
        btn.classList.toggle('search-mode-btn--active', btn.getAttribute('data-mode') === mode);
      });
      input.placeholder = mode === 'strongs'
        ? 'e.g. G3056, H430, G25'
        : 'e.g. love, in the beginning, “the word was God”';
    }

    modeBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        setMode(btn.getAttribute('data-mode'));
        var q = input.value.trim();
        if (q) dispatchSearch(q);
        input.focus();
      });
    });

    function dispatchSearch(query) {
      var isStrongsPattern = /^[GgHh]\d+$/.test(query.replace(/\s+/g, ''));
      if (isStrongsPattern && currentMode !== 'topics') setMode('strongs');
      if (currentMode === 'strongs') {
        handleStrongsSearch(query);
      } else if (currentMode === 'topics') {
        handleTopicsSearch(query);
      } else {
        handleSearchInput(query);
      }
    }

    // Pre-fill from ?q=, ?s=, or ?t= URL params
    var params = new URLSearchParams(window.location.search);
    var s = params.get('s') || '';
    var q = params.get('q') || '';
    var t = params.get('t') || '';
    if (s) { input.value = s; setMode('strongs'); handleStrongsSearch(s); }
    else if (t) { input.value = t; setMode('topics'); handleTopicsSearch(t); }
    else if (q) { input.value = q; handleSearchInput(q); }

    input.addEventListener('input', function () {
      clearTimeout(_searchDebounce);
      _searchDebounce = setTimeout(function () {
        var query = input.value.trim();
        dispatchSearch(query);
        var url = new URL(window.location.href);
        if (currentMode === 'strongs' && query.length >= 2) {
          url.searchParams.set('s', query);
          url.searchParams.delete('q'); url.searchParams.delete('t');
        } else if (currentMode === 'topics' && query.length >= 3) {
          url.searchParams.set('t', query);
          url.searchParams.delete('q'); url.searchParams.delete('s');
        } else if (query.length >= 4) {
          url.searchParams.set('q', query);
          url.searchParams.delete('s'); url.searchParams.delete('t');
        } else {
          url.searchParams.delete('q'); url.searchParams.delete('s'); url.searchParams.delete('t');
        }
        history.replaceState(null, '', url.toString());
      }, 300);
    });
  }

  function closeSearch() { /* no-op: search lives on its own page */ }

  // ── Bible Reader ─────────────────────────────────────────────────────────
  function initReaderPage() {
    var triggerLookup = initReaderLookup();
    initReaderBrowse();
    initReaderKeyboard();

    // Bootstrap from URL params: ?ref= (preferred) or legacy ?book=&ch=&v=
    var params = new URLSearchParams(window.location.search);
    var refStr = params.get('ref') || '';
    if (!refStr) {
      var bk = params.get('book');
      var ch = params.get('ch');
      var v  = params.get('v');
      if (bk) refStr = bk + ' ' + (ch || '1') + (v ? ':' + v : '');
    }
    if (refStr && triggerLookup) {
      var input = document.getElementById('reader-lookup-input');
      if (input) { input.value = refStr; triggerLookup(); }
    }
  }

  // ── Reader lookup + render ────────────────────────────────────────────────
  function initReaderLookup() {
    var input    = document.getElementById('reader-lookup-input');
    var btn      = document.getElementById('reader-lookup-btn');
    var statusEl = document.getElementById('reader-lookup-status');
    if (!input) return null;

    function setStatus(msg) { if (statusEl) statusEl.textContent = msg; }

    function doLookup() {
      var q         = input.value.trim();
      var resultsEl = document.getElementById('reader-results');
      if (!q) { if (resultsEl) resultsEl.innerHTML = ''; return; }

      // Library ref intercept: "WCF 4", "WSC 1", "HC 26" etc.
      var libRef = parseLibraryRef(q);
      if (libRef) {
        setStatus('');
        var libUrl = new URL(window.location.href);
        libUrl.searchParams.set('ref', q);
        history.replaceState(null, '', libUrl.toString());
        renderReaderLibrary(libRef, q);
        return;
      }

      var refs = parseMultiRef(q, null);
      if (!refs.length) {
        setStatus('Could not parse — try: Gen 1, John 3:16-21, or WCF 1');
        return;
      }
      setStatus('');

      // Chapter-0 intercept: "Genesis 0" renders the book introduction page
      if (refs.length === 1 && refs[0].wholeChapter && refs[0].ch === 0) {
        var url0 = new URL(window.location.href);
        url0.searchParams.set('ref', q);
        history.replaceState(null, '', url0.toString());
        renderReaderBookIntro(refs[0].bookId, refs[0].bookName);
        return;
      }

      // Verse-window mode: when parallels are on, restrict a whole-chapter lookup to the first
      // PARALLEL_VERSE_WINDOW verses so each page stays manageable with parallel panels.
      // Navigation buttons then step through 5-verse windows rather than whole chapters.
      if (getParallelsEnabled() && refs.length === 1) {
        var r0 = refs[0];
        if (r0.wholeChapter) {
          // Full chapter \u2192 first window
          refs[0] = {
            bookId: r0.bookId, bookName: r0.bookName,
            ch: r0.ch, endCh: r0.ch,
            v: 1, endV: PARALLEL_VERSE_WINDOW,
            wholeChapter: false, verseWindow: true,
            display: r0.bookName + ' ' + r0.ch + ':1\u2013' + PARALLEL_VERSE_WINDOW
          };
          input.value = r0.bookName + ' ' + r0.ch + ':1-' + PARALLEL_VERSE_WINDOW;
        } else if (!r0.wholeChapter && r0.ch === r0.endCh) {
          // Same-chapter verse range (produced by window nav buttons) \u2014 mark as verseWindow
          // so the nav state and nav buttons behave consistently.
          r0.verseWindow = true;
        }
      }

      if (resultsEl) resultsEl.innerHTML = '<p class="reader-hint">Loading\u2026</p>';

      var version = getVersion();

      // Update URL so the lookup is shareable / survives a refresh
      var url = new URL(window.location.href);
      url.searchParams.set('ref', q);
      history.replaceState(null, '', url.toString());

      Promise.all(refs.map(function (ref) {
        return resolveVerses(ref, version)
          .then(function (verses) { return { ref: ref, verses: verses }; })
          .catch(function ()      { return { ref: ref, verses: null   }; });
      })).then(function (groups) {
        renderReaderResults(groups, version);
      });
    }

    _readerLookupFn = doLookup;
    if (btn) btn.addEventListener('click', doLookup);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); doLookup(); }
    });
    input.addEventListener('input', function () { setStatus(''); });
    return doLookup;
  }

  function initReaderBrowse() {
    var bookSel = document.getElementById('reader-book-select');
    var chSel   = document.getElementById('reader-ch-select');
    if (!bookSel || !chSel || !metaBooks) return;

    // Bible books optgroup
    var bibleGroup = document.createElement('optgroup');
    bibleGroup.label = 'Bible';
    metaBooks.forEach(function (b) {
      var opt = document.createElement('option');
      opt.value = b.id;
      opt.textContent = b.name;
      bibleGroup.appendChild(opt);
    });
    bookSel.appendChild(bibleGroup);

    // Library optgroup — loaded async from index.json
    fetch(LIB_INDEX_URL)
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (docs) {
        libIndexCache = docs;
        var libGroup = document.createElement('optgroup');
        libGroup.label = 'Library';
        docs.forEach(function (d) {
          var opt = document.createElement('option');
          opt.value = 'lib:' + d.abbrev.toLowerCase();
          opt.textContent = d.abbrev + ' — ' + d.title;
          libGroup.appendChild(opt);
        });
        bookSel.appendChild(libGroup);
      })
      .catch(function () { /* library group unavailable — ignore */ });

    bookSel.addEventListener('change', function () {
      var val = bookSel.value;

      // Library doc selected
      if (val && val.indexOf('lib:') === 0) {
        var abbrevKey = val.slice(4);
        var docId     = LIB_ABBREV_MAP[abbrevKey];
        if (!docId) return;
        var abbrev    = abbrevKey.toUpperCase();
        // Populate chapter select with sections once doc is loaded
        var fillSections = function (doc) {
          chSel._libDocId = docId;
          chSel._bookId   = null;
          chSel.innerHTML = '<option value="">§…</option>';
          for (var i = 1; i <= doc.totalSections; i++) {
            var o = document.createElement('option');
            o.value = String(i);
            o.textContent = i;
            chSel.appendChild(o);
          }
          chSel.disabled = false;
        };
        if (libDocCache[docId]) {
          fillSections(libDocCache[docId]);
        } else {
          fetch(LIB_DOCS_BASE + '/' + docId + '.json')
            .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
            .then(function (d) { libDocCache[docId] = d; fillSections(d); })
            .catch(function () {});
        }
        return;
      }

      // Bible book selected
      var bk = metaBooks.find(function (b) { return b.id === val; });
      if (!bk) {
        chSel.innerHTML = '<option value="">Ch…</option>';
        chSel.disabled = true;
        chSel._bookId   = null;
        chSel._libDocId = null;
        return;
      }
      chSel._bookId   = bk.id;
      chSel._libDocId = null;
      chSel.innerHTML = '<option value="">Ch…</option>';
      var introOpt = document.createElement('option');
      introOpt.value = '0';
      introOpt.textContent = 'Intro';
      chSel.appendChild(introOpt);
      for (var i = 1; i <= (bk.chapters || 999); i++) {
        var opt = document.createElement('option');
        opt.value = String(i);
        opt.textContent = i;
        chSel.appendChild(opt);
      }
      chSel.disabled = false;
    });

    chSel.addEventListener('change', function () {
      if (!bookSel.value || !chSel.value) return;
      var val = bookSel.value;
      var lookupInput = document.getElementById('reader-lookup-input');

      // Library section selected
      if (val.indexOf('lib:') === 0) {
        var abbrevKey2 = val.slice(4).toUpperCase();
        var ref2 = abbrevKey2 + ' ' + chSel.value;
        if (lookupInput) lookupInput.value = ref2;
        if (_readerLookupFn) _readerLookupFn();
        return;
      }

      // Bible chapter selected
      var bk = metaBooks.find(function (b) { return b.id === val; });
      if (!bk) return;
      var ref = bk.name + ' ' + chSel.value;
      if (lookupInput) lookupInput.value = ref;
      if (_readerLookupFn) _readerLookupFn();
    });
  }

  function initReaderKeyboard() {
    document.addEventListener('keydown', function (e) {
      var tag = document.activeElement && document.activeElement.tagName.toLowerCase();
      if (tag === 'input' || tag === 'textarea' || tag === 'select') return;
      if (_backdropEl && !_backdropEl.classList.contains('bsw-modal-backdrop--hidden')) return;
      if (!_readerNavState) return;
      var nav = _readerNavState;
      var goLeft  = e.key === 'ArrowLeft'  || e.key === 'k';
      var goRight = e.key === 'ArrowRight' || e.key === 'j';
      if (!goLeft && !goRight) return;

      var ref = null;

      if (nav.verseStart !== null) {
        // Verse-window mode: step by PARALLEL_VERSE_WINDOW
        if (goLeft) {
          if (nav.verseStart > 1) {
            var ps = Math.max(1, nav.verseStart - PARALLEL_VERSE_WINDOW);
            var pe = nav.verseStart - 1;
            ref = nav.bookName + ' ' + nav.ch + ':' + ps + '-' + pe;
          } else if (nav.ch > 1) {
            ref = nav.bookName + ' ' + (nav.ch - 1); // intercepted → first window of prev chapter
          }
        } else {
          if (!nav.atChEnd) {
            var ns = nav.verseEnd + 1;
            var ne = nav.verseEnd + PARALLEL_VERSE_WINDOW;
            if (nav.maxChV) ne = Math.min(ne, nav.maxChV);
            ref = nav.bookName + ' ' + nav.ch + ':' + ns + '-' + ne;
          } else if (nav.ch < nav.maxCh) {
            ref = nav.bookName + ' ' + (nav.ch + 1); // intercepted → first window of next chapter
          }
        }
      } else {
        // Standard chapter-by-chapter mode (ch=0 = intro page)
        if (goLeft && nav.ch > 1) {
          ref = nav.bookName + ' ' + (nav.ch - 1);
        } else if (goLeft && nav.ch === 1) {
          ref = nav.bookName + ' 0'; // back to intro
        } else if (goRight && nav.ch === 0) {
          ref = nav.bookName + ' 1'; // intro → chapter 1
        } else if (goRight && nav.ch < nav.maxCh) {
          ref = nav.bookName + ' ' + (nav.ch + 1);
        }
      }

      if (!ref) return;
      e.preventDefault();
      var lookupInput = document.getElementById('reader-lookup-input');
      if (lookupInput) lookupInput.value = ref;
      if (_readerLookupFn) _readerLookupFn();
    });
  }

  function renderReaderSidebar(bookId, ch) {
    var sidebar = document.getElementById('reader-sidebar');
    if (!sidebar) return;
    if (!bookId || !metaBooks) { sidebar.innerHTML = ''; return; }
    var bk = metaBooks.find(function (b) { return b.id === bookId; });
    if (!bk) { sidebar.innerHTML = ''; return; }

    var maxCh = bk.chapters || 150;
    var html = '<div class="reader-sidebar__book">' + escHtml(bk.name) + '</div>';
    var introActive = (ch === 0) ? ' reader-sidebar__intro--active' : '';
    html += '<div class="reader-sidebar__intro-row">' +
      '<button class="reader-sidebar__intro' + introActive + '" data-nav-label="' +
      escHtml(bk.name + ' 0') + '">Intro</button>' +
      '</div>';
    html += '<div class="reader-sidebar__grid">';
    for (var i = 1; i <= maxCh; i++) {
      var active = (i === ch) ? ' reader-sidebar__ch--active' : '';
      html += '<button class="reader-sidebar__ch' + active + '" data-nav-label="' +
        escHtml(bk.name + ' ' + i) + '">' + i + '</button>';
    }
    html += '</div>';
    sidebar.innerHTML = html;

    if (!sidebar._navWired) {
      sidebar._navWired = true;
      sidebar.addEventListener('click', function (e) {
        var btn = e.target.closest('.reader-sidebar__ch, .reader-sidebar__intro');
        if (!btn) return;
        var label = btn.getAttribute('data-nav-label');
        if (!label) return;
        var input = document.getElementById('reader-lookup-input');
        if (input) input.value = label;
        if (_readerLookupFn) _readerLookupFn();
      });
    }

    var activeBtn = sidebar.querySelector('.reader-sidebar__ch--active');
    if (activeBtn) {
      setTimeout(function () { activeBtn.scrollIntoView({ block: 'nearest' }); }, 50);
    }
  }

  function syncBrowseSelects() {
    if (!_readerNavState) return;
    // Library nav state is synced directly by renderReaderLibrary — skip here.
    if (_readerNavState.isLib) return;
    var bookSel = document.getElementById('reader-book-select');
    var chSel   = document.getElementById('reader-ch-select');
    if (!bookSel || !chSel) return;
    bookSel.value = _readerNavState.bookId;
    var bk = metaBooks && metaBooks.find(function (b) { return b.id === _readerNavState.bookId; });
    if (!bk) return;
    if (chSel._bookId !== _readerNavState.bookId) {
      chSel._bookId = _readerNavState.bookId;
      chSel.innerHTML = '<option value="">Ch…</option>';
      var introOpt = document.createElement('option');
      introOpt.value = '0';
      introOpt.textContent = 'Intro';
      chSel.appendChild(introOpt);
      for (var i = 1; i <= (bk.chapters || 999); i++) {
        var opt = document.createElement('option');
        opt.value = String(i);
        opt.textContent = i;
        chSel.appendChild(opt);
      }
      chSel.disabled = false;
    }
    chSel.value = String(_readerNavState.ch);
  }

  function _buildNavButtons(ref, maxCh, verses, extraClass) {
    // Build prev/next nav HTML for a single result group.
    // In verse-window mode (ref.verseWindow), advance by PARALLEL_VERSE_WINDOW instead of a chapter.
    var cls = 'reader-chapter-nav' + (extraClass ? ' ' + extraClass : '');
    var html = '<div class="' + cls + '">';

    if (ref.wholeChapter) {
      // Standard chapter navigation (ch=1 prev links to intro)
      if (ref.ch > 1) {
        var p = ref.bookName + ' ' + (ref.ch - 1);
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(p) + '">← ' + escHtml(p) + '</button>';
      } else if (ref.ch === 1) {
        var introLbl = ref.bookName + ' 0';
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(introLbl) + '">← Intro</button>';
      } else {
        html += '<span></span>';
      }
      if (ref.ch < maxCh) {
        var n = ref.bookName + ' ' + (ref.ch + 1);
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(n) + '">' + escHtml(n) + ' →</button>';
      }
    } else if (ref.verseWindow) {
      // Verse-window mode: step by PARALLEL_VERSE_WINDOW within the chapter; wrap at boundaries.
      var maxV    = verses && verses.chapterMaxV;
      var startV  = ref.v;
      var endV    = ref.endV;
      // At chapter end if: got fewer verses than requested, OR endV reached/passed the last verse.
      var atChEnd = !verses || verses.length < PARALLEL_VERSE_WINDOW ||
                    (maxV !== undefined && endV >= maxV);

      // Prev button
      if (startV > 1) {
        var prevStart = Math.max(1, startV - PARALLEL_VERSE_WINDOW);
        var prevEnd   = startV - 1;
        var prevLbl   = ref.bookName + ' ' + ref.ch + ':' + prevStart + '-' + prevEnd;
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(prevLbl) + '">← Prev 5 verses</button>';
      } else if (ref.ch > 1) {
        var prevChLbl = ref.bookName + ' ' + (ref.ch - 1);
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(prevChLbl) + '">← ' + escHtml(ref.bookName + ' ' + (ref.ch - 1)) + '</button>';
      } else if (ref.ch === 1) {
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(ref.bookName + ' 0') + '">← Intro</button>';
      } else {
        html += '<span></span>';
      }

      // Next button
      if (!atChEnd) {
        var nextStart = endV + 1;
        var nextEnd   = endV + PARALLEL_VERSE_WINDOW;
        if (maxV) nextEnd = Math.min(nextEnd, maxV);
        var nextLbl   = ref.bookName + ' ' + ref.ch + ':' + nextStart + '-' + nextEnd;
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(nextLbl) + '">Next 5 verses →</button>';
      } else if (ref.ch < maxCh) {
        var nextChLbl = ref.bookName + ' ' + (ref.ch + 1);
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(nextChLbl) + '">' + escHtml(ref.bookName + ' ' + (ref.ch + 1)) + ' →</button>';
      }
    }

    html += '</div>';
    return html;
  }

  // ── Library document reader ──────────────────────────────────────────────
  function renderReaderLibrary(libRef, rawStr) {
    var el = document.getElementById('reader-results');
    if (!el) return;

    el.innerHTML = '<p class="reader-hint">Loading…</p>';

    var browseHint = document.querySelector('.reader-browse-hint');
    if (browseHint) browseHint.textContent = 'j / → next section · k / ← prev';

    // Seed nav state with bookName = abbrev so keyboard shortcuts produce "WCF 5" etc.
    _readerNavState = {
      bookId: null, bookName: libRef.abbrev,
      ch: parseInt(libRef.section, 10), maxCh: null,
      verseStart: null, verseEnd: null, atChEnd: false,
      isLib: true
    };

    function loadDoc() {
      return libDocCache[libRef.docId]
        ? Promise.resolve(libDocCache[libRef.docId])
        : fetch(LIB_DOCS_BASE + '/' + libRef.docId + '.json')
            .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
            .then(function (d) { libDocCache[libRef.docId] = d; return d; });
    }

    loadDoc().then(function (doc) {
      if (_readerNavState && _readerNavState.isLib) {
        _readerNavState.maxCh = doc.totalSections;
      }

      var secNum  = parseInt(libRef.section, 10);
      var section = doc.sections.find(function (s) { return parseInt(s.ref, 10) === secNum; })
                 || doc.sections[0];
      if (!section) {
        el.innerHTML = '<p class="reader-hint">Section not found.</p>';
        return;
      }

      var total  = doc.totalSections;
      var abbrev = doc.abbrev;

      function navBtn(label, text) {
        return '<button class="reader-nav-btn" data-nav-label="' + escHtml(label) + '">' + escHtml(text) + '</button>';
      }

      var prevNum = secNum - 1;
      var nextNum = secNum + 1;
      var prevHtml = prevNum >= 1 ? navBtn(abbrev + ' ' + prevNum, '← ' + abbrev + ' ' + prevNum) : '<span></span>';
      var nextHtml = nextNum <= total ? navBtn(abbrev + ' ' + nextNum, abbrev + ' ' + nextNum + ' →') : '';
      var navRow = '<div class="reader-chapter-nav">' + prevHtml + nextHtml + '</div>';

      var html = '<div class="reader-result-group reader-lib-section">';
      html += navRow;
      html += '<h2 class="reader-result-group__title">' + escHtml(abbrev + ' ' + section.ref) + '</h2>';
      html += '<p class="reader-lib-docname">' + escHtml(doc.title) + '</p>';
      html += '<div class="reader-lib-content">' + section.html + '</div>';
      html += navRow.replace('reader-chapter-nav"', 'reader-chapter-nav reader-chapter-nav--bottom"');
      html += '</div>';

      // Update sidebar to show section numbers for this doc
      var sidebar = document.getElementById('reader-sidebar');
      if (sidebar) {
        var sbHtml = '<div class="reader-sidebar__book">' + escHtml(abbrev) + '</div>';
        sbHtml += '<div class="reader-sidebar__grid">';
        for (var i = 1; i <= total; i++) {
          var active = (i === secNum) ? ' reader-sidebar__ch--active' : '';
          sbHtml += '<button class="reader-sidebar__ch' + active + '" data-nav-label="' +
            escHtml(abbrev + ' ' + i) + '">' + i + '</button>';
        }
        sbHtml += '</div>';
        sidebar.innerHTML = sbHtml;
        if (!sidebar._libNavWired) {
          sidebar._libNavWired = true;
          sidebar.addEventListener('click', function (e) {
            var btn = e.target.closest('.reader-sidebar__ch');
            if (!btn) return;
            var lbl = btn.getAttribute('data-nav-label');
            if (!lbl) return;
            var inp = document.getElementById('reader-lookup-input');
            if (inp) inp.value = lbl;
            if (_readerLookupFn) _readerLookupFn();
          });
        }
        var activeBtn = sidebar.querySelector('.reader-sidebar__ch--active');
        if (activeBtn) setTimeout(function () { activeBtn.scrollIntoView({ block: 'nearest' }); }, 50);
      }

      // Sync browse selects for library doc
      var bookSel = document.getElementById('reader-book-select');
      var chSel   = document.getElementById('reader-ch-select');
      if (bookSel) bookSel.value = 'lib:' + abbrev.toLowerCase();
      if (chSel) {
        if (chSel._libDocId !== libRef.docId) {
          chSel._libDocId = libRef.docId;
          chSel.innerHTML = '<option value="">§…</option>';
          for (var j = 1; j <= total; j++) {
            var opt = document.createElement('option');
            opt.value = String(j);
            opt.textContent = j;
            chSel.appendChild(opt);
          }
          chSel.disabled = false;
        }
        chSel.value = libRef.section;
      }

      el.innerHTML = html;
      wireReaderNav(el);

      // Wire .ref links so verse tooltips work within confession text
      wireRefLinks();
    }).catch(function () {
      el.innerHTML = '<p class="reader-hint">Could not load library document.</p>';
    });
  }

  // ── Book intro page (Chapter 0) ───────────────────────────────────────────
  function renderReaderBookIntro(bookId, bookName) {
    var el = document.getElementById('reader-results');
    if (!el) return;
    var bkMeta = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
    var maxCh = bkMeta ? (bkMeta.chapters || 999) : 999;

    _readerNavState = {
      bookId: bookId, bookName: bookName, ch: 0, maxCh: maxCh,
      verseStart: null, verseEnd: null, atChEnd: false
    };
    syncBrowseSelects();
    renderReaderSidebar(bookId, 0);
    if (_bookInfoOpen) _refreshBookInfoPanel();

    var browseHint = document.querySelector('.reader-browse-hint');
    if (browseHint) browseHint.textContent = 'j / → next chapter · k / ← prev';

    el.innerHTML = '<p class="reader-hint">Loading…</p>';

    if (_bookInfoCache[bookId]) {
      _renderIntroInReader(el, _bookInfoCache[bookId], bookId, bookName, maxCh);
      return;
    }
    var url = _resolve('../../data/books/introductions/' + bookId + '.json');
    fetch(url)
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (data) {
        _bookInfoCache[bookId] = data;
        if (_readerNavState && _readerNavState.bookId === bookId && _readerNavState.ch === 0)
          _renderIntroInReader(el, data, bookId, bookName, maxCh);
      })
      .catch(function () {
        el.innerHTML = '<p class="reader-hint">No introduction available for this book yet.</p>';
      });
  }

  function _riSection(heading, contentHtml) {
    return '<section class="ri-section">' +
      '<h3 class="ri-section__heading">' + escHtml(heading) + '</h3>' +
      contentHtml + '</section>';
  }

  function _renderIntroInReader(el, d, bookId, bookName, maxCh) {
    var ch1Lbl = bookName + ' 1';
    var body   = '';

    // Author / Date meta row
    body += '<div class="ri-meta">' +
      '<span><strong>Author:</strong> ' + escHtml(d.author || '—') + '</span>' +
      '<span><strong>Date:</strong> '   + escHtml(d.date   || '—') + '</span>' +
      '</div>';

    // Purpose
    if (d.purpose || d.setting) {
      body += _riSection('Purpose', '<p class="ri-body">' + escHtml(d.purpose || d.setting) + '</p>');
    }

    // Historical Context (enriched field)
    if (d.context) {
      body += _riSection('Historical Context', '<p class="ri-body">' + escHtml(d.context) + '</p>');
    }

    // Themes — expanded detail when available, chips as fallback
    if (d.themes_detail && d.themes_detail.length) {
      var tdHtml = d.themes_detail.map(function (t) {
        return '<div class="ri-theme-item">' +
          '<h4 class="ri-theme-title">' + escHtml(t.title) + '</h4>' +
          '<p class="ri-body">' + escHtml(t.text) + '</p>' +
          '</div>';
      }).join('');
      body += _riSection('Key Themes', tdHtml);
    } else if (d.themes && d.themes.length) {
      var chips = '<div class="reader-bookinfo-themes">' +
        d.themes.map(function (t) {
          return '<span class="reader-bookinfo-theme">' + escHtml(t) + '</span>';
        }).join('') + '</div>';
      body += _riSection('Themes', chips);
    }

    // Key People (enriched field)
    if (d.key_people && d.key_people.length) {
      var ppHtml = '<ul class="ri-people">' +
        d.key_people.map(function (p) {
          return '<li class="ri-person"><strong class="ri-person__name">' +
            escHtml(p.name) + '</strong><span class="ri-person__role"> — ' +
            escHtml(p.role) + '</span></li>';
        }).join('') + '</ul>';
      body += _riSection('Key People', ppHtml);
    }

    // Structural Outline
    if (d.outline && d.outline.length) {
      var olHtml = '<ol class="reader-bookinfo-outline">' +
        d.outline.map(function (s) {
          var link = s.ref
            ? '<a class="ref" data-ref="' + escHtml(s.ref) + '">' + escHtml(s.label) + '</a>'
            : escHtml(s.label);
          return '<li>' + link +
            (s.chapters ? ' <span class="reader-bookinfo-ch">ch. ' + escHtml(s.chapters) + '</span>' : '') +
            '</li>';
        }).join('') + '</ol>';
      body += _riSection('Outline', olHtml);
    }

    // Key Verses — multi-list if enriched, single verse as fallback
    if (d.key_verses && d.key_verses.length) {
      var kvHtml = '<ul class="ri-keyverses">' +
        d.key_verses.map(function (kv) {
          return '<li class="ri-keyverse">' +
            '<a class="ref ri-keyverse__ref" data-ref="' + escHtml(kv.ref) + '">' + escHtml(kv.ref) + '</a>' +
            (kv.note ? '<span class="ri-keyverse__note"> — ' + escHtml(kv.note) + '</span>' : '') +
            '</li>';
        }).join('') + '</ul>';
      body += _riSection('Key Verses', kvHtml);
    } else if (d.key_verse) {
      body += _riSection('Key Verse',
        '<p class="ri-body"><a class="ref" data-ref="' + escHtml(d.key_verse) + '">' +
        escHtml(d.key_verse) + '</a></p>');
    }

    // Christ in [Book] (enriched field)
    if (d.christ_connection) {
      body += _riSection('Christ in ' + d.title,
        '<p class="ri-body ri-body--christ">' + escHtml(d.christ_connection) + '</p>');
    }

    // Timeline
    if (d.timeline) {
      var tl = d.timeline, tlParts = [];
      if (tl.before && tl.before.length) {
        tlParts.push(tl.before.map(function (b) {
          return '<a class="ref" data-ref="' + escHtml(b.ref) + '">← ' + escHtml(b.label) + '</a>';
        }).join(' · '));
      }
      tlParts.push('<strong class="ri-tl-current">' + escHtml(d.title) + '</strong>' +
        (tl.date ? ' <span class="reader-bookinfo-tldate">(' + escHtml(tl.date) + ')</span>' : ''));
      if (tl.after && tl.after.length) {
        tlParts.push(tl.after.map(function (a) {
          return '<a class="ref" data-ref="' + escHtml(a.ref) + '">' + escHtml(a.label) + ' →</a>';
        }).join(' · '));
      }
      body += _riSection('Redemptive-Historical Timeline',
        '<div class="ri-timeline">' + tlParts.join('<span class="ri-tl-sep"> · </span>') + '</div>');
    }

    el.innerHTML =
      '<div class="reader-intro-page">' +
        '<div class="reader-chapter-nav">' +
          '<span></span>' +
          '<button class="reader-nav-btn" data-nav-label="' + escHtml(ch1Lbl) + '">' + escHtml(ch1Lbl) + ' →</button>' +
        '</div>' +
        '<div class="reader-intro-inner">' +
          '<h2 class="reader-intro-title">Introduction to ' + escHtml(d.title) + '</h2>' +
          body +
        '</div>' +
        '<div class="reader-chapter-nav reader-chapter-nav--bottom reader-intro-begin">' +
          '<span></span>' +
          '<button class="reader-nav-btn reader-nav-btn--begin" data-nav-label="' + escHtml(ch1Lbl) + '">Begin Reading ' + escHtml(bookName) + ' →</button>' +
        '</div>' +
      '</div>';

    wireReaderNav(el);
    wireRefLinks(el);
  }

  function renderReaderResults(groups, version) {
    var el = document.getElementById('reader-results');
    if (!el) return;
    var html = '';
    groups.forEach(function (g, idx) {
      var bkMeta = metaBooks && metaBooks.find(function (b) { return b.id === g.ref.bookId; });
      var maxCh  = bkMeta ? (bkMeta.chapters || 999) : 999;
      html += '<div class="reader-result-group">';

      // Top navigation: whole-chapter or verse-window
      if (g.ref.wholeChapter || g.ref.verseWindow) {
        html += _buildNavButtons(g.ref, maxCh, g.verses, '');
      }

      html += '<h2 class="reader-result-group__title">' + escHtml(g.ref.display) + '</h2>';
      if (!g.verses || !g.verses.length) {
        html += '<p class="reader-hint">Not available in ' + escHtml(version) + '.</p>';
      } else if (getInterlinearEnabled()) {
        html += '<div class="reader-result-group__text reader-interlinear-text">';
        g.verses.forEach(function (vObj) {
          html += '<div class="reader-verse-block">' +
            '<span class="reader-verse" data-ch="' + vObj.chapter + '" data-v="' + vObj.verse + '">' +
            '<sup class="reader-verse__num">' + vObj.verse + '</sup>' +
            escHtml(vObj.text) + '</span>' +
            '<div class="reader-interlinear-row" data-ch="' + vObj.chapter + '" data-v="' + vObj.verse + '"></div>' +
            '</div>';
        });
        html += '</div>';
        var attr = ATTRIBUTION[version];
        if (attr) html += '<p class="reader-result-group__attr">' + escHtml(attr) + '</p>';
      } else {
        html += '<p class="reader-result-group__text">';
        g.verses.forEach(function (vObj) {
          html += '<span class="reader-verse" data-ch="' + vObj.chapter + '" data-v="' + vObj.verse + '">' +
            '<sup class="reader-verse__num">' + vObj.verse + '</sup>' +
            escHtml(vObj.text) + '</span> ';
        });
        html += '</p>';
        var attr = ATTRIBUTION[version];
        if (attr) html += '<p class="reader-result-group__attr">' + escHtml(attr) + '</p>';
      }

      // Bottom nav mirrors top for easy forward/back after reading
      if (g.ref.wholeChapter || g.ref.verseWindow) {
        html += _buildNavButtons(g.ref, maxCh, g.verses, 'reader-chapter-nav--bottom');
      }

      html += '</div>';
    });

    // Track nav state for keyboard shortcuts
    if (groups.length === 1 && (groups[0].ref.wholeChapter || groups[0].ref.verseWindow)) {
      var navBk = metaBooks && metaBooks.find(function (b) { return b.id === groups[0].ref.bookId; });
      var navRef = groups[0].ref;
      var navVs  = groups[0].verses;
      var navMaxV = navRef.verseWindow ? (navVs && navVs.chapterMaxV) : undefined;
      _readerNavState = {
        bookId:     navRef.bookId,
        bookName:   navRef.bookName,
        ch:         navRef.ch,
        maxCh:      navBk ? (navBk.chapters || 999) : 999,
        verseStart: navRef.verseWindow ? navRef.v   : null,
        verseEnd:   navRef.verseWindow ? navRef.endV : null,
        maxChV:     navMaxV,
        atChEnd:    navRef.verseWindow ? (
          !navVs || navVs.length < PARALLEL_VERSE_WINDOW ||
          (navMaxV !== undefined && navRef.endV >= navMaxV)
        ) : false
      };
    } else {
      _readerNavState = null;
    }
    syncBrowseSelects();

    // Update keyboard hint to match current nav mode
    var browseHint = document.querySelector('.reader-browse-hint');
    if (browseHint) {
      browseHint.textContent = (_readerNavState && _readerNavState.verseStart !== null)
        ? 'j / → next 5 verses · k / ← prev'
        : 'j / → next chapter · k / ← prev';
    }

    // Sidebar: show chapter grid for any single-book result set
    var sidebarBookId = null, sidebarCh = null;
    if (groups.length >= 1) {
      var firstBkId = groups[0].ref.bookId;
      var allSameBook = groups.every(function (g) { return g.ref.bookId === firstBkId; });
      if (allSameBook) {
        sidebarBookId = firstBkId;
        if (groups.length === 1 && groups[0].ref.wholeChapter) sidebarCh = groups[0].ref.ch;
      }
    }
    renderReaderSidebar(sidebarBookId, sidebarCh);
    if (_bookInfoOpen) _refreshBookInfoPanel();

    // When _readerNavState is null (single-verse or multi-group search),
    // syncBrowseSelects() skips updating bookSel. Sync it here so the
    // study-link banner MutationObserver reads the correct current book.
    if (!_readerNavState) {
      var _bSel = document.getElementById('reader-book-select');
      if (_bSel) _bSel.value = sidebarBookId || '';
    }

    el.innerHTML = html || '<p class="reader-hint">No results.</p>';

    // Clear the side panel — it will be rebuilt incrementally as cross-refs load
    var xrefPanel = document.getElementById('reader-xref-panel');
    if (xrefPanel) xrefPanel.innerHTML = '';

    wireReaderNav(el);
    wireVerseNumberPopup(el);
    applyHighlights(el);
    applyBookmarks(el);

    // Track rendered groups, inject cross-refs and (if enabled) parallel panels
    _readerGroups = [];
    var domGroups = el.querySelectorAll('.reader-result-group');
    groups.forEach(function (g, idx) {
      var groupEl = domGroups[idx];
      if (!groupEl) return;
      _readerGroups.push({ ref: g.ref, el: groupEl });
      injectReaderFootnotes(g.ref, groupEl);
      if (getParallelsEnabled()) injectParallelPanels(g.ref, groupEl);
      if (getInterlinearEnabled()) injectAllInterlinearRows(g.ref, groupEl);
    });

    // Inject compare panels after all other injections
    if (isCompareEnabled()) {
      var cmpVer = getCompareVersion();
      if (cmpVer && cmpVer !== version) injectComparePanel(groups, cmpVer, el);
    }
  }

  // ── Reader side panel: Notes / Cross-refs / Commentary switcher ──────────
  var _readerPanelActiveTab = 'notes';

  function _ensureReaderPanelStructure(panel) {
    if (panel.querySelector('.reader-panel-tabs')) return;
    panel.innerHTML =
      '<div class="reader-panel-tabs">' +
        '<button class="reader-panel-tab" data-ptab="notes">Notes</button>' +
        '<button class="reader-panel-tab" data-ptab="xrefs">Cross-refs</button>' +
        '<button class="reader-panel-tab" data-ptab="commentary">Commentary</button>' +
      '</div>' +
      '<div class="reader-panel-notes reader-panel-body"></div>' +
      '<div class="reader-panel-xrefs reader-panel-body" hidden></div>' +
      '<div class="reader-panel-commentary reader-panel-body" hidden></div>';
    panel.querySelectorAll('.reader-panel-tab').forEach(function (btn) {
      btn.addEventListener('click', function () {
        _readerPanelActiveTab = btn.getAttribute('data-ptab');
        _activateReaderPanelTab(panel, _readerPanelActiveTab);
      });
    });
    _activateReaderPanelTab(panel, _readerPanelActiveTab);
  }

  function _activateReaderPanelTab(panel, tab) {
    panel.querySelectorAll('.reader-panel-tab').forEach(function (b) {
      b.classList.toggle('reader-panel-tab--active', b.getAttribute('data-ptab') === tab);
    });
    panel.querySelectorAll('.reader-panel-body').forEach(function (b) { b.hidden = true; });
    var bodyEl = panel.querySelector('.reader-panel-' + tab);
    if (bodyEl) bodyEl.hidden = false;
    if (tab === 'notes') _readerPanelRenderNotes(panel);
    else if (tab === 'commentary') _readerPanelRenderCommentary(panel);
  }

  function _readerPanelRenderNotes(panel) {
    var body = panel.querySelector('.reader-panel-notes');
    if (!body) return;
    body.innerHTML = '';
    var state = _readerNavState;
    if (!state) { body.innerHTML = '<p class="bsw-note-empty">Navigate to a chapter to see notes.</p>'; return; }

    var verses = document.querySelectorAll('#reader-results .reader-verse[data-ch][data-v]');
    var seen = Object.create(null), verseList = [];
    verses.forEach(function (el) {
      var key = el.getAttribute('data-ch') + ':' + el.getAttribute('data-v');
      if (!seen[key]) { seen[key] = true; verseList.push({ ch: el.getAttribute('data-ch'), v: el.getAttribute('data-v') }); }
    });

    var hasAny = false;
    verseList.forEach(function (vv) {
      var notes = getNotesForVerse(state.bookId, +vv.ch, +vv.v);
      if (!notes.length) return;
      hasAny = true;
      var group = document.createElement('div');
      group.className = 'reader-notes-group';
      var heading = document.createElement('div');
      heading.className = 'reader-notes-group__heading';
      heading.textContent = state.bookName + ' ' + vv.ch + ':' + vv.v;
      group.appendChild(heading);
      notes.forEach(function (note) {
        var item = document.createElement('div');
        item.className = 'reader-notes-item';
        var txt = document.createElement('div');
        txt.className = 'reader-notes-item__text';
        txt.textContent = note.text;
        var meta = document.createElement('div');
        meta.className = 'reader-notes-item__meta';
        var rangeLabel = note.display && note.display !== (state.bookName + ' ' + vv.ch + ':' + vv.v)
          ? note.display + ' · ' : '';
        meta.textContent = rangeLabel + _noteRelTime(note.updated);
        var actions = document.createElement('div');
        actions.className = 'bsw-note-actions';
        var delBtn = document.createElement('button');
        delBtn.className = 'bsw-note-action-btn bsw-note-action-btn--del';
        delBtn.textContent = 'Delete';
        delBtn.addEventListener('click', (function (id) {
          return function () { deleteNoteV2(id); _readerPanelRenderNotes(panel); };
        })(note.id));
        actions.appendChild(delBtn);
        item.appendChild(txt);
        item.appendChild(meta);
        item.appendChild(actions);
        group.appendChild(item);
      });
      body.appendChild(group);
    });

    if (!hasAny) {
      var empty = document.createElement('p');
      empty.className = 'bsw-note-empty';
      empty.textContent = 'No notes for this passage.';
      body.appendChild(empty);
    }

    if (verseList.length) {
      var compose = document.createElement('div');
      compose.className = 'bsw-note-compose reader-panel-compose';
      var sel = document.createElement('select');
      sel.className = 'reader-panel-verse-sel';
      verseList.forEach(function (vv) {
        var opt = document.createElement('option');
        opt.value = vv.ch + ':' + vv.v;
        opt.textContent = state.bookName + ' ' + vv.ch + ':' + vv.v;
        sel.appendChild(opt);
      });
      var ta = document.createElement('textarea');
      ta.className = 'bsw-note-textarea';
      ta.placeholder = 'Add a note…';
      var saveBtn = document.createElement('button');
      saveBtn.className = 'vs-context-btn';
      saveBtn.textContent = 'Save';
      var footer = document.createElement('div');
      footer.className = 'bsw-note-compose-footer';
      footer.appendChild(sel);
      footer.appendChild(saveBtn);
      compose.appendChild(ta);
      compose.appendChild(footer);
      body.appendChild(compose);
      saveBtn.addEventListener('click', function () {
        var t = ta.value.trim();
        if (!t) return;
        var parts = sel.value.split(':');
        var p = parseRef(state.bookName + ' ' + parts[0] + ':' + parts[1]);
        if (p) { createNoteV2(p, t); ta.value = ''; _readerPanelRenderNotes(panel); }
      });
    }
  }

  function _readerPanelRenderCommentary(panel) {
    var body = panel.querySelector('.reader-panel-commentary');
    if (!body || body._commLoaded) return;
    var state = _readerNavState;
    if (!state) { body.innerHTML = '<p class="bsw-note-empty">Navigate to a chapter to load commentary.</p>'; return; }
    body._commLoaded = true;

    var p = parseRef(state.bookName + ' ' + state.ch + ':1');
    if (!p) return;
    p.wholeChapter = true;
    p.endCh = p.ch;
    p.endV = 9999;

    var opts = COMMENTARY_SOURCES.map(function (s) {
      return '<option value="' + s.id + '"' + (s.id === _commentarySource ? ' selected' : '') + '>' + s.label + '</option>';
    }).join('');
    body.innerHTML =
      '<div class="reader-panel-comm-picker">' +
        '<select class="reader-panel-comm-select">' + opts + '</select>' +
      '</div>' +
      '<div class="reader-panel-comm-content"></div>';

    var sel       = body.querySelector('.reader-panel-comm-select');
    var contentEl = body.querySelector('.reader-panel-comm-content');

    function loadContent(src) {
      contentEl.innerHTML = '<p class="bsw-note-empty">Loading…</p>';
      loadCommentary(p.bookId, src).then(function (data) {
        var html = _extractCommHtml(data, p, src);
        if (!html) { contentEl.innerHTML = '<p class="bsw-note-empty">No commentary for this chapter.</p>'; return; }
        contentEl.innerHTML = html + '<p class="bsw-modal__commentary-attr">' + _commAttr(src) + '</p>';
        wireRefLinks(contentEl);
      }).catch(function () {
        contentEl.innerHTML = '<p class="bsw-note-empty">Could not load commentary.</p>';
      });
    }

    sel.addEventListener('change', function () {
      _commentarySource = sel.value;
      localStorage.setItem('bsw_comm_src', _commentarySource);
      loadContent(_commentarySource);
    });

    loadContent(_commentarySource);
  }

  // Rebuilds cross-ref content in the side panel; initializes switcher structure on first call.
  function _refreshXrefPanel() {
    var panel = document.getElementById('reader-xref-panel');
    if (!panel) return;
    _ensureReaderPanelStructure(panel);

    var xrefsBody = panel.querySelector('.reader-panel-xrefs');
    if (!xrefsBody) return;
    xrefsBody.innerHTML = '';

    var commBody = panel.querySelector('.reader-panel-commentary');
    if (commBody) { commBody._commLoaded = false; commBody.innerHTML = ''; }

    var sups = document.querySelectorAll('.reader-result-group .reader-xref-note');
    if (!sups.length) {
      if (_readerPanelActiveTab === 'notes') _readerPanelRenderNotes(panel);
      else if (_readerPanelActiveTab === 'commentary') _readerPanelRenderCommentary(panel);
      return;
    }

    var seenVerses = [], byVerse = Object.create(null);
    sups.forEach(function (sup) {
      var verse = sup.closest('.reader-verse');
      if (!verse) return;
      var ch = verse.getAttribute('data-ch'), v = verse.getAttribute('data-v');
      var key = ch + ':' + v;
      if (!byVerse[key]) { byVerse[key] = { ch: ch, v: v, sups: [] }; seenVerses.push(key); }
      byVerse[key].sups.push(sup);
    });

    seenVerses.forEach(function (key) {
      var vd = byVerse[key];
      var group = document.createElement('div');
      group.className = 'reader-xref-group';
      var title = document.createElement('div');
      title.className = 'reader-xref-group__title';
      title.textContent = 'v.' + vd.v;
      group.appendChild(title);
      var list = document.createElement('ul');
      list.className = 'reader-xref-group__list';
      vd.sups.forEach(function (sup) {
        var ref = sup.getAttribute('data-ref');
        if (!ref) return;
        var p = parseRef(ref);
        if (!p) return;
        var li = document.createElement('li');
        li.className = 'reader-xref-group__item';
        var num = document.createElement('span');
        num.className = 'reader-xref-group__num';
        num.textContent = sup.textContent;
        var link = document.createElement('span');
        link.className = 'reader-xref-group__link';
        link.textContent = ref;
        link.setAttribute('tabindex', '0');
        link.setAttribute('role', 'button');
        link.setAttribute('aria-label', 'Cross-reference: ' + ref);
        wireRefEl(link, p);
        li.appendChild(num);
        li.appendChild(link);
        list.appendChild(li);
      });
      group.appendChild(list);
      xrefsBody.appendChild(group);
    });

    if (_readerPanelActiveTab === 'notes') _readerPanelRenderNotes(panel);
    else if (_readerPanelActiveTab === 'commentary') _readerPanelRenderCommentary(panel);
  }

  function injectReaderFootnotes(parsed, groupEl) {
    if (!parsed || !groupEl) return;

    loadCrossRefs(parsed.bookId).then(function (data) {
      if (!data) return;

      var endCh = parsed.wholeChapter ? parsed.ch : Math.min(parsed.endCh, parsed.ch + 4);

      for (var c = parsed.ch; c <= endCh; c++) {
        var chData = data[String(c)];
        if (!chData) continue;
        var startV = (c === parsed.ch && !parsed.wholeChapter) ? parsed.v : 1;
        var stopV  = (c === parsed.endCh && !parsed.wholeChapter) ? Math.min(parsed.endV, 9999) : 9999;
        var keys   = Object.keys(chData).map(Number)
          .filter(function (n) { return n >= startV && n <= stopV; })
          .sort(function (a, b) { return a - b; });

        keys.forEach(function (vNum) {
          var rawRefs = chData[String(vNum)];
          if (!rawRefs || !rawRefs.length) return;

          var verseSpan = groupEl.querySelector(
            '.reader-verse[data-ch="' + c + '"][data-v="' + vNum + '"]'
          );
          if (!verseSpan) return;

          // Parse entries, rank by votes (most relevant first), limit to top 5,
          // then sort the survivors by canonical Bible order for display.
          var entries = rawRefs.map(parseCrossRefEntry);
          entries.sort(function (a, b) { return b.votes - a.votes; });
          entries = entries.slice(0, XREF_CHAPTER_LIMIT);
          entries.sort(_compareCanonical);

          entries.forEach(function (entry, fnNum) {
            var p = parseRef(entry.ref);
            if (!p) return;
            var sup = document.createElement('sup');
            sup.className = 'reader-xref-note';
            sup.setAttribute('data-ref', entry.ref);
            sup.setAttribute('aria-label', 'Cross-reference: ' + entry.ref);
            sup.setAttribute('tabindex', '0');
            sup.setAttribute('role', 'button');
            sup.textContent = String(fnNum + 1);
            wireRefEl(sup, p);
            verseSpan.appendChild(sup);
          });
        });
      }

      // Rebuild the side panel after each book's cross-refs load
      _refreshXrefPanel();

    }).catch(function () {});
  }

  // ── Parallel Passage Reader ───────────────────────────────────────────────

  var PARALLELS_STORAGE_KEY   = 'bsw_parallels';
  var PARALLEL_VERSE_WINDOW   = 5; // verses per page in verse-window mode (also preview count)
  var PARALLEL_PREVIEW_VERSES = PARALLEL_VERSE_WINDOW; // verses shown before "show more" expander

  function getParallelsEnabled() {
    return localStorage.getItem(PARALLELS_STORAGE_KEY) === '1';
  }

  function setParallelsEnabled(on) {
    localStorage.setItem(PARALLELS_STORAGE_KEY, on ? '1' : '0');
  }

  function loadParallels(bookId) {
    if (bookId in parallelsCache) return Promise.resolve(parallelsCache[bookId]);
    var url = PARALLELS_ROOT + '/' + bookId + '.json';
    return fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) {
        parallelsCache[bookId] = (data && Object.keys(data).length) ? data : null;
        return parallelsCache[bookId];
      })
      .catch(function () {
        parallelsCache[bookId] = null;
        return null;
      });
  }

  // Build and inject the toggle button into the reader browse bar
  function initParallelToggle() {
    var browseBar = document.querySelector('.reader-browse-bar');
    if (!browseBar || document.getElementById('reader-parallels-btn')) return;

    var btn = document.createElement('button');
    btn.id = 'reader-parallels-btn';
    btn.className = 'reader-parallels-btn' +
      (getParallelsEnabled() ? ' reader-parallels-btn--on' : '');
    btn.setAttribute('aria-pressed', getParallelsEnabled() ? 'true' : 'false');
    btn.title = 'Show parallel passages, fulfillments, and OT prophecy connections';
    btn.textContent = '⇌ Parallels';

    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, hint || null);

    btn.addEventListener('click', function () {
      var on = !getParallelsEnabled();
      setParallelsEnabled(on);
      btn.classList.toggle('reader-parallels-btn--on', on);
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');

      // If currently showing a whole chapter, reload so the verse-window mode (or lack of it)
      // activates immediately rather than requiring manual navigation.
      if (_readerNavState && _readerNavState.verseStart === null) {
        var chRef = _readerNavState.bookName + ' ' + _readerNavState.ch;
        var lookupInput = document.getElementById('reader-lookup-input');
        if (lookupInput) lookupInput.value = chRef;
        if (_readerLookupFn) { _readerLookupFn(); return; }
      }

      if (on) {
        injectAllParallelPanels();
      } else {
        removeAllParallelPanels();
      }
    });
  }

  function injectAllParallelPanels() {
    _readerGroups.forEach(function (item) {
      // Don't double-inject
      if (!item.el.querySelector('.reader-parallels-container')) {
        injectParallelPanels(item.ref, item.el);
      }
    });
  }

  function removeAllParallelPanels() {
    document.querySelectorAll('.reader-parallels-container').forEach(function (el) {
      el.remove();
    });
  }

  // Inject parallel panels for one result group
  function injectParallelPanels(parsed, groupEl) {
    if (!parsed || !groupEl) return;

    loadParallels(parsed.bookId).then(function (data) {
      if (!data) return;

      var startV = parsed.wholeChapter ? 1 : parsed.v;
      var endV   = parsed.wholeChapter ? 9999 : parsed.endV;
      var startCh = parsed.ch;
      var endCh   = parsed.wholeChapter ? parsed.ch : parsed.endCh;

      // Collect all parallel sections that start within the displayed range
      var sections = [];
      for (var c = startCh; c <= endCh; c++) {
        var chData = data[String(c)];
        if (!chData) continue;
        Object.keys(chData).forEach(function (vStr) {
          var vNum = parseInt(vStr, 10);
          var sv = (c === startCh) ? startV : 1;
          var ev = (c === endCh) ? endV : 9999;
          if (vNum < sv || vNum > ev) return;
          chData[vStr].forEach(function (entry) {
            sections.push({ ch: c, v: vNum, entry: entry });
          });
        });
      }
      if (!sections.length) return;

      // Sort by chapter then start verse
      sections.sort(function (a, b) { return a.ch - b.ch || a.v - b.v; });

      // Pre-fetch all parallel books in the background so text is ready when expanded
      var version = getVersion();
      var seenBooks = Object.create(null);
      sections.forEach(function (s) {
        (s.entry.refs || []).forEach(function (refObj) {
          var p = parseRef(refObj.passage);
          if (p && !seenBooks[p.bookId]) {
            seenBooks[p.bookId] = true;
            loadBook(version, p.bookId).catch(function () {});
          }
        });
      });

      // Build the container
      var container = document.createElement('div');
      container.className = 'reader-parallels-container';

      // Group sections by their verse label (avoid repeating the same label)
      sections.forEach(function (s) {
        var entry = s.entry;
        (entry.refs || []).forEach(function (refObj) {
          var panel = buildParallelPanel(refObj, entry, parsed.bookName, s.ch, s.v);
          if (panel) container.appendChild(panel);
        });
      });

      groupEl.appendChild(container);

      // Trigger text loading for each panel
      container.querySelectorAll('.reader-parallel-section[data-parallel-ref]')
        .forEach(function (panelEl) {
          var refStr = panelEl.getAttribute('data-parallel-ref');
          var p = parseRef(refStr);
          if (!p) return;
          var bodyEl = panelEl.querySelector('.reader-parallel-body');
          if (bodyEl) loadParallelText(p, bodyEl);
        });
    });
  }

  var _PARALLEL_TYPE_META = {
    'parallel':        { icon: '⇌', label: 'Parallel',      cls: 'reader-parallel-badge--parallel' },
    'fulfillment':     { icon: '✓', label: 'Fulfilled in',   cls: 'reader-parallel-badge--fulfillment' },
    'prophecy-source': { icon: '⌖', label: 'Prophesied in', cls: 'reader-parallel-badge--prophecy' },
    'quotation':       { icon: '«', label: 'Quoted in',      cls: 'reader-parallel-badge--quotation' }
  };

  function buildParallelPanel(refObj, entry, sourceBookName, startCh, startV) {
    var p = parseRef(refObj.passage);
    if (!p) return null;

    var typeMeta = _PARALLEL_TYPE_META[entry.type] || _PARALLEL_TYPE_META['parallel'];
    var verseLabel = sourceBookName + ' ' + startCh + ':' + startV;
    var sectionLabel = entry.label ? ' · ' + entry.label : '';

    var panel = document.createElement('div');
    panel.className = 'reader-parallel-section';
    panel.setAttribute('data-parallel-ref', refObj.passage);
    panel.setAttribute('data-parallel-type', entry.type || 'parallel');

    var header = document.createElement('div');
    header.className = 'reader-parallel-header';

    var badge = document.createElement('span');
    badge.className = 'reader-parallel-badge ' + typeMeta.cls;
    badge.textContent = typeMeta.icon + ' ' + typeMeta.label;

    var refSpan = document.createElement('span');
    refSpan.className = 'reader-parallel-ref-label';
    refSpan.innerHTML = escHtml(refObj.passage) +
      (sectionLabel ? '<em class="reader-parallel-section-label">' + escHtml(sectionLabel) + '</em>' : '');

    var collapseBtn = document.createElement('button');
    collapseBtn.className = 'reader-parallel-collapse';
    collapseBtn.setAttribute('aria-label', 'Collapse');
    collapseBtn.setAttribute('aria-expanded', 'true');
    collapseBtn.textContent = '▾';

    var readBtn = document.createElement('a');
    readBtn.className = 'reader-parallel-read-link';
    readBtn.href = READER_URL + '?ref=' + encodeURIComponent(refObj.passage);
    readBtn.textContent = '↗';
    readBtn.title = 'Open in Reader';

    header.appendChild(badge);
    header.appendChild(refSpan);
    header.appendChild(readBtn);
    header.appendChild(collapseBtn);

    var body = document.createElement('div');
    body.className = 'reader-parallel-body';
    body.innerHTML = '<span class="reader-parallel-loading">Loading…</span>';

    panel.appendChild(header);
    panel.appendChild(body);

    collapseBtn.addEventListener('click', function () {
      var collapsed = panel.classList.toggle('reader-parallel-section--collapsed');
      collapseBtn.textContent = collapsed ? '▸' : '▾';
      collapseBtn.setAttribute('aria-expanded', collapsed ? 'false' : 'true');
    });

    return panel;
  }

  function loadParallelText(parsedRef, bodyEl) {
    var version = getVersion();
    resolveVerses(parsedRef, version).then(function (verses) {
      if (!verses || !verses.length) {
        bodyEl.innerHTML = '<span class="reader-parallel-empty">Not available in ' +
          escHtml(version) + '.</span>';
        return;
      }

      var preview = verses.slice(0, PARALLEL_PREVIEW_VERSES);
      var rest    = verses.slice(PARALLEL_PREVIEW_VERSES);

      var html = '<p class="reader-parallel-text">';
      preview.forEach(function (vr) {
        html += '<span class="reader-verse" data-ch="' + vr.chapter + '" data-v="' + vr.verse + '">' +
          '<sup class="reader-verse__num">' + vr.verse + '</sup>' +
          escHtml(vr.text) + '</span> ';
      });
      html += '</p>';

      if (rest.length) {
        html += '<div class="reader-parallel-rest" hidden>';
        html += '<p class="reader-parallel-text">';
        rest.forEach(function (vr) {
          html += '<span class="reader-verse" data-ch="' + vr.chapter + '" data-v="' + vr.verse + '">' +
            '<sup class="reader-verse__num">' + vr.verse + '</sup>' +
            escHtml(vr.text) + '</span> ';
        });
        html += '</p></div>';
        html += '<button class="reader-parallel-more-btn">' +
          '▾ Show ' + rest.length + ' more verse' + (rest.length === 1 ? '' : 's') +
          '</button>';
      }

      bodyEl.innerHTML = html;

      var moreBtn = bodyEl.querySelector('.reader-parallel-more-btn');
      if (moreBtn) {
        moreBtn.addEventListener('click', function () {
          bodyEl.querySelector('.reader-parallel-rest').removeAttribute('hidden');
          moreBtn.remove();
        });
      }

      // Wire verse spans as ref links opening the modal
      bodyEl.querySelectorAll('.reader-verse').forEach(function (span) {
        var c = span.getAttribute('data-ch');
        var v = span.getAttribute('data-v');
        if (!c || !v) return;
        var refStr = parsedRef.bookName + ' ' + c + ':' + v;
        var pv = parseRef(refStr);
        if (!pv) return;
        span.style.cursor = 'pointer';
        span.addEventListener('click', function () { openModal(pv); });
      });
    }).catch(function () {
      bodyEl.innerHTML = '<span class="reader-parallel-empty">Could not load passage.</span>';
    });
  }

  function wireReaderNav(resultsEl) {
    if (resultsEl._navWired) return;
    resultsEl._navWired = true;
    resultsEl.addEventListener('click', function (e) {
      var btn = e.target.closest('.reader-nav-btn');
      if (!btn) return;
      var label = btn.getAttribute('data-nav-label');
      if (!label) return;
      var input = document.getElementById('reader-lookup-input');
      if (input) input.value = label;
      if (_readerLookupFn) _readerLookupFn();
    });
  }

  // ── Reader verse-number popup ─────────────────────────────────────────────
  var _vsPopupEl    = null;
  var _vsPopupRef   = null; // refStr currently shown in popup
  var _vsNoteEditor = null; // reference to the textarea in the popup

  function _popupHide() {
    if (!_vsPopupEl) return;
    _vsPopupEl.classList.remove('vs-verse-popup--visible');
    _vsPopupEl.setAttribute('aria-hidden', 'true');
    var noteArea = _vsPopupEl.querySelector('.vs-verse-popup__note-area');
    if (noteArea) noteArea.hidden = true;
    _vsPopupRef = null;
  }

  function _popupUpdateHighlightBtn(refStr) {
    var btn = _vsPopupEl && _vsPopupEl.querySelector('#vs-popup-highlight');
    if (!btn) return;
    var n = getNote(refStr);
    btn.textContent = (n && n.highlight) ? '★ Remove highlight' : '☆ Highlight verse';
    btn.classList.toggle('vs-verse-popup__action--active', !!(n && n.highlight));
  }

  function _popupUpdateBookmarkBtn(refStr) {
    var btn = _vsPopupEl && _vsPopupEl.querySelector('#vs-popup-bookmark');
    if (!btn) return;
    var on = isBookmarked(refStr);
    btn.textContent = on ? '★ Remove bookmark' : '☆ Bookmark';
    btn.classList.toggle('vs-verse-popup__action--active', on);
  }

  function wireVerseNumberPopup(resultsEl) {
    if (resultsEl._verseNumWired) return;
    resultsEl._verseNumWired = true;

    if (!_vsPopupEl) {
      var popup = document.createElement('div');
      popup.id = 'vs-verse-popup';
      popup.className = 'vs-verse-popup';
      popup.setAttribute('aria-hidden', 'true');
      popup.innerHTML =
        '<div class="vs-verse-popup__ref"></div>' +
        '<div class="vs-verse-popup__actions">' +
          '<a class="vs-verse-popup__action" id="vs-verse-popup-study" href="#">' +
            'Open in Verse Study' +
          '</a>' +
          '<a class="vs-verse-popup__action" id="vs-popup-compare" href="#">All translations →</a>' +
          '<button class="vs-verse-popup__action" id="vs-popup-bookmark" type="button">☆ Bookmark</button>' +
          '<button class="vs-verse-popup__action" id="vs-popup-highlight" type="button">☆ Highlight verse</button>' +
          '<button class="vs-verse-popup__action" id="vs-popup-note" type="button">✎ Add / edit note</button>' +
          '<button class="vs-verse-popup__action" id="vs-popup-memory" type="button">☆ Add to Memory</button>' +
          '<a class="vs-verse-popup__action" id="vs-popup-notes-link" href="' + NOTES_URL + '">My Notes →</a>' +
          '<a class="vs-verse-popup__action" id="vs-popup-bookmarks-link" href="' + BOOKMARKS_URL + '">Bookmarks →</a>' +
          '<a class="vs-verse-popup__action" id="vs-popup-memory-link" href="' + MEMORY_URL + '">Memory List →</a>' +
        '</div>' +
        '<div class="vs-verse-popup__note-area" hidden>' +
          '<textarea class="vs-verse-popup__textarea" rows="3" placeholder="Your note…"></textarea>' +
          '<div class="vs-verse-popup__note-btns">' +
            '<button class="vs-verse-popup__save-btn" type="button">Save</button>' +
            '<button class="vs-verse-popup__cancel-btn" type="button">Cancel</button>' +
          '</div>' +
        '</div>';
      document.body.appendChild(popup);
      _vsPopupEl = popup;

      document.addEventListener('click', function (e) {
        if (!_vsPopupEl.classList.contains('vs-verse-popup--visible')) return;
        if (!_vsPopupEl.contains(e.target) && !e.target.classList.contains('reader-verse__num')) {
          _popupHide();
        }
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && _vsPopupEl.classList.contains('vs-verse-popup--visible')) {
          _popupHide();
        }
      });

      // Bookmark toggle
      popup.querySelector('#vs-popup-bookmark').addEventListener('click', function () {
        if (!_vsPopupRef) return;
        var isOn = toggleBookmark(_vsPopupRef);
        _popupUpdateBookmarkBtn(_vsPopupRef);
        var numEl3 = _vsPopupCurrentSpan && _vsPopupCurrentSpan.querySelector('.reader-verse__num');
        if (numEl3) numEl3.classList.toggle('reader-verse__num--bookmarked', isOn);
      });

      // Highlight toggle
      popup.querySelector('#vs-popup-highlight').addEventListener('click', function () {
        if (!_vsPopupRef) return;
        var isOn = toggleHighlight(_vsPopupRef);
        _popupUpdateHighlightBtn(_vsPopupRef);
        var verseSpan = _vsPopupCurrentSpan;
        if (verseSpan) {
          verseSpan.classList.toggle('reader-verse--highlighted', isOn);
          var numEl2 = verseSpan.querySelector('.reader-verse__num');
          if (numEl2) numEl2.classList.toggle('reader-verse__num--highlighted', isOn);
        }
      });

      // Show/hide note editor
      popup.querySelector('#vs-popup-note').addEventListener('click', function () {
        var noteArea = popup.querySelector('.vs-verse-popup__note-area');
        var ta = popup.querySelector('.vs-verse-popup__textarea');
        noteArea.hidden = !noteArea.hidden;
        if (!noteArea.hidden && _vsPopupRef) {
          var n = getNote(_vsPopupRef);
          ta.value = (n && n.note) ? n.note : '';
          ta.focus();
        }
      });

      // Save note
      popup.querySelector('.vs-verse-popup__save-btn').addEventListener('click', function () {
        if (!_vsPopupRef) return;
        var ta = popup.querySelector('.vs-verse-popup__textarea');
        var n = getNote(_vsPopupRef) || {};
        n.note = ta.value.trim();
        saveNote(_vsPopupRef, n);
        popup.querySelector('.vs-verse-popup__note-area').hidden = true;
        // Update note indicator on verse
        if (_vsPopupCurrentSpan) {
          _vsPopupCurrentSpan.classList.toggle('reader-verse--has-note', !!n.note);
        }
      });

      // Cancel note
      popup.querySelector('.vs-verse-popup__cancel-btn').addEventListener('click', function () {
        popup.querySelector('.vs-verse-popup__note-area').hidden = true;
      });
    }

    resultsEl.addEventListener('click', function (e) {
      var numEl = e.target.closest('.reader-verse__num');
      if (!numEl) return;

      var verseSpan = numEl.closest('.reader-verse');
      if (!verseSpan) return;

      var ch = verseSpan.getAttribute('data-ch');
      var v  = verseSpan.getAttribute('data-v');
      if (!ch || !v) return;

      var bookName = _readerNavState ? _readerNavState.bookName : null;
      if (!bookName) {
        var group = numEl.closest('.reader-result-group');
        if (group) {
          var title = group.querySelector('.reader-result-group__title');
          if (title) {
            var m = (title.textContent || '').match(/^([\w\s]+?)\s+\d/);
            if (m) bookName = m[1].trim();
          }
        }
      }
      if (!bookName) return;

      var refStr = bookName + ' ' + ch + ':' + v;
      _vsPopupRef = refStr;
      _vsPopupCurrentSpan = verseSpan;

      var parsed = parseRef(refStr);
      if (parsed) {
        e.stopPropagation();
        openModal(parsed);
      }
    });
  }

  var _vsPopupCurrentSpan = null;

  // Apply highlights and note indicators to all .reader-verse elements
  function applyHighlights(resultsEl) {
    var notes = getNotes();
    var verses = resultsEl.querySelectorAll('.reader-verse[data-ch][data-v]');
    verses.forEach(function (span) {
      var ch = span.getAttribute('data-ch');
      var v  = span.getAttribute('data-v');
      // bookName from nav state or group title
      var bookName = _readerNavState ? _readerNavState.bookName : null;
      if (!bookName) {
        var group = span.closest('.reader-result-group');
        if (group) {
          var title = group.querySelector('.reader-result-group__title');
          if (title) {
            var m2 = (title.textContent || '').match(/^([\w\s]+?)\s+\d/);
            if (m2) bookName = m2[1].trim();
          }
        }
      }
      if (!bookName) return;
      var refStr = bookName + ' ' + ch + ':' + v;
      var n = notes[refStr];
      span.classList.toggle('reader-verse--highlighted', !!(n && n.highlight));
      span.classList.toggle('reader-verse--has-note', !!(n && n.note));
      var numEl = span.querySelector('.reader-verse__num');
      if (numEl) numEl.classList.toggle('reader-verse__num--highlighted', !!(n && n.highlight));
    });
  }

  function applyBookmarks(resultsEl) {
    var bookmarks = getBookmarks();
    if (bookmarks.length === 0) return;
    var set = Object.create(null);
    bookmarks.forEach(function (r) { set[r] = true; });

    var verses = resultsEl.querySelectorAll('.reader-verse[data-ch][data-v]');
    verses.forEach(function (span) {
      var ch = span.getAttribute('data-ch');
      var v  = span.getAttribute('data-v');
      var bookName = _readerNavState ? _readerNavState.bookName : null;
      if (!bookName) {
        var group = span.closest('.reader-result-group');
        if (group) {
          var title = group.querySelector('.reader-result-group__title');
          if (title) {
            var m3 = (title.textContent || '').match(/^([\w\s]+?)\s+\d/);
            if (m3) bookName = m3[1].trim();
          }
        }
      }
      if (!bookName) return;
      var refStr = bookName + ' ' + ch + ':' + v;
      var numEl = span.querySelector('.reader-verse__num');
      if (numEl) numEl.classList.toggle('reader-verse__num--bookmarked', !!set[refStr]);
    });
  }

  function handleSearchInput(query) {
    var statusEl  = document.getElementById('bsw-search-status');
    var resultsEl = document.getElementById('bsw-search-results');
    if (!statusEl || !resultsEl) return;

    var _lit = extractLiteral(query.toLowerCase().trim());
    var _isLiteral = _lit !== null && _lit.length >= 1;
    if (!_isLiteral && query.length < 4) {
      statusEl.textContent = query.length > 0
        ? 'Keep typing… (4+ characters, or "quote" for exact match)'
        : '';
      resultsEl.innerHTML = '';
      return;
    }

    var version = getVersion();
    if (!metaBooks || !metaBooks.length) {
      statusEl.textContent = 'Book data not loaded yet.';
      return;
    }

    var gen = ++_searchGeneration;
    var q   = query.toLowerCase();
    statusEl.textContent = 'Searching…';
    resultsEl.innerHTML  = '';

    var allResults = [];
    var loaded     = 0;

    var booksToSearch = metaBooks;
    var total = booksToSearch.length;

    booksToSearch.forEach(function (book) {
      var bookOrder = metaBooks.indexOf(book);
      loadBook(version, book.id)
        .then(function (chapters) {
          if (gen !== _searchGeneration) return;
          loaded++;
          if (chapters) {
            Object.keys(chapters).forEach(function (ch) {
              var chNum = parseInt(ch, 10);
              Object.keys(chapters[ch]).forEach(function (v) {
                var text = chapters[ch][v];
                if (fuzzyMatchVerse(text, query)) {
                  allResults.push({
                    bookOrder: bookOrder,
                    bookId: book.id,
                    bookName: book.name,
                    ch: chNum,
                    v: parseInt(v, 10),
                    ref: book.name + ' ' + ch + ':' + v,
                    text: text
                  });
                }
              });
            });
            allResults.sort(function (a, b) {
              if (a.bookOrder !== b.bookOrder) return a.bookOrder - b.bookOrder;
              if (a.ch !== b.ch) return a.ch - b.ch;
              return a.v - b.v;
            });
          }
          var done = loaded === total;
          renderSearchResults(allResults, query, gen);
          if (done) {
            statusEl.textContent = allResults.length
              ? allResults.length + ' result' + (allResults.length === 1 ? '' : 's') + ' in ' + version
              : 'No results for "' + query + '" in ' + version + '.';
          } else {
            statusEl.textContent = 'Searching… (' + loaded + ' / ' + total + ' books)';
          }
        })
        .catch(function () {
          if (gen !== _searchGeneration) return;
          loaded++;
          var done = loaded === total;
          if (done) {
            renderSearchResults(allResults, query, gen);
            statusEl.textContent = allResults.length
              ? allResults.length + ' result' + (allResults.length === 1 ? '' : 's') + ' in ' + version
              : 'No results for "' + query + '" in ' + version + '.';
          }
        });
    });
  }

  function renderSearchResults(results, query, gen) {
    if (gen !== _searchGeneration) return;
    var resultsEl = document.getElementById('bsw-search-results');
    if (!resultsEl) return;

    var MAX    = 200;
    var shown  = results.slice(0, MAX);

    resultsEl.innerHTML = shown.map(function (r) {
      var readHref = READER_URL + '?ref=' + encodeURIComponent(r.bookName + ' ' + r.ch);
      return '<div class="bsw-search-result" role="listitem"' +
               ' data-ref="' + escHtml(r.ref) + '" tabindex="0">' +
               '<div class="bsw-search-result__ref">' +
                 escHtml(r.ref) +
                 '<a class="bsw-search-result__read" href="' + readHref +
                   '" tabindex="-1">Read chapter</a>' +
               '</div>' +
               '<div class="bsw-search-result__text">' + highlightMatch(r.text, query) + '</div>' +
             '</div>';
    }).join('') + (results.length > MAX
      ? '<p class="bsw-search-more">Showing first ' + MAX + ' of ' + results.length +
          ' results — try a more specific phrase.</p>'
      : '');

    resultsEl.querySelectorAll('.bsw-search-result').forEach(function (el) {
      var parsed = parseRef(el.getAttribute('data-ref'));
      if (!parsed) return;
      var open = function () { closeSearch(); openModal(parsed); };
      el.addEventListener('click', open);
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
      });
    });
  }

  // ── Strong's number search ────────────────────────────────────────────────

  function handleStrongsSearch(rawId) {
    var statusEl  = document.getElementById('bsw-search-status');
    var resultsEl = document.getElementById('bsw-search-results');
    if (!statusEl || !resultsEl) return;

    var strongsId = rawId.replace(/\s+/g, '').toUpperCase();
    if (!/^[GH]\d+$/.test(strongsId)) {
      statusEl.textContent = 'Enter a Strong\'s number, e.g. G3056 or H430.';
      resultsEl.innerHTML = '';
      return;
    }

    var isGreek = strongsId.charAt(0) === 'G';
    statusEl.textContent = 'Loading…';
    resultsEl.innerHTML  = '';

    var gen = ++_searchGeneration;

    loadStrongs(isGreek ? 'greek' : 'hebrew').then(function (strongsDict) {
      if (gen !== _searchGeneration) return;
      var entry = strongsDict && strongsDict[strongsId];

      if (!metaBooks || !metaBooks.length) {
        statusEl.textContent = 'Book data not loaded yet.'; return;
      }

      var booksToSearch = metaBooks.filter(function (b) {
        return isGreek ? b.testament === 'NT' : b.testament === 'OT';
      });
      var total  = booksToSearch.length;
      var loaded = 0;
      var allResults = [];

      statusEl.textContent = 'Searching' +
        (entry && entry.gloss ? ' for "' + entry.gloss + '"' : ' ' + strongsId) + '…';
      renderStrongsResults([], strongsId, entry, gen);

      booksToSearch.forEach(function (book) {
        var bookOrder = metaBooks.indexOf(book);
        loadInterlinear(book.id).then(function (interlinear) {
          if (gen !== _searchGeneration) return;
          loaded++;
          if (interlinear) {
            Object.keys(interlinear).forEach(function (ch) {
              var chNum = parseInt(ch, 10);
              Object.keys(interlinear[ch]).forEach(function (v) {
                var toks     = interlinear[ch][v];
                var matching = toks && toks.filter(function (t) { return t.s === strongsId; });
                if (matching && matching.length) {
                  allResults.push({
                    bookOrder:    bookOrder,
                    bookId:       book.id,
                    bookName:     book.name,
                    ch:           chNum,
                    v:            parseInt(v, 10),
                    ref:          book.name + ' ' + chNum + ':' + v,
                    usagePhrases: matching.map(function (t) { return t.text || ''; }).filter(Boolean)
                  });
                }
              });
            });
            allResults.sort(function (a, b) {
              if (a.bookOrder !== b.bookOrder) return a.bookOrder - b.bookOrder;
              if (a.ch !== b.ch) return a.ch - b.ch;
              return a.v - b.v;
            });
          }
          var done = loaded === total;
          renderStrongsResults(allResults, strongsId, entry, gen);
          statusEl.textContent = done
            ? (allResults.length
                ? allResults.length + ' occurrence' + (allResults.length === 1 ? '' : 's') + ' of ' + strongsId
                : 'No occurrences of ' + strongsId + ' found.')
            : 'Searching… (' + loaded + ' / ' + total + ' books)';
        }).catch(function () {
          if (gen !== _searchGeneration) return;
          loaded++;
          if (loaded === total) {
            renderStrongsResults(allResults, strongsId, entry, gen);
            statusEl.textContent = allResults.length
              ? allResults.length + ' occurrence' + (allResults.length === 1 ? '' : 's') + ' of ' + strongsId
              : 'No occurrences of ' + strongsId + ' found.';
          }
        });
      });
    });
  }

  // ── Topics search ─────────────────────────────────────────────────────────
  var _topicsIndexCache = null;

  function _buildTopicsIndex() {
    if (_topicsIndexCache) return Promise.resolve(_topicsIndexCache);
    try {
      var cached = sessionStorage.getItem('bsw_topics_idx');
      if (cached) { _topicsIndexCache = JSON.parse(cached); return Promise.resolve(_topicsIndexCache); }
    } catch (e) {}

    return fetch(TOPICS_ROOT + 'index.html')
      .then(function (r) { return r.text(); })
      .then(function (html) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');
        var cards = doc.querySelectorAll('.topic-card');
        var entries = [];
        cards.forEach(function (card) {
          var href = card.getAttribute('href');
          if (!href) return;
          var h3 = card.querySelector('h3');
          var title = h3 ? h3.textContent.replace(/^[^\wÀ-￿]+/, '').trim() : href;
          entries.push({ url: TOPICS_ROOT + href.replace(/^\.\//, ''), title: title });
        });
        return Promise.all(entries.map(function (entry) {
          return fetch(entry.url.replace(/\/?$/, '/') + 'index.html')
            .then(function (r) { return r.text(); })
            .then(function (html) { return _indexTopicPage(entry, html); })
            .catch(function () { return []; });
        }));
      })
      .then(function (pages) {
        var idx = [].concat.apply([], pages);
        _topicsIndexCache = idx;
        try { sessionStorage.setItem('bsw_topics_idx', JSON.stringify(idx)); } catch (e) {}
        return idx;
      });
  }

  function _indexTopicPage(entry, html) {
    var parser = new DOMParser();
    var doc = parser.parseFromString(html, 'text/html');
    var sections = [];
    var sectionEls = doc.querySelectorAll('section[id], .study-section[id]');
    if (!sectionEls.length) sectionEls = doc.querySelectorAll('section');
    sectionEls.forEach(function (sec) {
      var id = sec.id || '';
      var h2 = sec.querySelector('h2');
      var heading = h2 ? h2.textContent.trim() : '';
      var textParts = [];
      sec.querySelectorAll('p, .card-body, .callout, .accordion-body, .info-box p, .tl-content p, td').forEach(function (el) {
        var t = el.textContent.replace(/\s+/g, ' ').trim();
        if (t.length > 20) textParts.push(t);
      });
      var fullText = textParts.join(' ').replace(/\s+/g, ' ').slice(0, 4000);
      if (heading || fullText.length > 40) {
        sections.push({
          topicTitle: entry.title,
          topicUrl: entry.url.replace(/\/?$/, '/'),
          sectionId: id,
          heading: heading,
          text: fullText
        });
      }
    });
    if (!sections.length) {
      var body = doc.body ? doc.body.textContent.replace(/\s+/g, ' ').slice(0, 3000) : '';
      sections.push({ topicTitle: entry.title, topicUrl: entry.url.replace(/\/?$/, '/'), sectionId: '', heading: '', text: body });
    }
    return sections;
  }

  function _topicExcerpt(text, terms, maxLen) {
    var lower = text.toLowerCase();
    var pos = lower.length;
    for (var i = 0; i < terms.length; i++) {
      var p = lower.indexOf(terms[i]);
      if (p !== -1 && p < pos) pos = p;
    }
    var start = Math.max(0, pos - 60);
    var end = Math.min(text.length, start + maxLen);
    var excerpt = (start > 0 ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '');
    var escaped = escHtml(excerpt);
    terms.forEach(function (term) {
      var re = new RegExp('(' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
      escaped = escaped.replace(re, '<mark class="search-highlight">$1</mark>');
    });
    return escaped;
  }

  function handleTopicsSearch(query) {
    var statusEl  = document.getElementById('bsw-search-status');
    var resultsEl = document.getElementById('bsw-search-results');
    if (!statusEl || !resultsEl) return;
    if (!query || query.length < 3) {
      statusEl.textContent = query.length > 0 ? 'Keep typing… (3+ characters)' : '';
      resultsEl.innerHTML = '';
      return;
    }
    statusEl.textContent = 'Indexing topic pages…';
    resultsEl.innerHTML = '';

    var gen = ++_searchGeneration;
    _buildTopicsIndex().then(function (index) {
      if (gen !== _searchGeneration) return;
      var terms = query.toLowerCase().trim().split(/\s+/).filter(Boolean);
      var matches = [];
      index.forEach(function (sec) {
        var haystack = (sec.heading + ' ' + sec.text).toLowerCase();
        var score = 0;
        terms.forEach(function (term) {
          var re = new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
          var m = haystack.match(re);
          if (m) score += m.length;
          if (sec.heading.toLowerCase().indexOf(term) !== -1) score += 5;
        });
        if (score > 0) matches.push({ sec: sec, score: score });
      });
      matches.sort(function (a, b) { return b.score - a.score; });

      if (!matches.length) {
        statusEl.textContent = 'No results in topic studies.';
        resultsEl.innerHTML = '<p class="search-page-none">No results found for “' + escHtml(query) + '” in topic studies.</p>';
        return;
      }
      statusEl.textContent = matches.length + ' result' + (matches.length === 1 ? '' : 's') + ' in topic studies';
      var html = '';
      matches.slice(0, 25).forEach(function (m) {
        var s   = m.sec;
        var url = escHtml(s.topicUrl + (s.sectionId ? '#' + s.sectionId : ''));
        var excerpt = _topicExcerpt(s.text, terms, 200);
        html +=
          '<div class="search-topic-result">' +
            '<div class="str-breadcrumb">' +
              '<a class="str-topic-link" href="' + url + '">' + escHtml(s.topicTitle) + '</a>' +
              (s.heading
                ? ' <span class="str-sep">›</span> <span class="str-heading">' + escHtml(s.heading) + '</span>'
                : '') +
            '</div>' +
            (excerpt ? '<div class="str-excerpt">' + excerpt + '</div>' : '') +
            '<a class="str-open vs-context-btn" href="' + url + '">Open ↗</a>' +
          '</div>';
      });
      resultsEl.innerHTML = html;
    }).catch(function () {
      if (gen !== _searchGeneration) return;
      statusEl.textContent = 'Could not load topic pages.';
    });
  }

  function renderStrongsResults(results, strongsId, entry, gen) {
    if (gen !== _searchGeneration) return;
    var resultsEl = document.getElementById('bsw-search-results');
    if (!resultsEl) return;

    var headerHtml = entry
      ? '<div class="strongs-def-card">' +
          '<span class="strongs-def-id">'      + escHtml(strongsId)          + '</span>' +
          (entry.lemma    ? '<span class="strongs-def-lemma">'    + escHtml(entry.lemma)    + '</span>' : '') +
          (entry.translit ? '<span class="strongs-def-translit">' + escHtml(entry.translit) + '</span>' : '') +
          (entry.gloss    ? '<span class="strongs-def-gloss">'    + escHtml(entry.gloss)    + '</span>' : '') +
        '</div>'
      : '';

    var MAX   = 200;
    var shown = results.slice(0, MAX);

    var html = headerHtml + shown.map(function (r) {
      var readHref   = READER_URL + '?ref=' + encodeURIComponent(r.bookName + ' ' + r.ch);
      var phraseHtml = r.usagePhrases.length
        ? '<div class="bsw-search-result__text strongs-usage-phrase">' +
            r.usagePhrases.map(function (p) { return '"' + escHtml(p) + '"'; }).join(', ') +
          '</div>'
        : '';
      return '<div class="bsw-search-result" role="listitem"' +
               ' data-ref="' + escHtml(r.ref) + '" tabindex="0">' +
               '<div class="bsw-search-result__ref">' +
                 escHtml(r.ref) +
                 '<a class="bsw-search-result__read" href="' + readHref + '" tabindex="-1">Read chapter</a>' +
               '</div>' +
               phraseHtml +
             '</div>';
    }).join('');

    if (results.length > MAX) {
      html += '<p class="bsw-search-more">Showing first ' + MAX + ' of ' + results.length + ' occurrences.</p>';
    }

    resultsEl.innerHTML = html;

    resultsEl.querySelectorAll('.bsw-search-result').forEach(function (el) {
      var parsed = parseRef(el.getAttribute('data-ref'));
      if (!parsed) return;
      var open = function () { closeSearch(); openModal(parsed); };
      el.addEventListener('click', open);
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
      });
    });
  }

  // ── Fuzzy matching ─────────────────────���──────────────────────────────────
  // If query is wrapped in matching " or ' quotes, returns the inner literal.
  // Otherwise returns null (unquoted query).
  function extractLiteral(q) {
    if (q.length >= 2) {
      var f = q.charAt(0), l = q.charAt(q.length - 1);
      if ((f === '"' && l === '"') || (f === "'" && l === "'")) return q.slice(1, -1);
    }
    return null;
  }

  // Match a verse against a query using exact substring matching.
  // Wrap in quotes ("…" or '…') to force an exact literal match only.
  // Unquoted multi-word queries require every word to appear as a substring.
  function fuzzyMatchVerse(text, query) {
    var tl  = text.toLowerCase();
    var ql  = query.toLowerCase().trim();
    var lit = extractLiteral(ql);
    if (lit !== null) return tl.indexOf(lit) !== -1; // quoted: only exact literal
    if (tl.indexOf(ql) !== -1) return true;           // fast path: full phrase
    // Multi-word: every word must appear as a substring
    var qWords = ql.split(/\s+/).filter(function (w) { return w.length >= 2; });
    if (qWords.length < 2) return false;
    return qWords.every(function (qw) { return tl.indexOf(qw) !== -1; });
  }

  function highlightMatch(text, query) {
    var q   = query.toLowerCase();
    var lit = extractLiteral(q);
    if (lit !== null) q = lit; // highlight the literal, not the quotes
    var lower  = text.toLowerCase();
    var result = '';
    var start  = 0;
    var idx;
    while ((idx = lower.indexOf(q, start)) !== -1) {
      result += escHtml(text.slice(start, idx));
      result += '<mark class="bsw-search__highlight">' +
                  escHtml(text.slice(idx, idx + q.length)) +
                '</mark>';
      start = idx + q.length;
    }
    return result + escHtml(text.slice(start));
  }

  // ── Wire a single [data-ref] element ─────────────────────────────────────
  function wireRefEl(el, parsed) {
    if (el.tagName === 'A') {
      el.removeAttribute('href');
      el.setAttribute('role', 'button');
      if (!el.getAttribute('tabindex')) el.setAttribute('tabindex', '0');
    }
    el.addEventListener('mouseenter', function () { scheduleShow(el, parsed); });
    el.addEventListener('mouseleave', function () { scheduleHide(); });
    el.addEventListener('focus',      function () { scheduleShow(el, parsed); });
    el.addEventListener('blur',       function () { scheduleHide(); });
    el.addEventListener('click', function (e) {
      e.preventDefault();
      cancelShow();
      hideTooltip();
      openModal(parsed);
    });
    el.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openModal(parsed);
      }
    });
  }

  // ── Wire all explicit [data-ref] elements on the page ────────────────────
  function wireRefLinks() {
    var els = document.querySelectorAll('[data-ref]');
    els.forEach(function (el) {
      var parsed = parseRef(el.dataset.ref);
      if (parsed) wireRefEl(el, parsed);
    });
  }

  // ── Auto-tag bare scripture references in text nodes ─────────────────────
  // Walks all text nodes, detects "Book Ch:V[-V2]" patterns, wraps them in
  // <a class="ref" data-ref="..."> and wires tooltip/modal on the fly.
  // Also scans for continuation refs (e.g. "; 13:4; 21:33" after "Gen 12:8").
  function autoTagRefs() {
    if (!bookLookup) return;

    var REF_RE = /\b((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+){0,3})\s+(\d+):(\d+)(?:[-–](?:(\d+):)?(\d+))?/g;
    var SKIP   = { script:1, style:1, code:1, pre:1, textarea:1, a:1, button:1, select:1, option:1, label:1 };

    var walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          var el = node.parentElement;
          if (!el) return NodeFilter.FILTER_REJECT;
          if (SKIP[el.tagName.toLowerCase()]) return NodeFilter.FILTER_REJECT;
          if (el.closest('[data-ref], .bsw-tooltip, .bsw-modal-backdrop')) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    var nodes = [];
    var n;
    while ((n = walker.nextNode())) {
      if (n.nodeValue.length > 4) nodes.push(n);
    }

    nodes.forEach(function (textNode) {
      var text = textNode.nodeValue;
      REF_RE.lastIndex = 0;
      if (!REF_RE.test(text)) return;
      REF_RE.lastIndex = 0;

      var parent = textNode.parentNode;
      var frag   = document.createDocumentFragment();
      var last   = 0;
      var m;

      while ((m = REF_RE.exec(text)) !== null) {
        var raw    = m[0].trim();
        var parsed = parseRef(raw);
        if (!parsed) continue;

        if (m.index > last) {
          frag.appendChild(document.createTextNode(text.slice(last, m.index)));
        }
        var a = document.createElement('a');
        a.className = 'ref';
        a.setAttribute('data-ref', raw);
        a.textContent = raw;
        wireRefEl(a, parsed);
        frag.appendChild(a);

        // Scan for continuation refs sharing the same book, e.g. "; 13:4; 21:33"
        var contPos = m.index + m[0].length;
        var curCh   = parsed.ch;

        for (;;) {
          var cm = text.slice(contPos).match(
            /^([,;]\s*)((?:(\d+):)?(\d+)(?:[-–](?:(\d+):)?(\d+))?)/
          );
          if (!cm) break;

          var ccCh = cm[3] ? parseInt(cm[3], 10) : curCh;
          var ccV  = parseInt(cm[4], 10);

          // Guard: if no chapter given and next chars look like a book name
          // (e.g. "2" in "2 Peter"), don't treat it as a verse continuation.
          if (!cm[3]) {
            var after = text.slice(contPos + cm[0].length);
            if (/^\s+[A-Za-z]/.test(after)) break;
          }

          var cDataRef = parsed.bookName + ' ' + ccCh + ':' + ccV;
          if (cm[6]) cDataRef += '-' + (cm[5] ? cm[5] + ':' : '') + cm[6];

          var cParsed = parseRef(cDataRef);
          if (!cParsed) break;

          frag.appendChild(document.createTextNode(cm[1]));
          var ca = document.createElement('a');
          ca.className = 'ref';
          ca.setAttribute('data-ref', cDataRef);
          ca.textContent = cm[2];
          wireRefEl(ca, cParsed);
          frag.appendChild(ca);

          if (cm[3]) curCh = ccCh;
          contPos += cm[0].length;
        }

        last = contPos;
        REF_RE.lastIndex = contPos;
      }

      if (last > 0) {
        if (last < text.length) {
          frag.appendChild(document.createTextNode(text.slice(last)));
        }
        parent.replaceChild(frag, textNode);
      }
    });

    // If the page declares a book context, tag bare ch:v refs and Ch. N refs
    var pageBook = document.body && document.body.getAttribute('data-bible-book');
    if (pageBook) {
      var pbId   = normalizeBook(pageBook);
      var pbData = pbId && metaBooks && metaBooks.find(function (b) { return b.id === pbId; });
      if (pbData) {
        autoTagBareRefs(pbData.id, pbData.name);
        autoTagBareChapters(pbData.id, pbData.name);
      }
    }
    // Tag "Book Ch" whole-chapter refs anywhere on the page (e.g. "Ps 22", "Job 3").
    autoTagChapterRefs();
  }

  // ── Auto-tag "Book Ch" whole-chapter refs in text nodes ──────────────────
  // Handles patterns like "Ps 22", "Job 3", "1 John 4" that have no verse
  // number. Runs after autoTagRefs so already-wired verse refs are skipped.
  // Also follows semicolon/comma continuations: "Ps 22; 23" → Ps 22, Ps 23.
  function autoTagChapterRefs() {
    if (!bookLookup || !metaBooks) return;

    // "Book Ch" (optional range "–N") not followed by colon/digit (which would
    // indicate a verse ref already handled by autoTagRefs).
    // Group 3 captures the end chapter when a range like "17–19" is present.
    var BOOK_CH_RE = /\b((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+){0,3})\s+(\d+)(?:\s*[-–]\s*(\d+))?(?!\s*[:\d])/g;
    var SKIP = { script:1, style:1, code:1, pre:1, textarea:1, a:1, button:1, select:1, option:1, label:1 };

    var walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          var el = node.parentElement;
          if (!el) return NodeFilter.FILTER_REJECT;
          if (SKIP[el.tagName.toLowerCase()]) return NodeFilter.FILTER_REJECT;
          if (el.closest('[data-ref], .bsw-tooltip, .bsw-modal-backdrop')) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    var nodes = [];
    var n;
    while ((n = walker.nextNode())) {
      if (n.nodeValue.length > 3) nodes.push(n);
    }

    nodes.forEach(function (textNode) {
      var text = textNode.nodeValue;
      BOOK_CH_RE.lastIndex = 0;

      // Quick pre-check: does text contain any valid book name candidate?
      var hasValid = false;
      var tm;
      while ((tm = BOOK_CH_RE.exec(text)) !== null) {
        if (normalizeBook(tm[1])) { hasValid = true; break; }
      }
      if (!hasValid) return;
      BOOK_CH_RE.lastIndex = 0;

      var parent = textNode.parentNode;
      var frag   = document.createDocumentFragment();
      var last   = 0;
      var curBookId = null, curBookName = null;
      var m;

      while ((m = BOOK_CH_RE.exec(text)) !== null) {
        var bookId = normalizeBook(m[1]);
        if (!bookId) continue;

        var bk       = metaBooks.find(function (b) { return b.id === bookId; });
        var ch       = parseInt(m[2], 10);
        var endCh    = m[3] ? parseInt(m[3], 10) : ch;
        var bookName = bk ? bk.name : m[1];
        var display  = bookName + ' ' + ch + (endCh !== ch ? '–' + endCh : '');

        var parsed = {
          bookId: bookId, bookName: bookName,
          ch: ch, v: 1, endCh: endCh, endV: 9999,
          display: display, raw: display, wholeChapter: true
        };

        if (m.index > last) {
          frag.appendChild(document.createTextNode(text.slice(last, m.index)));
        }
        var a = document.createElement('a');
        a.className = 'ref';
        a.setAttribute('data-ref', display);
        a.textContent = m[0].trim();
        wireRefEl(a, parsed);
        frag.appendChild(a);

        curBookId   = bookId;
        curBookName = bookName;
        var contPos = m.index + m[0].length;

        // Continuation: "; 23" or ", 24" → next chapter of the same book.
        for (;;) {
          var cm = text.slice(contPos).match(/^([,;]\s*)(\d+)(?!\s*[:\d])/);
          if (!cm) break;
          // Guard: digit followed by space+alpha is a book number (e.g. "1 Kings"),
          // not a chapter continuation — let the main loop handle it as a new book ref.
          if (/^\s+[A-Za-z]/.test(text.slice(contPos + cm[0].length))) break;
          var nextCh  = parseInt(cm[2], 10);
          var cDisp   = curBookName + ' ' + nextCh;
          var cParsed = {
            bookId: curBookId, bookName: curBookName,
            ch: nextCh, v: 1, endCh: nextCh, endV: 9999,
            display: cDisp, raw: cDisp, wholeChapter: true
          };
          frag.appendChild(document.createTextNode(cm[1]));
          var ca = document.createElement('a');
          ca.className = 'ref';
          ca.setAttribute('data-ref', cDisp);
          ca.textContent = cm[2];
          wireRefEl(ca, cParsed);
          frag.appendChild(ca);
          contPos += cm[0].length;
        }

        last = contPos;
        BOOK_CH_RE.lastIndex = contPos;
      }

      if (last > 0) {
        if (last < text.length) {
          frag.appendChild(document.createTextNode(text.slice(last)));
        }
        parent.replaceChild(frag, textNode);
      }
    });
  }

  // ── Tag bare "ch:v" refs using the page-level book context ───────────────
  // Called only when <body data-bible-book="BookName"> is set.
  // Handles continuations (e.g. "1:1, 1:4, 1:9, 22:8") the same way autoTagRefs does.
  function autoTagBareRefs(bookId, bookName) {
    var BARE_RE = /\b(\d+):(\d+)(?:[-–](?:(\d+):)?(\d+))?/g;
    var SKIP    = { script:1, style:1, code:1, pre:1, textarea:1, a:1, button:1, select:1, option:1, label:1 };

    var walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          var el = node.parentElement;
          if (!el) return NodeFilter.FILTER_REJECT;
          if (SKIP[el.tagName.toLowerCase()]) return NodeFilter.FILTER_REJECT;
          if (el.closest('[data-ref], .bsw-tooltip, .bsw-modal-backdrop')) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    var nodes = [];
    var n;
    while ((n = walker.nextNode())) {
      if (n.nodeValue.length > 2) nodes.push(n);
    }

    nodes.forEach(function (textNode) {
      var text = textNode.nodeValue;
      BARE_RE.lastIndex = 0;
      if (!BARE_RE.test(text)) return;
      BARE_RE.lastIndex = 0;

      var parent = textNode.parentNode;
      var frag   = document.createDocumentFragment();
      var last   = 0;
      var m;

      while ((m = BARE_RE.exec(text)) !== null) {
        var pCh = parseInt(m[1], 10);
        var pV  = parseInt(m[2], 10);

        var dataRef = bookName + ' ' + pCh + ':' + pV;
        if (m[4]) dataRef += '-' + (m[3] ? m[3] + ':' : '') + m[4];

        var parsed = parseRef(dataRef);
        if (!parsed) continue;

        if (m.index > last) {
          frag.appendChild(document.createTextNode(text.slice(last, m.index)));
        }
        var a = document.createElement('a');
        a.className = 'ref';
        a.setAttribute('data-ref', dataRef);
        a.textContent = m[0];
        wireRefEl(a, parsed);
        frag.appendChild(a);

        var contPos = m.index + m[0].length;
        var curCh   = pCh;

        for (;;) {
          var cm = text.slice(contPos).match(
            /^([,;]\s*)((?:(\d+):)?(\d+)(?:[-–](?:(\d+):)?(\d+))?)/
          );
          if (!cm) break;

          var ccCh = cm[3] ? parseInt(cm[3], 10) : curCh;
          var ccV  = parseInt(cm[4], 10);

          if (!cm[3]) {
            var after = text.slice(contPos + cm[0].length);
            if (/^\s+[A-Za-z]/.test(after)) break;
          }

          var cDataRef = bookName + ' ' + ccCh + ':' + ccV;
          if (cm[6]) cDataRef += '-' + (cm[5] ? cm[5] + ':' : '') + cm[6];

          var cParsed = parseRef(cDataRef);
          if (!cParsed) break;

          frag.appendChild(document.createTextNode(cm[1]));
          var ca = document.createElement('a');
          ca.className = 'ref';
          ca.setAttribute('data-ref', cDataRef);
          ca.textContent = cm[2];
          wireRefEl(ca, cParsed);
          frag.appendChild(ca);

          if (cm[3]) curCh = ccCh;
          contPos += cm[0].length;
        }

        last = contPos;
        BARE_RE.lastIndex = contPos;
      }

      if (last > 0) {
        if (last < text.length) {
          frag.appendChild(document.createTextNode(text.slice(last)));
        }
        parent.replaceChild(frag, textNode);
      }
    });
  }

  // ── Tag bare "Ch. N" / "ch. N–M" refs using the page-level book context ───
  // Called only when <body data-bible-book="BookName"> is set.
  // Handles "Ch. 1", "ch. 9", "Ch. 1–3", "Chap. 12" etc. and links them to
  // the whole chapter (or chapter range) in the current book.
  function autoTagBareChapters(bookId, bookName) {
    // Matches: Ch.? N, Chap.? N, ch.? N — optionally followed by –N or -N range.
    var CHAP_RE = /\b[Cc]hap?\.?\s*(\d+)(?:\s*[-–]\s*(\d+))?/g;
    var SKIP    = { script:1, style:1, code:1, pre:1, textarea:1, a:1, button:1, select:1, option:1, label:1 };

    var walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          var el = node.parentElement;
          if (!el) return NodeFilter.FILTER_REJECT;
          if (SKIP[el.tagName.toLowerCase()]) return NodeFilter.FILTER_REJECT;
          if (el.closest('[data-ref], .bsw-tooltip, .bsw-modal-backdrop')) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    var nodes = [];
    var n;
    while ((n = walker.nextNode())) {
      if (n.nodeValue.length > 2) nodes.push(n);
    }

    nodes.forEach(function (textNode) {
      var text = textNode.nodeValue;
      CHAP_RE.lastIndex = 0;
      if (!CHAP_RE.test(text)) return;
      CHAP_RE.lastIndex = 0;

      var parent = textNode.parentNode;
      var frag   = document.createDocumentFragment();
      var last   = 0;
      var m;

      while ((m = CHAP_RE.exec(text)) !== null) {
        var startCh = parseInt(m[1], 10);
        var endCh   = m[2] ? parseInt(m[2], 10) : startCh;
        var display = bookName + ' ' + startCh + (endCh !== startCh ? '–' + endCh : '');
        var dataRef = bookName + ' ' + startCh + (endCh !== startCh ? '–' + endCh : '');

        var parsed = {
          bookId:      bookId,
          bookName:    bookName,
          ch:          startCh,
          v:           1,
          endCh:       endCh,
          endV:        9999,
          display:     display,
          raw:         dataRef,
          wholeChapter: true
        };

        if (m.index > last) {
          frag.appendChild(document.createTextNode(text.slice(last, m.index)));
        }
        var a = document.createElement('a');
        a.className = 'ref';
        a.setAttribute('data-ref', dataRef);
        a.textContent = m[0];
        wireRefEl(a, parsed);
        frag.appendChild(a);
        last = m.index + m[0].length;
      }

      if (last > 0) {
        if (last < text.length) {
          frag.appendChild(document.createTextNode(text.slice(last)));
        }
        parent.replaceChild(frag, textNode);
      }
    });
  }

  // ── Auto-updating inline verse elements (.bsw-verse[data-ref]) ───────────
  // Any element with class="bsw-verse" and data-ref="Book Ch:V" will have its
  // content replaced with the verse text in the current version and will update
  // live whenever the version picker changes.
  function wireInlineVerses() {
    var els = document.querySelectorAll('.bsw-verse[data-ref]');
    if (!els.length) return;
    var version = getVersion();
    els.forEach(function (el) { populateInlineVerse(el, version); });
  }

  function populateInlineVerse(el, versionId) {
    var parsed = parseRef(el.getAttribute('data-ref'));
    if (!parsed) return;

    el.classList.add('bsw-verse--loading');
    resolveVerses(parsed, versionId).then(function (verses) {
      el.classList.remove('bsw-verse--loading');
      if (!verses || !verses.length) return;
      el.innerHTML = verses.map(function (vr) {
        return '<sup class="bsw-verse__num">' + vr.verse + '</sup>' +
               '<span class="bsw-verse__text">' + escHtml(vr.text) + '</span>';
      }).join(' ');
    }).catch(function () {
      el.classList.remove('bsw-verse--loading');
    });
  }

  function updateInlineVerses(versionId) {
    document.querySelectorAll('.bsw-verse[data-ref]').forEach(function (el) {
      populateInlineVerse(el, versionId);
    });
  }

  // ── Utility ───────────────────────────────────────────────────────────────
  function escHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // ── Compare (side-by-side translation) ───────────────────────────────────

  function isCompareEnabled() { return !!localStorage.getItem(COMPARE_KEY); }
  function getCompareVersion() { return localStorage.getItem(COMPARE_KEY) || ''; }
  function setCompareVersion(id) { localStorage.setItem(COMPARE_KEY, id || ''); }

  function initCompareToggle() {
    var browseBar = document.querySelector('.reader-browse-bar');
    if (!browseBar || document.getElementById('reader-compare-btn')) return;

    var btn = document.createElement('button');
    btn.id = 'reader-compare-btn';
    btn.className = 'reader-compare-btn' + (isCompareEnabled() ? ' reader-compare-btn--on' : '');
    btn.setAttribute('aria-pressed', isCompareEnabled() ? 'true' : 'false');
    btn.title = 'Compare translations side by side';
    btn.textContent = '⇅ Compare';

    // Insert before the parallels button or the hint span
    var parallelsBtn = document.getElementById('reader-parallels-btn');
    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, parallelsBtn || hint || null);

    btn.addEventListener('click', function () {
      var on = !isCompareEnabled();
      if (on) {
        // Pick a default secondary version different from primary
        var primary = getVersion();
        var def = null;
        if (metaVersions) {
          for (var i = 0; i < metaVersions.length; i++) {
            if (metaVersions[i].id !== primary) { def = metaVersions[i].id; break; }
          }
        }
        setCompareVersion(def || 'KJV');
      } else {
        setCompareVersion('');
      }
      btn.classList.toggle('reader-compare-btn--on', on);
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      if (_readerLookupFn) _readerLookupFn();
    });
  }

  function injectComparePanel(groups, cmpVer, resultsEl) {
    var primaryVer = getVersion();
    var domGroups  = resultsEl.querySelectorAll('.reader-result-group');

    domGroups.forEach(function (groupEl, gIdx) {
      var g = groups[gIdx];
      if (!g) return;

      var textEl = groupEl.querySelector('.reader-result-group__text');
      var attrEl = groupEl.querySelector('.reader-result-group__attr');
      // Fall back to any hint paragraph when no verse text (error state)
      var hintEl = !textEl ? groupEl.querySelector('.reader-hint') : null;
      var contentEl = textEl || hintEl;
      if (!contentEl) return;

      // ── Build compare wrap ──────────────────────────────
      var wrap = document.createElement('div');
      wrap.className = 'reader-compare-wrap';

      // Primary panel
      var p1 = document.createElement('div');
      p1.className = 'reader-compare-panel';
      p1.appendChild(_buildComparePanelHdr(primaryVer, 'primary'));
      // Move existing content nodes into primary panel
      contentEl.parentNode.removeChild(contentEl);
      p1.appendChild(contentEl);
      if (attrEl && attrEl.parentNode) {
        attrEl.parentNode.removeChild(attrEl);
        p1.appendChild(attrEl);
      }

      // Secondary panel (content loaded async)
      var p2 = document.createElement('div');
      p2.className = 'reader-compare-panel';
      p2.appendChild(_buildComparePanelHdr(cmpVer, 'secondary'));
      var p2body = document.createElement('div');
      p2body.innerHTML = '<p class="reader-hint">Loading…</p>';
      p2.appendChild(p2body);

      wrap.appendChild(p1);
      wrap.appendChild(p2);

      // Insert before bottom nav if present, otherwise append
      var bottomNav = groupEl.querySelector('.reader-chapter-nav--bottom');
      if (bottomNav) groupEl.insertBefore(wrap, bottomNav);
      else groupEl.appendChild(wrap);

      // ── Fetch secondary version ─────────────────────────
      resolveVerses(g.ref, cmpVer).then(function (verses) {
        if (!verses || !verses.length) {
          p2body.innerHTML = '<p class="reader-hint">Not available in ' +
            escHtml(cmpVer) + '.</p>';
          return;
        }
        var html = '<p class="reader-result-group__text">';
        verses.forEach(function (vObj) {
          html += '<span class="reader-verse" data-ch="' + vObj.chapter +
            '" data-v="' + vObj.verse + '">' +
            '<sup class="reader-verse__num">' + vObj.verse + '</sup>' +
            escHtml(vObj.text) + '</span> ';
        });
        html += '</p>';
        var attr = ATTRIBUTION[cmpVer];
        if (attr) html += '<p class="reader-result-group__attr">' + escHtml(attr) + '</p>';
        p2body.innerHTML = html;
      }).catch(function () {
        p2body.innerHTML = '<p class="reader-hint">Could not load ' +
          escHtml(cmpVer) + '.</p>';
      });
    });
  }

  function _buildComparePanelHdr(versionId, role) {
    var hdr = document.createElement('div');
    hdr.className = 'reader-compare-panel__hdr';

    var lbl = document.createElement('span');
    lbl.className = 'reader-compare-panel__label';
    lbl.textContent = role === 'primary' ? 'A:' : 'B:';

    var sel = document.createElement('select');
    sel.className = 'reader-compare-ver-sel';
    sel.setAttribute('aria-label', role === 'primary' ? 'Primary version' : 'Comparison version');

    if (metaVersions) {
      metaVersions.forEach(function (mv) {
        var opt = document.createElement('option');
        opt.value = mv.id;
        opt.textContent = mv.id;
        opt.title = mv.name;
        if (mv.id === versionId) opt.selected = true;
        sel.appendChild(opt);
      });
    }

    sel.addEventListener('change', function () {
      if (role === 'primary') {
        setVersion(sel.value); // triggers re-render via setVersion
      } else {
        setCompareVersion(sel.value);
        if (_readerLookupFn) _readerLookupFn();
      }
    });

    hdr.appendChild(lbl);
    hdr.appendChild(sel);
    return hdr;
  }

  // ── Interlinear Reader ────────────────────────────────────────────────────

  var INTERLINEAR_KEY = 'bsw_interlinear';
  var _riPopoverEl    = null;
  var _riActiveTile   = null;

  function getInterlinearEnabled() {
    return localStorage.getItem(INTERLINEAR_KEY) === '1';
  }
  function setInterlinearEnabled(on) {
    localStorage.setItem(INTERLINEAR_KEY, on ? '1' : '0');
  }

  var SPLIT_KEY   = 'bsw_split_panel';
  var WIDE_KEY    = 'bsw_wide_reader';
  var SIDEBAR_KEY = 'bsw_sidebar_chapters';

  function initSplitToggle() {
    var browseBar = document.querySelector('.reader-browse-bar');
    if (!browseBar || document.getElementById('reader-split-btn')) return;

    var layout = document.querySelector('.reader-layout');
    var on = !!localStorage.getItem(SPLIT_KEY);
    if (on && layout) layout.classList.add('reader-layout--split');

    var btn = document.createElement('button');
    btn.id = 'reader-split-btn';
    btn.className = 'reader-split-btn' + (on ? ' reader-split-btn--on' : '');
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.title = 'Toggle 50/50 text / panel split';
    btn.textContent = '⇔ Split';

    var interlinearBtn = document.getElementById('reader-interlinear-btn');
    var compareBtn     = document.getElementById('reader-compare-btn');
    var parallelsBtn   = document.getElementById('reader-parallels-btn');
    var hint           = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, interlinearBtn || compareBtn || parallelsBtn || hint || null);

    btn.addEventListener('click', function () {
      on = !on;
      if (on) {
        localStorage.setItem(SPLIT_KEY, '1');
        // deactivate Wide if on
        var wideBtn = document.getElementById('reader-wide-btn');
        if (wideBtn && wideBtn.classList.contains('reader-wide-btn--on')) wideBtn.click();
      } else {
        localStorage.removeItem(SPLIT_KEY);
      }
      if (layout) layout.classList.toggle('reader-layout--split', on);
      btn.classList.toggle('reader-split-btn--on', on);
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }

  function initWideToggle() {
    var browseBar = document.querySelector('.reader-browse-bar');
    if (!browseBar || document.getElementById('reader-wide-btn')) return;

    var layout = document.querySelector('.reader-layout');
    var on = !!localStorage.getItem(WIDE_KEY);
    if (on && layout) layout.classList.add('reader-layout--wide');

    var btn = document.createElement('button');
    btn.id = 'reader-wide-btn';
    btn.className = 'reader-wide-btn' + (on ? ' reader-wide-btn--on' : '');
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.title = 'Hide panel for distraction-free reading';
    btn.textContent = '⛶ Wide';

    var splitBtn       = document.getElementById('reader-split-btn');
    var interlinearBtn = document.getElementById('reader-interlinear-btn');
    var compareBtn     = document.getElementById('reader-compare-btn');
    var parallelsBtn   = document.getElementById('reader-parallels-btn');
    var hint           = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, splitBtn || interlinearBtn || compareBtn || parallelsBtn || hint || null);

    btn.addEventListener('click', function () {
      on = !on;
      if (on) {
        localStorage.setItem(WIDE_KEY, '1');
        // deactivate Split if on
        var splitBtn2 = document.getElementById('reader-split-btn');
        if (splitBtn2 && splitBtn2.classList.contains('reader-split-btn--on')) splitBtn2.click();
      } else {
        localStorage.removeItem(WIDE_KEY);
      }
      if (layout) layout.classList.toggle('reader-layout--wide', on);
      btn.classList.toggle('reader-wide-btn--on', on);
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }

  function initSidebarToggle() {
    var browseBar = document.querySelector('.reader-browse-bar');
    if (!browseBar || document.getElementById('reader-sidebar-btn')) return;
    var layout  = document.querySelector('.reader-layout');
    var on = !!localStorage.getItem(SIDEBAR_KEY);
    if (on && layout) layout.classList.add('reader-layout--with-sidebar');

    var btn = document.createElement('button');
    btn.id = 'reader-sidebar-btn';
    btn.className = 'reader-sidebar-btn' + (on ? ' reader-sidebar-btn--on' : '');
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.title = 'Show chapter list';
    btn.textContent = '≡ Chapters';

    var wideBtn        = document.getElementById('reader-wide-btn');
    var splitBtn       = document.getElementById('reader-split-btn');
    var interlinearBtn = document.getElementById('reader-interlinear-btn');
    var compareBtn     = document.getElementById('reader-compare-btn');
    var parallelsBtn   = document.getElementById('reader-parallels-btn');
    var hint           = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, wideBtn || splitBtn || interlinearBtn || compareBtn || parallelsBtn || hint || null);

    btn.addEventListener('click', function () {
      on = !on;
      if (on) {
        localStorage.setItem(SIDEBAR_KEY, '1');
        if (layout) layout.classList.add('reader-layout--with-sidebar');
        if (_readerNavState) renderReaderSidebar(_readerNavState.bookId, _readerNavState.ch);
      } else {
        localStorage.removeItem(SIDEBAR_KEY);
        if (layout) layout.classList.remove('reader-layout--with-sidebar');
      }
      btn.classList.toggle('reader-sidebar-btn--on', on);
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }

  function initInterlinearToggle() {
    var browseBar = document.querySelector('.reader-browse-bar');
    if (!browseBar || document.getElementById('reader-interlinear-btn')) return;

    var btn = document.createElement('button');
    btn.id = 'reader-interlinear-btn';
    btn.className = 'reader-interlinear-btn' + (getInterlinearEnabled() ? ' reader-interlinear-btn--on' : '');
    btn.setAttribute('aria-pressed', getInterlinearEnabled() ? 'true' : 'false');
    btn.title = 'Show Greek/Hebrew interlinear below each verse';
    btn.textContent = '⊞ Interlinear';

    var compareBtn = document.getElementById('reader-compare-btn');
    var parallelsBtn = document.getElementById('reader-parallels-btn');
    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, compareBtn || parallelsBtn || hint || null);

    btn.addEventListener('click', function () {
      var on = !getInterlinearEnabled();
      setInterlinearEnabled(on);
      btn.classList.toggle('reader-interlinear-btn--on', on);
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');

      // Re-render so the block vs inline verse layout switches
      if (_readerNavState) {
        var chRef = _readerNavState.bookName + ' ' + _readerNavState.ch;
        var lookupInput = document.getElementById('reader-lookup-input');
        if (lookupInput) lookupInput.value = chRef;
      }
      if (_readerLookupFn) _readerLookupFn();
    });
  }

  // ── Book Info toggle ──────────────────────────────────────────────────────
  var _bookInfoOpen = false;
  var _bookInfoCache = {};

  function initBookInfoToggle() {
    var browseBar = document.querySelector('.reader-browse-bar');
    if (!browseBar || document.getElementById('reader-bookinfo-btn')) return;

    var btn = document.createElement('button');
    btn.id = 'reader-bookinfo-btn';
    btn.className = 'reader-bookinfo-btn';
    btn.setAttribute('aria-pressed', 'false');
    btn.title = 'Book introduction — author, date, outline';
    btn.textContent = '📖 Book Info';

    var interlinearBtn = document.getElementById('reader-interlinear-btn');
    var compareBtn     = document.getElementById('reader-compare-btn');
    var parallelsBtn   = document.getElementById('reader-parallels-btn');
    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, interlinearBtn || compareBtn || parallelsBtn || hint || null);

    btn.addEventListener('click', function () {
      _bookInfoOpen = !_bookInfoOpen;
      btn.classList.toggle('reader-bookinfo-btn--on', _bookInfoOpen);
      btn.setAttribute('aria-pressed', _bookInfoOpen ? 'true' : 'false');
      _refreshBookInfoPanel();
    });
  }

  function _refreshBookInfoPanel() {
    var container = document.getElementById('reader-results');
    if (!container) return;
    var existing = document.getElementById('reader-bookinfo-panel');
    if (!_bookInfoOpen) {
      if (existing) existing.remove();
      return;
    }

    var bookId = _readerNavState && _readerNavState.bookId;
    if (!bookId) {
      if (existing) existing.remove();
      return;
    }

    if (!existing) {
      existing = document.createElement('div');
      existing.id = 'reader-bookinfo-panel';
      existing.className = 'reader-bookinfo-panel';
      container.parentNode.insertBefore(existing, container);
    }
    existing.innerHTML = '<div class="reader-bookinfo-loading">Loading…</div>';

    if (_bookInfoCache[bookId]) {
      _renderBookInfoContent(existing, _bookInfoCache[bookId]);
      return;
    }

    var url = _resolve('../../data/books/introductions/' + bookId + '.json');
    fetch(url)
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (data) {
        _bookInfoCache[bookId] = data;
        if (_bookInfoOpen && _readerNavState && _readerNavState.bookId === bookId) {
          _renderBookInfoContent(existing, data);
        }
      })
      .catch(function () {
        if (existing.parentNode) {
          existing.innerHTML = '<p class="reader-bookinfo-empty">No introduction available for this book yet.</p>';
        }
      });
  }

  function _renderBookInfoContent(panel, d) {
    var outlineHtml = '';
    if (d.outline && d.outline.length) {
      outlineHtml = '<ol class="reader-bookinfo-outline">' +
        d.outline.map(function (s) {
          var link = s.ref
            ? '<a class="ref" data-ref="' + escHtml(s.ref) + '">' + escHtml(s.label) + '</a>'
            : escHtml(s.label);
          return '<li>' + link +
            (s.chapters ? ' <span class="reader-bookinfo-ch">ch. ' + escHtml(s.chapters) + '</span>' : '') +
            '</li>';
        }).join('') + '</ol>';
    }

    var themesHtml = '';
    if (d.themes && d.themes.length) {
      themesHtml = '<div class="reader-bookinfo-themes">' +
        d.themes.map(function (t) {
          return '<span class="reader-bookinfo-theme">' + escHtml(t) + '</span>';
        }).join('') + '</div>';
    }

    var timelineHtml = '';
    if (d.timeline) {
      var tl = d.timeline;
      var parts = [];
      if (tl.before && tl.before.length) {
        parts.push(tl.before.map(function (b) {
          return '<a class="ref" data-ref="' + escHtml(b.ref) + '">← ' + escHtml(b.label) + '</a>';
        }).join(''));
      }
      parts.push('<strong>' + escHtml(d.title) + '</strong>' +
        (tl.date ? ' <span class="reader-bookinfo-tldate">(' + escHtml(tl.date) + ')</span>' : ''));
      if (tl.after && tl.after.length) {
        parts.push(tl.after.map(function (a) {
          return '<a class="ref" data-ref="' + escHtml(a.ref) + '">' + escHtml(a.label) + ' →</a>';
        }).join(''));
      }
      timelineHtml = '<div class="reader-bookinfo-timeline">' + parts.join(' · ') + '</div>';
    }

    panel.innerHTML =
      '<div class="reader-bookinfo-inner">' +
        '<div class="reader-bookinfo-header">' +
          '<h3 class="reader-bookinfo-title">' + escHtml(d.title) + '</h3>' +
          '<button class="reader-bookinfo-close" aria-label="Close book info">✕</button>' +
        '</div>' +
        '<div class="reader-bookinfo-meta">' +
          '<span><strong>Author:</strong> ' + escHtml(d.author || '—') + '</span>' +
          '<span><strong>Date:</strong> ' + escHtml(d.date || '—') + '</span>' +
        '</div>' +
        '<p class="reader-bookinfo-purpose">' + escHtml(d.purpose || d.setting || '') + '</p>' +
        themesHtml +
        (outlineHtml ? '<h4 class="reader-bookinfo-subhead">Outline</h4>' + outlineHtml : '') +
        timelineHtml +
      '</div>';

    wireRefLinks(panel);

    panel.querySelector('.reader-bookinfo-close').addEventListener('click', function () {
      _bookInfoOpen = false;
      var btn = document.getElementById('reader-bookinfo-btn');
      if (btn) { btn.classList.remove('reader-bookinfo-btn--on'); btn.setAttribute('aria-pressed', 'false'); }
      panel.remove();
    });
  }

  function injectAllInterlinearRows(ref, groupEl) {
    if (!groupEl) return;
    var bkMeta = metaBooks && metaBooks.find(function (b) { return b.id === ref.bookId; });
    var testament = (bkMeta && bkMeta.testament === 'NT') ? 'greek' : 'hebrew';
    Promise.all([loadInterlinear(ref.bookId), loadStrongs(testament)])
      .then(function (results) {
        var interlinear = results[0];
        var strongsDict = results[1];
        if (!interlinear) return;
        var rows = groupEl.querySelectorAll('.reader-interlinear-row');
        rows.forEach(function (rowEl) {
          var ch = rowEl.getAttribute('data-ch');
          var v  = rowEl.getAttribute('data-v');
          var vTokens = interlinear[ch] && interlinear[ch][v];
          if (!vTokens || !vTokens.length) { rowEl.style.display = 'none'; return; }
          renderReaderInterlinearRow(vTokens, strongsDict, rowEl, testament === 'hebrew');
        });
      });
  }

  function renderReaderInterlinearRow(vTokens, strongsDict, container, isHebrew) {
    var valid = vTokens.filter(function (t) { return t.s; });
    if (!valid.length) { container.style.display = 'none'; return; }

    var grid = document.createElement('div');
    grid.className = isHebrew ? 'ri-grid ri-grid--rtl' : 'ri-grid';

    valid.forEach(function (tok) {
      var entry = strongsDict && strongsDict[tok.s];
      var tile  = document.createElement('button');
      tile.type = 'button';
      tile.className = 'ri-tile';

      tile.innerHTML =
        (entry && entry.lemma
          ? '<div class="ri-tile__lemma">' + escHtml(entry.lemma) + '</div>' +
            (entry.translit ? '<div class="ri-tile__translit">' + escHtml(entry.translit) + '</div>' : '')
          : '<div class="ri-tile__lemma ri-tile__lemma--none">—</div>') +
        '<div class="ri-tile__eng">' + escHtml(tok.text || '') + '</div>' +
        '<div class="ri-tile__s">' + escHtml(tok.s) + '</div>';

      (function (t, e) {
        tile.addEventListener('click', function () { _riShowPopover(t, e, tile); });
      }(tok, entry));

      grid.appendChild(tile);
    });

    container.appendChild(grid);
  }

  function _riShowPopover(tok, entry, tileEl) {
    if (_riActiveTile === tileEl && _riPopoverEl && !_riPopoverEl.hasAttribute('hidden')) {
      _riPopoverEl.setAttribute('hidden', '');
      tileEl.classList.remove('ri-tile--active');
      _riActiveTile = null;
      return;
    }
    if (_riActiveTile) _riActiveTile.classList.remove('ri-tile--active');
    _riActiveTile = tileEl;
    tileEl.classList.add('ri-tile--active');

    if (!_riPopoverEl) {
      _riPopoverEl = document.createElement('div');
      _riPopoverEl.className = 'ri-popover';
      _riPopoverEl.setAttribute('hidden', '');
      document.body.appendChild(_riPopoverEl);
      document.addEventListener('click', function (e) {
        if (!_riPopoverEl || _riPopoverEl.hasAttribute('hidden')) return;
        if (!_riPopoverEl.contains(e.target) && !e.target.closest('.ri-tile')) {
          _riPopoverEl.setAttribute('hidden', '');
          if (_riActiveTile) { _riActiveTile.classList.remove('ri-tile--active'); _riActiveTile = null; }
        }
      }, true);
    }

    var html = '<button class="ri-popover__close" aria-label="Close">✕</button>';
    // Header: English gloss + Strong's number
    html += '<div class="ri-popover__header">';
    if (tok.text) html += '<span class="ri-popover__eng">' + escHtml(tok.text) + '</span>';
    if (tok.s)    html += '<span class="ri-popover__s">'   + escHtml(tok.s)    + '</span>';
    html += '</div>';
    if (entry) {
      if (entry.lemma) {
        html += '<div class="ri-popover__orig">';
        html += '<span class="ri-popover__lemma">' + escHtml(entry.lemma) + '</span>';
        if (entry.translit) html += '<span class="ri-popover__translit">' + escHtml(entry.translit) + '</span>';
        html += '</div>';
      }
      if (entry.gloss)   html += '<div class="ri-popover__gloss">'   + escHtml(entry.gloss)   + '</div>';
      if (entry.def && entry.def !== entry.gloss) {
        var d = entry.def.length > 260 ? entry.def.slice(0, 260) + '…' : entry.def;
        html += '<div class="ri-popover__def">' + escHtml(d) + '</div>';
      }
      if (entry.deriv)   html += '<div class="ri-popover__deriv">'   + escHtml(entry.deriv)   + '</div>';
    } else if (tok.s) {
      html += '<div class="ri-popover__no-entry">No dictionary entry for ' + escHtml(tok.s) + '.</div>';
    }
    if (tok.s) {
      html += '<div class="ri-popover__links">' +
        '<a class="vs-context-btn" href="' + escHtml(SEARCH_URL + '?s=' + encodeURIComponent(tok.s)) + '">All verses with ' + escHtml(tok.s) + '</a>' +
        '<a class="vs-context-btn" href="' + escHtml(WORD_URL   + '?s=' + encodeURIComponent(tok.s)) + '">Word Deep Dive</a>' +
        '</div>';
    }
    _riPopoverEl.innerHTML = html;
    _riPopoverEl.removeAttribute('hidden');

    // Position fixed (viewport-relative) below the tile
    var rect = tileEl.getBoundingClientRect();
    var left = Math.min(rect.left, window.innerWidth - 290);
    _riPopoverEl.style.left = Math.max(6, left) + 'px';
    _riPopoverEl.style.top  = (rect.bottom + 6) + 'px';

    var closeBtn = _riPopoverEl.querySelector('.ri-popover__close');
    if (closeBtn) closeBtn.addEventListener('click', function () {
      _riPopoverEl.setAttribute('hidden', '');
      if (_riActiveTile) { _riActiveTile.classList.remove('ri-tile--active'); _riActiveTile = null; }
    });
  }

  // ── Verse Study Page ──────────────────────────────────────────────────────

  function initVerseStudyPage() {
    var params = new URLSearchParams(window.location.search);
    var refStr = params.get('ref') || '';
    var vOverride = params.get('v') || '';
    if (vOverride && metaVersions && metaVersions.find(function (mv) { return mv.id === vOverride; })) {
      localStorage.setItem(STORAGE_KEY, vOverride);
    }

    var focalEl = document.getElementById('vs-focal-text');
    if (!refStr) {
      if (focalEl) focalEl.textContent = 'No verse specified. Try: ?ref=John+3:16';
      return;
    }

    var parsed = parseRef(refStr);
    if (!parsed) {
      if (focalEl) focalEl.textContent = 'Could not parse reference: ' + refStr;
      return;
    }

    document.title = parsed.display + ' — Verse Study — Bible Study';

    // Update header ref and back link
    var headerRef = document.getElementById('vs-header-ref');
    if (headerRef) headerRef.textContent = parsed.display;

    var backLink = document.getElementById('vs-back-link');
    if (backLink) {
      backLink.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch);
      backLink.textContent = '← ' + parsed.bookName + ' ' + parsed.ch + ' in Reader';
    }

    // Context toggle
    var CTX_KEY = 'bsw_dissect_ctx';
    var ctxOn = localStorage.getItem(CTX_KEY) !== '0';
    var ctxToggle = document.getElementById('vs-context-toggle');

    function applyCtx(on) {
      var prev = document.getElementById('vs-context-prev');
      var next = document.getElementById('vs-context-next');
      if (prev) { if (on) prev.removeAttribute('hidden'); else prev.setAttribute('hidden', ''); }
      if (next) { if (on) next.removeAttribute('hidden'); else next.setAttribute('hidden', ''); }
      if (ctxToggle) {
        ctxToggle.classList.toggle('vs-context-btn--on', on);
        ctxToggle.setAttribute('aria-pressed', on ? 'true' : 'false');
      }
    }

    if (ctxToggle) {
      ctxToggle.addEventListener('click', function () {
        ctxOn = !ctxOn;
        localStorage.setItem(CTX_KEY, ctxOn ? '1' : '0');
        applyCtx(ctxOn);
      });
    }

    // Memory button on verse study page (only for single-verse refs)
    var vsMemBtn = document.getElementById('vs-memory-btn');
    if (vsMemBtn && parsed.v) {
      var vsMemRef = parsed.bookName + ' ' + parsed.ch + ':' + parsed.v;
      function _vsUpdateMemBtn() {
        var has = _memHas(vsMemRef);
        vsMemBtn.textContent = has ? '⭐ Memorizing' : '☆ Memorize';
        vsMemBtn.classList.toggle('vs-context-btn--on', has);
      }
      _vsUpdateMemBtn();
      vsMemBtn.addEventListener('click', function () {
        if (_memHas(vsMemRef)) _memRemove(vsMemRef); else _memAdd(vsMemRef);
        _vsUpdateMemBtn();
      });
    } else if (vsMemBtn) {
      vsMemBtn.setAttribute('hidden', '');
    }

    // Hook version changes to re-render verse text
    _verseStudyUpdateFn = function (versionId) {
      loadVerseStudyVerse(parsed, versionId);
    };

    // Mobile section nav wiring
    var mobileSelect = document.getElementById('vs-section-select');
    if (mobileSelect) {
      mobileSelect.addEventListener('change', function () {
        if (!this.value) return;
        var target = document.getElementById(this.value);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        this.value = '';
      });
    }

    // Load verse content, then sections
    loadVerseStudyVerse(parsed, getVersion()).then(function () { applyCtx(ctxOn); });
    loadVerseSections(parsed);
  }

  function loadVerseStudyVerse(parsed, versionId) {
    var focalTextEl = document.getElementById('vs-focal-text');
    var focalNumEl  = document.getElementById('vs-focal-num');
    var prevEl      = document.getElementById('vs-context-prev');
    var nextEl      = document.getElementById('vs-context-next');
    var tokenRow    = document.getElementById('vs-token-row');

    if (focalTextEl) focalTextEl.textContent = 'Loading…';

    return loadBook(versionId, parsed.bookId).then(function (chapters) {
      if (!chapters) {
        if (focalTextEl) focalTextEl.textContent = 'Not available in ' + versionId + '.';
        return;
      }
      var chData = chapters[String(parsed.ch)];
      if (!chData) {
        if (focalTextEl) focalTextEl.textContent = 'Chapter not found.';
        return;
      }
      var text = chData[String(parsed.v)];
      if (!text) {
        if (focalTextEl) focalTextEl.textContent = 'Verse not found.';
        return;
      }

      if (focalNumEl) focalNumEl.textContent = parsed.v;
      if (focalTextEl) {
        focalTextEl.textContent = text;
        if (_termMap2) { focalTextEl._termsTagged = false; autoTagTerms(focalTextEl); }
      }

      // Previous verse (same chapter)
      if (prevEl) {
        var pv = parsed.v - 1;
        var pvText = pv >= 1 ? chData[String(pv)] : null;
        if (pvText) {
          prevEl.innerHTML = '<sup class="vs-ctx-num">' + pv + '</sup>' +
            '<span class="vs-ctx-text">' + escHtml(pvText) + '</span>';
        } else {
          prevEl.innerHTML = '';
        }
      }

      // Next verse (same chapter)
      if (nextEl) {
        var nv = parsed.v + 1;
        var nvText = chData[String(nv)];
        if (nvText) {
          nextEl.innerHTML = '<sup class="vs-ctx-num">' + nv + '</sup>' +
            '<span class="vs-ctx-text">' + escHtml(nvText) + '</span>';
        } else {
          nextEl.innerHTML = '';
        }
      }

      // Word token row
      _vsCurrentRef = parsed;
      if (tokenRow) vsRenderTokenRow(text, tokenRow);

      // Update header height CSS variable for scroll-margin calculations
      var header = document.getElementById('vs-sticky-header');
      if (header) {
        document.documentElement.style.setProperty('--vs-header-h', header.offsetHeight + 'px');
      }
    }).catch(function () {
      if (focalTextEl) focalTextEl.textContent = 'Could not load verse.';
    });
  }

  // ── Word token row ────────────────────────────────────────────────────────

  function vsTokenizeVerse(text) {
    var tokens = [];
    var parts = text.split(/(\s+)/);
    parts.forEach(function (part) {
      if (!part) return;
      if (/^\s+$/.test(part)) {
        tokens.push({ type: 'space', text: ' ' });
        return;
      }
      var m = part.match(/^([^A-Za-z0-9]*)([A-Za-z0-9'''’-]+)([^A-Za-z0-9]*)$/);
      if (m) {
        if (m[1]) tokens.push({ type: 'punct', text: m[1] });
        tokens.push({ type: 'word', text: m[2] });
        if (m[3]) tokens.push({ type: 'punct', text: m[3] });
      } else {
        tokens.push({ type: 'punct', text: part });
      }
    });
    return tokens.filter(function (t) { return t.text; });
  }

  function vsRenderTokenRow(text, container) {
    container.innerHTML = '';
    var tokens = vsTokenizeVerse(text);
    tokens.forEach(function (tok) {
      if (tok.type === 'word') {
        var btn = document.createElement('button');
        btn.className = 'vs-token';
        btn.textContent = tok.text;
        btn.setAttribute('aria-label', tok.text);
        (function (wordText) {
          btn.addEventListener('click', function () { vsOpenWordStudy(btn, wordText); });
        }(tok.text));
        container.appendChild(btn);
      } else if (tok.type === 'space') {
        container.appendChild(document.createTextNode(' '));
      } else {
        var span = document.createElement('span');
        span.className = 'vs-token-punct';
        span.textContent = tok.text;
        container.appendChild(span);
      }
    });
  }

  var _vsActiveToken  = null;
  var _vsWordPanelEl  = null;
  var _wdCurrentFilter = null; // active translation phrase filter on word page
  var _wdCurrentBook   = null; // active book id filter on word page
  var _wdBookList      = null; // full unfiltered book list, set on init

  // ── Strong's data loaders ─────────────────────────────────────────────────

  function loadStrongs(testament) {
    if (strongsCache[testament]) return Promise.resolve(strongsCache[testament]);
    return fetch(STRONGS_ROOT + '/' + testament + '.json')
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { strongsCache[testament] = d; return d; })
      .catch(function () { strongsCache[testament] = null; return null; });
  }

  function loadInterlinear(bookId) {
    if (bookId in interlinearCache) return Promise.resolve(interlinearCache[bookId]);
    return fetch(INTERLINEAR_ROOT + '/' + bookId + '.json')
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { interlinearCache[bookId] = d; return d; })
      .catch(function () { interlinearCache[bookId] = null; return null; });
  }

  function _vsTestament(parsed) {
    var bk = metaBooks && metaBooks.find(function (b) { return b.id === parsed.bookId; });
    return (bk && bk.testament === 'NT') ? 'greek' : 'hebrew';
  }

  // Match a clicked English word against the interlinear token list for the verse.
  // Returns the first matching token {s, text} or null.
  function _vsMatchToken(verseTokens, wordText) {
    if (!verseTokens || !verseTokens.length) return null;
    var norm = wordText.toLowerCase().replace(/[^a-z]/g, '');

    // Pass 1: exact match on the token text
    for (var i = 0; i < verseTokens.length; i++) {
      var t   = verseTokens[i];
      var tkn = (t.text || '').toLowerCase().replace(/[^a-z]/g, '');
      if (tkn === norm) return t;
    }
    // Pass 2: clicked word appears inside a multi-word token ("he gave" contains "gave")
    for (var j = 0; j < verseTokens.length; j++) {
      var t2  = verseTokens[j];
      var tkn2 = (t2.text || '').toLowerCase().replace(/[^a-z]/g, '');
      if (tkn2 && tkn2.indexOf(norm) !== -1) return t2;
    }
    // Pass 3: token is a single word and clicked word starts with it (prefix)
    for (var k = 0; k < verseTokens.length; k++) {
      var t3   = verseTokens[k];
      var tkn3 = (t3.text || '').toLowerCase().replace(/[^a-z]/g, '');
      if (tkn3 && tkn3.indexOf(' ') === -1 && norm.indexOf(tkn3) === 0 && tkn3.length > 2) return t3;
    }
    return null;
  }

  // ── Word study flyout panel ───────────────────────────────────────────────

  function vsOpenWordStudy(tokenEl, wordText) {
    // Toggle off same token
    if (_vsActiveToken === tokenEl) {
      tokenEl.classList.remove('vs-token--active');
      _vsActiveToken = null;
      if (_vsWordPanelEl) _vsWordPanelEl.setAttribute('hidden', '');
      return;
    }
    if (_vsActiveToken) _vsActiveToken.classList.remove('vs-token--active');
    _vsActiveToken = tokenEl;
    tokenEl.classList.add('vs-token--active');

    // Create or reuse the word panel element (inserted right after token row)
    var tokenRow = document.getElementById('vs-token-row');
    if (!tokenRow) return;

    if (!_vsWordPanelEl) {
      _vsWordPanelEl = document.createElement('div');
      _vsWordPanelEl.id = 'vs-word-panel';
      _vsWordPanelEl.className = 'vs-word-panel';
    }
    if (_vsWordPanelEl.parentNode !== tokenRow.parentNode) {
      tokenRow.parentNode.insertBefore(_vsWordPanelEl, tokenRow.nextSibling);
    }
    _vsWordPanelEl.innerHTML = '<div class="vs-word-panel__loading">Loading…</div>';
    _vsWordPanelEl.removeAttribute('hidden');

    var parsed = _vsCurrentRef;
    if (!parsed) return;

    var testament = _vsTestament(parsed);

    Promise.all([
      loadInterlinear(parsed.bookId),
      loadStrongs(testament)
    ]).then(function (results) {
      var interlinear  = results[0];
      var strongsDict  = results[1];

      var chData    = interlinear && interlinear[String(parsed.ch)];
      var vTokens   = chData && chData[String(parsed.v)];
      var match     = _vsMatchToken(vTokens, wordText);
      var strongsId = match ? match.s : null;
      var entry     = strongsId ? (strongsDict && strongsDict[strongsId]) : null;

      _vsRenderWordPanel(wordText, strongsId, entry, null, tokenEl);
    }).catch(function () {
      if (_vsWordPanelEl) {
        _vsWordPanelEl.innerHTML = '<div class="vs-word-panel__no-data">Could not load word data.</div>';
      }
    });
  }

  function _vsRenderWordPanel(wordText, strongsId, entry, morph, tokenEl) {
    if (!_vsWordPanelEl) return;

    var html = '<div class="vs-word-panel__inner">';
    html += '<button class="vs-word-panel__close" aria-label="Close word study" id="vs-word-panel-close">✕</button>';

    // ── Header: English word + Strong's number ────────────────────────────
    html += '<div class="vs-word-panel__header">';
    html += '<span class="vs-word-panel__eng">' + escHtml(wordText) + '</span>';
    if (strongsId) {
      html += '<span class="vs-word-panel__strongs">' + escHtml(strongsId) + '</span>';
    }
    html += '</div>';

    if (entry) {
      // ── Original language: lemma + transliteration ──────────────────────
      if (entry.lemma) {
        html += '<div class="vs-word-panel__orig">';
        html += '<span class="vs-word-panel__lemma">' + escHtml(entry.lemma) + '</span>';
        if (entry.translit) {
          html += '<span class="vs-word-panel__translit">' + escHtml(entry.translit) + '</span>';
        }
        if (entry.pronounce) {
          html += '<span class="vs-word-panel__pronounce">(' + escHtml(entry.pronounce) + ')</span>';
        }
        html += '</div>';
      }
      // ── Definition / gloss ───────────────────────────────────────────────
      if (entry.gloss) {
        html += '<div class="vs-word-panel__gloss">' + escHtml(entry.gloss) + '</div>';
      }
      if (entry.def && entry.def !== entry.gloss) {
        var shortDef = entry.def.length > 300 ? entry.def.slice(0, 300) + '…' : entry.def;
        html += '<div class="vs-word-panel__def">' + escHtml(shortDef) + '</div>';
      }
      // ── Derivation / root ────────────────────────────────────────────────
      if (entry.deriv) {
        html += '<div class="vs-word-panel__deriv">' + escHtml(entry.deriv) + '</div>';
      }
    } else if (strongsId) {
      html += '<div class="vs-word-panel__no-entry">Strong\'s entry not found for ' + escHtml(strongsId) + '.</div>';
    } else {
      html += '<div class="vs-word-panel__no-data">No Strong\'s data found for "' + escHtml(wordText) + '".' +
        '<br><small>Interlinear data may not be available for this verse.</small></div>';
    }

    // ── Action links ─────────────────────────────────────────────────────
    if (strongsId) {
      html += '<div class="vs-word-panel__actions">' +
        '<a class="vs-context-btn" href="' +
        escHtml(SEARCH_URL + '?s=' + encodeURIComponent(strongsId)) +
        '">All verses with ' + escHtml(strongsId) + '</a>' +
        '<a class="vs-context-btn" href="' +
        escHtml(WORD_URL + '?s=' + encodeURIComponent(strongsId)) +
        '">Word Deep Dive</a>' +
        '</div>';
    }

    html += '</div>';
    _vsWordPanelEl.innerHTML = html;

    var closeBtn = document.getElementById('vs-word-panel-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        if (_vsActiveToken) {
          _vsActiveToken.classList.remove('vs-token--active');
          _vsActiveToken = null;
        }
        _vsWordPanelEl.setAttribute('hidden', '');
      });
    }
  }

  // ── Modal Word Study tab ──────────────────────────────────────────────────

  function renderModalWordStudy(parsed, container) {
    container._wsLoaded = true;
    container.innerHTML = '<div class="bsw-ws-loading">Loading word data…</div>';

    if (!parsed || (!parsed.v && parsed.v !== 0)) {
      container.innerHTML = '<p class="bsw-ws-note">Word study is available for single-verse references.</p>';
      return;
    }

    var testament = _vsTestament(parsed);

    Promise.all([
      loadInterlinear(parsed.bookId),
      loadStrongs(testament)
    ]).then(function (results) {
      var interlinear = results[0];
      var strongsDict = results[1];

      var chData  = interlinear && interlinear[String(parsed.ch)];
      var vTokens = chData && chData[String(parsed.v)];

      if (!vTokens || !vTokens.length) {
        container.innerHTML = '<p class="bsw-ws-note">No interlinear data available for ' +
          escHtml(parsed.display) + '.</p>';
        return;
      }

      var html = '<div class="bsw-ws-table">';
      vTokens.forEach(function (tok) {
        if (!tok.s) return;
        var entry = strongsDict && strongsDict[tok.s];
        html += '<div class="bsw-ws-row">';
        html += '<div class="bsw-ws-eng">' + escHtml(tok.text || '–') + '</div>';
        html += '<div class="bsw-ws-strongs"><a class="bsw-ws-strongs-link" href="' +
          escHtml(WORD_URL + '?s=' + encodeURIComponent(tok.s)) + '" target="_blank">' +
          escHtml(tok.s) + ' ↗</a></div>';
        if (entry) {
          html += '<div class="bsw-ws-lemma">' + escHtml(entry.lemma || '') + '</div>';
          html += '<div class="bsw-ws-translit">' + escHtml(entry.translit || '') + '</div>';
          html += '<div class="bsw-ws-gloss">' + escHtml(entry.gloss || '') + '</div>';
        } else {
          html += '<div class="bsw-ws-lemma"></div><div class="bsw-ws-translit"></div><div class="bsw-ws-gloss"></div>';
        }
        html += '</div>';
      });
      html += '</div>';
      html += '<p class="bsw-ws-attr">Interlinear data: public domain (tahmmee/interlinear_bibledata). ' +
        'Strong\'s dictionary: openscriptures/strongs (public domain).</p>';
      container.innerHTML = html;
    }).catch(function () {
      container.innerHTML = '<p class="bsw-ws-note">Could not load word study data.</p>';
    });
  }

  // ── Interlinear sentence diagram ─────────────────────────────────────────

  // Sort tokens by their position in the English verse text so tiles read
  // left-to-right in verse order rather than Strong's-number order.
  function vsOrderByVerseText(tokens, verseText) {
    if (!tokens || !tokens.length) return tokens || [];
    var clean = verseText.toLowerCase().replace(/['''"",.:;!?()\[\]\-]/g, ' ');
    var positioned = tokens.map(function (tok, i) {
      var phrase = (tok.text || '').toLowerCase().replace(/['''"",.:;!?()\[\]\-]/g, ' ').trim();
      var pos = phrase ? clean.indexOf(phrase) : -1;
      return { tok: tok, pos: pos < 0 ? 1e6 + i : pos, orig: i };
    });
    positioned.sort(function (a, b) {
      return a.pos !== b.pos ? a.pos - b.pos : a.orig - b.orig;
    });
    return positioned.map(function (p) { return p.tok; });
  }

  function vsRenderInterlinear(vTokens, strongsDict, container, isHebrew) {
    if (!vTokens || !vTokens.length) {
      container.innerHTML = '<p class="vs-interlinear-note">No interlinear data available.</p>';
      return;
    }

    var verseText = (document.getElementById('vs-focal-text') || {}).textContent || '';
    var tokens = vsOrderByVerseText(
      vTokens.filter(function (t) { return t.s; }),
      verseText
    );

    var grid = document.createElement('div');
    grid.className = isHebrew ? 'vs-interlinear-grid vs-interlinear-grid--rtl' : 'vs-interlinear-grid';

    var detail = document.createElement('div');
    detail.className = 'vs-interlinear-detail';
    detail.setAttribute('hidden', '');

    var activeTile = null;

    tokens.forEach(function (tok) {
      var entry = strongsDict && strongsDict[tok.s];

      var tile = document.createElement('button');
      tile.className = 'vs-tile';
      tile.type = 'button';

      var orig = (entry && entry.lemma)
        ? '<div class="vs-tile__lemma">' + escHtml(entry.lemma) + '</div>' +
          (entry.translit ? '<div class="vs-tile__translit">' + escHtml(entry.translit) + '</div>' : '')
        : '<div class="vs-tile__lemma vs-tile__lemma--missing">—</div>';

      tile.innerHTML =
        orig +
        '<div class="vs-tile__divider"></div>' +
        '<div class="vs-tile__eng">' + escHtml(tok.text || '') + '</div>' +
        '<div class="vs-tile__strongs">' + escHtml(tok.s) + '</div>';

      tile.addEventListener('click', function () {
        if (activeTile === tile) {
          tile.classList.remove('vs-tile--active');
          activeTile = null;
          detail.setAttribute('hidden', '');
          return;
        }
        if (activeTile) activeTile.classList.remove('vs-tile--active');
        activeTile = tile;
        tile.classList.add('vs-tile--active');
        vsRenderTileDetail(tok, entry, detail);
        detail.removeAttribute('hidden');
      });

      grid.appendChild(tile);
    });

    container.appendChild(grid);
    container.appendChild(detail);

    var attr = document.createElement('p');
    attr.className = 'vs-interlinear-attr';
    attr.innerHTML = 'Interlinear: public domain (tahmmee/interlinear_bibledata). ' +
      'Strong&#x2019;s: openscriptures/strongs (public domain).';
    container.appendChild(attr);
  }

  function vsRenderTileDetail(tok, entry, detailEl) {
    var html = '<div class="vs-id-header">' +
      '<span class="vs-id-eng">' + escHtml(tok.text || '') + '</span>' +
      '<span class="vs-id-strongs">' + escHtml(tok.s || '') + '</span>';
    if (entry && entry.lemma) {
      html += '<span class="vs-id-lemma">' + escHtml(entry.lemma) + '</span>';
      if (entry.translit) html += '<span class="vs-id-translit">' + escHtml(entry.translit) + '</span>';
      if (entry.pronounce) html += '<span class="vs-id-pronounce">(' + escHtml(entry.pronounce) + ')</span>';
    }
    html += '</div>';
    if (entry) {
      if (entry.gloss) {
        html += '<div class="vs-id-gloss">' + escHtml(entry.gloss) + '</div>';
      }
      if (entry.def && entry.def !== entry.gloss) {
        html += '<div class="vs-id-def">' + escHtml(entry.def) + '</div>';
      }
      if (entry.deriv) {
        html += '<div class="vs-id-deriv">' + escHtml(entry.deriv) + '</div>';
      }
    } else {
      html += '<p class="vs-id-note">No Strong\'s entry for ' + escHtml(tok.s || '') + '.</p>';
    }
    if (tok.s) {
      html += '<div class="vs-id-actions">' +
        '<a class="vs-context-btn" href="' +
        escHtml(SEARCH_URL + '?s=' + encodeURIComponent(tok.s)) +
        '">All verses with ' + escHtml(tok.s) + '</a>' +
        '<a class="vs-context-btn" href="' +
        escHtml(WORD_URL + '?s=' + encodeURIComponent(tok.s)) +
        '">Word Deep Dive</a>' +
        '</div>';
    }
    detailEl.innerHTML = html;
  }

  // ── Verse Study sections ──────────────────────────────────────────────────

  function loadVerseSections(parsed) {
    var container = document.getElementById('vs-sections-container');
    if (!container) return;

    // Interlinear section first so it appears at the top
    var interlinearSec = vsCreateSection(container, 'vs-interlinear', 'Interlinear');
    var testament = _vsTestament(parsed);
    Promise.all([loadInterlinear(parsed.bookId), loadStrongs(testament)])
      .then(function (results) {
        var chData  = results[0] && results[0][String(parsed.ch)];
        var vTokens = chData && chData[String(parsed.v)];
        if (!vTokens || !vTokens.length) { interlinearSec.el.remove(); vsRebuildNav(); return; }
        vsRenderInterlinear(vTokens, results[1], interlinearSec.bodyEl, testament === 'hebrew');
        interlinearSec.el.removeAttribute('hidden');
        vsRebuildNav();
      });

    // Notes section — always present, renders immediately
    var notesSec = vsCreateSection(container, 'vs-notes', 'Notes');
    _renderNotesPanel(parsed, notesSec.bodyEl);
    notesSec.el.removeAttribute('hidden');
    vsRebuildNav();

    // Create remaining sections in canonical order (hidden initially)
    var xrefSec  = vsCreateSection(container, 'vs-xrefs',      'Cross-References');
    var commSec  = vsCreateSection(container, 'vs-commentary', 'Commentary');
    var parSec   = vsCreateSection(container, 'vs-parallels',  'Parallel Passages');
    var cmpSec   = vsCreateSection(container, 'vs-compare',    'All Translations');

    // Load cross-references
    loadCrossRefs(parsed.bookId).then(function (data) {
      var entries = vsExtractXrefs(data, parsed);
      if (!entries || !entries.length) { xrefSec.el.remove(); vsRebuildNav(); return; }
      vsRenderXrefList(entries, xrefSec.bodyEl);
      xrefSec.el.removeAttribute('hidden');
      vsRebuildNav();
    });

    // Load commentary — with source picker
    (function () {
      function vsLoadComm(src) {
        commSec.bodyEl.innerHTML = '<p class="bsw-modal__loading">Loading commentary…</p>';
        loadCommentary(parsed.bookId, src).then(function (data) {
          var html = _extractCommHtml(data, parsed, src);
          var attrHtml = html ? '<p class="vs-commentary-attr">' + _commAttr(src) + '</p>' : '';
          if (!html && commSec.el.hidden) {
            commSec.el.remove(); vsRebuildNav(); return;
          }
          commSec.bodyEl.innerHTML = (html || '<p class="bsw-modal__commentary-empty">No commentary found for this verse.</p>') + attrHtml;
          wireRefLinks(commSec.bodyEl);
          if (commSec.el.hasAttribute('hidden')) {
            commSec.el.removeAttribute('hidden');
            vsRebuildNav();
          }
        });
      }

      // Build picker
      var opts = COMMENTARY_SOURCES.map(function (s) {
        return '<option value="' + s.id + '"' + (s.id === _commentarySource ? ' selected' : '') + '>' + s.label + '</option>';
      }).join('');
      var pickerEl = document.createElement('div');
      pickerEl.className = 'vs-comm-picker';
      pickerEl.innerHTML = '<label class="vs-comm-label">Source:</label>' +
        '<select class="vs-comm-select">' + opts + '</select>';
      commSec.bodyEl.parentNode.insertBefore(pickerEl, commSec.bodyEl);

      pickerEl.querySelector('.vs-comm-select').addEventListener('change', function () {
        _commentarySource = this.value;
        localStorage.setItem('bsw_comm_src', _commentarySource);
        vsLoadComm(_commentarySource);
      });

      vsLoadComm(_commentarySource);
    }());

    // Load parallel passages
    loadParallels(parsed.bookId).then(function (data) {
      var sections = vsExtractParallels(data, parsed);
      if (!sections || !sections.length) { parSec.el.remove(); vsRebuildNav(); return; }
      vsRenderParallelList(sections, parSec.bodyEl, parsed);
      parSec.el.removeAttribute('hidden');
      vsRebuildNav();
    });

    // All Translations — always present if versions are loaded
    if (metaVersions && metaVersions.length) {
      vsRenderVersionCompare(parsed, cmpSec.bodyEl);
      cmpSec.el.removeAttribute('hidden');
      vsRebuildNav();
    } else {
      cmpSec.el.remove();
      vsRebuildNav();
    }

    // Nave's Topics — only for single-verse refs
    if (parsed.v) {
      var topicSec = vsCreateSection(container, 'vs-topics', 'Nave\'s Topics');
      renderVSTopics(parsed, topicSec.bodyEl);
      topicSec.el.removeAttribute('hidden');
      vsRebuildNav();
    }

    // Confessions — only for single-verse refs
    if (parsed.v) {
      var confSec = vsCreateSection(container, 'vs-confessions', 'Confessional Citations');
      var confUrl = _LIB_VERSE_IDX_BASE + '/' + parsed.bookId + '.json';
      (_libVerseCache[parsed.bookId]
        ? Promise.resolve(_libVerseCache[parsed.bookId])
        : fetch(confUrl).then(function (r) { return r.ok ? r.json() : Promise.reject(); })
            .then(function (d) { _libVerseCache[parsed.bookId] = d; return d; })
      ).then(function (data) {
        var cits = (data[String(parsed.ch)] && data[String(parsed.ch)][String(parsed.v)]) || [];
        if (!cits.length) { confSec.el.remove(); vsRebuildNav(); return; }
        renderModalConfessions(parsed, confSec.bodyEl);
        confSec.el.removeAttribute('hidden');
        vsRebuildNav();
      }).catch(function () { confSec.el.remove(); vsRebuildNav(); });
    }

    // Dictionary — only for single-verse refs
    if (parsed.v) {
      var dictSec = vsCreateSection(container, 'vs-dictionary', 'Dictionary');
      _dictEntriesForVerse(parsed).then(function (entries) {
        if (!entries.length) { dictSec.el.remove(); vsRebuildNav(); return; }
        renderVSDictionary(parsed, dictSec.bodyEl);
        dictSec.el.removeAttribute('hidden');
        vsRebuildNav();
      }).catch(function () { dictSec.el.remove(); vsRebuildNav(); });
    }
  }

  function vsCreateSection(container, id, label) {
    var sec = document.createElement('section');
    sec.className = 'vs-section';
    sec.id = id;
    sec.setAttribute('hidden', '');

    var heading = document.createElement('h2');
    heading.className = 'vs-section-heading';
    heading.textContent = label;

    var body = document.createElement('div');
    body.className = 'vs-section-body';

    sec.appendChild(heading);
    sec.appendChild(body);
    container.appendChild(sec);
    return { el: sec, bodyEl: body, id: id, label: label };
  }

  function vsRebuildNav() {
    var sidebar     = document.getElementById('vs-sidebar');
    var mobileNav   = document.getElementById('vs-mobile-nav');
    var mobileSelect= document.getElementById('vs-section-select');
    var visible     = Array.prototype.slice.call(
      document.querySelectorAll('#vs-sections-container .vs-section:not([hidden])')
    );

    if (sidebar) {
      sidebar.innerHTML = '';
      visible.forEach(function (sec) {
        var hd = sec.querySelector('.vs-section-heading');
        if (!hd) return;
        var btn = document.createElement('button');
        btn.className = 'vs-nav-btn';
        btn.textContent = hd.textContent;
        btn.addEventListener('click', function () {
          sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
        sidebar.appendChild(btn);
      });
    }

    if (mobileSelect) {
      mobileSelect.innerHTML = '<option value="">Jump to section…</option>';
      visible.forEach(function (sec) {
        var hd = sec.querySelector('.vs-section-heading');
        if (!hd) return;
        var opt = document.createElement('option');
        opt.value = sec.id;
        opt.textContent = hd.textContent;
        mobileSelect.appendChild(opt);
      });
    }

    // Show/hide mobile nav based on whether there are any visible sections
    if (mobileNav) {
      if (visible.length > 0) mobileNav.removeAttribute('hidden');
      else mobileNav.setAttribute('hidden', '');
    }
  }

  // ── All-translations compare section ─────────────────────────────────────

  function vsRenderVersionCompare(parsed, container) {
    if (!metaVersions || !metaVersions.length) return;
    var currentVer = getVersion();

    metaVersions.forEach(function (ver) {
      var row = document.createElement('div');
      row.className = 'vs-cmp-row' + (ver.id === currentVer ? ' vs-cmp-row--current' : '');

      var hdr = document.createElement('div');
      hdr.className = 'vs-cmp-row__hdr';
      hdr.innerHTML =
        '<span class="vs-cmp-row__id">' + escHtml(ver.id) + '</span>' +
        '<span class="vs-cmp-row__name">' + escHtml(ver.fullname || ver.name || ver.id) + '</span>';
      row.appendChild(hdr);

      var textEl = document.createElement('p');
      textEl.className = 'vs-cmp-row__text vs-cmp-row__text--loading';
      textEl.textContent = 'Loading…';
      row.appendChild(textEl);

      container.appendChild(row);

      resolveVerses(parsed, ver.id).then(function (rows) {
        var text = rows && rows[0] && rows[0].text;
        if (text) {
          textEl.className = 'vs-cmp-row__text';
          textEl.textContent = text;
        } else {
          textEl.className = 'vs-cmp-row__text vs-cmp-row__text--na';
          textEl.textContent = 'Not available in this translation.';
        }
      }).catch(function () {
        textEl.className = 'vs-cmp-row__text vs-cmp-row__text--na';
        textEl.textContent = 'Could not load.';
      });
    });
  }

  // ── Cross-ref helpers ─────────────────────────────────────────────────────

  function vsExtractXrefs(data, parsed) {
    if (!data) return null;
    var chData = data[String(parsed.ch)];
    if (!chData) return null;
    var rawRefs = chData[String(parsed.v)];
    if (!rawRefs || !rawRefs.length) return null;
    var entries = rawRefs.map(parseCrossRefEntry);
    entries.sort(_compareCanonical);
    return entries;
  }

  function vsRenderXrefList(entries, container) {
    var div = document.createElement('div');
    div.className = 'vs-xref-list';
    entries.forEach(function (entry) {
      var tierClass = '';
      if (entry.votes > 1) {
        tierClass = entry.votes >= 15 ? ' bsw-xref--high' :
                    entry.votes >= 6  ? ' bsw-xref--med'  : ' bsw-xref--low';
      }
      var a = document.createElement('a');
      a.className = 'vs-xref-link' + tierClass;
      a.setAttribute('data-ref', entry.ref);
      a.setAttribute('role', 'button');
      a.setAttribute('tabindex', '0');
      a.textContent = entry.ref;
      var p = parseRef(entry.ref);
      if (p) wireRefEl(a, p);
      div.appendChild(a);
    });
    container.appendChild(div);
  }

  // ── Commentary helpers ────────────────────────────────────────────────────

  function vsExtractCommentary(data, parsed) {
    // Delegates to shared _extractCommHtml helper; kept for any remaining callers
    return _extractCommHtml(data, parsed, _commentarySource);
  }

  // ── Parallel passage helpers ──────────────────────────────────────────────

  function vsExtractParallels(data, parsed) {
    if (!data) return null;
    var chData = data[String(parsed.ch)];
    if (!chData) return null;
    var entries = chData[String(parsed.v)];
    if (!entries || !entries.length) return null;
    return entries;
  }

  function vsRenderParallelList(sections, container, parsed) {
    var version = getVersion();
    sections.forEach(function (entry) {
      (entry.refs || []).forEach(function (refObj) {
        var p = parseRef(refObj.passage);
        if (!p) return;

        var typeMeta = _PARALLEL_TYPE_META[entry.type] || _PARALLEL_TYPE_META['parallel'];

        var panel = document.createElement('div');
        panel.className = 'vs-parallel-panel';

        var header = document.createElement('div');
        header.className = 'vs-parallel-header';

        var badge = document.createElement('span');
        badge.className = 'reader-parallel-badge ' + typeMeta.cls;
        badge.textContent = typeMeta.icon + ' ' + typeMeta.label;

        var refSpan = document.createElement('span');
        refSpan.className = 'vs-parallel-ref';
        refSpan.textContent = refObj.passage;

        var readLink = document.createElement('a');
        readLink.className = 'vs-parallel-read-link';
        readLink.href = READER_URL + '?ref=' + encodeURIComponent(refObj.passage);
        readLink.textContent = '↗';
        readLink.title = 'Open in Reader';

        header.appendChild(badge);
        header.appendChild(refSpan);
        header.appendChild(readLink);

        var body = document.createElement('div');
        body.className = 'vs-parallel-body';
        body.innerHTML = '<span class="reader-parallel-loading">Loading…</span>';

        panel.appendChild(header);
        panel.appendChild(body);
        container.appendChild(panel);

        resolveVerses(p, version).then(function (verses) {
          if (!verses || !verses.length) {
            body.innerHTML = '<span class="reader-parallel-empty">Not available in ' +
              escHtml(version) + '.</span>';
            return;
          }
          var html = '<p class="vs-parallel-text">';
          verses.forEach(function (vr) {
            html += '<sup class="reader-verse__num" style="cursor:default">' +
              vr.verse + '</sup>' + escHtml(vr.text) + ' ';
          });
          html += '</p>';
          body.innerHTML = html;
        }).catch(function () {
          body.innerHTML = '<span class="reader-parallel-empty">Could not load passage.</span>';
        });
      });
    });
  }

  // ── Word Deep Dive page ───────────────────────────────────────────────────

  function initWordPage() {
    var params   = new URLSearchParams(window.location.search);
    var rawId    = (params.get('s') || '').trim().toUpperCase();
    var headerEl = document.getElementById('wd-header');

    if (!rawId || !/^[GH]\d+$/.test(rawId)) {
      headerEl.innerHTML = '<p class="wd-error">No Strong\'s number provided. Use <code>?s=G3056</code> or <code>?s=H430</code>.</p>';
      return;
    }

    document.title = rawId + ' — Word Study — Bible Study';

    // Update back link to search page pre-filled with this Strong's number
    var backLink = document.getElementById('wd-back-link');
    if (backLink) backLink.href = SEARCH_URL + '?s=' + encodeURIComponent(rawId);

    var testament = rawId[0] === 'G' ? 'greek' : 'hebrew';

    // Register so setVersion() re-renders occurrences on any version change
    _wdRerenderFn = function (ver) {
      var versesSection = document.getElementById('wd-verses');
      if (versesSection && versesSection._rerenderFn) versesSection._rerenderFn(ver);
    };

    // Phase 0: load metadata + strong's entry
    Promise.all([loadVersions(), loadBooks(), loadStrongs(testament)])
      .then(function (results) {
        var strongsDict = results[2];
        var entry = strongsDict && strongsDict[rawId];

        _wdRenderHeader(rawId, entry, headerEl);

        // Phase 1: scan all interlinear files for this testament
        var books = metaBooks.filter(function (b) {
          return b.testament === (testament === 'greek' ? 'NT' : 'OT');
        });

        var bookMatches = {}; // bookId → [{ch, v, phrases:[]}]
        var totalCount  = 0;
        var translationCount = {}; // phrase → count

        var fetches = books.map(function (bk) {
          return loadInterlinear(bk.id).then(function (data) {
            if (!data) return;
            Object.keys(data).forEach(function (ch) {
              Object.keys(data[ch]).forEach(function (v) {
                var tokens = data[ch][v];
                var phrases = [];
                tokens.forEach(function (tok) {
                  if (tok.s === rawId && tok.text) {
                    phrases.push(tok.text);
                    var norm = _wdNormalizePhrase(tok.text);
                    translationCount[norm] = (translationCount[norm] || 0) + 1;
                    totalCount++;
                  }
                });
                if (phrases.length) {
                  if (!bookMatches[bk.id]) bookMatches[bk.id] = { book: bk, verses: [] };
                  bookMatches[bk.id].verses.push({ ch: ch, v: v, phrases: phrases });
                }
              });
            });
          });
        });

        return Promise.all(fetches).then(function () {
          return { bookMatches: bookMatches, totalCount: totalCount, translationCount: translationCount };
        });
      })
      .then(function (results) {
        var bookMatches      = results.bookMatches;
        var totalCount       = results.totalCount;
        var translationCount = results.translationCount;

        if (!totalCount) {
          document.getElementById('wd-stats').removeAttribute('hidden');
          document.getElementById('wd-stats').innerHTML =
            '<p class="wd-no-results">No occurrences found for ' + escHtml(rawId) + '.</p>';
          return;
        }

        var bookList = Object.keys(bookMatches).map(function (id) { return bookMatches[id]; });
        _wdBookList    = bookList;
        _wdCurrentFilter = null;
        _wdCurrentBook   = null;

        // Render stats
        _wdRenderStats(totalCount, bookList.length, translationCount);

        // Render translations
        _wdRenderTranslations();

        // Render books overview
        _wdRenderBooks();

        // Phase 2: load verse text and render all occurrences
        _wdRenderVerses(rawId);
      })
      .catch(function (err) {
        headerEl.innerHTML = '<p class="wd-error">Failed to load data: ' + escHtml(String(err)) + '</p>';
      });
  }

  function _wdRenderHeader(rawId, entry, el) {
    var html = '<div class="wd-header-inner">';
    html += '<span class="wd-id">' + escHtml(rawId) + '</span>';
    if (entry) {
      if (entry.lemma)    html += '<span class="wd-lemma">'    + escHtml(entry.lemma)    + '</span>';
      if (entry.translit) html += '<span class="wd-translit">' + escHtml(entry.translit) + '</span>';
      if (entry.pronounce) html += '<span class="wd-pronounce">(' + escHtml(entry.pronounce) + ')</span>';
      html += '</div>';
      if (entry.gloss) html += '<div class="wd-gloss">' + escHtml(entry.gloss) + '</div>';
      if (entry.def && entry.def !== entry.gloss) {
        html += _wdRenderDefChips(entry.def);
      }
      if (entry.deriv) html += '<div class="wd-deriv">' + escHtml(entry.deriv) + '</div>';
    } else {
      html += '</div><p class="wd-no-entry">Strong\'s dictionary entry not found for ' + escHtml(rawId) + '.</p>';
    }
    el.innerHTML = html;

    // wire the "show more" toggle
    var toggle = el.querySelector('.wd-def-toggle');
    var extra  = el.querySelector('.wd-def-extra');
    if (toggle && extra) {
      toggle.addEventListener('click', function () {
        var open = extra.style.display !== 'none';
        extra.style.display = open ? 'none' : '';
        toggle.textContent = open ? '+ more' : '− less';
      });
    }
  }

  function _wdRenderDefChips(def) {
    var items = def.split(/,\s*/);
    var primary = [];   // plain translation words
    var tagged  = [];   // [idiom] / [phrase] / etc.

    items.forEach(function (raw) {
      var item = raw.trim();
      if (!item) return;
      var m = item.match(/^\[([^\]]+)\]\s*(.*)/);
      if (m) {
        var label = m[2].trim() || m[1];
        tagged.push('<span class="wd-def-chip wd-def-chip--tagged" title="' + escHtml(m[1]) + '">' +
          escHtml(label) + '</span>');
      } else {
        primary.push('<span class="wd-def-chip">' + escHtml(item) + '</span>');
      }
    });

    var html = '<div class="wd-def-chips">';
    html += primary.join('');
    if (tagged.length) {
      html += '<div class="wd-def-extra" style="display:none">' + tagged.join('') + '</div>';
      html += '<button class="wd-def-toggle">+ more</button>';
    }
    html += '</div>';
    return html;
  }

  function _wdRenderStats(total, bookCount, translationCount) {
    var uniqueTranslations = Object.keys(translationCount).length;
    var statsEl = document.getElementById('wd-stats');
    statsEl.innerHTML =
      '<div class="wd-stat-card"><span class="wd-stat-num">' + total + '</span><span class="wd-stat-label">occurrences</span></div>' +
      '<div class="wd-stat-card"><span class="wd-stat-num">' + bookCount + '</span><span class="wd-stat-label">books</span></div>' +
      '<div class="wd-stat-card"><span class="wd-stat-num">' + uniqueTranslations + '</span><span class="wd-stat-label">unique translations</span></div>';
    statsEl.removeAttribute('hidden');
    var bodyEl = document.getElementById('wd-body');
    if (bodyEl) bodyEl.removeAttribute('hidden');
  }

  // ── Phrase normalization
  // Iteratively strips leading function words so "him to his father" ≡ "doth my father" ≡ "father".
  // Possessives are collapsed: "father's" → "father".
  var _wdStopWords = (function () {
    var w = 'a an the to unto from with by in of at for on upon into through about before after ' +
            'over under against between among ' +
            'i me my mine we us our ours you your yours ' +
            'he him his she her hers it its they them their theirs ' +
            'ye thy thine thou thee ' +
            'and or but nor ' +
            'doth hath is was be am are were shall will do did does had have has ' +
            'let not neither also even thus so yet then now ' +
            'that which this these those yea nay no';
    var set = {};
    w.split(' ').forEach(function (t) { set[t] = true; });
    return set;
  }());

  function _wdNormalizePhrase(raw) {
    var s = (raw || '').toLowerCase().trim();
    // collapse possessives: father's → father, fathers' → fathers
    s = s.replace(/(\w)'s\b/g, '$1').replace(/(\w)s'\s/g, '$1s ');
    var words = s.split(/\s+/);
    // strip leading stop words one at a time, leaving at least one word
    while (words.length > 1 && _wdStopWords[words[0]]) {
      words.shift();
    }
    return words.join(' ') || s;
  }

  // Compute translation counts (normalized) for the given book subset.
  function _wdCalcTranslationCounts(bookFilter) {
    var counts = {};
    (_wdBookList || []).forEach(function (bm) {
      if (bookFilter && bm.book.id !== bookFilter) return;
      bm.verses.forEach(function (occ) {
        occ.phrases.forEach(function (p) {
          var n = _wdNormalizePhrase(p);
          counts[n] = (counts[n] || 0) + 1;
        });
      });
    });
    return counts;
  }

  // Compute per-book verse counts for the given translation filter.
  function _wdCalcBookCounts(translationFilter) {
    var counts = {};
    (_wdBookList || []).forEach(function (bm) {
      var n = translationFilter
        ? bm.verses.filter(function (occ) {
            return occ.phrases.some(function (p) { return _wdNormalizePhrase(p) === translationFilter; });
          }).length
        : bm.verses.length;
      if (n > 0) counts[bm.book.id] = n;
    });
    return counts;
  }

  function _wdRenderTranslations() {
    var section = document.getElementById('wd-translations');
    var body    = document.getElementById('wd-translations-body');
    if (!body) return;

    var counts = _wdCalcTranslationCounts(_wdCurrentBook);
    var total  = Object.keys(counts).reduce(function (s, k) { return s + counts[k]; }, 0);
    var pairs  = Object.keys(counts).map(function (k) { return { phrase: k, count: counts[k] }; });
    pairs.sort(function (a, b) { return b.count - a.count; });

    var html = '';
    pairs.forEach(function (p) {
      var pct    = total ? Math.round((p.count / total) * 100) : 0;
      var active = p.phrase === _wdCurrentFilter;
      html += '<button class="wd-translation-row' + (active ? ' wd-translation-row--active' : '') +
        '" data-phrase="' + escHtml(p.phrase) + '">' +
        '<span class="wd-translation-phrase">' + escHtml(p.phrase) + '</span>' +
        '<div class="wd-translation-bar-wrap">' +
        '<div class="wd-translation-bar" style="width:' + pct + '%"></div>' +
        '</div>' +
        '<span class="wd-translation-count">' + p.count + '</span>' +
        '</button>';
    });
    body.innerHTML = html;

    if (!body._transWired) {
      body._transWired = true;
      body.addEventListener('click', function (e) {
        var row = e.target.closest('.wd-translation-row');
        if (!row) return;
        _wdToggleFilter(row.dataset.phrase);
      });
    }

    section.removeAttribute('hidden');
  }

  function _wdToggleFilter(phrase) {
    _wdCurrentFilter = (phrase === _wdCurrentFilter) ? null : phrase;
    _wdRenderBooks();    // recompute book counts under new translation filter
    _wdRefreshVerses();
  }

  function _wdToggleBook(bookId) {
    _wdCurrentBook = (bookId === _wdCurrentBook) ? null : bookId;
    _wdRenderBooks();         // repaint pills so active state reflects new selection
    _wdRenderTranslations();  // recompute translation counts under new book filter
    _wdRefreshVerses();
  }

  function _wdRenderBooks() {
    var section = document.getElementById('wd-books');
    var body    = document.getElementById('wd-books-body');
    if (!body) return;

    var counts = _wdCalcBookCounts(_wdCurrentFilter);
    var sorted = (_wdBookList || []).slice().sort(function (a, b) {
      return (a.book.bookNumber || 0) - (b.book.bookNumber || 0);
    });

    var html = '';
    sorted.forEach(function (bm) {
      var count = counts[bm.book.id] || 0;
      if (!count) return;
      var active = bm.book.id === _wdCurrentBook;
      html += '<button class="wd-book-pill' + (active ? ' wd-book-pill--active' : '') +
        '" data-book="' + escHtml(bm.book.id) + '">' +
        escHtml(bm.book.name) + ' <span class="wd-book-count">' + count + '</span></button>';
    });
    body.innerHTML = html;

    if (!body._bookWired) {
      body._bookWired = true;
      body.addEventListener('click', function (e) {
        var pill = e.target.closest('.wd-book-pill[data-book]');
        if (!pill) return;
        _wdToggleBook(pill.dataset.book);
      });
    }

    section.removeAttribute('hidden');
  }

  function _wdRefreshVerses() {
    var section = document.getElementById('wd-verses');
    if (section && section._applyFilters) section._applyFilters(_wdCurrentFilter, _wdCurrentBook);
  }

  function _wdRenderVerses(strongsId) {
    var section    = document.getElementById('wd-verses');
    var statusEl   = document.getElementById('wd-verses-status');
    var body       = document.getElementById('wd-verses-body');
    var versionSel = document.getElementById('bible-version');
    var version    = (versionSel && versionSel.value) || localStorage.getItem('bsw_version') || 'bsb';

    section.removeAttribute('hidden');

    var sorted = (_wdBookList || []).slice().sort(function (a, b) {
      return (a.book.bookNumber || 0) - (b.book.bookNumber || 0);
    });

    function renderVerseCard(occ, book, bookSection, ver) {
      var refStr = book.name + ' ' + occ.ch + ':' + occ.v;
      var card = document.createElement('div');
      card.className = 'wd-verse-card';

      var refLink = document.createElement('a');
      refLink.className = 'ref wd-verse-ref-link';
      refLink.dataset.ref = refStr;
      refLink.href = '#';
      refLink.textContent = refStr;
      card.appendChild(refLink);

      var textEl = document.createElement('div');
      textEl.className = 'wd-verse-text';
      textEl.textContent = 'Loading…';
      card.appendChild(textEl);
      bookSection.appendChild(card);

      // Build deduplicated search terms (original + normalized core).
      // Sort longest-first, then drop shorter terms already covered by a longer
      // one to avoid double-marking (e.g. drop "father" when "his father" present).
      var termSet = {};
      occ.phrases.forEach(function (p) {
        var lo = p.toLowerCase().trim();
        if (lo) termSet[lo] = true;
        var norm = _wdNormalizePhrase(p);
        if (norm) termSet[norm] = true;
      });
      var searchTerms = Object.keys(termSet).sort(function (a, b) { return b.length - a.length; });
      searchTerms = searchTerms.filter(function (term, i) {
        var re = new RegExp('\\b' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b');
        for (var j = 0; j < i; j++) { if (re.test(searchTerms[j])) return false; }
        return true;
      });

      var parsed = parseRef(refStr);
      resolveVerses(parsed, ver).then(function (rows) {
        var text = rows && rows[0] && rows[0].text;
        if (text) {
          // Apply to plain text first (before escaping) to avoid marking inside tags
          var marked = text;
          searchTerms.forEach(function (term) {
            var esc = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
            marked = marked.replace(new RegExp('\\b(' + esc + ')\\b', 'gi'), '\x00$1\x01');
          });
          // Escape each segment, wrap marked spans
          textEl.innerHTML = marked.split(/\x00([^\x01]*)\x01/).map(function (seg, i) {
            return i % 2 === 0
              ? escHtml(seg)
              : '<mark class="wd-highlight">' + escHtml(seg) + '</mark>';
          }).join('');
        } else {
          textEl.textContent = '(verse not available)';
        }
      }).catch(function () {
        textEl.textContent = '(could not load)';
      });
    }

    function render(ver, translationFilter, bookFilter) {
      body.innerHTML = '';
      statusEl.innerHTML = '';

      // Build active-filter chips in status bar
      var chips = '';
      if (translationFilter) chips += '<span class="wd-chip">“' + escHtml(translationFilter) +
        '” <button class="wd-chip-clear" data-clear="trans">×</button></span>';
      if (bookFilter) {
        var bm2 = (_wdBookList || []).find(function (b) { return b.book.id === bookFilter; });
        var bName = bm2 ? bm2.book.name : bookFilter;
        chips += '<span class="wd-chip">' + escHtml(bName) +
          ' <button class="wd-chip-clear" data-clear="book">×</button></span>';
      }
      if (chips) {
        var chipBar = document.createElement('div');
        chipBar.className = 'wd-filter-bar';
        chipBar.innerHTML = chips;
        chipBar.addEventListener('click', function (e) {
          var btn = e.target.closest('.wd-chip-clear');
          if (!btn) return;
          if (btn.dataset.clear === 'trans') _wdToggleFilter(_wdCurrentFilter);
          else _wdToggleBook(_wdCurrentBook);
        });
        statusEl.appendChild(chipBar);
      }

      var total = 0;
      sorted.forEach(function (bm) {
        if (bookFilter && bm.book.id !== bookFilter) return;
        var occs = translationFilter
          ? bm.verses.filter(function (occ) {
              return occ.phrases.some(function (p) { return _wdNormalizePhrase(p) === translationFilter; });
            })
          : bm.verses;
        if (!occs.length) return;
        total += occs.length;

        var bookSection = document.createElement('div');
        bookSection.className = 'wd-book-section';
        bookSection.id = 'wd-book-' + bm.book.id;

        var heading = document.createElement('h3');
        heading.className = 'wd-book-heading';
        heading.textContent = bm.book.name;
        bookSection.appendChild(heading);
        body.appendChild(bookSection);

        occs.forEach(function (occ) { renderVerseCard(occ, bm.book, bookSection, ver); });
      });

      if (!total) {
        var empty = document.createElement('p');
        empty.className = 'wd-no-results';
        empty.textContent = 'No occurrences match the active filters.';
        body.appendChild(empty);
      }

      var countEl = document.createElement('p');
      countEl.className = 'wd-verses-count';
      countEl.textContent = total + ' verse' + (total === 1 ? '' : 's');
      statusEl.appendChild(countEl);

      wireRefLinks();
    }

    section._rerenderFn  = function (ver) { render(ver, _wdCurrentFilter, _wdCurrentBook); };
    section._applyFilters = function (tf, bf) { render(getVersion(), tf, bf); };
    render(version, null, null);
  }

  // ── Daily Discipline Page ─────────────────────────────────────────────────

  var DAILY_PLAN_KEY   = 'bsw_daily_plan';
  var DAILY_DEVOT_KEY  = 'bsw_daily_devot';
  var DAILY_NOTIF_KEY  = 'bsw_daily_notif';
  var DAILY_NOTIF_DISMISSED = 'bsw_daily_notif_dismissed';
  var DAILY_PLANS_ROOT    = _resolve('../../data/plans');
  var DAILY_VOTD_URL      = _resolve('../../data/votd/verses.json');
  var DAILY_CALENDAR_BASE = _resolve('../../read/');

  // Plans that use Jan-1 as Day 1 (no date picker needed)
  var DAILY_AUTO_PLANS = ['bible-in-a-year', 'bible-in-a-year-chronological'];

  // All plan metadata (id + title only; full data fetched on demand)
  var DAILY_PLAN_META = [
    { id: 'bible-in-a-year',               title: 'Bible in a Year',               days: 365 },
    { id: 'bible-in-a-year-chronological', title: 'Bible in a Year — Chronological', days: 365 },
    { id: 'mcheyne',                        title: "M'Cheyne",                       days: 365 },
    { id: 'nt-90-days',                     title: 'NT in 90 Days',                  days: 90  },
    { id: 'psalms-proverbs',               title: 'Psalms & Proverbs',              days: 31  },
    { id: 'gospels-30-days',               title: 'Gospels in 30 Days',             days: 30  }
  ];

  var DAILY_DEVOT_META = [
    { id: 'spurgeon-morning', label: 'Spurgeon — Morning' },
    { id: 'spurgeon-evening', label: 'Spurgeon — Evening' },
    { id: 'daily-psalms',     label: 'Daily Psalms' },
    { id: 'proverbs-month',   label: 'Proverbs of the Month' },
    { id: 'nt-daily',         label: 'NT Daily Reading' }
  ];

  var DAILY_DEVOT_BASE = _resolve('../../data/devotionals');

  function _dailyDayOfYear() {
    var now   = new Date();
    var start = new Date(now.getFullYear(), 0, 1);
    return Math.floor((now - start) / 86400000) + 1; // 1–365
  }

  function _dailyPeriod() {
    return new Date().getHours() < 12 ? 'morning' : 'evening';
  }

  function _dailyDayNum(planId, startDateStr) {
    if (DAILY_AUTO_PLANS.indexOf(planId) !== -1) {
      return _dailyDayOfYear();
    }
    if (!startDateStr) return 1;
    var start = new Date(startDateStr + 'T00:00:00');
    var today = new Date();
    today = new Date(today.getFullYear(), today.getMonth(), today.getDate());
    return Math.max(1, Math.floor((today - start) / 86400000) + 1);
  }

  function _dailyPassageUrl(passage) {
    return DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(passage);
  }

  function _dailyReadAllUrl(passages) {
    return DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(passages.join(', '));
  }

  function initDailyPage() {
    var planSelect  = document.getElementById('daily-plan-select');
    var devotSelect = document.getElementById('daily-devot-select');
    if (!planSelect) return;

    // ── Date/greeting header
    var greetingEl = document.getElementById('daily-greeting');
    var dateEl     = document.getElementById('daily-date');
    var now        = new Date();
    var period     = _dailyPeriod();
    var days       = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    var months     = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    if (greetingEl) {
      var hour = now.getHours();
      var salutation = hour < 12 ? 'Good morning' : hour < 17 ? 'Good afternoon' : 'Good evening';
      greetingEl.textContent = salutation;
    }
    if (dateEl) {
      dateEl.textContent = days[now.getDay()] + ' • ' + months[now.getMonth()] + ' ' + now.getDate() + ', ' + now.getFullYear();
    }

    // ── Populate plan selector
    var savedPlan = localStorage.getItem(DAILY_PLAN_KEY) || 'bible-in-a-year';
    DAILY_PLAN_META.forEach(function (pm) {
      var opt = document.createElement('option');
      opt.value = pm.id;
      opt.textContent = pm.title;
      if (pm.id === savedPlan) opt.selected = true;
      planSelect.appendChild(opt);
    });

    // ── Populate devotional selector
    if (devotSelect) {
      var defaultDevot = period === 'morning' ? 'spurgeon-morning' : 'spurgeon-evening';
      var savedDevot = localStorage.getItem(DAILY_DEVOT_KEY) || defaultDevot;
      DAILY_DEVOT_META.forEach(function (dm) {
        var opt = document.createElement('option');
        opt.value = dm.id;
        opt.textContent = dm.label;
        if (dm.id === savedDevot) opt.selected = true;
        devotSelect.appendChild(opt);
      });
      devotSelect.addEventListener('change', function () {
        localStorage.setItem(DAILY_DEVOT_KEY, devotSelect.value);
        _dailyRenderDevotional(devotSelect.value, period);
      });
    }

    // ── Plan selector change
    planSelect.addEventListener('change', function () {
      var pid = planSelect.value;
      localStorage.setItem(DAILY_PLAN_KEY, pid);
      _dailyRenderPlan(pid);
    });

    // ── Start date picker
    var datepicker = document.getElementById('daily-plan-datepicker');
    var dateInput  = document.getElementById('daily-start-date');
    if (dateInput) {
      dateInput.addEventListener('change', function () {
        var pid = planSelect.value;
        if (dateInput.value) {
          localStorage.setItem('bsw_daily_start_' + pid, dateInput.value);
        }
        _dailyRenderPlan(pid);
      });
    }

    // ── Initial renders
    _dailyRenderPlan(savedPlan);
    _dailyRenderVOTD();
    _dailyRenderDevotional(localStorage.getItem(DAILY_DEVOT_KEY) || 'daily-psalms', period);
    _dailySetupNotifications(period);
  }

  function _dailyRenderPlan(planId) {
    var contentEl  = document.getElementById('daily-plan-content');
    var datepicker = document.getElementById('daily-plan-datepicker');
    var dateInput  = document.getElementById('daily-start-date');
    if (!contentEl) return;

    var isAuto = DAILY_AUTO_PLANS.indexOf(planId) !== -1;
    if (datepicker) {
      if (isAuto) datepicker.setAttribute('hidden', '');
      else        datepicker.removeAttribute('hidden');
    }

    var startDateStr = isAuto ? null : (localStorage.getItem('bsw_daily_start_' + planId) || '');
    if (dateInput) {
      dateInput.value = startDateStr || '';
      if (!isAuto && !startDateStr) {
        // Default start date to today
        var today = new Date();
        var yyyy  = today.getFullYear();
        var mm    = ('0' + (today.getMonth() + 1)).slice(-2);
        var dd    = ('0' + today.getDate()).slice(-2);
        var todayStr = yyyy + '-' + mm + '-' + dd;
        dateInput.value = todayStr;
        localStorage.setItem('bsw_daily_start_' + planId, todayStr);
        startDateStr = todayStr;
      }
    }

    var dn   = _dailyDayNum(planId, startDateStr);
    var meta = DAILY_PLAN_META.find(function (p) { return p.id === planId; });
    var totalDays = meta ? meta.days : 365;

    contentEl.innerHTML = '<div class="daily-loading">Loading…</div>';

    fetch(DAILY_PLANS_ROOT + '/' + planId + '.json')
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (plan) {
        var clampedDay = Math.min(Math.max(dn, 1), plan.total_days);
        var dayData    = plan.days[clampedDay - 1];
        if (!dayData) { contentEl.innerHTML = '<p class="daily-plan-empty">No reading for today.</p>'; return; }

        var passages = dayData.passages || [];
        var html  = '<p class="daily-plan-day">Day ' + clampedDay + ' of ' + plan.total_days + '</p>';
        html += '<div class="daily-passages">';
        passages.forEach(function (p) {
          html += '<a class="daily-passage-chip" href="' + escHtml(_dailyPassageUrl(p)) + '">' + escHtml(p) + '</a>';
        });
        html += '</div>';
        if (passages.length > 1) {
          html += '<a class="daily-read-all" href="' + escHtml(_dailyReadAllUrl(passages)) + '">Read all today&rsquo;s sections &rarr;</a>';
        } else if (passages.length === 1) {
          html += '<a class="daily-read-all" href="' + escHtml(_dailyPassageUrl(passages[0])) + '">Read today&rsquo;s passage &rarr;</a>';
        }
        contentEl.innerHTML = html;
      })
      .catch(function () {
        contentEl.innerHTML = '<p class="daily-plan-empty">Could not load plan data.</p>';
      });
  }

  function _dailyRenderVOTD() {
    var el = document.getElementById('daily-votd-content');
    if (!el) return;
    el.innerHTML = '<div class="daily-loading">Loading…</div>';

    fetch(DAILY_VOTD_URL)
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (verses) {
        var doy  = _dailyDayOfYear();
        var ref  = verses[(doy - 1) % verses.length];
        var parsed = parseRef(ref);
        if (!parsed || !parsed.bookId) {
          el.innerHTML = '<p class="daily-plan-empty">Could not load verse.</p>';
          return;
        }
        var version = getVersion();
        return loadBook(version, parsed.bookId).then(function (chapters) {
          var chData = chapters && chapters[String(parsed.ch)];
          var text   = chData && chData[String(parsed.v)];
          if (!text) { el.innerHTML = '<p class="daily-plan-empty">Verse unavailable.</p>'; return; }
          el.innerHTML =
            '<blockquote>' + escHtml(text) + '</blockquote>' +
            '<cite>— <a class="ref" data-ref="' + escHtml(ref) + '">' + escHtml(ref) + '</a>' +
            ' &nbsp;<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(ref)) + '">Read in context &rarr;</a></cite>';
          wireRefLinks(el);
        });
      })
      .catch(function () {
        el.innerHTML = '<p class="daily-plan-empty">Could not load verse of the day.</p>';
      });
  }

  function _dailyRenderDevotional(source, period) {
    var titleEl = document.getElementById('daily-devot-title');
    var bodyEl  = document.getElementById('daily-devot-content');
    if (!bodyEl) return;

    var periodLabel = period === 'morning' ? 'Morning' : 'Evening';
    if (titleEl) {
      titleEl.innerHTML = periodLabel + ' Devotional <span class="daily-period-badge">' +
        (period === 'morning' ? '🌅' : '🌙') + ' ' + periodLabel + '</span>';
    }
    bodyEl.innerHTML = '<div class="daily-loading">Loading…</div>';

    var now       = new Date();
    var dayOfYear = _dailyDayOfYear();
    var dom       = now.getDate();       // 1–31
    var version   = getVersion();

    // ── Daily Psalms: morning = Psalm cycling by dayOfYear, evening = second Psalm or NT verse
    if (source === 'daily-psalms') {
      var psalmNumMorning = ((dayOfYear - 1) % 150) + 1;
      // Evening: offset by 75 so morning/evening are different
      var psalmNumEvening = ((dayOfYear - 1 + 75) % 150) + 1;
      var psalmNum = period === 'morning' ? psalmNumMorning : psalmNumEvening;
      var refStr   = 'Psalms ' + psalmNum;
      loadBook(version, 'psalms').then(function (chapters) {
        var chData = chapters && chapters[String(psalmNum)];
        if (!chData) { bodyEl.innerHTML = '<p class="daily-plan-empty">Psalm unavailable.</p>'; return; }
        var verses  = Object.keys(chData).sort(function (a, b) { return +a - +b; });
        // Show first 6 verses
        var preview = verses.slice(0, 6).map(function (v) { return chData[v]; }).join(' ');
        if (verses.length > 6) preview += ' …';
        bodyEl.innerHTML =
          '<p class="daily-devot-ref">Psalm ' + psalmNum + '</p>' +
          '<p class="daily-devot-text">' + escHtml(preview) + '</p>' +
          '<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(refStr)) + '">Read all of Psalm ' + psalmNum + ' →</a>';
      }).catch(function () {
        bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load Psalms.</p>';
      });
      return;
    }

    // ── Proverbs of the Month: Proverbs chapter = day of month (1–31; Proverbs has 31 ch)
    if (source === 'proverbs-month') {
      var ch = Math.min(dom, 31);
      if (period === 'evening') {
        // Evening: a short Psalm complement
        var psNum = ((dayOfYear - 1) % 150) + 1;
        loadBook(version, 'psalms').then(function (chapters) {
          var chData = chapters && chapters[String(psNum)];
          if (!chData) { bodyEl.innerHTML = '<p class="daily-plan-empty">Psalm unavailable.</p>'; return; }
          var verses  = Object.keys(chData).sort(function (a, b) { return +a - +b; });
          var preview = verses.slice(0, 6).map(function (v) { return chData[v]; }).join(' ');
          if (verses.length > 6) preview += ' …';
          bodyEl.innerHTML =
            '<p class="daily-devot-ref">Psalm ' + psNum + ' (evening reflection)</p>' +
            '<p class="daily-devot-text">' + escHtml(preview) + '</p>' +
            '<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent('Psalms ' + psNum)) + '">Read all of Psalm ' + psNum + ' →</a>';
        }).catch(function () { bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load.</p>'; });
        return;
      }
      loadBook(version, 'proverbs').then(function (chapters) {
        var chData = chapters && chapters[String(ch)];
        if (!chData) { bodyEl.innerHTML = '<p class="daily-plan-empty">Proverbs unavailable.</p>'; return; }
        var verses  = Object.keys(chData).sort(function (a, b) { return +a - +b; });
        var preview = verses.slice(0, 6).map(function (v) { return chData[v]; }).join(' ');
        if (verses.length > 6) preview += ' …';
        bodyEl.innerHTML =
          '<p class="daily-devot-ref">Proverbs ' + ch + '</p>' +
          '<p class="daily-devot-text">' + escHtml(preview) + '</p>' +
          '<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent('Proverbs ' + ch)) + '">Read all of Proverbs ' + ch + ' →</a>';
      }).catch(function () {
        bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load Proverbs.</p>';
      });
      return;
    }

    // ── NT Daily: cycle through NT (260 chapters: Matt–Rev)
    if (source === 'nt-daily') {
      var NT_BOOKS_CHRON = [
        ['matthew',34],['mark',16],['luke',24],['john',21],['acts',28],
        ['james',5],['galatians',6],['1thessalonians',5],['2thessalonians',3],
        ['1corinthians',16],['2corinthians',13],['romans',16],
        ['philippians',4],['philemon',1],['colossians',4],['ephesians',6],
        ['1timothy',6],['titus',3],['2timothy',4],
        ['hebrews',13],['1peter',5],['2peter',3],
        ['1john',5],['2john',1],['3john',1],['jude',1],['revelation',22]
      ];
      var totalNT = NT_BOOKS_CHRON.reduce(function (s, b) { return s + b[1]; }, 0);
      var ntOffset = period === 'evening' ? Math.floor(totalNT / 2) : 0;
      var ntIdx    = ((dayOfYear - 1 + ntOffset) % totalNT);
      var cumul = 0;
      var ntBook = null, ntCh = 1;
      for (var i = 0; i < NT_BOOKS_CHRON.length; i++) {
        var info = NT_BOOKS_CHRON[i];
        if (ntIdx < cumul + info[1]) { ntBook = info[0]; ntCh = ntIdx - cumul + 1; break; }
        cumul += info[1];
      }
      if (!ntBook) { bodyEl.innerHTML = '<p class="daily-plan-empty">Could not determine passage.</p>'; return; }
      loadBook(version, ntBook).then(function (chapters) {
        var chData = chapters && chapters[String(ntCh)];
        if (!chData) { bodyEl.innerHTML = '<p class="daily-plan-empty">Chapter unavailable.</p>'; return; }
        var bkName = metaBooks ? (metaBooks.find(function (b) { return b.id === ntBook; }) || {}).name || ntBook : ntBook;
        var verses  = Object.keys(chData).sort(function (a, b) { return +a - +b; });
        var preview = verses.slice(0, 6).map(function (v) { return chData[v]; }).join(' ');
        if (verses.length > 6) preview += ' …';
        var refLink = bkName + ' ' + ntCh;
        bodyEl.innerHTML =
          '<p class="daily-devot-ref">' + escHtml(refLink) + '</p>' +
          '<p class="daily-devot-text">' + escHtml(preview) + '</p>' +
          '<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(refLink)) + '">Read full chapter →</a>';
      }).catch(function () { bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load.</p>'; });
      return;
    }

    // ── Spurgeon's Morning and Evening
    if (source === 'spurgeon-morning' || source === 'spurgeon-evening') {
      var spPeriod = (source === 'spurgeon-morning') ? 'morning' : 'evening';
      var fileName = (source === 'spurgeon-morning') ? 'spurgeon-morning.json' : 'spurgeon-evening.json';
      var mm = String(now.getMonth() + 1).padStart(2, '0');
      var dd = String(now.getDate()).padStart(2, '0');
      var dateKey = mm + '-' + dd;

      if (titleEl) {
        titleEl.innerHTML = 'Spurgeon — ' + (spPeriod === 'morning' ? 'Morning' : 'Evening') +
          ' <span class="daily-period-badge">' + (spPeriod === 'morning' ? '🌅 Morning' : '🌙 Evening') + '</span>';
      }

      fetch(DAILY_DEVOT_BASE + '/' + fileName)
        .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
        .then(function (entries) {
          var entry = entries[dateKey];
          if (!entry) {
            bodyEl.innerHTML = '<p class="daily-plan-empty">No entry for today.</p>';
            return;
          }
          var ref = entry.verse_ref || '';
          var refLink = ref
            ? ' &nbsp;<a class="ref" data-ref="' + escHtml(ref) + '">' + escHtml(ref) + '</a>'
            : '';
          var paragraphs = entry.body.split('\n\n').filter(function (p) { return p.trim(); });
          var bodyHtml = paragraphs.map(function (p) {
            return '<p>' + escHtml(p.trim()) + '</p>';
          }).join('');
          bodyEl.innerHTML =
            '<blockquote class="daily-spurgeon-verse">' +
              escHtml(entry.verse_text) +
              '<cite>' + refLink + '</cite>' +
            '</blockquote>' +
            '<div class="daily-spurgeon-body">' + bodyHtml + '</div>';
          wireRefLinks(bodyEl);
        })
        .catch(function () {
          bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load Spurgeon devotional.</p>';
        });
      return;
    }

    bodyEl.innerHTML = '<p class="daily-plan-empty">Select a devotional source above.</p>';
  }

  function _dailySetupNotifications(period) {
    // Don't ask if already dismissed permanently
    if (localStorage.getItem(DAILY_NOTIF_DISMISSED) === '1') {
      _dailySchedulePeriodSwitch(period);
      return;
    }

    // Check if period changed since last stored notification
    var lastPeriod = localStorage.getItem(DAILY_NOTIF_KEY);
    if (lastPeriod && lastPeriod !== period) {
      // Period changed — if we have permission, fire a notification now
      if (typeof Notification !== 'undefined' && Notification.permission === 'granted') {
        _dailyFireNotification(period);
      }
    }
    localStorage.setItem(DAILY_NOTIF_KEY, period);

    // Show a permission request banner if not yet decided
    if (typeof Notification !== 'undefined' && Notification.permission === 'default') {
      _dailyShowNotifBanner();
    }

    _dailySchedulePeriodSwitch(period);
  }

  function _dailyShowNotifBanner() {
    var page = document.querySelector('.daily-page');
    if (!page) return;
    var banner = document.createElement('div');
    banner.className = 'daily-notif-banner';
    banner.innerHTML =
      '<span>Get notified when your morning & evening devotional changes.</span>' +
      '<button id="daily-notif-allow">Enable notifications</button>' +
      '<button class="daily-notif-dismiss" aria-label="Dismiss">✕</button>';
    page.insertBefore(banner, page.firstChild);
    banner.querySelector('#daily-notif-allow').addEventListener('click', function () {
      Notification.requestPermission().then(function (perm) {
        if (perm === 'granted') _dailyFireNotification(_dailyPeriod());
        banner.remove();
      });
    });
    banner.querySelector('.daily-notif-dismiss').addEventListener('click', function () {
      localStorage.setItem(DAILY_NOTIF_DISMISSED, '1');
      banner.remove();
    });
  }

  function _dailyFireNotification(period) {
    if (typeof Notification === 'undefined' || Notification.permission !== 'granted') return;
    var title = period === 'morning' ? 'Good morning — Daily devotional ready' : 'Good evening — Evening devotional ready';
    var body  = period === 'morning' ? 'Your morning reading and verse of the day await.' : 'Your evening reflection and devotional are ready.';
    if (navigator.serviceWorker && navigator.serviceWorker.controller) {
      navigator.serviceWorker.ready.then(function (reg) {
        reg.showNotification(title, { body: body, icon: 'favicon.svg', badge: 'favicon.svg' });
      });
    } else {
      new Notification(title, { body: body, icon: 'favicon.svg' });
    }
  }

  function _dailySchedulePeriodSwitch(currentPeriod) {
    var now    = new Date();
    var target = new Date(now.getFullYear(), now.getMonth(), now.getDate(), currentPeriod === 'morning' ? 12 : 24, 0, 0, 0);
    var ms     = target - now;
    if (ms <= 0) return;
    setTimeout(function () {
      var newPeriod = _dailyPeriod();
      localStorage.setItem(DAILY_NOTIF_KEY, newPeriod);
      if (typeof Notification !== 'undefined' && Notification.permission === 'granted') {
        _dailyFireNotification(newPeriod);
      }
      // Re-render devotional heading + content for the new period
      var devotSrc = localStorage.getItem(DAILY_DEVOT_KEY) || 'daily-psalms';
      _dailyRenderDevotional(devotSrc, newPeriod);
    }, ms);
  }

  // ── Scripture Memory ─────────────────────────────────────────────────────

  var MEMORY_KEY      = 'bsw_memory';
  var MEMORY_MODE_KEY = 'bsw_memory_mode';
  var MEMORY_URL      = _resolve('../../memorize/');

  function _memGet()      { try { return JSON.parse(localStorage.getItem(MEMORY_KEY) || '{}'); } catch (e) { return {}; } }
  function _memSet(state) { try { localStorage.setItem(MEMORY_KEY, JSON.stringify(state)); } catch (e) {} }

  function _memHas(ref) { return !!_memGet()[ref]; }

  function _memAdd(ref) {
    var state = _memGet();
    if (state[ref]) return;
    var today = _memTodayStr();
    state[ref] = { addedDate: today, interval: 1, nextReview: today, score: 0, reps: 0 };
    _memSet(state);
  }

  function _memRemove(ref) {
    var state = _memGet();
    delete state[ref];
    _memSet(state);
  }

  function _memTodayStr() {
    var d = new Date();
    return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2);
  }

  function _memIsDue(entry) {
    return _memTodayStr() >= entry.nextReview;
  }

  function _memApplyScore(entry, score) {
    var interval = entry.interval || 1;
    if      (score === 0) interval = 1;
    else if (score === 1) interval = Math.max(1, Math.ceil(interval * 1.2));
    else if (score === 2) interval = Math.max(2, Math.ceil(interval * 2.5));
    else                  interval = Math.max(4, Math.ceil(interval * 3.5));
    var next = new Date();
    next.setDate(next.getDate() + interval);
    entry.interval   = interval;
    entry.nextReview = next.getFullYear() + '-' + ('0' + (next.getMonth() + 1)).slice(-2) + '-' + ('0' + next.getDate()).slice(-2);
    entry.score      = score;
    entry.reps       = (entry.reps || 0) + 1;
    return entry;
  }

  function _memDaysUntil(dateStr) {
    var today = new Date();
    today = new Date(today.getFullYear(), today.getMonth(), today.getDate());
    var target = new Date(dateStr + 'T00:00:00');
    return Math.max(0, Math.ceil((target - today) / 86400000));
  }

  function _memRefreshModalBtn(ref) {
    var btn = _modalEl && _modalEl.querySelector('.bsw-modal__memory-btn');
    if (!btn) return;
    var has = _memHas(ref);
    btn.textContent = has ? '⭐ Memorizing' : '☆ Memorize';
    btn.classList.toggle('bsw-modal__memory-btn--active', has);
    btn._memRef = ref;
  }

  function initMemorizePage() {
    if (!document.getElementById('mem-list')) return;

    var state    = _memGet();
    var dueCount = Object.keys(state).filter(function (r) { return _memIsDue(state[r]); }).length;
    var badge    = document.getElementById('mem-due-badge');
    if (badge) {
      if (dueCount > 0) { badge.textContent = dueCount; badge.removeAttribute('hidden'); }
      else               badge.setAttribute('hidden', '');
    }

    var modeSelect = document.getElementById('mem-mode-select');
    if (modeSelect) {
      modeSelect.value = localStorage.getItem(MEMORY_MODE_KEY) || 'ref-to-text';
      modeSelect.addEventListener('change', function () {
        localStorage.setItem(MEMORY_MODE_KEY, modeSelect.value);
      });
    }

    var tabs        = document.querySelectorAll('.mem-tab');
    var browsePanel = document.getElementById('mem-browse-panel');
    var reviewPanel = document.getElementById('mem-review-panel');
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        var which = tab.getAttribute('data-tab');
        tabs.forEach(function (t) {
          t.classList.toggle('mem-tab--active', t === tab);
          t.setAttribute('aria-selected', t === tab ? 'true' : 'false');
        });
        if (which === 'browse') {
          browsePanel.removeAttribute('hidden');
          reviewPanel.setAttribute('hidden', '');
        } else {
          browsePanel.setAttribute('hidden', '');
          reviewPanel.removeAttribute('hidden');
          _memStartReview();
        }
      });
    });

    var addInput = document.getElementById('mem-add-input');
    var addBtn   = document.getElementById('mem-add-btn');
    var addError = document.getElementById('mem-add-error');
    function doAdd() {
      var raw    = (addInput && addInput.value.trim()) || '';
      if (!raw) return;
      var parsed = parseRef(raw);
      if (!parsed || !parsed.bookId) {
        if (addError) { addError.textContent = 'Could not parse — try: John 3:16'; addError.removeAttribute('hidden'); }
        return;
      }
      if (!parsed.v) {
        if (addError) { addError.textContent = 'Please enter a specific verse (e.g. John 3:16).'; addError.removeAttribute('hidden'); }
        return;
      }
      if (addError) addError.setAttribute('hidden', '');
      var ref = parsed.bookName + ' ' + parsed.ch + ':' + parsed.v;
      _memAdd(ref);
      if (addInput) addInput.value = '';
      _memRenderList();
    }
    if (addBtn)   addBtn.addEventListener('click', doAdd);
    if (addInput) addInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') doAdd(); });

    var backBtn = document.getElementById('mem-back-browse');
    if (backBtn) backBtn.addEventListener('click', function () {
      browsePanel.removeAttribute('hidden');
      reviewPanel.setAttribute('hidden', '');
      tabs.forEach(function (t) {
        var isBrowse = t.getAttribute('data-tab') === 'browse';
        t.classList.toggle('mem-tab--active', isBrowse);
        t.setAttribute('aria-selected', isBrowse ? 'true' : 'false');
      });
    });

    _memRenderList();
  }

  function _memRenderList() {
    var listEl  = document.getElementById('mem-list');
    var emptyEl = document.getElementById('mem-empty');
    if (!listEl) return;
    var state = _memGet();
    var refs  = Object.keys(state);
    if (!refs.length) {
      listEl.innerHTML = '';
      if (emptyEl) emptyEl.removeAttribute('hidden');
      return;
    }
    if (emptyEl) emptyEl.setAttribute('hidden', '');
    refs.sort(function (a, b) {
      var da = state[a].nextReview, db = state[b].nextReview;
      return da < db ? -1 : da > db ? 1 : 0;
    });
    listEl.innerHTML = '';
    refs.forEach(function (ref) {
      var entry = state[ref];
      var due   = _memIsDue(entry);
      var days  = _memDaysUntil(entry.nextReview);
      var item  = document.createElement('div');
      item.className = 'mem-item' + (due ? ' mem-item--due' : '');
      var refEl = document.createElement('span');
      refEl.className = 'mem-item__ref';
      refEl.textContent = ref;
      var statusEl = document.createElement('span');
      statusEl.className = 'mem-item__status' + (due ? ' mem-item__status--due' : '');
      statusEl.textContent = due ? 'Due today' : 'In ' + days + ' day' + (days === 1 ? '' : 's');
      var btns = document.createElement('div');
      btns.className = 'mem-item__btns';
      var reviewBtn = document.createElement('button');
      reviewBtn.className = 'mem-item__review-btn';
      reviewBtn.textContent = 'Review';
      (function (r) { reviewBtn.addEventListener('click', function () { _memReviewSingle(r); }); }(ref));
      var removeBtn = document.createElement('button');
      removeBtn.className = 'mem-item__remove-btn';
      removeBtn.textContent = '✕';
      removeBtn.title = 'Remove from memory list';
      (function (r) {
        removeBtn.addEventListener('click', function () { _memRemove(r); _memRenderList(); });
      }(ref));
      btns.appendChild(reviewBtn);
      btns.appendChild(removeBtn);
      item.appendChild(refEl);
      item.appendChild(statusEl);
      item.appendChild(btns);
      listEl.appendChild(item);
    });
    var dueCount = Object.keys(state).filter(function (r) { return _memIsDue(state[r]); }).length;
    var badge = document.getElementById('mem-due-badge');
    if (badge) {
      if (dueCount > 0) { badge.textContent = dueCount; badge.removeAttribute('hidden'); }
      else               badge.setAttribute('hidden', '');
    }
  }

  var _memQueue    = [];
  var _memQueueIdx = 0;

  function _memStartReview() {
    var state = _memGet();
    _memQueue    = Object.keys(state).filter(function (r) { return _memIsDue(state[r]); });
    _memQueueIdx = 0;
    _memShowReviewCard();
  }

  function _memReviewSingle(ref) {
    _memQueue    = [ref];
    _memQueueIdx = 0;
    var browsePanel = document.getElementById('mem-browse-panel');
    var reviewPanel = document.getElementById('mem-review-panel');
    if (browsePanel) browsePanel.setAttribute('hidden', '');
    if (reviewPanel) reviewPanel.removeAttribute('hidden');
    document.querySelectorAll('.mem-tab').forEach(function (t) {
      var isReview = t.getAttribute('data-tab') === 'review';
      t.classList.toggle('mem-tab--active', isReview);
      t.setAttribute('aria-selected', isReview ? 'true' : 'false');
    });
    _memShowReviewCard();
  }

  function _memShowReviewCard() {
    var progressEl = document.getElementById('mem-review-progress');
    var cardEl     = document.getElementById('mem-card');
    var doneEl     = document.getElementById('mem-review-done');
    if (!cardEl) return;
    if (_memQueueIdx >= _memQueue.length) {
      var n = _memQueue.length;
      if (progressEl) progressEl.innerHTML = n > 0
        ? '<span>' + n + ' of ' + n + '</span>' +
          '<div class="mem-progress-bar"><div class="mem-progress-fill" style="width:100%"></div></div>'
        : '';
      cardEl.setAttribute('hidden', '');
      if (doneEl) {
        var pEl = doneEl.querySelector('p');
        if (pEl) pEl.textContent = n === 0
          ? 'All caught up — nothing due right now.'
          : 'Session complete — well done! You reviewed ' + (n === 1 ? '1 verse' : n + ' verses') + '.';
        doneEl.removeAttribute('hidden');
      }
      var badge = document.getElementById('mem-due-badge');
      if (badge) badge.setAttribute('hidden', '');
      return;
    }
    if (doneEl) doneEl.setAttribute('hidden', '');
    cardEl.removeAttribute('hidden');
    var total = _memQueue.length, done = _memQueueIdx;
    if (progressEl) {
      progressEl.innerHTML =
        '<span>' + (done + 1) + ' of ' + total + '</span>' +
        '<div class="mem-progress-bar"><div class="mem-progress-fill" style="width:' +
        Math.round(done / total * 100) + '%"></div></div>';
    }
    var ref     = _memQueue[_memQueueIdx];
    var mode    = localStorage.getItem(MEMORY_MODE_KEY) || 'ref-to-text';
    var frontEl = document.getElementById('mem-card-front');
    var backEl  = document.getElementById('mem-card-back');
    var actsEl  = document.getElementById('mem-card-actions');
    if (!frontEl) return;
    backEl.setAttribute('hidden', '');
    actsEl.setAttribute('hidden', '');
    frontEl.removeAttribute('hidden');

    if (mode === 'ref-to-text') {
      frontEl.innerHTML =
        '<p class="mem-card__label">Reference</p>' +
        '<p class="mem-card__ref">' + escHtml(ref) + '</p>' +
        '<p class="mem-card__hint">Recall the verse text, then reveal.</p>' +
        '<button class="mem-show-btn" id="mem-show-answer">Show Answer</button>';
      _memWireShowBtn(ref, mode, null);
    } else {
      frontEl.innerHTML = '<p class="mem-card__hint" style="font-size:.85rem">Loading…</p>';
      var parsed = parseRef(ref);
      if (parsed && parsed.bookId) {
        loadBook(getVersion(), parsed.bookId).then(function (chs) {
          var text = chs && chs[String(parsed.ch)] && chs[String(parsed.ch)][String(parsed.v)];
          frontEl.innerHTML =
            '<p class="mem-card__label">Verse Text</p>' +
            '<p class="mem-card__verse-text">&ldquo;' + escHtml(text || ref) + '&rdquo;</p>' +
            '<p class="mem-card__hint">Recall the reference, then reveal.</p>' +
            '<button class="mem-show-btn" id="mem-show-answer">Show Answer</button>';
          _memWireShowBtn(ref, mode, text);
        }).catch(function () {
          frontEl.innerHTML = '<p class="mem-card__ref">' + escHtml(ref) + '</p>' +
            '<button class="mem-show-btn" id="mem-show-answer">Show Answer</button>';
          _memWireShowBtn(ref, mode, null);
        });
      }
    }
  }

  function _memWireShowBtn(ref, mode, cachedText) {
    var showBtn = document.getElementById('mem-show-answer');
    if (!showBtn) return;
    showBtn.addEventListener('click', function () {
      var frontEl = document.getElementById('mem-card-front');
      var backEl  = document.getElementById('mem-card-back');
      var actsEl  = document.getElementById('mem-card-actions');
      function renderAnswer(text) {
        if (mode === 'ref-to-text') {
          backEl.innerHTML =
            '<p class="mem-card__verse-text">&ldquo;' + escHtml(text || '(verse unavailable)') + '&rdquo;</p>' +
            '<p class="mem-card__verse-ref">' + escHtml(ref) + '</p>';
        } else {
          backEl.innerHTML =
            '<p class="mem-card__label">Reference</p><p class="mem-card__ref">' + escHtml(ref) + '</p>';
        }
        if (frontEl) frontEl.setAttribute('hidden', '');
        backEl.removeAttribute('hidden');
        actsEl.removeAttribute('hidden');
        _memWireRatingBtns(ref);
      }
      if (cachedText) { renderAnswer(cachedText); return; }
      var parsed = parseRef(ref);
      if (parsed && parsed.bookId) {
        loadBook(getVersion(), parsed.bookId).then(function (chs) {
          renderAnswer(chs && chs[String(parsed.ch)] && chs[String(parsed.ch)][String(parsed.v)]);
        }).catch(function () { renderAnswer(null); });
      } else { renderAnswer(null); }
    });
  }

  function _memWireRatingBtns(ref) {
    var actsEl = document.getElementById('mem-card-actions');
    if (!actsEl) return;
    actsEl.querySelectorAll('.mem-rate-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var score = parseInt(btn.getAttribute('data-score'), 10);
        var state = _memGet();
        if (state[ref]) { state[ref] = _memApplyScore(state[ref], score); _memSet(state); }
        _memQueueIdx++;
        _memShowReviewCard();
        _memRenderList();
      }, { once: true });
    });
  }

  // ── Nave's Topical Bible ──────────────────────────────────────────────────

  var NAVE_URL       = _resolve('../../data/topical/nave.json');
  var NAVE_VIDX_ROOT = _resolve('../../data/topical/verse-index');
  var TOPICAL_URL    = _resolve('../../topical/');

  var _naveData      = null;   // [{slug, title, verses}]
  var _naveMap       = null;   // slug → topic object
  var _naveByLetter  = null;   // letter → [{slug, title, verses}]
  var _naveLoading   = null;   // Promise<void>
  var _naveVidxCache = {};     // bookId → {ch:v → [slug,...]}

  function _naveLoad() {
    if (_naveLoading) return _naveLoading;
    _naveLoading = fetch(NAVE_URL)
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (data) {
        _naveData = data;
        _naveMap  = {};
        _naveByLetter = {};
        data.forEach(function (t) {
          _naveMap[t.slug] = t;
          var letter = t.title.charAt(0).toUpperCase();
          if (!_naveByLetter[letter]) _naveByLetter[letter] = [];
          _naveByLetter[letter].push(t);
        });
      });
    return _naveLoading;
  }

  function _naveLoadVidx(bookId) {
    if (_naveVidxCache[bookId] !== undefined) return Promise.resolve(_naveVidxCache[bookId]);
    return fetch(NAVE_VIDX_ROOT + '/' + bookId + '.json')
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { _naveVidxCache[bookId] = d || {}; return _naveVidxCache[bookId]; })
      .catch(function () { _naveVidxCache[bookId] = {}; return {}; });
  }

  // Returns [{slug, title, verses}] for a given verse ref (parsed object)
  function _naveTopicsForVerse(parsed) {
    if (!parsed || !parsed.bookId || !parsed.v) return Promise.resolve([]);
    return Promise.all([_naveLoad(), _naveLoadVidx(parsed.bookId)]).then(function () {
      var key   = parsed.ch + ':' + parsed.v;
      var vidx  = _naveVidxCache[parsed.bookId] || {};
      var slugs = vidx[key] || [];
      return slugs.map(function (s) { return _naveMap && _naveMap[s]; }).filter(Boolean);
    });
  }

  // ── Topical browse page ───────────────────────────────────────────────────
  function initTopicalPage() {
    var listEl       = document.getElementById('topical-list');
    var loadingEl    = document.getElementById('topical-loading');
    var emptyEl      = document.getElementById('topical-empty');
    var detailColEl  = document.getElementById('topical-detail-col');
    var detailEl     = document.getElementById('topical-detail');
    var alphaEl      = document.getElementById('topical-alpha');
    var searchEl     = document.getElementById('topical-search');
    var countEl      = document.getElementById('topical-search-count');
    if (!listEl) return;

    var _activeLetter = '';
    var _activeTopic  = null;

    function renderDetailPanel(topic) {
      _activeTopic = topic;
      detailColEl.removeAttribute('hidden');
      var MAX_READ = 120;
      var readVerses = topic.verses.length > MAX_READ ? topic.verses.slice(0, MAX_READ) : topic.verses;
      var readUrl = READER_URL + '?ref=' + encodeURIComponent(readVerses.join(', '));
      var readLabel = topic.verses.length > MAX_READ
        ? 'Read first ' + MAX_READ + ' verses →'
        : 'Read all ' + topic.verses.length + ' verses →';
      detailEl.innerHTML =
        '<div class="topical-detail__head">' +
          '<h2 class="topical-detail__title">' + escHtml(topic.title) + '</h2>' +
          '<div class="topical-detail__meta-row">' +
            '<p class="topical-detail__meta">' + topic.verses.length + ' scripture reference' +
              (topic.verses.length !== 1 ? 's' : '') + '</p>' +
            '<a class="topical-read-all" href="' + escHtml(readUrl) + '">' + readLabel + '</a>' +
          '</div>' +
        '</div>' +
        '<div class="topical-detail__body">' +
          '<div class="topical-refs">' +
            topic.verses.map(function (ref) {
              return '<a class="topical-ref-chip ref" data-ref="' + escHtml(ref) + '">' + escHtml(ref) + '</a>';
            }).join('') +
          '</div>' +
        '</div>';
      wireRefLinks(detailEl);
    }

    function renderList(topics) {
      if (!topics || !topics.length) {
        listEl.innerHTML = '';
        emptyEl.removeAttribute('hidden');
        return;
      }
      emptyEl.setAttribute('hidden', '');
      listEl.innerHTML = topics.map(function (t) {
        var isActive = _activeTopic && _activeTopic.slug === t.slug;
        return '<div class="topical-item' + (isActive ? ' topical-item--active' : '') +
          '" data-slug="' + escHtml(t.slug) + '">' +
          '<span class="topical-item__title">' + escHtml(t.title) + '</span>' +
          '<span class="topical-item__count">' + t.verses.length + '</span>' +
          '</div>';
      }).join('');
      listEl.querySelectorAll('.topical-item').forEach(function (item) {
        item.addEventListener('click', function () {
          var slug  = item.getAttribute('data-slug');
          var topic = _naveMap && _naveMap[slug];
          if (!topic) return;
          listEl.querySelectorAll('.topical-item').forEach(function (el) {
            el.classList.remove('topical-item--active');
          });
          item.classList.add('topical-item--active');
          renderDetailPanel(topic);
          // Update URL without full navigation
          var url = new URL(window.location.href);
          url.searchParams.set('topic', slug);
          history.replaceState(null, '', url.toString());
        });
      });
    }

    function buildAlphaBar(byLetter) {
      var letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
      alphaEl.innerHTML = '';
      letters.forEach(function (letter) {
        var btn = document.createElement('button');
        btn.className = 'topical-alpha-btn' +
          (letter === _activeLetter ? ' topical-alpha-btn--active' : '') +
          (!byLetter[letter] ? ' topical-alpha-btn--empty' : '');
        btn.textContent = letter;
        btn.setAttribute('role', 'tab');
        btn.setAttribute('aria-selected', letter === _activeLetter ? 'true' : 'false');
        btn.addEventListener('click', function () {
          if (!byLetter[letter]) return;
          _activeLetter = letter;
          if (searchEl) { searchEl.value = ''; }
          if (countEl) countEl.setAttribute('hidden', '');
          alphaEl.querySelectorAll('.topical-alpha-btn').forEach(function (b) {
            b.classList.toggle('topical-alpha-btn--active', b.textContent === letter);
            b.setAttribute('aria-selected', b.textContent === letter ? 'true' : 'false');
          });
          renderList(byLetter[letter] || []);
        });
        alphaEl.appendChild(btn);
      });
    }

    _naveLoad().then(function () {
      if (loadingEl) loadingEl.setAttribute('hidden', '');

      buildAlphaBar(_naveByLetter);

      // URL params: ?topic=slug or ?q=query
      var params       = new URLSearchParams(window.location.search);
      var topicParam   = params.get('topic') || '';
      var queryParam   = params.get('q')     || '';

      if (topicParam && _naveMap && _naveMap[topicParam]) {
        var topic = _naveMap[topicParam];
        var letter = topic.title.charAt(0).toUpperCase();
        _activeLetter = letter;
        buildAlphaBar(_naveByLetter);
        renderList(_naveByLetter[letter] || []);
        renderDetailPanel(topic);
        // Scroll the item into view
        setTimeout(function () {
          var el = listEl.querySelector('[data-slug="' + topicParam + '"]');
          if (el) el.scrollIntoView({ block: 'nearest' });
        }, 50);
      } else if (queryParam) {
        if (searchEl) searchEl.value = queryParam;
        var results = _naveData.filter(function (t) {
          return t.title.toLowerCase().indexOf(queryParam.toLowerCase()) !== -1;
        });
        if (countEl) { countEl.textContent = results.length + ' topics'; countEl.removeAttribute('hidden'); }
        renderList(results);
      } else {
        // Default: show letter A
        var firstLetter = Object.keys(_naveByLetter).sort()[0] || 'A';
        _activeLetter = firstLetter;
        buildAlphaBar(_naveByLetter);
        renderList(_naveByLetter[firstLetter] || []);
      }

      // Show placeholder in detail panel if nothing selected
      if (!_activeTopic) {
        detailColEl.removeAttribute('hidden');
        detailEl.innerHTML = '<p class="topical-detail-placeholder">Select a topic to see its scripture references.</p>';
      }
    }).catch(function () {
      if (loadingEl) loadingEl.textContent = 'Could not load topic data.';
    });

    // Search
    if (searchEl) {
      searchEl.addEventListener('input', function () {
        var q = searchEl.value.trim().toLowerCase();
        if (!_naveData) return;
        if (!q) {
          if (countEl) countEl.setAttribute('hidden', '');
          renderList(_naveByLetter[_activeLetter] || []);
          return;
        }
        var results = _naveData.filter(function (t) {
          return t.title.toLowerCase().indexOf(q) !== -1;
        });
        if (countEl) { countEl.textContent = results.length + ' topics'; countEl.removeAttribute('hidden'); }
        renderList(results);
      });
    }
  }

  // ── Topical tab in verse modal ─────────────────────────────────────────────
  function renderModalTopics(parsed, container) {
    container.innerHTML = '<p class="topical-modal-empty">Loading…</p>';
    _naveTopicsForVerse(parsed).then(function (topics) {
      if (!topics.length) {
        container.innerHTML = '<p class="topical-modal-empty">No Nave\'s topics found for this verse.</p>';
        return;
      }
      var browseUrl = escHtml(TOPICAL_URL);
      var label = topics.length === 1 ? '1 topic' : topics.length + ' topics';
      var html =
        '<p class="topical-modal-meta">' +
          '<span>' + label + ' in Nave\'s Topical Bible</span>' +
          '<a class="topical-modal-browse" href="' + browseUrl + '">Browse all →</a>' +
        '</p>' +
        '<div class="topical-modal-chips">';
      topics.forEach(function (t) {
        html += '<a class="topical-modal-chip" href="' +
          escHtml(TOPICAL_URL + '?topic=' + encodeURIComponent(t.slug)) + '">' +
          escHtml(t.title) +
          '<span class="topical-modal-chip__count">' + t.verses.length + '</span>' +
          '</a>';
      });
      html += '</div>';
      container.innerHTML = html;
    }).catch(function () {
      container.innerHTML = '<p class="topical-modal-empty">Could not load topic data.</p>';
    });
    container._topicsLoaded = true;
  }

  // ── Confessions modal tab ───────────────────────────────────────────────────
  var _LIB_VERSE_IDX_BASE = _resolve('../../data/library/verse-index');
  var _libVerseCache       = {};

  function renderModalConfessions(parsed, container) {
    container._confLoaded = true;
    if (!parsed || !parsed.bookId) {
      container.innerHTML = '<p class="bsw-modal-topics-empty">No verse selected.</p>';
      return;
    }
    container.innerHTML = '<p class="bsw-modal-topics-empty">Loading…</p>';

    var bookId = parsed.bookId;
    var ch     = String(parsed.ch);
    var v      = String(parsed.v);

    var url = _LIB_VERSE_IDX_BASE + '/' + bookId + '.json';
    (_libVerseCache[bookId]
      ? Promise.resolve(_libVerseCache[bookId])
      : fetch(url).then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
          .then(function (d) { _libVerseCache[bookId] = d; return d; })
    ).then(function (data) {
      var citations = (data[ch] && data[ch][v]) || [];
      if (!citations.length) {
        container.innerHTML = '<p class="bsw-modal-topics-empty">No confessional citations for this verse.</p>';
        return;
      }
      // Group by document abbreviation
      var byDoc = {};
      citations.forEach(function (c) {
        if (!byDoc[c.doc]) byDoc[c.doc] = [];
        byDoc[c.doc].push(c);
      });
      var html = '<div class="bsw-modal-confessions">';
      Object.keys(byDoc).forEach(function (doc) {
        html += '<div class="bsw-conf-group">';
        html += '<div class="bsw-conf-group__doc">' + escHtml(doc) + '</div>';
        byDoc[doc].forEach(function (c) {
          var refLabel = c.doc + ' ' + c.section;
          var href = READER_URL + '?ref=' + encodeURIComponent(refLabel);
          html += '<a class="bsw-conf-item" href="' + escHtml(href) + '">' +
            '<span class="bsw-conf-item__ref">' + escHtml(refLabel) + '</span>' +
            '<span class="bsw-conf-item__text">' + escHtml(c.heading) + '</span>' +
          '</a>';
        });
        html += '</div>';
      });
      html += '</div>';
      container.innerHTML = html;
    }).catch(function () {
      container.innerHTML = '<p class="bsw-modal-topics-empty">Could not load confessional data.</p>';
    });
  }

  // ── Topical section in Verse Study page ─────────────────────────────────────
  function renderVSTopics(parsed, container) {
    container.innerHTML = '<p class="topical-modal-empty">Loading…</p>';
    _naveTopicsForVerse(parsed).then(function (topics) {
      if (!topics.length) {
        container.innerHTML = '<p class="topical-modal-empty">No Nave\'s topics for this verse.</p>';
        return;
      }
      var html = '<div class="vs-topical-list">';
      topics.forEach(function (t) {
        html += '<a class="vs-topical-item" href="' +
          escHtml(TOPICAL_URL + '?topic=' + encodeURIComponent(t.slug)) + '">' +
          escHtml(t.title) +
          '<span class="vs-topical-count">' + t.verses.length + '</span>' +
          '</a>';
      });
      html += '</div>';
      container.innerHTML = html;
    }).catch(function () {
      container.innerHTML = '<p class="topical-modal-empty">Could not load topic data.</p>';
    });
  }

  // ── Easton's Bible Dictionary ─────────────────────────────────────────────

  var DICT_IDX_URL   = _resolve('../../data/dictionary/index.json');
  var DICT_ENTRY_URL = _resolve('../../data/dictionary/');          // + slug + '.json'
  var DICT_VIDX_URL  = _resolve('../../data/dictionary/verse-index/');
  var DICT_PAGE_URL  = _resolve('../../dictionary/');

  var _dictData     = null;   // [{id, term, brief}]
  var _dictMap      = null;   // id → {id, term, brief}
  var _dictByLetter = null;   // letter → [{id, term, brief}]
  var _dictLoading  = null;   // Promise<void>
  var _dictEntryCache = {};   // slug → {id, term, html, refs, source}
  var _dictVidxCache  = {};   // bookId → {ch: {v: [{id, term}]}}

  function _dictLoad() {
    if (_dictLoading) return _dictLoading;
    _dictLoading = fetch(DICT_IDX_URL)
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (data) {
        _dictData     = data;
        _dictMap      = {};
        _dictByLetter = {};
        data.forEach(function (e) {
          _dictMap[e.id] = e;
          var letter = e.term.charAt(0).toUpperCase();
          if (!_dictByLetter[letter]) _dictByLetter[letter] = [];
          _dictByLetter[letter].push(e);
        });
      });
    return _dictLoading;
  }

  function _dictLoadEntry(slug) {
    if (_dictEntryCache[slug]) return Promise.resolve(_dictEntryCache[slug]);
    return fetch(DICT_ENTRY_URL + slug + '.json')
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (d) { _dictEntryCache[slug] = d; return d; });
  }

  function _dictLoadVidx(bookId) {
    if (_dictVidxCache[bookId] !== undefined) return Promise.resolve(_dictVidxCache[bookId]);
    return fetch(DICT_VIDX_URL + bookId + '.json')
      .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
      .then(function (d) { _dictVidxCache[bookId] = d || {}; return d; })
      .catch(function () { _dictVidxCache[bookId] = {}; return {}; });
  }

  function _dictEntriesForVerse(parsed) {
    if (!parsed || !parsed.bookId || !parsed.ch || !parsed.v) return Promise.resolve([]);
    return _dictLoadVidx(parsed.bookId).then(function (vidx) {
      var ch   = String(parsed.ch);
      var v    = String(parsed.v);
      return (vidx[ch] && vidx[ch][v]) || [];
    });
  }

  // Render VS1 Dictionary section
  function renderVSDictionary(parsed, container) {
    container.innerHTML = '<p class="dict-modal-empty">Loading…</p>';
    _dictEntriesForVerse(parsed).then(function (entries) {
      if (!entries.length) {
        container.innerHTML = '<p class="dict-modal-empty">No dictionary entries for this verse.</p>';
        return;
      }
      var html = '<div class="vs-dict-list">';
      entries.forEach(function (e) {
        var href = DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id);
        html += '<a class="vs-dict-item" href="' + escHtml(href) + '">' +
          '<span class="vs-dict-item__term">' + escHtml(e.term) + '</span>' +
          '<span class="vs-dict-item__arrow">&#x2192;</span>' +
          '</a>';
      });
      html += '</div>';
      container.innerHTML = html;
    }).catch(function () {
      container.innerHTML = '<p class="dict-modal-empty">Could not load dictionary data.</p>';
    });
  }

  // Render modal Dictionary tab — shows brief definitions inline
  function renderModalDictionary(parsed, container) {
    container._dictLoaded = true;
    if (!parsed || !parsed.v) {
      container.innerHTML = '<p class="dict-modal-empty">No verse selected.</p>';
      return;
    }
    container.innerHTML = '<p class="dict-modal-empty">Loading…</p>';
    _dictEntriesForVerse(parsed).then(function (entries) {
      if (!entries.length) {
        container.innerHTML = '<p class="dict-modal-empty">No dictionary entries for this verse.</p>';
        return;
      }
      var html = '';
      entries.forEach(function (e) {
        var href = DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id);
        var meta = _dictMap && _dictMap[e.id];
        var brief = meta ? meta.brief : '';
        // Trim brief to first sentence or 120 chars
        if (brief) {
          var dot = brief.indexOf('. ', 40);
          if (dot > 0 && dot < 140) brief = brief.slice(0, dot + 1);
          else if (brief.length > 130) brief = brief.slice(0, 127) + '…';
        }
        html += '<div class="bsw-dict-panel-entry">' +
          '<p class="bsw-dict-panel-entry__term">' + escHtml(e.term) + '</p>' +
          (brief ? '<p class="bsw-dict-panel-entry__brief">' + escHtml(brief) + '</p>' : '') +
          '<a class="bsw-dict-panel-entry__link" href="' + escHtml(href) + '">Full entry &#x2192;</a>' +
          '</div>';
      });
      html += '<p style="margin-top:.75rem;font-size:.75rem;">' +
        '<a class="bsw-dict-panel-entry__link" href="' + escHtml(DICT_PAGE_URL) + '">Browse full dictionary &#x2192;</a></p>';
      container.innerHTML = html;
    }).catch(function () {
      container.innerHTML = '<p class="dict-modal-empty">Could not load dictionary data.</p>';
    });
  }

  // ── Dictionary standalone page ────────────────────────────────────────────
  function initDictionaryPage() {
    var listEl      = document.getElementById('dict-list');
    var loadingEl   = document.getElementById('dict-loading');
    var emptyEl     = document.getElementById('dict-empty');
    var detailColEl = document.getElementById('dict-detail-col');
    var detailEl    = document.getElementById('dict-detail');
    var alphaEl     = document.getElementById('dict-alpha');
    var searchEl    = document.getElementById('dict-search');
    var countEl     = document.getElementById('dict-search-count');
    if (!listEl) return;

    var _activeLetter = null;
    var _activeSlug   = null;

    function showDetail(entry) {
      _activeSlug = entry.id;
      detailColEl.removeAttribute('hidden');

      // Update active state in list
      listEl.querySelectorAll('.dict-item').forEach(function (el) {
        el.classList.toggle('dict-item--active', el.dataset.id === entry.id);
      });

      // Header
      detailEl.innerHTML =
        '<div class="dict-detail__head">' +
          '<h2 class="dict-detail__title">' + escHtml(entry.term) + '</h2>' +
          '<p class="dict-detail__meta">' + escHtml(entry.source || "Easton's Bible Dictionary (1897)") + '</p>' +
        '</div>' +
        '<div class="dict-detail__body"><p class="dict-loading">Loading…</p></div>';

      _dictLoadEntry(entry.id).then(function (full) {
        var body = detailEl.querySelector('.dict-detail__body');
        var refsHtml = '';
        if (full.refs && full.refs.length) {
          refsHtml =
            '<div class="dict-detail__refs">' +
              '<p class="dict-detail__refs-label">Scripture References</p>' +
              '<div class="dict-detail__ref-chips">' +
              full.refs.map(function (r) {
                return '<a class="dict-ref-chip ref" data-ref="' + escHtml(r) + '">' + escHtml(r) + '</a>';
              }).join('') +
              '</div>' +
            '</div>';
        }
        body.innerHTML = full.html + refsHtml;
        wireRefLinks(body);
      }).catch(function () {
        var body = detailEl.querySelector('.dict-detail__body');
        if (body) body.innerHTML = '<p>Could not load entry.</p>';
      });
    }

    function renderList(entries) {
      if (!entries || !entries.length) {
        listEl.innerHTML = '';
        emptyEl.removeAttribute('hidden');
        return;
      }
      emptyEl.setAttribute('hidden', '');
      listEl.innerHTML = entries.map(function (e) {
        return '<div class="dict-item' + (e.id === _activeSlug ? ' dict-item--active' : '') +
          '" data-id="' + escHtml(e.id) + '">' +
          '<span class="dict-item__title">' + escHtml(e.term) + '</span>' +
          '</div>';
      }).join('');

      listEl.querySelectorAll('.dict-item').forEach(function (item) {
        item.addEventListener('click', function () {
          var id    = item.dataset.id;
          var entry = _dictMap && _dictMap[id];
          if (!entry) return;
          listEl.querySelectorAll('.dict-item').forEach(function (el) {
            el.classList.remove('dict-item--active');
          });
          item.classList.add('dict-item--active');
          showDetail(entry);
        });
      });
    }

    function buildAlphaBar(byLetter) {
      alphaEl.innerHTML = '';
      'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach(function (letter) {
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'dict-alpha-btn' +
          (letter === _activeLetter ? ' dict-alpha-btn--active' : '') +
          (!byLetter[letter] ? ' dict-alpha-btn--empty' : '');
        btn.textContent = letter;
        if (byLetter[letter]) {
          btn.addEventListener('click', function () {
            _activeLetter = letter;
            searchEl.value = '';
            if (countEl) { countEl.setAttribute('hidden', ''); }
            alphaEl.querySelectorAll('.dict-alpha-btn').forEach(function (b) {
              b.classList.toggle('dict-alpha-btn--active', b.textContent === letter);
            });
            renderList(byLetter[letter] || []);
          });
        }
        alphaEl.appendChild(btn);
      });
    }

    _dictLoad().then(function () {
      if (loadingEl) loadingEl.setAttribute('hidden', '');

      // Check for ?entry=slug param
      var entryParam = new URLSearchParams(window.location.search).get('entry');
      var firstLetter = Object.keys(_dictByLetter).sort()[0] || 'A';

      if (entryParam && _dictMap && _dictMap[entryParam]) {
        var entry  = _dictMap[entryParam];
        var letter = entry.term.charAt(0).toUpperCase();
        _activeLetter = letter;
        buildAlphaBar(_dictByLetter);
        renderList(_dictByLetter[letter] || []);
        showDetail(entry);
      } else {
        _activeLetter = firstLetter;
        buildAlphaBar(_dictByLetter);
        renderList(_dictByLetter[firstLetter] || []);
        detailEl.innerHTML = '<p class="dict-detail-placeholder">Select an entry to read its definition.</p>';
      }

      if (searchEl) {
        searchEl.addEventListener('input', function () {
          var q = searchEl.value.trim().toLowerCase();
          if (!q) {
            if (countEl) countEl.setAttribute('hidden', '');
            _activeLetter = firstLetter;
            buildAlphaBar(_dictByLetter);
            renderList(_dictByLetter[firstLetter] || []);
            return;
          }
          var results = _dictData.filter(function (e) {
            return e.term.toLowerCase().includes(q) || e.brief.toLowerCase().includes(q);
          });
          if (countEl) {
            countEl.textContent = results.length + ' result' + (results.length !== 1 ? 's' : '');
            countEl.removeAttribute('hidden');
          }
          _activeLetter = null;
          buildAlphaBar(_dictByLetter);
          renderList(results.slice(0, 200));
        });
      }
    }).catch(function () {
      if (loadingEl) loadingEl.textContent = 'Failed to load dictionary.';
    });
  }

  // ── Term hover tooltip (site-wide noun/concept linking) ───────────────────

  var _termTipEl      = null;
  var _termTipTimer   = null;
  var _termTipHide    = null;
  var _termMap2       = null;   // lowercase → {term, dictId?, dictBrief?, naveSlugs[]}
  var _termMapReady   = null;   // Promise
  var _termMultiRe    = null;   // Regex for multi-word terms
  var _termSingleSet  = null;   // Set of lowercase single-word proper nouns

  function _buildTermTooltipDOM() {
    if (_termTipEl) return;
    var el = document.createElement('div');
    el.id        = 'bsw-term-tooltip';
    el.className = 'bsw-term-tooltip';
    el.setAttribute('aria-hidden', 'true');
    document.body.appendChild(el);
    _termTipEl = el;
    el.addEventListener('mouseenter', function () { cancelTermHide(); });
    el.addEventListener('mouseleave', function () { _scheduleTermHide(); });
  }

  function _scheduleTermShow(anchor, key) {
    cancelTermHide();
    if (_termTipTimer) clearTimeout(_termTipTimer);
    _termTipTimer = setTimeout(function () { _showTermTip(anchor, key); }, 250);
  }

  function _scheduleTermHide() {
    if (_termTipTimer) { clearTimeout(_termTipTimer); _termTipTimer = null; }
    _termTipHide = setTimeout(function () { _hideTermTip(); }, 180);
  }

  function cancelTermHide() {
    if (_termTipHide) { clearTimeout(_termTipHide); _termTipHide = null; }
  }

  function _hideTermTip() {
    if (_termTipEl) {
      _termTipEl.classList.remove('bsw-term-tooltip--visible');
      _termTipEl.setAttribute('aria-hidden', 'true');
    }
  }

  function _positionTermTip(anchor) {
    if (!_termTipEl) return;
    var r  = anchor.getBoundingClientRect();
    var tt = _termTipEl.getBoundingClientRect();
    var vw = window.innerWidth;
    var vh = window.innerHeight;
    var top  = r.bottom + 8;
    var left = r.left;
    if (top + tt.height > vh - 8)  top  = r.top - tt.height - 8;
    if (left + tt.width > vw - 8)  left = vw - tt.width - 8;
    if (left < 8) left = 8;
    _termTipEl.style.top  = top  + 'px';
    _termTipEl.style.left = left + 'px';
  }

  function _showTermTip(anchor, key) {
    _buildTermTooltipDOM();
    var entry = _termMap2 && _termMap2[key];
    if (!entry) return;

    var src = [];
    if (entry.dictId)     src.push("Easton's");
    if (entry.naveSlugs && entry.naveSlugs.length) src.push("Nave's");

    var html =
      '<div class="bsw-term-tooltip__head">' +
        '<span class="bsw-term-tooltip__term">' + escHtml(entry.term) + '</span>' +
        '<span class="bsw-term-tooltip__src">' + escHtml(src.join(' · ')) + '</span>' +
      '</div>' +
      '<div class="bsw-term-tooltip__body">';

    if (entry.dictBrief) {
      var brief = entry.dictBrief;
      var dot = brief.indexOf('. ', 50);
      if (dot > 0 && dot < 160) brief = brief.slice(0, dot + 1);
      else if (brief.length > 120) brief = brief.slice(0, 117) + '…';
      html += '<p class="bsw-term-tooltip__brief">' + escHtml(brief) + '</p>';
    }

    if (entry.naveSlugs && entry.naveSlugs.length) {
      html += '<div class="bsw-term-tooltip__nave"><p class="bsw-term-tooltip__nave-label">Nave\'s Topics</p><div class="bsw-term-tooltip__nave-chips">';
      entry.naveSlugs.slice(0, 4).forEach(function (ns) {
        var t = _naveMap && _naveMap[ns];
        if (!t) return;
        var href = TOPICAL_URL + '?topic=' + encodeURIComponent(t.slug);
        html += '<a class="bsw-term-tooltip__nave-chip" href="' + escHtml(href) + '">' +
          escHtml(t.title.charAt(0) + t.title.slice(1).toLowerCase()) +
          ' <span style="opacity:.6">(' + t.verses.length + ')</span></a>';
      });
      html += '</div></div>';
    }

    html += '<div class="bsw-term-tooltip__links">';
    if (entry.dictId) {
      var dHref = DICT_PAGE_URL + '?entry=' + encodeURIComponent(entry.dictId);
      html += '<a class="bsw-term-tooltip__link" href="' + escHtml(dHref) + '">Dictionary &#x2192;</a>';
    }
    if (entry.naveSlugs && entry.naveSlugs.length) {
      var nHref = TOPICAL_URL + '?topic=' + encodeURIComponent(entry.naveSlugs[0]);
      html += '<a class="bsw-term-tooltip__link" href="' + escHtml(nHref) + '">Topics &#x2192;</a>';
    }
    html += '</div></div>';

    _termTipEl.innerHTML = html;
    _termTipEl.classList.add('bsw-term-tooltip--visible');
    _termTipEl.setAttribute('aria-hidden', 'false');
    _positionTermTip(anchor);
  }

  // Build combined dict+nave lookup map
  function _loadTermMap() {
    if (_termMap2) return Promise.resolve(_termMap2);
    if (_termMapReady) return _termMapReady;
    _termMapReady = Promise.all([_dictLoad(), _naveLoad()]).then(function () {
      var map  = {};
      var multi = [];

      if (_dictData) {
        _dictData.forEach(function (e) {
          var k = e.term.toLowerCase();
          if (!map[k]) map[k] = { term: e.term, naveSlugs: [] };
          map[k].dictId    = e.id;
          map[k].dictBrief = e.brief;
        });
      }

      if (_naveData) {
        _naveData.forEach(function (t) {
          // Nave titles are ALLCAPS — convert to Title Case for matching
          var title = t.title.charAt(0) + t.title.slice(1).toLowerCase();
          var k = title.toLowerCase();
          if (!map[k]) map[k] = { term: title, naveSlugs: [] };
          else if (!map[k].term) map[k].term = title;
          map[k].naveSlugs.push(t.slug);
        });
      }

      _termMap2 = map;

      // Build multi-word regex (longest first)
      var multiKeys = Object.keys(map).filter(function (k) {
        return k.indexOf(' ') >= 0 && k.length >= 4;
      }).sort(function (a, b) { return b.length - a.length; });

      if (multiKeys.length) {
        var escaped = multiKeys.map(function (k) {
          return k.replace(/[-[\]{}()*+?.,\\^$|#]/g, '\\$&');
        });
        try {
          _termMultiRe = new RegExp('\\b(' + escaped.join('|') + ')\\b', 'gi');
        } catch (e) {
          _termMultiRe = null;
        }
      }

      // Single-word set: only proper nouns (will be checked for capitalization at tag time)
      _termSingleSet = new Set(Object.keys(map).filter(function (k) {
        return k.indexOf(' ') < 0 && k.length >= 3;
      }));

      return map;
    });
    return _termMapReady;
  }

  // Wire a single .term or .term-link element
  function _wireTermEl(el) {
    if (el._termWired) return;
    el._termWired = true;
    var key = (el.dataset.termKey || el.textContent || '').toLowerCase().trim();
    el.addEventListener('mouseenter', function () { _scheduleTermShow(el, key); });
    el.addEventListener('mouseleave', function () { _scheduleTermHide(); });
    el.addEventListener('click', function (e) {
      if (_termTipEl && _termTipEl.classList.contains('bsw-term-tooltip--visible')) {
        _hideTermTip();
        // Don't prevent default — allow any href on the element
      }
    });
  }

  // Tag text nodes in root with .term-link spans
  function autoTagTerms(root) {
    if (!_termMap2) return;
    if (!root) return;
    if (root._termsTagged) return;
    root._termsTagged = true;

    // Containers to skip entirely
    var skipTags = new Set(['script','style','svg','canvas','select','option','textarea','input','button','a']);

    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        var p = node.parentElement;
        if (!p) return NodeFilter.FILTER_REJECT;
        var tag = p.tagName.toLowerCase();
        if (skipTags.has(tag)) return NodeFilter.FILTER_REJECT;
        if (p.closest('a, .term-link, [data-ref], .bsw-tooltip, .bsw-term-tooltip, .site-sidebar, nav, footer')) {
          return NodeFilter.FILTER_REJECT;
        }
        if (!node.textContent.trim()) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    var nodes = [];
    var node;
    while ((node = walker.nextNode())) nodes.push(node);

    nodes.forEach(function (textNode) {
      _tagTextNode(textNode);
    });

    // Wire any pre-existing .term elements in root
    root.querySelectorAll('.term, .term-link').forEach(_wireTermEl);
  }

  function _tagTextNode(textNode) {
    var text = textNode.textContent;
    if (text.length < 3) return;

    var modified = false;
    var html     = '';
    var last     = 0;

    // Step 1: find multi-word phrase matches
    if (_termMultiRe) {
      _termMultiRe.lastIndex = 0;
      var mResult;
      while ((mResult = _termMultiRe.exec(text)) !== null) {
        var matchStr = mResult[0];
        var pos      = mResult.index;
        var key      = matchStr.toLowerCase();
        if (_termMap2[key]) {
          html += escHtml(text.slice(last, pos));
          html += '<span class="term-link" data-term-key="' + escHtml(key) + '">' +
            escHtml(matchStr) + '</span>';
          last     = pos + matchStr.length;
          modified = true;
        }
      }
    }

    // Step 2: scan remaining text for capitalized single-word proper nouns
    var remaining = last === 0 ? text : (text.slice(last));
    var remaining_offset = last;

    // Simple word-boundary scan
    var wordRe = /\b([A-Z][a-z]{2,})\b/g;
    var wResult;
    var segLast = 0;
    var segHtml = '';
    var segMod  = false;

    wordRe.lastIndex = 0;
    while ((wResult = wordRe.exec(remaining)) !== null) {
      var word    = wResult[1];
      var wpos    = wResult.index;
      var key2    = word.toLowerCase();

      if (!_termSingleSet.has(key2)) continue;

      // Skip sentence-initial capitals: check char before the word in the FULL text
      var absPos  = remaining_offset + wpos;
      var pre     = absPos > 0 ? text.charAt(absPos - 1) : '';
      // If preceded by sentence-enders or newlines, this is sentence-start capitalisation
      if (absPos === 0 || /[.!?\n\r]/.test(pre)) continue;
      // Also skip if preceded by quote/em-dash after punctuation
      if (/["'"‘’“”—]/.test(pre)) {
        var pre2 = absPos > 1 ? text.charAt(absPos - 2) : '';
        if (/[.!?\n]/.test(pre2)) continue;
      }

      segHtml += escHtml(remaining.slice(segLast, wpos));
      segHtml += '<span class="term-link" data-term-key="' + escHtml(key2) + '">' +
        escHtml(word) + '</span>';
      segLast  = wpos + word.length;
      segMod   = true;
    }

    if (segMod) {
      segHtml += escHtml(remaining.slice(segLast));
      html    += segHtml;
      modified = true;
    } else if (modified) {
      html += escHtml(text.slice(last));
    }

    if (!modified) return;

    var span = document.createElement('span');
    span.innerHTML = html;
    // Wire term-links within the new span
    span.querySelectorAll('.term-link').forEach(_wireTermEl);
    textNode.parentNode.replaceChild(span, textNode);
  }

  // Designated containers to auto-tag on page load
  var _AUTOTAG_SELECTORS = [
    'blockquote.scripture',
    '[data-autotag]',
    '.lib-chapter',
    '.lib-father-quote',
    '.lib-creed'
  ].join(', ');

  function runAutoTagTerms() {
    _loadTermMap().then(function () {
      // Wire explicit .term elements site-wide
      document.querySelectorAll('.term').forEach(function (el) {
        var key = el.textContent.toLowerCase().trim();
        if (!el.classList.contains('term-link') && _termMap2 && _termMap2[key]) {
          el.classList.add('term-link');
          el.dataset.termKey = key;
        }
        _wireTermEl(el);
      });

      // Auto-tag designated content containers
      document.querySelectorAll(_AUTOTAG_SELECTORS).forEach(function (container) {
        autoTagTerms(container);
      });
    });
  }

  // ── Reading Plans — home widget ──────────────────────────────────────────

  var PLANS_KEY  = 'bsw_plans';
  var PLANS_ROOT = _resolve('../../data/plans');

  function _plansGetState()   { try { return JSON.parse(localStorage.getItem(PLANS_KEY) || '{}'); } catch (e) { return {}; } }
  function _plansDayNum(s) {
    if (!s || !s.startDate) return 1;
    var start = new Date(s.startDate + 'T00:00:00');
    var today = new Date();
    today = new Date(today.getFullYear(), today.getMonth(), today.getDate());
    return Math.floor((today - start) / 86400000) + 1;
  }

  function initPlansHomeWidget() {
    var widget = document.getElementById('home-plans-widget');
    if (!widget) return;

    var state   = _plansGetState();
    var enrolled = Object.keys(state).filter(function (id) { return state[id] && state[id].startDate; });
    if (!enrolled.length) return;

    Promise.all(enrolled.map(function (id) {
      return fetch(PLANS_ROOT + '/' + id + '.json')
        .then(function (r) { return r.ok ? r.json() : null; })
        .catch(function () { return null; });
    })).then(function (plans) {
      var html = '<div class="plans-widget">' +
        '<h2 class="plans-widget__heading">Today\'s Reading</h2>';

      var any = false;
      plans.forEach(function (plan) {
        if (!plan) return;
        var s  = state[plan.id];
        var dn = _plansDayNum(s);
        if (dn < 1 || dn > plan.total_days) {
          html += '<div class="plans-widget__item">' +
            '<span class="plans-widget__title">' + escHtml(plan.title) + '</span> — ' +
            '<span class="plans-widget__done">Complete!</span></div>';
          any = true;
          return;
        }
        var day  = plan.days[dn - 1];
        var comp = s.completed && s.completed[dn];
        html += '<div class="plans-widget__item' + (comp ? ' plans-widget__item--done' : '') + '">';
        html += '<span class="plans-widget__title">' + escHtml(plan.title) + '</span>';
        html += ' <span class="plans-widget__meta">Day ' + dn + ' of ' + plan.total_days + '</span>';
        html += '<div class="plans-widget__passages">';
        day.passages.forEach(function (p) {
          html += '<a class="plans-widget__passage" href="' +
            escHtml(READ_URL + '?ref=' + encodeURIComponent(p)) + '">' +
            escHtml(p) + '</a>';
        });
        html += '</div>';
        if (comp) {
          html += '<span class="plans-widget__check">✓ Done</span>';
        } else {
          html += '<a class="plans-widget__goto" href="plans/">Open Reading Plans →</a>';
        }
        html += '</div>';
        any = true;
      });

      html += '</div>';

      if (any) {
        widget.innerHTML = html;
        widget.removeAttribute('hidden');
        // Insert before the Tools h2
        var toolsH2 = Array.from(widget.parentNode.querySelectorAll('h2'))
          .find(function (h) { return h.textContent.trim() === 'Tools'; });
        if (toolsH2) toolsH2.parentNode.insertBefore(widget, toolsH2);
      }
    });
  }

  // ── Bootstrap

  // ── Bootstrap ─────────────────────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
