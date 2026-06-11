# BPG Agent Guide — Biblepedia Gap Analysis

## What this loop does

The BPG (Biblepedia Gap) loop identifies topics that exist in some sources but are missing
from the current Biblepedia article corpus. It runs in two phases:

**Phase 1 — Compute:** Run `bpg-compute-gaps.py` to produce `../data/biblepedia/gaps.json`.
This is a deterministic script (no synthesis, no LLM) — just cross-reference analysis.
It outputs every topic gap with a priority score and gap type.

**Phase 2 — Curate:** Review the computed gap list. Classify each gap as:
- `stub-needed` — should get a synthesized article in the BP loop (high coverage topics)
- `redirect-only` — term is an alias or minor variant; just needs a redirect to another article
- `names-only` — Hitchcock-only name with no scripture narrative; note as low priority
- `skip` — too obscure or a data artifact; not worth an article

Update `../data/biblepedia/gaps.json` with the curation decisions.

**Phase 3 — Populate BP Phase 2:** Transfer `stub-needed` items to `BP_PROGRESS.md`
Phase 2 Work Queue so the synthesis loop can cover them.

---

## Files to read in order before starting

1. `BPG_SCRIPT_GUIDE.md` — explains the compute script and gap schema
2. `BPG_PROGRESS.md` — work queue; claim your phase before starting

---

## Session workflow

### Phase 1: Compute gaps (one-time, ~5 minutes)

```bash
python3 ../scripts/bpg-compute-gaps.py
```

Verify: `../data/biblepedia/gaps.json` is created and has 1,000+ entries.
Update `BPG_PROGRESS.md`: mark Phase 1 `complete`.

### Phase 2: Curate the gap list

The gap list will have ~2,000–3,000 entries. Work through them in priority order
(sorted by `priority_score` descending). For each gap:

1. Read `term` and `gap_type`
2. Check if a Biblepedia article already exists at `../data/biblepedia/articles/{slug}.json`
3. If it exists, mark the gap `already-covered`
4. Otherwise, assign one of: `stub-needed` · `redirect-only` · `names-only` · `skip`

**Curate in batches** — claim 100–200 gaps per session (track by `id` range in the progress file).
Update the `status` field of each curated gap in-place in `gaps.json`.

### Phase 3: Populate BP Phase 2

When curation is complete (all gaps have a status), extract `stub-needed` gaps and
add them as rows in `BP_PROGRESS.md` Phase 2 Work Queue. Group by topic domain:
- Gap unit names: `gap-doctrine`, `gap-virtue`, `gap-prophetic`, `gap-person`, etc.
- Each unit: ~50 related gap articles

---

## Gap priority scoring

The compute script assigns a `priority_score` (0–100):

| Factor | Weight | Notes |
|---|---|---|
| Nave verse count | 40% | >200 verses = max score |
| Is a core doctrine (faith, grace, love...) | 30% | Detected by keyword list |
| Has ISBE entry | 20% | ISBE coverage = scholarly importance |
| Has Hitchcock entry | 10% | Named entity = probably worth noting |

Gap types (mutually exclusive, first match wins):
- `doctrine-no-article` — Nave topic clearly a theological concept; no Easton/Smith entry
- `practice-no-article` — Nave topic is a biblical practice (prayer, fasting, worship...)
- `person-name-only` — Hitchcock name with no dict article; biblical figure with refs
- `place-name-only` — Hitchcock place with no dict article
- `smith-scholarly` — Smith entry not in Easton (often obscure proper nouns)
- `isbe-scholarly` — ISBE-only entry; may be academic/technical term

---

## Redirect rules

A term is `redirect-only` if:
- It is a variant spelling of another article (e.g., "ELIAS" → "Elijah")
- It is a plural or adjectival form of an existing article (e.g., "LEVITES" → "Levi")
- The Nave entry has fewer than 10 verses AND the term clearly overlaps another

For redirect-only items, record the target slug in the `redirect_to` field of the gap entry.
The Biblepedia JS will use this to forward to the correct article.

---

## Curation speed guide

- **Obvious skips:** Single-word Nave topics that are generic English (e.g., "WORKS", "CHARACTER") — these can be skipped unless verse count > 150
- **Obvious stubs:** Core doctrines (Trinity, Justification, Sanctification, Resurrection, Eschatology) — always `stub-needed` regardless of score
- **Names:** If a Hitchcock name appears in more than 20 Bible references and has a clear narrative, mark `stub-needed`; otherwise `names-only`
