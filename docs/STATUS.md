# STATUS — live view

> Update this file in the same commit as the work it describes.
> Last updated: **2026-07-19** (restructure + COW repairs + 2 Kings 12)

- **Site**: LIVE at https://kingdombiblestudy.com — deploy on every push to
  master (owner approval required before pushing).
- **Design**: Daylight (2026-07-12).
- **Completed arcs** (records in [archive/](archive/)): Astro migration +
  rebrand ([OVERHAUL.md](archive/OVERHAUL.md)); Heights H1–H6, Desk D1–D5,
  A-gaps A1–A4 ([ROADMAP.md](archive/ROADMAP.md) — outside re-evaluation
  B+ → A−); adversarial audit fix batches P1–P6 ([AUDIT.md](archive/AUDIT.md));
  OL decomposition through Phase 4a / P26 / P27
  ([plans/OL-DESK-PLAN.md](plans/OL-DESK-PLAN.md)).
- **In flight**: COW synthesis — 587/1,189 chapters done (frontier:
  2 Kings 14); the 62 legacy validator failures (John 4, Luke 13, Genesis 41,
  1 Samuel 5) are repaired and the full corpus validates clean;
  OL Phase 4b pending the owner review ([REVIEW-CHECKLIST.md](REVIEW-CHECKLIST.md)).
- **Pending recovery**: the original `working/` guides + generation scripts
  live on the owner's other machine (see TODO).
- **CI**: `validate.yml` (data + library + synthesis validators, JS syntax,
  full build) on every push/PR; `deploy.yml` on master pushes.
- **2026-07-19 restructure**: planning docs centralized under `docs/`;
  `CLAUDE.md` hub added; agent prompts reconstructed into `docs/agents/`;
  gitignore knowledge-tracking policy reversed; historical migration tooling
  removed (`tools/convert-pages.mjs`, `diff-pages.mjs`, `tools/terms/`).
