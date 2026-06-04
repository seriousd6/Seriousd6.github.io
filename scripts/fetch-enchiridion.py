#!/usr/bin/env python3
"""
fetch-enchiridion.py
Fetch Augustine's Enchiridion from Wikisource (NPNF1 Vol. III) and write
BSW Library HTML v2 to data/library/html/augustine-enchiridion.html.

Source: Nicene and Post-Nicene Fathers: Series I/Volume III/Doctrinal
        Treatises of St. Augustin/The Enchiridion/Chapter N
        (chapters 1–122, plus index/intro page)

Sections:
  1. Introduction — What Is Wisdom?       (index + Ch 1–7)
  2. Faith: Creation, Sin, and the Fall   (Ch 8–33)
  3. Faith: The Incarnation and Redemption (Ch 34–55)
  4. Faith: The Spirit, Church, and Last Things (Ch 56–83)
  5. Hope: The Lord's Prayer              (Ch 84–116)
  6. Love: The Two Commandments           (Ch 117–122)
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

# ---------------------------------------------------------------------------
# Paths / constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.dirname(SCRIPT_DIR)
OUT_PATH   = os.path.join(REPO_ROOT, 'data', 'library', 'html',
                          'augustine-enchiridion.html')

WS_API   = 'https://en.wikisource.org/w/api.php'
HEADERS  = {'User-Agent': 'bible-study-library-builder/1.0 (dse.saved@gmail.com)'}
RATE     = 1.0   # seconds between requests

_NPNF_BASE = (
    'Nicene and Post-Nicene Fathers: Series I/Volume III/'
    'Doctrinal Treatises of St. Augustin/The Enchiridion'
)
_INDEX_PAGE  = _NPNF_BASE
_CHAPTER_FMT = _NPNF_BASE + '/Chapter {n}'

# Section boundaries: (heading, [page_titles])
SECTIONS = [
    (
        'Introduction — What Is Wisdom?',
        [_INDEX_PAGE] + [_CHAPTER_FMT.format(n=i) for i in range(1, 8)],
    ),
    (
        'Faith: Creation, Sin, and the Fall',
        [_CHAPTER_FMT.format(n=i) for i in range(8, 34)],
    ),
    (
        'Faith: The Incarnation and Redemption',
        [_CHAPTER_FMT.format(n=i) for i in range(34, 56)],
    ),
    (
        'Faith: The Spirit, Church, and Last Things',
        [_CHAPTER_FMT.format(n=i) for i in range(56, 84)],
    ),
    (
        'Hope: The Lord\'s Prayer',
        [_CHAPTER_FMT.format(n=i) for i in range(84, 117)],
    ),
    (
        'Love: The Two Commandments',
        [_CHAPTER_FMT.format(n=i) for i in range(117, 123)],
    ),
]

# ---------------------------------------------------------------------------
# MediaWiki chrome selectors to strip
# ---------------------------------------------------------------------------
_STRIP_SELECTORS = [
    '.mw-editsection',
    '#toc', '.toc',
    '.navbox', '.navbox-inner',
    '.reflist', '.references', '.mw-references-wrap',
    '.printfooter',
    '#catlinks',
    '.sister-project',
    '.noprint',
    'sup.reference', 'sup.cite_ref',
    '.mw-empty-elt',
    '.ws-noexport',
    '.ws-header', '.ws-footer', '.wst-header-structure', '.wst-header',
    '.wst-footer',
    '.wst-custom-rule',
    '.wst-gap',
    '.pagenum', '.ws-pagenum',
    '.wst-nop',
    'span.anchor',
    '.licenseContainer', '.mw-collapsible-box', '.mw-collapsible',
]

# ---------------------------------------------------------------------------
# HTML cleaning helpers
# ---------------------------------------------------------------------------

def _clean_soup(soup):
    """Strip MediaWiki chrome, images, inline styles from a parsed page."""
    for tag in soup.find_all(['style', 'link', 'meta']):
        tag.decompose()
    for img in soup.find_all('img'):
        img.decompose()
    for sel in _STRIP_SELECTORS:
        for el in soup.select(sel):
            el.decompose()
    # Remove empty paragraphs produced after stripping chrome
    for p in soup.find_all('p'):
        if not p.get_text(strip=True):
            p.decompose()
    return soup


def _replace_deprecated_tags(soup):
    """
    Replace <i> with <em> and <b> with <strong> throughout; also strip
    style="" attributes and empty <a id="..."> anchors per format rules.
    """
    # i → em
    for tag in soup.find_all('i'):
        tag.name = 'em'
    # b → strong
    for tag in soup.find_all('b'):
        tag.name = 'strong'
    # strip style attributes
    for tag in soup.find_all(style=True):
        del tag['style']
    # remove id= from headings (MediaWiki adds "Chapter_1" etc.)
    for tag in soup.find_all(re.compile(r'^h[1-6]$')):
        if 'id' in tag.attrs:
            del tag['id']
    # remove empty anchor targets  <a id="..."></a>  (W9 warning)
    for a in soup.find_all('a'):
        if not a.get('href') and a.get('id') and not a.get_text(strip=True):
            a.decompose()
    # unwrap mw-heading divs — extract the heading element, discard the div
    for div in soup.find_all('div', class_='mw-heading'):
        div.unwrap()
    return soup


def _remove_page_markers(soup):
    """Remove page-number markers and [Pg N] text patterns."""
    for cls in ('pagenum', 'pageno', 'pb', 'pgmark'):
        for span in soup.find_all(class_=cls):
            span.decompose()
    # Remove [Pg N] text patterns from text nodes
    for text_node in soup.find_all(string=True):
        cleaned = re.sub(r'\[Pg\s+\d+\]', '', str(text_node))
        if cleaned != str(text_node):
            text_node.replace_with(cleaned)
    return soup


def _extract_content_html(soup):
    """
    Return the inner HTML of the mw-parser-output div (or full soup if absent),
    after all cleaning passes.
    """
    content = soup.find(class_='mw-parser-output') or soup
    # Collect all top-level children, skip empty text nodes
    parts = []
    for child in content.children:
        if isinstance(child, NavigableString):
            if str(child).strip():
                parts.append(str(child))
        elif isinstance(child, Tag):
            parts.append(str(child))
    return '\n'.join(parts).strip()


# ---------------------------------------------------------------------------
# Wikisource fetch
# ---------------------------------------------------------------------------

def fetch_page(page_title):
    """
    Fetch a Wikisource page via the parse API.
    Returns cleaned HTML string, or None if the page is missing / empty.
    """
    params = {
        'action':             'parse',
        'page':               page_title,
        'prop':               'text',
        'disableeditsection': 'true',
        'disabletoc':         'true',
        'format':             'json',
        'formatversion':      '2',
    }
    try:
        resp = requests.get(WS_API, params=params, headers=HEADERS, timeout=45)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f'    [network error] {e}', file=sys.stderr)
        return None

    if 'error' in data:
        code = data['error'].get('code', '')
        if code == 'missingtitle':
            print(f'    [skip] missing: {page_title}')
            return None
        print(f'    [API error] {code}: {data["error"].get("info","")}', file=sys.stderr)
        return None

    raw_html = data['parse']['text']
    soup = BeautifulSoup(raw_html, 'html.parser')
    _clean_soup(soup)
    _replace_deprecated_tags(soup)
    _remove_page_markers(soup)
    return _extract_content_html(soup)


# ---------------------------------------------------------------------------
# Section assembly
# ---------------------------------------------------------------------------

def fetch_section(heading, page_titles):
    """
    Fetch multiple Wikisource pages and concatenate their content into one
    section, wrapping in <section data-heading="...">.
    Returns (section_html, word_count).
    """
    parts = []
    for i, title in enumerate(page_titles):
        print(f'  fetching [{i+1}/{len(page_titles)}]: {title.split("/")[-1]}')
        html = fetch_page(title)
        if html:
            parts.append(html)
        if i < len(page_titles) - 1:
            time.sleep(RATE)

    combined = '\n'.join(parts).strip()
    if not combined:
        print(f'  [warn] section "{heading}" yielded no content', file=sys.stderr)
        # Provide a minimal placeholder so the section is not hollow
        combined = f'<p>Content for this section could not be retrieved.</p>'

    # Wrap in section element with h2 heading
    safe_heading = heading.replace('"', '&quot;')
    h2 = f'<h2 class="lib-section__title">{heading}</h2>'
    section_html = (
        f'<section data-heading="{safe_heading}">\n'
        f'{h2}\n'
        f'{combined}\n'
        f'</section>'
    )

    # Count words for summary
    text = BeautifulSoup(combined, 'html.parser').get_text(' ', strip=True)
    word_count = len(text.split())
    return section_html, word_count


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print('fetch-enchiridion.py — Augustine, Enchiridion (NPNF1 Vol. III)')
    print(f'Output: {OUT_PATH}')
    print()

    all_sections = []
    total_words  = 0

    for sec_i, (heading, pages) in enumerate(SECTIONS, 1):
        print(f'\n=== Section {sec_i}/6: {heading} ({len(pages)} pages) ===')
        section_html, wc = fetch_section(heading, pages)
        all_sections.append(section_html)
        total_words += wc
        print(f'  section words: {wc:,}')

    # Write output
    output = '\n\n'.join(all_sections) + '\n'
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write(output)

    print('\n' + '=' * 60)
    print(f'Sections  : {len(all_sections)}')
    print(f'Total words: {total_words:,}')
    print(f'Written to : {OUT_PATH}')
    print()


if __name__ == '__main__':
    main()
