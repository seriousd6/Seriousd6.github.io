#!/usr/bin/env python3
"""
fetch-julian.py — Fetch Revelations of Divine Love (Warrack translation, Long Text)
from Wikisource and write BSW Library HTML v2 to data/library/html/julian-revelations.html

Source: https://en.wikisource.org/wiki/Revelations_of_Divine_Love
Chapters 1–86, grouped into 13 thematic sections matching Julian's own numbering.
"""

import json
import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
HTML_DIR    = os.path.join(REPO_ROOT, 'data', 'library', 'html')
INDEX_PATH  = os.path.join(REPO_ROOT, 'data', 'library', 'index.json')
OUT_PATH    = os.path.join(HTML_DIR, 'julian-revelations.html')

WS_API   = 'https://en.wikisource.org/w/api.php'
HEADERS  = {'User-Agent': 'bible-study-library-builder/1.0 (dse.saved@gmail.com)'}
RATE_DELAY = 1.0  # seconds between API requests

# ---------------------------------------------------------------------------
# Section plan — 13 sections covering all 86 chapters
# Each entry: (heading, [chapter numbers])
# ---------------------------------------------------------------------------
SECTIONS = [
    (
        'Introduction — Prologue',
        list(range(1, 2)),       # Ch 1: "A revelation of love which Jesus Christ…"
    ),
    (
        'The First Revelation — The Crowned Head',
        list(range(2, 10)),      # Chs 2–9
    ),
    (
        'The Second Revelation — The Discolouring of His Face',
        list(range(10, 11)),     # Ch 10
    ),
    (
        'The Third Revelation — God in a Point',
        list(range(11, 12)),     # Ch 11
    ),
    (
        'The Fourth Revelation — The Plenteous Bleeding',
        list(range(12, 13)),     # Ch 12
    ),
    (
        'The Fifth Revelation — The Fiend Overcome',
        list(range(13, 14)),     # Ch 13
    ),
    (
        'The Sixth Revelation — The High, Marvellous Thanks',
        list(range(14, 15)),     # Ch 14
    ),
    (
        'The Seventh Revelation — The Contraries',
        list(range(15, 16)),     # Ch 15
    ),
    (
        'The Eighth Revelation — The Passion',
        list(range(16, 22)),     # Chs 16–21
    ),
    (
        'The Ninth through Twelfth Revelations',
        list(range(22, 27)),     # Chs 22–26
    ),
    (
        'The Thirteenth Revelation — Sin and the Long-Suffering of God',
        list(range(27, 41)),     # Chs 27–40
    ),
    (
        'The Fourteenth Revelation — Prayer and the Motherhood of God',
        list(range(41, 64)),     # Chs 41–63
    ),
    (
        'The Fifteenth and Sixteenth Revelations — Rest and the Final Showing',
        list(range(64, 87)),     # Chs 64–86
    ),
]

# ---------------------------------------------------------------------------
# HTML cleaning — adapted from fetch-library-docs.py
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
    '.ws-header', '.ws-footer', '.wst-header-structure', '.wst-header', '.wst-footer',
    '.wst-custom-rule',
    '.wst-gap',
    '.pagenum', '.ws-pagenum',
    '.wst-nop',
    'span.anchor',
    '.licenseContainer', '.mw-collapsible-box', '.mw-collapsible',
    # Decorative drop-cap wrappers — unwrapped below to preserve the letter
    # (removing the span avoids W-CHROME warnings; text content is preserved)
]

# Drop-cap class names that wrap the first letter of each chapter decoratively.
# These have no BSW CSS support, so we unwrap them (preserving the letter text).
_DROPINITIAL_CLASSES = {'dropinitial', 'dropinitial-mid', 'dropinitial-initial',
                         'drop-initial-no-image'}


def _is_footnote_div(div):
    """True if a prp-pages-output div contains only footnotes/references."""
    text = div.get_text(strip=True)
    if not text:
        return True
    # Footnote divs start with an arrow (↑), dagger (†), or contain zero-width space + arrow
    cleaned = text.lstrip('​').strip()
    if cleaned.startswith('↑') or cleaned.startswith('†'):
        return True
    paras = div.find_all('p')
    text_paras = [p for p in paras if len(p.get_text(strip=True)) > 30]
    return len(text_paras) == 0


def _clean_soup(soup):
    """Remove MediaWiki chrome, styles, images, and empty elements."""
    for tag in soup.find_all(['style', 'link', 'meta']):
        tag.decompose()
    for img in soup.find_all('img'):
        img.decompose()
    # Remove HTML comments (parser cache reports, etc.)
    from bs4 import Comment
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    for sel in _STRIP_SELECTORS:
        for el in soup.select(sel):
            el.decompose()
    for p in soup.find_all('p'):
        if not p.get_text(strip=True):
            p.decompose()
    return soup


def _inner_html(tag):
    return ''.join(str(c) for c in tag.children)


def _extract_prp_content(content):
    """Extract substantive text from prp-pages-output divs, skipping footnotes."""
    pp_divs = content.find_all(class_='prp-pages-output')
    if not pp_divs:
        return None
    parts = [_inner_html(d) for d in pp_divs if not _is_footnote_div(d)]
    return '\n'.join(parts) if parts else None


def _replace_deprecated_tags(html_str):
    """Convert <i>→<em>, <b>→<strong> without a full re-parse."""
    # Handle <i class="..."> and plain <i> — replace opening tags
    html_str = re.sub(r'<i(\s[^>]*)?>', lambda m: f'<em{m.group(1) or ""}>', html_str)
    html_str = re.sub(r'</i>', '</em>', html_str)
    html_str = re.sub(r'<b(\s[^>]*)?>', lambda m: f'<strong{m.group(1) or ""}>', html_str)
    html_str = re.sub(r'</b>', '</strong>', html_str)
    return html_str


def _strip_inline_styles(html_str):
    """Remove style="..." attributes from HTML."""
    return re.sub(r'\s*style="[^"]*"', '', html_str)


def _clean_chapter_html(raw_html):
    """
    Full cleaning pipeline for one chapter's raw Wikisource HTML:
    1. Parse and strip MediaWiki chrome
    2. Extract prp-pages-output content (main text, skip footnotes)
    3. Remove empty anchors
    4. Replace <i>/<b> with <em>/<strong>
    5. Strip inline styles
    Returns a clean HTML string containing only the chapter's prose.
    """
    soup = BeautifulSoup(raw_html, 'html.parser')
    _clean_soup(soup)

    content = soup.find(class_='mw-parser-output') or soup
    prp_html = _extract_prp_content(content)

    if prp_html:
        # Re-parse the extracted content for further cleaning
        inner_soup = BeautifulSoup(prp_html, 'html.parser')
    else:
        # Fallback: use the full content area
        inner_soup = content

    # Unwrap dropinitial decorative drop-cap spans (preserves the letter text,
    # removes chrome class wrappers that have no BSW CSS support)
    for span in inner_soup.find_all('span'):
        if any(cls in _DROPINITIAL_CLASSES for cls in span.get('class', [])):
            span.unwrap()

    # Remove empty anchor tags (W9 rule)
    for a in inner_soup.find_all('a'):
        if a.get('id') and not a.get('href') and not a.get_text(strip=True):
            a.decompose()

    # Remove any remaining mw-heading wrappers, promoting their headings
    # (for this text they appear rarely but keep things clean)
    for mwh in inner_soup.find_all(class_='mw-heading'):
        mwh.unwrap()

    result = str(inner_soup)
    result = _replace_deprecated_tags(result)
    result = _strip_inline_styles(result)

    # Remove any stray parser cache comments that slipped through
    result = re.sub(r'<!--\s*NewPP limit.*?-->', '', result, flags=re.DOTALL)
    result = re.sub(r'<!--\s*Transclusion expansion.*?-->', '', result, flags=re.DOTALL)
    result = re.sub(r'<!--.*?-->', '', result, flags=re.DOTALL)

    return result.strip()


# ---------------------------------------------------------------------------
# Wikisource fetch
# ---------------------------------------------------------------------------

def _fetch_chapter(chapter_num):
    """
    Fetch one chapter from Wikisource.
    Returns cleaned HTML string or None if the page is missing/empty.
    """
    page_title = f'Revelations of Divine Love/Chapter {chapter_num}'
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
        resp = requests.get(WS_API, params=params, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f'  [Ch {chapter_num}] network error: {e}', file=sys.stderr)
        return None

    if 'error' in data:
        code = data['error'].get('code', '')
        if code == 'missingtitle':
            print(f'  [Ch {chapter_num}] missing — skipping')
            return None
        print(f'  [Ch {chapter_num}] API error [{code}]: {data["error"].get("info", "")}',
              file=sys.stderr)
        return None

    raw_html = data['parse']['text']
    if not raw_html:
        print(f'  [Ch {chapter_num}] empty response — skipping')
        return None

    cleaned = _clean_chapter_html(raw_html)
    if not cleaned or len(cleaned) < 50:
        print(f'  [Ch {chapter_num}] cleaned HTML too short — skipping')
        return None

    return cleaned


# ---------------------------------------------------------------------------
# Build sections
# ---------------------------------------------------------------------------

def build_output(chapter_htmls):
    """
    Given {ch_num: html_str}, assemble 13 BSW Library v2 sections.
    Returns (html_output, section_count, missing_chapters).
    """
    parts = []
    missing = []

    for heading, chapters in SECTIONS:
        section_parts = []
        for ch in chapters:
            html = chapter_htmls.get(ch)
            if html:
                section_parts.append(html)
            else:
                missing.append(ch)

        if not section_parts:
            print(f'  WARN: section "{heading}" has no content — omitting')
            continue

        safe_heading = heading.replace('"', '&quot;')
        body = '\n'.join(section_parts)
        section_html = (
            f'<section data-heading="{safe_heading}">\n'
            f'<h2 class="lib-section__title">{heading}</h2>\n'
            f'{body}\n'
            f'</section>'
        )
        parts.append(section_html)

    return '\n\n'.join(parts) + '\n', len(parts), sorted(set(missing))


# ---------------------------------------------------------------------------
# Index patching
# ---------------------------------------------------------------------------

def _patch_index(section_count):
    """Update totalSections for julian-revelations in data/library/index.json."""
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index = json.load(f)

    entry = next((d for d in index if d['id'] == 'julian-revelations'), None)
    if entry is None:
        print('  WARN: julian-revelations not found in index.json — skipping patch')
        return

    old = entry.get('totalSections')
    entry['totalSections'] = section_count
    print(f'  [index] totalSections: {old} → {section_count}')

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
        f.write('\n')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print('fetch-julian.py — Revelations of Divine Love (Warrack, Long Text, 86 chs)')
    print(f'Output: {OUT_PATH}')
    print()

    # Fetch all 86 chapters
    chapter_htmls = {}
    for ch in range(1, 87):
        if ch > 1:
            time.sleep(RATE_DELAY)
        print(f'  Fetching Chapter {ch}…', end=' ', flush=True)
        html = _fetch_chapter(ch)
        if html:
            chapter_htmls[ch] = html
            # Rough word count for this chapter
            words = len(BeautifulSoup(html, 'html.parser').get_text().split())
            print(f'OK ({words}w)')
        else:
            print('SKIPPED')

    fetched = len(chapter_htmls)
    total_requested = 86
    missing_fetch = [ch for ch in range(1, 87) if ch not in chapter_htmls]
    print(f'\nFetched: {fetched}/{total_requested} chapters')
    if missing_fetch:
        print(f'Missing: {missing_fetch}')

    # Build sections
    print('\nBuilding sections…')
    output_html, section_count, missing_sect = build_output(chapter_htmls)

    # Word count on final output
    all_text = BeautifulSoup(output_html, 'html.parser').get_text()
    word_count = len(all_text.split())

    # Write output
    os.makedirs(HTML_DIR, exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write(output_html)
    print(f'Wrote: {OUT_PATH}')

    # Patch index
    print('\nPatching index.json…')
    _patch_index(section_count)

    # Summary
    print()
    print('=' * 60)
    print(f'Sections produced : {section_count}')
    print(f'Total word count  : {word_count:,}')
    print(f'Chapters fetched  : {fetched}/{total_requested}')
    if missing_sect:
        print(f'Chapters missing  : {missing_sect}')
    else:
        print('Chapters missing  : none')
    print('=' * 60)


if __name__ == '__main__':
    main()
