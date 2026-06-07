/* timelapse-map.js — Biblical History Time-Lapse (animated)
 *
 * Animation model:
 *   - _time runs 0 → TOTAL_TIME via requestAnimationFrame
 *   - Empires: pre-created Leaflet polygons; opacity interpolated each frame
 *   - Routes:  pre-created Leaflet polylines; coords grow progressively
 *   - Figures: pre-created Leaflet markers; position interpolated each frame
 *   - Events:  info panel updates when nearest event changes
 *
 * No layer destroy/recreate on every frame — only setStyle / setLatLng / setLatLngs.
 */
'use strict';

import { escHtml } from './core.js';
import { wireRefLinks } from './wire.js';

var _DATA_URL  = new URL('../../data/maps/timelapse.json', import.meta.url).href;
var TILE_URL   = 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';
var TILE_ATTR  = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>';

var TOTAL_TIME = 1080;   /* time units (0 = 2100 BC, 1080 = AD 100) */
var SPEED_MAP  = { slow: 5, normal: 12, fast: 30 }; /* time units / second */

/* ── Era → static-map cross-link table ───────────────────────────────────── */
var ERA_TO_MAP = {
  'The Patriarchs':         'patriarchal-journeys',
  'Moses & the Exodus':     'exodus',
  'Conquest & Judges':      'conquest',
  'The Monarchy':           'david-kingdom',
  'Exile & Return':         'return-exile',
  'Between the Testaments': 'intertestamental',
  'Life of Christ':         'holy-land',
  'The Early Church':       'paul-journeys'
};

/* ── State ───────────────────────────────────────────────────────────────── */
var _map          = null;
var _data         = null;
var _time         = 0;
var _playing      = false;
var _raf          = null;
var _lastTs       = null;
var _speed        = 12;
var _lastEventIdx = -1;

/* Step-mode: auto-pause at each event boundary */
var _stepMode      = true;
var _lastPausedIdx = -1;

/* Pre-created layer references */
var _empLayers   = {};   /* id → L.polygon */
var _routeLayers = {};   /* id → L.polyline */
var _figLayers   = {};   /* id → L.marker   */
var _placeLayers = {};   /* id → L.marker (divIcon dot) */
var _placeTipEl    = null; /* combined stacking tooltip (dots + route) */
var _hoveredRoute  = null; /* route currently under cursor — read by _onPlaceMouseMove */
var _tribeLayers = {};   /* id → { poly, label } */
var _tribeTipEl  = null; /* custom tribe tooltip — bottom-right corner at cursor */

/* Side-panel DOM cache — avoid rebuilding every animation frame */
var _visibleEmpKey = '';   /* serialized key of currently shown empires */
var _visibleFigKey = '';   /* serialized key of currently shown figures */

/* ── Year display helper ─────────────────────────────────────────────────── */
function _yearFromT(t) {
  /* linear: t=0 → 2100 BC, t=1080 → AD 100 */
  var raw = 2100 - (t / TOTAL_TIME) * 2200;
  if (raw > 0.5)  return 'c. ' + Math.round(raw)  + ' BC';
  if (raw <= 0.5 && raw >= -0.5) return 'c. 1 BC / AD 1';
  return 'c. AD ' + Math.round(-raw);
}

/* ── Init ────────────────────────────────────────────────────────────────── */
// INTENT: Fetch timelapse.json, initialise Leaflet + all pre-built event layers,
//   wire playback controls and the RAF animation loop, then honour a #t=<n>
//   deep-link to jump to a specific time offset on load.
// CHANGE? _DATA_URL resolves relative to this module file (assets/js/); if
//   this file moves, update _DATA_URL. TOTAL_TIME must match the last event's
//   .t field in timelapse.json or the slider will clamp early — update both
//   together. Leaflet map instance is stored in module-level _map; if multiple
//   timelapse instances were ever needed, that would need to change.
// VERIFY: Load /maps/timelapse/ → map renders with events ✓. Load
//   /maps/timelapse/#t=400 → map jumps to t=400 ✓. Play 3s, pause, scrub →
//   resume plays from scrubbed position ✓.
export function initTimelapsePage() {
  if (!document.getElementById('tl-map')) return;
  if (!window.L) { document.getElementById('tl-map').textContent = 'Map library failed to load.'; return; }

  _map = L.map('tl-map', { zoomControl: true, attributionControl: true });
  L.tileLayer(TILE_URL, { maxZoom: 19, attribution: TILE_ATTR }).addTo(_map);
  _map.setView([33, 38], 5);

  fetch(_DATA_URL)
    .then(function (r) { return r.json(); })
    .then(function (d) {
      _data = d;
      _buildLayers();
      _buildEventList();
      _wireControls();
      _wireEventToggle();
      _wireEventSearch();
      _render(0);
      /* Honor #t=<n> deep-link from static maps page */
      var hashMatch = location.hash.match(/^#t=(\d+(?:\.\d+)?)$/);
      if (hashMatch) _seekTo(parseFloat(hashMatch[1]));
    })
    .catch(function (e) {
      console.error('[Timelapse] load failed:', e);
      var container = document.getElementById('tl-event-list') || document.getElementById('tl-container');
      if (container) container.innerHTML = '<p style="padding:1rem;color:var(--color-muted,#888)">Unable to load animated map data.</p>';
    });
}

/* ── Pre-build all Leaflet layers (called once after data loads) ──────────── */
function _buildLayers() {
  /* Empire polygons */
  (_data.empires || []).forEach(function (emp) {
    var poly = L.polygon(emp.coords, {
      color:       emp.color,
      weight:      1,
      fillColor:   emp.color,
      fillOpacity: 0,
      opacity:     0,
      dashArray:   '5 4',
      interactive: false
    });
    poly.addTo(_map);
    _empLayers[emp.id] = poly;

    /* Permanent label at centroid — visibility controlled via opacity */
    var icon = L.divIcon({
      className: 'tl-region-label',
      html: '<span>' + escHtml(emp.label) + '</span>',
      iconSize: [1,1], iconAnchor: [0,0]
    });
    var labelMarker = L.marker(poly.getBounds().getCenter(), {
      icon: icon, interactive: false, keyboard: false, opacity: 0
    });
    labelMarker.addTo(_map);
    emp._labelMarker = labelMarker;
  });

  /* Route polylines */
  // INTENT: Each route gets a slightly thicker transparent hit-area polyline stacked
  //   above the visible line so mouseover fires reliably on thin lines; the visible line
  //   carries color and animates via _renderRoutes. The hit line is always transparent.
  // CHANGE? _routeLayers[id] is the visible line. Route description is rendered inside
  //   _onPlaceMouseMove via _hoveredRoute. If route schema adds fields, update
  //   the _hoveredRoute HTML block in _onPlaceMouseMove.
  // VERIFY: Hover Paul's 1st Journey line — tooltip shows label + description text.
  (_data.routes || []).forEach(function (route) {
    var line = L.polyline([[0,0]], {
      color:     route.color,
      weight:    route.weight || 2.5,
      opacity:   0,
      lineCap:   'round',
      lineJoin:  'round',
      dashArray: route.dashed ? '8 5' : null,
      interactive: false
    });
    line.addTo(_map);
    line._routeId = route.id;
    _routeLayers[route.id] = line;

    /* Transparent wide hit line on top for easy hover */
    var hit = L.polyline([[0,0]], {
      color:    'transparent',
      weight:   14,
      opacity:  0,
      lineCap:  'round',
      lineJoin: 'round'
    });
    hit._routeId = route.id;
    hit.addTo(_map);
    /* Set _hoveredRoute so _onPlaceMouseMove includes the route in the shared stack */
    hit.on('mouseover', function (e) {
      var r = (_data.routes || []).find(function (x) { return x.id === e.target._routeId; });
      var vis = _routeLayers[e.target._routeId];
      if (r && vis && (vis.options.opacity || 0) > 0.01) { _hoveredRoute = r; _onPlaceMouseMove(e); }
    });
    hit.on('mousemove', _onPlaceMouseMove);
    hit.on('mouseout',  function () { _hoveredRoute = null; });
    line._hitLine = hit;
  });

  /* Figure markers */
  (_data.figures || []).forEach(function (fig) {
    var isJesus = fig.id === 'jesus';
    var dotStyle = isJesus
      ? 'background:#c8a84b;width:14px;height:14px;border:2px solid #fff;box-shadow:0 1px 6px rgba(0,0,0,.5);'
      : 'background:' + escHtml(fig.color || '#e63') + ';';
    var nameStyle = isJesus ? 'font-weight:800;' : '';
    var icon = L.divIcon({
      className: 'tl-figure-icon',
      html: '<span class="tl-figure-dot" style="' + dotStyle + '"></span>' +
            '<span class="tl-figure-name" style="' + nameStyle + '">' + escHtml(fig.label) + '</span>',
      iconSize: [isJesus ? 14 : 12, isJesus ? 14 : 12],
      iconAnchor: [isJesus ? 7 : 6, isJesus ? 7 : 6]
    });
    var marker = L.marker(
      [fig.positions[0].lat, fig.positions[0].lon],
      { icon: icon, interactive: true, keyboard: false, opacity: 0 }
    );
    marker.addTo(_map);
    _figLayers[fig.id] = marker;
  });

  /* Tribe polygons */
  (_data.tribes || []).forEach(function (tribe) {
    var poly = L.polygon(tribe.coords, {
      color: tribe.color,
      weight: 1,
      fillColor: tribe.color,
      fillOpacity: 0,
      opacity: 0,
      interactive: true
    });
    /* Custom tooltip so bottom-right corner sits exactly at the cursor tip */
    (function (t) {
      poly.on('mousemove', function (e) { _showTribeTip(t, e.originalEvent); });
      poly.on('mouseout',  _hideTribeTip);
    }(tribe));
    poly.addTo(_map);
    /* Centroid label */
    var bounds = poly.getBounds();
    var center = tribe.labelCenter
      ? L.latLng(tribe.labelCenter[0], tribe.labelCenter[1])
      : bounds.getCenter();
    var labelIcon = L.divIcon({
      className: 'tl-tribe-label',
      html: '<span>' + escHtml(tribe.label) + '</span>',
      iconSize: [1,1], iconAnchor: [0,0]
    });
    var labelMarker = L.marker(center, {
      icon: labelIcon, interactive: false, keyboard: false, opacity: 0
    });
    labelMarker.addTo(_map);
    _tribeLayers[tribe.id] = { poly: poly, label: labelMarker };
  });

  /* Place markers — L.marker with divIcon; no individual tooltip binding.
     A single map mousemove handler (_onPlaceMouseMove) finds all visible
     markers within 22px and renders a combined tooltip for all of them. */
  var placeIcon = L.divIcon({
    className:  'tl-place-dot',
    html:       '<span></span>',
    iconSize:   [12, 12],
    iconAnchor: [6, 6]
  });
  (_data.places || []).forEach(function (place) {
    var marker = L.marker([place.lat, place.lon], {
      icon:         placeIcon,
      interactive:  false,   /* hover handled at map level */
      keyboard:     false,
      opacity:      0,
      zIndexOffset: 100
    });
    marker._placeData = place;   /* stash for hover lookup */
    marker.addTo(_map);
    _placeLayers[place.id] = marker;
  });

  /* Build the shared tooltip elements and wire map-level hover */
  _placeTipEl = document.createElement('div');
  _placeTipEl.className = 'tl-place-tip';
  document.body.appendChild(_placeTipEl);
  _map.on('mousemove', _onPlaceMouseMove);
  _map.on('mouseout',  _hidePlaceTip);

  _tribeTipEl = document.createElement('div');
  _tribeTipEl.className = 'tl-tribe-tip';
  document.body.appendChild(_tribeTipEl);

  /* Slider ticks — only era-change events or major:true to avoid density */
  var ticks  = document.getElementById('tl-ticks');
  var slider = document.getElementById('tl-slider');
  if (slider) slider.max = TOTAL_TIME;

  if (ticks && _data.events) {
    var prevEra = null;
    _data.events.forEach(function (ev) {
      var isEraChange = ev.era !== prevEra;
      prevEra = ev.era;
      if (!isEraChange && !ev.major) return;
      var tick = document.createElement('span');
      tick.className   = 'tl-tick';
      tick.title       = ev.year + ' — ' + ev.label;
      tick.style.left  = ((ev.t / TOTAL_TIME) * 100) + '%';
      tick.addEventListener('click', function () {
        _seekTo(ev.t);
        if (_playing) _stopPlay();
      });
      ticks.appendChild(tick);
    });
  }
}

/* ── Controls ────────────────────────────────────────────────────────────── */
function _wireControls() {
  var slider     = document.getElementById('tl-slider');
  var playBtn    = document.getElementById('tl-play');
  var speedEl    = document.getElementById('tl-speed');
  var stepToggle = document.getElementById('tl-step-toggle');
  var continueBtn= document.getElementById('tl-continue');

  if (slider) {
    slider.value = 0;
    slider.addEventListener('input', function () {
      _seekTo(parseFloat(slider.value));
      if (_playing) _stopPlay();
    });
  }
  if (playBtn) {
    playBtn.addEventListener('click', function () {
      _playing ? _stopPlay() : _startPlay();
    });
  }
  if (speedEl) {
    speedEl.addEventListener('change', function () {
      _speed = SPEED_MAP[speedEl.value] || 12;
    });
  }
  if (stepToggle) {
    /* Reflect initial state */
    stepToggle.classList.toggle('tl-btn-step--active', _stepMode);
    stepToggle.addEventListener('click', _toggleStepMode);
  }
  if (continueBtn) {
    continueBtn.hidden = true;
    continueBtn.addEventListener('click', _continuePlay);
  }
}

function _seekTo(t) {
  _time = Math.max(0, Math.min(t, TOTAL_TIME));

  /* Reset step-mode pause index so Play after a seek pauses at this event */
  if (_data && _data.events) {
    var events = _data.events;
    var idx = 0;
    for (var i = 0; i < events.length; i++) {
      if (events[i].t <= _time) idx = i;
      else break;
    }
    _lastPausedIdx = idx - 1;
  }

  _render(_time);
  var slider = document.getElementById('tl-slider');
  if (slider) slider.value = _time;
}

function _startPlay() {
  if (_time >= TOTAL_TIME) _time = 0;
  _playing = true;
  _lastTs  = null;
  var btn = document.getElementById('tl-play');
  if (btn) btn.textContent = '⏸';
  _raf = requestAnimationFrame(_animLoop);
}

function _stopPlay() {
  _playing = false;
  if (_raf) { cancelAnimationFrame(_raf); _raf = null; }
  var btn = document.getElementById('tl-play');
  if (btn) btn.textContent = '▶';
}

function _continuePlay() {
  var cont = document.getElementById('tl-continue');
  if (cont) cont.hidden = true;
  _startPlay();
}

function _toggleStepMode() {
  _stepMode = !_stepMode;
  var btn = document.getElementById('tl-step-toggle');
  if (btn) {
    btn.classList.toggle('tl-btn-step--active', _stepMode);
    btn.setAttribute('aria-pressed', String(_stepMode));
  }
  /* If step mode disabled while the Continue button is showing, resume play */
  if (!_stepMode) {
    var cont = document.getElementById('tl-continue');
    if (cont && !cont.hidden) {
      cont.hidden = true;
      _startPlay();
    }
  }
}

// INTENT: Main RAF loop. Advances _time by _speed * delta each frame (where
//   delta = ms since last frame / 1000; _speed is events-per-second). Stopping
//   cancels the RAF via _stopPlay(); restarting reschedules it via _startPlay().
//   Manual scrubber drags update _time directly and call _render(), so the map
//   stays accurate during playback or pause.
// CHANGE? If you change _speed defaults, update the scrubber step size (tl-slider
//   step attribute) proportionally so a single drag step advances a meaningful amount.
// VERIFY: Play → Pause → drag scrubber → Play; animation should resume from the
//   dragged position, not jump back to where it was when paused.
function _animLoop(ts) {
  if (!_lastTs) _lastTs = ts;
  var dt = (ts - _lastTs) / 1000;
  _lastTs = ts;
  _time = Math.min(_time + dt * _speed, TOTAL_TIME);

  /* Step mode: pause the moment we cross the next unseen event boundary */
  if (_stepMode && _data) {
    var events  = _data.events || [];
    var nextIdx = _lastPausedIdx + 1;
    if (nextIdx < events.length && _time >= events[nextIdx].t) {
      _time          = events[nextIdx].t;
      _lastPausedIdx = nextIdx;
      _render(_time);
      var sliderEl = document.getElementById('tl-slider');
      if (sliderEl) sliderEl.value = _time;
      _stopPlay();
      var cont = document.getElementById('tl-continue');
      if (cont) cont.hidden = false;
      return;
    }
  }

  _render(_time);

  var slider = document.getElementById('tl-slider');
  if (slider) slider.value = _time;

  if (_time >= TOTAL_TIME) { _stopPlay(); return; }
  _raf = requestAnimationFrame(_animLoop);
}

/* ── Main render ─────────────────────────────────────────────────────────── */
function _render(t) {
  _renderEmpires(t);
  _renderRoutes(t);
  _renderFigures(t);
  _renderPlaces(t);
  _renderTribes(t);
  _renderInfo(t);
}

/* ── Empire opacity interpolation ───────────────────────────────────────── */
function _lerp(a, b, frac) { return a + (b - a) * frac; }

function _stageValue(stages, t, key) {
  if (!stages || !stages.length) return 0;
  if (t <= stages[0].t)                           return stages[0][key] || 0;
  var last = stages[stages.length - 1];
  if (t >= last.t)                                return last[key]      || 0;
  for (var i = 0; i < stages.length - 1; i++) {
    var s0 = stages[i], s1 = stages[i+1];
    if (t >= s0.t && t <= s1.t) {
      var frac = (t - s0.t) / (s1.t - s0.t);
      return _lerp(s0[key] || 0, s1[key] || 0, frac);
    }
  }
  return 0;
}

function _renderEmpires(t) {
  var visible = [];
  (_data.empires || []).forEach(function (emp) {
    var poly = _empLayers[emp.id];
    if (!poly) return;
    var fo = _stageValue(emp.stages, t, 'o');
    var bo = fo > 0.01 ? Math.min(fo + 0.08, 0.4) : 0;
    poly.setStyle({ fillOpacity: fo, opacity: bo });
    if (emp._labelMarker) emp._labelMarker.setOpacity(fo > 0.06 ? 1 : 0);
    if (fo > 0.04) visible.push({ id: emp.id, label: emp.label, color: emp.color });
  });

  /* Update side-panel empire list only when the visible set changes */
  var key = visible.map(function (e) { return e.id; }).join(',');
  if (key === _visibleEmpKey) return;
  _visibleEmpKey = key;
  var listEl = document.getElementById('tl-empire-list');
  if (!listEl) return;
  listEl.innerHTML = '';
  visible.forEach(function (e) {
    var row = document.createElement('div');
    row.className = 'tl-empire-item';
    row.innerHTML =
      '<span class="tl-empire-swatch" style="background:' + escHtml(e.color) + '"></span>' +
      '<span class="tl-empire-name">'  + escHtml(e.label) + '</span>';
    listEl.appendChild(row);
  });
}

/* ── Route progressive drawing ───────────────────────────────────────────── */
function _partialCoords(coords, progress) {
  if (progress <= 0) return [coords[0]];
  if (progress >= 1) return coords;
  var total  = coords.length - 1;
  var raw    = progress * total;
  var idx    = Math.floor(raw);
  var frac   = raw - idx;
  var result = coords.slice(0, idx + 1);
  if (frac > 0 && idx < total) {
    var p0 = coords[idx], p1 = coords[idx + 1];
    result = result.concat([[
      p0[0] + frac * (p1[0] - p0[0]),
      p0[1] + frac * (p1[1] - p0[1])
    ]]);
  }
  return result;
}

function _renderRoutes(t) {
  (_data.routes || []).forEach(function (route) {
    var line = _routeLayers[route.id];
    if (!line) return;

    /* Figure-linked routes: stay visible while the figure is alive */
    var figureActive = false;
    if (route.figureId) {
      var fig = (_data.figures || []).find(function (f) { return f.id === route.figureId; });
      if (fig) figureActive = _figurePos(fig.positions, t, fig.end) !== null;
    }

    var linger = route.linger != null ? route.linger : 120;
    var totalWindow = route.end + (figureActive ? 0 : linger) + 80;
    if (t < route.start || t > totalWindow) {
      line.setStyle({ opacity: 0 });
      if (line._hitLine) line._hitLine.setStyle({ opacity: 0 });
      return;
    }

    /* Draw phase: start → end */
    var progress = Math.min((t - route.start) / Math.max(route.end - route.start, 1), 1);
    /* Fade: figure-linked routes only fade after the figure disappears */
    var fadeStart = route.figureId
      ? (figureActive ? Infinity : route.end)
      : route.end + linger;
    var alpha = 1;
    if (t > fadeStart) alpha = Math.max(0, 1 - (t - fadeStart) / 80);
    var partial = _partialCoords(route.coords, progress);
    if (partial.length >= 2) {
      line.setLatLngs(partial);
      line.setStyle({ opacity: alpha * (route.opacity || 0.85) });
      /* Keep hit line in sync so hover only works when the route is visible */
      if (line._hitLine) {
        line._hitLine.setLatLngs(partial);
        line._hitLine.setStyle({ opacity: alpha > 0.05 ? 0.001 : 0 });
      }
    } else {
      line.setStyle({ opacity: 0 });
      if (line._hitLine) line._hitLine.setStyle({ opacity: 0 });
    }
  });
}

/* ── Figure position interpolation ──────────────────────────────────────── */
// INTENT: Linearly interpolates lat/lon between the two positions[] entries that
//   bracket the current time t. Returns null if t is before the first position
//   (not yet visible), after fig.end (explicit exit), or more than 50 units past
//   the last position (linger window expired). The null return is the signal to
//   hide the figure's Leaflet marker by setting opacity to 0.
// CHANGE? If you add a new figure, ensure positions[] entries are sorted by t
//   ascending and that fig.end is set; without end, the figure lingers 50 units
//   past its last waypoint and may overlap the next historical era.
// VERIFY: Scrub to t=633 (Elijah translated); the Elijah marker should disappear
//   at exactly t=633, not linger into the Elisha era.
function _figurePos(positions, t, end) {
  if (!positions || !positions.length) return null;
  if (t < positions[0].t) return null; /* not yet visible */
  if (end != null && t > end) return null; /* explicit exit time */
  var last = positions[positions.length - 1];
  if (t > last.t + 50)   return null; /* linger expired */
  if (t >= last.t) return { lat: last.lat, lon: last.lon, note: last.note };

  for (var i = 0; i < positions.length - 1; i++) {
    var p0 = positions[i], p1 = positions[i+1];
    if (t >= p0.t && t <= p1.t) {
      var frac = (t - p0.t) / (p1.t - p0.t);
      return {
        lat:  _lerp(p0.lat, p1.lat, frac),
        lon:  _lerp(p0.lon, p1.lon, frac),
        note: frac < 0.5 ? p0.note : p1.note
      };
    }
  }
  return null;
}

function _renderFigures(t) {
  var visible = [];
  (_data.figures || []).forEach(function (fig) {
    var marker = _figLayers[fig.id];
    if (!marker) return;
    var pos = _figurePos(fig.positions, t, fig.end);
    if (!pos) { marker.setOpacity(0); marker._figData = null; return; }
    marker.setLatLng([pos.lat, pos.lon]);
    marker.setOpacity(1);
    // INTENT: Store current figure state on the marker so _onPlaceMouseMove can
    //   include figures in the same stacking tooltip as place dots — avoids native
    //   Leaflet tooltips (which render a separate, non-stacking tooltip per marker).
    // CHANGE? If fig.color or pos.note schema changes, update _onPlaceMouseMove
    //   which reads marker._figData.{label, color, note}.
    marker._figData = { label: fig.label, color: fig.color || '#e63', note: pos.note || '' };
    visible.push({ id: fig.id, label: fig.label, color: fig.color, note: pos.note || '' });
  });

  /* Update side-panel figures list only when the visible set or notes change */
  var key = visible.map(function (f) { return f.id + ':' + f.note; }).join('|');
  if (key === _visibleFigKey) return;
  _visibleFigKey = key;
  var figEl = document.getElementById('tl-figures');
  if (!figEl) return;
  figEl.innerHTML = '';
  visible.forEach(function (f) {
    var item = document.createElement('div');
    item.className = 'tl-figure-item';
    item.innerHTML =
      '<span class="tl-figure-item__name" style="color:' + escHtml(f.color || '#c44d29') + '">' +
        escHtml(f.label) + '</span>' +
      (f.note ? '<span class="tl-figure-item__note">' + escHtml(f.note) + '</span>' : '');
    figEl.appendChild(item);
  });
}

/* ── Info panel ──────────────────────────────────────────────────────────── */
function _renderInfo(t) {
  /* Find the nearest event at or before current time */
  var events = _data.events || [];
  var idx = 0;
  for (var i = 0; i < events.length; i++) {
    if (events[i].t <= t) idx = i;
    else break;
  }

  /* Update year display always */
  var yearEl = document.getElementById('tl-info-year');
  if (yearEl) yearEl.textContent = _yearFromT(t);

  /* Only update info panel text when event changes */
  if (idx === _lastEventIdx) return;
  _lastEventIdx = idx;

  var ev = events[idx];
  if (!ev) return;

  var contentEl = document.getElementById('tl-info-content');
  var eraEl     = document.getElementById('tl-info-era');
  var labelEl   = document.getElementById('tl-info-label');
  var descEl    = document.getElementById('tl-info-desc');
  var refsEl    = document.getElementById('tl-info-refs');
  var listEl    = document.getElementById('tl-event-list');

  /* Fade out, update, fade back in */
  if (contentEl) contentEl.style.opacity = '0';

  if (eraEl)   eraEl.textContent   = ev.era   || '';
  if (labelEl) labelEl.textContent = ev.label || '';
  if (descEl) {
    descEl.textContent = ev.desc || '';
    /* Remove any previously rendered desc_extended block */
    var prevDetails = descEl.nextElementSibling;
    if (prevDetails && prevDetails.classList.contains('tl-desc-extended')) {
      prevDetails.remove();
    }
    /* Render desc_extended if present */
    if (ev.desc_extended) {
      var details = document.createElement('details');
      details.className = 'tl-desc-extended';
      var summary = document.createElement('summary');
      summary.textContent = 'Read more';
      var extP = document.createElement('p');
      extP.textContent = ev.desc_extended;
      details.appendChild(summary);
      details.appendChild(extP);
      descEl.insertAdjacentElement('afterend', details);
    }
  }

  /* Rebuild scripture ref chips */
  if (refsEl) {
    refsEl.innerHTML = '';
    if (ev.refs && ev.refs.length) {
      ev.refs.forEach(function (ref) {
        var a = document.createElement('a');
        a.className = 'ref tl-ref-chip';
        a.setAttribute('data-ref', ref);
        a.textContent = ref;
        refsEl.appendChild(a);
      });
      wireRefLinks(refsEl);
    }
  }

  if (contentEl) {
    /* Double rAF ensures the browser renders opacity:0 before animating back */
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { contentEl.style.opacity = '1'; });
    });
  }

  /* Scroll the event list */
  if (listEl) {
    listEl.querySelectorAll('.tl-ev-item').forEach(function (el, i) {
      el.classList.toggle('tl-ev-item--active', i === idx);
    });
    var active = listEl.querySelector('.tl-ev-item--active');
    if (active) active.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  }

  /* Update static-map deep-link in the info panel */
  var mapLinkEl = document.getElementById('tl-map-link');
  if (mapLinkEl) {
    var mapId = ERA_TO_MAP[ev.era];
    if (mapId) {
      mapLinkEl.href    = '../#' + mapId;
      mapLinkEl.hidden  = false;
    } else {
      mapLinkEl.hidden  = true;
    }
  }

  /* Pan map to event's suggested center if specified */
  if (ev.center && ev.zoom && _map) {
    _map.flyTo(ev.center, ev.zoom, { animate: true, duration: 0.8 });
  }
}

/* ── Place markers ───────────────────────────────────────────────────────── */
function _renderPlaces(t) {
  (_data.places || []).forEach(function (place) {
    var marker = _placeLayers[place.id];
    if (!marker) return;
    var visible = (t >= (place.visibleFrom || 0)) && (t <= (place.visibleTo || TOTAL_TIME));
    marker.setOpacity(visible ? 1 : 0);
  });
}

/* ── Place + figure proximity tooltip ────────────────────────────────────── */
// INTENT: Single map-level mousemove handler builds one stacking tooltip for all
//   visible place dots AND figure markers within _PLACE_HIT_PX of the cursor.
//   Place dots are non-interactive (interactive:false) so they can't bindTooltip;
//   figures previously used native bindTooltip which rendered separately and couldn't
//   stack. Now both share this handler so the tooltip always shows everything nearby.
// CHANGE? If place marker positions or figure marker positions diverge from
//   _placeLayers/_figLayers, update the two forEach loops. If _figData schema
//   changes (set in _renderFigures), update the figure HTML block below.
// VERIFY: On the timelapse map, position the slider so a named figure (e.g. Moses)
//   is near a place dot → hovering between them shows both in one stacked tooltip.
var _PLACE_HIT_PX = 22;   /* pixel radius that counts as "hovering this dot" */

function _onPlaceMouseMove(e) {
  if (!_data || !_placeTipEl) return;
  var pt = e.containerPoint;
  var nearby = [];

  (_data.places || []).forEach(function (place) {
    var visible = (_time >= (place.visibleFrom || 0)) && (_time <= (place.visibleTo || TOTAL_TIME));
    if (!visible) return;
    var marker = _placeLayers[place.id];
    if (!marker) return;
    var mPt = _map.latLngToContainerPoint(marker.getLatLng());
    if (pt.distanceTo(mPt) <= _PLACE_HIT_PX) nearby.push({ type: 'place', data: place });
  });

  /* Also check visible figure markers */
  Object.keys(_figLayers).forEach(function (id) {
    var marker = _figLayers[id];
    if (!marker || !marker._figData) return;  /* _figData=null means hidden (set by _renderFigures) */
    var mPt = _map.latLngToContainerPoint(marker.getLatLng());
    if (pt.distanceTo(mPt) <= _PLACE_HIT_PX) nearby.push({ type: 'figure', data: marker._figData });
  });

  if (!nearby.length && !_hoveredRoute) { _hidePlaceTip(); return; }

  /* Build combined HTML — dots first, then hovered route (with separator) */
  var html = '';
  nearby.forEach(function (item, i) {
    if (i > 0) html += '<div class="tl-place-tip-sep"></div>';
    if (item.type === 'figure') {
      var fd = item.data;
      html += '<div class="tl-place-tt-label tl-fig-tt-label" style="border-left-color:' +
              escHtml(fd.color) + '">' + escHtml(fd.label) + '</div>' +
              (fd.note ? '<div class="tl-place-tt-sig">' + escHtml(fd.note) + '</div>' : '');
    } else {
      var place = item.data;
      html += '<div class="tl-place-tt-label">' + escHtml(place.label) + '</div>' +
              '<div class="tl-place-tt-sig">'   + escHtml(place.significance || '') + '</div>';
    }
  });
  if (_hoveredRoute) {
    if (html) html += '<div class="tl-place-tip-sep"></div>';
    html += '<div class="tl-route-tt-label" style="border-left-color:' +
            escHtml(_hoveredRoute.color || '#999') + '">' + escHtml(_hoveredRoute.label) + '</div>' +
            (_hoveredRoute.description
              ? '<div class="tl-route-tt-desc">' + escHtml(_hoveredRoute.description) + '</div>' : '');
  }

  _placeTipEl.innerHTML = html;
  _placeTipEl.style.display = 'block';

  /* Position above-right of cursor; clamp to viewport on next frame when size is known.
     If the single-column tooltip exceeds the viewport height, switch to two columns so
     many stacked entries don't cascade off-screen. getBoundingClientRect() forces a
     synchronous reflow so the post-class measurements are accurate. */
  var cx = e.originalEvent.clientX, cy = e.originalEvent.clientY;
  _placeTipEl.style.left = (cx + 14) + 'px';
  _placeTipEl.style.top  = (cy - 14) + 'px';
  requestAnimationFrame(function () {
    if (_placeTipEl.style.display === 'none') return;
    /* Reset to single-column before measuring so re-entries don't accumulate wide class */
    _placeTipEl.classList.remove('tl-place-tip--wide');
    var r = _placeTipEl.getBoundingClientRect();
    /* Switch to two-column layout when content would overflow the viewport */
    if (r.height > window.innerHeight - 48) {
      _placeTipEl.classList.add('tl-place-tip--wide');
      r = _placeTipEl.getBoundingClientRect();   /* re-measure after reflow */
    }
    var x = cx + 14, y = cy - r.height - 8;
    if (x + r.width  > window.innerWidth  - 8) x = cx - r.width - 14;
    if (y < 8)                                  y = cy + 14;
    if (y + r.height > window.innerHeight - 8) y = window.innerHeight - r.height - 8;
    _placeTipEl.style.left = x + 'px';
    _placeTipEl.style.top  = y + 'px';
  });
}

function _hidePlaceTip() {
  if (_placeTipEl) {
    _placeTipEl.style.display = 'none';
    _placeTipEl.classList.remove('tl-place-tip--wide');
  }
}

/* ── Tribe tooltip — bottom-right corner at cursor ───────────────────────── */
function _showTribeTip(tribe, domEvent) {
  if (!_tribeTipEl) return;
  _tribeTipEl.innerHTML =
    '<div class="tl-tribe-tt-name">'   + escHtml(tribe.label)     + '</div>' +
    (tribe.patriarch
      ? '<div class="tl-tribe-tt-detail">' + escHtml(tribe.patriarch) + '</div>' : '') +
    (tribe.verse
      ? '<div class="tl-tribe-tt-verse">'  + escHtml(tribe.verse)     + '</div>' : '');
  _tribeTipEl.style.display = 'block';
  /* Position bottom-right at cursor after render so we have real dimensions */
  var cx = domEvent.clientX, cy = domEvent.clientY;
  requestAnimationFrame(function () {
    if (!_tribeTipEl || _tribeTipEl.style.display === 'none') return;
    var w = _tribeTipEl.offsetWidth, h = _tribeTipEl.offsetHeight;
    var x = cx - w, y = cy - h;
    /* Clamp so tip never disappears off screen edges */
    if (x < 4) x = cx + 4;
    if (y < 4) y = cy + 4;
    _tribeTipEl.style.left = x + 'px';
    _tribeTipEl.style.top  = y + 'px';
  });
}

function _hideTribeTip() {
  if (_tribeTipEl) _tribeTipEl.style.display = 'none';
}

/* ── Tribal boundary overlays ────────────────────────────────────────────── */
/* Tribes appear at t=390, fade out at t=580 */
var _TRIBE_FADE_IN  = 380;   /* fade starts here, reaches full at t=390 (Land Divided) */
var _TRIBE_HOLD     = 574;
var _TRIBE_FADE_OUT = 580;

function _renderTribes(t) {
  var alpha = 0;
  if (t >= _TRIBE_FADE_IN && t <= _TRIBE_HOLD) {
    alpha = Math.min((t - _TRIBE_FADE_IN) / 10, 1);
  } else if (t > _TRIBE_HOLD && t <= _TRIBE_FADE_OUT) {
    alpha = Math.max(0, 1 - (t - _TRIBE_HOLD) / (_TRIBE_FADE_OUT - _TRIBE_HOLD));
  }
  Object.keys(_tribeLayers).forEach(function (id) {
    var entry = _tribeLayers[id];
    entry.poly.setStyle({ fillOpacity: alpha * 0.22, opacity: alpha * 0.5 });
    entry.label.setOpacity(alpha > 0.3 ? 1 : 0);
    /* Disable SVG pointer-events on invisible polygons so they can't
       intercept clicks or trigger tooltips over figure dots */
    var el = entry.poly.getElement();
    if (el) el.style.pointerEvents = alpha > 0 ? '' : 'none';
  });
}

/* ── Event list sidebar (built once after data loads) ───────────────────── */
function _buildEventList() {
  var listEl = document.getElementById('tl-event-list');
  if (!listEl || !_data) return;

  /* Build era → color lookup from _data.eras if present */
  var eraColors = {};
  (_data.eras || []).forEach(function (era) { eraColors[era.id] = era.color; });

  listEl.innerHTML = '';
  (_data.events || []).forEach(function (ev, i) {
    var color = eraColors[ev.era] || 'var(--color-border, #ddd)';
    var item = document.createElement('div');
    item.className = 'tl-ev-item';
    item.style.borderLeftColor = color;
    item.innerHTML =
      '<span class="tl-ev-year">' + escHtml(ev.year) + '</span>' +
      '<span class="tl-ev-label">' + escHtml(ev.label) + '</span>';
    item.addEventListener('click', function () {
      _seekTo(ev.t);
      if (_playing) _stopPlay();
    });
    listEl.appendChild(item);
  });
}

/* ── Event list text filter ──────────────────────────────────────────────── */
// INTENT: Filter visible event items by search query. Shows a "No events match" message
//   when all items are hidden so the user knows the query returned zero results.
// CHANGE? If .tl-ev-item selector changes, update both the filter loop and the count check.
// VERIFY: Open /maps/timelapse/, type "zzz" → "No events match" message; clear input → list restores.
function _wireEventSearch() {
  var input  = document.getElementById('tl-event-search');
  var listEl = document.getElementById('tl-event-list');
  if (!input || !listEl) return;
  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase();
    var visible = 0;
    listEl.querySelectorAll('.tl-ev-item').forEach(function (el) {
      var show = !q || el.textContent.toLowerCase().includes(q);
      el.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    var emptyEl = listEl.querySelector('.tl-ev-empty');
    if (!visible && q) {
      if (!emptyEl) {
        emptyEl = document.createElement('p');
        emptyEl.className = 'tl-ev-empty';
        listEl.appendChild(emptyEl);
      }
      emptyEl.textContent = 'No events match "' + q + '"';
    } else if (emptyEl) {
      emptyEl.remove();
    }
  });
}

/* ── Mobile event-list toggle ────────────────────────────────────────────── */
function _wireEventToggle() {
  var btn    = document.getElementById('tl-events-toggle');
  var col    = document.querySelector('.tl-event-col');
  if (!btn || !col) return;
  /* On mobile the column is always in DOM; toggle is only shown via CSS */
  btn.addEventListener('click', function () {
    var hidden = col.style.display === 'none';
    col.style.display = hidden ? '' : 'none';
  });
}
