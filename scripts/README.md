# Scripts — Data Build and Maintenance

All scripts run from the **repo root** unless noted. Python 3.9+ required.

---

## Dev Server

| Script | What it does | When to run |
|--------|-------------|-------------|
| `serve.py` | Starts a local HTTP server (default port 8000) for development | Any time you need to preview the site locally |
| `restart.py` | Kills the existing serve.py process and restarts it | When the server gets stuck or needs a port change |

---

## Data Fetch Scripts

These pull from upstream sources and write to `data/`. Most are one-time setup;
re-run only if the upstream source has published corrections or new content.
See `data/SOURCES.md` for source URLs, licenses, and commit pins.

| Script | Produces | When to re-run |
|--------|---------|----------------|
| `fetch-bsb.py` | `data/bible/BSB/` — Berean Standard Bible text | If BSB publishes a corrected edition |
| `fetch-versions.py` | `data/bible/YLT/`, `DBY/`, `GNV/`, `AKJV/`, `WEBBE/` — public domain versions | If new public-domain versions are added |
| `fetch-bible-data.sh` | Shell wrapper around Bible fetch operations | As needed during initial setup |
| `fetch-crossrefs.py` | `data/crossrefs/{bookId}.json` — OpenBible TSK cross-references | If OpenBible.info publishes an updated dataset |
| `fetch-commentary.py` | `data/commentary/mhc/{bookId}.json` — Matthew Henry Concise | One-time setup |
| `fetch-more-commentaries.py` | `data/commentary/barnes/`, `jfb/`, `clarke/`, `vincent/` | One-time setup |
| `fetch-strongs.py` | `data/strongs/greek.json`, `data/strongs/hebrew.json` | If openscriptures/strongs publishes corrections |
| `fetch-lexicons.py` | `data/interlinear/greek/`, `data/interlinear/hebrew/` | If morphgnt/sblgnt or openscriptures/morphhb publish corrections |
| `fetch-nave.py` | `data/topical/{topic-slug}.json` | If openscriptures/nave publishes corrections |
| `fetch-dictionary.py` | `data/dictionary/{term-slug}.json` — ISBE entries | One-time setup |
| `fetch-smith.py` | `data/smith/` — Smith's Bible Dictionary | One-time setup |
| `fetch-hitchcock.py` | `data/hitchcock/` — Hitchcock's Bible Names | One-time setup |
| `fetch-torrey.py` | `data/torrey/` — Torrey's Treasury of Scripture Knowledge | One-time setup |
| `fetch-spurgeon.py` | `data/devotionals/spurgeon-morning.json`, `spurgeon-evening.json` | One-time setup |

---

## Build Scripts

These generate derived data from already-fetched source files. Re-run after re-syncing
their input data, or when the generation logic changes.

| Script | Input | Output | When to re-run |
|--------|-------|--------|----------------|
| `build-parallels.py` | Hardcoded curated lookup table (in-script) | `data/parallels/{bookId}.json` — parallel passage data | When the curated list is edited |
| `build-verse-index.py` | `library/*.html` pages | `data/library/verse-index/{bookId}.json` — verse → confessional citation reverse lookup | After editing any library HTML page |
| `build-dict-verse-index.py` | `data/dictionary/` | Verse → dictionary term index | After re-fetching dictionary data |
| `build-library-data.py` | `library/*.html` pages | `data/library/index.json` + verse-index files | After editing any library HTML page |
| `build-library-json.py` | Library HTML | JSON summaries for search | After editing library pages |
| `build-topics-manifest.py` | `topics/*/index.html` pages | Topics search manifest | After adding or editing topic pages |
| `generate-wordcloud.py` | `data/interlinear/` | `data/wordcloud/frequencies.json` | After re-fetching interlinear data |
| `generate-reading-plans.py` | Hardcoded plan data (in-script) | `data/plans/*.json` | When plan content is edited |
| `generate-chronological-plan.py` | Hardcoded chronological order | `data/plans/chronological.json` | One-time setup; re-run if order is corrected |

---

## Enrich Scripts

These add richer content to existing book introduction JSON files, batch by batch.
Run in order (1–7) during initial setup; re-run a specific batch if its content is edited.

| Script | Covers |
|--------|--------|
| `enrich-batch-1.py` | Genesis – 2 Samuel |
| `enrich-batch-2.py` | 1 Kings – Nehemiah |
| `enrich-batch-3.py` | Esther – Song of Solomon |
| `enrich-batch-4.py` | Isaiah – Daniel |
| `enrich-batch-5.py` | Hosea – Malachi |
| `enrich-batch-6.py` | Matthew – Acts |
| `enrich-batch-7.py` | Romans – Revelation |
| `enrich-book-intros.py` | General book introduction enrichments (all books) |
| `enrich-timelines.py` | Adds timeline strip data to book introductions |
| `write-book-intros.py` | Writes initial intro JSON stubs for remaining books |

---

## Utility Scripts

| Script | What it does |
|--------|-------------|
| `new-topic.sh` | Scaffolds a new topic page: `bash scripts/new-topic.sh <slug> "Title"` |
| `check-contrast.py` | WCAG AA contrast ratio checker for all color pairs in `style.css` (light + dark mode) |

---

## Typical Initial Setup Order

```
# 1. Bible text
python3 scripts/fetch-bsb.py
python3 scripts/fetch-versions.py YLT DBY GNV AKJV WEBBE

# 2. Cross-references and commentary
python3 scripts/fetch-crossrefs.py
python3 scripts/fetch-commentary.py
python3 scripts/fetch-more-commentaries.py

# 3. Original languages
python3 scripts/fetch-lexicons.py
python3 scripts/fetch-strongs.py

# 4. Reference tools
python3 scripts/fetch-nave.py
python3 scripts/fetch-dictionary.py
python3 scripts/fetch-smith.py
python3 scripts/fetch-hitchcock.py
python3 scripts/fetch-torrey.py
python3 scripts/fetch-spurgeon.py

# 5. Build derived data
python3 scripts/build-parallels.py
python3 scripts/build-verse-index.py
python3 scripts/build-dict-verse-index.py
python3 scripts/build-library-data.py
python3 scripts/build-topics-manifest.py
python3 scripts/generate-wordcloud.py
python3 scripts/generate-reading-plans.py
python3 scripts/generate-chronological-plan.py

# 6. Enrich book introductions (in order)
python3 scripts/enrich-batch-1.py
# ... through enrich-batch-7.py
python3 scripts/enrich-timelines.py
```
