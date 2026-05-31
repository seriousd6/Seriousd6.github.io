#!/usr/bin/env python3
"""generate-wordcloud.py
Builds data/wordcloud/frequencies.json — pre-computed Strong's lemma frequency data
for the word cloud page. Run once after interlinear data is fetched.

Gloss strategy: count the actual English translation text for every token in the
interlinear files, normalize off leading articles/prepositions/pronouns, then use
the most common result. This gives the word cloud labels that match what Bible
readers actually see in the text. A small GLOSS_OVERRIDES table handles edge cases
where the automatic approach needs editorial correction.

Output: top 250 theologically meaningful lemmas with per-testament and per-genre counts.
"""

import json, os, glob, collections, re

BASE     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTERDIR = os.path.join(BASE, 'data', 'interlinear')
OUTDIR   = os.path.join(BASE, 'data', 'wordcloud')
OUTFILE  = os.path.join(OUTDIR, 'frequencies.json')

# ── Genre assignments ──────────────────────────────────────────────────────────
GENRE_MAP = {
    'genesis':'law','exodus':'law','leviticus':'law','numbers':'law','deuteronomy':'law',
    'joshua':'history','judges':'history','ruth':'history',
    '1samuel':'history','2samuel':'history','1kings':'history','2kings':'history',
    '1chronicles':'history','2chronicles':'history',
    'ezra':'history','nehemiah':'history','esther':'history',
    'job':'poetry','psalms':'poetry','proverbs':'poetry',
    'ecclesiastes':'poetry','songofsolomon':'poetry',
    'isaiah':'prophecy','jeremiah':'prophecy','lamentations':'prophecy',
    'ezekiel':'prophecy','daniel':'prophecy',
    'hosea':'prophecy','joel':'prophecy','amos':'prophecy','obadiah':'prophecy',
    'jonah':'prophecy','micah':'prophecy','nahum':'prophecy','habakkuk':'prophecy',
    'zephaniah':'prophecy','haggai':'prophecy','zechariah':'prophecy','malachi':'prophecy',
    'matthew':'gospels','mark':'gospels','luke':'gospels','john':'gospels',
    'acts':'acts',
    'romans':'epistles','1corinthians':'epistles','2corinthians':'epistles',
    'galatians':'epistles','ephesians':'epistles','philippians':'epistles',
    'colossians':'epistles','1thessalonians':'epistles','2thessalonians':'epistles',
    '1timothy':'epistles','2timothy':'epistles','titus':'epistles','philemon':'epistles',
    'hebrews':'epistles','james':'epistles','1peter':'epistles','2peter':'epistles',
    '1john':'epistles','2john':'epistles','3john':'epistles','jude':'epistles',
    'revelation':'apocalyptic',
}

TESTAMENT_MAP = {
    'genesis':'OT','exodus':'OT','leviticus':'OT','numbers':'OT','deuteronomy':'OT',
    'joshua':'OT','judges':'OT','ruth':'OT','1samuel':'OT','2samuel':'OT',
    '1kings':'OT','2kings':'OT','1chronicles':'OT','2chronicles':'OT',
    'ezra':'OT','nehemiah':'OT','esther':'OT','job':'OT','psalms':'OT',
    'proverbs':'OT','ecclesiastes':'OT','songofsolomon':'OT',
    'isaiah':'OT','jeremiah':'OT','lamentations':'OT','ezekiel':'OT','daniel':'OT',
    'hosea':'OT','joel':'OT','amos':'OT','obadiah':'OT','jonah':'OT','micah':'OT',
    'nahum':'OT','habakkuk':'OT','zephaniah':'OT','haggai':'OT','zechariah':'OT','malachi':'OT',
    'matthew':'NT','mark':'NT','luke':'NT','john':'NT','acts':'NT',
    'romans':'NT','1corinthians':'NT','2corinthians':'NT','galatians':'NT','ephesians':'NT',
    'philippians':'NT','colossians':'NT','1thessalonians':'NT','2thessalonians':'NT',
    '1timothy':'NT','2timothy':'NT','titus':'NT','philemon':'NT','hebrews':'NT',
    'james':'NT','1peter':'NT','2peter':'NT','1john':'NT','2john':'NT','3john':'NT',
    'jude':'NT','revelation':'NT',
}

# ── Stop lists — function words that obscure theological content ───────────────
GREEK_STOP = {
    'G3588',  # ὁ/ἡ/τό — the (article)
    'G2532',  # καί — and/also
    'G1161',  # δέ — but/and/now
    'G846',   # αὐτός — him/her/it/they/same
    'G1519',  # εἰς — into/to/for
    'G1722',  # ἐν — in/among/by
    'G1537',  # ἐκ/ἐξ — out of/from
    'G575',   # ἀπό — from/away from
    'G3326',  # μετά — with/after
    'G2596',  # κατά — according to/down
    'G4314',  # πρός — to/toward/with
    'G1223',  # διά — through/because of
    'G1909',  # ἐπί — on/upon/at
    'G5259',  # ὑπό — under/by
    'G3844',  # παρά — beside/from/against
    'G4862',  # σύν — with/together
    'G4253',  # πρό — before/in front of
    'G1799',  # ἐνώπιον — before/in the presence of
    'G3739',  # ὅς/ἥ/ὅ — who/which/that (relative)
    'G5100',  # τις — someone/something/certain
    'G3956',  # πᾶς — all/every/whole
    'G3778',  # οὗτος — this/these
    'G1565',  # ἐκεῖνος — that/those (distal)
    'G1438',  # ἑαυτοῦ — himself/itself/themselves
    'G3745',  # ὅσος — as much as/as many as
    'G3748',  # ὅστις — whoever/whatever
    'G3761',  # οὐδέ — neither/nor/not even
    'G3762',  # οὐδείς — no one/nothing/none
    'G3361',  # μή — not (with subj/inf)
    'G3756',  # οὐ/οὐκ/οὐχ — not
    'G1487',  # εἰ — if/whether
    'G2443',  # ἵνα — that/in order that/so that
    'G3753',  # ὅτε — when/while
    'G3767',  # οὖν — therefore/then/so
    'G1063',  # γάρ — for/because/so
    'G3779',  # οὕτω/οὕτως — thus/in this way
    'G302',   # ἄν — (conditional particle)
    'G3699',  # ὅπου — where
    'G3704',  # ὅπως — how/that/in order that
    'G3752',  # ὅταν — whenever/when
    'G2228',  # ἤ — or/than
    'G235',   # ἀλλά — but/except/yet
    'G3303',  # μέν — indeed/on the one hand
    'G5613',  # ὡς — as/like/when/because
    'G3754',  # ὅτι — that/because/how (conjunction)
    'G4459',  # πῶς — how
    'G3763',  # οὐδέποτε — never
    'G3364',  # οὐ μή — certainly not (negative particle)
    'G3004',  # λέγω — say/speak (too generic to be useful in a word cloud)
    # Pronouns — personal, demonstrative, interrogative
    'G848',   # αὑτοῦ — of himself
    'G5213',  # ὑμῖν — to you (dative plural)
    'G3450',  # μου — of me
    'G5216',  # ὑμῶν — of you (genitive plural)
    'G1473',  # ἐγώ — I
    'G4771',  # σύ — you
    'G1700',  # ἐμοῦ — of me
    'G3165',  # με — me (accusative)
    'G5101',  # τίς — who?/what? (interrogative)
    'G4675',  # σου — of you (genitive singular)
    'G5209',  # ὑμᾶς — you (accusative plural)
    'G2257',  # ἡμῶν — of us
    'G2254',  # ἡμῖν — to us
    'G3427',  # μοι — to me
    'G4012',  # περί — about/concerning
    'G5124',  # τοῦτο — this/that (neut. demonstrative)
    'G5023',  # ταῦτα — these things (demonstrative plural)
    'G5210',  # ὑμεῖς — you (nominative plural pronoun)
    'G4671',  # σοί — to thee (dative singular pronoun)
    'G4571',  # σέ — thee (accusative singular pronoun)
    'G1437',  # ἐάν — if (conditional particle)
    'G2071',  # ἔσομαι — will be (future copula)
    'G2076',  # ἐστί(ν) — is/are (copula)
    'G2258',  # ἦν — was (copula)
    'G1510',  # εἰμί — be/am/is (copula)
    # Additional function words revealed by NT supplement analysis
    'G5228',  # ὑπέρ — over/above/for (preposition)
    'G3363',  # ἵνα μή — lest/not (negative purpose particle)
    'G3568',  # νῦν — now (temporal particle)
    'G2249',  # ἡμεῖς — we (nominative plural pronoun)
    'G1511',  # εἶναι — to be (copula infinitive)
    'G243',   # ἄλλος — another/other (not distinct enough for word cloud)
    'G1410',  # δύναμαι — can/be able (auxiliary; G1411 δύναμις "power" kept)
    # Additional NT function words found in supplement pass
    'G2531',  # καθώς — as/just as (comparative conjunction)
    'G5037',  # τέ — and/both (enclitic conjunction)
    'G2248',  # ἡμᾶς — us (accusative plural pronoun)
    'G1526',  # εἰσί — are (third-person plural copula)
    'G5119',  # τότε — then/at that time (temporal particle)
    'G5607',  # ὤν — being (present participle of εἰμί, copula)
    'G2193',  # ἕως — until/as far as (preposition/conjunction)
    'G3825',  # πάλιν — again (adverb; too generic for word cloud)
    'G5026',  # ταύτῃ — this (dative fem. form of demonstrative οὗτος)
    'G2089',  # ἔτι — yet/still (temporal particle)
    'G3650',  # ὅλος — all/whole/entire (too generic)
    'G3195',  # μέλλω — be about to/shall (auxiliary modal)
    'G1163',  # δεῖ — it is necessary/must (impersonal necessity verb)
    'G2087',  # ἕτερος — another/other (of different kind; too generic alongside G243)
    'G2398',  # ἴδιος — own/private (adjective; too generic)
    'G1563',  # ἐκεῖ — there (spatial adverb)
    'G3777',  # οὔτε — neither/nor (copulative negative conjunction)
    # Scribal/lexical variants already counted elsewhere
    'H3069',  # {YHWH} — scribal variant of H3068
    'G2401',  # Ἰδουμαία — skip
    'G3666',  # ὁμοιόω — make like (too abstract)
    'G3760',  # οὐδαμῶς — by no means
}

# Hebrew function words
HEBREW_STOP = {
    'H853',   # את — direct object marker
    'H834',   # אשׁר — who/which/that (relative)
    'H3588',  # כי — that/because/when/for
    'H4480',  # מן — from/out of
    'H413',   # אל — to/toward/into
    'H5921',  # על — upon/over/about
    'H5704',  # עד — until/as far as
    'H3651',  # כן — so/thus
    'H518',   # אם — if/whether
    'H1571',  # גם — also/even
    'H428',   # אלה — these
    'H2088',  # זה — this (masc)
    'H2063',  # זאת — this (fem)
    'H1992',  # הם/המה — they/them (masc)
    'H2004',  # הן/הנה — they/them (fem)
    'H3602',  # כה — thus/so
    'H3863',  # לו — if only
    'H3809',  # לא — not (Aramaic)
    'H4310',  # מי — who?
    'H4100',  # מה — what?/why?
    'H3808',  # לא — no/not
    'H369',   # אין — there is not
    'H3605',  # כל — all/every/whole
    'H5750',  # עד — still/yet/again
    'H7535',  # רק — only/but/except
    'H389',   # אך — only/surely/but
    'H645',   # אפו — now/then
    'H227',   # אז — then/at that time
}

# ── Normalization — strip leading function words to get core translation ───────
# Applied iteratively until stable; gives the most common "bare" English gloss.
_LEAD_RE = re.compile(
    r'^(the|a|an|'
    r'of|in|by|for|with|from|to|into|on|upon|at|through|as|and|or|'
    r'his|her|their|our|my|your|its|this|that|these|those|'
    r'he|she|they|we|thou|ye|you|thee|me|him|us|them|it|i|'
    r'unto|o|oh|'
    r'am|is|are|was|were|will|shall|have|has|had|do|does|did|be|been|being|'
    r'not|no|now|then|also|even|yet|but|so|'
    r'which|who|whose|whom)\s+',
    re.IGNORECASE
)

def normalize_translation(text):
    """Strip leading function words iteratively; cap at 3 words; capitalize."""
    t = text.strip().lower()
    prev = None
    while prev != t:
        prev = t
        t = _LEAD_RE.sub('', t)
    t = t.strip(' ,-;:.')
    parts = t.split()
    if len(parts) > 3:
        t = ' '.join(parts[:3])
    return t[0].upper() + t[1:] if t else ''


# ── Small override table — only for cases where auto-extraction fails ──────────
# These are editorial choices: theological precision, disambiguation, or
# cases where the interlinear text format distorts the most-common-form logic.
GLOSS_OVERRIDES = {
    # Divine name — distinguish from Adonai (H136) and Greek kyrios (G2962)
    'H3068': 'LORD (Yahweh)',
    # Adonai — distinguish from Yahweh and Greek kyrios
    'H136':  'Lord (Adonai)',
    # Prophetic declaration formula — "saith" (auto) is archaic; "Declares" is clearer
    'H5002': 'Declares the LORD',
    # H1696 (dabar as verb) and H1697 (dabar as noun) — disambiguate
    'H1696': 'Speak',
    'H1697': 'Word',
    # NT supplement overrides — auto-extraction gives the most common KJV surface form,
    # but the theological term is more recognizable/important in these cases:
    'G863':  'Forgive',    # ἀφίημι; auto gives "Left" because "leave" outnumbers "forgive"
    'G281':  'Amen',       # ἀμήν; auto gives "Verily" (KJV "verily I say"), but "Amen" is universal
    'G3793': 'Crowd',      # ὄχλος; auto gives "People" — disambiguate from G2992 λαός (People)
    'G1453': 'Risen',      # ἐγείρω; auto gives "Raised" — "Risen" is the more familiar theological term
    'G2198': 'Live',       # ζάω — auto gives "Live"; keep as-is (just confirming)
    'G2222': 'Life',       # ζωή — key NT term; auto gives "Life" correctly
    'G5485': 'Grace',      # χάρις — key NT term; auto gives "Grace" correctly
    'G932':  'Kingdom',    # βασιλεία — key NT term; auto gives "Kingdom" correctly
    # More NT supplement refinements
    'G165':  'Eternal',    # αἰών; auto gives "Ever" (from "for ever") — "Eternal" is clearer
    'G3870': 'Exhort',     # παρακαλέω; auto gives archaic "Besought" — "Exhort" is the primary NT sense
    'G1849': 'Authority',  # ἐξουσία; auto gives "Power" — disambiguate from G1411 δύναμις (miraculous power)
}


def normalize_id(book_file):
    return os.path.splitext(os.path.basename(book_file))[0].lower()

def load_strongs():
    heb = json.load(open(os.path.join(BASE, 'data', 'strongs', 'hebrew.json'), encoding='utf-8'))
    grk = json.load(open(os.path.join(BASE, 'data', 'strongs', 'greek.json'), encoding='utf-8'))
    merged = {}
    merged.update(heb)
    merged.update(grk)
    return merged

def best_translation(strongs_id, trans_counts):
    """Return the most common normalized English translation for a Strong's ID."""
    raw = trans_counts.get(strongs_id)
    if not raw:
        return ''
    normed = collections.Counter()
    for text, cnt in raw.items():
        n = normalize_translation(text)
        if n:
            normed[n] += cnt
    if not normed:
        return ''
    return normed.most_common(1)[0][0]

def first_gloss(strongs_id, entry, trans_counts):
    """Return a clean primary English gloss. Priority: override > actual translations > Strong's dict."""
    if strongs_id in GLOSS_OVERRIDES:
        return GLOSS_OVERRIDES[strongs_id]

    bt = best_translation(strongs_id, trans_counts)
    if bt and len(bt) >= 2:
        return bt

    # Fallback: Strong's dictionary def field
    def_str = entry.get('def', '')
    if def_str:
        d = def_str.strip()
        d = re.sub(r'^(properly,?\s*|primarily\s*|literally\s*|i\.e\.\s*)', '', d, flags=re.I)
        d = re.sub(r'\(.*?\)', '', d)
        d = re.split(r'[;:,]', d)[0].strip()
        d = re.split(r'\bi\.e\b|\bhence\b|\bthat is\b', d)[0].strip()
        d = d.strip(' .-')
        d = re.sub(r'^(a |an |the )', '', d, flags=re.I).strip()
        if len(d) > 30:
            d = d[:30].rsplit(' ', 1)[0]
        if d:
            return d[0].upper() + d[1:]

    # Last resort: first item from gloss field
    gloss_str = entry.get('gloss', '')
    if not gloss_str:
        return strongs_id
    g = gloss_str.strip().rstrip('.')
    g = re.sub(r'^(\[.*?\]|[+X]\s*)+', '', g).strip()
    parts = re.split(r'[,;]', g)
    result = parts[0].strip()
    result = re.sub(r'\[.*?\]|\(.*?\)', '', result).strip(' -+X')
    if result:
        result = result[0].upper() + result[1:]
    return result or strongs_id


def main():
    print("Loading Strong's lexicons...")
    strongs = load_strongs()

    # Frequency counters
    global_counts = collections.Counter()
    ot_counts     = collections.Counter()
    nt_counts     = collections.Counter()
    genre_counts  = {g: collections.Counter() for g in
                     ['law','history','poetry','prophecy','gospels','acts','epistles','apocalyptic']}

    # Translation text collector: strongs_id -> Counter({raw_text: count})
    trans_counts = collections.defaultdict(collections.Counter)

    files = sorted(glob.glob(os.path.join(INTERDIR, '*.json')))
    print(f"Processing {len(files)} interlinear files...")

    for f in files:
        book_id  = normalize_id(f)
        testament = TESTAMENT_MAP.get(book_id, 'OT')
        genre     = GENRE_MAP.get(book_id, 'history')

        try:
            data = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print(f"  SKIP {book_id}: {e}")
            continue

        for ch in data.values():
            for v in ch.values():
                for word in v:
                    s = word.get('s', '')
                    if not s:
                        continue
                    global_counts[s] += 1
                    if testament == 'OT':
                        ot_counts[s] += 1
                    else:
                        nt_counts[s] += 1
                    gc = genre_counts.get(genre)
                    if gc is not None:
                        gc[s] += 1
                    # Collect translation text for gloss computation
                    t = word.get('text', '').strip()
                    if t:
                        trans_counts[s][t.lower()] += 1

    print(f"Total unique lemmas: {len(global_counts)}")
    print(f"Total word tokens:   {sum(global_counts.values())}")

    stop_all = GREEK_STOP | HEBREW_STOP
    filtered = {k: v for k, v in global_counts.items() if k not in stop_all}
    top = sorted(filtered.items(), key=lambda x: x[1], reverse=True)[:250]

    words = []
    for strongs_id, count in top:
        entry = strongs.get(strongs_id, {})
        gloss = first_gloss(strongs_id, entry, trans_counts)

        if not gloss:
            gloss = entry.get('def', '')[:40] or strongs_id

        lang = 'H' if strongs_id.startswith('H') else 'G'
        words.append({
            'id':       strongs_id,
            'lang':     lang,
            'lemma':    entry.get('lemma', ''),
            'translit': entry.get('translit', ''),
            'gloss':    gloss,
            'count':    count,
            'ot':       ot_counts.get(strongs_id, 0),
            'nt':       nt_counts.get(strongs_id, 0),
            'genres': {
                'law':        genre_counts['law'].get(strongs_id, 0),
                'history':    genre_counts['history'].get(strongs_id, 0),
                'poetry':     genre_counts['poetry'].get(strongs_id, 0),
                'prophecy':   genre_counts['prophecy'].get(strongs_id, 0),
                'gospels':    genre_counts['gospels'].get(strongs_id, 0),
                'acts':       genre_counts['acts'].get(strongs_id, 0),
                'epistles':   genre_counts['epistles'].get(strongs_id, 0),
                'apocalyptic':genre_counts['apocalyptic'].get(strongs_id, 0),
            }
        })

    # ── NT-specific supplement ─────────────────────────────────────────────
    # The global top-250 is dominated by OT Hebrew (OT is ~77% of Bible text).
    # For the NT cross shape to have enough words, we append the top NT lemmas
    # by NT count that didn't make the global cut.  We cap at 80 extras so the
    # JSON stays manageable; the JS scope filter then picks the best 150 to render.
    global_ids_set = {w['id'] for w in words}
    nt_sorted = sorted(
        [(sid, nt_counts[sid]) for sid in nt_counts
         if sid not in global_ids_set and sid not in stop_all],
        key=lambda x: x[1], reverse=True
    )
    nt_added = 0
    for strongs_id, _nt_cnt in nt_sorted:
        if nt_added >= 80:
            break
        entry = strongs.get(strongs_id, {})
        if not entry:
            continue  # unknown ID — skip
        gloss = first_gloss(strongs_id, entry, trans_counts)
        if not gloss or gloss == strongs_id:
            continue  # couldn't resolve a human-readable gloss — skip
        lang = 'H' if strongs_id.startswith('H') else 'G'
        words.append({
            'id':       strongs_id,
            'lang':     lang,
            'lemma':    entry.get('lemma', ''),
            'translit': entry.get('translit', ''),
            'gloss':    gloss,
            'count':    global_counts.get(strongs_id, 0),
            'ot':       ot_counts.get(strongs_id, 0),
            'nt':       nt_counts.get(strongs_id, 0),
            'genres': {g: genre_counts[g].get(strongs_id, 0) for g in genre_counts},
        })
        nt_added += 1
    print(f"NT supplement: added {nt_added} words")

    os.makedirs(OUTDIR, exist_ok=True)
    with open(OUTFILE, 'w', encoding='utf-8') as f:
        json.dump({'words': words}, f, ensure_ascii=False, separators=(',', ':'))

    print(f"\nWritten {len(words)} words to {OUTFILE}")
    print("\nTop 30:")
    for w in words[:30]:
        print(f"  {w['id']:8s} {w['count']:6d}  {w['gloss']}")


if __name__ == '__main__':
    main()
