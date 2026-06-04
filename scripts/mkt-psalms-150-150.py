"""
MKT Psalms chapter 150 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-150-150.py

=== Overview ===

Psalm 150 is the Grand Doxology — the liturgical climax of the entire Psalter.
Five psalms of pure hallelujah praise close the book (146–150); Psalm 150
is the peak. Its architecture is intentional:

- v1: WHERE to praise — sanctuary (earthly) + firmament (cosmic expanse)
- v2: WHY to praise — mighty acts + surpassing greatness
- vv3–5: HOW to praise — eight instruments + dance
- v6: WHO praises — every breathing thing; no exclusion

The psalm makes no petitions, no laments, no conditions. It is the Psalter's
final word: total, universal, cosmic doxology. The T tier preserves the
terse, cadenced Hebrew couplets that give the psalm its driving momentum.

=== Contested-term decisions ===

H3050 (יָהּ, Yah): The short form of YHWH, appearing in "Hallelujah"
    (hallelu-Yah = praise Yah). Rendered "LORD" in all tiers, consistent
    with every prior Psalms script. "Praise the LORD!" = the conventional
    English rendering of hallelujah.

H410 (אֵל, El) in v1: "hallelu-El b'qodsho" = Praise God/El in his
    sanctuary. El here is a straightforward name for God, not a title of
    might (as it is in some contexts). All tiers: "God."

H7549 (רָקִיעַ, raqia): The dome/vault/firmament of Gen 1:6–8 — the solid
    sky-dome that separates upper and lower waters. With H5797 (oz, strength/
    power): "firmament of his power." L: "firmament" (source-preserving);
    M: "vault" (natural English); T: "vast expanse" (evokes the cosmic dome).
    The echo of Gen 1:6 is intentional: God stretched out the raqia; now all
    creation in that raqia is called to praise him.

H7782 (שׁוֹפָר, shofar): A ram's horn, not a metal instrument. The KJV
    "trumpet" is conventional but inexact. L: "shofar" (source-accurate);
    M: "trumpet" (established English convention for clarity); T: "shofar"
    (the T tier here serves the scholarly reader who should know it is a
    ram's horn). Documented because this deviates from the token gloss.

H5035 (נֶבֶל, nebel): The large, harp-like stringed instrument (psaltery/
    lute). H3658 (כִּנּוֹר, kinnor): The smaller lyre — David's instrument
    (1 Sam 16:23). L/M/T: "lyre and harp" — nebel first, kinnor second,
    following the Hebrew order. "Psaltery" (KJV) is archaic; "lyre" is the
    consensus modern scholarly rendering of nebel.

H8596 (תֹּף, toph): Tambourine/hand-drum. H4234 (מָחוֹל, machol): Dance
    (noun). The pairing toph umachol is a fixed liturgical formula (Ps 149:3;
    Jer 31:4). All tiers: "tambourine and dance."

H4482 (מִנִּים, minnim): Strings / stringed instruments — the precise
    instrument is uncertain; it occurs only here. H5748 (עּוּגָב, ugab):
    A pipe or flute instrument (the only certain reed/wind instrument in the
    list). All tiers: "strings and flute" — "organ" (KJV for ugab) is
    anachronistic.

H6767 (צֶלְצֶל / צִלְצָל, tzeliltzel): Cymbals. Appears twice in v5 with
    different modifiers:
    1) H8088 (שֵׁמַע, shema — sound, hearing): cymbals of sound =
       "resounding cymbals" — the reverberant, sustained ring.
    2) H8643 (תְּרוּעָה, teruah — loud acclamation, blast, shout):
       cymbals of acclamation = "clashing/crashing cymbals" — the
       sharp, striking clash of the liturgical shout. The teruah is the
       same sonic idiom as the shofar-blast that accompanied the ark
       (2 Sam 6:15) and the Jubilee (Lev 25:9). L/M: "resounding...
       clashing"; T: "resounding... crashing" for the cadential rhythm.

H5397 (נְשָׁמָה, neshama): Breath, breath of life. The same word as
    Gen 2:7 — the breath God breathed into Adam's nostrils to animate him.
    The final verse thus closes a canonical arc: God gave the neshama;
    all who carry it are summoned to return it in praise. L: "breathing
    thing" (literal); M: "that has breath" (natural English); T: "living
    breath" (carries the Gen 2:7 resonance — "living" echoes the act of
    creation, "breath" names the gift).

=== OT intertextuality ===

v1 raqia — echoes Gen 1:6–8. The same firmament God stretched out in
    creation is now the stage from which he is praised. Praise fills the
    space creation opened up.

v6 neshama — echoes Gen 2:7. The divine breath that made Adam a living
    soul (nephesh chayah) is the same faculty by which "everything that
    breathes" now praises its Giver. The Psalter ends where creation
    began: with God's own breath, returned to him as doxology.

Instruments in vv3–5 — match the temple worship descriptions in 1 Chr 15–16
    (when David installed the ark in Jerusalem) and 2 Chr 5:12–13 (the
    dedication of Solomon's temple). The list is comprehensive: wind,
    strings, percussion, dance — the whole range of human musical expression.

=== Aspect and tense notes ===

The psalm is entirely in the imperative/jussive mood. There are no
    indicative-historical verbs. Every line is a command addressed to the
    entire creation. The terse Hebrew is 2–4 words per half-verse; the
    L tier preserves this terseness. M expands minimally for idiom. T uses
    line breaks to honour the staccato pulse of the Hebrew.
"""

import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]


PSALMS = {

  # ===========================================================================
  # Psalm 150 — The Grand Doxology
  # Cosmic and earthly praise; eight instruments + dance; every breathing thing
  # ===========================================================================
  "150": {
    "1": {
      "L": "Praise the LORD! Praise God in his sanctuary; praise him in the firmament of his power.",
      "M": "Praise the LORD! Praise God in his holy sanctuary; praise him in the vault of his power.",
      "T": "Praise the LORD!\nPraise God in his sanctuary —\npraise him in the vast expanse of his power."
    },
    "2": {
      "L": "Praise him for his mighty acts; praise him according to his abundant greatness.",
      "M": "Praise him for his mighty deeds; praise him for the fullness of his greatness.",
      "T": "Praise him for his mighty acts —\npraise him for the surpassing greatness\nof all he is."
    },
    "3": {
      "L": "Praise him with the blast of the shofar; praise him with lyre and harp.",
      "M": "Praise him with the blast of the trumpet; praise him with lyre and harp.",
      "T": "Praise him with the shofar's cry —\npraise him with lyre\nand harp."
    },
    "4": {
      "L": "Praise him with tambourine and dance; praise him with strings and pipe.",
      "M": "Praise him with tambourine and dancing; praise him with strings and flute.",
      "T": "Praise him with tambourine and dance —\npraise him with strings\nand flute."
    },
    "5": {
      "L": "Praise him with resounding cymbals; praise him with clashing cymbals.",
      "M": "Praise him with resounding cymbals; praise him with crashing cymbals.",
      "T": "Praise him with resounding cymbals —\npraise him with crashing cymbals."
    },
    "6": {
      "L": "Let every breathing thing praise the LORD! Praise the LORD!",
      "M": "Let everything that has breath praise the LORD! Praise the LORD!",
      "T": "Let every living breath praise the LORD —\nPraise the LORD!"
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 150 written.')

if __name__ == '__main__':
    main()
