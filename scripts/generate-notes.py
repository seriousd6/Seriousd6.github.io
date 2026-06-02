#!/usr/bin/env python3
"""
scripts/generate-notes.py — generate per-verse translation analysis notes.

For every verse in every book, produces:
  - token array: code, lemma, transliteration, POS, dispute level, all three tiers,
    semantic range excerpt
  - flags: high-dispute tokens with plain-English explanation of the debate
  - tier_divergences: tokens where Literal ≠ Thought (showing the range of choice)
  - structure_note: one-line description of the verse's grammatical character

Output: data/translation/notes/{book}.json
  Shape: {"1": {"1": {token, flags, tier_divergences, structure_note}}}

Run:
  python3 scripts/generate-notes.py              # all books
  python3 scripts/generate-notes.py --book john  # one book
  python3 scripts/generate-notes.py --testament nt
"""

import json
import os
import argparse
from pathlib import Path

ROOT      = Path(__file__).parent.parent
INTER_DIR = ROOT / 'data' / 'interlinear'
GLOSS_DIR = ROOT / 'data' / 'translation'
OUT_DIR   = ROOT / 'data' / 'translation' / 'notes'

NT_BOOKS = [
    'matthew','mark','luke','john','acts',
    'romans','1corinthians','2corinthians','galatians','ephesians',
    'philippians','colossians','1thessalonians','2thessalonians',
    '1timothy','2timothy','titus','philemon','hebrews',
    'james','1peter','2peter','1john','2john','3john','jude','revelation',
]
OT_BOOKS = [
    'genesis','exodus','leviticus','numbers','deuteronomy',
    'joshua','judges','ruth','1samuel','2samuel',
    '1kings','2kings','1chronicles','2chronicles',
    'ezra','nehemiah','esther','job','psalms','proverbs',
    'ecclesiastes','songofsolomon','isaiah','jeremiah','lamentations',
    'ezekiel','daniel','hosea','joel','amos','obadiah',
    'jonah','micah','nahum','habakkuk','zephaniah','haggai',
    'zechariah','malachi',
]
ALL_BOOKS = NT_BOOKS + OT_BOOKS

# ── Dispute explanations for known contested codes ────────────────────────────
DISPUTE_NOTES = {
    # Greek
    'G1342': 'δίκαιος — "righteous" (moral quality) vs. "just" (legal standing). Paul uses this in both senses, and which reading shapes entire doctrines of justification.',
    'G1343': 'δικαιοσύνη — "righteousness" (moral attribute) vs. "justification" (legal declaration). The Reformation turned on this word: is it a quality God gives or a status he declares?',
    'G4561': 'σάρξ — "flesh" (physical body, neutral) vs. "sinful nature" (Paul\'s ethical sense). Using one English word across both contexts either over- or under-interprets Paul.',
    'G166':  'αἰώνιος — "eternal" (timeless) vs. "age-long" (pertaining to the coming age). Some argue it describes quality of life in the Age to Come, not mere duration.',
    'G3056': 'λόγος — "word" (utterance) vs. "Word" (divine Person in John 1) vs. "Reason/Logic" (Greek philosophical sense). John\'s prologue deliberately evokes all three.',
    'G26':   'ἀγάπη — "love" vs. "charity" (KJV) vs. "self-giving love." Distinct from φιλία (warm affection) and ἔρως (desire). The MKT Thought tier expands to "self-giving love."',
    'G4151': 'πνεῦμα — "spirit" vs. "Spirit." Capitalization is a theological decision, not a grammatical fact. Greek has no capital letters.',
    'G3551': 'νόμος — "law" (general moral law) vs. "the Law" (Torah specifically) vs. "a law" (a principle). Context determines which, but translators must choose.',
    'G4102': 'πίστις — "faith" (subjective trust) vs. "faithfulness" (objective reliability). "Faith of Christ" (G1342 Χριστοῦ) may mean trust IN Christ or the faithfulness OF Christ.',
    'G5485': 'χάρις — "grace" (unmerited favor) vs. "favor" (patron\'s gift in social context). The patron-client background charges this word with economic and social concreteness.',
    'G2842': 'κοινωνία — "fellowship" (warm association) vs. "communion" (Eucharistic) vs. "sharing/partnership" (economic). All three are attested; context decides.',
    'G3340': 'μετανοέω — "repent" (religious) vs. "change one\'s mind" (literal: meta + noeō). The religious sense is genuine but the literal helps show it is cognitive, not merely emotional.',
    # Hebrew
    'H3068': 'יהוה — The divine name (YHWH). LORD (small caps) hides the personal name. Yahweh/Jehovah are reconstructions of the consonants. The MKT\'s choice shapes the reader\'s sense of intimacy with God.',
    'H430':  'אֱלֹהִים — Grammatically plural, normally takes singular verbs when referring to Israel\'s God. Translating as "God" (singular) interprets the plural; "gods" would be technically accurate but theologically wrong in monotheistic contexts.',
    'H7307': 'רוּחַ — "spirit" / "Spirit" / "wind" / "breath." Genesis 1:2 is famously ambiguous: "the Spirit of God," "a wind from God," or "the breath of God" are all grammatically valid.',
    'H2617': 'חֶסֶד — No English equivalent. Combines covenant loyalty, active kindness, and steadfast love. "Mercy" is too weak; "lovingkindness" is archaic; "steadfast love" misses the relational dimension.',
    'H5315': 'נֶפֶשׁ — "soul" (Greek-influenced: non-material self) vs. "life" (the whole living person) vs. "self" (the person as subject). Hebrew nefesh is embodied, not a separate immaterial substance.',
    'H1285': 'בְּרִית — "covenant." The full weight: a formal, oath-bound relationship with stipulations and consequences. English "covenant" is thinner than the Hebrew concept.',
    'H6666': 'צְדָקָה — "righteousness" (moral quality) vs. "justice" (social-legal action). OT prophets use this for God\'s vindicating action for the oppressed; "righteousness" alone misses the social dimension.',
    'H5769': 'עוֹלָם — "eternal" / "everlasting" / "age-long." Like Greek αἰώνιος, debate centers on whether this is absolute timelessness or the span of an era.',
}

# ── POS descriptions ──────────────────────────────────────────────────────────
POS_NOTES = {
    'verb':        'action or state word',
    'noun':        'person, place, thing, or concept',
    'adjective':   'descriptor of a noun',
    'adverb':      'modifier of a verb or adjective',
    'preposition': 'relational word showing position, direction, or cause',
    'conjunction': 'connecting word linking clauses',
    'pronoun':     'stands in for a noun already established',
    'article':     'marks definiteness ("the")',
    'particle':    'grammatical function word',
}

# ── Load glossary ──────────────────────────────────────────────────────────────

def load_glossary():
    out = {}
    for lang in ('greek', 'hebrew'):
        path = GLOSS_DIR / f'glossary-{lang}.json'
        if not path.exists():
            continue
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        out.update(data)
    return out

# ── Per-verse note generation ─────────────────────────────────────────────────

def verse_notes(tokens, glossary):
    """Generate structured notes for one verse."""
    tok_notes      = []
    flags          = []
    divergences    = []
    pos_types      = set()
    has_verb       = False
    has_high_disp  = False

    seen_codes = set()

    for tok in tokens:
        code = tok.get('s', '')
        text = tok.get('text', '')
        if not code:
            tok_notes.append({'text': text})
            continue

        entry = glossary.get(code, {})
        lemma    = entry.get('lemma', '')
        translit = entry.get('translit', '')
        pos      = entry.get('pos', '')
        disp     = entry.get('dispute_level', 0)
        tiers    = entry.get('tiers') or {}
        s_range  = (entry.get('semantic_range') or '')[:200]

        lit = (tiers.get('literal')   or {}).get('primary', '') or text
        med = (tiers.get('mediating') or {}).get('primary', '') or text
        tho = (tiers.get('thought')   or {}).get('primary', '') or text

        if pos:
            pos_types.add(pos)
        if pos == 'verb':
            has_verb = True
        if disp >= 2:
            has_high_disp = True

        tn = {
            'code':    code,
            'text':    text,
            'lemma':   lemma,
            'translit':translit,
            'pos':     pos,
            'disp':    disp,
            'lit':     lit,
            'med':     med,
            'tho':     tho,
            'range':   s_range,
        }
        tok_notes.append(tn)

        # Flag high-dispute words (once per code per verse)
        if disp >= 2 and code not in seen_codes:
            note = DISPUTE_NOTES.get(code, f'Dispute level {disp}: multiple significant translation options.')
            flags.append({
                'code':  code,
                'lemma': lemma,
                'disp':  disp,
                'note':  note,
            })

        # Record tier divergences
        if lit != tho and code not in seen_codes:
            divergences.append({
                'code':  code,
                'lemma': lemma,
                'lit':   lit,
                'tho':   tho,
            })

        seen_codes.add(code)

    # One-line structure note
    parts = []
    if has_verb:
        parts.append('contains a main verb')
    if 'preposition' in pos_types:
        parts.append('prepositional phrase(s)')
    if 'conjunction' in pos_types:
        parts.append('clause connector(s)')
    if has_high_disp:
        parts.append('⚑ theologically contested vocabulary')
    structure_note = '; '.join(parts) if parts else ''

    return {
        'tokens':       tok_notes,
        'flags':        flags,
        'divergences':  divergences,
        'structure':    structure_note,
    }

# ── Book processing ───────────────────────────────────────────────────────────

def process_book(book, glossary):
    inter_path = INTER_DIR / f'{book}.json'
    if not inter_path.exists():
        return None

    with open(inter_path, encoding='utf-8') as f:
        inter = json.load(f)

    out    = {}
    verses = 0
    flags  = 0

    for ch_str, ch_data in inter.items():
        out[ch_str] = {}
        for v_str, tokens in ch_data.items():
            notes = verse_notes(tokens, glossary)
            # Only store non-empty notes (saves space)
            slim = {
                'tokens': notes['tokens'],
            }
            if notes['flags']:
                slim['flags'] = notes['flags']
                flags += len(notes['flags'])
            if notes['divergences']:
                slim['div'] = notes['divergences']
            if notes['structure']:
                slim['struct'] = notes['structure']
            out[ch_str][v_str] = slim
            verses += 1

    return out, verses, flags

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--book',      default=None)
    parser.add_argument('--testament', default='all', choices=['all','nt','ot'])
    args = parser.parse_args()

    if args.book:
        books = [args.book.lower()]
    elif args.testament == 'nt':
        books = NT_BOOKS
    elif args.testament == 'ot':
        books = OT_BOOKS
    else:
        books = ALL_BOOKS

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print('Loading glossary…')
    glossary = load_glossary()
    print(f'  {len(glossary)} entries')
    print()

    total_v = 0
    total_f = 0

    for book in books:
        result = process_book(book, glossary)
        if result is None:
            print(f'  {book:20} — no interlinear data')
            continue

        book_data, verses, flagged = result
        out_path = OUT_DIR / f'{book}.json'
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(book_data, f, ensure_ascii=False, separators=(',', ':'))

        kb = out_path.stat().st_size // 1024
        total_v += verses
        total_f += flagged
        print(f'  {book:22} {verses:4}v  {flagged:4} flags  {kb:5} KB')

    print(f'\n  Total: {total_v} verses  {total_f} flagged terms')
    print(f'  Output: data/translation/notes/')

if __name__ == '__main__':
    main()
