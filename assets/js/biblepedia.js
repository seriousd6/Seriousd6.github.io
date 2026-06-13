/* biblepedia.js — Wiki-type Bible reference page */
'use strict';

import {
  escHtml,
  _smithLoad, _smithData, _smithMap, _smithLoadEntry,
  _isbeLoad, _isbeData, _isbeMap, _isbeLoadEntry,
  _hitchLoad, _hitchData, _hitchMap,
  _resolve, READER_URL
} from './core.js';
import {
  _dictLoad, _dictData, _dictMap,
  _dictLoadEntry,
  _naveLoad, _naveData, _naveMap,
  BIBLEPEDIA_URL
} from './library.js';
import { wireRefLinks } from './wire.js';

// ── Constants ─────────────────────────────────────────────────────────────────

var DICT_VIDX_URL     = _resolve('../../data/dictionary/verse-index/');
var BP_ARTICLES_URL   = _resolve('../../data/biblepedia/articles/');
var BP_IDX_URL        = _resolve('../../data/biblepedia/index.json');
var BP_STRONGS_URL    = _resolve('../../data/biblepedia/strongs/');

var VIDX_CACHE = {};

// ── Search dropdown state ─────────────────────────────────────────────────────

var _srDrop        = null;   // currently-open dropdown element
var _docListenOnce = false;  // whether the global mousedown handler is registered
var _searchToken   = 0;      // incremented on every _showSearchResults call to cancel stale renders

var CATEGORY_TILES = [
  { id: 'people',   label: 'People',   icon: '👤', desc: 'Biblical figures & patriarchs' },
  { id: 'places',   label: 'Places',   icon: '📍', desc: 'Cities, lands & geography' },
  { id: 'concepts', label: 'Concepts', icon: '📖', desc: 'Doctrine, themes & objects' },
  { id: 'names',    label: 'Names',    icon: '✍',  desc: 'Etymology of Biblical names' }
];

var FEATURED_SLUGS = ['jerusalem', 'covenant', 'atonement', 'faith', 'prayer', 'grace', 'messiah'];

var RECENT_KEY = 'bsw_bp_recent';
var RECENT_MAX = 8;

// ── BP index (powers home, browse, search, and quick-info) ───────────────────

var _bpIdxData    = null;
var _bpIdxMap     = null;    // id → entry
var _bpIdxLoading = null;

function _bpIdxLoad() {
  if (_bpIdxLoading) return _bpIdxLoading;
  _bpIdxLoading = fetch(BP_IDX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      _bpIdxData = data;
      _bpIdxMap  = {};
      data.forEach(function (e) { _bpIdxMap[e.id] = e; });
    })
    .catch(function () { _bpIdxData = []; _bpIdxMap = {}; });
  return _bpIdxLoading;
}

// ── Entry point ───────────────────────────────────────────────────────────────

export function initBiblepediaPage() {
  var container = document.getElementById('bp-container');
  if (!container) return;

  var params   = new URLSearchParams(window.location.search);
  var slug     = (params.get('a') || params.get('entry') || '').toLowerCase().replace(/\s+/g, '-');
  var query    = params.get('q') || '';
  var category = params.get('cat') || '';

  if (slug) {
    _showArticle(container, slug);
  } else if (query) {
    _showSearchResults(container, query);
  } else if (category) {
    _showCategory(container, category);
  } else {
    _showHome(container);
  }
}

// ── Home view ─────────────────────────────────────────────────────────────────

function _showHome(container) {
  var recent   = _getRecent();
  var featured = FEATURED_SLUGS[new Date().getDay() % FEATURED_SLUGS.length];

  container.innerHTML =
    '<div class="bp-home">' +
      '<div class="bp-home__header">' +
        '<h1 class="bp-home__title">Biblepedia</h1>' +
        '<p class="bp-home__sub">6,000+ articles on Biblical people, places, concepts, and topics</p>' +
      '</div>' +
      '<div class="bp-home__search-wrap">' +
        '<span class="bp-home__search-icon">🔍</span>' +
        '<input id="bp-home-search" type="search" class="bp-home__search" ' +
          'placeholder="Search people, places, concepts, topics…" autocomplete="off" spellcheck="false" />' +
      '</div>' +
      (recent.length ? _recentHtml(recent) : '') +
      '<div class="bp-category-tiles" id="bp-cat-tiles">' +
        CATEGORY_TILES.map(function (c) {
          return '<a class="bp-category-tile" href="' + escHtml(BIBLEPEDIA_URL + '?cat=' + c.id) + '">' +
            '<span class="bp-category-tile__icon">' + c.icon + '</span>' +
            '<span class="bp-category-tile__label">' + escHtml(c.label) + '</span>' +
            '<span class="bp-category-tile__count">' + escHtml(c.desc) + '</span>' +
          '</a>';
        }).join('') +
      '</div>' +
      '<div id="bp-featured-wrap"></div>' +
      '<div id="bp-alpha-wrap">' +
        '<p class="bp-loading-init">Loading A–Z index…</p>' +
      '</div>' +
    '</div>';

  var searchEl = container.querySelector('#bp-home-search');
  if (searchEl) {
    _ensureDocListener();
    var _srTimer;
    searchEl.addEventListener('input', function () {
      clearTimeout(_srTimer);
      var q = searchEl.value.trim().toLowerCase();
      if (q.length < 2) { _closeDrop(); return; }
      _srTimer = setTimeout(function () {
        _bpIdxLoad().then(function () { _showSearchDropdown(searchEl, container, q); });
      }, 150);
    });
    searchEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        var q = searchEl.value.trim();
        _closeDrop();
        if (q.length >= 2) _showSearchResults(container, q);
      }
      if (e.key === 'Escape') _closeDrop();
    });
  }

  _bpIdxLoad().then(function () {
    var featuredWrap = container.querySelector('#bp-featured-wrap');
    if (featuredWrap) {
      var entry = _bpIdxMap && _bpIdxMap[featured];
      if (entry && entry.brief) {
        featuredWrap.innerHTML =
          '<div class="bp-featured">' +
            '<p class="bp-featured__label">Featured Article</p>' +
            '<p class="bp-featured__title">' + escHtml(entry.term) + '</p>' +
            '<p class="bp-featured__excerpt">' + escHtml(entry.brief) + '</p>' +
            '<a class="bp-featured__link" href="' +
              escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(featured)) +
            '">Read article →</a>' +
          '</div>';
      }
    }
    _renderAlphaStrip(container.querySelector('#bp-alpha-wrap'), container);
  });
}

function _recentHtml(recent) {
  return '<div class="bp-recent">' +
    '<p class="bp-recent__label">Recently viewed</p>' +
    '<div class="bp-recent__chips">' +
    recent.map(function (r) {
      return '<a class="bp-recent__chip" href="' +
        escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(r.slug)) + '">' +
        escHtml(r.term) + '</a>';
    }).join('') +
    '</div></div>';
}

function _renderAlphaStrip(wrapper, container) {
  if (!wrapper || !_bpIdxData) return;
  var byl     = _buildOmniByLetter();
  var letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

  var html =
    '<div class="bp-alpha" id="bp-alpha">' +
    letters.map(function (l) {
      var has = byl[l] && byl[l].length > 0;
      return '<button type="button" class="bp-alpha-btn' + (!has ? ' bp-alpha-btn--empty' : '') +
        '" data-letter="' + l + '">' + l + '</button>';
    }).join('') +
    '</div>' +
    '<div id="bp-alpha-results"></div>';

  wrapper.innerHTML = html;

  wrapper.querySelectorAll('.bp-alpha-btn:not(.bp-alpha-btn--empty)').forEach(function (btn) {
    btn.addEventListener('click', function () {
      wrapper.querySelectorAll('.bp-alpha-btn').forEach(function (b) {
        b.classList.toggle('bp-alpha-btn--active', b === btn);
      });
      var items = byl[btn.dataset.letter] || [];
      _renderBrowseList(wrapper.querySelector('#bp-alpha-results'), items, container);
    });
  });

  var firstBtn = wrapper.querySelector('.bp-alpha-btn:not(.bp-alpha-btn--empty)');
  if (firstBtn) firstBtn.click();
}

// ── Category view ─────────────────────────────────────────────────────────────

function _showCategory(container, cat) {
  var info = CATEGORY_TILES.find(function (c) { return c.id === cat; });
  if (!info) { _showHome(container); return; }

  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span>' +
      '<span>' + escHtml(info.label) + '</span>' +
    '</nav>' +
    '<div class="bp-browse-header">' +
      '<h2>' + info.icon + ' ' + escHtml(info.label) + '</h2>' +
    '</div>' +
    '<p class="bp-loading-init">Loading…</p>';

  _bpIdxLoad().then(function () {
    var items = _getItemsByCategory(cat);
    var loadingEl = container.querySelector('.bp-loading-init');
    if (loadingEl) loadingEl.remove();
    _renderBrowseList(container, items, container);
  });
}

// ── Search results ────────────────────────────────────────────────────────────

function _showSearchResults(container, query) {
  var q     = query.toLowerCase().trim();
  var token = ++_searchToken;
  _closeDrop();

  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span>' +
      '<span>Search</span>' +
    '</nav>' +
    '<div class="bp-results-search-row">' +
      '<span class="bp-home__search-icon">🔍</span>' +
      '<input id="bp-results-search" type="search" class="bp-home__search" ' +
        'value="' + escHtml(query) + '" autocomplete="off" spellcheck="false" />' +
    '</div>' +
    '<p class="bp-loading-init">Searching…</p>';

  var refineEl = container.querySelector('#bp-results-search');
  if (refineEl) {
    var _rTimer;
    refineEl.addEventListener('input', function () {
      clearTimeout(_rTimer);
      var nq = refineEl.value.trim();
      _rTimer = setTimeout(function () { if (nq.length >= 2) _showSearchResults(container, nq); }, 200);
    });
    refineEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { var nq = refineEl.value.trim(); if (nq.length >= 2) _showSearchResults(container, nq); }
      if (e.key === 'Escape') _showHome(container);
    });
    refineEl.focus();
    refineEl.select();
  }

  _bpIdxLoad().then(function () {
    if (token !== _searchToken) return;
    var titleMatches = _searchTitleMatches(q);
    var titleIds     = new Set(titleMatches.map(function (e) { return e.id; }));
    var bodyMatches  = _searchBodyMatches(q, titleIds);
    var totalCount   = titleMatches.length + bodyMatches.length;

    var loadingEl = container.querySelector('.bp-loading-init');
    if (loadingEl) loadingEl.remove();

    var html =
      '<div class="bp-results-header">' +
        '<h2>Results for "' + escHtml(query) + '"</h2>' +
        '<span class="bp-results-count">' + totalCount +
          ' article' + (totalCount !== 1 ? 's' : '') + '</span>' +
        '<button type="button" class="bp-browse-back" id="bp-search-home">← Home</button>' +
      '</div>';

    if (!totalCount) {
      html +=
        '<div class="bp-results-empty">' +
          '<p>No articles found for "<strong>' + escHtml(query) + '</strong>".</p>' +
          '<p class="bp-results-empty__suggest">Try a different spelling or browse by letter.</p>' +
        '</div>';
    } else {
      if (titleMatches.length) {
        html += '<h3 class="bp-results-group-head">Title matches ' +
          '<span class="bp-results-group-count">(' + titleMatches.length + ')</span></h3>';
        html += '<div class="bp-results-list">';
        titleMatches.forEach(function (item) {
          var brief = item.brief || '';
          if (brief.length > 140) brief = brief.slice(0, 137) + '…';
          html += '<button type="button" class="bp-result-item" data-slug="' + escHtml(item.id) + '">' +
            '<div class="bp-result-item__head">' +
              _catBadgeHtml(item.category || 'concepts') +
              '<span class="bp-result-item__term">' + _highlightMatch(item.term, q) + '</span>' +
            '</div>' +
            (brief ? '<span class="bp-result-item__brief">' + escHtml(brief) + '</span>' : '') +
          '</button>';
        });
        html += '</div>';
      }
      if (bodyMatches.length) {
        html += '<h3 class="bp-results-group-head">Content matches ' +
          '<span class="bp-results-group-count">(' + bodyMatches.length + ')</span></h3>';
        html += '<div class="bp-results-list">';
        bodyMatches.forEach(function (item) {
          html += '<button type="button" class="bp-result-item" data-slug="' + escHtml(item.id) + '">' +
            '<div class="bp-result-item__head">' +
              _catBadgeHtml(item.category || 'concepts') +
              '<span class="bp-result-item__term">' + escHtml(item.term) + '</span>' +
            '</div>' +
            (item.brief ? '<span class="bp-result-item__brief">' + _excerptMatch(item.brief, q, 70) + '</span>' : '') +
          '</button>';
        });
        html += '</div>';
      }
    }

    var wrap = document.createElement('div');
    wrap.innerHTML = html;
    container.appendChild(wrap);

    wrap.querySelectorAll('.bp-result-item[data-slug]').forEach(function (btn) {
      btn.addEventListener('click', function () { _showArticle(container, btn.dataset.slug); });
    });

    var backBtn = wrap.querySelector('#bp-search-home');
    if (backBtn) backBtn.addEventListener('click', function () { _showHome(container); });
  });
}

// ── Search dropdown ───────────────────────────────────────────────────────────

function _closeDrop() {
  if (_srDrop) { _srDrop.remove(); _srDrop = null; }
}

function _ensureDocListener() {
  if (_docListenOnce) return;
  _docListenOnce = true;
  document.addEventListener('mousedown', function (e) {
    if (!_srDrop) return;
    var inp = document.getElementById('bp-home-search');
    if (inp && inp.contains(e.target)) return;
    if (_srDrop.contains(e.target)) return;
    _closeDrop();
  });
}

function _showSearchDropdown(searchEl, container, q) {
  var wrap = searchEl.closest('.bp-home__search-wrap');
  if (!wrap) return;

  var titleMatches = _searchTitleMatches(q);
  var titleIds     = new Set(titleMatches.map(function (e) { return e.id; }));
  var bodyMatches  = _searchBodyMatches(q, titleIds);
  var totalCount   = titleMatches.length + bodyMatches.length;
  var topTitle     = titleMatches.slice(0, 20);
  var topBody      = bodyMatches.slice(0, 20);

  _closeDrop();

  var drop = document.createElement('div');
  drop.className = 'bp-search-dropdown';
  var html = '';

  if (topTitle.length) {
    html += '<div class="bp-drop-section">';
    html += '<div class="bp-drop-section__head">Top title matches</div>';
    topTitle.forEach(function (e) {
      html += '<button type="button" class="bp-drop-item" data-slug="' + escHtml(e.id) + '">' +
        _catBadgeHtml(e.category || 'concepts') +
        '<span class="bp-drop-item__term">' + _highlightMatch(e.term, q) + '</span>' +
      '</button>';
    });
    html += '</div>';
  }

  if (topBody.length) {
    html += '<div class="bp-drop-section">';
    html += '<div class="bp-drop-section__head">Content matches</div>';
    topBody.forEach(function (e) {
      html += '<button type="button" class="bp-drop-item bp-drop-item--body" data-slug="' + escHtml(e.id) + '">' +
        _catBadgeHtml(e.category || 'concepts') +
        '<div class="bp-drop-item__body">' +
          '<span class="bp-drop-item__term">' + escHtml(e.term) + '</span>' +
          (e.brief ? '<span class="bp-drop-item__brief">' + _excerptMatch(e.brief, q, 50) + '</span>' : '') +
        '</div>' +
      '</button>';
    });
    html += '</div>';
  }

  if (!topTitle.length && !topBody.length) {
    html += '<div class="bp-drop-empty">No results for "<strong>' + escHtml(q) + '</strong>"</div>';
  } else {
    html += '<button type="button" class="bp-drop-all" data-q="' + escHtml(q) + '">' +
      'See all ' + totalCount + ' results for "<strong>' + escHtml(q) + '</strong>" →' +
    '</button>';
  }

  drop.innerHTML = html;
  wrap.appendChild(drop);
  _srDrop = drop;

  drop.querySelectorAll('.bp-drop-item[data-slug]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      _closeDrop();
      _showArticle(container, btn.dataset.slug);
    });
  });

  var allBtn = drop.querySelector('.bp-drop-all[data-q]');
  if (allBtn) {
    allBtn.addEventListener('click', function () {
      _closeDrop();
      _showSearchResults(container, allBtn.dataset.q);
    });
  }
}

// Returns HTML with the first occurrence of q highlighted via <mark>
function _highlightMatch(text, q) {
  var lower = text.toLowerCase();
  var idx   = lower.indexOf(q);
  if (idx < 0) return escHtml(text);
  return escHtml(text.slice(0, idx)) +
    '<mark class="bp-highlight">' + escHtml(text.slice(idx, idx + q.length)) + '</mark>' +
    escHtml(text.slice(idx + q.length));
}

// Returns an escaped excerpt of brief with the first occurrence of q highlighted
function _excerptMatch(brief, q, ctx) {
  ctx = ctx || 60;
  var lower  = brief.toLowerCase();
  var idx    = lower.indexOf(q);
  if (idx < 0) return escHtml(brief.slice(0, ctx * 2));
  var start  = Math.max(0, idx - ctx);
  var end    = Math.min(brief.length, idx + q.length + ctx);
  return (start > 0 ? '…' : '') +
    escHtml(brief.slice(start, idx)) +
    '<mark class="bp-highlight">' + escHtml(brief.slice(idx, idx + q.length)) + '</mark>' +
    escHtml(brief.slice(idx + q.length, end)) +
    (end < brief.length ? '…' : '');
}

// ── Article view ──────────────────────────────────────────────────────────────

function _showArticle(container, slug) {
  container.innerHTML = '<p class="bp-loading-init">Loading article…</p>';

  Promise.all([
    _dictLoad(), _smithLoad(), _isbeLoad(), _hitchLoad(), _bpIdxLoad()
  ]).then(function () {
    var eastonMeta = _dictMap  && (_dictMap[slug]  || _findByTitle(_dictData,  slug));
    var smithMeta  = _smithMap && (_smithMap[slug] || _findByTitle(_smithData, slug));
    var isbeMeta   = _isbeMap  && (_isbeMap[slug]  || _findByTitle(_isbeData,  slug));
    var hitch      = _hitchMap && (_hitchMap[slug] || _findHitchByTitle(slug));
    var bpIdx      = _bpIdxMap && _bpIdxMap[slug];

    if (!eastonMeta && !smithMeta && !isbeMeta) {
      _showSearchResults(container, slug.replace(/-/g, ' '));
      return;
    }

    var displayTerm = (eastonMeta && eastonMeta.term) ||
                      (smithMeta  && smithMeta.term)  ||
                      (isbeMeta   && isbeMeta.term)   ||
                      (bpIdx      && bpIdx.term)      ||
                      slug;

    _addRecent(slug, displayTerm);
    _renderArticleShell(container, slug, displayTerm, hitch, eastonMeta, smithMeta, isbeMeta, bpIdx);

    var loads = [
      eastonMeta ? _dictLoadEntry(eastonMeta.id || slug)  : Promise.resolve(null),
      smithMeta  ? _smithLoadEntry(smithMeta.id)          : Promise.resolve(null),
      isbeMeta   ? _isbeLoadEntry(isbeMeta.id)            : Promise.resolve(null),
      fetch(BP_ARTICLES_URL + slug + '.json')
        .then(function (r) { return r.ok ? r.json() : null; })
        .catch(function () { return null; })
    ];

    Promise.all(loads).then(function (bodies) {
      _populateArticleBody(
        container, slug, displayTerm,
        bodies[0], bodies[1], bodies[2],
        hitch, bodies[3], bpIdx
      );
      _loadRelatedArticles(container, bodies[0], bodies[1], bodies[2], slug);
    }).catch(function () {
      var bodyEl = container.querySelector('#bp-article-body');
      if (bodyEl) bodyEl.innerHTML = '<p>Could not load article content.</p>';
    });
  });
}


function _renderArticleShell(container, slug, term, hitch, eastonMeta, smithMeta, isbeMeta, bpIdx) {
  var cat      = (bpIdx && bpIdx.category) || _detectCategory(slug, term, hitch, eastonMeta || smithMeta || isbeMeta);
  var catBadge = _catBadgeHtml(cat);

  var badgeHtml = catBadge;
  if (hitch && cat !== 'names') {
    badgeHtml += ' <span class="bp-cat-badge bp-cat-badge--name">Name</span>';
  }

  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span>' +
      '<span class="bp-cat-badge ' + _catClass(cat) + '" style="font-size:.72rem">' +
        escHtml(cat.charAt(0).toUpperCase() + cat.slice(1)) + '</span>' +
      '<span class="bp-breadcrumb__sep">›</span>' +
      '<span>' + escHtml(term) + '</span>' +
    '</nav>' +
    '<header class="bp-article__header">' +
      '<div class="bp-article__title-row">' +
        '<h1 class="bp-article__title">' + escHtml(term) + '</h1>' +
        '<div class="bp-article__badges">' + badgeHtml + '</div>' +
      '</div>' +
      (hitch && hitch.meaning ? '<p class="bp-article__meaning">Name meaning: "' + escHtml(hitch.meaning) + '"</p>' : '') +
    '</header>' +
    '<div class="bp-article__layout">' +
      '<div class="bp-article__main">' +
        '<div id="bp-article-body"><p class="bp-loading-init">Loading…</p></div>' +
      '</div>' +
      '<aside class="bp-article__sidebar">' +
        '<div class="bp-sidebar-panel" id="bp-quickinfo-panel">' +
          '<div class="bp-sidebar-panel__head">Quick Info</div>' +
          '<div class="bp-sidebar-panel__body" id="bp-quickinfo-body">' +
            '<p class="bp-sidebar-empty">Loading…</p>' +
          '</div>' +
        '</div>' +
        '<div class="bp-sidebar-panel" id="bp-related-panel">' +
          '<div class="bp-sidebar-panel__head">Related Articles</div>' +
          '<div class="bp-sidebar-panel__body" id="bp-related-body">' +
            '<p class="bp-sidebar-empty">Loading…</p>' +
          '</div>' +
        '</div>' +
      '</aside>' +
    '</div>';
}

function _populateArticleBody(container, slug, term, eastonFull, smithFull, isbeFull, hitch, bpArticle, bpIdx) {
  var bodyEl = container.querySelector('#bp-article-body');
  if (!bodyEl) return;

  var cat = (bpIdx && bpIdx.category) || _detectCategory(slug, term, hitch, eastonFull || smithFull || isbeFull);

  // Collect refs (prefer BP key_refs)
  var allRefs  = [];
  var seenRefs = {};
  var addRef = function (r) { if (r && !seenRefs[r]) { seenRefs[r] = true; allRefs.push(r); } };
  ((bpArticle && bpArticle.key_refs) || (bpIdx && bpIdx.key_refs) || []).forEach(addRef);
  [eastonFull, smithFull, isbeFull].forEach(function (full) {
    if (full && full.refs) full.refs.forEach(addRef);
  });

  // Build body HTML: synthesis + source sections
  var html = '';
  if (bpArticle && bpArticle.intro) {
    html += '<div class="bp-synthesis">' + bpArticle.intro + '</div>';
  }

  // Easton's — open by default when no synthesis, else collapsed
  var eastonTag  = bpArticle && bpArticle.intro ? 'details' : 'div';
  var eastonHead = bpArticle && bpArticle.intro
    ? '<summary><span class="vs-dict-src-badge" data-dict-src="easton">E</span>' +
      '<span class="bp-src-section__name">Easton\'s Bible Dictionary</span>' +
      '<span class="bp-src-section__toggle">▸</span></summary>'
    : '<div class="bp-src-section__head"><span class="vs-dict-src-badge" data-dict-src="easton">E</span>' +
      '<span class="bp-src-section__name">Easton\'s Bible Dictionary</span></div>';

  if (eastonFull) {
    html += '<' + eastonTag + ' class="bp-src-section" id="easton">' +
      eastonHead +
      '<div class="bp-src-section__body" data-wikilink-src="easton">' + (eastonFull.html || '') + '</div>' +
      '</' + eastonTag + '>';
  }

  if (smithFull) {
    html += '<details class="bp-src-section" id="smith">' +
      '<summary>' +
        '<span class="vs-dict-src-badge" data-dict-src="smith">S</span>' +
        '<span class="bp-src-section__name">Smith\'s Bible Dictionary</span>' +
        '<span class="bp-src-section__toggle">▸</span>' +
      '</summary>' +
      '<div class="bp-src-section__body" data-wikilink-src="smith">' + (smithFull.html || '') + '</div>' +
    '</details>';
  }

  if (isbeFull) {
    html += '<details class="bp-src-section" id="isbe">' +
      '<summary>' +
        '<span class="vs-dict-src-badge" data-dict-src="isbe">IS</span>' +
        '<span class="bp-src-section__name">Int\'l Standard Bible Encyclopaedia</span>' +
        '<span class="bp-src-section__toggle">▸</span>' +
      '</summary>' +
      '<div class="bp-src-section__body" data-wikilink-src="isbe">' + (isbeFull.html || '') + '</div>' +
    '</details>';
  }

  bodyEl.innerHTML = html;
  wireRefLinks(bodyEl);
  bodyEl.querySelectorAll('[data-wikilink-src]').forEach(function (srcBody) {
    _wikifyLinks(srcBody, slug);
  });

  // Nave's section + Quick Info: load together to avoid double fetch
  var naveSlugs = (bpArticle && bpArticle.nave_slugs) ||
                  (bpIdx && (bpIdx.nave_topics || []).map(function (t) { return t.slug; })) ||
                  [];

  var doWithNave = function (naveTopics) {
    // Append Nave's section to body
    if (naveTopics && naveTopics.length) {
      var naveEl = document.createElement('details');
      naveEl.className = 'bp-src-section';
      naveEl.id = 'nave';
      naveEl.innerHTML =
        '<summary>' +
          '<span class="vs-dict-src-badge" data-dict-src="nave">N</span>' +
          '<span class="bp-src-section__name">Nave\'s Topical Bible</span>' +
          '<span class="bp-src-section__toggle">▸</span>' +
        '</summary>' +
        '<div class="bp-src-section__body">' + _naveBodyHtml(naveTopics) + '</div>';
      bodyEl.appendChild(naveEl);
      wireRefLinks(naveEl);
    }

    // Fetch and append Original Language Connections section
    fetch(BP_STRONGS_URL + slug + '.json')
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (data) {
        if (data && data.connections && data.connections.length) {
          var slEl = document.createElement('div');
          slEl.className = 'bp-strongs-section';
          slEl.id = 'bp-strongs';
          slEl.innerHTML = _renderStrongsSection(data.connections);
          bodyEl.appendChild(slEl);
        }
      })
      .catch(function () {});

    // Render the Quick Info sidebar
    _renderQuickInfo(container, cat, hitch, eastonFull, smithFull, isbeFull, bpArticle, bpIdx);
  };

  if (naveSlugs.length) {
    _naveLoad().then(function () {
      var topics = naveSlugs
        .map(function (s) { return _naveMap && _naveMap[s]; })
        .filter(Boolean);
      doWithNave(topics);
    }).catch(function () { doWithNave([]); });
  } else {
    doWithNave([]);
  }
}

// ── Quick Info sidebar panel ──────────────────────────────────────────────────

function _renderQuickInfo(container, cat, hitch, eastonFull, smithFull, isbeFull, bpArticle, bpIdx) {
  var panel = container.querySelector('#bp-quickinfo-body');
  if (!panel) return;

  var meaning  = (bpArticle && bpArticle.hitchcock_meaning) ||
                 (bpIdx && bpIdx.hitchcock_meaning) ||
                 (hitch && hitch.meaning);
  var keyRefs  = (bpArticle && bpArticle.key_refs) || (bpIdx && bpIdx.key_refs) || [];

  var html = '';

  // Category
  html += '<div class="bp-qi-row">' +
    '<span class="bp-qi-label">Category</span>' +
    '<div>' + _catBadgeHtml(cat) + '</div>' +
  '</div>';

  // Name meaning (Hitchcock)
  if (meaning) {
    html += '<div class="bp-qi-row">' +
      '<span class="bp-qi-label">Name</span>' +
      '<span class="bp-qi-meaning">"' + escHtml(meaning) + '"</span>' +
    '</div>';
  }

  // Key Verses
  if (keyRefs.length) {
    html += '<div class="bp-qi-row">' +
      '<span class="bp-qi-label">Key Verses</span>' +
      '<div class="bp-qi-refs">' +
      keyRefs.slice(0, 5).map(function (r) {
        return '<a class="dict-ref-chip ref" data-ref="' + escHtml(r) + '">' + escHtml(r) + '</a>';
      }).join('') +
      '</div>' +
    '</div>';
  }

  // Sources
  var srcBadges = [];
  if (eastonFull) srcBadges.push('<span class="vs-dict-src-badge" data-dict-src="easton">E</span>');
  if (smithFull)  srcBadges.push('<span class="vs-dict-src-badge" data-dict-src="smith">S</span>');
  if (isbeFull)   srcBadges.push('<span class="vs-dict-src-badge" data-dict-src="isbe">IS</span>');
  if (meaning && (hitch || (bpArticle && bpArticle.hitchcock_meaning) || (bpIdx && bpIdx.hitchcock_meaning))) {
    srcBadges.push('<span class="vs-dict-src-badge" data-dict-src="hitchcock">H</span>');
  }

  if (srcBadges.length) {
    html += '<div class="bp-qi-row bp-qi-row--last">' +
      '<span class="bp-qi-label">Sources</span>' +
      '<div class="bp-qi-sources">' + srcBadges.join('') + '</div>' +
    '</div>';
  }

  panel.innerHTML = html;
  wireRefLinks(panel);
}

// ── Nave's topic body HTML ────────────────────────────────────────────────────

function _naveBodyHtml(naveTopics) {
  if (!naveTopics || !naveTopics.length) return '';
  var html = '';
  naveTopics.forEach(function (t) {
    var verses = t.verses || [];
    var title  = t.title.charAt(0) + t.title.slice(1).toLowerCase();
    html += '<div class="bp-nave-topic">' +
      '<p class="bp-nave-topic__title">' + escHtml(title) +
        ' <span class="bp-nave-topic__count">(' + verses.length + ' verses)</span></p>' +
      '<div class="bp-nave-topic__verses">';
    verses.slice(0, 60).forEach(function (v) {
      html += '<a class="ref" data-ref="' + escHtml(v) + '">' + escHtml(v) + '</a>';
    });
    if (verses.length > 60) {
      html += '<span class="bp-nave-topic__more">… and ' + (verses.length - 60) + ' more</span>';
    }
    html += '</div></div>';
  });
  return html;
}

// ── Original Language Connections ─────────────────────────────────────────────

var _BOOK_ORDER = ['genesis','exodus','leviticus','numbers','deuteronomy','joshua','judges','ruth',
  '1samuel','2samuel','1kings','2kings','1chronicles','2chronicles','ezra','nehemiah','esther',
  'job','psalms','proverbs','ecclesiastes','songofsolomon','isaiah','jeremiah','lamentations',
  'ezekiel','daniel','hosea','joel','amos','obadiah','jonah','micah','nahum','habakkuk',
  'zephaniah','haggai','zechariah','malachi',
  'matthew','mark','luke','john','acts','romans','1corinthians','2corinthians','galatians',
  'ephesians','philippians','colossians','1thessalonians','2thessalonians','1timothy','2timothy',
  'titus','philemon','hebrews','james','1peter','2peter','1john','2john','3john','jude','revelation'];

var _BOOK_ABBREV = {genesis:'Gen',exodus:'Exo',leviticus:'Lev',numbers:'Num',deuteronomy:'Deu',
  joshua:'Jos',judges:'Jdg',ruth:'Rut','1samuel':'1Sa','2samuel':'2Sa','1kings':'1Ki',
  '2kings':'2Ki','1chronicles':'1Ch','2chronicles':'2Ch',ezra:'Ezr',nehemiah:'Neh',
  esther:'Est',job:'Job',psalms:'Ps',proverbs:'Pro',ecclesiastes:'Ecc',
  songofsolomon:'Sng',isaiah:'Isa',jeremiah:'Jer',lamentations:'Lam',ezekiel:'Ezk',
  daniel:'Dan',hosea:'Hos',joel:'Jol',amos:'Amo',obadiah:'Oba',jonah:'Jon',micah:'Mic',
  nahum:'Nah',habakkuk:'Hab',zephaniah:'Zep',haggai:'Hag',zechariah:'Zec',malachi:'Mal',
  matthew:'Mat',mark:'Mrk',luke:'Luk',john:'Jhn',acts:'Act',romans:'Rom',
  '1corinthians':'1Co','2corinthians':'2Co',galatians:'Gal',ephesians:'Eph',
  philippians:'Php',colossians:'Col','1thessalonians':'1Th','2thessalonians':'2Th',
  '1timothy':'1Ti','2timothy':'2Ti',titus:'Tit',philemon:'Phm',hebrews:'Heb',
  james:'Jas','1peter':'1Pe','2peter':'2Pe','1john':'1Jn','2john':'2Jn',
  '3john':'3Jn',jude:'Jud',revelation:'Rev'};

var _NT_START_IDX = 39; // index of 'matthew' in _BOOK_ORDER (0-based)

function _renderStrongsSection(connections) {
  var html = '<h3 class="bp-strongs-section__title">Original Language Connections</h3>';

  connections.forEach(function (c) {
    var isHeb  = c.lang === 'hebrew';
    var pct    = c.total > 0 ? Math.round((c.count / c.total) * 100) : 0;
    var langLabel = isHeb ? 'Hebrew' : 'Greek';

    // Build heat map cells
    var maxCount = Math.max.apply(null, _BOOK_ORDER.map(function (b) { return c.books[b] || 0; }));
    var ntIdx = _NT_START_IDX;
    var cells = _BOOK_ORDER.map(function (b, i) {
      var n      = c.books[b] || 0;
      var intens = maxCount > 0 ? Math.round((n / maxCount) * 100) : 0;
      var abbr   = _BOOK_ABBREV[b] || b;
      var isNT   = i >= ntIdx;
      var gap    = i === ntIdx ? '<span class="bp-sl-heatmap-gap"></span>' : '';
      return gap + '<span class="bp-sl-cell' + (n === 0 ? ' bp-sl-cell--zero' : '') +
        (isNT ? ' bp-sl-cell--nt' : '') + '"' +
        ' style="--intens:' + intens + '"' +
        ' title="' + escHtml(abbr) + (n ? ': ' + n : '') + '">' +
        '</span>';
    }).join('');

    html +=
      '<div class="bp-sl-card">' +
        '<div class="bp-sl-card__head">' +
          '<span class="bp-sl-code bp-sl-code--' + c.lang + '">' + escHtml(c.code) + '</span>' +
          '<span class="bp-sl-lemma">' + escHtml(c.lemma) + '</span>' +
          (c.translit ? '<span class="bp-sl-translit">' + escHtml(c.translit) + '</span>' : '') +
          '<span class="bp-sl-lang">' + langLabel + '</span>' +
        '</div>' +
        (c.gloss ? '<div class="bp-sl-gloss">' + escHtml(c.gloss) + '</div>' : '') +
        (c.def ? '<div class="bp-sl-def">' + escHtml(c.def) + '</div>' : '') +
        '<div class="bp-sl-stats">' +
          '<span class="bp-sl-count"><strong>' + c.count + '</strong> occurrence' + (c.count !== 1 ? 's' : '') + ' as this term</span>' +
          '<span class="bp-sl-pct">' + pct + '% of ' + c.total + ' total uses</span>' +
          '<a class="bp-sl-read-btn" href="' + escHtml(READER_URL + '?strongs=' + encodeURIComponent(c.code)) + '">' +
            'Read all in interlinear &#x2192;' +
          '</a>' +
        '</div>' +
        '<div class="bp-sl-heatmap" aria-label="Bible distribution">' + cells + '</div>' +
        '<div class="bp-sl-heatmap-legend">' +
          '<span>OT</span>' +
          '<span class="bp-sl-heatmap-legend__nt">NT</span>' +
        '</div>' +
      '</div>';
  });

  return html;
}

// ── Wiki-link injection ────────────────────────────────────────────────────────

function _wikifyLinks(root, currentSlug) {
  if (!_bpIdxData) return;

  if (!_wikiTitleMap) {
    _wikiTitleMap = {};
    _wikiTitles   = [];
    _bpIdxData.forEach(function (e) {
      if (!e.has_article) return; // only link to full articles
      var label = e.term;
      if (!label || label.length < 3) return;
      var key = label.toLowerCase();
      if (!_wikiTitleMap[key]) {
        _wikiTitleMap[key] = e.id;
        _wikiTitles.push(label);
      }
    });
    _wikiTitles.sort(function (a, b) { return b.length - a.length; });
  }

  var skipTags = new Set(['script','style','svg','canvas','select','option','textarea','input','button','a']);
  var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode: function (node) {
      var p = node.parentElement;
      if (!p) return NodeFilter.FILTER_REJECT;
      if (skipTags.has(p.tagName.toLowerCase())) return NodeFilter.FILTER_REJECT;
      if (p.closest('a, .wiki-link, [data-ref]')) return NodeFilter.FILTER_REJECT;
      if (!node.textContent.trim()) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });

  var nodes = [];
  var n;
  while ((n = walker.nextNode())) nodes.push(n);

  var usedTitles = new Set([currentSlug]);

  nodes.forEach(function (textNode) {
    _wikifyTextNode(textNode, usedTitles);
  });
}

var _wikiTitleMap = null;
var _wikiTitles   = null;

function _wikifyTextNode(textNode, usedTitles) {
  var text = textNode.textContent;
  if (text.length < 3) return;

  var result   = text;
  var modified = false;

  for (var i = 0; i < _wikiTitles.length; i++) {
    var title = _wikiTitles[i];
    var key   = title.toLowerCase();
    var slug  = _wikiTitleMap[key];
    if (!slug || usedTitles.has(slug)) continue;

    var idx = result.toLowerCase().indexOf(key);
    if (idx < 0) continue;

    var before = idx > 0 ? result[idx - 1] : ' ';
    var after  = idx + key.length < result.length ? result[idx + key.length] : ' ';
    if (/\w/.test(before) || /\w/.test(after)) continue;

    var matched = result.slice(idx, idx + title.length);
    result = result.slice(0, idx) +
      '<a class="wiki-link" href="' + escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(slug)) + '">' +
      escHtml(matched) + '</a>' +
      result.slice(idx + title.length);
    usedTitles.add(slug);
    modified = true;
    break;
  }

  if (modified) {
    var span = document.createElement('span');
    span.innerHTML = result;
    textNode.parentNode.replaceChild(span, textNode);
  }
}

// ── Related articles ──────────────────────────────────────────────────────────

function _loadRelatedArticles(container, eastonFull, smithFull, isbeFull, currentSlug) {
  var relatedEl = container.querySelector('#bp-related-body');
  if (!relatedEl) return;

  var allRefs = [];
  var seen    = {};
  [eastonFull, smithFull, isbeFull].forEach(function (full) {
    if (!full || !full.refs) return;
    full.refs.forEach(function (r) { if (!seen[r]) { seen[r] = true; allRefs.push(r); } });
  });

  if (!allRefs.length) {
    relatedEl.innerHTML = '<p class="bp-sidebar-empty">No related articles found.</p>';
    return;
  }

  var bookIds = _refsToBookIds(allRefs);
  if (!bookIds.length) {
    relatedEl.innerHTML = '<p class="bp-sidebar-empty">No related articles found.</p>';
    return;
  }

  Promise.all(bookIds.slice(0, 5).map(function (bk) { return _loadVidxDict(bk); }))
    .then(function () {
      var scores = {};
      allRefs.forEach(function (ref) {
        var parsed = _parseRefSimple(ref);
        if (!parsed) return;
        var dictIdx = VIDX_CACHE['dict:' + parsed.bookId];
        if (!dictIdx) return;
        var ch = String(parsed.ch);
        var v  = String(parsed.v);
        if (dictIdx[ch] && dictIdx[ch][v]) {
          dictIdx[ch][v].forEach(function (e) {
            if (e.id !== currentSlug) scores[e.id] = (scores[e.id] || 0) + 1;
          });
        }
      });

      var ranked = Object.keys(scores)
        .map(function (id) { return { id: id, score: scores[id] }; })
        .sort(function (a, b) { return b.score - a.score; })
        .slice(0, 6);

      if (!ranked.length) {
        relatedEl.innerHTML = '<p class="bp-sidebar-empty">No related articles found.</p>';
        return;
      }

      var html = '<div class="bp-related-list">';
      ranked.forEach(function (item) {
        var meta = _bpIdxMap && _bpIdxMap[item.id];
        if (!meta) { meta = _dictMap && _dictMap[item.id]; }
        if (!meta) return;
        var cat  = meta.category || _detectCategory(item.id, meta.term, null, meta);
        html += '<button type="button" class="bp-related-item" data-slug="' + escHtml(item.id) + '">' +
          _catBadgeHtml(cat) +
          '<span class="bp-related-item__term">' + escHtml(meta.term) + '</span>' +
          '<span class="bp-related-item__arrow">›</span>' +
        '</button>';
      });
      html += '</div>';
      relatedEl.innerHTML = html;

      relatedEl.querySelectorAll('.bp-related-item[data-slug]').forEach(function (btn) {
        btn.addEventListener('click', function () {
          _showArticle(container.closest('#bp-container') || container, btn.dataset.slug);
        });
      });
    })
    .catch(function () {
      relatedEl.innerHTML = '<p class="bp-sidebar-empty">Could not load related articles.</p>';
    });
}

function _loadVidxDict(bookId) {
  var key = 'dict:' + bookId;
  if (VIDX_CACHE[key] !== undefined) return Promise.resolve();
  VIDX_CACHE[key] = null;
  return fetch(DICT_VIDX_URL + bookId + '.json')
    .then(function (r) { return r.ok ? r.json() : {}; })
    .then(function (d) { VIDX_CACHE[key] = d; })
    .catch(function ()  { VIDX_CACHE[key] = {}; });
}

// ── Category detection ────────────────────────────────────────────────────────

var PLACE_SIGNALS  = ['city', 'town', 'village', 'sea of', 'river', 'mount ', 'mountain',
                      'valley', 'region', 'land of', 'wilderness', 'plain of', 'well of', 'gate of'];
var PEOPLE_SIGNALS = ['son of', 'daughter of', 'father of', 'mother of', 'brother of',
                      'wife of', 'king of', 'priest', 'prophet', 'apostle'];

function _detectCategory(slug, term, hitch, meta) {
  if (!meta && !hitch) return 'concepts';
  var brief = ((meta && (meta.brief || '')) + ' ' + term).toLowerCase();
  for (var i = 0; i < PLACE_SIGNALS.length;  i++) { if (brief.indexOf(PLACE_SIGNALS[i])  >= 0) return 'places'; }
  for (var j = 0; j < PEOPLE_SIGNALS.length; j++) { if (brief.indexOf(PEOPLE_SIGNALS[j]) >= 0) return 'people'; }
  if (hitch) return 'names';
  return 'concepts';
}

function _catClass(cat) {
  return 'bp-cat-badge--' + (cat === 'people' ? 'people' : cat === 'places' ? 'place' : cat === 'names' ? 'name' : 'concept');
}

function _catBadgeHtml(cat) {
  var label = cat === 'people' ? 'Person' : cat === 'places' ? 'Place' : cat === 'names' ? 'Name' : 'Concept';
  return '<span class="bp-cat-badge ' + _catClass(cat) + '">' + escHtml(label) + '</span>';
}

// ── Browse / search helpers ───────────────────────────────────────────────────

// Returns entries whose term contains q, ranked by match quality
function _searchTitleMatches(q) {
  if (!_bpIdxData) return [];
  var scored = [];
  _bpIdxData.forEach(function (e) {
    var t = e.term.toLowerCase();
    if (t.indexOf(q) < 0) return;
    var score = (t === q) ? 0 : t.startsWith(q) ? 1 : _wordStartsWith(t, q) ? 2 : 3;
    scored.push({ e: e, score: score });
  });
  scored.sort(function (a, b) {
    if (a.score !== b.score) return a.score - b.score;
    var aP = a.e.has_article ? 0 : 1, bP = b.e.has_article ? 0 : 1;
    if (aP !== bP) return aP - bP;
    return a.e.term.localeCompare(b.e.term);
  });
  return scored.map(function (r) { return r.e; });
}

// Returns entries whose brief contains q but whose term does not (title matches excluded via Set)
function _searchBodyMatches(q, excludeIds) {
  if (!_bpIdxData) return [];
  var results = [];
  _bpIdxData.forEach(function (e) {
    if (excludeIds.has(e.id)) return;
    if ((e.brief || '').toLowerCase().indexOf(q) < 0) return;
    results.push(e);
  });
  results.sort(function (a, b) {
    var aP = a.has_article ? 0 : 1, bP = b.has_article ? 0 : 1;
    if (aP !== bP) return aP - bP;
    return a.term.localeCompare(b.term);
  });
  return results;
}

function _wordStartsWith(termLower, q) {
  return termLower.split(/[\s\-]/).some(function (w) {
    return w.length > q.length && w.startsWith(q);
  });
}

function _buildOmniByLetter() {
  if (!_bpIdxData) return {};
  var byl  = {};
  var seen = {};
  _bpIdxData.forEach(function (e) {
    var letter = e.term.charAt(0).toUpperCase();
    if (!byl[letter]) byl[letter] = [];
    if (!seen[e.term.toLowerCase()]) {
      seen[e.term.toLowerCase()] = true;
      byl[letter].push(e);
    }
  });
  Object.keys(byl).forEach(function (l) {
    byl[l].sort(function (a, b) { return a.term.localeCompare(b.term); });
  });
  return byl;
}

function _getItemsByCategory(cat) {
  if (!_bpIdxData) return [];
  return _bpIdxData
    .filter(function (e) { return e.category === cat || (cat === 'names' && e.hitchcock_meaning); })
    .sort(function (a, b) { return a.term.localeCompare(b.term); });
}

function _renderBrowseList(wrapper, items, container) {
  var el = wrapper.querySelector('#bp-alpha-results') || wrapper;
  if (!items.length) {
    el.innerHTML = '<p style="color:var(--color-muted);font-style:italic;padding:.5rem">No entries found.</p>';
    return;
  }

  var html = '<div class="bp-browse-list">';
  items.slice(0, 400).forEach(function (item) {
    html += '<button type="button" class="bp-browse-item" data-slug="' + escHtml(item.id || item.slug) + '">' +
      _catBadgeHtml(item.category || 'concepts') +
      '<span class="bp-browse-item__term">' + escHtml(item.term || item.label) + '</span>' +
    '</button>';
  });
  html += '</div>';
  el.innerHTML = html;

  el.querySelectorAll('.bp-browse-item[data-slug]').forEach(function (btn) {
    btn.addEventListener('click', function () { _showArticle(container, btn.dataset.slug); });
  });
}

// ── Lookup helpers ────────────────────────────────────────────────────────────

function _findByTitle(data, slug) {
  if (!data) return null;
  var term = slug.replace(/-/g, ' ').toLowerCase();
  for (var i = 0; i < data.length; i++) {
    var e = data[i];
    if ((e.term || e.title || '').toLowerCase() === term) return e;
  }
  return null;
}

function _findHitchByTitle(slug) {
  if (!_hitchData) return null;
  var term = slug.replace(/-/g, ' ').toLowerCase();
  for (var i = 0; i < _hitchData.length; i++) {
    if (_hitchData[i].term.toLowerCase() === term) return _hitchData[i];
  }
  return null;
}

function _refsToBookIds(refs) {
  var books     = [];
  var seenBooks = {};
  var ABBREVS   = _bookAbbrevMap();
  refs.forEach(function (ref) {
    var lower  = ref.toLowerCase().split(/\s+\d/)[0].trim();
    var bookId = ABBREVS[lower];
    if (bookId && !seenBooks[bookId]) { seenBooks[bookId] = true; books.push(bookId); }
  });
  return books;
}

function _parseRefSimple(ref) {
  var m = ref.match(/^([\w\s\.]+?)\s+(\d+)(?::(\d+))?/);
  if (!m) return null;
  var bk = m[1].replace(/\.$/, '').toLowerCase().trim();
  var bookId = _bookAbbrevMap()[bk];
  if (!bookId) return null;
  return { bookId: bookId, ch: parseInt(m[2], 10), v: m[3] ? parseInt(m[3], 10) : 1 };
}

function _bookAbbrevMap() {
  return {
    'genesis': 'genesis', 'exodus': 'exodus', 'leviticus': 'leviticus',
    'numbers': 'numbers', 'deuteronomy': 'deuteronomy', 'joshua': 'joshua',
    'judges': 'judges', 'ruth': 'ruth', '1 samuel': '1samuel', '2 samuel': '2samuel',
    '1 kings': '1kings', '2 kings': '2kings', '1 chronicles': '1chronicles',
    '2 chronicles': '2chronicles', 'ezra': 'ezra', 'nehemiah': 'nehemiah',
    'esther': 'esther', 'job': 'job', 'psalms': 'psalms', 'psalm': 'psalms',
    'proverbs': 'proverbs', 'ecclesiastes': 'ecclesiastes',
    'song of solomon': 'songofsolomon', 'isaiah': 'isaiah', 'jeremiah': 'jeremiah',
    'lamentations': 'lamentations', 'ezekiel': 'ezekiel', 'daniel': 'daniel',
    'hosea': 'hosea', 'joel': 'joel', 'amos': 'amos', 'obadiah': 'obadiah',
    'jonah': 'jonah', 'micah': 'micah', 'nahum': 'nahum', 'habakkuk': 'habakkuk',
    'zephaniah': 'zephaniah', 'haggai': 'haggai', 'zechariah': 'zechariah',
    'malachi': 'malachi',
    'matthew': 'matthew', 'mark': 'mark', 'luke': 'luke', 'john': 'john',
    'acts': 'acts', 'romans': 'romans', '1 corinthians': '1corinthians',
    '2 corinthians': '2corinthians', 'galatians': 'galatians', 'ephesians': 'ephesians',
    'philippians': 'philippians', 'colossians': 'colossians',
    '1 thessalonians': '1thessalonians', '2 thessalonians': '2thessalonians',
    '1 timothy': '1timothy', '2 timothy': '2timothy', 'titus': 'titus',
    'philemon': 'philemon', 'hebrews': 'hebrews', 'james': 'james',
    '1 peter': '1peter', '2 peter': '2peter', '1 john': '1john',
    '2 john': '2john', '3 john': '3john', 'jude': 'jude', 'revelation': 'revelation',
    'gen': 'genesis', 'ex': 'exodus', 'exod': 'exodus', 'lev': 'leviticus',
    'num': 'numbers', 'deut': 'deuteronomy', 'josh': 'joshua', 'judg': 'judges',
    '1 sam': '1samuel', '2 sam': '2samuel', '1 ki': '1kings', '2 ki': '2kings',
    '1 chr': '1chronicles', '2 chr': '2chronicles', 'neh': 'nehemiah',
    'esth': 'esther', 'ps': 'psalms', 'psa': 'psalms', 'prov': 'proverbs',
    'eccl': 'ecclesiastes', 'song': 'songofsolomon', 'isa': 'isaiah',
    'jer': 'jeremiah', 'lam': 'lamentations', 'ezek': 'ezekiel', 'dan': 'daniel',
    'hos': 'hosea', 'obad': 'obadiah', 'mic': 'micah', 'nah': 'nahum',
    'hab': 'habakkuk', 'zeph': 'zephaniah', 'hag': 'haggai', 'zech': 'zechariah',
    'mal': 'malachi', 'matt': 'matthew', 'rom': 'romans',
    '1 cor': '1corinthians', '2 cor': '2corinthians', 'gal': 'galatians',
    'eph': 'ephesians', 'phil': 'philippians', 'col': 'colossians',
    '1 thess': '1thessalonians', '2 thess': '2thessalonians',
    '1 tim': '1timothy', '2 tim': '2timothy', 'tit': 'titus', 'phlm': 'philemon',
    'heb': 'hebrews', 'jas': 'james', '1 pet': '1peter', '2 pet': '2peter',
    'rev': 'revelation'
  };
}

// ── Recent articles ───────────────────────────────────────────────────────────

function _getRecent() {
  try { return JSON.parse(localStorage.getItem(RECENT_KEY) || '[]'); }
  catch (e) { return []; }
}

function _addRecent(slug, term) {
  try {
    var list = _getRecent().filter(function (r) { return r.slug !== slug; });
    list.unshift({ slug: slug, term: term });
    if (list.length > RECENT_MAX) list = list.slice(0, RECENT_MAX);
    localStorage.setItem(RECENT_KEY, JSON.stringify(list));
  } catch (e) {}
}
