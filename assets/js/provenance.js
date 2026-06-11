/**
 * provenance.js — source attribution helpers for rendered data.
 *
 * Loaded as a plain <script> (not a module) alongside main.js so pages can
 * call window.BSW_PROVENANCE.getSourceBadge() after any data fetch completes.
 *
 * The provenance manifest (data/provenance.json) maps path-prefix keys to
 * source metadata. Pages pass the matching key (e.g. "commentary/barnes")
 * and get back a ready-to-insert HTML badge string.
 */

(function () {
  'use strict';

  /* ── Root detection — mirrors main.js approach ── */
  // INTENT: Derive data URL root from this script's own src so the manifest
  //   fetch works from any subdirectory without a hardcoded absolute path.
  // CHANGE? If assets/js/ moves, update the '../..' offset below.
  // VERIFY: window.BSW_PROVENANCE._root should equal the site root URL.
  var _src  = (document.currentScript && document.currentScript.src) || '';
  var _root = _src ? new URL('../../', _src).href : '/';

  var _manifest = null;   /* populated after first fetch */
  var _pending  = [];     /* callbacks waiting for manifest load */

  function _load(cb) {
    if (_manifest) { cb(_manifest); return; }
    _pending.push(cb);
    if (_pending.length > 1) return;   /* already fetching */
    fetch(_root + 'data/provenance.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        _manifest = data;
        var q = _pending.slice(); _pending = [];
        for (var i = 0; i < q.length; i++) q[i](_manifest);
      })
      .catch(function () {
        _manifest = {};
        var q = _pending.slice(); _pending = [];
        for (var i = 0; i < q.length; i++) q[i](_manifest);
      });
  }

  /* ── Public API ── */

  /**
   * getSourceBadge(dataType, [onReady])
   *
   * Returns an HTML string badge for the given data type key (e.g. "commentary/barnes").
   * If the manifest hasn't loaded yet, returns a placeholder and calls onReady(badgeHtml)
   * once it has — caller can then replace the placeholder in the DOM.
   *
   * For synchronous use after you know the manifest is loaded, omit onReady.
   */
  function getSourceBadge(dataType, onReady) {
    // INTENT: Two-phase design — immediate placeholder so callers don't have to
    //   async-wrap every render path, plus an optional callback for live DOM updates.
    //   The placeholder id is stable so callers can querySelector for it.
    // CHANGE? If badge HTML structure changes, update about/index.html inline examples too.
    // VERIFY: In verse-study, "Barnes Notes · Public Domain" chip appears under commentary header.

    var placeholderId = 'prov-badge-' + dataType.replace(/\//g, '-') + '-' + Date.now();

    function _build(m) {
      var entry = m[dataType];
      if (!entry) return '';
      var isAI = (entry.type === 'ai_assisted');
      var cls  = isAI ? 'src-badge src-badge--ai' : 'src-badge';
      var text = entry.name;
      if (entry.author) text += ' · ' + entry.author;
      if (entry.year)   text += ' · ' + entry.year;
      if (!isAI && entry.license) text += ' · ' + entry.license;
      if (isAI) {
        text += ' · AI-assisted';
        var link = entry.about_url || '/about/';
        return '<span class="' + cls + '">' + _esc(text) + ' · <a href="' + link + '">details</a></span>';
      }
      return '<span class="' + cls + '">' + _esc(text) + '</span>';
    }

    if (_manifest) {
      return _build(_manifest);
    }

    /* manifest not yet loaded — return placeholder and fill async */
    var placeholder = '<span id="' + placeholderId + '" class="src-badge" style="visibility:hidden"></span>';
    if (onReady) {
      _load(function (m) {
        var badge = _build(m);
        var el = document.getElementById(placeholderId);
        if (el && badge) { el.outerHTML = badge; }
        onReady(badge);
      });
    }
    return placeholder;
  }

  /** Preload the manifest eagerly (call once on pages that heavily use badges) */
  function preload() { _load(function () {}); }

  function _esc(s) {
    return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  /* ── Expose globally ── */
  window.BSW_PROVENANCE = {
    getSourceBadge: getSourceBadge,
    preload: preload,
    _root: _root
  };

}());
