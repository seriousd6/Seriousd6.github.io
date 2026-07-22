# STATUS — live view

> Update this file in the same commit as the work it describes.
> Last updated: **2026-07-22** (Full Treatments: Romans + Revelation; treatment
> eligibility tied to COW synthesis; **2 Kings + 1 Chronicles COW synthesis
> complete → 52.7%**, frontier now 2 Chronicles)

- **Site**: LIVE at https://kingdombiblestudy.com — deploy on every push to
  master (owner approval required before pushing).
- **Design**: Daylight (2026-07-12). Self-hosted font subsets extended to
  **Greek + Greek-Extended (polytonic) + Latin-Extended** (2026-07-21) so
  original-language notes (Greek words, macron transliterations) render in
  Literata rather than a mismatched/absent OS fallback — still fully self-hosted
  (no external fonts). Build auto-precaches them + bumps `APP_CACHE_V`.
- **Completed arcs** (records in [archive/](archive/)): Astro migration +
  rebrand ([OVERHAUL.md](archive/OVERHAUL.md)); Heights H1–H6, Desk D1–D5,
  A-gaps A1–A4 ([ROADMAP.md](archive/ROADMAP.md) — outside re-evaluation
  B+ → A−); adversarial audit fix batches P1–P6 ([AUDIT.md](archive/AUDIT.md));
  OL decomposition through Phase 4a / P26 / P27
  ([plans/OL-DESK-PLAN.md](plans/OL-DESK-PLAN.md)).
- **In flight (active focus)**: **COW synthesis — 627/1,189 chapters = 52.7%.**
  NOT a single canonical frontier: **Genesis→1 Chronicles and the entire NT are
  complete** (2 Kings + all 29 chapters of 1 Chronicles finished 2026-07-22 via
  calibrated fan-outs — genealogy + narrative profiles both calibrated; each
  chapter hard-read + validated before commit); the gap is now the OT back-half
  (**2 Chronicles → Malachi** + the poetic/wisdom books). OT frontier =
  **2 Chronicles 1**. Advancing this loop is
  the current focus — it also gates the Studies tool, since a book earns a Full
  Treatment only after its synthesis is done (see below). The
  62 legacy validator failures (John 4, Luke 13, Genesis 41, 1 Samuel 5) are
  repaired and the full corpus validates clean; OL Phase 4b pending the owner
  review ([REVIEW-CHECKLIST.md](REVIEW-CHECKLIST.md)).
- **Studies — one Full Treatment per book (reshaped 2026-07-20)**: the earlier
  three tiers were **collapsed into a single per-book page** — a rich intro
  (overview, **timeline**, key people, key vocabulary, language notes, reception,
  literary/cultural — auto-consolidated from the existing data trees) followed by
  the synthesized commentary in per-chapter divisions (original-language /
  historical / Christ lenses, verse-by-verse, Cloud of Witnesses + attributed
  external scholarship, per-chapter "For reflection"), with a chapter picker +
  lazy-load for many-chapter books. Page `topics/[book]/commentary.astro` +
  `assets/js/entries/commentary.js` + `assets/css/commentary.css`; one loop + one
  tracker ([agents/study-pipeline.md](agents/study-pipeline.md)). **Done (4/66):**
  **Philemon** (seed, 1 ch), **Hebrews** (13 ch), **Romans** (16 ch), and
  **Revelation** (22 ch) — Romans + Revelation generated 2026-07-22 via a 38-agent
  fan-out (overviews hand-written; chapters by subagents; each validated + BSB
  versification-checked before commit). Their hand-authored `topics/<book>/
  {index,deep-dive}` pages now redirect to the treatment. **Eligibility (owner,
  2026-07-22):** a book is treatment-ready ONLY when its COW synthesis is
  complete — **38 books qualify today** (Genesis–1 Kings + all NT); 34 remain
  eligible. **Psalms is `⛔` blocked** — it has NO synthesis; its overview
  `_book.json` is kept as a head-start, but no chapters were generated and it is
  not wired live. (It will also need a big-book nav — grouped by the 5 books /
  search — before its 150-chapter picker scales.) The Guide/Study-Guide tiers,
  pages, data, and stage docs were removed.
  Guarded by `scripts/validate-commentary.py` (CI). Note: the earlier 3-tier commit
  was pushed but its deploy is stuck in an ongoing GitHub Actions outage; all of
  this supersedes it and is **local-only pending review**.
- **Pending recovery**: the original `working/` guides + generation scripts
  live on the owner's other machine (see TODO).
- **CI**: `validate.yml` (data + library + synthesis validators, JS syntax,
  full build) on every push/PR; `deploy.yml` on master pushes.
- **2026-07-19 restructure**: planning docs centralized under `docs/`;
  `CLAUDE.md` hub added; agent prompts reconstructed into `docs/agents/`;
  gitignore knowledge-tracking policy reversed; historical migration tooling
  removed (`tools/convert-pages.mjs`, `diff-pages.mjs`, `tools/terms/`).
