/* timeline.js — Timeline pages (3-column: eras → events → detail)
 * Shared by Biblical Timeline and Church History Timeline.
 * Each page gets its own isolated controller via _makeController(cfg). */
'use strict';

import { _resolve, escHtml, READER_URL, MAPS_URL, ERA_MAP_LINKS, MAP_LABELS } from './core.js';
import { wireRefLinks, autoTagRefs } from './wire.js';
import { autoTagTermsWhenReady } from './terms.js';

var _BIBLICAL_EVENTS_URL = _resolve('../../data/timeline/events.json');
var _BIBLICAL_DETAIL_URL = _resolve('../../data/timeline/detail.json');
var _CHURCH_EVENTS_URL   = _resolve('../../data/timeline/church-events.json');
var _CHURCH_DETAIL_URL   = _resolve('../../data/timeline/church-detail.json');

/* ── TLU-E: Church history event → library document map ─────────────────── */
var CHURCH_LIB_LINKS = {
  'anselm':        [{ docId: 'anselm-cur-deus-homo', label: 'Cur Deus Homo' },
                    { docId: 'anselm-proslogion',     label: 'Proslogion' }],
  'augustine':     [{ docId: 'augustine-confessions',          label: 'Confessions' },
                    { docId: 'augustine-city-of-god',          label: 'City of God' },
                    { docId: 'augustine-on-trinity',           label: 'On the Trinity' },
                    { docId: 'augustine-enchiridion',          label: 'Enchiridion' }],
  'aquinas':       [{ docId: 'aquinas-summa-part-i', label: 'Summa Theologica I' }],
  'luther-95-theses': [{ docId: 'luther-95-theses',        label: '95 Theses' },
                       { docId: 'luther-bondage-of-will',   label: 'Bondage of the Will' }],
  'calvin-geneva': [{ docId: 'calvin-institutes-vol1', label: 'Institutes (Vol. 1)' }],
  'westminster':   [{ docId: 'westminster-confession',         label: 'Westminster Confession' },
                    { docId: 'westminster-shorter-catechism',  label: 'Shorter Catechism' }],
  'nicaea-i':      [{ docId: 'nicaea-i', label: 'Council of Nicaea (AD 325)' }],
  'chalcedon':     [{ docId: 'chalcedon-451', label: 'Definition of Chalcedon' }],
  'benedictine-rule': [{ docId: 'benedict-rule', label: 'Rule of St. Benedict' }],
};

/* ── Controller factory ────────────────────────────────────────────────────
 * Creates an isolated controller with its own state, bound to the DOM
 * elements present on the page.  Both timeline pages share the same
 * element IDs (tl2-eras-spine, tl2-events-spine, tl-detail) because they
 * are on separate pages — no collision. */

function _makeController(cfg) {
  var eventsUrl  = cfg.eventsUrl;
  var detailUrl  = cfg.detailUrl;
  var isChurch   = !!cfg.isChurch;
  var storageKey = cfg.storageKey || 'bsw_tl'; // TLU-B: namespace per page

  // Instance state
  var _data        = null;
  var _detailCache = null;
  var _detailProm  = null;
  var _activeEra   = null;
  var _activeId    = null;
  var _activeEraObj  = null; // keep era object for prev/next nav

  /* ── Proportional positioning ─────────────────────────────────────────── */
  // INTENT: Maps each event's yearNum to a CSS top% using a linear scale over
  //   the finite range of yearNums (4%–92% band). Events with yearNum >= 9000
  //   or null (eschatological / undated placeholders) are pinned to 95% rather
  //   than computed — including 9999 in the scale range would collapse all finite
  //   events into < 1% of the spine height.
  // CHANGE? If you add an era with yearNum outside the current range, re-check
  //   the min/max computation; they are derived dynamically from finite values,
  //   but extreme outliers can still distort the visible scale. Consider pinning
  //   any yearNum > 2200 CE (post-Revelation) the same way 9000+ is pinned.
  // VERIFY: The "Life of Jesus" cluster should appear near the bottom ~15% of the
  //   biblical spine, visually separate from the OT events above.
  function _proportionalPositions(yearNums, minGap) {
    if (yearNums.length === 0) return [];
    if (yearNums.length === 1) {
      return [yearNums[0] == null || yearNums[0] >= 9000 ? 95 : 50];
    }

    // Separate finite positions from pinned end items
    var finite = yearNums.filter(function(y) { return y != null && y < 9000; });
    if (!finite.length) return yearNums.map(function() { return 95; });

    var minY = Math.min.apply(null, finite);
    var maxY = Math.max.apply(null, finite);
    var span = maxY - minY || 1;

    return yearNums.map(function(y) {
      if (y == null || y >= 9000) return 95;
      var pct = (y - minY) / span * 100;
      return 4 + pct * 0.88; // leave room at top and bottom
    });
  }

  /* Enforce minimum gap between consecutive positioned items (in-place). */
  function _enforceMinGap(pcts, minGap) {
    for (var i = 1; i < pcts.length; i++) {
      if (pcts[i] - pcts[i - 1] < minGap) pcts[i] = pcts[i - 1] + minGap;
    }
    // Scale back if we've pushed past 95
    var hi = pcts[pcts.length - 1];
    if (hi > 95) {
      var scale = 95 / hi;
      for (var j = 0; j < pcts.length; j++) pcts[j] = Math.max(4, pcts[j] * scale);
    }
    return pcts;
  }

  /* ── Era spine ────────────────────────────────────────────────────────── */
  function _renderEraSpine() {
    var wrap = document.getElementById('tl2-eras-spine');
    if (!wrap || !_data) return;

    var eraMin = {};
    _data.events.forEach(function(ev) {
      if (eraMin[ev.era] === undefined || ev.yearNum < eraMin[ev.era])
        eraMin[ev.era] = ev.yearNum;
    });

    var eras = _data.eras.filter(function(e) { return eraMin[e.id] !== undefined; });
    eras.sort(function(a, b) { return eraMin[a.id] - eraMin[b.id]; });

    // TLU-H: separate pinned (consummation) from proportionally-positioned eras
    var yearNums  = eras.map(function(e) { return eraMin[e.id]; });
    var raw       = _proportionalPositions(yearNums, 6);
    var positions = _enforceMinGap(raw.slice(), 6);

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

    // TLU-H: consummation era has minYear 9999 — show meaningful label
    var yr = document.createElement('span');
    yr.className   = 'tl2-node-year';
    if (minYear == null || minYear >= 9000) {
      yr.textContent = '—';
    } else {
      yr.textContent = minYear < 0
        ? 'c. ' + Math.abs(minYear) + ' BC'
        : 'AD ' + minYear;
    }

    // TLU-G: event count badge
    var count = _data
      ? _data.events.filter(function(ev) { return ev.era === era.id; }).length
      : 0;
    var countBadge = document.createElement('span');
    countBadge.className   = 'tl2-node-count';
    countBadge.textContent = count;

    text.appendChild(lbl);
    text.appendChild(yr);
    text.appendChild(countBadge);
    btn.appendChild(dot);
    btn.appendChild(text);

    btn.addEventListener('click', function() { _selectEra(era); });
    return btn;
  }

  /* ── Event spine ──────────────────────────────────────────────────────── */
  function _renderEventSpine(era) {
    var wrap  = document.getElementById('tl2-events-spine');
    var label = document.getElementById('tl2-events-label');
    if (!wrap) return;

    if (label) {
      label.innerHTML =
        '<span class="tl2-col-era-dot" style="background:' + era.color + '"></span>' +
        escHtml(era.label);
    }

    var events = _data.events.filter(function(ev) { return ev.era === era.id; });
    events.sort(function(a, b) { return a.yearNum - b.yearNum; });

    // TLU-H: handle null/9999 yearNum in event spine positioning
    var yearNums  = events.map(function(ev) { return ev.yearNum; });
    var raw       = _proportionalPositions(yearNums, 7);
    var positions = _enforceMinGap(raw.slice(), 7);

    wrap.innerHTML = '';
    events.forEach(function(ev, i) {
      wrap.appendChild(_makeEventNode(ev, era, positions[i]));
    });
  }

  function _makeEventNode(ev, era, pct) {
    var btn = document.createElement('button');
    btn.className       = 'tl2-event-node';
    btn.style.top       = pct + '%';
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

  /* ── TLU-G: extrabiblical indicator — post-detail-load pass ─────────── */
  function _markExtrabiblical() {
    if (!_detailCache || isChurch) return;
    document.querySelectorAll('.tl2-event-node').forEach(function(btn) {
      var evId  = btn.dataset.eventId;
      var d     = _detailCache[evId];
      if (d && d.extrabiblical && !btn.querySelector('.tl2-ev-arch')) {
        var arch = document.createElement('span');
        arch.className = 'tl2-ev-arch';
        arch.title     = 'Extrabiblical evidence';
        arch.textContent = '⛏';
        var textEl = btn.querySelector('.tl2-node-text');
        if (textEl) textEl.appendChild(arch);
      }
    });
  }

  /* ── Selection handlers ───────────────────────────────────────────────── */
  function _selectEra(era) {
    _activeEra    = era.id;
    _activeEraObj = era;
    _activeId     = null;

    document.querySelectorAll('.tl2-era-node').forEach(function(n) {
      n.classList.toggle('tl2-era-node--active', n.dataset.eraId === era.id);
    });

    var detail = document.getElementById('tl-detail');
    if (detail) detail.innerHTML = '<p class="tl2-placeholder">← Select an event</p>';

    _renderEventSpine(era);

    // TLU-A: push URL state
    history.replaceState(null, '', '?era=' + encodeURIComponent(era.id));
    // TLU-B: persist session
    try { sessionStorage.setItem(storageKey + '_era', era.id); } catch (e) {}
    try { sessionStorage.removeItem(storageKey + '_event'); } catch (e) {}
  }

  function _clickEvent(ev, era) {
    if (_activeId === ev.id) {
      _activeId = null;
      document.querySelectorAll('.tl2-event-node').forEach(function(n) {
        n.classList.remove('tl2-event-node--active');
      });
      var d = document.getElementById('tl-detail');
      if (d) d.innerHTML = '<p class="tl2-placeholder">← Select an event</p>';
      // TLU-A: restore era-only URL
      history.replaceState(null, '', '?era=' + encodeURIComponent(_activeEra || era.id));
      try { sessionStorage.removeItem(storageKey + '_event'); } catch (e) {}
      return;
    }

    _activeId     = ev.id;
    _activeEraObj = era;

    document.querySelectorAll('.tl2-event-node').forEach(function(n) {
      n.classList.toggle('tl2-event-node--active', n.dataset.eventId === ev.id);
    });

    // TLU-C: compute index within era's events for prev/next nav
    var eraEvents = _data
      ? _data.events.filter(function(e) { return e.era === era.id; })
          .sort(function(a, b) { return a.yearNum - b.yearNum; })
      : [];
    var idx = eraEvents.findIndex(function(e) { return e.id === ev.id; });

    var panel = document.getElementById('tl-detail');
    if (panel) {
      panel.innerHTML = _buildDetailShell(
        ev, era,
        '<div class="tl-detail-loading">Loading…</div>',
        { idx: idx, total: eraEvents.length, eraEvents: eraEvents }
      );
      _wireDetailNav(panel, era, eraEvents);
      _wireDetailClose(era);
    }

    _loadDetail().then(function(details) {
      if (_activeId !== ev.id) return;
      var detail = (details && details[ev.id]) || null;
      if (panel) {
        panel.innerHTML = _buildDetailShell(
          ev, era,
          _buildDetailBody(ev, detail),
          { idx: idx, total: eraEvents.length, eraEvents: eraEvents }
        );
        _wireDetailNav(panel, era, eraEvents);
        _wireDetailClose(era);
        wireRefLinks(panel);
        autoTagRefs();
        var detailBody = panel.querySelector('.tl-detail-body');
        if (detailBody) autoTagTermsWhenReady(detailBody);
        var detailInner = panel.querySelector('.tl-detail-inner');
        if (detailInner && window.BibleUI && window.BibleUI.autoTagPlacesIn) {
          window.BibleUI.autoTagPlacesIn(detailInner);
        }
        // TLU-G: mark extrabiblical after detail loaded
        _markExtrabiblical();
      }
    });

    // TLU-A: push URL state
    history.replaceState(null, '',
      '?era=' + encodeURIComponent(era.id) +
      '&event=' + encodeURIComponent(ev.id)
    );
    // TLU-B: persist session
    try { sessionStorage.setItem(storageKey + '_event', ev.id); } catch (e) {}
  }

  /* ── Detail: lazy-load once ───────────────────────────────────────────── */
  // INTENT: _detailCache holds the full detail JSON for the current timeline
  //   (biblical or church). The first call fetches the appropriate
  //   data/timeline/*-detail.json and caches the whole object; subsequent event
  //   clicks resolve from the in-memory cache synchronously. _detailProm prevents
  //   duplicate concurrent fetches if two clicks arrive before the first resolves.
  // CHANGE? If you add a new detail field to the JSON, update _buildDetailBody
  //   to render it — _detailCache is never invalidated, so adding a field to JSON
  //   without updating the renderer has no visible effect until a hard reload.
  // VERIFY: Click two events in the same era back-to-back; the Network tab should
  //   show only one fetch — the second detail panel loads from the cache.
  function _loadDetail() {
    if (_detailCache) return Promise.resolve(_detailCache);
    if (_detailProm)  return _detailProm;
    _detailProm = fetch(detailUrl)
      .then(function(r) { return r.ok ? r.json() : {}; })
      .then(function(d) { _detailCache = d; return d; })
      .catch(function() { return {}; });
    return _detailProm;
  }

  function _wireDetailClose(era) {
    var btn = document.getElementById('tl-detail-close');
    if (!btn) return;
    btn.addEventListener('click', function() {
      _activeId = null;
      document.querySelectorAll('.tl2-event-node--active').forEach(function(n) {
        n.classList.remove('tl2-event-node--active');
      });
      var detail = document.getElementById('tl-detail');
      if (detail) detail.innerHTML = '<p class="tl2-placeholder">← Select an event</p>';
      // TLU-A: restore era-only URL on close
      if (_activeEra) {
        history.replaceState(null, '', '?era=' + encodeURIComponent(_activeEra));
      }
      try { sessionStorage.removeItem(storageKey + '_event'); } catch (e) {}
    });
  }

  /* TLU-C: wire prev/next buttons after shell is in DOM */
  function _wireDetailNav(panel, era, eraEvents) {
    var prevBtn = panel.querySelector('.tl-detail-nav-btn--prev');
    var nextBtn = panel.querySelector('.tl-detail-nav-btn--next');
    if (prevBtn) {
      prevBtn.addEventListener('click', function() {
        var cur  = eraEvents.findIndex(function(e) { return e.id === _activeId; });
        if (cur > 0) _clickEvent(eraEvents[cur - 1], era);
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', function() {
        var cur  = eraEvents.findIndex(function(e) { return e.id === _activeId; });
        if (cur < eraEvents.length - 1) _clickEvent(eraEvents[cur + 1], era);
      });
    }
  }

  /* ── Detail panel HTML builders ───────────────────────────────────────── */
  function _buildDetailShell(ev, era, bodyHtml, nav) {
    // TLU-J: mobile breadcrumb
    var breadcrumb =
      '<div class="tl-detail-breadcrumb">' +
        '<span style="color:' + era.color + '">' + escHtml(era.label) + '</span>' +
        ' › ' + escHtml(ev.label) +
      '</div>';

    // TLU-C: prev/next nav
    var navHtml = '';
    if (nav) {
      var prevDis = nav.idx <= 0 ? ' tl-detail-nav-btn--disabled' : '';
      var nextDis = nav.idx >= nav.total - 1 ? ' tl-detail-nav-btn--disabled' : '';
      navHtml =
        '<div class="tl-detail-nav">' +
          '<button class="tl-detail-nav-btn tl-detail-nav-btn--prev' + prevDis + '" type="button">← Prev</button>' +
          '<span class="tl-detail-nav-pos">' + (nav.idx + 1) + ' of ' + nav.total + '</span>' +
          '<button class="tl-detail-nav-btn tl-detail-nav-btn--next' + nextDis + '" type="button">Next →</button>' +
        '</div>';
    }

    return (
      '<div class="tl-detail-inner">' +
        breadcrumb +
        '<button id="tl-detail-close" class="tl-detail-close" aria-label="Close">✕</button>' +
        navHtml +
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
        body += '<div class="tl-detail-verse">' +
          '<a class="tl-detail-verse-ref ref" data-ref="' + escHtml(v.ref) + '">' +
            escHtml(v.ref) +
          '</a>' +
          '<span class="tl-detail-verse-note">' + escHtml(v.note) + '</span>' +
          '</div>';
      });
      body += '</div></section>';
    }

    if (detail && detail.key_texts && detail.key_texts.length) {
      body += '<section class="tl-detail-section">';
      body += '<h4 class="tl-detail-section-title">Key Texts</h4>';
      body += '<div class="tl-detail-verses">';
      detail.key_texts.forEach(function(v) {
        var isRef = v.ref && /^[A-Z1-3]/.test(v.ref);
        var refHtml = isRef
          ? '<a class="tl-detail-verse-ref ref" data-ref="' + escHtml(v.ref) + '">' + escHtml(v.ref) + '</a>'
          : '<span class="tl-detail-verse-ref tl-detail-verse-ref--doc">' + escHtml(v.ref) + '</span>';
        body += '<div class="tl-detail-verse">' +
          refHtml +
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

    if (detail && detail.significance) {
      body += '<section class="tl-detail-section">';
      body += '<h4 class="tl-detail-section-title">Theological Significance</h4>';
      body += '<p class="tl-detail-text">' + escHtml(detail.significance) + '</p>';
      body += '</section>';
    }

    if (detail && detail.christ_connection) {
      body += '<section class="tl-detail-section tl-detail-section--christ">';
      body += '<h4 class="tl-detail-section-title tl-detail-section-title--christ">Connection to Christ</h4>';
      body += '<p class="tl-detail-text">' + escHtml(detail.christ_connection) + '</p>';
      body += '</section>';
    }

    if (detail && detail.legacy) {
      body += '<section class="tl-detail-section tl-detail-section--legacy">';
      body += '<h4 class="tl-detail-section-title tl-detail-section-title--legacy">Legacy</h4>';
      body += '<p class="tl-detail-text">' + escHtml(detail.legacy) + '</p>';
      body += '</section>';
    }

    // TLU-E: library document links for church history events
    if (isChurch && CHURCH_LIB_LINKS[ev.id]) {
      var libLinks = CHURCH_LIB_LINKS[ev.id];
      var libRoot  = _resolve('../../library/');
      body += '<div class="tl-detail-lib-links">' +
        '<span class="tl-detail-maps-label">Read in Library</span>' +
        libLinks.map(function(l) {
          return '<a class="tl-detail-lib-chip" href="' + escHtml(libRoot + l.docId + '/') + '">' +
            '📖 ' + escHtml(l.label) +
          '</a>';
        }).join('') +
      '</div>';
    }

    if (ev.ref) {
      var href = READER_URL + '?ref=' + encodeURIComponent(ev.ref);
      // TLU-K: no target="_blank" for in-site navigation
      body += '<div class="tl-detail-footer">' +
        '<a class="tl-detail-ref-link" href="' + href + '">' +
          'Open ' + escHtml(ev.ref) + ' in Reader →' +
        '</a></div>';
    }

    // TLU-D: cross-timeline bridge — show at bottom of biblical NT/church era events
    if (!isChurch && _activeEra === 'church') {
      var chHref = _resolve('../church-history/');
      body += '<div class="tl-detail-crossover">' +
        '<span class="tl-detail-crossover__label">Continue the story</span>' +
        '<a class="tl-detail-crossover__link" href="' + chHref + '">' +
          'Church History Timeline — from Pentecost to today →' +
        '</a>' +
      '</div>';
    }

    // TLU-K: related maps — no target="_blank"
    var eraMapIds = (ERA_MAP_LINKS && _activeEra && ERA_MAP_LINKS[_activeEra]) || [];
    if (eraMapIds.length) {
      body += '<div class="tl-detail-maps">' +
        '<span class="tl-detail-maps-label">Related Maps</span>' +
        eraMapIds.map(function(id) {
          var label = (MAP_LABELS && MAP_LABELS[id]) || id;
          return '<a class="tl-detail-map-chip" href="' + escHtml(MAPS_URL + '#' + id) + '">' +
            '🗺 ' + escHtml(label) +
          '</a>';
        }).join('') +
      '</div>';
    }

    return body;
  }

  /* ── TLU-I: quick search across all eras ─────────────────────────────── */
  function _handleSearch(q) {
    var eraSpine   = document.getElementById('tl2-eras-spine');
    var eventsWrap = document.getElementById('tl2-events-spine');
    var evLabel    = document.getElementById('tl2-events-label');

    if (!q) {
      // Restore normal mode
      if (eraSpine) {
        eraSpine.querySelectorAll('.tl2-era-node').forEach(function(n) {
          n.classList.remove('tl2-era-node--dim');
        });
      }
      if (eventsWrap) {
        eventsWrap.innerHTML = '<p class="tl2-placeholder">← Select an era</p>';
      }
      if (evLabel) evLabel.innerHTML = 'Events';
      return;
    }

    var ql = q.toLowerCase();
    var matches = (_data ? _data.events : []).filter(function(ev) {
      return (ev.label || '').toLowerCase().indexOf(ql) !== -1 ||
             (ev.desc  || '').toLowerCase().indexOf(ql) !== -1;
    });

    // Dim era nodes that have no matching events
    var matchingEraIds = {};
    matches.forEach(function(ev) { matchingEraIds[ev.era] = true; });
    if (eraSpine) {
      eraSpine.querySelectorAll('.tl2-era-node').forEach(function(n) {
        n.classList.toggle('tl2-era-node--dim', !matchingEraIds[n.dataset.eraId]);
      });
    }

    // Render matching events in the events column
    if (eventsWrap) {
      if (!matches.length) {
        eventsWrap.innerHTML = '<p class="tl2-placeholder">No events match.</p>';
      } else {
        eventsWrap.innerHTML = '';
        var eraMap = {};
        if (_data) _data.eras.forEach(function(e) { eraMap[e.id] = e; });
        matches.forEach(function(ev) {
          var era = eraMap[ev.era] || { color: '#888', label: ev.era };
          // Use flat positioning for search results (not proportional)
          var node = _makeEventNode(ev, era, 0);
          node.style.position = 'relative';
          node.style.top      = '0';
          node.style.margin   = '0 0 .3rem 0';
          // Add era color dot hint
          var dot = document.createElement('span');
          dot.className = 'tl2-col-era-dot';
          dot.style.cssText = 'background:' + era.color + ';margin-right:.25rem';
          node.insertBefore(dot, node.firstChild);
          eventsWrap.appendChild(node);
        });
      }
    }
    if (evLabel) evLabel.innerHTML = 'Search Results';
  }

  /* ── Public init ──────────────────────────────────────────────────────── */
  return {
    init: function() {
      var spine = document.getElementById('tl2-eras-spine');
      if (!spine) return;

      // TLU-I: wire search input
      var searchInput = document.querySelector('.tl2-search');
      if (searchInput) {
        searchInput.addEventListener('input', function() {
          _handleSearch(searchInput.value.trim());
        });
      }

      fetch(eventsUrl)
        .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); })
        .then(function(data) {
          _data = data;
          _renderEraSpine();

          // TLU-A + TLU-B: restore selection from URL params or sessionStorage
          var params    = new URLSearchParams(location.search);
          var eraParam  = params.get('era');
          var evParam   = params.get('event');

          // Fall back to sessionStorage if no URL params (TLU-B)
          if (!eraParam) {
            try { eraParam = sessionStorage.getItem(storageKey + '_era') || ''; } catch (e) {}
          }
          if (!evParam) {
            try { evParam = sessionStorage.getItem(storageKey + '_event') || ''; } catch (e) {}
          }

          if (eraParam) {
            var matchEra = data.eras.find(function(e) { return e.id === eraParam; });
            if (matchEra) {
              _selectEra(matchEra);
              if (evParam) {
                var matchEv = data.events.find(function(e) { return e.id === evParam; });
                if (matchEv) _clickEvent(matchEv, matchEra);
              }
            }
          }
        })
        .catch(function(err) {
          console.error('[Timeline] load error:', err);
          spine.innerHTML = '<p style="padding:1rem;color:var(--color-muted)">Unable to load timeline data.</p>';
        });
    }
  };
}

/* ── Exported init functions ───────────────────────────────────────────── */

// INTENT: Bootstrap the biblical timeline on /timeline/ — fetches
//   data/timeline/events.json + detail.json via _makeController, then persists
//   the user's era/event selection in sessionStorage under keys bsw_tl_era and
//   bsw_tl_event so the selection survives a same-tab page reload.
// CHANGE? If the data files are renamed, update _BIBLICAL_EVENTS_URL /
//   _BIBLICAL_DETAIL_URL at the top of this file. If the storageKey prefix
//   changes, also update any bookmarks that embed ?era= / ?event= URL params
//   since _makeController reads these on init to restore state.
// VERIFY: Load /timeline/ → era list and event list render; click an event →
//   reload page → same era and event are re-selected from sessionStorage.
export function initTimelinePage() {
  _makeController({
    eventsUrl:  _BIBLICAL_EVENTS_URL,
    detailUrl:  _BIBLICAL_DETAIL_URL,
    isChurch:   false,
    storageKey: 'bsw_tl',
  }).init();
}

// INTENT: Bootstrap the church history timeline on /church-history/ — same
//   controller as initTimelinePage but loads church-events/detail JSONs and
//   uses bsw_chtl_era / bsw_chtl_event as the sessionStorage namespace so the
//   two timelines don't overwrite each other's saved selection.
// CHANGE? Rename _CHURCH_EVENTS_URL / _CHURCH_DETAIL_URL at the top of this
//   file if the data files move. isChurch:true gates church-specific rendering
//   branches inside _makeController — search "isChurch" to find them.
// VERIFY: Load /church-history/ → eras and events render; navigate to an event;
//   reload → selection restored. Open /timeline/ in a separate tab → its
//   selection is independent (different storageKey namespace).
export function initChurchTimelinePage() {
  _makeController({
    eventsUrl:  _CHURCH_EVENTS_URL,
    detailUrl:  _CHURCH_DETAIL_URL,
    isChurch:   true,
    storageKey: 'bsw_chtl',
  }).init();
}
