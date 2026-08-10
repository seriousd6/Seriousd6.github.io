#!/usr/bin/env python3
"""
synthesis-loop.py — the unattended driver for the COW synthesis loop.

Splits the loop into the part a model must do (write the prose) and the part a
script should do (choose the unit, verify it, stamp it, commit it, and refuse
anything that does not earn the standard). An agent only has to write files;
everything mechanical is here, so a run can be left alone.

    python3 scripts/synthesis-loop.py next                    # what to work on
    python3 scripts/synthesis-loop.py next --queue repair --worst-first
    python3 scripts/synthesis-loop.py finish <book> <ch>      # verify+stamp+commit
    python3 scripts/synthesis-loop.py finish <book> <ch> --unattended
    python3 scripts/synthesis-loop.py status

EXIT CODES (stable — a shell loop depends on them)
    0  success
    2  usage error
    3  queue empty — nothing left to do, stop the loop
    4  the chapter failed verification; nothing was committed

`finish` runs, in order: validator -> lint (chapter) -> fidelity -> stamp ->
gate (chapter) -> gate (corpus) -> commit. Any failure stops before the commit,
so bad work cannot land.

The fidelity step is the one a script cannot do for you: it fails unless every
verse carries a self-grade recorded by whoever wrote the prose, after reading it
back against its source.

WITH --unattended a failed chapter is copied to scratchpad/rejected/ and then
reverted with git checkout, leaving a clean tree so the next iteration can
proceed. Without it the files are left in place for inspection and the loop
stops. Losing one chapter's output is cheap — the source catena is untouched and
it can be regenerated; a stalled loop with a dirty tree is not.
"""
import os, sys, subprocess, argparse, shutil, datetime, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PY = sys.executable or 'python3'

def run(args, capture=True):
    return subprocess.run(args, cwd=ROOT, text=True,
                          capture_output=capture)

def say(step, ok, detail=''):
    mark = 'ok  ' if ok else 'FAIL'
    print(f'  [{mark}] {step}{(" — " + detail) if detail else ""}')

def chapter_files(book, ch):
    return [f'data/commentary/cow-synthesis/{book}/{ch}.json',
            f'data/commentary/cow-synthesis-tags/{book}/{ch}.json']

def cmd_next(a):
    args = [PY, 'scripts/synthesis-frontier.py', '--next']
    if a.queue:
        args += ['--queue', a.queue]
    if a.worst_first:
        args += ['--worst-first']
    r = run(args)
    if r.returncode == 3:
        print('queue empty', file=sys.stderr)
        return 3
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        return r.returncode
    print(r.stdout.strip())
    return 0

def cmd_status(a):
    r = run([PY, 'scripts/synthesis-frontier.py'], capture=False)
    return r.returncode

def quarantine(book, ch):
    """Preserve a rejected attempt before reverting it (scratchpad is gitignored)."""
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    dest = os.path.join(ROOT, 'scratchpad', 'rejected', f'{book}-{ch}-{stamp}')
    os.makedirs(dest, exist_ok=True)
    for rel in chapter_files(book, ch):
        src = os.path.join(ROOT, rel)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(dest, os.path.basename(rel) if 'tags' not in rel
                                          else 'tags-' + os.path.basename(rel)))
    return dest

def cmd_finish(a):
    book, ch = a.book, a.chapter
    prose = os.path.join(ROOT, f'data/commentary/cow-synthesis/{book}/{ch}.json')
    if not os.path.exists(prose):
        print(f'no synthesis file for {book} {ch}', file=sys.stderr)
        return 2

    print(f'\nfinishing {book} {ch}')
    steps = [
        ('validator', [PY, 'scripts/validate-synthesis.py', '--verse', book, ch]),
        # --enforce-all matters here: a chapter under repair still carries the
        # OLD legacy stamp, which a plain --gate would skip, passing vacuously.
        ('lint (chapter)', [PY, 'scripts/audit-synthesis-quality.py',
                            '--gate', '--enforce-all', '--book', book,
                            '--chapter', ch, '--worst', '0', '--boilerplate', '0']),
        # Self-grading is a separate step from the lint because it answers a
        # different question: not "is this prose repetitive" but "does it say
        # only what the witnesses say". No script can judge that, so this fails
        # unless the writer has recorded a grade for every verse.
        ('fidelity (self-graded)', [PY, 'scripts/synthesis-fidelity.py',
                                    '--book', book, '--chapter', ch,
                                    '--signals-only']),
    ]
    for name, args in steps:
        r = run(args)
        if r.returncode != 0:
            say(name, False)
            print((r.stdout or '')[-2500:])
            return fail(a, book, ch, f'failed {name}')
        say(name, True)

    # A dry run must leave no residue, but it should still exercise the stamp
    # and both gates for real — otherwise it rehearses nothing worth knowing.
    # So: snapshot the tags file, run the whole chain, restore at the end.
    tags_rel = chapter_files(book, ch)[1]
    tags_abs = os.path.join(ROOT, tags_rel)
    snapshot = open(tags_abs, encoding='utf-8').read() if a.dry_run and os.path.exists(tags_abs) else None

    r = run([PY, 'scripts/backfill-synthesis-qa.py', '--book', book,
             '--chapter', ch, '--standard', 'current', '--overwrite'])
    if r.returncode != 0:
        say('stamp', False, 'the chapter did not earn the current standard')
        print((r.stdout or '')[-2500:])
        if snapshot is not None:
            open(tags_abs, 'w', encoding='utf-8').write(snapshot)
        return fail(a, book, ch, 'did not earn the current standard at the stamp')
    say('stamp', True, (r.stdout or '').strip().splitlines()[0] if r.stdout else '')

    for name, args in [
        ('gate (chapter)', [PY, 'scripts/audit-synthesis-quality.py', '--gate',
                            '--book', book, '--chapter', ch, '--worst', '0',
                            '--boilerplate', '0']),
        ('gate (corpus)', [PY, 'scripts/audit-synthesis-quality.py', '--gate',
                           '--worst', '0', '--boilerplate', '0']),
    ]:
        r = run(args)
        if r.returncode != 0:
            say(name, False)
            print((r.stdout or '')[-2500:])
            if snapshot is not None:
                open(tags_abs, 'w', encoding='utf-8').write(snapshot)
            return fail(a, book, ch, f'failed {name}')
        say(name, True)

    n = len(json.load(open(prose, encoding='utf-8')))
    verb = 'repair: ' if a.repair else ''
    msg = f'COW synthesis {verb}{book} {ch} ({n} verses)'.replace('  ', ' ')
    if a.dry_run:
        if snapshot is not None:
            open(tags_abs, 'w', encoding='utf-8').write(snapshot)
        say('commit', True, f'(dry run) would commit: {msg}')
        say('restore', True, 'dry run left the tree unchanged')
        return 0
    run(['git', 'add'] + chapter_files(book, ch))
    r = run(['git', 'commit', '-m', msg])
    if r.returncode != 0:
        say('commit', False, (r.stdout or r.stderr or '').strip()[:200])
        return 4
    say('commit', True, msg)
    return 0

def note(book, ch, kind, text):
    """Record something for a human to read later. An unattended loop cannot
    stop and ask, so a rejection that leaves no trace is a rejection nobody
    learns from."""
    run([PY, 'scripts/synthesis-note.py', '--book', book, '--chapter', str(ch),
         '--kind', kind, '--note', text[:500]])

def fail(a, book, ch, why=''):
    if a.unattended:
        dest = quarantine(book, ch)
        run(['git', 'checkout', '--'] + chapter_files(book, ch))
        note(book, ch, 'rejected',
             f'{why or "failed verification"}; reverted, attempt kept at '
             f'{os.path.relpath(dest, ROOT)}')
        print(f'  reverted; rejected attempt kept at {os.path.relpath(dest, ROOT)}')
    else:
        print('  files left in place for inspection '
              '(use --unattended to auto-revert and keep the loop moving)')
    return 4

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('next'); p.set_defaults(fn=cmd_next)
    p.add_argument('--queue', choices=['generate', 'repair'])
    p.add_argument('--worst-first', action='store_true')

    p = sub.add_parser('status'); p.set_defaults(fn=cmd_status)

    p = sub.add_parser('finish'); p.set_defaults(fn=cmd_finish)
    p.add_argument('book'); p.add_argument('chapter')
    p.add_argument('--repair', action='store_true',
                   help='use the repair commit-message form')
    p.add_argument('--unattended', action='store_true',
                   help='revert a failed chapter (quarantining it first) so the '
                        'loop can continue without a dirty tree')
    p.add_argument('--dry-run', action='store_true')

    a = ap.parse_args()
    return a.fn(a)

if __name__ == '__main__':
    sys.exit(main())
