#!/usr/bin/env python3
"""
clean-library-html.py
Multi-mode cleaning script for BSW Library HTML docs.

Usage:
  python3 scripts/clean-library-html.py --mode mediawiki
  python3 scripts/clean-library-html.py --mode ccel
  python3 scripts/clean-library-html.py --mode gutenberg
  python3 scripts/clean-library-html.py --mode tags
  python3 scripts/clean-library-html.py --mode artifacts
  python3 scripts/clean-library-html.py --mode json-sections

  --mode artifacts   Strip remaining source chrome across ALL HTML docs:
    - dropinitial* spans (decorative drop caps) — unwrap, keep text
    - smcap / sc / smc spans — convert to <span class="smallcaps">
    - pageno / pb / pgmark spans — remove entirely (page markers)
    - tei-noteref spans — remove (TEI footnote ref artefacts)
    - NoteRef / Note / Footnote / mnote — remove (CCEL footnote chrome)
    - GutSmall — unwrap (already a tag mode pass, belt-and-suspenders)
    - indexpageno / blackletter — remove
    - module-wikidata-link / nowrap spans — unwrap
    - ws-poem-break / ws-poem-line — unwrap
    - Auto-generated class names (c014, c007, i2…) stripped from p/td/a
    - <hr> elements removed
    Deliberately NOT touched: wst-* classes (styled by library.css)
"""

import argparse
import json
import os
import re
import sys
from bs4 import BeautifulSoup, NavigableString, Tag

HTML_DIR = "data/library/html"
JSON_DIR = "data/library/docs"

# ── Doc lists ────────────────────────────────────────────────────────────────

MEDIAWIKI_DOCS = [
    "ambrose-on-duties", "anselm-cur-deus-homo", "apostolic-constitutions",
    "aristides-apology", "athanasius-life-of-antony",
    "athanasius-on-incarnation", "athenagoras-writings", "augustine-city-of-god",
    "augustine-confessions", "augustine-on-christian-doctrine", "augustine-on-trinity",
    "basil-on-holy-spirit", "book-of-common-prayer", "brother-lawrence-practice",
    "calvin-institutes-book1",
    "cassian-conferences", "chesterton-heretics", "chesterton-orthodoxy",
    "chrysostom-homilies-acts",
    "chrysostom-on-priesthood", "cloud-of-unknowing", "cyril-catechetical-lectures",
    "eusebius-church-history", "francis-of-assisi-writings", "gregory-great-pastoral-rule",
    "gregory-nazianzus-orations", "gregory-nyssa-great-catechism", "gregory-palamas-texts",
    "imitation-of-christ", "irenaeus-against-heresies", "john-of-damascus-exposition",
    "john-of-cross-dark-night", "kuyper-calvinism", "leo-sermons",
    "machen-christianity-liberalism", "maximus-confessor-texts", "minucius-felix-octavius",
    "origen-against-celsus",
    "origen-de-principiis", "owen-mortification", "pilgrims-progress",
    "roman-catechism", "ryle-holiness", "shepherd-of-hermas",
    "spurgeon-all-of-grace", "symeon-new-theologian-texts", "teresa-interior-castle",
    "tertullian-apology", "tertullian-prescription", "wesley-sermons",
]

CCEL_DOCS = [
    "baxter-reformed-pastor", "benedict-rule", "bernard-on-loving-god",
    "catherine-dialogue", "edwards-freedom-of-will", "edwards-religious-affections",
    "francis-de-sales-devout-life", "ignatius-spiritual-exercises", "julian-revelations",
    "luther-bondage-of-will", "meister-eckhart-sermons", "pseudo-dionysius-works",
    "taylor-holy-living", "whitefield-sermons", "william-law-serious-call",
]

GUTENBERG_DOCS = [
    "boethius-consolation", "bunyan-holy-war", "butler-analogy",
    "chesterton-everlasting-man",
    "calvin-institutes-vol2", "pascal-pensees", "paley-natural-theology",
    "brainerd-journal", "carey-enquiry",
]


# ── Tag cleanup (shared across all modes) ────────────────────────────────────

def replace_i_with_em(soup):
    """Replace all <i> tags with <em>, preserving children."""
    for tag in soup.find_all("i"):
        em = soup.new_tag("em")
        for child in list(tag.children):
            em.append(child.extract())
        tag.replace_with(em)


def replace_b_with_strong(soup):
    """Replace all <b> tags with <strong>, preserving children."""
    for tag in soup.find_all("b"):
        strong = soup.new_tag("strong")
        for child in list(tag.children):
            strong.append(child.extract())
        tag.replace_with(strong)


def remove_style_attrs(soup):
    """Remove all style= attributes from all tags (including empty style='')."""
    for tag in soup.find_all(True):
        if 'style' in tag.attrs:
            del tag["style"]


def remove_pagenum_elements(soup):
    """Remove <span class="pagenum"> and elements with tei-pb class."""
    for el in soup.find_all(class_="pagenum"):
        el.decompose()
    for el in soup.find_all(class_=re.compile(r"tei-pb")):
        el.decompose()
    # Also remove <hr class="page">
    for el in soup.find_all("hr", class_="page"):
        el.decompose()


def remove_empty_anchors(soup):
    """Remove <a id="..."> with no href and no meaningful text."""
    for a in soup.find_all("a"):
        if a.get("id") and not a.get("href") and not a.get_text(strip=True):
            a.decompose()


def remove_id_from_p(soup):
    """Remove id= attributes from <p> tags."""
    for p in soup.find_all("p"):
        if p.get("id"):
            del p["id"]


def apply_tag_rules(soup):
    """Apply all tag-level cleanup rules to a soup object."""
    replace_i_with_em(soup)
    replace_b_with_strong(soup)
    remove_style_attrs(soup)
    remove_pagenum_elements(soup)
    remove_empty_anchors(soup)
    remove_id_from_p(soup)


# ── MediaWiki mode ───────────────────────────────────────────────────────────

def clean_mediawiki(soup):
    """
    Unwrap mw-content-ltr/mw-parser-output divs, replace mw-heading divs
    with their heading children, remove mw-editsection spans, and strip
    id attributes from headings. Preserves existing section boundaries.
    """
    # Unwrap the mw-parser-output div — replace div with its children in-place.
    # We do this on ALL matching divs (sometimes nested).
    for mw_div in soup.find_all("div", class_=re.compile(r"mw-parser-output")):
        mw_div.unwrap()

    # Replace <div class="mw-heading ..."> with just the heading tag inside
    for mw_heading_div in soup.find_all("div", class_=re.compile(r"mw-heading")):
        # Find the heading child (h1-h6)
        heading_child = mw_heading_div.find(re.compile(r"^h[1-6]$"))
        if heading_child:
            mw_heading_div.replace_with(heading_child)
        else:
            mw_heading_div.unwrap()

    # Remove mw-editsection spans entirely
    for span in soup.find_all("span", class_="mw-editsection"):
        span.decompose()

    # Remove id attributes from heading tags (they contain anchors like "Chapter_I")
    for h in soup.find_all(re.compile(r"^h[1-6]$")):
        if h.get("id"):
            del h["id"]

    apply_tag_rules(soup)


# ── CCEL mode ────────────────────────────────────────────────────────────────

def clean_ccel(soup):
    """
    Remove ccel.org links, unwrap book-font-* divs, remove spacers,
    strip numeric id attrs from headings, strip Normal/Default p classes.
    """
    # Remove <a href="...ccel.org..."> — keep text content
    for a in soup.find_all("a", href=True):
        if "ccel.org" in a["href"]:
            # Replace the anchor with its text content (unwrap)
            a.unwrap()

    # Unwrap divs with CCEL wrapper classes
    ccel_class_pattern = re.compile(
        r"book-font-size-malleable|book-font-family|book-theme-malleable"
    )
    # Collect first, then unwrap to avoid mutation during iteration
    for div in soup.find_all("div", class_=ccel_class_pattern):
        div.unwrap()

    # Remove spacer divs
    for div in soup.find_all("div", class_="spacer"):
        div.decompose()

    # Remove numeric id attrs (e.g., id="i-p0.1") from heading tags
    id_pattern = re.compile(r"^[a-zA-Z0-9._-]+-p\d+\.\d+$|^i-p")
    for h in soup.find_all(re.compile(r"^h[1-6]$")):
        if h.get("id") and re.match(r"^[a-z0-9._-]*[.-]?p\d", h["id"]):
            del h["id"]

    # Strip class="Normal" and class="Default" from <p> tags
    for p in soup.find_all("p"):
        classes = p.get("class", [])
        new_classes = [c for c in classes if c not in ("Normal", "Default", "Body")]
        if new_classes:
            p["class"] = new_classes
        elif "class" in p.attrs:
            del p["class"]

    apply_tag_rules(soup)


# ── Gutenberg mode ───────────────────────────────────────────────────────────

GUTENBERG_REMOVE_PATTERNS = [
    re.compile(r"project gutenberg", re.IGNORECASE),
    re.compile(r"transcribed from", re.IGNORECASE),
    re.compile(r"transcriber", re.IGNORECASE),
]


def clean_gutenberg(soup):
    """
    Remove Project Gutenberg boilerplate paragraphs, gapspace divs,
    GutSmall spans (unwrap), and <hr> elements.
    """
    # Remove paragraphs containing Gutenberg/transcriber text
    for p in soup.find_all("p"):
        text = p.get_text()
        if any(pat.search(text) for pat in GUTENBERG_REMOVE_PATTERNS):
            p.decompose()

    # Remove <div class="gapspace"> elements
    for div in soup.find_all("div", class_="gapspace"):
        div.decompose()

    # Unwrap <span class="GutSmall"> (keep text)
    for span in soup.find_all("span", class_="GutSmall"):
        span.unwrap()

    # Remove <hr> elements
    for hr in soup.find_all("hr"):
        hr.decompose()

    apply_tag_rules(soup)


# ── Artifacts mode (all 103 HTML docs) ──────────────────────────────────────

# Classes to strip entirely (element removed, no text kept)
_STRIP_CLASSES = {
    "pageno", "pb", "pgmark",           # page markers (W-PAGE)
    "tei-noteref",                       # TEI footnote refs
    "NoteRef", "Note", "Footnote",       # CCEL footnote chrome
    "mnote",                             # CCEL margin notes
    "indexpageno",                       # index page numbers
    "blackletter", "blackletter-mode-",  # display-only formatting
}

# Classes to unwrap (remove tag, keep inner text/children)
_UNWRAP_CLASSES = {
    "dropinitial", "drop-initial-image", "dropinitial-image",
    "dropinitial-initial", "dropinitial-mid", "dropinitial-fl",
    "GutSmall",
    "module-wikidata-link",
    "nowrap",
    "ws-poem-break", "ws-poem-line",
}

# Classes to convert to <span class="smallcaps">
_SMALLCAPS_CLASSES = {"smcap", "sc", "smc"}

# Pattern for auto-generated CSS class names from source converters
_AUTO_CLASS_RE = re.compile(r"^c\d{2,}$|^[a-zA-Z]\d{3,}$|^i[0-9]$")

# Classes on block elements that are safe to strip (default/normal paragraphs)
_STRIP_P_CLASSES = {"Normal", "Default", "Body", "normal"}


def clean_artifacts(soup):
    """
    Strip remaining source-chrome artifacts across all docs.
    Safe to run repeatedly — idempotent.

    Each step does a fresh soup.find_all() to avoid acting on already-decomposed
    tags (decomposing a parent also kills its children in the BS4 tree).
    """
    # 1. Strip elements whose class intersects _STRIP_CLASSES (remove entirely)
    for tag in list(soup.find_all(True)):
        if tag.attrs is None:
            continue
        classes = set(tag.get("class") or [])
        if classes & _STRIP_CLASSES:
            tag.decompose()

    # 2. Unwrap elements whose class intersects _UNWRAP_CLASSES (keep children)
    for tag in list(soup.find_all(True)):
        if tag.attrs is None:
            continue
        classes = set(tag.get("class") or [])
        if classes & _UNWRAP_CLASSES:
            tag.unwrap()

    # 3. Convert smcap/sc/smc spans to <span class="smallcaps">
    for tag in list(soup.find_all(True)):
        if tag.attrs is None:
            continue
        classes = set(tag.get("class") or [])
        if classes & _SMALLCAPS_CLASSES:
            tag["class"] = ["smallcaps"]

    # 4. Strip auto-generated class names from block/inline and heading elements
    for tag in soup.find_all(["p", "td", "th", "a", "span", "div",
                               "h1", "h2", "h3", "h4", "h5", "h6"]):
        if tag.attrs is None:
            continue
        classes = tag.get("class") or []
        new_classes = [c for c in classes if not _AUTO_CLASS_RE.match(c)]
        if new_classes != classes:
            if new_classes:
                tag["class"] = new_classes
            elif "class" in tag.attrs:
                del tag["class"]

    # 5. Strip default-paragraph classes from <p> tags
    for p in soup.find_all("p"):
        if p.attrs is None:
            continue
        classes = p.get("class") or []
        new_classes = [c for c in classes if c not in _STRIP_P_CLASSES]
        if new_classes != classes:
            if new_classes:
                p["class"] = new_classes
            elif "class" in p.attrs:
                del p["class"]

    # 6. Remove <hr> elements (section structure is carried by <section> tags)
    for hr in list(soup.find_all("hr")):
        hr.decompose()


def clean_artifacts_all():
    """Apply artifact cleanup to every HTML doc in HTML_DIR."""
    html_files = sorted(
        os.path.join(HTML_DIR, f)
        for f in os.listdir(HTML_DIR)
        if f.endswith(".html")
    )
    changed = 0
    for path in html_files:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        soup = BeautifulSoup(raw, "html.parser")
        clean_artifacts(soup)
        result = str(soup)
        if result != raw:
            with open(path, "w", encoding="utf-8") as f:
                f.write(result)
            docid = os.path.basename(path).replace(".html", "")
            print(f"  artifacts  {docid}")
            changed += 1

    print(f"\nDone: {len(html_files)} files checked, {changed} modified")


# ── JSON sections mode ───────────────────────────────────────────────────────

def apply_tag_rules_to_html_string(html_str):
    """Apply tag cleanup rules to an HTML string and return cleaned string."""
    soup = BeautifulSoup(html_str, "html.parser")
    apply_tag_rules(soup)
    return str(soup)


def clean_json_sections():
    """Apply tag cleanup to HTML content in all JSON doc files."""
    json_files = sorted(
        f for f in os.listdir(JSON_DIR) if f.endswith(".json")
    )
    total = 0
    for fname in json_files:
        path = os.path.join(JSON_DIR, fname)
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        modified = False
        sections = data.get("sections", [])
        for sec in sections:
            if "html" in sec:
                cleaned = apply_tag_rules_to_html_string(sec["html"])
                if cleaned != sec["html"]:
                    sec["html"] = cleaned
                    modified = True

        if modified:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  cleaned  {fname}")
        else:
            print(f"  ok       {fname}")
        total += 1

    print(f"\nDone: processed {total} JSON files")


# ── Tags-only mode (all 103 HTML docs) ──────────────────────────────────────

def clean_tags_all():
    """Apply tag rules to every HTML doc."""
    html_files = sorted(
        os.path.join(HTML_DIR, f)
        for f in os.listdir(HTML_DIR)
        if f.endswith(".html")
    )
    for path in html_files:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        soup = BeautifulSoup(raw, "html.parser")
        apply_tag_rules(soup)
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        docid = os.path.basename(path).replace(".html", "")
        print(f"  tags     {docid}")

    print(f"\nDone: processed {len(html_files)} HTML files")

    # Verify <i> count drops to 0
    i_total = 0
    for path in html_files:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        soup = BeautifulSoup(raw, "html.parser")
        i_total += len(soup.find_all("i"))
    print(f"Post-tags <i> count: {i_total} (should be 0)")


# ── Main ─────────────────────────────────────────────────────────────────────

def process_html_doc(docid, clean_fn, mode_name):
    path = os.path.join(HTML_DIR, docid + ".html")
    if not os.path.exists(path):
        print(f"  MISSING  {docid}")
        return
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    soup = BeautifulSoup(raw, "html.parser")
    clean_fn(soup)
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"  {mode_name:<12} {docid}")


def main():
    parser = argparse.ArgumentParser(description="Clean BSW Library HTML docs")
    parser.add_argument(
        "--mode",
        choices=["mediawiki", "ccel", "gutenberg", "tags", "artifacts", "json-sections"],
        required=True,
        help="Cleaning mode to apply",
    )
    args = parser.parse_args()

    if args.mode == "mediawiki":
        print(f"Running mediawiki mode on {len(MEDIAWIKI_DOCS)} docs...")
        for docid in MEDIAWIKI_DOCS:
            process_html_doc(docid, clean_mediawiki, "mediawiki")
        print(f"\nDone: {len(MEDIAWIKI_DOCS)} docs cleaned")

    elif args.mode == "ccel":
        print(f"Running ccel mode on {len(CCEL_DOCS)} docs...")
        for docid in CCEL_DOCS:
            process_html_doc(docid, clean_ccel, "ccel")
        print(f"\nDone: {len(CCEL_DOCS)} docs cleaned")

    elif args.mode == "gutenberg":
        print(f"Running gutenberg mode on {len(GUTENBERG_DOCS)} docs...")
        for docid in GUTENBERG_DOCS:
            process_html_doc(docid, clean_gutenberg, "gutenberg")
        print(f"\nDone: {len(GUTENBERG_DOCS)} docs cleaned")

    elif args.mode == "tags":
        print("Running tags mode on ALL 103 HTML docs...")
        clean_tags_all()

    elif args.mode == "artifacts":
        print("Running artifacts mode on ALL HTML docs...")
        clean_artifacts_all()

    elif args.mode == "json-sections":
        print("Running json-sections mode on all JSON docs...")
        clean_json_sections()


if __name__ == "__main__":
    main()
