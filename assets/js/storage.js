/* storage.js — Notes, highlights, bookmarks, history, streak, reading plans state */
'use strict';

import { NOTES_KEY, BOOKMARKS_KEY, parseRef } from './core.js';

// ── Notes & highlights (legacy v1) ────────────────────────────────────────
export var _HL_COLORS = ['yellow','orange','pink','red','purple','lavender','green','teal','blue','mint'];

export function getNotes() {
  try { return JSON.parse(localStorage.getItem(NOTES_KEY) || '{}'); }
  catch (e) { return {}; }
}
export function getNote(refStr) {
  return getNotes()[refStr] || null;
}
export function saveNote(refStr, data) {
  var all = getNotes();
  if (data === null || (!data.highlight && !data.note && !(data.tags && data.tags.length))) {
    delete all[refStr];
  } else {
    all[refStr] = data;
  }
  localStorage.setItem(NOTES_KEY, JSON.stringify(all));
}
export function toggleHighlight(refStr, color) {
  color = color || 'yellow';
  var n = getNote(refStr) || {};
  n.highlight = (n.highlight === color) ? false : color;
  saveNote(refStr, n);
  return n.highlight;
}
export function getTags(refStr) {
  var n = getNote(refStr);
  return (n && Array.isArray(n.tags)) ? n.tags : [];
}
export function addTag(refStr, tag) {
  tag = tag.toLowerCase().trim();
  if (!tag) return;
  var n    = getNote(refStr) || {};
  var tags = Array.isArray(n.tags) ? n.tags : [];
  if (tags.indexOf(tag) === -1) tags.push(tag);
  n.tags = tags;
  saveNote(refStr, n);
}
export function removeTag(refStr, tag) {
  var n = getNote(refStr);
  if (!n || !Array.isArray(n.tags)) return;
  n.tags = n.tags.filter(function (t) { return t !== tag; });
  saveNote(refStr, n);
}

// ── Notes v2 — verse-range-aware, timestamped ─────────────────────────────
var NOTES_V2_KEY    = 'bsw_notes_v2';
var _notesV2Counter = 0;

function _getNotesV2() {
  try { return JSON.parse(localStorage.getItem(NOTES_V2_KEY) || '[]'); }
  catch (e) { return []; }
}
function _saveNotesV2(arr) { localStorage.setItem(NOTES_V2_KEY, JSON.stringify(arr)); }

function _migrateOldNotes() {
  if (localStorage.getItem(NOTES_V2_KEY + '_migrated')) return;
  var old      = getNotes();
  var migrated = _getNotesV2();
  var now      = Date.now();
  Object.keys(old).forEach(function (refStr) {
    var d = old[refStr];
    if (!d || !d.note) return;
    var p = parseRef(refStr);
    if (!p) return;
    migrated.push({
      id: 'n_' + now + '_' + (_notesV2Counter++),
      bookId: p.bookId, ch: +p.ch, v: +p.v,
      endCh: null, endV: null,
      display: p.display || refStr,
      text: d.note, created: now, updated: now
    });
  });
  _saveNotesV2(migrated);
  localStorage.setItem(NOTES_V2_KEY + '_migrated', '1');
}

export function createNoteV2(parsed, text) {
  var arr  = _getNotesV2();
  var note = {
    id: 'n_' + Date.now() + '_' + (_notesV2Counter++),
    bookId: parsed.bookId, ch: +parsed.ch, v: +parsed.v,
    endCh: parsed.endCh ? +parsed.endCh : null, endV: parsed.endV ? +parsed.endV : null,
    display: parsed.display || (parsed.bookName + ' ' + parsed.ch + ':' + parsed.v),
    text: text, created: Date.now(), updated: Date.now()
  };
  arr.push(note);
  _saveNotesV2(arr);
  return note;
}
export function updateNoteV2(id, text) {
  var arr = _getNotesV2();
  arr.forEach(function (n) { if (n.id === id) { n.text = text; n.updated = Date.now(); } });
  _saveNotesV2(arr);
}
export function deleteNoteV2(id) {
  _saveNotesV2(_getNotesV2().filter(function (n) { return n.id !== id; }));
}
export function getNotesForVerse(bookId, ch, v) {
  return _getNotesV2().filter(function (note) {
    if (note.bookId !== bookId) return false;
    if (!note.endCh && !note.endV) return note.ch === +ch && note.v === +v;
    var pos   = +ch * 1000 + +v;
    var start = note.ch * 1000 + note.v;
    var end   = (note.endCh || note.ch) * 1000 + (note.endV || note.v);
    return pos >= start && pos <= end;
  });
}
export function getNotesForChapter(bookId, ch) {
  return _getNotesV2().filter(function (note) {
    return note.bookId === bookId && note.ch === +ch;
  });
}
export function hasNotesForVerse(bookId, ch, v) {
  return getNotesForVerse(bookId, ch, v).length > 0;
}
export function _noteRelTime(ts) {
  var d = Date.now() - ts;
  if (d < 60000)     return 'just now';
  if (d < 3600000)   return Math.floor(d / 60000)    + 'm ago';
  if (d < 86400000)  return Math.floor(d / 3600000)  + 'h ago';
  if (d < 604800000) return Math.floor(d / 86400000) + 'd ago';
  return new Date(ts).toLocaleDateString();
}

// ── Storage schema versioning & migration ─────────────────────────────────
var BSW_STORAGE_V     = 1;
var BSW_STORAGE_V_KEY = 'bsw_storage_v';

export function _runStorageMigrations() {
  try {
    var storedV = parseInt(localStorage.getItem(BSW_STORAGE_V_KEY) || '0', 10);
    if (storedV >= BSW_STORAGE_V) return;
    if (storedV < 1) {
      _migrateOldNotes();
      storedV = 1;
    }
    localStorage.setItem(BSW_STORAGE_V_KEY, String(BSW_STORAGE_V));
  } catch (e) { /* non-fatal */ }
}

// ── Bookmarks ─────────────────────────────────────────────────────────────
export function getBookmarks() {
  try { return JSON.parse(localStorage.getItem(BOOKMARKS_KEY) || '[]'); }
  catch (e) { return []; }
}
export function isBookmarked(refStr) {
  return getBookmarks().indexOf(refStr) !== -1;
}
export function toggleBookmark(refStr) {
  var list = getBookmarks();
  var idx  = list.indexOf(refStr);
  if (idx === -1) { list.unshift(refStr); }
  else            { list.splice(idx, 1);  }
  localStorage.setItem(BOOKMARKS_KEY, JSON.stringify(list));
  return idx === -1;
}

// ── History ───────────────────────────────────────────────────────────────
var HISTORY_KEY = 'bsw_history';
var STREAK_KEY  = 'bsw_streak';

export function _historyPush(ref) {
  try {
    var arr = JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]');
    arr = arr.filter(function (r) { return r !== ref; });
    arr.unshift(ref);
    if (arr.length > 100) arr.length = 100;
    localStorage.setItem(HISTORY_KEY, JSON.stringify(arr));
  } catch (e) { /* ignore */ }
}
export function _historyGet() {
  try { return JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]'); }
  catch (e) { return []; }
}

export function _streakTodayStr() {
  var d = new Date();
  return d.getFullYear() + '-' +
    String(d.getMonth() + 1).padStart(2, '0') + '-' +
    String(d.getDate()).padStart(2, '0');
}
export function _recordReadingDay() {
  try {
    var data  = JSON.parse(localStorage.getItem(STREAK_KEY) || '{"days":[]}');
    var today = _streakTodayStr();
    if (data.days.indexOf(today) === -1) {
      data.days.push(today);
      data.days.sort();
      if (data.days.length > 400) data.days = data.days.slice(-400);
      localStorage.setItem(STREAK_KEY, JSON.stringify(data));
    }
  } catch (e) { /* ignore */ }
}

export function initHistoryWidget() {
  var el = document.getElementById('bsw-history');
  if (!el) return;
  var hist = _historyGet();
  if (!hist.length) { el.setAttribute('hidden', ''); return; }
  el.removeAttribute('hidden');
  el.innerHTML = '<h2>Recently Viewed</h2><div class="history-chips">' +
    hist.slice(0, 20).map(function (ref) {
      return '<a class="history-chip ref" data-ref="' + ref + '">' + ref + '</a>';
    }).join('') +
    '</div>';
}
