/* tooltip.js — Verse hover tooltip.
 *
 * Shows a small floating panel with verse text when the user hovers or focuses
 * a .ref link. The panel is shared (one element in the DOM); position is
 * recalculated each time it's shown.
 *
 * Show/hide are both intentionally delayed:
 *   show: 300 ms — prevents flickering when the mouse briefly passes over a link.
 *   hide: 200 ms — gives the user time to move the mouse onto the tooltip itself
 *                  (e.g. to select and copy the verse text).
 *
 * wire.js calls scheduleShow/scheduleHide; the indirect registration via
 * registerScheduleShow() in core.js avoids a circular import between wire ↔ tooltip.
 */
'use strict';

import { getVersion, resolveVerses, registerScheduleShow } from './core.js';

// Shared tooltip DOM element; built once by buildTooltipDOM().
var _tooltipEl = null;
// Pending show/hide timer handles — cancelled when the opposing action fires.
var _showTimer = null;
var _hideTimer = null;

// buildTooltipDOM: creates #bsw-tooltip and appends it to <body>.
// Called once by app.js after DOM is ready. Idempotent — safe to call multiple times.
export function buildTooltipDOM() {
  if (document.getElementById('bsw-tooltip')) {
    _tooltipEl = document.getElementById('bsw-tooltip');
    return;
  }
  var el = document.createElement('div');
  el.id        = 'bsw-tooltip';
  el.className = 'bsw-tooltip';
  el.setAttribute('role', 'tooltip');
  el.setAttribute('aria-hidden', 'true');
  el.innerHTML =
    '<div class="bsw-tooltip__ref"></div>' +
    '<div class="bsw-tooltip__text"></div>';
  document.body.appendChild(el);
  _tooltipEl = el;

  // Keep the tooltip visible while the mouse is over it so the user can read/copy.
  el.addEventListener('mouseenter', function () { cancelHide(); });
  el.addEventListener('mouseleave', function () { scheduleHide(); });
}

// scheduleShow: queues a tooltip display after 300 ms.
// Cancels any pending hide timer so moving from link to tooltip keeps it open.
export function scheduleShow(anchorEl, parsed) {
  cancelHide();
  cancelShow();
  _showTimer = setTimeout(function () { showTooltip(anchorEl, parsed); }, 300);
}

// cancelShow: prevents a pending tooltip from appearing (e.g. mouse moved away quickly).
export function cancelShow() {
  if (_showTimer) { clearTimeout(_showTimer); _showTimer = null; }
}

// scheduleHide: queues tooltip dismissal after 200 ms.
export function scheduleHide() {
  cancelShow();
  _hideTimer = setTimeout(function () { hideTooltip(); }, 200);
}

export function cancelHide() {
  if (_hideTimer) { clearTimeout(_hideTimer); _hideTimer = null; }
}

// showTooltip: makes the tooltip visible, shows "Loading…" immediately,
// then replaces that with real verse text once resolveVerses() resolves.
// Positions the tooltip below the anchor (flips above if too close to viewport bottom).
export function showTooltip(anchorEl, parsed) {
  if (!_tooltipEl) return;
  var version = getVersion();

  _tooltipEl.querySelector('.bsw-tooltip__ref').textContent =
    parsed.display + ' · ' + version;
  _tooltipEl.querySelector('.bsw-tooltip__text').textContent = 'Loading…';
  _tooltipEl.classList.add('bsw-tooltip--visible');
  _tooltipEl.setAttribute('aria-hidden', 'false');
  // Add a modifier class for whole-chapter refs so CSS can apply different max-width.
  _tooltipEl.classList.toggle('bsw-tooltip--chapter', !!parsed.wholeChapter);
  positionTooltip(anchorEl);

  resolveVerses(parsed, version)
    .then(function (verses) {
      // Abort if the tooltip was hidden before the fetch completed.
      if (!_tooltipEl.classList.contains('bsw-tooltip--visible')) return;
      if (!verses || !verses.length) {
        _tooltipEl.querySelector('.bsw-tooltip__text').textContent = 'Verse not found.';
        return;
      }
      var preview;
      if (parsed.wholeChapter && parsed.endCh !== parsed.ch) {
        // Multi-chapter range: show the first verse of each chapter as a preview.
        var parts = [];
        for (var c = parsed.ch; c <= parsed.endCh; c++) {
          var cv = verses.filter(function (vr) { return vr.chapter === c; })[0];
          if (cv) parts.push('Ch.' + c + ': ' + cv.text);
        }
        preview = parts.join('  ');
        if (preview.length > 240) preview = preview.slice(0, 237) + '…';
      } else if (parsed.wholeChapter) {
        // Single whole chapter: show first two verses.
        preview = verses.slice(0, 2).map(function (vr) {
          return vr.verse + '. ' + vr.text;
        }).join('  ');
        if (preview.length > 220) preview = preview.slice(0, 217) + '…';
      } else {
        // Single verse or verse range: show full text, truncated at 120 chars.
        preview = verses[0].text;
        if (preview.length > 120) preview = preview.slice(0, 117) + '…';
      }
      _tooltipEl.querySelector('.bsw-tooltip__text').textContent = preview;
      // Re-position after content change in case height shifted.
      positionTooltip(anchorEl);
    })
    .catch(function () {
      if (_tooltipEl.classList.contains('bsw-tooltip--visible')) {
        _tooltipEl.querySelector('.bsw-tooltip__text').textContent = 'Click to view this passage';
      }
    });
}

// hideTooltip: immediately dismisses the tooltip and marks it aria-hidden.
export function hideTooltip() {
  if (!_tooltipEl) return;
  _tooltipEl.classList.remove('bsw-tooltip--visible');
  _tooltipEl.setAttribute('aria-hidden', 'true');
}

// positionTooltip: places the tooltip below the anchor element.
// Flips above if the bottom edge would overflow the viewport.
// Clamps horizontally so the tooltip stays within the viewport.
export function positionTooltip(anchorEl) {
  if (!_tooltipEl) return;
  var rect = anchorEl.getBoundingClientRect();
  var tt   = _tooltipEl.getBoundingClientRect();
  var gap  = 8;
  var top  = rect.bottom + gap;
  var left = rect.left;

  if (top + tt.height > window.innerHeight - 16) {
    top = rect.top - tt.height - gap;
    _tooltipEl.classList.add('bsw-tooltip--above');
  } else {
    _tooltipEl.classList.remove('bsw-tooltip--above');
  }
  left = Math.max(16, Math.min(left, window.innerWidth - tt.width - 16));

  _tooltipEl.style.top  = top  + 'px';
  _tooltipEl.style.left = left + 'px';
}

// Register scheduleShow with core.js so wire.js can invoke it without
// creating a circular dependency (wire → tooltip → core → wire).
registerScheduleShow(scheduleShow);
