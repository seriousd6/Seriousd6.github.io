# Z Commentary — Agent Reference Guide

This document is handed to a Claude Code agent as context before writing any Z commentary or echo scripts. Read it in full before starting work.

---

## 1. What the Z Commentary Suite Is

Four parallel data layers for all 66 books, each exposed in the verse-study page:

| Layer | Data path | UI label | What it provides |
|-------|-----------|----------|------------------|
| **Echo** | `data/echoes/{book}.json` | Echoes & Fulfillments panel | Typed, linked OT↔NT connections per verse |
| **mkt-original** | `data/commentary/mkt-original/{book}.json` | Original Language (MKT) | What the Greek/Hebrew reveals that the translation doesn't surface |
| **mkt-context** | `data/commentary/mkt-context/{book}.json` | Historical Context (MKT) | What the original audience knew — ANE/Second Temple background, intertextuality |
| **mkt-christ** | `data/commentary/mkt-christ/{book}.json` | Christ in Every Verse (MKT) | How each verse fits the trajectory toward Christ; types, shadows, fulfillments |

The echo layer is the **data layer** — structured entries rendered as badge + ref link + note in the UI. The three commentary types are the **prose layer** — HTML injected into the commentary panel. They complement each other: echoes identify the connection; mkt-christ provides the exegetical argument.

---

## 2. Directory Map

```
data/
  echoes/                   {book}.json  → { "ch": { "v": [ {type, target, note} ] } }
  commentary/
    mkt-original/           {book}.json  → { "ch": { "v": "<html>" } }
    mkt-context/            {book}.json  → { "ch": { "v": "<html>" } }
    mkt-christ/             {book}.json  → { "ch": { "v": "<html>" } }
  translation/
    draft/mediating/        {book}.json  — MKT text to quote in commentary
    glossary-greek.json     — 5,523 Greek entries; semantic_range and source_data.thayer most useful
    glossary-hebrew.json    — 8,674 Hebrew entries; semantic_range and source_data.bdb most useful
  interlinear/              {book}.json  — Strongs tokens per verse
  parallels/                {book}.json  — prototype echo data; absorb before writing echoes
scripts/
  zc-echo-{book}-{start}-{end}.py     — echo data scripts
  zc-original-{book}-{start}-{end}.py
  zc-context-{book}-{start}-{end}.py
  zc-christ-{book}-{start}-{end}.py
Z_COMMENTARY_SCRIPT_GUIDE.md — boilerplate, HTML rules, parallels absorption
Z_PROGRESS.md               — work queue and status tracker
Z_AGENT_PROMPT.md           — claim protocol (this is the session entry point)
```

---

## 3. Data Schemas

### Echo entry

```json
{ "type": "allusion", "target": "Isa 53:7", "note": "The Servant led as a lamb to slaughter — John the Baptist's naming activates this register without explicit citation." }
```

- `type`: `quote | allusion | type | shadow | theme | fulfillment`
- `target`: a parseable Bible reference (`"Isa 53:7"`, `"Gen 22:8"`)
- `note`: 1–2 sentences — the argument for the connection, not just a label

### Commentary entry

```json
{ "3": { "16": "<p><strong>ἠγάπησεν</strong> (aorist) — a single completed act...</p>" } }
```

Each value is a well-formed HTML string. See `Z_COMMENTARY_SCRIPT_GUIDE.md` for HTML rules.

---

## 4. Content Principles

These apply across all three commentary types and the echo layer.

**4a. Add information — never just restate the text**

The commentary reader can already see the MKT translation. Every entry must tell them something the translation does not: a lexical nuance, a cultural practice, a background text, a typological argument. If you cannot add information beyond what the MKT text surface conveys, the entry is not ready.

**4b. Be honest about uncertainty**

- Echo: if a connection is thematic rather than deliberate verbal allusion, use `theme` not `allusion`. If a fulfillment connection is debated (e.g. Hosea 11:1 in Matt 2:15), note the debate rather than asserting one reading.
- mkt-christ: some verses have no direct Christological connection. A brief canonical-context note ("This genealogical entry places Christ within the Davidic line") is better than a forced type. Never manufacture Christological connections that are not defensible.

**4c. Distinguish what the text says from what tradition says**

The commentary is exegetical, not doctrinal enforcement. Present the range of defensible readings; state which reading the MKT follows and why.

**4d. Use the source language**

- Cite Greek/Hebrew terms when they are the reason for the comment
- Transliterate after the first use: `<em>dikaiosýnē</em> (righteousness)` then just `dikaiosýnē`
- Reference the Strongs code if it helps: `G1343 δικαιοσύνη`

---

## 5. Type-by-Type Content Guide

### 5a. mkt-original — Original Language Commentary

**Purpose:** Every translational choice has a reason rooted in the source text. This layer makes those reasons visible.

**What to cover per verse:**
- Verb aspect and its significance: aorist = completed act (snapshot), present = ongoing, perfect = past act with present result ("it stands written")
- Hebrew verbal aspect: perfect = complete, imperfect = ongoing/potential, waw-consecutive = narrative past
- Word-level nuance: which Greek/Hebrew word is used and why its semantic range matters
- Syntax that the translation necessarily smooths: genitive constructions, chiasm, asyndeton, emphatic word order, double negatives
- Textual variants that affect meaning (when present)
- Polysemy decisions: where σάρξ / πνεῦμα / δικαιοσύνη / חֶסֶד / נֶפֶשׁ could go different ways and why the MKT chose as it did

**What NOT to cover:** historical background (that's mkt-context), typology (that's mkt-christ), theological application (that's for the reader), general paraphrase.

**Length:** 1–3 `<p>` blocks, ~50–150 words per verse. Denser for theologically loaded verses (John 1:1, Rom 3:21–26, Gen 1:1–2). Brief for formulaic or transitional verses.

**Worked example — John 3:16:**
```html
<p><strong>ἠγάπησεν</strong> (aorist) marks the giving of the Son as a single completed historical act — not ongoing sentiment but a definitive event. The English "loved" flattens this.</p>
<p><strong>μονογενῆ</strong> — <em>monogenē</em>, only-begotten or unique-in-kind. Carries the relational weight of the father–son bond that makes the giving costly; more than "one-of-a-kind" in the abstract.</p>
<p><strong>ἵνα μὴ ἀπόληται</strong> — purpose clause with subjunctive: the goal is rescue from a state of perishing, not deliverance from an external sentence newly imposed.</p>
```

---

### 5b. mkt-context — Historical Context Commentary

**Purpose:** Restore what the original audience already knew — the background that the author assumed and that modern readers lack.

**What to cover per verse:**
- Second Temple Jewish beliefs, practices, and institutions that the text assumes (synagogue, purity laws, taxation, patronage systems)
- ANE cultural background for OT texts (creation myth polemics, suzerain-vassal treaties, kinship customs)
- Honor-shame dynamics: what would have been socially scandalous or vindicating to first-century hearers
- Intertextual echoes the author expected the audience to catch — OT allusions that carry freight without being explicit quotes
- Geographic and historical situation (the significance of locations, political context of Roman occupation, etc.)
- Rabbinic parallels or Second Temple literature that illuminates the passage (cite briefly; do not require readers to know the source)

**What NOT to cover:** the Greek/Hebrew mechanics (that's mkt-original), Christological connections (that's mkt-christ), general theological summary.

**Length:** 1–3 `<p>` blocks, ~50–150 words per verse. More for verses dense with cultural assumptions (covenant meals, purity controversies, judicial language); brief for narrative transitions.

**Worked example — John 2:6 (the water jars):**
```html
<p>Six stone water jars for Jewish purification rites (<em>katharismos</em>) — Jewish purity law required ritual hand-washing before meals and between courses. The quantity (20–30 gallons each) signals a household prepared for extended Passover hospitality.</p>
<p>Stone vessels were preferred because, unlike clay, they could not contract ritual impurity under Levitical law (Lev 11:33). Their prominence in the scene is not incidental — the vessels of purification become the vessels of celebration.</p>
```

---

### 5c. mkt-christ — Christ in Every Verse

**Purpose:** Trace how each verse participates in the biblical narrative that culminates in Christ. This is not forced allegory — it is honest canonical reading.

**The five directness levels (use these to classify connections):**

| Level | Description |
|-------|-------------|
| `direct` | NT explicitly cites this verse as fulfilled in Christ (e.g. Isa 7:14 / Matt 1:23) |
| `type` | OT person, institution, or event structurally anticipates Christ (e.g. Passover lamb, Melchizedek) |
| `shadow` | Broader OT pattern or theme that points forward less directly (e.g. temple → Christ as temple) |
| `theme` | Shared theological theme (e.g. God as shepherd, righteousness, covenant) — NT builds on this vocabulary |
| `revelation of God` | The verse reveals something about God's character or action that the NT presents as expressed fully in Christ |

**Rules:**
- Every verse gets an entry. For narrative, genealogical, or formulaic verses, a brief entry using `theme` or `revelation of God` is appropriate.
- State the directness level in the prose, even if not using the exact word: "This direct prophecy…", "As a type…", "The theme of…"
- Do not manufacture connections. If the Christological freight of a verse is genuinely indirect, say so: "This verse does not directly anticipate Christ, but establishes the covenant structure — the faithfulness of God to his people — that the NT presents as fulfilled in Christ."
- For NT verses: trace how they reveal Christ's fulfillment of OT themes, or how they present Christ's person and work.

**Length:** 1–2 `<p>` blocks, ~30–100 words per verse. Denser for prophetic passages; brief for administrative lists and genealogies.

**Worked example — Exod 12:3 (Passover lamb):**
```html
<p>A type: the Passover lamb anticipates Christ with structural precision — selected beforehand, unblemished, killed at Passover, its blood applied to avert judgment (1 Cor 5:7; John 1:29). The pattern is not an analogy the NT invents; it is a design the Exodus narrative establishes and the NT claims as deliberate.</p>
```

**Worked example — 1 Kgs 6:14 (Solomon finishes the temple):**
```html
<p>A shadow: the completion of Solomon's temple represents the dwelling of God with his people — the theme that runs from the Tabernacle through to John 1:14 ("the Word tabernacled among us") and Rev 21:3. The Solomonic temple is the high point of this trajectory before it is destroyed; Christ is its permanent fulfillment (John 2:19–21).</p>
```

---

### 5d. Echo Layer — Special Notes

**NT books:** NT-to-OT echoes are the primary direction. Trace what the NT author is doing with OT texts.

**OT books:** OT-to-NT echoes are the forward direction — where this OT text is taken up in the NT. Be specific: cite the NT verse, not just a vague "this anticipates…"

**Revelation:** Almost every verse in Revelation echoes OT material. Be selective — include echoes that illuminate the meaning, not every verbal parallel. A verse with 6 defensible echoes should show 2–3 best ones.

**Psalms:** Many Psalms are cited in the NT as Christological. Where the NT explicitly quotes a psalm verse, use `quote` or `fulfillment`. Where the NT applies a psalm typologically, use `type` or `allusion`. Always note whether the NT citation follows the LXX text.

**Contested echoes:** Some echoes are disputed (scholars disagree whether a connection is intentional). Note the debate briefly in the `note` field rather than asserting certainty: "Possibly alludes to… — the verbal overlap is notable though some scholars consider it coincidental."

---

## 6. Parallelism and Serialization Rules

### Safe to parallelize

| Task | Writes to | Safe with |
|------|-----------|-----------|
| Any type for `john` | `data/echoes/john.json`, `data/commentary/mkt-*/john.json` | Same type for any other book |
| `mkt-original` for `john` | `data/commentary/mkt-original/john.json` | `mkt-context` for `john` (different files) |
| Any commentary type for any book | per-book files only | Any type for any other book |

### Must serialize

| Conflict | Reason |
|----------|--------|
| Two agents writing the **same type** for the **same book** simultaneously | Both write to the same JSON file; last writer wins |
| `mkt-original` + `mkt-context` for the **same book** at the **same chapter range** | Same file + overlapping chapter keys; merge collision risk |

**Safe parallel pattern for one book:** assign different chapter ranges to different agents within the same type. The `merge_comm` helper writes only absent keys, so chapter-disjoint ranges on the same book are safe.

---

## 7. Verse Coverage

**Every verse in the claimed range must have an entry.** This includes:

- Genealogy entries (`"Noah was the father of Shem, Ham, and Japheth"`) — a brief entry is fine
- Doxologies and closing formulas — note what they reveal about the theology of the passage
- Transitional verses (`"After these things Jesus..."`) — note the narrative function
- List items in census, inventory, or law sections — brief entries are fine; it is worse to skip them

The verse-study page shows "No commentary available" for missing entries. Gaps undercut the feature.

---

## 8. Frequently Confused Things

- **Echo layer ≠ mkt-christ.** Echoes are structured data (machine-readable, rendered as badges with ref links). mkt-christ is prose HTML. They work together but are separate files.
- **Parallels are the prototype, not the source of truth.** `data/parallels/` will be retired once echoes cover the same books. Do not add to parallels; add to echoes instead.
- **mkt-context ≠ general theology.** Context commentary is about what the *original audience* knew, not about modern theological application.
- **Chapter and verse keys are strings** (`"3"`, `"16"`) — not integers.
- **The commentary directory for mhcc (default) is the root:** `data/commentary/{book}.json`. MKT commentary goes in subdirectories: `data/commentary/mkt-original/{book}.json`. The `load_comm('mkt-original', 'john')` helper handles this correctly.
- **The echo target must be a parseable ref.** Use the short-book form: `"Isa 53:7"`, `"Gen 22:8"`, `"Ps 22:1"`. This is what gets turned into a `.ref` link in the UI.
