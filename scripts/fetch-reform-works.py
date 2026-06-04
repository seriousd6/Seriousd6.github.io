#!/usr/bin/env python3
"""
fetch-reform-works.py — Convert EEBO-TCP Phase 1 XML to library HTML format.

Handles three Reformation-era works from EEBO-TCP (CC0 licensed):
  - Tyndale, Obedience of a Christian Man (1528) → TCP A14136
  - Cranmer, Defence of the True and Catholic Doctrine of the Sacrament (1550) → TCP A19571
  - Bullinger, Fifty Godly Sermons (Decades) (1577) → TCP A17183

Usage:
  python3 scripts/fetch-reform-works.py
  python3 scripts/fetch-reform-works.py --doc tyndale-obedience
  python3 scripts/fetch-reform-works.py --doc cranmer-defence
  python3 scripts/fetch-reform-works.py --doc bullinger-decades
"""

import argparse
import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
HTML_DIR    = os.path.join(REPO_ROOT, 'data', 'library', 'html')
INDEX_PATH  = os.path.join(REPO_ROOT, 'data', 'library', 'index.json')

HEADERS = {'User-Agent': 'bible-study-library-builder/1.0 (dse.saved@gmail.com)'}

EEBO_RAW  = 'https://raw.githubusercontent.com/textcreationpartnership/{tcpid}/master/{tcpid}.xml'
IA_STREAM = 'https://archive.org/stream/{ia_id}/{ia_id}_djvu.txt'


# ---------------------------------------------------------------------------
# EEBO-TCP fetch
# ---------------------------------------------------------------------------

def fetch_eebo(tcp_id):
    """Fetch and parse a TEI XML file from EEBO-TCP Phase 1 GitHub repos."""
    url = EEBO_RAW.format(tcpid=tcp_id)
    print(f'  Fetching {url}', file=sys.stderr)
    resp = requests.get(url, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, 'lxml-xml')


# ---------------------------------------------------------------------------
# Archive.org OCR fetch
# ---------------------------------------------------------------------------

def fetch_ia_text(ia_id):
    """Fetch OCR plain text from an archive.org djvu.txt via the stream viewer."""
    url = IA_STREAM.format(ia_id=ia_id)
    print(f'  Fetching {url}', file=sys.stderr)
    resp = requests.get(url, headers={**HEADERS, 'User-Agent': 'Mozilla/5.0'}, timeout=120)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    pre = soup.find('pre')
    if not pre:
        raise ValueError(f'No <pre> tag found in archive.org stream for {ia_id}')
    text = pre.get_text()
    # Normalise double-spaces from djvu OCR
    text = re.sub(r'  +', ' ', text)
    return text


# ---------------------------------------------------------------------------
# TEI → HTML conversion helpers
# ---------------------------------------------------------------------------

_LONG_S = str.maketrans({'ſ': 's'})
_SOFTYHYPHEN = '­'

# Characters to remove: pilcrow (section marker), section sign
_PILCROW_RE = re.compile(r'^[¶§]\s*')


def normalize_ws(text):
    """Collapse whitespace; handle long-s, soft-hyphen, and print artifacts."""
    text = text.translate(_LONG_S).replace(_SOFTYHYPHEN, '')
    # Remove EOL hyphen markers (already handled by get_text but keep for safety)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def clean_heading(text):
    """Strip leading pilcrow/section signs from section headings."""
    text = normalize_ws(text)
    text = _PILCROW_RE.sub('', text)
    return text


def esc(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def tei_element_to_html(el, depth=0):
    """
    Recursively convert a TEI BeautifulSoup element to an HTML string.
    Depth controls whether sub-headings use h3 or h4.
    """
    parts = []
    for child in el.children:
        if isinstance(child, NavigableString):
            # Inline text fragments inside structural elements — skip
            continue
        if not isinstance(child, Tag):
            continue
        name = child.name
        if name in ('head',):
            # Already handled by caller
            continue
        if name in ('milestone', 'pb', 'fw', 'note'):
            # Page breaks, running headers, marginal notes — skip
            continue
        if name == 'p':
            text = normalize_ws(child.get_text())
            if text:
                parts.append(f'<p>{esc(text)}</p>')
        elif name in ('l',):
            # verse line
            text = normalize_ws(child.get_text())
            if text:
                parts.append(f'<p>{esc(text)}</p>')
        elif name in ('lg',):
            # verse group — treat like a block
            parts.extend(tei_element_to_html(child, depth))
        elif name == 'div':
            inner_head = child.find('head', recursive=False)
            if inner_head:
                htag = 'h3' if depth == 0 else 'h4'
                headtext = clean_heading(inner_head.get_text())
                parts.append(f'<{htag}>{esc(headtext)}</{htag}>')
            parts.extend(tei_element_to_html(child, depth + 1))
        elif name == 'list':
            items = child.find_all('item', recursive=False)
            if items:
                parts.append('<ul>')
                for it in items:
                    parts.append(f'<li>{esc(normalize_ws(it.get_text()))}</li>')
                parts.append('</ul>')
        elif name == 'q':
            text = normalize_ws(child.get_text())
            if text:
                parts.append(f'<blockquote class="scripture"><p>{esc(text)}</p></blockquote>')
        elif name in ('trailer', 'closer', 'salute', 'signed', 'dateline'):
            text = normalize_ws(child.get_text())
            if text:
                parts.append(f'<p><em>{esc(text)}</em></p>')
        else:
            # Unknown element — recurse for content
            parts.extend(tei_element_to_html(child, depth))
    return parts


def build_section_html(heading, content_parts):
    """Wrap content in the standard library section format."""
    inner = '\n'.join(content_parts)
    return (
        f'<section data-heading="{esc(heading)}">'
        f'<h2 class="lib-section__title">{esc(heading)}</h2>\n'
        f'{inner}\n'
        f'</section>'
    )


# ---------------------------------------------------------------------------
# Tyndale — Obedience of a Christian Man (A14136)
# ---------------------------------------------------------------------------

TYNDALE_SECTION_MAP = {
    'to_the_reader': 'Preface to the Reader',
    'prologue': 'The Prologue unto the Book',
}

TYNDALE_PART_HEADINGS = [
    'The Obedience of Children unto Their Elders',
    'The Obedience of Wives unto Their Husbands',
    'The Obedience of Servants unto Their Masters',
    'The Obedience of Subjects unto Kings and Rulers',
    'Against the Pope\'s False Power',
    'Of the Signs and Sacraments',
    'The Coming of Antichrist',
    'Of Prayer and Good Deeds',
    'On the Fourfold Sense of Scripture',
    'On the Obedience Described',
]


def build_tyndale(soup):
    """Extract sections from Tyndale's Obedience of a Christian Man.

    TEI structure:
      <front>  — title_page, to_the_reader, prologue
      <body>   — 14 part divs (the main treatise)
      <back>   — table_of_contents, errata, colophon (skipped)
    """
    text_el = soup.find('text')
    if not text_el:
        raise ValueError('No <text> element found')

    sections = []

    # --- Front matter (to_the_reader + prologue) ---
    front = text_el.find('front')
    if front:
        for div in front.find_all('div', recursive=False):
            dtype = div.get('type', '')
            if dtype == 'title_page':
                continue
            head = div.find('head', recursive=False)
            if head:
                heading = clean_heading(head.get_text())
            elif dtype in TYNDALE_SECTION_MAP:
                heading = TYNDALE_SECTION_MAP[dtype]
            else:
                continue
            content = tei_element_to_html(div)
            if content:
                sections.append(build_section_html(heading, content))

    # --- Body (main treatise parts) ---
    body = text_el.find('body')
    if not body:
        raise ValueError('No <body> element found')

    for div in body.find_all('div', recursive=False):
        dtype = div.get('type', '')
        head = div.find('head', recursive=False)
        if head:
            heading = clean_heading(head.get_text())
        elif dtype in TYNDALE_SECTION_MAP:
            heading = TYNDALE_SECTION_MAP[dtype]
        else:
            heading = dtype.replace('_', ' ').title() or 'Section'

        content = tei_element_to_html(div)
        if content:
            sections.append(build_section_html(heading, content))

    return sections


# ---------------------------------------------------------------------------
# Cranmer — Defence of the True and Catholic Doctrine of the Sacrament (A19571)
# ---------------------------------------------------------------------------

CRANMER_BOOK_HEADINGS = {
    '1': 'Book I — Of the True and Catholic Doctrine and Use of the Sacrament',
    '2': 'Book II — Against the Error of Transubstantiation',
    '3': 'Book III — The Manner How Christ is Present in His Supper',
    '4': 'Book IV — Of the Eating and Drinking of the Body and Blood of Christ',
    '5': 'Book V — Of the Oblation and Sacrifice of Our Saviour Christ',
}


def build_cranmer(soup):
    """Extract sections from Cranmer's Defence of the Sacrament.

    TEI structure: books numbered 1–5 as div type=book n=1..5.
    """
    text_el = soup.find('text') or soup
    body = text_el.find('body')
    if not body:
        raise ValueError('No body element found')

    sections = []
    for div in body.find_all('div', recursive=False):
        dtype = div.get('type', '')
        n = div.get('n', '')

        if dtype == 'book':
            heading = CRANMER_BOOK_HEADINGS.get(n, f'Book {n}')
        else:
            head = div.find('head', recursive=False)
            heading = clean_heading(head.get_text()) if head else dtype.title()

        content = tei_element_to_html(div)
        if content:
            sections.append(build_section_html(heading, content))

    return sections


# ---------------------------------------------------------------------------
# Bullinger — Fifty Godly Sermons (Decades) (A17183)
# ---------------------------------------------------------------------------

# Limit to the first two Decades (20 sermons) to keep the file manageable.
# The full 50-sermon text is 6MB of XML.
BULLINGER_MAX_DECADES = 2


_DECADE_ORDINALS = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
}

def build_bullinger(soup):
    """Extract sections from Bullinger's Decades (first two decades).

    TEI structure:
      body > div type=sermons > div (decade) > div (sermon)
    Each sermon becomes one library section.
    """
    text_el = soup.find('text') or soup
    body = text_el.find('body')
    if not body:
        raise ValueError('No body element found')

    sermons_div = body.find('div', type='sermons') or body
    sections = []

    decade_count = 0
    for decade in sermons_div.find_all('div', recursive=False):
        decade_head = decade.find('head', recursive=False)
        if not decade_head:
            continue

        decade_count += 1
        if decade_count > BULLINGER_MAX_DECADES:
            break

        decade_roman = _DECADE_ORDINALS.get(decade_count, str(decade_count))
        sermon_num = 0

        for sermon in decade.find_all('div', recursive=False):
            s_head = sermon.find('head', recursive=False)
            if not s_head:
                continue
            sermon_num += 1
            s_heading_raw = clean_heading(s_head.get_text())
            full_heading = f'Decade {decade_roman}, Sermon {sermon_num} — {s_heading_raw}'
            content = tei_element_to_html(sermon)
            if content:
                sections.append(build_section_html(full_heading, content))

    return sections


# ---------------------------------------------------------------------------
# Zwingli — Commentary on True and False Religion (IA latinworkscorres03zwin)
# 1929 Heidelberg Press edition (public domain since 2025)
# Translated by Henry Preble, revised by Clarence Nevin Heller
# ---------------------------------------------------------------------------

# (char positions in the fetched cleaned text; verified against the djvu.txt)
_ZWINGLI_SECTIONS = [
    ('Dedication to King Francis I',
     'To the most Christian King of France',
     'The Word Religion\n'),

    ('I–II — The Word Religion and Between Whom Religion Subsists',
     'The Word Religion\n',
     '[6]. The Christian Religion'),

    ('III–VI — God, Man, Religion, and the Christian Faith',
     '[6]. The Christian Religion',
     'Repentance'),

    ('VII–XI — Repentance, the Law, Sin, and the Holy Ghost',
     'Repentance',
     '[12]. The Keys'),

    ('XII–XIV — The Keys and the Church',
     '[12]. The Keys',
     '[18]. The Eucharist'),

    ('XV–XVII — The Sacraments and Baptism',
     # The Sacraments section intro appears before the Eucharist chapter
     # We split into sub-sections by using the Eucharist start as boundary
     None,   # placeholder; handled specially
     None),

    ('XVIII — The Eucharist',
     '[18]. The Eucharist',
     'Purgatory\n'),

    ('XIX–XXVI — Confession, Vows, Invocation, Merits, and Purgatory',
     'Purgatory\n',
     '[29], Statues and Images'),

    ('XXVII–XXIX — Magisterial Office, Offence, and Statues and Images',
     '[29], Statues and Images',
     'REPLY TO EMSER'),

    ('Reply to Emser (Antibolon, 1524)',
     'REPLY TO EMSER',
     None),
]

# Simplified section layout (without the placeholder entry)
# Section cuts: (heading, start_marker, end_marker)
# start_marker is searched in the full text; end_marker delimits the section end.
_ZWINGLI_CUTS = [
    ('Dedication to King Francis I',
     'To the most Christian King of France',
     '[2]. Between Whom Religion Subsists'),

    ('I–V: The Word Religion, God, Man, and Religion',
     '[2]. Between Whom Religion Subsists',
     '[6]. The Christian Religion'),

    ('VI–VII: The Christian Religion and the Gospel',
     '[6]. The Christian Religion',
     '[8]. Repentance'),

    ('VIII–XI: Repentance, the Law, Sin, and the Holy Ghost',
     '[8]. Repentance',
     '[12]. The Keys'),

    ('XII–XVII: The Keys, the Church, the Sacraments, and Baptism',
     '[12]. The Keys',
     '[18]. The Eucharist'),

    ('XVIII: The Eucharist',
     '[18]. The Eucharist',
     'serve for reward.'),

    ('XIX–XXVI: Confession, Vows, Invocation, Merits, Prayer, and Purgatory',
     'Holy Scripture knows nothing of the fire of purgatory',
     '[29], Statues and Images'),

    ('XXVII–XXIX: Magisterial Office, Offence, and Statues and Images',
     '[29], Statues and Images',
     'REPLY TO EMSER'),

    ('Reply to Emser (Antibolon, 1524)',
     'REPLY TO EMSER',
     None),
]


def _ia_text_to_paras(raw_block):
    """Convert a raw OCR text block to a list of <p> HTML strings.

    Heuristics:
    - A blank line (or a line that is purely a page number/running header)
      signals a paragraph break.
    - Lines that are ONLY page numbers (e.g. '56', '57') are dropped.
    - Running headers like 'The Works of Huldreich Zwingli' and 'On True and
      False Religion' are dropped.
    - Chapter sub-headings (short lines in sentence case) become <h3>.
    """
    _DROP = re.compile(
        r'^(\d+|'
        r'The Works of Huldreich Zwingli|'
        r'On True and False Religion|'
        r'Huldreich Zwingli\'s|'
        r'Reply to Emser|'
        r'^\*.*|'  # footnote markers
        r'DATE DUE.*|'
        r'JA.*|JAM.*'
        r')$', re.IGNORECASE)

    lines = raw_block.split('\n')
    paragraphs = []
    current = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current:
                paragraphs.append(' '.join(current))
                current = []
            continue
        if _DROP.match(stripped):
            continue
        current.append(stripped)

    if current:
        paragraphs.append(' '.join(current))

    result = []
    for para in paragraphs:
        if not para.strip():
            continue
        text = para.strip()
        # Short paragraph (< 100 chars) may be a sub-heading
        if len(text) < 80 and not text.endswith('.') and not text[0].isdigit():
            result.append(f'<h3>{esc(text)}</h3>')
        else:
            result.append(f'<p>{esc(text)}</p>')
    return result


def build_zwingli(text):
    """Split the Zwingli Commentary OCR text into library sections.

    text — the cleaned djvu.txt content from the archive.org stream viewer.
    Source: latinworkscorres03zwin (1929 Heidelberg Press, public domain 2025).
    Sections span from Zwingli's Dedication through the Reply to Emser.
    """
    # Start at the Dedication to Francis I (Zwingli's own text begins here)
    ded_marker = 'To the most Christian King of France'
    ded_idx = text.find(ded_marker)
    if ded_idx < 0:
        raise ValueError('Could not locate Dedication in text')

    # End before the library due-date stamp (OCR artifact at end of scan)
    end_marker = 'DATE DUE'
    end_idx = text.lower().find(end_marker.lower(), ded_idx)
    if end_idx < 0:
        end_idx = len(text)

    body = text[ded_idx:end_idx]

    sections = []
    for heading, start_marker, end_marker in _ZWINGLI_CUTS:
        if start_marker is None:
            continue

        # Find start within the body
        s_idx = body.lower().find(start_marker.lower())
        if s_idx < 0:
            print(f'  WARNING: section "{heading}" — start not found, skipping',
                  file=sys.stderr)
            continue

        # Find end
        if end_marker:
            e_idx = body.lower().find(end_marker.lower(), s_idx + len(start_marker))
            if e_idx < 0:
                e_idx = len(body)
        else:
            e_idx = len(body)

        block = body[s_idx:e_idx]
        paras = _ia_text_to_paras(block)
        if paras:
            sections.append(build_section_html(heading, paras))

    return sections


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

MANIFEST = [
    {
        'id': 'zwingli-true-false-religion',
        'ia_id': 'latinworkscorres03zwin',   # archive.org identifier; 1929 Heidelberg Press (PD 2025)
        'build': build_zwingli,
        'index_meta': {
            'abbrev': 'ZwinRel',
            'title': 'Commentary on True and False Religion',
            'year': 1525,
            'type': 'father',
            'tradition': 'reformed',
            'era': 'reformation',
            'author': 'Ulrich Zwingli',
            'desc': (
                'Zwingli\'s most comprehensive theological work — 29 chapters covering '
                'the whole of Christian doctrine from God and man through the sacraments, '
                'the eucharist, purgatory, and images. The pioneering Protestant systematic '
                'theology (March 1525). English translation by Henry Preble (1929).'
            ),
        },
    },
    {
        'id': 'tyndale-obedience',
        'tcp_id': 'A14136',
        'build': build_tyndale,
        'index_meta': {
            'abbrev': 'TynOb',
            'title': 'The Obedience of a Christian Man',
            'year': 1528,
            'type': 'father',
            'tradition': 'anglican',
            'era': 'reformation',
            'author': 'William Tyndale',
            'desc': (
                '"What thou canst not overcome with scripture and with open reason, that shalt '
                'thou overcome with art." Tyndale\'s foundational manifesto on biblical '
                'authority, the duty of Christian rulers, and the right of all to read '
                'Scripture — foundational for the English Reformation.'
            ),
        },
    },
    {
        'id': 'cranmer-defence',
        'tcp_id': 'A19571',
        'build': build_cranmer,
        'index_meta': {
            'abbrev': 'CranDef',
            'title': 'A Defence of the True and Catholic Doctrine of the Sacrament',
            'year': 1550,
            'type': 'father',
            'tradition': 'anglican',
            'era': 'reformation',
            'author': 'Thomas Cranmer',
            'desc': (
                'Cranmer\'s five-book defence of Reformed eucharistic doctrine against '
                'transubstantiation — defining the Anglican via media between Rome and Zwingli; '
                'written under Edward VI, the foundational Anglican statement on the Lord\'s Supper.'
            ),
        },
    },
    {
        'id': 'bullinger-decades',
        'tcp_id': 'A17183',
        'build': build_bullinger,
        'index_meta': {
            'abbrev': 'BullDec',
            'title': 'Decades (Selections: Decades I–II)',
            'year': 1549,
            'type': 'sermon',
            'tradition': 'reformed',
            'era': 'reformation',
            'author': 'Heinrich Bullinger',
            'desc': (
                'The first twenty of Bullinger\'s fifty doctrinal sermons covering the whole of '
                'Christian doctrine — the theological standard for the English church under '
                'Edward VI and Elizabeth I, and one of the most influential Reformed works of '
                'the 16th century.'
            ),
        },
    },
]


# ---------------------------------------------------------------------------
# Index patch
# ---------------------------------------------------------------------------

def patch_index(meta):
    """Add or update entry in data/library/index.json."""
    import json
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index = json.load(f)

    doc_id = meta['id']
    html_url = f"{doc_id}.html"

    # Build entry from index_meta + standard fields
    entry = {'id': doc_id, 'html_url': html_url}
    entry.update(meta['index_meta'])

    # Remove existing entry if present
    index = [e for e in index if e.get('id') != doc_id]
    index.append(entry)

    # Sort by year then title
    index.sort(key=lambda e: (e.get('year', 0), e.get('title', '')))

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f'  Updated index.json with {doc_id}')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process(entry):
    doc_id = entry['id']
    out_path = os.path.join(HTML_DIR, f'{doc_id}.html')

    if 'ia_id' in entry:
        # Archive.org OCR source
        print(f'\n=== {doc_id} (IA {entry["ia_id"]}) ===')
        text = fetch_ia_text(entry['ia_id'])
        time.sleep(1)
        sections = entry['build'](text)
    else:
        # EEBO-TCP TEI XML source
        print(f'\n=== {doc_id} (TCP {entry["tcp_id"]}) ===')
        soup = fetch_eebo(entry['tcp_id'])
        time.sleep(1)
        sections = entry['build'](soup)

    print(f'  Built {len(sections)} sections')

    if not sections:
        print(f'  WARNING: No sections generated for {doc_id}')
        return

    html = '\n'.join(sections) + '\n'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Wrote {out_path} ({len(html):,} bytes)')

    patch_index(entry)


def main():
    parser = argparse.ArgumentParser(description='Fetch Reformation-era works from EEBO-TCP')
    parser.add_argument('--doc', help='Specific doc id to process')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    manifest = MANIFEST
    if args.doc:
        manifest = [e for e in MANIFEST if e['id'] == args.doc]
        if not manifest:
            print(f'Unknown doc: {args.doc}. Available: {[e["id"] for e in MANIFEST]}')
            sys.exit(1)

    for entry in manifest:
        if args.dry_run:
            print(f'Would process: {entry["id"]} (TCP {entry["tcp_id"]})')
        else:
            process(entry)

    print('\nDone.')


if __name__ == '__main__':
    main()
