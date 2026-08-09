#!/usr/bin/env python3
"""
compose-study-tabs.py — turn a multi-part topical study into one tabbed page.

A five-part study authored as `index.astro` + `part-1..N.astro` becomes a single
page whose parts are sub-tabs, following the book-commentary chapter-picker
paradigm (see `.tg-tabs` in topic-guide.css and entries/study-tabs.js). The part
files are replaced by redirect stubs so existing links keep working.

    python3 scripts/compose-study-tabs.py korahs-rebellion --dry-run
    python3 scripts/compose-study-tabs.py salvation-assurance

Everything is inferred from the existing files — accent colour, hero variant,
title, description, part titles — so the transform carries no per-study
configuration and no prose is retyped. Tab labels default to a roman numeral
plus a short form of the part title; override with --labels if the defaults read
badly.

The script is idempotent-unsafe by design: it reads the ORIGINAL part files, so
run it once per study, from a clean tree, and check the diff.
"""
import os, re, sys, argparse, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
WORDS = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
         6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}

def read(p):
    return open(p, encoding='utf-8').read()

def one(pattern, text, what, flags=re.S):
    m = re.search(pattern, text, flags)
    if not m:
        sys.exit(f'could not find {what}')
    return m.group(1).strip()

def container_body(src):
    """Inner HTML of <main><div class="container"> … </div></main>."""
    body = src.split('<div class="container">', 1)[1].rsplit('</main>', 1)[0]
    return body.rstrip().removesuffix('</div>').rstrip()

def strip_related(body):
    """Drop the trailing related/continue strip; return (body, strip_html)."""
    m = re.search(r'(<div class="tg-related">.*?</div>\s*</div>|<div class="tg-related">.*?</div>)\s*$',
                  body, re.S)
    if not m:
        return body, ''
    return body[:m.start()].rstrip(), m.group(1).strip()

def short_label(title, limit=22):
    t = re.sub(r'^(The|A|An)\s+', '', title).split(':')[0].split('—')[0].strip()
    if len(t) <= limit:
        return t
    words, out = t.split(), []
    for w in words:
        if len(' '.join(out + [w])) > limit:
            break
        out.append(w)
    return ' '.join(out) or t[:limit]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slug', help='directory under src/pages/topics/')
    ap.add_argument('--labels', help='comma-separated tab labels, one per part')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()

    d = os.path.join(ROOT, 'src/pages/topics', a.slug)
    idx = os.path.join(d, 'index.astro')
    if not os.path.exists(idx):
        sys.exit(f'no such study: {idx}')
    parts = sorted(g for g in os.listdir(d) if re.fullmatch(r'part-\d+\.astro', g))
    if not parts:
        sys.exit('no part-N.astro files to compose')

    hub = read(idx)
    if 'tg-tabs' in hub:
        sys.exit('already composed — run this once per study, from a clean tree')

    title = one(r'<Base title=\{"(.*?)"\}', hub, 'the Base title')
    desc = one(r'description=\{"(.*?)"\}', hub, 'the Base description')
    hero_open = one(r'(<header class="tg-hero[^>]*>)', hub, 'the hero element')
    accent = one(r'--tg-accent:\s*([^;"]+)', hero_open, 'the accent colour')
    hero_inner = one(r'<div class="tg-hero__inner">(.*?)</div>\s*</header>', hub, 'the hero body')
    breadcrumb = one(r'(<nav class="tg-breadcrumb">.*?</nav>)', hub, 'the breadcrumb')

    overview = container_body(hub)
    # the part cards become the tab bar; keep their intro paragraph as the
    # overview lede so the framing survives
    lede = ''
    pm = re.search(r'<section class="tg-section" id="parts">(.*?)</section>', overview, re.S)
    if pm:
        lp = re.search(r'<p>(.*?)</p>', pm.group(1), re.S)
        if lp:
            lede = lp.group(1).strip()
        overview = overview.replace(pm.group(0), '').replace('\n\n\n', '\n\n')
    overview, related = strip_related(overview)

    panels = []
    for f in parts:
        s = read(os.path.join(d, f))
        body, _ = strip_related(container_body(s))
        panels.append({
            'id': f[:-6],
            'kicker': one(r'<span class="tg-hero__type">(.*?)</span>', s, f'{f} kicker'),
            'title': one(r'<h1 class="tg-hero__title">(.*?)</h1>', s, f'{f} title'),
            'intro': one(r'<p class="tg-hero__intro">(.*?)</p>', s, f'{f} intro'),
            'verse': one(r'<blockquote class="tg-hero__key-verse">(.*?)</blockquote>', s, f'{f} key verse'),
            'body': body.strip(),
        })

    labels = [l.strip() for l in a.labels.split(',')] if a.labels else \
             [f'{ROMAN[i]} · {short_label(p["title"])}' for i, p in enumerate(panels)]
    if len(labels) != len(panels):
        sys.exit(f'{len(labels)} labels for {len(panels)} parts')

    out = io.StringIO(); w = out.write
    w("---\nimport Base from '../../../layouts/Base.astro';\n---\n\n")
    w(f'<Base title={{"{title}"}} description={{"{desc}"}} '
      'bodyAttrs={{"class":"tg-study"}} entry="study-tabs">\n')
    w('<Fragment slot="head-end">\n<link rel="stylesheet" href="../../assets/css/topic-guide.css">\n</Fragment>\n')
    w(breadcrumb)
    w(hero_open + '\n    <div class="tg-hero__inner">' + hero_inner + '</div>\n  </header>')
    w(f'<main style="--tg-accent: {accent}">\n    <div class="container">\n\n')

    w('      <nav class="tg-tabs" aria-label="Study parts" data-current="overview">\n')
    w('        <span class="tg-tabs__label">Part</span>\n        <div class="tg-tabs__grid">\n')
    w('          <a class="tg-tabs__btn is-active" href="#overview" data-part="overview" aria-current="true">Overview</a>\n')
    for p, lab in zip(panels, labels):
        w(f'          <a class="tg-tabs__btn" href="#{p["id"]}" data-part="{p["id"]}">{lab}</a>\n')
    w('        </div>\n      </nav>\n\n')

    w('      <section class="tg-part" id="overview" aria-labelledby="overview-h">\n')
    w('        <div class="tg-part__head">\n          <span class="tg-part__kicker">Overview</span>\n')
    w(f'          <h2 class="tg-part__title" id="overview-h">'
      f'A Study in {WORDS.get(len(panels), len(panels))} Parts</h2>\n')
    if lede:
        w(f'          <p class="tg-part__intro">{lede} Use the tabs above to move between them.</p>\n')
    w('        </div>\n' + overview.strip() + '\n      </section>\n\n')

    for p in panels:
        w(f'      <section class="tg-part" id="{p["id"]}" aria-labelledby="{p["id"]}-h">\n')
        w('        <div class="tg-part__head">\n')
        w(f'          <span class="tg-part__kicker">{p["kicker"]}</span>\n')
        w(f'          <h2 class="tg-part__title" id="{p["id"]}-h">{p["title"]}</h2>\n')
        w(f'          <p class="tg-part__intro">{p["intro"]}</p>\n')
        w(f'          <blockquote class="tg-part__verse">{p["verse"]}</blockquote>\n')
        w('        </div>\n' + p['body'] + '\n      </section>\n\n')

    if related:
        w('      ' + related + '\n\n')
    w('    </div>\n  </main>\n</Base>\n')
    composed = out.getvalue()

    study_name = re.split(r'\s+—\s+', title)[0]
    stubs = {}
    for i, p in enumerate(panels):
        r = ROMAN[i]
        stubs[p['id']] = f'''---
// /topics/{a.slug}/{p["id"]}.html — RETIRED ({__import__("datetime").date.today().isoformat()}).
// The parts became sub-tabs on one page, following the book-commentary
// chapter-picker paradigm, so the study is read without page loads between
// parts. Kept as a redirect so bookmarks, inbound links, and cached PWA
// entries still land on the right part.
---

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Redirecting… — {study_name}, Part {r}</title>
  <meta name="robots" content="noindex" />
  <meta http-equiv="refresh" content="0; url=/topics/{a.slug}/#{p["id"]}" />
  <script is:inline>window.location.replace('/topics/{a.slug}/#{p["id"]}');</script>
</head>
<body><p>Part {r} is now a tab on the <a href="/topics/{a.slug}/#{p["id"]}">{study_name}</a> study. Redirecting…</p></body>
</html>
'''

    print(f'{a.slug}: {len(panels)} parts -> 1 page with {len(panels)+1} tabs')
    for p, lab in zip(panels, labels):
        print(f'    {p["id"]}  "{lab}"  — {p["title"]}')
    if a.dry_run:
        print('  (dry run — nothing written)')
        return 0
    open(idx, 'w', encoding='utf-8').write(composed)
    for pid, stub in stubs.items():
        open(os.path.join(d, f'{pid}.astro'), 'w', encoding='utf-8').write(stub)
    print(f'  wrote index.astro ({len(composed.splitlines())} lines) + '
          f'{len(stubs)} redirect stubs')
    return 0

if __name__ == '__main__':
    sys.exit(main())
