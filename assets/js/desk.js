/* desk.js — the Logos-style work surface (/desk/).
 *
 * Model: a recursive split tree. A node is either a split
 *   { t:'s', id, d:'row'|'col', r:0..1, a:node, b:node }
 * or a panel
 *   { t:'p', id, url, title }        (url === null → resource chooser)
 * The tree drives GEOMETRY ONLY: every panel's DOM (with its iframe) lives
 * flat inside #desk-root, absolutely positioned from the computed rects.
 * Splits, closes, and divider drags never reparent a panel element — moving
 * an iframe in the DOM reloads it, which would wipe a reader's state.
 *
 * Each iframe hosts a normal site page; Base.astro's pre-paint embed
 * bootstrap hides the framed page's chrome, so multiple /read/ panels give
 * genuinely independent Bible readers. Layout persists to localStorage
 * (urls refreshed from each iframe on navigation — same-origin).
 */
'use strict';

import { resourcePrefix } from './desk-frame.js';

var LS_KEY  = 'bsw_desk_layout_v1';
var GUTTER  = 6;      // divider thickness, px
var MIN_R   = 0.12;   // divider drag clamp

var RESOURCES = [
  { k: 'bible',      label: 'Bible',              url: '/read/',                 ref: true },
  { k: 'today',      label: 'Today',              url: '/today/' },
  { k: 'search',     label: 'Search / Explore',   url: '/search/' },
  { k: 'biblepedia', label: 'Biblepedia',         url: '/biblepedia/' },
  { k: 'library',    label: 'Library',            url: '/library/' },
  { k: 'answers',    label: 'Topical Answers',    url: '/answers/' },
  { k: 'maps',       label: 'Maps',               url: '/maps/' },
  { k: 'timeline',   label: 'Timeline',           url: '/timeline/' },
  { k: 'compare',    label: 'Compare',            url: '/compare/' },
  { k: 'workshop',   label: 'Original Languages', url: '/translation/workshop/' },
  { k: 'discipline', label: 'Discipline',         url: '/discipline/' },
  { k: 'notes',      label: 'My Notes',           url: '/notes/' },
];

var _root    = null;   // layout tree root node
var _rootEl  = null;   // #desk-root
var _panels  = Object.create(null);   // panel id → element
var _uid     = 1;

function _nid() { return 'n' + (_uid++); }

function _panelNode(url, title) { return { t: 'p', id: _nid(), url: url || null, title: title || '' }; }

function _defaultLayout() {
  return {
    t: 's', id: _nid(), d: 'row', r: 0.4,
    a: _panelNode('/today/', 'Today'),
    b: _panelNode('/read/', 'Bible'),
  };
}

// ── Persistence ─────────────────────────────────────────────────────────────
function _save() {
  try { localStorage.setItem(LS_KEY, JSON.stringify(_root)); } catch (e) {}
}
function _load() {
  try {
    var raw = localStorage.getItem(LS_KEY);
    if (!raw) return null;
    var tree = JSON.parse(raw);
    // Re-id the whole tree (uids must not collide with this session's counter).
    (function walk(n) {
      n.id = _nid();
      if (n.t === 's') { walk(n.a); walk(n.b); }
    })(tree);
    return tree;
  } catch (e) { return null; }
}

// ── Tree ops ────────────────────────────────────────────────────────────────
function _findParent(node, id, parent) {
  if (node.id === id) return { node: node, parent: parent || null };
  if (node.t !== 's') return null;
  return _findParent(node.a, id, node) || _findParent(node.b, id, node);
}

function _splitPanel(panelId, dir, url, title) {
  var hit = _findParent(_root, panelId, null);
  if (!hit || hit.node.t !== 'p') return null;
  var oldNode = hit.node;
  var fresh   = _panelNode(url || null, title);   // url omitted → chooser
  var split   = { t: 's', id: _nid(), d: dir, r: 0.5, a: oldNode, b: fresh };
  if (!hit.parent) _root = split;
  else if (hit.parent.a === oldNode) hit.parent.a = split;
  else hit.parent.b = split;
  _layout();
  _save();
  return fresh;
}

function _closePanel(panelId) {
  var hit = _findParent(_root, panelId, null);
  if (!hit) return;
  var el = _panels[panelId];
  if (el) { el.remove(); delete _panels[panelId]; }
  if (!hit.parent) {
    _root = _panelNode(null);   // last panel closed → empty chooser
  } else {
    var sibling = hit.parent.a === hit.node ? hit.parent.b : hit.parent.a;
    var gp = _findParent(_root, hit.parent.id, null);
    if (!gp || !gp.parent) _root = sibling;
    else if (gp.parent.a === hit.parent) gp.parent.a = sibling;
    else gp.parent.b = sibling;
  }
  _layout();
  _save();
}

function _addPanelToRoot() {
  var fresh = _panelNode(null);
  _root = { t: 's', id: _nid(), d: 'row', r: 0.62, a: _root, b: fresh };
  _layout();
  _save();
}

// ── Panel DOM ───────────────────────────────────────────────────────────────
function _esc(s) {
  return String(s).replace(/[&<>"']/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
  });
}

function _resourceLabel(url) {
  for (var i = 0; i < RESOURCES.length; i++) {
    if (url.indexOf(RESOURCES[i].url) === 0) return RESOURCES[i].label;
  }
  return 'Panel';
}

function _buildPanelEl(node) {
  var el = document.createElement('section');
  el.className = 'desk-panel';
  el.setAttribute('data-panel-id', node.id);
  el.innerHTML =
    '<header class="desk-panel__bar">' +
      '<span class="desk-panel__title">' + _esc(node.title || (node.url ? _resourceLabel(node.url) : 'New panel')) + '</span>' +
      '<span class="desk-panel__spacer"></span>' +
      '<button class="desk-panel__btn desk-panel__btn--link" data-act="link" hidden ' +
        'title="Link navigation: linked Bible panels follow each other" aria-label="Link panel navigation" ' +
        'aria-pressed="' + (node.link ? 'true' : 'false') + '">🔗</button>' +
      '<button class="desk-panel__btn" data-act="split-r" title="Split right" aria-label="Split right">◫</button>' +
      '<button class="desk-panel__btn" data-act="split-d" title="Split down" aria-label="Split down">⬓</button>' +
      '<button class="desk-panel__btn" data-act="close" title="Close panel" aria-label="Close panel">✕</button>' +
    '</header>' +
    '<div class="desk-panel__body"></div>';

  el.addEventListener('click', function (e) {
    var btn = e.target.closest('.desk-panel__btn');
    if (!btn) return;
    var act = btn.getAttribute('data-act');
    if (act === 'split-r') _splitPanel(node.id, 'row');
    else if (act === 'split-d') _splitPanel(node.id, 'col');
    else if (act === 'close') _closePanel(node.id);
    else if (act === 'link') {
      node.link = !node.link;
      btn.setAttribute('aria-pressed', node.link ? 'true' : 'false');
      _save();
    }
  });

  if (node.url) _mountFrame(el, node);
  else _mountChooser(el, node);
  return el;
}

function _mountFrame(el, node) {
  var body = el.querySelector('.desk-panel__body');
  var frame = document.createElement('iframe');
  frame.className = 'desk-panel__frame';
  frame.src = node.url;
  frame.setAttribute('title', node.title || _resourceLabel(node.url));
  frame.addEventListener('load', function () {
    // Announce the Desk to the page (arms desk-frame.js: cross-resource
    // clicks become panels, reader linking activates). Re-sent on every
    // load because navigation replaces the frame's document.
    try { frame.contentWindow.postMessage({ type: 'bsw-desk-hello' }, location.origin); } catch (e) {}
    // Same-origin: track in-panel navigation so the layout restores where
    // the user actually was, and let the page retitle the panel bar.
    try {
      var loc = frame.contentWindow.location;
      if (loc && loc.pathname) node.url = loc.pathname + loc.search;
      var t = frame.contentDocument && frame.contentDocument.title;
      if (t) {
        node.title = t.replace(/\s+—.*$/, '');
        var tEl = el.querySelector('.desk-panel__title');
        if (tEl) tEl.textContent = node.title;
      }
    } catch (e) {}
    // The link toggle only means something on Bible panels.
    var linkBtn = el.querySelector('.desk-panel__btn--link');
    if (linkBtn) linkBtn.hidden = resourcePrefix(node.url || '') !== 'read';
    _save();
  });
  body.appendChild(frame);
}

function _mountChooser(el, node) {
  var body = el.querySelector('.desk-panel__body');
  var box = document.createElement('div');
  box.className = 'desk-chooser';
  box.innerHTML =
    '<p class="desk-chooser__head">Open a resource</p>' +
    '<div class="desk-chooser__grid">' +
      RESOURCES.map(function (r) {
        return '<button class="desk-chooser__item" data-k="' + r.k + '">' + _esc(r.label) + '</button>';
      }).join('') +
    '</div>' +
    '<form class="desk-chooser__refrow" hidden>' +
      '<input class="desk-chooser__refinput" type="text" placeholder="Passage — John 3, Psalm 23… (optional)" aria-label="Passage">' +
      '<button class="desk-chooser__go" type="submit">Open Bible</button>' +
    '</form>';
  body.appendChild(box);

  var refRow = box.querySelector('.desk-chooser__refrow');
  box.addEventListener('click', function (e) {
    var item = e.target.closest('.desk-chooser__item');
    if (!item) return;
    var res = RESOURCES.filter(function (r) { return r.k === item.getAttribute('data-k'); })[0];
    if (!res) return;
    if (res.ref) {
      // Bible: offer an optional passage before opening.
      refRow.hidden = false;
      refRow.querySelector('.desk-chooser__refinput').focus();
      return;
    }
    _choose(node, el, res.url, res.label);
  });
  refRow.addEventListener('submit', function (e) {
    e.preventDefault();
    var v = refRow.querySelector('.desk-chooser__refinput').value.trim();
    _choose(node, el, v ? '/read/?ref=' + encodeURIComponent(v) : '/read/', 'Bible');
  });
}

function _choose(node, el, url, label) {
  node.url = url;
  node.title = label;
  el.querySelector('.desk-panel__body').innerHTML = '';
  el.querySelector('.desk-panel__title').textContent = label;
  _mountFrame(el, node);
  _save();
}

// ── Geometry: tree → absolute rects; panels positioned, never reparented ───
function _layout() {
  if (!_rootEl) return;
  var W = _rootEl.clientWidth, H = _rootEl.clientHeight;
  // Drop stale dividers; panels persist by id.
  _rootEl.querySelectorAll('.desk-divider').forEach(function (d) { d.remove(); });
  var seen = Object.create(null);
  var narrow = window.innerWidth < 900;

  if (narrow) {
    // Phone / narrow: stack every panel full-width in tree order.
    var flat = [];
    (function collect(n) { if (n.t === 'p') flat.push(n); else { collect(n.a); collect(n.b); } })(_root);
    var PH = Math.max(340, Math.round(window.innerHeight * 0.72));
    _rootEl.style.height = (flat.length * (PH + GUTTER)) + 'px';
    flat.forEach(function (n, i) {
      _place(n, { x: 0, y: i * (PH + GUTTER), w: W, h: PH });
      seen[n.id] = 1;
    });
  } else {
    _rootEl.style.height = '';
    (function walk(n, rect) {
      if (n.t === 'p') {
        _place(n, rect);
        seen[n.id] = 1;
        return;
      }
      var a, b, div = document.createElement('div');
      div.className = 'desk-divider desk-divider--' + n.d;
      div.setAttribute('data-split-id', n.id);
      if (n.d === 'row') {
        var wA = Math.round((rect.w - GUTTER) * n.r);
        a = { x: rect.x, y: rect.y, w: wA, h: rect.h };
        b = { x: rect.x + wA + GUTTER, y: rect.y, w: rect.w - wA - GUTTER, h: rect.h };
        div.style.cssText = 'left:' + (rect.x + wA) + 'px;top:' + rect.y + 'px;width:' + GUTTER + 'px;height:' + rect.h + 'px;';
      } else {
        var hA = Math.round((rect.h - GUTTER) * n.r);
        a = { x: rect.x, y: rect.y, w: rect.w, h: hA };
        b = { x: rect.x, y: rect.y + hA + GUTTER, w: rect.w, h: rect.h - hA - GUTTER };
        div.style.cssText = 'left:' + rect.x + 'px;top:' + (rect.y + hA) + 'px;width:' + rect.w + 'px;height:' + GUTTER + 'px;';
      }
      div.addEventListener('pointerdown', _dragStart);
      _rootEl.appendChild(div);
      walk(n.a, a);
      walk(n.b, b);
    })(_root, { x: 0, y: 0, w: W, h: H });
  }

  // Remove panel elements whose nodes are gone (closed subtrees).
  Object.keys(_panels).forEach(function (id) {
    if (!seen[id]) { _panels[id].remove(); delete _panels[id]; }
  });
}

function _place(node, rect) {
  var el = _panels[node.id];
  if (!el) {
    el = _buildPanelEl(node);
    _panels[node.id] = el;
    _rootEl.appendChild(el);
  }
  el.style.cssText = 'left:' + rect.x + 'px;top:' + rect.y + 'px;width:' + rect.w + 'px;height:' + rect.h + 'px;';
}

// ── Divider drag ────────────────────────────────────────────────────────────
function _dragStart(e) {
  var splitId = e.currentTarget.getAttribute('data-split-id');
  var hit = _findParent(_root, splitId, null);
  if (!hit) return;
  var split = hit.node;
  e.preventDefault();
  _rootEl.classList.add('desk-root--dragging');
  var rootRect = _rootEl.getBoundingClientRect();

  // The split's own rect must be recomputed to translate pointer → ratio.
  var splitRect = null;
  (function walk(n, rect) {
    if (splitRect || n.t !== 's') return;
    if (n.id === splitId) { splitRect = rect; return; }
    if (n.d === 'row') {
      var wA = Math.round((rect.w - GUTTER) * n.r);
      walk(n.a, { x: rect.x, y: rect.y, w: wA, h: rect.h });
      walk(n.b, { x: rect.x + wA + GUTTER, y: rect.y, w: rect.w - wA - GUTTER, h: rect.h });
    } else {
      var hA = Math.round((rect.h - GUTTER) * n.r);
      walk(n.a, { x: rect.x, y: rect.y, w: rect.w, h: hA });
      walk(n.b, { x: rect.x, y: rect.y + hA + GUTTER, w: rect.w, h: rect.h - hA - GUTTER });
    }
  })(_root, { x: 0, y: 0, w: _rootEl.clientWidth, h: _rootEl.clientHeight });
  if (!splitRect) { _rootEl.classList.remove('desk-root--dragging'); return; }

  function move(ev) {
    var r = split.d === 'row'
      ? (ev.clientX - rootRect.left - splitRect.x) / splitRect.w
      : (ev.clientY - rootRect.top - splitRect.y) / splitRect.h;
    split.r = Math.max(MIN_R, Math.min(1 - MIN_R, r));
    _layout();
  }
  function up() {
    document.removeEventListener('pointermove', move);
    document.removeEventListener('pointerup', up);
    _rootEl.classList.remove('desk-root--dragging');
    _save();
  }
  document.addEventListener('pointermove', move);
  document.addEventListener('pointerup', up);
}

// ── Frame messages: cross-resource opens + reader linking ──────────────────
function _panelByWindow(win) {
  var ids = Object.keys(_panels);
  for (var i = 0; i < ids.length; i++) {
    var f = _panels[ids[i]].querySelector('iframe');
    if (f && f.contentWindow === win) return ids[i];
  }
  return null;
}

function _collectPanels(n, out) {
  if (n.t === 'p') out.push(n);
  else { _collectPanels(n.a, out); _collectPanels(n.b, out); }
  return out;
}

function _flash(id) {
  var el = _panels[id];
  if (!el) return;
  el.classList.add('desk-panel--flash');
  setTimeout(function () { el.classList.remove('desk-panel--flash'); }, 900);
}

function _onFrameMessage(e) {
  if (e.origin !== location.origin || !e.data || !e.data.type) return;
  var srcId = _panelByWindow(e.source);
  if (!srcId) return;

  if (e.data.type === 'bsw-desk-open' && e.data.url) {
    var url = String(e.data.url);
    if (resourcePrefix(url) === 'desk') return;
    // Reuse: if another panel already shows this resource, navigate it there
    // (the Logos "target panel" behavior) instead of tiling endlessly.
    var target = _collectPanels(_root, []).filter(function (n) {
      return n.id !== srcId && n.url && resourcePrefix(n.url) === resourcePrefix(url);
    })[0];
    if (target) {
      var f = _panels[target.id] && _panels[target.id].querySelector('iframe');
      if (f) {
        try { f.contentWindow.location.replace(url); } catch (err) { f.src = url; }
        target.url = url;
        _flash(target.id);
        _save();
        return;
      }
    }
    // No panel to reuse: split the source along its longer axis.
    var srcEl = _panels[srcId];
    var dir = srcEl && srcEl.offsetHeight > srcEl.offsetWidth ? 'col' : 'row';
    var fresh = _splitPanel(srcId, dir, url, _resourceLabel(url));
    if (fresh) _flash(fresh.id);
    return;
  }

  if (e.data.type === 'bsw-desk-nav' && e.data.ref) {
    var hit = _findParent(_root, srcId, null);
    if (!hit || !hit.node.link) return;   // source isn't link-toggled
    _collectPanels(_root, []).forEach(function (n) {
      if (n.id === srcId || !n.link || resourcePrefix(n.url || '') !== 'read') return;
      var f = _panels[n.id] && _panels[n.id].querySelector('iframe');
      if (f) {
        try { f.contentWindow.postMessage({ type: 'bsw-desk-goto', ref: e.data.ref }, location.origin); } catch (err) {}
      }
    });
  }
}

// ── Init ────────────────────────────────────────────────────────────────────
export function initDesk() {
  _rootEl = document.getElementById('desk-root');
  if (!_rootEl) return;
  _root = _load() || _defaultLayout();
  _layout();
  window.addEventListener('message', _onFrameMessage);

  var addBtn = document.getElementById('desk-add-btn');
  if (addBtn) addBtn.addEventListener('click', _addPanelToRoot);
  var resetBtn = document.getElementById('desk-reset-btn');
  if (resetBtn) resetBtn.addEventListener('click', function () {
    Object.keys(_panels).forEach(function (id) { _panels[id].remove(); delete _panels[id]; });
    _root = _defaultLayout();
    _layout();
    _save();
  });

  var _rsz = null;
  window.addEventListener('resize', function () {
    clearTimeout(_rsz);
    _rsz = setTimeout(_layout, 120);
  });
}
