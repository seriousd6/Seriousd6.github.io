/* bp-lite.js — the trimmed biblepedia index for the hover/tap layer.
 *
 * The full data/biblepedia/index.json is 1.8 MB, and term tooltips + the
 * reader's word-tap/place popups were idle-fetching all of it on nearly
 * every content page — while needing only id/term/category/brief/
 * hitchcock_meaning/has_article/redirect. tools/build-assets.mjs emits
 * /assets/bp-lite.json with exactly those fields (~35% smaller raw, and the
 * dropped key_refs/nave_topics were the poorly-compressing part).
 *
 * Falls back to the full index when the lite file isn't there (dev servers
 * that only serve the repo root). Same array shape either way.
 */
'use strict';

import { _resolve } from './core.js';

var _ready = null;
var _tagReady = null;

// Tagging-layer index (P11): same array shape as bp-lite minus brief /
// hitchcock_meaning (~1/3 the bytes). Pages tag with this; the brief-carrying
// index loads only when a tooltip/popup actually needs prose.
export function loadBPTag() {
  if (_tagReady) return _tagReady;
  _tagReady = fetch(_resolve('../bp-tag.json'))
    .then(function (r) { if (!r.ok) throw new Error(String(r.status)); return r.json(); })
    .catch(function () { return loadBPLite(); });
  return _tagReady;
}

export function loadBPLite() {
  if (_ready) return _ready;
  _ready = fetch(_resolve('../bp-lite.json'))
    .then(function (r) { if (!r.ok) throw new Error(String(r.status)); return r.json(); })
    .catch(function () {
      return fetch(_resolve('../../data/biblepedia/index.json'))
        .then(function (r) { return r.ok ? r.json() : null; })
        .catch(function () { return null; });
    });
  return _ready;
}
