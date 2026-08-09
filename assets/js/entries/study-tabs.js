/* entries/study-tabs.js — multi-part topical studies as sub-tabs.
 *
 * Same paradigm as the book-commentary chapter picker (entries/commentary.js):
 * a sticky bar of buttons, one panel shown at a time, deep-linkable by hash.
 * The difference is that every panel is already in the DOM, so switching is
 * instant and needs no fetch — a five-part study is one page, not five.
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

  function show(id, push) {
    var found = panels.some(function (p) { return p.id === id; });
    if (!found) return false;
    panels.forEach(function (p) { p.hidden = p.id !== id; });
    btns.forEach(function (b) {
      var on = b.dataset.part === id;
      b.classList.toggle('is-active', on);
      if (on) b.setAttribute('aria-current', 'true');
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
        // Keep the tab bar in view: switching panels should land the reader at
        // the top of the new part, not wherever the old one had them scrolled.
        var top = bar.getBoundingClientRect().top + window.pageYOffset - 8;
        window.scrollTo({ top: top, behavior: 'smooth' });
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

  var initial = (location.hash || '').slice(1);
  var target = initial && document.getElementById(initial);
  var panel = target && target.closest('.tg-part');
  if (panel) {
    show(panel.id, false);
    // The browser already jumped to the anchor while every panel was visible.
    // Hiding five of them shrinks the document under that scroll offset, which
    // can leave the reader staring at blank space. Re-anchor on the next frame,
    // once the post-hide layout is final — and anchor on the tab bar rather than
    // the panel, so the landing position is the same however the panel resizes.
    var landOn = (target !== panel) ? target : bar;
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { landOn.scrollIntoView(); });
    });
  } else {
    if (!show(initial, false)) show(panels[0].id, false);
  }
}

boot(initStudyTabs);
