"""
MKT Psalms chapters 89–90 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-89-90.py

=== Overview of this unit ===

Ps 89 (52 v) — A Maskil of Ethan the Ezrahite. The longest and most theologically
    complex of the royal psalms, and the climactic psalm of Book III (Pss 73–89). The
    psalm moves through three massive movements:

    vv1-18:  PRAISE — the psalmist vows eternal song of the LORD's chesed and emunah
        (steadfast love and faithfulness), grounding that praise in God's cosmic
        sovereignty (vv5-13) and the moral order of his throne (v14).

    vv19-37: COVENANT — the Davidic covenant oath quoted at length. God's first-person
        pledges to David (vv19-37): 'I have found David my servant... I will establish
        his seed forever... I have sworn by my holiness.' Seven times the word
        chesed or emunah appears in this section — the covenant is soaked in them.

    vv38-51: LAMENT — the devastating collapse. 'But you have cast off and rejected;
        you are wroth with your anointed.' The section uses the same covenant
        vocabulary in reverse: where God had promised exaltation, the king is
        humiliated; where God had promised to drive back enemies, enemies now prevail.
        The pivot word is the emphatic 'you' (attah) at v38 — the same God who swore
        the oath is now, apparently, its breaker.

    v52:     DOXOLOGY — the closing doxology of Book III (Pss 73–89), not part of
        Psalm 89 per se. 'Blessed be the LORD forever! Amen and Amen.'

    KEY TERM: chesed (H2617) appears 7 times in Ps 89 (vv1, 2, 14, 24, 28, 33, 49).
    emunah (H530, faithfulness) appears 7 times (vv1, 2, 5, 8, 24, 33, 37). The
    entire psalm is a meditation on whether these twin covenant qualities hold when
    everything around them seems to have collapsed.

    Rahab (v10): Not Rahab the harlot of Jericho, but the mythic chaos-dragon, a
    symbol of primordial chaos and of Egypt (cf. Isa 51:9; Job 26:12). The crushing
    of Rahab is a creation-theology image: the LORD conquered chaos at the beginning
    and can do so again.

    vv3-4: God's first-person covenant speech embedded in the psalm without formal
    quotation markers in the Hebrew. Rendered in quotation marks to signal the voice
    shift. The covenant language is the same as the Davidic covenant in 2 Samuel 7.

Ps 90 (17 v) — A Prayer of Moses the man of God. The only psalm attributed to Moses
    in the Psalter, and deliberately placed as the first psalm of Book IV (Pss 90–106).
    Its placement immediately after the collapse described in Ps 89 is intentional:
    the loss of the Davidic monarchy sends the community back to an even older anchor —
    Moses, the Exodus, and the eternal God who preceded all human institutions.

    Structure:
    vv1-2:   God's eternal nature — our dwelling place across all generations; from
        everlasting to everlasting he is God (before mountains, before creation).
    vv3-6:   Human transience — God returns man to dust; a thousand years = a night
        watch; we are like grass, springing up and withering in a single day.
    vv7-11:  The cause: our sins under God's wrath; our iniquities laid bare in the
        light of his face; our years as a sigh.
    vv12-17: Prayer for reorientation — teach us to number our days; satisfy us with
        chesed; let your work appear; establish the work of our hands.

    v12 is one of the most cited verses in the Psalter: 'Teach us to number our days
    that we may gain a heart of wisdom.' The wisdom tradition (Proverbs, Job, Qohelet)
    threads through this verse: knowing the brevity of life is the beginning of wisdom.

    v4 is an OT anchor for the NT's 'with the Lord a day is as a thousand years, and
    a thousand years as a day' (2 Pet 3:8). The comparison is not mathematical but
    qualitative: God's relationship to time is categorically different from ours.

=== Contested-term decisions ===

H2617 (חֶסֶד, chesed): "steadfast love" in L/M throughout. In T: "steadfast love" with
    occasional variation in address forms ("your steadfast love"). The term dominates
    Ps 89; reducing it to "love" or "mercy" loses the covenantal-loyalty dimension.
    Consistent with all prior Psalms scripts.

H530 (אֱמוּנָה, emunah): "faithfulness" in all tiers. The abstract noun of the root
    aman (to be firm, reliable). Paired with chesed throughout Ps 89 as the two
    defining qualities of God's character. Appears at vv1, 2, 5, 8, 24, 33, 37.

H571 (אֶמֶת, emet): "faithfulness" in L/M at Ps 89:14, 49 where it pairs with chesed.
    Rendered "truth" in T at v14 to distinguish from emunah and preserve the slight
    nuance (emet = reliability/truth; emunah = steadfast faithfulness).

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M. In T: "LORD" or
    "the LORD" per cadence. Consistent with all prior Psalms scripts.

H136 (אֲדֹנָי, Adonai): "Lord" (not LORD) in L/M/T. The sovereign title. Appears at
    Ps 89:49, 50; Ps 90:1, 17 (and implied in Ps 90:17 "Lord our God").

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Consistent throughout Psalms scripts.

H410 (אֵל, El): "God" in all tiers. Shorter divine title used frequently in Ps 89.

H5945 (עֶלְיוֹן, Elyon): "Most High" in all tiers. Appears at Ps 89:27. Consistent
    with all prior Psalms scripts.

H6662 (צַדִּיק, tsadiq) / H6664 (צֶדֶק, tsedeq): "righteousness" in L/M. In T:
    "righteousness" — the judicial-relational quality of right order. At Ps 89:14 it
    pairs with mishpat (justice/judgment) as co-foundations of God's throne.

H4941 (מִשְׁפָּט, mishpat): "justice" in L/M. In T: "justice" at Ps 89:14.

H5315 (נֶפֶשׁ, nefesh): "soul" in L; "life" or "soul" in M/T depending on context.
    At Ps 89:48: "his soul from the hand of Sheol" — nefesh = embodied self, the
    whole person facing death; rendered "soul" in L, "life" in M, "his very life"
    in T.

H5542 (סֶלָה, Selah): Retained as "Selah" in all tiers. Appears at Ps 89:4, 37, 45, 48.

H4905 (מַשְׂכִּיל, Maskil): Superscription marker for Ps 89. "A Maskil" in L;
    "A contemplative poem" in M; "A teaching poem" in T. Consistent with Ps 78.

H7723 (שָׁוְא, shav): "in vain / futility / emptiness" at Ps 89:47. Rendered
    "futility" in L/M; "emptiness" in T.

H7585 (שְׁאוֹל, Sheol): Retained as "Sheol" in L; "the grave" in M; "the grave" in T
    at Ps 89:48. The underworld of the dead — not a place of conscious torment in OT
    usage but the realm of the shades where life's vitality is absent.

H5769 (עוֹלָם, olam): "forever / everlasting" in all tiers. The primary Hebrew word
    for indefinite duration / age-to-come. At Ps 90:2 the doubled form "from
    everlasting to everlasting" (me-olam ad-olam) = absolute eternity.

=== Textual and interpretive notes ===

Ps 89:3-4 — God's covenant speech embedded in the psalm. The Hebrew lacks explicit
    quotation markers (as is common in biblical poetry), but the first-person divine
    voice is unmistakable: 'I have made a covenant... I have sworn to David my servant.'
    Rendered in quotation marks in all tiers to signal the voice shift.

Ps 89:10 — Rahab: The mythic chaos-monster / Egypt symbol, not Rahab the harlot.
    See Isa 51:9 ('Was it not you who cut Rahab in pieces, who pierced the dragon?')
    and Job 26:12. The crushing of Rahab is a creation-mythology claim: YHWH defeated
    chaos at the foundation of the world.

Ps 89:14 — 'Righteousness and justice are the foundation (mekon) of your throne.'
    The word mekon = established base, foundation-support. The divine throne rests on
    moral order. This verse is the theological center of vv5-18.

Ps 89:19 — 'To your faithful one' (hasid, H2623, singular). Could be a prophet
    (Nathan? Samuel?), or used collectively for 'your faithful servants.' Rendered
    'your faithful ones' (collective) in M/T; 'your faithful one' in L.

Ps 89:38 — The pivot. The emphatic pronoun attah ('you, yourself') opens the lament:
    'But YOU have cast off and rejected.' The contrast with Ps 78:38 ('But HE, full
    of compassion') is probably deliberate — there God's grace absorbed the covenant
    failure; here the failure seems to overwhelm even that grace. The psalm ends
    without resolution, leaving the cry hanging in the air. Book IV (beginning at Ps 90)
    is the Psalter's answer.

Ps 89:52 — Closing doxology of Book III (Pss 73–89), not part of Psalm 89's content.
    'Blessed be the LORD forever! Amen and Amen.' Each of the Psalter's five books
    closes with such a doxology.

Ps 90:1 — 'Dwelling place' (ma'on, H4583): a fixed abode, a refuge. The claim that
    God is Israel's dwelling place precedes the creation of the world (v2). This is
    the foundation: before there was anything to live in, God was home.

Ps 90:4 — 'A watch in the night': A four-hour shift, one quarter of the night. The
    comparison implies that even the longest human span — a millennium — goes by
    for God as quickly as a shift of night duty. Not mathematical (1000 = 4 hours)
    but qualitative: God's experience of time is incommensurable with ours.

Ps 90:10 — 'Seventy years... eighty': The standard human lifespan in the ancient
    world. Not a precise actuarial claim but a cultural marker for a full life. The
    following phrase 'toil and grief' (aven va-yagon — H205 + H3015) is the verdict
    on what those years actually contain. The verb 'fly away' (H5774 uph) is the
    same root used of birds taking flight — life departs suddenly and naturally.

Ps 90:17 — 'The beauty/favor of the Lord' (no'am, H5278): graciousness, pleasantness,
    delight. Used of the LORD's own loveliness in Ps 27:4. The prayer is for God's own
    quality to rest on the work of human hands — transforming labor into something that
    participates in the divine beauty.

=== Aspect and tense notes ===

Ps 89 vv1-18: The psalmist uses cohortatives of resolve ('I will sing,' 'I will
    declare,' 'I will make known') and hymnic presents (God 'rules,' 'stills,' 'has
    founded'). The covenant section (vv19-37) uses Hebrew perfects of completed
    covenantal action ('I have sworn,' 'I have made,' 'I have found') — the past
    covenant decision stands.

Ps 89 vv38-51: The lament section uses perfects of completed past action — God 'has
    cast off,' 'has been wroth,' 'has renounced,' 'has defiled.' The devastation is
    described as accomplished fact. The imperfects in vv46ff. switch to ongoing
    anguished questions ('how long?' 'will you hide?').

Ps 90: The psalm alternates between hymnic indicatives describing God's eternal nature
    (vv1-2), narrative perfects of divine judgment (vv3-11), and jussive/imperative
    prayers (vv12-17). The prayer-imperatives of vv13-17 use the Piel and Hiphil
    causatives: 'satisfy us,' 'make us glad,' 'let appear,' 'establish' — all
    requesting God to act toward the community with the power he has demonstrated
    cosmically.
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
  # Psalm 89 — A Maskil of Ethan the Ezrahite: Covenant, Collapse, and Cry
  # ===========================================================================
  "89": {
    "1": {
      "L": "A Maskil of Ethan the Ezrahite. Of the steadfast love of the LORD I will sing forever; with my mouth I will declare your faithfulness to all generations.",
      "M": "A contemplative poem of Ethan the Ezrahite. I will sing of the LORD's steadfast love forever; with my mouth I will proclaim your faithfulness to every generation.",
      "T": "A teaching poem of Ethan the Ezrahite.\nOf the LORD's steadfast love I will sing — forever.\nWith my own mouth I will declare your faithfulness\nto every generation that comes after."
    },
    "2": {
      "L": "For I said, 'Steadfast love will be built up forever; your faithfulness you will establish in the very heavens.'",
      "M": "For I declared, 'Your steadfast love is built to stand forever; your faithfulness is established in the heavens themselves.'",
      "T": "I have said it:\nyour steadfast love is being built up to last forever.\nYou have fixed your faithfulness in the heavens themselves."
    },
    "3": {
      "L": "'I have made a covenant with my chosen one; I have sworn to David my servant:'",
      "M": "'I have made a covenant with my chosen one; I have sworn an oath to David my servant:'",
      "T": "'I have cut a covenant with the one I chose.\nI have sworn my oath to David — my servant:'"
    },
    "4": {
      "L": "'I will establish your offspring forever, and build your throne for all generations.' Selah",
      "M": "'I will make your line endure forever and build your throne for every generation to come.' Selah",
      "T": "'Your line will stand — forever.\nI will build your throne\nfor every generation to come.'\nSelah."
    },
    "5": {
      "L": "The heavens praise your wonders, O LORD; your faithfulness also in the assembly of the holy ones.",
      "M": "The heavens praise your wonders, O LORD; your faithfulness is declared in the congregation of the holy ones.",
      "T": "The heavens praise your wonders, LORD—\nyour faithfulness rings out\nin the assembly of the holy ones."
    },
    "6": {
      "L": "For who in the heavens can be compared to the LORD? Who among the sons of the mighty is like the LORD?",
      "M": "For who in all the heavens can be compared with the LORD? Who among the heavenly beings is like the LORD?",
      "T": "Who in all of heaven can compare to the LORD?\nAmong all the heavenly beings —\nwho is like him?"
    },
    "7": {
      "L": "God greatly to be feared in the council of the holy ones, and awesome above all who are around him.",
      "M": "A God greatly feared in the assembly of the holy ones and awesome above all who surround him.",
      "T": "He is held in awe in the council of the holy ones—\ngreat, terrifying,\nlifted above everything and everyone that circles him."
    },
    "8": {
      "L": "O LORD God of hosts, who is mighty like you, O LORD? Your faithfulness surrounds you on every side.",
      "M": "LORD God of hosts, who is as powerful as you, LORD? Your faithfulness wraps around you on every side.",
      "T": "LORD, God of the heavenly armies—\nwho is as mighty as you?\nYour faithfulness is your very atmosphere."
    },
    "9": {
      "L": "You rule the raging of the sea; when its waves rise, you still them.",
      "M": "You govern the surging sea; when its waves rear up, you calm them.",
      "T": "You hold the raging sea in check.\nWhen the waves rise and rear up—\nyou still them."
    },
    "10": {
      "L": "You crushed Rahab like one who is slain; with your strong arm you scattered your enemies.",
      "M": "You crushed Rahab like a slaughtered carcass; with your mighty arm you scattered your enemies.",
      "T": "You crushed Rahab like a body laid out in defeat—\nthe chaos-dragon, the old enemy.\nWith the full strength of your arm\nyou scattered everyone who opposed you."
    },
    "11": {
      "L": "The heavens are yours; the earth also is yours; the world and all that fills it — you have founded them.",
      "M": "The heavens belong to you; the earth also is yours; you founded the world and everything in it.",
      "T": "The heavens are yours.\nThe earth is yours.\nYou laid the foundations of the world\nand filled it with life."
    },
    "12": {
      "L": "The north and the south — you created them; Tabor and Hermon rejoice in your name.",
      "M": "North and south — you created them; Tabor and Hermon sing for joy in your name.",
      "T": "North and south — you made them all.\nTabor and Hermon sing for joy\nat the sound of your name."
    },
    "13": {
      "L": "You have a mighty arm; your hand is strong, your right hand exalted.",
      "M": "Your arm is mighty; your hand is strong; your right hand is raised high.",
      "T": "Your arm is strength itself.\nYour hand is strong.\nYour right hand is lifted high."
    },
    "14": {
      "L": "Righteousness and justice are the foundation of your throne; steadfast love and faithfulness go before your face.",
      "M": "Righteousness and justice are the foundation of your throne; steadfast love and faithfulness lead the way before you.",
      "T": "Righteousness and justice — these are what your throne rests on.\nSteadfast love and truth\nwalk out ahead of you."
    },
    "15": {
      "L": "Blessed are the people who know the joyful sound; O LORD, they walk in the light of your face.",
      "M": "Blessed is the people who know the joyful shout; they walk, LORD, in the light of your face.",
      "T": "How blessed are the people who know what it is\nto shout for joy before you—\nthey live in the light of your face, LORD."
    },
    "16": {
      "L": "In your name they rejoice all day long, and in your righteousness they are exalted.",
      "M": "They rejoice in your name all day long and are lifted up by your righteousness.",
      "T": "All day long your name is their joy.\nYour righteousness lifts them higher."
    },
    "17": {
      "L": "For you are the glory of their strength; by your favor our horn is exalted.",
      "M": "For you are the splendor of their strength; by your favor our strength is raised high.",
      "T": "You are the source of everything that makes them strong.\nBy your favor our horn is lifted high."
    },
    "18": {
      "L": "For our shield belongs to the LORD; our king is the Holy One of Israel.",
      "M": "For our shield belongs to the LORD; our king is the Holy One of Israel.",
      "T": "Our shield belongs to the LORD.\nThe Holy One of Israel — he is our king."
    },
    "19": {
      "L": "Then you spoke in a vision to your faithful one and said: 'I have set help upon a mighty warrior; I have exalted one chosen from the people.'",
      "M": "You spoke in a vision to your faithful servants and said: 'I have given help to a warrior; I have raised up a young man chosen from among the people.'",
      "T": "You spoke it as a vision—\nwords to those who followed you:\n'I have set my strength on a warrior.\nI have lifted up the one I chose from the people.'"
    },
    "20": {
      "L": "'I have found David my servant; with my holy oil I have anointed him,'",
      "M": "'I have found David my servant; with my holy oil I have anointed him,'",
      "T": "'I found David — my servant.\nWith my holy oil I anointed him,'"
    },
    "21": {
      "L": "'so that my hand shall be established with him; my arm also shall strengthen him.'",
      "M": "'My hand will uphold him steadily; my arm will give him strength.'",
      "T": "'my hand to sustain him,\nmy arm to make him strong.'"
    },
    "22": {
      "L": "'The enemy shall not exact upon him; the son of wickedness shall not afflict him.'",
      "M": "'No enemy will overpower him; no wicked person will oppress him.'",
      "T": "'No enemy will get the upper hand over him.\nNo man of wickedness will crush him.'"
    },
    "23": {
      "L": "'I will crush his foes before him and strike down those who hate him.'",
      "M": "'I will shatter his enemies before his eyes and defeat all who hate him.'",
      "T": "'Before his eyes I will crush his enemies—\nstrike down every one who hates him.'"
    },
    "24": {
      "L": "'My faithfulness and my steadfast love shall be with him; and in my name his horn shall be exalted.'",
      "M": "'My faithfulness and steadfast love will be with him; through my name his strength will be raised high.'",
      "T": "'My faithfulness will be at his side.\nMy steadfast love will never leave him.\nIn my name his strength will rise.'"
    },
    "25": {
      "L": "'And I will set his hand over the sea and his right hand over the rivers.'",
      "M": "'I will extend his dominion to the sea and his right hand over the rivers.'",
      "T": "'I will stretch his hand to the sea—\nhis right hand to the great rivers.'"
    },
    "26": {
      "L": "'He shall cry out to me, \"You are my Father, my God, and the Rock of my salvation!\"'",
      "M": "'He will call out to me, \"You are my Father, my God, and the Rock who saves me!\"'",
      "T": "'And he will cry to me:\n\"You are my Father—\nmy God, the Rock of my salvation.\"'"
    },
    "27": {
      "L": "'And I will make him the firstborn, the highest of the kings of the earth.'",
      "M": "'I will appoint him as my firstborn, the highest of all the kings of the earth.'",
      "T": "'I will make him my firstborn—\nhigher than any king who walks the earth.'"
    },
    "28": {
      "L": "'My steadfast love I will keep for him forever; and my covenant shall stand firm with him.'",
      "M": "'I will maintain my steadfast love for him forever, and my covenant with him will be secure.'",
      "T": "'My steadfast love I will keep for him — always.\nMy covenant with him will hold.'"
    },
    "29": {
      "L": "'And I will make his offspring endure forever, and his throne as the days of the heavens.'",
      "M": "'His line will continue forever, and his throne will last as long as the heavens above.'",
      "T": "'His children will endure — forever.\nHis throne — as long as the sky stands.'"
    },
    "30": {
      "L": "'If his children forsake my law and do not walk in my judgments,'",
      "M": "'If his descendants abandon my instruction and refuse to live by my rulings,'",
      "T": "'If his children abandon my teaching\nand refuse to walk in what I have laid down,'"
    },
    "31": {
      "L": "'if they violate my statutes and do not keep my commandments,'",
      "M": "'if they break my decrees and fail to keep my commandments,'",
      "T": "'if they violate my statutes\nand set aside my commands,'"
    },
    "32": {
      "L": "'then I will punish their transgression with the rod, and their iniquity with stripes.'",
      "M": "'then I will punish their rebellion with a rod and their sin with blows.'",
      "T": "'then I will deal with their rebellion—\na rod across the transgression, stripes for the sin.'"
    },
    "33": {
      "L": "'But my steadfast love I will not take from him, nor will I be false to my faithfulness.'",
      "M": "'But I will not withdraw my steadfast love from him or betray my faithfulness.'",
      "T": "'But my steadfast love I will not strip away.\nMy faithfulness I will not betray.'"
    },
    "34": {
      "L": "'I will not violate my covenant or alter the word that has gone out from my lips.'",
      "M": "'I will not break my covenant or change what I have spoken.'",
      "T": "'I will not break the covenant.\nI will not walk back a single word I have spoken.'"
    },
    "35": {
      "L": "'Once for all I have sworn by my holiness; I will not lie to David.'",
      "M": "'I have sworn by my own holiness once and for all; I will not deceive David.'",
      "T": "'I have sworn it — by my own holiness, once for all.\nI will not lie to David.'"
    },
    "36": {
      "L": "'His offspring shall endure forever, and his throne as long as the sun before me.'",
      "M": "'His descendants will endure forever; his throne will last as long as the sun shines before me.'",
      "T": "'His line will endure — forever.\nHis throne will stand as long as the sun burns before me.'"
    },
    "37": {
      "L": "'Like the moon it shall be established forever — a faithful witness in the sky.' Selah",
      "M": "'Like the moon it will be established forever, that faithful witness set in the heavens.' Selah",
      "T": "'Like the moon, fixed in place forever—\na faithful witness in the sky above.'\nSelah."
    },
    "38": {
      "L": "But you have cast off and rejected; you are full of wrath against your anointed one.",
      "M": "But now you have cast off and rejected him; you are enraged against your anointed king.",
      "T": "But you—\nyou have cast him off.\nYou have been furious with your anointed one."
    },
    "39": {
      "L": "You have renounced the covenant with your servant; you have defiled his crown in the dust.",
      "M": "You have repudiated the covenant with your servant; you have thrown his crown into the dust.",
      "T": "You set aside the covenant with your servant.\nYou threw his crown into the dirt."
    },
    "40": {
      "L": "You have breached all his walls; you have brought his strongholds to ruin.",
      "M": "You have broken down all his walls and reduced his fortifications to rubble.",
      "T": "You broke down every wall that protected him.\nYou turned his strongholds to rubble."
    },
    "41": {
      "L": "All who pass by the way plunder him; he has become a reproach to his neighbors.",
      "M": "All who pass by strip him of what he has; he has become a mockery to his neighbors.",
      "T": "Everyone passing by plunders him.\nHe has become a joke to those who once called him neighbor."
    },
    "42": {
      "L": "You have lifted up the right hand of his adversaries; you have made all his enemies rejoice.",
      "M": "You have strengthened the hand of his enemies; you have let all who hate him celebrate.",
      "T": "You gave his enemies the upper hand.\nYou let everyone who hates him shout for joy."
    },
    "43": {
      "L": "You have also turned back the edge of his sword and have not made him stand in battle.",
      "M": "You have blunted his sword in battle and failed to hold him up when he fought.",
      "T": "You turned his own sword dull.\nYou let him fall in battle\nwithout holding him up."
    },
    "44": {
      "L": "You have brought his splendor to an end and cast his throne to the ground.",
      "M": "You have stripped away his glory and hurled his throne down to the ground.",
      "T": "His splendor — you ended it.\nHis throne — you threw it to the ground."
    },
    "45": {
      "L": "You have cut short the days of his youth; you have covered him with shame. Selah",
      "M": "You have shortened the days of his prime and wrapped him in shame. Selah",
      "T": "You cut short the years of his youth.\nYou dressed him in shame.\nSelah."
    },
    "46": {
      "L": "How long, O LORD? Will you hide yourself forever? How long will your wrath burn like fire?",
      "M": "How long, O LORD? Will you hide yourself away forever? How long will your anger blaze like fire?",
      "T": "How long, LORD?\nWill you hide yourself away forever?\nHow long will your wrath keep burning?"
    },
    "47": {
      "L": "Remember how brief my time is! For what futility you have created all the sons of man!",
      "M": "Remember how short my span of life is! For what emptiness you have made all the children of man!",
      "T": "Remember how short my time is—\nhow brief the span you gave us.\nFor what emptiness did you make them,\nall the children of Adam?"
    },
    "48": {
      "L": "What man is there who can live and never see death? Who can deliver his soul from the hand of Sheol? Selah",
      "M": "What man can go on living and never see death? Who can rescue his life from the grip of the grave? Selah",
      "T": "What man lives and escapes death?\nWho can pull his very life\nfrom the grip of the grave?\nSelah."
    },
    "49": {
      "L": "Lord, where is your former steadfast love, which by your faithfulness you swore to David?",
      "M": "Lord, where is your steadfast love of old, which in your faithfulness you swore to David?",
      "T": "Lord — where is the steadfast love you showed before?\nThe love you swore to David in your faithfulness?\nWhere has it gone?"
    },
    "50": {
      "L": "Remember, Lord, the reproach of your servants — how I carry in my bosom the insults of all the many peoples,",
      "M": "Remember, Lord, the mocking your servants endure — how I bear in my heart the taunts of all those nations,",
      "T": "Remember, Lord, how your servants are mocked.\nHow I carry it here, pressed against my chest—\nthe taunts of every people."
    },
    "51": {
      "L": "with which your enemies, O LORD, have mocked, with which they have mocked the footsteps of your anointed one.",
      "M": "with which your enemies, LORD, have taunted, mocking every step of your anointed king.",
      "T": "With that same contempt your enemies have mocked, LORD—\nmocked the very footsteps of your anointed one."
    },
    "52": {
      "L": "Blessed be the LORD forever! Amen and Amen.",
      "M": "Blessed be the LORD forever! Amen and Amen.",
      "T": "Blessed be the LORD — forever.\nAmen and Amen."
    }
  },

  # ===========================================================================
  # Psalm 90 — A Prayer of Moses the Man of God: Time, Eternity, and Wisdom
  # ===========================================================================
  "90": {
    "1": {
      "L": "A Prayer of Moses the man of God. Lord, you have been our dwelling place throughout all generations.",
      "M": "A Prayer of Moses the man of God. Lord, you have been our home in every generation.",
      "T": "A Prayer of Moses the man of God.\nLord — in every generation,\nyou have been where we live."
    },
    "2": {
      "L": "Before the mountains were brought forth, or you had formed the earth and the world — from everlasting to everlasting you are God.",
      "M": "Before the mountains were born, or you had shaped the earth and the world — from age to age you are God.",
      "T": "Before the mountains were born—\nbefore you shaped the earth and all that fills it—\nfrom eternity to eternity,\nyou are God."
    },
    "3": {
      "L": "You return man to dust and say, 'Return, O children of man!'",
      "M": "You turn human beings back to dust and say, 'Return, O children of Adam!'",
      "T": "You turn people back to dust\nand say,\n'Return, children of Adam.'"
    },
    "4": {
      "L": "For a thousand years in your sight are but as yesterday when it has passed, or as a watch in the night.",
      "M": "For a thousand years in your sight are like yesterday after it has passed — like a single watch in the night.",
      "T": "A thousand years in your sight\nare like yesterday, already gone—\nlike a single watch in the night."
    },
    "5": {
      "L": "You sweep them away as with a flood; they are like a sleep — like grass that springs up in the morning.",
      "M": "You sweep them away like a sudden flood; they are like a dream, like grass that sprouts in the morning.",
      "T": "You sweep them away like a flood.\nThey are a dream—\nlike grass that springs up in the morning."
    },
    "6": {
      "L": "In the morning it flourishes and springs up; in the evening it is cut down and withers.",
      "M": "In the morning it blossoms and shoots up; by evening it is mown down and dry.",
      "T": "In the morning it rises and blooms.\nBy evening it is cut down and withered."
    },
    "7": {
      "L": "For we are consumed by your anger; by your wrath we are dismayed.",
      "M": "We are brought to an end by your anger; by your fury we are overwhelmed.",
      "T": "Your anger consumes us.\nYour wrath leaves us undone."
    },
    "8": {
      "L": "You have set our iniquities before you, our secret sins in the light of your face.",
      "M": "You have placed our sins before you and our hidden faults in the full light of your presence.",
      "T": "You have laid out our iniquities before you—\neven our secret sins,\nexposed in the light of your face."
    },
    "9": {
      "L": "For all our days have passed away under your wrath; we bring our years to an end like a sigh.",
      "M": "All our days slip away under your wrath; we bring our years to an end like a breath.",
      "T": "All our days pass away under your wrath.\nWe finish our years with a sigh—\na breath, and they are gone."
    },
    "10": {
      "L": "The days of our years are seventy, or if by reason of strength eighty years; yet their pride is but toil and trouble, for it is soon gone and we fly away.",
      "M": "The span of our years is seventy — or if we are strong, eighty — but even then they contain only toil and grief; they pass quickly and we are gone.",
      "T": "Seventy years — that is what we get.\nEighty, if strength holds.\nBut even those years are burdened with toil and grief.\nThen quickly, quickly — we fly away."
    },
    "11": {
      "L": "Who understands the power of your anger? Who fears your wrath as they ought?",
      "M": "Who truly grasps the force of your anger? Who fears your wrath as it deserves?",
      "T": "Who really understands the power of your anger?\nWho fears your wrath\nthe way it deserves to be feared?"
    },
    "12": {
      "L": "So teach us to number our days, that we may gain a heart of wisdom.",
      "M": "Teach us, then, to count our days aright, that we may acquire a wise heart.",
      "T": "So teach us to count our days—\nthat we may bring home\na heart of wisdom."
    },
    "13": {
      "L": "Return, O LORD! How long? Have compassion on your servants!",
      "M": "Turn back, LORD! How long will this go on? Have mercy on your servants!",
      "T": "Return, LORD — how long?\nTake pity on your servants."
    },
    "14": {
      "L": "Satisfy us in the morning with your steadfast love, that we may rejoice and be glad all our days.",
      "M": "Fill us in the morning with your steadfast love, so that we may celebrate and rejoice through all our days.",
      "T": "Fill us in the morning with your steadfast love.\nThen we will rejoice—\nand be glad through all our days."
    },
    "15": {
      "L": "Make us glad as many days as you have afflicted us, and as many years as we have seen evil.",
      "M": "Give us gladness to match the days you have made us suffer — joy equal to the years we have known trouble.",
      "T": "Make our gladness equal our grief—\njoy that answers year for year\nthe time we spent in trouble."
    },
    "16": {
      "L": "Let your work be seen by your servants and your glory by their children.",
      "M": "Let your work appear to your servants and your splendor shine on their children.",
      "T": "Show your work to your servants.\nLet your glory be what their children see."
    },
    "17": {
      "L": "And let the favor of the LORD our God be upon us; and establish the work of our hands upon us — yes, establish the work of our hands!",
      "M": "May the favor of the LORD our God rest upon us; establish the work of our hands — yes, establish the work of our hands!",
      "T": "Let the beauty of the LORD our God rest on us.\nEstablish the work of our hands—\nyes, Lord — establish it."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 89–90 written.')

if __name__ == '__main__':
    main()
