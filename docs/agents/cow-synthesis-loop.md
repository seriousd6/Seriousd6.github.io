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

Progress is derived from the data itself — there is no tracker file. Walk the
books in canonical order (`data/bible/books.json`); the next work unit is the
first chapter whose `cow-synthesis/<book>/<ch>.json` is missing, given the
source `cow/<book>/<ch>.json` exists. As of **2026-07-22: 598/1,189 done
(50.3%), frontier = 1 Chronicles 1** (Genesis→**2 Kings** and the whole NT are
now complete; Chronicles→Malachi is the remaining OT back-half, still
untouched). NB the NT was synthesized in an earlier pass, so the frontier is
purely OT — the count is not a single canonical sweep.

## Per-chapter procedure

1. **Study one finished pair first** (e.g. `cow-synthesis/2kings/13.json` +
   its tags file) and skim the chapter's `cow/<book>/<ch>.json` source. Match
   the established voice exactly.
2. Write the prose file: for EVERY verse in the chapter (mirror the source
   file's verse keys EXACTLY — never renumber or re-versify), one HTML string
   that narrates what the witnesses say — attributed by name, with each
   commentator's school named inline in the corpus's DISPLAY form:
   `<strong>Reformed</strong>`, `<strong>Wesleyan</strong>`,
   `<strong>puritan</strong>`, `<strong>grammatical-historical</strong>`
   (the enum slugs like `wesleyan-arminian` appear only in tags files, never
   in prose). Real disagreements surface as disagreements; scripture
   references are `<a class="ref" data-ref="2 Kings 13:10">v.10</a>` (NEVER
   a bare "Book Ch:V" outside an anchor; chapter-only citations point at
   verse 1, e.g. `data-ref="2 Chronicles 24:1"`).
   **Source noise**: the catena files contain scrape residue (page chrome,
   CSS/JS fragments) and occasionally a witness fragment that clearly
   belongs to another passage — skip both entirely; never synthesize a view
   from them.
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
4. **Validate before committing** — must pass clean:
   `python scripts/validate-synthesis.py --verse <book> <ch>`
   (350–650 words per verse targeting ~500; prose/tags keys must match 1:1;
   every ref linked; school slugs/prevalence from the enums).
5. Commit exactly: `COW synthesis: <book> <ch> (<N> verses)`.
   Scratch work goes in `scratchpad/` (gitignored). Do not push — pushes
   deploy production and need owner approval.

## Quality bar

- Grounded ONLY in what the sources say — never invent a commentator's view.
- Narrative prose, not a template. The original run had an "anti-template
  lint" (lost with `working/`; pending recovery) that blocked degenerate
  filler — the under-length John 4 output shows the failure mode it guarded
  against. Vary openings and structure verse to verse; let the material lead.
- Where witnesses genuinely divide (e.g. who the "saviour" of 2 Kings 13:5
  is), present the debate honestly and record it in `debates`.

## Repairs (resolved 2026-07-19)

The 62 validator failures found when wiring CI (John 4 wholesale, Luke 13 ×4,
Genesis 41 ×3, 1 Samuel 5 ×1) are fixed; the full corpus validates clean.
Watch for the failure mode they revealed: degenerate template filler can also
hide INSIDE the length window — spot-read, don't trust word counts alone.
