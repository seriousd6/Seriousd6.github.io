/*
 * reader-audio.js — read-aloud (TTS) of the open reader passage via the Web Speech API.
 *
 * Reads the rendered chapter verse-by-verse, highlighting and auto-scrolling to the
 * current verse, with play / pause / stop and a speed control. No backend, no data —
 * uses the browser's built-in speechSynthesis. Verses are spoken one utterance each
 * (short utterances avoid the Chrome long-utterance cutoff and give clean per-verse
 * progress + highlight tracking).
 *
 * INTENT: Turn passive reading into a hands-free / accessible study + devotional mode.
 * CHANGE? Reads `.reader-verse[data-v]` elements inside #reader-results (skipping compare
 *   cells); if that verse markup changes, update _collectVerses/_verseText. A
 *   MutationObserver on #reader-results stops playback on any re-render (new lookup /
 *   chapter) so audio never desyncs from the visible text.
 * VERIFY: Open /read/, load a chapter, click "🔊 Listen" — it reads aloud, the current
 *   verse highlights and scrolls into view; Pause/Resume/Stop and the speed select work;
 *   navigating to another chapter stops playback.
 */

var _RATE_KEY = 'bsw_reader_tts_rate';
var _synth    = (typeof window !== 'undefined') ? window.speechSynthesis : null;

var _verses   = [];          // ordered .reader-verse elements being read
var _idx      = -1;          // index of the verse currently/last spoken
var _state    = 'stopped';   // 'stopped' | 'playing' | 'paused'
var _btn      = null;
var _barEl    = null;
var _observer = null;

function _rate() {
  var r = parseFloat(localStorage.getItem(_RATE_KEY));
  return (r >= 0.5 && r <= 2) ? r : 1;
}
function _setRate(r) { try { localStorage.setItem(_RATE_KEY, String(r)); } catch (e) {} }

// Clean spoken text for one verse: drop the verse-number sup, xref notes, echo chips,
// and any injected interlinear row, then collapse whitespace.
function _verseText(verse) {
  var clone = verse.cloneNode(true);
  clone.querySelectorAll(
    '.reader-verse__num, .reader-xref-note, .reader-echo-marker, .reader-interlinear-row, sup'
  ).forEach(function (el) { el.remove(); });
  return (clone.textContent || '').replace(/\s+/g, ' ').trim();
}

function _collectVerses() {
  var results = document.getElementById('reader-results');
  if (!results) return [];
  return Array.prototype.slice.call(results.querySelectorAll('.reader-verse[data-v]'))
    .filter(function (v) { return !v.closest('.reader-compare-cell'); });
}

// The first verse not scrolled above the top of the viewport — so "Listen" starts
// reading from where the user is currently looking.
function _firstVisibleIndex() {
  for (var i = 0; i < _verses.length; i++) {
    var r = _verses[i].getBoundingClientRect();
    if (r.bottom > 90) return i;
  }
  return 0;
}

function _highlight(i) {
  _verses.forEach(function (v, j) { v.classList.toggle('reader-verse--reading', j === i); });
  if (_verses[i] && _verses[i].scrollIntoView) {
    _verses[i].scrollIntoView({ block: 'center', behavior: 'smooth' });
  }
}

function _speakFrom(i) {
  if (!_synth) return;
  if (i >= _verses.length) { _stop(); return; }
  _idx = i;
  _highlight(i);
  _updateUi();
  var text = _verseText(_verses[i]);
  if (!text) { _speakFrom(i + 1); return; }
  var u = new SpeechSynthesisUtterance(text);
  u.rate = _rate();
  u.onend   = function () { if (_state === 'playing') _speakFrom(_idx + 1); };
  u.onerror = function () { if (_state === 'playing') _speakFrom(_idx + 1); };
  _synth.speak(u);
}

function _play() {
  _verses = _collectVerses();
  if (!_verses.length) return;
  _state = 'playing';
  _armObserver();
  _updateUi();
  var start = (_idx >= 0 && _idx < _verses.length) ? _idx : _firstVisibleIndex();
  _synth.cancel();
  _speakFrom(start);
}

// Click a verse while reading is active to jump playback there. Capture phase so it
// runs before the verse-text-highlight / number-popup handlers, which it suppresses.
function _onVerseClick(e) {
  if (_state === 'stopped') return;
  if (e.target.closest('.reader-verse__num, a, button, .reader-echo-marker, .reader-xref-note, .reader-audio-bar')) return;
  var verse = e.target.closest('#reader-results .reader-verse[data-v]');
  if (!verse || verse.closest('.reader-compare-cell')) return;
  if (!_verses.length) _verses = _collectVerses();
  var i = _verses.indexOf(verse);
  if (i < 0) return;
  e.preventDefault();
  e.stopPropagation();
  _state = 'playing';
  _armObserver();
  _synth.cancel();
  _speakFrom(i);
}
function _pause()  { if (_synth && _state === 'playing') { _synth.pause();  _state = 'paused';  _updateUi(); } }
function _resume() { if (_synth && _state === 'paused')  { _synth.resume(); _state = 'playing'; _updateUi(); } }
function _stop() {
  if (_synth) _synth.cancel();
  _state = 'stopped'; _idx = -1;
  _verses.forEach(function (v) { v.classList.remove('reader-verse--reading'); });
  _disarmObserver();
  _updateUi();
}
function _toggle() {
  if (_state === 'playing') _pause();
  else if (_state === 'paused') _resume();
  else _play();
}

// Stop playback whenever the passage re-renders, so audio never reads stale/desynced text.
function _armObserver() {
  if (_observer) return;
  var results = document.getElementById('reader-results');
  if (!results) return;
  _observer = new MutationObserver(function () { _stop(); });
  _observer.observe(results, { childList: true });
}
function _disarmObserver() { if (_observer) { _observer.disconnect(); _observer = null; } }

function _updateUi() {
  // While active, verses show a pointer cursor (they're click-to-jump targets).
  document.body.classList.toggle('bsw-reader-audio-active', _state !== 'stopped');
  if (_btn) {
    var playing = _state === 'playing';
    var active  = _state !== 'stopped';
    _btn.setAttribute('aria-pressed', active ? 'true' : 'false');
    _btn.classList.toggle('reader-audio-btn--on', active);
    _btn.textContent = playing ? 'Pause' : (active ? 'Resume' : 'Listen');
  }
  if (_barEl) {
    _barEl.hidden = _state === 'stopped';
    var tb = _barEl.querySelector('[data-act="toggle"]');
    if (tb) tb.textContent = _state === 'playing' ? '⏸' : '▶';
    var st = _barEl.querySelector('.reader-audio-bar__status');
    if (st) st.textContent = (_idx >= 0 && _verses[_idx])
      ? 'verse ' + (_verses[_idx].getAttribute('data-v') || '') : '';
  }
}

function _buildBar() {
  var bar = document.createElement('div');
  bar.className = 'reader-audio-bar';
  bar.hidden = true;
  bar.innerHTML =
    '<button class="reader-audio-bar__btn" data-act="toggle" type="button" aria-label="Play or pause">⏸</button>' +
    '<button class="reader-audio-bar__btn" data-act="stop" type="button" aria-label="Stop reading">⏹</button>' +
    '<label class="reader-audio-bar__rate">Speed ' +
      '<select class="reader-audio-bar__rate-sel" aria-label="Reading speed">' +
        '<option value="0.75">0.75×</option><option value="1">1×</option>' +
        '<option value="1.25">1.25×</option><option value="1.5">1.5×</option><option value="2">2×</option>' +
      '</select></label>' +
    '<span class="reader-audio-bar__status"></span>' +
    '<span class="reader-audio-bar__hint">tap a verse to jump</span>';
  document.body.appendChild(bar);
  var sel = bar.querySelector('.reader-audio-bar__rate-sel');
  sel.value = String(_rate());
  sel.addEventListener('change', function () {
    _setRate(parseFloat(sel.value));
    if (_state === 'playing') { _synth.cancel(); _speakFrom(_idx); }  // apply mid-read
  });
  bar.querySelector('[data-act="toggle"]').addEventListener('click', _toggle);
  bar.querySelector('[data-act="stop"]').addEventListener('click', _stop);
  return bar;
}

export function initReaderAudio() {
  // Graceful: if the browser lacks the Web Speech API, no button is shown.
  if (!_synth || typeof SpeechSynthesisUtterance === 'undefined') return;
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-audio-btn')) return;

  _btn = document.createElement('button');
  _btn.id        = 'reader-audio-btn';
  _btn.className = 'reader-audio-btn';
  _btn.type      = 'button';
  _btn.textContent = 'Listen';
  _btn.title     = 'Read this passage aloud';
  _btn.setAttribute('aria-pressed', 'false');

  // Visible directly in the browse bar (not tucked inside the view popover).
  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(_btn, hint || null);
  _btn.addEventListener('click', _toggle);

  _barEl = _buildBar();
  document.addEventListener('click', _onVerseClick, true);  // click-a-verse-to-jump
  window.addEventListener('beforeunload', _stop);
  _synth.cancel();   // clear any lingering utterance from a prior page
}
