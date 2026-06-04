#!/usr/bin/env python3
"""
fetch-vincent.py — Fetch The Commonitory of Vincent of Lerins from Wikisource
and produce a BSW Library HTML v2 file at data/library/html/vincent-of-lerins-commonitory.html

Source: Wikisource NPNF2 Vol. XI, chapters 1–33 via the MediaWiki parse API.
Page pattern:
  Nicene and Post-Nicene Fathers: Series II/Volume XI/The Commonitory of Vincent of Lerins/Chapter N

Sections (8):
  1. Preface and the Vincentian Canon  — Ch 1–4
  2. The Test of Antiquity             — Ch 5–9
  3. The Authority of Councils         — Ch 10–13
  4. Development of Doctrine           — Ch 14–18
  5. Against Novelty                   — Ch 19–22
  6. False Teachers and Their Methods  — Ch 23–26
  7. Examples and Summaries            — Ch 27–30
  8. Final Exhortations                — Ch 31–33
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
OUT_FILE    = os.path.join(REPO_ROOT, 'data', 'library', 'html',
                           'vincent-of-lerins-commonitory.html')

WS_API      = 'https://en.wikisource.org/w/api.php'
HEADERS     = {'User-Agent': 'bible-study-library-builder/1.0 (dse.saved@gmail.com)'}
RATE_DELAY  = 1.0  # seconds between requests

NPNF2_BASE  = ('Nicene and Post-Nicene Fathers: Series II/Volume XI/'
               'The Commonitory of Vincent of Lerins/Chapter ')

# ---------------------------------------------------------------------------
# Section groupings: (heading, list of chapter numbers)
# ---------------------------------------------------------------------------
SECTIONS = [
    ('Preface and the Vincentian Canon',   list(range(1, 5))),   # Ch 1–4
    ('The Test of Antiquity',              list(range(5, 10))),  # Ch 5–9
    ('The Authority of Councils',          list(range(10, 14))), # Ch 10–13
    ('Development of Doctrine',            list(range(14, 19))), # Ch 14–18
    ('Against Novelty',                    list(range(19, 23))), # Ch 19–22
    ('False Teachers and Their Methods',   list(range(23, 27))), # Ch 23–26
    ('Examples and Summaries',             list(range(27, 31))), # Ch 27–30
    ('Final Exhortations',                 list(range(31, 34))), # Ch 31–33
]

# ---------------------------------------------------------------------------
# Wikisource fetch helpers
# ---------------------------------------------------------------------------

def fetch_chapter(chapter_num):
    """Fetch one chapter from Wikisource. Returns raw HTML string or None."""
    page_title = f'{NPNF2_BASE}{chapter_num}'
    params = {
        'action': 'parse',
        'page': page_title,
        'prop': 'text',
        'format': 'json',
        'formatversion': '2',
    }
    try:
        resp = requests.get(WS_API, params=params, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if 'error' in data:
            print(f'  [skip] Ch {chapter_num}: {data["error"].get("info", "API error")}')
            return None
        return data['parse']['text']
    except Exception as exc:
        print(f'  [skip] Ch {chapter_num}: {exc}')
        return None


# ---------------------------------------------------------------------------
# HTML cleaning helpers
# ---------------------------------------------------------------------------

def _replace_tag(soup_tag, old_name, new_name):
    """Replace all occurrences of old_name with new_name in-place."""
    for tag in soup_tag.find_all(old_name):
        tag.name = new_name


def clean_chapter_html(raw_html):
    """
    Parse raw MediaWiki HTML, apply BSW Library v2 cleaning, and return a list
    of cleaned <p> Tag objects (prose content only).

    Cleaning steps:
      - Unwrap mw-parser-output
      - Remove mw-editsection spans
      - Remove mw-heading* divs (just extract their text as headings? No — skip them,
        chapter headings are synthesised from section headings in the parent)
      - Remove pagenum / pageno spans and [Pg N] text
      - Remove empty <a id="..."> anchor tags
      - Remove style="" attributes
      - Convert <i> → <em>, <b> → <strong>
      - Keep only <p> elements as prose
    """
    soup = BeautifulSoup(raw_html, 'html.parser')

    # 1. Unwrap mw-parser-output container (keep children)
    mw_output = soup.find(class_='mw-parser-output')
    if mw_output:
        mw_output.unwrap()

    # 2. Remove mw-editsection spans entirely
    for el in soup.find_all(class_='mw-editsection'):
        el.decompose()

    # 3. Remove mw-heading divs (they duplicate chapter numbering; not needed)
    for el in soup.find_all(class_=re.compile(r'\bmw-heading\b')):
        el.decompose()

    # 4. Remove pagenum / pageno / tei-pb spans
    for el in soup.find_all(class_=re.compile(r'\bpagenum\b|\bpageno\b|\btei-pb\b')):
        el.decompose()

    # 5. Remove empty <a id="..."> anchor targets (no href, no text)
    for el in soup.find_all('a'):
        if el.get('id') and not el.get('href') and not el.get_text(strip=True):
            el.decompose()

    # 6. Remove id="" attributes from all headings (they produce anchor clutter)
    for el in soup.find_all(re.compile(r'^h[1-6]$')):
        if el.get('id'):
            del el['id']

    # 7. Remove style="" attributes from all elements
    for el in soup.find_all(True):
        if el.get('style'):
            del el['style']

    # 8. Remove class="" attributes from all elements (strip source chrome)
    for el in soup.find_all(True):
        if el.get('class'):
            del el['class']

    # 9. Convert deprecated tags
    for tag in soup.find_all('i'):
        tag.name = 'em'
    for tag in soup.find_all('b'):
        tag.name = 'strong'

    # 10. Remove [Pg N] text nodes
    pg_pat = re.compile(r'\[Pg\s+\d+\]')
    for text_node in soup.find_all(string=pg_pat):
        new_text = pg_pat.sub('', str(text_node))
        text_node.replace_with(new_text)

    # 11. Collect prose <p> elements; skip if empty or purely whitespace
    paragraphs = []
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if not text:
            continue
        paragraphs.append(p)

    return paragraphs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print('fetch-vincent.py — The Commonitory of Vincent of Lerins')
    print('='*60)

    # Fetch all chapters first (collect into dict keyed by chapter number)
    chapter_paras = {}  # ch_num → list of <p> Tags
    for ch_num in range(1, 34):
        print(f'  Fetching chapter {ch_num}...', end=' ', flush=True)
        raw = fetch_chapter(ch_num)
        if raw:
            paras = clean_chapter_html(raw)
            chapter_paras[ch_num] = paras
            print(f'{len(paras)} paragraphs')
        else:
            chapter_paras[ch_num] = []
            # already printed skip message above
        if ch_num < 33:
            time.sleep(RATE_DELAY)

    print()

    # Build output HTML
    output_parts = []
    total_words = 0
    sections_written = 0

    for heading, ch_list in SECTIONS:
        # Gather all paragraphs for chapters in this section
        section_paras = []
        for ch_num in ch_list:
            paras = chapter_paras.get(ch_num, [])
            section_paras.extend(paras)

        if not section_paras:
            print(f'  [warn] Section "{heading}" has no content — skipping')
            continue

        # Render section
        lines = [f'<section data-heading="{heading}">']
        lines.append(f'<h2 class="lib-section__title">{heading}</h2>')
        for p in section_paras:
            # Render the paragraph tag as a string, strip trailing newlines
            p_str = str(p).strip()
            lines.append(p_str)
        lines.append('</section>')
        output_parts.append('\n'.join(lines))

        # Word count for this section
        section_text = ' '.join(p.get_text(' ', strip=True) for p in section_paras)
        words = len(section_text.split())
        total_words += words
        sections_written += 1
        print(f'  Section {sections_written}: "{heading}" — {len(section_paras)} paras, {words} words')

    # Write file
    final_html = '\n'.join(output_parts) + '\n'
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print()
    print(f'Written: {OUT_FILE}')
    print(f'Sections: {sections_written}')
    print(f'Total words: {total_words:,}')


if __name__ == '__main__':
    main()
