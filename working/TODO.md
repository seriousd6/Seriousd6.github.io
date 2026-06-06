# Bible Study Website — Working TODO

Track progress here. Mark items `[x]` when complete.
Completed items are archived in `working/todo-archive.md`.
Long-term, data-blocked, and Z/O category work lives in `working/Deferred-Todo.md` — not for the loop agent.

> **Before adding any item to this file, read `working/todo-workflow.md`.**
> It defines the required format (Problem / Fix / Verify), priority labels, prefix codes,
> and the rules for what belongs here vs. Deferred-Todo.md. Items without this format will
> be unclear to future agents and may be skipped.

---

## Open Bug Reports

### NAV-4 — verse-study chapter-boundary navigation dead-end *(MEDIUM)*

**Problem:** `assets/js/verse-study.js` lines 222–243. The prev/next verse navigation in `verse-study/` silently hides when it reaches a chapter boundary. At verse 1, `pv >= 1` is false → `prevNavLink` gets the `hidden` attribute. At the last verse (e.g., John 3:36), `chData[String(37)]` is undefined → `nextNavLink` gets `hidden`. A user studying verse-by-verse reaches the end of a chapter and the arrow simply vanishes — they must use "← Reader" and re-navigate to continue.

**Fix:**
- [ ] `assets/js/verse-study.js` (next-verse block, ~line 230): When `chData[String(nv)]` is undefined, instead of hiding `nextNavLink`, set its `href` to `VERSE_STUDY_URL + '?ref=' + encodeURIComponent(bookName + ' ' + (ch+1) + ':1')` and its label to `›› Ch {ch+1}`. Use `metaBooks[book].chapters` to guard against wrapping past the last chapter of the book.
- [ ] `assets/js/verse-study.js` (prev-verse block, ~line 222): When `pv < 1`, instead of hiding `prevNavLink`, show a chapter-level fallback link to `Ch {ch-1}` (or hide only at book chapter 1, verse 1).

**Verify:** Navigate to verse-study for the last verse of John 3 → next link shows `›› Ch 4` and links to John 4:1. Navigate to John 1:1 → prev link is absent (book start) or shows a chapter-level fallback.

---

### RI-D · Interlinear tile click — setTimeout dead weight *(MEDIUM)*

**Problem:** `assets/js/interlinear.js` — `_riShowPopover` (line 453). The core race condition is already fixed (`e.stopPropagation()` on tile click at line 116; `.ri-tile--active` applied at line 413). The `setTimeout(10ms)` wrapper at line 453 is now dead weight — it was needed to delay registering the outside-click listener, but `stopPropagation` makes the delay unnecessary. It adds fragile timing to a path that no longer needs it. Additionally, `.ri-tile` has no minimum touch target size.

**Fix:**
- [ ] `assets/js/interlinear.js` (`_riShowPopover`, line 453): Remove the `setTimeout` wrapper. Register the outside-click listener directly after the popover is inserted: `document.addEventListener('click', function _outside(e) { if (!pop.contains(e.target)) { pop.remove(); _riPopoverEl = null; if (_riActiveTile) { _riActiveTile.classList.remove('ri-tile--active'); _riActiveTile = null; } document.removeEventListener('click', _outside); } });`
- [ ] `assets/css/reader.css` (`.ri-tile` rule): Add `min-height: 44px;` for WCAG 2.5.5 touch target compliance.

**Verify:** Click an interlinear tile — immediate active highlight and popover, no flicker or immediate-close. Click outside — popover closes cleanly and active class is removed from the tile.

---

## Open Apocrypha Data Issues

*Audit pass 2026-06-05 (cycle 2). Cross-checked apocrypha version data against canon orders.*

### DATA-3 · BRENTON missing 3 OT data files *(MEDIUM)*

**Problem:** `data/bible-apocrypha/BRENTON/` is missing three books that the LXX canon order lists. The scope fix (changing `"scope"` to `"ot-only"` in `versions.json`) is already applied — the 27 NT 404s are gone. The remaining gap is in the data files themselves.

**Fix:**
- [ ] Re-run `scripts/fetch-apocrypha.py BRENTON --force` to populate the missing files.
- [ ] Confirm `data/bible-apocrypha/BRENTON/nahum.json` is created (was genuinely absent from the original fetch).
- [ ] Confirm `data/bible-apocrypha/BRENTON/daniel.json` is created (LXX Daniel base form, distinct from the additions file).
- [ ] Confirm `data/bible-apocrypha/BRENTON/esther.json` is created (canonical base form, distinct from `additions-esther.json`).

**Verify:** Open apocrypha reader, select BRENTON, navigate to Nahum — chapter loads without a 404 error.

---

### DATA-4 · DR apocrypha missing 4 Daniel/Esther additions *(LOW)*

**Problem:** `data/bible-apocrypha/DR/` has 73 files; the `dr` canon order in `apocrypha-canon-orders.json` lists 77. The four missing books are `additions-esther`, `prayer-of-azariah`, `susanna`, and `bel-and-dragon` — Daniel/Esther additions that the Douay-Rheims includes. Navigating to any of them shows a fetch error.

**Fix:**
- [ ] Re-run `scripts/fetch-apocrypha.py` targeting DR for `additions-esther`, `prayer-of-azariah`, `susanna`, `bel-and-dragon`.
- [ ] If the DR source treats these as chapters of Daniel/Esther rather than standalone books, update the `dr` entry in `data/apocrypha-canon-orders.json` to remove the standalone entries instead.

**Verify:** DR selected in apocrypha reader → navigate to Susanna → verses display, no fetch error.

---

### DATA-5 · WEB-CE missing 3 Daniel additions *(MEDIUM)*

**Problem:** `data/bible-apocrypha/WEB-CE/` has 74 files; the canon order lists 77. Missing: `bel-and-dragon`, `prayer-of-azariah`, `susanna`. These three Daniel additions ARE present in the WEB-CE upstream source — they were simply not fetched. A user selecting WEB-CE and navigating to Susanna sees a confusing "not available in this version" error.

**Fix:**
- [ ] Run `scripts/fetch-apocrypha.py` targeting WEB-CE for `bel-and-dragon`, `prayer-of-azariah`, `susanna`.
- [ ] Confirm the three files appear in `data/bible-apocrypha/WEB-CE/`.

**Verify:** WEB-CE selected in apocrypha reader → navigate to Susanna → verses display.

---

### DATA-6 · DR / KJV-APO / WEB-CE canonical books contaminated with Strong's markup *(HIGH)*

**Problem:** The 66 canonical book files in `data/bible-apocrypha/DR/`, `KJV-APO/`, and `WEB-CE/` contain Strong's interlinear annotations in the verse text — e.g. `In|strong="H0430"the|strong="H0853"beginning…`. Contamination rates: DR 87%, KJV-APO 100%, WEB-CE 99.8%. The deuterocanonical-specific books in the same directories are clean. Every canonical chapter in these three versions is unreadable.

**Fix:**
- [ ] Write `scripts/fix-apocrypha-strongs.py` that walks all three version directories, strips the pattern `\|strong="[HG]\d+"` (and surrounding whitespace artifacts) from every verse string, and writes files back in-place.
- [ ] Run the script and spot-check `DR/genesis.json` verse 1:1 — should read `"In the beginning God created the heaven and the earth."` with no pipe characters.

**Verify:** Open apocrypha reader, select DR, navigate to Genesis 1 — plain readable English, no `|strong=` artifacts anywhere in the verse text.

---

### DATA-7 · BRENTON missing spaces in verse text (~1% of verses) *(MEDIUM)*

**Problem:** Approximately 399 verses in `data/bible-apocrypha/BRENTON/` have adjacent words concatenated without spaces — e.g. `"Thebook"`, `"sonof"`, `"Loverighteousness"`. Root cause: USFM inline markers were not tokenised correctly during the original fetch, causing adjacent words to merge.

**Fix:**
- [ ] Preferred: Re-run `scripts/fetch-apocrypha.py BRENTON --force` with corrected USFM tokenisation. Recount the affected verses after re-fetch — the count should drop from ~399 to 0.
- [ ] Fallback (if re-fetch is not practical): Write a post-processing pass using `re.sub(r'([a-z])([A-Z])', r'\1 \2', text)` on all verse strings in the BRENTON directory. Low false-positive risk in Biblical text (no camelCase proper nouns).

**Verify:** `data/bible-apocrypha/BRENTON/tobit.json` verse 1:1 reads `"The book of the words of Tobit…"` not `"Thebook of the words of Tobit…"`.

---

### DATA-8 · additions-esther chapter count mismatch *(LOW)*

**Problem:** `data/apocrypha-books.json` declares `additions-esther` as 7 chapters, but both `data/bible-apocrypha/WEB-CE/additions-esther.json` and `data/bible-apocrypha/BRENTON/additions-esther.json` contain 10 chapters (Greek Esther continuous chapter numbering). The apocrypha reader hits a "chapter not found" error past chapter 7.

**Fix:**
- [ ] Inspect both files — note what chapter keys are present and what content they contain.
- [ ] Either update `data/apocrypha-books.json` `additions-esther` entry to reflect the correct chapter count (10), or restructure the data files to the declared 7-chapter schema if the source supports it.
- [ ] Update `data/apocrypha-canon-orders.json` chapter count field for `additions-esther` if changed.

**Verify:** Apocrypha reader with WEB-CE or BRENTON selected — navigate additions-esther chapter by chapter to the end without hitting a "chapter not found" error.

---

### DATA-9 · BRENTON Baruch missing chapter 6 (Letter of Jeremiah) *(LOW)*

**Problem:** `data/bible-apocrypha/BRENTON/baruch.json` has 5 chapters; `data/apocrypha-books.json` declares 6. Chapter 6 is the Letter of Jeremiah — a distinct text traditionally appended to Baruch in LXX manuscripts and included in Brenton's 1851 translation. Navigating to Baruch chapter 6 in the apocrypha reader returns a fetch/parse error.

**Fix:**
- [ ] Preferred: Re-run `scripts/fetch-apocrypha.py BRENTON --force` with corrected chapter handling to capture Baruch chapter 6.
- [ ] Fallback: Manually source Brenton's Baruch chapter 6 (73 verses, opening: `"The copy of an epistle, which Jeremy sent…"`) from Wikisource (public domain) and append to `baruch.json` as chapter key `"6"` with verse keys `"1"` through `"73"`.

**Verify:** `data/bible-apocrypha/BRENTON/baruch.json` has chapter keys 1–6. Navigating to Baruch chapter 6 in the apocrypha reader displays the Letter of Jeremiah text.

---

## Library Content Cleanup

- [x] **Newman Apologia `[Pg N]` spans** — stripped 418 `.pagenum` spans via BeautifulSoup.
- [x] **Smalcald Articles Part III sub-article `lib-article` nesting** — all 13 articles restructured.

*All other library expansion work complete — see archive. Blocked/deferred items in `Deferred-Todo.md`.*

---

## Audit Summary (reference)

The following dimensions were audited in June 2026. All findings from these audits have been implemented and archived in `working/todo-archive.md`.

| Dimension | Status |
|---|---|
| 1 — Code Comment Audit | Complete (CODE-1–10, 3 cycles) |
| 2 — Empty/Loading State Audit | Complete (UX-1–7, 3 cycles) |
| 3 — Mobile Responsiveness | Complete (CSS-1–14, 3 cycles) |
| 4 — Data Path Integrity | Complete (DATA-1–2, cycles 1–3; DATA-3–9 open above) |
| 5 — Feature Completeness | Complete (AUD-1, AUD-6, 3 cycles) |
| 6 — Performance | Complete (PERF-1–5, 3 cycles) |
| 7 — Visual System | Complete (CSS-7–14, 3 cycles) |
| 8 — Navigation & Discoverability | Complete (NAV-1–3; NAV-4 open above) |
| 9 — PWA & Offline | Complete (PWA-1–5) |
| 10 — Accessibility | Complete (AUD-2–5, 2 cycles) |

*Active open items from audit cycles are tracked above (DATA-3–9, NAV-4).*
