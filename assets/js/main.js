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
  // INTENT: BOOK_STUDIES is populated from data/books-content.json (primary) and
  //   data/topics.json (fallback). Both are async; _readerUpdate is set by
  //   initReaderStudyLink() so the banner fires whenever either load completes.
  //   _bookContent holds the full books-content.json object for tier-aware banners.
  // CHANGE? If books-content.json schema changes (guide/deep_dive/commentary keys),
  //   update getBannerItems() and loadBooksContent() below. If topics.json is
  //   removed, also remove the loadTopics() BOOK_STUDIES fallback path.
  // VERIFY: Open the reader on Romans; the study banner shows tier links.
  //   Open on a book with no content; banner is hidden.
  var BOOK_STUDIES   = {};
  var _bookContent   = null;
  var _readerUpdate  = null;

  /* ── Nav data ─────────────────────────────────────────────── */
  // Static navigation tree. The "topics" group's subgroup items start empty —
  // loadTopics() appends links after fetching data/topics.json.
  // Library items are hardcoded here since they don't change without a code edit.
  // Tool links appear above the collapsible groups so they're always visible.
  var NAV = {
    tools: [
      { label: '📖 The Holy Bible',        href: _r('read/') },
      { label: '📜 Apocrypha',             href: _r('apocrypha/') },
      { label: '🔍 Explore',               href: _r('search/') },
      { label: '📚 Studies',               href: _r('studies/') },
      { label: '✝ Discipline',             href: _r('discipline/') },
      { label: '🔬 Original Language Study', href: _r('translation/workshop/') },
      { label: 'ℹ About / AI',               href: _r('about/') }
    ],
    groups: [
      {
        id: 'history',
        label: 'History',
        icon: '🕰',
        children: [
          { label: '📜 Biblical Timeline',  href: _r('history/?tab=timeline') },
          { label: '⛪ Church History',     href: _r('history/?tab=church') },
          { label: '🗺 Maps',               href: _r('history/?tab=maps') },
          { label: '🎬 Animated Map',       href: _r('history/?tab=timelapse') }
        ]
      },
      {
        id: 'explore',
        label: 'Explore',
        icon: '🔍',
        children: [
          { label: '🔍 Search',        href: _r('search/') },
          { label: '📑 Topics',        href: _r('search/?tab=topics') },
          { label: '📖 Study Guides',  href: _r('search/?tab=guides') },
          { label: '📘 Biblepedia',     href: _r('biblepedia/') },
          { label: '☁ Word Cloud',     href: _r('search/?tab=wordcloud') }
        ]
      },
      {
        id: 'discipline',
        label: 'Discipline',
        icon: '✝',
        children: [
          { label: '✝ Discipline Hub',    href: _r('discipline/') },
          { label: '📅 Discipline History', href: _r('discipline/?tab=history') },
          { label: '📊 Reading Progress', href: _r('progress/') }
        ]
      },
      {
        id: 'library',
        label: 'Library',
        icon: '📚',
        children: [
          { label: '📋 Library',                href: _r('library/') },
          { label: '📚 Reading History',        href: _r('library/progress/') }
        ],
        subgroups: []
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
    if (new URLSearchParams(location.search).get('minimal')) {
      /* No sidebar in minimal/iframe mode — remove the 240px body padding-left
         that style.css applies by default so the page fills the iframe fully. */
      document.body.classList.add('sidebar-collapsed');
      return;
    }

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

    /* Translation Workshop — pinned footer at the very bottom of the sidebar */
    var sbFooter = mk('div', 'sb-footer');
    var wsLink = mk('a', 'sb-workshop-link');
    wsLink.href = _r('translation/workshop/');
    wsLink.textContent = '⚙ Translation Workshop';
    if (isActive(_r('translation/workshop/'))) wsLink.setAttribute('aria-current', 'page');
    sbFooter.appendChild(wsLink);
    sidebar.appendChild(sbFooter);

    /* Collapse tab */
    var tab = mk('button', 'sidebar-tab');
    tab.setAttribute('aria-label', 'Toggle sidebar');
    tab.setAttribute('aria-controls', 'site-sidebar');
    tab.innerHTML = '&#x2039;';

    /* Mobile topbar */
    var topbar    = mk('div', 'mobile-topbar');
    topbar.setAttribute('role', 'banner');
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

  /* ── Load books-content.json — primary source for BOOK_STUDIES ── */
  // INTENT: Fetches the books-content manifest and builds BOOK_STUDIES (used
  //   by the reader study banner). Also stores the full manifest in _bookContent
  //   so getBannerItems() can make tier-aware link decisions per navigation state.
  //   Falls back gracefully — if fetch fails, the topics.json fallback below
  //   provides basic BOOK_STUDIES entries for books with existing study pages.
  // CHANGE? If books-content.json schema changes (guide/deep_dive/commentary
  //   keys or the url field name), update both here and in getBannerItems().
  // VERIFY: Open reader on Romans — study banner appears. Open on Genesis —
  //   banner is hidden.
  function loadBooksContent() {
    fetch(_r('data/books-content.json'))
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (data) {
        _bookContent = data;
        if (data.books) {
          Object.keys(data.books).forEach(function (bookId) {
            var bc = data.books[bookId];
            var best = (bc.commentary && bc.commentary.exists && bc.commentary.url)
              || (bc.deep_dive && bc.deep_dive.exists && bc.deep_dive.url)
              || (bc.guide && bc.guide.exists && bc.guide.url);
            if (best) BOOK_STUDIES[bookId] = { href: _r(best), label: bookId };
          });
        }
        if (_readerUpdate) _readerUpdate();
      })
      .catch(function () {});
  }

  /* ── Load topics.json — fallback BOOK_STUDIES for books not in books-content ── */
  // INTENT: Provides backward-compatible BOOK_STUDIES entries from topics.json
  //   for any book with a t.book field. loadBooksContent() overrides these entries
  //   once books-content.json loads (it runs first in the init sequence).
  //   Sidebar subgroup DOM elements no longer exist, so this only builds state.
  // CHANGE? If topics.json is fully retired, remove this function and its call.
  // VERIFY: Remove books-content.json temporarily — reader banner for Hebrews
  //   still shows the study-guides/hebrews/ link from topics.json.
  function loadTopics() {
    fetch(_r('data/topics.json'))
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (topics) {
        topics.forEach(function (t) {
          var href = t.href ? _r(t.href) : _r('topics/' + t.slug + '/');
          if (t.book && !BOOK_STUDIES[t.book]) {
            BOOK_STUDIES[t.book] = { href: href, label: t.label };
          }
        });
        if (_readerUpdate) _readerUpdate();
      })
      .catch(function () {});
  }

  /* ── Tier-aware banner items ─────────────────────────────── */
  // INTENT: Returns an array of { label, href, icon } items for the reader study
  //   banner, choosing the most contextually useful tiers based on navigation state.
  //   ch===0 = book intro (show all tiers); ch>0 = chapter view (prefer deep dive).
  //   Falls back to the legacy BOOK_STUDIES single-link if _bookContent is absent.
  // CHANGE? If books-content.json adds new tiers or renames guide/deep_dive/
  //   commentary keys, update the bc field reads here. If reader.js adds a verse
  //   field to _readerNavState, add verse-level Tier 3 preference logic.
  // VERIFY: Reader at Romans intro (ch=0) → banner shows all available tiers.
  //   Reader at Romans 8 (ch=8) → banner shows "Deep dive" link to topics/romans/.
  //   Reader at Genesis 1 → banner is hidden (no content).
  function getBannerItems(bookId, ch) {
    if (!_bookContent || !_bookContent.books) {
      var legacy = BOOK_STUDIES[bookId];
      return legacy ? [{ label: 'Study resource', href: legacy.href, icon: '📖' }] : null;
    }
    var bc = _bookContent.books[bookId];
    if (!bc) return null;
    var items = [];
    if (ch === 0) {
      if (bc.deep_dive  && bc.deep_dive.exists)  items.push({ label: 'Deep Dive',   href: _r(bc.deep_dive.url),  icon: '⊕' });
      if (bc.guide      && bc.guide.exists)       items.push({ label: 'Study Guide', href: _r(bc.guide.url),      icon: '◎' });
      if (bc.commentary && bc.commentary.exists)  items.push({ label: 'Commentary',  href: _r(bc.commentary.url), icon: '❧' });
    } else {
      if (bc.commentary && bc.commentary.exists && bc.commentary.chapters_done.indexOf(ch) !== -1)
        items.push({ label: 'Verse commentary', href: _r(bc.commentary.url + '#ch-' + ch), icon: '❧' });
      else if (bc.deep_dive && bc.deep_dive.exists)
        items.push({ label: 'Deep dive',  href: _r(bc.deep_dive.url), icon: '⊕' });
      if (bc.guide && bc.guide.exists)
        items.push({ label: 'Study guide', href: _r(bc.guide.url), icon: '◎' });
    }
    return items.length ? items : null;
  }

  /* ── Reader: tier-aware study banner ─────────────────────── */
  // INTENT: Watches the reader's results container for any navigation (chapter
  //   render, book intro). On each change, reads window._readerNavState (set by
  //   reader.js) for current bookId+ch, calls getBannerItems() to pick the right
  //   tier links, and renders them. Multiple tiers render as links separated by ·.
  // CHANGE? If reader.js changes the _readerNavState shape (bookId, ch keys),
  //   update the destructuring below. If getBannerItems() signature changes, update
  //   the call here.
  // VERIFY: Reader on Romans 8 → banner shows "⊕ Deep dive" + "◎ Study guide".
  //   Reader on Genesis 1 → banner hidden. Navigate back to Romans → banner
  //   reappears without a page reload.
  function initReaderStudyLink() {
    var bookSel   = document.getElementById('reader-book-select');
    var resultsEl = document.getElementById('reader-results');
    if (!bookSel || !resultsEl) return;

    var banner = mk('div', 'reader-study-banner');
    banner.setAttribute('hidden', '');
    resultsEl.parentNode.insertBefore(banner, resultsEl);

    function update() {
      var state  = window._readerNavState;
      var bookId = (state && state.bookId) || bookSel.value;
      var ch     = (state && state.ch != null) ? state.ch : -1;
      var items  = getBannerItems(bookId, ch);
      if (items && items.length) {
        var html = '<span class="reader-study-banner__icon" aria-hidden="true">📖</span>' +
                   '<span class="reader-study-banner__text">Study resources:</span>';
        items.forEach(function (item, i) {
          if (i > 0) html += '<span class="reader-study-banner__sep" aria-hidden="true"> · </span>';
          html += '<a class="reader-study-banner__link" href="' + item.href + '">' +
                    item.icon + ' ' + item.label + '</a>';
        });
        banner.innerHTML = html;
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
  loadBooksContent();
  loadTopics();

})();
