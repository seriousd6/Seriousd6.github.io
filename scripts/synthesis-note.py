#!/usr/bin/env python3
"""
synthesis-note.py — append to (and read) the COW loop's notebook.

The loop runs unattended, so it cannot stop and ask. Anything a human would want
to know afterwards goes into docs/agents/cow-synthesis-notes.json instead:
a fidelity call worth a second opinion, a tool flag the writer overrode, a
defect in the source, a chapter the driver rejected.

    python3 scripts/synthesis-note.py --book joshua --chapter 21 \
        --kind fidelity --note "v12 graded B: Gill is stretched toward Christ" \
        --verses 12

    python3 scripts/synthesis-note.py --list
    python3 scripts/synthesis-note.py --list --kind disagreement
    python3 scripts/synthesis-note.py --list --since 2026-08-09 --book joshua

Appends are locked and read-modify-write, so parallel loop runs cannot shred the
file — though note that the loop itself should not be run in parallel, since
nothing claims a chapter off the queue.

The file is TRACKED (docs/, not scratchpad/) because it is knowledge about the
corpus, and the whole point is that someone reads it later.
"""
import json, os, sys, argparse, datetime, fcntl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NOTES = os.path.join(ROOT, 'docs/agents/cow-synthesis-notes.json')

def load():
    with open(NOTES, encoding='utf-8') as fh:
        return json.load(fh)

def append(entry):
    """Read-modify-write under an exclusive lock."""
    with open(NOTES, 'r+', encoding='utf-8') as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            data = json.load(fh)
            data.setdefault('entries', []).append(entry)
            fh.seek(0)
            json.dump(data, fh, indent=2, ensure_ascii=False)
            fh.write('\n')
            fh.truncate()
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)
    return len(data['entries'])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book')
    ap.add_argument('--chapter')
    ap.add_argument('--kind')
    ap.add_argument('--note')
    ap.add_argument('--verses', help='comma-separated verse keys the note is about')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--since', help='YYYY-MM-DD, for --list')
    a = ap.parse_args()

    data = load()
    valid = list(data.get('kinds') or [])

    if a.list:
        rows = data.get('entries') or []
        if a.kind:
            rows = [r for r in rows if r.get('kind') == a.kind]
        if a.book:
            rows = [r for r in rows if r.get('book') == a.book]
        if a.since:
            rows = [r for r in rows if str(r.get('at', '')) >= a.since]
        if not rows:
            print('no notes match')
            return 0
        print(f'{len(rows)} note(s)\n' + '=' * 74)
        for r in rows:
            where = f'{r.get("book","?")} {r.get("chapter","?")}'
            vs = (' v' + ','.join(r['verses'])) if r.get('verses') else ''
            print(f'\n[{r.get("at","?")}] {r.get("kind","?"):14s} {where}{vs}')
            print(f'  {r.get("note","")}')
        return 0

    missing = [f for f in ('kind', 'note') if not getattr(a, f)]
    if missing:
        print(f'--{" and --".join(missing)} required to append '
              f'(or pass --list). Kinds: {", ".join(valid)}', file=sys.stderr)
        return 2
    if a.kind not in valid:
        print(f'unknown kind {a.kind!r}; use one of: {", ".join(valid)}', file=sys.stderr)
        return 2

    entry = {'at': datetime.date.today().isoformat(), 'kind': a.kind}
    if a.book:
        entry['book'] = a.book
    if a.chapter:
        entry['chapter'] = str(a.chapter)
    if a.verses:
        entry['verses'] = [v.strip() for v in a.verses.split(',') if v.strip()]
    entry['note'] = a.note
    n = append(entry)
    print(f'noted ({n} total): [{entry["kind"]}] {a.book or ""} {a.chapter or ""} — {a.note[:70]}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
