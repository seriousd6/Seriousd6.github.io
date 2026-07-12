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
    js.onerror = function () { _leafletReady = null; reject(new Error('Leaflet CDN unreachable')); };
    document.head.appendChild(js);
  });
  return _leafletReady;
}
