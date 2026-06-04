"""
MKT Psalms chapters 132–137 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-132-137.py

=== Overview of this unit ===

Psalms 132–137 span the close of the Songs of Ascents (Psalms 120–134) and the
opening of the final Davidic grouping (138–145), followed by the exile lament of
Psalm 137.

Ps 132 (18 v) — The Davidic Covenant and the Election of Zion. The longest Ascent
    psalm and the only royal psalm in the collection. Structured as two matching
    panels: David's oath to find a home for the ark (vv1–10) and the LORD's
    answering oath to David (vv11–18). The "afflictions" of v1 are David's
    labours in pursuit of bringing the ark to Jerusalem (the entire narrative of
    2 Sam 6). The ark is located at Ephrathah / fields of Jaar (= Kiriath-jearim,
    where it rested 20 years after the Philistines returned it, 1 Sam 7:1–2).
    The oracle in vv11–18 is the Davidic covenant given poetic form: a conditional
    succession promise (vv11–12) + the unconditional election of Zion (vv13–14)
    + a cascade of blessings (vv15–18). The "horn" (v17) is the messianic shoot
    of Davidic strength (cf. Ezek 29:21; Luke 1:69); the "lamp" is the promised
    dynasty that the LORD will not extinguish (cf. 1 Kgs 11:36; 2 Kgs 8:19).

Ps 133 (3 v) — The Blessing of Unity. A wisdom miniature on fraternal harmony.
    Two similes: oil running from head to beard to hem (Aaron's priestly
    consecration — blessing flows from above) and the dew of Hermon on Zion
    (extravagant northern dew covering the southern hill — life out of all
    proportion to what Zion could produce). The phrase "life for evermore" (ki
    sham tzivvah YHWH et-ha-berakha) is the theological landing point: where
    such unity exists the LORD commands covenant life.

Ps 134 (3 v) — Night Liturgy / Blessing at the Close of Ascents. The pilgrim
    songs end with a mutual blessing: the congregation calls the night-watch
    priests to bless the LORD (vv1–2); the priests bless the congregation in
    return (v3). This is the liturgical hinge between arrival and departure.

Ps 135 (21 v) — Hallelujah: The LORD Above All Gods. Praise for the LORD's
    sovereignty over creation, history, and all rival deities. Draws heavily on
    Deut 7:6 (segullah, treasured possession, v4), Exod 34:10 (wonders, v9),
    and Ps 115:4–7 (the idol polemic, vv15–17 here). The bookending Hallelujah
    (vv1, 21) frames the entire psalm as congregational praise.

Ps 136 (26 v) — The Great Hallel. Every verse carries the antiphonal refrain
    "ki le'olam chasdo" (for his steadfast love endures forever). The psalm
    moves through three movements: creation (vv1–9) → exodus and conquest
    (vv10–22) → present praise of the universal provider (vv23–26). The 26-fold
    repetition of H2617 (chesed) makes this the defining text for that term in
    the Psalter. Sung as the Great Hallel at Passover (cf. Matt 26:30). The
    refrain is liturgically fixed; all three tiers preserve it verbatim so the
    antiphonal cadence is undisturbed.

Ps 137 (9 v) — By the Rivers of Babylon. An exile lament and imprecation from
    the Babylonian captivity. The psalm is unified by the tension of memory (Zion
    recalled, v1) and demand (the captors' mockery, v3), resolved by a fierce
    oath of loyalty (vv5–6) and an even fiercer call for justice against Edom
    and Babylon (vv7–9). The final imprecation (v9) is one of the hardest verses
    in Scripture. All three tiers render it without softening: this is the raw
    prayer of people who saw Babylon do the same to their own infants. The T tier
    does not add a disclaimer; the horror of the line is its meaning.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in all tiers throughout. Consistent with all prior
    Psalms scripts.

H430 (אֱלֹהִים, Elohim): "God" in all tiers — standard.

H2617 (חֶסֶד, chesed): "steadfast love" in all three tiers in Psalm 136 refrain.
    This is the defining text for chesed and the rendering cannot waver. The
    KJV "mercy" understates the covenantal dimension. "Steadfast love" (following
    RSV/ESV tradition) carries both the relational loyalty and the active kindness.
    Consistent with prior Psalms scripts.

H7272 (רֶגֶל, regel) at Ps 132:7: "footstool" — the ark of the covenant is the
    literal footstool of the divine throne (cf. 1 Chr 28:2; Isa 66:1). L/M/T all
    use "footstool" to keep the throne-room imagery.

H7161 (קֶרֶן, qeren, horn) at Ps 132:17: "horn" in L/T; "shoot of strength" in
    M to clarify the idiom. The horn = concentrated power, virile strength, the
    messianic scion. "Make the horn to bud" = cause a new growth of Davidic
    strength to sprout (the same verb צָמַח as in Zechariah's Branch oracles).

H5220 (נֵר, ner, lamp) at Ps 132:17: "lamp" in all tiers — the dynastic lamp that
    the LORD refused to extinguish for David's sake (1 Kgs 11:36; 2 Kgs 8:19).

H5459 (סְגֻלָּה, segullah) at Ps 135:4: "treasured possession" in L/M/T —
    the covenant-election term from Deut 7:6; 14:2; 26:18. "Peculiar treasure"
    (KJV) and "special possession" are alternatives but "treasured possession"
    is more precise.

H6041 (עָנִי, ani, poor/afflicted) at Ps 132:15: "poor" in L/M; "the poor" in T.
    The material referent is primary here — actual destitute people in Jerusalem,
    not a spiritualised category.

H4325 (מַיִם, mayim) + H5488 (סוּף, suph) = yam suph at Ps 136:13,15:
    Literally "Sea of Reeds" — "Red Sea" is the traditional English rendering
    established from the LXX (ἐρυθρὰ θάλασσα). L/T use "Sea of Reeds"
    (more accurate); M uses "Red Sea" (established English).

H376/H120 (אִישׁ/אָדָם, man/human) at Ps 135:8: "human" in L/M/T — inclusive.

H2617 (chesed) at Ps 136: The refrain "ki le'olam chasdo" is rendered uniformly
    as "for his steadfast love endures forever" across all 26 occurrences in
    all three tiers. No variation, since this is liturgical repetition.

=== OT intertextuality and NT connections ===

Ps 132:8 — "Arise, O LORD, to your resting place" quotes the formula from
    Num 10:35–36 (used when the ark set out / came to rest). 2 Chr 6:41–42
    quotes this psalm nearly verbatim. The ark = the presence of God moving.

Ps 132:11–12 — The Davidic covenant oath echoes 2 Sam 7:12–16 (Nathan's oracle)
    in poetic form. The conditionality in v12 is the Ps 89 tension: the promise
    is unconditional for the dynasty but conditional for individual kings.

Ps 132:17 — "Make the horn to bud" uses the צָמַח (tzemach) root that becomes
    the technical Messianic "Branch" term (Jer 23:5; 33:15; Zech 3:8; 6:12).
    Luke 1:69 ("a horn of salvation in the house of David") quotes this directly.

Ps 133:1 — "How good and pleasant for brothers to dwell in unity" is applied
    communally in NT contexts (Acts 2:44–46 — the early church as this unity).
    John 17:21 (that they may all be one) is its ultimate Johannine expression.

Ps 134:3 — The blessing closes with the same formula as Ps 121:2 ("the LORD
    who made heaven and earth"), tying the final Ascent back to the first travel
    psalm. The Creator is the ultimate blesser.

Ps 135:14 — "The LORD will vindicate his people" quotes Deut 32:36 verbatim.

Ps 135:15–17 — The idol polemic is quoted or echoed at Rom 1:23 (exchanged the
    glory of God for images) and the underlying logic of 1 Cor 12:2.

Ps 136:1 — "Give thanks to the LORD, for he is good" is quoted at 1 Chr 16:34;
    2 Chr 5:13; 7:3; Ezra 3:11; Jer 33:11; and is the origin of the common
    congregational response. Jesus and the disciples sang "a hymn" (Matt 26:30;
    Mark 14:26) at the Last Supper — traditionally Ps 136 as the Great Hallel.

Ps 137:8–9 — The Babylon imprecation: "Daughter of Babylon" is echoed at
    Isa 47:1–15 (the taunt of Babylon). Rev 18 ("Babylon the Great is fallen")
    draws on this entire complex of exile lament and divine vengeance. The
    "little ones dashed against rocks" is mirrored in Isa 13:16,18 as part of
    Babylon's own judgment.

=== Aspect and tense notes ===

Ps 132:1–10: The Hebrew perfects in vv2–5 (he swore, he vowed) report David's
    past oath as reported speech. The imperatives in vv8–10 (Arise, let your
    priests be clothed) are the prayer for the ark's installation.

Ps 132:11–18: Divine oracle in v11 opens with Hebrew perfect ("the LORD swore")
    — the oath is already completed and binding. The conditional imperfects in
    v12 ("if your sons will keep") are the succession clause. The imperfects of
    vv14–18 are the LORD's own declarations of settled purpose ("I will").

Ps 133:3: "There the LORD commanded (tzivvah, perfect) the blessing" — aorist-
    style completed act; the command stands. Rendered as present-ongoing in M/T
    (the commanded blessing remains in force wherever unity exists).

Ps 136: All declarative statements are participial or finite imperfect, implying
    ongoing or characteristic action. The refrain is nominal: "his chesed
    [endures] to the age." No finite verb in the Hebrew refrain — the endurance
    is simply asserted as fact. "Endures" added in English for idiom.

Ps 137:1–6: Hebrew perfects throughout (we sat, we wept, we hung). These are
    specific past events rendered as completed past. The vow in vv5–6 uses
    jussive/imperfect: "let my right hand forget / let my tongue cling."

Ps 137:7: Imperative directed at the LORD ("Remember, O LORD") — urgent petition.

Ps 137:8–9: The beatitude form "Blessed/happy is the one who..." (אַשְׁרֵי, ashrei)
    is the same form as Ps 1:1. All tiers preserve this formal echo: these are
    not curses from the psalmist but beatitudes pronounced on the avenger of
    Zion's suffering, placed in God's hands.
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
  # Psalm 132 — The Davidic Covenant and the Election of Zion
  # Royal psalm; David's oath for the ark; God's answering oath; horn of David
  # ===========================================================================
  "132": {
    "1": {
      "L": "A Song of Ascents. O LORD, remember David and all his afflictions,",
      "M": "A Song of Ascents. O LORD, remember David — remember all his hardships,",
      "T": "A Song of Ascents.\nO LORD, remember David —\nremember all his hardships;"
    },
    "2": {
      "L": "how he swore to the LORD and vowed to the Mighty One of Jacob:",
      "M": "how he made a solemn oath to the LORD and vowed to the Mighty One of Jacob:",
      "T": "how he swore to the LORD —\nvowed to the Mighty One of Jacob:"
    },
    "3": {
      "L": "'I will not enter the tent of my house, nor go up into the bed I lie on;'",
      "M": "'I will not enter my house, nor climb into my bed;'",
      "T": "'I will not go to my house —\nnor climb into my bed;'"
    },
    "4": {
      "L": "'I will not give sleep to my eyes or slumber to my eyelids,'",
      "M": "'I will allow no sleep to my eyes, no slumber to my eyelids,'",
      "T": "'I will give no sleep to my eyes,\nno slumber to my eyelids,'"
    },
    "5": {
      "L": "'until I find a place for the LORD, a dwelling for the Mighty One of Jacob.'",
      "M": "'until I find a fitting place for the LORD — a dwelling for the Mighty One of Jacob.'",
      "T": "'until I find a place for the LORD —\na dwelling\nfor the Mighty One of Jacob.'"
    },
    "6": {
      "L": "Behold, we heard of it in Ephrathah; we found it in the fields of Jaar.",
      "M": "We heard of the ark at Ephrathah; we discovered it in the fields of Jaar.",
      "T": "We heard of the ark in Ephrathah —\nwe found it\nin the fields of Jaar."
    },
    "7": {
      "L": "Let us go to his dwelling place; let us worship at his footstool.",
      "M": "Let us go to his dwelling place; let us bow down at his footstool.",
      "T": "Let us go to his dwelling —\nlet us bow down\nat his footstool."
    },
    "8": {
      "L": "Arise, O LORD, to your resting place — you and the ark of your might.",
      "M": "Rise up, O LORD, to your resting place — you and the ark that holds your power.",
      "T": "Arise, O LORD, to your resting place —\nyou, and the ark\nof your strength."
    },
    "9": {
      "L": "Let your priests be clothed with righteousness, and let your faithful ones shout for joy.",
      "M": "Clothe your priests with righteousness, and let your devoted people shout for joy.",
      "T": "Clothe your priests in righteousness —\nlet your faithful ones\nshout for joy."
    },
    "10": {
      "L": "For the sake of your servant David, do not turn away the face of your anointed one.",
      "M": "For your servant David's sake, do not reject your anointed king.",
      "T": "For your servant David's sake —\ndo not turn away\nthe face of your anointed."
    },
    "11": {
      "L": "The LORD swore to David in truth — he will not turn back from it: 'Of the fruit of your body I will set one upon your throne.'",
      "M": "The LORD made a sworn, true covenant with David — he will never go back on it: 'I will place one of your own descendants upon your throne.'",
      "T": "The LORD swore in truth to David —\nan oath he will not retract:\n'From the fruit of your body I will set one upon your throne.'"
    },
    "12": {
      "L": "'If your sons keep my covenant and my testimonies that I shall teach them, their sons also shall sit upon your throne forever.'",
      "M": "'If your sons keep my covenant and the decrees I teach them, their sons too shall sit upon your throne forever.'",
      "T": "'If your sons keep my covenant —\nthe testimonies I will teach them —\nthen their sons will sit on your throne forever.'"
    },
    "13": {
      "L": "For the LORD has chosen Zion; he has desired it for his dwelling place.",
      "M": "The LORD has chosen Zion; he has made it his desired home.",
      "T": "For the LORD has chosen Zion —\nhe has desired it\nfor his dwelling."
    },
    "14": {
      "L": "'This is my resting place forever; here I will dwell, for I have desired it.'",
      "M": "'This is my resting place forever; here I will live, for I have longed for it.'",
      "T": "'This is my rest forever —\nhere I will dwell,\nfor I have desired it.'"
    },
    "15": {
      "L": "'I will abundantly bless her provisions; I will satisfy her poor with bread.'",
      "M": "'I will richly bless her food supply; I will fill the poor with bread.'",
      "T": "'I will bless her provisions abundantly —\nI will satisfy the poor\nwith bread.'"
    },
    "16": {
      "L": "'I will clothe her priests with salvation, and her faithful ones shall shout aloud for joy.'",
      "M": "'I will dress her priests with salvation, and her devoted people will shout with joy.'",
      "T": "'I will clothe her priests with salvation —\nher faithful ones\nwill shout aloud for joy.'"
    },
    "17": {
      "L": "'There I will cause a horn to bud for David; I have prepared a lamp for my anointed.'",
      "M": "'There I will make a shoot of strength grow for David; I have set a lamp ready for my anointed.'",
      "T": "'There I will make the horn of David to bud —\nI have ordained a lamp\nfor my anointed.'"
    },
    "18": {
      "L": "'His enemies I will clothe with shame, but upon him his crown will shine.'",
      "M": "'I will dress his enemies in shame, but his crown will gleam upon his head.'",
      "T": "'His enemies I will clothe in shame —\nbut upon his own head\nhis crown will flourish.'"
    }
  },

  # ===========================================================================
  # Psalm 133 — The Blessing of Unity
  # Fraternal unity; priestly oil; dew of Hermon; commanded life
  # ===========================================================================
  "133": {
    "1": {
      "L": "A Song of Ascents. Of David. Behold, how good and how pleasant it is when brothers dwell together in unity!",
      "M": "A Song of Ascents. Of David. How wonderfully good it is, how delightful, when brothers live together as one!",
      "T": "A Song of Ascents. Of David.\nBehold — how good, how pleasant,\nwhen brothers dwell together in unity!"
    },
    "2": {
      "L": "It is like the precious oil upon the head, running down upon the beard, the beard of Aaron, running down to the collar of his garments!",
      "M": "It is like costly anointing oil poured on the head, running down over the beard — Aaron's beard — flowing all the way down to the edge of his robes!",
      "T": "It is like the precious anointing oil\npoured on the head, running down\nupon the beard — Aaron's beard —\nflowing all the way to the hem of his robes."
    },
    "3": {
      "L": "It is like the dew of Hermon, like dew falling on the mountains of Zion, for there the LORD commanded the blessing — life forevermore.",
      "M": "It is like the dew of Hermon descending on the mountains of Zion — for there the LORD has commanded the blessing: life that lasts forever.",
      "T": "It is like the dew of Hermon\nfalling on the mountains of Zion —\nfor there the LORD commands the blessing:\nlife for evermore."
    }
  },

  # ===========================================================================
  # Psalm 134 — Night Liturgy at the Close of the Ascents
  # Call to night-watch priests; mutual blessing; Creator blesses from Zion
  # ===========================================================================
  "134": {
    "1": {
      "L": "A Song of Ascents. Come, bless the LORD, all you servants of the LORD, who stand in the house of the LORD by night.",
      "M": "A Song of Ascents. Come, bless the LORD, all you servants of the LORD who stand watch in his house through the night.",
      "T": "A Song of Ascents.\nCome — bless the LORD,\nall you servants of the LORD\nwho stand by night in his house."
    },
    "2": {
      "L": "Lift up your hands toward the holy place and bless the LORD.",
      "M": "Raise your hands toward the sanctuary and bless the LORD.",
      "T": "Lift your hands toward the sanctuary —\nbless\nthe LORD."
    },
    "3": {
      "L": "May the LORD, who made heaven and earth, bless you from Zion.",
      "M": "May the LORD, maker of heaven and earth, bless you from Zion.",
      "T": "May the LORD bless you from Zion —\nthe LORD who made\nheaven and earth."
    }
  },

  # ===========================================================================
  # Psalm 135 — Hallelujah: The LORD Above All Gods
  # Sovereignty over creation and history; idol polemic; doxology from Zion
  # ===========================================================================
  "135": {
    "1": {
      "L": "Praise the LORD! Praise the name of the LORD; praise him, O you servants of the LORD,",
      "M": "Praise the LORD! Praise the name of the LORD; praise him, all you servants of the LORD,",
      "T": "Praise the LORD!\nPraise the name of the LORD —\npraise him, O servants of the LORD,"
    },
    "2": {
      "L": "you who stand in the house of the LORD, in the courts of the house of our God.",
      "M": "you who stand in the LORD's house and serve in the courts of our God.",
      "T": "you who stand in the house of the LORD,\nin the courts\nof the house of our God."
    },
    "3": {
      "L": "Praise the LORD, for the LORD is good; sing praises to his name, for it is pleasant.",
      "M": "Praise the LORD, for the LORD is good; sing praises to his name — it is a delight.",
      "T": "Praise the LORD — for the LORD is good;\nsing praises to his name,\nfor it is pleasant."
    },
    "4": {
      "L": "For the LORD has chosen Jacob for himself, Israel as his treasured possession.",
      "M": "For the LORD chose Jacob as his own, Israel as his prized and treasured possession.",
      "T": "For the LORD has chosen Jacob for himself —\nIsrael\nas his treasured possession."
    },
    "5": {
      "L": "For I know that the LORD is great, and that our Lord is above all gods.",
      "M": "I know that the LORD is great — our Lord stands above every so-called god.",
      "T": "I know that the LORD is great —\nour Lord\nabove all gods."
    },
    "6": {
      "L": "Whatever the LORD pleases, he does — in heaven and on earth, in the seas and all their depths.",
      "M": "The LORD does whatever he pleases — in heaven and on earth, in the seas and every depth.",
      "T": "Whatever the LORD pleases, he does —\nin heaven, on earth,\nin the seas and all their depths."
    },
    "7": {
      "L": "He causes the clouds to rise from the ends of the earth; he makes lightning for the rain; he brings out the wind from his storehouses.",
      "M": "He draws up clouds from the far ends of the earth, makes lightning flash with the rain, and releases the wind from his storehouses.",
      "T": "He draws clouds up from the ends of the earth —\nmakes lightning flash with rain,\nbrings the wind from his storehouses."
    },
    "8": {
      "L": "He struck down the firstborn of Egypt — both human and beast.",
      "M": "He struck down the firstborn of Egypt — both people and animals alike.",
      "T": "He struck down Egypt's firstborn —\nboth people\nand animals."
    },
    "9": {
      "L": "He sent signs and wonders into your midst, O Egypt — against Pharaoh and all his servants.",
      "M": "He sent miraculous signs and wonders into Egypt — striking Pharaoh and all his servants.",
      "T": "He sent signs and wonders into your midst, O Egypt —\nagainst Pharaoh\nand all his servants."
    },
    "10": {
      "L": "He struck down many nations and slew powerful kings —",
      "M": "He defeated great nations and put mighty kings to death —",
      "T": "He struck down great nations,\nslew powerful kings —"
    },
    "11": {
      "L": "Sihon, king of the Amorites, and Og, king of Bashan, and all the kingdoms of Canaan —",
      "M": "Sihon king of the Amorites, Og king of Bashan, and all the kingdoms of Canaan —",
      "T": "Sihon, king of the Amorites;\nOg, king of Bashan;\nand all the kingdoms of Canaan —"
    },
    "12": {
      "L": "and gave their land as an inheritance, an inheritance to Israel his people.",
      "M": "and gave their land as an inheritance — an inheritance to his people Israel.",
      "T": "and gave their land as an inheritance —\nan inheritance\nfor Israel his people."
    },
    "13": {
      "L": "Your name, O LORD, endures forever; your renown, O LORD, throughout all generations.",
      "M": "O LORD, your name endures forever; your memory is kept alive through every generation.",
      "T": "O LORD, your name endures forever —\nyour memorial\nthrough all generations."
    },
    "14": {
      "L": "For the LORD will vindicate his people and will have compassion on his servants.",
      "M": "The LORD will uphold the cause of his people and will show compassion toward his servants.",
      "T": "For the LORD will vindicate his people —\nhe will have compassion\non his servants."
    },
    "15": {
      "L": "The idols of the nations are silver and gold, the work of human hands.",
      "M": "The idols of the nations are silver and gold — nothing but the work of human hands.",
      "T": "The idols of the nations are silver and gold —\nthe work\nof human hands."
    },
    "16": {
      "L": "They have mouths but cannot speak; they have eyes but cannot see;",
      "M": "They have mouths, but they cannot speak; they have eyes, but they cannot see;",
      "T": "Mouths — but they cannot speak;\neyes — but they cannot see;"
    },
    "17": {
      "L": "they have ears but cannot hear; there is no breath at all in their mouths.",
      "M": "they have ears but cannot hear; there is not a breath of air in their mouths.",
      "T": "ears — but they cannot hear;\nno breath at all\nin their mouths."
    },
    "18": {
      "L": "Those who make them become like them; so does everyone who trusts in them.",
      "M": "Those who make them will become like them — and so will all who put their trust in them.",
      "T": "Those who make them will become like them —\nso will everyone\nwho puts their trust in them."
    },
    "19": {
      "L": "Bless the LORD, O house of Israel! Bless the LORD, O house of Aaron!",
      "M": "Praise the LORD, O house of Israel! Praise the LORD, O house of Aaron!",
      "T": "Bless the LORD, O house of Israel!\nBless the LORD,\nO house of Aaron!"
    },
    "20": {
      "L": "Bless the LORD, O house of Levi! You who fear the LORD, bless the LORD!",
      "M": "Praise the LORD, O house of Levi! All who fear the LORD, praise the LORD!",
      "T": "Bless the LORD, O house of Levi!\nYou who fear the LORD —\nbless the LORD!"
    },
    "21": {
      "L": "Blessed be the LORD from Zion, he who dwells in Jerusalem. Praise the LORD!",
      "M": "Praise be to the LORD from Zion — he who makes his home in Jerusalem. Praise the LORD!",
      "T": "Blessed be the LORD from Zion —\nhe who dwells\nin Jerusalem. Praise the LORD!"
    }
  },

  # ===========================================================================
  # Psalm 136 — The Great Hallel
  # 26-verse antiphonal psalm; chesed refrain; creation → exodus → conquest → present
  # ===========================================================================
  "136": {
    "1": {
      "L": "Give thanks to the LORD, for he is good — for his steadfast love endures forever.",
      "M": "Give thanks to the LORD, for he is good — for his steadfast love endures forever.",
      "T": "Give thanks to the LORD, for he is good —\nfor his steadfast love endures forever."
    },
    "2": {
      "L": "Give thanks to the God of gods — for his steadfast love endures forever.",
      "M": "Give thanks to the God above all gods — for his steadfast love endures forever.",
      "T": "Give thanks to the God of gods —\nfor his steadfast love endures forever."
    },
    "3": {
      "L": "Give thanks to the Lord of lords — for his steadfast love endures forever.",
      "M": "Give thanks to the Lord who reigns above all lords — for his steadfast love endures forever.",
      "T": "Give thanks to the Lord of lords —\nfor his steadfast love endures forever."
    },
    "4": {
      "L": "To him who alone does great wonders — for his steadfast love endures forever.",
      "M": "To him who alone performs great wonders — for his steadfast love endures forever.",
      "T": "To him who alone works great wonders —\nfor his steadfast love endures forever."
    },
    "5": {
      "L": "To him who made the heavens by wisdom — for his steadfast love endures forever.",
      "M": "To him who made the heavens with wisdom — for his steadfast love endures forever.",
      "T": "To him who crafted the heavens by wisdom —\nfor his steadfast love endures forever."
    },
    "6": {
      "L": "To him who spread out the earth upon the waters — for his steadfast love endures forever.",
      "M": "To him who laid the earth out over the waters — for his steadfast love endures forever.",
      "T": "To him who stretched the earth over the waters —\nfor his steadfast love endures forever."
    },
    "7": {
      "L": "To him who made the great lights — for his steadfast love endures forever.",
      "M": "To him who made the great lights — for his steadfast love endures forever.",
      "T": "To him who made the great lights —\nfor his steadfast love endures forever."
    },
    "8": {
      "L": "The sun to rule the day — for his steadfast love endures forever.",
      "M": "The sun to govern the day — for his steadfast love endures forever.",
      "T": "The sun to govern the day —\nfor his steadfast love endures forever."
    },
    "9": {
      "L": "The moon and stars to rule the night — for his steadfast love endures forever.",
      "M": "The moon and stars to govern the night — for his steadfast love endures forever.",
      "T": "Moon and stars to govern the night —\nfor his steadfast love endures forever."
    },
    "10": {
      "L": "To him who struck Egypt through their firstborn — for his steadfast love endures forever.",
      "M": "To him who struck down Egypt by killing their firstborn — for his steadfast love endures forever.",
      "T": "To him who struck Egypt through their firstborn —\nfor his steadfast love endures forever."
    },
    "11": {
      "L": "And brought Israel out from among them — for his steadfast love endures forever.",
      "M": "Who led Israel out from among them — for his steadfast love endures forever.",
      "T": "Who led Israel out from their midst —\nfor his steadfast love endures forever."
    },
    "12": {
      "L": "With a strong hand and an outstretched arm — for his steadfast love endures forever.",
      "M": "With a powerful hand and an arm stretched wide — for his steadfast love endures forever.",
      "T": "With a strong hand, with an outstretched arm —\nfor his steadfast love endures forever."
    },
    "13": {
      "L": "To him who divided the Sea of Reeds in two — for his steadfast love endures forever.",
      "M": "To him who split the Red Sea apart — for his steadfast love endures forever.",
      "T": "To him who split the Sea of Reeds —\nfor his steadfast love endures forever."
    },
    "14": {
      "L": "And made Israel pass through the midst of it — for his steadfast love endures forever.",
      "M": "Who led Israel safely through its midst — for his steadfast love endures forever.",
      "T": "Who led Israel through the midst of it —\nfor his steadfast love endures forever."
    },
    "15": {
      "L": "And swept Pharaoh and his army into the Sea of Reeds — for his steadfast love endures forever.",
      "M": "And swept Pharaoh and his army into the Red Sea — for his steadfast love endures forever.",
      "T": "And swept Pharaoh and his army into the Sea —\nfor his steadfast love endures forever."
    },
    "16": {
      "L": "To him who led his people through the wilderness — for his steadfast love endures forever.",
      "M": "To him who guided his people through the desert — for his steadfast love endures forever.",
      "T": "To him who led his people through the wilderness —\nfor his steadfast love endures forever."
    },
    "17": {
      "L": "To him who struck down great kings — for his steadfast love endures forever.",
      "M": "To him who defeated great kings — for his steadfast love endures forever.",
      "T": "To him who struck down great kings —\nfor his steadfast love endures forever."
    },
    "18": {
      "L": "And killed renowned kings — for his steadfast love endures forever.",
      "M": "Who slew renowned kings — for his steadfast love endures forever.",
      "T": "Who slew renowned kings —\nfor his steadfast love endures forever."
    },
    "19": {
      "L": "Sihon, king of the Amorites — for his steadfast love endures forever.",
      "M": "Sihon, king of the Amorites — for his steadfast love endures forever.",
      "T": "Sihon, king of the Amorites —\nfor his steadfast love endures forever."
    },
    "20": {
      "L": "And Og, king of Bashan — for his steadfast love endures forever.",
      "M": "And Og, king of Bashan — for his steadfast love endures forever.",
      "T": "Og, king of Bashan —\nfor his steadfast love endures forever."
    },
    "21": {
      "L": "And gave their land as an inheritance — for his steadfast love endures forever.",
      "M": "Who gave their land as an inheritance — for his steadfast love endures forever.",
      "T": "Who gave their land as an inheritance —\nfor his steadfast love endures forever."
    },
    "22": {
      "L": "An inheritance to Israel his servant — for his steadfast love endures forever.",
      "M": "An inheritance given to Israel his servant — for his steadfast love endures forever.",
      "T": "An inheritance to Israel, his servant —\nfor his steadfast love endures forever."
    },
    "23": {
      "L": "Who remembered us in our low estate — for his steadfast love endures forever.",
      "M": "Who remembered us when we were brought low — for his steadfast love endures forever.",
      "T": "Who remembered us in our humiliation —\nfor his steadfast love endures forever."
    },
    "24": {
      "L": "And rescued us from our enemies — for his steadfast love endures forever.",
      "M": "And delivered us from our enemies — for his steadfast love endures forever.",
      "T": "Who tore us free from our enemies —\nfor his steadfast love endures forever."
    },
    "25": {
      "L": "Who gives food to all creatures — for his steadfast love endures forever.",
      "M": "Who provides food for every living thing — for his steadfast love endures forever.",
      "T": "Who gives food to all flesh —\nfor his steadfast love endures forever."
    },
    "26": {
      "L": "Give thanks to the God of heaven — for his steadfast love endures forever.",
      "M": "Give thanks to the God of heaven — for his steadfast love endures forever.",
      "T": "Give thanks to the God of heaven —\nfor his steadfast love endures forever."
    }
  },

  # ===========================================================================
  # Psalm 137 — By the Rivers of Babylon
  # Exile lament; oath of loyalty to Jerusalem; imprecation against Edom and Babylon
  # ===========================================================================
  "137": {
    "1": {
      "L": "By the rivers of Babylon — there we sat down; yes, we wept when we remembered Zion.",
      "M": "By the rivers of Babylon we sat down and wept when we remembered Zion.",
      "T": "By the rivers of Babylon —\nthere we sat down and wept,\nwhen we remembered Zion."
    },
    "2": {
      "L": "We hung our harps on the willows in the midst of that land.",
      "M": "We hung up our harps in the willow trees there.",
      "T": "We hung our harps\nupon the willows\nin the midst of that place."
    },
    "3": {
      "L": "For there our captors demanded of us songs, and those who had devastated us demanded gladness, saying, 'Sing us one of the songs of Zion!'",
      "M": "Our captors demanded that we sing for them; those who had ruined us wanted entertainment: 'Sing us a song of Zion!'",
      "T": "There our captors demanded songs from us —\nthose who had ravaged us demanded joy:\n'Sing us one of the songs of Zion!'"
    },
    "4": {
      "L": "How shall we sing the LORD's song in a foreign land?",
      "M": "But how could we sing the LORD's song in a foreign land?",
      "T": "How can we sing the LORD's song\nin a foreign land?"
    },
    "5": {
      "L": "If I forget you, O Jerusalem, let my right hand wither.",
      "M": "If I forget you, O Jerusalem, may my right hand lose all skill.",
      "T": "If I forget you, O Jerusalem —\nlet my right hand\nwither."
    },
    "6": {
      "L": "If I do not remember you, let my tongue cling to the roof of my mouth, if I do not set Jerusalem above my highest joy.",
      "M": "If I do not hold you in memory, may my tongue stick to the roof of my mouth — if I do not place Jerusalem above my greatest delight.",
      "T": "If I do not remember you —\nlet my tongue cling to the roof of my mouth —\nif I do not hold Jerusalem above my highest joy."
    },
    "7": {
      "L": "Remember, O LORD, against the Edomites the day of Jerusalem — how they said, 'Tear it down, tear it down, right down to its foundations!'",
      "M": "Remember, O LORD, what Edom's sons did on the day Jerusalem fell — how they shouted, 'Tear it down! Tear it down to its very foundations!'",
      "T": "Remember, O LORD, against Edom\nthe day Jerusalem fell —\nhow they cried: 'Tear it down! Tear it down\nto its very foundations!'"
    },
    "8": {
      "L": "O daughter of Babylon, doomed to be destroyed — blessed is he who repays you what you have done to us!",
      "M": "O Babylon, marked for destruction — how happy will be the one who pays you back for what you did to us!",
      "T": "O daughter of Babylon, destined for ruin —\nhappy the one\nwho repays you as you treated us!"
    },
    "9": {
      "L": "Blessed is he who seizes and dashes your infants against the rock.",
      "M": "Blessed is he who takes your little ones and smashes them against the rocks.",
      "T": "Blessed shall he be who seizes your children\nand dashes them\nagainst the rock."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 132–137 written.')

if __name__ == '__main__':
    main()
