/* lib-browser.js — 4-column library browser (filter | authors | list | reader) */
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
var _keyListener = null;  // current paginated-mode arrow-key listener (cleaned up on mode change)
var _filters     = { tradition: 'all', era: 'all', author: 'all', type: 'all', sort: 'year-asc', q: '' };
var _sectionIdx  = {};    // docId → current section index (paginated mode)
var _authorsQ           = '';    // authors panel search string
var _authorsSearchTimer = null;

var _PAGINATE_THRESHOLD = 1;   // all multi-section docs paginate (one section at a time)
var _LIB_POS_PREFIX     = 'bsw_lbpos_';
var _LIB_FILTERS_KEY    = 'bsw_lib_filters';

var _findTerm      = '';   // active in-reader search term (persists across paginated re-renders)
var _findMatchSecs = [];   // section indices containing the term (paginated mode)
var _findCurrMatch = 0;    // which match index is currently shown (paginated mode)
var _findDocId     = '';   // doc whose find state is live (cleared when switching docs)

export function initLibBrowserPage() {
  if (!document.getElementById('lb-container')) return;
  _evictStalePositions();

  var toggleBtn = document.getElementById('lb-filter-toggle');
  if (toggleBtn) {
    toggleBtn.title = 'Collapse filters';
    toggleBtn.addEventListener('click', function() {
      var layout    = document.getElementById('lb-container');
      var collapsed = layout.classList.toggle('lb-layout--filters-collapsed');
      toggleBtn.textContent = collapsed ? '›' : '‹';
      toggleBtn.title = collapsed ? 'Expand filters' : 'Collapse filters';
      toggleBtn.setAttribute('aria-label', collapsed ? 'Expand filters' : 'Collapse filters');
    });
  }

  var authorsToggleBtn = document.getElementById('lb-authors-toggle');
  if (authorsToggleBtn) {
    authorsToggleBtn.title = 'Collapse authors';
    authorsToggleBtn.addEventListener('click', function() {
      var layout    = document.getElementById('lb-container');
      var collapsed = layout.classList.toggle('lb-layout--authors-collapsed');
      authorsToggleBtn.textContent = collapsed ? '›' : '‹';
      authorsToggleBtn.title = collapsed ? 'Expand authors' : 'Collapse authors';
      authorsToggleBtn.setAttribute('aria-label', collapsed ? 'Expand authors' : 'Collapse authors');
    });
  }

  var listToggleBtn = document.getElementById('lb-list-toggle');
  if (listToggleBtn) {
    listToggleBtn.title = 'Collapse document list';
    listToggleBtn.addEventListener('click', function() {
      var layout    = document.getElementById('lb-container');
      var collapsed = layout.classList.toggle('lb-layout--list-collapsed');
      listToggleBtn.textContent = collapsed ? '›' : '‹';
      listToggleBtn.title = collapsed ? 'Expand document list' : 'Collapse document list';
      listToggleBtn.setAttribute('aria-label', collapsed ? 'Expand document list' : 'Collapse document list');
    });
  }

  _initFromUrl();

  // ?focus=1 — collapse filter/authors/list panels so the reader fills the view.
  // Used by omni-search library links to land directly in the document.
  if (new URLSearchParams(window.location.search).get('focus') === '1') {
    var layout = document.getElementById('lb-container');
    if (layout) {
      layout.classList.add('lb-layout--filters-collapsed');
      layout.classList.add('lb-layout--authors-collapsed');
      layout.classList.add('lb-layout--list-collapsed');
    }
    if (toggleBtn) { toggleBtn.textContent = '›'; toggleBtn.setAttribute('aria-label', 'Expand filters'); }
    if (authorsToggleBtn) { authorsToggleBtn.textContent = '›'; authorsToggleBtn.setAttribute('aria-label', 'Expand authors'); }
    if (listToggleBtn) { listToggleBtn.textContent = '›'; listToggleBtn.setAttribute('aria-label', 'Expand document list'); }
  }

  _initMobileTabs();

  fetch(INDEX_URL)
    .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function(data) {
      _index = data;
      _buildFilterPanel();
      _buildSortControl();
      _applyFilters();
      _sortFiltered();
      _renderAuthors();
      _renderList();
      _wireList();
      _wireAuthors();

      if (_activeId) _openDoc(_activeId);
    })
    .catch(function(err) {
      console.error('[LibBrowser] index load error:', err);
    });
}

/* ── Mobile tab bar ─────────────────────────────────────────────────────── */

var _currentTab = 'list';  // default tab on mobile

function _initMobileTabs() {
  var layout = document.getElementById('lb-container');
  if (!layout) return;

  // Only activate tab mode at ≤600px; use matchMedia so desktop isn't affected
  var mq = window.matchMedia('(max-width: 600px)');

  function activate(active) {
    if (!active) {
      layout.classList.remove('lb-layout--tabbed');
      var bar = document.getElementById('lb-tab-bar');
      if (bar) bar.style.display = 'none';
      return;
    }
    layout.classList.add('lb-layout--tabbed');
    var bar = document.getElementById('lb-tab-bar');
    if (bar) bar.style.display = '';
    _switchTab(_currentTab);
  }

  // Build tab bar once and insert before the layout
  if (!document.getElementById('lb-tab-bar')) {
    var bar = document.createElement('div');
    bar.id = 'lb-tab-bar';
    bar.className = 'lb-tab-bar';
    bar.style.display = 'none';  // hidden until mobile MQ fires
    ['filter','authors','list','reader'].forEach(function(tab) {
      var btn = document.createElement('button');
      btn.className = 'lb-tab-btn';
      btn.dataset.tab = tab;
      btn.textContent = tab.charAt(0).toUpperCase() + tab.slice(1);
      btn.addEventListener('click', function() { _switchTab(tab); });
      bar.appendChild(btn);
    });
    layout.parentNode.insertBefore(bar, layout);
  }

  // When a doc is opened on mobile, auto-switch to the reader tab
  var origOpenDoc = window._lbOpenDocHook;
  window._lbOpenDocHook = function(docId) {
    if (mq.matches && docId) _switchTab('reader');
  };

  mq.addEventListener('change', function(e) { activate(e.matches); });
  activate(mq.matches);
}

function _switchTab(tab) {
  _currentTab = tab;
  var layout = document.getElementById('lb-container');
  var bar    = document.getElementById('lb-tab-bar');
  if (!layout) return;

  // Remove all tab state classes
  ['filters','authors','list','reader'].forEach(function(t) {
    layout.classList.remove('lb-tab--' + t);
  });
  layout.classList.add('lb-tab--' + tab);

  // Update active button
  if (bar) {
    bar.querySelectorAll('.lb-tab-btn').forEach(function(btn) {
      btn.classList.toggle('lb-tab-btn--active', btn.dataset.tab === tab);
    });
  }
}

/* ── URL state ───────────────────────────────────────────────────────────── */

function _initFromUrl() {
  var p = new URLSearchParams(window.location.search);
  var hasUrlFilters = p.get('tradition') || p.get('era') || p.get('type') || p.get('author') || p.get('sort') || p.get('q');

  if (hasUrlFilters) {
    if (p.get('tradition')) _filters.tradition = p.get('tradition');
    if (p.get('era'))       _filters.era       = p.get('era');
    if (p.get('type'))      _filters.type      = p.get('type');
    if (p.get('author'))    _filters.author    = p.get('author');
    if (p.get('sort'))      _filters.sort      = p.get('sort');
    if (p.get('q'))         _filters.q         = p.get('q');
  } else {
    // Restore filters from last session when the URL is clean
    try {
      var saved = JSON.parse(localStorage.getItem(_LIB_FILTERS_KEY) || '{}');
      if (saved.tradition) _filters.tradition = saved.tradition;
      if (saved.era)       _filters.era       = saved.era;
      if (saved.type)      _filters.type      = saved.type;
      if (saved.author)    _filters.author    = saved.author;
      if (saved.sort)      _filters.sort      = saved.sort;
      if (saved.q)         _filters.q         = saved.q;
    } catch(e) {}
  }

  if (p.get('doc'))  _activeId = p.get('doc');
  // Restore section index for the active doc so deep links land on the right chapter
  var sec = parseInt(p.get('section') || '0', 10);
  if (_activeId && sec > 0) _sectionIdx[_activeId] = sec;
}

function _saveFilters() {
  try { localStorage.setItem(_LIB_FILTERS_KEY, JSON.stringify(_filters)); } catch(e) {}
}

function _evictStalePositions() {
  try {
    var cutoff = Date.now() - 90 * 24 * 60 * 60 * 1000;
    for (var i = localStorage.length - 1; i >= 0; i--) {
      var key = localStorage.key(i);
      if (!key || key.indexOf(_LIB_POS_PREFIX) !== 0) continue;
      var raw = localStorage.getItem(key);
      if (!raw || /^\d+$/.test(raw)) continue; // legacy bare int: can't evict
      try {
        var data = JSON.parse(raw);
        if (data.ts && data.ts < cutoff) localStorage.removeItem(key);
      } catch(ex) {}
    }
  } catch(e) {}
}

function _clearAllFilters() {
  _filters.tradition = 'all';
  _filters.era       = 'all';
  _filters.type      = 'all';
  _filters.author    = 'all';
  var panel = document.getElementById('lb-filter-panel');
  if (panel) {
    panel.querySelectorAll('.lb-chip').forEach(function(c) {
      c.classList.toggle('lb-chip--active', c.dataset.value === 'all');
    });
  }
  _saveFilters();
  _updateClearBtn();
  _applyFilters();
  _sortFiltered();
  _renderAuthors();
  _renderList();
  _pushUrlState();
}

function _updateClearBtn() {
  var btn = document.getElementById('lb-filter-clear');
  if (!btn) return;
  var nonDefault = _filters.tradition !== 'all' || _filters.era !== 'all' ||
                   _filters.type !== 'all' || _filters.author !== 'all';
  btn.style.display = nonDefault ? '' : 'none';
}

function _pushUrlState() {
  var p = new URLSearchParams();
  if (_filters.tradition !== 'all')      p.set('tradition', _filters.tradition);
  if (_filters.era       !== 'all')      p.set('era',       _filters.era);
  if (_filters.type      !== 'all')      p.set('type',      _filters.type);
  if (_filters.author    !== 'all')      p.set('author', _filters.author);
  if (_filters.sort      !== 'year-asc') p.set('sort',      _filters.sort);
  if (_filters.q)                        p.set('q',         _filters.q);
  if (_activeId)                         p.set('doc',       _activeId);
  // Persist the current section index so back/forward and shared links land correctly
  var curSec = _activeId && _sectionIdx[_activeId] != null ? _sectionIdx[_activeId] : 0;
  if (curSec > 0)                        p.set('section',   String(curSec));
  var qs = p.toString();
  history.replaceState(null, '', qs ? '?' + qs : window.location.pathname);
}

/* ── Filter constants ────────────────────────────────────────────────────── */

// Filter levels in order highest → lowest: tradition > type.
// Author is managed by the dedicated Authors panel, not by the filter chip cascade.
// Era is independent.
var _FILTER_HIERARCHY = ['tradition', 'type'];

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
  { value: 'roman-catholic',    label: 'Roman Catholic' },
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
  { value: 'encyclical', label: 'Encyclical' },
  { value: 'father',     label: 'Father' },
  { value: 'apologetics',label: 'Apologetics' },
  { value: 'commentary', label: 'Commentary' },
  { value: 'devotional', label: 'Devotional' },
  { value: 'history',    label: 'History' },
  { value: 'liturgy',    label: 'Liturgy' },
  { value: 'sermon',     label: 'Sermon' }
];

var _TRAD_LABELS = {
  ecumenical: 'Ecumenical', reformed: 'Reformed', lutheran: 'Lutheran',
  anglican: 'Anglican', baptist: 'Baptist', anabaptist: 'Anabaptist',
  congregationalist: 'Congregationalist', methodist: 'Methodist',
  orthodox: 'Orthodox', 'roman-catholic': 'Roman Catholic', patristic: 'Patristic'
};

var _TYPE_LABELS = {
  creed: 'Creed', confession: 'Confession', catechism: 'Catechism',
  canons: 'Canons', council: 'Council', encyclical: 'Encyclical',
  father: 'Father', apologetics: 'Apologetics', commentary: 'Commentary',
  devotional: 'Devotional', history: 'History', liturgy: 'Liturgy', sermon: 'Sermon'
};

/* ── Filter panel ────────────────────────────────────────────────────────── */

function _buildFilterPanel() {
  var panel = document.getElementById('lb-filter-panel');
  if (!panel) return;

  var html = '<div class="lb-filter-clear-row"><button id="lb-filter-clear" class="lb-filter-clear" style="display:none">✕ Clear</button></div>';
  html += _chipGroup('Tradition', 'tradition', _TRADITIONS);
  html += _chipGroup('Era', 'era', _ERAS);
  html += _chipGroup('Type', 'type', _TYPES);

  panel.innerHTML = html;
  _updateClearBtn();

  var clearBtn = document.getElementById('lb-filter-clear');
  if (clearBtn) clearBtn.addEventListener('click', _clearAllFilters);

  panel.addEventListener('click', function(e) {
    var chip = e.target.closest('.lb-chip');
    if (!chip) return;
    var key   = chip.dataset.filter;
    var value = chip.dataset.value;

    if (value !== 'all' && _filters[key] === value) value = 'all';
    _filters[key] = value;

    // Reset lower-level chips in the cascade (tradition → type)
    var level = _FILTER_HIERARCHY.indexOf(key);
    if (level !== -1) {
      for (var i = level + 1; i < _FILTER_HIERARCHY.length; i++) {
        var lowerKey = _FILTER_HIERARCHY[i];
        _filters[lowerKey] = 'all';
        panel.querySelectorAll('[data-filter="' + lowerKey + '"]').forEach(function(c) {
          c.classList.toggle('lb-chip--active', c.dataset.value === 'all');
        });
      }
    }

    chip.closest('.lb-chips').querySelectorAll('.lb-chip').forEach(function(c) {
      c.classList.toggle('lb-chip--active', c.dataset.value === value);
    });

    _saveFilters();
    _updateClearBtn();
    _applyFilters();
    _sortFiltered();
    _renderAuthors();
    _renderList();
    _pushUrlState();
  });
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

/* ── Authors panel ───────────────────────────────────────────────────────── */

function _renderAuthors() {
  var panel = document.getElementById('lb-authors');
  if (!panel) return;

  // Build author groups from docs that pass tradition/era/type/search but NOT the author filter,
  // so the author list shows who's available given the other filters.
  var q = _filters.q.toLowerCase();
  var preAuthor = (_index || []).filter(function(doc) {
    if (_filters.tradition !== 'all' && doc.tradition !== _filters.tradition) return false;
    if (_filters.era       !== 'all' && doc.era       !== _filters.era)       return false;
    if (_filters.type !== 'all') {
      if (_filters.type === 'confession') {
        if (doc.type !== 'confession' && doc.type !== 'canons') return false;
      } else {
        if (doc.type !== _filters.type) return false;
      }
    }
    if (q) return (doc.title.toLowerCase().indexOf(q) !== -1) ||
                  (doc.desc  && doc.desc.toLowerCase().indexOf(q)  !== -1);
    return true;
  });

  // Group by author; null/undefined author → '_anon'
  var authorMap = {};
  var authorOrder = [];
  preAuthor.forEach(function(doc) {
    var key = doc.author || '_anon';
    if (!authorMap[key]) {
      authorMap[key] = { name: doc.author || null, tradition: doc.tradition, docs: [], minYear: doc.year || 9999 };
      authorOrder.push(key);
    }
    if ((doc.year || 9999) < authorMap[key].minYear) authorMap[key].minYear = doc.year || 9999;
    authorMap[key].docs.push(doc);
  });

  // Sort by earliest year
  authorOrder.sort(function(a, b) { return authorMap[a].minYear - authorMap[b].minYear; });

  var total = preAuthor.length;

  // Search input (value preserved across re-renders via _authorsQ)
  var searchHtml =
    '<div class="lb-authors-search-row">' +
      '<input id="lb-authors-search" class="lb-search lb-authors-search" type="search" ' +
        'placeholder="Search authors…" autocomplete="off" value="' + escHtml(_authorsQ) + '">' +
    '</div>';

  var html = '';

  // Apply authors panel search to filter visible rows (does not affect doc filtering)
  var aq = _authorsQ.toLowerCase();
  var namedKeys = authorOrder.filter(function(k) {
    if (k === '_anon') return false;
    if (aq) return authorMap[k].name.toLowerCase().indexOf(aq) !== -1;
    return true;
  });
  var hasAnon = authorOrder.indexOf('_anon') !== -1 && (!aq || 'creeds councils'.indexOf(aq) !== -1);

  // "All authors" row — always visible
  var allActive = _filters.author === 'all' ? ' lb-author-item--active' : '';
  html += '<button class="lb-author-item' + allActive + '" data-author-key="all">' +
            '<span class="lb-author-dot lb-author-dot--ecumenical"></span>' +
            '<span class="lb-author-name">All</span>' +
            '<span class="lb-author-count">' + total + '</span>' +
          '</button>';

  namedKeys.forEach(function(key) {
    var a      = authorMap[key];
    var active = _filters.author === a.name ? ' lb-author-item--active' : '';
    var trad   = a.tradition || 'ecumenical';
    var count  = a.docs.length;
    html +=
      '<button class="lb-author-item' + active + '" data-author-key="' + escHtml(a.name) + '">' +
        '<span class="lb-author-dot lb-author-dot--' + escHtml(trad) + '"></span>' +
        '<span class="lb-author-name">' + escHtml(a.name) + '</span>' +
        (count > 1 ? '<span class="lb-author-count">' + count + '</span>' : '') +
      '</button>';
  });

  // Anonymous / Ecumenical group (creeds, councils, etc.)
  if (hasAnon) {
    var anon       = authorMap['_anon'];
    var anonActive = _filters.author === '_anon' ? ' lb-author-item--active' : '';
    html += '<div class="lb-authors-separator"></div>';
    html +=
      '<button class="lb-author-item' + anonActive + '" data-author-key="_anon">' +
        '<span class="lb-author-dot lb-author-dot--ecumenical"></span>' +
        '<span class="lb-author-name">Creeds &amp; Councils</span>' +
        '<span class="lb-author-count">' + anon.docs.length + '</span>' +
      '</button>';
  }

  panel.innerHTML = searchHtml + html;

  // Wire the search input (re-attached after each re-render)
  var searchEl = document.getElementById('lb-authors-search');
  if (searchEl) {
    searchEl.addEventListener('input', function() {
      clearTimeout(_authorsSearchTimer);
      var val = searchEl.value;
      _authorsSearchTimer = setTimeout(function() {
        _authorsQ = val.trim();
        _renderAuthors();
        var newInput = document.getElementById('lb-authors-search');
        if (newInput) { newInput.focus(); newInput.value = val; }
      }, 150);
    });
  }
}

function _wireAuthors() {
  var panel = document.getElementById('lb-authors');
  if (!panel) return;
  panel.addEventListener('click', function(e) {
    var item = e.target.closest('.lb-author-item');
    if (!item) return;
    var key = item.dataset.authorKey;
    if (key === undefined) return;

    // Toggle: clicking the active author resets to 'all'
    if (key !== 'all' && _filters.author === key) key = 'all';
    _filters.author = key;

    _saveFilters();
    _updateClearBtn();
    _applyFilters();
    _sortFiltered();
    _renderAuthors();
    _renderList();
    _pushUrlState();
  });
}

/* ── Sort control ────────────────────────────────────────────────────────── */

function _buildSortControl() {
  var container = document.getElementById('lb-list-controls');
  if (!container) return;

  container.innerHTML =
    '<div class="lb-list-search-row">' +
      '<input id="lb-search" class="lb-search" type="search" placeholder="Search…" autocomplete="off" aria-label="Search documents" />' +
    '</div>' +
    '<div class="lb-sort-row">' +
      '<label class="lb-sort-label" for="lb-sort">Sort</label>' +
      '<select id="lb-sort" class="lb-sort-select">' +
        '<option value="year-asc">Year ↑</option>' +
        '<option value="year-desc">Year ↓</option>' +
        '<option value="title-asc">Title A–Z</option>' +
      '</select>' +
    '</div>';

  var searchEl = document.getElementById('lb-search');
  if (searchEl) {
    if (_filters.q) searchEl.value = _filters.q;
    searchEl.addEventListener('input', function() {
      clearTimeout(_searchTimer);
      var q = searchEl.value.trim();
      _searchTimer = setTimeout(function() {
        _filters.q = q;
        _saveFilters();
        _applyFilters();
        _sortFiltered();
        _renderAuthors();
        _renderList();
        _pushUrlState();
      }, 200);
    });
  }

  var sel = document.getElementById('lb-sort');
  if (!sel) return;
  sel.value = _filters.sort;

  sel.addEventListener('change', function() {
    _filters.sort = sel.value;
    _saveFilters();
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
    if (_filters.author !== 'all') {
      // '_anon' special key matches docs with no author field
      if (_filters.author === '_anon') {
        if (doc.author) return false;
      } else {
        if (doc.author !== _filters.author) return false;
      }
    }

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
    var suggestions = [];
    if (_filters.tradition !== 'all') suggestions.push('tradition');
    if (_filters.era       !== 'all') suggestions.push('era');
    if (_filters.type      !== 'all') suggestions.push('type');
    if (_filters.author    !== 'all') suggestions.push('author');
    if (_filters.q)                   suggestions.push('search');
    var hint = suggestions.length ? ' Try removing the ' + suggestions[0] + ' filter.' : '';
    list.innerHTML =
      '<p class="lb-list-empty">No documents match.' + hint + '</p>' +
      '<div class="lb-list-reset-row"><button class="lb-list-reset-btn" id="lb-list-reset">Reset filters</button></div>';
    var resetBtn = document.getElementById('lb-list-reset');
    if (resetBtn) resetBtn.addEventListener('click', _clearAllFilters);
    return;
  }

  var html = '';
  _filtered.forEach(function(doc) {
    var active  = doc.id === _activeId ? ' lb-list-item--active' : '';
    var yearStr = doc.year < 500 ? 'c. ' + doc.year + ' AD' : String(doc.year);
    var trad    = _TRAD_LABELS[doc.tradition] || doc.tradition;
    var type    = _TYPE_LABELS[doc.type] || doc.type;
    var overviewBadge = doc.textType === 'overview'
      ? '<span class="lb-item-overview-badge">Overview</span>'
      : '';
    var volBadge = (doc.volume_label && doc.volume !== 0)
      ? '<span class="lb-item-vol-badge">' + escHtml(doc.volume_label) + '</span>'
      : '';
    html +=
      '<button class="lb-list-item' + active + '" data-doc-id="' + escHtml(doc.id) + '" aria-label="' + escHtml(doc.title) + '" title="' + escHtml(doc.title) + '">' +
        '<span class="lb-item-abbrev lb-item-abbrev--' + escHtml(doc.tradition) + '">' + escHtml(doc.abbrev) + '</span>' +
        '<span class="lb-item-body">' +
          '<span class="lb-item-title">' + escHtml(doc.title) + overviewBadge + volBadge + '</span>' +
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
      _renderList();
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
  if (_keyListener) { document.removeEventListener('keydown', _keyListener); _keyListener = null; }
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

  panel.innerHTML =
    '<div class="lb-reader-skeleton">' +
      '<div class="lb-skeleton-line lb-skeleton-line--title"></div>' +
      '<div class="lb-skeleton-line lb-skeleton-line--meta"></div>' +
      '<div class="lb-skeleton-line"></div>' +
      '<div class="lb-skeleton-line"></div>' +
      '<div class="lb-skeleton-line lb-skeleton-line--short"></div>' +
    '</div>';

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

/* ── Paginated section progress (localStorage) ──────────────────────────── */

function _loadSectionIdx(docId) {
  try {
    var raw = localStorage.getItem(_LIB_POS_PREFIX + docId);
    if (!raw) return 0;
    if (/^\d+$/.test(raw)) return parseInt(raw, 10) || 0; // legacy bare int
    return JSON.parse(raw).idx || 0;
  } catch(e) { return 0; }
}
function _saveSectionIdx(docId, idx) {
  try { localStorage.setItem(_LIB_POS_PREFIX + docId, JSON.stringify({ idx: idx, ts: Date.now() })); } catch(e) {}
}

/* ── Reader shared header builder ────────────────────────────────────────── */

function _readerHeaderHtml(doc, entry, volHtml, extraHtml) {
  var tradition   = (entry && entry.tradition) || 'ecumenical';
  var tradLabel   = _TRAD_LABELS[tradition] || tradition;
  var typeLabel   = _TYPE_LABELS[doc.type] || doc.type;
  var year        = entry && entry.year;
  var yearStr     = year ? (year < 500 ? 'c. ' + year + ' AD' : String(year)) : '';
  var author      = entry && entry.author;
  var readerHref  = _resolve('../../library/read/') + '?doc=' + encodeURIComponent(doc.id);
  return (
    '<div class="lb-reader-header">' +
      '<div class="lb-reader-title-row">' +
        '<h2 class="lb-reader-title">' + escHtml(doc.title) + '</h2>' +
        '<div class="lb-reader-title-actions">' +
          '<button class="lb-find-btn" id="lb-find-btn" title="Find in document" aria-label="Find in document">&#x1F50D;</button>' +
          '<a class="lb-reader-open-link" href="' + readerHref + '" target="_blank" title="Open in full-screen reader">&#x2922;</a>' +
        '</div>' +
      '</div>' +
      '<div class="lb-reader-meta">' +
        '<span class="lib-badge lib-badge--' + escHtml(tradition) + '">' + escHtml(tradLabel) + '</span>' +
        (yearStr ? '<span class="lb-reader-year">'   + escHtml(yearStr) + '</span>' : '') +
        (author  ? '<span class="lb-reader-author">' + escHtml(author)  + '</span>' : '') +
        '<span class="lb-reader-type">' + escHtml(typeLabel) + '</span>' +
        '<span class="lb-section-counter" id="lb-section-counter"></span>' +
      '</div>' +
      volHtml +
      '<div class="lb-find-bar" id="lb-find-bar" hidden>' +
        '<input class="lb-find-input" id="lb-find-input" type="search" placeholder="Find in document…" autocomplete="off" aria-label="Find text">' +
        '<button class="lb-find-submit" id="lb-find-submit">Find</button>' +
        '<span class="lb-find-result" id="lb-find-result"></span>' +
        '<button class="lb-find-close" id="lb-find-close" aria-label="Close find bar">&#x2715;</button>' +
      '</div>' +
      (extraHtml || '') +
    '</div>'
  );
}

/* ── Volume switcher chip HTML ────────────────────────────────────────────── */

function _volHtml(doc, entry) {
  if (!entry || !entry.series || !_index) return '';
  var siblings = _index
    .filter(function(d) { return d.series === entry.series; })
    .sort(function(a, b) { return (a.volume || 0) - (b.volume || 0); });
  if (siblings.length < 2) return '';
  var html = '<div class="lb-reader-volumes">';
  siblings.forEach(function(sib) {
    var active = sib.id === doc.id ? ' lb-vol-chip--active' : '';
    html += '<button class="lb-vol-chip' + active + '" data-vol-id="' + escHtml(sib.id) + '">' +
              escHtml(sib.volume_label || sib.title) +
            '</button>';
  });
  return html + '</div>';
}

/* ── Wire volume chips ───────────────────────────────────────────────────── */

function _wireVolChips(panel) {
  var volBar = panel.querySelector('.lb-reader-volumes');
  if (!volBar) return;
  volBar.addEventListener('click', function(e) {
    var chip = e.target.closest('.lb-vol-chip');
    if (chip && chip.dataset.volId && chip.dataset.volId !== _activeId) _openDoc(chip.dataset.volId);
  });
}

/* ── Sub-pagination helpers for long sections (mirrors lib-reader.js) ──────── */

var _lbSubPageIdx = 0;  // current sub-page within the active book section

function _lbSplitAtH3(wrap) {
  var groups  = [];
  var current = { label: null, els: [] };
  Array.prototype.forEach.call(wrap.children, function(el) {
    if (el.tagName === 'H3') {
      if (current.els.length || current.label !== null) groups.push(current);
      current = { label: el.textContent.trim(), els: [el] };
    } else {
      current.els.push(el);
    }
  });
  if (current.els.length || current.label !== null) groups.push(current);
  return groups;
}

function _lbSubPagerHtml(subPage, numPages, label) {
  var pos = label
    ? escHtml(label) + ' <span class="lb-subpager-count">(' + (subPage + 1) + '/' + numPages + ')</span>'
    : 'Page ' + (subPage + 1) + ' of ' + numPages;
  return '<div class="lb-subpager" data-pages="' + numPages + '" data-current="' + subPage + '">' +
    '<button class="lb-subpager-btn lb-subpager-prev"' + (subPage === 0 ? ' disabled' : '') + '>&#8592;</button>' +
    '<span class="lb-subpager-pos">' + pos + '</span>' +
    '<button class="lb-subpager-btn lb-subpager-next"' + (subPage >= numPages - 1 ? ' disabled' : '') + '>&#8594;</button>' +
  '</div>';
}

/* ── Render a single section (paginated mode body) ───────────────────────── */

function _renderSectionBody(doc, idx, stripTitle, subPage) {
  var s    = doc.sections[idx];
  var html = s.html || '';
  subPage  = subPage || 0;

  var wrap = document.createElement('div');
  wrap.innerHTML = html;

  if (stripTitle) {
    var first = wrap.firstElementChild;
    if (first && first.tagName === 'H2') {
      var cls = first.className || '';
      if (cls.indexOf('lib-section__title') !== -1 || cls.indexOf('lib-chapter__title') !== -1 ||
          cls.indexOf('section-heading') !== -1 || first.textContent.trim() === (s.heading || '').trim()) {
        first.remove();
      }
    }
    // Prefer splitting at h3 chapter headings when present
    if (wrap.querySelector(':scope > h3')) {
      var groups   = _lbSplitAtH3(wrap);
      var numPages = groups.length;
      if (numPages > 1) {
        subPage = Math.max(0, Math.min(subPage, numPages - 1));
        _lbSubPageIdx = subPage;
        var group    = groups[subPage];
        var fragHtml = group.els.map(function(el) { return el.outerHTML; }).join('');
        var pager    = _lbSubPagerHtml(subPage, numPages, group.label);
        return '<section class="lb-reader-section" id="lbrs-0">' + pager + fragHtml + pager + '</section>';
      }
    }
    html = wrap.innerHTML;
  } else {
    var headingHtml = '';
    if (s.heading && !_bodyHasHeading(html, s.heading)) {
      headingHtml = '<h2 class="lb-section-heading">' + escHtml(s.heading) + '</h2>';
    }
    html = headingHtml + wrap.innerHTML;
  }

  return '<section class="lb-reader-section" id="lbrs-0">' + html + '</section>';
}

/* ── Text highlighting helpers ───────────────────────────────────────────── */

// Walks all text nodes under el and wraps every occurrence of term with <mark>.
// Returns array of inserted mark elements (used to scroll to first result).
function _highlightInEl(el, term) {
  if (!term) return [];
  var marks  = [];
  var lterm  = term.toLowerCase();
  var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null, false);
  var nodes  = [];
  var node;
  while ((node = walker.nextNode())) nodes.push(node);
  nodes.forEach(function(textNode) {
    var text = textNode.nodeValue;
    var ltxt = text.toLowerCase();
    var pos  = ltxt.indexOf(lterm);
    if (pos === -1) return;
    var frag   = document.createDocumentFragment();
    var cursor = 0;
    while (pos !== -1) {
      if (pos > cursor) frag.appendChild(document.createTextNode(text.slice(cursor, pos)));
      var mark = document.createElement('mark');
      mark.className = 'lb-find-mark';
      mark.textContent = text.slice(pos, pos + term.length);
      frag.appendChild(mark);
      marks.push(mark);
      cursor = pos + term.length;
      pos = ltxt.indexOf(lterm, cursor);
    }
    if (cursor < text.length) frag.appendChild(document.createTextNode(text.slice(cursor)));
    textNode.parentNode.replaceChild(frag, textNode);
  });
  return marks;
}

function _clearHighlights(el) {
  el.querySelectorAll('mark.lb-find-mark').forEach(function(m) {
    var parent = m.parentNode;
    if (parent) { parent.replaceChild(document.createTextNode(m.textContent), m); parent.normalize(); }
  });
}

/* ── Find bar wiring ─────────────────────────────────────────────────────── */

// goToFn: null in scroll mode, the paginated goTo(idx) closure in paginated mode.
// Calling goToFn re-renders the panel synchronously (including a fresh _wireFindBar
// call that restores _findTerm), so we must not touch panel DOM after calling it.
function _wireFindBar(panel, doc, goToFn) {
  var btn    = panel.querySelector('#lb-find-btn');
  var bar    = panel.querySelector('#lb-find-bar');
  var input  = panel.querySelector('#lb-find-input');
  var submit = panel.querySelector('#lb-find-submit');
  var result = panel.querySelector('#lb-find-result');
  var close  = panel.querySelector('#lb-find-close');
  if (!btn || !bar) return;

  // Restore search state after a paginated re-render (goToFn caused a full panel rebuild)
  if (_findTerm && doc.id === _findDocId) {
    input.value = _findTerm;
    bar.hidden  = false;
    var body = panel.querySelector('.lb-reader-body');
    if (body) {
      var restored = _highlightInEl(body, _findTerm);
      if (result) {
        if (goToFn && _findMatchSecs.length > 1) {
          result.textContent = 'Match ' + (_findCurrMatch + 1) + ' of ' + _findMatchSecs.length;
        } else if (restored.length) {
          result.textContent = restored.length + (restored.length !== 1 ? ' results' : ' result');
        }
      }
      if (restored.length) restored[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }

  btn.addEventListener('click', function() {
    bar.hidden = !bar.hidden;
    if (!bar.hidden) { input.focus(); input.select(); }
  });

  close.addEventListener('click', function() {
    bar.hidden       = true;
    _findTerm        = '';
    _findMatchSecs   = [];
    input.value      = '';
    result.textContent = '';
    var body = panel.querySelector('.lb-reader-body');
    if (body) _clearHighlights(body);
  });

  function doSearch() {
    var term = input.value.trim();
    _findTerm = term;
    var body  = panel.querySelector('.lb-reader-body');
    if (body)  _clearHighlights(body);
    if (!term) { result.textContent = ''; return; }

    if (goToFn) {
      // Paginated: find matching sections by string search, navigate to first
      _findMatchSecs = [];
      _findCurrMatch = 0;
      doc.sections.forEach(function(s, i) {
        if (s.html.toLowerCase().indexOf(term.toLowerCase()) !== -1) _findMatchSecs.push(i);
      });
      if (!_findMatchSecs.length) { result.textContent = 'Not found'; return; }
      // goToFn re-renders synchronously; the inner _wireFindBar restore handles highlight + result text
      goToFn(_findMatchSecs[0]);
    } else {
      // Scroll mode: highlight directly
      if (!body) { result.textContent = 'Not found'; return; }
      var marks = _highlightInEl(body, term);
      result.textContent = marks.length ? marks.length + (marks.length !== 1 ? ' results' : ' result') : 'Not found';
      if (marks.length) marks[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }

  submit.addEventListener('click', doSearch);
  input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter')  { e.preventDefault(); doSearch(); }
    if (e.key === 'Escape') { bar.hidden = true; }
  });
}

/* ── Main renderer ───────────────────────────────────────────────────────── */

function _renderReader(doc) {
  var entry    = _index && _index.find(function(d) { return d.id === doc.id; });
  var sections = doc.sections || [];
  var panel    = document.getElementById('lb-reader');
  if (!panel) return;

  // Reset find state when the user opens a different document
  if (doc.id !== _findDocId) {
    _findTerm      = '';
    _findMatchSecs = [];
    _findCurrMatch = 0;
    _findDocId     = doc.id;
  }

  var vHtml = _volHtml(doc, entry);

  // Clean up paginated keyboard listener before deciding on render mode
  if (_keyListener) { document.removeEventListener('keydown', _keyListener); _keyListener = null; }

  if (sections.length > _PAGINATE_THRESHOLD) {
    // ── Paginated mode ──────────────────────────────────────────────────────
    var idx = _sectionIdx[doc.id];
    if (idx === undefined) {
      idx = _loadSectionIdx(doc.id);
      _sectionIdx[doc.id] = idx;
    }
    idx = Math.max(0, Math.min(idx, sections.length - 1));

    _renderPaginatedView(doc, entry, vHtml, idx, panel);
  } else {
    // ── Scroll mode ─────────────────────────────────────────────────────────
    var multiSection = sections.length > 1;
    var tocHtml = '';
    if (multiSection) {
      tocHtml = '<nav class="lb-reader-toc"><div class="lb-reader-toc-label">Contents</div><ul class="lb-reader-toc-list">';
      sections.forEach(function(s, i) {
        tocHtml += '<li><a href="#lbrs-' + i + '">' + escHtml(s.heading) + '</a></li>';
      });
      tocHtml += '</ul></nav>';
    }
    var bodyHtml = '';
    sections.forEach(function(s, i) {
      var headingHtml = '';
      if (multiSection && s.heading && !_bodyHasHeading(s.html, s.heading)) {
        headingHtml = '<h2 class="lb-section-heading">' + escHtml(s.heading) + '</h2>';
      }
      bodyHtml += '<section class="lb-reader-section" id="lbrs-' + i + '">' + headingHtml + s.html + '</section>';
    });

    panel.innerHTML = _readerHeaderHtml(doc, entry, vHtml, tocHtml) + '<div class="lb-reader-body">' + bodyHtml + '</div>';

    var readerCol = document.querySelector('.lb-col--reader');
    if (readerCol) readerCol.scrollTop = 0;
    _wireVolChips(panel);
    wireRefLinks(panel);
    autoTagRefs();
    var body = panel.querySelector('.lb-reader-body');
    if (body) autoTagTermsWhenReady(body);
    _wireScrollSpy();
    _wireFindBar(panel, doc, null);
  }
}

function _renderPaginatedView(doc, entry, vHtml, idx, panel) {
  var sections  = doc.sections;
  var total     = sections.length;
  var s         = sections[idx];
  var useTabBar = (total <= 7);

  var navHtml;
  if (useTabBar) {
    var tabs = sections.map(function(sec, i) {
      var label = sec.heading || ('§' + (i + 1));
      if (label.length > 26) label = label.slice(0, 23) + '…';
      return '<button class="lb-sec-tab' + (i === idx ? ' lb-sec-tab--active' : '') + '" data-idx="' + i + '">' +
               escHtml(label) + '</button>';
    }).join('');
    navHtml = '<div class="lb-sec-tab-bar">' + tabs + '</div>';
  } else {
    var opts = sections.map(function(sec, i) {
      return '<option value="' + i + '"' + (i === idx ? ' selected' : '') + '>' +
               escHtml(sec.heading || ('Section ' + (i + 1))) + '</option>';
    }).join('');
    navHtml =
      '<nav class="lb-reader-pager" aria-label="Section navigation">' +
        '<button class="lb-pager-btn lb-pager-prev"' + (idx === 0 ? ' disabled' : '') + ' aria-label="Previous">&#8592;</button>' +
        '<select class="lb-pager-select" aria-label="Jump to section">' + opts + '</select>' +
        '<button class="lb-pager-btn lb-pager-next"' + (idx >= total - 1 ? ' disabled' : '') + ' aria-label="Next">&#8594;</button>' +
        '<span class="lb-pager-pos">' + (idx + 1) + '/' + total + '</span>' +
      '</nav>';
  }

  var progressHtml = useTabBar
    ? '<div class="lb-pager-progress"><span class="lb-pager-pos">' + (idx + 1) + ' / ' + total + '</span></div>'
    : '<div class="lb-pager-progress">' + (s.heading ? '<span class="lb-pager-heading">' + escHtml(s.heading) + '</span>' : '') + '</div>';

  var pagerHtml = navHtml + progressHtml;
  // Reset sub-page when navigating to a different top-level section
  _lbSubPageIdx = 0;
  var bodyHtml  = _renderSectionBody(doc, idx, true, 0);

  panel.innerHTML = _readerHeaderHtml(doc, entry, vHtml, pagerHtml) + '<div class="lb-reader-body">' + bodyHtml + '</div>';

  var readerCol = document.querySelector('.lb-col--reader');
  if (readerCol) readerCol.scrollTop = 0;

  _wireVolChips(panel);

  function goTo(newIdx) {
    newIdx = Math.max(0, Math.min(newIdx, total - 1));
    _sectionIdx[doc.id] = newIdx;
    _saveSectionIdx(doc.id, newIdx);
    _pushUrlState();
    _renderPaginatedView(doc, entry, vHtml, newIdx, panel);
  }

  // Wire sub-pager (chapter navigation within a book section)
  function wireSubPager() {
    var body = panel.querySelector('.lb-reader-body');
    if (!body) return;
    body.querySelectorAll('.lb-subpager').forEach(function(sp) {
      var numSubs = parseInt(sp.dataset.pages, 10);
      var curSub  = parseInt(sp.dataset.current, 10);
      sp.querySelector('.lb-subpager-prev').addEventListener('click', function() {
        var newSub = Math.max(0, curSub - 1);
        var body2 = panel.querySelector('.lb-reader-body');
        if (body2) {
          body2.innerHTML = _renderSectionBody(doc, idx, true, newSub);
          wireSubPager();
          body2.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
      sp.querySelector('.lb-subpager-next').addEventListener('click', function() {
        var newSub = Math.min(numSubs - 1, curSub + 1);
        var body2 = panel.querySelector('.lb-reader-body');
        if (body2) {
          body2.innerHTML = _renderSectionBody(doc, idx, true, newSub);
          wireSubPager();
          body2.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }
  wireSubPager();

  // Wire tab bar
  panel.querySelectorAll('.lb-sec-tab').forEach(function(btn) {
    btn.addEventListener('click', function() { goTo(parseInt(btn.dataset.idx, 10)); });
  });

  // Wire dropdown
  var sel = panel.querySelector('.lb-pager-select');
  if (sel) sel.addEventListener('change', function() { goTo(parseInt(sel.value, 10)); });

  var prevBtn = panel.querySelector('.lb-pager-prev');
  var nextBtn = panel.querySelector('.lb-pager-next');
  if (prevBtn) prevBtn.addEventListener('click', function() { goTo(idx - 1); });
  if (nextBtn) nextBtn.addEventListener('click', function() { goTo(idx + 1); });

  // Arrow-key navigation (detach previous listener first)
  if (_keyListener) document.removeEventListener('keydown', _keyListener);
  _keyListener = function(e) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    if (e.target && e.target.matches('input, select, textarea, [contenteditable]')) return;
    if (e.key === 'ArrowLeft')  { e.preventDefault(); goTo(idx - 1); }
    if (e.key === 'ArrowRight') { e.preventDefault(); goTo(idx + 1); }
  };
  document.addEventListener('keydown', _keyListener);

  wireRefLinks(panel);
  autoTagRefs();
  var body = panel.querySelector('.lb-reader-body');
  if (body) autoTagTermsWhenReady(body);
  _wireFindBar(panel, doc, goTo);
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

  var counter = panel.querySelector('#lb-section-counter');

  _spyListener = function() {
    // Find the last section whose top is at or above the threshold line (~100px from column top)
    var colTop    = readerCol.getBoundingClientRect().top;
    var threshold = colTop + 100;

    var activeId  = null;
    var activeIdx = -1;
    sections.forEach(function(s, i) {
      if (s.getBoundingClientRect().top <= threshold) { activeId = s.id; activeIdx = i; }
    });

    // Update "§ N of M" counter in the sticky header
    if (counter && activeIdx !== -1) {
      counter.textContent = '§ ' + (activeIdx + 1) + ' of ' + sections.length;
    }

    tocLinks.forEach(function(a) {
      var isActive = !!activeId && a.getAttribute('href') === '#' + activeId;
      a.classList.toggle('lb-toc-active', isActive);
      if (isActive) { a.setAttribute('aria-current', 'location'); }
      else           { a.removeAttribute('aria-current'); }
    });
  };

  readerCol.addEventListener('scroll', _spyListener, { passive: true });
  // Run once immediately so the first section is marked active on load
  _spyListener();
}
