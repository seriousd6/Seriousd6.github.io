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
  2026-07-22)*. **627/1,189 = 52.7% done** (Genesis→**1 Chronicles** + the whole
  NT complete; corpus validates clean). **2 Kings + 1 Chronicles finished
  2026-07-22** (genealogy + narrative fan-out profiles both calibrated). Frontier
  = **2 Chronicles 1**; the remaining OT back-half is 2 Chronicles → Malachi +
  the poetic/wisdom books (~562 ch). Genealogy chapters synthesize from raw catena
  fine (commentators discuss the names) — mirror the source's sparse verse keys
  exactly. This also unblocks the Book Treatment loop (a book is treatment-eligible only
  once its synthesis is done). Procedure:
  [agents/cow-synthesis-loop.md](agents/cow-synthesis-loop.md).
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

## Done

→ [todo-archive.md](todo-archive.md)
