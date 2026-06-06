/* reader.js — Bible reader page: lookup, browse, keyboard nav, sidebar, compare */
'use strict';

import {
  getVersion, setVersion, loadBook, loadCrossRefs, loadCommentary, parseRef, parseMultiRef,
  normalizeBook, metaBooks, metaVersions, bookOrder, READER_URL, SEARCH_URL, MAPS_URL, escHtml,
  _compareCanonical, parseCrossRefEntry, resolveVerses,
  ATTRIBUTION, COMMENTARY_SOURCES, getCommentarySource, setCommentarySource,
  onVersionChange, _resolve, BOOKMARKS_URL,
  LIB_INDEX_URL, LIB_DOCS_BASE, LIB_ABBREV_MAP, libDocCache, libIndexCache,
  BOOK_MAP_LINKS, MAP_LABELS
} from './core.js';
import { autoTagTerms } from './terms.js';
import {
  getNotes, getNote, saveNote, toggleHighlight, _HL_COLORS,
  _historyPush, _historyGet, _recordReadingDay, getNotesForVerse, getNotesForChapter,
  createNoteV2, deleteNoteV2, updateNoteV2, _noteRelTime
} from './storage.js';
import {
  wireRefLinks, wireRefEl, applyHighlights, applyBookmarks, autoTagRefs,
  autoTagBareRefs, autoTagBareChapters
} from './wire.js';
import { getParallelsEnabled, injectAllParallelPanels, applyParallelPagination } from './parallels.js';
import {
  getInterlinearEnabled, injectAllInterlinearRows
} from './interlinear.js';

export { initViewToggle, initSplitToggle, initFontSizeControls, initWideToggle, initSidebarToggle } from './interlinear.js';

// ── Xref footnote-numbers toggle ──────────────────────────────────────────
var XREF_NOTES_KEY = 'bsw_xref_notes';

export function isXrefNotesEnabled()    { return !!localStorage.getItem(XREF_NOTES_KEY); }
// INTENT: Persist the cross-reference footnote-number toggle so the user's preference
//   survives page reload — presence of the key means on, absence means off.
// CHANGE? XREF_NOTES_KEY is read back by isXrefNotesEnabled and by initXrefNotesToggle
//   on load (line ~47). If the key name changes, update both; also update the VERIFY below.
// VERIFY: Enable † Footnotes in the reader; reload — the button should still appear active
//   and verse footnote numbers should be visible in the text.
export function setXrefNotesEnabled(on) {
  try {
    if (on) localStorage.setItem(XREF_NOTES_KEY, '1');
    else    localStorage.removeItem(XREF_NOTES_KEY);
  } catch (e) {}
  document.body.classList.toggle('bsw-xref-notes-on', !!on);
}

export function initXrefNotesToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-xref-notes-btn')) return;

  // Apply persisted state on load (absent key = default off)
  setXrefNotesEnabled(isXrefNotesEnabled());

  var on  = isXrefNotesEnabled();
  var btn = document.createElement('button');
  btn.id        = 'reader-xref-notes-btn';
  btn.className = 'reader-xref-notes-btn' + (on ? ' reader-xref-notes-btn--on' : '');
  btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  btn.title     = 'Show cross-reference footnote numbers inline';
  btn.textContent = '† Footnotes';

  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);

  btn.addEventListener('click', function () {
    on = !on;
    setXrefNotesEnabled(on);
    btn.classList.toggle('reader-xref-notes-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  });
}

// ── Compare state ─────────────────────────────────────────────────────────
var COMPARE_KEY = 'bsw_compare';
export function isCompareEnabled()    { return !!localStorage.getItem(COMPARE_KEY); }
export function getCompareVersion()   { return localStorage.getItem(COMPARE_KEY) || ''; }
// INTENT: Persist the compare-mode version selection so the reader reopens in the
//   same side-by-side state; empty string means compare is off.
// CHANGE? COMPARE_KEY is read by isCompareEnabled and getCompareVersion on every doLookup.
//   Removing this key (e.g. user clears storage) silently disables compare mode — acceptable.
// VERIFY: Enable ⇅ Compare, choose a version, reload the reader — compare should still be
//   active with the same version selected, and two columns should render.
export function setCompareVersion(id) { try { localStorage.setItem(COMPARE_KEY, id || ''); } catch (e) {} }

export function initCompareToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-compare-btn')) return;
  var btn = document.createElement('button');
  btn.id        = 'reader-compare-btn';
  btn.className = 'reader-compare-btn' + (isCompareEnabled() ? ' reader-compare-btn--on' : '');
  btn.setAttribute('aria-pressed', isCompareEnabled() ? 'true' : 'false');
  btn.title     = 'Compare translations side by side';
  btn.textContent = '⇅ Compare';
  var parallelsBtn = document.getElementById('reader-parallels-btn');
  var hint         = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, parallelsBtn || hint || null);
  btn.addEventListener('click', function () {
    var on = !isCompareEnabled();
    if (on) {
      var primary = getVersion();
      var def     = null;
      if (metaVersions) {
        for (var i = 0; i < metaVersions.length; i++) {
          var mv = metaVersions[i];
          if (!mv.stub && mv.id !== primary) { def = mv.id; break; }
        }
      }
      setCompareVersion(def || 'KJV');
    } else {
      setCompareVersion('');
    }
    btn.classList.toggle('reader-compare-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    if (window._readerLookupFn) window._readerLookupFn();
  });
}

// INTENT: Build a per-verse CSS grid inside each result group, injecting the
//   compare layout into the existing DOM rather than replacing it. Primary cells
//   are filled immediately; secondary (cmpVer) cells start as loading placeholders
//   and are filled when resolveVerses resolves. Because primary text stays in place,
//   _deactivateCompare must remove only the compare grid, not the whole group.
// VERIFY: Toggle compare on/off; primary text should not flash or re-fetch.
//   The Network tab should show only one fetch per cmpVer×book combination.
export function injectComparePanel(groups, cmpVer, resultsEl) {
  var primaryVer = getVersion();
  var domGroups  = resultsEl.querySelectorAll('.reader-result-group');

  domGroups.forEach(function (groupEl, gIdx) {
    var g = groups[gIdx];
    if (!g || !g.verses || !g.verses.length) return;
    var textEl = groupEl.querySelector('.reader-result-group__text');
    var attrEl = groupEl.querySelector('.reader-result-group__attr');

    // Build the per-verse grid: two sticky column headers, then pairs of cells
    var grid = document.createElement('div');
    grid.className = 'reader-compare-grid';

    var hdrA = _buildComparePanelHdr(primaryVer, 'primary');
    hdrA.className = 'reader-compare-col-hdr reader-compare-col-hdr--a';
    var hdrB = _buildComparePanelHdr(cmpVer, 'secondary');
    hdrB.className = 'reader-compare-col-hdr reader-compare-col-hdr--b';
    grid.appendChild(hdrA);
    grid.appendChild(hdrB);

    // Primary cells filled immediately; secondary cells show a loading indicator
    g.verses.forEach(function (vObj) {
      var key = String(vObj.chapter) + ':' + String(vObj.verse);

      var cellA = document.createElement('div');
      cellA.className = 'reader-compare-cell reader-compare-cell--a';
      cellA.dataset.verse = key;
      cellA.setAttribute('data-book', g.ref.bookName);
      var supA = document.createElement('sup');
      supA.className = 'reader-verse__num reader-compare-vnum';
      supA.textContent = String(vObj.verse);
      cellA.appendChild(supA);
      cellA.appendChild(document.createTextNode(vObj.text));

      var cellB = document.createElement('div');
      cellB.className = 'reader-compare-cell reader-compare-cell--b reader-compare-cell--loading';
      cellB.dataset.verse = key;
      cellB.innerHTML = '<span class="reader-compare-loading">…</span>';

      grid.appendChild(cellA);
      grid.appendChild(cellB);
    });

    // Wire verse-number popups on primary cells (secondary fills asynchronously)
    wireVerseNumberPopup(grid);

    // Insert grid before bottom nav (or append), then remove the old flowing text block
    var bottomNav = groupEl.querySelector('.reader-chapter-nav--bottom');
    if (bottomNav) groupEl.insertBefore(grid, bottomNav);
    else groupEl.appendChild(grid);
    if (textEl && textEl.parentNode) textEl.parentNode.removeChild(textEl);
    if (attrEl && attrEl.parentNode) attrEl.parentNode.removeChild(attrEl);

    // Fill secondary cells once the comparison version loads
    resolveVerses(g.ref, cmpVer).then(function (verses) {
      var byVerse = {};
      if (verses && verses.length) {
        verses.forEach(function (v) { byVerse[v.chapter + ':' + v.verse] = v.text; });
      }
      grid.querySelectorAll('.reader-compare-cell--b').forEach(function (cell) {
        var key2 = cell.dataset.verse;
        var text = byVerse[key2];
        var vNum = key2.split(':')[1];
        cell.classList.remove('reader-compare-cell--loading');
        cell.innerHTML = '';
        if (text) {
          cell.setAttribute('data-book', g.ref.bookName);
          var supB = document.createElement('sup');
          supB.className = 'reader-verse__num reader-compare-vnum';
          supB.textContent = vNum;
          cell.appendChild(supB);
          cell.appendChild(document.createTextNode(text));
        } else {
          var unavail = document.createElement('span');
          unavail.className = 'reader-compare-unavail';
          unavail.textContent = '—';
          cell.appendChild(unavail);
        }
      });
      applyHighlights(grid);
      wireVerseNumberPopup(grid);
      var attr = ATTRIBUTION[cmpVer];
      if (attr) {
        var attrEl2 = document.createElement('p');
        attrEl2.className = 'reader-result-group__attr';
        attrEl2.textContent = attr;
        grid.after(attrEl2);
      }
    }).catch(function () {
      grid.querySelectorAll('.reader-compare-cell--b').forEach(function (cell) {
        cell.classList.remove('reader-compare-cell--loading');
        cell.innerHTML = '<span class="reader-compare-unavail">—</span>';
      });
    });
  });
}

function _buildComparePanelHdr(versionId, role) {
  var hdr = document.createElement('div');
  hdr.className = 'reader-compare-panel__hdr';
  var lbl = document.createElement('span');
  lbl.className  = 'reader-compare-panel__label';
  lbl.textContent = role === 'primary' ? 'A:' : 'B:';
  var sel = document.createElement('select');
  sel.className = 'reader-compare-ver-sel';
  sel.setAttribute('aria-label', role === 'primary' ? 'Primary version' : 'Comparison version');
  if (metaVersions) {
    metaVersions.forEach(function (mv) {
      if (mv.group === 'apocrypha') return;
      if (mv.stub) return;
      var opt = document.createElement('option');
      opt.value = mv.id; opt.textContent = mv.id; opt.title = mv.name;
      if (mv.id === versionId) opt.selected = true;
      sel.appendChild(opt);
    });
  }
  sel.addEventListener('change', function () {
    if (role === 'primary') { setVersion(sel.value); }
    else { setCompareVersion(sel.value); if (window._readerLookupFn) window._readerLookupFn(); }
  });
  hdr.appendChild(lbl); hdr.appendChild(sel);
  return hdr;
}

// ── Reader nav state ──────────────────────────────────────────────────────
window._readerNavState  = null;
window._readerGroups    = [];
// CHANGE? window._readerLookupFn is assigned to doLookup inside initReaderLookup() and
//   called by: _navigateChapter (prev/next chapter), initCompareToggle (compare on/off),
//   onVersionChange callback, and the keyboard nav handler. Removing or renaming the
//   assignment breaks all in-page navigation without any JS error — it just silently noops.
window._readerLookupFn  = null;

// ── Chapter read tracking ─────────────────────────────────────────────────
// INTENT: Module-level constant so the key is visible in search and easy to update.
// CHANGE? progress/index.html reads this same key to render the chapter progress grid.
//   If this key is renamed, update progress/index.html:getChapterRead() too.
// VERIFY: Mark a chapter as read in the reader; inspect localStorage — bsw_chapter_read
//   should contain an object keyed by "{bookId}.{ch}" with { read: true, date: "YYYY-MM-DD" }.
var READ_KEY = 'bsw_chapter_read';

// ── Stripped mode — no side panel (used when navigating from Reading Progress) ──
var _strippedMode = !!new URLSearchParams(location.search).get('stripped');

// ── initReaderPage ────────────────────────────────────────────────────────
export function initReaderPage() {
  initReaderLookup();
  initReaderBrowse();
  initReaderKeyboard();
  if (_strippedMode) {
    var panel = document.getElementById('reader-xref-panel');
    if (panel) panel.hidden = true;
  } else {
    _ensureReaderPanelStructure();
  }

  onVersionChange(function () {
    if (window._readerLookupFn) window._readerLookupFn();
  });
}

// ── initReaderLookup ──────────────────────────────────────────────────────
export function initReaderLookup() {
  var input    = document.getElementById('reader-lookup-input');
  var btn      = document.getElementById('reader-lookup-btn');
  var statusEl = document.getElementById('reader-lookup-status');
  if (!input) return;

  function setStatus(msg) { if (statusEl) statusEl.textContent = msg; }

  // INTENT: Single entry point for all in-page navigation. Parses the input,
  //   fetches verses, updates history.replaceState, writes bsw_history, and
  //   re-renders all right-panel tabs. Any navigation that bypasses doLookup
  //   leaves URL state, bsw_history, and the right panel out of sync.
  // CHANGE? If you add a new right-panel section, add it to the panel refresh
  //   sequence inside doLookup (after _loadReaderXrefs / _loadReaderNotes calls).
  // VERIFY: Navigate to Romans 8; URL should update to ?ref=Romans+8, history
  //   dropdown should prepend the entry, and all three panel tabs should refresh.
  function doLookup() {
    var q         = input.value.trim();
    var resultsEl = document.getElementById('reader-results');
    if (!q) { if (resultsEl) resultsEl.innerHTML = ''; return; }

    var refs = parseMultiRef(q, null);

    // Bare book name → whole book as a single ref; chapter breaks are injected at render time.
    if (!refs.length) {
      var _bid = normalizeBook(q);
      var _bkm = _bid && metaBooks && metaBooks.find(function (b) { return b.id === _bid; });
      if (_bkm) {
        refs.push({ bookId: _bkm.id, bookName: _bkm.name, ch: 1, v: 1,
          endCh: (_bkm.chapters || 1), endV: 9999,
          display: _bkm.name, wholeChapter: true, wholeBook: true });
        input.value = _bkm.name;
        q = _bkm.name;
      }
    }

    if (!refs.length) {
      setStatus('Could not parse — try: Gen 1, John 3:16-21');
      return;
    }
    setStatus('');

    var url = new URL(window.location.href);
    url.searchParams.set('ref', q);
    history.replaceState(null, '', url.toString());

    // Chapter-0 intercept → book introduction page
    if (refs.length === 1 && refs[0].bookId && refs[0].ch === 0) {
      _renderReaderBookIntro(refs[0].bookId, refs[0].bookName);
      return;
    }

    if (resultsEl) resultsEl.innerHTML = '<p class="reader-hint">Loading…</p>';

    var ver = getVersion();

    window._readerGroups = [];
    Promise.all(refs.map(function (ref) {
      return resolveVerses(ref, ver).then(function (verses) {
        return { ref: ref, verses: verses };
      }).catch(function () { return { ref: ref, verses: null }; });
    })).then(function (groups) {
      if (!resultsEl) return;
      resultsEl.innerHTML = '';
      var any = false;

      groups.forEach(function (g, idx) {
        if (!g.verses || !g.verses.length) return;
        any = true;
        window._readerGroups.push(g);

        var groupEl = document.createElement('div');
        groupEl.className = 'reader-result-group';

        // Whole-book view: skip per-chapter nav buttons (chapter breaks act as structure).
        if (g.ref.bookId && !g.ref.wholeBook) groupEl.appendChild(_buildNavButtons(g.ref, 'top'));

        var title = document.createElement('h2');
        title.className   = 'reader-result-group__title';
        title.textContent = g.ref.display;
        groupEl.appendChild(title);

        // Use a <div> container for whole-book so chapter-break <div>s are valid children.
        var textEl = document.createElement(g.ref.wholeBook ? 'div' : 'p');
        textEl.className = 'reader-result-group__text';
        var _prevCh = null;
        g.verses.forEach(function (vObj) {
          // Insert a chapter-break divider whenever the chapter number advances.
          if (g.ref.wholeBook && vObj.chapter !== _prevCh && _prevCh !== null) {
            var brk = document.createElement('div');
            brk.className = 'reader-chapter-break';
            brk.innerHTML = '<span class="reader-chapter-break__label">' +
              escHtml(g.ref.bookName + ' ' + vObj.chapter) + '</span>';
            textEl.appendChild(brk);
          }
          _prevCh = vObj.chapter;
          var span = document.createElement('span');
          span.className = 'reader-verse';
          span.setAttribute('data-book', g.ref.bookName);
          span.setAttribute('data-ch',   String(vObj.chapter));
          span.setAttribute('data-v',    String(vObj.verse));
          var sup = document.createElement('sup');
          sup.className   = 'reader-verse__num';
          sup.textContent = String(vObj.verse);
          span.appendChild(sup);
          span.appendChild(document.createTextNode(vObj.text + ' '));
          textEl.appendChild(span);
        });
        groupEl.appendChild(textEl);

        var attrEl = document.createElement('p');
        attrEl.className  = 'reader-result-group__attr';
        attrEl.textContent = ATTRIBUTION[ver] || '';
        attrEl.hidden = !!(g.ref.v && !g.ref.endV);
        groupEl.appendChild(attrEl);

        if (g.ref.bookId && !g.ref.wholeBook) groupEl.appendChild(_buildNavButtons(g.ref, 'bottom'));

        // D-D: Mark chapter as read button (whole chapter views only, not single verses)
        if (g.ref.bookId && g.ref.ch && !g.ref.v) {
          var markRow = document.createElement('div');
          markRow.className = 'reader-mark-row';
          var markKey = g.ref.bookId + '.' + g.ref.ch;
          var markBtn2 = document.createElement('button');
          markBtn2.className = 'reader-mark-btn';
          markBtn2.type = 'button';
          markBtn2.dataset.key = markKey;
          (function (btn, key) {
            function getRead() { try { return JSON.parse(localStorage.getItem(READ_KEY) || '{}'); } catch (e) { return {}; } }
            var alreadyRead = !!(getRead()[key] && getRead()[key].read);
            if (alreadyRead) {
              btn.textContent = '✓ Read';
              btn.classList.add('reader-mark-btn--done');
              btn.disabled = true;
            } else {
              btn.textContent = 'Mark chapter as read ✓';
              btn.addEventListener('click', function () {
                var data = getRead();
                data[key] = { read: true, date: new Date().toISOString().slice(0, 10) };
                localStorage.setItem(READ_KEY, JSON.stringify(data));
                btn.textContent = '✓ Read';
                btn.classList.add('reader-mark-btn--done');
                btn.disabled = true;
              });
            }
          }(markBtn2, markKey));
          markRow.appendChild(markBtn2);
          groupEl.appendChild(markRow);
        }

        resultsEl.appendChild(groupEl);

        if (idx === 0 && g.ref.bookId) {
          window._readerNavState = {
            bookId:   g.ref.bookId,
            bookName: g.ref.bookName,
            ch:       g.ref.ch
          };
          syncBrowseSelects(g.ref.bookId, g.ref.ch);
          // loadBook hits the cache (already fetched by resolveVerses above).
          var _navCh = g.ref.ch, _navBookId = g.ref.bookId;
          loadBook(ver, _navBookId).then(function (chapters) {
            if (chapters) renderReaderSidebar(_navBookId, chapters, _navCh);
          }).catch(function () {});
          // Populate the Notes/Commentary/Cross Refs side panel for this passage.
          if (!_strippedMode) loadReaderPanelContent(g.ref);
        }
      });

      if (!any) {
        resultsEl.innerHTML = '<p class="reader-hint">Verse not found in ' + escHtml(ver) + '.</p>';
        return;
      }

      applyHighlights(resultsEl);
      applyBookmarks(resultsEl);
      wireVerseNumberPopup(resultsEl);
      wireVerseTextHighlight(resultsEl);
      injectReaderFootnotes(resultsEl);

      if (isCompareEnabled()) injectComparePanel(window._readerGroups, getCompareVersion(), resultsEl);
      if (getInterlinearEnabled()) injectAllInterlinearRows(resultsEl);
      if (getParallelsEnabled()) { applyParallelPagination(resultsEl); injectAllParallelPanels(resultsEl); }

      _historyPush(q, ver);
      _recordReadingDay();
    }).catch(function (err) {
      if (resultsEl) resultsEl.innerHTML = '<p class="reader-hint">Could not load passage.</p>';
      console.error('[BibleUI] reader error:', err);
    });
  }

  // CHANGE? All in-page navigation calls window._readerLookupFn(); callers:
  //   _navigateChapter (prev/next chapter buttons + keyboard), initCompareToggle (⇅ button),
  //   onVersionChange callback, and initXrefNotesToggle (indirectly via reload).
  //   If doLookup is ever renamed or this assignment is removed, all in-page navigation
  //   silently becomes a no-op with no JS error.
  window._readerLookupFn = doLookup;
  if (btn) btn.addEventListener('click', doLookup);
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { e.preventDefault(); doLookup(); }
  });
  input.addEventListener('input', function () { setStatus(''); });

  // Pre-fill input from URL and trigger lookup
  var params = new URLSearchParams(window.location.search);
  var refStr = params.get('ref') || params.get('q') || '';
  if (refStr) {
    input.value = refStr;
    doLookup();
  } else {
    var resultsEl = document.getElementById('reader-results');
    var hist = _historyGet();
    var lastRef = hist[0];
    if (lastRef && !sessionStorage.getItem('bsw_reader_resume_dismissed') && resultsEl) {
      // RD-C: returning user — show dismissable resume banner
      var banner = document.createElement('div');
      banner.className = 'reader-resume-banner';
      banner.innerHTML =
        'Continue where you left off: ' +
        '<a class="reader-resume-link" href="?ref=' + encodeURIComponent(lastRef) + '">' + escHtml(lastRef) + '</a>' +
        '<button class="reader-resume-dismiss" aria-label="Dismiss">✕</button>';
      resultsEl.appendChild(banner);
      banner.querySelector('.reader-resume-dismiss').addEventListener('click', function () {
        banner.remove();
        sessionStorage.setItem('bsw_reader_resume_dismissed', '1');
      });
    } else if (!lastRef && resultsEl) {
      // RD-H: first-time visitor — show empty state with quick-start chips
      resultsEl.innerHTML =
        '<div class="reader-empty-state">' +
          '<p class="reader-hint">Enter a reference above — <em>John 3:16</em>, <em>Romans 8</em>, <em>Gen 1; John 1:1–14</em></p>' +
          '<div class="reader-quick-starts">' +
            '<a class="reader-qs-chip" href="?ref=John+1">John 1</a>' +
            '<a class="reader-qs-chip" href="?ref=Psalms+23">Psalm 23</a>' +
            '<a class="reader-qs-chip" href="?ref=Romans+8">Romans 8</a>' +
            '<a class="reader-qs-chip" href="?ref=Genesis+1">Genesis 1</a>' +
            '<a class="reader-qs-chip" href="?ref=Isaiah+53">Isaiah 53</a>' +
          '</div>' +
        '</div>';
    }
  }
}

function _buildNavButtons(parsedRef, pos) {
  var nav = document.createElement('div');
  nav.className = 'reader-chapter-nav reader-chapter-nav--' + pos;

  var prevBtn = document.createElement('button');
  prevBtn.className  = 'reader-nav-btn reader-nav-btn--prev';
  prevBtn.textContent = '← Previous';
  prevBtn.addEventListener('click', function () { _navigateChapter(parsedRef, -1); });

  var nextBtn = document.createElement('button');
  nextBtn.className  = 'reader-nav-btn reader-nav-btn--next';
  nextBtn.textContent = 'Next →';
  nextBtn.addEventListener('click', function () { _navigateChapter(parsedRef, 1); });

  nav.appendChild(prevBtn);
  nav.appendChild(nextBtn);
  return nav;
}

// INTENT: Prev/next chapter navigation must use _readerLookupFn (in-page) rather
//   than window.location.href (full reload). A full reload resets the right panel,
//   loses scroll position, and reverts all toggle states (interlinear, compare, etc.).
//   The ch=0 intro-page branch below is the canonical pattern for in-page nav.
// CHANGE? If the lookup input element ID ('reader-lookup-input') changes, update
//   both this function and the sidebar chapter-button wiring.
// VERIFY: Click next-chapter 3 times; the Network tab should show no full-page
//   navigation — only data fetches. Right panel content should remain visible.
function _navigateChapter(parsedRef, delta) {
  var bookIdx = bookOrder && bookOrder[parsedRef.bookId];
  if (bookIdx === undefined) return;
  var nextCh = parsedRef.ch + delta;

  // ch 1 → prev → intro page
  if (nextCh === 0) {
    var introInput = document.getElementById('reader-lookup-input');
    if (introInput) introInput.value = parsedRef.bookName + ' 0';
    if (window._readerLookupFn) { window._readerLookupFn(); return; }
  }

  loadBook(getVersion(), parsedRef.bookId).then(function (chapters) {
    var maxCh = chapters ? Object.keys(chapters).map(Number).reduce(function (a, b) { return a > b ? a : b; }, 0) : 999;
    var inp = document.getElementById('reader-lookup-input');
    var newRef;
    if (nextCh >= 1 && nextCh <= maxCh) {
      newRef = parsedRef.bookName + ' ' + nextCh;
    } else if (nextCh < 1 && bookIdx > 0) {
      var prevBook = metaBooks && metaBooks[bookIdx - 1];
      if (prevBook) newRef = prevBook.name + ' 1';
    } else if (nextCh > maxCh) {
      var nextBook = metaBooks && metaBooks[bookIdx + 1];
      if (nextBook) newRef = nextBook.name + ' 1';
    }
    if (newRef && inp) {
      inp.value = newRef;
      if (window._readerLookupFn) window._readerLookupFn();
    }
  }).catch(function () {});
}

// ── initReaderBrowse ──────────────────────────────────────────────────────
export function initReaderBrowse() {
  var bookSel = document.getElementById('reader-book-select');
  var chSel   = document.getElementById('reader-ch-select');
  var verSel  = document.getElementById('reader-ver-select');
  if (!bookSel || !chSel || !metaBooks) return;

  // ── Translation picker ─────────────────────────────────────────────────────
  if (verSel && metaVersions) {
    var curVer = getVersion();
    var tierLabels = { 1: 'Common', 2: 'Literal', 3: 'Other' };
    var groups = {};
    metaVersions.forEach(function (v) {
      if (v.group === 'apocrypha') return;  // apocrypha-only versions live in the separate reader
      if (v.stub) return;                   // no data files yet
      var t = v.tier || 3;
      if (!groups[t]) groups[t] = [];
      groups[t].push(v);
    });
    Object.keys(groups).sort().forEach(function (t) {
      var grp = document.createElement('optgroup');
      grp.label = tierLabels[t] || 'Other';
      groups[t].forEach(function (v) {
        var opt = document.createElement('option');
        opt.value       = v.id;
        opt.textContent = v.id + ' — ' + v.name;
        if (v.id === curVer) opt.selected = true;
        grp.appendChild(opt);
      });
      verSel.appendChild(grp);
    });

    verSel.addEventListener('change', function () {
      setVersion(verSel.value);
      // onVersionChange callback in initReaderPage re-renders automatically
    });

    // Keep in sync if version changes from the global sidebar picker
    onVersionChange(function (newId) {
      if (verSel.value !== newId) verSel.value = newId;
    });
  }

  // Bible books optgroup
  var bibleGroup = document.createElement('optgroup');
  bibleGroup.label = 'Bible';
  metaBooks.forEach(function (b) {
    var opt = document.createElement('option');
    opt.value       = b.id;
    opt.textContent = b.name;
    bibleGroup.appendChild(opt);
  });
  bookSel.appendChild(bibleGroup);

  // Library optgroup — loaded async
  fetch(LIB_INDEX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (docs) {
      libIndexCache = docs;
      var libGroup = document.createElement('optgroup');
      libGroup.label = 'Library';
      docs.forEach(function (d) {
        var opt = document.createElement('option');
        opt.value       = 'lib:' + d.abbrev.toLowerCase();
        opt.textContent = d.abbrev + ' — ' + d.title;
        libGroup.appendChild(opt);
      });
      bookSel.appendChild(libGroup);
    })
    .catch(function () {});

  bookSel.addEventListener('change', function () {
    var val = bookSel.value;

    if (val && val.indexOf('lib:') === 0) {
      var abbrevKey = val.slice(4);
      var docId     = LIB_ABBREV_MAP[abbrevKey];
      if (!docId) return;
      var fillSections = function (doc) {
        chSel._libDocId = docId;
        chSel._bookId   = null;
        chSel.innerHTML = '<option value="">§…</option>';
        for (var i = 1; i <= doc.totalSections; i++) {
          var o = document.createElement('option');
          o.value = String(i); o.textContent = i;
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

    var bk = metaBooks.find(function (b) { return b.id === val; });
    if (!bk) {
      chSel.innerHTML = '<option value="">Ch…</option>';
      chSel.disabled  = true;
      chSel._bookId   = null;
      chSel._libDocId = null;
      return;
    }
    chSel._bookId   = bk.id;
    chSel._libDocId = null;
    chSel.innerHTML = '<option value="">Ch…</option>';
    var introOpt = document.createElement('option');
    introOpt.value = '0'; introOpt.textContent = 'Intro';
    chSel.appendChild(introOpt);
    for (var i = 1; i <= (bk.chapters || 150); i++) {
      var opt = document.createElement('option');
      opt.value = String(i); opt.textContent = i;
      chSel.appendChild(opt);
    }
    chSel.disabled = false;
  });

  chSel.addEventListener('change', function () {
    if (!bookSel.value || !chSel.value) return;
    var val = bookSel.value;
    var lookupInput = document.getElementById('reader-lookup-input');

    if (val.indexOf('lib:') === 0) {
      var ref2 = val.slice(4).toUpperCase() + ' ' + chSel.value;
      if (lookupInput) lookupInput.value = ref2;
      if (window._readerLookupFn) window._readerLookupFn();
      return;
    }

    var bk = metaBooks.find(function (b) { return b.id === val; });
    if (!bk) return;
    var ref = bk.name + ' ' + chSel.value;
    if (lookupInput) lookupInput.value = ref;
    if (window._readerLookupFn) window._readerLookupFn();
  });
}

export function syncBrowseSelects(bookId, ch) {
  var bookSel    = document.getElementById('reader-book-select');
  var chapterSel = document.getElementById('reader-ch-select');
  if (bookSel) bookSel.value = bookId;
  if (chapterSel) chapterSel.value = String(ch);
}

// ── initReaderKeyboard ────────────────────────────────────────────────────
export function initReaderKeyboard() {
  document.addEventListener('keydown', function (e) {
    var tag = document.activeElement && document.activeElement.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;

    var state = window._readerNavState;
    if (!state) return;

    var parsedRef = {
      bookId:   state.bookId,
      bookName: state.bookName,
      ch:       state.ch,
      v:        1, endCh: state.ch, endV: 9999, display: state.bookName + ' ' + state.ch
    };

    if (e.key === 'ArrowRight' || e.key === 'j') {
      e.preventDefault();
      _navigateChapter(parsedRef, 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'k') {
      e.preventDefault();
      _navigateChapter(parsedRef, -1);
    }
  });
}

// ── injectReaderFootnotes ─────────────────────────────────────────────────
export function injectReaderFootnotes(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-verse[data-book][data-ch][data-v]').forEach(function (verseEl) {
    var bookName = verseEl.getAttribute('data-book');
    var ch       = parseInt(verseEl.getAttribute('data-ch'), 10);
    var v        = parseInt(verseEl.getAttribute('data-v'), 10);
    var bk = metaBooks && metaBooks.find(function (b) { return b.name === bookName || b.id === bookName; });
    if (!bk) return;

    loadCrossRefs(bk.id).then(function (data) {
      if (!data) return;
      var chData = data[String(ch)];
      if (!chData) return;
      var rawRefs = chData[String(v)];
      if (!rawRefs || !rawRefs.length) return;
      var entries = rawRefs.map(parseCrossRefEntry);
      entries.sort(function (a, b) { return b.votes - a.votes; });
      entries = entries.slice(0, 5);
      entries.sort(_compareCanonical);
      entries.forEach(function (entry, i) {
        var p = parseRef(entry.ref);
        if (!p) return;
        var sup = document.createElement('sup');
        sup.className = 'reader-xref-note';
        sup.setAttribute('data-ref', entry.ref);
        sup.setAttribute('tabindex', '0');
        sup.setAttribute('role', 'button');
        sup.textContent = String(i + 1);
        wireRefEl(sup, p);
        verseEl.appendChild(sup);
      });
    }).catch(function () {});
  });
}

// ── wireVerseNumberPopup ──────────────────────────────────────────────────
var _activeVerseEl = null;

export function wireVerseNumberPopup(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-verse__num').forEach(function (numEl) {
    if (numEl._versePopupWired) return;
    numEl._versePopupWired = true;
    numEl.addEventListener('click', function (e) {
      e.preventDefault();
      // Standard verse span or compare grid cell
      var verseEl  = numEl.closest('.reader-verse') || numEl.closest('.reader-compare-cell');
      if (!verseEl) return;
      // RD-E: highlight active verse
      if (_activeVerseEl) _activeVerseEl.classList.remove('reader-verse--active');
      verseEl.classList.add('reader-verse--active');
      _activeVerseEl = verseEl;
      // Remove highlight when modal closes
      var bd = document.querySelector('.bsw-modal-backdrop');
      if (bd && !bd._readerVerseObserver) {
        bd._readerVerseObserver = new MutationObserver(function () {
          if (bd.classList.contains('bsw-modal-backdrop--hidden') && _activeVerseEl) {
            _activeVerseEl.classList.remove('reader-verse--active');
            _activeVerseEl = null;
          }
        });
        bd._readerVerseObserver.observe(bd, { attributes: true, attributeFilter: ['class'] });
      }
      var bookName, ch, v;
      if (verseEl.classList.contains('reader-compare-cell')) {
        bookName = verseEl.getAttribute('data-book');
        var parts = (verseEl.getAttribute('data-verse') || '').split(':');
        ch = parts[0];
        v  = parts[1];
      } else {
        bookName = verseEl.getAttribute('data-book');
        ch       = verseEl.getAttribute('data-ch');
        v        = verseEl.getAttribute('data-v');
      }
      if (!bookName || !ch || !v) return;
      var ref = bookName + ' ' + ch + ':' + v;
      var parsed = parseRef(ref);
      if (parsed) {
        import('./modal.js').then(function (m) { m.openModal(parsed); });
      }
    });
    numEl.style.cursor = 'pointer';
  });
}

// ── Quick verse highlight picker ──────────────────────────────────────────
// Solid swatch colours for the picker buttons (opaque, easy to distinguish).
var _HL_SWATCHES = {
  yellow: '#f5d000', orange: '#f07820', pink:     '#d84080',
  red:    '#cc3030', purple: '#8030b8', lavender: '#9080cc',
  green:  '#30a850', teal:   '#20a898', blue:     '#2878e0', mint: '#38c8b0'
};
var _hlPicker        = null;
var _hlPickerVerseEl = null;
var _hlPickerRef     = null;

function _getHlPicker() {
  if (_hlPicker) return _hlPicker;
  _hlPicker = document.createElement('div');
  _hlPicker.className = 'reader-hl-picker';
  _hlPicker.setAttribute('role', 'toolbar');
  _hlPicker.setAttribute('aria-label', 'Highlight colour');
  _hlPicker.hidden = true;

  _HL_COLORS.forEach(function (color) {
    var btn = document.createElement('button');
    btn.className = 'reader-hl-swatch';
    btn.type = 'button';
    btn.setAttribute('data-hl-color', color);
    btn.title = color.charAt(0).toUpperCase() + color.slice(1);
    btn.style.background = _HL_SWATCHES[color] || color;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      if (_hlPickerRef && _hlPickerVerseEl) {
        var newHl = toggleHighlight(_hlPickerRef, color);
        _applyHlToVerseEl(_hlPickerVerseEl, newHl);
      }
      _hideHlPicker();
    });
    _hlPicker.appendChild(btn);
  });

  var clearBtn = document.createElement('button');
  clearBtn.className = 'reader-hl-swatch reader-hl-swatch--clear';
  clearBtn.type = 'button';
  clearBtn.title = 'Remove highlight';
  clearBtn.textContent = '×';
  clearBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    if (_hlPickerRef && _hlPickerVerseEl) {
      var n = getNote(_hlPickerRef) || {};
      n.highlight = false;
      saveNote(_hlPickerRef, n);
      _applyHlToVerseEl(_hlPickerVerseEl, false);
    }
    _hideHlPicker();
  });
  _hlPicker.appendChild(clearBtn);

  document.body.appendChild(_hlPicker);

  document.addEventListener('click', function (e) {
    if (_hlPicker && !_hlPicker.hidden && !_hlPicker.contains(e.target)) _hideHlPicker();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && _hlPicker && !_hlPicker.hidden) _hideHlPicker();
  });

  return _hlPicker;
}

function _showHlPicker(verseEl, ref, clientX, clientY) {
  var picker = _getHlPicker();
  _hlPickerVerseEl = verseEl;
  _hlPickerRef     = ref;

  var note = getNote(ref);
  var activeColor = note && note.highlight;
  picker.querySelectorAll('[data-hl-color]').forEach(function (btn) {
    btn.classList.toggle('reader-hl-swatch--active', btn.getAttribute('data-hl-color') === activeColor);
  });

  picker.hidden = false;
  // Position: show below click, clamp to viewport
  var pw = picker.offsetWidth  || 280;
  var ph = picker.offsetHeight || 36;
  var vw = window.innerWidth,  vh = window.innerHeight;
  var px = Math.max(4, Math.min(clientX - pw / 2, vw - pw - 4));
  var py = clientY + 12;
  if (py + ph > vh) py = clientY - ph - 8;
  picker.style.left = px + 'px';
  picker.style.top  = py + 'px';
}

function _hideHlPicker() {
  if (_hlPicker) _hlPicker.hidden = true;
  _hlPickerVerseEl = null;
  _hlPickerRef     = null;
}

function _applyHlToVerseEl(verseEl, hl) {
  verseEl.className = verseEl.className.replace(/\breader-verse--hl-\S+/g, '').trim();
  if (hl && hl !== false) verseEl.classList.add('reader-verse--hl-' + hl);
}

export function wireVerseTextHighlight(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-verse').forEach(function (verseEl) {
    if (verseEl._hlWired) return;
    verseEl._hlWired = true;
    verseEl.addEventListener('click', function (e) {
      if (e.target.closest('.reader-verse__num') ||
          e.target.closest('a') ||
          e.target.closest('[role="button"]')) return;
      var bookName = verseEl.getAttribute('data-book');
      var ch       = verseEl.getAttribute('data-ch');
      var v        = verseEl.getAttribute('data-v');
      if (!bookName || !ch || !v) return;
      e.stopPropagation();
      _showHlPicker(verseEl, bookName + ' ' + ch + ':' + v, e.clientX, e.clientY);
    });
  });
}

// ── Reader side panel ─────────────────────────────────────────────────────
var _readerPanelActiveTab = 'notes';
var _readerPanelParsed    = null;

export function _ensureReaderPanelStructure() {
  // The xref panel is the right-hand aside — it holds Notes/Commentary/Cross Refs tabs.
  var panel = document.getElementById('reader-xref-panel');
  if (!panel) return null;
  if (panel.querySelector('.reader-panel-tabs')) return panel;

  panel.innerHTML =
    '<div class="reader-panel-tabs">' +
      '<button class="reader-panel-tab reader-panel-tab--active" data-panel-tab="notes">Notes</button>' +
      '<button class="reader-panel-tab" data-panel-tab="commentary">Commentary</button>' +
      '<button class="reader-panel-tab" data-panel-tab="xrefs">Cross Refs</button>' +
      '<button class="reader-panel-tab" data-panel-tab="bookmarks">Bookmarks</button>' +
    '</div>' +
    '<div class="reader-panel-body" id="reader-panel-notes"></div>' +
    '<div class="reader-panel-body" id="reader-panel-commentary" hidden></div>' +
    '<div class="reader-panel-body" id="reader-panel-xrefs" hidden></div>' +
    '<div class="reader-panel-body" id="reader-panel-bookmarks" hidden></div>';

  panel.querySelectorAll('.reader-panel-tab').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var tab = btn.getAttribute('data-panel-tab');
      _activateReaderPanelTab(tab);
    });
  });

  return panel;
}

export function _activateReaderPanelTab(tab) {
  _readerPanelActiveTab = tab;
  var panel = document.getElementById('reader-xref-panel');
  if (!panel) return;
  panel.querySelectorAll('.reader-panel-tab').forEach(function (btn) {
    btn.classList.toggle('reader-panel-tab--active', btn.getAttribute('data-panel-tab') === tab);
  });
  panel.querySelectorAll('.reader-panel-body').forEach(function (body) {
    body.hidden = (body.id !== 'reader-panel-' + tab);
  });
  // Lazy-load content when a tab is first opened for the current passage.
  if (_readerPanelParsed) _loadPanelTab(tab, _readerPanelParsed);
}

// ── Panel content loading ─────────────────────────────────────────────────

export function loadReaderPanelContent(parsed) {
  _readerPanelParsed = parsed;
  // Re-activate comm mode for the new passage if it was on before chapter navigation.
  var commBtn = document.getElementById('reader-comm-toggle');
  if (commBtn && commBtn.getAttribute('aria-pressed') === 'true') {
    _activateCommMode();
  }
  var commEl = document.getElementById('reader-panel-commentary');
  var xrefEl = document.getElementById('reader-panel-xrefs');
  // Clear lazy-load flags so the new passage is fetched when each tab is opened.
  if (commEl)  { commEl._commLoaded  = false; commEl.innerHTML  = ''; }
  if (xrefEl)  { xrefEl._xrefsLoaded = false; xrefEl.innerHTML = ''; }
  // Notes are always reloaded immediately (user may have added/deleted notes).
  var notesEl = document.getElementById('reader-panel-notes');
  if (notesEl) _loadReaderNotes(parsed, notesEl);
  // Pre-load whichever tab is already active.
  if (_readerPanelActiveTab === 'commentary' && commEl) _loadReaderCommentary(parsed, commEl);
  if (_readerPanelActiveTab === 'xrefs'      && xrefEl) _loadReaderXrefs(parsed, xrefEl);
  if (_readerPanelActiveTab === 'bookmarks') {
    var bmEl = document.getElementById('reader-panel-bookmarks');
    if (bmEl) _loadReaderBookmarks(bmEl);
  }
}

function _loadPanelTab(tab, parsed) {
  if (tab === 'notes') {
    var notesEl = document.getElementById('reader-panel-notes');
    if (notesEl) _loadReaderNotes(parsed, notesEl);
  } else if (tab === 'commentary') {
    var commEl = document.getElementById('reader-panel-commentary');
    if (commEl && !commEl._commLoaded) _loadReaderCommentary(parsed, commEl);
  } else if (tab === 'xrefs') {
    var xrefEl = document.getElementById('reader-panel-xrefs');
    if (xrefEl && !xrefEl._xrefsLoaded) _loadReaderXrefs(parsed, xrefEl);
  } else if (tab === 'bookmarks') {
    var bmEl = document.getElementById('reader-panel-bookmarks');
    if (bmEl) _loadReaderBookmarks(bmEl);
  }
}

function _loadReaderBookmarks(container) {
  var KEY = 'bsw_bookmarks';
  var bms;
  try { bms = JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { bms = []; }

  if (!bms.length) {
    container.innerHTML =
      '<p class="reader-hint" style="padding:.75rem">No bookmarks yet. Click a verse number and choose "Bookmark" to save a reference.</p>';
  } else {
    var ul = document.createElement('ul');
    ul.className = 'reader-bookmark-list';
    bms.forEach(function (ref) {
      var li  = document.createElement('li');
      li.className = 'reader-bookmark-item';
      var star = document.createElement('span');
      star.className = 'reader-bookmark-star';
      star.textContent = '★';
      var a = document.createElement('a');
      a.className = 'reader-bookmark-ref';
      a.href = '#';
      a.textContent = ref;
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var input = document.getElementById('reader-lookup-input');
        if (input) input.value = ref;
        if (window._readerLookupFn) window._readerLookupFn();
      });
      li.appendChild(star);
      li.appendChild(a);
      ul.appendChild(li);
    });
    container.innerHTML = '';
    container.appendChild(ul);
  }
  // INTENT: BOOKMARKS_URL is exported from core.js but never surfaced in any UI — this is its
  //   intended hook. Without this link the standalone bookmarks page is unreachable from the UI.
  // CHANGE? If BOOKMARKS_URL path changes in core.js the link href updates automatically.
  // VERIFY: Open reader → Bookmarks tab. "View all bookmarks ↗" link should appear at the bottom.
  //   Clicking it navigates to bookmarks/index.html with the full bookmark list.
  var viewAll = document.createElement('a');
  viewAll.className = 'reader-bm-viewall';
  viewAll.href = BOOKMARKS_URL;
  viewAll.textContent = 'View all bookmarks ↗';
  container.appendChild(viewAll);
}

function _loadReaderNotes(parsed, container) {
  var notes = getNotesForChapter(parsed.bookId, parsed.ch);
  var bk    = metaBooks && metaBooks.find(function (b) { return b.id === parsed.bookId; });
  var chLabel = (bk ? bk.name : parsed.bookId) + ' ' + parsed.ch;

  var html = '';
  if (notes.length) {
    html += '<div class="reader-notes-group">';
    html += '<div class="reader-notes-group__heading">' + escHtml(chLabel) + '</div>';
    notes.forEach(function (note) {
      html += '<div class="reader-notes-item" data-note-id="' + escHtml(note.id) + '">' +
        '<div class="reader-notes-item__text">' + escHtml(note.text) + '</div>' +
        '<div class="reader-notes-item__meta">' + escHtml(note.display) + ' · ' + _noteRelTime(note.created) +
          ' <button class="bsw-note-action-btn bsw-note-action-btn--del" style="margin-left:.3rem" data-del-id="' + escHtml(note.id) + '">Delete</button>' +
        '</div>' +
      '</div>';
    });
    html += '</div>';
  } else {
    html = '<p class="reader-hint">No notes for ' + escHtml(chLabel) + '.</p>';
  }
  // Compose form
  html += '<div class="reader-panel-compose">' +
    '<textarea class="bsw-note-textarea" placeholder="Add a chapter note for ' + escHtml(chLabel) + ' (click a verse number to note a specific verse)…" rows="3"></textarea>' +
    '<p class="reader-hint" style="font-size:.72rem;margin:.15rem 0 .3rem;">Verse-specific notes: click the verse number ↑</p>' +
    '<div style="margin-top:0.3rem;display:flex;gap:.4rem;justify-content:flex-end;">' +
      '<button class="bsw-note-action-btn reader-panel-note-save">Save</button>' +
    '</div>' +
  '</div>';
  container.innerHTML = html;

  // Wire delete buttons
  container.querySelectorAll('[data-del-id]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      deleteNoteV2(btn.getAttribute('data-del-id'));
      _loadReaderNotes(parsed, container);
    });
  });

  // Wire save button
  var ta      = container.querySelector('.bsw-note-textarea');
  var saveBtn = container.querySelector('.reader-panel-note-save');
  if (ta && saveBtn) {
    saveBtn.addEventListener('click', function () {
      var text = ta.value.trim();
      if (!text) return;
      createNoteV2(parsed, text);
      ta.value = '';
      _loadReaderNotes(parsed, container);
    });
  }
}

function _loadReaderCommentary(parsed, container) {
  container._commLoaded = true;
  var src = getCommentarySource();

  var opts = COMMENTARY_SOURCES.map(function (s) {
    return '<option value="' + escHtml(s.id) + '"' + (s.id === src ? ' selected' : '') + '>' + escHtml(s.label) + '</option>';
  }).join('');

  container.innerHTML =
    '<div class="reader-panel-comm-picker">' +
      '<select class="reader-panel-comm-select">' + opts + '</select>' +
    '</div>' +
    '<div class="reader-panel-comm-body"><p class="reader-hint">Loading commentary…</p></div>';

  var sel    = container.querySelector('.reader-panel-comm-select');
  var bodyEl = container.querySelector('.reader-panel-comm-body');

  function loadSrc(source) {
    bodyEl.innerHTML = '<p class="reader-hint">Loading commentary…</p>';
    loadCommentary(parsed.bookId, source).then(function (data) {
      if (!data) { bodyEl.innerHTML = '<p class="reader-hint">No commentary available.</p>'; return; }
      var chData = data[String(parsed.ch)];
      if (!chData) { bodyEl.innerHTML = '<p class="reader-hint">No commentary for this chapter.</p>'; return; }
      // Find the nearest section at or before the starting verse.
      var sectionKeys = Object.keys(chData).map(Number).sort(function (a, b) { return a - b; });
      var startV = parsed.v || 1;
      var endV   = parsed.wholeChapter ? 9999 : (parsed.endV || startV);
      var foundV = null;
      for (var vi = startV; vi >= 1; vi--) {
        if (chData[String(vi)]) { foundV = vi; break; }
      }
      var html = '';
      if (foundV !== null) {
        html += '<div class="reader-panel-comm-section">' + chData[String(foundV)] + '</div>';
        sectionKeys.forEach(function (v) {
          if (v > startV && v <= endV && chData[String(v)]) {
            html += '<div class="reader-panel-comm-section">' + chData[String(v)] + '</div>';
          }
        });
      }
      if (!html) { bodyEl.innerHTML = '<p class="reader-hint">No commentary found for this passage.</p>'; return; }
      var src2 = COMMENTARY_SOURCES.find(function (s) { return s.id === source; });
      html += '<p class="reader-hint" style="margin-top:1rem;font-style:italic">' + escHtml((src2 && src2.attr) || '') + '</p>';
      bodyEl.innerHTML = html;
      wireRefLinks(bodyEl);
    }).catch(function () {
      bodyEl.innerHTML = '<p class="reader-hint">Could not load commentary.</p>';
    });
  }

  sel.addEventListener('change', function () {
    setCommentarySource(sel.value);
    loadSrc(sel.value);
  });
  loadSrc(src);
}

function _buildXrefHtml(xdata, parsed) {
  var html = '';
  // Cap to one chapter for whole-chapter views; allow up to 2 for verse ranges
  var maxCh = parsed.wholeChapter
    ? parsed.ch
    : Math.min(parsed.endCh || parsed.ch, parsed.ch + 1);
  for (var c = parsed.ch; c <= maxCh; c++) {
    var chData = xdata[String(c)];
    if (!chData) continue;
    var startV = (c === parsed.ch) ? (parsed.v || 1) : 1;
    var stopV  = (c === (parsed.endCh || c))
      ? (parsed.wholeChapter ? 9999 : (parsed.endV || parsed.v || 9999))
      : 9999;
    Object.keys(chData).map(Number)
      .filter(function (n) { return n >= startV && n <= stopV; })
      .sort(function (a, b) { return a - b; })
      .forEach(function (vNum) {
        var rawRefs = chData[String(vNum)];
        if (!rawRefs || !rawRefs.length) return;
        var entries = rawRefs.map(parseCrossRefEntry)
          .sort(function (a, b) { return b.votes - a.votes; })
          .slice(0, 8)
          .sort(_compareCanonical);
        html += '<div class="reader-xref-group">' +
          '<div class="reader-xref-group__title">v.' + vNum + '</div>' +
          '<ul class="reader-xref-group__list">';
        entries.forEach(function (e) {
          html += '<li class="reader-xref-group__item">' +
            '<span class="reader-xref-group__link" data-ref="' + escHtml(e.ref) + '" role="button" tabindex="0">' + escHtml(e.ref) + '</span>' +
          '</li>';
        });
        html += '</ul></div>';
      });
  }
  return html;
}

function _loadReaderXrefs(parsed, container) {
  container._xrefsLoaded = true;
  container.innerHTML = '<p class="reader-hint">Loading cross-references…</p>';

  // For multi-passage lookups, show refs for only the first passage and offer chips
  // to switch. The groups array holds all loaded passages.
  var groups   = window._readerGroups || [];
  var multiPassage = groups.length > 1;

  loadCrossRefs(parsed.bookId).then(function (xdata) {
    if (!xdata) { container.innerHTML = '<p class="reader-xref-empty">No cross-references for this book.</p>'; return; }

    var bk     = metaBooks && metaBooks.find(function (b) { return b.id === parsed.bookId; });
    var chName = (bk ? bk.name : parsed.bookId) + ' ' + parsed.ch;

    var noteHtml = multiPassage
      ? '<p class="reader-hint reader-xref-scope-note">Showing cross-refs for <strong>' + escHtml(chName) + '</strong></p>'
      : '';

    // Chip row for switching passages when multiple groups are loaded
    var chipsHtml = '';
    if (multiPassage) {
      chipsHtml = '<div class="reader-xref-chips">';
      groups.forEach(function (g, i) {
        var bkG = metaBooks && metaBooks.find(function (b) { return b.id === g.ref.bookId; });
        var label = (bkG ? bkG.name : (g.ref.bookId || '')) + ' ' + g.ref.ch;
        var active = (g.ref.bookId === parsed.bookId && g.ref.ch === parsed.ch);
        chipsHtml += '<button class="reader-xref-chip' + (active ? ' reader-xref-chip--active' : '') +
          '" data-xref-idx="' + i + '">' + escHtml(label) + '</button>';
      });
      chipsHtml += '</div>';
    }

    var bodyHtml = _buildXrefHtml(xdata, parsed);
    if (!bodyHtml) bodyHtml = '<p class="reader-xref-empty">No cross-references for this passage.</p>';

    container.innerHTML = noteHtml + chipsHtml + '<div class="reader-xref-body">' + bodyHtml + '</div>';
    wireRefLinks(container);

    // Wire chip clicks to reload refs for the selected passage
    if (multiPassage) {
      container.querySelectorAll('.reader-xref-chip').forEach(function (chip) {
        chip.addEventListener('click', function () {
          var idx = parseInt(chip.getAttribute('data-xref-idx'), 10);
          var g2  = groups[idx];
          if (!g2 || !g2.ref.bookId) return;
          // Update active chip
          container.querySelectorAll('.reader-xref-chip').forEach(function (c) {
            c.classList.toggle('reader-xref-chip--active', c === chip);
          });
          // Reload xrefs for selected passage
          loadCrossRefs(g2.ref.bookId).then(function (xdata2) {
            var bodyEl = container.querySelector('.reader-xref-body');
            if (!bodyEl) return;
            var bkG2  = metaBooks && metaBooks.find(function (b) { return b.id === g2.ref.bookId; });
            var label2 = (bkG2 ? bkG2.name : g2.ref.bookId) + ' ' + g2.ref.ch;
            var note2  = container.querySelector('.reader-xref-scope-note');
            if (note2) note2.innerHTML = 'Showing cross-refs for <strong>' + escHtml(label2) + '</strong>';
            if (!xdata2) { bodyEl.innerHTML = '<p class="reader-xref-empty">No cross-references for this book.</p>'; return; }
            var h2 = _buildXrefHtml(xdata2, g2.ref);
            bodyEl.innerHTML = h2 || '<p class="reader-xref-empty">No cross-references for this passage.</p>';
            wireRefLinks(bodyEl);
          }).catch(function () {});
        });
      });
    }
  }).catch(function () {
    container.innerHTML = '<p class="reader-xref-empty">Could not load cross-references.</p>';
  });
}

export function renderReaderSidebar(bookId, chapters, activeCh) {
  var sidebar = document.getElementById('reader-sidebar');
  if (!sidebar || !chapters) return;
  var chNums   = Object.keys(chapters).map(Number).sort(function (a, b) { return a - b; });
  var bk       = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
  var bookName = bk ? bk.name : bookId;

  var html = '<div class="reader-sidebar__book">' + escHtml(bookName) + '</div>';
  html += '<div class="reader-sidebar__intro-row">';
  html += '<button class="reader-sidebar__intro' + (activeCh === 0 ? ' reader-sidebar__intro--active' : '') +
    '" data-nav-label="' + escHtml(bookName + ' 0') + '">Intro</button>';
  html += '</div>';
  html += '<div class="reader-sidebar__grid">';
  chNums.forEach(function (n) {
    html += '<button class="reader-sidebar__ch' + (n === activeCh ? ' reader-sidebar__ch--active' : '') +
      '" data-nav-label="' + escHtml(bookName + ' ' + n) + '">' + n + '</button>';
  });
  html += '</div>';
  sidebar.innerHTML = html;

  sidebar.querySelectorAll('[data-nav-label]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var label = btn.getAttribute('data-nav-label');
      var input = document.getElementById('reader-lookup-input');
      if (input) input.value = label;
      if (window._readerLookupFn) window._readerLookupFn();
    });
  });
}

// Expose so interlinear.js can refresh the sidebar on-demand (avoids circular import).
window._renderSidebarFn = renderReaderSidebar;

// ── Book introduction ─────────────────────────────────────────────────────
var _bookInfoCache = {};

function _adjacentBook(bookId, delta, wrap) {
  if (!metaBooks || !bookId) return null;
  var idx = bookOrder && (bookId in bookOrder) ? bookOrder[bookId] : -1;
  if (idx < 0) return null;
  var nextIdx = idx + delta;
  if (wrap) nextIdx = ((nextIdx % metaBooks.length) + metaBooks.length) % metaBooks.length;
  var bk = metaBooks[nextIdx];
  if (!bk) return null;
  return { id: bk.id, name: bk.name, chapters: bk.chapters || 999 };
}

function _outlineNavRef(bookName, chapters) {
  if (!chapters) return null;
  return bookName + ' ' + chapters.replace(/[–—]/g, '-').trim();
}

var _VERSE_CITE_RE = /((?:\d\s?)?[A-Z][a-z]+(?:\s+of\s+[A-Z][a-z]+)?\.?\s+\d+:\d+(?:[–\-]\d+)?)/g;
var _BARE_CH_V_RE  = /\b(\d+:\d+(?:[-–](?!\d+:)\d+)?)\b/g;

function _autoLinkRefs(text, bookName) {
  if (!text) return '';
  var parts = text.split(_VERSE_CITE_RE);
  return parts.map(function (part, i) {
    if (i % 2 === 1) {
      return '<a class="ref" data-ref="' + escHtml(part.trim()) + '">' + escHtml(part) + '</a>';
    }
    if (bookName) {
      var subparts = part.split(_BARE_CH_V_RE);
      return subparts.map(function (sub, j) {
        if (j % 2 === 1) {
          return '<a class="ref" data-ref="' + escHtml(bookName + ' ' + sub) + '">' + escHtml(sub) + '</a>';
        }
        return escHtml(sub);
      }).join('');
    }
    return escHtml(part);
  }).join('');
}

function _riSection(heading, contentHtml) {
  return '<section class="ri-section">' +
    '<h3 class="ri-section__heading">' + escHtml(heading) + '</h3>' +
    contentHtml + '</section>';
}

var _RH_ERAS = [
  { slug: 'creation',         label: 'Creation' },
  { slug: 'patriarchs',       label: 'Patriarchs' },
  { slug: 'moses',            label: 'Moses & Exodus' },
  { slug: 'conquest',         label: 'Conquest & Judges' },
  { slug: 'monarchy',         label: 'The Monarchy' },
  { slug: 'exile',            label: 'Exile' },
  { slug: 'restoration',      label: 'Restoration' },
  { slug: 'intertestamental', label: 'Intertestamental' },
  { slug: 'gospels',          label: 'The Gospels' },
  { slug: 'church',           label: 'The Church' },
  { slug: 'consummation',     label: 'Consummation' }
];

function _renderTimeline(tl, bookTitle) {
  var html = '';

  // Era arc: segmented colour bar + active-era label (replaces the old wrapping chip list)
  if (tl.period) {
    var _activeEra = null;
    for (var _ei = 0; _ei < _RH_ERAS.length; _ei++) {
      if (_RH_ERAS[_ei].slug === tl.period) { _activeEra = _RH_ERAS[_ei]; break; }
    }
    html += '<div class="ri-tl-arc" aria-label="Redemptive-historical era">';
    html += '<div class="ri-tl-arc-track">';
    _RH_ERAS.forEach(function (era) {
      var cls = 'ri-tl-era' + (era.slug === tl.period ? ' ri-tl-era--active' : '');
      html += '<span class="' + cls + '" title="' + escHtml(era.label) + '"></span>';
    });
    html += '</div>';
    if (_activeEra) {
      html += '<div class="ri-tl-arc-lbl">Period: <strong>' + escHtml(_activeEra.label) + '</strong></div>';
    }
    html += '</div>';
  }

  var before = (tl.before || []).slice();
  var after  = (tl.after  || []).slice();
  while (before.length < 3) before.unshift(null);
  while (after.length  < 3) after.push(null);

  html += '<div class="ri-tl-row">';
  before.concat([null], after).forEach(function (item, idx) {
    if (idx === 3) {
      // Centre slot — current book. Dot is first child so the connector line bisects it
      // regardless of whether a date label follows.
      html += '<div class="ri-tl-item">' +
        '<div class="ri-tl-dot ri-tl-dot--current"></div>' +
        '<div class="ri-tl-label ri-tl-label--current">' + escHtml(bookTitle) + '</div>' +
        (tl.date ? '<div class="ri-tl-year ri-tl-year--current">' + escHtml(tl.date) + '</div>' : '') +
      '</div>';
      return;
    }
    if (!item) {
      html += '<div class="ri-tl-item ri-tl-item--empty"><div class="ri-tl-dot ri-tl-dot--empty"></div></div>';
      return;
    }
    var type    = item.type  || 'event';
    var label   = item.label || '';
    var year    = item.year  || '';
    var ref     = item.ref   || '';
    var href    = (type === 'book' && ref) ? (READER_URL + '?ref=' + encodeURIComponent(ref)) : null;
    // book-type: navigate to reader via href. event/world with a ref: hoverable link (tooltip + modal).
    var labelEl = href
      ? '<a class="ri-tl-label ri-tl-label--' + escHtml(type) + '" href="' + escHtml(href) + '">' + escHtml(label) + '</a>'
      : ref
        ? '<a class="ref ri-tl-label ri-tl-label--' + escHtml(type) + '" data-ref="' + escHtml(ref) + '">' + escHtml(label) + '</a>'
        : '<span class="ri-tl-label ri-tl-label--' + escHtml(type) + '">' + escHtml(label) + '</span>';
    // Dot first — keeps it at a fixed vertical position so the connector line always
    // bisects it, even when a year label appears below.
    html += '<div class="ri-tl-item">' +
      '<div class="ri-tl-dot ri-tl-dot--' + escHtml(type) + '"></div>' +
      labelEl +
      (year ? '<div class="ri-tl-year">' + escHtml(year) + '</div>' : '') +
    '</div>';
  });
  html += '</div>';
  return html;
}

function _renderIntroInReader(el, d, bookId, bookName, maxCh) {
  var ch1Lbl = bookName + ' 1';
  var body   = '';
  var _bk    = d.title;

  body += '<div class="ri-meta">' +
    '<span><strong>Author:</strong> ' + escHtml(d.author || '—') + '</span>' +
    '<span><strong>Date:</strong> '   + escHtml(d.date   || '—') + '</span>' +
    '</div>';

  var kvFeat     = (d.key_verses && d.key_verses.length) ? d.key_verses[0] : null;
  var kvFeatRef  = kvFeat ? kvFeat.ref  : (d.key_verse  || null);
  var kvFeatNote = kvFeat ? (kvFeat.note || null) : null;
  if (kvFeatRef) {
    body += '<div class="reader-intro-keyverse">' +
      '<span class="reader-intro-kv-label">Key Verse</span>' +
      '<a class="ref ri-keyverse__ref" data-ref="' + escHtml(kvFeatRef) + '">' + escHtml(kvFeatRef) + '</a>' +
      (kvFeatNote ? '<span class="reader-intro-kv-note">' + escHtml(kvFeatNote) + '</span>' : '') +
      '</div>';
  }

  if (d.purpose || d.setting) {
    body += _riSection('Purpose', '<p class="ri-body">' + _autoLinkRefs(d.purpose || d.setting, _bk) + '</p>');
  }
  if (d.context) {
    body += _riSection('Historical Context', '<p class="ri-body">' + _autoLinkRefs(d.context, _bk) + '</p>');
  }
  if (d.themes_detail && d.themes_detail.length) {
    var tdHtml = d.themes_detail.map(function (t) {
      return '<div class="ri-theme-item">' +
        '<h4 class="ri-theme-title">' + escHtml(t.title) + '</h4>' +
        '<p class="ri-body">' + _autoLinkRefs(t.text, _bk) + '</p>' +
        '</div>';
    }).join('');
    body += _riSection('Key Themes', tdHtml);
  } else if (d.themes && d.themes.length) {
    body += _riSection('Themes', '<div class="reader-bookinfo-themes">' +
      d.themes.map(function (t) {
        return '<span class="reader-bookinfo-theme">' + escHtml(t) + '</span>';
      }).join('') + '</div>');
  }
  if (d.key_people && d.key_people.length) {
    body += _riSection('Key People', '<ul class="ri-people">' +
      d.key_people.map(function (p) {
        return '<li class="ri-person"><strong class="ri-person__name">' +
          escHtml(p.name) + '</strong><span class="ri-person__role"> — ' +
          escHtml(p.role) + '</span></li>';
      }).join('') + '</ul>');
  }
  if (d.outline && d.outline.length) {
    body += _riSection('Outline', '<ol class="reader-bookinfo-outline">' +
      d.outline.map(function (s) {
        var navRef = _outlineNavRef(d.title, s.chapters) || s.ref || null;
        var link = navRef
          ? '<a class="ri-outline-nav" data-nav-label="' + escHtml(navRef) + '">' + escHtml(s.label) + '</a>'
          : escHtml(s.label);
        return '<li>' + link +
          (s.chapters ? ' <span class="reader-bookinfo-ch">ch. ' + escHtml(s.chapters) + '</span>' : '') +
          '</li>';
      }).join('') + '</ol>');
  }
  if (d.key_verses && d.key_verses.length) {
    body += _riSection('Key Verses', '<ul class="ri-keyverses">' +
      d.key_verses.map(function (kv) {
        return '<li class="ri-keyverse">' +
          '<a class="ref ri-keyverse__ref" data-ref="' + escHtml(kv.ref) + '">' + escHtml(kv.ref) + '</a>' +
          (kv.note ? '<span class="ri-keyverse__note"> — ' + escHtml(kv.note) + '</span>' : '') +
          '</li>';
      }).join('') + '</ul>');
  } else if (d.key_verse) {
    body += _riSection('Key Verse',
      '<p class="ri-body"><a class="ref" data-ref="' + escHtml(d.key_verse) + '">' +
      escHtml(d.key_verse) + '</a></p>');
  }
  if (d.christ_connection) {
    body += _riSection('Christ in ' + d.title,
      '<p class="ri-body ri-body--christ">' + _autoLinkRefs(d.christ_connection, _bk) + '</p>');
  }
  if (d.timeline) {
    body += _riSection('Redemptive-Historical Timeline', _renderTimeline(d.timeline, d.title));
  }

  /* Related Maps — link to the maps page pre-selecting each relevant map */
  var mapIds = BOOK_MAP_LINKS[bookId] || [];
  if (mapIds.length) {
    var mapChips = mapIds.map(function (id) {
      var label = MAP_LABELS[id] || id;
      return '<a class="ri-map-chip" href="' + escHtml(MAPS_URL + '#' + id) + '" target="_blank" rel="noopener">' +
        '🗺 ' + escHtml(label) +
      '</a>';
    }).join('');
    body += _riSection('Related Maps', '<div class="ri-map-chips">' + mapChips + '</div>');
  }

  var prevBk    = _adjacentBook(bookId, -1, true);
  var prevBkBtn = prevBk
    ? '<button class="reader-nav-btn" data-nav-label="' + escHtml(prevBk.name + ' ' + prevBk.chapters) + '">← ' + escHtml(prevBk.name) + '</button>'
    : '<span></span>';

  el.innerHTML =
    '<div class="reader-intro-page">' +
      '<div class="reader-chapter-nav">' +
        prevBkBtn +
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

  _wireReaderNav(el);
  wireRefLinks(el);
  el.querySelectorAll('.ri-body, .ri-keyverse__note, .ri-person__role, .reader-intro-kv-note').forEach(function (b) {
    b._termsTagged = false;
    autoTagTerms(b);
  });
  /* Tag biblical place names after terms are done so we don't double-wrap */
  var introInner = el.querySelector('.reader-intro-inner');
  if (introInner && window.BibleUI && window.BibleUI.autoTagPlacesIn) {
    window.BibleUI.autoTagPlacesIn(introInner);
  }
}

function _wireReaderNav(el) {
  if (el._navWired) return;
  el._navWired = true;
  el.addEventListener('click', function (e) {
    var btn = e.target.closest('.reader-nav-btn, .ri-outline-nav');
    if (!btn) return;
    var label = btn.getAttribute('data-nav-label');
    if (!label) return;
    var lookupInput = document.getElementById('reader-lookup-input');
    if (lookupInput) lookupInput.value = label;
    if (window._readerLookupFn) window._readerLookupFn();
  });
}

function _renderReaderBookIntro(bookId, bookName) {
  var el = document.getElementById('reader-results');
  if (!el) return;
  var bkMeta = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
  var maxCh  = bkMeta ? (bkMeta.chapters || 999) : 999;

  window._readerNavState = { bookId: bookId, bookName: bookName, ch: 0, maxCh: maxCh };
  syncBrowseSelects(bookId, 0);

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
      if (window._readerNavState && window._readerNavState.bookId === bookId && window._readerNavState.ch === 0) {
        _renderIntroInReader(el, data, bookId, bookName, maxCh);
      }
    })
    .catch(function () {
      el.innerHTML = '<p class="reader-hint">No introduction available for this book yet.</p>';
    });
}

// ── Commentary Mode — RD-M ────────────────────────────────────────────────
// INTENT: Verse-locked split view. Replaces the flowing reader text with a
//   per-verse CSS grid so each verse is horizontally aligned with its commentary.
//   _commModeChData stores { [srcId]: chapterObj } for the current passage;
//   it is rebuilt whenever loadReaderPanelContent fires with a new passage.
// CHANGE? _commModeChData is keyed only for the first passage's chapter. If
//   multi-passage commentary is needed, switch to a [bookId+ch] composite key.
// VERIFY: Load John 3, click Commentary, observe per-verse rows with source
//   picker. Navigate to John 4 — rows update. Click Commentary again to restore.

var _commModeChData = null;

export function initCommModeToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-comm-toggle')) return;

  var btn = document.createElement('button');
  btn.id        = 'reader-comm-toggle';
  btn.className = 'reader-comm-toggle';
  btn.type      = 'button';
  btn.textContent = 'Commentary';

  // Restore visual state from localStorage (activation happens on next passage load)
  var saved = false;
  try { saved = localStorage.getItem('bsw_reader_comm_mode') === '1'; } catch (e) {}
  btn.setAttribute('aria-pressed', saved ? 'true' : 'false');

  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);

  btn.addEventListener('click', function () {
    if (btn.getAttribute('aria-pressed') === 'true') {
      _deactivateCommMode();
    } else {
      _activateCommMode();
    }
  });
}

function _activateCommMode() {
  var parsed = _readerPanelParsed;
  if (!parsed || !parsed.bookId) return;

  var btn = document.getElementById('reader-comm-toggle');
  if (btn) btn.setAttribute('aria-pressed', 'true');
  try { localStorage.setItem('bsw_reader_comm_mode', '1'); } catch (e) {}

  var layout = document.querySelector('.reader-layout');
  if (layout) layout.classList.add('reader-layout--comm-mode');

  var bookId = parsed.bookId;
  var ch     = parsed.ch;
  var chDataMap = {};
  _commModeChData = chDataMap;

  Promise.all(COMMENTARY_SOURCES.map(function (s) {
    return loadCommentary(bookId, s.id).then(function (bookData) {
      chDataMap[s.id] = (bookData && bookData[String(ch)]) || null;
    }).catch(function () { chDataMap[s.id] = null; });
  })).then(function () {
    // Guard: a subsequent navigation may have replaced _commModeChData already
    if (_commModeChData === chDataMap) _buildCommGrid();
  });
}

function _deactivateCommMode() {
  var btn = document.getElementById('reader-comm-toggle');
  if (btn) btn.setAttribute('aria-pressed', 'false');
  try { localStorage.setItem('bsw_reader_comm_mode', '0'); } catch (e) {}

  var layout = document.querySelector('.reader-layout');
  if (layout) layout.classList.remove('reader-layout--comm-mode');

  _commModeChData = null;

  // Re-render from scratch to restore the original inline verse flow
  if (window._readerLookupFn) window._readerLookupFn();
}

// Return largest key ≤ v in chd, or null if none exists.
function _commFindKey(chd, v) {
  if (!chd) return null;
  var keys = Object.keys(chd).map(Number).sort(function (a, b) { return a - b; });
  for (var i = keys.length - 1; i >= 0; i--) {
    if (keys[i] <= v) return keys[i];
  }
  return null;
}

function _buildCommGrid() {
  var resultsEl = document.getElementById('reader-results');
  if (!resultsEl) return;

  resultsEl.querySelectorAll('.reader-result-group').forEach(function (groupEl) {
    var textEl = groupEl.querySelector('.reader-result-group__text');
    if (!textEl) return;
    var verseSpans = Array.prototype.slice.call(textEl.querySelectorAll('.reader-verse'));
    if (!verseSpans.length) return;

    var verseData = verseSpans.map(function (span) {
      return {
        span: span,
        ch:   parseInt(span.getAttribute('data-ch'), 10),
        v:    parseInt(span.getAttribute('data-v'),  10)
      };
    });

    var grid = document.createElement('div');
    grid.className   = 'reader-comm-grid';
    grid._verseData  = verseData; // stored so _rebuildCommCells can re-run on source change

    // Row 1: single global source picker spanning both columns
    grid.appendChild(_buildCommGlobalPicker());

    // Rows 2+: one verse cell per verse in column 1, with explicit grid-row
    verseData.forEach(function (vd, idx) {
      var cell = document.createElement('div');
      cell.className      = 'reader-comm-cell reader-comm-cell--verse';
      cell.style.gridRow    = String(idx + 2); // row 1 = picker
      cell.style.gridColumn = '1';
      cell.appendChild(vd.span);
      grid.appendChild(cell);
    });

    textEl.parentNode.replaceChild(grid, textEl);

    // Commentary cells: one per section, spanning the rows of all verses in the section
    _rebuildCommCells(grid);
  });
}

function _buildCommGlobalPicker() {
  var curSrc = getCommentarySource();
  var wrap   = document.createElement('div');
  wrap.className = 'reader-comm-picker-row';

  var lbl = document.createElement('span');
  lbl.className   = 'reader-comm-picker-label';
  lbl.textContent = 'Source:';
  wrap.appendChild(lbl);

  var sel = document.createElement('select');
  sel.className = 'reader-comm-src-sel';
  sel.setAttribute('aria-label', 'Commentary source');
  COMMENTARY_SOURCES.forEach(function (s) {
    var opt = document.createElement('option');
    opt.value       = s.id;
    opt.textContent = s.label;
    if (s.id === curSrc) opt.selected = true;
    sel.appendChild(opt);
  });
  wrap.appendChild(sel);

  sel.addEventListener('change', function () {
    setCommentarySource(sel.value);
    // Rebuild commentary cells in all grids and keep sibling pickers in sync
    document.querySelectorAll('.reader-comm-grid').forEach(function (g) {
      _rebuildCommCells(g);
      var sib = g.querySelector('.reader-comm-src-sel');
      if (sib && sib !== sel) sib.value = sel.value;
    });
  });

  return wrap;
}

function _rebuildCommCells(grid) {
  if (!grid._verseData) return;
  var verseData = grid._verseData;
  var srcId     = getCommentarySource();
  var chd       = _commModeChData && _commModeChData[srcId];

  // Remove previous commentary cells, keep picker and verse cells
  grid.querySelectorAll('.reader-comm-cell--comm').forEach(function (el) { el.remove(); });

  // Group consecutive verses that share the same foundKey into sections.
  // Each section gets exactly one commentary cell spanning all its rows.
  var sections = [];
  verseData.forEach(function (vd, idx) {
    var foundKey = _commFindKey(chd, vd.v);
    var last = sections.length ? sections[sections.length - 1] : null;
    if (last && last.foundKey === foundKey && last.ch === vd.ch) {
      last.endIdx = idx;
    } else {
      sections.push({ foundKey: foundKey, ch: vd.ch, startIdx: idx, endIdx: idx });
    }
  });

  sections.forEach(function (sec) {
    var startRow  = sec.startIdx + 2; // +2: row 1 is the picker
    var spanCount = sec.endIdx - sec.startIdx + 1;

    var cell = document.createElement('div');
    cell.className      = 'reader-comm-cell reader-comm-cell--comm';
    cell.style.gridRow    = startRow + ' / span ' + spanCount;
    cell.style.gridColumn = '2';

    if (sec.foundKey !== null && chd && chd[String(sec.foundKey)]) {
      var html = chd[String(sec.foundKey)];
      // If this section's foundKey is before the first displayed verse, show a
      // section-range note so the reader knows the commentary covers more context.
      if (sec.foundKey < verseData[sec.startIdx].v) {
        var allKeys = Object.keys(chd).map(Number).sort(function (a, b) { return a - b; });
        var nextKey = null;
        for (var k = 0; k < allKeys.length; k++) {
          if (allKeys[k] > sec.foundKey) { nextKey = allKeys[k]; break; }
        }
        var rangeEnd = nextKey !== null ? (nextKey - 1) : '…';
        html = '<p class="reader-comm-span-note">▸ section v.' + sec.foundKey + '–' + rangeEnd + '</p>' + html;
      }
      cell.innerHTML = html;
      wireRefLinks(cell);
    } else {
      cell.innerHTML = '<p class="reader-hint">No commentary available.</p>';
    }

    grid.appendChild(cell);
  });
}
