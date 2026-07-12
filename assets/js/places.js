/* places.js — Biblical place-name auto-tagger and hover tooltip.
 *
 * Loads data/maps/places.json once, builds a regex from all names + aliases,
 * walks text nodes in target containers, and wraps matches in <a class="map-place">
 * elements that show a hover tooltip linking to the maps page.
 *
 * Public API:
 *   autoTagPlaces(rootEl)       — tag places inside a specific element (call after
 *                                 dynamic renders in reader.js / timeline.js)
 *   runAutoTagPlaces()          — idle-time full-page pass on static containers
 */
'use strict';

import { _resolve, escHtml, MAPS_URL } from './core.js';

/* ── Data URL (relative to this file) ───────────────────────────────────── */
var _PLACES_URL = _resolve('../../data/maps/places.json');

/* ── State ───────────────────────────────────────────────────────────────── */
var _placesReady  = null;          // Promise; resolves once places are loaded
var _placesByName = null;          // Map: lowercase name/alias → place entry
var _placesById   = null;          // Map: place id → place entry
var _placesAll    = null;          // Array of all place entries
var _placeRe      = null;          // Combined alternation regex (longest first)

/* ── Tooltip DOM ─────────────────────────────────────────────────────────── */
var _tip       = null;
var _showTimer = null;
var _hideTimer = null;

/* ── Load & index ────────────────────────────────────────────────────────── */
export function loadPlaces() {
  if (_placeRe)     return Promise.resolve();
  if (_placesReady) return _placesReady;
  // INTENT: Fetch + index places.json once; null-reset on failure so the next
  //   call can retry (a truthy rejected Promise would otherwise permanently block
  //   retries, causing one unhandled rejection per chapter navigation).
  // CHANGE? _PLACES_URL points to data/maps/places.json; if the filename changes,
  //   also update sw.js SHELL_URLS and the path in timelapse-map.js.
  // VERIFY: Throttle to Offline in DevTools, load /read/, navigate chapters —
  //   no "Uncaught (in promise)" errors for places.js in the console.
  _placesReady = fetch(_PLACES_URL)
    .then(function (r) { return r.json(); })
    .then(function (places) { _buildIndex(places); })
    .catch(function () { _placesReady = null; });
  return _placesReady;
}

function _buildIndex(places) {
  _placesByName = Object.create(null);
  _placesById   = Object.create(null);
  _placesAll    = places;
  var allNames = [];

  places.forEach(function (p) {
    _placesById[p.id] = p;
    var names = [p.name].concat(p.aliases || []);
    names.forEach(function (n) {
      if (n.length < 3) return;
      var k = n.toLowerCase();
      if (!_placesByName[k]) {
        _placesByName[k] = p;
        allNames.push(n);
      }
    });
  });

  /* Longest match first so "Mount Sinai" beats "Sinai" */
  allNames.sort(function (a, b) { return b.length - a.length; });

  /* Build single combined regex with word boundaries */
  var escaped = allNames.map(function (n) {
    return '\\b' + n.replace(/[-[\]{}()*+?.,\\^$|#]/g, '\\$&') + '\\b';
  });
  _placeRe = new RegExp('(' + escaped.join('|') + ')', 'gi');
}

/* ── Text-node walker ────────────────────────────────────────────────────── */
var _SKIP_TAGS = { SCRIPT:1, STYLE:1, CODE:1, PRE:1, TEXTAREA:1, SVG:1 };

function _walkText(root, cb) {
  var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode: function (node) {
      var p = node.parentElement;
      if (!p) return NodeFilter.FILTER_SKIP;
      if (_SKIP_TAGS[p.tagName]) return NodeFilter.FILTER_SKIP;
      /* Skip inside existing interactive elements. .term-link is excluded so a
         place tag never NESTS inside a term tag (two stacked hover tooltips);
         the upgrade pass in autoTagPlaces converts those term-links instead. */
      if (p.closest('a, [data-ref], .map-place, .term-link, .bsw-term, .bsw-modal-backdrop, .maps-page'))
        return NodeFilter.FILTER_SKIP;
      return node.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
    }
  });
  var nodes = [];
  var n;
  while ((n = tw.nextNode())) nodes.push(n);
  nodes.forEach(cb);
}

/* ── Anchor factory ──────────────────────────────────────────────────────── */
/* The href deep-links the maps page to the place itself: ?focus=lat,lon,zoom
   flies there and drops a highlight ring, #mapId selects the era map first
   (both handled in maps.js _initMapsPage/_applyFocusParam). */
export function placeMapHref(place, mapId) {
  return MAPS_URL + '?focus=' + place.lat + ',' + place.lon + ',10#' + (mapId || place.mapId);
}

function _makePlaceAnchor(place, text) {
  var a = document.createElement('a');
  a.className = 'map-place';
  a.href      = placeMapHref(place);
  a.target    = '_blank';
  a.rel       = 'noopener';
  a.setAttribute('data-place-id', place.id);
  a.textContent = text;
  a.addEventListener('mouseenter', function () { _scheduleShow(a, place); });
  a.addEventListener('mouseleave', function () { _scheduleHide(); });
  a.addEventListener('focus',      function () { _scheduleShow(a, place); });
  a.addEventListener('blur',       function () { _scheduleHide(); });
  return a;
}

/* ── Core tagger ─────────────────────────────────────────────────────────── */
export function autoTagPlaces(rootEl) {
  if (!_placeRe || !_placesByName) return;
  var root = rootEl || document.body;

  /* Upgrade pass: a name that is BOTH a biblepedia term and a place (e.g.
     Samaria) may already be wrapped as a hover-only .term-link. Replacing the
     span (listeners go with the node) makes the place layer own it — one
     tooltip, a real map link, and the place popup covers the article link. */
  root.querySelectorAll('span.term-link').forEach(function (el) {
    var place = _placesByName[(el.textContent || '').trim().toLowerCase()];
    if (place && el.parentNode) el.replaceWith(_makePlaceAnchor(place, el.textContent));
  });

  _walkText(root, function (textNode) {
    var text = textNode.nodeValue;
    _placeRe.lastIndex = 0;
    if (!_placeRe.test(text)) return;
    _placeRe.lastIndex = 0;

    var frag = document.createDocumentFragment();
    var last = 0, m;

    while ((m = _placeRe.exec(text)) !== null) {
      var place = _placesByName[m[0].toLowerCase()];
      if (!place) continue;

      if (m.index > last) {
        frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      }

      frag.appendChild(_makePlaceAnchor(place, m[0]));
      last = m.index + m[0].length;
    }

    _placeRe.lastIndex = 0;

    if (last > 0) {
      if (last < text.length) {
        frag.appendChild(document.createTextNode(text.slice(last)));
      }
      textNode.parentNode.replaceChild(frag, textNode);
    }
  });
}

/* ── Idle-time full-page tagging ─────────────────────────────────────────── */
/* Only targets high-signal containers; avoids scanning every Bible verse. */
var _TARGETS = [
  '.reader-intro-inner',   /* book intro text */
  '.tl-detail-inner',      /* biblical timeline event detail */
  '.maps-detail-overview', /* map overview panel */
  '.topic-intro',          /* topic page introductions */
  '.study-guide-body'      /* study guide content */
];

export function runAutoTagPlaces() {
  loadPlaces().then(function () {
    _TARGETS.forEach(function (sel) {
      document.querySelectorAll(sel).forEach(function (el) {
        if (el._placesTagged) return;
        el._placesTagged = true;
        autoTagPlaces(el);
      });
    });
  });
}

/* Convenience wrapper for dynamic renders (reader.js, timeline.js): loads
   places if needed then immediately tags the supplied element.           */
export function autoTagPlacesIn(el) {
  if (!el || el._placesTagged) return;
  loadPlaces().then(function () {
    if (el._placesTagged) return;
    el._placesTagged = true;
    autoTagPlaces(el);
  });
}

/* ── Tooltip ─────────────────────────────────────────────────────────────── */
function _buildTip() {
  if (_tip) return;
  var el = document.createElement('div');
  el.id        = 'bsw-place-tip';
  el.className = 'bsw-place-tip';
  el.setAttribute('aria-hidden', 'true');
  document.body.appendChild(el);
  _tip = el;
  el.addEventListener('mouseenter', function () { _cancelHide(); });
  el.addEventListener('mouseleave', function () { _scheduleHide(); });
}

function _scheduleShow(anchor, place) {
  _cancelHide();
  if (_showTimer) clearTimeout(_showTimer);
  _showTimer = setTimeout(function () { _showTip(anchor, place); }, 230);
}

function _scheduleHide() {
  if (_showTimer) { clearTimeout(_showTimer); _showTimer = null; }
  _hideTimer = setTimeout(function () {
    if (_tip) {
      _tip.classList.remove('bsw-place-tip--visible');
      _tip.setAttribute('aria-hidden', 'true');
    }
  }, 200);
}

function _cancelHide() {
  if (_hideTimer) { clearTimeout(_hideTimer); _hideTimer = null; }
}

/* ── Accessors for the reader's place popup (reader-place.js) ────────────── */
export function getPlace(id) { return (_placesById && _placesById[id]) || null; }
export function getAllPlaces() { return _placesAll || []; }
/* Cancels a pending hover show and hides the tip — the popup takes over. */
export function hidePlaceTip() {
  if (_showTimer) { clearTimeout(_showTimer); _showTimer = null; }
  if (_tip) {
    _tip.classList.remove('bsw-place-tip--visible');
    _tip.setAttribute('aria-hidden', 'true');
  }
}

function _showTip(anchor, place) {
  _buildTip();
  var mapLabel = place.mapId.replace(/-/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); });
  _tip.innerHTML =
    '<div class="bsw-place-tip__header">' +
      ''+
      '<span class="bsw-place-tip__name">' + escHtml(place.name) + '</span>' +
    '</div>' +
    '<p class="bsw-place-tip__desc">' + escHtml(place.desc) + '</p>' +
    '<a class="bsw-place-tip__link" href="' + escHtml(placeMapHref(place)) + '" target="_blank" rel="noopener">' +
      'View on Map · ' + escHtml(mapLabel) + ' →' +
    '</a>';

  _tip.classList.add('bsw-place-tip--visible');
  _tip.setAttribute('aria-hidden', 'false');
  _positionTip(anchor);
}

function _positionTip(anchor) {
  if (!_tip) return;
  _tip.style.top  = '-9999px';
  _tip.style.left = '-9999px';
  var r  = anchor.getBoundingClientRect();
  var tt = _tip.getBoundingClientRect();
  var vw = window.innerWidth;
  var vh = window.innerHeight;
  var top  = r.bottom + window.scrollY + 6;
  var left = r.left   + window.scrollX;
  if (r.bottom + tt.height + 14 > vh) top = r.top + window.scrollY - tt.height - 6;
  if (left + tt.width > vw - 8)       left = vw - tt.width - 8;
  if (left < 8)                        left = 8;
  _tip.style.top  = top  + 'px';
  _tip.style.left = left + 'px';
}
