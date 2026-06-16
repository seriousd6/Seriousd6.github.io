"""
Data-integrity checks for the Bible study site. Fast, high-signal assertions over the
data the app depends on — the kind of breakage that is invisible in code review but
breaks the live site (a father with no article, an out-of-range red-letter verse, a
stale offline manifest pointing at a missing file).

Run from repo root:  python3 scripts/validate-data.py
Exits non-zero on any FAIL, so it can gate CI. Add checks as features grow.
"""

import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent.parent
fails = []
def check(ok, msg):
    print(('  ok  ' if ok else 'FAIL  ') + msg)
    if not ok:
        fails.append(msg)


def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))


# 1 — Key index/manifest files parse as JSON.
print('\n[1] core JSON parses')
for p in ['data/biblepedia/index.json', 'data/biblepedia/links.json', 'data/library/index.json',
          'data/red-letter.json', 'data/offline-manifest.json',
          'data/maps/regions.json',                  # canonical region geometry
          'data/sections-index.json', 'data/sections-aliases.json', 'data/sections-body.json',  # topical search
          'data/commentary/cow/john/1.json']:   # per-chapter served Cloud of Witnesses file
    try:
        load(p); check(True, p)
    except Exception as e:
        check(False, f'{p}: {e}')


# 2 — Cloud of Witnesses: every Father in _CATENA_ROWS has a Biblepedia article whose
#     slug matches cowSlug(). This is the exact gap that left names linking to nothing.
print('\n[2] Cloud of Witnesses father → Biblepedia article coverage')
core = (ROOT / 'assets/js/core.js').read_text()
block = core[core.find('var _CATENA_ROWS'):core.find('export var CATENA_FATHERS')]
displays = re.findall(r"\['([^']+)','[^']*','[^']*',\[", block)
slug = lambda n: re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')
art = ROOT / 'data/biblepedia/articles'
missing = [d for d in displays if not (art / f'{slug(d)}.json').exists()]
check(not missing, f'{len(displays)} fathers, missing articles: {missing}')


# 3 — Red-letter ranges are well-formed and within each chapter's verse count.
print('\n[3] red-letter ranges valid & in-range')
rl = load('data/red-letter.json')
bad = []
for speaker, books in rl.items():
    for book, chapters in books.items():
        ilp = ROOT / 'data/interlinear' / f'{book}.json'
        inv = json.loads(ilp.read_text()) if ilp.exists() else None
        for ch, ranges in chapters.items():
            maxv = max((int(v) for v in inv[ch]), default=0) if (inv and ch in inv) else 10**6
            for r in ranges:
                if not (isinstance(r, list) and len(r) == 2 and 1 <= r[0] <= r[1] <= maxv):
                    bad.append(f'{speaker} {book} {ch} {r}')
check(not bad, f'{sum(len(c) for b in rl.values() for c in b.values())} ranges; bad: {bad[:8]}')


# 4 — Offline manifest points only at files that exist (sample-safe: checks all paths).
print('\n[4] offline manifest references exist')
man = load('data/offline-manifest.json')
absent = []
for g in man['groups']:
    for f in g['files']:
        if not (ROOT / f).exists():
            absent.append(f)
            if len(absent) > 8:
                break
check(not absent, f'{sum(g["count"] for g in man["groups"])} files; absent: {absent[:8]}')


# 5 — Served Cloud of Witnesses commentary is per-chapter HTML-string files {v:str}.
#     Commentary is now split into data/commentary/{src}/{book}/{ch}.json (split-commentary.py
#     / cow-merge.py) so a verse tap fetches one chapter, not the whole (up to 14 MB) book.
print('\n[5] Cloud of Witnesses served shape (per-chapter)')
for book in ['matthew', 'mark', 'luke', 'john']:
    bookdir = ROOT / 'data/commentary/cow' / book
    if not bookdir.is_dir():
        continue
    chfiles = sorted(bookdir.glob('*.json'))
    nverses, ok = 0, bool(chfiles)
    for cf in chfiles:
        ch = json.loads(cf.read_text())
        if not all(isinstance(v, str) and v for v in ch.values()):
            ok = False
        nverses += len(ch)
    check(ok, f'{book}: {len(chfiles)} chapter files, {nverses} verse keys, all str')


print()
if fails:
    print(f'{len(fails)} FAILURE(S)')
    sys.exit(1)
print('all data checks passed')
