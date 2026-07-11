/* mem.js — Scripture-memory storage helpers (extracted from daily.js, Phase 2.5).
 *
 * Split out so the universal verse modal's "Memorize" button (registered via
 * registerMemHelpers in core-boot) doesn't drag the whole daily.js page module
 * onto every page. daily.js imports these for the memorize page and VOTD;
 * modal.js calls _memHas/_memAdd/_memRemove/_memRefreshModalBtn synchronously.
 */
'use strict';

export var MEMORY_KEY      = 'bsw_memory';
export var MEMORY_MODE_KEY = 'bsw_memory_mode';

// INTENT: Serialize / deserialize the memory-verse set to localStorage under
//   MEMORY_KEY. The schema is a flat object {[ref]: {added, nextReview, score, tags}}.
//   _memGet returns {} on parse error so callers always get a safe object.
// CHANGE? _memAdd, _memRemove, _memHas, _memIsDue, _memApplyScore, and
//   initMemorizePage (daily.js) all depend on this schema shape; if the per-verse
//   entry structure changes, every one of those functions must be updated together.
export function _memGet()      { try { return JSON.parse(localStorage.getItem(MEMORY_KEY) || '{}'); } catch (e) { return {}; } }
export function _memSet(state) { try { localStorage.setItem(MEMORY_KEY, JSON.stringify(state)); } catch (e) {} }

export function _memHas(ref) { return !!_memGet()[ref]; }

export function _memAdd(ref) {
  var state = _memGet();
  if (state[ref]) return;
  var today = _memTodayStr();
  state[ref] = { addedDate: today, interval: 1, nextReview: today, score: 0, reps: 0 };
  _memSet(state);
}

export function _memRemove(ref) {
  var state = _memGet();
  delete state[ref];
  _memSet(state);
}

export function _memTodayStr() {
  var d = new Date();
  return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2);
}

export function _memIsDue(entry) {
  return _memTodayStr() >= entry.nextReview;
}

export function _memApplyScore(entry, score) {
  var interval = entry.interval || 1;
  if      (score === 0) interval = 1;
  else if (score === 1) interval = Math.max(1, Math.ceil(interval * 1.2));
  else if (score === 2) interval = Math.max(2, Math.ceil(interval * 2.5));
  else                  interval = Math.max(4, Math.ceil(interval * 3.5));
  var next = new Date();
  next.setDate(next.getDate() + interval);
  entry.interval   = interval;
  entry.nextReview = next.getFullYear() + '-' + ('0' + (next.getMonth() + 1)).slice(-2) + '-' + ('0' + next.getDate()).slice(-2);
  entry.score      = score;
  entry.reps       = (entry.reps || 0) + 1;
  return entry;
}

export function _memDaysUntil(dateStr) {
  var today = new Date();
  today = new Date(today.getFullYear(), today.getMonth(), today.getDate());
  var target = new Date(dateStr + 'T00:00:00');
  return Math.max(0, Math.ceil((target - today) / 86400000));
}

export function _memNormalizeTag(t) {
  return t.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

export function _memAllTags() {
  var state = _memGet();
  var seen  = Object.create(null);
  Object.keys(state).forEach(function (r) {
    (state[r].tags || []).forEach(function (t) { seen[t] = true; });
  });
  return Object.keys(seen).sort();
}

export function _memTagAdd(ref, rawTag) {
  var tag   = _memNormalizeTag(rawTag);
  if (!tag) return;
  var state = _memGet();
  if (!state[ref]) return;
  var tags  = state[ref].tags || [];
  if (tags.indexOf(tag) === -1) tags.push(tag);
  state[ref].tags = tags;
  _memSet(state);
}

export function _memTagRemove(ref, tag) {
  var state = _memGet();
  if (!state[ref]) return;
  state[ref].tags = (state[ref].tags || []).filter(function (t) { return t !== tag; });
  _memSet(state);
}

export function _memRefreshModalBtn(ref) {
  var modalEl = document.querySelector('.bsw-modal');
  var btn = modalEl && modalEl.querySelector('.bsw-modal__memory-btn');
  if (!btn) return;
  var has = _memHas(ref);
  btn.textContent = has ? '⭐ Memorizing' : '☆ Memorize';
  btn.classList.toggle('bsw-modal__memory-btn--active', has);
  btn._memRef = ref;
}
