/* parallels.js — Parallel passage reader (P1/P2/P3 types) */
'use strict';

import {
  PARALLELS_ROOT, READER_URL, getVersion, loadBook, parseRef, escHtml,
  metaBooks, parallelsCache
} from './core.js';
import { wireRefLinks } from './wire.js';

export var PARALLELS_STORAGE_KEY = 'bsw_parallels';
export var PARALLEL_VERSE_WINDOW = 3;

export function getParallelsEnabled() {
  return localStorage.getItem(PARALLELS_STORAGE_KEY) === '1';
}
export function setParallelsEnabled(on) {
  localStorage.setItem(PARALLELS_STORAGE_KEY, on ? '1' : '0');
}

// INTENT: Fetch parallel-passage data for a book once, caching the result
//   (including null on 404/error) so subsequent calls return immediately without
//   re-fetching. Null cache is intentional — books with no parallel data should
//   not retry on every verse render.
// CHANGE? parallelsCache is imported from core.js and keyed by bookId; if its
//   key schema changes (e.g. to `${version}/${bookId}`), update this cache write
//   and injectParallelPanels' cache-hit check.
// VERIFY: Open reader, enable parallels, navigate two chapters of the same book —
//   Network tab should show exactly one fetch for that book's parallels JSON.
export function loadParallels(bookId) {
  if (parallelsCache[bookId] !== undefined) return Promise.resolve(parallelsCache[bookId]);
  var url = PARALLELS_ROOT + '/' + bookId + '.json';
  return fetch(url)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { parallelsCache[bookId] = d; return d; })
    .catch(function () { parallelsCache[bookId] = null; return null; });
}

// INTENT: Insert the "⇉ Parallels" toggle button into the reader browse bar and
//   wire its click handler; restores prior on/off state from localStorage. This
//   function bootstraps the entire parallels subsystem — calling it is required
//   before any parallel panels can render.
// CHANGE? The click handler drives a 4-function cascade: applyParallelPagination
//   + injectAllParallelPanels (on) or removeAllParallelPanels + removeParallelPagination
//   (off). Also updates PARALLELS_STORAGE_KEY in localStorage; if the key name
//   changes, update getParallelsEnabled/setParallelsEnabled too.
// VERIFY: Open /read/, confirm "⇉ Parallels" button appears; toggle it on/off
//   and verify parallel panels appear/disappear; reload page and confirm the
//   on/off state is restored from localStorage.
export function initParallelToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-parallels-btn')) return;

  var on  = getParallelsEnabled();
  var btn = document.createElement('button');
  btn.id        = 'reader-parallels-btn';
  btn.className = 'reader-parallels-btn' + (on ? ' reader-parallels-btn--on' : '');
  btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  btn.title     = 'Show parallel passages';
  btn.textContent = '⇉ Parallels';

  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);

  btn.addEventListener('click', function () {
    on = !on;
    setParallelsEnabled(on);
    btn.classList.toggle('reader-parallels-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    var resultsEl = document.getElementById('reader-results');
    if (resultsEl) {
      if (on) {
        applyParallelPagination(resultsEl);
        injectAllParallelPanels(resultsEl);
      } else {
        removeAllParallelPanels(resultsEl);
        removeParallelPagination(resultsEl);
      }
    }
  });
}

export function injectAllParallelPanels(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-result-group').forEach(function (groupEl) {
    var parsed = _groupParsedRef(groupEl);
    if (parsed) injectParallelPanels(groupEl, parsed);
  });
}

export function removeAllParallelPanels(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-parallels-container').forEach(function (el) { el.remove(); });
}

export function injectParallelPanels(groupEl, parsed) {
  if (!parsed || !parsed.bookId) return;
  if (groupEl.querySelector('.reader-parallels-container')) return;
  loadParallels(parsed.bookId).then(function (data) {
    if (!data) return;
    var chData = data[String(parsed.ch)];
    if (!chData) return;
    var startV = parsed.v || 1;
    var endV   = parsed.endV || startV;
    var sets   = [];
    // Iterate actual verse keys to avoid a 9999-iteration loop when endV is a sentinel.
    Object.keys(chData).map(Number).sort(function (a, b) { return a - b; }).forEach(function (v) {
      if (v >= startV && (endV >= 9999 || v <= endV)) {
        // Each verse entry is [{type, label, refs:[{passage,label}]}], not a flat string array.
        sets.push({ v: v, groups: chData[String(v)] });
      }
    });
    if (!sets.length) return;
    buildParallelPanel(groupEl, parsed, sets);
  }).catch(function () {});
}

// INTENT: Build and inject the parallel-passage panel DOM for a reader verse
//   group, including badge, label, "Read →" link, and collapse button for each
//   parallel ref. Calls wireRefLinks(container) for hover-preview/modal wiring.
// CHANGE? wireRefLinks is imported from wire.js; if that function's signature or
//   expected container structure changes, this call will silently mis-wire refs.
//   Also: BADGE_TYPE_MAP and BADGE_PHRASE_MAP here must stay in sync with parallel
//   data schema (data/crossrefs/*.json type field values).
// VERIFY: Enable parallels on a cross-referenced passage (e.g. Matthew 5:3) —
//   panel renders with correct badge colours and hovering a ref shows the verse
//   preview tooltip.
export function buildParallelPanel(groupEl, parsed, sets) {
  var container = document.createElement('div');
  container.className = 'reader-parallels-container';

  // Map type → CSS badge modifier (controls colour). Source-variants share the same colour family.
  var BADGE_TYPE_MAP = {
    'parallel':         'parallel',
    'fulfillment':      'fulfillment',
    'prophecy-source':  'prophecy',
    'quotation':        'quotation',
    'quotation-source': 'quotation',
    'allusion':         'allusion',
    'allusion-source':  'allusion',
  };
  // Human-readable connection phrase shown in the badge — reads as a verb toward the linked ref.
  var BADGE_PHRASE_MAP = {
    'parallel':         'Parallel',
    'fulfillment':      'Fulfilled in',
    'prophecy-source':  'Fulfills',
    'quotation':        'Quotes',
    'quotation-source': 'Quoted in',
    'allusion':         'Alludes to',
    'allusion-source':  'Referenced in',
  };

  sets.forEach(function (s) {
    // Each verse entry is an array of group objects: [{type, label, refs:[{passage,label}]}]
    var groups = Array.isArray(s.groups) ? s.groups : [];
    groups.forEach(function (group) {
      var groupType = group.type || 'parallel';
      var badgeMod  = BADGE_TYPE_MAP[groupType] || 'parallel';
      var groupRefs = Array.isArray(group.refs) ? group.refs : [];

      groupRefs.forEach(function (refObj) {
        var passage = refObj.passage;
        if (!passage) return;

        var section = document.createElement('div');
        section.className = 'reader-parallel-section';
        section.setAttribute('data-parallel-type', groupType);

        var header = document.createElement('div');
        header.className = 'reader-parallel-header';

        var badge = document.createElement('span');
        badge.className = 'reader-parallel-badge reader-parallel-badge--' + badgeMod;
        badge.textContent = BADGE_PHRASE_MAP[groupType] || groupType.charAt(0).toUpperCase() + groupType.slice(1);

        // The label carries data-ref so wireRefLinks wires it for hover-preview/modal.
        var refLabel = document.createElement('span');
        refLabel.className = 'reader-parallel-ref-label';
        refLabel.setAttribute('data-ref', passage);
        refLabel.setAttribute('role', 'button');
        refLabel.setAttribute('tabindex', '0');
        refLabel.textContent = passage;

        // Read → navigates to the reader page; uses a real href so the browser
        // follows it directly instead of opening the verse modal.
        var readLink = document.createElement('a');
        readLink.className = 'reader-parallel-read-link';
        readLink.href = READER_URL + '?ref=' + encodeURIComponent(passage);
        readLink.textContent = 'Read →';

        var collapseBtn = document.createElement('button');
        collapseBtn.className = 'reader-parallel-collapse';
        collapseBtn.textContent = '−';
        collapseBtn.setAttribute('aria-label', 'Collapse');

        collapseBtn.addEventListener('click', function () {
          var collapsed = section.classList.toggle('reader-parallel-section--collapsed');
          collapseBtn.textContent = collapsed ? '+' : '−';
          collapseBtn.setAttribute('aria-label', collapsed ? 'Expand' : 'Collapse');
        });

        header.appendChild(badge);
        header.appendChild(refLabel);
        header.appendChild(readLink);
        header.appendChild(collapseBtn);

        var body = document.createElement('div');
        body.className = 'reader-parallel-body';
        body.innerHTML = '<p class="reader-parallel-loading">Loading…</p>';

        section.appendChild(header);
        section.appendChild(body);
        container.appendChild(section);

        loadParallelText(passage, getVersion(), body);
      });
    });
  });

  if (!container.children.length) return;
  wireRefLinks(container);

  var bottomNav = groupEl.querySelector('.reader-chapter-nav--bottom');
  if (bottomNav) groupEl.insertBefore(container, bottomNav);
  else groupEl.appendChild(container);
}

var PARALLEL_PAGE_SIZE = 5;

// INTENT: Fetch the target passage text for a parallel panel body and render it
//   with optional pagination when the verse range exceeds PARALLEL_PAGE_SIZE (5).
//   Pagination buttons re-call this function with an updated page arg; they do
//   not re-fetch — loadBook() caches the full chapter.
// CHANGE? PARALLEL_PAGE_SIZE (line ~197) controls items per page; pager buttons
//   use data-page attribute which this function reads back. If loadBook's return
//   shape changes (currently {chapter: {verse: text}}), update the ch/verse
//   access at line ~208 here.
// VERIFY: Enable parallels on Psalm 119 — a long parallel should show a pager;
//   click Next/Prev and verify verse text changes without a new network request
//   (chapter JSON is already cached by loadBook).
export function loadParallelText(ref, version, container, page) {
  page = page || 0;
  var parsed = parseRef(ref);
  if (!parsed) { container.innerHTML = ''; return; }
  loadBook(version, parsed.bookId).then(function (chapters) {
    if (!chapters) {
      container.innerHTML = '<p class="reader-parallel-empty">Not available.</p>';
      return;
    }
    var ch     = chapters[String(parsed.ch)];
    var startV = parseInt(parsed.v, 10);
    var endV   = parsed.endV ? parseInt(parsed.endV, 10) : startV;

    var allVerses = ch
      ? Object.keys(ch).map(Number)
          .filter(function (n) { return n >= startV && n <= endV; })
          .sort(function (a, b) { return a - b; })
      : [];

    var totalPages = Math.max(1, Math.ceil(allVerses.length / PARALLEL_PAGE_SIZE));
    page = Math.max(0, Math.min(page, totalPages - 1));
    var pageVerses = allVerses.slice(page * PARALLEL_PAGE_SIZE, (page + 1) * PARALLEL_PAGE_SIZE);

    var parts = pageVerses.map(function (vNum) {
      return '<sup class="reader-verse__num">' + vNum + '</sup>' + escHtml(ch[String(vNum)]);
    });

    var textHtml = parts.length
      ? '<p class="reader-parallel-text">' + parts.join(' ') + '</p>'
      : '<p class="reader-parallel-empty">Not available in this version.</p>';

    var navHtml = '';
    if (totalPages > 1 && pageVerses.length) {
      var firstV = pageVerses[0];
      var lastV  = pageVerses[pageVerses.length - 1];
      var info   = 'vv. ' + firstV + (lastV !== firstV ? '–' + lastV : '');
      navHtml = '<div class="reader-parallel-pager">' +
        (page > 0
          ? '<button class="reader-parallel-pager__btn" data-page="' + (page - 1) + '">← Prev</button>'
          : '<span class="reader-parallel-pager__spacer"></span>') +
        '<span class="reader-parallel-pager__info">' + info + '</span>' +
        (page < totalPages - 1
          ? '<button class="reader-parallel-pager__btn" data-page="' + (page + 1) + '">Next →</button>'
          : '<span class="reader-parallel-pager__spacer"></span>') +
        '</div>';
    }

    container.innerHTML = textHtml + navHtml;

    container.querySelectorAll('.reader-parallel-pager__btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        loadParallelText(ref, version, container, parseInt(btn.getAttribute('data-page'), 10));
      });
    });
  }).catch(function () {
    container.innerHTML = '<p class="reader-parallel-empty">Could not load.</p>';
  });
}

// Returns the verse range of currently *visible* verses in the group.
// When verse pagination is active (display:none on hidden verses), this narrows
// the parallel lookup to only the shown verses instead of the whole chapter.
function _groupParsedRef(groupEl) {
  var all     = Array.from(groupEl.querySelectorAll('.reader-verse[data-book][data-ch]'));
  var visible = all.filter(function (v) { return v.style.display !== 'none'; });
  var pool    = visible.length ? visible : all;
  if (!pool.length) return null;
  var firstEl  = pool[0];
  var lastEl   = pool[pool.length - 1];
  var bookName = firstEl.getAttribute('data-book');
  var ch       = parseInt(firstEl.getAttribute('data-ch'), 10);
  var bk       = metaBooks && metaBooks.find(function (b) { return b.name === bookName || b.id === bookName; });
  if (!bk) return null;
  var startV = parseInt(firstEl.getAttribute('data-v'), 10) || 1;
  var endV   = parseInt(lastEl.getAttribute('data-v'),  10) || startV;
  return { bookId: bk.id, bookName: bk.name, ch: ch, v: startV, endCh: ch, endV: endV, display: bk.name + ' ' + ch };
}

// ── Main-reader verse pagination (active only when parallels is on) ────────

var READER_PAGE_SIZE = 5;

export function applyParallelPagination(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-result-group').forEach(function (groupEl) {
    if (groupEl.querySelector('.reader-parallel-page-nav')) return; // already done
    var verses = Array.from(groupEl.querySelectorAll('.reader-result-group__text > .reader-verse'));
    if (verses.length <= READER_PAGE_SIZE) return; // short enough — no nav needed
    _paginateGroup(groupEl, verses, 0);
  });
}

export function removeParallelPagination(resultsEl) {
  if (!resultsEl) return;
  resultsEl.querySelectorAll('.reader-result-group__text > .reader-verse').forEach(function (v) {
    v.style.display = '';
  });
  resultsEl.querySelectorAll('.reader-parallel-page-nav').forEach(function (el) { el.remove(); });
}

// INTENT: Show/hide individual reader verses via style.display to implement
//   page-by-page navigation within a long chapter group, and re-inject parallel
//   panels for the newly visible verse slice on every page change. The DOM
//   stores page state in data-rpage attributes on nav buttons rather than in JS
//   state, so panel injection always reads the current visible set.
// CHANGE? READER_PAGE_SIZE (line ~279) controls items per page. Re-injection of
//   parallel panels at line ~342 calls injectParallelPanels with a freshly
//   computed _groupParsedRef — if _groupParsedRef's visible-verse detection
//   logic changes, parallels may inject for the wrong verse range. data-rpage
//   attribute name must stay in sync with the nav button click handler below.
// VERIFY: Enable parallels on Psalm 119 (176 verses), navigate to page 2 —
//   only vv. 6–10 should be visible; parallel panels should refresh to match
//   that verse range, not the full chapter.
function _paginateGroup(groupEl, verses, page) {
  var totalPages = Math.ceil(verses.length / READER_PAGE_SIZE);
  page = Math.max(0, Math.min(page, totalPages - 1));
  var pageStart = page * READER_PAGE_SIZE;
  var pageEnd   = Math.min(pageStart + READER_PAGE_SIZE, verses.length);

  // Show/hide verses for this page
  verses.forEach(function (v, i) {
    v.style.display = (i >= pageStart && i < pageEnd) ? '' : 'none';
  });

  // Remove old page-nav and any injected parallel panels (they'll be re-injected)
  var existing = groupEl.querySelector('.reader-parallel-page-nav');
  if (existing) existing.remove();
  groupEl.querySelectorAll('.reader-parallels-container').forEach(function (el) { el.remove(); });

  var firstV = verses[pageStart].getAttribute('data-v');
  var lastV  = verses[pageEnd - 1].getAttribute('data-v');
  var info   = 'vv. ' + firstV + (lastV !== firstV ? '–' + lastV : '');

  var nav = document.createElement('div');
  nav.className = 'reader-parallel-page-nav';
  nav.innerHTML =
    (page > 0
      ? '<button class="reader-parallel-pager__btn" data-rpage="' + (page - 1) + '">← Prev 5</button>'
      : '<span class="reader-parallel-pager__spacer"></span>') +
    '<span class="reader-parallel-pager__info">' + escHtml(info) + ' of ' + verses.length + ' vv.</span>' +
    (page < totalPages - 1
      ? '<button class="reader-parallel-pager__btn" data-rpage="' + (page + 1) + '">Next 5 →</button>'
      : '<span class="reader-parallel-pager__spacer"></span>');

  // Insert right after the verse text paragraph
  var textEl = groupEl.querySelector('.reader-result-group__text');
  if (textEl && textEl.nextSibling) textEl.parentNode.insertBefore(nav, textEl.nextSibling);
  else if (textEl) textEl.parentNode.appendChild(nav);
  else groupEl.appendChild(nav);

  nav.querySelectorAll('[data-rpage]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      _paginateGroup(groupEl, verses, parseInt(btn.getAttribute('data-rpage'), 10));
      // Re-inject parallels for the new visible verse slice
      if (getParallelsEnabled()) {
        var parsed = _groupParsedRef(groupEl);
        if (parsed) injectParallelPanels(groupEl, parsed);
      }
    });
  });
}
