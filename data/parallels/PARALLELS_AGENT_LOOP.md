# Parallels Data Expansion — Agent Loop Prompt

Paste this prompt into Claude Code when spawning a data-expansion agent.
Edit the TARGET BOOK block at the top before each run.

---

## AGENT TASK

You are filling `data/parallels/{book}.json` for a Bible study website.
The parallels feature shows synoptic parallel passages side-by-side in the reader.

**TARGET BOOK**: (set this before running — e.g. `1kings`)
**BOOK DISPLAY NAME**: (e.g. `1 Kings`)
**CHAPTERS TO FILL**: (e.g. `all` or `1-22`)

## SCHEMA

File path: `data/parallels/{book}.json`
Format:
```json
{
  "CH": {
    "V": [
      {
        "end": END_VERSE,
        "label": "Pericope title",
        "type": "parallel",
        "refs": [
          { "passage": "Book CH:V-V", "label": "Pericope title" }
        ]
      }
    ]
  }
}
```

- `CH` = chapter number as a string key
- `V` = start verse of the pericope (string key)
- `end` = last verse of the pericope in this chapter
- `type` must be exactly `"parallel"` (not prophecy-source, quotation, etc.)
- `refs` = array of parallel passages that tell the same story/event
- Each `passage` must use the canonical book name from `data/bible/books.json`
  (e.g. "1 Kings", "2 Chronicles", "Isaiah", "Matthew", "Mark")
- The label in `refs` should be the same as the parent label

## RULES

1. Only add entries for pericopes that genuinely share the same event or content
   across two or more Bible passages. Do not add cross-references — only true
   synoptic parallels (same story told in multiple books).
2. Valid parallel families:
   - Kings ↔ Chronicles (the main OT parallel)
   - Samuel ↔ Chronicles
   - 2 Kings ↔ Jeremiah ↔ Isaiah (Hezekiah narrative)
   - 2 Kings ↔ Jeremiah (Fall of Jerusalem)
   - The four Gospels (already well-covered in matthew/mark/luke/john.json)
   - Acts events that parallel Gospel events
3. Do NOT duplicate entries. If Matthew 3:1 already lists Mark 1:1-6 as a ref,
   you should add the reciprocal in mark.json but not re-add to matthew.json.
4. Check existing file before writing — merge with what's already there.
5. Short descriptive labels: "David's census", "Hezekiah's illness", "Passover kept".
6. If a pericope spans multiple chapters, use the chapter where it begins.
   `end` is the last verse of the pericope IN THAT CHAPTER ONLY (cross-chapter
   ranges are handled by the reader's verse range resolver automatically).

## VERIFICATION

After writing, run:
```
python3 -c "
import json
with open('data/parallels/{BOOK}.json') as f:
    d = json.load(f)
total = sum(len(vs) for ch in d.values() for vs in ch.values())
print(f'{len(d)} chapters, {total} pericopes')
# spot-check a pericope
ch1 = next(iter(d.values()))
v1 = next(iter(ch1.values()))
print(json.dumps(v1[0], indent=2))
"
```

Check the tracker at `data/parallels/PARALLELS_TRACKER.md` and mark your book DONE.

## TRACKER UPDATE

At the end, open `data/parallels/PARALLELS_TRACKER.md` and change the book row
from `[ ]` to `[x]` and add the pericope count.
