# Original-Language Decomposition — Architectural Plan

Directive (owner, 2026-07-13): the Translation Workshop "needs to be turned
into a tab for the study desk … deeper original language tools, insights,
etc as a desk link from interlinear button clicks or a verse reader lock …
the decomposed original study tool may be individual tab types."

Goal: the workshop dissolves into **individually linkable desk panel
types**. The standalone page becomes a thin launcher (or retires outright,
like /verse-study/ did). Every OL surface is reachable two ways: an
interlinear/word click opens it as a desk panel seeded with that word, or a
🔗 verse-lock follows the linked reader.

---

## 1 · What the workshop is today (code inventory)

`assets/js/workshop.js` — 5,606 lines, one module, shared mutable state
(`st`), three modes plus five side systems:

| Surface | What it renders | Data it pulls |
|---|---|---|
| **Verse Study** mode | passage tiles (interlinear) + 8 insight tabs: Literary, Cultural, Intertextual, Synthesis, Cross-refs, Commentary, Grammar, Word | interlinear, strongs, crossrefs, commentary, idioms index, curated passage notes |
| **Word Study** mode | the lexical dossier: grammar section, tiers view, attested uses, extrabiblical uses, LXX bridge, book distribution, cognate family, author frequency | strongs, lexicons (Thayer/BDB), vocab tiers, author-freq, cognates, refs |
| **Book Study** mode | book-level OL overview | book meta, freq data |
| Dashboard | review-progress wall ("GREEK REVIEWED n of 5,523") | localStorage review state |
| Flashcards | vocabulary SRS review | vocab tiers + localStorage |
| Primer | grammar primer chapters | static primer content |
| Translation mode | per-verse translation decisions, import/export JSON | localStorage decisions |
| Queue | word review queue | localStorage |

Already done (P19): the workshop page is a desk resource ("Original
Languages"), is 🔗-linkable, and follows the linked reader's navigation
(`bsw:desk-goto` → `_studyPassage`). Interlinear-popover and strongs-banner
links already open it as a panel via the desk's cross-resource
interception.

## 2 · Target shape — the individual tab types

Three desk resource types replace the monolith. Each is a small page that
strips to content in a frame (the existing embed bootstrap), loads only its
own module, and understands desk link messages.

### `ol-verse` — Original Language Verse  (route: `/ol/verse/?ref=`)
The Verse Study mode extracted: interlinear tile row for the verse + the
insight tabs (Literary / Cultural / Intertextual / Synthesis / Grammar).
Cross-refs and Commentary tabs are DROPPED here — the reader's own
apparatus and side panels already own those jobs; duplicating them in an OL
panel was workshop bloat.
- **Verse lock**: follows `bsw:desk-goto` from a linked reader (same
  contract as compare/workshop today), landing on verse 1 of the chapter
  with prev/next verse controls.
- Tile click → sends the word to a linked `ol-word` panel (see message
  below) or opens the dossier inline if none is linked.

### `ol-word` — Word Dossier  (route: `/ol/word/?s=`)
The Word Study mode extracted: full dossier (lemma header, grammar, senses/
tiers, attested + extrabiblical uses, LXX bridge, book distribution,
cognate family).
- **Word lock** (new): a linked `ol-word` panel live-updates when the user
  taps a word in a linked reader (word-tap popover), clicks an interlinear
  tile, or clicks a tile in a linked `ol-verse` panel.
- New desk message: `bsw-desk-word { code, lang }`, emitted by
  reader-wordtap / interlinear / ol-verse via desk-frame.js; the desk
  forwards it to link-toggled `ol-word` panels exactly like
  `bsw-desk-places` routes to maps. Unlinked fallback: the click opens a
  new `ol-word` panel via the normal cross-resource interception.

### `ol-translate` — Translation Bench  (route: `/ol/translate/?ref=`, LAST)
Translation mode + its decisions store, import/export. Kept because the
data (user decisions in localStorage) must stay reachable, but extracted
last and only if still wanted — it is the least-used surface.

### Retire / fold
- **Dashboard, Queue**: retire. Their only job (progress motivation) moves
  to a one-line "n words reviewed" chip in `ol-word`'s empty state.
- **Flashcards**: move behind a chip on the Discipline page (it is a
  practice habit, not a study surface). Own decision point at Phase 4.
- **Primer**: becomes a static /ol/primer/ page linked from `ol-verse`'s
  Grammar tab. No JS beyond the shell.
- **/translation/workshop/**: after Phases 1–3, becomes a redirect to
  `/ol/word/` (preserving `?s=` and `?ref=` params → the matching new
  route) so every existing deep link keeps working.

## 2b · Also in scope (owner directive, 2026-07-14): the reader's Study tab

The reader's Passage Study Desk (study-desk.js — the drawer with the
Passage / Synth / Comm. / Voices / Word / Vers. / Places / Pedia / Book
binder rail) decomposes the same way: each binder blade is a candidate
desk panel type that follows a linked reader instead of living inside the
reader's own drawer. Sequencing: AFTER the workshop phases below, because
the blades share renderers with `ol-word`/`ol-verse` once those exist
(the Word blade IS the dossier; the Vers. blade IS compare; Places is the
maps follower that already exists). Expected outcome: the in-reader drawer
stays for phones/single-window use; on the Desk, each blade is a panel.

## 3 · Phases

### Phase 1 — carve seams inside the monolith (no behavior change)
Split workshop.js into modules along the lines it already has:
- `assets/js/ol-data.js` — every loader/cache (`_loadTiers`,
  `_loadAuthorFreq`, `_loadIdioms`, cognates, refs). Pure functions +
  module caches; imported by everything else.
- `assets/js/ol-dossier.js` — `_renderDossier`, `_renderGrammarSection`,
  `_renderTiersView`, `_renderAttestedUses`, `_renderExtrabib`,
  `_renderLxxBridge`, `_renderBookDistribution`, cognate renderers.
  Signature: `renderDossier(code, lang, hostEl, opts)`.
- `assets/js/ol-verse.js` — passage tiles + insight-tab renderers.
  Signature: `renderVersePanel(ref, hostEl, opts)`.
- `workshop.js` keeps the shell, modes, dashboard, flashcards, translation
  state — importing the three new modules.
Gate: build passes, workshop behaves identically, bundle graph shows the
three chunks shared.

### Phase 2 — the two new pages + desk registration
Strangler-fig start (2026-07-14): the /ol/word/ and /ol/verse/ routes ship
FIRST as thin facades over the existing workshop module — a solo flag
(path-derived) hides the mode bar/dashboard/advanced chrome and boots the
right mode; the desk word-lock message lands end-to-end. The module split
underneath (ol-dossier.js etc.) then proceeds without route churn.
- `src/pages/ol/word/index.astro` (entry `ol-word`) and
  `src/pages/ol/verse/index.astro` (entry `ol-verse`): minimal chrome, one
  host element, boot calls the Phase-1 module directly. No dashboard, no
  queue, no mode bar.
- desk.js RESOURCES gains `{ k:'olword', label:'Word Dossier', url:'/ol/word/' }`
  and `{ k:'olverse', label:'OL Verse', url:'/ol/verse/' }`; both join
  LINKABLE and the goto-forward filter; `resourcePrefix` 'ol' handling
  (both share the prefix → same-prefix panel reuse groups them, which is
  correct: an OL click reuses an existing OL panel).
- `bsw-desk-word` message wired end-to-end (desk-frame emit → desk forward
  → ol-word applies). reader-wordtap's "Full word study" action and the
  interlinear popover's desk button emit it when linked panels exist.
Gate: bible + ol-verse + ol-word three-panel desk works fully linked —
navigate chapter → ol-verse follows; tap word → ol-word follows.

### Phase 3 — reroute every entry point
- Interlinear popover, strongs banner "Workshop →", study-desk word blade
  "Open in Translation Workshop →" → `/ol/word/?s=`.
- Search explore Strong's cards keep pointing at `/read/?strongs=`
  (occurrence browsing) — the reader remains the occurrences surface;
  `ol-word` is the dossier surface. The strongs banner links to BOTH.
- Sidebar Tools: "Original Language Study" stays on the FULL app until
  Phase 4 executes the flashcards/primer/translation-mode decisions —
  redirecting it now would orphan those modes (deviation from the original
  Phase 3 text, recorded 2026-07-14).
Gate: no in-app link targets /translation/workshop/ except the redirect.

### Phase 4 — retire the monolith
Owner decisions (2026-07-14):
(a) Flashcards live in the WORD TAB (button moved from the topbar into the
    word-mode header, so /ol/word/ panels carry it) and stay visible from
    Disciplines — Memory → Original Language already reads the same deck
    (bsw_ws_fc_deck), and now links "🄯 Flashcards →" (/ol/word/?fc=1,
    which boots straight into review).
(b) Dashboard + review queue: RETIRED.
(c) Translation mode: RETIRED (the ⚙ advanced panel is gone; dashboard,
    queue, and primer were translation-mode phases, so they retire with
    it). Stored decisions (localStorage) remain untouched.
(d) Book Study mode: retires from the OL app; its content concept folds
    into the §2b study-blade decomposition (the reader's Book blade).

Phase 4a (shipped): decisions applied — flashcards relocated + ?fc=1 deep
link, translation chrome removed with guards, sidebar → /ol/word/.
Phase 4b (remaining): /translation/workshop/ → param-preserving redirect;
purge the dead translation/dashboard/queue/primer code from workshop.js;
decide where primer content resurfaces (candidate: ol-verse Grammar tab).
- /translation/workshop/ → param-preserving redirect page.
- Dashboard/queue code deleted; flashcards decision executed; primer
  extracted; dead loaders pruned from workshop.js until nothing imports it
  and the file is removed.
- sw precache and AUDIT/ROADMAP notes updated.
Gate: `grep -rn "workshop" assets src` returns only the redirect + history.

## 4 · Contracts to hold through all phases

- **Deep links keep working**: `?s=CODE` and `?ref=REF` never break —
  Phase 4's redirect maps them onto the new routes.
- **Translation decisions data**: localStorage keys owned by translation
  mode are untouched until `ol-translate` exists; export/import must ship
  in the same phase that moves the UI.
- **Desk message protocol**: additions only (`bsw-desk-word`); existing
  types unchanged. Same-origin checks on both ends, like every existing
  handler.
- **Frame-lite**: both new entries skip PWA/history-widget init in frames
  (the core-boot `_framed` path already does this for free).
- **One era of naming**: user-facing label is "Original Languages"; "Word
  Dossier" and "OL Verse" are the panel names; the word "workshop"
  disappears from UI.

## 5 · Risks

- workshop.js's shared `st` object couples modes; Phase 1 must pass state
  explicitly into the extracted renderers (host element + options), not
  export `st`.
- The insight tabs (Literary/Cultural/…) read curated per-passage JSON that
  may be sparse; ol-verse needs honest empty states, not blank panes.
- Panel reuse by prefix means an `ol-verse` click could reuse an `ol-word`
  panel (both prefix 'ol'); if that feels wrong in practice, key reuse by
  full resource url instead (small desk.js change, noted here so it isn't
  rediscovered).
- Bundle: three new entries must not re-duplicate the big data loaders —
  Phase 1's ol-data.js is what prevents that.
