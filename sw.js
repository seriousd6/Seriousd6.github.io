/* sw.js — Bible Study PWA service worker
 *
 * ── Cache strategy ─────────────────────────────────────────────────────────
 *   HTML pages       → network-first  (always fresh when online)
 *   CSS / JS / icons → cache-first    (APP_CACHE_V; bump to bust)
 *   JSON data files  → cache-first    in a PER-DATASET bucket (bsw-data-{seg}-{ver}),
 *                      so each dataset busts independently (see DATA_VERSIONS below).
 *
 * ── How to invalidate on deploy ───────────────────────────────────────────
 *   • Changed HTML / CSS / JS / icons   → bump APP_CACHE_V (e.g. v19 → v20)
 *   • Changed ONE dataset's JSON        → bump that dataset's entry in DATA_VERSIONS
 *                                         (e.g. commentary v1 → v2); other buckets survive
 *   • Changed many / unlisted datasets  → bump DATA_DEFAULT_V (clears all unlisted ones)
 *   • Emergency full reset              → bump APP_CACHE_V + every DATA_VERSIONS entry
 *   On activate, the current app shell + every still-current data bucket are kept; stale
 *   data buckets and any older bsw-* cache are deleted.
 *
 * ── Rollback procedure ────────────────────────────────────────────────────
 *   1. Revert the bad commit and redeploy.
 *   2. Bump APP_CACHE_V (and the affected DATA_VERSIONS entry if data changed).
 *   3. The F9 SW update toast prompts online users to reload; they get the
 *      reverted files immediately.  Offline users are unaffected until they
 *      come online and accept the update prompt.
 */

'use strict';

var APP_CACHE_V  = 'bsw-app-v186';  // bump when HTML/CSS/JS/icon changes

// ── Per-dataset data caches ────────────────────────────────────────────────
// A SINGLE global data cache meant every JSON tweak (e.g. one red-letter or commentary
// edit) evicted ALL cached data (~800 MB), forcing users to re-download every large book.
// Each top-level dataset under data/ now has its OWN versioned bucket: bsw-data-{seg}-{ver}.
// Bump ONLY the dataset whose JSON changed; unlisted datasets fall back to DATA_DEFAULT_V.
// A cached bucket is valid iff its version === the current version for its segment — the
// activate handler deletes only the mismatched ones, so a red-letter bump never touches the
// bible or commentary buckets. data/{dir}/… buckets by dir; root files (data/red-letter.json)
// bucket by filename stem.
// CHANGE? To invalidate one dataset, bump its entry below (or DATA_DEFAULT_V to clear all
//   unlisted ones). _dataSeg / _dataCacheForPath drive the fetch routing AND the offline-
//   download / precacheBible funcs — keep them consistent.
var DATA_DEFAULT_V = 'v1';
var DATA_VERSIONS = {
  bible: 'v1', commentary: 'v1', interlinear: 'v1', strongs: 'v1',
  crossrefs: 'v1', echoes: 'v1', parallels: 'v1', 'red-letter': 'v1',
  library: 'v1', biblepedia: 'v19', maps: 'v4', timeline: 'v1', study: 'v1',
  books: 'v1', dictionary: 'v1', smith: 'v1', hitchcock: 'v1', torrey: 'v1',
  grammar: 'v1', plans: 'v1', devotionals: 'v1', translation: 'v1', synthesis: 'v1'
};
function _dataSeg(path) {
  var m = path.match(/\/data\/([^\/?#]+)(\/|$)/);
  if (!m) return 'misc';
  return (m[2] === '/') ? m[1] : m[1].replace(/\.json$/, '');  // dir name, or root-file stem
}
function _dataVer(seg) { return DATA_VERSIONS[seg] || DATA_DEFAULT_V; }
function _dataCacheName(seg) { return 'bsw-data-' + seg + '-' + _dataVer(seg); }
function _dataCacheForPath(path) { return _dataCacheName(_dataSeg(path)); }
function _cacheForUrl(url) {
  var p; try { p = new URL(url, self.location.origin).pathname; } catch (e) { p = String(url); }
  return _dataCacheForPath(p);
}

// App shell: files cached immediately on install
var SHELL_URLS = [
  './',
  './index.html',
  './read/index.html',
  './search/index.html',
  './verse-study/index.html',
  './notes/index.html',
  './settings/index.html',
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
  './library/progress/index.html',
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
  './apocrypha/index.html',
  './church-history/index.html',
  './discipline/index.html',
  './history/index.html',
  './maps/timelapse/index.html',
  './progress/index.html',
  './reflections/index.html',
  './studies/index.html',
  './tracker/index.html',
  './worship/index.html',
  './offline.html',
  './memorize/index.html',
  './journal/index.html',
  './study-guides/index.html',
  './study-guides/hebrews/index.html',
  './study-guides/ephesians/index.html',
  './study-guides/romans-1-8/index.html',
  './study-guides/sermon-on-the-mount/index.html',
  './study-guides/psalms/index.html',
  // ── BUILD:ASSETS-START ────────────────────────────────────────────────────
  // JS/CSS precache list. In the committed source this is the literal dev tree;
  // tools/build-assets.mjs REGENERATES everything between these markers at build
  // time (bundled entries, hashed chunks, stable externals, minified CSS) and
  // stamps APP_CACHE_V with a content hash. Do not hand-edit between markers
  // except to keep the dev list in sync with new source files.
  './assets/css/style.css',
  './assets/css/bible-ui.css',
  './assets/css/daily.css',
  './assets/css/memorize.css',
  './assets/css/reader.css',
  './assets/css/verse-study.css',
  './assets/css/book-study.css',
  './assets/css/library.css',
  './assets/css/topic-guide.css',
  './assets/css/topic-shell.css',
  './assets/css/study-guide.css',
  './assets/css/study-nav.css',
  './assets/css/dictionary.css',
  './assets/css/timeline.css',
  './assets/css/maps.css',
  './assets/css/wordcloud.css',
  './assets/css/devotionals.css',
  './assets/css/apocrypha.css',
  './assets/css/discipline.css',
  './assets/css/lib-browser.css',
  './assets/css/lib-progress.css',
  './assets/css/lib-reader.css',
  './assets/css/ol-companion.css',
  './assets/css/timelapse.css',
  './assets/css/topical.css',
  './assets/js/core-boot.js',
  './assets/js/entries/generic.js',
  './assets/js/entries/home.js',
  './assets/js/entries/reader.js',
  './assets/js/entries/memorize.js',
  './assets/js/entries/biblepedia.js',
  './assets/js/entries/timeline.js',
  './assets/js/entries/church-history.js',
  './assets/js/entries/maps.js',
  './assets/js/entries/timelapse.js',
  './assets/js/entries/wordcloud.js',
  './assets/js/entries/lib-reader.js',
  './assets/js/entries/lib-browser.js',
  './assets/js/entries/lib-progress.js',
  './assets/js/entries/apocrypha.js',
  './assets/js/entries/settings.js',
  './assets/js/entries/search.js',
  './assets/js/core.js',
  './assets/js/storage.js',
  './assets/js/mem.js',
  './assets/js/tooltip.js',
  './assets/js/modal.js',
  './assets/js/wire.js',
  './assets/js/pwa.js',
  './assets/js/search.js',
  './assets/js/reader.js',
  './assets/js/reader-audio.js',
  './assets/js/study-desk.js',
  './assets/js/parallels.js',
  './assets/js/synoptic.js',
  './assets/js/biblepedia.js',
  './assets/js/interlinear.js',
  './assets/js/verse-study.js',
  './assets/js/daily.js',
  './assets/js/library.js',
  './assets/js/terms.js',
  './assets/js/sections.js',
  './assets/js/timeline.js',
  './assets/js/maps.js',
  './assets/js/wordcloud.js',
  './assets/js/main.js',
  './assets/js/settings.js',
  './assets/js/apocrypha-reader.js',
  './assets/js/lib-browser.js',
  './assets/js/lib-progress.js',
  './assets/js/lib-reader.js',
  './assets/js/ol-companion.js',
  './assets/js/places.js',
  './assets/js/sg-progress.js',
  './assets/js/store.js',
  './assets/js/sync.js',
  './assets/js/timelapse-map.js',
  './assets/js/tracker.js',
  './assets/css/workshop.css',
  './assets/js/workshop.js',
  // ── BUILD:ASSETS-END ──────────────────────────────────────────────────────
  './favicon.svg',
  './favicon.ico',
  './manifest.json',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './data/versions/versions.json',
  './data/apocrypha-books.json',
  './data/apocrypha-canon-orders.json',
  './data/topics.json',
  './data/topics-index.json',
  './data/bible/books.json',
  './data/votd/verses.json',
  './data/plans/bible-in-a-year.json',
  './data/plans/bible-in-a-year-chronological.json',
  './data/plans/mcheyne.json',
  './data/plans/nt-90-days.json',
  './data/plans/psalms-proverbs.json',
  './data/plans/gospels-30-days.json',
  './data/plans/heidelberg-weekly.json',
  './data/plans/wsc-quarterly.json',
  './data/devotionals/spurgeon-morning.json',
  './data/devotionals/spurgeon-evening.json',
  // Extended lexicons
  './data/strongs/bdb.json',
  './data/strongs/thayer.json',
  // Reference dictionaries & topical textbooks
  './data/dictionary/index.json',  // Easton's (parity with smith/index.json below)
  './data/smith/index.json',
  './data/hitchcock/index.json',
  './data/torrey/torrey.json',
  // Generic library full-screen reader (target of every "Open in reader" button)
  './library/read/index.html',
  // Standalone library pages (council/confession docs with inline HTML)
  './library/nicaea-i/index.html',
  './library/constantinople-i/index.html',
  './library/ephesus-431/index.html',
  './library/chalcedon-451/index.html',
  './library/orange-529/index.html',
  './library/smalcald-articles/index.html',
  './timeline/index.html',
  './maps/index.html',
  './wordcloud/index.html',
  './data/timeline/events.json',
  './data/timeline/detail.json',
  './data/maps/places.json',
  './data/maps/timelapse.json',
  './data/maps/regions.json',
  './data/maps/place-coords.json',
  './data/sections-index.json',
  './data/sections-aliases.json',
  './data/sections-body.json',
  './data/wordcloud/frequencies.json',
  // Translation Workshop (SW-A through SW-M) — added 2026-06-06
  './translation/workshop/index.html',
  // Grammar data (SW-B particles, morphSig; SW-C debates; SW-H cognates; SW-I semantic; SW-J author-freq)
  './data/grammar/greek-particles.json',
  './data/grammar/hebrew-particles.json',
  './data/grammar/greek-morphology-significance.json',
  './data/grammar/hebrew-morphology-significance.json',
  './data/grammar/grammar-debates.json',
  './data/grammar/cognate-families-greek.json',
  './data/grammar/cognate-families-hebrew.json',
  './data/grammar/cognate-index-greek.json',
  './data/grammar/cognate-index-hebrew.json',
  './data/grammar/author-freq-greek.json',
  './data/grammar/author-freq-hebrew.json',
  './data/grammar/semantic-fields-greek.json',
  './data/grammar/semantic-fields-hebrew.json',
  // Literary data (SW-D)
  './data/literary/genre.json',
  './data/literary/structures.json',
  './data/literary/devices-glossary.json',
  // Idiom data (SW-E)
  './data/idioms.json',
  './data/idioms-index.json',
  // Cultural background data (SW-F)
  './data/cultural/frameworks.json',
  './data/cultural/book-context.json',
  './data/cultural/symbols.json',
  // Second Temple context (SW-L)
  './data/second-temple/context.json',
  // OT-in-NT quotations (SW-K)
  './data/ot-in-nt/quotations.json',
];

// ── Install ────────────────────────────────────────────────────────────────
self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(APP_CACHE_V).then(function (cache) {
      return Promise.all(
        SHELL_URLS.map(function (url) {
          // cache:'reload' bypasses the HTTP cache so the new SW always
          // gets fresh files from the server, not stale copies from the
          // old SW's cache (which would defeat the version bump).
          return fetch(url, { cache: 'reload' }).then(function (r) {
            if (r.ok) return cache.put(url, r);
          }).catch(function () {});
        })
      );
    }).then(function () {
      return self.skipWaiting();
    })
  );
});

// ── Activate ───────────────────────────────────────────────────────────────
self.addEventListener('activate', function (e) {
  // Keep the current app shell and every per-dataset bucket whose version is still current;
  // delete stale-versioned data buckets and any other old bsw-* cache (incl. the pre-split
  // single global data cache). A foreign cache (not bsw-*) is left untouched.
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) {
        if (k === APP_CACHE_V) return null;                       // current app shell → keep
        var m = /^bsw-data-(.+)-(v\d+)$/.exec(k);
        if (m) return (m[2] === _dataVer(m[1])) ? null : caches.delete(k);  // data bucket: keep iff current
        if (k.indexOf('bsw-') === 0) return caches.delete(k);     // old app/global cache → delete
        return null;                                              // foreign cache → leave
      }));
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

  // Navigation (HTML) → network-first, app cache as fallback
  if (req.mode === 'navigate') {
    e.respondWith(networkFirst(req, APP_CACHE_V));
    return;
  }

  // JSON data files → cache-first in this dataset's own bucket (so a bump to one dataset
  // doesn't evict the others). _dataCacheForPath maps the URL to bsw-data-{seg}-{ver}.
  if (path.includes('/data/') || path.endsWith('.json')) {
    e.respondWith(cacheFirst(req, _dataCacheForPath(path)));
    return;
  }

  // App shell assets (CSS, JS, icons) → cache-first in APP_CACHE_V
  if (path.includes('/assets/') || path.endsWith('.css') || path.endsWith('.js') ||
      path.endsWith('.svg') || path.endsWith('.ico') || path.endsWith('.png')) {
    e.respondWith(cacheFirst(req, APP_CACHE_V));
    return;
  }
});

// INTENT: Network-first with cache fallback; serves offline.html if both fail.
//   ignoreSearch:true allows cached base URLs (e.g. /discipline/index.html) to match
//   navigations with query params (/discipline/?tab=journal) so SPA pages load offline.
// CHANGE? If a page needs distinct caches per query string (not this site's model), remove
//   ignoreSearch and cache the parameterized URL directly in SHELL_URLS instead.
// VERIFY: In DevTools Network → Offline, navigate to /discipline/?tab=journal — the
//   Discipline page should load from cache and show the Journal tab, not offline.html.
function networkFirst(req, cacheName) {
  return fetch(req).then(function (response) {
    if (response.ok) {
      var clone = response.clone();
      caches.open(cacheName).then(function (cache) { cache.put(req, clone); });
    }
    return response;
  }).catch(function () {
    return caches.match(req, { ignoreSearch: true }).then(function (cached) {
      if (cached) return cached;
      return caches.match('./offline.html').then(function (offlinePage) {
        return offlinePage || new Response('<h1>Offline</h1>', {
          headers: { 'Content-Type': 'text/html' }
        });
      });
    });
  });
}

// INTENT: Stale-while-revalidate — returns cached copy immediately if available, then
//   fetches a fresh copy in the background to update the cache for next time.
//   First-time requests have no cached copy so the network fetch is awaited directly.
// CHANGE? If a resource should never serve stale (e.g. a version manifest), use
//   networkFirst instead; changing here would affect all CSS/JS/JSON routing.
// VERIFY: Load /assets/js/core-boot.js, go offline in DevTools, reload — the file should
//   still load from cache with no network error in the console.
function cacheFirst(req, cacheName) {
  return caches.open(cacheName).then(function (cache) {
    return cache.match(req).then(function (cached) {
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

  // Settings → Offline: download or purge a named group's URL list, reporting
  // {group, done, total, phase} progress back to the requesting page.
  if (e.data.type === 'OFFLINE_DOWNLOAD') {
    offlineDownload(e.data, e.source);
  }
  if (e.data.type === 'OFFLINE_PURGE') {
    offlinePurge(e.data, e.source);
  }

  if (e.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

// INTENT: User-initiated offline store. Fetches/caches (or deletes) an explicit URL
//   list into its per-dataset bucket and streams progress to the Settings page. Unlike the
//   background precacheBible, this is foreground and explicit, so it uses a larger
//   chunk and no inter-chunk delay; failures are skipped (a 404 for a non-existent
//   commentary src×book combo is normal and must not abort the run).
// CHANGE? Message shape: {type:'OFFLINE_DOWNLOAD'|'OFFLINE_PURGE', group:string,
//   urls:string[]}. The Settings page (assets/js/settings.js) sends it and listens for
//   {type:'OFFLINE_PROGRESS', group, done, total, phase:'download'|'purge'|'done'}.
// VERIFY: Settings → Offline → Download "Maps & timeline"; the progress bar fills and
//   DevTools → Cache Storage → bsw-data-maps-* gains data/maps/*.json entries.
function _post(client, msg) {
  if (client && client.postMessage) { client.postMessage(msg); return; }
  // No direct sender (e.g. page sent via reg.active before controlling) — broadcast.
  self.clients.matchAll({ type: 'window' }).then(function (cs) {
    cs.forEach(function (c) { c.postMessage(msg); });
  });
}

function offlineDownload(data, client) {
  var urls = data.urls || [];
  var group = data.group || '';
  var total = urls.length, done = 0;
  // Each URL is stored in its own dataset bucket (_cacheForUrl) so it is served by the
  // cacheFirst routing and survives an unrelated dataset's version bump.
  var CHUNK = 16, i = 0;
  function next() {
    if (i >= urls.length) {
      _post(client, { type: 'OFFLINE_PROGRESS', group: group, done: done, total: total, phase: 'done' });
      return;
    }
    var slice = urls.slice(i, i + CHUNK); i += CHUNK;
    Promise.all(slice.map(function (url) {
      return caches.open(_cacheForUrl(url)).then(function (cache) {
        return cache.match(url).then(function (hit) {
          if (hit) return;
          return fetch(url).then(function (r) { if (r.ok) return cache.put(url, r.clone()); }).catch(function () {});
        });
      });
    })).then(function () {
      done += slice.length;
      _post(client, { type: 'OFFLINE_PROGRESS', group: group, done: done, total: total, phase: 'download' });
      setTimeout(next, 0);   // yield so foreground navigation stays responsive
    });
  }
  next();
}

function offlinePurge(data, client) {
  var urls = data.urls || [];
  var group = data.group || '';
  var total = urls.length, done = 0;
  var CHUNK = 64, i = 0;
  function next() {
    if (i >= urls.length) {
      _post(client, { type: 'OFFLINE_PROGRESS', group: group, done: done, total: total, phase: 'done' });
      return;
    }
    var slice = urls.slice(i, i + CHUNK); i += CHUNK;
    Promise.all(slice.map(function (url) {
      return caches.open(_cacheForUrl(url)).then(function (cache) { return cache.delete(url); });
    })).then(function () {
      done += slice.length;
      _post(client, { type: 'OFFLINE_PROGRESS', group: group, done: done, total: total, phase: 'purge' });
      setTimeout(next, 0);
    });
  }
  next();
}

// INTENT: Prefetches all Bible book JSON files for the given versions in the background
//   after the first page load, so subsequent offline reads don't require a network connection.
//   Chunks are fetched in groups of 6 (CHUNK) with 150 ms gaps to avoid saturating the
//   browser connection pool and competing with foreground navigation fetches.
// CHANGE? Expected message shape: { type: 'PRECACHE_BIBLE', base: string, books: string[],
//   versions: string[] }. Sent by pwa.js:initPWA after SW registration; if that call site
//   changes the message schema this function breaks silently (books/versions default to []).
// VERIFY: After first load in Chrome, open DevTools → Application → Cache Storage →
//   bsw-data-v3; entries for data/bible/KJV/Gen.json etc. should appear progressively.
function precacheBible(data) {
  var books    = data.books    || [];
  var versions = data.versions || [];
  var base     = (data.base    || './').replace(/\/?$/, '/');

  var urls = [];

  versions.forEach(function (ver) {
    books.forEach(function (bid) {
      urls.push(base + 'data/bible/' + ver + '/' + bid + '.json');
    });
  });

  // Crossrefs, interlinear, echoes, and Torrey verse-index: pre-cache fully.
  // echoes (~1.6 MB) and torrey/verse-index (~788 KB) power core verse-study
  // panels; without precaching they silently fail offline for unvisited books.
  ['crossrefs', 'interlinear', 'echoes', 'torrey/verse-index'].forEach(function (dir) {
    books.forEach(function (bid) {
      urls.push(base + 'data/' + dir + '/' + bid + '.json');
    });
  });

  // Commentary is ~74 MB across 330 files; excluded from auto pre-cache.
  // Each commentary file is cached on first access via the per-dataset cacheFirst
  // strategy, so offline support is preserved for books the user actually reads.

  urls.push(base + 'data/strongs/greek.json');
  urls.push(base + 'data/strongs/hebrew.json');

  books.forEach(function (bid) {
    urls.push(base + 'data/parallels/' + bid + '.json');
  });

  // Each precached file goes into its own dataset bucket (bible/crossrefs/interlinear/…)
  // via _cacheForUrl, matching the cacheFirst routing.
  {
    var CHUNK = 6;
    var i = 0;

    function nextChunk() {
      var slice = urls.slice(i, i + CHUNK);
      if (slice.length === 0) return;
      i += CHUNK;
      Promise.all(slice.map(function (url) {
        return caches.open(_cacheForUrl(url)).then(function (cache) {
          return cache.match(url).then(function (hit) {
            if (hit) return;
            return fetch(url).then(function (r) {
              if (r.ok) cache.put(url, r.clone());
            }).catch(function () {});
          });
        });
      })).then(function () {
        setTimeout(nextChunk, 150);
      });
    }

    nextChunk();
  }
}
