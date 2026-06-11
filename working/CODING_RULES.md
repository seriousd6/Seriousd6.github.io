# Coding Rules — Bible Study Website

Concrete, enforceable rules derived from the existing codebase. Every rule here reflects
what the code already does — your additions should be invisible in style.

---

## 1. JavaScript Syntax

**Use `var`, not `let` or `const`.**
Every JS file in this codebase uses `var` for variable declarations. Do not mix in `let`/`const`
— it looks inconsistent and provides no real benefit in the strict-mode ES module context used here.

**Every JS file starts with `'use strict';` on line 1.**
Exception: short inline `<script>` blocks in HTML pages (they don't need it).

**Use named functions, not arrow functions, for event listeners and callbacks.**
Prefer:
```js
btn.addEventListener('click', function () { … });
```
Not:
```js
btn.addEventListener('click', () => { … });
```
Arrow functions appear in some newer code but are not the house style.

**Ternary operators are fine for simple assignments; avoid nested ternaries.**

**Never use `eval`, `with`, or `document.write`.**

---

## 2. Module and Import Rules

**All page-level JS uses ES modules.** Every feature file imports what it needs from `core.js` or
from its direct siblings. Never import from a module two levels away — if two modules both need
something, it belongs in `core.js`.

**Path constants always come from `core.js`.** Never write a fetch URL like:
```js
fetch('../../data/bible/' + version + '/' + book + '.json')   // WRONG
```
Use:
```js
fetch(DATA_ROOT + '/' + version + '/' + book + '.json')        // RIGHT
```
The full list is at the top of `core.js`. If you need a new root, add it there — not inline.

**No circular imports.** `core.js` imports nothing from feature modules. Feature modules import
from `core.js` and `wire.js` only. `app.js` imports from all feature modules but nothing imports
from `app.js`.

**`window.BibleUI` is the only legitimate global.** It is set in `app.js` and exposes a small
API for cross-module calls that can't go through normal imports. Do not add new `window.*` state.
The only existing exception is `window._readerLookupFn` for the reader's in-page navigation.

---

## 3. Comment Requirements (non-negotiable per CLAUDE.md)

Required on: new exported functions, non-trivial algorithms, any code that touches
`localStorage`, any `window.*` or cache variable.

```js
// INTENT: [one sentence — what this block does and WHY, not a restatement of the obvious]
// CHANGE? [specific variables, file paths, or downstream callers to update if you modify this]
// VERIFY: [what to observe in the browser/console to confirm correctness]
```

Short helpers under 5 lines need only `// INTENT:` if anything.
Complex state flows require all three lines.

**`CHANGE?` must name specific things** — variable names, file paths, callers. Not "update related code."
**`VERIFY:` must be observable** — "open verse-study.js and click John 3:16 — the cross-refs panel shows." Not "run the tests."

**Do not comment what the code obviously does.** Name your variables well instead.

---

## 4. CSS Rules

**Only use CSS custom properties for color, never hardcode hex values.**
```css
color: #8a7a6a;            /* WRONG — hardcoded muted color */
color: var(--color-muted); /* RIGHT */
```

**Dark mode is mandatory for any rule that sets a color or background.**
After any new CSS rule that uses `--color-*`, check whether it needs a `[data-theme="dark"]`
override. The dark theme uses `[data-theme="dark"]` attribute on `<body>`.

**One CSS file per feature.** Don't add reader styles to `style.css`. Don't add topic-guide styles
to `reader.css`. The pattern is `assets/css/{feature-name}.css`.

**Use `rem` not `px` for font sizes.** Use `px` only for borders, shadows, and fixed decorative
dimensions.

**CSS class names follow BEM-ish convention** — each feature has a prefix (`reader-`, `vs-`, `wd-`,
`tg-`, `lib-`). Match the existing prefix for the page you're editing.

**`cursor: pointer` belongs on every interactive element** — buttons, links styled as buttons,
clickable cards. The CSS file for each feature should include it.

**Never use `!important`** unless you're overriding a third-party style (which doesn't exist here).

---

## 5. HTML Patterns

**Scripture reference links always use the `.ref` pattern:**
```html
<a class="ref" data-ref="John 3:16">John 3:16</a>
<a class="ref" data-ref="Romans 8:28-39">Romans 8:28–39</a>
```
`wire.js`'s `wireRefLinks()` picks these up automatically. Never use bare text for verse references
in content — they won't get hover tooltips or modal popups.

**Scripture blocks use `<blockquote class="scripture">`:**
```html
<blockquote class="scripture">
  For God so loved the world…
  <cite><a class="ref" data-ref="John 3:16">John 3:16</a></cite>
</blockquote>
```

**Script tag order at end of `<body>`** — always in this exact sequence:
```html
<script src="../../assets/js/main.js"></script>
<script type="module" src="../../assets/js/app.js"></script>
```
`main.js` is synchronous and builds the sidebar (which app.js depends on). Never reverse this.

**Path depth:** Pages two levels deep use `../../` prefix. Pages one level deep use `../`.
Always use relative paths, never absolute paths like `/assets/js/app.js`.

**`<button>` elements must have `type="button"`** unless they're in a form. Prevents accidental
form submission.

---

## 6. State and localStorage

**All localStorage keys use the `bsw_` prefix.** Existing keys:
```
bsw_version       bsw_theme         bsw_sidebar       bsw_notes_v2
bsw_chapter_read  bsw_plans         bsw_lib_progress  bsw_sg_progress
bsw_tracker       bsw_memory        bsw_journal       bsw_gratitude
bsw_reflections   bsw_worship       bsw_history
```
Adding a new key: add it to this list in `working/site-overview.md` and add a comment in the
storage module that explains it.

**Always wrap localStorage calls in try/catch.** Storage can be unavailable in private browsing:
```js
try {
  localStorage.setItem('bsw_something', value);
} catch (e) {}
```

**Read storage functions are in `storage.js`.** Don't call `localStorage` directly for notes,
highlights, or history — use the exported functions (`getNotes`, `saveNote`, etc.).

**`sessionStorage` is acceptable** for single-session flags (like "user dismissed this banner") —
use the same `bsw_` prefix convention.

---

## 7. Network and Fetch

**Every `fetch()` call needs a `.catch()` handler.** Failure is silent — don't throw errors to
the user, just return null / empty data:
```js
fetch(url)
  .then(function (r) { return r.ok ? r.json() : null; })
  .catch(function () { return null; })
  .then(function (data) {
    if (!data) return;  // graceful no-op
    // … use data
  });
```

**Cache fetched data in module-level variables.** Loading the same JSON file twice wastes
bandwidth. Pattern: `var _cache = {}; _cache[key] = data;` — check before fetching.

**No fetch calls inside tight loops or event handlers that fire on every keystroke.**
Debounce search input; load interlinear on demand (not all books at once if possible).

---

## 8. Service Worker

**Bump `APP_CACHE_V` in `sw.js` on every deploy that changes HTML, CSS, or JS.**
The string looks like `'bsw-app-v64'` — increment the number.
Forgetting this means users get stale code from their cache.

**Bump `DATA_CACHE_V` only when JSON data schemas change** — not on every deploy.

**Do not modify the SW cache strategy** (network-first for HTML, cache-first for data/assets)
without understanding the full implications for offline use. This is a high-blast-radius change.

---

## 9. Quick Reference — Common Patterns

### Inject content into a DOM element after a fetch:
```js
element.innerHTML = '';                          // clear first
var frag = document.createDocumentFragment();
// … build DOM nodes …
element.appendChild(frag);
wireRefLinks(element);                           // wire .ref links after any DOM insertion
```

### Add a toggle button to the browse bar (reader):
```js
var btn = document.createElement('button');
btn.className = 'my-feature-btn' + (active ? ' my-feature-btn--on' : '');
btn.setAttribute('aria-pressed', active ? 'true' : 'false');
btn.title = 'Descriptive tooltip';
btn.textContent = 'Label';
var hint = browseBar.querySelector('.reader-browse-hint');
browseBar.insertBefore(btn, hint || null);       // insert before keyboard hint
```

### Register a version-change callback (app.js):
```js
import { onVersionChange } from './core.js';
onVersionChange(function (newVersion) {
  // re-fetch or re-render using the new version
});
```

### CSS dark mode block structure:
```css
.my-component {
  color: var(--color-text);
  background: var(--color-surface);
}
[data-theme="dark"] .my-component {
  /* only override if var(--color-*) doesn't auto-adapt */
}
```

### New topic page checklist:
1. Copy `topics/_template/index.html` → `topics/{slug}/index.html`
2. Set `--tg-accent` and hero modifier class
3. Add to `topics/index.html` (card entry)
4. Add to `data/topics.json` (nav entry)

---

## 10. What Not to Do

- **No `package.json` or npm dependencies** — no build step means no bundler
- **No CSS frameworks** — Tailwind, Bootstrap, etc. are banned
- **No inline event handlers** (`onclick="…"` in HTML) — wire via JS
- **No `console.log` in committed code** — use `console.warn` for real warnings only
- **No restructuring the directory layout** — discuss first
- **No large JSON data commits** — data files come from Python scripts or API; don't hand-write them
- **No hardcoded Bible text** — always fetch from `data/bible/{version}/{book}.json`
- **No changes to `CLAUDE.md`** — it's the project constitution, not a scratchpad
