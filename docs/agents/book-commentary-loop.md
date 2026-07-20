# Book Commentary — the Full Treatment loop

> Authored 2026-07-19; reshaped 2026-07-20. This is **the** per-book study loop: it
> writes the synthesized commentary that, together with an auto-assembled intro,
> forms the one **Full Treatment** per book ([study-pipeline.md](study-pipeline.md)).
> See [../plans/book-capstone-plan.md](../plans/book-capstone-plan.md) and the
> sibling [cow-synthesis-loop.md](cow-synthesis-loop.md). Keep this current if the
> contract changes.

## What it is

The **Commentary** is the full expository treatment of a book: **various voices,
section by section, then verse by verse within each section.** Each book is
handled on its own logical structure — sections follow the book's natural
pericopes; inside a section the commentary proceeds verse by verse, weaving the
attributed voices as it goes.

It is the capstone — the **full synthesis**. For each section and verse, bring as
many perspectives as the text warrants:
- **Original language** — the key Greek/Hebrew term(s), what the grammar or word
  choice does, and what English loses.
- **Historical context** — the setting, background, and cultural world behind the
  passage (Second-Temple, Greco-Roman, ANE — as relevant).
- **Christ** — how the verse/section reveals, anticipates, or is fulfilled in
  Christ. Surface Christ across the whole book, not only the obvious texts.
- **The Cloud of Witnesses** — the internal catena, attributed by name + school.
- **External scholarship** — named modern voices, paraphrased (see below).

The two families of voices come from two places:
1. **Internal — the Cloud of Witnesses.** The catena already on the site:
   `data/commentary/cow/<book>/<ch>.json` (raw multi-voice) and
   `data/commentary/cow-synthesis/<book>/<ch>.json` (the AI-distilled per-verse
   synthesis). These are the primary grounding.
2. **External — attributed scholarship.** Named scholars and works *beyond* the
   site's corpus (e.g. a standard modern commentary), cited by name and
   summarized — **never copied verbatim.** Same posture the COW synthesis uses
   for its witnesses. Copyright-safe: attribute and paraphrase, do not reproduce.

This is generated **one chapter per iteration** (plus a one-time `_book.json`
overview per book), by an autonomous loop. It is flagged **AI-assisted**.

## Data layout

| Tree | Role |
|---|---|
| `data/commentary/cow/<book>/<ch>.json` | INPUT — raw catena, per verse (all 66 books) |
| `data/commentary/cow-synthesis/<book>/<ch>.json` | INPUT — distilled per-verse synthesis (where present) |
| `data/synthesis/<book>/<ch>.json` | INPUT — per-pericope five-domain synthesis (for section boundaries) |
| `data/books/introductions/<book>.json` | INPUT — book overview material |
| `data/commentary/exposition/<book>/_book.json` | OUTPUT — book-level commentary overview |
| `data/commentary/exposition/<book>/<ch>.json` | OUTPUT — per-chapter, section → verse-by-verse |

## Ordering — governed by the pipeline

This loop **is** the Book Treatment loop ([study-pipeline.md](study-pipeline.md)):
one Full Treatment per book, no separate stages. The treatment PAGE assembles the
intro from existing per-book data; this loop writes the commentary. Claim the
book's **Treatment** cell in [study-pipeline-tracker.md](study-pipeline-tracker.md).

**Within a claimed book**, do the units in order: write `_book.json` (the
overview) first, then chapters `1..N` — the next unit is the first chapter whose
`exposition/<book>/<ch>.json` is missing (its source `cow/<book>/<ch>.json`
always exists). A book is complete when `_book.json` and every chapter file exist.

## Output schemas

### `_book.json` — book-level overview (written once per book, first)
```json
{
  "id": "<book id>", "title": "<display name>",
  "testament": "OT|NT", "genre": "<bk genre: torah|history|wisdom|prophecy|gospel|epistle|apocalyptic>",
  "overview": {
    "argument":  "<html>",   // the book's flow of thought / structure of the argument
    "occasion":  "<html>",   // author, date, audience, occasion (grounded, non-speculative)
    "theology":  "<html>",   // the book's central theological contribution
    "christ":    "<html>",   // how the book reveals / anticipates Christ
    "structure": [ { "label": "…", "range": "1-7", "gist": "one line" } ]
  },
  "witnesses": ["Full Name", "…"],          // internal COW voices drawn on across the book
  "external":  [ { "name": "…", "work": "…", "year": "…", "note": "…" } ],  // attributed, paraphrased
  "ai_assisted": true,
  "_source": {
    "kind": "commentary", "method": "ai-assisted", "generated": "YYYY-MM-DD",
    "inputs": ["data/commentary/cow/<book>/1.json", "data/commentary/cow-synthesis/<book>/1.json",
               "external scholarship (attributed)"]
  }
}
```

### `<ch>.json` — per chapter, keyed by pericope start verse
```json
{
  "_meta": {                            // optional — chapter-level
    "title": "God Has Spoken in His Son",     // shown on the chapter division (esp. multi-chapter books)
    "reflection": ["<html question>", "…"]    // per-chapter "For reflection" questions (refs linked)
  },
  "1": {
    "pericope_label": "Greeting",
    "range": "1-3",
    "exposition": "<html>",           // flowing commentary on the WHOLE section (gets the illuminated drop cap)
    "original_language": "<html>",    // optional — key Greek/Hebrew terms in this section; what English loses
    "historical_context": "<html>",   // optional — setting / background behind the section
    "christ": "<html>",               // optional — Christ in this section
    "verses": [
      { "v": "1", "note": "<html>" }, // verse-by-verse; weave witnesses + the perspectives inline, by name + school
      { "v": "2", "note": "<html>" }
    ],
    "witnesses": [ { "voice": "John Chrysostom", "tradition": "eastern", "point": "…" } ],
    "external":  [ { "name": "…", "point": "…" } ],
    "application": "<html>"           // optional; a closing pastoral turn for the section
  }
}
```

- **Verse keys mirror the source `cow/<book>/<ch>.json` EXACTLY** — never
  renumber or re-versify. Every verse in the chapter appears in exactly one
  section's `verses` array.
- Section boundaries follow the book's logic — prefer the pericope divisions
  already in `data/synthesis/<book>/<ch>.json` where they exist; otherwise divide
  by the argument.
- Voices named in prose use their **display school** inline
  (`<strong>Reformed</strong>`, `<strong>eastern</strong>`, etc.) as the COW
  synthesis does; enum slugs never appear in prose.
- Scripture refs are **always** `<a class="ref" data-ref="Philemon 1:6">v.6</a>`
  — never a bare "Book Ch:V". Chapter-only citations point at verse 1.
- **Source noise**: the catena files carry scrape residue (page chrome, CSS/JS
  fragments) and occasionally a fragment that belongs to another passage — skip
  both; never synthesize a view from them.

## Per-unit procedure

1. **Study one finished pair first** (once any exist): a book's `_book.json` +
   one `<ch>.json`, plus the seed reference (Philemon —
   `data/commentary/exposition/philemon/`). Match the established voice exactly.
2. Read the chapter's `cow/<book>/<ch>.json` (raw voices) and
   `cow-synthesis/<book>/<ch>.json` (distilled) and the `synthesis/<book>/<ch>.json`
   pericope labels. Identify the section boundaries and the voices present.
3. For `_book.json` units: write the overview from the book's inputs.
4. For chapter units: for every section, write the flowing `exposition`, then the
   verse-by-verse `verses` notes, weaving internal witnesses (attributed by name
   + school) and adding external scholarship (named, paraphrased, in `external`).
   Real disagreements surface as disagreements.
5. **Validate before committing** — must pass clean:
   `python scripts/validate-commentary.py --chapter <book> <ch>` (verse keys
   mirror source 1:1; every ref linked; `_source` present; sections non-empty).
   For overviews: `python scripts/validate-commentary.py --overview <book>`.
6. Commit exactly:
   - `Commentary: <book> overview` (for `_book.json`)
   - `Commentary: <book> <ch> (<N> verses)` (for a chapter)
   When a book's commentary first exists, flip `books-content.json` →
   `books.<book>.commentary.exists = true` and update `coverage` /
   `chapters_done` in the same commit. Scratch in `scratchpad/` (gitignored).
   Do not push — pushes deploy production and need owner approval.

## Quality bar

- Grounded ONLY in what the witnesses (internal + external) actually say — never
  invent a commentator's view or an external scholar's position.
- **Full synthesis** — across a section and its verses, cover the perspectives the
  text warrants: original language, historical context, Christ, the Cloud of
  Witnesses, and external scholarship. Not every verse needs every lens, but the
  section as a whole should be multi-perspectival, and Christ should surface across
  the book, not only at the obvious texts. Use the optional section fields
  (`original_language` / `historical_context` / `christ`) for the heavier context
  that does not fit a single verse note.
- **Commentary-level**, not a paraphrase of the verse: exposition explains the
  argument; verse notes do real exegetical work (grammar, key terms, the
  interpretive options and who holds them).
- Narrative prose, not a template. Vary openings and structure section to section;
  let the material lead. Degenerate filler can hide inside the length window —
  spot-read, don't trust word counts.
- External sources are **attributed and paraphrased, never quoted verbatim** at
  length. When witnesses divide, present the debate honestly.

## Tracker

State lives in the combined [study-pipeline-tracker.md](study-pipeline-tracker.md)
(**Commentary** column). Reference exemplar: **philemon** (overview + ch 1, all 25
verses, multi-perspective). Mark `🔄 (n/N ch)` while chapters are in flight; `✅`
only when `_book.json` and every chapter exist, `books-content.json` is flipped,
and the validator passes.
