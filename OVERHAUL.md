# JS → Astro Migration — Overhaul Plan

_Regenerated 2026-07-11 from a fresh read of the repo._

## What "migrated to Astro" really means here

The July-2026 cutover was billed as complete, but it only finished **Phase 1: the
structural shell**. Astro is currently used as an HTML templating layer and nothing
more:

- All 74 pages are `.astro` files sharing `src/layouts/Base.astro` +
  `src/components/Sidebar.astro`.
- `astro.config.mjs` sets `compressHTML: false` and `build.format: 'preserve'`
  **specifically so `dist/` DOM-diffs clean against the retired legacy HTML** — the
  Phase-1 acceptance test. Astro is deliberately producing byte-similar output.
- **Zero** framework islands, `client:*` directives, or `.astro` content components.
- `assets/js` and `assets/css` are **not** in Astro's build pipeline. They live at the
  repo root and are copied verbatim by the `root-statics.mjs` dev middleware and by
  `deploy.yml`. No bundling, tree-shaking, hashing, or code-splitting happens.

The content itself is still a **client-rendered JS app wrapped in an Astro shell**.
Pages ship empty scaffolding `<div id="…">` landmarks, and 40 JS modules (**1.8 MB**
total) inject the actual content at runtime.

### The central problem

`assets/js/app.js` **statically imports 30 of the 40 modules** and is loaded on nearly
every page via `Base.astro` (`appJs` defaults to `true`). It then guards each module's
`init()` behind a `getElementById` check. Net effect: **every page downloads and parses
~1.8 MB of JavaScript to use one module.** For a PWA whose whole value proposition is
offline speed, this is the biggest single regression to fix, and it is entirely
mechanical to unwind.

A pattern for the fix already exists in-repo: `dictionary` and `translation/workshop`
set `appJs={false}` / `mainJs={false}` and supply their own inline `slot="after-scripts"`
module script. That per-page-entry model just needs to become the default.

## Guardrails (invariants every phase must hold)

1. **`data/` is immovable.** ~50k files written hourly by the local auto-sync. Read it,
   never relocate it. Build-time reads (Astro frontmatter `import`/`fs`) are fine.
2. **The site is served from the repo root of a user GitHub Pages site.** Root-absolute
   asset URLs (`/assets/js/...`) must keep resolving.
3. **Keep the copy lists in `tools/root-statics.mjs` and `.github/workflows/deploy.yml`
   in sync** whenever files move into or out of the overlay tree.
4. **`sw.js`**: bump `APP_CACHE_V` on any asset-URL change; reconcile its precache
   manifest when asset paths change (Phase 3+).
5. **Redirect stubs and `_template` scaffolds** ship verbatim — not Astro pages.
6. CI must stay green: `validate.yml` (data validators + `node --check` + `astro build`).

---

## Phase 2 — De-monolith the client runtime  ·  ✅ **DONE 2026-07-11**

**Shipped:** `assets/js/core-boot.js` (shared boot, `boot(pageInit, opts)`) + 15 entry
modules under `assets/js/entries/`; `Base.astro` gained an `entry` prop (default
`generic`); `app.js` deleted; `sw.js` precache updated, `APP_CACHE_V` → v185 (also
fixed pre-existing precache gaps: `synoptic.js`, `biblepedia.js`). Measured transitive
payload: generic pages **1,800 KB → 509 KB (−72 %)**; reader 779 KB; maps 694 KB.
Remaining fat in core-boot is the modal-renderer set (`verse-study`/`daily`/`library`/
`search` + deps) — lazy-loading those on first modal-tab click is the Phase 2.5
follow-up, or falls out naturally in Phase 3/4.

### Phase 2.5 — ✅ **DONE 2026-07-11**

The "modal-renderer set" turned out to be mostly **dead code**: modal.js stored the five
registered tab renderers but never invoked them (tabs are Verse/Notes/Connections;
verse-study.js imports library.js renderers directly). Shipped:

- Dead `registerModal*` bridge removed from modal.js + core-boot; `verse-study.js`
  (+`interlinear.js`) and `library.js` fall out of the eager graph entirely.
- `mem.js` extracted from daily.js (memory-verse localStorage/SRS helpers) so the
  modal's Memorize button no longer drags the 62 KB daily page module everywhere.
- Sidebar Search button + Ctrl+K/`?` hotkeys inlined into core-boot (`buildSearchNav`);
  the 60 KB search engine now loads only on `search/` via its own `entries/search.js`.
- `terms.js`/`places.js` dynamic-imported in their existing idle slots;
  `apocrypha-reader.js` fire-and-forget after `wireRefLinks`; `BibleUI.initOLSection` /
  `autoTagPlacesIn` became lazy wrappers (their callers already tolerate promises).
- `sw.js` → v186 (+`mem.js`, `entries/search.js` precached).

**Eager payload: generic pages 509 → 200 KB** (−89 % vs the original 1,800 KB);
reader 558 KB; maps 385 KB. Verified with a headless-Chromium functional pass: modal
opens via ref click, search returns results, John 3:16 renders, library populates,
Ctrl+K navigates, `window.BibleUI` surface exact.

_Known pre-existing issue (not fixed here):_ the injected sidebar Search **button** has
been dead since the Candlelight static-sidebar commit — its `.version-picker` anchor no
longer exists (the sidebar's 🔍 Explore link covers navigation; Ctrl+K still works).
Decide in Phase 5 whether to re-anchor it next to `#bible-version` or delete the code.

**Goal:** each page loads only the JS it uses. Kill the 1.8 MB-on-every-page tax.

**Approach (low risk, no pipeline change yet):**
- Create thin per-page entry modules under `assets/js/entries/` (e.g. `reader.entry.js`,
  `library.entry.js`, `home.entry.js`) that import only `core.js` + the module(s) that
  page actually needs, then call that page's `init()` directly (drop the `getElementById`
  dispatch — the entry *is* the dispatch).
- Add an `entry` prop to `Base.astro`; when set, emit
  `<script type="module" src="/assets/js/entries/{entry}.js">` instead of the shared
  `app.js`. Default `appJs` stays until every page declares an entry, then retire `app.js`.
- Factor the truly-shared boot (theme, PWA register, storage migrations, version/book
  load, tooltip/modal/ref-wiring, search button) into one `core-boot.js` every entry
  imports, so the modal/version-picker/search still work everywhere.

**Acceptance:**
- Per-page transferred JS drops from ~1.8 MB to that page's real footprint.
- DOM diff vs. current `dist/` unchanged (content still client-rendered, just less code).
- Manual smoke of each page family: reader, verse-study, library, dictionary, biblepedia,
  timeline, maps, daily/plans, memorize, topics, workshop — features intact, no console
  errors, `window.BibleUI.openReader('john',3,16)` still navigates.

**Risk:** low. Pure import-graph surgery; the `window.BibleUI` public surface and
cross-module callback registration in `app.js` must be preserved in `core-boot.js`.

---

## Phase 3 — Bring assets into the Astro/Vite pipeline

**Goal:** let Astro/Vite bundle, tree-shake, code-split, and content-hash the JS/CSS
that Phase 2 split by hand — and retire manual cache-busting (`?v=2`, `APP_CACHE_V`).

**Approach:**
- Move `assets/js` + `assets/css` under `src/` (or import them from `.astro` frontmatter)
  so Vite owns them. Keep `data/`, `sw.js`, fonts, icons in the root overlay.
- Replace hand-written entry `<script>` tags with Astro `<script>`/component imports so
  hashing + splitting are automatic.
- Reconcile `sw.js`: precache the hashed asset URLs Astro emits (generate its manifest at
  build time instead of hand-maintaining it); collapse `APP_CACHE_V` bumping into the
  build hash.
- Trim `root-statics.mjs` / `deploy.yml` copy lists to what still lives at root.

**Acceptance:** identical rendered pages; assets fingerprinted; `astro build` produces the
full deployable tree (fewer manual copy steps); offline/PWA still passes an install +
offline-load smoke test.

**Risk:** medium — touches the deploy overlay and the service worker. Do it behind a
`dist/` diff and a real offline test before flipping `deploy.yml`.

---

## Phase 4 — Static-render the data-driven content (the real payoff)

**Goal:** stop shipping JS to render content that is fixed at build time. Read `data/`
JSON in `.astro` frontmatter and emit real HTML; hydrate only genuinely interactive bits
as islands.

**Prioritize by (static-ness × first-paint/SEO value):**
1. **Library** browser lists, author/creed/confession/catechism pages — content is a
   direct projection of `data/library/**`. Strong SSG candidate; the inline reader can
   stay an island.
2. **Topics** pages and `topics/_template` — largely static prose already.
3. **Dictionary / Biblepedia / ISBE / Smith / Torrey / Hitchcock** entries — huge, static,
   SEO-valuable; render entries at build time, keep search as an island.
4. **Reading plans / daily** tables from `data/plans/**` — static tables + a small
   progress island.

Leave inherently interactive, state-heavy surfaces (reader with live translation compare,
maps/timelapse, workshop, verse-study desk, wordcloud) as client apps — convert their
mount to an Astro island (`client:visible` / `client:idle`) rather than SSG-ing them.

**Acceptance:** targeted pages render meaningful content with **JS disabled**; hydration
scoped to interactive widgets only; measurable JS-payload and first-paint improvement.

**Risk:** medium–high, per page family. Do it page-family by page-family, each behind a
visual + DOM check. This is where Astro finally earns its place; also where the diff-clean
acceptance from Phase 1 is intentionally *retired* (SSG output will differ from the legacy
client-rendered DOM by design).

---

## Phase 5 — Componentize & converge

**Goal:** collapse the remaining duplication and the transitional apparatus.

- Extract repeated shell chunks into `.astro` components / islands: the verse **modal**,
  **tooltip**, **version picker**, sidebar **search** button, home **card grid**, the
  `_template` / `_template-book` scaffolds.
- Where content is fully SSG'd, drop those paths from the root overlay and the copy lists.
- Consider relaxing `compressHTML: false` / `format: 'preserve'` once the DOM-diff
  acceptance is no longer needed (post-Phase-4).
- Final PWA/offline pass; update `README.md` architecture section to match reality.

---

## Sequencing & ROI

| Phase | Effort | Risk | Payoff | Do when |
|------|--------|------|--------|---------|
| 2 — per-page entries | S–M | Low | **High** (kills 1.8 MB tax) | **Now** |
| 3 — assets into Vite | M | Med | High (hashing, splitting, sw) | After 2 |
| 4 — SSG data pages | L | Med–High | **Highest** (real Astro win) | Incremental, after 3 |
| 5 — componentize | M | Low | Medium (maintainability) | Ongoing / last |

**Recommended immediate step:** Phase 2. It's mechanical, reversible, needs no pipeline or
service-worker changes, and delivers the largest user-visible speedup on its own.

## Open decisions (need owner input before locking scope)

- **How far to go?** Phase 2 alone is a big, safe win. Phases 4–5 are a genuine
  re-architecture — confirm appetite before starting them.
- **Deploy-pipeline tolerance:** Phase 3 changes `deploy.yml` and `sw.js`. Confirm we can
  test an offline install against a preview before flipping the live deploy.
- **Keep this plan tracked in-repo or in `working/`?** `OVERHAUL.md` at root is committed
  and deployed as a static file; `working/` is gitignored. Say which you prefer.
