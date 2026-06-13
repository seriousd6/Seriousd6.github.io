#!/usr/bin/env python3
"""Build data/interlinear/align/{book}.json — token-to-translation alignment index.

For each interlinear token in each verse, computes the [char_start, char_len] span
in each translation's verse text that best corresponds to that token. This allows
interlinear.js to highlight exactly the right English word when hovering a tile,
even when the interlinear gloss uses different words than the active translation.

Algorithm per token:
  1. Extract content words from the token's English gloss (strip stop words, possessives,
     common morphological suffixes).
  2. Try each candidate word against the translation verse text (longest first) using
     word-boundary regex, including +/- trailing 's' for plural/singular variants.
  3. Record [char_start, len_of_matched_text] or null if no match found.

Output: data/interlinear/align/{book}.json
  {ch: {v: {trans_id: [[start,len]|null, ...one per token]}}}
"""

import json, os, re, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(path):
    with open(os.path.join(BASE, path)) as f:
        return json.load(f)

TRANSLATIONS = ['KJV', 'ASV', 'WEB', 'BSB', 'MKT-L', 'MKT-M', 'MKT-T']

# MKT translations use a different path and schema ({ch:{v:text}}, no "chapters" wrapper)
MKT_TIER = {'MKT-L': 'literal', 'MKT-M': 'mediating', 'MKT-T': 'thought'}
MKT_DRAFT_ROOT = os.path.join(BASE, 'data', 'translation', 'draft')

STOP = {
    'a','an','the','of','in','to','and','or','not','is','it','he','she','his',
    'her','my','thy','me','him','was','be','by','as','at','so','we','no','do',
    'but','for','on','with','from','that','this','are','have','has','had','its',
    'our','your','who','they','them','their','i','you','us','which','what','whom',
    'whose','when','where','will','would','shall','should','may','might','can',
    'could','am','were','been','being','into','upon','then','after','before',
    'also','now','here','there','up','out','if','how','all','one','more','up',
    'than','yet','even','over','own','did','said','unto','down','off','hath',
    'art','thou','thee','ye','doth','dost','thine','hast','wilt',
}

# Quasi-function words: not stop words, but low-specificity — determiners, quantifiers,
# common generic adjectives/adverbs. Tried only after true content words fail.
QUASI = {
    'every','each','both','some','any','many','few','several','much','less',
    'other','another','same','such','else','whole','half','either','neither',
    'just','still','again','thus','very','well','away','back','else',
    'first','last','next','high','low','far','near','long','short','full',
    'true','right','left','good','great','old','new','small','large','little',
    'like','way','make','take','give','come','know','see','say',
}

def content_words(text):
    """Return gloss words in two tiers: nouns/verbs first (tier 1), then quasi-function
    words (tier 2). Within each tier, sorted longest-first for specificity. Stop words
    and possessives are stripped before ranking."""
    raw = re.findall(r"[a-zA-Z']+", text.lower())
    seen, tier1, tier2 = set(), [], []
    for w in raw:
        w = re.sub(r"'s$|s'$", '', w)
        if w in STOP or len(w) <= 2 or w in seen:
            continue
        seen.add(w)
        (tier2 if w in QUASI else tier1).append(w)
    tier1.sort(key=len, reverse=True)
    tier2.sort(key=len, reverse=True)
    return tier1 + tier2

def find_span(verse_text, candidates):
    """Return [char_start, char_len] for the first candidate found (word boundary,
    case-insensitive). Tries exact match, then ±'s' for plural/singular. None if miss."""
    for w in candidates:
        esc = re.escape(w)
        m = re.search(r'\b' + esc + r'\b', verse_text, re.I)
        if m:
            return [m.start(), len(m.group(0))]
        # try with trailing 's' (singular → plural)
        if not w.endswith('s'):
            m = re.search(r'\b' + esc + r's\b', verse_text, re.I)
            if m:
                return [m.start(), len(m.group(0))]
        # try without trailing 's' (plural → singular), must keep stem ≥3 chars
        elif len(w) > 3:
            m = re.search(r'\b' + re.escape(w[:-1]) + r'\b', verse_text, re.I)
            if m:
                return [m.start(), len(m.group(0))]
    return None

print('Loading book metadata…')
books_meta = load('data/bible/books.json')
book_ids   = [b['id'] for b in books_meta]

out_dir = os.path.join(BASE, 'data', 'interlinear', 'align')
os.makedirs(out_dir, exist_ok=True)

t0 = time.time()
total_tokens = matched = written = 0

for book_id in book_ids:
    il_path = os.path.join(BASE, 'data', 'interlinear', book_id + '.json')
    if not os.path.exists(il_path):
        continue

    with open(il_path) as f:
        il = json.load(f)

    # Load available translations for this book
    trans_chapters = {}
    for t in TRANSLATIONS:
        if t in MKT_TIER:
            tp = os.path.join(MKT_DRAFT_ROOT, MKT_TIER[t], book_id + '.json')
            if os.path.exists(tp):
                with open(tp) as f:
                    trans_chapters[t] = json.load(f)  # flat {ch:{v:text}}
        else:
            tp = os.path.join(BASE, 'data', 'bible', t, book_id + '.json')
            if os.path.exists(tp):
                with open(tp) as f:
                    trans_chapters[t] = json.load(f).get('chapters', {})

    if not trans_chapters:
        continue

    book_align = {}

    for ch_str, verses in il.items():
        book_align[ch_str] = {}
        for v_str, tokens in verses.items():
            verse_align = {}
            for trans, chapters in trans_chapters.items():
                verse_text = chapters.get(ch_str, {}).get(v_str, '')
                if not verse_text:
                    verse_align[trans] = [None] * len(tokens)
                    continue
                spans = []
                for tok in tokens:
                    cw   = content_words(tok.get('text', ''))
                    span = find_span(verse_text, cw)
                    spans.append(span)
                    total_tokens += 1
                    if span:
                        matched += 1
                verse_align[trans] = spans
            book_align[ch_str][v_str] = verse_align

    out_path = os.path.join(out_dir, book_id + '.json')
    with open(out_path, 'w') as f:
        json.dump(book_align, f, separators=(',', ':'), ensure_ascii=False)
    written += 1

elapsed = time.time() - t0
pct = 100 * matched / total_tokens if total_tokens else 0
print(f'  {written} books, {total_tokens:,} tokens, {pct:.1f}% matched ({elapsed:.1f}s)')
print(f'Done → data/interlinear/align/ ({written} files)')
