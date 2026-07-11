/* word.js — Word Deep Dive page */
'use strict';

import {
  SEARCH_URL, WORD_URL, metaBooks,
  getVersion, escHtml, parseRef, resolveVerses,
  loadStrongs, loadLexicon, loadInterlinear, onVersionChange
} from './core.js';
import { wireRefLinks } from './wire.js';
import { expandMorphCode } from './interlinear.js';
import { autoTagTermsWhenReady } from './terms.js';

var _wdCurrentFilter = null;
var _wdCurrentBook   = null;
var _wdBookList      = null;
var _wdMorphCount    = null;
/* WD-L: shared across promise chain so _wdRenderRelatedWords can access them */
var _wdEntry         = null;
var _wdStrongsDict   = null;

/* ── URL hash helpers (WD-B) ─────────────────────────────────────────────── */

function _wdWriteHash() {
  var parts = [];
  if (_wdCurrentBook)   parts.push('book=' + encodeURIComponent(_wdCurrentBook));
  if (_wdCurrentFilter) parts.push('trans=' + encodeURIComponent(_wdCurrentFilter));
  var base = window.location.pathname + window.location.search;
  window.history.replaceState(null, '', base + (parts.length ? '#' + parts.join('&') : ''));
}

function _wdReadHash() {
  var hash = window.location.hash.replace(/^#/, '');
  var result = { book: null, trans: null };
  hash.split('&').forEach(function (part) {
    var kv = part.split('=');
    if (kv[0] === 'book' && kv[1])  result.book  = decodeURIComponent(kv[1]);
    if (kv[0] === 'trans' && kv[1]) result.trans = decodeURIComponent(kv[1]);
  });
  return result;
}

export function initWordPage() {
  var params   = new URLSearchParams(window.location.search);
  var rawId    = (params.get('s') || '').trim().toUpperCase();
  var headerEl = document.getElementById('wd-header');

  if (!rawId || !/^[GH]\d+$/.test(rawId)) {
    headerEl.innerHTML = '<p class="wd-error">No Strong\'s number provided. Use <code>?s=G3056</code> or <code>?s=H430</code>.</p>';
    return;
  }

  document.title = rawId + ' — Word Study — Kingdom Bible Study';

  var backLink = document.getElementById('wd-back-link');
  if (backLink) {
    if (params.get('from') === 'wordcloud') {
      backLink.href = '../wordcloud/';
      backLink.textContent = '← Word Cloud';
    } else {
      backLink.href = SEARCH_URL + '?s=' + encodeURIComponent(rawId);
    }
  }

  var testament = rawId[0] === 'G' ? 'greek' : 'hebrew';

  onVersionChange(function (ver) {
    var versesSection = document.getElementById('wd-verses');
    if (versesSection && versesSection._rerenderFn) versesSection._rerenderFn(ver);
  });

  /* WD-B: restore filters from Back/Forward navigation */
  window.addEventListener('hashchange', function () {
    var h = _wdReadHash();
    _wdCurrentBook   = h.book;
    _wdCurrentFilter = h.trans;
    _wdRenderBooks();
    _wdRenderTranslations();
    _wdRefreshVerses();
  });

  Promise.all([loadStrongs(testament), loadLexicon(testament)])
    .then(function (results) {
      var strongsDict = results[0];
      var lexDict     = results[1];
      var entry    = strongsDict && strongsDict[rawId];
      var lexEntry = lexDict    && lexDict[rawId];

      /* WD-L: store for use after interlinear fetches resolve */
      _wdEntry       = entry;
      _wdStrongsDict = strongsDict;

      _wdRenderHeader(rawId, entry, lexEntry, headerEl);

      var books = metaBooks.filter(function (b) {
        return b.testament === (testament === 'greek' ? 'NT' : 'OT');
      });

      var bookMatches      = {};
      var totalCount       = 0;
      var translationCount = {};
      var morphCount       = {};   /* WD-C */
      var completed        = 0;
      var total            = books.length;

      /* WD-A: insert progress element below the header */
      var progressEl = document.createElement('p');
      progressEl.id = 'wd-progress';
      progressEl.className = 'wd-progress';
      progressEl.textContent = 'Loading books… 0 / ' + total;
      var statsEl = document.getElementById('wd-stats');
      statsEl.parentNode.insertBefore(progressEl, statsEl);

      // INTENT: Batch interlinear fetches (5 books at a time) to stay within the browser's
      //   6-connection-per-host limit; firing 27–39 simultaneous fetches would queue all of them
      //   and offer no faster start than sequential batches of 5.
      // CHANGE? If BATCH_SIZE changes, also update core.js loadInterlinear comment. The
      //   accumulator vars (bookMatches, translationCount, morphCount) are captured by closure
      //   and mutated inside each batch — do not move this block out of its current scope.
      // VERIFY: DevTools → Network → filter 'interlinear'; first word lookup should show ≤5
      //   requests in-flight at once. Total request count equals the testament's book count.
      var BATCH_SIZE = 5;
      var bookChunks = [];
      for (var ci = 0; ci < books.length; ci += BATCH_SIZE) {
        bookChunks.push(books.slice(ci, ci + BATCH_SIZE));
      }

      function _processBatch(chunkIdx) {
        if (chunkIdx >= bookChunks.length) return Promise.resolve();
        return Promise.all(bookChunks[chunkIdx].map(function (bk) {
          return loadInterlinear(bk.id).then(function (data) {
            completed++;
            progressEl.textContent = 'Loading books… ' + completed + ' / ' + total;
            if (!data) return;
            Object.keys(data).forEach(function (ch) {
              Object.keys(data[ch]).forEach(function (v) {
                var tokens = data[ch][v];
                var phrases = [];
                tokens.forEach(function (tok) {
                  if (tok.s === rawId && tok.text) {
                    phrases.push(tok.text);
                    var norm = _wdNormalizePhrase(tok.text);
                    translationCount[norm] = (translationCount[norm] || 0) + 1;
                    totalCount++;
                    /* WD-C: collect morph codes */
                    if (tok.m) morphCount[tok.m] = (morphCount[tok.m] || 0) + 1;
                  }
                });
                if (phrases.length) {
                  if (!bookMatches[bk.id]) bookMatches[bk.id] = { book: bk, verses: [] };
                  bookMatches[bk.id].verses.push({ ch: ch, v: v, phrases: phrases });
                }
              });
            });
          });
        })).then(function () { return _processBatch(chunkIdx + 1); });
      }

      return _processBatch(0).then(function () {
        return { bookMatches: bookMatches, totalCount: totalCount, translationCount: translationCount, morphCount: morphCount };
      });
    })
    .then(function (results) {
      var bookMatches      = results.bookMatches;
      var totalCount       = results.totalCount;
      var translationCount = results.translationCount;

      /* WD-A: remove progress indicator */
      var prog = document.getElementById('wd-progress');
      if (prog) prog.parentNode.removeChild(prog);

      if (!totalCount) {
        document.getElementById('wd-stats').removeAttribute('hidden');
        document.getElementById('wd-stats').innerHTML =
          '<p class="wd-no-results">No occurrences found for ' + escHtml(rawId) + '.</p>';
        return;
      }

      var bookList = Object.keys(bookMatches).map(function (id) { return bookMatches[id]; });
      _wdBookList   = bookList;
      _wdMorphCount = results.morphCount;

      /* WD-B: restore filters from URL hash before first render */
      var h = _wdReadHash();
      _wdCurrentFilter = h.trans;
      _wdCurrentBook   = h.book;

      _wdRenderStats(totalCount, bookList.length, translationCount, results.morphCount);
      _wdRenderRelatedWords(_wdEntry, _wdStrongsDict);
      _wdRenderTranslations();
      _wdRenderBooks();
      _wdRenderVerses(rawId);
    })
    .catch(function (err) {
      var prog = document.getElementById('wd-progress');
      if (prog) prog.parentNode.removeChild(prog);
      headerEl.innerHTML = '<p class="wd-error">Failed to load data: ' + escHtml(String(err)) + '</p>';
    });
}

function _wdRenderHeader(rawId, entry, lexEntry, el) {
  var isGreek = rawId.charAt(0) === 'G';
  var html = '<div class="wd-header-inner">';
  html += '<span class="wd-id">' + escHtml(rawId) + '</span>';
  if (entry) {
    if (entry.lemma)    html += '<span class="wd-lemma">'    + escHtml(entry.lemma)    + '</span>';
    if (entry.translit) html += '<span class="wd-translit">' + escHtml(entry.translit) + '</span>';
    if (entry.pronounce) html += '<span class="wd-pronounce">(' + escHtml(entry.pronounce) + ')</span>';
    html += '</div>';
    if (entry.gloss) html += '<div class="wd-gloss">' + escHtml(entry.gloss) + '</div>';
    if (entry.def && entry.def !== entry.gloss) {
      html += _wdRenderDefChips(entry.def);
    }
    if (entry.deriv) html += '<div class="wd-deriv">' + escHtml(entry.deriv) + '</div>';
  } else {
    html += '</div><p class="wd-no-entry">Strong\'s dictionary entry not found for ' + escHtml(rawId) + '.</p>';
  }
  if (lexEntry && (lexEntry.short_def || lexEntry.long_def)) {
    var lexLabel = isGreek ? 'Thayer' : 'BDB';
    var short = lexEntry.short_def || '';
    var long_ = lexEntry.long_def  || '';
    var showToggle = long_ && long_ !== short && long_.length > short.length + 10;
    html += '<div class="wd-lexicon">' +
      '<span class="wd-lexicon-label">' + lexLabel + '</span>' +
      '<span class="wd-lexicon-short">' + escHtml(short) + '</span>';
    if (showToggle) {
      html += '<div class="wd-lexicon-long" hidden>' + escHtml(long_) + '</div>' +
              '<button class="wd-lexicon-toggle" type="button">+ full entry</button>';
    }
    html += '</div>';
  }
  /* WD-H: Strong's (1890) as a second lexical source card */
  if (entry && (entry.gloss || entry.def)) {
    html += '<div class="wd-lexicon wd-lexicon--strongs">' +
      '<span class="wd-lexicon-label">Strong\'s (1890)</span>' +
      '<span class="wd-lexicon-short">' + escHtml(entry.gloss || '') + '</span>';
    if (entry.def && entry.def !== entry.gloss) {
      html += '<div class="wd-lexicon-long" hidden>' + escHtml(entry.def) + '</div>' +
              '<button class="wd-lexicon-toggle" type="button">+ full entry</button>';
    }
    html += '</div>';
  }
  el.innerHTML = html;

  var toggle = el.querySelector('.wd-def-toggle');
  var extra  = el.querySelector('.wd-def-extra');
  if (toggle && extra) {
    toggle.addEventListener('click', function () {
      var open = extra.style.display !== 'none';
      extra.style.display = open ? 'none' : '';
      toggle.textContent = open ? '+ more' : '− less';
    });
  }
  var lexToggle = el.querySelector('.wd-lexicon-toggle');
  var lexLong   = el.querySelector('.wd-lexicon-long');
  if (lexToggle && lexLong) {
    lexToggle.addEventListener('click', function () {
      var hidden = lexLong.hasAttribute('hidden');
      if (hidden) { lexLong.removeAttribute('hidden'); lexToggle.textContent = '− less'; }
      else         { lexLong.setAttribute('hidden', ''); lexToggle.textContent = '+ full entry'; }
    });
  }
}

function _wdRenderDefChips(def) {
  var items = def.split(/,\s*/);
  var primary = [];
  var tagged  = [];

  items.forEach(function (raw) {
    var item = raw.trim();
    if (!item) return;
    var m = item.match(/^\[([^\]]+)\]\s*(.*)/);
    if (m) {
      var label = m[2].trim() || m[1];
      tagged.push('<span class="wd-def-chip wd-def-chip--tagged" title="' + escHtml(m[1]) + '">' +
        escHtml(label) + '</span>');
    } else {
      primary.push('<span class="wd-def-chip">' + escHtml(item) + '</span>');
    }
  });

  var html = '<div class="wd-def-chips">';
  html += primary.join('');
  if (tagged.length) {
    html += '<div class="wd-def-extra" style="display:none">' + tagged.join('') + '</div>';
    html += '<button class="wd-def-toggle">+ more</button>';
  }
  html += '</div>';
  return html;
}

function _wdRenderStats(total, bookCount, translationCount, morphCount) {
  var uniqueTranslations = Object.keys(translationCount).length;
  var statsEl = document.getElementById('wd-stats');
  statsEl.innerHTML =
    '<div class="wd-stat-card"><span class="wd-stat-num">' + total + '</span><span class="wd-stat-label">occurrences</span></div>' +
    '<div class="wd-stat-card"><span class="wd-stat-num">' + bookCount + '</span><span class="wd-stat-label">books</span></div>' +
    '<div class="wd-stat-card"><span class="wd-stat-num">' + uniqueTranslations + '</span><span class="wd-stat-label">unique translations</span></div>';
  /* WD-G: "By genre" breakdown chips */
  var genreCounts = {};
  (_wdBookList || []).forEach(function (bm) {
    var genre = (bm.book.genre || 'other');
    genreCounts[genre] = (genreCounts[genre] || 0) + bm.verses.length;
  });
  var genreKeys = Object.keys(genreCounts).sort(function (a, b) {
    return genreCounts[b] - genreCounts[a];
  });
  if (genreKeys.length > 1) {
    var genreHtml = '<div class="wd-genre-row">';
    genreKeys.forEach(function (g) {
      genreHtml += '<span class="wd-genre-chip">' + escHtml(g) +
        ' <span class="wd-genre-count">' + genreCounts[g] + '</span></span>';
    });
    genreHtml += '</div>';
    statsEl.insertAdjacentHTML('beforeend', genreHtml);
  }

  statsEl.removeAttribute('hidden');
  var bodyEl = document.getElementById('wd-body');
  if (bodyEl) bodyEl.removeAttribute('hidden');

  /* WD-C: morph table — inserted between stat cards and body */
  if (morphCount && Object.keys(morphCount).length) {
    var morphEl = document.getElementById('wd-morph-table-wrap');
    if (!morphEl) {
      morphEl = document.createElement('div');
      morphEl.id = 'wd-morph-table-wrap';
      statsEl.parentNode.insertBefore(morphEl, bodyEl);
    }
    _wdRenderMorphTable(morphCount, morphEl);
  }
}

/* WD-C: expand morph codes and render a sortable table */
function _wdRenderMorphTable(morphCount, container) {
  var pairs = Object.keys(morphCount).map(function (code) {
    return { code: code, label: expandMorphCode(code) || code, count: morphCount[code] };
  });
  pairs.sort(function (a, b) { return b.count - a.count; });

  var html = '<table class="wd-morph-table">' +
    '<thead><tr><th>Form</th><th>Code</th><th>Count</th></tr></thead><tbody>';
  pairs.forEach(function (p) {
    html += '<tr><td>' + escHtml(p.label) + '</td><td class="wd-morph-code">' +
      escHtml(p.code) + '</td><td class="wd-morph-n">' + p.count + '</td></tr>';
  });
  html += '</tbody></table>';
  container.innerHTML = html;
}

/* WD-L: render "Related Words" pill grid from see_also cross-refs in the strongs entry.
// INTENT: Surface near-synonym and root-word links already encoded in the `deriv` field so the
//   user can jump to semantic neighbors without returning to search. `see_also` arrays were
//   generated by scripts/add-see-also.py from G\d+/H\d+ patterns in each entry's `deriv` text.
// CHANGE? If word.js's DOM insertion order changes (morph table position), update the
//   insertBefore reference target (#wd-morph-table-wrap or #wd-body accordingly).
// VERIFY: Load ?s=G26 (agape); related words panel should show G25 (agapao) and G5368 (phileo)
//   pills. Load ?s=H3068 (YHWH); panel should show H430 (Elohim). Panel absent for simple
//   words with no cross-refs. */
function _wdRenderRelatedWords(entry, strongsDict) {
  var refs = entry && Array.isArray(entry.see_also) ? entry.see_also : [];
  /* cap at 12 pills — deriv chains can be long for complex compound words */
  refs = refs.slice(0, 12);

  var existingEl = document.getElementById('wd-related-wrap');
  if (existingEl) existingEl.parentNode.removeChild(existingEl);
  if (!refs.length || !strongsDict) return;

  var pills = refs.filter(function (id) {
    return strongsDict[id] && strongsDict[id].lemma;
  });
  if (!pills.length) return;

  var wrap = document.createElement('div');
  wrap.id = 'wd-related-wrap';
  wrap.className = 'wd-related-wrap';

  var heading = document.createElement('h3');
  heading.className = 'wd-related-heading';
  heading.textContent = 'Related Words';
  wrap.appendChild(heading);

  var grid = document.createElement('div');
  grid.className = 'wd-related-grid';

  pills.forEach(function (id) {
    var e = strongsDict[id];
    var pill = document.createElement('a');
    pill.className = 'wd-related-pill';
    pill.href = WORD_URL + '?s=' + encodeURIComponent(id);
    pill.title = id + ' — ' + (e.def || e.gloss || '');
    pill.innerHTML = '<span class="wd-related-id">' + escHtml(id) + '</span>' +
                     '<span class="wd-related-lemma">' + escHtml(e.lemma || '') + '</span>' +
                     '<span class="wd-related-gloss">' + escHtml(e.gloss || '') + '</span>';
    grid.appendChild(pill);
  });

  wrap.appendChild(grid);

  /* insert after morph table (if present) or after stats, before body */
  var bodyEl   = document.getElementById('wd-body');
  var morphEl  = document.getElementById('wd-morph-table-wrap');
  var anchor   = morphEl || document.getElementById('wd-stats');
  if (anchor && anchor.parentNode) {
    anchor.parentNode.insertBefore(wrap, anchor.nextSibling || bodyEl);
  }
}

var _wdStopWords = (function () {
  var w = 'a an the to unto from with by in of at for on upon into through about before after ' +
          'over under against between among ' +
          'i me my mine we us our ours you your yours ' +
          'he him his she her hers it its they them their theirs ' +
          'ye thy thine thou thee ' +
          'and or but nor ' +
          'doth hath is was be am are were shall will do did does had have has ' +
          'let not neither also even thus so yet then now ' +
          'that which this these those yea nay no';
  var set = {};
  w.split(' ').forEach(function (t) { set[t] = true; });
  return set;
}());

function _wdNormalizePhrase(raw) {
  var s = (raw || '').toLowerCase().trim();
  s = s.replace(/(\w)'s\b/g, '$1').replace(/(\w)s'\s/g, '$1s ');
  var words = s.split(/\s+/);
  while (words.length > 1 && _wdStopWords[words[0]]) {
    words.shift();
  }
  return words.join(' ') || s;
}

function _wdCalcTranslationCounts(bookFilter) {
  var counts = {};
  (_wdBookList || []).forEach(function (bm) {
    if (bookFilter && bm.book.id !== bookFilter) return;
    bm.verses.forEach(function (occ) {
      occ.phrases.forEach(function (p) {
        var n = _wdNormalizePhrase(p);
        counts[n] = (counts[n] || 0) + 1;
      });
    });
  });
  return counts;
}

function _wdCalcBookCounts(translationFilter) {
  var counts = {};
  (_wdBookList || []).forEach(function (bm) {
    var n = translationFilter
      ? bm.verses.filter(function (occ) {
          return occ.phrases.some(function (p) { return _wdNormalizePhrase(p) === translationFilter; });
        }).length
      : bm.verses.length;
    if (n > 0) counts[bm.book.id] = n;
  });
  return counts;
}

function _wdRenderTranslations() {
  var section = document.getElementById('wd-translations');
  var body    = document.getElementById('wd-translations-body');
  if (!body) return;

  var counts = _wdCalcTranslationCounts(_wdCurrentBook);
  var total  = Object.keys(counts).reduce(function (s, k) { return s + counts[k]; }, 0);
  var pairs  = Object.keys(counts).map(function (k) { return { phrase: k, count: counts[k] }; });
  pairs.sort(function (a, b) { return b.count - a.count; });

  /* WD-K: label above the list */
  var html = '<p class="wd-trans-label">How this word is translated:</p>';

  /* WD-D: "All" row that clears the filter */
  var allActive = !_wdCurrentFilter;
  html += '<button class="wd-translation-row' + (allActive ? ' wd-translation-row--active' : '') +
    '" data-phrase="" title="Show all translations">' +
    '<span class="wd-translation-phrase">All translations</span>' +
    '<div class="wd-translation-bar-wrap"><div class="wd-translation-bar" style="width:100%"></div></div>' +
    '<span class="wd-translation-count">' + total + '</span>' +
    '</button>';

  pairs.forEach(function (p) {
    var pct    = total ? Math.round((p.count / total) * 100) : 0;
    var active = p.phrase === _wdCurrentFilter;
    html += '<button class="wd-translation-row' + (active ? ' wd-translation-row--active' : '') +
      '" data-phrase="' + escHtml(p.phrase) + '"' +
      ' title="Click to filter by this translation">' +
      '<span class="wd-translation-phrase">' + escHtml(p.phrase) + '</span>' +
      '<div class="wd-translation-bar-wrap">' +
      '<div class="wd-translation-bar" style="width:' + pct + '%"></div>' +
      '</div>' +
      /* WD-K: show percentage next to count */
      '<span class="wd-translation-count">' + p.count + ' <span class="wd-trans-pct">(' + pct + '%)</span></span>' +
      '</button>';
  });
  body.innerHTML = html;

  if (!body._transWired) {
    body._transWired = true;
    body.addEventListener('click', function (e) {
      var row = e.target.closest('.wd-translation-row');
      if (!row) return;
      /* empty data-phrase means "All" — pass null to clear */
      _wdToggleFilter(row.dataset.phrase || null);
    });
  }

  section.removeAttribute('hidden');
}

function _wdToggleFilter(phrase) {
  /* null or same phrase → clear; otherwise set */
  _wdCurrentFilter = (phrase && phrase !== _wdCurrentFilter) ? phrase : null;
  _wdWriteHash();
  _wdRenderBooks();
  _wdRenderTranslations();
  _wdRefreshVerses();
}

function _wdToggleBook(bookId) {
  _wdCurrentBook = (bookId && bookId !== _wdCurrentBook) ? bookId : null;
  _wdWriteHash();
  _wdRenderBooks();
  _wdRenderTranslations();
  _wdRefreshVerses();
}

function _wdRenderBooks() {
  var section = document.getElementById('wd-books');
  var body    = document.getElementById('wd-books-body');
  if (!body) return;

  var counts = _wdCalcBookCounts(_wdCurrentFilter);
  var sorted = (_wdBookList || []).slice().sort(function (a, b) {
    return (a.book.bookNumber || 0) - (b.book.bookNumber || 0);
  });

  /* WD-D: "All books" pill clears the book filter */
  var allBooksActive = !_wdCurrentBook;
  var totalVerses = Object.keys(counts).reduce(function (s, k) { return s + counts[k]; }, 0);
  var html = '<button class="wd-book-pill' + (allBooksActive ? ' wd-book-pill--active' : '') +
    '" data-book="" title="Show all books">' +
    'All <span class="wd-book-count">' + totalVerses + '</span></button>';

  sorted.forEach(function (bm) {
    var count = counts[bm.book.id] || 0;
    if (!count) return;
    var active = bm.book.id === _wdCurrentBook;
    html += '<button class="wd-book-pill' + (active ? ' wd-book-pill--active' : '') +
      '" data-book="' + escHtml(bm.book.id) + '"' +
      ' title="Click to filter by this book">' +
      escHtml(bm.book.name) + ' <span class="wd-book-count">' + count + '</span></button>';
  });
  body.innerHTML = html;

  if (!body._bookWired) {
    body._bookWired = true;
    body.addEventListener('click', function (e) {
      var pill = e.target.closest('.wd-book-pill[data-book]');
      if (!pill) return;
      /* empty data-book means "All books" — pass null to clear */
      _wdToggleBook(pill.dataset.book || null);
    });
  }

  section.removeAttribute('hidden');
}

function _wdRefreshVerses() {
  var section = document.getElementById('wd-verses');
  if (section && section._applyFilters) section._applyFilters(_wdCurrentFilter, _wdCurrentBook);
}

function _wdRenderVerses(strongsId) {
  var section    = document.getElementById('wd-verses');
  var statusEl   = document.getElementById('wd-verses-status');
  var body       = document.getElementById('wd-verses-body');
  var version    = getVersion();

  section.removeAttribute('hidden');

  var sorted = (_wdBookList || []).slice().sort(function (a, b) {
    return (a.book.bookNumber || 0) - (b.book.bookNumber || 0);
  });

  function renderVerseCard(occ, book, bookSection, ver) {
    var refStr = book.name + ' ' + occ.ch + ':' + occ.v;
    var card = document.createElement('div');
    card.className = 'wd-verse-card';

    var refLink = document.createElement('a');
    refLink.className = 'ref wd-verse-ref-link';
    refLink.dataset.ref = refStr;
    refLink.href = '#';
    refLink.textContent = refStr;
    card.appendChild(refLink);

    var textEl = document.createElement('div');
    textEl.className = 'wd-verse-text';
    textEl.textContent = 'Loading…';
    card.appendChild(textEl);
    bookSection.appendChild(card);

    var termSet = {};
    occ.phrases.forEach(function (p) {
      var lo = p.toLowerCase().trim();
      if (lo) termSet[lo] = true;
      var norm = _wdNormalizePhrase(p);
      if (norm) termSet[norm] = true;
    });
    var searchTerms = Object.keys(termSet).sort(function (a, b) { return b.length - a.length; });
    searchTerms = searchTerms.filter(function (term, i) {
      var re = new RegExp('\\b' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b');
      for (var j = 0; j < i; j++) { if (re.test(searchTerms[j])) return false; }
      return true;
    });

    var parsed = parseRef(refStr);
    resolveVerses(parsed, ver).then(function (rows) {
      var text = rows && rows[0] && rows[0].text;
      if (text) {
        var marked = text;
        searchTerms.forEach(function (term) {
          var esc = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
          marked = marked.replace(new RegExp('\\b(' + esc + ')\\b', 'gi'), '\x00$1\x01');
        });
        textEl.innerHTML = marked.split(/\x00([^\x01]*)\x01/).map(function (seg, i) {
          return i % 2 === 0
            ? escHtml(seg)
            : '<mark class="wd-highlight">' + escHtml(seg) + '</mark>';
        }).join('');
        autoTagTermsWhenReady(textEl);
      } else {
        textEl.textContent = '(verse not available)';
      }
    }).catch(function () {
      textEl.textContent = '(could not load)';
    });
  }

  function render(ver, translationFilter, bookFilter) {
    body.innerHTML = '';
    statusEl.innerHTML = '';

    var chips = '';
    if (translationFilter) chips += '<span class="wd-chip">"' + escHtml(translationFilter) +
      '" <button class="wd-chip-clear" data-clear="trans">×</button></span>';
    if (bookFilter) {
      var bm2 = (_wdBookList || []).find(function (b) { return b.book.id === bookFilter; });
      var bName = bm2 ? bm2.book.name : bookFilter;
      chips += '<span class="wd-chip">' + escHtml(bName) +
        ' <button class="wd-chip-clear" data-clear="book">×</button></span>';
    }
    if (chips) {
      /* WD-D/WD-J: show "Clear all filters" when both filters are active */
      if (translationFilter && bookFilter) {
        chips += '<button class="wd-filter-clear-all" style="margin-left:auto">Clear all</button>';
      }
      var chipBar = document.createElement('div');
      chipBar.className = 'wd-filter-bar';
      chipBar.innerHTML = chips;
      chipBar.addEventListener('click', function (e) {
        var btn = e.target.closest('.wd-chip-clear');
        if (btn) {
          if (btn.dataset.clear === 'trans') _wdToggleFilter(_wdCurrentFilter);
          else _wdToggleBook(_wdCurrentBook);
          return;
        }
        if (e.target.closest('.wd-filter-clear-all')) {
          _wdCurrentFilter = null;
          _wdCurrentBook   = null;
          _wdWriteHash();
          _wdRenderBooks();
          _wdRenderTranslations();
          _wdRefreshVerses();
        }
      });
      statusEl.appendChild(chipBar);
    }

    var total = 0;
    sorted.forEach(function (bm) {
      if (bookFilter && bm.book.id !== bookFilter) return;
      var occs = translationFilter
        ? bm.verses.filter(function (occ) {
            return occ.phrases.some(function (p) { return _wdNormalizePhrase(p) === translationFilter; });
          })
        : bm.verses;
      if (!occs.length) return;
      total += occs.length;

      var bookSection = document.createElement('div');
      bookSection.className = 'wd-book-section';
      bookSection.id = 'wd-book-' + bm.book.id;

      var heading = document.createElement('h3');
      heading.className = 'wd-book-heading';
      heading.textContent = bm.book.name;

      /* WD-E: "Read in context" link per book section */
      var readerLink = document.createElement('a');
      readerLink.className = 'wd-book-reader-link';
      readerLink.href = '../read/?book=' + encodeURIComponent(bm.book.id);
      readerLink.textContent = 'Read in context →';
      heading.appendChild(readerLink);

      bookSection.appendChild(heading);
      body.appendChild(bookSection);

      occs.forEach(function (occ) { renderVerseCard(occ, bm.book, bookSection, ver); });
    });

    if (!total) {
      var empty = document.createElement('p');
      empty.className = 'wd-no-results';
      empty.textContent = 'No occurrences match the active filters.';
      body.appendChild(empty);
    }

    var countEl = document.createElement('p');
    countEl.className = 'wd-verses-count';
    countEl.textContent = total + ' verse' + (total === 1 ? '' : 's');
    statusEl.appendChild(countEl);

    wireRefLinks();
  }

  section._rerenderFn  = function (ver) { render(ver, _wdCurrentFilter, _wdCurrentBook); };
  section._applyFilters = function (tf, bf) { render(getVersion(), tf, bf); };
  render(version, null, null);

  /* WD-I: keyboard navigation through verse list */
  var _focusedCardIdx = -1;
  document.addEventListener('keydown', function (e) {
    /* Ignore when focused inside an input or textarea */
    var tag = (e.target.tagName || '').toUpperCase();
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;

    var cards = Array.prototype.slice.call(body.querySelectorAll('.wd-verse-card'));

    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      if (!cards.length) return;
      if (_focusedCardIdx >= 0 && _focusedCardIdx < cards.length) {
        cards[_focusedCardIdx].classList.remove('wd-verse-card--focused');
      }
      _focusedCardIdx = e.key === 'ArrowDown'
        ? Math.min(_focusedCardIdx + 1, cards.length - 1)
        : Math.max(_focusedCardIdx - 1, 0);
      var card = cards[_focusedCardIdx];
      card.classList.add('wd-verse-card--focused');
      card.scrollIntoView({ block: 'nearest' });
      return;
    }
    if (e.key === 'b') {
      var booksBody = document.getElementById('wd-books-body');
      if (booksBody) { var firstPill = booksBody.querySelector('.wd-book-pill'); if (firstPill) firstPill.focus(); }
      return;
    }
    if (e.key === 't') {
      var transBody = document.getElementById('wd-translations-body');
      if (transBody) { var firstRow = transBody.querySelector('.wd-translation-row'); if (firstRow) firstRow.focus(); }
      return;
    }
    if (e.key === 'Escape') {
      if (_wdCurrentFilter || _wdCurrentBook) {
        _wdCurrentFilter = null;
        _wdCurrentBook   = null;
        _wdWriteHash();
        _wdRenderBooks();
        _wdRenderTranslations();
        _wdRefreshVerses();
      }
    }
  });
}
