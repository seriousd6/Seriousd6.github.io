# Parallels Data Expansion Tracker

Phase 2 and 3 work queue for agents filling `data/parallels/` synoptic parallel entries.
Only `type: "parallel"` entries appear in the synoptic panel; other types belong in echoes.

See `PARALLELS_AGENT_LOOP.md` for the agent prompt and schema.

---

## Phase 1 — Gospel parallels (COMPLETE)

The four Gospels are already well-filled by prior work sessions.

| Book | Status | Parallel entries |
|------|--------|-----------------|
| matthew.json | ✅ done | 67 |
| mark.json | ✅ done | 58 |
| luke.json | ✅ done | 62 |
| john.json | ✅ done | 12 |

---

## Phase 2 — Kings / Chronicles / Samuel parallels

The Kings-Chronicles parallel is the largest OT synoptic pair (~90% of Kings events appear in Chronicles and vice versa). Samuel also has significant overlap with Chronicles.

Target: ~50 pericopes per book pair.

| Book | Status | Parallel entries | Notes |
|------|--------|-----------------|-------|
| 1kings.json | [ ] | 3 (seed) | Needs full coverage chs 1-22 |
| 2kings.json | [ ] | 5 (seed) | Needs full coverage chs 1-25 |
| 1chronicles.json | [ ] | 7 (seed) | Needs full coverage chs 1-29 |
| 2chronicles.json | [ ] | 7 (seed) | Needs full coverage chs 1-36 |
| 1samuel.json | [ ] | 0 | Add Samuel ↔ Chronicles parallels |
| 2samuel.json | [ ] | 8 (seed) | Needs completion; esp. chs 5-10 ↔ 1 Chr |

**Key parallel families for this phase:**
- 1 Kings 1-2 ↔ 1 Chronicles 28-29 (David's last days / Solomon's coronation)
- 1 Kings 3-11 ↔ 2 Chronicles 1-9 (Solomon's reign)
- 1 Kings 12-16 ↔ 2 Chronicles 10-16 (Divided kingdom early period)
- 1 Kings 17-2 Kings 17 ↔ 2 Chronicles 17-28 (Prophetic era)
- 2 Kings 18-20 ↔ 2 Chronicles 29-32 ↔ Isaiah 36-39 (Hezekiah)
- 2 Kings 21-23 ↔ 2 Chronicles 33-35 (Manasseh, Josiah)
- 2 Kings 24-25 ↔ 2 Chronicles 36 ↔ Jeremiah 52 (Fall of Jerusalem)
- 2 Samuel 5-10 ↔ 1 Chronicles 11-19 (David's consolidation)
- 2 Samuel 24 ↔ 1 Chronicles 21 (David's census)

---

## Phase 3 — Prophetic and minor prophet parallels

| Book | Status | Parallel entries | Notes |
|------|--------|-----------------|-------|
| isaiah.json | [ ] | 4 (seed) | Already has Hezekiah; expand Isa 36-39 ↔ 2 Kgs 18-20 |
| jeremiah.json | [ ] | 1 (seed) | Jer 52 ↔ 2 Kgs 24-25 complete; check Jer 39 ↔ 2 Kgs 25 |
| micah.json | [ ] | 1 (seed) | Micah 4:1-5 ↔ Isaiah 2:1-5 (Swords into plowshares) |
| amos.json | [ ] | 0 | Check for Obadiah / Joel overlaps |
| joel.json | [ ] | 0 | Joel 3 ↔ Amos 9 (Day of the Lord restoration) |
| hosea.json | [ ] | 0 | Minor parallels only |
| psalms.json | [ ] | 7 (seed) | Expand: Ps 18 ↔ 2 Sam 22; Ps 14 ↔ Ps 53; Ps 108 ↔ Ps 57+60 |
| ezra.json | [ ] | 1 (seed) | Ezra 1 ↔ 2 Chr 36:22-23 (Cyrus decree) |

---

## Phase 4 — Acts / Epistles (future)

Acts has some Gospel parallels (e.g. Pentecost connects to Joel 2).
Epistles occasionally quote the same passages (Romans/Galatians). Low priority.

---

## How to run an agent

1. Copy `PARALLELS_AGENT_LOOP.md` prompt
2. Set TARGET BOOK, BOOK DISPLAY NAME, and CHAPTERS TO FILL at the top
3. Spawn a `claude` agent with that prompt
4. Agent reads existing file, identifies gaps, fills pericopes, verifies, marks tracker

Each agent session should target ONE book at a time to stay focused.
