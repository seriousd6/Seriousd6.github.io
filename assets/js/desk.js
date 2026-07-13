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
var NAMES_KEY = 'bsw_desk_layouts_v1';   // named layouts: { name: strippedTree }
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
var _maxId   = null;   // maximized panel id (transient — not persisted)

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

// ── Named + shareable layouts (P9) ──────────────────────────────────────────
// A stripped tree carries only shape + urls (ids and per-panel history are
// session state). _reviveTree validates everything on the way back in — a
// shared #z= link is untrusted input, so panel urls must be same-origin
// absolute paths.
function _stripTree(n) {
  if (n.t === 's') return { t: 's', d: n.d, r: n.r, a: _stripTree(n.a), b: _stripTree(n.b) };
  return { t: 'p', url: n.url, title: n.title };
}
function _reviveTree(n) {
  if (!n || (n.t !== 's' && n.t !== 'p')) throw new Error('bad node');
  if (n.t === 's') {
    return { t: 's', id: _nid(), d: n.d === 'col' ? 'col' : 'row',
             r: Math.min(0.88, Math.max(0.12, +n.r || 0.5)),
             a: _reviveTree(n.a), b: _reviveTree(n.b) };
  }
  var url = (typeof n.url === 'string' && n.url.charAt(0) === '/' && n.url.charAt(1) !== '/') ? n.url : null;
  return { t: 'p', id: _nid(), url: url, title: String(n.title || '') };
}
function _namedLayouts() {
  try { return JSON.parse(localStorage.getItem(NAMES_KEY) || '{}'); } catch (e) { return {}; }
}
function _setNamedLayouts(map) {
  try { localStorage.setItem(NAMES_KEY, JSON.stringify(map)); } catch (e) {}
}
// Swap the whole surface to a new tree (named-layout load, shared link).
function _applyTree(tree) {
  Object.keys(_panels).forEach(function (id) { _panels[id].remove(); delete _panels[id]; });
  _maxId = null;
  _mobileActive = null;
  _root = tree;
  _layout();
  _save();
}
function _shareLink() {
  var json = JSON.stringify(_stripTree(_root));
  var b64  = btoa(unescape(encodeURIComponent(json)))
    .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  return location.origin + '/desk/#z=' + b64;
}
// /desk/#bible+maps (resource keys) or /desk/#z=<b64 tree> from "Copy share
// link". Returns null when the hash is absent or unusable.
function _treeFromHash() {
  var h = location.hash.replace(/^#/, '');
  if (!h) return null;
  try {
    if (h.indexOf('z=') === 0) {
      var b = h.slice(2).replace(/-/g, '+').replace(/_/g, '/');
      while (b.length % 4) b += '=';   // some browsers' atob wants padding
      return _reviveTree(JSON.parse(decodeURIComponent(escape(atob(b)))));
    }
    var nodes = [];
    decodeURIComponent(h).split('+').forEach(function (k) {
      k = k.toLowerCase().trim();
      if (!k) return;
      var res = RESOURCES.filter(function (r) {
        return r.k === k || r.url.split('/').filter(Boolean)[0] === k;
      })[0];
      if (res) nodes.push(_panelNode(res.url, res.label));
    });
    if (!nodes.length) return null;
    var tree = nodes[nodes.length - 1];
    for (var i = nodes.length - 2; i >= 0; i--) {
      tree = { t: 's', id: _nid(), d: 'row', r: 1 / (nodes.length - i), a: nodes[i], b: tree };
    }
    return tree;
  } catch (e) {
    try { console.warn('[desk] could not apply shared layout:', e); } catch (e2) {}
    return null;
  }
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
  _maxId = null;   // splitting implies working with the layout again
  var oldNode = hit.node;
  var fresh   = _panelNode(url || null, title);   // url omitted → chooser
  if (window.innerWidth < 900) _mobileActive = fresh.id;
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
  if (_maxId === panelId) _maxId = null;
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

// Detach a panel node from the tree (its element stays mounted — dock it
// again right away). Returns null for the tree's only panel.
function _detachNode(panelId) {
  var hit = _findParent(_root, panelId, null);
  if (!hit || !hit.parent) return null;
  var node = hit.node;
  var sibling = hit.parent.a === node ? hit.parent.b : hit.parent.a;
  var gp = _findParent(_root, hit.parent.id, null);
  if (!gp || !gp.parent) _root = sibling;
  else if (gp.parent.a === hit.parent) gp.parent.a = sibling;
  else gp.parent.b = sibling;
  return node;
}

// Insert a detached node beside the target panel, on the given side.
function _dockNode(node, targetId, quad) {
  var hit = _findParent(_root, targetId, null);
  if (!hit) return;
  var target = hit.node;
  var dir   = (quad === 'left' || quad === 'right') ? 'row' : 'col';
  var first = (quad === 'left' || quad === 'top');
  var split = { t: 's', id: _nid(), d: dir, r: 0.5,
                a: first ? node : target, b: first ? target : node };
  if (!hit.parent) _root = split;
  else if (hit.parent.a === target) hit.parent.a = split;
  else hit.parent.b = split;
}

function _addPanelToRoot() {
  var fresh = _panelNode(null);
  _root = { t: 's', id: _nid(), d: 'row', r: 0.62, a: _root, b: fresh };
  if (window.innerWidth < 900) _mobileActive = fresh.id;   // show the chooser
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
      '<button class="desk-panel__btn desk-panel__btn--back" data-act="back" hidden ' +
        'title="Back (this panel)" aria-label="Back in this panel">←</button>' +
      '<span class="desk-panel__title">' + _esc(node.title || (node.url ? _resourceLabel(node.url) : 'New panel')) + '</span>' +
      '<span class="desk-panel__spacer"></span>' +
      '<button class="desk-panel__btn desk-panel__btn--link" data-act="link" hidden ' +
        'title="Link navigation: linked Bible panels follow each other" aria-label="Link panel navigation" ' +
        'aria-pressed="' + (node.link ? 'true' : 'false') + '">🔗</button>' +
      '<button class="desk-panel__btn" data-act="split-r" title="Split right" aria-label="Split right">◫</button>' +
      '<button class="desk-panel__btn" data-act="split-d" title="Split down" aria-label="Split down">⬓</button>' +
      '<button class="desk-panel__btn desk-panel__btn--max" data-act="max" title="Maximize panel" aria-label="Maximize panel" aria-pressed="false">⛶</button>' +
      '<button class="desk-panel__btn" data-act="close" title="Close panel" aria-label="Close panel">✕</button>' +
    '</header>' +
    '<div class="desk-panel__body"></div>';

  el.addEventListener('pointerenter', function () { _activeId = node.id; });
  _wireSwipe(el.querySelector('.desk-panel__bar'));
  el.querySelector('.desk-panel__bar').addEventListener('pointerdown', function (e) {
    if (e.target.closest('.desk-panel__btn') || e.button !== 0) return;
    _barDragStart(e, node.id);
  });

  el.addEventListener('click', function (e) {
    var btn = e.target.closest('.desk-panel__btn');
    if (!btn) return;
    var act = btn.getAttribute('data-act');
    if (act === 'link') {
      node.link = !node.link;
      btn.setAttribute('aria-pressed', node.link ? 'true' : 'false');
      _retireLinkHint();   // the feature has been discovered
      _save();
    } else if (act === 'back') {
      // Panel-local back: our own URL stack + location.replace, because the
      // frame's history.back() walks the SHARED session history and can pop
      // another panel's (or the Desk's) entry instead.
      var prev = node.hist && node.hist.pop();
      if (prev) {
        node._goingBack = true;
        var f = el.querySelector('iframe');
        if (f) { try { f.contentWindow.location.replace(prev); } catch (err) { f.src = prev; } }
      }
      btn.hidden = !(node.hist && node.hist.length);
      _save();
    } else {
      _panelAction(node.id, act);
    }
  });

  if (node.url) _mountFrame(el, node);
  else _mountChooser(el, node);
  return el;
}

// P12: while the saved layout restores, panels after the first mount their
// iframes staggered (+300 ms each) so a many-panel desk doesn't fire every
// page load at once. Splits and chooser picks after boot mount immediately.
var _booting = false;
var _bootMounts = 0;

function _mountFrame(el, node) {
  if (_booting && _bootMounts++ > 0) {
    var delay = _bootMounts * 300;
    setTimeout(function () {
      if (el.isConnected && !el.querySelector('iframe')) _mountFrameNow(el, node);
    }, delay);
    return;
  }
  _mountFrameNow(el, node);
}

function _mountFrameNow(el, node) {
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
    // the user actually was, and let the page retitle the panel bar. Each
    // navigation also feeds the panel's own back stack (the ← button).
    try {
      var loc = frame.contentWindow.location;
      if (loc && loc.pathname) {
        var newUrl = loc.pathname + loc.search;
        if (node.url && node.url !== newUrl && !node._goingBack) {
          (node.hist = node.hist || []).push(node.url);
          if (node.hist.length > 20) node.hist.shift();
        }
        node._goingBack = false;
        node.url = newUrl;
        var backBtn = el.querySelector('.desk-panel__btn--back');
        if (backBtn) backBtn.hidden = !(node.hist && node.hist.length);
      }
      var t = frame.contentDocument && frame.contentDocument.title;
      if (t) {
        node.title = t.replace(/\s+—.*$/, '');
        var tEl = el.querySelector('.desk-panel__title');
        if (tEl) tEl.textContent = node.title;
        var tabBtn = _rootEl && _rootEl.querySelector('.desk-tab-btn[data-id="' + node.id + '"]');
        if (tabBtn) tabBtn.textContent = node.title;
      }
    } catch (e) {}
    // The link toggle means something on Bible panels (follow navigation)
    // and maps panels (show a linked reader's chapter places).
    var linkBtn = el.querySelector('.desk-panel__btn--link');
    if (linkBtn) {
      var rp = resourcePrefix(node.url || '');
      linkBtn.hidden = rp !== 'read' && rp !== 'maps' && rp !== 'compare';
    }
    _maybeLinkHint();
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

  // Maximize: the chosen panel gets the whole surface; the others stay
  // mounted (hidden iframes keep their state) until restored.
  if (_maxId && !narrow) {
    var all = _collectPanels(_root, []);
    var maxNode = all.filter(function (n) { return n.id === _maxId; })[0];
    if (!maxNode) { _maxId = null; }
    else {
      all.forEach(function (n) {
        seen[n.id] = 1;
        if (n.id === _maxId) { _place(n, { x: 0, y: 0, w: W, h: H }); }
        else if (_panels[n.id]) { _panels[n.id].classList.add('desk-panel--hidden'); }
      });
      _syncMaxButtons();
      return;
    }
  }

  var oldTabbar = _rootEl.querySelector('.desk-tabbar');
  if (oldTabbar) oldTabbar.remove();

  if (narrow) {
    // Phone (A4): one panel at a time + a bottom tab strip. Inactive panels
    // that have been visited stay mounted (hidden iframes keep state);
    // never-visited ones aren't built until their tab is tapped, so a phone
    // doesn't pay for the whole layout up front.
    var flat = _collectPanels(_root, []);
    if (!flat.length) return;
    if (!_mobileActive || !flat.some(function (n) { return n.id === _mobileActive; })) {
      _mobileActive = flat[0].id;
    }
    var TAB_H = 46;
    flat.forEach(function (n) {
      seen[n.id] = 1;
      if (n.id === _mobileActive) _place(n, { x: 0, y: 0, w: W, h: H - TAB_H });
      else if (_panels[n.id]) _panels[n.id].classList.add('desk-panel--hidden');
    });
    _buildMobileTabbar(flat);
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
      div.tabIndex = 0;
      div.setAttribute('role', 'separator');
      div.setAttribute('aria-orientation', n.d === 'row' ? 'vertical' : 'horizontal');
      div.setAttribute('aria-label', 'Resize panels (arrow keys)');
      div.addEventListener('keydown', _dividerKeydown);
      _rootEl.appendChild(div);
      walk(n.a, a);
      walk(n.b, b);
    })(_root, { x: 0, y: 0, w: W, h: H });
  }

  // Remove panel elements whose nodes are gone (closed subtrees).
  Object.keys(_panels).forEach(function (id) {
    if (!seen[id]) { _panels[id].remove(); delete _panels[id]; }
  });
  _syncMaxButtons();
}

var _mobileActive = null;   // narrow-mode visible panel id

function _buildMobileTabbar(flat) {
  var bar = document.createElement('div');
  bar.className = 'desk-tabbar';
  bar.setAttribute('role', 'tablist');
  bar.setAttribute('aria-label', 'Desk panels');
  flat.forEach(function (n) {
    var btn = document.createElement('button');
    btn.className = 'desk-tab-btn' + (n.id === _mobileActive ? ' desk-tab-btn--active' : '');
    btn.type = 'button';
    btn.setAttribute('role', 'tab');
    btn.setAttribute('aria-selected', n.id === _mobileActive ? 'true' : 'false');
    btn.setAttribute('data-id', n.id);
    btn.textContent = n.title || (n.url ? _resourceLabel(n.url) : 'New panel');
    btn.addEventListener('click', function () { _mobileActive = n.id; _layout(); });
    bar.appendChild(btn);
  });
  _wireTabSwipe(bar, flat);
  var add = document.createElement('button');
  add.className = 'desk-tab-btn desk-tab-btn--add';
  add.type = 'button';
  add.setAttribute('aria-label', 'Add panel');
  add.textContent = '+';
  add.addEventListener('click', _addPanelToRoot);
  bar.appendChild(add);
  _rootEl.appendChild(bar);
}

// P12: phone swipe — a horizontal swipe on the tab strip (or a panel's title
// bar) moves to the previous/next panel. The panel BODY can't host this: it's
// an iframe, and touches inside it never reach the desk document.
function _swipeToNeighbor(dir) {
  var flat = _collectPanels(_root, []);
  var idx = -1;
  flat.forEach(function (n, i) { if (n.id === _mobileActive) idx = i; });
  if (idx === -1) return;
  var next = flat[idx + dir];
  if (!next) return;
  _mobileActive = next.id;
  _layout();
}

function _wireSwipe(el) {
  var x0 = null, y0 = null;
  el.addEventListener('touchstart', function (e) {
    if (e.touches.length !== 1) { x0 = null; return; }
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY;
  }, { passive: true });
  el.addEventListener('touchend', function (e) {
    if (x0 === null || window.innerWidth >= 900) return;
    var t = e.changedTouches[0];
    var dx = t.clientX - x0, dy = t.clientY - y0;
    x0 = null;
    if (Math.abs(dx) < 55 || Math.abs(dy) > 45) return;
    _swipeToNeighbor(dx < 0 ? 1 : -1);   // swipe left → next panel
  }, { passive: true });
}

function _wireTabSwipe(bar) { _wireSwipe(bar); }

function _syncMaxButtons() {
  Object.keys(_panels).forEach(function (id) {
    var btn = _panels[id].querySelector('.desk-panel__btn--max');
    if (btn) btn.setAttribute('aria-pressed', _maxId === id ? 'true' : 'false');
  });
}

function _place(node, rect) {
  var el = _panels[node.id];
  if (!el) {
    el = _buildPanelEl(node);
    _panels[node.id] = el;
    _rootEl.appendChild(el);
  }
  el.classList.remove('desk-panel--hidden');
  el.style.cssText = 'left:' + rect.x + 'px;top:' + rect.y + 'px;width:' + rect.w + 'px;height:' + rect.h + 'px;';
}

// P12: keyboard divider resize. Arrows nudge the split ratio; _layout()
// rebuilds every divider element, so focus is re-planted on the new element
// carrying the same split id.
function _dividerKeydown(e) {
  var splitId = e.currentTarget.getAttribute('data-split-id');
  var hit = _findParent(_root, splitId, null);
  if (!hit || hit.node.t !== 's') return;
  var split = hit.node;
  var delta = 0;
  if (split.d === 'row')  delta = e.key === 'ArrowLeft' ? -0.03 : e.key === 'ArrowRight' ? 0.03 : 0;
  else                    delta = e.key === 'ArrowUp'   ? -0.03 : e.key === 'ArrowDown'  ? 0.03 : 0;
  if (!delta) return;
  e.preventDefault();
  split.r = Math.max(MIN_R, Math.min(1 - MIN_R, split.r + delta));
  _layout();
  _save();
  var fresh = _rootEl.querySelector('.desk-divider[data-split-id="' + splitId + '"]');
  if (fresh) fresh.focus();
}

// ── Divider drag ────────────────────────────────────────────────────────────
function _dragStart(e) {
  var splitId = e.currentTarget.getAttribute('data-split-id');
  var hit = _findParent(_root, splitId, null);
  if (!hit) return;
  var split = hit.node;
  e.preventDefault();
  // preventDefault suppresses pointerdown's native focus — restore it so a
  // click followed by arrow keys resizes (P12 keyboard path).
  try { e.currentTarget.focus(); } catch (err) {}
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
  _activeId = srcId;   // the panel the user is interacting with

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
      var rp = resourcePrefix(n.url || '');
      if (n.id === srcId || !n.link || (rp !== 'read' && rp !== 'compare')) return;
      var f = _panels[n.id] && _panels[n.id].querySelector('iframe');
      if (f) {
        try { f.contentWindow.postMessage({ type: 'bsw-desk-goto', ref: e.data.ref }, location.origin); } catch (err) {}
      }
    });
    return;
  }

  // A panel forwarded a Desk keyboard shortcut (typed while its frame had focus).
  if (e.data.type === 'bsw-desk-key' && e.data.act) {
    _panelAction(srcId, e.data.act);
    return;
  }

  // A linked reader's chapter finished tagging its places → linked maps
  // panels show them (markers + fit).
  if (e.data.type === 'bsw-desk-places' && e.data.ids) {
    var srcHit = _findParent(_root, srcId, null);
    if (!srcHit || !srcHit.node.link) return;
    _collectPanels(_root, []).forEach(function (n) {
      if (n.id === srcId || !n.link || resourcePrefix(n.url || '') !== 'maps') return;
      var f = _panels[n.id] && _panels[n.id].querySelector('iframe');
      if (f) {
        try { f.contentWindow.postMessage({ type: 'bsw-desk-show-places', ref: e.data.ref, ids: e.data.ids, mapId: e.data.mapId || null }, location.origin); } catch (err) {}
      }
    });
  }
}

// ── Linking first-use hint (A2) ─────────────────────────────────────────────
// The 🔗 toggle is the least discoverable desk feature. The first time the
// surface holds two+ linkable panels with none linked, a one-time hint
// appears beside the toggle. Dismissing it — or using any link toggle —
// retires it for good.
var HINT_KEY = 'bsw_desk_linkhint';
var LINKABLE = { read: 1, maps: 1, compare: 1 };

function _retireLinkHint() {
  try { localStorage.setItem(HINT_KEY, '1'); } catch (e) {}
  var tip = _rootEl && _rootEl.querySelector('.desk-link-hint');
  if (tip) tip.remove();
}

function _maybeLinkHint() {
  try { if (localStorage.getItem(HINT_KEY)) return; } catch (e) { return; }
  if (!_rootEl || _rootEl.querySelector('.desk-link-hint')) return;
  var linkables = _collectPanels(_root, []).filter(function (n) {
    return LINKABLE[resourcePrefix(n.url || '')];
  });
  if (linkables.length < 2) return;
  if (linkables.some(function (n) { return n.link; })) { _retireLinkHint(); return; }
  var host = _panels[linkables[0].id];
  var btn = host && host.querySelector('.desk-panel__btn--link');
  if (!btn || btn.hidden) return;
  var tip = document.createElement('div');
  tip.className = 'desk-link-hint';
  tip.setAttribute('role', 'note');
  tip.innerHTML =
    'Tip: <b>link panels</b> with the 🔗 above — linked Bibles navigate together, ' +
    'and linked Maps and Compare panels follow along. ' +
    '<button class="desk-link-hint__x" aria-label="Dismiss tip">Got it</button>';
  host.appendChild(tip);
  tip.querySelector('.desk-link-hint__x').addEventListener('click', _retireLinkHint);
}

// ── Panel actions (shared by bar buttons, shortcuts, frame-forwarded keys) ──
var _activeId = null;   // last panel the pointer entered / that messaged us

function _panelAction(panelId, act) {
  if (!panelId || !_panels[panelId]) return;
  if (act === 'split-r') _splitPanel(panelId, 'row');
  else if (act === 'split-d') _splitPanel(panelId, 'col');
  else if (act === 'close') _closePanel(panelId);
  else if (act === 'max') { _maxId = _maxId === panelId ? null : panelId; _layout(); }
}

// Ctrl+Shift+→ split right · Ctrl+Shift+↓ split down · Ctrl+Shift+⏎ maximize
// · Ctrl+Shift+⌫ close. Shared map with desk-frame.js — keep in sync.
export function deskKeyAction(e) {
  if (!(e.ctrlKey || e.metaKey) || !e.shiftKey) return null;
  var t = e.target;
  if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return null;
  switch (e.key) {
    case 'ArrowRight': return 'split-r';
    case 'ArrowDown':  return 'split-d';
    case 'Enter':      return 'max';
    case 'Backspace':  return 'close';
  }
  return null;
}

// ── Drag a panel bar to re-dock it beside another panel ────────────────────
// Pure tree surgery on drop (detach + dock) — panel elements never move in
// the DOM, so iframes never reload mid-rearrange.
var _dropHint = null;

function _quadrantAt(el, x, y) {
  var r = el.getBoundingClientRect();
  var rx = (x - r.left) / r.width, ry = (y - r.top) / r.height;
  // Nearest edge wins; ties prefer horizontal docking.
  var d = [ { q: 'left', v: rx }, { q: 'right', v: 1 - rx }, { q: 'top', v: ry }, { q: 'bottom', v: 1 - ry } ];
  d.sort(function (a, b) { return a.v - b.v; });
  return d[0].q;
}

function _hintRect(el, quad) {
  var r = el.getBoundingClientRect(), o = _rootEl.getBoundingClientRect();
  var x = r.left - o.left, y = r.top - o.top, w = r.width, h = r.height;
  if (quad === 'left')   return { x: x, y: y, w: w / 2, h: h };
  if (quad === 'right')  return { x: x + w / 2, y: y, w: w / 2, h: h };
  if (quad === 'top')    return { x: x, y: y, w: w, h: h / 2 };
  return { x: x, y: y + h / 2, w: w, h: h / 2 };
}

function _barDragStart(e, srcId) {
  if (window.innerWidth < 900 || _maxId) return;
  var startX = e.clientX, startY = e.clientY;
  var dragging = false;
  var target = null, quad = null;

  function move(ev) {
    if (!dragging) {
      if (Math.abs(ev.clientX - startX) < 6 && Math.abs(ev.clientY - startY) < 6) return;
      dragging = true;
      _rootEl.classList.add('desk-root--dragging', 'desk-root--moving');
      if (!_dropHint) {
        _dropHint = document.createElement('div');
        _dropHint.className = 'desk-drop-hint';
        _rootEl.appendChild(_dropHint);
      }
    }
    target = null;
    var ids = Object.keys(_panels);
    for (var i = 0; i < ids.length; i++) {
      if (ids[i] === srcId) continue;
      var r = _panels[ids[i]].getBoundingClientRect();
      if (ev.clientX >= r.left && ev.clientX <= r.right && ev.clientY >= r.top && ev.clientY <= r.bottom) {
        target = ids[i];
        break;
      }
    }
    if (target) {
      quad = _quadrantAt(_panels[target], ev.clientX, ev.clientY);
      var hr = _hintRect(_panels[target], quad);
      _dropHint.style.cssText = 'display:block;left:' + hr.x + 'px;top:' + hr.y + 'px;width:' + hr.w + 'px;height:' + hr.h + 'px;';
    } else {
      quad = null;
      _dropHint.style.display = 'none';
    }
  }
  function up() {
    document.removeEventListener('pointermove', move);
    document.removeEventListener('pointerup', up);
    _rootEl.classList.remove('desk-root--dragging', 'desk-root--moving');
    if (_dropHint) _dropHint.style.display = 'none';
    if (!dragging || !target || !quad || target === srcId) return;
    var node = _detachNode(srcId);
    if (!node) return;
    _dockNode(node, target, quad);
    _layout();
    _save();
  }
  document.addEventListener('pointermove', move);
  document.addEventListener('pointerup', up);
}

// ── Init ────────────────────────────────────────────────────────────────────
// ── Layouts menu (P9) ───────────────────────────────────────────────────────
var _layMenuEl = null;

function _renderLayoutsMenu() {
  var saved = _namedLayouts();
  var names = Object.keys(saved).sort();
  _layMenuEl.innerHTML =
    (names.length
      ? names.map(function (n) {
          return '<div class="desk-lay-row">' +
            '<button type="button" class="desk-lay-load" data-n="' + _esc(n) + '">' + _esc(n) + '</button>' +
            '<button type="button" class="desk-lay-del" data-n="' + _esc(n) + '" aria-label="Delete layout ' + _esc(n) + '">✕</button>' +
          '</div>';
        }).join('')
      : '<p class="desk-lay-empty">No saved layouts yet.</p>') +
    '<div class="desk-lay-saverow">' +
      '<input type="text" class="desk-lay-name" placeholder="Layout name" maxlength="40" aria-label="Layout name">' +
      '<button type="button" class="desk-lay-savebtn">Save</button>' +
    '</div>' +
    '<button type="button" class="desk-lay-share">Copy share link</button>';

  _layMenuEl.querySelectorAll('.desk-lay-load').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var tree = _namedLayouts()[btn.getAttribute('data-n')];
      if (!tree) return;
      try { _applyTree(_reviveTree(tree)); } catch (e) { return; }
      _closeLayoutsMenu();
    });
  });
  _layMenuEl.querySelectorAll('.desk-lay-del').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var map = _namedLayouts();
      delete map[btn.getAttribute('data-n')];
      _setNamedLayouts(map);
      _renderLayoutsMenu();
    });
  });
  var nameInput = _layMenuEl.querySelector('.desk-lay-name');
  var saveIt = function () {
    var name = nameInput.value.trim();
    if (!name) { nameInput.focus(); return; }
    var map = _namedLayouts();
    map[name] = _stripTree(_root);
    _setNamedLayouts(map);
    _renderLayoutsMenu();
  };
  _layMenuEl.querySelector('.desk-lay-savebtn').addEventListener('click', saveIt);
  nameInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') saveIt(); });
  var shareBtn = _layMenuEl.querySelector('.desk-lay-share');
  shareBtn.addEventListener('click', function () {
    var link = _shareLink();
    var ok = function () { shareBtn.textContent = 'Copied ✓'; setTimeout(function () { shareBtn.textContent = 'Copy share link'; }, 1600); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(link).then(ok, function () { window.prompt('Share this layout:', link); });
    } else {
      window.prompt('Share this layout:', link);
    }
  });
}

function _closeLayoutsMenu() {
  if (_layMenuEl) { _layMenuEl.remove(); _layMenuEl = null; }
}

function _toggleLayoutsMenu(anchorBtn) {
  if (_layMenuEl) { _closeLayoutsMenu(); return; }
  _layMenuEl = document.createElement('div');
  _layMenuEl.className = 'desk-lay-menu';
  _renderLayoutsMenu();
  anchorBtn.parentNode.appendChild(_layMenuEl);
  var r = anchorBtn.getBoundingClientRect();
  _layMenuEl.style.top   = (r.bottom + 6) + 'px';
  _layMenuEl.style.right = Math.max(8, window.innerWidth - r.right) + 'px';
  setTimeout(function () {
    document.addEventListener('pointerdown', function outside(e) {
      if (_layMenuEl && !_layMenuEl.contains(e.target) && e.target !== anchorBtn) {
        _closeLayoutsMenu();
        document.removeEventListener('pointerdown', outside);
      }
    });
  }, 0);
}

export function initDesk() {
  _rootEl = document.getElementById('desk-root');
  if (!_rootEl) return;
  var fromHash = _treeFromHash();
  _root = fromHash || _load() || _defaultLayout();
  _booting = true;
  _bootMounts = 0;
  _layout();
  _booting = false;
  if (fromHash) {
    _save();   // a shared layout becomes the working layout
    try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
  }
  window.addEventListener('message', _onFrameMessage);

  // Shortcuts while the Desk document itself has focus (chrome, dividers);
  // desk-frame.js forwards the same combos typed inside panel frames.
  document.addEventListener('keydown', function (e) {
    var act = deskKeyAction(e);
    if (!act) return;
    var target = _activeId && _panels[_activeId] ? _activeId : _collectPanels(_root, [])[0] && _collectPanels(_root, [])[0].id;
    if (!target) return;
    e.preventDefault();
    _panelAction(target, act);
  });

  var addBtn = document.getElementById('desk-add-btn');
  if (addBtn) addBtn.addEventListener('click', _addPanelToRoot);
  var layBtn = document.getElementById('desk-layouts-btn');
  if (layBtn) layBtn.addEventListener('click', function () { _toggleLayoutsMenu(layBtn); });
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
