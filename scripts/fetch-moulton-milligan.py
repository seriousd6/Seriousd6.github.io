#!/usr/bin/env python3
"""
scripts/fetch-moulton-milligan.py — fetch and parse G.H. Moulton & G. Milligan,
Vocabulary of the Greek New Testament Illustrated from the Papyri and Other
Non-Literary Sources (Hodder & Stoughton, 1930; public domain).

This lexicon is the definitive reference for NT Greek as ordinary Koine — showing
how words like λόγος, ἀγάπη, and πίστις appear in non-literary papyri (receipts,
letters, contracts), demonstrating that NT Greek was not "Holy Ghost Greek" but
the common language of everyday life.

Source: archive.org OCR text of the 1930 volume.
Primary archive ID: vocabularyofgree00mouluoft (tries several fallbacks).

Output:
  data/strongs/moulton-milligan.json  keyed by G code:
    { entry_text: str, papyri_examples: [{citation, text, note}] }

Coverage: top ~500 NT Greek codes by frequency; partial coverage elsewhere.
The fetch will succeed for entries where the OCR is clean enough to parse.

Usage: python3 scripts/fetch-moulton-milligan.py
"""
import json
import os
import re
import time
import unicodedata

try:
    import urllib.request as urlreq
except ImportError:
    import urllib as urlreq

ROOT      = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRONGS   = os.path.join(ROOT, 'data', 'strongs')
OUT_PATH  = os.path.join(STRONGS, 'moulton-milligan.json')
CACHE_DIR = os.path.join(ROOT, 'scripts', '_cache')

# Top NT Greek codes by frequency (same set as Phase 1 + high-dispute codes)
# Priority: codes where M&M evidence is most useful for the Workshop
PRIORITY_G_CODES = [
    'G3056',  # λόγος — word/reason/account
    'G26',    # ἀγάπη — love
    'G4102',  # πίστις — faith/faithfulness
    'G1343',  # δικαιοσύνη — righteousness
    'G4561',  # σάρξ — flesh/sinful nature
    'G166',   # αἰώνιος — eternal
    'G5485',  # χάρις — grace/favour
    'G2222',  # ζωή — life
    'G4151',  # πνεῦμα — spirit
    'G40',    # ἅγιος — holy
    'G2316',  # θεός — God
    'G2962',  # κύριος — Lord
    'G1391',  # δόξα — glory
    'G1515',  # εἰρήνη — peace
    'G1680',  # ἐλπίς — hope
    'G2041',  # ἔργον — work/deed
    'G1242',  # διαθήκη — covenant/testament
    'G3340',  # μετανοέω — repent/change mind
    'G907',   # βαπτίζω — baptize/immerse
    'G3670',  # ὁμολογέω — confess/acknowledge
    'G2842',  # κοινωνία — fellowship/sharing
    'G3551',  # νόμος — law
    'G4991',  # σωτηρία — salvation
    'G652',   # ἀπόστολος — apostle/sent one
    'G3340',  # μετανοέω
    'G1515',  # εἰρήνη
    'G225',   # ἀλήθεια — truth
    'G444',   # ἄνθρωπος — man/human being
    'G5590',  # ψυχή — soul/life
    'G2424',  # Ἰησοῦς — Jesus
    'G5547',  # Χριστός — Christ
]

# Archive.org IDs to try for the M&M volume
ARCHIVE_IDS = [
    'vocabularyofgree00mouluoft',
    'vocabularyofgreek0000moul',
    'VocabularyGreekNT1930',
]

# Papyri citation patterns: P.Oxy, BGU, P.Lond, P.Tebt, P.Flor, P.Giess etc.
PAPYRI_RE = re.compile(
    r'((?:P\.|BGU|PSI|CPR|SB|UPZ)\s*[A-Za-z]*\.?\s*\d+(?:\.\d+)?(?:\s+\(\w+\.?\s*\d+\))?)',
    re.IGNORECASE
)

# Greek word detection: starts with Greek Unicode character
GREEK_START_RE = re.compile(r'^[Ͱ-Ͽἀ-῿]')

# M&M entry header pattern: Greek word followed by inflection info
ENTRY_HEAD_RE = re.compile(
    r'^([Ͱ-Ͽἀ-῿][Ͱ-Ͽἀ-῿\s\-,]+?)'
    r'\s*[\.,]',
    re.MULTILINE
)


def _strip_diacritics(text):
    """Remove Greek diacritical marks for fuzzy matching."""
    nfkd = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))


def build_lemma_index():
    """Build {stripped_lemma: G_code} map from greek.json for matching."""
    path = os.path.join(STRONGS, 'greek.json')
    if not os.path.exists(path):
        print('  Warning: greek.json not found — lemma matching disabled')
        return {}
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    index = {}
    for code, entry in data.items():
        if not code.startswith('G'):
            continue
        lemma = entry.get('lemma', '')
        if lemma:
            stripped = _strip_diacritics(lemma).lower()
            index[stripped] = code
    print(f'  Lemma index: {len(index):,} G codes')
    return index


def _fetch_url(url, timeout=30):
    """Fetch URL text with a simple User-Agent header. Returns text or None."""
    try:
        req = urlreq.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlreq.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f'    fetch {url[:60]}… — {e}')
        return None


def fetch_archive_text(archive_id):
    """Try to fetch full OCR text from archive.org DjVu endpoint."""
    cache_path = os.path.join(CACHE_DIR, f'mm_{archive_id}.txt')
    if os.path.exists(cache_path):
        print(f'  Using cached text for {archive_id}')
        with open(cache_path, encoding='utf-8') as f:
            return f.read()

    # Try DjVu full-text endpoint
    djvu_url = f'https://archive.org/download/{archive_id}/{archive_id}_djvu.txt'
    print(f'  Trying DjVu text: {archive_id}…')
    text = _fetch_url(djvu_url)
    if text and len(text) > 10000:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(cache_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'    Got {len(text):,} chars')
        return text

    # Try alternate text endpoint
    txt_url = f'https://archive.org/download/{archive_id}/{archive_id}.txt'
    print(f'  Trying plain text: {archive_id}…')
    text = _fetch_url(txt_url)
    if text and len(text) > 10000:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(cache_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'    Got {len(text):,} chars')
        return text

    return None


def extract_papyri_examples(entry_text):
    """Extract papyri citation blocks from an M&M entry text.

    Looks for patterns like: P.Oxy. 113.9 (A.D. 100) "account of bronze money"
    Returns list of {citation, text, note} dicts (up to 3).
    """
    examples = []
    # Split into sentences/clauses around papyri citation markers
    segments = re.split(r'\n|(?<=\.)\s+(?=[A-Z\(])', entry_text)
    for seg in segments:
        m = PAPYRI_RE.search(seg)
        if not m:
            continue
        citation = m.group(1).strip()
        # Text after the citation
        after = seg[m.end():].strip()
        # Extract quoted text (in quotes or significant snippet)
        quote = ''
        q_match = re.search(r'["“]([^"”]{5,120})["”]', after)
        if q_match:
            quote = q_match.group(1).strip()
        else:
            # Take up to 100 chars of context
            quote = after[:100].strip()

        if citation and (quote or len(after) > 10):
            examples.append({
                'citation': citation,
                'text': quote or after[:80],
                'note': '',
            })
        if len(examples) >= 3:
            break
    return examples


def parse_entries_from_text(text, lemma_index):
    """Parse M&M OCR text into {G_code: {entry_text, papyri_examples}}.

    M&M entries are alphabetical by lemma. Each entry starts with a Greek word
    (or transliteration) followed by grammatical info, then definition and
    papyri citations. OCR quality is variable.

    Strategy:
    1. Find lines that start with Greek characters
    2. Collect text until next Greek-headed line
    3. Try to map the lemma to a G code via the lemma_index
    4. Extract papyri citations from the collected entry text
    """
    # INTENT: Single-pass parse collecting entry blocks by Greek start-of-line;
    #   fragile against OCR noise but adequate for top-priority entries.
    entries = {}
    lines = text.split('\n')
    current_lemma = None
    current_block = []

    def flush():
        nonlocal current_lemma, current_block
        if not current_lemma or not current_block:
            return
        block_text = ' '.join(current_block).strip()
        # Map lemma to G code
        stripped = _strip_diacritics(current_lemma).lower().strip('.,;: ')
        code = lemma_index.get(stripped)
        if not code:
            # Try first word only
            first = stripped.split()[0] if stripped.split() else ''
            code = lemma_index.get(first)
        if code and code not in entries:
            papyri = extract_papyri_examples(block_text)
            if papyri:
                entries[code] = {
                    'entry_text': block_text[:600],
                    'papyri_examples': papyri,
                }
        current_lemma = None
        current_block = []

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue
        if GREEK_START_RE.match(stripped_line):
            flush()
            # Extract lemma: word chars at start up to first punctuation
            m = re.match(r'^([Ͱ-Ͽἀ-῿̀-ͯ]+)', stripped_line)
            if m:
                current_lemma = m.group(1)
                current_block = [stripped_line]
        elif current_lemma:
            current_block.append(stripped_line)

    flush()
    return entries


def main():
    os.makedirs(STRONGS, exist_ok=True)
    os.makedirs(CACHE_DIR, exist_ok=True)

    print('Fetching Moulton & Milligan (1930) from archive.org…')
    lemma_index = build_lemma_index()

    raw_text = None
    for archive_id in ARCHIVE_IDS:
        raw_text = fetch_archive_text(archive_id)
        if raw_text:
            break
        time.sleep(1)

    if not raw_text:
        print('\n  All archive.org IDs failed. Writing empty output file.')
        print('  To provide M&M data manually:')
        print('    1. Download the DjVu text from archive.org')
        print('    2. Save as scripts/_cache/mm_vocabularyofgree00mouluoft.txt')
        print('    3. Re-run this script')
        with open(OUT_PATH, 'w', encoding='utf-8') as f:
            json.dump({}, f)
        return

    print(f'\nParsing entries from {len(raw_text):,} chars…')
    entries = parse_entries_from_text(raw_text, lemma_index)
    print(f'  {len(entries):,} entries with papyri examples extracted')

    # Report coverage of priority codes
    covered = [c for c in PRIORITY_G_CODES if c in entries]
    print(f'  Priority codes covered: {len(covered)}/{len(set(PRIORITY_G_CODES))}')

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    kb = os.path.getsize(OUT_PATH) // 1024
    print(f'\n  Wrote {len(entries):,} entries  {kb} KB → {OUT_PATH}')
    print('Done. Run scripts/seed-glossary.py to inject extrabiblical_uses into phase bundles.')


if __name__ == '__main__':
    main()
