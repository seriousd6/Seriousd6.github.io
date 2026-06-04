"""
MKT Psalms chapters 126–131 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-126-131.py

=== Overview of this unit ===

All six psalms belong to the Songs of Ascents (Pss 120–134), pilgrimage hymns
sung as worshippers went up to Jerusalem for the three annual festivals. They
are marked by a characteristic stepped-repetition style (anadiplosis), brevity,
and a movement between lament and praise.

Ps 126 (6 v) — The Restoration of Zion. A congregational psalm in two halves:
    the memory of the return from exile (vv1-3) and a prayer for fuller restoration
    (v4), closing with the great sowing/reaping promise (vv5-6). The frozen Hebrew
    idiom שׁוּב שְׁבוּת (shuv shevut) at vv1 and 4 means "reverse the fortunes"
    not merely "release from captivity" — it is used in contexts that have nothing
    to do with Babylon (e.g. Job 42:10). Translated "restored the fortunes" in M/T;
    "turned the captivity" in L to preserve the word-for-word feel. The "streams in
    the Negev" (v4) are the desert wadis that run only after heavy rain — a vivid
    image of sudden reversal. Vv5-6 shape the NT theology of redemptive suffering
    (John 12:24; Rom 8:18-23; Gal 6:9): the seed goes into the ground in grief;
    the harvest comes in joy.

Ps 127 (5 v) — Unless the LORD Builds. A wisdom psalm attributed to Solomon
    (Jedidiah, "beloved of the LORD" — same root as H3039 yedid at v2). The
    opening double-maxim (house/city) establishes the principle of divine priority;
    the famous v2 follows with the contrast between anxious labour and the gift of
    rest. V2 is deliberately ambiguous: God gives sleep "to his beloved" (Heb.
    liydido) — the gift is rest itself, not just what happens during sleep. Vv3-5
    shift from the public arena (city/house) to the domestic: children as divine
    gift, arrows in the quiver, the blessed man at the gate.

Ps 128 (6 v) — Blessed Is Everyone Who Fears the LORD. A blessing psalm on the
    domestic rewards of covenant faithfulness: table, wife like a vine, children
    like olive shoots, grandchildren, and peace on Israel. The ashrei ("blessed")
    opening echoes Ps 1:1 and frames the whole as a wisdom observation. The closing
    v6 shifts to communal scope: shalom upon Israel.

Ps 129 (8 v) — Greatly Have They Afflicted Me. Communal lament-turned-confidence.
    The refrain of vv1-2 mirrors Ps 124:1-2's liturgical echo form. The ploughing
    image (v3) is uniquely graphic: the enemy is not merely attacking but farming
    on Israel's back — exploitation turned into agricultural metaphor. The LORD's
    cutting of the cords (v4) is the decisive act. The imprecation (vv5-8) is
    characterised by withering rather than violent destruction: enemies who are
    like rooftop grass — rootless, unable to hold harvest blessing.

Ps 130 (8 v) — De Profundis. One of the seven Penitential Psalms (the sixth in
    the traditional list); Luther called it one of the "Pauline psalms." Its
    movement is the arc of the Psalter in miniature: cry (vv1-2), confession and
    forgiveness (vv3-4), waiting (vv5-6), and communal hope (vv7-8). The
    watchmen/morning image (v6) uses double repetition — the only verse in the
    Psalter that exactly repeats its own second half — to enact the experience of
    waiting. H5547 selichah ("forgiveness," v4) appears only here in the OT;
    H6304 peduth ("redemption," v7) is the noun form of padah (ransom/redeem).

Ps 131 (3 v) — A Humble Heart. The shortest of the Songs of Ascents (with
    Ps 117). David's psalm of childlike trust: not haughty, not reaching for what
    is too great. The weaned-child image (v2) is carefully chosen: a weaned child
    is past the feeding-need stage — it rests with its mother not out of hunger
    but out of secure love. The silence of v2 is contentment, not despair. The
    psalm closes, like Ps 130, with a call to communal hope.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M/T throughout. Consistent with all prior
    Psalms scripts.

H136 (אֲדֹנָי, Adonai): "Lord" (not small-caps) in L/M/T where distinct from
    YHWH. At 130:2, 3 Adonai appears alongside YHWH in the same verse — the
    distinction is preserved: "LORD" for YHWH, "Lord" for Adonai.

H3050 (יָהּ, Yah): Short form of YHWH at 130:3. Rendered "LORD" (same as
    YHWH) consistent with prior scripts; the use of the short form in the same
    verse as Adonai is a literary intensification, not a different deity.

H2617 (חֶסֶד, chesed): "steadfast love" in L/M/T. At 130:7 it anchors the
    communal hope: "with the LORD there is steadfast love." Consistent throughout.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M/T. At 130:5-6, the nefesh waits and
    longs; at 131:2, the nefesh is quieted. The embodied self, not the Greek
    immaterial soul; but "soul" preserves the traditional piety and cadence.

H7622 / H7870 (שְׁבוּת / שִׁיבַת, shevut / shivat): At 126:1 and 126:4.
    The phrase שׁוּב שְׁבוּת is a frozen idiom for "reverse/restore fortunes,"
    not limited to Babylonian captivity (cf. Job 42:10, Ezek 16:53). L uses
    "turned the captivity" (literal word-for-word); M/T use "restored the
    fortunes" to avoid restricting the meaning to one historical exile.

H5547 (סְלִיחָה, selichah): "forgiveness" at 130:4. This noun occurs only
    once in the entire OT. Related to sālach (H5545), to forgive/pardon.
    Rendered "forgiveness" in all tiers; T unpacks the awe this evokes.

H6304 (פְּדוּת, peduth): "redemption" at 130:7. Noun of H6299 padah, to
    ransom/redeem/liberate. "Redemption" in all tiers. Suggests liberation by
    payment of price — stronger than mere forgiveness.

H3039 (יְדִיד, yedid): "beloved" at 127:2. Same root as Jedidiah (Solomon's
    other name, 2 Sam 12:25). The word carries covenantal warmth; "his beloved"
    is accurate and worth preserving.

H1580 (גָּמֻל, gamul / weaned child): At 131:2. A weaned child is no longer
    nursing — the rest is contentment, not hunger. Both occurrences of gamul in
    v2 rendered "weaned child" to preserve the deliberate repetition.

H435 (אַשְׁרֵי, ashrei): "blessed" in L/M/T at 127:5 and 128:1-2, 4.
    Consistent with all prior Psalms scripts. Same word as Ps 1:1.

=== OT intertextuality and NT connections ===

Ps 126:5-6 — The sowing/reaping-with-tears/joy pattern underlies John 12:24
    (the grain of wheat falling into the ground), 2 Cor 9:6, and Gal 6:9. Paul
    does not quote the psalm directly but the image is foundational.

Ps 127:1 — "Unless the LORD builds the house" is cited in early Christian
    reflection on the church as God's building (1 Cor 3:9-15; Eph 2:20-22).

Ps 130:3-4 — "If you mark iniquities, who could stand? But there is forgiveness
    with you." Luther saw this as the Pauline question and answer in miniature
    (Rom 3:23 + 8:1). The logic of v4 is subtle: forgiveness creates fear (awe/
    reverence), not presumption — because only a holy God's forgiveness has weight.

Ps 130:7-8 — "Plentiful redemption" and "redeem from all iniquities" anticipate
    the NT vocabulary of ἀπολύτρωσις and the complete work of Christ (Tit 2:14,
    Heb 9:12). The T tier notes the redemptive arc.

Ps 131:2 — The weaned-child image for the soul's rest before God is one of the
    OT's most striking images of what NT theology calls "peace with God" (Rom 5:1).
    Not striving, not pleading — simply resting.

=== Aspect and tense notes ===

Ps 126: Perfect verbs in vv1-3 describe completed rescue (past, certain). V4 is
    imperative ("restore"). Vv5-6 mix participles and imperfects — the sowing/
    reaping principle is presented as a timeless promise, not an historical claim.

Ps 127: Imperfects throughout in the "unless... in vain" structure, expressing
    general truths. V2 has two infinitives (rising/sitting) used substantivally.
    The final clause "he gives sleep" is a perfect of certainty.

Ps 128: Imperfects as future promises ("you shall eat," "you shall see").
    The ashrei verbs are participial constructions — ongoing characteristic
    behaviour, not one-time acts.

Ps 129: Perfects of historical experience (affliction) alternate with
    jussives (the imprecations in vv5-8). The ploughing image (v3) is vivid
    perfect — it happened and its furrow remains.

Ps 130: Perfect of initiated action at v1 (I called); imperatives at v2 (hear);
    conditional at v3 (if you should mark); statement of fact at v4; perfects
    of trust at vv5-6. The watchman repetition (v6) is imperfect — habitual,
    ongoing longing. V7 is jussive (let Israel hope).

Ps 131: The verbs in vv1-2 are perfect (I have not lifted up, I have calmed
    and quieted) — completed inner acts whose result is the present state.
    The weaned child comparison uses כְּ (like) twice; the soul is declared
    to be in that state.
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
  # Psalm 126 — When the LORD Restored the Fortunes of Zion
  # Memory of return from exile; prayer for fuller restoration; sowing in tears
  # ===========================================================================
  "126": {
    "1": {
      "L": "A Song of Ascents. When the LORD turned the captivity of Zion, we were like those who dream.",
      "M": "A Song of Ascents. When the LORD restored the fortunes of Zion, we were like people in a dream.",
      "T": "A Song of Ascents.\nWhen the LORD turned Zion's fortunes around,\nwe were like people dreaming."
    },
    "2": {
      "L": "Then our mouth was filled with laughter and our tongue with shouts of joy; then they said among the nations, 'The LORD has done great things for them.'",
      "M": "Then our mouths were full of laughter and our tongues rang out with shouts of joy; the nations were saying, 'The LORD has done great things for them!'",
      "T": "Then our mouths were full of laughter\nand our tongues rang with joy.\nThe nations said:\n'The LORD has done great things for them!'"
    },
    "3": {
      "L": "The LORD has done great things for us; we are glad.",
      "M": "The LORD has done great things for us — and we are overjoyed.",
      "T": "The LORD has done great things for us.\nWe are glad."
    },
    "4": {
      "L": "Restore our fortunes, O LORD, like streams in the Negev.",
      "M": "Restore our fortunes, O LORD, like the streams that suddenly fill the desert wadis.",
      "T": "Turn back our fortunes, O LORD —\nlike the wadis of the Negev\nrunning full after rain."
    },
    "5": {
      "L": "Those who sow in tears shall reap in joy.",
      "M": "Those who plant in tears will harvest with shouts of joy.",
      "T": "Those who sow in tears\nwill reap\nwith shouts of joy."
    },
    "6": {
      "L": "He who goes forth weeping, bearing precious seed, shall come home with shouts of joy, bringing his sheaves with him.",
      "M": "The one who sets out weeping, carrying the seed bag, will come home with joyful shouts, loaded down with the harvest.",
      "T": "He goes out weeping,\ncarrying his precious seed —\nbut he comes home with shouts of joy,\nladen with sheaves."
    }
  },

  # ===========================================================================
  # Psalm 127 — Unless the LORD Builds
  # Of Solomon; divine priority in all labour; children as heritage
  # ===========================================================================
  "127": {
    "1": {
      "L": "A Song of Ascents. Of Solomon. Unless the LORD builds the house, those who build it labor in vain; unless the LORD keeps watch over the city, the watchman stays awake in vain.",
      "M": "A Song of Ascents. Of Solomon. Unless the LORD builds the house, the builders work to no purpose; unless the LORD guards the city, the sentinels watch for nothing.",
      "T": "A Song of Ascents. For Solomon.\nUnless the LORD builds the house,\nthe builders labor in vain.\nUnless the LORD guards the city,\nthe watchman watches for nothing."
    },
    "2": {
      "L": "It is in vain for you to rise early, to stay up late, to eat the bread of sorrows; for so he gives sleep to his beloved.",
      "M": "It is pointless to rise before dawn and work until dark, eating meals of anxious toil — for the LORD gives sleep as a gift to those he loves.",
      "T": "Why rise so early? Why sit up so late?\nEating anxious bread?\nFor the LORD gives to his beloved\nthe gift of sleep."
    },
    "3": {
      "L": "Behold, children are a heritage from the LORD; the fruit of the womb is his reward.",
      "M": "Yes, children are a gift from the LORD; they are a reward he gives.",
      "T": "Look — children are a heritage from the LORD.\nThe fruit of the womb\nis his reward."
    },
    "4": {
      "L": "Like arrows in the hand of a warrior are the children of one's youth.",
      "M": "Children born in a man's prime are like arrows in the hand of a soldier.",
      "T": "Like arrows in a warrior's hand —\nso are the children\nborn in your prime."
    },
    "5": {
      "L": "Blessed is the man who fills his quiver with them; he will not be put to shame when he speaks with his enemies in the gate.",
      "M": "How blessed is the man who has his quiver full of them! He will not be put to shame when he faces his enemies at the city gate.",
      "T": "Blessed is the man whose quiver is full of them —\nhe will not be put to shame\nwhen he faces his enemies at the gate."
    }
  },

  # ===========================================================================
  # Psalm 128 — Blessed Is Everyone Who Fears the LORD
  # Wisdom blessing on the household of covenant faithfulness
  # ===========================================================================
  "128": {
    "1": {
      "L": "A Song of Ascents. Blessed is everyone who fears the LORD, who walks in his ways.",
      "M": "A Song of Ascents. How blessed is every person who fears the LORD and walks in his ways.",
      "T": "A Song of Ascents.\nBlessed — truly blessed —\nis everyone who fears the LORD,\nwho walks in his ways."
    },
    "2": {
      "L": "The labor of your hands you shall eat; blessed shall you be, and it shall be well with you.",
      "M": "You will enjoy the fruit of your labor; you will be blessed, and things will go well for you.",
      "T": "What your hands work for,\nyou will eat.\nBlessed you will be —\nand all will be well."
    },
    "3": {
      "L": "Your wife shall be like a fruitful vine in the innermost parts of your house; your children like olive shoots around your table.",
      "M": "Your wife will be like a fruitful vine flourishing within your home; your children like young olive trees gathered around your table.",
      "T": "Your wife — a fruitful vine\nin the heart of your home.\nYour children — olive saplings\naround your table."
    },
    "4": {
      "L": "Behold, thus shall the man be blessed who fears the LORD.",
      "M": "This is the blessing that comes to the man who fears the LORD.",
      "T": "See — this is how the man who fears the LORD\nis blessed."
    },
    "5": {
      "L": "May the LORD bless you from Zion, and may you see the prosperity of Jerusalem all the days of your life.",
      "M": "May the LORD bless you from Zion; may you see Jerusalem flourish all the days of your life.",
      "T": "May the LORD bless you from Zion.\nMay you see Jerusalem prosper\nall the days of your life."
    },
    "6": {
      "L": "May you see your children's children! Peace be upon Israel.",
      "M": "May you live to see your grandchildren. Peace be upon Israel.",
      "T": "May you see your children's children.\nPeace upon Israel."
    }
  },

  # ===========================================================================
  # Psalm 129 — Greatly Have They Afflicted Me
  # Communal lament of persistent suffering; confidence in the LORD's justice;
  # imprecation against those who hate Zion
  # ===========================================================================
  "129": {
    "1": {
      "L": "A Song of Ascents. 'Many a time have they afflicted me from my youth' — let Israel now say.",
      "M": "A Song of Ascents. 'Again and again they have attacked me since my earliest days' — let Israel say this now.",
      "T": "A Song of Ascents.\n'Many times they have set upon me from my youth' —\nlet Israel say it now."
    },
    "2": {
      "L": "Many a time have they afflicted me from my youth, yet they have not prevailed against me.",
      "M": "Again and again they have attacked me since my earliest days, and yet they have never overcome me.",
      "T": "Many times they have set upon me from my youth —\nand yet\nthey have not prevailed."
    },
    "3": {
      "L": "The plowers plowed upon my back; they made long their furrows.",
      "M": "They plowed across my back like farmers cutting their furrows; they made them long and deep.",
      "T": "They plowed across my back —\nthe furrows they cut\nran deep and long."
    },
    "4": {
      "L": "The LORD is righteous; he has cut the cords of the wicked.",
      "M": "But the LORD is righteous — he has cut through the ropes the wicked used to bind me.",
      "T": "The LORD is righteous —\nhe has cut the cords\nof the wicked."
    },
    "5": {
      "L": "May all who hate Zion be put to shame and turned backward.",
      "M": "May every one who hates Zion be put to shame and driven back.",
      "T": "May all who hate Zion\nbe put to shame\nand turned back."
    },
    "6": {
      "L": "Let them be as the grass on the housetops, which withers before one can pluck it up.",
      "M": "May they be like grass growing on a flat rooftop, which withers before it even has a chance to grow.",
      "T": "Let them be like grass on the housetops —\nwithering\nbefore it ever grows."
    },
    "7": {
      "L": "With which the reaper does not fill his hand nor the binder of sheaves his arms,",
      "M": "No reaper ever fills his hands with it, and no one gathers it into sheaves —",
      "T": "No reaper fills his hand with it.\nNo one gathers it\ninto sheaves."
    },
    "8": {
      "L": "nor do those who pass by say, 'The blessing of the LORD be upon you! We bless you in the name of the LORD.'",
      "M": "and no one passing by will say, 'The LORD's blessing be on you! We pronounce blessing over you in the name of the LORD.'",
      "T": "No one passing by will say:\n'The LORD's blessing be upon you!'\n'We bless you in the name of the LORD!'"
    }
  },

  # ===========================================================================
  # Psalm 130 — De Profundis
  # One of the seven Penitential Psalms; cry from depths, forgiveness, waiting,
  # and the hope of plentiful redemption; Luther called it a "Pauline psalm"
  # ===========================================================================
  "130": {
    "1": {
      "L": "A Song of Ascents. Out of the depths I call to you, O LORD.",
      "M": "A Song of Ascents. From the depths of despair I cry out to you, O LORD.",
      "T": "A Song of Ascents.\nOut of the depths I cry to you,\nO LORD."
    },
    "2": {
      "L": "O Lord, hear my voice; let your ears be attentive to the voice of my supplications.",
      "M": "O Lord, hear my voice; let your ears be open to my pleading.",
      "T": "O Lord — hear my voice.\nLet your ears be attentive\nto my cries for mercy."
    },
    "3": {
      "L": "If you, O LORD, should mark iniquities, O Lord, who could stand?",
      "M": "If you, O LORD, kept a record of sins, Lord, who could stand before you?",
      "T": "If you, LORD, were to count every iniquity —\nO Lord,\nwho could stand?"
    },
    "4": {
      "L": "But there is forgiveness with you, that you may be feared.",
      "M": "But forgiveness is found with you — and that is why you are held in awe.",
      "T": "But with you there is forgiveness —\nand that is why\nyou are held in awe."
    },
    "5": {
      "L": "I wait for the LORD, my soul waits, and in his word I hope.",
      "M": "I wait for the LORD — my whole being waits — and in his word I put my hope.",
      "T": "I wait for the LORD.\nMy soul waits —\nand in his word I hope."
    },
    "6": {
      "L": "My soul longs for the Lord more than watchmen for the morning, more than watchmen for the morning.",
      "M": "My soul waits for the Lord more than sentinels long for the morning light — yes, more than sentinels wait for morning.",
      "T": "My soul waits for the Lord\nmore than watchmen wait for morning —\nmore than watchmen wait for morning."
    },
    "7": {
      "L": "Let Israel hope in the LORD, for with the LORD is steadfast love, and with him is plentiful redemption.",
      "M": "O Israel, put your hope in the LORD, for with the LORD is steadfast love, and with him is abundant redemption.",
      "T": "O Israel — hope in the LORD!\nWith the LORD is steadfast love;\nwith him is plentiful redemption."
    },
    "8": {
      "L": "And he will redeem Israel from all his iniquities.",
      "M": "He will redeem Israel from all its sins.",
      "T": "He will redeem Israel\nfrom all\nits iniquities."
    }
  },

  # ===========================================================================
  # Psalm 131 — A Humble Heart
  # Of David; childlike trust; the weaned child at rest with its mother;
  # the opposite of the pride that grasps at what is too great
  # ===========================================================================
  "131": {
    "1": {
      "L": "A Song of Ascents. Of David. O LORD, my heart is not lifted up; my eyes are not raised too high; I do not occupy myself with great matters or with things too wonderful for me.",
      "M": "A Song of Ascents. Of David. LORD, my heart is not proud; my eyes are not raised in arrogance; I do not involve myself with things too grand or too marvellous for me.",
      "T": "A Song of Ascents. Of David.\nO LORD, my heart is not proud.\nMy eyes are not raised too high.\nI do not reach for things too great,\ntoo wonderful for me."
    },
    "2": {
      "L": "Surely I have calmed and quieted my soul, like a weaned child with its mother; like a weaned child is my soul within me.",
      "M": "No, I have settled and silenced my soul; like a weaned child resting contentedly with its mother — like a weaned child, my soul is at rest within me.",
      "T": "But I have stilled and quieted my soul —\nlike a weaned child\ncontent in its mother's arms.\nLike a weaned child:\nthat is my soul within me."
    },
    "3": {
      "L": "Let Israel hope in the LORD from this time forth and forevermore.",
      "M": "O Israel, put your hope in the LORD both now and forever.",
      "T": "O Israel — hope in the LORD,\nfrom this moment forward\nand forever."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 126–131 written.')

if __name__ == '__main__':
    main()
