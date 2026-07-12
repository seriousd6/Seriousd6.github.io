# UI Overhaul Plan — Kingdom Bible Study

> Status document for the July 2026 site overhaul: Astro migration + "Candlelight"
> redesign + rebrand + Google Drive sync + JS-runtime/data-page overhaul.
> Kept current as phases land.
> Last updated: **2026-07-11** · Live: https://kingdombiblestudy.com

## Decisions

- **Framework**: migrate the hand-authored static site to **Astro** (static output,
  GitHub Pages via Actions).
- **Asset pipeline** *(revised 2026-07-11)*: `assets/js` **is** bundled now — the
  original "ship verbatim" decision existed because modules relied on
  `import.meta.url` data paths and `?v=` cache-busters. Those blockers were removed
  (all data URLs resolve through `core.js _resolve()`; content hashing replaced
  `?v=`), and `tools/build-assets.mjs` Vite-bundles per-page entries with stable
  URLs + hashed minified chunks. `astro dev` still serves the raw tree as native ESM.
- **Design direction**: **Candlelight** — the site's existing warm
  parchment/oak/gold identity, kept but disciplined. Chosen from three mocked
  directions (Candlelight / Study Desk / Rubric); mockups:
  https://claude.ai/code/artifact/fbf24564-2d1c-416d-ba0d-27f6c9080f36
- **Brand**: "Bible Study" → **"Kingdom Bible Study"**, matching the
  kingdombiblestudy.com custom domain.
- **Sync**: personalized cross-device sync via **Google Identity Services +
  Drive `appDataFolder`** (user's own Drive, no backend, $0).
- **Design direction — "Daylight"** *(2026-07-12, supersedes Candlelight)*: chosen from
  three mocked directions (Rubric / Lapis / Daylight —
  https://claude.ai/code/artifact/3d419123-5e13-44d3-b76f-2c904d0d8b07). Paper-white
  ground, green-biased ink, **olive** primary (laurel) + **brass** accent (lampstand) +
  **ember** for red-letter; Archivo (variable) for all UI chrome, Literata (variable)
  for scripture/long-form; stroke SVG icons replace emoji; study markup stays always-on
  but quieted. Dark theme is "Evening" (moss-black). Token source of truth unchanged:
  `:root` blocks in `assets/css/style.css`; living style guide at `/design/`.
- **Static-first content** *(2026-07-11)*: data-driven pages render at build time
  ("render-then-enhance") — the client app that serves the legacy query-param URLs
  detects the static path and replaces the pre-rendered DOM with the enriched view.
  One implementation per app; static HTML is its build-time snapshot.

## Completed

### Phase 0–1 — Astro structural migration (2026-07-11)
- 75 pages converted to `src/pages/*.astro` sharing `src/layouts/Base.astro`;
  DOM-diff-verified **identical** to the legacy HTML before cutover
  (`tools/convert-pages.mjs` / `tools/diff-pages.mjs`, now historical).
- **Overlay layout**: `assets/`, `data/`, `sw.js` stay at the repo root (the
  hourly data auto-sync writes there). `tools/root-statics.mjs` serves them in
  `astro dev`; `.github/workflows/deploy.yml` copies what the build doesn't emit.
- 9 redirect stubs + `_template` scaffolds + `offline.html` ship verbatim —
  copy lists live in `root-statics.mjs` and `deploy.yml` (keep in sync).
- Cutover complete: Pages source = GitHub Actions, auto-deploy on every push
  to master, legacy root HTML deleted. Rollback = revert + push.

### Rebrand (2026-07-11)
- Titles/OG metas across all pages, sidebar logo, PWA manifest
  (name "Kingdom Bible Study", short_name "Kingdom"), onboarding, share-scene
  canvas, dynamic `document.title` strings, offline page.

### Phase 2 (Candlelight) — design application (2026-07-11)
- **Static sidebar**: nav renders at build time from
  `src/components/Sidebar.astro` (edit nav links THERE); `assets/js/main.js`
  only wires behavior. Pre-paint bootstrap in `Base.astro` applies
  collapse/overlay/embedded state before first paint.
- **Tokens** (`assets/css/style.css`): warmer parchment ground, warm off-white
  surfaces, hairline borders, deeper oak sidebar; candlelit deep-brown dark
  mode; new `--shadow-card` / `--radius-card` tokens.
- **Cards**: home page + 21 surfaces across bible-ui / library / lib-browser /
  discipline / biblepedia adopted the tokens. `reader.css` deliberately keeps
  its compact 6px style. Footer is a quiet hairline rule in both themes.

### Google Drive sync — built and ACTIVE (2026-07-11)
- `assets/js/sync.js` + Settings → "Sync & Backup": backup/restore of all
  `bsw_*` localStorage state to the user's Drive app-data area; auto-backup
  with change detection; confirm-gated restore.
- Google Cloud config done (project + Drive API + Testing-mode consent screen
  + web client ID); client ID wired into `sync.js`. The OAuth app stays in
  **Testing** mode deliberately — see the activation section below for the
  console steps if the client ID ever needs recreating.

### JS runtime & data-page overhaul, Phases 2–5 (2026-07-11)

Shipped in sequence on `claude/repo-overhaul-context-1ixq9c` (per-phase detail
in the commit messages):

- **Per-page JS entries** *(Phase 2 + 2.5)* — the `app.js` monolith (30 static
  imports, ~1.8 MB parsed on every page) is gone. Each page loads a thin entry
  from `assets/js/entries/` (selected by Base.astro's `entry` prop, default
  `generic`); the shared boot lives in `assets/js/core-boot.js`, which
  lazy-loads heavy pieces (terms/places tagging at idle, search engine only on
  the search page, `mem.js` extracted from daily.js for the modal's Memorize
  button, dead modal-renderer bridge deleted).
  **Eager JS on generic pages: 1,800 KB → 200 KB (−89 %)**; reader 558 KB.
- **Vite asset pipeline** *(Phase 3)* — `npm run build` = `astro build` +
  `tools/build-assets.mjs`: entries bundle with **stable URLs** + hashed
  minified chunks; `core.js`/`tracker.js` are stable externals (inline page
  scripts import them — single module instance); CSS minified in place;
  `sw.js`'s JS/CSS precache list and `APP_CACHE_V` are **generated from the
  emitted bytes** (manual cache bumps for JS/CSS are retired). Emitted:
  JS 1.9 MB → 880 KB, CSS 876 → 628 KB.
- **Static data pages** *(Phase 4)* — **4,418 Biblepedia articles** at
  `/biblepedia/<slug>/` and **143 library documents** at `/library/read/<id>/`
  render at build time (render-then-enhance; legacy `?a=`/`?doc=` URLs still
  work; link emitters point at the canonical paths). The library browser's
  catalog is crawlable no-JS. Reading-plan tables stay client-side by design
  (build date ≠ view date). Build: 4,635 pages in ~35 s.
- **Convergence** *(Phase 5)* — dead modules deleted (`word.js`,
  `provenance.js`, `discipline-strip.js`, the dead sidebar Search-button
  injection); `compressHTML: true`; `@astrojs/sitemap` + `robots.txt`
  (all 4,635 pages in `sitemap-index.xml`); README architecture rewritten.

Deferred deliberately: framework islands for modal/tooltip (plain JS is
bundled + lazy already), `_template` scaffolds, `dictionary/` redirect page's
vestigial markup, `verse-study.js`/`ol-companion.js` (reachable via the
documented `BibleUI.initOLSection` API; emitted only as a lazy chunk).

### Privacy, terms & sync transparency (2026-07-11)
- **/privacy/ + /terms/ pages**: plain-language policy — data lives in the
  browser and (optionally) the user's own Drive app-data area for cross-device
  continuation only; never evaluated, shared, or sold; includes the Google API
  Limited Use statement. Linked from the site footer and the sync UI.
- **Sync UI transparency**: green/gray connected badge, live "backing up N
  items (~KB)" line, and a "What gets synced, and where it goes" disclosure in
  Settings → Sync & Backup.

### Housekeeping (2026-07-11)
- CI fixed twice: branch filter (`main` → `master`; it had never run) and
  missing `beautifulsoup4` install. Validate is green and runs the full
  production build (astro + assets) on every push.
- Astro 5.18.2 → **6.4.8** + esbuild override `^0.28.1` →
  **0 open Dependabot alerts**.

### Daylight increment 1 — foundation (2026-07-12)
- Retokened `style.css` (light + both dark paths) to the Daylight palette; self-hosted
  Archivo + Literata variable subsets (via @fontsource, build-time dep); fonts join the
  generated sw precache.
- Sidebar rebuilt: flat **Read / Study / Practice / Tools** IA with stroke SVG icons
  (accordion + duplicate labels gone, wordmark no longer truncates, version picker
  moved below nav; `wireSidebar` contract preserved — its group loop no-ops).
- Reader markup quieted: red-letter → ember token, term links → 1px muted dotted,
  ref links stay ink-colored with a faint dotted rule (brass on hover), the gold 🔗
  echo pills → small bordered brass-count chips (emoji hidden).
- Biblepedia category badges retinted to the earthy "field set" (light + both dark
  paths); dark notification-banner button contrast fixed.
- `/design/` style guide added (token-driven specimens).
- Verified: full functional pass on the built dist (home plan, reader, modal,
  biblepedia, library doc, discipline) with zero page errors.

### Daylight increment 2 — surfaces (2026-07-12)
- **Reader toolbar consolidated**: lookup, browse selects, and every feature toggle
  flow as one wrapping control band under a single hairline (desktop ≥641px;
  mobile keeps its stacked 44px layout). "Browse:" label and keyboard-hint text
  retired; buttons de-emojied (⚙ View → **Aa** with aria-label, 📖 Study Tools →
  Study Tools, ⇅ Compare → Compare, 🔊 Listen → Listen/Pause/Resume).
- **Topics & study guides in-family**: the seven `--bk-accent` genre tints retuned
  to the Daylight field set (epistle navy → slate #3a4a70, prophecy violet →
  #4f4a78, …); the two pages loading Google Fonts (Cinzel/EB Garamond/…) now fall
  back to the self-hosted faces — no external font requests anywhere. Study-guide
  pages + template finally link `book-study.css`, fixing the long-unstyled tier nav.
- **Home hierarchy**: the notification banner moved from above the greeting to the
  end of the page; the red BEHIND stamp became a muted "catching up" chip (brass on
  subtle surface; "ahead" wears olive).
- **Library filters**: tradition/era/type chips render as wrapped pill rows instead
  of a ~30-row stack of full-width buttons.

### Daylight increments 3–6 — completion (2026-07-12)
- **3 · Apparatus rail** (`assets/js/reader-rail.js`): chapter-head chips counting
  connections / places / notes, built from a debounced MutationObserver over
  `#reader-results` (zero reader.js surgery); chips scroll to the first marker or
  open the notes panel.
- **4 · Emoji sweep**: colored pictographs out of every tab bar/button/label;
  stroke SVGs on the biblepedia hub tiles and onboarding cards; typographic
  glyphs (arrows, ✓✕★☆✦☰⚑) deliberately kept.
- **5 · Hex sweep**: 336 lines across 18 CSS files stop hardcoding the old
  Candlelight palette — former token literals → `var(--token)`, rgba overlays →
  `color-mix`, stale `var(--x, #hex)` fallbacks collapsed. Dictionary source
  badges (E/S/IS/H/N/T/Str) retinted to the field set.
- **6 · Type inversion**: `body` speaks Archivo; scripture/long-form containers
  (`#reader-results`, apocrypha, library readers + curated `.lib-doc` pages,
  biblepedia article bodies, VOTD/devotionals, `blockquote.scripture`,
  `.bsw-verse`) opt back into Literata at a book-like measure.

**The Daylight overhaul is complete.** Every increment carried a full
headless-Chromium functional pass and screenshot review in both themes.

## Next up

> **The active plan has moved to [`ROADMAP.md`](ROADMAP.md)** — the 2026-07-12
> outside evaluation (overall grade: B+) and the phased path to the heights
> (query understanding, apparatus surfacing, topical answer pages, audits).


1. **Remaining Candlelight polish** (optional, incremental):
   - Study-guide / topic page typography alignment (they carry their own
     Google-Fonts look today).
   - Reader study-desk panels onto the card token language, if desired.
2. **Unscheduled candidates**: content collections for topics/study-guides,
   Astro view transitions, self-hosting Leaflet (maps currently load it from
   unpkg — an offline gap), static rendering for more page families.

## Google Drive sync activation — step by step

Everything here is free: no billing account, no verification review. Do it
signed into the Google account whose Drive should hold the backups.

### 1. Create the project
Go to https://console.cloud.google.com (accept terms on first visit). Project
picker in the top bar → **New project** → name it `Kingdom Bible Study` →
Create. No billing account, no organization.

### 2. Enable the Drive API
With that project selected: **APIs & Services → Library** → search
**"Google Drive API"** → open it → **Enable**. (Grants the project permission
to call the API; stores nothing.)

### 3. Configure the consent screen
**APIs & Services → OAuth consent screen** (newer console layouts:
**Google Auth Platform → Branding / Audience**):
- **User type**: External (personal Gmail can't pick Internal — fine).
- **App name**: Kingdom Bible Study; your email for support + developer contact.
  Skip logo and all optional fields.
- **Publishing status / Audience**: leave in **Testing** — important. Under
  **Test users**, **add your own Gmail address**. Testing mode + you as a test
  user means Google's app-verification review never applies.
- If a **Scopes** / "Data Access" step is offered, add
  `https://www.googleapis.com/auth/drive.appdata` ("See, create, and delete its
  own configuration data in your Google Drive"). If you can't find that UI,
  skip it — the app requests the scope at sign-in time anyway.

### 4. Create the OAuth client ID
**APIs & Services → Credentials → + Create Credentials → OAuth client ID**:
- **Application type**: Web application. Name: anything (e.g. `kbs-web`).
- **Authorized JavaScript origins** — add BOTH:
  - `https://kingdombiblestudy.com`
  - `http://localhost:4321`  (so sync works in `npm run dev`)
- **Authorized redirect URIs**: leave **empty** (Google Identity Services
  token flow doesn't use one).
- Create → copy the **Client ID** (long string ending in
  `.apps.googleusercontent.com`). Ignore the client secret — a browser-only
  app never uses it, and the client ID itself is not a secret (the origin
  allowlist is what controls use).

### 5. Wire it into the site
- Paste the client ID into `var GOOGLE_CLIENT_ID = '...'` at the top of
  `assets/js/sync.js`.
- Commit + push (deploys automatically — the build stamps a new asset hash,
  so no manual `APP_CACHE_V` bump is needed anymore). Or paste the client ID
  into a Claude Code session and ask it to do this step.

### 6. First connection — what to expect
- Settings → **Sync & Backup** → **Connect Google Drive**.
- Google shows **"Google hasn't verified this app"** — normal Testing-mode
  banner; as a registered test user, continue past it.
- Backups land in a hidden Drive app-data area (not visible among your files,
  readable only by this app; counts against your normal Drive storage — the
  file is kilobytes). Auto-backup runs on Settings visits when data changed;
  access tokens renew silently, with an occasional re-approval popup if the
  browser blocks silent renewal.
- To sever access later: the Disconnect button, or
  https://myaccount.google.com/permissions.

## Operational notes

- **`APP_CACHE_V` and the JS/CSS precache list are stamped at build time**
  (`tools/build-assets.mjs`, `BUILD:ASSETS` markers in `sw.js`) — asset changes
  deploy with correct cache-busting automatically. Manual bumps are only ever
  needed for the hand-listed HTML/data entries in `SHELL_URLS`.
- Page edits happen in `src/pages/`; nav edits in `src/components/Sidebar.astro`;
  local page-generating tooling must author `.astro`, not raw HTML.
- New pages with their own feature module: add a thin entry under
  `assets/js/entries/` and set `entry="<name>"` on `<Base>` (see README).
  Resolve data URLs through `core.js _resolve()` — never `import.meta.url`
  (it breaks inside bundled chunks).
- `npm run dev` (localhost:4321) serves pages from `src/` and statics from the
  repo root (unbundled native ESM); every push to master deploys (~2–3 min).
- Design token source of truth: `:root` blocks in `assets/css/style.css`
  (light + two dark blocks — keep all three in sync).
