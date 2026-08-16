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
    python3 scripts/synthesis-loop.py finish <book> <ch> --unattended --push
    python3 scripts/synthesis-loop.py size <book> <ch>        # how big a unit is
    python3 scripts/synthesis-loop.py status

EXIT CODES (stable — a shell loop depends on them)
    0  success
    2  usage error
    3  queue empty — nothing left to do, stop the loop
    4  the chapter failed verification; nothing was committed
    5  --push only: another run finished this chapter first; ours was dropped

`finish` runs, in order: validator -> lint (chapter) -> fidelity -> stamp ->
gate (chapter) -> gate (corpus) -> commit. Any failure stops before the commit,
so bad work cannot land.

The fidelity step is the one a script cannot do for you: it fails unless every
verse carries a self-grade recorded by whoever wrote the prose, after reading it
back against its source.

WITH --push the finished chapter is synced onto origin/master and pushed. That
is not optional for a scheduled run: those fire in fresh containers, so a commit
that is never pushed dies with the container. The sync is a rebuild rather than a
rebase — the chapter files and any new notebook entries are replayed on top of
the current origin/master — so it cannot leave a conflicted tree, and a chapter
another run finished first is detected and dropped instead of fought over.

WITH --unattended a failed chapter is copied to scratchpad/rejected/ and then
reverted with git checkout, leaving a clean tree so the next iteration can
proceed. Without it the files are left in place for inspection and the loop
stops. Losing one chapter's output is cheap — the source catena is untouched and
it can be regenerated; a stalled loop with a dirty tree is not.
"""
import os, sys, subprocess, argparse, shutil, datetime, json, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PY = sys.executable or 'python3'

def run(args, capture=True):
    return subprocess.run(args, cwd=ROOT, text=True,
                          capture_output=capture)

def say(step, ok, detail=''):
    mark = 'ok  ' if ok else 'FAIL'
    print(f'  [{mark}] {step}{(" — " + detail) if detail else ""}')

NOTES_REL = 'docs/agents/cow-synthesis-notes.json'

def chapter_files(book, ch):
    return [f'data/commentary/cow-synthesis/{book}/{ch}.json',
            f'data/commentary/cow-synthesis-tags/{book}/{ch}.json']

def cmd_next(a):
    args = [PY, 'scripts/synthesis-frontier.py', '--next']
    if a.queue:
        args += ['--queue', a.queue]
    if a.worst_first:
        args += ['--worst-first']
    if a.spread:
        args += ['--spread', str(a.spread)]
    r = run(args)
    if r.returncode == 3:
        print('queue empty', file=sys.stderr)
        return 3
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        return r.returncode
    print(r.stdout.strip())
    return 0

def cmd_size(a):
    """Source words in a chapter, so a batch can be budgeted before it starts.

    --worst-first is also longest-first: defect weight counts defective verses
    and verse count tracks source size, so the head of the repair queue runs
    about 1.55x the corpus median. A fixed "two chapters per batch" is therefore
    the wrong unit at this end of the queue, and a worker that can measure the
    unit first can decide whether it is a whole batch on its own.
    """
    sys.path.insert(0, HERE)
    import synthesis_qa as QA
    p = os.path.join(ROOT, f'data/commentary/cow/{a.book}/{a.chapter}.json')
    if not os.path.exists(p):
        print(f'no source catena for {a.book} {a.chapter}', file=sys.stderr)
        return 2
    src = json.load(open(p, encoding='utf-8'))
    total = sum(QA.usable_source_words(blob or '') for blob in src.values())
    print(f'{a.book} {a.chapter}: {len(src)} source keys, {total} usable source words')
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
    # Whether this is a repair is a fact about the tree, not a flag the caller
    # has to remember: a chapter already tracked in HEAD is being rewritten.
    tracked = run(['git', 'ls-files', '--error-unmatch',
                   chapter_files(book, ch)[0]]).returncode == 0
    verb = 'repair: ' if (a.repair or tracked) else ''
    msg = f'COW synthesis {verb}{book} {ch} ({n} verses)'.replace('  ', ' ')
    if a.dry_run:
        if snapshot is not None:
            open(tags_abs, 'w', encoding='utf-8').write(snapshot)
        say('commit', True, f'(dry run) would commit: {msg}')
        say('restore', True, 'dry run left the tree unchanged')
        return 0
    base = (run(['git', 'merge-base', 'HEAD', 'origin/master']).stdout or '').strip()
    run(['git', 'add'] + chapter_files(book, ch))
    r = run(['git', 'commit', '-m', msg])
    if r.returncode != 0:
        say('commit', False, (r.stdout or r.stderr or '').strip()[:200])
        return 4
    say('commit', True, msg)
    if a.push:
        if not base:
            say('push', False, 'no merge-base with origin/master')
            return 4
        return push_chapter(book, ch, msg, base)
    return 0

def notes_entries(ref=None):
    """The notebook's entry list, from a git ref or from the working tree."""
    if ref:
        r = run(['git', 'show', f'{ref}:{NOTES_REL}'])
        if r.returncode != 0:
            return []
        text = r.stdout
    else:
        p = os.path.join(ROOT, NOTES_REL)
        if not os.path.exists(p):
            return []
        text = open(p, encoding='utf-8').read()
    try:
        return json.loads(text).get('entries') or []
    except Exception:
        return []

def append_notes(entries):
    if not entries:
        return
    p = os.path.join(ROOT, NOTES_REL)
    data = json.load(open(p, encoding='utf-8'))
    data.setdefault('entries', []).extend(entries)
    with open(p, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write('\n')

def push_chapter(book, ch, msg, base):
    """Replay this chapter (and any notes written for it) onto origin/master.

    Deliberately NOT a rebase. A rebase of two runs that touched the same JSON
    leaves a conflicted tree that an unattended session cannot resolve, and the
    notebook conflicts on every parallel append because both sides grow the same
    array. Rebuilding instead is total: reset to origin, write the files back,
    re-append the notes, commit once. The only thing that can go wrong is losing
    a race, and that is checked for explicitly.
    """
    files = [f for f in chapter_files(book, ch)
             if os.path.exists(os.path.join(ROOT, f))]
    blobs = {f: open(os.path.join(ROOT, f), encoding='utf-8').read() for f in files}
    mine = unpushed_notes(base)

    # HEAD:master, never 'master': a scheduled container checks out at a
    # detached HEAD, where the local 'master' ref is whatever the clone left
    # behind. Pushing it sends a stale commit and is rejected every time, which
    # reads as "push rejected four times" on work that was perfectly sound.
    for attempt in range(4):
        r = run(['git', 'fetch', 'origin', 'master'])
        if r.returncode != 0:
            if attempt == 3:
                say('push', False, 'could not fetch origin/master')
                return 4
            time.sleep(2 ** (attempt + 1))
            continue

        # Did someone else finish this chapter while we were writing it?
        if run(['git', 'diff', '--quiet', base, 'origin/master', '--']
               + chapter_files(book, ch)).returncode != 0:
            run(['git', 'reset', '--hard', 'origin/master'])
            append_notes(mine)
            if mine:
                run(['git', 'add', NOTES_REL])
                run(['git', 'commit', '-m', f'Loop notes: {book} {ch}'])
                run(['git', 'push', 'origin', 'HEAD:master'])
            say('push', True, f'another run finished {book} {ch} first — dropped ours')
            return 5

        run(['git', 'reset', '--hard', 'origin/master'])
        for rel, text in blobs.items():
            dest = os.path.join(ROOT, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, 'w', encoding='utf-8').write(text)
        append_notes(mine)
        run(['git', 'add'] + list(blobs) + ([NOTES_REL] if mine else []))
        r = run(['git', 'commit', '-m', msg])
        if r.returncode != 0:
            say('push', False, 'nothing to commit after rebuilding onto origin')
            return 4
        r = run(['git', 'push', 'origin', 'HEAD:master'])
        if r.returncode == 0:
            say('push', True, 'origin/master')
            return 0
        if attempt < 3:
            time.sleep(2 ** (attempt + 1))
    say('push', False, 'push rejected four times')
    return 4

def note(book, ch, kind, text):
    """Record something for a human to read later. An unattended loop cannot
    stop and ask, so a rejection that leaves no trace is a rejection nobody
    learns from."""
    run([PY, 'scripts/synthesis-note.py', '--book', book, '--chapter', str(ch),
         '--kind', kind, '--note', text[:500]])

def unpushed_notes(ref):
    """Entries present locally but not in `ref`, compared by content.

    Positional slicing is wrong here: another run may have pushed notes of its
    own, so the remote's list can be longer than ours and still be missing
    everything we wrote.
    """
    seen = {json.dumps(e, sort_keys=True) for e in notes_entries(ref)}
    return [e for e in notes_entries()
            if json.dumps(e, sort_keys=True) not in seen]

def push_notes(msg):
    """Land the notebook on its own. A scheduled run dies with its container, so
    a note that is only written to the working tree is a note nobody reads."""
    for attempt in range(4):
        run(['git', 'fetch', 'origin', 'master'])
        mine = unpushed_notes('origin/master')
        if not mine:
            return
        run(['git', 'reset', '--hard', 'origin/master'])
        append_notes(mine)
        run(['git', 'add', NOTES_REL])
        if run(['git', 'commit', '-m', msg]).returncode != 0:
            return
        if run(['git', 'push', 'origin', 'HEAD:master']).returncode == 0:
            say('push (notes)', True, msg)
            return
        time.sleep(2 ** (attempt + 1))

def fail(a, book, ch, why=''):
    if a.unattended:
        dest = quarantine(book, ch)
        run(['git', 'checkout', '--'] + chapter_files(book, ch))
        note(book, ch, 'rejected',
             f'{why or "failed verification"}; reverted, attempt kept at '
             f'{os.path.relpath(dest, ROOT)}')
        print(f'  reverted; rejected attempt kept at {os.path.relpath(dest, ROOT)}')
        if getattr(a, 'push', False):
            push_notes(f'Loop notes: {book} {ch} rejected')
    else:
        print('  files left in place for inspection '
              '(use --unattended to auto-revert and keep the loop moving)')
    return 4

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('next'); p.set_defaults(fn=cmd_next)
    p.add_argument('--queue', choices=['generate', 'repair', 'auto'],
                   help="'auto' drains repair first, then generation, and is "
                        "empty only when both are; prints '<queue> <book> <ch>'")
    p.add_argument('--worst-first', action='store_true')
    p.add_argument('--spread', type=int, default=0, metavar='N',
                   help='pick uniformly from the first N of the queue instead '
                        'of its head — use it when runs may overlap')

    p = sub.add_parser('size'); p.set_defaults(fn=cmd_size)
    p.add_argument('book'); p.add_argument('chapter')

    p = sub.add_parser('status'); p.set_defaults(fn=cmd_status)

    p = sub.add_parser('finish'); p.set_defaults(fn=cmd_finish)
    p.add_argument('book'); p.add_argument('chapter')
    p.add_argument('--repair', action='store_true',
                   help='force the repair commit-message form (otherwise '
                        'inferred: a chapter already tracked in HEAD is a repair)')
    p.add_argument('--unattended', action='store_true',
                   help='revert a failed chapter (quarantining it first) so the '
                        'loop can continue without a dirty tree')
    p.add_argument('--push', action='store_true',
                   help='sync onto origin/master and push — required for a '
                        'scheduled run, whose container does not outlive it')
    p.add_argument('--dry-run', action='store_true')

    a = ap.parse_args()
    return a.fn(a)

if __name__ == '__main__':
    sys.exit(main())
