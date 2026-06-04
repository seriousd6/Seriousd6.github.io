/* tracker.js — Daily discipline-completion tracking.
 *
 * Stores explicit completion bits for disciplines whose done-state cannot be
 * derived from other data.  Reading and prayer completion are derived on the
 * fly from bsw_plans and bsw_journal respectively, so they require no extra
 * storage here.
 *
 * Storage key: bsw_tracker
 *   { [YYYY-MM-DD]: { devotional?: true, memory?: true } }
 *
 * Public API
 *   markDone(discipline)           — record today's discipline as complete
 *   isDone(discipline, date?)      — check explicit bit (today if omitted)
 *   isReadingDone(date?)           — derived: any enrolled plan day marked done
 *   isPrayerDone(date?)            — derived: any journal entry written today
 *   getToday()                     → { reading, devotional, memory, prayer }
 *   onUpdate(fn)                   — register a callback for same-tab changes
 */
'use strict';

export var TRACKER_KEY = 'bsw_tracker';

var _listeners = [];

// ── Internal helpers ──────────────────────────────────────────────────────────
export function _todayStr() {
  var d = new Date();
  return d.getFullYear() + '-' +
    String(d.getMonth() + 1).padStart(2, '0') + '-' +
    String(d.getDate()).padStart(2, '0');
}

function _getAll() {
  try { return JSON.parse(localStorage.getItem(TRACKER_KEY) || '{}'); }
  catch (e) { return {}; }
}

function _setAll(data) {
  try { localStorage.setItem(TRACKER_KEY, JSON.stringify(data)); }
  catch (e) {}
  _listeners.forEach(function (fn) { try { fn(); } catch (_) {} });
}

// ── Explicit bits (devotional, memory) ───────────────────────────────────────
export function markDone(discipline) {
  var today = _todayStr();
  var all   = _getAll();
  if (!all[today]) all[today] = {};
  all[today][discipline] = true;
  // Keep only the last 400 days to bound storage growth
  var keys = Object.keys(all).sort();
  if (keys.length > 400) keys.slice(0, keys.length - 400).forEach(function (k) { delete all[k]; });
  _setAll(all);
}

export function isDone(discipline, date) {
  date = date || _todayStr();
  var rec = _getAll()[date];
  return !!(rec && rec[discipline]);
}

// ── Derived: reading (from bsw_plans) ────────────────────────────────────────
// Returns true if any enrolled plan has today's day number marked complete.
export function isReadingDone(date) {
  date = date || _todayStr();
  try {
    var plans = JSON.parse(localStorage.getItem('bsw_plans') || '{}');
    var d     = new Date(date + 'T00:00:00');
    return Object.keys(plans).some(function (id) {
      var p = plans[id];
      if (!p || !p.startDate) return false;
      var start  = new Date(p.startDate + 'T00:00:00');
      var dayNum = Math.floor((d - start) / 86400000) + 1;
      return !!(p.completed && p.completed[dayNum]);
    });
  } catch (e) { return false; }
}

// ── Derived: prayer (from bsw_journal) ───────────────────────────────────────
// Returns true if any journal entry's date field matches the given date.
export function isPrayerDone(date) {
  date = date || _todayStr();
  try {
    var journal = JSON.parse(localStorage.getItem('bsw_journal') || '[]');
    return journal.some(function (e) { return e.date === date; });
  } catch (e) { return false; }
}

// ── Derived: reflection (from bsw_reflections) ───────────────────────────────
// Returns true if any reflection entry was written on the given date.
export function isReflectionDone(date) {
  date = date || _todayStr();
  try {
    var reflections = JSON.parse(localStorage.getItem('bsw_reflections') || '[]');
    return reflections.some(function (e) { return e.date === date; });
  } catch (e) { return false; }
}

// ── Derived: worship — has a sermon entry for the most recent Sunday ──────────
// Shows whether the last Sunday (or today if Sunday) has a worship entry.
export function isWorshipDone(date) {
  date = date || _todayStr();
  try {
    var d = new Date(date + 'T00:00:00');
    // Walk back to the most recent Sunday
    var dow = d.getDay(); // 0=Sun
    var sunday = new Date(d.getTime() - dow * 86400000);
    var sunStr = sunday.getFullYear() + '-' +
      String(sunday.getMonth() + 1).padStart(2, '0') + '-' +
      String(sunday.getDate()).padStart(2, '0');
    var worship = JSON.parse(localStorage.getItem('bsw_worship') || '[]');
    return worship.some(function (e) { return e.date === sunStr; });
  } catch (e) { return false; }
}

// ── Derived: gratitude (from bsw_gratitude) ──────────────────────────────────
export function isGratitudeDone(date) {
  date = date || _todayStr();
  try {
    var entries = JSON.parse(localStorage.getItem('bsw_gratitude') || '[]');
    return entries.some(function (e) { return e.date === date; });
  } catch (e) { return false; }
}

// ── Derived: fasting — any fast logged this week ──────────────────────────────
export function isFastingDone(date) {
  date = date || _todayStr();
  try {
    var d = new Date(date + 'T00:00:00');
    var dow = d.getDay();
    var sunday = new Date(d.getTime() - dow * 86400000);
    var saturday = new Date(sunday.getTime() + 6 * 86400000);
    function toStr(dt) {
      return dt.getFullYear() + '-' +
        String(dt.getMonth() + 1).padStart(2, '0') + '-' +
        String(dt.getDate()).padStart(2, '0');
    }
    var sunStr = toStr(sunday), satStr = toStr(saturday);
    var fasts = JSON.parse(localStorage.getItem('bsw_fasting') || '[]');
    return fasts.some(function (f) { return f.date >= sunStr && f.date <= satStr; });
  } catch (e) { return false; }
}

// ── Combined status ───────────────────────────────────────────────────────────
export function getToday() {
  var today = _todayStr();
  return {
    reading:    isReadingDone(today),
    devotional: isDone('devotional', today),
    memory:     isDone('memory', today),
    prayer:     isPrayerDone(today),
    reflection: isReflectionDone(today),
    worship:    isWorshipDone(today),
    gratitude:  isGratitudeDone(today),
    fasting:    isFastingDone(today),
  };
}

// ── Change notifications ──────────────────────────────────────────────────────
// Allows the home-page tracker card to re-render when a discipline is marked
// done in the same tab (cross-tab updates fire via the native `storage` event).
export function onUpdate(fn) {
  _listeners.push(fn);
}
