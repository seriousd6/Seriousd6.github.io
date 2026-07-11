# UI Overhaul Plan — Kingdom Bible Study

> Status document for the July 2026 site overhaul: Astro migration + "Candlelight"
> redesign + rebrand + Google Drive sync. Kept current as phases land.
> Last updated: **2026-07-11** · Live: https://kingdombiblestudy.com

## Decisions

- **Framework**: migrate the hand-authored static site to **Astro** (static output,
  GitHub Pages via Actions). The legacy JS/CSS/data runtime ships verbatim —
  no bundling of `assets/js` (modules rely on `import.meta.url` data paths and
  `?v=` cache-busters; bundling would break them).
- **Design direction**: **Candlelight** — the site's existing warm
  parchment/oak/gold identity, kept but disciplined. Chosen from three mocked
  directions (Candlelight / Study Desk / Rubric); mockups:
  https://claude.ai/code/artifact/fbf24564-2d1c-416d-ba0d-27f6c9080f36
- **Brand**: "Bible Study" → **"Kingdom Bible Study"**, matching the
  kingdombiblestudy.com custom domain.
- **Sync**: personalized cross-device sync via **Google Identity Services +
  Drive `appDataFolder`** (user's own Drive, no backend, $0).

## Completed

### Phase 0–1 — Astro structural migration (2026-07-11)
- 75 pages converted to `src/pages/*.astro` sharing `src/layouts/Base.astro`;
  DOM-diff-verified **identical** to the legacy HTML before cutover
  (`tools/convert-pages.mjs` / `tools/diff-pages.mjs`, now historical).
- **Overlay layout**: `assets/`, `data/`, `sw.js` stay at the repo root (the
  hourly data auto-sync writes there). `tools/root-statics.mjs` serves them in
  `astro dev`; `.github/workflows/deploy.yml` copies them into `dist/`.
- 9 redirect stubs + `_template` scaffolds + `offline.html` ship verbatim —
  copy lists live in `root-statics.mjs` and `deploy.yml` (keep in sync).
- Cutover complete: Pages source = GitHub Actions, auto-deploy on every push
  to master, legacy root HTML deleted. Rollback = revert + push.

### Rebrand (2026-07-11)
- Titles/OG metas across all pages, sidebar logo, PWA manifest
  (name "Kingdom Bible Study", short_name "Kingdom"), onboarding, share-scene
  canvas, dynamic `document.title` strings, offline page.

### Phase 2 — Candlelight application (2026-07-11)
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

### Google Drive sync — built, dormant (2026-07-11)
- `assets/js/sync.js` + Settings → "Sync & Backup": backup/restore of all
  `bsw_*` localStorage state to the user's Drive app-data area; auto-backup
  with change detection; confirm-gated restore.
- **Activation blocked on one manual step** (see below).

### Housekeeping (2026-07-11)
- CI fixed twice: branch filter (`main` → `master`; it had never run) and
  missing `beautifulsoup4` install. Validate is green and now also runs a full
  Astro build on every push.
- Astro 5.18.2 → **6.4.8** (build output verified byte-identical) + esbuild
  override `^0.28.1` → **0 open Dependabot alerts**.

## Next up

1. **Activate Drive sync** — follow "Google Drive sync activation" below
   (~10 min, free, user action only).
2. **Remaining Candlelight polish** (optional, incremental):
   - Study-guide / topic page typography alignment (they carry their own
     Google-Fonts look today).
   - Reader study-desk panels onto the card token language, if desired.
3. **Phase 3 candidates** (unscheduled): content collections for
   topics/study-guides, per-page JS bundling, Astro view transitions.

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
- Bump `APP_CACHE_V` in `sw.js` (sync.js is cache-first; clients won't see the
  change without a bump).
- Commit + push (deploys automatically). Or paste the client ID into a Claude
  Code session and ask it to do this step.

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

- **Every asset change needs an `APP_CACHE_V` bump in `sw.js`** (currently
  v184) — CSS/JS are cache-first in the service worker.
- Page edits happen in `src/pages/`; nav edits in `src/components/Sidebar.astro`;
  local page-generating tooling must author `.astro`, not raw HTML.
- `npm run dev` (localhost:4321) serves pages from `src/` and statics from the
  repo root; every push to master deploys (~2–3 min).
- Design token source of truth: `:root` blocks in `assets/css/style.css`
  (light + two dark blocks — keep all three in sync).
