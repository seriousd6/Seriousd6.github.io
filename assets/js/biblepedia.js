/* biblepedia.js — Wiki-type Bible reference page */
'use strict';

import {
  escHtml,
  _smithLoad, _smithData, _smithMap, _smithLoadEntry,
  _isbeLoad, _isbeData, _isbeMap, _isbeLoadEntry,
  _hitchLoad, _hitchData, _hitchMap,
  _resolve, READER_URL, MAPS_URL
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
var BP_LINKS_URL      = _resolve('../../data/biblepedia/links.json');
// Reader page for full library texts; article JSONs carry library_refs:[{id,title,author,type}]
// for works/authors that exist in the Library (creeds, councils, church-father writings).
var LIBRARY_READ_URL  = _resolve('../../library/read/');
// Group registry: {groups:[{id,name,members:[articleId…]}]}. One source of truth for the
// bidirectional group↔member relationship — the group article authors a link_table, while each
// member article shows a "Member of" backlink computed from here (e.g. jesus-christ → The Trinity).
var BP_GROUPS_URL     = _resolve('../../data/biblepedia/groups.json');
var _bpGroupsCache    = null;
function _bpGroupsLoad() {
  if (!_bpGroupsCache) {
    _bpGroupsCache = fetch(BP_GROUPS_URL)
      .then(function (r) { return r.ok ? r.json() : { groups: [] }; })
      .catch(function () { return { groups: [] }; });
  }
  return _bpGroupsCache;
}

// Motif registry: a CROSS-CUTTING imagery/typology overlay keyed by EXISTING article id. It never
// recategorizes an article (Adam stays a Person, Exodus an Event) — it adds a secondary "Motif ·
// <Family>" badge, a Quick Info row, and (for types) a "Fulfilled in" panel. Shape: { families:{id:
// {name,order,blurb}}, modes:{id:label}, motifs:{ articleId:{ family, modes[], gloss,
// typology?:{shadow,fulfillment,fulfilled_in,refs[]} } } }. Built by /tmp/build_motifs.py; see
// working/MOTIFS_DESIGN.md. Bump DATA_VERSIONS.biblepedia in sw.js when the file changes.
var BP_MOTIFS_URL   = _resolve('../../data/biblepedia/motifs.json');
var _bpMotifsCache  = null;
function _bpMotifsLoad() {
  if (!_bpMotifsCache) {
    _bpMotifsCache = fetch(BP_MOTIFS_URL)
      .then(function (r) { return r.ok ? r.json() : { motifs: {}, families: {}, modes: {} }; })
      .catch(function () { return { motifs: {}, families: {}, modes: {} }; });
  }
  return _bpMotifsCache;
}

// Region registry: anchor-region aggregation keyed by an article id (category=regions). Shape:
// { regions: { <id>: { name, kind:power|land|sub-region, blurb, map_region|null, focus:[lat,lon,zoom],
// powers[], places[], events:[{id, at|coords}], people[] } } }. Drives the Regions browse, the hero
// map (place + event markers), and the reverse "In the region" backlink on member articles. Source of
// truth: data/biblepedia/regions.json. Bump DATA_VERSIONS.biblepedia in sw.js when the file changes.
var BP_REGIONS_URL  = _resolve('../../data/biblepedia/regions.json');
var _bpRegionsCache = null;
function _bpRegionsLoad() {
  if (!_bpRegionsCache) {
    _bpRegionsCache = fetch(BP_REGIONS_URL)
      .then(function (r) { return r.ok ? r.json() : { regions: {} }; })
      .catch(function () { return { regions: {} }; });
  }
  return _bpRegionsCache;
}

// INTENT: Reverse index { memberArticleId → [{id,name,role}] } so a member article (a place/event/
//   person) can show which region(s) it belongs to. Built once from the registry; role lets the
//   backlink read naturally ("place in", "event in", "figure of").
// CHANGE? Roles come from which list (places/events/people) the id appears in; if you add a member
//   list to the registry schema, extend the three forEach blocks here.
function _bpRegionsByMember(data) {
  var idx = {};
  var regions = (data && data.regions) || {};
  var add = function (mid, rid, name, role) {
    if (!mid) return;
    (idx[mid] = idx[mid] || []).push({ id: rid, name: name, role: role });
  };
  Object.keys(regions).forEach(function (rid) {
    var r = regions[rid];
    (r.places || []).forEach(function (p) { add(p, rid, r.name, 'place'); });
    (r.events || []).forEach(function (e) { add(e && e.id, rid, r.name, 'event'); });
    (r.people || []).forEach(function (p) { add(p, rid, r.name, 'person'); });
  });
  return idx;
}

// Place coordinates for the "Location" mini-map on place articles. Built by
// scripts/build-place-coords.py from OpenBible.info data: { places: { slug: {lat,lon,conf,
// name,source,alts?,region?} } }. conf = identified | disputed | region; an absent slug means
// the place has no known location (no map shown).
var BP_PLACECOORDS_URL = _resolve('../../data/maps/place-coords.json');
// INTENT: One lazy session-cached fetch of the place→coordinate map; only requested when a
//   place article actually renders (most articles aren't places), keeping other pages lean.
// CHANGE? Shape is { places: {…} } produced by scripts/build-place-coords.py — re-run that and
//   bump DATA_VERSIONS.maps in sw.js when the file changes. Resolves to the inner `places` object.
// VERIFY: Open ?a=jerusalem → Network shows one place-coords.json fetch; ?a=jesus-christ (a
//   concept) triggers NO such fetch.
var _placeCoords = null;
function _placeCoordsLoad() {
  if (!_placeCoords) {
    _placeCoords = fetch(BP_PLACECOORDS_URL)
      .then(function (r) { return r.ok ? r.json() : { places: {} }; })
      .then(function (d) { return (d && d.places) || {}; })
      .catch(function () { return {}; });
  }
  return _placeCoords;
}

// INTENT: Lazy-inject Leaflet's CSS+JS (same pinned 1.9.4 the Maps page uses) the first time a
//   place article needs a map, so the Biblepedia page ships no map library until it's used.
// CHANGE? Touches the global `window.L`. Keep the version + SRI hashes identical to
//   maps/index.html; if you change one, change both or tiles/markers break. Resolves once L exists.
// VERIFY: Open a place article → one leaflet.js + leaflet.css request in Network; reopening
//   another place article issues NO second request (promise is cached).
var _leafletReady = null;
function _ensureLeaflet() {
  if (window.L) return Promise.resolve();
  if (_leafletReady) return _leafletReady;
  _leafletReady = new Promise(function (resolve, reject) {
    var css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
    css.integrity = 'sha384-sHL9NAb7lN7rfvG5lfHpm643Xkcjzp4jFvuavGOndn6pjVqS6ny56CAt3nsEVT4H';
    css.crossOrigin = '';
    document.head.appendChild(css);
    var js = document.createElement('script');
    js.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
    js.integrity = 'sha384-cxOPjt7s7Iz04uaHJceBmS+qpjv2JkIHNVcuOrM+YHwZOmJGBXI00mdUXEq65HTH';
    js.crossOrigin = '';
    js.onload = function () { resolve(); };
    js.onerror = reject;
    document.head.appendChild(js);
  });
  return _leafletReady;
}

var VIDX_CACHE = {};

// ── Link graph (precomputed connections, built by scripts/build-biblepedia-links.py) ──
// INTENT: One lazy fetch of the whole link graph; powers the Connections sidebar with typed,
//   weighted neighbours + a backlink ("Referenced by N") count, replacing the old verse-only
//   "Related Articles". Cached for the session; degrades to {} so callers can fall back.
// CHANGE? links.json shape: { links: { id: { indeg, conn:[[neighborId, weight, basis]] } } }.
//   Rebuild it (build-biblepedia-links.py) whenever article intros/key_refs change.
// VERIFY: Open an article → Network shows one links.json fetch; the Connections panel lists
//   neighbours grouped by category. Block links.json → panel falls back to verse-based related.
var _bpLinks = null, _bpLinksLoading = null;
function _bpLinksLoad() {
  if (_bpLinks) return Promise.resolve(_bpLinks);
  if (_bpLinksLoading) return _bpLinksLoading;
  _bpLinksLoading = fetch(BP_LINKS_URL)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { _bpLinks = (d && d.links) ? d : { links: {} }; return _bpLinks; })
    .catch(function () { _bpLinks = { links: {} }; return _bpLinks; });
  return _bpLinksLoading;
}

// ── Search dropdown state ─────────────────────────────────────────────────────

var _srDrop        = null;   // currently-open dropdown element
var _docListenOnce = false;  // whether the global mousedown handler is registered
var _searchToken   = 0;      // incremented on every _showSearchResults call to cancel stale renders

var CATEGORY_TILES = [
  { id: 'people',   label: 'People',   icon: '👤', desc: 'Biblical figures & patriarchs' },
  { id: 'places',   label: 'Places',   icon: '📍', desc: 'Cities, lands & geography' },
  { id: 'regions',  label: 'Regions',  icon: '🗺', desc: 'Lands & powers, with maps' },
  { id: 'concepts', label: 'Concepts', icon: '📖', desc: 'Doctrine, themes & objects' },
  { id: 'names',    label: 'Names',    icon: '✍',  desc: 'Etymology of Biblical names' },
  { id: 'events',   label: 'Events',   icon: '⚡', desc: 'Key events & episodes' },
  { id: 'father',   label: 'Church Fathers', icon: '⛪', desc: 'Voices of the historic church' },
  { id: 'commentator', label: 'Commentators', icon: '🖋', desc: 'Classic Bible commentators' }
];

// Special browse views (not real categories): curated cross-cuts surfaced as home tiles and
// routed through _showCategory → _showAnchors / _showGroups.
var SPECIAL_TILES = [
  { id: 'anchors', label: 'Anchors', icon: '⚓', desc: 'The major people, places & concepts', special: true },
  { id: 'groups',  label: 'Groups',  icon: '🗂', desc: 'The Twelve, the kings, the tribes…',  special: true },
  { id: 'motifs',  label: 'Motifs',  icon: '🕊', desc: 'Imagery, metaphor & types of Christ', special: true }
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
  // Static article pages (Phase 4): /biblepedia/<slug>/ is pre-rendered at build
  // time; detect the path and enhance it exactly like the ?a= flow (the client
  // render replaces the static DOM with the enriched view).
  if (!slug) {
    var cleanPath = window.location.pathname.replace(/\/index\.html$/, '/');
    var pathMatch = cleanPath.match(/\/biblepedia\/([a-z0-9.-]+)\/$/);
    if (pathMatch) slug = pathMatch[1];
  }
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
        '<p class="bp-home__sub" id="bp-home-count">Articles on Biblical people, places, concepts, and topics</p>' +
      '</div>' +
      '<div class="bp-home__search-wrap">' +
        '<span class="bp-home__search-icon">🔍</span>' +
        '<input id="bp-home-search" type="search" class="bp-home__search" ' +
          'placeholder="Search people, places, concepts, topics…" autocomplete="off" spellcheck="false" />' +
      '</div>' +
      (recent.length ? _recentHtml(recent) : '') +
      '<div class="bp-category-tiles" id="bp-cat-tiles">' +
        CATEGORY_TILES.concat(SPECIAL_TILES).map(function (c) {
          return '<a class="bp-category-tile' + (c.special ? ' bp-category-tile--special' : '') +
              '" href="' + escHtml(BIBLEPEDIA_URL + '?cat=' + c.id) + '">' +
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
    // AUD-23: report the real article count (rounded down to the nearest 100) instead of
    // a hardcoded, inflated figure that disagreed with the index and the page meta tag.
    var countEl = container.querySelector('#bp-home-count');
    if (countEl && _bpIdxData && _bpIdxData.length) {
      var rounded = Math.floor(_bpIdxData.length / 100) * 100;
      countEl.textContent = rounded.toLocaleString() + '+ articles on Biblical people, places, concepts, and topics';
    }
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
  if (!wrapper) return;
  // UX-18: _bpIdxLoad resolves to [] on fetch failure; show an explicit message instead of
  // an empty A–Z grid (which looked like the page silently broke).
  if (!_bpIdxData || !_bpIdxData.length) {
    wrapper.innerHTML = '<p class="bp-loading-init">Couldn’t load the Biblepedia index. ' +
      'Check your connection and reload the page.</p>';
    return;
  }
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
  if (cat === 'groups')  { _showGroups(container);  return; }
  if (cat === 'anchors') { _showAnchors(container); return; }
  if (cat === 'motifs')  { _showMotifs(container);  return; }
  // 'regions' IS a real category (articles carry category=regions), but it gets a custom
  // registry-driven browse (grouped by kind, with member counts) instead of the generic A–Z list.
  if (cat === 'regions') { _showRegions(container); return; }
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

// ── Groups view (browse all curated groups) ───────────────────────────────────
// INTENT: A home "Groups" tile lands here — every group from groups.json as a card linking to its
//   hub article, with each member linked directly so the reader can dive in from the overview.
function _showGroups(container) {
  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span><span>Groups</span>' +
    '</nav>' +
    '<div class="bp-browse-header"><h2>🗂 Groups</h2></div>' +
    '<p class="bp-browse-sub">Sets of related articles — the Twelve Apostles, the kings, the tribes, ' +
      'and more. Open a group, or jump straight to a member.</p>' +
    '<p class="bp-loading-init">Loading…</p>';

  Promise.all([_bpGroupsLoad(), _bpIdxLoad()]).then(function (res) {
    var groups = ((res[0] && res[0].groups) || []).slice().sort(function (a, b) {
      return (b.members || []).length - (a.members || []).length;
    });
    var loadingEl = container.querySelector('.bp-loading-init');
    if (loadingEl) loadingEl.remove();

    var html = '<div class="bp-groups-grid">';
    groups.forEach(function (g) {
      var members = (g.members || []).map(function (mid) {
        var e = _bpIdxMap && _bpIdxMap[mid];
        var name = (e && e.term) || mid.replace(/-/g, ' ');
        return '<a class="wiki-link" href="' + escHtml(BIBLEPEDIA_URL + '?a=' +
          encodeURIComponent(mid)) + '">' + escHtml(name) + '</a>';
      }).join('');
      html += '<div class="bp-group-card">' +
        '<a class="bp-group-card__title" href="' + escHtml(BIBLEPEDIA_URL + '?a=' +
          encodeURIComponent(g.id)) + '">' + escHtml(g.name) + '</a>' +
        '<span class="bp-group-card__count">' + (g.members || []).length + ' members</span>' +
        '<div class="bp-group-card__members">' + members + '</div>' +
      '</div>';
    });
    html += '</div>';
    container.insertAdjacentHTML('beforeend', html);
  });
}

// ── Motifs view (browse biblical imagery & typology by family) ────────────────
// INTENT: A home "Motifs" tile lands here — every motif from motifs.json grouped by family
//   (Elemental, Fauna, Cultic…), each linking to its article. Type motifs are flagged so the
//   reader can scan which images are types/shadows fulfilled in Christ. Reverse of the per-article
//   motif badge: this is the cross-cutting index of the overlay.
// VERIFY: Open ?cat=motifs → family sections with linked motifs; "lamb" shows a "type" flag.
function _showMotifs(container) {
  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span><span>Motifs</span>' +
    '</nav>' +
    '<div class="bp-browse-header"><h2>🕊 Motifs &amp; Types</h2></div>' +
    '<p class="bp-browse-sub">Recurring biblical imagery, metaphors, and types — images that thread ' +
      'through Scripture (water, vine, lamb, temple) and shadows fulfilled in Christ. ' +
      '<span class="bp-motif-flag bp-motif-flag--type">Type</span> marks an Old-Testament pattern ' +
      'fulfilled in the New.</p>' +
    '<p class="bp-loading-init">Loading…</p>';

  Promise.all([_bpMotifsLoad(), _bpIdxLoad()]).then(function (res) {
    var data = res[0] || {};
    var motifs = data.motifs || {};
    var families = data.families || {};
    var loadingEl = container.querySelector('.bp-loading-init');
    if (loadingEl) loadingEl.remove();

    // Bucket motif ids by family, then order families by their `order` field.
    var byFam = {};
    Object.keys(motifs).forEach(function (id) {
      var fam = motifs[id].family || 'other';
      (byFam[fam] = byFam[fam] || []).push(id);
    });
    var famIds = Object.keys(byFam).sort(function (a, b) {
      return ((families[a] && families[a].order) || 99) - ((families[b] && families[b].order) || 99);
    });

    var html = '<div class="bp-motif-families">';
    famIds.forEach(function (fam) {
      var info = families[fam] || { name: fam };
      var ids = byFam[fam].sort(function (a, b) {
        var na = (_bpIdxMap && _bpIdxMap[a] && _bpIdxMap[a].term) || a;
        var nb = (_bpIdxMap && _bpIdxMap[b] && _bpIdxMap[b].term) || b;
        return na.localeCompare(nb);
      });
      var chips = ids.map(function (id) {
        var m = motifs[id];
        var name = (_bpIdxMap && _bpIdxMap[id] && _bpIdxMap[id].term) || id.replace(/-/g, ' ');
        var isType = (m.modes || []).indexOf('type') !== -1;
        return '<a class="bp-motif-chip" href="' +
          escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(id)) + '" title="' +
          escHtml(m.gloss || '') + '">' + escHtml(name) +
          (isType ? '<span class="bp-motif-flag bp-motif-flag--type">type</span>' : '') +
        '</a>';
      }).join('');
      html += '<section class="bp-motif-family">' +
        '<h3 class="bp-motif-family__name">' + escHtml(info.name) +
          '<span class="bp-motif-family__count">' + ids.length + '</span></h3>' +
        (info.blurb ? '<p class="bp-motif-family__blurb">' + escHtml(info.blurb) + '</p>' : '') +
        '<div class="bp-motif-chips">' + chips + '</div>' +
      '</section>';
    });
    html += '</div>';
    container.insertAdjacentHTML('beforeend', html);
  });
}

// ── Regions view (browse anchor regions by kind) ──────────────────────────────
// INTENT: The "Regions" tile lands here — every region from regions.json grouped by kind (Powers,
//   Lands, Sub-regions), each a chip linking to its article, with a count of mapped members so the
//   reader sees at a glance how rich each region's hub is. Reverse of the per-article hero map.
// VERIFY: Open ?cat=regions → three kind sections; "Egypt" chip under Powers, "Galilee" under Lands.
var REGION_KINDS = [
  { id: 'power',      name: 'Regional Powers', blurb: 'Empires and kingdoms that ruled the biblical world.' },
  { id: 'land',       name: 'Lands',           blurb: 'The major lands and districts of the biblical story.' },
  { id: 'sub-region', name: 'Sub-regions',     blurb: 'Smaller territories and neighbouring nations.' }
];
function _showRegions(container) {
  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span><span>Regions</span>' +
    '</nav>' +
    '<div class="bp-browse-header"><h2>🗺 Regions</h2></div>' +
    '<p class="bp-browse-sub">Anchor regions of Scripture — each gathers its places, the events that ' +
      'happened there, and the people who passed through, around an interactive map.</p>' +
    '<p class="bp-loading-init">Loading…</p>';

  Promise.all([_bpRegionsLoad(), _bpIdxLoad()]).then(function (res) {
    var regions = (res[0] && res[0].regions) || {};
    var loadingEl = container.querySelector('.bp-loading-init');
    if (loadingEl) loadingEl.remove();

    // Bucket region ids by kind; unknown kinds fall under Sub-regions so nothing is dropped.
    var byKind = {};
    Object.keys(regions).forEach(function (id) {
      var k = regions[id].kind || 'sub-region';
      (byKind[k] = byKind[k] || []).push(id);
    });

    var html = '<div class="bp-region-kinds">';
    REGION_KINDS.forEach(function (kind) {
      var ids = (byKind[kind.id] || []).sort(function (a, b) {
        return (regions[a].name || a).localeCompare(regions[b].name || b);
      });
      if (!ids.length) return;
      var chips = ids.map(function (id) {
        var r = regions[id];
        var n = (r.places || []).length + (r.events || []).length + (r.people || []).length;
        return '<a class="bp-region-chip" href="' +
          escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(id)) + '" title="' +
          escHtml(r.blurb || '') + '">' + escHtml(r.name || id.replace(/-/g, ' ')) +
          '<span class="bp-region-chip__count">' + n + '</span></a>';
      }).join('');
      html += '<section class="bp-region-kind">' +
        '<h3 class="bp-region-kind__name">' + escHtml(kind.name) +
          '<span class="bp-region-kind__count">' + ids.length + '</span></h3>' +
        '<p class="bp-region-kind__blurb">' + escHtml(kind.blurb) + '</p>' +
        '<div class="bp-region-chips">' + chips + '</div>' +
      '</section>';
    });
    html += '</div>';
    container.insertAdjacentHTML('beforeend', html);
  });
}

// ── Anchors view (the major people, places & concepts) ────────────────────────
// INTENT: A home "Anchors" tile lands here — the most-connected articles (by link-graph in-degree)
//   grouped into Concepts / People / Places, so the foundational topics of the faith are one click
//   away. A small stoplist drops language/meta terms that rank high but aren't true anchors.
var ANCHOR_STOP = { 'hebrew': 1, 'greek': 1, 'testament': 1, 'new-testament': 1, 'old-testament': 1,
  'scripture': 1, 'book': 1, 'post': 1, 'beyond': 1, 'tradition': 1,
  'quotations-in-the-new-testament': 1 };
function _showAnchors(container) {
  container.innerHTML =
    '<nav class="bp-breadcrumb">' +
      '<a href="' + escHtml(BIBLEPEDIA_URL) + '">Biblepedia</a>' +
      '<span class="bp-breadcrumb__sep">›</span><span>Anchors</span>' +
    '</nav>' +
    '<div class="bp-browse-header"><h2>⚓ Anchors</h2></div>' +
    '<p class="bp-browse-sub">The major people, places, and concepts of the faith — the most ' +
      'connected articles, gathered in one place.</p>' +
    '<p class="bp-loading-init">Loading…</p>';

  Promise.all([_bpLinksLoad(), _bpIdxLoad()]).then(function (res) {
    var anchors = (res[0] && res[0].anchors) || [];
    var buckets = { concepts: [], people: [], places: [] };
    anchors.forEach(function (pair) {
      var id = pair[0];
      if (ANCHOR_STOP[id]) return;
      var e = _bpIdxMap && _bpIdxMap[id];
      if (!e || e.redirect || !e.has_article) return;
      var cat = _normCat(e.category);
      if (buckets[cat] && buckets[cat].length < 30) buckets[cat].push(e);
    });
    var loadingEl = container.querySelector('.bp-loading-init');
    if (loadingEl) loadingEl.remove();

    var sections = [['concepts', '📖 Concepts'], ['people', '👤 People'], ['places', '📍 Places']];
    var html = '';
    sections.forEach(function (s) {
      var items = buckets[s[0]];
      if (!items.length) return;
      html += '<div class="bp-anchor-section"><h3 class="bp-anchor-section__head">' + s[1] + '</h3>' +
        '<div class="bp-browse-list">' +
        items.map(function (e) {
          return '<button type="button" class="bp-browse-item" data-slug="' + escHtml(e.id) + '">' +
            _catBadgeHtml(e.category) +
            '<span class="bp-browse-item__term">' + escHtml(e.term) + '</span>' +
          '</button>';
        }).join('') +
        '</div></div>';
    });
    container.insertAdjacentHTML('beforeend', html);
    container.querySelectorAll('.bp-browse-item[data-slug]').forEach(function (btn) {
      btn.addEventListener('click', function () { _showArticle(container, btn.dataset.slug); });
    });
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
              _akaHtml(item) +
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
        _akaHtml(e) +
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
    // INTENT: Synonym articles (e.g. Golgotha/Skull → Calvary) are merged into one canonical
    //   article; each alias keeps a lightweight index entry carrying {redirect:<canonicalId>}
    //   but no article JSON file. Follow it here so every pre-existing ?a=<alias> link,
    //   recent-history slug, Connections-graph edge, and term-tag lands on the one canonical page.
    // CHANGE? Redirect targets live in index.json alias entries (has_article:false, redirect:id),
    //   produced by the merge pass recorded in data/biblepedia/merges.json. If you rename a
    //   canonical id you must update its aliases' redirect fields (and merges.json) to match.
    // VERIFY: Open ?a=golgotha — the Calvary article renders and the console shows no 404 for
    //   golgotha.json (the fetch below uses the resolved canonical slug).
    // Follow the redirect CHAIN (merge alias → canonical → umbrella parent), capturing any
    // `anchor` along the way: e.g. atonement-day-of → day-of-atonement → feast#day-of-atonement,
    // or ?a=wrath → god#wrath. Bounded to avoid cycles.
    var _facetAnchor = '';
    for (var _hop = 0; _hop < 6 && _bpIdxMap && _bpIdxMap[slug] && _bpIdxMap[slug].redirect &&
                       _bpIdxMap[_bpIdxMap[slug].redirect]; _hop++) {
      if (_bpIdxMap[slug].anchor) _facetAnchor = _bpIdxMap[slug].anchor;
      slug = _bpIdxMap[slug].redirect;
    }
    // A direct ?a=parent#anchor link (hash) targets a facet section too.
    if (!_facetAnchor && window.location.hash) _facetAnchor = window.location.hash.slice(1);

    var eastonMeta = _dictMap  && (_dictMap[slug]  || _findByTitle(_dictData,  slug));
    var smithMeta  = _smithMap && (_smithMap[slug] || _findByTitle(_smithData, slug));
    var isbeMeta   = _isbeMap  && (_isbeMap[slug]  || _findByTitle(_isbeData,  slug));
    var hitch      = _hitchMap && (_hitchMap[slug] || _findHitchByTitle(slug));
    var bpIdx      = _bpIdxMap && _bpIdxMap[slug];

    // Render if ANY source has the term — including a Biblepedia-only article (bpIdx),
    // e.g. Cloud of Witnesses church fathers, which are absent from the biblical
    // dictionaries Easton/Smith/ISBE. Without the bpIdx check those fall through to
    // search and never open.
    if (!eastonMeta && !smithMeta && !isbeMeta && !bpIdx) {
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
      _loadConnections(container, slug, bodies);
      if (_facetAnchor) _openFacet(container, _facetAnchor);
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
        '<div class="bp-sidebar-panel" id="bp-library-panel" style="display:none">' +
          '<div class="bp-sidebar-panel__head">In the Library</div>' +
          '<div class="bp-sidebar-panel__body" id="bp-library-body"></div>' +
        '</div>' +
        '<div class="bp-sidebar-panel" id="bp-related-panel">' +
          '<div class="bp-sidebar-panel__head">Connections</div>' +
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

  // Prefer the article FILE's own category over index.json. The index is rebuilt only in the
  // deferred post-loop batch, so a freshly promoted region (egypt: places→regions in its file but
  // still "places" in a stale index) must render from the file or its hero map/badge won't show.
  var cat = (bpArticle && bpArticle.category) || (bpIdx && bpIdx.category) ||
            _detectCategory(slug, term, hitch, eastonFull || smithFull || isbeFull);
  // If the file's category differs from what the shell rendered (built from the stale index before
  // the file loaded), correct the breadcrumb + header badges so the page is internally consistent.
  if (bpArticle && bpArticle.category && (!bpIdx || bpIdx.category !== bpArticle.category)) {
    _syncCatBadges(container, cat);
  }

  // "In the Library" panel — surfaces full-text Library docs for articles that ARE a Library
  // work (e.g. a creed) or are a church father whose writings are in the Library.
  _renderLibraryPanel(container, bpArticle);

  // "Location" panel — interactive mini-map for place articles (coords from place-coords.json).
  _renderLocationPanel(container, slug, cat, term);

  // Collect refs (prefer BP key_refs)
  var allRefs  = [];
  var seenRefs = {};
  var addRef = function (r) { if (r && !seenRefs[r]) { seenRefs[r] = true; allRefs.push(r); } };
  ((bpArticle && bpArticle.key_refs) || (bpIdx && bpIdx.key_refs) || []).forEach(addRef);
  [eastonFull, smithFull, isbeFull].forEach(function (full) {
    if (full && full.refs) full.refs.forEach(addRef);
  });

  // Build body HTML: synthesis + link tables + source sections
  var html = '';
  if (bpArticle && bpArticle.intro) {
    html += '<div class="bp-synthesis">' + bpArticle.intro + '</div>';
  }
  // Region hero map: the centerpiece of a region article. A mount point goes here (right after the
  // intro, ABOVE the member tables) and is filled async by _renderRegionMap once Leaflet + coords
  // load. Only region articles get it; for everything else the string stays empty.
  if (cat === 'regions') {
    html += '<div id="bp-region-map" class="bp-region-map-wrap"></div>';
  }
  // Link tables: curated, in-body grids that link to each member article (e.g. the Twelve
  // Apostles). Unlike the graph-based Connections sidebar these are hand-authored and exhaustive,
  // so an enumerable set ("the Twelve", "the judges") is navigable directly from the prose.
  html += _linkTablesHtml(bpArticle);
  // Facet sections: closely-related sub-topics folded in as collapsible, anchored <details> (e.g.
  // the Wrath of God under God). Each was its own article whose ?a= link now redirects here#anchor.
  html += _facetSectionsHtml(bpArticle);

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
  if (cat === 'regions') _renderRegionMap(container, slug, term);
  wireRefLinks(bodyEl);
  bodyEl.querySelectorAll('[data-wikilink-src]').forEach(function (srcBody) {
    _wikifyLinks(srcBody, slug);
  });
  // Auto-wikify the synthesis intro and any folded facet sections too — not just the source
  // dictionary bodies — so internal article mentions in the AI-written overview become navigable
  // links like everywhere else. _wikifyLinks skips text already inside a/.wiki-link/[data-ref],
  // so hand-authored wiki-links and the verse refs wired just above are left untouched. Each
  // block gets its own first-occurrence set (matching how each source section is wikified).
  bodyEl.querySelectorAll('.bp-synthesis, .bp-facet__body').forEach(function (proseEl) {
    _wikifyLinks(proseEl, slug);
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
          // Group all original-language words into one collapsible section (like the
          // Nave's / Easton sections), each word a collapsed card inside it.
          var nWords = data.connections.length;
          var slEl = document.createElement('details');
          slEl.className = 'bp-src-section';
          slEl.id = 'bp-strongs';
          slEl.innerHTML =
            '<summary class="bp-src-section__head">' +
              '<span class="vs-dict-src-badge" data-dict-src="strongs">OL</span>' +
              '<span class="bp-src-section__name">Original Languages' +
                ' <span class="bp-src-section__count">(' + nWords + ' word' + (nWords !== 1 ? 's' : '') + ')</span>' +
              '</span>' +
              '<span class="bp-src-section__toggle">▸</span>' +
            '</summary>' +
            '<div class="bp-src-section__body">' + _renderStrongsSection(data.connections) + '</div>';
          bodyEl.appendChild(slEl);
        }
      })
      .catch(function () {});

    // Render the Quick Info sidebar, then add the async "Member of" row into it
    _renderQuickInfo(container, cat, hitch, eastonFull, smithFull, isbeFull, bpArticle, bpIdx);
    _renderMemberOf(container, slug);
    _renderRegionOf(container, slug);
    _renderGroupMembers(container, slug);
    // Cross-cutting motif overlay: secondary badge + Quick Info row + "Fulfilled in" panel.
    // Called here (after Quick Info is built) so its async row injects into a populated panel,
    // matching _renderMemberOf's timing contract.
    _renderMotif(container, slug);
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

// ── Facet sections (umbrella folds: sub-topics as collapsible anchored <details>) ──────────────
// INTENT: A major article (God, Offering, Feast, Jesus Christ) absorbs closely-related sub-topics
//   as collapsible sections, each with its own anchor + key verses. The former standalone article
//   redirects to ?a=<parent> with an `anchor`, so every old link/term-tag lands on the right section.
// DATA: bpArticle.sections = [{ anchor, title, body(HTML), key_refs[] }]. Folded by
//   scripts/apply-biblepedia-umbrellas.py (registry: data/biblepedia/umbrellas.json).
// VERIFY: Open ?a=wrath → the God article renders with the "Wrath of God" <details> open and
//   scrolled into view; collapsing/expanding sections lets the reader manage the page.
function _facetSectionsHtml(bpArticle) {
  var secs = bpArticle && bpArticle.sections;
  if (!secs || !secs.length) return '';

  var items = secs.map(function (s) {
    var refs = (s.key_refs || []).map(function (r) {
      return '<a class="dict-ref-chip ref" data-ref="' + escHtml(r) + '">' + escHtml(r) + '</a>';
    }).join('');
    return '<details class="bp-facet" id="' + escHtml(s.anchor) + '">' +
      '<summary class="bp-facet__summary">' +
        '<span class="bp-facet__title">' + escHtml(s.title) + '</span>' +
        '<span class="bp-facet__toggle">▸</span>' +
      '</summary>' +
      '<div class="bp-facet__body">' + (s.body || '') +
        (refs ? '<div class="bp-facet__refs">' + refs + '</div>' : '') +
      '</div>' +
    '</details>';
  }).join('');

  return '<div class="bp-facets"><h2 class="bp-facets__head">Aspects</h2>' + items + '</div>';
}

// Open + scroll to a facet section by anchor (from a redirect's anchor or a #hash).
function _openFacet(container, anchor) {
  var root = container || document;
  var el;
  try { el = root.querySelector('#' + (window.CSS && CSS.escape ? CSS.escape(anchor) : anchor)); }
  catch (e) { el = null; }
  if (!el || el.className.indexOf('bp-facet') === -1) return;
  el.open = true;
  el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ── "Member of" backlink (group membership) ───────────────────────────────────
// INTENT: An article that belongs to one or more curated groups (the Twelve Apostles, the
//   Trinity, the kings of Judah…) lists those groups as a "Member of" row in the Quick Info
//   sidebar panel — the reverse direction of a group article's link_table. Data: groups.json.
// VERIFY: Open ?a=jesus-christ → Quick Info shows a "Member of" row linking to The Holy Trinity.
//   Open ?a=jerusalem (in no group) → no such row appears.
function _renderMemberOf(container, slug) {
  var panel = container.querySelector('#bp-quickinfo-body');
  if (!panel) return;
  _bpGroupsLoad().then(function (data) {
    var groups = (data && data.groups) || [];
    var belongs = groups.filter(function (g) {
      return (g.members || []).indexOf(slug) !== -1;
    });
    if (!belongs.length || !panel.isConnected) return;

    var links = belongs.map(function (g) {
      return '<a class="wiki-link" href="' +
        escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(g.id)) + '">' +
        escHtml(g.name) + '</a>';
    }).join('');

    var row = document.createElement('div');
    row.className = 'bp-qi-row';
    row.innerHTML = '<span class="bp-qi-label">Member of</span>' +
      '<div class="bp-qi-groups">' + links + '</div>';
    // Place it just after the Category row (the first row) for prominence.
    var first = panel.querySelector('.bp-qi-row');
    if (first && first.nextSibling) panel.insertBefore(row, first.nextSibling);
    else panel.appendChild(row);
  });
}

// ── "In the region" Quick Info row (reverse of a region's member tables) ───────────────────────
// INTENT: A place/event/person that belongs to one or more anchor regions lists those regions as an
//   "In the region" row in Quick Info — the reverse of the region article's member tables and hero
//   map. Lets the reader jump from, say, Capernaum up to the Galilee region hub. Data: regions.json.
// VERIFY: Open ?a=capernaum → Quick Info shows "In the region: Galilee". ?a=moses → "Egypt".
//   ?a=covenant (no region) → no such row.
function _renderRegionOf(container, slug) {
  var panel = container.querySelector('#bp-quickinfo-body');
  if (!panel) return;
  _bpRegionsLoad().then(function (data) {
    if ((data.regions || {})[slug]) return;   // a region article doesn't link to itself
    var hits = _bpRegionsByMember(data)[slug] || [];
    if (!hits.length || !panel.isConnected) return;

    // De-dupe regions (a person can appear in several member lists of one region).
    var seen = {}, links = [];
    hits.forEach(function (h) {
      if (seen[h.id]) return;
      seen[h.id] = 1;
      links.push('<a class="wiki-link" href="' +
        escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(h.id)) + '">' + escHtml(h.name) + '</a>');
    });

    var row = document.createElement('div');
    row.className = 'bp-qi-row';
    row.innerHTML = '<span class="bp-qi-label">In the region</span>' +
      '<div class="bp-qi-groups">' + links.join('') + '</div>';
    var first = panel.querySelector('.bp-qi-row');
    if (first && first.nextSibling) panel.insertBefore(row, first.nextSibling);
    else panel.appendChild(row);
  });
}

// ── "Group members" Quick Info row (reverse of "Member of": shown on a group hub) ──────────────
// INTENT: A group hub article (apostles, trinity, kings-of-judah…) lists its members as a Quick
//   Info row linking each member's article — the sidebar counterpart to the in-body link table.
// VERIFY: Open ?a=apostles → Quick Info shows a "Group members" row of 13 linked names.
function _renderGroupMembers(container, slug) {
  var panel = container.querySelector('#bp-quickinfo-body');
  if (!panel) return;
  _bpGroupsLoad().then(function (data) {
    var groups = (data && data.groups) || [];
    var grp = null;
    for (var i = 0; i < groups.length; i++) {
      if (groups[i].id === slug) { grp = groups[i]; break; }
    }
    if (!grp || !grp.members || !grp.members.length || !panel.isConnected) return;

    var links = grp.members.map(function (mid) {
      var e = _bpIdxMap && _bpIdxMap[mid];
      var name = (e && e.term) || mid.replace(/-/g, ' ');
      return '<a class="wiki-link" href="' +
        escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(mid)) + '">' +
        escHtml(name) + '</a>';
    }).join('');

    var row = document.createElement('div');
    row.className = 'bp-qi-row';
    row.innerHTML = '<span class="bp-qi-label">Group members</span>' +
      '<div class="bp-qi-groups">' + links + '</div>';
    var first = panel.querySelector('.bp-qi-row');
    if (first && first.nextSibling) panel.insertBefore(row, first.nextSibling);
    else panel.appendChild(row);
  });
}

// ── Motif overlay (cross-cutting imagery/typology) ────────────────────────────
// INTENT: When an article is in the motif registry, mark it WITHOUT changing its category — a
//   secondary "Motif · <Family>" badge (and a "Type" badge for typological images) in the header,
//   a "Motif" Quick Info row linking to the family browse, and, for types, a "Fulfilled in" sidebar
//   panel rendering the shadow → fulfillment with its verse refs (wired by wireRefLinks).
// DATA: motifs.json keyed by article id (see _bpMotifsLoad). Adding/editing a motif is a data-only
//   change (re-run /tmp/build_motifs.py) — no code edit needed.
// VERIFY: Open ?a=lamb → header shows "Concept" + "Motif · Fauna" + "Type"; Quick Info has a Motif
//   row; a "Fulfilled in Christ" panel shows the Passover-lamb shadow and John 1:29 etc. as links.
//   Open ?a=heart → "Motif · Body & Garment" badge, Motif row, but NO fulfillment panel (not a type).
function _renderMotif(container, slug) {
  _bpMotifsLoad().then(function (data) {
    var m = data && data.motifs && data.motifs[slug];
    if (!m) return;
    var families = data.families || {};
    var modeLabels = data.modes || {};
    var famName = (families[m.family] && families[m.family].name) || m.family;
    var isType  = (m.modes || []).indexOf('type') !== -1;

    // 1) Secondary header badge(s) — appended after the category badge, never replacing it.
    var badges = container.querySelector('.bp-article__badges');
    if (badges) {
      var pill = ' <span class="bp-cat-badge bp-cat-badge--motif" title="' +
        escHtml(m.gloss || '') + '">Motif · ' + escHtml(famName) + '</span>';
      if (isType) pill += ' <span class="bp-cat-badge bp-cat-badge--type">Type</span>';
      badges.insertAdjacentHTML('beforeend', pill);
    }

    // 2) Quick Info "Motif" row — family links to the browse view; modes shown as a sub-label.
    var qi = container.querySelector('#bp-quickinfo-body');
    if (qi && qi.isConnected) {
      var modeStr = (m.modes || []).map(function (md) { return escHtml(modeLabels[md] || md); }).join(', ');
      var row = document.createElement('div');
      row.className = 'bp-qi-row';
      row.innerHTML = '<span class="bp-qi-label">Motif</span>' +
        '<div class="bp-qi-motif">' +
          '<a class="wiki-link" href="' + escHtml(BIBLEPEDIA_URL + '?cat=motifs') + '">' +
            escHtml(famName) + '</a>' +
          (modeStr ? '<span class="bp-qi-motif__modes">' + modeStr + '</span>' : '') +
        '</div>';
      var first = qi.querySelector('.bp-qi-row');
      if (first && first.nextSibling) qi.insertBefore(row, first.nextSibling);
      else qi.appendChild(row);
    }

    // 3) "Fulfilled in" panel — only for types. Inserted after the Library panel (or, lacking it,
    //    after Quick Info), so the typology reads high in the sidebar like a key fact.
    if (m.typology) _renderMotifPanel(container, m.typology);
  });
}

// Render the shadow → fulfillment typology as a sidebar panel; refs become wired verse links.
function _renderMotifPanel(container, typ) {
  var anchor = container.querySelector('#bp-library-panel') || container.querySelector('#bp-quickinfo-panel');
  if (!anchor) return;
  var fulfilledIn = { christ: 'Christ', church: 'the Church', spirit: 'the Spirit',
                      'new-creation': 'the New Creation' }[typ.fulfilled_in] || 'Christ';
  var refs = (typ.refs || []).map(function (r) {
    return '<a class="dict-ref-chip ref" data-ref="' + escHtml(r) + '">' + escHtml(r) + '</a>';
  }).join('');

  var panel = document.createElement('div');
  panel.className = 'bp-sidebar-panel bp-motif-panel';
  panel.innerHTML =
    '<div class="bp-sidebar-panel__head">Fulfilled in ' + escHtml(fulfilledIn) + '</div>' +
    '<div class="bp-sidebar-panel__body">' +
      (typ.shadow ? '<div class="bp-motif-typ"><span class="bp-motif-typ__label">Shadow</span>' +
        '<p class="bp-motif-typ__text">' + escHtml(typ.shadow) + '</p></div>' : '') +
      (typ.fulfillment ? '<div class="bp-motif-typ"><span class="bp-motif-typ__label">Fulfillment</span>' +
        '<p class="bp-motif-typ__text">' + escHtml(typ.fulfillment) + '</p></div>' : '') +
      (refs ? '<div class="bp-motif-typ__refs">' + refs + '</div>' : '') +
    '</div>';
  anchor.insertAdjacentElement('afterend', panel);
  wireRefLinks(panel);
}

// ── Link tables (in-body, curated navigation grids) ───────────────────────────
// INTENT: Render hand-authored tables that link to each member of an enumerable group from
//   within the article body (e.g. the Twelve Apostles → each apostle's article). This is the
//   counterpart to the term-graph Connections sidebar: exhaustive and ordered, not inferred.
// DATA: bpArticle.link_tables = [{ title?, note?, columns:[…], rows:[{ id?, cells:[…] }] }].
//   The first cell of a row links to article ?a=<id> when id is present; other cells are plain
//   text. Verse references written as <a class="ref" data-ref> inside a cell are wired by the
//   caller's wireRefLinks(bodyEl); to keep that working, cell text is inserted as-is (callers
//   author trusted content) rather than escaped — matching how intro HTML is handled.
// VERIFY: Open ?a=apostles → a "The Twelve Apostles" table lists each apostle as a link that
//   opens their article; an article without link_tables renders nothing here.
function _linkTablesHtml(bpArticle) {
  var tables = bpArticle && bpArticle.link_tables;
  if (!tables || !tables.length) return '';

  return tables.map(function (t) {
    var cols = (t.columns || []).map(function (c) {
      return '<th>' + escHtml(c) + '</th>';
    }).join('');

    var rows = (t.rows || []).map(function (row) {
      var cells = (row.cells || []).map(function (cell, i) {
        if (i === 0 && row.id) {
          return '<td class="bp-link-table__name"><a class="wiki-link" href="' +
            escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(row.id)) + '">' +
            escHtml(cell) + '</a></td>';
        }
        return '<td>' + cell + '</td>';
      }).join('');
      return '<tr>' + cells + '</tr>';
    }).join('');

    return '<div class="bp-link-table">' +
      (t.title ? '<h3 class="bp-link-table__title">' + escHtml(t.title) + '</h3>' : '') +
      '<div class="bp-link-table__scroll"><table>' +
        (cols ? '<thead><tr>' + cols + '</tr></thead>' : '') +
        '<tbody>' + rows + '</tbody>' +
      '</table></div>' +
      (t.note ? '<p class="bp-link-table__note">' + t.note + '</p>' : '') +
    '</div>';
  }).join('');
}

// ── "In the Library" sidebar panel ────────────────────────────────────────────
// INTENT: When an article corresponds to full texts in the Library (a creed/council, or a
//   church father whose works are held), link out so the reader can read the primary source.
//   Data lives in the article JSON's library_refs[] (built by the biblepedia→library map);
//   panel stays hidden when absent so ordinary articles are unaffected.
// VERIFY: Open ?a=augustine-of-hippo → "In the Library" lists Confessions, City of God, …, each
//   linking to library/read/?doc=<id>. Open ?a=jerusalem → panel is absent.
function _renderLibraryPanel(container, bpArticle) {
  var refs  = bpArticle && bpArticle.library_refs;
  var panel = container.querySelector('#bp-library-panel');
  var body  = container.querySelector('#bp-library-body');
  if (!panel || !body || !refs || !refs.length) return;

  var html = '<div class="bp-lib-refs">';
  refs.forEach(function (r) {
    html += '<a class="bp-lib-ref" href="' + escHtml(LIBRARY_READ_URL) +
              '?doc=' + encodeURIComponent(r.id) + '">' +
      '<span class="bp-lib-ref__title">' + escHtml(r.title) + '</span>' +
      (r.author ? '<span class="bp-lib-ref__meta">' + escHtml(r.author) + '</span>' : '') +
    '</a>';
  });
  html += '</div>';

  body.innerHTML = html;
  panel.style.display = '';
}

// ── Location mini-map panel (place articles only) ─────────────────────────────
var CARTO_TILES = 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';
var CARTO_ATTR  = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>' +
                  ' &copy; <a href="https://carto.com/attributions">CARTO</a>';

function _locNorm(s) { return (s || '').toLowerCase().replace(/[^a-z0-9]+/g, ''); }

// INTENT: For a place-category article, fetch its coordinate and inject a small interactive
//   Leaflet map ("Location" panel) just below Quick Info — close zoom + green pin when the site
//   is identified, wide zoom + amber pin + "Location uncertain" badge when disputed, and a wide
//   regional view + "Approximate region" badge when only a territory is known. Places with no
//   known location (absent from place-coords.json) get no panel at all.
// CHANGE? Coordinates/confidence come from data/maps/place-coords.json (scripts/build-place-coords.py).
//   The panel is inserted via insertAdjacentElement after #bp-quickinfo-panel, so it depends on the
//   sidebar shell built in _renderArticleShell; the "Open in full map" link targets the Maps page's
//   ?focus=lat,lon,zoom handler in assets/js/maps.js — keep that param contract in sync.
// VERIFY: ?a=jerusalem → green pin, close zoom, no badge. ?a=petra → amber pin + "Location
//   uncertain" + faint alt pins. ?a=zabulon → wide view + "Approximate region". ?a=cave → no panel.
function _renderLocationPanel(container, slug, cat, term) {
  if (cat !== 'places') return;
  var qi = container.querySelector('#bp-quickinfo-panel');
  if (!qi) return;
  _placeCoordsLoad().then(function (coords) {
    var e = coords[slug];
    if (!e) return;  // unknown location → no map panel

    var zoom  = e.conf === 'identified' ? 11 : (e.conf === 'region' ? 7 : 8);
    var badge = '';
    if (e.conf === 'disputed') {
      badge = '<span class="bp-loc-badge bp-loc-badge--disputed">Location uncertain</span>';
    } else if (e.conf === 'region') {
      badge = '<span class="bp-loc-badge bp-loc-badge--region">Approximate region</span>';
    }
    // "Identified with X" only when the source headword differs from the article title (e.g.
    // Petra → Sela), and not for region fallbacks (whose name is just the article term).
    var idNote = (e.name && e.source !== 'region' && _locNorm(e.name) !== _locNorm(term))
      ? '<p class="bp-loc-id">Identified with ' + escHtml(e.name) + '</p>' : '';
    var focusUrl = MAPS_URL + '?focus=' + e.lat + ',' + e.lon + ',' + zoom;

    var panel = document.createElement('div');
    panel.className = 'bp-sidebar-panel bp-location-panel';
    panel.innerHTML =
      '<div class="bp-sidebar-panel__head">Location' + badge + '</div>' +
      '<div class="bp-sidebar-panel__body">' +
        '<div class="bp-loc-map"></div>' +
        idNote +
        '<div class="bp-loc-foot">' +
          '<a class="bp-loc-openmap" href="' + escHtml(focusUrl) + '">Open in full map →</a>' +
          '<span class="bp-loc-attr">Locations: ' +
            '<a href="https://www.openbible.info/geo/" target="_blank" rel="noopener">OpenBible.info</a> (CC BY)' +
          '</span>' +
        '</div>' +
      '</div>';
    qi.insertAdjacentElement('afterend', panel);

    _ensureLeaflet().then(function () {
      var mapEl = panel.querySelector('.bp-loc-map');
      // scrollWheelZoom off so the map doesn't trap page scroll on a long article
      var map = L.map(mapEl, { zoomControl: true, attributionControl: true, scrollWheelZoom: false });
      L.tileLayer(CARTO_TILES, { maxZoom: 19, attribution: CARTO_ATTR }).addTo(map);
      map.setView([e.lat, e.lon], zoom);
      // Use circleMarkers (not L.marker) — the Biblepedia page doesn't ship Leaflet's default
      // marker icon images, so a plain marker would render broken.
      var color = e.conf === 'identified' ? '#2f7d32' : (e.conf === 'region' ? '#c47a2a' : '#c08a2a');
      L.circleMarker([e.lat, e.lon], {
        radius: e.conf === 'region' ? 11 : 8, color: color, weight: 3,
        fillColor: color, fillOpacity: e.conf === 'region' ? 0.15 : 0.4
      }).addTo(map).bindPopup(escHtml(term));
      // Competing identifications for disputed sites, shown faint
      (e.alts || []).forEach(function (a) {
        L.circleMarker([a.lat, a.lon], {
          radius: 5, color: '#7a7a7a', weight: 2, fillColor: '#b8b8b8', fillOpacity: 0.35
        }).addTo(map).bindPopup('Alternative: ' + escHtml(a.name || ''));
      });
      // The panel was just inserted; Leaflet measured a 0-height container mid-insert.
      setTimeout(function () { map.invalidateSize(); }, 60);
    }).catch(function () {
      // Leaflet CDN blocked / offline: degrade to a text note; the "Open in full map" link stays.
      var mapEl = panel.querySelector('.bp-loc-map');
      if (mapEl) mapEl.innerHTML = '<p class="bp-loc-id" style="padding:.6rem">Map unavailable offline.</p>';
    });
  });
}

// ── Region hero map (region articles only) ────────────────────────────────────
// Geometry (polygon backdrops) lives in data/maps/regions.json — coordOrder [lat,lon], same as
// Leaflet. One lazy, session-cached fetch shared across region articles in a session.
var _MAPS_REGIONS_URL = _resolve('../../data/maps/regions.json');
var _mapsRegionsCache = null;
function _mapsRegionsLoad() {
  if (!_mapsRegionsCache) {
    _mapsRegionsCache = fetch(_MAPS_REGIONS_URL)
      .then(function (r) { return r.ok ? r.json() : { regions: [] }; })
      .catch(function () { return { regions: [] }; });
  }
  return _mapsRegionsCache;
}

// INTENT: Build the interactive hero map for a region article — every member PLACE (green) and
//   EVENT (amber) as a hoverable circleMarker (tooltip = name) that, when it maps to an article,
//   navigates on click. If the registry names a map_region, its polygon is drawn underneath as
//   context. The view fits the markers' bounds (falling back to the registry `focus`). Place coords
//   come from place-coords.json; events are anchored by {at:<place id>} or explicit {coords:[lat,lon]}.
// CHANGE? Marker/colour contract is shared with the CSS legend (.bp-rmap-legend) and the single-pin
//   _renderLocationPanel palette; event anchoring + member ids come from data/biblepedia/regions.json
//   (validated by scripts/apply-biblepedia-regions.py). Polygon ids must exist in data/maps/regions.json.
// VERIFY: ?a=egypt → map with green place pins + 2 amber event pins inside a faint Egypt polygon;
//   hovering a pin shows its name, clicking "Rameses" opens that article. ?a=galilee → markers only
//   (no polygon), bounds hug the lake towns.
var RMAP_PLACE = '#2f7d32';   // green — matches identified-place pin in _renderLocationPanel
var RMAP_EVENT = '#c2410c';   // amber/rust — events, visually distinct from places
function _renderRegionMap(container, slug, term) {
  var mount = container.querySelector('#bp-region-map');
  if (!mount) return;
  Promise.all([_bpRegionsLoad(), _placeCoordsLoad(), _bpIdxLoad()]).then(function (res) {
    var reg = ((res[0] && res[0].regions) || {})[slug];
    if (!reg) { mount.remove(); return; }   // not a registered region → no map
    var coords = res[1] || {};

    // Resolve every marker up front so we can drop the panel entirely if none resolve.
    var markers = [];   // {lat, lon, name, role, href?}
    var artHref = function (id) {
      return (_bpIdxMap && _bpIdxMap[id]) ? (BIBLEPEDIA_URL + '?a=' + encodeURIComponent(id)) : null;
    };
    var nameOf = function (id) {
      return (_bpIdxMap && _bpIdxMap[id] && _bpIdxMap[id].term) || id.replace(/-/g, ' ');
    };
    (reg.places || []).forEach(function (pid) {
      var c = coords[pid];
      if (c) markers.push({ lat: c.lat, lon: c.lon, name: nameOf(pid), role: 'place', href: artHref(pid) });
    });
    (reg.events || []).forEach(function (ev) {
      if (!ev) return;
      var lat, lon;
      if (ev.coords) { lat = ev.coords[0]; lon = ev.coords[1]; }
      else if (ev.at && coords[ev.at]) { lat = coords[ev.at].lat; lon = coords[ev.at].lon; }
      if (lat == null) return;
      markers.push({ lat: lat, lon: lon, name: nameOf(ev.id), role: 'event', href: artHref(ev.id) });
    });

    if (!markers.length && !reg.map_region) { mount.remove(); return; }

    var focus = reg.focus || [];
    var focusUrl = MAPS_URL + '?focus=' + (focus[0] || 0) + ',' + (focus[1] || 0) + ',' + (focus[2] || 7);
    mount.className = 'bp-region-map-wrap bp-sidebar-panel';
    mount.innerHTML =
      '<div class="bp-sidebar-panel__head">Map of ' + escHtml(term) +
        '<span class="bp-rmap-legend">' +
          '<span class="bp-rmap-legend__item"><i class="bp-rmap-dot bp-rmap-dot--place"></i>Places</span>' +
          '<span class="bp-rmap-legend__item"><i class="bp-rmap-dot bp-rmap-dot--event"></i>Events</span>' +
        '</span>' +
      '</div>' +
      '<div class="bp-region-map"></div>' +
      '<div class="bp-loc-foot">' +
        '<a class="bp-loc-openmap" href="' + escHtml(focusUrl) + '">Open in full map →</a>' +
        '<span class="bp-loc-attr">Locations: ' +
          '<a href="https://www.openbible.info/geo/" target="_blank" rel="noopener">OpenBible.info</a> (CC BY)' +
        '</span>' +
      '</div>';

    var geomP = reg.map_region ? _mapsRegionsLoad() : Promise.resolve(null);
    Promise.all([_ensureLeaflet(), geomP]).then(function (r2) {
      var mapsDoc = r2[1];
      var mapEl = mount.querySelector('.bp-region-map');
      var map = L.map(mapEl, { zoomControl: true, attributionControl: true, scrollWheelZoom: false });
      L.tileLayer(CARTO_TILES, { maxZoom: 19, attribution: CARTO_ATTR }).addTo(map);

      var bounds = [];

      // Polygon backdrop (context) drawn first so markers sit on top.
      if (reg.map_region && mapsDoc && mapsDoc.regions) {
        var geom = mapsDoc.regions.find(function (g) { return g.id === reg.map_region; });
        var periods = geom && geom.periods;
        if (periods && periods.length) {
          // Prefer the largest-extent period for a teaching backdrop (first is fine if one).
          var poly = (periods[0] && periods[0].coords) || [];
          if (poly.length) {
            L.polygon(poly, { color: '#5c3d1e', weight: 1.5, opacity: 0.5,
              fillColor: '#b8860b', fillOpacity: 0.08 }).addTo(map);
            poly.forEach(function (pt) { bounds.push(pt); });
          }
        }
      }

      markers.forEach(function (m) {
        var color = m.role === 'event' ? RMAP_EVENT : RMAP_PLACE;
        var cm = L.circleMarker([m.lat, m.lon], {
          radius: m.role === 'event' ? 7 : 6, color: color, weight: 2,
          fillColor: color, fillOpacity: m.role === 'event' ? 0.85 : 0.55,
          className: 'bp-rmap-marker'
        }).addTo(map);
        // Hover label (sticky tooltip); click navigates to the article when one exists.
        cm.bindTooltip(escHtml(m.name), { direction: 'top', opacity: 0.95 });
        if (m.href) {
          cm.on('click', function () { window.location.href = m.href; });
          cm.options.interactive = true;
          cm.getElement && cm.getElement() && (cm.getElement().style.cursor = 'pointer');
        }
        bounds.push([m.lat, m.lon]);
      });

      if (bounds.length >= 2) {
        map.fitBounds(bounds, { padding: [28, 28] });
      } else if (bounds.length === 1) {
        map.setView(bounds[0], (focus[2] || 9));
      } else if (focus.length >= 2) {
        map.setView([focus[0], focus[1]], focus[2] || 7);
      }
      // Container was measured mid-insert at 0 height; force a re-measure.
      setTimeout(function () { map.invalidateSize(); }, 60);
    }).catch(function () {
      var mapEl = mount.querySelector('.bp-region-map');
      if (mapEl) mapEl.innerHTML = '<p class="bp-loc-id" style="padding:.6rem">Map unavailable offline.</p>';
    });
  });
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

// INTENT: Each original-language word renders as an individually collapsible card
//   (collapsed by default) inside the one "Original Languages" section, so a word-rich
//   article shows a tidy list of informative title-bars the reader expands one at a time.
// CHANGE? Each word is a <details class="bp-sl-card"> with an informative <summary>
//   (code · lemma · transliteration · gloss · occurrence count); the heat map and stats
//   live in the body, shown only when expanded. The outer "Original Languages" wrapper
//   is built in _renderArticleShell. Heat-map cell logic unchanged.
// VERIFY: Open a Biblepedia article with original-language data (e.g. a person/word like
//   "aaron"); the "Original Languages" group lists collapsed word bars; each bar shows
//   the Strong's code, the Greek/Hebrew word, transliteration, gloss, and count; clicking
//   one expands its distribution heat map.
function _renderStrongsSection(connections) {
  return connections.map(function (c) {
    var isHeb  = c.lang === 'hebrew';
    var pct    = c.total > 0 ? Math.round((c.count / c.total) * 100) : 0;
    var langLabel = isHeb ? 'Hebrew' : 'Greek';
    var glossShort = c.gloss ? c.gloss.replace(/\.\s*$/, '') : '';

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

    // Informative title bar: code · word · transliteration · gloss · count
    var summary =
      '<summary class="bp-sl-card__head">' +
        '<span class="bp-sl-chevron" aria-hidden="true">▸</span>' +
        '<span class="bp-sl-code bp-sl-code--' + c.lang + '">' + escHtml(c.code) + '</span>' +
        '<span class="bp-sl-lemma">' + escHtml(c.lemma) + '</span>' +
        (c.translit ? '<span class="bp-sl-translit">' + escHtml(c.translit) + '</span>' : '') +
        (glossShort ? '<span class="bp-sl-gloss-inline">' + escHtml(glossShort) + '</span>' : '') +
        '<span class="bp-sl-count-chip" title="occurrences as this term">' + c.count + '×</span>' +
      '</summary>';

    var body =
      '<div class="bp-sl-card__body">' +
        '<div class="bp-sl-lang-line">' + langLabel +
          (c.gloss ? ' &middot; ' + escHtml(c.gloss) : '') + '</div>' +
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

    return '<details class="bp-sl-card">' + summary + body + '</details>';
  }).join('');
}

// INTENT: Render the "(aka Calvary)" suffix on a search/dropdown result that is an alias
//   pointer (entry.redirect set). The entry stays visible in search so "Golgotha" still
//   surfaces a hit, but is labelled as routing to its canonical article. Click still uses the
//   alias id as data-slug; _showArticle resolves the redirect.
// CHANGE? Reads _bpIdxMap[redirect].term for the canonical display name; used by both
//   _showSearchResults and _showSearchDropdown.
// VERIFY: Search "Golgotha" — the result reads "Golgotha (aka Calvary)" and opens Calvary.
function _akaHtml(entry) {
  if (!entry || !entry.redirect) return '';
  var canon = _bpIdxMap && _bpIdxMap[entry.redirect];
  if (!canon) return '';
  return ' <span class="bp-result-aka">(aka ' + escHtml(canon.term) + ')</span>';
}

// ── Wiki-link injection ────────────────────────────────────────────────────────

function _wikifyLinks(root, currentSlug) {
  if (!_bpIdxData) return;

  if (!_wikiTitleMap) {
    _wikiTitleMap = {};
    _wikiTitles   = [];
    // INTENT: Build the term→article map for in-prose auto-linking. Besides full articles, an
    //   alias entry (has_article:false but redirect:<canonicalId>) must still tag its own term
    //   to the canonical article, and a canonical's `aliases` (alternate display names like
    //   "the place of a skull") must tag there too — so merging synonym articles never loses a
    //   link name. First registration of a key wins (titles are length-sorted below).
    // CHANGE? Mirrors the redirect/alias contract in _showArticle + data/biblepedia/merges.json.
    //   If you add a new alias term, no JS change is needed — it flows from index.json.
    // VERIFY: On the Calvary article, the word "Golgotha" in prose renders as a .wiki-link whose
    //   href is ?a=calvary (not ?a=golgotha, though that would also redirect).
    var _addWiki = function (label, target) {
      if (!label || label.length < 3 || !target) return;
      var key = label.toLowerCase();
      if (!_wikiTitleMap[key]) { _wikiTitleMap[key] = target; _wikiTitles.push(label); }
    };
    _bpIdxData.forEach(function (e) {
      var target = e.redirect || (e.has_article ? e.id : null);
      if (!target) return;
      _addWiki(e.term, target);
      (e.aliases || []).forEach(function (a) { _addWiki(a, e.id); });
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

// ── Connections (precomputed link graph) ──────────────────────────────────────

// Contextual group labels by the CURRENT article's category, so a place shows "People here /
// Events here / Nearby places" while a person shows "Related people / Places / Events".
function _connLabels(curCat) {
  curCat = _normCat(curCat);
  var base = { people: 'People', places: 'Places', events: 'Events', concepts: 'Concepts',
               father: 'Church Fathers', commentator: 'Commentators', names: 'Names' };
  if (curCat === 'places') { base.people = 'People here'; base.events = 'Events here'; base.places = 'Nearby places'; }
  else if (curCat === 'people') { base.people = 'Related people'; }
  else if (curCat === 'events') { base.events = 'Related events'; }
  return base;
}

// INTENT: Render the typed Connections panel from the precomputed graph (links.json). Neighbours
//   are grouped by category with contextual headers and a backlink count; falls back to the
//   verse-based related list when the graph lacks an entry for this article.
// CHANGE? Reads _bpLinks.links[slug] = {indeg, conn:[[id,weight,basis]]}; neighbour term/category
//   come from _bpIdxMap. If links.json schema changes, update here.
// VERIFY: Open "jerusalem" → Connections shows "People here", "Events here", "Nearby places"
//   groups and "Referenced by N articles".
function _loadConnections(container, slug, bodies) {
  var el = container.querySelector('#bp-related-body');
  if (!el) return;
  _bpLinksLoad().then(function () {
    var node = _bpLinks.links && _bpLinks.links[slug];
    if (!node || !node.conn || !node.conn.length) {
      _loadRelatedArticles(container, bodies[0], bodies[1], bodies[2], slug);  // fallback
      return;
    }
    var labels = _connLabels(_bpIdxMap[slug] && _bpIdxMap[slug].category);
    var groups = {};
    node.conn.forEach(function (c) {
      var meta = _bpIdxMap && _bpIdxMap[c[0]];
      if (!meta) return;
      var cat = _normCat(meta.category);
      (groups[cat] || (groups[cat] = [])).push({ id: c[0], term: meta.term });
    });

    var html = '';
    if (node.indeg) {
      html += '<p class="bp-conn-backlinks">Referenced by <strong>' + node.indeg +
        '</strong> article' + (node.indeg !== 1 ? 's' : '') + '</p>';
    }
    ['people', 'places', 'events', 'concepts', 'father', 'commentator', 'names'].forEach(function (cat) {
      var items = groups[cat];
      if (!items || !items.length) return;
      html += '<div class="bp-conn-group">' +
        '<div class="bp-conn-group__head">' + escHtml(labels[cat] || cat) + '</div>' +
        '<div class="bp-related-list">';
      items.slice(0, 8).forEach(function (it) {
        html += '<button type="button" class="bp-related-item" data-slug="' + escHtml(it.id) + '">' +
          _catBadgeHtml(cat) +
          '<span class="bp-related-item__term">' + escHtml(it.term) + '</span>' +
          '<span class="bp-related-item__arrow">›</span>' +
        '</button>';
      });
      html += '</div></div>';
    });
    if (!html) { _loadRelatedArticles(container, bodies[0], bodies[1], bodies[2], slug); return; }
    el.innerHTML = html;
    el.querySelectorAll('.bp-related-item[data-slug]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        _showArticle(container.closest('#bp-container') || container, btn.dataset.slug);
      });
    });
  });
}

// ── Related articles (verse-co-occurrence fallback) ───────────────────────────

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

// INTENT: Canonicalize a raw index category to one of the known plural keys so the UI
//   handles the singular variants the index still emits (concept/event) and the extra
//   categories (events, commentator) uniformly. See DATA-15 for the generator-side fix.
// CHANGE? If a new category is added to data/biblepedia/index.json, add it here AND give it
//   a badge in _catClass/_catBadgeHtml plus (optionally) a CATEGORY_TILES entry, or it falls
//   back to "concepts" and won't be browsable by tile.
// VERIFY: An article whose index category is "event" or "events" shows an "Event" badge
//   (orange), not "Concept".
function _normCat(cat) {
  switch (cat) {
    case 'person':      return 'people';
    case 'place':       return 'places';
    case 'concept':     return 'concepts';
    case 'name':        return 'names';
    case 'event':       return 'events';
    default:            return cat || 'concepts';
  }
}

function _catClass(cat) {
  cat = _normCat(cat);
  var map = { people: 'people', places: 'place', concepts: 'concept', names: 'name',
              events: 'event', father: 'father', commentator: 'commentator', regions: 'region' };
  return 'bp-cat-badge--' + (map[cat] || 'concept');
}

function _catBadgeHtml(cat) {
  cat = _normCat(cat);
  var labels = { people: 'Person', places: 'Place', concepts: 'Concept', names: 'Name',
                 events: 'Event', father: 'Church Father', commentator: 'Commentator', regions: 'Region' };
  return '<span class="bp-cat-badge ' + _catClass(cat) + '">' + escHtml(labels[cat] || 'Concept') + '</span>';
}

// INTENT: Re-point the breadcrumb + header category badges to `cat` after the article file reveals a
//   category the (stale, pre-rebuild) index didn't have — e.g. a promoted region. Keeps the visible
//   badge in sync with the body's behaviour without waiting for build-biblepedia-index.py.
// CHANGE? Targets the badge markup emitted by _renderArticleShell (breadcrumb .bp-cat-badge with the
//   inline font-size, and the first .bp-article__badges .bp-cat-badge). If that markup changes, update here.
function _syncCatBadges(container, cat) {
  var nc = _normCat(cat);
  var crumb = container.querySelector('.bp-breadcrumb .bp-cat-badge');
  if (crumb) {
    crumb.className = 'bp-cat-badge ' + _catClass(nc);
    crumb.textContent = nc.charAt(0).toUpperCase() + nc.slice(1);
  }
  var head = container.querySelector('.bp-article__badges .bp-cat-badge');
  if (head) head.outerHTML = _catBadgeHtml(nc);
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
  // AUD-22: compare on normalized categories so singular index variants (concept/event)
  // browse alongside their plural canonical form.
  cat = _normCat(cat);
  return _bpIdxData
    .filter(function (e) { return _normCat(e.category) === cat || (cat === 'names' && e.hitchcock_meaning); })
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
