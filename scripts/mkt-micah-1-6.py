"""
MKT Micah chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-micah-1-6.py

=== CHAPTER OVERVIEW ===

Micah of Moresheth-gath was a Judean country prophet who ministered during the reigns of
Jotham, Ahaz, and Hezekiah — contemporaneous with Isaiah, though his vantage is rural
southwestern Judah, not Jerusalem's court. He is distinctive for giving the sharpest
social-justice indictment of any eighth-century prophet (chs. 2–3), the clearest
messianic-geographic prophecy (5:2, naming Bethlehem Ephrathah), and the most compressed
ethical summary in the Hebrew Bible (6:8).

Chapter 1: Theophany of divine judgment descending on Samaria and Judah. Cosmic summons
  (all peoples as witnesses), world-shaking arrival of the LORD, Samaria's destruction
  decreed. The lament section (1:8–16) is a sequence of wordplays on Judean city names —
  the disaster is travelling south. Micah himself takes up the qinah funeral lament.

Chapter 2: Social predation by the powerful — night plots to seize fields by daylight.
  The LORD announces a matching counter-device: disaster for this family. A silencing
  confrontation with false prophets (2:6–11) who want comfortable oracles. Closes with
  a promise of the Shepherd-Breaker leading the remnant out.

Chapter 3: Three escalating indictments to the leadership class: (a) rulers who devour
  the people like meat in a pot (3:1–4); (b) prophets who sell their oracles for food
  (3:5–7), contrasted with Micah's own Spirit-empowerment (3:8); (c) the full corrupt
  establishment resting on false security (3:9–11). Climax: Zion plowed as a field (3:12),
  later quoted verbatim in Jer 26:18 as precedent for Jeremiah's temple sermon.

Chapter 4: Counter-vision of the restored Zion. The "swords into plowshares" passage
  (4:1–4) is nearly identical to Isaiah 2:2–4 — either a common oracle or deliberate
  parallel. The community's covenant declaration (4:5). Lament sections about the present
  crisis (4:9–10, Babylonian exile explicitly anticipated) frame the vision of ultimate
  restoration (4:6–8, 4:11–13).

Chapter 5: The Bethlehem oracle (5:2) — the humblest Judean village will produce the
  ruler whose origins are from of old. NT citation: Matthew 2:6; John 7:42. Followed by
  the remnant's waiting period (5:3), the shepherd-king's global reign (5:4), the Assyrian
  crisis resolved through seven-and-eight commanders (5:5–6), the remnant as dew and lion
  (5:7–8), and the purging of every false military and cultic security (5:10–15).

Chapter 6: The covenant-lawsuit (rib) genre: mountains and foundations of the earth
  summoned as ancient witnesses. The LORD presents his covenant case — Exodus, redemption,
  Moses-Aaron-Miriam, Balak/Balaam (6:3–5). The worshipper's anxious escalation of
  sacrifices (6:6–7) is deflected. The counter-demand (6:8) stands alone. Then God's
  prosecutorial response: commercial fraud (6:9–12), agricultural curse (6:14–15),
  the Omri-Ahab indictment (6:16).

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention).
  T: "Yahweh" in theophany contexts (1:3), oracle introductions of covenantal/eschatological
  weight (4:2, 6:1–5), and direct divine speech; "the LORD" in lighter narrative and
  liturgical formula references. Following Amos/Hosea/Joel conventions.

- H136 (אֲדֹנָי) + compound at 1:2: H136 + H3069 (the ketiv YHWH used with Adonai) =
  L/M "the Lord GOD"; T "the Sovereign LORD." Single H136 = "the Lord."

- H7307 (רוּחַ / ruah):
  At 2:7: "the Spirit of the LORD" (capital) — the prophetic Spirit driving the divine word.
  At 2:11: "spirit of wind and falsehood" (lowercase) — false prophetic disposition.
  At 3:8: "the Spirit of the LORD" (capital) — Micah's own prophetic empowerment.

- H4941 (מִשְׁפָּט / mishpat): "justice" in all tiers throughout. Central at 3:1, 3:8–9, 6:8.

- H2617 (חֶסֶד / hesed) at 6:8:
  L: "steadfast love" (standard covenant register).
  M: "covenant faithfulness" (makes the relational-legal sense explicit).
  T: "covenant love" (combines binding obligation and tender loyalty).
  Hesed is willed covenantal loyalty with active kindness; no English word covers it fully.

- H5315 (נֶפֶשׁ / nefesh) at 6:7: L: "soul"; M/T: "life" — embodied self, not Greek
  immaterial soul. "The fruit of my body for the sin of my life" is the correct register.

- Covenant lawsuit (rib) genre at 6:1–8: T tier names the genre and surfaces the
  mountains-as-ancient-witnesses motif from ANE treaty structure.

- H5769 (עוֹלָם / olam) at 5:2: "from of old, from ancient days" (L); "from ancient times"
  (M); T: "before memory's beginning" — avoids asserting explicit eternal pre-existence
  while honouring the messianic weight and antiquity claim.

- Micah 4:1–4 / Isaiah 2:2–4 parallel: The texts are nearly verbatim. T notes the shared
  tradition at 4:1. No textual-critical adjustment needed — both are canonical.

- Micah 3:12 echo in Jeremiah 26:18: T notes the later citation.

- Hebrew aspect: Prophetic perfects in judgment oracles rendered as future indicatives
  ("I will make," "I will pour down"). Hoy (הוֹי) at 2:1 rendered "Woe" in all tiers.

- Poetic structure: T uses line breaks for the theophany (1:3–4), the lament (1:8–16
  key verses), the woe oracle (2:1–3), the cannibalism metaphor (3:2–3), the restored-Zion
  vision (4:1–5), the Bethlehem oracle (5:2–4), and the rib passage (6:1–8). M is prose.
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

MICAH = {
  "1": {
    "1": {
      "L": "The word of the LORD that came to Micah the Morasthite in the days of Jotham, Ahaz, and Hezekiah, kings of Judah, which he saw concerning Samaria and Jerusalem.",
      "M": "The word of the LORD that came to Micah the Morasthite in the days of Jotham, Ahaz, and Hezekiah, kings of Judah — what he saw concerning Samaria and Jerusalem.",
      "T": "Micah of Moresheth received the LORD's word in the reigns of Jotham, Ahaz, and Hezekiah over Judah — a vision whose targets were Samaria and Jerusalem."
    },
    "2": {
      "L": "Hear, all you peoples; give heed, O earth and all that fills it; and let the Lord GOD be a witness against you, the Lord from his holy temple.",
      "M": "Hear, all you peoples; listen, O earth and all that fills it; for the Lord GOD will be a witness against you — the Lord from his holy temple.",
      "T": "Every nation, listen!\nAll the earth and all its fullness — hear the charge!\nThe Sovereign LORD himself is the witness against you,\nthe Lord who speaks from his holy sanctuary."
    },
    "3": {
      "L": "For behold, the LORD is coming out of his place, and will come down and tread upon the high places of the earth.",
      "M": "For behold, the LORD is coming out of his place; he will come down and tread upon the high places of the earth.",
      "T": "Watch — Yahweh is departing from his place!\nHe descends; he treads across the heights of the earth.\nNo mountain is high enough to stop him."
    },
    "4": {
      "L": "The mountains will melt under him, and the valleys will be cleft, as wax before the fire, as waters poured down a steep slope.",
      "M": "The mountains will melt under him and the valleys will be split open, like wax before the fire, like waters rushing down a steep slope.",
      "T": "Mountains dissolve beneath his step;\nvalleys crack open like wax at the flame,\nlike water flung down a cliff face."
    },
    "5": {
      "L": "All this is for the transgression of Jacob and for the sins of the house of Israel. What is the transgression of Jacob? Is it not Samaria? And what are the high places of Judah? Are they not Jerusalem?",
      "M": "All this is because of the transgression of Jacob and the sins of the house of Israel. What is Jacob's transgression? Is it not Samaria? And what are the high places of Judah? Are they not Jerusalem?",
      "T": "All this fury — on account of Jacob's rebellion,\nthe sins of the house of Israel.\nWho is the source of Jacob's rebellion? Samaria.\nWho erected Judah's idolatrous shrines? Jerusalem."
    },
    "6": {
      "L": "Therefore I will make Samaria a heap of ruins in the open field, a place for vineyard plantings; I will pour down her stones into the valley and lay bare her foundations.",
      "M": "Therefore I will make Samaria a ruin heap in the open country, a planting ground for vineyards; I will pour her stones down into the valley and lay bare her foundations.",
      "T": "So Samaria becomes a heap of rubble on an open hillside,\na site cleared for vineyards.\nI will tumble her stones down into the ravine\nand strip her down to bedrock."
    },
    "7": {
      "L": "And all her carved images shall be beaten to pieces, all her prostitution wages shall be burned with fire, and all her idols I will lay desolate; for from the fee of a prostitute she gathered them, and to the fee of a prostitute they shall return.",
      "M": "All her carved images shall be shattered, all her prostitution wages shall be burned with fire, and all her idols I will lay waste; for she gathered them from the fees of prostitution, and to prostitution fees they shall return.",
      "T": "Her idols are smashed, every carved image shattered;\nthe shrine-wages will burn in the fire.\nAll her gods I will ruin.\nShe built her cult from the earnings of harlotry —\nto harlotry's earnings they will return."
    },
    "8": {
      "L": "For this I will lament and wail; I will go stripped and naked; I will make lamentation like the jackals, and mourning like the ostriches.",
      "M": "For this I will wail and lament; I will go stripped and naked; I will howl like a jackal and mourn like an ostrich.",
      "T": "So I am left to wail and howl,\nto walk stripped bare and naked.\nI cry like a jackal;\nI mourn like an owl in the desert night."
    },
    "9": {
      "L": "For her wound is incurable; it has come to Judah; it has reached to the gate of my people, to Jerusalem.",
      "M": "For her wound is incurable; it has come to Judah; it has reached even to the gate of my people, to Jerusalem.",
      "T": "The wound is past healing.\nIt has crossed the border into Judah;\nit has knocked at the gate of my own city — Jerusalem itself."
    },
    "10": {
      "L": "Tell it not in Gath; weep not at all; in Beth-le-aphrah roll yourself in the dust.",
      "M": "Declare it not in Gath; weep not at all; in Beth-le-aphrah roll yourself in the dust.",
      "T": "Say nothing in Gath — do not give Philistia the news.\nWeep instead, but silently.\nIn Dust-town — Beth-le-aphrah — roll in the dust of mourning."
    },
    "11": {
      "L": "Pass on, inhabitants of Shaphir, in nakedness and shame; the inhabitants of Zaanan do not come out; the lamentation of Beth-ezel shall take away from you its standing.",
      "M": "Pass on in nakedness and shame, inhabitants of Shaphir; the inhabitants of Zaanan do not come out; Beth-ezel mourns — it can no longer support you.",
      "T": "Fairtown — Shaphir — march into exile, naked and ashamed.\nExodus-town — Zaanan — cannot march out to help.\nBeth-ezel is in ruins: the place you leaned on has no ground left to stand on."
    },
    "12": {
      "L": "For the inhabitants of Maroth writhe anxiously for good, because disaster has come down from the LORD to the gate of Jerusalem.",
      "M": "For the inhabitants of Maroth wait anxiously for good news, because disaster has come down from the LORD to the gate of Jerusalem.",
      "T": "Bitterness-town — Maroth — waits and hopes for good news.\nNone comes: Yahweh himself has sent the disaster\nall the way to Jerusalem's gate."
    },
    "13": {
      "L": "Harness the chariot to the swift steeds, O inhabitants of Lachish — it was the beginning of sin to the daughter of Zion, for in you were found the transgressions of Israel.",
      "M": "Harness swift steeds to the chariot, O inhabitants of Lachish — you were the beginning of sin for the daughter of Zion, for in you the transgressions of Israel were found.",
      "T": "Harness the horses, Lachish — your war chariots will not save you!\nYou were the first to import Israel's sin into Judah,\nthe gateway through which the northern rebellion entered Zion."
    },
    "14": {
      "L": "Therefore you shall give parting gifts to Moresheth-gath; the houses of Achzib shall be a deceitful thing to the kings of Israel.",
      "M": "Therefore you shall give parting gifts to Moresheth-gath; the houses of Achzib shall be a deception to the kings of Israel.",
      "T": "So bid farewell with parting gifts to Moresheth-gath —\nyou are losing her forever.\nAnd Achzib? Its name means Deception:\nthat is all the kings of Israel will get from it."
    },
    "15": {
      "L": "I will again bring a conqueror against you, O inhabitants of Mareshah; the glory of Israel shall come to Adullam.",
      "M": "I will again bring a conqueror against you, inhabitants of Mareshah; the glory of Israel shall come to Adullam.",
      "T": "Mareshah — Heir-town — gets a foreign heir:\na conqueror is coming to possess you.\nThe glory of Israel will find its refuge\nin the cave of Adullam — a fugitive king once more."
    },
    "16": {
      "L": "Make yourself bald and shave for the children of your delight; make your baldness as wide as the eagle's, for they have gone from you into exile.",
      "M": "Shave your head and make yourself bald for your precious children; make your baldness as wide as the eagle's, for they have gone from you into exile.",
      "T": "Shave your head — shave it bare — and weep for your beloved children.\nMake your baldness as broad as the vulture's bald crown;\nfor they are taken from you, carried off into exile."
    }
  },
  "2": {
    "1": {
      "L": "Woe to those who devise iniquity and work evil on their beds; in the light of morning they perform it, because it is in the power of their hands.",
      "M": "Woe to those who plan iniquity and work evil on their beds; at the dawn of morning they carry it out, because it is within their power.",
      "T": "Woe to those who lie awake at night scheming evil,\nplotting injustice when they should be sleeping.\nAt sunrise they act — because they have the power to."
    },
    "2": {
      "L": "They covet fields and seize them, and houses, and take them away; they oppress a man and his household, a man and his inheritance.",
      "M": "They covet fields and seize them, and houses, and take them; they oppress a man and his house, a man and his inheritance.",
      "T": "They see a field and they want it — so they take it.\nThey see a house and they want it — so they grab it.\nThey crush a man, strip away his household,\nrob him of the land his fathers left him."
    },
    "3": {
      "L": "Therefore thus says the LORD: Behold, I am devising disaster against this family, from which you cannot remove your necks; and you shall not walk haughtily, for it will be an evil time.",
      "M": "Therefore thus says the LORD: I am devising disaster against this family, from which you cannot free your necks; and you shall not walk haughtily, for the time will be evil.",
      "T": "Therefore the LORD has this to say:\nI too am plotting — plotting disaster for this family.\nYou will not pull your necks out of that yoke.\nNo more walking about with heads held high —\nthis is going to be a time of catastrophe."
    },
    "4": {
      "L": "In that day they shall take up a taunt against you and lament with a bitter lamentation, and say, 'We are utterly ruined; he changes the portion of my people; how he removes it from me — to the rebellious he divides our fields.'",
      "M": "In that day a taunt shall be raised against you, and a bitter lamentation shall be chanted, saying, 'We are utterly ruined; the portion of my people is exchanged; how it is removed from me! To the faithless he apportions our fields.'",
      "T": "When that day comes, a mocking dirge will be sung against you —\na bitter requiem:\n'We are finished — ruined to the last!\nOur land has been handed to strangers;\nwhat was ours has been stripped away.\nOur fields are divided out to our conquerors.'"
    },
    "5": {
      "L": "Therefore you shall have no one to cast the measuring line by lot in the assembly of the LORD.",
      "M": "Therefore you shall have no one to cast the lot in the assembly of the LORD.",
      "T": "Because of this, not one of you will stand in the LORD's assembly\nto cast the lot for the land.\nThe inheritance is forfeited."
    },
    "6": {
      "L": "'Do not preach' — thus they preach — 'one should not preach these things; disgrace will not overtake us.'",
      "M": "'Stop preaching!' — so they preach — 'you should not preach about these things; disgrace will not come upon us.'",
      "T": "'Shut up!' they say — they the preachers!\n'Don't prophesy like this; don't bring such shame on us!'\nBut disgrace is already on its way."
    },
    "7": {
      "L": "Should this be said, O house of Jacob? Is the Spirit of the LORD impatient? Are these his deeds? Do not my words do good to him who walks uprightly?",
      "M": "Is this to be said, O house of Jacob? Is the Spirit of the LORD cut short? Are these his deeds? Do not my words do good to him who walks uprightly?",
      "T": "People of Jacob, is this the right question to be asking?\nIs the Spirit of the LORD limited or impatient?\nWould God actually do such things?\nOnly ask whether you are walking uprightly —\nbecause my words do good to those who are."
    },
    "8": {
      "L": "But lately my people have risen up as an enemy; you strip the robe from the peaceful, from those who pass by trustingly with no thought of war.",
      "M": "But recently my people have risen up as an enemy; you strip the cloak from those who pass by unsuspecting, men returning from war, wanting only peace.",
      "T": "But my own people have turned predator:\nyou strip the cloaks off travelers who pass in good faith —\nmen coming home from battle, wanting nothing but peace —\nand you ambush them."
    },
    "9": {
      "L": "The women of my people you drive out from their pleasant houses; from their young children you take away my glory forever.",
      "M": "The women of my people you drive out from their pleasant houses; from their young children you take away my blessing forever.",
      "T": "You evict widows from the homes they love.\nYou rob their children of everything I intended for them —\nnot just property, but dignity, inheritance, a future."
    },
    "10": {
      "L": "Arise and go, for this is not your resting place, because of uncleanness that destroys with a grievous destruction.",
      "M": "Arise and depart, for this is not your place of rest, because of its uncleanness that destroys with a painful destruction.",
      "T": "Get up and go — this land will not be your resting place.\nYou have fouled it with corruption;\nnow it will destroy you: a ruin that cannot be escaped."
    },
    "11": {
      "L": "If a man walking in a spirit of wind and falsehood should lie, saying, 'I will preach to you of wine and strong drink,' he would be the preacher for this people.",
      "M": "If someone walks in a spirit of wind and deceit, lying and saying, 'I will preach to you of wine and strong drink,' that person would be the prophet for this people!",
      "T": "The only prophet this people wants\nis one who lies with breath and bluster and says:\n'Wine! Strong drink! That is what I see in your future!'\nThat kind of prophet they will follow."
    },
    "12": {
      "L": "I will surely gather all of you, O Jacob; I will surely assemble the remnant of Israel; I will set them together like sheep in a fold, like a flock in its pasture, and it will be noisy with people.",
      "M": "I will surely gather all of you, O Jacob; I will surely assemble the remnant of Israel; I will set them together like sheep in a fold, like a flock in its pasture, and it will be noisy with people.",
      "T": "But I will gather you, Jacob — every last one.\nI will bring the remnant of Israel home,\nset them like sheep in a pen,\nlike a flock in the middle of good pasture.\nThe noise of many people — coming home."
    },
    "13": {
      "L": "The one who breaks open goes up before them; they break through, they pass through the gate, and go out by it; their king passes on before them, the LORD at their head.",
      "M": "The one who breaks through goes up before them; they break out, pass through the gate, and go out by it; their king goes on before them, the LORD at their head.",
      "T": "The Breaker goes ahead of them —\nhe smashes a path through the gate.\nThey pour through it, streaming into the open.\nTheir king at the front; Yahweh himself leading the way."
    }
  },
  "3": {
    "1": {
      "L": "And I said: Hear, O heads of Jacob and rulers of the house of Israel! Is it not for you to know justice?",
      "M": "And I said: Hear, O heads of Jacob and rulers of the house of Israel! Is it not for you to know justice?",
      "T": "Then I said:\nListen, you leaders of Jacob,\nyou rulers who govern the house of Israel —\nis it not your whole charge to know what justice is?"
    },
    "2": {
      "L": "You who hate the good and love the evil, who tear the skin from off my people and the flesh from off their bones —",
      "M": "you who hate what is good and love what is evil, who tear the skin from my people and the flesh from their bones —",
      "T": "You who despise good and embrace evil —\nwho skin my people alive,\nwho strip the flesh from their bones —"
    },
    "3": {
      "L": "who also eat the flesh of my people, and flay their skin from off them, and break their bones in pieces, and chop them up as for the pot, and as meat in the midst of a caldron.",
      "M": "who eat the flesh of my people, and strip their skin from them, and break their bones in pieces, and chop them up like meat in a pot, like flesh in a caldron.",
      "T": "who devour my people's flesh,\ntear off their skin,\ncrack their bones,\nchop them into pieces for the cooking pot,\nlike chunks of meat in a boiling cauldron."
    },
    "4": {
      "L": "Then they will cry to the LORD, but he will not answer them; he will hide his face from them at that time, as they have made their deeds evil.",
      "M": "Then they will cry out to the LORD, but he will not answer them; he will hide his face from them at that time, because their deeds have been evil.",
      "T": "When judgment falls, they will cry out to the LORD —\nand he will not answer.\nHe will hide his face from them then,\nbecause of the evil they have practised."
    },
    "5": {
      "L": "Thus says the LORD concerning the prophets who lead my people astray, who cry 'Peace' when they have something to eat, but declare war against the one who puts nothing in their mouths —",
      "M": "Thus says the LORD concerning the prophets who lead my people astray, who cry 'Peace' when they have something to eat, but declare war against the one who gives them nothing to eat —",
      "T": "This is what the LORD says against the prophets\nwho mislead my people:\nif you feed them, they cry 'All is well!'\nIf you do not, they call down war against you.\nThey sell their oracles for a meal."
    },
    "6": {
      "L": "Therefore it shall be night to you, without vision, and darkness to you, without divination; the sun shall go down upon the prophets, and the day shall be dark over them.",
      "M": "Therefore it shall be night for you, with no vision, and darkness for you, with no divination; the sun shall set over the prophets, and the day shall go dark over them.",
      "T": "So your light goes out —\nno more visions, no more dreams.\nDarkness for the seers;\nthe sun sets at noon for the prophets,\nand the day turns black."
    },
    "7": {
      "L": "The seers shall be put to shame, and the diviners confounded; they shall all cover their lips, for there is no answer from God.",
      "M": "The seers shall be ashamed, and the diviners put to shame; they shall all cover their mouths, for there is no answer from God.",
      "T": "The seers will be shamed.\nThe diviners will cringe.\nEvery last one of them will put their hands over their mouths —\nbecause God will not speak to them."
    },
    "8": {
      "L": "But as for me, I am full of power, with the Spirit of the LORD, and with justice and might, to declare to Jacob his transgression and to Israel his sin.",
      "M": "But as for me, I am filled with power, with the Spirit of the LORD, and with justice and strength, to declare to Jacob his transgression and to Israel his sin.",
      "T": "But I am different:\nfilled with power by the Spirit of the LORD,\nfull of justice and courage —\nto name Jacob's rebellion for what it is\nand tell Israel the truth about its sin."
    },
    "9": {
      "L": "Hear this, you heads of the house of Jacob and rulers of the house of Israel, who detest justice and make crooked all that is straight —",
      "M": "Hear this, you heads of the house of Jacob and rulers of the house of Israel, who despise justice and make crooked all that is straight —",
      "T": "Hear this, rulers of Jacob,\nleaders of Israel:\nyou who detest justice,\nwho twist everything straight into a tangle —"
    },
    "10": {
      "L": "who build Zion with blood and Jerusalem with iniquity.",
      "M": "who build Zion with blood and Jerusalem with wrongdoing.",
      "T": "who erect Zion's walls with the blood of the poor\nand raise Jerusalem's buildings on a foundation of injustice."
    },
    "11": {
      "L": "Her heads give judgment for a bribe; her priests teach for a price; her prophets practice divination for money; yet they lean on the LORD and say, 'Is not the LORD in our midst? Disaster shall not come upon us.'",
      "M": "Her rulers judge for a bribe; her priests teach for payment; her prophets give oracles for money; yet they lean on the LORD and say, 'Is not the LORD among us? Disaster will not come upon us.'",
      "T": "The judges take bribes.\nThe priests sell their rulings.\nThe prophets peddle their visions for a fee —\nand then they all lean on the LORD:\n'God is with us! Nothing bad will happen here!'"
    },
    "12": {
      "L": "Therefore because of you Zion shall be plowed as a field; Jerusalem shall become a heap of ruins, and the mountain of the house like wooded heights.",
      "M": "Therefore because of you Zion shall be plowed as a field; Jerusalem shall become a heap of ruins, and the mountain of the temple a wooded height.",
      "T": "Therefore — because of you —\nZion will be plowed under like a field.\nJerusalem will become a rubble heap.\nThe hill where the temple stands will go back to forest.\n[This oracle was cited verbatim in Jer 26:18 as precedent for Jeremiah's temple sermon.]"
    }
  },
  "4": {
    "1": {
      "L": "But it shall come to pass in the latter days that the mountain of the house of the LORD shall be established at the top of the mountains, and it shall be exalted above the hills; and peoples shall stream to it.",
      "M": "But in the latter days it shall come to pass that the mountain of the house of the LORD shall be established as the highest of the mountains and shall be raised above the hills; and peoples shall stream to it.",
      "T": "But in the days to come\nthe mountain of the LORD's house\nwill stand at the summit of all mountains,\nlifted high above every hill.\nNations will come streaming toward it.\n[This vision is shared almost word-for-word with Isaiah 2:2–4.]"
    },
    "2": {
      "L": "And many nations shall come and say, 'Come, let us go up to the mountain of the LORD and to the house of the God of Jacob, that he may teach us his ways and we may walk in his paths; for from Zion shall go out the law, and the word of the LORD from Jerusalem.'",
      "M": "And many nations shall come and say, 'Come, let us go up to the mountain of the LORD, to the house of the God of Jacob, that he may teach us his ways and we may walk in his paths.' For from Zion shall go forth instruction, and the word of the LORD from Jerusalem.",
      "T": "Many nations will flow in:\n'Come — let us go up to the LORD's mountain,\nto the house of Jacob's God.\nLet him show us how to live;\nlet us walk his road.'\nFor from Zion the Torah goes forth,\nand from Jerusalem comes the word of the LORD."
    },
    "3": {
      "L": "He shall judge between many peoples and decide disputes for strong nations far away; and they shall beat their swords into plowshares, and their spears into pruning hooks; nation shall not lift up sword against nation, neither shall they learn war anymore.",
      "M": "He shall judge between many peoples and decide for strong and distant nations; and they shall beat their swords into plowshares, and their spears into pruning hooks; nation shall not lift up sword against nation, neither shall they learn war anymore.",
      "T": "He will rule between peoples, far and near;\nnations will lay their quarrels before him.\nThen:\nswords beaten into plowshares,\nspears into pruning hooks.\nNation will not draw a sword against nation;\nno one will study war anymore."
    },
    "4": {
      "L": "But they shall sit every man under his vine and under his fig tree, and no one shall make them afraid; for the mouth of the LORD of hosts has spoken.",
      "M": "But they shall sit, each one under his vine and under his fig tree, and no one shall make them afraid, for the mouth of the LORD of hosts has spoken.",
      "T": "And every person will sit\nunder their own vine, their own fig tree,\nwith no one left to threaten them —\nbecause the LORD of hosts has spoken it."
    },
    "5": {
      "L": "For all the peoples walk each in the name of its god, but we will walk in the name of the LORD our God forever and ever.",
      "M": "For all the peoples walk each in the name of its god, but we will walk in the name of the LORD our God forever and ever.",
      "T": "Every nation still follows its own gods —\nbut we will walk in the name of the LORD our God,\nnow and always."
    },
    "6": {
      "L": "In that day, declares the LORD, I will assemble the lame and gather those who have been driven away, and those whom I have afflicted;",
      "M": "In that day, declares the LORD, I will assemble the lame and gather those who have been driven away, and those whom I have afflicted;",
      "T": "In that coming day — Yahweh's own word —\nI will gather the lame,\nI will bring home the scattered,\nall those I struck down in my anger."
    },
    "7": {
      "L": "and the lame I will make a remnant, and those who were cast off, a strong nation; and the LORD will reign over them in Mount Zion from this time forth and forevermore.",
      "M": "and the lame I will make a remnant, and those who were cast off, a strong nation; and the LORD will reign over them in Mount Zion from now on and forevermore.",
      "T": "The lame will become the remnant;\nthe exiles will become a powerful nation.\nThe LORD will be king over them on Mount Zion\nfrom that day forever."
    },
    "8": {
      "L": "And you, O tower of the flock, hill of the daughter of Zion, to you shall it come — the former dominion shall come, the kingdom of the daughter of Jerusalem.",
      "M": "And you, O tower of the flock, hill of the daughter of Zion, to you shall come the former dominion — the kingdom of the daughter of Jerusalem.",
      "T": "And you, watchtower of the flock,\nfortress hill of daughter Zion —\nthe old sovereignty is coming back to you,\nthe kingdom for daughter Jerusalem."
    },
    "9": {
      "L": "Now why do you cry aloud? Is there no king in you? Has your counselor perished, that pain has seized you like a woman in labor?",
      "M": "Now why do you cry aloud? Is there no king in you? Has your counselor perished, that pain has seized you like a woman in labor?",
      "T": "Then why are you crying out now?\nHave you no king? Has your wise counsel collapsed?\nIs that why pain has gripped you like a woman in labor?"
    },
    "10": {
      "L": "Writhe and groan, O daughter of Zion, like a woman in labor, for now you shall go out from the city and dwell in the open country; you shall go even to Babylon; there you shall be rescued; there the LORD will redeem you from the hand of your enemies.",
      "M": "Writhe and groan, O daughter of Zion, like a woman in labor, for now you shall go out from the city and dwell in the open country; you shall go to Babylon. There you shall be rescued; there the LORD will redeem you from the hand of your enemies.",
      "T": "Writhe in your labor pain, daughter Zion —\nyou are going through what a mother goes through.\nYou will leave the city; you will live in the open.\nYou will go all the way to Babylon.\nBut there — there! — Yahweh will rescue you;\nhe will redeem you from your captors' hands."
    },
    "11": {
      "L": "And now many nations have gathered against you, saying, 'Let her be defiled, and let our eyes look in triumph upon Zion.'",
      "M": "Now many nations are assembled against you, saying, 'Let her be defiled, and let our eyes gloat over Zion.'",
      "T": "Now the nations are massing against you,\nsaying: 'Desecrate her!\nLet us enjoy the spectacle of Zion's ruin!'"
    },
    "12": {
      "L": "But they do not know the thoughts of the LORD, and do not understand his plan, that he has gathered them like sheaves to the threshing floor.",
      "M": "But they do not know the thoughts of the LORD; they do not understand his plan, that he has gathered them like sheaves to the threshing floor.",
      "T": "They do not know what the LORD is thinking;\nthey cannot read his counsel.\nHe is gathering them — the way a farmer gathers sheaves —\nstraight to the threshing floor."
    },
    "13": {
      "L": "Arise and thresh, O daughter of Zion; for I will make your horn iron and your hoofs bronze; you shall crush many peoples; and you shall devote their gain to the LORD, and their wealth to the Lord of the whole earth.",
      "M": "Arise and thresh, O daughter of Zion; for I will make your horn iron and your hoofs bronze; you shall beat in pieces many peoples; and you shall devote their gain to the LORD, and their wealth to the Lord of the whole earth.",
      "T": "Rise up, daughter Zion — thresh them!\nI am making your horns iron,\nyour hooves bronze.\nYou will pulverize many nations.\nTheir wealth is consecrated to Yahweh,\ntheir spoil to the Lord of all the earth."
    }
  },
  "5": {
    "1": {
      "L": "Now muster your troops, O daughter of troops; a siege is laid against us; with a rod they strike the judge of Israel on the cheek.",
      "M": "Now muster your troops, O daughter of troops; a siege has been laid against us; with a rod they strike the ruler of Israel on the cheek.",
      "T": "Muster your forces, besieged city!\nThe enemy has surrounded us;\nthey humiliate our ruler —\nstruck on the cheek with a rod."
    },
    "2": {
      "L": "But you, O Bethlehem Ephrathah, too little to be among the clans of Judah, from you shall come forth for me one who is to be ruler in Israel, whose coming forth is from of old, from ancient days.",
      "M": "But you, O Bethlehem Ephrathah, too small to be counted among the clans of Judah — from you shall come forth for me one who is to be ruler in Israel, whose origin is from of old, from ancient days.",
      "T": "But you, Bethlehem Ephrathah —\ntoo small to appear on the clan-list of Judah —\nfrom you will come the one who is to govern Israel for me.\nHis origins reach back before memory's beginning,\nto ages before time."
    },
    "3": {
      "L": "Therefore he shall give them up until the time when she who is in labor has given birth; then the rest of his brothers shall return to the people of Israel.",
      "M": "Therefore he will give them up until the time when she who is in labor gives birth; and the rest of his brothers shall return to the people of Israel.",
      "T": "And so for now he abandons them —\nuntil the birth: until the labor is over.\nThen the exiled brothers will return\nto join the people of Israel."
    },
    "4": {
      "L": "And he shall stand and shepherd his flock in the strength of the LORD, in the majesty of the name of the LORD his God. And they shall dwell secure, for now he shall be great to the ends of the earth.",
      "M": "And he shall stand and shepherd his flock in the strength of the LORD, in the majesty of the name of the LORD his God. And they shall dwell secure, for now he shall be great to the ends of the earth.",
      "T": "He will stand firm and tend his people\nin the strength of the LORD,\nin the authority of the LORD his God's name.\nThey will settle in safety —\nfor his greatness will reach to the ends of the earth."
    },
    "5": {
      "L": "And he shall be their peace. When the Assyrian comes into our land and treads in our palaces, then we will raise against him seven shepherds and eight princes of men.",
      "M": "And this one shall be their peace. When the Assyrian comes into our land and marches through our palaces, we will raise against him seven shepherds and eight human commanders.",
      "T": "This ruler will himself be peace.\nWhen Assyria invades — when they march through our open doors —\nwe will set against them seven shepherds, eight commanders:\nan overwhelming response."
    },
    "6": {
      "L": "They shall shepherd the land of Assyria with the sword, and the land of Nimrod at its entrances; and he shall deliver us from the Assyrian when he comes into our land and when he treads within our border.",
      "M": "They shall rule the land of Assyria with the sword, and the land of Nimrod at its entrances; and he shall deliver us from the Assyrian when he comes into our land and within our borders.",
      "T": "They will take the sword to Assyria itself,\nconquer Nimrod's ancient land from its own gates.\nHe will rescue us from the Assyrian invasion —\nevery foot of ground within our borders."
    },
    "7": {
      "L": "Then the remnant of Jacob shall be in the midst of many peoples, like dew from the LORD, like showers on the grass, which delay not for a man nor wait for the children of man.",
      "M": "Then the remnant of Jacob shall be in the midst of many peoples, like dew from the LORD, like showers on the grass, which do not wait for a man or tarry for the children of man.",
      "T": "The remnant of Jacob scattered among the nations —\nlike dew from the LORD,\nlike sudden showers on the grass:\nunaided by human effort,\ngiven by God alone."
    },
    "8": {
      "L": "And the remnant of Jacob shall be among the nations, in the midst of many peoples, like a lion among the beasts of the forest, like a young lion among flocks of sheep, which, when it passes through, treads down and tears in pieces, and there is none to deliver.",
      "M": "And the remnant of Jacob shall be among the nations, in the midst of many peoples, like a lion among the beasts of the forest, like a young lion among flocks of sheep, which, when it goes through, treads down and tears to pieces, and there is none to rescue.",
      "T": "The remnant of Jacob among the peoples —\nlike a lion in the forest,\nlike a young lion loose among sheep:\nit passes through; it tears; it takes;\nand no one can stop it."
    },
    "9": {
      "L": "Your hand shall be lifted up over your adversaries, and all your enemies shall be cut off.",
      "M": "Your hand shall be lifted up over your adversaries, and all your enemies shall be cut off.",
      "T": "Your hand will be raised against every enemy;\nall who oppose you will be swept away."
    },
    "10": {
      "L": "And it shall come to pass in that day, declares the LORD, that I will cut off your horses from among you and destroy your chariots;",
      "M": "And in that day, declares the LORD, I will cut off your horses from among you and will destroy your chariots;",
      "T": "In that coming day — Yahweh declares —\nI will strip away your warhorses,\nsmash your chariots to pieces."
    },
    "11": {
      "L": "and I will cut off the cities of your land and throw down all your strongholds;",
      "M": "and I will cut off the cities of your land and tear down all your strongholds;",
      "T": "I will demolish your fortified cities,\npull down every stronghold where you felt secure."
    },
    "12": {
      "L": "and I will cut off sorceries from your hand, and you shall have no more diviners;",
      "M": "and I will cut off sorcery from your hand, and you shall have no more fortune-tellers;",
      "T": "I will cut the sorcery from your hands;\nno more oracle-merchants in your land."
    },
    "13": {
      "L": "and I will cut off your carved images and your pillars from among you, and you shall bow down no more to the work of your hands;",
      "M": "and I will cut off your carved images and your stone pillars from among you, and you shall no longer bow down to the work of your own hands;",
      "T": "Your stone idols — I will destroy them;\nyour sacred pillars — I will uproot them.\nYou will never again prostrate yourselves before your own handiwork."
    },
    "14": {
      "L": "and I will uproot your Asherah poles from among you and destroy your cities.",
      "M": "and I will root up your Asherah poles from among you and destroy your cities.",
      "T": "I will tear out your Asherah poles\nand raze your cities to the ground."
    },
    "15": {
      "L": "And in anger and wrath I will execute vengeance upon the nations that did not obey.",
      "M": "And in anger and wrath I will execute vengeance upon the nations that did not obey.",
      "T": "And the nations that refused to listen —\nI will deal with them in fury,\nin the heat of my wrath."
    }
  },
  "6": {
    "1": {
      "L": "Hear now what the LORD says: Arise, plead your case before the mountains, and let the hills hear your voice.",
      "M": "Hear now what the LORD says: Arise, plead your case before the mountains, and let the hills hear your voice.",
      "T": "Listen to what the LORD is saying:\nRise up — bring your case before the mountains.\nLet the hills be your audience."
    },
    "2": {
      "L": "Hear, O mountains, the indictment of the LORD, and you enduring foundations of the earth; for the LORD has an indictment against his people, and he will contend with Israel.",
      "M": "Hear, O mountains, the LORD's indictment, and you enduring foundations of the earth; for the LORD has an indictment against his people, and he will contend with Israel.",
      "T": "Mountains — listen to the LORD's lawsuit;\nyou bedrock foundations of the earth — hear it out.\nYahweh has a legal case against his people;\nhe is taking Israel to court.\n[The rib genre: mountains and earth are ancient covenant witnesses, as in Deut 32:1.]"
    },
    "3": {
      "L": "'O my people, what have I done to you? And in what have I wearied you? Answer me!'",
      "M": "'O my people, what have I done to you? In what have I wearied you? Testify against me!'",
      "T": "'My people — what have I done to you?\nTell me how I have burdened you.\nAnswer me! Make your case.'"
    },
    "4": {
      "L": "'For I brought you up from the land of Egypt and redeemed you from the house of slavery; and I sent before you Moses, Aaron, and Miriam.'",
      "M": "'For I brought you up from the land of Egypt and redeemed you from the house of slavery; and I sent before you Moses, Aaron, and Miriam.'",
      "T": "'I brought you out of Egypt.\nI redeemed you from the slave house.\nI gave you Moses, Aaron, and Miriam to lead the way.'"
    },
    "5": {
      "L": "'O my people, remember what Balak king of Moab devised, and what Balaam the son of Beor answered him; and what happened from Shittim to Gilgal, that you may know the righteous acts of the LORD.'",
      "M": "'O my people, remember what Balak king of Moab devised, and what Balaam the son of Beor answered him, and what happened from Shittim to Gilgal, so that you may know the saving acts of the LORD.'",
      "T": "'Remember Balak's scheme, king of Moab —\nand how Balaam son of Beor answered him.\nRemember the journey from Shittim to Gilgal —\nevery step of it is Yahweh's saving righteousness toward you.'"
    },
    "6": {
      "L": "'With what shall I come before the LORD, and bow myself before God on high? Shall I come before him with burnt offerings, with calves a year old?'",
      "M": "'With what shall I come before the LORD, and bow myself before God on high? Shall I come with burnt offerings, with year-old calves?'",
      "T": "'How can I approach the LORD?\nHow do I bow before the high God?\nShall I bring burnt offerings?\nYear-old calves? Is that the price?'"
    },
    "7": {
      "L": "'Will the LORD be pleased with thousands of rams, with ten thousands of rivers of oil? Shall I give my firstborn for my transgression, the fruit of my body for the sin of my soul?'",
      "M": "'Will the LORD be pleased with thousands of rams, with ten thousand streams of oil? Shall I give my firstborn for my transgression, the fruit of my body for the sin of my life?'",
      "T": "'Thousands of rams — ten thousand streams of olive oil —\nwould that be enough?\nShall I give my own child,\nmy firstborn, for my crimes?\nThe fruit of my own body for the sins of my life?'"
    },
    "8": {
      "L": "He has shown you, O man, what is good; and what does the LORD require of you but to do justice, and to love steadfast love, and to walk humbly with your God?",
      "M": "He has shown you, O man, what is good; and what does the LORD require of you but to do justice, and to love covenant faithfulness, and to walk humbly with your God?",
      "T": "The answer has already been given, O mortal:\nyou know what is good.\nThis is all the LORD asks of you:\ndo justice;\ncherish covenant love;\nwalk humbly at your God's side."
    },
    "9": {
      "L": "The voice of the LORD cries to the city, and it is wisdom to fear your name: 'Hear, O tribe and assembly of the city!'",
      "M": "The voice of the LORD cries to the city — it is wise to fear your name — 'Hear, O tribe! Who appointed the rod?'",
      "T": "The LORD's voice calls to the city.\nWisdom means fearing that name.\nListen — all you clans, all you citizens:\nwho appointed the rod that is coming?"
    },
    "10": {
      "L": "'Are there yet the treasures of wickedness in the house of the wicked, and the accursed scant measure?'",
      "M": "'Are there yet treasures of wickedness in the house of the wicked, and the short measure that is accursed?'",
      "T": "'The wicked house still packed with ill-gotten wealth;\nthe dishonest measure — cursed, and still in use.'"
    },
    "11": {
      "L": "'Shall I acquit the man with wicked scales and with a bag of deceitful weights?'",
      "M": "'Shall I declare innocent the one who uses wicked scales and a bag of deceitful weights?'",
      "T": "'Can I call that person innocent\nwho cheats with rigged scales\nand a pouch of false weights?'"
    },
    "12": {
      "L": "'Your rich men are full of violence; your inhabitants speak lies, and their tongue is deceitful in their mouth.'",
      "M": "'Your wealthy people are full of violence; your residents speak lies, and their tongues are deceitful in their mouths.'",
      "T": "'Your rich men are saturated with violence;\nyour citizens deal in lies;\nevery word out of their mouths is a fraud.'"
    },
    "13": {
      "L": "'Therefore I strike you with a grievous blow, making you desolate because of your sins.'",
      "M": "'Therefore I am striking you with a grievous blow, devastating you because of your sins.'",
      "T": "'Therefore I am striking you down —\nan incurable blow;\nI am making you waste away\nbecause of what you have done.'"
    },
    "14": {
      "L": "'You shall eat, but not be satisfied, and there shall be emptiness within you; you shall put things away, but not preserve them, and what you preserve I will give to the sword.'",
      "M": "'You shall eat, but not be satisfied, and there shall be hunger within you; you shall put away goods, but not save them, and what you do save I will give to the sword.'",
      "T": "'You will eat — and still be empty.\nYou will store up — and lose it.\nWhatever you manage to hold on to,\nI will hand over to the sword.'"
    },
    "15": {
      "L": "'You shall sow, but not reap; you shall tread olives, but not anoint yourself with oil; you shall tread grapes, but not drink wine.'",
      "M": "'You shall sow, but not reap; you shall press olives, but not anoint yourselves with oil; you shall tread grapes, but not drink the wine.'",
      "T": "'You will plant — but not harvest.\nYou will press the olives — but never rub on the oil.\nYou will crush the grapes — but never taste the wine.'"
    },
    "16": {
      "L": "'For the statutes of Omri are kept, and all the works of the house of Ahab; you walk in their counsels, that I may make you a desolation, and your inhabitants a hissing; so you shall bear the scorn of my people.'",
      "M": "'For the statutes of Omri are kept, and all the practices of the house of Ahab; and you follow their counsel, that I may make you a desolation, and your inhabitants a hissing; so you shall bear the reproach of my people.'",
      "T": "'You are living by Omri's code;\nyou are doing exactly what Ahab's house did;\nyou follow their playbook to the letter.\nSo I will make you a wasteland;\nyour people will be a byword of horror.\nYou will carry the shame of my people on your backs.'"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'micah')
        merge_tier(existing, MICAH, tier_key)
        save(tier_dir, 'micah', existing)
    print('Micah 1–6 written.')

if __name__ == '__main__':
    main()
