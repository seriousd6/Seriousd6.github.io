#!/usr/bin/env python3
r"""
validate-library-format.py
Checks each HTML doc in data/library/html/ against BSW Library HTML v2 format rules.

FAIL rules (R-prefix) -- must fix before indexing:
  R1   Root contains non-section elements or unstripped MediaWiki/CCEL wrappers
  R3   Section's first child is not <hN class="lib-section__title">
  R5   Any style="" attributes (inline styles)
  R6   Deprecated <i> or <b> tags
  R7   Source chrome: MediaWiki divs, CCEL wrappers, Gutenberg boilerplate
  R8   Page-number markers: pagenum, tei-pb, [Pg N] patterns
  R11  Hollow sections: no <p> element and text < 600 chars
  R12  Near-empty document: total text < 1,000 words

WARN rules (W-prefix) -- flag for cleanup, do not block:
  W9       Empty <a id="..."> anchor targets
  W10      Under-split: >100KB file with <=3 sections
  W-BR     More than 20 <br> elements (use <p> instead)
  W-HR     Any <hr> elements present
  W-PAGE   Remaining page markers: pageno, pb, pgmark
  W-CHROME Source-chrome classes with no CSS support (dropinitial*, smcap, sc,
            smc, NoteRef, Footnote, mnote, GutSmall, indexpageno, tei-noteref)
  W-AUTO   Auto-generated class names matching c\d{2,} or [a-zA-Z]\d{3,}

Usage:
  python3 scripts/validate-library-format.py --all
  python3 scripts/validate-library-format.py --all --warn
  python3 scripts/validate-library-format.py <docid> [<docid> ...] --warn
"""

import argparse
import os
import re
import sys
from bs4 import BeautifulSoup

HTML_DIR = "data/library/html"

HEADING_PAT = re.compile(r"^h[1-6]$")

# Source-chrome classes that have no CSS support and indicate un-cleaned HTML.
# wst-* classes are intentionally excluded here — they have CSS in library.css.
CHROME_CLASSES = {
    "dropinitial", "dropinitial-image", "dropinitial-initial",
    "dropinitial-mid", "dropinitial-fl", "drop-initial-image",
    "smcap", "sc", "smc",
    "NoteRef", "Note", "Footnote", "mnote",
    "GutSmall", "indexpageno", "blackletter", "blackletter-mode-",
    "tei-noteref",
    # These are distinct from wst-* functional classes — ws-poem is Wikisource UI
    "ws-poem-break", "ws-poem-line",
    "module-wikidata-link",
}

# Auto-generated class pattern from source converters (c014, c007, i2, i4, etc.)
AUTO_CLASS_PAT = re.compile(r"^c\d{2,}$|^[a-zA-Z]\d{3,}$|^i[0-9]$")


def validate_file(path, check_warnings=False):
    """Return (fail_bool, fail_list, warn_list) for one file.

    fail_bool is True when there are FAIL-level violations.
    fail_list  — FAIL violations (R-rules)
    warn_list  — WARN violations (W-rules), only populated when check_warnings=True
    """
    fails = []
    warns = []
    size = os.path.getsize(path)

    with open(path, encoding="utf-8") as f:
        raw = f.read()

    soup = BeautifulSoup(raw, "html.parser")
    sections = soup.find_all("section", attrs={"data-heading": True})

    # ── R1: Root contains non-section elements ──────────────────────────────
    mw_output = soup.find(class_="mw-parser-output")
    if mw_output:
        fails.append("[R1] mw-parser-output div found (MediaWiki wrapper not unwrapped)")
    book_font = soup.find(class_=re.compile(r"book-font-size"))
    if book_font:
        fails.append("[R1] book-font-size div found (CCEL wrapper not unwrapped)")
    root_divs = [c for c in soup.children if getattr(c, "name", None) == "div"]
    if root_divs:
        fails.append(f"[R1] {len(root_divs)} <div> element(s) at root level")

    # ── R3: First section child not <hN class="lib-section__title"> ────────
    bad_r3 = 0
    for sec in sections:
        first = next((c for c in sec.children if getattr(c, "name", None)), None)
        if first is None or not HEADING_PAT.match(first.name) \
                or "lib-section__title" not in first.get("class", []):
            bad_r3 += 1
    if bad_r3:
        fails.append(f"[R3] {bad_r3} section(s) whose first child is not <hN class=\"lib-section__title\">")

    # ── R5: Inline styles ───────────────────────────────────────────────────
    style_count = len(re.findall(r"\bstyle=", raw))
    if style_count:
        fails.append(f"[R5] {style_count} inline style= attribute(s) found")

    # ── R6: Deprecated tags ─────────────────────────────────────────────────
    i_count = len(soup.find_all("i"))
    b_count = len(soup.find_all("b"))
    if i_count or b_count:
        fails.append(f"[R6] Deprecated tags: {i_count} <i>, {b_count} <b>")

    # ── R7: External chrome ─────────────────────────────────────────────────
    if soup.find(class_=re.compile(r"mw-heading")):
        fails.append("[R7] MediaWiki mw-heading div(s) found")
    if soup.find(class_="mw-editsection"):
        fails.append("[R7] MediaWiki mw-editsection span(s) found")
    if soup.find(class_=re.compile(r"book-font-size-malleable|ccel")):
        fails.append("[R7] CCEL wrapper class(es) found")
    ccel_links = [a for a in soup.find_all("a", href=True) if "ccel.org" in a["href"]]
    if ccel_links:
        fails.append(f"[R7] {len(ccel_links)} ccel.org link(s) found")
    if "PROJECT GUTENBERG" in raw.upper():
        fails.append("[R7] Project Gutenberg boilerplate text found")

    # ── R8: Page-number markers ─────────────────────────────────────────────
    if soup.find(class_="pagenum"):
        fails.append('[R8] class="pagenum" element(s) found')
    if soup.find(class_=re.compile(r"tei.*tei-pb|tei-pb")):
        fails.append('[R8] class="tei tei-pb" element(s) found')
    pg_markers = re.findall(r"\[Pg\s+\d+\]", raw)
    if pg_markers:
        fails.append(f"[R8] {len(pg_markers)} [Pg N] page marker(s) found")

    # ── R11: Hollow sections ─────────────────────────────────────────────────
    # A section is hollow if it has no <p> children and its total text is < 600 chars.
    # This catches structural-divider stubs and empty TOC placeholder sections.
    hollow = []
    for sec in sections:
        if sec.find_parent("section"):
            continue  # skip nested sections
        if not sec.find("p") and not sec.find("div") and not sec.find("table"):
            text_len = len(sec.get_text(" ", strip=True))
            if text_len < 600:
                hollow.append(sec.get("data-heading", "")[:50])
    if hollow:
        sample = hollow[:3]
        extra = f" (+ {len(hollow) - 3} more)" if len(hollow) > 3 else ""
        fails.append(
            f"[R11] {len(hollow)} hollow section(s) with no <p> and text <600 chars: "
            f"{sample}{extra}"
        )

    # ── R12: Near-empty document ─────────────────────────────────────────────
    # Total text under ~1,000 words indicates missing content (cassian/julian problem).
    total_text = soup.get_text(" ", strip=True)
    word_count = len(total_text.split())
    if word_count < 1000:
        fails.append(
            f"[R12] Near-empty document: only ~{word_count} words "
            f"(expected ≥1,000 for a substantive work)"
        )

    # ── W9: Empty anchor targets ────────────────────────────────────────────
    if check_warnings:
        empty_anchors = [
            a for a in soup.find_all("a")
            if a.get("id") and not a.get("href") and not a.get_text(strip=True)
        ]
        if empty_anchors:
            warns.append(f"[W9] {len(empty_anchors)} empty <a id=\"...\"> anchor target(s)")

    # ── W10: Under-split ────────────────────────────────────────────────────
    if check_warnings and size > 100_000 and len(sections) <= 3:
        warns.append(
            f"[W10] Under-split: {size // 1024}KB file with only {len(sections)} section(s)"
        )

    # ── W-BR: Excessive <br> elements ───────────────────────────────────────
    if check_warnings:
        br_count = len(soup.find_all("br"))
        if br_count > 20:
            warns.append(f"[W-BR] {br_count} <br> elements (use <p> tags instead)")

    # ── W-HR: Any <hr> elements ─────────────────────────────────────────────
    if check_warnings:
        hr_count = len(soup.find_all("hr"))
        if hr_count:
            warns.append(f"[W-HR] {hr_count} <hr> element(s) found (use section boundaries)")

    # ── W-PAGE: Remaining page markers not caught by R8 ────────────────────
    if check_warnings:
        page_classes = {"pageno", "pb", "pgmark"}
        page_hits = []
        for el in soup.find_all(True):
            for cls in el.get("class", []):
                if cls in page_classes:
                    page_hits.append(cls)
        if page_hits:
            from collections import Counter
            summary = dict(Counter(page_hits).most_common(4))
            warns.append(f"[W-PAGE] Page-marker classes found: {summary}")

    # ── W-CHROME: Unsupported source-chrome classes ─────────────────────────
    if check_warnings:
        chrome_found = {}
        for el in soup.find_all(True):
            for cls in el.get("class", []):
                if cls in CHROME_CLASSES:
                    chrome_found[cls] = chrome_found.get(cls, 0) + 1
        if chrome_found:
            from collections import Counter
            top = dict(Counter(chrome_found).most_common(5))
            total_chrome = sum(chrome_found.values())
            warns.append(
                f"[W-CHROME] {total_chrome} unsupported source-chrome class(es): {top}"
            )

    # ── W-AUTO: Auto-generated class names ──────────────────────────────────
    if check_warnings:
        auto_count = 0
        for el in soup.find_all(True):
            for cls in el.get("class", []):
                if AUTO_CLASS_PAT.match(cls):
                    auto_count += 1
        if auto_count:
            warns.append(
                f"[W-AUTO] {auto_count} auto-generated class name(s) "
                f"(e.g. c014, c007 — strip these)"
            )

    failed = len(fails) > 0
    return failed, fails, warns


def main():
    parser = argparse.ArgumentParser(
        description="Validate BSW Library HTML format (v2)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Check all docs in data/library/html/",
    )
    parser.add_argument(
        "--warn", action="store_true",
        help="Also show WARN-level findings (W-rules)",
    )
    parser.add_argument(
        "docs", nargs="*",
        help="Doc IDs to check (without .html extension)",
    )
    args = parser.parse_args()

    if args.all:
        files = sorted(
            os.path.join(HTML_DIR, f)
            for f in os.listdir(HTML_DIR)
            if f.endswith(".html")
        )
    else:
        if not args.docs:
            parser.print_help()
            sys.exit(1)
        files = [os.path.join(HTML_DIR, d + ".html") for d in args.docs]

    total = len(files)
    n_pass = 0
    n_fail = 0
    n_warn_only = 0

    for fpath in files:
        docid = os.path.basename(fpath).replace(".html", "")
        if not os.path.exists(fpath):
            print(f"MISSING  {docid}")
            n_fail += 1
            continue

        failed, fails, warns = validate_file(fpath, check_warnings=args.warn)

        if failed:
            print(f"FAIL     {docid}")
            for v in fails:
                print(f"         {v}")
            if warns:
                for w in warns:
                    print(f"         {w}")
            n_fail += 1
        elif warns:
            print(f"WARN     {docid}")
            for w in warns:
                print(f"         {w}")
            n_warn_only += 1
            n_pass += 1
        else:
            print(f"PASS     {docid}")
            n_pass += 1

    print(f"\n{'='*60}")
    summary = f"Total: {total}  |  PASS: {n_pass}  |  FAIL: {n_fail}"
    if args.warn and n_warn_only:
        summary += f"  (WARN-only: {n_warn_only})"
    print(summary)


if __name__ == "__main__":
    main()
