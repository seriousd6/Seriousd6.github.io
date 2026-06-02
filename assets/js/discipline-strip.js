/* discipline-strip.js — Compact daily status strip for discipline pages.
 *
 * Renders a single row of coloured dots showing today's discipline completion
 * at the top of any discipline page. Each dot links to its respective page so
 * the user can jump between disciplines without going back to the home page.
 *
 * Usage: call initDisciplineStrip() from a <script type="module"> on any
 * discipline page. The strip injects itself before <main>'s first child.
 */
'use strict';

import { getToday, onUpdate } from './tracker.js';

var ITEMS = [
  { key: 'reading',    label: 'Reading',    color: '#5c3d1e', href: '../plans/' },
  { key: 'devotional', label: 'Devotional', color: '#e67e22', href: '../devotionals/' },
  { key: 'memory',     label: 'Memory',     color: '#2980b9', href: '../memorize/' },
  { key: 'prayer',     label: 'Prayer',     color: '#8e44ad', href: '../journal/' },
  { key: 'reflection', label: 'Reflection', color: '#16a085', href: '../journal/?tab=reflections' },
  { key: 'worship',    label: 'Worship',    color: '#4caf50', href: '../worship/' },
];

var _el = null;

function _render() {
  if (!_el) return;
  var status = getToday();
  _el.innerHTML = ITEMS.map(function (item) {
    var done   = !!status[item.key];
    var color  = done ? item.color : 'var(--color-border)';
    var opacity = done ? '1' : '0.45';
    return '<a class="disc-strip__item' + (done ? ' disc-strip__item--done' : '') + '" href="' + item.href + '" title="' + item.label + (done ? ' ✓' : '') + '">' +
      '<span class="disc-strip__dot" style="background:' + color + ';opacity:' + opacity + '"></span>' +
      '<span class="disc-strip__label">' + item.label + '</span>' +
    '</a>';
  }).join('');
}

export function initDisciplineStrip() {
  // Inject the strip element and its stylesheet once
  if (!document.getElementById('disc-strip-style')) {
    var style = document.createElement('style');
    style.id = 'disc-strip-style';
    style.textContent = [
      '.disc-strip {',
      '  display: flex; gap: 0; flex-wrap: wrap;',
      '  background: var(--color-surface); border-bottom: 1px solid var(--color-border);',
      '  padding: 0.45rem 1rem; margin-bottom: 0; font-family: var(--font-ui);',
      '}',
      '.disc-strip__item {',
      '  display: flex; align-items: center; gap: 0.32rem;',
      '  padding: 0.2rem 0.65rem; text-decoration: none;',
      '  font-size: 0.72rem; color: var(--color-muted);',
      '  border-right: 1px solid var(--color-border);',
      '  transition: color 0.12s;',
      '}',
      '.disc-strip__item:last-child { border-right: none; }',
      '.disc-strip__item:hover { color: var(--color-text); }',
      '.disc-strip__item--done { color: var(--color-text); font-weight: 500; }',
      '.disc-strip__dot {',
      '  width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0;',
      '}',
      '@media (max-width: 540px) { .disc-strip__label { display: none; } .disc-strip__item { padding: 0.2rem 0.5rem; } }',
    ].join('\n');
    document.head.appendChild(style);
  }

  _el = document.createElement('div');
  _el.className = 'disc-strip';
  _el.setAttribute('aria-label', "Today's discipline status");

  // Insert at the very top of <main>
  var main = document.querySelector('main');
  if (main) main.insertBefore(_el, main.firstChild);

  _render();
  onUpdate(_render);

  // Re-render on localStorage changes from other tabs
  window.addEventListener('storage', function (e) {
    var keys = ['bsw_tracker','bsw_plans','bsw_journal','bsw_reflections','bsw_worship'];
    if (keys.indexOf(e.key) !== -1) _render();
  });
}
