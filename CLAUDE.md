# CLAUDE.md — Project Context for AI Assistance

This file is read by Claude Code and Claude AI assistants to understand the
project conventions, goals, and constraints.

## Project Purpose

A personal Bible study reference website hosted on GitHub Pages (static HTML/CSS/JS).
No backend, no build system required — pure static files the owner edits in Sublime Text.

## Core Design Principles

1. **No build step** — Plain HTML, CSS, and vanilla JS only. No React, no bundler.
2. **GitHub Pages compatible** — Everything must work as static files from the repo root.
3. **Easy to extend** — The owner will add new topic pages over time; patterns must be consistent.
4. **Scripture-first** — UI should be clean and readable; scripture text is the star.

## Bible Reference Linking Convention

Use `<a class="ref" data-ref="Book Ch:V">display text</a>` throughout all content.
`assets/js/main.js` wires these up at runtime. Default API: Bible Gateway.

```html
<a class="ref" data-ref="John 3:16">John 3:16</a>
<a class="ref" data-ref="Revelation 1:1-3">Revelation 1:1–3</a>
```

## Bible Versions

Supported versions are listed in `data/versions/versions.json`.
The user's preferred default version is stored in `localStorage` key `bsw_version`.

## File Naming Conventions

- HTML files: `lowercase-with-hyphens.html`
- CSS/JS: same pattern, in `assets/css/` and `assets/js/`
- Topic slugs: `topics/<slug>/index.html`
- Data files: JSON, snake_case keys

## Adding a Topic Page

Copy `topics/_template/index.html` and edit:
- `<title>` and `<h1>`
- The `<meta name="description">` tag
- The main content section
- Add a card entry in `topics/index.html`

## Style Guide (CSS)

- CSS custom properties are defined in `assets/css/style.css` under `:root`
- Primary color: `--color-primary`
- Scripture blocks use `<blockquote class="scripture">`
- Key terms use `<span class="term">`

## Known Future Work

- [x] Bible version switcher UI
- [x] In-page cross-reference tooltip (hover a `.ref` to preview verse)
- [x] Search across all topic pages
- [x] Verse highlight / personal notes (localStorage)
- [ ] Mobile navigation improvements

## Code Comments *(required for all new code)*

**Every non-obvious function, algorithm, cache, or cross-module state interaction written or modified by an agent MUST include this comment format:**

```js
// INTENT: [one sentence — what this block does and WHY, not just what it obviously does]
// CHANGE? [what else to update if you modify this code — downstream side-effects]
// VERIFY: [a runtime check to confirm correctness — what to observe in the browser/console]
```

Rules:
- **Required** on: new exported functions, non-trivial algorithms, any code that touches shared/global state, caches, and cross-module couplings (`window.*`, `localStorage.*`).
- Short helpers (< 5 lines, obvious purpose) need only `INTENT` if anything.
- Complex state flows **must** have all three lines.
- `CHANGE?` must name specific variables, file paths, or downstream callers — not vague advice.
- `VERIFY` must describe a browser/console observation, not "run the tests".
- Do **not** add comments that restate what the code obviously does.

**Worked example — `wordcloud.js` spiral placement:**

```js
// INTENT: Archimedean spiral (r = b·θ) places each word by sweeping outward from
//   a seed pixel; b=5 gives ~450px max radius in MAX_ITER steps. The adaptive step
//   TARGET_D / Math.max(r, TARGET_D) keeps arc-distance constant rather than
//   angular-distance, so words pack evenly at all radii.
// CHANGE? If you change SVG_W/SVG_H calculation, the mask cache key must also change
//   (it includes dimensions) or stale masks will be reused after window resize.
// VERIFY: Render the OT (tablets) scope; all words should stay within the arch
//   boundary. No words should appear in the gap between the two tablet halves.
```

---

## What NOT to Do

- Do not introduce a package.json / npm dependency unless explicitly asked
- Do not use a CSS framework (Bootstrap, Tailwind) unless asked
- Do not restructure the directory layout without discussing first
- Do not commit large Bible text JSON dumps — use API calls instead
