#!/usr/bin/env python3
"""
Fetches Spurgeon's Morning and Evening (public domain, 1865) from GitHub
and emits two JSON files:

  data/devotionals/spurgeon-morning.json
  data/devotionals/spurgeon-evening.json

Each file is an object keyed by "MM-DD":
  {
    "01-01": {
      "verse_text": "They did eat of the fruit of the land…",
      "verse_ref":  "Joshua 5:12",
      "body":       "Israel's weary wanderings were all over…"
    },
    …
  }

Run from the repo root:  python3 scripts/fetch-spurgeon.py
"""

import json, re, urllib.request
from pathlib import Path

SRC_URL  = 'https://raw.githubusercontent.com/russianryebread/morning-and-evening/master/m_e.json'
OUT_DIR  = Path(__file__).resolve().parent.parent / 'data' / 'devotionals'

# Unicode separators used around the em-dash in this dataset
_DASH_RE = re.compile(r'[   ]*—[   ]*')


def _strip_header(body):
    """Remove the date/verse header lines from the body (first 2 non-blank lines)."""
    lines = body.replace('\r\n', '\n').split('\n')
    skipped = 0
    result = []
    for line in lines:
        stripped = line.strip()
        if skipped < 2:
            # Skip first two non-blank lines (date header + verse citation)
            if stripped:
                skipped += 1
            continue
        result.append(stripped)
    # Collapse multiple blank lines to one, strip leading/trailing blanks
    out = []
    prev_blank = False
    for line in result:
        if line == '':
            if not prev_blank:
                out.append('')
            prev_blank = True
        else:
            out.append(line)
            prev_blank = False
    return '\n'.join(out).strip()


def _parse_keyverse(keyverse):
    """Split 'verse text — Book Ch:V' into (text, ref)."""
    # Split on em-dash (with optional surrounding spaces/narrow-nobreak)
    parts = _DASH_RE.split(keyverse, maxsplit=1)
    if len(parts) == 2:
        text = parts[0].strip().strip('"').strip('“”')
        ref  = parts[1].strip()
    else:
        text = keyverse.strip()
        ref  = ''
    return text, ref


def _fmt_key(month, day):
    return f'{int(month):02d}-{int(day):02d}'


def main():
    print(f'Fetching {SRC_URL} …')
    with urllib.request.urlopen(SRC_URL) as resp:
        raw = json.loads(resp.read().decode('utf-8'))

    morning = {}
    evening = {}

    for entry in raw:
        if entry is None:
            continue
        key  = _fmt_key(entry['month'], entry['day'])
        kv   = entry.get('keyverse', '')
        body = entry.get('body', '')
        vtext, vref = _parse_keyverse(kv)
        cleaned_body = _strip_header(body)

        record = {'verse_text': vtext, 'verse_ref': vref, 'body': cleaned_body}

        if entry.get('time') == 'am':
            morning[key] = record
        else:
            evening[key] = record

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    m_path = OUT_DIR / 'spurgeon-morning.json'
    e_path = OUT_DIR / 'spurgeon-evening.json'

    m_path.write_text(json.dumps(morning, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    e_path.write_text(json.dumps(evening, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    print(f'  Morning: {len(morning)} entries → {m_path.relative_to(Path(__file__).parent.parent)}')
    print(f'  Evening: {len(evening)} entries → {e_path.relative_to(Path(__file__).parent.parent)}')


if __name__ == '__main__':
    main()
