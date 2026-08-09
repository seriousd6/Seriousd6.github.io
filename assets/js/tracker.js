/* tracker.js — Daily discipline-completion tracking.
 *
 * Most disciplines are auto-detected: reading is derived from bsw_plans, prayer
 * from bsw_journal, and so on.  Auto-detection is convenient but it cannot see
 * everything — a devotional read in a paper book, a prayer that was never typed
 * up, a sermon heard but not logged.  Every discipline therefore also carries a
 * MANUAL OVERRIDE that the user can set from the checklist UI.
 *
 * Storage key: bsw_tracker
 *   { [YYYY-MM-DD]: {
 *       devotional?: true,          // legacy explicit bits (devotional, memory)
 *       memory?: true,
 *       manual?: { [discipline]: boolean }   // true = force done, false = force not-done
 *   } }
 *
 * Resolution order for every discipline, on every date:
 *   1. manual[key] if present  (true or false — an explicit user decision wins)
 *   2. otherwise the auto-detected value
 * Clearing the override (setManual(key, null)) returns the discipline to auto.
 *
 * Public API
 *   markDone(discipline, date?)          — record an explicit completion bit
 *   isDone(discipline, date?)            — explicit bit, honouring any override
 *   setManual(d, value, date?)           — true / false to force, null to clear
 *   getManual(discipline, date?)         — true | false | undefined (= auto)
 *   toggleManual(discipline, date?)      — flip the effective state for that date
 *   isAuto(discipline, date?)            — true when no override is set
 *   isReadingDone(date?) … isFastingDone(date?)  — per-discipline, override-aware
 *   getStatus(date?)                     → { reading, devotional, … } for any date
 *   getToday()                           → getStatus(today)
 *   DISCIPLINES                          — the canonical key list
 *   onUpdate(fn)                         — callback for same-tab changes
 */
'use strict';

export var TRACKER_KEY = 'bsw_tracker';

// INTENT: One canonical ordered list of discipline keys, so UI consumers (the home-page
//   checklist, the discipline tab strip) iterate the same set the status object reports.
// CHANGE? Adding a discipline means: add the key here, add a `_derived` branch below, and
//   add a label in whichever UI lists it. Missing the `_derived` branch makes it silently
//   always-false unless manually ticked.
export var DISCIPLINES = [
  'reading', 'devotional', 'memory', 'prayer',
  'reflection', 'worship', 'gratitude', 'fasting',
];

var _listeners = [];

// ── Internal helpers ──────────────────────────────────────────────────────────
function _fmt(d) {
  return d.getFullYear() + '-' +
    String(d.getMonth() + 1).padStart(2, '0') + '-' +
    String(d.getDate()).padStart(2, '0');
}

export function _todayStr() { return _fmt(new Date()); }

function _getAll() {
  try { return JSON.parse(localStorage.getItem(TRACKER_KEY) || '{}'); }
  catch (e) { return {}; }
}

function _setAll(data) {
  try { localStorage.setItem(TRACKER_KEY, JSON.stringify(data)); }
  catch (e) {}
  _listeners.forEach(function (fn) { try { fn(); } catch (_) {} });
}

// Keep only the last 400 days so storage cannot grow without bound.
function _prune(all) {
  var keys = Object.keys(all).sort();
  if (keys.length > 400) keys.slice(0, keys.length - 400).forEach(function (k) { delete all[k]; });
  return all;
}

function _readJson(key, fallback) {
  try { return JSON.parse(localStorage.getItem(key) || fallback); }
  catch (e) { try { return JSON.parse(fallback); } catch (_) { return null; } }
}

// ── Manual overrides ──────────────────────────────────────────────────────────
// INTENT: Let the user record a discipline the auto-detection cannot see, and equally
//   un-record one it wrongly inferred. Three states, not two: true, false, and absent.
// CHANGE? `absent` must stay distinguishable from `false` — collapsing them would make
//   "clear the override" impossible and strand any discipline the user once un-ticked.
// VERIFY: setManual('reading', true) → isReadingDone() true even with no plan enrolled;
//   setManual('reading', null) → back to whatever bsw_plans says.
export function getManual(discipline, date) {
  var rec = _getAll()[date || _todayStr()];
  if (!rec || !rec.manual) return undefined;
  var v = rec.manual[discipline];
  return typeof v === 'boolean' ? v : undefined;
}

export function setManual(discipline, value, date) {
  date = date || _todayStr();
  var all = _getAll();
  if (!all[date]) all[date] = {};
  if (value === null || value === undefined) {
    if (all[date].manual) {
      delete all[date].manual[discipline];
      if (!Object.keys(all[date].manual).length) delete all[date].manual;
    }
  } else {
    if (!all[date].manual) all[date].manual = {};
    all[date].manual[discipline] = !!value;
  }
  _setAll(_prune(all));
}

export function isAuto(discipline, date) {
  return getManual(discipline, date) === undefined;
}

// Flip the *effective* state: whatever the row currently shows, show the opposite.
// If that lands back on the auto-detected value the override is cleared rather than
// pinned, so a row only stays manual for as long as it actually disagrees with reality.
export function toggleManual(discipline, date) {
  date = date || _todayStr();
  var want = !_effective(discipline, date);
  if (_derived(discipline, date) === want) setManual(discipline, null, date);
  else setManual(discipline, want, date);
  return want;
}

// ── Explicit bits (devotional, memory) ───────────────────────────────────────
export function markDone(discipline, date) {
  date = date || _todayStr();
  var all = _getAll();
  if (!all[date]) all[date] = {};
  all[date][discipline] = true;
  _setAll(_prune(all));
}

function _explicit(discipline, date) {
  var rec = _getAll()[date];
  return !!(rec && rec[discipline] === true);
}

export function isDone(discipline, date) {
  return _effective(discipline, date || _todayStr());
}

// ── Auto-detection, one function per discipline ───────────────────────────────
// Each `_raw*` reads another module's storage key and is deliberately override-free;
// the exported `is*Done` wrappers below apply the override on top.

// CHANGE? Reads 'bsw_plans' (schema { [planId]: { startDate: string, completed: { [dayNum]: … } } })
//   owned by daily.js and the Plans tab. If either renames the key or changes the schema this
//   silently returns false — update all three together.
function _rawReadingDone(date) {
  var plans = _readJson('bsw_plans', '{}');
  if (!plans) return false;
  var d = new Date(date + 'T00:00:00');
  return Object.keys(plans).some(function (id) {
    var p = plans[id];
    if (!p || !p.startDate) return false;
    var start  = new Date(p.startDate + 'T00:00:00');
    var dayNum = Math.floor((d - start) / 86400000) + 1;
    return !!(p.completed && p.completed[dayNum]);
  });
}

function _rawEntryOnDate(key, date) {
  var list = _readJson(key, '[]');
  return Array.isArray(list) && list.some(function (e) { return e && e.date === date; });
}

// Worship looks back to the most recent Sunday rather than the day itself.
function _rawWorshipDone(date) {
  var d = new Date(date + 'T00:00:00');
  var sunday = new Date(d.getTime() - d.getDay() * 86400000);
  return _rawEntryOnDate('bsw_worship', _fmt(sunday));
}

// Fasting counts anywhere in the containing Sun–Sat week.
function _rawFastingDone(date) {
  var d = new Date(date + 'T00:00:00');
  var sunday = new Date(d.getTime() - d.getDay() * 86400000);
  var sunStr = _fmt(sunday), satStr = _fmt(new Date(sunday.getTime() + 6 * 86400000));
  var fasts = _readJson('bsw_fasting', '[]');
  return Array.isArray(fasts) && fasts.some(function (f) {
    return f && f.date >= sunStr && f.date <= satStr;
  });
}

function _derived(discipline, date) {
  switch (discipline) {
    case 'reading':    return _rawReadingDone(date);
    case 'prayer':     return _rawEntryOnDate('bsw_journal', date);
    case 'reflection': return _rawEntryOnDate('bsw_reflections', date);
    case 'gratitude':  return _rawEntryOnDate('bsw_gratitude', date);
    case 'worship':    return _rawWorshipDone(date);
    case 'fasting':    return _rawFastingDone(date);
    default:           return _explicit(discipline, date);   // devotional, memory
  }
}

function _effective(discipline, date) {
  var m = getManual(discipline, date);
  if (m !== undefined) return m;
  try { return _derived(discipline, date); } catch (e) { return false; }
}

export function isReadingDone(date)    { return _effective('reading',    date || _todayStr()); }
export function isPrayerDone(date)     { return _effective('prayer',     date || _todayStr()); }
export function isReflectionDone(date) { return _effective('reflection', date || _todayStr()); }
export function isWorshipDone(date)    { return _effective('worship',    date || _todayStr()); }
export function isGratitudeDone(date)  { return _effective('gratitude',  date || _todayStr()); }
export function isFastingDone(date)    { return _effective('fasting',    date || _todayStr()); }

// ── Combined status ───────────────────────────────────────────────────────────
// INTENT: Aggregate one date's completion across all 8 discipline dimensions; the home-page
//   checklist and the discipline tab strip both read this on load and after every onUpdate.
// VERIFY: Complete reading for today → getToday().reading === true; tick any row in the
//   home checklist → getToday() flips for that key even with no underlying entry.
export function getStatus(date) {
  date = date || _todayStr();
  var out = {};
  DISCIPLINES.forEach(function (k) { out[k] = _effective(k, date); });
  return out;
}

export function getToday() { return getStatus(_todayStr()); }

// ── Change notifications ──────────────────────────────────────────────────────
// CHANGE? Same-tab only (fired by _setAll). Cross-tab changes arrive via the native
//   window 'storage' event, which callers wire separately.
export function onUpdate(fn) { _listeners.push(fn); }
