"""
BPG Gap Analysis — Compute Biblepedia Coverage Gaps

Compares all source indexes and produces data/biblepedia/gaps.json.
This is a deterministic compute script — no content generation required.

Sources analyzed:
  - data/dictionary/index.json  (Easton's: 3,963 entries)
  - data/smith/index.json       (Smith's: 4,639 entries)
  - data/isbe/index.json        (ISBE: 9,380 entries)
  - data/hitchcock/index.json   (Hitchcock's Names: 2,616 entries)
  - data/topical/nave.json      (Nave's Topics: 5,322 entries)

Output: data/biblepedia/gaps.json
Run: python3 scripts/bpg-compute-gaps.py
"""

import json, os, re
from collections import defaultdict

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DICT_IDX   = os.path.join(ROOT, 'data/dictionary/index.json')
SMITH_IDX  = os.path.join(ROOT, 'data/smith/index.json')
ISBE_IDX   = os.path.join(ROOT, 'data/isbe/index.json')
HITCH_IDX  = os.path.join(ROOT, 'data/hitchcock/index.json')
NAVE_FILE  = os.path.join(ROOT, 'data/topical/nave.json')
ARTICLES   = os.path.join(ROOT, 'data/biblepedia/articles')
OUT_FILE   = os.path.join(ROOT, 'data/biblepedia/gaps.json')
os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

# ── Core doctrine keywords for priority boosting ──────────────────────────────
DOCTRINE_KEYWORDS = {
    'faith', 'grace', 'salvation', 'redemption', 'atonement', 'justification',
    'sanctification', 'glorification', 'resurrection', 'trinity', 'incarnation',
    'reconciliation', 'forgiveness', 'repentance', 'regeneration', 'baptism',
    'covenant', 'election', 'predestination', 'prayer', 'worship', 'sin',
    'judgment', 'heaven', 'hell', 'eternal', 'spirit', 'holy spirit',
    'scripture', 'revelation', 'prophecy', 'messiah', 'kingdom', 'church',
    'gospel', 'love', 'obedience', 'righteousness', 'holiness', 'mercy',
    'wrath', 'justice', 'sacrifice', 'priest', 'king', 'prophet',
}

# ── Slug helpers ──────────────────────────────────────────────────────────────
def make_slug(term):
    s = term.lower()
    s = re.sub(r'[,\'\"\(\)]', '', s)
    s = re.sub(r'[\s\-/]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s

def normalize(term):
    return re.sub(r'[^a-z0-9\s]', '', term.lower()).strip()

# ── Load all source indexes ───────────────────────────────────────────────────
print('Loading source indexes...')
easton = json.load(open(DICT_IDX,  encoding='utf-8'))
smith  = json.load(open(SMITH_IDX, encoding='utf-8'))
isbe   = json.load(open(ISBE_IDX,  encoding='utf-8'))
hitch  = json.load(open(HITCH_IDX, encoding='utf-8'))
nave   = json.load(open(NAVE_FILE, encoding='utf-8'))
print(f'  Easton: {len(easton)}, Smith: {len(smith)}, ISBE: {len(isbe)}, Hitch: {len(hitch)}, Nave: {len(nave)}')

# ── Build normalized lookup sets ─────────────────────────────────────────────
easton_norms = { normalize(e['term']): e for e in easton }
smith_norms  = { normalize(e['term']): e for e in smith  }
isbe_norms   = { normalize(e['term']): e for e in isbe   }
hitch_norms  = { normalize(e['term']): e for e in hitch  }

# Build a map of slugs already synthesized
existing_slugs = set()
if os.path.isdir(ARTICLES):
    for fn in os.listdir(ARTICLES):
        if fn.endswith('.json'):
            existing_slugs.add(fn[:-5])

print(f'  Existing synthesized articles: {len(existing_slugs)}')

# ── Gap detection ─────────────────────────────────────────────────────────────
# A "gap" is a topic in at least one source with no article in the three main
# dictionary sources (Easton + Smith + ISBE). This means:
#   - Nave-only topics (topical concept but no dictionary article)
#   - Smith-only entries (in Smith but not Easton)
#   - ISBE-only entries (scholarly entries absent from both Easton and Smith)
#   - Hitchcock names with no dict article

gaps = []

# ── 1. Nave-only topics ───────────────────────────────────────────────────────
print('Finding Nave-only topic gaps...')
for topic in nave:
    title = topic.get('title', '')
    if not title: continue
    n = normalize(title)
    # Exact match only — compound Nave topics like "AFFLICTIONS AND ADVERSITIES" are
    # distinct from a brief Easton entry on "AFFLICTIONS"; prefix/substring matching
    # would incorrectly suppress high-value topical gaps.
    in_easton = n in easton_norms
    in_smith  = n in smith_norms
    in_isbe   = n in isbe_norms
    if in_easton or in_smith or in_isbe:
        continue  # Already covered

    slug = make_slug(title)
    verse_count = len(topic.get('verses', []))
    words = set(n.split())
    is_doctrine = bool(words & DOCTRINE_KEYWORDS)
    hitchcock_e = hitch_norms.get(n)
    isbe_e = isbe_norms.get(n)

    # Gap type
    practice_words = {'prayer', 'worship', 'fasting', 'baptism', 'communion', 'ministry', 'giving'}
    virtue_words   = {'faith', 'hope', 'love', 'joy', 'peace', 'patience', 'humility', 'zeal', 'obedience', 'thankfulness'}
    vice_words     = {'pride', 'anger', 'envy', 'malice', 'hypocrisy', 'covetousness', 'impatience', 'rebellion'}
    prophetic_words = {'prophecies', 'prophecy', 'israel', 'restoration', 'kingdom'}

    if words & prophetic_words and 'prophecies' in n:
        gap_type = 'prophetic'
    elif words & practice_words:
        gap_type = 'practice'
    elif words & virtue_words:
        gap_type = 'virtue'
    elif words & vice_words:
        gap_type = 'vice'
    elif is_doctrine:
        gap_type = 'doctrine-no-article'
    else:
        gap_type = 'concept-no-article'

    # Priority score (0–100): verse count dominates for Nave topics
    score = 0
    if verse_count >= 500:   score += 50
    elif verse_count >= 200: score += 40
    elif verse_count >= 100: score += 30
    elif verse_count >= 50:  score += 20
    elif verse_count >= 20:  score += 10
    else:                    score += 3
    score += 30 if is_doctrine else 0
    score += 15 if isbe_e else 0
    score += 5  if hitchcock_e else 0

    gaps.append({
        'id': slug,
        'term': title.title() if title == title.upper() else title,
        'original_title': title,
        'gap_type': gap_type,
        'sources_present': ['nave'],
        'sources_absent': ['easton', 'smith', 'isbe'],
        'nave_verse_count': verse_count,
        'nave_slug': topic.get('slug', slug),
        'isbe_id': isbe_e['id'] if isbe_e else None,
        'smith_id': None,
        'hitchcock_meaning': hitchcock_e['meaning'] if hitchcock_e else None,
        'priority_score': min(100, score),
        'status': 'already-covered' if slug in existing_slugs else 'not-reviewed',
    })

print(f'  Nave-only gaps: {len(gaps)}')

# ── 2. Smith-only entries (not in Easton) ─────────────────────────────────────
print('Finding Smith-only entry gaps...')
smith_only_count = 0
for e in smith:
    n = normalize(e['term'])
    if n in easton_norms: continue  # Covered by Easton
    # Also check isbe
    in_isbe = n in isbe_norms
    slug = make_slug(e['term'])
    hitchcock_e = hitch_norms.get(n)
    score = 10  # base score for any Smith entry
    score += 15 if in_isbe else 0
    score += 10 if hitchcock_e else 0
    brief = e.get('brief', '')
    # Detect probable type
    place_signals = ['city', 'town', 'village', 'mount', 'valley', 'river', 'sea of', 'region', 'land of']
    is_place = any(s in brief.lower() for s in place_signals)
    gap_type = 'smith-place' if is_place else ('smith-person' if hitchcock_e else 'smith-scholarly')
    gaps.append({
        'id': slug,
        'term': e['term'],
        'original_title': e['term'],
        'gap_type': gap_type,
        'sources_present': ['smith'] + (['isbe'] if in_isbe else []),
        'sources_absent': ['easton'] + ([] if in_isbe else ['isbe']),
        'nave_verse_count': 0,
        'nave_slug': None,
        'isbe_id': isbe_norms[n]['id'] if in_isbe else None,
        'smith_id': e['id'],
        'hitchcock_meaning': hitchcock_e['meaning'] if hitchcock_e else None,
        'priority_score': score,
        'status': 'already-covered' if slug in existing_slugs else 'not-reviewed',
    })
    smith_only_count += 1

print(f'  Smith-only gaps: {smith_only_count}')

# ── 3. ISBE-only entries (not in Easton or Smith) ─────────────────────────────
print('Finding ISBE-only entry gaps...')
isbe_only_count = 0
for e in isbe:
    n = normalize(e['term'])
    if n in easton_norms or n in smith_norms: continue
    slug = make_slug(e['term'])
    hitchcock_e = hitch_norms.get(n)
    score = 5  # base; ISBE-only is lower priority
    score += 10 if hitchcock_e else 0
    brief = e.get('brief', '')
    place_signals = ['city', 'town', 'village', 'mount', 'valley', 'river', 'sea of', 'region', 'land of']
    is_place = any(s in brief.lower() for s in place_signals)
    gap_type = 'isbe-place' if is_place else ('isbe-person' if hitchcock_e else 'isbe-scholarly')
    gaps.append({
        'id': slug,
        'term': e['term'],
        'original_title': e['term'],
        'gap_type': gap_type,
        'sources_present': ['isbe'],
        'sources_absent': ['easton', 'smith'],
        'nave_verse_count': 0,
        'nave_slug': None,
        'isbe_id': e['id'],
        'smith_id': None,
        'hitchcock_meaning': hitchcock_e['meaning'] if hitchcock_e else None,
        'priority_score': score,
        'status': 'already-covered' if slug in existing_slugs else 'not-reviewed',
    })
    isbe_only_count += 1

print(f'  ISBE-only gaps: {isbe_only_count}')

# ── Deduplicate by id (keep highest priority_score) ──────────────────────────
print('Deduplicating...')
deduped = {}
for g in gaps:
    gid = g['id']
    if gid not in deduped or g['priority_score'] > deduped[gid]['priority_score']:
        deduped[gid] = g

# Sort by priority_score descending, then term ascending
final = sorted(deduped.values(), key=lambda g: (-g['priority_score'], g['term'].lower()))

# ── Write output ──────────────────────────────────────────────────────────────
with open(OUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print(f'\n✓ Wrote {len(final)} gap entries to {OUT_FILE}')

# Summary breakdown
from collections import Counter
by_type   = Counter(g['gap_type'] for g in final)
by_status = Counter(g['status']   for g in final)
print('\nBy gap type:')
for t, c in sorted(by_type.items(), key=lambda x: -x[1]):
    print(f'  {t:<30} {c}')
print('\nBy status:')
for s, c in sorted(by_status.items(), key=lambda x: -x[1]):
    print(f'  {s:<25} {c}')
print(f'\nTop 20 highest-priority gaps:')
for g in final[:20]:
    print(f"  [{g['priority_score']:3d}] {g['term']:<40} {g['gap_type']}")
