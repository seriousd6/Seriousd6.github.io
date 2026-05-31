/* parallels.js — Parallel passage reader (P1/P2/P3 types) */
'use strict';

import {
  PARALLELS_ROOT, getVersion, loadBook, parseRef, escHtml,
  metaBooks, parallelsCache
} from './core.js';
import { wireRefLinks, wireRefEl } from './wire.js';

export var PARALLELS_STORAGE_KEY = 'bsw_parallels';
export var PARALLEL_VERSE_WINDOW = 3;

export function getParallelsEnabled() {
  return localStorage.getItem(PARALLELS_STORAGE_KEY) === '1';
}
export function setParallelsEnabled(on) {
  localStorage.setItem(PARALLELS_STORAGE_KEY, on ? '1' : '0');
}

export function loadParallels(bookId) {
  if (parallelsCache[bookId] !== undefined) return Promise.resolve(parallelsCache[bookId]);
  var url = PARALLELS_ROOT + '/' + bookId + '.json';
  return fetch(url)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { parallelsCache[bookId] = d; return d; })
    .catch(function () { parallelsCache[bookId] = null; return null; });
}

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
      if (on) injectAllParallelPanels(resultsEl);
      else    removeAllParallelPanels(resultsEl);
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

export function buildParallelPanel(groupEl, parsed, sets) {
  var container = document.createElement('div');
  container.className = 'reader-parallels-container';

  var KNOWN_BADGE_TYPES = ['parallel', 'fulfillment', 'prophecy', 'quotation'];

  sets.forEach(function (s) {
    // Each verse entry is an array of group objects: [{type, label, refs:[{passage,label}]}]
    var groups = Array.isArray(s.groups) ? s.groups : [];
    groups.forEach(function (group) {
      var groupType = group.type || 'parallel';
      var badgeMod  = KNOWN_BADGE_TYPES.indexOf(groupType) !== -1 ? groupType : 'parallel';
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
        badge.textContent = groupType.charAt(0).toUpperCase() + groupType.slice(1);

        var refLabel = document.createElement('span');
        refLabel.className = 'reader-parallel-ref-label';
        refLabel.textContent = passage;

        var readLink = document.createElement('a');
        readLink.className = 'reader-parallel-read-link';
        readLink.setAttribute('data-ref', passage);
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

export function loadParallelText(ref, version, container) {
  var parsed = parseRef(ref);
  if (!parsed) { container.innerHTML = ''; return; }
  loadBook(version, parsed.bookId).then(function (chapters) {
    if (!chapters) {
      container.innerHTML = '<p class="reader-parallel-empty">Not available.</p>';
      return;
    }
    var ch     = chapters[String(parsed.ch)];
    var startV = parsed.v;
    var endV   = parsed.endV || parsed.v;
    var parts  = [];
    if (ch) {
      Object.keys(ch).map(Number)
        .filter(function (n) { return n >= startV && n <= endV; })
        .sort(function (a, b) { return a - b; })
        .forEach(function (vNum) {
          parts.push('<sup class="reader-verse__num">' + vNum + '</sup>' + escHtml(ch[String(vNum)]));
        });
    }
    container.innerHTML = parts.length
      ? '<p class="reader-parallel-text">' + parts.join(' ') + '</p>'
      : '<p class="reader-parallel-empty">Not available in this version.</p>';
  }).catch(function () {
    container.innerHTML = '<p class="reader-parallel-empty">Could not load.</p>';
  });
}

function _groupParsedRef(groupEl) {
  var verseEl = groupEl.querySelector('.reader-verse[data-book][data-ch]');
  if (!verseEl) return null;
  var bookName = verseEl.getAttribute('data-book');
  var ch       = parseInt(verseEl.getAttribute('data-ch'), 10);
  var bk = metaBooks && metaBooks.find(function (b) { return b.name === bookName || b.id === bookName; });
  if (!bk) return null;
  return { bookId: bk.id, bookName: bk.name, ch: ch, v: 1, endCh: ch, endV: 9999, display: bk.name + ' ' + ch };
}
