# STATUS — live view

> Update this file in the same commit as the work it describes.
> Last updated: **2026-08-09** (Psalms 21 COW synthesis repaired — CI green again;
> two new five-part topical studies: Korah's Rebellion and Assurance of Salvation.
> Previously 2026-08-02: Full Treatments Romans + Revelation; treatment
> eligibility tied to COW synthesis; **Job (42/42) COW synthesis complete →
> 62.1%**, frontier now Psalms 1)

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
- **In flight (active focus)**: **COW synthesis — 738/1,189 chapters = 62.1%.**
  NOT a single canonical frontier: **Genesis→Job and the entire NT are complete**
  (2 Chronicles + Ezra + Nehemiah + Esther + all 42 of **Job** finished —
  genealogy/register + narrative + dialogue-poetry profiles all calibrated;
  each chapter validated + scrape-meta-scanned + anti-templating-checked before
  commit); the gap is now the OT back-half (**Psalms → Malachi** + the remaining
  poetic/wisdom books). OT frontier = **Psalms 1** (pure Hebrew poetry, 150 ch).
  Advancing this loop is
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
- **Multi-part studies use sub-tabs (2026-08-09)**: a five-part study is one
  page with a sticky part-picker, not five linked pages — the same paradigm as
  the book-commentary chapter picker (`.bkc-chapternav`), reused as the generic
  `.tg-tabs` component in `topic-guide.css` + `assets/js/entries/study-tabs.js`.
  Every panel ships in the HTML and is hidden by JS, so with scripting off the
  study degrades to one long readable page. Both five-part studies are converted —
  Korah's Rebellion and Assurance of Salvation — with their old `part-N.html`
  URLs kept as redirect stubs to `#part-N`. The transform itself is a tracked
  tool, `scripts/compose-study-tabs.py`, which infers accent, hero variant,
  titles and part bodies from the existing files, so a future multi-part study
  converts in one command.
- **One registry, enforced (2026-08-09)**: `data/books-content.json` is the
  single source of truth for what the site offers. `/topics/index.html` had
  looked like a second registry — it carries (carried) a hand-maintained card
  grid — but has redirected to `/studies/` since the Studies reshape, so its
  cards rendered for nobody; **church-authority sat live and unreachable**
  because it was registered only there. It is now in `topical[]`, the dead grid
  is removed, and `scripts/validate-topics-registry.py` fails CI if any live
  study under `src/pages/topics/<slug>/` is missing from the registry.
- **Topical studies (hand-authored, separate from the book pipeline)**: eight
  live under `topics/`, listed via the `topical` array in
  `data/books-content.json`. Both newest ones are five-part studies built on the
  `topic-guide.css` component set with no per-study CSS; each part carries its
  own sticky TOC, further-reading list, and prev/next nav.
  **Assurance of Salvation (2026-08-09)** at `topics/salvation-assurance/`
  (`index` hub + `part-1`…`part-5`): the OT→NT thread of salvation; the keeping
  and warning texts read in context with the six hardest passages worked closely;
  seven traditions each stated at its strongest with its weakest link; the tests
  Scripture gives and how to run them; keeping the fire and the way back.
  Even-handed by owner direction — comfort and warning held in tension rather
  than one traded for the other. It represents all seven traditions at their
  strongest but **does adjudicate**: Part II demonstrates in a 14-row table that
  three of the five harmonising strategies are one reading which carries every
  hard text without forcing any, and Part III states the verdict plainly,
  separating exegetical strain (a real defect) from metaphysical mystery (which
  Scripture itself retains). The hub says where it lands up front.
  **Korah's Rebellion (2026-08-09)** at
  `topics/korahs-rebellion/`: text/composition/reception, the theological sprawl,
  the divided church, the NT's answer, and spiritual abuse. Its Part V was drafted
  and owner-reviewed before the pages were built.
- **COW synthesis quality (2026-08-09)**: full-corpus audit found **43% of
  Commentary A is degenerate filler** — 9,354 grade-D verses in 356 chapters,
  all from the single 2026-07-22 mass batch; everything generated since is
  clean. The validators never saw it (they check length, not whether length was
  earned). The lost **anti-template lint is recovered** as
  `scripts/audit-synthesis-quality.py`. Audit + proposed prompt fixes:
  [plans/cow-synthesis-quality-audit.md](plans/cow-synthesis-quality-audit.md).
  **Prevention is in place** (2026-08-09): six prose rules added to the loop
  prompt, the lint is a required pre-commit gate, and the `thin` exemption now
  lets genuinely sparse verses come in at 120–349 words — validated against the
  source (catena ≤ 200 words), so the flag cannot excuse a lazy entry. The lint
  also now checks **fidelity** — 101 verses name a commentator with no comment on
  that chapter in any source corpus (98 Ellicott; his corpus skips Joshua 12 and
  Nehemiah 7, which is exactly where the invention is). Every verse carries a
  per-verse `qa` block (standard, date, grade, checks performed), so the repair
  backlog is machine-readable, **fidelity is self-graded per verse** (the one
  check no script can make — `synthesis-fidelity.py` supplies the read-back and
  the signals; a verse without a grade will not stamp), and **the lint runs as a
  CI gate** — a ratchet
  that exempts the legacy debt by `qa.standard`, fails any unstamped verse, and
  refuses to let the exempt set grow. No regeneration of the debt has started, but **the loop is ready to start it** —
  `scripts/synthesis-frontier.py` serves both queues from the metadata
  (generate: 432 chapters; repair: 447), and `backfill-synthesis-qa.py
  --standard current` stamps finished work, refusing anything that grades C/D or
  names an ungrounded voice. `synthesis-loop.py` runs the whole cycle unattended; the launch prompt is
  `docs/agents/cow-synthesis-loop-prompt.md` and the run writes what it could
  not stop to ask into `docs/agents/cow-synthesis-notes.json`.
- **Disciplines (2026-08-09)**: completion is no longer purely auto-detected.
  `assets/js/tracker.js` resolves every discipline as *manual override → derived*,
  where the override is three-state (`true` force-on / `false` force-off / absent
  = auto) and stored per date under `bsw_tracker[date].manual`. `markDone`,
  `getStatus` and every `is*Done` take an optional date, so past days are
  addressable. The home-page checklist circles are buttons (`toggleManual`), and
  a toggle that lands back on the detected value *clears* the override rather
  than pinning it. Reading plans gained a **catch-up list** of past unmarked days
  and a **clickable full schedule** (`setDayDone(planId, dayNum, done)` writes
  `bsw_plans[...].completed[day] = <date>`, which is what tracker reads back).
  Disclosure state lives outside the cards so marking a day does not collapse
  what is open.
- **Pending recovery**: the original `working/` guides + generation scripts
  live on the owner's other machine (see TODO).
- **CI**: `validate.yml` (data + library + synthesis validators, JS syntax,
  full build) on every push/PR; `deploy.yml` on master pushes.
- **2026-07-19 restructure**: planning docs centralized under `docs/`;
  `CLAUDE.md` hub added; agent prompts reconstructed into `docs/agents/`;
  gitignore knowledge-tracking policy reversed; historical migration tooling
  removed (`tools/convert-pages.mjs`, `diff-pages.mjs`, `tools/terms/`).
