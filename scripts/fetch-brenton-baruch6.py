#!/usr/bin/env python3
"""fetch-brenton-baruch6.py

Appends chapter 6 (Letter of Jeremiah, 73 verses) to
data/bible-apocrypha/BRENTON/baruch.json.

Source: Brenton's LXX 1851 text via eBible.org USFM zip.
The eBible.org BRENTON zip contains a separate USFM file for the
Letter of Jeremiah (LJE / Bar6). This script extracts those verses
and appends them as chapter "6" in baruch.json.

Fallback: if LJE is not in the zip, prints a diagnostic and exits 1.
"""

import io
import json
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BARUCH_PATH = REPO_ROOT / 'data' / 'bible-apocrypha' / 'BRENTON' / 'baruch.json'

# eBible.org BRENTON download URL (same source as fetch-apocrypha.py)
BRENTON_URL = 'https://ebible.org/Scriptures/eng-Brenton_usfm.zip'

USFM_STRIP = re.compile(
    r'\\(?:id|h|toc\d*|mt\d*|ms\d*|mr|s\d*|r|d|p|q\d*|b|li\d*|sp|nb|m|pi\d*|pc|mi|phi|'
    r'f \+.*?\\f\*|x \+.*?\\x\*|add|bk|it|em|bd|sc|nd|wj|qt|sig|sls|tl|dc|ord|pmo|pmc|pmr|'
    r'va|vp|ca|cp)[^\n]*',
    re.DOTALL,
)


def strip_usfm_inline(line: str) -> str:
    """Remove USFM markers from a single text line."""
    # Remove inline tags: \tag ...\tag*  or  \tag
    line = re.sub(r'\\[a-z]+\d*\*', '', line)
    line = re.sub(r'\\[a-z]+\d*\s', ' ', line)
    line = re.sub(r'\s+', ' ', line)
    return line.strip()


def parse_lxx_usfm(text: str) -> dict:
    """Parse USFM text and return {verse_num: verse_text} for all verses."""
    verses = {}
    current_verse = None
    parts = []

    for line in text.splitlines():
        line = line.strip()
        # Verse marker: \v N text...
        vm = re.match(r'^\\v\s+(\d+)\s*(.*)', line)
        if vm:
            # Save accumulated text for previous verse
            if current_verse is not None and parts:
                verses[current_verse] = ' '.join(parts).strip()
            current_verse = str(int(vm.group(1)))  # normalise: no leading zeros
            parts = [strip_usfm_inline(vm.group(2))] if vm.group(2).strip() else []
        elif current_verse is not None and line and not line.startswith('\\'):
            parts.append(strip_usfm_inline(line))
        elif current_verse is not None and line.startswith('\\') and not re.match(r'^\\[cspqbmh]', line):
            # continuation inline tag on its own line — treat as verse text
            cleaned = strip_usfm_inline(line)
            if cleaned:
                parts.append(cleaned)

    if current_verse is not None and parts:
        verses[current_verse] = ' '.join(parts).strip()

    return verses


def main():
    print(f'Downloading BRENTON zip from {BRENTON_URL} …')
    try:
        req = urllib.request.Request(BRENTON_URL, headers={'User-Agent': 'bible-study-fetch/1.0'})
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
    except Exception as e:
        print(f'ERROR: download failed: {e}')
        sys.exit(1)

    print(f'Downloaded {len(raw):,} bytes. Scanning for Letter of Jeremiah (LJE / Bar6) …')

    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        candidates = [n for n in zf.namelist()
                      if re.search(r'(?i)(lje|bar6|baruch.*6)', n)]
        print('Candidate files:', candidates if candidates else '(none found by name)')

        # Also search all files for \id LJE or \id BAR (which might include ch 6)
        lje_text = None
        for name in zf.namelist():
            if not name.endswith('.usfm') and not name.endswith('.SFM') and not name.endswith('.sfm'):
                continue
            content = zf.read(name).decode('utf-8', errors='replace')
            if re.search(r'\\id\s+LJE', content, re.IGNORECASE):
                print(f'Found LJE in: {name}')
                lje_text = content
                break

        if lje_text is None:
            # Try: maybe Baruch file has a second chapter marker \c 6
            for name in zf.namelist():
                if not (name.endswith('.usfm') or name.endswith('.SFM') or name.endswith('.sfm')):
                    continue
                content = zf.read(name).decode('utf-8', errors='replace')
                if re.search(r'\\id\s+BAR', content, re.IGNORECASE):
                    # Check for chapter 6
                    if re.search(r'\\c\s+6\b', content):
                        print(f'Found BAR with \\c 6 in: {name}')
                        # Extract just the chapter-6 portion
                        m = re.search(r'(\\c\s+6\b.*?)(?=\\c\s+7\b|$)', content, re.DOTALL)
                        if m:
                            lje_text = m.group(1)
                        break

    if lje_text is None:
        print('ERROR: Letter of Jeremiah (LJE / Baruch ch 6) not found in eBible.org BRENTON zip.')
        print('The eBible.org source does not include this chapter. DATA-9 remains blocked.')
        sys.exit(1)

    verses = parse_lxx_usfm(lje_text)
    if not verses:
        print('ERROR: No verses parsed from LJE text.')
        sys.exit(1)

    print(f'Parsed {len(verses)} verses for Letter of Jeremiah.')
    print(f'  v1 preview: {list(verses.values())[0][:100]}')

    # Load existing baruch.json and append chapter 6
    with open(BARUCH_PATH, encoding='utf-8') as f:
        baruch = json.load(f)

    chapters = baruch.get('chapters', baruch)
    if '6' in chapters:
        print('Chapter 6 already present — overwriting.')
    chapters['6'] = verses

    with open(BARUCH_PATH, 'w', encoding='utf-8') as f:
        json.dump(baruch, f, ensure_ascii=False, separators=(',', ':'))
        f.write('\n')

    print(f'SUCCESS: BRENTON/baruch.json now has chapters {sorted(chapters.keys())}')
    print(f'Total verses in ch 6: {len(chapters["6"])}')


if __name__ == '__main__':
    main()
