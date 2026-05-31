/**
 * main.js — builds and wires the left sidebar navigation.
 *
 * Loaded as a plain <script> (not a module) so it runs before app.js and can
 * insert the sidebar synchronously. This guarantees #bible-version exists in the
 * DOM when app.js calls populateVersionPicker() and wireVersionPicker().
 *
 * Responsibilities:
 *   - Detects the site root from its own <script src> so links work from any
 *     subdirectory (important for GitHub Pages).
 *   - Builds the full sidebar DOM: logo, version picker, tool links, collapsible
 *     groups (Topics, Library).
 *   - Loads data/topics.json asynchronously and populates the Bible Books and
 *     Topical Studies subgroups. Static library items are hardcoded here.
 *   - Manages sidebar collapse state in localStorage (key: bsw_sidebar).
 *   - On the reader page, shows a "Study guide available" banner when the open
 *     book has a corresponding topic page.
 *
 * This file must not import ES modules — it is a non-module script.
 */

(function () {
  'use strict';

  /* ── Root detection ───────────────────────────────────────── */
  // Use the script's own src URL to derive the site root, so _r() builds correct
  // hrefs regardless of which subdirectory the page is in. Falls back to '/' for
  // environments where currentScript is unavailable (e.g. deferred execution).
  var _src  = (document.currentScript && document.currentScript.src) || '';
  var _root = _src ? new URL('../../', _src).href : '/';
  function _r(p) { return _root + p; }

  /* ── Module-level state shared between sidebar and reader ──── */
  // BOOK_STUDIES: maps book IDs (e.g. "REV") to { href, label } objects.
  // Built by loadTopics() after topics.json loads; read by initReaderStudyLink()
  // to show the study guide banner when the reader navigates to a covered book.
  var BOOK_STUDIES   = {};
  // _readerUpdate: callback set by initReaderStudyLink(); invoked after topics load
  // so the banner can appear if the reader already has a book selected.
  var _readerUpdate  = null;

  /* ── Nav data ─────────────────────────────────────────────── */
  // Static navigation tree. The "topics" group's subgroup items start empty —
  // loadTopics() appends links after fetching data/topics.json.
  // Library items are hardcoded here since they don't change without a code edit.
  // Tool links appear above the collapsible groups so they're always visible.
  var NAV = {
    tools: [
      { label: '📖 The Holy Bible', href: _r('read/') },
      { label: '🔍 Search', href: _r('search/') }
    ],
    groups: [
      {
        id: 'discipline',
        label: 'Discipline',
        icon: '✝',
        children: [
          { label: '📅 Reading Plans',  href: _r('plans/') },
          { label: '🌅 Devotionals',    href: _r('devotionals/') },
          { label: '⭐ Memory',          href: _r('memorize/') },
          { label: '🙏 Prayer Journal', href: _r('journal/') },
          { label: '📝 Personal Notes', href: _r('notes/') }
        ]
      },
      {
        id: 'reference',
        label: 'Reference',
        icon: '📘',
        children: [
          { label: '📖 Dictionary',  href: _r('dictionary/') },
          { label: '🕰 Timeline',    href: _r('timeline/') },
          { label: '🗺 Maps',        href: _r('maps/') },
          { label: '☁ Word Cloud',  href: _r('wordcloud/') }
        ]
      },
      {
        id: 'library',
        label: 'Library',
        icon: '📚',
        children: [
          { label: '📋 Library', href: _r('library/') }
        ],
        subgroups: [
          { id: 'book-overviews',   label: 'Bible Book Overviews', items: [] },
          { id: 'study-guides',     label: 'Study Guides',         items: [] },
          { id: 'topical-articles', label: 'Topical Articles',     items: [] }
        ]
      }
    ]
  };

  /* ── URL helpers ──────────────────────────────────────────── */
  // _norm: normalises a URL to always end with '/' and strips trailing index.html
  // so that isActive() correctly identifies the current page regardless of how
  // the URL was typed (e.g. /read/ and /read/index.html should both match).
  function _norm(href) {
    return href.replace(/\/index\.html(\?.*)?$/, '/').replace(/([^/])$/, '$1/');
  }
  var _locN  = _norm(window.location.href);
  var _rootN = _norm(_root);

  // isActive: true when the normalised current URL exactly matches href.
  // isAncestor: true when the current URL is under href (for parent group highlighting).
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
      if (isActive(group.children[i].href) || isAncestor(group.children[i].href)) return true;
    }
    if (group.subgroups) {
      for (s = 0; s < group.subgroups.length; s++) {
        if (subgroupHasActive(group.subgroups[s])) return true;
      }
    }
    return false;
  }

  // _isTopicPage: true when viewing an individual topic (e.g. /topics/prayer/).
  // Topic pages use sidebar-overlay mode — the sidebar floats over content rather
  // than pushing it aside, to give more reading space.
  var _pathname    = window.location.pathname.replace(/\/index\.html$/, '/').replace(/([^/])$/, '$1/');
  var _isTopicPage = /\/topics\/[^/]+\/$/.test(_pathname) && _pathname !== _norm(_r('topics/'));

  /* ── localStorage ─────────────────────────────────────────── */
  // Persists the sidebar open/collapsed state across page loads.
  // Values: "collapsed" | "open" (or null = default open).
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
  // Constructs and inserts the full sidebar DOM before any other body content.
  // Also creates the collapse tab, mobile topbar (hamburger), and backdrop overlay.
  // Collapse behaviour differs by context:
  //   Desktop non-topic page  → pushes content (sidebar-collapsed class on body)
  //   Desktop topic page      → overlays content (sidebar-overlay + sb-open toggle)
  //   Mobile (<1024 px)       → always overlay, toggled by hamburger button
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

    /* Version picker — must exist synchronously so app.js can call
     * populateVersionPicker() and wireVersionPicker() after metadata loads.
     * The <select> starts empty; app.js fills it from versions.json. */
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

    /* Theme toggle — appended at the bottom of the nav scroll area */
    nav.appendChild(mk('div', 'sb-divider'));
    var themeBtn = mk('button', '');
    themeBtn.id = 'bsw-theme-btn';
    function _isDark() {
      var th = document.documentElement.getAttribute('data-theme');
      if (th) return th === 'dark';
      return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
    function _updateThemeLabel() {
      themeBtn.textContent = _isDark() ? '☀ Light Mode' : '🌙 Dark Mode';
    }
    _updateThemeLabel();
    themeBtn.addEventListener('click', function () {
      var next = _isDark() ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('bsw_theme', next); } catch (e) {}
      _updateThemeLabel();
    });
    nav.appendChild(themeBtn);

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
  // Fetches the topics manifest and appends links into the Bible Books and
  // Topical Studies subgroups inside the sidebar. Each topic entry must have
  // { slug, label, type } where type is "book" (goes under Bible Books) or
  // anything else (goes under Topical Studies). An optional "book" field maps
  // the topic to a book ID so the reader can show the study guide banner.
  // If the fetch fails, static sidebar items still render normally.
  function loadTopics() {
    var bookEl    = document.getElementById('sbsg-library-book-overviews');
    var studyEl   = document.getElementById('sbsg-library-study-guides');
    var topicalEl = document.getElementById('sbsg-library-topical-articles');
    if (!bookEl && !studyEl && !topicalEl) return;

    fetch(_r('data/topics.json'))
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (topics) {
        topics.forEach(function (t) {
          // Allow an explicit href override (e.g. study-guides/) instead of the default topics/ path.
          var href = t.href ? _r(t.href) : _r('topics/' + t.slug + '/');
          var a    = mk('a', 'sb-subchild');
          a.href   = href;
          a.textContent = t.label;
          if (isActive(href)) a.setAttribute('aria-current', 'page');

          if (t.type === 'book')  { if (bookEl)    bookEl.appendChild(a); }
          else if (t.type === 'study') { if (studyEl) studyEl.appendChild(a); }
          else                    { if (topicalEl) topicalEl.appendChild(a); }

          if (t.book) BOOK_STUDIES[t.book] = { href: href, label: t.label };
        });

        /* Expand the subgroup (and its parent group) if active page is inside */
        [bookEl, studyEl, topicalEl].forEach(function (itemsEl) {
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
  // Watches the reader's book selector and verse container for changes.
  // When the reader is showing a book that has a corresponding topic page
  // in BOOK_STUDIES, a banner appears above the chapter with a link to that page.
  // The banner is hidden for books without a study guide.
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
