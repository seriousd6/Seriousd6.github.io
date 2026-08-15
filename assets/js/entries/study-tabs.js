/* entries/study-tabs.js — multi-part topical studies as sub-tabs.
 *
 * Same paradigm as the book-commentary chapter picker (entries/commentary.js):
 * a sticky bar of buttons, one panel shown at a time, deep-linkable by hash.
 * The difference is that every panel is already in the DOM, so switching is
 * instant and needs no fetch — a multi-part study is one page, not N.
 *
 * CONTRACT (see src/pages/topics/korahs-rebellion/index.astro):
 *   .tg-tabs            sticky bar, data-current="<id>"
 *   .tg-tabs__btn       one per part, data-part="<id>", href="#<id>"
 *   .tg-part            one panel per part, id="<id>"
 *
 * Progressive enhancement: panels are visible in the served HTML and only
 * hidden once this runs, so with JS off the study reads as one long page.
 */
import { boot } from '../core-boot.js';

function initStudyTabs() {
  var bar = document.querySelector('.tg-tabs');
  if (!bar) return;
  var btns = Array.prototype.slice.call(bar.querySelectorAll('.tg-tabs__btn'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('.tg-part'));
  if (!btns.length || !panels.length) return;
  var grid = bar.querySelector('.tg-tabs__grid');

  // The in-part Contents bar sticks below this one, so it needs this one's
  // height. Publishing it as a custom property keeps the arithmetic in CSS and
  // means studies without a part picker simply never define it (--tg-tabs-h
  // falls back to 0, which is the correct offset for them).
  function publishHeight() {
    var h = Math.round(bar.getBoundingClientRect().height);
    if (h) document.documentElement.style.setProperty('--tg-tabs-h', h + 'px');
  }

  // The strip scrolls sideways on a narrow screen. Two things follow: the
  // reader needs to see that it does (the edge fade), and the active tab must
  // never be one of the ones parked off-screen.
  function syncOverflow() {
    if (!grid) return;
    var slack = grid.scrollWidth - grid.clientWidth;
    grid.classList.toggle('is-overflowing', slack > 2);
    grid.classList.toggle('at-start', grid.scrollLeft <= 2);
    grid.classList.toggle('at-end', grid.scrollLeft >= slack - 2);
  }

  function revealTab(btn) {
    if (!grid || !btn) return;
    // Deliberately not scrollIntoView: that would scroll the page as well as
    // the strip, fighting the panel scroll we do right after switching tabs.
    var g = grid.getBoundingClientRect(), b = btn.getBoundingClientRect();
    var pad = 16;
    if (b.left < g.left + pad) grid.scrollLeft -= (g.left + pad - b.left);
    else if (b.right > g.right - pad) grid.scrollLeft += (b.right - (g.right - pad));
    syncOverflow();
  }

  function show(id, push) {
    var found = panels.some(function (p) { return p.id === id; });
    if (!found) return false;
    panels.forEach(function (p) { p.hidden = p.id !== id; });
    btns.forEach(function (b) {
      var on = b.dataset.part === id;
      b.classList.toggle('is-active', on);
      if (on) { b.setAttribute('aria-current', 'true'); revealTab(b); }
      else b.removeAttribute('aria-current');
    });
    bar.dataset.current = id;
    if (push) {
      try { history.pushState(null, '', '#' + id); } catch (e) {}
    }
    return true;
  }

  btns.forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      if (show(b.dataset.part, true)) {
        // Switching panels should land the reader at the top of the new part,
        // not wherever the old one had them scrolled. Scroll the panel rather
        // than the bar: the bar is sticky, so its measured top is already the
        // pinned offset and scrolling to it walks the page down a little
        // further on every click. .tg-part carries the scroll-margin that
        // clears the topbar and the bar itself.
        var target = document.getElementById(b.dataset.part);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // In-panel TOC links must reveal their panel before jumping to the anchor,
  // otherwise a link into a hidden section scrolls nowhere.
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a || a.classList.contains('tg-tabs__btn')) return;
    var id = a.getAttribute('href').slice(1);
    if (!id) return;
    var target = document.getElementById(id);
    if (!target) return;
    var panel = target.closest('.tg-part');
    if (panel && panel.hidden) show(panel.id, false);
  });

  window.addEventListener('popstate', function () {
    show((location.hash || '').slice(1) || panels[0].id, false);
  });

  function remeasure() { publishHeight(); syncOverflow(); }

  if (grid) grid.addEventListener('scroll', syncOverflow, { passive: true });
  window.addEventListener('resize', remeasure);
  remeasure();
  // Self-hosted fonts land after first paint and change every tab's width and
  // the bar's height, which can turn a strip that just fit into a scrolling
  // one (or the reverse). Re-measure once they are in.
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () {
      remeasure();
      var on = bar.querySelector('.tg-tabs__btn.is-active');
      if (on) revealTab(on);
    }).catch(function () {});
  }

  var initial = (location.hash || '').slice(1);
  var target = initial && document.getElementById(initial);
  var panel = target && target.closest('.tg-part');
  if (panel) {
    show(panel.id, false);
    // The browser already jumped to the anchor while every panel was visible.
    // Hiding the others shrinks the document under that scroll offset, which
    // can leave the reader staring at blank space. Re-anchor on the next frame,
    // once the post-hide layout is final.
    var landOn = target;
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { landOn.scrollIntoView(); });
    });
  } else {
    if (!show(initial, false)) show(panels[0].id, false);
  }
}

boot(initStudyTabs);
