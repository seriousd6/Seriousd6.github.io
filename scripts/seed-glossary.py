#!/usr/bin/env python3
"""
scripts/seed-glossary.py — generate initial draft translation glossary
from existing Strong's data and interlinear frequency counts.

Outputs:
  data/translation/glossary-greek.json        (one entry per G code)
  data/translation/glossary-hebrew.json       (one entry per H code)
  data/translation/glossary-phrases-greek.json  (empty scaffold)
  data/translation/glossary-phrases-hebrew.json (empty scaffold)

Run once to seed; thereafter the Workshop UI manages all edits.
Entries already present in the output files are NOT overwritten, so
the script is safe to re-run after seeding begins.
"""
import json
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRONGS     = os.path.join(ROOT, 'data', 'strongs')
INTERLINEAR = os.path.join(ROOT, 'data', 'interlinear')
OUT         = os.path.join(ROOT, 'data', 'translation')

# NT canonical order
NT_BOOKS = [
    'matthew', 'mark', 'luke', 'john', 'acts',
    'romans', '1corinthians', '2corinthians', 'galatians', 'ephesians',
    'philippians', 'colossians', '1thessalonians', '2thessalonians',
    '1timothy', '2timothy', 'titus', 'philemon', 'hebrews',
    'james', '1peter', '2peter', '1john', '2john', '3john', 'jude', 'revelation',
]

OT_BOOKS = [
    'genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy',
    'joshua', 'judges', 'ruth', '1samuel', '2samuel',
    '1kings', '2kings', '1chronicles', '2chronicles',
    'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs',
    'ecclesiastes', 'songofsolomon', 'isaiah', 'jeremiah', 'lamentations',
    'ezekiel', 'daniel', 'hosea', 'joel', 'amos', 'obadiah',
    'jonah', 'micah', 'nahum', 'habakkuk', 'zephaniah', 'haggai',
    'zechariah', 'malachi',
]

# Dispute levels for theologically contested terms (0–4)
DISPUTED_GREEK = {
    'G1342': 4,  # δίκαιος — righteous/just
    'G1343': 4,  # δικαιοσύνη — righteousness/justification
    'G4561': 4,  # σάρξ — flesh/sinful nature
    'G166':  3,  # αἰώνιος — eternal/age-long
    'G3056': 3,  # λόγος — Word/word/reason
    'G26':   3,  # ἀγάπη — love/charity
    'G4151': 3,  # πνεῦμα — spirit/Spirit
    'G3551': 3,  # νόμος — law/Law
    'G4102': 3,  # πίστις — faith/faithfulness
    'G2316': 2,  # θεός — God/god
    'G2041': 2,  # ἔργον — work/deed
    'G1680': 2,  # ἐλπίς — hope
    'G3962': 2,  # πατήρ — father/Father
    'G2222': 2,  # ζωή — life
    'G40':   2,  # ἅγιος — holy/saint
    'G3498': 2,  # νεκρός — dead
    'G5485': 2,  # χάρις — grace/favor
    'G2842': 2,  # κοινωνία — fellowship/communion/sharing
    'G3340': 2,  # μετανοέω — repent/change one's mind
    'G0907': 2,  # βαπτίζω — baptize/immerse
    'G3670': 2,  # ὁμολογέω — confess/acknowledge
}

DISPUTED_HEBREW = {
    'H430':  4,  # אֱלֹהִים — God/gods
    'H7307': 4,  # רוּחַ — spirit/Spirit/wind/breath
    'H2617': 4,  # חֶסֶד — steadfast love/lovingkindness/mercy
    'H3068': 4,  # יהוה — LORD/Yahweh/Jehovah
    'H5315': 3,  # נֶפֶשׁ — soul/life/self
    'H1285': 3,  # בְּרִית — covenant
    'H6666': 3,  # צְדָקָה — righteousness/justice
    'H571':  2,  # אֱמֶת — truth/faithfulness
    'H2580': 2,  # חֵן — grace/favor
    'H8199': 2,  # שָׁפַט — judge/govern
    'H4428': 2,  # מֶלֶךְ — king
    'H5769': 3,  # עוֹלָם — eternal/everlasting/age
    'H3519': 2,  # כָּבוֹד — glory/honor
    'H7965': 2,  # שָׁלוֹם — peace/wholeness/shalom
    'H6944': 2,  # קֹדֶשׁ — holiness/holy/sanctuary
    'H539':  2,  # אָמַן → אֱמוּנָה — faith/faithfulness/trust
    'H3045': 2,  # יָדַע — know (intimate knowledge vs. cognitive)
}

# Curated primary glosses for high-frequency entries where alphabetic Strong's
# ordering gives a misleading first token. Keyed by Strong's code.
# Thought-tier overrides are (literal, thought) tuples; None = same as literal.
KNOWN_PRIMARIES = {
    # Greek — top-frequency function words and contested terms
    'G846':  ('him',            'himself'),     # αὐτός — pronoun, not "her" first
    'G1722': ('in',             'in'),           # ἐν — not "about"
    'G1519': ('into',           'into'),         # εἰς — not "against"
    'G3756': ('not',            'not'),          # οὐ — not "nay"
    'G3361': ('not',            'not'),          # μή
    'G3004': ('say',            'say'),          # λέγω — not "ask"
    'G3956': ('all',            'every'),        # πᾶς
    'G3739': ('who',            'who'),          # ὅς — relative pronoun
    'G2532': ('and',            'and'),          # καί (already correct, confirm)
    'G2316': ('God',            'God'),          # θεός (already correct)
    'G3588': ('the',            'the'),          # ὁ — definite article
    'G1161': ('but',            'but'),          # δέ — adversative particle
    'G5207': ('son',            'son'),          # υἱός
    'G444':  ('man',            'human being'),  # ἄνθρωπος
    'G2962': ('Lord',           'Lord'),         # κύριος
    'G2424': ('Jesus',          'Jesus'),        # Ἰησοῦς
    'G5547': ('Christ',         'Christ'),       # Χριστός
    'G4151': ('spirit',         'Spirit'),       # πνεῦμα
    'G26':   ('love',           'unconditional love'),  # ἀγάπη
    'G3056': ('word',           'the Word'),     # λόγος
    'G4561': ('flesh',          'sinful nature'),# σάρξ
    'G166':  ('eternal',        'everlasting'),  # αἰώνιος
    'G1343': ('righteousness',  'justification'),# δικαιοσύνη
    'G1342': ('righteous',      'just'),         # δίκαιος
    'G4102': ('faith',          'faithfulness'), # πίστις
    'G3551': ('law',            'the Law'),      # νόμος
    'G5485': ('grace',          'favor'),        # χάρις
    'G1722': ('in',             'in'),           # ἐν
    'G2041': ('work',           'deed'),         # ἔργον
    'G40':   ('holy',           'set apart'),    # ἅγιος
    'G3340': ('repent',         'change one\'s mind'),  # μετανοέω
    'G907':  ('baptize',        'immerse'),      # βαπτίζω
    'G2222': ('life',           'life'),         # ζωή
    'G3962': ('father',         'Father'),       # πατήρ
    'G1680': ('hope',           'hope'),         # ἐλπίς
    'G26':   ('love',           'self-giving love'),    # ἀγάπη
    'G5368': ('love',           'love'),         # φιλέω

    # Hebrew — top-frequency and contested
    'H3068': ('LORD',           'Yahweh'),       # יהוה
    'H430':  ('God',            'God/gods'),     # אֱלֹהִים — not "angels"
    'H559':  ('say',            'say'),          # אָמַר — not "answer"
    'H1121': ('son',            'son'),          # בֵּן — not "age"
    'H6213': ('do',             'do'),           # עָשָׂה
    'H935':  ('come',           'come'),         # בּוֹא — not "abide"
    'H776':  ('earth',          'land'),         # אֶרֶץ — not "country"
    'H3117': ('day',            'day'),          # יוֹם — not "age"
    'H7307': ('spirit',         'Spirit/breath'),# רוּחַ
    'H2617': ('steadfast love', 'lovingkindness'),# חֶסֶד
    'H5315': ('soul',           'life/self'),    # נֶפֶשׁ
    'H1285': ('covenant',       'covenant'),     # בְּרִית
    'H6666': ('righteousness',  'justice'),      # צְדָקָה
    'H7965': ('peace',          'wholeness/shalom'), # שָׁלוֹם
    'H3519': ('glory',          'glory'),        # כָּבוֹד
    'H6944': ('holiness',       'holiness'),     # קֹדֶשׁ
    'H571':  ('truth',          'faithfulness'), # אֱמֶת
    'H2580': ('grace',          'favor'),        # חֵן
    'H4428': ('king',           'king'),         # מֶלֶךְ (already correct)
    'H3820': ('heart',          'heart/mind'),   # לֵב
    'H5971': ('people',         'people'),       # עַם
    'H3478': ('Israel',         'Israel'),       # already correct
    'H3068': ('LORD',           'Yahweh'),       # יהוה — already correct
    'H1121': ('son',            'son'),          # בֵּן
    'H5650': ('servant',        'servant'),      # עֶבֶד
    'H3027': ('hand',           'hand'),         # יָד
    'H6440': ('face',           'presence'),     # פָּנִים
    'H3045': ('know',           'know intimately'),  # יָדַע
    'H539':  ('believe',        'trust'),        # אָמַן
}

# POS inference from definition strings
_VERB_RE = re.compile(
    r'\bverb\b|to \w+|i\.e\. to |\(v\.\)|\bact\b', re.I
)
_CONJ_RE = re.compile(r'^(and|or|but|for|now|yet|so|then|therefore)\b', re.I)
_PREP_RE = re.compile(r'\bpreposition\b|denoting |among |between |through ', re.I)
_PRON_RE = re.compile(r'\bpronoun\b|reflexive|reciprocal', re.I)
_ADV_RE  = re.compile(r'\badverb\b|not |always |never |only |very ', re.I)
_ART_RE  = re.compile(r'\barticle\b', re.I)
_ADJ_RE  = re.compile(r'\badjective\b|\badj\b', re.I)

def _infer_pos(entry):
    gloss = entry.get('gloss', '')
    def_  = entry.get('def',   '')
    text  = gloss + ' ' + def_
    if _ART_RE.search(text):  return 'article'
    if _PRON_RE.search(text): return 'pronoun'
    if _CONJ_RE.match(gloss): return 'conjunction'
    if _PREP_RE.search(text): return 'preposition'
    if _ADV_RE.search(text):  return 'adverb'
    if _VERB_RE.search(text): return 'verb'
    if _ADJ_RE.search(text):  return 'adjective'
    return 'noun'

# Patterns that indicate a gloss token is a compound/idiomatic usage hint,
# not a standalone primary rendering.
_SKIP_GLOSS = re.compile(
    r'^X\s'           # "X exceeding" — compound multiplier usage
    r'|\+\s'          # "+ away" — directional compound
    r'|\[.*?\]'       # "[idiom]", "[phrase]"
    r'|^\('           # starts with parenthetical
    r'|\bself\b'      # reflexive forms like "(him-)self"
    r'|\(-'           # contains dash inside parens — inflected suffix notation
    r'|^\s*\d',       # starts with a number
    re.I
)

def _clean_token(tok):
    """Strip stray punctuation left by comma-splitting inside parentheticals."""
    tok = tok.strip(' \t\n.,;')
    # Remove unmatched trailing paren
    if tok.endswith(')') and '(' not in tok:
        tok = tok[:-1].strip()
    # Remove unmatched leading paren
    if tok.startswith('(') and ')' not in tok:
        tok = tok[1:].strip()
    return tok

def _pick_primary(gloss, def_=''):
    """Pick the best primary gloss from a Strong's comma-separated gloss field.
    Skips compound/inflected usage hints (X, +, brackets, parens) and returns
    the first remaining clean token — first is primary in Strong's ordering."""
    parts = [_clean_token(p) for p in gloss.split(',') if p.strip()]
    parts = [p for p in parts if p]

    clean = [p for p in parts if not _SKIP_GLOSS.search(p) and len(p) > 1]

    if clean:
        return clean[0]  # first clean token = primary meaning in Strong's ordering

    # All tokens compound-style — extract first clause from def
    if def_:
        clause = re.split(r'[;,]', def_)[0].strip()
        words  = clause.split()
        if words:
            return ' '.join(words[:4]).rstrip(',;')

    return re.sub(r'^X\s+', '', parts[0]).strip() if parts else ''

def _make_tiers(gloss, def_='', code=''):
    # Curated override wins over algorithmic pick
    if code and code in KNOWN_PRIMARIES:
        lit, tho = KNOWN_PRIMARIES[code]
        return {
            'literal':   {'primary': lit, 'notes': None},
            'mediating': {'primary': lit, 'notes': None},
            'thought':   {'primary': tho or lit, 'notes': None},
        }

    parts = [_clean_token(p) for p in gloss.split(',') if p.strip()]
    parts = [p for p in parts if p]
    clean = [p for p in parts if not _SKIP_GLOSS.search(p) and len(p) > 1]

    primary = clean[0] if clean else _pick_primary(gloss, def_)
    alt     = clean[1] if len(clean) > 1 else primary
    return {
        'literal':   {'primary': primary, 'notes': None},
        'mediating': {'primary': primary, 'notes': None},
        'thought':   {'primary': alt or primary, 'notes': None},
    }

def compute_freq(books, code_prefix):
    """Count Strong's code occurrences; returns (total_counter, {code: {book: count}})."""
    total  = Counter()
    by_book = {}  # {code: {book: count}}
    for book in books:
        fpath = os.path.join(INTERLINEAR, f'{book}.json')
        if not os.path.exists(fpath):
            continue
        try:
            with open(fpath, encoding='utf-8') as f:
                data = json.load(f)
            for _ch, verses in data.items():
                for _v, tokens in verses.items():
                    for tok in tokens:
                        code = tok.get('s', '')
                        if code and code.startswith(code_prefix):
                            total[code] += 1
                            if code not in by_book:
                                by_book[code] = {}
                            by_book[code][book] = by_book[code].get(book, 0) + 1
        except Exception as e:
            print(f'  Warning: {book}.json — {e}')
    return total, by_book

def load_existing(path):
    """Load an existing glossary file (for non-destructive re-run)."""
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}

def seed_greek(nt_freq, nt_book_freq, existing):
    with open(os.path.join(STRONGS, 'greek.json'), encoding='utf-8') as f:
        greek = json.load(f)
    try:
        with open(os.path.join(STRONGS, 'thayer.json'), encoding='utf-8') as f:
            thayer = json.load(f)
    except Exception:
        thayer = {}
    try:
        with open(os.path.join(STRONGS, 'abbott-smith.json'), encoding='utf-8') as f:
            abbott = json.load(f)
    except Exception:
        abbott = {}
    try:
        with open(os.path.join(STRONGS, 'attested-uses-greek.json'), encoding='utf-8') as f:
            attested_greek = json.load(f)
    except Exception:
        attested_greek = {}
    try:
        with open(os.path.join(STRONGS, 'moulton-milligan.json'), encoding='utf-8') as f:
            mm = json.load(f)
    except Exception:
        mm = {}

    glossary = {}
    for code, entry in greek.items():
        if not code.startswith('G'):
            continue
        # Don't overwrite entries that already have a user status
        if code in existing and existing[code].get('status') != 'draft':
            glossary[code] = existing[code]
            continue

        gloss   = entry.get('gloss', '')
        def_    = entry.get('def',   '')
        deriv   = entry.get('deriv', '')
        lemma   = entry.get('lemma', '')
        trans   = entry.get('translit', '')
        freq    = nt_freq.get(code, 0)
        bfreq   = nt_book_freq.get(code, {})

        th      = thayer.get(code, {})
        th_sh   = th.get('short_def', '')
        th_lg   = th.get('long_def',  '')
        if th_lg and len(th_lg) > 600:
            th_lg = th_lg[:600] + '…'

        ab      = abbott.get(code, {})

        disp = DISPUTED_GREEK.get(code, 0)
        if freq > 1000: disp = max(disp, 1)

        sources = ['dodson']
        if th_sh:  sources.append('thayer')
        if ab.get('gloss') or ab.get('def'): sources.append('abbott')

        glossary[code] = {
            'lemma':     lemma,
            'translit':  trans,
            'pos':       _infer_pos(entry),
            'domain':    [],
            'dispute_level': disp,
            'status':    'draft',
            'nt_freq':   freq,
            'book_freq': bfreq,
            'book_defaults': {},
            'tiers':     _make_tiers(gloss, def_, code),
            'context_overrides': [],
            'related_lemmas': [],
            'semantic_range': def_ or gloss,
            'expansion': '',
            'sources':   sources,
            'source_data': {
                'dodson': {'gloss': gloss, 'def': def_, 'deriv': deriv},
                'thayer': {'short': th_sh, 'long': th_lg},
                'abbott': {
                    'gloss':          ab.get('gloss', ''),
                    'def':            ab.get('def', ''),
                    'classical_note': ab.get('classical_note', ''),
                    'lxx_note':       ab.get('lxx_note', ''),
                },
            },
            'attested_uses': attested_greek.get(code, []),
            'extrabiblical_uses': [
                dict(ex, source='M&M')
                for ex in (mm.get(code) or {}).get('papyri_examples', [])[:2]
            ],
            'user_notes':   '',
            'decision_log': [],
        }
    return glossary

def seed_hebrew(ot_freq, ot_book_freq, existing):
    with open(os.path.join(STRONGS, 'hebrew.json'), encoding='utf-8') as f:
        hebrew = json.load(f)
    try:
        with open(os.path.join(STRONGS, 'bdb.json'), encoding='utf-8') as f:
            bdb = json.load(f)
    except Exception:
        bdb = {}
    try:
        with open(os.path.join(STRONGS, 'gesenius.json'), encoding='utf-8') as f:
            gesenius = json.load(f)
    except Exception:
        gesenius = {}
    try:
        with open(os.path.join(STRONGS, 'attested-uses-hebrew.json'), encoding='utf-8') as f:
            attested_hebrew = json.load(f)
    except Exception:
        attested_hebrew = {}
    try:
        with open(os.path.join(STRONGS, 'lxx-bridge.json'), encoding='utf-8') as f:
            lxx_bridge_data = json.load(f)
    except Exception:
        lxx_bridge_data = {}

    glossary = {}
    for code, entry in hebrew.items():
        if not code.startswith('H'):
            continue
        if code in existing and existing[code].get('status') != 'draft':
            glossary[code] = existing[code]
            continue

        gloss   = entry.get('gloss', '')
        def_    = entry.get('def',   '')
        deriv   = entry.get('deriv', '')
        lemma   = entry.get('lemma', '')
        trans   = entry.get('translit', '')
        freq    = ot_freq.get(code, 0)
        bfreq   = ot_book_freq.get(code, {})

        b       = bdb.get(code, {})
        b_sh    = b.get('short_def', '')
        b_lg    = b.get('long_def',  '')
        if b_lg and len(b_lg) > 600:
            b_lg = b_lg[:600] + '…'

        ge      = gesenius.get(code, {})

        disp = DISPUTED_HEBREW.get(code, 0)
        if freq > 1000: disp = max(disp, 1)

        sources = ['hebrew']
        if b_sh:  sources.append('bdb')
        if ge.get('gloss') or ge.get('def'): sources.append('gesenius')

        glossary[code] = {
            'lemma':     lemma,
            'translit':  trans,
            'pos':       _infer_pos(entry),
            'domain':    [],
            'dispute_level': disp,
            'status':    'draft',
            'ot_freq':   freq,
            'book_freq': bfreq,
            'book_defaults': {},
            'tiers':     _make_tiers(gloss, def_, code),
            'context_overrides': [],
            'related_lemmas': [],
            'semantic_range': def_ or gloss,
            'expansion': '',
            'sources':   sources,
            'source_data': {
                'hebrew': {'gloss': gloss, 'def': def_, 'deriv': deriv},
                'bdb':    {'short': b_sh, 'long': b_lg},
                'gesenius': {
                    'gloss':     ge.get('gloss', ''),
                    'def':       ge.get('def', ''),
                    'cognates':  ge.get('cognates', ''),
                    'root_note': ge.get('root_note', ''),
                },
            },
            'attested_uses': attested_hebrew.get(code, []),
            'lxx_bridge':   lxx_bridge_data.get(code, []),
            'user_notes':   '',
            'decision_log': [],
        }
    return glossary

def main():
    os.makedirs(OUT, exist_ok=True)

    print('1/4  Computing NT Greek frequencies from interlinear…')
    nt_freq, nt_book_freq = compute_freq(NT_BOOKS, 'G')
    print(f'     {sum(nt_freq.values()):,} token occurrences across {len(nt_freq)} distinct G codes')

    print('2/4  Computing OT Hebrew frequencies from interlinear…')
    ot_freq, ot_book_freq = compute_freq(OT_BOOKS, 'H')
    print(f'     {sum(ot_freq.values()):,} token occurrences across {len(ot_freq)} distinct H codes')

    greek_path = os.path.join(OUT, 'glossary-greek.json')
    print('3/4  Seeding Greek glossary…')
    existing_g = load_existing(greek_path)
    greek_gloss = seed_greek(nt_freq, nt_book_freq, existing_g)
    with open(greek_path, 'w', encoding='utf-8') as f:
        json.dump(greek_gloss, f, ensure_ascii=False, separators=(',', ':'))
    print(f'     {len(greek_gloss):,} entries → {greek_path}')

    hebrew_path = os.path.join(OUT, 'glossary-hebrew.json')
    print('4/4  Seeding Hebrew glossary…')
    existing_h = load_existing(hebrew_path)
    hebrew_gloss = seed_hebrew(ot_freq, ot_book_freq, existing_h)
    with open(hebrew_path, 'w', encoding='utf-8') as f:
        json.dump(hebrew_gloss, f, ensure_ascii=False, separators=(',', ':'))
    print(f'     {len(hebrew_gloss):,} entries → {hebrew_path}')

    # Empty phrase scaffolds
    for fname in ('glossary-phrases-greek.json', 'glossary-phrases-hebrew.json'):
        p = os.path.join(OUT, fname)
        if not os.path.exists(p):
            with open(p, 'w') as f:
                json.dump({}, f)
            print(f'     Created empty {fname}')

    # ── Phase bundles (workshop loads these instead of the full 11MB files) ──
    print('\nGenerating phase bundles…')

    def slim(entry, code):
        """Compact entry for phase bundles — drops verbose long_def strings."""
        sd      = entry.get('source_data', {})
        dodson  = sd.get('dodson', {})
        thayer  = sd.get('thayer', {})
        hebrew  = sd.get('hebrew', {})
        bdb     = sd.get('bdb', {})
        abbott  = sd.get('abbott', {})
        gesenius = sd.get('gesenius', {})
        return {
            'lemma':        entry.get('lemma', ''),
            'translit':     entry.get('translit', ''),
            'pos':          entry.get('pos', ''),
            'domain':       entry.get('domain', []),
            'dispute_level':entry.get('dispute_level', 0),
            'status':       entry.get('status', 'draft'),
            'nt_freq':      entry.get('nt_freq', 0),
            'ot_freq':      entry.get('ot_freq', 0),
            'book_freq':    entry.get('book_freq', {}),
            'book_defaults': entry.get('book_defaults', {}),
            'tiers':        entry.get('tiers', {}),
            'context_overrides': entry.get('context_overrides', []),
            'related_lemmas':    entry.get('related_lemmas', []),
            'semantic_range':    entry.get('semantic_range', ''),
            'expansion':    entry.get('expansion', ''),
            'sources':      entry.get('sources', []),
            # Include first source's gloss + short def; drop verbose long_def
            'source_data': {
                'dodson': {'gloss': dodson.get('gloss',''), 'def': dodson.get('def','')[:300], 'deriv': dodson.get('deriv','')},
                'thayer': {'short': thayer.get('short',''), 'long': thayer.get('long','')[:400]},
                'hebrew': {'gloss': hebrew.get('gloss',''), 'def': hebrew.get('def','')[:300], 'deriv': hebrew.get('deriv','')},
                'bdb':    {'short': bdb.get('short',''),   'long': bdb.get('long','')[:400]},
                'abbott': {
                    'gloss':          abbott.get('gloss', ''),
                    'def':            abbott.get('def', '')[:400],
                    'classical_note': abbott.get('classical_note', '')[:200],
                },
                'gesenius': {
                    'gloss':     gesenius.get('gloss', ''),
                    'def':       gesenius.get('def', '')[:400],
                    'cognates':  gesenius.get('cognates', '')[:200],
                    'root_note': gesenius.get('root_note', '')[:150],
                },
            },
            'attested_uses':      entry.get('attested_uses', [])[:6],
            'extrabiblical_uses': entry.get('extrabiblical_uses', [])[:2],
            'lxx_bridge':         entry.get('lxx_bridge', [])[:3],
            'user_notes':   entry.get('user_notes', ''),
            'decision_log': entry.get('decision_log', []),
        }

    def write_bundle(path, entries_dict):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(entries_dict, f, ensure_ascii=False, separators=(',', ':'))
        kb = os.path.getsize(path) // 1024
        print(f'     {len(entries_dict):4} entries  {kb:5} KB  → {os.path.basename(path)}')

    # Phase 1 — top 200 NT Greek
    p1_codes = sorted(greek_gloss.keys(), key=lambda c: -(greek_gloss[c].get('nt_freq') or 0))[:200]
    p1 = {c: slim(greek_gloss[c], c) for c in p1_codes}
    write_bundle(os.path.join(OUT, 'phase1.json'), p1)

    # Phase 2 — top 200 OT Hebrew
    p2_codes = sorted(hebrew_gloss.keys(), key=lambda c: -(hebrew_gloss[c].get('ot_freq') or 0))[:200]
    p2 = {c: slim(hebrew_gloss[c], c) for c in p2_codes}
    write_bundle(os.path.join(OUT, 'phase2.json'), p2)

    # Phase 5 — contested terms (dispute_level >= 3, both languages)
    p5g = {c: slim(e, c) for c, e in greek_gloss.items()  if e.get('dispute_level', 0) >= 3}
    p5h = {c: slim(e, c) for c, e in hebrew_gloss.items() if e.get('dispute_level', 0) >= 3}
    write_bundle(os.path.join(OUT, 'phase5.json'), {**p5g, **p5h})

    # Slim index — queue display only (no source_data at all), for "All" views
    def slim_idx(entry):
        # Includes tiers so the dossier Override form works in "All" views.
        # Omits source_data to keep the index small.
        return {
            'lemma':         entry.get('lemma', ''),
            'translit':      entry.get('translit', ''),
            'pos':           entry.get('pos', ''),
            'dispute_level': entry.get('dispute_level', 0),
            'nt_freq':       entry.get('nt_freq', 0),
            'ot_freq':       entry.get('ot_freq', 0),
            'book_freq':     entry.get('book_freq', {}),
            'book_defaults': entry.get('book_defaults', {}),
            'status':        entry.get('status', 'draft'),
            'tiers':         entry.get('tiers', {}),
            'semantic_range': (entry.get('semantic_range') or '')[:200],
            'user_notes':    entry.get('user_notes', ''),
            'decision_log':  entry.get('decision_log', []),
        }

    idx_g = {c: slim_idx(e) for c, e in greek_gloss.items()}
    write_bundle(os.path.join(OUT, 'index-greek.json'), idx_g)

    idx_h = {c: slim_idx(e) for c, e in hebrew_gloss.items()}
    write_bundle(os.path.join(OUT, 'index-hebrew.json'), idx_h)

    # Print top-10 by frequency for verification
    top_g = sorted(nt_freq.items(), key=lambda x: -x[1])[:10]
    print('\nTop NT Greek by frequency:')
    for code, n in top_g:
        e = greek_gloss.get(code, {})
        tiers = e.get('tiers', {})
        lit = tiers.get('literal', {}).get('primary', '')
        print(f'  {code:6}  {e.get("lemma",""):15}  {lit:20}  {n:,}×')

    top_h = sorted(ot_freq.items(), key=lambda x: -x[1])[:10]
    print('\nTop OT Hebrew by frequency:')
    for code, n in top_h:
        e = hebrew_gloss.get(code, {})
        tiers = e.get('tiers', {})
        lit = tiers.get('literal', {}).get('primary', '')
        print(f'  {code:6}  {e.get("lemma",""):15}  {lit:20}  {n:,}×')

    print('\nSeed complete.')

if __name__ == '__main__':
    main()
