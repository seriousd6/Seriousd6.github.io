# COW Synthesis Loop — procedure

> Reconstructed 2026-07-19 from the loop's own commits, the validator, and the
> shipped data (the original prompt lived in the lost `working/` tree). This is
> now the canonical procedure; keep it current if the contract changes.

## What it is

"Cloud of Witnesses" synthesis (**Commentary A**) distils all the patristic /
reformation / modern voices on a verse into one ~500-word grounded summary,
shown in the reader's commentary layer and flagged AI-assisted. It is generated
one chapter per iteration by an autonomous agent loop.

Do not confuse with **Commentary B** (`data/synthesis/<book>/<ch>.json`,
per-pericope five-domain sections) — complete at 1,189/1,189 and validated by
the same script's `--section` mode.

## Data layout

| Tree | Role |
|---|---|
| `data/commentary/cow/<book>/<ch>.json` | INPUT — merged multi-voice catena per verse (complete, all 66 books) |
| `data/commentary/cow-sources/<slug>/` | INPUT — 37 per-commentator corpora (committed intermediates) |
| `data/commentary/cow-synthesis/<book>/<ch>.json` | OUTPUT — `{ "<verse>": "<html>" }`, one prose blob per verse |
| `data/commentary/cow-synthesis-tags/<book>/<ch>.json` | OUTPUT — parallel per-verse tags (see contract) |

## Frontier rule (how the loop knows what's next)

Progress is derived from the data itself — there is no tracker file, and since
2026-08-09 the per-verse `qa` metadata makes both queues queryable. **Do not
hand-count and do not trust a figure written in this file: ask the tool.**

```
python3 scripts/synthesis-frontier.py                    # summary + both queues
python3 scripts/synthesis-frontier.py --next             # one unit: "<book> <ch>"
python3 scripts/synthesis-frontier.py --next --queue repair --worst-first
python3 scripts/synthesis-frontier.py --next --queue auto --worst-first
```

**`--queue auto` is how you run the corpus to completion in one pass**: it serves
repair until that queue is empty, then generation, and exits 3 only when both are
done. Repair leads deliberately — finishing the corpus while 43% of what is
already published is filler would only grow the surface to fix. In this mode
`--next` prints `<queue> <book> <ch>`, so the caller knows which kind of work it
picked up.

There are **two queues**, and a loop should drain them in this order:

| queue | what it holds | how it is derived |
|---|---|---|
| **generate** | chapters with a source catena but no synthesis | `cow/<book>/<ch>.json` exists, `cow-synthesis/<book>/<ch>.json` does not |
| **repair** | chapters carrying the 2026-07-22 debt | any verse with `qa.standard == legacy-unversioned` and `qa.grade` in C/D, any unstamped verse, or any verse with `qa.ungrounded_voices` |

`--next` prints one `<book> <ch>` line and exits 3 when the queue is empty, so a
shell loop can drive itself:

```sh
unit=$(python3 scripts/synthesis-frontier.py --next --queue repair) || exit 0
set -- $unit; book=$1; ch=$2

# or, to run everything to completion (three fields, repair first):
unit=$(python3 scripts/synthesis-frontier.py --next --queue auto) || exit 0
set -- $unit; queue=$1; book=$2; ch=$3
```

`--worst-first` orders the repair queue by defect weight, counting a fidelity
defect three times a grade defect — so the chapters that invent commentators
(Joshua 21, Joshua 12) come before the merely padded ones.

**Book profiles still matter.** Psalms is pure Hebrew poetry — apply the Job
dialogue-poetry profile (witnesses on wording, imagery, textual variants, and
the flow of the psalm rather than events); chapters range from 2 verses (Ps 117)
to 176 (Ps 119), so size waves accordingly. NB the NT was synthesized in an
earlier pass, so the generate queue is purely OT — the count is not a single
canonical sweep.

> **Out-of-range source key (2026-07-22):** some `cow/` chapters carry a scrape
> key whose verse number is out-of-range for the chapter and whose content is
> entirely foreign-passage material (e.g. **2 Chronicles 27** source has a key
> `16` — 2 Chron 27 has only 9 verses — holding Matthew Henry on 2 Chron 28,
> Ahaz). Treat these as scrape corruption: **omit them** rather than synthesize a
> nonexistent verse (documented in the ch27 commit). A source-vs-synthesis
> key-diff will legitimately show ch27 as 9-vs-10; that is expected, not a defect.

## Running it unattended

**Launch prompt:** [cow-synthesis-loop-prompt.md](cow-synthesis-loop-prompt.md)
— paste it into a fresh session and leave it. **Notebook:**
[cow-synthesis-notes.json](cow-synthesis-notes.json) — an unattended loop cannot
stop and ask, so fidelity calls worth a second opinion, tool flags it overrode,
source defects, and chapters the driver rejected all go there:

```
python3 scripts/synthesis-note.py --book <book> --chapter <ch> \
    --kind <fidelity|disagreement|source-defect|observation> --note "..."
python3 scripts/synthesis-note.py --list [--kind ...] [--since YYYY-MM-DD]
```

The driver writes a `rejected` note itself whenever `--unattended` reverts a
chapter, so a failure that nobody watched still leaves a trail.

`scripts/synthesis-loop.py` owns everything mechanical — choosing the unit,
verifying it, stamping it, committing it, and refusing anything that has not
earned the standard. **An agent only has to write the prose and tags files.**

```sh
while unit=$(python3 scripts/synthesis-loop.py next --queue auto --worst-first); do
  set -- $unit; queue=$1; book=$2; ch=$3

  #  ... the agent writes cow-synthesis/$book/$ch.json + the tags file here,
  #      and records a fidelity self-grade on every tags entry ...

  python3 scripts/synthesis-loop.py finish "$book" "$ch" --unattended || continue
done
```

`finish` infers repair-vs-generate from the tree (a chapter already tracked in
HEAD is being rewritten), so the commit message is right without the caller
passing a flag it could get wrong.

`finish` runs validator → chapter lint → **fidelity** → stamp → chapter gate →
corpus gate → commit, and stops before the commit on any failure, so bad work
cannot land. The fidelity step fails unless every verse carries a self-grade —
that one cannot be automated away, which is exactly why it is a gate.

**Exit codes** (stable; the loop depends on them): `0` success · `2` usage ·
`3` queue empty, stop · `4` chapter failed verification, nothing committed.

Two details that make unattended running safe:

- **`--unattended` reverts a failed chapter** after copying it to
  `scratchpad/rejected/<book>-<ch>-<timestamp>/`, so the tree stays clean and the
  next iteration proceeds. Losing one chapter's output is cheap — the source
  catena is untouched and it can be regenerated; a stalled loop with a dirty tree
  is not. Without the flag the files are left in place for inspection.
- **The chapter lint runs `--enforce-all`.** A chapter under repair still carries
  its OLD `legacy-unversioned` stamp, which the plain gate skips — so without
  this the first check would pass vacuously on exactly the work it is meant to
  judge. (It did, until it was caught in testing.)

`--dry-run` rehearses the whole chain, stamp and both gates included, then
restores the tags file so the tree is unchanged.

## Per-chapter procedure

1. **Study one finished pair first** (e.g. `cow-synthesis/2kings/13.json` +
   its tags file) and skim the chapter's `cow/<book>/<ch>.json` source. Match
   the established voice exactly.
2. Write the prose file: for EVERY verse in the chapter (mirror the source
   file's verse keys EXACTLY — never renumber or re-versify), one HTML string
   that narrates what the witnesses say — attributed by name, with each
   commentator's school named inline as a `<strong>` tag. **Going-forward
   convention: use the FULL enum slug** exactly as it appears in the tags file —
   `<strong>reformed</strong>`, `<strong>wesleyan-arminian</strong>`,
   `<strong>puritan-evangelical</strong>`, `<strong>grammatical-historical</strong>`
   — since that is the plurality form (~81% of school-label occurrences, 5.4k vs
   1.3k short) and it matches the tags. NB the shipped corpus is historically
   **inconsistent** on this cosmetic point: `<strong>` is used freely for
   commentator names (`<strong>Gill</strong>`), key terms, and schools in short
   (`puritan`/`wesleyan`) and mixed-case (`Reformed`) forms — the reader layer
   renders `<strong>` as plain bold, so none of it fails validation or misleads a
   reader. Don't retrofit old chapters; just follow the full-slug convention in
   new work. (A 2026-08-01 Esther batch was normalized short→full to match.)
   Real disagreements surface as disagreements; scripture
   references are `<a class="ref" data-ref="2 Kings 13:10">v.10</a>` (NEVER
   a bare "Book Ch:V" outside an anchor; chapter-only citations point at
   verse 1, e.g. `data-ref="2 Chronicles 24:1"`).
   **Source noise**: the catena files contain scrape residue (page chrome,
   CSS/JS fragments) and occasionally a witness fragment that clearly
   belongs to another passage — skip both entirely; never synthesize a view
   from them. **Skip noise SILENTLY**: the reader-facing prose must NEVER
   narrate the skipping — no "scrape residue", "page chrome", "the source's
   noise", "belongs to another passage", "credited to no witness", or any
   mention that a fragment was set aside. Omit the noise as though it were
   never in the source (the 2 Kings 13 gold standard does this). A reader must
   not be able to tell any editing happened. Likewise never log the noise as a
   `debate` or `outlier` in the tags. (Verify with a grep for those phrases
   before committing — a 2026-07-22 batch shipped meta-commentary that had to
   be regenerated.)
3. Write the parallel tags file — per verse:
   - `voices`: non-empty list of commentator FULL names ("Keil and
     Delitzsch", "Matthew Henry").
   - `schools`: `[{school, prevalence, summary}]` — school slugs from:
     eastern-antiochene, eastern-alexandrian, latin-fathers, reformed,
     lutheran, wesleyan-arminian, puritan-evangelical,
     grammatical-historical. Prevalence measures how much of the verse's
     witness set carries that school's reading: 1 voice = `single`,
     2 = `several`, most = `majority`, all = `unanimous`; use `minority`
     for a small dissenting subset against a larger consensus. (Older
     chapters are inconsistent here; this is the rule going forward.)
   - `debates`: `[{question, sides: [{position, holders}]}]` — holders use
     short names ("Ellicott"); a critic quoted by a witness but not himself
     a witness is credited as reported, e.g. "Thenius (as reported by
     Ellicott)".
   - `outliers`: `[{voice, note}]`.
   - `themes`: short strings.
   - `fidelity`: **your own read-back verdict, one per verse** — see step 4.
   - `qa`: the metadata block — **required, or CI rejects the chapter as
     unstamped.** Do not hand-write it; step 5 stamps it from the measured
     result, so it cannot claim a grade the prose did not earn.
4. **Read it back and self-grade the fidelity of every verse.** This is the
   one check no script can perform. The lint measures repetition and confirms a
   named voice exists somewhere in the chapter's sources; neither tells you
   whether a 430-word paraphrase of 90 words of Gill still says what Gill said.

   ```
   python3 scripts/synthesis-fidelity.py --book <book> --chapter <ch>
   ```

   It prints source and synthesis side by side with the signals that predict
   where invention hides — **expansion ratio** (corpus median is 0.84x, because
   a synthesis normally distils; past ~6x the prose is mostly not coming from
   the page in front of it), **unsourced proper nouns**, and **ungrounded
   voices**. Read each verse against its source and record the verdict on the
   tags entry, beside `voices`:

   ```json
   "fidelity": {"grade": "A", "checked_by": "self"}
   "fidelity": {"grade": "B", "checked_by": "self", "note": "why it leans"}
   ```

   > **A** — every claim traces to the source; the expansion is framing, not new
   > content. **B** — faithful but stretched; the prose leans further than the
   > witness does. A note is required, so "B" cannot become a shrug.
   > **C** — an unsupported claim is present. Do not record it and ship;
   > **rewrite the verse.** The validator rejects a stored C.

   Grade honestly. A quietly wrong B costs a reader more than an admitted one,
   and the whole point of the audit was that nothing was watching this.

5. **Validate AND lint before committing** — both must pass clean:
   `python3 scripts/validate-synthesis.py --verse <book> <ch>`
   (350–650 words per verse targeting ~500 — or the thin exemption below;
   prose/tags keys must match 1:1; every ref linked; school slugs/prevalence
   from the enums), then
   `python3 scripts/audit-synthesis-quality.py --book <book> --chapter <ch>`
   (**every verse must grade A or B**; any UNSOURCED/NOISE/META/SLOT flag is a
   hard stop). The validator cannot see whether the length was *earned*; the
   lint can. **CI runs `--gate` on every push**, so a chapter that fails the lint
   fails the build — stamp each verse's `qa` block with
   `standard: cow-prose-rules-2026-08-09` and the checks you performed, or the
   gate rejects it as unstamped.
6. **Stamp the qa block** once validator, lint and fidelity are clean:

   ```
   python3 scripts/backfill-synthesis-qa.py --book <book> --standard current --overwrite
   ```

   This measures each verse and writes `standard: cow-prose-rules-2026-08-09`,
   the grade, the date, the full check list, and your fidelity verdict with the
   expansion ratio filled in by the tool — so the measured number cannot be
   typed by hand and the judgement cannot be manufactured by a script. It
   **refuses** any verse that grades C/D, names an ungrounded voice, or carries
   no fidelity self-grade — the standard is a claim about
   quality, so it has to be earned. If it refuses, fix the prose and re-run;
   never hand-edit a `qa` block to get past it.
7. Confirm the gate agrees, exactly as CI will run it:
   `python3 scripts/audit-synthesis-quality.py --gate`
8. Commit exactly: `COW synthesis: <book> <ch> (<N> verses)`.
   For repair work: `COW synthesis repair: <book> <ch> (<N> verses)`.
   Scratch work goes in `scratchpad/` (gitignored). Do not push — pushes
   deploy production and need owner approval.

## Repair procedure (the 2026-07-22 debt)

Same loop, different queue. 9,354 verses across ~356 chapters were written to no
standard and graded C or D by the
[quality audit](../plans/cow-synthesis-quality-audit.md). Repair is regeneration
of the prose, not patching: a padded verse cannot be trimmed into a good one,
because the material was never there.

1. `python3 scripts/synthesis-frontier.py --next --queue repair --worst-first`
2. **Read the existing prose first, to see what the defect actually is.** The
   audit names three shapes: stock carriers ("the witnesses note" up to 13 times
   in a verse), the verse re-quoted to add length, and the parenthesised
   slot-list. Recognising which one is in front of you is quicker than diagnosing
   from scratch.
3. Regenerate the chapter from `cow/<book>/<ch>.json` under the prose rules
   below. Where the sources are genuinely thin, use the **thin exemption** rather
   than padding — that is the whole reason it exists.
4. **Drop, don't launder, an ungrounded attribution.** If the old prose credits a
   witness with no comment on this chapter, he does not appear in the new prose
   at all. Do not go looking for something else of his to say instead.
5. Validate, lint, stamp (`--standard current`), gate, commit — steps 4–7 of the
   per-chapter procedure.

The exempt count in `--gate` output is the progress meter: it starts at 21,682
and falls as chapters are repaired. It may never rise.

## Prose rules (2026-08-09 — after the quality audit)

The [quality audit](../plans/cow-synthesis-quality-audit.md) found 43% of the
corpus was filler that passed every validator. These rules exist because each
was violated at scale; the lint enforces them mechanically.

**1. Banned carrier phrases.** These were used as filler to reach the floor —
"the verse displays" 49,437 times, "the witnesses note" 45,395 times (up to 13
in a single verse). Do not use any of them as a stock sentence opener:

> the verse displays · the witnesses note · so the witnesses · the grammatical
> voices note · the lesson the expositors draw · the witnesses do not divide ·
> the verse holds together · the shared, dominant note

Naming what a witness says is fine — *"Gill reads the fruit of the offspring"*.
Wrapping every clause in a stock carrier is not. **No carrier sentence may open
more than one paragraph in a verse.**

**2. Never narrate the source's thinness.** The reader must not be told that the
comment is brief, that the witnesses said little, or that the synthesis is short
as a result. "The very brief comment matches the very brief verse" shipped 2,399
times. If the witnesses say little, **write less** — see the thin exemption.

**3. Never narrate the skipping of noise.** Already a rule; restated because 28
verses shipped "The Jamieson-Fausset-Brown note here is misplaced". Omit the
residue as though it were never in the source.

**4. The floor is a floor, not a target.** 350 words is the minimum for a verse
with normal witness material, not a quota to reach. Padding to hit it is the
single defect that produced the audit.

**5. Cap re-quoting.** Quoted scripture must not exceed roughly a fifth of the
verse, and **the same fragment must never be quoted twice**. Re-quoting the
verse to add length is padding.

**6. No slot-lists.** The degenerate `; the <clause> (<gloss>); the <clause>
(<gloss>)` shape — walking the verse phrase by phrase in parentheses — is
banned outright. It was the worst offender in Joshua and Numbers.

### Fidelity — the attribution rule

**Never name a commentator who has no comment on the chapter.** The audit found
101 verses attributing views to a witness absent from every source corpus — 98
of them Ellicott, and the pattern gives the cause away: **Ellicott's corpus
covers Joshua 1–11 and 13, and the fabrication is in chapter 12.** The generator
filled the slot it expected rather than leaving it empty.

- A voice may only be named if it appears in `cow/<book>/<ch>.json` **or** in one
  of the 36 `cow-sources/<slug>/` corpora for that book and chapter.
- Voices legitimately span verse keys, so check the whole chapter, not the verse.
- If a witness has nothing on this chapter, **say nothing in his name.** A verse
  with three witnesses is not worse than one with five.
- The lint enforces this as `UNSOURCED`; it is a hard stop.

### Per-verse QA metadata

Every verse's tags entry carries a `qa` block recording what was actually done
to it — so the next wave of repairs can tell "written to the current standard"
from "not yet looked at" without re-reading the corpus:

```json
"qa": {
  "v": 1,
  "standard": "cow-prose-rules-2026-08-09",
  "generated": "2026-08-09",
  "grade": "A",
  "checks": ["length", "refs-linked", "tags-match", "schools-valid",
             "voices-sourced", "no-meta", "no-noise", "no-slot",
             "no-carriers", "quotes-capped"],
  "lint": "audit-synthesis-quality/1"
}
```

The contract, the check ids, and the standard names live in
`scripts/synthesis_qa.py`; `validate-synthesis.py` enforces the block's shape and
the lint reports drift between the recorded grade and the recomputed one. New
work must stamp `standard: cow-prose-rules-2026-08-09` and list every check it
passed. Existing verses carry `legacy-unversioned` plus the grade they scored in
the 2026-08-09 audit — that is the repair backlog, machine-readable.

### The thin exemption

Some verses genuinely carry two lines of witness material. Forcing those to 350
words is what manufactured the filler, so the contract now allows an opt-out:

- Set `"thin": true` on the verse's **tags** entry.
- The verse's prose must then be **120–349 words**.
- The exemption is checked against the source, not taken on trust: the catena
  blob for that verse must be **≤ 200 visible words**. A rich source marked
  thin fails; a thin flag left on a verse that grew past 349 words fails.

Use it where it is true. A thin entry that says one thing well is worth more
than 350 words that say it four times.

#### Declaring scrape residue (2026-08-10)

The exemption used to measure the RAW blob, which collided with the rule that
the writer must ignore scrape residue. Where a verse is mostly residue the two
rules left **no legal output**: over 200 raw words refused the exemption, and
the handful of usable words could not honestly reach the 350-word floor. That is
padding by contract — the very defect the repair exists to remove. Found on
**numbers 7** (vv. 4, 16, 40, 82, all Jamieson-Fausset-Brown blocks on Leviticus
16–17 filed under Numbers); a corpus scan put the shape at **575 verses across
387 chapters**, so it blocks roughly a third of the corpus.

The source is now measured the way the writer is required to READ it. Declare
the residue on the verse's tags entry, as a sibling of `voices`:

```json
"excluded_voices": ["Jamieson, Fausset and Brown"]
```

`source_words` then subtracts those blocks before applying the ≤ 200 test.

- **Declared, not detected.** No automatic residue-sniffing: a rule that guessed
  wrong would silently license a short verse on a rich source, and no cheap
  textual test separates "JFB on the Day of Atonement, filed under Numbers 7"
  from "JFB on Numbers 7". Same division of labour as the fidelity self-grade —
  the human judges, the tool verifies the shape.
- **It cannot be gamed.** A declared voice must actually head a block in that
  verse's blob, or the validator fails the verse, so the field cannot be padded
  with names to buy a thin pass.
- **It cannot break committed work.** Excluding a voice only lowers the measured
  source, and the only check reading it is an upper bound. With no exclusions
  declared the measurement is byte-identical to the old behaviour.
- Excluding a block does **not** license mentioning it. The residue still goes
  unnarrated in the prose, and the reason for the exclusion belongs in the
  notebook as a `source-defect` note.

## Quality bar

- Grounded ONLY in what the sources say — never invent a commentator's view.
- **Length follows the material.** A verse with rich witnesses runs long; a
  verse with sparse ones runs short and is marked `thin`. Writing every verse to
  ~430 words regardless of the source is the signature of the defect the audit
  found.
- Narrative prose, not a template. The original run had an "anti-template
  lint" (lost with `working/`; pending recovery) that blocked degenerate
  filler — the under-length John 4 output shows the failure mode it guarded
  against. Vary openings and structure verse to verse; let the material lead.
- **Anti-templating (poetry chapters especially):** do NOT open verse after
  verse with the full KJV verse in quotes followed by an em-dash. That rote
  "quote-the-verse, dash, comment" shape reads as a template even when the
  bodies differ (Job 5 shipped 26/27 verses that way and had to be
  regenerated). Most verses should open with a framing sentence and weave the
  quoted phrase in mid-sentence; keep quote-led openings a minority (rule of
  thumb ≤ ~⅓ of the chapter). A quick check: count verses whose visible text
  starts with a quotation mark before committing.
- Where witnesses genuinely divide (e.g. who the "saviour" of 2 Kings 13:5
  is), present the debate honestly and record it in `debates`.

## Repairs (resolved 2026-08-09) — Psalms 21

Psalms 21 shipped (commit `98557344`) with five verses under the 350-word floor
(vv. 5, 6, 10, 11, 12 at 319–349), turning CI red on master. Repaired by
expanding each from material already in `cow/psalms/21.json` that the first pass
left unused — Matthew Henry on vv. 5–6 (the source's Henry block sits under key
`1` and runs through v. 6), Keil and Delitzsch's `שׁוּה על` / Gen 12:2 note and
their `נטה רעה` idiom (their blocks span verse ranges under keys `4` and `10`),
Ellicott's second reference at v. 10, and Gill's fuller staging at v. 12.
Tags updated in step (Henry → `puritan-evangelical` at vv. 5–6; K&D added at
v. 11).

**Two things this chapter illustrates for future work:**

- **Voices legitimately spill across verse keys.** A per-verse check of
  "is this commentator in this verse's source?" produces heavy false positives —
  Keil and Delitzsch head their blocks with a verse range, and Matthew Henry's
  run covers a whole strophe. Check the WHOLE chapter source before concluding a
  voice was invented. (A scan of Psalms 1–24 flags 180+ per-verse mismatches and
  **zero** chapter-level ones.)
- **Psalms 21 key `13` carries scrape residue** — a Jamieson, Fausset and Brown
  block on 2 Chronicles 31 (Hezekiah and the temple courses). Correctly omitted
  in both passes; do not synthesize from it. Note that "Hezekiah" appears
  legitimately in vv. 1 and 4, where Clarke discusses the psalm's occasion.

## Repairs (resolved 2026-07-19)

The 62 validator failures found when wiring CI (John 4 wholesale, Luke 13 ×4,
Genesis 41 ×3, 1 Samuel 5 ×1) are fixed; the full corpus validates clean.
Watch for the failure mode they revealed: degenerate template filler can also
hide INSIDE the length window — spot-read, don't trust word counts alone.
