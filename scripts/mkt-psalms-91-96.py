"""
MKT Psalms chapters 91–96 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-91-96.py

=== Overview of this unit ===

Six psalms spanning the transition from Book IV's opening (Ps 90, Moses) into the first
cluster of "enthronement psalms" (93–99 are the classic group). Together they move from
sheltered trust (91) through Sabbath praise (92) into a burst of cosmic kingship hymns
(93–96) that declare the LORD's universal sovereignty over creation, nations, and time.

Ps 91 (16 v) — "Whoever dwells in the shelter of the Most High." One of the most beloved
    psalms of trust in the Psalter. No named author (though ancient tradition associates
    it with Moses; the LXX even adds "of Moses"). Structure:
    vv1-2:    Declaration of shelter — dwelling under the shadow of the Almighty.
    vv3-13:   God's comprehensive protection — seven specific threats neutralized.
    vv14-16:  God's own first-person promise to the one who "clings" to him in love.

    CRITICAL NOTE: vv11-12 are quoted verbatim by Satan in the temptation of Jesus
    (Matt 4:6 / Luke 4:10-11). The devil uses a protection promise as a temptation
    toward presumption — a significant NT interpretive frame for this psalm.

    The verb in v14 is chashaq (H2836) — "to cling, to set one's desire upon." Stronger
    than mere "love." It implies adhesion, the way a lover clings or a limpet holds rock.
    Rendered "clings to me in love" in M, "has clung to me" in L.

Ps 92 (15 v) — "A Psalm / A Song for the Sabbath day." The only psalm in the Psalter
    with an explicit Sabbath superscription. No author named. Structure:
    vv1-3:    It is good to praise — declared with musical specificity.
    vv4-5:    Gladness in God's works, wonder at their depth.
    vv6-9:    The wicked flourish momentarily; God is Most High forever.
    vv10-11:  The psalmist's own exaltation — anointed with fresh oil.
    vv12-15:  The righteous like palm and cedar — still bearing fruit in old age.

    The Sabbath connection is thematic: the day of rest directs attention away from
    one's own labor toward God's works. The psalm's twin movement (God's hiddenness
    to those who don't look, vv6-9 / God's abundance to those who wait, vv12-15)
    maps onto Sabbath spirituality.

Ps 93 (5 v) — "The LORD reigns." The opening of the "enthronement psalms" (93, 95–99).
    A brief, dense declaration of divine kingship. The image of the primordial waters
    (vv3-4) echoes the creation mythos — God's throne precedes and outlasts the
    sea's roar. The final verse pivots to the Mosaic/Priestly theme: divine holiness
    adorning the house of God "forevermore."

Ps 94 (23 v) — "O LORD, God of vengeance." A communal lament calling for divine justice
    against oppressors who murder the vulnerable (widows, foreigners, orphans) and
    deny that God sees. The psalm moves from urgent outcry (vv1-7) through wisdom
    argument (vv8-15) to personal testimony and confident conclusion (vv16-23).

    v11 is quoted by Paul in 1 Cor 3:20: "The LORD knows the thoughts of the wise,
    that they are futile." Paul applies the Psalm's "thoughts of man" to specifically
    the "wise" of Corinth.

Ps 95 (11 v) — "Come, let us sing for joy." The first of the enthronement cluster that
    begins with worship but ends with warning. The second half (vv7b-11) is extensively
    quoted in Hebrews 3-4 (especially v7b: "today if you hear his voice..."; v11: "they
    shall not enter my rest"). Hebrews interprets "rest" christologically as the final
    sabbath rest of God's people.

    The place names Meribah (H4808, "quarreling/contention") and Massah (H4532,
    "testing/trial") refer to Exodus 17:1-7 / Numbers 20:1-13 where Israel demanded
    water and tested God. The Hebrew plays on their meanings.

Ps 96 (13 v) — "Sing to the LORD a new song." This psalm is largely parallel to
    1 Chronicles 16:23-33 (the psalm David ordered sung when the Ark arrived in
    Jerusalem). Its theology is expansive: the "new song" calls not just Israel but
    all nations to worship, and anticipates the LORD coming to judge the earth (v13).
    That final verse is one of the clearest OT anticipations of eschatological judgment
    in Psalms.

=== Contested-term decisions ===

H2617 (חֶסֶד, chesed): Does not appear prominently in Ps 91-96 (chesed appears at
    Ps 92:2 in the morning/faithfulness pairing). Rendered "steadfast love" in L/M/T
    at Ps 92:2. Consistent with all prior Psalms scripts.

H530 (אֱמוּנָה, emunah): "faithfulness" in all tiers at Ps 92:2 (paired with chesed)
    and Ps 96:13 (God judges "with his faithfulness"). Consistent throughout.

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M. In T: "LORD" or "the LORD"
    per cadence and line structure. Consistent with all prior Psalms scripts.

H5945 (עֶלְיוֹן, Elyon): "Most High" in all tiers. Appears at Ps 91:1, 9; 92:1, 8.

H7706 (שַׁדַּי, Shaddai): "Almighty" in L/M/T. Appears at Ps 91:1 ("shadow of the
    Almighty"). The name evokes God's sovereign sufficiency and power.

H4268 (מַחֲסֶה, makhseh): "refuge" in all tiers. Appears at Ps 91:2, 9. A place of
    shelter, a hiding-place from danger.

H571 (אֱמֶת, emet): "faithfulness" in L/M at Ps 96:13. Slightly distinct from emunah —
    emet emphasizes reliability/truth. In T: "faithfulness" maintained for parallelism
    with "righteousness" in the final verse.

H5542 (סֶלָה, Selah): Does not appear in Ps 91-96.

H6664 (צֶדֶק, tsedeq) / H6666 (צְדָקָה, tsedaqah): "righteousness" in L/M/T.
    Appears at Ps 96:13 ("judge the world in righteousness"). Judicial-relational
    quality of right order; not mere "correctness" but covenantal rightness.

H4941 (מִשְׁפָּט, mishpat): "justice" in L/M/T. At Ps 94:15 ("justice will return to
    the righteous"). At Ps 96:10 ("he will judge the peoples with equity/justice").

H2836 (חָשַׁק, chashaq): "cling / set one's desire upon" at Ps 91:14. More intense
    than "love" — implies adhesion, passionate attachment. Rendered "clings to me
    in love" in M; "has set his love on me" in L; "who clings to me" in T.

H5315 (נֶפֶשׁ, nefesh): Not prominent in this unit. Where it appears contextually
    (Ps 94:19 "my soul"), rendered "soul" in L, "soul" in M, context-sensitive in T.

=== Textual and interpretive notes ===

Ps 91:11-12 — The "angel verses" quoted by Satan (Matt 4:6 / Luke 4:10-11). The quote
    is verbatim from the LXX. The psalm gives a genuine promise; the temptation is to
    use the promise presumptively — to engineer a situation requiring rescue rather than
    trusting within providential life. The verses are not cancelled by the NT usage;
    they retain their comfort for those who live within God's purposes.

Ps 91:14-16 — Divine first-person speech embedded without formal introduction. The shift
    from 3rd person description (vv3-13) to God's direct "I will" (vv14-16) is typical
    of Hebrew "oracle of assurance" form. Rendered with a clear speech marker ("says
    the LORD" in v14 L; "declares the LORD" in v14 M) to signal the voice shift.

Ps 92:1 — The superscription "A Psalm / A Song for the Sabbath day" is unusual. Most
    psalms have only "A Psalm of David" or similar; adding "for the Sabbath" makes this
    the only day-specific psalm in the canonical Psalter.

Ps 93:3-4 — The "floods" (naharoth, H5104) are the great rivers or primordial waters.
    In ancient Near Eastern cosmology, the sea/deep represented chaos. The LORD's
    mastery of the roaring waters is a creation-theology claim: he who defeated chaos
    at the start continues to reign over it. See also Ps 89:9-10 (Rahab).

Ps 94:11 — Cited in 1 Corinthians 3:20 as Scripture. Paul applies it to the "thoughts
    of the wise" specifically. The LXX has "the wise" where Hebrew has "man" (adam) —
    Paul follows the LXX reading.

Ps 95:7b-11 — The hinge point of the psalm, introduced by "Today, if you hear his
    voice." The word "today" (H3117, yom) is theologically loaded in Hebrews: the
    author treats every reading of this psalm as a new "today" — the warning is always
    contemporary, never merely historical.

Ps 96:13 — The final verse announces God "coming to judge the earth." The verb is
    participle (ba', "coming") — this is not a one-time past event but a continuous
    theological reality. The repeated "for he comes, for he comes" (ki ba', ki ba')
    doubles the urgency.

=== Aspect and tense notes ===

Ps 91: Mix of participial descriptions (the one who dwells, the one who says) in vv1-2
    and imperfect verbs of ongoing protection (vv3-13). The divine speech (vv14-16)
    uses cohortative perfects of assured future action: "I will deliver, I will set
    him on high, I will be with him." These are the strongest form of divine promise.

Ps 92: Hymnic presents (it is good, you have made me glad) and descriptive perfects
    (your works, LORD, how great). The wicked's flourishing is described with Hebrew
    infinitive + finite verb construction implying simultaneity and then sudden end.

Ps 93: Short psalm, mostly nominal sentences (The LORD is clothed, your throne is
    established, your testimonies are sure). The Hebrew uses no explicit past/present
    tense in the nominal clauses — they assert timeless fact.

Ps 94: Urgent imperatives (rise up, lift yourself, vv1-2), then 3rd-person description
    of wicked acts (vv3-7), then 2nd-person direct address to the wicked (vv8-11),
    then 2nd-person address to the disciplined one (v12), then personal testimony
    in 1st person (vv16-23). The perspective shifts are intentional.

Ps 95-96: Cohortatives of invitation throughout ("let us sing, let us shout, let us
    bow down"). These are not commands but invitations — the speaker includes himself
    in the call to worship. The final verses of Ps 96 shift to jussives (let the
    heavens rejoice, let the earth be glad) — widening the circle to all creation.
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
  # Psalm 91 — Shelter Under the Shadow of the Almighty
  # ===========================================================================
  "91": {
    "1": {
      "L": "He who dwells in the shelter of the Most High will abide in the shadow of the Almighty.",
      "M": "Whoever lives in the shelter of the Most High will rest in the shadow of the Almighty.",
      "T": "Whoever makes their home in the shelter of the Most High\nwill rest in the shadow of the Almighty."
    },
    "2": {
      "L": "I will say of the LORD, 'He is my refuge and my fortress, my God, in whom I trust.'",
      "M": "I will say to the LORD, 'You are my refuge and my fortress, my God, in whom I trust.'",
      "T": "I say to the LORD:\n'You are my refuge, my fortress —\nmy God. I trust you.'"
    },
    "3": {
      "L": "Surely he will deliver you from the snare of the fowler and from the deadly pestilence.",
      "M": "He will rescue you from the hunter's trap and from every deadly disease.",
      "T": "He will pull you free from the trap the hunter set—\nand from the deadly plague."
    },
    "4": {
      "L": "He will cover you with his feathers, and under his wings you will take refuge; his faithfulness is a shield and buckler.",
      "M": "He will shelter you under his feathers; you will find refuge beneath his wings; his faithfulness is your shield and armor.",
      "T": "He spreads his feathers over you—\nunder his wings you find shelter.\nHis faithfulness is your shield,\nyour rampart that holds."
    },
    "5": {
      "L": "You will not be afraid of the terror by night, nor the arrow that flies by day,",
      "M": "You will not fear the terror that comes in the night or the arrow that flies in the daylight,",
      "T": "You will not dread the terror that prowls the night,\nnor the arrow loosed in broad day,"
    },
    "6": {
      "L": "nor the pestilence that walks in darkness, nor the destruction that wastes at noonday.",
      "M": "nor the disease that moves through the dark or the plague that strikes at noon.",
      "T": "nor the plague that moves through the darkness,\nnor the destruction that strikes at full noon."
    },
    "7": {
      "L": "A thousand shall fall at your side and ten thousand at your right hand; it shall not come near you.",
      "M": "A thousand may fall beside you, ten thousand at your right hand — but it will not reach you.",
      "T": "A thousand may fall at your side,\nten thousand at your right hand—\nbut it will not touch you."
    },
    "8": {
      "L": "Only with your eyes will you look and see the reward of the wicked.",
      "M": "You will only watch with your own eyes and see the fate of the wicked.",
      "T": "You will only watch with your own eyes\nand see what becomes of the wicked."
    },
    "9": {
      "L": "Because you have made the LORD — my refuge, the Most High — your habitation,",
      "M": "Because you have made the LORD your refuge, the Most High your dwelling place,",
      "T": "Because you have made the LORD your refuge—\nthe Most High the place where you live—"
    },
    "10": {
      "L": "no evil shall befall you, and no plague shall come near your dwelling.",
      "M": "no evil will happen to you, and no plague will come close to your home.",
      "T": "no evil will be allowed to reach you,\nno plague will come near where you live."
    },
    "11": {
      "L": "For he will give his angels charge over you to guard you in all your ways.",
      "M": "He will command his angels to guard you in all your ways.",
      "T": "He will command his angels concerning you—\nto guard you in every path you take."
    },
    "12": {
      "L": "They will bear you up in their hands, lest you strike your foot against a stone.",
      "M": "They will hold you up in their arms so your foot does not strike against a stone.",
      "T": "They will carry you in their arms\nso your foot never strikes a stone."
    },
    "13": {
      "L": "On the lion and the adder you will tread; you will trample underfoot the young lion and the serpent.",
      "M": "You will walk on the lion and the cobra; you will trample the young lion and the serpent underfoot.",
      "T": "You will walk over the lion and the serpent—\ntrample the young lion,\ntrample the ancient snake."
    },
    "14": {
      "L": "'Because he has set his love upon me,' says the LORD, 'I will deliver him; I will set him on high, because he has known my name.'",
      "M": "'Because he clings to me in love,' declares the LORD, 'I will rescue him; I will set him beyond reach, because he truly knows who I am.'",
      "T": "'Because he has clung to me in love,' says the LORD,\n'I will deliver him.\nI will lift him out of reach—\nbecause he knows my name.'"
    },
    "15": {
      "L": "'He will call upon me and I will answer him; I will be with him in trouble; I will rescue him and honor him.'",
      "M": "'When he calls on me I will answer; I will be with him in his trouble; I will rescue him and give him honor.'",
      "T": "'When he calls — I will answer.\nI will be with him in his trouble.\nI will rescue him and cover him with honor.'"
    },
    "16": {
      "L": "'With long life I will satisfy him and show him my salvation.'",
      "M": "'I will give him a full life and let him see my saving power.'",
      "T": "'I will fill him with long life\nand show him my salvation.'"
    }
  },

  # ===========================================================================
  # Psalm 92 — A Song for the Sabbath: Praising the Deep Works of God
  # ===========================================================================
  "92": {
    "1": {
      "L": "A Psalm. A Song for the Sabbath day. It is a good thing to give thanks to the LORD and to sing praises to your name, O Most High,",
      "M": "A Psalm. A Song for the Sabbath day. It is good to give thanks to the LORD and to sing praises to your name, O Most High,",
      "T": "A Psalm. A Song for the Sabbath day.\nHow good it is to give thanks to the LORD—\nto sing praises to your name, Most High,"
    },
    "2": {
      "L": "to declare your steadfast love in the morning and your faithfulness every night,",
      "M": "to declare your steadfast love each morning and your faithfulness through every night,",
      "T": "to declare your steadfast love each morning\nand your faithfulness through the night,"
    },
    "3": {
      "L": "upon an instrument of ten strings and upon the harp, upon the lyre with a solemn sound.",
      "M": "to the music of the ten-stringed lute and the melody of the harp, with the rippling of the lyre.",
      "T": "with a ten-stringed lute,\nthe rippling melody of the harp."
    },
    "4": {
      "L": "For you, O LORD, have made me glad by your work; at the works of your hands I will sing for joy.",
      "M": "You have made me glad, LORD, by what you have done; I sing for joy over all that your hands have made.",
      "T": "You have made me glad, LORD,\nby everything you have done.\nI shout for joy\nat the work of your hands."
    },
    "5": {
      "L": "How great are your works, O LORD! Your thoughts are very deep.",
      "M": "How great are your works, LORD! How utterly deep are your thoughts!",
      "T": "How great your works are, LORD!\nHow deep your designs—\nbeyond all measuring."
    },
    "6": {
      "L": "A brutish man does not know, and a fool does not understand this:",
      "M": "A senseless person cannot grasp it, and a fool does not understand:",
      "T": "The senseless person does not see it.\nThe fool never understands:"
    },
    "7": {
      "L": "that though the wicked spring up like grass and all the workers of iniquity flourish, it is that they shall be destroyed forever —",
      "M": "the wicked may spring up like grass and every evildoer may flourish, but they are headed for eternal ruin —",
      "T": "the wicked may spring up like grass,\nevery evildoer may flourish—\nbut it is only so they can be destroyed forever."
    },
    "8": {
      "L": "but you, O LORD, are on high forevermore.",
      "M": "while you, LORD, are exalted on high forever.",
      "T": "But you, LORD—\nyou are high above it all, forever."
    },
    "9": {
      "L": "For behold, your enemies, O LORD — for behold, your enemies will perish; all the workers of iniquity will be scattered.",
      "M": "Yes, your enemies, LORD — your enemies will certainly perish; all who do evil will be scattered.",
      "T": "Look — your enemies, LORD.\nYour enemies will perish.\nAll who do evil will be scattered."
    },
    "10": {
      "L": "But you have exalted my horn like that of a wild ox; I have been anointed with fresh oil.",
      "M": "But you have raised my strength high like the horn of a wild bull; you have anointed me with fresh oil.",
      "T": "But you have raised my strength high—\nlike the horn of a wild ox.\nYou have anointed me with fresh oil."
    },
    "11": {
      "L": "My eye has seen the defeat of my enemies; my ears have heard the ruin of the evildoers who rise up against me.",
      "M": "My eyes have seen the downfall of my enemies; my ears have heard the ruin of those who rose against me.",
      "T": "My own eyes have seen it—\nwhat happens to those who hated me.\nWith my own ears I have heard the ruin\nof those who rose against me."
    },
    "12": {
      "L": "The righteous flourish like the palm tree and grow like a cedar in Lebanon.",
      "M": "The righteous person flourishes like the palm tree and grows tall like a cedar of Lebanon.",
      "T": "The righteous flourish like the palm tree—\nthey grow tall and strong\nlike a cedar of Lebanon."
    },
    "13": {
      "L": "They are planted in the house of the LORD; they flourish in the courts of our God.",
      "M": "Planted in the house of the LORD, they will flourish in the courts of our God.",
      "T": "Planted in the house of the LORD—\nthey flourish in the courts of our God."
    },
    "14": {
      "L": "They still bear fruit in old age; they are ever full of sap and green,",
      "M": "In old age they still produce fruit; they remain vigorous and full of life,",
      "T": "Even in old age they bear fruit—\nstill vigorous, still green,"
    },
    "15": {
      "L": "declaring that the LORD is upright; he is my rock, and there is no unrighteousness in him.",
      "M": "bearing witness that the LORD is just — he is my rock, and there is nothing wrong in him.",
      "T": "still bearing witness:\nthe LORD is just.\nHe is my rock,\nand there is no wrong in him."
    }
  },

  # ===========================================================================
  # Psalm 93 — The LORD Reigns: Majesty Over the Primordial Waters
  # ===========================================================================
  "93": {
    "1": {
      "L": "The LORD reigns; he is clothed with majesty; the LORD is clothed with strength; he has girded himself. Yes, the world is established; it shall not be moved.",
      "M": "The LORD reigns! He is clothed with majesty; the LORD is dressed in strength and has girded himself. The world is firmly established — it cannot be shaken.",
      "T": "The LORD reigns!\nHe is clothed with majesty—\ndressed in strength, girded with power.\nThe world stands firm,\nunshakeable."
    },
    "2": {
      "L": "Your throne is established from of old; you are from everlasting.",
      "M": "Your throne has been established from ancient times; you yourself are from everlasting.",
      "T": "Your throne was set from the beginning—\nyou yourself are from eternity."
    },
    "3": {
      "L": "The floods have lifted up, O LORD; the floods have lifted up their voice; the floods lift up their waves.",
      "M": "The great waters have lifted up their voice, LORD; the rushing floods have lifted up their voice and their crashing waves.",
      "T": "The rivers roar, LORD—\nthe rivers roar and raise their voices.\nThe great floods thunder their waves."
    },
    "4": {
      "L": "Mightier than the sounds of many waters, mightier than the waves of the sea — the LORD on high is mighty.",
      "M": "Mightier than the roar of many waters, mightier than the waves of the sea — the LORD on high is mighty.",
      "T": "Mightier than the roar of countless waters—\nmightier than the crashing of the sea—\nthe LORD on high is mighty."
    },
    "5": {
      "L": "Your testimonies are very trustworthy; holiness befits your house, O LORD, forevermore.",
      "M": "Your decrees are completely trustworthy; holiness adorns your house, LORD, forevermore.",
      "T": "Your decrees are utterly reliable, LORD.\nHoliness adorns your house—\nforevermore."
    }
  },

  # ===========================================================================
  # Psalm 94 — O God of Vengeance: Justice for the Oppressed
  # ===========================================================================
  "94": {
    "1": {
      "L": "O LORD, God of vengeance! O God of vengeance, shine forth!",
      "M": "O LORD, God who avenges — God of justice, arise and shine forth!",
      "T": "LORD, God who avenges—\nGod of justice, rise up!\nShine forth!"
    },
    "2": {
      "L": "Lift yourself up, O Judge of the earth; render a recompense to the proud!",
      "M": "Rise up, Judge of the earth; pay back to the proud what they deserve!",
      "T": "Rise up, Judge of the earth—\npay back the proud\nwhat their pride has earned."
    },
    "3": {
      "L": "How long shall the wicked, O LORD, how long shall the wicked exult?",
      "M": "How long, LORD, will the wicked — how long will the wicked rejoice in triumph?",
      "T": "How long, LORD?\nHow long will the wicked—\nhow long will the wicked keep celebrating?"
    },
    "4": {
      "L": "They pour out arrogant words; all the workers of iniquity boast.",
      "M": "They spew proud words without end; all who do evil brag without restraint.",
      "T": "They pour out arrogant words.\nAll who do evil boast\nwithout shame."
    },
    "5": {
      "L": "They crush your people, O LORD, and afflict your inheritance.",
      "M": "They crush your people, LORD, and oppress those who belong to you.",
      "T": "Your people, LORD—\nthey crush them.\nYour own inheritance — they grind it down."
    },
    "6": {
      "L": "They slay the widow and the sojourner, and they murder the fatherless.",
      "M": "They murder the widow and the foreigner and kill the fatherless.",
      "T": "They murder widows and foreigners.\nThey kill the fatherless."
    },
    "7": {
      "L": "And they say, 'The LORD does not see; the God of Jacob does not perceive.'",
      "M": "And they say, 'The LORD never sees it; the God of Jacob pays no attention.'",
      "T": "And they say,\n'The LORD doesn't see it.\nThe God of Jacob pays no attention.'"
    },
    "8": {
      "L": "Understand, O most brutish of the people! O fools, when will you be wise?",
      "M": "Grasp this, you most senseless among the people — fools, when will you become wise?",
      "T": "Wake up, you most senseless among all the people.\nYou fools — when will wisdom finally reach you?"
    },
    "9": {
      "L": "He who planted the ear — shall he not hear? He who formed the eye — shall he not see?",
      "M": "The one who made the ear — does he not hear? The one who formed the eye — does he not see?",
      "T": "The one who made the ear—\ndoes he not hear?\nThe one who shaped the eye—\ndoes he not see?"
    },
    "10": {
      "L": "He who chastises the nations — shall he not rebuke? He who teaches man knowledge,",
      "M": "The one who corrects the nations — will he not call them to account? The one who teaches all people —",
      "T": "The one who disciplines entire nations—\nwill he not correct?\nThe one who teaches all humanity—"
    },
    "11": {
      "L": "the LORD knows the thoughts of man, that they are but a breath.",
      "M": "the LORD knows what human beings think — that their thoughts are nothing but vapor.",
      "T": "the LORD knows what people think.\nHe knows how empty it all is."
    },
    "12": {
      "L": "Blessed is the man whom you discipline, O LORD, and teach out of your law,",
      "M": "Blessed is the one you discipline, LORD, and instruct from your teaching,",
      "T": "Blessed is the one you discipline, LORD—\nthe one you teach from your own instruction,"
    },
    "13": {
      "L": "to give him rest from days of trouble, until a pit is dug for the wicked.",
      "M": "giving him rest in days of trouble until a pit is dug for the wicked.",
      "T": "giving them rest from days of trouble\nwhile the pit is being prepared for the wicked."
    },
    "14": {
      "L": "For the LORD will not forsake his people; he will not abandon his inheritance.",
      "M": "The LORD will not abandon his people or desert his inheritance.",
      "T": "The LORD will not abandon his people.\nHe will never forsake his inheritance."
    },
    "15": {
      "L": "For justice will return to the righteous, and all the upright in heart will follow it.",
      "M": "Surely justice will return to the righteous, and all who are upright in heart will pursue it.",
      "T": "Justice will return to the upright.\nAll who hold a straight heart\nwill follow in its train."
    },
    "16": {
      "L": "Who rises up for me against the wicked? Who stands up for me against the workers of evil?",
      "M": "Who will stand up for me against the wicked? Who will take my side against evildoers?",
      "T": "Who will rise up on my behalf against the wicked?\nWho will stand with me\nagainst those who do evil?"
    },
    "17": {
      "L": "Unless the LORD had been my help, my soul would have dwelt in silence in an instant.",
      "M": "If the LORD had not been my help, I would very soon have lain in the silence of death.",
      "T": "If the LORD had not come to my aid—\nin a moment I would have been in the silence of the grave."
    },
    "18": {
      "L": "When I thought, 'My foot is slipping,' your steadfast love, O LORD, held me up.",
      "M": "When I felt my foot giving way, your steadfast love, LORD, held me steady.",
      "T": "When I felt my foot slipping,\nyour steadfast love, LORD,\nwas what held me up."
    },
    "19": {
      "L": "When the cares of my heart are many, your comforts cheer my soul.",
      "M": "When anxious thoughts multiply inside me, your comfort brings delight to my soul.",
      "T": "When my inner life was crowded with anxious thoughts,\nyour comfort was what brought me joy."
    },
    "20": {
      "L": "Can wicked rulers be allied with you — those who frame injustice by statute?",
      "M": "Can a corrupt throne have any fellowship with you — one that enacts harm through its own laws?",
      "T": "Can a corrupt government count itself your partner—\none that enacts suffering\nthrough the law itself?"
    },
    "21": {
      "L": "They band together against the life of the righteous and condemn the innocent to death.",
      "M": "They join forces against the lives of the righteous and condemn the innocent to death.",
      "T": "They conspire against the lives of the upright\nand condemn the innocent."
    },
    "22": {
      "L": "But the LORD has become my stronghold, and my God the rock of my refuge.",
      "M": "But the LORD is my strong fortress, and my God is the rock where I take shelter.",
      "T": "But the LORD has become my fortress.\nMy God — the rock where I shelter."
    },
    "23": {
      "L": "He will bring back on them their iniquity and cut them off in their own wickedness; the LORD our God will cut them off.",
      "M": "He will pay them back for their sin and destroy them for their evil; the LORD our God will wipe them out.",
      "T": "He will turn their own evil back on them.\nHe will cut them off for what they have done.\nThe LORD our God will destroy them."
    }
  },

  # ===========================================================================
  # Psalm 95 — Come, Let Us Worship — and Hear the Warning Voice
  # ===========================================================================
  "95": {
    "1": {
      "L": "O come, let us sing for joy to the LORD; let us shout aloud to the rock of our salvation!",
      "M": "Come, let us sing joyfully to the LORD; let us shout aloud to the Rock who saves us!",
      "T": "Come — let us sing to the LORD!\nLet us shout aloud to the Rock who saves us!"
    },
    "2": {
      "L": "Let us come before his presence with thanksgiving; let us extol him with songs of praise.",
      "M": "Let us come before him with thanksgiving and celebrate him with songs of praise.",
      "T": "Let us come before him with gratitude—\ncelebrating him with songs."
    },
    "3": {
      "L": "For the LORD is a great God and a great King above all gods.",
      "M": "For the LORD is a great God, a great King greater than all other gods.",
      "T": "For the LORD is a great God—\na great King above everything that calls itself a god."
    },
    "4": {
      "L": "In his hand are the deep places of the earth; the heights of the mountains are his also.",
      "M": "The deepest places of the earth are in his hand, and the mountain peaks belong to him.",
      "T": "The depths of the earth are in his hand.\nThe mountain summits are his."
    },
    "5": {
      "L": "The sea is his, and he made it; and his hands formed the dry land.",
      "M": "The sea is his — he made it; his own hands shaped the dry land.",
      "T": "The sea is his — he made it.\nHis hands shaped every stretch of dry ground."
    },
    "6": {
      "L": "O come, let us worship and bow down; let us kneel before the LORD our Maker!",
      "M": "Come, let us bow down and worship; let us kneel before the LORD who made us.",
      "T": "Come — let us bow down and worship.\nLet us kneel before the LORD who made us."
    },
    "7": {
      "L": "For he is our God and we are the people of his pasture and the sheep of his hand. Today, if you hear his voice,",
      "M": "For he is our God, and we are the people of his pasture, the flock he tends. Today — if only you would hear his voice:",
      "T": "He is our God.\nWe are the people of his pasture,\nthe flock in his care.\nToday — if you will hear his voice:"
    },
    "8": {
      "L": "'Do not harden your hearts as at Meribah, as on the day of Massah in the wilderness,'",
      "M": "'Do not make your hearts stubborn, as at Meribah — as on that day at Massah in the wilderness,'",
      "T": "'Do not harden your hearts the way your fathers did at Meribah—\nthe way they did that day at Massah in the desert.'"
    },
    "9": {
      "L": "'when your fathers tested me and put me to the proof, though they had seen my work.'",
      "M": "'Your ancestors put me to the test and challenged me, even after seeing all I had done.'",
      "T": "'They tested me there — put me to the proof—\neven after they had seen everything I did.'"
    },
    "10": {
      "L": "'For forty years I was weary with that generation and said, \"They are a people who go astray in their heart, and they have not known my ways.\"'",
      "M": "'For forty years I was provoked by that generation and declared, \"This people's heart keeps wandering; they have never learned my ways.\"'",
      "T": "'For forty years that generation wore out my patience.\nI said: these people's hearts are always wandering—\nthey have never truly known my ways.'"
    },
    "11": {
      "L": "'Therefore I swore in my anger, \"They shall not enter into my rest.\"'",
      "M": "'So in my anger I swore: \"They will never enter my rest.\"'",
      "T": "'So I swore in my anger:\nThey will not enter my rest.'"
    }
  },

  # ===========================================================================
  # Psalm 96 — Sing to the LORD a New Song: Universal Praise and Coming Judgment
  # ===========================================================================
  "96": {
    "1": {
      "L": "Sing to the LORD a new song; sing to the LORD, all the earth!",
      "M": "Sing a new song to the LORD; let all the earth sing to the LORD!",
      "T": "Sing to the LORD a new song!\nSing to the LORD, all the earth!"
    },
    "2": {
      "L": "Sing to the LORD, bless his name; proclaim the good news of his salvation from day to day.",
      "M": "Sing to the LORD; praise his name; announce his salvation day after day.",
      "T": "Sing to the LORD.\nPraise his name.\nProclaim his salvation—\nday after day, without end."
    },
    "3": {
      "L": "Declare his glory among the nations, his marvelous works among all the peoples.",
      "M": "Announce his glory among the nations and his wonderful deeds among all peoples.",
      "T": "Declare his glory to every nation.\nHis wonders — to every people."
    },
    "4": {
      "L": "For great is the LORD and greatly to be praised; he is to be feared above all gods.",
      "M": "For the LORD is great and most worthy of praise; he is to be held in awe above every other god.",
      "T": "The LORD is great—\nworthy of all praise—\nto be held in awe above everything called a god."
    },
    "5": {
      "L": "For all the gods of the peoples are idols, but the LORD made the heavens.",
      "M": "All the gods of the nations are nothing — mere idols — but the LORD made the heavens.",
      "T": "All the gods of the nations are empty things.\nBut the LORD made the heavens."
    },
    "6": {
      "L": "Honor and majesty are before him; strength and beauty are in his sanctuary.",
      "M": "Honor and majesty surround him; strength and beauty fill his sanctuary.",
      "T": "Honor and majesty walk before him.\nStrength and beauty fill his sanctuary."
    },
    "7": {
      "L": "Ascribe to the LORD, O families of the peoples, ascribe to the LORD glory and strength.",
      "M": "Give to the LORD, all you families of the nations — give to the LORD glory and strength.",
      "T": "Give to the LORD, all you families of the nations—\ngive to the LORD glory and power."
    },
    "8": {
      "L": "Ascribe to the LORD the glory due his name; bring an offering and come into his courts.",
      "M": "Give to the LORD the honor his name deserves; bring your offering and come into his courts.",
      "T": "Give to the LORD the glory his name deserves.\nBring an offering and come into his courts."
    },
    "9": {
      "L": "Worship the LORD in the beauty of holiness; tremble before him, all the earth!",
      "M": "Worship the LORD in the splendor of his holiness; let all the earth tremble before him.",
      "T": "Bow before the LORD in the beauty of holiness.\nLet all the earth tremble at his presence."
    },
    "10": {
      "L": "Say among the nations, 'The LORD reigns! The world also is established, it shall not be moved; he will judge the peoples with equity.'",
      "M": "Declare among the nations: 'The LORD reigns! The world is set in place and cannot be shaken; he will judge the peoples with justice.'",
      "T": "Declare it among the nations: The LORD reigns!\nThe world stands firm — unshakeable.\nHe will judge every people with equity."
    },
    "11": {
      "L": "Let the heavens be glad and let the earth rejoice; let the sea roar and all that fills it.",
      "M": "Let the heavens rejoice and the earth be glad; let the sea and everything in it roar out.",
      "T": "Let the heavens rejoice.\nLet the earth be glad.\nLet the sea roar—\nand everything that lives in it."
    },
    "12": {
      "L": "Let the field be joyful, and all that is in it; then shall all the trees of the forest rejoice",
      "M": "Let the fields exult and everything in them; let all the trees of the forest shout for joy",
      "T": "Let the fields burst with joy—\neverything in them exulting.\nLet all the forest trees shout for gladness"
    },
    "13": {
      "L": "before the LORD, for he comes, for he comes to judge the earth. He will judge the world with righteousness and the peoples with his faithfulness.",
      "M": "before the LORD, for he is coming — coming to judge the earth. He will judge the world in righteousness and the peoples in his faithfulness.",
      "T": "before the LORD — for he is coming.\nHe is coming to judge the earth.\nHe will judge the world in righteousness,\nand the peoples in his faithfulness."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 91–96 written.')

if __name__ == '__main__':
    main()
