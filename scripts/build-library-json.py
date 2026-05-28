#!/usr/bin/env python3
"""
Reads every library HTML page and produces one JSON file per document:
  data/library/docs/{docId}.json

Each JSON contains a 'sections' array where each section is a navigable
unit the Reader can display: a confession chapter, catechism Q&A, etc.
Each section stores its inner HTML verbatim so .ref links survive and
bible.js can wire them up after injection.

Run from the repo root:  python3 scripts/build-library-json.py
"""

import json
import re
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise SystemExit('pip install beautifulsoup4')

REPO    = Path(__file__).resolve().parent.parent
LIB_DIR = REPO / 'library'
OUT_DIR = REPO / 'data' / 'library' / 'docs'
IDX_PATH = REPO / 'data' / 'library' / 'index.json'

DOCS = [
    ('apostles-creed',              'Apos', 200,  'creed'),
    ('nicene-creed',                'Nic',  381,  'creed'),
    ('athanasian-creed',            'Ath',  500,  'creed'),
    ('heidelberg-catechism',        'HC',   1563, 'catechism'),
    ('belgic-confession',           'Belg', 1561, 'confession'),
    ('canons-of-dort',              'CoD',  1619, 'canons'),
    ('westminster-confession',      'WCF',  1646, 'confession'),
    ('westminster-shorter-catechism','WSC', 1647, 'catechism'),
    ('westminster-larger-catechism', 'WLC', 1648, 'catechism'),
    ('london-baptist-confession',   'LBC',  1689, 'confession'),
    ('augsburg-confession',         'AC',   1530, 'confession'),
    ('39-articles',                 '39A',  1571, 'confession'),
    # Church Fathers (same lib-chapter extraction as confessions)
    ('ignatius',         'Ign',   108, 'father'),
    ('justin-martyr',    'JM',    165, 'father'),
    ('irenaeus',         'Iren',  202, 'father'),
    ('tertullian',       'Tert',  220, 'father'),
    ('athanasius',       'Atha',  373, 'father'),
    ('chrysostom',       'Chrys', 407, 'father'),
    ('augustine',        'Aug',   430, 'father'),
    ('gregory-nazianzus','GNaz',  390, 'father'),
]


def _clean_html(el):
    """Return the outer HTML of el as a string with lib-refs spans intact."""
    return str(el)


def _id_to_num(el_id):
    """Extract the numeric part of an id like 'ch3', 'q12', 'head2'."""
    m = re.search(r'(\d+)', el_id or '')
    return m.group(1) if m else None


def extract_creed(soup):
    creed_el = soup.find(class_='lib-creed')
    if not creed_el:
        main = soup.find('main') or soup.body or soup
        creed_el = main
    h1 = soup.find('h1')
    heading = h1.get_text(strip=True) if h1 else 'Creed'
    return [{'ref': '1', 'heading': heading, 'html': _clean_html(creed_el)}]


def extract_confession(soup):
    sections = []
    for chapter in soup.find_all(['div', 'section'], class_='lib-chapter'):
        ch_id  = chapter.get('id', '')
        ref    = _id_to_num(ch_id) or ch_id
        h2     = chapter.find(['h2'])
        heading = h2.get_text(strip=True) if h2 else ('Section ' + ref)
        sections.append({'ref': ref, 'heading': heading, 'html': _clean_html(chapter)})
    return sections


def extract_catechism(soup):
    sections = []
    for qa in soup.find_all('div', class_='lib-qa'):
        qa_id  = qa.get('id', '')
        ref    = _id_to_num(qa_id) or qa_id
        num_el = qa.find(class_='lib-qa__num') or qa.find(class_='lib-article__num')
        q_el   = qa.find(class_='lib-qa__q')
        q_text = q_el.get_text(strip=True) if q_el else ''
        heading = 'Q' + ref + ('. ' + q_text if q_text else '')
        sections.append({'ref': ref, 'heading': heading, 'html': _clean_html(qa)})
    return sections


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load existing index.json for title/year metadata
    meta_by_id = {}
    if IDX_PATH.exists():
        for entry in json.loads(IDX_PATH.read_text('utf-8')):
            meta_by_id[entry['id']] = entry

    for slug, abbrev, year, doc_type in DOCS:
        html_path = LIB_DIR / slug / 'index.html'
        if not html_path.exists():
            print(f'  skip {slug}: not found')
            continue

        html  = html_path.read_text(encoding='utf-8')
        soup  = BeautifulSoup(html, 'html.parser')

        h1    = soup.find('h1')
        title = h1.get_text(strip=True) if h1 else slug.replace('-', ' ').title()

        if doc_type == 'creed':
            sections = extract_creed(soup)
        elif doc_type in ('confession', 'canons', 'father'):
            sections = extract_confession(soup)
        else:
            sections = extract_catechism(soup)

        doc = {
            'id':            slug,
            'abbrev':        abbrev,
            'title':         title,
            'year':          year,
            'type':          doc_type,
            'totalSections': len(sections),
            'sections':      sections,
        }

        out_path = OUT_DIR / f'{slug}.json'
        out_path.write_text(
            json.dumps(doc, indent=2, ensure_ascii=False) + '\n',
            encoding='utf-8'
        )
        print(f'  {abbrev:6s}  {len(sections):4d} sections  →  data/library/docs/{slug}.json')


if __name__ == '__main__':
    main()
