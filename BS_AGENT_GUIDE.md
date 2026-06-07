# Book Study — Agent Reference Guide

Read this file in full before writing any book study script.

---

## 1. What the Book Study is

The Book Study panel in the Original Language Study workshop gives a reader a world-class orientation to a biblical book before or alongside verse-by-verse study. It surfaces:

- Who wrote it, when, and why
- How the book is structured (outline)
- The central theological and literary themes with substantive treatment
- Key vocabulary: the characteristic words of this book with their original-language significance
- Christological reading: how this book fits the sweep to Christ
- How the book has been read through church history (reception)
- Practical reading guidance: what to watch for, common misreadings to avoid

---

## 2. What already exists — read this first

`data/books/introductions/{bookId}.json` contains a rich introduction for every one of the 66 books. **Read this file first for your claimed book.** It already has:

| Field | Content |
|-------|---------|
| `author` | Who wrote it and the basis for that attribution |
| `date` | Date of composition with historical context |
| `setting` | Provenance and occasion |
| `purpose` | Why the author wrote it |
| `themes` | Array of theme labels |
| `themes_detail` | Array of `{title, text}` — full paragraphs for each theme |
| `outline` | Array of `{label, chapters, ref}` — chapter-range outline |
| `key_verse` | The single most representative verse |
| `key_verses` | Array of `{ref, note}` — significant passages with explanation |
| `christ_connection` | Prose paragraph on how the book connects to Christ |
| `context` | Historical and canonical context paragraph |
| `key_people` | Array of `{name, role}` — major figures |
| `timeline` | `{date, before: [{label, ref}], after: [{label, ref}]}` — redemptive-historical placement |

**Do not reproduce this content in the supplemental file.** The UI merges both files; the introduction handles the fields above.

Also read:
- `data/literary/genre.json` — `{genre, sub[], literary_note, structure_note}` for this book
- `data/cultural/book-context.json` — `{historical_context, cultural_frameworks[], key_cultural_notes[]}` for this book

---

## 3. What the supplemental file adds

`data/workshop/book-study/{bookId}.json` adds four fields the introduction does not have:

### `key_vocabulary` (array of 12–18 entries)

The most characteristic vocabulary of this book, selected by two criteria:
1. **Author-distinctive words** — Strong's codes where the `peak` author in `data/grammar/author-freq-{greek|hebrew}.json` matches this book's author group (see Section 4 for the author group mapping)
2. **Theologically significant within this book** — words that carry interpretive weight in this book specifically

Each entry:
```json
{
  "code": "G1343",
  "lemma": "δικαιοσύνη",
  "translit": "dikaiosynē",
  "gloss": "righteousness",
  "significance": "2–3 sentences. WHY this word matters in this specific book — not a generic definition. The theological/literary/rhetorical load it carries here, what its semantic range implies that English loses, and how understanding the original changes interpretation."
}
```

**Quality bar for `significance`:** A reader should learn something they couldn't get from a dictionary. "This word means X" is not enough. "Paul uses this 33× in Romans (his highest density anywhere) always in the forensic register — God's declarative act, not a moral quality the believer develops" is the target.

Never just list words. Every entry needs a significance note that earns its place.

### `language_notes` (HTML string)

3–5 paragraphs on what the original language specifically reveals in this book. Not generic grammar — observations about THIS book.

For **NT Greek books:**
- Characteristic aspect choices (e.g., John's use of perfect tense for abiding states)
- Particle patterns and what they reveal about argument structure (e.g., Paul's γάρ/οὖν rhythm in Romans)
- Key Greek idioms or constructions that are opaque in English
- Genre-specific language features (e.g., diatribe in Romans, apocalyptic in Revelation)
- Any textual/manuscript issues that affect translation

For **OT Hebrew books:**
- Root-play and wordplay that disappears in English (e.g., הָעָם and עָמַל in Job, יהוה and the plot in Esther)
- Binyan choices that signal theological meaning
- Poetic structure if applicable (acrostics, parallelism patterns, cola structure)
- Narrative grammar — waw-consecutive chains, fronting for emphasis
- Any LXX divergences that are theologically significant

Length target: 400–700 words of HTML. Use `<p>` tags. No headings needed — the UI provides the section label.

### `reception` (HTML string)

A concise 300–400 word survey of how this book has been read through church history. One paragraph per major tradition is ideal:

- **Patristic** — which church fathers engaged it most and their signature interpretive moves
- **Medieval** — notable allegorical or scholastic readings if relevant
- **Reformation** — Luther, Calvin, or Zwingli if they wrote on it; the interpretive shift if any
- **Modern** — the one or two critical debates that define contemporary scholarship

Do not attempt comprehensiveness. Pick the most significant interpretive moments. A short paragraph that illuminates is better than a list of names.

### `reading_guide` (HTML string)

200–300 words of practical guidance for the student approaching this book in the workshop:

- What to watch for as you read verse by verse
- The single most important thing to understand before starting
- Common misreadings to avoid (with a sentence on why they happen)
- Where to start if dipping in rather than reading sequentially

---

## 4. Author group mapping

Use this to find characteristic vocabulary from the author-freq files.

**Greek (NT):**
| Books | Author group key |
|-------|-----------------|
| Matthew | `Matthew` |
| Mark | `Mark` |
| Luke, Acts | `Luke` |
| John, 1–3 John, Revelation | `John` |
| Romans, 1–2 Cor, Gal, Eph, Phil, Col, 1–2 Thess, 1–2 Tim, Titus, Philemon | `Paul` |
| Hebrews | `Hebrews` |
| James | `James` |
| 1–2 Peter | `Peter` |
| Jude | `Jude` |

**Hebrew (OT):**
| Books | Author group key |
|-------|-----------------|
| Genesis–Deuteronomy | `Moses` |
| Joshua–Esther | `Historical` |
| Job, Psalms, Proverbs, Ecclesiastes, Song of Solomon | `Wisdom` |
| Isaiah–Daniel | `Major` |
| Hosea–Malachi | `Minor` |

---

## 5. How to identify characteristic vocabulary

Run this Python snippet for any NT book (adjust `book_id` and `author_group`):

```python
import json

book_id    = 'romans'
author_group = 'Paul'

# Load author frequency data
freq = json.load(open('data/grammar/author-freq-greek.json'))

# Load glossary for lemma / translit / semantic_range
glossary = json.load(open('data/translation/glossary-greek.json'))

# Find words where this author peaks, sorted by their rate
candidates = [
    (code, data)
    for code, data in freq.items()
    if data.get('peak') == author_group
]
candidates.sort(key=lambda x: x[1]['rates'].get(author_group, 0), reverse=True)

# Show top 25 with glossary info
for code, data in candidates[:25]:
    g = glossary.get(code, {})
    rate = data['rates'].get(author_group, 0)
    print(f"{code:8} {g.get('lemma',''):20} {g.get('tiers',{}).get('literal',{}).get('primary',''):20} rate={rate:.2f}  {(g.get('semantic_range') or '')[:60]}")
```

For OT books, use `author-freq-hebrew.json` and `glossary-hebrew.json` instead.

From this list, pick 12–18 words that are:
1. Genuinely important to this book (not just frequent because of author group in general)
2. Words where the original-language insight matters — particles and prepositions rarely qualify unless the book's theology specifically hinges on one
3. A mix of content words (nouns, verbs) and 2–3 theologically contested terms if any exist for this book

---

## 6. Quality checklist

Before running the script, review your content dictionary:

- [ ] `key_vocabulary` has 12–18 entries, all with substantive `significance` notes (not just definitions)
- [ ] `language_notes` covers observations specific to THIS book, not generic grammar
- [ ] `reception` names specific figures or movements and what was distinctive about their reading
- [ ] `reading_guide` gives actionable guidance a student can act on immediately
- [ ] All HTML uses `<p>`, `<strong>`, `<em>` only — no `<h3>`, `<h4>`, `<ul>`, `<li>` (the UI provides structure)
- [ ] JSON is valid — no trailing commas, all strings properly escaped
- [ ] Script uses `merge_book_study()` so re-running never overwrites an already-populated field

---

## 7. What NOT to do

- Do not reproduce content from `data/books/introductions/{bookId}.json` — the UI already reads that file directly
- Do not write `significance` notes that just restate the dictionary gloss
- Do not add `language_notes` that are generic ("Greek has cases") rather than book-specific
- Do not write `reception` that is just a list of names without interpretive content
- Do not generate more than 18 `key_vocabulary` entries — quality over quantity
