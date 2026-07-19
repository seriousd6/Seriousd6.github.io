> Reconstructed 2026-07-19 from the public About page (src/pages/about/index.astro), the only surviving copy after the original gitignored working/ files were lost from this clone. Companion guides referenced below (e.g. TRANSLATION_AGENT_GUIDE.md, BS_AGENT_GUIDE.md, MKT_PROGRESS.md, site-overview.md) are still pending recovery from the owner's other machine — treat missing references accordingly.

## Before doing anything else, read these files in full, in order:

1. `CLAUDE.md` — project constraints, comment requirements, what not to do
2. `docs/site-overview.md` (pending recovery) — architecture, module map, CSS system, localStorage keys
3. `CODING_RULES.md` — hard syntax and pattern rules for this codebase
4. `CODING_PHILOSOPHY.md` — how to think about changes, scope discipline

Do not skip any of these. They are short and will save you from expensive mistakes.

---

## Step 1 — Pick 2–3 work items from `docs/TODO.md`

Read `docs/TODO.md` in full first. Then apply these filters:

### Skip entirely:
- The entire **Z4–Z8 MKT Commentary Suite** section
- The entire **Phase Z — Modern Kingdom Translation** section
- The entire **Phase O — Long-term / Deferred** section
- Any row marked `*(claimed — see docs/inprogress-*.md)*`
- Any item that contains `DATA BLOCKED`
- Any item whose Fix says `"Agents generate …"` — those are data-generation tasks

### Prefer:
- **HIGH** priority items before MEDIUM, MEDIUM before LOW
- Items whose **Fix** section names specific files and functions
- Items touching only 1–3 files
- Items where all prerequisite infrastructure items are already checked off

---

## Step 2 — Verify the items are real work

For each item you've selected, before claiming it:
1. Locate the file and function named in the **Problem** section
2. Confirm the described issue actually exists in the current code
3. If the item was already fixed silently, mark it [x] and pick a different item

---

## Step 3 — Claim the items

In `docs/TODO.md`, append ` *(agent: in-progress)*` to each item's heading line.
Save the file. Re-read it to confirm the change landed.

---

## Step 4 — Study the relevant files

For each claimed item, read:
- The file(s) named in the **Problem** section
- Any sibling functions that the Fix will affect
- The corresponding `.css` file if CSS changes are part of the Fix
- `docs/site-overview.md` if you need architectural context

Read enough to understand **why** the current code works before changing it.

---

## Step 5 — Implement

**Before writing a single line of code:**
- Re-read `CODING_RULES.md` Section 3 (comment requirements) and Section 1 (JS syntax)
- Confirm you know which CSS file to edit
- Confirm you know which module to import from

**While implementing:**
- Add `// INTENT:` / `// CHANGE?` / `// VERIFY:` comments per CLAUDE.md — required
- Use `var` not `let`/`const` — this codebase uses `var` consistently throughout
- Use `'use strict';` at the top of any new JS file
- Do not touch code outside the Fix checklist

---

## Step 6 — Verify the work

For JS changes:
- Trace through the function from call site to output
- Check that every code path (happy path + error/missing-data path) is handled
- Confirm any new localStorage reads/writes use the right key
- Confirm any new fetch() calls have a .catch() handler

For CSS changes:
- Confirm selector specificity won't be overridden by existing rules
- Confirm dark mode is handled (`[data-theme="dark"]` override)
- Confirm `var(--color-*)` is used instead of hardcoded hex

---

## Step 7 — Mark complete and summarize

For each completed item in `docs/TODO.md`:
1. Change [ ] to [x] on every sub-item you completed
2. Remove the *(agent: in-progress)* suffix from the heading
3. If partially complete, note what remains

After updating the file, write a brief summary: what changed, which files were modified,
any edge cases or caveats. Move completed tasks to docs/todo-archive.md.

---

## Key facts about this codebase

| Thing | Where it lives |
|---|---|
| Path constants (DATA_ROOT, READER_URL, etc.) | `assets/js/core.js` |
| Bible version state | `localStorage['bsw_version']`, getVersion() / setVersion() in core.js |
| All fetch caches | Module-level var in each feature module |
| Dark mode | `[data-theme="dark"]` attribute on body, toggled by storage.js |
| Reference link wiring | wireRefLinks() in wire.js — called after any DOM insertion |
| Scripture reference format | `<a class="ref" data-ref="Book Ch:V">display text</a>` |
| localStorage key prefix | bsw_ — always |
| CSS variable root | assets/css/style.css :root {} block |
| Per-feature CSS | assets/css/{feature}.css — one per feature module |
| Service worker cache | sw.js — APP_CACHE_V bump required on every code deploy |
