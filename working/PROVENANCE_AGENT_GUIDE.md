# Provenance Agent Reference Guide

Read this file in full before writing any provenance script.

---

## 1. What the Provenance Annotation Pass Does

Every JSON data file in this repo ultimately gets a top-level `"_source"` key that
records where the data came from and how it was produced. This serves two purposes:

1. **Inline attribution** — the raw data itself carries its provenance, independently
   of the UI badge system.
2. **Auditability** — anyone inspecting the JSON files directly can see whether content
   is public-domain historic text, CC-licensed external data, or AI-generated.

The UI badge system (`assets/js/provenance.js` + `data/provenance.json`) already handles
display for most directories. This annotation pass adds `"_source"` to individual files
as well, starting with AI-generated content (highest transparency priority).

---

## 2. The `_source` Schema

### For external (public-domain or openly-licensed) data:

```json
"_source": {
  "type": "external",
  "name": "Barnes' Notes on the Bible",
  "author": "Albert Barnes",
  "year": "1832–1885",
  "license": "Public domain",
  "url": "https://crosswire.org/sword/",
  "fetched": "2026"
}
```

### For AI-assisted content:

```json
"_source": {
  "type": "ai_assisted",
  "name": "Book Study Notes",
  "model": "claude-sonnet-4-6",
  "generated": "2026",
  "reviewer": "David Seis",
  "about_url": "/about/"
}
```

### For derived/computed data:

```json
"_source": {
  "type": "derived",
  "name": "Word Frequency Data",
  "derived_from": "data/interlinear/",
  "script": "scripts/generate-wordcloud.py"
}
```

### For project-curated data:

```json
"_source": {
  "type": "project_curated",
  "name": "Bible Timeline Events",
  "year": "2026",
  "reviewer": "David Seis",
  "note": "Manually curated biblical chronology with AI-assisted event descriptions"
}
```

---

## 3. Where to Add `_source`

### Rule for large directories (hundreds of individual files):
**Do NOT modify every individual file.** Instead, add `_source` to the directory's
`index.json` (if one exists). The provenance manifest (`data/provenance.json`) already
documents the entire directory. The goal of this annotation pass is to make the
provenance visible from within the data, not to bloat every individual record.

Directories where only `index.json` gets annotated:
- `data/dictionary/` → annotate `data/dictionary/index.json`
- `data/isbe/` → annotate `data/isbe/index.json`
- `data/smith/` → annotate `data/smith/index.json`
- `data/hitchcock/` → annotate the root index if one exists
- `data/topical/` → annotate index if one exists

### Rule for smaller directories (≤ 100 files):
Annotate each individual JSON file. Use a Python script to batch-process the directory.

Directories that get per-file annotation:
- `data/workshop/book-study/` — 66 files, AI-generated, HIGH priority
- `data/translation/draft/literal/` — ~54 files, AI-generated, HIGH priority
- `data/translation/draft/mediating/` — ~54 files, AI-generated
- `data/translation/draft/thought/` — ~54 files, AI-generated
- `data/echoes/` — ~66 files, AI-assisted
- `data/commentary/synthesis/` — ~66 files, AI-assisted
- `data/commentary/mkt-christ/` — AI-assisted
- `data/commentary/mkt-context/` — AI-assisted
- `data/commentary/mkt-original/` — AI-assisted
- `data/commentary/barnes/` — per-book (27 NT books), external
- `data/commentary/ellicott/` — per-book, external
- `data/commentary/rwp/` — per-book (NT only), external
- `data/commentary/wesley/` — per-book, external
- `data/commentary/jfb/` — per-book, external
- `data/commentary/clarke/` — per-book, external
- `data/commentary/calvin/` — per-book, external
- `data/strongs/` — 5 files, external
- `data/devotionals/` — 2 files, external
- `data/timeline/` — 4 files, project-curated + AI-assisted

### Rule for MHC (flat commentary files):
The flat `data/commentary/*.json` files (genesis.json, exodus.json, etc.) are MHC.
Add `_source` to each.

---

## 4. How to Write the Annotation Script

Use this pattern for a batch-annotation script:

```python
#!/usr/bin/env python3
"""
Annotate data/workshop/book-study/ with _source fields.
Run from repo root: python3 scripts/annotate-book-study.py
"""
import json, os, pathlib

SOURCE = {
    "type": "ai_assisted",
    "name": "Book Study Notes",
    "model": "claude-sonnet-4-6",
    "generated": "2026",
    "reviewer": "David Seis",
    "about_url": "/about/"
}

DIR = pathlib.Path("data/workshop/book-study")

for p in sorted(DIR.glob("*.json")):
    data = json.loads(p.read_text())
    if "_source" in data:
        print(f"  skip {p.name} (already annotated)")
        continue
    data["_source"] = SOURCE
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"  annotated {p.name}")

print("done.")
```

Key rules:
- **Never overwrite** existing `_source` if already present (check `if "_source" in data`)
- Run from repo root
- Print each file as it's processed so progress is visible
- One script per work unit (don't combine multiple directories in one script)

---

## 5. How to verify

After running the script, spot-check three files:

```python
import json, pathlib

p = pathlib.Path("data/workshop/book-study/genesis.json")
data = json.loads(p.read_text())
print(json.dumps(data.get("_source"), indent=2))
```

Expected output should match the `_source` schema exactly. Confirm:
- `_source.type` is correct (`ai_assisted`, `external`, etc.)
- `_source.name` matches the name in `data/provenance.json` for this directory
- The existing data fields (`key_vocabulary`, `language_notes`, etc.) are untouched
- JSON is valid (script didn't corrupt any file)

---

## 6. Quality checklist before marking a row complete

- [ ] Script runs without errors from repo root
- [ ] All files in the directory (or index.json for large dirs) have `_source`
- [ ] No existing data was overwritten or corrupted
- [ ] Three spot-check files show correct `_source` content
- [ ] `PROVENANCE_PROGRESS.md` row updated to `complete`
