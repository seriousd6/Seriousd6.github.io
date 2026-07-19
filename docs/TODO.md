# TODO — canonical task list

Rules: pick tasks here; mark yours `*(in progress — <date>)*`; move finished
items to [todo-archive.md](todo-archive.md) **in the same commit as the work**.
Keep [STATUS.md](STATUS.md) current in that same commit.

## Now

- [ ] **COW synthesis loop — resume at the frontier** (2 Kings 12; 603 chapters
  remain of 1,189). Procedure: [agents/cow-synthesis-loop.md](agents/cow-synthesis-loop.md).
- [ ] **COW repairs — 4 chapters fail `validate-synthesis.py`**: John 4 (all 54
  verses under-length — old degenerate run), Luke 13 (4 verses), Genesis 41
  (vv. 8, 12, 15 over-length), 1 Samuel 5 (v. 11 over-length). Regenerate/trim
  to the 350–650-word contract. CI stays red-on-push until these pass.
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
