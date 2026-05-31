/* timeline.js — Biblical Timeline page (3-column: eras → events → detail) */
'use strict';

import { _resolve, escHtml, READER_URL } from './core.js';
import { wireRefLinks, autoTagRefs } from './wire.js';
import { autoTagTermsWhenReady } from './terms.js';

var EVENTS_URL = _resolve('../../data/timeline/events.json');
var DETAIL_URL = _resolve('../../data/timeline/detail.json');

var _data        = null;  // events.json { eras, events }
var _detailCache = null;  // detail.json keyed by event id
var _detailProm  = null;  // in-flight fetch promise (singleton)
var _activeEra   = null;  // currently selected era id
var _activeId    = null;  // currently selected event id

export function initTimelinePage() {
  var spine = document.getElementById('tl2-eras-spine');
  if (!spine) return;

  fetch(EVENTS_URL)
    .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function(data) {
      _data = data;
      _renderEraSpine();
    })
    .catch(function(err) {
      console.error('[Timeline] load error:', err);
      spine.innerHTML = '<p style="padding:1rem;color:var(--color-muted)">Unable to load timeline data.</p>';
    });
}

/* ── Proportional positioning ─────────────────────────────────────────────── */
/* Maps an array of yearNums to top% values (0-100) preserving relative order.
   minGap% prevents labels from overlapping when events cluster in time.
   A 4/92 buffer shrinks the usable range so edge nodes aren't clipped. */
function _proportionalPositions(yearNums, minGap) {
  if (yearNums.length === 1) return [50];

  var minY = Math.min.apply(null, yearNums);
  var maxY = Math.max.apply(null, yearNums);
  var span = maxY - minY || 1;

  var pcts = yearNums.map(function(y) { return (y - minY) / span * 100; });

  // forward pass: enforce minimum gap between consecutive nodes
  for (var i = 1; i < pcts.length; i++) {
    if (pcts[i] - pcts[i - 1] < minGap) {
      pcts[i] = pcts[i - 1] + minGap;
    }
  }

  // scale back to 0-100 if the enforcement pushed us past 100
  var hi = pcts[pcts.length - 1];
  if (hi > 100) {
    pcts = pcts.map(function(p) { return p / hi * 100; });
  }

  // add top/bottom buffer so no node is cut off at the edge
  return pcts.map(function(p) { return 4 + p * 0.92; });
}

/* ── Column 1: Era spine ──────────────────────────────────────────────────── */

function _renderEraSpine() {
  var wrap = document.getElementById('tl2-eras-spine');
  if (!wrap || !_data) return;

  // find the earliest event yearNum per era for positioning
  var eraMin = {};
  _data.events.forEach(function(ev) {
    if (eraMin[ev.era] === undefined || ev.yearNum < eraMin[ev.era]) {
      eraMin[ev.era] = ev.yearNum;
    }
  });

  // only keep eras that have events, sorted chronologically
  var eras = _data.eras.filter(function(e) { return eraMin[e.id] !== undefined; });
  eras.sort(function(a, b) { return eraMin[a.id] - eraMin[b.id]; });

  var positions = _proportionalPositions(
    eras.map(function(e) { return eraMin[e.id]; }),
    6   // 6% minimum gap keeps era labels from overlapping
  );

  eras.forEach(function(era, i) {
    wrap.appendChild(_makeEraNode(era, positions[i], eraMin[era.id]));
  });
}

function _makeEraNode(era, pct, minYear) {
  var btn = document.createElement('button');
  btn.className     = 'tl2-era-node';
  btn.style.top     = pct + '%';
  btn.dataset.eraId = era.id;
  btn.setAttribute('aria-label', era.label);

  var dot = document.createElement('span');
  dot.className        = 'tl2-node-dot';
  dot.style.background = era.color;

  var text = document.createElement('span');
  text.className = 'tl2-node-text';

  var lbl = document.createElement('span');
  lbl.className   = 'tl2-node-label';
  lbl.textContent = era.label;

  var yr = document.createElement('span');
  yr.className   = 'tl2-node-year';
  yr.textContent = minYear < 0 ? 'c. ' + Math.abs(minYear) + ' BC' : 'AD ' + minYear;

  text.appendChild(lbl);
  text.appendChild(yr);
  btn.appendChild(dot);
  btn.appendChild(text);

  btn.addEventListener('click', function() { _selectEra(era); });
  return btn;
}

/* ── Column 2: Event spine ────────────────────────────────────────────────── */

function _renderEventSpine(era) {
  var wrap  = document.getElementById('tl2-events-spine');
  var label = document.getElementById('tl2-events-label');
  if (!wrap) return;

  // update column header to show selected era
  if (label) {
    label.innerHTML =
      '<span class="tl2-col-era-dot" style="background:' + era.color + '"></span>' +
      escHtml(era.label);
  }

  var events = _data.events.filter(function(ev) { return ev.era === era.id; });
  events.sort(function(a, b) { return a.yearNum - b.yearNum; });

  var positions = _proportionalPositions(
    events.map(function(ev) { return ev.yearNum; }),
    7   // 7% minimum gap for sub-event labels
  );

  wrap.innerHTML = '';
  events.forEach(function(ev, i) {
    wrap.appendChild(_makeEventNode(ev, era, positions[i]));
  });
}

function _makeEventNode(ev, era, pct) {
  var btn = document.createElement('button');
  btn.className      = 'tl2-event-node';
  btn.style.top      = pct + '%';
  btn.dataset.eventId = ev.id;
  btn.setAttribute('aria-label', ev.label);

  var dot = document.createElement('span');
  dot.className        = 'tl2-node-dot tl2-node-dot--sm';
  dot.style.background = era.color;

  var text = document.createElement('span');
  text.className = 'tl2-node-text';

  var lbl = document.createElement('span');
  lbl.className   = 'tl2-node-label';
  lbl.textContent = ev.label;

  var yr = document.createElement('span');
  yr.className   = 'tl2-node-year';
  yr.textContent = ev.yearDisplay;

  text.appendChild(lbl);
  text.appendChild(yr);
  btn.appendChild(dot);
  btn.appendChild(text);

  btn.addEventListener('click', function() { _clickEvent(ev, era); });
  return btn;
}

/* ── Selection handlers ───────────────────────────────────────────────────── */

function _selectEra(era) {
  _activeEra = era.id;
  _activeId  = null;

  document.querySelectorAll('.tl2-era-node').forEach(function(n) {
    n.classList.toggle('tl2-era-node--active', n.dataset.eraId === era.id);
  });

  // reset detail column to placeholder
  var detail = document.getElementById('tl-detail');
  if (detail) detail.innerHTML = '<p class="tl2-placeholder">← Select an event</p>';

  _renderEventSpine(era);
}

function _clickEvent(ev, era) {
  // toggle off if already selected
  if (_activeId === ev.id) {
    _activeId = null;
    document.querySelectorAll('.tl2-event-node').forEach(function(n) {
      n.classList.remove('tl2-event-node--active');
    });
    var detail = document.getElementById('tl-detail');
    if (detail) detail.innerHTML = '<p class="tl2-placeholder">← Select an event</p>';
    return;
  }

  _activeId = ev.id;

  document.querySelectorAll('.tl2-event-node').forEach(function(n) {
    n.classList.toggle('tl2-event-node--active', n.dataset.eventId === ev.id);
  });

  // show loading state immediately
  var panel = document.getElementById('tl-detail');
  if (panel) {
    panel.innerHTML = _buildDetailShell(ev, era, '<div class="tl-detail-loading">Loading…</div>');
  }

  _loadDetail().then(function(details) {
    if (_activeId !== ev.id) return;  // selection changed while loading
    var detail = (details && details[ev.id]) || null;
    if (panel) {
      panel.innerHTML = _buildDetailShell(ev, era, _buildDetailBody(ev, detail));
      // Wire data-ref verse badges (hover tooltip + verse modal).
      wireRefLinks(panel);
      // Tag plain-text Bible references in the body prose (e.g. "Genesis 1:1").
      autoTagRefs();
      // Tag theological terms (dictionary, Nave's topics, Smith's, Hitchcock names).
      // .tl-detail-body is a new DOM node each injection so _termsTagged is unset.
      var detailBody = panel.querySelector('.tl-detail-body');
      if (detailBody) autoTagTermsWhenReady(detailBody);
      _wireDetailClose();
    }
  });
}

/* ── Detail: lazy-load detail.json once ──────────────────────────────────── */

function _loadDetail() {
  if (_detailCache) return Promise.resolve(_detailCache);
  if (_detailProm)  return _detailProm;
  _detailProm = fetch(DETAIL_URL)
    .then(function(r) { return r.ok ? r.json() : {}; })
    .then(function(d) { _detailCache = d; return d; })
    .catch(function() { return {}; });
  return _detailProm;
}

function _wireDetailClose() {
  var btn = document.getElementById('tl-detail-close');
  if (!btn) return;
  btn.addEventListener('click', function() {
    _activeId = null;
    document.querySelectorAll('.tl2-event-node--active').forEach(function(n) {
      n.classList.remove('tl2-event-node--active');
    });
    var detail = document.getElementById('tl-detail');
    if (detail) detail.innerHTML = '<p class="tl2-placeholder">← Select an event</p>';
  });
}

/* ── Detail panel HTML builders ──────────────────────────────────────────── */

function _buildDetailShell(ev, era, bodyHtml) {
  return (
    '<div class="tl-detail-inner">' +
      '<button id="tl-detail-close" class="tl-detail-close" aria-label="Close">✕</button>' +
      '<div class="tl-detail-header" style="border-left-color:' + era.color + '">' +
        '<div class="tl-detail-header-meta">' +
          '<span class="tl-detail-era-dot" style="background:' + era.color + '"></span>' +
          '<span class="tl-detail-era-name">' + escHtml(era.label) + '</span>' +
          '<span class="tl-detail-year">' + escHtml(ev.yearDisplay) + '</span>' +
        '</div>' +
        '<h2 class="tl-detail-title">' + escHtml(ev.label) + '</h2>' +
      '</div>' +
      '<div class="tl-detail-body">' + bodyHtml + '</div>' +
    '</div>'
  );
}

function _buildDetailBody(ev, detail) {
  var body = '';

  var overview = (detail && detail.overview) || ev.desc || '';
  if (overview) {
    body += '<p class="tl-detail-overview">' + escHtml(overview) + '</p>';
  }

  if (detail && detail.key_people && detail.key_people.length) {
    body += '<section class="tl-detail-section">';
    body += '<h4 class="tl-detail-section-title">Key People</h4>';
    body += '<ul class="tl-detail-people">';
    detail.key_people.forEach(function(p) {
      body += '<li class="tl-detail-person">' +
        '<span class="tl-detail-person-name">' + escHtml(p.name) + '</span>' +
        ' — ' + escHtml(p.role) + '</li>';
    });
    body += '</ul></section>';
  }

  if (detail && detail.key_verses && detail.key_verses.length) {
    body += '<section class="tl-detail-section">';
    body += '<h4 class="tl-detail-section-title">Key Verses</h4>';
    body += '<div class="tl-detail-verses">';
    detail.key_verses.forEach(function(v) {
      // data-ref wired after injection so hover tooltip + modal both work
      body += '<div class="tl-detail-verse">' +
        '<a class="tl-detail-verse-ref ref" data-ref="' + escHtml(v.ref) + '">' +
          escHtml(v.ref) +
        '</a>' +
        '<span class="tl-detail-verse-note">' + escHtml(v.note) + '</span>' +
        '</div>';
    });
    body += '</div></section>';
  }

  if (detail && detail.context) {
    body += '<section class="tl-detail-section">';
    body += '<h4 class="tl-detail-section-title">Historical Context</h4>';
    body += '<p class="tl-detail-text">' + escHtml(detail.context) + '</p>';
    body += '</section>';
  }

  if (detail && detail.extrabiblical) {
    body += '<section class="tl-detail-section">';
    body += '<h4 class="tl-detail-section-title">Extrabiblical Evidence</h4>';
    body += '<p class="tl-detail-text tl-detail-text--evidence">' + escHtml(detail.extrabiblical) + '</p>';
    body += '</section>';
  }

  if (detail && detail.christ_connection) {
    body += '<section class="tl-detail-section tl-detail-section--christ">';
    body += '<h4 class="tl-detail-section-title tl-detail-section-title--christ">Connection to Christ</h4>';
    body += '<p class="tl-detail-text">' + escHtml(detail.christ_connection) + '</p>';
    body += '</section>';
  }

  if (ev.ref) {
    var href = READER_URL + '?ref=' + encodeURIComponent(ev.ref);
    body += '<div class="tl-detail-footer">' +
      '<a class="tl-detail-ref-link" href="' + href + '" target="_blank" rel="noopener">' +
        'Open ' + escHtml(ev.ref) + ' in Reader →' +
      '</a></div>';
  }

  return body;
}
