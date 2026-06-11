/* biblepedia.js — Wiki-type Bible reference page */
'use strict';

import {
  escHtml,
  _smithLoad, _smithData, _smithMap, _smithLoadEntry,
  _isbeLoad, _isbeData, _isbeMap, _isbeLoadEntry,
  _hitchLoad, _hitchData, _hitchMap,
  _resolve
} from './core.js';
import {
  _dictLoad, _dictData, _dictMap,
  _dictLoadEntry,
  BIBLEPEDIA_URL
} from './library.js';
import { wireRefLinks } from './wire.js';

// ── Constants ────────────────────────────────────────────────────────────────

var DICT_VIDX_URL  = _resolve('../../data/dictionary/verse-index/');
var SMITH_VIDX_URL = _resolve('../../data/smith/verse-index/');
var ISBE_VIDX_URL  = _resolve('../../data/isbe/verse-index/');

var VIDX_CACHE = {};

var CATEGORY_TILES = [
  { id: 'people',  label: 'People',   icon: '👤', desc: 'Biblical figures & patriarchs' },
  { id: 'places',  label: 'Places',   icon: '📍', desc: 'Cities, lands & geography' },
  { id: 'concepts',label: 'Concepts', icon: '📖', desc: 'Doctrine, themes & objects' },
  { id: 'names',   label: 'Names',    icon: '✍', desc: 'Etymology of Biblical names' }
];

// Featured articles shown on the home page (rotate by day-of-week)
var FEATURED_SLUGS = ['jerusalem', 'covenant', 'atonement', 'faith', 'prayer', 'grace', 'messiah'];

var RECENT_KEY = 'bsw_bp_recent';
var RECENT_MAX = 8;

// Source definitions shared across the module
var SOURCES = [
  { key: 'easton',    badge: 'E',  label: "Easton's Bible Dictionary (M.G. Easton, 1897)"        },
  { key: 'smith',     badge: 'S',  label: "Smith's Bible Dictionary (William Smith, 1884)"       },
  { key: 'isbe',      badge: 'IS', label: "Int'l Standard Bible Encyclopaedia (James Orr, 1915)" }
];

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
  var recent = _getRecent();
  var featured = FEATURED_SLUGS[new Date().getDay() % FEATURED_SLUGS.length];

  container.innerHTML =
    '<div class="bp-home">' +
      '<div class="bp-home__header">' +
        '<h1 class="bp-home__title">Biblepedia</h1>' +
        '<p class="bp-home__sub">8,000+ articles on Biblical people, places, concepts, and topics</p>' +
      '</div>' +
      '<div class="bp-home__search-wrap">' +
        '<span class="bp-home__search-icon">🔍</span>' +
        '<input id="bp-home-search" type="search" class="bp-home__search" ' +
          'placeholder="Search people, places, concepts…" autocomplete="off" spellcheck="false" />' +
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
    var _timer;
    searchEl.addEventListener('input', function () {
      clearTimeout(_timer);
      var q = searchEl.value.trim();
      _timer = setTimeout(function () {
        if (q.length >= 2) {
          _showSearchResults(container, q);
        }
      }, 200);
    });
    searchEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        var q = searchEl.value.trim();
        if (q) _showSearchResults(container, q);
      }
    });
  }

  // Load all sources then build A-Z and featured article
  Promise.all([_dictLoad(), _smithLoad(), _isbeLoad(), _hitchLoad()]).then(function () {
    var featuredWrap = container.querySelector('#bp-featured-wrap');
    if (featuredWrap) {
      var entry = _dictMap && _dictMap[featured];
      if (entry) {
        featuredWrap.innerHTML =
          '<div class="bp-featured">' +
            '<p class="bp-featured__label">Featured Article</p>' +
            '<p class="bp-featured__title">' + escHtml(entry.term) + '</p>' +
            (entry.brief ? '<p class="bp-featured__excerpt">' + escHtml(entry.brief) + '</p>' : '') +
            '<a class="bp-featured__link" href="' + escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(featured)) + '">Read article →</a>' +
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
      return '<a class="bp-recent__chip" href="' + escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(r.slug)) + '">' +
        escHtml(r.term) + '</a>';
    }).join('') +
    '</div></div>';
}

function _renderAlphaStrip(wrapper, container) {
  if (!wrapper) return;
  var omni = _buildOmniByLetter();
  var letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  var coverage = {};
  letters.forEach(function (l) { if (omni[l] && omni[l].length) coverage[l] = true; });

  var html =
    '<div class="bp-alpha" id="bp-alpha">' +
    letters.map(function (l) {
      return '<button type="button" class="bp-alpha-btn' +
        (!coverage[l] ? ' bp-alpha-btn--empty' : '') + '" data-letter="' + l + '">' + l + '</button>';
    }).join('') +
    '</div>' +
    '<div id="bp-alpha-results"></div>';

  wrapper.innerHTML = html;

  wrapper.querySelectorAll('.bp-alpha-btn:not(.bp-alpha-btn--empty)').forEach(function (btn) {
    btn.addEventListener('click', function () {
      wrapper.querySelectorAll('.bp-alpha-btn').forEach(function (b) {
        b.classList.toggle('bp-alpha-btn--active', b === btn);
      });
      var items = omni[btn.dataset.letter] || [];
      _renderBrowseList(wrapper.querySelector('#bp-alpha-results'), items, container);
    });
  });

  // Auto-show 'A'
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

  Promise.all([_dictLoad(), _smithLoad(), _isbeLoad(), _hitchLoad()]).then(function () {
    var items = _getItemsByCategory(cat);
    container.querySelector('.bp-loading-init').remove();
    _renderBrowseList(container, items, container);
  });
}

// ── Search results ────────────────────────────────────────────────────────────

function _showSearchResults(container, query) {
  var q = query.toLowerCase().trim();
  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span>' +
      '<span>Search: ' + escHtml(query) + '</span>' +
    '</nav>' +
    '<p class="bp-loading-init">Searching…</p>';

  Promise.all([_dictLoad(), _smithLoad(), _isbeLoad(), _hitchLoad()]).then(function () {
    var results = _searchAll(q);
    var loadingEl = container.querySelector('.bp-loading-init');
    if (loadingEl) loadingEl.remove();

    var html =
      '<div class="bp-results-header">' +
        '<h2>Results for "' + escHtml(query) + '"</h2>' +
        '<span class="bp-results-count">' + results.length + ' article' + (results.length !== 1 ? 's' : '') + '</span>' +
        '<button type="button" class="bp-browse-back" id="bp-search-home">← Back</button>' +
      '</div>';

    if (results.length) {
      html += '<div class="bp-results-list">';
      results.slice(0, 120).forEach(function (item) {
        var brief = item.brief || '';
        if (brief.length > 140) brief = brief.slice(0, 137) + '…';
        html += '<button type="button" class="bp-result-item" data-slug="' + escHtml(item.slug) + '">' +
          '<div class="bp-result-item__head">' +
            _badgesHtml(item) +
            '<span class="bp-result-item__term">' + escHtml(item.label) + '</span>' +
          '</div>' +
          (brief ? '<span class="bp-result-item__brief">' + escHtml(brief) + '</span>' : '') +
        '</button>';
      });
      html += '</div>';
    } else {
      html +=
        '<div class="bp-results-empty">' +
          '<p>No articles found for "<strong>' + escHtml(query) + '</strong>".</p>' +
          '<p class="bp-results-empty__suggest">Try a different spelling or browse by letter.</p>' +
        '</div>';
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

// ── Article view ──────────────────────────────────────────────────────────────

function _showArticle(container, slug) {
  container.innerHTML =
    '<p class="bp-loading-init">Loading article…</p>';

  Promise.all([
    _dictLoad(), _smithLoad(), _isbeLoad(), _hitchLoad()
  ]).then(function () {
    // Look up entries across sources — first try exact slug, then normalized title search
    var eastonMeta = _dictMap   && (_dictMap[slug]   || _findByTitle(_dictData,  slug));
    var smithMeta  = _smithMap  && (_smithMap[slug]  || _findByTitle(_smithData, slug));
    var isbeMeta   = _isbeMap   && (_isbeMap[slug]   || _findByTitle(_isbeData,  slug));
    var hitch      = _hitchMap  && (_hitchMap[slug]  || _findHitchByTitle(slug));

    if (!eastonMeta && !smithMeta && !isbeMeta) {
      // Fall back to search
      _showSearchResults(container, slug.replace(/-/g, ' '));
      return;
    }

    var displayTerm = (eastonMeta && eastonMeta.term) ||
                      (smithMeta  && smithMeta.term)  ||
                      (isbeMeta   && isbeMeta.term)    ||
                      slug;

    // Save to recent
    _addRecent(slug, displayTerm);

    // Build the article shell immediately with placeholders
    _renderArticleShell(container, slug, displayTerm, hitch, eastonMeta, smithMeta, isbeMeta);

    // Load full entry bodies in parallel
    var loads = [
      eastonMeta ? _dictLoadEntry(eastonMeta.id || slug) : Promise.resolve(null),
      smithMeta  ? _smithLoadEntry(smithMeta.id)         : Promise.resolve(null),
      isbeMeta   ? _isbeLoadEntry(isbeMeta.id)           : Promise.resolve(null)
    ];

    Promise.all(loads).then(function (bodies) {
      var eastonFull = bodies[0];
      var smithFull  = bodies[1];
      var isbeFull   = bodies[2];

      _populateArticleBody(container, slug, displayTerm, eastonFull, smithFull, isbeFull, hitch);
      _loadRelatedArticles(container, eastonFull, smithFull, isbeFull, slug);
    }).catch(function () {
      var bodyEl = container.querySelector('#bp-article-body');
      if (bodyEl) bodyEl.innerHTML = '<p>Could not load article content.</p>';
    });
  });
}

function _renderArticleShell(container, slug, term, hitch, eastonMeta, smithMeta, isbeMeta) {
  var cat      = _detectCategory(slug, term, hitch, eastonMeta || smithMeta || isbeMeta);
  var catBadge = _catBadgeHtml(cat);

  var badgeHtml = catBadge;
  if (hitch && cat !== 'names') {
    badgeHtml += ' <span class="bp-cat-badge bp-cat-badge--name">Name</span>';
  }

  var sourceBadgesHtml = '';
  if (eastonMeta) sourceBadgesHtml += '<span class="vs-dict-src-badge" data-dict-src="easton">E</span>';
  if (smithMeta)  sourceBadgesHtml += '<span class="vs-dict-src-badge" data-dict-src="smith">S</span>';
  if (isbeMeta)   sourceBadgesHtml += '<span class="vs-dict-src-badge" data-dict-src="isbe">IS</span>';

  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span>' +
      '<span class="bp-cat-badge ' + _catClass(cat) + '" style="font-size:.72rem">' + escHtml(cat.charAt(0).toUpperCase() + cat.slice(1)) + '</span>' +
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
        '<div class="bp-sidebar-panel">' +
          '<div class="bp-sidebar-panel__head">Sources</div>' +
          '<div class="bp-sidebar-panel__body" style="display:flex;flex-direction:column;gap:.4rem;font-size:.85rem">' +
            sourceBadgesHtml +
            (eastonMeta ? ' <a href="' + escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(slug)) + '#easton" style="color:var(--color-primary);text-decoration:none;font-size:.82rem">Easton\'s</a>' : '') +
            (smithMeta  ? ' · <a href="' + escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(slug)) + '#smith" style="color:var(--color-primary);text-decoration:none;font-size:.82rem">Smith\'s</a>' : '') +
            (isbeMeta   ? ' · <a href="' + escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(slug)) + '#isbe" style="color:var(--color-primary);text-decoration:none;font-size:.82rem">ISBE</a>' : '') +
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

function _populateArticleBody(container, slug, term, eastonFull, smithFull, isbeFull, hitch) {
  var bodyEl = container.querySelector('#bp-article-body');
  if (!bodyEl) return;

  // Collect all refs from all sources
  var allRefs = [];
  var seenRefs = {};
  [eastonFull, smithFull, isbeFull].forEach(function (full) {
    if (!full || !full.refs) return;
    full.refs.forEach(function (r) {
      if (!seenRefs[r]) { seenRefs[r] = true; allRefs.push(r); }
    });
  });

  var html = '';

  // Infobox with key verses
  if (allRefs.length) {
    var topRefs = allRefs.slice(0, 6);
    html +=
      '<div class="bp-infobox">' +
        '<div class="bp-infobox__head">Quick Reference</div>' +
        '<div class="bp-infobox__body">' +
          (hitch && hitch.meaning
            ? '<div class="bp-infobox__row"><span class="bp-infobox__label">Name</span><span>' + escHtml(hitch.meaning) + '</span></div>'
            : '') +
          '<div class="bp-infobox__row">' +
            '<span class="bp-infobox__label">Key Verses</span>' +
            '<span class="bp-infobox__refs">' +
            topRefs.map(function (r) {
              return '<a class="dict-ref-chip ref" data-ref="' + escHtml(r) + '">' + escHtml(r) + '</a>';
            }).join('') +
            '</span>' +
          '</div>' +
        '</div>' +
      '</div>';
  }

  // Primary source: Easton's (full body, not collapsible)
  if (eastonFull) {
    html +=
      '<div class="bp-src-section" id="easton">' +
        '<div class="bp-src-section__head">' +
          '<span class="vs-dict-src-badge" data-dict-src="easton">E</span>' +
          '<span class="bp-src-section__name">Easton\'s Bible Dictionary</span>' +
        '</div>' +
        '<div class="bp-src-section__body" data-wikilink-src="easton">' +
          (eastonFull.html || '') +
        '</div>' +
      '</div>';
  }

  // Secondary sources: collapsible <details>
  if (smithFull) {
    html +=
      '<details class="bp-src-section" id="smith">' +
        '<summary>' +
          '<span class="vs-dict-src-badge" data-dict-src="smith">S</span>' +
          '<span class="bp-src-section__name">Smith\'s Bible Dictionary</span>' +
          '<span class="bp-src-section__toggle">▸</span>' +
        '</summary>' +
        '<div class="bp-src-section__body" data-wikilink-src="smith">' +
          (smithFull.html || '') +
        '</div>' +
      '</details>';
  }

  if (isbeFull) {
    html +=
      '<details class="bp-src-section" id="isbe">' +
        '<summary>' +
          '<span class="vs-dict-src-badge" data-dict-src="isbe">IS</span>' +
          '<span class="bp-src-section__name">Int\'l Standard Bible Encyclopaedia</span>' +
          '<span class="bp-src-section__toggle">▸</span>' +
        '</summary>' +
        '<div class="bp-src-section__body" data-wikilink-src="isbe">' +
          (isbeFull.html || '') +
        '</div>' +
      '</details>';
  }

  bodyEl.innerHTML = html;

  // Wire verse ref links
  wireRefLinks(bodyEl);

  // Run wiki-link pass on each source body
  bodyEl.querySelectorAll('[data-wikilink-src]').forEach(function (srcBody) {
    _wikifyLinks(srcBody, slug);
  });
}

// ── Wiki-link injection ────────────────────────────────────────────────────────
// Scans rendered article body text nodes for mentions of known article titles
// and wraps them as cross-links to other Biblepedia articles.

function _wikifyLinks(root, currentSlug) {
  if (!_dictData) return;

  // Build title → slug map (lazy, shared)
  if (!_wikiTitleMap) {
    _wikiTitleMap = {};
    _wikiTitles   = [];
    var addEntry = function (e) {
      var label = (e.term || e.title || '').trim();
      if (!label || label.length < 3) return;
      var slug = (e.id || '').toLowerCase();
      var key  = label.toLowerCase();
      if (!_wikiTitleMap[key]) {
        _wikiTitleMap[key] = slug;
        _wikiTitles.push(label);
      }
    };
    if (_dictData)  _dictData.forEach(addEntry);
    if (_smithData) _smithData.forEach(addEntry);
    if (_isbeData)  _isbeData.forEach(addEntry);
    // Sort longest first so multi-word titles match before their fragments
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

  var usedTitles = new Set();
  usedTitles.add(currentSlug);

  nodes.forEach(function (textNode) {
    _wikifyTextNode(textNode, usedTitles);
  });
}

var _wikiTitleMap = null;
var _wikiTitles   = null;

function _wikifyTextNode(textNode, usedTitles) {
  var text = textNode.textContent;
  if (text.length < 3) return;

  var result = text;
  var modified = false;

  // Only process titles we haven't linked yet, longest first
  for (var i = 0; i < _wikiTitles.length; i++) {
    var title = _wikiTitles[i];
    var key   = title.toLowerCase();
    var slug  = _wikiTitleMap[key];
    if (!slug || usedTitles.has(slug)) continue;

    // Word-boundary-aware search (manual, not regex, to avoid ReDoS on large title sets)
    var idx = result.toLowerCase().indexOf(key);
    if (idx < 0) continue;

    // Check word boundaries
    var before = idx > 0 ? result[idx - 1] : ' ';
    var after  = idx + key.length < result.length ? result[idx + key.length] : ' ';
    if (/\w/.test(before) || /\w/.test(after)) continue;

    // Replace first occurrence only
    var matched = result.slice(idx, idx + title.length);
    result = result.slice(0, idx) +
      '<a class="wiki-link" href="' + escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(slug)) + '">' +
      escHtml(matched) + '</a>' +
      result.slice(idx + title.length);
    usedTitles.add(slug);
    modified = true;
    break; // one link per text node to avoid nested replacement issues
  }

  if (modified) {
    var span = document.createElement('span');
    span.innerHTML = result;
    textNode.parentNode.replaceChild(span, textNode);
  }
}

// ── Related articles ──────────────────────────────────────────────────────────
// Fetches verse-index files for books referenced by the current article and
// finds the most frequently co-cited entries.

function _loadRelatedArticles(container, eastonFull, smithFull, isbeFull, currentSlug) {
  var relatedEl = container.querySelector('#bp-related-body');
  if (!relatedEl) return;

  // Collect all verse refs from all sources
  var allRefs = [];
  var seen = {};
  [eastonFull, smithFull, isbeFull].forEach(function (full) {
    if (!full || !full.refs) return;
    full.refs.forEach(function (r) {
      if (!seen[r]) { seen[r] = true; allRefs.push(r); }
    });
  });

  if (!allRefs.length) {
    relatedEl.innerHTML = '<p class="bp-sidebar-empty">No related articles found.</p>';
    return;
  }

  // Parse refs to get unique book IDs (format: "Gen. 1:1" → bookId)
  var bookIds = _refsToBookIds(allRefs);
  if (!bookIds.length) {
    relatedEl.innerHTML = '<p class="bp-sidebar-empty">No related articles found.</p>';
    return;
  }

  // Fetch verse indexes for first 5 unique books to limit requests
  var books = bookIds.slice(0, 5);
  Promise.all(books.map(function (bk) { return _loadVidxAll(bk); }))
    .then(function () {
      var scores = {};
      allRefs.forEach(function (ref) {
        var parsed = _parseRefSimple(ref);
        if (!parsed) return;
        var bk = parsed.bookId;
        var ch = String(parsed.ch);
        var v  = String(parsed.v);
        // Check Easton's index
        var dictIdx = VIDX_CACHE['dict:' + bk];
        if (dictIdx && dictIdx[ch] && dictIdx[ch][v]) {
          dictIdx[ch][v].forEach(function (e) {
            if (e.id !== currentSlug) {
              scores[e.id] = (scores[e.id] || 0) + 1;
            }
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

      // Look up display terms
      var html = '<div class="bp-related-list">';
      ranked.forEach(function (item) {
        var meta = _dictMap && _dictMap[item.id];
        if (!meta) return;
        var cat = _detectCategory(item.id, meta.term, _hitchMap && _hitchMap[item.id], meta);
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

function _loadVidxAll(bookId) {
  var dictKey  = 'dict:' + bookId;
  if (!VIDX_CACHE[dictKey]) {
    VIDX_CACHE[dictKey] = null; // mark loading
    return fetch(DICT_VIDX_URL + bookId + '.json')
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (d) { VIDX_CACHE[dictKey] = d; })
      .catch(function () { VIDX_CACHE[dictKey] = {}; });
  }
  return Promise.resolve();
}

// ── Category detection ────────────────────────────────────────────────────────

var PLACE_SIGNALS = ['city', 'town', 'village', 'sea of', 'river', 'mount ', 'mountain', 'valley', 'region', 'land of', 'wilderness', 'plain of', 'well of', 'gate of'];
var PEOPLE_SIGNALS = ['son of', 'daughter of', 'father of', 'mother of', 'brother of', 'wife of', 'king of', 'priest', 'prophet', 'apostle'];

function _detectCategory(slug, term, hitch, meta) {
  if (!meta && !hitch) return 'concepts';

  var brief = ((meta && (meta.brief || '')) + ' ' + term).toLowerCase();

  for (var i = 0; i < PLACE_SIGNALS.length; i++) {
    if (brief.indexOf(PLACE_SIGNALS[i]) >= 0) return 'places';
  }
  for (var j = 0; j < PEOPLE_SIGNALS.length; j++) {
    if (brief.indexOf(PEOPLE_SIGNALS[j]) >= 0) return 'people';
  }
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

// ── Search logic ──────────────────────────────────────────────────────────────

function _searchAll(q) {
  var results = [];
  var seen    = {};

  var addData = function (data, srcKey) {
    if (!data) return;
    data.forEach(function (e) {
      var label = e.term || e.title || '';
      var nkey  = label.toLowerCase();
      var brief = e.brief || e.meaning || '';
      if (!label) return;
      var hay = nkey + ' ' + brief.toLowerCase();
      if (hay.indexOf(q) < 0) return;
      if (seen[nkey]) return;
      seen[nkey] = true;
      results.push({
        slug:  e.id || nkey,
        label: label,
        brief: brief,
        src:   srcKey
      });
    });
  };

  addData(_dictData,  'easton');
  addData(_smithData, 'smith');
  addData(_isbeData,  'isbe');
  addData(_hitchData, 'hitchcock');

  // Sort: exact matches first, then starts-with, then contains
  results.sort(function (a, b) {
    var aLabel = a.label.toLowerCase();
    var bLabel = b.label.toLowerCase();
    var aExact = aLabel === q ? 0 : aLabel.startsWith(q) ? 1 : 2;
    var bExact = bLabel === q ? 0 : bLabel.startsWith(q) ? 1 : 2;
    if (aExact !== bExact) return aExact - bExact;
    return aLabel.localeCompare(bLabel);
  });

  return results;
}

// ── Browse helpers ────────────────────────────────────────────────────────────

function _buildOmniByLetter() {
  var byl = {};
  var seen = {};

  var addData = function (data, srcKey) {
    if (!data) return;
    data.forEach(function (e) {
      var label = e.term || e.title || '';
      if (!label) return;
      var nkey   = label.toLowerCase();
      var letter = label.charAt(0).toUpperCase();
      if (!byl[letter]) byl[letter] = [];
      if (!seen[nkey]) {
        seen[nkey] = true;
        byl[letter].push({ slug: e.id || nkey, label: label, src: srcKey, brief: e.brief || e.meaning || '' });
      }
    });
  };

  addData(_dictData,  'easton');
  addData(_smithData, 'smith');
  addData(_isbeData,  'isbe');

  Object.keys(byl).forEach(function (l) {
    byl[l].sort(function (a, b) { return a.label.localeCompare(b.label); });
  });

  return byl;
}

function _getItemsByCategory(cat) {
  var items = [];
  var seen  = {};

  var addData = function (data) {
    if (!data) return;
    data.forEach(function (e) {
      var label = e.term || e.title || '';
      if (!label) return;
      var nkey = label.toLowerCase();
      if (seen[nkey]) return;
      seen[nkey] = true;
      var hitch  = _hitchMap && _hitchMap[(e.id || '').toLowerCase()];
      var detCat = _detectCategory((e.id || '').toLowerCase(), label, hitch, e);
      if (detCat === cat || (cat === 'names' && hitch)) {
        items.push({ slug: e.id || nkey, label: label, brief: e.brief || '' });
      }
    });
  };

  addData(_dictData);
  addData(_smithData);
  items.sort(function (a, b) { return a.label.localeCompare(b.label); });
  return items;
}

function _renderBrowseList(wrapper, items, container) {
  var el = wrapper.querySelector('#bp-alpha-results') || wrapper;
  if (items.length === 0) {
    el.innerHTML = '<p style="color:var(--color-muted);font-style:italic;padding:.5rem">No entries found.</p>';
    return;
  }

  var html = '<div class="bp-browse-list">';
  items.slice(0, 400).forEach(function (item) {
    html += '<button type="button" class="bp-browse-item" data-slug="' + escHtml(item.slug) + '">' +
      '<span class="bp-browse-item__term">' + escHtml(item.label) + '</span>' +
    '</button>';
  });
  html += '</div>';
  el.innerHTML = html;

  el.querySelectorAll('.bp-browse-item[data-slug]').forEach(function (btn) {
    btn.addEventListener('click', function () { _showArticle(container, btn.dataset.slug); });
  });
}

function _badgesHtml(item) {
  if (!item.src) return '';
  return '<span class="vs-dict-src-badge" data-dict-src="' + escHtml(item.src) + '">' +
    (item.src === 'easton' ? 'E' : item.src === 'smith' ? 'S' : item.src === 'isbe' ? 'IS' : 'N') +
    '</span>';
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
  var books = [];
  var seenBooks = {};
  var BOOK_ABBREVS = _bookAbbrevMap();

  refs.forEach(function (ref) {
    var lower = ref.toLowerCase().split(/\s+\d/)[0].trim();
    var bookId = BOOK_ABBREVS[lower];
    if (bookId && !seenBooks[bookId]) {
      seenBooks[bookId] = true;
      books.push(bookId);
    }
  });
  return books;
}

function _parseRefSimple(ref) {
  // "Genesis 1:2" or "Gen. 1:2" → { bookId, ch, v }
  var m = ref.match(/^([\w\s\.]+?)\s+(\d+)(?::(\d+))?/);
  if (!m) return null;
  var bk = m[1].replace(/\.$/, '').toLowerCase().trim();
  var bookId = _bookAbbrevMap()[bk];
  if (!bookId) return null;
  return { bookId: bookId, ch: parseInt(m[2], 10), v: m[3] ? parseInt(m[3], 10) : 1 };
}

// Shared book name map — maps display names (full or abbreviated) to the
// filename stem used by verse-index files (lowercase, no spaces/periods).
// Easton's refs use full names ("Exodus 6:20"); abbreviations for other sources.
function _bookAbbrevMap() {
  return {
    // Full names (Easton's format)
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
    // Short abbreviations
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

// ── Recent articles (localStorage) ───────────────────────────────────────────

function _getRecent() {
  try {
    return JSON.parse(localStorage.getItem(RECENT_KEY) || '[]');
  } catch (e) { return []; }
}

function _addRecent(slug, term) {
  try {
    var list = _getRecent().filter(function (r) { return r.slug !== slug; });
    list.unshift({ slug: slug, term: term });
    if (list.length > RECENT_MAX) list = list.slice(0, RECENT_MAX);
    localStorage.setItem(RECENT_KEY, JSON.stringify(list));
  } catch (e) {}
}
