# CLAUDE.md — Kingdom Bible Study

Live PWA at https://kingdombiblestudy.com (GitHub Pages). **Every push to master
deploys production. Do not push without explicit owner approval.** Local commits
are always fine.

## Read first

- [docs/TODO.md](docs/TODO.md) — the canonical task list. Pick work there; update it
  (and [docs/STATUS.md](docs/STATUS.md)) **in the same commit as the work itself**.
- [docs/plans/](docs/plans/) — active plans · [docs/archive/](docs/archive/) — completed records
  (migration, roadmap, audits) · [docs/agents/](docs/agents/) — agent prompts & loop procedures.

## Architecture in 30 seconds

- **Pages**: `src/pages/*.astro` (~86 authored) + build-time content pages
  (biblepedia, library, answers). Layout: `src/layouts/Base.astro`; nav lives in
  `src/components/Sidebar.astro` (edit links THERE, `assets/js/main.js` only wires it).
- **Overlay**: `assets/`, `data/`, `sw.js` live at the repo ROOT. The owner's
  hourly local auto-sync writes `data/` — never move or rename it.
  `tools/root-statics.mjs` serves the overlay in `astro dev`; `deploy.yml`
  copies it into dist. The redirect-stub copy lists in `root-statics.mjs` and
  `deploy.yml` **must stay in sync**.
- **Build**: `npm run build` = `astro build` + `tools/build-assets.mjs`
  (Vite-bundles `assets/js/entries/*`, minifies CSS, stamps `sw.js`
  `APP_CACHE_V` + JS/CSS precache from the emitted bytes — never hand-bump for
  JS/CSS; only the hand-listed HTML/data `SHELL_URLS` entries are manual).
- **Dev**: `npm run dev` → localhost:4321 (raw ESM, no bundling).

## Conventions

- New page with its own JS: thin entry in `assets/js/entries/` +
  `entry="<name>"` on `<Base>`. Resolve data URLs through `core.js` `_resolve()`
  — never `import.meta.url` (breaks inside bundled chunks).
- Design tokens: the `:root` blocks in `assets/css/style.css` — light + two dark
  blocks, keep all three in sync. Current design language: **Daylight**
  (see `/design/` style guide).
- localStorage keys are prefixed `bsw_`.
- Commentary data: `data/commentary/<source>/<book>/<ch>.json`. Synthesis is
  dual-format and **both are live**: `data/synthesis/<book>/<ch>.json` (study
  desk, per-pericope) and `data/synthesis/<book>.json` (OL Synthesis tab,
  8 books) — see `assets/js/ol-data.js` and `assets/js/study-desk.js`.
- Bible refs in HTML: `<a class="ref" data-ref="Romans 8:28">` (wired globally).

## Validation

`python scripts/validate-data.py`, `validate-library-format.py --all`, and
`validate-synthesis.py` guard the data tree; CI (`validate.yml`) runs all three
plus `node --check` over all JS and the full production build on every push/PR.

## Ground rules

- Knowledge is TRACKED. Task lists, plans, prompts, and procedures live in
  `docs/` — never in gitignored scratch dirs. Deploys are an explicit allowlist
  (`deploy.yml`), so tracked docs never ship to the site.
- Autonomous loops (e.g. COW synthesis — see
  [docs/agents/cow-synthesis-loop.md](docs/agents/cow-synthesis-loop.md)) derive
  their progress from the data tree itself, commit per work-unit with the
  documented message format, and must pass the validators before committing.
- Don't commit `dist/`, `node_modules/`; `scratchpad/` and the `working/` raw
  caches stay ignored.
