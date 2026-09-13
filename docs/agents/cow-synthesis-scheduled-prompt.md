# COW Synthesis Loop — the scheduled prompt

The launch prompt in [cow-synthesis-loop-prompt.md](cow-synthesis-loop-prompt.md)
assumes one session that lives until the corpus is done. **This one is for a
Routine that fires every 30 minutes into a fresh session.** The difference is not
cosmetic — two things change and both are load-bearing:

- **A scheduled run must push.** Its container is reclaimed when the run ends, so
  a commit that only exists locally is a commit that never happened. Every
  chapter goes to `origin/master` before the run moves on. Pushing master is
  standing-approved (see `CLAUDE.md`).
- **Scheduled runs overlap.** A chapter takes longer than the 30-minute gap, so
  at any moment two or three sessions are writing. Nothing claims a chapter, so
  collisions are handled two ways: `--spread` makes two runs unlikely to pick the
  same chapter, and `finish --push` detects the case where they did — it checks
  whether the chapter moved on `origin/master` since this run forked, and if so
  drops its own prose (keeping its notes) rather than clobbering the winner.
  That is exit code **5**, and it is a normal outcome, not a failure.

Each run does a **bounded batch** rather than running to completion, so a
session's lifetime stays near the firing interval instead of growing without
limit.

**Budget the batch by source words, not by chapter count.** `--worst-first` is
also longest-first: defect weight counts defective verses, and verse count
tracks source size, so the head of the repair queue runs about **1.55x the corpus
median** (30.4k words against 19.6k). The tail is worse — 1 Corinthians 15 is
116k words and the corpus maximum is 151k, with 37.6% of chapters at 25k or
larger. A flat "two chapters" therefore asks for a fixed amount of work and gets
a wildly variable one; measured across six consecutive picks by one worker:
34.7k, 28.3k, 30.6k, 68.7k, 20.0k, 18.9k, 75.6k. The last was abandoned
unattempted when the worker ran out of context.

So measure the unit before committing to it:

```sh
python3 scripts/synthesis-loop.py size <book> <ch>
```

Over ~40k usable source words, that chapter is the whole batch. Under it, two
are reasonable. (Figures above measured 2026-08-16 by a live worker and
reproduced by `size`.)

---

```
Run a batch of COW synthesis work, unattended, then stop. You are one of several
scheduled runs working the same queue concurrently — read the concurrency rules
below before you touch anything.

The procedure is docs/agents/cow-synthesis-loop.md. Read it in full first and
follow it rather than this summary wherever the two differ.

Start clean, on the current master:

    git fetch origin master && git reset --hard origin/master

Then do UP TO 3 CHAPTERS, and stop. Per chapter:

1. unit=$(python3 scripts/synthesis-loop.py next --queue auto --worst-first --spread 40)
   set -- $unit; queue=$1; book=$2; ch=$3
   --spread 40 picks at random from the queue's worst 40 instead of its head, so
   two concurrent runs rarely choose the same chapter. Do not drop it, and do not
   pick a chapter by hand. Exit 3 means ALL FOUR queues are empty — the corpus is
   done; stop and say so.

2. What to read first depends on which queue served you:
   - "repair" — read the EXISTING prose to see which defect shape it is: stock
     carrier phrases, the verse re-quoted for length, or the parenthesised
     slot-list.
   - "generate" — there is nothing to read yet. Study a finished chapter instead
     (cow-synthesis/2kings/13.json is the gold standard) and match its voice.
   - "polish" — the chapter's worst verses graded B. Read them AND the fidelity
     notes recorded against them (synthesis-note.py --list --book <book>): the B
     was recorded by a writer who said in the note where the prose leans past
     its witness. Fix that specific lean; do not simply rewrite around it.
   - "legacy" — the chapter is still on the 2026-07-22 per-verse prose, one blob
     per verse. Rewrite it as pericope tiles under the current rules, exactly as
     a repair: regenerate from the catena rather than re-tiling the old prose.

3. Read data/commentary/cow/<book>/<ch>.json and write the chapter under the
   prose rules in the loop doc. On a repair, regenerate rather than trim — a
   padded verse cannot be trimmed into a good one, because the material was
   never there.
   - Mirror the source's verse keys exactly.
   - Where the sources are genuinely thin, use the thin exemption
     ("thin": true on the tags entry, prose 120-349 words) rather than padding.
   - If a witness has no comment on this chapter, say nothing in his name. Drop
     the attribution; do not go looking for something else of his to say.

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

5. Write your notes BEFORE finishing, so the push carries them (see below).

6. python3 scripts/synthesis-loop.py finish "$book" "$ch" --unattended --push
   Runs validator -> lint -> fidelity -> stamp -> gates -> commit -> push, and
   refuses anything that has not earned the standard.
       exit 0  landed on origin/master.
       exit 4  failed; it reverted the chapter, pushed a "rejected" note, and
               left the tree clean. Go to the next chapter.
       exit 5  another run finished this chapter first. Yours was dropped and
               your notes were kept. This is expected. Go to the next chapter.

Concurrency rules — the whole batch depends on these:
- NEVER git push by hand, and never force-push. finish --push is the only thing
  that writes to origin, and it is built to lose a race safely.
- NEVER rebase or merge to resolve a conflict. If the tree is dirty or diverged
  for any reason you did not cause, run
  "git fetch origin master && git reset --hard origin/master" and pick again.
- NEVER edit a chapter that is not the one you picked this iteration.
- Between chapters, start from origin again: git fetch origin master &&
  git reset --hard origin/master.

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

Other rules:
- Never hand-edit a qa block. Step 6 writes it.
- If the same chapter fails twice, note it and move on; do not keep retrying.
- Do not switch queues by hand; --queue auto does it, in the order
  repair -> generate -> polish -> legacy.
- If a chapter is genuinely unworkable because its SOURCE is defective, do not
  keep declining it every run: write a source-defect note, and say plainly in
  your report that it belongs on docs/agents/cow-synthesis-blocklist.json. Do
  not add it yourself — the blocklist is the owner's call — but a block that
  lives only in a prompt costs every worker a draw, every run, forever.
- Do not touch anything outside data/commentary/cow-synthesis*/ and the notebook.
- When the batch budget is spent, stop. Another run fires in 30 minutes and
  will continue. Never start a chapter you cannot finish — an abandoned pick
  costs the queue nothing but costs the run everything.

Finish by reporting: which chapters landed, which were dropped to a race, which
failed, and what "python3 scripts/synthesis-loop.py status" says now.
```

---

## Arming and disarming

Two Routines an hour apart in phase give a 30-minute cadence (a Routine's
minimum interval is hourly).

**A Routine must fire into a persistent session that already has the repo.**
This was learned the expensive way on 2026-08-15: the first attempt used
`create_new_session_on_fire`, which fired 56 times over 28 hours and produced
absolutely nothing. `create_trigger` has no `source_url` parameter and the
account's environment carries no repository binding of its own, so every fired
session came up with **no clone** and died on the first command. The failure is
silent and easy to mistake for the loop being slow: the Routine reports firing on
schedule, `last_fired_at` advances, and no session appears in the session list
(scheduled runs are excluded from it by default) — the only honest signal is that
the frontier meters do not move.

So the shape is: **long-lived workers, poked on a schedule.**

```sh
# one worker per Routine, each created WITH the repo attached
mcp__Claude_Code_Remote__create_session \
    source_url=https://github.com/seriousd6/Seriousd6.github.io \
    source_revision=master  permission_mode=auto  tags='["cow-synthesis-batch"]'

# a Routine that pokes that worker, rather than spawning a blank one
mcp__Claude_Code_Remote__create_trigger \
    persistent_session_id=session_...  cron_expression='13 * * * *'

mcp__Claude_Code_Remote__list_triggers
mcp__Claude_Code_Remote__update_trigger  trigger_id=... enabled=false   # pause
mcp__Claude_Code_Remote__delete_trigger  trigger_id=...                 # remove
```

`update_trigger` cannot add or change a session binding — to repoint a Routine at
a different worker, delete it and create a new one.

Two workers 30 minutes out of phase keep the concurrency the `--spread` and
exit-5 machinery was built for. The cost of a persistent worker is context
growth: it compacts as the pokes accumulate, so each poke asks it to flag when
its context is getting long, and a worker that says so should be replaced with a
fresh session rather than nursed.

**Check the meters, not the firings.** A Routine that fires perfectly and does
nothing looks identical to one that is working, from everywhere except the data.

## The hourly poke (current text, 2026-09-13)

The block above is the full standing procedure; a persistent worker has already
read it. What the Routine actually sends each hour is a short poke that names
what changed since the worker last looked. It is tracked here because it is the
thing that actually runs — a prompt that lives only inside a Routine is
knowledge nobody can review.

**Worker A** (`trig_013MAoEBMhzYYLzGuB9Ryet8`, fires at `:13`) carries this text
as of 2026-09-13. **Worker B** (`trig_019Kd3xEeRNyLNuth964AEu5`, `:43`) still
carries the previous generation/repair-era text; it keeps working unchanged,
because `--queue auto` picks up the new queues on its own and the blocklist
makes its "do not attempt numbers 31" clause moot. Repoint it with
`update_trigger` when convenient.

```
Run another COW synthesis batch, then stop. The queue changed — pull first, it is all in the repo.

1. git fetch origin master && git reset --hard origin/master

2. Generation and repair are DONE — 1,189/1,189 chapters, zero defects left in circulation. The loop now works two FOLLOW-ON queues and `--queue auto` serves them in order:
   polish — 239 chapters holding the 1,063 verses that graded B (faithful but stretched, or thin enough for the lint to mark down);
   legacy — 132 chapters still on the 2026-07-22 per-verse prose (3,133 verses stamped legacy-unversioned; another 5,525 sit inside the polish chapters and get re-stamped when those are rewritten).
   Same unit, same pipeline, same rules as repair. Exit 3 now means all four queues are empty; say so and stop.

3. numbers 31 is on docs/agents/cow-synthesis-blocklist.json and the picker no longer offers it — you do not need to decline it by hand any more. If you hit another chapter whose SOURCE is genuinely unworkable, write a source-defect note and say in your report that it belongs on the blocklist. Do not add it yourself.

4. Budget the batch by SOURCE WORDS, not chapter count. After each pick run
       python3 scripts/synthesis-loop.py size "$book" "$ch"
   Over ~40,000 usable source words that chapter is the WHOLE batch — do it and stop. Under that, two chapters is a reasonable batch. --worst-first is also longest-first. Never start a chapter you cannot finish; an abandoned pick costs the run everything and the queue nothing.

Otherwise as before. Pick with
    python3 scripts/synthesis-loop.py next --queue auto --worst-first --spread 40
On a "polish" pick, read the existing prose AND the fidelity notes recorded against its B verses —
    python3 scripts/synthesis-note.py --list --book "$book"
— the note says where the prose leans past its witness; fix that specific lean rather than rewriting around it. On a "legacy" pick, regenerate from the catena as pericope tiles; do not re-tile the old per-verse prose.

Write under the prose rules in docs/agents/cow-synthesis-loop.md, fidelity-self-grade every verse, record notes with scripts/synthesis-note.py before finishing, and land with
    python3 scripts/synthesis-loop.py finish "$book" "$ch" --unattended --push
Exit 5 means the other worker got there first — expected, move on. Reset to origin/master between chapters. Never push by hand, never force-push, never rebase. If a push fails, note it and stop rather than working around it by hand.

Report chapters landed, dropped, failed, and the meters from "python3 scripts/synthesis-loop.py status". Then stop and wait for the next poke. Say so if your context is getting long — I would rather rotate you than have you degrade.
```

## Watching it

```sh
python3 scripts/synthesis-loop.py status                  # all queues + grades
python3 scripts/synthesis-frontier.py --blocked            # what is suppressed, and why
python3 scripts/synthesis-note.py --list --since <date>   # what the runs saw
python3 scripts/synthesis-note.py --list --kind rejected  # what the driver refused
git log --oneline --since=<date> --grep='^COW synthesis'  # what actually landed
```

The meters in `status` are the honest ones. **synthesized** climbed to 1,189/1,189
and **to repair** fell to zero on 2026-09-12; what moves now is **to polish**
(239 chapters / 1,063 grade-B verses) and **to rewrite** (132 chapters / 3,133
legacy verses), and the **legacy-unversioned** line in the verses-by-standard
block falls as both drain. A run that reports three chapters landed but moves no
meter is a run that did nothing — check the notebook for `rejected` entries
first.

`python3 scripts/synthesis-frontier.py --blocked` prints what the blocklist is
suppressing and why. A queue that reads empty while a chapter is blocked is
empty *of workable chapters*, which is the honest answer; the blocked one is
waiting on an owner decision, not on a worker.

## What to expect from concurrency

Collisions are the cost of running several sessions against one queue, and they
are bounded rather than eliminated. With a 40-wide spread and three overlapping
runs, roughly one pick in fifteen collides; the loser writes a chapter that is
then dropped. That is wasted tokens, not corrupted data — the winner's chapter is
untouched and both runs' notes survive. If the waste ever looks material, widen
`--spread` before adding anything cleverer.
