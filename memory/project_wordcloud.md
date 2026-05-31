---
name: project_wordcloud
description: Word Cloud (J1) — implementation details, data pipeline, and architecture decisions
metadata:
  type: project
---

**J1 Word Cloud is complete (2026-05-30).** Hosted at `wordcloud/index.html`.

## Files created
- `wordcloud/index.html` — page HTML
- `assets/js/wordcloud.js` — ES module; init function `initWordCloudPage()`
- `assets/css/wordcloud.css` — styles
- `scripts/generate-wordcloud.py` — build script (run to regenerate `data/wordcloud/frequencies.json`)
- `data/wordcloud/frequencies.json` — pre-computed data (56 KB, 250 lemmas)

## Data pipeline
The build script loads all 66 interlinear files, counts Strong's number (lemma) occurrences, applies a ~50-entry stop list (Greek/Hebrew function words, prepositions, conjunctions, pronouns), and outputs the top 250 meaningful lemmas with per-testament and per-genre counts.

**Why:** The Strong's `gloss` field lists all translation options alphabetically, not the primary meaning. A `GLOSS_OVERRIDES` dict in the script overrides ~100 common words with clean primary glosses.

**How to apply:** If new interlinear data is added or stop list needs tuning, re-run `python3 scripts/generate-wordcloud.py` from the repo root.

## Architecture
- Spiral layout: pure-JS Archimedean spiral with canvas text measurement and bounding-box collision detection
- Scope filter: 10 buttons (Whole Bible / OT / NT / 7 genres) — all computed from the pre-built JSON, no re-fetch
- Proper noun toggle: `PROPER_IDS` Set in JS; hides Israel, David, Jesus, Moses, Egypt, Jerusalem, Jacob, Aaron, Solomon, Saul, and NT proper nouns
- Color scheme: Hebrew words = warm (amber/rust), Greek = cool (teal/indigo); shade varies by rank
- Detail panel: Strong's ID, lemma, transliteration, occurrence count, per-genre bar chart, link to Word Study page

## Wired into
- `app.js`: `import { initWordCloudPage } from './wordcloud.js'` + DOM check for `#wc-container`
- `main.js`: `{ label: '☁ Word Cloud', href: _r('wordcloud/') }` in tools nav
- `sw.js`: CSS, JS, HTML, and frequencies.json in SHELL_URLS (APP_CACHE_V → v35)

## Also completed same session
- E1 (Bible timeline) and E2 (Biblical maps) marked done in TODO — already fully implemented
- M5 (bible.js modularisation) marked done — 16-module ES split completed in prior session
