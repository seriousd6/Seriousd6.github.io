# Biblepedia Gap Analysis — Progress Tracker

Last updated: 2026-06-10 — Phase 1 complete. gaps.json generated: 8,344 gaps (1,057 Nave-only, 1,894 Smith-only, 5,404 ISBE-only). Phase 2 curation now open.

Read before starting: **BPG_AGENT_GUIDE.md** → **BPG_SCRIPT_GUIDE.md** → this file.

---

## Summary

| Phase | Description | Status |
|---|---|---|
| Phase 1 — Compute | Run bpg-compute-gaps.py → gaps.json | complete (8,344 gaps) |
| Phase 2 — Curate | Review gaps.json and assign statuses | not started |
| Phase 3 — Populate | Transfer stub-needed gaps to BP_PROGRESS.md Phase 2 | blocked (Phase 2) |

---

## Phase 1: Compute gaps

Single run, ~30 seconds. No content authoring required.

| Task | Status | Notes |
|---|---|---|
| Run bpg-compute-gaps.py | complete | `python3 scripts/bpg-compute-gaps.py` |
| Verify gaps.json has > 1,000 entries | complete | 8,344 entries |
| Verify top 10 entries are major doctrine/concept gaps | complete | Top: Angel [70], Obedience [70], Judgment [60], Afflictions [50], Jesus the Christ [50] |

Phase 2 is now open. Curation batches below.

---

## Phase 2: Curate the gap list

Work through `data/biblepedia/gaps.json` in batches of ~100 gaps per session.
Each session claims a batch, writes a `bpg-curate-{N}.py` script, runs it, and marks the batch done.

Estimated total: ~2,500 gaps to review. At 100/session ≈ 25 curation sessions.

| Batch | Gap ID Range | Count | Status | Script |
|---|---|---|---|---|
| C01 | angel-a-spirit → commandments (priority 70–60) | ~100 | not started | scripts/bpg-curate-01.py |
| C02 | afflictions-and-adversities → thankfulness (priority 50–40) | ~100 | not started | scripts/bpg-curate-02.py |
| C03 | remaining priority-40+ gaps | ~200 | not started | scripts/bpg-curate-03.py |
| C04–C25 | smith/isbe-scholarly batches | ~8,000 | not started | scripts/bpg-curate-{N}.py |

---

## Phase 3: Populate BP Phase 2

Once all curation is done:
1. Count `stub-needed` gaps
2. Group into topic domains (~50 gaps each)
3. Add rows to `BP_PROGRESS.md` Phase 2 Work Queue
4. Mark Phase 3 `complete` here

| Task | Status |
|---|---|
| Count stub-needed gaps | not started |
| Group into BP Phase 2 units | not started |
| Update BP_PROGRESS.md | not started |

---

## Expected gap counts (from pre-run analysis, 2026-06-10)

| Gap type | Estimated count | Notes |
|---|---|---|
| Nave-only topics | ~1,001 | Topics with no dict article |
| Smith-only entries | ~2,038 | In Smith but not Easton |
| ISBE-only entries | ~5,496 | Scholarly entries not in Easton/Smith |
| High-priority stubs expected | ~300–500 | After curation |

Top 15 highest-priority gaps (by Nave verse count):

| Term | Nave Verses | Gap Type | Expected Status |
|---|---|---|---|
| Jesus, the Christ | 2471 | doctrine | stub-needed |
| Afflictions and Adversities | 862 | practice | stub-needed |
| Minister, Christian | 846 | doctrine | stub-needed |
| Wicked (People) | 761 | concept | stub-needed |
| Righteous | 560 | concept | stub-needed |
| Zeal, Religious | 417 | virtue | stub-needed |
| Israel, Prophecies Concerning | 361 | prophetic | stub-needed |
| Obedience | 295 | virtue | stub-needed |
| Backsliders | 256 | concept | stub-needed |
| Thankfulness | 240 | virtue | stub-needed |
| Angel (a Spirit) | 237 | concept | probably in Easton as "Angel" — verify |
| Hypocrisy | 224 | concept | stub-needed |
| Commandments | 212 | doctrine | stub-needed |
| Pride | 202 | vice | stub-needed |
| Judgment | 154 | doctrine | stub-needed |
