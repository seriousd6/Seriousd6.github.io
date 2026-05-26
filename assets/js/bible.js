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
  var VERSIONS_URL = _resolve('../../data/versions/versions.json');
  var BOOKS_URL    = _resolve('../../data/bible/books.json');
  var SEARCH_URL   = _resolve('../../search/');
  var READER_URL   = _resolve('../../read/');
  var STORAGE_KEY  = 'bsw_version';
  var DEFAULT_VER  = 'BSB';

  // ── In-memory caches ──────────────────────────────────────────────────────
  // key "{VERSION}:{bookId}" → chapters object {"1":{"1":"text",...},...}
  var bookCache     = Object.create(null);
  // key "{bookId}" → cross-ref object {"ch":{"v":["ref",...]},...} or null
  var crossRefCache = Object.create(null);
  // key "{bookId}" → commentary object {"ch":{"startV":"html",...},...} or null
  var commentaryCache = Object.create(null);
  // key "{bookId}" → parallel passage data {"ch":{"v":[{...}]}} or null
  var parallelsCache  = Object.create(null);
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
  }

  // ── Init ──────────────────────────────────────────────────────────────────
  function init() {
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
      }
      autoTagRefs();
      wireInlineVerses();
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

    var bookData = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
    var bookName = bookData ? bookData.name : m[1];

    var display = bookName + ' ' + ch + ':' + v;
    if (m[5]) {
      display += '–' + (m[4] ? m[4] + ':' : '') + m[5];
    }

    return { bookId: bookId, bookName: bookName, ch: ch, v: v,
             endCh: endCh, endV: endV, display: display, raw: str };
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

  function loadCommentary(bookId) {
    if (bookId in commentaryCache) return Promise.resolve(commentaryCache[bookId]);
    var url = COMMENTARY_ROOT + '/' + bookId + '.json';
    return fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) {
        commentaryCache[bookId] = (data && Object.keys(data).length) ? data : null;
        return commentaryCache[bookId];
      })
      .catch(function () {
        commentaryCache[bookId] = null;
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
        '<button class="bsw-modal__close" aria-label="Close verse viewer">✕</button>' +
      '</div>' +
      '<div class="bsw-modal__version-bar">' +
        '<label for="bsw-modal-version">Version:</label>' +
        '<select id="bsw-modal-version"></select>' +
      '</div>' +
      '<div class="bsw-modal__tabs" role="tablist">' +
        '<button class="bsw-modal__tab bsw-modal__tab--active" data-tab="verse" role="tab" aria-selected="true">Verse</button>' +
        '<button class="bsw-modal__tab" data-tab="commentary" role="tab" aria-selected="false">Commentary</button>' +
      '</div>' +
      // Verse + Cross-References split panel (default view)
      '<div class="bsw-modal__split">' +
        '<div class="bsw-modal__verse-col">' +
          '<div class="bsw-modal__body" aria-live="polite"></div>' +
          '<div class="bsw-modal__attribution"></div>' +
        '</div>' +
        '<div class="bsw-modal__xrefs-col">' +
          '<div class="bsw-modal__xrefs-heading">Cross-References</div>' +
          '<div class="bsw-modal__xrefs-panel"></div>' +
        '</div>' +
      '</div>' +
      // Commentary panel (hidden until tab click)
      '<div class="bsw-modal__commentary-panel" hidden></div>';

    backdrop.appendChild(modal);
    document.body.appendChild(backdrop);

    _backdropEl = backdrop;
    _modalEl    = modal;

    modal.querySelector('.bsw-modal__close').addEventListener('click', hideModal);
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
      var splitEl = modal.querySelector('.bsw-modal__split');
      var commEl  = modal.querySelector('.bsw-modal__commentary-panel');
      if (tab === 'verse') {
        if (splitEl) splitEl.removeAttribute('hidden');
        if (commEl)  commEl.setAttribute('hidden', '');
      } else if (tab === 'commentary') {
        if (splitEl) splitEl.setAttribute('hidden', '');
        if (commEl) {
          commEl.removeAttribute('hidden');
          if (!commEl._commentaryLoaded) renderCommentary(_modalEl._parsedRef, commEl);
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
    var xrefsEl = _modalEl.querySelector('.bsw-modal__xrefs-panel');
    var bodyEl  = _modalEl.querySelector('.bsw-modal__body');
    var attrElR = _modalEl.querySelector('.bsw-modal__attribution');
    _modalEl.querySelectorAll('.bsw-modal__tab').forEach(function (b) {
      var isVerse = b.getAttribute('data-tab') === 'verse';
      b.classList.toggle('bsw-modal__tab--active', isVerse);
      b.setAttribute('aria-selected', isVerse ? 'true' : 'false');
    });
    var splitEl = _modalEl.querySelector('.bsw-modal__split');
    var commEl  = _modalEl.querySelector('.bsw-modal__commentary-panel');
    if (bodyEl)  bodyEl.removeAttribute('hidden');
    if (attrElR) attrElR.removeAttribute('hidden');
    if (splitEl) splitEl.removeAttribute('hidden');
    if (xrefsEl) xrefsEl._xrefLoaded = false;
    if (commEl)  { commEl.setAttribute('hidden', '');  commEl._commentaryLoaded = false; }

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
        readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch + ':' + parsed.v);
        readCh.textContent = 'Read chapter ↗';
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
              html += '<div class="bsw-modal__verse">' +
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
            return '<div class="bsw-modal__verse">' +
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
            return '<div class="bsw-modal__verse">' +
              '<sup class="bsw-modal__verse-num">' + vr.verse + '</sup>' +
              '<span class="bsw-modal__verse-text">' + escHtml(vr.text) + '</span>' +
              '</div>';
          }).join('');
        }
        body.innerHTML = html;
        attr.textContent = ATTRIBUTION[versionId] || '';

        // Auto-load cross-refs in the parallel right column
        var xrefsPanel = _modalEl.querySelector('.bsw-modal__xrefs-panel');
        if (xrefsPanel && !xrefsPanel._xrefLoaded) {
          renderCrossRefs(parsed, xrefsPanel);
        }
      })
      .catch(function () {
        body.innerHTML =
          '<p class="bsw-modal__error">Could not load ' + escHtml(versionId) + ' data.</p>';
      });
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

  function renderCommentary(parsed, container) {
    if (!parsed) {
      container.innerHTML = '<p class="bsw-modal__commentary-empty">No reference selected.</p>';
      return;
    }
    container._commentaryLoaded = true;
    container.innerHTML = '<p class="bsw-modal__loading">Loading commentary…</p>';

    loadCommentary(parsed.bookId).then(function (data) {
      if (!data) {
        container.innerHTML = '<p class="bsw-modal__commentary-empty">No commentary available for this book.</p>';
        return;
      }

      var chData = data[String(parsed.ch)];
      if (!chData) {
        container.innerHTML = '<p class="bsw-modal__commentary-empty">No commentary found for this chapter.</p>';
        return;
      }

      // Search backwards from target verse to find the enclosing section
      var html = '';
      var endV = parsed.wholeChapter ? 9999 : parsed.endV;
      var startV = parsed.v;

      // For verse ranges / chapters: collect all sections within the range
      var sectionKeys = Object.keys(chData).map(Number).sort(function (a, b) { return a - b; });

      if (parsed.wholeChapter) {
        // Show all sections in the chapter
        sectionKeys.forEach(function (v) {
          html += '<div class="bsw-modal__commentary-section">' + chData[String(v)] + '</div>';
        });
      } else {
        // Find the section that covers the target verse (search backwards)
        var foundV = null;
        for (var v = startV; v >= 1; v--) {
          if (chData[String(v)]) { foundV = v; break; }
        }
        if (foundV !== null) {
          html = '<div class="bsw-modal__commentary-section">' + chData[String(foundV)] + '</div>';
          // If it's a range, also show subsequent sections that fall within the range
          sectionKeys.forEach(function (v) {
            if (v > startV && v <= endV && chData[String(v)]) {
              html += '<div class="bsw-modal__commentary-section">' + chData[String(v)] + '</div>';
            }
          });
        }
      }

      if (!html) {
        container.innerHTML = '<p class="bsw-modal__commentary-empty">No commentary found for this verse.</p>';
        return;
      }

      var attr = '<p class="bsw-modal__commentary-attr">Matthew Henry\'s Concise Commentary' +
        ' (Public Domain)</p>';
      container.innerHTML = html + attr;
    }).catch(function () {
      container.innerHTML = '<p class="bsw-modal__commentary-empty">Could not load commentary.</p>';
    });
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

    // Pre-fill from ?q= so searches can be linked/bookmarked
    var params = new URLSearchParams(window.location.search);
    var q = params.get('q') || '';
    if (q) { input.value = q; handleSearchInput(q); }

    input.addEventListener('input', function () {
      clearTimeout(_searchDebounce);
      _searchDebounce = setTimeout(function () {
        var query = input.value.trim();
        handleSearchInput(query);
        var url = new URL(window.location.href);
        if (query.length >= 4) { url.searchParams.set('q', query); }
        else                   { url.searchParams.delete('q');      }
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

      var refs = parseMultiRef(q, null);
      if (!refs.length) {
        setStatus('Could not parse — try: Gen 1 or John 3:16-21');
        return;
      }
      setStatus('');

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

    metaBooks.forEach(function (b) {
      var opt = document.createElement('option');
      opt.value = b.id;
      opt.textContent = b.name;
      bookSel.appendChild(opt);
    });

    bookSel.addEventListener('change', function () {
      var bk = metaBooks.find(function (b) { return b.id === bookSel.value; });
      if (!bk) {
        chSel.innerHTML = '<option value="">Ch…</option>';
        chSel.disabled = true;
        chSel._bookId = null;
        return;
      }
      chSel._bookId = bk.id;
      chSel.innerHTML = '<option value="">Ch…</option>';
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
      var bk = metaBooks.find(function (b) { return b.id === bookSel.value; });
      if (!bk) return;
      var ref = bk.name + ' ' + chSel.value;
      var lookupInput = document.getElementById('reader-lookup-input');
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
            ref = nav.bookName + ' ' + nav.ch + ':' + ns + '-' + ne;
          } else if (nav.ch < nav.maxCh) {
            ref = nav.bookName + ' ' + (nav.ch + 1); // intercepted → first window of next chapter
          }
        }
      } else {
        // Standard chapter-by-chapter mode
        if (goLeft && nav.ch > 1) {
          ref = nav.bookName + ' ' + (nav.ch - 1);
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
        var btn = e.target.closest('.reader-sidebar__ch');
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
    var bookSel = document.getElementById('reader-book-select');
    var chSel   = document.getElementById('reader-ch-select');
    if (!bookSel || !chSel) return;
    bookSel.value = _readerNavState.bookId;
    var bk = metaBooks && metaBooks.find(function (b) { return b.id === _readerNavState.bookId; });
    if (!bk) return;
    if (chSel._bookId !== _readerNavState.bookId) {
      chSel._bookId = _readerNavState.bookId;
      chSel.innerHTML = '<option value="">Ch…</option>';
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
      // Standard chapter navigation
      if (ref.ch > 1) {
        var p = ref.bookName + ' ' + (ref.ch - 1);
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(p) + '">← ' + escHtml(p) + '</button>';
      } else {
        html += '<span></span>';
      }
      if (ref.ch < maxCh) {
        var n = ref.bookName + ' ' + (ref.ch + 1);
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(n) + '">' + escHtml(n) + ' →</button>';
      }
    } else if (ref.verseWindow) {
      // Verse-window mode: step by PARALLEL_VERSE_WINDOW within the chapter; wrap at boundaries.
      // "fewer verses than window" means we're at the end of the chapter.
      var atChEnd = !verses || verses.length < PARALLEL_VERSE_WINDOW;
      var startV  = ref.v;
      var endV    = ref.endV;

      // Prev button
      if (startV > 1) {
        var prevStart = Math.max(1, startV - PARALLEL_VERSE_WINDOW);
        var prevEnd   = startV - 1;
        var prevLbl   = ref.bookName + ' ' + ref.ch + ':' + prevStart + '-' + prevEnd;
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(prevLbl) + '">← Prev 5 verses</button>';
      } else if (ref.ch > 1) {
        var prevChLbl = ref.bookName + ' ' + (ref.ch - 1);
        html += '<button class="reader-nav-btn" data-nav-label="' + escHtml(prevChLbl) + '">← ' + escHtml(ref.bookName + ' ' + (ref.ch - 1)) + '</button>';
      } else {
        html += '<span></span>';
      }

      // Next button
      if (!atChEnd) {
        var nextStart = endV + 1;
        var nextEnd   = endV + PARALLEL_VERSE_WINDOW;
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
      _readerNavState = {
        bookId:     navRef.bookId,
        bookName:   navRef.bookName,
        ch:         navRef.ch,
        maxCh:      navBk ? (navBk.chapters || 999) : 999,
        verseStart: navRef.verseWindow ? navRef.v   : null,
        verseEnd:   navRef.verseWindow ? navRef.endV : null,
        atChEnd:    navRef.verseWindow ? (!navVs || navVs.length < PARALLEL_VERSE_WINDOW) : false
      };
    } else {
      _readerNavState = null;
    }
    syncBrowseSelects();

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

    el.innerHTML = html || '<p class="reader-hint">No results.</p>';

    // Clear the side panel — it will be rebuilt incrementally as cross-refs load
    var xrefPanel = document.getElementById('reader-xref-panel');
    if (xrefPanel) xrefPanel.innerHTML = '';

    wireReaderNav(el);

    // Track rendered groups, inject cross-refs and (if enabled) parallel panels
    _readerGroups = [];
    var domGroups = el.querySelectorAll('.reader-result-group');
    groups.forEach(function (g, idx) {
      var groupEl = domGroups[idx];
      if (!groupEl) return;
      _readerGroups.push({ ref: g.ref, el: groupEl });
      injectReaderFootnotes(g.ref, groupEl);
      if (getParallelsEnabled()) injectParallelPanels(g.ref, groupEl);
    });
  }

  // Clears and rebuilds the cross-ref side panel from all .reader-xref-note elements in results.
  function _refreshXrefPanel() {
    var panel = document.getElementById('reader-xref-panel');
    if (!panel) return;

    // Collect all verse spans that have footnote sups, in DOM order
    var groups = document.querySelectorAll('.reader-xref-group--panel');
    // Remove old panel content
    panel.innerHTML = '';

    var notes = document.querySelectorAll('.reader-result-group .reader-xref-note');
    if (!notes.length) return;

    var heading = document.createElement('div');
    heading.className = 'reader-xref-panel__heading';
    heading.textContent = 'Cross References';
    panel.appendChild(heading);

    // Group sups by their parent verse span (data-ch + data-v)
    var seenVerses = [];
    var byVerse = Object.create(null);
    notes.forEach(function (sup) {
      var verse = sup.closest('.reader-verse');
      if (!verse) return;
      var ch = verse.getAttribute('data-ch');
      var v  = verse.getAttribute('data-v');
      var key = ch + ':' + v;
      if (!byVerse[key]) {
        byVerse[key] = { ch: ch, v: v, sups: [] };
        seenVerses.push(key);
      }
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
      panel.appendChild(group);
    });
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

  // ── Bootstrap ─────────────────────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
