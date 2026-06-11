/* parallels.js — Parallel passage reader (P1/P2/P3 types) */
'use strict';

import {
  PARALLELS_ROOT, READER_URL, getVersion, loadBook, parseRef, escHtml,
  metaBooks, parallelsCache, loadEchoes
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

// TEMPORARY: Merges data/echoes/ into the parallel panel while echoes generation
//   is ongoing. Echoes take precedence over legacy parallels — any verse covered
//   by echoes has its parallels entry suppressed to avoid duplication. Once echoes
//   generation is complete and fully replaces data/parallels/, this merge can be
//   removed and loadParallels can revert to a simple fetch of data/parallels/.
// INTENT: Returns a merged chapter-keyed object suitable for injectParallelPanels.
//   Caches the merged result into parallelsCache so both sources are fetched once.
// VERIFY: Open reader, enable parallels on Jeremiah 1 — should show echo entries
//   (e.g. v.5 → Gal 1:15). Navigate same chapter twice — only one network request.
export function loadParallels(bookId) {
  if (parallelsCache[bookId] !== undefined) return Promise.resolve(parallelsCache[bookId]);

  var parallelsFetch = fetch(PARALLELS_ROOT + '/' + bookId + '.json')
    .then(function (r) { return r.ok ? r.json() : null; })
    .catch(function () { return null; });

  return Promise.all([parallelsFetch, loadEchoes(bookId)]).then(function (results) {
    var parData  = results[0] || {};
    var echoData = results[1] || {};
    var merged   = {};

    // Echoes first: convert to parallels schema and stake claim on their verses
    Object.keys(echoData).forEach(function (ch) {
      merged[ch] = merged[ch] || {};
      Object.keys(echoData[ch]).forEach(function (v) {
        var entries = echoData[ch][v];
        if (!Array.isArray(entries) || !entries.length) return;
        var adapted = entries.filter(function (e) { return e.target; })
                             .map(_adaptEchoEntry);
        if (adapted.length) merged[ch][v] = adapted;
      });
    });

    // Parallels second: only add for verses not already covered by echoes
    Object.keys(parData).forEach(function (ch) {
      Object.keys(parData[ch]).forEach(function (v) {
        if (merged[ch] && merged[ch][v]) return; // echoes suppress this verse
        merged[ch] = merged[ch] || {};
        merged[ch][v] = parData[ch][v];
      });
    });

    var result = Object.keys(merged).length ? merged : null;
    parallelsCache[bookId] = result;
    return result;
  });
}

// Convert echoes schema { type, target, note } to parallels renderer schema
// { type, refs: [{ passage, label }] }.
function _adaptEchoEntry(e) {
  return { type: e.type, refs: [{ passage: e.target, label: e.note || e.target }] };
}

// INTENT: Insert the "⇉ Parallels" toggle button into the reader browse bar and
//   wire its click handler. Activating parallels shows the echoes panel (50/50
//   layout); deactivating removes it. Mutually exclusive with commentary mode —
//   turning parallels ON calls window._readerDeactivateComm (set by reader.js),
//   and turning commentary ON calls window._readerTurnOffParallels (set here).
// CHANGE? Echoes panel layout class is 'reader-layout--echoes' on .reader-layout;
//   panel element is #reader-echoes-panel. If either name changes, update CSS and
//   _activateEchoesLayout/_deactivateEchoesPanel. Also update PARALLELS_STORAGE_KEY
//   in getParallelsEnabled/setParallelsEnabled if key name changes.
// VERIFY: Open /read/, confirm "⇉ Parallels" button appears; toggle ON — reader
//   splits 50/50 and echoes populate; navigate chapters — echoes refresh; toggle
//   OFF — layout returns to normal. Enable Commentary then Parallels — Commentary
//   deactivates automatically (and vice versa).
export function initParallelToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-parallels-btn')) return;

  var on  = getParallelsEnabled();
  var btn = document.createElement('button');
  btn.id        = 'reader-parallels-btn';
  btn.className = 'reader-parallels-btn' + (on ? ' reader-parallels-btn--on' : '');
  btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  btn.title     = 'Show echoes and connections panel';
  btn.textContent = '⇉ Parallels';

  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);

  // Expose so reader.js _activateCommMode can enforce mutual exclusion without
  // a circular import.
  window._readerTurnOffParallels = function () {
    if (!on) return;
    on = false;
    setParallelsEnabled(false);
    btn.classList.remove('reader-parallels-btn--on');
    btn.setAttribute('aria-pressed', 'false');
    _deactivateEchoesPanel();
  };

  // Restore layout if parallels was on before page reload — content will be
  // populated by doLookup via refreshEchoesPanel() when the passage renders.
  if (on) _activateEchoesLayout();

  btn.addEventListener('click', function () {
    on = !on;
    setParallelsEnabled(on);
    btn.classList.toggle('reader-parallels-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    if (on) {
      if (window._readerDeactivateComm) window._readerDeactivateComm();
      _activateEchoesLayout();
      refreshEchoesPanel();
    } else {
      _deactivateEchoesPanel();
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
    // Echo-specific types (TEMPORARY — remove when echoes fully replaces parallels)
    'quote':            'quotation',
    'citation':         'quotation',
    'type':             'type',
    'typology':         'type',
    'shadow':           'shadow',
    'theme':            'theme',
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
    // Echo-specific types (TEMPORARY — remove when echoes fully replaces parallels)
    'quote':            'Quotes',
    'citation':         'Cites',
    'type':             'Prefigures',
    'typology':         'Prefigures',
    'shadow':           'Foreshadows',
    'theme':            'Theme in',
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

  // Hide chapter-break divs that have no visible verse on this page. A break is
  // visible only if its next verse sibling (or verse before the next break) is shown.
  var textEl = groupEl.querySelector('.reader-result-group__text');
  if (textEl) {
    textEl.querySelectorAll('.reader-chapter-break').forEach(function (brk) {
      var next = brk.nextElementSibling;
      while (next && !next.classList.contains('reader-verse') && !next.classList.contains('reader-chapter-break')) {
        next = next.nextElementSibling;
      }
      var hide = !next || next.classList.contains('reader-chapter-break') || next.style.display === 'none';
      brk.style.display = hide ? 'none' : '';
    });
  }

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
      // Sync commentary grid if active (window callback set by reader.js)
      if (window._readerOnPageChange) window._readerOnPageChange(groupEl);
    });
  });
}

// ── Echoes panel (replaces inline parallel panels in the new 50/50 layout) ──

function _activateEchoesLayout() {
  var layout = document.querySelector('.reader-layout');
  if (layout) layout.classList.add('reader-layout--echoes');
  var panel = document.getElementById('reader-echoes-panel');
  if (panel) panel.hidden = false;
}

function _deactivateEchoesPanel() {
  var layout = document.querySelector('.reader-layout');
  if (layout) layout.classList.remove('reader-layout--echoes');
  var panel = document.getElementById('reader-echoes-panel');
  if (panel) { panel.hidden = true; panel.innerHTML = ''; }
  // Remove verse markers added by _markEchoVerses
  var resultsEl = document.getElementById('reader-results');
  if (resultsEl) {
    resultsEl.querySelectorAll('.reader-verse--has-echo, .reader-verse--echo-hover').forEach(function (v) {
      v.classList.remove('reader-verse--has-echo', 'reader-verse--echo-hover');
    });
  }
}

// Map echo type → badge CSS modifier (controls colour).
var _ECHO_BADGE_CLASS = {
  'quote': 'quotation', 'citation': 'quotation', 'quotation': 'quotation', 'quotation-source': 'quotation',
  'allusion': 'allusion', 'allusion-source': 'allusion',
  'fulfillment': 'fulfillment', 'prophecy-source': 'fulfillment',
  'type': 'type', 'typology': 'type',
  'shadow': 'shadow',
  'theme': 'theme',
  'parallel': 'parallel',
};
// Human-readable verb phrase shown in the badge.
var _ECHO_BADGE_LABEL = {
  'quote': 'Quotes', 'citation': 'Cites', 'quotation': 'Quotes', 'quotation-source': 'Cited in',
  'allusion': 'Alludes to', 'allusion-source': 'Cited in',
  'fulfillment': 'Fulfilled in', 'prophecy-source': 'Fulfills',
  'type': 'Prefigures', 'typology': 'Prefigures',
  'shadow': 'Foreshadows',
  'theme': 'Theme in',
  'parallel': 'Parallel',
};

// INTENT: Populate the echoes panel for the currently-rendered passage. Reads
//   window._readerGroups to know which (bookId, ch) pairs are on screen, fetches
//   echoes for each via loadEchoes (cached), then builds expandable echo cards.
//   Called from reader.js doLookup on every navigation and from initParallelToggle
//   when the user turns parallels on mid-session.
// CHANGE? Depends on window._readerGroups (array of { ref: {bookId, ch} }) being
//   kept up-to-date by reader.js doLookup. Also depends on #reader-echoes-panel
//   element in read/index.html and .reader-layout--echoes class in reader.css.
//   If loadEchoes signature changes, update the Promise.all call below.
// VERIFY: Enable Parallels on Romans 8 — echoes panel should list all echo entries
//   for that chapter with v. numbers, badge labels, and target refs. Navigate to
//   Romans 9 — panel should refresh without manual toggle. Hover a card — matching
//   verse in main text gets a blue left border. Hover the verse — card highlights.
export function refreshEchoesPanel() {
  if (!getParallelsEnabled()) return;
  var panel = document.getElementById('reader-echoes-panel');
  if (!panel) return;

  var groups = window._readerGroups;
  if (!groups || !groups.length) return;

  panel.innerHTML = '<p class="reader-echo-panel__loading">Loading echoes…</p>';

  // Collect unique chapters per bookId from the current rendered groups.
  // Handle multi-chapter refs (e.g. "John 1-3": ch=1, endCh=3) by expanding
  // the chapter range so echoes from all rendered chapters are included.
  var bookChMap = Object.create(null);
  groups.forEach(function (g) {
    var ref = g && g.ref;
    if (!ref || !ref.bookId) return;
    if (!bookChMap[ref.bookId]) bookChMap[ref.bookId] = [];
    var startCh = ref.ch || 1;
    var endCh   = ref.endCh ? Math.min(ref.endCh, startCh + 29) : startCh; // cap at 30 chapters
    for (var c = startCh; c <= endCh; c++) {
      if (bookChMap[ref.bookId].indexOf(c) === -1) bookChMap[ref.bookId].push(c);
    }
  });

  var bookIds = Object.keys(bookChMap);
  if (!bookIds.length) { panel.innerHTML = ''; return; }

  Promise.all(bookIds.map(function (bookId) {
    return loadEchoes(bookId).then(function (data) { return { bookId: bookId, data: data }; });
  })).then(function (results) {
    _buildEchoesPanel(panel, results, bookChMap, groups);
  }).catch(function () {
    panel.innerHTML = '<p class="reader-echo-panel__empty">Could not load echoes.</p>';
  });
}

function _buildEchoesPanel(panel, results, bookChMap, groups) {
  // Flatten all echo entries, sorted by chapter then verse for reading order.
  var allEntries = [];
  results.forEach(function (r) {
    var echoData = r.data;
    if (!echoData) return;
    (bookChMap[r.bookId] || []).forEach(function (ch) {
      var chData = echoData[String(ch)];
      if (!chData) return;
      Object.keys(chData).forEach(function (v) {
        var entries = chData[v];
        if (!Array.isArray(entries)) return;
        entries.forEach(function (entry) {
          if (!entry.target) return;
          allEntries.push({ v: parseInt(v, 10), ch: ch, bookId: r.bookId, entry: entry });
        });
      });
    });
  });
  allEntries.sort(function (a, b) { return a.ch !== b.ch ? a.ch - b.ch : a.v - b.v; });

  // Build panel DOM via a document fragment to avoid multiple reflows.
  var wrapper = document.createElement('div');
  wrapper.className = 'reader-echo-panel';

  var hdr = document.createElement('div');
  hdr.className = 'reader-echo-panel__header';
  var passageLabel = groups[0] && groups[0].ref ? (groups[0].ref.display || '') : '';
  hdr.innerHTML =
    '<span class="reader-echo-panel__title">Echoes &amp; Connections</span>' +
    (passageLabel ? '<span class="reader-echo-panel__ref">' + escHtml(passageLabel) + '</span>' : '') +
    '<span class="reader-echo-panel__count">' + allEntries.length + ' connection' + (allEntries.length !== 1 ? 's' : '') + '</span>';
  wrapper.appendChild(hdr);

  if (!allEntries.length) {
    var empty = document.createElement('p');
    empty.className = 'reader-echo-panel__empty';
    empty.textContent = 'No echoes found for this passage.';
    wrapper.appendChild(empty);
  } else {
    var list = document.createElement('div');
    list.className = 'reader-echo-panel__list';

    allEntries.forEach(function (item, idx) {
      var entry  = item.entry;
      var type   = entry.type || 'allusion';
      var bClass = _ECHO_BADGE_CLASS[type] || 'allusion';
      var bLabel = _ECHO_BADGE_LABEL[type] || type;
      var note   = entry.note   || '';
      var target = entry.target || '';
      var bodyId = 'echo-body-' + idx;

      var card = document.createElement('div');
      card.className = 'reader-echo-card';
      card.setAttribute('data-echo-v',  String(item.v));
      card.setAttribute('data-echo-ch', String(item.ch));

      var toggle = document.createElement('button');
      toggle.className = 'reader-echo-card__toggle';
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-controls', bodyId);
      toggle.innerHTML =
        '<span class="reader-echo-card__v">v.' + item.v + '</span>' +
        '<span class="reader-echo-card__badge reader-echo-card__badge--' + escHtml(bClass) + '">' + escHtml(bLabel) + '</span>' +
        '<span class="reader-echo-card__target" title="' + escHtml(target) + '">' + escHtml(target) + '</span>' +
        '<span class="reader-echo-card__chevron" aria-hidden="true">&#9654;</span>';

      var body = document.createElement('div');
      body.className = 'reader-echo-card__body';
      body.id = bodyId;
      body.hidden = true;

      // Verse text block — fetched lazily on first expand via loadParallelText
      var verseBlock = document.createElement('div');
      verseBlock.className = 'reader-echo-card__verse';
      body.appendChild(verseBlock);

      if (note) {
        var noteEl = document.createElement('p');
        noteEl.className = 'reader-echo-card__note';
        noteEl.textContent = note;
        body.appendChild(noteEl);
      }
      var readLink = document.createElement('a');
      readLink.className = 'reader-echo-card__read';
      readLink.href = READER_URL + '?ref=' + encodeURIComponent(target);
      readLink.textContent = 'Read ' + target + ' →';
      body.appendChild(readLink);

      // Expand/collapse; load verse text once on first expansion
      var textLoaded = false;
      toggle.addEventListener('click', function () {
        var expanded = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', !expanded ? 'true' : 'false');
        body.hidden = expanded;
        card.classList.toggle('reader-echo-card--expanded', !expanded);
        if (!expanded && !textLoaded) {
          textLoaded = true;
          loadParallelText(target, getVersion(), verseBlock);
        }
      });

      card.appendChild(toggle);
      card.appendChild(body);
      list.appendChild(card);
    });

    wrapper.appendChild(list);
  }

  panel.innerHTML = '';
  panel.appendChild(wrapper);

  _wireEchoHovers(panel, allEntries);
  _markEchoVerses(allEntries);
}

// INTENT: Wire bidirectional hover: hovering an echo card highlights the matched
//   verse in the main text; hovering a .reader-verse--has-echo highlights its
//   cards in the panel. Uses class toggles so multiple overlapping echoes all
//   light up at once. Called after _buildEchoesPanel inserts the cards.
// CHANGE? Relies on data-echo-v/data-echo-ch on cards and data-v/data-ch on
//   .reader-verse spans (set by reader.js render loop). If those attributes are
//   renamed, update the querySelectorAll selectors in both hover handlers here.
// VERIFY: Open Romans 8; enable Parallels. Hover an echo card — the corresponding
//   verse in the left column should show a coloured left border/highlight. Hover
//   that verse — the card in the right panel should show a highlight background.
function _wireEchoHovers(panel, allEntries) {
  var resultsEl = document.getElementById('reader-results');
  if (!resultsEl) return;

  // Card → verse
  panel.querySelectorAll('.reader-echo-card').forEach(function (card) {
    var v  = card.getAttribute('data-echo-v');
    var ch = card.getAttribute('data-echo-ch');
    card.addEventListener('mouseenter', function () {
      resultsEl.querySelectorAll('.reader-verse[data-v="' + v + '"][data-ch="' + ch + '"]')
        .forEach(function (verse) { verse.classList.add('reader-verse--echo-hover'); });
    });
    card.addEventListener('mouseleave', function () {
      resultsEl.querySelectorAll('.reader-verse--echo-hover')
        .forEach(function (v) { v.classList.remove('reader-verse--echo-hover'); });
    });
  });

  // Verse → cards
  resultsEl.querySelectorAll('.reader-verse--has-echo').forEach(function (verse) {
    var v  = verse.getAttribute('data-v');
    var ch = verse.getAttribute('data-ch');
    verse.addEventListener('mouseenter', function () {
      panel.querySelectorAll('.reader-echo-card[data-echo-v="' + v + '"][data-echo-ch="' + ch + '"]')
        .forEach(function (card) { card.classList.add('reader-echo-card--highlight'); });
    });
    verse.addEventListener('mouseleave', function () {
      panel.querySelectorAll('.reader-echo-card--highlight')
        .forEach(function (card) { card.classList.remove('reader-echo-card--highlight'); });
    });
  });
}

function _markEchoVerses(allEntries) {
  var resultsEl = document.getElementById('reader-results');
  if (!resultsEl) return;
  // Clear previous markers before re-marking (passage may have changed)
  resultsEl.querySelectorAll('.reader-verse--has-echo')
    .forEach(function (v) { v.classList.remove('reader-verse--has-echo'); });
  allEntries.forEach(function (item) {
    resultsEl.querySelectorAll('.reader-verse[data-v="' + item.v + '"][data-ch="' + item.ch + '"]')
      .forEach(function (verse) { verse.classList.add('reader-verse--has-echo'); });
  });
}
