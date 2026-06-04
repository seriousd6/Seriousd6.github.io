"""
MKT Psalms chapters 79–84 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-79-84.py

=== Overview of this unit ===

This unit covers six psalms spanning two distinct collections:
- Psalms 79–83 belong to the Asaph collection (Book III, Pss 73–89), continuing within
  the Elohistic Psalter (Pss 42–83) where Elohim dominates over YHWH.
- Psalm 84 opens the second Korah collection (Pss 84–88), shifting to the Korahite
  tradition associated with the temple singers (cf. 1 Chr 9:19).

Pss 79–80 are national laments closely paralleling Ps 74, likely responding to the
Babylonian destruction of Jerusalem (586 BC). Ps 81 is a covenant-renewal liturgy for
the autumn festival. Ps 82 is the divine-council judgment poem. Ps 83 is the longest
imprecatory prayer in the Psalter (ten enemy nations named). Ps 84 is a beloved
pilgrimage psalm expressing deep longing for the house of God.

=== Superscriptions ===

Superscription text is merged into v1 of each psalm (following convention established
in PSA-1 through PSA-13a), separated from the verse body by a blank line in T tier.

Ps 79: "A Psalm of Asaph" — no performance designation; simple identification.
Ps 80: "To the chief Musician upon Shoshannimeduth, A Psalm of Asaph."
        Shoshannimeduth (שׁוֹשַׁנִּים עֵדוּת) = "Lilies of the Covenant/Testimony";
        M/T: "To the choirmaster. To the tune 'Lilies of the Covenant.'"
Ps 81: "To the chief Musician upon Gittith, A Psalm of Asaph."
        Gittith (גִּתִּית) = a tune associated with Gath or the winepress;
        M/T: "To the choirmaster. To the tune of the Gittith."
Ps 82: "A Psalm of Asaph" — no performance designation.
Ps 83: "A Song or Psalm of Asaph" — dual genre label (shiyr + mizmor); both retained.
Ps 84: "To the chief Musician upon Gittith, A Psalm for the sons of Korah."
        Same Gittith tune; note authorship shift from Asaph to the Korah guild.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M; "the LORD" in T.
      Appears at Pss 79:5,9; 80:4,19; 81:10; 83:16,18; 84:1,2,3,8,11,12.
      The Elohistic dominance of Pss 79–83 means YHWH is less frequent than Elohim;
      its appearance is theologically emphatic.

H430  (אֱלֹהִים, Elohim): "God" in all tiers throughout all six psalms.
      In Ps 82 the same word designates both the one supreme God (vv1,8) and the
      divine council members / unjust judges who are addressed as "gods" (vv1,6);
      context distinguishes usage (see note below).

H3068+H6635 (יהוה צְבָאוֹת, YHWH of hosts): "LORD of hosts" in L/M/T.
      Appears at Pss 80:4,7,14,19; 84:1,3,8,12. "LORD of hosts" kept in T;
      the military-heavenly-council image is essential to both psalms.

H430+H6635 (אֱלֹהִים צְבָאוֹת, God of hosts): "God of hosts" in L/M/T. Ps 80:7,14.

H3068+H430+H6635 (LORD God of hosts): "LORD God of hosts" in L/M/T. Pss 80:4; 84:8.

H2617 (חֶסֶד, hesed): Does not appear as a key term in Pss 79–84, but covenant
      loyalty is the implicit basis of every appeal throughout the unit.

H5542 (סֶלָה, Selah): Retained as "Selah" at end of: Ps 81:7; Ps 82:2; Ps 83:8;
      Ps 84:4,8.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M; varies in T.
      Key occurrence: Ps 84:2 — rendered "My whole being" in T to capture the
      Hebrew sense of nefesh as the whole embodied person, not merely the spirit.

H430 in the divine-council context (Ps 82): At v1 "congregation of the mighty"
      (בַּעֲדַת-אֵל, 'adat el = divine assembly) and "among the gods" (אֱלֹהִים =
      elohim, the council members). At v6 the "gods" being addressed are the same
      council members now sentenced to die as mortals. Rendered "gods" in L/M;
      in T "divine rulers" at v1 description, "you are gods" at v6 (preserving the
      exact wording cited by Jesus in John 10:34 — crucial for NT connection).

H3068 as proper name in Ps 83:18: The verse makes the divine name programmatic:
      "whose name alone is YHWH." In L/M: "whose name alone is the LORD"; in T:
      "Yahweh is your name" — bringing the personal name forward precisely where
      the text foregrounds it as the point.

H4546 (מְסִלּוֹת, mesilloth, "highways/pilgrim roads" at Ps 84:5): Rendered
      "ways" in L (ambiguous, faithful to KJV tradition), "pilgrim roads" in M,
      "the pilgrim roads to Zion" in T (explicit destination clarified).

H1057 (בָּכָא, Baca at Ps 84:6): Possibly "weeping" (related to H1058, bakah) or
      a species of balsam tree. Untranslated as "Baca" in L/M; T adds interpretive
      gloss: "the valley of Baca — the valley of weeping."

Ps 80 refrain escalation: The three refrains deliberately escalate the divine title:
      v3: "O God" (Elohim); v7: "O God of hosts" (Elohim of Hosts); v19: "O LORD God
      of hosts" (YHWH Elohim of Hosts). This escalation is preserved exactly in all
      three tiers; it is a deliberate literary-theological intensification.

=== OT echoes and NT connections ===

- Ps 79:6,8–9 → Rev 16:1 (pouring out wrath); the wrath-vocabulary feeds apocalyptic.
- Ps 79:9 "for your name's sake" → refrain of the OT petition tradition (Ezek 20:9,14).
- Ps 80:1 "Shepherd of Israel" → John 10:11 (Jesus as the Good Shepherd).
- Ps 80:8–11 Vine from Egypt → John 15:1 ("I am the true vine"); Jesus's claim
  fulfills and exceeds the vine allegory of Ps 80.
- Ps 80:17 "son of man" (ben-adam) → Dan 7:13; Matt 8:20; the Davidic king at God's
  right hand becomes a messianic title.
- Ps 81:10 "Open your mouth wide" → Matt 5:6 (those who hunger and thirst will be
  filled); the abundance-provision theology.
- Ps 82:6–7 "You are gods" → John 10:34 — Jesus quotes this verse in the controversy
  about his own divine identity; the psalm's logic underpins his argument.
- Ps 84:2 "Living God" → Matt 16:16 ("Son of the living God"); the title distinguishes
  YHWH from lifeless idols.
- Ps 84:10 "doorkeeper" → radical honor-shame inversion: the lowest role in God's house
  surpasses the highest rank among the wicked.
- Ps 84:11 "sun and shield" → Rev 21:23 (God as light); Eph 6:16 (shield of faith).

=== Aspect and tense notes ===

Ps 79: Past tense for the lament (vv1–4, disaster has happened); present and imperative
in the petition (vv5–12); future promise at v13.

Ps 80: Three refrains (vv3,7,19) are jussive imperatives ("Turn us again!"). The vine
narrative (vv8–11) is all historical past (completed acts of planting/growth). Vv12–13
shift to ongoing present (the vine is currently being ravaged). Vv14–18 are petitions.

Ps 81: The psalm shifts mid-v5 from third-person past to direct divine speech (first
person). God's speech (vv6–16) uses past tense for historical acts (Exodus), then
contrary-to-fact conditionals for what could have been (vv13–16, "If only... I would
have...").

Ps 82: God's speech in vv2–7 mixes rhetorical questions, imperatives, and declarations.
The final verse (v8) is the psalmist's imperative plea directed back at God.

Ps 83: Predominantly imperative — the psalmist is urgently requesting action. Historical
references (vv9–12) use past tense to ground the appeal in precedent.

Ps 84: Present tense of experience dominates (the pilgrim is currently longing, walking).
Refrains of blessing ("Blessed") are general present/gnomic.
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
  "79": {
    "1": {
      "L": "A Psalm of Asaph. O God, the nations are come into thine inheritance; thy holy temple have they defiled; they have laid Jerusalem on heaps.",
      "M": "A Psalm of Asaph. O God, the nations have invaded your inheritance; they have defiled your holy temple; they have laid Jerusalem in ruins.",
      "T": "A Psalm of Asaph.\n\nO God — the nations have stormed into your inheritance;\nthey have desecrated your holy temple;\nthey have left Jerusalem a heap of rubble."
    },
    "2": {
      "L": "The dead bodies of thy servants have they given to be meat unto the fowls of heaven, the flesh of thy saints unto the beasts of the earth.",
      "M": "They have given the corpses of your servants as food to the birds of the heavens, the flesh of your godly ones to the beasts of the earth.",
      "T": "The corpses of your servants they flung out\nas carrion for the birds of the sky;\nthe flesh of your faithful they left\nfor the beasts of the field."
    },
    "3": {
      "L": "Their blood have they shed like water round about Jerusalem; and there was none to bury them.",
      "M": "They have poured out their blood like water all around Jerusalem, and there was no one to bury the dead.",
      "T": "Their blood has been poured out like water\nall around Jerusalem —\nand there was no one left to bury them."
    },
    "4": {
      "L": "We are become a reproach to our neighbours, a scorn and derision to them that are round about us.",
      "M": "We have become a reproach to our neighbors, a mockery and derision to those around us.",
      "T": "We have become the taunt of our neighbors —\nscorned and mocked\nby everyone who surrounds us."
    },
    "5": {
      "L": "How long, LORD? wilt thou be angry for ever? shall thy jealousy burn like fire?",
      "M": "How long, O LORD? Will you be angry forever? Will your jealousy burn like fire?",
      "T": "How long, O LORD — how long?\nWill your anger smolder on without end?\nWill your burning jealousy never cool?"
    },
    "6": {
      "L": "Pour out thy wrath upon the heathen that have not known thee, and upon the kingdoms that have not called upon thy name.",
      "M": "Pour out your wrath on the nations that do not know you, and on the kingdoms that do not call on your name!",
      "T": "Pour out your wrath on the nations who refuse to know you —\non the kingdoms that will not call on your name!"
    },
    "7": {
      "L": "For they have devoured Jacob, and laid waste his dwelling place.",
      "M": "For they have devoured Jacob and laid waste his homeland.",
      "T": "For they have swallowed Jacob whole\nand left his home a wasteland."
    },
    "8": {
      "L": "O remember not against us former iniquities; let thy tender mercies speedily prevent us: for we are brought very low.",
      "M": "Do not hold our former iniquities against us; let your compassion come quickly to meet us, for we are utterly brought low.",
      "T": "Do not hold our ancient sins against us;\nlet your compassion race ahead to meet us —\nfor we are sinking, brought as low as we can go."
    },
    "9": {
      "L": "Help us, O God of our salvation, for the glory of thy name: and deliver us, and purge away our sins, for thy name's sake.",
      "M": "Help us, O God of our salvation, for the glory of your name; deliver us and forgive our sins, for your name's sake!",
      "T": "Help us, O God who saves us —\nact for the honor of your name!\nDeliver us. Forgive our sins.\nYour name is at stake."
    },
    "10": {
      "L": "Wherefore should the heathen say, Where is their God? let him be known among the heathen in our sight by the revenging of the blood of thy servants which is shed.",
      "M": "Why should the nations say, 'Where is their God?' Before our eyes, let the avenging of your servants' shed blood be known among the nations.",
      "T": "Why should the nations sneer: 'Where is their God?'\nLet them watch with their own eyes\nas you answer the blood of your servants\nthat cries out before you."
    },
    "11": {
      "L": "Let the sighing of the prisoner come before thee; according to the greatness of thy power preserve thou those that are appointed to die.",
      "M": "Let the groaning of the prisoner come before you; according to your great power, preserve those condemned to die!",
      "T": "Let the groaning of the prisoner reach your ears;\nby the might of your arm,\nspare those who have been sentenced to death."
    },
    "12": {
      "L": "And render unto our neighbours sevenfold into their bosom their reproach, wherewith they have reproached thee, O Lord.",
      "M": "Return to our neighbors sevenfold into their bosom the reproach with which they have taunted you, O Lord.",
      "T": "Pay back our neighbors sevenfold —\nlet every insult they hurled at you, O Lord,\nfall back into their own laps, multiplied."
    },
    "13": {
      "L": "So we thy people and sheep of thy pasture will give thee thanks for ever: we will shew forth thy praise to all generations.",
      "M": "Then we your people, the sheep of your pasture, will give you thanks forever; from generation to generation we will recount your praise.",
      "T": "Then we — your people,\nthe flock you shepherd —\nwill praise you forever.\nFrom age to age we will tell the whole story\nof all you have done."
    }
  },
  "80": {
    "1": {
      "L": "To the chief Musician upon Shoshannimeduth, A Psalm of Asaph. Give ear, O Shepherd of Israel, thou that leadest Joseph like a flock; thou that dwellest between the cherubims, shine forth.",
      "M": "To the choirmaster. To the tune 'Lilies of the Covenant.' A Psalm of Asaph. Give ear, O Shepherd of Israel, you who lead Joseph like a flock! You who are enthroned above the cherubim, shine forth!",
      "T": "To the worship leader. To the tune 'Lilies of the Covenant.' A Psalm of Asaph.\n\nHear us, O Shepherd of Israel —\nyou who lead Joseph like a flock,\nyou who are enthroned above the cherubim:\nshine forth!"
    },
    "2": {
      "L": "Before Ephraim and Benjamin and Manasseh stir up thy strength, and come and save us.",
      "M": "Before Ephraim and Benjamin and Manasseh, stir up your might and come to save us!",
      "T": "Before the tribes of Ephraim, Benjamin, and Manasseh —\nstir up your power\nand come to rescue us!"
    },
    "3": {
      "L": "Turn us again, O God, and cause thy face to shine; and we shall be saved.",
      "M": "Restore us, O God; let your face shine upon us, that we may be saved!",
      "T": "Restore us, O God —\nlet your face shine on us,\nand we will be saved!"
    },
    "4": {
      "L": "O LORD God of hosts, how long wilt thou be angry against the prayer of thy people?",
      "M": "O LORD God of hosts, how long will you be angry with your people's prayers?",
      "T": "O LORD God of hosts — how long\nwill you fume against the very prayers\nyour people bring before you?"
    },
    "5": {
      "L": "Thou feedest them with the bread of tears; and givest them tears to drink in great measure.",
      "M": "You have fed them with the bread of tears and given them tears to drink in full measure.",
      "T": "You have given us tears for bread\nand measured out cups full of weeping for us to drink."
    },
    "6": {
      "L": "Thou makest us a strife unto our neighbours: and our enemies laugh among themselves.",
      "M": "You make us a bone of contention for our neighbors, and our enemies mock us.",
      "T": "You have made us an object of dispute among our neighbors;\nour enemies laugh at what has become of us."
    },
    "7": {
      "L": "Turn us again, O God of hosts, and cause thy face to shine; and we shall be saved.",
      "M": "Restore us, O God of hosts; let your face shine upon us, that we may be saved!",
      "T": "Restore us, O God of hosts —\nlet your face shine on us,\nand we will be saved!"
    },
    "8": {
      "L": "Thou hast brought a vine out of Egypt: thou hast cast out the heathen, and planted it.",
      "M": "You brought a vine out of Egypt; you drove out the nations and planted it.",
      "T": "You uprooted a vine from Egypt,\ncleared the land by driving out the nations,\nand planted it here."
    },
    "9": {
      "L": "Thou preparedst room before it, and didst cause it to take deep root, and it filled the land.",
      "M": "You cleared the ground before it; it took deep root and filled all the land.",
      "T": "You prepared the soil before it;\nit sank deep roots\nand spread until it covered the land."
    },
    "10": {
      "L": "The hills were covered with the shadow of it, and the boughs thereof were like the goodly cedars.",
      "M": "The mountains were covered with its shade, and its branches were like towering cedars.",
      "T": "Its shade covered the mountains;\nits branches grew like the great cedars of Lebanon."
    },
    "11": {
      "L": "She sent out her boughs unto the sea, and her branches unto the river.",
      "M": "It sent its branches to the sea and its shoots to the River.",
      "T": "Its branches reached the sea to the west;\nits shoots stretched east to the Euphrates."
    },
    "12": {
      "L": "Why hast thou then broken down her hedges, so that all they which pass by the way do pluck her?",
      "M": "Why then have you broken down its walls, so that all who pass along the road pluck its fruit?",
      "T": "Why, then, have you torn down its walls?\nNow every passerby stops and strips it bare."
    },
    "13": {
      "L": "The boar out of the wood doth waste it, and the wild beast of the field doth devour it.",
      "M": "The boar from the forest ravages it, and all the wild creatures of the field feed on it.",
      "T": "The wild boar out of the forest tears it apart;\nthe beasts of the field devour whatever remains."
    },
    "14": {
      "L": "Return, we beseech thee, O God of hosts: look down from heaven, and behold, and visit this vine;",
      "M": "Return, we pray, O God of hosts! Look down from heaven, see, and tend this vine!",
      "T": "Turn back to us, O God of hosts —\nlook down from heaven;\nsee it. Come and tend this vine."
    },
    "15": {
      "L": "And the vineyard which thy right hand hath planted, and the branch that thou madest strong for thyself.",
      "M": "Look at the stock your right hand planted, and the son you made strong for yourself.",
      "T": "Look at what your right hand planted —\nthe vine you cultivated as your own;\nlook at the son you raised up in your strength."
    },
    "16": {
      "L": "It is burned with fire, it is cut down: they perish at the rebuke of thy countenance.",
      "M": "It is burned with fire and cut down; may they perish at the rebuke of your face!",
      "T": "It has been burned; it has been hacked to the ground —\nlet those who did this perish\nat a single word of rebuke from your face."
    },
    "17": {
      "L": "Let thy hand be upon the man of thy right hand, upon the son of man whom thou madest strong for thyself.",
      "M": "Let your hand be on the man of your right hand, the son of man whom you have made strong for yourself.",
      "T": "Let your hand rest on the one at your right hand —\nthe son of man\nyou yourself have chosen and strengthened."
    },
    "18": {
      "L": "So will not we go back from thee: quicken us, and we will call upon thy name.",
      "M": "Then we will not turn back from you; give us life, and we will call on your name!",
      "T": "Then we will never turn away from you again.\nGive us new life,\nand we will call on your name."
    },
    "19": {
      "L": "Turn us again, O LORD God of hosts, cause thy face to shine; and we shall be saved.",
      "M": "Restore us, O LORD God of hosts; let your face shine upon us, that we may be saved!",
      "T": "Restore us, O LORD God of hosts —\nlet your face shine on us,\nand we will be saved!"
    }
  },
  "81": {
    "1": {
      "L": "To the chief Musician upon Gittith, A Psalm of Asaph. Sing aloud unto God our strength: make a joyful noise unto the God of Jacob.",
      "M": "To the choirmaster. To the tune of the Gittith. A Psalm of Asaph. Sing aloud to God our strength; shout for joy to the God of Jacob!",
      "T": "To the worship leader. To the tune of the Gittith. A Psalm of Asaph.\n\nSing out to God, our strength —\nshout for joy to the God of Jacob!"
    },
    "2": {
      "L": "Take a psalm, and bring hither the timbrel, the pleasant harp with the psaltery.",
      "M": "Raise a song; sound the tambourine, the sweet lyre with the harp.",
      "T": "Strike up the music!\nBring the tambourine,\nthe sweet-sounding lyre, and the harp."
    },
    "3": {
      "L": "Blow up the trumpet in the new moon, in the time appointed, on our solemn feast day.",
      "M": "Blow the trumpet at the new moon, at the full moon, on our feast day.",
      "T": "Sound the trumpet at the new moon —\nat the full moon, on the appointed day,\nthe day of our great festival."
    },
    "4": {
      "L": "For this was a statute for Israel, and a law of the God of Jacob.",
      "M": "For it is a statute for Israel, a rule given by the God of Jacob.",
      "T": "This is what God has required of Israel —\na law laid down by the God of Jacob himself."
    },
    "5": {
      "L": "This he ordained in Joseph for a testimony, when he went out through the land of Egypt: where I heard a language that I understood not.",
      "M": "He established it as a decree in Joseph when he went out over the land of Egypt. I hear a voice I had not known:",
      "T": "He made it a covenant requirement for Joseph\nwhen God went out over the land of Egypt.\nNow I hear a voice I had not known before —"
    },
    "6": {
      "L": "'I removed his shoulder from the burden: his hands were delivered from the pots.'",
      "M": "'I removed the burden from his shoulder; his hands were freed from the basket.'",
      "T": "'I lifted the crushing load from his shoulder;\nI freed his hands from the slave's brick-basket.'"
    },
    "7": {
      "L": "'Thou calledst in trouble, and I delivered thee; I answered thee in the secret place of thunder: I proved thee at the waters of Meribah. Selah.'",
      "M": "'In your distress you called, and I rescued you; I answered you from the hidden place of thunder; I tested you at the waters of Meribah. Selah.'",
      "T": "'You cried out in your trouble, and I came to rescue you;\nI answered you from inside the thunder's hiding place.\nI put you to the test at the waters of Meribah. Selah.'"
    },
    "8": {
      "L": "'Hear, O my people, and I will testify unto thee: O Israel, if thou wilt hearken unto me;'",
      "M": "'Listen, O my people, while I admonish you! O Israel, if you would only listen to me!'",
      "T": "'Hear me, my people — let me speak plainly:\nO Israel, if you would only listen!'"
    },
    "9": {
      "L": "'There shall no strange god be in thee; neither shalt thou worship any strange god.'",
      "M": "'There must be no foreign god among you; you must not bow down to any alien god.'",
      "T": "'No foreign god may have a place among you;\nyou must never bow to any god but me.'"
    },
    "10": {
      "L": "'I am the LORD thy God, which brought thee out of the land of Egypt: open thy mouth wide, and I will fill it.'",
      "M": "'I am the LORD your God, who brought you up out of the land of Egypt. Open your mouth wide, and I will fill it.'",
      "T": "'I am the LORD your God —\nthe one who brought you out of Egypt.\nOpen your mouth as wide as you can;\nI will fill it.'"
    },
    "11": {
      "L": "'But my people would not hearken to my voice; and Israel would none of me.'",
      "M": "'But my people did not listen to my voice; Israel would not submit to me.'",
      "T": "'But my people refused to hear my voice;\nIsrael wanted nothing to do with me.'"
    },
    "12": {
      "L": "'So I gave them up unto their own hearts' lust: and they walked in their own counsels.'",
      "M": "'So I gave them over to their stubborn hearts, to follow their own devices.'",
      "T": "'So I let them go —\nI handed them over to the desires of their own stubborn hearts\nto do exactly as they pleased.'"
    },
    "13": {
      "L": "'Oh that my people had hearkened unto me, and Israel had walked in my ways!'",
      "M": "'If only my people would listen to me, if only Israel would walk in my ways!'",
      "T": "'Oh, if only my people would listen!\nIf only Israel would walk in my ways!'"
    },
    "14": {
      "L": "'I should soon have subdued their enemies, and turned my hand against their adversaries.'",
      "M": "'I would quickly have subdued their enemies and turned my hand against their foes.'",
      "T": "'How swiftly I would have crushed their enemies\nand turned my power against everyone who opposed them!'"
    },
    "15": {
      "L": "'The haters of the LORD should have submitted themselves unto him: but their time should have endured for ever.'",
      "M": "'Those who hate the LORD would have cringed before him, and Israel's time of peace would have endured forever.'",
      "T": "'Those who hate the LORD would have groveled before him,\nand Israel's flourishing would have gone on forever.'"
    },
    "16": {
      "L": "'He should have fed them also with the finest of the wheat: and with honey out of the rock should I have satisfied thee.'",
      "M": "'I would have fed you with the finest of the wheat, and with honey from the rock I would have satisfied you.'",
      "T": "'I would have fed you the finest wheat;\nwith honey flowing from the rock\nI would have satisfied you completely.'"
    }
  },
  "82": {
    "1": {
      "L": "A Psalm of Asaph. God standeth in the congregation of the mighty; he judgeth among the gods.",
      "M": "A Psalm of Asaph. God has taken his place in the divine assembly; in the midst of the gods he holds judgment:",
      "T": "A Psalm of Asaph.\n\nGod has risen to stand in the divine assembly;\nin the midst of the heavenly council he pronounces judgment:"
    },
    "2": {
      "L": "'How long will ye judge unjustly, and accept the persons of the wicked? Selah.'",
      "M": "'How long will you go on judging unjustly and showing partiality to the wicked? Selah.'",
      "T": "'How long will you keep pronouncing corrupt verdicts,\nshowing favor to the wicked at every turn? Selah.'"
    },
    "3": {
      "L": "'Defend the poor and fatherless: do justice to the afflicted and needy.'",
      "M": "'Defend the poor and fatherless; maintain the right of the afflicted and the destitute.'",
      "T": "'Defend those who have nothing — the poor, the orphan;\nsee that justice is actually done for the afflicted and the needy.'"
    },
    "4": {
      "L": "'Deliver the poor and needy: rid them out of the hand of the wicked.'",
      "M": "'Rescue the poor and needy; save them from the grip of the wicked.'",
      "T": "'Rescue the poor and the needy;\npry them out of the wicked's grasp.'"
    },
    "5": {
      "L": "'They know not, neither will they understand; they walk on in darkness: all the foundations of the earth are out of course.'",
      "M": "'They have no knowledge and no understanding; they walk about in darkness, and all the foundations of the earth are shaken.'",
      "T": "'They will not know. They will not understand.\nThey walk through the world in moral darkness —\nand when justice fails at the top,\nthe very foundations of the earth give way.'"
    },
    "6": {
      "L": "'I said, Ye are gods; and all of you are children of the most High.'",
      "M": "'I declared, \"You are gods, sons of the Most High, every one of you.\"'",
      "T": "'I myself declared it: you are gods —\nevery one of you a son of the Most High.'"
    },
    "7": {
      "L": "'But ye shall die like men, and fall like one of the princes.'",
      "M": "'Nevertheless, you will die like mere mortals and fall like any fallen ruler.'",
      "T": "'And yet — you will die just like ordinary men;\nyou will fall like any other ruler\nwho failed those in his care.'"
    },
    "8": {
      "L": "Arise, O God, judge the earth: for thou shalt inherit all nations.",
      "M": "Rise up, O God, judge the earth; for all the nations belong to you!",
      "T": "Rise up, O God — judge the earth!\nAll the nations are your inheritance;\nit is time to claim what is yours."
    }
  },
  "83": {
    "1": {
      "L": "A Song or Psalm of Asaph. Keep not thou silence, O God: hold not thy peace, and be not still, O God.",
      "M": "A Song. A Psalm of Asaph. O God, do not remain silent; do not hold your peace or be still, O God!",
      "T": "A Song. A Psalm of Asaph.\n\nO God, do not stay silent!\nDo not hold back. Do not be still, O God —"
    },
    "2": {
      "L": "For, lo, thine enemies make a tumult: and they that hate thee have lifted up the head.",
      "M": "For behold, your enemies are in an uproar; those who hate you have raised their heads.",
      "T": "for look — your enemies are roaring;\nthose who hate you have lifted their heads in open defiance."
    },
    "3": {
      "L": "They have taken crafty counsel against thy people, and consulted against thy hidden ones.",
      "M": "They devise cunning plans against your people and scheme against your treasured ones.",
      "T": "They are plotting in secret against your people,\nconsulting against the ones you hold as your own treasure."
    },
    "4": {
      "L": "They have said, Come, and let us cut them off from being a nation; that the name of Israel may be no more in remembrance.",
      "M": "They say, 'Come, let us wipe them out as a nation; let the name of Israel be remembered no more!'",
      "T": "'Come,' they say, 'let us erase them from the map —\nlet the name Israel vanish from memory forever.'"
    },
    "5": {
      "L": "For they have consulted together with one consent: they are confederate against thee:",
      "M": "For they conspire with one accord; they have made a covenant against you —",
      "T": "They have formed one united conspiracy;\nthey have made a pact against you —"
    },
    "6": {
      "L": "the tents of Edom, and the Ishmaelites; of Moab, and the Hagarenes;",
      "M": "the tents of Edom and the Ishmaelites, Moab and the Hagrites,",
      "T": "the clans of Edom and the Ishmaelites,\nMoab and the Hagrites,"
    },
    "7": {
      "L": "Gebal, and Ammon, and Amalek; the Philistines with the inhabitants of Tyre;",
      "M": "Gebal and Ammon and Amalek, Philistia with the inhabitants of Tyre,",
      "T": "Gebal, Ammon, and Amalek,\nPhilistia alongside the people of Tyre."
    },
    "8": {
      "L": "Assur also is joined with them: they have holpen the children of Lot. Selah.",
      "M": "Assyria too has joined them; they lend their strength to the children of Lot. Selah.",
      "T": "Even Assyria has entered the alliance —\nlending its military power to the cause of Lot's descendants. Selah."
    },
    "9": {
      "L": "Do unto them as unto the Midianites; as to Sisera, as to Jabin, at the brook of Kison:",
      "M": "Do to them as you did to Midian, as to Sisera and Jabin at the river Kishon —",
      "T": "Deal with them as you dealt with Midian,\nas you dealt with Sisera and Jabin at the river Kishon —"
    },
    "10": {
      "L": "Which perished at Endor: they became as dung for the earth.",
      "M": "who were destroyed at En-dor and became dung for the ground.",
      "T": "who were annihilated at En-dor\nand became nothing but dung rotting in the ground."
    },
    "11": {
      "L": "Make their nobles like Oreb, and like Zeeb: yea, all their princes as Zebah, and as Zalmunna:",
      "M": "Make their nobles like Oreb and Zeeb; make all their princes like Zebah and Zalmunna —",
      "T": "Make their leaders like Oreb and Zeeb;\nlet all their commanders meet the end of Zebah and Zalmunna —"
    },
    "12": {
      "L": "Who said, Let us take to ourselves the houses of God in possession.",
      "M": "who said, 'Let us seize for ourselves the pastures of God.'",
      "T": "those who boasted: 'We will seize God's own land\nand claim it as ours.'"
    },
    "13": {
      "L": "O my God, make them like a wheel; as the stubble before the wind.",
      "M": "O my God, make them like whirling dust, like chaff before the wind.",
      "T": "O my God, make them like tumbleweeds —\nlike dry chaff the wind scatters\nand never finds again."
    },
    "14": {
      "L": "As the fire burneth a wood, and as the flame setteth the mountains on fire;",
      "M": "As fire consumes the forest, as the flame sets the mountains ablaze —",
      "T": "As wildfire sweeps through a forest,\nas flame leaps to set whole mountains burning —"
    },
    "15": {
      "L": "So persecute them with thy tempest, and make them afraid with thy storm.",
      "M": "so pursue them with your storm and terrify them with your tempest.",
      "T": "so pursue them with your storm;\ndrive them into terror with your hurricane."
    },
    "16": {
      "L": "Fill their faces with shame; that they may seek thy name, O LORD.",
      "M": "Fill their faces with shame, that they may seek your name, O LORD.",
      "T": "Cover their faces with shame —\nperhaps in their humiliation\nthey will finally seek your name, O LORD."
    },
    "17": {
      "L": "Let them be confounded and troubled for ever; yea, let them be put to shame, and perish:",
      "M": "Let them be put to shame and dismayed forever; let them be disgraced and perish!",
      "T": "Let them be shamed and shattered — forever;\nlet them be disgraced and destroyed."
    },
    "18": {
      "L": "That men may know that thou, whose name alone is the LORD, art the most high over all the earth.",
      "M": "Let them know that you alone, whose name is the LORD, are the Most High over all the earth.",
      "T": "Let every nation learn at last\nthat you alone — Yahweh is your name —\nare the Most High over all the earth."
    }
  },
  "84": {
    "1": {
      "L": "To the chief Musician upon Gittith, A Psalm for the sons of Korah. How amiable are thy tabernacles, O LORD of hosts!",
      "M": "To the choirmaster. To the tune of the Gittith. A Psalm for the sons of Korah. How lovely is your dwelling place, O LORD of hosts!",
      "T": "To the worship leader. To the tune of the Gittith. A Psalm for the sons of Korah.\n\nHow beloved is your dwelling place —\nhow beautiful!\nO LORD of hosts!"
    },
    "2": {
      "L": "My soul longeth, yea, even fainteth for the courts of the LORD: my heart and my flesh crieth out for the living God.",
      "M": "My soul longs, yes, faints for the courts of the LORD; my heart and my flesh cry out for the living God.",
      "T": "My whole being longs for the courts of the LORD —\nI am faint with longing.\nMy heart, my very flesh, cries out\nfor the living God."
    },
    "3": {
      "L": "Yea, the sparrow hath found an house, and the swallow a nest for herself, where she may lay her young, even thine altars, O LORD of hosts, my King and my God.",
      "M": "Even the sparrow has found a home, and the swallow a nest for herself where she may lay her young — even your altars, O LORD of hosts, my King and my God!",
      "T": "Even the sparrow has found a home there,\nand the swallow a nest where she can lay her young —\nright there beside your altars,\nO LORD of hosts, my King, my God!"
    },
    "4": {
      "L": "Blessed are they that dwell in thy house: they will be still praising thee. Selah.",
      "M": "Blessed are those who dwell in your house; they are ever singing your praise! Selah.",
      "T": "How blessed are those who live in your house —\nthey never stop praising you. Selah."
    },
    "5": {
      "L": "Blessed is the man whose strength is in thee; in whose heart are the ways of them.",
      "M": "Blessed is the man whose strength is in you, in whose heart are the pilgrim roads.",
      "T": "Blessed is the person whose strength is in you —\nthe one who already has the pilgrim roads to Zion\nwritten on their heart."
    },
    "6": {
      "L": "Who passing through the valley of Baca make it a well; the rain also filleth the pools.",
      "M": "As they pass through the valley of Baca they make it a place of springs; the early rain also covers it with pools.",
      "T": "As they pass through the valley of Baca — the valley of weeping —\nthey turn it into a place of springs;\nthe early rain clothes it with pools."
    },
    "7": {
      "L": "They go from strength to strength, every one of them in Zion appeareth before God.",
      "M": "They go from strength to strength; each one appears before God in Zion.",
      "T": "They move from strength to strength,\nuntil every one of them stands\nbefore God in Zion."
    },
    "8": {
      "L": "O LORD God of hosts, hear my prayer: give ear, O God of Jacob. Selah.",
      "M": "O LORD God of hosts, hear my prayer; give ear, O God of Jacob! Selah.",
      "T": "O LORD God of hosts — hear my prayer!\nGive ear to me, O God of Jacob. Selah."
    },
    "9": {
      "L": "Behold, O God our shield, and look upon the face of thine anointed.",
      "M": "Behold our shield, O God; look on the face of your anointed!",
      "T": "Look on us, O God — our shield!\nTurn your face toward your anointed king."
    },
    "10": {
      "L": "For a day in thy courts is better than a thousand. I had rather be a doorkeeper in the house of my God, than to dwell in the tents of wickedness.",
      "M": "For a single day in your courts is better than a thousand elsewhere. I would rather stand at the threshold of the house of my God than dwell comfortably in the tents of the wicked.",
      "T": "One day in your courts outweighs a thousand anywhere else.\nI would rather stand at the door of my God's house as a beggar\nthan make myself at home in the finest tent the wicked can offer."
    },
    "11": {
      "L": "For the LORD God is a sun and shield: the LORD will give grace and glory: no good thing will he withhold from them that walk uprightly.",
      "M": "For the LORD God is a sun and shield; the LORD bestows favor and honor. No good thing does he withhold from those who walk with integrity.",
      "T": "For the LORD God is sun and shield —\nsun: the source of all light and life;\nshield: our protection against all that would destroy us.\nHe lavishes favor and honor\nand withholds not one good thing\nfrom those who walk in integrity."
    },
    "12": {
      "L": "O LORD of hosts, blessed is the man that trusteth in thee.",
      "M": "O LORD of hosts, blessed is the one who trusts in you!",
      "T": "O LORD of hosts —\nblessed, truly blessed,\nis everyone who puts their trust in you."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 79–84 written.')

if __name__ == '__main__':
    main()
