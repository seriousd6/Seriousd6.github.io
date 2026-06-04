"""
MKT Psalms chapters 97–102 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-97-102.py

=== Overview of this unit ===

Ps 97 (12 v) — An enthronement psalm: "The LORD reigns!" The psalm is a theophany —
    the appearance of the divine King in fire, lightning, and earthquake. Mountains
    melt; heavens declare his righteousness; idol-worshippers are put to shame; those
    who love the LORD and hate evil receive light and joy. Closely related to Ps 96
    (which it may follow as a liturgical pair).

    The theophanic imagery (fire, lightning, earthquake, melting mountains) echoes
    the Sinai tradition (Exod 19; Hab 3; Ps 18) — the LORD's approach shakes the
    created order.

    v11 "Light is sown for the righteous" — one of the most unusual images in the
    Psalter. Light, normally immediate and radiating, is here seeded into the ground
    to grow. The image suggests that righteousness leads to an increasing yield of
    light — justice ripens over time.

Ps 98 (9 v) — "O sing to the LORD a new song!" A companion to Ps 96 (nearly identical
    opening). The "new song" is called for because a new act of salvation has been
    accomplished. Ps 98 grounds the praise in God's historic deliverance of Israel
    (vv1-3) and then calls the entire created order — sea, rivers, hills — to join
    the cosmic praise (vv7-9). The concluding note is eschatological: "he comes to
    judge the earth."

    v1 — God's "right hand and holy arm" = the divine warrior imagery. The arm that
    worked the Exodus (Exod 6:6; 15:16) is the same arm that works this new salvation.

    v3 — "He has remembered his steadfast love (chesed) and faithfulness (emunah)
    to the house of Israel." This deliberately echoes the Abrahamic promise and the
    Sinai covenant formula. The nations witness what was promised to Israel.

Ps 99 (9 v) — The third enthronement psalm in sequence (Pss 97, 98, 99). Its
    distinctive refrain "Holy is he!" (vv3, 5) and "For the LORD our God is holy"
    (v9) gives it a trisagion structure parallel to Isaiah 6. The psalm grounds God's
    kingship in both cosmic power (vv1-3) and historical covenant (vv4-8) — he reigns
    not only as Creator but as the God of Moses, Aaron, and Samuel.

    v4 — "The king in his strength loves justice" — ambiguous: either "the might of a
    king who loves justice" (characterizing YHWH) or "a king's real power consists in
    love of justice." Both senses are present; T surfaces the latter.

    v8 — "A forgiving God to them, but an avenger of their wrongdoings." The tension
    between forgiveness and justice is explicit — he both pardoned and punished. The
    Hebrew nasa' (to lift/forgive) and naqam (to avenge) stand side by side.

Ps 100 (5 v) — One of the most beloved short psalms. A Psalm of Todah (thanksgiving
    offering). Five verses that form a complete act of worship: summons (v1), invitation
    to serve (v2), theological anchor (v3), liturgical instruction (v4), and doxological
    foundation (v5). The center is v3: "Know that the LORD is God — it is he who made
    us, and we are his." The basis for worship is not feeling but knowing.

    v5 — "His steadfast love endures forever" — the refrain of Ps 136 (used 26 times)
    and throughout Chronicles at key worship moments (1 Chr 16:34; 2 Chr 5:13; 7:3).

Ps 101 (8 v) — A Psalm of David. A royal psalm of ethical commitment — often called
    the "mirror of princes." The psalmist (king) vows to sing of chesed and mishpat
    (steadfast love and justice), walk with integrity, refuse to tolerate wickedness
    in his court, and cut off evildoers. The psalm is both personal and political.

    v2b "O when will you come to me?" — an unexpected prayer in the middle of the
    ethical commitment. The king cannot rule with integrity apart from divine presence.
    The question reveals the psalm's Godward orientation: the ethical life depends on
    God's drawing near.

    v8 — "Morning by morning" — morning was when courts convened in the ancient Near
    East (2 Sam 15:2; Jer 21:12). The king's morning duty was to render justice.

Ps 102 (28 v) — "A Prayer of an afflicted man when he is overwhelmed and pours out
    his complaint before the LORD." One of the seven Penitential Psalms. A profound
    lament with a remarkable structural pivot:

    vv1-11:   The afflicted man's lament — desperate physical and social suffering.
    vv12-22:  Confident proclamation — the LORD will arise and build up Zion. The
        psalmist's certainty shifts from personal distress to cosmic/communal hope.
    vv23-28:  Second lament and resolution — broken life (vv23-24) gives way to
        meditation on God's eternal nature (vv25-28).

    vv25-27 are quoted verbatim in Hebrews 1:10-12 as spoken by God to the Son.
    The author of Hebrews reads "you laid the foundation of the earth" as addressed
    to Christ — the Creator who remains "the same" while creation passes away.

    v6 — "Desert owl" and "owl of the waste places": H6893 (qaat = pelican or desert
    owl) and H3563 (kos = owl). Precise species uncertain; the point is desolate,
    solitary birds of ruin.

    v27 — "But you are the same" (attah-hu', lit. "you are he"): An absolute predication
    of divine identity and changelessness. The phrase attah-hu' appears in Deutero-Isaiah
    (Isa 43:10, 13) as God's own self-identification. In Ps 102 it anchors the contrast
    between perishing creation and the eternal God.

=== Contested-term decisions ===

H2617 (חֶסֶד, chesed): "steadfast love" in L/M throughout. In T: "steadfast love" —
    consistent with all prior Psalms scripts. Appears at Ps 98:3; 100:5; 101:1; 102:17.

H3068 (יהוה, YHWH): "LORD" in L/M. In T: "LORD" or "the LORD" per cadence.
    Consistent with all prior Psalms scripts.

H430 (אֱלֹהִים, Elohim): "God" in all tiers.

H410 (אֵל, El): "God" in all tiers (Ps 102:24).

H5945 (עֶלְיוֹן, Elyon): Not present in this unit by name; the concept of God's
    supremacy over all gods is present in Ps 97:9 ("most high over all the earth")
    and Ps 99:2 ("exalted above all the peoples").

H530 (אֱמוּנָה, emunah, faithfulness): "faithfulness" in all tiers (Ps 98:3; 100:5).

H571 (אֶמֶת, emet, truth/faithfulness): "faithfulness" at Ps 98:3 where it appears
    with chesed. "faithfulness" in all tiers.

H4427 (מָלַךְ, malak): "reigns" in all tiers. The enthronement formula "The LORD
    reigns" (YHWH malak) is a Hebrew perfect/stative — rendered as present proclamation.

H6918 (קָדוֹשׁ, qadosh): "holy" in all tiers. The refrain of Ps 99.

H8426 (תּוֹדָה, todah): The thanksgiving/thank-offering. "thanksgiving" in L/M.
    In T: "thanksgiving offering" at the superscription.

H4941 (מִשְׁפָּט, mishpat): "justice" in L/M/T — consistent with all prior Psalms
    scripts (paired with chesed in Ps 101:1).

H5315 (נֶפֶשׁ, nefesh): "souls" in L at Ps 97:10; "lives" in M/T.

H5769 (עוֹלָם, olam): "forever" / "everlasting" — Ps 100:5; 102:12, 24, 27.

H8537 (תֹּם, tom) / H8549 (תָּמִים, tamim): "integrity" / "blameless" at Ps 101:2.
    Rendered "integrity" and "blameless" in L/M. In T: "integrity" and "blameless."

=== Textual and interpretive notes ===

Ps 97:7 — "All gods bow down before him" — the gods of the nations are real enough
    to be commanded to worship YHWH; the psalm asserts their subordination, not their
    non-existence. This is the "divine council" motif (cf. Pss 82; 89:5-8).

Ps 98:1-3 — Chiastic structure: v1 (new song → marvellous things), v2 (salvation →
    righteousness → nations see), v3 (chesed + emunah → Israel → ends of earth). The
    nations witness Israel's covenant God at work.

Ps 99:4 — "The king in his strength loves justice" — the Hebrew 'oz-melek (strength
    of the king) is ambiguous. Could modify the king or describe what justice-love
    produces. Both readings preserved in M; T draws out the second.

Ps 100:3 — The MT has lo' (not = "not we ourselves") as ketib; the qere reads lo
    (= "and we are his"). Modern editions follow qere. I follow qere in all tiers.

Ps 101:2b — "O when will you come to me?" — an abrupt prayer breaking the ethical
    declaration. The king's integrity depends on divine visitation. T surfaces this.

Ps 102:25-27 — Heb 1:10-12 quotes these verses as God speaking to the Son. The T
    tier surfaces the NT trajectory without imposing it at the OT reading stage.

=== Aspect and tense notes ===

Pss 97-99 use hymnic presents (God "reigns," "sits," "loves") and perfects of completed
    divine action ("he has done," "he has made known," "he has remembered"). The
    enthronement formula "The LORD reigns" is a Hebrew perfect/stative best rendered
    as a present proclamation.

Ps 101 uses cohortatives of resolve ("I will sing," "I will walk," "I will not set,"
    "I will cut off") — vows of future intention made in the present moment of commitment.

Ps 102 alternates between perfects of past suffering ("my days passed"), ongoing
    presents ("I am like an owl"), and future trust ("you will arise"). The lament
    moves from past/present anguish to eschatological confidence.
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

  # ==========================================================================
  # Psalm 97 — The LORD Reigns: Theophany of the Divine King
  # ==========================================================================
  "97": {
    "1": {
      "L": "The LORD reigns; let the earth rejoice! Let the many coastlands be glad!",
      "M": "The LORD reigns; let the earth rejoice! Let all the distant coastlands be glad!",
      "T": "The LORD reigns!\nLet the earth break into joy.\nLet every distant coastland be glad."
    },
    "2": {
      "L": "Clouds and thick darkness are round about him; righteousness and justice are the foundation of his throne.",
      "M": "Clouds and thick darkness surround him; righteousness and justice are the foundation of his throne.",
      "T": "Clouds and deep darkness circle him.\nBut his throne rests on righteousness and justice—\nthe moral order is what holds."
    },
    "3": {
      "L": "Fire goes before him and burns up his enemies on every side.",
      "M": "Fire goes out before him and consumes his enemies on every side.",
      "T": "Fire goes before him.\nIt burns his enemies\non every side."
    },
    "4": {
      "L": "His lightnings lit up the world; the earth saw and trembled.",
      "M": "His lightnings illuminate the world; the earth sees and shakes with fear.",
      "T": "His lightning blazes across the world.\nThe earth sees it\nand shudders."
    },
    "5": {
      "L": "The mountains melt like wax before the LORD, before the Lord of all the earth.",
      "M": "The mountains melt like wax before the LORD, before the Lord of all the earth.",
      "T": "The mountains melt like wax\nbefore the LORD—\nbefore the Lord of all the earth."
    },
    "6": {
      "L": "The heavens declare his righteousness, and all peoples see his glory.",
      "M": "The heavens proclaim his righteousness, and all the peoples behold his glory.",
      "T": "The heavens are announcing his righteousness.\nEvery people on earth\nis seeing his glory."
    },
    "7": {
      "L": "All who worship carved images are put to shame — those who boast in idols. All gods bow down before him.",
      "M": "All who worship carved images are put to shame — those who boast in worthless idols. All gods bow down before him.",
      "T": "Shame on everyone who worships carved images,\nwho boasts in things of nothing.\nEvery god bows down before him."
    },
    "8": {
      "L": "Zion heard and was glad, and the daughters of Judah rejoiced because of your judgments, O LORD.",
      "M": "Zion heard and was glad, and the towns of Judah rejoiced because of your judgments, O LORD.",
      "T": "Zion heard it and was glad.\nThe towns of Judah broke into rejoicing\nbecause of your judgments, LORD."
    },
    "9": {
      "L": "For you, O LORD, are most high over all the earth; you are exalted far above all gods.",
      "M": "For you, LORD, are most high over all the earth; you are raised far above all gods.",
      "T": "You, LORD, are lifted highest over all the earth.\nYou are exalted far above every god."
    },
    "10": {
      "L": "O you who love the LORD, hate evil! He preserves the souls of his faithful; he delivers them from the hand of the wicked.",
      "M": "You who love the LORD, hate evil! He guards the lives of his faithful and rescues them from the power of the wicked.",
      "T": "Love the LORD — and hate evil.\nHe guards the lives of those who are faithful to him.\nHe pulls them free from the grip of the wicked."
    },
    "11": {
      "L": "Light is sown for the righteous, and joy for the upright in heart.",
      "M": "Light is sown for the righteous and gladness for the upright in heart.",
      "T": "Light has been seeded in the ground for the righteous—\nit is growing.\nGladness waits for those with honest hearts."
    },
    "12": {
      "L": "Rejoice in the LORD, O you righteous, and give thanks to his holy name!",
      "M": "Rejoice in the LORD, you who are righteous, and give thanks to his holy name!",
      "T": "Rejoice in the LORD, you righteous.\nGive thanks to his holy name."
    }
  },

  # ==========================================================================
  # Psalm 98 — Sing a New Song: The LORD's Victory Proclaimed to All Nations
  # ==========================================================================
  "98": {
    "1": {
      "L": "A Psalm. O sing to the LORD a new song, for he has done marvelous things! His right hand and his holy arm have worked salvation for him.",
      "M": "A Psalm. Sing to the LORD a new song, for he has done wondrous things! His own right hand and his holy arm have gained him the victory.",
      "T": "A Psalm.\nSing to the LORD a new song—\nhe has done remarkable things.\nWith his own right hand,\nwith his holy arm,\nhe won the victory himself."
    },
    "2": {
      "L": "The LORD has made known his salvation; he has revealed his righteousness in the sight of the nations.",
      "M": "The LORD has made his salvation known and has displayed his righteousness before the nations.",
      "T": "The LORD has made his salvation known.\nHe let the nations see his righteousness\nwith their own eyes."
    },
    "3": {
      "L": "He has remembered his steadfast love and his faithfulness to the house of Israel. All the ends of the earth have seen the salvation of our God.",
      "M": "He has remembered his steadfast love and faithfulness to the house of Israel. All the ends of the earth have witnessed the salvation of our God.",
      "T": "He remembered his steadfast love—\nhis faithfulness to the house of Israel.\nAnd now the farthest ends of the earth\nhave seen the salvation of our God."
    },
    "4": {
      "L": "Make a joyful noise to the LORD, all the earth! Break forth into joyful song and sing praises!",
      "M": "Shout for joy to the LORD, all the earth! Burst into song and sing praises!",
      "T": "Shout for joy to the LORD — all the earth!\nBurst out in song and sing his praises!"
    },
    "5": {
      "L": "Sing praises to the LORD with the harp, with the harp and the voice of melody!",
      "M": "Sing praises to the LORD with the harp, with the harp and the sound of singing!",
      "T": "Praise him with the harp—\nwith harp and voice together,\nmelody joined to melody."
    },
    "6": {
      "L": "With trumpets and the sound of the horn make a joyful noise before the King, the LORD!",
      "M": "With trumpets and the blast of the ram's horn shout for joy before the King, the LORD!",
      "T": "With trumpets and the ram's horn blast—\nshout for joy before the King, the LORD!"
    },
    "7": {
      "L": "Let the sea roar, and all that fills it; the world and those who dwell in it!",
      "M": "Let the sea thunder with all that is in it, the world and all who live in it!",
      "T": "Let the sea roar with everything in it.\nLet the world join in—\nand all who live here."
    },
    "8": {
      "L": "Let the rivers clap their hands; let the hills sing together for joy!",
      "M": "Let the rivers clap their hands; let the mountains sing together for joy!",
      "T": "Let the rivers clap their hands.\nLet the mountains sing together—\nfor joy!"
    },
    "9": {
      "L": "Before the LORD, for he comes to judge the earth! He will judge the world with righteousness and the peoples with equity.",
      "M": "Before the LORD, for he is coming to judge the earth! He will rule the world with righteousness and the peoples with fairness.",
      "T": "— before the LORD!\nFor he is coming to judge the earth.\nHe will rule the world with righteousness\nand the peoples with perfect fairness."
    }
  },

  # ==========================================================================
  # Psalm 99 — Holy Is He! The Enthroned LORD of Moses, Aaron, and Samuel
  # ==========================================================================
  "99": {
    "1": {
      "L": "The LORD reigns; let the peoples tremble! He sits enthroned between the cherubim; let the earth quake!",
      "M": "The LORD reigns; let the peoples tremble! He is enthroned above the cherubim; let the earth shake!",
      "T": "The LORD reigns!\nLet the peoples tremble.\nHe sits enthroned above the cherubim—\nlet the earth quake."
    },
    "2": {
      "L": "The LORD is great in Zion; he is exalted above all the peoples.",
      "M": "The LORD is great in Zion; he is raised high above all the peoples.",
      "T": "The LORD is great in Zion.\nHe is exalted above every people."
    },
    "3": {
      "L": "Let them praise your great and awesome name — holy is he!",
      "M": "Let them praise your great and fearsome name — holy is he!",
      "T": "Let them praise your name—\ngreat and awe-inspiring.\nHoly is he!"
    },
    "4": {
      "L": "The king in his strength loves justice. You have established equity; you have executed justice and righteousness in Jacob.",
      "M": "The mighty king loves justice. You have established fairness; you have carried out justice and righteousness in Jacob.",
      "T": "A king's true strength is love of justice.\nYou established equity.\nYou executed justice and righteousness in Jacob."
    },
    "5": {
      "L": "Exalt the LORD our God; worship at his footstool — holy is he!",
      "M": "Exalt the LORD our God and bow down at his footstool — holy is he!",
      "T": "Exalt the LORD our God!\nBow down before his footstool—\nholy is he!"
    },
    "6": {
      "L": "Moses and Aaron were among his priests; Samuel also was among those who called on his name. They called to the LORD and he answered them.",
      "M": "Moses and Aaron were among his priests; Samuel was among those who called on his name. They called out to the LORD, and he answered them.",
      "T": "Moses and Aaron stood among his priests.\nSamuel was among those who called on his name.\nThey called to the LORD—\nand he answered."
    },
    "7": {
      "L": "In the pillar of cloud he spoke to them; they kept his testimonies and the decree he gave them.",
      "M": "He spoke to them in the pillar of cloud; they kept his testimonies and the law he gave them.",
      "T": "He spoke to them from the pillar of cloud.\nThey kept what he gave them—\nhis testimonies, his decrees."
    },
    "8": {
      "L": "O LORD our God, you answered them; you were a forgiving God to them, but an avenger of their wrongdoings.",
      "M": "LORD our God, you answered them; you were a God who forgave them, yet you held them accountable for their offenses.",
      "T": "LORD our God — you answered them.\nYou were a God who forgave.\nYet you called their wrongs to account."
    },
    "9": {
      "L": "Exalt the LORD our God and worship at his holy mountain, for the LORD our God is holy!",
      "M": "Exalt the LORD our God and worship at his holy mountain, for the LORD our God is holy!",
      "T": "Exalt the LORD our God!\nWorship at his holy mountain—\nfor the LORD our God is holy!"
    }
  },

  # ==========================================================================
  # Psalm 100 — A Psalm of Thanksgiving: Know That the LORD Is God
  # ==========================================================================
  "100": {
    "1": {
      "L": "A Psalm for giving thanks. Make a joyful noise to the LORD, all the earth!",
      "M": "A Psalm of thanksgiving. Shout for joy to the LORD, all the earth!",
      "T": "A Psalm for the thanksgiving offering.\nShout for joy to the LORD — all the earth!"
    },
    "2": {
      "L": "Serve the LORD with gladness! Come before his presence with singing!",
      "M": "Serve the LORD with joy! Come into his presence with songs of praise!",
      "T": "Serve the LORD with gladness.\nCome before him with singing."
    },
    "3": {
      "L": "Know that the LORD is God! It is he who made us, and we are his; we are his people and the sheep of his pasture.",
      "M": "Know that the LORD is God! He made us, and we belong to him; we are his people, the flock he tends.",
      "T": "Know this: the LORD is God.\nHe made us — we belong to him.\nWe are his people, the flock of his pasture."
    },
    "4": {
      "L": "Enter his gates with thanksgiving and his courts with praise! Give thanks to him; bless his name!",
      "M": "Enter his gates with thanksgiving and his courts with praise! Thank him and bless his name!",
      "T": "Enter his gates with thanksgiving.\nCome into his courts with praise.\nThank him. Bless his name."
    },
    "5": {
      "L": "For the LORD is good; his steadfast love endures forever, and his faithfulness to all generations.",
      "M": "For the LORD is good; his steadfast love endures forever, and his faithfulness reaches to every generation.",
      "T": "The LORD is good.\nHis steadfast love endures forever.\nHis faithfulness reaches to every generation."
    }
  },

  # ==========================================================================
  # Psalm 101 — The King's Vow: Steadfast Love, Justice, and Integrity
  # ==========================================================================
  "101": {
    "1": {
      "L": "A Psalm of David. I will sing of steadfast love and justice; to you, O LORD, I will make music.",
      "M": "A Psalm of David. I will sing of steadfast love and justice; to you, LORD, I will make music.",
      "T": "A Psalm of David.\nOf steadfast love and justice I will sing—\nto you, LORD, I will make music."
    },
    "2": {
      "L": "I will behave wisely in a blameless way. O when will you come to me? I will walk with integrity of heart within my house.",
      "M": "I will conduct myself with wisdom and integrity. O when will you come to me? I will walk with a blameless heart within my own house.",
      "T": "I will walk the path of integrity.\nO when will you come to me?\nInside my own house I will walk\nwith a whole and blameless heart."
    },
    "3": {
      "L": "I will not set before my eyes any worthless thing. I hate the doing of those who turn aside; it shall not cling to me.",
      "M": "I will not place anything vile before my eyes. I despise the conduct of those who fall away; it will have no hold on me.",
      "T": "I will set nothing vile before my eyes.\nThe ways of those who turn away — I hate them.\nThey will not take hold of me."
    },
    "4": {
      "L": "A perverse heart shall be far from me; I will not know evil.",
      "M": "I will have nothing to do with a crooked heart; I will have no part in evil.",
      "T": "A twisted heart — let it stay far from me.\nEvil — I will not know it."
    },
    "5": {
      "L": "Whoever slanders his neighbor in secret I will destroy. A haughty look and an arrogant heart I will not endure.",
      "M": "Whoever slanders his neighbor in private, him I will silence. The proud-eyed and the arrogant-hearted I will not tolerate.",
      "T": "Whoever slanders a neighbor in secret—\nI will put an end to them.\nThe proud look, the arrogant heart—\nnot in my house."
    },
    "6": {
      "L": "My eyes shall be on the faithful of the land, that they may dwell with me; whoever walks in the blameless way shall minister to me.",
      "M": "My eyes will be on the faithful people of the land, that they may live with me; only those who walk blamelessly will serve in my presence.",
      "T": "My eyes will be on the faithful of the land—\nthose are the ones I want near me.\nOnly those who walk with integrity\nwill stand in my service."
    },
    "7": {
      "L": "No one who practices deceit shall dwell in my house; no one who utters lies shall stand before my eyes.",
      "M": "No one who practices deceit will live in my house; no one who tells lies will remain in my presence.",
      "T": "No one who deals in deceit\nwill have a place in my house.\nNo one who speaks lies\nwill stand before my eyes."
    },
    "8": {
      "L": "Morning by morning I will destroy all the wicked of the land, cutting off all evildoers from the city of the LORD.",
      "M": "Each morning I will silence all the wicked in the land, cutting off every evildoer from the city of the LORD.",
      "T": "Each morning I will clear out the wicked from the land—\ncutting off every evildoer\nfrom the city of the LORD."
    }
  },

  # ==========================================================================
  # Psalm 102 — A Prayer in Affliction: Human Frailty and God's Eternal Throne
  # ==========================================================================
  "102": {
    "1": {
      "L": "A Prayer of an afflicted man, when he is overwhelmed and pours out his complaint before the LORD. Hear my prayer, O LORD; let my cry come to you!",
      "M": "A Prayer of an afflicted man when he is faint and pours out his anguish before the LORD. Hear my prayer, O LORD; let my cry reach you!",
      "T": "A Prayer of one who is afflicted—\noverwhelmed, pouring out his heart before the LORD.\nHear my prayer, LORD.\nLet my cry come before you."
    },
    "2": {
      "L": "Do not hide your face from me in the day of my distress! Incline your ear to me; answer me speedily in the day when I call!",
      "M": "Do not hide your face from me when I am in trouble! Lean down and listen; answer me quickly when I call!",
      "T": "Do not hide your face from me\nin the day of my distress.\nBend your ear toward me.\nAnswer me quickly—\nthe day I call."
    },
    "3": {
      "L": "For my days pass away like smoke, and my bones burn like a furnace.",
      "M": "For my days are vanishing like smoke, and my bones burn like a blazing hearth.",
      "T": "My days disappear like smoke.\nMy bones burn\nlike a heap of coals."
    },
    "4": {
      "L": "My heart is struck down like grass and has withered; I forget to eat my bread.",
      "M": "My heart is crushed like grass and has dried up; I have even forgotten to eat.",
      "T": "My heart is beaten down like grass and withered.\nI have forgotten to eat."
    },
    "5": {
      "L": "Because of my loud groaning my bones cling to my flesh.",
      "M": "From my constant groaning I am reduced to skin and bones.",
      "T": "My groaning never stops—\nmy bones are grinding against my skin."
    },
    "6": {
      "L": "I am like a desert owl, like an owl of the waste places.",
      "M": "I am like a pelican of the desert, like an owl haunting the ruins.",
      "T": "I have become a bird of the desolate places—\na solitary owl among the rubble."
    },
    "7": {
      "L": "I lie awake; I am like a lonely sparrow on the housetop.",
      "M": "I cannot sleep; I am like a solitary bird stranded on a rooftop.",
      "T": "I lie awake.\nA lone sparrow on a rooftop—\nthat is what I am."
    },
    "8": {
      "L": "All the day my enemies taunt me; those who mock me use my name as a curse.",
      "M": "My enemies insult me all day long; those who deride me invoke my name as a curse.",
      "T": "My enemies taunt me all day long.\nThose who mock me\nuse my name as a curse."
    },
    "9": {
      "L": "For I eat ashes like bread and mingle tears with my drink,",
      "M": "For I eat ashes instead of bread and mix my tears into what I drink,",
      "T": "I eat ashes like bread.\nI mix my tears into my drink."
    },
    "10": {
      "L": "because of your indignation and your anger; for you have taken me up and thrown me down.",
      "M": "because of your fury and wrath; for you have lifted me up only to hurl me down.",
      "T": "Because of your fury.\nBecause of your wrath.\nYou lifted me up—\nand threw me down."
    },
    "11": {
      "L": "My days are like a lengthening shadow; I wither away like grass.",
      "M": "My days are like a fading shadow at evening; I am withering like grass.",
      "T": "My days are an evening shadow stretched long before it vanishes.\nI am withering like grass."
    },
    "12": {
      "L": "But you, O LORD, are enthroned forever; your name endures to all generations.",
      "M": "But you, LORD, are enthroned forever; your name endures throughout every generation.",
      "T": "But you, LORD—\nyou are enthroned forever.\nYour name endures\nthrough every generation."
    },
    "13": {
      "L": "You will arise and have pity on Zion; it is the time to show her favor — the appointed time has come.",
      "M": "You will rise up and have mercy on Zion; the time to show her favor has come — the appointed hour is here.",
      "T": "You will arise and have mercy on Zion.\nThe time to favor her has come.\nThe appointed moment is here."
    },
    "14": {
      "L": "For your servants cherish her stones and show pity for her dust.",
      "M": "For your servants hold her very stones dear and take pity even on her dust.",
      "T": "Your servants love even her rubble.\nThey grieve over the dust of her ruins."
    },
    "15": {
      "L": "The nations will fear the name of the LORD, and all the kings of the earth your glory.",
      "M": "The nations will stand in awe of the name of the LORD, and all the kings of the earth will reverence your glory.",
      "T": "When that happens the nations will fear the name of the LORD.\nEvery king on earth will stand in awe of his glory."
    },
    "16": {
      "L": "For the LORD will build up Zion; he will appear in his glory.",
      "M": "For the LORD will rebuild Zion and reveal himself in his glory.",
      "T": "For the LORD is building Zion again.\nHe will appear — in his full glory."
    },
    "17": {
      "L": "He regards the prayer of the destitute and does not despise their prayer.",
      "M": "He listens to the prayer of the helpless and does not ignore their cry.",
      "T": "He turns toward the prayer of the stripped-bare.\nHe does not brush it aside."
    },
    "18": {
      "L": "Let this be recorded for a generation to come, so that a people yet to be created may praise the LORD.",
      "M": "Let this be written down for a future generation, so that a people not yet born will praise the LORD.",
      "T": "Write this down for the generation to come—\nso that a people not yet born\nwill praise the LORD."
    },
    "19": {
      "L": "That he looked down from his holy height; from heaven the LORD looked at the earth,",
      "M": "That the LORD looked down from his holy height; from heaven he gazed upon the earth,",
      "T": "He looked down from the height of his holiness.\nFrom heaven the LORD bent his gaze to the earth—"
    },
    "20": {
      "L": "to hear the groaning of the prisoner, to set free those who were doomed to die,",
      "M": "to hear the groaning of the prisoner and release those condemned to death,",
      "T": "— to hear the prisoner's groan,\nto set free those marked for death,"
    },
    "21": {
      "L": "that they may declare in Zion the name of the LORD and his praise in Jerusalem,",
      "M": "so that the name of the LORD would be proclaimed in Zion and his praise sung in Jerusalem,",
      "T": "so that in Zion the name of the LORD would be declared—\nhis praise ringing out in Jerusalem—"
    },
    "22": {
      "L": "when peoples are gathered together and kingdoms, to serve the LORD.",
      "M": "when peoples and kingdoms assemble together to worship the LORD.",
      "T": "— when peoples gather,\nkingdoms together,\nto serve the LORD."
    },
    "23": {
      "L": "He has broken my strength in the middle of my way; he has cut short my days.",
      "M": "He has sapped my strength in midcourse; he has shortened my days.",
      "T": "He broke my strength at the midpoint of my journey.\nHe cut my days short."
    },
    "24": {
      "L": "I said, 'O my God, take me not away in the midst of my days — you whose years endure through all generations!'",
      "M": "I said, 'O my God, do not take me away in the middle of my life — you whose years go on through all generations!'",
      "T": "I said,\n'O my God — do not take me away at half my days.\nYour years span every generation;\nmine are barely begun.'"
    },
    "25": {
      "L": "Of old you laid the foundation of the earth, and the heavens are the work of your hands.",
      "M": "Long ago you laid the earth's foundation, and the heavens are the handiwork you shaped.",
      "T": "Long ago you laid the earth's foundation.\nThe heavens are the work of your hands."
    },
    "26": {
      "L": "They will perish, but you will remain; they will all wear out like a garment. You will change them like a robe, and they will pass away,",
      "M": "They will perish, but you will endure; they will all wear out like old clothes. You will roll them up like a garment and they will be changed,",
      "T": "They will perish — but you will remain.\nThey will wear out like an old cloak.\nYou will roll them up and change them like a robe,\nand they will pass away—"
    },
    "27": {
      "L": "but you are the same, and your years will not come to an end.",
      "M": "but you are ever the same, and your years will never end.",
      "T": "— but you are the same.\nYou are unchanging.\nYour years have no end."
    },
    "28": {
      "L": "The children of your servants shall dwell secure; their offspring shall be established before you.",
      "M": "The children of your servants will live in safety; their descendants will be established in your presence.",
      "T": "The children of your servants will remain.\nTheir descendants will be planted firmly\nbefore you."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 97–102 written.')

if __name__ == '__main__':
    main()
