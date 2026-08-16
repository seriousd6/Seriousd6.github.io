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

Each run does a **bounded batch** (3 chapters below) rather than running to
completion, so a session's lifetime stays near the firing interval instead of
growing without limit. Raise or lower that number to trade throughput against
token spend; it is the only knob that matters.

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
   pick a chapter by hand. Exit 3 means BOTH queues are empty — the corpus is
   done; stop and say so.

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
- Do not switch queues by hand; --queue auto does it. Repair finishes first.
- Do not touch anything outside data/commentary/cow-synthesis*/ and the notebook.
- After 3 chapters, stop. Another run fires in 30 minutes and will continue.

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

## Watching it

```sh
python3 scripts/synthesis-loop.py status                  # both queues + grades
python3 scripts/synthesis-note.py --list --since <date>   # what the runs saw
python3 scripts/synthesis-note.py --list --kind rejected  # what the driver refused
git log --oneline --since=<date> --grep='^COW synthesis'  # what actually landed
```

The two meters in `status` are the honest ones: the **exempt/legacy count** falls
as chapters are repaired, and **synthesized** climbs toward 1,189 as generation
proceeds. A run that reports three chapters landed but moves neither meter is a
run that did nothing — check the notebook for `rejected` entries first.

## What to expect from concurrency

Collisions are the cost of running several sessions against one queue, and they
are bounded rather than eliminated. With a 40-wide spread and three overlapping
runs, roughly one pick in fifteen collides; the loser writes a chapter that is
then dropped. That is wasted tokens, not corrupted data — the winner's chapter is
untouched and both runs' notes survive. If the waste ever looks material, widen
`--spread` before adding anything cleverer.
