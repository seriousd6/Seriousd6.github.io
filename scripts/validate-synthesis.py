#!/usr/bin/env python3
"""
validate-synthesis.py — validators for the two synthesis commentaries.

Commentary A (per-verse COW synthesis):
    python3 scripts/validate-synthesis.py --verse {book} {ch}
  Checks data/commentary/cow-synthesis/{book}/{ch}.json and the parallel
  cow-synthesis-tags file: each verse's prose is non-empty HTML ~400–600 words;
  tags carry `voices` (list), `schools` (valid slugs + prevalence), and the
  optional debates/outliers/themes; every prose verse has a tags entry and vice versa.

Commentary B (per-section synthesis):
    python3 scripts/validate-synthesis.py --section {book}
  Checks data/synthesis/{book}/{ch}.json for every chapter: each section has the
  required domain fields, total 500–1000 words; and — crucially — that EVERY paragraph
  heading in data/paragraphs/{book}.json has a matching section key (outline-match), so
  the study-desk Outline never has a dead ✦.

No args validates everything that exists under both trees.
Exit non-zero on any failure.
"""
import json, os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import synthesis_qa as QA

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []
def check(ok, msg):
    print(('  ok  ' if ok else 'FAIL  ') + msg)
    if not ok: fails.append(msg)

def words(html):
    return len(re.sub(r'<[^>]+>', ' ', html or '').split())

# Every scripture cross-reference in the prose MUST be a clickable .ref link (see the loop
# guides + scripts/link-refs.py). This flags any "Book Ch[:V]" reference left as plain text
# OUTSIDE an <a> element — so the loop never ships un-hyperlinked references.
_BOOKS = json.loads((__import__('pathlib').Path(ROOT) / 'data/bible/books.json').read_text())
_BOOK_ALT = '|'.join(re.escape(b['name']) for b in sorted(_BOOKS, key=lambda b: -len(b['name'])))
_FULLREF = re.compile(r'\b(' + _BOOK_ALT + r')\s+\d+(?::\d+(?:[-–]\d+)?)?\b')
def unlinked_refs(html):
    bare = re.sub(r'<a\b[^>]*>.*?</a>', '', html or '', flags=re.S)
    return [m.group(0) for m in _FULLREF.finditer(bare)]

VALID_SCHOOLS = {
    'eastern-antiochene', 'eastern-alexandrian', 'latin-fathers', 'reformed',
    'lutheran', 'wesleyan-arminian', 'puritan-evangelical', 'grammatical-historical'
}
VALID_PREVALENCE = {'unanimous', 'majority', 'several', 'minority', 'single'}
SECTION_DOMAINS = ['synthesis', 'historical_context', 'literary_structure',
                   'theological_application', 'christology']

def load(p):
    return json.loads(open(p, encoding='utf-8').read())

# ── Commentary A ────────────────────────────────────────────────────────────
# ── the thin-verse exemption (owner decision, 2026-08-09) ───────────────────
# The 350-word floor is what manufactured the corpus's filler: a verse with two
# lines of witness material was still required to reach 350 words, so the loop
# padded. See docs/plans/cow-synthesis-quality-audit.md.
#
# A verse may set `"thin": true` in its TAGS entry to opt out of the floor. The
# exemption is not the author's say-so — it is checked against the source: the
# catena blob for that verse must actually be sparse, and the prose must
# actually be short. Both directions are enforced so the flag cannot be used to
# excuse a lazy entry on a rich source, nor left on a verse that grew.
THIN_SOURCE_MAX = 200   # visible words of catena below which "thin" is allowed
THIN_MIN, THIN_MAX = 120, 349

def source_chapter(book, ch):
    """The whole catena for a chapter as {verse: blob}, or None."""
    p = os.path.join(ROOT, 'data/commentary/cow', book, f'{ch}.json')
    if not os.path.exists(p):
        return None
    try:
        return load(p)
    except Exception:
        return None

def source_blob(book, ch, v):
    """The raw catena for one verse, or None if unavailable."""
    src = source_chapter(book, ch)
    return None if src is None else src.get(v, '')

def source_words(book, ch, v, excluded=None):
    """Catena words for one verse, minus any voice blocks declared as residue.

    Measures the source the way the writer is required to READ it: the prose
    rules oblige them to ignore scrape residue, so a blob that is mostly residue
    must not be counted as a rich source. See synthesis_qa.usable_source_words
    for why the exclusion is declared rather than detected.
    """
    blob = source_blob(book, ch, v)
    if blob is None:
        return None
    try:
        return QA.usable_source_words(blob, excluded)
    except Exception:
        return None

def validate_verse(book, ch):
    prose_p = os.path.join(ROOT, 'data/commentary/cow-synthesis', book, f'{ch}.json')
    tags_p  = os.path.join(ROOT, 'data/commentary/cow-synthesis-tags', book, f'{ch}.json')
    if not os.path.exists(prose_p):
        check(False, f'A {book} {ch}: prose file missing ({prose_p})'); return
    prose = load(prose_p)
    tags  = load(tags_p) if os.path.exists(tags_p) else {}
    check(bool(tags), f'A {book} {ch}: tags file present')

    # Coverage replaces the old "one entry per source verse" rule. An entry may
    # declare a range and stand for a span of verses (a pericope), but the spans
    # must tile the chapter EXACTLY — no gaps, no overlaps. The reader infers a
    # section's end from the next key, so a gap would make it advertise a span it
    # does not actually cover; this check is what makes that inference honest.
    #
    # Scoped to chapters that ACTUALLY declare a range. Enforcing it everywhere
    # would retroactively fail work that predates pericopes, and for good
    # reasons: the corpus legitimately omits out-of-range scrape keys (the
    # documented 2 Chronicles 27 key "16" holds Matthew Henry on chapter 28),
    # and a few chapters carry a synthesis for a verse the catena lacks. Those
    # are recorded as advisories by --coverage rather than failures here.
    src_all = source_chapter(book, ch)
    spans = {k: ((tags.get(k) or {}).get('range') if isinstance(tags.get(k), dict) else None)
             for k in prose}
    if src_all and any(spans.values()):
        cov = QA.coverage_problems(src_all.keys(), spans)
        check(not cov, f'A {book} {ch}: pericopes tile the chapter ({"; ".join(cov[:3])})')

    for v, html in prose.items():
        w = words(html)
        is_html = isinstance(html, str) and html.strip().startswith('<')
        tag_entry = tags.get(v) if isinstance(tags.get(v), dict) else {}
        thin = bool(tag_entry.get('thin'))
        excluded = tag_entry.get('excluded_voices') or []
        try:
            lo, hi = QA.parse_range(v, tag_entry.get('range'))
        except ValueError:
            lo, hi = int(v), int(v)
        span = list(range(lo, hi + 1))
        if excluded:
            # A declared exclusion must name a block that is actually in this
            # verse's blob, so the field cannot be padded with names to buy a
            # thin pass on a rich source.
            # A declared exclusion must name a block somewhere in the span this
            # entry covers, so the field cannot be padded with names.
            blob_all = ' '.join(str(source_blob(book, ch, str(x)) or '') for x in span)
            bogus = QA.undeclarable_voices(blob_all, excluded)
            check(not bogus,
                  f'A {book} {ch}:{v}: excluded_voices names a block absent from '
                  f'this entry\'s source ({bogus})')
        if thin:
            # A pericope's source is the union of the verses it covers.
            sw = sum((source_words(book, ch, str(x), excluded) or 0) for x in span)
            check(sw <= THIN_SOURCE_MAX,
                  f'A {book} {ch}:{v}: "thin" is justified by the source '
                  f'({sw} usable source words across {len(span)} verse(s) after '
                  f'{len(excluded)} declared exclusion(s), must be <= {THIN_SOURCE_MAX})')
            check(is_html and THIN_MIN <= w <= THIN_MAX,
                  f'A {book} {ch}:{v}: thin verse is HTML, {w} words '
                  f'({THIN_MIN}-{THIN_MAX}; drop the flag if it grew past {THIN_MAX})')
        else:
            check(is_html and 350 <= w <= 650,
                  f'A {book} {ch}:{v}: prose is HTML, {w} words (target ~500, 350–650)')
        ul = unlinked_refs(html)
        check(not ul, f'A {book} {ch}:{v}: every scripture ref is a .ref link (unlinked: {ul[:4]})')
        t = tags.get(v)
        check(isinstance(t, dict), f'A {book} {ch}:{v}: has a tags entry')
        if isinstance(t, dict) and 'qa' in t:
            probs = QA.qa_problems(t['qa'])
            check(not probs, f'A {book} {ch}:{v}: qa block is well formed ({"; ".join(probs)})')
        if not isinstance(t, dict):
            continue
        check(isinstance(t.get('voices'), list) and t['voices'],
              f'A {book} {ch}:{v}: tags.voices is a non-empty list (for badges)')
        sch = t.get('schools') or []
        ok_sch = isinstance(sch, list) and sch and all(
            isinstance(s, dict) and s.get('school') in VALID_SCHOOLS
            and s.get('prevalence') in VALID_PREVALENCE for s in sch)
        check(ok_sch, f'A {book} {ch}:{v}: schools valid (known slug + prevalence)')
    # every tags entry should have prose too
    for v in tags:
        check(v in prose, f'A {book} {ch}:{v}: tags entry has matching prose')

# ── Commentary B ────────────────────────────────────────────────────────────
def validate_section(book):
    para_p = os.path.join(ROOT, 'data/paragraphs', f'{book}.json')
    para = load(para_p) if os.path.exists(para_p) else {}
    syn_dir = os.path.join(ROOT, 'data/synthesis', book)
    any_ch = False
    for ch in sorted(para.keys(), key=lambda x: int(x)):
        headings = para[ch].get('headings') or []
        syn_p = os.path.join(syn_dir, f'{ch}.json')
        syn = load(syn_p) if os.path.exists(syn_p) else None
        if syn is None:
            # only flag chapters that have been started (skip not-yet-generated chapters silently)
            continue
        any_ch = True
        # outline-match: every heading.before must be a key
        expected = [str(h['before']) for h in headings] or ['1']
        for k in expected:
            check(k in syn, f'B {book} {ch}: outline-match — section key "{k}" exists for its heading')
        for k, sec in syn.items():
            missing = [d for d in SECTION_DOMAINS if not (isinstance(sec.get(d), str) and sec[d].strip())]
            check(not missing, f'B {book} {ch}:{k}: has all domains {SECTION_DOMAINS} (missing: {missing})')
            tot = sum(words(sec.get(d, '')) for d in SECTION_DOMAINS)
            check(450 <= tot <= 1100, f'B {book} {ch}:{k}: {tot} words total (target 500–1000)')
            ul = [r for d in SECTION_DOMAINS for r in unlinked_refs(sec.get(d, ''))]
            check(not ul, f'B {book} {ch}:{k}: every scripture ref is a .ref link (unlinked: {ul[:4]})')
            check(bool(sec.get('pericope_label')) and bool(sec.get('range')),
                  f'B {book} {ch}:{k}: has pericope_label + range')
    if not any_ch:
        check(False, f'B {book}: no synthesis chapters found under data/synthesis/{book}/')

def main():
    args = sys.argv[1:]
    if args and args[0] == '--verse' and len(args) >= 3:
        validate_verse(args[1], args[2])
    elif args and args[0] == '--section' and len(args) >= 2:
        validate_section(args[1])
    else:
        # validate everything present
        for p in glob.glob(os.path.join(ROOT, 'data/commentary/cow-synthesis/*/*.json')):
            book = os.path.basename(os.path.dirname(p)); ch = os.path.splitext(os.path.basename(p))[0]
            validate_verse(book, ch)
        for d in glob.glob(os.path.join(ROOT, 'data/synthesis/*/')):
            validate_section(os.path.basename(os.path.dirname(d)))
    print()
    if fails:
        print(f'{len(fails)} FAILURE(S)'); sys.exit(1)
    print('all synthesis checks passed')

if __name__ == '__main__':
    main()
