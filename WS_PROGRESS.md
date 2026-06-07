# Wide Source Commentary Progress

**Last updated:** 2026-06-07 (infrastructure created; no synthesis data yet)
**Source of truth:** `data/commentary/synthesis/`
**Purpose:** Per-verse synthesis of Calvin, Matthew Henry Concise (mhcc), Ellicott, JFB, Clarke, Wesley, and Barnes (NT). Each verse gets a 100–250 word prose synthesis plus a `voices` array of 40–80 word excerpts. See `WS_AGENT_GUIDE.md` for content principles.

---

## Summary

| | Synthesis |
|-|-----------|
| NT complete (books) | 0 / 27 |
| OT complete (books) | 0 / 39 |
| NT in-progress | 0 |
| OT in-progress | 0 |

---

## Priority Order

Phase 1 (NT epistles — densest synthesis value): Hebrews, Romans, Galatians, Ephesians, 1 John  
Phase 2 (NT narratives): John, Luke, Acts  
Phase 3 (remaining NT)  
Phase 4 (OT — Genesis, Psalms, Isaiah first)  
Phase 5 (remaining OT)

---

## New Testament

| Book | bookId | Chs | Synthesis | Status |
|------|--------|-----|-----------|--------|
| Matthew | matthew | 28 | | not started |
| Mark | mark | 16 | | not started |
| Luke | luke | 24 | | not started |
| John | john | 21 | | not started |
| Acts | acts | 28 | | not started |
| Romans | romans | 16 | | not started |
| 1 Corinthians | 1corinthians | 16 | | not started |
| 2 Corinthians | 2corinthians | 13 | | not started |
| Galatians | galatians | 6 | | not started |
| Ephesians | ephesians | 6 | | not started |
| Philippians | philippians | 4 | | not started |
| Colossians | colossians | 4 | | not started |
| 1 Thessalonians | 1thessalonians | 5 | | not started |
| 2 Thessalonians | 2thessalonians | 3 | | not started |
| 1 Timothy | 1timothy | 6 | | not started |
| 2 Timothy | 2timothy | 4 | | not started |
| Titus | titus | 3 | | not started |
| Philemon | philemon | 1 | | not started |
| Hebrews | hebrews | 13 | | not started |
| James | james | 5 | | not started |
| 1 Peter | 1peter | 5 | | not started |
| 2 Peter | 2peter | 3 | | not started |
| 1 John | 1john | 5 | | not started |
| 2 John | 2john | 1 | | not started |
| 3 John | 3john | 1 | | not started |
| Jude | jude | 1 | | not started |
| Revelation | revelation | 22 | | not started |

---

## Old Testament

| Book | bookId | Chs | Synthesis | Status |
|------|--------|-----|-----------|--------|
| Genesis | genesis | 50 | | not started |
| Exodus | exodus | 40 | | not started |
| Leviticus | leviticus | 27 | | not started |
| Numbers | numbers | 36 | | not started |
| Deuteronomy | deuteronomy | 34 | | not started |
| Joshua | joshua | 24 | | not started |
| Judges | judges | 21 | | not started |
| Ruth | ruth | 4 | | not started |
| 1 Samuel | 1samuel | 31 | | not started |
| 2 Samuel | 2samuel | 24 | | not started |
| 1 Kings | 1kings | 22 | | not started |
| 2 Kings | 2kings | 25 | | not started |
| 1 Chronicles | 1chronicles | 29 | | not started |
| 2 Chronicles | 2chronicles | 36 | | not started |
| Ezra | ezra | 10 | | not started |
| Nehemiah | nehemiah | 13 | | not started |
| Esther | esther | 10 | | not started |
| Job | job | 42 | | not started |
| Psalms | psalms | 150 | | not started |
| Proverbs | proverbs | 31 | | not started |
| Ecclesiastes | ecclesiastes | 12 | | not started |
| Song of Solomon | songofsolomon | 8 | | not started |
| Isaiah | isaiah | 66 | | not started |
| Jeremiah | jeremiah | 52 | | not started |
| Lamentations | lamentations | 5 | | not started |
| Ezekiel | ezekiel | 48 | | not started |
| Daniel | daniel | 12 | | not started |
| Hosea | hosea | 14 | | not started |
| Joel | joel | 3 | | not started |
| Amos | amos | 9 | | not started |
| Obadiah | obadiah | 1 | | not started |
| Jonah | jonah | 4 | | not started |
| Micah | micah | 7 | | not started |
| Nahum | nahum | 3 | | not started |
| Habakkuk | habakkuk | 3 | | not started |
| Zephaniah | zephaniah | 3 | | not started |
| Haggai | haggai | 2 | | not started |
| Zechariah | zechariah | 14 | | not started |
| Malachi | malachi | 4 | | not started |

---

## NT Work Queue

Work units are ≤99 verses (greedy chapter packing). Claim one row at a time — set Status to `in-progress @ <ISO timestamp>` before writing; set to `complete` after running and verifying.

| Script | Book | Chapters | Verses (est.) | Status |
|--------|------|----------|---------------|--------|
| ws-synthesis-hebrews-1-4.py | hebrews | 1–4 | ~90 | in-progress @ 2026-06-07T12:16:20Z |
| ws-synthesis-hebrews-5-9.py | hebrews | 5–9 | ~99 | not started |
| ws-synthesis-hebrews-10-13.py | hebrews | 10–13 | ~90 | not started |
| ws-synthesis-romans-1-4.py | romans | 1–4 | ~97 | not started |
| ws-synthesis-romans-5-8.py | romans | 5–8 | ~97 | not started |
| ws-synthesis-romans-9-11.py | romans | 9–11 | ~91 | not started |
| ws-synthesis-romans-12-16.py | romans | 12–16 | ~89 | not started |
| ws-synthesis-galatians-1-6.py | galatians | 1–6 | ~149 | not started |
| ws-synthesis-ephesians-1-6.py | ephesians | 1–6 | ~155 | not started |
| ws-synthesis-1john-1-5.py | 1john | 1–5 | ~105 | not started |
| ws-synthesis-john-1-4.py | john | 1–4 | ~87 | not started |
| ws-synthesis-john-5-8.py | john | 5–8 | ~99 | not started |
| ws-synthesis-john-9-12.py | john | 9–12 | ~97 | not started |
| ws-synthesis-john-13-17.py | john | 13–17 | ~95 | not started |
| ws-synthesis-john-18-21.py | john | 18–21 | ~94 | not started |

*(Add OT work queue entries when Phase 4 begins.)*
