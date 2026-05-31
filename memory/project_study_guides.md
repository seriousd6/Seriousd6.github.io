---
name: project-study-guides
description: Study guides section — location, format, authoring conventions, and what's been built
metadata:
  type: project
---

Study guides live at `study-guides/{slug}/index.html` — distinct from `topics/` (thematic essays) and `library/` (historical documents). Per N3 in TODO.md.

**Format:** Chapter-by-chapter static HTML. No JSON data files. No build step.

**CSS classes introduced (pending study-guide.css):** `sg-chapter-header`, `sg-chapter-num`, `sg-chapter-ref`, `sg-wave`, `sg-ot-context`, `sg-warning`, `sg-warning__label`, `sg-questions`, `sg-questions__list`, `sg-overview-table`, `sg-divider`. An inline `<style>` block handles these until the CSS file is created. Uses existing `topic-guide.css` classes for the hero and section layout.

**Per-chapter structure:**
1. `.sg-chapter-header` badge + chapter reference
2. `.sg-wave` — what the argument is doing here
3. Teaching content with `.tg-note.sg-ot-context` boxes for each major OT citation (original context first, then how Hebrews deploys it)
4. `.sg-warning` boxes for the 5 warning passages
5. `.sg-questions` — 5 discussion questions per chapter

**Built so far:**
- `study-guides/hebrews/index.html` — 13-chapter Hebrews study guide (complete)
  - All 5 warning passages marked (2:1-4; 3:7-4:11; 6:4-8; 10:26-31; 12:25-29)
  - Major OT texts treated in original context: Ps 2, 8, 22, 40, 45, 95, 102, 110, 110:4; 2 Sam 7; Gen 2, 14, 22; Exod 19, 24, 25; Lev 16; Num 12/13-14; Jer 31; Hab 2; Hag 2; Prov 3; Deut 31/Josh 1; Ps 118

**Why:** User wants detail, OT context for full understanding, and the group to "ride the wave of the arguments." Another agent is handling navigation/access layer (index page, CSS file, nav integration).
