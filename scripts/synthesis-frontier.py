#!/usr/bin/env python3
"""
synthesis-frontier.py — "what should the COW loop do next?"

Progress is derived from the data tree, never from a tracker file. There are now
TWO queues, and this answers both:

  generate   chapters with a source catena but no synthesis yet
  repair     chapters carrying legacy-unversioned verses that graded C or D,
             or verses whose attributions are ungroundable (fidelity defects)

Usage:
    python3 scripts/synthesis-frontier.py                 # summary + both queues
    python3 scripts/synthesis-frontier.py --next          # one unit, for a loop
    python3 scripts/synthesis-frontier.py --next --queue repair
    python3 scripts/synthesis-frontier.py --queue repair --limit 30
    python3 scripts/synthesis-frontier.py --stats         # coverage only

--next prints a single "book chapter" line and exits 0, or exits 3 when the
queue is empty, so a loop can drive itself:

    unit=$(python3 scripts/synthesis-frontier.py --next --queue repair) || exit 0
    set -- $unit; book=$1; ch=$2
"""
import json, os, sys, glob, argparse, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import synthesis_qa as QA

def canonical_books():
    p = os.path.join(ROOT, 'data/bible/books.json')
    return [b['id'] for b in json.load(open(p, encoding='utf-8'))]

def chapters_of(tree, book):
    d = os.path.join(ROOT, f'data/commentary/{tree}', book)
    if not os.path.isdir(d):
        return []
    out = []
    for f in glob.glob(os.path.join(d, '*.json')):
        n = os.path.basename(f)[:-5]
        if n.isdigit():
            out.append(int(n))
    return sorted(out)

def scan():
    books = canonical_books()
    generate, repair, stats = [], [], collections.Counter()
    for b in books:
        src = set(chapters_of('cow', b))
        syn = set(chapters_of('cow-synthesis', b))
        for ch in sorted(src - syn):
            generate.append((b, ch))
        for ch in sorted(src & syn):
            tp = os.path.join(ROOT, 'data/commentary/cow-synthesis-tags', b, f'{ch}.json')
            if not os.path.exists(tp):
                repair.append((b, ch, 'no tags file', 0, 0)); continue
            try:
                tags = json.load(open(tp, encoding='utf-8'))
            except Exception:
                repair.append((b, ch, 'unreadable tags', 0, 0)); continue
            bad = unstamped = ung = 0
            for v, t in tags.items():
                if not isinstance(t, dict):
                    continue
                qa = t.get('qa')
                if not isinstance(qa, dict):
                    unstamped += 1; stats['unstamped'] += 1; continue
                std = qa.get('standard')
                stats[f'standard:{std}'] += 1
                stats[f'grade:{qa.get("grade")}'] += 1
                if qa.get('ungrounded_voices'):
                    ung += 1
                if std == QA.LEGACY_STANDARD and qa.get('grade') in ('C', 'D'):
                    bad += 1
            if bad or unstamped or ung:
                why = []
                if bad: why.append(f'{bad} legacy C/D')
                if unstamped: why.append(f'{unstamped} unstamped')
                if ung: why.append(f'{ung} ungrounded')
                repair.append((b, ch, ', '.join(why), bad, ung))
    return generate, repair, stats

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--queue', choices=['generate', 'repair'], default=None)
    ap.add_argument('--next', action='store_true')
    ap.add_argument('--stats', action='store_true')
    ap.add_argument('--limit', type=int, default=25)
    ap.add_argument('--worst-first', action='store_true',
                    help='repair queue ordered by defect count, not canonical order')
    a = ap.parse_args()

    generate, repair, stats = scan()
    if a.worst_first:
        repair.sort(key=lambda r: -(r[3] + r[4] * 3))

    if a.next:
        q = a.queue or ('generate' if generate else 'repair')
        items = generate if q == 'generate' else repair
        if not items:
            print(f'{q} queue empty', file=sys.stderr)
            return 3
        print(f'{items[0][0]} {items[0][1]}')
        return 0

    total_src = sum(len(chapters_of('cow', b)) for b in canonical_books())
    done = total_src - len(generate)
    print(f'\nCOW SYNTHESIS FRONTIER')
    print(f'  synthesized : {done}/{total_src} chapters ({100*done/total_src:.1f}%)')
    print(f'  to generate : {len(generate)} chapters')
    print(f'  to repair   : {len(repair)} chapters')
    print('\n  verses by standard:')
    for k, v in sorted(stats.items()):
        if k.startswith('standard:'):
            print(f'    {k.split(":",1)[1]:32s} {v:6d}')
    print('  verses by recorded grade:')
    for g in ('A', 'B', 'C', 'D'):
        print(f'    {g} {stats.get(f"grade:{g}", 0):6d}')
    if stats.get('unstamped'):
        print(f'    unstamped {stats["unstamped"]}  <- these fail the CI gate')

    if a.stats:
        return 0
    if a.queue in (None, 'generate'):
        print(f'\n  NEXT TO GENERATE (canonical order, first {a.limit}):')
        for b, ch in generate[:a.limit]:
            print(f'    {b} {ch}')
        if not generate:
            print('    — none, generation is complete')
    if a.queue in (None, 'repair'):
        order = 'worst first' if a.worst_first else 'canonical order'
        print(f'\n  NEXT TO REPAIR ({order}, first {a.limit}):')
        for row in repair[:a.limit]:
            print(f'    {row[0]} {row[1]:>3}  — {row[2]}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
