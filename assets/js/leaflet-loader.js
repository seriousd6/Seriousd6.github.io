/* leaflet-loader.js — one lazy Leaflet CDN load, shared by every surface that
 * renders a map outside /maps/ (biblepedia Location panels, the reader's
 * place popup). Rejects when the CDN is unreachable (offline PWA) — callers
 * degrade to a text note and keep their "open in map explorer" links.
 */
'use strict';

export var CARTO_TILES = 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';
export var CARTO_ATTR  = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>' +
                         ' &copy; <a href="https://carto.com/attributions">CARTO</a>';

var _leafletReady = null;

export function ensureLeaflet() {
  if (window.L) return Promise.resolve();
  if (_leafletReady) return _leafletReady;
  _leafletReady = new Promise(function (resolve, reject) {
    // Self-hosted (P16): unpkg was a single point of failure — blocked CDNs
    // and flaky mobile connections left the maps pages dead. The vendored
    // copy also precaches, so map chrome works offline (tiles still can't).
    var css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = '/assets/vendor/leaflet/leaflet.css';
    document.head.appendChild(css);
    var js = document.createElement('script');
    js.src = '/assets/vendor/leaflet/leaflet.js';
    js.onload = function () { resolve(); };
    js.onerror = function () { _leafletReady = null; reject(new Error('Leaflet failed to load')); };
    document.head.appendChild(js);
  });
  return _leafletReady;
}
