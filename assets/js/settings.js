/*
 * settings.js — Settings → Offline data manager.
 *
 * The site is lazy/light by default (only what you read is cached). This page lets a
 * user opt in to storing whole features for offline use, and purge them again to
 * reclaim space. Each feature group comes from data/offline-manifest.json (built by
 * scripts/build-offline-manifest.py); downloading/purging is delegated to the service
 * worker (sw.js OFFLINE_DOWNLOAD / OFFLINE_PURGE), which streams OFFLINE_PROGRESS back.
 *
 * INTENT: Keep all heavy fetching in the SW (one cache, survives navigation) and keep
 *   this file to UI + messaging. Per-group "downloaded" state is remembered in
 *   localStorage so the UI can show status without scanning thousands of cache entries.
 * CHANGE? Message contract with sw.js: send {type:'OFFLINE_DOWNLOAD'|'OFFLINE_PURGE',
 *   group, urls}; receive {type:'OFFLINE_PROGRESS', group, done, total, phase}. If the
 *   manifest group shape changes, update renderGroups().
 * VERIFY: Settings → Offline → Download "Maps & timeline" → bar fills to 100%, status
 *   becomes "Downloaded", storage-used figure rises; Remove returns it to "Not stored".
 */
(function () {
  'use strict';

  var MANIFEST_URL = '../data/offline-manifest.json';
  var LS_PREFIX = 'bsw_offline_';            // bsw_offline_{group} = '1' when stored
  var manifest = null;
  var busy = {};                             // group → true while in flight

  function $(id) { return document.getElementById(id); }
  function fmtBytes(b) {
    if (b >= 1073741824) return (b / 1073741824).toFixed(1) + ' GB';
    if (b >= 1048576) return (b / 1048576).toFixed(0) + ' MB';
    if (b >= 1024) return (b / 1024).toFixed(0) + ' KB';
    return b + ' B';
  }
  function isStored(id) { try { return localStorage.getItem(LS_PREFIX + id) === '1'; } catch (e) { return false; } }
  function setStored(id, v) { try { v ? localStorage.setItem(LS_PREFIX + id, '1') : localStorage.removeItem(LS_PREFIX + id); } catch (e) {} }

  // ── service worker plumbing ───────────────────────────────────────────────
  function swController() {
    return (navigator.serviceWorker && navigator.serviceWorker.controller) || null;
  }
  function sendSW(msg) {
    var c = swController();
    if (c) { c.postMessage(msg); return Promise.resolve(); }
    // Not yet controlled — fall back to the active registration.
    return navigator.serviceWorker.ready.then(function (reg) {
      if (reg.active) reg.active.postMessage(msg);
    });
  }

  var progressHandlers = {};   // group → fn(done,total,phase)
  if (navigator.serviceWorker) {
    navigator.serviceWorker.addEventListener('message', function (e) {
      var d = e.data || {};
      if (d.type !== 'OFFLINE_PROGRESS') return;
      var h = progressHandlers[d.group];
      if (h) h(d.done, d.total, d.phase);
    });
  }

  function runGroup(action, group, urls, onProgress) {
    return new Promise(function (resolve) {
      progressHandlers[group] = function (done, total, phase) {
        onProgress(done, total, phase);
        if (phase === 'done') { delete progressHandlers[group]; resolve(); }
      };
      sendSW({ type: action, group: group, urls: urls });
    });
  }

  // ── storage estimate ──────────────────────────────────────────────────────
  function refreshStorage() {
    if (!navigator.storage || !navigator.storage.estimate) return;
    navigator.storage.estimate().then(function (est) {
      var used = est.usage || 0, quota = est.quota || 0;
      $('set-storage').textContent = quota
        ? fmtBytes(used) + ' used of ~' + fmtBytes(quota) + ' available'
        : fmtBytes(used) + ' used';
    });
  }

  // ── rendering ─────────────────────────────────────────────────────────────
  function groupById(id) {
    return manifest.groups.filter(function (g) { return g.id === id; })[0];
  }

  function setStatus(id, text, cls) {
    var el = $('grp-status-' + id);
    if (el) { el.textContent = text; el.className = 'set-grp__status ' + (cls || ''); }
  }
  function setBar(id, pct) {
    var bar = $('grp-bar-' + id), wrap = $('grp-barwrap-' + id);
    if (wrap) wrap.style.display = pct == null ? 'none' : 'block';
    if (bar) bar.style.width = (pct || 0) + '%';
  }
  function refreshButtons(id) {
    var dl = $('grp-dl-' + id), rm = $('grp-rm-' + id);
    var b = !!busy[id], stored = isStored(id);
    if (dl) { dl.disabled = b || stored; dl.textContent = stored ? 'Stored' : 'Download'; }
    if (rm) { rm.disabled = b || !stored; }
  }

  function download(id) {
    var g = groupById(id);
    if (!g || busy[id]) return;
    busy[id] = true; refreshButtons(id);
    setStatus(id, 'Downloading…', 'set-grp__status--working'); setBar(id, 0);
    runGroup('OFFLINE_DOWNLOAD', id, g.files, function (done, total, phase) {
      setBar(id, total ? Math.round(done / total * 100) : 100);
    }).then(function () {
      busy[id] = false; setStored(id, true);
      setStatus(id, 'Downloaded', 'set-grp__status--done'); setBar(id, null);
      refreshButtons(id); refreshStorage();
    });
  }

  function purge(id) {
    var g = groupById(id);
    if (!g || busy[id]) return;
    busy[id] = true; refreshButtons(id);
    setStatus(id, 'Removing…', 'set-grp__status--working'); setBar(id, 0);
    runGroup('OFFLINE_PURGE', id, g.files, function (done, total, phase) {
      setBar(id, total ? Math.round(done / total * 100) : 100);
    }).then(function () {
      busy[id] = false; setStored(id, false);
      setStatus(id, 'Not stored', ''); setBar(id, null);
      refreshButtons(id); refreshStorage();
    });
  }

  function renderGroups() {
    var host = $('set-groups');
    host.innerHTML = '';
    manifest.groups.forEach(function (g) {
      if (!g.count) return;
      var stored = isStored(g.id);
      var card = document.createElement('div');
      card.className = 'set-grp';
      card.innerHTML =
        '<div class="set-grp__main">' +
          '<div class="set-grp__head">' +
            '<span class="set-grp__label">' + g.label + '</span>' +
            '<span class="set-grp__size">' + fmtBytes(g.bytes) + ' · ' + g.count + ' files</span>' +
          '</div>' +
          '<div class="set-grp__desc">' + g.desc + '</div>' +
          '<div class="set-grp__barwrap" id="grp-barwrap-' + g.id + '" style="display:none">' +
            '<div class="set-grp__bar" id="grp-bar-' + g.id + '"></div>' +
          '</div>' +
        '</div>' +
        '<div class="set-grp__side">' +
          '<span class="set-grp__status ' + (stored ? 'set-grp__status--done' : '') + '" id="grp-status-' + g.id + '">' +
            (stored ? 'Downloaded' : 'Not stored') + '</span>' +
          '<div class="set-grp__btns">' +
            '<button class="set-btn set-btn--dl" id="grp-dl-' + g.id + '" type="button">Download</button>' +
            '<button class="set-btn set-btn--rm" id="grp-rm-' + g.id + '" type="button">Remove</button>' +
          '</div>' +
        '</div>';
      host.appendChild(card);
      $('grp-dl-' + g.id).addEventListener('click', function () { download(g.id); });
      $('grp-rm-' + g.id).addEventListener('click', function () { purge(g.id); });
      refreshButtons(g.id);
    });
  }

  function totalBytes() { return manifest.groups.reduce(function (s, g) { return s + g.bytes; }, 0); }

  async function downloadAll() {
    for (var i = 0; i < manifest.groups.length; i++) {
      var g = manifest.groups[i];
      if (g.count && !isStored(g.id)) {
        await new Promise(function (res) {
          download(g.id);
          var iv = setInterval(function () { if (!busy[g.id]) { clearInterval(iv); res(); } }, 300);
        });
      }
    }
  }
  async function purgeAll() {
    for (var i = 0; i < manifest.groups.length; i++) {
      var g = manifest.groups[i];
      if (g.count && isStored(g.id)) {
        await new Promise(function (res) {
          purge(g.id);
          var iv = setInterval(function () { if (!busy[g.id]) { clearInterval(iv); res(); } }, 300);
        });
      }
    }
  }

  // ── init ──────────────────────────────────────────────────────────────────
  fetch(MANIFEST_URL).then(function (r) { return r.json(); }).then(function (m) {
    manifest = m;
    $('set-total').textContent = fmtBytes(totalBytes());
    renderGroups();
    refreshStorage();
    $('set-dl-all').addEventListener('click', function () {
      if (confirm('Download all features for offline use (' + fmtBytes(totalBytes()) + ')? This may take a while and use significant storage.')) downloadAll();
    });
    $('set-purge-all').addEventListener('click', function () {
      if (confirm('Remove all downloaded offline data?')) purgeAll();
    });
  }).catch(function () {
    $('set-groups').innerHTML = '<p class="set-err">Could not load the offline catalogue. Reload and try again.</p>';
  });

  if (!('serviceWorker' in navigator)) {
    var warn = $('set-nosw');
    if (warn) warn.style.display = 'block';
  }
})();
