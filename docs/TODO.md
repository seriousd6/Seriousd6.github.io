# TODO — canonical task list

Rules: pick tasks here; mark yours `*(in progress — <date>)*`; move finished
items to [todo-archive.md](todo-archive.md) **in the same commit as the work**.
Keep [STATUS.md](STATUS.md) current in that same commit.

## Now

### Looping work — fills the Studies tool (`/studies/`)

> Shared architecture: [plans/book-capstone-plan.md](plans/book-capstone-plan.md).
> The book pipeline is claimed + tracked in one place
> ([agents/study-pipeline-tracker.md](agents/study-pipeline-tracker.md)); COW +
> provenance derive their frontier from the data tree. Every loop commits per
> work-unit and must pass its validator before committing. No pushes without
> owner approval.

- [ ] **COW synthesis loop — continue at the OT frontier** *(active focus —
  2026-08-02)*. **738/1,189 = 62.1% done** (Genesis→**Job** + the whole NT
  complete; corpus validates clean). **2 Chronicles + Ezra + Nehemiah + Esther +
  Job (42/42) finished** (narrative + genealogy/register + dialogue-poetry
  profiles all calibrated; anti-templating check added — see loop-doc). Frontier =
  **Psalms 1** — pure Hebrew poetry, 150 ch (verse counts range 2 → 176), the
  largest remaining book; then the rest of Psalms → Malachi + poetic/wisdom
  (~451 ch). Mirror the source's sparse verse keys exactly, EXCEPT omit
  out-of-range scrape keys (see loop-doc ch27 note). This also unblocks the Book
  Treatment loop (a book is treatment-eligible only once its synthesis is done —
  **2 Chronicles + Ezra + Nehemiah + Esther + Job now eligible**; completing
  Psalms synthesis will finally unblock the long-pending Psalms treatment).
  Procedure: [agents/cow-synthesis-loop.md](agents/cow-synthesis-loop.md).
- [ ] **Book Treatment loop** — the single per-book study that fills the Studies
  tool: **one Full Treatment** per book (auto-assembled intro + synthesized
  multi-perspective commentary in per-chapter divisions, chapter picker +
  lazy-load for big books). One tracker, agent-claimed. Entry:
  [agents/study-pipeline.md](agents/study-pipeline.md); tracker:
  [agents/study-pipeline-tracker.md](agents/study-pipeline-tracker.md).
  **Eligibility: only books with complete COW synthesis** (38 today). Done:
  **Philemon** (seed), **Hebrews**, **Romans** (16 ch), **Revelation** (22 ch);
  34 eligible books remain. **Psalms is `⛔` blocked** — no COW synthesis; its
  overview `_book.json` is kept as a head-start (not wired), and it will need a
  big-book nav (grouped by the 5 books / search) before its 150-ch picker scales.
- [ ] **COW synthesis quality debt — 43% of the corpus is filler**
  *(audit done 2026-08-09, repair NOT started —
  [plans/cow-synthesis-quality-audit.md](plans/cow-synthesis-quality-audit.md))*.
  The 2026-07-22 mass batch (19,178 verses, 88% of the corpus) reached the
  350-word floor with stock carrier phrases and re-quoted scripture: 9,354
  grade-D verses across 356 chapters. Everything generated 07-23 onward is
  clean (0.0%), so the current per-chapter procedure is sound and the debt is
  historical. Anti-template lint recovered as
  `scripts/audit-synthesis-quality.py`. **Prevention is DONE (2026-08-09):** the
  six prose rules are in the loop prompt, the lint is a required pre-commit gate
  alongside the validator, and the owner chose the `thin` exemption for the
  350-word floor (source-checked, implemented in `validate-synthesis.py`).
  **Remaining: the repair itself** — ~9,354 grade-D verses in ~356 chapters,
  priority Romans, Hebrews, 1–2 Corinthians, Genesis, Exodus, Judges. Not
  started; needs an owner call on scope. **The loop is ready to run it**:
  `scripts/synthesis-frontier.py` derives both queues (generate / repair) from
  the qa metadata, `synthesis-loop.py` drives it unattended (verify → lint →
  fidelity → stamp → gate → commit, reverting anything that fails), and the
  repair procedure is documented in
  [agents/cow-synthesis-loop.md](agents/cow-synthesis-loop.md). Launch prompt:
  [agents/cow-synthesis-loop-prompt.md](agents/cow-synthesis-loop-prompt.md);
  the run's notebook is
  [agents/cow-synthesis-notes.json](agents/cow-synthesis-notes.json) — read it
  after a run, it is where an unattended loop puts what it could not stop to ask.
  **Scheduled since 2026-08-14**: two Routines fire a bounded 3-chapter batch
  every 30 minutes into a fresh session, using
  [agents/cow-synthesis-scheduled-prompt.md](agents/cow-synthesis-scheduled-prompt.md).
  Those runs overlap, so they pick with `--spread 40` and land work with
  `finish --push`, which drops a chapter another run already finished (exit 5)
  instead of clobbering it. Progress is the two meters in
  `synthesis-loop.py status`, not the number of runs.
  Note the lint cannot become a CI gate
  **The lint is now a CI gate** (`validate.yml`), exempting the legacy debt via
  `qa.standard` so it is green today while protecting all new and repaired work;
  the exempt count doubles as the repair progress meter. **The backlog is now
  machine-readable**: every verse carries a `qa` block with the standard it was
  written to and the grade it scored, so the repair loop can select work by
  query (`qa.grade == "D"`) instead of re-scanning. **Also found: 101 verses
  attribute views to a commentator absent from every source corpus** (98
  Ellicott, in Joshua and Nehemiah) — flagged `UNSOURCED` by the lint and
  recorded per-verse as `qa.ungrounded_voices`.
- [ ] **Provenance loop — add `_source` fields** across the data tree, AI-generated
  content first. [agents/provenance-loop.md](agents/provenance-loop.md).
- [ ] **Owner: run [REVIEW-CHECKLIST.md](REVIEW-CHECKLIST.md)** (19 points,
  2026-07-14). Item 13's answer (which dossier sections you use) gates the
  workshop.js purge below.
- [ ] **Recover from the other machine** (working/ tree): `site-overview.md`,
  `*_AGENT_GUIDE.md` / `*_SCRIPT_GUIDE.md`, `*_PROGRESS.md`, `MOTIFS_DESIGN.md`,
  `CODING_RULES.md`, `CODING_PHILOSOPHY.md`, and the generation scripts
  (`cow-merge.py`, `split-commentary.py`, `link-refs.py`, the anti-template
  lint). Commit knowledge into `docs/` + `scripts/`; then update the two
  MOTIFS_DESIGN pointers (`assets/js/biblepedia.js:49`,
  `data/biblepedia/motifs.json` note).
- [ ] **OL-DESK-PLAN Phase 4b** ([plans/OL-DESK-PLAN.md](plans/OL-DESK-PLAN.md)):
  `/translation/workshop/` → param-preserving redirect; purge dead
  translation/dashboard/queue/primer code from `assets/js/workshop.js`
  (5,600 lines); decide where the grammar primer resurfaces.

## Next

- [x] **One Full Treatment page** built — `topics/[book]/commentary.astro`: rich
  intro (overview, timeline, key people, vocabulary, language, reception, literary/
  cultural) + synthesized commentary in per-chapter divisions + per-chapter
  reflection + chapter-picker/lazy-load. **Philemon** seeds it. (2026-07-20 reshape
  collapsed the three tiers into this; the Guide/Study-Guide pages + docs were removed.)
- [ ] Retire/redirect the hand-authored `topics/psalms/` {index,deep-dive} pages +
  `study-guides/psalms/` once the Psalms Full Treatment is generated (reframe folds
  their content in — see [agents/study-pipeline.md](agents/study-pipeline.md)).
  **Done:** Hebrews, Romans, Revelation — their `topics/<book>/{index,deep-dive}`
  (+ `study-guides/hebrews/`) now redirect to the Full Treatment. Also still to do:
  the `/study-guides/` hub itself once Psalms is retired.
- [ ] Delete merged remote branch `claude/repo-overhaul-context-1ixq9c`
  (0 ahead of master; remote op — bundle with the next approved push).
- [ ] Audit leftovers ([archive/AUDIT.md](archive/AUDIT.md)): verse-ranking
  depth (proximity/length normalization); sw.js precache tiering (225 assets on
  install); phone reader-toolbar density; answers build scans the BSB twice;
  Desk A/B/C link groups; answers preview caps/notes.
- [ ] About page (`src/pages/about/index.astro`): its prompt copies now mirror
  `docs/agents/` — keep them in sync when prompts change.
- [x] **Discipline: catch-up + manual ticks** (2026-08-09) — two owner-reported gaps.
  (1) A missed reading-plan day was invisible and unmarkable: the card only ever
  showed *today*. Enrolled plans now carry a **catch-up list** (every past
  unmarked day, with its calendar date, its passage links and a tick), and the
  **full schedule is clickable**, so any day — past, today or ahead — can be
  marked or unmarked. That is the "select the date" path. (2) The home-page and
  Discipline checklists were read-only and purely auto-detected, so a devotional
  read on paper never counted. `tracker.js` now carries a **three-state manual
  override** per discipline per date (force-on / force-off / auto) that every
  `is*Done` consults first; the home checklist circles are buttons. Covered by
  27 unit assertions + 20 browser assertions (see the commit).
- [x] **Topical study: Assurance of Salvation** (2026-08-09) — five-part
  hand-authored study at `topics/salvation-assurance/` (`index` hub +
  `part-1`…`part-5`) on the `topic-guide.css` component set: the OT→NT thread of
  salvation, the competing verses read in context, seven traditions at their
  strongest, the tests of faith, and keeping the fire / the way back. Registered
  in the `topical` array of `data/books-content.json` so it lists under
  `/studies/`. Structure and pastoral balance (even-handed) were owner-chosen
  before drafting.
- [x] **Topical study: Korah's Rebellion** (2026-08-09) — five-part hand-authored
  study at `topics/korahs-rebellion/` (`index` hub + `part-1`…`part-5`) on the
  `topic-guide.css` component set. Registered in the `topical` array of
  `data/books-content.json` so it lists under `/studies/`. Part V (spiritual
  abuse) was owner-reviewed before the page was built.

## Done

→ [todo-archive.md](todo-archive.md)
