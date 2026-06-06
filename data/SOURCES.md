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

### Barnes' Notes, JFB, Adam Clarke, Calvin's Commentaries
- **Source:** CrossWire SWORD Project public domain modules
- **Fetch script:** `scripts/fetch-more-commentaries.py`
- **Data path:** `data/commentary/barnes/`, `data/commentary/jfb/`, `data/commentary/clarke/`, `data/commentary/calvin/`
- **License:** Public domain (all pre-1928)
- **Last pulled:** 2026
- **Commit/version:** unknown — pin on next re-sync

### Ellicott's Commentary for English Readers
- **Source:** StudyLight.org (https://www.studylight.org/commentaries/eng/ebc/) — text is public domain
- **Fetch script:** `scripts/fetch-ellicott.py`
- **Data path:** `data/commentary/ellicott/{bookId}.json`
- **License:** Public domain (Charles J. Ellicott ed., 1878–1884; pre-1928)
- **Last pulled:** 2026-06-04
- **Coverage:** Full Bible (66 books, 22,300 verse sections) — complete OT and NT coverage
- **Note:** StudyLight.org robots.txt: `Allow: /, Content-Signal: search=yes` — scraping permitted

### Robertson's Word Pictures in the NT
- **Source:** CrossWire SWORD Project — RWP module (A.T. Robertson, 1930–1933)
- **Fetch script:** `scripts/fetch-more-commentaries.py --only rwp`
- **Data path:** `data/commentary/rwp/{bookId}.json`
- **License:** Public domain (published 1930–1933, pre-1928 for all volumes)
- **Last pulled:** 2026-06-03
- **Coverage:** NT only (27 books) — 7,201 sections

### Wesley's Explanatory Notes
- **Source:** CrossWire SWORD Project — Wesley module (John Wesley, 1765)
- **Fetch script:** `scripts/fetch-more-commentaries.py --only wesley`
- **Data path:** `data/commentary/wesley/{bookId}.json`
- **License:** Public domain (1765)
- **Last pulled:** 2026-06-03
- **Coverage:** Full Bible (64 books with content) — 15,649 sections

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

### Gesenius' Hebrew-Chaldee Lexicon to the Old Testament (Tregelles tr., 1857)
- **Source:** archive.org — public domain (pre-1923); preferred item: `geseniushebrew00geseuoft`
- **Fetch script:** `scripts/fetch-gesenius.py`
- **Data path:** `data/strongs/gesenius.json`
- **License:** Public domain (1857 Tregelles translation of Wilhelm Gesenius)
- **Last pulled:** (not yet run — run fetch-gesenius.py to populate)
- **Why:** Foundational Hebrew lexicon with Semitic cognate data (Arabic, Aramaic, Syriac,
  Phoenician parallels) that grounds Hebrew roots in the broader Semitic family. BDB (1906)
  was built on Gesenius; Gesenius has richer cognate/etymology depth for disputed terms
  (e.g., H2617 חֶסֶד — Arabic cognate meaning shame/reproach illuminates why the range is wide).
- **Workshop UI:** Shown as "Gesenius (1857)" source card in the Lexical Sources section.
  Injected into Hebrew entries via `seed-glossary.py` (source_data.gesenius).

### Abbott-Smith, Manual Greek Lexicon of the New Testament (1922)
- **Source:** https://ccel.org/ccel/abbott_smith/lexicon (CCEL — G.H. Abbott-Smith, 3rd ed. 1922)
- **Fetch script:** `scripts/fetch-abbott-smith.py`
- **Data path:** `data/strongs/abbott-smith.json`
- **License:** Public domain (published 1922, pre-1928)
- **Last pulled:** (not yet run — run fetch-abbott-smith.py to populate)
- **Why:** NT-specific lexicon with classical usage notes and LXX cross-references;
  provides an independent third witness for Greek semantic range alongside Dodson (CC0)
  and Thayer (1889). Cited as the compact scholarly standard for NT Greek.
- **Workshop UI:** Shown as "Abbott-Smith (1922)" source card in the Lexical Sources section
  of the dossier. Injected into entries via `seed-glossary.py` (source_data.abbott).

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

### ISBE — International Standard Bible Encyclopaedia
- **Source:** CrossWire SWORD Project — ISBE module (James Orr ed., 1915)
- **URL:** `https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/ISBE.zip`
- **Fetch script:** `scripts/fetch-isbe.py`
- **Data path:** `data/isbe/{slug}.json`, `data/isbe/index.json`, `data/isbe/verse-index/`
- **License:** Public domain (1915)
- **Last pulled:** 2026-06-03
- **Entries:** 9,380 articles; 24,736 verse index entries
- **Commit/version:** SWORD module version 2.2 (2009-09-07)

### Easton's Bible Dictionary
- **Source:** CrossWire SWORD Project — Easton module (M.G. Easton, 1897)
- **Fetch script:** `scripts/fetch-dictionary.py`
- **Data path:** `data/dictionary/{term-slug}.json`, `data/dictionary/index.json`
- **License:** Public domain (1897)
- **Last pulled:** 2026
- **Commit/version:** n/a (file download)

### Smith's Bible Dictionary
- **Source:** CrossWire SWORD Project / public domain text (William Smith, 1884)
- **Fetch script:** `scripts/fetch-smith.py`
- **Data path:** `data/smith/{slug}.json`, `data/smith/index.json`
- **License:** Public domain (1884)
- **Last pulled:** 2026
- **Commit/version:** n/a (file download)

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

### Creeds, Confessions, Catechisms (static HTML)
- **Source:** reformed.org, ccel.org, and public domain text
- **Fetch script:** `scripts/build-library-data.py` (parses committed HTML library pages)
- **Data path:** `data/library/`, `data/library/verse-index/`
- **License:** All documents public domain (pre-1700)
- **Last pulled:** n/a (text committed directly)

### Reformation-Era Works via EEBO-TCP + Archive.org (2026-06-03)
Four primary Reformation works added:
- **Tyndale, Obedience of a Christian Man (1528)** — TCP A14136 (EEBO-TCP CC0); original 1528 printing (Bodleian Library copy); 16 sections
- **Zwingli, Commentary on True and False Religion (1525)** — archive.org `latinworkscorres03zwin`; 1929 Heidelberg Press tr. (Henry Preble; public domain 2025); 9 sections
- **Bullinger, Decades I–II (1577 Eng. tr.)** — TCP A17183 (EEBO-TCP CC0); Parker Society translation; Decades I–II (20 sermons)
- **Cranmer, Defence of the True and Catholic Doctrine of the Sacrament (1550)** — TCP A19571 (EEBO-TCP CC0); original 1550 printing (British Library copy); 5 books
- **Fetch script:** `scripts/fetch-reform-works.py` (EEBO-TCP GitHub + archive.org stream)
- **Data path:** `data/library/html/` (`tyndale-obedience.html`, `zwingli-true-false-religion.html`, `bullinger-decades.html`, `cranmer-defence.html`)
- **License:** CC0 (EEBO-TCP) / Public domain 2025 (Zwingli 1929 tr.)
- **Last pulled:** 2026-06-03
- **Melanchthon Loci Communes** — DATA BLOCKED: all English translations (Hill 1944, Manschreck 1965) under copyright; no pre-1928 public domain English translation exists

### Papal Encyclicals and Vatican Documents (2026-06-03)
11 documents fetched from vatican.va and papalencyclicals.net:
- **Aeterni Patris (1879)** — Leo XIII — vatican.va; public domain
- **Rerum Novarum (1891)** — Leo XIII — papalencyclicals.net; public domain
- **Providentissimus Deus (1893)** — Leo XIII — papalencyclicals.net; public domain
- **Pascendi Dominici Gregis (1907)** — Pius X — papalencyclicals.net; public domain
- **Divino Afflante Spiritu (1943)** — Pius XII — vatican.va; public domain
- **Humani Generis (1950)** — Pius XII — vatican.va; public domain
- **Pacem in Terris (1963)** — John XXIII — vatican.va; freely available from Holy See
- **Dei Verbum (1965)** — Vatican II — vatican.va; freely available from Holy See
- **Deus Caritas Est (2005)** — Benedict XVI — vatican.va; freely available from Holy See
- **Spe Salvi (2007)** — Benedict XVI — vatican.va; freely available from Holy See
- **Fides et Ratio (1998)** — John Paul II — vatican.va; freely available from Holy See
- **Data path:** `data/library/html/` (rerum-novarum.html, providentissimus-deus.html, divino-afflante-spiritu.html, dei-verbum.html, fides-et-ratio.html, aeterni-patris.html, humani-generis.html, pascendi.html, pacem-in-terris.html, deus-caritas-est.html, spe-salvi.html)
- **License:** Pre-1928 documents public domain; post-1928 Vatican documents freely reproduced by the Holy See for non-commercial use
- **Last pulled:** 2026-06-03

### Additional Confessions fetched via fetch-library-docs.py (2026-06-03)
New confessions added from Wikisource and Project Gutenberg:
- **Gallican Confession (1559)** — Wikisource: *The Creeds of Christendom*, Vol. III
- **Scots Confession (1560)** — Wikisource: *Scots Confession*
- **Apology of the Augsburg Confession (1531)** — Gutenberg #6744 (Bente/Dau tr.)
- **Luther's Large Catechism (1529)** — Gutenberg #1722 (Bente/Dau tr.)
- **New Hampshire Confession of Faith (1833)** — Wikisource: *New Hampshire Baptist Confession of Faith (1833)*
- **Abstract of Principles (1858)** — Wikisource: *Abstract of Principles*
- **Methodist Articles of Religion (1784)** — Wikisource: *Articles of Religion (Methodist)*
- **Fetch script:** `scripts/fetch-library-docs.py` (Wikisource/Gutenberg modes)
- **Data path:** `data/library/html/`, `data/library/docs/`
- **License:** All public domain
- **Last pulled:** 2026-06-03

### Apologetics Documents — Patristic & 19th Century (2026-06-03)

New apologetics documents added from Wikisource (ANF) and CCEL:
- **To Autolycus** (Theophilus of Antioch, c. 180) — Wikisource: *Ante-Nicene Fathers/Volume II/Theophilus to Autolycus*, Books I–III; Roberts-Donaldson translation; first recorded use of "Trinity" (τριάς)
- **The Christian View of God and the World** (James Orr, 1893) — CCEL: `ccel.org/ccel/orr/view`, 5 grouped sections (Kerr Lectures I–IX + appendices)
- **Fetch script:** `scripts/fetch-library-docs.py` (Wikisource grouped_pages + CCEL ccel_grouped modes)
- **License:** Both public domain
- **Last pulled:** 2026-06-03

### Medieval Mystical Texts — Bonaventure (2026-06-04)

- **Bonaventure, Itinerarium Mentis in Deum / The Soul's Journey into God (c. 1259)** — CCEL: `ccel.org/ccel/bonaventure/mindsroad`; George Boas translation (1953, Johns Hopkins University Press); CCEL confirms public domain; 4 sections: Prologue, Chapters I–II (creation), Chapters III–IV (soul as image), Chapters V–VII (Being, Trinity, mystical passage)
- **Data path:** `data/library/html/bonaventure-itinerarium.html`
- **Library index:** `data/library/index.json` — id: `bonaventure-itinerarium`, abbrev: `BonI`, totalSections: 4
- **License:** Public domain (per CCEL)
- **Last pulled:** 2026-06-04

### Liturgical & Church-Order Documents (2026-06-03)

New liturgical documents added from Wikisource:
- **Book of Common Prayer (1662)** — Wikisource: *Book of Common Prayer (1892)*, 4 sections
  (Morning Prayer, Evening Prayer, Holy Communion, The Litany); the 1892 Wikisource transcription
  preserves the 1662 text from the original manuscript attached to the Act of Uniformity
- **Apostolic Constitutions (c.380)** — Wikisource: *Ante-Nicene Fathers/Volume VII/Constitutions
  of the Holy Apostles*, 36 section sub-pages grouped into 6 library sections (Books I–VIII);
  Philip Schaff et al. translation; text is from ANF Vol. VII
- **Fetch script:** `scripts/fetch-library-docs.py` (Wikisource subpages/grouped_pages modes)
- **License:** Both public domain

---

## Apocryphal Bible Versions

### Douay-Rheims 1899 (DR)
- **Source:** eBible.org — `engDRA_usfm.zip` (ID: engDRA)
- **Coverage:** 73 books (66 canonical + 7 deuterocanonical: Tobit, Judith, 1–2 Maccabees, Wisdom, Sirach, Baruch)
- **Data path:** `data/bible-apocrypha/DR/`
- **Fetch script:** `scripts/fetch-apocrypha.py DR`
- **License:** Public domain (1899 American revision of the 1610 Rheims–Douai Bible)

### World English Bible Catholic Edition (WEB-CE)
- **Source:** eBible.org — `eng-web-c_usfm.zip` (ID: eng-web-c)
- **Coverage:** 74 books (66 canonical + 8 deuterocanonical: Tobit, Judith, 1–2 Maccabees, Wisdom, Sirach, Baruch, Additions to Esther; Greek Esther ESG and Greek Daniel DAG variants)
- **Data path:** `data/bible-apocrypha/WEB-CE/`
- **Fetch script:** `scripts/fetch-apocrypha.py WEB-CE`
- **License:** Public domain (CC0)

### KJV with Apocrypha 1611 (KJV-APO)
- **Source:** eBible.org — `eng-kjv_usfm.zip` (ID: eng-kjv)
- **Coverage:** 80 books (66 canonical + 14 Protestant Apocrypha: Tobit, Judith, 1–2 Maccabees, Wisdom, Sirach, Baruch, Additions to Esther, Prayer of Azariah, Susanna, Bel & Dragon, 1–2 Esdras, Prayer of Manasseh)
- **Data path:** `data/bible-apocrypha/KJV-APO/`
- **Fetch script:** `scripts/fetch-apocrypha.py KJV-APO`
- **License:** Public domain (1769 standardized text)

### Brenton's LXX English 1851 (BRENTON)
- **Source:** eBible.org — `eng-Brenton_usfm.zip` (ID: eng-Brenton); Psalm 151 extracted from Psalms USFM chapter 151
- **Coverage:** 51 books (OT-only translation — no NT; includes 15 deuterocanonical books including 3–4 Maccabees and Psalm 151)
- **Data path:** `data/bible-apocrypha/BRENTON/`
- **Fetch script:** `scripts/fetch-apocrypha.py BRENTON`
- **License:** Public domain (1851 translation by Sir Lancelot C.L. Brenton)

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
