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

  var DATA_ROOT    = _resolve('../../data/bible');
  var VERSIONS_URL = _resolve('../../data/versions/versions.json');
  var BOOKS_URL    = _resolve('../../data/bible/books.json');
  var SEARCH_URL   = _resolve('../../search/');
  var READER_URL   = _resolve('../../read/');
  var STORAGE_KEY  = 'bsw_version';
  var DEFAULT_VER  = 'KJV';

  // ── In-memory caches ──────────────────────────────────────────────────────
  // key "{VERSION}:{bookId}" → chapters object {"1":{"1":"text",...},...}
  var bookCache = Object.create(null);
  var metaVersions = null;   // Array of version objects from versions.json
  var metaBooks    = null;   // Array of book objects from books.json
  var bookLookup   = null;   // Map: normalized string → bookId

  // ── Public API ────────────────────────────────────────────────────────────
  window.BibleUI = {
    init: init,
    getVersion: getVersion,
    setVersion: setVersion,
    openModal: openModal,
    openReader: function (bookId, ch, v) {
      var ref = bookId + ' ' + (ch || 1) + (v ? ':' + v : '');
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
      if (document.getElementById('reader-results')) initReaderPage();
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
        data.forEach(function (book) {
          // canonical name (lower, no spaces)
          bookLookup[book.name.toLowerCase()] = book.id;
          bookLookup[book.name.toLowerCase().replace(/\s+/g, '')] = book.id;
          // self-reference by id
          bookLookup[book.id] = book.id;
          // each abbreviation (case-insensitive)
          book.abbrevs.forEach(function (a) {
            bookLookup[a.toLowerCase()] = book.id;
          });
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
  var _readerLookupFn = null; // set by initReaderLookup; called on version change

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
      '<div class="bsw-modal__body" aria-live="polite"></div>' +
      '<div class="bsw-modal__attribution"></div>';

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
        readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookId + ' ' + parsed.ch);
        readCh.textContent = 'Open in Reader ↗';
      } else if (parsed.wholeChapter) {
        readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookId + ' ' + parsed.ch);
        readCh.textContent = 'Read chapter ↗';
      } else {
        readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookId + ' ' + parsed.ch);
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
            var chRef2   = READER_URL + '?ref=' + encodeURIComponent(parsed.bookId + ' ' + c);
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
            var chRef = parsed.bookId + ' ' + parsed.ch;
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
      })
      .catch(function () {
        body.innerHTML =
          '<p class="bsw-modal__error">Could not load ' + escHtml(versionId) + ' data.</p>';
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

  function renderReaderResults(groups, version) {
    var el = document.getElementById('reader-results');
    if (!el) return;
    var html = '';
    groups.forEach(function (g) {
      html += '<div class="reader-result-group">';
      html += '<h2 class="reader-result-group__title">' + escHtml(g.ref.display) + '</h2>';
      if (!g.verses || !g.verses.length) {
        html += '<p class="reader-hint">Not available in ' + escHtml(version) + '.</p>';
      } else {
        html += '<p class="reader-result-group__text">';
        g.verses.forEach(function (vObj) {
          html += '<span class="reader-verse">' +
            '<sup class="reader-verse__num">' + vObj.verse + '</sup>' +
            escHtml(vObj.text) + ' </span>';
        });
        html += '</p>';
        var attr = ATTRIBUTION[version];
        if (attr) html += '<p class="reader-result-group__attr">' + escHtml(attr) + '</p>';
      }
      html += '</div>';
    });
    el.innerHTML = html || '<p class="reader-hint">No results.</p>';
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
      var readHref = READER_URL + '?ref=' + encodeURIComponent(r.bookId + ' ' + r.ch);
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

    // "Book Ch" not followed by optional whitespace then colon/digit
    // (which would indicate a verse ref already handled by autoTagRefs).
    var BOOK_CH_RE = /\b((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+){0,3})\s+(\d+)(?!\s*[:\d])/g;
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
        var bookName = bk ? bk.name : m[1];
        var display  = bookName + ' ' + ch;

        var parsed = {
          bookId: bookId, bookName: bookName,
          ch: ch, v: 1, endCh: ch, endV: 9999,
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
