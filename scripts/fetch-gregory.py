#!/usr/bin/env python3
"""
fetch-gregory.py
Fetches Parts I–III of Gregory the Great's Book of Pastoral Rule from Wikisource,
cleans the HTML to BSW Library v2 format, then prepends them to the existing Part IV.

Output: data/library/html/gregory-great-pastoral-rule.html
"""

import json
import re
import sys
import time
import urllib.request
import urllib.parse
from html.parser import HTMLParser

try:
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError:
    print("ERROR: beautifulsoup4 not installed. Run: pip3 install beautifulsoup4")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

WIKI_API = "https://en.wikisource.org/w/api.php"
BASE_PAGE = "Nicene and Post-Nicene Fathers: Series II/Volume XII/Gregory the Great/The Book of Pastoral Rule"

OUTPUT_PATH = "data/library/html/gregory-great-pastoral-rule.html"
EXISTING_PART_IV_PATH = "data/library/html/gregory-great-pastoral-rule.html"

PART_TITLES = {
    "I":   "Part I — Who Ought and Who Ought Not to Undertake Pastoral Rule",
    "II":  "Part II — The Life of the Shepherd",
    "III": "Part III — How the Shepherd Should Teach and Admonish",
}


# ---------------------------------------------------------------------------
# Fetch helpers
# ---------------------------------------------------------------------------

def fetch_wiki_html(page_title: str, retries: int = 4) -> str | None:
    """Return raw HTML string from Wikisource parse API, or None on failure.
    Retries on 429 with exponential back-off (5s, 10s, 20s, 40s).
    """
    params = urllib.parse.urlencode({
        "action": "parse",
        "page": page_title,
        "prop": "text",
        "format": "json",
        "formatversion": "2",
    })
    url = f"{WIKI_API}?{params}"
    wait = 5
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "BSW-library-bot/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            if "error" in data:
                return None  # page missing (not a rate-limit)
            return data["parse"]["text"]
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries:
                print(f"  [429 rate-limit] waiting {wait}s …")
                time.sleep(wait)
                wait *= 2
                continue
            print(f"  [HTTP {e.code}] {e.reason}")
            return None
        except Exception as e:
            print(f"  [network error] {e}")
            return None
    return None


def chapter_page(part: str, chapter: str) -> str:
    """Build the Wikisource page title for a chapter or prologue."""
    return f"{BASE_PAGE}/Part {part}/{chapter}"


# ---------------------------------------------------------------------------
# HTML cleaning
# ---------------------------------------------------------------------------

def clean_html(raw_html: str) -> str:
    """
    Strip MediaWiki chrome and convert to BSW Library v2-compliant HTML.
    Returns cleaned inner HTML (no section wrapper — caller adds that).
    """
    soup = BeautifulSoup(raw_html, "html.parser")

    # 1. Unwrap outer MediaWiki parser wrappers
    for cls in ("mw-parser-output", "mw-content-ltr", "mw-content-rtl",
                "prp-pages-output"):
        for div in soup.find_all("div", class_=cls):
            div.unwrap()

    # 2. Remove edit-section spans entirely
    for span in soup.find_all("span", class_="mw-editsection"):
        span.decompose()

    # 3. Remove module-wikidata-link spans
    for span in soup.find_all("span", class_="module-wikidata-link"):
        span.decompose()

    # 4. Unwrap mw-heading divs (keep inner heading tag)
    for div in soup.find_all("div", class_=re.compile(r"mw-heading")):
        div.unwrap()

    # 5. Strip id= attributes from headings (mw anchor ids like "Chapter_I")
    for tag in soup.find_all(re.compile(r"^h[1-6]$")):
        if tag.get("id"):
            del tag["id"]

    # 6. Remove page-number markers
    for cls in ("pagenum", "pageno", "pb", "pgmark", "tei-pb", "tei tei-pb"):
        for span in soup.find_all("span", class_=cls):
            span.decompose()
    # Also remove empty anchors used as page markers
    for a in soup.find_all("a"):
        if not a.get_text(strip=True) and not a.find():
            a.decompose()

    # 7. Remove inline style attributes everywhere
    for tag in soup.find_all(style=True):
        del tag["style"]

    # 8. Convert <i> → <em> and <b> → <strong>
    for i_tag in soup.find_all("i"):
        i_tag.name = "em"
    for b_tag in soup.find_all("b"):
        b_tag.name = "strong"

    # 9. Normalise small-caps spans to class="smallcaps"
    for span in soup.find_all("span", class_=re.compile(r"^(smcap|sc|smc|smallcaps)$")):
        span["class"] = ["smallcaps"]

    # 10. Remove dropinitial decorative spans (keep text)
    for span in soup.find_all("span", class_=re.compile(r"dropinitial")):
        span.unwrap()

    # 11. Remove wst-asc / nowrap spans (unwrap)
    for span in soup.find_all("span", class_=re.compile(r"^(wst-asc|nowrap)$")):
        span.unwrap()

    # 12. Remove Wikisource navigation / header / footer divs that are chrome
    #     (categories, noprint, toc, sister-project boxes, etc.)
    chrome_div_ids = {"toc", "catlinks", "mw-normal-catlinks", "mw-hidden-catlinks",
                      "siteNotice", "contentSub", "jump-to-nav"}
    chrome_div_classes = re.compile(
        r"(noprint|mw-indicators|mw-jump-link|printfooter|catlinks|"
        r"sister-project|ws-noexport|mbox|ambox|tmbox|navigation-not-searchable|"
        r"NavFrame|wikitable|toc)"
    )
    for div in soup.find_all("div", id=chrome_div_ids):
        div.decompose()
    for div in soup.find_all("div", class_=chrome_div_classes):
        div.decompose()
    # Also remove <table> elements (Wikisource navboxes, infoboxes)
    for table in soup.find_all("table"):
        table.decompose()

    # 13. Remove Wikisource transclusion cache comment blocks (HTML comments)
    #     BeautifulSoup Comment objects
    from bs4 import Comment
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()

    # 14. Remove <h1> (page title — redundant inside our section)
    for h1 in soup.find_all("h1"):
        h1.decompose()

    # 15. Remove auto-generated class names: c\d{2,} or [a-zA-Z]\d{3,}
    auto_cls_pat = re.compile(r"^([a-zA-Z]\d{3,}|c\d{2,}|i[0-4])$")
    for tag in soup.find_all(class_=True):
        cleaned = [c for c in tag.get("class", []) if not auto_cls_pat.match(c)]
        if cleaned:
            tag["class"] = cleaned
        else:
            del tag["class"]

    # 16. Strip id= from <p> tags
    for p in soup.find_all("p", id=True):
        del p["id"]

    # 17. Collect the cleaned body text — skip empty top-level elements
    parts = []
    for child in soup.children:
        if isinstance(child, NavigableString):
            text = str(child).strip()
            if text:
                parts.append(text)
        elif isinstance(child, Tag):
            rendered = str(child).strip()
            if rendered:
                parts.append(rendered)

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Fetch one part — discovers chapters and accumulates HTML in a single pass
# ---------------------------------------------------------------------------

def fetch_part_all(part_roman: str, max_chapters: int = 50) -> tuple[list[str], str]:
    """
    Fetch Prologue (if present) and Chapter 1…N for a given part.
    Returns (found_keys, concatenated_cleaned_html).
    Each page is fetched only once; no separate probe step.
    Stops after 2 consecutive missing chapter numbers.
    """
    found_keys: list[str] = []
    chunks: list[str] = []

    # Try prologue first
    prologue_title = chapter_page(part_roman, "Prologue")
    print(f"  Fetching: {prologue_title}")
    raw = fetch_wiki_html(prologue_title)
    if raw is not None:
        print(f"    → found prologue")
        found_keys.append("Prologue")
        cleaned = clean_html(raw)
        if cleaned.strip():
            chunks.append(cleaned)
    else:
        print(f"    → no prologue")
    time.sleep(1.5)

    # Fetch chapters
    consecutive_misses = 0
    for n in range(1, max_chapters + 1):
        title = chapter_page(part_roman, f"Chapter {n}")
        print(f"  Fetching: {title}")
        raw = fetch_wiki_html(title)
        if raw is not None:
            print(f"    → found Chapter {n}")
            found_keys.append(f"Chapter {n}")
            cleaned = clean_html(raw)
            if cleaned.strip():
                chunks.append(cleaned)
            consecutive_misses = 0
        else:
            print(f"    → missing")
            consecutive_misses += 1
            if consecutive_misses >= 2:
                break
        time.sleep(1.5)

    return found_keys, "\n".join(chunks)


# ---------------------------------------------------------------------------
# Build section HTML
# ---------------------------------------------------------------------------

def make_section(part_roman: str, body_html: str) -> str:
    heading = PART_TITLES[part_roman]
    return (
        f'<section data-heading="{heading}">'
        f'<h2 class="lib-section__title">{heading}</h2>\n'
        f'{body_html}\n'
        f'</section>'
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=== fetch-gregory.py ===")

    # ── Step 1: Read existing Part IV ──────────────────────────────────────
    print("\n[1] Reading existing Part IV …")
    with open(EXISTING_PART_IV_PATH, encoding="utf-8") as f:
        part_iv_html = f.read().strip()
    print(f"  Part IV: {len(part_iv_html)} chars")

    sections = []

    # ── Step 2: Fetch Parts I and II (known chapter counts) ────────────────
    for part_roman, max_ch in [("I", 11), ("II", 11)]:
        print(f"\n[2] Fetching Part {part_roman} …")
        found_keys, body_html = fetch_part_all(part_roman, max_chapters=max_ch)
        print(f"  Sub-pages found: {found_keys}")
        section = make_section(part_roman, body_html)
        sections.append(section)
        print(f"  Part {part_roman}: {len(body_html)} chars from {len(found_keys)} sub-page(s)")

    # ── Step 3: Fetch Part III (up to 40 chapters) ─────────────────────────
    print("\n[3] Fetching Part III …")
    found_keys_iii, body_html_iii = fetch_part_all("III", max_chapters=40)
    print(f"  Sub-pages found ({len(found_keys_iii)}): {found_keys_iii}")
    section_iii = make_section("III", body_html_iii)
    sections.append(section_iii)
    print(f"  Part III: {len(body_html_iii)} chars from {len(found_keys_iii)} sub-page(s)")

    part_iii_chapter_count = sum(1 for k in found_keys_iii if k.startswith("Chapter"))

    # ── Step 4: Append existing Part IV ────────────────────────────────────
    sections.append(part_iv_html)

    # ── Step 5: Write output ───────────────────────────────────────────────
    output = "\n\n".join(sections) + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"\n[4] Written: {OUTPUT_PATH}")

    # ── Step 6: Stats ──────────────────────────────────────────────────────
    total_chars = len(output)
    # Rough word count: strip tags, count whitespace-separated tokens
    text_only = re.sub(r"<[^>]+>", " ", output)
    words = len(text_only.split())
    print(f"\n=== Summary ===")
    print(f"  Sections written : 4 (Parts I, II, III + existing Part IV)")
    print(f"  Part III chapters: {part_iii_chapter_count}")
    print(f"  Total file size  : {total_chars:,} chars")
    print(f"  Approx word count: {words:,} words")


if __name__ == "__main__":
    main()
