# Kingdom Bible Study

A personal Bible study site — reader, word study, cross-references, devotionals,
disciplines tracking, and a church-history library — hosted on GitHub Pages as a
PWA with full offline support.

## Live Site

> https://kingdombiblestudy.com/

## Architecture (Astro, overhauled July 2026)

Pages are authored as `.astro` files sharing one layout. Data-driven content is
**statically rendered at build time** (4,400+ Biblepedia articles, 143 library
documents) with the client apps enhancing in place; page JavaScript is split
into per-page entries bundled through Vite. `src/pages/` is the single source
of truth for page HTML.

```
├── src/
│   ├── layouts/Base.astro   # Universal shell: head boilerplate, theme bootstrap,
│   │                        #   base CSS, sidebar, footer, main.js + per-page
│   │                        #   entry module (entry prop → assets/js/entries/*)
│   ├── components/Sidebar.astro  # Static site nav (edit nav links HERE;
│   │                        #   assets/js/main.js only wires behavior)
│   └── pages/               # One .astro file per page, mirrors URL structure
│       ├── biblepedia/[slug]/    # 4,418 static articles from data/biblepedia
│       └── library/read/[doc]/   # 143 static documents from data/library
├── assets/                  # css/, js/, fonts/ — SOURCE tree; `astro dev`
│   │                        #   serves it raw (native ESM), the build bundles it
│   ├── js/core-boot.js      # Shared boot: theme, PWA, Bible metadata, modal,
│   │                        #   ref wiring, window.BibleUI. Heavy modules load
│   │                        #   lazily (idle-time dynamic imports)
│   └── js/entries/          # One thin entry per page family; Base.astro's
│                            #   `entry` prop selects it (default "generic")
├── data/                    # Bible text, commentary, library JSON (~50k files);
│                            #   written hourly by the local auto-sync — do not move
├── sw.js                    # Service worker. APP_CACHE_V + the JS/CSS precache
│                            #   list are GENERATED at build (BUILD:ASSETS markers)
│                            #   — no manual version bumps for JS/CSS changes
├── tools/
│   ├── build-assets.mjs     # Post-astro build step: Vite-bundles entries (stable
│   │                        #   entry URLs, hashed minified chunks), externalizes
│   │                        #   core.js/tracker.js (inline scripts import them —
│   │                        #   single module instance), minifies CSS + classic
│   │                        #   scripts, regenerates sw.js into dist/
│   ├── build-search-index.mjs  # Build-time inverted verse-search index (BSB)
│   └── root-statics.mjs     # Dev-server middleware: serves the root static tree
└── .github/workflows/
    ├── validate.yml         # Data integrity + JS syntax + full build (every push)
    └── deploy.yml           # Pages deploy on every push to master
```

**Overlay layout:** the runtime data tree stays at the repo root (the hourly
data auto-sync writes to `data/` — do not move it). `tools/root-statics.mjs`
bridges `astro dev` to the root `assets/`/`data/` dirs; `npm run build` emits
assets + sw.js + PWA statics into `dist/`, and `deploy.yml` adds `data/`, the
`_template` scaffolds, and the verbatim redirect stubs (`devotionals/`,
`plans/`, `word/`, …). The verbatim-file lists in `tools/root-statics.mjs` and
`deploy.yml` must stay in sync.

**Render-then-enhance:** Biblepedia articles (`/biblepedia/<slug>/`) and
library documents (`/library/read/<id>/`) are full static HTML — crawlable
(see `sitemap-index.xml`), instant on first paint, readable without JS. On
load, the same client apps that serve the legacy `?a=`/`?doc=` URLs detect the
path and replace the static DOM with the enriched interactive view. There is
one implementation of each app; static HTML is its build-time snapshot.

## Development

```bash
npm install
npm run dev       # localhost:4321 — pages from src/, statics from repo root (unbundled)
npm run build     # astro build + tools/build-assets.mjs → complete dist/ minus data/
```

Every push to `master` deploys via `.github/workflows/deploy.yml`.

## Adding a page

Create `src/pages/<section>/index.astro` using `Base.astro`:

```astro
---
import Base from '../../layouts/Base.astro';
---
<Base title={"My Page — Kingdom Bible Study"} description={"…"}>
  <main>…</main>
</Base>
```

Extra CSS goes in a `<Fragment slot="head-end">`; inline scripts/styles need
`is:inline`. Use `<a class="ref" data-ref="Romans 8:28">` for hotlinked Bible
references (wired by `assets/js/wire.js`).

If the page needs its own feature module, add a thin entry to
`assets/js/entries/` (import `boot` from `../core-boot.js`, call your init in
the callback) and set `entry="<name>"` on `<Base>`. The Vite build picks up new
entries automatically; keep imports relative and resolve data URLs through
`core.js`'s `_resolve()` (never `import.meta.url` — it breaks inside chunks).

## Validation

`python3 scripts/validate-data.py`, `python3 scripts/validate-library-format.py --all`,
and `python3 scripts/validate-synthesis.py` guard the data tree; CI runs all
three plus `node --check` over all JS (including `assets/js/entries/`) and the
full production build.

## Project docs

Start at [`CLAUDE.md`](CLAUDE.md) (the agent/developer hub). The canonical task
list is [`docs/TODO.md`](docs/TODO.md), live status in
[`docs/STATUS.md`](docs/STATUS.md), active plans in [`docs/plans/`](docs/plans/),
agent prompts and loop procedures in [`docs/agents/`](docs/agents/), and
completed records — including the July 2026 JS→Astro migration
([`docs/archive/OVERHAUL.md`](docs/archive/OVERHAUL.md)) — in
[`docs/archive/`](docs/archive/).
