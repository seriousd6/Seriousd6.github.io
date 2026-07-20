/* entries/commentary.js — Full Treatment page (topics/<book>/commentary.html).
 *
 * Boots the shared UI (ref-link wiring, verse modal) and wires the chapter nav.
 * Small books render every chapter statically (nav = scroll + active-state only).
 * Many-chapter books (data-lazy) show ONE chapter at a time and lazy-load the
 * rest on demand via loadCommentary(book, 'exposition', ch) — the same blessed
 * path-resolution + cache the reader uses. See src/pages/topics/[book]/commentary.astro.
 */
'use strict';
import { boot } from '../core-boot.js';
import { loadCommentary } from '../core.js';
import { wireRefLinks } from '../wire.js';

var READER = '/read/?ref=';
function rhref(ref) { return READER + encodeURIComponent(ref); }
function refLink(ref, text, cls) {
  return '<a class="ref' + (cls ? ' ' + cls : '') + '" data-ref="' + ref + '" href="' + rhref(ref) + '">' + text + '</a>';
}
function lens(cls, label, html) {
  if (!html) return '';
  return '<div class="bkc-lens bkc-lens--' + cls + '"><span class="bkc-lens__label">' + label + '</span><div class="bkc-lens__body">' + html + '</div></div>';
}

// Build one chapter's HTML, matching src/pages/topics/[book]/commentary.astro.
function renderChapter(bookName, ch, data) {
  var cmeta = data._meta || {};
  var keys = Object.keys(data).filter(function (k) { return k !== '_meta'; })
    .sort(function (a, z) { return parseInt(a, 10) - parseInt(z, 10); });
  var head = '<div class="bkc-chapter__head"><span class="bkc-chapter__num">' + bookName + ' ' + ch + '</span>' +
    (cmeta.title ? '<span class="bkc-chapter__title">' + cmeta.title + '</span>' : '') +
    refLink(bookName + ' ' + ch, 'read the chapter →', 'bkc-chapter__read') + '</div>';

  var body = keys.map(function (k, i) {
    var sec = data[k];
    var h = '<h3 class="bkc-rubric"><span class="bkc-rubric__mark" aria-hidden="true">❧</span>' +
      '<span class="bkc-rubric__label">' + (sec.pericope_label || '') + '</span>' +
      (sec.range ? refLink(bookName + ' ' + ch + ':' + sec.range, bookName + ' ' + ch + ':' + sec.range, 'bkc-rubric__ref') : '') + '</h3>';
    var expo = sec.exposition ? '<div class="bkc-exposition' + (i === 0 ? ' bkc-exposition--lead' : '') + '">' + sec.exposition + '</div>' : '';
    var lenses = lens('lang', 'Original language', sec.original_language) +
      lens('hist', 'Historical context', sec.historical_context) +
      lens('christ', 'Christ here', sec.christ);
    var verses = '';
    if (sec.verses && sec.verses.length) {
      verses = '<dl class="bkc-verses">' + sec.verses.map(function (v) {
        return '<div class="bkc-verse"><dt class="bkc-verse__num">' +
          refLink(bookName + ' ' + ch + ':' + v.v, 'v.' + v.v) +
          '</dt><dd class="bkc-verse__note">' + (v.note || '') + '</dd></div>';
      }).join('') + '</dl>';
    }
    var voices = '';
    var ws = sec.witnesses || [], xs = sec.external || [];
    if (ws.length || xs.length) {
      voices = '<aside class="bkc-voices"><div class="bkc-voices__head">Voices on this section</div>' +
        ws.map(function (w) {
          return '<div class="bkc-voice"><span class="bkc-voice__name">' + w.voice + '</span>' +
            (w.tradition ? '<span class="bkc-voice__trad">' + w.tradition + '</span>' : '') +
            (w.point ? '<span class="bkc-voice__point">' + w.point + '</span>' : '') + '</div>';
        }).join('') +
        xs.map(function (x) {
          return '<div class="bkc-voice bkc-voice--external"><span class="bkc-voice__name">' + x.name +
            (x.work ? '<span class="bkc-voice__work">, ' + x.work + (x.year ? ' (' + x.year + ')' : '') + '</span>' : '') + '</span>' +
            '<span class="bkc-voice__trad bkc-voice__trad--ext">external</span>' +
            (x.point ? '<span class="bkc-voice__point">' + x.point + '</span>' : '') + '</div>';
        }).join('') + '</aside>';
    }
    var app = sec.application ? '<div class="bkc-application"><span class="bkc-application__label">For today</span><div class="bkc-application__body">' + sec.application + '</div></div>' : '';
    return '<article class="bkc-section" id="ch-' + ch + '-v-' + k + '">' + h + expo + lenses + verses + voices + app + '</article>';
  }).join('');

  var refl = '';
  if (cmeta.reflection && cmeta.reflection.length) {
    refl = '<div class="bkc-reflection"><span class="bkc-reflection__label">For reflection</span><ol class="bkc-reflection__list">' +
      cmeta.reflection.map(function (q) { return '<li>' + q + '</li>'; }).join('') + '</ol></div>';
  }
  return '<section class="bkc-chapter" id="ch-' + ch + '" data-ch="' + ch + '">' + head + body + refl + '</section>';
}

function initCommentaryTreatment() {
  var root = document.querySelector('.treatment[data-book]');
  if (!root) return;
  var nav = root.querySelector('.bkc-chapternav');
  var host = root.querySelector('#bkc-commentary');
  if (!nav || !host) return;
  var bookId = root.dataset.book, bookName = root.dataset.bookName || bookId;
  var lazy = root.dataset.lazy === '1';
  var btns = Array.prototype.slice.call(nav.querySelectorAll('.bkc-chapternav__btn'));

  function setActive(ch) {
    btns.forEach(function (b) { b.classList.toggle('is-active', b.dataset.ch === String(ch)); });
    nav.dataset.current = String(ch);
  }

  if (!lazy) {
    // all chapters are on the page — nav just scrolls + tracks active on scroll
    btns.forEach(function (b) {
      b.addEventListener('click', function () { setActive(b.dataset.ch); });
    });
    var sections = Array.prototype.slice.call(host.querySelectorAll('.bkc-chapter'));
    if ('IntersectionObserver' in window && sections.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) setActive(e.target.dataset.ch); });
      }, { rootMargin: '-45% 0px -50% 0px' });
      sections.forEach(function (s) { io.observe(s); });
    }
    return;
  }

  // lazy: one chapter at a time; swap on click
  var loading = false;
  function show(ch) {
    if (loading || nav.dataset.current === String(ch)) return;
    loading = true;
    host.setAttribute('aria-busy', 'true');
    host.style.opacity = '0.5';
    loadCommentary(bookId, 'exposition', ch).then(function (res) {
      var data = res && res[String(ch)];
      if (data) {
        host.innerHTML = renderChapter(bookName, ch, data);
        wireRefLinks();
        setActive(ch);
        try { history.replaceState(null, '', '#ch-' + ch); } catch (e) {}
        nav.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      host.style.opacity = '';
      host.removeAttribute('aria-busy');
      loading = false;
    });
  }
  btns.forEach(function (b) {
    b.addEventListener('click', function (e) { e.preventDefault(); show(parseInt(b.dataset.ch, 10)); });
  });
  // deep-link support (#ch-N)
  var m = (location.hash || '').match(/^#ch-(\d+)$/);
  if (m) show(parseInt(m[1], 10));
}

boot(initCommentaryTreatment);
