"""
MKT Psalms chapters 67–69 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-67-69.py

=== Overview of this unit ===

Ps 67 (7 v) — A harvest blessing psalm with a missional horizon. The opening prayer
    echoes the Aaronic blessing of Numbers 6:24–26 ("The LORD bless you and keep you;
    the LORD make his face shine upon you..."). The psalm's theological logic: God's
    blessing of Israel is not an end in itself but a means by which "your way may be
    known upon earth" — a missional purpose clause driving the entire poem. The repeated
    refrain (vv3, 5) "Let the peoples praise you, O God; let all the peoples praise you"
    is the psalm's heartbeat: universal worship is the goal. v4 grounds this in a vision
    of divine governance — God will judge the peoples with equity (H4334 mishor = fairness/
    uprightness), a positive prospect, not threat. The harvest in v6 ("the earth has
    yielded its increase") confirms that the blessing has already begun, feeding the
    momentum toward the eschatological universalism of v7. Psalm 67 is the doxological
    hinge between the Elohistic Psalter's laments (Pss 42–66) and the beginning of what
    follows.

Ps 68 (35 v) — The great processional-victory psalm; one of the most theologically
    complex in the Psalter. Its opening (v1) is a direct citation of Numbers 10:35
    ("Arise, O LORD, and let your enemies be scattered"), anchoring the psalm in the
    wilderness march. The epithets build rapidly: God as cloud-rider / storm-rider (v4,
    v33 — a divine-warrior title also used of Baal in Ugaritic texts, making the
    designation polemically exclusive), Father of the fatherless and defender of widows
    (v5 — an explicit patron-client / honor-shame social claim), liberator of prisoners
    (v6), marching wilderness God who makes Sinai tremble (vv7–8). The victory herald
    of v11 is the feminine plural participle מְבַשְּׂרוֹת (mevassarot) — women who carry
    victory news, anticipating the role of women at the empty tomb. v13 contains the
    difficult sheepfold/cooking-pot image (H8240 shephattayim): Israel lying in servile
    ash but emerging gleaming like a silver-and-gold dove. vv15–16 address the mountains
    of Bashan with mock-envy: this small hill, Zion, is the one God chose. v17 pictures
    the divine chariot-host: "twenty thousand, even thousands of angels" — the divine
    warrior's army is innumerable.

    KEY — v18 and Ephesians 4:8: The Hebrew reads "you have received gifts from men"
    (tribute taken from conquered peoples — the pattern of an ancient Near Eastern king
    ascending after victory). Paul's citation in Eph 4:8 reads "he gave gifts to men" —
    a typological midrash applying the ascending Christ's gift-giving to the church. The
    Psalms translation follows the Hebrew original in all three tiers ("received gifts");
    the Eph 4:8 echo is documented here, not embedded in the text.

    v22 announces the divine reversal: from Bashan to the depths of the sea, no extreme
    is beyond God's reach. The processional description (vv24–25) includes women with
    timbrels. The assembly lists tribal leaders (v27 — "little Benjamin" leading, recalling
    Benjamin as the youngest, the patron tribe of Saul and Paul). v31 reaches its
    universalist climax: princes from Egypt, Ethiopia stretching out her hands to God.
    The psalm ends with three verses of doxology (vv33–35).

Ps 69 (36 v) — One of the most frequently cited psalms in the NT. Its lament imagery
    (drowning in waters, mire, floods — vv1–3, 14–15) is the classic chaos/death motif.
    The psalm is unusual in explicitly confessing the psalmist's own sin (v5), then
    expressing concern that his suffering not discredit those who trust God (v6).
    The NT citations from this psalm:

    - v4b ("hated me without a cause") — John 15:25, applied to Jesus
    - v9a ("zeal for your house has eaten me up") — John 2:17, cleansing of the temple
    - v9b ("reproaches of those who reproach you have fallen on me") — Romans 15:3
    - v21 (gall and vinegar) — all four passion narratives (Matt 27:34,48; Mark 15:36;
      Luke 23:36; John 19:28–30) — the soldiers' offer to Jesus on the cross
    - vv22–23 (table as snare; darkened eyes) — Romans 11:9–10, applied to Israel's
      hardening
    - v25 ("let their habitation be desolate") — Acts 1:20, applied to Judas

    The imprecatory section (vv22–28) is among the most intense in the Psalter. It is
    rendered faithfully — imprecation is part of the full range of covenant prayer. The
    turn in v29 ("But I am poor and sorrowful") is one of the Psalter's great pivots:
    from imprecation to praise, grounded in the certainty of divine hearing (vv31–33).
    The psalm ends with an eschatological horizon: God rebuilding Zion and its cities,
    the servants' children inheriting (vv35–36).

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps) in L/M throughout. In T: "the LORD" or "LORD"
    per cadence. Consistent with all prior Psalms scripts.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. We are still within Book II of the
    Elohistic Psalter (Ps 42–89), which systematically prefers Elohim.

H410 (אֵל, El): "God" in all tiers. Shorter divine title.

H136 (אֲדֹנָי, Adonai): "the Lord" (capitalized Lord, not LORD) in all tiers.
    The sovereign title, distinct from the personal name Yahweh. Appears at Ps 68:11,
    17, 19, 20; Ps 69:6.

H3050 (יָהּ, Yah): The short form of the divine name, appearing in Ps 68:4 ("JAH").
    Rendered "Yah" in L (transliteration, the correct short form); "the LORD" in M/T,
    since "Yah" without explanation would confuse most readers.

H2617 (חֶסֶד, chesed): "steadfast love" in L/M throughout. In T: "steadfast love"
    or contextually "love" when the surrounding phrase already conveys covenant loyalty.
    Appears prominently at Ps 69:13, 16. Consistent with all prior Psalms scripts.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M. In T: "soul," "life," or "throat" (the
    literal neck/throat meaning suits Ps 69:1 — "waters have come in to my soul/throat").
    Rendered "throat" in T at 69:1 to surface the physical-drowning image. "Soul" in
    L/M at 69:1 per the established gloss.

H7307 (רוּחַ, ruach): Does not appear as Spirit/wind in a contested theological sense
    in Pss 67–69. Not a focus in this unit.

H5058 (נְגִינָה, neginah / Neginoth): Musical heading for Ps 67. "Neginoth" in L
    (the traditional transliteration); "stringed instruments" in M/T. Consistent with
    prior Psalms scripts.

H8420 (שׁוֹשַׁן, shoshan / Shoshannim): Melody title for Ps 69 ("upon Shoshannim").
    "Shoshannim" in L; "The Lilies" in M/T (lilies = the melody name or song-type).
    Also appears in Ps 45 and 80 superscriptions.

H5542 (סֶלָה, Selah): Retained as "Selah" in all tiers throughout. Appears at Ps 67:1,4;
    Ps 68:7,19,32.

H1319 (בָּשַׂר, basar): The feminine plural participle in Ps 68:11 (מְבַשְּׂרוֹת,
    mevassarot) = women who bring good news / herald victory. Rendered "women heralds"
    in L, "women who announced the victory" in M/T. This is the same root as NT
    εὐαγγελίζω (evangelizō = to announce good news / gospel).

H8240 (שְׁפַתַּיִם, shephattayim) at Ps 68:13: Two interpretations exist — "sheepfolds"
    (ESV, NASB, following the image of Israel as livestock staying among the pens) or
    "cooking pots" (KJV, following a Targum variant), implying servile, sooty work.
    Either image = lowly condition before exaltation. Rendered "the sheepfolds" in L/M;
    "the dust and the ash" in T (capturing the lowness without forcing either specific
    image, since the Hebrew's exact referent is uncertain).

H3050+H3678 at Ps 68:4 ("rideth upon the heavens"): The cloud-/storm-rider epithet
    of the divine warrior. Used of Baal in Ugaritic literature (rkb 'rpt); its
    application to YHWH is a polemical claim. Rendered literally in L/M ("rides upon
    the heavens"); in T the storm-cloud background is surfaced.

Ps 68:18 and Eph 4:8: Hebrew "you have received gifts from men" (tribute of a
    conquering king ascending in victory); Paul's citation "gave gifts to men" is a
    typological midrash. L/M follow the Hebrew. Documented in this header only.

=== Aspect and tense notes ===

Ps 67 — The verbs shift between jussive/cohortative (wishes/prayers: "let the peoples
    praise," "let the nations be glad") and the indicative perfect (v6: "the earth has
    yielded its increase" — the harvest is described as already happening, confirming
    the blessing). The perfect in v6 is rendered as past/present, not future.

Ps 68 — A complex mixture of imperatives (v1: "let God arise"; vv4,26,32: "sing!"),
    narrative perfects of past salvation-history (vv7–9: Sinai theophany), and
    imperfects of confident future (vv31: "princes shall come"). The psalm's temporal
    movement is deliberately fluid — past rescue grounds present praise grounds future
    expectation.

Ps 69 — Primarily a lament in the present (imperfect / participle of ongoing suffering)
    with a sharp future turn at v29 onward. The imprecatory section (vv22–28) is
    jussive/cohortative (prayers for divine action against enemies). The praise section
    (vv30–36) opens with cohortatives of resolve ("I will praise," "I will magnify")
    and ends with assurance-perfects ("God will save," "will build").
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
  # Psalm 67 — Harvest Blessing and Universal Praise
  # ===========================================================================
  "67": {
    "1": {
      "L": "To the chief Musician. On Neginoth. A Psalm — A Song. May God be gracious to us and bless us; and cause his face to shine upon us. Selah",
      "M": "To the director of music. On stringed instruments. A Psalm. A Song. May God be gracious to us and bless us, and may he cause his face to shine upon us. Selah",
      "T": "To the choirmaster. With stringed instruments. A Psalm. A Song.\nMay God deal gently with us and give us his blessing.\nMay the light of his face fall on us.\nSelah."
    },
    "2": {
      "L": "that your way may be known upon earth, your salvation among all nations.",
      "M": "so that your way may be known on earth, your saving power among all the nations.",
      "T": "Let it spread outward—\nlet the earth know what you are like,\nlet every nation see what it means to be rescued by you."
    },
    "3": {
      "L": "Let the peoples praise you, O God; let all the peoples praise you.",
      "M": "Let the peoples praise you, O God; let all the peoples give you praise.",
      "T": "Let the peoples praise you, God—\nevery last people on earth."
    },
    "4": {
      "L": "Let the nations be glad and sing for joy; for you will judge the peoples with equity, and govern the nations upon earth. Selah",
      "M": "Let the nations be glad and shout for joy; for you will judge the peoples with fairness, and guide the nations of the earth. Selah",
      "T": "Let the nations erupt in joy and song—\nbecause you will govern them straight,\nruling every people on earth with justice.\nSelah."
    },
    "5": {
      "L": "Let the peoples praise you, O God; let all the peoples praise you.",
      "M": "Let the peoples praise you, O God; let all the peoples give you praise.",
      "T": "Let the peoples praise you, God—\nevery last people on earth."
    },
    "6": {
      "L": "The earth has yielded its increase; God, our own God, blesses us.",
      "M": "The earth has given its harvest; God, our own God, has blessed us.",
      "T": "The earth has opened and given what it held.\nGod—our own God—has blessed us."
    },
    "7": {
      "L": "God blesses us; and all the ends of the earth shall fear him.",
      "M": "God blesses us, and all the ends of the earth will stand in awe of him.",
      "T": "God blesses us.\nAnd from the farthest edge of the world to the nearest,\npeople will stand in awe of him."
    }
  },

  # ===========================================================================
  # Psalm 68 — The Great Processional: God's Victory March and Universal Reign
  # ===========================================================================
  "68": {
    "1": {
      "L": "To the chief Musician. A Psalm — A Song of David. Let God arise; let his enemies be scattered; let those who hate him flee before him.",
      "M": "To the director of music. A Psalm of David. A Song. Let God arise and let his enemies be scattered; let those who hate him flee from before him.",
      "T": "To the choirmaster. A Psalm of David. A Song.\nUp—let God rise!\nLet his enemies scatter\nand all who hate him run."
    },
    "2": {
      "L": "As smoke is driven away, drive them away; as wax melts before fire, so let the wicked perish before God.",
      "M": "As smoke is dispersed by the wind, may you disperse them; as wax melts before fire, so let the wicked vanish from before God.",
      "T": "Scatter them like smoke before a gust of wind.\nMelt them like wax before a flame.\nLet the wicked dissolve—right before God's face."
    },
    "3": {
      "L": "But let the righteous be glad; let them rejoice before God; let them exult with great joy.",
      "M": "But let the righteous be glad and rejoice before God; let them celebrate with great joy.",
      "T": "The righteous, though—let them be overjoyed.\nLet them celebrate before God.\nLet the joy be extravagant."
    },
    "4": {
      "L": "Sing to God, sing praises to his name; extol him who rides upon the heavens — Yah is his name — and exult before him.",
      "M": "Sing to God, sing praises to his name; exalt him who rides upon the heavens — the LORD is his name — and rejoice before him.",
      "T": "Sing to God! Sing praise to his name!\nExalt the one who rides the storm-clouds—\nYah, that is his name, the living God—\nand come before him with your whole heart."
    },
    "5": {
      "L": "A father of the fatherless and a defender of widows is God in his holy dwelling.",
      "M": "God in his holy dwelling is a father to the fatherless and a defender of widows.",
      "T": "In his holy home,\nGod is father to those who have no father,\ndefender of those whose husbands are gone."
    },
    "6": {
      "L": "God sets the solitary in a household; he leads out the prisoners to prosperity; but the rebellious dwell in a parched land.",
      "M": "God gives the isolated a home to belong to; he brings prisoners out into freedom; but the rebellious must live in a barren land.",
      "T": "He places the lonely in families—gives them somewhere to belong.\nHe leads prisoners out into open country.\nBut those who refuse him are left in the wasteland."
    },
    "7": {
      "L": "O God, when you marched forth before your people, when you strode through the wilderness — Selah —",
      "M": "O God, when you went out before your people, when you marched through the wilderness — Selah —",
      "T": "God—when you marched out ahead of your people,\nwhen you cut through the wilderness at their head—\nSelah—"
    },
    "8": {
      "L": "the earth shook, the heavens poured down rain, at the presence of God — even Sinai itself — at the presence of God, the God of Israel.",
      "M": "the earth shook and the heavens poured down rain at the presence of God — even Sinai itself trembled — at the presence of God, the God of Israel.",
      "T": "the earth shook.\nThe sky opened and rain poured down\nin the presence of the God of Israel.\nEven Sinai trembled before him."
    },
    "9": {
      "L": "A generous rain you sent, O God; your inheritance that was exhausted, you strengthened.",
      "M": "You sent an abundant rain, O God; you restored your weary inheritance.",
      "T": "You sent soaking rain, God.\nWhen your people were spent, you revived them—\nmade your inheritance strong again."
    },
    "10": {
      "L": "Your congregation dwelt in it; in your goodness, O God, you provided for the poor.",
      "M": "Your congregation settled in the land; in your goodness, O God, you provided for the needy.",
      "T": "Your people made their home there.\nIn your generosity, God, you provided\nfor those who had nothing."
    },
    "11": {
      "L": "The Lord gave the command; great was the host of women heralds.",
      "M": "The Lord gave the word; great was the army of women who announced the victory.",
      "T": "The Lord spoke his word\nand a vast company of women carried the news—\nVictory! Victory!"
    },
    "12": {
      "L": "Kings of armies fled, they fled; and she who remained at home divided the spoil.",
      "M": "The kings of armies fled in haste; she who stayed at home shared in the plunder.",
      "T": "The armies' kings scattered and ran—\nand even those who had stayed behind at home\ngot to share in what was won."
    },
    "13": {
      "L": "Though you lay among the sheepfolds, the wings of a dove are covered with silver, its pinions with shimmering gold.",
      "M": "Even if you once lay among the sheepfolds, you shall shine like the wings of a dove, silver-covered, its feathers gleaming with gold.",
      "T": "Though you lay in the dust and the ash—\nyou will shine like a dove's wings:\nsilver on every feather,\ngold flashing in the light."
    },
    "14": {
      "L": "When the Almighty scattered kings in the land, snow fell on Zalmon.",
      "M": "When the Almighty scattered kings throughout the land, snow fell on Zalmon.",
      "T": "When the Almighty routed kings across the land,\nsnow fell on Zalmon—\na white brilliance after the battle."
    },
    "15": {
      "L": "The mountain of God is like the mountain of Bashan; a high mountain, like the mountain of Bashan.",
      "M": "The mountain of God is like the mountain of Bashan — a high, many-peaked mountain, like the mountain of Bashan.",
      "T": "O mountain of God—\nyou are like the heights of Bashan,\nlike that great, many-ridged peak."
    },
    "16": {
      "L": "Why do you look with envy, you many-peaked mountains? This is the mountain which God has desired for his dwelling — yes, the LORD will dwell there forever.",
      "M": "Why do you look with envy, O many-peaked mountains? This is the mountain that God chose for his dwelling place — yes, the LORD will dwell there forever.",
      "T": "Why do you stare so jealously at this hill, you great mountains?\nThis is the one God chose—\nthis is where he decided to live.\nThe LORD will make it his home forever."
    },
    "17": {
      "L": "The chariots of God are myriads, thousands upon thousands; the Lord is among them, as at Sinai, in his holy place.",
      "M": "The chariots of God number in the tens of thousands, thousands upon thousands; the Lord is among them — as at Sinai — in his holy place.",
      "T": "God's war-chariots are past counting—\ntens of thousands, and thousands more beyond that.\nThe Lord himself is present in their midst,\nhere in his holy place, as he was once at Sinai."
    },
    "18": {
      "L": "You have ascended on high, leading a train of captives; you have received gifts from men — even from the rebellious — so that the LORD God might dwell there.",
      "M": "You have ascended to the heights, leading a train of captives; you have received tribute from men — even from those who rebelled — so that the LORD God might make his dwelling there.",
      "T": "You climbed to the heights, a procession of captives at your heel.\nYou took tribute from the nations—\neven from those who had defied you—\nso that the LORD God could set up his dwelling here."
    },
    "19": {
      "L": "Blessed be the Lord, who day by day bears our burdens — the God of our salvation. Selah",
      "M": "Blessed be the Lord, who day after day carries our burdens for us — the God of our salvation. Selah",
      "T": "Praise the Lord—\nhe is the one who shoulders our load\nevery single day.\nHe is the God who saves.\nSelah."
    },
    "20": {
      "L": "Our God is a God of salvation; and to the LORD, the Lord, belong the pathways of escape from death.",
      "M": "Our God is the God of deliverance; and to the LORD, the Lord, belong the ways of escape from death.",
      "T": "This is our God—the God who saves.\nAnd it is the LORD, our Lord, who holds the keys:\nwho gets out of death alive, and who does not."
    },
    "21": {
      "L": "But God will shatter the head of his enemies, the hairy crown of him who walks on still in his guilty ways.",
      "M": "But God will crush the head of his enemies, the proud skull of those who persist in their guilt.",
      "T": "But God will split the skull of his enemies—\nthe proud, disheveled heads of those who keep on sinning\nand refuse to turn."
    },
    "22": {
      "L": "The Lord said, 'I will bring back from Bashan; I will bring my people back from the depths of the sea—'",
      "M": "The Lord declared, 'I will bring them back from Bashan; I will bring my people back from the depths of the sea—'",
      "T": "The Lord announced it:\n'I will bring them back—from Bashan, from the deep sea.\nThere is no place too far or too dark\nfor me to retrieve what is mine.'"
    },
    "23": {
      "L": "so that your foot may be bathed in blood, and the tongue of your dogs may have its portion from the enemies.",
      "M": "so that your foot will be stained in the blood of your enemies, and the tongues of your dogs will lap it up.",
      "T": "—so that you can walk through the wreckage of your enemies,\nand even the dogs that follow you\nwill lap up what remains."
    },
    "24": {
      "L": "They have seen your procession, O God — the procession of my God, my King, into the sanctuary.",
      "M": "People have witnessed your procession, O God — the procession of my God, my King, into the holy place.",
      "T": "They have seen it—your processional, God.\nMy God, my King, entering his sanctuary\nwith all his glory."
    },
    "25": {
      "L": "The singers go in front; the musicians follow after; among them are the young women playing tambourines.",
      "M": "The singers lead the procession; behind them come the musicians; among them, young women playing tambourines.",
      "T": "Singers at the front,\nmusicians following behind,\nand in among them—\ngirls with tambourines."
    },
    "26": {
      "L": "Bless God in the great assembly; bless the LORD — all you who are of Israel's spring.",
      "M": "Bless God in the great assembly; praise the LORD, all you who come from the fountain of Israel.",
      "T": "Bless God in the great gathering.\nPraise the LORD, all you who spring from Israel's source."
    },
    "27": {
      "L": "There is Benjamin, the youngest, leading them; the princes of Judah with their company; the princes of Zebulun, and the princes of Naphtali.",
      "M": "There is Benjamin, the youngest, leading the way; the princes of Judah in their bright company; the princes of Zebulun and the princes of Naphtali.",
      "T": "Little Benjamin out in front, leading—\nand behind him the princes of Judah in their ranks,\nthe princes of Zebulun,\nthe princes of Naphtali."
    },
    "28": {
      "L": "Your God has ordained your strength; strengthen, O God, what you have wrought for us.",
      "M": "Your God has established your power; show your strength, O God, in what you have already begun for us.",
      "T": "Your God decreed that you would be strong.\nNow confirm it, God—finish what you started among us."
    },
    "29": {
      "L": "Because of your temple at Jerusalem, kings shall bring tribute to you.",
      "M": "Because of your temple in Jerusalem, kings will bring their gifts to you.",
      "T": "Because of your house here in Jerusalem,\nkings will come carrying tribute to you."
    },
    "30": {
      "L": "Rebuke the beasts of the reeds, the herd of bulls with the calves of the peoples; until each one stoops to bring pieces of silver; scatter the peoples who delight in war.",
      "M": "Rebuke the beast that lurks in the reeds, the herd of bulls among the peoples' young, until they submit and bring silver tribute; scatter the peoples who delight in war.",
      "T": "Rebuke that beast crouching in the reeds—\nthe bull-herds among the nations' young—\nuntil they throw down their silver and bow.\nScatter those who live for war."
    },
    "31": {
      "L": "Nobles shall come from Egypt; Cush shall hasten to stretch out its hands to God.",
      "M": "Envoys will come from Egypt; Ethiopia will quickly extend her hands to God.",
      "T": "Egypt will send its own princes.\nEthiopia will rush to reach out toward God with open hands—\nall of them coming."
    },
    "32": {
      "L": "Sing to God, O kingdoms of the earth; sing praises to the Lord. Selah",
      "M": "Sing to God, O kingdoms of the earth; sing praises to the Lord. Selah",
      "T": "You kingdoms of the earth—sing to God!\nSing your praise to the Lord.\nSelah."
    },
    "33": {
      "L": "to him who rides upon the most ancient heavens — see, he sends out his voice, a mighty voice.",
      "M": "to him who rides upon the ancient heavens — listen, he thunders with his mighty voice.",
      "T": "To the one who rides the oldest heavens—\nhe lifts his voice,\nand it is a voice of power.\nHear it."
    },
    "34": {
      "L": "Ascribe strength to God; his majesty is over Israel, and his power is in the skies.",
      "M": "Ascribe power to God; his splendor is over Israel, and his strength is in the heavens.",
      "T": "Give God the glory of his strength.\nHis splendor is over Israel,\nhis power is in the skies above."
    },
    "35": {
      "L": "Awesome is God from his holy places — the God of Israel; he gives strength and power to his people. Blessed be God!",
      "M": "God is awe-inspiring from his sanctuary — the God of Israel is the one who gives strength and power to his people. Blessed be God!",
      "T": "Awe-striking is God from his holy place.\nThe God of Israel—he gives his people their strength,\nmakes them powerful.\nBlessed be God."
    }
  },

  # ===========================================================================
  # Psalm 69 — Lament of the Drowning Man, NT's Most Cited Psalm
  # ===========================================================================
  "69": {
    "1": {
      "L": "To the chief Musician. Upon Shoshannim. A Psalm of David. Save me, O God; for the waters have come in up to my soul.",
      "M": "To the director of music. To the tune of 'The Lilies.' A Psalm of David. Save me, O God, for the waters have risen to my neck.",
      "T": "To the choirmaster. To the tune 'Lilies.' A Psalm of David.\nSave me, God—\nthe water is at my throat."
    },
    "2": {
      "L": "I sink in deep mire, where there is no foothold; I have entered the deep waters, and the flood sweeps over me.",
      "M": "I am sinking in the deep mud — no place to stand; I have come into the depths of the waters, and the current sweeps over me.",
      "T": "I'm sinking in deep mud—\nno bottom, no foothold.\nI've gone under into deep water,\nand the current is overwhelming me."
    },
    "3": {
      "L": "I am worn out with my crying; my throat is parched; my eyes fail as I wait for my God.",
      "M": "I am exhausted from calling out; my throat is raw; my eyes have given out while waiting for my God.",
      "T": "I have cried until I have nothing left.\nMy throat is raw.\nMy eyes are worn out from scanning the horizon for my God."
    },
    "4": {
      "L": "Those who hate me without cause are more than the hairs of my head; mighty are those who would destroy me as enemies without reason; what I did not steal, must I then restore?",
      "M": "Those who hate me without cause outnumber the hairs of my head; those who are my enemies for no reason and who would destroy me are powerful; am I to restore what I never took?",
      "T": "The ones who hate me without reason—\nthere are more of them than hairs on my head.\nMy enemies who want to destroy me for things I never did—they are powerful.\nAnd now I am being made to restore what I never stole."
    },
    "5": {
      "L": "O God, you know my foolishness; and my sins are not hidden from you.",
      "M": "O God, you know my foolishness; and my sins are not concealed from you.",
      "T": "God, you know my failures—\nthe foolish things I've done.\nMy sins are completely visible to you."
    },
    "6": {
      "L": "Let not those who wait for you be put to shame on my account, O Lord GOD of hosts; let not those who seek you be brought to confusion for my sake, O God of Israel.",
      "M": "Let not those who hope in you be disgraced because of me, O Lord GOD of hosts; let not those who seek you be humiliated on my account, O God of Israel.",
      "T": "LORD God of hosts—\ndon't let those who trust you be put to shame because of what is happening to me.\nGod of Israel—\ndon't let those who seek you be brought to disgrace on my account."
    },
    "7": {
      "L": "For it is for your sake that I have carried reproach; shame has covered my face.",
      "M": "For your sake I have borne disgrace; humiliation has covered my face.",
      "T": "This is happening because of you—\nI am carrying the reproach that belongs to you.\nAnd it has covered my face with shame."
    },
    "8": {
      "L": "I have become a stranger to my own brothers, a foreigner to my mother's sons.",
      "M": "I have become a stranger to my brothers, an outsider to my own mother's children.",
      "T": "My own brothers do not recognize me anymore.\nTo my mother's children, I am a stranger."
    },
    "9": {
      "L": "For zeal for your house has consumed me; and the reproaches of those who reproach you have fallen on me.",
      "M": "Zeal for your house has consumed me; and the insults directed at you have landed on me.",
      "T": "I burned so completely for your house\nthat it consumed me from the inside.\nEvery insult aimed at you\nhas found its mark in me."
    },
    "10": {
      "L": "When I wept and fasted in affliction of soul, it became my reproach.",
      "M": "When I wept and humbled my soul with fasting, that became a source of shame for me.",
      "T": "I wept. I fasted—denied myself even food as a sign of grief.\nAnd they turned it into something to mock me with."
    },
    "11": {
      "L": "I put on sackcloth for my clothing; and I became a byword to them.",
      "M": "I dressed in sackcloth, and I became a laughingstock to them.",
      "T": "I wore sackcloth—\nand became a joke.\nA proverb for fools."
    },
    "12": {
      "L": "Those who sit at the gate talk about me; and I am the song of the drunkards.",
      "M": "Those who sit at the city gate gossip about me; and I have become the subject of the drunkards' songs.",
      "T": "The elders who sit at the gate whisper about me.\nThe drunkards have written songs about me."
    },
    "13": {
      "L": "But as for me, my prayer is to you, O LORD, at an acceptable time; O God, in the abundance of your steadfast love, answer me in the truth of your salvation.",
      "M": "But as for me, my prayer is directed to you, LORD, at a time of your favor; O God, in your great steadfast love, answer me in the faithfulness of your salvation.",
      "T": "But I—I keep praying to you, LORD,\nwhen the moment of your favor comes.\nGod, in all the breadth of your steadfast love—\nanswer me;\nin the faithfulness of your salvation—\nlook at me."
    },
    "14": {
      "L": "Deliver me from the mire, and let me not sink; let me be rescued from those who hate me and from the deep waters.",
      "M": "Rescue me from the mire and do not let me sink; let me be saved from those who hate me and from the deep water.",
      "T": "Pull me out of this mud—\ndo not let me go under.\nRescue me from those who hate me,\nfrom these waters that are over my head."
    },
    "15": {
      "L": "Let not the flood of waters sweep over me; let not the deep swallow me up; let not the pit close its mouth over me.",
      "M": "Let not the flood sweep me away; let not the depths swallow me; let not the pit close its mouth on me.",
      "T": "Do not let the flood current carry me away.\nDo not let the deep swallow me.\nDo not let the mouth of the pit close over me."
    },
    "16": {
      "L": "Answer me, O LORD, for your steadfast love is good; in the abundance of your compassion, turn to me.",
      "M": "Hear me, LORD, for your steadfast love is good; in your great compassion, turn toward me.",
      "T": "Hear me, LORD—your steadfast love is good and real.\nTurn toward me.\nIn all the depth of your compassion—turn."
    },
    "17": {
      "L": "And do not hide your face from your servant; for I am in distress — answer me quickly.",
      "M": "Do not turn your face away from your servant; I am in great distress — answer me quickly.",
      "T": "Do not look away from your servant.\nI am in desperate trouble—\nanswer me, and do it now."
    },
    "18": {
      "L": "Draw near to my soul and redeem it; ransom me because of my enemies.",
      "M": "Come near to my soul and rescue it; set me free because of my enemies.",
      "T": "Come close to my life and buy it back.\nSet me free—\nbefore my enemies finish what they started."
    },
    "19": {
      "L": "You have known my reproach, my shame, and my dishonor; all my adversaries are before you.",
      "M": "You know my disgrace, my shame, and my humiliation; all my enemies are in your sight.",
      "T": "You have seen it all—the reproach, the shame, the dishonor.\nEvery one of my adversaries is in your line of sight."
    },
    "20": {
      "L": "Reproach has broken my heart, so that I am in despair; I looked for sympathy, but there was none; and for comforters, but I found none.",
      "M": "Disgrace has broken my heart so that I am in anguish; I looked for someone to show compassion, but there was none; and for comforters, but I found none.",
      "T": "The disgrace of it has broken my heart.\nI am undone.\nI looked for someone to feel sorry for me—no one.\nI looked for someone who would sit with me in it—not one person."
    },
    "21": {
      "L": "They gave me gall for my food; and for my thirst they gave me vinegar to drink.",
      "M": "They put bitter gall in my food; and when I was thirsty, they offered me vinegar to drink.",
      "T": "When I needed food, they gave me poison.\nWhen I was parched, they handed me vinegar to drink."
    },
    "22": {
      "L": "Let their table before them become a snare; and when they are at peace, let it become a trap.",
      "M": "Let their table be set as a snare before them; and what was meant for their prosperity become a trap.",
      "T": "May the very table they feast at become a trap.\nMay what they take such comfort in\nspring shut on them."
    },
    "23": {
      "L": "Let their eyes be darkened so they cannot see; and cause their loins to quake continually.",
      "M": "Let their eyes be darkened so they cannot see; and let their bodies tremble without ceasing.",
      "T": "Let their sight go dark—\nblind to the truth.\nLet their bodies shake and never be still."
    },
    "24": {
      "L": "Pour out your fury upon them; and let your burning anger overtake them.",
      "M": "Pour out your wrath upon them; let your fierce anger seize them.",
      "T": "Pour your wrath over them.\nLet your burning anger catch up with them and hold them."
    },
    "25": {
      "L": "Let their encampment be left desolate; let no one dwell in their tents.",
      "M": "Let their camp become desolate; let no one live in their dwelling.",
      "T": "Let their homes stand empty.\nLet no one move in where they lived."
    },
    "26": {
      "L": "For they have persecuted the one you have struck; and they recount the pain of those you have wounded.",
      "M": "For they have harassed the one whom you have afflicted; they have gossiped about the suffering of those you wounded.",
      "T": "They hunted down the very one you had already struck.\nThey mocked the pain of those you wounded.\nThere is no mercy in them."
    },
    "27": {
      "L": "Add guilt upon their guilt; and let them not enter into your righteousness.",
      "M": "Pile their guilt on top of their guilt; and do not let them share in your vindication.",
      "T": "Let their guilt accumulate—\nmore on top of more.\nNever let them come into the place where you make things right."
    },
    "28": {
      "L": "Let them be blotted out of the scroll of the living; and let them not be enrolled with the righteous.",
      "M": "Let them be erased from the scroll of the living; let them not be listed among the righteous.",
      "T": "Erase their names from the scroll of the living.\nDo not let them be counted among the righteous."
    },
    "29": {
      "L": "But I am poor and in pain; let your salvation, O God, lift me on high.",
      "M": "But I am afflicted and in pain; may your salvation, O God, lift me up.",
      "T": "But I—I am poor and I am hurting.\nGod, let your salvation be the thing that lifts me out of this."
    },
    "30": {
      "L": "I will praise the name of God with a song; I will magnify him with thanksgiving.",
      "M": "I will praise the name of God with a song of praise; I will honor him with thanksgiving.",
      "T": "I will praise the name of God with a song.\nI will make him great with thanksgiving."
    },
    "31": {
      "L": "This will please the LORD more than an ox, more than a bull with horns and hoofs.",
      "M": "This will please the LORD more than an ox or a bull with its horns and hoofs.",
      "T": "This—the song, the thanks—\npleases the LORD more than a prize bull,\nmore than any animal you could lead to an altar."
    },
    "32": {
      "L": "The humble shall see it and be glad; you who seek God, let your hearts revive.",
      "M": "The afflicted will see it and rejoice; those of you who seek God, may your hearts be renewed.",
      "T": "Those who are poor and low will see this and be glad.\nYou who seek God—let it put life back in your heart."
    },
    "33": {
      "L": "For the LORD hears the poor, and does not despise his prisoners.",
      "M": "For the LORD listens to the needy; he does not look down on those he has bound.",
      "T": "The LORD hears the poor.\nHe does not dismiss the ones who are imprisoned and cannot get out."
    },
    "34": {
      "L": "Let heaven and earth praise him, the seas and everything that stirs in them.",
      "M": "Let heaven and earth give him praise, the seas and every living thing in them.",
      "T": "Heaven and earth—praise him.\nThe seas and everything alive in them."
    },
    "35": {
      "L": "For God will save Zion and rebuild the cities of Judah; and they will settle there and possess it.",
      "M": "For God will save Zion and rebuild the cities of Judah; people will live there and take possession of it.",
      "T": "God will save Zion.\nHe will rebuild the cities of Judah.\nHis people will live there—it will be theirs."
    },
    "36": {
      "L": "The offspring of his servants shall inherit it; and those who love his name shall dwell in it.",
      "M": "The children of his servants will inherit it; and those who love his name will live there.",
      "T": "The children of those who served him will inherit it.\nAll who love his name—\nthey will live there."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 67–69 written.')

if __name__ == '__main__':
    main()
