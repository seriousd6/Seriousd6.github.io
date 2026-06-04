/* lib-progress.js — Library reading history and tradition coverage (LR-C) */
'use strict';

import { _resolve, escHtml } from './core.js';

var LIB_INDEX_URL     = _resolve('../../data/library/index.json');
var _LIB_COMPLETE_KEY = 'bsw_lib_complete';

var _TRAD_DISPLAY = {
  patristic:      'Church Fathers',
  reformed:       'Reformed',
  lutheran:       'Lutheran',
  anglican:       'Anglican',
  baptist:        'Baptist',
  orthodox:       'Orthodox',
  'roman-catholic': 'Roman Catholic',
  methodist:      'Methodist',
  ecumenical:     'Ecumenical'
};

var _TRAD_ORDER = [
  'patristic', 'reformed', 'lutheran', 'anglican',
  'baptist', 'orthodox', 'roman-catholic', 'methodist', 'ecumenical'
];

var _TRAD_COLORS = {
  patristic:       '#8b6914',
  reformed:        '#2a5a8a',
  lutheran:        '#5a2a8a',
  anglican:        '#1a6b4a',
  baptist:         '#8a3a1a',
  orthodox:        '#c0792a',
  'roman-catholic': '#8a1a2a',
  methodist:       '#1a6b8a',
  ecumenical:      '#4a6a4a'
};

export function initLibProgressPage() {
  var root = document.getElementById('lp-root');
  if (!root) return;

  var log = {};
  try { log = JSON.parse(localStorage.getItem(_LIB_COMPLETE_KEY) || '{}'); } catch(e) {}

  fetch(LIB_INDEX_URL)
    .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function(index) { _render(root, log, index); })
    .catch(function() { _render(root, log, []); });
}

function _render(root, log, index) {
  var completedIds = Object.keys(log);
  var totalDocs    = completedIds.length;

  // Count totals per tradition from index
  var tradTotals = {};
  index.forEach(function(d) {
    var t = d.tradition || 'ecumenical';
    tradTotals[t] = (tradTotals[t] || 0) + 1;
  });

  // Count completions per tradition
  var tradDone = {};
  completedIds.forEach(function(id) {
    var t = log[id].tradition || 'ecumenical';
    tradDone[t] = (tradDone[t] || 0) + 1;
  });

  var tradsTouched = Object.keys(tradDone).length;

  // Encouragement line
  var encLine = '';
  if (!totalDocs) {
    encLine = 'No completed works yet. Finish reading a document and click "Mark as read" to begin.';
  } else {
    var gaps = _TRAD_ORDER.filter(function(t) { return !tradDone[t]; });
    if (gaps.length) {
      encLine = 'You\'ve read from ' + tradsTouched + ' of 9 traditions. Try a ' + (_TRAD_DISPLAY[gaps[0]] || gaps[0]) + ' work next.';
    } else {
      encLine = 'You\'ve read from all 9 traditions. Excellent breadth!';
    }
  }

  // Build tradition coverage bar
  var coverageHtml = '<div class="lp-coverage">';
  coverageHtml += '<h2 class="lp-section-title">Tradition Coverage</h2>';
  coverageHtml += '<div class="lp-coverage-bars">';
  _TRAD_ORDER.forEach(function(trad) {
    var done  = tradDone[trad] || 0;
    var total = tradTotals[trad] || 0;
    var pct   = total ? Math.round((done / total) * 100) : 0;
    var color = _TRAD_COLORS[trad] || '#888';
    var label = _TRAD_DISPLAY[trad] || trad;
    coverageHtml +=
      '<div class="lp-bar-row">' +
        '<span class="lp-bar-label">' + escHtml(label) + '</span>' +
        '<div class="lp-bar-track">' +
          '<div class="lp-bar-fill" style="width:' + pct + '%;background:' + escHtml(color) + '"></div>' +
        '</div>' +
        '<span class="lp-bar-count">' + done + ' / ' + total + '</span>' +
      '</div>';
  });
  coverageHtml += '</div></div>';

  // Stats row
  var statsHtml =
    '<div class="lp-stats">' +
      '<div class="lp-stat"><span class="lp-stat-num">' + totalDocs + '</span><span class="lp-stat-label">Works completed</span></div>' +
      '<div class="lp-stat"><span class="lp-stat-num">' + tradsTouched + '</span><span class="lp-stat-label">Traditions touched</span></div>' +
    '</div>';

  // Encouragement
  var encHtml = '<p class="lp-encourage">' + escHtml(encLine) + '</p>';

  // Completion log (newest first)
  var logHtml = '<div class="lp-log">';
  logHtml += '<h2 class="lp-section-title">Completed Works</h2>';

  if (!totalDocs) {
    logHtml += '<p class="lp-log-empty">No completed works yet.</p>';
  } else {
    var sorted = completedIds.slice().sort(function(a, b) {
      return (log[b].completedDate || '') < (log[a].completedDate || '') ? -1 : 1;
    });
    sorted.forEach(function(id) {
      var entry = log[id];
      var trad  = entry.tradition || 'ecumenical';
      var color = _TRAD_COLORS[trad] || '#888';
      var tradLabel = _TRAD_DISPLAY[trad] || trad;
      var readHref  = _resolve('../../library/read/') + '?doc=' + encodeURIComponent(id);
      logHtml +=
        '<div class="lp-log-item">' +
          '<div class="lp-log-main">' +
            '<a class="lp-log-title" href="' + escHtml(readHref) + '">' + escHtml(entry.title || id) + '</a>' +
            (entry.author ? '<span class="lp-log-author">' + escHtml(entry.author) + '</span>' : '') +
          '</div>' +
          '<div class="lp-log-meta">' +
            '<span class="lp-trad-chip" style="background:' + escHtml(color) + '">' + escHtml(tradLabel) + '</span>' +
            (entry.completedDate ? '<span class="lp-log-date">' + escHtml(entry.completedDate) + '</span>' : '') +
          '</div>' +
        '</div>';
    });
  }
  logHtml += '</div>';

  root.innerHTML = statsHtml + encHtml + coverageHtml + logHtml;
}
