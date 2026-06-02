/* lib-reader.js — Unified library document reader (library/read/index.html) */
'use strict';

import { _resolve, escHtml } from './core.js';
import { wireRefLinks, autoTagRefs } from './wire.js';
import { autoTagTermsWhenReady } from './terms.js';

var LIB_DOCS_ROOT = _resolve('../../data/library/docs/');

export function initLibReaderPage() {
  var content = document.getElementById('lib-reader-content');
  if (!content) return;

  var docId = new URLSearchParams(window.location.search).get('doc');
  if (!docId) {
    content.innerHTML = '<p class="lr-error">No document specified. <a href="../">Return to Library</a></p>';
    return;
  }

  content.innerHTML = '<p class="lr-loading">Loading…</p>';

  fetch(LIB_DOCS_ROOT + docId + '.json')
    .then(function(r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function(doc) { _render(doc, content); })
    .catch(function(err) {
      console.error('[LibReader]', err);
      content.innerHTML = '<p class="lr-error">Document not found. <a href="../">Return to Library</a></p>';
    });
}

var _TYPE_BADGE = { creed: 'ecumenical', confession: 'reformed', catechism: 'reformed', canons: 'reformed', father: 'ecumenical' };
var _TYPE_LABEL = { creed: 'Creed', confession: 'Confession', catechism: 'Catechism', canons: 'Canons', father: 'Church Father' };

function _render(doc, content) {
  document.title = doc.title + ' — Library — Bible Study';

  var header = document.getElementById('lib-reader-header');
  if (header) {
    var badge = _TYPE_BADGE[doc.type] || 'ecumenical';
    var label = _TYPE_LABEL[doc.type] || doc.type;
    header.innerHTML =
      '<a class="lr-back" href="../">← Library</a>' +
      '<h1 class="lr-doc-title">' + escHtml(doc.title) + '</h1>' +
      '<div class="lib-meta">' +
        '<span class="lib-badge lib-badge--' + escHtml(badge) + '">' + escHtml(label) + '</span>' +
        (doc.year ? '<span>' + escHtml(String(doc.year)) + '</span>' : '') +
        '<span>' + escHtml(String(doc.totalSections)) + ' ' + escHtml(_sectionLabel(doc)) + '</span>' +
      '</div>';
  }

  var toc = document.getElementById('lib-reader-toc');
  if (toc) {
    if (doc.sections && doc.sections.length > 1) {
      var tocHtml = '<div class="lr-toc-heading">Contents</div><ul class="lr-toc-list">';
      doc.sections.forEach(function(s, i) {
        tocHtml += '<li><a href="#lrs-' + i + '">' + escHtml(s.heading) + '</a></li>';
      });
      toc.innerHTML = tocHtml + '</ul>';
    } else {
      // Single-section documents (short creeds): hide sidebar entirely
      var sidebar = toc.closest('.lr-sidebar');
      if (sidebar) sidebar.hidden = true;
    }
  }

  var html = '';
  if (doc.sections) {
    doc.sections.forEach(function(s, i) {
      html += '<section class="lr-section" id="lrs-' + i + '">' + s.html + '</section>';
    });
  }
  content.innerHTML = html;

  // Wire all interactives into the freshly-injected content
  wireRefLinks(content);
  autoTagRefs();
  autoTagTermsWhenReady(content);

  // Record that this document was opened so the home page can show "Continue reading"
  _saveLibProgress(docId, doc.title, doc.totalSections);
}

var _LIB_PROGRESS_KEY = 'bsw_lib_progress';

function _saveLibProgress(docId, title, totalSections) {
  try {
    var data = JSON.parse(localStorage.getItem(_LIB_PROGRESS_KEY) || '{}');
    var today = new Date().toISOString().slice(0, 10);
    // Keep at most 10 recent documents; evict oldest by lastRead
    data[docId] = { title: title, href: location.href, lastRead: today, totalSections: totalSections || 0 };
    var keys = Object.keys(data);
    if (keys.length > 10) {
      keys.sort(function (a, b) { return data[a].lastRead < data[b].lastRead ? -1 : 1; });
      delete data[keys[0]];
    }
    localStorage.setItem(_LIB_PROGRESS_KEY, JSON.stringify(data));
  } catch (e) { /* non-fatal */ }
}

function _sectionLabel(doc) {
  var n = doc.totalSections;
  if (doc.type === 'catechism') return n === 1 ? 'Question' : 'Questions';
  if (doc.type === 'father')    return n === 1 ? 'Selection' : 'Selections';
  return n === 1 ? 'Section' : 'Chapters';
}
