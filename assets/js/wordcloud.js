/* wordcloud.js — Biblical Word Cloud page
 *
 * Shape-constrained spiral word cloud. Each scope (OT, NT, genres) renders
 * words inside a thematic shape drawn on an offscreen canvas and converted
 * to a pixel bitmask. The Archimedean spiral uses an adaptive step size
 * (constant 2-pixel arc distance) so no positions are ever skipped.
 * Words that cannot be placed without overlap are simply omitted.
 */
'use strict';

import { _resolve, escHtml } from './core.js';

var FREQ_URL = _resolve('../../data/wordcloud/frequencies.json');

var _words       = [];
var _activeScope = 'all';
var _showProper  = true;
var _maskCache   = {};  // keyed by shapeKey_w_h

// Proper names — these are toggled by the "Hide names" button.
// Includes key OT patriarchs, NT apostles, and named leaders.
var PROPER_IDS = new Set([
  'H3068','H3478','H1732','H4872','H85','H87','H3327','H3290',
  'H4714','H3389','H3063','H7586','H175','H8010',
  'G2424','G5547','G4613','G2474',
  'G3972','G4074','G2491',  // Paul, Peter, John (NT supplement additions)
]);

// ── Scope → shape mapping ─────────────────────────────────────────────────────

// rotProb: fraction of eligible words (below the top-25% by frequency) that
// are rotated -90°.  Higher values help fill narrow regions of the shape.
// The cross uses 0.65 because its narrow Latin-cross arms (22% beam width)
// need rotated words to fill the tight top arm and vertical beam efficiently.
var SCOPES = [
  { id: 'all',        label: 'Whole Bible',   shape: 'oval',    minPx: 9, maxPx: 44, rotProb: 0.30, getCount: function (w) { return w.count; } },
  { id: 'ot',         label: 'Old Testament', shape: 'tablets', minPx: 9, maxPx: 40, rotProb: 0.35, getCount: function (w) { return w.ot; } },
  { id: 'nt',         label: 'New Testament', shape: 'cross',   minPx: 8, maxPx: 34, rotProb: 0.65, getCount: function (w) { return w.nt; } },
  { id: 'law',        label: 'Law',           shape: 'scroll',  minPx: 8, maxPx: 34, rotProb: 0.30, getCount: function (w) { return w.genres.law; } },
  { id: 'history',    label: 'History',       shape: 'shield',  minPx: 9, maxPx: 42, rotProb: 0.30, getCount: function (w) { return w.genres.history; } },
  { id: 'poetry',     label: 'Poetry',        shape: 'heart',   minPx: 9, maxPx: 40, rotProb: 0.30, getCount: function (w) { return w.genres.poetry; } },
  { id: 'prophecy',   label: 'Prophecy',      shape: 'trumpet', minPx: 8, maxPx: 38, rotProb: 0.45, getCount: function (w) { return w.genres.prophecy; } },
  { id: 'gospels',    label: 'Gospels',       shape: 'fish',    minPx: 8, maxPx: 34, rotProb: 0.30, getCount: function (w) { return w.genres.gospels; } },
  { id: 'acts',       label: 'Acts',          shape: 'dove',    minPx: 8, maxPx: 32, rotProb: 0.30, getCount: function (w) { return w.genres.acts; } },
  { id: 'epistles',   label: 'Epistles',      shape: 'scroll',  minPx: 8, maxPx: 36, rotProb: 0.30, getCount: function (w) { return w.genres.epistles; } },
  { id: 'apocalyptic',label: 'Revelation',    shape: 'star',    minPx: 8, maxPx: 32, rotProb: 0.35, getCount: function (w) { return w.genres.apocalyptic; } },
];

// Per-shape SVG heights (shapes have different natural aspect ratios).
// The cross is tallest — its extra height gives the long bottom arm room for words.
var SHAPE_H = {
  oval:    580, tablets: 560, cross:   820, scroll:  380,
  shield:  620, heart:   620, flame:   680, fish:    400,
  trumpet: 440, dove:    460, star:    600,
};

// ── Shape drawing functions ───────────────────────────────────────────────────
// Each function fills the shape (black) on a 2D canvas at size (w × h).

function _shapeOval(ctx, w, h) {
  ctx.beginPath();
  ctx.ellipse(w / 2, h / 2, w * 0.47, h * 0.46, 0, 0, Math.PI * 2);
  ctx.fill();
}

function _shapeTablets(ctx, w, h) {
  var margin = w * 0.03;
  var gap    = w * 0.05;
  var tabW   = (w - 2 * margin - gap) / 2;
  var top    = h * 0.05;
  var tabH   = h * 0.90;
  _oneTablet(ctx, margin,              top, tabW, tabH);
  _oneTablet(ctx, margin + tabW + gap, top, tabW, tabH);
}

function _oneTablet(ctx, x, y, w, h) {
  var r = w / 2; // arch radius = half tablet width
  ctx.beginPath();
  ctx.moveTo(x, y + h);
  ctx.lineTo(x + w, y + h);
  ctx.lineTo(x + w, y + r);
  ctx.arc(x + r, y + r, r, 0, Math.PI, true);
  ctx.closePath();
  ctx.fill();
}

function _shapeCross(ctx, w, h) {
  // Latin cross: crossbar placed at ~1/4 from top gives the classic
  // short-top / long-bottom arm ratio (~1:3). Narrower beams (22% / 20%)
  // make the silhouette read as a cross rather than a plus sign.
  var vw = w * 0.22;            // vertical beam width
  var hh = h * 0.20;            // horizontal beam height
  var vx = (w - vw) / 2;
  var hy = h * 0.22;            // crossbar top-edge at 22% — top arm ≈17%, bottom arm ≈57%
  ctx.fillRect(vx, h * 0.03, vw, h * 0.94);   // vertical beam, nearly full height
  ctx.fillRect(w * 0.06, hy, w * 0.88, hh);   // horizontal beam
}

function _shapeShield(ctx, w, h) {
  ctx.beginPath();
  ctx.moveTo(w * 0.05, h * 0.05);
  ctx.lineTo(w * 0.95, h * 0.05);
  ctx.lineTo(w * 0.95, h * 0.58);
  ctx.quadraticCurveTo(w * 0.95, h * 0.84, w * 0.50, h * 0.96);
  ctx.quadraticCurveTo(w * 0.05, h * 0.84, w * 0.05, h * 0.58);
  ctx.closePath();
  ctx.fill();
}

function _shapeHeart(ctx, w, h) {
  var cx = w / 2;
  var r  = w * 0.265;
  var ty = h * 0.33;
  // Two circles form the top lobes
  ctx.beginPath(); ctx.arc(cx - r, ty, r, 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(cx + r, ty, r, 0, Math.PI * 2); ctx.fill();
  // Triangle body pointing down
  ctx.beginPath();
  ctx.moveTo(w * 0.04, ty);
  ctx.lineTo(w * 0.96, ty);
  ctx.lineTo(cx, h * 0.96);
  ctx.closePath();
  ctx.fill();
}

function _shapeFlame(ctx, w, h) {
  ctx.beginPath();
  ctx.moveTo(w * 0.50, h * 0.03);
  ctx.bezierCurveTo(w * 0.88, h * 0.20, w * 0.90, h * 0.58, w * 0.78, h * 0.74);
  ctx.bezierCurveTo(w * 0.68, h * 0.88, w * 0.60, h * 0.95, w * 0.50, h * 0.97);
  ctx.bezierCurveTo(w * 0.40, h * 0.95, w * 0.32, h * 0.88, w * 0.22, h * 0.74);
  ctx.bezierCurveTo(w * 0.10, h * 0.58, w * 0.12, h * 0.20, w * 0.50, h * 0.03);
  ctx.fill();
}

function _shapeFish(ctx, w, h) {
  var cy   = h / 2;
  var nose = w * 0.05;
  var tail = w * 0.76;
  var mid  = (nose + tail) / 2;
  var ry   = h * 0.44;
  // Body (lens shape)
  ctx.beginPath();
  ctx.moveTo(nose, cy);
  ctx.quadraticCurveTo(mid, cy - ry, tail, cy);
  ctx.quadraticCurveTo(mid, cy + ry, nose, cy);
  ctx.fill();
  // Tail fin
  ctx.beginPath();
  ctx.moveTo(tail, cy);
  ctx.lineTo(w * 0.97, cy - ry * 0.65);
  ctx.lineTo(w * 0.97, cy + ry * 0.65);
  ctx.closePath();
  ctx.fill();
}

function _shapeScroll(ctx, w, h) {
  // Horizontal capsule (scroll shape)
  var r = h * 0.44;
  var lx = r, rx = w - r;
  ctx.beginPath();
  ctx.arc(lx, h / 2, r, Math.PI / 2, -Math.PI / 2, true);
  ctx.arc(rx, h / 2, r, -Math.PI / 2, Math.PI / 2, true);
  ctx.closePath();
  ctx.fill();
}

function _shapeTrumpet(ctx, w, h) {
  // Side-view trumpet: bell (right) → narrow tube → small mouthpiece flare (left).
  // The bell occupies most of the right half and is the main word-placement area;
  // the tube is narrow so rotated words fill it naturally.
  var bx = w * 0.50;   // x where the tube widens into the bell
  var ty = h * 0.37;   // tube top
  var by = h * 0.63;   // tube bottom

  ctx.beginPath();
  ctx.moveTo(w * 0.03, h * 0.43);                                                      // mouthpiece tip top
  ctx.quadraticCurveTo(w * 0.12, h * 0.35, w * 0.22, ty);                             // mouthpiece flare → tube top
  ctx.lineTo(bx, ty);                                                                    // along tube top
  ctx.bezierCurveTo(w * 0.68, h * 0.18, w * 0.84, h * 0.07, w * 0.97, h * 0.06);    // bell top flare
  ctx.lineTo(w * 0.97, h * 0.94);                                                       // bell right edge
  ctx.bezierCurveTo(w * 0.84, h * 0.93, w * 0.68, h * 0.82, bx, by);                // bell bottom flare
  ctx.lineTo(w * 0.22, by);                                                              // along tube bottom
  ctx.quadraticCurveTo(w * 0.12, h * 0.65, w * 0.03, h * 0.57);                      // mouthpiece flare → tip bottom
  ctx.closePath();
  ctx.fill();
}

function _shapeDove(ctx, w, h) {
  // Dove with spread wings, viewed from slightly above.
  // Single closed path: left wingtip → wings sweep up → head arc → right wingtip
  // → trailing edges back → forked tail → close.
  var cx = w / 2;
  ctx.beginPath();
  ctx.moveTo(w * 0.03, h * 0.44);                                                     // left wingtip
  ctx.bezierCurveTo(w * 0.10, h * 0.06, w * 0.26, h * 0.20, cx - w * 0.10, h * 0.38); // left wing leading edge
  ctx.quadraticCurveTo(cx, h * 0.16, cx + w * 0.10, h * 0.38);                        // head arc
  ctx.bezierCurveTo(w * 0.74, h * 0.20, w * 0.90, h * 0.06, w * 0.97, h * 0.44);     // right wing leading edge
  ctx.bezierCurveTo(w * 0.84, h * 0.54, cx + w * 0.16, h * 0.58, cx + w * 0.12, h * 0.68); // right wing trailing edge
  ctx.lineTo(cx + w * 0.16, h * 0.92);                                                 // right tail prong
  ctx.lineTo(cx,             h * 0.78);                                                 // tail notch
  ctx.lineTo(cx - w * 0.16, h * 0.92);                                                 // left tail prong
  ctx.lineTo(cx - w * 0.12, h * 0.68);                                                 // back to left wing join
  ctx.bezierCurveTo(cx - w * 0.16, h * 0.58, w * 0.16, h * 0.54, w * 0.03, h * 0.44); // left wing trailing edge
  ctx.closePath();
  ctx.fill();
}

function _shapeStar(ctx, w, h) {
  var n  = 6; // six-pointed star
  var cx = w / 2, cy = h / 2;
  var R  = Math.min(w, h) * 0.46;
  var r  = R * 0.44;
  ctx.beginPath();
  for (var i = 0; i < n * 2; i++) {
    var ang = (i * Math.PI / n) - Math.PI / 2;
    var len = i % 2 === 0 ? R : r;
    var x   = cx + len * Math.cos(ang);
    var y   = cy + len * Math.sin(ang);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.closePath();
  ctx.fill();
}

var SHAPE_FNS = {
  oval:    _shapeOval,
  tablets: _shapeTablets,
  cross:   _shapeCross,
  shield:  _shapeShield,
  heart:   _shapeHeart,
  flame:   _shapeFlame,
  fish:    _shapeFish,
  scroll:  _shapeScroll,
  trumpet: _shapeTrumpet,
  dove:    _shapeDove,
  star:    _shapeStar,
};

// ── Pixel mask ────────────────────────────────────────────────────────────────

// INTENT: Rasterise the SVG shape onto an offscreen canvas at the exact render
//   dimensions, then build a Uint8Array mask where 1 = valid placement pixel
//   (alpha > 64). The cache key includes w and h so the mask is rebuilt when
//   the window is resized — stale masks would place words outside the shape.
// CHANGE? If SVG_W/SVG_H calculation changes, also update any callers that
//   pass dimensions; a mismatch between mask size and SVG size misaligns placement.
// VERIFY: With browser DevTools, inspect _maskCache after render; the key should
//   be "{shape}_{svgWidth}_{svgHeight}" matching the rendered SVG dimensions.
function _buildMask(shapeKey, w, h) {
  var key = shapeKey + '_' + w + '_' + h;
  if (_maskCache[key]) return _maskCache[key];

  var fn = SHAPE_FNS[shapeKey];
  if (!fn) return null;

  var c = document.createElement('canvas');
  c.width = w; c.height = h;
  var ctx = c.getContext('2d');
  ctx.fillStyle = '#000';
  fn(ctx, w, h);

  var raw  = ctx.getImageData(0, 0, w, h).data;
  var mask = new Uint8Array(w * h);
  for (var i = 0, n = mask.length; i < n; i++) {
    mask[i] = raw[i * 4 + 3] > 64 ? 1 : 0;
  }

  var result = { mask: mask, w: w, h: h };
  _maskCache[key] = result;
  return result;
}

// INTENT: Test whether a bw×bh box at (x,y) fits entirely within the mask.
//   Checks four corners first (O(1) fast rejection for out-of-shape positions),
//   then samples interior on a grid whose step is proportional to the smaller
//   bounding-box dimension — large words get denser sampling than small ones.
// CHANGE? If SVG_W/SVG_H calculation changes, the mask cache key must change too
//   (see _buildMask) or this function will test against a stale mask.
// VERIFY: Render the OT (tablets) scope; confirm words stay within arch boundaries.
function _fitsInMask(m, x, y, bw, bh) {
  var x0 = Math.floor(x),      y0 = Math.floor(y);
  var x1 = Math.ceil(x + bw),  y1 = Math.ceil(y + bh);
  if (x0 < 0 || y0 < 0 || x1 >= m.w || y1 >= m.h) return false;

  // Always check four corners
  var mw = m.w, mask = m.mask;
  if (!mask[y0*mw+x0] || !mask[y0*mw+x1] ||
      !mask[y1*mw+x0] || !mask[y1*mw+x1]) return false;

  // Sample interior on a grid
  var step = Math.max(4, Math.floor(Math.min(bw, bh) / 3));
  for (var py = y0; py <= y1; py += step) {
    for (var px = x0; px <= x1; px += step) {
      if (!mask[py * mw + px]) return false;
    }
  }
  return true;
}

// ── Rendering ─────────────────────────────────────────────────────────────────

function _render() {
  var svgWrap = document.getElementById('wc-svg-wrap');
  if (!svgWrap) return;
  svgWrap.innerHTML = '<div class="wc-loading">Building cloud…</div>';
  setTimeout(function () { _doRender(svgWrap); }, 30);
}

function _doRender(svgWrap) {
  var scope = SCOPES.find(function (s) { return s.id === _activeScope; }) || SCOPES[0];

  // Filter and sort words by active-scope count
  var items = _words.map(function (w) {
    return { w: w, count: scope.getCount(w) };
  }).filter(function (item) {
    if (item.count === 0) return false;
    if (!_showProper && PROPER_IDS.has(item.w.id)) return false;
    return true;
  });
  items.sort(function (a, b) { return b.count - a.count; });
  items = items.slice(0, 150);

  if (!items.length) {
    svgWrap.innerHTML = '<p class="wc-empty">No words for this scope.</p>';
    return;
  }

  // Font-size scaling: log-linear from scope's minPx to maxPx
  var maxC   = items[0].count;
  var minC   = items[items.length - 1].count;
  var lmax   = Math.log(maxC + 1);
  var lmin   = Math.log(minC + 1);
  var lrng   = lmax - lmin || 1;
  var MIN_PX = scope.minPx || 9;
  var MAX_PX = scope.maxPx || 40;

  function fontSize(c) {
    return Math.round(MIN_PX + ((Math.log(c + 1) - lmin) / lrng) * (MAX_PX - MIN_PX));
  }

  // Measure text widths via offscreen canvas
  var cvs = document.createElement('canvas');
  var mctx = cvs.getContext('2d');
  function measure(text, size) {
    mctx.font = 'bold ' + size + 'px system-ui, sans-serif';
    return { w: Math.ceil(mctx.measureText(text).width) + 6, h: size + 8 };
  }

  var SVG_W = Math.min(svgWrap.offsetWidth || 800, 900);
  var SVG_H = SHAPE_H[scope.shape] || 600;

  var maskData = _buildMask(scope.shape, SVG_W, SVG_H);

  // rotProb drives how many eligible words (below the top-20% by frequency)
  // get rotated -90°.  Shapes with narrow arms (cross, flame) use higher values.
  var rotProb = scope.rotProb !== undefined ? scope.rotProb : 0.35;

  // Prepare word objects.
  // Top 20% by frequency always stay horizontal so the most prominent words
  // remain easy to read.  Below that, each word is randomly rotated with
  // probability rotProb, using -90° (reads bottom-to-top, standard convention).
  var words = items.map(function (item, idx) {
    var size  = fontSize(item.count);
    var dim   = measure(item.w.gloss, size);
    var pct   = idx / (items.length - 1 || 1);
    var rot   = (pct < 0.20 || Math.random() > rotProb) ? 0 : -90;
    return {
      w:       item.w,
      count:   item.count,
      size:    size,
      dim:     dim,
      rot:     rot,
      color:   _wordColor(item.w.lang, pct),
      x:       0,
      y:       0,
      placed:  false
    };
  });

  // ── Archimedean spiral placement ──────────────────────────────────────────
  // INTENT: Place each word by walking an Archimedean spiral (r = b·θ) outward
  //   from a seed pixel. The adaptive step TARGET_D / Math.max(r, TARGET_D) keeps
  //   arc-distance constant (not angular-distance) so words pack evenly at all
  //   radii. b=5 gives ~450px max radius across MAX_ITER steps — enough to reach
  //   any part of the largest shape at the default SVG dimensions.
  // CHANGE? If SVG_W/SVG_H calculation changes, update the _buildMask cache key
  //   (it includes dimensions) or stale masks will be reused after a window resize.
  // VERIFY: Render the OT (tablets) scope; all words should stay inside the arch
  //   boundary with none appearing in the gap between the two tablet halves.

  var cx = SVG_W / 2, cy = SVG_H / 2;
  var placedBoxes = [];
  var TARGET_D = 2;        // px between consecutive spiral positions
  var MAX_ITER = 8000;
  var b = 5;               // spiral expansion rate (≈450px radius in MAX_ITER steps)
  var RESTART_AFTER = 120; // teleport to new seed after N consecutive mask misses

  // Pre-sample 200 valid seed pixels from the mask for round-robin seeding.
  var seedPool = [];
  if (maskData) {
    for (var sp = 0; sp < 500 && seedPool.length < 200; sp++) {
      var rpx = Math.floor(Math.random() * SVG_W);
      var rpy = Math.floor(Math.random() * SVG_H);
      if (maskData.mask[rpy * maskData.w + rpx]) seedPool.push({ x: rpx, y: rpy });
    }
  }
  var seedIdx = 0;

  // _spiralPlace: try to fit bw×bh using a restartable Archimedean spiral.
  // Closes over b, TARGET_D, maskData, placedBoxes, SVG_W, SVG_H, seedPool, RESTART_AFTER.
  function _spiralPlace(bw, bh, startX, startY, iters) {
    var sx = startX, sy = startY;
    var theta = Math.random() * Math.PI * 2;
    var missStreak = 0;
    for (var i = 0; i < iters; i++) {
      var r = b * theta;
      var x = sx + r * Math.cos(theta) - bw / 2;
      var y = sy + r * Math.sin(theta) - bh / 2;
      theta += TARGET_D / Math.max(r, TARGET_D);

      if (maskData) {
        if (!_fitsInMask(maskData, x, y, bw, bh)) {
          // INTENT: After RESTART_AFTER consecutive out-of-mask positions the spiral
          //   has escaped a narrow arm (e.g. the cross's vertical beam). Teleporting
          //   to a random seedPool pixel restarts a fresh local spiral inside the
          //   shape, turning one long useless sweep into many productive short ones.
          if (++missStreak >= RESTART_AFTER && seedPool.length > 0) {
            var ns = seedPool[Math.floor(Math.random() * seedPool.length)];
            sx = ns.x; sy = ns.y;
            theta = Math.random() * Math.PI * 2;
            missStreak = 0;
          }
          continue;
        }
      } else {
        if (x < 2 || x + bw > SVG_W - 2 || y < 2 || y + bh > SVG_H - 2) continue;
      }
      missStreak = 0;

      var ok = true;
      for (var j = 0; j < placedBoxes.length; j++) {
        var p = placedBoxes[j];
        if (x < p.x + p.w && x + bw > p.x && y < p.y + p.h && y + bh > p.y) {
          ok = false; break;
        }
      }
      if (ok) return { x: x, y: y };
    }
    return null;
  }

  // First pass: top 25% by rank spiral from center; the rest from random mask pixels.
  words.forEach(function (word, wi) {
    var bw = word.rot === 0 ? word.dim.w : word.dim.h;
    var bh = word.rot === 0 ? word.dim.h : word.dim.w;
    var sx, sy;
    if (wi < Math.ceil(words.length * 0.25) || seedPool.length === 0) {
      sx = cx; sy = cy;
    } else {
      var seed = seedPool[seedIdx % seedPool.length];
      seedIdx++;
      sx = seed.x; sy = seed.y;
    }
    var pos = _spiralPlace(bw, bh, sx, sy, MAX_ITER);
    if (pos) {
      word.x = pos.x; word.y = pos.y; word.placed = true;
      placedBoxes.push({ x: pos.x, y: pos.y, w: bw, h: bh });
    }
  });

  // INTENT: Retry unplaced words with the opposite rotation. A word too wide to
  //   fit horizontally in a narrow arm (e.g. the cross's vertical beam) often
  //   fits rotated 90°, so flipping rotation before discarding recovers ~10–15%
  //   of words that would otherwise be silently dropped.
  words.forEach(function (word) {
    if (word.placed) return;
    word.rot = word.rot === 0 ? -90 : 0;
    var bw = word.rot === 0 ? word.dim.w : word.dim.h;
    var bh = word.rot === 0 ? word.dim.h : word.dim.w;
    var rsx = seedPool.length > 0 ? seedPool[Math.floor(Math.random() * seedPool.length)].x : cx;
    var rsy = seedPool.length > 0 ? seedPool[Math.floor(Math.random() * seedPool.length)].y : cy;
    var pos = _spiralPlace(bw, bh, rsx, rsy, Math.floor(MAX_ITER / 2));
    if (pos) {
      word.x = pos.x; word.y = pos.y; word.placed = true;
      placedBoxes.push({ x: pos.x, y: pos.y, w: bw, h: bh });
    } else {
      word.rot = word.rot === 0 ? -90 : 0; // restore original rotation if still unplaced
    }
  });

  // ── Render SVG ────────────────────────────────────────────────────────────
  var placed = words.filter(function (w) { return w.placed; });
  if (!placed.length) {
    svgWrap.innerHTML = '<p class="wc-empty">Could not fit any words in this shape.</p>';
    return;
  }

  var placedLangs = new Set(placed.map(function (ww) { return ww.w.lang; }));
  _updateLegend(placedLangs);

  var parts = [
    '<svg viewBox="0 0 ' + SVG_W + ' ' + SVG_H + '" ' +
    'xmlns="http://www.w3.org/2000/svg" class="wc-svg" ' +
    'role="img" aria-label="Biblical word cloud">'
  ];

  words.forEach(function (word, idx) {
    if (!word.placed) return;
    var bw = word.rot === 0 ? word.dim.w : word.dim.h;
    var bh = word.rot === 0 ? word.dim.h : word.dim.w;
    var cx = word.x + bw / 2;
    var cy = word.y + bh / 2;
    // Baseline position — for 0°: near bottom of box; for −90°: same offset
    // applied in natural coords, which after rotation puts baseline at box right.
    var tx = cx;
    var ty = word.rot === 0
      ? word.y + word.dim.h - 4
      : cy + word.dim.h / 2 - 4;
    var xformAttr = word.rot === 0
      ? ''
      : ' transform="rotate(-90 ' + cx.toFixed(1) + ' ' + cy.toFixed(1) + ')"';
    parts.push(
      '<text' + xformAttr + ' ' +
      'x="' + tx.toFixed(1) + '" ' +
      'y="' + ty.toFixed(1) + '" ' +
      'text-anchor="middle" ' +
      'font-size="' + word.size + '" ' +
      'font-weight="bold" ' +
      'font-family="system-ui, sans-serif" ' +
      'fill="' + word.color + '" ' +
      'class="wc-word" ' +
      'data-idx="' + idx + '" ' +
      'tabindex="0" role="button" ' +
      'aria-label="' + escHtml(word.w.gloss) + ', ' + word.count.toLocaleString() + ' occurrences">' +
      escHtml(word.w.gloss) +
      '</text>'
    );
  });

  parts.push('</svg>');
  svgWrap.innerHTML = parts.join('');

  // Wire interaction
  var svg = svgWrap.querySelector('.wc-svg');
  if (svg) {
    svg.addEventListener('click', function (e) {
      var el = e.target.closest('.wc-word');
      if (el) _showDetail(words[parseInt(el.dataset.idx, 10)]);
    });
    svg.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      var el = e.target.closest && e.target.closest('.wc-word');
      if (!el) return;
      e.preventDefault();
      _showDetail(words[parseInt(el.dataset.idx, 10)]);
    });
  }
}

// ── Color ──────────────────────────────────────────────────────────────────────
// Hebrew → warm (amber/rust), Greek → cool (teal/indigo), shade varies by rank

var HEB_COLORS = ['#7c2d12','#b45309','#a16207','#92400e','#854d0e','#9a3412','#78350f'];
var GRK_COLORS = ['#1e3a5f','#155e75','#164e63','#1d4ed8','#1e40af','#0f766e','#075985'];

function _wordColor(lang, pct) {
  var pal = lang === 'H' ? HEB_COLORS : GRK_COLORS;
  var idx = Math.min(Math.floor(pct * pal.length), pal.length - 1);
  return pal[idx];
}

// ── Scope filter buttons ──────────────────────────────────────────────────────

function _buildScopeButtons() {
  var wrap = document.getElementById('wc-scope-bar');
  if (!wrap) return;
  SCOPES.forEach(function (scope) {
    var btn = document.createElement('button');
    btn.className  = 'wc-scope-btn' + (scope.id === 'all' ? ' wc-scope-btn--active' : '');
    btn.textContent = scope.label;
    btn.dataset.scopeId = scope.id;
    btn.title = scope.shape.charAt(0).toUpperCase() + scope.shape.slice(1) + ' shape';
    btn.addEventListener('click', function () {
      _activeScope = scope.id;
      wrap.querySelectorAll('.wc-scope-btn').forEach(function (b) {
        b.classList.toggle('wc-scope-btn--active', b.dataset.scopeId === scope.id);
      });
      _render();
    });
    wrap.appendChild(btn);
  });
}

function _wireProperToggle() {
  var btn = document.getElementById('wc-proper-toggle');
  if (!btn) return;
  // Restore persisted toggle state
  var stored = localStorage.getItem('bsw_wc_showProper');
  if (stored !== null) {
    _showProper = stored !== 'false';
    btn.classList.toggle('wc-proper-toggle--on', _showProper);
    btn.textContent = _showProper ? 'Hide names' : 'Show names';
  }
  btn.addEventListener('click', function () {
    _showProper = !_showProper;
    localStorage.setItem('bsw_wc_showProper', String(_showProper));
    btn.classList.toggle('wc-proper-toggle--on', _showProper);
    btn.textContent = _showProper ? 'Hide names' : 'Show names';
    _render();
  });
}

// ── Detail panel ──────────────────────────────────────────────────────────────

function _showDetail(word) {
  var panel    = document.getElementById('wc-detail');
  var nameEl   = document.getElementById('wc-detail-gloss');
  var idEl     = document.getElementById('wc-detail-id');
  var lemmaEl  = document.getElementById('wc-detail-lemma');
  var countEl  = document.getElementById('wc-detail-count');
  var testEl   = document.getElementById('wc-detail-testament');
  var defEl    = document.getElementById('wc-detail-def');
  var linkEl   = document.getElementById('wc-detail-word-link');
  if (!panel || !word) return;

  var w         = word.w;
  var langName  = w.lang === 'H' ? 'Hebrew' : 'Greek';
  var testament = w.ot > w.nt ? 'Old Testament' : 'New Testament';

  if (nameEl)  nameEl.textContent  = w.gloss;
  if (idEl)    idEl.textContent    = w.id + ' — ' + langName;
  if (lemmaEl) lemmaEl.textContent = w.lemma + (w.translit ? ' (' + w.translit + ')' : '');
  if (countEl) countEl.textContent = word.count.toLocaleString() + ' occurrences';
  if (testEl)  testEl.textContent  = testament + ' word';
  if (defEl)   defEl.innerHTML     = _buildBars(w);

  if (linkEl) {
    linkEl.href = '../word/?s=' + encodeURIComponent(w.id) + '&from=wordcloud';
  }

  panel.hidden = false;
  panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function _buildBars(w) {
  var bars = [
    { label: 'Law',        count: w.genres.law },
    { label: 'History',    count: w.genres.history },
    { label: 'Poetry',     count: w.genres.poetry },
    { label: 'Prophecy',   count: w.genres.prophecy },
    { label: 'Gospels',    count: w.genres.gospels },
    { label: 'Acts',       count: w.genres.acts },
    { label: 'Epistles',   count: w.genres.epistles },
    { label: 'Revelation', count: w.genres.apocalyptic },
  ].filter(function (b) { return b.count > 0; });

  if (!bars.length) return '';
  var maxB = Math.max.apply(null, bars.map(function (b) { return b.count; }));

  return '<div class="wc-detail-bars">' +
    bars.map(function (b) {
      var pct = Math.round((b.count / maxB) * 100);
      return '<div class="wc-detail-bar-row">' +
        '<span class="wc-detail-bar-label">' + escHtml(b.label) + '</span>' +
        '<div class="wc-detail-bar-track"><div class="wc-detail-bar-fill" style="width:' + pct + '%"></div></div>' +
        '<span class="wc-detail-bar-count">' + b.count.toLocaleString() + '</span>' +
        '</div>';
    }).join('') +
    '</div>';
}

function _updateLegend(langs) {
  var hebEl = document.getElementById('wc-legend-heb');
  var grkEl = document.getElementById('wc-legend-grk');
  if (hebEl) hebEl.style.display = langs.has('H') ? '' : 'none';
  if (grkEl) grkEl.style.display = langs.has('G') ? '' : 'none';
}

document.addEventListener('click', function (e) {
  if (e.target && e.target.id === 'wc-detail-close') {
    var panel = document.getElementById('wc-detail');
    if (panel) panel.hidden = true;
  }
});

// ── Init ──────────────────────────────────────────────────────────────────────

export function initWordCloudPage() {
  if (!document.getElementById('wc-container')) return;

  fetch(FREQ_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      _words = data.words || [];
      _buildScopeButtons();
      _wireProperToggle();
      _render();

      // Re-render when container width changes by more than 20px (e.g. sidebar open/close, orientation change)
      var _wcLastW = 0;
      var _wcResizeTimer = null;
      var svgWrapEl = document.getElementById('wc-svg-wrap');
      if (svgWrapEl && typeof ResizeObserver !== 'undefined') {
        _wcLastW = svgWrapEl.offsetWidth;
        new ResizeObserver(function (entries) {
          var newW = Math.round(entries[0].contentRect.width);
          if (Math.abs(newW - _wcLastW) < 20) return;
          _wcLastW = newW;
          clearTimeout(_wcResizeTimer);
          _wcResizeTimer = setTimeout(_render, 100);
        }).observe(svgWrapEl);
      }
    })
    .catch(function (err) {
      console.error('[WordCloud] failed to load frequencies:', err);
      var c = document.getElementById('wc-container');
      if (c) c.innerHTML = '<p style="padding:2rem;color:var(--color-muted)">Unable to load word frequency data.</p>';
    });
}
