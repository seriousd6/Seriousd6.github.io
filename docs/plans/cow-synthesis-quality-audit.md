# COW Synthesis Quality Audit — 2026-08-09

> Full-corpus audit of **Commentary A** (`data/commentary/cow-synthesis/`),
> prompted by the owner's observation that some entries repeat phrases to reach
> the 350-word minimum. **Finding: confirmed, and larger than the sample
> suggested.** 43% of the corpus is degenerate filler.
>
> Tool: [`scripts/audit-synthesis-quality.py`](../../scripts/audit-synthesis-quality.py)
> — this is the **anti-template lint** the TODO lists as lost with the `working/`
> tree. It is now recovered and tracked.
>
> **Nothing has been regenerated.** The prompt changes (§6) and the floor
> decision (§7) are applied, so *new* work is protected. Repairing the existing
> 9,354 grade-D verses is a separate, much larger decision (§8).

---

## 1. The headline

| | verses | share |
|---|---:|---:|
| **A** — reads like the gold standard (2 Kings 13, Psalms) | 8,078 | 37.3% |
| **B** — sound, some repetition | 2,587 | 11.9% |
| **C** — visibly repetitive | 1,663 | 7.7% |
| **D** — degenerate, filler reaching length | 9,354 | **43.1%** |

**356 of 757 chapters are entirely grade C/D.** Corpus: 21,682 verses.

`validate-synthesis.py` passes every one of them. It checks that a verse is
present, linked, tagged, and 350–650 words. It cannot check whether the length
was *earned* — which is precisely the gap the lost lint used to cover.

## 2. Root cause: one batch, one day

The defect is not spread evenly. It splits on the generation date, sharply:

| generated | verses | grade C+D | META hits | SLOT hits |
|---|---:|---:|---:|---:|
| **2026-07-22** (one mass batch) | 19,178 | **57.4%** | 5,575 | 2,384 |
| 2026-07-23 onward (per-chapter loop) | 2,504 | **0.0%** | 0 | 0 |

19,178 verses — 88% of the corpus — were generated in a single day's fan-out.
Everything produced since, under the documented per-chapter procedure with
calibrated profiles, is clean. **The current procedure works. The debt is
historical.**

The batch was internally uneven, which points at differing per-agent prompts
rather than a single bad template:

- clean within the batch: 1 Chronicles, 1–2 Kings, 2 Samuel, 2 Chronicles (0.0%)
- destroyed within the batch: Judges, Romans, Titus, Philippians, 3 John (100.0%)

The loop doc already records that *"a 2026-07-22 batch shipped meta-commentary
that had to be regenerated."* That repair addressed one symptom in some
chapters. The bulk of the day's output was never quality-checked, because the
lint that would have caught it no longer existed.

## 3. The mechanism — how length was reached

Grade-D verses hit the word count with stock carrier sentences and re-quoted
scripture rather than with commentary.

| | grade A | grade D |
|---|---:|---:|
| stock carrier phrases per verse | 0.47 | **10.28** |
| share of the verse that is quoted text | 18.5% | 22.3% |

The carriers, corpus-wide:

| phrase | uses | verses | max in one verse |
|---|---:|---:|---:|
| "the verse displays…" | 49,437 | 6,115 | 12 |
| "the witnesses note…" | 45,395 | 12,439 | **13** |
| "so the witnesses…" | 7,826 | 6,914 | 3 |
| "the grammatical voices note…" | 5,345 | 5,342 | 2 |
| "the lesson the expositors draw…" | 2,760 | 2,760 | 1 |
| "the witnesses do not divide…" | 2,351 | 2,350 | 2 |

`ephesians 3:3` (473 words) says "The witnesses note" five times around one
clause. `1 timothy 5:9` (524 words) re-quotes the same verse fragment three
times. `joshua 17:1` (601 words) walks the verse phrase-by-phrase in a
parenthesised slot-list — and reaches 601 words, well past the floor.

**Padding is not confined to short verses.** Grade-D verses average *more* words
than grade-A ones. The floor did not cap the damage; it set a target the
generator overshot with filler.

## 4. Three named defects a reader can see

| flag | verses | what it is |
|---|---:|---|
| **META** | 5,575 (25.7%) | narrating the *source's* thinness to the reader — "The very brief comment matches the very brief verse" (2,399 uses of that exact sentence), "With so brief a body of comment the synthesis is short" |
| **SLOT** | 2,384 (11.0%) | the degenerate `; the <clause> (<gloss>); the <clause> (<gloss>)` filler shape |
| **NOISE** | 28 (0.1%) | narrating that a fragment was skipped — "The Jamieson-Fausset-Brown note here is misplaced" — **explicitly banned** by the loop doc, shipped anyway |

META and NOISE both violate the existing rule that the reader "must not be able
to tell any editing happened." They are not merely dull; they break the contract.

## 5. What is NOT wrong

Two things I checked and cleared, so effort is not wasted on them:

- **The validators are sound.** `validate-synthesis`, `validate-data`, and
  `validate-library-format` all pass. This is a quality gap, not a correctness
  one — which is exactly why it survived.

### CORRECTION (2026-08-09, later the same day)

An earlier version of this section claimed *"no fabricated commentators —
21,682 verses, zero exceptions."* **That was wrong.** The scan behind it ran
over Psalms only; I generalised it to the corpus without re-running. Corrected
finding, after checking every verse against the merged catena **and** all 36
`cow-sources/` corpora, with tolerance for name variants:

**101 verses attribute material to a commentator who has no comment on that
chapter in any source tree** (0.47% of the corpus).

| voice | verses | books |
|---|---:|---|
| Charles Ellicott | 98 | Joshua 87, Nehemiah 11 |
| Gregory | 2 | John |
| Tertullian | 1 | 2 Corinthians |

The pattern is the tell: **Ellicott's own corpus covers Joshua 1–11 and 13 —
chapter 12 is missing — and Joshua 12 is precisely where the synthesis invents
him.** Nehemiah is identical (corpus has every chapter but 7; chapter 7 is
flagged). The generator filled a slot the source could not fill rather than
leaving it empty.

Three earlier versions of this check were wrong in the other direction, which is
worth recording so the next person doesn't repeat them: matching on a voice's
last name flags every "X of Y" patristic name (Pelusium, Hippo, Nyssa are
places); a ≥4-character token filter silently drops "Leo"; and checking only the
merged `cow/` catena misses everything drawn from `cow-sources/`. Raw flags fell
368 → 202 → 101 as each was fixed. **Ground the check before trusting the
count.**

## 6. Loop-prompt changes — APPLIED 2026-08-09

All six are now in [`docs/agents/cow-synthesis-loop.md`](../agents/cow-synthesis-loop.md)
under "Prose rules". Each maps to a measured defect.

1. **Ban the stock carriers outright.** Name them: "the verse displays", "the
   witnesses note", "so the witnesses", "the grammatical voices note", "the
   lesson the expositors draw", "the witnesses do not divide". Require that no
   carrier sentence open more than one paragraph in a verse.
2. **Ban META explicitly.** The reader must never be told the source is brief.
   *If the witnesses say little, write less* — see §7.
3. **Make the floor a floor, not a target.** State that a verse with thin
   witness material should come in short and that this is correct; the current
   350-word minimum converts thin material into filler.
4. **Cap re-quoting.** Quoted scripture must not exceed ~20% of the verse, and
   the same fragment must not be quoted twice.
5. **Ban the slot-list shape** (`; the <clause> (<gloss>)` chains) by name.
6. **Require the lint to pass before commit**, alongside the validator:
   `python3 scripts/audit-synthesis-quality.py --book <book> --chapter <ch>`.

## 7. RESOLVED — the 350-word floor (owner decision, 2026-08-09)

**Chosen: option (b), the `thin` exemption.** Implemented in
`scripts/validate-synthesis.py` and documented in the loop prompt.

A verse may set `"thin": true` on its tags entry; its prose must then be
120–349 words, and the exemption is validated against the source rather than
taken on trust — the catena blob must be ≤ 200 visible words. A rich source
marked thin fails; a thin flag left on a verse that grew past 349 fails; a short
verse without the flag still fails the normal floor. All four paths are tested.

The evidence behind the decision: even in the **clean** batch, verses with under
100 words of source still produce a median of 431 words of synthesis — a 4–5×
expansion. Synthesis length sits at 410–440 words across every band of source
richness, which is the signature of writing to a target rather than to the
material. 13.5% of the clean batch has sparse sources, so the exemption has real
work to do.

### The original framing, kept for the record

The tension as first written: recommendations 2 and 3 collide with `validate-synthesis.py`'s hard 350-word
floor. Some verses genuinely have two lines of witness material; the honest
output is 150 words, and the floor forbids it. **The floor is what manufactured
the filler.** Options:

- **(a)** Lower or remove the floor and let length follow the material. Honest,
  and makes the lint the real quality gate — but the reader layer then shows
  visibly uneven entries.
- **(b)** Keep the floor and allow a `"thin": true` marker on verses whose
  sources are genuinely sparse, exempting them.
- **(c)** Keep the floor and widen the input — synthesize sparse verses in
  pericope groups rather than one at a time.

I'd take **(b)**: it preserves the reader experience, records the fact where a
tool can see it, and removes the incentive to pad. It is also the smallest
change to the existing contract.

## 8. Per-verse QA metadata (added 2026-08-09)

Every verse now carries a `qa` block on its tags entry: schema version, the
standard it was written to, the date, the grade it scored, the checks actually
performed, and the tool that graded it. Contract in `scripts/synthesis_qa.py`;
shape enforced by `validate-synthesis.py`; drift between recorded and recomputed
grade reported by the lint.

All 21,682 existing verses are stamped `legacy-unversioned` with their audit
grade — **the repair backlog is now machine-readable**, so the next wave can
select work with a query instead of a re-scan. Verses with unsourced
attributions additionally carry `ungrounded_voices`.

Backfill tool: `scripts/backfill-synthesis-qa.py`. It preserves each file's own
indentation — the tags tree mixes 1-space, 2-space and flush-left, and
normalising it buries the real change under ~380k lines of churn.

## 9. The CI gate (enabled 2026-08-09)

`validate.yml` now runs `audit-synthesis-quality.py --gate` on every push. It is
a **ratchet, not a cliff** — a gate that judged the whole corpus would be
permanently red and therefore ignored:

| verse state | gate behaviour |
|---|---|
| `qa.standard: cow-prose-rules-2026-08-09` | enforced in full — must grade A/B, no UNSOURCED/NOISE/META/SLOT |
| `qa.standard: legacy-unversioned` | skipped as tracked debt |
| no `qa` block | **fails** — otherwise omitting metadata would be the easy way to dodge the gate |
| legacy count above `LEGACY_BASELINE` (21,682) | **fails** — the exemption may shrink as chapters are repaired, never grow |

Green today: 0 enforced, 21,682 exempt, 0 unstamped. Every verse written or
repaired from now on is protected against regression, and the exempt count is a
live progress meter for the repair.

All four paths are tested in isolation: a real grade-A chapter stamped to the
current standard passes; a padded verse fails on grade; a verse naming an
unsourced voice fails on UNSOURCED; an unstamped verse and an inflated legacy
count each fail.

## 10. Repair scope, if approved

The queue is derived from the metadata, not from this list — run
`python3 scripts/synthesis-frontier.py --queue repair --worst-first`, which
weights a fidelity defect three times a grade defect and so leads with the
chapters that invent commentators (Joshua 21, Joshua 12).

- ~9,354 grade-D verses across ~447 chapters flagged for repair.
- Procedure: "Repair procedure" in
  [`docs/agents/cow-synthesis-loop.md`](../agents/cow-synthesis-loop.md).
- By reader impact the heavy books are Romans, Hebrews, 1–2 Corinthians,
  Genesis, Exodus, Judges (90–100% C+D).
- Already clean, leave alone: Job, Psalms, 1–2 Kings, 1–2 Chronicles, 2 Samuel,
  Ezra, Esther, Nehemiah, Matthew, John.

## 11. Running the lint

```
python3 scripts/audit-synthesis-quality.py                      # whole corpus
python3 scripts/audit-synthesis-quality.py --book romans        # one book
python3 scripts/audit-synthesis-quality.py --book psalms --chapter 21
python3 scripts/audit-synthesis-quality.py --json out.json      # machine-readable
python3 scripts/audit-synthesis-quality.py --gate               # the CI gate
```

Thresholds are calibrated against the loop's own gold standard (2 Kings 13 and
Psalms: MATTR ≈ 0.63, compression ratio ≈ 0.46) versus known-degenerate chapters
(Joshua 17, Numbers 33: MATTR ≈ 0.31–0.37, compression ≈ 0.20–0.26). Lexical
variety uses a moving-average TTR so it does not fall mechanically with length,
and compression ratio catches repetition that n-gram counting misses.
