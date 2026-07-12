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

### H3 — First-run demonstration
- The onboarding names 4 features; the site has 15, and the *chain*
  (verse → modal → connections → word study → article) is the product.
- MVP: a "See everything on one verse" card in onboarding + a `/tour/` page
  that walks John 3:16 through the whole chain with deep links.

### H4 — Mobile & accessibility audit
- Dedicated phone pass over reader, library browser, discipline hub, search
  (biblepedia was fixed reactively; the rest never had one).
- axe-core automated pass + keyboard walk of the main flows; fix what it finds.

### H5 — Search performance
- Verse search fetches whole books in loops; fine on broadband, sluggish on
  phones. Build-time compact index (stem → refs) served as static JSON chunks.
- Defer until H1 proves what queries actually look like.

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
- H3 — pending
- H4 — pending
- H5 — pending
