#!/usr/bin/env python3
"""
Scans topics/ and regenerates data/topics.json.

For each topic folder (excluding _template* dirs) it extracts:
  - label  : from <h1 class="tg-hero__title">, or data-bible-book attr, or <title>
  - type   : "book" if tg-hero__type starts with "Book Study" or body has bk-* class;
             "topical" otherwise
  - book   : (optional) data-bible-book value, lowercased — used by the Reader banner

Existing entries keep their label/book if already present in the JSON; only newly
discovered slugs are appended.  Run from the repo root:

    python3 scripts/build-topics-manifest.py
"""

import html as html_mod
import json
import re
from pathlib import Path

REPO_ROOT  = Path(__file__).resolve().parent.parent
TOPICS_DIR = REPO_ROOT / 'topics'
OUTPUT     = REPO_ROOT / 'data' / 'topics.json'
SKIP       = ('_',)


def _text(html, pattern):
    """Return inner text of first regex match, HTML tags stripped."""
    m = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
    if not m:
        return ''
    return html_mod.unescape(re.sub(r'<[^>]+>', '', m.group(1)).strip())


def _attr(html, attr):
    m = re.search(r'\b' + re.escape(attr) + r'="([^"]*)"', html)
    return m.group(1) if m else ''


def parse_page(slug, html):
    # Label
    label = _text(html, r'class="tg-hero__title"[^>]*>(.*?)</')
    if not label:
        bib = _attr(html, 'data-bible-book')
        label = bib if bib else ''
    if not label:
        raw = _text(html, r'<title>(.*?)</title>')
        label = re.sub(r'\s*[—–·-].*$', '', raw).strip()
    if not label:
        label = slug.replace('-', ' ').title()

    # Type
    hero_type = _text(html, r'class="tg-hero__type"[^>]*>(.*?)</')
    if hero_type.lower().startswith('book study'):
        topic_type = 'book'
    elif re.search(r'class="[^"]*\bbk-', html):
        topic_type = 'book'
    else:
        topic_type = 'topical'

    # Book ID for Reader banner
    book_id = _attr(html, 'data-bible-book').lower() or None

    entry = {'slug': slug, 'label': label, 'type': topic_type}
    if book_id:
        entry['book'] = book_id
    return entry


def main():
    # Load existing manifest to preserve hand-edited labels
    existing = {}
    if OUTPUT.exists():
        try:
            for e in json.loads(OUTPUT.read_text('utf-8')):
                existing[e['slug']] = e
        except Exception:
            pass

    entries = []
    for path in sorted(TOPICS_DIR.iterdir()):
        if not path.is_dir():
            continue
        slug = path.name
        if any(slug.startswith(p) for p in SKIP):
            continue
        index = path / 'index.html'
        if not index.exists():
            print(f'  skip {slug}: no index.html')
            continue

        if slug in existing:
            entries.append(existing[slug])
            print(f'  = {slug} (kept existing entry)')
        else:
            html  = index.read_text(encoding='utf-8')
            entry = parse_page(slug, html)
            entries.append(entry)
            print(f'  + {slug} ({entry["type"]}): {entry["label"]}')

    # Sort: books first, then topical, alphabetically within each group
    entries.sort(key=lambda e: (0 if e['type'] == 'book' else 1, e['label'].lower()))

    OUTPUT.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + '\n',
        encoding='utf-8'
    )
    print(f'\nWrote {len(entries)} topics → {OUTPUT.relative_to(REPO_ROOT)}')


if __name__ == '__main__':
    main()
