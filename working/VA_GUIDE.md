# Verse Auditor Guide

Reference for rule set, abbreviation table, file types, and edge cases.
Read this before auditing any file. Used by `VA_AGENT_PROMPT.md` in Step 2.

---

## Rule Catalogue

| ID | Pattern | Example Input | Result | Context needed |
|---|---|---|---|---|
| R1 | Full canonical book name + Ch:V | `Romans 16:25` | `<a class="ref" data-ref="Romans 16:25">Romans 16:25</a>` | None |
| R2 | Abbreviated book name + Ch:V | `1Cor 10:31`, `Jn 3:16`, `Ps 23:1` | Same as R1 after normalization | None |
| R3 | Verse continuation in same clause | `John 3:16, 17, 18` | Each continuation tagged with inherited book+ch | Prior ref in clause |
| R4 | Semicolon list | `(John 3:16; Rom 5:8)` | Each ref caught by R1/R2 individually | None |
| R5 | Bare Ch:V only | `3:16` | `<a class="ref" data-ref="John 3:16">3:16</a>` | `--book` required |
| R6 | Verse mention: `v. 5`, `vv. 5-7` | In commentary with known ch | Tagged with book + current chapter | `--book` + chapter key |
| R7 | Chapter mention: `chap. 3`, `ch. 3` | In commentary | `<a class="ref" data-ref="John 3:1">John 3</a>` | `--book` required |

**Double-wrap guard:** `va_process.py` never touches text already inside an existing `<a ... data-ref>` anchor. Idempotent — safe to re-run.

**Greek/Hebrew script guard:** Regex requires Latin-alphabet book name before Ch:V. Lemma text like `δοῦλος 5:12` is never matched.

**Tag attribute guard:** The script splits HTML by tags and processes only text nodes, not tag attributes. `href="John 3:16"` is never double-processed.

---

## Context Resolution by File Type

| File Type | Book Context Source | Chapter Context Source |
|---|---|---|
| `json_commentary` `{ch:{v:html}}` | filename stem (`romans` → `Romans`) | outer JSON key string (`"3"`) |
| `json_echoes` `{ch:{v:[objects]}}` | filename stem | from `target` field ch (not passed to note) |
| `html` with `<body data-bible-book="John">` | attribute value | none |
| `html` without `data-bible-book` | none — R5/R6/R7 disabled | none |
| `json_book_study` | none — R5/R6/R7 disabled | none |
| `json_library_doc` | none — R5/R6/R7 disabled | none |

---

## Section Priorities

Process T first (most bare refs), then M, E, L, D, K, P, O.

| Code | Section | File type | Notes |
|---|---|---|---|
| T | Traditional Commentaries | json_commentary | ellicott, jfb, barnes, clarke, wesley, rwp, calvin, synthesis |
| M | MKT Commentaries | json_commentary | mkt-original, mkt-context, mkt-christ |
| E | Echoes | json_echoes | Normalize `target` field; tag `note` field |
| L | Library HTML | html | Pre-tagged in many files; run to catch any gaps |
| D | Library Docs JSON | json_library_doc | {sections:[{html:...}]} — mostly pre-tagged |
| K | Book Study JSON | json_book_study | Prose string fields only |
| P | Topic Pages | html | Check `<body data-bible-book>` for R5 context |
| O | Other HTML | html | index.html, compare, bookmarks, etc. |

---

## Full Book Abbreviation Table

Used by `va_process.py`'s `normalize_book()`. All keys are lowercase; lookup is case-insensitive.

### Old Testament

| Abbreviation(s) | Canonical |
|---|---|
| gen | Genesis |
| exod, exo | Exodus |
| lev | Leviticus |
| num | Numbers |
| deut, dt | Deuteronomy |
| josh, jos | Joshua |
| judg, jdg | Judges |
| ruth | Ruth |
| 1sam, 1sa | 1 Samuel |
| 2sam, 2sa | 2 Samuel |
| 1kgs, 1ki, 1kings | 1 Kings |
| 2kgs, 2ki, 2kings | 2 Kings |
| 1chr, 1chron, 1ch | 1 Chronicles |
| 2chr, 2chron, 2ch | 2 Chronicles |
| ezra | Ezra |
| neh | Nehemiah |
| esth, est | Esther |
| job | Job |
| ps, pss, psa, psalm | Psalms |
| prov, pro, prv | Proverbs |
| eccl, eccles, ecc | Ecclesiastes |
| song, sos, cant | Song of Solomon |
| isa | Isaiah |
| jer | Jeremiah |
| lam | Lamentations |
| ezek, eze | Ezekiel |
| dan | Daniel |
| hos | Hosea |
| joel | Joel |
| amos | Amos |
| obad, ob | Obadiah |
| jon | Jonah |
| mic | Micah |
| nah | Nahum |
| hab | Habakkuk |
| zeph | Zephaniah |
| hag | Haggai |
| zech, zec | Zechariah |
| mal | Malachi |

### New Testament

| Abbreviation(s) | Canonical |
|---|---|
| matt, mt | Matthew |
| mk, mar | Mark |
| lk | Luke |
| jn, jno | John |
| acts | Acts |
| rom | Romans |
| 1cor, 1co | 1 Corinthians |
| 2cor, 2co | 2 Corinthians |
| gal | Galatians |
| eph | Ephesians |
| phil, php | Philippians |
| col | Colossians |
| 1thess, 1thes, 1th | 1 Thessalonians |
| 2thess, 2thes, 2th | 2 Thessalonians |
| 1tim, 1ti | 1 Timothy |
| 2tim, 2ti | 2 Timothy |
| tit | Titus |
| phlm, phm, philem | Philemon |
| heb | Hebrews |
| jas, jm | James |
| 1pet, 1pe | 1 Peter |
| 2pet, 2pe | 2 Peter |
| 1jn, 1john | 1 John |
| 2jn, 2john | 2 John |
| 3jn, 3john | 3 John |
| jude | Jude |
| rev, apoc | Revelation |

---

## Canonical Form Rules

All `data-ref` attribute values must use these canonical forms:

- Book name: full canonical (`Romans`, `1 Corinthians`, `Song of Solomon`) — never abbreviated
- Space between number-prefix and book name: `1 Corinthians`, not `1Corinthians`
- Chapter:Verse separator: `:` (colon)
- Verse range: `-` (hyphen), no spaces: `Romans 16:25-27`
- Chapter-only: `Romans 16` (no verse — only for R7 chapter mentions)

Display text = `data-ref` value verbatim.

---

## Edge Cases

**"v." before a verse number:** In commentary prose, `v. 5` or `vv. 5-7` are common references to the current chapter. Only apply R6 for json_commentary files where both book (stem) and chapter (JSON key) are known. Never apply to HTML files without explicit `--book` + `--chapter` args.

**Parenthetical ref lists:** `(John 3:16; Rom 5:8; Heb 11:1)` — R1/R2 catches each ref individually. The semicolons are not part of the ref and stay as text between the links.

**Qualified refs:** `See Romans 8:28`, `Compare Acts 13:2` — the qualifier word (`See`, `Compare`, `Comp.`) is plain text before the ref. The regex uses word boundary, so the qualifier is not included in the match. Correct output: `See <a class="ref" data-ref="Romans 8:28">Romans 8:28</a>`.

**Chapter ranges:** `Romans 8-11` (chapters, no verse) — NOT tagged. The regex requires `Ch:V` format. Chapter-range references are intentionally left as plain text; they don't map to a single verse for the tooltip system.

**Roman numeral book prefixes:** `I Cor`, `II Cor` — NOT in the abbreviation table. Commentaries rarely use Roman numerals. If encountered, mark the row with a Notes entry and `skipped`.

**Psalm vs. Psalms:** Both `Psalm 23:1` and `Psalms 23:1` are valid; the canonical name is `Psalms`. If the source uses `Psalm`, the script normalizes it to `Psalms`. Display text will show `Psalms 23:1`.

**Greek/Hebrew script followed by Strong's numbers:** `G3056` or `H1697` — never wrapped. The regex requires a Latin book name before digits.

**HTML entities in references:** Rare in commentary JSON, but `&amp;` etc. in text nodes won't affect book-name matching since the regex looks for Latin letters.

---

## Verification Checklist (per file)

Run with `--dry-run --show-sample 5` first and confirm:

- [ ] `data-ref` values use canonical book names (full, with spaces: `1 Corinthians`, not `1Cor`)
- [ ] No double-wrapping: no `<a data-ref` inside another `<a data-ref`
- [ ] No Greek/Hebrew lemma text wrapped
- [ ] Parenthetical ref lists: each ref gets its own link
- [ ] `Refs fixed` count is plausible (0 is fine if file was already clean)
- [ ] Sample `BEFORE` shows bare text; `AFTER` shows the tagged version

**Browser verification (Section T/M):**
Open Commentary tab in workshop for a verse from the processed book.
Select the relevant commentary source. Hover a reference → tooltip should appear.
Click → verse modal should open.

**Regression check (Section P):**
Open the processed topic page in browser. Existing `<a class="ref">` links still work (not double-wrapped, tooltips fire normally).

---

## Quick Commands

```bash
# Dry run on one commentary file
python3 scripts/va_process.py data/commentary/ellicott/romans.json --dry-run --show-sample 5

# Process and write
python3 scripts/va_process.py data/commentary/ellicott/romans.json

# Echoes (book from stem)
python3 scripts/va_process.py data/echoes/mark.json --dry-run --show-sample 3

# Topic page with known book
python3 scripts/va_process.py topics/john/index.html --book John --dry-run --show-sample 3

# Discovery (run once per day)
python3 scripts/va_discover.py

# Idempotency check: should show refs_fixed=0 on a processed file
python3 scripts/va_process.py data/commentary/ellicott/romans.json --dry-run
```

---

## Timestamp Utilities

```python
from datetime import datetime, timezone, timedelta

def now_iso():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def is_stale(ts_str, hours=1):
    """True if the 'in-progress @ TIMESTAMP' row is older than threshold."""
    ts = datetime.fromisoformat(ts_str.split('@ ')[1].strip().replace('Z', '+00:00'))
    age = datetime.now(timezone.utc) - ts
    return age > timedelta(hours=hours)

def discovery_overdue(ts_str):
    """True if Next discovery due timestamp is in the past."""
    if '(not yet run)' in ts_str:
        return True
    ts = datetime.fromisoformat(ts_str.strip().replace('Z', '+00:00'))
    return datetime.now(timezone.utc) >= ts
```
