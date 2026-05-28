#!/usr/bin/env python3
"""
Reads every library HTML page and produces:
  data/library/index.json               — metadata list
  data/library/verse-index/{bookId}.json — verse → confessional citations

Run from the repo root:  python3 scripts/build-library-data.py

The verse-index powers the verse modal "Confessions" tab in bible.js.
"""

import json, re
from collections import defaultdict
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise SystemExit('pip install beautifulsoup4')

REPO     = Path(__file__).resolve().parent.parent
LIB_DIR  = REPO / 'library'
OUT_DIR  = REPO / 'data' / 'library'
IDX_PATH = OUT_DIR / 'index.json'

# ── Document metadata ────────────────────────────────────────────────────────

DOCS = [
    # id                            abbrev  year  type
    ('apostles-creed',             'Apos',  200,  'creed'),
    ('nicene-creed',               'Nic',   381,  'creed'),
    ('athanasian-creed',           'Ath',   500,  'creed'),
    ('heidelberg-catechism',       'HC',    1563, 'catechism'),
    ('belgic-confession',          'Belg',  1561, 'confession'),
    ('canons-of-dort',             'CoD',   1619, 'canons'),
    ('westminster-confession',     'WCF',   1646, 'confession'),
    ('westminster-shorter-catechism','WSC', 1647, 'catechism'),
    ('westminster-larger-catechism','WLC',  1648, 'catechism'),
    ('london-baptist-confession',  'LBC',   1689, 'confession'),
    ('augsburg-confession',        'AC',    1530, 'confession'),
    ('39-articles',                '39A',   1571, 'confession'),
]

# ── Ref normalisation ────────────────────────────────────────────────────────

BOOK_ID_MAP = {
    # OT
    'genesis':'genesis','gen':'genesis','gn':'genesis',
    'exodus':'exodus','ex':'exodus','exo':'exodus',
    'leviticus':'leviticus','lev':'leviticus',
    'numbers':'numbers','num':'numbers','nm':'numbers',
    'deuteronomy':'deuteronomy','deut':'deuteronomy','dt':'deuteronomy',
    'joshua':'joshua','josh':'joshua','jos':'joshua',
    'judges':'judges','judg':'judges','jdg':'judges',
    'ruth':'ruth',
    '1samuel':'1samuel','1sam':'1samuel','1 sam':'1samuel',
    '2samuel':'2samuel','2sam':'2samuel','2 sam':'2samuel',
    '1kings':'1kings','1kgs':'1kings','1 kgs':'1kings','1 kings':'1kings',
    '2kings':'2kings','2kgs':'2kings','2 kgs':'2kings','2 kings':'2kings',
    '1chronicles':'1chronicles','1chron':'1chronicles','1chr':'1chronicles','1 chron':'1chronicles',
    '2chronicles':'2chronicles','2chron':'2chronicles','2chr':'2chronicles','2 chron':'2chronicles',
    'ezra':'ezra',
    'nehemiah':'nehemiah','neh':'nehemiah',
    'esther':'esther','est':'esther',
    'job':'job',
    'psalm':'psalms','psalms':'psalms','psa':'psalms','ps':'psalms',
    'proverbs':'proverbs','prov':'proverbs','pr':'proverbs',
    'ecclesiastes':'ecclesiastes','eccl':'ecclesiastes','ecc':'ecclesiastes',
    'song of solomon':'songofsolomon','song':'songofsolomon','ss':'songofsolomon',
    'isaiah':'isaiah','isa':'isaiah',
    'jeremiah':'jeremiah','jer':'jeremiah',
    'lamentations':'lamentations','lam':'lamentations',
    'ezekiel':'ezekiel','ezek':'ezekiel','eze':'ezekiel',
    'daniel':'daniel','dan':'daniel',
    'hosea':'hosea','hos':'hosea',
    'joel':'joel',
    'amos':'amos',
    'obadiah':'obadiah','obad':'obadiah',
    'jonah':'jonah','jon':'jonah',
    'micah':'micah','mic':'micah',
    'nahum':'nahum','nah':'nahum',
    'habakkuk':'habakkuk','hab':'habakkuk',
    'zephaniah':'zephaniah','zeph':'zephaniah',
    'haggai':'haggai','hag':'haggai',
    'zechariah':'zechariah','zech':'zechariah',
    'malachi':'malachi','mal':'malachi',
    # NT
    'matthew':'matthew','matt':'matthew','mt':'matthew',
    'mark':'mark','mk':'mark',
    'luke':'luke','lk':'luke',
    'john':'john','jn':'john',
    'acts':'acts','ac':'acts',
    'romans':'romans','rom':'romans',
    '1corinthians':'1corinthians','1cor':'1corinthians','1 cor':'1corinthians',
    '2corinthians':'2corinthians','2cor':'2corinthians','2 cor':'2corinthians',
    'galatians':'galatians','gal':'galatians',
    'ephesians':'ephesians','eph':'ephesians',
    'philippians':'philippians','phil':'philippians',
    'colossians':'colossians','col':'colossians',
    '1thessalonians':'1thessalonians','1thess':'1thessalonians','1 thess':'1thessalonians',
    '2thessalonians':'2thessalonians','2thess':'2thessalonians','2 thess':'2thessalonians',
    '1timothy':'1timothy','1tim':'1timothy','1 tim':'1timothy',
    '2timothy':'2timothy','2tim':'2timothy','2 tim':'2timothy',
    'titus':'titus','tit':'titus',
    'philemon':'philemon','phlm':'philemon',
    'hebrews':'hebrews','heb':'hebrews',
    'james':'james','jas':'james',
    '1peter':'1peter','1pet':'1peter','1 pet':'1peter',
    '2peter':'2peter','2pet':'2peter','2 pet':'2peter',
    '1john':'1john','1jn':'1john','1 john':'1john',
    '2john':'2john','2jn':'2john','2 john':'2john',
    '3john':'3john','3jn':'3john','3 john':'3john',
    'jude':'jude',
    'revelation':'revelation','rev':'revelation',
}

_REF_RE = re.compile(
    r'^(?P<book>(?:\d\s*)?[A-Za-z\s]+?)'
    r'\s+(?P<ch>\d+)'
    r'(?::(?P<v>\d+)(?:-\d+)?)?'
    r'\b',
    re.IGNORECASE
)

def normalise_book(raw):
    """Return canonical bookId string or None."""
    clean = re.sub(r'\s+', ' ', raw.strip().lower())
    # Remove trailing dots (abbreviations)
    clean = clean.rstrip('.')
    # Normalise "1 cor" → "1corinthians" etc.
    clean_no_space = clean.replace(' ', '')
    if clean_no_space in BOOK_ID_MAP:
        return BOOK_ID_MAP[clean_no_space]
    if clean in BOOK_ID_MAP:
        return BOOK_ID_MAP[clean]
    return None

def parse_ref(data_ref_str):
    """
    Parse a data-ref attribute like "Romans 8:28", "1 Cor 10:31", "Ps 119:105-110"
    Returns (bookId, ch, v_start) or None.
    """
    s = data_ref_str.strip()
    m = _REF_RE.match(s)
    if not m:
        return None
    book_id = normalise_book(m.group('book'))
    if not book_id:
        return None
    ch  = m.group('ch')
    v   = m.group('v') or '1'
    return book_id, ch, v

def get_text_no_refs(el):
    """Get text of element with lib-refs spans removed."""
    soup = BeautifulSoup(str(el), 'html.parser')
    for span in soup.find_all('span', class_='lib-refs'):
        span.decompose()
    return soup.get_text(' ', strip=True)

def extract_refs(el):
    """Return list of data-ref values from all .ref links inside el."""
    return [a['data-ref'] for a in el.find_all('a', {'data-ref': True}) if a.get('data-ref')]

# ── Per-document section extraction ─────────────────────────────────────────

def extract_creed(soup, slug):
    """Creeds use a flat lib-creed div — treat as one section."""
    creed_el = soup.find(class_='lib-creed')
    if not creed_el:
        # Fallback: grab all data-ref from main
        main = soup.find('main') or soup
        proofs = extract_refs(main)
        text   = get_text_no_refs(main)
        return [{'section_ref': '1', 'text': text, 'proofs': proofs}]
    proofs = extract_refs(creed_el)
    text   = get_text_no_refs(creed_el)
    return [{'section_ref': '1', 'text': text, 'proofs': proofs}]

def extract_confession(soup, slug):
    """Returns list of {section_ref, text, proofs}."""
    sections = []
    # Support both <div class="lib-chapter"> and <section class="lib-chapter">
    for chapter in soup.find_all(['div', 'section'], class_='lib-chapter'):
        ch_id = chapter.get('id', '')
        ch_num = re.sub(r'\D', '', ch_id)

        # For confessions: lib-article items
        articles = chapter.find_all('div', class_='lib-article')
        if not articles:
            # Fallback: entire chapter is one section
            text   = get_text_no_refs(chapter)
            proofs = extract_refs(chapter)
            sections.append({'section_ref': ch_id, 'text': text, 'proofs': proofs})
            continue

        for art in articles:
            num_el = art.find(class_='lib-article__num')
            art_num = num_el.get_text(strip=True).rstrip('.') if num_el else ''
            text_el = art.find(class_='lib-article__text')
            if not text_el:
                text_el = art
            text   = get_text_no_refs(text_el)
            proofs = extract_refs(art)
            ref    = f'{ch_num}.{art_num}' if ch_num and art_num else ch_id
            sections.append({'section_ref': ref, 'text': text, 'proofs': proofs})
    return sections

def extract_catechism(soup, slug):
    """Returns list of {section_ref, q, a, proofs}."""
    sections = []
    for qa in soup.find_all('div', class_='lib-qa'):
        num_el = (qa.find(class_='lib-qa__num') or
                  qa.find(class_='lib-article__num') or
                  qa.find('span', class_='lib-qa__num'))
        q_el   = qa.find(class_='lib-qa__q') or qa.find('p', class_='lib-qa__q')
        a_el   = qa.find(class_='lib-qa__a') or qa.find('p', class_='lib-qa__a')
        num    = num_el.get_text(strip=True).lstrip('Q').rstrip('.') if num_el else ''
        q      = q_el.get_text(strip=True) if q_el else ''
        a      = get_text_no_refs(a_el) if a_el else ''
        proofs = extract_refs(qa)
        sections.append({'section_ref': num, 'q': q, 'a': a, 'proofs': proofs})
    return sections

# ── Build verse index ────────────────────────────────────────────────────────

def build_verse_index(all_sections):
    """
    all_sections: list of {abbrev, doc_slug, section_ref, text_or_qa, proofs}
    Returns: dict of bookId → {ch → {v → [citation, …]}}
    """
    by_book = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for sec in all_sections:
        for ref_str in sec.get('proofs', []):
            parsed = parse_ref(ref_str)
            if not parsed:
                continue
            book_id, ch, v = parsed
            # Human-readable citation label
            label  = sec.get('section_ref', '')
            abbrev = sec.get('abbrev', '')
            cite   = f'{abbrev} {label}' if abbrev and label else label
            entry  = {
                'doc':  abbrev,
                'slug': sec.get('doc_slug', ''),
                'ref':  cite,
                'text': (sec.get('text') or sec.get('a') or sec.get('q') or '')[:200]
            }
            by_book[book_id][ch][v].append(entry)
    return by_book

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / 'verse-index').mkdir(exist_ok=True)

    index_meta = []
    all_sections = []

    for slug, abbrev, year, doc_type in DOCS:
        html_path = LIB_DIR / slug / 'index.html'
        if not html_path.exists():
            print(f'  skip {slug}: file not found')
            continue

        html = html_path.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        # Title from <h1>
        h1 = soup.find('h1')
        title = h1.get_text(strip=True) if h1 else slug.replace('-', ' ').title()

        # Extract sections based on type
        if doc_type == 'creed':
            sections = extract_creed(soup, slug)
        elif doc_type in ('confession', 'canons'):
            sections = extract_confession(soup, slug)
        else:  # catechism
            sections = extract_catechism(soup, slug)

        for sec in sections:
            sec['abbrev']   = abbrev
            sec['doc_slug'] = slug
        all_sections.extend(sections)

        n_proofs = sum(len(s.get('proofs', [])) for s in sections)
        print(f'  {abbrev:6s} {len(sections):4d} sections  {n_proofs:5d} proof-text refs')

        index_meta.append({
            'id':     slug,
            'abbrev': abbrev,
            'title':  title,
            'year':   year,
            'type':   doc_type,
            'href':   f'library/{slug}/'
        })

    # Write index.json
    IDX_PATH.write_text(json.dumps(index_meta, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'\nWrote index.json ({len(index_meta)} docs)')

    # Build + write verse-index
    verse_idx = build_verse_index(all_sections)
    for book_id, chapters in sorted(verse_idx.items()):
        out = {ch: dict(verses) for ch, verses in chapters.items()}
        path = OUT_DIR / 'verse-index' / f'{book_id}.json'
        path.write_text(json.dumps(out, ensure_ascii=False) + '\n', encoding='utf-8')

    total_refs = sum(
        len(citations)
        for chapters in verse_idx.values()
        for verses in chapters.values()
        for citations in verses.values()
    )
    print(f'Wrote verse-index for {len(verse_idx)} books  ({total_refs} total citation entries)')


if __name__ == '__main__':
    main()
