#!/usr/bin/env python3
"""Build data/biblepedia/strongs/{article_id}.json — Original Language Connections.

For each Biblepedia article, finds Hebrew/Greek Strong's words that are
translated into the article's term in the interlinear data. Outputs one
JSON file per article that has connections, containing:
  - code, lang, lemma, translit, gloss, def
  - count: times translated as this term
  - total: total occurrences of this code in the interlinear
  - books: {book_id: count} distribution (only books with matches)
"""
import json, os, re, glob, sys, time
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(path):
    with open(os.path.join(BASE, path)) as f:
        return json.load(f)

print('Loading Strong\'s dictionaries…')
greek_dict  = load('data/strongs/greek.json')
hebrew_dict = load('data/strongs/hebrew.json')
bdb_dict    = load('data/strongs/bdb.json')
thayer_dict = load('data/strongs/thayer.json')

print('Loading book order…')
books_meta = load('data/bible/books.json')
BOOK_ORDER = [b['id'] for b in books_meta]  # canonical order

# ── Phase 1: scan all interlinear data ───────────────────────────────────────

interlinear_dir = os.path.join(BASE, 'data/interlinear')

# code → {book → {text → count}}
code_data = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
# code → total occurrences across all books/texts
code_totals = defaultdict(int)

print('Scanning interlinear data…')
t0 = time.time()
for fname in sorted(os.listdir(interlinear_dir)):
    if not fname.endswith('.json'):
        continue
    book = fname[:-5]  # strip .json
    with open(os.path.join(interlinear_dir, fname)) as f:
        data = json.load(f)
    for ch, verses in data.items():
        for v, tokens in verses.items():
            for tok in tokens:
                code = tok.get('s', '').strip()
                text = tok.get('text', '').strip()
                if not code or not text:
                    continue
                code_data[code][book][text] += 1
                code_totals[code] += 1

print(f'  {len(code_data)} unique codes, {sum(code_totals.values())} tokens ({time.time()-t0:.1f}s)')

# ── Phase 2: word-level inverted index ───────────────────────────────────────
# word (lowercase, alpha) → list of (text, code, book, count)

print('Building inverted text index…')
t1 = time.time()
word_index = defaultdict(list)

for code, book_data in code_data.items():
    for book, text_counts in book_data.items():
        for text, count in text_counts.items():
            words = re.findall(r'[a-z]{3,}', text.lower())
            for word in set(words):
                word_index[word].append((text, code, book, count))

print(f'  {len(word_index)} index words ({time.time()-t1:.1f}s)')

# ── Phase 3: look up connections per article ──────────────────────────────────

def get_strongs_meta(code):
    lang = 'hebrew' if code.startswith('H') else 'greek'
    if lang == 'hebrew':
        base = hebrew_dict.get(code, {})
        lex  = bdb_dict.get(code, {})
    else:
        base = greek_dict.get(code, {})
        lex  = thayer_dict.get(code, {})
    lemma   = lex.get('lemma') or base.get('lemma', '')
    translit = lex.get('translit') or base.get('translit', '')
    gloss   = base.get('gloss', '')
    defn    = lex.get('short_def') or base.get('def', '')
    return lang, lemma, translit, gloss, defn

def build_pattern(term):
    """Regex that matches term as a whole word within token text, case-insensitive."""
    return re.compile(r'(?<![a-z])' + re.escape(term.lower()) + r'(?![a-z])', re.I)

def term_key_words(term):
    """Extract significant words (3+ alpha chars, not stopwords) from term."""
    STOPS = {'the','and','but','for','with','from','into','unto','upon','over',
              'under','also','this','that','they','them','their','there','when',
              'then','thus','both','each','more','most','some','very','than',
              'not','nor','yet','all','any','one','two','may','can','was','are',
              'has','had','have','been','were','will','shall','let','out','her',
              'his','him','its','our','your','who','whom','which','what','how'}
    words = re.findall(r'[a-z]{3,}', term.lower())
    sig = [w for w in words if w not in STOPS]
    return sig if sig else words

MIN_MATCH_COUNT = 2    # ignore codes with fewer than this many matches
MIN_MATCH_RATIO = 0.005  # at least 0.5% of total occurrences must match this term
MAX_CONNECTIONS = 12  # max codes per article

articles_dir = os.path.join(BASE, 'data/biblepedia/articles')
out_dir      = os.path.join(BASE, 'data/biblepedia/strongs')
os.makedirs(out_dir, exist_ok=True)

article_files = sorted(glob.glob(os.path.join(articles_dir, '*.json')))
print(f'\nProcessing {len(article_files)} articles…')
t2 = time.time()

written = 0
skipped = 0

for filepath in article_files:
    with open(filepath) as f:
        try:
            article = json.load(f)
        except Exception:
            continue

    art_id = article.get('id', '')
    term   = article.get('term', '')
    if not art_id or not term:
        continue

    pattern   = build_pattern(term)
    key_words = term_key_words(term)

    # Gather candidate (text, code, book, count) tuples via inverted index
    candidates = {}  # (text, code, book) → count
    for word in key_words:
        for text, code, book, count in word_index.get(word, []):
            key = (text, code, book)
            if key not in candidates:
                candidates[key] = count

    # Verify each candidate with the full pattern and aggregate by code
    code_results = defaultdict(lambda: defaultdict(int))  # code → {book → count}

    for (text, code, book), count in candidates.items():
        if pattern.search(text):
            code_results[code][book] += count

    if not code_results:
        skipped += 1
        continue

    # Build connection list, filter and sort by match count
    connections = []
    for code, book_counts in code_results.items():
        total_match = sum(book_counts.values())
        total_occ = code_totals[code]
        if total_match < MIN_MATCH_COUNT:
            continue
        if total_occ > 0 and (total_match / total_occ) < MIN_MATCH_RATIO:
            continue
        lang, lemma, translit, gloss, defn = get_strongs_meta(code)
        # Books dict: only books with matches, in canonical order
        books_ordered = {b: book_counts[b] for b in BOOK_ORDER if b in book_counts}
        connections.append({
            'code':    code,
            'lang':    lang,
            'lemma':   lemma,
            'translit': translit,
            'gloss':   gloss,
            'def':     defn,
            'count':   total_match,
            'total':   code_totals[code],
            'books':   books_ordered,
        })

    if not connections:
        skipped += 1
        continue

    connections.sort(key=lambda c: -c['count'])
    connections = connections[:MAX_CONNECTIONS]

    out_path = os.path.join(out_dir, art_id + '.json')
    with open(out_path, 'w') as f:
        json.dump({'connections': connections}, f, separators=(',', ':'), ensure_ascii=False)
    written += 1

elapsed = time.time() - t2
print(f'  Written: {written}  |  No connections: {skipped}  |  {elapsed:.1f}s')
print(f'\nDone → data/biblepedia/strongs/ ({written} files)')
