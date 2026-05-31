/* word.js — Word Deep Dive page */
'use strict';

import {
  SEARCH_URL, WORD_URL, metaBooks,
  getVersion, escHtml, parseRef, resolveVerses,
  loadStrongs, loadLexicon, loadInterlinear, onVersionChange
} from './core.js';
import { wireRefLinks } from './wire.js';
import { expandMorphCode } from './interlinear.js';

var _wdCurrentFilter = null;
var _wdCurrentBook   = null;
var _wdBookList      = null;

export function initWordPage() {
  var params   = new URLSearchParams(window.location.search);
  var rawId    = (params.get('s') || '').trim().toUpperCase();
  var headerEl = document.getElementById('wd-header');

  if (!rawId || !/^[GH]\d+$/.test(rawId)) {
    headerEl.innerHTML = '<p class="wd-error">No Strong\'s number provided. Use <code>?s=G3056</code> or <code>?s=H430</code>.</p>';
    return;
  }

  document.title = rawId + ' — Word Study — Bible Study';

  var backLink = document.getElementById('wd-back-link');
  if (backLink) backLink.href = SEARCH_URL + '?s=' + encodeURIComponent(rawId);

  var testament = rawId[0] === 'G' ? 'greek' : 'hebrew';

  onVersionChange(function (ver) {
    var versesSection = document.getElementById('wd-verses');
    if (versesSection && versesSection._rerenderFn) versesSection._rerenderFn(ver);
  });

  Promise.all([loadStrongs(testament), loadLexicon(testament)])
    .then(function (results) {
      var strongsDict = results[0];
      var lexDict     = results[1];
      var entry    = strongsDict && strongsDict[rawId];
      var lexEntry = lexDict    && lexDict[rawId];

      _wdRenderHeader(rawId, entry, lexEntry, headerEl);

      var books = metaBooks.filter(function (b) {
        return b.testament === (testament === 'greek' ? 'NT' : 'OT');
      });

      var bookMatches      = {};
      var totalCount       = 0;
      var translationCount = {};

      var fetches = books.map(function (bk) {
        return loadInterlinear(bk.id).then(function (data) {
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
                }
              });
              if (phrases.length) {
                if (!bookMatches[bk.id]) bookMatches[bk.id] = { book: bk, verses: [] };
                bookMatches[bk.id].verses.push({ ch: ch, v: v, phrases: phrases });
              }
            });
          });
        });
      });

      return Promise.all(fetches).then(function () {
        return { bookMatches: bookMatches, totalCount: totalCount, translationCount: translationCount };
      });
    })
    .then(function (results) {
      var bookMatches      = results.bookMatches;
      var totalCount       = results.totalCount;
      var translationCount = results.translationCount;

      if (!totalCount) {
        document.getElementById('wd-stats').removeAttribute('hidden');
        document.getElementById('wd-stats').innerHTML =
          '<p class="wd-no-results">No occurrences found for ' + escHtml(rawId) + '.</p>';
        return;
      }

      var bookList = Object.keys(bookMatches).map(function (id) { return bookMatches[id]; });
      _wdBookList      = bookList;
      _wdCurrentFilter = null;
      _wdCurrentBook   = null;

      _wdRenderStats(totalCount, bookList.length, translationCount);
      _wdRenderTranslations();
      _wdRenderBooks();
      _wdRenderVerses(rawId);
    })
    .catch(function (err) {
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

function _wdRenderStats(total, bookCount, translationCount) {
  var uniqueTranslations = Object.keys(translationCount).length;
  var statsEl = document.getElementById('wd-stats');
  statsEl.innerHTML =
    '<div class="wd-stat-card"><span class="wd-stat-num">' + total + '</span><span class="wd-stat-label">occurrences</span></div>' +
    '<div class="wd-stat-card"><span class="wd-stat-num">' + bookCount + '</span><span class="wd-stat-label">books</span></div>' +
    '<div class="wd-stat-card"><span class="wd-stat-num">' + uniqueTranslations + '</span><span class="wd-stat-label">unique translations</span></div>';
  statsEl.removeAttribute('hidden');
  var bodyEl = document.getElementById('wd-body');
  if (bodyEl) bodyEl.removeAttribute('hidden');
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

  var html = '';
  pairs.forEach(function (p) {
    var pct    = total ? Math.round((p.count / total) * 100) : 0;
    var active = p.phrase === _wdCurrentFilter;
    html += '<button class="wd-translation-row' + (active ? ' wd-translation-row--active' : '') +
      '" data-phrase="' + escHtml(p.phrase) + '">' +
      '<span class="wd-translation-phrase">' + escHtml(p.phrase) + '</span>' +
      '<div class="wd-translation-bar-wrap">' +
      '<div class="wd-translation-bar" style="width:' + pct + '%"></div>' +
      '</div>' +
      '<span class="wd-translation-count">' + p.count + '</span>' +
      '</button>';
  });
  body.innerHTML = html;

  if (!body._transWired) {
    body._transWired = true;
    body.addEventListener('click', function (e) {
      var row = e.target.closest('.wd-translation-row');
      if (!row) return;
      _wdToggleFilter(row.dataset.phrase);
    });
  }

  section.removeAttribute('hidden');
}

function _wdToggleFilter(phrase) {
  _wdCurrentFilter = (phrase === _wdCurrentFilter) ? null : phrase;
  _wdRenderBooks();
  _wdRefreshVerses();
}

function _wdToggleBook(bookId) {
  _wdCurrentBook = (bookId === _wdCurrentBook) ? null : bookId;
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

  var html = '';
  sorted.forEach(function (bm) {
    var count = counts[bm.book.id] || 0;
    if (!count) return;
    var active = bm.book.id === _wdCurrentBook;
    html += '<button class="wd-book-pill' + (active ? ' wd-book-pill--active' : '') +
      '" data-book="' + escHtml(bm.book.id) + '">' +
      escHtml(bm.book.name) + ' <span class="wd-book-count">' + count + '</span></button>';
  });
  body.innerHTML = html;

  if (!body._bookWired) {
    body._bookWired = true;
    body.addEventListener('click', function (e) {
      var pill = e.target.closest('.wd-book-pill[data-book]');
      if (!pill) return;
      _wdToggleBook(pill.dataset.book);
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
      var chipBar = document.createElement('div');
      chipBar.className = 'wd-filter-bar';
      chipBar.innerHTML = chips;
      chipBar.addEventListener('click', function (e) {
        var btn = e.target.closest('.wd-chip-clear');
        if (!btn) return;
        if (btn.dataset.clear === 'trans') _wdToggleFilter(_wdCurrentFilter);
        else _wdToggleBook(_wdCurrentBook);
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
}
