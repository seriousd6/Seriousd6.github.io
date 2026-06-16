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
def validate_verse(book, ch):
    prose_p = os.path.join(ROOT, 'data/commentary/cow-synthesis', book, f'{ch}.json')
    tags_p  = os.path.join(ROOT, 'data/commentary/cow-synthesis-tags', book, f'{ch}.json')
    if not os.path.exists(prose_p):
        check(False, f'A {book} {ch}: prose file missing ({prose_p})'); return
    prose = load(prose_p)
    tags  = load(tags_p) if os.path.exists(tags_p) else {}
    check(bool(tags), f'A {book} {ch}: tags file present')
    for v, html in prose.items():
        w = words(html)
        check(isinstance(html, str) and html.strip().startswith('<') and 350 <= w <= 650,
              f'A {book} {ch}:{v}: prose is HTML, {w} words (target ~500, 350–650)')
        ul = unlinked_refs(html)
        check(not ul, f'A {book} {ch}:{v}: every scripture ref is a .ref link (unlinked: {ul[:4]})')
        t = tags.get(v)
        check(isinstance(t, dict), f'A {book} {ch}:{v}: has a tags entry')
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
