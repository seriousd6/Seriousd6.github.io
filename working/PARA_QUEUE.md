# Paragraph Structure Work Queue

**Goal:** Generate `data/paragraphs/{bookId}.json` for all 66 books — paragraph breaks, types (narrative/poetry/dialogue/list/doxology), and section headings per chapter.

**Agent:** `PARA_AGENT_PROMPT.md`  
**Output directory:** `data/paragraphs/`

**Status values:** `not started` | `in-progress @ <ISO timestamp>` | `complete`

---

## New Testament (27 books)

| Book | bookId | Chs | Status |
|------|--------|-----|--------|
| Matthew | matthew | 28 | complete |
| Mark | mark | 16 | complete |
| Luke | luke | 24 | complete |
| John | john | 21 | complete |
| Acts | acts | 28 | complete |
| Romans | romans | 16 | complete |
| 1 Corinthians | 1corinthians | 16 | complete |
| 2 Corinthians | 2corinthians | 13 | complete |
| Galatians | galatians | 6 | complete |
| Ephesians | ephesians | 6 | complete |
| Philippians | philippians | 4 | complete |
| Colossians | colossians | 4 | complete |
| 1 Thessalonians | 1thessalonians | 5 | complete |
| 2 Thessalonians | 2thessalonians | 3 | complete |
| 1 Timothy | 1timothy | 6 | complete |
| 2 Timothy | 2timothy | 4 | complete |
| Titus | titus | 3 | complete |
| Philemon | philemon | 1 | complete |
| Hebrews | hebrews | 13 | complete |
| James | james | 5 | complete |
| 1 Peter | 1peter | 5 | complete |
| 2 Peter | 2peter | 3 | complete |
| 1 John | 1john | 5 | complete |
| 2 John | 2john | 1 | complete |
| 3 John | 3john | 1 | complete |
| Jude | jude | 1 | complete |
| Revelation | revelation | 22 | complete |

---

## Old Testament (39 books)

Long books (>25 chapters) are split into rows of ~25 chapters each.

| Book | bookId | Chs | Status |
|------|--------|-----|--------|
| Genesis 1–25 | genesis | 1–25 | complete |
| Genesis 26–50 | genesis | 26–50 | complete |
| Exodus 1–20 | exodus | 1–20 | complete |
| Exodus 21–40 | exodus | 21–40 | complete |
| Leviticus | leviticus | 27 | complete |
| Numbers 1–18 | numbers | 1–18 | complete |
| Numbers 19–36 | numbers | 19–36 | complete |
| Deuteronomy 1–17 | deuteronomy | 1–17 | complete |
| Deuteronomy 18–34 | deuteronomy | 18–34 | complete |
| Joshua | joshua | 24 | complete |
| Judges | judges | 21 | complete |
| Ruth | ruth | 4 | complete |
| 1 Samuel 1–16 | 1samuel | 1–16 | complete |
| 1 Samuel 17–31 | 1samuel | 17–31 | complete |
| 2 Samuel | 2samuel | 24 | complete |
| 1 Kings | 1kings | 22 | complete |
| 2 Kings 1–13 | 2kings | 1–13 | complete |
| 2 Kings 14–25 | 2kings | 14–25 | complete |
| 1 Chronicles 1–15 | 1chronicles | 1–15 | complete |
| 1 Chronicles 16–29 | 1chronicles | 16–29 | complete |
| 2 Chronicles 1–18 | 2chronicles | 1–18 | complete |
| 2 Chronicles 19–36 | 2chronicles | 19–36 | complete |
| Ezra | ezra | 10 | complete |
| Nehemiah | nehemiah | 13 | complete |
| Esther | esther | 10 | complete |
| Job 1–21 | job | 1–21 | complete |
| Job 22–42 | job | 22–42 | complete |
| Psalms 1–30 | psalms | 1–30 | complete |
| Psalms 31–60 | psalms | 31–60 | complete |
| Psalms 61–90 | psalms | 61–90 | complete |
| Psalms 91–120 | psalms | 91–120 | complete |
| Psalms 121–150 | psalms | 121–150 | complete |
| Proverbs 1–15 | proverbs | 1–15 | complete |
| Proverbs 16–31 | proverbs | 16–31 | complete |
| Ecclesiastes | ecclesiastes | 12 | complete |
| Song of Solomon | songofsolomon | 8 | complete |
| Isaiah 1–22 | isaiah | 1–22 | complete |
| Isaiah 23–44 | isaiah | 23–44 | complete |
| Isaiah 45–66 | isaiah | 45–66 | complete |
| Jeremiah 1–26 | jeremiah | 1–26 | complete |
| Jeremiah 27–52 | jeremiah | 27–52 | complete |
| Lamentations | lamentations | 5 | complete |
| Ezekiel 1–24 | ezekiel | 1–24 | complete |
| Ezekiel 25–48 | ezekiel | 25–48 | complete |
| Daniel | daniel | 12 | complete |
| Hosea | hosea | 14 | complete |
| Joel | joel | 3 | complete |
| Amos | amos | 9 | complete |
| Obadiah | obadiah | 1 | complete |
| Jonah | jonah | 4 | complete |
| Micah | micah | 7 | complete |
| Nahum | nahum | 3 | complete |
| Habakkuk | habakkuk | 3 | complete |
| Zephaniah | zephaniah | 3 | complete |
| Haggai | haggai | 2 | complete |
| Zechariah | zechariah | 14 | complete |
| Malachi | malachi | 4 | complete |
