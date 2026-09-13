#!/usr/bin/env python3
"""
synthesis-frontier.py — "what should the COW loop do next?"

Progress is derived from the data tree, never from a tracker file. There are FOUR
queues, drained in this order, and this answers all of them:

  repair     chapters carrying legacy-unversioned verses that graded C or D,
             verses with no qa stamp, or verses whose attributions are
             ungroundable (fidelity defects)
  generate   chapters with a source catena but no synthesis yet
  polish     chapters whose worst remaining verses graded B — faithful but
             stretched, or thin enough that the lint marked them down
  legacy     chapters still carrying the 2026-07-22 per-verse prose, graded A
             at the time but written before any recorded standard

The first two ran the corpus to 1,189/1,189 and then to zero defects. The last
two are the follow-on work: 1,063 grade-B verses first, then the ~8,700 verses
still stamped `legacy-unversioned`. They are disjoint by construction — a
chapter appears in exactly the earliest queue it qualifies for — so the three
chapter counts add up to the work that is actually left.

A chapter listed in docs/agents/cow-synthesis-blocklist.json is filtered out of
every queue. A block that lives only in an operator's prompt is not a block: the
picker keeps serving the chapter and every worker spends a draw declining it.

Usage:
    python3 scripts/synthesis-frontier.py                 # summary + queues
    python3 scripts/synthesis-frontier.py --next          # one unit, for a loop
    python3 scripts/synthesis-frontier.py --next --queue polish
    python3 scripts/synthesis-frontier.py --queue legacy --limit 30
    python3 scripts/synthesis-frontier.py --stats         # coverage only

--next prints a single "book chapter" line and exits 0, or exits 3 when the
queue is empty, so a loop can drive itself:

    unit=$(python3 scripts/synthesis-frontier.py --next --queue repair) || exit 0
    set -- $unit; book=$1; ch=$2
"""
import json, os, sys, glob, argparse, collections, random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import synthesis_qa as QA

BLOCKLIST_REL = 'docs/agents/cow-synthesis-blocklist.json'

# The order `auto` drains. Defects first, then the unwritten, then the merely
# weak, then the merely old: at every point the loop is working on the worst
# thing left rather than the next thing in canonical order.
AUTO_ORDER = ('repair', 'generate', 'polish', 'legacy')

def blocklist():
    """Chapters the owner has taken out of circulation, as {(book, ch): why}.

    Read by every queue, not just the one that surfaced the problem: a blocked
    chapter that is defective is also legacy, so filtering one queue would just
    move it to another. A missing or unparseable file blocks nothing — this must
    never be able to stop the loop, only to narrow it.
    """
    p = os.path.join(ROOT, BLOCKLIST_REL)
    if not os.path.exists(p):
        return {}
    try:
        data = json.load(open(p, encoding='utf-8'))
    except Exception:
        return {}
    out = {}
    for row in data.get('blocked') or []:
        try:
            out[(row['book'], int(row['chapter']))] = row.get('why', '')
        except (KeyError, TypeError, ValueError):
            continue
    return out

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
    """Every queue, in one pass over the tags tree.

    Rows are (book, chapter, why, weight, weight3) — the last two are what
    --worst-first sorts on, the second counting triple. A chapter lands in
    exactly one queue: the earliest it qualifies for. That keeps the meters
    honest (three counts that add up to the chapters left, not three
    overlapping views of the same 300) and it keeps `auto` from offering a
    chapter for polishing that is really waiting on a defect repair.
    """
    books = canonical_books()
    generate, repair, polish, legacy = [], [], [], []
    stats = collections.Counter()
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
            bad = unstamped = ung = weak = old = 0
            for v, t in tags.items():
                if not isinstance(t, dict):
                    continue
                qa = t.get('qa')
                if not isinstance(qa, dict):
                    unstamped += 1; stats['unstamped'] += 1; continue
                std = qa.get('standard')
                grade = qa.get('grade')
                stats[f'standard:{std}'] += 1
                stats[f'grade:{grade}'] += 1
                if qa.get('ungrounded_voices'):
                    ung += 1
                if std == QA.LEGACY_STANDARD and grade in ('C', 'D'):
                    bad += 1
                if grade == 'B':
                    weak += 1
                if std == QA.LEGACY_STANDARD:
                    old += 1
            if bad or unstamped or ung:
                why = []
                if bad: why.append(f'{bad} legacy C/D')
                if unstamped: why.append(f'{unstamped} unstamped')
                if ung: why.append(f'{ung} ungrounded')
                repair.append((b, ch, ', '.join(why), bad, ung))
            elif weak:
                why = f'{weak} grade B'
                if old:
                    why += f', {old} legacy'
                # The legacy verses inside a polish chapter are counted here
                # rather than carried on the row: --worst-first weighs r[4]
                # triple, and a chapter should be polished for its weak prose,
                # not for how old the rest of it is.
                stats['legacy-in-polish'] += old
                polish.append((b, ch, why, weak, 0))
            elif old:
                legacy.append((b, ch, f'{old} legacy-unversioned', old, 0))
    return generate, repair, polish, legacy, stats

def choose(items, spread):
    """Head of the queue, or a uniform pick from its first `spread` entries.

    Concurrent runs are the reason this exists. The queue is deterministic, so
    two sessions that ask at the same moment get the same chapter and one of
    them wastes its work. Spreading the pick over a window makes that rare
    without needing a lock: with 40 candidates a collision costs one chapter,
    and the pusher that loses the race detects it and moves on."""
    if spread and len(items) > 1:
        return items[random.randrange(min(spread, len(items)))]
    return items[0]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--queue',
                    choices=['generate', 'repair', 'polish', 'legacy', 'auto'],
                    default=None,
                    help="'auto' drains repair, then generation, then polish, "
                         "then legacy, and is empty only when all four are — use "
                         "it to run the corpus to completion in one pass. With "
                         "--next it prints '<queue> <book> <ch>' so the caller "
                         "knows which it got.")
    ap.add_argument('--next', action='store_true')
    ap.add_argument('--stats', action='store_true')
    ap.add_argument('--limit', type=int, default=25)
    ap.add_argument('--worst-first', action='store_true',
                    help='order by defect weight rather than canonical order: '
                         'repair by defect count (fidelity counted triple), '
                         'polish by grade-B count, legacy by legacy-verse count')
    ap.add_argument('--spread', type=int, default=0, metavar='N',
                    help='with --next, pick uniformly from the first N of the '
                         'queue instead of its head, so concurrent runs rarely '
                         'land on the same chapter')
    ap.add_argument('--blocked', action='store_true',
                    help='list the chapters the blocklist is suppressing and exit')
    a = ap.parse_args()

    generate, repair, polish, legacy, stats = scan()

    # One filter, applied to every queue. A blocked chapter is usually blocked
    # for a reason that would qualify it for more than one of them.
    blocked = blocklist()
    suppressed = [row for row in repair + polish + legacy
                  if (row[0], row[1]) in blocked]
    keep = lambda rows: [r for r in rows if (r[0], r[1]) not in blocked]
    generate, repair, polish, legacy = (keep(generate), keep(repair),
                                        keep(polish), keep(legacy))

    if a.blocked:
        if not blocked:
            print('nothing is blocked')
            return 0
        print(f'\n  BLOCKED ({len(blocked)}) — filtered out of every queue:')
        for (b, ch), why in sorted(blocked.items()):
            print(f'    {b} {ch}\n      {why[:400]}')
        print(f'\n  see {BLOCKLIST_REL}')
        return 0

    if a.worst_first:
        for q in (repair, polish, legacy):
            q.sort(key=lambda r: -(r[3] + r[4] * 3))

    queues = {'repair': repair, 'generate': generate,
              'polish': polish, 'legacy': legacy}

    if a.next:
        if a.queue == 'auto':
            # Worst first, in the large: a defect outranks a gap, a gap outranks
            # weak prose, and weak prose outranks prose that is merely old.
            for q in AUTO_ORDER:
                if queues[q]:
                    row = choose(queues[q], a.spread)
                    print(f'{q} {row[0]} {row[1]}')
                    return 0
            print('all queues empty', file=sys.stderr)
            return 3
        q = a.queue or ('generate' if generate else 'repair')
        items = queues[q]
        if not items:
            print(f'{q} queue empty', file=sys.stderr)
            return 3
        row = choose(items, a.spread)
        print(f'{row[0]} {row[1]}')
        return 0

    total_src = sum(len(chapters_of('cow', b)) for b in canonical_books())
    done = total_src - len(generate)
    print(f'\nCOW SYNTHESIS FRONTIER')
    print(f'  synthesized : {done}/{total_src} chapters ({100*done/total_src:.1f}%)')
    print(f'  to generate : {len(generate)} chapters')
    print(f'  to repair   : {len(repair)} chapters')
    print(f'  to polish   : {len(polish)} chapters '
          f'({sum(r[3] for r in polish)} grade-B verses, and '
          f'{stats.get("legacy-in-polish", 0)} legacy verses alongside them)')
    print(f'  to rewrite  : {len(legacy)} chapters '
          f'({sum(r[3] for r in legacy)} legacy verses)')
    if blocked:
        print(f'  blocked     : {len(blocked)} chapters '
              f'({len(suppressed)} of them would otherwise be queued) '
              f'— see {BLOCKLIST_REL}')
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
    order = 'worst first' if a.worst_first else 'canonical order'
    for q, label in (('repair', 'REPAIR'), ('polish', 'POLISH'),
                     ('legacy', 'REWRITE FROM LEGACY')):
        if a.queue not in (None, q):
            continue
        print(f'\n  NEXT TO {label} ({order}, first {a.limit}):')
        for row in queues[q][:a.limit]:
            print(f'    {row[0]} {row[1]:>3}  — {row[2]}')
        if not queues[q]:
            print('    — none')
    return 0

if __name__ == '__main__':
    sys.exit(main())
