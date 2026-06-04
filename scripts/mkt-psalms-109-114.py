"""
MKT Psalms chapters 109–114 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-109-114.py

=== Overview of this unit ===

Ps 109 (31 v) — An imprecatory lament of David. David is surrounded by false accusers;
    the central section (vv6-19) is his prayer for retributive judgment on his primary
    adversary (the shift from plural "they" in vv2-5 to singular "he" in vv6-19 signals
    one chief enemy). The psalm moves from lament → imprecation → plea → confidence → vow.
    This is not private vindictiveness: the psalm is addressed to God as the righteous
    judge. The imprecation is the inverse of the covenant blessings — the enemy receives
    the curses that fall on covenant-breakers (cf. Deut 28).

    Key structure:
      vv1-5:   Lament — enemies repay love with accusation
      vv6-19:  Imprecation against the chief enemy (singular)
      v20:     Transition — "Let this be the reward of my adversaries"
      vv21-25: Personal plea — poor, needy, fading, mocked
      vv26-27: Prayer for rescue and recognition
      vv28-29: Confidence in reversal
      vv30-31: Vow to praise in the congregation

    Acts 1:20 quotes v8 ("Let another take his office") as fulfilled in Judas Iscariot.

Ps 110 (7 v) — The most-quoted OT text in the NT (Matt 22:44; Mark 12:36; Luke 20:42;
    Acts 2:34; Heb 1:13; 5:6; 7:17, 21; 10:13). A royal-messianic psalm of David.
    Two divine oracles dominate: the enthronement oracle (v1: "Sit at my right hand")
    and the priestly oracle (v4: "You are a priest forever after the order of Melchizedek").
    The psalm fuses the offices of king and priest in one figure — the foundation of
    Hebrews' Christology. V1 presents a dialogue between YHWH and "my Lord" (Heb. le'adoni,
    to my lord) — the psalmist addresses his own overlord/king as "lord" while YHWH
    addresses that king from the divine throne.

Ps 111 (10 v) — Acrostic (22 half-lines, one for each letter of the Hebrew alphabet).
    A praise hymn for God's works. V10 ("the fear of the LORD is the beginning of wisdom")
    is programmatic wisdom — parallel to Prov 1:7 and Job 28:28. Paired with Ps 112: God's
    character (111) is mirrored in the righteous person (112).

Ps 112 (10 v) — Acrostic, paired with 111. Focuses on the blessed person who fears the
    LORD. V9 is quoted in 2 Cor 9:9 ("he has distributed freely, he has given to the poor;
    his righteousness endures forever") as the character of the generous giver.

Ps 113 (9 v) — First of the Hallel Psalms (113–118), sung at Passover, Pentecost, and
    Tabernacles. The Hallel would have been sung at the Last Supper (cf. Matt 26:30;
    Mark 14:26: "when they had sung a hymn"). V7-8 echo the Hannah song (1 Sam 2:7-8)
    and anticipates the Magnificat (Luke 1:52-53).

Ps 114 (8 v) — Second Hallel Psalm. The Exodus retold as cosmic drama: creation (sea,
    Jordan, mountains, hills) is personified as fleeing in terror at God's presence.
    The rhetoric is interrogative: "What ailed you?" The answer is never spoken — the
    presence of the God of Jacob is its own sufficient explanation. V8 recalls the
    water-from-the-rock tradition (Exod 17:6; Num 20:11).

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M/T throughout — consistent with all prior Psalms
    scripts.

H2617 (חֶסֶד, chesed) at Ps 109:12, 21, 26: "steadfast love" in L; "loyal kindness" /
    "steadfast love" in M/T. At v12 chesed is the covenant-loyalty that no one shows the
    enemy's orphans — rendered "steadfast love" (L) / "loyal kindness" (M/T) to capture
    the human dimension of the term as well as the divine. At vv21, 26 it is the ground of
    David's appeal to God — "steadfast love" throughout.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. At Ps 109:1 the phrase "God of my praise"
    (El tehillati) is retained as vocative; at v26 "LORD my God" combines both divine
    names.

H5315 (נֶפֶשׁ, nefesh) in Ps 109: "soul" in L/T; "life" or "soul" in M depending on
    context. At v20 "against my soul" = against my life/person — "against me" in M.
    At v31 "his soul" = his life — "him" in M.

H7854 (שָׂטָן, satan) at Ps 109:6: "accuser" in L/M; "adversary in court" in T. The
    Hebrew satan here is the legal-adversary role, not the proper noun "Satan" (NT Devil).
    The parallel with "stand at his right hand" (the position of the accusing witness in
    an Israelite trial) confirms the forensic context.

H6486 (פְּקֻדָּה, pequddah) at Ps 109:8: "office/position" in L/M/T. The term denotes
    an appointed oversight role. Quoted in Acts 1:20 (LXX episkopen) for the vacancy left
    by Judas. Rendered "office" (L) / "position" (M) / "place of responsibility" (T).

H5002 (נְאוּם, ne'um) at Ps 110:1: "declaration of / says" — the prophetic-oracle
    formula (neum-YHWH = "oracle of the LORD" / "says the LORD"). Here rendered "The
    LORD declared" (M) and "The LORD's decree" (T) to retain the solemnity of the
    formula.

H113 (אָדֹן, adon) at Ps 110:1: "my Lord" (le'adoni = to my lord) — the second
    occurrence refers to the royal figure the psalmist addresses, not to God. Rendered
    "my Lord" in L and preserved with context in M/T.

H1700 (דִּבְרָה, dibrah) at Ps 110:4: "order" — as in "according to the manner/order
    of." The Melchizedek comparison draws on Gen 14:18-20 (priest-king of Salem who
    blessed Abram and received tithes). Hebrews 7 unpacks this extensively.

H7307 (רוּחַ, ruach) does not appear in this unit.

H3374 (יִרְאַת, yir'at) + H3068 at Ps 111:10 / 112:1: "fear of the LORD" — retained
    in all tiers. This is reverence-in-relationship, not dread. In T tier the relational
    quality is surfaced: "live in the fear of the LORD."

Acrostic structure (Pss 111, 112): The Hebrew acrostic (22 letters of the Hebrew
    alphabet across 22 half-lines per psalm) cannot be reproduced in English without
    forcing awkward alphabetic constructions. It is noted in the header only; the English
    follows the sense of each line. The T tier honors the compact, epigrammatic style the
    acrostic demands.

Hallel identity (Pss 113–114): The opening "Praise the LORD" (Hallelu-Yah) is
    transliterated as a liturgical marker in all tiers — "Praise the LORD!" is the
    English equivalent that best carries the assembly-context of the term.

=== Aspect and tense notes ===

Ps 109: The imprecatory section (vv6-19) uses jussives throughout — "let him be..."
    These are wishes/prayers, not statements. The L tier preserves "let him be" /
    "may it be" to honour the jussive. The M tier also uses "let" constructions. The T
    tier maintains the petitionary register.

Ps 110: V1 uses perfect for the oracle ("The LORD has declared" / "has sworn") —
    the prophetic perfect of certainty. The military imagery (vv2, 5-6) uses
    imperfect-consecutive (narrative future certain). V4 is a second perfect oracle.

Ps 111-112: Praise hymns use participial forms for God's ongoing works — "he is
    gracious," "he gives." These are habitual/characterising presents, not past acts.

Ps 113: The rhetorical question in vv5-6 ("who is like...?") expects no answer.
    V9 uses the participle for God's action on the barren woman — ongoing divine habit.

Ps 114: All verbs are perfects describing the Exodus as a completed, definitive act.
    The interrogative vv5-6 use imperfect-consecutive with a waw — "and you fled." V7
    shifts to imperative: "Tremble!"

=== OT echoes and NT connections ===

Ps 109:8 → Acts 1:20 (Judas; quoted directly)
Ps 110:1 → Matt 22:44; Mark 12:36; Luke 20:42-43; Acts 2:34; Heb 1:13
Ps 110:4 → Heb 5:6; 5:10; 6:20; 7:3, 11, 15, 17, 21
Ps 112:9 → 2 Cor 9:9
Ps 113:7-8 → 1 Sam 2:7-8 (Hannah); Luke 1:52-53 (Magnificat)
Ps 114 → Passover Haggadah; the sea and Jordan as witnesses of the Exodus
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
  # Psalm 109 — Imprecatory Lament of David
  # Enemies repay love with false accusation; David appeals to God the judge
  # ===========================================================================
  "109": {
    # --- Superscription and opening lament (vv1-5) ---
    "1": {
      "L": "A Psalm of David. O God of my praise, do not hold your peace!",
      "M": "A Psalm of David. O God — the one I praise — do not be silent!",
      "T": "A Psalm of David.\nO God, whom I praise —\ndo not hold your peace!"
    },
    "2": {
      "L": "For the mouths of the wicked and the deceitful are opened against me; they have spoken against me with a lying tongue.",
      "M": "The mouths of the wicked and the treacherous are open wide against me; they have spoken against me with false words.",
      "T": "Wicked mouths, lying mouths —\nthey have opened wide against me.\nThey speak nothing but deceit."
    },
    "3": {
      "L": "They have surrounded me with words of hatred and attacked me without cause.",
      "M": "They encircle me with hateful words and fight against me for no reason.",
      "T": "They surround me with words of hatred.\nThey fight against me —\nfor no reason at all."
    },
    "4": {
      "L": "In return for my love they accuse me, but I am in prayer.",
      "M": "In exchange for my love they have become my adversaries, though I give myself to prayer.",
      "T": "I loved them — and they became my accusers.\nI gave myself to prayer\nwhile they sharpened their case against me."
    },
    "5": {
      "L": "They have repaid me evil for good and hatred for my love.",
      "M": "They have paid me back evil for good and hatred in place of my love.",
      "T": "Good — they repaid it with evil.\nLove —\nthey repaid it with hatred."
    },
    # --- Imprecation against the chief enemy (vv6-19) ---
    "6": {
      "L": "Appoint a wicked man over him; let an accuser stand at his right hand.",
      "M": "Set a wicked man to judge him; let an accuser take his place at his right hand.",
      "T": "Appoint a wicked man to stand over him.\nLet an adversary in court\ntake his place at his right hand."
    },
    "7": {
      "L": "When he is judged, let him be found guilty; let his prayer be counted as sin.",
      "M": "When he faces judgment, let him be condemned; let even his prayer be turned against him.",
      "T": "When he comes before the judge — let him be condemned.\nEven his prayer —\nlet it be held against him."
    },
    "8": {
      "L": "Let his days be few; let another take his office.",
      "M": "Let his life be cut short; let someone else take his position.",
      "T": "Let his days be few.\nLet another take over\nhis place of responsibility."
    },
    "9": {
      "L": "Let his children become fatherless and his wife a widow.",
      "M": "Let his children be left without a father and his wife become a widow.",
      "T": "His children — let them lose their father.\nHis wife —\nlet her become a widow."
    },
    "10": {
      "L": "Let his children wander and beg and seek their bread from their desolate places.",
      "M": "Let his children wander and beg, searching for bread far from their ruined homes.",
      "T": "Let his children wander — begging for bread —\nsearching through the ruins\nof what was once home."
    },
    "11": {
      "L": "Let the creditor seize all that he has; let strangers plunder the fruit of his labor.",
      "M": "Let creditors take everything he owns; let foreigners carry off all he has worked for.",
      "T": "Let the creditor take everything.\nWhat he labored for —\nlet strangers carry it all away."
    },
    "12": {
      "L": "Let there be none to extend steadfast love to him, nor any to show favor to his fatherless children.",
      "M": "Let no one show him loyal kindness or take pity on the children he left behind.",
      "T": "Let no one show him mercy.\nLet no one take pity\non the children he orphaned."
    },
    "13": {
      "L": "Let his posterity be cut off; let their name be blotted out in the following generation.",
      "M": "Let his line come to an end; let his family name be wiped out in the next generation.",
      "T": "Let his line be cut off.\nLet his name\nbe erased from the face of history."
    },
    "14": {
      "L": "Let the iniquity of his fathers be remembered before the LORD, and let not his mother's sin be blotted out.",
      "M": "Let the LORD keep his fathers' guilt on record and never wipe out his mother's sin.",
      "T": "Let the LORD keep his fathers' guilt on record.\nLet his mother's sin\nnever be erased."
    },
    "15": {
      "L": "Let them be before the LORD continually, that he may cut off the memory of them from the earth.",
      "M": "Let all those sins stand always before the LORD, until he wipes out their very memory from the earth.",
      "T": "Let those sins stay before the LORD — always —\nuntil he cuts off\neven the memory of them from the earth."
    },
    "16": {
      "L": "Because he did not remember to show steadfast love, but pursued the poor and needy and the brokenhearted, to put them to death.",
      "M": "For he never thought to show loyal kindness, but hounded the poor, the needy, and the brokenhearted, intent on killing them.",
      "T": "He never thought to show mercy.\nInstead, he hunted the poor and the brokenhearted —\ndriven to destroy them."
    },
    "17": {
      "L": "He loved cursing; let it come upon him! He did not delight in blessing; let it be far from him!",
      "M": "He loved to curse others — let curses fall on him! He took no pleasure in blessing — let blessing stay far away from him!",
      "T": "He loved to curse — let curses fall on him.\nHe never cared for blessing —\nlet blessing be far, far from him."
    },
    "18": {
      "L": "He clothed himself with cursing as his garment; let it enter his body like water and his bones like oil.",
      "M": "He wrapped himself in curses like a coat; let that curse seep into his body like water and into his bones like oil.",
      "T": "He wore curses like a coat.\nMay those curses soak into his body like water,\ninto his very bones like oil."
    },
    "19": {
      "L": "Let it be like a garment that he wraps around him, like a belt that he wears every day.",
      "M": "Let it cling to him like the clothing he wears, like a belt strapped on every single day.",
      "T": "Let it be what he wears —\nthe garment he pulls around himself,\nthe belt fastened on day after day."
    },
    # --- Transition (v20) ---
    "20": {
      "L": "This is the reward of my adversaries from the LORD — of those who speak evil against my soul.",
      "M": "Let the LORD repay my accusers with all of this — those who speak evil against me.",
      "T": "This is what I ask the LORD to bring\non those who accuse me —\non all who speak evil against my life."
    },
    # --- Personal plea (vv21-25) ---
    "21": {
      "L": "But you, O Lord GOD, act on my behalf for your name's sake; because your steadfast love is good, deliver me!",
      "M": "But you, O Lord GOD, deal with me for the sake of your own name; your steadfast love is good — deliver me!",
      "T": "But you — O Lord GOD —\nact for me, for your own name's sake.\nYour steadfast love is good.\nDeliver me."
    },
    "22": {
      "L": "For I am poor and needy, and my heart is wounded within me.",
      "M": "For I am poor and in need, and my heart is deeply wounded within me.",
      "T": "I am poor and needy —\nmy heart\nis pierced within me."
    },
    "23": {
      "L": "I fade like a lengthening shadow; I am shaken off like a locust.",
      "M": "I am fading like an evening shadow, brushed away like a locust.",
      "T": "I am fading like a shadow at evening —\nshaken off\nlike a locust brushed from a sleeve."
    },
    "24": {
      "L": "My knees are weak from fasting, and my flesh has become thin, without fat.",
      "M": "My knees buckle from fasting; my body has wasted away, lean and gaunt.",
      "T": "My knees are weak with fasting.\nMy body is skin and bone —\nno substance left."
    },
    "25": {
      "L": "I have become a reproach to them; when they see me, they shake their heads.",
      "M": "I am the object of their scorn; when they catch sight of me, they shake their heads.",
      "T": "I have become an object of mockery.\nThey see me —\nand they shake their heads."
    },
    # --- Prayer for rescue (vv26-27) ---
    "26": {
      "L": "Help me, O LORD my God! Save me according to your steadfast love.",
      "M": "Help me, O LORD my God; save me in keeping with your steadfast love.",
      "T": "Help me, LORD my God!\nSave me\naccording to your steadfast love."
    },
    "27": {
      "L": "Let them know that this is your hand — that you, O LORD, have done it.",
      "M": "Let them see that your hand is behind this — that you, LORD, are the one who has acted.",
      "T": "Let them know: this is your hand.\nYou, LORD —\nyou are the one who has done this."
    },
    # --- Confidence in reversal (vv28-29) ---
    "28": {
      "L": "Let them curse, but you will bless; when they arise, let them be put to shame, but may your servant rejoice.",
      "M": "Let them curse — you will bless. When they rise against me, let them be shamed; but let your servant be glad.",
      "T": "Let them curse — but you, you will bless.\nWhen they rise up against me, let them be put to shame.\nLet your servant rejoice."
    },
    "29": {
      "L": "Let my accusers be clothed with dishonor; let them be wrapped in their own shame as in a cloak.",
      "M": "Let my accusers be dressed in disgrace and wrapped in their own shame like a mantle.",
      "T": "Let my accusers wear disgrace.\nLet them be wrapped in shame\nlike a mantle thrown around their shoulders."
    },
    # --- Vow of praise (vv30-31) ---
    "30": {
      "L": "I will give great thanks to the LORD with my mouth; I will praise him in the midst of the multitude.",
      "M": "With my voice I will give the LORD great thanks; I will praise him among the gathered crowd.",
      "T": "With my mouth I will give the LORD great thanks.\nI will praise him\nin the midst of the crowd."
    },
    "31": {
      "L": "For he stands at the right hand of the needy, to save him from those who condemn his soul.",
      "M": "For he stands at the right hand of the poor person, to rescue him from all who would condemn him.",
      "T": "For he stands at the right hand of the poor —\nto save them\nfrom those who would condemn them."
    }
  },

  # ===========================================================================
  # Psalm 110 — Royal-Messianic Psalm of David
  # Two divine oracles: the enthronement (v1) and the priestly oath (v4)
  # ===========================================================================
  "110": {
    "1": {
      "L": "A Psalm of David. The declaration of the LORD to my Lord: Sit at my right hand, until I make your enemies your footstool.",
      "M": "A Psalm of David. The LORD declared to my Lord: 'Sit at my right hand until I make your enemies a stool for your feet.'",
      "T": "A Psalm of David.\nThe LORD's decree to my Lord:\n'Sit at my right hand\nuntil I make your enemies\na footstool beneath your feet.'"
    },
    "2": {
      "L": "The LORD sends forth from Zion your mighty scepter. Rule in the midst of your enemies!",
      "M": "The LORD extends your powerful scepter from Zion: rule over your enemies!",
      "T": "The LORD sends out your strong scepter from Zion.\nRule —\nright in the middle of your enemies."
    },
    "3": {
      "L": "Your people offer themselves willingly on the day of your power, in holy splendor; from the womb of the morning, the dew of your youth is yours.",
      "M": "On the day you march to war, your people volunteer freely, arrayed in holy splendor. Like dew born from the womb of the dawn, your young warriors come to you.",
      "T": "On the day you go to war —\nyour people come to you willingly,\narrayed in holy splendor.\nLike dew from the womb of the dawn,\nyour young warriors gather."
    },
    "4": {
      "L": "The LORD has sworn and will not relent: You are a priest forever after the order of Melchizedek.",
      "M": "The LORD has taken an oath he will not revoke: 'You are a priest forever, of the same order as Melchizedek.'",
      "T": "The LORD has sworn — and will not go back on it:\n'You are a priest forever,\nof the order of Melchizedek.'"
    },
    "5": {
      "L": "The Lord is at your right hand; he will shatter kings on the day of his wrath.",
      "M": "The Lord stands at your right hand; he will crush kings on the day of his wrath.",
      "T": "The Lord stands at your right hand.\nOn the day of his wrath —\nhe will shatter kings."
    },
    "6": {
      "L": "He will execute judgment among the nations, filling them with corpses; he will shatter the chief over the wide earth.",
      "M": "He will bring judgment on the nations, filling the land with the dead; he will crush rulers across the wide earth.",
      "T": "He will judge the nations —\ncorpses will fill the earth.\nHe will crush rulers\nacross the whole wide world."
    },
    "7": {
      "L": "He will drink from the brook by the way; therefore he will lift up his head.",
      "M": "He drinks from the stream along the road, and because of this he will hold his head high.",
      "T": "He drinks from the brook beside the road.\nAnd so —\nhe lifts his head high."
    }
  },

  # ===========================================================================
  # Psalm 111 — Acrostic Praise for God's Works and Character
  # 22 half-lines, one per letter of the Hebrew alphabet; paired with Ps 112
  # ===========================================================================
  "111": {
    "1": {
      "L": "Praise the LORD! I will give thanks to the LORD with my whole heart, in the company of the upright, in the congregation.",
      "M": "Praise the LORD! I will thank the LORD with my whole heart, in the gathering of the upright, in the full congregation.",
      "T": "Praise the LORD!\nWith my whole heart I will give thanks to the LORD —\nin the company of the upright,\nin the full congregation."
    },
    "2": {
      "L": "Great are the works of the LORD, sought out by all who delight in them.",
      "M": "The works of the LORD are great, studied carefully by all who find pleasure in them.",
      "T": "Great are the works of the LORD —\npored over by all\nwho take delight in them."
    },
    "3": {
      "L": "His work is full of honor and majesty, and his righteousness endures forever.",
      "M": "All he does is glorious and majestic, and his righteousness endures forever.",
      "T": "His work is splendor and majesty in full.\nHis righteousness —\nit endures forever."
    },
    "4": {
      "L": "He has made his wonderful works to be remembered; the LORD is gracious and compassionate.",
      "M": "He has made his wonders unforgettable; the LORD is gracious and full of compassion.",
      "T": "He made his wonders memorable.\nThe LORD is gracious —\nfull of compassion."
    },
    "5": {
      "L": "He has given food to those who fear him; he remembers his covenant forever.",
      "M": "He provides food for all who fear him; he is always mindful of his covenant.",
      "T": "He gives food to those who fear him.\nHe is mindful of his covenant —\nalways, forever."
    },
    "6": {
      "L": "He has shown his people the power of his works, in giving them the inheritance of the nations.",
      "M": "He showed his people what his works can do, giving them the nations' land as their possession.",
      "T": "He showed his people the power of his works —\ngiving them the nations' land\nas their inheritance."
    },
    "7": {
      "L": "The works of his hands are faithfulness and justice; all his precepts are sure.",
      "M": "Everything he does is faithful and just; all his instructions are reliable.",
      "T": "His works are faithfulness and justice.\nAll his commandments —\ntrusty, reliable, sure."
    },
    "8": {
      "L": "They stand firm forever and ever, performed with faithfulness and uprightness.",
      "M": "They hold firm forever and ever, carried out with complete faithfulness and integrity.",
      "T": "They stand firm — forever and ever —\ndone in faithfulness\nand integrity."
    },
    "9": {
      "L": "He sent redemption to his people; he has ordained his covenant forever. Holy and awesome is his name.",
      "M": "He sent redemption to his people and established his covenant forever. His name is holy and full of awe.",
      "T": "He sent redemption to his people.\nHe established his covenant forever.\nHoly and awesome is his name."
    },
    "10": {
      "L": "The fear of the LORD is the beginning of wisdom; a good understanding have all those who practice it. His praise endures forever.",
      "M": "The fear of the LORD is where wisdom begins; those who live by it gain deep understanding. His praise endures forever.",
      "T": "The fear of the LORD is where wisdom begins.\nAll who live by it understand deeply.\nHis praise endures forever."
    }
  },

  # ===========================================================================
  # Psalm 112 — Acrostic Portrait of the Righteous Person
  # Paired with 111; God's character mirrored in the one who fears him
  # ===========================================================================
  "112": {
    "1": {
      "L": "Praise the LORD! Blessed is the man who fears the LORD, who greatly delights in his commandments.",
      "M": "Praise the LORD! How blessed is the one who fears the LORD and finds great joy in his commands!",
      "T": "Praise the LORD!\nBlessed is the one who fears the LORD —\nwho deeply delights in his commands."
    },
    "2": {
      "L": "His offspring will be mighty in the land; the generation of the upright will be blessed.",
      "M": "His children will be a powerful presence in the land; the descendants of the upright will be blessed.",
      "T": "His children will be a force in the land.\nThe generation of the upright —\nblessed."
    },
    "3": {
      "L": "Wealth and riches are in his house, and his righteousness endures forever.",
      "M": "Prosperity and riches fill his home, and his righteousness endures forever.",
      "T": "Wealth and riches are in his house.\nHis righteousness —\nit endures forever."
    },
    "4": {
      "L": "Light dawns in the darkness for the upright; he is gracious, compassionate, and righteous.",
      "M": "Even in the dark, light breaks for the upright; he is gracious, compassionate, and righteous.",
      "T": "In darkness, light dawns for the upright.\nHe is gracious, compassionate,\nand righteous."
    },
    "5": {
      "L": "Good is the man who is generous and lends; who conducts his affairs with justice.",
      "M": "It goes well with the one who is generous in lending and manages his business with justice.",
      "T": "Good things come to the one who is generous,\nwho lends freely\nand runs his affairs with justice."
    },
    "6": {
      "L": "For the righteous will never be moved; he will be remembered forever.",
      "M": "The righteous will never be shaken; they will be remembered forever.",
      "T": "The righteous will never be shaken.\nThey will be remembered —\nforever."
    },
    "7": {
      "L": "He is not afraid of evil tidings; his heart is firm, trusting in the LORD.",
      "M": "He does not fear bad news; his heart is steady, trusting in the LORD.",
      "T": "He is not afraid of bad news.\nHis heart is steady —\ntrusting in the LORD."
    },
    "8": {
      "L": "His heart is established; he will not be afraid, until he looks in triumph on his adversaries.",
      "M": "His heart is steady; he will not fear. In the end he will see his enemies get what they deserve.",
      "T": "His heart is steady — he will not be afraid —\nuntil the day he looks on his enemies\nand sees what has come to them."
    },
    "9": {
      "L": "He has distributed freely; he has given to the poor; his righteousness endures forever; his horn is exalted in honor.",
      "M": "He gives freely to the poor; his righteousness endures forever; his honor is lifted high.",
      "T": "He gives freely — to the poor.\nHis righteousness endures forever.\nHis honor is exalted."
    },
    "10": {
      "L": "The wicked man sees it and is angry; he gnashes his teeth and melts away; the desire of the wicked will perish.",
      "M": "The wicked see all this and seethe; they grind their teeth and waste away. What the wicked crave will come to nothing.",
      "T": "The wicked see it — and rage.\nThey gnash their teeth and waste away.\nWhat the wicked desire —\nit will all come to nothing."
    }
  },

  # ===========================================================================
  # Psalm 113 — First Hallel: The God Who Stoops
  # Opening of the Passover Hallel (Pss 113–118); echoes Hannah and Magnificat
  # ===========================================================================
  "113": {
    "1": {
      "L": "Praise the LORD! Praise, O servants of the LORD, praise the name of the LORD!",
      "M": "Praise the LORD! Let those who serve the LORD give praise — praise the name of the LORD!",
      "T": "Praise the LORD!\nO servants of the LORD — praise!\nPraise the name of the LORD!"
    },
    "2": {
      "L": "Blessed be the name of the LORD from this time forth and forevermore!",
      "M": "Let the name of the LORD be praised from now and for all time to come!",
      "T": "Let the name of the LORD be blessed —\nfrom now\nand forevermore!"
    },
    "3": {
      "L": "From the rising of the sun to its setting, the name of the LORD is to be praised!",
      "M": "From the rising of the sun to where it sets, the name of the LORD deserves all praise!",
      "T": "From sunrise to sunset —\nfrom east to west —\nthe name of the LORD is to be praised."
    },
    "4": {
      "L": "The LORD is high above all nations, and his glory is above the heavens.",
      "M": "The LORD reigns above all nations; his glory soars above the very heavens.",
      "T": "The LORD is high above all nations.\nHis glory —\nabove the very heavens."
    },
    "5": {
      "L": "Who is like the LORD our God, who dwells on high,",
      "M": "Who can compare with the LORD our God, who has his throne so high above —",
      "T": "Who is like the LORD our God —\nthroned on high,"
    },
    "6": {
      "L": "who humbles himself to look upon the heavens and the earth?",
      "M": "yet bends down to look at both heaven and earth?",
      "T": "yet who stoops down\nto look at heaven and earth?"
    },
    "7": {
      "L": "He raises the poor from the dust and lifts the needy from the ash heap,",
      "M": "He lifts the poor out of the dust and raises the needy from the garbage heap,",
      "T": "He raises the poor from the dust —\nhe lifts the needy\nfrom the ash heap,"
    },
    "8": {
      "L": "to make them sit with princes, with the princes of his people.",
      "M": "to seat them alongside princes — the princes of his own people.",
      "T": "to seat them beside princes —\nthe princes\nof his own people."
    },
    "9": {
      "L": "He gives the barren woman a home, making her a joyful mother of children. Praise the LORD!",
      "M": "He gives the childless woman a home, turning her into a glad mother of children. Praise the LORD!",
      "T": "He gives the barren woman a home —\nhe makes her a joyful mother of children.\nPraise the LORD!"
    }
  },

  # ===========================================================================
  # Psalm 114 — Second Hallel: The Exodus as Cosmic Drama
  # Creation personified fleeing at God's presence; water from the rock
  # ===========================================================================
  "114": {
    "1": {
      "L": "When Israel went out from Egypt, the house of Jacob from a people of strange language,",
      "M": "When Israel came out of Egypt, when the family of Jacob left a people of foreign speech,",
      "T": "When Israel came out of Egypt —\nJacob's house\nleaving a people of strange speech —"
    },
    "2": {
      "L": "Judah became his sanctuary, Israel his dominion.",
      "M": "Judah became God's holy place, Israel his kingdom.",
      "T": "Judah became his sanctuary.\nIsrael —\nhis dominion."
    },
    "3": {
      "L": "The sea saw it and fled; the Jordan turned back.",
      "M": "The sea saw and fled; the Jordan reversed its course.",
      "T": "The sea looked — and fled.\nThe Jordan\nturned and ran."
    },
    "4": {
      "L": "The mountains skipped like rams and the hills like young lambs.",
      "M": "The mountains leaped like rams and the hills like young lambs.",
      "T": "The mountains skipped like rams.\nThe hills —\nlike young lambs."
    },
    "5": {
      "L": "What ailed you, O sea, that you fled? O Jordan, that you turned back?",
      "M": "What happened to you, sea, that you ran? And you, Jordan — that you reversed your course?",
      "T": "What ailed you, O sea — that you fled?\nO Jordan —\nthat you turned and ran?"
    },
    "6": {
      "L": "O mountains, that you skipped like rams? O hills, like young lambs?",
      "M": "You mountains — why did you leap like rams? You hills, like young lambs?",
      "T": "O mountains — why did you skip like rams?\nO hills —\nlike young lambs?"
    },
    "7": {
      "L": "Tremble, O earth, at the presence of the Lord, at the presence of the God of Jacob,",
      "M": "Tremble before the Lord, O earth — tremble before the God of Jacob,",
      "T": "Tremble, O earth,\nat the presence of the Lord —\nat the presence of the God of Jacob,"
    },
    "8": {
      "L": "who turns the rock into a pool of water, the flint into a spring of water.",
      "M": "who turns solid rock into a pool of water and hard flint into a flowing spring.",
      "T": "who turns the rock into a pool of water —\nthe flint\ninto a flowing spring."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 109–114 written.')

if __name__ == '__main__':
    main()
