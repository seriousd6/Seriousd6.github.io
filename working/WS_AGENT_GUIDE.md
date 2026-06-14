# Wide Source Commentary — Agent Reference Guide

This document is handed to a Claude Code agent before writing any `ws-synthesis-*` scripts. Read it in full before starting work.

---

## 1. What the Wide Source Commentary Is

A per-verse synthesis layer drawn from the best public-domain commentators in the Christian tradition. Each verse entry contains:

- A **synthesis paragraph** (100–250 words) — prose you write that integrates the voices into a coherent reading of the verse
- A **voices array** — 40–80 word excerpts from each source that contributed to the synthesis
- A **consensus field** — whether the sources broadly agree, differ in emphasis, or genuinely disagree
- A **key_tension field** — one sentence naming the disagreement when `consensus` is `"mixed"` or `"divided"`

This layer is displayed in two places: the reader's commentary tab (source id: `synthesis`) and the book's `topics/{book}/commentary.html` page.

---

## 2. Source Files Available

For every book, these commentary JSON files exist in `data/commentary/`:

| Source id | Path | Commentator | Notes |
|-----------|------|-------------|-------|
| `mhcc` | `data/commentary/{book}.json` | Matthew Henry Concise | **Top-level path — no subdirectory.** Puritanical, devotional, strong on application |
| `calvin` | `data/commentary/calvin/{book}.json` | John Calvin | Precise, grammatical, Reformed; strong on original languages |
| `ellicott` | `data/commentary/ellicott/{book}.json` | Charles Ellicott | Verse-by-verse, scholarly, Anglican; strong on syntax |
| `jfb` | `data/commentary/jfb/{book}.json` | Jamieson-Fausset-Brown | Encyclopedic, evangelical; strong on cross-reference |
| `clarke` | `data/commentary/clarke/{book}.json` | Adam Clarke | Detailed, Wesleyan; strong on philology |
| `wesley` | `data/commentary/wesley/{book}.json` | John Wesley | Brief, pastoral, practical |
| `barnes` | `data/commentary/barnes/{book}.json` | Albert Barnes | NT only; thorough, Reformed Baptist |
| `rwp` | `data/commentary/rwp/{book}.json` | Robertson's Word Pictures | NT only; grammatical, Greek syntax focus |
| `catena` | `data/commentary/catena/{book}.json` | Catena Aurea (Aquinas) | Patristic chain commentary; 66 books |
| `mkt-original` | `data/commentary/mkt-original/{book}.json` | MKT Original Languages | Greek/Hebrew word analysis; 66 books |
| `mkt-context` | `data/commentary/mkt-context/{book}.json` | MKT Context | Historical/literary background; 66 books |
| `mkt-christ` | `data/commentary/mkt-christ/{book}.json` | MKT Christological | Christological themes and typology; 66 books |

**Reading the source files:** Each source file is structured `{ "ch": { "v": "<html>" } }`. Some sources use a section-entry approach — the closest key ≤ the verse number is the relevant entry. Check a few keys near your verse to find it.

---

## 3. Data Schema (output)

**Output path:** `data/commentary/synthesis/{book}.json`

```json
{
  "1": {
    "1": {
      "synthesis": "<p>...</p>",
      "voices": [
        { "src": "calvin",   "attr": "Calvin's Commentaries",    "html": "<p>...</p>" },
        { "src": "mhcc",     "attr": "Matthew Henry Concise",    "html": "<p>...</p>" },
        { "src": "ellicott", "attr": "Ellicott's Commentary",    "html": "<p>...</p>" }
      ],
      "consensus": "affirm",
      "key_tension": null
    }
  }
}
```

**Field rules:**

- `synthesis` — HTML string, one or more `<p>` blocks. 100–250 words. See Section 4.
- `voices` — Array of 2–6 entries, one per source that contributed meaningfully. Never include a source that had nothing relevant to say about this specific verse. 40–80 words per entry. Prefer direct quotes over paraphrase; if paraphrasing, do not put it in quotes.
- `src` — must match one of the source ids in the table above
- `attr` — human-readable attribution string as it will appear in the UI
- `consensus` — `"affirm"` (voices broadly agree), `"mixed"` (significant variation in emphasis or application), `"divided"` (genuine scholarly disagreement on a point of substance)
- `key_tension` — null when `consensus = "affirm"`; otherwise a single sentence naming what the difference is

---

## 4. Synthesis Paragraph Principles

**4a. Synthesize — do not just concatenate**

The synthesis paragraph is not a list of what each commentator said in turn. It is a single coherent reading of the verse that integrates the insights of the tradition. Start with the point all voices agree on, then add the most significant insight from the tradition that enriches that core reading, then note any meaningful variation.

**4b. Structure**

1. Topic sentence — the verse's central claim or action, stated plainly
2. The tradition's best insight — what the best commentators add beyond what the verse surface says (philological precision, cultural background, theological weight, typological connection)
3. Variation note (if `consensus ≠ "affirm"`) — one sentence naming the emphasis difference or disagreement

**4c. Attribution in prose**

Use commentator names inline: "Calvin stresses…", "Henry characteristically draws out the practical application…", "Both Ellicott and JFB note…", "Clarke and Wesley diverge here…". This makes the synthesis feel like a conversation with the tradition, not a blended summary.

**4d. Be honest about silence**

When a source entry is for a section rather than the specific verse (i.e., the closest key is several verses away), and the content is not specifically about this verse, either skip that source or note it briefly: "Clarke here treats the broader paragraph rather than this verse specifically." Do not stretch a section comment to cover a verse it was not written for.

**4e. Never manufacture consensus**

If Calvin and Henry genuinely disagree on the weight of a term, say so. `consensus: "divided"` with a clear `key_tension` is more honest and more useful than a smoothed synthesis that obscures the difference.

**4f. Length targets**

- Normal verse: 1–2 `<p>` blocks, 100–160 words
- Theologically dense verse (John 1:1, Rom 3:21, Heb 1:3, etc.): up to 3 `<p>` blocks, up to 250 words
- Transitional or formulaic verse: 1 short `<p>` block, 60–100 words

---

## 5. Voices Excerpt Principles

**5a. Excerpts are chosen, not generated**

Copy 40–80 words directly from the source HTML (strip tags for selection, then wrap in `<p>`). Choose the excerpt that most directly addresses this verse — the commentator's sharpest, most specific sentence, not a generic opening.

**5b. Section-level entries**

If a source's closest entry is for a section (`key = v - 3`, for example) and the prose is obviously about the broader passage, copy the sentence or two that is most applicable to the specific verse and note the range: "Henry on vv. 1–3:…"

**5c. Strip formatting artifacts**

Source HTML often contains `<b>`, `<i>`, `<em>`, `<strong>`, cross-ref links, and chapter headings. In the voices excerpt, keep `<strong>` for key terms and `<em>` for transliterations; strip everything else to plain `<p>` text.

---

## 6. Consensus Classification

| Value | When to use |
|-------|-------------|
| `"affirm"` | All included voices reach the same conclusion on the verse's main point. Minor differences in application or word choice are not enough to upgrade to `"mixed"`. |
| `"mixed"` | One or more voices differs meaningfully in emphasis, application, or what they think is the verse's most important feature — but none contradicts the others outright. Typical: Henry focuses on devotional application while Calvin focuses on grammatical precision; they don't disagree, but they're pointing at different things. |
| `"divided"` | Two or more voices reach genuinely different conclusions on an interpretive question (e.g., the identity of a referent, the force of a Greek term, whether something is conditional or unconditional). Use this sparingly — most verses have genuine consensus among these Reformed/evangelical commentators. |

---

## 7. Coverage Goal

Every verse in the claimed chapter range must have an entry. This includes:

- Genealogies and lists — brief is fine; one `<p>` noting what the tradition says about the section's significance
- Transitional verses — note the narrative function; one voice on what the transition signals
- Doxologies and benedictions — tradition often has rich things to say about these; do not skip

The commentary page renders "No synthesis available" for missing entries. Gaps undercut the feature.

---

## 8. Parallelism Rules

Two agents may work the same book if they cover **different chapter ranges**. The `merge_synthesis` helper writes only absent chapter/verse keys — chapter-disjoint ranges are safe.

Two agents must **not** work the same chapter range of the same book simultaneously.

---

## 9. Frequently Confused Things

- **`synthesis` ≠ a quote.** The synthesis is your prose. The voices array holds the quotes.
- **`voices` ≠ all eight sources.** Only include sources that said something specifically useful about this verse. 2–4 voices is typical. 6 is the ceiling.
- **Source section entries.** `data/commentary/hebrews.json` (mhcc top-level) key `"1": {"1": ...}` may have the commentary for verses 1–4 all in verse key `"1"`. Read the actual content to see what range it covers before excerpting.
- **mhcc path is unique.** Every other source uses `data/commentary/{src}/{book}.json`. mhcc alone is at `data/commentary/{book}.json` (top-level). Always special-case it when building paths in scripts.
- **`key_tension` must be a sentence, not a word.** "Predestination vs. free will" is not a sentence. "Calvin reads the verb as a divine sovereign decree; Wesley takes it as a conditional promise that requires human response" is.
- **HTML in synthesis and voices uses `<p>`, `<strong>`, `<em>` only.** No headings, lists, blockquotes, or links.
