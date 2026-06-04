#!/usr/bin/env python3
"""
fetch-cassian.py — Fetch John Cassian's Conferences from Wikisource (NPNF2 Vol. XI)
and write data/library/html/cassian-conferences.html in BSW Library HTML v2 format.

25 sections: Preface (preserved from existing file) + Conferences I–XXIV.
Each Conference section concatenates all its chapters in order.

Rate limit: 1.5s between requests (Wikisource policy).
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.dirname(SCRIPT_DIR)
HTML_DIR   = os.path.join(REPO_ROOT, 'data', 'library', 'html')
OUT_PATH   = os.path.join(HTML_DIR, 'cassian-conferences.html')

WS_API   = 'https://en.wikisource.org/w/api.php'
HEADERS  = {'User-Agent': 'bible-study-library-builder/1.0 (dse.saved@gmail.com)'}
DELAY    = 1.5  # seconds between requests

BASE = ('Nicene and Post-Nicene Fathers: Series II/Volume XI/'
        'John Cassian/Conferences of John Cassian, Part')

# Part mapping for each conference (1-indexed)
CONFERENCE_PARTS = {
    1: 'I',  2: 'I',  3: 'I',  4: 'I',  5: 'I',
    6: 'I',  7: 'I',  8: 'I',  9: 'I', 10: 'I',
    11: 'II', 12: 'II', 13: 'II', 14: 'II', 15: 'II',
    16: 'II', 17: 'II',
    18: 'III', 19: 'III', 20: 'III', 21: 'III', 22: 'III',
    23: 'III', 24: 'III',
}

# Approximate max chapters per conference (we stop at first 404/empty)
MAX_CHAPTERS = {
     1: 23,  2: 26,  3: 22,  4: 22,  5: 27,  6: 17,  7: 34,
     8: 25,  9: 36, 10: 14, 11: 15, 12: 16, 13: 18, 14: 19,
    15: 10, 16: 28, 17: 30, 18: 16, 19: 16, 20: 12, 21: 35,
    22: 15, 23: 21, 24: 26,
}

# Conference headings (1-indexed)
CONFERENCE_TITLES = {
     1: 'Conference I — The Goal and End of the Monk (Abbot Moses)',
     2: 'Conference II — On Discretion (Abbot Moses)',
     3: 'Conference III — On the Three Renunciations (Abbot Paphnutius)',
     4: 'Conference IV — On the Lusts of the Flesh and of the Spirit (Abbot Daniel)',
     5: 'Conference V — On the Eight Principal Faults (Abbot Serapion)',
     6: 'Conference VI — On the Death of Holy Men and of Evil (Abbot Theodore)',
     7: 'Conference VII — On the Mutability of the Soul (Abbot Serenus)',
     8: 'Conference VIII — On Principalities (Abbot Serenus)',
     9: 'Conference IX — On Prayer (Abbot Isaac)',
    10: 'Conference X — On Prayer (continued) (Abbot Isaac)',
    11: 'Conference XI — On Perfection (Abbot Chaeremon)',
    12: 'Conference XII — On Chastity (Abbot Chaeremon)',
    13: 'Conference XIII — On Divine Protection and Free Will (Abbot Chaeremon)',
    14: 'Conference XIV — On Spiritual Knowledge (Abbot Nesteros)',
    15: 'Conference XV — On Divine Gifts (Abbot Nesteros)',
    16: 'Conference XVI — On Friendship (Abbot Joseph)',
    17: 'Conference XVII — On Making Promises (Abbot Joseph)',
    18: 'Conference XVIII — On the Three Sorts of Monks (Abbot Piamun)',
    19: 'Conference XIX — On the Goal of the Coenobite and Hermit (Abbot John)',
    20: 'Conference XX — On the End of Penitence (Abbot Pinufius)',
    21: 'Conference XXI — On the Relaxation of Lent (Abbot Theonas)',
    22: 'Conference XXII — On Night Illusions (Abbot Theonas)',
    23: 'Conference XXIII — On Sinlessness (Abbot Theonas)',
    24: 'Conference XXIV — On Mortification (Abbot Abraham)',
}


def _roman(n):
    """Convert integer (1-based) to uppercase Roman numeral string."""
    vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
            (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    r = ''
    for v, s in vals:
        while n >= v:
            r += s
            n -= v
    return r


def fetch_page(page_title):
    """Fetch parsed HTML from Wikisource API. Returns raw HTML string or None."""
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
        if 'parse' not in data:
            return None
        return data['parse']['text']
    except Exception as e:
        print(f"  [error] {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# HTML cleaning
# ---------------------------------------------------------------------------

# Attributes to keep on elements (everything else is stripped)
KEEP_ATTRS = {
    'a': ['href'],
    'td': ['colspan', 'rowspan'],
    'th': ['colspan', 'rowspan'],
}

# Tags to unwrap (keep text, remove tag)
UNWRAP_TAGS = {'span', 'font', 'big', 'small', 'sup', 'sub', 'abbr',
               'cite', 'q', 'bdo', 'em', 'strong', 'u', 's', 'del', 'ins'}

# Tags to strip entirely (remove tag AND its content)
STRIP_TAGS = {'style', 'script', 'noscript', 'head', 'meta', 'link',
              'figure', 'figcaption', 'nav'}


def clean_html(raw_html):
    """
    Take raw Wikisource API HTML and return a list of clean <p>...</p> strings.

    Strategy:
    1. Parse with BeautifulSoup.
    2. Remove MediaWiki chrome (mw-parser-output wrapper, categories, navboxes,
       edit sections, page-number spans, header/footer boilerplate,
       transclusion cache comments).
    3. Convert block elements to plain <p> paragraphs.
    4. Strip all inline tags except <a href>.
    5. Drop empty or very-short paragraphs.
    """
    soup = BeautifulSoup(raw_html, 'html.parser')

    # ── 1. Remove MediaWiki chrome ──────────────────────────────────────────
    for tag in soup.find_all(class_=re.compile(
            r'mw-editsection|mw-heading|mw-references|'
            r'printfooter|catlinks|noprint|toc|sister-project|'
            r'wikisource-transcluded-header|ws-noexport|'
            r'navigation-not-searchable|pagenum|tei-pb|'
            r'page_break|pagenumber|pageno')):
        tag.decompose()

    # Remove HTML comments (transclusion reports etc.)
    for comment in soup.find_all(string=lambda t: isinstance(t, str) and t.strip().startswith('Transclusion')):
        comment.extract()
    # Remove ALL html comments
    from bs4 import Comment
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()

    # Remove the outer mw-parser-output div (unwrap it — keep children)
    mw = soup.find(class_='mw-parser-output')
    if mw:
        mw.unwrap()

    # Remove Header template block (the "Nicene and Post-Nicene Fathers..." header)
    for tag in soup.find_all('div', class_=re.compile(r'ws-header|header-template')):
        tag.decompose()

    # Remove table-of-contents like tables
    for tag in soup.find_all('table'):
        tag.decompose()

    # Remove <hr> elements
    for tag in soup.find_all('hr'):
        tag.decompose()

    # ── 2. Build list of text-bearing block elements ────────────────────────
    # Collect all <p>, <h1>-<h6>, <blockquote>, <li> in document order.
    # We'll turn them all into <p> elements.
    paragraphs = []

    def is_block(tag):
        return tag.name in ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                             'blockquote', 'li', 'dd', 'dt')

    for el in soup.find_all(is_block):
        # Skip if it's nested inside another block we'll process
        if el.find_parent(['blockquote', 'li']) and el.name not in ('h1','h2','h3','h4','h5','h6'):
            pass  # allow — blockquote/li paragraphs are fine to include

        # Clean inline content
        cleaned = clean_inline(el)
        text = cleaned.strip()

        # Skip very short / empty
        if len(text) < 5:
            continue

        # Skip obvious boilerplate lines
        low = text.lower()
        if any(low.startswith(x) for x in [
            'nicene and post-nicene', 'john cassian', 'conferences of john cassian',
            'next:', 'previous:', '← ', '→ ', 'edit', 'retrieved from',
            'this page was last', 'categories:', 'hidden category',
        ]):
            continue

        paragraphs.append(f'<p>{text}</p>')

    return paragraphs


def clean_inline(el):
    """
    Return a clean inline HTML string for the content of el.
    - Keeps <a href="..."> but strips all other attributes.
    - Converts <b>/<strong> to nothing (keeps text).
    - Converts <i>/<em> to nothing (keeps text).
    - Strips all other inline tags (keeps text).
    - Removes footnote-like content (sup with number/[N]).
    """
    # Work on a copy so we don't mutate the tree
    import copy
    el_copy = copy.copy(el)

    result = []
    for child in el_copy.children:
        result.append(_render_inline(child))
    return ''.join(result).strip()


def _render_inline(node):
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ''

    tag = node.name

    # Skip footnote markers: <sup> with short text like [1] or * or †
    if tag == 'sup':
        txt = node.get_text()
        if re.match(r'^\s*[\[\(]?\d+[\]\)]?\s*$', txt) or txt.strip() in ('*', '†', '‡', '§'):
            return ''
        # non-numeric sup — keep as plain text
        return node.get_text()

    # Keep <a href> (external links become plain text; internal keep href)
    if tag == 'a':
        href = node.get('href', '')
        inner = ''.join(_render_inline(c) for c in node.children)
        if href and not href.startswith('#') and inner:
            return inner  # strip links, keep text only
        return inner

    # For all other tags — render children only (unwrap)
    return ''.join(_render_inline(c) for c in node.children)


# ---------------------------------------------------------------------------
# Preface extraction
# ---------------------------------------------------------------------------

def extract_preface(existing_path):
    """Read the existing file and return the first <section> (Preface) as-is."""
    if not os.path.exists(existing_path):
        return None
    with open(existing_path, encoding='utf-8') as f:
        content = f.read()
    # The preface is the first <section data-heading="Preface">...</section>
    m = re.search(
        r'(<section data-heading="Preface">.*?</section>)',
        content, re.DOTALL
    )
    if m:
        return m.group(1)
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print('=== fetch-cassian.py ===')

    # 1. Preserve existing Preface
    print('\n[1] Extracting Preface from existing file...')
    preface_html = extract_preface(OUT_PATH)
    if preface_html:
        print(f'    Preface found ({len(preface_html)} chars)')
    else:
        print('    WARNING: Preface not found in existing file. Will write empty placeholder.')
        preface_html = ('<section data-heading="Preface">'
                        '<h2 class="lib-section__title">Preface</h2>'
                        '<p>[Preface not available]</p>'
                        '</section>')

    # 2. Fetch each conference
    sections = [preface_html]
    chapter_counts = {}

    for conf_num in range(1, 25):
        roman_conf = _roman(conf_num)
        roman_part = CONFERENCE_PARTS[conf_num]
        title = CONFERENCE_TITLES[conf_num]
        max_ch = MAX_CHAPTERS[conf_num]

        print(f'\n[Conference {roman_conf}] {title}')

        # Try Part preface first (only once per part, at start)
        # (not collected into a separate section — we just skip it)

        chapter_paragraphs = []
        chapters_fetched = 0

        for ch_num in range(1, max_ch + 20):  # +20 buffer beyond approximate max
            # Correct Wikisource path: "Conferences of John Cassian, Part_I/Conference_I/Chapter_1"
            page_title = (f'{BASE}_{roman_part}/'
                          f'Conference_{roman_conf}/Chapter_{ch_num}')

            print(f'  Fetching Chapter {ch_num}...', end='', flush=True)
            time.sleep(DELAY)

            raw = fetch_page(page_title)
            if raw is None:
                print(' 404/error — stopping')
                break

            paras = clean_html(raw)
            if not paras:
                print(' empty — stopping')
                break

            print(f' {len(paras)} paragraphs')
            chapter_paragraphs.extend(paras)
            chapters_fetched += 1

        chapter_counts[conf_num] = chapters_fetched
        print(f'  => {chapters_fetched} chapters fetched for Conference {roman_conf}')

        if not chapter_paragraphs:
            # Fallback: create a stub section
            chapter_paragraphs = [f'<p>[Content for Conference {roman_conf} not available]</p>']

        # Build the section
        body = '\n'.join(chapter_paragraphs)
        section = (
            f'<section data-heading="{title}">'
            f'<h2 class="lib-section__title">{title}</h2>\n'
            f'{body}\n'
            f'</section>'
        )
        sections.append(section)

    # 3. Write output
    print(f'\n[3] Writing {OUT_PATH}...')
    output = '\n'.join(sections) + '\n'
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f'    Written: {len(output):,} bytes, {len(sections)} sections')

    # 4. Summary
    print('\n=== Summary ===')
    print(f'Total sections: {len(sections)} (1 Preface + {len(sections)-1} Conferences)')
    print('\nChapter counts per conference:')
    total_chapters = 0
    for cn in range(1, 25):
        count = chapter_counts.get(cn, 0)
        total_chapters += count
        print(f'  Conference {_roman(cn):>6}: {count} chapters')
    print(f'\nTotal chapters fetched: {total_chapters}')

    # Word count
    total_text = re.sub(r'<[^>]+>', ' ', output)
    words = len(total_text.split())
    print(f'Approximate word count: {words:,}')

    print('\nDone.')


if __name__ == '__main__':
    main()
