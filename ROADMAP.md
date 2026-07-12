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
- H3 — pending
- H4 — pending
- H5 — pending
