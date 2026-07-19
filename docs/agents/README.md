> Reconstructed 2026-07-19 from the public About page (src/pages/about/index.astro), the only surviving copy after the original gitignored working/ files were lost from this clone. Companion guides referenced below (e.g. TRANSLATION_AGENT_GUIDE.md, BS_AGENT_GUIDE.md, MKT_PROGRESS.md, site-overview.md) are still pending recovery from the owner's other machine — treat missing references accordingly.

# Agent Prompts & Guides — Index

- `mkt-translation-agent.md` — MKT Translation Agent Prompt: claim a work unit and write a static Python script producing the three-tier Modern Kingdom Translation (formerly `working/MKT_AGENT_PROMPT.md`).
- `book-study-agent.md` — Book Study Agent Prompt plus the surviving BS Agent Guide excerpt: per-book key vocabulary, language notes, reception, and reading guide (formerly `working/BS_AGENT_PROMPT.md` + excerpt of `working/BS_AGENT_GUIDE.md`).
- `loop-agent.md` — Loop Agent Prompt: general UI/code maintenance loop driven by the TODO queue, including the codebase map table (formerly `working/LOOP_AGENT_PROMPT.md`).
- `provenance-loop.md` — Short description of the provenance loop that adds `"_source"` fields to JSON data files (formerly `working/PROVENANCE_AGENT_GUIDE.md`; only the description survives).

## Provenance note

These files were reconstructed on 2026-07-19 by extracting the verbatim prompt texts embedded in the public About page (`src/pages/about/index.astro`), after the original gitignored `working/` copies were lost from this clone. Stale `working/…` paths inside the prompts were updated to their new `docs/…` locations (e.g. `working/TODO.md` → `docs/TODO.md`, `working/site-overview.md` → `docs/site-overview.md`); no other content changes were made. Companion documents still pending recovery from the owner's other machine: TRANSLATION_AGENT_GUIDE.md, MKT_STATIC_SCRIPT_GUIDE.md, MKT_PROGRESS.md, BS_AGENT_GUIDE.md (full version), BS_SCRIPT_GUIDE.md, BS_PROGRESS.md, site-overview.md, CODING_RULES.md, CODING_PHILOSOPHY.md, CLAUDE.md, PROVENANCE_PROGRESS.md, TODO.md, todo-archive.md.
