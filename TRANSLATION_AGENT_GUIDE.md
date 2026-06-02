# MKT Translation — Agent Reference Guide

This document is designed to be handed to a Claude Code agent as context. It describes the **Modern Kingdom Translation (MKT)** project's data model, file layout, and conventions so that multiple agents can work simultaneously without stepping on each other.

---

## 1. What This Project Is

An original English Bible translation produced directly from the Hebrew (WLC/BHS) and Greek (SBLGNT/NA28) texts, packaged as static JSON files served by a GitHub Pages website. No build step; no bundler. All files are plain JSON or HTML.

The translation has **three tiers per verse**, derived from lemma-level glossary decisions:

| Tier | Key | Goal |
|------|-----|------|
| Literal | `L` / `lit` | Word-for-word, preserves source syntax and word order |
| Mediating | `M` / `med` | Natural English sentence flow, accurate primary glossary renderings |
| Thought | `T` / `tho` | Meaning-driven; idioms rendered as meaning, poetry with cadence |

---

## 2. Directory Map

```
data/
  interlinear/        Raw source: one file per book, Strongs tokens per verse
  translation/
    glossary-greek.json       5,523 Greek lemma entries
    glossary-hebrew.json      8,674 Hebrew lemma entries
    glossary-phrases-greek.json   (empty — reserved for phrase idioms)
    glossary-phrases-hebrew.json  (empty — reserved)
    index-greek.json          Slim index of all Greek entries (phase bundle for "All Greek" tab)
    index-hebrew.json         Slim index of all Hebrew entries
    phase1.json               Top 200 NT Greek by frequency (with full source_data)
    phase2.json               Top 200 OT Hebrew by frequency (with full source_data)
    phase5.json               Contested terms sorted by dispute_level
    draft/
      literal/        {book}.json  → { "ch": { "v": "verse text" } }
      mediating/      {book}.json
      thought/        {book}.json
    notes/            {book}.json  → { "ch": { "v": { tokens, flags, div, struct, [reasoning] } } }
scripts/
  translate-with-claude.py   Main AI translation driver (reads interlinear + glossary, calls Claude)
  apply-decisions.py         Merges workshop export → glossary-*.json
  seed-glossary.py           Rebuilds phase bundles from glossary files
  mkt-genesis-1-10.py        Manual initial draft Genesis 1–10 (static data, no API)
  mkt-genesis-11-20.py       Manual initial draft Genesis 11–20
  mkt-john-1-5.py            Manual initial draft John 1–5
  mkt-john-6-10.py           Manual initial draft John 6–10
  mkt-john-11-15.py          Manual initial draft John 11–15
  mkt-john-16-21.py          Manual initial draft John 16–21
translation/workshop/index.html   Browser UI for reviewing lemma decisions
```

---

## 3. Data Schemas

### 3a. Interlinear token (source data)

**File:** `data/interlinear/{book}.json`

```json
{
  "1": {
    "1": [
      { "s": "G746", "text": "the beginning" },
      { "s": "G1722", "text": "In" }
    ]
  }
}
```

- `s`: Strong's code (`G####` = Greek, `H####` = Hebrew)
- `text`: the English surface text from the base translation at that token position

### 3b. Glossary entry

**File:** `data/translation/glossary-greek.json` or `glossary-hebrew.json`

```json
{
  "G3056": {
    "lemma": "λόγος",
    "translit": "lógos",
    "pos": "noun",
    "domain": [],
    "dispute_level": 4,
    "status": "draft",
    "nt_freq": 330,
    "ot_freq": 0,
    "tiers": {
      "literal":   { "primary": "Word",  "notes": null },
      "mediating": { "primary": "Word",  "notes": null },
      "thought":   { "primary": "Word",  "notes": null }
    },
    "context_overrides": [
      {
        "condition": "In John 1 Prologue",
        "literal":   "Word",
        "mediating": "Word",
        "thought":   "Word"
      }
    ],
    "semantic_range": "a word, what someone has said; also Reason/Logic in Greek philosophy",
    "source_data": {
      "dodson": { "gloss": "...", "def": "...", "deriv": "..." },
      "thayer":  { "short": "...", "long": "..." },
      "hebrew":  { "gloss": "", "def": "", "deriv": "" },
      "bdb":     { "short": "", "long": "" }
    },
    "user_notes": "",
    "decision_log": [
      { "action": "confirmed", "date": "2026-06-01", "note": "Accepted proposed renderings" }
    ]
  }
}
```

**Status values** (in order of review lifecycle):

| Status | Meaning |
|--------|---------|
| `draft` | No decision yet — initial seed value |
| `confirmed` | Accepted proposed renderings as-is |
| `override` | Accepted with manually corrected tier values |
| `disputed` | Flagged as needing more research |
| `deferred` | Skipped for later |
| `locked` | Final — will not change |

### 3c. Draft verse file

**File:** `data/translation/draft/{tier}/{book}.json`

```json
{ "1": { "1": "In the beginning was the Word, and the Word was with God, and the Word was God." } }
```

Chapter keys and verse keys are **strings** of the chapter/verse number.

### 3d. Notes file

**File:** `data/translation/notes/{book}.json`

Currently stores interlinear token context (written by `generate-notes.py`). When `translate-with-claude.py` runs, it merges in a `reasoning` key per verse:

```json
{
  "1": {
    "1": {
      "tokens": [ { "code": "G746", "text": "beginning", "lemma": "ἀρχή", ... } ],
      "flags": [],
      "div": null,
      "struct": null,
      "reasoning": {
        "structure": "A triadic chiasm: Word–God, Word with God, Word is God.",
        "decisions": [
          "λόγος rendered 'Word' (not 'Reason') — John activates both Greek and OT registers simultaneously.",
          "Anarthrous θεός in clause 3 is qualitative (Colwell), not indefinite."
        ],
        "key_terms": [
          { "code": "G3056", "word": "λόγος", "note": "Evokes Stoic Logos, OT Wisdom/dabar, and Genesis 1 simultaneously." }
        ]
      }
    }
  }
}
```

---

## 4. Current Status (as of 2026-06-01)

**Primary progress tracker:** `MKT_PROGRESS.md` at the repo root. It lists every book with chapter counts, verse counts, and script references. Update it whenever a new book or chapter range is completed.


### Hand-translated books (real 3-tier content in draft files)

| Book | Language | Chapters | Method |
|------|----------|----------|--------|
| Genesis | Hebrew | 1–36 (of 50) | Static scripts — hand-authored data |
| John | Greek | 1–21 (all) | Static scripts — hand-authored data |
| Matthew | Greek | 1–28 (all) | Static scripts — hand-authored data |
| Mark | Greek | 1–16 (all) | Static scripts — hand-authored data |
| Romans | Greek | 1–16 (all) | Static scripts — hand-authored data |
| Philippians | Greek | 1–4 (all) | mkt-phase3 |
| Colossians | Greek | 1–4 (all) | mkt-phase3 |
| Titus | Greek | 1–3 (all) | mkt-phase2 |
| 2 Thessalonians | Greek | 1–3 (all) | mkt-phase2 |
| 2 Peter | Greek | 1–3 (all) | mkt-phase2 |
| Philemon | Greek | 1 (all) | mkt-phase1 |
| 2 John | Greek | 1 (all) | mkt-phase1 |
| 3 John | Greek | 1 (all) | mkt-phase1 |
| Jude | Greek | 1 (all) | mkt-phase1 |
| Acts | Greek | 1–10 (of 28) | mkt-acts-1-5, mkt-acts-6-10 |

### Untranslated (draft files are empty `{}`)

All 51 remaining books — both OT and NT — have empty draft files as of 2026-06-01. The word-salad placeholder text that was previously auto-populated from interlinear tokens has been wiped.

**Partial gaps in hand-translated books:**
- Genesis chapters 37–50 — wiped; needs new static scripts or `translate-with-claude.py`
- Acts chapters 11–28 — wiped; needs `translate-with-claude.py`

### Scripts written but not yet run

Two static scripts have full hardcoded translations and just need to be executed:

```bash
python3 scripts/mkt-phase4.py     # Galatians + Ephesians (all chapters)
python3 scripts/mkt-luke-1-6.py   # Luke chapters 1–6
```

Running these is instant (no API calls).

### Key facts

- **`translate-with-claude.py` has never been run.** It is the intended path for AI-assisted translation of remaining books.
- **Glossary decisions: 0 confirmed** — all 5,523 Greek and 8,674 Hebrew entries are still `draft`. The glossary decisions workshop is the next priority before running the AI translator.
- **Notes:** All verses have interlinear token data in `notes/`. No verse has a `reasoning` key — that key is only written by `translate-with-claude.py`.

---

## 5. Translation Principles (Summary for Agents)

These are baked into `translate-with-claude.py`'s system prompt and must be respected whenever writing or revising translation text:

1. **Greek verb aspect over tense.** Aorist = single complete act. Present = ongoing. Perfect = past act, lasting present result ("it stands written").
2. **Hebrew aspect over tense.** Perfect = complete; Imperfect = ongoing/potential. Waw-consecutive imperfect = narrative past.
3. **Polysemy is normal.** σάρξ, πνεῦμα, νόμος each have multiple valid renderings; context and tier determine the choice. Do not force one English word.
4. **Divine passive.** Jewish passive verbs often imply God as unnamed agent — note this.
5. **Honour-shame culture.** Patron-client, shame/vindication dynamics often underlie vocabulary choices.
6. **OT intertextuality.** Deliberate OT echoes in NT texts carry theological weight; mark them.
7. **Do not flatten Hebrew poetry.** Parallelism is meaningful. Preserve line structure in poetic books.
8. **Greek articles.** Anarthrous nouns are not automatically indefinite. Apply Colwell's rule, qualitative use, and Granville Sharp explicitly.

---

## 6. Contested Terms to Handle With Care

These terms appear in Genesis and/or John and have `dispute_level >= 3`. Any agent writing or revising translations involving them must make an explicit choice and note it:

### Greek (John)

| Code | Lemma | Primary gloss | Issue |
|------|-------|---------------|-------|
| G3056 | λόγος | Word | John 1 evokes Greek Logos + OT Wisdom + Hebrew dabar simultaneously |
| G4102 | πίστις | faith | "Faith of Christ" may be Christ's own faithfulness, not just trust in him |
| G4561 | σάρξ | flesh | Physical body in John 1:14; fallen human nature in other contexts — do not collapse |
| G166 | αἰώνιος | eternal | May denote quality of age-to-come life rather than infinite duration |
| G4151 | πνεῦμα | Spirit | Capitalisation is a theological decision; Greek has no capitals |
| G26 | ἀγάπη | love | Willed, covenantal, self-giving — distinct from φιλία and ἔρως |
| G1343 | δικαιοσύνη | righteousness | Whether given quality or declared legal status shaped the Reformation |

### Hebrew (Genesis)

| Code | Lemma | Primary gloss | Issue |
|------|-------|---------------|-------|
| H3068 | יהוה | LORD | The divine personal name; "LORD" (small-caps) hides it |
| H430 | אֱלֹהִים | God | Grammatically plural; context determines sense |
| H7307 | רוּחַ | Spirit | Spirit / wind / breath — all attested in Gen 1:2; ambiguity may be intentional |
| H2617 | חֶסֶד | steadfast love | No English equivalent; covenant loyalty + active kindness combined |
| H5315 | נֶפֶשׁ | soul | Embodied self, not Greek immaterial soul |
| H1285 | בְּרִית | covenant | Formal, oath-bound, legally structured relationship |

---

## 7. Key Scripts Reference

### `mkt-{book}-{range}.py` — Static draft scripts (used for Genesis and John)

These scripts are how the existing Genesis and John drafts were produced. Each file contains the full three-tier translation **hardcoded as a Python dictionary** and writes it directly to the draft JSON files. No API calls, no glossary lookups — pure data.

```bash
# Genesis (two scripts covering chapters 1–20; 21–50 have no static scripts yet)
python3 scripts/mkt-genesis-1-10.py
python3 scripts/mkt-genesis-11-20.py

# John (four scripts)
python3 scripts/mkt-john-1-5.py
python3 scripts/mkt-john-6-10.py
python3 scripts/mkt-john-11-15.py
python3 scripts/mkt-john-16-21.py
```

**Writes:**
- `data/translation/draft/literal/{book}.json`
- `data/translation/draft/mediating/{book}.json`
- `data/translation/draft/thought/{book}.json`

**Does not write notes/reasoning.** Token data in `notes/` was generated separately by `generate-notes.py`.

---

### `translate-with-claude.py` — AI translation driver (not yet used)

This script is the intended path for translating additional books. It makes Claude API calls per chapter, reading the interlinear data and glossary decisions, and returns all three tiers plus structured reasoning notes.

**It has not been run on any book yet.** Genesis and John predate it; they were produced by the static scripts above.

```bash
# Single chapter (fast, good for targeted work)
python3 scripts/translate-with-claude.py --book john --chapter 1

# Whole book (safe to resume — skips already-done chapters)
python3 scripts/translate-with-claude.py --book genesis

# Re-translate already-done chapters
python3 scripts/translate-with-claude.py --book john --overwrite

# Different model
python3 scripts/translate-with-claude.py --book john --model claude-opus-4-8
```

**Reads:**
- `data/interlinear/{book}.json` (source tokens)
- `data/translation/glossary-{greek,hebrew}.json` (lemma decisions)

**Writes:**
- `data/translation/draft/literal/{book}.json`
- `data/translation/draft/mediating/{book}.json`
- `data/translation/draft/thought/{book}.json`
- `data/translation/notes/{book}.json` (adds `reasoning` key per verse, merges with existing token data)

**Safe to resume** — existing chapters are skipped unless `--overwrite` is passed.

### `apply-decisions.py` — Merge workshop export to glossary

```bash
# Dry run first to see what will change
python3 scripts/apply-decisions.py mkt-decisions-2026-06-01.json --dry-run

# Apply
python3 scripts/apply-decisions.py mkt-decisions-2026-06-01.json
```

**Workflow:** Workshop UI → "Export JSON" button → run this script → run `seed-glossary.py`.

### `seed-glossary.py` — Rebuild phase bundles

Run after applying decisions to update the phase JSON files the workshop UI loads.

```bash
python3 scripts/seed-glossary.py
```

---

## 8. Multi-Agent Parallelism Rules

### Safe to parallelize (no file conflicts)

| Task | Files written | Parallel-safe with |
|------|--------------|-------------------|
| Translate Genesis chapters 1–25 | `draft/*/genesis.json`, `notes/genesis.json` | Translate John chapters |
| Translate John chapters | `draft/*/john.json`, `notes/john.json` | Translate Genesis chapters |
| Translate any other book (Romans, Psalms…) | `draft/*/{book}.json`, `notes/{book}.json` | Any other book |
| Review Genesis translation quality | reads only | Any write task on other books |

### Must serialize (would cause file conflicts)

| Conflict | Reason |
|----------|--------|
| Two agents translating same book simultaneously | Both write `draft/*/genesis.json` → last writer wins, earlier work lost |
| `translate-with-claude.py` + `apply-decisions.py` | Both read/write `glossary-*.json` |
| `apply-decisions.py` + `seed-glossary.py` | `seed-glossary.py` reads glossary files that `apply-decisions.py` is mid-write |

### Chapter-level split for Genesis

Genesis is 50 chapters. **Chapters 1–36 already have real translations** (static scripts). Chapters 37–50 need translation. Safe parallel split for the remaining work:

- **Agent A:** chapters 37–42 (`--chapter` flag with `translate-with-claude.py`, or new static scripts)
- **Agent B:** chapters 43–50

These write to different keys in the same JSON file — safe only if each agent reads, patches, and writes atomically. The `translate-with-claude.py` script does this correctly per chapter.

### Chapter-level split for John

John is 21 chapters. Existing script boundaries:

- **Agent A:** John 1–5 (`mkt-john-1-5.py` range)
- **Agent B:** John 6–10
- **Agent C:** John 11–15
- **Agent D:** John 16–21

---

## 9. Translation Workshop (Browser UI)

**URL:** `translation/workshop/index.html` (served locally or via GitHub Pages)

The workshop is the human-driven tool for making lemma decisions before running the AI translation. It reads phase bundle JSON files and writes decisions to `localStorage` key `bsw_ws_decisions`.

**Review queue order:**
1. Phase 1 — Top 200 NT Greek (sorted by NT frequency)
2. Phase 2 — Top 200 OT Hebrew (sorted by OT frequency)
3. Phase 5 — Contested Terms (sorted by dispute_level desc)
4. All Greek / All Hebrew (the full 5,523 / 8,674 entries)

**Decision actions:**
- **Confirm** — Accept proposed tier renderings; status → `confirmed`
- **Override** — Edit tier values + write reasoning; status → `override`
- **Inform** — Add a note to the decision log without changing status
- **Dispute** — Flag for deeper research; status → `disputed`
- **Defer** — Skip for now; status → `deferred`
- **Lock** — Seal a confirmed/override entry as final; status → `locked`

**Export/Import:** "Export JSON" button downloads `mkt-decisions-YYYY-MM-DD.json`. This file is the input to `apply-decisions.py`.

---

## 10. Prompt Context the AI Translator Receives Per Chapter

When `translate-with-claude.py` runs, each chapter call to Claude receives:

1. **System prompt** — Full MKT translation principles (8 rules above, expanded)
2. **Chapter context** — Named context descriptions for key chapters (John 1, Gen 1, etc.)
3. **Contested vocabulary block** — All `dispute_level >= 2` codes in the chapter, with full dispute notes and glossary proposals
4. **Confirmed glossary block** — All `confirmed/override/locked` codes in the chapter with their approved renderings
5. **Interlinear data** — Every verse as `vN: word[CODE/lemma] word[CODE/lemma]...`

Claude returns JSON in the form:
```json
{
  "CHAPTER": {
    "VERSE": {
      "lit": "...",
      "med": "...",
      "tho": "...",
      "notes": {
        "structure": "one-sentence grammatical summary",
        "decisions": ["decision 1", "decision 2"],
        "key_terms": [{"code": "G3056", "word": "λόγος", "note": "..."}]
      }
    }
  }
}
```

---

## 11. Frequently Confused Things

- **`notes/` files are not the AI reasoning.** The `tokens` / `flags` / `div` / `struct` keys are written by `generate-notes.py` from interlinear data. The `reasoning` key is what `translate-with-claude.py` adds. Currently no book has `reasoning` yet.
- **The glossary files are the ground truth for decisions.** The `localStorage` in the browser is a working state. `apply-decisions.py` is how those browser decisions become durable.
- **Chapter and verse keys are strings, not integers.** `"1"`, not `1`.
- **`disp` field in notes tokens** is display priority (0 = secondary/non-displayed in default view, 1+ = primary rendered word). It is interlinear metadata, not a tier value.
- **Phase bundles ≠ glossary.** `phase1.json` etc. are pre-computed subsets of the glossary with full `source_data` for the workshop UI. They are generated by `seed-glossary.py` and are read-only inputs to the workshop.
