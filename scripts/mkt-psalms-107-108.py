"""
MKT Psalms chapters 107–108 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-107-108.py

=== Overview of this unit ===

Ps 107 (43 v) — Anonymous congregational hymn of thanksgiving. The most architecturally
    elaborate psalm in Book IV/V (Pss 90–150). Its structure is a fourfold rescue-cycle
    built around two recurring refrains, framed by an opening summons (vv1-3) and a
    wisdom coda (vv33-43):

    SUMMONS (vv1-3): Call to the redeemed to give thanks; they have been gathered from
        the four compass points — east, west, north, south.

    CYCLE 1 (vv4-9): Desert wanderers. Those who had no road and no city found one when
        they cried to the LORD. The resolution (v9) is characteristically Psalter: God
        "satisfies the longing soul." H8264 (longing/yearning) — nefesh as craving self.

    CYCLE 2 (vv10-16): Prisoners in darkness and iron. They sat in the shadow of death
        (H6757, tsalmaveth — same word as Ps 23:4) because they had defied God's word.
        His answer: he shatters bronze gates and cuts iron bars.

    CYCLE 3 (vv17-22): Sick fools. Not innocently afflicted — "fools" (H191, evilim)
        made sick by their "way" (the path of sin). His answer: he sends his word and
        heals (v20). The word as healing agent anticipates John 1 and the gospel healings.

    CYCLE 4 (vv23-32): Sailors in the storm. The most vivid section — the psalm shifts
        from summary to dramatic poetry: ships heaving to the sky, plunging to the deep,
        sailors lurching like drunkards, skill "swallowed up" (H1104, bala). God silences
        the storm "to a whisper" (H1827, demamah — the same word as the "still small
        voice" in 1 Kings 19:12).

    WISDOM CODA (vv33-43): God's sovereignty over geography and social order. He can
        reverse any situation — rivers to desert, desert to springs; he can raise the
        poor and abase the proud. The psalm closes with the classic wisdom summons (v43):
        whoever is wise, let them "observe" (H8104, shamar — keep, guard, attend to)
        these things and "consider" (H995, bin — discern, understand deeply) the
        steadfast love of the LORD.

    This psalm is quoted in NT contexts of grace and healing (especially v20 re. the
    healing word), and the storm narrative parallels the Synoptic sea-calming accounts
    (Matt 8:23-27, Mark 4:35-41, Luke 8:22-25) with near-verbal overlap.

Ps 108 (13 v) — A Psalm of David. A liturgical composite: vv1-5 = Ps 57:7-11;
    vv6-13 = Ps 60:5-12. The psalm moves from personal vow of praise (vv1-5) to
    national petition backed by a divine oracle (vv6-13). It was composed or edited
    to stand as a self-contained liturgy for corporate worship — individual trust
    becoming the foundation for communal confidence. The divine speech (vv7-9)
    asserts God's sovereignty over the entire land (both Israel's tribal territory
    and its traditional enemies: Moab, Edom, Philistia). The petition that follows
    (vv10-13) honestly admits that God had been distant — and calls him back.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M/T throughout — consistent with all prior Psalms
    scripts.

H2617 (חֶסֶד, chesed): "steadfast love" in L/M/T throughout. This is the theological
    spine of Ps 107: it appears at vv1, 8, 15, 21, 31 (the summons and all four
    thanksgiving refrains) and v43 (the wisdom close). The entire psalm is a meditation
    on what chesed looks like when it acts. At Ps 108:4 chesed is paired with faithfulness
    (H571, emet) — "steadfast love" / "faithfulness" in all tiers.

H5315 (נֶפֶשׁ, nefesh): "soul" in all tiers. Used as the embodied, craving self at Ps
    107:5 ("soul fainted"), 107:9 ("longing soul," "hungry soul"), 107:18 ("soul
    loathed"), and 107:26 ("soul melted"). This is nefesh as appetitive/vital self, not
    Greek immaterial soul.

H7307 (רוּחַ, ruach) at Ps 107:25: "wind" in all tiers. The storm wind God commands —
    natural phenomenon, not the Spirit. Consistent with the ruach-as-wind reading in
    Ps 104:3-4.

H4691 (מְצוּקוֹת, metsukoth / distresses): "distresses" in L/M; "distresses" or
    "desperate straits" in T. Appears in the cry refrain (vv6, 13, 19, 28) — each time
    the same word, giving the refrain its verbal unity.

H6757 (צַלְמָוֶת, tsalmaveth / shadow of death): "shadow of death" in L/M/T — the
    compound word carries the full weight of death-realm imagery. Same word as Ps 23:4;
    the prisoners literally sit in the death-shadow.

H1827 (דְּמָמָה, demamah / calm/stillness) at Ps 107:29: "calm" (L) / "calm" (M) /
    "whisper" (T) — this is the exact word used for Elijah's "still small voice" in
    1 Kings 19:12 (qol demamah daqah, the voice of thin silence). The T tier surfaces
    this echo.

H3519 (כָּבוֹד, kavod / glory) at Ps 108:1: "my glory" (L) — the Psalter idiom for
    the inner self that makes music (the soul/spirit). Rendered "with all my soul" (M)
    and "everything I have" (T) to convey the sense of one's full inner person being
    consecrated to praise.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Consistent throughout.

H2710 (חֹקֵק, choqeq / lawgiver/scepter) at Ps 108:8: "scepter" in L/M/T — the
    royal symbol of rule, not the legislative function. Judah bears the scepter
    of royal governance (cf. Gen 49:10, "the scepter shall not depart from Judah").

H4581 (מָעוֹז, maoz / strength/fortress) at Ps 108:8: "helmet" (L) / "helmet" (M) /
    "helmet" (T) — Ephraim's tribe occupied the central highlands, the "head" of
    Israel geographically; the warrior-helmet image fits. Prior Psalms scripts
    rendered this "strength of my head" (Ps 60 context); here rendered "helmet on
    my head" for clarity.

=== Refrain consistency ===

Ps 107 contains two refrains repeated four times each:

  Cry refrain (vv6, 13, 19, 28):
    L: "Then they cried to the LORD in their trouble, and he delivered them from their distresses."
    (v6/19 use H5337 yatsal "deliver/rescue"; v13/19/28 use H3467 yasha "save" — rendered
    "delivered" vs "saved" accordingly in L; M/T unified)

  Thanksgiving refrain (vv8, 15, 21, 31):
    L/M: "Let them give thanks to the LORD for his steadfast love, for his wonderful works
          to the children of man!"
    T: Same, line-broken for poetry.

=== Textual and interpretive notes ===

Ps 107:3 — H3220 (yam, "sea") here means the western direction (Mediterranean); rendered
    "from the south" would misread it. The four-direction formula is east–west–north–sea
    (= west). Rendered "from east and west, from north and from the sea" in L;
    "from every direction" in M; "east and west, north and south" in T (the natural
    English idiom for all four points).

Ps 107:20 — "He sent his word and healed them." This verse is the theological climax of
    the third cycle. The "word" (H1697, dabar) as the agent of healing is striking —
    God does not come in person; his word accomplishes the rescue. The T tier notes this.

Ps 107:27 — H2451 (chokmah, "wisdom/skill") at "wits' end" literally: "all their
    wisdom was swallowed up." The sailors' professional competence is simply consumed
    by the storm. Rendered "all their skill was swallowed up" in L/M; "all their
    wisdom — every bit of it — was gone" in T.

Ps 107:40-41 — The God who pours contempt on princes and lifts the poor echoes the
    Magnificat (Luke 1:51-53) and the Hannah song (1 Sam 2:7-8). This is a key
    structural pattern: the reversal of social positions by divine action.

Ps 108:7-9 — The divine oracle of dominion. God speaks in the first person, claiming
    the entire land as his possession. The tripartite claim (Gilead/Manasseh =
    Transjordan; Ephraim/Judah = Cisjordan highlands; Moab/Edom/Philistia = surrounding
    nations) is a complete assertion of sovereignty from Jordan to the sea. The demeaning
    images for Moab (washbasin) and Edom (sandal-throwing = claiming ownership of land
    by walking it, cf. Ruth 4:7) are terse and pointed — they are not rivals but
    utilities in God's economy.

=== Aspect and tense notes ===

Ps 107: The four cycles use a consistent tense-pattern: perfect (completed act)
    for the description of the group's plight; waw-consecutive imperfect (narrative
    past) for the cry and rescue; jussive for the refrain ("let them thank"). The
    wisdom coda shifts to the imperfect for ongoing divine reversal ("he turns rivers,"
    "he lifts the poor") — these are habitual/gnomic presents, not single past acts.

Ps 108: The personal section (vv1-5) is imperfect/cohortative (volitional present:
    "I will sing," "I will awaken"). The divine speech (vv7-9) uses perfect for the
    oracle: God "has spoken" (perfect) and the claimed acts are also expressed as
    certain future by the perfects of confidence. The petition (vv10-13) uses the
    imperfect interrogative ("who will bring?").
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
  # Psalm 107 — Great Congregational Hymn of Thanksgiving
  # Four rescue-cycles + wisdom coda; the psalm of steadfast love
  # ===========================================================================
  "107": {
    # --- Summons (vv1-3) ---
    "1": {
      "L": "Give thanks to the LORD, for he is good, for his steadfast love endures forever!",
      "M": "Give thanks to the LORD, for he is good; his steadfast love endures forever!",
      "T": "Give thanks to the LORD — he is good.\nHis steadfast love endures forever."
    },
    "2": {
      "L": "Let the redeemed of the LORD say so — those he has redeemed from the hand of the enemy,",
      "M": "Let those the LORD has redeemed declare it — those he bought back from the grip of the enemy,",
      "T": "Let the redeemed of the LORD say so—\nthose he has rescued\nfrom the enemy's hand,"
    },
    "3": {
      "L": "and gathered from the lands, from the east and from the west, from the north and from the sea.",
      "M": "and gathered in from every land — from east and west, from north and south.",
      "T": "gathered home from every land—\nfrom east and west,\nfrom north and south."
    },
    # --- Cycle 1: Desert Wanderers (vv4-9) ---
    "4": {
      "L": "Some wandered in a desert wilderness, finding no path to a city to dwell in.",
      "M": "Some wandered in the desert waste, finding no road to a city where they could live.",
      "T": "Some wandered in the desert—\nno road, no direction,\nno city to call home."
    },
    "5": {
      "L": "Hungry and thirsty, their soul fainted within them.",
      "M": "Hungry and thirsty, their soul grew faint within them.",
      "T": "Hungry and thirsty,\ntheir soul\nfainted within them."
    },
    "6": {
      "L": "Then they cried to the LORD in their trouble, and he delivered them from their distresses.",
      "M": "Then they cried to the LORD in their trouble, and he rescued them from their distresses.",
      "T": "Then they cried to the LORD in their trouble—\nand he delivered them\nfrom their distresses."
    },
    "7": {
      "L": "He led them by a straight way until they reached a city to dwell in.",
      "M": "He guided them on a straight path to a city where they could settle.",
      "T": "He led them by a straight road\nuntil they arrived\nat a city to call home."
    },
    "8": {
      "L": "Let them give thanks to the LORD for his steadfast love, for his wonderful works to the children of man!",
      "M": "Let them give thanks to the LORD for his steadfast love and for his wonders done for the children of man!",
      "T": "Let them give thanks to the LORD for his steadfast love—\nfor all the wonders he has done\nfor the children of man!"
    },
    "9": {
      "L": "For he satisfies the longing soul, and the hungry soul he fills with good things.",
      "M": "For he gives what the hungry soul longs for and fills the starving soul with good things.",
      "T": "For he satisfies the soul that longs.\nThe hungry soul—\nhe fills it with every good thing."
    },
    # --- Cycle 2: Prisoners in Darkness (vv10-16) ---
    "10": {
      "L": "Some sat in darkness and in the shadow of death, prisoners in affliction and iron —",
      "M": "Some sat in darkness and in the shadow of death, bound in misery and iron chains —",
      "T": "Some sat in darkness — in the shadow of death—\nprisoners in iron chains,\nbowed down in misery,"
    },
    "11": {
      "L": "for they had rebelled against the words of God and despised the counsel of the Most High.",
      "M": "for they had defied the commands of God and rejected the plan of the Most High.",
      "T": "because they had defied the words of God\nand scorned the counsel\nof the Most High."
    },
    "12": {
      "L": "So he humbled their heart with hard labor; they stumbled, with none to help.",
      "M": "So he wore them down with grinding toil; they stumbled and fell, with no one to help.",
      "T": "So he broke their pride with hard labor.\nThey stumbled and fell—\nno one there to help."
    },
    "13": {
      "L": "Then they cried to the LORD in their trouble, and he saved them from their distresses.",
      "M": "Then they cried to the LORD in their trouble, and he saved them from their distresses.",
      "T": "Then they cried to the LORD in their trouble—\nand he delivered them\nfrom their distresses."
    },
    "14": {
      "L": "He brought them out of darkness and the shadow of death and shattered their bonds.",
      "M": "He led them out of the darkness and the shadow of death and broke their chains apart.",
      "T": "He brought them out of darkness,\nout of death's long shadow—\nand shattered every chain."
    },
    "15": {
      "L": "Let them give thanks to the LORD for his steadfast love, for his wonderful works to the children of man!",
      "M": "Let them give thanks to the LORD for his steadfast love and for his wonders done for the children of man!",
      "T": "Let them give thanks to the LORD for his steadfast love—\nfor all the wonders he has done\nfor the children of man!"
    },
    "16": {
      "L": "For he has shattered the doors of bronze and cut the bars of iron in two.",
      "M": "For he has smashed the gates of bronze and snapped the iron bars.",
      "T": "For he has shattered the gates of bronze\nand cut through\nthe bars of iron."
    },
    # --- Cycle 3: Sick Fools (vv17-22) ---
    "17": {
      "L": "Some were fools; they were afflicted because of their sinful way and because of their iniquities.",
      "M": "Some were fools who made themselves sick by the path they chose, suffering because of their own sins.",
      "T": "Some were their own worst enemies—\nmade sick by the road they chose,\nbowed down by what they had done."
    },
    "18": {
      "L": "Their soul loathed every kind of food, and they drew near to the gates of death.",
      "M": "Their soul could not bear any food, and they were approaching the very gates of death.",
      "T": "Their soul turned from every food.\nThey had come\nto the gates of death."
    },
    "19": {
      "L": "Then they cried to the LORD in their trouble, and he saved them from their distresses.",
      "M": "Then they cried to the LORD in their trouble, and he saved them from their distresses.",
      "T": "Then they cried to the LORD in their trouble—\nand he delivered them\nfrom their distresses."
    },
    "20": {
      "L": "He sent out his word and healed them and delivered them from their destructions.",
      "M": "He sent his word and healed them and pulled them back from the pit of destruction.",
      "T": "He sent his word — and healed them.\nJust his word —\nand he pulled them back from destruction."
    },
    "21": {
      "L": "Let them give thanks to the LORD for his steadfast love, for his wonderful works to the children of man!",
      "M": "Let them give thanks to the LORD for his steadfast love and for his wonders done for the children of man!",
      "T": "Let them give thanks to the LORD for his steadfast love—\nfor all the wonders he has done\nfor the children of man!"
    },
    "22": {
      "L": "And let them offer sacrifices of thanksgiving and declare his works with singing.",
      "M": "Let them bring offerings of thanksgiving and tell of his deeds with shouts of joy.",
      "T": "Let them bring offerings of thanksgiving.\nLet them recount his deeds\nwith shouts of joy."
    },
    # --- Cycle 4: Sailors in the Storm (vv23-32) ---
    "23": {
      "L": "Those who went down to the sea in ships and did their business on the great waters —",
      "M": "Some went down to the sea in ships, plying their trade on the wide and open sea —",
      "T": "Some went down to the sea in ships—\ndoing their work\non the great and open waters—"
    },
    "24": {
      "L": "these saw the works of the LORD, his wonders in the deep.",
      "M": "they witnessed what the LORD does — his wonders in the depths.",
      "T": "they saw the works of the LORD—\nhis wonders\nin the deep."
    },
    "25": {
      "L": "For he spoke and raised up a stormy wind, which lifted up its waves.",
      "M": "He spoke and a storm-wind rose, whipping the sea into waves.",
      "T": "He spoke — and the storm wind rose.\nIt tore across the water\nand drove the waves high."
    },
    "26": {
      "L": "They mounted up to the heavens and went down to the depths; their soul melted away in their calamity.",
      "M": "They heaved up to the sky and plunged back down to the depths; they were terrified out of their senses.",
      "T": "Up to the sky — then down to the depths.\nEvery bit of courage they had\nmelted in the terror."
    },
    "27": {
      "L": "They reeled and staggered like a drunkard, and all their skill was swallowed up.",
      "M": "They lurched and stumbled like drunken men, and every bit of their seamanship was consumed.",
      "T": "They lurched and staggered like drunkards.\nAll their skill — every last bit of it —\nswallowed up."
    },
    "28": {
      "L": "Then they cried to the LORD in their trouble, and he brought them out of their distresses.",
      "M": "Then they cried to the LORD in their trouble, and he brought them out of their distresses.",
      "T": "Then they cried to the LORD in their trouble—\nand he delivered them\nfrom their distresses."
    },
    "29": {
      "L": "He stilled the storm to a calm, so that its waves were hushed.",
      "M": "He calmed the storm to a stillness, and the waves went quiet.",
      "T": "He stilled the storm to a whisper.\nThe waves —\nthey were still."
    },
    "30": {
      "L": "Then they were glad because they were quiet, and he led them to their desired haven.",
      "M": "They were overjoyed as the sea grew calm, and he guided them into the harbor they had longed for.",
      "T": "Then they were glad — the sea was quiet.\nAnd he guided them in\nto the harbor they had longed for."
    },
    "31": {
      "L": "Let them give thanks to the LORD for his steadfast love, for his wonderful works to the children of man!",
      "M": "Let them give thanks to the LORD for his steadfast love and for his wonders done for the children of man!",
      "T": "Let them give thanks to the LORD for his steadfast love—\nfor all the wonders he has done\nfor the children of man!"
    },
    "32": {
      "L": "Let them exalt him in the congregation of the people and praise him in the assembly of the elders.",
      "M": "Let them lift up his name in the great assembly of the people and honor him in the council of the elders.",
      "T": "Let them lift him high in the congregation—\nlet them praise him\nbefore the council of elders."
    },
    # --- Wisdom Coda: God's Sovereignty over Land and People (vv33-43) ---
    "33": {
      "L": "He turns rivers into a desert and springs of water into thirsty ground,",
      "M": "He can turn rivers into desert and springs of water into parched ground,",
      "T": "He turns rivers into desert.\nHe turns springs of water\ninto cracked and thirsty ground."
    },
    "34": {
      "L": "a fruitful land into a salt waste, for the wickedness of those who dwell in it.",
      "M": "fertile land into a barren salt flat — for the wickedness of those who live there.",
      "T": "Fertile land — he turns it to a salt waste\nbecause of the wickedness\nof those who live in it."
    },
    "35": {
      "L": "He turns the desert into pools of water and dry land into springs of water.",
      "M": "But he can also turn the desert into pools of water and dry ground into flowing springs.",
      "T": "He turns the desert into pools of water.\nHe turns dry ground\ninto flowing springs."
    },
    "36": {
      "L": "And there he settles the hungry to dwell, so that they establish a city to live in.",
      "M": "He brings the hungry to live there, and they build a city to call home.",
      "T": "He brings the hungry to settle there.\nThey build a city—\nthey call it home."
    },
    "37": {
      "L": "They sow fields and plant vineyards that yield a fruitful harvest.",
      "M": "They plant fields and vineyards that bring in an abundant crop.",
      "T": "They plant fields and vineyards.\nThey bring in a harvest\nrich beyond what they sowed."
    },
    "38": {
      "L": "He blesses them so they multiply greatly, and he does not let their livestock decrease.",
      "M": "He blesses them and they grow in number, and he keeps their herds from shrinking.",
      "T": "He blesses them — they multiply greatly.\nHe keeps their flocks\nfrom dwindling."
    },
    "39": {
      "L": "When they are diminished and brought low through oppression, trouble, and sorrow,",
      "M": "But when they are cut down and humbled through oppression, calamity, and grief,",
      "T": "But then — they are brought low.\nOppression, calamity, grief:\nthey dwindle."
    },
    "40": {
      "L": "he pours contempt on princes and makes them wander in trackless wastes;",
      "M": "he pours contempt on rulers and sends them wandering in pathless deserts —",
      "T": "He pours contempt on rulers—\nhe drives them to wander\nin pathless, empty wastes."
    },
    "41": {
      "L": "but he lifts the needy out of their affliction and makes their families like flocks.",
      "M": "but he raises the poor person up from their misery and makes their family grow like a flock.",
      "T": "But he lifts the poor\nout of affliction—\nand makes their family like a flock."
    },
    "42": {
      "L": "The upright see it and are glad, and all wickedness shuts its mouth.",
      "M": "The righteous see all this and rejoice, while every voice of wickedness is silenced.",
      "T": "The upright see it and are glad.\nEvery mouth that speaks wickedness\nis shut."
    },
    "43": {
      "L": "Whoever is wise, let him observe these things and consider the steadfast love of the LORD.",
      "M": "Let those who are wise take note of all this and reflect carefully on the steadfast love of the LORD.",
      "T": "Whoever is wise — let them attend to this.\nLet them sit with it and understand:\nthe steadfast love of the LORD is over all."
    }
  },

  # ===========================================================================
  # Psalm 108 — A Song of David (composite: Pss 57:7-11 + 60:5-12)
  # Personal vow of praise becoming national petition
  # ===========================================================================
  "108": {
    "1": {
      "L": "A Song. A Psalm of David. My heart is steadfast, O God; I will sing and make music, even with my glory.",
      "M": "A Song. A Psalm of David. My heart is ready, O God; I will sing and praise you with all my soul.",
      "T": "A Song. A Psalm of David.\nMy heart is steadfast, O God.\nI will sing — I will make music\nwith everything I have."
    },
    "2": {
      "L": "Awake, harp and lyre! I myself will awaken the dawn.",
      "M": "Awake, harp and lyre! I will be the one to rouse the dawn.",
      "T": "Awake, harp and lyre!\nI will be the one\nwho wakes the dawn."
    },
    "3": {
      "L": "I will give thanks to you, O LORD, among the peoples and I will sing praises to you among the nations.",
      "M": "I will praise you, O LORD, among all peoples and sing your praises among the nations.",
      "T": "I will thank you, LORD,\namong all the peoples.\nI will sing your praises\namong the nations."
    },
    "4": {
      "L": "For your steadfast love is great above the heavens, and your faithfulness reaches to the clouds.",
      "M": "For your steadfast love towers above the heavens, and your faithfulness reaches to the skies.",
      "T": "Your steadfast love towers above the heavens.\nYour faithfulness\nreaches to the clouds."
    },
    "5": {
      "L": "Be exalted, O God, above the heavens! Let your glory be over all the earth!",
      "M": "Be lifted high above the heavens, O God! Let your glory fill the whole earth!",
      "T": "Be exalted, O God — above the heavens.\nLet your glory cover\nall the earth."
    },
    "6": {
      "L": "That your beloved may be delivered — save us by your right hand and answer us.",
      "M": "Save your beloved ones — rescue us by your mighty hand and answer our prayer.",
      "T": "Save your beloved ones—\nreach out with your right hand\nand rescue us. Answer us."
    },
    "7": {
      "L": "God has spoken in his holiness: I will exult; I will divide Shechem and portion out the valley of Succoth.",
      "M": "God has spoken from his holy place: 'I will celebrate; I will apportion Shechem and measure out the valley of Succoth.'",
      "T": "God has spoken from his holiness:\n'I will triumph!\nI will divide Shechem;\nI will apportion the valley of Succoth.'"
    },
    "8": {
      "L": "Gilead is mine; Manasseh is mine; Ephraim is the helmet of my head; Judah is my scepter.",
      "M": "Gilead belongs to me; Manasseh belongs to me; Ephraim is the helmet on my head; Judah is my royal scepter.",
      "T": "Gilead is mine. Manasseh is mine.\nEphraim — the helmet on my head.\nJudah — my royal scepter."
    },
    "9": {
      "L": "Moab is my washbasin; over Edom I cast my sandal; over Philistia I shout in triumph.",
      "M": "Moab is my washbasin; over Edom I toss my sandal; over Philistia I raise a victory shout.",
      "T": "Moab — I wash my feet there.\nEdom — I claim it by throwing my sandal.\nOver Philistia I shout in triumph."
    },
    "10": {
      "L": "Who will bring me to the fortified city? Who will lead me to Edom?",
      "M": "Who will take me into the strong, walled city? Who will guide me all the way to Edom?",
      "T": "Who will lead me to the fortified city?\nWho will bring me\nall the way into Edom?"
    },
    "11": {
      "L": "Have you not rejected us, O God? And you, O God, do you not go out with our armies?",
      "M": "God, have you not turned your back on us? Why do you no longer march out with our armies?",
      "T": "Have you rejected us, God?\nDo you no longer march out\nwith our armies?"
    },
    "12": {
      "L": "Give us help against our foes, for the help of man is worthless.",
      "M": "Come to our aid against the enemy — human help amounts to nothing.",
      "T": "Give us help against the enemy.\nHuman help is worthless—\nonly you can save."
    },
    "13": {
      "L": "With God we shall act valiantly, for it is he who will tread down our enemies.",
      "M": "With God we will fight with courage, for he is the one who will crush our enemies underfoot.",
      "T": "With God — we will do great things.\nFor it is he who will tread down\nour enemies."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 107–108 written.')

if __name__ == '__main__':
    main()
