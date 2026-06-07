/* interlinear.js — Interlinear view, book-info panel, font/wide/split/sidebar toggles */
'use strict';

import {
  getVersion, loadBook, loadInterlinear, loadStrongs, loadLexicon,
  metaBooks, metaVersions, bookOrder, READER_URL, WORD_URL, escHtml, parseRef
} from './core.js';

export var INTERLINEAR_KEY = 'bsw_interlinear';
var _riPopoverEl     = null;
var _riActiveTile    = null;
var _riScrollCleanup = null;  // fn to remove scroll-close listener; set in _riShowPopover

export function getInterlinearEnabled() {
  return localStorage.getItem(INTERLINEAR_KEY) === '1';
}
export function setInterlinearEnabled(on) {
  localStorage.setItem(INTERLINEAR_KEY, on ? '1' : '0');
}

var SPLIT_KEY   = 'bsw_split_panel';
var WIDE_KEY    = 'bsw_wide_reader';
var SIDEBAR_KEY = 'bsw_sidebar_chapters';

// ── initInterlinearToggle ─────────────────────────────────────────────────
export function initInterlinearToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-interlinear-btn')) return;

  var on  = getInterlinearEnabled();
  var btn = document.createElement('button');
  btn.id        = 'reader-interlinear-btn';
  btn.className = 'reader-interlinear-btn' + (on ? ' reader-interlinear-btn--on' : '');
  btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  btn.title     = 'Toggle interlinear view';
  btn.textContent = 'Interlinear';

  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);

  btn.addEventListener('click', function () {
    on = !on;
    setInterlinearEnabled(on);
    btn.classList.toggle('reader-interlinear-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    var resultsEl = document.getElementById('reader-results');
    if (resultsEl) {
      if (on) injectAllInterlinearRows(resultsEl);
      else    resultsEl.querySelectorAll('.reader-interlinear-row').forEach(function (el) { el.remove(); });
    }
  });
}

// ── initBookInfoToggle ────────────────────────────────────────────────────
// INTENT: The Book Info button navigates to ch=0 (the canonical full-page intro)
//   rather than maintaining a duplicate inline panel renderer. It reads bookName
//   from window._readerNavState, which is written by reader.js on every passage
//   load. If the reader hasn't loaded a passage yet (blank load), state.bookName
//   is undefined and the button does nothing — this is expected behaviour.
// CHANGE? If reader.js changes the shape of _readerNavState (e.g. renames
//   bookName), update the state.bookName read in the click handler below.
// VERIFY: Open any chapter; click Book Info; the reader should navigate to that
//   book's ch=0 intro page. Then navigate to a different book and click again —
//   it should show the new book's intro.
export function initBookInfoToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-bookinfo-btn')) return;

  var btn = document.createElement('button');
  btn.id        = 'reader-bookinfo-btn';
  btn.className = 'reader-bookinfo-btn';
  btn.title     = 'Book introduction (opens full-page intro)';
  btn.textContent = 'Book Info';

  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);

  btn.addEventListener('click', function () {
    var state = window._readerNavState;
    if (!state || !state.bookName) return;
    var inp = document.getElementById('reader-lookup-input');
    if (inp) inp.value = state.bookName + ' 0';
    if (window._readerLookupFn) window._readerLookupFn();
  });
}


// ── initViewToggle — ⚙ View popover (RD-B) ───────────────────────────────
export function initViewToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-view-btn')) return;

  var wrap = document.createElement('div');
  wrap.className = 'reader-view-wrap';

  var btn = document.createElement('button');
  btn.id        = 'reader-view-btn';
  btn.className = 'reader-view-btn';
  btn.title     = 'View options';
  btn.setAttribute('aria-haspopup', 'true');
  btn.setAttribute('aria-expanded', 'false');
  btn.textContent = '⚙ View';

  var popover = document.createElement('div');
  popover.id        = 'reader-view-popover';
  popover.className = 'reader-view-popover';
  popover.setAttribute('hidden', '');

  wrap.appendChild(btn);
  wrap.appendChild(popover);

  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(wrap, hint || null);

  btn.addEventListener('click', function (e) {
    e.stopPropagation();
    var open = !popover.hasAttribute('hidden');
    if (open) {
      popover.setAttribute('hidden', '');
      btn.setAttribute('aria-expanded', 'false');
    } else {
      popover.removeAttribute('hidden');
      btn.setAttribute('aria-expanded', 'true');
    }
  });

  document.addEventListener('click', function (e) {
    if (!wrap.contains(e.target)) {
      popover.setAttribute('hidden', '');
      btn.setAttribute('aria-expanded', 'false');
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !popover.hasAttribute('hidden')) {
      popover.setAttribute('hidden', '');
      btn.setAttribute('aria-expanded', 'false');
    }
  });
}

function _getViewPopover() {
  return document.getElementById('reader-view-popover');
}

// ── initSplitToggle ───────────────────────────────────────────────────────
export function initSplitToggle() {
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
  var popover = _getViewPopover();
  if (popover) {
    popover.appendChild(btn);
  } else {
    var interlinearBtn = document.getElementById('reader-interlinear-btn');
    var compareBtn     = document.getElementById('reader-compare-btn');
    var parallelsBtn   = document.getElementById('reader-parallels-btn');
    var hint           = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, interlinearBtn || compareBtn || parallelsBtn || hint || null);
  }
  btn.addEventListener('click', function () {
    on = !on;
    if (on) {
      localStorage.setItem(SPLIT_KEY, '1');
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

// ── initFontSizeControls ──────────────────────────────────────────────────
export function initFontSizeControls() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-font-size-grp')) return;
  var FONT_KEY = 'bsw_fontsize';
  var SIZES    = ['sm', 'md', 'lg', 'xl'];
  var LABELS   = { sm: 'A−', md: 'A', lg: 'A+', xl: 'A++' };
  var saved    = localStorage.getItem(FONT_KEY) || 'md';
  SIZES.forEach(function (s) { document.body.classList.remove('bsw-font-' + s); });
  document.body.classList.add('bsw-font-' + saved);
  var grp = document.createElement('div');
  grp.id        = 'reader-font-size-grp';
  grp.className = 'reader-font-size-grp';
  grp.setAttribute('aria-label', 'Font size');
  SIZES.forEach(function (size) {
    var b = document.createElement('button');
    b.className    = 'reader-font-size-btn' + (size === saved ? ' reader-font-size-btn--active' : '');
    b.dataset.size = size;
    b.title        = 'Font size: ' + size.toUpperCase();
    b.textContent  = LABELS[size];
    b.addEventListener('click', function () {
      SIZES.forEach(function (s) { document.body.classList.remove('bsw-font-' + s); });
      document.body.classList.add('bsw-font-' + size);
      localStorage.setItem(FONT_KEY, size);
      grp.querySelectorAll('.reader-font-size-btn').forEach(function (x) {
        x.classList.toggle('reader-font-size-btn--active', x.dataset.size === size);
      });
    });
    grp.appendChild(b);
  });
  var popover2 = _getViewPopover();
  if (popover2) {
    popover2.appendChild(grp);
  } else {
    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(grp, hint || null);
  }
}

// ── initWideToggle ────────────────────────────────────────────────────────
export function initWideToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-wide-btn')) return;
  var layout = document.querySelector('.reader-layout');
  var on = !!localStorage.getItem(WIDE_KEY);
  if (on && layout) layout.classList.add('reader-layout--wide');
  var btn = document.createElement('button');
  btn.id        = 'reader-wide-btn';
  btn.className = 'reader-wide-btn' + (on ? ' reader-wide-btn--on' : '');
  btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  btn.title     = 'Wide layout';
  btn.textContent = '⇿ Wide';
  var popoverW = _getViewPopover();
  if (popoverW) {
    popoverW.appendChild(btn);
  } else {
    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, hint || null);
  }
  btn.addEventListener('click', function () {
    on = !on;
    if (on) localStorage.setItem(WIDE_KEY, '1');
    else    localStorage.removeItem(WIDE_KEY);
    if (layout) layout.classList.toggle('reader-layout--wide', on);
    btn.classList.toggle('reader-wide-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  });
}

// ── initSidebarToggle ─────────────────────────────────────────────────────
export function initSidebarToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-sidebar-btn')) return;
  var sidebar = document.querySelector('.reader-sidebar');
  if (!sidebar) return;
  var on = !!localStorage.getItem(SIDEBAR_KEY);
  // CSS activates the sidebar column via a class on the layout, not the sidebar itself.
  var layout = document.querySelector('.reader-layout');
  if (on && layout) layout.classList.add('reader-layout--with-sidebar');
  var btn = document.createElement('button');
  btn.id        = 'reader-sidebar-btn';
  btn.className = 'reader-sidebar-btn' + (on ? ' reader-sidebar-btn--on' : '');
  btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  btn.title     = 'Chapter list sidebar';
  btn.textContent = '☰ Chapters';
  var popoverS = _getViewPopover();
  if (popoverS) {
    popoverS.appendChild(btn);
  } else {
    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, hint || null);
  }
  btn.addEventListener('click', function () {
    on = !on;
    if (on) {
      localStorage.setItem(SIDEBAR_KEY, '1');
      // Populate the sidebar immediately if it has no chapter grid yet.
      // This covers the case where the button was toggled after a passage loaded
      // but renderReaderSidebar's async loadBook().then() hadn't resolved yet,
      // or the user toggled the sidebar before any lookup.
      var sidebarEl = document.querySelector('.reader-sidebar');
      var state     = window._readerNavState;
      if (sidebarEl && !sidebarEl.querySelector('.reader-sidebar__grid') &&
          state && state.bookId && typeof window._renderSidebarFn === 'function') {
        loadBook(getVersion(), state.bookId).then(function (chapters) {
          if (chapters) window._renderSidebarFn(state.bookId, chapters, state.ch || 0);
        }).catch(function () {});
      }
    } else {
      localStorage.removeItem(SIDEBAR_KEY);
    }
    if (layout) layout.classList.toggle('reader-layout--with-sidebar', on);
    btn.classList.toggle('reader-sidebar-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  });
}

// ── injectAllInterlinearRows ──────────────────────────────────────────────
export function injectAllInterlinearRows(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-verse[data-book][data-ch][data-v]').forEach(function (verseEl) {
    _injectInterlinearForVerse(verseEl);
  });
}

function _injectInterlinearForVerse(verseEl) {
  if (verseEl.nextElementSibling && verseEl.nextElementSibling.classList.contains('reader-interlinear-row')) return;
  var bookName = verseEl.getAttribute('data-book');
  var ch       = parseInt(verseEl.getAttribute('data-ch'), 10);
  var v        = parseInt(verseEl.getAttribute('data-v'), 10);
  var bk = metaBooks && metaBooks.find(function (b) { return b.name === bookName || b.id === bookName; });
  if (!bk) return;

  var row = document.createElement('div');
  row.className = 'reader-interlinear-row';
  row.innerHTML = '<p class="reader-hint">Loading interlinear…</p>';
  verseEl.parentNode.insertBefore(row, verseEl.nextSibling);

  loadInterlinear(bk.id).then(function (data) {
    if (!data) { row.innerHTML = '<p class="reader-hint">No interlinear data for this book.</p>'; return; }
    var chData = data[String(ch)];
    if (!chData) { row.innerHTML = ''; return; }
    var vData  = chData[String(v)];
    if (!vData || !vData.length) { row.innerHTML = ''; return; }
    renderReaderInterlinearRow(row, vData, bk.id);
  }).catch(function () { row.innerHTML = ''; });
}

export function renderReaderInterlinearRow(container, tokens, bookId) {
  var isNT  = _isNTBook(bookId);
  var lang  = isNT ? 'greek' : 'hebrew';
  loadStrongs(lang).then(function (strongsDict) {
    // ri-grid--rtl reverses word order for Hebrew (OT books).
    var html = '<div class="ri-grid' + (!isNT ? ' ri-grid--rtl' : '') + '">';
    tokens.forEach(function (tok) {
      // tok fields: s (Strong's key), text (contextual English). Lemma/translit come from the dict entry.
      var entry = strongsDict && tok.s && strongsDict[tok.s];
      html += '<span class="ri-tile" data-strongs="' + escHtml(tok.s || '') + '">' +
        '<span class="ri-tile__lemma">' + escHtml((entry && entry.lemma) || '') + '</span>' +
        '<span class="ri-tile__translit">' + escHtml((entry && entry.translit) || '') + '</span>' +
        '<span class="ri-tile__eng">' + escHtml(tok.text || (entry && entry.gloss) || '') + '</span>' +
        (tok.s ? '<span class="ri-tile__s">' + escHtml(tok.s) + '</span>' : '') +
      '</span>';
    });
    html += '</div>';
    container.innerHTML = html;

    container.querySelectorAll('.ri-tile').forEach(function (tile) {
      tile.addEventListener('click', function (e) {
        e.stopPropagation();  // prevents bubble to document outside-click listener
        _riShowPopover(tile, strongsDict);
      });
    });
  }).catch(function () {
    container.innerHTML = '<p class="reader-hint">Could not load Strong\'s data.</p>';
  });
}

function _isNTBook(bookId) {
  var NT_FIRST = 'matthew';
  if (!metaBooks || !bookOrder) return false;
  var idx = bookOrder[bookId];
  var ntIdx = bookOrder[NT_FIRST] || bookOrder['mat'];
  return idx >= ntIdx;
}

function _riShowPopover(tile, strongsDict) {
  // INTENT: Renders a lexicon card for the clicked tile's Strong's entry; positions it
  //   within viewport bounds (fixed element — scroll offsets must NOT be added to
  //   getBoundingClientRect coords); closes on scroll so it never floats adrift.
  // CHANGE? POP_W (280) must match .ri-popover width in reader.css (line 2022).
  //   WORD_URL is imported from core.js; if the word/ path changes, update core.js line 45.
  //   _riScrollCleanup is module-level — if you add new close triggers (e.g. Escape),
  //   call _riScrollCleanup() and null it before removing the popover.
  // VERIFY: Click a tile near the right edge → popover stays fully within viewport.
  //   Click a tile near the bottom → popover flips above the tile.
  //   Open popover; scroll the reader → popover disappears immediately.
  //   Popover shows "Word Study →" link navigating to word/?s=G3056 (or correct code).
  var strongs = tile.getAttribute('data-strongs');
  if (!strongs) return;
  var entry = strongsDict && strongsDict[strongs];
  if (!entry) return;

  // Tear down any existing popover and its scroll listener
  if (_riScrollCleanup)  { _riScrollCleanup(); _riScrollCleanup = null; }
  if (_riActiveTile)     { _riActiveTile.classList.remove('ri-tile--active'); }
  if (_riPopoverEl)      { _riPopoverEl.remove(); _riPopoverEl = null; }

  var pop = document.createElement('div');
  pop.className = 'ri-popover';
  pop.innerHTML =
    '<button class="ri-popover__close" type="button" aria-label="Close">&#x2715;</button>' +
    '<div class="ri-popover__header">' +
      (entry.gloss ? '<span class="ri-popover__eng">' + escHtml(entry.gloss) + '</span>' : '') +
      '<span class="ri-popover__s">' + escHtml(strongs) + '</span>' +
    '</div>' +
    '<div class="ri-popover__orig">' +
      '<span class="ri-popover__lemma">' + escHtml(entry.lemma || '') + '</span>' +
      (entry.translit ? '<span class="ri-popover__translit">' + escHtml(entry.translit) + '</span>' : '') +
    '</div>' +
    (entry.def   ? '<p class="ri-popover__def">'   + escHtml(entry.def)   + '</p>' : '') +
    (entry.deriv ? '<p class="ri-popover__deriv">' + escHtml(entry.deriv) + '</p>' : '') +
    '<div class="ri-popover__links">' +
      '<a class="vs-context-btn" href="' + escHtml(WORD_URL + '?s=' + encodeURIComponent(strongs)) + '" ' +
         'title="Open full word study">Word Study →</a>' +
    '</div>';

  document.body.appendChild(pop);
  _riPopoverEl  = pop;
  _riActiveTile = tile;
  tile.classList.add('ri-tile--active');

  // RI-A: Viewport-clamped position — fixed element uses viewport coords, no scroll offset
  var POP_W = 280, POP_MARGIN = 8;
  var r = tile.getBoundingClientRect();
  pop.style.left = Math.min(
    Math.max(POP_MARGIN, r.left),
    window.innerWidth - POP_W - POP_MARGIN
  ) + 'px';
  pop.style.top = (r.bottom + 4) + 'px';
  // Flip above tile if popover would overflow the bottom edge
  requestAnimationFrame(function () {
    if (!_riPopoverEl) return;
    var popH = pop.offsetHeight;
    if (r.bottom + 4 + popH > window.innerHeight - POP_MARGIN) {
      pop.style.top = Math.max(POP_MARGIN, r.top - popH - 4) + 'px';
    }
  });

  // RI-B: Close on scroll — fixed popover can't track the tile as the reader scrolls
  var scrollTarget = document.querySelector('.reader-content') ||
                     document.getElementById('reader-results') ||
                     window;
  var _scrollClose = function () {
    scrollTarget.removeEventListener('scroll', _scrollClose);
    _riScrollCleanup = null;
    if (_riActiveTile) { _riActiveTile.classList.remove('ri-tile--active'); _riActiveTile = null; }
    if (_riPopoverEl)  { _riPopoverEl.remove(); _riPopoverEl = null; }
  };
  _riScrollCleanup = function () { scrollTarget.removeEventListener('scroll', _scrollClose); };
  scrollTarget.addEventListener('scroll', _scrollClose, { passive: true });

  pop.querySelector('.ri-popover__close').addEventListener('click', function () {
    if (_riScrollCleanup) { _riScrollCleanup(); _riScrollCleanup = null; }
    tile.classList.remove('ri-tile--active');
    _riActiveTile = null;
    pop.remove();
    _riPopoverEl = null;
  });

  // Safe direct listener: tile click uses e.stopPropagation(), so this won't fire
  // for the same click that opened the popover (no setTimeout race needed).
  document.addEventListener('click', function _outside(e) {
    if (!pop.contains(e.target)) {
      document.removeEventListener('click', _outside);
      if (_riScrollCleanup) { _riScrollCleanup(); _riScrollCleanup = null; }
      if (_riActiveTile) { _riActiveTile.classList.remove('ri-tile--active'); _riActiveTile = null; }
      pop.remove();
      _riPopoverEl = null;
    }
  });
}

// ── expandMorphCode (exposed for verse-study.js) ──────────────────────────
export function expandMorphCode(code) {
  if (!code) return '';
  // Simple expansion — full morphology parsing would be very large
  return code;
}
