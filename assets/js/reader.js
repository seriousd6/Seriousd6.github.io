/* reader.js — Bible reader page: lookup, browse, keyboard nav, sidebar, compare */
'use strict';

import {
  getVersion, setVersion, loadBook, loadCrossRefs, loadCommentary, parseRef, parseMultiRef,
  normalizeBook, metaBooks, metaVersions, bookOrder, READER_URL, SEARCH_URL, escHtml,
  _compareCanonical, parseCrossRefEntry, resolveVerses,
  ATTRIBUTION, COMMENTARY_SOURCES, getCommentarySource, setCommentarySource,
  onVersionChange, _resolve,
  LIB_INDEX_URL, LIB_DOCS_BASE, LIB_ABBREV_MAP, libDocCache, libIndexCache
} from './core.js';
import { autoTagTerms } from './terms.js';
import {
  getNotes, getNote, _historyPush, _recordReadingDay, getNotesForVerse, getNotesForChapter,
  createNoteV2, deleteNoteV2, updateNoteV2, _noteRelTime
} from './storage.js';
import {
  wireRefLinks, wireRefEl, applyHighlights, applyBookmarks, autoTagRefs,
  autoTagBareRefs, autoTagBareChapters
} from './wire.js';
import { getParallelsEnabled, injectAllParallelPanels } from './parallels.js';
import {
  getInterlinearEnabled, injectAllInterlinearRows
} from './interlinear.js';

export { initSplitToggle, initFontSizeControls, initWideToggle, initSidebarToggle } from './interlinear.js';

// ── Compare state ─────────────────────────────────────────────────────────
var COMPARE_KEY = 'bsw_compare';
export function isCompareEnabled()    { return !!localStorage.getItem(COMPARE_KEY); }
export function getCompareVersion()   { return localStorage.getItem(COMPARE_KEY) || ''; }
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
          if (metaVersions[i].id !== primary) { def = metaVersions[i].id; break; }
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

export function injectComparePanel(groups, cmpVer, resultsEl) {
  // Delegate to interlinear.js implementation
  var primaryVer = getVersion();
  var domGroups  = resultsEl.querySelectorAll('.reader-result-group');

  domGroups.forEach(function (groupEl, gIdx) {
    var g = groups[gIdx];
    if (!g) return;
    var textEl    = groupEl.querySelector('.reader-result-group__text');
    var attrEl    = groupEl.querySelector('.reader-result-group__attr');
    var hintEl    = !textEl ? groupEl.querySelector('.reader-hint') : null;
    var contentEl = textEl || hintEl;
    if (!contentEl) return;

    var wrap = document.createElement('div');
    wrap.className = 'reader-compare-wrap';
    var p1 = document.createElement('div');
    p1.className = 'reader-compare-panel';
    p1.appendChild(_buildComparePanelHdr(primaryVer, 'primary'));
    contentEl.parentNode.removeChild(contentEl);
    p1.appendChild(contentEl);
    if (attrEl && attrEl.parentNode) { attrEl.parentNode.removeChild(attrEl); p1.appendChild(attrEl); }

    var p2 = document.createElement('div');
    p2.className = 'reader-compare-panel';
    p2.appendChild(_buildComparePanelHdr(cmpVer, 'secondary'));
    var p2body = document.createElement('div');
    p2body.innerHTML = '<p class="reader-hint">Loading…</p>';
    p2.appendChild(p2body);
    wrap.appendChild(p1);
    wrap.appendChild(p2);

    var bottomNav = groupEl.querySelector('.reader-chapter-nav--bottom');
    if (bottomNav) groupEl.insertBefore(wrap, bottomNav);
    else groupEl.appendChild(wrap);

    resolveVerses(g.ref, cmpVer).then(function (verses) {
      if (!verses || !verses.length) {
        p2body.innerHTML = '<p class="reader-hint">Not available in ' + escHtml(cmpVer) + '.</p>';
        return;
      }
      var html = '<p class="reader-result-group__text">';
      verses.forEach(function (vObj) {
        html += '<span class="reader-verse" data-book="' + escHtml(g.ref.bookName) +
          '" data-ch="' + vObj.chapter + '" data-v="' + vObj.verse + '">' +
          '<sup class="reader-verse__num">' + vObj.verse + '</sup>' +
          escHtml(vObj.text) + '</span> ';
      });
      html += '</p>';
      var attr = ATTRIBUTION[cmpVer];
      if (attr) html += '<p class="reader-result-group__attr">' + escHtml(attr) + '</p>';
      p2body.innerHTML = html;
      applyHighlights(p2body);
    }).catch(function () {
      p2body.innerHTML = '<p class="reader-hint">Could not load ' + escHtml(cmpVer) + '.</p>';
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
window._readerLookupFn  = null;

// ── initReaderPage ────────────────────────────────────────────────────────
export function initReaderPage() {
  initReaderLookup();
  initReaderBrowse();
  initReaderKeyboard();
  _ensureReaderPanelStructure();

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

  function doLookup() {
    var q         = input.value.trim();
    var resultsEl = document.getElementById('reader-results');
    if (!q) { if (resultsEl) resultsEl.innerHTML = ''; return; }

    var refs = parseMultiRef(q, null);

    // Bare book name → whole book (one ref per chapter)
    if (!refs.length) {
      var _bid = normalizeBook(q);
      var _bkm = _bid && metaBooks && metaBooks.find(function (b) { return b.id === _bid; });
      if (_bkm) {
        for (var _ci = 1; _ci <= (_bkm.chapters || 1); _ci++) {
          refs.push({ bookId: _bkm.id, bookName: _bkm.name, ch: _ci, v: 1, endCh: _ci, endV: 9999,
            display: _bkm.name + ' ' + _ci, wholeChapter: true });
        }
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

        if (g.ref.bookId) groupEl.appendChild(_buildNavButtons(g.ref, 'top'));

        var title = document.createElement('h2');
        title.className   = 'reader-result-group__title';
        title.textContent = g.ref.display;
        groupEl.appendChild(title);

        var textEl = document.createElement('p');
        textEl.className = 'reader-result-group__text';
        g.verses.forEach(function (vObj) {
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
        groupEl.appendChild(attrEl);

        if (g.ref.bookId) groupEl.appendChild(_buildNavButtons(g.ref, 'bottom'));

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
          loadReaderPanelContent(g.ref);
        }
      });

      if (!any) {
        resultsEl.innerHTML = '<p class="reader-hint">Verse not found in ' + escHtml(ver) + '.</p>';
        return;
      }

      applyHighlights(resultsEl);
      applyBookmarks(resultsEl);
      wireVerseNumberPopup(resultsEl);
      injectReaderFootnotes(resultsEl);

      if (isCompareEnabled()) injectComparePanel(window._readerGroups, getCompareVersion(), resultsEl);
      if (getInterlinearEnabled()) injectAllInterlinearRows(resultsEl);
      if (getParallelsEnabled()) injectAllParallelPanels(resultsEl);

      _historyPush(q, ver);
      _recordReadingDay();
    }).catch(function (err) {
      if (resultsEl) resultsEl.innerHTML = '<p class="reader-hint">Could not load passage.</p>';
      console.error('[BibleUI] reader error:', err);
    });
  }

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
    if (nextCh >= 1 && nextCh <= maxCh) {
      var newRef = parsedRef.bookName + ' ' + nextCh;
      window.location.href = READER_URL + '?ref=' + encodeURIComponent(newRef);
    } else if (nextCh < 1 && bookIdx > 0) {
      var prevBook = metaBooks && metaBooks[bookIdx - 1];
      if (prevBook) {
        window.location.href = READER_URL + '?ref=' + encodeURIComponent(prevBook.name + ' 1');
      }
    } else if (nextCh > maxCh) {
      var nextBook = metaBooks && metaBooks[bookIdx + 1];
      if (nextBook) {
        window.location.href = READER_URL + '?ref=' + encodeURIComponent(nextBook.name + ' 1');
      }
    }
  }).catch(function () {});
}

// ── initReaderBrowse ──────────────────────────────────────────────────────
export function initReaderBrowse() {
  var bookSel = document.getElementById('reader-book-select');
  var chSel   = document.getElementById('reader-ch-select');
  if (!bookSel || !chSel || !metaBooks) return;

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
export function wireVerseNumberPopup(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-verse__num').forEach(function (numEl) {
    numEl.addEventListener('click', function (e) {
      e.preventDefault();
      var verseEl  = numEl.closest('.reader-verse');
      if (!verseEl) return;
      var bookName = verseEl.getAttribute('data-book');
      var ch       = verseEl.getAttribute('data-ch');
      var v        = verseEl.getAttribute('data-v');
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
    '</div>' +
    '<div class="reader-panel-body" id="reader-panel-notes"></div>' +
    '<div class="reader-panel-body" id="reader-panel-commentary" hidden></div>' +
    '<div class="reader-panel-body" id="reader-panel-xrefs" hidden></div>';

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
  }
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
    '<textarea class="bsw-note-textarea" placeholder="Add a note for ' + escHtml(parsed.display || chLabel) + '…" rows="3"></textarea>' +
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

function _loadReaderXrefs(parsed, container) {
  container._xrefsLoaded = true;
  container.innerHTML = '<p class="reader-hint">Loading cross-references…</p>';

  loadCrossRefs(parsed.bookId).then(function (xdata) {
    if (!xdata) { container.innerHTML = '<p class="reader-xref-empty">No cross-references for this book.</p>'; return; }

    var html = '';
    for (var c = parsed.ch; c <= Math.min(parsed.endCh || parsed.ch, parsed.ch + 4); c++) {
      var chData = xdata[String(c)];
      if (!chData) continue;
      var startV = (c === parsed.ch)             ? (parsed.v || 1)      : 1;
      var stopV  = (c === (parsed.endCh || c))   ? (parsed.wholeChapter ? 9999 : (parsed.endV || parsed.v || 9999)) : 9999;
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
    if (!html) { container.innerHTML = '<p class="reader-xref-empty">No cross-references for this passage.</p>'; return; }
    container.innerHTML = html;
    wireRefLinks(container);
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
  if (tl.period) {
    html += '<div class="ri-tl-arc" aria-label="Redemptive-historical era">';
    _RH_ERAS.forEach(function (era) {
      var active = (era.slug === tl.period) ? ' ri-tl-era--active' : '';
      html += '<span class="ri-tl-era' + active + '">' + era.label + '</span>';
    });
    html += '</div>';
  }
  var before = (tl.before || []).slice();
  var after  = (tl.after  || []).slice();
  while (before.length < 3) before.unshift(null);
  while (after.length  < 3) after.push(null);

  html += '<div class="ri-tl-row">';
  before.concat([null], after).forEach(function (item, idx) {
    if (idx === 3) {
      // Centre slot — the current book. Use the larger --current dot.
      html += '<div class="ri-tl-item">' +
        (tl.date ? '<div class="ri-tl-year ri-tl-year--current">' + escHtml(tl.date) + '</div>' : '') +
        '<div class="ri-tl-dot ri-tl-dot--current"></div>' +
        '<div class="ri-tl-label ri-tl-label--current">' + escHtml(bookTitle) + '</div>' +
      '</div>';
      return;
    }
    if (!item) {
      html += '<div class="ri-tl-item ri-tl-item--empty"><div class="ri-tl-dot ri-tl-dot--empty"></div></div>';
      return;
    }
    // Data fields: label (display text), ref (passage), type (event/book/world), year
    var type    = item.type  || 'event';
    var label   = item.label || '';
    var year    = item.year  || '';
    var href    = (type === 'book' && item.ref) ? (READER_URL + '?ref=' + encodeURIComponent(item.ref)) : null;
    var labelEl = href
      ? '<a class="ri-tl-label ri-tl-label--' + escHtml(type) + '" href="' + escHtml(href) + '">' + escHtml(label) + '</a>'
      : '<span class="ri-tl-label ri-tl-label--' + escHtml(type) + '">' + escHtml(label) + '</span>';
    html += '<div class="ri-tl-item">' +
      (year ? '<div class="ri-tl-year">' + escHtml(year) + '</div>' : '') +
      '<div class="ri-tl-dot ri-tl-dot--' + escHtml(type) + '"></div>' +
      labelEl +
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
