"""
MKT Psalms chapter 119 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-119-119.py

=== Overview ===

Ps 119 (176 v) — The Great Torah Psalm. The longest chapter in the Bible and the longest
    psalm. An elaborate alphabetic acrostic: 22 stanzas of 8 verses each, one per letter
    of the Hebrew alphabet (Aleph through Tav). Every verse in each stanza begins with
    that letter in Hebrew. The structure is devotional, not narrative — a sustained
    meditation on the life of one who loves God's instruction, cycling through petition,
    praise, lament, testimony, and confession.

    The eight Torah synonyms used throughout, with rendering choices:
      H8451 (תּוֹרָה, torah)    → "law" in L/M/T (= the whole body of divine instruction)
      H1697 (דָּבָר, dabar)    → "word" in L/M/T (= what God has spoken/promised)
      H6490 (פִּקּוּד, piqqud)  → "precepts" in L/M/T (= specific directives)
      H2706 (חֹק, choq)       → "statutes" in L/M/T (= enacted decrees)
      H4687 (מִצְוָה, mitsvah) → "commandments" in L/M/T (= direct commands)
      H5713 (עֵדוּת, edut)    → "testimonies" in L/M/T (= solemn declarations/decrees)
      H4941 (מִשְׁפָּט, mishpat)→ "judgments" in L/M/T (= authoritative rulings/ordinances)
      H565  (אִמְרָה, imrah)   → "word"/"promise" in L/M/T (poetic synonym for dabar)

    These eight words rotate through all 176 verses with near-perfect distribution (almost
    every verse has at least one). The T tier treats them as slightly distinct in meaning
    where context warrants but does not invent false distinctions — the psalmist uses them
    as near-synonyms for rhetorical variety.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M/T — consistent with all prior Psalms scripts.

H2617 (חֶסֶד, chesed): "steadfast love" in L/M/T. Appears at vv41, 64, 76, 88, 124,
    149, 159. Each occurrence is the appeal of the afflicted psalmist to God's covenant
    loyalty — not merely affection, but the structured faithfulness of the suzerain to
    his vassal.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M/T. The embodied, desiring self — not the Greek
    immaterial soul. At v20 "my soul is consumed with longing," at v25 "my soul clings to
    the dust," at v81 "my soul faints" — all express the full person in extremity, not a
    disembodied spirit.

H430 (אֱלֹהִים, Elohim): "God" in all tiers.

H835 (אַשְׁרֵי, ashre): "blessed" in L/M/T — the plural construct of well-being/happiness,
    the Psalter's characteristic beatitude form. Not "happy" (too weak) but the full
    benediction of one living in alignment with God's order.

H7585 (שְׁאוֹל, sheol) does not appear in Ps 119. H4194 (מָוֶת, death) appears at v109
    only obliquely ("my life is in my hand"). H6757 (tsalmaveth, shadow of death) does not
    appear here.

Acrostic letter names: The interlinear preserves the Hebrew letter names (ALEPH, BETH,
    GIMEL, etc.) as prefixes on the first token of v1, 9, 17, 25, 33, 41, 49, 57, 65,
    73, 81, 89, 97, 105, 113, 121, 129, 137, 145, 153, 161, 169. These are included at
    the head of the first verse of each stanza in all three tiers, since they are part of
    the canonical structure of the poem.

=== Aspect and tense notes ===

Ps 119 uses a complex mixture of aspects throughout:
    - Perfect (completed) for past testimony: "Before I was afflicted I strayed" (v67),
      "I have inclined my heart" (v112), "I have kept your precepts" (v168).
    - Imperfect/cohortative for ongoing commitment and prayer: "I will keep," "teach me,"
      "give me understanding," "let your steadfast love come."
    - Jussive for petition: "Let not the proud oppress me" (v122), "Let my soul live" (v175).
    These tense distinctions are preserved in all tiers. The T tier brings out the emotional
    arc of petition-within-commitment that characterises the psalm.

=== OT intertextuality ===

v105 — "Your word is a lamp to my feet" — echoes Prov 6:23 ("the commandment is a lamp")
    and anticipates the NT "light of the world" motif (John 8:12, 2 Pet 1:19).
v89 — "Forever, O LORD, your word is firmly established in the heavens" — echoes Isa 40:8
    ("the word of our God will stand forever") and is picked up in Matt 24:35.
v176 — "I have strayed like a lost sheep" — anticipates the Synoptic lost-sheep parable
    (Luke 15:3-7, Matt 18:12-14) and Isa 53:6 ("All we like sheep have gone astray").
v130 — "The opening of your words gives light" — the word as illuminating agent, parallel
    to Gen 1:3 (light by divine speech) and John 1:4-5 (the Word as light).
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
  "119": {

    # =========================================================================
    # ALEPH stanza (vv 1–8) — Blessed are those whose way is blameless
    # =========================================================================
    "1": {
      "L": "ALEPH. Blessed are those whose way is blameless, who walk in the law of the LORD!",
      "M": "ALEPH. How blessed are those who live without fault, walking by the LORD's instruction!",
      "T": "ALEPH.\nBlessed are those whose path is pure—\nwho walk in the law of the LORD."
    },
    "2": {
      "L": "Blessed are those who keep his testimonies and seek him with their whole heart,",
      "M": "Blessed are those who guard his decrees and pursue him with all their heart,",
      "T": "Blessed are those who keep his decrees\nand seek him\nwith an undivided heart—"
    },
    "3": {
      "L": "who also do no iniquity but walk in his ways.",
      "M": "who do nothing wrong but walk in his ways.",
      "T": "who do nothing wrong\nand walk\nin his ways."
    },
    "4": {
      "L": "You have commanded your precepts to be kept diligently.",
      "M": "You have given your precepts to be carefully obeyed.",
      "T": "You have commanded your precepts\nto be faithfully kept."
    },
    "5": {
      "L": "O that my ways were steadfast to keep your statutes!",
      "M": "How I wish my ways were truly set on keeping your statutes!",
      "T": "If only my ways were set firm\nto keep your statutes—"
    },
    "6": {
      "L": "Then I would not be put to shame when I look to all your commandments.",
      "M": "Then I would not be shamed whenever I consider all your commandments.",
      "T": "then I would not be ashamed\nwhen I look on all\nyour commandments."
    },
    "7": {
      "L": "I will praise you with an upright heart when I have learned your righteous judgments.",
      "M": "I will thank you with a sincere heart as I learn your righteous decrees.",
      "T": "I will praise you with an honest heart\nwhen I have learned\nyour righteous judgments."
    },
    "8": {
      "L": "I will keep your statutes — O do not forsake me utterly!",
      "M": "I will keep your statutes — please, LORD, do not abandon me.",
      "T": "I will keep your statutes.\nO LORD, do not forsake me\nutterly."
    },

    # =========================================================================
    # BETH stanza (vv 9–16) — How can a young man keep his way clean?
    # =========================================================================
    "9": {
      "L": "BETH. How can a young man keep his way clean? By guarding it according to your word.",
      "M": "BETH. How can a young person keep their life pure? By living in line with your word.",
      "T": "BETH.\nHow does a young person keep their way pure?\nBy living according to your word."
    },
    "10": {
      "L": "With my whole heart I have sought you; let me not stray from your commandments.",
      "M": "With all my heart I have pursued you — do not let me drift from your commandments.",
      "T": "With my whole heart I have sought you.\nDo not let me wander\nfrom your commandments."
    },
    "11": {
      "L": "Your word I have stored up in my heart so that I might not sin against you.",
      "M": "I have treasured your word in my heart so I will not sin against you.",
      "T": "I have stored your word in my heart\nso that I would not sin\nagainst you."
    },
    "12": {
      "L": "Blessed are you, O LORD; teach me your statutes!",
      "M": "Blessed are you, O LORD — teach me your statutes!",
      "T": "Blessed are you, O LORD.\nTeach me your statutes."
    },
    "13": {
      "L": "With my lips I have recounted all the judgments of your mouth.",
      "M": "With my lips I have declared all the decrees that have come from your mouth.",
      "T": "With my lips I have spoken\nevery judgment\nthat has come from your mouth."
    },
    "14": {
      "L": "In the way of your testimonies I rejoice as much as in all riches.",
      "M": "I rejoice in the path of your decrees as much as in every kind of wealth.",
      "T": "I rejoice in the path of your testimonies\nas much as in\nall riches."
    },
    "15": {
      "L": "I will meditate on your precepts and look to your ways.",
      "M": "I will reflect on your precepts and keep my eyes on your paths.",
      "T": "I will meditate on your precepts\nand look to your ways."
    },
    "16": {
      "L": "I will delight in your statutes; I will not forget your word.",
      "M": "I will delight in your statutes — I will not forget your word.",
      "T": "I will delight in your statutes.\nI will not forget your word."
    },

    # =========================================================================
    # GIMEL stanza (vv 17–24) — Open my eyes to see wondrous things
    # =========================================================================
    "17": {
      "L": "GIMEL. Deal bountifully with your servant, that I may live and keep your word.",
      "M": "GIMEL. Be generous with your servant so that I may live and obey your word.",
      "T": "GIMEL.\nDeal generously with your servant\nso I may live\nand keep your word."
    },
    "18": {
      "L": "Open my eyes, that I may behold wondrous things out of your law.",
      "M": "Open my eyes to see the wonderful truths that lie in your instruction.",
      "T": "Open my eyes\nthat I may see\nthe wonders hidden in your law."
    },
    "19": {
      "L": "I am a stranger on the earth; hide not your commandments from me.",
      "M": "I am a foreigner on this earth — do not hide your commandments from me.",
      "T": "I am a stranger in this world.\nDo not hide your commandments\nfrom me."
    },
    "20": {
      "L": "My soul is consumed with longing for your judgments at all times.",
      "M": "My soul is worn out with longing for your ordinances at every moment.",
      "T": "My soul is consumed with longing\nfor your judgments\nat every hour."
    },
    "21": {
      "L": "You have rebuked the proud, those who are cursed, who stray from your commandments.",
      "M": "You rebuke the arrogant — those who are cursed — who drift from your commandments.",
      "T": "You rebuke the arrogant — those who are cursed—\nwho wander\nfrom your commandments."
    },
    "22": {
      "L": "Remove from me reproach and contempt, for I have kept your testimonies.",
      "M": "Take away the scorn and contempt that fall on me, for I have kept your decrees.",
      "T": "Remove from me reproach and contempt—\nI have kept\nyour testimonies."
    },
    "23": {
      "L": "Even though princes sit and speak against me, your servant meditates on your statutes.",
      "M": "Even when rulers sit together plotting against me, your servant reflects on your statutes.",
      "T": "Even when rulers sit plotting against me,\nyour servant meditates\non your statutes."
    },
    "24": {
      "L": "Your testimonies are my delight and my counselors.",
      "M": "Your decrees are my delight — they are my counselors.",
      "T": "Your testimonies are my delight.\nThey are my counselors."
    },

    # =========================================================================
    # DALETH stanza (vv 25–32) — My soul clings to the dust
    # =========================================================================
    "25": {
      "L": "DALETH. My soul clings to the dust; revive me according to your word.",
      "M": "DALETH. My soul is brought low to the dust — give me life according to your word.",
      "T": "DALETH.\nMy soul clings to the dust.\nRevive me\naccording to your word."
    },
    "26": {
      "L": "I have declared my ways and you answered me; teach me your statutes.",
      "M": "I laid out my ways before you and you listened — now teach me your statutes.",
      "T": "I declared my ways and you heard me.\nNow teach me\nyour statutes."
    },
    "27": {
      "L": "Make me understand the way of your precepts, and I will meditate on your wondrous works.",
      "M": "Help me understand the path of your precepts, and I will ponder your wonderful deeds.",
      "T": "Make me understand the way of your precepts—\nthen I will speak\nof your wonderful works."
    },
    "28": {
      "L": "My soul melts for sorrow; strengthen me according to your word.",
      "M": "My soul dissolves in grief — lift me up according to your word.",
      "T": "My soul is melting with sorrow.\nStrengthen me\naccording to your word."
    },
    "29": {
      "L": "Remove from me the way of lying and graciously grant me your law.",
      "M": "Keep me from every path of falsehood and mercifully give me your instruction.",
      "T": "Remove from me the way of falsehood.\nGraciously grant me\nyour law."
    },
    "30": {
      "L": "I have chosen the way of truth; your judgments I have laid before me.",
      "M": "I have chosen the path of truth and set your decrees before me.",
      "T": "I have chosen the path of truth.\nYour judgments I have set\nbefore me."
    },
    "31": {
      "L": "I have held fast to your testimonies, O LORD; let me not be put to shame.",
      "M": "I have clung to your decrees, O LORD — do not let me be put to shame.",
      "T": "I have clung to your testimonies, O LORD.\nDo not let me be shamed."
    },
    "32": {
      "L": "I run in the way of your commandments when you enlarge my heart.",
      "M": "I will run the path of your commandments when you set my heart free.",
      "T": "I will run the path of your commandments\nwhen you enlarge\nmy heart."
    },

    # =========================================================================
    # HE stanza (vv 33–40) — Teach me, O LORD, the way of your statutes
    # =========================================================================
    "33": {
      "L": "HE. Teach me, O LORD, the way of your statutes, and I will keep it to the end.",
      "M": "HE. Teach me, LORD, the path of your statutes, and I will follow it to the very end.",
      "T": "HE.\nTeach me, LORD, the way of your statutes.\nI will keep it\nto the very end."
    },
    "34": {
      "L": "Give me understanding that I may keep your law and observe it with my whole heart.",
      "M": "Grant me understanding to keep your law and obey it with all my heart.",
      "T": "Give me understanding so I may keep your law\nand observe it\nwith my whole heart."
    },
    "35": {
      "L": "Lead me in the path of your commandments, for I delight in it.",
      "M": "Guide me along the path of your commandments — that is where my delight is.",
      "T": "Make me walk in the path of your commandments—\nfor that is where\nmy delight lies."
    },
    "36": {
      "L": "Incline my heart to your testimonies and not toward dishonest gain.",
      "M": "Turn my heart toward your decrees and away from selfish gain.",
      "T": "Bend my heart toward your testimonies\nand away\nfrom greed."
    },
    "37": {
      "L": "Turn away my eyes from looking at vanity and revive me in your ways.",
      "M": "Turn my eyes away from worthless things and give me life by your ways.",
      "T": "Turn my eyes away from what is worthless.\nRevive me\nby your ways."
    },
    "38": {
      "L": "Confirm your word to your servant, you who are devoted to your fear.",
      "M": "Fulfill your promise to your servant — the promise given to those who revere you.",
      "T": "Confirm your word to your servant—\nthe promise made\nto all who fear you."
    },
    "39": {
      "L": "Turn away the reproach which I dread, for your judgments are good.",
      "M": "Take away the shame I dread, for your decrees are good.",
      "T": "Take away the shame I fear—\nfor your judgments\nare good."
    },
    "40": {
      "L": "Behold, I long for your precepts; revive me in your righteousness.",
      "M": "See how I long for your precepts — give me life through your righteousness.",
      "T": "See how I long for your precepts.\nRevive me\nin your righteousness."
    },

    # =========================================================================
    # VAU stanza (vv 41–48) — Let your steadfast love come to me
    # =========================================================================
    "41": {
      "L": "VAU. Let your steadfast love come to me, O LORD, your salvation according to your word;",
      "M": "VAU. Let your steadfast love come to me, LORD — your salvation just as you have promised,",
      "T": "VAU.\nLet your steadfast love come to me, O LORD—\nyour salvation,\njust as you have promised—"
    },
    "42": {
      "L": "that I may have an answer for him who taunts me, for I trust in your word.",
      "M": "so I will have a reply for those who mock me, because I trust in your word.",
      "T": "so that I have an answer\nfor those who taunt me.\nI trust in your word."
    },
    "43": {
      "L": "And do not take the word of truth utterly out of my mouth, for I have hoped in your judgments.",
      "M": "Do not let me lose the power to speak truth, for my hope is in your decrees.",
      "T": "Do not take the word of truth from my mouth—\nfor my hope rests\nin your judgments."
    },
    "44": {
      "L": "So shall I keep your law continually, forever and ever.",
      "M": "I will keep your law at all times, forever and ever.",
      "T": "Then I will keep your law always—\nforever\nand ever."
    },
    "45": {
      "L": "And I will walk in a wide place, for I have sought your precepts.",
      "M": "I will move freely, for I have sought out your precepts.",
      "T": "I will walk in wide-open freedom—\nfor I have sought\nyour precepts."
    },
    "46": {
      "L": "I will also speak of your testimonies before kings and will not be ashamed.",
      "M": "I will speak of your decrees before kings and will not be ashamed.",
      "T": "I will speak of your testimonies\neven before kings—\nI will not be ashamed."
    },
    "47": {
      "L": "I will delight myself in your commandments, which I love.",
      "M": "I will find my delight in your commandments, which I love.",
      "T": "I will delight in your commandments—\nwhich I love\nwith all my heart."
    },
    "48": {
      "L": "I will lift up my hands toward your commandments, which I love, and I will meditate on your statutes.",
      "M": "I will reach out toward your commandments, which I love, and reflect on your statutes.",
      "T": "I will lift my hands to your commandments, which I love.\nI will meditate\non your statutes."
    },

    # =========================================================================
    # ZAIN stanza (vv 49–56) — Remember your word to your servant
    # =========================================================================
    "49": {
      "L": "ZAIN. Remember your word to your servant, on which you have made me hope.",
      "M": "ZAIN. Remember the word you gave to your servant — the word that gave me hope.",
      "T": "ZAIN.\nRemember your word to your servant—\nthe word by which\nyou gave me hope."
    },
    "50": {
      "L": "This is my comfort in my affliction: that your word has given me life.",
      "M": "This is what comforts me when I suffer: your word has kept me alive.",
      "T": "This is my comfort in affliction:\nyour word\nhas given me life."
    },
    "51": {
      "L": "The arrogant have utterly mocked me, yet I have not turned from your law.",
      "M": "The proud have made fun of me at every turn, yet I have not swerved from your law.",
      "T": "The arrogant have mocked me without mercy—\nbut I have not turned away\nfrom your law."
    },
    "52": {
      "L": "I remember your judgments of old, O LORD, and I am comforted.",
      "M": "I call to mind your ancient decrees, O LORD, and find comfort in them.",
      "T": "I remember your ancient judgments, O LORD—\nand I am comforted."
    },
    "53": {
      "L": "Horror has seized me because of the wicked who forsake your law.",
      "M": "Rage and anguish grip me when I see the wicked forsaking your law.",
      "T": "Horror seizes me\nbecause of the wicked\nwho abandon your law."
    },
    "54": {
      "L": "Your statutes have been my songs in the house of my pilgrimage.",
      "M": "Your statutes have been the songs I sing in this place where I am passing through.",
      "T": "Your statutes have been my songs\nin the house\nof my pilgrimage."
    },
    "55": {
      "L": "I have remembered your name in the night, O LORD, and have kept your law.",
      "M": "I call your name to mind in the night, O LORD, and keep your law.",
      "T": "I remember your name in the night, O LORD,\nand I keep\nyour law."
    },
    "56": {
      "L": "This blessing I have had because I kept your precepts.",
      "M": "This is what has been mine because I kept your precepts.",
      "T": "This is what I have:\nbecause I kept\nyour precepts."
    },

    # =========================================================================
    # CHETH stanza (vv 57–64) — You are my portion, O LORD
    # =========================================================================
    "57": {
      "L": "CHETH. You are my portion, O LORD; I promise to keep your words.",
      "M": "CHETH. The LORD is my portion — this I have declared. I commit to keeping your words.",
      "T": "CHETH.\nYou are my portion, O LORD.\nI have made my vow:\nI will keep your words."
    },
    "58": {
      "L": "I sought your favor with my whole heart; be gracious to me according to your word.",
      "M": "I have asked for your favor with all my heart — be gracious to me as you have promised.",
      "T": "I have sought your favor with my whole heart.\nBe merciful to me\naccording to your word."
    },
    "59": {
      "L": "When I considered my ways, I turned my feet to your testimonies.",
      "M": "When I stopped to think about my life, I turned my steps back to your decrees.",
      "T": "When I thought over my ways,\nI turned my feet\ntoward your testimonies."
    },
    "60": {
      "L": "I hurry and do not delay to keep your commandments.",
      "M": "I was quick and did not hesitate to obey your commandments.",
      "T": "I made haste — I did not delay\nto keep\nyour commandments."
    },
    "61": {
      "L": "The cords of the wicked have entangled me, but I have not forgotten your law.",
      "M": "The wicked have tried to trap me, but I have not forgotten your law.",
      "T": "The cords of the wicked have wrapped around me—\nbut I have not forgotten\nyour law."
    },
    "62": {
      "L": "At midnight I rise to give you thanks for your righteous judgments.",
      "M": "I rise at midnight to thank you for your righteous decrees.",
      "T": "At midnight I rise to give you thanks—\nbecause your judgments\nare righteous."
    },
    "63": {
      "L": "I am a companion of all who fear you and of those who keep your precepts.",
      "M": "I am a friend to all who reverence you and to all who keep your precepts.",
      "T": "I am a companion\nof all who fear you\nand keep your precepts."
    },
    "64": {
      "L": "The earth is full of your steadfast love, O LORD; teach me your statutes.",
      "M": "The earth is full of your steadfast love, O LORD — teach me your statutes.",
      "T": "The earth is full of your steadfast love, O LORD.\nTeach me your statutes."
    },

    # =========================================================================
    # TETH stanza (vv 65–72) — You have dealt well with your servant
    # =========================================================================
    "65": {
      "L": "TETH. You have dealt well with your servant, O LORD, according to your word.",
      "M": "TETH. You have been good to your servant, LORD — just as you promised.",
      "T": "TETH.\nYou have dealt well with your servant, O LORD—\njust as you\nhave promised."
    },
    "66": {
      "L": "Teach me good judgment and knowledge, for I believe in your commandments.",
      "M": "Teach me discernment and understanding, for I trust in your commandments.",
      "T": "Teach me discernment and knowledge—\nfor I have trusted\nin your commandments."
    },
    "67": {
      "L": "Before I was afflicted I strayed, but now I keep your word.",
      "M": "Before I suffered I used to wander; but now I keep your word.",
      "T": "Before I was afflicted, I wandered.\nBut now\nI keep your word."
    },
    "68": {
      "L": "You are good and do good; teach me your statutes.",
      "M": "You are good, and you do what is good — teach me your statutes.",
      "T": "You are good, and you do good.\nTeach me\nyour statutes."
    },
    "69": {
      "L": "The proud have smeared lies against me, but I will keep your precepts with my whole heart.",
      "M": "The arrogant have spread lies about me, but I will keep your precepts with all my heart.",
      "T": "The proud have forged lies against me—\nbut with my whole heart\nI will keep your precepts."
    },
    "70": {
      "L": "Their heart is gross like grease, but I delight in your law.",
      "M": "Their hearts are hardened and insensible, but I delight in your law.",
      "T": "Their heart is as fat as grease—\nbut I delight\nin your law."
    },
    "71": {
      "L": "It is good for me that I was afflicted, that I might learn your statutes.",
      "M": "My suffering was good for me, because it taught me your statutes.",
      "T": "It was good for me to be afflicted—\nso that I could learn\nyour statutes."
    },
    "72": {
      "L": "The law of your mouth is better to me than thousands of pieces of gold and silver.",
      "M": "The instruction that comes from your mouth is worth more to me than thousands of gold and silver coins.",
      "T": "The law from your mouth is better to me\nthan thousands of pieces\nof gold and silver."
    },

    # =========================================================================
    # JOD stanza (vv 73–80) — Your hands have made and fashioned me
    # =========================================================================
    "73": {
      "L": "JOD. Your hands have made me and fashioned me; give me understanding to learn your commandments.",
      "M": "JOD. Your hands made me and formed me — give me understanding to learn your commandments.",
      "T": "JOD.\nYour hands made me and fashioned me.\nGive me understanding\nto learn your commandments."
    },
    "74": {
      "L": "Those who fear you will see me and be glad, because I have hoped in your word.",
      "M": "Those who revere you will see me and be glad, because I have put my hope in your word.",
      "T": "Those who fear you will see me and rejoice—\nbecause I have put my hope\nin your word."
    },
    "75": {
      "L": "I know, O LORD, that your judgments are right and that in faithfulness you have afflicted me.",
      "M": "I know, O LORD, that your decrees are right and that you disciplined me out of faithfulness.",
      "T": "I know, O LORD, that your judgments are right—\nand that out of faithfulness\nyou have afflicted me."
    },
    "76": {
      "L": "Let your steadfast love be my comfort according to your promise to your servant.",
      "M": "Let your faithful love be a comfort to me, just as you promised your servant.",
      "T": "Let your steadfast love be my comfort—\naccording to your word\nto your servant."
    },
    "77": {
      "L": "Let your tender mercies come to me that I may live, for your law is my delight.",
      "M": "Let your compassion come to me so I may live — your law is my delight.",
      "T": "Let your tender mercies come to me so I may live.\nYour law is my delight."
    },
    "78": {
      "L": "Let the proud be put to shame, for they have wronged me without cause; I will meditate on your precepts.",
      "M": "May the proud be shamed — without reason they have twisted things against me; I will reflect on your precepts.",
      "T": "Let the proud be ashamed—\nthey treated me wrongly without cause.\nI will meditate on your precepts."
    },
    "79": {
      "L": "Let those who fear you turn to me, those who know your testimonies.",
      "M": "Let those who fear you gather around me — those who know your decrees.",
      "T": "Let those who fear you turn to me—\nall those who know\nyour testimonies."
    },
    "80": {
      "L": "Let my heart be blameless in your statutes so that I may not be ashamed.",
      "M": "May my heart be wholly devoted to your statutes, so I will not be put to shame.",
      "T": "Let my heart be blameless in your statutes—\nso that I will not be ashamed."
    },

    # =========================================================================
    # CAPH stanza (vv 81–88) — My soul faints for your salvation
    # =========================================================================
    "81": {
      "L": "CAPH. My soul faints for your salvation, but I hope in your word.",
      "M": "CAPH. My soul is worn out waiting for your salvation, but I hope in your word.",
      "T": "CAPH.\nMy soul is faint with longing for your salvation—\nbut I hope\nin your word."
    },
    "82": {
      "L": "My eyes fail with watching for your word; I ask, 'When will you comfort me?'",
      "M": "My eyes are strained looking for your word, asking, 'When will you comfort me?'",
      "T": "My eyes are worn out looking for your word—\nI keep asking:\nwhen will you comfort me?"
    },
    "83": {
      "L": "For I have become like a wineskin in the smoke, yet I have not forgotten your statutes.",
      "M": "I am like a wineskin dried out in the smoke, yet I do not forget your statutes.",
      "T": "I am like a wineskin dried in the smoke—\nyet I have not forgotten\nyour statutes."
    },
    "84": {
      "L": "How long must your servant endure? When will you judge those who pursue me?",
      "M": "How many days of my life are left? When will you bring judgment on those who persecute me?",
      "T": "How long must your servant wait?\nWhen will you execute judgment\non those who pursue me?"
    },
    "85": {
      "L": "The arrogant have dug pits for me; they do not live by your law.",
      "M": "The proud have set traps for me — people who do not follow your law.",
      "T": "The arrogant have dug pits for me—\npeople who have no regard\nfor your law."
    },
    "86": {
      "L": "All your commandments are faithful; they persecute me wrongfully — help me!",
      "M": "All your commands are trustworthy; they are hounding me without cause — help me!",
      "T": "All your commandments are faithful.\nThey are persecuting me without cause—\nhelp me!"
    },
    "87": {
      "L": "They have all but done away with me on earth, but I have not forsaken your precepts.",
      "M": "They nearly destroyed me from the earth, but I have not abandoned your precepts.",
      "T": "They nearly wiped me from the earth—\nbut I did not forsake\nyour precepts."
    },
    "88": {
      "L": "Revive me according to your steadfast love, that I may keep the testimonies of your mouth.",
      "M": "Give me life according to your steadfast love, so that I will obey the decrees that come from your mouth.",
      "T": "Give me life according to your steadfast love—\nthen I will keep\nthe testimony of your mouth."
    },

    # =========================================================================
    # LAMED stanza (vv 89–96) — Forever, O LORD, your word is firmly fixed
    # =========================================================================
    "89": {
      "L": "LAMED. Forever, O LORD, your word is firmly established in the heavens.",
      "M": "LAMED. Your word, O LORD, stands firm forever — fixed in the heavens.",
      "T": "LAMED.\nForever, O LORD, your word is settled—\nfirmly fixed\nin the heavens."
    },
    "90": {
      "L": "Your faithfulness endures through all generations; you established the earth and it stands fast.",
      "M": "Your faithfulness lasts through every generation — you set the earth in place and it holds firm.",
      "T": "Your faithfulness spans every generation.\nYou established the earth\nand it stands firm."
    },
    "91": {
      "L": "They continue to this day according to your ordinances, for all things are your servants.",
      "M": "Everything continues to this day according to your decrees, for all things serve you.",
      "T": "All things continue to this day\naccording to your decrees—\nfor all things are your servants."
    },
    "92": {
      "L": "If your law had not been my delight, I would have perished in my affliction.",
      "M": "If your law had not been my joy, I would have died in my suffering.",
      "T": "If your law had not been my delight,\nI would have perished\nin my affliction."
    },
    "93": {
      "L": "I will never forget your precepts, for by them you have given me life.",
      "M": "I will never forget your precepts, for through them you have kept me alive.",
      "T": "I will never forget your precepts—\nfor through them\nyou have given me life."
    },
    "94": {
      "L": "I am yours; save me, for I have sought your precepts.",
      "M": "I belong to you — rescue me, for I have devoted myself to your precepts.",
      "T": "I am yours — save me!\nFor I have sought out\nyour precepts."
    },
    "95": {
      "L": "The wicked lie in wait to destroy me, but I consider your testimonies.",
      "M": "The wicked lurk to destroy me, but my attention stays fixed on your decrees.",
      "T": "The wicked wait to destroy me—\nbut I give my mind\nto your testimonies."
    },
    "96": {
      "L": "I have seen a limit to all perfection, but your commandment is exceedingly broad.",
      "M": "I have seen that every human achievement has its limits, but your commandment has no bounds.",
      "T": "I have seen that all human perfection has an end—\nbut your commandment\nis boundless."
    },

    # =========================================================================
    # MEM stanza (vv 97–104) — O how I love your law!
    # =========================================================================
    "97": {
      "L": "MEM. O how I love your law! It is my meditation all the day.",
      "M": "MEM. How I love your law! I think about it all day long.",
      "T": "MEM.\nO how I love your law!\nIt is my meditation\nall through the day."
    },
    "98": {
      "L": "Your commandment makes me wiser than my enemies, for it is ever with me.",
      "M": "Your commandments make me wiser than my enemies, for they are always with me.",
      "T": "Your commandments make me wiser than my enemies—\nfor they are always with me."
    },
    "99": {
      "L": "I have more insight than all my teachers, for your testimonies are my meditation.",
      "M": "I understand more than all my teachers do, for your decrees fill my thoughts.",
      "T": "I have more understanding than all my teachers—\nfor your testimonies\nare my meditation."
    },
    "100": {
      "L": "I understand more than the elders, because I keep your precepts.",
      "M": "I discern more than those who are older, because I observe your precepts.",
      "T": "I understand more than the elders—\nbecause I keep\nyour precepts."
    },
    "101": {
      "L": "I have held back my feet from every evil way in order to keep your word.",
      "M": "I have kept my feet from every wrong path so that I could obey your word.",
      "T": "I have held my feet back from every evil path\nso that I might keep\nyour word."
    },
    "102": {
      "L": "I have not departed from your judgments, for you have taught me.",
      "M": "I have not turned away from your decrees, for you yourself have been my teacher.",
      "T": "I have not turned from your judgments—\nfor you\nhave taught me."
    },
    "103": {
      "L": "How sweet are your words to my taste, sweeter than honey to my mouth!",
      "M": "How sweet your words are to me — sweeter than honey in my mouth!",
      "T": "How sweet your words are to my taste—\nsweeter than honey\nto my mouth!"
    },
    "104": {
      "L": "Through your precepts I get understanding; therefore I hate every false way.",
      "M": "Your precepts give me discernment; that is why I hate every path of falsehood.",
      "T": "Through your precepts I gain understanding—\ntherefore I hate\nevery false path."
    },

    # =========================================================================
    # NUN stanza (vv 105–112) — Your word is a lamp to my feet
    # =========================================================================
    "105": {
      "L": "NUN. Your word is a lamp to my feet and a light to my path.",
      "M": "NUN. Your word is a lamp that lights my feet and a light for my path.",
      "T": "NUN.\nYour word is a lamp to my feet\nand a light\nto my path."
    },
    "106": {
      "L": "I have sworn and confirmed it: I will keep your righteous judgments.",
      "M": "I have taken an oath and will hold to it: I will follow your righteous decrees.",
      "T": "I have sworn an oath — and I will keep it:\nto obey your righteous\njudgments."
    },
    "107": {
      "L": "I am severely afflicted; revive me, O LORD, according to your word!",
      "M": "I am deeply afflicted — give me life again, LORD, as you have promised!",
      "T": "I am greatly afflicted.\nRevive me, O LORD—\naccording to your word."
    },
    "108": {
      "L": "Accept, O LORD, the freewill offerings of my mouth, and teach me your judgments.",
      "M": "O LORD, please accept the willing praise of my lips and teach me your decrees.",
      "T": "Accept, O LORD, the willing offerings of my lips—\nand teach me\nyour judgments."
    },
    "109": {
      "L": "My life is in my hand continually, yet I do not forget your law.",
      "M": "I hold my life in my hands at every moment, yet I do not forget your law.",
      "T": "My life is in my hands at every moment—\nbut I do not forget\nyour law."
    },
    "110": {
      "L": "The wicked have set a snare for me, but I have not strayed from your precepts.",
      "M": "The wicked laid a trap for me, but I have not wandered from your precepts.",
      "T": "The wicked have set a snare for me—\nbut I have not strayed\nfrom your precepts."
    },
    "111": {
      "L": "Your testimonies are my heritage forever, for they are the joy of my heart.",
      "M": "Your decrees are mine as an inheritance forever — they are the joy of my heart.",
      "T": "Your testimonies are my heritage forever—\nfor they are the joy\nof my heart."
    },
    "112": {
      "L": "I have inclined my heart to perform your statutes forever, to the very end.",
      "M": "I have set my heart on keeping your statutes always — right to the end.",
      "T": "I have inclined my heart to keep your statutes—\nalways,\nto the very end."
    },

    # =========================================================================
    # SAMECH stanza (vv 113–120) — I hate the double-minded
    # =========================================================================
    "113": {
      "L": "SAMECH. I hate the double-minded, but I love your law.",
      "M": "SAMECH. I hate those who are half-hearted, but your law I love.",
      "T": "SAMECH.\nI hate the double-minded—\nbut I love\nyour law."
    },
    "114": {
      "L": "You are my hiding place and my shield; I hope in your word.",
      "M": "You are my shelter and my shield — I hope in your word.",
      "T": "You are my hiding place and my shield.\nI hope in your word."
    },
    "115": {
      "L": "Depart from me, you evildoers, that I may keep the commandments of my God.",
      "M": "Get away from me, you who do evil — I intend to keep the commands of my God.",
      "T": "Away from me, you evildoers!\nI will keep the commandments\nof my God."
    },
    "116": {
      "L": "Uphold me according to your word that I may live and do not let me be ashamed of my hope.",
      "M": "Sustain me as you have promised so I may live — do not let my hope put me to shame.",
      "T": "Hold me up according to your word so I may live—\ndo not let my hope\nbecome shame."
    },
    "117": {
      "L": "Hold me up, that I may be safe and may look upon your statutes continually.",
      "M": "Support me and I will be safe, and I will keep my gaze fixed on your statutes always.",
      "T": "Hold me up and I will be safe—\ncontinually turning my attention\nto your statutes."
    },
    "118": {
      "L": "You have rejected all who stray from your statutes, for their deceit is falsehood.",
      "M": "You reject all who drift away from your statutes — their deceptions are empty lies.",
      "T": "You have dismissed all who stray from your statutes—\nfor their deceit\nis pure falsehood."
    },
    "119": {
      "L": "All the wicked of the earth you remove like dross; therefore I love your testimonies.",
      "M": "You sweep away all the wicked of the earth like impure dross — therefore I love your decrees.",
      "T": "You sweep away the wicked like dross—\ntherefore I love\nyour testimonies."
    },
    "120": {
      "L": "My flesh trembles for fear of you, and I am in dread of your judgments.",
      "M": "I tremble in awe of you — your judgments fill me with holy dread.",
      "T": "My flesh trembles in fear of you.\nI stand in awe\nof your judgments."
    },

    # =========================================================================
    # AIN stanza (vv 121–128) — I have done what is just and right
    # =========================================================================
    "121": {
      "L": "AIN. I have done what is just and right; do not leave me to my oppressors.",
      "M": "AIN. I have acted with justice and integrity — do not hand me over to those who oppress me.",
      "T": "AIN.\nI have done what is just and right.\nDo not leave me\nto my oppressors."
    },
    "122": {
      "L": "Be a pledge of good to your servant; let not the proud oppress me.",
      "M": "Guarantee good things for your servant — do not let the proud trample me.",
      "T": "Stand surety for your servant's good.\nDo not let the proud\noppress me."
    },
    "123": {
      "L": "My eyes fail from looking for your salvation and for the word of your righteousness.",
      "M": "My eyes are worn out watching for your salvation and for the fulfillment of your righteous promise.",
      "T": "My eyes are failing\nas I look for your salvation—\nfor the word of your righteousness."
    },
    "124": {
      "L": "Deal with your servant according to your steadfast love and teach me your statutes.",
      "M": "Treat your servant according to your steadfast love and teach me your statutes.",
      "T": "Deal with your servant according to your steadfast love.\nTeach me\nyour statutes."
    },
    "125": {
      "L": "I am your servant; give me understanding that I may know your testimonies.",
      "M": "I am your servant — give me discernment to understand your decrees.",
      "T": "I am your servant.\nGive me understanding\nthat I may know your testimonies."
    },
    "126": {
      "L": "It is time for the LORD to act, for they have broken your law.",
      "M": "It is time for you to act, LORD — they have rendered your law void.",
      "T": "It is time for you to act, LORD—\nthey have broken\nyour law."
    },
    "127": {
      "L": "Therefore I love your commandments above gold, yes above fine gold.",
      "M": "Therefore I love your commandments more than gold — more than the finest gold.",
      "T": "Therefore I love your commandments\nmore than gold—\nmore than the finest gold."
    },
    "128": {
      "L": "Therefore I consider all your precepts about everything to be right and I hate every false way.",
      "M": "For that reason I consider all your precepts to be right in every area, and I hate every path of falsehood.",
      "T": "I count all your precepts right in everything—\nand I hate\nevery false path."
    },

    # =========================================================================
    # PE stanza (vv 129–136) — Your testimonies are wonderful
    # =========================================================================
    "129": {
      "L": "PE. Your testimonies are wonderful; therefore my soul keeps them.",
      "M": "PE. Your decrees are wonderful — that is why I treasure them.",
      "T": "PE.\nYour testimonies are wonderful.\nThat is why my soul\nkeeps them."
    },
    "130": {
      "L": "The unfolding of your words gives light; it gives understanding to the simple.",
      "M": "When your words are opened up they shed light; they give understanding to the untrained mind.",
      "T": "When your words are opened, they give light.\nThey give understanding\nto those with no learning."
    },
    "131": {
      "L": "I opened my mouth and panted, for I longed for your commandments.",
      "M": "I opened my mouth and panted in longing — I craved your commandments.",
      "T": "I opened my mouth and panted—\nI was longing\nfor your commandments."
    },
    "132": {
      "L": "Turn to me and be gracious to me, as you do to those who love your name.",
      "M": "Look on me and be merciful, as is your custom toward those who love your name.",
      "T": "Turn to me and be merciful—\nas you do for all those\nwho love your name."
    },
    "133": {
      "L": "Order my steps in your word and let no iniquity have dominion over me.",
      "M": "Keep my steps firm in your word and do not let any sin take control of me.",
      "T": "Steady my steps according to your word—\nlet no sin\nhave dominion over me."
    },
    "134": {
      "L": "Deliver me from human oppression, and I will keep your precepts.",
      "M": "Set me free from human cruelty, and I will keep your precepts.",
      "T": "Deliver me from human oppression—\nand I will keep\nyour precepts."
    },
    "135": {
      "L": "Make your face shine upon your servant and teach me your statutes.",
      "M": "Let your face shine on your servant and teach me your statutes.",
      "T": "Make your face shine on your servant\nand teach me\nyour statutes."
    },
    "136": {
      "L": "Streams of water run down from my eyes because they do not keep your law.",
      "M": "My eyes pour down rivers of tears because people do not keep your law.",
      "T": "Streams of tears run down my eyes—\nbecause your law\nis not kept."
    },

    # =========================================================================
    # TZADDI stanza (vv 137–144) — Righteous are you, O LORD
    # =========================================================================
    "137": {
      "L": "TZADDI. Righteous are you, O LORD, and upright are your judgments.",
      "M": "TZADDI. You are righteous, O LORD, and your decrees are just.",
      "T": "TZADDI.\nRighteous are you, O LORD.\nYour judgments\nare upright."
    },
    "138": {
      "L": "You have commanded your testimonies in righteousness and in all faithfulness.",
      "M": "The decrees you have commanded are righteous and completely trustworthy.",
      "T": "The testimonies you have given are righteous—\nfaithful\nin every way."
    },
    "139": {
      "L": "My zeal has consumed me because my enemies have forgotten your words.",
      "M": "A burning zeal has consumed me, because my enemies disregard your words.",
      "T": "My zeal has consumed me—\nbecause my enemies\nhave forgotten your words."
    },
    "140": {
      "L": "Your word is very pure, and therefore your servant loves it.",
      "M": "Your word is completely pure — that is why your servant loves it.",
      "T": "Your word is utterly pure—\ntherefore your servant\nloves it."
    },
    "141": {
      "L": "I am small and despised, yet I do not forget your precepts.",
      "M": "I am lowly and scorned, but I have not forgotten your precepts.",
      "T": "I am small and looked down on—\nbut I do not forget\nyour precepts."
    },
    "142": {
      "L": "Your righteousness is an everlasting righteousness, and your law is truth.",
      "M": "Your righteousness stands forever, and your law is truth.",
      "T": "Your righteousness is everlasting.\nYour law is truth."
    },
    "143": {
      "L": "Trouble and anguish have found me out, yet your commandments are my delight.",
      "M": "Distress and trouble have overtaken me, yet your commandments are my delight.",
      "T": "Trouble and anguish have come upon me—\nbut your commandments\nare my delight."
    },
    "144": {
      "L": "Your testimonies are righteous forever; give me understanding that I may live.",
      "M": "Your decrees are right for all time — give me understanding so I may live.",
      "T": "The righteousness of your testimonies is everlasting.\nGive me understanding\nthat I may live."
    },

    # =========================================================================
    # KOPH stanza (vv 145–152) — I cry with my whole heart; answer me, O LORD
    # =========================================================================
    "145": {
      "L": "KOPH. With my whole heart I cried; answer me, O LORD! I will keep your statutes.",
      "M": "KOPH. I called out with all my heart — answer me, LORD! I will keep your statutes.",
      "T": "KOPH.\nWith my whole heart I cried — answer me, O LORD!\nI will keep your statutes."
    },
    "146": {
      "L": "I cried to you; save me, that I may keep your testimonies.",
      "M": "I called out to you — save me, so I can keep your decrees.",
      "T": "I cried to you: save me!\nThen I will keep\nyour testimonies."
    },
    "147": {
      "L": "I rise before dawn and cry for help; I hope in your word.",
      "M": "I am awake before daybreak to cry out — I put my hope in your word.",
      "T": "I rise before dawn and cry for help.\nI hope\nin your word."
    },
    "148": {
      "L": "My eyes are awake before the watches of the night, that I may meditate on your word.",
      "M": "I am awake through the night watches to reflect on your word.",
      "T": "My eyes are open before the night watch—\nto meditate\non your word."
    },
    "149": {
      "L": "Hear my voice according to your steadfast love, O LORD; revive me according to your justice.",
      "M": "Listen to me, LORD, in your steadfast love — give me life according to your justice.",
      "T": "Hear my voice, O LORD, in your steadfast love.\nRevive me\naccording to your judgment."
    },
    "150": {
      "L": "They draw near who pursue evil purposes; they are far from your law.",
      "M": "Those who chase after wickedness are closing in on me — they are far from your law.",
      "T": "Those who pursue evil draw near to me.\nThey are far\nfrom your law."
    },
    "151": {
      "L": "But you are near, O LORD, and all your commandments are truth.",
      "M": "But you are near, O LORD — all your commandments are truth.",
      "T": "But you are near, O LORD.\nAll your commandments\nare truth."
    },
    "152": {
      "L": "Long ago I learned from your testimonies that you have founded them forever.",
      "M": "I have known from ancient times about your decrees — you established them to last forever.",
      "T": "From ancient times I have known this about your testimonies:\nyou founded them\nto last forever."
    },

    # =========================================================================
    # RESH stanza (vv 153–160) — Look on my affliction and deliver me
    # =========================================================================
    "153": {
      "L": "RESH. Look upon my affliction and deliver me, for I do not forget your law.",
      "M": "RESH. Look at my suffering and rescue me, for I have not forgotten your law.",
      "T": "RESH.\nLook on my affliction and deliver me—\nfor I have not forgotten\nyour law."
    },
    "154": {
      "L": "Plead my cause and deliver me; give me life according to your word.",
      "M": "Take up my case and rescue me — give me life as you have promised.",
      "T": "Plead my cause and deliver me.\nRevive me\naccording to your word."
    },
    "155": {
      "L": "Salvation is far from the wicked, for they do not seek your statutes.",
      "M": "Rescue is far from the wicked — they have no interest in your statutes.",
      "T": "Salvation is far from the wicked—\nfor they have not sought\nyour statutes."
    },
    "156": {
      "L": "Great are your tender mercies, O LORD; revive me according to your judgments.",
      "M": "Your compassion is vast, O LORD — give me life according to your decrees.",
      "T": "Great are your tender mercies, O LORD.\nRevive me\naccording to your judgments."
    },
    "157": {
      "L": "Many are my persecutors and my enemies, yet I have not turned aside from your testimonies.",
      "M": "I have many persecutors and enemies, yet I have not turned from your decrees.",
      "T": "Many persecutors and enemies surround me—\nbut I have not turned\nfrom your testimonies."
    },
    "158": {
      "L": "I look at the faithless with loathing, because they do not keep your word.",
      "M": "I saw those who were disloyal and it grieved me, because they do not keep your word.",
      "T": "I looked at the faithless and was grieved—\nbecause they would not keep\nyour word."
    },
    "159": {
      "L": "Consider how I love your precepts! Revive me, O LORD, according to your steadfast love.",
      "M": "See how much I love your precepts! Give me life, LORD, in your steadfast love.",
      "T": "See how I love your precepts!\nRevive me, O LORD—\naccording to your steadfast love."
    },
    "160": {
      "L": "The sum of your word is truth, and every one of your righteous judgments endures forever.",
      "M": "The whole of your word is truth, and every one of your righteous decrees stands forever.",
      "T": "The sum of your word is truth.\nEvery one of your righteous judgments\nendures forever."
    },

    # =========================================================================
    # SHIN stanza (vv 161–168) — Princes have persecuted me without cause
    # =========================================================================
    "161": {
      "L": "SHIN. Princes have persecuted me without cause, but my heart stands in awe of your word.",
      "M": "SHIN. Rulers have hounded me without any reason, but my heart trembles in reverence before your word.",
      "T": "SHIN.\nRulers have persecuted me without cause—\nbut my heart stands in awe\nof your word."
    },
    "162": {
      "L": "I rejoice at your word like one who finds great spoil.",
      "M": "I rejoice over your word like someone finding a great treasure.",
      "T": "I rejoice at your word\nlike one who discovers\ngreat plunder."
    },
    "163": {
      "L": "I hate and abhor lying, but I love your law.",
      "M": "I deeply hate falsehood and deception, but I love your law.",
      "T": "I hate and abhor falsehood—\nbut your law\nI love."
    },
    "164": {
      "L": "Seven times a day I praise you for your righteous judgments.",
      "M": "Seven times each day I praise you because your decrees are just.",
      "T": "Seven times a day I praise you—\nbecause of your righteous\njudgments."
    },
    "165": {
      "L": "Great peace have those who love your law; nothing causes them to stumble.",
      "M": "Those who love your law enjoy great peace — nothing will trip them up.",
      "T": "Great peace belongs to those who love your law.\nNothing causes them\nto stumble."
    },
    "166": {
      "L": "I hope for your salvation, O LORD, and I have done your commandments.",
      "M": "I put my hope in your salvation, O LORD, and I have carried out your commandments.",
      "T": "I have hoped for your salvation, O LORD—\nand I have kept\nyour commandments."
    },
    "167": {
      "L": "My soul has kept your testimonies and I love them exceedingly.",
      "M": "I have kept your decrees with my whole being and I love them deeply.",
      "T": "My soul has kept your testimonies—\nand I love them\nexceedingly."
    },
    "168": {
      "L": "I have kept your precepts and your testimonies, for all my ways are before you.",
      "M": "I have obeyed your precepts and your decrees — all my ways are open before you.",
      "T": "I have kept your precepts and your testimonies—\nfor all my ways\nare before you."
    },

    # =========================================================================
    # TAV stanza (vv 169–176) — Let my cry come before you, O LORD
    # =========================================================================
    "169": {
      "L": "TAV. Let my cry come before you, O LORD; give me understanding according to your word.",
      "M": "TAV. Let my cry reach you, O LORD — grant me understanding as you have promised.",
      "T": "TAV.\nLet my cry come before you, O LORD.\nGive me understanding\naccording to your word."
    },
    "170": {
      "L": "Let my plea come before you; deliver me according to your word.",
      "M": "Let my prayer reach you — rescue me as you have promised.",
      "T": "Let my supplication come before you.\nDeliver me\naccording to your word."
    },
    "171": {
      "L": "My lips shall pour forth praise, for you teach me your statutes.",
      "M": "My lips will overflow with praise, because you have taught me your statutes.",
      "T": "My lips will overflow with praise—\nbecause you teach me\nyour statutes."
    },
    "172": {
      "L": "My tongue shall sing of your word, for all your commandments are righteous.",
      "M": "My tongue will celebrate your word, for all your commandments are right.",
      "T": "My tongue will sing of your word—\nfor all your commandments\nare righteousness."
    },
    "173": {
      "L": "Let your hand be ready to help me, for I have chosen your precepts.",
      "M": "Be ready to help me, for I have chosen your precepts.",
      "T": "Let your hand be ready to help me—\nfor I have chosen\nyour precepts."
    },
    "174": {
      "L": "I long for your salvation, O LORD, and your law is my delight.",
      "M": "I have longed for your salvation, O LORD — your law is my delight.",
      "T": "I have longed for your salvation, O LORD.\nYour law is my delight."
    },
    "175": {
      "L": "Let my soul live and it shall praise you; let your judgments help me.",
      "M": "Let me live so that I may praise you — let your decrees sustain me.",
      "T": "Let my soul live — and it will praise you.\nLet your judgments\nhelp me."
    },
    "176": {
      "L": "I have gone astray like a lost sheep; seek your servant, for I do not forget your commandments.",
      "M": "I have wandered away like a lost sheep — come and find me, for I have not forgotten your commandments.",
      "T": "I have strayed like a lost sheep.\nSeek your servant—\nfor I have not forgotten\nyour commandments."
    }

  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 119 written.')

if __name__ == '__main__':
    main()
