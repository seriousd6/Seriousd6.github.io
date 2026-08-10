#!/usr/bin/env python3
"""
backfill-synthesis-qa.py — stamp a qa block onto existing Commentary A verses.

Writes, per verse, what was ACTUALLY true of it when it was generated: which
standard applied (for everything predating 2026-08-09, none — `legacy-unversioned`),
what the tooling of the day verified, the grade the lint gives it now, and the
date its chapter was committed.

This is deliberately conservative about `checks`: it records only what the
validator of the time really enforced (length, linked refs, key correspondence,
school enums). It does NOT claim the new checks were performed, because they
were not — that is the whole point of recording the standard.

    python3 scripts/backfill-synthesis-qa.py --dry-run          # report only
    python3 scripts/backfill-synthesis-qa.py --book psalms      # one book
    python3 scripts/backfill-synthesis-qa.py                    # whole corpus
    python3 scripts/backfill-synthesis-qa.py --overwrite        # restamp existing

Each file is rewritten with ITS OWN indentation, detected from the original
bytes — the tags tree is not uniform (most files are 1-space, some, e.g.
john/4.json, are 2-space). Normalising them would bury the added blocks in
hundreds of thousands of lines of reformatting churn.
"""
import json, os, re, sys, glob, argparse, subprocess, collections, datetime

TODAY = datetime.date.today().isoformat()

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import synthesis_qa as QA
import importlib.util
spec = importlib.util.spec_from_file_location('audit', os.path.join(HERE, 'audit-synthesis-quality.py'))
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

LEGACY_CHECKS = ['length', 'refs-linked', 'tags-match', 'schools-valid']
# What a chapter written to the current standard has actually been through.
CURRENT_CHECKS = ['length', 'refs-linked', 'tags-match', 'schools-valid',
                  'voices-sourced', 'no-meta', 'no-noise', 'no-slot',
                  'no-carriers', 'quotes-capped', 'fidelity-self-graded']

def chapter_dates():
    """book/chapter -> the date its synthesis file first appeared."""
    out = subprocess.run(
        ['git', 'log', '--format=%x01%ad', '--date=short', '--diff-filter=AM',
         '--name-only', '--', 'data/commentary/cow-synthesis'],
        cwd=ROOT, capture_output=True, text=True).stdout
    # git log is newest-first, so OVERWRITE as we walk: the last value assigned
    # is the oldest commit that touched the file — i.e. when it was generated.
    # (setdefault here would record the most recent edit instead, which for any
    # chapter that has since been repaired is the wrong date entirely.)
    cur, dates = None, {}
    for line in out.splitlines():
        if line.startswith('\x01'):
            cur = line[1:]
        elif line.startswith('data/commentary/cow-synthesis/'):
            p = line.split('/')
            if len(p) >= 5:
                dates[(p[3], p[4][:-5])] = cur
    return dates

def detect_indent(raw, default=1):
    """Indent width of a file's own formatting.

    The tags tree is NOT uniform: most files are 1-space, some are 2-space
    (john/4.json), and some are flush-left with no indent at all
    (1kings/8.json). Guessing wrong reformats the whole file and buries the
    real change, so read it off the first content line rather than assuming.
    """
    for line in raw.split('\n')[1:8]:
        st = line.lstrip(' \t')
        if st.startswith('"'):
            return len(line) - len(st)
    return default

_SRC_CACHE = {}
def source_text(book, ch, v):
    """The catena blob for one verse, for the expansion ratio."""
    key = (book, ch)
    if key not in _SRC_CACHE:
        p = os.path.join(ROOT, 'data/commentary/cow', book, f'{ch}.json')
        try:
            _SRC_CACHE[key] = json.load(open(p, encoding='utf-8'))
        except Exception:
            _SRC_CACHE[key] = {}
    return _SRC_CACHE[key].get(v, '')

def grade_of(m):
    z, t = m['compress'], m['ttr']
    return ('A' if z >= 0.42 and t >= 0.58 else
            'B' if z >= 0.36 and t >= 0.50 else
            'C' if z >= 0.30 and t >= 0.45 else 'D')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book')
    ap.add_argument('--chapter',
                    help='restrict to one chapter — required for unattended '
                         'stamping, so a part-repaired book does not refuse on '
                         'the chapters not yet done')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--overwrite', action='store_true')
    ap.add_argument('--standard', choices=['legacy', 'current'], default='legacy',
                    help="'current' stamps a finished chapter to "
                         f"{QA.CURRENT_STANDARD} — refused unless every verse "
                         "grades A/B with no ungrounded voices")
    a = ap.parse_args()

    dates = chapter_dates()
    src = QA.SourceIndex(ROOT)
    pattern = os.path.join(ROOT, 'data/commentary/cow-synthesis', a.book or '*',
                           f'{a.chapter}.json' if a.chapter else '*.json')
    files = sorted(glob.glob(pattern))
    if not files:
        print(f'no files matched {pattern}', file=sys.stderr)
        return 2

    current = a.standard == 'current'
    if current and not a.book:
        print('--standard current is per-chapter work; pass --book (and normally '
              'one chapter\'s worth of files at a time)', file=sys.stderr)
        return 2

    stamped = skipped = 0
    grades = collections.Counter()
    touched = 0
    refused = []
    for prose_p in files:
        book = prose_p.split(os.sep)[-2]
        ch = os.path.basename(prose_p)[:-5]
        tags_p = prose_p.replace('cow-synthesis', 'cow-synthesis-tags')
        if not os.path.exists(tags_p):
            continue
        prose = json.load(open(prose_p, encoding='utf-8'))
        raw = open(tags_p, encoding='utf-8').read()
        tags = json.loads(raw)
        indent = detect_indent(raw)
        gen = dates.get((book, ch), '2026-07-22')
        changed = False
        for v, html in prose.items():
            t = tags.get(v)
            if not isinstance(t, dict):
                continue
            if 'qa' in t and not a.overwrite:
                skipped += 1
                continue
            m, _, _ = audit.verse_metrics(html)
            g = grade_of(m)
            ung = src.ungrounded_voices(book, ch, t.get('voices'))

            # The writer records the fidelity judgement as a sibling of `voices`;
            # we fold it into the qa block and fill `expansion` ourselves, so the
            # measured number cannot be typed in by hand and the judgement cannot
            # be synthesised by a script. Neither half is much use alone.
            fid = t.pop('fidelity', None) or (t.get('qa') or {}).get('fidelity')
            if fid is not None:
                fid = dict(fid)
                fid.setdefault('checked_by', 'self')
                fid['expansion'] = QA.expansion_ratio(
                    QA.visible(html) and len(QA.visible(html).split()),
                    len(QA.visible(source_text(book, ch, v)).split()))

            if current:
                probs = QA.fidelity_problems(fid, required=True)
                if probs:
                    refused.append(f'{book} {ch}:{v} fidelity — {probs[0]}'); continue
                # The current standard is a claim about quality, so it has to be
                # earned. Refuse rather than stamp a lie the CI gate will catch.
                if g not in ('A', 'B'):
                    refused.append(f'{book} {ch}:{v} grades {g}'); continue
                if ung:
                    refused.append(f'{book} {ch}:{v} ungrounded: {", ".join(ung)}'); continue
            grades[g] += 1
            qa = collections.OrderedDict([
                ('v', QA.QA_SCHEMA_VERSION),
                ('standard', QA.CURRENT_STANDARD if current else QA.LEGACY_STANDARD),
                ('generated', TODAY if current else gen),
                ('grade', g),
                ('checks', list(CURRENT_CHECKS if current else LEGACY_CHECKS)),
                ('lint', 'audit-synthesis-quality/1'),
            ])
            if fid is not None:
                qa['fidelity'] = fid
            if ung and not current:
                qa['ungrounded_voices'] = ung
            t['qa'] = qa
            stamped += 1
            changed = True
        if changed and not a.dry_run:
            with open(tags_p, 'w', encoding='utf-8') as fh:
                fh.write(json.dumps(tags, indent=indent, ensure_ascii=False)
                         + ('\n' if raw.endswith('\n') else ''))
            touched += 1

    print(f'{"would stamp" if a.dry_run else "stamped"}: {stamped} verses '
          f'across {touched or len(files)} files   (skipped {skipped} already stamped)')
    print('  grades:', dict(sorted(grades.items())))
    if refused:
        print(f'\n  REFUSED {len(refused)} verses — the current standard must be earned:')
        for r in refused[:20]:
            print(f'    {r}')
        if len(refused) > 20:
            print(f'    ... and {len(refused)-20} more')
        print('  Fix the prose and re-run; do not hand-edit the qa block.')
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
