/* interlinear.js — Interlinear view, book-info panel, font/wide/split/sidebar toggles */
'use strict';

import {
  getVersion, loadBook, loadInterlinear, loadStrongs, loadLexicon,
  metaBooks, metaVersions, bookOrder, READER_URL, escHtml, parseRef, _resolve
} from './core.js';
import { wireRefLinks } from './wire.js';

export var INTERLINEAR_KEY = 'bsw_interlinear';
var _riPopoverEl  = null;
var _riActiveTile = null;

var _TL_ERA_LABELS = {
  creation: 'Creation', patriarchs: 'Patriarchs', moses: 'Moses & Exodus',
  conquest: 'Conquest & Judges', monarchy: 'The Monarchy', exile: 'Exile',
  restoration: 'Restoration', intertestamental: 'Intertestamental',
  gospels: 'The Gospels', church: 'The Church', consummation: 'Consummation'
};

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
var _bookInfoOpen  = false;
var _bookInfoCache = {};    // bookId → rich intro JSON from data/books/introductions/

export function initBookInfoToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-bookinfo-btn')) return;

  var btn = document.createElement('button');
  btn.id        = 'reader-bookinfo-btn';
  btn.className = 'reader-bookinfo-btn';
  btn.title     = 'Book information';
  btn.setAttribute('aria-pressed', 'false');
  btn.textContent = 'Book Info';

  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);

  btn.addEventListener('click', function () {
    _bookInfoOpen = !_bookInfoOpen;
    btn.classList.toggle('reader-bookinfo-btn--on', _bookInfoOpen);
    btn.setAttribute('aria-pressed', _bookInfoOpen ? 'true' : 'false');
    _refreshBookInfoPanel(_bookInfoOpen);
  });
}

function _refreshBookInfoPanel(open) {
  var panel = document.getElementById('reader-bookinfo-panel');
  if (!panel) {
    // Panel missing from HTML — create and insert it before the results area.
    panel = document.createElement('div');
    panel.id = 'reader-bookinfo-panel';
    panel.className = 'reader-bookinfo-panel';
    var results = document.getElementById('reader-results');
    if (!results) return;
    results.parentNode.insertBefore(panel, results);
  }
  if (!open) { panel.hidden = true; return; }
  panel.hidden = false;
  var state = window._readerNavState;
  if (!state || !state.bookId) return;
  _renderBookInfoContent(state.bookId, panel);
}

function _renderBookInfoContent(bookId, panel) {
  var bk = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
  if (!bk) { panel.innerHTML = '<p class="reader-hint">No information available.</p>'; return; }

  // Show skeleton from metaBooks while the rich intro JSON loads.
  panel.innerHTML = '<p class="reader-hint">Loading book information…</p>';

  if (_bookInfoCache[bookId]) {
    _renderIntroHtml(panel, bk, _bookInfoCache[bookId]);
    return;
  }

  var url = _resolve('../../data/books/introductions/' + bookId + '.json');
  fetch(url)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (data) {
      _bookInfoCache[bookId] = data || {};
      _renderIntroHtml(panel, bk, _bookInfoCache[bookId]);
    })
    .catch(function () {
      // Fall back to the basic metaBooks fields on fetch failure.
      _renderIntroHtml(panel, bk, {});
    });
}

function _renderIntroHtml(panel, bk, intro) {
  var author   = intro.author   || '';
  var date     = intro.date     || '';
  var purpose  = intro.purpose  || intro.setting || '';
  var themes   = Array.isArray(intro.themes) ? intro.themes : [];
  var keyVerse = intro.key_verse || (intro.key_verses && intro.key_verses[0] && intro.key_verses[0].ref) || '';
  var kvNote   = intro.key_verses && intro.key_verses[0] ? intro.key_verses[0].note || '' : '';

  // Meta row: join non-empty fields with a mid-dot separator
  var metaParts = [];
  if (bk.testament) metaParts.push(escHtml(bk.testament));
  if (author)       metaParts.push(escHtml(author));
  if (date)         metaParts.push(escHtml(date));
  var meta = metaParts.join('<span class="reader-bookinfo-meta-sep"> · </span>');

  var kvHtml = '';
  if (keyVerse) {
    kvHtml = '<div class="reader-bookinfo-keyverse">' +
      '<span class="reader-bookinfo-kv-label">Key Verse</span>' +
      '<a class="reader-bookinfo-kv-ref ref" data-ref="' + escHtml(keyVerse) + '">' + escHtml(keyVerse) + '</a>' +
      (kvNote ? '<span class="reader-bookinfo-kv-note">' + escHtml(kvNote) + '</span>' : '') +
    '</div>';
  }

  var themesHtml = '';
  if (themes.length) {
    themesHtml = '<div class="reader-bookinfo-themes">' +
      themes.map(function (t) {
        return '<span class="reader-bookinfo-theme">' + escHtml(t) + '</span>';
      }).join('') +
    '</div>';
  }

  // Compact 3-item timeline: most-recent before event, current book, first after event
  var tlHtml = '';
  var tl = intro.timeline;
  if (tl) {
    var beforeItem = tl.before && tl.before.length ? tl.before[tl.before.length - 1] : null;
    var afterItem  = tl.after  && tl.after.length  ? tl.after[0]                      : null;
    var eraLabel   = tl.period ? (_TL_ERA_LABELS[tl.period] || tl.period) : '';

    var _tlItem = function (item) {
      if (!item) return '<div class="ri-tl-item ri-tl-item--empty"><div class="ri-tl-dot ri-tl-dot--empty"></div></div>';
      var type  = item.type  || 'event';
      var label = item.label || '';
      var year  = item.year  || '';
      var ref   = item.ref   || '';
      // Add data-ref so the tooltip/modal system can wire hover previews.
      var lbl = ref
        ? '<a class="ref ri-tl-label ri-tl-label--' + escHtml(type) + '" data-ref="' + escHtml(ref) + '">' + escHtml(label) + '</a>'
        : '<span class="ri-tl-label ri-tl-label--' + escHtml(type) + '">' + escHtml(label) + '</span>';
      return '<div class="ri-tl-item">' +
        '<div class="ri-tl-dot ri-tl-dot--' + escHtml(type) + '"></div>' +
        lbl +
        (year ? '<div class="ri-tl-year">' + escHtml(year) + '</div>' : '') +
      '</div>';
    };

    tlHtml =
      '<div class="reader-bookinfo-timeline">' +
      (eraLabel
        ? '<div class="ri-tl-arc-lbl" style="margin-bottom:.45rem">Period: <strong>' + escHtml(eraLabel) + '</strong></div>'
        : '') +
      '<div class="ri-tl-row ri-tl-row--compact">' +
        _tlItem(beforeItem) +
        '<div class="ri-tl-item">' +
          '<div class="ri-tl-dot ri-tl-dot--current"></div>' +
          '<div class="ri-tl-label ri-tl-label--current">' + escHtml(bk.name) + '</div>' +
          (tl.date ? '<div class="ri-tl-year ri-tl-year--current">' + escHtml(tl.date) + '</div>' : '') +
        '</div>' +
        _tlItem(afterItem) +
      '</div>' +
      '</div>';
  }

  panel.innerHTML =
    '<div class="reader-bookinfo-inner">' +
      '<div class="reader-bookinfo-header">' +
        '<h3 class="reader-bookinfo-title">' + escHtml(intro.title || bk.name) + '</h3>' +
      '</div>' +
      (meta ? '<div class="reader-bookinfo-meta">' + meta + '</div>' : '') +
      kvHtml +
      (purpose ? '<p class="reader-bookinfo-purpose">' + escHtml(purpose) + '</p>' : '') +
      themesHtml +
      tlHtml +
    '</div>';

  // Wire all [data-ref] elements in the panel (key verse, timeline items) for
  // hover tooltips and modal. Panel is dynamically created so wireRefLinks is
  // not called automatically — we must call it explicitly here.
  wireRefLinks(panel);
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
  var interlinearBtn = document.getElementById('reader-interlinear-btn');
  var compareBtn     = document.getElementById('reader-compare-btn');
  var parallelsBtn   = document.getElementById('reader-parallels-btn');
  var hint           = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, interlinearBtn || compareBtn || parallelsBtn || hint || null);
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
  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(grp, hint || null);
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
  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);
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
  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);
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
      tile.addEventListener('click', function () {
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
  var strongs = tile.getAttribute('data-strongs');
  if (!strongs) return;
  var entry = strongsDict && strongsDict[strongs];
  if (!entry) return;

  if (_riPopoverEl) _riPopoverEl.remove();
  var pop = document.createElement('div');
  pop.className = 'ri-popover';
  pop.innerHTML =
    '<button class="ri-popover__close" aria-label="Close">&#x2715;</button>' +
    '<div class="ri-popover__header">' +
      (entry.gloss ? '<span class="ri-popover__eng">' + escHtml(entry.gloss) + '</span>' : '') +
      '<span class="ri-popover__s">' + escHtml(strongs) + '</span>' +
    '</div>' +
    '<div class="ri-popover__orig">' +
      '<span class="ri-popover__lemma">' + escHtml(entry.lemma || '') + '</span>' +
      (entry.translit ? '<span class="ri-popover__translit">' + escHtml(entry.translit) + '</span>' : '') +
    '</div>' +
    (entry.def   ? '<p class="ri-popover__def">'   + escHtml(entry.def)   + '</p>' : '') +
    (entry.deriv ? '<p class="ri-popover__deriv">' + escHtml(entry.deriv) + '</p>' : '');
  document.body.appendChild(pop);
  _riPopoverEl  = pop;
  _riActiveTile = tile;

  var r   = tile.getBoundingClientRect();
  pop.style.top  = (r.bottom + window.scrollY + 4) + 'px';
  pop.style.left = Math.max(8, r.left + window.scrollX) + 'px';

  pop.querySelector('.ri-popover__close').addEventListener('click', function () { pop.remove(); _riPopoverEl = null; });
  setTimeout(function () {
    document.addEventListener('click', function _outside(e) {
      if (!pop.contains(e.target) && e.target !== tile) { pop.remove(); _riPopoverEl = null; document.removeEventListener('click', _outside); }
    });
  }, 10);
}

// ── expandMorphCode (exposed for verse-study.js) ──────────────────────────
export function expandMorphCode(code) {
  if (!code) return '';
  // Simple expansion — full morphology parsing would be very large
  return code;
}
