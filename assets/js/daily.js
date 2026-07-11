/* daily.js — Daily Discipline page, Scripture Memory, Plans home widget */
'use strict';

import {
  READER_URL, metaBooks, metaVersions,
  getVersion, escHtml, parseRef, loadBook, resolveVerses,
  _resolve
} from './core.js';
import { wireRefLinks } from './wire.js';
import { initHistoryWidget, _shareVerseAsImage } from './modal.js';
import { markDone } from './tracker.js';
import {
  MEMORY_KEY, MEMORY_MODE_KEY,
  _memGet, _memSet, _memHas, _memAdd, _memRemove, _memTodayStr,
  _memIsDue, _memApplyScore, _memDaysUntil, _memAllTags,
  _memTagAdd, _memTagRemove
} from './mem.js';

// ── Daily Page constants ──────────────────────────────────────────────────────
var DAILY_PLAN_KEY   = 'bsw_daily_plan';
var DAILY_DEVOT_KEY  = 'bsw_daily_devot';
var DAILY_NOTIF_KEY  = 'bsw_daily_notif';
var DAILY_NOTIF_DISMISSED = 'bsw_daily_notif_dismissed';
var DAILY_PLANS_ROOT    = _resolve('../../data/plans');
var DAILY_VOTD_URL      = _resolve('../../data/votd/verses.json');
var DAILY_CALENDAR_BASE = _resolve('../../read/');
var DAILY_DEVOT_BASE    = _resolve('../../data/devotionals');

var DAILY_AUTO_PLANS = ['bible-in-a-year', 'bible-in-a-year-chronological'];

var DAILY_PLAN_META = [
  { id: 'bible-in-a-year',               title: 'Bible in a Year',               days: 365 },
  { id: 'bible-in-a-year-chronological', title: 'Bible in a Year — Chronological', days: 365 },
  { id: 'mcheyne',                        title: "M'Cheyne",                       days: 365 },
  { id: 'nt-90-days',                     title: 'NT in 90 Days',                  days: 90  },
  { id: 'psalms-proverbs',               title: 'Psalms & Proverbs',              days: 31  },
  { id: 'gospels-30-days',               title: 'Gospels in 30 Days',             days: 30  }
];

// Catechism plans removed from home page selector; migrate any saved choice
var _CATECHISM_PLAN_IDS = ['heidelberg-weekly', 'wsc-quarterly'];

var DAILY_DEVOT_META = [
  { id: 'variety',          label: 'Variety (rotating authors)' },
  { id: 'spurgeon-morning', label: 'Spurgeon — Morning' },
  { id: 'spurgeon-evening', label: 'Spurgeon — Evening' },
  { id: 'daily-psalms',     label: 'Daily Psalms' },
  { id: 'proverbs-month',   label: 'Proverbs of the Month' },
  { id: 'nt-daily',         label: 'NT Daily Reading' }
];

// INTENT: Every file-backed devotional shares one JSON shape
//   ("MM-DD" -> { verse_text, verse_ref, body }), so they render through a single
//   code path (_dailyRenderDevotEntry). This map is the registry of those files
//   plus the byline shown to the reader. Data is produced by
//   scripts/build-devotionals.py from public-domain editions.
// CHANGE? To add an author: ship its data/devotionals/<slug>.json and add an entry
//   here, then list the slug in DAILY_VARIETY below to include it in the rotation.
var DAILY_DEVOT_SOURCES = {
  'spurgeon-morning': { file: 'spurgeon-morning.json', author: 'Charles Spurgeon', work: 'Morning by Morning' },
  'spurgeon-evening': { file: 'spurgeon-evening.json', author: 'Charles Spurgeon', work: 'Evening by Evening' },
  'winslow-morning':  { file: 'winslow-morning.json',  author: 'Octavius Winslow', work: 'Morning Thoughts' },
  'winslow-evening':  { file: 'winslow-evening.json',  author: 'Octavius Winslow', work: 'Evening Thoughts' },
  'meyer':            { file: 'meyer.json',            author: 'F.B. Meyer',       work: 'Our Daily Walk' },
  'jowett':           { file: 'jowett.json',           author: 'J.H. Jowett',      work: 'My Daily Meditation' }
};

// INTENT: "Variety" rotates to a different author each day, per slot. The index is
//   keyed off day-of-year so it's stable within a day but cycles over time. Both
//   lists are ordered by AUTHOR; the evening slot starts one step ahead of morning
//   (see _dailyResolveVariety), so as long as no two adjacent entries share an
//   author, morning and evening never show the same author on the same date.
// CHANGE? Add new author slugs here once their data ships (period-neutral authors
//   go in BOTH lists). Missing/gap days are handled at render time by falling
//   through to the next author in rotation.
var DAILY_VARIETY = {
  morning: ['winslow-morning', 'spurgeon-morning', 'meyer', 'jowett'],
  evening: ['winslow-evening', 'spurgeon-evening', 'meyer', 'jowett']
};

// ── Streak ────────────────────────────────────────────────────────────────────
var STREAK_KEY = 'bsw_streak';

function _streakFmtDate(d) {
  return d.getFullYear() + '-' +
    String(d.getMonth() + 1).padStart(2, '0') + '-' +
    String(d.getDate()).padStart(2, '0');
}
function _streakPrevDay(ds) {
  var d = new Date(ds + 'T12:00:00');
  return _streakFmtDate(new Date(d.getTime() - 86400000));
}

// INTENT: "Today or yesterday" starting point keeps the streak alive if the user hasn't
//   read yet today but did read yesterday — prevents a midnight reset from breaking a
//   multi-day streak before the user opens the app on the new day.
// CHANGE? If the grace window changes (e.g., "within 36 hours"), update the cursor
//   initialisation below; the same logic appears in tracker.js:isReadingDone.
// VERIFY: On a device, mark a reading day, then advance the OS clock past midnight
//   without opening the app. Reopen — current streak should be unchanged (not 0).
function _computeStreakFromDays(days) {
  if (!days || !days.length) return { current: 0, longest: 0 };
  var set = Object.create(null);
  days.forEach(function (d) { set[d] = true; });
  var today     = _streakFmtDate(new Date());
  var yesterday = _streakPrevDay(today);

  // Current streak: walk backwards from today (or yesterday if not read today yet)
  var current = 0;
  var cursor = set[today] ? today : (set[yesterday] ? yesterday : null);
  while (cursor && set[cursor]) {
    current++;
    cursor = _streakPrevDay(cursor);
  }

  // Longest streak: scan sorted days
  var sorted = days.slice().sort();
  var longest = current;
  var run = 1;
  for (var i = 1; i < sorted.length; i++) {
    if (sorted[i] === sorted[i - 1]) continue; // skip duplicates
    if (sorted[i - 1] === _streakPrevDay(sorted[i])) {
      run++;
      if (run > longest) longest = run;
    } else {
      run = 1;
    }
  }
  return { current: current, longest: longest };
}

// ── Helper functions ──────────────────────────────────────────────────────────
function _dailyDayOfYear() {
  var now   = new Date();
  var start = new Date(now.getFullYear(), 0, 1);
  return Math.floor((now - start) / 86400000) + 1;
}

function _dailyPeriod() {
  return new Date().getHours() < 12 ? 'morning' : 'evening';
}

function _dailyDayNum(planId, startDateStr) {
  if (DAILY_AUTO_PLANS.indexOf(planId) !== -1) {
    return _dailyDayOfYear();
  }
  if (!startDateStr) return 1;
  var start = new Date(startDateStr + 'T00:00:00');
  var today = new Date();
  today = new Date(today.getFullYear(), today.getMonth(), today.getDate());
  return Math.max(1, Math.floor((today - start) / 86400000) + 1);
}

function _dailyPassageUrl(passage) {
  return DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(passage);
}

function _dailyReadAllUrl(passages) {
  return DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(passages.join(', '));
}

// ── initDailyPage ─────────────────────────────────────────────────────────────
// INTENT: Bootstrap the full daily reading page (daily.html) — reads DAILY_PLAN_KEY
//   and DAILY_DEVOT_KEY from localStorage to restore the user's last plan and
//   devotional selection, reads bsw_daily_start_{pid} to compute today's day
//   number, and renders greeting, plan passages, VOTD, and devotional sections.
// CHANGE? Depends on localStorage keys: DAILY_PLAN_KEY, DAILY_DEVOT_KEY,
//   `bsw_daily_start_${planId}`, STREAK_KEY. If any key name changes, also update
//   the corresponding getters/setters and the plan-reset logic in _dailyRenderPlan.
// VERIFY: Open /daily/, switch reading plan via the select — passages update and
//   the selection persists after a hard reload.
export function initDailyPage() {
  var planSelect  = document.getElementById('daily-plan-select');
  if (!planSelect) return;

  var greetingEl = document.getElementById('daily-greeting');
  var dateEl     = document.getElementById('daily-date');
  var now        = new Date();
  var period     = _dailyPeriod();
  var days       = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  var months     = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  if (greetingEl) {
    var hour = now.getHours();
    var salutation = hour < 12 ? 'Good morning' : hour < 17 ? 'Good afternoon' : 'Good evening';
    greetingEl.textContent = salutation;
  }
  if (dateEl) {
    dateEl.textContent = days[now.getDay()] + ' • ' + months[now.getMonth()] + ' ' + now.getDate() + ', ' + now.getFullYear();
  }

  var savedPlan = localStorage.getItem(DAILY_PLAN_KEY) || 'bible-in-a-year';
  if (_CATECHISM_PLAN_IDS.indexOf(savedPlan) !== -1) {
    savedPlan = 'bible-in-a-year';
    localStorage.setItem(DAILY_PLAN_KEY, savedPlan);
  }
  DAILY_PLAN_META.forEach(function (pm) {
    var opt = document.createElement('option');
    opt.value = pm.id;
    opt.textContent = pm.title;
    if (pm.id === savedPlan) opt.selected = true;
    planSelect.appendChild(opt);
  });

  // HP-D: devot source chips
  var defaultDevot = period === 'morning' ? 'spurgeon-morning' : 'spurgeon-evening';
  var savedDevot = localStorage.getItem(DAILY_DEVOT_KEY) || defaultDevot;
  var devotChips = document.querySelectorAll('.daily-devot-chip');
  devotChips.forEach(function (chip) {
    if (chip.dataset.src === savedDevot) chip.classList.add('daily-devot-chip--active');
    chip.addEventListener('click', function () {
      devotChips.forEach(function (c) { c.classList.remove('daily-devot-chip--active'); });
      chip.classList.add('daily-devot-chip--active');
      localStorage.setItem(DAILY_DEVOT_KEY, chip.dataset.src);
      _dailyRenderDevotional(chip.dataset.src, period);
    });
  });

  planSelect.addEventListener('change', function () {
    var pid = planSelect.value;
    localStorage.setItem(DAILY_PLAN_KEY, pid);
    _dailyRenderPlan(pid);
  });

  var datepicker = document.getElementById('daily-plan-datepicker');
  var dateInput  = document.getElementById('daily-start-date');
  if (dateInput) {
    dateInput.addEventListener('change', function () {
      var pid = planSelect.value;
      if (dateInput.value) {
        localStorage.setItem('bsw_daily_start_' + pid, dateInput.value);
      }
      _dailyRenderPlan(pid);
    });
  }

  _dailyRenderPlan(savedPlan);
  _dailyRenderVOTD();
  _dailyRenderDevotional(savedDevot, period);
  _dailySetupNotifications(period);
  initHistoryWidget();
}

// INTENT: Fetch today's passages for planId and render them into #daily-plan-content,
//   computing today's day number from the plan start date in localStorage. Also
//   wires the "Mark as read" button which updates bsw_plans and re-renders to
//   refresh the streak badge.
function _dailyRenderPlan(planId) {
  var contentEl  = document.getElementById('daily-plan-content');
  var datepicker = document.getElementById('daily-plan-datepicker');
  var dateInput  = document.getElementById('daily-start-date');
  if (!contentEl) return;

  var isAuto = DAILY_AUTO_PLANS.indexOf(planId) !== -1;
  if (datepicker) {
    if (isAuto) datepicker.setAttribute('hidden', '');
    else        datepicker.removeAttribute('hidden');
  }

  var startDateStr = isAuto ? null : (localStorage.getItem('bsw_daily_start_' + planId) || '');
  if (dateInput) {
    dateInput.value = startDateStr || '';
    if (!isAuto && !startDateStr) {
      var today = new Date();
      var yyyy  = today.getFullYear();
      var mm    = ('0' + (today.getMonth() + 1)).slice(-2);
      var dd    = ('0' + today.getDate()).slice(-2);
      var todayStr = yyyy + '-' + mm + '-' + dd;
      dateInput.value = todayStr;
      localStorage.setItem('bsw_daily_start_' + planId, todayStr);
      startDateStr = todayStr;
    }
  }

  var dn   = _dailyDayNum(planId, startDateStr);
  var meta = DAILY_PLAN_META.find(function (p) { return p.id === planId; });

  contentEl.innerHTML = '<div class="daily-loading">Loading…</div>';

  fetch(DAILY_PLANS_ROOT + '/' + planId + '.json')
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (plan) {
      var clampedDay = Math.min(Math.max(dn, 1), plan.total_days);
      var dayData    = plan.days[clampedDay - 1];
      if (!dayData) { contentEl.innerHTML = '<p class="daily-plan-empty">No reading for today.</p>'; return; }

      // CHANGE? bsw_plans schema: { [planId]: { completed: { [dayNum]: dateStr } } }
      //   tracker.js:isReadingDone reads this same key to determine daily-discipline status.
      //   bsw_daily_start_{planId} is a per-plan start date written only by this function;
      //   if the key pattern changes, the date picker restore at line ~203 breaks silently.
      var plansStateRaw = {};
      try { plansStateRaw = JSON.parse(localStorage.getItem('bsw_plans') || '{}'); } catch (_) {}
      var completedMap  = (plansStateRaw[planId] && plansStateRaw[planId].completed) || {};
      var completedCount = Object.keys(completedMap).length;
      var pct = plan.type === 'catechism' ? Math.min(100, Math.round((clampedDay / plan.total_days) * 100))
                                           : Math.min(100, Math.round((completedCount / plan.total_days) * 100));
      var expectedPct = Math.round((dn / plan.total_days) * 100);
      var paceStatus = pct > expectedPct + 2 ? 'ahead' : pct < expectedPct - 2 ? 'behind' : 'on-track';
      var finishLabel = '';
      if (isAuto) {
        var endDt = new Date(new Date().getFullYear(), 0, 1);
        endDt.setDate(endDt.getDate() + plan.total_days - 1);
        finishLabel = endDt.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
      } else if (startDateStr) {
        var sDt = new Date(startDateStr + 'T00:00:00');
        var fDt = new Date(sDt.getTime() + (plan.total_days - 1) * 86400000);
        finishLabel = fDt.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' });
      }
      var html = '<div class="daily-plan-progress">' +
        '<div class="daily-plan-progress-bar"><div class="daily-plan-progress-fill" style="width:' + pct + '%"></div></div>' +
        '<span class="daily-plan-progress-text">' + pct + '%' +
        (finishLabel ? ' &nbsp;·&nbsp; Finish: ' + finishLabel : '') +
        ' &nbsp;<span class="daily-plan-pace daily-plan-pace--' + paceStatus + '">' + paceStatus.replace('-', ' ') + '</span></span>' +
        '</div>' +
        '<p class="daily-plan-day">' +
        (plan.type === 'catechism'
          ? dayData.label
          : 'Day ' + clampedDay + ' of ' + plan.total_days +
            (completedCount ? ' &nbsp;·&nbsp; ' + completedCount + ' completed' : '')) +
        '</p>';

      if (plan.type === 'catechism' && dayData.href) {
        if (dayData.questions) {
          html += '<p class="daily-plan-questions">' + escHtml(dayData.questions) + '</p>';
        }
        if (dayData.desc) {
          html += '<p class="daily-plan-desc">' + escHtml(dayData.desc) + '</p>';
        }
        var libHref = _resolve('../../') + dayData.href;
        html += '<a class="daily-read-all" href="' + escHtml(libHref) + '">Read today\'s section &rarr;</a>';
      } else {
        var passages = dayData.passages || [];
        html += '<div class="daily-passages">';
        passages.forEach(function (p) {
          html += '<a class="daily-passage-chip" href="' + escHtml(_dailyPassageUrl(p)) + '">' + escHtml(p) + '</a>';
        });
        html += '</div>';
        if (passages.length > 1) {
          html += '<a class="daily-read-all" href="' + escHtml(_dailyReadAllUrl(passages)) + '">Read all today&rsquo;s sections &rarr;</a>';
        } else if (passages.length === 1) {
          html += '<a class="daily-read-all" href="' + escHtml(_dailyPassageUrl(passages[0])) + '">Read today&rsquo;s passage &rarr;</a>';
        }
        // Mark today done button
        var isDayDone = !!completedMap[clampedDay];
        html += '<button class="daily-mark-done-btn' + (isDayDone ? ' daily-mark-done-btn--done' : '') +
          '" id="daily-mark-done" data-plan="' + escHtml(planId) + '" data-day="' + clampedDay + '"' +
          (isDayDone ? ' disabled' : '') + '>' + (isDayDone ? '✓ Done' : '✓ Mark today as done') + '</button>';
      }

      // Reading streak (from bsw_streak.days — every day the Bible reader was opened)
      var streakData = {};
      try { streakData = JSON.parse(localStorage.getItem(STREAK_KEY) || '{}'); } catch (_) {}
      var streak = _computeStreakFromDays(streakData.days || []);
      html += '<div class="daily-plan-streak">';
      if (streak.current > 0) {
        html += '<span class="daily-plan-streak-flame">🔥</span>' +
          '<span class="daily-plan-streak-num">' + streak.current + '</span>' +
          '<span class="daily-plan-streak-lbl">day streak</span>';
        if (streak.longest > streak.current) {
          html += '<span class="daily-plan-streak-best">Best: ' + streak.longest + '</span>';
        }
      } else {
        html += '<span class="daily-plan-streak-empty">Open the Bible reader to start your streak</span>';
      }
      html += '</div>';

      contentEl.innerHTML = html;
      // Wire mark-done click
      var markBtn = contentEl.querySelector('#daily-mark-done');
      if (markBtn && !markBtn.disabled) {
        markBtn.addEventListener('click', function () {
          try {
            var state = JSON.parse(localStorage.getItem('bsw_plans') || '{}');
            if (!state[planId]) state[planId] = { completed: {} };
            if (!state[planId].completed) state[planId].completed = {};
            state[planId].completed[clampedDay] = new Date().toISOString().slice(0, 10);
            localStorage.setItem('bsw_plans', JSON.stringify(state));
          } catch (_) {}
          markDone('reading');
          markBtn.textContent = '✓ Done';
          markBtn.classList.add('daily-mark-done-btn--done');
          markBtn.disabled = true;
          _dailyRenderPlan(planId); // re-render to update pct + streak
        });
      }
    })
    .catch(function () {
      contentEl.innerHTML = '<p class="daily-plan-empty">Could not load plan data.</p>';
    });
}

// INTENT: Fetch DAILY_VOTD_URL and render a random verse for today using the
//   day-of-year as a stable index so the same verse shows all day regardless of reload.
function _dailyRenderVOTD() {
  var el = document.getElementById('daily-votd-content');
  if (!el) return;
  el.innerHTML = '<div class="daily-loading">Loading…</div>';

  fetch(DAILY_VOTD_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (verses) {
      var doy  = _dailyDayOfYear();
      var ref  = verses[(doy - 1) % verses.length];
      var parsed = parseRef(ref);
      if (!parsed || !parsed.bookId) {
        el.innerHTML = '<p class="daily-plan-empty">Could not load verse.</p>';
        return;
      }
      var version = getVersion();
      return loadBook(version, parsed.bookId).then(function (chapters) {
        var chData = chapters && chapters[String(parsed.ch)];
        var text   = chData && chData[String(parsed.v)];
        if (!text) { el.innerHTML = '<p class="daily-plan-empty">Verse unavailable.</p>'; return; }
        el.innerHTML =
          '<blockquote>' + escHtml(text) + '</blockquote>' +
          '<cite>— <a class="ref" data-ref="' + escHtml(ref) + '">' + escHtml(ref) + '</a>' +
          ' &nbsp;<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(ref)) + '">Read in context &rarr;</a></cite>' +
          '<div class="daily-votd-actions">' +
            '<button class="daily-votd-btn" id="daily-votd-copy">Copy</button>' +
            '<button class="daily-votd-btn" id="daily-votd-mem">' + (_memHas(ref) ? '⭐ Memorizing' : '☆ Memorize') + '</button>' +
            '<button class="daily-votd-btn" id="daily-votd-share">Share image</button>' +
          '</div>';
        wireRefLinks(el);
        // HP-F: wire action buttons
        var copyBtn = el.querySelector('#daily-votd-copy');
        if (copyBtn) {
          copyBtn.addEventListener('click', function () {
            navigator.clipboard.writeText(text + ' — ' + ref).then(function () {
              copyBtn.textContent = 'Copied ✓';
              setTimeout(function () { copyBtn.textContent = 'Copy'; }, 2000);
            }).catch(function () {});
          });
        }
        var memBtn = el.querySelector('#daily-votd-mem');
        if (memBtn) {
          memBtn.addEventListener('click', function () {
            if (_memHas(ref)) {
              // already memorizing — no toggle out from here, just confirm
              memBtn.textContent = '⭐ Memorizing';
            } else {
              _memAdd(ref);
              memBtn.textContent = '⭐ Memorizing';
            }
          });
        }
        var shareBtn = el.querySelector('#daily-votd-share');
        if (shareBtn) {
          shareBtn.addEventListener('click', function () {
            _shareVerseAsImage(text, ref, version);
          });
        }
      });
    })
    .catch(function () {
      el.innerHTML = '<p class="daily-plan-empty">Could not load verse of the day.</p>';
    });
}

// INTENT: Fetch the selected devotional source (DAILY_DEVOT_KEY) for the current
//   period (morning/evening) and render it into #daily-devot-content; wires the
//   source-picker dropdown so the user can switch devotional without reloading.
function _dailyRenderDevotional(source, period) {
  var titleEl = document.getElementById('daily-devot-title');
  var bodyEl  = document.getElementById('daily-devot-content');
  if (!bodyEl) return;

  var periodLabel = period === 'morning' ? 'Morning' : 'Evening';
  if (titleEl) {
    titleEl.innerHTML = periodLabel + ' Devotional <span class="daily-period-badge">' +
      (period === 'morning' ? '🌅' : '🌙') + ' ' + periodLabel + '</span>';
  }
  bodyEl.innerHTML = '<div class="daily-loading">Loading…</div>';

  var now       = new Date();
  var dayOfYear = _dailyDayOfYear();
  var dom       = now.getDate();
  var version   = getVersion();

  if (source === 'daily-psalms') {
    var psalmNumMorning = ((dayOfYear - 1) % 150) + 1;
    var psalmNumEvening = ((dayOfYear - 1 + 75) % 150) + 1;
    var psalmNum = period === 'morning' ? psalmNumMorning : psalmNumEvening;
    var refStr   = 'Psalms ' + psalmNum;
    loadBook(version, 'psalms').then(function (chapters) {
      var chData = chapters && chapters[String(psalmNum)];
      if (!chData) { bodyEl.innerHTML = '<p class="daily-plan-empty">Psalm unavailable.</p>'; return; }
      var verses  = Object.keys(chData).sort(function (a, b) { return +a - +b; });
      var preview = verses.slice(0, 6).map(function (v) { return chData[v]; }).join(' ');
      if (verses.length > 6) preview += ' …';
      bodyEl.innerHTML =
        '<p class="daily-devot-ref">Psalm ' + psalmNum + '</p>' +
        '<p class="daily-devot-text">' + escHtml(preview) + '</p>' +
        '<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(refStr)) + '">Read all of Psalm ' + psalmNum + ' →</a>';
    }).catch(function () {
      bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load Psalms.</p>';
    });
    return;
  }

  if (source === 'proverbs-month') {
    var ch = Math.min(dom, 31);
    if (period === 'evening') {
      var psNum = ((dayOfYear - 1) % 150) + 1;
      loadBook(version, 'psalms').then(function (chapters) {
        var chData = chapters && chapters[String(psNum)];
        if (!chData) { bodyEl.innerHTML = '<p class="daily-plan-empty">Psalm unavailable.</p>'; return; }
        var verses  = Object.keys(chData).sort(function (a, b) { return +a - +b; });
        var preview = verses.slice(0, 6).map(function (v) { return chData[v]; }).join(' ');
        if (verses.length > 6) preview += ' …';
        bodyEl.innerHTML =
          '<p class="daily-devot-ref">Psalm ' + psNum + ' (evening reflection)</p>' +
          '<p class="daily-devot-text">' + escHtml(preview) + '</p>' +
          '<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent('Psalms ' + psNum)) + '">Read all of Psalm ' + psNum + ' →</a>';
      }).catch(function () { bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load.</p>'; });
      return;
    }
    loadBook(version, 'proverbs').then(function (chapters) {
      var chData = chapters && chapters[String(ch)];
      if (!chData) { bodyEl.innerHTML = '<p class="daily-plan-empty">Proverbs unavailable.</p>'; return; }
      var verses  = Object.keys(chData).sort(function (a, b) { return +a - +b; });
      var preview = verses.slice(0, 6).map(function (v) { return chData[v]; }).join(' ');
      if (verses.length > 6) preview += ' …';
      bodyEl.innerHTML =
        '<p class="daily-devot-ref">Proverbs ' + ch + '</p>' +
        '<p class="daily-devot-text">' + escHtml(preview) + '</p>' +
        '<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent('Proverbs ' + ch)) + '">Read all of Proverbs ' + ch + ' →</a>';
    }).catch(function () {
      bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load Proverbs.</p>';
    });
    return;
  }

  if (source === 'nt-daily') {
    var NT_BOOKS_CHRON = [
      ['matthew',28],['mark',16],['luke',24],['john',21],['acts',28],
      ['james',5],['galatians',6],['1thessalonians',5],['2thessalonians',3],
      ['1corinthians',16],['2corinthians',13],['romans',16],
      ['philippians',4],['philemon',1],['colossians',4],['ephesians',6],
      ['1timothy',6],['titus',3],['2timothy',4],
      ['hebrews',13],['1peter',5],['2peter',3],
      ['1john',5],['2john',1],['3john',1],['jude',1],['revelation',22]
    ];
    var totalNT = NT_BOOKS_CHRON.reduce(function (s, b) { return s + b[1]; }, 0);
    var ntOffset = period === 'evening' ? Math.floor(totalNT / 2) : 0;
    var ntIdx    = ((dayOfYear - 1 + ntOffset) % totalNT);
    var cumul = 0;
    var ntBook = null, ntCh = 1;
    for (var i = 0; i < NT_BOOKS_CHRON.length; i++) {
      var info = NT_BOOKS_CHRON[i];
      if (ntIdx < cumul + info[1]) { ntBook = info[0]; ntCh = ntIdx - cumul + 1; break; }
      cumul += info[1];
    }
    if (!ntBook) { bodyEl.innerHTML = '<p class="daily-plan-empty">Could not determine passage.</p>'; return; }
    loadBook(version, ntBook).then(function (chapters) {
      var chData = chapters && chapters[String(ntCh)];
      if (!chData) { bodyEl.innerHTML = '<p class="daily-plan-empty">Chapter unavailable.</p>'; return; }
      var bkName = metaBooks ? (metaBooks.find(function (b) { return b.id === ntBook; }) || {}).name || ntBook : ntBook;
      var verses  = Object.keys(chData).sort(function (a, b) { return +a - +b; });
      var preview = verses.slice(0, 6).map(function (v) { return chData[v]; }).join(' ');
      if (verses.length > 6) preview += ' …';
      var refLink = bkName + ' ' + ntCh;
      bodyEl.innerHTML =
        '<p class="daily-devot-ref">' + escHtml(refLink) + '</p>' +
        '<p class="daily-devot-text">' + escHtml(preview) + '</p>' +
        '<a class="daily-devot-link" href="' + escHtml(DAILY_CALENDAR_BASE + '?ref=' + encodeURIComponent(refLink)) + '">Read full chapter →</a>';
    }).catch(function () { bodyEl.innerHTML = '<p class="daily-plan-empty">Could not load.</p>'; });
    return;
  }

  // File-backed devotionals (Spurgeon, Winslow, …) and the "variety" rotation all
  // share one JSON shape, so they render through the same path. Variety resolves
  // to a per-day author for the current slot before rendering.
  if (source === 'variety' || DAILY_DEVOT_SOURCES[source]) {
    var mm = String(now.getMonth() + 1).padStart(2, '0');
    var dd = String(now.getDate()).padStart(2, '0');
    var dateKey = mm + '-' + dd;

    var resolver = (source === 'variety')
      ? _dailyResolveVariety(period, dateKey, dayOfYear)
      : _dailyFetchDevotEntry(source, dateKey);

    resolver.then(function (res) {
      if (!res) {
        bodyEl.innerHTML = '<p class="daily-plan-empty">No devotional for today.</p>';
        return;
      }
      _dailyRenderDevotEntry(res, period);
    });
    return;
  }

  bodyEl.innerHTML = '<p class="daily-plan-empty">Select a devotional source above.</p>';
}

// Fetch one author's entry for dateKey; resolves to {slug, meta, entry} or null
// (null when the file is missing or has no entry for that day — e.g. a gap date).
function _dailyFetchDevotEntry(slug, dateKey) {
  var meta = DAILY_DEVOT_SOURCES[slug];
  if (!meta) return Promise.resolve(null);
  return fetch(DAILY_DEVOT_BASE + '/' + meta.file)
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (data) {
      if (!data || !data[dateKey]) return null;
      return { slug: slug, meta: meta, entry: data[dateKey] };
    })
    .catch(function () { return null; });
}

// Pick the day's author for a slot, walking the rotation (wrapping) until one has
// an entry for today — so an author whose edition omits a date is skipped, not blank.
function _dailyResolveVariety(period, dateKey, dayOfYear) {
  var pool = DAILY_VARIETY[period] || [];
  if (!pool.length) return Promise.resolve(null);
  // Evening starts one author ahead of morning so the two slots don't coincide.
  var offset = (period === 'evening') ? 1 : 0;
  var start = (dayOfYear - 1 + offset) % pool.length;
  var order = [];
  for (var i = 0; i < pool.length; i++) order.push(pool[(start + i) % pool.length]);
  var idx = 0;
  function tryNext() {
    if (idx >= order.length) return null;
    return _dailyFetchDevotEntry(order[idx++], dateKey).then(function (res) {
      return res || tryNext();
    });
  }
  return Promise.resolve().then(tryNext);
}

// Render a resolved devotional entry ({slug, meta, entry}) with an author byline.
function _dailyRenderDevotEntry(res, period) {
  var titleEl = document.getElementById('daily-devot-title');
  var bodyEl  = document.getElementById('daily-devot-content');
  if (!bodyEl) return;
  var meta = res.meta, entry = res.entry;

  if (titleEl) {
    titleEl.innerHTML = escHtml(meta.author) +
      ' <span class="daily-period-badge">' +
      (period === 'morning' ? '🌅 Morning' : '🌙 Evening') + '</span>';
  }

  var ref = entry.verse_ref || '';
  var refLink = ref
    ? ' &nbsp;<a class="ref" data-ref="' + escHtml(ref) + '">' + escHtml(ref) + '</a>'
    : '';
  var paragraphs = (entry.body || '').split('\n\n').filter(function (p) { return p.trim(); });
  var bodyHtml = paragraphs.map(function (p) {
    return '<p>' + escHtml(p.trim()) + '</p>';
  }).join('');
  bodyEl.innerHTML =
    '<blockquote class="daily-spurgeon-verse">' +
      escHtml(entry.verse_text) +
      '<cite>' + refLink + '</cite>' +
    '</blockquote>' +
    '<div class="daily-spurgeon-body">' + bodyHtml + '</div>' +
    '<p class="daily-devot-attribution">— ' + escHtml(meta.author) +
      ', <em>' + escHtml(meta.work) + '</em></p>';
  wireRefLinks(bodyEl);
}

function _dailySetupNotifications(period) {
  if (localStorage.getItem(DAILY_NOTIF_DISMISSED) === '1') {
    _dailySchedulePeriodSwitch(period);
    return;
  }

  var lastPeriod = localStorage.getItem(DAILY_NOTIF_KEY);
  if (lastPeriod && lastPeriod !== period) {
    if (typeof Notification !== 'undefined' && Notification.permission === 'granted') {
      _dailyFireNotification(period);
    }
  }
  localStorage.setItem(DAILY_NOTIF_KEY, period);

  if (typeof Notification !== 'undefined' && Notification.permission === 'default') {
    _dailyShowNotifBanner();
  }

  _dailySchedulePeriodSwitch(period);
}

function _dailyShowNotifBanner() {
  var page = document.querySelector('.daily-page');
  if (!page) return;
  var banner = document.createElement('div');
  banner.className = 'daily-notif-banner';
  banner.innerHTML =
    '<span>Get notified when your morning & evening devotional changes.</span>' +
    '<button id="daily-notif-allow">Enable notifications</button>' +
    '<button class="daily-notif-dismiss" aria-label="Dismiss">✕</button>';
  page.insertBefore(banner, page.firstChild);
  banner.querySelector('#daily-notif-allow').addEventListener('click', function () {
    Notification.requestPermission().then(function (perm) {
      if (perm === 'granted') _dailyFireNotification(_dailyPeriod());
      banner.remove();
    });
  });
  banner.querySelector('.daily-notif-dismiss').addEventListener('click', function () {
    localStorage.setItem(DAILY_NOTIF_DISMISSED, '1');
    banner.remove();
  });
}

function _dailyFireNotification(period) {
  if (typeof Notification === 'undefined' || Notification.permission !== 'granted') return;
  var title = period === 'morning' ? 'Good morning — Daily devotional ready' : 'Good evening — Evening devotional ready';
  var body  = period === 'morning' ? 'Your morning reading and verse of the day await.' : 'Your evening reflection and devotional are ready.';
  if (navigator.serviceWorker && navigator.serviceWorker.controller) {
    navigator.serviceWorker.ready.then(function (reg) {
      reg.showNotification(title, { body: body, icon: 'favicon.svg', badge: 'favicon.svg' });
    });
  } else {
    new Notification(title, { body: body, icon: 'favicon.svg' });
  }
}

function _dailySchedulePeriodSwitch(currentPeriod) {
  var now    = new Date();
  var target = new Date(now.getFullYear(), now.getMonth(), now.getDate(), currentPeriod === 'morning' ? 12 : 24, 0, 0, 0);
  var ms     = target - now;
  if (ms <= 0) return;
  setTimeout(function () {
    var newPeriod = _dailyPeriod();
    localStorage.setItem(DAILY_NOTIF_KEY, newPeriod);
    if (typeof Notification !== 'undefined' && Notification.permission === 'granted') {
      _dailyFireNotification(newPeriod);
    }
    var devotSrc = localStorage.getItem(DAILY_DEVOT_KEY) || 'daily-psalms';
    _dailyRenderDevotional(devotSrc, newPeriod);
  }, ms);
}

// ── Scripture Memory ──────────────────────────────────────────────────────────
// Storage helpers (schema, SRS scoring, tags, modal button refresh) live in
// mem.js so the verse modal's Memorize button doesn't pull daily.js onto every
// page — see the import at the top of this file. Page-level review state
// (_memTagFilter, _memQueue, …) stays here.
var _memTagFilter = null;

// INTENT: Bootstrap the memorization/flashcard page — reads MEMORY_KEY (via
//   _memGet) for the verse set and MEMORY_MODE_KEY for the current review mode
//   (all | due | tag), then renders the verse list, SRS due-count badge, and
//   mode-toggle buttons.
// CHANGE? Depends on _memGet schema — if per-verse entry shape changes, the
//   rendering logic here (due filtering, tag display) must be updated. Also
//   depends on MEMORY_MODE_KEY; if that key changes, update _memSetMode too.
// VERIFY: Add 2 verses to memory, open /daily/memorize/ — both appear in list;
//   mark one as reviewed and confirm the due count decrements.
export function initMemorizePage() {
  if (!document.getElementById('mem-list')) return;

  var state    = _memGet();
  var dueCount = Object.keys(state).filter(function (r) { return _memIsDue(state[r]); }).length;
  var badge    = document.getElementById('mem-due-badge');
  if (badge) {
    if (dueCount > 0) { badge.textContent = dueCount; badge.removeAttribute('hidden'); }
    else               badge.setAttribute('hidden', '');
  }

  var modeSelect = document.getElementById('mem-mode-select');
  if (modeSelect) {
    modeSelect.value = localStorage.getItem(MEMORY_MODE_KEY) || 'ref-to-text';
    modeSelect.addEventListener('change', function () {
      localStorage.setItem(MEMORY_MODE_KEY, modeSelect.value);
    });
  }

  var tabs        = document.querySelectorAll('.mem-tab');
  var browsePanel = document.getElementById('mem-browse-panel');
  var reviewPanel = document.getElementById('mem-review-panel');
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      var which = tab.getAttribute('data-tab');
      tabs.forEach(function (t) {
        t.classList.toggle('mem-tab--active', t === tab);
        t.setAttribute('aria-selected', t === tab ? 'true' : 'false');
      });
      if (which === 'browse') {
        browsePanel.removeAttribute('hidden');
        reviewPanel.setAttribute('hidden', '');
      } else {
        browsePanel.setAttribute('hidden', '');
        reviewPanel.removeAttribute('hidden');
        _memStartReview();
      }
    });
  });

  var addInput    = document.getElementById('mem-add-input');
  var addBtn      = document.getElementById('mem-add-btn');
  var addPassInput = document.getElementById('mem-add-passage-input');
  var addPassBtn   = document.getElementById('mem-add-passage-btn');
  var addError    = document.getElementById('mem-add-error');

  function doAdd() {
    var raw    = (addInput && addInput.value.trim()) || '';
    if (!raw) return;
    var parsed = parseRef(raw);
    if (!parsed || !parsed.bookId) {
      if (addError) { addError.textContent = 'Could not parse — try: John 3:16'; addError.removeAttribute('hidden'); }
      return;
    }
    if (!parsed.v) {
      if (addError) { addError.textContent = 'Please enter a specific verse (e.g. John 3:16).'; addError.removeAttribute('hidden'); }
      return;
    }
    if (addError) addError.setAttribute('hidden', '');
    var ref = parsed.bookName + ' ' + parsed.ch + ':' + parsed.v;
    _memAdd(ref);
    if (addInput) addInput.value = '';
    _memRenderList();
  }
  if (addBtn)   addBtn.addEventListener('click', doAdd);
  if (addInput) addInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') doAdd(); });

  // Passage add — accepts a verse range like "John 3:16-18"
  function doAddPassage() {
    var raw = (addPassInput && addPassInput.value.trim()) || '';
    if (!raw) return;
    var parsed = parseRef(raw);
    if (!parsed || !parsed.bookId || !parsed.v) {
      if (addError) { addError.textContent = 'Could not parse passage — try: John 3:16-18'; addError.removeAttribute('hidden'); }
      return;
    }
    if (addError) addError.setAttribute('hidden', '');
    var ref = parsed.display; // e.g. "John 3:16–18"
    // Store as a single memory entry flagged as a passage
    var state = _memGet();
    if (!state[ref]) {
      var today = _memTodayStr();
      state[ref] = {
        addedDate:   today,
        interval:    1,
        nextReview:  today,
        score:       0,
        reps:        0,
        isPassage:   true,
        passStart:   { bookId: parsed.bookId, bookName: parsed.bookName, ch: parsed.ch, v: parsed.v },
        passEnd:     { ch: parsed.endCh, v: parsed.endV },
      };
      _memSet(state);
    }
    if (addPassInput) addPassInput.value = '';
    _memRenderList();
  }
  if (addPassBtn)   addPassBtn.addEventListener('click', doAddPassage);
  if (addPassInput) addPassInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') doAddPassage(); });

  var backBtn = document.getElementById('mem-back-browse');
  if (backBtn) backBtn.addEventListener('click', function () {
    browsePanel.removeAttribute('hidden');
    reviewPanel.setAttribute('hidden', '');
    tabs.forEach(function (t) {
      var isBrowse = t.getAttribute('data-tab') === 'browse';
      t.classList.toggle('mem-tab--active', isBrowse);
      t.setAttribute('aria-selected', isBrowse ? 'true' : 'false');
    });
  });

  var scopeSelect = document.getElementById('mem-scope-select');
  function _memRefreshScopeSelect() {
    if (!scopeSelect) return;
    var tags = _memAllTags();
    var cur  = scopeSelect.value;
    scopeSelect.innerHTML = '<option value="">All</option>' +
      tags.map(function (t) {
        return '<option value="' + escHtml(t) + '">' + escHtml(t) + '</option>';
      }).join('');
    if (cur && tags.indexOf(cur) !== -1) scopeSelect.value = cur;
  }
  _memRefreshScopeSelect();
  if (scopeSelect) {
    scopeSelect.addEventListener('change', function () {
      _memTagFilter = this.value || null;
      _memRenderList();
    });
  }

  var ankiBtn = document.getElementById('mem-anki-btn');
  if (ankiBtn) ankiBtn.addEventListener('click', _memAnkiExport);

  _memRenderList();

  // Keyboard shortcuts during review — skip when focus is in a text input
  document.addEventListener('keydown', function (e) {
    if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT')) return;
    if (!reviewPanel || reviewPanel.hasAttribute('hidden')) return;

    var showBtn  = document.getElementById('mem-show-answer');
    var actsEl   = document.getElementById('mem-card-actions');
    var rateMap  = { '1': 0, '2': 1, '3': 2, '4': 3 }; // key → score

    // Space / Enter flips the card (show answer)
    if ((e.key === ' ' || e.key === 'Enter') && showBtn && !showBtn.hasAttribute('hidden')) {
      e.preventDefault();
      showBtn.click();
      return;
    }
    // 1–4 trigger rating buttons once the answer is visible
    if (rateMap[e.key] !== undefined && actsEl && !actsEl.hasAttribute('hidden')) {
      e.preventDefault();
      var btn = actsEl.querySelector('[data-score="' + rateMap[e.key] + '"]');
      if (btn) btn.click();
    }
  });
}

function _memRenderList() {
  var listEl   = document.getElementById('mem-list');
  var emptyEl  = document.getElementById('mem-empty');
  var footerEl = document.getElementById('mem-list-footer');
  var filterEl = document.getElementById('mem-tag-filter-row');
  if (!listEl) return;
  var state = _memGet();
  var allRefs = Object.keys(state);

  var allTags = _memAllTags();
  if (filterEl) {
    if (allTags.length) {
      filterEl.innerHTML = '';
      var tagOptions = [''].concat(allTags);
      tagOptions.forEach(function (t) {
        var chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'mem-tag-filter-chip' + ((_memTagFilter === (t || null)) ? ' mem-tag-filter-chip--active' : '');
        chip.textContent = t || 'All';
        chip.addEventListener('click', function () {
          _memTagFilter = t || null;
          var scopeSelect = document.getElementById('mem-scope-select');
          if (scopeSelect) scopeSelect.value = _memTagFilter || '';
          _memRenderList();
        });
        filterEl.appendChild(chip);
      });
      filterEl.removeAttribute('hidden');
    } else {
      filterEl.innerHTML = '';
      filterEl.setAttribute('hidden', '');
    }
  }

  var refs = _memTagFilter
    ? allRefs.filter(function (r) {
        return (state[r].tags || []).indexOf(_memTagFilter) !== -1;
      })
    : allRefs;

  if (!allRefs.length) {
    listEl.innerHTML = '';
    if (emptyEl)  emptyEl.removeAttribute('hidden');
    if (footerEl) footerEl.setAttribute('hidden', '');
    return;
  }
  if (emptyEl)  emptyEl.setAttribute('hidden', '');
  if (footerEl) footerEl.removeAttribute('hidden');

  refs.sort(function (a, b) {
    var da = state[a].nextReview, db = state[b].nextReview;
    return da < db ? -1 : da > db ? 1 : 0;
  });
  listEl.innerHTML = '';
  refs.forEach(function (ref) {
    var entry = state[ref];
    var due   = _memIsDue(entry);
    var days  = _memDaysUntil(entry.nextReview);
    var item  = document.createElement('div');
    item.className = 'mem-item' + (due ? ' mem-item--due' : '');

    var refEl = document.createElement('span');
    refEl.className = 'mem-item__ref';
    refEl.textContent = ref;

    var statusEl = document.createElement('span');
    statusEl.className = 'mem-item__status' + (due ? ' mem-item__status--due' : '');
    statusEl.textContent = due ? 'Due today' : 'In ' + days + ' day' + (days === 1 ? '' : 's');

    var btns = document.createElement('div');
    btns.className = 'mem-item__btns';
    var reviewBtn = document.createElement('button');
    reviewBtn.className = 'mem-item__review-btn';
    reviewBtn.textContent = 'Review';
    (function (r) { reviewBtn.addEventListener('click', function () { _memReviewSingle(r); }); }(ref));
    var removeBtn = document.createElement('button');
    removeBtn.className = 'mem-item__remove-btn';
    removeBtn.textContent = '✕';
    removeBtn.title = 'Remove from memory list';
    (function (r) {
      removeBtn.addEventListener('click', function () { _memRemove(r); _memRenderList(); });
    }(ref));
    btns.appendChild(reviewBtn);
    btns.appendChild(removeBtn);

    var tagArea = document.createElement('div');
    tagArea.className = 'mem-item__tags';
    (entry.tags || []).forEach(function (tag) {
      var chip = document.createElement('span');
      chip.className = 'mem-tag-chip';
      chip.innerHTML = escHtml(tag) +
        '<button class="mem-tag-chip__rm" type="button" aria-label="Remove tag ' + escHtml(tag) + '">×</button>';
      (function (r, t) {
        chip.querySelector('.mem-tag-chip__rm').addEventListener('click', function () {
          _memTagRemove(r, t);
          _memRenderList();
        });
      }(ref, tag));
      tagArea.appendChild(chip);
    });

    var addTagInput = document.createElement('input');
    addTagInput.type = 'text';
    addTagInput.placeholder = '+ tag';
    addTagInput.className = 'mem-tag-add-input';
    addTagInput.setAttribute('aria-label', 'Add tag to ' + ref);
    (function (r, inp) {
      inp.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' && inp.value.trim()) {
          _memTagAdd(r, inp.value);
          inp.value = '';
          _memRenderList();
        }
      });
      inp.addEventListener('blur', function () {
        if (inp.value.trim()) { _memTagAdd(r, inp.value); inp.value = ''; _memRenderList(); }
      });
    }(ref, addTagInput));
    tagArea.appendChild(addTagInput);

    var topRow = document.createElement('div');
    topRow.className = 'mem-item__top';
    topRow.appendChild(refEl);
    topRow.appendChild(statusEl);
    topRow.appendChild(btns);
    item.appendChild(topRow);
    item.appendChild(tagArea);
    listEl.appendChild(item);
  });

  var dueCount = allRefs.filter(function (r) { return _memIsDue(state[r]); }).length;
  var badge = document.getElementById('mem-due-badge');
  if (badge) {
    if (dueCount > 0) { badge.textContent = dueCount; badge.removeAttribute('hidden'); }
    else               badge.setAttribute('hidden', '');
  }
}

function _memAnkiExport() {
  var state   = _memGet();
  var version = getVersion();
  var refs    = Object.keys(state);
  if (_memTagFilter) {
    refs = refs.filter(function (r) {
      return (state[r].tags || []).indexOf(_memTagFilter) !== -1;
    });
  }
  if (!refs.length) {
    alert('No verses to export.');
    return;
  }

  var byBook = Object.create(null);
  refs.forEach(function (ref) {
    var parsed = parseRef(ref);
    if (!parsed || !parsed.bookId) return;
    if (!byBook[parsed.bookId]) byBook[parsed.bookId] = [];
    byBook[parsed.bookId].push({ ref: ref, parsed: parsed });
  });

  var bookIds = Object.keys(byBook);
  var rows    = [];

  Promise.all(bookIds.map(function (bookId) {
    return loadBook(version, bookId).then(function (chapters) {
      byBook[bookId].forEach(function (item) {
        var p    = item.parsed;
        var text = chapters && chapters[String(p.ch)] && chapters[String(p.ch)][String(p.v)];
        if (text) rows.push(item.ref + '\t' + text.replace(/\t|\n/g, ' '));
      });
    }).catch(function () {});
  })).then(function () {
    if (!rows.length) { alert('Could not fetch verse text. Try again while online.'); return; }
    rows.sort();
    var content = '#separator:Tab\n#html:false\n#notetype:Basic\n' + rows.join('\n');
    var blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    var url  = URL.createObjectURL(blob);
    var a    = document.createElement('a');
    a.href   = url;
    a.download = 'bible-memory' + (_memTagFilter ? '-' + _memTagFilter : '') + '.txt';
    a.click();
    setTimeout(function () { URL.revokeObjectURL(url); }, 5000);
  });
}

var _memQueue    = [];
var _memQueueIdx = 0;

function _memStartReview() {
  var state = _memGet();
  _memQueue    = Object.keys(state).filter(function (r) {
    if (!_memIsDue(state[r])) return false;
    if (_memTagFilter && (state[r].tags || []).indexOf(_memTagFilter) === -1) return false;
    return true;
  });
  _memQueueIdx = 0;
  _memShowReviewCard();
}

function _memReviewSingle(ref) {
  _memQueue    = [ref];
  _memQueueIdx = 0;
  var browsePanel = document.getElementById('mem-browse-panel');
  var reviewPanel = document.getElementById('mem-review-panel');
  if (browsePanel) browsePanel.setAttribute('hidden', '');
  if (reviewPanel) reviewPanel.removeAttribute('hidden');
  document.querySelectorAll('.mem-tab').forEach(function (t) {
    var isReview = t.getAttribute('data-tab') === 'review';
    t.classList.toggle('mem-tab--active', isReview);
    t.setAttribute('aria-selected', isReview ? 'true' : 'false');
  });
  _memShowReviewCard();
}

function _memShowReviewCard() {
  var progressEl = document.getElementById('mem-review-progress');
  var cardEl     = document.getElementById('mem-card');
  var doneEl     = document.getElementById('mem-review-done');
  if (!cardEl) return;
  if (_memQueueIdx >= _memQueue.length) {
    var n = _memQueue.length;
    if (progressEl) progressEl.innerHTML = n > 0
      ? '<span>' + n + ' of ' + n + '</span>' +
        '<div class="mem-progress-bar"><div class="mem-progress-fill" style="width:100%"></div></div>'
      : '';
    cardEl.setAttribute('hidden', '');
    if (doneEl) {
      var pEl = doneEl.querySelector('p');
      if (pEl) pEl.textContent = n === 0
        ? 'All caught up — nothing due right now.'
        : 'Session complete — well done! You reviewed ' + (n === 1 ? '1 verse' : n + ' verses') + '.';
      doneEl.removeAttribute('hidden');
    }
    var badge = document.getElementById('mem-due-badge');
    if (badge) badge.setAttribute('hidden', '');
    return;
  }
  if (doneEl) doneEl.setAttribute('hidden', '');
  cardEl.removeAttribute('hidden');
  var total = _memQueue.length, done = _memQueueIdx;
  if (progressEl) {
    progressEl.innerHTML =
      '<span>' + (done + 1) + ' of ' + total + '</span>' +
      '<div class="mem-progress-bar"><div class="mem-progress-fill" style="width:' +
      Math.round(done / total * 100) + '%"></div></div>';
  }
  var ref     = _memQueue[_memQueueIdx];
  var mode    = localStorage.getItem(MEMORY_MODE_KEY) || 'ref-to-text';
  var frontEl = document.getElementById('mem-card-front');
  var backEl  = document.getElementById('mem-card-back');
  var actsEl  = document.getElementById('mem-card-actions');
  if (!frontEl) return;
  backEl.setAttribute('hidden', '');
  actsEl.setAttribute('hidden', '');
  frontEl.removeAttribute('hidden');

  if (mode === 'ref-to-text') {
    frontEl.innerHTML =
      '<p class="mem-card__label">Reference</p>' +
      '<p class="mem-card__ref">' + escHtml(ref) + '</p>' +
      '<p class="mem-card__hint">Recall the verse text, then reveal.</p>' +
      '<button class="mem-show-btn" id="mem-show-answer">Show Answer</button>';
    _memWireShowBtn(ref, mode, null);
  } else {
    frontEl.innerHTML = '<p class="mem-card__hint" style="font-size:.85rem">Loading…</p>';
    var parsed = parseRef(ref);
    if (parsed && parsed.bookId) {
      loadBook(getVersion(), parsed.bookId).then(function (chs) {
        var text = chs && chs[String(parsed.ch)] && chs[String(parsed.ch)][String(parsed.v)];
        frontEl.innerHTML =
          '<p class="mem-card__label">Verse Text</p>' +
          '<p class="mem-card__verse-text">&ldquo;' + escHtml(text || ref) + '&rdquo;</p>' +
          '<p class="mem-card__hint">Recall the reference, then reveal.</p>' +
          '<button class="mem-show-btn" id="mem-show-answer">Show Answer</button>';
        _memWireShowBtn(ref, mode, text);
      }).catch(function () {
        frontEl.innerHTML = '<p class="mem-card__ref">' + escHtml(ref) + '</p>' +
          '<button class="mem-show-btn" id="mem-show-answer">Show Answer</button>';
        _memWireShowBtn(ref, mode, null);
      });
    }
  }
}

function _memLoadPassageText(entry) {
  // Returns Promise<string> — all verses in a passage entry concatenated.
  var ps = entry.passStart, pe = entry.passEnd;
  return loadBook(getVersion(), ps.bookId).then(function (chs) {
    var lines = [];
    if (!chs) return '(text unavailable)';
    var ch = ps.ch, endCh = pe.ch, endV = pe.v;
    for (var c = ch; c <= endCh; c++) {
      var chObj = chs[String(c)] || {};
      var startV = (c === ch) ? ps.v : 1;
      var stopV  = (c === endCh) ? endV : 999;
      for (var v = startV; v <= stopV; v++) {
        if (!chObj[String(v)]) break;
        lines.push(escHtml(String(v)) + ' ' + escHtml(chObj[String(v)]));
      }
    }
    return lines.join(' ');
  });
}

function _memWireShowBtn(ref, mode, cachedText) {
  var showBtn = document.getElementById('mem-show-answer');
  if (!showBtn) return;
  var entry = _memGet()[ref];
  var isPassage = !!(entry && entry.isPassage);

  showBtn.addEventListener('click', function () {
    var frontEl = document.getElementById('mem-card-front');
    var backEl  = document.getElementById('mem-card-back');
    var actsEl  = document.getElementById('mem-card-actions');

    function renderAnswer(text) {
      if (mode === 'ref-to-text' || isPassage) {
        backEl.innerHTML =
          '<p class="mem-card__verse-text" style="text-align:left;line-height:1.7">' +
          (isPassage ? text : '&ldquo;' + escHtml(text || '(verse unavailable)') + '&rdquo;') +
          '</p>' +
          '<p class="mem-card__verse-ref">' + escHtml(ref) + '</p>';
      } else {
        backEl.innerHTML =
          '<p class="mem-card__label">Reference</p><p class="mem-card__ref">' + escHtml(ref) + '</p>';
      }
      if (frontEl) frontEl.setAttribute('hidden', '');
      backEl.removeAttribute('hidden');
      actsEl.removeAttribute('hidden');
      _memWireRatingBtns(ref);
    }

    if (isPassage && entry) {
      backEl.innerHTML = '<p class="mem-card__hint">Loading passage…</p>';
      frontEl.setAttribute('hidden', '');
      _memLoadPassageText(entry).then(renderAnswer).catch(function () { renderAnswer('(unavailable)'); });
      return;
    }
    if (cachedText) { renderAnswer(cachedText); return; }
    var parsed = parseRef(ref);
    if (parsed && parsed.bookId) {
      loadBook(getVersion(), parsed.bookId).then(function (chs) {
        renderAnswer(chs && chs[String(parsed.ch)] && chs[String(parsed.ch)][String(parsed.v)]);
      }).catch(function () { renderAnswer(null); });
    } else { renderAnswer(null); }
  });
}

function _memWireRatingBtns(ref) {
  var actsEl = document.getElementById('mem-card-actions');
  if (!actsEl) return;
  actsEl.querySelectorAll('.mem-rate-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var score = parseInt(btn.getAttribute('data-score'), 10);
      var state = _memGet();
      if (state[ref]) { state[ref] = _memApplyScore(state[ref], score); _memSet(state); }
      _memQueueIdx++;
      _memShowReviewCard();
      _memRenderList();
    }, { once: true });
  });
}

// ── Reading Plans — home widget ───────────────────────────────────────────────
var PLANS_KEY  = 'bsw_plans';
var PLANS_ROOT = _resolve('../../data/plans');

function _plansGetState()   { try { return JSON.parse(localStorage.getItem(PLANS_KEY) || '{}'); } catch (e) { return {}; } }
function _plansDayNum(s) {
  if (!s || !s.startDate) return 1;
  var start = new Date(s.startDate + 'T00:00:00');
  var today = new Date();
  today = new Date(today.getFullYear(), today.getMonth(), today.getDate());
  return Math.floor((today - start) / 86400000) + 1;
}

// INTENT: Render the reading plan progress widget on the studies home page —
//   reads plan state from localStorage via _plansGetState and outputs a compact
//   progress bar + current passage link for the active plan.
// CHANGE? _plansGetState reads bsw_plans from localStorage; if the plans state
//   schema changes, the rendering logic here must be updated in tandem.
export function initPlansHomeWidget() {
  var widget = document.getElementById('home-plans-widget');
  if (!widget) return;

  var state    = _plansGetState();
  var enrolled = Object.keys(state).filter(function (id) { return state[id] && state[id].startDate; });
  if (!enrolled.length) return;

  Promise.all(enrolled.map(function (id) {
    return fetch(PLANS_ROOT + '/' + id + '.json')
      .then(function (r) { return r.ok ? r.json() : null; })
      .catch(function () { return null; });
  })).then(function (plans) {
    var html = '<div class="plans-widget">' +
      '<h2 class="plans-widget__heading">Today\'s Reading</h2>';

    var any = false;
    plans.forEach(function (plan) {
      if (!plan) return;
      var s  = state[plan.id];
      var dn = _plansDayNum(s);
      if (dn < 1 || dn > plan.total_days) {
        html += '<div class="plans-widget__item">' +
          '<span class="plans-widget__title">' + escHtml(plan.title) + '</span> — ' +
          '<span class="plans-widget__done">Complete!</span></div>';
        any = true;
        return;
      }
      var day  = plan.days[dn - 1];
      var comp = s.completed && s.completed[dn];
      html += '<div class="plans-widget__item' + (comp ? ' plans-widget__item--done' : '') + '">';
      html += '<span class="plans-widget__title">' + escHtml(plan.title) + '</span>';
      html += ' <span class="plans-widget__meta">Day ' + dn + ' of ' + plan.total_days + '</span>';
      html += '<div class="plans-widget__passages">';
      day.passages.forEach(function (p) {
        html += '<a class="plans-widget__passage" href="' +
          escHtml(READER_URL + '?ref=' + encodeURIComponent(p)) + '">' +
          escHtml(p) + '</a>';
      });
      html += '</div>';
      if (comp) {
        html += '<span class="plans-widget__check">✓ Done</span>';
      } else {
        html += '<a class="plans-widget__goto" href="plans/">Open Reading Plans →</a>';
      }
      html += '</div>';
      any = true;
    });

    html += '</div>';

    if (any) {
      widget.innerHTML = html;
      widget.removeAttribute('hidden');
      var toolsH2 = Array.from(widget.parentNode.querySelectorAll('h2'))
        .find(function (h) { return h.textContent.trim() === 'Tools'; });
      if (toolsH2) toolsH2.parentNode.insertBefore(widget, toolsH2);
    }
  });
}
