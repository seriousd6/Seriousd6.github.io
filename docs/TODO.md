# TODO — canonical task list

Rules: pick tasks here; mark yours `*(in progress — <date>)*`; move finished
items to [todo-archive.md](todo-archive.md) **in the same commit as the work**.
Keep [STATUS.md](STATUS.md) current in that same commit.

## Now

### Looping work — fills the Studies tool (`/studies/`)

> Shared architecture: [plans/book-capstone-plan.md](plans/book-capstone-plan.md).
> Each loop derives its frontier from the data tree, commits per work-unit, and
> must pass `python scripts/validate-commentary.py` (or `validate-synthesis.py`)
> before committing. No pushes without owner approval.

- [ ] **COW synthesis loop — continue at the frontier** (2 Kings 14; 602
  chapters remain of 1,189; corpus currently validates clean). Procedure:
  [agents/cow-synthesis-loop.md](agents/cow-synthesis-loop.md).
- [ ] **Book Commentary loop — the capstone** (Studies Tier 3). Full section→verse
  treatment per book: internal Cloud of Witnesses + attributed external sources,
  illuminated page. **Seed reference: Philemon** (overview + ch 1, live at
  `topics/philemon/commentary.html`). Frontier = first `(book, ch)` missing under
  `data/commentary/exposition/`. [agents/book-commentary-loop.md](agents/book-commentary-loop.md).
- [ ] **Book Guide loop** (Studies Tier 1) — general overview per book →
  `data/books/guide/<book>.json`. [agents/book-guide-loop.md](agents/book-guide-loop.md).
- [ ] **Bible Study Guide loop** (Studies Tier 2, formerly "Deep Dive") —
  chapter-by-chapter group session guides → `data/books/study-guide/<book>.json`.
  [agents/book-study-guide-loop.md](agents/book-study-guide-loop.md).
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

- [ ] **Generated pages for Tiers 1 & 2**: render Book Guide (`topics/[book]/`)
  and Bible Study Guide (`topics/[book]/deep-dive`) from the loop data via
  `getStaticPaths`, reusing the finished `book-study.css` `bk-*` template and
  excluding the 5 hand-authored literal dirs. The Tier 3 commentary page
  (`topics/[book]/commentary.astro`) is already built; these two are the next
  render step so the guide/study-guide loops light up their badges.
- [ ] Reconcile the legacy `/study-guides/` hub (5 hand-authored) with the per-book
  Bible Study Guide tier once the loop produces session data.
- [ ] The 5 hand-authored "Deep Dive" pages still hold scholarly content under the
  new **Bible Study Guide** label — superseded by the study-guide loop as it reaches
  each book (romans, psalms, revelation, hebrews, sermon-on-the-mount).
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
