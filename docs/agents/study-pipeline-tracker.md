# Study Pipeline Tracker

> The single source of truth for the **Book Treatment** loop across all 66 books.
> Procedure: [study-pipeline.md](study-pipeline.md). One column: each book gets one
> Full Treatment. Agents update the cell as they work. **Do not push**; commit
> tracker edits with the work.
>
> Legend: `⬜` not started · `🔄 @<ISO-time> <agent> (n/N ch)` in progress ·
> `✅` complete (overview + all chapters exist + validate) · `♻️` reframe (fold
> existing hand-authored content into the treatment) · `⛔` blocked (no COW
> synthesis yet — not eligible).
>
> **Eligibility rule (owner, 2026-07-22):** a book gets a Full Treatment ONLY
> once its COW synthesis is complete — the treatment is built on the distilled
> `cow-synthesis/` tree, not the raw catena. Today **38 books** qualify
> (Genesis–1 Kings + the whole NT); the 27 zero-synthesis OT books and partial
> 2 Kings are blocked until the COW loop reaches them. See
> [cow-synthesis-loop.md](cow-synthesis-loop.md).
>
> Snapshot: **4/66** treatments complete (Philemon, Hebrews, **Romans**,
> **Revelation**); **34** more eligible now. Reference exemplar: **Philemon**.
> Reframe exemplars done: Hebrews, Romans (16 ch), Revelation (22 ch).
> **Psalms** is `⛔` blocked — it has NO COW synthesis; its overview `_book.json`
> is kept as a head-start for when synthesis lands.

| # | Book | T | Ch | Full Treatment |
|---:|------|:--:|--:|:--------------:|
| 1 | Genesis | OT | 50 | ⬜ |
| 2 | Exodus | OT | 40 | ⬜ |
| 3 | Leviticus | OT | 27 | ⬜ |
| 4 | Numbers | OT | 36 | ⬜ |
| 5 | Deuteronomy | OT | 34 | ⬜ |
| 6 | Joshua | OT | 24 | ⬜ |
| 7 | Judges | OT | 21 | ⬜ |
| 8 | Ruth | OT | 4 | ⬜ |
| 9 | 1 Samuel | OT | 31 | ⬜ |
| 10 | 2 Samuel | OT | 24 | ⬜ |
| 11 | 1 Kings | OT | 22 | ⬜ |
| 12 | 2 Kings | OT | 25 | ⬜ |
| 13 | 1 Chronicles | OT | 29 | ⬜ |
| 14 | 2 Chronicles | OT | 36 | ⬜ |
| 15 | Ezra | OT | 10 | ⬜ |
| 16 | Nehemiah | OT | 13 | ⬜ |
| 17 | Esther | OT | 10 | ⬜ |
| 18 | Job | OT | 42 | ⬜ |
| 19 | Psalms | OT | 150 | ⛔ blocked — no COW synthesis (overview only) |
| 20 | Proverbs | OT | 31 | ⬜ |
| 21 | Ecclesiastes | OT | 12 | ⬜ |
| 22 | Song of Solomon | OT | 8 | ⬜ |
| 23 | Isaiah | OT | 66 | ⬜ |
| 24 | Jeremiah | OT | 52 | ⬜ |
| 25 | Lamentations | OT | 5 | ⬜ |
| 26 | Ezekiel | OT | 48 | ⬜ |
| 27 | Daniel | OT | 12 | ⬜ |
| 28 | Hosea | OT | 14 | ⬜ |
| 29 | Joel | OT | 3 | ⬜ |
| 30 | Amos | OT | 9 | ⬜ |
| 31 | Obadiah | OT | 1 | ⬜ |
| 32 | Jonah | OT | 4 | ⬜ |
| 33 | Micah | OT | 7 | ⬜ |
| 34 | Nahum | OT | 3 | ⬜ |
| 35 | Habakkuk | OT | 3 | ⬜ |
| 36 | Zephaniah | OT | 3 | ⬜ |
| 37 | Haggai | OT | 2 | ⬜ |
| 38 | Zechariah | OT | 14 | ⬜ |
| 39 | Malachi | OT | 4 | ⬜ |
| 40 | Matthew | NT | 28 | ⬜ |
| 41 | Mark | NT | 16 | ⬜ |
| 42 | Luke | NT | 24 | ⬜ |
| 43 | John | NT | 21 | ⬜ |
| 44 | Acts | NT | 28 | ⬜ |
| 45 | Romans | NT | 16 | ✅ |
| 46 | 1 Corinthians | NT | 16 | ⬜ |
| 47 | 2 Corinthians | NT | 13 | ⬜ |
| 48 | Galatians | NT | 6 | ⬜ |
| 49 | Ephesians | NT | 6 | ⬜ |
| 50 | Philippians | NT | 4 | ⬜ |
| 51 | Colossians | NT | 4 | ⬜ |
| 52 | 1 Thessalonians | NT | 5 | ⬜ |
| 53 | 2 Thessalonians | NT | 3 | ⬜ |
| 54 | 1 Timothy | NT | 6 | ⬜ |
| 55 | 2 Timothy | NT | 4 | ⬜ |
| 56 | Titus | NT | 3 | ⬜ |
| 57 | Philemon | NT | 1 | ✅ |
| 58 | Hebrews | NT | 13 | ✅ |
| 59 | James | NT | 5 | ⬜ |
| 60 | 1 Peter | NT | 5 | ⬜ |
| 61 | 2 Peter | NT | 3 | ⬜ |
| 62 | 1 John | NT | 5 | ⬜ |
| 63 | 2 John | NT | 1 | ⬜ |
| 64 | 3 John | NT | 1 | ⬜ |
| 65 | Jude | NT | 1 | ⬜ |
| 66 | Revelation | NT | 22 | ✅ |
