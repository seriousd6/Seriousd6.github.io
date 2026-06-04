"""
MKT Isaiah chapters 31–33 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-31-33.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
- H136 (אֲדֹנָי): "Lord" (all tiers) — does not appear prominently in these chapters.
- H6635 (צְבָאוֹת): "of hosts" (all tiers) — 31:4,5.
- H7307 (רוּחַ): Two distinct senses here:
    - 31:3 "not spirit" — the flesh/spirit contrast in the Egyptian horses; lowercase "spirit"
      (this is ontological contrast, not reference to the divine Spirit).
    - 32:2 "from the wind" — literal shelter; lowercase "wind."
    - 32:15 "the Spirit" — uppercase; the divine Spirit poured from on high, the eschatological
      gift that reverses the desolation described in vv.9–14.
- H4941 (מִשְׁפָּט): "judgment" (L) / "justice" (M/T) — consistent with all prior Isaiah scripts.
- H6664 / H6666 (צֶדֶק / צְדָקָה): "righteousness" (all tiers) — 32:1, 32:16, 32:17, 33:5.
- H5081 (נָדִיב): "liberal/noble" (L: "liberal") / "noble" (M/T) — 32:5,8. The term carries
  both the sense of generosity and of noble standing; prior Isaiah scripts use "noble."
- H5036 (נָבָל): "vile person/fool" (L: "vile person") / "fool" (M/T) — 32:5,6. The Hebrew נָבָל
  denotes not merely stupidity but active moral coarseness (cf. Nabal, Ps 14:1).
- H1285 (בְּרִית): "covenant" — 33:8 "he hath broken the covenant"; all tiers. The treacherous
  destroyer (Assyria) violated the terms of a negotiated treaty.
- H691 (אֶרְאֶלָּם): 33:7 "their brave ones/valiant ones" — MT has אֶרְאֶלָּם ("their heroes");
  some read אֲרִיאֵל ("Ariel") but plural suffix and context favor "their valiant champions."
  L: "their valiant ones"; M/T: "their brave warriors."
- H4853 (מַשָּׂא): Does not appear in these chapters (contrast with 30:6).
- H5315 (נֶפֶשׁ): 32:6 "soul/appetite of the hungry" — rendered "the hungry" in M/T (the
  נֶפֶשׁ here is the craving self; a person starved of food).
- H2617 (חֶסֶד): Does not appear in chs. 31–33.
- Messianic/eschatological register: 32:1–2 is widely read as an ideal-king oracle with
  messianic resonance; T acknowledges this by preserving the forward-looking grammar without
  collapsing it into allegory. 33:17 ("the king in his beauty") is similarly left open in T.
- 31:4–5 paradox: Yahweh as lion (warrior, 31:4) AND as protecting birds (31:5). The same
  divine act of descent is both siege and shelter — this is core Isaianic theology; T holds
  both images.
- 31:8 — "sword not of a man" anticipates the angelic slaughter of 185,000 Assyrians (2 Kgs
  19:35; Isa 37:36). L preserves the legal precision ("not of a man / not of a mortal").
- 32:15 "until" structure: the desolation described in vv.9–14 will last until the Spirit
  transforms it — the longest temporal suspension in this section of Isaiah. T makes the
  "until... then" sequence vivid by separating them with a line break.
- 33:14–16 — The "who may dwell" wisdom question (cf. Ps 15, Ps 24) answered with a character
  description; T renders it with the rhetorical force of a liturgical entrance question.
- 33:22 — The triple "the LORD is our X" formula (judge / lawgiver / king) is one of Isaiah's
  most concentrated theological affirmations; L preserves the anaphora; T gives it its full
  weight with line breaks.
- Poetry/prose structure: Ch. 31 — tightly concentrated woe oracle throughout; T uses line
  breaks for each strophe. Ch. 32 — vv.1–8 eschatological vision (poetic), vv.9–14 prophetic
  address (prose-poetry), vv.15–20 Spirit-renewal oracle (poetic); T uses line breaks for vv.
  1–8 and 15–20. Ch. 33 — complex literary unit: woe oracle (v.1), community prayer (v.2),
  theophany (vv.3–4), hymn (vv.5–6), lament (vv.7–9), divine oracle (vv.10–13), wisdom poem
  (vv.14–16), restoration vision (vv.17–24); T uses line breaks throughout Ch. 33's poetry.
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
            if v not in existing[ch]:
                existing[ch][v] = tiers[tier_key]

ISAIAH = {
  "31": {
    "1": {
      "L": "Woe to those who go down to Egypt for help, and rely on horses; who trust in chariots because they are many, and in horsemen because they are very strong; but who look not to the Holy One of Israel, neither seek the LORD!",
      "M": "Woe to those who go down to Egypt for help, relying on horses and trusting in chariots because there are so many and in cavalry because it is so strong — but who do not look to the Holy One of Israel or seek the LORD!",
      "T": "Woe to those who go down to Egypt for help,\nstaking everything on horses,\ntrusting in chariots because there are so many\nand in cavalry because it is so strong —\nbut not looking to the Holy One of Israel,\nnot seeking Yahweh."
    },
    "2": {
      "L": "Yet he also is wise and will bring calamity; he has not called back his words, but will arise against the house of the evildoers, and against the help of those who work iniquity.",
      "M": "Yet he too is wise and brings disaster; he does not take back his word. He will arise against the house of those who do evil and against the help of those who practice wickedness.",
      "T": "But Yahweh too is wise — and he brings disaster.\nHe does not take back his word.\nHe will rise against the household of evildoers\nand against those who support the wicked."
    },
    "3": {
      "L": "Now the Egyptians are men, and not God; and their horses are flesh, and not spirit. And when the LORD shall stretch out his hand, both the helper shall stumble, and the helped shall fall, and they shall all fail together.",
      "M": "The Egyptians are human, not God; their horses are flesh, not spirit. When the LORD stretches out his hand, the helper will stumble and the one being helped will fall, and they will all perish together.",
      "T": "The Egyptians are human — not God;\ntheir horses are flesh — not spirit.\nWhen Yahweh extends his hand,\nboth helper and helped will stumble and fall —\nand all will perish together."
    },
    "4": {
      "L": "For thus saith the LORD unto me: As a lion or a young lion growling over his prey, when a multitude of shepherds is called out against him, is not dismayed at their voice nor abases himself for the noise of them — so shall the LORD of hosts come down to fight upon mount Zion and upon the hill thereof.",
      "M": "For this is what the LORD said to me: As a lion or a young lion growls over its prey, and though a whole company of shepherds is mustered against it, it is not frightened by their shouts or intimidated by the noise — so the LORD of hosts will come down to wage war on Mount Zion and on its hill.",
      "T": "For this is what Yahweh said to me:\nAs a lion, a young lion, crouches growling over its prey\nand a whole pack of shepherds is called out against it —\nunfrightened by their shouts,\nunmoved by all their noise —\nso Yahweh of hosts will come down\nto wage war on Mount Zion and its hill."
    },
    "5": {
      "L": "As birds flying, so will the LORD of hosts defend Jerusalem; defending also he will deliver it; and passing over he will preserve it.",
      "M": "Like birds hovering over their young, so the LORD of hosts will shield Jerusalem; shielding, he will deliver it; passing over, he will rescue it.",
      "T": "Like birds hovering over their nest,\nso Yahweh of hosts will cover Jerusalem —\ncovering, he will deliver it;\npassing over, he will rescue it."
    },
    "6": {
      "L": "Return ye unto him from whom the children of Israel have deeply revolted.",
      "M": "Turn back to him from whom the people of Israel have so deeply defected.",
      "T": "Return — return to the one\nfrom whom the children of Israel have strayed so far."
    },
    "7": {
      "L": "For in that day every man shall cast away his idols of silver, and his idols of gold, which your hands have made for yourselves as a sin.",
      "M": "For in that day every person will throw away the idols of silver and gold that their own hands have made — things that have been their sin.",
      "T": "On that day everyone will throw away\ntheir silver idols and golden images —\nthings their own hands crafted\nthat became their downfall."
    },
    "8": {
      "L": "And the Assyrian shall fall by the sword, not of a man; and the sword, not of a mortal, shall devour him; and he shall flee before the sword, and his young men shall be put to forced labor.",
      "M": "Then the Assyrian will fall by a sword that is not of any man; no human sword will consume him. He will flee from the sword, and his young warriors will be broken into forced labor.",
      "T": "The Assyrian will fall — but not by any human sword.\nNo mortal blade will cut him down.\nHe will flee from before the sword,\nand his young warriors will be taken, made to serve."
    },
    "9": {
      "L": "His rock shall pass away for fear, and his princes shall be dismayed at the ensign, saith the LORD, whose fire is in Zion and whose furnace is in Jerusalem.",
      "M": "His stronghold will crumble in terror, and his commanders will be terrified at the signal standard, declares the LORD, whose fire is in Zion and whose furnace is in Jerusalem.",
      "T": "His stronghold will crumble in terror;\nhis commanders will flee in panic at the sight of Yahweh's battle standard —\ndeclares Yahweh,\nwhose fire burns in Zion,\nwhose furnace blazes in Jerusalem."
    }
  },
  "32": {
    "1": {
      "L": "Behold, a king shall reign in righteousness, and princes shall rule in judgment.",
      "M": "See — a king will reign in righteousness, and his rulers will govern with justice.",
      "T": "Look — a king will reign in righteousness,\nand his rulers will govern with justice."
    },
    "2": {
      "L": "And a man shall be as a hiding place from the wind, and a covert from the tempest; as rivers of water in a dry place, as the shadow of a great rock in a weary land.",
      "M": "Each leader will be like a hiding place from the wind, a shelter from the storm — like streams of water in a dry land, like the shade of a great rock in a parched and weary ground.",
      "T": "Each one of them will be a shelter from the wind,\na refuge from the storm —\nlike streams of water in the desert,\nlike the cool shadow of a great rock\nin a scorching, exhausted land."
    },
    "3": {
      "L": "And the eyes of them that see shall not be dim, and the ears of them that hear shall hearken.",
      "M": "Then the eyes of those who see will no longer be closed, and the ears of those who hear will be attentive.",
      "T": "Eyes that can see will no longer be shut;\nears that can hear will actually listen."
    },
    "4": {
      "L": "The heart also of the rash shall understand knowledge, and the tongue of stammerers shall be ready to speak plainly.",
      "M": "The heart of the impulsive will understand and know, and the tongue of those who stumbled over words will speak with clarity.",
      "T": "The heart of the reckless will understand at last,\nand tongues that once stumbled and stammered\nwill speak with clarity."
    },
    "5": {
      "L": "The vile person shall no more be called liberal, nor the churl said to be bountiful.",
      "M": "No longer will the fool be called noble, nor the miser praised as generous.",
      "T": "The fool will no longer be called noble;\nthe miser will no longer be praised as generous."
    },
    "6": {
      "L": "For the vile person will speak villany, and his heart will work iniquity, to practise hypocrisy, and to utter error against the LORD, to make empty the soul of the hungry, and to cause the drink of the thirsty to fail.",
      "M": "For the fool speaks foolishness, and his heart devises wickedness — practicing godlessness and speaking distortion about the LORD, leaving the hungry without food and cutting off drink from the thirsty.",
      "T": "For the fool speaks foolishness;\nhis heart brews nothing but wickedness —\npracticing profanity and preaching distortion about Yahweh,\nleaving the hungry with empty hands,\ndenying water to those who are parched."
    },
    "7": {
      "L": "The instruments of the churl also are evil: he deviseth wicked devices to destroy the poor with lying words, even when the needy speaketh right.",
      "M": "The miser's schemes are all evil; he devises wicked plans to ruin the poor with false words, even when the needy speak the truth.",
      "T": "The miser's tools are all evil —\nhe schemes with wicked designs\nto ruin the poor with lies,\neven when the needy speaks justly."
    },
    "8": {
      "L": "But the liberal man deviseth liberal things; and by liberal things shall he stand.",
      "M": "But the noble person plans noble things, and by noble deeds he stands firm.",
      "T": "But the one with a generous heart devises generous acts —\nand by those generous acts he stands."
    },
    "9": {
      "L": "Rise up, ye women that are at ease; hear my voice, ye careless daughters; give ear unto my speech.",
      "M": "Rise up, you women who are at ease; hear my voice. Give attention to what I say, you complacent daughters.",
      "T": "Rise up, you women who are at ease —\nlisten to my voice;\nyou complacent daughters, pay attention to what I am saying."
    },
    "10": {
      "L": "Many days and years shall ye be troubled, ye careless women: for the vintage shall fail, the gathering shall not come.",
      "M": "In little more than a year you complacent women will tremble, for the grape harvest will fail and the gathering will not come.",
      "T": "Within a year and a little more,\nyou who are so complacent will shudder —\nfor the grape harvest will fail\nand the gathering will not come."
    },
    "11": {
      "L": "Tremble, ye women that are at ease; be troubled, ye careless ones: strip you, and make you bare, and gird sackcloth upon your loins.",
      "M": "Tremble, you women who are at ease; shudder, you who feel secure! Strip off your clothes, bare your body, and tie sackcloth around your waist.",
      "T": "Tremble, you women at ease;\nshudder, you who feel so secure!\nStrip off your fine clothes,\nlay yourselves bare,\nand tie on sackcloth at your waist."
    },
    "12": {
      "L": "They shall lament for the teats, for the pleasant fields, for the fruitful vine.",
      "M": "Beat your breasts in mourning for the pleasant fields and the fruitful vines.",
      "T": "Beat your breasts in mourning\nfor the fertile fields,\nfor the pleasant vineyards,\nfor the fruitful vines."
    },
    "13": {
      "L": "Upon the land of my people shall come up thorns and briers; yea, upon all the houses of joy in the joyous city.",
      "M": "Thorns and briers will spring up on the soil of my people's land, on every house of celebration in the bustling city.",
      "T": "Thorns and briers will overgrow\nmy people's land —\nyes, every house of celebration\nin the city once filled with joy."
    },
    "14": {
      "L": "For the palace shall be forsaken; the multitude of the city shall be left; the forts and towers shall be for dens forever, a joy of wild asses, a pasture of flocks —",
      "M": "For the palace will be abandoned, the busy city deserted; the citadel and the watchtower will serve as lairs for wild donkeys and grazing ground for flocks — forever —",
      "T": "The palace will be abandoned,\nthe crowded city emptied out;\nthe citadel and the watchtower will become\nforever dens for wild donkeys,\npasture for wandering flocks —"
    },
    "15": {
      "L": "until the Spirit be poured upon us from on high, and the wilderness become a fruitful field, and the fruitful field be counted as a forest.",
      "M": "until the Spirit is poured upon us from on high, and the wilderness becomes a fruitful orchard, and what is fruitful orchard is counted as forest.",
      "T": "until the Spirit is poured upon us from on high.\nThen the wilderness will become an orchard,\nand what is now orchard will seem like ancient forest."
    },
    "16": {
      "L": "Then judgment shall dwell in the wilderness, and righteousness remain in the fruitful field.",
      "M": "Then justice will dwell in the wilderness, and righteousness remain in the fruitful orchard.",
      "T": "Then justice will settle in the wilderness,\nand righteousness make its permanent home in the orchard."
    },
    "17": {
      "L": "And the work of righteousness shall be peace; and the effect of righteousness, quietness and assurance for ever.",
      "M": "The fruit of righteousness will be peace, and the result of righteousness will be quietness and confident security forever.",
      "T": "The fruit of righteousness will be peace;\nthe harvest of righteousness —\nquietness and confident security, forever."
    },
    "18": {
      "L": "And my people shall dwell in a peaceable habitation, and in sure dwellings, and in quiet resting places;",
      "M": "My people will dwell in a peaceful home, in secure dwellings, and in undisturbed resting places —",
      "T": "My people will live in peaceful homes,\nin secure dwellings,\nin undisturbed resting places —"
    },
    "19": {
      "L": "when it shall hail, coming down on the forest; and the city shall be laid utterly low.",
      "M": "even when hail comes crashing through the forest and the city is utterly humbled and leveled.",
      "T": "even when hail comes crashing through the forest\nand the city is leveled to the ground."
    },
    "20": {
      "L": "Blessed are ye that sow beside all waters, that send forth thither the feet of the ox and the ass.",
      "M": "Blessed are you who sow beside every stream, who let your oxen and donkeys range freely.",
      "T": "Blessed are you who sow\nbeside every flowing stream —\nwho let the ox and donkey\nrange freely where they will."
    }
  },
  "33": {
    "1": {
      "L": "Woe to thee that spoilest, and thou wast not spoiled; and dealest treacherously, and they dealt not treacherously with thee! When thou shalt cease to spoil, thou shalt be spoiled; and when thou shalt make an end to deal treacherously, they shall deal treacherously with thee.",
      "M": "Woe to you, destroyer who has not been destroyed, betrayer who has not been betrayed! When you finish destroying, you yourself will be destroyed; when you have done with betrayal, you will be betrayed.",
      "T": "Woe to you, destroyer — you who have not yet been destroyed!\nYou who betray — and have not been betrayed!\nWhen you stop destroying, you will be destroyed;\nwhen you finish with betrayal, you will be betrayed."
    },
    "2": {
      "L": "O LORD, be gracious unto us; we have waited for thee: be thou their arm every morning, our salvation also in the time of trouble.",
      "M": "LORD, be gracious to us; we wait for you. Be our arm of strength every morning, our salvation in the time of trouble.",
      "T": "O Yahweh, be gracious to us —\nwe have waited for you.\nBe our arm of strength every morning,\nour salvation in the time of trouble."
    },
    "3": {
      "L": "At the noise of the tumult the peoples fled; at the lifting up of thyself the nations were scattered.",
      "M": "At the uproar of your voice the peoples flee; when you rise up, the nations scatter.",
      "T": "At the thunder of your voice the peoples flee;\nat your rising up the nations scatter."
    },
    "4": {
      "L": "And your spoil shall be gathered as the caterpillar gathereth: as the running to and fro of locusts shall men run upon it.",
      "M": "Your spoil will be gathered as the locust swarm strips a field; like grasshoppers leaping on it, people will rush over it.",
      "T": "Your plunder will be stripped away\nas locusts strip a field —\npeople rushing over it like a swarm of grasshoppers."
    },
    "5": {
      "L": "The LORD is exalted; for he dwelleth on high: he hath filled Zion with judgment and righteousness.",
      "M": "The LORD is exalted, for he dwells on high; he has filled Zion with justice and righteousness.",
      "T": "Yahweh is exalted — he dwells on high;\nhe has filled Zion with justice and righteousness."
    },
    "6": {
      "L": "And the stability of thy times shall be abundance of salvation, wisdom, and knowledge: the fear of the LORD is his treasure.",
      "M": "He will be the stability of your times — an abundance of salvation, wisdom, and knowledge; the fear of the LORD is his treasure.",
      "T": "He will be the steady foundation beneath your days:\nsalvation in abundance, wisdom, and knowledge —\nand the fear of Yahweh is the treasure he offers."
    },
    "7": {
      "L": "Behold, their valiant ones shall cry without; the ambassadors of peace shall weep bitterly.",
      "M": "Look — their brave warriors cry out in the streets; the envoys of peace are weeping bitterly.",
      "T": "Look — their brave warriors\ncry out in the open streets;\nthe peace envoys are weeping bitterly."
    },
    "8": {
      "L": "The highways lie waste, the wayfaring man ceaseth; he hath broken the covenant, he hath despised the cities, he regardeth no man.",
      "M": "The highways are desolate, all travel has ceased; he has broken the covenant, he has despised the cities, he has no regard for human life.",
      "T": "The highways lie empty, all travel stopped.\nHe broke the covenant,\nhe despised the cities,\nhe has no regard for any human life."
    },
    "9": {
      "L": "The earth mourneth and languisheth: Lebanon is ashamed and hewn down: Sharon is like a wilderness; and Bashan and Carmel shake off their leaves.",
      "M": "The earth mourns and fades; Lebanon withers in shame; the Sharon plain is like a desert; Bashan and Carmel are stripping off their leaves.",
      "T": "The earth mourns and fades;\nLebanon is shamed and withers;\nSharon has become a desert;\nBashan and Carmel shake off their leaves."
    },
    "10": {
      "L": "Now will I rise, saith the LORD; now will I be exalted; now will I lift up myself.",
      "M": "'Now I will rise,' declares the LORD; 'now I will be exalted; now I will be lifted up.'",
      "T": "'Now I will rise,' declares Yahweh.\n'Now I will be exalted;\nnow I will be lifted high.'"
    },
    "11": {
      "L": "Ye shall conceive chaff, ye shall bring forth stubble: your breath, as fire, shall devour you.",
      "M": "You conceive chaff; you give birth to stubble; your own breath, like fire, will consume you.",
      "T": "You conceive nothing but chaff;\nyou give birth to stubble —\nyour own breath will be the fire that consumes you."
    },
    "12": {
      "L": "And the peoples shall be as the burnings of lime: as thorns cut up shall they be burned in the fire.",
      "M": "The peoples will be burned like limestone; like cut thornbushes they will be set ablaze in the fire.",
      "T": "The peoples will be burned to lime —\nlike cut thornbushes thrown into the fire."
    },
    "13": {
      "L": "Hear, ye that are far off, what I have done; and, ye that are near, acknowledge my might.",
      "M": "Hear, you who are far away, what I have done; and you who are near, acknowledge my power.",
      "T": "Hear — all you who are far away —\nhear what I have done;\nand you who are near — acknowledge my power."
    },
    "14": {
      "L": "The sinners in Zion are afraid; fearfulness hath surprised the godless: Who among us shall dwell with the devouring fire? who among us shall dwell with everlasting burnings?",
      "M": "The sinners in Zion are terrified; trembling has seized the godless: 'Who among us can live with the devouring fire? Who among us can dwell in perpetual flames?'",
      "T": "The sinners in Zion are terrified;\ntrembling seizes the godless:\n'Who among us can live next to the devouring fire?\nWho among us can survive among everlasting flames?'"
    },
    "15": {
      "L": "He that walketh righteously, and speaketh uprightly; he that despiseth the gain of oppressions, that shaketh his hands from holding of bribes, that stoppeth his ears from hearing of blood, and shutteth his eyes from seeing evil —",
      "M": "The one who walks righteously and speaks honestly, who refuses unjust gain, who shakes his hands free of bribes, who stops his ears from plots of bloodshed, and shuts his eyes from looking on evil —",
      "T": "The one who walks in righteousness\nand speaks honestly,\nwho despises profit squeezed from the poor,\nwho shakes bribe-money from his hands,\nwho stops his ears from hearing of bloodshed,\nwho shuts his eyes rather than gaze on evil —"
    },
    "16": {
      "L": "he shall dwell on high: his place of defence shall be the munitions of rocks: bread shall be given him; his waters shall be sure.",
      "M": "that person will dwell on the heights; his refuge will be a fortress of rocks. His bread will be provided; his water will be reliable.",
      "T": "that one will dwell on the heights;\nhis refuge will be a stronghold of rock.\nHis bread will be given to him;\nhis water will never run dry."
    },
    "17": {
      "L": "Thine eyes shall see the king in his beauty: they shall behold the land that is very far off.",
      "M": "Your eyes will see the king in his beauty; they will look out over a land that stretches far away.",
      "T": "Your eyes will see the king in his beauty —\nyou will look out over a land\nthat stretches far in every direction."
    },
    "18": {
      "L": "Thine heart shall meditate terror: Where is the scribe? where is the receiver? where is he that counted the towers?",
      "M": "Your heart will recall the terror: 'Where is the scribe? Where is the one who tallied the tribute? Where is the one who counted the towers?'",
      "T": "Your heart will look back on the old terror and ask —\n'Where is the scribe now?\nWhere is the one who counted out the tribute?\nWhere is the one who tallied the towers?'"
    },
    "19": {
      "L": "Thou shalt not see that fierce people, a people of a deeper speech than thou canst perceive; of a stammering tongue, that thou canst not understand.",
      "M": "You will no longer see that fierce people — a people of speech too deep to make out, of a strange tongue that you cannot understand.",
      "T": "You will see that brutal people no more —\nthat people with speech too deep to follow,\nwith a strange, garbled tongue\nyou could never understand."
    },
    "20": {
      "L": "Look upon Zion, the city of our solemnities: thine eyes shall see Jerusalem, a quiet habitation, a tabernacle that shall not be taken down; not one of the stakes thereof shall ever be removed, neither shall any of the cords thereof be broken.",
      "M": "Look upon Zion, the city of our appointed festivals! Your eyes will see Jerusalem — a dwelling at peace, a tent that will never be taken down, whose stakes will never be pulled up, and none of whose ropes will ever be broken.",
      "T": "Look upon Zion —\ncity of our sacred assemblies!\nYour eyes will see Jerusalem:\na dwelling at peace,\na tent that will never be taken down,\nwhose stakes will never be pulled up,\nwhose ropes will never snap."
    },
    "21": {
      "L": "But there the glorious LORD will be unto us a place of broad rivers and streams; wherein shall go no galley with oars, neither shall gallant ship pass thereby.",
      "M": "But there the LORD in his glory will be for us a place of broad rivers and streams — where no warship with oars will sail and no mighty vessel will pass through.",
      "T": "But there Yahweh in his glory\nwill be for us a place of wide rivers and flowing streams —\nno warship with oars will sail there,\nno great vessel will pass through."
    },
    "22": {
      "L": "For the LORD is our judge, the LORD is our lawgiver, the LORD is our king; he will save us.",
      "M": "For the LORD is our judge, the LORD is our lawgiver, the LORD is our king — he will save us.",
      "T": "For Yahweh is our judge;\nYahweh is our lawgiver;\nYahweh is our king —\nhe will save us."
    },
    "23": {
      "L": "Thy tacklings are loosed; they could not well strengthen their mast, they could not spread the sail: then is the prey of a great spoil divided; the lame take the prey.",
      "M": "Your rigging hangs slack; the mast cannot be steadied; no sail can be spread. Then a great plunder will be divided — even the lame will carry off their share of the spoil.",
      "T": "Your ship's ropes hang loose —\nthe mast cannot be held upright,\nno sail can be unfurled.\nThen the plunder will be divided,\nand even the lame will take their share of the spoil."
    },
    "24": {
      "L": "And the inhabitant shall not say, I am sick: the people that dwell therein shall be forgiven their iniquity.",
      "M": "And no inhabitant will say, 'I am sick'; the people who dwell there will have their iniquity forgiven.",
      "T": "And no one living there will say, 'I am sick' —\nthe people who dwell in that city\nwill have their iniquity forgiven."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 31–33 written.')

if __name__ == '__main__':
    main()
