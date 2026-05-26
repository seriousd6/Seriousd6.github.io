#!/usr/bin/env python3
"""
fetch-strongs.py — Download Strong's dictionaries + interlinear word data.

Output:
  data/strongs/greek.json        — Strong's Greek dictionary (G1–G5624)
  data/strongs/hebrew.json       — Strong's Hebrew dictionary (H1–H8674)
  data/interlinear/{bookId}.json — per-book: {ch:{v:[{s,text}]}}

Data sources (all public domain):
  Strong's dicts    : openscriptures/strongs (GitHub raw JS files)
  Interlinear words : tahmmee/interlinear_bibledata (per-book, per-chapter JSON)

Usage:
  python3 scripts/fetch-strongs.py [--force]
"""

import argparse, json, os, re, sys, time, urllib.request

REPO_ROOT       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_STRONGS     = os.path.join(REPO_ROOT, 'data', 'strongs')
OUT_INTERLINEAR = os.path.join(REPO_ROOT, 'data', 'interlinear')
BOOKS_JSON      = os.path.join(REPO_ROOT, 'data', 'bible', 'books.json')

GREEK_DICT_URL  = 'https://raw.githubusercontent.com/openscriptures/strongs/master/greek/strongs-greek-dictionary.js'
HEBREW_DICT_URL = 'https://raw.githubusercontent.com/openscriptures/strongs/master/hebrew/strongs-hebrew-dictionary.js'
TAHMMEE_BASE    = 'https://raw.githubusercontent.com/tahmmee/interlinear_bibledata/master/src'

# tahmmee uses different dir names for numbered books and compound names
TAHMMEE_BOOK_MAP = {
    '1chronicles':    'i_chronicles',
    '2chronicles':    'ii_chronicles',
    '1corinthians':   'i_corinthians',
    '2corinthians':   'ii_corinthians',
    '1john':          'i_john',
    '2john':          'ii_john',
    '3john':          'iii_john',
    '1kings':         'i_kings',
    '2kings':         'ii_kings',
    '1peter':         'i_peter',
    '2peter':         'ii_peter',
    '1samuel':        'i_samuel',
    '2samuel':        'ii_samuel',
    '1thessalonians': 'i_thessalonians',
    '2thessalonians': 'ii_thessalonians',
    '1timothy':       'i_timothy',
    '2timothy':       'ii_timothy',
    'songofsolomon':  'song_of_solomon',
}


def fetch(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'bsw-fetch/1.0'})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode('utf-8', errors='replace')
    except Exception:
        return None


def parse_strongs_js(js_text):
    """
    Extract JSON from openscriptures Strong's JS files.
    Format: var strongs_xxx_dictionary = { ... };\n\nmodule.exports = ...
    The file ends with `};\n\nmodule.exports = ...` which makes vanilla json.loads fail.
    """
    m = re.search(r'\{', js_text)
    if not m:
        return None
    start = m.start()
    json_str = js_text[start:]
    # Strip trailing `;\nmodule.exports = ...` after the final `}`
    json_str = re.sub(r'\}\s*;\s*(module\.exports\s*=.*)?$', '}', json_str.rstrip())
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f'    JSON parse error: {e}')
        return None


def _normalize_strongs(raw):
    """Normalize 'g25' or 'G0025' or 'h7225' to 'G25' / 'H7225'."""
    if not raw:
        return ''
    raw = raw.strip()
    if raw and raw[0].lower() in ('g', 'h'):
        prefix = raw[0].upper()
        num    = raw[1:].lstrip('0') or '0'
        return prefix + num
    return raw


def transform_greek(raw):
    out = {}
    for key, entry in raw.items():
        k = _normalize_strongs(key.strip())
        pron = entry.get('pronun', {})
        out[k] = {
            'lemma':    entry.get('lemma', ''),
            'translit': entry.get('translit') or pron.get('sbl') or pron.get('dict') or '',
            'pronounce': pron.get('dict') or pron.get('sbl') or '',
            'gloss':    (entry.get('kjv_def') or entry.get('kjv') or '').strip(),
            'def':      (entry.get('strongs_def') or '').strip(),
            'deriv':    (entry.get('derivation') or '').strip(),
        }
    return out


def transform_hebrew(raw):
    out = {}
    for key, entry in raw.items():
        k = _normalize_strongs(key.strip())
        pron = entry.get('pronun', {})
        out[k] = {
            'lemma':    entry.get('lemma', ''),
            'translit': entry.get('translit') or pron.get('sbl') or pron.get('dict') or '',
            'pronounce': pron.get('dict') or pron.get('sbl') or '',
            'gloss':    (entry.get('kjv_def') or entry.get('kjv') or '').strip(),
            'def':      (entry.get('strongs_def') or '').strip(),
            'deriv':    (entry.get('derivation') or '').strip(),
        }
    return out


def fetch_interlinear_book(book_id, num_chapters, force=False):
    """
    Download all chapters for a book from tahmmee/interlinear_bibledata.
    Returns dict: {ch_str: {v_str: [{s, text}]}} or None if nothing fetched.
    """
    tahmmee_id = TAHMMEE_BOOK_MAP.get(book_id, book_id)
    result = {}
    fetched = 0

    for ch in range(1, num_chapters + 1):
        url  = f'{TAHMMEE_BASE}/{tahmmee_id}/{ch}.json'
        text = fetch(url)
        if not text:
            continue

        try:
            ch_data = json.loads(text)
        except Exception:
            continue

        # ch_data: {verse_str: [{text:..., number:...}, ...]}
        if not isinstance(ch_data, dict):
            continue

        ch_out = {}
        for v_str, words in ch_data.items():
            if not isinstance(words, list):
                continue
            tokens = []
            for wd in words:
                s    = _normalize_strongs(str(wd.get('number', '') or ''))
                text_w = (wd.get('text') or '').strip()
                if s or text_w:
                    tokens.append({'s': s, 'text': text_w})
            if tokens:
                ch_out[v_str] = tokens
        if ch_out:
            result[str(ch)] = ch_out
            fetched += 1

        # Polite rate limit: 10 req/s max
        time.sleep(0.1)

    return result if fetched else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true', help='Re-generate existing files')
    args = parser.parse_args()

    os.makedirs(OUT_STRONGS,     exist_ok=True)
    os.makedirs(OUT_INTERLINEAR, exist_ok=True)

    with open(BOOKS_JSON) as f:
        books_meta = json.load(f)

    # ── 1. Strong's Greek dictionary ─────────────────────────────────────────
    greek_out = os.path.join(OUT_STRONGS, 'greek.json')
    if os.path.exists(greek_out) and not args.force:
        print('data/strongs/greek.json exists — skipping (--force to re-fetch)')
    else:
        print('Fetching Strong\'s Greek dictionary…')
        js = fetch(GREEK_DICT_URL, timeout=60)
        if js:
            raw = parse_strongs_js(js)
            if raw:
                compact = transform_greek(raw)
                with open(greek_out, 'w', encoding='utf-8') as f:
                    json.dump(compact, f, ensure_ascii=False, separators=(',', ':'))
                print(f'  Saved {len(compact)} Greek entries → data/strongs/greek.json')
            else:
                print('  ERROR: Could not parse Greek JS')
        else:
            print('  ERROR: Could not download Greek dict')

    # ── 2. Strong's Hebrew dictionary ────────────────────────────────────────
    hebrew_out = os.path.join(OUT_STRONGS, 'hebrew.json')
    if os.path.exists(hebrew_out) and not args.force:
        print('data/strongs/hebrew.json exists — skipping (--force to re-fetch)')
    else:
        print('Fetching Strong\'s Hebrew dictionary…')
        js = fetch(HEBREW_DICT_URL, timeout=60)
        if js:
            raw = parse_strongs_js(js)
            if raw:
                compact = transform_hebrew(raw)
                with open(hebrew_out, 'w', encoding='utf-8') as f:
                    json.dump(compact, f, ensure_ascii=False, separators=(',', ':'))
                print(f'  Saved {len(compact)} Hebrew entries → data/strongs/hebrew.json')
            else:
                print('  ERROR: Could not parse Hebrew JS')
        else:
            print('  ERROR: Could not download Hebrew dict')

    # ── 3. Interlinear per-book ───────────────────────────────────────────────
    print('\nFetching interlinear data from tahmmee/interlinear_bibledata…')
    saved = skipped = failed = 0

    for bk in books_meta:
        bid      = bk['id']
        n_ch     = bk.get('chapters', 1)
        out_path = os.path.join(OUT_INTERLINEAR, bid + '.json')

        if os.path.exists(out_path) and not args.force:
            skipped += 1
            continue

        print(f'  {bk["name"]} ({n_ch} ch)…', end=' ', flush=True)
        data = fetch_interlinear_book(bid, n_ch)
        if data:
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
            v_count = sum(len(vs) for ch in data.values() for vs in [ch])
            print(f'{len(data)} chapters')
            saved += 1
        else:
            print('no data')
            failed += 1

    print(f'\nDone. Saved: {saved}  Skipped: {skipped}  Failed: {failed}')
    print(f'  Strongs   : {OUT_STRONGS}')
    print(f'  Interlinear: {OUT_INTERLINEAR}')


if __name__ == '__main__':
    main()
