# TODO Workflow Guide

How to add, claim, complete, and archive work items for the Bible study site.
This is the single source of truth for TODO format. Both `audit-agent-guide.md` and
`LOOP_AGENT_PROMPT.md` defer to this file.

---

## Which File Gets the Item?

Before writing anything, decide where it belongs:

| Situation | File |
|---|---|
| Concrete bug or gap — specific file, function, symptom | `working/TODO.md` |
| Multi-session agent data generation (Z4–Z8 MKT commentaries) | `working/Deferred-Todo.md` |
| Long-term / out-of-scope / deprioritised (Phase O) | `working/Deferred-Todo.md` |
| Needs external data or copyright clearance that doesn't exist yet | `working/Deferred-Todo.md` |
| Already tracked anywhere | Do nothing — search before writing |

**Rule of thumb:** If a human or agent could act on the item in a single focused session today, it belongs in `TODO.md`. If it requires an external dependency, months of generation work, or a re-evaluation decision, it belongs in `Deferred-Todo.md`.

---

## Item Format (required)

Every item in `TODO.md` must follow this template exactly:

```markdown
### PREFIX-N · Short descriptive title *(HIGH / MEDIUM / LOW)*

**Problem:** One paragraph. What is broken, missing, or inconsistent?
Name the specific file(s) and function(s) where the issue lives.
Describe the observable symptom — what a user sees or cannot do.
Do not write vague items like "improve performance" or "add error handling".

**Fix:**
- [ ] `filename.js` (`functionName`): One-line description of the specific change.
- [ ] `filename.css`: Specific rule to add or change.
- [ ] Any other affected files, one line each.

Every Fix bullet **must** start with `- [ ]`. This is how an agent marks individual steps done
(`- [x]`) and how completion is tracked. A Fix bullet without a checkbox cannot be checked off
and the item cannot be properly archived.

**Verify:** One sentence. What to observe in the browser or console to confirm the fix worked.
```

### Priority labels

| Label | Meaning |
|---|---|
| **HIGH** | Broken behavior, data loss risk, or confusing UX on the main daily-use path |
| **MEDIUM** | Missing feature, degraded experience, or inconsistency visible to a regular user |
| **LOW** | Polish, edge case, minor visual issue, or rarely-reached flow |

### Prefix codes

| Prefix | Use for |
|---|---|
| `NAV-` | Navigation, routing, broken links, orphaned pages |
| `UX-` | User experience flows, empty states, loading states, error feedback |
| `CSS-` | Visual system, dark mode, typography, layout, responsiveness |
| `CODE-` | Code quality, comment discipline, architecture, coupling |
| `PWA-` | Offline, service worker, install flow, manifest |
| `DATA-` | Data files, missing JSON, broken fetch paths, schema mismatches |
| `PERF-` | Performance, unnecessary fetches, oversized data loads |
| `AUD-` | Audit-discovered items that don't fit a more specific prefix |
| `RI-` | Reader interlinear specific |
| `WS-` | Translation Workshop specific |

Assign the next unused number for the prefix. Check `working/todo-archive.md` and the current
`TODO.md` to find the highest existing number before picking the next one.

### What a good item looks like

Good:
> **Problem:** `assets/js/verse-study.js` lines 222–243 hides the prev/next link when at a chapter boundary. The user reaches John 3:36, the arrow disappears, and there is no way to advance to John 4:1 without leaving the page.

Bad:
> **Problem:** Navigation could be improved on the verse study page.

Good items name a file, a line or function, and describe a user-visible symptom. Bad items describe a category of work without grounding it in the code.

---

## How to Add an Item (step by step)

1. **Search first.** Grep `working/TODO.md` and `working/todo-archive.md` for the file or function name. If the item is already tracked or already done, stop.

2. **Decide the file.** Use the table at the top of this guide. If unsure, prefer `TODO.md` for actionable items.

3. **Find the right section.** Items go at the bottom of the most relevant existing section. If no section fits, add a new `##` section at the bottom of `TODO.md`, above the Audit Summary table.

4. **Write the entry** using the template above. All three fields (**Problem**, **Fix**, **Verify**) are required. A missing **Verify** is a sign the fix isn't concrete enough yet.

5. **Do not add items to `Deferred-Todo.md` during a loop/audit session.** That file is maintained manually by the project owner.

---

## How to Claim an Item

When an agent or session is about to work on an item, mark it claimed to prevent double work:

Append ` *(agent: in-progress)*` to the item's `###` heading line:

```markdown
### NAV-4 — verse-study chapter-boundary navigation dead-end *(MEDIUM)* *(agent: in-progress)*
```

Save the file. Re-read it to confirm the tag landed correctly.

**One session should claim no more than 2–3 items at a time.** Claiming 10 items and finishing 2 leaves stale in-progress tags that confuse future sessions.

---

## How to Mark an Item Complete

When all **Fix** checklist sub-items are done:

1. Change each `- [ ]` to `- [x]` on every sub-item you completed.
2. Remove the ` *(agent: in-progress)*` suffix from the heading.
3. If you only partially completed an item, leave `[ ]` on the remaining sub-items and add a brief note to the **Problem** field: `*(partially done: JS complete, CSS pending)*`. Do not mark the heading `[x]`.

---

## How to Archive a Completed Item

When an item is 100% complete (all sub-items `[x]`), move it out of `TODO.md`:

1. **Cut** the entire item block (heading + Problem + Fix + Verify) from `TODO.md`.
2. **Open** `working/todo-archive.md`.
3. **Find or create** a `## YYYY-MM-DD` heading for today's date at the top of the archive (the archive is newest-first).
4. **Paste** the item under that heading.
5. **Save both files.**

### Archive entry format

The archive entry keeps the original item format exactly — no reformatting needed. Just paste it under the date heading:

```markdown
## 2026-06-06

### NAV-4 — verse-study chapter-boundary navigation dead-end *(MEDIUM)*

**Problem:** ...
**Fix:** ...
**Verify:** ...
```

Items with `[x]`-only sub-items (everything checked) or fully-prose items (no checkboxes) are both fine to archive as-is.

---

## What NOT to Add to TODO.md

- Items already tracked (search before writing)
- Vague items without a specific file and symptom
- Z4–Z8 data generation tasks → those go in `Deferred-Todo.md` and `Z_PROGRESS.md`
- Phase O long-term stubs → `Deferred-Todo.md`
- Data-blocked items → `Deferred-Todo.md`
- "Refactor X" with no concrete bug or user-visible symptom
- Items that require modifying `CLAUDE.md`, `working/site-overview.md`, or agent guides
  (those are reference documents, not work items)

---

## Quick Reference Card

```
ADD:     Search first → decide file → find section → write Problem/Fix/Verify → assign PREFIX-N
CLAIM:   Append *(agent: in-progress)* to the ### heading
DONE:    [x] all sub-items, remove *(agent: in-progress)*
ARCHIVE: Cut from TODO.md → paste under ## YYYY-MM-DD in todo-archive.md
DEFER:   Does not fit today → Deferred-Todo.md (owner maintains that file)
```
