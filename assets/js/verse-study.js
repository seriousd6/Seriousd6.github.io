/* verse-study.js — Verse Study page */
'use strict';

import {
  READER_URL, SEARCH_URL, WORD_URL, VERSE_STUDY_URL,
  metaVersions, metaBooks,
  COMMENTARY_SOURCES, FATHER_SLUGS,
  getVersion, onVersionChange, escHtml,
  parseRef, resolveVerses, loadBook,
  loadCrossRefs, loadCommentary, loadEchoes,
  loadInterlinear, loadStrongs, loadLexicon,
  parseCrossRefEntry, _compareCanonical,
  getCommentarySource, setCommentarySource,
  _hitchLoad, _hitchMap, _hitchData,
  _setOGMeta, _resolve
} from './core.js';
import { getNotes } from './storage.js';
import { _HL_COLORS } from './storage.js';
import { wireRefEl, wireRefLinks, applyHighlights } from './wire.js';
import { expandMorphCode } from './interlinear.js';
// loadParallels retained for reference — verse-study now uses loadEchoes (see AUD-9)
import { loadParallels } from './parallels.js';
import {
  _renderNotesPanel, _shareVerseAsImage,
  _extractCommHtml, _commAttr
} from './modal.js';
import {
  renderModalConfessions, renderModalFathers,
  renderVSTopics, renderVSDictionary,
  _dictEntriesForVerse, loadLibVerseIndex
} from './library.js';
import { autoTagTerms } from './terms.js';

// ── Module state ──────────────────────────────────────────────────────────────
var _vsActiveToken = null;
var _vsWordPanelEl = null;
var _vsCurrentRef  = null;
var _vsNavObserver = null;

var _ECHO_TYPE_META = {
  'quote':       { label: 'Direct Quote',   cls: 'vs-echo-badge--quote' },
  'allusion':    { label: 'Allusion',       cls: 'vs-echo-badge--allusion' },
  'fulfillment': { label: 'Fulfillment',    cls: 'vs-echo-badge--fulfillment' },
  'type':        { label: 'Type',           cls: 'vs-echo-badge--type' },
  'shadow':      { label: 'Shadow',         cls: 'vs-echo-badge--shadow' },
  'theme':       { label: 'Theme',          cls: 'vs-echo-badge--theme' }
};

var _PARALLEL_TYPE_META = {
  'parallel':        { icon: '⇌', label: 'Parallel',      cls: 'reader-parallel-badge--parallel' },
  'fulfillment':     { icon: '✓', label: 'Fulfilled in',   cls: 'reader-parallel-badge--fulfillment' },
  'prophecy-source': { icon: '⌖', label: 'Prophesied in', cls: 'reader-parallel-badge--prophecy' },
  'quotation':       { icon: '«', label: 'Quoted in',      cls: 'reader-parallel-badge--quotation' }
};

// Commentary source is read fresh via getCommentarySource() (see core.js) so
// that changes made in the modal are reflected here without a page reload.

// ── initVerseStudyPage ────────────────────────────────────────────────────────
// INTENT: Entry point called by app.js on page load. Parses the ?ref= URL param to
//   load the focal verse, seeds localStorage state for version preference, context-view
//   setting, and memory mode from URL params so deep-links can set initial UI state.
// CHANGE? If localStorage keys change, update all three: bsw_version (line 65),
//   bsw_dissect_ctx (lines 93/110), bsw_memory (lines 121/130/140). If app.js call
//   site changes, also update modal.js line 426 which links to verse-study/?ref=.
// VERIFY: Load verse-study/?ref=John+3:16 — focal verse text renders; version selector
//   shows the saved version; ?v=KJV in URL overrides localStorage and selects KJV.
export function initVerseStudyPage() {
  var params = new URLSearchParams(window.location.search);
  var refStr = params.get('ref') || '';
  var vOverride = params.get('v') || '';
  if (vOverride && metaVersions && metaVersions.find(function (mv) { return mv.id === vOverride; })) {
    localStorage.setItem('bsw_version', vOverride);
  }

  var focalEl = document.getElementById('vs-focal-text');
  if (!refStr) {
    if (focalEl) focalEl.textContent = 'No verse specified. Try: ?ref=John+3:16';
    return;
  }

  var parsed = parseRef(refStr);
  if (!parsed) {
    if (focalEl) focalEl.textContent = 'Could not parse reference: ' + refStr;
    return;
  }

  _setOGMeta(parsed.display + ' — Verse Study', parsed.display + ' — cross-references, commentary, parallel passages, and word study.');

  var headerRef = document.getElementById('vs-header-ref');
  if (headerRef) headerRef.textContent = parsed.display;
  document.title = parsed.display + ' — Verse Study — Bible Study';

  var backLink = document.getElementById('vs-back-link');
  if (backLink) {
    backLink.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch);
    backLink.textContent = '← ' + parsed.bookName + ' ' + parsed.ch + ' in Reader';
  }

  var CTX_KEY = 'bsw_dissect_ctx';
  var ctxOn = localStorage.getItem(CTX_KEY) !== '0';
  var ctxToggle = document.getElementById('vs-context-toggle');

  function applyCtx(on) {
    var prev = document.getElementById('vs-context-prev');
    var next = document.getElementById('vs-context-next');
    if (prev) { if (on) prev.removeAttribute('hidden'); else prev.setAttribute('hidden', ''); }
    if (next) { if (on) next.removeAttribute('hidden'); else next.setAttribute('hidden', ''); }
    if (ctxToggle) {
      ctxToggle.classList.toggle('vs-context-btn--on', on);
      ctxToggle.setAttribute('aria-pressed', on ? 'true' : 'false');
    }
  }

  if (ctxToggle) {
    ctxToggle.addEventListener('click', function () {
      ctxOn = !ctxOn;
      localStorage.setItem(CTX_KEY, ctxOn ? '1' : '0');
      applyCtx(ctxOn);
    });
  }

  // Memory button
  var vsMemBtn = document.getElementById('vs-memory-btn');
  if (vsMemBtn && parsed.v) {
    var vsMemRef = parsed.bookName + ' ' + parsed.ch + ':' + parsed.v;
    function _vsUpdateMemBtn() {
      try {
        var state = JSON.parse(localStorage.getItem('bsw_memory') || '{}');
        var has = !!state[vsMemRef];
        vsMemBtn.textContent = has ? '⭐ Memorizing' : '☆ Memorize';
        vsMemBtn.classList.toggle('vs-context-btn--on', has);
      } catch (e) {}
    }
    _vsUpdateMemBtn();
    vsMemBtn.addEventListener('click', function () {
      try {
        var state = JSON.parse(localStorage.getItem('bsw_memory') || '{}');
        if (state[vsMemRef]) {
          delete state[vsMemRef];
        } else {
          var today = (function () {
            var d = new Date();
            return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2);
          }());
          state[vsMemRef] = { addedDate: today, interval: 1, nextReview: today, score: 0, reps: 0 };
        }
        localStorage.setItem('bsw_memory', JSON.stringify(state));
      } catch (e) {}
      _vsUpdateMemBtn();
    });
  } else if (vsMemBtn) {
    vsMemBtn.setAttribute('hidden', '');
  }

  var vsShareBtn = document.getElementById('vs-share-btn');
  if (vsShareBtn && parsed.v) {
    vsShareBtn.removeAttribute('hidden');
    vsShareBtn.addEventListener('click', function () {
      var fEl  = document.getElementById('vs-focal-text');
      var text = fEl ? fEl.textContent.trim() : '';
      var ref  = (document.getElementById('vs-header-ref') || {}).textContent || '';
      if (text && ref) _shareVerseAsImage(text, ref, getVersion());
    });
  }

  // Register version-change callback
  onVersionChange(function (versionId) {
    loadVerseStudyVerse(parsed, versionId);
  });

  // Mobile section nav
  var mobileSelect = document.getElementById('vs-section-select');
  if (mobileSelect) {
    mobileSelect.addEventListener('change', function () {
      if (!this.value) return;
      var target = document.getElementById(this.value);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      this.value = '';
    });
  }

  // VS-H: measure header before verse fetch so scroll-margin-top is correct immediately
  requestAnimationFrame(function () {
    var header = document.getElementById('vs-sticky-header');
    if (header) {
      document.documentElement.style.setProperty('--vs-header-h', header.offsetHeight + 'px');
    }
  });

  loadVerseStudyVerse(parsed, getVersion()).then(function () { applyCtx(ctxOn); });
  loadVerseSections(parsed);
}

// ── loadVerseStudyVerse ───────────────────────────────────────────────────────
// INTENT: Primary verse-load pipeline — fetches the book JSON, sets focal verse text,
//   renders prev/next context verses with chapter-crossing logic (ch-1 last verse /
//   ch+1 first verse when at boundaries), and renders the morphological token row.
//   Called by initVerseStudyPage and by app.js after a version change in the modal.
// CHANGE? If vsRenderTokenRow signature changes (verse-study.js line ~290), update
//   the call at the end of this function. If loadBook cache strategy changes (core.js),
//   verify chapter-crossing prev/next still works across cold/warm cache loads.
// VERIFY: Load John 1:1 — prev context is absent (start of book). Load John 1:51 →
//   next shows John 2:1 (chapter crossing). Token row shows morphological tiles.
export function loadVerseStudyVerse(parsed, versionId) {
  var focalTextEl = document.getElementById('vs-focal-text');
  var focalNumEl  = document.getElementById('vs-focal-num');
  var prevEl      = document.getElementById('vs-context-prev');
  var nextEl      = document.getElementById('vs-context-next');
  var tokenRow    = document.getElementById('vs-token-row');

  if (focalTextEl) focalTextEl.textContent = 'Loading…';

  return loadBook(versionId, parsed.bookId).then(function (chapters) {
    if (!chapters) {
      if (focalTextEl) focalTextEl.textContent = 'Not available in ' + versionId + '.';
      return;
    }
    var chData = chapters[String(parsed.ch)];
    if (!chData) {
      if (focalTextEl) focalTextEl.textContent = 'Chapter not found.';
      return;
    }
    var text = chData[String(parsed.v)];
    if (!text) {
      if (focalTextEl) focalTextEl.textContent = 'Verse not found.';
      return;
    }

    if (focalNumEl) focalNumEl.textContent = parsed.v;
    if (focalTextEl) {
      focalTextEl.textContent = text;
      if (typeof autoTagTerms === 'function') {
        focalTextEl._termsTagged = false;
        autoTagTerms(focalTextEl);
      }
    }

    // VS-A / NAV-4: prev/next verse nav with cross-chapter fallback
    // INTENT: At verse 1 or last verse, show a chapter-jump link (Ch N-1 or Ch N+1:1)
    //   instead of hiding the arrow; prevents study dead-ends at chapter boundaries.
    // CHANGE? bk.chapters (from metaBooks) guards against linking past the book end.
    //   If VERSE_STUDY_URL changes in core.js, hrefs here update automatically.
    // VERIFY: Navigate to last verse of John 3 → next arrow shows 'Ch 4 ›' linking
    //   to John 4:1. Navigate to John 1:1 → prev arrow is hidden (book start).
    var prevNavLink = document.getElementById('vs-prev-link');
    var nextNavLink = document.getElementById('vs-next-link');
    var bk = metaBooks && metaBooks.find(function (b) { return b.id === parsed.bookId; });
    if (prevNavLink) {
      var pv = parsed.v - 1;
      if (pv >= 1 && chData[String(pv)]) {
        prevNavLink.href = VERSE_STUDY_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch + ':' + pv);
        prevNavLink.title = parsed.bookName + ' ' + parsed.ch + ':' + pv;
        prevNavLink.textContent = '‹';
        prevNavLink.setAttribute('aria-label', 'Previous verse');
        prevNavLink.removeAttribute('hidden');
      } else if (parsed.ch > 1) {
        var prevCh = parsed.ch - 1;
        prevNavLink.href = VERSE_STUDY_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + prevCh + ':1');
        prevNavLink.title = parsed.bookName + ' ' + prevCh + ':1';
        prevNavLink.textContent = '← Ch ' + prevCh;
        prevNavLink.setAttribute('aria-label', 'Go to chapter ' + prevCh);
        prevNavLink.removeAttribute('hidden');
      } else {
        prevNavLink.setAttribute('hidden', '');
      }
    }
    if (nextNavLink) {
      var nv = parsed.v + 1;
      if (chData[String(nv)]) {
        nextNavLink.href = VERSE_STUDY_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch + ':' + nv);
        nextNavLink.title = parsed.bookName + ' ' + parsed.ch + ':' + nv;
        nextNavLink.textContent = '›';
        nextNavLink.setAttribute('aria-label', 'Next verse');
        nextNavLink.removeAttribute('hidden');
      } else if (bk && parsed.ch < bk.chapters) {
        var nextCh = parsed.ch + 1;
        nextNavLink.href = VERSE_STUDY_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + nextCh + ':1');
        nextNavLink.title = parsed.bookName + ' ' + nextCh + ':1';
        nextNavLink.textContent = 'Ch ' + nextCh + ' »';
        nextNavLink.setAttribute('aria-label', 'Go to chapter ' + nextCh);
        nextNavLink.removeAttribute('hidden');
      } else {
        nextNavLink.setAttribute('hidden', '');
      }
    }

    // VS-E: copy verse button
    var copyBtn = document.getElementById('vs-copy-btn');
    if (copyBtn && text) {
      copyBtn.removeAttribute('hidden');
      copyBtn.onclick = function () {
        var ref = (document.getElementById('vs-header-ref') || {}).textContent || '';
        navigator.clipboard.writeText(text + (ref ? ' — ' + ref : '')).then(function () {
          copyBtn.textContent = 'Copied ✓';
          setTimeout(function () { copyBtn.textContent = 'Copy'; }, 1800);
        });
      };
    }

    if (prevEl) {
      var pv = parsed.v - 1;
      var pvText = pv >= 1 ? chData[String(pv)] : null;
      if (pvText) {
        prevEl.innerHTML = '<sup class="vs-ctx-num">' + pv + '</sup>' +
          '<span class="vs-ctx-text">' + escHtml(pvText) + '</span>';
      } else {
        prevEl.innerHTML = '';
      }
    }

    if (nextEl) {
      var nv = parsed.v + 1;
      var nvText = chData[String(nv)];
      if (nvText) {
        nextEl.innerHTML = '<sup class="vs-ctx-num">' + nv + '</sup>' +
          '<span class="vs-ctx-text">' + escHtml(nvText) + '</span>';
      } else {
        nextEl.innerHTML = '';
      }
    }

    _vsCurrentRef = parsed;
    if (tokenRow) vsRenderTokenRow(text, tokenRow);

    var header = document.getElementById('vs-sticky-header');
    if (header) {
      var hlRef2 = parsed.bookName + ' ' + parsed.ch + ':' + parsed.v;
      var notes  = getNotes();
      var hlNote = notes[hlRef2];
      var hlCol  = hlNote && hlNote.highlight;
      if (hlCol === true) hlCol = 'yellow';
      _HL_COLORS.forEach(function (c) { header.classList.remove('vs-header--hl-' + c); });
      if (hlCol) header.classList.add('vs-header--hl-' + hlCol);
      document.documentElement.style.setProperty('--vs-header-h', header.offsetHeight + 'px');
    }
  }).catch(function () {
    if (focalTextEl) focalTextEl.textContent = 'Could not load verse.';
  });
}

// ── Word token row ────────────────────────────────────────────────────────────
function vsTokenizeVerse(text) {
  var tokens = [];
  var parts = text.split(/(\s+)/);
  parts.forEach(function (part) {
    if (!part) return;
    if (/^\s+$/.test(part)) {
      tokens.push({ type: 'space', text: ' ' });
      return;
    }
    var m = part.match(/^([^A-Za-z0-9]*)([A-Za-z0-9''''-]+)([^A-Za-z0-9]*)$/);
    if (m) {
      if (m[1]) tokens.push({ type: 'punct', text: m[1] });
      tokens.push({ type: 'word', text: m[2] });
      if (m[3]) tokens.push({ type: 'punct', text: m[3] });
    } else {
      tokens.push({ type: 'punct', text: part });
    }
  });
  return tokens.filter(function (t) { return t.text; });
}

function vsRenderTokenRow(text, container) {
  container.innerHTML = '';
  var tokens = vsTokenizeVerse(text);
  tokens.forEach(function (tok) {
    if (tok.type === 'word') {
      var btn = document.createElement('button');
      btn.className = 'vs-token';
      btn.textContent = tok.text;
      btn.setAttribute('aria-label', tok.text);
      (function (wordText) {
        btn.addEventListener('click', function () { vsOpenWordStudy(btn, wordText); });
      }(tok.text));
      container.appendChild(btn);
    } else if (tok.type === 'space') {
      container.appendChild(document.createTextNode(' '));
    } else {
      var span = document.createElement('span');
      span.className = 'vs-token-punct';
      span.textContent = tok.text;
      container.appendChild(span);
    }
  });
}

// ── Word study flyout ─────────────────────────────────────────────────────────
function _vsTestament(parsed) {
  var bk = metaBooks && metaBooks.find(function (b) { return b.id === parsed.bookId; });
  return (bk && bk.testament === 'NT') ? 'greek' : 'hebrew';
}

function _vsMatchToken(verseTokens, wordText) {
  if (!verseTokens || !verseTokens.length) return null;
  var norm = wordText.toLowerCase().replace(/[^a-z]/g, '');

  for (var i = 0; i < verseTokens.length; i++) {
    var t   = verseTokens[i];
    var tkn = (t.text || '').toLowerCase().replace(/[^a-z]/g, '');
    if (tkn === norm) return t;
  }
  for (var j = 0; j < verseTokens.length; j++) {
    var t2   = verseTokens[j];
    var tkn2 = (t2.text || '').toLowerCase().replace(/[^a-z]/g, '');
    if (tkn2 && tkn2.indexOf(norm) !== -1) return t2;
  }
  for (var k = 0; k < verseTokens.length; k++) {
    var t3   = verseTokens[k];
    var tkn3 = (t3.text || '').toLowerCase().replace(/[^a-z]/g, '');
    if (tkn3 && tkn3.indexOf(' ') === -1 && norm.indexOf(tkn3) === 0 && tkn3.length > 2) return t3;
  }
  return null;
}

function vsOpenWordStudy(tokenEl, wordText) {
  if (_vsActiveToken === tokenEl) {
    tokenEl.classList.remove('vs-token--active');
    _vsActiveToken = null;
    if (_vsWordPanelEl) _vsWordPanelEl.setAttribute('hidden', '');
    return;
  }
  if (_vsActiveToken) _vsActiveToken.classList.remove('vs-token--active');
  _vsActiveToken = tokenEl;
  tokenEl.classList.add('vs-token--active');

  var tokenRow = document.getElementById('vs-token-row');
  if (!tokenRow) return;

  if (!_vsWordPanelEl) {
    _vsWordPanelEl = document.createElement('div');
    _vsWordPanelEl.id = 'vs-word-panel';
    _vsWordPanelEl.className = 'vs-word-panel';
  }
  if (_vsWordPanelEl.parentNode !== tokenRow.parentNode) {
    tokenRow.parentNode.insertBefore(_vsWordPanelEl, tokenRow.nextSibling);
  }
  _vsWordPanelEl.innerHTML = '<div class="vs-word-panel__loading">Loading…</div>';
  _vsWordPanelEl.removeAttribute('hidden');

  var parsed = _vsCurrentRef;
  if (!parsed) return;

  var testament = _vsTestament(parsed);

  Promise.all([
    loadInterlinear(parsed.bookId),
    loadStrongs(testament),
    loadLexicon(testament),
    _hitchLoad()
  ]).then(function (results) {
    var interlinear  = results[0];
    var strongsDict  = results[1];
    var lexDict      = results[2];

    var chData    = interlinear && interlinear[String(parsed.ch)];
    var vTokens   = chData && chData[String(parsed.v)];
    var match     = _vsMatchToken(vTokens, wordText);
    var strongsId = match ? match.s : null;
    var entry     = strongsId ? (strongsDict && strongsDict[strongsId]) : null;
    var lexEntry  = strongsId ? (lexDict    && lexDict[strongsId])    : null;

    _vsRenderWordPanel(wordText, strongsId, entry, lexEntry, tokenEl, match && match.m);
  }).catch(function () {
    if (_vsWordPanelEl) {
      _vsWordPanelEl.innerHTML = '<div class="vs-word-panel__no-data">Could not load word data.</div>';
    }
  });
}

function _vsRenderWordPanel(wordText, strongsId, entry, lexEntry, tokenEl, morphCode) {
  if (!_vsWordPanelEl) return;

  var html = '<div class="vs-word-panel__inner">';
  html += '<button class="vs-word-panel__close" aria-label="Close word study" id="vs-word-panel-close">✕</button>';

  html += '<div class="vs-word-panel__header">';
  html += '<span class="vs-word-panel__eng">' + escHtml(wordText) + '</span>';
  if (strongsId) {
    html += '<span class="vs-word-panel__strongs">' + escHtml(strongsId) + '</span>';
  }
  html += '</div>';

  if (entry) {
    if (entry.lemma) {
      html += '<div class="vs-word-panel__orig">';
      html += '<span class="vs-word-panel__lemma">' + escHtml(entry.lemma) + '</span>';
      if (entry.translit) {
        html += '<span class="vs-word-panel__translit">' + escHtml(entry.translit) + '</span>';
      }
      if (entry.pronounce) {
        html += '<span class="vs-word-panel__pronounce">(' + escHtml(entry.pronounce) + ')</span>';
      }
      html += '</div>';
    }
    if (entry.gloss) {
      html += '<div class="vs-word-panel__gloss">' + escHtml(entry.gloss) + '</div>';
    }
    if (entry.def && entry.def !== entry.gloss) {
      var isLong = entry.def.length > 300;
      html += '<div class="vs-word-panel__def">';
      html += '<span class="vs-wp-def-text">' + escHtml(isLong ? entry.def.slice(0, 300) : entry.def) + '</span>';
      if (isLong) {
        html += '<span class="vs-wp-def-rest" hidden>' + escHtml(entry.def.slice(300)) + '</span>';
        html += ' <button class="vs-wp-def-more" type="button">more…</button>';
      }
      html += '</div>';
    }
    if (entry.deriv) {
      html += '<div class="vs-word-panel__deriv">' + escHtml(entry.deriv) + '</div>';
    }
  } else if (strongsId) {
    html += '<div class="vs-word-panel__no-entry">Strong\'s entry not found for ' + escHtml(strongsId) + '.</div>';
  } else {
    html += '<div class="vs-word-panel__no-data">No Strong\'s data found for "' + escHtml(wordText) + '".' +
      '<br><small>Interlinear data may not be available for this verse.</small></div>';
  }

  if (morphCode) {
    var morphExpanded = expandMorphCode(morphCode);
    if (morphExpanded) {
      html += '<div class="vs-word-panel__morph">' + escHtml(morphExpanded) + '</div>';
    }
  }

  if (lexEntry && (lexEntry.short_def || lexEntry.long_def)) {
    var _isGreek = strongsId && strongsId.charAt(0) === 'G';
    html += '<div class="vs-word-panel__lexicon">' +
      '<span class="vs-word-panel__lex-label">' + (_isGreek ? 'Thayer' : 'BDB') + '</span> ' +
      escHtml(lexEntry.short_def || lexEntry.long_def) +
      '</div>';
  }

  if (entry && entry.gloss && _hitchMap) {
    var _hitchSlug = entry.gloss.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    var _hitchEntry = _hitchMap[_hitchSlug];
    if (_hitchEntry) {
      html += '<div class="vs-word-panel__lexicon vs-word-panel__hitch">' +
        '<span class="vs-word-panel__lex-label">Name</span> ' +
        escHtml(_hitchEntry.meaning) +
        '</div>';
    }
  }

  if (strongsId) {
    html += '<div class="vs-word-panel__actions">' +
      '<a class="vs-context-btn" href="' +
      escHtml(SEARCH_URL + '?s=' + encodeURIComponent(strongsId)) +
      '">All verses with ' + escHtml(strongsId) + '</a>' +
      '<a class="vs-context-btn" href="' +
      escHtml(WORD_URL + '?s=' + encodeURIComponent(strongsId)) +
      '">Word Deep Dive</a>' +
      '</div>';
  }

  html += '</div>';
  _vsWordPanelEl.innerHTML = html;

  var closeBtn = document.getElementById('vs-word-panel-close');
  if (closeBtn) {
    closeBtn.addEventListener('click', function () {
      if (_vsActiveToken) {
        _vsActiveToken.classList.remove('vs-token--active');
        _vsActiveToken = null;
      }
      _vsWordPanelEl.setAttribute('hidden', '');
    });
  }

  // VS-F: wire the "more…" expand button
  var moreBtn = _vsWordPanelEl.querySelector('.vs-wp-def-more');
  if (moreBtn) {
    moreBtn.addEventListener('click', function () {
      var rest = _vsWordPanelEl.querySelector('.vs-wp-def-rest');
      if (rest) rest.removeAttribute('hidden');
      moreBtn.remove();
    });
  }
}

// ── Modal Word Study tab ──────────────────────────────────────────────────────
export function renderModalWordStudy(parsed, container) {
  container._wsLoaded = true;
  container.innerHTML = '<div class="bsw-ws-loading">Loading word data…</div>';

  if (!parsed || (!parsed.v && parsed.v !== 0)) {
    container.innerHTML = '<p class="bsw-ws-note">Word study is available for single-verse references.</p>';
    return;
  }

  var testament = _vsTestament(parsed);

  Promise.all([
    loadInterlinear(parsed.bookId),
    loadStrongs(testament)
  ]).then(function (results) {
    var interlinear = results[0];
    var strongsDict = results[1];

    var chData  = interlinear && interlinear[String(parsed.ch)];
    var vTokens = chData && chData[String(parsed.v)];

    if (!vTokens || !vTokens.length) {
      container.innerHTML = '<p class="bsw-ws-note">No interlinear data available for ' +
        escHtml(parsed.display) + '.</p>';
      return;
    }

    var html = '<div class="bsw-ws-table">';
    vTokens.forEach(function (tok) {
      if (!tok.s) return;
      var entry = strongsDict && strongsDict[tok.s];
      html += '<div class="bsw-ws-row">';
      html += '<div class="bsw-ws-eng">' + escHtml(tok.text || '–') + '</div>';
      html += '<div class="bsw-ws-strongs"><a class="bsw-ws-strongs-link" href="' +
        escHtml(WORD_URL + '?s=' + encodeURIComponent(tok.s)) + '" target="_blank">' +
        escHtml(tok.s) + ' ↗</a></div>';
      if (entry) {
        html += '<div class="bsw-ws-lemma">' + escHtml(entry.lemma || '') + '</div>';
        html += '<div class="bsw-ws-translit">' + escHtml(entry.translit || '') + '</div>';
        html += '<div class="bsw-ws-gloss">' + escHtml(entry.gloss || '') + '</div>';
      } else {
        html += '<div class="bsw-ws-lemma"></div><div class="bsw-ws-translit"></div><div class="bsw-ws-gloss"></div>';
      }
      html += '</div>';
    });
    html += '</div>';
    html += '<p class="bsw-ws-attr">Interlinear data: public domain (tahmmee/interlinear_bibledata). ' +
      'Strong\'s dictionary: openscriptures/strongs (public domain).</p>';
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML = '<p class="bsw-ws-note">Could not load word study data.</p>';
  });
}

// ── Interlinear sentence diagram ──────────────────────────────────────────────
function vsOrderByVerseText(tokens, verseText) {
  if (!tokens || !tokens.length) return tokens || [];
  var clean = verseText.toLowerCase().replace(/['''"",.:;!?()\[\]\-]/g, ' ');
  var positioned = tokens.map(function (tok, i) {
    var phrase = (tok.text || '').toLowerCase().replace(/['''"",.:;!?()\[\]\-]/g, ' ').trim();
    var pos = phrase ? clean.indexOf(phrase) : -1;
    return { tok: tok, pos: pos < 0 ? 1e6 + i : pos, orig: i };
  });
  positioned.sort(function (a, b) {
    return a.pos !== b.pos ? a.pos - b.pos : a.orig - b.orig;
  });
  return positioned.map(function (p) { return p.tok; });
}

function vsRenderInterlinear(vTokens, strongsDict, container, isHebrew) {
  if (!vTokens || !vTokens.length) {
    container.innerHTML = '<p class="vs-interlinear-note">No interlinear data available.</p>';
    return;
  }

  var verseText = (document.getElementById('vs-focal-text') || {}).textContent || '';
  var tokens = vsOrderByVerseText(
    vTokens.filter(function (t) { return t.s; }),
    verseText
  );

  var grid = document.createElement('div');
  grid.className = isHebrew ? 'vs-interlinear-grid vs-interlinear-grid--rtl' : 'vs-interlinear-grid';

  var detail = document.createElement('div');
  detail.className = 'vs-interlinear-detail';
  detail.setAttribute('hidden', '');

  var activeTile = null;

  tokens.forEach(function (tok) {
    var entry = strongsDict && strongsDict[tok.s];

    var tile = document.createElement('button');
    tile.className = 'vs-tile';
    tile.type = 'button';

    var orig = (entry && entry.lemma)
      ? '<div class="vs-tile__lemma"' + (isHebrew ? ' dir="rtl"' : '') + '>' + escHtml(entry.lemma) + '</div>' +
        (entry.translit ? '<div class="vs-tile__translit">' + escHtml(entry.translit) + '</div>' : '')
      : '<div class="vs-tile__lemma vs-tile__lemma--missing">—</div>';

    tile.innerHTML =
      orig +
      '<div class="vs-tile__divider"></div>' +
      '<div class="vs-tile__eng">' + escHtml(tok.text || '') + '</div>' +
      '<div class="vs-tile__strongs">' + escHtml(tok.s) + '</div>';

    tile.addEventListener('click', function () {
      if (activeTile === tile) {
        tile.classList.remove('vs-tile--active');
        activeTile = null;
        detail.setAttribute('hidden', '');
        return;
      }
      if (activeTile) activeTile.classList.remove('vs-tile--active');
      activeTile = tile;
      tile.classList.add('vs-tile--active');
      vsRenderTileDetail(tok, entry, detail);
      detail.removeAttribute('hidden');
    });

    grid.appendChild(tile);
  });

  container.appendChild(grid);
  container.appendChild(detail);

  var attr = document.createElement('p');
  attr.className = 'vs-interlinear-attr';
  attr.innerHTML = 'Interlinear: public domain (tahmmee/interlinear_bibledata). ' +
    'Strong&#x2019;s: openscriptures/strongs (public domain).';
  container.appendChild(attr);
}

function vsRenderTileDetail(tok, entry, detailEl) {
  var html = '<div class="vs-id-header">' +
    '<span class="vs-id-eng">' + escHtml(tok.text || '') + '</span>' +
    '<span class="vs-id-strongs">' + escHtml(tok.s || '') + '</span>';
  if (entry && entry.lemma) {
    html += '<span class="vs-id-lemma">' + escHtml(entry.lemma) + '</span>';
    if (entry.translit) html += '<span class="vs-id-translit">' + escHtml(entry.translit) + '</span>';
    if (entry.pronounce) html += '<span class="vs-id-pronounce">(' + escHtml(entry.pronounce) + ')</span>';
  }
  html += '</div>';
  if (entry) {
    if (entry.gloss) {
      html += '<div class="vs-id-gloss">' + escHtml(entry.gloss) + '</div>';
    }
    if (entry.def && entry.def !== entry.gloss) {
      html += '<div class="vs-id-def">' + escHtml(entry.def) + '</div>';
    }
    if (entry.deriv) {
      html += '<div class="vs-id-deriv">' + escHtml(entry.deriv) + '</div>';
    }
  } else {
    html += '<p class="vs-id-note">No Strong\'s entry for ' + escHtml(tok.s || '') + '.</p>';
  }
  if (tok.m) {
    var morphLbl = expandMorphCode(tok.m);
    if (morphLbl) html += '<div class="vs-id-morph">' + escHtml(morphLbl) + '</div>';
  }
  if (tok.s) {
    html += '<div class="vs-id-actions">' +
      '<a class="vs-context-btn" href="' +
      escHtml(SEARCH_URL + '?s=' + encodeURIComponent(tok.s)) +
      '">All verses with ' + escHtml(tok.s) + '</a>' +
      '<a class="vs-context-btn" href="' +
      escHtml(WORD_URL + '?s=' + encodeURIComponent(tok.s)) +
      '">Word Deep Dive</a>' +
      '</div>';
  }
  detailEl.innerHTML = html;
}

// ── Verse Study sections ──────────────────────────────────────────────────────
function loadVerseSections(parsed) {
  var container = document.getElementById('vs-sections-container');
  if (!container) return;

  // Interlinear
  var interlinearSec = vsCreateSection(container, 'vs-interlinear', 'Interlinear');
  var testament = _vsTestament(parsed);
  Promise.all([loadInterlinear(parsed.bookId), loadStrongs(testament)])
    .then(function (results) {
      var chData  = results[0] && results[0][String(parsed.ch)];
      var vTokens = chData && chData[String(parsed.v)];
      if (!vTokens || !vTokens.length) { interlinearSec.el.remove(); vsRebuildNav(); return; }
      vsRenderInterlinear(vTokens, results[1], interlinearSec.bodyEl, testament === 'hebrew');
      interlinearSec.el.removeAttribute('hidden');
      vsRebuildNav();
    })
    .catch(function () {
      // INTENT: Remove the hidden section so a fetch failure doesn't leave a ghost nav entry.
      // CHANGE? If loadStrongs gains its own internal catch, this may fire less often — verify
      //   the section is still removed by blocking data/strongs/*.json in DevTools Network.
      interlinearSec.el.remove();
      vsRebuildNav();
    });

  // Notes
  var notesSec = vsCreateSection(container, 'vs-notes', 'Notes');
  _renderNotesPanel(parsed, notesSec.bodyEl);
  notesSec.el.removeAttribute('hidden');
  vsRebuildNav();

  var xrefSec  = vsCreateSection(container, 'vs-xrefs',      'Cross-References');
  var commSec  = vsCreateSection(container, 'vs-commentary', 'Commentary');
  var parSec   = vsCreateSection(container, 'vs-echoes', 'Echoes &amp; Fulfillments');
  var cmpSec   = vsCreateSection(container, 'vs-compare',    'All Translations');

  // Cross-references
  loadCrossRefs(parsed.bookId).then(function (data) {
    var entries = vsExtractXrefs(data, parsed);
    if (!entries || !entries.length) { xrefSec.el.remove(); vsRebuildNav(); return; }
    vsRenderXrefList(entries, xrefSec.bodyEl);
    xrefSec.el.removeAttribute('hidden');
    vsRebuildNav();
  }).catch(function () { xrefSec.el.remove(); vsRebuildNav(); });

  // Commentary with source picker
  (function () {
    function vsLoadComm(src) {
      commSec.bodyEl.innerHTML = '<p class="bsw-modal__loading">Loading commentary…</p>';
      loadCommentary(parsed.bookId, src).then(function (data) {
        // _extractCommHtml returns {html, foundV} — destructure before use
        var commResult = _extractCommHtml(data, parsed, src);
        var html = commResult ? commResult.html : null;
        var attrHtml = html ? '<p class="vs-commentary-attr">' + _commAttr(src) + '</p>' : '';
        if (!html && commSec.el.hasAttribute('hidden')) {
          commSec.el.remove(); vsRebuildNav(); return;
        }
        commSec.bodyEl.innerHTML = (html || '<p class="bsw-modal__commentary-empty">No commentary found for this verse.</p>') + attrHtml;
        wireRefLinks(commSec.bodyEl);
        // VS-G: collapse long commentary entries with a "Read more" expand
        var COMM_THRESHOLD = 800;
        if (commSec.bodyEl.textContent.length > COMM_THRESHOLD) {
          var wrapper = document.createElement('div');
          wrapper.className = 'vs-comm-truncated';
          while (commSec.bodyEl.firstChild) wrapper.appendChild(commSec.bodyEl.firstChild);
          commSec.bodyEl.appendChild(wrapper);
          var expandBtn = document.createElement('button');
          expandBtn.className = 'vs-comm-expand-btn';
          expandBtn.type = 'button';
          expandBtn.textContent = 'Read more ▾';
          commSec.bodyEl.appendChild(expandBtn);
          expandBtn.addEventListener('click', function () {
            wrapper.classList.remove('vs-comm-truncated--clamped');
            expandBtn.remove();
          });
          wrapper.classList.add('vs-comm-truncated--clamped');
        }
        if (commSec.el.hasAttribute('hidden')) {
          commSec.el.removeAttribute('hidden');
          vsRebuildNav();
        }
      }).catch(function () {
        commSec.bodyEl.innerHTML = '<p class="bsw-modal__commentary-empty">Could not load commentary. Check your connection.</p>';
      });
    }

    var commSrc = getCommentarySource();
    var opts = COMMENTARY_SOURCES.map(function (s) {
      return '<option value="' + s.id + '"' + (s.id === commSrc ? ' selected' : '') + '>' + s.label + '</option>';
    }).join('');
    var pickerEl = document.createElement('div');
    pickerEl.className = 'vs-comm-picker';
    pickerEl.innerHTML = '<label class="vs-comm-label">Source:</label>' +
      '<select class="vs-comm-select">' + opts + '</select>';
    commSec.bodyEl.parentNode.insertBefore(pickerEl, commSec.bodyEl);

    pickerEl.querySelector('.vs-comm-select').addEventListener('change', function () {
      setCommentarySource(this.value);
      vsLoadComm(this.value);
    });

    vsLoadComm(getCommentarySource());
  }());

  // Echoes & Fulfillments — OT→NT typological connections for this verse
  loadEchoes(parsed.bookId).then(function (data) {
    var echoes = vsExtractEchoes(data, parsed);
    if (!echoes || !echoes.length) { parSec.el.remove(); vsRebuildNav(); return; }
    vsRenderEchoList(echoes, parSec.bodyEl);
    wireRefLinks(parSec.bodyEl);
    parSec.el.removeAttribute('hidden');
    vsRebuildNav();
  }).catch(function () { parSec.el.remove(); vsRebuildNav(); });

  // All Translations — lazy-load on scroll into view (VS-D)
  if (metaVersions && metaVersions.length) {
    cmpSec.el.removeAttribute('hidden');
    vsRebuildNav();
    var cmpObserver = new IntersectionObserver(function (entries) {
      if (!entries[0].isIntersecting) return;
      cmpObserver.disconnect();
      vsRenderVersionCompare(parsed, cmpSec.bodyEl);
    }, { threshold: 0.05 });
    cmpObserver.observe(cmpSec.el);
  } else {
    cmpSec.el.remove();
    vsRebuildNav();
  }

  // Nave's Topics
  if (parsed.v) {
    var topicSec = vsCreateSection(container, 'vs-topics', 'Nave\'s Topics');
    renderVSTopics(parsed, topicSec.bodyEl);
    topicSec.el.removeAttribute('hidden');
    vsRebuildNav();
  }

  // Confessions
  if (parsed.v) {
    var confSec = vsCreateSection(container, 'vs-confessions', 'Confessional Citations');
    loadLibVerseIndex(parsed.bookId).then(function (data) {
      var all  = (data[String(parsed.ch)] && data[String(parsed.ch)][String(parsed.v)]) || [];
      var cits = all.filter(function (c) { return !FATHER_SLUGS[c.slug]; });
      if (!cits.length) { confSec.el.remove(); vsRebuildNav(); return; }
      renderModalConfessions(parsed, confSec.bodyEl);
      confSec.el.removeAttribute('hidden');
      vsRebuildNav();
    }).catch(function () { confSec.el.remove(); vsRebuildNav(); });
  }

  // Church Fathers
  if (parsed.v) {
    var fathersSec = vsCreateSection(container, 'vs-fathers', 'Church Fathers');
    loadLibVerseIndex(parsed.bookId).then(function (data) {
      var all  = (data[String(parsed.ch)] && data[String(parsed.ch)][String(parsed.v)]) || [];
      var cits = all.filter(function (c) { return !!FATHER_SLUGS[c.slug]; });
      if (!cits.length) { fathersSec.el.remove(); vsRebuildNav(); return; }
      renderModalFathers(parsed, fathersSec.bodyEl);
      fathersSec.el.removeAttribute('hidden');
      vsRebuildNav();
    }).catch(function () { fathersSec.el.remove(); vsRebuildNav(); });
  }

  // Dictionary
  if (parsed.v) {
    var dictSec = vsCreateSection(container, 'vs-dictionary', 'Dictionary');
    _dictEntriesForVerse(parsed).then(function (entries) {
      if (!entries.length) { dictSec.el.remove(); vsRebuildNav(); return; }
      renderVSDictionary(parsed, dictSec.bodyEl);
      dictSec.el.removeAttribute('hidden');
      vsRebuildNav();
    }).catch(function () { dictSec.el.remove(); vsRebuildNav(); });
  }

  // INTENT: window.BibleUI indirection — ol-companion.js registers initOLSection on
  //   window.BibleUI in app.js rather than being imported directly here. This avoids a
  //   circular import: ol-companion.js imports from core.js, and verse-study.js also
  //   imports from core.js; a direct import of ol-companion.js here would create an
  //   import cycle. The window.BibleUI global is the deliberate decoupling point.
  // CHANGE? If the coupling strategy changes (e.g., to a shared event bus), update
  //   app.js (registration of window.BibleUI.initOLSection) and ol-companion.js export.
  // VERIFY: Load verse-study/?ref=Romans+8:1 — OL Companion section renders below the
  //   other sections with tier comparison rows. No console errors about circular imports.
  // Original Language Companion — MKT token analysis, tier comparison, dispute flags
  if (parsed.v && window.BibleUI && typeof window.BibleUI.initOLSection === 'function') {
    window.BibleUI.initOLSection(parsed, vsCreateSection, vsRebuildNav)
      .catch(function(e) { console.warn('[OL Companion]', e); });
  }
}

function vsCreateSection(container, id, label) {
  var sec = document.createElement('section');
  sec.className = 'vs-section';
  sec.id = id;
  sec.setAttribute('hidden', '');

  var heading = document.createElement('h2');
  heading.className = 'vs-section-heading';
  heading.textContent = label;

  var body = document.createElement('div');
  body.className = 'vs-section-body';
  body.id = id + '-body';

  // VS-C: collapse toggle
  var toggleBtn = document.createElement('button');
  toggleBtn.className = 'vs-section-toggle';
  toggleBtn.setAttribute('aria-expanded', 'true');
  toggleBtn.setAttribute('aria-controls', id + '-body');
  toggleBtn.textContent = '▾';
  heading.appendChild(toggleBtn);

  toggleBtn.addEventListener('click', function () {
    var expanded = toggleBtn.getAttribute('aria-expanded') === 'true';
    toggleBtn.setAttribute('aria-expanded', String(!expanded));
    body.hidden = expanded;
    toggleBtn.textContent = expanded ? '▸' : '▾';
  });

  sec.appendChild(heading);
  sec.appendChild(body);
  container.appendChild(sec);
  return { el: sec, bodyEl: body, id: id, label: label };
}

function vsRebuildNav() {
  // VS-B: disconnect previous scroll-spy observer before rebuilding
  if (_vsNavObserver) { _vsNavObserver.disconnect(); _vsNavObserver = null; }

  var sidebar     = document.getElementById('vs-sidebar');
  var mobileNav   = document.getElementById('vs-mobile-nav');
  var mobileSelect= document.getElementById('vs-section-select');
  var visible     = Array.prototype.slice.call(
    document.querySelectorAll('#vs-sections-container .vs-section:not([hidden])')
  );

  if (sidebar) {
    sidebar.innerHTML = '';
    visible.forEach(function (sec) {
      var hd = sec.querySelector('.vs-section-heading');
      if (!hd) return;
      var btn = document.createElement('button');
      btn.className = 'vs-nav-btn';
      btn.dataset.sectionId = sec.id;
      btn.textContent = hd.textContent.replace('▾', '').replace('▸', '').trim();
      btn.addEventListener('click', function () {
        sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
      sidebar.appendChild(btn);
    });

    // VS-B: wire scroll-spy observer
    if (visible.length > 0) {
      _vsNavObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var id = entry.target.id;
          document.querySelectorAll('#vs-sidebar .vs-nav-btn').forEach(function (b) {
            b.classList.toggle('vs-nav-btn--active', b.dataset.sectionId === id);
          });
        });
      }, { rootMargin: '-8% 0px -75% 0px', threshold: 0 });
      visible.forEach(function (sec) { _vsNavObserver.observe(sec); });
    }
  }

  if (mobileSelect) {
    mobileSelect.innerHTML = '<option value="">Jump to section…</option>';
    visible.forEach(function (sec) {
      var hd = sec.querySelector('.vs-section-heading');
      if (!hd) return;
      var opt = document.createElement('option');
      opt.value = sec.id;
      opt.textContent = hd.textContent;
      mobileSelect.appendChild(opt);
    });
  }

  if (mobileNav) {
    if (visible.length > 0) mobileNav.removeAttribute('hidden');
    else mobileNav.setAttribute('hidden', '');
  }
}

// ── All-translations compare ──────────────────────────────────────────────────
// INTENT: Renders a verse row for every non-stub version. All "Loading…"
//   placeholders appear immediately (good for perceived performance), then fetches
//   are fired in sequential batches of BATCH_SIZE so we stay within the browser's
//   6-connection-per-host limit. Consistent with the batch pattern in word.js.
// CHANGE? BATCH_SIZE controls concurrency — 5 keeps us under the 6-connection cap
//   while allowing a second batch to start before the first is fully visible.
//   resolveVerses() is imported from core.js; if its signature changes, update
//   the call here. getVersion() supplies the "current" highlight class.
// VERIFY: DevTools → Network → filter by book id (e.g. "john"). Scroll to "All
//   Translations" on verse-study/?ref=John+3:16 — should see ≤5 simultaneous
//   requests, then a second wave, rather than 11 all at once.
function vsRenderVersionCompare(parsed, container) {
  if (!metaVersions || !metaVersions.length) return;
  var currentVer = getVersion();
  var BATCH_SIZE = 5;

  // Build DOM rows upfront so all "Loading…" placeholders appear immediately,
  // paired with each version so batched fetch closures can update them.
  var items = [];
  metaVersions.forEach(function (ver) {
    if (ver.stub) return;  // no data files — would 404 on every load
    var row = document.createElement('div');
    row.className = 'vs-cmp-row' + (ver.id === currentVer ? ' vs-cmp-row--current' : '');

    var hdr = document.createElement('div');
    hdr.className = 'vs-cmp-row__hdr';
    hdr.innerHTML =
      '<span class="vs-cmp-row__id">' + escHtml(ver.id) + '</span>' +
      '<span class="vs-cmp-row__name">' + escHtml(ver.fullname || ver.name || ver.id) + '</span>';
    row.appendChild(hdr);

    var textEl = document.createElement('p');
    textEl.className = 'vs-cmp-row__text vs-cmp-row__text--loading';
    textEl.textContent = 'Loading…';
    row.appendChild(textEl);

    container.appendChild(row);
    items.push({ ver: ver, textEl: textEl, row: row });
  });

  // Slice into chunks and process sequentially; within each chunk fetches run in parallel.
  var chunks = [];
  for (var i = 0; i < items.length; i += BATCH_SIZE) {
    chunks.push(items.slice(i, i + BATCH_SIZE));
  }

  function _processBatch(chunkIdx) {
    if (chunkIdx >= chunks.length) return;
    Promise.all(chunks[chunkIdx].map(function (item) {
      return resolveVerses(parsed, item.ver.id).then(function (rows) {
        var text = rows && rows[0] && rows[0].text;
        if (text) {
          item.textEl.className = 'vs-cmp-row__text';
          item.textEl.textContent = text;
          applyHighlights(item.row);
        } else {
          item.textEl.className = 'vs-cmp-row__text vs-cmp-row__text--na';
          item.textEl.textContent = 'Not available in this translation.';
        }
      }).catch(function () {
        item.textEl.className = 'vs-cmp-row__text vs-cmp-row__text--na';
        item.textEl.textContent = 'Could not load.';
      });
    })).then(function () { _processBatch(chunkIdx + 1); });
  }

  _processBatch(0);
}

// ── Cross-ref helpers ─────────────────────────────────────────────────────────
function vsExtractXrefs(data, parsed) {
  if (!data) return null;
  var chData = data[String(parsed.ch)];
  if (!chData) return null;
  var rawRefs = chData[String(parsed.v)];
  if (!rawRefs || !rawRefs.length) return null;
  var entries = rawRefs.map(parseCrossRefEntry);
  entries.sort(_compareCanonical);
  return entries;
}

function vsRenderXrefList(entries, container) {
  var div = document.createElement('div');
  div.className = 'vs-xref-list';
  entries.forEach(function (entry) {
    var tierClass = '';
    if (entry.votes > 1) {
      tierClass = entry.votes >= 15 ? ' bsw-xref--high' :
                  entry.votes >= 6  ? ' bsw-xref--med'  : ' bsw-xref--low';
    }
    var a = document.createElement('a');
    a.className = 'vs-xref-link' + tierClass;
    a.setAttribute('data-ref', entry.ref);
    a.setAttribute('role', 'button');
    a.setAttribute('tabindex', '0');
    a.textContent = entry.ref;
    var p = parseRef(entry.ref);
    if (p) wireRefEl(a, p);
    div.appendChild(a);
  });
  container.appendChild(div);
}

// ── Echoes & Fulfillments helpers ─────────────────────────────────────────────
// INTENT: Extract echo entries for the current verse from per-book echoes data.
//   Returns the array of {type, target, note} objects for data[ch][v], or null if absent.
// CHANGE? If the echoes data schema changes (e.g. nested under a "echoes" key), update the
//   accessor path here and in loadEchoes in core.js.
// VERIFY: Open verse-study for John 1:29 — the "Echoes & Fulfillments" section should appear
//   with entries for Exod 12 (type) and Isa 53:7 (allusion) and their notes.
function vsExtractEchoes(data, parsed) {
  if (!data) return null;
  var chData = data[String(parsed.ch)];
  if (!chData) return null;
  var entries = chData[String(parsed.v)];
  if (!entries || !entries.length) return null;
  return entries;
}

function vsRenderEchoList(echoes, container) {
  echoes.forEach(function (echo) {
    var meta = _ECHO_TYPE_META[echo.type] || { label: echo.type || 'Echo', cls: 'vs-echo-badge--allusion' };

    var entry = document.createElement('div');
    entry.className = 'vs-echo-entry';

    var header = document.createElement('div');
    header.className = 'vs-echo-header';

    var badge = document.createElement('span');
    badge.className = 'vs-echo-badge ' + meta.cls;
    badge.textContent = meta.label;

    var refLink = document.createElement('a');
    refLink.className = 'ref vs-echo-ref';
    refLink.dataset.ref = echo.target || '';
    refLink.textContent = echo.target || '';

    header.appendChild(badge);
    header.appendChild(refLink);
    entry.appendChild(header);

    if (echo.note) {
      var note = document.createElement('p');
      note.className = 'vs-echo-note';
      note.textContent = echo.note;
      entry.appendChild(note);
    }

    container.appendChild(entry);
  });
}

// ── Parallel passage helpers ──────────────────────────────────────────────────
function vsExtractParallels(data, parsed) {
  if (!data) return null;
  var chData = data[String(parsed.ch)];
  if (!chData) return null;
  var entries = chData[String(parsed.v)];
  if (!entries || !entries.length) return null;
  return entries;
}

function vsRenderParallelList(sections, container, parsed) {
  var version = getVersion();
  sections.forEach(function (entry) {
    (entry.refs || []).forEach(function (refObj) {
      var p = parseRef(refObj.passage);
      if (!p) return;

      var typeMeta = _PARALLEL_TYPE_META[entry.type] || _PARALLEL_TYPE_META['parallel'];

      var panel = document.createElement('div');
      panel.className = 'vs-parallel-panel';

      var header = document.createElement('div');
      header.className = 'vs-parallel-header';

      var badge = document.createElement('span');
      badge.className = 'reader-parallel-badge ' + typeMeta.cls;
      badge.textContent = typeMeta.icon + ' ' + typeMeta.label;

      var refSpan = document.createElement('span');
      refSpan.className = 'vs-parallel-ref';
      refSpan.textContent = refObj.passage;

      var readLink = document.createElement('a');
      readLink.className = 'vs-parallel-read-link';
      readLink.href = READER_URL + '?ref=' + encodeURIComponent(refObj.passage);
      readLink.textContent = '↗';
      readLink.title = 'Open in Reader';

      header.appendChild(badge);
      header.appendChild(refSpan);
      header.appendChild(readLink);

      var body = document.createElement('div');
      body.className = 'vs-parallel-body';
      body.innerHTML = '<span class="reader-parallel-loading">Loading…</span>';

      panel.appendChild(header);
      panel.appendChild(body);
      container.appendChild(panel);

      resolveVerses(p, version).then(function (verses) {
        if (!verses || !verses.length) {
          body.innerHTML = '<span class="reader-parallel-empty">Not available in ' +
            escHtml(version) + '.</span>';
          return;
        }
        var html = '<p class="vs-parallel-text">';
        verses.forEach(function (vr) {
          html += '<sup class="reader-verse__num" style="cursor:default">' +
            vr.verse + '</sup>' + escHtml(vr.text) + ' ';
        });
        html += '</p>';
        body.innerHTML = html;
      }).catch(function () {
        body.innerHTML = '<span class="reader-parallel-empty">Could not load passage.</span>';
      });
    });
  });
}
