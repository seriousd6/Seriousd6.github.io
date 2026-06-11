# Provenance Annotation Progress

Tracks the looping pass that adds `_source` fields to data files.
See `PROVENANCE_AGENT_GUIDE.md` for schema, rules, and script pattern.

**Last updated:** 2026-06-10

## Summary

| Status | Count |
|--------|-------|
| Complete | 0 |
| In Progress | 0 |
| Not Started | 27 |

---

## Work Queue

Priority ordering: AI-generated content first (most important to annotate), then
external data. Large directories (hundreds of files) annotate only the `index.json`.

| # | Directory / File | Type | Files | Approach | Script | Status |
|---|-----------------|------|-------|----------|--------|--------|
| 1 | `data/workshop/book-study/` | ai_assisted | 66 | per-file | `scripts/annotate-book-study.py` | not started |
| 2 | `data/translation/draft/literal/` | ai_assisted | ~54 | per-file | `scripts/annotate-translation-literal.py` | not started |
| 3 | `data/translation/draft/mediating/` | ai_assisted | ~54 | per-file | `scripts/annotate-translation-mediating.py` | not started |
| 4 | `data/translation/draft/thought/` | ai_assisted | ~54 | per-file | `scripts/annotate-translation-thought.py` | not started |
| 5 | `data/echoes/` | ai_assisted | ~66 | per-file | `scripts/annotate-echoes.py` | not started |
| 6 | `data/commentary/synthesis/` | ai_assisted | ~66 | per-file | `scripts/annotate-commentary-synthesis.py` | not started |
| 7 | `data/commentary/mkt-christ/` | ai_assisted | varies | per-file | `scripts/annotate-commentary-mkt-christ.py` | not started |
| 8 | `data/commentary/mkt-context/` | ai_assisted | varies | per-file | `scripts/annotate-commentary-mkt-context.py` | not started |
| 9 | `data/commentary/mkt-original/` | ai_assisted | varies | per-file | `scripts/annotate-commentary-mkt-original.py` | not started |
| 10 | `data/commentary/barnes/` | external | 27 | per-file | `scripts/annotate-commentary-barnes.py` | not started |
| 11 | `data/commentary/mhc/` (flat files) | external | 66 | per-file | `scripts/annotate-commentary-mhc.py` | not started |
| 12 | `data/commentary/jfb/` | external | ~66 | per-file | `scripts/annotate-commentary-jfb.py` | not started |
| 13 | `data/commentary/clarke/` | external | ~66 | per-file | `scripts/annotate-commentary-clarke.py` | not started |
| 14 | `data/commentary/calvin/` | external | ~66 | per-file | `scripts/annotate-commentary-calvin.py` | not started |
| 15 | `data/commentary/ellicott/` | external | 66 | per-file | `scripts/annotate-commentary-ellicott.py` | not started |
| 16 | `data/commentary/rwp/` | external | 27 | per-file | `scripts/annotate-commentary-rwp.py` | not started |
| 17 | `data/commentary/wesley/` | external | ~64 | per-file | `scripts/annotate-commentary-wesley.py` | not started |
| 18 | `data/strongs/` | external | 5 | per-file | `scripts/annotate-strongs.py` | not started |
| 19 | `data/devotionals/` | external | 2 | per-file | `scripts/annotate-devotionals.py` | not started |
| 20 | `data/timeline/` | project_curated | 4 | per-file | `scripts/annotate-timeline.py` | not started |
| 21 | `data/dictionary/index.json` | external | 1 index | index only | `scripts/annotate-dictionary.py` | not started |
| 22 | `data/isbe/index.json` | external | 1 index | index only | `scripts/annotate-isbe.py` | not started |
| 23 | `data/smith/index.json` | external | 1 index | index only | `scripts/annotate-smith.py` | not started |
| 24 | `data/topical/` index | external | varies | index only | `scripts/annotate-topical.py` | not started |
| 25 | `data/library/index.json` | external | 1 | single file | `scripts/annotate-library.py` | not started |
| 26 | `data/interlinear/` index | external | 1 index | index only | `scripts/annotate-interlinear.py` | not started |
| 27 | `data/wordcloud/` | derived | 1 | single file | `scripts/annotate-wordcloud.py` | not started |

---

## `_source` values by directory

Copy-paste these into your annotation scripts. Exact values must match `data/provenance.json`.

### AI-assisted content

```json
// workshop/book-study
{"type":"ai_assisted","name":"Book Study Notes","model":"claude-sonnet-4-6","generated":"2026","reviewer":"David Seis","about_url":"/about/"}

// translation/draft (all three tiers)
{"type":"ai_assisted","name":"Modern Kingdom Translation (MKT)","model":"claude-sonnet-4-6","generated":"2026","reviewer":"David Seis","about_url":"/about/"}

// echoes
{"type":"ai_assisted","name":"OT→NT Echo & Parallel Layer","model":"claude-sonnet-4-6","generated":"2026","reviewer":"David Seis","about_url":"/about/"}

// commentary/synthesis
{"type":"ai_assisted","name":"Synthesis Commentary","model":"claude-sonnet-4-6","generated":"2026","reviewer":"David Seis","about_url":"/about/"}

// commentary/mkt-christ
{"type":"ai_assisted","name":"Christological Commentary Notes","model":"claude-sonnet-4-6","generated":"2026","reviewer":"David Seis","about_url":"/about/"}

// commentary/mkt-context
{"type":"ai_assisted","name":"Historical Context Notes","model":"claude-sonnet-4-6","generated":"2026","reviewer":"David Seis","about_url":"/about/"}

// commentary/mkt-original
{"type":"ai_assisted","name":"Original Language Notes","model":"claude-sonnet-4-6","generated":"2026","reviewer":"David Seis","about_url":"/about/"}
```

### External commentary

```json
// commentary/barnes
{"type":"external","name":"Barnes' Notes on the Bible","author":"Albert Barnes","year":"1832–1885","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}

// commentary/mhc (flat files)
{"type":"external","name":"Matthew Henry Concise Commentary","author":"Matthew Henry","year":"1706","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}

// commentary/jfb
{"type":"external","name":"Jamieson, Fausset & Brown","author":"Jamieson, Fausset & Brown","year":"1871","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}

// commentary/clarke
{"type":"external","name":"Adam Clarke's Commentary","author":"Adam Clarke","year":"1810–1826","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}

// commentary/calvin
{"type":"external","name":"Calvin's Commentaries","author":"John Calvin","year":"1540–1564","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}

// commentary/ellicott
{"type":"external","name":"Ellicott's Commentary","author":"Charles J. Ellicott (ed.)","year":"1878–1884","license":"Public domain","url":"https://www.studylight.org/commentaries/eng/ebc/","fetched":"2026-06-04"}

// commentary/rwp
{"type":"external","name":"Robertson's Word Pictures","author":"A.T. Robertson","year":"1930–1933","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}

// commentary/wesley
{"type":"external","name":"Wesley's Explanatory Notes","author":"John Wesley","year":"1765","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}
```

### Lexicons, devotionals, timeline

```json
// strongs/greek
{"type":"external","name":"Strong's Greek Lexicon (Dodson)","license":"CC0","url":"https://github.com/openscriptures/strongs","fetched":"2026"}

// strongs/hebrew
{"type":"external","name":"Strong's Hebrew Lexicon (BDB)","year":"1906","license":"Public domain","url":"https://github.com/openscriptures/strongs","fetched":"2026"}

// strongs/thayer
{"type":"external","name":"Thayer's Greek Lexicon","author":"Joseph H. Thayer","year":"1889","license":"Public domain"}

// strongs/bdb
{"type":"external","name":"Brown-Driver-Briggs Hebrew Lexicon","year":"1906","license":"Public domain"}

// strongs/lxx-bridge
{"type":"external","name":"LXX Cross-Reference Bridge","license":"Public domain"}

// devotionals
{"type":"external","name":"Spurgeon's Morning and Evening","author":"C.H. Spurgeon","year":"1865","license":"Public domain","url":"https://ccel.org","fetched":"2026"}

// timeline
{"type":"project_curated","name":"Bible Timeline Events","year":"2026","reviewer":"David Seis","note":"Manually curated biblical chronology with AI-assisted event descriptions"}

// dictionary/index
{"type":"external","name":"Easton's Bible Dictionary","author":"M.G. Easton","year":"1897","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}

// isbe/index
{"type":"external","name":"Int'l Standard Bible Encyclopaedia","author":"James Orr (ed.)","year":"1915","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026-06-03"}

// smith/index
{"type":"external","name":"Smith's Bible Dictionary","author":"William Smith","year":"1884","license":"Public domain","url":"https://crosswire.org/sword/","fetched":"2026"}

// library/index
{"type":"external","name":"Library Documents (141 docs)","license":"Public domain / Holy See free use","note":"Patristic, Reformation, medieval, confessional, liturgical texts","fetched":"2026-06-04"}

// wordcloud
{"type":"derived","name":"Word Frequency Data","derived_from":"data/interlinear/","script":"scripts/generate-wordcloud.py"}
```

---

## Notes

- MHC commentary is the **flat** `data/commentary/*.json` files (not in a subdirectory).
  The annotate-commentary-mhc.py script should target those root-level book files only
  (excluding the `barnes/`, `jfb/`, etc. subdirectories).
- For `data/interlinear/`, annotate only the index or a single representative metadata
  file — not the 66 large morphological JSON files.
- The `data/topical/` directory may not have an index.json — check first. If it does,
  annotate that. If not, skip for now.
- If a file is an empty JSON object `{}` or has no meaningful content, skip it.
