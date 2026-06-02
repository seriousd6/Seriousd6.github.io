#!/usr/bin/env python3
"""
scripts/translate-with-claude.py — Translate the Bible using Claude AI.

Produces all three MKT tiers (Literal / Mediating / Thought) with per-verse
reasoning notes by calling the Claude API with rich linguistic context:
  - Full interlinear token data (lemma, code, gloss)
  - Glossary entries for every token, especially high-dispute words
  - Surrounding verse context
  - Cultural and grammatical context from the translation primers
  - Confirmed workshop decisions

Requires:
  1. python3 -m pip install anthropic
  2. export ANTHROPIC_API_KEY=sk-ant-...

Usage:
  python3 scripts/translate-with-claude.py --book john
  python3 scripts/translate-with-claude.py --book john --chapter 1
  python3 scripts/translate-with-claude.py --testament nt
  python3 scripts/translate-with-claude.py --all

Output:
  data/translation/draft/literal/{book}.json
  data/translation/draft/mediating/{book}.json
  data/translation/draft/thought/{book}.json
  data/translation/notes/{book}.json         (reasoning, replaces auto-generated)

The script is safe to resume — already-translated chapters are skipped unless
you pass --overwrite.
"""

import json
import os
import re
import time
import argparse
from pathlib import Path

try:
    import anthropic
except ImportError:
    print('ERROR: anthropic package not installed.')
    print('Run: python3 -m pip install anthropic')
    raise SystemExit(1)

ROOT      = Path(__file__).parent.parent
INTER_DIR = ROOT / 'data' / 'interlinear'
GLOSS_DIR = ROOT / 'data' / 'translation'
DRAFT_DIR = ROOT / 'data' / 'translation' / 'draft'
NOTES_DIR = ROOT / 'data' / 'translation' / 'notes'

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

# Book name lookup (for prompts)
BOOK_NAMES = {
    'genesis':'Genesis','exodus':'Exodus','leviticus':'Leviticus',
    'numbers':'Numbers','deuteronomy':'Deuteronomy','joshua':'Joshua',
    'judges':'Judges','ruth':'Ruth','1samuel':'1 Samuel','2samuel':'2 Samuel',
    '1kings':'1 Kings','2kings':'2 Kings','1chronicles':'1 Chronicles',
    '2chronicles':'2 Chronicles','ezra':'Ezra','nehemiah':'Nehemiah',
    'esther':'Esther','job':'Job','psalms':'Psalms','proverbs':'Proverbs',
    'ecclesiastes':'Ecclesiastes','songofsolomon':'Song of Solomon',
    'isaiah':'Isaiah','jeremiah':'Jeremiah','lamentations':'Lamentations',
    'ezekiel':'Ezekiel','daniel':'Daniel','hosea':'Hosea','joel':'Joel',
    'amos':'Amos','obadiah':'Obadiah','jonah':'Jonah','micah':'Micah',
    'nahum':'Nahum','habakkuk':'Habakkuk','zephaniah':'Zephaniah',
    'haggai':'Haggai','zechariah':'Zechariah','malachi':'Malachi',
    'matthew':'Matthew','mark':'Mark','luke':'Luke','john':'John',
    'acts':'Acts','romans':'Romans','1corinthians':'1 Corinthians',
    '2corinthians':'2 Corinthians','galatians':'Galatians','ephesians':'Ephesians',
    'philippians':'Philippians','colossians':'Colossians',
    '1thessalonians':'1 Thessalonians','2thessalonians':'2 Thessalonians',
    '1timothy':'1 Timothy','2timothy':'2 Timothy','titus':'Titus',
    'philemon':'Philemon','hebrews':'Hebrews','james':'James','1peter':'1 Peter',
    '2peter':'2 Peter','1john':'1 John','2john':'2 John','3john':'3 John',
    'jude':'Jude','revelation':'Revelation',
}

# ── Dispute explanations (same as generate-notes.py, condensed) ───────────────
DISPUTE_NOTES = {
    'G1342':'δίκαιος — righteous/just. Both moral quality and legal standing are attested.',
    'G1343':'δικαιοσύνη — righteousness/justification. Whether it is a quality given or a status declared shaped the Reformation.',
    'G4561':'σάρξ — flesh/sinful nature. Physical body in John 1:14; fallen human drive in Romans 7–8. Do not collapse these.',
    'G166': 'αἰώνιος — eternal/age-long. The word may denote quality of life in the coming Age rather than mere infinite duration.',
    'G3056':'λόγος — Word/word/Reason. John 1 intentionally evokes Greek philosophical Logos, OT Wisdom, and Hebrew dabar simultaneously.',
    'G26':  'ἀγάπη — love. Distinct from φιλία (warm affection) and ἔρως (desire). Willed, covenantal, self-giving.',
    'G4151':'πνεῦμα — spirit/Spirit/wind/breath. Capitalisation is a theological decision; Greek has no capitals.',
    'G3551':'νόμος — law/the Law. Distinguish Torah specifically from general moral principle.',
    'G4102':'πίστις — faith/faithfulness. "Faith of Christ" may be Christ\'s own faithfulness, not merely trust in him.',
    'G5485':'χάρις — grace. The patron\'s unearned gift creating loyal response — economic and social, not merely spiritual.',
    'G2842':'κοινωνία — fellowship/communion/sharing/partnership. All four senses are attested.',
    'G3340':'μετανοέω — repent/change one\'s mind. Cognitive reorientation, not mere emotional regret.',
    'H3068':'יהוה — LORD/Yahweh. The divine name; capitalised LORD hides the personal name.',
    'H430': 'אֱלֹהִים — God/gods. Grammatically plural; context determines singular or plural sense.',
    'H7307':'רוּחַ — spirit/Spirit/wind/breath. All three attested in Gen 1:2; the ambiguity may be intentional.',
    'H2617':'חֶסֶד — no English equivalent. Covenant loyalty + active kindness + steadfast love combined.',
    'H5315':'נֶפֶשׁ — soul/life/self. Hebrew nefesh is embodied — not a Greek immaterial soul.',
    'H1285':'בְּרִית — covenant. A formal, oath-bound, legally structured relationship.',
    'H6666':'צְדָקָה — righteousness/justice. Prophetic usage emphasises vindicating the oppressed, not merely moral purity.',
    'H5769':'עוֹלָם — eternal/everlasting/age-long. See αἰώνιος note.',
}

# ── System prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are the translator producing the Modern Kingdom Translation (MKT) — an original, copyright-free English translation directly from the Biblical Hebrew (Westminster Leningrad Codex / BHS) and Greek (SBLGNT / Nestle-Aland 28).

## Three Tiers

Every verse receives THREE distinct renderings:

**MKT-L (Literal):** Word-for-word. Preserve source syntax as far as English allows. One English word per lemma wherever possible. Nothing added, softened, or explained. Retain Greek/Hebrew word order where English can tolerate it. Show the structure even if it is wooden.

**MKT-M (Mediating):** Natural English sentence flow. Accurate primary glossary renderings. Idiomatic connectives only where English requires them. The default reading tier — accurate without being wooden.

**MKT-T (Thought):** Meaning-driven. Use alternate glossary renderings where they communicate the full sense more clearly to a modern reader. Render idioms as their meaning, not their form. Render poetry with contemporary cadence. The theology never changes — only how plainly the meaning is expressed.

## Translation Principles

1. **Aspect first for Greek verbs.** Aorist = single complete act (snapshot). Present = ongoing/repeated (video). Perfect = past act with lasting present result ("it stands written"). The tier renderings must reflect this.

2. **Hebrew aspect over tense.** Perfect = complete; Imperfect = ongoing/potential. Waw-consecutive turns imperfect to narrative past. Do not smooth this into simple English tense without noting it.

3. **Polysemy is normal.** Do not force one English word across all occurrences of σάρξ, πνεῦμα, νόμος, etc. Let the tier and context determine the rendering. Flag where you depart from the primary gloss.

4. **The divine passive.** Passive verbs in Jewish texts often imply God as the unnamed agent. Note this in reasoning.

5. **Honour-shame culture.** Social dynamics (patron-client, shaming, public vindication) often lie behind vocabulary choices. Note when this shapes meaning.

6. **Intertextuality.** Note deliberate OT echoes and LXX allusions — they carry theological weight the reader needs.

7. **Do not flatten poetry.** Hebrew parallelism is meaningful, not merely decorative. Preserve line structure in Psalms, Proverbs, and prophetic poetry.

8. **Articles and definiteness.** Greek anarthrous nouns are not automatically indefinite. Colwell's rule, qualitative use, and Granville Sharp rule apply. Reason explicitly about article decisions.

## Output Format

Return valid JSON only — no prose outside the JSON. Use this exact structure:

{
  "CHAPTER_NUMBER": {
    "VERSE_NUMBER": {
      "lit": "literal rendering",
      "med": "mediating rendering",
      "tho": "thought rendering",
      "notes": {
        "structure": "one sentence: grammatical character of this verse",
        "decisions": [
          "decision or observation 1",
          "decision or observation 2"
        ],
        "key_terms": [
          {"code": "G26", "word": "ἀγάπη", "note": "brief translation reasoning"}
        ]
      }
    }
  }
}

Be complete — include every verse in the chapter. Keep notes concise but substantive. A "decision" is a specific linguistic, theological, or cultural choice that a reader studying the text would want to know about. Minimum 1 decision per verse; more for dense passages."""

# ── Build chapter prompt ───────────────────────────────────────────────────────

def _chapter_context(book, ch_num):
    """Brief contextual description for the prompt."""
    CONTEXTS = {
        ('john', 1): 'The Prologue. John 1:1–18 introduces the Logos Christology, drawing on Genesis 1 and OT Wisdom/Word theology while engaging Greek philosophical Logos. Every clause is theologically dense.',
        ('john', 3): 'Jesus\'s night conversation with Nicodemus. Key passage on new birth, the Spirit, and John 3:16. Nicodemus misreads spiritual language as physical (born again / born from above).',
        ('romans', 1): 'Paul\'s thesis statement (1:16–17) and his case that all humanity stands under God\'s righteous judgment. 1:17 quotes Habakkuk 2:4 — central to the Reformation.',
        ('romans', 3): 'The universal indictment (3:1–20) and the first full statement of justification by faith (3:21–31). Contains the densest concentration of δικαιοσύνη / δίκαιος vocabulary in Paul.',
        ('genesis', 1): 'The creation account. Hebrew perfect and imperfect aspect are critical. The passage is a polemic against ANE creation myths: God acts by speech alone, creation is orderly, humanity uniquely bears the divine image.',
        ('isaiah', 53): 'The Servant Song. The chapter NT authors cite most often. Grammatical ambiguity about identity of servant is intentional. Perfect-tense verbs describe future events as complete (prophetic perfect).',
        ('psalms', 22): 'The psalm of desolation, cited by Jesus from the cross. Moves from abandonment cry to confidence to universal praise. Note the shift in aspect and mood at v.24.',
        ('hebrews', 1): 'The exordium: the Son as final and superior revelation. Dense use of the Greek perfect tense (καθίσεν, κεκληρονόμηκεν, etc.) — past events with lasting present results.',
    }
    return CONTEXTS.get((book, ch_num), f'{BOOK_NAMES.get(book, book)} chapter {ch_num}.')

def build_chapter_prompt(book, ch_num, ch_data, glossary):
    """Build the user message for one chapter."""
    lang = 'hebrew' if book in OT_BOOKS else 'greek'
    book_name = BOOK_NAMES.get(book, book)
    ctx = _chapter_context(book, ch_num)

    lines = [f'Translate {book_name} Chapter {ch_num}.\n']
    lines.append(f'CONTEXT: {ctx}\n')

    # Gather all codes in this chapter
    all_codes = {}
    for v_str, tokens in ch_data.items():
        for tok in tokens:
            code = tok.get('s', '')
            if code and code not in all_codes:
                entry = glossary.get(code, {})
                all_codes[code] = {
                    'lemma':    entry.get('lemma', ''),
                    'translit': entry.get('translit', ''),
                    'pos':      entry.get('pos', ''),
                    'disp':     entry.get('dispute_level', 0),
                    'tiers':    entry.get('tiers', {}),
                    'range':    (entry.get('semantic_range') or '')[:150],
                    'status':   entry.get('status', 'draft'),
                    'overrides':entry.get('context_overrides', []),
                }

    # High-dispute codes in this chapter
    flagged = {c: v for c, v in all_codes.items() if v['disp'] >= 2}
    if flagged:
        lines.append('CONTESTED VOCABULARY IN THIS CHAPTER:')
        for code, e in sorted(flagged.items(), key=lambda x: -x[1]['disp']):
            lit = (e['tiers'].get('literal') or {}).get('primary', '')
            tho = (e['tiers'].get('thought') or {}).get('primary', '')
            note = DISPUTE_NOTES.get(code, f'Dispute level {e["disp"]}')
            lines.append(f'  {code} {e["lemma"]} ({e["translit"]}): {note}')
            lines.append(f'    Glossary proposals: Literal="{lit}" Thought="{tho}"')
            if e['range']:
                lines.append(f'    Semantic range: {e["range"]}')
            if e['overrides']:
                lines.append(f'    Context overrides: {json.dumps(e["overrides"])}')
        lines.append('')

    # Confirmed/locked entries in this chapter
    confirmed = {c: v for c, v in all_codes.items() if v['status'] in ('confirmed','override','locked')}
    if confirmed:
        lines.append('CONFIRMED GLOSSARY DECISIONS (use these):')
        for code, e in sorted(confirmed.items()):
            lit = (e['tiers'].get('literal') or {}).get('primary', '')
            med = (e['tiers'].get('mediating') or {}).get('primary', '')
            tho = (e['tiers'].get('thought') or {}).get('primary', '')
            lines.append(f'  {code} {e["lemma"]}: L="{lit}" M="{med}" T="{tho}" [{e["status"]}]')
        lines.append('')

    # Interlinear tokens
    lines.append('INTERLINEAR DATA:')
    for v_str in sorted(ch_data.keys(), key=lambda x: int(x)):
        tokens = ch_data[v_str]
        parts = []
        for tok in tokens:
            code = tok.get('s', '')
            text = tok.get('text', '')
            if code:
                e = all_codes.get(code, {})
                lemma = e.get('lemma', '') or code
                parts.append(f'{text}[{code}/{lemma}]')
            else:
                parts.append(text)
        lines.append(f'  v{v_str}: {" ".join(parts)}')

    return '\n'.join(lines)

# ── API call ──────────────────────────────────────────────────────────────────

def translate_chapter(client, book, ch_num, ch_data, glossary, model, retry=2):
    """Call Claude to translate one chapter. Returns parsed dict or None."""
    prompt = build_chapter_prompt(book, ch_num, ch_data, glossary)

    for attempt in range(retry + 1):
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=4096,
                system=SYSTEM_PROMPT,
                messages=[{'role': 'user', 'content': prompt}],
                temperature=0.2,
            )
            raw = resp.content[0].text.strip()

            # Strip markdown code fences if present
            raw = re.sub(r'^```json\s*', '', raw)
            raw = re.sub(r'\s*```$', '', raw)

            data = json.loads(raw)
            return data

        except json.JSONDecodeError as e:
            if attempt < retry:
                print(f'      JSON parse error, retrying… ({e})')
                time.sleep(2)
            else:
                print(f'      FAILED to parse JSON after {retry+1} attempts')
                return None
        except Exception as e:
            if attempt < retry:
                print(f'      API error ({e}), retrying in 5s…')
                time.sleep(5)
            else:
                print(f'      FAILED: {e}')
                return None

# ── Merge chapter data into book files ────────────────────────────────────────

def load_book_file(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}

def write_book_file(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

def merge_chapter_into_book(book_data, ch_str, ch_result, tier):
    """Merge a tier's chapter translations into the book dict."""
    if ch_str not in book_data:
        book_data[ch_str] = {}
    for v_str, vdata in ch_result.items():
        v_str = str(v_str)
        text = vdata.get(tier, '') if isinstance(vdata, dict) else str(vdata)
        book_data[ch_str][v_str] = text

def merge_notes_into_book(notes_data, ch_str, ch_result):
    """Merge reasoning notes into the notes book dict."""
    if ch_str not in notes_data:
        notes_data[ch_str] = {}
    for v_str, vdata in ch_result.items():
        v_str = str(v_str)
        if isinstance(vdata, dict) and 'notes' in vdata:
            raw_notes = vdata['notes']
            # Merge with existing token data if present
            existing = notes_data[ch_str].get(v_str, {})
            existing['reasoning'] = raw_notes
            notes_data[ch_str][v_str] = existing
        else:
            notes_data[ch_str][v_str] = notes_data[ch_str].get(v_str, {})

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--book',       help='Single book to translate (e.g. john)')
    parser.add_argument('--chapter',    type=int, help='Single chapter (requires --book)')
    parser.add_argument('--testament',  choices=['nt', 'ot'], help='Translate one testament')
    parser.add_argument('--all',        action='store_true', help='Translate full Bible')
    parser.add_argument('--overwrite',  action='store_true', help='Re-translate already-done chapters')
    parser.add_argument('--model',      default='claude-sonnet-4-6',
                        help='Claude model to use (default: claude-sonnet-4-6)')
    args = parser.parse_args()

    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    if not api_key:
        print('ERROR: ANTHROPIC_API_KEY environment variable not set.')
        print('  export ANTHROPIC_API_KEY=sk-ant-...')
        return

    client = anthropic.Anthropic(api_key=api_key)

    if args.book:
        books = [args.book.lower()]
    elif args.testament == 'nt':
        books = NT_BOOKS
    elif args.testament == 'ot':
        books = OT_BOOKS
    elif args.all:
        books = ALL_BOOKS
    else:
        parser.print_help()
        print('\nSpecify --book, --testament, or --all')
        return

    # Load glossary
    print('Loading glossary…')
    glossary = {}
    for lang in ('greek', 'hebrew'):
        path = GLOSS_DIR / f'glossary-{lang}.json'
        if path.exists():
            with open(path, encoding='utf-8') as f:
                glossary.update(json.load(f))
    print(f'  {len(glossary)} entries')
    print()

    for book in books:
        inter_path = INTER_DIR / f'{book}.json'
        if not inter_path.exists():
            print(f'[{book}] no interlinear — skipping')
            continue

        with open(inter_path, encoding='utf-8') as f:
            inter = json.load(f)

        book_name = BOOK_NAMES.get(book, book)

        # Load existing output files
        lit_path  = DRAFT_DIR / 'literal'   / f'{book}.json'
        med_path  = DRAFT_DIR / 'mediating' / f'{book}.json'
        tho_path  = DRAFT_DIR / 'thought'   / f'{book}.json'
        notes_path= NOTES_DIR / f'{book}.json'

        lit_data   = load_book_file(lit_path)
        med_data   = load_book_file(med_path)
        tho_data   = load_book_file(tho_path)
        notes_data = load_book_file(notes_path)

        chapters = sorted(inter.keys(), key=lambda x: int(x))
        if args.chapter:
            chapters = [str(args.chapter)]

        print(f'[{book_name}] {len(chapters)} chapter(s)')

        for ch_str in chapters:
            ch_num = int(ch_str)
            ch_data = inter[ch_str]

            # Check if already translated
            if not args.overwrite and ch_str in lit_data and ch_str in med_data:
                existing_v = len(lit_data.get(ch_str, {}))
                print(f'  Ch {ch_num:3}: already done ({existing_v}v) — skipping')
                continue

            n_verses = len(ch_data)
            print(f'  Ch {ch_num:3}: {n_verses}v … ', end='', flush=True)

            t_start = time.time()
            result = translate_chapter(client, book, ch_num, ch_data, glossary, args.model)

            if result is None:
                print('FAILED')
                continue

            # Result may have string chapter key or int key
            ch_result = result.get(str(ch_num)) or result.get(ch_num) or result
            if not ch_result:
                # Sometimes Claude returns the whole thing flat (verse keys at top level)
                ch_result = result

            # Merge into book files
            merge_chapter_into_book(lit_data,   ch_str, ch_result, 'lit')
            merge_chapter_into_book(med_data,   ch_str, ch_result, 'med')
            merge_chapter_into_book(tho_data,   ch_str, ch_result, 'tho')
            merge_notes_into_book(notes_data, ch_str, ch_result)

            # Write after each chapter (resume-safe)
            write_book_file(lit_path,   lit_data)
            write_book_file(med_path,   med_data)
            write_book_file(tho_path,   tho_data)
            write_book_file(notes_path, notes_data)

            elapsed = time.time() - t_start
            done_v  = len(ch_result)
            print(f'done — {done_v}v in {elapsed:.1f}s')

        print(f'  [{book_name}] complete\n')

    print('Translation complete.')
    print('The output files now contain Claude-reasoned translations.')
    print('Run python3 scripts/generate-notes.py to refresh token-level data')
    print('(the reasoning field from this script is preserved).')

if __name__ == '__main__':
    main()
