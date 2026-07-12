/* reader-rail.js — per-chapter apparatus rail (Daylight increment 3).
 *
 * The Daylight direction keeps study markup always-on but pushes "everything
 * countable" toward an aggregate view. This module renders a small chip rail
 * at the head of every rendered chapter summarizing what the apparatus found —
 * cross-reference connections, synoptic parallels, tagged places, and saved
 * notes — with each chip wired to the existing feature control, so the rail is
 * an index onto the chapter, not a new feature surface.
 *
 * Deliberately zero-surgery: reader.js render internals are untouched. A
 * debounced MutationObserver on #reader-results (the same pattern the
 * chapter-completion tracker uses) rebuilds the rail after each render by
 * counting the markers already in the DOM:
 *   .reader-echo-marker  — connection chips injected by parallels.js
 *   .map-place           — place links tagged by places.js (idle/async, so a
 *                          late pass updates the count when tagging lands)
 *   notes                — read from the bsw_notes store for the current book
 *                          + chapter via window._readerNavState
 * Chip clicks .click() the existing toggle buttons (echoes, notes panel);
 * the places chip scrolls to the first tagged place.
 */
'use strict';

import { getNotesForChapter } from './storage.js';

var _observer = null;
var _debounce = null;

function _navState() {
  return (typeof window !== 'undefined' && window._readerNavState) || null;
}

function _notesCountFor(nav) {
  if (!nav || !nav.bookId || !nav.ch) return 0;
  try { return getNotesForChapter(nav.bookId, nav.ch).length; } catch (e) { return 0; }
}

function _chip(label, count, title, onClick) {
  var b = document.createElement('button');
  b.className = 'reader-rail__chip';
  b.type = 'button';
  b.title = title;
  b.innerHTML = '<b>' + count + '</b>' + label;
  b.addEventListener('click', onClick);
  return b;
}

function _clickIfPresent(id) {
  var el = document.getElementById(id);
  if (el) el.click();
}

function _buildRail(results) {
  var old = results.querySelector('.reader-rail');
  if (old) old.remove();

  var echoes = results.querySelectorAll('.reader-echo-marker').length;
  var places = results.querySelectorAll('.map-place').length;
  var notes  = _notesCountFor(_navState());

  // Tool chips render regardless; count chips only when nonzero.

  var rail = document.createElement('div');
  rail.className = 'reader-rail';
  rail.setAttribute('aria-label', 'Chapter apparatus');

  if (echoes) rail.appendChild(_chip('connections', echoes,
    'Verses with cross-reference connections — jump to the first',
    function () {
      var first = results.querySelector('.reader-echo-marker');
      if (first) { first.scrollIntoView({ block: 'center', behavior: 'smooth' }); }
    }));
  if (places) rail.appendChild(_chip('places', places,
    'Tagged places in this chapter — jump to the first',
    function () {
      var first = results.querySelector('.map-place');
      if (first) { first.scrollIntoView({ block: 'center', behavior: 'smooth' }); first.focus && first.focus(); }
    }));
  if (notes) rail.appendChild(_chip('notes', notes,
    'Your notes on this chapter — open the notes panel',
    function () { _clickIfPresent('reader-notes-panel-btn'); }));

  // Feature chips (Heights H2): the depth that used to hide inside the Study
  // Tools popover advertises itself at the chapter head. Each chip mirrors and
  // drives its existing toggle button, so the popover controls stay in sync.
  [
    { id: 'reader-comm-toggle',      label: 'commentary',  title: 'Toggle inline commentary (Matthew Henry, Barnes, JFB)' },
    { id: 'reader-interlinear-btn',  label: 'interlinear', title: 'Toggle the Greek/Hebrew interlinear view' },
    { id: 'reader-parallels-btn',    label: 'parallels',   title: 'Toggle synoptic parallel passages' }
  ].forEach(function (f) {
    var target = document.getElementById(f.id);
    if (!target) return;
    var on = target.getAttribute('aria-pressed') === 'true';
    var chip = document.createElement('button');
    chip.className = 'reader-rail__chip reader-rail__chip--tool' + (on ? ' reader-rail__chip--on' : '');
    chip.type = 'button';
    chip.title = f.title;
    chip.setAttribute('aria-pressed', on ? 'true' : 'false');
    chip.textContent = f.label;
    chip.addEventListener('click', function () {
      target.click();
      var nowOn = target.getAttribute('aria-pressed') === 'true';
      chip.classList.toggle('reader-rail__chip--on', nowOn);
      chip.setAttribute('aria-pressed', nowOn ? 'true' : 'false');
    });
    rail.appendChild(chip);
  });

  // Ahead of the chapter heading if we can find it, else prepend.
  var heading = results.querySelector('.reader-section-heading, h2');
  if (heading && heading.parentNode === results) {
    results.insertBefore(rail, heading.nextSibling);
  } else {
    results.insertBefore(rail, results.firstChild);
  }
}

export function initReaderRail() {
  var results = document.getElementById('reader-results');
  if (!results || _observer) return;

  var observe = function () { _observer.observe(results, { childList: true, subtree: true }); };
  _observer = new MutationObserver(function () {
    clearTimeout(_debounce);
    _debounce = setTimeout(function () {
      // Disconnect while we mutate so our own rail insert never re-triggers.
      _observer.disconnect();
      _buildRail(results);
      observe();
    }, 350);
  });
  observe();
}
