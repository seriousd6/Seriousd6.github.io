/* apocrypha-reader.js — Reader for complete apocryphal Bible versions.
 *
 * For full-Bible versions (DR, WEB-CE, KJV-APO, BRENTON) the reader shows all
 * canonical + deuterocanonical books arranged in the version's traditional order
 * (defined in data/apocrypha-canon-orders.json). Filter chips toggle between
 * "All | OT | Deuterocanonical | NT" views.
 *
 * For any version without scope="full-bible" the reader falls back to showing
 * just the 17 deuterocanonical books with the original canon-tradition chips.
 *
 * All chapter data is loaded from data/bible-apocrypha/{VERSION}/{bookId}.json —
 * the fetch script stores both canonical and deuterocanonical books there so this
 * module uses one consistent data root.
 */
'use strict';

import { _resolve, escHtml, metaBooks } from './core.js';
import { wireRefLinks } from './wire.js';

// ── URLs ─────────────────────────────────────────────────────────────────────
var APO_DATA_ROOT    = _resolve('../../data/bible-apocrypha');
var APO_BOOKS_URL    = _resolve('../../data/apocrypha-books.json');
var CANON_ORDERS_URL = _resolve('../../data/apocrypha-canon-orders.json');
var VERSIONS_URL     = _resolve('../../data/versions/versions.json');
var APO_READER_URL   = _resolve('../../apocrypha/');

// ── Module state ──────────────────────────────────────────────────────────────
// INTENT: All module-level caches are populated once at init and shared across
//   render calls. _canonOrders, _apoBooks, and metaBooks (from core.js) together
//   provide the full combined book list for any version.
// CHANGE? If any JSON schema changes (apocrypha-books.json, apocrypha-canon-orders.json,
//   versions.json) update the corresponding load function and field references here.
// VERIFY: Open apocrypha/ with DR selected; all 73 books should appear in the book select.
var _apoBooks     = null;   // 17 deuterocanonical books from apocrypha-books.json
var _apoVersions  = null;   // versions with group="apocrypha" from versions.json
var _canonOrders  = null;   // {dr:{books:[...]}, kjv-apocrypha:{...}, lxx:{...}}
var _bookCache    = {};     // "version:bookId" → chapters object or null
var _currentFilter = 'all'; // active filter chip id
var _currentVer   = null;   // active version id

var VER_KEY = 'bsw_apoc_version';

// ── Data loaders ──────────────────────────────────────────────────────────────

function _loadApoBooks() {
  if (_apoBooks) return Promise.resolve(_apoBooks);
  return fetch(APO_BOOKS_URL)
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) { _apoBooks = d; return d; });
}

function _loadApoVersions() {
  if (_apoVersions) return Promise.resolve(_apoVersions);
  return fetch(VERSIONS_URL)
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) {
      _apoVersions = d.filter(function (v) { return v.group === 'apocrypha'; });
      return _apoVersions;
    });
}

function _loadCanonOrders() {
  if (_canonOrders) return Promise.resolve(_canonOrders);
  return fetch(CANON_ORDERS_URL)
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) { _canonOrders = d; return d; });
}

function _loadBook(versionId, bookId) {
  // INTENT: All books (canonical + deuterocanonical) live in data/bible-apocrypha/{version}/.
  //   The fetch script populates both there so one data root serves the entire Bible.
  // CHANGE? If the directory structure changes, update APO_DATA_ROOT here and in fetch-apocrypha.py.
  // VERIFY: Network tab when reading Genesis 1 in WEB-CE should show
  //   bible-apocrypha/WEB-CE/genesis.json — not data/bible/WEB-CE/.
  var key = versionId + ':' + bookId;
  if (key in _bookCache) {
    return _bookCache[key] ? Promise.resolve(_bookCache[key]) : Promise.reject(new Error('no data'));
  }
  var url = APO_DATA_ROOT + '/' + versionId + '/' + bookId + '.json';
  return fetch(url)
    .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
    .then(function (data) {
      _bookCache[key] = data.chapters || data || null;
      return _bookCache[key];
    })
    .catch(function (err) { _bookCache[key] = null; throw err; });
}

// ── Book list helpers ─────────────────────────────────────────────────────────

function _getVer() {
  return _apoVersions && _apoVersions.find(function (v) { return v.id === _currentVer; });
}

function _isFullBible() {
  var ver = _getVer();
  return !!(ver && ver.scope === 'full-bible');
}

// Lookup book metadata from either the canonical or deuterocanonical list
function _findBook(bookId) {
  var apo = _apoBooks && _apoBooks.find(function (b) { return b.id === bookId; });
  if (apo) return apo;
  var canon = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
  return canon || null;
}

// Set of deuterocanonical book IDs — used for OT/Apo/NT bucketing
function _apoIdSet() {
  var s = {};
  (_apoBooks || []).forEach(function (b) { s[b.id] = true; });
  return s;
}

// Full ordered book list for the current version from canon-order data
// INTENT: Any version with a `canon_order` field uses that order (full-bible and
//   ot-only). For ot-only scope (BRENTON), NT canonical books are filtered out after
//   ordering so NT 404s don't appear in the list. Versions with no canon_order
//   fall back to the deuterocanonical-only list (_apoBooks). `_canonOrders[key]`
//   is an object `{label, note, books:[...]}` — `.books` must be addressed explicitly.
// CHANGE? If `apocrypha-canon-orders.json` schema changes (e.g. books array renamed),
//   update `.books` here. If new scope values are added to versions.json, decide
//   whether they should use a canon order and whether NT filtering applies.
//   _isFullBible() is separate — it only controls which filter chips are shown.
// VERIFY: Open /apocrypha/ with BRENTON — confirm only OT books appear (no NT).
//   With DR — confirm the full combined list including NT appears.
function _getOrderedBooks() {
  var ver = _getVer();
  var order = ver && _canonOrders && _canonOrders[ver.canon_order];
  var books;
  if (order) {
    books = (order.books || []).map(function (id) { return _findBook(id); }).filter(Boolean);
  } else {
    books = _apoBooks || [];
  }
  // OT-only versions (e.g. BRENTON): exclude NT books the canon order lists but
  // for which no data files exist — prevents 404s for all 27 NT slots.
  if (ver && ver.scope === 'ot-only') {
    books = books.filter(function (b) { return b.testament !== 'NT'; });
  }
  return books;
}

// Apply the current filter chip to a book list
function _applyFilter(books, filter) {
  if (filter === 'all') return books;
  if (_isFullBible()) {
    var apoSet = _apoIdSet();
    if (filter === 'apo') return books.filter(function (b) { return apoSet[b.id]; });
    if (filter === 'ot')  return books.filter(function (b) { return b.testament !== 'NT' && !apoSet[b.id]; });
    if (filter === 'nt')  return books.filter(function (b) { return b.testament === 'NT'; });
    return books;
  }
  // Apocrypha-only mode: filter by canon tradition
  return books.filter(function (b) { return b.canon && b.canon.indexOf(filter) !== -1; });
}

function _getActiveBooks() {
  return _applyFilter(_getOrderedBooks(), _currentFilter);
}

// ── URL state ─────────────────────────────────────────────────────────────────

function _getUrlParams() {
  var p = new URLSearchParams(window.location.search);
  return { book: p.get('book') || '', ch: p.get('ch') || '1' };
}

function _pushState(bookId, ch) {
  var url = APO_READER_URL + '?book=' + encodeURIComponent(bookId) + '&ch=' + encodeURIComponent(ch);
  history.pushState({ book: bookId, ch: ch }, '', url);
}

// ── DOM helpers ───────────────────────────────────────────────────────────────

function _getEl(id) { return document.getElementById(id); }

function _buildFilterChips() {
  // INTENT: Full-Bible versions get OT/Apo/NT testament chips; apocrypha-only versions
  //   get Catholic/Orthodox/LXX tradition chips. Both include "All" as the first chip.
  //   The controls label also updates to show the version's canon tradition name.
  // CHANGE? If filter chip IDs change, update _applyFilter() and _selectFilter().
  // VERIFY: Switch to WEB-CE; chips should read "All | OT | Deuterocanonical | NT".
  var bar = _getEl('apoc-canon-bar');
  if (!bar) return;

  // Update the header label to reflect the version's tradition
  var label = _getEl('apoc-controls-label');
  if (label) {
    var ver = _getVer();
    var orderKey = ver && ver.canon_order;
    var orderMeta = orderKey && _canonOrders && _canonOrders[orderKey];
    label.textContent = orderMeta ? orderMeta.label : 'Apocrypha';
  }

  var chips = _isFullBible()
    ? [
        { id: 'all', label: 'All Books' },
        { id: 'ot',  label: 'Old Testament' },
        { id: 'apo', label: 'Deuterocanonical' },
        { id: 'nt',  label: 'New Testament' }
      ]
    : [
        { id: 'all',      label: 'All Books' },
        { id: 'catholic', label: 'Catholic'  },
        { id: 'orthodox', label: 'Orthodox'  },
        { id: 'lxx',      label: 'LXX'       }
      ];

  bar.innerHTML = '';
  chips.forEach(function (chip) {
    var btn = document.createElement('button');
    btn.className = 'apoc-canon-chip' + (chip.id === _currentFilter ? ' apoc-canon-chip--active' : '');
    btn.dataset.filter = chip.id;
    btn.textContent = chip.label;
    btn.type = 'button';
    btn.setAttribute('aria-pressed', chip.id === _currentFilter ? 'true' : 'false');
    btn.addEventListener('click', function () { _selectFilter(chip.id); });
    bar.appendChild(btn);
  });
}

function _populateBookSelect(selectedId) {
  var sel = _getEl('apoc-book-select');
  if (!sel) return;
  var books = _getActiveBooks();
  sel.innerHTML = '';

  // For full-Bible views, wrap in OT / Apocrypha / NT optgroups when showing all
  if (_isFullBible() && _currentFilter === 'all') {
    var apoSet = _apoIdSet();
    var groups = [
      { label: 'Old Testament',      test: function (b) { return b.testament !== 'NT' && !apoSet[b.id]; } },
      { label: 'Deuterocanonical',   test: function (b) { return !!apoSet[b.id]; } },
      { label: 'New Testament',      test: function (b) { return b.testament === 'NT'; } }
    ];
    // Preserve canonical order within each group by filtering from ordered list
    groups.forEach(function (g) {
      var grpBooks = books.filter(g.test);
      if (!grpBooks.length) return;
      var grp = document.createElement('optgroup');
      grp.label = g.label;
      grpBooks.forEach(function (b) {
        var opt = document.createElement('option');
        opt.value       = b.id;
        opt.textContent = b.name;
        if (b.id === selectedId) opt.selected = true;
        grp.appendChild(opt);
      });
      sel.appendChild(grp);
    });
  } else {
    books.forEach(function (b) {
      var opt = document.createElement('option');
      opt.value       = b.id;
      opt.textContent = b.name;
      if (b.id === selectedId) opt.selected = true;
      sel.appendChild(opt);
    });
  }

  if (!selectedId && books.length) sel.value = books[0].id;
}

function _populateChSelect(bookId, selectedCh) {
  var sel  = _getEl('apoc-ch-select');
  var book = _findBook(bookId);
  if (!sel || !book) return;
  sel.disabled = false;
  sel.innerHTML = '';
  for (var i = 1; i <= book.chapters; i++) {
    var opt = document.createElement('option');
    opt.value       = String(i);
    opt.textContent = 'Chapter ' + i;
    if (String(i) === String(selectedCh)) opt.selected = true;
    sel.appendChild(opt);
  }
}

function _populateVerSelect() {
  var sel = _getEl('apoc-ver-select');
  if (!sel || !_apoVersions) return;
  sel.innerHTML = '';
  _apoVersions.forEach(function (v) {
    var opt = document.createElement('option');
    opt.value       = v.id;
    opt.textContent = v.name;
    if (v.id === _currentVer) opt.selected = true;
    sel.appendChild(opt);
  });
}

function _buildSidebarChapters(bookId, currentCh) {
  var sidebar = _getEl('apoc-sidebar');
  var book    = _findBook(bookId);
  if (!sidebar || !book) return;
  sidebar.innerHTML = '<p class="apoc-sidebar-book">' + escHtml(book.name) + '</p>';
  var grid = document.createElement('div');
  grid.className = 'apoc-ch-grid';
  for (var i = 1; i <= book.chapters; i++) {
    var btn = document.createElement('button');
    var isCurrent = String(i) === String(currentCh);
    btn.className   = 'apoc-ch-btn' + (isCurrent ? ' apoc-ch-btn--active' : '');
    btn.textContent = String(i);
    btn.dataset.ch  = String(i);
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Chapter ' + i);
    btn.setAttribute('aria-current', isCurrent ? 'page' : 'false');
    btn.addEventListener('click', (function (ch) {
      return function () { _navigateTo(bookId, ch); };
    }(i)));
    grid.appendChild(btn);
  }
  sidebar.appendChild(grid);
}

// ── Chapter render ────────────────────────────────────────────────────────────

function _bookBadge(book) {
  // INTENT: Returns a short tradition badge string. Canonical books show OT/NT.
  //   Deuterocanonical books show their canon traditions (Catholic · Orthodox etc).
  if (!book) return '';
  if (book.canon) return book.canon.map(function (c) { return c[0].toUpperCase() + c.slice(1); }).join(' · ');
  return book.testament || '';
}

function _renderChapter(bookId, ch, chapters) {
  // INTENT: Renders a chapter as flowing verse spans. wireRefLinks wires canonical
  //   refs to the verse tooltip; chapter nav links use ?book=&ch= parameters.
  // CHANGE? If verse data schema changes from {ch:{v:text}}, update the accessor below.
  // VERIFY: Open Genesis 1 in WEB-CE; 31 verses numbered 1-31 should render.
  var resultsEl = _getEl('apoc-reader-results');
  if (!resultsEl) return;

  var chData = chapters[String(ch)];
  if (!chData) {
    resultsEl.innerHTML = '<p class="apoc-msg">Chapter ' + ch + ' not found in this translation.</p>';
    return;
  }

  var book     = _findBook(bookId);
  var bookName = book ? book.name : bookId;
  var badge    = _bookBadge(book);
  var verCount = Object.keys(chData).length;

  var html = '<div class="apoc-chapter-header">'
    + '<h2 class="apoc-chapter-title">' + escHtml(bookName) + ' ' + ch + '</h2>'
    + (badge ? '<span class="apoc-canon-badge">' + escHtml(badge) + '</span>' : '')
    + '</div>'
    + '<div class="apoc-verses">';

  var verses = Object.keys(chData).sort(function (a, b) { return +a - +b; });
  verses.forEach(function (v) {
    html += '<span class="apoc-verse">'
      + '<sup class="apoc-verse-num">' + v + '</sup>'
      + escHtml(chData[v]) + ' </span>';
  });
  html += '</div>';

  // Prev/Next chapter navigation — also crosses book boundaries for full-Bible mode
  var prevCh = parseInt(ch, 10) - 1;
  var nextCh = parseInt(ch, 10) + 1;
  html += '<div class="apoc-chapter-nav">';
  if (prevCh >= 1) {
    html += '<a class="apoc-nav-btn" href="'
      + APO_READER_URL + '?book=' + encodeURIComponent(bookId) + '&ch=' + prevCh
      + '">← ' + escHtml(bookName) + ' ' + prevCh + '</a>';
  } else if (_isFullBible()) {
    // Try to link to the last chapter of the previous book in canonical order
    var prevBook = _getPrevBook(bookId);
    if (prevBook) {
      html += '<a class="apoc-nav-btn" href="'
        + APO_READER_URL + '?book=' + encodeURIComponent(prevBook.id)
        + '&ch=' + prevBook.chapters + '">'
        + '← ' + escHtml(prevBook.name) + ' ' + prevBook.chapters + '</a>';
    }
  }
  html += '<span class="apoc-nav-info">' + verCount + ' verses</span>';
  if (book && nextCh <= book.chapters) {
    html += '<a class="apoc-nav-btn" href="'
      + APO_READER_URL + '?book=' + encodeURIComponent(bookId) + '&ch=' + nextCh
      + '">' + escHtml(bookName) + ' ' + nextCh + ' →</a>';
  } else if (_isFullBible()) {
    var nextBook = _getNextBook(bookId);
    if (nextBook) {
      html += '<a class="apoc-nav-btn" href="'
        + APO_READER_URL + '?book=' + encodeURIComponent(nextBook.id) + '&ch=1">'
        + escHtml(nextBook.name) + ' 1 →</a>';
    }
  }
  html += '</div>';

  resultsEl.innerHTML = html;
  wireRefLinks(resultsEl);
  _buildSidebarChapters(bookId, ch);
}

// ── Cross-book navigation helpers ─────────────────────────────────────────────

function _getOrderedAll() {
  // Full ordered book list with no filter applied — used for prev/next book nav.
  return _applyFilter(_getOrderedBooks(), 'all');
}

function _getPrevBook(bookId) {
  var all = _getOrderedAll();
  var idx = all.findIndex(function (b) { return b.id === bookId; });
  return idx > 0 ? all[idx - 1] : null;
}

function _getNextBook(bookId) {
  var all = _getOrderedAll();
  var idx = all.findIndex(function (b) { return b.id === bookId; });
  return idx >= 0 && idx < all.length - 1 ? all[idx + 1] : null;
}

// ── Navigation ────────────────────────────────────────────────────────────────

function _navigateTo(bookId, ch) {
  // INTENT: Central navigation handler — updates URL, controls, and renders text.
  //   Loads from APO_DATA_ROOT which contains all books (canonical + apocryphal).
  // CHANGE? If data path or error message template changes, update here and in
  //   fetch-apocrypha.py docstring (users copy the command from the error message).
  // VERIFY: Navigate to Genesis 1 → Revelation 22 → clicking Next crosses to Tobit 1
  //   in DR mode; each step updates the browser URL and book select.
  var resultsEl = _getEl('apoc-reader-results');
  if (resultsEl) resultsEl.innerHTML = '<p class="apoc-msg apoc-msg--loading">Loading…</p>';

  _populateBookSelect(bookId);
  _populateChSelect(bookId, ch);
  _pushState(bookId, String(ch));

  _loadBook(_currentVer, bookId)
    .then(function (chapters) {
      _renderChapter(bookId, ch, chapters);
      var chSel = _getEl('apoc-ch-select');
      if (chSel) chSel.value = String(ch);
    })
    .catch(function () {
      if (!resultsEl) return;
      var verName = (_apoVersions.find(function (v) { return v.id === _currentVer; }) || {}).name || _currentVer;
      resultsEl.innerHTML = '<p class="apoc-msg apoc-msg--error">'
        + escHtml((_findBook(bookId) || {}).name || bookId) + ' is not yet available in '
        + escHtml(verName) + '.'
        + '<br>Run: <code>python3 scripts/fetch-apocrypha.py ' + escHtml(_currentVer) + '</code></p>';
    });
}

function _selectFilter(filter) {
  _currentFilter = filter;
  document.querySelectorAll('.apoc-canon-chip').forEach(function (btn) {
    var active = btn.dataset.filter === filter;
    btn.classList.toggle('apoc-canon-chip--active', active);
    btn.setAttribute('aria-pressed', active ? 'true' : 'false');
  });
  var bookSel  = _getEl('apoc-book-select');
  var prevBook = bookSel && bookSel.value;
  _populateBookSelect(null);
  var books   = _getActiveBooks();
  var newBook = prevBook && books.find(function (b) { return b.id === prevBook; })
    ? prevBook : (books[0] && books[0].id);
  if (newBook) {
    if (bookSel) bookSel.value = newBook;
    _populateChSelect(newBook, 1);
    _navigateTo(newBook, 1);
  }
}

function _onVersionChange(newVerId) {
  // INTENT: Rebuilds filter chips and book list when version changes because different
  //   versions may have different scopes (full-bible vs. apocrypha-only).
  // CHANGE? If version scope or canon_order fields change in versions.json, this rebuild
  //   ensures the UI always reflects the selected version's capabilities.
  // VERIFY: Switch from WEB-CE to a non-full-bible version; chips should change from
  //   OT/Apo/NT to Catholic/Orthodox/LXX.
  _currentVer    = newVerId;
  _currentFilter = 'all';
  try { localStorage.setItem(VER_KEY, _currentVer); } catch (e) {}
  _buildFilterChips();
  var books   = _getActiveBooks();
  var initBook = books[0] && books[0].id;
  if (initBook) {
    _populateBookSelect(initBook);
    _populateChSelect(initBook, 1);
    _navigateTo(initBook, 1);
  }
}

// ── Init ──────────────────────────────────────────────────────────────────────

export function initApocryphaReader() {
  // INTENT: Entry point from app.js. Loads all metadata in parallel then builds the UI
  //   and navigates to the URL-specified book/ch (or defaults to the first book).
  // CHANGE? Detection landmark is #apoc-reader-results — if it changes, update app.js.
  // VERIFY: Open apocrypha/?book=genesis&ch=1 with WEB-CE; Genesis 1 should render.
  if (!_getEl('apoc-reader-results')) return;

  var params = _getUrlParams();

  Promise.all([_loadApoBooks(), _loadApoVersions(), _loadCanonOrders()]).then(function () {
    try { _currentVer = localStorage.getItem(VER_KEY) || ''; } catch (e) { _currentVer = ''; }
    if (!_currentVer || !_apoVersions.find(function (v) { return v.id === _currentVer; })) {
      _currentVer = _apoVersions.length ? _apoVersions[0].id : '';
    }

    _buildFilterChips();
    _populateVerSelect();

    // Resolve initial book: prefer URL param, fall back to first visible book
    var books    = _getActiveBooks();
    var initBook = (params.book && _findBook(params.book)) ? params.book : (books[0] && books[0].id);
    var initCh   = params.ch || '1';

    _populateBookSelect(initBook);
    _populateChSelect(initBook, initCh);

    // Wire controls
    var bookSel = _getEl('apoc-book-select');
    var chSel   = _getEl('apoc-ch-select');
    var verSel  = _getEl('apoc-ver-select');

    if (bookSel) {
      bookSel.addEventListener('change', function () {
        _populateChSelect(bookSel.value, 1);
        _navigateTo(bookSel.value, 1);
      });
    }
    if (chSel) {
      chSel.addEventListener('change', function () {
        var bid = bookSel ? bookSel.value : initBook;
        _navigateTo(bid, chSel.value);
      });
    }
    if (verSel) {
      verSel.addEventListener('change', function () { _onVersionChange(verSel.value); });
    }

    // Browser history navigation
    window.addEventListener('popstate', function (e) {
      if (e.state && e.state.book) {
        _populateBookSelect(e.state.book);
        _populateChSelect(e.state.book, e.state.ch);
        _loadBook(_currentVer, e.state.book).then(function (chs) {
          _renderChapter(e.state.book, e.state.ch, chs);
        }).catch(function () {
          var resultsEl = _getEl('apoc-reader-results');
          if (resultsEl) resultsEl.innerHTML = '<p class="apoc-msg apoc-msg--error">Could not load this chapter. Check your connection.</p>';
        });
      }
    });

    if (initBook) _navigateTo(initBook, initCh);

  }).catch(function (err) {
    var el = _getEl('apoc-reader-results');
    if (el) el.innerHTML = '<p class="apoc-msg apoc-msg--error">Failed to load reader: ' + escHtml(String(err)) + '</p>';
  });
}

// ── Cross-ref routing ─────────────────────────────────────────────────────────

// INTENT: Converts unwired [data-ref] elements whose book name matches a deuterocanonical
//   book into anchor links targeting apocrypha/?book=...&ch=... so refs to Sirach,
//   Wisdom, etc. in the main reader point to the right place instead of being dead.
// CHANGE? If apocrypha-books.json abbrev arrays change, the map must be rebuilt (it's
//   cached after first call). If APO_READER_URL changes, update the href template.
// VERIFY: In main reader cross-ref panel, a link with data-ref="Sirach 3:3" should
//   become <a href="...apocrypha/?book=sirach&ch=3">.
var _apoAbbrevMap = null;

function _buildAbbrevMap() {
  if (_apoAbbrevMap) return Promise.resolve(_apoAbbrevMap);
  return _loadApoBooks().then(function (books) {
    _apoAbbrevMap = {};
    books.forEach(function (b) {
      _apoAbbrevMap[b.name.toLowerCase()] = b.id;
      b.abbrevs.forEach(function (a) { _apoAbbrevMap[a.toLowerCase()] = b.id; });
    });
    return _apoAbbrevMap;
  });
}

function _parseApoRef(refStr) {
  if (!_apoAbbrevMap || !refStr) return null;
  var m = refStr.match(/^(.+?)\s+(\d+)(?::(\d+))?/);
  if (!m) return null;
  var bookId = _apoAbbrevMap[m[1].trim().toLowerCase()];
  return bookId ? { bookId: bookId, ch: m[2] || '1' } : null;
}

export function wireApoRefLinks(root) {
  _buildAbbrevMap().then(function () {
    var container = root || document;
    container.querySelectorAll('[data-ref]').forEach(function (el) {
      if (el._refWired) return;
      var parsed = _parseApoRef(el.dataset.ref);
      if (!parsed) return;
      el._refWired = true;
      var href = APO_READER_URL + '?book=' + encodeURIComponent(parsed.bookId)
               + '&ch=' + encodeURIComponent(parsed.ch);
      if (el.tagName === 'A') {
        el.href = href;
      } else {
        var a = document.createElement('a');
        a.href = href; a.className = el.className;
        a.dataset.ref = el.dataset.ref; a.textContent = el.textContent;
        el.parentNode && el.parentNode.replaceChild(a, el);
      }
    });
  });
}

export function getApoReaderUrl() { return APO_READER_URL; }
