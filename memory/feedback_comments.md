---
name: feedback-comments
description: Always add purpose/intent comments to all code changes — functions, event wiring, data flows, and non-obvious constants
metadata:
  type: feedback
---

Always add comments explaining the **intended purpose** of code — not what the code literally does (names do that), but WHY it exists: what feature it enables, what problem it solves, what contract it fulfills.

**Why:** Without these comments, the purpose of individual pieces is lost when new features are added, IDs are renamed, or the codebase is revisited months later. This project has no build step, no type system, and no framework — comments are the primary layer of documentation.

**How to apply:**
- Every exported function: one-line comment stating its role in the app (e.g., "// Wires the search page input — called once after books/versions load")
- Every DOM ID lookup or attribute selector: comment what element it targets and why (e.g., "// Filter panel hidden by default — toggled by the Filter button")
- Every module-level variable: comment its purpose and lifetime
- Every non-obvious constant or data-attribute name: comment the contract (e.g., "// data-sort='canonical' means Bible book order; 'relevance' means score desc")
- Do NOT write comments that just restate the code ("increment counter by 1"); focus on intent and contracts

**Related:** [[feedback_testing]] (if added later)
