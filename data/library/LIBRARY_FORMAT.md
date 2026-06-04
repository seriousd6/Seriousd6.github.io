# BSW Library HTML Format Standard — v2

This file is the canonical reference for library document format. All HTML-path
docs in `data/library/html/` and section `.html` fields inside JSON-path docs in
`data/library/docs/` must conform to this standard.

Scripts that produce or transform library docs must output v2-compliant HTML.
`scripts/validate-library-format.py --all` enforces the rules below.

---

## 1. File root structure

A compliant HTML file is a bare sequence of `<section data-heading="...">` elements.
No `<html>`, `<head>`, `<body>`, or any wrapping `<div>` is present.

```html
<section data-heading="Chapter I — Title">
  <h2 class="lib-section__title">Chapter I — Title</h2>
  <p>Body text…</p>
</section>

<section data-heading="Chapter II — Next Title">
  <h2 class="lib-section__title">Chapter II — Next Title</h2>
  …
</section>
```

**Rules:**
- Every root-level element is `<section data-heading="...">` — no `<div>`, `<p>`, or other elements at root
- `data-heading` value is plain text only (no HTML tags; only `&amp;`, `&lt;`, `&gt;` entities)
- `data-heading` must match the text content of the section's first `<h2>` exactly
- The first child of every section is `<h2 class="lib-section__title">` (or `<h3>` for sub-works)
- Sections are substantive navigable units: chapter, homily, lecture, sermon, Q&A group, or conference
- Minimum 500 characters of prose text per section (see R11)
- Maximum ~100,000 characters per section; split large sections further

---

## 2. Allowed block elements

| Element | Class | Usage |
|---|---|---|
| `<p>` | (none) | Body paragraphs — the primary content container |
| `<p>` | `lib-center` | Centred text (attribution, titles, epigraphs) |
| `<p>` | `lib-verse` | Individual verse lines in poetry sections |
| `<blockquote>` | `scripture` | Extended Bible quotations rendered in the reader |
| `<blockquote>` | `lib-quote` | Extended non-scripture quotations |
| `<ul>`, `<ol>`, `<li>` | (none) | Lists |
| `<h3>` | (none) | In-section sub-headings (not section boundaries) |
| `<h4>` | (none) | Deeper sub-headings |
| `<aside>` | `lib-fn` | Scholarly footnote (full text, not just a marker) |
| `<table>` | `lib-table` | Tabular data only (catechism Q&A, comparison tables) |
| `<div>` | `stanza` | Poetry stanza wrapper (contains `<p class="lib-verse">`) |

No other block elements are allowed. In particular: `<center>`, `<hr>`, `<pre>`,
`<address>`, `<figure>`, `<figcaption>` are not allowed.

---

## 3. Allowed inline elements

| Element | Class | Usage |
|---|---|---|
| `<em>` | (none) | Emphasis (replaces `<i>`) |
| `<strong>` | (none) | Strong emphasis (replaces `<b>`) |
| `<sup>` | (none) | Superscript (footnote markers, ordinals) |
| `<a>` | `ref` + `data-ref="Book Ch:V"` | Bible reference link |
| `<span>` | `smallcaps` | Small-caps rendering |
| `<span>` | `lib-fn__marker` | Inline footnote marker linked to an `<aside class="lib-fn">` |
| `<span>` | `wst-verse` | Verse/thesis number label (Didache, Luther 95 Theses) |
| `<span>` | `wst-verse-default` | Same as above (legacy variant) |
| `<span>` | `wst-anchor` | Section/paragraph anchor label shown inline |
| `<span>` | `wst-fqm` | Marginal reference number (shown inline as muted label) |
| `<span>` | `wst-lang` | Language-tagged text (e.g. Greek quotations — rendered italic) |
| `<span>` | `wst-uppercase` | Uppercase small-caps style |
| `<span>` | `wst-tooltip` + `wst-tooltip-dash` | Text with native browser tooltip via `title=""` |

`wst-*` spans are styled by `assets/css/library.css` — they are functional, not chrome.

---

## 4. Tolerated structural elements

The following appear in source HTML and have CSS support in `library.css`, so they
are not stripped. They are *tolerated* but not the preferred form for new content.

| Element/Class | Source | CSS treatment |
|---|---|---|
| `<div class="prp-pages-output">` | Wikisource ProofreadPage | `display: contents` — invisible wrapper |
| `<div class="wst-center">` | Wikisource templates | `text-align: center` |
| `<div class="wst-block-center">` | Wikisource templates | Centred block |
| `<div class="wst-center-or-hi">` | Wikisource templates | Centred block |
| `<div class="stanza">` | Poetry | Verse stanza wrapper |
| `<div class="footnote">`, `<div class="footnotes">` | Various sources | Footnote container |
| `<div class="footer_note">` | CCEL sources | Footnote container |

When writing new content or resourcing a doc from scratch, prefer `<p class="lib-center">`,
`<div class="stanza">`, and `<aside class="lib-fn">` respectively.

---

## 5. Disallowed — never present in compliant docs

### 5a. Disallowed tags

| Tag | Replace with |
|---|---|
| `<i>` | `<em>` |
| `<b>` | `<strong>` |
| `<br>` | Close and open `<p>` tags |
| `<hr>` | Use section boundaries; remove decorative rules |
| `<small>` | Unwrap (keep text); use CSS if size reduction needed |
| `<big>` | Unwrap (keep text) |
| `<cite>` | Unwrap or wrap in `<em>` |
| `<center>` | `<p class="lib-center">` |
| `<font>` | Unwrap (keep text) |
| `<strike>`, `<s>` | `<del>` if semantically a deletion; otherwise unwrap |
| `<u>` | `<em>` or unwrap |
| `<dl>`, `<dt>`, `<dd>` | Convert to `<p>` or `<ul><li>` structure |

### 5b. Disallowed attributes

- `style="..."` — any inline style on any element
- `id="..."` on `<p>` tags
- `id="..."` on headings unless needed for footnote anchors
- `href="...ccel.org..."` — CCEL navigation links
- `class="Normal"`, `class="Default"`, `class="Body"` — CCEL default paragraph classes

### 5c. Disallowed source chrome

These indicate un-cleaned source HTML and must be removed:

**MediaWiki / Wikisource:**
- `<div class="mw-parser-output">`, `<div class="mw-content-ltr">` — unwrap
- `<div class="mw-heading">`, `<div class="mw-headingN">` — extract heading, remove div
- `<span class="mw-editsection">` — remove entirely
- `<span class="module-wikidata-link">` — remove
- `<span class="dropinitial">`, `dropinitial-*` — decorative drop caps, remove (keep text)
- `<span class="wst-asc">`, `<span class="nowrap">` — remove (unwrap)
- `id="..."` attributes on headings (`Chapter_I` style) — strip id

**CCEL:**
- `<div class="book-font-size-malleable">`, `book-font-family`, `book-theme-malleable` — unwrap
- `<div class="spacer">`, `<div id="navbar-spacer">` — remove
- `<a href="...ccel.org...">` — remove anchor (keep text)
- `<span class="Footnote">`, `<span class="mnote">` — remove (footnote text already in `<div class="footnote">`)
- `<sup class="Note">`, `<a class="NoteRef">`, `<a class="Note">` — remove or convert to `<sup class="lib-fn__marker">`
- `class="Normal"`, `class="Default"`, `class="Body"` on `<p>` — strip class

**Project Gutenberg:**
- Any `<p>` containing "PROJECT GUTENBERG" or "TRANSCRIBER" text — remove paragraph
- `<div class="gapspace">` — remove
- `<span class="GutSmall">` — unwrap
- `<hr>` used as boilerplate divider — remove

**Page markers (all sources):**
- `<span class="pagenum">` — remove
- `<span class="pageno">` — remove (Gutenberg/CCEL variant)
- `<span class="pb">` — remove (CCEL page-break marker)
- `<span class="pgmark">` — remove
- `<span class="tei tei-pb">`, `<span class="tei-pb">` — remove
- `[Pg N]` text patterns — remove
- `<a class="page">` — remove (Gutenberg page anchors)

**TEI XML remnants:**
- `<span class="tei tei-noteref">` — convert to `<sup class="lib-fn__marker">` or remove
- `class="tei-*"` on any element — strip class

**Small-caps variants (normalise to one class):**
- `<span class="smcap">`, `<span class="sc">`, `<span class="smc">`,
  `<span class="smcap">` → all convert to `<span class="smallcaps">`

**Auto-generated CSS class names:**
- Classes matching pattern `[a-zA-Z]\d{3,}` or `c\d{2,}` (e.g. `c007`, `c014`, `c006`) — strip class
- `class="i0"`, `class="i1"`, `class="i2"`, `class="i3"`, `class="i4"` (indentation artifacts) — strip
- `class="label"` on `<span>` or `<td>` — strip unless it's a meaningful semantic label

---

## 6. JSON-path documents (`data/library/docs/*.json`)

Schema per section:

```json
{
  "ref": "Q1",
  "heading": "Lord's Day 1 — Our Only Comfort",
  "html": "<div class=\"lib-qa\" id=\"q1\">...</div>"
}
```

- `ref` — unique identifier within the document (empty string for intro sections)
- `heading` — plain text, matches the visible heading in the HTML
- `html` — inner HTML of the section; apply rules 5a–5c to the HTML content
- Allowed inside `html`: all block/inline elements from sections 2–3 above,
  plus `lib-qa`, `lib-qa__num`, `lib-qa__q`, `lib-qa__a`, `lib-article`,
  `lib-article__num`, `lib-article__text`, `lib-lords-day`, `lib-creed`,
  `lib-clause`, `lib-refs` classes (catechism/confession display classes)

---

## 7. Content completeness requirements

A document is considered **content-complete** when:

- Total prose text across all sections ≥ 1,000 words
- Every section has at least one `<p>` element with ≥ 100 characters of text
- For works with known chapter counts: actual section count within 20% of expected count

Documents failing completeness (like a Cassian with only TOC entries, or a Julian
with only headings) must be re-sourced before being listed in `data/library/index.json`.

---

## 8. Validation levels

Run `python3 scripts/validate-library-format.py --all` to check all docs.

**FAIL** — must fix before indexing or committing:

| Code | Rule |
|---|---|
| R1 | Root contains non-section elements or MediaWiki/CCEL wrapper divs |
| R3 | Section's first child is not `<hN class="lib-section__title">` |
| R5 | Any `style="..."` attribute found |
| R6 | `<i>` or `<b>` tags found |
| R7 | Source chrome: MediaWiki divs, CCEL wrappers, Gutenberg boilerplate |
| R8 | Page-number markers: `pagenum`, `tei-pb`, `[Pg N]` |
| R11 | Hollow sections: no `<p>` element and text < 600 chars |
| R12 | Near-empty document: total text < 1,000 words across all sections |

**WARN** — flag for cleanup, does not block:

| Code | Rule |
|---|---|
| W9 | Empty `<a id="...">` anchor targets |
| W10 | Under-split: file > 100KB with ≤ 3 sections |
| W-BR | More than 20 `<br>` elements (use `<p>` tags instead) |
| W-HR | Any `<hr>` elements present |
| W-PAGE | Remaining page markers: `pageno`, `pb`, `pgmark`, `tei-noteref` |
| W-CHROME | Source-chrome classes with no CSS support: `dropinitial*`, `smcap`, `sc`, `smc`, `NoteRef`, `Footnote`, `mnote`, `GutSmall`, `indexpageno` |
| W-AUTOCLASS | Auto-generated class names matching `c\d{2,}` or `[a-zA-Z]\d{3,}` |

---

## 9. Sourcing new documents

When adding a new document:

1. Identify a public-domain source (CCEL, Project Gutenberg, Wikisource, NPNF series)
2. Choose the best text (prefer CCEL for theological works; Gutenberg for Reformation-era)
3. Run the appropriate cleaning mode: `scripts/clean-library-html.py --mode [mediawiki|ccel|gutenberg]`
4. Run `scripts/resection-library-html.py <docid> --heading h2` (adjust level as needed)
5. Run `scripts/clean-library-html.py --mode artifacts` (strips remaining chrome)
6. Run `scripts/validate-library-format.py <docid>` — fix all FAILs and WARNs
7. Add entry to `data/library/index.json` with correct `totalSections`
8. Run `scripts/build-library-search-index.py` to update the search index
9. Run `scripts/validate-library-format.py --all` — ensure no new failures

---

*Last updated: 2026-06-03*
