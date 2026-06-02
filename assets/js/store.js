/* store.js — Unified user-data read/write, export/import.
 *
 * Single source of truth for every localStorage key belonging to the user.
 * Reads localStorage directly so this module stays free of circular imports;
 * all other modules keep their own accessor helpers unchanged.
 *
 * Public API:
 *   exportAll()              → plain object with all user data (schema v2)
 *   downloadBackup()         → triggers a .json file download
 *   importAll(data, opts)    → restores data; opts.mode = 'merge' (default) | 'replace'
 *   readBackupFile(file)     → Promise<object>  (parses the file, does NOT import)
 *   summarise(data)          → human-readable summary string for confirm dialogs
 */
'use strict';

// ── Key registry ──────────────────────────────────────────────────────────────
// Every localStorage key that stores user-authored content or meaningful state.
export var STORE_KEYS = {
  plans:       'bsw_plans',
  memory:      'bsw_memory',
  journal:     'bsw_journal',
  notes:       'bsw_notes',       // v1: { [ref]: { highlight, note, tags } }
  notes_v2:    'bsw_notes_v2',   // v2: [ { id, bookId, ch, v, text, … } ]
  bookmarks:   'bsw_bookmarks',
  history:     'bsw_history',
  streak:      'bsw_streak',
  ver:         'bsw_version',
  theme:       'bsw_theme',
  devot:       'bsw_devot_period',
  sidebar:     'bsw_sidebar',
  memory_mode:   'bsw_memory_mode',  // flashcard direction pref
  tracker:       'bsw_tracker',      // daily discipline completion bits
  worship:       'bsw_worship',      // sermon notes entries
  fasting:       'bsw_fasting',      // fasting log entries
  reflections:   'bsw_reflections',  // study reflection journal entries
  lib_progress:  'bsw_lib_progress', // library document reading positions
  chapter_read:  'bsw_chapter_read', // Bible chapter completion { bookId: { ch: dateStr } }
};

var SCHEMA = 2;

// ── Internal helpers ──────────────────────────────────────────────────────────
function _get(key, fallback) {
  try {
    var raw = localStorage.getItem(key);
    return raw !== null ? JSON.parse(raw) : fallback;
  } catch (e) { return fallback; }
}

function _set(key, val) {
  try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {}
}

// ── Export ────────────────────────────────────────────────────────────────────
export function exportAll() {
  return {
    _schema:   SCHEMA,
    _exported: new Date().toISOString(),
    plans:     _get(STORE_KEYS.plans,     {}),
    memory:    _get(STORE_KEYS.memory,    {}),
    journal:   _get(STORE_KEYS.journal,   []),
    notes:     _get(STORE_KEYS.notes,     {}),
    notes_v2:  _get(STORE_KEYS.notes_v2,  []),
    bookmarks: _get(STORE_KEYS.bookmarks, []),
    history:   _get(STORE_KEYS.history,   []),
    streak:    _get(STORE_KEYS.streak,    { days: [] }),
    tracker:      _get(STORE_KEYS.tracker,      {}),
    worship:      _get(STORE_KEYS.worship,      []),
    fasting:      _get(STORE_KEYS.fasting,      []),
    reflections:  _get(STORE_KEYS.reflections,  []),
    lib_progress: _get(STORE_KEYS.lib_progress, {}),
    chapter_read: _get(STORE_KEYS.chapter_read, {}),
    prefs: {
      version:      localStorage.getItem(STORE_KEYS.ver)         || null,
      theme:        localStorage.getItem(STORE_KEYS.theme)       || null,
      devot_period: localStorage.getItem(STORE_KEYS.devot)       || null,
      sidebar:      localStorage.getItem(STORE_KEYS.sidebar)     || null,
      memory_mode:  localStorage.getItem(STORE_KEYS.memory_mode) || null,
    },
  };
}

export function downloadBackup() {
  var data    = exportAll();
  var blob    = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  var url     = URL.createObjectURL(blob);
  var a       = document.createElement('a');
  a.href      = url;
  a.download  = 'bsw-backup-' + new Date().toISOString().slice(0, 10) + '.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// ── Import ────────────────────────────────────────────────────────────────────
// opts.mode: 'merge'   (default) — incoming entries are added; existing data is
//                                   kept if the backup has nothing for that slot.
//            'replace'           — each section in the backup fully overwrites
//                                   the local copy; sections absent from the
//                                   backup are left untouched.
//
// Merge semantics:
//   plans      object-level merge: backup plan IDs win over existing for same key
//   memory     object-level merge: backup refs win
//   journal    append-by-id: entries whose id is not already present are added
//   notes      object-level merge: backup refs win
//   notes_v2   append-by-id: entries whose id is not already present are added
//   bookmarks  union, capped at 200
//   history    union, capped at 100 (backup entries added to the end)
//   streak     union of day strings, sorted
//   prefs      per-key overwrite only for non-null values in backup

export function importAll(data, opts) {
  opts = opts || {};
  var mode = opts.mode || 'merge';

  if (!data || typeof data !== 'object') throw new Error('Invalid backup: not a JSON object');

  if (mode === 'replace') {
    if (data.plans    !== undefined) _set(STORE_KEYS.plans,    data.plans);
    if (data.memory   !== undefined) _set(STORE_KEYS.memory,   data.memory);
    if (data.journal  !== undefined) _set(STORE_KEYS.journal,  data.journal);
    if (data.notes    !== undefined) _set(STORE_KEYS.notes,    data.notes);
    if (data.notes_v2 !== undefined) _set(STORE_KEYS.notes_v2, data.notes_v2);
    if (data.bookmarks !== undefined) _set(STORE_KEYS.bookmarks, data.bookmarks);
    if (data.history  !== undefined) _set(STORE_KEYS.history,  data.history);
    if (data.streak   !== undefined) _set(STORE_KEYS.streak,   data.streak);
    if (data.tracker      !== undefined) _set(STORE_KEYS.tracker,      data.tracker);
    if (data.worship      !== undefined) _set(STORE_KEYS.worship,      data.worship);
    if (data.fasting      !== undefined) _set(STORE_KEYS.fasting,      data.fasting);
    if (data.reflections  !== undefined) _set(STORE_KEYS.reflections,  data.reflections);
    if (data.lib_progress !== undefined) _set(STORE_KEYS.lib_progress, data.lib_progress);
    if (data.chapter_read !== undefined) _set(STORE_KEYS.chapter_read, data.chapter_read);
  } else {
    // plans — object merge
    if (data.plans && typeof data.plans === 'object') {
      _set(STORE_KEYS.plans, Object.assign(_get(STORE_KEYS.plans, {}), data.plans));
    }
    // memory — object merge
    if (data.memory && typeof data.memory === 'object') {
      _set(STORE_KEYS.memory, Object.assign(_get(STORE_KEYS.memory, {}), data.memory));
    }
    // journal — append by id
    if (Array.isArray(data.journal)) {
      var journal  = _get(STORE_KEYS.journal, []);
      var jIds     = {};
      journal.forEach(function (e) { if (e.id) jIds[e.id] = true; });
      data.journal.forEach(function (e) { if (e.id && !jIds[e.id]) journal.push(e); });
      _set(STORE_KEYS.journal, journal);
    }
    // notes v1 — object merge
    if (data.notes && typeof data.notes === 'object') {
      _set(STORE_KEYS.notes, Object.assign(_get(STORE_KEYS.notes, {}), data.notes));
    }
    // notes v2 — append by id
    if (Array.isArray(data.notes_v2)) {
      var nv2  = _get(STORE_KEYS.notes_v2, []);
      var nIds = {};
      nv2.forEach(function (n) { if (n.id) nIds[n.id] = true; });
      data.notes_v2.forEach(function (n) { if (n.id && !nIds[n.id]) nv2.push(n); });
      _set(STORE_KEYS.notes_v2, nv2);
    }
    // bookmarks — union
    if (Array.isArray(data.bookmarks)) {
      var bm    = _get(STORE_KEYS.bookmarks, []);
      var bmSet = {};
      bm.forEach(function (r) { bmSet[r] = true; });
      data.bookmarks.forEach(function (r) { if (r && !bmSet[r]) { bm.unshift(r); bmSet[r] = true; } });
      if (bm.length > 200) bm.length = 200;
      _set(STORE_KEYS.bookmarks, bm);
    }
    // history — union (backup entries appended, keep most recent 100)
    if (Array.isArray(data.history)) {
      var hist    = _get(STORE_KEYS.history, []);
      var histSet = {};
      hist.forEach(function (r) { histSet[r] = true; });
      data.history.forEach(function (r) { if (r && !histSet[r]) { hist.push(r); histSet[r] = true; } });
      if (hist.length > 100) hist.length = 100;
      _set(STORE_KEYS.history, hist);
    }
    // worship, fasting, reflections — append-by-id arrays
    ['worship', 'fasting', 'reflections'].forEach(function (k) {
      if (!Array.isArray(data[k])) return;
      var arr  = _get(STORE_KEYS[k], []);
      var seen = {};
      arr.forEach(function (e) { if (e.id) seen[e.id] = true; });
      data[k].forEach(function (e) { if (e.id && !seen[e.id]) arr.push(e); });
      _set(STORE_KEYS[k], arr);
    });
    // lib_progress — object merge per docId
    if (data.lib_progress && typeof data.lib_progress === 'object') {
      _set(STORE_KEYS.lib_progress, Object.assign(_get(STORE_KEYS.lib_progress, {}), data.lib_progress));
    }
    // chapter_read — deep merge per bookId
    if (data.chapter_read && typeof data.chapter_read === 'object') {
      var cr = _get(STORE_KEYS.chapter_read, {});
      Object.keys(data.chapter_read).forEach(function (bk) {
        cr[bk] = Object.assign(cr[bk] || {}, data.chapter_read[bk]);
      });
      _set(STORE_KEYS.chapter_read, cr);
    }
    // tracker — object-level merge (per-date objects merged)
    if (data.tracker && typeof data.tracker === 'object') {
      var tracker = _get(STORE_KEYS.tracker, {});
      Object.keys(data.tracker).forEach(function (date) {
        tracker[date] = Object.assign(tracker[date] || {}, data.tracker[date]);
      });
      _set(STORE_KEYS.tracker, tracker);
    }
    // streak — union of day strings
    if (data.streak && Array.isArray(data.streak.days)) {
      var streak = _get(STORE_KEYS.streak, { days: [] });
      var daySet = {};
      streak.days.forEach(function (d) { daySet[d] = true; });
      data.streak.days.forEach(function (d) { if (d && !daySet[d]) { streak.days.push(d); daySet[d] = true; } });
      streak.days.sort();
      _set(STORE_KEYS.streak, streak);
    }
  }

  // Prefs always merge per-key (non-null values in backup win)
  if (data.prefs && typeof data.prefs === 'object') {
    var p = data.prefs;
    if (p.version      != null) localStorage.setItem(STORE_KEYS.ver,         p.version);
    if (p.theme        != null) localStorage.setItem(STORE_KEYS.theme,       p.theme);
    if (p.devot_period != null) localStorage.setItem(STORE_KEYS.devot,       p.devot_period);
    if (p.sidebar      != null) localStorage.setItem(STORE_KEYS.sidebar,     p.sidebar);
    if (p.memory_mode  != null) localStorage.setItem(STORE_KEYS.memory_mode, p.memory_mode);
  }
}

// ── File helpers ──────────────────────────────────────────────────────────────
export function readBackupFile(file) {
  return new Promise(function (resolve, reject) {
    var reader = new FileReader();
    reader.onload = function (e) {
      try { resolve(JSON.parse(e.target.result)); }
      catch (_) { reject(new Error('File is not valid JSON')); }
    };
    reader.onerror = function () { reject(new Error('Could not read file')); };
    reader.readAsText(file);
  });
}

// ── Summary ───────────────────────────────────────────────────────────────────
// Returns a human-readable string describing the contents of a backup object.
// Useful for showing users what they are about to import.
export function summarise(data) {
  if (!data || typeof data !== 'object') return 'Invalid backup file.';

  var lines = [];

  if (data.plans && typeof data.plans === 'object') {
    var nPlans = Object.keys(data.plans).length;
    if (nPlans) lines.push(nPlans + ' reading plan' + (nPlans !== 1 ? 's' : '') + ' with progress');
  }
  if (data.memory && typeof data.memory === 'object') {
    var nMem = Object.keys(data.memory).length;
    if (nMem) lines.push(nMem + ' memory verse' + (nMem !== 1 ? 's' : ''));
  }
  if (Array.isArray(data.journal) && data.journal.length) {
    lines.push(data.journal.length + ' prayer journal entr' + (data.journal.length !== 1 ? 'ies' : 'y'));
  }
  var nNotes = 0;
  if (data.notes && typeof data.notes === 'object') nNotes += Object.keys(data.notes).length;
  if (Array.isArray(data.notes_v2)) nNotes += data.notes_v2.length;
  if (nNotes) lines.push(nNotes + ' verse annotation' + (nNotes !== 1 ? 's' : ''));

  if (Array.isArray(data.bookmarks) && data.bookmarks.length) {
    lines.push(data.bookmarks.length + ' bookmark' + (data.bookmarks.length !== 1 ? 's' : ''));
  }
  if (data.streak && Array.isArray(data.streak.days) && data.streak.days.length) {
    lines.push(data.streak.days.length + ' reading day' + (data.streak.days.length !== 1 ? 's' : '') + ' in streak');
  }
  if (data._exported) {
    lines.push('Exported: ' + new Date(data._exported).toLocaleDateString());
  }

  return lines.length ? lines.join('\n') : 'Backup appears empty.';
}
