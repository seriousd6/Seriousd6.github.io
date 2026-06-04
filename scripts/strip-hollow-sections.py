#!/usr/bin/env python3
"""Remove hollow section stubs from library HTML docs.

A section is hollow when it contains no <p> elements and its total text
content (including the h2 heading) is below MAX_CHARS.  These are
structural dividers (CHAPTER I, SECTION II, Roman-numeral separators,
NOTE A stub headers, etc.) that the resectioning script created from
heading tags but never had body text beneath them.

Run:  python3 scripts/strip-hollow-sections.py
"""

from pathlib import Path
from bs4 import BeautifulSoup

BASE = Path('data/library/html')
MAX_CHARS = 600   # sections below this with zero <p> tags are hollow

# Files confirmed to have hollow structural stubs — see audit 2026-06-03
TARGETS = [
    'baxter-reformed-pastor.html',
    'meister-eckhart-sermons.html',
    'luther-bondage-of-will.html',
    'pseudo-dionysius-works.html',
    'taylor-holy-living.html',
    'catherine-dialogue.html',
    'newman-apologia.html',
    'shepherd-of-hermas.html',
    'origen-de-principiis.html',
    'gregory-great-pastoral-rule.html',
]


def strip_hollow(path: Path) -> tuple[int, list[str]]:
    """Return (removed_count, list_of_removed_headings)."""
    html = path.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    removed = []
    for sec in soup.select('section[data-heading]'):
        # Only consider top-level sections (not nested inside another section)
        if sec.find_parent('section'):
            continue
        has_p = bool(sec.find('p'))
        text_len = len(sec.get_text(' ', strip=True))
        if not has_p and text_len < MAX_CHARS:
            removed.append(f'[{sec["data-heading"][:60]}] ({text_len} chars)')
            sec.decompose()

    if removed:
        # Serialize: BeautifulSoup adds html/body wrappers — strip them back off
        body = soup.find('body')
        out = ''.join(str(c) for c in body.children) if body else str(soup)
        path.write_text(out.strip() + '\n', encoding='utf-8')

    return len(removed), removed


def main():
    total_removed = 0
    for name in TARGETS:
        path = BASE / name
        if not path.exists():
            print(f'MISSING: {name}')
            continue
        count, headings = strip_hollow(path)
        if count:
            print(f'{name}: removed {count} hollow section(s)')
            for h in headings:
                print(f'  - {h}')
            total_removed += count
        else:
            print(f'{name}: nothing to remove')
    print(f'\nTotal sections removed: {total_removed}')


if __name__ == '__main__':
    main()
