/* lib-browser.js — 3-column library browser (filter → list → reader) */
'use strict';

import { _resolve, escHtml } from './core.js';
import { wireRefLinks, autoTagRefs } from './wire.js';
import { autoTagTermsWhenReady } from './terms.js';

var INDEX_URL = _resolve('../../data/library/index.json');
var DOCS_ROOT = _resolve('../../data/library/docs/');
var HTML_ROOT = _resolve('../../data/library/html/');

var _index       = null;  // full index from index.json
var _filtered    = [];    // current filtered + sorted subset
var _activeId    = null;  // currently open document id
var _docCache    = {};    // id → loaded doc JSON/HTML
var _listWired   = false; // event delegation registered once
var _searchTimer = null;
var _spyListener = null;  // current scroll-spy listener (disconnected on next render)
var _filters     = { tradition: 'all', era: 'all', author: 'all', type: 'all', sort: 'year-asc', q: '' };

export function initLibBrowserPage() {
  if (!document.getElementById('lb-container')) return;

  var toggleBtn = document.getElementById('lb-filter-toggle');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      var layout    = document.getElementById('lb-container');
      var collapsed = layout.classList.toggle('lb-layout--filters-collapsed');
      toggleBtn.textContent = collapsed ? '›' : '‹';
      toggleBtn.setAttribute('aria-label', collapsed ? 'Expand filters' : 'Collapse filters');
    });
  }

  var listToggleBtn = document.getElementById('lb-list-toggle');
  if (listToggleBtn) {
    listToggleBtn.addEventListener('click', function() {
      var layout    = document.getElementById('lb-container');
      var collapsed = layout.classList.toggle('lb-layout--list-collapsed');
      listToggleBtn.textContent = collapsed ? '›' : '‹';
      listToggleBtn.setAttribute('aria-label', collapsed ? 'Expand document list' : 'Collapse document list');
    });
  }

  _initFromUrl();

  fetch(INDEX_URL)
    .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function(data) {
      _index = data;
      _buildFilterPanel();
      _buildSortControl();
      _applyFilters();
      _sortFiltered();
      _renderList();
      _wireList();

      if (_activeId) _openDoc(_activeId);
    })
    .catch(function(err) {
      console.error('[LibBrowser] index load error:', err);
    });
}

/* ── URL state ───────────────────────────────────────────────────────────── */

function _initFromUrl() {
  var p = new URLSearchParams(window.location.search);
  if (p.get('tradition')) _filters.tradition = p.get('tradition');
  if (p.get('era'))       _filters.era       = p.get('era');
  if (p.get('type'))      _filters.type      = p.get('type');
  if (p.get('author'))    _filters.author    = p.get('author');
  if (p.get('sort'))      _filters.sort      = p.get('sort');
  if (p.get('q'))         _filters.q         = p.get('q');
  if (p.get('doc'))       _activeId          = p.get('doc');
}

function _pushUrlState() {
  var p = new URLSearchParams();
  if (_filters.tradition !== 'all')      p.set('tradition', _filters.tradition);
  if (_filters.era       !== 'all')      p.set('era',       _filters.era);
  if (_filters.type      !== 'all')      p.set('type',      _filters.type);
  if (_filters.author    !== 'all')      p.set('author',    _filters.author);
  if (_filters.sort      !== 'year-asc') p.set('sort',      _filters.sort);
  if (_filters.q)                        p.set('q',         _filters.q);
  if (_activeId)                         p.set('doc',       _activeId);
  var qs = p.toString();
  history.replaceState(null, '', qs ? '?' + qs : window.location.pathname);
}

/* ── Filter constants ────────────────────────────────────────────────────── */

// Filter levels in order highest → lowest: tradition > author > type.
// Changing a higher level resets all lower levels to 'all'.
// Era is independent — it doesn't cascade into/from the hierarchy.
var _FILTER_HIERARCHY = ['tradition', 'author', 'type'];

var _TRADITIONS = [
  { value: 'all',              label: 'All' },
  { value: 'ecumenical',       label: 'Ecumenical' },
  { value: 'reformed',         label: 'Reformed' },
  { value: 'lutheran',         label: 'Lutheran' },
  { value: 'anglican',         label: 'Anglican' },
  { value: 'baptist',          label: 'Baptist' },
  { value: 'anabaptist',       label: 'Anabaptist' },
  { value: 'congregationalist',label: 'Congregationalist' },
  { value: 'methodist',        label: 'Methodist' },
  { value: 'orthodox',         label: 'Orthodox' },
  { value: 'catholic',         label: 'Catholic' },
  { value: 'patristic',        label: 'Patristic' }
];

var _ERAS = [
  { value: 'all',              label: 'All' },
  { value: 'patristic',        label: 'Patristic' },
  { value: 'medieval',         label: 'Medieval' },
  { value: 'reformation',      label: 'Reformation' },
  { value: 'post-reformation', label: 'Post-Reformation' },
  { value: 'modern',           label: 'Modern' }
];

var _TYPES = [
  { value: 'all',        label: 'All' },
  { value: 'creed',      label: 'Creed' },
  { value: 'confession', label: 'Confession' },
  { value: 'catechism',  label: 'Catechism' },
  { value: 'canons',     label: 'Canons' },
  { value: 'council',    label: 'Council' },
  { value: 'father',     label: 'Father' }
];

var _TRAD_LABELS = {
  ecumenical: 'Ecumenical', reformed: 'Reformed', lutheran: 'Lutheran',
  anglican: 'Anglican', baptist: 'Baptist', anabaptist: 'Anabaptist',
  congregationalist: 'Congregationalist', methodist: 'Methodist',
  orthodox: 'Orthodox', catholic: 'Catholic', patristic: 'Patristic'
};

var _TYPE_LABELS = {
  creed: 'Creed', confession: 'Confession', catechism: 'Catechism',
  canons: 'Canons', council: 'Council', father: 'Father'
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
  html += _chipGroup('Era', 'era', _ERAS);
  html += _authorChipGroupHtml(_filters.tradition);
  html += _chipGroup('Type', 'type', _TYPES);

  panel.innerHTML = html;

  // Restore search box value when navigating back via URL
  var searchEl = document.getElementById('lb-search');
  if (searchEl && _filters.q) searchEl.value = _filters.q;

  // Chip clicks — delegate to the panel
  panel.addEventListener('click', function(e) {
    var chip = e.target.closest('.lb-chip');
    if (!chip) return;
    var key   = chip.dataset.filter;
    var value = chip.dataset.value;

    // Clicking the already-active chip deselects it (resets to 'all')
    if (value !== 'all' && _filters[key] === value) value = 'all';

    _filters[key] = value;

    // Reset all lower-level filters to 'all' (tradition → author → type)
    var level = _FILTER_HIERARCHY.indexOf(key);
    if (level !== -1) {
      for (var i = level + 1; i < _FILTER_HIERARCHY.length; i++) {
        var lowerKey = _FILTER_HIERARCHY[i];
        _filters[lowerKey] = 'all';
        if (lowerKey !== 'author') {
          panel.querySelectorAll('[data-filter="' + lowerKey + '"]').forEach(function(c) {
            c.classList.toggle('lb-chip--active', c.dataset.value === 'all');
          });
        }
      }
      if (key === 'tradition') _rebuildAuthorChips(panel, value);
    }

    chip.closest('.lb-chips').querySelectorAll('.lb-chip').forEach(function(c) {
      c.classList.toggle('lb-chip--active', c.dataset.value === value);
    });

    _applyFilters();
    _sortFiltered();
    _renderList();
    _pushUrlState();
  });

  // Search — independent of filter hierarchy, doesn't reset anything
  if (searchEl) {
    searchEl.addEventListener('input', function() {
      clearTimeout(_searchTimer);
      var q = searchEl.value.trim();
      _searchTimer = setTimeout(function() {
        _filters.q = q;
        _applyFilters();
        _sortFiltered();
        _renderList();
        _pushUrlState();
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

// _filters[filterKey] drives the initial active state so URL-restored filters render correctly
function _chipGroup(label, filterKey, items, groupId) {
  var attr = groupId ? ' data-filter-group="' + escHtml(groupId) + '"' : '';
  var html = '<div class="lb-filter-section"' + attr + '><div class="lb-filter-label">' + escHtml(label) + '</div><div class="lb-chips">';
  var current = _filters[filterKey] || 'all';
  items.forEach(function(item) {
    var active = item.value === current ? ' lb-chip--active' : '';
    html += '<button class="lb-chip' + active + '" data-filter="' + escHtml(filterKey) + '" data-value="' + escHtml(item.value) + '">' + escHtml(item.label) + '</button>';
  });
  return html + '</div></div>';
}

/* ── Sort control ────────────────────────────────────────────────────────── */

function _buildSortControl() {
  var container = document.getElementById('lb-list-controls');
  if (!container) return;

  container.innerHTML =
    '<div class="lb-sort-row">' +
      '<label class="lb-sort-label" for="lb-sort">Sort</label>' +
      '<select id="lb-sort" class="lb-sort-select">' +
        '<option value="year-asc">Year ↑</option>' +
        '<option value="year-desc">Year ↓</option>' +
        '<option value="title-asc">Title A–Z</option>' +
      '</select>' +
    '</div>';

  var sel = document.getElementById('lb-sort');
  if (!sel) return;
  sel.value = _filters.sort;

  sel.addEventListener('change', function() {
    _filters.sort = sel.value;
    _sortFiltered();
    _renderList();
    _pushUrlState();
  });
}

/* ── Filtering & sorting ─────────────────────────────────────────────────── */

function _applyFilters() {
  var q = _filters.q.toLowerCase();
  _filtered = _index.filter(function(doc) {
    if (_filters.tradition !== 'all' && doc.tradition !== _filters.tradition) return false;
    if (_filters.era       !== 'all' && doc.era       !== _filters.era)       return false;
    if (_filters.author    !== 'all' && doc.author    !== _filters.author)    return false;

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

function _sortFiltered() {
  var sort = _filters.sort;
  _filtered.sort(function(a, b) {
    if (sort === 'year-desc') return (b.year || 0) - (a.year || 0);
    if (sort === 'title-asc') return a.title.localeCompare(b.title);
    return (a.year || 0) - (b.year || 0); // year-asc default
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
      _pushUrlState();
      return;
    }
    _openDoc(docId);
  });
}

/* ── Reader panel ────────────────────────────────────────────────────────── */

function _renderReaderPlaceholder() {
  var panel = document.getElementById('lb-reader');
  if (panel) panel.innerHTML = '<p class="lb-reader-placeholder">← Select a document</p>';
  if (_spyListener) {
    var readerCol = document.querySelector('.lb-col--reader');
    if (readerCol) readerCol.removeEventListener('scroll', _spyListener);
    _spyListener = null;
  }
}

function _openDoc(docId) {
  _activeId = docId;
  _pushUrlState();

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

  // Full-text documents use a standalone HTML file rather than an embedded-JSON doc
  var entry    = _index && _index.find(function(d) { return d.id === docId; });
  var htmlFile = entry && entry.html_url;

  var fetchPromise = htmlFile
    ? fetch(HTML_ROOT + htmlFile)
        .then(function(r) { return r.ok ? r.text() : Promise.reject(r.status); })
        .then(function(html) { return _parseHtmlDoc(docId, html); })
    : fetch(DOCS_ROOT + docId + '.json')
        .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); });

  fetchPromise
    .then(function(doc) {
      _docCache[docId] = doc;
      if (_activeId === docId) _renderReader(doc);
    })
    .catch(function(err) {
      console.error('[LibBrowser] doc load error:', err);
      if (_activeId === docId) {
        panel.innerHTML = '<p class="lb-reader-loading">Error loading document.</p>';
      }
    });
}

// Parse a standalone HTML file into the same {id, title, type, sections} shape the reader expects
function _parseHtmlDoc(docId, html) {
  var wrap = document.createElement('div');
  wrap.innerHTML = html;
  var entry    = _index && _index.find(function(d) { return d.id === docId; });
  var sections = [];
  wrap.querySelectorAll('section[data-heading]').forEach(function(el) {
    sections.push({ ref: String(sections.length + 1), heading: el.getAttribute('data-heading'), html: el.innerHTML });
  });
  // Fallback: no section wrappers — treat entire body as one section
  if (!sections.length) sections.push({ ref: '1', heading: '', html: html });
  return {
    id:       docId,
    title:    (entry && entry.title)  || docId,
    type:     (entry && entry.type)   || '',
    sections: sections
  };
}

// Return true when the section HTML already opens with a heading matching `text`.
// Checks the first element and its first child — covers both direct <h2> and
// the <section class="lib-chapter"><h2 class="lib-chapter__title"> pattern.
function _bodyHasHeading(html, text) {
  var tmp = document.createElement('div');
  tmp.innerHTML = html;
  var target = text.trim();
  function matchEl(el) {
    return el && /^H[1-6]$/.test(el.tagName) && el.textContent.trim() === target;
  }
  var first = tmp.firstElementChild;
  return matchEl(first) || matchEl(first && first.firstElementChild);
}

function _renderReader(doc) {
  var entry     = _index && _index.find(function(d) { return d.id === doc.id; });
  var tradition = (entry && entry.tradition) || 'ecumenical';
  var tradLabel = _TRAD_LABELS[tradition] || tradition;
  var typeLabel = _TYPE_LABELS[doc.type] || doc.type;
  var year      = entry && entry.year;
  var yearStr   = year ? (year < 500 ? 'c. ' + year + ' AD' : String(year)) : '';
  var author    = entry && entry.author;

  // Inline TOC — only for multi-section documents
  var multiSection = doc.sections && doc.sections.length > 1;
  var tocHtml = '';
  if (multiSection) {
    tocHtml = '<nav class="lb-reader-toc"><div class="lb-reader-toc-label">Contents</div><ul class="lb-reader-toc-list">';
    doc.sections.forEach(function(s, i) {
      tocHtml += '<li><a href="#lbrs-' + i + '">' + escHtml(s.heading) + '</a></li>';
    });
    tocHtml += '</ul></nav>';
  }

  var bodyHtml = '';
  if (doc.sections) {
    doc.sections.forEach(function(s, i) {
      // Only inject a section heading when the body doesn't already open with the same text.
      // Older JSON docs (Westminster, Belgic, patristics…) embed an h2.lib-chapter__title
      // that duplicates s.heading — in those cases the existing heading is sufficient.
      var headingHtml = '';
      if (multiSection && s.heading && !_bodyHasHeading(s.html, s.heading)) {
        headingHtml = '<h2 class="lb-section-heading">' + escHtml(s.heading) + '</h2>';
      }
      bodyHtml += '<section class="lb-reader-section" id="lbrs-' + i + '">' + headingHtml + s.html + '</section>';
    });
  }

  var panel = document.getElementById('lb-reader');
  if (!panel) return;

  panel.innerHTML =
    '<div class="lb-reader-header">' +
      '<h2 class="lb-reader-title">' + escHtml(doc.title) + '</h2>' +
      '<div class="lb-reader-meta">' +
        '<span class="lib-badge lib-badge--' + escHtml(tradition) + '">' + escHtml(tradLabel) + '</span>' +
        (yearStr ? '<span class="lb-reader-year">'   + escHtml(yearStr) + '</span>' : '') +
        (author  ? '<span class="lb-reader-author">' + escHtml(author)  + '</span>' : '') +
        '<span class="lb-reader-type">' + escHtml(typeLabel) + '</span>' +
      '</div>' +
      tocHtml +
    '</div>' +
    '<div class="lb-reader-body">' + bodyHtml + '</div>';

  // Scroll the column (not the inner div) back to the top
  var readerCol = document.querySelector('.lb-col--reader');
  if (readerCol) readerCol.scrollTop = 0;

  // Wire all interactives into the freshly-injected content
  wireRefLinks(panel);
  autoTagRefs();
  var body = panel.querySelector('.lb-reader-body');
  if (body) autoTagTermsWhenReady(body);

  _wireScrollSpy();
}

/* ── Scroll-spy ──────────────────────────────────────────────────────────── */

function _wireScrollSpy() {
  var readerCol = document.querySelector('.lb-col--reader');
  var panel     = document.getElementById('lb-reader');
  if (!readerCol || !panel) return;

  // Disconnect the previous listener before attaching a new one
  if (_spyListener) readerCol.removeEventListener('scroll', _spyListener);

  var sections = panel.querySelectorAll('.lb-reader-section');
  var tocLinks = panel.querySelectorAll('.lb-reader-toc-list a');
  if (!sections.length || !tocLinks.length) return;

  _spyListener = function() {
    // Find the last section whose top is at or above the threshold line (~100px from column top)
    var colTop    = readerCol.getBoundingClientRect().top;
    var threshold = colTop + 100;

    var activeId = null;
    sections.forEach(function(s) {
      if (s.getBoundingClientRect().top <= threshold) activeId = s.id;
    });

    tocLinks.forEach(function(a) {
      a.classList.toggle('lb-toc-active', !!activeId && a.getAttribute('href') === '#' + activeId);
    });
  };

  readerCol.addEventListener('scroll', _spyListener, { passive: true });
  // Run once immediately so the first section is marked active on load
  _spyListener();
}
