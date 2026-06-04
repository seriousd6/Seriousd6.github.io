/* library.js — Topical, Dictionary, Library pages and modal tabs */
'use strict';

import {
  READER_URL, FATHER_SLUGS, escHtml,
  _torreyLoad, _torreyData, _torreyMap, _torreyByLetter,
  _torreyLoadVidx, _torreyTopicsForVerse,
  _torreyVidxCache,
  _smithLoad, _smithData, _smithMap, _smithByLetter, _smithEntryCache, _smithLoadEntry,
  _isbeLoad, _isbeData, _isbeMap, _isbeByLetter, _isbeEntryCache, _isbeLoadEntry,
  _hitchLoad, _hitchData, _hitchMap, _hitchByLetter,
  _loadLibDoc, _loadLibIndex,
  _resolve
} from './core.js';
import { wireRefLinks } from './wire.js';

// ── Nave constants ──────────────────────────────────────────────────────────
export var DICT_PAGE_URL = _resolve('../../dictionary/');

var NAVE_URL       = _resolve('../../data/topical/nave.json');
var NAVE_VIDX_ROOT = _resolve('../../data/topical/verse-index');

export var _naveData     = null;
export var _naveMap      = null;
export var _naveByLetter = null;
var _naveLoading   = null;
var _naveVidxCache = {};

export function _naveLoad() {
  if (_naveLoading) return _naveLoading;
  _naveLoading = fetch(NAVE_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      _naveData = data;
      _naveMap  = {};
      _naveByLetter = {};
      data.forEach(function (t) {
        _naveMap[t.slug] = t;
        var letter = t.title.charAt(0).toUpperCase();
        if (!_naveByLetter[letter]) _naveByLetter[letter] = [];
        _naveByLetter[letter].push(t);
      });
    });
  return _naveLoading;
}

function _naveLoadVidx(bookId) {
  if (_naveVidxCache[bookId] !== undefined) return Promise.resolve(_naveVidxCache[bookId]);
  return fetch(NAVE_VIDX_ROOT + '/' + bookId + '.json')
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { _naveVidxCache[bookId] = d || {}; return _naveVidxCache[bookId]; })
    .catch(function () { _naveVidxCache[bookId] = {}; return {}; });
}

function _naveTopicsForVerse(parsed) {
  if (!parsed || !parsed.bookId || !parsed.v) return Promise.resolve([]);
  return Promise.all([_naveLoad(), _naveLoadVidx(parsed.bookId)]).then(function () {
    var key   = parsed.ch + ':' + parsed.v;
    var vidx  = _naveVidxCache[parsed.bookId] || {};
    var slugs = vidx[key] || [];
    return slugs.map(function (s) { return _naveMap && _naveMap[s]; }).filter(Boolean);
  });
}

// ── Easton's Dictionary ───────────────────────────────────────────────────────
var DICT_IDX_URL   = _resolve('../../data/dictionary/index.json');
var DICT_ENTRY_URL = _resolve('../../data/dictionary/');
var DICT_VIDX_URL  = _resolve('../../data/dictionary/verse-index/');

// ── Smith's verse-index ───────────────────────────────────────────────────────
var SMITH_VIDX_URL  = _resolve('../../data/smith/verse-index/');
var _smithVidxCache = {};

// ── ISBE verse-index ─────────────────────────────────────────────────────────
var ISBE_VIDX_URL  = _resolve('../../data/isbe/verse-index/');
var _isbeVidxCache = {};

export var _dictData      = null;
export var _dictMap       = null;
var _dictByLetter  = null;
var _dictLoading   = null;
var _dictEntryCache = {};
var _dictVidxCache  = {};

export function _dictLoad() {
  if (_dictLoading) return _dictLoading;
  _dictLoading = fetch(DICT_IDX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      _dictData     = data;
      _dictMap      = {};
      _dictByLetter = {};
      data.forEach(function (e) {
        _dictMap[e.id] = e;
        var letter = e.term.charAt(0).toUpperCase();
        if (!_dictByLetter[letter]) _dictByLetter[letter] = [];
        _dictByLetter[letter].push(e);
      });
    });
  return _dictLoading;
}

function _dictLoadEntry(slug) {
  if (_dictEntryCache[slug]) return Promise.resolve(_dictEntryCache[slug]);
  return fetch(DICT_ENTRY_URL + slug + '.json')
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (d) { _dictEntryCache[slug] = d; return d; });
}

function _dictLoadVidx(bookId) {
  if (_dictVidxCache[bookId] !== undefined) return Promise.resolve(_dictVidxCache[bookId]);
  return fetch(DICT_VIDX_URL + bookId + '.json')
    .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
    .then(function (d) { _dictVidxCache[bookId] = d || {}; return d; })
    .catch(function () { _dictVidxCache[bookId] = {}; return {}; });
}

function _smithLoadVidx(bookId) {
  if (_smithVidxCache[bookId] !== undefined) return Promise.resolve(_smithVidxCache[bookId]);
  return fetch(SMITH_VIDX_URL + bookId + '.json')
    .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
    .then(function (d) { _smithVidxCache[bookId] = d || {}; return d; })
    .catch(function () { _smithVidxCache[bookId] = {}; return {}; });
}

function _isbeLoadVidx(bookId) {
  if (_isbeVidxCache[bookId] !== undefined) return Promise.resolve(_isbeVidxCache[bookId]);
  return fetch(ISBE_VIDX_URL + bookId + '.json')
    .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
    .then(function (d) { _isbeVidxCache[bookId] = d || {}; return d; })
    .catch(function () { _isbeVidxCache[bookId] = {}; return {}; });
}

// INTENT: Loads per-verse dictionary entries from Easton, Smith, and ISBE verse indexes,
//   deduplicating by source:id so the verse modal shows each matching article once.
// CHANGE? Adding a new dictionary source requires: (1) a vidx loader function, (2) a new
//   Promise in Promise.all, (3) a forEach block here, and (4) the source key in library.js
//   display/render code (the badge lookup in renderModalDict and initDictionaryPage).
// VERIFY: Open verse modal for Genesis 1:1; Dictionary tab should list entries from all three
//   sources (E badge, S badge, IS badge) when relevant articles exist.
export function _dictEntriesForVerse(parsed) {
  if (!parsed || !parsed.bookId || !parsed.ch || !parsed.v) return Promise.resolve([]);
  var ch = String(parsed.ch);
  var v  = String(parsed.v);
  return Promise.all([_dictLoadVidx(parsed.bookId), _smithLoadVidx(parsed.bookId), _isbeLoadVidx(parsed.bookId)])
    .then(function (results) {
      var eastonVidx = results[0];
      var smithVidx  = results[1];
      var isbeVidx   = results[2];
      var entries = [];
      var seen = {};
      ((eastonVidx[ch] && eastonVidx[ch][v]) || []).forEach(function (e) {
        var key = 'easton:' + e.id;
        if (!seen[key]) { seen[key] = true; entries.push({ id: e.id, term: e.term, source: 'easton' }); }
      });
      ((smithVidx[ch] && smithVidx[ch][v]) || []).forEach(function (e) {
        var key = 'smith:' + e.id;
        if (!seen[key]) { seen[key] = true; entries.push({ id: e.id, term: e.term, source: 'smith' }); }
      });
      ((isbeVidx[ch] && isbeVidx[ch][v]) || []).forEach(function (e) {
        var key = 'isbe:' + e.id;
        if (!seen[key]) { seen[key] = true; entries.push({ id: e.id, term: e.term, source: 'isbe' }); }
      });
      return entries;
    });
}

// ── Library verse-index ───────────────────────────────────────────────────────
var _LIB_VERSE_IDX_BASE = _resolve('../../data/library/verse-index');
var _libVerseCache      = {};

export function loadLibVerseIndex(bookId) {
  if (_libVerseCache[bookId]) return Promise.resolve(_libVerseCache[bookId]);
  var url = _LIB_VERSE_IDX_BASE + '/' + bookId + '.json';
  return fetch(url)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (d) { _libVerseCache[bookId] = d; return d; })
    .catch(function () { _libVerseCache[bookId] = {}; return {}; });
}

// ── Topical modal tab ─────────────────────────────────────────────────────────
export function renderModalTopics(parsed, container) {
  container.innerHTML = '<p class="topical-modal-empty">Loading…</p>';
  Promise.all([_naveTopicsForVerse(parsed), _torreyTopicsForVerse(parsed)]).then(function (results) {
    var naveTopics   = results[0];
    var torreyTopics = results[1];
    var html = '';

    if (naveTopics.length) {
      var label = naveTopics.length === 1 ? '1 topic' : naveTopics.length + ' topics';
      html += '<p class="topical-modal-meta">' +
        '<span>' + label + ' in Nave\'s</span>' +
        '<a class="topical-modal-browse" href="' + escHtml(DICT_PAGE_URL) + '">Browse all →</a>' +
        '</p><div class="topical-modal-chips">';
      naveTopics.forEach(function (t) {
        html += '<a class="topical-modal-chip" href="' +
          escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(t.slug) + '&src=nave') + '">' +
          escHtml(t.title) +
          '<span class="topical-modal-chip__count">' + t.verses.length + '</span></a>';
      });
      html += '</div>';
    }

    if (torreyTopics.length) {
      var tlabel = torreyTopics.length === 1 ? '1 topic' : torreyTopics.length + ' topics';
      html += '<p class="topical-modal-meta topical-modal-meta--torrey">' +
        '<span>' + tlabel + ' in Torrey\'s</span>' +
        '<a class="topical-modal-browse" href="' + escHtml(DICT_PAGE_URL) + '">Browse →</a>' +
        '</p><div class="topical-modal-chips">';
      torreyTopics.forEach(function (t) {
        html += '<a class="topical-modal-chip" href="' +
          escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(t.slug) + '&src=torrey') + '">' +
          escHtml(t.title) +
          '<span class="topical-modal-chip__count">' + (t.verses ? t.verses.length : '') + '</span></a>';
      });
      html += '</div>';
    }

    if (!html) {
      html = '<p class="topical-modal-empty">No topics found for this verse.</p>';
    }
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML = '<p class="topical-modal-empty">Could not load topic data.</p>';
  });
  container._topicsLoaded = true;
}

// ── Confessions modal tab ─────────────────────────────────────────────────────
export function renderModalConfessions(parsed, container) {
  container._confLoaded = true;
  if (!parsed || !parsed.bookId) {
    container.innerHTML = '<p class="bsw-modal-topics-empty">No verse selected.</p>';
    return;
  }
  container.innerHTML = '<p class="bsw-modal-topics-empty">Loading…</p>';

  loadLibVerseIndex(parsed.bookId).then(function (data) {
    var ch  = String(parsed.ch);
    var v   = String(parsed.v);
    var all = (data[ch] && data[ch][v]) || [];
    var citations = all.filter(function (c) { return !FATHER_SLUGS[c.slug]; });
    if (!citations.length) {
      container.innerHTML = '<p class="bsw-modal-topics-empty">No confessional citations for this verse.</p>';
      return;
    }
    var byDoc = {};
    citations.forEach(function (c) {
      if (!byDoc[c.doc]) byDoc[c.doc] = [];
      byDoc[c.doc].push(c);
    });
    var html = '<div class="bsw-modal-confessions">';
    Object.keys(byDoc).forEach(function (doc) {
      html += '<div class="bsw-conf-group">';
      html += '<div class="bsw-conf-group__doc">' + escHtml(doc) + '</div>';
      byDoc[doc].forEach(function (c) {
        var refLabel = c.doc + ' ' + c.section;
        var href = READER_URL + '?ref=' + encodeURIComponent(refLabel);
        html += '<a class="bsw-conf-item" href="' + escHtml(href) + '">' +
          '<span class="bsw-conf-item__ref">' + escHtml(refLabel) + '</span>' +
          '<span class="bsw-conf-item__text">' + escHtml(c.heading) + '</span>' +
        '</a>';
      });
      html += '</div>';
    });
    html += '</div>';
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML = '<p class="bsw-modal-topics-empty">Could not load confessional data.</p>';
  });
}

// ── Church Fathers modal tab ──────────────────────────────────────────────────
var _LIB_FATHER_URL = _resolve('../../library/');

export function renderModalFathers(parsed, container) {
  container._fathersLoaded = true;
  if (!parsed || !parsed.bookId) {
    container.innerHTML = '<p class="bsw-modal-topics-empty">No verse selected.</p>';
    return;
  }
  container.innerHTML = '<p class="bsw-modal-topics-empty">Loading…</p>';

  loadLibVerseIndex(parsed.bookId).then(function (data) {
    var ch  = String(parsed.ch);
    var v   = String(parsed.v);
    var all = (data[ch] && data[ch][v]) || [];
    var citations = all.filter(function (c) { return !!FATHER_SLUGS[c.slug]; });
    if (!citations.length) {
      container.innerHTML = '<p class="bsw-modal-topics-empty">No Church Father citations for this verse.</p>';
      return;
    }
    var bySlug = {};
    var slugOrder = [];
    citations.forEach(function (c) {
      if (!bySlug[c.slug]) { bySlug[c.slug] = []; slugOrder.push(c.slug); }
      bySlug[c.slug].push(c);
    });
    var html = '<div class="bsw-modal-fathers">';
    slugOrder.forEach(function (slug) {
      var fatherName = FATHER_SLUGS[slug] || slug;
      html += '<div class="bsw-father-group">';
      html += '<div class="bsw-father-group__name">' + escHtml(fatherName) + '</div>';
      bySlug[slug].forEach(function (c) {
        var href = _LIB_FATHER_URL + escHtml(slug) + '/#ch' + encodeURIComponent(c.section);
        html += '<a class="bsw-father-item" href="' + href + '">' +
          '<span class="bsw-father-item__section">' + escHtml(c.heading) + '</span>' +
        '</a>';
      });
      html += '</div>';
    });
    html += '</div>';
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML = '<p class="bsw-modal-topics-empty">Could not load Church Father data.</p>';
  });
}

// ── Topical section in Verse Study page ───────────────────────────────────────
export function renderVSTopics(parsed, container) {
  container.innerHTML = '<p class="topical-modal-empty">Loading…</p>';
  _naveTopicsForVerse(parsed).then(function (topics) {
    if (!topics.length) {
      container.innerHTML = '<p class="topical-modal-empty">No Nave\'s topics for this verse.</p>';
      return;
    }
    var html = '<div class="vs-topical-list">';
    topics.forEach(function (t) {
      html += '<a class="vs-topical-item" href="' +
        escHtml(DICT_PAGE_URL + '?entry=' + encodeURIComponent(t.slug) + '&src=nave') + '">' +
        escHtml(t.title) +
        '<span class="vs-topical-count">' + t.verses.length + '</span>' +
        '</a>';
    });
    html += '</div>';
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML = '<p class="topical-modal-empty">Could not load topic data.</p>';
  });
}

// ── Dictionary — Verse Study section ─────────────────────────────────────────
export function renderVSDictionary(parsed, container) {
  container.innerHTML = '<p class="dict-modal-empty">Loading…</p>';
  _dictEntriesForVerse(parsed).then(function (entries) {
    if (!entries.length) {
      container.innerHTML = '<p class="dict-modal-empty">No dictionary entries for this verse.</p>';
      return;
    }
    var html = '<div class="vs-dict-list">';
    entries.forEach(function (e) {
      var src = e.source;
      var href = src === 'smith'
        ? DICT_PAGE_URL + '?src=smith&entry=' + encodeURIComponent(e.id)
        : src === 'isbe'
          ? DICT_PAGE_URL + '?src=isbe&entry=' + encodeURIComponent(e.id)
          : DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id);
      var badge      = src === 'smith' ? 'S' : src === 'isbe' ? 'IS' : 'E';
      var badgeColor = src === 'smith' ? '#1d4ed8' : src === 'isbe' ? '#1e3a5f' : '#7c3aed';
      html += '<a class="vs-dict-item" href="' + escHtml(href) + '">' +
        '<span class="vs-dict-src-badge" style="background:' + badgeColor + '">' + badge + '</span>' +
        '<span class="vs-dict-item__term">' + escHtml(e.term) + '</span>' +
        '<span class="vs-dict-item__arrow">&#x2192;</span>' +
        '</a>';
    });
    html += '</div>';
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML = '<p class="dict-modal-empty">Could not load dictionary data.</p>';
  });
}

// ── Dictionary modal tab ──────────────────────────────────────────────────────
export function renderModalDictionary(parsed, container) {
  container._dictLoaded = true;
  if (!parsed || !parsed.v) {
    container.innerHTML = '<p class="dict-modal-empty">No verse selected.</p>';
    return;
  }
  container.innerHTML = '<p class="dict-modal-empty">Loading…</p>';
  _dictEntriesForVerse(parsed).then(function (entries) {
    if (!entries.length) {
      container.innerHTML = '<p class="dict-modal-empty">No dictionary entries for this verse.</p>';
      return;
    }
    var html = '';
    entries.forEach(function (e) {
      var src    = e.source;
      var href   = src === 'smith'
        ? DICT_PAGE_URL + '?src=smith&entry=' + encodeURIComponent(e.id)
        : src === 'isbe'
          ? DICT_PAGE_URL + '?src=isbe&entry=' + encodeURIComponent(e.id)
          : DICT_PAGE_URL + '?entry=' + encodeURIComponent(e.id);
      var meta   = src === 'smith' ? (_smithMap && _smithMap[e.id])
                 : src === 'isbe'  ? (_isbeMap  && _isbeMap[e.id])
                 : (_dictMap && _dictMap[e.id]);
      var badge      = src === 'smith' ? 'S' : src === 'isbe' ? 'IS' : 'E';
      var badgeColor = src === 'smith' ? '#1d4ed8' : src === 'isbe' ? '#1e3a5f' : '#7c3aed';
      var brief = meta ? meta.brief : '';
      if (brief) {
        var dot = brief.indexOf('. ', 40);
        if (dot > 0 && dot < 140) brief = brief.slice(0, dot + 1);
        else if (brief.length > 130) brief = brief.slice(0, 127) + '…';
      }
      html += '<div class="bsw-dict-panel-entry">' +
        '<p class="bsw-dict-panel-entry__term">' +
        '<span class="vs-dict-src-badge" style="background:' + badgeColor + '">' + badge + '</span>' +
        escHtml(e.term) + '</p>' +
        (brief ? '<p class="bsw-dict-panel-entry__brief">' + escHtml(brief) + '</p>' : '') +
        '<a class="bsw-dict-panel-entry__link" href="' + escHtml(href) + '">Full entry &#x2192;</a>' +
        '</div>';
    });
    html += '<p style="margin-top:.75rem;font-size:.75rem;">' +
      '<a class="bsw-dict-panel-entry__link" href="' + escHtml(DICT_PAGE_URL) + '">Browse full dictionary &#x2192;</a></p>';
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML = '<p class="dict-modal-empty">Could not load dictionary data.</p>';
  });
}

// ── Dictionary omni-search page ───────────────────────────────────────────────
export function initDictionaryPage() {
  var listEl      = document.getElementById('dict-list');
  var loadingEl   = document.getElementById('dict-loading');
  var emptyEl     = document.getElementById('dict-empty');
  var detailColEl = document.getElementById('dict-detail-col');
  var detailEl    = document.getElementById('dict-detail');
  var alphaEl     = document.getElementById('dict-alpha');
  var searchEl    = document.getElementById('dict-search');
  var countEl     = document.getElementById('dict-search-count');
  var filtersEl   = document.getElementById('dict-source-filters');
  if (!listEl) return;

  var _activeLetter  = null;
  var _activeItemKey = null;
  var _omniIndex    = {};
  var _omniByLetter = {};

  var OMNI_SOURCES = [
    {
      key: 'easton',    label: "Easton's",   badge: 'E',  badgeColor: '#7c3aed',
      type: 'dict',     meta: "Easton's Bible Dictionary (M.G. Easton, 1897)",
      load: function () { return _dictLoad(); },
      getData: function () { return { data: _dictData,  map: _dictMap,  byLetter: _dictByLetter  }; },
      loadEntry: function (id) { return _dictLoadEntry(id); }
    },
    {
      key: 'smith',     label: "Smith's",    badge: 'S',  badgeColor: '#1d4ed8',
      type: 'dict',     meta: "Smith's Bible Dictionary (William Smith, 1884)",
      load: function () { return _smithLoad(); },
      getData: function () { return { data: _smithData, map: _smithMap, byLetter: _smithByLetter }; },
      loadEntry: function (id) { return _smithLoadEntry(id); }
    },
    {
      key: 'isbe',      label: 'ISBE',       badge: 'IS', badgeColor: '#1e3a5f',
      type: 'dict',     meta: "Int'l Standard Bible Encyclopaedia (James Orr ed., 1915)",
      load: function () { return _isbeLoad(); },
      getData: function () { return { data: _isbeData,  map: _isbeMap,  byLetter: _isbeByLetter  }; },
      loadEntry: function (id) { return _isbeLoadEntry(id); }
    },
    {
      key: 'hitchcock', label: 'Names',      badge: 'N',  badgeColor: '#065f46',
      type: 'names',    meta: "Hitchcock's Bible Names (Roswell Hitchcock, 1874)",
      load: function () { return _hitchLoad(); },
      getData: function () { return { data: _hitchData, map: _hitchMap, byLetter: _hitchByLetter }; }
    },
    {
      key: 'nave',      label: "Nave's",     badge: 'NV', badgeColor: '#b45309',
      type: 'topical',  meta: "Nave's Topical Bible (Orville Nave, 1896)",
      load: function () { return _naveLoad(); },
      getData: function () { return { data: _naveData,  map: _naveMap,  byLetter: _naveByLetter  }; }
    },
    {
      key: 'torrey',    label: "Torrey's",   badge: 'TR', badgeColor: '#be123c',
      type: 'topical',  meta: "Torrey's Topical Textbook (R.A. Torrey, 1897)",
      load: function () { return _torreyLoad(); },
      getData: function () { return { data: _torreyData, map: _torreyMap, byLetter: _torreyByLetter }; }
    }
  ];

  function _findSrc(key) {
    for (var i = 0; i < OMNI_SOURCES.length; i++) {
      if (OMNI_SOURCES[i].key === key) return OMNI_SOURCES[i];
    }
    return null;
  }

  var _enabled = {};
  OMNI_SOURCES.forEach(function (s) { _enabled[s.key] = true; });

  if (filtersEl) {
    OMNI_SOURCES.forEach(function (src) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'dict-filter-chip dict-filter-chip--on';
      btn.dataset.src = src.key;
      btn.innerHTML =
        '<span class="dict-filter-chip__badge" style="background:' + src.badgeColor + '">' +
          escHtml(src.badge) +
        '</span>' + escHtml(src.label);
      btn.addEventListener('click', function () {
        _enabled[src.key] = !_enabled[src.key];
        btn.classList.toggle('dict-filter-chip--on', _enabled[src.key]);
        var q = searchEl ? searchEl.value.trim().toLowerCase() : '';
        if (q) { _doSearch(q); } else { _refreshLetter(); }
      });
      filtersEl.appendChild(btn);
    });
  }

  function _normalKey(s) {
    return s.toLowerCase().replace(/[',\-\.]/g, '').replace(/\s+/g, ' ').trim();
  }

  function _buildOmniIndex() {
    var idx = {};
    OMNI_SOURCES.forEach(function (src) {
      var d = src.getData();
      if (!d.data) return;
      d.data.forEach(function (e) {
        var label = e.term || e.title || '';
        var nkey  = _normalKey(label);
        if (!nkey) return;
        if (!idx[nkey]) {
          idx[nkey] = { key: nkey, label: label, letter: label.charAt(0).toUpperCase(), allSources: [] };
        } else {
          var cur = idx[nkey].label;
          if (cur === cur.toUpperCase() && label !== label.toUpperCase()) {
            idx[nkey].label = label;
          }
        }
        idx[nkey].allSources.push({ srcKey: src.key, entry: e });
      });
    });
    _omniIndex = idx;
    var byl = {};
    Object.keys(idx).forEach(function (nkey) {
      var item = idx[nkey];
      var l = item.letter;
      if (!byl[l]) byl[l] = [];
      byl[l].push(item);
    });
    Object.keys(byl).forEach(function (l) {
      byl[l].sort(function (a, b) { return a.label.localeCompare(b.label); });
    });
    _omniByLetter = byl;
  }

  function _hasEnabledSource(item) {
    for (var i = 0; i < item.allSources.length; i++) {
      if (_enabled[item.allSources[i].srcKey]) return true;
    }
    return false;
  }

  function _omniCoverage() {
    var cov = {};
    Object.keys(_omniByLetter).forEach(function (l) {
      for (var i = 0; i < _omniByLetter[l].length; i++) {
        if (_hasEnabledSource(_omniByLetter[l][i])) { cov[l] = true; break; }
      }
    });
    return cov;
  }

  function _getLetterItems(letter) {
    return (_omniByLetter[letter] || []).filter(_hasEnabledSource);
  }

  function _searchItems(q) {
    var results = [];
    Object.keys(_omniIndex).forEach(function (nkey) {
      var item = _omniIndex[nkey];
      if (!_hasEnabledSource(item)) return;
      var hay = item.label.toLowerCase();
      item.allSources.forEach(function (s) {
        if (_enabled[s.srcKey]) {
          hay += ' ' + (s.entry.brief || s.entry.meaning || '').toLowerCase();
        }
      });
      if (hay.indexOf(q) !== -1) results.push(item);
    });
    results.sort(function (a, b) { return a.label.localeCompare(b.label); });
    return results;
  }

  function buildAlphaBar() {
    var cov = _omniCoverage();
    alphaEl.innerHTML = '';
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach(function (letter) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'dict-alpha-btn' +
        (letter === _activeLetter ? ' dict-alpha-btn--active' : '') +
        (!cov[letter] ? ' dict-alpha-btn--empty' : '');
      btn.textContent = letter;
      if (cov[letter]) {
        btn.addEventListener('click', function () {
          if (searchEl) { searchEl.value = ''; }
          if (countEl)  { countEl.setAttribute('hidden', ''); }
          _showLetter(letter);
        });
      }
      alphaEl.appendChild(btn);
    });
  }

  function _showLetter(letter) {
    _activeLetter = letter;
    alphaEl.querySelectorAll('.dict-alpha-btn').forEach(function (b) {
      b.classList.toggle('dict-alpha-btn--active', b.textContent === letter);
    });
    renderList(_getLetterItems(letter));
  }

  function _showFirstLetter() {
    var cov   = _omniCoverage();
    var first = Object.keys(cov).sort()[0] || 'A';
    _activeLetter = first;
    buildAlphaBar();
    renderList(_getLetterItems(first));
  }

  function _refreshLetter() {
    buildAlphaBar();
    if (_activeLetter) { renderList(_getLetterItems(_activeLetter)); }
    else { _showFirstLetter(); }
  }

  function _srcBadgesHtml(item) {
    var out = '';
    item.allSources.forEach(function (s) {
      if (!_enabled[s.srcKey]) return;
      var src = _findSrc(s.srcKey);
      if (src) out += '<span class="dict-item__src" style="background:' + src.badgeColor + '">' + escHtml(src.badge) + '</span>';
    });
    return out;
  }

  function renderList(items) {
    if (!items || !items.length) {
      listEl.innerHTML = '';
      emptyEl.removeAttribute('hidden');
      return;
    }
    emptyEl.setAttribute('hidden', '');
    listEl.innerHTML = items.map(function (item) {
      return '<div class="dict-item' + (item.key === _activeItemKey ? ' dict-item--active' : '') +
        '" data-key="' + escHtml(item.key) + '">' +
        '<span class="dict-item__badges">' + _srcBadgesHtml(item) + '</span>' +
        '<span class="dict-item__title">' + escHtml(item.label) + '</span>' +
        '</div>';
    }).join('');
    listEl.querySelectorAll('.dict-item').forEach(function (el) {
      el.addEventListener('click', function () {
        var found = _omniIndex[el.dataset.key];
        if (!found) return;
        listEl.querySelectorAll('.dict-item').forEach(function (x) {
          x.classList.remove('dict-item--active');
        });
        el.classList.add('dict-item--active');
        _activeItemKey = found.key;
        showDetail(found);
      });
    });
  }

  function showDetail(item) {
    _activeItemKey = item.key;
    detailColEl.removeAttribute('hidden');
    detailEl.innerHTML =
      '<div class="dict-detail__head">' +
        '<h2 class="dict-detail__title">' + escHtml(item.label) + '</h2>' +
      '</div>' +
      '<div class="dict-detail__sources"></div>';

    var sourcesEl = detailEl.querySelector('.dict-detail__sources');
    var anyVisible = false;

    item.allSources.forEach(function (srcEntry) {
      if (!_enabled[srcEntry.srcKey]) return;
      anyVisible = true;
      var src = _findSrc(srcEntry.srcKey);
      if (!src) return;
      var e = srcEntry.entry;

      var section = document.createElement('div');
      section.className = 'dict-src-section';

      var headHtml =
        '<div class="dict-src-section__head">' +
          '<span class="dict-item__src" style="background:' + src.badgeColor + '">' + escHtml(src.badge) + '</span>' +
          '<span class="dict-src-section__name">' + escHtml(src.meta) + '</span>' +
        '</div>';

      if (src.type === 'names') {
        section.innerHTML =
          headHtml +
          '<div class="dict-src-section__body">' +
            '<p class="dict-detail__meaning">' + escHtml(e.meaning || '') + '</p>' +
          '</div>';
        sourcesEl.appendChild(section);
        return;
      }

      if (src.type === 'topical') {
        var verses    = e.verses || [];
        var chips     = verses.map(function (r) {
          return '<a class="dict-ref-chip ref" data-ref="' + escHtml(r) + '">' + escHtml(r) + '</a>';
        }).join('');
        section.innerHTML =
          headHtml +
          '<div class="dict-src-section__body">' +
            (verses.length
              ? '<p class="dict-detail__refs-label">' + verses.length + ' reference' + (verses.length !== 1 ? 's' : '') + '</p>' +
                '<div class="dict-detail__ref-chips">' + chips + '</div>'
              : '<p class="dict-empty">No verses listed.</p>') +
          '</div>';
        sourcesEl.appendChild(section);
        wireRefLinks(section);
        return;
      }

      section.innerHTML =
        headHtml +
        '<div class="dict-src-section__body"><p class="dict-loading">Loading…</p></div>';
      sourcesEl.appendChild(section);

      var body = section.querySelector('.dict-src-section__body');
      src.loadEntry(e.id || e.slug).then(function (full) {
        var refsHtml = '';
        if (full.refs && full.refs.length) {
          refsHtml =
            '<div class="dict-detail__refs">' +
              '<p class="dict-detail__refs-label">Scripture References</p>' +
              '<div class="dict-detail__ref-chips">' +
              full.refs.map(function (r) {
                return '<a class="dict-ref-chip ref" data-ref="' + escHtml(r) + '">' + escHtml(r) + '</a>';
              }).join('') +
              '</div>' +
            '</div>';
        }
        body.innerHTML = full.html + refsHtml;
        wireRefLinks(body);
      }).catch(function () {
        body.innerHTML = '<p>Could not load entry.</p>';
      });
    });

    if (!anyVisible) {
      sourcesEl.innerHTML = '<p class="dict-empty" style="padding:1rem">No sources enabled for this entry.</p>';
    }
  }

  function _doSearch(q) {
    var results = _searchItems(q);
    _activeLetter = null;
    buildAlphaBar();
    if (countEl) {
      countEl.textContent = results.length + ' result' + (results.length !== 1 ? 's' : '');
      countEl.removeAttribute('hidden');
    }
    renderList(results.slice(0, 300));
  }

  if (searchEl) {
    searchEl.addEventListener('input', function () {
      var q = searchEl.value.trim().toLowerCase();
      if (!q) {
        if (countEl) countEl.setAttribute('hidden', '');
        _refreshLetter();
        return;
      }
      _doSearch(q);
    });
  }

  var _urlParams  = new URLSearchParams(window.location.search);
  var _entryParam = _urlParams.get('entry') || '';
  var _srcParam   = _urlParams.get('src')   || '';

  function _tryShowUrlEntry() {
    if (!_entryParam) return false;
    var found = _omniIndex[_normalKey(_entryParam)];
    if (!found) {
      OMNI_SOURCES.forEach(function (src) {
        if (found) return;
        if (_srcParam && src.key !== _srcParam) return;
        var d = src.getData();
        if (d.map && d.map[_entryParam]) {
          var e = d.map[_entryParam];
          found = _omniIndex[_normalKey(e.term || e.title || '')];
        }
      });
    }
    if (!found) return false;
    _activeLetter = found.letter;
    buildAlphaBar();
    renderList(_getLetterItems(found.letter));
    showDetail(found);
    return true;
  }

  _dictLoad().then(function () {
    if (loadingEl) loadingEl.setAttribute('hidden', '');
    _buildOmniIndex();
    if (!_tryShowUrlEntry()) {
      _showFirstLetter();
      detailEl.innerHTML = '<p class="dict-detail-placeholder">Select an entry to read its definition.</p>';
    }

    ['smith', 'isbe', 'hitchcock', 'nave', 'torrey'].forEach(function (key) {
      var src = _findSrc(key);
      if (!src) return;
      src.load().then(function () {
        _buildOmniIndex();
        buildAlphaBar();
        var q = searchEl ? searchEl.value.trim().toLowerCase() : '';
        if (q) { _doSearch(q); }
        else if (_activeLetter) { renderList(_getLetterItems(_activeLetter)); }
      }).catch(function () {});
    });
  }).catch(function () {
    if (loadingEl) loadingEl.textContent = 'Failed to load dictionary.';
  });
}
