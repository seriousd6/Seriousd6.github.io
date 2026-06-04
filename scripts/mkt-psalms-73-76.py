"""
MKT Psalms chapters 73–76 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-73-76.py

=== Overview of this unit ===

All four psalms are Asaph psalms (Book III of the Psalter, Pss 73–89), and all belong
to the Elohistic Psalter (Pss 42–83), where Elohim (H430) dominates over YHWH (H3068).
This explains why some psalms substitute "God" where other collections would have "LORD."

Ps 73 — The Psalm of Theodicy; Asaph's Crisis Resolved (28 verses):
         The philosophical and spiritual heart of the Psalter. Asaph confesses that
         his envy of the wicked nearly destroyed his faith (vv2–16), then describes
         the turning point: entering the sanctuary, where he understood the end of the
         wicked (v17). The psalm moves from crisis (vv1–16) through reversal (vv17–20)
         to renewal and declaration of exclusive trust (vv21–28). The akh (אַךְ, "truly/
         surely") particle appears at vv1 and 13, forming a theological bracket: the
         opening confession of God's goodness and the near-collapse of that confidence.
         V25 ("Whom have I in heaven but you?") is one of the most concentrated
         expressions of covenantal monotheism in Scripture.

Ps 74 — National Lament over the Destruction of the Sanctuary (23 verses):
         A communal lament over the burning of the temple, almost certainly composed
         after the Babylonian destruction of 586 BC. Two structural pillars:
         (1) vv1–11: lament over the desolation and plea for God to act;
         (2) vv12–17: a creation-hymn recalling God's ancient cosmic victories
         (splitting the sea, crushing Leviathan, fixing the seasons), offered as the
         basis for appeal; (3) vv18–23: renewed plea for remembrance and action.
         "Leviathan" (H3882) at v14 is the chaos-sea-dragon of ancient Near Eastern
         cosmology, here domesticated as a creature God crushed at creation. The
         "turtledove" metaphor at v19 (H8449) is the congregation portrayed as a
         small, vulnerable bird surrounded by predators.

Ps 75 — God the Just Judge; The Cup of Wrath (10 verses):
         A liturgical psalm blending congregational thanksgiving (v1) with direct
         divine speech (vv2–5), theological reflection (vv6–8), and a personal vow
         (vv9–10). The "horn" (H7161, קֶרֶן) as a symbol of pride/power appears four
         times (vv4,5,10×2) — the psalm is organized around its raising and lowering.
         V8 introduces the distinctive "cup of wrath" image: the LORD holds a cup
         foaming with mixed wine that all the wicked of the earth must drain to the
         last drop. "Altaschith" (H516, אַל-תַּשְׁחֵת = "do not destroy") is the tune
         heading shared with Pss 57–59; possibly recalls David's sparing of Saul.

Ps 76 — Hymn of Victory; God the Fearsome Warrior (12 verses):
         A Zion hymn celebrating God's decisive military victory, likely associated
         with the miraculous defeat of Sennacherib's army (2 Kgs 19; Isa 37).
         Organized around the theme of divine terror (Hebrew פַּחַד, "fear/dread"):
         who can stand before God when aroused? The psalm moves from God's dwelling
         place (vv1–3) to his dominance over warriors (vv4–6) to his universal
         judgeship (vv7–9) to a call for tribute (vv10–12). V10 contains a striking
         theological assertion: even human wrath ends up praising God; the remainder
         he girds on like a weapon.

=== Superscriptions ===

Following the convention established in PSA-1 through PSA-12a, superscription text is
merged into v1 of each psalm, separated from the verse body by a blank line in T tier.

Ps 73: "A Psalm of Asaph" — no performance designation. In L/M written at the front.
Ps 74: "Maschil of Asaph" — maskil (H4905) = an instructional or contemplative poem.
Ps 75: "To the chief Musician, Altaschith, A Psalm or Song of Asaph" — full heading.
Ps 76: "To the chief Musician on Neginoth, A Psalm or Song of Asaph" — full heading.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M; "the LORD" in T.
      Appears explicitly at Ps 75:8; Ps 76:11. Both psalms are within the Elohistic
      Psalter where YHWH is less frequent, but these occurrences are genuine.

H430  (אֱלֹהִים, Elohim): "God" in all tiers throughout all four psalms.
      This is the dominant divine address in the Asaph/Elohistic collection.

H136  (אֲדֹנָי, Adonai): "Lord" (capital-L, not small-caps LORD) in all tiers.
      Does not appear in Pss 73–76 except as part of the compound Adonai-YHWH.

H3069 (יְהוִה, YHWH with Adonai vowels): Appears at Ps 73:28 following H136 (Adonai),
      forming the compound divine title "Adonai YHWH." Convention: "Lord GOD" in L/M
      (capital L + small-caps GOD = the standard English rendering of אֲדֹנָי יְהוִה),
      "the Lord GOD" in T tier.

H2617 (חֶסֶד, hesed): "steadfast love" in all tiers — MKT standard.
      Not a prominent term in Pss 73–76; does not appear as a key word.

H5542 (סֶלָה, selah): Retained as "Selah" appended to verse end throughout.
      Appears at: Ps 73:— (none); Ps 74:— (none in interlinear); Ps 75:3; Ps 76:3,9.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M; varies in T depending on context.
      Key occurrences: Ps 73:21 ("my soul / inner being"); Ps 74:19 ("soul of your dove"
      = the life/community of the congregation — rendered "community" in M/T to avoid
      the oddity of a dove having a "soul" in English).

H7161 (קֶרֶן, qeren, "horn"): "horn" in all tiers at Ps 75:4,5,10. The horn is the
      standard Hebrew metaphor for power, pride, and vindication. Preserving "horn" in
      all tiers keeps the four-fold repetition's literary impact intact.

H7307 (רוּחַ, ruach): Appears at Ps 76:12 as "spirit of princes" — not the divine
      Spirit here but the breath/pride/spirit of human rulers. Rendered "spirit" in L/M;
      "proud breath" in T to surface the deflation implicit in God "cutting it off."

H4720 (מִקְדָּשׁ/מִקְדְּשֵׁי, miqdash/miqdashei, "sanctuary/sanctuaries"): The pivotal
      word in Ps 73:17. The Hebrew may be plural ("sanctuaries of God" or "sacred courts
      of God"). Rendered "sanctuary of God" in L (singular, following traditional
      rendering), "the sanctuary of God" in M, "the sacred courts of God" in T (to
      acknowledge the possible plural and the sense of the temple precinct as a whole).

H4905 (מַשְׂכִּיל, maskil): "Maschil" in L (traditional transliteration), "Maskil" in M/T
      (modern scholarly form). Denotes an instructional or contemplative psalm — left
      untranslated per convention, as its exact meaning is uncertain.

H1254 (בָּרָא, bara): "created/made" — not a contested term here.

H389  (אַךְ, akh, "surely/truly/only"): At Ps 73:1 rendered "Truly" in L/M, "Yes, truly"
      in T — the thesis statement that frames the whole psalm. At Ps 73:13 rendered
      "All in vain" (though akh here is better served by the following לְרִיק = "for
      nothing") — see v13 note below. At Ps 73:18 "Surely" in L/M, "You have placed"
      in T (where the certainty is implicit). At Ps 75:3 "I bear up" = the adverb is
      embedded in the verb context.

H7385 (רִיק, riq, "emptiness/in vain"): At Ps 73:13 this word — not akh — carries the
      "in vain" sense. Rendered "in vain" in L, "for nothing" in M, makes the T's
      rhetorical question ("What was the point of...?") natural.

"Leviathan" (H3882): At Ps 74:14 the word is a proper name for the chaos-sea-monster
      of ancient cosmology; retained as "Leviathan" in all tiers. The "many heads" are
      a standard motif (cf. Ugaritic Ba'al cycle); do not collapse to singular.

"Turtledove" (H8449): At Ps 74:19 the congregation is called God's "turtledove" —
      a tender diminutive for a vulnerable, beloved community. Rendered "your dove" in
      L/M; T expands slightly: "your dove — your congregation" to make the image clear.

=== OT echoes and NT connections ===

- Ps 73:17 "I went into the sanctuary" → Heb 4:14–16 (entering the true sanctuary);
  the spatial-spiritual movement from confusion to clarity anticipates the NT motif of
  access to God's presence as the source of understanding.
- Ps 73:24 "afterward you will receive me to glory" → 1 Cor 15:43; John 17:24 —
  one of the clearest OT hints at resurrection/glorification, though the Hebrew is
  ambiguous ("take me with honor" could mean escorting a king or exalting after death).
- Ps 73:25 "Whom have I in heaven but you?" → John 6:68 (Peter: "To whom shall we go?
  You have the words of eternal life") — both express radical exclusive dependence.
- Ps 73:26 "God is the strength of my heart and my portion forever" → Phil 4:7,19;
  Rev 21:3 — God as "portion" (H2506) = the inheritance-share language of the Levites
  (Num 18:20; Deut 10:9), applied now to every believer's relationship with God.
- Ps 74:1-2 destruction of the sanctuary → Rev 11:1-2 (measuring the temple);
  the national lament pattern of this psalm resurfaces in apocalyptic literature.
- Ps 74:14 "Leviathan" → Rev 12:3; 13:1 — the sea monster with multiple heads;
  also Isa 27:1 and Job 41. Apocalyptic literature draws directly on this imagery.
- Ps 75:8 "cup of wrath" → Rev 14:10; 16:19; Matt 26:39 (Gethsemane) — the cup the
  wicked drain in Ps 75 becomes the cup Jesus asks to pass from him. Profound reversal.
- Ps 76:10 "the wrath of man shall praise you" → Rom 8:28 (all things work for good
  for those who love God) — the theological claim that even hostile actions end up
  serving God's purposes.

=== Aspect and tense notes ===

Ps 73: The psalm moves through a narrative arc — past crisis (vv2–16, past tense),
pivotal event (v17, ingressive past "until I entered"), and resolved present (vv23–28,
present and future). The perfect verbs of the opening confession (v1 "God is good")
state an unchanging truth rendered with English simple present. The despair section
(vv2–16) uses mostly past tense. The sanctuary section (vv17–20) continues past tense
but builds toward present confidence. Vv23–28 are entirely present/future: "I am
continually with you," "you hold me," "you guide me," "afterward you will receive me."

Ps 74: Predominantly past tense in the lament description (vv3–9, what the enemy did),
then present and imperative in the appeal section (vv18–23). The creation recital
(vv12–17) uses past tense for accomplished historical-cosmic events.

Ps 75: God's speech (vv2–5) is future/present — "I will judge," "I bear up" — the
divine Judge speaking about what he will do and what he presently holds. The psalmist's
section (vv9–10) shifts to first person future vow.

Ps 76: Mostly descriptive historical past of the great victory (vv3–6), then present
attribute (vv7–9), then imperative and future (vv10–12). The "dead sleep" of the
warriors (v5) is a dramatic past tense perfect.
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
  "73": {
    "1": {
      "L": "A Psalm of Asaph. Truly God is good to Israel, even to such as are of a clean heart.",
      "M": "A Psalm of Asaph. Truly God is good to Israel, to those who are pure in heart.",
      "T": "A Psalm of Asaph.\n\nTruly, God is good to Israel —\nto all who are pure in heart."
    },
    "2": {
      "L": "But as for me, my feet had well nigh slipped; my steps were almost gone.",
      "M": "But as for me, my feet nearly slipped; my steps almost gave way.",
      "T": "As for me — my feet nearly slipped;\nI came within a step of going down."
    },
    "3": {
      "L": "For I was envious at the arrogant, when I saw the prosperity of the wicked.",
      "M": "For I was envious of the arrogant when I saw how the wicked prosper.",
      "T": "I was eaten up with envy of the arrogant —\nI couldn't stop watching the wicked thrive."
    },
    "4": {
      "L": "For there are no bands in their death; and their strength is firm.",
      "M": "For they have no anguish in their death; their bodies are sleek and strong.",
      "T": "They die without a struggle;\ntheir bodies are sleek and powerful to the end."
    },
    "5": {
      "L": "They are not in trouble as other men; neither are they plagued like other men.",
      "M": "They are not in trouble like other people; they are not plagued like the rest of mankind.",
      "T": "They don't suffer the way ordinary people do;\nthey escape the troubles that wear everyone else down."
    },
    "6": {
      "L": "Therefore pride compasseth them about as a chain; violence covereth them as a garment.",
      "M": "Therefore pride adorns them like a necklace; violence wraps them like a garment.",
      "T": "So they wear their pride like a necklace\nand drape themselves in violence like a robe."
    },
    "7": {
      "L": "Their eyes stand out with fatness; they have more than heart could wish.",
      "M": "Their eyes bulge with prosperity; the desires of their heart exceed all bounds.",
      "T": "Their eyes bulge with excess;\nthe schemes of their hearts know no limit."
    },
    "8": {
      "L": "They are corrupt, and speak wickedly concerning oppression; they speak loftily.",
      "M": "They scoff and speak with malice; they talk of oppression with arrogance.",
      "T": "They mock others and plot cruelty;\ntheir boasting climbs all the way to heaven."
    },
    "9": {
      "L": "They set their mouth against the heavens, and their tongue walketh through the earth.",
      "M": "They direct their mouths against the heavens, and their tongue ranges across the earth.",
      "T": "They point their mouths straight at heaven\nand strut their tongues across the whole earth."
    },
    "10": {
      "L": "Therefore his people return hither; and waters of a full cup are wrung out to them.",
      "M": "Therefore people keep returning to them, and a full cup of water is drained by them.",
      "T": "And so people keep flocking after them,\ndrinking up everything they offer."
    },
    "11": {
      "L": "And they say, How doth God know? and is there knowledge in the Most High?",
      "M": "They say, 'How can God know? Does the Most High have knowledge?'",
      "T": "And they ask: 'Can God actually see this?\nDoes the Most High know anything at all?'"
    },
    "12": {
      "L": "Behold, these are the ungodly, who prosper in the world; they increase in riches.",
      "M": "See — these are the wicked, always at ease, growing in wealth.",
      "T": "Just look at them — the wicked —\ncoasting through life without a care,\npiling up wealth all the while."
    },
    "13": {
      "L": "Verily, I have cleansed my heart in vain, and washed my hands in innocency.",
      "M": "Surely I have kept my heart clean for nothing, and washed my hands in innocence in vain.",
      "T": "What was the point of keeping my heart clean?\nOf washing my hands in innocence —\nif it all amounts to nothing?"
    },
    "14": {
      "L": "For all the day long have I been plagued, and chastened every morning.",
      "M": "For all day long I have been afflicted, and punishment comes every morning.",
      "T": "Every day I have been beaten down;\nevery morning brings another round of suffering."
    },
    "15": {
      "L": "If I say, I will speak thus; behold, I should offend against the generation of thy children.",
      "M": "If I had said, 'I will speak this way,' I would have betrayed the generation of your children.",
      "T": "But if I had spoken these thoughts aloud,\nI would have betrayed your people —\nthe whole community of your children."
    },
    "16": {
      "L": "When I thought to know this, it was too painful for me;",
      "M": "When I tried to make sense of all this, it was a torment before my eyes —",
      "T": "When I tried to work this out on my own,\nit was nothing but confusion and pain —"
    },
    "17": {
      "L": "Until I went into the sanctuary of God; then understood I their end.",
      "M": "until I entered the sanctuary of God; then I grasped their end.",
      "T": "until I entered the sacred courts of God.\nThere I finally understood\nwhat awaits them in the end."
    },
    "18": {
      "L": "Surely thou didst set them in slippery places; thou castedst them down into destruction.",
      "M": "Surely you have placed them on slippery ground; you cast them down to desolation.",
      "T": "You have placed them on slippery ground,\npoised to cast them headlong into ruin."
    },
    "19": {
      "L": "How are they brought into desolation in a moment; they are utterly consumed with terrors.",
      "M": "How suddenly they are destroyed, completely swept away by terrors!",
      "T": "In a single moment they collapse —\nswept away, annihilated by sheer terror!"
    },
    "20": {
      "L": "As a dream when one awaketh; so, O Lord, when thou awakest, thou shalt despise their image.",
      "M": "Like a dream that vanishes when one awakes, so when you arise, O Lord, you despise their fleeting form.",
      "T": "They are like a dream that dissolves the moment you wake —\nwhen you arise, O Lord,\ntheir whole existence fades like smoke."
    },
    "21": {
      "L": "Thus my heart was grieved, and I was pricked in my reins:",
      "M": "When my heart was embittered and I was pierced in my inner being —",
      "T": "There was a time when my heart was bitter with resentment,\nwhen I felt stabbed through —"
    },
    "22": {
      "L": "So foolish was I, and ignorant; I was as a beast before thee.",
      "M": "I was brutish and ignorant; I was no better than an animal before you.",
      "T": "I was nothing but a brute, senseless as a beast in your presence."
    },
    "23": {
      "L": "Nevertheless I am continually with thee; thou hast holden me by my right hand.",
      "M": "Yet I am always with you; you hold me by my right hand.",
      "T": "And yet — I am always with you;\nyou hold me by the right hand."
    },
    "24": {
      "L": "Thou shalt guide me with thy counsel, and afterward receive me to glory.",
      "M": "You guide me with your counsel, and afterward you will receive me into glory.",
      "T": "You guide me with your wisdom,\nand afterward you will take me up into glory."
    },
    "25": {
      "L": "Whom have I in heaven but thee? And there is none upon earth that I desire beside thee.",
      "M": "Whom in heaven do I have but you? And on earth there is nothing I desire besides you.",
      "T": "What do I have in heaven but you?\nAnd on earth — there is nothing else I want."
    },
    "26": {
      "L": "My flesh and my heart faileth; but God is the strength of my heart and my portion for ever.",
      "M": "My flesh and my heart may fail, but God is the strength of my heart and my portion forever.",
      "T": "My body wastes away;\nmy heart gives out —\nbut God is the rock of my heart,\nmy portion and inheritance forever."
    },
    "27": {
      "L": "For lo, they that are far from thee shall perish; thou hast destroyed all them that go a whoring from thee.",
      "M": "For behold, those who are far from you will perish; you destroy all who are unfaithful to you.",
      "T": "Those who wander far from you will be destroyed;\nyou cut off everyone who breaks faith with you."
    },
    "28": {
      "L": "But it is good for me to draw near to God; I have put my trust in the Lord GOD, that I may declare all thy works.",
      "M": "But as for me, it is good to be near God; I have made the Lord GOD my refuge, that I may declare all your works.",
      "T": "But for me, drawing near to God is my greatest good —\nI have made the Lord GOD my shelter,\nso I can tell of all that he has done."
    }
  },
  "74": {
    "1": {
      "L": "Maschil of Asaph. O God, why hast thou cast us off for ever? Why doth thine anger smoke against the sheep of thy pasture?",
      "M": "A Maskil of Asaph. O God, why have you rejected us forever? Why does your anger smolder against the sheep of your pasture?",
      "T": "A Maskil of Asaph.\n\nO God, why have you abandoned us forever?\nWhy does your anger keep smoldering\nagainst the flock you shepherd?"
    },
    "2": {
      "L": "Remember thy congregation, which thou hast purchased of old; the rod of thine inheritance, which thou hast redeemed; this mount Zion, wherein thou hast dwelt.",
      "M": "Remember your congregation, which you acquired long ago, the tribe of your inheritance, which you redeemed — Mount Zion, where you have made your dwelling.",
      "T": "Remember the people you claimed for yourself long ago —\nthe community you redeemed to be your inheritance.\nRemember Mount Zion, where you chose to dwell."
    },
    "3": {
      "L": "Lift up thy feet unto the perpetual desolations; even all that the enemy hath done wickedly in the sanctuary.",
      "M": "Make your way to the perpetual ruins; the enemy has wrought complete destruction in the sanctuary.",
      "T": "Come and see what is left —\ndesolation that stretches on without end.\nSee everything the enemy did to your sanctuary."
    },
    "4": {
      "L": "Thine enemies roar in the midst of thy congregations; they set up their ensigns for signs.",
      "M": "Your enemies have roared in the midst of your assembly; they have set up their own banners as signs.",
      "T": "Your enemies roared right inside your sacred courts;\nthey planted their own battle flags\nwhere yours had stood."
    },
    "5": {
      "L": "A man was famous as he lifted up axes upon the thick trees.",
      "M": "They were like men wielding axes to fell a dense forest.",
      "T": "They swung their axes like woodsmen in a thicket,\nhacking through everything in sight."
    },
    "6": {
      "L": "But now they break down the carved work thereof at once with axes and hammers.",
      "M": "All its carved paneling they smashed apart with axes and hammers.",
      "T": "The carved woodwork — all of it —\nthey shattered with axes and hammers."
    },
    "7": {
      "L": "They have cast fire into thy sanctuary; they have defiled the dwelling place of thy name by casting it to the ground.",
      "M": "They set your sanctuary on fire; they defiled the dwelling place of your name by pulling it down to the ground.",
      "T": "They burned your sanctuary to the ground\nand dropped the tabernacle of your name in the dust."
    },
    "8": {
      "L": "They said in their hearts, Let us destroy them together; they have burned up all the synagogues of God in the land.",
      "M": "They said in their hearts, 'We will crush them all together'; they burned down every meeting place of God throughout the land.",
      "T": "'We will wipe them out completely,' they said —\nand they burned down every place of worship in the land."
    },
    "9": {
      "L": "We see not our signs; there is no more any prophet; neither is there among us any that knoweth how long.",
      "M": "We see none of our signs; there is no longer a prophet; and none of us knows how long this will last.",
      "T": "We see no sign from you anywhere.\nNo prophet speaks.\nNone of us knows when this will end."
    },
    "10": {
      "L": "O God, how long shall the adversary reproach? Shall the enemy blaspheme thy name for ever?",
      "M": "How long, O God, will the enemy mock you? Is the adversary to revile your name forever?",
      "T": "How long, O God — how long?\nWill the enemy go on mocking you?\nWill they blaspheme your name forever?"
    },
    "11": {
      "L": "Why withdrawest thou thy hand, even thy right hand? Pluck it out of thy bosom.",
      "M": "Why do you hold back your hand, your right hand? Draw it out from under your garment and act!",
      "T": "Why are you keeping your hand restrained —\nyour right hand tucked away?\nPull it out. Act."
    },
    "12": {
      "L": "For God is my King of old, working salvation in the midst of the earth.",
      "M": "Yet God my King is from of old, bringing salvation in the midst of the earth.",
      "T": "And yet — God has been my King since ancient days,\nwinning victories across the whole earth."
    },
    "13": {
      "L": "Thou didst divide the sea by thy strength; thou brakest the heads of the dragons in the waters.",
      "M": "You split the sea apart by your power; you shattered the heads of the sea monsters on the waters.",
      "T": "You split the sea open by your power;\nyou crushed the heads of the sea-dragons on the waters."
    },
    "14": {
      "L": "Thou brakest the heads of leviathan in pieces, and gavest him to be meat to the people inhabiting the wilderness.",
      "M": "You crushed the many heads of Leviathan; you gave his carcass as food for the creatures of the wilderness.",
      "T": "You broke every head of Leviathan\nand fed his remains to the desert creatures."
    },
    "15": {
      "L": "Thou didst cleave the fountain and the flood; thou driedst up mighty rivers.",
      "M": "You split open springs and streams; you dried up the ever-flowing rivers.",
      "T": "You split the earth to release springs;\nyou dried up rivers that had flowed without ceasing."
    },
    "16": {
      "L": "The day is thine, the night also is thine; thou hast prepared the light and the sun.",
      "M": "The day belongs to you; the night also is yours; you established the light and the sun.",
      "T": "The day is yours;\nthe night belongs to you as well —\nyou set the sun and all its light in place."
    },
    "17": {
      "L": "Thou hast set all the borders of the earth; thou hast made summer and winter.",
      "M": "You have fixed all the boundaries of the earth; you have made both summer and winter.",
      "T": "You drew the boundaries of every land;\nyou shaped the seasons — summer and winter alike."
    },
    "18": {
      "L": "Remember this, that the enemy hath reproached, O LORD, and that the foolish people have blasphemed thy name.",
      "M": "Remember this, O LORD: the enemy has mocked, and a foolish people has reviled your name.",
      "T": "Remember all of this, O LORD —\nhow the enemy has mocked you,\nhow this foolish people has reviled your name."
    },
    "19": {
      "L": "O deliver not the soul of thy turtledove unto the multitude of the wicked; forget not the congregation of thy poor for ever.",
      "M": "Do not hand over your dove to the pack of enemies; do not forget the community of your poor forever.",
      "T": "Do not abandon your dove — your congregation —\nto the pack of predators.\nDo not forget your afflicted people forever."
    },
    "20": {
      "L": "Have respect unto the covenant; for the dark places of the earth are full of the habitations of cruelty.",
      "M": "Look to your covenant, for the dark corners of the land are filled with dens of violence.",
      "T": "Look to your covenant!\nEvery dark corner of this land\nis crammed full of brutal violence."
    },
    "21": {
      "L": "O let not the oppressed return ashamed; let the poor and needy praise thy name.",
      "M": "Do not let the oppressed be turned away in shame; let the poor and needy praise your name.",
      "T": "Let not the oppressed be turned away in disgrace —\nlet the poor and needy praise your name instead."
    },
    "22": {
      "L": "Arise, O God, plead thine own cause; remember how the foolish man reproacheth thee daily.",
      "M": "Rise up, O God, and defend your cause; remember how fools mock you every single day.",
      "T": "Rise up, O God — defend your own cause!\nRemember how the fool mocks you day after day."
    },
    "23": {
      "L": "Forget not the voice of thine enemies; the tumult of those that rise up against thee increaseth continually.",
      "M": "Do not forget the clamor of your enemies; the uproar of those who defy you rises without ceasing.",
      "T": "Do not forget the roar of your enemies —\nthe clamor of those who rise against you\nnever stops rising."
    }
  },
  "75": {
    "1": {
      "L": "To the chief Musician, Altaschith, A Psalm or Song of Asaph. We give thanks unto thee, O God, we give thanks; for that thy name is near thy wondrous works declare.",
      "M": "To the choirmaster. According to 'Do Not Destroy.' A Psalm. A Song of Asaph. We give thanks to you, O God; we give thanks, for your name is near; we declare your wondrous deeds.",
      "T": "To the worship leader. 'Do Not Destroy.' A Psalm. A Song of Asaph.\n\nWe give you thanks, O God —\nwe give you thanks!\nFor your name is near;\nwe declare your wondrous works."
    },
    "2": {
      "L": "When I shall receive the congregation, I will judge uprightly.",
      "M": "When I choose the appointed time, I will judge with perfect equity.",
      "T": "When I choose the moment,\nI will dispense justice without favor."
    },
    "3": {
      "L": "The earth and all the inhabitants thereof are dissolved; I bear up the pillars of it. Selah.",
      "M": "When the earth totters and all its people with it, it is I who hold its pillars firm. Selah.",
      "T": "When the whole earth trembles\nand every person on it staggers —\nI am the one who holds the pillars steady. Selah."
    },
    "4": {
      "L": "I said unto the fools, Deal not foolishly; and to the wicked, Lift not up the horn.",
      "M": "I say to the arrogant, 'Stop your boasting,' and to the wicked, 'Do not raise your horn.'",
      "T": "I tell the arrogant: 'Stop strutting around!'\nAnd to the wicked: 'Put that horn down.'"
    },
    "5": {
      "L": "Lift not up your horn on high; speak not with a stiff neck.",
      "M": "Do not raise your horn on high; do not speak with an arrogant neck.",
      "T": "Do not raise your horn against heaven;\ndo not speak with such stiff-necked pride."
    },
    "6": {
      "L": "For promotion cometh neither from the east, nor from the west, nor from the south.",
      "M": "For advancement comes neither from east nor west, nor from the wilderness of the south.",
      "T": "Power does not rise from east or west,\nnor does it surge up out of the desert wilderness —"
    },
    "7": {
      "L": "But God is the judge; he putteth down one, and setteth up another.",
      "M": "but God is the judge; he brings one person down and raises another up.",
      "T": "it is God alone who judges,\nbringing one low and raising another high."
    },
    "8": {
      "L": "For in the hand of the LORD there is a cup, and the wine is red; it is full of mixture; and he poureth out of the same; but the dregs thereof, all the wicked of the earth shall wring them out, and drink.",
      "M": "For in the hand of the LORD there is a cup of foaming wine, well mixed; he pours it out, and all the wicked of the earth shall drain it to the very dregs.",
      "T": "For in the LORD's hand there is a cup\nbrimming with wine, foaming and spiced —\nhe pours it out,\nand all the wicked of the earth\nshall drain it to the last bitter drop."
    },
    "9": {
      "L": "But I will declare for ever; I will sing praises to the God of Jacob.",
      "M": "But as for me, I will declare this forever; I will sing praises to the God of Jacob.",
      "T": "But as for me — I will praise him forever;\nI will sing to the God of Jacob."
    },
    "10": {
      "L": "All the horns of the wicked also will I cut off; but the horns of the righteous shall be exalted.",
      "M": "All the horns of the wicked I will cut down, but the horns of the righteous shall be lifted high.",
      "T": "Every horn the wicked have raised —\nI will cut them all down.\nBut the horns of the righteous\nwill rise."
    }
  },
  "76": {
    "1": {
      "L": "To the chief Musician on Neginoth, A Psalm or Song of Asaph. In Judah is God known; his name is great in Israel.",
      "M": "To the choirmaster, with stringed instruments. A Psalm. A Song of Asaph. God is known in Judah; his name is great in Israel.",
      "T": "To the worship leader, with stringed instruments. A Psalm. A Song of Asaph.\n\nGod has made himself known in Judah;\nhis name is great across all Israel."
    },
    "2": {
      "L": "In Salem also is his tabernacle, and his dwelling place in Zion.",
      "M": "His tabernacle is in Salem; his dwelling place is in Zion.",
      "T": "His tent is pitched in Salem;\nhis home is Zion."
    },
    "3": {
      "L": "There brake he the arrows of the bow, the shield, and the sword, and the battle. Selah.",
      "M": "There he shattered the flashing arrows, the shield, the sword, and all the weapons of war. Selah.",
      "T": "There — right there — he shattered the arrows in flight,\nthe shield, the sword,\nevery weapon of war. Selah."
    },
    "4": {
      "L": "Thou art more glorious and excellent than the mountains of prey.",
      "M": "You are glorious and majestic, more than the everlasting mountains of plunder.",
      "T": "How glorious you are —\nmore majestic than mountains heaped with ancient spoil."
    },
    "5": {
      "L": "The stouthearted are spoiled; they have slept their sleep; and none of the men of might have found their hands.",
      "M": "The valiant warriors have been stripped of their plunder; they have fallen into the sleep of death; not one soldier could lift a hand.",
      "T": "The mighty warriors were plundered;\nthey have fallen into the sleep of death —\nnot one soldier could raise a hand."
    },
    "6": {
      "L": "At thy rebuke, O God of Jacob, both the chariot and horse are cast into a dead sleep.",
      "M": "At your rebuke, O God of Jacob, both chariot and horse fell into a dead sleep.",
      "T": "A single word of rebuke from the God of Jacob —\nand horse and chariot fell into death's deep sleep."
    },
    "7": {
      "L": "Thou, even thou, art to be feared; and who may stand in thy sight when once thou art angry?",
      "M": "But you — you alone are to be feared. Who can stand before you when your anger is kindled?",
      "T": "You — you are the one to be feared.\nWho could stand in your presence\nwhen your anger blazes?"
    },
    "8": {
      "L": "Thou didst cause judgment to be heard from heaven; the earth feared, and was still,",
      "M": "From heaven you pronounced judgment; the earth feared and stood still —",
      "T": "You spoke judgment from heaven;\nthe earth heard and went utterly silent —"
    },
    "9": {
      "L": "When God arose to judgment, to save all the meek of the earth. Selah.",
      "M": "when God arose to judge, to save all the humble of the earth. Selah.",
      "T": "when God rose to pronounce judgment\nand rescue all the meek of the earth. Selah."
    },
    "10": {
      "L": "Surely the wrath of man shall praise thee; the remainder of wrath shalt thou restrain.",
      "M": "Surely human fury will bring you praise; whatever wrath remains you will restrain.",
      "T": "Even human rage ends up praising you;\nwhatever fury is left over,\nyou gird on like a weapon."
    },
    "11": {
      "L": "Vow, and pay unto the LORD your God; let all that be round about him bring presents unto him that ought to be feared.",
      "M": "Make vows to the LORD your God and keep them; let all the surrounding nations bring tribute to the one who is to be feared.",
      "T": "Make your vows to the LORD your God and keep them;\nlet every nation around him bring tribute\nto the one who inspires such dread."
    },
    "12": {
      "L": "He shall cut off the spirit of princes; he is terrible to the kings of the earth.",
      "M": "He cuts off the spirit of princes; he is fearsome to the kings of the earth.",
      "T": "He strips the proud breath from princes;\nhe is terrifying to every king on earth."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 73–76 written.')

if __name__ == '__main__':
    main()
