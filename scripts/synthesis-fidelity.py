#!/usr/bin/env python3
"""
synthesis-fidelity.py — the read-back that makes self-grading possible.

The lint measures repetition and checks that a NAMED voice exists in the source.
Neither tells you whether a 430-word paraphrase of 90 words of Gill still says
what Gill said. That is a reading task. This script does not attempt to judge
it — it lays the source and the synthesis side by side, computes the signals
that predict where invention hides, and leaves the judgement to the writer.

    python3 scripts/synthesis-fidelity.py --book joshua --chapter 21
    python3 scripts/synthesis-fidelity.py --book psalms --chapter 21 --signals-only
    python3 scripts/synthesis-fidelity.py --book psalms --chapter 21 --json

SIGNALS (advisory — a high number is a place to look, not a verdict):

  expansion   prose words / source words. Corpus median is 0.84x: a synthesis
              normally DISTILS its catena. Past ~6x (7% of the corpus) the prose
              is mostly not coming from the page in front of it. A pericope
              entry is measured against the UNION of the verses its `range`
              covers, not the blob under its start key — measuring the key
              alone made every ranged entry read as a stretch it was not.
  entities    proper nouns in the prose that appear nowhere in the source or the
              KJV text of the verse — the shape a fabricated attribution takes.
  voices      tagged voices with no comment on this chapter in any corpus. This
              one is not advisory; the lint fails on it.

Write the verdict into the tags entry as a sibling of `voices`:

    "fidelity": {"grade": "A", "checked_by": "self"}
    "fidelity": {"grade": "B", "checked_by": "self", "note": "why"}

Then `synthesis-loop.py finish` folds it into the qa block, filling `expansion`
itself. A verse without it will not stamp.
"""
import json, os, re, sys, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import synthesis_qa as QA

TAG = re.compile(r'<[^>]+>')
def vis(h):
    return re.sub(r'\s+', ' ', TAG.sub(' ', str(h or ''))).strip()

# Editorial vocabulary the writer supplies rather than the source: school
# labels, version names, and the study's own framing. Without these the entity
# signal is ~70% false positives and nobody reads it.
EDITORIAL = {
    'reformed', 'lutheran', 'wesleyan', 'arminian', 'puritan', 'evangelical',
    'grammatical', 'historical', 'antiochene', 'alexandrian', 'eastern',
    'latin', 'fathers', 'authorized', 'authorised', 'version', 'jfb', 'kjv',
    'psalter', 'messianic', 'christological', 'christology', 'testament',
    'gospel', 'gospels', 'epistle', 'psalm', 'psalms', 'chapter', 'verse',
    'hebrew', 'greek', 'aramaic', 'english', 'septuagint', 'vulgate', 'targum',
    'talmud', 'midrash', 'masoretic', 'church', 'israel', 'god', 'lord',
    'christ', 'jesus', 'spirit', 'father', 'son', 'scripture', 'scriptures',
    'jew', 'jews', 'jewish', 'gentile', 'gentiles', 'apostle', 'apostles',
}
ENT = re.compile(r'(?<![.!?]\s)(?<!^)\b([A-Z][a-zA-Z]{2,})\b')

def entities(text, pool):
    out = []
    for m in ENT.finditer(text):
        w = m.group(1)
        wl = w.lower()
        if wl in EDITORIAL or '-' in w:
            continue
        if wl not in pool:
            out.append(w)
    seen, uniq = set(), []
    for w in out:
        if w not in seen:
            seen.add(w); uniq.append(w)
    return uniq

def kjv_chapter(book, ch):
    p = os.path.join(ROOT, 'data/bible/KJV', f'{book}.json')
    if not os.path.exists(p):
        return {}
    try:
        return (json.load(open(p, encoding='utf-8')).get('chapters') or {}).get(ch, {})
    except Exception:
        return {}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book', required=True)
    ap.add_argument('--chapter', required=True)
    ap.add_argument('--signals-only', action='store_true',
                    help='omit the side-by-side text; just the numbers')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    book, ch = a.book, a.chapter

    prose_p = os.path.join(ROOT, 'data/commentary/cow-synthesis', book, f'{ch}.json')
    src_p = os.path.join(ROOT, 'data/commentary/cow', book, f'{ch}.json')
    tags_p = os.path.join(ROOT, 'data/commentary/cow-synthesis-tags', book, f'{ch}.json')
    for p in (prose_p, src_p):
        if not os.path.exists(p):
            print(f'missing {p}', file=sys.stderr); return 2
    prose = json.load(open(prose_p, encoding='utf-8'))
    src = json.load(open(src_p, encoding='utf-8'))
    tags = json.load(open(tags_p, encoding='utf-8')) if os.path.exists(tags_p) else {}
    kjv = kjv_chapter(book, ch)
    index = QA.SourceIndex(ROOT)
    chapter_pool = index.pool(book, ch)

    rows, flagged = [], 0
    for v, html in prose.items():
        t = tags.get(v) if isinstance(tags.get(v), dict) else {}
        # A pericope entry stands on the whole span it covers, so that is what
        # it must be measured against; anything else grades the writer on a
        # denominator no rule uses. See QA.span_source_text.
        keys = QA.span_keys(v, t.get('range'))
        stext = vis(QA.span_source_text(src, v, t.get('range')))
        ptext = vis(html)
        pool = (stext + ' ' + chapter_pool + ' '
                + ' '.join(str(kjv.get(k, '')) for k in keys)).lower()
        pw, sw = len(ptext.split()), len(stext.split())
        ratio = QA.expansion_ratio(pw, sw)
        ents = entities(ptext, pool)
        ung = index.ungrounded_voices(book, ch, t.get('voices'))
        fid = t.get('fidelity') or (t.get('qa') or {}).get('fidelity')
        row = {'verse': v, 'range': t.get('range'), 'span': keys,
               'prose_words': pw, 'source_words': sw,
               'expansion': ratio, 'entities': ents, 'ungrounded_voices': ung,
               'fidelity': fid,
               'stretch': bool(ratio and ratio > QA.STRETCH_RATIO)}
        if row['stretch'] or ents or ung:
            flagged += 1
        rows.append(row)

    if a.json:
        json.dump({'book': book, 'chapter': ch, 'verses': rows},
                  sys.stdout, indent=1, ensure_ascii=False)
        print()
        return 0

    print(f'\nFIDELITY READ-BACK — {book} {ch}   ({len(rows)} verses, {flagged} with a signal)')
    print('=' * 78)
    for r in rows:
        marks = []
        if r['stretch']:
            marks.append(f'STRETCH {r["expansion"]}x')
        if r['entities']:
            marks.append('ENTITIES: ' + ', '.join(r['entities'][:6]))
        if r['ungrounded_voices']:
            marks.append('UNSOURCED: ' + ', '.join(r['ungrounded_voices']))
        have = (r['fidelity'] or {}).get('grade')
        label = f'v{r["verse"]}' if not r['range'] else f'vv.{r["range"]}'
        print(f'\n{label}  source {r["source_words"]}w -> prose {r["prose_words"]}w '
              f'({r["expansion"]}x)   self-grade: {have or "MISSING"}')
        for m in marks:
            print(f'    ! {m}')
        if not a.signals_only:
            print('    --- source ---')
            span_src = vis(QA.span_source_text(src, r['verse'], r['range']))
            print('    ' + (span_src or '(none)')[:1200])
            print('    --- synthesis ---')
            print('    ' + vis(prose[r['verse']])[:1200])

    missing = [r['verse'] for r in rows if not (r['fidelity'] or {}).get('grade')]
    print('\n' + '=' * 78)
    if missing:
        print(f'{len(missing)} verses have no fidelity grade: {", ".join(missing[:15])}')
        print('Add  "fidelity": {"grade": "A", "checked_by": "self"}  to each tags entry.')
        return 1
    print('every verse carries a fidelity self-grade')
    return 0

if __name__ == '__main__':
    sys.exit(main())
