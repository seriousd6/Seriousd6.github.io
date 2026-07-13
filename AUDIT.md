# Adversarial Audit — 2026-07-13

Every route crawled cold (desktop 1366px + phone 390px), errors and weights
measured, screenshots reviewed, code paths traced. Nothing exempted. This is
the "everything wrong" list — bugs, inefficiencies, redundancies, design
debt, and missed usefulness — ordered by section, each item tagged
**[bug]** / **[perf]** / **[ux]** / **[ia]** (information architecture) /
**[a11y]** / **[quality]**, with severity ●●● high, ●● medium, ● low.

Fixed during this audit (commit `4617a585`): "anxiety" had no answers page
(649 Nave stubs skipped — 233 now generated from text), answers pages were
unreachable (no sidebar link, no search pointer), trailing "?" broke query
intent. Those are not re-listed below.

**Status (2026-07-13, post-audit fix batches P1–P6):** items marked ✔ below
are fixed and verified; items marked ✕ were withdrawn after closer
investigation showed the finding was wrong. Unmarked items remain open.

---

## 1 · Outright bugs found

- ✔ ●●● **[bug] /about/ overflows phones by 148px** — horizontal page scroll on
  every mobile visit to the transparency page.
- ✔ ●● **[bug] Compare fires 12 guaranteed 404s per lookup** — it fetches every
  version in versions.json, including the 12 `stub:true` versions with no
  data files (YLT, DBY, GNV, AKJV, WEBBE, MKT-L/M/T, DR, KJV-APO, WEB-CE,
  BRENTON). Wasted requests, console noise, and 12 dead rows attempted per
  verse. The precache path already knows to filter these; compare doesn't.
- ✔ ●● **[bug] Workshop "Choose your study depth" dialog renders detached** —
  an unstyled card floating at the top-left of the page with no backdrop or
  centering, above a separate app frame. First impression of the deepest tool
  on the site is a layout accident.
- ✔ ● **[bug] /history/ era column layout glitches** — era labels overlap their
  count badges ("Conquest & Judges", "Between the Testaments"), and huge
  uneven vertical gaps between eras make the timeline read as broken.

## 2 · Search & discovery

- ✔ ●●● **[quality] Generated answers pages are unranked** (now ranked, with curated pinned openers for modern topics) — the 233 text-
  matched topics list verses in canonical order, so the strongest verse isn't
  first (fixed for "anxiety" only by luck of Psalms coming early). They
  should rank exact-word hits above synonym hits before capping at 40.
- ●● **[quality] Verse ranking is still shallow** — weight = match-type sum;
  no phrase proximity, no verse-length normalization, no popularity signal.
  "love" returns Genesis 22:2 first because canonical order breaks ties.
- ✕ ●● **[ia] Two search UIs with different powers** — WITHDRAWN: closer
  reading of core-boot.js shows Ctrl+K simply focuses or navigates to
  /search/ — there is no second search UI, so feature parity is automatic.
- ✔ ●● **[quality] No typo tolerance** — "anxeity" returns nothing and doesn't
  suggest "anxiety". One edit-distance pass over the token list would fix it.
- ✔ ● **[ia] Omni sections vs answers pages overlap** (topic chips now link to /answers/ pages) — the Omni "topics"
  section and /answers/ serve the same intent with different presentations;
  the Omni topic section could simply BE the answers preview.
- ● **[quality] Synonym table is 24 hand-picked entries** — good ones, but a
  systematic pass (lemma-based, from the interlinear data the site already
  has) would cover far more ("crucifixion" → "crucified" works via stem, but
  "resurrection" → "raised" doesn't).

## 3 · Information architecture & redundancy

- ✔ ●●● **[ia] Three home-shaped sidebar entries** — Home (→ Desk on desktop,
  → daily page on phone), The Desk, and Today. Three labels, two
  destinations, platform-dependent behavior. "Home" should collapse into one
  clear entry per platform.
- ✔ ●●● **[ia] The graveyard of orphan pages** (adopted into the shell or redirected; sidebar links added) — /notes/, /bookmarks/,
  /compare/, /tracker/, /wordcloud/, /maps/, /timeline/, /church-history/,
  /study-guides/ are all real pages reachable only through in-page links (or
  not at all). Bookmarks and My Study even have their own nonstandard chrome
  ("← Home" buttons, no sidebar) — they predate the shell and it shows.
- ✔ ●● **[ia] Compare exists three times** — CORRECTED: the verse modal's
  "All translations" was already a plain link into /compare/ (no third
  codepath). What remained was a naming collision: the reader toolbar's
  side-by-side second-translation toggle was also labeled "Compare". Renamed
  to "2 Versions" so the two features read as distinct.
- ✔ ●● **[ia] Word study exists four times** — unified on the reader's
  `?strongs=` occurrence-browser mode as the canonical deep link (it was
  already the richest surface: lemma banner + paged passages + interlinear
  highlight, and biblepedia already targeted it). The verse modal's "Word
  Deep Dive", search's Strong's cards, and the interlinear tile popover now
  all point there; the passage-desk word blade serves in-page study; the
  Translation Workshop remains as the explicitly-labeled specialist dossier,
  linked from the strongs banner and the word blade.
- ✔ ●● **[ia] Three annotation systems with unclear boundaries** — My Study
  gained a Journal tab surfacing the Disciplines prayer journal and study
  reflections read-only (dates, text, refs, tags, links back to edit in
  Disciplines), so "where did I write that?" has one answer. The systems
  keep separate storage by design (verse-anchored vs date-anchored).
- ✔ ●● **[ux] /studies/ is a wall of disabled cards** — 60+ grayed-out books
  with dead Guide/Deep-Dive/Commentary chips; only a handful have content.
  The default view should be "Has Content", with the rest behind "all books"
  — advertise what exists, not what doesn't.
- ✕ ● **[ia] /history/ hub duplicates standalone routes** — WITHDRAWN
  after re-testing: the hub's tabs switch same-document (lazy-loaded
  iframes shown/hidden; verified the page never reloads on tab clicks),
  and framing the standalone routes with ?minimal=1 is the same
  composition pattern the Desk uses — the standalone routes exist for
  deep links. The one real defect here — landing on an empty three-pane
  view — was ✔ fixed (the timeline auto-selects the earliest era).
- ✔ ● **[ia] /tracker/ duplicates the Today tracker card** as a standalone
  orphan page.
- ✔ ● **[ux] My Study header has six buttons** — Export all data / Import all
  data / Import notes / Export text / Export notes / ← Home. Two overlapping
  import/export systems side by side, plus a Home button next to a sidebar
  that has Home. Should be one Export/Import pair with format options.

## 4 · The Desk

- ✔ ●● **[ux] No per-panel back/address control** — navigate a biblepedia
  panel three articles deep and there's no back button; browser Back pops
  the top window's history unpredictably (iframe navigations share the
  session history). Panels need a small back affordance (history.back() on
  the frame) and/or breadcrumb.
- ✔ ●● **[ux] Layouts aren't shareable or savable** — Layouts ▾ menu added:
  named save/load/delete, `/desk/#bible+maps` hash form, and a copy-able
  share link encoding the full tree (`/desk/#z=…`) that reproduces the
  workspace on any device.
- ● **[ux] One global link-set** — Logos has A/B/C link groups; here every
  linked panel joins the same set, so two independent linked pairs aren't
  possible.
- ● **[perf] Desktop restore builds every panel eagerly** — the phone desk
  lazy-builds per tab, but a restored 6-panel desktop layout loads six full
  pages at once (~130 KB JS/CSS each after frame-lite, plus data). Off-screen
  is impossible on desktop, but staggered/idle mounting isn't.
- ● **[ux] Chooser can't open an arbitrary page** — 12 fixed resources; no
  "open any URL/topic/article" input except the Bible passage field.

## 5 · Performance & network

- ✔ ●●● **[perf] The 1.8 MB biblepedia index is idle-fetched on nearly every
  content page** (second pass: pages now tag with 367 KB bp-tag.json; briefs load on first hover) to power term tooltips (and now word-tap article actions).
  The tooltip needs term/id/brief/category — a trimmed terms-index (~300 KB)
  would serve the hover layer, with the full index only on biblepedia itself.
- ✔ ●● **[perf] nave.json is 1.4 MB** (topics-lite.json, 176 KB) and fetched whole by the Omni topics
  section at runtime; the topic chips need slug+title+count (~150 KB).
- ✔ ●● **[perf] reader.css is 120 KB** — the Passage Study Desk layer
  (~36 KB: drawer, blades, binder rail) now lives in reader-study.css,
  injected on the first Study-button press; plain reading parses 131→92 KB
  (minified) and never pays for the desk.
- ✔ ● **[perf] /read/?ref=John+3 costs ~2.1 MB cold** — re-measured at
  2.65 MB, now 1.82 MB (−31%): the tagging layer fetches bp-tag.json
  (367 KB, no briefs) instead of bp-lite (1.2 MB) — the brief-carrying
  index loads only on the first tooltip/tap — and crossref + echo marker
  data (~700 KB) defers to idle so it never blocks first paint.
  Commentary/interlinear were already toggle-gated.
- ● **[perf] The answers build scans the whole BSB twice** — once in
  answers-topics.mjs, once in build-search-index.mjs (build went 15 s →
  35 s). Share one tokenization pass.
- ● **[perf] sw.js precaches 225 assets on install** — includes every page
  family's entry+chunks whether or not the user ever visits; consider tiering
  (shell now, features on first use — the data layer already works this way).

## 6 · Mobile

- ✔ ●● **[bug] /about/ overflow** (see §1).
- ● **[ux] Desk tab strip lacks swipe** — tabs tap fine, but the natural
  phone gesture (swipe between panels) isn't wired.
- ● **[ux] Reader toolbar is still dense on phones** — lookup, book/chapter
  selects, version, Compare, Aa, Study Tools, Notes, Listen, ? in two
  wrapping rows before any scripture shows.

## 7 · Accessibility

- ✔ ●● **[a11y] Word-tap is mouse/touch-only** (keyboard path: select word + W, listed in the ? overlay) — the richest hub (lexeme
  popover) can't be opened from the keyboard at all; term/place anchors can
  be focused but words can't. A keyboard path (e.g. verse focus + key) or an
  equivalent command is needed.
- ● **[a11y] Desk drag interactions have no keyboard equivalent** — divider
  resize and drag-to-re-dock are pointer-only (split/close/maximize do have
  shortcuts).
- ● **[a11y] Hover tooltips (term/place) don't appear on focus for the
  word-tap-upgraded surfaces** — places.js wires focus/blur, terms.js only
  mouseenter/leave.

## 8 · Content & quality

- ✔ ●● **[quality] Workshop dashboard opens with "GREEK REVIEWED 0 of 5,523 ·
  0%"** (getting-started zero-state added) — a demotivating zero-state for a tool most users open once; the
  wall-of-text "Dashboard" panel reads like documentation, not UI.
- ● **[quality] Nave ALL-CAPS titles titleCase imperfectly** — "Ai" fine,
  but multi-part heads like "Olives, Mount Of" keep odd inversions from the
  1896 source on answers pages.
- ● **[quality] Answers preview is BSB-only and first-8-parseable** — a
  chapter-level or unparseable ref silently drops out of the preview cards.
- ● **[quality] Generated answers cap at 40 canonical refs** with no "why
  these" note beyond the source line.

## 9 · Environmental (not actionable in code)

- Leaflet + tiles come from CDNs — maps/mini-maps die offline (they degrade
  with notes + working links, by design). Self-hosting Leaflet would remove
  the unpkg dependency; tiles can't realistically be self-hosted.

---

## Priority order (if fixing top-down)

1. §1 bugs (about overflow, compare 404s, workshop dialog, history layout)
2. Rank the generated answers pages; trim the term-tooltip index (§2, §5)
3. IA collapse: home trinity, orphan adoption or removal, studies default
   filter, compare unification (§3)
4. Desk panel back button + named layouts (§4)
5. Keyboard path for word-tap (§7)
6. The rest as taste dictates.
