#!/usr/bin/env python3
"""
fetch-ellicott.py — Scrape Ellicott's Commentary for English Readers from StudyLight.org.

Ellicott's Commentary for English Readers (Charles John Ellicott ed., 1878-1884) is public domain.
Source: StudyLight.org (https://www.studylight.org/commentaries/eng/ebc/)
robots.txt: Allow: /, Content-Signal: search=yes,ai-train=no — scraping permitted.

Output: data/commentary/ellicott/{bookId}.json
Data shape: {"chapter": {"verseNum": "<p>HTML text</p>", ...}}
            Same as other commentary sources (jfb, clarke, etc.)

Usage:
  python3 scripts/fetch-ellicott.py [--force] [--delay 0.5] [--only genesis,john]
"""

import argparse, json, os, re, time, urllib.request

REPO_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS_JSON = os.path.join(REPO_ROOT, 'data', 'bible', 'books.json')
OUT_DIR    = os.path.join(REPO_ROOT, 'data', 'commentary', 'ellicott')

BASE_URL   = 'https://www.studylight.org/commentaries/eng/ebc/{slug}-{ch}.html'
HEADERS    = {'User-Agent': 'bsw-fetch/1.0 (personal Bible study site; public domain content)'}


# ── Book ID → StudyLight URL slug ────────────────────────────────────────────

def book_to_slug(book_id):
    """Convert internal book ID to StudyLight URL slug."""
    if book_id == 'songofsolomon':
        return 'song-of-solomon'
    # Insert hyphen after a leading digit: 1samuel → 1-samuel, 2kings → 2-kings
    return re.sub(r'^(\d)', r'\1-', book_id)


# ── HTML cleaning ─────────────────────────────────────────────────────────────

def clean_html(raw_html):
    """Strip StudyLight chrome, keep commentary text as clean HTML."""
    # Remove return-to-top div
    html = re.sub(r'<div[^>]*class="return-to-top-div"[^>]*>.*?</div>', '', raw_html,
                  flags=re.DOTALL | re.IGNORECASE)
    # Remove biblio div
    html = re.sub(r'<div[^>]*class="biblio"[^>]*>.*?</div>', '', html,
                  flags=re.DOTALL | re.IGNORECASE)
    # Remove scroll indicator div
    html = re.sub(r'<div[^>]*class="scroll-indicator"[^>]*>.*?</div>', '', html,
                  flags=re.DOTALL | re.IGNORECASE)
    # Convert scriptRef spans to plain text (their inner text is the citation)
    html = re.sub(r'<span[^>]*class="scriptRef"[^>]*>(.*?)</span>', r'\1',
                  html, flags=re.DOTALL | re.IGNORECASE)
    # Convert <br/> and <br /> to <br>
    html = re.sub(r'<br\s*/>', '<br>', html, flags=re.IGNORECASE)
    # Strip any remaining div/span wrappers that aren't <p>, <strong>, <em>, <br>
    html = re.sub(r'<(?!/?(?:p|strong|em|br)\b)[a-z][^>]*>', ' ', html, flags=re.IGNORECASE)
    html = re.sub(r'</(?!(?:p|strong|em)\b)[a-z]+>', ' ', html, flags=re.IGNORECASE)
    # Normalise whitespace inside tags
    html = re.sub(r'>\s+<', '><', html)
    html = re.sub(r'\s{3,}', ' ', html)
    return html.strip()


def extract_verses(html):
    """
    Parse StudyLight chapter HTML and return {verseNum: html_string}.

    Handles two data-entry formats:
      verse-N       — individual verse (most books)
      verses-N-M    — block entry covering a verse range (short books like Obadiah, 2 John)
                      stored under verse N (the first verse of the range)
    """
    # Split on h3 boundaries to get sections
    sections = re.split(r'(?=<h3[^>]*class="commentaries-entry-number")', html, flags=re.IGNORECASE)

    result = {}
    for section in sections:
        # Find the primary anchor's data-entry attribute in this h3
        m = re.search(r'data-entry="([^"]+)"', section, re.IGNORECASE)
        if not m:
            continue
        entry = m.group(1)

        # Individual verse entry: verse-N
        vm = re.match(r'^verse-(\d+)$', entry)
        if vm:
            verse_num = vm.group(1)
        else:
            # Range entry: verses-N-M → store under first verse N
            rm = re.match(r'^verses-(\d+)-\d+$', entry)
            if rm:
                verse_num = rm.group(1)
            else:
                continue  # intro/section entries — skip

        # Extract content after the closing </h3>
        body_start = section.find('</h3>')
        if body_start == -1:
            continue
        body = section[body_start + 5:]

        # Clean and store if non-empty
        cleaned = clean_html(body)
        # Minimal text content check: must have real word content
        text_only = re.sub(r'<[^>]+>', '', cleaned).strip()
        if len(text_only) < 10:
            continue

        result[verse_num] = cleaned

    return result


# ── HTTP fetch ────────────────────────────────────────────────────────────────

def fetch_chapter(slug, ch, delay=0.5):
    """Fetch a single chapter page from StudyLight. Returns HTML string or None."""
    url = BASE_URL.format(slug=slug, ch=ch)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status != 200:
                return None
            html = r.read().decode('utf-8', errors='replace')
        time.sleep(delay)
        return html
    except Exception as e:
        print(f'    WARN: {url} — {e}')
        time.sleep(delay * 2)
        return None


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Fetch Ellicott\'s Commentary from StudyLight.org.')
    parser.add_argument('--force', action='store_true', help='Re-fetch even if output file exists')
    parser.add_argument('--delay', type=float, default=0.5, help='Seconds between requests (default 0.5)')
    parser.add_argument('--only', help='Comma-separated book IDs to fetch (e.g. genesis,john)')
    args = parser.parse_args()

    only = set(x.strip() for x in args.only.split(',')) if args.only else None

    with open(BOOKS_JSON) as f:
        books = json.load(f)

    os.makedirs(OUT_DIR, exist_ok=True)

    total_books = 0
    total_verses = 0

    for book in books:
        book_id = book['id']
        if only and book_id not in only:
            continue

        out_file = os.path.join(OUT_DIR, book_id + '.json')

        # Skip if already done (resume support)
        if os.path.exists(out_file) and not args.force:
            with open(out_file) as f:
                existing = json.load(f)
            n = sum(len(vs) for vs in existing.values())
            if n > 0:
                print(f'  {book["name"]}: {n} verses already fetched — skipping (--force to re-fetch)')
                continue

        slug = book_to_slug(book_id)
        ch_count = book['chapters']
        print(f'\n── {book["name"]} ({book_id}, {ch_count} chs, slug={slug}) ──')

        book_data = {}
        for ch in range(1, ch_count + 1):
            html = fetch_chapter(slug, ch, args.delay)
            if html is None:
                print(f'    ch {ch}: FAILED')
                continue

            # Verify this is actually an Ellicott page (not a 404 redirect)
            if 'ebc' not in html.lower() and 'ellicott' not in html.lower():
                print(f'    ch {ch}: not Ellicott content')
                continue

            verses = extract_verses(html)
            if verses:
                book_data[str(ch)] = verses
                print(f'    ch {ch}: {len(verses)} verses')
            else:
                print(f'    ch {ch}: no verses found')

        # Sort chapters numerically before writing
        sorted_data = {}
        for ch_key in sorted(book_data.keys(), key=int):
            sorted_data[ch_key] = {}
            for v_key in sorted(book_data[ch_key].keys(), key=int):
                sorted_data[ch_key][v_key] = book_data[ch_key][v_key]

        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_data, f, ensure_ascii=False, separators=(',', ':'))

        n = sum(len(vs) for vs in sorted_data.values())
        print(f'  → {n} verse sections written to {out_file}')
        total_books += 1
        total_verses += n

    print(f'\nAll done. {total_books} books, {total_verses} verse sections.')


if __name__ == '__main__':
    main()
