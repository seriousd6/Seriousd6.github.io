/* lib-browser.js — 3-column library browser (filter → list → reader) */
'use strict';

import { _resolve, escHtml } from './core.js';
import { wireRefLinks, autoTagRefs } from './wire.js';
import { autoTagTermsWhenReady } from './terms.js';

var INDEX_URL = _resolve('../../data/library/index.json');
var DOCS_ROOT = _resolve('../../data/library/docs/');

var _index       = null;  // full index from index.json
var _filtered    = [];    // current filtered subset
var _activeId    = null;  // currently open document id
var _docCache    = {};    // id → loaded doc JSON
var _listWired   = false; // event delegation registered once
var _searchTimer = null;
var _filters     = { tradition: 'all', author: 'all', type: 'all', q: '' };

export function initLibBrowserPage() {
  if (!document.getElementById('lb-container')) return;

  // Wire the filter column collapse toggle
  var toggleBtn = document.getElementById('lb-filter-toggle');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      var layout    = document.getElementById('lb-container');
      var collapsed = layout.classList.toggle('lb-layout--filters-collapsed');
      toggleBtn.textContent = collapsed ? '›' : '‹';
      toggleBtn.setAttribute('aria-label', collapsed ? 'Expand filters' : 'Collapse filters');
    });
  }

  // Wire the document list collapse toggle
  var listToggleBtn = document.getElementById('lb-list-toggle');
  if (listToggleBtn) {
    listToggleBtn.addEventListener('click', function() {
      var layout    = document.getElementById('lb-container');
      var collapsed = layout.classList.toggle('lb-layout--list-collapsed');
      listToggleBtn.textContent = collapsed ? '›' : '‹';
      listToggleBtn.setAttribute('aria-label', collapsed ? 'Expand document list' : 'Collapse document list');
    });
  }

  fetch(INDEX_URL)
    .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function(data) {
      _index = data;
      _buildFilterPanel();
      _applyFilters();
      _renderList();
      _wireList();

      // Auto-open a document if ?doc= is present in the URL
      var docId = new URLSearchParams(window.location.search).get('doc');
      if (docId) _openDoc(docId);
    })
    .catch(function(err) {
      console.error('[LibBrowser] index load error:', err);
    });
}

/* ── Filter constants ────────────────────────────────────────────────────── */

// Filter levels in order highest → lowest: tradition > author > type.
// Changing a higher level resets all lower levels to 'all'.
var _FILTER_HIERARCHY = ['tradition', 'author', 'type'];

var _TRADITIONS = [
  { value: 'all',        label: 'All' },
  { value: 'ecumenical', label: 'Ecumenical' },
  { value: 'reformed',   label: 'Reformed' },
  { value: 'lutheran',   label: 'Lutheran' },
  { value: 'anglican',   label: 'Anglican' },
  { value: 'baptist',    label: 'Baptist' },
  { value: 'catholic',   label: 'Catholic' },
  { value: 'patristic',  label: 'Patristic' }
];

var _TYPES = [
  { value: 'all',        label: 'All' },
  { value: 'creed',      label: 'Creed' },
  { value: 'confession', label: 'Confession' },
  { value: 'catechism',  label: 'Catechism' },
  { value: 'father',     label: 'Father' }
];

var _TRAD_LABELS = {
  ecumenical: 'Ecumenical', reformed: 'Reformed', lutheran: 'Lutheran',
  anglican: 'Anglican', baptist: 'Baptist', catholic: 'Catholic', patristic: 'Patristic'
};

var _TYPE_LABELS = {
  creed: 'Creed', confession: 'Confession', catechism: 'Catechism',
  canons: 'Canons', father: 'Father'
};

/* ── Filter panel ────────────────────────────────────────────────────────── */

function _buildFilterPanel() {
  var panel = document.getElementById('lb-filter-panel');
  if (!panel) return;

  var html =
    '<div class="lb-filter-section">' +
      '<input id="lb-search" class="lb-search" type="search" placeholder="Search…" autocomplete="off" aria-label="Search documents" />' +
    '</div>';

  html += _chipGroup('Tradition', 'tradition', _TRADITIONS);
  html += _authorChipGroupHtml('all');  // initially show all authors
  html += _chipGroup('Type', 'type', _TYPES);

  panel.innerHTML = html;

  // Chip clicks — delegate to the panel
  panel.addEventListener('click', function(e) {
    var chip = e.target.closest('.lb-chip');
    if (!chip) return;
    var key   = chip.dataset.filter;
    var value = chip.dataset.value;

    // Update the changed filter
    _filters[key] = value;

    // Reset all lower-level filters to 'all'
    var level = _FILTER_HIERARCHY.indexOf(key);
    for (var i = level + 1; i < _FILTER_HIERARCHY.length; i++) {
      var lowerKey = _FILTER_HIERARCHY[i];
      _filters[lowerKey] = 'all';
      // Don't update author chips via querySelectorAll here — _rebuildAuthorChips does it
      if (lowerKey !== 'author') {
        panel.querySelectorAll('[data-filter="' + lowerKey + '"]').forEach(function(c) {
          c.classList.toggle('lb-chip--active', c.dataset.value === 'all');
        });
      }
    }

    // When tradition changes, rebuild the author chip list to match available authors
    if (key === 'tradition') _rebuildAuthorChips(panel, value);

    // Update active state within the changed chip group
    chip.closest('.lb-chips').querySelectorAll('.lb-chip').forEach(function(c) {
      c.classList.toggle('lb-chip--active', c.dataset.value === value);
    });

    _applyFilters();
    _renderList();
  });

  // Search — independent of filter hierarchy, doesn't reset anything
  var searchEl = document.getElementById('lb-search');
  if (searchEl) {
    searchEl.addEventListener('input', function() {
      clearTimeout(_searchTimer);
      var q = searchEl.value.trim();
      _searchTimer = setTimeout(function() {
        _filters.q = q;
        _applyFilters();
        _renderList();
      }, 200);
    });
  }
}

// Build the author chip group HTML scoped to a given tradition ('all' = no scope)
function _authorChipGroupHtml(tradition) {
  var counts = {};
  _index.forEach(function(doc) {
    if (!doc.author) return;
    if (tradition !== 'all' && doc.tradition !== tradition) return;
    counts[doc.author] = (counts[doc.author] || 0) + 1;
  });
  var names = Object.keys(counts).sort();
  var items = [{ value: 'all', label: 'All' }].concat(
    names.map(function(a) {
      return { value: a, label: counts[a] > 1 ? a + ' (' + counts[a] + ')' : a };
    })
  );
  return _chipGroup('Author', 'author', items, 'author');
}

// Rebuild only the author chip group when tradition changes, so the list stays relevant
function _rebuildAuthorChips(panel, tradition) {
  var existing = panel.querySelector('[data-filter-group="author"]');
  if (!existing) return;
  var temp = document.createElement('div');
  temp.innerHTML = _authorChipGroupHtml(tradition);
  var fresh = temp.firstElementChild;
  // 'All' is always active after a tradition change (hierarchy reset author to 'all')
  fresh.querySelectorAll('[data-filter="author"]').forEach(function(c) {
    c.classList.toggle('lb-chip--active', c.dataset.value === 'all');
  });
  existing.replaceWith(fresh);
}

function _chipGroup(label, filterKey, items, groupId) {
  var attr = groupId ? ' data-filter-group="' + escHtml(groupId) + '"' : '';
  var html = '<div class="lb-filter-section"' + attr + '><div class="lb-filter-label">' + escHtml(label) + '</div><div class="lb-chips">';
  items.forEach(function(item) {
    var active = item.value === 'all' ? ' lb-chip--active' : '';
    html += '<button class="lb-chip' + active + '" data-filter="' + escHtml(filterKey) + '" data-value="' + escHtml(item.value) + '">' + escHtml(item.label) + '</button>';
  });
  return html + '</div></div>';
}

/* ── Filtering ───────────────────────────────────────────────────────────── */

function _applyFilters() {
  var q = _filters.q.toLowerCase();
  _filtered = _index.filter(function(doc) {
    if (_filters.tradition !== 'all' && doc.tradition !== _filters.tradition) return false;
    if (_filters.author !== 'all' && doc.author !== _filters.author) return false;

    // 'confession' type filter also matches 'canons'
    if (_filters.type !== 'all') {
      if (_filters.type === 'confession') {
        if (doc.type !== 'confession' && doc.type !== 'canons') return false;
      } else {
        if (doc.type !== _filters.type) return false;
      }
    }

    if (q) {
      return (doc.title.toLowerCase().indexOf(q) !== -1) ||
             (doc.desc && doc.desc.toLowerCase().indexOf(q) !== -1);
    }
    return true;
  });
}

/* ── Document list ───────────────────────────────────────────────────────── */

function _renderList() {
  var list    = document.getElementById('lb-list');
  var countEl = document.getElementById('lb-list-count');
  if (!list) return;

  if (countEl) {
    countEl.textContent = _filtered.length + ' document' + (_filtered.length !== 1 ? 's' : '');
  }

  if (!_filtered.length) {
    list.innerHTML = '<p class="lb-list-empty">No documents match.</p>';
    return;
  }

  var html = '';
  _filtered.forEach(function(doc) {
    var active  = doc.id === _activeId ? ' lb-list-item--active' : '';
    var yearStr = doc.year < 500 ? 'c. ' + doc.year + ' AD' : String(doc.year);
    var trad    = _TRAD_LABELS[doc.tradition] || doc.tradition;
    var type    = _TYPE_LABELS[doc.type] || doc.type;
    html +=
      '<button class="lb-list-item' + active + '" data-doc-id="' + escHtml(doc.id) + '" aria-label="' + escHtml(doc.title) + '">' +
        '<span class="lb-item-abbrev lb-item-abbrev--' + escHtml(doc.tradition) + '">' + escHtml(doc.abbrev) + '</span>' +
        '<span class="lb-item-body">' +
          '<span class="lb-item-title">' + escHtml(doc.title) + '</span>' +
          '<span class="lb-item-meta">' + escHtml(yearStr) + ' · ' + escHtml(trad) + ' · ' + escHtml(type) + '</span>' +
          (doc.desc ? '<span class="lb-item-desc">' + escHtml(doc.desc) + '</span>' : '') +
        '</span>' +
      '</button>';
  });
  list.innerHTML = html;
}

// Wire list click once; re-renders replace innerHTML but the container element stays
function _wireList() {
  if (_listWired) return;
  _listWired = true;
  var container = document.getElementById('lb-list');
  if (!container) return;
  container.addEventListener('click', function(e) {
    var item = e.target.closest('.lb-list-item');
    if (!item) return;
    var docId = item.dataset.docId;
    if (!docId) return;
    if (_activeId === docId) {
      // Click the active document again → deselect and show placeholder
      _activeId = null;
      item.classList.remove('lb-list-item--active');
      _renderReaderPlaceholder();
      return;
    }
    _openDoc(docId);
  });
}

/* ── Reader panel ────────────────────────────────────────────────────────── */

function _renderReaderPlaceholder() {
  var panel = document.getElementById('lb-reader');
  if (panel) panel.innerHTML = '<p class="lb-reader-placeholder">← Select a document</p>';
}

function _openDoc(docId) {
  _activeId = docId;

  // Sync list active state
  document.querySelectorAll('.lb-list-item').forEach(function(el) {
    el.classList.toggle('lb-list-item--active', el.dataset.docId === docId);
  });

  var panel = document.getElementById('lb-reader');
  if (!panel) return;

  if (_docCache[docId]) {
    _renderReader(_docCache[docId]);
    return;
  }

  panel.innerHTML = '<p class="lb-reader-loading">Loading…</p>';

  fetch(DOCS_ROOT + docId + '.json')
    .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function(doc) {
      _docCache[docId] = doc;
      // Guard: user may have selected a different doc while this was in flight
      if (_activeId === docId) _renderReader(doc);
    })
    .catch(function(err) {
      console.error('[LibBrowser] doc load error:', err);
      if (_activeId === docId) {
        panel.innerHTML = '<p class="lb-reader-loading">Error loading document.</p>';
      }
    });
}

function _renderReader(doc) {
  var entry     = _index && _index.find(function(d) { return d.id === doc.id; });
  var tradition = (entry && entry.tradition) || 'ecumenical';
  var tradLabel = _TRAD_LABELS[tradition] || tradition;
  var typeLabel = _TYPE_LABELS[doc.type] || doc.type;
  var year      = entry && entry.year;
  var yearStr   = year ? (year < 500 ? 'c. ' + year + ' AD' : String(year)) : '';

  // Inline TOC — only for multi-section documents
  var tocHtml = '';
  if (doc.sections && doc.sections.length > 1) {
    tocHtml = '<nav class="lb-reader-toc"><div class="lb-reader-toc-label">Contents</div><ul class="lb-reader-toc-list">';
    doc.sections.forEach(function(s, i) {
      tocHtml += '<li><a href="#lbrs-' + i + '">' + escHtml(s.heading) + '</a></li>';
    });
    tocHtml += '</ul></nav>';
  }

  var bodyHtml = '';
  if (doc.sections) {
    doc.sections.forEach(function(s, i) {
      bodyHtml += '<section class="lb-reader-section" id="lbrs-' + i + '">' + s.html + '</section>';
    });
  }

  var panel = document.getElementById('lb-reader');
  if (!panel) return;

  panel.innerHTML =
    '<div class="lb-reader-header">' +
      '<h2 class="lb-reader-title">' + escHtml(doc.title) + '</h2>' +
      '<div class="lb-reader-meta">' +
        '<span class="lib-badge lib-badge--' + escHtml(tradition) + '">' + escHtml(tradLabel) + '</span>' +
        (yearStr ? '<span class="lb-reader-year">' + escHtml(yearStr) + '</span>' : '') +
        '<span class="lb-reader-type">' + escHtml(typeLabel) + '</span>' +
      '</div>' +
      tocHtml +
    '</div>' +
    '<div class="lb-reader-body">' + bodyHtml + '</div>';

  panel.scrollTop = 0;

  // Wire all interactives into the freshly-injected content
  wireRefLinks(panel);
  autoTagRefs();
  var body = panel.querySelector('.lb-reader-body');
  if (body) autoTagTermsWhenReady(body);
}
