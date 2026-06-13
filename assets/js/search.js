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
  SEARCH_URL, READER_URL, STRONGS_ROOT, TOPICS_ROOT, WORD_URL, TOPICS_INDEX_URL,
  escHtml, computeTextSimilarity, _scoreResult,
  _loadLibIndex, _loadLibSearch, libIndexCache, bookCache,
  loadStrongs, _smithLoad, _smithData, _resolve,
  _torreyLoad, _torreyData, _hitchLoad, _hitchData
} from './core.js';

var _LIBRARY_ROOT = _resolve('../../library/');
import { _naveLoad, _naveData, DICT_PAGE_URL } from './library.js';
import { wireRefLinks, wireRefEl } from './wire.js';
import { _showShortcutsOverlay } from './modal.js';
import { autoTagTermsWhenReady } from './terms.js';

// ── Session state ─────────────────────────────────────────────────────────
var _searchDebounce    = null;
// INTENT: _searchGeneration is incremented at the top of every handleExploreSearch
//   call. Each async section captures the value at start time as a local `gen`
//   and checks `if (gen !== _searchGeneration) return` before writing results.
//   This prevents a slow book-fetch from a previous query overwriting faster
//   results from a newer one. Removing or moving any gen guard causes interleaved
//   results during fast typing.
// CHANGE? Any new async section added to handleExploreSearch MUST capture
//   `var gen = _searchGeneration` at the top and guard result-writing with
//   `if (gen !== _searchGeneration) return`.
// VERIFY: Type "love" quickly followed by "faith"; only "faith" results should
//   appear — no "love" results should flash in or overwrite.
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
// OS-C: module-level ref so _toggleRecentSearches can call it without knowing the active tab
var _fireSearch        = null;

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

  // Hub browse tabs — show an iframe panel instead of the search panel.
  var _hubTabs = ['topics', 'guides', 'dictionary', 'wordcloud'];

  function setSearchTab(tab) {
    _searchPageTab = tab;
    tabBtns.forEach(function (btn) {
      var isActive = btn.getAttribute('data-search-tab') === tab;
      btn.classList.toggle('search-tab--active', isActive);
      btn.setAttribute('aria-selected', String(isActive));
    });

    var isHubTab    = _hubTabs.indexOf(tab) !== -1;
    var searchPanel = document.getElementById('search-search-panel');
    if (searchPanel) searchPanel.hidden = isHubTab;

    // Activate the matching hub panel and lazy-load its iframe.
    _hubTabs.forEach(function (ht) {
      var panel = document.getElementById('search-hub-' + ht);
      if (!panel) return;
      var isThis = (ht === tab);
      panel.classList.toggle('explore-hub-panel--active', isThis);
      if (isThis) {
        var iframe = panel.querySelector('iframe');
        if (iframe && !iframe.getAttribute('src') && iframe.dataset.src) {
          iframe.src = iframe.dataset.src;
        }
      }
    });

    if (!isHubTab) {
      if (verseCtx)   verseCtx.hidden   = (tab !== 'verse');
      if (exploreCtx) exploreCtx.hidden = (tab !== 'explore');
    }

    // Persist tab selection.
    history.replaceState(null, '', '?tab=' + tab);
    try { localStorage.setItem('bsw_explore_tab', tab); } catch (e) {}
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
  // OS-A: apply initial active state from persisted sort mode
  sortBtns.forEach(function (b) {
    b.classList.toggle('search-mode-btn--active', b.getAttribute('data-sort') === _searchSortMode);
  });
  sortBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      _searchSortMode = btn.getAttribute('data-sort');
      try { localStorage.setItem('bsw_search_sort', _searchSortMode); } catch (e) {}
      sortBtns.forEach(function (b) {
        b.classList.toggle('search-mode-btn--active', b === btn);
      });
      if (_lastSearchResults.length) renderSearchResults(_lastSearchResults, _lastSearchQuery);
    });
  });

  // Testament filter — re-renders cached results without refetching.
  // OS-A: use search-mode-btn--active (has CSS rules) instead of search-filter--active (no rules)
  var testamentBtns = document.querySelectorAll('[data-testament]');
  // OS-A: apply initial active state
  testamentBtns.forEach(function (b) {
    b.classList.toggle('search-mode-btn--active', b.getAttribute('data-testament') === _filterTestament);
  });
  testamentBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      _filterTestament = btn.getAttribute('data-testament');
      testamentBtns.forEach(function (b) {
        b.classList.toggle('search-mode-btn--active', b === btn);
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

  // Shared trigger: cancels any pending debounce and fires the search immediately.
  // Assigned to the module-level _fireSearch so _toggleRecentSearches can use it (OS-C).
  _fireSearch = function () {
    clearTimeout(_searchDebounce);
    var q = input.value.trim();
    if (!q) { _clearResults(); return; }
    if (_searchPageTab === 'verse') handleSearchInput(q);
    else if (_searchPageTab === 'explore') handleExploreSearch(q);
  };

  // Search button — forces an immediate re-run on click.
  var goBtn = document.getElementById('bsw-search-go');
  if (goBtn) goBtn.addEventListener('click', _fireSearch);

  // Enter key on the input also bypasses the debounce.
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { e.preventDefault(); _fireSearch(); }
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

  // OS-J: when switching back to verse tab, re-render cached results immediately
  // so the pane isn't blank after visiting Explore.
  tabBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (btn.getAttribute('data-search-tab') === 'verse' &&
          _lastSearchResults.length && _lastSearchQuery) {
        renderSearchResults(_lastSearchResults, _lastSearchQuery);
      }
    });
  });

  // Support ?q= and ?tab= URL parameters; also restore from localStorage.
  var params = new URLSearchParams(window.location.search);
  var qParam   = params.get('q');
  var tabParam = params.get('tab') || (function () {
    try { return localStorage.getItem('bsw_explore_tab'); } catch (e) { return null; }
  }());

  if (tabParam && tabParam !== 'verse') {
    setSearchTab(tabParam);
    if (tabParam === 'explore' && qParam) {
      input.value = qParam;
      handleExploreSearch(qParam);
    }
  } else if (qParam) {
    input.value = qParam;
    handleSearchInput(qParam);
  }
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
      // OS-C: use _fireSearch so only the active tab's handler runs (not both)
      input.value = chip.textContent;
      drop.hidden = true;
      if (_fireSearch) _fireSearch();
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
  // INTENT: Fast path for verse references; bypasses the full-text scan and loading bar,
  //   so we show a brief "Looking up…" indicator and surface any fetch error explicitly.
  // CHANGE? The element ID 'bsw-search-output' is also used by the full-text path below;
  //   if renamed, update both this block and the _searchOut assignment at line ~443.
  // VERIFY: Block *.json in DevTools Network, type "John 3:16" — output should show
  //   "Could not load…" rather than staying blank or stuck on a previous result.
  var parsed = parseRef(query);
  if (parsed) {
    var _refOut = document.getElementById('bsw-search-output');
    if (_refOut) _refOut.innerHTML = '<p class="omni-loading">Looking up ' + escHtml(parsed.display) + '…</p>';
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
    }).catch(function () {
      var out = document.getElementById('bsw-search-output');
      if (out) out.innerHTML = '<p class="search-page-none">Could not load “' + escHtml(query) + '”. Check your connection and try again.</p>';
    });
    return;
  }

  // Extract the literal phrase if the query is quoted ("like this").
  // The bare `q` is used for the indexOf scan; the original `query` is kept for
  // score-ranking and history — so "love" and `"love"` produce identical ranked results.
  var literal = extractLiteral(query);
  var q = (literal || query).toLowerCase();
  // AND logic: split unquoted multi-word queries so every word must appear in the verse.
  var andWords = (!literal && q.indexOf(' ') !== -1) ? q.split(/\s+/).filter(Boolean) : null;

  var books = metaBooks || [];
  var results = [];
  var pending = 0;

  var booksToSearch = _filterBook
    ? books.filter(function (b) { return b.id === _filterBook; })
    : (_filterTestament === 'ot' ? books.filter(function (b) { return b.testament === 'OT'; })
       : _filterTestament === 'nt' ? books.filter(function (b) { return b.testament === 'NT'; })
       : books);

  // Show a loading indicator immediately so the user knows work is underway.
  // INTENT: When no filter narrows the search, append a filter tip so users know they can reduce
  //   the 66-book concurrent fetch by selecting OT / NT / Book first. This doesn't batch the
  //   requests but reduces how often cold 66-book loads happen.
  // CHANGE? If the filter UI changes from OT/NT/Book buttons to something else, update the tip text.
  // VERIFY: Search "love" with no filter — loading message should include "Tip: use OT/NT/Book…".
  //   Search "grace" with OT selected — tip should NOT appear (booksToSearch.length < 66).
  var _searchOut = document.getElementById('bsw-search-output');
  var _sortRow   = document.getElementById('bsw-search-sort-row');
  var _tipHtml   = (booksToSearch.length === 66)
    ? ' <span class="omni-filter-tip">Tip: use OT / NT / Book filters to search faster.</span>'
    : '';
  if (_searchOut) _searchOut.innerHTML = '<p class="omni-loading">Searching ' + booksToSearch.length + ' books…' + _tipHtml + '</p>';
  if (_sortRow) _sortRow.hidden = true;
  var _partialDone = false;

  booksToSearch.forEach(function (book) {
    pending++;
    loadBook(version, book.id).then(function (chapters) {
      if (gen !== _searchGeneration) { pending--; return; }
      if (chapters) {
        Object.keys(chapters).forEach(function (chStr) {
          Object.keys(chapters[chStr]).forEach(function (vStr) {
            var text = chapters[chStr][vStr];
            var tl   = text && text.toLowerCase();
            var matches = tl && (andWords
              ? andWords.every(function (w) { return tl.indexOf(w) !== -1; })
              : tl.indexOf(q) !== -1);
            if (matches) {
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
      // Render a first-pass preview as soon as 20+ results accumulate so the user
      // sees something while the remaining books still load.
      if (!_partialDone && results.length >= 20 && gen === _searchGeneration) {
        _partialDone = true;
        renderSearchResults(results.slice(), query);
      }
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
    out.innerHTML = '<p class="search-page-none">No results for "' + escHtml(query) + '".</p>';
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

  // OS-B: post-filter by the active testament/book filter so switching filters
  // immediately re-scopes already-loaded results without a new search.
  var bookMetaMap = Object.create(null);
  if (metaBooks) metaBooks.forEach(function (b) { bookMetaMap[b.id] = b; });
  if (_filterBook) {
    sorted = sorted.filter(function (r) { return r.bookId === _filterBook; });
  } else if (_filterTestament !== 'all') {
    sorted = sorted.filter(function (r) {
      var m = bookMetaMap[r.bookId];
      return m && m.testament.toLowerCase() === _filterTestament;
    });
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

  var literal    = extractLiteral(query);
  var effectiveQ = literal || query;
  var ql         = effectiveQ.toLowerCase();
  // AND queries highlight each word separately; phrase and single-word queries use one mark.
  var andWords   = (!literal && ql.indexOf(' ') !== -1) ? ql.split(/\s+/).filter(Boolean) : null;

  var html = batch.map(function (r) {
    var text    = r.text || '';
    var display = andWords ? _highlightMulti(text, andWords) : (function () {
      var idx = text.toLowerCase().indexOf(ql);
      return idx >= 0
        ? escHtml(text.slice(0, idx)) +
          '<mark>' + escHtml(text.slice(idx, idx + ql.length)) + '</mark>' +
          escHtml(text.slice(idx + ql.length))
        : escHtml(text);
    })();
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
  container.querySelectorAll('.bsw-search-result__text').forEach(autoTagTermsWhenReady);

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
    out.innerHTML = "<p class=\"omni-none\">Could not load Strong's data.</p>";
  });
}

export function renderStrongsResults(results, query, out) {
  if (!out) return;
  if (!results.length) {
    out.innerHTML = "<p class=\"omni-none\">No Strong's entries for \"" + escHtml(query) + "\".</p>";
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
      out.innerHTML = '<p class="omni-none">No topics for "' + escHtml(query) + '".</p>';
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
      out.innerHTML = '<p class="omni-none">No dictionary entries for "' + escHtml(query) + '".</p>';
      return;
    }
    out.innerHTML = res.slice(0, 20).map(function (e) {
      var href = escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id));
      return '<div class="search-dict-result">' +
        '<div class="sdr-head">' +
          '<a class="sdr-term" href="' + href + '">' + escHtml(e.term) + '</a>' +
          "<span class=\"sdr-source\">Smith's</span>" +
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

// _highlightMulti: marks every occurrence of each word in `words` within `text`.
// Ranges are merged so overlapping matches don't produce nested <mark> tags.
function _highlightMulti(text, words) {
  if (!words || !words.length) return escHtml(text);
  var tl = text.toLowerCase();
  var ranges = [];
  words.forEach(function (w) {
    var i = 0, found;
    while ((found = tl.indexOf(w, i)) !== -1) {
      ranges.push([found, found + w.length]);
      i = found + w.length;
    }
  });
  if (!ranges.length) return escHtml(text);
  ranges.sort(function (a, b) { return a[0] - b[0]; });
  var merged = [ranges[0].slice()];
  for (var i = 1; i < ranges.length; i++) {
    var last = merged[merged.length - 1];
    if (ranges[i][0] <= last[1]) last[1] = Math.max(last[1], ranges[i][1]);
    else merged.push(ranges[i].slice());
  }
  var out = '', pos = 0;
  merged.forEach(function (r) {
    out += escHtml(text.slice(pos, r[0]));
    out += '<mark>' + escHtml(text.slice(r[0], r[1])) + '</mark>';
    pos = r[1];
  });
  return out + escHtml(text.slice(pos));
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
    { key: 'topics',     title: "Topics (Nave's)" },
    { key: 'torrey',     title: 'Torrey Topics' },
    { key: 'dictionary', title: 'Dictionary' },
    { key: 'names',      title: 'Bible Names' },
    { key: 'library',    title: 'Library' },
    { key: 'guides',     title: 'Study Guides' }
  ];

  out.innerHTML = SECTIONS.map(function (s) {
    return '<section class="omni-section" data-explore-section="' + s.key + '">' +
      '<div class="omni-section__head">' +
        '<h3 class="omni-section__title">' + escHtml(s.title) + '</h3>' +
        '<span class="omni-section__count" data-explore-count="' + s.key + '"></span>' +
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

  var vb  = body('verses');
  var wb  = body('words');
  var tb  = body('topics');
  var rrb = body('torrey');
  var db  = body('dictionary');
  var nb  = body('names');
  var lb  = body('library');
  var gb  = body('guides');

  if (vb)  _exploreVerses(q, vb);
  if (wb)  _exploreWords(q, wb);
  if (tb)  _exploreTopics(q, tb);
  if (rrb) _exploreTorrey(q, rrb);
  if (db)  _exploreDict(q, db);
  if (nb)  _exploreNames(q, nb);
  if (lb)  _exploreLibrary(q, lb);
  if (gb)  _exploreGuides(q, gb);
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

  _setExploreCount('verses', preview.length);
  if (!preview.length) {
    container.innerHTML = '<p class="omni-none">Switch to Verse Search for full results. ' + switchBtn + '</p>';
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
    container.querySelectorAll('.bsw-search-result__text').forEach(autoTagTermsWhenReady);
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
  // Whole-word boundary check so "love" doesn't match "beloved" as a primary hit.
  var wordRe = new RegExp('\\b' + ql.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b', 'i');
  Promise.all([loadStrongs('greek'), loadStrongs('hebrew')]).then(function (dicts) {
    var primary = [];   // lemma / translit / number matches
    var byDefn  = [];   // definition contains the query as a whole word
    dicts.forEach(function (dict) {
      if (!dict) return;
      Object.keys(dict).forEach(function (key) {
        var e     = dict[key];
        var lemma = (e.lemma || '').toLowerCase();
        var trans = (e.translit || '').toLowerCase();
        var defn  = e.definition || '';
        if (lemma.indexOf(ql) >= 0 || trans.indexOf(ql) >= 0 || key.toLowerCase() === ql) {
          primary.push({ key: key, entry: e });
        } else if (wordRe.test(defn)) {
          byDefn.push({ key: key, entry: e });
        }
      });
    });

    // Primary matches first, then definition matches; cap display at 8.
    var results = primary.concat(byDefn);
    if (!results.length) {
      _setExploreCount('words', 0);
      container.innerHTML = "<p class=\"omni-none\">No Strong's entries found.</p>";
      return;
    }

    _setExploreCount('words', results.length);
    var shown = results.slice(0, 8);
    container.innerHTML = shown.map(function (r) {
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
    (results.length > 8
      ? '<a class="omni-see-all" href="' + escHtml(WORD_URL + '?s=' + encodeURIComponent(q)) +
          '">See all ' + results.length + " matches →</a>"
      : '');
  }).catch(function () {
    container.innerHTML = "<p class=\"omni-none\">Could not load Strong's data.</p>";
  });
}

// ── Explore: Topics (Nave's) ──────────────────────────────────────────────
// Shows up to 20 Nave's topic chips whose title contains the query string.
function _exploreTopics(q, container) {
  _naveLoad().then(function () {
    if (!_naveData) { container.innerHTML = '<p class="omni-none">—</p>'; return; }
    var ql  = q.toLowerCase();
    var res = _naveData.filter(function (t) { return t.title.toLowerCase().indexOf(ql) >= 0; });
    _setExploreCount('topics', res.length);
    if (!res.length) { container.innerHTML = '<p class="omni-none">No topics found.</p>'; return; }
    container.innerHTML = '<div class="omni-topics-row">' +
      res.slice(0, 20).map(function (t) {
        return '<a class="omni-topic-chip" href="' +
          escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(t.slug) + '&src=nave') + '">' +
          escHtml(t.title) +
          ' <span class="omni-topic-chip__count">(' + t.verses.length + ')</span></a>';
      }).join('') +
    '</div>';
  });
}

// ── Explore: Torrey Topics ────────────────────────────────────────────────
// OS-G: Torrey's New Topical Textbook — same pattern as Nave's topics.
function _exploreTorrey(q, container) {
  _torreyLoad().then(function () {
    if (!_torreyData) { container.innerHTML = '<p class="omni-none">—</p>'; return; }
    var ql  = q.toLowerCase();
    var res = _torreyData.filter(function (t) { return t.title.toLowerCase().indexOf(ql) >= 0; });
    _setExploreCount('torrey', res.length);
    if (!res.length) { container.innerHTML = '<p class="omni-none">No Torrey topics found.</p>'; return; }
    container.innerHTML = '<div class="omni-topics-row">' +
      res.slice(0, 20).map(function (t) {
        return '<a class="omni-topic-chip" href="' +
          escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(t.slug) + '&src=torrey') + '">' +
          escHtml(t.title) +
          ' <span class="omni-topic-chip__count">(' + t.verses.length + ')</span></a>';
      }).join('') +
    '</div>';
  });
}

// ── Explore: Bible Names (Hitchcock) ──────────────────────────────────────
// OS-H: Hitchcock's Bible Names dictionary — useful for proper-noun queries.
function _exploreNames(q, container) {
  _hitchLoad().then(function () {
    if (!_hitchData) { container.innerHTML = '<p class="omni-none">—</p>'; return; }
    var ql  = q.toLowerCase();
    var res = _hitchData.filter(function (e) {
      return e.term.toLowerCase().indexOf(ql) >= 0 ||
             e.meaning.toLowerCase().indexOf(ql) >= 0;
    });
    _setExploreCount('names', res.length);
    if (!res.length) { container.innerHTML = '<p class="omni-none">No name entries found.</p>'; return; }
    container.innerHTML = res.slice(0, 10).map(function (e) {
      var href = escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id) + '&src=hitchcock');
      return '<div class="search-dict-result">' +
        '<div class="sdr-head">' +
          '<a class="sdr-term" href="' + href + '">' + escHtml(e.term) + '</a>' +
          '<span class="sdr-source">Hitchcock</span>' +
        '</div>' +
        '<p class="sdr-brief">' + escHtml(e.meaning) + '</p>' +
      '</div>';
    }).join('');
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
    _setExploreCount('dictionary', res.length);
    if (!res.length) {
      container.innerHTML = '<p class="omni-none">No dictionary entries found.</p>';
      return;
    }
    container.innerHTML = res.slice(0, 5).map(function (e) {
      var href = escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id));
      return '<div class="search-dict-result">' +
        '<div class="sdr-head">' +
          '<a class="sdr-term" href="' + href + '">' + escHtml(e.term) + '</a>' +
          "<span class=\"sdr-source\">Smith's</span>" +
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
// Full-text search across all library documents using the passage-level search
// index (data/library/search-index.json). Falls back to title matching via the
// manifest when a doc has no entries in the search index.
function _exploreLibrary(q, container) {
  Promise.all([
    _loadLibIndex().catch(function () { return null; }),
    _loadLibSearch().catch(function () { return null; })
  ]).then(function (both) {
    var index     = both[0];
    var searchIdx = both[1];

    if (!index && !searchIdx) { container.innerHTML = '<p class="omni-none">—</p>'; return; }

    var ql = q.toLowerCase();

    // Build docId → index entry map for title/year/abbrev lookup.
    var indexMap = Object.create(null);
    if (index) index.forEach(function (d) { indexMap[d.id] = d; });

    // Full-text scan: first matching passage per document wins; store snippet + section ref.
    var hits = Object.create(null);
    if (searchIdx) {
      searchIdx.forEach(function (entry) {
        if (hits[entry.docId]) return;
        var textL = (entry.text || '').toLowerCase();
        var headL = (entry.heading || '').toLowerCase();
        if (textL.indexOf(ql) !== -1 || headL.indexOf(ql) !== -1) {
          var idx     = textL.indexOf(ql);
          var snippet = '';
          if (idx !== -1) {
            var s = Math.max(0, idx - 60);
            var e = Math.min(entry.text.length, idx + ql.length + 80);
            snippet = (s > 0 ? '…' : '') + entry.text.slice(s, e).trim() +
                      (e < entry.text.length ? '…' : '');
          }
          hits[entry.docId] = { docId: entry.docId, snippet: snippet, ref: entry.ref };
        }
      });
    }

    // Fallback: title match for docs not represented in the search index.
    if (index) {
      index.forEach(function (doc) {
        if (!hits[doc.id] && doc.title.toLowerCase().indexOf(ql) !== -1) {
          hits[doc.id] = { docId: doc.id, snippet: doc.desc || '', ref: null };
        }
      });
    }

    var results = Object.keys(hits).map(function (k) { return hits[k]; });
    _setExploreCount('library', results.length);
    if (!results.length) {
      container.innerHTML = '<p class="omni-none">No library documents found.</p>';
      return;
    }

    container.innerHTML = results.slice(0, 6).map(function (hit) {
      var doc      = indexMap[hit.docId] || {};
      // section param is 0-based; search index ref is 1-based — subtract 1
      var secIdx   = hit.ref ? Math.max(0, parseInt(hit.ref, 10) - 1) : 0;
      var secParam = secIdx > 0 ? '&section=' + secIdx : '';
      var href = escHtml(_LIBRARY_ROOT + '?doc=' + encodeURIComponent(hit.docId) +
                         secParam + '&focus=1');
      return '<a class="omni-lib-card" href="' + href + '">' +
        (doc.abbrev ? '<span class="omni-lib-card__abbrev">' + escHtml(doc.abbrev) + '</span>' : '') +
        '<span class="omni-lib-card__title">' + escHtml(doc.title || hit.docId) + '</span>' +
        (doc.year ? '<span class="omni-lib-card__year">' + doc.year + '</span>' : '') +
        (hit.snippet ? '<span class="omni-lib-card__snippet">' + highlightMatch(hit.snippet, q) + '</span>' : '') +
      '</a>';
    }).join('');
  }).catch(function () {
    container.innerHTML = '<p class="omni-none">Could not load library.</p>';
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

// OS-F: updates the count badge in a section header
function _setExploreCount(key, count) {
  var el = document.querySelector('[data-explore-count="' + key + '"]');
  if (el) el.textContent = count > 0 ? String(count) : '';
}

// ── Topics index for search (site-wide topic pages) ───────────────────────
// Fetches data/topics-index.json — a manifest of all site study-guide pages.
var _topicsIndexCache = null;

function _buildTopicsIndex() {
  if (_topicsIndexCache) return Promise.resolve(_topicsIndexCache);
  return fetch(TOPICS_INDEX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (d) { _topicsIndexCache = d; return d; })
    .catch(function () { return []; });
}

// ── Explore: Study Guides ─────────────────────────────────────────────────
// INTENT: Searches site study-guide pages using TOPICS_INDEX_URL (data/topics-index.json).
//   When a guide entry has an explicit `href` field, that path is used directly
//   because study guides live at study-guides/, not the default topics/ path.
//   Falling back to TOPICS_ROOT + slug would produce broken links for study guides.
// CHANGE? If study guides move to a different URL structure, update the href
//   fallback path here and the `href` field generation in topics-index.json.
// VERIFY: Search "hebrews" in Explore; the result link should go to
//   study-guides/hebrews/, not topics/hebrews/.
function _exploreGuides(q, container) {
  _buildTopicsIndex().then(function (guides) {
    if (!guides || !guides.length) {
      container.innerHTML = '<p class="omni-none">No study guides found.</p>';
      return;
    }
    var ql  = q.toLowerCase();
    var res = guides.filter(function (g) {
      return g.title.toLowerCase().indexOf(ql) !== -1 ||
             (g.desc && g.desc.toLowerCase().indexOf(ql) !== -1);
    });
    _setExploreCount('guides', res.length);
    if (!res.length) {
      container.innerHTML = '<p class="omni-none">No study guides match.</p>';
      return;
    }
    container.innerHTML = res.map(function (g) {
      // Use explicit href when present (e.g. study-guides/), fall back to topics/ path
      var href = g.href ? escHtml(_resolve('../../' + g.href)) : escHtml(TOPICS_ROOT + g.slug + '/');
      return '<a class="omni-lib-card" href="' + href + '">' +
        '<span class="omni-lib-card__title">' + escHtml(g.title) + '</span>' +
        (g.desc ? '<span class="omni-lib-card__snippet">' + escHtml(g.desc) + '</span>' : '') +
      '</a>';
    }).join('');
  }).catch(function () {
    container.innerHTML = '<p class="omni-none">Could not load study guides.</p>';
  });
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
