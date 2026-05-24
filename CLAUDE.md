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

- [ ] Bible version switcher UI
- [ ] In-page cross-reference tooltip (hover a `.ref` to preview verse)
- [ ] Search across all topic pages
- [ ] Verse highlight / personal notes (localStorage)
- [ ] Mobile navigation improvements

## What NOT to Do

- Do not introduce a package.json / npm dependency unless explicitly asked
- Do not use a CSS framework (Bootstrap, Tailwind) unless asked
- Do not restructure the directory layout without discussing first
- Do not commit large Bible text JSON dumps — use API calls instead
