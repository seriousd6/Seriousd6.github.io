#!/usr/bin/env python3
"""
scripts/fetch-gesenius.py — fetch Wilhelm Gesenius, Hebrew-Chaldee Lexicon to the
Old Testament (Tregelles translation, 1857) from archive.org and map entries to
Strong's H codes.

Source: archive.org — public domain (pre-1923)
Output: data/strongs/gesenius.json
  Keys:   Strong's H code  (e.g. "H2617")
  Values: {gloss, def, cognates, root_note}
    gloss      — primary gloss / headword
    def        — main definition text
    cognates   — Semitic cognate languages note (Arabic, Aramaic, Syriac, Phoenician)
    root_note  — etymology, root derivation, or Persian/loan-word note

Usage:
  python3 scripts/fetch-gesenius.py

Run seed-glossary.py afterwards to inject entries into phase bundles.

Archive.org identifiers tried in order (any public domain scan will do):
  geseniushebrew00geseuoft  (Toronto scan, 1859 corrected edition — high quality)
  gesenius1847hebrewlex     (alternative)
"""
import json
import os
import re
import sys
import time
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print('Missing dependencies. Install: pip install requests beautifulsoup4')
    sys.exit(1)

ROOT         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRONGS_PATH = os.path.join(ROOT, 'data', 'strongs', 'hebrew.json')
OUT_PATH     = os.path.join(ROOT, 'data', 'strongs', 'gesenius.json')

# archive.org full-text search URL for Gesenius
ARCHIVE_BASE = 'https://archive.org'
ARCHIVE_IDS  = [
    'geseniushebrew00geseuoft',
    'gesenius1847hebrewlex',
    'hebrewchaldeelex00geserich',
]
HEADERS  = {'User-Agent': 'Bible-Study-Website/1.0 personal-study (fetch-gesenius.py)'}
DELAY_S  = 1.5

# Semitic cognate language markers in Gesenius entries
_COGNATE_LANGS = re.compile(
    r'\b(?:Arab(?:ic)?|Aram(?:aic)?|Syr(?:iac)?|Phoen(?:ician)?|Eth(?:iopic)?'
    r'|Akk(?:adian)?|Ugar(?:itic)?|Assyr(?:ian)?)\b',
    re.I
)
_ROOT_MARKERS = re.compile(
    r'(?:from|root|deriv(?:ed)?|cognate|akin|related)\s+(?:of|to|from)\s+',
    re.I
)


def build_lemma_index(strongs_path):
    """Build lemma → H code map from data/strongs/hebrew.json."""
    with open(strongs_path, encoding='utf-8') as f:
        hebrew = json.load(f)
    by_lemma = {}
    for code, entry in hebrew.items():
        lemma = entry.get('lemma', '').strip()
        if lemma and code.startswith('H'):
            by_lemma.setdefault(lemma, code)
    return by_lemma


def _strip_niqqud(text):
    """Remove Hebrew vowel points (niqqud) and cantillation marks for fuzzy matching.
    Hebrew niqqud: U+05B0–U+05BD, U+05BF, U+05C1–U+05C2, U+05C4–U+05C5, U+05C7
    Cantillation: U+0591–U+05AF
    """
    return re.sub(r'[֑-ְ֯-ׇ]', '', text).strip()


def fetch_archive_text(session, archive_id):
    """Fetch plain-text content of an archive.org item via the djvu/text endpoint."""
    # Try the plain-text endpoint (fast) before falling back to full HTML page list
    txt_url = f'{ARCHIVE_BASE}/stream/{archive_id}/{archive_id}_djvu.txt'
    try:
        resp = session.get(txt_url, headers=HEADERS, timeout=60)
        if resp.status_code == 200 and len(resp.text) > 5000:
            return resp.text, 'text'
    except Exception:
        pass

    # Fallback: scan the item's page list for OCR text files
    meta_url = f'{ARCHIVE_BASE}/metadata/{archive_id}'
    resp = session.get(meta_url, headers=HEADERS, timeout=30)
    if resp.status_code != 200:
        return None, None
    meta = resp.json()
    files = meta.get('files', [])
    # Prefer _djvu.txt; fall back to _text.pdf → not useful, or _abbyy.gz (skip)
    for f in files:
        name = f.get('name', '')
        if name.endswith('_djvu.txt'):
            dl_url = f'{ARCHIVE_BASE}/download/{archive_id}/{name}'
            r2 = session.get(dl_url, headers=HEADERS, timeout=60)
            if r2.status_code == 200:
                return r2.text, 'text'
    return None, None


def extract_entries_from_text(text):
    """Parse Gesenius OCR plain text into a list of entry dicts.

    Gesenius entries follow the pattern:
      Hebrew headword (maybe transliteration)  definition text  [cognate notes]

    Because OCR quality varies, we use heuristics:
    - Hebrew letters (U+05D0–U+05EA) mark entry headwords
    - Lines starting with 2+ Hebrew letters followed by space are entry starts
    """
    entries = []
    current = None

    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue

        # Detect start of new entry: line begins with Hebrew characters
        hebrew_start = re.match(r'^([א-תװ-״יִ-פְֿ-ׇ]+)', line)
        if hebrew_start and len(hebrew_start.group(1)) >= 1:
            if current:
                entries.append(current)
            hw = hebrew_start.group(1)
            rest = line[len(hebrew_start.group(0)):].strip(' .,;()').strip()
            current = {
                '_headword': hw,
                '_lines':    [rest] if rest else [],
            }
        elif current:
            current['_lines'].append(line)

    if current:
        entries.append(current)

    # Convert raw lines into structured fields
    result = []
    for e in entries:
        full_def = ' '.join(e['_lines'])[:800]
        hw = e['_headword']

        # Primary gloss — first comma/semicolon-delimited clause
        gloss = re.split(r'[;,]', full_def)[0].strip()[:150]

        # Cognate note: sentence(s) containing language names
        cognate_lines = [s.strip() for s in re.split(r'[.;]', full_def)
                         if _COGNATE_LANGS.search(s)]
        cognates = '; '.join(cognate_lines[:3])[:300]

        # Root note: etymology / derivation sentences
        root_lines = [s.strip() for s in re.split(r'[.;]', full_def)
                      if _ROOT_MARKERS.search(s)]
        root_note = '; '.join(root_lines[:2])[:200]

        result.append({
            '_headword': hw,
            'gloss':     gloss,
            'def':       full_def,
            'cognates':  cognates,
            'root_note': root_note,
        })
    return result


def extract_entries_from_html(soup):
    """Fallback HTML parser for structured CCEL or other HTML Gesenius sources."""
    entries = []
    body = (soup.find('div', class_='book') or soup.find('div', id='content') or soup.body)
    if not body:
        return entries

    for p in body.find_all('p'):
        bolds = p.find_all(['b', 'strong'])
        if not bolds:
            continue
        hw = bolds[0].get_text(strip=True)
        if not re.search(r'[א-ת]', hw):
            continue
        full_text = p.get_text(separator=' ', strip=True)
        def_text = full_text[len(hw):].strip(' .,;')[:600]
        cognate_lines = [s.strip() for s in re.split(r'[.;]', def_text)
                         if _COGNATE_LANGS.search(s)]
        cognates = '; '.join(cognate_lines[:3])[:300]
        root_lines = [s.strip() for s in re.split(r'[.;]', def_text)
                      if _ROOT_MARKERS.search(s)]
        root_note = '; '.join(root_lines[:2])[:200]
        entries.append({
            '_headword': hw,
            'gloss':     re.split(r'[;,]', def_text)[0].strip()[:150],
            'def':       def_text,
            'cognates':  cognates,
            'root_note': root_note,
        })
    return entries


def map_entries_to_strongs(entries, by_lemma):
    """Map parsed Gesenius entries to Strong's H codes by Hebrew headword matching."""
    result    = {}
    unmatched = []

    # Build niqqud-stripped index for fuzzy pass
    stripped  = {_strip_niqqud(lemma): code for lemma, code in by_lemma.items()}

    for e in entries:
        hw    = e['_headword']

        # Pass 1: exact lemma match (with niqqud)
        code  = by_lemma.get(hw, '')

        # Pass 2: niqqud-stripped fuzzy match
        if not code:
            code = stripped.get(_strip_niqqud(hw), '')

        if not code:
            unmatched.append(hw)
            continue

        if code not in result:
            result[code] = {
                'gloss':     e['gloss'],
                'def':       e['def'],
                'cognates':  e['cognates'],
                'root_note': e['root_note'],
            }
        else:
            existing = result[code]
            if not existing['cognates'] and e['cognates']:
                existing['cognates'] = e['cognates']
            if not existing['root_note'] and e['root_note']:
                existing['root_note'] = e['root_note']

    return result, unmatched


def main():
    if not os.path.exists(STRONGS_PATH):
        print(f'ERROR: {STRONGS_PATH} not found. Run fetch-strongs.py first.')
        sys.exit(1)

    print('1/4  Building Strong\'s Hebrew lemma index…')
    by_lemma = build_lemma_index(STRONGS_PATH)
    print(f'     {len(by_lemma):,} lemmas indexed')

    session = requests.Session()

    print('2/4  Fetching Gesenius text from archive.org…')
    raw_text  = None
    used_id   = None

    for archive_id in ARCHIVE_IDS:
        print(f'     Trying {archive_id}…', end='', flush=True)
        try:
            text, fmt = fetch_archive_text(session, archive_id)
            if text:
                raw_text = text
                used_id  = archive_id
                print(f' OK ({fmt}, {len(text):,} chars)')
                break
            else:
                print(' no text found')
        except Exception as ex:
            print(f' ERROR: {ex}')
        time.sleep(DELAY_S)

    if not raw_text:
        print('\nERROR: Could not retrieve Gesenius text from any archive.org source.')
        print('Manual option: download the _djvu.txt file from archive.org and run:')
        print('  python3 scripts/fetch-gesenius.py --file /path/to/gesenius.txt')
        sys.exit(1)

    print(f'3/4  Extracting entries from {used_id}…')
    entries = extract_entries_from_text(raw_text)
    print(f'     {len(entries):,} raw entries extracted')

    print('4/4  Mapping to Strong\'s H codes…')
    result, unmatched = map_entries_to_strongs(entries, by_lemma)
    print(f'     Mapped:    {len(result):,} entries')
    print(f'     Unmatched: {len(unmatched):,} headwords')
    if unmatched and len(unmatched) <= 20:
        for hw in unmatched[:20]:
            print(f'       {hw}')

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f'\nWrote {len(result):,} entries → {OUT_PATH}')
    print('Next: run scripts/seed-glossary.py to inject Gesenius into phase bundles.')


if __name__ == '__main__':
    main()
