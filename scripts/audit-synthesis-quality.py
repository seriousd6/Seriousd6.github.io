#!/usr/bin/env python3
"""
audit-synthesis-quality.py — the anti-template lint for Commentary A.

validate-synthesis.py checks that a verse is *present, linked, and long enough*.
It cannot see whether the length was earned. This script looks for the failure
modes that hide INSIDE the 350–650 window:

  PAD    intra-verse repetition — the same clause said twice to reach the floor
  TMPL   cross-verse templating — one skeleton refilled down a chapter
  BOIL   corpus-wide boilerplate — a stock sentence used everywhere
  FLOOR  length written to the minimum rather than to the material
  THIN   low lexical variety for the word count
  QUOTE  too many verses opening with the quoted verse (documented rule)

Usage:
    python3 scripts/audit-synthesis-quality.py                  # whole corpus
    python3 scripts/audit-synthesis-quality.py --book psalms    # one book
    python3 scripts/audit-synthesis-quality.py --book psalms --chapter 21
    python3 scripts/audit-synthesis-quality.py --json out.json  # machine-readable
    python3 scripts/audit-synthesis-quality.py --worst 40       # ranked offenders

Exit code is 0 always in report mode; use --fail-over N to make CI-style gates.
This is a *quality* signal, not a correctness gate: read the flagged verses.
"""
import json, os, re, sys, glob, argparse, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import synthesis_qa as QA
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYN = os.path.join(ROOT, 'data/commentary/cow-synthesis')

# ── text handling ───────────────────────────────────────────────────────────
TAG = re.compile(r'<[^>]+>')
WS = re.compile(r'\s+')
NONWORD = re.compile(r"[^a-z0-9' ]+")

def visible(html):
    """HTML -> plain visible text."""
    return WS.sub(' ', TAG.sub(' ', html or '')).strip()

def norm(text):
    """Lowercase, strip punctuation/quotes/dashes — for comparing wording."""
    t = text.lower().replace('’', "'").replace('‘', "'")
    t = t.replace('“', ' ').replace('”', ' ').replace('—', ' ')
    return WS.sub(' ', NONWORD.sub(' ', t)).strip()

def words(text):
    return norm(text).split()

SENT_SPLIT = re.compile(r'(?<=[.!?;])\s+')
def sentences(text):
    return [s for s in (x.strip() for x in SENT_SPLIT.split(text)) if s]

def ngrams(toks, n):
    return [' '.join(toks[i:i + n]) for i in range(len(toks) - n + 1)]

# ── per-verse metrics ───────────────────────────────────────────────────────
NGRAM_N = 8          # long enough that an honest repeat is rare
MIN_SENT_WORDS = 7   # ignore fragments when comparing sentences
MATTR_WINDOW = 200   # moving-average TTR window (raw TTR falls with length)

# Named defect families, each a phrase the reader should never see.
# META  — narrating the source's thinness instead of commenting on the verse
# NOISE — narrating that a fragment was skipped (explicitly banned by the loop doc)
# SLOT  — the degenerate "the <clause> (gloss); the <clause> (gloss)" filler shape
META = re.compile(
    r"\b(the (very )?(brief|thin|short|slender|scanty)(est)? comment[s]? "
    r"(matches|answers|suits)|with so brief a body of comment|"
    r"the comment(ary)? (is|being) (very )?(brief|thin|scanty)|"
    r"so (brief|thin|scanty) a comment|the witnesses (say|offer) little|"
    r"little is said (here )?by the witnesses)", re.I)
NOISE = re.compile(
    r"\b(note here is misplaced|belongs to another (passage|chapter|verse)|"
    r"is misplaced|scrape (residue|noise)|page chrome|credited to no witness|"
    r"the source'?s? noise|appears to be (residue|misplaced))", re.I)
SLOT = re.compile(r"(?:;\s*the [a-z][^;()]{0,120}\([^)]{0,80}\)\s*){2,}", re.I)

def mattr(toks, w=MATTR_WINDOW):
    """Moving-average type-token ratio — comparable across lengths."""
    if len(toks) <= w:
        return round(len(set(toks)) / len(toks), 4) if toks else 0.0
    vals = [len(set(toks[i:i + w])) / w for i in range(0, len(toks) - w + 1, 10)]
    return round(sum(vals) / len(vals), 4)

def verse_metrics(html):
    text = visible(html)
    toks = words(text)
    n = len(toks)
    m = {'words': n}

    # lexical variety, length-normalised (raw TTR falls mechanically with length)
    m['ttr'] = mattr(toks)
    # repetition-insensitive-to-length: repetitive prose compresses far better
    raw = norm(text).encode()
    m['compress'] = round(len(zlib.compress(raw, 6)) / len(raw), 4) if raw else 1.0

    # named defect families
    m['meta'] = len(META.findall(text))
    m['noise'] = len(NOISE.findall(text))
    m['slot'] = len(SLOT.findall(text))

    # intra-verse repeated n-grams
    gs = ngrams(toks, NGRAM_N)
    c = Counter(gs)
    dup = {g: k for g, k in c.items() if k > 1}
    m['dup_ngrams'] = len(dup)
    m['max_ngram_repeat'] = max(c.values()) if c else 0
    m['dup_ngram_frac'] = round(sum(k - 1 for k in dup.values()) / len(gs), 4) if gs else 0.0
    m['worst_ngram'] = max(dup, key=lambda g: dup[g]) if dup else None

    # intra-verse near-duplicate sentences
    sents = [norm(s) for s in sentences(text)]
    sents = [s for s in sents if len(s.split()) >= MIN_SENT_WORDS]
    sc = Counter(sents)
    m['dup_sentences'] = sum(k - 1 for k in sc.values() if k > 1)
    m['sent_count'] = len(sents)

    # opening style
    stripped = text.lstrip()
    m['quote_led'] = bool(stripped[:1] in ('“', '"', '‘'))
    return m, sents, toks

# ── scoring ─────────────────────────────────────────────────────────────────
def flags_for(m, chapter_tmpl_hits, floor_lo=350, floor_hi=375):
    """Flags are tiered: NOISE/META/SLOT are categorical defects (a reader can see
    them); PAD/THIN are statistical and want a human read before acting."""
    f = []
    if m.get('ungrounded'):
        f.append('UNSOURCED')
    if m['noise']:
        f.append('NOISE')
    if m['meta']:
        f.append('META')
    if m['slot']:
        f.append('SLOT')
    if m['dup_sentences'] >= 1:
        f.append('PAD')
    # Thresholds calibrated against the loop's gold standard (2 Kings 13,
    # Psalms: ttr ~0.63, zip ~0.46) versus known-degenerate chapters
    # (Joshua 17, Numbers 33: ttr ~0.31-0.37, zip ~0.20-0.26).
    if m['compress'] <= 0.30 or m['dup_ngram_frac'] >= 0.08:
        f.append('PAD')
    if m['ttr'] < 0.45:
        f.append('THIN')
    if floor_lo <= m['words'] <= floor_hi:
        f.append('FLOOR')
    if chapter_tmpl_hits >= 3:
        f.append('TMPL')
    return sorted(set(f))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book')
    ap.add_argument('--chapter')
    ap.add_argument('--worst', type=int, default=25)
    ap.add_argument('--json')
    ap.add_argument('--boilerplate', type=int, default=25)
    ap.add_argument('--fail-over', type=int, default=None,
                    help='exit 1 if more than N verses carry a PAD flag')
    ap.add_argument('--gate', action='store_true',
                    help='CI mode: enforce the standard on verses written to it, '
                         'exempt the tracked legacy debt, exit 1 on any violation')
    a = ap.parse_args()

    pattern = os.path.join(SYN, a.book or '*', f'{a.chapter}.json' if a.chapter else '*.json')
    files = sorted(glob.glob(pattern))
    if not files:
        print(f'no files matched {pattern}', file=sys.stderr)
        return 2

    SRC = QA.SourceIndex(ROOT)
    verses = []                      # per-verse records
    corpus_sentences = Counter()     # normalized sentence -> count
    sentence_example = {}
    chapter_rows = []

    for path in files:
        book = path.split(os.sep)[-2]
        ch = os.path.basename(path)[:-5]
        data = json.load(open(path, encoding='utf-8'))
        tpath = path.replace('cow-synthesis', 'cow-synthesis-tags')
        tags = json.load(open(tpath, encoding='utf-8')) if os.path.exists(tpath) else {}

        per_verse_sents = {}
        quote_led = 0
        for v, html in data.items():
            m, sents, toks = verse_metrics(html)
            per_verse_sents[v] = set(sents)
            quote_led += 1 if m['quote_led'] else 0
            for s in sents:
                corpus_sentences[s] += 1
                sentence_example.setdefault(s, f'{book} {ch}:{v}')
            t = tags.get(v) if isinstance(tags.get(v), dict) else {}
            m['ungrounded'] = SRC.ungrounded_voices(book, ch, t.get('voices'))
            m['qa'] = t.get('qa')
            verses.append({'book': book, 'ch': ch, 'v': v, **m})

        # cross-verse templating: sentences shared between different verses
        shared = Counter()
        for v, ss in per_verse_sents.items():
            for s in ss:
                shared[s] += 1
        tmpl_sentences = {s: k for s, k in shared.items() if k >= 2}
        tmpl_hits_by_verse = {
            v: sum(1 for s in ss if s in tmpl_sentences) for v, ss in per_verse_sents.items()
        }
        for rec in verses[-len(data):]:
            rec['tmpl_hits'] = tmpl_hits_by_verse.get(rec['v'], 0)

        chapter_rows.append({
            'book': book, 'ch': ch, 'verses': len(data),
            'quote_led': quote_led,
            'quote_led_frac': round(quote_led / len(data), 3) if data else 0,
            'tmpl_sentences': len(tmpl_sentences),
            'tmpl_span': max(tmpl_sentences.values()) if tmpl_sentences else 0,
        })

    for rec in verses:
        rec['flags'] = flags_for(rec, rec.get('tmpl_hits', 0))
        # letter grade on the gold-standard scale (see flags_for)
        z, t = rec['compress'], rec['ttr']
        rec['grade'] = ('A' if z >= 0.42 and t >= 0.58 else
                        'B' if z >= 0.36 and t >= 0.50 else
                        'C' if z >= 0.30 and t >= 0.45 else 'D')

    # ── report ──────────────────────────────────────────────────────────────
    n = len(verses)
    print(f'\n{"=" * 78}\nCOW SYNTHESIS QUALITY AUDIT — {n} verses, {len(files)} chapters\n{"=" * 78}')

    # length distribution
    buckets = [(0, 349), (350, 375), (376, 400), (401, 450), (451, 500),
               (501, 600), (601, 650), (651, 99999)]
    print('\nLENGTH DISTRIBUTION')
    for lo, hi in buckets:
        c = sum(1 for r in verses if lo <= r['words'] <= hi)
        bar = '#' * int(60 * c / n) if n else ''
        label = f'{lo}-{hi}' if hi < 99999 else f'{lo}+'
        print(f'  {label:>9} {c:6d} ({100*c/n:5.1f}%) {bar}')

    gr = Counter(r['grade'] for r in verses)
    print('\nQUALITY GRADE (calibrated on the gold-standard chapters)')
    for g, label in (('A', 'reads like 2 Kings 13 / Psalms'),
                     ('B', 'sound, some repetition'),
                     ('C', 'visibly repetitive'),
                     ('D', 'degenerate — filler reaching length')):
        c = gr.get(g, 0)
        print(f'  {g}  {c:6d} ({100*c/n:5.1f}%)  {label}')

    fl = Counter(f for r in verses for f in r['flags'])
    print('\nFLAG COUNTS')
    for k in ('UNSOURCED', 'NOISE', 'META', 'SLOT', 'PAD', 'THIN', 'FLOOR', 'TMPL'):
        print(f'  {k:6s} {fl.get(k,0):6d} ({100*fl.get(k,0)/n:5.1f}%)')

    # correlation: does hugging the floor predict padding?
    near = [r for r in verses if 350 <= r['words'] <= 375]
    far = [r for r in verses if r['words'] >= 450]
    def rate(rs, flag):
        return 100 * sum(1 for r in rs if flag in r['flags']) / len(rs) if rs else 0
    # per-book defect table
    bybook = defaultdict(lambda: Counter())
    bookn = Counter()
    for r in verses:
        bookn[r['book']] += 1
        for fg in r['flags']:
            bybook[r['book']][fg] += 1
    print('\nPER-BOOK DEFECT RATES (books with any categorical defect)')
    print(f'  {"book":>14} {"verses":>6} {"NOISE":>6} {"META":>6} {"SLOT":>6} {"PAD":>6}')
    rows = sorted(bybook.items(),
                  key=lambda kv: -(kv[1]['META'] + kv[1]['SLOT'] * 2 + kv[1]['NOISE'] * 5))
    for b, c in rows[:22]:
        if not (c['META'] or c['SLOT'] or c['NOISE']):
            break
        print(f'  {b:>14} {bookn[b]:6d} {c["NOISE"]:6d} {c["META"]:6d} {c["SLOT"]:6d} {c["PAD"]:6d}')

    print('\nFLOOR-HUGGING vs PADDING')
    print(f'  verses 350-375 words: {len(near):5d}   PAD rate {rate(near,"PAD"):5.1f}%   '
          f'mean TTR {sum(r["ttr"] for r in near)/len(near):.3f}   '
          f'mean zip {sum(r["compress"] for r in near)/len(near):.3f}' if near else '  none')
    print(f'  verses 450+   words: {len(far):5d}   PAD rate {rate(far,"PAD"):5.1f}%   '
          f'mean TTR {sum(r["ttr"] for r in far)/len(far):.3f}   '
          f'mean zip {sum(r["compress"] for r in far)/len(far):.3f}' if far else '  none')

    # fidelity: attributions with no comment on that chapter in any source corpus
    ung = [r for r in verses if r.get('ungrounded')]
    print('\nFIDELITY — attributions not groundable in ANY source corpus')
    print(f'  {len(ung)} verses ({100*len(ung)/n:.2f}%)')
    cnt = Counter(v for r in ung for v in r['ungrounded'])
    for name, k in cnt.most_common(8):
        books = sorted({r['book'] for r in ung if name in r['ungrounded']})
        print(f'    {k:5d}x  {name:24s} {", ".join(books)[:52]}')

    # qa metadata coverage + drift between recorded and recomputed grade
    have = [r for r in verses if r.get('qa')]
    print('\nQA METADATA')
    print(f'  verses carrying a qa block: {len(have)}/{n} ({100*len(have)/n:.1f}%)')
    if have:
        std = Counter(r['qa'].get('standard') for r in have)
        for k, c in std.most_common():
            print(f'    standard {k}: {c}')
        drift = [r for r in have if r['qa'].get('grade') != r['grade']]
        print(f'  recorded grade differs from recomputed: {len(drift)}')
        for r in drift[:5]:
            print(f'    {r["book"]} {r["ch"]}:{r["v"]}  recorded {r["qa"].get("grade")} -> now {r["grade"]}')

    # corpus boilerplate
    print(f'\nCORPUS BOILERPLATE — most reused sentences (>= {MIN_SENT_WORDS} words)')
    for s, k in corpus_sentences.most_common(a.boilerplate):
        if k < 3:
            break
        print(f'  {k:5d}x  {s[:96]}{"..." if len(s) > 96 else ""}')
        print(f'         first seen: {sentence_example[s]}')

    # worst verses
    def severity(r):
        return (len(r.get('ungrounded') or []) * 6 + r['noise'] * 5 + r['slot'] * 3 + r['meta'] * 2
                + r['dup_ngram_frac'] * 4 + r['dup_sentences'] * 0.5
                + (0.62 - r['ttr']) * 3 + (0.40 - r['compress']) * 6
                + r.get('tmpl_hits', 0) * 0.1)
    worst = sorted([r for r in verses if r['flags']], key=severity, reverse=True)[:a.worst]
    print(f'\nWORST {len(worst)} VERSES BY SEVERITY')
    for r in worst:
        print(f'  {r["book"]:>14} {r["ch"]:>3}:{r["v"]:<4} {r["words"]:4d}w '
              f'ttr={r["ttr"]:.3f} zip={r["compress"]:.3f} dupfrac={r["dup_ngram_frac"]:.3f} '
              f'meta={r["meta"]} slot={r["slot"]} noise={r["noise"]} {",".join(r["flags"])}')
        if r['worst_ngram']:
            print(f'        repeated: "{r["worst_ngram"][:88]}"')

    # chapter-level templating + quote-led
    print('\nCHAPTERS WITH HEAVIEST CROSS-VERSE TEMPLATING')
    for c in sorted(chapter_rows, key=lambda c: -c['tmpl_sentences'])[:15]:
        if c['tmpl_sentences'] == 0:
            break
        print(f'  {c["book"]:>14} {c["ch"]:>3}  {c["verses"]:3d} verses  '
              f'{c["tmpl_sentences"]:3d} repeated sentences (max span {c["tmpl_span"]})')

    print('\nCHAPTERS BREACHING THE QUOTE-LED-OPENING RULE (> 1/3)')
    bad_q = [c for c in chapter_rows if c['quote_led_frac'] > 0.34 and c['verses'] >= 4]
    for c in sorted(bad_q, key=lambda c: -c['quote_led_frac'])[:20]:
        print(f'  {c["book"]:>14} {c["ch"]:>3}  {c["quote_led"]}/{c["verses"]} '
              f'({c["quote_led_frac"]*100:.0f}%)')
    print(f'  ({len(bad_q)} chapters over the threshold)')

    if a.json:
        json.dump({'verses': verses, 'chapters': chapter_rows,
                   'boilerplate': corpus_sentences.most_common(300)},
                  open(a.json, 'w'), indent=1)
        print(f'\nwrote {a.json}')

    if a.gate:
        return run_gate(verses)

    if a.fail_over is not None and fl.get('PAD', 0) > a.fail_over:
        return 1
    return 0


# ── CI gate ─────────────────────────────────────────────────────────────────
# A ratchet, not a cliff. The corpus is 43% grade D, so a gate that judged every
# verse would be permanently red and therefore useless. Instead:
#
#   * verses stamped with the CURRENT standard are held to it in full;
#   * verses stamped legacy-unversioned are the tracked 2026-07-22 debt and are
#     skipped — but their number may never exceed the recorded baseline, so the
#     exemption cannot be used to smuggle new work in;
#   * a verse with NO qa block fails outright, because omitting the metadata
#     would otherwise be the easiest way to dodge the gate.
#
# Net effect: CI is green today, and every verse written or repaired from now on
# is protected against regression.
FATAL_FLAGS = ('UNSOURCED', 'NOISE', 'META', 'SLOT')

def run_gate(verses):
    unstamped, legacy, enforced, violations = [], 0, 0, []
    for r in verses:
        qa = r.get('qa')
        if not isinstance(qa, dict):
            unstamped.append(r); continue
        std = qa.get('standard')
        if std == QA.LEGACY_STANDARD:
            legacy += 1; continue
        if std != QA.CURRENT_STANDARD:
            violations.append((r, f'unknown qa.standard {std!r}')); continue
        enforced += 1
        bad = [f for f in FATAL_FLAGS if f in r['flags']]
        if bad:
            violations.append((r, 'defect: ' + ','.join(bad)))
        elif r['grade'] not in ('A', 'B'):
            violations.append((r, f'grade {r["grade"]} (must be A or B)'))

    print('\n' + '=' * 78)
    print(f'CI GATE — standard {QA.CURRENT_STANDARD}')
    print('=' * 78)
    print(f'  enforced (current standard) : {enforced}')
    print(f'  exempt   (tracked debt)     : {legacy} / baseline {QA.LEGACY_BASELINE}')
    print(f'  unstamped (no qa block)     : {len(unstamped)}')
    print(f'  violations                  : {len(violations)}')

    fail = False
    if legacy > QA.LEGACY_BASELINE:
        print(f'\n  FAIL: the legacy exemption grew ({legacy} > {QA.LEGACY_BASELINE}).')
        print('        New work must be stamped with the current standard.')
        fail = True
    for r in unstamped[:20]:
        print(f'  FAIL {r["book"]} {r["ch"]}:{r["v"]} — no qa block; stamp it before committing')
    if len(unstamped) > 20:
        print(f'  ... and {len(unstamped) - 20} more unstamped')
    for r, why in violations[:30]:
        print(f'  FAIL {r["book"]} {r["ch"]}:{r["v"]} — {why}')
    if len(violations) > 30:
        print(f'  ... and {len(violations) - 30} more violations')

    if unstamped or violations or fail:
        return 1
    print('\n  gate passed')
    return 0

if __name__ == '__main__':
    sys.exit(main())
