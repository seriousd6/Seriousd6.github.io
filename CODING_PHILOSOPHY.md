# Coding Philosophy — Bible Study Website

This document describes *how to think* about work on this site — not syntax rules (see `CODING_RULES.md`)
but the engineering mindset that produces good results here specifically.

---

## 1. Scripture is the star

Every UI decision should make the text easier to read and engage with, not harder. The warm
off-white background, Georgia serif, 1.75 line-height, and 860px max-width are deliberate
choices to replicate the feeling of a well-designed book. Chrome exists to serve the text.

When a feature adds visual weight, ask: does this help the user engage with Scripture, or does
it just look impressive? Reduce chrome. Push text forward.

---

## 2. Read before you write

Every file in this codebase has a design embedded in it. Before touching a function, read it
and the two functions above and below it. Understand the data contract, the failure modes,
and the naming conventions that are already present. Your addition should look like it was
always there.

This is especially true for:
- `core.js` — the shared foundation; misuse propagates everywhere
- `storage.js` — the data model; wrong key names or missing migration can corrupt user data
- `app.js` — the wiring layer; adding a callback in the wrong place creates subtle ordering bugs

---

## 3. Trust the platform

This site uses no framework, no transpiler, no bundler. That is a strength, not a limitation.

The Web platform (ES modules, CSS custom properties, `localStorage`, `fetch`, `IntersectionObserver`,
`history.replaceState`) is powerful enough for everything this site needs. If you find yourself
thinking "I wish I had React here," the real answer is usually "I need to structure this function
better."

Don't add abstractions the platform already provides. Don't polyfill things that work in every
modern browser. Don't build state management when `localStorage` + module-level cache variables
are sufficient.

---

## 4. Fail gracefully; never fail visibly

A Bible study session interrupted by a JavaScript error is a worse outcome than a section
that silently doesn't load. Design every network-dependent feature to degrade:

- Missing commentary → section simply doesn't render; no error thrown
- Missing cross-refs → cross-ref panel empty; no crash
- `localStorage` unavailable → features that need storage skip gracefully; the rest of the page works

Never `throw` to the user. Never leave an error string in the UI. A blank panel is better than
a broken one.

---

## 5. One correct way per problem

This codebase has already solved most of its common problems. Inline reference links use
`.ref` + `data-ref`. Module communication uses registered callbacks in `app.js`. Data caching
uses module-level `var` objects. Path resolution uses `_resolve()` from `core.js`.

When you need to solve a problem that resembles one already solved, find where it was solved
before and follow the same pattern exactly. Introducing a second pattern for the same problem
creates maintenance debt that eventually becomes a bug.

---

## 6. Small complete wins beat large partial ones

A session that ships 2 fully working, verified bug fixes is better than a session that touches
10 files and leaves the codebase in an intermediate state. The TODO list is long; the quality
of each shipped item matters more than the count.

Before starting an item, ask: can I finish this in this session? If the answer is no, either
pick a smaller item or scope down the current one and note what's left.

---

## 7. Scope is sacred

An item's Fix checklist is the contract. Work within it. Do not:
- Clean up "while you're in there" (unless it's a genuine correctness issue)
- Refactor a function that's not in the Fix (even if it could be better)
- Add a feature that's adjacent to the one you're implementing
- Improve error handling that's not part of the described fix

The audit dimensions in `working/audit-agent-guide.md` exist specifically to catch issues
that should then be written up as new TODO items — not fixed immediately. Follow that loop.

---

## 8. State lives in one place per concern

**User data** → `localStorage` (via `storage.js` functions, not raw calls)
**UI state that affects rendering** → module-level `var` flags (e.g., `_interlinearOn`)
**Ephemeral per-session state** → `sessionStorage` with `bsw_` prefix
**URL state for deep-linking** → `history.replaceState()` or `location.hash`
**Cross-module coordination** → `app.js` registered callbacks or `window.BibleUI`

When you're not sure where state belongs, ask: should this survive a page refresh? A tab close?
A share to another user? The answer determines which layer it belongs in.

---

## 9. Dark mode is first-class

A site used for personal devotions and Scripture study gets opened at 6am and at 11pm. Dark
mode is not an accessibility checkbox — it's a daily use feature. Every visual component
must work in both light and dark mode before it ships.

The dark mode is implemented via `[data-theme="dark"]` on `<body>`. CSS custom properties
handle most of it automatically, but some components need explicit overrides. Check before
shipping.

---

## 10. Don't break what works

This site has 15+ features, 18 translations, 28+ library documents, commentary for 66 books,
and a daily discipline system — all working without a build step or server. That is a real
achievement, and it is fragile in specific ways:

- Changing `parseRef()` in `core.js` breaks every feature that loads Bible text
- Bumping `APP_CACHE_V` incorrectly breaks offline users until they clear their cache
- Renaming a `localStorage` key without a migration wipes user notes and history
- Removing or reordering script tags in HTML breaks the sidebar

Before any change, ask: what is the blast radius? If it touches `core.js`, `storage.js`,
`sw.js`, or `app.js` — slow down and re-read `CODING_RULES.md` Section 6 and 8.

---

## 11. The user at 6am

When evaluating a UX decision, think of a person opening their phone in early morning for a
quiet hour of reading. They want:
- Fast load, even on slow WiFi
- Familiar layout (no surprise changes to navigation)
- Text that's easy on the eyes
- Features that work without hunting for them
- Their previous place restored automatically

They do not want:
- Popups and banners
- Slow-loading components that block the text
- Navigation that requires multiple taps
- Anything that demands attention before they can read

This mental model should govern every UX choice: buttons, animations, empty states, loading
feedback, and default states.

---

## 12. Verify, don't assume

"It looks right" is not the same as "it works." After every implementation:

1. Trace through the logic from call site to output — every branch
2. Check the error path — what happens when the fetch fails? When the element doesn't exist?
3. Check the dark mode path — does the CSS look right in both themes?
4. Re-read the original Problem description — does your change actually address it?

A missed `.catch()`, a missing `null` check, or a forgotten dark mode rule are the most
common ways a technically correct implementation ships broken. They are also the easiest
things to catch by reading carefully before committing.

---

## 13. The no-build-step contract

The owner edits files directly in Sublime Text and pushes. There is no compile step, no
minification, no linting pipeline. This is a design constraint, not an oversight.

Every time you're tempted to add a `package.json`, a build script, or a preprocessor:
the answer is no. The price of breaking this contract is paid by the person maintaining
the site for the next decade.

If a task genuinely cannot be done without tooling — write a one-off Python script in `scripts/`
that runs locally and produces a static output file. That pattern is already established for
all data generation. Apply it rather than reaching for npm.
