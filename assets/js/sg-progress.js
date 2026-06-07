/* sg-progress.js — Study guide session progress tracking
 * Storage key: bsw_sg_progress
 * Shape: { [slug]: [sectionId, ...] }
 */

var _SG_KEY = 'bsw_sg_progress';

function _load() {
  try { return JSON.parse(localStorage.getItem(_SG_KEY)) || {}; } catch (e) { return {}; }
}

function _save(data) {
  try { localStorage.setItem(_SG_KEY, JSON.stringify(data)); } catch (e) {}
}

export function markComplete(slug, sectionId) {
  var data = _load();
  if (!data[slug]) data[slug] = [];
  if (data[slug].indexOf(sectionId) === -1) data[slug].push(sectionId);
  data[slug + '_lastUpdated'] = new Date().toISOString();
  _save(data);
}

export function markIncomplete(slug, sectionId) {
  var data = _load();
  if (!data[slug]) return;
  data[slug] = data[slug].filter(function (id) { return id !== sectionId; });
  data[slug + '_lastUpdated'] = new Date().toISOString();
  _save(data);
}

export function isComplete(slug, sectionId) {
  var data = _load();
  return !!(data[slug] && data[slug].indexOf(sectionId) !== -1);
}

export function getProgress(slug) {
  var data = _load();
  return { done: data[slug] ? data[slug].length : 0, completed: data[slug] || [] };
}

/* initSgProgress — wire "Mark complete" buttons on a study guide page.
 * Call after DOM is ready. slug identifies the guide (e.g. "hebrews").
 * total is the total number of completable sections for progress display.
 */
// INTENT: Wire "Mark complete" toggle buttons onto every .tg-section[id] element
//   for a given study-guide slug; persists state to bsw_sg_progress via _SG_KEY
//   and calls _refreshTabDots so chapter-tab completion indicators stay in sync.
// CHANGE? If study guide HTML renames .tg-section[id] → another selector, update
//   the querySelectorAll here and in _refreshTabDots. If bsw_sg_progress schema
//   changes ({ [slug]: string[] }), update _load/_save plus store.js exportAll.
// VERIFY: Open /study-guides/hebrews/ → click "Mark complete" on section 1 →
//   button changes to "✓ Completed" and a dot appears on the chapter tab. Reload
//   → state persists. Click again → reverts cleanly.
export function initSgProgress(slug, total) {
  var data     = _load();
  var completed = data[slug] || [];

  document.querySelectorAll('.tg-section[id]').forEach(function (sec) {
    var sectionId = sec.id;
    var done      = completed.indexOf(sectionId) !== -1;

    var btn = document.createElement('button');
    btn.type      = 'button';
    btn.className = 'sg-complete-btn' + (done ? ' sg-complete-btn--done' : '');
    btn.dataset.section = sectionId;
    btn.textContent     = done ? '✓ Completed' : 'Mark complete';
    btn.setAttribute('aria-pressed', String(done));

    btn.addEventListener('click', function () {
      var nowDone = btn.getAttribute('aria-pressed') !== 'true';
      if (nowDone) {
        markComplete(slug, sectionId);
        btn.textContent = '✓ Completed';
        btn.classList.add('sg-complete-btn--done');
      } else {
        markIncomplete(slug, sectionId);
        btn.textContent = 'Mark complete';
        btn.classList.remove('sg-complete-btn--done');
      }
      btn.setAttribute('aria-pressed', String(nowDone));
      _refreshTabDots(slug);
    });

    sec.appendChild(btn);
  });

  _refreshTabDots(slug);
}

// INTENT: Append a .sg-tab-dot span to any .sg-tab-btn whose data-target section
//   is completed, and remove it if the section is no longer completed. Called on
//   every mark/unmark to keep the chapter nav visually in sync with progress state.
function _refreshTabDots(slug) {
  var completed = _load()[slug] || [];
  document.querySelectorAll('.sg-tab-btn[data-target]').forEach(function (tab) {
    var target = tab.dataset.target;
    var isDone = completed.indexOf(target) !== -1;
    var dot    = tab.querySelector('.sg-tab-dot');
    if (isDone && !dot) {
      var d = document.createElement('span');
      d.className   = 'sg-tab-dot';
      d.title       = 'Completed';
      d.textContent = '●';
      tab.appendChild(d);
    } else if (!isDone && dot) {
      dot.remove();
    }
  });
}
