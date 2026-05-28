#!/usr/bin/env python3
"""
Enrich all 66 book intro JSON files with richer fields via the Claude API.

New fields added to each book:
  key_people      — list of {name, role}  (3–6 entries)
  context         — 2-sentence historical/cultural background
  christ_connection — 2-sentence note on how the book points to Christ
  key_verses      — list of {ref, note}  (3–4 entries)
  themes_detail   — list of {title, text}  (3–4 expanded theme paragraphs)

Usage:
  ANTHROPIC_API_KEY=sk-ant-... python3 scripts/enrich-book-intros.py

The script skips any book whose JSON already has 'key_people'.
Re-run with --overwrite to regenerate all.
"""

import json, os, sys, time, urllib.request, urllib.error

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
if not API_KEY:
    sys.exit("Error: ANTHROPIC_API_KEY environment variable not set.")

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "books", "introductions")
OVERWRITE = "--overwrite" in sys.argv

SYSTEM = (
    "You are a biblical scholar with expertise in both testaments. "
    "Respond ONLY with valid JSON — no markdown fences, no prose outside the JSON object."
)

PROMPT_TPL = """\
Given this existing book introduction data for the biblical book of {title}:

{existing}

Add the following new fields and return a JSON object containing ONLY these four new fields
(do not repeat any existing fields):

{{
  "key_people": [
    {{"name": "...", "role": "one sentence describing their significance"}}
    // 3–6 major figures; skip for short epistles with no named figures beyond the author
  ],
  "context": "2 sentences of historical and cultural background — date, audience, occasion, relevant ANE or Greco-Roman world context.",
  "christ_connection": "2 sentences on how this book anticipates, prefigures, or directly reveals Jesus Christ — specific types, prophecies, or themes.",
  "key_verses": [
    {{"ref": "Book Ch:V", "note": "one sentence on why this verse is pivotal"}}
    // 3–4 entries; use the canonical English book name
  ],
  "themes_detail": [
    {{"title": "Theme Name", "text": "3–4 sentences expanding on this theme within the book"}}
    // 3–4 entries that go deeper than the one-word theme chips already in the data
  ]
}}

Rules:
- All refs use the canonical English book name (e.g. "1 Corinthians 13:4", "Song of Solomon 8:6")
- key_people: skip figures whose role is already obvious from the book title alone unless their role is theologically significant
- Be theologically precise and confessionally orthodox (Reformed/evangelical)
- JSON only — no markdown, no explanation
"""


def call_claude(book_id, existing_data):
    prompt = PROMPT_TPL.format(
        title=existing_data.get("title", book_id),
        existing=json.dumps(existing_data, indent=2)
    )
    payload = json.dumps({
        "model": "claude-opus-4-7",
        "max_tokens": 1800,
        "system": SYSTEM,
        "messages": [{"role": "user", "content": prompt}]
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.loads(resp.read())
    text = body["content"][0]["text"].strip()
    # Strip any accidental markdown fences
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text)


def process(path, book_id):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    if not OVERWRITE and "key_people" in data:
        print(f"  skip  {book_id} (already enriched)")
        return False

    print(f"  fetch {book_id} ...", end=" ", flush=True)
    try:
        extras = call_claude(book_id, data)
    except Exception as e:
        print(f"ERROR: {e}")
        return False

    # Merge new fields into existing data (preserving field order)
    for key in ("key_people", "context", "christ_connection", "key_verses", "themes_detail"):
        if key in extras:
            data[key] = extras[key]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("done")
    return True


books = sorted(f[:-5] for f in os.listdir(OUT) if f.endswith(".json"))
print(f"Enriching {len(books)} books...\n")

ok, skip, fail = 0, 0, 0
for book_id in books:
    path = os.path.join(OUT, book_id + ".json")
    result = process(path, book_id)
    if result is True:
        ok += 1
        time.sleep(0.5)   # gentle rate-limit
    elif result is False and "already enriched" in open(path).read()[:0]:
        skip += 1
    else:
        if result is False:
            fail += 1

print(f"\nDone — updated: {ok}, skipped: {len(books)-ok-fail}, errors: {fail}")
