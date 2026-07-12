/* parallels.js — Echo connections inline in reader text */
'use strict';

import {
  READER_URL, getVersion, loadBook, parseRef, escHtml, loadEchoes
} from './core.js';
import { autoTagTermsWhenReady } from './terms.js';

// ── Echo toggle ──────────────────────────────────────────────────────────────
var _ECHO_KEY = 'bsw_echoes';
export function isEchoEnabled() { return localStorage.getItem(_ECHO_KEY) !== '0'; }
export function setEchoEnabled(on) {
  try { localStorage.setItem(_ECHO_KEY, on ? '1' : '0'); } catch (e) {}
}

// INTENT: Inject the ◉ Parallels button into the reader browse bar.
//   Toggling on/off re-runs markEchoVerses (which clears markers when disabled).
// CHANGE? The button insertion uses .reader-browse-hint as anchor; if that span
//   is removed from read/index.html, the button appends to end of browseBar instead.
// VERIFY: Load any chapter — button appears; click to toggle off — dots vanish;
//   click again — dots re-appear.
export function initEchoToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-echoes-btn')) return;

  var on  = isEchoEnabled();
  var btn = document.createElement('button');
  btn.id        = 'reader-echoes-btn';
  btn.type      = 'button';
  btn.className = 'reader-echoes-btn' + (on ? ' reader-echoes-btn--on' : '');
  btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  btn.title     = 'Show inline echo and connection links next to verses';
  btn.textContent = 'Connections';

  // Prefer the 📖 Study Tools popover (interlinear.js); fall back to inline.
  var stPop = document.getElementById('reader-studytools-popover');
  if (stPop) {
    stPop.appendChild(btn);
  } else {
    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, hint || null);
  }

  btn.addEventListener('click', function () {
    on = !on;
    setEchoEnabled(on);
    btn.classList.toggle('reader-echoes-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    if (on) {
      // Re-run markers for the current passage
      if (typeof window._readerLookupFn === 'function') window._readerLookupFn();
      else markEchoVerses();
    } else {
      // Clear all existing markers without reloading
      var resultsEl = document.getElementById('reader-results');
      if (resultsEl) {
        resultsEl.querySelectorAll('.reader-verse--has-echo')
          .forEach(function (v) { v.classList.remove('reader-verse--has-echo'); });
        resultsEl.querySelectorAll('.reader-echo-marker')
          .forEach(function (m) { m.remove(); });
        resultsEl.querySelectorAll('.reader-echo-inline')
          .forEach(function (b) { b.remove(); });
      }
    }
  });
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

// INTENT: Fetch echoes for the current passage and mark verses with inline dot
//   markers. Called from reader.js doLookup on every navigation. Reads
//   window._readerGroups to know which (bookId, ch) pairs are on screen.
// VERIFY: Navigate to Romans 8 — verses with echoes should show a small dot
//   marker; clicking it expands an inline card with badge, target ref, and
//   verse text. Navigate to another chapter — markers clear and refresh.
export function markEchoVerses() {
  if (!isEchoEnabled()) return;
  var groups = window._readerGroups;
  if (!groups || !groups.length) return;

  var bookChMap = Object.create(null);
  groups.forEach(function (g) {
    var ref = g && g.ref;
    if (!ref || !ref.bookId) return;
    if (!bookChMap[ref.bookId]) bookChMap[ref.bookId] = [];
    var startCh = ref.ch || 1;
    var endCh   = ref.endCh ? Math.min(ref.endCh, startCh + 29) : startCh;
    for (var c = startCh; c <= endCh; c++) {
      if (bookChMap[ref.bookId].indexOf(c) === -1) bookChMap[ref.bookId].push(c);
    }
  });

  var bookIds = Object.keys(bookChMap);
  if (!bookIds.length) return;

  Promise.all(bookIds.map(function (bookId) {
    return loadEchoes(bookId).then(function (data) { return { bookId: bookId, data: data }; });
  })).then(function (results) {
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
    _markEchoVerses(allEntries);
  }).catch(function () {});
}

function _markEchoVerses(allEntries) {
  var resultsEl = document.getElementById('reader-results');
  if (!resultsEl) return;

  // Clear previous markers and inline blocks
  resultsEl.querySelectorAll('.reader-verse--has-echo')
    .forEach(function (v) { v.classList.remove('reader-verse--has-echo'); });
  resultsEl.querySelectorAll('.reader-echo-marker')
    .forEach(function (m) { m.remove(); });
  resultsEl.querySelectorAll('.reader-echo-inline')
    .forEach(function (b) { b.remove(); });

  // Group entries by ch:v so each verse gets one marker showing all its echoes
  var byVerse = Object.create(null);
  allEntries.forEach(function (item) {
    var key = item.ch + ':' + item.v;
    if (!byVerse[key]) byVerse[key] = [];
    byVerse[key].push(item);
  });

  Object.keys(byVerse).forEach(function (key) {
    var items = byVerse[key];
    var parts = key.split(':');
    var ch = parts[0], v = parts[1];

    resultsEl.querySelectorAll('.reader-verse[data-v="' + v + '"][data-ch="' + ch + '"]')
      .forEach(function (verse) {
        verse.classList.add('reader-verse--has-echo');

        var verseRef = ((verse.getAttribute('data-book') || '') + ' ' + ch + ':' + v).trim();

        // INTENT: a high-visibility chip (link glyph + count) makes echo/connection
        //   presence obvious at a glance; the active-verse highlight (toggled below)
        //   plus the panel's "Connections for {ref}" header make it unambiguous which
        //   verse a given marker and its open panel belong to.
        // CHANGE? Styling lives in reader.css: .reader-echo-marker (chip),
        //   .reader-verse--echo-active (open-verse highlight), .reader-echo-inline__head.
        // VERIFY: Toggle "◉ Connections" on a chapter with echoes (e.g. Matthew 1) — each
        //   marked verse shows a gold link-count chip; click one and that verse highlights
        //   and the panel header names the verse.
        var marker = document.createElement('button');
        marker.className = 'reader-echo-marker';
        marker.type = 'button';
        marker.setAttribute('aria-expanded', 'false');
        marker.setAttribute('aria-label',
          'Connections: ' + items.length + ' for ' + verseRef);
        marker.innerHTML =
          '<span class="reader-echo-marker__icon" aria-hidden="true">🔗</span>' +
          '<span class="reader-echo-marker__count" aria-hidden="true">' + items.length + '</span>';
        verse.appendChild(marker);

        var inlineBlock = document.createElement('div');
        inlineBlock.className = 'reader-echo-inline';
        inlineBlock.hidden = true;
        if (verse.nextSibling) {
          verse.parentNode.insertBefore(inlineBlock, verse.nextSibling);
        } else {
          verse.parentNode.appendChild(inlineBlock);
        }

        var built = false;
        marker.addEventListener('click', function (e) {
          e.stopPropagation();
          var expanded = marker.getAttribute('aria-expanded') === 'true';
          marker.setAttribute('aria-expanded', String(!expanded));
          marker.classList.toggle('reader-echo-marker--open', !expanded);
          verse.classList.toggle('reader-verse--echo-active', !expanded);
          inlineBlock.hidden = expanded;
          if (!expanded && !built) {
            built = true;
            _buildInlineCards(items, inlineBlock, verseRef);
          }
        });
      });
  });
}

// Build compact echo cards inside an inline expansion block.
// Reuses badge/card styles from echo-card without the v. prefix (redundant
// when the block is anchored to a specific verse).
function _buildInlineCards(items, container, verseRef) {
  var frag = document.createDocumentFragment();
  if (verseRef) {
    var head = document.createElement('div');
    head.className = 'reader-echo-inline__head';
    head.innerHTML =
      '<span class="reader-echo-inline__icon" aria-hidden="true">🔗</span>' +
      'Connections for <strong>' + escHtml(verseRef) + '</strong>';
    frag.appendChild(head);
  }
  items.forEach(function (item, idx) {
    var entry  = item.entry;
    var type   = entry.type || 'allusion';
    var bClass = _ECHO_BADGE_CLASS[type] || 'allusion';
    var bLabel = _ECHO_BADGE_LABEL[type] || type;
    var note   = entry.note   || '';
    var target = entry.target || '';
    var bodyId = 'echo-il-' + item.ch + '-' + item.v + '-' + idx;

    var card = document.createElement('div');
    card.className = 'reader-echo-card';
    card.setAttribute('data-echo-v',    String(item.v));
    card.setAttribute('data-echo-ch',   String(item.ch));
    card.setAttribute('data-echo-type', bClass);

    var toggle = document.createElement('button');
    toggle.className = 'reader-echo-card__toggle';
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', bodyId);
    toggle.innerHTML =
      '<span class="reader-echo-card__badge reader-echo-card__badge--' + escHtml(bClass) + '">' + escHtml(bLabel) + '</span>' +
      '<span class="reader-echo-card__target" title="' + escHtml(target) + '">' + escHtml(target) + '</span>' +
      '<span class="reader-echo-card__chevron" aria-hidden="true">&#9654;</span>';

    var body = document.createElement('div');
    body.className = 'reader-echo-card__body';
    body.id = bodyId;
    body.hidden = true;

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

    var textLoaded = false;
    toggle.addEventListener('click', function () {
      var expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', !expanded ? 'true' : 'false');
      body.hidden = expanded;
      card.classList.toggle('reader-echo-card--expanded', !expanded);
      if (!expanded && !textLoaded) {
        textLoaded = true;
        _loadEchoText(target, getVersion(), verseBlock);
      }
    });

    card.appendChild(toggle);
    card.appendChild(body);
    frag.appendChild(card);
  });
  container.appendChild(frag);
}

// INTENT: Render echo "connection" cards grouped by verse into an arbitrary container,
//   reusing the reader's exact inline-card UI (badge + collapsible target + on-demand verse
//   text). The Passage Study Desk calls this so its Connections section is identical to the
//   reader's, except annotated per-verse ("Connections for {book ch:v}") and collapsed.
// CHANGE? entries shape: [{book, ch, v, entry:{type,target,note}}]. Delegates to
//   _buildInlineCards (one head + cards per verse); if that signature changes, update here.
//   Caller owns the container (clear it before re-rendering a new passage).
// VERIFY: Open the study desk on Matthew 1 with echoes present — the Connections section
//   shows a "Connections for Matthew 1:1" head and the same expandable cards as the reader.
export function renderEchoCardsGrouped(entries, container) {
  if (!entries || !entries.length) return false;
  var byVerse = Object.create(null), order = [];
  entries.forEach(function (it) {
    var k = it.ch + ':' + it.v;
    if (!byVerse[k]) { byVerse[k] = []; order.push(k); }
    byVerse[k].push(it);
  });
  order.sort(function (a, b) {
    var pa = a.split(':'), pb = b.split(':');
    return (pa[0] - pb[0]) || (pa[1] - pb[1]);
  });
  order.forEach(function (k) {
    var items = byVerse[k];
    var first = items[0];
    var verseRef = ((first.book || '') + ' ' + first.ch + ':' + first.v).trim();
    _buildInlineCards(items, container, verseRef);
  });
  return true;
}

var _PARALLEL_PAGE_SIZE = 5;

// Fetch verse text for an echo card body and render it. Paginates when the
// verse range exceeds _PARALLEL_PAGE_SIZE; loadBook() caches the full chapter.
function _loadEchoText(ref, version, container, page) {
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

    var totalPages = Math.max(1, Math.ceil(allVerses.length / _PARALLEL_PAGE_SIZE));
    page = Math.max(0, Math.min(page, totalPages - 1));
    var pageVerses = allVerses.slice(page * _PARALLEL_PAGE_SIZE, (page + 1) * _PARALLEL_PAGE_SIZE);

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
      var info   = 'vv. ' + firstV + (lastV !== firstV ? '–' + lastV : '');
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
    if (parts.length) autoTagTermsWhenReady(container);

    container.querySelectorAll('.reader-parallel-pager__btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        _loadEchoText(ref, version, container, parseInt(btn.getAttribute('data-page'), 10));
      });
    });
  }).catch(function () {
    container.innerHTML = '<p class="reader-parallel-empty">Could not load.</p>';
  });
}
