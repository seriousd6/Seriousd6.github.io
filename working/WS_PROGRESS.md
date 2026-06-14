# Wide Source Commentary Progress

**Last updated:** 2026-06-14
**Source of truth:** `data/commentary/synthesis/`
**Purpose:** Per-verse synthesis from 11 sources: Calvin, Matthew Henry Concise (mhcc — top-level path), Ellicott, JFB, Clarke, Wesley, Barnes (NT), Robertson's Word Pictures (NT), Catena Aurea, MKT Original Languages, MKT Context, and MKT Christological. Each verse gets a 100–250 word prose synthesis plus a `voices` array of 40–80 word excerpts. See `WS_AGENT_GUIDE.md` for content principles.

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

Work units target **≤45 verses** (typically 1–2 chapters). Long chapters (30+ verses) get their own row. Claim one row at a time — set Status to `in-progress @ <ISO timestamp>` before writing; set to `complete` after running and verifying.

| Script | Book | Chapters | Verses (est.) | Status |
|--------|------|----------|---------------|--------|
| ws-synthesis-hebrews-1-2.py | hebrews | 1–2 | ~32 | not started |
| ws-synthesis-hebrews-3-4.py | hebrews | 3–4 | ~35 | not started |
| ws-synthesis-hebrews-5-6.py | hebrews | 5–6 | ~34 | not started |
| ws-synthesis-hebrews-7.py | hebrews | 7 | ~28 | not started |
| ws-synthesis-hebrews-8-9.py | hebrews | 8–9 | ~41 | not started |
| ws-synthesis-hebrews-10.py | hebrews | 10 | ~39 | not started |
| ws-synthesis-hebrews-11.py | hebrews | 11 | ~40 | not started |
| ws-synthesis-hebrews-12.py | hebrews | 12 | ~29 | not started |
| ws-synthesis-hebrews-13.py | hebrews | 13 | ~25 | not started |
| ws-synthesis-romans-1.py | romans | 1 | ~32 | not started |
| ws-synthesis-romans-2.py | romans | 2 | ~29 | not started |
| ws-synthesis-romans-3.py | romans | 3 | ~31 | not started |
| ws-synthesis-romans-4.py | romans | 4 | ~25 | not started |
| ws-synthesis-romans-5-6.py | romans | 5–6 | ~44 | not started |
| ws-synthesis-romans-7.py | romans | 7 | ~25 | not started |
| ws-synthesis-romans-8.py | romans | 8 | ~39 | not started |
| ws-synthesis-romans-9.py | romans | 9 | ~33 | not started |
| ws-synthesis-romans-10.py | romans | 10 | ~21 | not started |
| ws-synthesis-romans-11.py | romans | 11 | ~36 | not started |
| ws-synthesis-romans-12-13.py | romans | 12–13 | ~35 | not started |
| ws-synthesis-romans-14.py | romans | 14 | ~23 | not started |
| ws-synthesis-romans-15.py | romans | 15 | ~33 | not started |
| ws-synthesis-romans-16.py | romans | 16 | ~27 | not started |
| ws-synthesis-galatians-1-2.py | galatians | 1–2 | ~45 | not started |
| ws-synthesis-galatians-3.py | galatians | 3 | ~29 | not started |
| ws-synthesis-galatians-4.py | galatians | 4 | ~31 | not started |
| ws-synthesis-galatians-5-6.py | galatians | 5–6 | ~44 | not started |
| ws-synthesis-ephesians-1-2.py | ephesians | 1–2 | ~45 | not started |
| ws-synthesis-ephesians-3.py | ephesians | 3 | ~21 | not started |
| ws-synthesis-ephesians-4.py | ephesians | 4 | ~32 | not started |
| ws-synthesis-ephesians-5.py | ephesians | 5 | ~33 | not started |
| ws-synthesis-ephesians-6.py | ephesians | 6 | ~24 | not started |
| ws-synthesis-1john-1-2.py | 1john | 1–2 | ~39 | not started |
| ws-synthesis-1john-3-4.py | 1john | 3–4 | ~45 | not started |
| ws-synthesis-1john-5.py | 1john | 5 | ~21 | not started |
| ws-synthesis-john-1.py | john | 1 | ~51 | not started |
| ws-synthesis-john-2.py | john | 2 | ~25 | not started |
| ws-synthesis-john-3.py | john | 3 | ~36 | not started |
| ws-synthesis-john-4.py | john | 4 | ~54 | not started |
| ws-synthesis-john-5.py | john | 5 | ~47 | not started |
| ws-synthesis-john-6.py | john | 6 | ~71 | not started |
| ws-synthesis-john-7.py | john | 7 | ~53 | not started |
| ws-synthesis-john-8.py | john | 8 | ~59 | not started |
| ws-synthesis-john-9.py | john | 9 | ~41 | not started |
| ws-synthesis-john-10.py | john | 10 | ~42 | not started |
| ws-synthesis-john-11.py | john | 11 | ~57 | not started |
| ws-synthesis-john-12.py | john | 12 | ~50 | not started |
| ws-synthesis-john-13.py | john | 13 | ~38 | not started |
| ws-synthesis-john-14.py | john | 14 | ~31 | not started |
| ws-synthesis-john-15.py | john | 15 | ~27 | not started |
| ws-synthesis-john-16.py | john | 16 | ~33 | not started |
| ws-synthesis-john-17.py | john | 17 | ~26 | not started |
| ws-synthesis-john-18.py | john | 18 | ~40 | not started |
| ws-synthesis-john-19.py | john | 19 | ~42 | not started |
| ws-synthesis-john-20.py | john | 20 | ~31 | not started |
| ws-synthesis-john-21.py | john | 21 | ~25 | not started |

*(Add OT work queue entries when Phase 4 begins.)*
