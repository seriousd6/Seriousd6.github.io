
## Before doing anything else, read these files in full, in order:

1. `CLAUDE.md` — project constraints, comment requirements, what not to do
2. `working/site-overview.md` — architecture, module map, CSS system, localStorage keys
3. `CODING_RULES.md` — hard syntax and pattern rules for this codebase
4. `CODING_PHILOSOPHY.md` — how to think about changes, scope discipline
5. `working/todo-workflow.md` — required format for reading, claiming, completing, and archiving TODO items

Do not skip any of these. They are short and will save you from expensive mistakes.

---

## Step 1 — Pick 2–3 work items from `working/TODO.md`

Read `working/TODO.md` in full first. The file contains only actionable items — Z, O, and blocked
work has already been separated into `working/Deferred-Todo.md`. See `working/todo-workflow.md`
for the full decision rules.

### Skip:
- Any item marked ` *(agent: in-progress)*` — it's being worked by another session
- Any item that contains `DATA BLOCKED` — external data is unavailable
- Any item whose Fix says `"Agents generate …"` — data-generation tasks, not site code

### Prefer:
- **HIGH** priority items before MEDIUM, MEDIUM before LOW
- Items whose **Fix** section names specific files and functions — you can act on these directly
- Items touching only 1–3 files — avoid sessions that balloon across the whole codebase
- Items where all prerequisite `[x]` infrastructure items are already checked off
- Self-contained LOW items after HIGH/MEDIUM work is exhausted — they ship cleanly

### Good session shapes:
- Two HIGH items from the same feature area (e.g., two DATA-* items touching the same fetch script)
- One HIGH + two LOW items from different areas
- Three MEDIUM items that are independent

### Warn and stop if:
- Every non-claimed, non-blocked item in the list is already `[x]` → report complete and exit
- You cannot find 2 items that meet the criteria → pick 1 and explain why

---

## Step 2 — Verify the items are real work

For each item you've selected, before claiming it:

1. Locate the file and function named in the **Problem** section
2. Confirm the described issue actually exists in the current code (read the function)
3. If the item says it was `[x]` already but doesn't look done, the checkbox was wrong:
   - Mark it `[x]` and pick a different item

If an item's described problem does NOT exist (i.e., it was silently fixed by earlier work),
mark it `[x]` in `working/TODO.md` and pick another item.

---

## Step 3 — Claim the items

In `working/TODO.md`, append ` *(agent: in-progress)*` to each item's heading line.
Save the file. Re-read it to confirm the change landed.

Example:
```
### RD-J · Attribution Line — Suppress for Single-Verse Results *(LOW)* *(agent: in-progress)*
```

---

## Step 4 — Study the relevant files

For each claimed item, read:
- The file(s) named in the **Problem** section — find the exact function
- Any sibling functions that the Fix will affect (imports, callers, re-exports)
- The corresponding `.css` file if CSS changes are part of the Fix
- The matching section of `working/site-overview.md` if you need architectural context

Read enough to understand **why** the current code works the way it does before changing it.
Do not skim. A 10-minute read avoids an hour of debugging.

---

## Step 5 — Implement

Work through each item's **Fix** checklist line by line.

**Before writing a single line of code:**
- Re-read `CODING_RULES.md` Section 3 (comment requirements) and Section 1 (JS syntax)
- Confirm you know which CSS file to edit (every feature has its own `.css` file)
- Confirm you know which module to import from (paths come from `core.js`, never hardcoded)

**While implementing:**
- Add `// INTENT:` / `// CHANGE?` / `// VERIFY:` comments per CLAUDE.md — these are required
- Use `var` not `let`/`const` — this codebase uses `var` consistently throughout
- Use `'use strict';` at the top of any new JS file
- Do not touch code outside the Fix checklist — scope creep is the enemy of a clean session
- Dark mode: any new CSS rule using `--color-*` vars that needs a dark variant → add it under `[data-theme="dark"]`

**Do not:**
- Add `console.log` calls (use `console.warn` only for genuine error states)
- Introduce new `localStorage` keys without the `bsw_` prefix
- Hardcode paths — use the constants from `core.js`
- Touch `sw.js` unless the Fix explicitly requires it (cache busting is destructive if done wrong)
- Modify `CLAUDE.md`, `working/site-overview.md`, or other agent guides during an implementation session

---

## Step 6 — Verify the work

No browser is available in most loop contexts. Verify by careful code reading:

**For JS changes:**
- Trace through the function from call site to output — does the logic produce the described fix?
- Check that every code path (happy path + error/missing-data path) is handled
- Confirm any new `localStorage` reads/writes use the right key
- Confirm any new `fetch()` calls have a `.catch()` handler

**For CSS changes:**
- Confirm the selector specificity won't be overridden by an existing rule
- Confirm dark mode is handled if needed (`[data-theme="dark"]` override)
- Confirm `var(--color-*)` is used instead of any hardcoded hex

**For HTML changes:**
- Confirm all scripture references use `<a class="ref" data-ref="Book Ch:V">` not bare text
- Confirm `<script>` tags are at the end of `<body>` in the right order:
  `main.js` (sync) then `app.js` (module)

**Spot-check:**
Re-read the original **Problem** description. Ask: does my change actually address it?
If the answer is "mostly" or "partially" — either finish it or note what was left undone in the TODO entry.

---

## Step 7 — Mark complete and summarize

See `working/todo-workflow.md` for the full rules. Quick version:

For each completed item in `working/TODO.md`:
1. Change `[ ]` to `[x]` on every sub-item you completed.
2. Remove the ` *(agent: in-progress)*` suffix from the heading.
3. If only partially done, leave `[ ]` on remaining sub-items and note: `*(partially done: JS complete, CSS pending)*`

**If 100% complete — archive it:**
1. Cut the entire item block from `TODO.md`.
2. Open `working/todo-archive.md`.
3. Add or find a `## YYYY-MM-DD` heading for today at the top of the archive (newest-first).
4. Paste the item under that heading.
5. Save both files.

**If partially complete:** Update the Problem/Fix description to reflect what remains. Keep it in `TODO.md`.

After all items are handled, write a brief summary:
- What was changed, which files were modified
- Any edge cases or caveats the next session should know about

---

## Key facts about this codebase

| Thing | Where it lives |
|---|---|
| Path constants (DATA_ROOT, READER_URL, etc.) | `assets/js/core.js` |
| Bible version state | `localStorage['bsw_version']`, `getVersion()` / `setVersion()` in `core.js` |
| All fetch caches | Module-level `var` in each feature module (e.g., `_commCache` in `reader.js`) |
| Cross-module callbacks | Registered in `assets/js/app.js` via `onVersionChange()` etc. |
| Dark mode | `[data-theme="dark"]` attribute on `<body>`, toggled by `storage.js` |
| Reference link wiring | `wireRefLinks()` in `wire.js` — called after any DOM insertion with `.ref` links |
| Scripture reference format | `<a class="ref" data-ref="Book Ch:V">display text</a>` |
| localStorage key prefix | `bsw_` — always |
| CSS variable root | `assets/css/style.css` `:root {}` block |
| Per-feature CSS | `assets/css/{feature}.css` — one per feature module |
| Service worker cache | `sw.js` — `APP_CACHE_V` bump required on every code deploy |
| Python scripts | `scripts/` — offline data generation only, never run on-site |
