> Reconstructed 2026-07-19 from the public About page (src/pages/about/index.astro), the only surviving copy after the original gitignored working/ files were lost from this clone. Companion guides referenced below (e.g. TRANSLATION_AGENT_GUIDE.md, BS_AGENT_GUIDE.md, MKT_PROGRESS.md, site-overview.md) are still pending recovery from the owner's other machine — treat missing references accordingly.

# Provenance Loop

Description extracted from the About page's "Citation & Provenance System" section. The full agent guide (originally `working/PROVENANCE_AGENT_GUIDE.md`, now this file's slot) is otherwise lost; only this description survives.

Every piece of data on this site is mapped to its source in `data/provenance.json`. Pages that render data from AI-assisted sources display an "AI-assisted · details" badge. Pages that render verbatim public-domain scholarship display a badge such as "Barnes Notes · 1832–1885 · Public Domain".

An ongoing looping process (this guide — `docs/agents/provenance-loop.md`) progressively adds a `"_source"` field to individual JSON data files, prioritizing AI-generated content first. The progress is tracked in `docs/provenance_progress.md` (pending recovery). As this work proceeds, more of the raw data files will carry inline source attribution in addition to the UI badges.
