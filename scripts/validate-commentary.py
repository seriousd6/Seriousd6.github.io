#!/usr/bin/env python3
"""
validate-commentary.py — validators for the three book-capstone loops that fill
the Studies tool (see docs/plans/book-capstone-plan.md).

Commentary (Tier 3, the capstone) — book overview + per-chapter section->verse:
    python3 scripts/validate-commentary.py --overview {book}
    python3 scripts/validate-commentary.py --chapter  {book} {ch}
  Overview: data/commentary/exposition/{book}/_book.json has overview.{argument,
  occasion,theology,christ}, a structure list, witnesses, ai_assisted=true, and a
  _source block.
  Chapter: data/commentary/exposition/{book}/{ch}.json — each section has
  pericope_label + range + exposition + a verses list; the union of verse numbers
  across sections MIRRORS the source data/commentary/cow/{book}/{ch}.json keys
  exactly (no verse skipped or invented); every scripture ref is a .ref link.

Book Guide (Tier 1):
    python3 scripts/validate-commentary.py --guide {book}
  data/books/guide/{book}.json shape + refs-linked + _source.

Bible Study Guide (Tier 2):
    python3 scripts/validate-commentary.py --study-guide {book}
  data/books/study-guide/{book}.json sessions shape + refs-linked + _source.

No args validates everything that exists under all three trees.
Exit non-zero on any failure.
"""
import json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []
def check(ok, msg):
    print(('  ok  ' if ok else 'FAIL  ') + msg)
    if not ok:
        fails.append(msg)

def load(p):
    return json.loads(open(p, encoding='utf-8').read())

def words(html):
    return len(re.sub(r'<[^>]+>', ' ', html or '').split())

def nonempty_html(x):
    return isinstance(x, str) and bool(x.strip())

# Every scripture cross-reference in prose MUST be a clickable .ref link (mirrors
# validate-synthesis.py) — flags any "Book Ch[:V]" left as plain text outside an <a>.
_BOOKS = json.loads((__import__('pathlib').Path(ROOT) / 'data/bible/books.json').read_text(encoding='utf-8'))
_BOOK_ALT = '|'.join(re.escape(b['name']) for b in sorted(_BOOKS, key=lambda b: -len(b['name'])))
_FULLREF = re.compile(r'\b(' + _BOOK_ALT + r')\s+\d+(?::\d+(?:[-–]\d+)?)?\b')
def unlinked_refs(html):
    bare = re.sub(r'<a\b[^>]*>.*?</a>', '', html or '', flags=re.S)
    return [m.group(0) for m in _FULLREF.finditer(bare)]

def check_refs(label, *htmls):
    ul = [r for h in htmls for r in unlinked_refs(h)]
    check(not ul, f'{label}: every scripture ref is a .ref link (unlinked: {ul[:4]})')

def has_source(label, obj):
    src = obj.get('_source') if isinstance(obj, dict) else None
    check(isinstance(src, dict) and src.get('kind') and src.get('method'),
          f'{label}: has a _source block (kind + method) for the provenance loop')

# ── Tier 3 — Commentary ─────────────────────────────────────────────────────
EXPO = 'data/commentary/exposition'

def validate_overview(book):
    p = os.path.join(ROOT, EXPO, book, '_book.json')
    if not os.path.exists(p):
        check(False, f'C {book} overview: _book.json missing ({p})'); return
    m = load(p)
    ov = m.get('overview') or {}
    for field in ('argument', 'occasion', 'theology', 'christ'):
        check(nonempty_html(ov.get(field)), f'C {book} overview: overview.{field} is non-empty HTML')
    check(isinstance(ov.get('structure'), list) and ov['structure'],
          f'C {book} overview: overview.structure is a non-empty list')
    for s in (ov.get('structure') or []):
        check(isinstance(s, dict) and s.get('label') and s.get('range'),
              f'C {book} overview: each structure item has label + range')
    check(isinstance(m.get('witnesses'), list) and m['witnesses'],
          f'C {book} overview: witnesses is a non-empty list (Cloud of Witnesses drawn on)')
    check(m.get('ai_assisted') is True, f'C {book} overview: ai_assisted is true (AI-assisted disclosure)')
    check_refs(f'C {book} overview', ov.get('argument'), ov.get('occasion'),
               ov.get('theology'), ov.get('christ'))
    has_source(f'C {book} overview', m)

def _source_verse_keys(book, ch):
    """Verse keys of the source catena the chapter must mirror."""
    p = os.path.join(ROOT, 'data/commentary/cow', book, f'{ch}.json')
    if not os.path.exists(p):
        return None
    return {str(k) for k in load(p).keys() if str(k).isdigit()}

def validate_chapter(book, ch):
    p = os.path.join(ROOT, EXPO, book, f'{ch}.json')
    if not os.path.exists(p):
        check(False, f'C {book} {ch}: chapter file missing ({p})'); return
    data = load(p)
    check(isinstance(data, dict) and data, f'C {book} {ch}: is a non-empty object keyed by section-start verse')
    cmeta = data.get('_meta') or {}
    if cmeta.get('reflection'):
        check_refs(f'C {book} {ch} _meta.reflection', *(cmeta.get('reflection') or []))
    covered = []
    for k, sec in data.items():
        if k == '_meta':
            continue
        lab = f'C {book} {ch}:{k}'
        check(str(k).isdigit(), f'{lab}: section key is a verse number')
        check(isinstance(sec, dict) and sec.get('pericope_label') and sec.get('range'),
              f'{lab}: has pericope_label + range')
        check(nonempty_html(sec.get('exposition')) and words(sec.get('exposition')) >= 40,
              f'{lab}: exposition is real prose (>=40 words), not filler')
        verses = sec.get('verses')
        check(isinstance(verses, list) and verses, f'{lab}: has a non-empty verses list')
        for vn in (verses or []):
            check(isinstance(vn, dict) and str(vn.get('v', '')).isdigit() and nonempty_html(vn.get('note')),
                  f'{lab}: each verse note has a numeric v + non-empty note')
            if isinstance(vn, dict) and str(vn.get('v', '')).isdigit():
                covered.append(str(vn['v']))
            check_refs(f'{lab} v.{vn.get("v")}', vn.get('note') if isinstance(vn, dict) else '')
        check_refs(lab, sec.get('exposition'), sec.get('application'),
                   sec.get('original_language'), sec.get('historical_context'), sec.get('christ'))
        for w in (sec.get('witnesses') or []):
            check(isinstance(w, dict) and w.get('voice'), f'{lab}: each witness has a voice name')
        for x in (sec.get('external') or []):
            check(isinstance(x, dict) and x.get('name'), f'{lab}: each external source has a name')
    # mirror check — the union of verse numbers must equal the source catena's keys
    src = _source_verse_keys(book, ch)
    dup = sorted({v for v in covered if covered.count(v) > 1}, key=int)
    check(not dup, f'C {book} {ch}: no verse appears in two sections (dupes: {dup})')
    if src is None:
        check(False, f'C {book} {ch}: source catena data/commentary/cow/{book}/{ch}.json missing — cannot mirror-check')
    else:
        cov = set(covered)
        missing = sorted(src - cov, key=int)
        extra = sorted(cov - src, key=int)
        check(cov == src,
              f'C {book} {ch}: verses mirror source exactly (missing: {missing[:6]}, extra: {extra[:6]})')

# ── Tier 1 — Book Guide ─────────────────────────────────────────────────────
def validate_guide(book):
    p = os.path.join(ROOT, 'data/books/guide', f'{book}.json')
    if not os.path.exists(p):
        check(False, f'G {book}: guide file missing ({p})'); return
    g = load(p)
    check(g.get('id') == book, f'G {book}: id matches filename')
    for field in ('one_line', 'orientation', 'how_to_read', 'christ_in_book'):
        check(nonempty_html(g.get(field)), f'G {book}: {field} is non-empty')
    check(isinstance(g.get('structure'), list) and g['structure'], f'G {book}: structure is a non-empty list')
    check(isinstance(g.get('themes'), list) and g['themes'], f'G {book}: themes is a non-empty list')
    check_refs(f'G {book}', g.get('orientation'), g.get('how_to_read'), g.get('christ_in_book'))
    has_source(f'G {book}', g)

# ── Tier 2 — Bible Study Guide ──────────────────────────────────────────────
def validate_study_guide(book):
    p = os.path.join(ROOT, 'data/books/study-guide', f'{book}.json')
    if not os.path.exists(p):
        check(False, f'S {book}: study-guide file missing ({p})'); return
    sg = load(p)
    check(sg.get('id') == book, f'S {book}: id matches filename')
    sessions = sg.get('sessions')
    check(isinstance(sessions, list) and sessions, f'S {book}: sessions is a non-empty list')
    for i, s in enumerate(sessions or [], 1):
        lab = f'S {book} session {i}'
        check(isinstance(s, dict) and s.get('title') and s.get('range'), f'{lab}: has title + range')
        check(nonempty_html(s.get('big_idea')), f'{lab}: big_idea is non-empty')
        for arr in ('observe', 'interpret', 'apply'):
            check(isinstance(s.get(arr), list) and s[arr], f'{lab}: {arr} is a non-empty list of questions')
        check(nonempty_html(s.get('leader_notes')), f'{lab}: leader_notes is non-empty')
        check_refs(lab, s.get('big_idea'), s.get('leader_notes'), ' '.join(
            (s.get('observe') or []) + (s.get('interpret') or []) + (s.get('apply') or [])))
    has_source(f'S {book}', sg)

def main():
    a = sys.argv[1:]
    if a and a[0] == '--overview' and len(a) >= 2:
        validate_overview(a[1])
    elif a and a[0] == '--chapter' and len(a) >= 3:
        validate_chapter(a[1], a[2])
    elif a and a[0] == '--guide' and len(a) >= 2:
        validate_guide(a[1])
    elif a and a[0] == '--study-guide' and len(a) >= 2:
        validate_study_guide(a[1])
    else:
        for p in glob.glob(os.path.join(ROOT, EXPO, '*', '_book.json')):
            validate_overview(os.path.basename(os.path.dirname(p)))
        for p in glob.glob(os.path.join(ROOT, EXPO, '*', '*.json')):
            if os.path.basename(p) == '_book.json':
                continue
            book = os.path.basename(os.path.dirname(p))
            ch = os.path.splitext(os.path.basename(p))[0]
            validate_chapter(book, ch)
        for p in glob.glob(os.path.join(ROOT, 'data/books/guide', '*.json')):
            validate_guide(os.path.splitext(os.path.basename(p))[0])
        for p in glob.glob(os.path.join(ROOT, 'data/books/study-guide', '*.json')):
            validate_study_guide(os.path.splitext(os.path.basename(p))[0])
    print()
    if fails:
        print(f'{len(fails)} FAILURE(S)'); sys.exit(1)
    print('all commentary/guide checks passed')

if __name__ == '__main__':
    main()
