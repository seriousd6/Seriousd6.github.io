/* search.js — Search page init, verse search, Strong's, explore/omni-search, topics search.
 *
 * Entry points:
 *   buildSearchDOM()  — called from app.js on every page; injects the global Search button
 *                       into the sidebar and wires Ctrl+K to open the search page.
 *   initSearchPage()  — called only on search/index.html; wires the full search UI.
 *
 * The page has two top-level modes toggled by [data-search-tab]:
 *   "verse"   — full-text keyword search across all Bible book JSON files.
 *   "explore" — combined omni-search: verses preview + Nave's topics + Strong's + dict + library.
 *
 * Results are written to #bsw-search-output (verse tab) or #bsw-explore-output (explore tab).
 * Sort state ("relevance" | "canonical") is persisted in localStorage.
 *
 * CSS classes used here come from bible-ui.css; the ones that matter most:
 *   Verse cards:   .bsw-search-result, .bsw-search-result__ref, .bsw-search-result__text
 *   Load more:     .omni-see-all
 *   Explore:       .omni-section, .omni-section__head, .omni-section__title, .omni-section__count
 *   Strong's:      .omni-strongs-card and its BEM children
 *   Topics:        .omni-topic-chip, .omni-topic-chip__count
 *   Dictionary:    .search-dict-result, .sdr-head, .sdr-term, .sdr-source, .sdr-brief
 *   Library:       .omni-lib-card and its BEM children
 *   History:       .search-history-dropdown, .search-history-chips, .search-history-chip
 */
'use strict';

import {
  getVersion, loadBook, parseRef, normalizeBook, metaBooks, bookLookup, bookOrder,
  SEARCH_URL, READER_URL, STRONGS_ROOT, TOPICS_ROOT, WORD_URL,
  escHtml, computeTextSimilarity, _scoreResult,
  _loadLibIndex, libIndexCache, bookCache,
  loadStrongs, _smithLoad, _smithData
} from './core.js';
import { _naveLoad, _naveData, DICT_PAGE_URL } from './library.js';
import { wireRefLinks, wireRefEl } from './wire.js';
import { _showShortcutsOverlay } from './modal.js';

// ── Session state ─────────────────────────────────────────────────────────
var _searchDebounce    = null;
// Incremented each time a new search starts; stale async results check this
// before rendering so a slow book fetch from a previous query can't overwrite newer results.
var _searchGeneration  = 0;
// Cached so re-sort and re-filter can re-render without refetching.
var _lastSearchResults = [];
var _lastSearchQuery   = '';
// "relevance" = score desc; "canonical" = Bible book order (Genesis → Revelation).
var _searchSortMode    = 'relevance';
try { _searchSortMode = localStorage.getItem('bsw_search_sort') || 'relevance'; } catch (e) {}
// "all" | "ot" | "nt" — matches lowercase data-testament attribute values.
var _filterTestament   = 'all';
// Book ID string (e.g. "GEN") or "" for all books.
var _filterBook        = '';
// Which top-level tab is active ("verse" | "explore").
var _searchPageTab     = 'verse';
var _exploreFilter     = 'all';
// Exposed so external code (e.g. the Explore tab's "Full verse search →" button) can
// programmatically switch tabs.
var _switchSearchTab   = null;

// ── buildSearchDOM ────────────────────────────────────────────────────────
// Injected on every page by app.js after books/versions load.
export function buildSearchDOM() {
  var vp = document.querySelector('.version-picker');
  if (vp && !document.getElementById('bsw-search-btn')) {
    var btn = document.createElement('button');
    btn.id        = 'bsw-search-btn';
    btn.className = 'bsw-search-btn';
    btn.setAttribute('aria-label', 'Search verses (Ctrl+K)');
    btn.textContent = 'Search';
    vp.parentNode.insertBefore(btn, vp);
    btn.addEventListener('click', function () {
      var inp = document.getElementById('bsw-search-input');
      if (inp) { inp.focus(); inp.select(); } else { window.location.href = SEARCH_URL; }
    });
  }

  // Ctrl+K: focus the search input if on the search page, otherwise navigate.
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      var inp = document.getElementById('bsw-search-input');
      if (inp) { inp.focus(); inp.select(); } else { window.location.href = SEARCH_URL; }
    }
  });

  // '?' opens the keyboard shortcuts overlay.
  // '/' focuses the reader search bar (only on the reader page).
  document.addEventListener('keydown', function (e) {
    if (e.key !== '?' && e.key !== '/') return;
    if (e.key === '/' && !document.getElementById('reader-results')) return;
    var tag = document.activeElement && document.activeElement.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
    if (e.key === '?') { e.preventDefault(); _showShortcutsOverlay(); }
  });

  var pageInput = document.getElementById('bsw-search-input');
  if (pageInput) initSearchPage(pageInput);
}

// ── initSearchPage ────────────────────────────────────────────────────────
// Wires all interactive elements on search/index.html.
export function initSearchPage(input) {
  input.focus();

  var tabBtns      = document.querySelectorAll('[data-search-tab]');
  var verseCtx     = document.getElementById('bsw-verse-ctx');
  var exploreCtx   = document.getElementById('bsw-explore-ctx');
  var filterToggle = document.getElementById('bsw-filter-toggle');
  var filterPanel  = document.getElementById('bsw-filter-panel');
  var sortRow      = document.getElementById('bsw-search-sort-row');

  // Inject the recent-searches dropdown immediately below the input.
  _injectRecentSearchesDropdown(input);

  if (filterToggle && filterPanel) {
    filterToggle.addEventListener('click', function () {
      var open = !filterPanel.hidden;
      filterPanel.hidden = open;
      filterToggle.textContent = open ? 'Filter ▾' : 'Filter ▴';
    });
  }

  function setSearchTab(tab) {
    _searchPageTab = tab;
    tabBtns.forEach(function (btn) {
      btn.classList.toggle('search-tab--active', btn.getAttribute('data-search-tab') === tab);
    });
    if (verseCtx)   verseCtx.hidden   = (tab !== 'verse');
    if (exploreCtx) exploreCtx.hidden = (tab !== 'explore');
  }

  _switchSearchTab = setSearchTab;

  tabBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var tab = btn.getAttribute('data-search-tab');
      setSearchTab(tab);
      if (tab === 'explore') {
        var q = input.value.trim();
        if (q.length >= 2) handleExploreSearch(q);
      }
    });
  });

  // Sort buttons — changing sort re-renders without refetching.
  var sortBtns = document.querySelectorAll('[data-sort]');
  sortBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      _searchSortMode = btn.getAttribute('data-sort');
      try { localStorage.setItem('bsw_search_sort', _searchSortMode); } catch (e) {}
      sortBtns.forEach(function (b) {
        b.classList.toggle('search-sort--active', b === btn);
      });
      if (_lastSearchResults.length) renderSearchResults(_lastSearchResults, _lastSearchQuery);
    });
  });

  // Testament filter — re-renders cached results without refetching.
  var testamentBtns = document.querySelectorAll('[data-testament]');
  testamentBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      _filterTestament = btn.getAttribute('data-testament');
      testamentBtns.forEach(function (b) {
        b.classList.toggle('search-filter--active', b === btn);
      });
      if (_lastSearchResults.length) renderSearchResults(_lastSearchResults, _lastSearchQuery);
    });
  });

  // Book dropdown — restricts full-text search to a single book.
  var bookSelect = document.getElementById('bsw-book-filter');
  if (bookSelect && metaBooks) {
    metaBooks.forEach(function (b) {
      var opt = document.createElement('option');
      opt.value = b.id;
      opt.textContent = b.name;
      bookSelect.appendChild(opt);
    });
    bookSelect.addEventListener('change', function () {
      _filterBook = bookSelect.value;
      if (_lastSearchResults.length) renderSearchResults(_lastSearchResults, _lastSearchQuery);
    });
  }

  // Sub-tabs (Strong's, Topics, Dictionary) — fire their own handler when activated.
  var subTabBtns = document.querySelectorAll('[data-sub-tab]');
  subTabBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var tab = btn.getAttribute('data-sub-tab');
      subTabBtns.forEach(function (b) { b.classList.toggle('sub-tab--active', b === btn); });
      document.querySelectorAll('[data-sub-ctx]').forEach(function (ctx) {
        ctx.hidden = ctx.getAttribute('data-sub-ctx') !== tab;
      });
      var q = input.value.trim();
      if (tab === 'strongs' && q) handleStrongsSearch(q);
      if (tab === 'topics'  && q) handleTopicsSearch(q);
      if (tab === 'dict'    && q) handleDictSearch(q);
    });
  });

  // Explore section filter buttons.
  document.querySelectorAll('[data-explore-filter]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      _applyExploreFilter(btn.getAttribute('data-explore-filter'));
    });
  });

  // Main input: debounced 250 ms, routes to verse or explore handler.
  input.addEventListener('input', function () {
    clearTimeout(_searchDebounce);
    var q = input.value.trim();
    _toggleRecentSearches(input, !q);
    if (!q) { _clearResults(); return; }
    _searchDebounce = setTimeout(function () {
      if (_searchPageTab === 'verse') handleSearchInput(q);
      else if (_searchPageTab === 'explore') handleExploreSearch(q);
    }, 250);
  });

  // Show recent searches on focus when input is empty.
  input.addEventListener('focus', function () {
    _toggleRecentSearches(input, !input.value.trim());
  });
  input.addEventListener('blur', function () {
    // Delay so clicks on history chips register before the dropdown hides.
    setTimeout(function () { _toggleRecentSearches(input, false); }, 200);
  });

  // Support ?q= URL parameter so other pages can link directly to a search.
  var params = new URLSearchParams(window.location.search);
  var qParam = params.get('q');
  if (qParam) { input.value = qParam; handleSearchInput(qParam); }
}

function _clearResults() {
  var out = document.getElementById('bsw-search-output');
  if (out) out.innerHTML = '';
}

// ── Recent searches dropdown ──────────────────────────────────────────────
// Injects the dropdown shell (hidden initially) directly below the search input.
// Populated and shown/hidden by _toggleRecentSearches.
//
// We wrap the input in a position:relative div so the dropdown's
// "top: calc(100% + 2px)" anchors to the bottom of the input field, not the
// bottom of the entire .search-page-input-wrap (which includes the tab row).
function _injectRecentSearchesDropdown(input) {
  if (document.getElementById('bsw-history-dropdown')) return;

  var wrapper       = document.createElement('div');
  wrapper.style.cssText = 'position:relative;';
  input.parentNode.insertBefore(wrapper, input);
  wrapper.appendChild(input);

  var drop = document.createElement('div');
  drop.id        = 'bsw-history-dropdown';
  drop.className = 'search-history-dropdown';
  drop.hidden    = true;
  wrapper.appendChild(drop);
}

// Shows or hides the recent-searches dropdown.
// When showing, re-renders history chips from localStorage so they're always fresh.
function _toggleRecentSearches(input, show) {
  var drop = document.getElementById('bsw-history-dropdown');
  if (!drop) return;
  if (!show) { drop.hidden = true; return; }

  var hist = _getSearchHistory();
  if (!hist.length) { drop.hidden = true; return; }

  var chipsHtml = hist.map(function (q) {
    return '<button class="search-history-chip" type="button">' + escHtml(q) + '</button>';
  }).join('');

  drop.innerHTML =
    '<div class="search-history-chips">' + chipsHtml + '</div>' +
    '<button class="search-history-clear" type="button">Clear history</button>';

  drop.querySelectorAll('.search-history-chip').forEach(function (chip) {
    chip.addEventListener('click', function () {
      input.value = chip.textContent;
      drop.hidden = true;
      handleSearchInput(chip.textContent);
      if (_searchPageTab === 'explore') handleExploreSearch(chip.textContent);
    });
  });

  drop.querySelector('.search-history-clear').addEventListener('click', function () {
    try { localStorage.removeItem('bsw_search_history'); } catch (e) {}
    drop.hidden = true;
  });

  drop.hidden = false;
}

// ── handleSearchInput ─────────────────────────────────────────────────────
// Main verse search handler. Fires after the 250 ms debounce.
// Two code paths:
//   1. If the query parses as a Bible reference, fetch that verse directly.
//   2. Otherwise do a full-text scan across all qualifying books.
//
// Quoted phrases ("the word was God") are supported: the quotes are stripped and
// the inner phrase is used verbatim as the search string, bypassing fuzzy matching.
export function handleSearchInput(query) {
  if (!query || query.length < 3) return;
  var gen = ++_searchGeneration;
  var version = getVersion();

  _saveSearchHistory(query);

  // Direct reference lookup — skip full-text scan for "Book Ch:V" queries.
  var parsed = parseRef(query);
  if (parsed) {
    loadBook(version, parsed.bookId).then(function (chapters) {
      if (gen !== _searchGeneration) return;
      var ch   = chapters && chapters[String(parsed.ch)];
      var text = ch && ch[String(parsed.v)];
      if (text) {
        var results = [{ ref: parsed.display, bookId: parsed.bookId,
                         ch: parsed.ch, v: parsed.v, text: text }];
        _lastSearchResults = results;
        _lastSearchQuery   = query;
        renderSearchResults(results, query);
      }
    }).catch(function () {});
    return;
  }

  // Extract the literal phrase if the query is quoted ("like this").
  // The bare `q` is used for the indexOf scan; the original `query` is kept for
  // score-ranking and history — so "love" and `"love"` produce identical ranked results.
  var literal = extractLiteral(query);
  var q = (literal || query).toLowerCase();

  var books = metaBooks || [];
  var results = [];
  var pending = 0;

  var booksToSearch = _filterBook
    ? books.filter(function (b) { return b.id === _filterBook; })
    : (_filterTestament === 'ot' ? books.filter(function (b) { return b.testament === 'OT'; })
       : _filterTestament === 'nt' ? books.filter(function (b) { return b.testament === 'NT'; })
       : books);

  booksToSearch.forEach(function (book) {
    pending++;
    loadBook(version, book.id).then(function (chapters) {
      if (gen !== _searchGeneration) { pending--; return; }
      if (chapters) {
        Object.keys(chapters).forEach(function (chStr) {
          Object.keys(chapters[chStr]).forEach(function (vStr) {
            var text = chapters[chStr][vStr];
            if (text && text.toLowerCase().indexOf(q) !== -1) {
              results.push({
                ref:    book.name + ' ' + chStr + ':' + vStr,
                bookId: book.id,
                ch:     parseInt(chStr, 10),
                v:      parseInt(vStr, 10),
                text:   text,
                // Score with the original (possibly multi-word) query, not the literal,
                // so that "love one another" ranks verses with all three words higher.
                score:  _scoreResult(text, literal || query)
              });
            }
          });
        });
      }
      pending--;
      if (pending === 0 && gen === _searchGeneration) {
        _lastSearchResults = results;
        _lastSearchQuery   = query;
        renderSearchResults(results, query);
      }
    }).catch(function () { pending--; });
  });

  if (booksToSearch.length === 0) renderSearchResults([], query);
}

// ── renderSearchResults ───────────────────────────────────────────────────
// Renders verse search results into #bsw-search-output.
// Sort modes: "relevance" (score desc) or "canonical" (Genesis → Revelation).
//
// Pagination: shows the first BATCH (50) results, then appends on "Load more" clicks.
// Each "Load more" call closes over the already-sorted array and the current offset,
// so no module-level pagination state is needed.
export function renderSearchResults(results, query) {
  var out = document.getElementById('bsw-search-output');
  if (!out) return;

  var sortRow = document.getElementById('bsw-search-sort-row');

  if (!results || !results.length) {
    out.innerHTML = '<p class="search-page-none">No results for “' + escHtml(query) + '”.</p>';
    if (sortRow) sortRow.hidden = true;
    return;
  }

  if (sortRow) sortRow.hidden = false;

  var sorted = results.slice();
  if (_searchSortMode === 'canonical') {
    sorted.sort(function (a, b) {
      var ao = bookOrder && bookOrder[a.bookId] || 0;
      var bo = bookOrder && bookOrder[b.bookId] || 0;
      if (ao !== bo) return ao - bo;
      if (a.ch !== b.ch) return a.ch - b.ch;
      return a.v - b.v;
    });
  } else {
    sorted.sort(function (a, b) { return (b.score || 0) - (a.score || 0); });
  }

  out.innerHTML = '<p class="omni-none">' + results.length + ' result' +
    (results.length !== 1 ? 's' : '') + '</p>';

  _appendVerseResultBatch(sorted, query, 0, out);
}

// Appends one batch of 50 results to the container, then attaches a "Load more"
// button if there are still results beyond this batch.
var _VERSE_BATCH = 50;

function _appendVerseResultBatch(sorted, query, offset, container) {
  var batch     = sorted.slice(offset, offset + _VERSE_BATCH);
  var remaining = sorted.length - offset - batch.length;

  // Use the extracted literal for highlighting so quoted searches highlight correctly.
  var effectiveQ = extractLiteral(query) || query;

  var html = batch.map(function (r) {
    var text = r.text || '';
    var ql   = effectiveQ.toLowerCase();
    var idx  = text.toLowerCase().indexOf(ql);
    var display = idx >= 0
      ? escHtml(text.slice(0, idx)) +
        '<mark>' + escHtml(text.slice(idx, idx + effectiveQ.length)) + '</mark>' +
        escHtml(text.slice(idx + effectiveQ.length))
      : escHtml(text);
    return '<div class="bsw-search-result">' +
      '<a class="bsw-search-result__ref ref" data-ref="' + escHtml(r.ref) + '">' +
        escHtml(r.ref) + '</a>' +
      '<p class="bsw-search-result__text">' + display + '</p>' +
      '</div>';
  }).join('');

  // Remove any existing "Load more" button before inserting the new batch.
  var old = container.querySelector('.search-load-more-btn');
  if (old) old.remove();

  container.insertAdjacentHTML('beforeend', html);
  wireRefLinks(container);

  if (remaining > 0) {
    var btnLabel = 'Load ' + Math.min(_VERSE_BATCH, remaining) + ' more' +
      ' (' + remaining + ' remaining)';
    var moreBtn = document.createElement('button');
    moreBtn.className   = 'omni-see-all search-load-more-btn';
    moreBtn.textContent = btnLabel;
    moreBtn.addEventListener('click', function () {
      _appendVerseResultBatch(sorted, query, offset + _VERSE_BATCH, container);
    });
    container.appendChild(moreBtn);
  }
}

// ── handleStrongsSearch ───────────────────────────────────────────────────
// Searches both Greek and Hebrew Strong's dictionaries.
// Matches on number, lemma, transliteration, or definition.
export function handleStrongsSearch(query) {
  var out = document.getElementById('bsw-strongs-output');
  if (!out) return;
  out.innerHTML = '<p class="omni-loading">Loading…</p>';

  var q = query.trim().toLowerCase();
  Promise.all([loadStrongs('greek'), loadStrongs('hebrew')]).then(function (dicts) {
    var results = [];
    dicts.forEach(function (dict) {
      if (!dict) return;
      Object.keys(dict).forEach(function (key) {
        var entry = dict[key];
        var lemma = (entry.lemma || '').toLowerCase();
        var trans = (entry.translit || '').toLowerCase();
        var defn  = (entry.definition || '').toLowerCase();
        if (lemma.indexOf(q) >= 0 || trans.indexOf(q) >= 0 ||
            defn.indexOf(q) >= 0 || key.toLowerCase() === q) {
          results.push({ key: key, entry: entry });
        }
      });
    });
    renderStrongsResults(results, query, out);
  }).catch(function () {
    out.innerHTML = '<p class="omni-none">Could not load Strong’s data.</p>';
  });
}

export function renderStrongsResults(results, query, out) {
  if (!out) return;
  if (!results.length) {
    out.innerHTML = '<p class="omni-none">No Strong’s entries for “' + escHtml(query) + '”.</p>';
    return;
  }
  out.innerHTML = results.slice(0, 50).map(function (r) {
    var e    = r.entry;
    var href = escHtml(WORD_URL + '?s=' + encodeURIComponent(r.key));
    return '<div class="omni-strongs-card">' +
      '<span class="omni-strongs-card__code">' + escHtml(r.key) + '</span>' +
      '<span class="omni-strongs-card__lemma">' + escHtml(e.lemma || '') + '</span>' +
      (e.translit
        ? '<span class="omni-strongs-card__translit">(' + escHtml(e.translit) + ')</span>'
        : '') +
      '<span class="omni-strongs-card__gloss">' +
        escHtml((e.definition || '').slice(0, 120)) + '</span>' +
      '<a class="omni-strongs-card__link" href="' + href + '">Study →</a>' +
    '</div>';
  }).join('');
}

// ── handleTopicsSearch ────────────────────────────────────────────────────
// Searches Nave's Topical Bible for topic titles containing the query.
export function handleTopicsSearch(query) {
  var out = document.getElementById('bsw-topics-output');
  if (!out) return;
  out.innerHTML = '<p class="omni-loading">Loading…</p>';
  _naveLoad().then(function () {
    if (!_naveData) { out.innerHTML = '<p class="omni-none">Could not load topics.</p>'; return; }
    var q   = query.toLowerCase();
    var res = _naveData.filter(function (t) { return t.title.toLowerCase().indexOf(q) >= 0; });
    if (!res.length) {
      out.innerHTML = '<p class="omni-none">No topics for “' + escHtml(query) + '”.</p>';
      return;
    }
    out.innerHTML = '<div class="omni-topics-row">' +
      res.slice(0, 100).map(function (t) {
        return '<a class="omni-topic-chip" href="' +
          escHtml(TOPICS_ROOT + '?topic=' + encodeURIComponent(t.slug)) + '">' +
          escHtml(t.title) +
          '<span class="omni-topic-chip__count"> (' + t.verses.length + ')</span>' +
        '</a>';
      }).join('') +
    '</div>';
  });
}

// ── handleDictSearch ──────────────────────────────────────────────────────
// Searches Smith's Bible Dictionary index for entries whose term contains the query.
// Writes up to 20 results into #bsw-dict-search-output (shown on the dict sub-tab).
export function handleDictSearch(query) {
  var out = document.getElementById('bsw-dict-search-output');
  if (!out) return;
  out.innerHTML = '<p class="omni-loading">Loading…</p>';
  _smithLoad().then(function () {
    if (!_smithData) {
      out.innerHTML = '<p class="omni-none">Could not load dictionary.</p>';
      return;
    }
    var q   = query.toLowerCase();
    var res = _smithData.filter(function (e) { return e.term.toLowerCase().indexOf(q) >= 0; });
    if (!res.length) {
      out.innerHTML = '<p class="omni-none">No dictionary entries for “' + escHtml(query) + '”.</p>';
      return;
    }
    out.innerHTML = res.slice(0, 20).map(function (e) {
      var href = escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id));
      return '<div class="search-dict-result">' +
        '<div class="sdr-head">' +
          '<a class="sdr-term" href="' + href + '">' + escHtml(e.term) + '</a>' +
          '<span class="sdr-source">Smith’s</span>' +
        '</div>' +
        (e.brief ? '<p class="sdr-brief">' + escHtml(e.brief) + '</p>' : '') +
      '</div>';
    }).join('');
  });
}

// ── extractLiteral / fuzzyMatchVerse / highlightMatch ─────────────────────
// Strips surrounding quotes so "grace abounding" is treated as a required phrase.
export function extractLiteral(q) {
  var m = q.match(/^"([^"]+)"$/) || q.match(/^'([^']+)'$/);
  return m ? m[1] : null;
}

export function fuzzyMatchVerse(text, query) {
  var q   = query.toLowerCase();
  var t   = text.toLowerCase();
  var lit = extractLiteral(q);
  if (lit !== null) return t.indexOf(lit) !== -1;
  return t.indexOf(q) !== -1 || computeTextSimilarity(query, text) > 30;
}

export function highlightMatch(text, query) {
  var q   = extractLiteral(query.toLowerCase()) || query.toLowerCase();
  var idx = text.toLowerCase().indexOf(q);
  if (idx < 0) return escHtml(text);
  return escHtml(text.slice(0, idx)) +
    '<mark>' + escHtml(text.slice(idx, idx + q.length)) + '</mark>' +
    escHtml(text.slice(idx + q.length));
}

// ── handleExploreSearch ───────────────────────────────────────────────────
// Omni-search on the "Explore" tab. Builds five sections inside
// #bsw-explore-output: Verses, Word Studies, Topics (Nave's), Dictionary, Library.
// Each section fills itself asynchronously; the explore filter is re-applied
// after each section updates so the show/hide state is always correct.
export function handleExploreSearch(query) {
  var out = document.getElementById('bsw-explore-output');
  if (!out) return;

  var q = query.trim();
  if (!q || q.length < 2) { out.innerHTML = ''; return; }

  // Build the five section skeletons in one pass.
  var SECTIONS = [
    { key: 'verses',     title: 'Verses' },
    { key: 'words',      title: 'Word Studies' },
    { key: 'topics',     title: 'Topics (Nave’s)' },
    { key: 'dictionary', title: 'Dictionary' },
    { key: 'library',    title: 'Library' }
  ];

  out.innerHTML = SECTIONS.map(function (s) {
    return '<section class="omni-section" data-explore-section="' + s.key + '">' +
      '<div class="omni-section__head">' +
        '<h3 class="omni-section__title">' + escHtml(s.title) + '</h3>' +
      '</div>' +
      '<div class="omni-section__body" data-explore-body="' + s.key + '">' +
        '<p class="omni-loading">Loading…</p>' +
      '</div>' +
    '</section>';
  }).join('');

  // Re-apply the active filter so already-selected sections hide correctly.
  _applyExploreFilter(_exploreFilter);

  function body(key) {
    return out.querySelector('[data-explore-body="' + key + '"]');
  }

  var vb = body('verses');
  var wb = body('words');
  var tb = body('topics');
  var db = body('dictionary');
  var lb = body('library');

  if (vb) _exploreVerses(q, vb);
  if (wb) _exploreWords(q, wb);
  if (tb) _exploreTopics(q, tb);
  if (db) _exploreDict(q, db);
  if (lb) _exploreLibrary(q, lb);
}

// ── Explore: Verses ───────────────────────────────────────────────────────
// Shows the verse if the query is a direct reference.
// For keyword queries, scans books already in the fetch cache so no new network
// requests are made — then shows up to 5 preview matches plus a link to switch
// to the full Verse Search tab.
function _exploreVerses(q, container) {
  var parsed = parseRef(q);
  if (parsed) {
    container.innerHTML =
      '<a class="bsw-search-result__ref ref" data-ref="' + escHtml(parsed.display) + '">' +
        escHtml(parsed.display) + '</a>';
    wireRefLinks(container);
    return;
  }

  // Scan only already-cached book data to avoid firing dozens of new fetches
  // just for a 5-result preview.
  var version = getVersion();
  var ql      = q.toLowerCase();
  var preview = [];

  var books = metaBooks || [];
  for (var i = 0; i < books.length && preview.length < 5; i++) {
    var cacheKey = version + ':' + books[i].id;
    var chapters = bookCache[cacheKey];
    if (!chapters) continue;
    var chKeys = Object.keys(chapters);
    for (var ci = 0; ci < chKeys.length && preview.length < 5; ci++) {
      var ch   = chapters[chKeys[ci]];
      var vKeys = Object.keys(ch);
      for (var vi = 0; vi < vKeys.length && preview.length < 5; vi++) {
        var text = ch[vKeys[vi]];
        if (text && text.toLowerCase().indexOf(ql) !== -1) {
          preview.push({
            ref:  books[i].name + ' ' + chKeys[ci] + ':' + vKeys[vi],
            text: text
          });
        }
      }
    }
  }

  var switchBtn = '<button class="omni-see-all" type="button" data-switch-tab="verse">' +
    'Full verse search →</button>';

  if (!preview.length) {
    container.innerHTML = '<p class="omni-none">No cached matches. ' + switchBtn + '</p>';
  } else {
    var html = preview.map(function (r) {
      var idx     = r.text.toLowerCase().indexOf(ql);
      var display = idx >= 0
        ? escHtml(r.text.slice(0, idx)) +
          '<mark>' + escHtml(r.text.slice(idx, idx + q.length)) + '</mark>' +
          escHtml(r.text.slice(idx + q.length))
        : escHtml(r.text);
      return '<div class="bsw-search-result">' +
        '<a class="bsw-search-result__ref ref" data-ref="' + escHtml(r.ref) + '">' +
          escHtml(r.ref) + '</a>' +
        '<p class="bsw-search-result__text">' + display + '</p>' +
      '</div>';
    }).join('');
    container.innerHTML = html + '<p class="omni-none" style="margin-top:.5rem">' + switchBtn + '</p>';
    wireRefLinks(container);
  }

  // Wire the tab-switch button so clicking it switches to Verse Search and fires the search.
  container.querySelectorAll('[data-switch-tab]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (_switchSearchTab) {
        _switchSearchTab('verse');
        var inp = document.getElementById('bsw-search-input');
        if (inp && inp.value.trim()) handleSearchInput(inp.value.trim());
      }
    });
  });
}

// ── Explore: Word Studies ─────────────────────────────────────────────────
// If the query is a Strong's number (G/H + digits), link directly to the word study page.
// Otherwise search both Greek and Hebrew Strong's dictionaries for matching
// lemma or transliteration and show up to 4 results as cards.
function _exploreWords(q, container) {
  // Direct Strong's number — skip the dictionary scan entirely.
  if (/^[GgHh]\d+$/.test(q.trim())) {
    var id   = q.trim().toUpperCase();
    var href = escHtml(WORD_URL + '?s=' + encodeURIComponent(id));
    container.innerHTML =
      '<a class="omni-see-all" href="' + href + '">' +
        'Open word study for ' + escHtml(id) + ' →</a>';
    return;
  }

  container.innerHTML = '<p class="omni-loading">Loading…</p>';

  var ql = q.toLowerCase();
  Promise.all([loadStrongs('greek'), loadStrongs('hebrew')]).then(function (dicts) {
    var results = [];
    dicts.forEach(function (dict) {
      if (!dict) return;
      Object.keys(dict).forEach(function (key) {
        var e     = dict[key];
        var lemma = (e.lemma || '').toLowerCase();
        var trans = (e.translit || '').toLowerCase();
        // Match on lemma or transliteration; skip definition to keep results tight.
        if (lemma.indexOf(ql) >= 0 || trans.indexOf(ql) >= 0 || key.toLowerCase() === ql) {
          results.push({ key: key, entry: e });
        }
      });
    });

    if (!results.length) {
      container.innerHTML = '<p class="omni-none">No Strong’s entries found.</p>';
      return;
    }

    container.innerHTML = results.slice(0, 4).map(function (r) {
      var e    = r.entry;
      var href = escHtml(WORD_URL + '?s=' + encodeURIComponent(r.key));
      return '<div class="omni-strongs-card">' +
        '<span class="omni-strongs-card__code">' + escHtml(r.key) + '</span>' +
        '<span class="omni-strongs-card__lemma">' + escHtml(e.lemma || '') + '</span>' +
        (e.translit
          ? '<span class="omni-strongs-card__translit">(' + escHtml(e.translit) + ')</span>'
          : '') +
        '<span class="omni-strongs-card__gloss">' +
          escHtml((e.definition || '').slice(0, 100)) + '</span>' +
        '<a class="omni-strongs-card__link" href="' + href + '">Study →</a>' +
      '</div>';
    }).join('') +
    (results.length > 4
      ? '<a class="omni-see-all" href="' + escHtml(SEARCH_URL + '?q=' + encodeURIComponent(q)) +
          '">See all ' + results.length + ' Strong’s matches →</a>'
      : '');
  }).catch(function () {
    container.innerHTML = '<p class="omni-none">Could not load Strong’s data.</p>';
  });
}

// ── Explore: Topics (Nave's) ──────────────────────────────────────────────
// Shows up to 20 Nave's topic chips whose title contains the query string.
function _exploreTopics(q, container) {
  _naveLoad().then(function () {
    if (!_naveData) { container.innerHTML = '<p class="omni-none">—</p>'; return; }
    var ql  = q.toLowerCase();
    var res = _naveData.filter(function (t) { return t.title.toLowerCase().indexOf(ql) >= 0; });
    if (!res.length) { container.innerHTML = '<p class="omni-none">No topics found.</p>'; return; }
    container.innerHTML = '<div class="omni-topics-row">' +
      res.slice(0, 20).map(function (t) {
        return '<a class="omni-topic-chip" href="' +
          escHtml(TOPICS_ROOT + '?topic=' + encodeURIComponent(t.slug)) + '">' +
          escHtml(t.title) +
          ' <span class="omni-topic-chip__count">(' + t.verses.length + ')</span></a>';
      }).join('') +
    '</div>';
  });
}

// ── Explore: Dictionary ───────────────────────────────────────────────────
// Searches Smith's Bible Dictionary index for terms containing the query.
// Shows up to 5 entries with brief descriptions and links to the dictionary page.
function _exploreDict(q, container) {
  _smithLoad().then(function () {
    if (!_smithData) { container.innerHTML = '<p class="omni-none">—</p>'; return; }
    var ql  = q.toLowerCase();
    var res = _smithData.filter(function (e) { return e.term.toLowerCase().indexOf(ql) >= 0; });
    if (!res.length) {
      container.innerHTML = '<p class="omni-none">No dictionary entries found.</p>';
      return;
    }
    container.innerHTML = res.slice(0, 5).map(function (e) {
      var href = escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id));
      return '<div class="search-dict-result">' +
        '<div class="sdr-head">' +
          '<a class="sdr-term" href="' + href + '">' + escHtml(e.term) + '</a>' +
          '<span class="sdr-source">Smith’s</span>' +
        '</div>' +
        (e.brief ? '<p class="sdr-brief">' + escHtml(e.brief.slice(0, 160)) + '</p>' : '') +
      '</div>';
    }).join('') +
    (res.length > 5
      ? '<a class="omni-see-all" href="' + escHtml(DICT_PAGE_URL) + '">Browse full dictionary →</a>'
      : '');
  }).catch(function () {
    container.innerHTML = '<p class="omni-none">Could not load dictionary.</p>';
  });
}

// ── Explore: Library ──────────────────────────────────────────────────────
// Filters the library index (confessions, catechisms, etc.) by title substring
// and shows matching documents as cards linking to their library pages.
function _exploreLibrary(q, container) {
  _loadLibIndex().then(function (index) {
    if (!index) { container.innerHTML = '<p class="omni-none">—</p>'; return; }
    var ql  = q.toLowerCase();
    var res = index.filter(function (doc) {
      return doc.title.toLowerCase().indexOf(ql) >= 0;
    });
    if (!res.length) {
      container.innerHTML = '<p class="omni-none">No library documents found.</p>';
      return;
    }
    container.innerHTML = res.slice(0, 8).map(function (doc) {
      // href is a site-root-relative path from the index (e.g. "library/apostles-creed/").
      var href = escHtml('/' + doc.href);
      return '<a class="omni-lib-card" href="' + href + '">' +
        '<span class="omni-lib-card__abbrev">' + escHtml(doc.abbrev || '') + '</span>' +
        '<span class="omni-lib-card__title">' + escHtml(doc.title) + '</span>' +
        (doc.year ? '<span class="omni-lib-card__year">' + doc.year + '</span>' : '') +
      '</a>';
    }).join('');
  }).catch(function () {
    container.innerHTML = '<p class="omni-none">Could not load library index.</p>';
  });
}

// ── _applyExploreFilter ───────────────────────────────────────────────────
// Shows/hides explore sections based on the active filter button.
// "all" shows everything; any other value shows only the matching section.
function _applyExploreFilter(filter) {
  _exploreFilter = filter;
  document.querySelectorAll('[data-explore-filter]').forEach(function (btn) {
    btn.classList.toggle('explore-filter--active',
      btn.getAttribute('data-explore-filter') === filter);
  });
  document.querySelectorAll('[data-explore-section]').forEach(function (sec) {
    var show = filter === 'all' || sec.getAttribute('data-explore-section') === filter;
    sec.hidden = !show;
  });
}

// ── Topics index for search (site-wide topic pages) ───────────────────────
// Placeholder for a future index of /topics/* pages.
var _topicsIndexCache = null;

function _buildTopicsIndex() {
  if (_topicsIndexCache) return Promise.resolve(_topicsIndexCache);
  return Promise.resolve([]);
}

// ── Search history ────────────────────────────────────────────────────────
// Persists the 10 most recent search queries in localStorage.
function _saveSearchHistory(query) {
  if (!query || query.length < 2) return;
  try {
    var hist = JSON.parse(localStorage.getItem('bsw_search_history') || '[]');
    hist = hist.filter(function (q) { return q !== query; });
    hist.unshift(query);
    if (hist.length > 10) hist.length = 10;
    localStorage.setItem('bsw_search_history', JSON.stringify(hist));
  } catch (e) {}
}

export function _getSearchHistory() {
  try { return JSON.parse(localStorage.getItem('bsw_search_history') || '[]'); }
  catch (e) { return []; }
}
