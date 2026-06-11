# Paragraph Structure Work Queue

**Goal:** Generate `data/paragraphs/{bookId}.json` for all 66 books — paragraph breaks, types (narrative/poetry/dialogue/list/doxology), and section headings per chapter.

**Agent:** `PARA_AGENT_PROMPT.md`  
**Output directory:** `data/paragraphs/`

**Status values:** `not started` | `in-progress @ <ISO timestamp>` | `complete`

---

## New Testament (27 books)

| Book | bookId | Chs | Status |
|------|--------|-----|--------|
| Matthew | matthew | 28 | not started |
| Mark | mark | 16 | not started |
| Luke | luke | 24 | not started |
| John | john | 21 | not started |
| Acts | acts | 28 | not started |
| Romans | romans | 16 | not started |
| 1 Corinthians | 1corinthians | 16 | not started |
| 2 Corinthians | 2corinthians | 13 | not started |
| Galatians | galatians | 6 | not started |
| Ephesians | ephesians | 6 | not started |
| Philippians | philippians | 4 | not started |
| Colossians | colossians | 4 | not started |
| 1 Thessalonians | 1thessalonians | 5 | not started |
| 2 Thessalonians | 2thessalonians | 3 | not started |
| 1 Timothy | 1timothy | 6 | not started |
| 2 Timothy | 2timothy | 4 | not started |
| Titus | titus | 3 | not started |
| Philemon | philemon | 1 | not started |
| Hebrews | hebrews | 13 | not started |
| James | james | 5 | not started |
| 1 Peter | 1peter | 5 | not started |
| 2 Peter | 2peter | 3 | not started |
| 1 John | 1john | 5 | not started |
| 2 John | 2john | 1 | not started |
| 3 John | 3john | 1 | not started |
| Jude | jude | 1 | not started |
| Revelation | revelation | 22 | not started |

---

## Old Testament (39 books)

Long books (>25 chapters) are split into rows of ~25 chapters each.

| Book | bookId | Chs | Status |
|------|--------|-----|--------|
| Genesis 1–25 | genesis | 1–25 | not started |
| Genesis 26–50 | genesis | 26–50 | not started |
| Exodus 1–20 | exodus | 1–20 | not started |
| Exodus 21–40 | exodus | 21–40 | not started |
| Leviticus | leviticus | 27 | not started |
| Numbers 1–18 | numbers | 1–18 | not started |
| Numbers 19–36 | numbers | 19–36 | not started |
| Deuteronomy 1–17 | deuteronomy | 1–17 | not started |
| Deuteronomy 18–34 | deuteronomy | 18–34 | not started |
| Joshua | joshua | 24 | not started |
| Judges | judges | 21 | not started |
| Ruth | ruth | 4 | not started |
| 1 Samuel 1–16 | 1samuel | 1–16 | not started |
| 1 Samuel 17–31 | 1samuel | 17–31 | not started |
| 2 Samuel | 2samuel | 24 | not started |
| 1 Kings | 1kings | 22 | not started |
| 2 Kings 1–13 | 2kings | 1–13 | not started |
| 2 Kings 14–25 | 2kings | 14–25 | not started |
| 1 Chronicles 1–15 | 1chronicles | 1–15 | not started |
| 1 Chronicles 16–29 | 1chronicles | 16–29 | not started |
| 2 Chronicles 1–18 | 2chronicles | 1–18 | not started |
| 2 Chronicles 19–36 | 2chronicles | 19–36 | not started |
| Ezra | ezra | 10 | not started |
| Nehemiah | nehemiah | 13 | not started |
| Esther | esther | 10 | not started |
| Job 1–21 | job | 1–21 | not started |
| Job 22–42 | job | 22–42 | not started |
| Psalms 1–30 | psalms | 1–30 | not started |
| Psalms 31–60 | psalms | 31–60 | not started |
| Psalms 61–90 | psalms | 61–90 | not started |
| Psalms 91–120 | psalms | 91–120 | not started |
| Psalms 121–150 | psalms | 121–150 | not started |
| Proverbs 1–15 | proverbs | 1–15 | not started |
| Proverbs 16–31 | proverbs | 16–31 | not started |
| Ecclesiastes | ecclesiastes | 12 | not started |
| Song of Solomon | songofsolomon | 8 | not started |
| Isaiah 1–22 | isaiah | 1–22 | not started |
| Isaiah 23–44 | isaiah | 23–44 | not started |
| Isaiah 45–66 | isaiah | 45–66 | not started |
| Jeremiah 1–26 | jeremiah | 1–26 | not started |
| Jeremiah 27–52 | jeremiah | 27–52 | not started |
| Lamentations | lamentations | 5 | not started |
| Ezekiel 1–24 | ezekiel | 1–24 | not started |
| Ezekiel 25–48 | ezekiel | 25–48 | not started |
| Daniel | daniel | 12 | not started |
| Hosea | hosea | 14 | not started |
| Joel | joel | 3 | not started |
| Amos | amos | 9 | not started |
| Obadiah | obadiah | 1 | not started |
| Jonah | jonah | 4 | not started |
| Micah | micah | 7 | not started |
| Nahum | nahum | 3 | not started |
| Habakkuk | habakkuk | 3 | not started |
| Zephaniah | zephaniah | 3 | not started |
| Haggai | haggai | 2 | not started |
| Zechariah | zechariah | 14 | not started |
| Malachi | malachi | 4 | not started |
