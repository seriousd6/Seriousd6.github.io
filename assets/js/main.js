/**
 * main.js — Bible Study Website core JavaScript
 *
 * Responsibilities:
 *  1. Build and wire the Studies slide-in nav panel
 *
 * Version persistence is handled entirely by bible.js (BibleUI).
 */

(function () {
  'use strict';

  /* ── Path detection ─────────────────────────────────────── */
  var _src  = (document.currentScript && document.currentScript.src) || '';
  var _root = _src ? new URL('../../', _src).href : '/';
  function _r(path) { return _root + path; }

  /* ── Study library ──────────────────────────────────────── */
  var LIBRARY = {
    books: [
      { title: '📜 Revelation',  href: _r('topics/revelation/') }
    ],
    topics: [
      { title: '🙏 Prayer', href: _r('topics/prayer/') }
    ]
  };

  /* ── Panel state ────────────────────────────────────────── */
  var _panel    = null;
  var _overlay  = null;
  var _panelBtn = null;

  function buildNavPanel() {
    var nav = document.querySelector('.site-header .site-nav') ||
              document.querySelector('.site-header--topic .site-nav');
    if (!nav) return;

    /* Studies button */
    _panelBtn = document.createElement('button');
    _panelBtn.className = 'nav-panel-btn';
    _panelBtn.setAttribute('aria-expanded', 'false');
    _panelBtn.setAttribute('aria-controls', 'nav-panel');
    _panelBtn.textContent = 'Studies ▾';
    nav.appendChild(_panelBtn);

    /* Backdrop overlay */
    _overlay = document.createElement('div');
    _overlay.className = 'nav-panel-overlay';
    _overlay.id = 'nav-panel-overlay';
    document.body.appendChild(_overlay);

    /* Slide-in panel */
    _panel = document.createElement('nav');
    _panel.className = 'nav-panel';
    _panel.id = 'nav-panel';
    _panel.setAttribute('aria-label', 'Study library');

    var loc = window.location.href.replace(/\/(?:index\.html)?$/, '/');

    function makeSection(title, items) {
      var sec = document.createElement('div');
      sec.className = 'nav-panel__section';
      var h = document.createElement('h3');
      h.className = 'nav-panel__section-title';
      h.textContent = title;
      sec.appendChild(h);
      var ul = document.createElement('ul');
      ul.className = 'nav-panel__list';
      items.forEach(function (item) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = item.href;
        a.textContent = item.title;
        var normalized = item.href.replace(/\/(?:index\.html)?$/, '/');
        if (loc.startsWith(normalized)) {
          a.setAttribute('aria-current', 'page');
        }
        li.appendChild(a);
        ul.appendChild(li);
      });
      sec.appendChild(ul);
      return sec;
    }

    /* Panel header row */
    var hdr = document.createElement('div');
    hdr.className = 'nav-panel__header';
    var hTitle = document.createElement('span');
    hTitle.className = 'nav-panel__heading';
    hTitle.textContent = 'Studies';
    var closeBtn = document.createElement('button');
    closeBtn.className = 'nav-panel__close';
    closeBtn.setAttribute('aria-label', 'Close panel');
    closeBtn.innerHTML = '&#x2715;';
    hdr.appendChild(hTitle);
    hdr.appendChild(closeBtn);

    _panel.appendChild(hdr);
    _panel.appendChild(makeSection('Bible Books', LIBRARY.books));
    _panel.appendChild(makeSection('Topical Studies', LIBRARY.topics));
    document.body.appendChild(_panel);

    /* Events */
    _panelBtn.addEventListener('click', openPanel);
    closeBtn.addEventListener('click', closePanel);
    _overlay.addEventListener('click', closePanel);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && _panel.classList.contains('is-open')) closePanel();
    });
  }

  function openPanel() {
    if (!_panel) return;
    _panel.classList.add('is-open');
    _overlay.classList.add('is-visible');
    _panelBtn.setAttribute('aria-expanded', 'true');
    var closeBtn = _panel.querySelector('.nav-panel__close');
    if (closeBtn) closeBtn.focus();
  }

  function closePanel() {
    if (!_panel) return;
    _panel.classList.remove('is-open');
    _overlay.classList.remove('is-visible');
    _panelBtn.setAttribute('aria-expanded', 'false');
    _panelBtn.focus();
  }

  buildNavPanel();

})();
