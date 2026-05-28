/**
 * main.js — builds and wires the left sidebar navigation.
 * Sidebar skeleton (including #bible-version) builds synchronously so bible.js
 * can run immediately.  Topic links are populated async from data/topics.json.
 */

(function () {
  'use strict';

  /* ── Root detection ───────────────────────────────────────── */
  var _src  = (document.currentScript && document.currentScript.src) || '';
  var _root = _src ? new URL('../../', _src).href : '/';
  function _r(p) { return _root + p; }

  /* ── Module-level state shared between sidebar and reader ──── */
  var BOOK_STUDIES   = {};   // populated by loadTopics(); read by reader banner
  var _readerUpdate  = null; // set by initReaderStudyLink(); called after topics load

  /* ── Nav data ─────────────────────────────────────────────── */
  /* Topic subgroups start empty — loadTopics() fills them in.  */
  var NAV = {
    groups: [
      {
        id: 'topics',
        label: 'Topics',
        icon: '📚',
        children: [
          { label: '📋 All Topics', href: _r('topics/') }
        ],
        subgroups: [
          { id: 'bible-books', label: 'Bible Books',     items: [] },
          { id: 'topical',     label: 'Topical Studies', items: [] }
        ]
      },
      {
        id: 'library',
        label: 'Library',
        icon: '📜',
        children: [
          { label: '📋 All Documents', href: _r('library/') }
        ],
        subgroups: [
          {
            id: 'ecumenical',
            label: 'Ecumenical Creeds',
            items: [
              { label: "Apostles' Creed",  href: _r('library/apostles-creed/') },
              { label: 'Nicene Creed',     href: _r('library/nicene-creed/') },
              { label: 'Athanasian Creed', href: _r('library/athanasian-creed/') }
            ]
          },
          {
            id: 'reformed',
            label: 'Reformed',
            items: [
              { label: 'Heidelberg Catechism',         href: _r('library/heidelberg-catechism/') },
              { label: 'Belgic Confession',             href: _r('library/belgic-confession/') },
              { label: 'Canons of Dort',                href: _r('library/canons-of-dort/') },
              { label: 'Westminster Confession',        href: _r('library/westminster-confession/') },
              { label: 'Westminster Larger Catechism',  href: _r('library/westminster-larger-catechism/') },
              { label: 'Westminster Shorter Catechism', href: _r('library/westminster-shorter-catechism/') },
              { label: 'London Baptist Confession',     href: _r('library/london-baptist-confession/') }
            ]
          },
          {
            id: 'lutheran',
            label: 'Lutheran',
            items: [
              { label: 'Augsburg Confession', href: _r('library/augsburg-confession/') }
            ]
          },
          {
            id: 'anglican',
            label: 'Anglican',
            items: [
              { label: '39 Articles', href: _r('library/39-articles/') }
            ]
          }
        ]
      }
    ],
    tools: [
      { label: '📖 Reader',         href: _r('read/') },
      { label: '🔍 Search',         href: _r('search/') },
      { label: '📅 Reading Plans',  href: _r('plans/') },
      { label: '🌅 Devotionals',    href: _r('devotionals/') },
      { label: '⭐ Memory',          href: _r('memorize/') },
      { label: '📑 Topical Bible',  href: _r('topical/') },
      { label: '📘 Dictionary',      href: _r('dictionary/') }
    ]
  };

  /* ── URL helpers ──────────────────────────────────────────── */
  function _norm(href) {
    return href.replace(/\/index\.html(\?.*)?$/, '/').replace(/([^/])$/, '$1/');
  }
  var _locN  = _norm(window.location.href);
  var _rootN = _norm(_root);

  function isActive(href)   { return _locN === _norm(href); }
  function isAncestor(href) {
    var n = _norm(href);
    return n !== _rootN && _locN !== n && _locN.startsWith(n);
  }

  function subgroupHasActive(sg) {
    for (var i = 0; i < sg.items.length; i++) {
      if (isActive(sg.items[i].href) || isAncestor(sg.items[i].href)) return true;
    }
    return false;
  }

  function groupHasActive(group) {
    var s;
    for (var i = 0; i < group.children.length; i++) {
      if (isActive(group.children[i].href)) return true;
    }
    if (group.subgroups) {
      for (s = 0; s < group.subgroups.length; s++) {
        if (subgroupHasActive(group.subgroups[s])) return true;
      }
    }
    return false;
  }

  /* Is this a topic detail page (/topics/prayer/, /topics/revelation/) */
  var _pathname    = window.location.pathname.replace(/\/index\.html$/, '/').replace(/([^/])$/, '$1/');
  var _isTopicPage = /\/topics\/[^/]+\/$/.test(_pathname) && _pathname !== _norm(_r('topics/'));

  /* ── localStorage ─────────────────────────────────────────── */
  var _LS = 'bsw_sidebar';
  function getState()   { try { return localStorage.getItem(_LS); }  catch(e) { return null; } }
  function saveState(v) { try { localStorage.setItem(_LS, v); }      catch(e) {} }

  /* ── DOM helpers ──────────────────────────────────────────── */
  function mk(tag, cls) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    return e;
  }

  /* ── Build a collapsible sub-group within a group ── */
  function buildSubgroup(sg, groupId) {
    var active = subgroupHasActive(sg);
    var sgId   = 'sbsg-' + groupId + '-' + sg.id;

    var wrapper = mk('div', 'sb-subgroup');

    var btn = mk('button', 'sb-subgroup-btn');
    btn.setAttribute('aria-expanded', active ? 'true' : 'false');
    btn.setAttribute('aria-controls', sgId);
    if (active) btn.classList.add('is-active');

    var lbl   = mk('span', 'sb-subgroup-label');
    lbl.textContent = sg.label;
    var arrow = mk('span', 'sb-subgroup-arrow');
    arrow.innerHTML = '&#x25B6;';
    btn.appendChild(lbl);
    btn.appendChild(arrow);

    var items = mk('div', 'sb-subgroup-items');
    items.id = sgId;
    if (!active) items.setAttribute('hidden', '');

    sg.items.forEach(function (child) {
      var a = mk('a', 'sb-subchild');
      a.href = child.href;
      a.textContent = child.label;
      if (isActive(child.href)) a.setAttribute('aria-current', 'page');
      items.appendChild(a);
    });

    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      if (open) { items.setAttribute('hidden', ''); }
      else      { items.removeAttribute('hidden'); }
    });

    wrapper.appendChild(btn);
    wrapper.appendChild(items);
    return wrapper;
  }

  /* ── Build sidebar ────────────────────────────────────────── */
  function buildSidebar() {

    var sidebar = mk('aside', 'site-sidebar');
    sidebar.id  = 'site-sidebar';
    sidebar.setAttribute('aria-label', 'Site navigation');

    /* Head: logo + collapse button */
    var head   = mk('div', 'sb-head');
    var logo   = mk('a', 'sb-logo');
    logo.href  = _r('');
    logo.textContent = '📖 Bible Study';
    var colBtn = mk('button', 'sb-collapse-btn');
    colBtn.setAttribute('aria-label', 'Collapse sidebar');
    colBtn.setAttribute('aria-controls', 'site-sidebar');
    colBtn.innerHTML = '&#x2039;';
    head.appendChild(logo);
    head.appendChild(colBtn);
    sidebar.appendChild(head);

    /* Scrollable nav */
    var nav = mk('div', 'sb-nav');
    nav.setAttribute('role', 'navigation');

    /* Home link */
    var homeLink = mk('a', 'sb-link');
    homeLink.href = _r('');
    homeLink.textContent = 'Home';
    if (_locN === _rootN) homeLink.setAttribute('aria-current', 'page');
    nav.appendChild(homeLink);

    /* Version picker — built synchronously so bible.js finds it immediately */
    var verRow    = mk('div', 'sb-version');
    var verLabel  = document.createElement('label');
    verLabel.setAttribute('for', 'bible-version');
    verLabel.textContent = 'Version:';
    var verSelect = document.createElement('select');
    verSelect.id  = 'bible-version';
    verRow.appendChild(verLabel);
    verRow.appendChild(verSelect);
    nav.appendChild(verRow);

    nav.appendChild(mk('div', 'sb-divider'));

    /* Tool links */
    NAV.tools.forEach(function (tool) {
      var a   = mk('a', 'sb-group-btn');
      a.href  = tool.href;
      var lbl = mk('span', 'sb-group-label');
      lbl.textContent = tool.label;
      a.appendChild(lbl);
      if (isActive(tool.href)) {
        a.setAttribute('aria-current', 'page');
        a.classList.add('is-active');
      }
      nav.appendChild(a);
    });

    nav.appendChild(mk('div', 'sb-divider'));

    /* Groups */
    NAV.groups.forEach(function (group) {
      var active = groupHasActive(group);

      var wrapper = mk('div', 'sb-group');

      var btn = mk('button', 'sb-group-btn');
      btn.setAttribute('aria-expanded', active ? 'true' : 'false');
      btn.setAttribute('aria-controls', 'sbg-' + group.id);
      if (active) btn.classList.add('is-active');

      var lbl   = mk('span', 'sb-group-label');
      lbl.textContent = group.icon + ' ' + group.label;
      var arrow = mk('span', 'sb-group-arrow');
      arrow.innerHTML = '&#x25B6;';
      btn.appendChild(lbl);
      btn.appendChild(arrow);

      var items = mk('div', 'sb-group-items');
      items.id  = 'sbg-' + group.id;
      if (!active) items.setAttribute('hidden', '');

      group.children.forEach(function (child) {
        var a = mk('a', 'sb-child');
        a.href = child.href;
        a.textContent = child.label;
        if (isActive(child.href)) a.setAttribute('aria-current', 'page');
        items.appendChild(a);
      });

      if (group.subgroups) {
        group.subgroups.forEach(function (sg) {
          items.appendChild(buildSubgroup(sg, group.id));
        });
      }

      btn.addEventListener('click', function () {
        var open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', open ? 'false' : 'true');
        if (open) { items.setAttribute('hidden', ''); }
        else      { items.removeAttribute('hidden'); }
      });

      wrapper.appendChild(btn);
      wrapper.appendChild(items);
      nav.appendChild(wrapper);
    });

    sidebar.appendChild(nav);

    /* Collapse tab */
    var tab = mk('button', 'sidebar-tab');
    tab.setAttribute('aria-label', 'Toggle sidebar');
    tab.setAttribute('aria-controls', 'site-sidebar');
    tab.innerHTML = '&#x2039;';

    /* Mobile topbar */
    var topbar    = mk('div', 'mobile-topbar');
    topbar.setAttribute('aria-hidden', 'true');
    var hamburger = mk('button', 'mobile-topbar__hamburger');
    hamburger.setAttribute('aria-label', 'Open navigation');
    hamburger.setAttribute('aria-expanded', 'false');
    hamburger.setAttribute('aria-controls', 'site-sidebar');
    hamburger.innerHTML = '&#9776;';
    var topLogo   = mk('a', 'mobile-topbar__logo');
    topLogo.href  = _r('');
    topLogo.textContent = '📖 Bible Study';
    topbar.appendChild(hamburger);
    topbar.appendChild(topLogo);

    /* Backdrop */
    var backdrop = mk('div', 'sidebar-backdrop');
    backdrop.setAttribute('aria-hidden', 'true');

    /* Inject into DOM */
    document.body.insertBefore(sidebar, document.body.firstChild);
    document.body.appendChild(tab);
    document.body.appendChild(topbar);
    document.body.appendChild(backdrop);

    /* ── Initial collapse/overlay state ── */
    if (_isTopicPage) {
      document.body.classList.add('sidebar-overlay');
      tab.innerHTML = '&#x203A;';
    } else {
      var saved = getState();
      if (saved === 'collapsed') {
        document.body.classList.add('sidebar-collapsed');
        tab.innerHTML = '&#x203A;';
        colBtn.innerHTML = '&#x203A;';
        colBtn.setAttribute('aria-label', 'Expand sidebar');
      }
    }

    /* ── Event helpers ── */
    function isMobile() { return window.innerWidth < 1024; }

    function setCollapseArrow(collapsed) {
      var c = collapsed ? '&#x203A;' : '&#x2039;';
      tab.innerHTML    = c;
      colBtn.innerHTML = c;
      colBtn.setAttribute('aria-label', collapsed ? 'Expand sidebar' : 'Collapse sidebar');
    }

    function desktopToggle() {
      var collapsed = document.body.classList.toggle('sidebar-collapsed');
      saveState(collapsed ? 'collapsed' : 'open');
      setCollapseArrow(collapsed);
    }

    function overlayOpen()  { document.body.classList.add('sb-open');    tab.innerHTML = '&#x2039;'; }
    function overlayClose() { document.body.classList.remove('sb-open'); tab.innerHTML = '&#x203A;'; }
    function mobileOpen()   { document.body.classList.add('sb-open');    hamburger.setAttribute('aria-expanded', 'true'); }
    function mobileClose()  { document.body.classList.remove('sb-open'); hamburger.setAttribute('aria-expanded', 'false'); }

    colBtn.addEventListener('click', function () {
      if (isMobile())        { mobileClose(); }
      else if (_isTopicPage) { overlayClose(); }
      else                   { desktopToggle(); }
    });

    tab.addEventListener('click', function () {
      if (isMobile()) return;
      if (_isTopicPage) {
        document.body.classList.contains('sb-open') ? overlayClose() : overlayOpen();
      } else {
        desktopToggle();
      }
    });

    hamburger.addEventListener('click', function () {
      document.body.classList.contains('sb-open') ? mobileClose() : mobileOpen();
    });

    backdrop.addEventListener('click', function () {
      mobileClose();
      if (_isTopicPage) overlayClose();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('sb-open')) {
        mobileClose();
        if (_isTopicPage) overlayClose();
      }
    });

    var legacyToggle = document.getElementById('topic-sidebar-toggle');
    if (legacyToggle) legacyToggle.style.display = 'none';
  }

  /* ── Load topics from data/topics.json ───────────────────── */
  function loadTopics() {
    var booksEl   = document.getElementById('sbsg-topics-bible-books');
    var topicalEl = document.getElementById('sbsg-topics-topical');
    if (!booksEl && !topicalEl) return;

    fetch(_r('data/topics.json'))
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (topics) {
        topics.forEach(function (t) {
          var href = _r('topics/' + t.slug + '/');
          var a    = mk('a', 'sb-subchild');
          a.href   = href;
          a.textContent = t.label;
          if (isActive(href)) a.setAttribute('aria-current', 'page');

          if (t.type === 'book') { if (booksEl)   booksEl.appendChild(a); }
          else                   { if (topicalEl) topicalEl.appendChild(a); }

          if (t.book) BOOK_STUDIES[t.book] = { href: href, label: t.label };
        });

        /* Expand the subgroup (and its parent group) if active page is inside */
        [booksEl, topicalEl].forEach(function (itemsEl) {
          if (!itemsEl || !itemsEl.querySelector('[aria-current="page"]')) return;

          var sgBtn = itemsEl.previousElementSibling;
          if (sgBtn && sgBtn.classList.contains('sb-subgroup-btn')) {
            sgBtn.setAttribute('aria-expanded', 'true');
            sgBtn.classList.add('is-active');
            itemsEl.removeAttribute('hidden');
          }

          /* Walk up to find the enclosing .sb-group-items */
          var node = itemsEl.parentNode;
          while (node && !node.classList.contains('sb-group-items')) node = node.parentNode;
          if (node) {
            node.removeAttribute('hidden');
            var gBtn = node.previousElementSibling;
            if (gBtn && gBtn.classList.contains('sb-group-btn')) {
              gBtn.setAttribute('aria-expanded', 'true');
              gBtn.classList.add('is-active');
            }
          }
        });

        if (_readerUpdate) _readerUpdate();
      })
      .catch(function () { /* fail silently — static items still render */ });
  }

  /* ── Reader: show study-guide link when a book with a study is open ── */
  function initReaderStudyLink() {
    var bookSel   = document.getElementById('reader-book-select');
    var resultsEl = document.getElementById('reader-results');
    if (!bookSel || !resultsEl) return;

    var banner = mk('div', 'reader-study-banner');
    banner.setAttribute('hidden', '');
    resultsEl.parentNode.insertBefore(banner, resultsEl);

    function update() {
      var bookId = bookSel.value;
      var study  = BOOK_STUDIES[bookId];
      if (study) {
        var bookName = bookSel.options[bookSel.selectedIndex]
          ? bookSel.options[bookSel.selectedIndex].text
          : study.label;
        banner.innerHTML =
          '<span class="reader-study-banner__icon">📖</span>' +
          '<span class="reader-study-banner__text">Study guide available:</span>' +
          '<a class="reader-study-banner__link" href="' + study.href + '">' +
            bookName + ' Study →' +
          '</a>';
        banner.removeAttribute('hidden');
      } else {
        banner.setAttribute('hidden', '');
      }
    }

    _readerUpdate = update;
    bookSel.addEventListener('change', update);

    if (typeof MutationObserver !== 'undefined') {
      new MutationObserver(update).observe(resultsEl, { childList: true });
    }
  }

  buildSidebar();
  initReaderStudyLink();
  loadTopics();

})();
