# Bible Study Website — Deferred & Long-Term Work

Items here are intentionally excluded from the day-to-day loop agent. They fall into three categories:
- **Z** — Ongoing multi-session agent generation work (MKT commentary suite)
- **O** — Deferred / out-of-scope for a personal static site
- **Blocked** — Data or copyright issues with no current resolution path

Active bugs and short-cycle improvements belong in `working/TODO.md`.

---

## Z4–Z8 MKT Commentary Suite

**Goal:** Three original verse-by-verse commentaries for all 66 books, an echo/fulfillment data layer, and a key-term concordance. Uses the same static script + guide + work queue pattern as the MKT translation.

**Commentaries:**
- **Z6 `mkt-original`** — Original Language: why each translation choice, what English misses (aspect, idiom, wordplay, semantic range, honor-shame, tense)
- **Z7 `mkt-context`** — Historical Context: what the original audience understood, ANE/Second Temple background, intertextual echoes
- **Z8 `mkt-christ`** — "Christ in Every Verse": types, shadows, fulfillments, prophecy — honest about directness (direct/type/shadow/theme/revelation of God)

### Infrastructure

- [x] `Z_COMMENTARY_SCRIPT_GUIDE.md` — static script boilerplate, HTML conventions, source data checklist
- [x] `Z_COMMENTARY_AGENT_GUIDE.md` — content principles and length targets for all three commentary types
- [x] `Z_PROGRESS.md` — full work queue (66 books × 3 commentaries + echo layer)
- [x] `Z_AGENT_PROMPT.md` — paste prompt for agent sessions

### Z4 — Echo & Fulfillment Data Layer

**Note: Echoes replace Parallels.** The existing parallels feature (`data/parallels/`, `loadParallels()`, the parallels panel) was the prototype. Once Z4 absorption is complete, the parallels panel in the reader is replaced by the Echoes & Fulfillments panel and `loadParallels()` is retired.

**Parallels absorption (do before retiring parallels.js):**
- [ ] Audit `data/parallels/` — review all entries for the books being processed
- [ ] Absorb `prophecy-source` entries → echo type `fulfillment`; `quotation` → `quote`; `parallel` → `theme` or `allusion` where substantive
- [ ] Add the `note` field that parallels entries lack (a brief argument for the connection)
- [ ] Document the absorption step in `Z_COMMENTARY_SCRIPT_GUIDE.md`

**Build status:**
- [ ] Echo script units added to `Z_PROGRESS.md` work queue
- [x] `assets/js/core.js` — `ECHOES_ROOT`, `loadEchoes()`, `echoesCache` implemented; `loadParallels()` retained in `parallels.js` pending full absorption
- [x] `assets/js/verse-study.js` — "Echoes & Fulfillments" panel implemented with type badges and `.ref` links
- [ ] `assets/js/reader.js` — still imports `loadParallels()` from `parallels.js`; replace with echoes once absorption is complete
- [x] `data/echoes/` — all 66 books generated

Echo types: `quote` | `allusion` | `type` | `shadow` | `theme` | `fulfillment`

### Z5 — Key Term Decision Commentary

*(Not started — `data/translation/term-commentary.json` does not yet exist)*

- [ ] `scripts/z5-terms-greek.py` — hardcoded decision notes for all Greek dispute_level≥2 terms (~60 entries)
- [ ] `scripts/z5-terms-hebrew.py` — Hebrew dispute_level≥2 terms (~40 entries)
- [ ] `data/translation/term-commentary.json` — output with lemma, decision_note HTML, key_verses, tradition_map
- [ ] `tools/terms/index.html` — searchable concordance page (tg-* CSS layout; left list, right panel)

### Z6–Z8 — Commentary Data Generation

- [x] `assets/js/core.js` — 3 entries added to `COMMENTARY_SOURCES`: `mkt-original`, `mkt-context`, `mkt-christ`
- [ ] Agents generate `data/commentary/mkt-original/{book}.json` — NT first, start John + Romans (ongoing via `Z_PROGRESS.md`)
- [ ] Agents generate `data/commentary/mkt-context/{book}.json` — NT first (ongoing)
- [ ] Agents generate `data/commentary/mkt-christ/{book}.json` — NT first (ongoing)

### Script naming convention
`scripts/zc-{type}-{book}-{start}-{end}.py`
Examples: `zc-original-john-1-5.py`, `zc-context-romans-1-8.py`, `zc-christ-genesis-1-10.py`, `zc-echo-john-1-5.py`

### Verification
- verse-study John 3:16 → all 3 new MKT sources in commentary picker
- verse-study John 1:29 → Echoes panel shows Exod 12 type + Isa 53:7 allusion
- `tools/terms/index.html` → G4102 πίστις decision note with tradition map
- No regressions: existing commentaries (mhcc, jfb, etc.) still load

### MKT Translation (NT continuation)
Track in `working/MKT_PROGRESS.md` and `Z_PROGRESS.md`. Agent sessions use `MKT_AGENT_PROMPT.md`.

---

## Translation Workshop — WS-G

### WS-G · Curated semantic-range descriptions for top-100 disputed/high-use terms *(LOW — agent task)*

**Why:** The current `semantic_range` field is generated from the Strong's `def` field — same text, relabeled. For the 100 most significant terms (Phase 1 + Phase 5 sets), the range should be a curated synthesis: what do all sources agree on, where do they diverge, and what does the corpus evidence show?

**Prerequisites:** WS-A–F complete (see archive).

**Tasks:**
- [ ] Design the agent prompt for curated range writing (reads: dodson + thayer + abbott-smith + attested uses → writes: `semantic_range` as 2-3 sentence synthesis)
- [ ] Agent pass: curate `semantic_range` for all Phase 1 Greek entries (200 entries)
- [ ] Agent pass: curate `semantic_range` for all Phase 2 Hebrew entries (200 entries)
- [ ] Agent pass: curate `semantic_range` for Phase 5 contested terms (17 entries — highest priority)
- [ ] `apply-decisions.py` — extend to support `semantic_range` field updates

---

## Data Blocked

These items cannot proceed until an external data source becomes available or a workaround is found.

### WD-M — LXX Bridge for Hebrew–Greek Links
Hebrew lemmas often have a canonical LXX Greek equivalent (e.g. H2617 חֶסֶד → G1656 ἔλεος). This connection is invisible on the current word study page.
- **Blocked:** `strongs` JSON has no `lxx`/`greek_equiv` field. Needs sourcing from openscriptures/strongs dataset before any JS implementation.

### REF-E — Gill's Commentary
John Gill's *Exposition of the Old and New Testaments* (1746–1763) would be a valuable addition as an older Reformed commentary with verse-by-verse OT coverage.
- **Blocked:** `Gill.zip` not in CrossWire rawzip or mods.d. No other clean, machine-readable public-domain source identified.

---

## Copyright / Availability Blocked

These items have been researched; no public-domain or freely-licensed text is available.

### Library Documents

- **Melanchthon, *Loci Communes* (1521)** — All English translations (Hill 1944, Manschreck 1965) are under copyright. No pre-1928 English translation exists.
- **Vatican II** (*Lumen Gentium*, *Dei Verbum*, *Sacrosanctum Concilium*) — The official Holy See English translations are freely available online but copyright status for redistribution is unclear.
- **Constantinople IV / Photian Council (879–880)** — No clear public-domain English translation available.
- **Hesychast Councils (1341, 1347, 1351)** — No standard public-domain English text identified.
- **Council of Jassy (1642)** / *Confession of Peter Mogila* — Availability unclear.

---

## Phase O — Long-term / Out-of-Scope

These items have been identified but are intentionally deferred. They require significant research, have unclear scope, or are likely out of scope for a personal static-site project. None should be started without deliberate re-evaluation.

- [ ] **O1. Audio support for memory verses**
  TTS integration or royalty-free audio recordings for Scripture memory so verses can be heard while commuting. No clear path on a static site without a TTS API dependency.

- [ ] **O3. MKT print / ePub edition**
  Generating a full three-tier MKT as a downloadable PDF or ePub. Significant formatting work; unclear demand for a personal study tool.

- [ ] **O4. Social sharing beyond verse image cards**
  Shareable verse links, QR codes, and embed codes. May belong here if the site remains personal, or as a later feature if broader readership becomes a goal.

- [ ] **O5. `bible.js` unit test suite**
  Jest or Vitest test suite for core functions (ref parsing, search, modal logic, localStorage handling). Low urgency while the site has one author who can manually verify. Revisit if contributors are added.

- [ ] **O6. Internationalisation of UI chrome**
  All button labels, headings, and status messages are hardcoded English. i18n requires a locale file system and ongoing translation maintenance.
