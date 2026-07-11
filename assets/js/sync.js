/* sync.js — Google Drive backup & restore for user study data (settings page).
 *
 * Entirely client-side: the browser talks directly to Google Identity Services
 * (GIS) and the Drive REST API — no server component, matching the static
 * GitHub Pages deployment. Backups live in the app-data folder of the USER'S
 * own Google Drive ('appDataFolder'), a private per-app area that never shows
 * up in their normal Drive file list and that this app alone can read.
 *
 * Public API:
 *   initSyncSection() — no-op unless the page contains #sync-section
 *                       (currently only settings/index).
 */
'use strict';

// ── Configuration ──────────────────────────────────────────────────────────
// GOOGLE_CLIENT_ID — one-time setup by the site owner:
//   1. At https://console.cloud.google.com/apis/credentials create an
//      OAuth 2.0 Client ID of type "Web application".
//   2. Add BOTH authorized JavaScript origins:
//        https://kingdombiblestudy.com
//        http://localhost:4321
//      No redirect URIs are needed — the GIS token flow doesn't use them.
//   3. In the same Google Cloud project, enable the Google Drive API
//      (APIs & Services → Library → "Google Drive API" → Enable).
//   4. Paste the client ID (ends in .apps.googleusercontent.com) below.
// While this is empty, the Sync & Backup section renders a "not configured"
// note instead of the connect UI, so shipping it blank is harmless.
var GOOGLE_CLIENT_ID = '';

var SYNC_STATE_KEY  = 'bsw_sync_state';   // { connected, lastBackupAt, lastHash }
var BACKUP_FILENAME = 'kbs-backup.json';
var DRIVE_SCOPE     = 'https://www.googleapis.com/auth/drive.appdata';
var GIS_SRC         = 'https://accounts.google.com/gsi/client';
var DRIVE_API       = 'https://www.googleapis.com/drive/v3';
var DRIVE_UPLOAD    = 'https://www.googleapis.com/upload/drive/v3';

// ── Module state ───────────────────────────────────────────────────────────
var _body           = null;   // container div the UI renders into
var _tokenClient    = null;   // GIS token client (created once after GIS loads)
var _tokenCb        = null;   // per-request success callback for the token client
var _tokenErrCb     = null;   // per-request error callback for the token client
var _accessToken    = null;   // OAuth access token — in-memory ONLY, never persisted
var _tokenExpiresAt = 0;      // epoch ms after which _accessToken is considered stale
var _fileId         = null;   // Drive file id of kbs-backup.json once discovered
var _gisLoadPromise = null;   // dedupe guard so the GIS <script> is injected once
var _autoBackupDone = false;  // auto-backup fires at most once per page load
var _busy           = false;  // guards against overlapping backup/restore clicks

// ── bsw_sync_state helpers ─────────────────────────────────────────────────
function _getSyncState() {
  try { return JSON.parse(localStorage.getItem(SYNC_STATE_KEY) || '{}'); }
  catch (e) { return {}; }
}
function _patchSyncState(patch) {
  var s = _getSyncState();
  Object.keys(patch).forEach(function (k) { s[k] = patch[k]; });
  try { localStorage.setItem(SYNC_STATE_KEY, JSON.stringify(s)); } catch (e) {}
}

// ── Snapshot ───────────────────────────────────────────────────────────────
// INTENT: Capture every user-data localStorage key (bsw_* prefix) as its RAW
//   string value — no JSON.parse round-trip — so restore is a byte-exact
//   setItem replay and unknown/future keys survive without schema knowledge.
//   SYNC_STATE_KEY is excluded: it is per-device sync bookkeeping and copying
//   it between devices would corrupt their change-detection hashes.
// CHANGE? If a user-data key is ever created WITHOUT the bsw_ prefix it will
//   silently be missing from Drive backups — keep new keys on the prefix
//   (see STORE_KEYS / STORE_PREFIXES in store.js, all bsw_*).
// VERIFY: In the console run localStorage, then compare against the uploaded
//   kbs-backup.json (Back up now → download via Drive API explorer): every
//   bsw_* key except bsw_sync_state should appear under .data verbatim.
function _buildSnapshot() {
  var data = {};
  try {
    for (var i = 0; i < localStorage.length; i++) {
      var k = localStorage.key(i);
      if (!k || k.indexOf('bsw_') !== 0 || k === SYNC_STATE_KEY) continue;
      data[k] = localStorage.getItem(k);
    }
  } catch (e) { /* storage unavailable — snapshot stays empty */ }
  return {
    savedAt: new Date().toISOString(),
    origin:  location.hostname,
    data:    data
  };
}

// INTENT: Cheap deterministic fingerprint of snapshot *data* (savedAt/origin
//   excluded — they change on every call) so auto-backup can tell "nothing
//   changed since last upload" without storing the whole serialized snapshot
//   in bsw_sync_state. Keys are sorted because localStorage enumeration order
//   is unspecified across browsers.
// CHANGE? Changing the hash algorithm invalidates every stored lastHash and
//   causes exactly one redundant auto-backup per device — harmless.
// VERIFY: Call twice with untouched data → identical string; edit any note
//   and call again → different string.
function _snapshotHash(snap) {
  var keys = Object.keys(snap.data).sort();
  var str  = keys.map(function (k) { return k + '\u0000' + snap.data[k]; }).join('\u0001');
  var h = 5381; // djb2
  for (var i = 0; i < str.length; i++) {
    h = ((h << 5) + h + str.charCodeAt(i)) | 0;
  }
  return String(h) + ':' + str.length;
}

// ── Google Identity Services (GIS) ─────────────────────────────────────────
function _loadGis() {
  if (_gisLoadPromise) return _gisLoadPromise;
  _gisLoadPromise = new Promise(function (resolve, reject) {
    if (window.google && window.google.accounts && window.google.accounts.oauth2) {
      resolve();
      return;
    }
    var s = document.createElement('script');
    s.src   = GIS_SRC;
    s.async = true;
    s.defer = true;
    s.onload  = function () { resolve(); };
    s.onerror = function () {
      _gisLoadPromise = null; // allow a retry on the next user action
      reject(new Error('Could not load the Google sign-in script (offline?)'));
    };
    document.head.appendChild(s);
  });
  return _gisLoadPromise;
}

// INTENT: Acquire an OAuth access token via the GIS token model. promptMode:
//   null  → user-initiated connect: Google decides whether to show consent.
//   ''    → silent-ish re-auth for returning visits / expired tokens: succeeds
//           without interaction when the user has an active Google session and
//           prior consent; otherwise error_callback fires (e.g. the browser
//           blocks the non-gesture popup) and the caller falls back to the
//           signed-out UI rather than spamming popups.
//   Tokens are held in module memory only — never written to storage — so a
//   shared computer never leaks Drive access via localStorage.
// CHANGE? The success/error callbacks are swapped per request via _tokenCb /
//   _tokenErrCb because initTokenClient() only accepts them at creation time.
//   Don't call initTokenClient more than once per page — GIS warns and leaks.
// VERIFY: With a configured client ID, click Connect → Google popup →
//   approve → status shows "Checking Drive…"; reload the page → reconnects
//   without a consent screen (active session), or shows signed-out quietly.
function _requestToken(promptMode) {
  return _loadGis().then(function () {
    return new Promise(function (resolve, reject) {
      var oauth2 = window.google.accounts.oauth2;
      if (!_tokenClient) {
        _tokenClient = oauth2.initTokenClient({
          client_id: GOOGLE_CLIENT_ID,
          scope:     DRIVE_SCOPE,
          callback:       function (resp) { if (_tokenCb)    _tokenCb(resp);   },
          error_callback: function (err)  { if (_tokenErrCb) _tokenErrCb(err); }
        });
      }
      _tokenCb = function (resp) {
        _tokenCb = _tokenErrCb = null;
        if (resp && resp.access_token) {
          _accessToken = resp.access_token;
          // Refresh one minute early so in-flight requests don't hit expiry.
          _tokenExpiresAt = Date.now() + ((parseInt(resp.expires_in, 10) || 3600) - 60) * 1000;
          resolve(_accessToken);
        } else {
          reject(new Error((resp && (resp.error_description || resp.error)) || 'Google sign-in failed'));
        }
      };
      _tokenErrCb = function (err) {
        _tokenCb = _tokenErrCb = null;
        reject(new Error((err && (err.message || err.type)) || 'Google sign-in was cancelled'));
      };
      try {
        if (promptMode === null || promptMode === undefined) {
          _tokenClient.requestAccessToken();
        } else {
          _tokenClient.requestAccessToken({ prompt: promptMode });
        }
      } catch (e) {
        _tokenCb = _tokenErrCb = null;
        reject(e);
      }
    });
  });
}

function _ensureToken() {
  if (_accessToken && Date.now() < _tokenExpiresAt) return Promise.resolve(_accessToken);
  return _requestToken(''); // expired/missing → re-request without a prompt
}

// ── Drive REST helpers ─────────────────────────────────────────────────────
// Wraps fetch with the bearer token; on a 401 (token revoked server-side
// before our local expiry estimate) retries exactly once with a fresh token.
// Rejects with a plain Error on any non-OK response — callers surface the
// message in the status line, so nothing here ever throws uncaught.
function _driveFetch(url, opts, isRetry) {
  return _ensureToken().then(function () {
    opts = opts || {};
    var headers = {};
    Object.keys(opts.headers || {}).forEach(function (k) { headers[k] = opts.headers[k]; });
    headers['Authorization'] = 'Bearer ' + _accessToken;
    return fetch(url, { method: opts.method || 'GET', headers: headers, body: opts.body });
  }).then(function (res) {
    if (res.status === 401 && !isRetry) {
      _accessToken = null;
      _tokenExpiresAt = 0;
      return _driveFetch(url, opts, true);
    }
    if (!res.ok) throw new Error('Google Drive request failed (HTTP ' + res.status + ')');
    return res;
  });
}

function _findBackupFile() {
  var q   = "name='" + BACKUP_FILENAME + "' and 'appDataFolder' in parents";
  var url = DRIVE_API + '/files' +
            '?q=' + encodeURIComponent(q) +
            '&spaces=appDataFolder' +
            '&fields=' + encodeURIComponent('files(id,name,modifiedTime)');
  return _driveFetch(url)
    .then(function (res) { return res.json(); })
    .then(function (json) {
      var f  = (json && json.files && json.files[0]) || null;
      _fileId = f ? f.id : null;
      return f;
    });
}

function _downloadBackupContent(fileId) {
  return _driveFetch(DRIVE_API + '/files/' + encodeURIComponent(fileId) + '?alt=media')
    .then(function (res) { return res.text(); })
    .then(function (txt) {
      try { return JSON.parse(txt); }
      catch (e) { throw new Error('Backup file in Drive is not valid JSON'); }
    });
}

// INTENT: Create-or-update kbs-backup.json via one multipart/related request
//   (uploadType=multipart) so metadata + content land atomically in a single
//   round trip. First upload POSTs with parents:['appDataFolder'] (parents are
//   immutable afterwards and MUST NOT be sent on update); later uploads PATCH
//   the known file id, which keeps exactly one backup file per account.
// CHANGE? If _fileId is stale (file deleted from another device between our
//   files.list and this upload) the PATCH 404s — the error surfaces in the
//   status line and the next page load re-lists and re-creates. Renaming
//   BACKUP_FILENAME orphans old backups; users would need to reconnect and
//   back up again.
// VERIFY: Back up twice, then run files.list against appDataFolder in the
//   Drive API explorer → exactly ONE kbs-backup.json, modifiedTime advancing.
function _uploadSnapshot(snap) {
  var boundary = 'kbs_sync_' + Date.now().toString(36);
  var meta     = { name: BACKUP_FILENAME, mimeType: 'application/json' };
  var method, url;
  if (_fileId) {
    method = 'PATCH';
    url    = DRIVE_UPLOAD + '/files/' + encodeURIComponent(_fileId) + '?uploadType=multipart';
  } else {
    meta.parents = ['appDataFolder'];
    method = 'POST';
    url    = DRIVE_UPLOAD + '/files?uploadType=multipart';
  }
  var body =
    '--' + boundary + '\r\n' +
    'Content-Type: application/json; charset=UTF-8\r\n\r\n' +
    JSON.stringify(meta) + '\r\n' +
    '--' + boundary + '\r\n' +
    'Content-Type: application/json\r\n\r\n' +
    JSON.stringify(snap) + '\r\n' +
    '--' + boundary + '--';
  return _driveFetch(url, {
    method:  method,
    headers: { 'Content-Type': 'multipart/related; boundary=' + boundary },
    body:    body
  }).then(function (res) { return res.json(); })
    .then(function (json) {
      if (json && json.id) _fileId = json.id;
      return json;
    });
}

// ── UI rendering ───────────────────────────────────────────────────────────
function _setStatus(msg) {
  var el = document.getElementById('sync-status');
  if (el) el.textContent = msg || '';
}

function _fmtTime(iso) {
  if (!iso) return 'never';
  try { return new Date(iso).toLocaleString(); } catch (e) { return String(iso); }
}

function _updateLastBackup(iso) {
  var el = document.getElementById('sync-last-time');
  if (el) el.textContent = _fmtTime(iso);
}

function _renderNotConfigured() {
  _body.innerHTML =
    '<div class="sync-setup">' +
      'Google Drive sync is not configured for this deployment yet. To enable it, the ' +
      'site owner needs to:' +
      '<ol>' +
        '<li>Create an OAuth 2.0 <em>Web application</em> client ID at ' +
          '<code>console.cloud.google.com/apis/credentials</code>.</li>' +
        '<li>Add authorized JavaScript origins <code>https://kingdombiblestudy.com</code> ' +
          'and <code>http://localhost:4321</code> (no redirect URIs are needed).</li>' +
        '<li>Enable the <strong>Google Drive API</strong> on the same project.</li>' +
        '<li>Paste the client ID into <code>GOOGLE_CLIENT_ID</code> at the top of ' +
          '<code>assets/js/sync.js</code>.</li>' +
      '</ol>' +
    '</div>';
}

function _renderConnecting() {
  _body.innerHTML =
    '<div class="sync-status" id="sync-status" role="status" aria-live="polite">' +
      'Reconnecting to Google Drive…' +
    '</div>';
}

function _renderSignedOut() {
  _body.innerHTML =
    '<div class="sync-row">' +
      '<button type="button" class="set-btn set-btn--primary" id="sync-connect">Connect Google Drive</button>' +
    '</div>' +
    '<p class="sync-note">Backups go only to a private app-data area of your own ' +
      'Google Drive — nothing is ever sent to this site or anyone else.</p>' +
    '<div class="sync-status" id="sync-status" role="status" aria-live="polite"></div>';
  document.getElementById('sync-connect').addEventListener('click', _onConnectClick);
}

function _renderSignedIn() {
  var st = _getSyncState();
  _body.innerHTML =
    '<div class="sync-row">' +
      '<span class="sync-last">Last backup: <strong id="sync-last-time"></strong></span>' +
    '</div>' +
    '<div class="sync-row">' +
      '<button type="button" class="set-btn set-btn--primary" id="sync-backup">Back up now</button>' +
      '<button type="button" class="set-btn" id="sync-restore">Restore from backup</button>' +
      '<button type="button" class="set-btn set-btn--danger" id="sync-disconnect">Disconnect</button>' +
    '</div>' +
    '<div class="sync-status" id="sync-status" role="status" aria-live="polite"></div>';
  _updateLastBackup(st.lastBackupAt || null);
  document.getElementById('sync-backup').addEventListener('click', function () {
    _doBackup(null, null, false);
  });
  document.getElementById('sync-restore').addEventListener('click', _doRestore);
  document.getElementById('sync-disconnect').addEventListener('click', _doDisconnect);
}

// ── Behaviors ──────────────────────────────────────────────────────────────
function _onConnectClick() {
  _setStatus('Opening Google sign-in…');
  _requestToken(null)
    .then(_onSignedIn)
    .catch(function (err) {
      _setStatus('Sign-in failed: ' + ((err && err.message) || err));
    });
}

function _onSignedIn() {
  _patchSyncState({ connected: true });
  _renderSignedIn();
  _setStatus('Checking Drive for an existing backup…');
  _findBackupFile()
    .then(function (f) {
      if (!f) {
        _updateLastBackup(_getSyncState().lastBackupAt || null);
        _setStatus('Connected. No backup in Drive yet.');
        return null;
      }
      // Prefer the savedAt recorded inside the file (matches the snapshot
      // exactly); fall back to Drive's modifiedTime if the body is unreadable.
      return _downloadBackupContent(f.id)
        .then(function (snap) {
          _updateLastBackup((snap && snap.savedAt) || f.modifiedTime || null);
          _setStatus('Connected.');
        })
        .catch(function () {
          _updateLastBackup(f.modifiedTime || null);
          _setStatus('Connected.');
        });
    })
    .catch(function (err) {
      _setStatus('Could not check Drive: ' + ((err && err.message) || err));
    })
    .then(_scheduleAutoBackup);
}

// INTENT: Fire-and-forget auto-backup — 5 s after a successful (re)connect,
//   at most once per page load, and only when the local data fingerprint
//   differs from bsw_sync_state.lastHash. Keeps Drive current without the
//   user thinking about it, while identical data never wastes an upload.
// CHANGE? The 5 s debounce lets the rest of settings-page init and any
//   just-restored state settle before hashing; shortening it risks uploading
//   a half-migrated snapshot on the load right after a schema migration.
// VERIFY: Connect, edit a note in another tab, reload the settings page →
//   within ~5 s the status line shows "Backing up changes…" then "Backup
//   complete." Reload again with no edits → no upload (hash unchanged).
function _scheduleAutoBackup() {
  if (_autoBackupDone) return;
  setTimeout(function () {
    if (_autoBackupDone || !_accessToken) return;
    var snap = _buildSnapshot();
    var hash = _snapshotHash(snap);
    if (_getSyncState().lastHash === hash) return; // nothing changed
    _autoBackupDone = true;
    _doBackup(snap, hash, true);
  }, 5000);
}

function _doBackup(snap, hash, auto) {
  if (_busy) return;
  _busy = true;
  snap = snap || _buildSnapshot();
  hash = hash || _snapshotHash(snap);
  _setStatus(auto ? 'Backing up changes…' : 'Backing up…');
  _uploadSnapshot(snap)
    .then(function () {
      _patchSyncState({ lastBackupAt: snap.savedAt, lastHash: hash });
      _updateLastBackup(snap.savedAt);
      _setStatus(auto ? 'Auto-backup complete.' : 'Backup complete.');
    })
    .catch(function (err) {
      _setStatus('Backup failed: ' + ((err && err.message) || err));
    })
    .then(function () { _busy = false; });
}

// INTENT: Restore = destructive overwrite of local bsw_* keys from the Drive
//   snapshot, then a full reload so every module re-reads localStorage from
//   scratch (no in-memory caches go stale). confirm() is mandatory because
//   this clobbers anything written locally since the backup was taken.
// CHANGE? Keys present locally but absent from the backup are deliberately
//   LEFT IN PLACE (write-only restore, per the snapshot contract) — deleting
//   them would turn an old backup into a data-loss event. bsw_sync_state is
//   never restored (device-local bookkeeping).
// VERIFY: Back up, change a bookmark, Restore from backup → confirm dialog →
//   page reloads with the pre-change bookmark; bsw_sync_state.lastHash matches
//   so no auto-backup fires on the reloaded page.
function _doRestore() {
  if (_busy) return;
  var ok = confirm(
    'Restore from your Google Drive backup?\n\n' +
    'This OVERWRITES the study data saved on this device (notes, bookmarks, ' +
    'plans, progress) with the backed-up copy, then reloads the page. ' +
    'Anything added on this device since that backup will be lost.'
  );
  if (!ok) return;
  _busy = true;
  _setStatus('Restoring from Drive…');
  _findBackupFile()
    .then(function (f) {
      if (!f) throw new Error('no backup file found in Drive');
      return _downloadBackupContent(f.id);
    })
    .then(function (snap) {
      if (!snap || !snap.data || typeof snap.data !== 'object') {
        throw new Error('backup file has an unexpected format');
      }
      Object.keys(snap.data).forEach(function (k) {
        // Safety: only ever write bsw_* keys, and never the sync state itself.
        if (k.indexOf('bsw_') !== 0 || k === SYNC_STATE_KEY) return;
        if (typeof snap.data[k] !== 'string') return;
        try { localStorage.setItem(k, snap.data[k]); } catch (e) {}
      });
      // Re-hash what is now on disk so the reloaded page's auto-backup sees
      // "unchanged" and doesn't immediately re-upload the restored data.
      _patchSyncState({
        lastBackupAt: snap.savedAt || new Date().toISOString(),
        lastHash:     _snapshotHash(_buildSnapshot())
      });
      _setStatus('Restore complete — reloading…');
      location.reload();
    })
    .catch(function (err) {
      _busy = false;
      _setStatus('Restore failed: ' + ((err && err.message) || err));
    });
}

function _doDisconnect() {
  var token = _accessToken;
  _accessToken    = null;
  _tokenExpiresAt = 0;
  _fileId         = null;
  _patchSyncState({ connected: false });
  // Revoke the grant so the app no longer appears authorized on the account.
  // Best-effort: the UI returns to signed-out regardless of revoke outcome.
  if (token && window.google && window.google.accounts && window.google.accounts.oauth2) {
    try { window.google.accounts.oauth2.revoke(token, function () {}); } catch (e) {}
  }
  _renderSignedOut();
  _setStatus('Disconnected. The backup file remains in your Google Drive.');
}

// ── Entry point ────────────────────────────────────────────────────────────
// INTENT: Self-guarded init called unconditionally from app.js. Renders into
//   #sync-body inside #sync-section. If a previous visit connected
//   (bsw_sync_state.connected) it attempts a no-prompt token so the section
//   comes up signed-in without user interaction; if that quiet attempt fails
//   (no Google session, popup blocked) it falls back to the signed-out UI
//   without surfacing an error — connecting is one click away, no popup spam.
// CHANGE? The connected flag is kept on silent failure on purpose: a blocked
//   popup or logged-out Google session is usually transient, and the retry
//   only happens when the user actually visits the settings page.
// VERIFY: On any non-settings page this returns immediately (no #sync-section).
//   On settings with an empty GOOGLE_CLIENT_ID it shows the setup note.
export function initSyncSection() {
  var root = document.getElementById('sync-section');
  if (!root) return;

  _body = document.getElementById('sync-body');
  if (!_body) {
    _body = document.createElement('div');
    _body.id = 'sync-body';
    root.appendChild(_body);
  }

  if (!GOOGLE_CLIENT_ID) {
    _renderNotConfigured();
    return;
  }

  if (_getSyncState().connected) {
    _renderConnecting();
    _requestToken('')
      .then(_onSignedIn)
      .catch(function () { _renderSignedOut(); });
  } else {
    _renderSignedOut();
  }
}
