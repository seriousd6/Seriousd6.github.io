/* pwa.js — Service Worker registration, PWA manifest injection, onboarding, SW update toast */
'use strict';

import { _resolve, SW_URL, MANIFEST_URL, SITE_ROOT, READER_URL, escHtml, metaBooks, metaVersions } from './core.js';

export function _initOnboarding() {
  if (localStorage.getItem('bsw_onboarded')) return;
  var overlay = document.createElement('div');
  overlay.className = 'bsw-onboard-overlay';
  var readerUrl  = READER_URL;
  var vsUrl      = _resolve('../../read/?study=1');   // SD-T5: verse study lives in the reader's study desk
  var libraryUrl = _resolve('../../library/');
  var memUrl     = _resolve('../../memorize/');
  overlay.innerHTML =
    '<div class="bsw-onboard-card">' +
      '<h2 class="bsw-onboard-title">Welcome to Kingdom Bible Study</h2>' +
      '<p class="bsw-onboard-sub">A personal offline Bible tool — no account needed, everything saved in your browser.</p>' +
      '<div class="bsw-onboard-features">' +
        '<a class="bsw-onboard-feature" href="' + escHtml(readerUrl) + '">' +
          '<span class="bsw-onboard-icon"><svg class=\"bsw-onboard-svg\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" aria-hidden=\"true\"><path d=\"M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15.5H6.5A2.5 2.5 0 0 0 4 21z\"/><path d=\"M4 18.5A2.5 2.5 0 0 1 6.5 16H20\"/></svg></span>' +
          '<div><strong>Bible Reader</strong><p>Any passage across multiple translations, with cross-references and commentary.</p></div>' +
        '</a>' +
        '<a class="bsw-onboard-feature" href="' + escHtml(vsUrl) + '">' +
          '<span class="bsw-onboard-icon"><svg class=\"bsw-onboard-svg\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" aria-hidden=\"true\"><circle cx=\"11\" cy=\"11\" r=\"6\"/><path d=\"M20 20l-4.5-4.5\"/></svg></span>' +
          '<div><strong>Verse Study</strong><p>Deep-dive any verse: Strong\'s lexicon, interlinear, parallel passages, and more.</p></div>' +
        '</a>' +
        '<a class="bsw-onboard-feature" href="' + escHtml(libraryUrl) + '">' +
          '<span class="bsw-onboard-icon"><svg class=\"bsw-onboard-svg\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" aria-hidden=\"true\"><path d=\"M5 21V5a2 2 0 0 1 2-2h3v18zM10 21V3h4v18zM14 21l3.5-17.5L21 4l-3 17z\"/></svg></span>' +
          '<div><strong>Library</strong><p>Historic confessions and catechisms — Westminster, Heidelberg, Nicene Creed, and more.</p></div>' +
        '</a>' +
        '<a class="bsw-onboard-feature" href="' + escHtml(memUrl) + '">' +
          '<span class="bsw-onboard-icon"><svg class=\"bsw-onboard-svg\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" aria-hidden=\"true\"><path d=\"M12 3l2.7 5.7 6.3.8-4.6 4.3 1.2 6.2-5.6-3.1-5.6 3.1 1.2-6.2L3 9.5l6.3-.8z\"/></svg></span>' +
          '<div><strong>Scripture Memory</strong><p>Spaced-repetition flashcards to memorize Bible verses at your own pace.</p></div>' +
        '</a>' +
      '</div>' +
      '<div class="bsw-onboard-actions">' +
        '<a class="bsw-onboard-tour" id="bsw-onboard-tour" href="' + escHtml(_resolve('../../tour/')) + '">See everything on one verse &#x2192;</a>' +
        '<button class="bsw-onboard-btn" id="bsw-onboard-start">Get started</button>' +
      '</div>' +
    '</div>';
  document.body.appendChild(overlay);
  var dismiss = function () {
    localStorage.setItem('bsw_onboarded', '1');
    overlay.remove();
  };
  overlay.querySelector('#bsw-onboard-start').addEventListener('click', dismiss);
  // The tour link navigates; just mark onboarding done so it doesn't reappear.
  overlay.querySelector('#bsw-onboard-tour').addEventListener('click', function () {
    localStorage.setItem('bsw_onboarded', '1');
  });
  overlay.addEventListener('click', function (e) { if (e.target === overlay) dismiss(); });
  document.addEventListener('keydown', function onKey(e) {
    if (e.key === 'Escape') { dismiss(); document.removeEventListener('keydown', onKey); }
  });
}

export function initPWA() {
  if (!document.querySelector('link[rel="manifest"]')) {
    var link = document.createElement('link');
    link.rel  = 'manifest';
    link.href = MANIFEST_URL;
    document.head.appendChild(link);
  }
  if (!document.querySelector('meta[name="theme-color"]')) {
    var meta = document.createElement('meta');
    meta.name    = 'theme-color';
    meta.content = '#5c3d1e';
    document.head.appendChild(meta);
    // INTENT: Inject a second theme-color meta for dark mode so the browser address bar /
    //   PWA title bar reflects the dark palette when the user's OS is in dark mode.
    //   The manifest spec has no media-query support so the splash-screen color remains
    //   the light-mode value; only the browser chrome is corrected here.
    // CHANGE? If the dark background color changes in style.css :root[data-theme="dark"],
    //   update the content value below to match (currently --color-bg: #1a1208).
    // VERIFY: In Chrome DevTools → Application → Manifest, two theme-color entries should
    //   appear (light and dark). On an Android device in dark mode, the PWA title bar
    //   should appear as dark brown rather than warm medium-brown.
    var metaDark = document.createElement('meta');
    metaDark.name    = 'theme-color';
    metaDark.content = '#3a2008';
    metaDark.setAttribute('media', '(prefers-color-scheme: dark)');
    document.head.appendChild(metaDark);
  }
  // INTENT: iOS Safari does not use the manifest for home-screen icons; it requires
  //   an explicit apple-touch-icon link in the document head. Injecting here once
  //   covers all pages via the shared initPWA() call in app.js.
  // CHANGE? If the icon path changes, update ./assets/icon-192.png in sw.js SHELL_URLS too.
  // VERIFY: On iOS Safari, "Add to Home Screen" should show the cross/book icon, not a webpage screenshot.
  if (!document.querySelector('link[rel="apple-touch-icon"]')) {
    var touchIcon = document.createElement('link');
    touchIcon.rel  = 'apple-touch-icon';
    touchIcon.href = _resolve('../../assets/icon-192.png');
    document.head.appendChild(touchIcon);
  }

  if (!('serviceWorker' in navigator)) return;

  navigator.serviceWorker.register(SW_URL).then(function (reg) {
    // INTENT: Send only versions that have actual data/bible/{id}/ files; stubs (stub:true),
    //   apocrypha group, and tier-3 MKT versions have no book JSON files and would each
    //   fire 66 silent 404 requests during background precache.
    // CHANGE? If data files are added for a stub version, remove its "stub":true field in
    //   data/versions/versions.json and it will automatically be included here.
    // VERIFY: After first page load, open DevTools Application → Cache Storage → bsw-data-bible-*;
    //   no data/bible/DR/, data/bible/MKT-L/, or data/bible/AKJV/ entries should appear.
    function triggerPrecache(sw) {
      if (!sw || !metaBooks || !metaVersions) return;
      sw.postMessage({
        type:     'PRECACHE_BIBLE',
        base:     SITE_ROOT,
        books:    metaBooks.map(function (b) { return b.id; }),
        versions: metaVersions
          .filter(function (v) { return !v.stub && !v.group && v.tier < 3; })
          .map(function (v) { return v.id; })
      });
    }

    if (reg.active) {
      triggerPrecache(reg.active);
    } else {
      navigator.serviceWorker.ready.then(function (r) { triggerPrecache(r.active); });
    }

    reg.addEventListener('updatefound', function () {
      var incoming = reg.installing;
      incoming.addEventListener('statechange', function () {
        if (incoming.state === 'installed' && navigator.serviceWorker.controller) {
          _showSWUpdateToast(reg);
        }
      });
    });
  }).catch(function (err) {
    console.warn('[BibleUI] SW registration failed:', err);
  });
}

function _showSWUpdateToast(reg) {
  var toast = document.getElementById('bsw-sw-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id        = 'bsw-sw-toast';
    toast.className = 'bsw-sw-toast';
    toast.innerHTML =
      '<span class="bsw-sw-toast__msg">A new version is available.</span>' +
      '<button class="bsw-sw-toast__btn" id="bsw-sw-reload">Reload</button>' +
      '<button class="bsw-sw-toast__dismiss" aria-label="Dismiss">&#x2715;</button>';
    document.body.appendChild(toast);
    toast.querySelector('.bsw-sw-toast__dismiss').addEventListener('click', function () {
      toast.hidden = true;
    });
  }
  toast.hidden = false;
  toast.querySelector('#bsw-sw-reload').onclick = function () {
    if (reg.waiting) reg.waiting.postMessage({ type: 'SKIP_WAITING' });
    navigator.serviceWorker.addEventListener('controllerchange', function () {
      window.location.reload();
    });
  };
  setTimeout(function () { if (toast) toast.hidden = true; }, 30000);
}
