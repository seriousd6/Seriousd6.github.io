# Kingdom Bible Study

A personal Bible study site — reader, word study, cross-references, devotionals,
disciplines tracking, and a church-history library — hosted on GitHub Pages as a
PWA with full offline support.

## Live Site

> https://kingdombiblestudy.com/

## Architecture (Astro, since July 2026)

Pages are authored as `.astro` files sharing one layout; the runtime (JS
modules, CSS, Bible data, service worker) ships verbatim. `src/pages/` is the
single source of truth for page HTML — the legacy root `*.html` pages were
retired after the cutover.

```
├── src/
│   ├── layouts/Base.astro   # Universal shell: head boilerplate, theme bootstrap,
│   │                        #   base CSS, footer, main.js/app.js pair
│   └── pages/               # One .astro file per page, mirrors URL structure
├── assets/                  # css/, js/ (ES modules), fonts/ — served as-is
├── data/                    # Bible text, commentary, library JSON (~50k files);
│   │                        #   written hourly by the local auto-sync — do not move
├── sw.js                    # Service worker (bump APP_CACHE_V on asset changes)
├── tools/
│   ├── root-statics.mjs     # Dev-server middleware: serves the root static tree
│   ├── convert-pages.mjs    # One-time legacy HTML → .astro converter
│   └── diff-pages.mjs       # DOM-diffs dist/ against legacy root HTML
└── .github/workflows/
    ├── validate.yml         # Data integrity + JS syntax + Astro build (every push)
    └── deploy.yml           # Pages deploy — manual until cutover (see file header)
```

**Overlay layout:** the static runtime tree stays at the repo root (the hourly
data auto-sync writes to `data/` — do not move it). `tools/root-statics.mjs`
bridges `astro dev` to the root `assets/`/`data/` dirs; `deploy.yml` copies them
into `dist/` for the Pages deploy. A handful of redirect stubs (`devotionals/`,
`plans/`, `word/`, …) and the `_template` scaffolds are not Astro pages and ship
verbatim — the copy lists live in `tools/root-statics.mjs` and `deploy.yml` and
must stay in sync.

## Development

```bash
npm install
npm run dev       # localhost:4321 — pages from src/, statics from repo root
npm run build     # dist/ (page HTML only; deploy workflow adds the static tree)
```

Every push to `master` deploys via `.github/workflows/deploy.yml`.
(`npm run convert` / `npm run diff` were the one-time migration tooling — kept
for reference; the legacy HTML they operated on is gone.)

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

## Validation

`python3 scripts/validate-data.py` and `python3 scripts/validate-library-format.py --all`
guard the data tree; CI also runs `node --check` over all JS and a full Astro build.
