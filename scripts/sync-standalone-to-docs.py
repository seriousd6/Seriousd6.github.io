#!/usr/bin/env python3
"""
sync-standalone-to-docs.py

Parses the existing standalone library/ID/index.html pages and writes
improved data/library/docs/ID.json files. Uses what we already have.
"""

import json, os, re, sys
from bs4 import BeautifulSoup, NavigableString

REPO    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB_DIR = os.path.join(REPO, 'library')
DOCS_DIR = os.path.join(REPO, 'data', 'library', 'docs')


def read_page(slug):
    path = os.path.join(LIB_DIR, slug, 'index.html')
    if not os.path.exists(path):
        return None
    with open(path, encoding='utf-8') as f:
        return BeautifulSoup(f.read(), 'html.parser')


def read_doc(slug):
    path = os.path.join(DOCS_DIR, slug + '.json')
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def write_doc(slug, data):
    path = os.path.join(DOCS_DIR, slug + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    words = sum(len(re.sub(r'<[^>]+>', '', s.get('html', '')).split())
                for s in data.get('sections', []))
    print(f'  wrote {slug}.json  {len(data["sections"])} sections  {words} words')


def inner_html(tag):
    return ''.join(str(c) for c in tag.children)


# ---------------------------------------------------------------------------
# Parser A: lib-chapter / lib-article pattern (Augsburg, Belgic, WCF, etc.)
# ---------------------------------------------------------------------------

def parse_lib_chapters(soup, one_section_per_chapter=True):
    """
    Each lib-chapter div → one section.
    heading = the h2/h3 inside the div.
    html    = everything inside the div (preserving lib-article markup).
    """
    sections = []
    for ch in soup.find_all(class_='lib-chapter'):
        h = ch.find(['h2', 'h3', 'h4'])
        heading = h.get_text(strip=True) if h else ''
        html = inner_html(ch)
        sections.append({'ref': ch.get('id', str(len(sections) + 1)),
                         'heading': heading,
                         'html': html})
    return sections


# ---------------------------------------------------------------------------
# Parser B: lib-lords-day / lib-qa pattern (Heidelberg Catechism)
# ---------------------------------------------------------------------------

def parse_heidelberg(soup):
    sections = []
    # lib-lords-day and lib-qa are siblings inside div.container
    container = soup.find(class_='lib-qa-container') \
                or soup.find(class_='container') \
                or soup.find('main')
    if not container:
        return sections

    current_heading = ''
    current_html = []

    def flush():
        if current_html:
            sections.append({
                'ref': '',
                'heading': current_heading,
                'html': '\n'.join(current_html),
            })

    # Walk all descendants at any depth, collecting lib-lords-day / lib-qa
    for el in container.find_all(class_=['lib-lords-day', 'lib-qa']):
        classes = el.get('class', [])
        if 'lib-lords-day' in classes:
            flush()
            current_heading = el.get_text(strip=True)
            current_html = []
        elif 'lib-qa' in classes:
            current_html.append(str(el))

    flush()
    return sections


# ---------------------------------------------------------------------------
# Parser C: Westminster Shorter/Larger Catechism (lib-qa pattern)
# ---------------------------------------------------------------------------

def parse_westminster_catechism(soup):
    sections = []
    for qa in soup.find_all(class_='lib-qa'):
        q_el = qa.find(class_='lib-qa__q')
        heading = 'Q. ' + q_el.get_text(strip=True) if q_el else ''
        sections.append({'ref': '', 'heading': heading, 'html': str(qa)})
    return sections


# ---------------------------------------------------------------------------
# Per-document extraction
# ---------------------------------------------------------------------------

def sync_augsburg(slug='augsburg-confession'):
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)
    secs = parse_lib_chapters(soup)
    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


def sync_belgic(slug='belgic-confession'):
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)
    secs = parse_lib_chapters(soup)
    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


def sync_canons_of_dort(slug='canons-of-dort'):
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)
    secs = parse_lib_chapters(soup)
    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


def sync_westminster_confession(slug='westminster-confession'):
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)
    secs = parse_lib_chapters(soup)
    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


def sync_westminster_catechism(slug, qa_class='lib-qa'):
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)
    secs = parse_westminster_catechism(soup)
    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


def sync_heidelberg():
    slug = 'heidelberg-catechism'
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)
    secs = parse_heidelberg(soup)
    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


def sync_39_articles():
    slug = '39-articles'
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)
    secs = parse_lib_chapters(soup)
    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


def sync_london_baptist():
    slug = 'london-baptist-confession'
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)
    secs = parse_lib_chapters(soup)
    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


def sync_simple(slug, creed_class='lib-creed-text'):
    """For creed pages (Apostles, Nicene, Athanasian)."""
    soup = read_page(slug)
    if not soup:
        print(f'  SKIP {slug}: no standalone page'); return
    existing = read_doc(slug)

    # Try lib-chapter first, then fallback to main content
    chapters = soup.find_all(class_='lib-chapter')
    if chapters:
        secs = parse_lib_chapters(soup)
    else:
        # Single-section: grab everything inside <main>
        main = soup.find('main')
        if not main:
            print(f'  SKIP {slug}: no main element'); return
        # Strip nav / header cruft
        for el in main.find_all(class_=['lib-back', 'site-footer', 'lib-meta']):
            el.decompose()
        secs = [{'ref': '1', 'heading': '', 'html': inner_html(main)}]

    data = {**existing, 'sections': secs, 'totalSections': len(secs)}
    write_doc(slug, data)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print('Syncing standalone pages → docs JSON...\n')

    # Confessions with lib-chapter structure
    sync_augsburg()
    sync_belgic()
    sync_canons_of_dort()
    sync_westminster_confession()
    sync_westminster_catechism('westminster-shorter-catechism')
    sync_westminster_catechism('westminster-larger-catechism')
    sync_heidelberg()
    sync_39_articles()
    sync_london_baptist()

    # Creeds (single section or simple h2 structure)
    sync_simple('apostles-creed')
    sync_simple('nicene-creed')
    sync_simple('athanasian-creed')

    # Councils (newly created standalone pages with lib-chapter structure)
    for slug in ['nicaea-i', 'constantinople-i', 'ephesus-431', 'chalcedon-451', 'orange-529']:
        soup = read_page(slug)
        if not soup:
            print(f'  SKIP {slug}: no standalone page'); continue
        existing = read_doc(slug)
        secs = parse_lib_chapters(soup)
        data = {**existing, 'sections': secs, 'totalSections': len(secs)}
        write_doc(slug, data)

    # Reformation confessions with lib-chapter structure (when created)
    for slug in ['leo-tome', 'smalcald-articles', 'schleitheim-confession',
                 'savoy-declaration', 'dordrecht-confession']:
        soup = read_page(slug)
        if not soup:
            print(f'  SKIP {slug}: no standalone page yet'); continue
        existing = read_doc(slug)
        secs = parse_lib_chapters(soup)
        data = {**existing, 'sections': secs, 'totalSections': len(secs)}
        write_doc(slug, data)

    print('\nDone.')
