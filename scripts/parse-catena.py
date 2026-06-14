"""
Catena Aurea parser — extracts the per-verse patristic catena (Aquinas, tr. J.H.
Newman 1841) into the project's commentary source format. The Catena covers only
the four Gospels (it is Aquinas's own patristic chain — effectively a public-domain
ACCS), so this produces data/commentary/catena/{matthew,mark,luke,john}.json.

TWO source editions are used because no single clean edition hosts all four:
  • Mark   — CCEL (https://www.ccel.org/ccel/aquinas/catena2.iii.{roman}.html).
             Clean UTF-8. Marks pericope text with <p class="scripture"> (leads with
             a verse number) and each Father with <p class="normal">Name, ref: …</p>;
             an untagged <p class="normal"> is a CONTINUATION of the prior Father.
  • Matthew, Luke, John — isidore.co single-page editions (CAMatthew/CALuke/CAJohn).
             Chapters are <a name="N"> anchors; pericope text is a color:red Arial
             span leading with "Ver. N." / "N."; each Father is explicitly tagged —
             a color:blue Arial span (Matthew) or <b>NAME</b> (Luke/John). Because
             the Father is tagged, no name whitelist is needed to find comment
             boundaries (unlike CCEL). The isidore Matthew/Mark pages lost their
             curly quotes to U+FFFD; clean_fffd() restores them (letter–letter →
             apostrophe, else → double quote — verified against context samples).

Output shape: {ch: {v: "<html>"}} where html concatenates the Father comments for a
pericope, each as <p><strong>Bede:</strong> …</p>. Comments are keyed at the
pericope's FIRST verse — identical to existing section-sources (mhcc, jfb) — so the
reader's "closest key <= verse" lookup (_extractCommHtml in modal.js) resolves any
verse to its pericope with no reader changes.

Run from repo root:  python3 scripts/parse-catena.py [matthew|mark|luke|john|all]
Cached HTML expected under working/catena-src/ (fetched separately so the parser is
network-free and re-runnable offline): mark_ch{N}.html (CCEL) and CA{Book}.htm
(isidore). CHANGE? If you re-fetch, keep those filenames or update CACHE lookups.
"""

import json, pathlib, re, sys, html as htmllib

ROOT = pathlib.Path(__file__).parent.parent
CACHE = ROOT / 'working' / 'catena-src'

# Per-Gospel config: which edition/extractor to use and how many chapters.
#   'ccel'    → per-chapter CCEL files mark_ch{N}.html, parsed by parse_ccel
#   'isidore' → single isidore file (the 'file' field), parsed by parse_isidore
BOOKS = {
    'matthew': {'source': 'isidore', 'file': 'CAMatthew.htm', 'chapters': 28},
    'mark':    {'source': 'ccel',                              'chapters': 16},
    'luke':    {'source': 'isidore', 'file': 'CALuke.htm',     'chapters': 24},
    'john':    {'source': 'isidore', 'file': 'CAJohn.htm',     'chapters': 21},
}

# Map the citation prefix that opens a <p class="normal"> to a stable display name.
# Catena attributes inline as "Bede, in Marc., i, 1:" — we take the text before the
# first comma/colon as the raw father token, then normalise spelling variants.
# CHANGE? If a Gospel introduces a Father not listed here, add it; unknown tokens are
#   kept verbatim (and reported by the script) rather than silently dropped.
FATHER_NORMALISE = {
    'chrys': 'Chrysostom', 'chrysostom': 'Chrysostom',
    'pseudo-chrys': 'Pseudo-Chrysostom',
    'aug': 'Augustine', 'augustine': 'Augustine',
    'bede': 'Bede', 'jerome': 'Jerome', 'pseudo-jerome': 'Pseudo-Jerome',
    'greg': 'Gregory', 'gregory': 'Gregory', 'gregory nyss': 'Gregory of Nyssa',
    'theophyl': 'Theophylact', 'theophylact': 'Theophylact',
    'hilary': 'Hilary', 'ambrose': 'Ambrose', 'origen': 'Origen',
    'cyril': 'Cyril', 'basil': 'Basil', 'remig': 'Remigius',
    'gloss': 'Gloss', 'glossa': 'Gloss', 'isidore': 'Isidore',
    'athanasius': 'Athanasius', 'damascene': 'John Damascene',
    'euseb': 'Eusebius', 'eusebius': 'Eusebius', 'maximus': 'Maximus',
    'leo': 'Leo', 'bede, in marc': 'Bede',
}

# A <p class="normal"> opens a new comment iff its text starts with a recognised
# Father citation: a short Capitalised token, then an optional ", work ref", then ":".
# We test the candidate token (lowercased, sans trailing ".") against FATHER_NORMALISE.
FATHER_RE = re.compile(r'^\s*([A-Z][A-Za-z][\w.\- ]{0,28}?)(?:,[^:]{0,40})?:\s')


def strip_tags(s):
    # Drop CCEL page-break spans and any other inline markup, unescape entities,
    # normalise whitespace. We keep no inner tags — comments become plain prose
    # wrapped by the caller in a single <p>.
    s = re.sub(r'<span class="pb"[^>]*>.*?</span>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    s = htmllib.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def parse_ccel_chapter(html_text):
    """Return [[first_verse, last_verse, [(display, clean_comment), ...]], ...] for
    one CCEL chapter page.

    CCEL emits ONE <p class="scripture"> per verse, so a multi-verse pericope is a
    *run* of consecutive scripture paragraphs followed by a run of comment
    paragraphs. We open a new pericope only on the first scripture paragraph that
    follows a comment (or the start of the chapter); consecutive scripture
    paragraphs extend the current pericope's verse range. The comment text is
    stored already stripped of its "Father, ref:" lead so build_book can render
    every source uniformly.
    """
    blocks = re.findall(
        r'<p class="(scripture|normal)"[^>]*>(.*?)</p>', html_text, re.S)
    pericopes = []          # list of [first_verse, last_verse, comments]
    cur = None
    last_cls = None
    for cls, body in blocks:
        text = strip_tags(body)
        if not text:
            continue
        if cls == 'scripture':
            # Bare "23." in most chapters, but CCEL writes the first verse of a
            # chapter as "Ver. 1:" — tolerate the optional prefix.
            m = re.match(r'\s*(?:Ver\.\s*)?(\d+)', text)
            if not m:
                continue
            v = int(m.group(1))
            if cur is None or last_cls == 'normal':
                cur = [v, v, []]
                pericopes.append(cur)
            else:
                cur[1] = v                                # extend range
        else:  # normal — a Father comment or a continuation
            if cur is None:
                last_cls = cls
                continue  # commentary before any verse (prologue) — skip
            fm = FATHER_RE.match(text)
            token = fm.group(1).strip().rstrip('.').lower() if fm else None
            if token in FATHER_NORMALISE:
                display = FATHER_NORMALISE[token]
                clean = FATHER_RE.sub('', text, count=1).strip()
                cur[2].append([display, clean])           # new comment
            elif cur[2]:
                cur[2][-1][1] += ' ' + text               # continuation
            # else: an unattributed lead paragraph with no prior comment — drop
        last_cls = cls
    return pericopes


# ── isidore.co extractor (Matthew, Luke, John) ────────────────────────────────

def clean_fffd(s):
    # The isidore Matthew/Mark editions lost every curly quote to U+FFFD. Restore:
    # a U+FFFD flanked by two letters was an apostrophe (John's, camel's); anywhere
    # else it was a double quote. Verified against context samples (177 apostrophe
    # vs 3414 quote positions in the Mark file).
    out = []
    for i, ch in enumerate(s):
        if ch == '�':
            prev = s[i - 1] if i else ' '
            nxt = s[i + 1] if i + 1 < len(s) else ' '
            out.append("’" if prev.isalpha() and nxt.isalpha() else '"')
        else:
            out.append(ch)
    return ''.join(out)


# Common abbreviated/upper-case Father tags in the isidore editions → display name.
# Unlike CCEL, the Father is explicitly tagged in the markup, so this map only
# tidies presentation; an unrecognised tag is Title-cased and kept verbatim.
ISIDORE_FATHER_FIX = {
    'chrys': 'Chrysostom', 'pseudo-chrys': 'Pseudo-Chrysostom',
    'aug': 'Augustine', 'pseudo-aug': 'Pseudo-Augustine',
    'greg': 'Gregory', 'greg naz': 'Gregory Nazianzen', 'greg nyss': 'Gregory of Nyssa',
    'theophyl': 'Theophylact', 'hieron': 'Jerome', 'ambr': 'Ambrose',
    'orig': 'Origen', 'remig': 'Remigius', 'bed': 'Bede', 'glossa': 'Gloss',
    'hilar': 'Hilary', 'euseb': 'Eusebius', 'damasc': 'John Damascene',
    'bas': 'Basil', 'isid': 'Isidore', 'cyril alex': 'Cyril',
}

# Strip the leading "work-citation:" left after removing the Father-name tag —
# e.g. "Hom. in Matt., Hom. i:", "de Trin., iii, 11:", "., non occ.:". After eating
# leading separator punctuation, it removes one short phrase ending in ; or : ONLY
# when that phrase contains a '.', ',' or digit (the hallmark of a reference). This
# spares ordinary prose that ends a clause in a colon (e.g. "he says:"), which has
# no such punctuation before the colon.
_CITATION_RE = re.compile(r'^[\s.,;:]*(?:[^:;]{0,50}?[.,0-9][^:;]{0,30}?[;:]\s+)?')


def _norm_isidore_father(raw):
    n = re.sub(r'\s+', ' ', strip_tags(raw)).strip().strip('.,;: ')
    key = n.lower().replace('.', '').strip()
    if key in ISIDORE_FATHER_FIX:
        return ISIDORE_FATHER_FIX[key]
    return n.title() if n.isupper() else n


# Leading red span = pericope scripture (color:red or hex #ff0000); leading <b> or
# blue span = Father attribution. Tested against the START of each <p> body so inline
# scripture quotes mid-comment are not mistaken for a new pericope.
_RED_LEAD = re.compile(r'^\s*<span[^>]*color:\s*(?:red|#ff0000)', re.I)
_FATHER_LEAD = re.compile(
    r'^\s*(?:<b>(.*?)</b>|<span[^>]*color:\s*blue[^>]*>(.*?)</span>)', re.I | re.S)


def parse_isidore(html_text, n_chapters):
    """Return {ch: [[first_v, last_v, [(display, clean_comment), ...]], ...]} for a
    whole isidore single-page Gospel. Chapters are <a name="N"> anchors; within a
    chapter, paragraphs (the <p> tags are unclosed) are classified by their leading
    inline markup — red span = scripture verse, <b>/blue span = Father, else
    continuation — using the same run-grouping as the CCEL path.
    """
    html_text = clean_fffd(html_text)
    # Body chapter targets are <a name="N">; the contents table uses <a href> so is
    # not matched here. Keep the first anchor per chapter number, in document order.
    anchors = [(int(m.group(1)), m.start())
               for m in re.finditer(r'<a\s+name="(\d+)"', html_text)]
    anchors = [(c, p) for c, p in anchors if 1 <= c <= n_chapters]
    seen, uniq = set(), []
    for c, p in anchors:
        if c not in seen:
            seen.add(c); uniq.append((c, p))
    uniq.sort(key=lambda x: x[1])

    out = {}
    for idx, (ch, start) in enumerate(uniq):
        end = uniq[idx + 1][1] if idx + 1 < len(uniq) else len(html_text)
        segment = html_text[start:end]
        pericopes = []
        cur = None
        last_kind = None
        # Split the segment into paragraph bodies on the unclosed <p ...> tags.
        for body in re.split(r'<p\b[^>]*>', segment)[1:]:
            body = body.split('<hr', 1)[0]               # drop trailing <hr> marker
            text = strip_tags(body)
            if not text:
                continue
            if _RED_LEAD.match(body):                     # scripture verse line
                m = re.match(r'\s*(?:Ver\.\s*)?(\d+)', text)
                if m:
                    v = int(m.group(1))
                elif re.match(r'\s*(?:Ver\.\s*)?[lI][.\s]', text):
                    v = 1   # OCR: a leading 'l.'/'I.' is a misread '1.' (chapter openings)
                else:
                    continue
                if cur is None or last_kind == 'comment':
                    cur = [v, v, []]
                    pericopes.append(cur)
                else:
                    cur[1] = v
                last_kind = 'scripture'
                continue
            fm = _FATHER_LEAD.match(body)
            if fm and cur is not None:
                display = _norm_isidore_father(fm.group(1) or fm.group(2))
                rest = strip_tags(body[fm.end():])
                clean = _CITATION_RE.sub('', rest, count=1).strip()
                if clean:
                    cur[2].append([display, clean])
                last_kind = 'comment'
            elif cur is not None and cur[2]:
                cur[2][-1][1] += ' ' + text               # continuation
                last_kind = 'comment'
        out[str(ch)] = pericopes
    return out


def build_book(book):
    cfg = BOOKS[book]
    if cfg['source'] == 'ccel':
        chapters = {str(ch): parse_ccel_chapter(
            (CACHE / f'{book}_ch{ch}.html').read_text(encoding='utf-8'))
            for ch in range(1, cfg['chapters'] + 1)}
    else:
        raw = (CACHE / cfg['file']).read_text(encoding='utf-8', errors='replace')
        chapters = parse_isidore(raw, cfg['chapters'])

    # Emit the Cloud of Witnesses INTERMEDIATE shape {ch:{v:[{f,html}]}} — a list of
    # voice objects per pericope key. scripts/cow-merge.py combines this with every
    # other resource's intermediate into the served data/commentary/catena/{book}.json.
    out = {}
    for ck, pericopes in chapters.items():
        out[ck] = {}
        for first_v, last_v, comments in pericopes:
            if not comments:
                continue
            out[ck][str(first_v)] = [{'f': d, 'html': c} for d, c in comments]
    return out


# Cloud of Witnesses resource id for the Catena Aurea (see COW_AGENT_GUIDE.md).
RESOURCE_ID = 'catena-aurea'


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    books = list(BOOKS) if arg == 'all' else [arg]
    for book in books:
        if book not in BOOKS:
            sys.exit(f'unknown book {book!r}; known: {list(BOOKS)} or "all"')
        data = build_book(book)
        outp = ROOT / 'data' / 'commentary' / 'cow-sources' / RESOURCE_ID / f'{book}.json'
        outp.parent.mkdir(parents=True, exist_ok=True)
        outp.write_text(json.dumps(data, ensure_ascii=False, indent=None))
        n_voices = sum(len(vs) for ch in data.values() for vs in ch.values())
        print(f'wrote {outp.relative_to(ROOT)} — {len(data)} chapters, {n_voices} voices')
    print('Now run: python3 scripts/cow-merge.py')


if __name__ == '__main__':
    main()
