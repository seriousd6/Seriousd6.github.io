#!/usr/bin/env python3
"""
scripts/fetch-abbott-smith.py — fetch G.H. Abbott-Smith, Manual Greek Lexicon of
the New Testament (3rd ed., 1922) from CCEL and map entries to Strong's G codes.

Source: https://ccel.org/ccel/abbott_smith/lexicon
Output: data/strongs/abbott-smith.json
  Keys:   Strong's G code  (e.g. "G3056")
  Values: {gloss, def, classical_note, lxx_note}

Usage:
  python3 scripts/fetch-abbott-smith.py

Run seed-glossary.py afterwards to inject entries into phase bundles.
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
STRONGS_PATH = os.path.join(ROOT, 'data', 'strongs', 'greek.json')
OUT_PATH     = os.path.join(ROOT, 'data', 'strongs', 'abbott-smith.json')

LEXICON_URL = 'https://ccel.org/ccel/abbott_smith/lexicon'
BASE_URL    = 'https://ccel.org'
HEADERS     = {'User-Agent': 'Bible-Study-Website/1.0 personal-study (fetch-abbott-smith.py)'}
DELAY_S     = 1.5  # polite delay between requests


def build_lemma_index(strongs_path):
    """Build lemma → G code map from data/strongs/greek.json for headword matching."""
    with open(strongs_path, encoding='utf-8') as f:
        greek = json.load(f)
    by_lemma = {}
    for code, entry in greek.items():
        lemma = entry.get('lemma', '').strip()
        if lemma and code.startswith('G'):
            by_lemma.setdefault(lemma, code)
    return by_lemma


def _strip_diacritics(text):
    """Remove combining diacritical marks so accented variants still match."""
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')


def fetch_page_urls(session):
    """Return ordered list of sub-page URLs for the Abbott-Smith lexicon.

    CCEL presents longer books as paginated HTML.  The index page links to
    each sub-page (one per alphabetical block).  Fall back to the root URL
    if no internal links are found.
    """
    resp = session.get(LEXICON_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    seen = set()
    urls = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'abbott_smith/lexicon' in href and href not in seen:
            seen.add(href)
            full = href if href.startswith('http') else BASE_URL + href
            urls.append(full)

    # The landing page itself is always included
    if LEXICON_URL not in seen:
        urls.insert(0, LEXICON_URL)
    return urls


def extract_entries_from_page(soup):
    """Extract raw lexicon entries from a parsed CCEL page.

    Abbott-Smith entries follow a consistent structure:
      <b>GreekHeadword</b>, transliteration, definition text [; classical note]
    The <b> tag may appear inside a <p> or an <div class="entry">.
    We scan every block element that starts with a bold Greek word.
    """
    entries = []
    # Prefer the main content container
    body = (soup.find('div', class_='book')
            or soup.find('div', id='content')
            or soup.find('article')
            or soup.body)
    if not body:
        return entries

    for tag in body.find_all(['p', 'div']):
        # Skip deeply nested containers; only shallow div.entry-type blocks
        if tag.name == 'div' and not any(c in (tag.get('class') or [])
                                          for c in ('entry', 'lex-entry', 'p')):
            continue
        bolds = tag.find_all(['b', 'strong'], recursive=False) or tag.find_all(['b', 'strong'])
        if not bolds:
            continue

        hw = bolds[0].get_text(strip=True)
        # Require at least one Greek character in the headword
        if not re.search(r'[Ͱ-Ͽἀ-῿]', hw):
            continue

        full_text = tag.get_text(separator=' ', strip=True)
        # Strip headword from the front to isolate definition text
        hw_pos = full_text.find(hw)
        def_text = full_text[hw_pos + len(hw):].strip(' .,;:()')[:800]

        # Detect in-text Strong's code hints  (e.g. "= G3056")
        g_hint = ''
        gm = re.search(r'\bG(\d+)\b', full_text)
        if gm:
            g_hint = 'G' + gm.group(1)

        # Classical note — flagged by "Cl.", "class.", "classical", or "cf. cl."
        classical = ''
        cl_m = re.search(
            r'(?:(?:cf\.?\s+)?[Cc]l(?:ass)?\.?[,: ]+)([^.;]{10,200})', def_text)
        if cl_m:
            classical = cl_m.group(1).strip()

        # LXX note
        lxx = ''
        lxx_m = re.search(r'\bLXX[,: ]+([^.;]{10,200})', def_text)
        if lxx_m:
            lxx = lxx_m.group(1).strip()

        # Primary gloss — first token before comma/semicolon
        gloss = re.split(r'[;,]', def_text)[0].strip()[:150]

        entries.append({
            '_headword': hw,
            '_g_hint':   g_hint,
            'gloss':          gloss,
            'def':            def_text,
            'classical_note': classical,
            'lxx_note':       lxx,
        })

    return entries


def map_entries_to_strongs(entries, by_lemma):
    """Map each parsed entry to a Strong's G code.

    Strategy (in priority order):
      1. In-text G code hint present in the CCEL markup.
      2. Exact lemma match against data/strongs/greek.json.
      3. Diacritic-stripped fuzzy match (handles accentuation variants).
    """
    result     = {}
    unmatched  = []

    # Pre-build stripped-lemma index for fuzzy pass
    stripped   = {_strip_diacritics(lemma): code for lemma, code in by_lemma.items()}

    for e in entries:
        hw    = e['_headword']
        hint  = e['_g_hint']

        # Pass 1: trust explicit G code in text
        code  = hint if (hint and hint in {v for v in by_lemma.values()}) else ''

        # Pass 2: exact match
        if not code:
            code = by_lemma.get(hw, '')

        # Pass 3: diacritic-stripped match
        if not code:
            code = stripped.get(_strip_diacritics(hw), '')

        if not code:
            unmatched.append(hw)
            continue

        # Merge: first entry for a G code wins; later entries fill empty fields
        if code not in result:
            result[code] = {
                'gloss':          e['gloss'],
                'def':            e['def'],
                'classical_note': e['classical_note'],
                'lxx_note':       e['lxx_note'],
            }
        else:
            existing = result[code]
            if not existing['classical_note'] and e['classical_note']:
                existing['classical_note'] = e['classical_note']
            if not existing['lxx_note'] and e['lxx_note']:
                existing['lxx_note'] = e['lxx_note']

    return result, unmatched


def main():
    if not os.path.exists(STRONGS_PATH):
        print(f'ERROR: {STRONGS_PATH} not found. Run fetch-strongs.py first.')
        sys.exit(1)

    print('1/4  Building Strong\'s Greek lemma index…')
    by_lemma = build_lemma_index(STRONGS_PATH)
    print(f'     {len(by_lemma):,} lemmas indexed')

    session = requests.Session()

    print('2/4  Fetching Abbott-Smith page list from CCEL…')
    try:
        page_urls = fetch_page_urls(session)
    except Exception as ex:
        print(f'     ERROR fetching index: {ex}')
        sys.exit(1)
    print(f'     {len(page_urls)} pages to fetch')

    print('3/4  Extracting entries…')
    all_entries = []
    for i, url in enumerate(page_urls, 1):
        print(f'     [{i:3}/{len(page_urls)}] {url}', end='', flush=True)
        try:
            resp = session.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            soup    = BeautifulSoup(resp.text, 'html.parser')
            entries = extract_entries_from_page(soup)
            all_entries.extend(entries)
            print(f'  → {len(entries)} entries')
        except Exception as ex:
            print(f'  → SKIP ({ex})')
        if i < len(page_urls):
            time.sleep(DELAY_S)

    print(f'     Total raw entries: {len(all_entries)}')

    print('4/4  Mapping to Strong\'s G codes…')
    result, unmatched = map_entries_to_strongs(all_entries, by_lemma)
    print(f'     Mapped:    {len(result):,} entries')
    print(f'     Unmatched: {len(unmatched):,} headwords')
    if unmatched and len(unmatched) <= 20:
        for hw in unmatched[:20]:
            print(f'       {hw}')

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f'\nWrote {len(result):,} entries → {OUT_PATH}')
    print('Next: run scripts/seed-glossary.py to inject Abbott-Smith into phase bundles.')


if __name__ == '__main__':
    main()
