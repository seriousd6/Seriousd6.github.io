/* sw.js — Bible Study PWA service worker
 *
 * Strategy:
 *   HTML pages       → network-first (always get updates when online)
 *   assets/data      → cache-first (static content; update in background)
 *   install          → pre-cache the app shell immediately
 *   message PRECACHE → background-download all Bible data in idle chunks
 */

'use strict';

var CACHE_VERSION = 'bsw-v15';

// App shell: files cached immediately on install
// These are the files needed to render any page offline.
var SHELL_URLS = [
  './',
  './index.html',
  './read/index.html',
  './search/index.html',
  './verse-study/index.html',
  './notes/index.html',
  './bookmarks/index.html',
  './compare/index.html',
  './topics/index.html',
  './topics/prayer/index.html',
  './topics/revelation/index.html',
  './topics/justification/index.html',
  './topics/holy-spirit/index.html',
  './topics/sermon-on-the-mount/index.html',
  './topics/romans/index.html',
  './topics/covenants/index.html',
  './topics/christology/index.html',
  './topics/psalms/index.html',
  './library/ignatius/index.html',
  './library/justin-martyr/index.html',
  './library/irenaeus/index.html',
  './library/tertullian/index.html',
  './library/athanasius/index.html',
  './library/chrysostom/index.html',
  './library/augustine/index.html',
  './library/gregory-nazianzus/index.html',
  './data/library/docs/ignatius.json',
  './data/library/docs/justin-martyr.json',
  './data/library/docs/irenaeus.json',
  './data/library/docs/tertullian.json',
  './data/library/docs/athanasius.json',
  './data/library/docs/chrysostom.json',
  './data/library/docs/augustine.json',
  './data/library/docs/gregory-nazianzus.json',
  './plans/index.html',
  './devotionals/index.html',
  './library/index.html',
  './data/library/index.json',
  './data/library/docs/apostles-creed.json',
  './data/library/docs/nicene-creed.json',
  './data/library/docs/athanasian-creed.json',
  './data/library/docs/heidelberg-catechism.json',
  './data/library/docs/belgic-confession.json',
  './data/library/docs/canons-of-dort.json',
  './data/library/docs/westminster-confession.json',
  './data/library/docs/westminster-shorter-catechism.json',
  './data/library/docs/westminster-larger-catechism.json',
  './data/library/docs/london-baptist-confession.json',
  './data/library/docs/augsburg-confession.json',
  './data/library/docs/39-articles.json',
  './library/apostles-creed/index.html',
  './library/nicene-creed/index.html',
  './library/athanasian-creed/index.html',
  './library/heidelberg-catechism/index.html',
  './library/westminster-confession/index.html',
  './library/westminster-shorter-catechism/index.html',
  './library/westminster-larger-catechism/index.html',
  './library/belgic-confession/index.html',
  './library/canons-of-dort/index.html',
  './library/london-baptist-confession/index.html',
  './library/augsburg-confession/index.html',
  './library/39-articles/index.html',
  './word/index.html',
  './dictionary/index.html',
  './offline.html',
  './assets/css/style.css',
  './assets/css/bible-ui.css',
  './assets/css/daily.css',
  './assets/css/memorize.css',
  './assets/css/topical.css',
  './assets/css/reader.css',
  './assets/css/verse-study.css',
  './assets/css/book-study.css',
  './assets/css/library.css',
  './assets/css/topic-guide.css',
  './assets/css/topic-shell.css',
  './assets/css/study-nav.css',
  './assets/css/word.css',
  './assets/css/dictionary.css',
  './assets/css/devotionals.css',
  './memorize/index.html',
  './topical/index.html',
  './assets/js/bible.js',
  './assets/js/main.js',
  './favicon.svg',
  './favicon.ico',
  './manifest.json',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './data/versions/versions.json',
  './data/bible/books.json',
  './data/votd/verses.json',
  './data/plans/bible-in-a-year.json',
  './data/plans/bible-in-a-year-chronological.json',
  './data/plans/mcheyne.json',
  './data/plans/nt-90-days.json',
  './data/plans/psalms-proverbs.json',
  './data/plans/gospels-30-days.json',
  './data/devotionals/spurgeon-morning.json',
  './data/devotionals/spurgeon-evening.json',
];

// ── Install ────────────────────────────────────────────────────────────────
self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE_VERSION).then(function (cache) {
      // Cache each shell URL individually so one failure doesn't abort the rest
      return Promise.all(
        SHELL_URLS.map(function (url) {
          return fetch(url).then(function (r) {
            if (r.ok) return cache.put(url, r);
          }).catch(function () {
            // Some pages may genuinely not exist yet — skip them silently
          });
        })
      );
    }).then(function () {
      return self.skipWaiting();
    })
  );
});

// ── Activate ───────────────────────────────────────────────────────────────
self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.filter(function (k) { return k !== CACHE_VERSION; })
          .map(function (k) { return caches.delete(k); })
      );
    }).then(function () {
      return self.clients.claim();
    })
  );
});

// ── Fetch ──────────────────────────────────────────────────────────────────
self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;

  var url;
  try { url = new URL(req.url); } catch (err) { return; }
  if (url.origin !== self.location.origin) return;

  var path = url.pathname;

  // Navigation (HTML) → network-first, cache as fallback
  if (req.mode === 'navigate') {
    e.respondWith(networkFirst(req));
    return;
  }

  // Data files and assets → cache-first, network fallback + background update
  if (path.includes('/data/') || path.includes('/assets/') ||
      path.endsWith('.css') || path.endsWith('.js') ||
      path.endsWith('.json') || path.endsWith('.svg') || path.endsWith('.ico')) {
    e.respondWith(cacheFirst(req));
    return;
  }
});

function networkFirst(req) {
  return fetch(req).then(function (response) {
    if (response.ok) {
      var clone = response.clone();
      caches.open(CACHE_VERSION).then(function (cache) { cache.put(req, clone); });
    }
    return response;
  }).catch(function () {
    return caches.match(req).then(function (cached) {
      if (cached) return cached;
      return caches.match('./offline.html').then(function (offlinePage) {
        return offlinePage || new Response('<h1>Offline</h1>', {
          headers: { 'Content-Type': 'text/html' }
        });
      });
    });
  });
}

function cacheFirst(req) {
  return caches.open(CACHE_VERSION).then(function (cache) {
    return cache.match(req).then(function (cached) {
      // Serve from cache immediately; fetch + update in background
      var networkFetch = fetch(req).then(function (response) {
        if (response.ok) cache.put(req, response.clone());
        return response;
      }).catch(function () { return cached; });

      return cached || networkFetch;
    });
  });
}

// ── Background pre-cache (triggered by page after first load) ──────────────
self.addEventListener('message', function (e) {
  if (!e.data) return;

  if (e.data.type === 'PRECACHE_BIBLE') {
    precacheBible(e.data);
  }

  if (e.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

function precacheBible(data) {
  var books    = data.books    || [];
  var versions = data.versions || [];
  var base     = (data.base    || './').replace(/\/?$/, '/');

  var urls = [];

  // Per-version Bible text (the largest dataset)
  versions.forEach(function (ver) {
    books.forEach(function (bid) {
      urls.push(base + 'data/bible/' + ver + '/' + bid + '.json');
    });
  });

  // Supporting per-book data (mhcc = flat path; others in subdirs)
  ['crossrefs', 'interlinear'].forEach(function (dir) {
    books.forEach(function (bid) {
      urls.push(base + 'data/' + dir + '/' + bid + '.json');
    });
  });
  // MHC (legacy flat path) + additional commentaries
  var commSources = ['', 'jfb', 'clarke', 'calvin', 'barnes'];
  commSources.forEach(function (src) {
    var prefix = src ? 'data/commentary/' + src + '/' : 'data/commentary/';
    books.forEach(function (bid) {
      urls.push(base + prefix + bid + '.json');
    });
  });

  // Strong's dictionaries
  urls.push(base + 'data/strongs/greek.json');
  urls.push(base + 'data/strongs/hebrew.json');

  // Parallels (not all books have data — failures are silently ignored)
  books.forEach(function (bid) {
    urls.push(base + 'data/parallels/' + bid + '.json');
  });

  caches.open(CACHE_VERSION).then(function (cache) {
    var CHUNK = 6;
    var i = 0;

    function nextChunk() {
      var slice = urls.slice(i, i + CHUNK);
      if (slice.length === 0) return;
      i += CHUNK;
      Promise.all(slice.map(function (url) {
        return cache.match(url).then(function (hit) {
          if (hit) return; // already cached — skip
          return fetch(url).then(function (r) {
            if (r.ok) cache.put(url, r.clone());
          }).catch(function () {});
        });
      })).then(function () {
        // Yield between chunks so the SW doesn't block other requests
        setTimeout(nextChunk, 150);
      });
    }

    nextChunk();
  });
}
