/* reader-place.js — the place popup: tap a tagged place in scripture and get
 * a verse-modal-style card instead of being bounced to the maps page.
 *
 * Contents: the place's description + its biblepedia brief, an era-aware
 * Leaflet mini-map (reading John puts Samaria in "Palestine in the Time of
 * Jesus", not the divided kingdom) showing the place highlighted among its
 * neighbors, and jump links — the map explorer (deep-linked so the place is
 * selected there too) and the full biblepedia article.
 *
 * The mini-map degrades offline to a note; the jump links always work.
 */
'use strict';

import { escHtml } from './core.js';
import { getPlace, getAllPlaces, hidePlaceTip, placeMapHref } from './places.js';
import { ensureLeaflet, CARTO_TILES, CARTO_ATTR } from './leaflet-loader.js';
import { _loadBPIndex } from './modal.js';

// ── Era selection ───────────────────────────────────────────────────────────
// The maps page's era maps, titled as maps.js titles them (subtitle text and
// the deep-link hash only — keep ids in sync with maps.js MAPS[].id).
var ERA_TITLES = {
  'patriarchal-journeys': 'Journeys of the Patriarchs',
  'exodus':               'The Exodus Route',
  'conquest':             'The Conquest of Canaan',
  'twelve-tribes':        'The Twelve Tribes of Israel',
  'judges':               'Israel in the Time of the Judges',
  'david-kingdom':        "David's Kingdom",
  'solomon-kingdom':      "Solomon's Kingdom",
  'divided-kingdom':      'The Divided Kingdom',
  'invasions':            'Assyrian and Babylonian Invasions',
  'return-exile':         'The Return from Exile',
  'intertestamental':     'Between the Testaments',
  'holy-land':            'Palestine in the Time of Jesus',
  'paul-journeys':        "Paul's Missionary Journeys",
  'seven-churches':       'The Seven Churches of Revelation',
  'ancient-near-east':    'The Ancient Near East',
  'jerusalem':            'Jerusalem',
};

// Which era map fits the book being read (coarse on purpose — it picks the
// map the reference belongs to, e.g. John → NT Palestine). Books not listed
// fall back to the place's own home map (place.mapId).
var BOOK_ERA = {
  genesis: 'patriarchal-journeys',
  exodus: 'exodus', leviticus: 'exodus', numbers: 'exodus', deuteronomy: 'exodus',
  joshua: 'conquest',
  judges: 'judges', ruth: 'judges',
  '1samuel': 'david-kingdom', '2samuel': 'david-kingdom', psalms: 'david-kingdom',
  proverbs: 'solomon-kingdom', ecclesiastes: 'solomon-kingdom', songofsolomon: 'solomon-kingdom',
  '1kings': 'divided-kingdom', '2kings': 'divided-kingdom',
  '1chronicles': 'divided-kingdom', '2chronicles': 'divided-kingdom',
  isaiah: 'invasions', jeremiah: 'invasions', lamentations: 'invasions', ezekiel: 'invasions',
  hosea: 'invasions', joel: 'invasions', amos: 'invasions', obadiah: 'invasions',
  jonah: 'invasions', micah: 'invasions', nahum: 'invasions', habakkuk: 'invasions',
  zephaniah: 'invasions', daniel: 'return-exile',
  ezra: 'return-exile', nehemiah: 'return-exile', esther: 'return-exile',
  haggai: 'return-exile', zechariah: 'return-exile', malachi: 'return-exile',
  matthew: 'holy-land', mark: 'holy-land', luke: 'holy-land', john: 'holy-land',
  acts: 'paul-journeys', romans: 'paul-journeys', '1corinthians': 'paul-journeys',
  '2corinthians': 'paul-journeys', galatians: 'paul-journeys', ephesians: 'paul-journeys',
  philippians: 'paul-journeys', colossians: 'paul-journeys', '1thessalonians': 'paul-journeys',
  '2thessalonians': 'paul-journeys', '1timothy': 'paul-journeys', '2timothy': 'paul-journeys',
  titus: 'paul-journeys', philemon: 'paul-journeys', hebrews: 'holy-land',
  james: 'holy-land', '1peter': 'paul-journeys', '2peter': 'paul-journeys',
  '1john': 'holy-land', '2john': 'holy-land', '3john': 'holy-land', jude: 'holy-land',
  revelation: 'seven-churches',
};

function _currentEra(place) {
  var nav = (typeof window !== 'undefined' && window._readerNavState) || null;
  return (nav && nav.bookId && BOOK_ERA[nav.bookId]) || place.mapId;
}

// ── Popup ───────────────────────────────────────────────────────────────────
var _backdrop = null;
var _leafletMap = null;

function _closePopup() {
  if (_leafletMap) { try { _leafletMap.remove(); } catch (e) {} _leafletMap = null; }
  if (_backdrop) { _backdrop.remove(); _backdrop = null; }
  document.removeEventListener('keydown', _onKey, true);
}
function _onKey(e) { if (e.key === 'Escape') { e.stopPropagation(); _closePopup(); } }

function _openPlacePopup(place) {
  _closePopup();
  hidePlaceTip();

  var era      = _currentEra(place);
  var eraTitle = ERA_TITLES[era] || '';
  var mapHref  = placeMapHref(place, era);

  _backdrop = document.createElement('div');
  _backdrop.className = 'bsw-placepop-backdrop';
  _backdrop.innerHTML =
    '<div class="bsw-placepop" role="dialog" aria-modal="true" aria-label="Place: ' + escHtml(place.name) + '">' +
      '<div class="bsw-placepop__head">' +
        '<div>' +
          '<div class="bsw-placepop__title">' + escHtml(place.name) + '</div>' +
          (eraTitle ? '<div class="bsw-placepop__era">' + escHtml(eraTitle) + '</div>' : '') +
        '</div>' +
        '<button class="bsw-placepop__close" aria-label="Close">&#x2715;</button>' +
      '</div>' +
      '<div class="bsw-placepop__body">' +
        '<p class="bsw-placepop__desc">' + escHtml(place.desc || '') + '</p>' +
        '<div class="bsw-placepop__map" aria-label="Map of ' + escHtml(place.name) + '"></div>' +
        '<div class="bsw-placepop__actions">' +
          '<a class="bsw-placepop__action" href="' + escHtml(mapHref) + '" target="_blank" rel="noopener">Open in map explorer &#x2192;</a>' +
        '</div>' +
      '</div>' +
    '</div>';
  document.body.appendChild(_backdrop);
  _backdrop.addEventListener('click', function (e) { if (e.target === _backdrop) _closePopup(); });
  _backdrop.querySelector('.bsw-placepop__close').addEventListener('click', _closePopup);
  document.addEventListener('keydown', _onKey, true);

  _fillMiniMap(place);
  _fillBiblepedia(place);
}

// Era-scoped mini-map: the place highlighted, its neighbors (nearest places
// from the same gazetteer, ~100 km box) as quiet dots with hover names.
function _fillMiniMap(place) {
  var mapEl = _backdrop && _backdrop.querySelector('.bsw-placepop__map');
  if (!mapEl || typeof place.lat !== 'number') { if (mapEl) mapEl.remove(); return; }
  ensureLeaflet().then(function () {
    if (!_backdrop || !_backdrop.querySelector('.bsw-placepop__map')) return;
    var L = window.L;
    _leafletMap = L.map(mapEl, { zoomControl: true, attributionControl: true, scrollWheelZoom: false });
    L.tileLayer(CARTO_TILES, { maxZoom: 19, attribution: CARTO_ATTR }).addTo(_leafletMap);
    _leafletMap.setView([place.lat, place.lon], 9);

    // Neighbors first so the target draws on top.
    getAllPlaces()
      .filter(function (p) {
        return p.id !== place.id &&
               Math.abs(p.lat - place.lat) < 0.9 && Math.abs(p.lon - place.lon) < 0.9;
      })
      .sort(function (a, b) {
        var da = Math.hypot(a.lat - place.lat, a.lon - place.lon);
        var db = Math.hypot(b.lat - place.lat, b.lon - place.lon);
        return da - db;
      })
      .slice(0, 12)
      .forEach(function (p) {
        L.circleMarker([p.lat, p.lon], {
          radius: 5, color: '#55682f', weight: 2, fillColor: '#55682f', fillOpacity: 0.25,
        }).addTo(_leafletMap).bindTooltip(escHtml(p.name));
      });

    // The tapped place: selected ring, label shown.
    L.circleMarker([place.lat, place.lon], {
      radius: 9, color: '#c0392b', weight: 3, fillColor: '#c0392b', fillOpacity: 0.25,
    }).addTo(_leafletMap).bindTooltip(escHtml(place.name), { permanent: true, direction: 'top' }).openTooltip();

    // The popup just animated in; Leaflet measured a mid-animation size.
    setTimeout(function () { if (_leafletMap) _leafletMap.invalidateSize(); }, 120);
  }).catch(function () {
    if (mapEl) {
      mapEl.classList.add('bsw-placepop__map--offline');
      mapEl.innerHTML = '<p>Map unavailable offline — the map explorer link below works when you reconnect.</p>';
    }
  });
}

// Biblepedia brief + full-article link, matched by place id then name.
function _fillBiblepedia(place) {
  _loadBPIndex().then(function (idx) {
    if (!_backdrop || !idx) return;
    var name = place.name.toLowerCase();
    var hit = idx.find(function (a) {
      return a.id === place.id || String(a.term || '').toLowerCase() === name;
    });
    if (!hit) return;
    var entry = hit.redirect ? (idx.find(function (a) { return a.id === hit.redirect; }) || hit) : hit;
    if (entry.brief && entry.brief !== place.desc) {
      var b = document.createElement('p');
      b.className = 'bsw-placepop__brief';
      b.textContent = entry.brief;
      var desc = _backdrop.querySelector('.bsw-placepop__desc');
      desc.insertAdjacentElement('afterend', b);
    }
    if (entry.has_article !== false && /^[a-z0-9.-]+$/.test(entry.id)) {
      var a = document.createElement('a');
      a.className = 'bsw-placepop__action';
      a.href = '/biblepedia/' + entry.id + '/';
      a.textContent = 'Full ' + (entry.term || place.name) + ' article →';
      _backdrop.querySelector('.bsw-placepop__actions').appendChild(a);
    }
  }).catch(function () {});
}

// ── Init ───────────────────────────────────────────────────────────────────
export function initPlacePopup() {
  var results = document.getElementById('reader-results');
  if (!results) return;
  // Capture phase, same reason as reader-wordtap.js: deeper reader handlers
  // stop propagation. Plain click only — modified clicks (new tab) keep the
  // anchor's own maps deep link.
  results.addEventListener('click', function (e) {
    var a = e.target.closest('a.map-place');
    if (!a) return;
    if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey || e.button !== 0) return;
    var place = getPlace(a.getAttribute('data-place-id'));
    if (!place) return;
    e.preventDefault();
    e.stopPropagation();
    _openPlacePopup(place);
  }, true);
}
