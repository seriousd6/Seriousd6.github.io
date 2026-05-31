# Data Sources

Record every external data source here. Update this file whenever a source is added,
changed, or removed. Include the commit hash or version tag so re-syncs are not done blind.

---

## Bible Text

### KJV, BSB, WEB, ASV (committed)
- **Source:** Committed directly; KJV/WEB/ASV from public domain; BSB from Berean Standard Bible
- **Data path:** `data/bible/KJV/`, `data/bible/BSB/`, `data/bible/WEB/`, `data/bible/ASV/`
- **License:** KJV/WEB/ASV: public domain; BSB: free for personal/non-commercial use
- **Last pulled:** 2026 (initial setup)
- **Commit/version:** unknown — pin on next re-sync

### YLT, DBY, GNV, AKJV, WEBBE (public domain versions)
- **Source:** https://github.com/wldeh/bible-api
- **Fetch script:** `scripts/fetch-versions.py`
- **Data path:** `data/bible/YLT/`, `data/bible/DBY/`, `data/bible/GNV/`, `data/bible/AKJV/`, `data/bible/WEBBE/`
- **License:** All public domain (pre-1930)
- **Last pulled:** 2026
- **Commit/version:** unknown — pin on next re-sync

---

## Cross-References

### OpenBible TSK Cross-References
- **Source:** https://openbible.info/data/cross-references.txt
- **Fetch script:** `scripts/fetch-crossrefs.py`
- **Data path:** `data/crossrefs/{bookId}.json`
- **License:** CC BY 4.0
- **Last pulled:** 2026
- **Commit/version:** n/a (file download, not a git repo)

---

## Commentaries

### Matthew Henry Concise Commentary (MHC)
- **Source:** CrossWire SWORD Project MHCom module
- **Fetch script:** `scripts/fetch-commentary.py`
- **Data path:** `data/commentary/mhc/{bookId}.json`
- **License:** Public domain
- **Last pulled:** 2026
- **Commit/version:** unknown — pin on next re-sync

### Barnes' Notes, JFB, Adam Clarke, Vincent's Word Studies
- **Source:** SWORD Project / e-Sword public domain modules
- **Fetch script:** `scripts/fetch-more-commentaries.py`
- **Data path:** `data/commentary/barnes/`, `data/commentary/jfb/`, `data/commentary/clarke/`, `data/commentary/vincent/`
- **License:** Public domain (all pre-1928)
- **Last pulled:** 2026
- **Commit/version:** unknown — pin on next re-sync

---

## Interlinear (Greek NT + Hebrew OT)

### Greek NT — SBLGNT with Morphological Tagging
- **Source:** https://github.com/morphgnt/sblgnt
- **Fetch script:** `scripts/fetch-lexicons.py`
- **Data path:** `data/interlinear/greek/{bookId}.json`
- **License:** CC BY 4.0
- **Last pulled:** 2026
- **Commit/version:** unknown — record hash on next pull

### Hebrew OT — OpenScriptures Morphological Hebrew Bible
- **Source:** https://github.com/openscriptures/morphhb
- **Fetch script:** `scripts/fetch-lexicons.py`
- **Data path:** `data/interlinear/hebrew/{bookId}.json`
- **License:** CC BY 4.0
- **Last pulled:** 2026
- **Commit/version:** unknown — record hash on next pull

---

## Strong's Concordance & Lexicons

### Strong's Numbers (Greek + Hebrew)
- **Source:** https://github.com/openscriptures/strongs
- **Fetch script:** `scripts/fetch-strongs.py`
- **Data path:** `data/strongs/greek.json`, `data/strongs/hebrew.json`
- **License:** Public domain (Dodson Greek Lexicon: CC0; BDB Hebrew: public domain)
- **Last pulled:** 2026
- **Commit/version:** unknown — record hash on next pull

---

## Nave's Topical Bible

- **Source:** https://github.com/openscriptures/nave
- **Fetch script:** `scripts/fetch-nave.py`
- **Data path:** `data/topical/{topic-slug}.json`
- **License:** Public domain (Orville Nave, 1896)
- **Last pulled:** 2026
- **Commit/version:** unknown — record hash on next pull

---

## Dictionary

### ISBE, Easton's, Smith's Bible Dictionaries
- **Source:** CCEL.org / public domain text files
- **Fetch scripts:** `scripts/fetch-dictionary.py`, `scripts/fetch-smith.py`
- **Data path:** `data/dictionary/{term-slug}.json`, `data/smith/`
- **License:** Public domain (ISBE 1915, Easton's 1897, Smith's 1863)
- **Last pulled:** 2026
- **Commit/version:** n/a (file downloads)

### Hitchcock's Bible Names
- **Source:** Public domain text
- **Fetch script:** `scripts/fetch-hitchcock.py`
- **Data path:** `data/hitchcock/`
- **License:** Public domain
- **Last pulled:** 2026
- **Commit/version:** n/a

---

## Devotionals

### Spurgeon's Morning and Evening
- **Source:** https://ccel.org — C.H. Spurgeon, 1865
- **Fetch script:** `scripts/fetch-spurgeon.py`
- **Data path:** `data/devotionals/spurgeon-morning.json`, `data/devotionals/spurgeon-evening.json`
- **License:** Public domain
- **Last pulled:** 2026
- **Commit/version:** n/a (file download)

---

## Confessional Library

### Creeds, Confessions, Catechisms
- **Source:** reformed.org, ccel.org, and public domain text
- **Fetch script:** `scripts/build-library-data.py` (parses committed HTML library pages)
- **Data path:** `data/library/`, `data/library/verse-index/`
- **License:** All documents public domain (pre-1700)
- **Last pulled:** n/a (text committed directly)

---

## Timeline & Maps

### Bible Timeline Events
- **Source:** Public domain / manually curated
- **Data path:** `data/timeline/events.json`
- **License:** n/a (project-created)

### Biblical Geography
- **Source:** OpenBible.info geography data
- **Data path:** embedded in `assets/js/maps.js`
- **License:** Public domain

---

## Word Cloud

### Frequency Data
- **Source:** Generated from interlinear data in this repo
- **Build script:** `scripts/generate-wordcloud.py`
- **Data path:** `data/wordcloud/frequencies.json`
- **License:** n/a (derived work)
- **Regenerate:** `python3 scripts/generate-wordcloud.py` from repo root

---

## Re-sync Procedure

When an upstream repo publishes corrections or new data:

1. Note the new commit hash you intend to pull
2. Clone or fetch the upstream repo at that commit
3. Run the corresponding fetch/build script from the repo root
4. Verify output with `python3 scripts/validate-data.py` (M3)
5. Commit the updated data files
6. Update the **Commit/version** field in this file
