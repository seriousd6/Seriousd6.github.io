#!/usr/bin/env python3
"""
resection-library-html.py
Splits a single HTML doc at heading boundaries into proper
<section data-heading="..."> elements with the correct first child.

Usage:
  python3 scripts/resection-library-html.py <docid> --heading h2
  python3 scripts/resection-library-html.py <docid> --heading h3
  python3 scripts/resection-library-html.py <docid> --multi h2,h3
  python3 scripts/resection-library-html.py <docid> --heading h1
"""

import argparse
import os
import re
import sys
from bs4 import BeautifulSoup, NavigableString, Tag

HTML_DIR = "data/library/html"


def get_heading_text(tag):
    """Return clean text of a heading element."""
    # Remove any leading/trailing whitespace and normalise internal whitespace
    return " ".join(tag.get_text().split())


def build_section(soup, heading_text, heading_level, content_tags):
    """
    Create a <section data-heading="..."> element containing:
      - <hN class="lib-section__title">heading_text</hN>
      - ...remaining content_tags
    """
    section = soup.new_tag("section", attrs={"data-heading": heading_text})

    # First child: heading with the lib-section__title class
    h_tag = soup.new_tag(heading_level, attrs={"class": "lib-section__title"})
    h_tag.string = heading_text
    section.append(h_tag)

    # Remaining content
    for item in content_tags:
        section.append(item)

    return section


def resection(docid, heading_levels):
    """
    Main resectioning logic.
    heading_levels: list of tag names to split on, e.g. ['h2'] or ['h2','h3'] or ['h1']
    """
    path = os.path.join(HTML_DIR, docid + ".html")
    if not os.path.exists(path):
        print(f"ERROR: {path} not found")
        sys.exit(1)

    with open(path, encoding="utf-8") as f:
        raw = f.read()

    soup = BeautifulSoup(raw, "html.parser")

    # Flatten all top-level content into a single ordered list.
    # We need to handle two cases:
    #   (A) File already has <section data-heading="..."> wrappers — flatten them
    #       into their children first, then re-split.
    #   (B) File is flat content at the top level.

    def deep_flatten(nodes, out):
        """
        Recursively flatten all <section> elements so that all leaf content
        (headings and body elements) end up in a single flat list.

        - <section data-heading="..."> (our BSW wrapper): unwrap, recurse into
          children so the heading tag is re-available for grouping.
        - <section> without data-heading (e.g. Gutenberg source sections): also
          unwrap and recurse, so nested content becomes top-level.
        """
        for node in nodes:
            if isinstance(node, Tag) and node.name == "section":
                # Unwrap all sections — both our BSW sections and raw source sections.
                children = list(node.children)
                for c in children:
                    c.extract()
                deep_flatten(children, out)
            else:
                if isinstance(node, Tag):
                    out.append(node.extract())
                else:
                    out.append(node)

    all_children = []
    deep_flatten(list(soup.children), all_children)

    # Now group by heading boundaries.
    # A heading is any element whose tag name is in heading_levels.
    heading_set = set(heading_levels)

    sections = []       # list of (heading_text, heading_level, content_nodes)
    pre_heading = []    # nodes before the first heading

    current_heading_text = None
    current_heading_level = None
    current_content = []

    def is_heading(node):
        return isinstance(node, Tag) and node.name in heading_set

    for node in all_children:
        if is_heading(node):
            if current_heading_text is not None:
                # Save the current section
                sections.append((current_heading_text, current_heading_level, current_content))
            elif pre_heading:
                # We had some content before the first heading; save as Preface
                # Only if non-empty (not just whitespace NavigableStrings)
                meaningful = [
                    n for n in pre_heading
                    if isinstance(n, Tag) or (isinstance(n, NavigableString) and n.strip())
                ]
                if meaningful:
                    sections.append(("Preface", current_heading_level or heading_levels[0], pre_heading))
                pre_heading = []
            current_heading_text = get_heading_text(node)
            current_heading_level = node.name
            current_content = []
        else:
            if current_heading_text is None:
                pre_heading.append(node)
            else:
                current_content.append(node)

    # Don't forget the last section
    if current_heading_text is not None:
        sections.append((current_heading_text, current_heading_level, current_content))
    elif pre_heading:
        # File had no headings at all — keep as single "Preface" section
        meaningful = [
            n for n in pre_heading
            if isinstance(n, Tag) or (isinstance(n, NavigableString) and n.strip())
        ]
        if meaningful:
            sections.append(("Preface", heading_levels[0], pre_heading))

    if not sections:
        print(f"  {docid}: WARNING — no sections found, file unchanged")
        return 0

    # Build a new soup with just the sections
    new_soup = BeautifulSoup("", "html.parser")
    for heading_text, heading_level, content in sections:
        # Filter out pure-whitespace NavigableStrings from content
        clean_content = [
            n for n in content
            if isinstance(n, Tag) or (isinstance(n, NavigableString) and n.strip())
        ]
        section_tag = build_section(new_soup, heading_text, heading_level, clean_content)
        new_soup.append(section_tag)
        new_soup.append(NavigableString("\n"))

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(new_soup))

    count = len(sections)
    print(f"  {docid}: {count} sections")
    return count


def main():
    parser = argparse.ArgumentParser(
        description="Resection a library HTML doc at heading boundaries"
    )
    parser.add_argument("docid", help="Doc ID (without .html extension)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--heading",
        help="Single heading level to split on (e.g. h2, h3, h1)",
    )
    group.add_argument(
        "--multi",
        help="Comma-separated heading levels (e.g. h2,h3)",
    )
    args = parser.parse_args()

    if args.heading:
        levels = [args.heading.lower()]
    else:
        levels = [h.strip().lower() for h in args.multi.split(",")]

    count = resection(args.docid, levels)
    return 0 if count > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
