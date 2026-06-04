"""
MKT Psalms chapters 85–88 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-85-88.py

=== Overview ===

All four psalms fall in Book III of the Psalter (Pss 73–89), the Asaph/Korah collection.

Ps 85 — National Restoration Prayer (13 verses, Sons of Korah):
    A communal psalm of return, likely post-exilic. Three movements: (1) vv1–3 recall
    past acts of divine favor — captivity restored, sin forgiven, wrath withdrawn;
    (2) vv4–7 petition for renewal; (3) vv8–13 shift to prophetic oracle, announcing
    that peace, steadfast love, faithfulness, and righteousness converge in a great
    eschatological meeting (v10). The famous fourfold personification of vv10–11 —
    hesed and emet kissing, tsedek and shalom embracing — is one of the most compact
    theological portraits in the OT.

Ps 86 — Prayer of David (17 verses):
    The only Davidic psalm in Book III and the only psalm in the Psalter titled simply
    "A Prayer of David." It is a mosaic psalm — nearly every phrase is borrowed from
    elsewhere in the Psalter, assembled here into a personal lament. Uses H136 (Adonai)
    more than any other psalm; YHWH (H3068) appears only at vv1, 6, 11, 17. The psalm
    pivots at v15 on the ancient covenant formula (Exod 34:6): "compassionate, gracious,
    slow to anger, abounding in steadfast love and faithfulness."

Ps 87 — The Universal Zion Psalm (7 verses, Sons of Korah):
    The most theologically audacious of the Korah psalms: Israel's ancient enemies
    (Rahab/Egypt, Babylon, Philistia, Tyre, Ethiopia) are declared to have been "born"
    in Zion — enrolled in God's city as citizens. The repeated phrase "this one was born
    there" (vv4, 5, 6) is a divine registry announcement. This anticipates the NT's
    universal mission and is echoed by Paul's "citizenship in heaven" (Phil 3:20). V7's
    "all my springs are in you" is an ejaculatory finale of praise.

Ps 88 — The Darkest Psalm (18 verses, Heman the Ezrahite via Korah):
    The only psalm in the Psalter that never finds resolution. Every other lament ends
    with at least a note of trust or praise; Psalm 88 ends in darkness: "darkness is my
    closest friend" (v18). The psalmist is near death (v3), cut off from companions
    (v8, 18), and attributes his suffering directly to God (vv6–7, 14–16). Its very
    presence in the canon validates the experience of faith without visible comfort.

=== Superscriptions ===

Per the convention established in PSA-1 through PSA-13a, superscription text is merged
into v1, separated from the verse body by a blank line in T tier.

Ps 85: "A Psalm for the Sons of Korah. To the chief Musician."
Ps 86: "A Prayer of David." — the superscription is terse; merged flush into v1 text.
Ps 87: "A Psalm or Song for the Sons of Korah." — Ps 87 is unusual in that v1 gives
        the heading AND the first verse is a statement about God's foundation, with no
        clear caesura; the heading is merged at the front per convention.
Ps 88: Full heading — "A Song. A Psalm of the Sons of Korah. To the chief Musician,
        upon Mahalath Leannoth. A Maschil of Heman the Ezrahite."

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M; "the LORD" in T.
      Ps 85:7 and 12; Ps 86:1,6,11,17; Ps 87:2,6; Ps 88:1,9,13,14.

H430  (אֱלֹהִים, Elohim): "God" in all tiers.
      Ps 85:4; Ps 86:10,12,14; Ps 87:3; Ps 88:1.

H136  (אֲדֹנָי, Adonai): "Lord" (capital L, not small-caps) in all tiers.
      Dominant in Ps 86 (vv3,4,5,8,9,12,15). Per PSA-13a convention.

H410  (אֵל, El — singular "God"): "God" in all tiers. Appears at Ps 86:15
      in the phrase "thou art a God merciful and gracious." El here is a
      qualitative description ("a God who is..."), rendered simply "God."

H2617 (חֶסֶד, hesed): "steadfast love" in all tiers — MKT standard.
      Key verse: Ps 85:7,10; Ps 86:5,13,15; Ps 88:11.

H571  (אֱמֶת, emet): "truth" in L; "faithfulness" in M/T throughout.
      Emet covers both truth and covenant fidelity; "faithfulness" captures
      the relational-covenant register better in M/T.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M; varies in T (often "life" or "whole being"
      when the context is mortal danger).

H5542 (סֶלָה, selah): Retained as "Selah" appended to verse end.
      Ps 85:2; Ps 87:3,6; Ps 88:7,10.

H7585 (שְׁאוֹל, Sheol): "Sheol" in all tiers — not "grave" or "hell."
      Appears at Ps 86:13; Ps 88:3. The word is a proper name for the realm
      of the dead; preserving it avoids both over-Christianising ("hell") and
      flattening ("grave").

H11   (אֲבַדּוֹן, Abaddon): Retained as "Abaddon" in all tiers at Ps 88:11.
      A proper name for the realm of destruction, paralleling Sheol. Its
      appearance in Rev 9:11 as a proper name confirms the translation choice.

H2670 (חָפְשִׁי, chofshi, "free"): At Ps 88:5 this word carries bitter irony —
      the dead are "free" (released from obligation) but also abandoned and cut off.
      Rendered "cast loose" in L/M; T renders "released into the company of the dead"
      to preserve the ironic sense of freedom-as-abandonment.

H5945 (עֶלְיוֹן, Elyon): "the Most High" in all tiers at Ps 87:5.

H7294 (רַהַב, Rahab): Retained as "Rahab" in all tiers at Ps 87:4. Here it is a
      poetic name for Egypt (the chaos-sea-monster), not the person Rahab of Jericho.
      Compare Job 9:13; 26:12; Isa 51:9.

H4257/H6031 (מַחֲלַת לְעַנּוֹת, Mahalath Leannoth): Left untranslated as the tune
      designation in Ps 88:1. Leannoth may derive from H6031 (affliction/suffering) —
      fitting this psalm's tone, but the musical term itself is uncertain.

H4905 (מַשְׂכִּיל, maskil): "Maschil" in L (traditional transliteration), "Maskil"
      in M/T. Denotes an instructional or contemplative psalm.

=== OT echoes and NT connections ===

- Ps 85:10 ("steadfast love and faithfulness meet") → 2 Cor 1:20 (all God's promises
  are Yes in Christ); Rom 3:21-26 (righteousness and grace reconciled at the cross).
- Ps 85:11 ("righteousness looks down from heaven") → Isa 45:8 (righteousness dropping
  from the skies). A repeated prophetic image of divine justice descending.
- Ps 86:15 (the hesed-emet formula) = verbatim echo of Exod 34:6 (the great proclamation
  of the divine name to Moses). This is the theological centre of the Hebrew Bible's
  portrait of God's character. John 1:14 ("full of grace and truth") is a deliberate NT
  echo of this formula.
- Ps 87:4-6 (nations "born in Zion") → Gal 4:26 (Jerusalem above, mother of us all);
  Phil 3:20 (citizenship in heaven); Rev 21:24-27 (nations walking in the new Jerusalem's
  light). This psalm is the OT seed of universalism-within-covenant.
- Ps 87:7 ("all my springs are in you") → John 4:14; 7:38 (rivers of living water
  flowing from within the believer); John 15:5 (apart from me you can do nothing).
- Ps 88 has no explicit NT citation but its structure of unresolved lament is fulfilled
  christologically in the cross-cry of Ps 22:1 (Matt 27:46) and in Jesus's experience
  of God-forsakenness, which this psalm anticipates most directly.

=== Aspect and tense notes ===

Ps 85: vv1-3 use Hebrew perfects — completed past acts ("you forgave," "you withdrew").
Render with simple past. vv4-7 are petitions and rhetorical questions (imperfects
with modal force) — render as requests and questions in English. vv8-13 shift to
prophetic future/present — the psalmist describes what he will hear (v8) and what will
follow (vv9-13). The verbs in vv9-13 are imperfects, best rendered as confident futures.

Ps 86: Present-tense petition throughout. Hebrew imperfects with imperative force
("Hear," "Preserve," "Be gracious," "Teach," "Unite"). The confession of God's character
(v15) is a present-tense statement of permanent truth.

Ps 87: Three present/eternal declarations (vv2-3), then a divine oracle (vv4-6), then
a chorus response (v7). The divine speech in vv4-6 uses perfect verbs — "I mention,"
"it will be said," "the LORD writes" — a prophetic perfect announcing completed future action.

Ps 88: The lament uses a mix of perfects (completed past: "you have put me in the pit,"
v6) and imperfects (ongoing: "I cry to you daily," v9,13). The psalm's unresolved tension
is grammatical as well as emotional — even the final verb (v18) is a perfect: "you have
put far from me." There is no vow of praise, no turn to hope.
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
  "85": {
    "1": {
      "L": "A Psalm for the sons of Korah. To the chief Musician. LORD, thou hast been favourable unto thy land; thou hast brought back the captivity of Jacob.",
      "M": "A Psalm of the Sons of Korah. For the choir director. O LORD, you showed favor to your land; you restored the fortunes of Jacob.",
      "T": "A Psalm of the Sons of Korah. For the worship leader.\n\nO LORD, you showed favor to your land —\nyou brought your people back,\nyou turned the fortunes of Jacob."
    },
    "2": {
      "L": "Thou hast forgiven the iniquity of thy people; thou hast covered all their sin. Selah.",
      "M": "You forgave the iniquity of your people; you covered over all their sin. Selah.",
      "T": "You forgave the guilt of your people;\nyou buried all their sin out of sight. Selah."
    },
    "3": {
      "L": "Thou hast taken away all thy wrath; thou hast turned thyself from the fierceness of thine anger.",
      "M": "You withdrew all your wrath; you turned away from your fierce anger.",
      "T": "You took back every last measure of your wrath;\nyou turned away from the blazing heat of your anger."
    },
    "4": {
      "L": "Turn us again, O God of our salvation, and cause thine indignation toward us to cease.",
      "M": "Restore us again, O God of our salvation, and set aside your displeasure against us.",
      "T": "Do it again, O God who saves us —\nturn us around and let your anger against us end."
    },
    "5": {
      "L": "Wilt thou be angry with us for ever? Wilt thou draw out thine anger to all generations?",
      "M": "Will you be angry with us forever? Will you extend your anger through every generation?",
      "T": "Will you stay angry with us forever?\nWill this fury reach down through every generation yet to come?"
    },
    "6": {
      "L": "Wilt thou not revive us again, that thy people may rejoice in thee?",
      "M": "Will you not revive us again, so that your people may rejoice in you?",
      "T": "Will you not breathe new life into us —\nso your people can burst into joy before you?"
    },
    "7": {
      "L": "Shew us thy steadfast love, O LORD, and grant us thy salvation.",
      "M": "Show us your steadfast love, O LORD, and grant us your salvation.",
      "T": "Let us see your steadfast love, O LORD —\ngrant us your saving help."
    },
    "8": {
      "L": "I will hear what God the LORD will speak; for he will speak peace unto his people and to his saints; but let them not turn again to folly.",
      "M": "I will listen to what God the LORD says; for he will speak peace to his people and to his faithful ones — only let them not return to folly.",
      "T": "I will listen for what God the LORD is saying —\nfor he speaks peace to his people and to his faithful ones.\nOnly this: let them not drift back into foolishness."
    },
    "9": {
      "L": "Surely his salvation is nigh unto them that fear him, that glory may dwell in our land.",
      "M": "Surely his salvation is near to those who fear him, so that glory may dwell in our land.",
      "T": "Surely his rescue is near — close enough to touch —\nfor all who revere him,\nso that his glory will take up residence in our land."
    },
    "10": {
      "L": "Steadfast love and truth are met together; righteousness and peace have kissed each other.",
      "M": "Steadfast love and faithfulness meet; righteousness and peace kiss.",
      "T": "Steadfast love and faithfulness find each other;\nrighteousness and peace lean in and kiss."
    },
    "11": {
      "L": "Truth springeth out of the earth; and righteousness hath looked down from heaven.",
      "M": "Faithfulness springs up from the earth, and righteousness looks down from heaven.",
      "T": "Faithfulness rises like a plant out of the ground;\nrighteousness bends down and gazes out from heaven."
    },
    "12": {
      "L": "Yea, the LORD shall give that which is good, and our land shall yield her increase.",
      "M": "Yes, the LORD will give what is good, and our land will yield its harvest.",
      "T": "Yes — the LORD will give what is truly good,\nand our land will pour out its abundance."
    },
    "13": {
      "L": "Righteousness shall go before him, and shall set his footsteps in the way.",
      "M": "Righteousness will march before him and prepare a path for his steps.",
      "T": "Righteousness goes ahead of him like a herald,\nmarking out the way where his feet will walk."
    }
  },
  "86": {
    "1": {
      "L": "A Prayer of David. Bow down thine ear, O LORD, and answer me; for I am poor and needy.",
      "M": "A Prayer of David. Turn your ear toward me, O LORD, and answer me, for I am poor and needy.",
      "T": "A Prayer of David.\n\nBend your ear toward me, O LORD — answer me;\nI have nothing, and I am desperate."
    },
    "2": {
      "L": "Preserve my soul, for I am faithful; save thou thy servant that trusteth in thee, O my God.",
      "M": "Preserve my soul, for I am devoted to you; save your servant who trusts in you — O my God.",
      "T": "Guard my life — I am yours, set apart for you.\nSave your servant who takes refuge in you,\nO my God."
    },
    "3": {
      "L": "Be merciful unto me, O Lord, for I cry unto thee all the day long.",
      "M": "Be gracious to me, O Lord, for I cry out to you all day long.",
      "T": "Show me your favor, O Lord —\nI have been calling to you all day without stopping."
    },
    "4": {
      "L": "Rejoice the soul of thy servant; for unto thee, O Lord, do I lift up my soul.",
      "M": "Gladden the soul of your servant, for to you, O Lord, I lift up my soul.",
      "T": "Fill your servant's heart with gladness —\nit is to you, O Lord, that I raise my whole being."
    },
    "5": {
      "L": "For thou, Lord, art good, and ready to forgive, and plenteous in steadfast love unto all them that call upon thee.",
      "M": "For you, O Lord, are good and forgiving, abounding in steadfast love for all who call on you.",
      "T": "You, O Lord, are genuinely good —\nquick to forgive,\noverflowing with covenant love for everyone who calls to you."
    },
    "6": {
      "L": "Give ear, O LORD, unto my prayer; and attend to the voice of my supplications.",
      "M": "Give ear to my prayer, O LORD; listen to the voice of my plea for mercy.",
      "T": "Listen to this prayer, O LORD —\npay close attention to my plea for mercy."
    },
    "7": {
      "L": "In the day of my trouble I will call upon thee; for thou wilt answer me.",
      "M": "On the day of my trouble I call to you, for you answer me.",
      "T": "On the day trouble overwhelms me, I call to you —\nbecause you answer."
    },
    "8": {
      "L": "Among the gods there is none like unto thee, O Lord; neither are there any works like unto thy works.",
      "M": "There is no one like you among the gods, O Lord, and no works compare to yours.",
      "T": "None of the so-called gods compares to you, O Lord —\nnot one of them can do what you do."
    },
    "9": {
      "L": "All nations whom thou hast made shall come and worship before thee, O Lord, and shall glorify thy name.",
      "M": "All the nations you have made will come and bow before you, O Lord, and they will glorify your name.",
      "T": "Every nation you have made will come\nand kneel before you, O Lord;\nthey will all bring glory to your name."
    },
    "10": {
      "L": "For thou art great, and doest wondrous things; thou art God alone.",
      "M": "For you are great and you do wonders; you alone are God.",
      "T": "You are great and you do astonishing things —\nyou and no other are God."
    },
    "11": {
      "L": "Teach me thy way, O LORD; I will walk in thy truth; unite my heart to fear thy name.",
      "M": "Teach me your way, O LORD, that I may walk in your truth; give me an undivided heart to reverence your name.",
      "T": "Show me the path you walk, O LORD —\nI want to move through life in step with your truth.\nBring all the scattered pieces of my heart into one\nso that I can truly honor your name."
    },
    "12": {
      "L": "I will praise thee, O Lord my God, with all my heart; and I will glorify thy name for evermore.",
      "M": "I will thank you, O Lord my God, with my whole heart; I will glorify your name forever.",
      "T": "I will praise you with everything I have, O Lord my God;\nI will keep lifting your name high — forever."
    },
    "13": {
      "L": "For great is thy steadfast love toward me; and thou hast delivered my soul from the lowest depths of Sheol.",
      "M": "For your steadfast love toward me is great; you have rescued my soul from the lowest depths of Sheol.",
      "T": "Your covenant love toward me is immense —\nyou pulled me back from the pit of Sheol,\nfrom the very lowest depths of death."
    },
    "14": {
      "L": "O God, proud men are risen against me, and an assembly of violent men have sought my soul; and they have not set thee before them.",
      "M": "O God, arrogant men have risen up against me; a band of ruthless men seeks my life — they do not keep you before them.",
      "T": "O God — arrogant men have come after me;\na gang of violent people is hunting my life,\nand they give no thought to you at all."
    },
    "15": {
      "L": "But thou, O Lord, art a God full of compassion and gracious, longsuffering, and plenteous in steadfast love and truth.",
      "M": "But you, O Lord, are a compassionate and gracious God, slow to anger, abounding in steadfast love and faithfulness.",
      "T": "But you, O Lord — you are a God of deep compassion,\nwarm and gracious,\nslow to ignite,\noverflowing with covenant love and unwavering faithfulness."
    },
    "16": {
      "L": "O turn unto me, and have mercy upon me; give thy strength unto thy servant, and save the son of thine handmaid.",
      "M": "Turn to me and be gracious to me; give your strength to your servant, and save the son of your maidservant.",
      "T": "Turn toward me — be gracious to me.\nGive your servant your strength;\nsave the son of the woman who has devoted her life to you."
    },
    "17": {
      "L": "Shew me a token for good; that they which hate me may see it, and be ashamed; because thou, LORD, hast holpen me and comforted me.",
      "M": "Show me a sign of your favor, so that those who hate me will see and be ashamed, because you, O LORD, have helped me and comforted me.",
      "T": "Give me a visible sign of your goodness —\nlet those who hate me see it and be humiliated,\nbecause you, O LORD, are the one who has helped me\nand held me close."
    }
  },
  "87": {
    "1": {
      "L": "A Psalm or Song for the sons of Korah. His foundation is in the holy mountains.",
      "M": "A Psalm. A Song of the Sons of Korah. His foundation is on the holy mountains.",
      "T": "A Psalm. A Song of the Sons of Korah.\n\nGod has built his city on the holy mountains —\nits foundations rest on sacred ground."
    },
    "2": {
      "L": "The LORD loveth the gates of Zion more than all the dwellings of Jacob.",
      "M": "The LORD loves the gates of Zion more than all the dwelling places of Jacob.",
      "T": "The LORD loves the gates of Zion\nmore than any other place where Jacob pitches his tent."
    },
    "3": {
      "L": "Glorious things are spoken of thee, O city of God. Selah.",
      "M": "Glorious things are spoken of you, O city of God. Selah.",
      "T": "Glorious things have been said about you,\nO city of God. Selah."
    },
    "4": {
      "L": "I will make mention of Rahab and Babylon to them that know me; behold Philistia, and Tyre, with Ethiopia: this man was born there.",
      "M": "Among those who acknowledge me I will name Rahab and Babylon; and behold — Philistia, Tyre, and Ethiopia: 'This one was born there.'",
      "T": "Among those who know me, God declares:\n'Rahab — Egypt — and Babylon I will count among my own;\nPhilistia, Tyre, even Ethiopia —\nof each one I say: this one was born there.'"
    },
    "5": {
      "L": "And of Zion it shall be said, This and that man was born in her; and the Most High himself shall establish her.",
      "M": "Of Zion it will be said, 'This one and that one were born in her,' and the Most High himself will establish her.",
      "T": "Of Zion they will say: 'Every one of them was born here' —\nand it is the Most High himself who will establish her."
    },
    "6": {
      "L": "The LORD shall count, when he writeth up the peoples, that this man was born there. Selah.",
      "M": "When the LORD records the enrollment of the peoples, he will write, 'This one was born there.' Selah.",
      "T": "The LORD keeps the registry.\nWhen he enrolls the nations he writes beside each name:\n'Born in Zion.' Selah."
    },
    "7": {
      "L": "As well the singers as they that dance: all my springs are in thee.",
      "M": "Singers and dancers alike say, 'All my springs of life are in you.'",
      "T": "Singers and dancers together cry out:\n'Every spring that feeds our life is found in you.'"
    }
  },
  "88": {
    "1": {
      "L": "A Song, a Psalm for the sons of Korah, to the chief Musician upon Mahalath Leannoth. Maschil of Heman the Ezrahite. O LORD God of my salvation, I have cried day and night before thee.",
      "M": "A Song. A Psalm of the Sons of Korah. For the choir director. According to Mahalath Leannoth. A Maskil of Heman the Ezrahite. O LORD, God of my salvation, I cry out to you day and night.",
      "T": "A Song. A Psalm of the Sons of Korah. For the worship leader. According to Mahalath Leannoth. A Maskil of Heman the Ezrahite.\n\nO LORD, God of my salvation —\nI cry out to you day and night."
    },
    "2": {
      "L": "Let my prayer come before thee; incline thine ear unto my cry.",
      "M": "Let my prayer come before you; turn your ear toward my cry.",
      "T": "Let my prayer reach you.\nBend your ear toward what I am crying out."
    },
    "3": {
      "L": "For my soul is full of troubles, and my life draweth nigh unto Sheol.",
      "M": "For my soul is saturated with troubles, and my life draws near to Sheol.",
      "T": "My whole being is swamped with trouble;\nI am being drawn toward Sheol —\nthe realm of the dead is pulling me in."
    },
    "4": {
      "L": "I am counted with them that go down into the pit; I am as a man that hath no strength.",
      "M": "I am reckoned among those who go down to the pit; I have become like a man with no strength at all.",
      "T": "I have been classified among those sinking into the pit —\nwritten off like a man who has nothing left in him."
    },
    "5": {
      "L": "Free among the dead, like the slain that lie in the grave, whom thou rememberest no more; and they are cut off from thy hand.",
      "M": "Like one cast loose among the dead — like the slain who lie in the grave — those you no longer remember, cut off from your hand.",
      "T": "Released into the company of the dead —\nlike soldiers abandoned in the grave\nwhom you hold in memory no longer,\ncut off from everything your hand provides."
    },
    "6": {
      "L": "Thou hast laid me in the lowest pit, in darkness, in the deep.",
      "M": "You have placed me in the lowest pit, in utter darkness, in the depths below.",
      "T": "You yourself have lowered me into the deepest pit —\ninto darkness,\ninto the black deeps below."
    },
    "7": {
      "L": "Thy wrath lieth hard upon me, and thou hast afflicted me with all thy waves. Selah.",
      "M": "Your wrath presses down hard on me, and you have battered me with all your waves. Selah.",
      "T": "The full weight of your wrath is crushing me;\nyou have broken over me, wave after wave. Selah."
    },
    "8": {
      "L": "Thou hast put away mine acquaintance far from me; thou hast made me an abomination unto them; I am shut up, and I cannot come forth.",
      "M": "You have pushed my companions far away from me; you have made me repulsive to them. I am sealed in and cannot get out.",
      "T": "You have driven away everyone who knew me —\nmade me something they recoil from.\nI am locked in with no way out."
    },
    "9": {
      "L": "Mine eye mourneth by reason of affliction; LORD, I have called daily upon thee; I have stretched out my hands unto thee.",
      "M": "My eye wastes away with grief; O LORD, I call to you every day; I spread out my hands toward you.",
      "T": "My eyes have gone dull with weeping and grief.\nEvery day, O LORD, I call out to you;\nI hold out my hands toward you."
    },
    "10": {
      "L": "Wilt thou shew wonders to the dead? Shall the dead arise and praise thee? Selah.",
      "M": "Do you perform wonders for the dead? Can the departed arise and praise you? Selah.",
      "T": "Do you work miracles for the dead?\nCan those who have died rise to praise you? Selah."
    },
    "11": {
      "L": "Shall thy steadfast love be declared in the grave? Or thy faithfulness in Abaddon?",
      "M": "Is your steadfast love announced in the grave? Is your faithfulness spoken of in Abaddon?",
      "T": "Does anyone in the grave speak of your love?\nDo the inhabitants of Abaddon testify to your faithfulness?"
    },
    "12": {
      "L": "Shall thy wonders be known in the dark? And thy righteousness in the land of forgetfulness?",
      "M": "Will your wonders be known in the darkness? Will your righteousness be heard of in the land of forgetting?",
      "T": "Can your astonishing works be known down in the dark?\nCan your justice be spoken of in the land where nothing is remembered?"
    },
    "13": {
      "L": "But unto thee have I cried, O LORD; and in the morning shall my prayer come before thee.",
      "M": "But I, O LORD, cry out to you; in the morning my prayer comes before you.",
      "T": "But I — I keep crying to you, O LORD.\nEvery morning my prayer rises up to meet you."
    },
    "14": {
      "L": "LORD, why castest thou off my soul? Why hidest thou thy face from me?",
      "M": "O LORD, why do you reject my soul? Why do you hide your face from me?",
      "T": "O LORD — why have you thrown me away?\nWhy do you keep hiding your face from me?"
    },
    "15": {
      "L": "I am afflicted and close to death from my youth up; I have suffered thy terrors; I am helpless.",
      "M": "I have been afflicted and near death since my youth; I suffer your terrors; I am overcome.",
      "T": "Since childhood I have lived in affliction, barely surviving —\nyour terrors have pressed down on me all my life;\nI am overwhelmed and numb."
    },
    "16": {
      "L": "Thy fierce wrath goeth over me; thy terrors have cut me off.",
      "M": "Your fierce wrath has swept over me; your terrors have destroyed me.",
      "T": "The torrent of your blazing wrath has surged over me;\nyour assaults have cut me down."
    },
    "17": {
      "L": "They came round about me daily like water; they compassed me about together.",
      "M": "They surround me like water all day long; they close in on me together.",
      "T": "Like a flood they circle me all day long;\nthey converge on me from every side."
    },
    "18": {
      "L": "Thou hast put far from me lover and friend; and mine acquaintance are in darkness.",
      "M": "You have put far from me those who love me and my friends; my companions are in darkness.",
      "T": "You have taken from me every lover and every friend —\nthey are all gone.\nDarkness alone remains."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 85–88 written.')

if __name__ == '__main__':
    main()
