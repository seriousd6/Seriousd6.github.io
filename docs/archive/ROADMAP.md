# Roadmap — From B+ to the Heights

> Findings from the 2026-07-12 outside evaluation of kingdombiblestudy.com as a
> Bible study tool, and the phased plan to close the gaps. Companion to
> `OVERHAUL.md` (the completed migration + Daylight record). Kept current as
> phases land.

## The evaluation in one table

Method: used the site cold, the way a newcomer would — typed natural questions,
hunted for features without insider knowledge, compared against BibleHub,
BlueLetterBible, STEP Bible, Logos, and YouVersion.

| Dimension | Grade | Finding |
|---|---|---|
| Content breadth | A | 10+ translations, 3 commentaries, Strong's + interlinear, TSK cross-refs, 4,600 encyclopedia articles, 143 historic documents, maps, timelines |
| Reading experience | A− | Post-Daylight typography and quiet markup; genuinely pleasant long-form reading |
| Study depth | B+ | Study desk, OL workshop, synthesis — deeper than most free tools |
| **Discovery & search** | **C** | *"what does the bible say about anxiety"* → **"No results."** The data to answer is all present (Omni returns 9 rich sections for "anxiety"); the query understanding is not |
| **Feature discoverability** | **C+** | Zero visible commentary affordances on a loaded chapter; interlinear/parallels/desk all behind popovers. A visitor can leave never knowing the depth exists |
| Practice loop | B+ | Plans + SRS memory + journal + streaks, no account needed |
| Mobile | B− | Structurally sound; has had one reactive fix, never an audit |
| Performance & offline | A− | ~200 KB pages, full offline PWA, static-rendered content |
| Trust & provenance | A− | AI-assisted badges, provenance manifest, source dates — ahead of commercial tools |

**Overall: B+.** Not held back by content, speed, design, or engineering — held
back entirely by *connecting a stranger to what's already inside*. It fails the
first question a newcomer asks, and it hides its depth behind popovers.

Out of scope by reality, not neglect: licensed modern translations (ESV/NIV/CSB)
— a licensing-cost ceiling. Mitigation is the compare view + original-language
tooling ("we show you the Greek/Hebrew instead").

## The plan

### H1 — Answer the question  ·  highest leverage
The site must do something useful with *"what does the bible say about X"*.

- **H1a · Query understanding (search.js)**
  - Normalize question boilerplate ("what does the bible say about", "bible
    verses about/on/for", "who was", "meaning of", …) down to the topic kernel.
  - When the Verse tab yields zero results and the query isn't a reference,
    automatically run the Omni (explore) search instead of dead-ending — with a
    "showing everything for *anxiety*" note.
  - Verification: the exact failing probe returns the 9-section Omni answer.
- **H1b · Static topical answer pages**
  - `/answers/<slug>/` rendered at build (render-then-enhance pattern already
    proven on biblepedia/library): topic head, key verses (hotlinked, wired to
    the modal), Nave's outline, related dictionary/biblepedia entries, related
    topics. Sourced from the Nave's/Torrey data already shipped.
  - These are the landing pages that make BibleHub a search-engine juggernaut;
    they join the sitemap. Scope control: generate for topics that have real
    content; odd ids stay client-rendered.
  - Search links topical results to these canonical pages.

### H2 — Surface the apparatus  ·  cheapest, do first
When a chapter loads, show what the site has for it.

- Extend the reader apparatus rail with feature chips: **Commentary** (3
  sources), **Interlinear**, **Parallels** — state-aware, wired to the existing
  toggles (open the feature, not blind-toggle; the connections-chip lesson).
- The rail becomes the front door to the depth that today hides in popovers.

### H6 — Click-distance audit  ·  RUN 2026-07-12

Sixteen top intents, walked in a real browser against the built site. Counts are
taps after arrival (T = typing). Target: ≤2 from the natural starting point.

| # | Intent | From | Path | Cost | Verdict |
|---|--------|------|------|------|---------|
| A | Read today's plan reading | home | "Read all today's sections" | 1 | ✓ |
| B | Look up John 3:16 | home / reader | lookup box → Go | T+1 | ✓ |
| C | "What does the Bible say about X" | home | Explore → type (kernel + omni fallback + /answers/ pages) | T+1 | ✓ *(was a dead end)* |
| D | Commentary on this chapter | reader | rail chip | 1 | ✓ *(was 3, behind popover)* |
| E | **What does this word mean** | reader | Study Tools → Interlinear/Study desk → navigate | **4+, undiscoverable** | ✗ |
| F | Cross-refs for a verse | reader | echo chip on the verse | 1 | ✓ |
| G | **Where is this place** | reader | **no path** — place layer never tags scripture (`places.js _TARGETS` covers intros/timeline/maps/topics only; manual `autoTagPlacesIn(#reader-results)` tags Matthew 4 fine) | ∞ | ✗ |
| H | Who was Melchizedek | reader | verse tap → Connections → article | 3 | ~ |
| I | Compare translations | reader | verse tap → All translations (or toolbar Compare) | 1–2 | ✓ |
| J | Memorize this verse | reader | verse tap → Memorize | 2 | ✓ |
| K | Note on a verse | reader | verse number tap (Notes panel default-on) | 1 | ✓ |
| L | Read a confession | home | Library → document | 2 | ✓ |
| M | See reading progress | home | sidebar | 1 | ✓ |
| N | Find a half-remembered phrase | anywhere | Ctrl+K → type ("cloud of witnesses" → exact hit) | T+1 | ✓ |
| O | Study a whole book | home | Studies → book | 2 | ✓ |
| P | Resume where I left off | home | The Holy Bible → "Continue where you left off" banner | 2 | ✓ |

**Score at audit time: 13 of 16 intents at ≤2 taps.** The offenders were the
remaining un-hubbed nouns — all three fixed 2026-07-12 (**16/16 now ≤2 taps**):

- **E · Word → lexicon — FIXED.** `reader-wordtap.js`: tapping a plain word in
  scripture opens a compact popover with the matched Strong's lemma /
  transliteration / gloss (resolved against the verse's interlinear tokens),
  plus "All occurrences" and "Full word study" (deep-links into the study
  desk's word blade). Defers to every existing tap surface — refs, terms,
  places, echo markers, verse numbers — and stands down when the interlinear
  view is active or text is selected. Verified: tap "tempted" in Matthew 4 →
  πειράζω peirázō G3985; "Full word study" opens the desk on G3985.
- **G · Place → map — FIXED.** `reader-rail.js` now runs `autoTagPlacesIn` on
  `#reader-results` once per chapter (keyed book|chapter so the rail's
  mutation observer doesn't loop). Chose option (a): always-on quiet tags,
  same treatment as terms. Verified: Matthew 4 tags 4 places, the rail chip
  counts them, hover shows the place tip.
- **H · Person → article — FIXED**, riding along with E: the word-tap popover
  checks the biblepedia index and adds a "Read the … article" action when the
  word names an article. Names the term layer already links (e.g. "Jesus")
  keep their existing 1-tap `.term-link`. Verified: tap "devil" in Matthew 4 →
  "Read the Devil article" → `/biblepedia/devil/`.

### H3 — First-run demonstration  ·  DONE 2026-07-12
- The onboarding names 4 features; the site has 15, and the *chain*
  (verse → modal → connections → word study → article) is the product.
- Shipped: `/tour/` — "Everything on one verse" walks John 3:16 through the
  chain in 7 live steps (verse modal demo in-page, word tap, `?strongs=G25`
  occurrences, `?study=1` full apparatus, biblepedia, `/answers/love/`,
  memorize). Onboarding gained a "See everything on one verse →" link beside
  Get started; the sidebar gained Tools → Site Tour.

### H4 — Mobile & accessibility audit  ·  DONE 2026-07-12
- Ran axe-core (WCAG 2.0/2.1 A+AA) + structural mobile checks (390px) over
  9 pages + 2 desktop passes, and a keyboard walk of the reader.
- Found & fixed: 3 critical `aria-required-children` (home devot chips were a
  role-less-children tablist → now `role="group"` with managed `aria-pressed`;
  the discipline More menu button lived inside the tablist → moved beside a
  new inner `.disc-tablist`); horizontal page overflow on mobile /search/
  (tab row now scrolls in place) and /discipline/?tab=memory (mode row wraps);
  tiny tap targets (echo markers 16×9 → ~28×25 effective via a hit-area
  pseudo-element with zero visual change; notification dismiss and keyboard-
  shortcuts buttons padded to ≥32px).
- Clean at close: axe zero violations on all 11 passes, no horizontal
  overflow, skip link + visible focus + logical tab order confirmed. The
  remaining flagged inline prose links (biblepedia refs) fall under the WCAG
  target-size inline exception.

### H5 — Search performance  ·  DONE 2026-07-12
- Verse search fetched all 66 books (several MB) and scanned linearly on every
  query. Now: `tools/build-search-index.mjs` emits a token → verse-id inverted
  index for BSB at build time (14,270 tokens, 26 letter chunks, ~2.1 MB raw,
  never precached), delta-encoded ids in `books.json` order.
- `assets/js/search-index.js` + the indexed path in `search.js`: one ~100 KB
  chunk per query word, substring-compatible token matching (unions every
  token containing the word, so "love" still hits "beloved"), AND-intersection
  for multi-word, phrase verification against real text for quoted queries,
  and text fetched only for the books of the top results (capped at 400
  results / 24 books with an honest "strongest N of M" note).
- Measured: "love one another" 3 chunks + 11 books (was 66); "cloud of
  witnesses" 1 book; anxiety question-kernel 6 books. Non-indexed versions
  (KJV etc.), offline, and dev fall back to the legacy loop automatically;
  the zero-result → Omni handoff (H1a) is preserved.

## Status

- H1a — **DONE** (2026-07-12): question-boilerplate → topic kernel; zero-result
  verse searches hand off to Omni with a note.
- H1b — **DONE** (2026-07-12): 4,674 static answer pages at `/answers/<slug>/`
  (+ letter index at `/answers/`) from Nave's — key verses with BSB text
  resolved at build, hotlinked to the verse modal, full reference list,
  biblepedia cross-links, in the sitemap; Omni topic chips link there.
- H2 — **DONE** (2026-07-12): apparatus rail gained state-aware Commentary /
  Interlinear / Parallels chips mirroring the Study Tools toggles.
- H6 (audit) — **RUN + FIXED** (2026-07-12): audit found 13/16 intents ≤2
  taps; the three offenders — word→lexicon (E), place→map (G),
  person→article (H) — are fixed and verified. **16/16 intents now ≤2 taps.**
- H3 — **DONE** (2026-07-12): `/tour/` walkthrough of John 3:16 through the
  whole chain with live deep links; onboarding tour CTA; sidebar Site Tour.
- H4 — **DONE** (2026-07-12): axe + mobile + keyboard audit; 3 critical ARIA
  violations, 2 mobile overflows, and the tiny-tap-target set all fixed;
  axe clean on all 11 passes.
- H5 — **DONE** (2026-07-12): build-time inverted index for BSB verse search;
  one letter-chunk per query word + top-result book fetches instead of the
  66-book scan; automatic legacy fallback for other versions and offline.

**All Heights phases (H1–H6) are complete.**

## Beyond the Heights — The Desk (Logos-style work surface)

### D1 — Surface v1  ·  DONE 2026-07-13
- `/desk/`: a recursive split layout of panels, each an iframe hosting an
  existing page (framed pages strip their own chrome pre-paint), so multiple
  `/read/` panels give genuinely independent Bible readers. Panels split
  right/down, close, and resize with draggable dividers; the tree drives
  geometry only — panel elements are never reparented (reparenting an iframe
  reloads it). Layout + per-panel URLs persist to localStorage; in-panel
  navigation is tracked same-origin and the page's title names the panel bar.
- Resource chooser per new panel: Bible (with optional passage), Today,
  Search, Biblepedia, Library, Answers, Maps, Timeline, Compare, Original
  Languages, Discipline, Notes.
- Landing: desktop `/` redirects pre-paint to the Desk (default layout =
  Today + Bible); phones keep the daily page; escape hatches `?classic=1`
  and `localStorage bsw_desk_home='0'`. The daily dashboard moved to a
  shared `DailyHome.astro` used by both `/` and the new `/today/` (also the
  Desk's default first panel). Sidebar: Read → The Desk; Practice → Today.
- Narrow screens: `/desk/` stacks panels full-width in tree order.

### D2 — panel linking + cross-resource opens  ·  DONE 2026-07-13
- postMessage protocol (same-origin checked both ways): the Desk announces
  itself to every frame on load (`bsw-desk-hello`, arming `desk-frame.js`
  loaded by core-boot on all pages — no-op outside the Desk).
- **Cross-resource clicks open panels, not replace content.** Inside a
  panel, a link to a different resource (reader → biblepedia article, maps,
  answers, …) posts `bsw-desk-open`: the Desk reuses an existing panel of
  that resource (navigates it + flash outline — the Logos "target panel"
  behavior) or splits the source panel along its longer axis. Same-resource
  navigation (next chapter, another article) stays in-panel; modified
  clicks and external links keep browser behavior.
- **Reader linking.** Bible panels get a 🔗 toggle (persisted). A linked
  reader emits `bsw-desk-nav` on every lookup (reader.js, at the URL
  update); the Desk forwards `bsw-desk-goto` to the other linked readers,
  which follow via the exposed lookup — loop-guarded so linked readers
  don't ping-pong. Each reader keeps its own version → side-by-side
  translation study.

### D3 — maximize, desk-home setting, tooltip → popup  ·  DONE 2026-07-13
- Panel maximize toggle (⛶): the chosen panel takes the whole surface;
  siblings stay mounted (hidden iframes keep their state) until restored.
  Splitting or closing exits maximize. Transient — not persisted.
- Settings → "Home page": "Open the Desk as home on desktop" checkbox wired
  to the `bsw_desk_home` flag the / redirect already honors.
- The reader's place hover-tooltip link now opens the place popup (mini-map,
  article, explorer links) instead of navigating to the maps page; outside
  the reader it stays a maps deep link. (Layout presets skipped per owner.)

### D4 — linked maps follower + drag-to-rearrange  ·  DONE 2026-07-13
- Maps panels join the link set: when a linked reader's chapter finishes
  tagging its places, reader-rail emits the place ids (`bsw-desk-places`,
  re-emitted when late tag passes change the count); the Desk forwards to
  link-toggled maps panels; maps.js drops ring markers on whichever era map
  is showing and fits the view (fly-to for a single place). Verified through
  the full pipeline — Matthew 4 delivers jerusalem/galilee/nazareth/
  capernaum/sea-of-galilee/decapolis/judea to the maps frame.
- Drag-to-rearrange: drag any panel bar onto another panel — the nearest
  edge (left/right/top/bottom half, shown as an accent drop hint) becomes
  the dock side. Drop is pure tree surgery (detach + dock, then relayout),
  so panel iframes never reload mid-rearrange (verified: an in-frame JS
  marker survives the move).

### D5 — compare follower + keyboard shortcuts  ·  DONE 2026-07-13
- Compare panels join the link set: a link-toggled All-Translations panel
  follows a linked reader's navigation (chapter refs land on verse 1) —
  verified John 3:16 filling all 16 version rows on follow.
- Desk shortcuts, working from the surface AND from inside any panel
  (frames forward the combo): Ctrl+Shift+→ split right, Ctrl+Shift+↓ split
  down, Ctrl+Shift+⏎ maximize, Ctrl+Shift+⌫ close. The acted-on panel is
  the one under the pointer / last interacted with; editable fields are
  exempt. Toolbar hint documents them.
- Desk panels also follow live Dark/Light toggles now (storage-event theme
  sync in initTheme — covers other open tabs too).

## Re-evaluation — 2026-07-13

Second outsider pass, same method as the 2026-07-12 evaluation: cold profile,
real browser, natural questions, feature hunting without insider knowledge.
(One regression was caught and fixed during the pass itself: desktop
first-runs landed on the Desk without the welcome card — it rendered inside
the Today panel instead. Framed pages no longer onboard; the Desk does.)

| Dimension | Was | Now | What changed |
|---|---|---|---|
| Content breadth | A | **A** | Unchanged (plus 20 region gazetteer entries) |
| Reading experience | A− | **A** | Every noun is now a hub: word taps (lexeme + highlight), term taps (article), place taps (era-aware map popup) — all quiet until touched |
| Study depth | B+ | **A−** | The Desk: independent readers, linked navigation, compare + maps followers, drag-to-rearrange, shortcuts — genuine parallel study |
| Discovery & search | C | **A−** | Question kernels, Omni fallback, 4,674 answer pages, indexed verse search (1 chunk + top-result books vs 66-book scans) |
| Feature discoverability | C+ | **B+** | Apparatus rail chips, /tour/, onboarding with tour CTA (now on the Desk too), 12-resource panel chooser. Gap: panel linking itself needs a first-use hint |
| Practice loop | B+ | **A−** | Today is the Desk's default first panel — the daily loop sits beside the text instead of behind a nav click |
| Mobile | B− | **B+** | H4 audit: axe clean ×11, overflows fixed, tap targets ≥32px. Desk degrades to a stacked feed — serviceable, not a surface |
| Performance & offline | A− | **A−** | Search is dramatically cheaper; but desk-as-home loads two full pages cold (~2.3 MB uncompressed) — panel weight is the new cost to watch |
| Trust & provenance | A− | **A−** | Unchanged |
| **Work surface** (new) | — | **A−** | Splits, linking, followers, re-dock, maximize, shortcuts, persistence. Gaps: named layouts, per-panel memory cost, no phone surface |

**Overall: B+ → A−.** The two C-grade failures that defined the first
evaluation — a stranger's first question dead-ending, and the depth hiding
behind popovers — are gone, and the site now has a work surface none of the
free competitors have. What separates it from an A: mobile is corrected
rather than designed-for, desk panel weight (each panel is a full page),
linking discoverability, and search ranking still being literal-match.

## The A gaps — plan (2026-07-13)

The four items between A− and A, ordered smallest to largest so each ships
on its own:

### A1 — Frame-lite panels  ·  panel weight
Every Desk panel boots like a standalone visit: it registers the service
worker, injects PWA meta, and fires the 66-book precache message — per
panel. Framed pages skip the PWA layer (registration, manifest/meta
injection, precache trigger) and the history widget; the host page owns
those. Measure the request/byte delta on a cold two-panel desk landing.

### A2 — Linking discoverability  ·  the 🔗 needs a first use
When the Desk first holds two or more linkable panels and none is linked,
show a one-time dismissible hint anchored at the link toggle ("Link panels
so they navigate together"). Dismissal (or first use of 🔗) persists.

### A3 — Search stemming + synonyms  ·  literal-match ranking
Query-side stemming over the existing index: a query word also matches
tokens sharing its stem (light suffix stripping: s/es/ed/ing/ly), weighted
between exact and prefix — "loving" finds "love". Plus a small curated
synonym table for common study queries (anxiety→worry/anxious/cares,
money→riches/wealth/mammon, …) applied as OR-expansions with a note in the
results. No index rebuild required.

### A4 — A phone surface, not a stack  ·  mobile designed-for
The Desk on a phone becomes one panel at a time with a bottom tab strip
(panel titles as tabs; swipe or tap to switch; add/close from a sheet).
The layout tree is shared with desktop — only the presentation differs.
Follow with a phone pass over the tour and answers pages.

- A1 — **DONE** (2026-07-13): framed pages skip the PWA layer + history widget; cold two-panel desk landing dropped 2,291 KB → 424 KB (−82%).
- A2 — **DONE** (2026-07-13): one-time 🔗 hint when two linkable panels exist and none is linked; retires on dismiss or first link.
- A3 — **DONE** (2026-07-13): query-side stemming ("loving" → 631 matches incl. love/loved) weighted between exact and prefix; 18-entry synonym table OR-expands (anxiety → anxious/worry/worried/cares, 106 matches) with an "Also searched related words" note.
- A4 — **DONE** (2026-07-13): narrow Desk is one panel + a bottom tab strip; panels lazy-build on first tab tap and stay mounted after (state kept); add/split focus the new chooser tab.
