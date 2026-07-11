/**
 * main.js — wires the statically-rendered left sidebar navigation.
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

  /* ── Shared hub-tab helper ────────────────────────────────── */
  // INTENT: Lazy-load a hub-tab iframe the first time its panel is shown — copy
  //   data-src→src exactly once. The History, Discipline, and Explore/Search tab
  //   controllers each used to re-implement this same 3-line reveal; this is the one
  //   copy. main.js loads (classic script) before those inline/module scripts, so the
  //   global is available to all three.
  // CHANGE? Callers that need an error fallback or a load hook attach their own
  //   listeners to the iframe (e.g. History adds a "could not load" message + a Leaflet
  //   resize on load). Keep the getAttribute('src') check — it is null when the src
  //   attribute is absent, which is more robust than reading the .src property ("about:blank").
  // VERIFY: Open History / Discipline / Explore tabs; each panel's iframe issues exactly
  //   one network request on first activation and is not refetched when re-selected.
  window.bswRevealFrame = function (iframe) {
    if (iframe && !iframe.getAttribute('src') && iframe.dataset && iframe.dataset.src) {
      iframe.src = iframe.dataset.src;
      return true;
    }
    return false;
  };

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

  // Nav data now lives in src/components/Sidebar.astro (statically rendered).

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

  /* ── Wire sidebar ─────────────────────────────────────────── */
  // The sidebar DOM is now rendered statically at build time by
  // src/components/Sidebar.astro (same markup buildSidebar() used to create).
  // This function only WIRES it: active-link marking (runtime because ?tab=
  // query links decide it), group toggles, collapse/overlay/mobile behavior,
  // theme button, and skip-link focus. Body state classes (sidebar-collapsed /
  // sidebar-overlay / is-embedded) are applied pre-paint by the inline
  // bootstrap in src/layouts/Base.astro; this re-applies them as a fallback
  // for any cached page that predates the bootstrap.
  // CHANGE? Selector contract with Sidebar.astro: #site-sidebar,
  //   .sb-collapse-btn, .sidebar-tab, .mobile-topbar__hamburger,
  //   .sidebar-backdrop, #bsw-theme-btn, .sb-group > .sb-group-btn +
  //   .sb-group-items. Keep both files in sync.
  // VERIFY: Sidebar visible with correct active link on load; collapse state
  //   persists across reloads; hamburger works < 1024px; hub-tab iframes
  //   (History/Discipline/Explore) show no sidebar inside the frame.
  function wireSidebar() {
    // Embedded as a hub "tab" (iframe or ?minimal=1): suppress all chrome.
    // The Base.astro bootstrap already added sidebar-collapsed + is-embedded
    // pre-paint (CSS hides the chrome); this fallback covers cached pages and
    // also reveals the per-page "← back to hub" links.
    var framed;
    try { framed = (window.self !== window.top); }
    catch (e) { framed = true; }  // cross-origin parent throws → definitely embedded
    if (framed || new URLSearchParams(location.search).get('minimal')) {
      document.body.classList.add('sidebar-collapsed');
      document.body.classList.add('is-embedded');
      document.querySelectorAll(
        '.hist-back-link, .prog-back-link, .ms-back-link, #trk-back-link'
      ).forEach(function (el) { el.hidden = false; });
      return;
    }

    var sidebar = document.getElementById('site-sidebar');
    if (!sidebar) return; // page ships without the static sidebar

    var colBtn    = sidebar.querySelector('.sb-collapse-btn');
    var tab       = document.querySelector('.sidebar-tab');
    var hamburger = document.querySelector('.mobile-topbar__hamburger');
    var backdrop  = document.querySelector('.sidebar-backdrop');
    if (!colBtn || !tab || !hamburger || !backdrop) return;

    /* ── Active-link marking ── */
    // Done at runtime (not build time) because hrefs like history/?tab=church
    // are active only for a matching query string.
    Array.prototype.forEach.call(sidebar.querySelectorAll('a[href]'), function (a) {
      if (isActive(a.href)) {
        a.setAttribute('aria-current', 'page');
        if (a.classList.contains('sb-group-btn')) a.classList.add('is-active');
      }
    });

    /* ── Expand the group containing the active page ── */
    Array.prototype.forEach.call(sidebar.querySelectorAll('.sb-group'), function (group) {
      var btn   = group.querySelector('.sb-group-btn');
      var items = group.querySelector('.sb-group-items');
      if (!btn || !items) return;
      var active = false;
      Array.prototype.forEach.call(items.querySelectorAll('a[href]'), function (a) {
        if (isActive(a.href) || isAncestor(a.href)) active = true;
      });
      if (active) {
        btn.setAttribute('aria-expanded', 'true');
        btn.classList.add('is-active');
        items.removeAttribute('hidden');
      }
      btn.addEventListener('click', function () {
        var open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', open ? 'false' : 'true');
        if (open) { items.setAttribute('hidden', ''); }
        else      { items.removeAttribute('hidden'); }
      });
    });

    /* ── Theme toggle ── */
    var themeBtn = document.getElementById('bsw-theme-btn');
    function _isDark() {
      var th = document.documentElement.getAttribute('data-theme');
      if (th) return th === 'dark';
      return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
    function _updateThemeLabel() {
      if (themeBtn) themeBtn.textContent = _isDark() ? '☀ Light Mode' : '🌙 Dark Mode';
    }
    _updateThemeLabel();
    if (themeBtn) {
      themeBtn.addEventListener('click', function () {
        var next = _isDark() ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        try { localStorage.setItem('bsw_theme', next); } catch (e) {}
        _updateThemeLabel();
      });
    }

    /* ── Skip link (AUD-27, WCAG 2.4.1): point it at <main> and move focus ── */
    var main = document.querySelector('main');
    var skip = document.querySelector('.skip-link');
    if (main && skip) {
      if (!main.id) main.id = 'main-content';
      main.setAttribute('tabindex', '-1');
      skip.href = '#' + main.id;
      skip.addEventListener('click', function () {
        setTimeout(function () { main.focus(); }, 0);
      });
    }

    /* ── Initial collapse/overlay state ── */
    // Fallback for cached pages without the pre-paint bootstrap; harmless
    // re-add when the bootstrap already ran.
    if (_isTopicPage) {
      document.body.classList.add('sidebar-overlay');
    } else if (getState() === 'collapsed') {
      document.body.classList.add('sidebar-collapsed');
    }

    /* ── Event helpers ── */
    function isMobile() { return window.innerWidth < 1024; }

    function setCollapseArrow(collapsed) {
      var c = collapsed ? '&#x203A;' : '&#x2039;';
      tab.innerHTML    = c;
      colBtn.innerHTML = c;
      colBtn.setAttribute('aria-label', collapsed ? 'Expand sidebar' : 'Collapse sidebar');
    }

    // Sync arrow glyphs with whatever state the bootstrap applied.
    setCollapseArrow(
      document.body.classList.contains('sidebar-collapsed') ||
      (document.body.classList.contains('sidebar-overlay') && !document.body.classList.contains('sb-open'))
    );

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

  wireSidebar();
  initReaderStudyLink();
  loadBooksContent();
  loadTopics();

})();
