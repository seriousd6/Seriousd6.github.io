#!/usr/bin/env python3
"""
scripts/build-lxx-bridge.py — build Hebrew→Greek semantic mapping data
for the Translation Workshop LXX Bridge section.

For each disputed/key Hebrew Strong's code, records which Greek Strong's codes
the Septuagint translators used to render it, with frequency counts and
semantic notes. This shows how ancient translators navigated the same
translation decisions the Workshop user faces.

Source: curated scholarly data for the ~20 most contested Hebrew terms,
from Hatch & Redpath Concordance to the LXX, Muraoka LXX Lexicon (2009),
and NETS translation notes. Frequencies are approximate occurrence counts
in the canonical LXX (Rahlfs edition).

Output:
  data/strongs/lxx-bridge.json  keyed by H code:
    [{ greek_code, greek_lemma, frequency, note }]
    entries sorted by frequency descending.

Usage: python3 scripts/build-lxx-bridge.py
"""
import json
import os

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRONGS  = os.path.join(ROOT, 'data', 'strongs')
OUT_PATH = os.path.join(STRONGS, 'lxx-bridge.json')

# Curated LXX rendering data for key Hebrew terms.
# note: explains what the Greek choice captures vs. misses — the gap between
#   Hebrew and Greek is the translator's dilemma, and these notes frame it.
CURATED_LXX = {
    'H2617': [  # חֶסֶד — steadfast love / lovingkindness / covenantal loyalty
        {
            'greek_code': 'G1656',
            'greek_lemma': 'ἔλεος',
            'frequency': 170,
            'note': 'Primary LXX rendering — captures mercy/compassion but loses the covenantal-loyalty dimension of חֶסֶד',
        },
        {
            'greek_code': 'G5485',
            'greek_lemma': 'χάρις',
            'frequency': 12,
            'note': 'Used where the relational grace/favour aspect is foregrounded over obligation',
        },
        {
            'greek_code': 'G1343',
            'greek_lemma': 'δικαιοσύνη',
            'frequency': 4,
            'note': 'Rare — occurs where חֶסֶד appears in parallelism with צְדָקָה',
        },
    ],
    'H7307': [  # רוּחַ — spirit / Spirit / wind / breath
        {
            'greek_code': 'G4151',
            'greek_lemma': 'πνεῦμα',
            'frequency': 264,
            'note': 'Used for both Spirit of God and human spirit — same lexical ambiguity as the Hebrew',
        },
        {
            'greek_code': 'G417',
            'greek_lemma': 'ἄνεμος',
            'frequency': 31,
            'note': 'Used when physical wind is the clear referent (weather contexts)',
        },
        {
            'greek_code': 'G4157',
            'greek_lemma': 'πνοή',
            'frequency': 6,
            'note': 'Breath of life contexts (Gen 6:17, Ezek 37:5)',
        },
    ],
    'H5315': [  # נֶפֶשׁ — soul / life / self / person
        {
            'greek_code': 'G5590',
            'greek_lemma': 'ψυχή',
            'frequency': 683,
            'note': 'Dominant rendering — but ψυχή imports Greek dualism; נֶפֶשׁ refers to the whole living person, not an immortal soul housed in a body',
        },
        {
            'greek_code': 'G2222',
            'greek_lemma': 'ζωή',
            'frequency': 54,
            'note': 'Used when נֶפֶשׁ clearly means biological life',
        },
        {
            'greek_code': 'G444',
            'greek_lemma': 'ἄνθρωπος',
            'frequency': 8,
            'note': 'Where נֶפֶשׁ = person/someone (e.g. Lev 2:1 "a person")',
        },
    ],
    'H6666': [  # צְדָקָה — righteousness / justice / saving acts
        {
            'greek_code': 'G1343',
            'greek_lemma': 'δικαιοσύνη',
            'frequency': 79,
            'note': 'Primary rendering — legal/moral rightness; loses the sense of concrete saving acts that צְדָקָה often carries in Isaiah',
        },
        {
            'greek_code': 'G1656',
            'greek_lemma': 'ἔλεος',
            'frequency': 22,
            'note': 'Occurs when צְדָקָה appears alongside חֶסֶד — translators read both as aspects of covenant faithfulness',
        },
        {
            'greek_code': 'G1654',
            'greek_lemma': 'ἐλεημοσύνη',
            'frequency': 7,
            'note': '"Almsgiving/charity" — reflects post-exilic narrowing of צְדָקָה toward concrete acts of generosity',
        },
    ],
    'H3068': [  # יהוה — the divine name (Tetragrammaton)
        {
            'greek_code': 'G2962',
            'greek_lemma': 'κύριος',
            'frequency': 6318,
            'note': '"Lord" — substitution for the divine Name following Second Temple practice; obscures the personal-name character of יהוה and shaped NT Christology when applied to Jesus',
        },
    ],
    'H430': [  # אֱלֹהִים — God / gods
        {
            'greek_code': 'G2316',
            'greek_lemma': 'θεός',
            'frequency': 2570,
            'note': 'Standard rendering; singular θεός for the grammatically plural אֱלֹהִים — LXX resolves the tension in favour of monotheism',
        },
        {
            'greek_code': 'G32',
            'greek_lemma': 'ἄγγελος',
            'frequency': 22,
            'note': 'In Ps 8:5 and divine council passages — "angels/heavenly beings"; used when אֱלֹהִים clearly refers to the heavenly court',
        },
    ],
    'H1285': [  # בְּרִית — covenant
        {
            'greek_code': 'G1242',
            'greek_lemma': 'διαθήκη',
            'frequency': 272,
            'note': 'Near-exclusive rendering — but διαθήκη normally means "last will/testament" in secular Greek, not a bilateral covenant; this shaped the NT phrase "new covenant" toward a testamentary reading',
        },
    ],
    'H571': [  # אֱמֶת — truth / faithfulness / reliability
        {
            'greek_code': 'G225',
            'greek_lemma': 'ἀλήθεια',
            'frequency': 92,
            'note': 'Dominant rendering — but ἀλήθεια is propositional truth; אֱמֶת is relational faithfulness/reliability (cognate with אָמַן, root of "amen")',
        },
        {
            'greek_code': 'G1343',
            'greek_lemma': 'δικαιοσύνη',
            'frequency': 14,
            'note': 'Occurs when אֱמֶת appears in contexts of moral rectitude or God\'s covenant obligations',
        },
    ],
    'H2580': [  # חֵן — grace / favour
        {
            'greek_code': 'G5485',
            'greek_lemma': 'χάρις',
            'frequency': 67,
            'note': 'Natural rendering — χάρις captures unmerited favour; חֵן emphasises the response it evokes ("finding grace in someone\'s eyes")',
        },
        {
            'greek_code': 'G1656',
            'greek_lemma': 'ἔλεος',
            'frequency': 8,
            'note': 'Occasional — where חֵן appears alongside חֶסֶד, both rendered by the mercy cluster',
        },
    ],
    'H7965': [  # שָׁלוֹם — peace / wholeness / well-being
        {
            'greek_code': 'G1515',
            'greek_lemma': 'εἰρήνη',
            'frequency': 220,
            'note': 'Standard rendering — but εἰρήνη is primarily absence of war/conflict; שָׁלוֹם is wholeness, well-being, right relationship — far broader in scope',
        },
        {
            'greek_code': 'G4991',
            'greek_lemma': 'σωτηρία',
            'frequency': 9,
            'note': 'Rare — used in military/deliverance contexts where שָׁלוֹם carries the sense of safety/salvation',
        },
    ],
    'H3519': [  # כָּבוֹד — glory / honour / weight / radiance
        {
            'greek_code': 'G1391',
            'greek_lemma': 'δόξα',
            'frequency': 215,
            'note': 'LXX transformed δόξα from its Greek sense of "opinion/reputation" into "divine radiance/splendour" — this is the word\'s greatest semantic shift in translation history',
        },
        {
            'greek_code': 'G5092',
            'greek_lemma': 'τιμή',
            'frequency': 18,
            'note': 'Used when כָּבוֹד is primarily honour given to humans rather than divine glory',
        },
    ],
    'H6944': [  # קֹדֶשׁ — holiness / the holy / consecrated space
        {
            'greek_code': 'G40',
            'greek_lemma': 'ἅγιος',
            'frequency': 470,
            'note': 'Standard rendering — ἅגיος acquired the "set apart for God" meaning almost entirely from its LXX use; in secular Greek it had little religious weight',
        },
        {
            'greek_code': 'G37',
            'greek_lemma': 'ἁγιάζω',
            'frequency': 62,
            'note': 'Verbal form — used when קֹדֶשׁ appears in consecrating/sanctifying contexts',
        },
    ],
    'H5769': [  # עוֹלָם — eternity / perpetuity / the distant age
        {
            'greek_code': 'G165',
            'greek_lemma': 'αἰών',
            'frequency': 386,
            'note': '"Age" or "eternal duration" — the LXX equation of עוֹלָם with αἰών drove the NT phrase εἰς τοὺς αἰῶνας and the debate over "eternal" vs. "age-long"',
        },
        {
            'greek_code': 'G166',
            'greek_lemma': 'αἰώνιος',
            'frequency': 68,
            'note': 'Adjectival form — "ζωὴ αἰώνιος" (eternal life) translates the Hebrew concept of enduring life in the coming age',
        },
    ],
    'H539': [  # אָמַן — trust / believe / be firm (root of אֱמוּנָה, faith)
        {
            'greek_code': 'G4100',
            'greek_lemma': 'πιστεύω',
            'frequency': 47,
            'note': 'LXX uses πιστεύω for the Hiphil (to trust/believe); NT saving faith in πιστεύω is grounded in this rendering of אָמַן — Gen 15:6 "Abraham πιστεύω"',
        },
        {
            'greek_code': 'G3982',
            'greek_lemma': 'πείθω',
            'frequency': 12,
            'note': '"Persuade/rely on" — used when אָמַן emphasises confident reliance on a person',
        },
    ],
    'H3045': [  # יָדַע — to know (intimate / experiential knowledge)
        {
            'greek_code': 'G1097',
            'greek_lemma': 'γινώσκω',
            'frequency': 360,
            'note': 'Standard rendering — but γινώσκω is cognitive/experiential; יָדַע includes knowing by intimate relationship (Gen 4:1 "Adam knew Eve") and moral discernment',
        },
        {
            'greek_code': 'G1492',
            'greek_lemma': 'οἶδα',
            'frequency': 85,
            'note': 'Used for knowing in the sense of acquired knowledge/recognition; less relational than γινώσκω',
        },
    ],
    'H8199': [  # שָׁפַט — to judge / govern / vindicate the oppressed
        {
            'greek_code': 'G2919',
            'greek_lemma': 'κρίνω',
            'frequency': 133,
            'note': 'Standard rendering — but שָׁפַט includes vindicating the oppressed and governing justly, not only passing judgment; κρίνω has a more neutral decisional sense',
        },
        {
            'greek_code': 'G1252',
            'greek_lemma': 'διακρίνω',
            'frequency': 8,
            'note': 'Used when שָׁפַט implies discerning or distinguishing between cases',
        },
    ],
    'H4428': [  # מֶלֶךְ — king
        {
            'greek_code': 'G935',
            'greek_lemma': 'βασιλεύς',
            'frequency': 2528,
            'note': 'Near-exclusive rendering — straightforward equivalence',
        },
    ],
}


def main():
    os.makedirs(STRONGS, exist_ok=True)

    print('Building LXX bridge from curated scholarly data…')
    print(f'  {len(CURATED_LXX)} Hebrew codes mapped')

    total_pairs = sum(len(v) for v in CURATED_LXX.values())
    print(f'  {total_pairs} Greek rendering pairs total')

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(CURATED_LXX, f, ensure_ascii=False, indent=2)

    kb = os.path.getsize(OUT_PATH) // 1024
    print(f'  Wrote {len(CURATED_LXX)} entries  {kb} KB → {OUT_PATH}')
    print('\nDone. Run scripts/seed-glossary.py to inject lxx_bridge into phase bundles.')


if __name__ == '__main__':
    main()
