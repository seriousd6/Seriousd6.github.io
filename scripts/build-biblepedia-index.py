#!/usr/bin/env python3
"""Build data/biblepedia/index.json — unified term index for Biblepedia.

Merges 4,417 BP articles + 5,322 Nave's topics + 2,616 Hitchcock names
into a single lightweight index that powers:
  - terms.js tooltip system (replaces 4 separate index fetches)
  - Biblepedia Quick Info sidebar panel
  - Home page browse / search / A-Z

Nave's content is absorbed into Biblepedia articles via nave_slugs; there
are no standalone Nave-only pages. Only full articles (has_article: true)
appear in the index.

Also writes nave_slugs back into each article JSON so biblepedia.js can
render the Nave's section without loading the full nave.json twice.

Each entry:
  id, term, category, brief, hitchcock_meaning,
  nave_topics [{slug, title, count}], key_refs, has_article
"""
import json, os, re, glob, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DATA-15: map any singular category variant to its canonical plural key so the index
# never contains both 'concept' and 'concepts' (the reader filters categories by exact match).
_CATEGORY_CANON = {
    'person': 'people', 'place': 'places', 'concept': 'concepts',
    'name': 'names', 'event': 'events',
}

def _norm_category(cat):
    return _CATEGORY_CANON.get(cat, cat or 'concepts')

# ── HTML utilities ────────────────────────────────────────────────────────────

def strip_html(html):
    if not html:
        return ''
    text = re.sub(r'<[^>]+>', '', html)
    text = (text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
                .replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' ')
                .replace('&#x2019;', "'").replace('&rsquo;', "'").replace('&ldquo;', '"')
                .replace('&rdquo;', '"'))
    return re.sub(r'\s+', ' ', text).strip()

def extract_brief(intro_html):
    """First sentence of intro, plain text, ≤ 200 chars."""
    text = strip_html(intro_html)
    if not text:
        return ''
    dot = text.find('. ', 40)
    if 0 < dot < 200:
        return text[:dot + 1]
    return text[:197] + ('…' if len(text) > 197 else '')

SMALLS = {'a', 'an', 'the', 'and', 'but', 'or', 'of', 'in', 'on', 'at', 'to',
           'by', 'for', 'with', 'from', 'into', 'unto', 'as'}

def normalize_title(title):
    """'AFFLICTIONS AND ADVERSITIES' → 'Afflictions and Adversities'"""
    words = title.strip().split()
    out = []
    for i, w in enumerate(words):
        out.append(w.lower() if (i > 0 and w.lower() in SMALLS) else w.capitalize())
    return ' '.join(out)

# ── Load sources ─────────────────────────────────────────────────────────────

def load(path):
    with open(os.path.join(BASE, path)) as f:
        return json.load(f)

nave_data  = load('data/topical/nave.json')
hitch_data = load('data/hitchcock/index.json')
dict_data  = load('data/dictionary/index.json')
smith_data = load('data/smith/index.json')

# ── Nave lookup maps ──────────────────────────────────────────────────────────

nave_by_slug = {}
nave_by_term = {}   # normalized-lowercase title → topic

for t in nave_data:
    s = t['slug']
    nave_by_slug[s] = t
    nt = normalize_title(t['title'])
    key = nt.lower()
    if key not in nave_by_term:
        nave_by_term[key] = t
    # Also raw uppercase title as key
    raw = t['title'].lower().strip()
    if raw not in nave_by_term:
        nave_by_term[raw] = t

hitch_by_id = {h['id'].lower(): h for h in hitch_data}

dict_brief_map  = {e['id']: e.get('brief', '') for e in dict_data}
smith_brief_map = {e['id']: e.get('brief', '') for e in smith_data}

# ── Process BP articles ───────────────────────────────────────────────────────

articles_dir  = os.path.join(BASE, 'data/biblepedia/articles')
article_files = sorted(glob.glob(os.path.join(articles_dir, '*.json')))

nave_covered  = set()   # slugs matched to a BP article
index_entries = []

def find_nave_for(art_id, term):
    """Return list of {slug, title, count} for matching Nave's topics."""
    results = []
    seen = set()

    def _add(t):
        if t and t['slug'] not in seen:
            seen.add(t['slug'])
            nave_covered.add(t['slug'])
            results.append({
                'slug':  t['slug'],
                'title': normalize_title(t['title']),
                'count': len(t.get('verses', []))
            })

    # 1) exact slug match
    _add(nave_by_slug.get(art_id))
    # 2) simple de-plural (kings → king)
    if not results:
        _add(nave_by_slug.get(art_id.rstrip('s')))
    # 3) term (lowercased) as title key
    if not results:
        _add(nave_by_term.get(term.lower()))
    # 4) article id with spaces instead of hyphens
    term_from_id = art_id.replace('-', ' ')
    if not results:
        _add(nave_by_term.get(term_from_id))
    return results

updated_articles = 0

for filepath in article_files:
    with open(filepath) as f:
        try:
            article = json.load(f)
        except Exception as e:
            print(f'  SKIP {filepath}: {e}', file=sys.stderr)
            continue

    art_id   = article.get('id', '')
    term     = article.get('term', '')
    # DATA-15: normalize to canonical plural category keys so the reader's exact-match
    # category browse (biblepedia.js _getItemsByCategory) doesn't drop singular variants.
    category = _norm_category(article.get('category', 'concepts'))
    key_refs = article.get('key_refs', [])[:6]
    intro    = article.get('intro', '')
    hm       = article.get('hitchcock_meaning')

    # Brief from intro, fallback to dict/smith index brief
    brief = extract_brief(intro)
    if not brief:
        fb = dict_brief_map.get(art_id) or smith_brief_map.get(art_id) or ''
        if fb:
            # strip trailing ellipsis placeholders like "A Alpha..."
            brief = extract_brief('<p>' + fb + '</p>')

    nav_topics = find_nave_for(art_id, term)
    nav_slugs  = [t['slug'] for t in nav_topics]

    # Write nave_slugs back into the article JSON (compact, in-place)
    if article.get('nave_slugs') != nav_slugs:
        article['nave_slugs'] = nav_slugs
        with open(filepath, 'w') as f:
            json.dump(article, f, separators=(',', ':'), ensure_ascii=False)
        updated_articles += 1

    index_entries.append({
        'id':                art_id,
        'term':              term,
        'category':          category,
        'brief':             brief,
        'hitchcock_meaning': hm,
        'nave_topics':       nav_topics,
        'key_refs':          key_refs,
        'has_article':       True,
    })

print(f'Processed {len(article_files)} articles ({updated_articles} updated with nave_slugs)')


# ── Sort and write ────────────────────────────────────────────────────────────

index_entries.sort(key=lambda e: e['term'].lower())

output_path = os.path.join(BASE, 'data/biblepedia/index.json')
with open(output_path, 'w') as f:
    json.dump(index_entries, f, separators=(',', ':'), ensure_ascii=False)

total   = len(index_entries)
matched = sum(1 for e in index_entries if e['nave_topics'])

size_kb = os.path.getsize(output_path) / 1024
print(f'\nWrote {total} entries → data/biblepedia/index.json ({size_kb:.0f} KB)')
print(f'  {total} full articles  |  {matched} with Nave\'s match')
