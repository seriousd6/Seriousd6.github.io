# COW Synthesis Loop — the launch prompt

Paste the block below as the first message of a fresh session in the repo. It is
written for an **unattended** run to completion: the loop never stops to ask, and
anything a human would want to know goes into
[`cow-synthesis-notes.json`](cow-synthesis-notes.json) to be read later.

It uses `--queue auto`, which **drains the repair queue first and then moves on
to generation**, and reports empty only when both are done. Repair leads because
finishing the corpus while 43% of what is already published is filler would just
grow the surface to fix. `--next` prints `<queue> <book> <ch>` in this mode, so
the loop knows which kind of work it just picked up.

Do not run two loops at once: nothing claims a chapter off the queue, so two
agents will pick the same one and collide at the commit.

---

```
Run the COW synthesis loop, unattended, until the whole corpus is done — every
chapter repaired and every remaining chapter generated.

The procedure is docs/agents/cow-synthesis-loop.md — read it in full first and
follow it rather than this summary wherever they differ.

Per chapter:

1. unit=$(python3 scripts/synthesis-loop.py next --queue auto --worst-first)
   set -- $unit; queue=$1; book=$2; ch=$3
   The queue is "repair" while damaged chapters remain, then "generate" for
   chapters with a source catena but no synthesis yet. Exit 3 means BOTH queues
   are empty — that is the only reason to stop.

2. If queue is "repair", read the EXISTING prose first to see which defect shape
   it is: stock carrier phrases, the verse re-quoted for length, or the
   parenthesised slot-list. If queue is "generate" there is nothing to read yet
   — study a finished chapter instead (cow-synthesis/2kings/13.json is the gold
   standard) and match its voice.

3. Read data/commentary/cow/<book>/<ch>.json and write the chapter under the
   prose rules in the loop doc. On a repair, regenerate rather than trim — a
   padded verse cannot be trimmed into a good one, because the material was
   never there.
   - Mirror the source's verse keys exactly.
   - Where the sources are genuinely thin, use the thin exemption
     ("thin": true on the tags entry, prose 120–349 words) rather than padding.
   - If a witness has no comment on this chapter, say nothing in his name.
     Drop the attribution; do not go looking for something else of his to say.

4. Self-grade fidelity, per verse:
       python3 scripts/synthesis-fidelity.py --book <book> --chapter <ch>
   Read each verse against its source and record your verdict on the tags entry,
   beside "voices":
       "fidelity": {"grade": "A", "checked_by": "self"}
       "fidelity": {"grade": "B", "checked_by": "self", "note": "why it leans"}
   A = every claim traces to the source. B = faithful but stretched (note
   required). C = an unsupported claim is present — rewrite the verse instead of
   recording it; a stored C is rejected.
   Grade EVERY verse, not only the ones the tool flags. The signals are
   advisory: a verse that expands 1.2x with no odd proper nouns can still put a
   claim in a commentator's mouth, and that is exactly the case no tool sees.

5. python3 scripts/synthesis-loop.py finish "$book" "$ch" --unattended
   Runs validator → lint → fidelity → stamp → gates → commit, and refuses
   anything that has not earned the standard. Exit 4 means it failed, reverted,
   and recorded a note; go to the next chapter. It works out repair-vs-generate
   from the tree itself, so the commit message is right without you passing a
   flag.

Notes instead of stopping. You are unattended, so never pause for review — write
it down and carry on:
    python3 scripts/synthesis-note.py --book <book> --chapter <ch> \
        --kind <fidelity|disagreement|source-defect|observation> \
        --note "<what a human should know>" [--verses 3,7]
Record at least:
  - any verse graded B, and why;
  - any STRETCH / ENTITIES / UNSOURCED flag you judged a false positive, and why;
  - any defect in the source itself (scrape residue, a misplaced witness block,
    an out-of-range verse key);
  - anything you had to guess about.

Rules:
- Never hand-edit a qa block. Step 5 writes it.
- Do not push. The commits stay local for review.
- If the same chapter fails twice, note it and move on; do not keep retrying.
- Do not switch queues by hand; --queue auto does it. Repair finishes first.
- Stop only when BOTH queues are empty (exit 3). That is the end of the corpus:
  1,189 chapters synthesized and none carrying the legacy debt.

Start by running: python3 scripts/synthesis-loop.py status
```

---

## Reviewing afterwards

```sh
python3 scripts/synthesis-loop.py next --queue auto       # what it would do next
python3 scripts/synthesis-note.py --list                 # everything
python3 scripts/synthesis-note.py --list --kind rejected # what the driver refused
python3 scripts/synthesis-note.py --list --kind disagreement
python3 scripts/synthesis-loop.py status                 # queue + grade movement
git log --oneline origin/master..                        # what it actually committed
```

Two progress meters in `status`: the **exempt count** starts at 21,682 and only
falls as chapters are repaired, and **synthesized** climbs from 757/1,189 as
generation proceeds. The run is over when the first reaches zero and the second
reaches 1,189. Rejected attempts are kept under `scratchpad/rejected/` (gitignored) if
you want to see what was thrown away.

## A caution about the fidelity grade

It is **self**-assessment, and a model grading its own work drifts generous. It
catches outright invention and forces a deliberate read-back, which is the
difference between "nothing was watching" and "something is" — but it is not an
independent audit. If the notes show few or no B grades across many chapters,
that is a signal the grading has become a rubber stamp, not a signal that the
prose is flawless. The natural next step, once the repair is underway, is a
second agent grading a sample of finished chapters blind.
