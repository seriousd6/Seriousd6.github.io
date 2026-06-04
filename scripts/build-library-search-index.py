#!/usr/bin/env python3
"""
Regenerates data/library/search-index.json from scratch.

Two source formats:
  Format A — JSON docs (data/library/docs/*.json)
      Only for docs that have NO html_url in index.json (confessions,
      catechisms, overview compilations).  Each section already has ref,
      heading, and an html string.

  Format B — HTML docs (data/library/html/*.html)
      For every index.json entry with an html_url field.
      Parse <section data-heading="…"> elements; body text = first <p>.
      Exception: TEI-format docs (class="tei tei-div" present) use
      .tei-head elements as section boundaries.

Run from the repo root:  python3 scripts/build-library-search-index.py
"""

import json
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise SystemExit('pip install beautifulsoup4')

REPO       = Path(__file__).resolve().parent.parent
DOCS_DIR   = REPO / 'data' / 'library' / 'docs'
HTML_DIR   = REPO / 'data' / 'library' / 'html'
IDX_PATH   = REPO / 'data' / 'library' / 'index.json'
OUT_PATH   = REPO / 'data' / 'library' / 'search-index.json'
MAX_CHARS  = 350


def _text(soup_el):
    return soup_el.get_text(' ', strip=True)[:MAX_CHARS] if soup_el else ''


def process_json_docs(html_doc_ids):
    """Format A: JSON sections from data/library/docs/*.json.
    Only process docs that do NOT have an html_url (no double-indexing)."""
    entries = []
    for path in sorted(DOCS_DIR.glob('*.json')):
        doc = json.loads(path.read_text('utf-8'))
        doc_id = doc.get('id', path.stem)
        if doc_id in html_doc_ids:
            continue  # will be indexed from HTML source
        for sec in doc.get('sections', []):
            raw_html = sec.get('html', '')
            text = _text(BeautifulSoup(raw_html, 'html.parser')) if raw_html else ''
            entries.append({
                'docId':   doc_id,
                'ref':     str(sec.get('ref', '')),
                'heading': sec.get('heading', ''),
                'text':    text,
            })
        print(f'  [A] {doc_id}: {len(doc.get("sections", []))} sections')
    return entries


def process_html_doc(doc_id, html_path):
    """Format B: parse a single HTML library doc and return entry list."""
    html = html_path.read_text('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    entries = []

    if 'tei tei-div' in html:
        # TEI format — Calvin's Institutes vol 1
        for i, head in enumerate(soup.select('.tei-head'), 1):
            heading = _text(head)
            sibling = head.find_next_sibling()
            text = _text(sibling) if sibling else ''
            entries.append({
                'docId':   doc_id,
                'ref':     str(i),
                'heading': heading,
                'text':    text,
            })
    else:
        for i, sec in enumerate(soup.select('section[data-heading]'), 1):
            heading = sec.get('data-heading', '')
            first_p = sec.find('p')
            text = _text(first_p) if first_p else _text(sec)[:MAX_CHARS]
            entries.append({
                'docId':   doc_id,
                'ref':     str(i),
                'heading': heading,
                'text':    text,
            })

    return entries


def main():
    index = json.loads(IDX_PATH.read_text('utf-8'))

    html_doc_ids = {e['id'] for e in index if e.get('html_url')}

    entries = []

    # Format A — JSON-only docs
    entries.extend(process_json_docs(html_doc_ids))

    # Format B — HTML docs
    html_count = 0
    for entry in index:
        if not entry.get('html_url'):
            continue
        doc_id   = entry['id']
        html_file = HTML_DIR / entry['html_url']
        if not html_file.exists():
            print(f'  [B] SKIP {doc_id}: {html_file.name} not found')
            continue
        doc_entries = process_html_doc(doc_id, html_file)
        entries.extend(doc_entries)
        html_count += 1
        print(f'  [B] {doc_id}: {len(doc_entries)} sections')

    # Sort for deterministic diffs
    entries.sort(key=lambda e: (e['docId'], e['ref'].zfill(6)))

    OUT_PATH.write_text(
        json.dumps(entries, ensure_ascii=False, separators=(',', ':')) + '\n',
        encoding='utf-8',
    )

    unique_docs = len({e['docId'] for e in entries})
    print(f'\nWrote {len(entries)} entries, {unique_docs} docs → {OUT_PATH.relative_to(REPO)}')


if __name__ == '__main__':
    main()
