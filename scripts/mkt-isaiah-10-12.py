"""
MKT Isaiah chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-10-12.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — consistent with mkt-isaiah-1-2 and 3-6
- H136 (אֲדֹנָי): "Lord" (L/M/T); "Lord GOD" when paired with יהוה (10:23, 10:24)
- H6635 (צְבָאוֹת): "of hosts" throughout — consistent with prior Isaiah scripts
- H6918+H3478 (קְדוֹשׁ יִשְׂרָאֵל): "the Holy One of Israel" — Isaiah's signature epithet
- H7307 (רוּחַ): "Spirit" (capital S, all tiers, 11:2) — here the Spirit explicitly rests on
  the messianic figure; this is divine agency, not the instrumental "spirit of judgment and
  burning" in 4:4 where lowercase was appropriate. The sevenfold Spirit is clearly divine.
- H5342 (נֵצֶר, 11:1): "branch" (L/M) / "Branch" (T) — the messianic growth from Jesse's
  stump; distinct from H6780 צֶמַח used in 4:2. T capitalises to signal messianic weight.
- H2415 (חֹטֶר, 11:1): "shoot" (L/M/T) — the tender green twig alongside the Branch.
- H1503 (גֶּזַע, 11:1): "stump" (L/M/T) — Jesse's dynasty is a felled tree; the new growth
  rises from apparent death. The stump image anticipates 6:13's "holy seed is its stump."
- H410+H1368 (אֵל גִּבּוֹר, 10:21): "the mighty God" (all tiers) — the same divine title as
  9:6 (one of the messianic child's names). The remnant returning to "El Gibbor" echoes the
  earlier promise. T notes this connection explicitly to prevent it being read as mere epithet.
- H3050 (יָהּ, 12:2): The short form of the divine name. Hebrew has יָהּ יְהוָה (Yah, YHWH).
  L = "Yah, the LORD"; M = "the LORD, the LORD himself"; T = "Yah — Yahweh himself." The
  combined form echoes Exodus 15:2 exactly — the new-Exodus theme of chapters 11–12.
- H7605 (שְׁאָר) / H7611 (שְׁאֵרִית): "remnant" consistently (10:20-22, 11:11, 11:16).
- H1945 (הוֹי, 10:1): "Woe" — the prophetic cry of lament/judgment. In 10:5, however, the
  address "Woe, Assyria!" is not an ethical woe against Assyria in the sense of 10:1; it is
  an ironic address to God's instrument. L/M preserve "Woe" in both cases; T 10:5 signals the
  address more clearly.
- H8081 (שֶׁמֶן, 10:27): "oil/anointing/fatness." The clause "the yoke will be destroyed
  because of oil" is textually ambiguous. L renders "because of fatness" (the ox too fat for
  the yoke); M renders "because of the anointing"; T takes the messianic reading: "shattered
  by the anointed one," consistent with the messianic momentum flowing into ch. 11.
- Refrain "his hand is stretched out still" (10:4): This is the fifth and final instance of
  the refrain running through 9:8–10:4. Rendered identically to how the ISA-2a script must
  render 9:12, 9:17, 9:21 for consistency: "his hand is stretched out still."
- Chapter 10 structure: 10:1-4 close the 9:8–10:4 woe cycle; 10:5-19 address Assyria as
  God's instrument and announce its punishment; 10:20-27 promise the remnant's return;
  10:28-32 dramatise the Assyrian advance (staccato march-poem); 10:33-34 announce the
  sudden felling. T preserves poetic line breaks throughout except 10:28-32 where T uses
  terse staccato lines mirroring the march's urgency.
- Chapter 11: Entirely poetry. T uses line breaks throughout. The peaceful-kingdom vision
  (11:6-9) must not be flattened into prose in any tier; L/M may be grammatically flat but
  should not truncate the parallelism.
- Chapter 12: A liturgical song in two stanzas (12:1-3 and 12:4-6). T honours the song
  structure with line breaks. The chapter deliberately echoes the Song of Moses (Exodus 15)
  and should be read as the culmination of the new-Exodus vision that began in 11:15-16.
- OT echo (12:2 / Exodus 15:2): T notes the echo explicitly. Paul quotes 11:10 in Romans 15:12.
- No significant textual-critical issues in these chapters; MT is followed throughout.
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

ISAIAH = {
  "10": {
    "1": {
      "L": "Woe to those who enact iniquitous statutes and to those who record oppressive decrees,",
      "M": "Woe to those who enact unjust laws and to those who issue oppressive rulings,",
      "T": "Woe to those who carve injustice into law,\nwho write exploitation into the statute books,"
    },
    "2": {
      "L": "to turn aside the poor from justice and to rob the right of the afflicted of my people, that widows may be their plunder and orphans their prey.",
      "M": "turning the poor away from justice and robbing the rights of the afflicted of my people, making widows their spoil and orphans their prey.",
      "T": "— laws that deny the poor any recourse,\nthat strip the rights of the afflicted of my people,\nthat leave widows as easy pickings\nand orphans to be plundered."
    },
    "3": {
      "L": "What will you do on the day of visitation, in the desolation that comes from far away? To whom will you flee for help, and where will you leave your glory?",
      "M": "What will you do on the day of reckoning, when devastation sweeps in from afar? To whom will you run for help? Where will you store away your wealth?",
      "T": "And when the day of reckoning finally arrives —\nwhen ruin sweeps in from the far horizon —\nwhere will you run?\nTo whom will you cry out for help?\nWhere will you stash what you have taken?"
    },
    "4": {
      "L": "Nothing remains but to crouch under captives or fall among the slain. For all this his anger has not turned away, and his hand is stretched out still.",
      "M": "There is nothing left but to cower among captives or collapse among the dead. For all this his anger has not turned away, and his hand is stretched out still.",
      "T": "There is nowhere left to go — only to sink down among the prisoners\nor fall among the slain.\nFor all of this, his anger has not turned back;\nhis hand is raised to strike again."
    },
    "5": {
      "L": "Woe, Assyria, the rod of my anger — the staff in their hand is my indignation!",
      "M": "Woe, Assyria — you are the rod of my anger; the club in whose hand is my fury!",
      "T": "Woe, Assyria — you are the rod of my rage,\nthe weapon gripped by a hand that is my own indignation!"
    },
    "6": {
      "L": "Against a godless nation I send him, and against the people of my wrath I charge him, to take plunder and to seize spoil, and to tread them down like mud in the streets.",
      "M": "I am sending him against a godless nation; I am ordering him against the people of my wrath to take spoil and seize plunder and to trample them like mud in the streets.",
      "T": "I have sent him against a people who have forsaken me —\nordered him to raid and ravage, to tread the godless underfoot\nlike mud on a city street."
    },
    "7": {
      "L": "But this is not what he intends, and this is not what his heart plans; for his heart is set to destroy and to cut off many nations.",
      "M": "But that is not his intention, and that is not what his heart plans; for his heart is fixed on destruction, on wiping out many nations.",
      "T": "But Assyria sees none of that. He is no one's errand-boy.\nDestruction is all he has in mind — nation after nation annihilated.\nThat is the whole of his agenda."
    },
    "8": {
      "L": "For he says: 'Are not all my commanders kings?'",
      "M": "For he boasts: 'Are not all my officers kings?'",
      "T": "He boasts: 'Look at my generals — every one of them is as good as a king!'"
    },
    "9": {
      "L": "Is not Calno like Carchemish? Is not Hamath like Arpad? Is not Samaria like Damascus?",
      "M": "Was not Calno taken as easily as Carchemish? Was not Hamath treated like Arpad? Was not Samaria like Damascus?",
      "T": "Calno fell like Carchemish. Hamath like Arpad. Samaria like Damascus.\nThey were all the same to me."
    },
    "10": {
      "L": "As my hand found the kingdoms of the idols — whose carved images exceeded those of Jerusalem and Samaria —",
      "M": "Just as my hand reached kingdoms whose idols surpassed those of Jerusalem and Samaria,",
      "T": "My hand has already taken kingdoms whose idol-images were grander than anything Jerusalem or Samaria ever displayed —"
    },
    "11": {
      "L": "shall I not also do to Jerusalem and her idols as I did to Samaria and her images?",
      "M": "shall I not treat Jerusalem and her idols just as I treated Samaria and her carved images?",
      "T": "— so shall I not do the same to Jerusalem and all the things she worships?"
    },
    "12": {
      "L": "When the Lord has finished all his work on Mount Zion and on Jerusalem, he will punish the fruit of the arrogant heart of the king of Assyria and the glory of his haughty looks.",
      "M": "Once the Lord has completed his work on Mount Zion and in Jerusalem, he will deal with the arrogant boasting of the heart of the king of Assyria and the proud look in his eyes.",
      "T": "When Yahweh has accomplished everything he set out to do on Mount Zion and in Jerusalem, he will turn his attention to the king of Assyria — punishing the pride that drove the instrument, the strutting arrogance blazing in those boastful eyes."
    },
    "13": {
      "L": "'By the strength of my hand I have done this, and by my wisdom, for I have understanding. I have removed the boundaries of peoples and plundered their treasures; like a mighty warrior I have brought down those who sat enthroned.'",
      "M": "'It is by my own power and wisdom that I have done this, for I am shrewd. I have erased the borders of nations and plundered their accumulated wealth; like a conquering champion I have toppled their enthroned rulers.'",
      "T": "'I did this by my own strength, my own genius — no one can question my brilliance.\nI erased their national borders as easily as drawing a line in sand.\nI ransacked their treasuries.\nI toppled enthroned kings like a battering ram breaks a gate.'"
    },
    "14": {
      "L": "My hand has found the wealth of the peoples like a nest, and as one gathers forsaken eggs I have gathered all the earth; and there was none that moved a wing, or opened its mouth, or chirped.",
      "M": "I have scooped up the riches of the peoples as easily as collecting eggs from a deserted nest; there was no wing stirred, no beak opened, no chirp of protest.",
      "T": "'Their wealth? An unguarded nest — I just reached in.\nI swept up the whole earth and no one stirred a wing,\nno one opened a beak,\nnot a sound of resistance.'"
    },
    "15": {
      "L": "Shall the axe boast over him who chops with it, or the saw magnify itself against him who wields it? As if a rod should lift up the one who lifts it, or a staff should lift him who is not wood!",
      "M": "Does an axe boast over the person who wields it? Does a saw exalt itself above the hand that drives it? As if a club could brandish the man who holds it, or a staff lift up a person who is not made of wood!",
      "T": "Does an axe congratulate itself on what the hand achieves?\nDoes the saw credit itself rather than the arm that draws it?\nAs if a stick could wave the one who swings it —\nas if a staff could carry the man!"
    },
    "16": {
      "L": "Therefore the Sovereign, the LORD of hosts, will send a wasting sickness among his stout warriors; under his glory a burning will be kindled like the kindling of fire.",
      "M": "Therefore the Sovereign LORD of hosts will send a wasting disease among the Assyrian's stout warriors; beneath his glory a blaze will be kindled like a consuming fire.",
      "T": "So the Sovereign Lord — Yahweh of hosts — will send a wasting plague\nthrough the ranks of Assyria's finest troops,\nand beneath all that vaunted glory\na fire will ignite and eat its way through."
    },
    "17": {
      "L": "The light of Israel will become a fire, and his Holy One a flame; it will burn and devour his thorns and his briars in one day.",
      "M": "The Light of Israel will become a fire, and his Holy One a flame; it will blaze up and devour his thorns and his briars in a single day.",
      "T": "The Light of Israel will turn into a fire;\nthe Holy One will be a consuming flame —\nand in a single day it will devour every thorn and brier\nthat Assyria has grown."
    },
    "18": {
      "L": "It will consume the glory of his forest and of his fruitful field, both soul and body; and he shall be as when a sick man wastes away.",
      "M": "It will consume the glory of his forest and his fertile fields, root and branch; and he will fade and waste away like a dying man.",
      "T": "Forest and orchard — his proudest glories —\nwill be eaten up entirely, soul and body,\nuntil the whole empire fades like a man dying of fever."
    },
    "19": {
      "L": "And the remaining trees of his forest will be so few in number that a child could write them down.",
      "M": "The trees left standing in his forest will be so few that even a child could count them and write them down.",
      "T": "Whatever trees survive?\nSo few that a child could jot down every last one of them."
    },
    "20": {
      "L": "In that day the remnant of Israel and the survivors of the house of Jacob will no more lean on him who struck them, but will lean on the LORD, the Holy One of Israel, in truth.",
      "M": "In that day the remnant of Israel and the survivors of Jacob's house will no longer rely on the one who struck them, but will truly lean on the LORD, the Holy One of Israel.",
      "T": "In that day the remnant of Israel,\nthe survivors of Jacob's household,\nwill stop leaning on the empire that once struck them.\nThey will lean on Yahweh alone —\nthe Holy One of Israel — and they will mean it."
    },
    "21": {
      "L": "A remnant will return — the remnant of Jacob — to the mighty God.",
      "M": "A remnant will return, the remnant of Jacob, to the mighty God.",
      "T": "A remnant will return — Jacob's remnant —\nback to the Mighty God.\n(El Gibbor: the same divine title given to the promised child in 9:6; the remnant returns to him.)"
    },
    "22": {
      "L": "For though your people Israel are as the sand of the sea, only a remnant of them will return. Destruction is decreed; it overflows with righteousness.",
      "M": "For though your people, Israel, are as numerous as the sand of the sea, only a remnant will return. Destruction has been decreed; it brims over with righteousness.",
      "T": "Your people, Israel, may be as countless as grains of sea-sand —\nbut only a remnant will come back.\nThe destruction that has been decreed will overflow like a flood;\nand it is a flood of righteousness."
    },
    "23": {
      "L": "For the Lord GOD of hosts will carry out a decreed destruction in the midst of all the land.",
      "M": "For the Lord GOD of hosts is executing his decreed destruction throughout the whole land.",
      "T": "The Lord Yahweh of hosts has issued his decree —\na destruction inevitable and complete,\nsweeping through the whole land."
    },
    "24": {
      "L": "Therefore thus says the Lord GOD of hosts: 'O my people who dwell in Zion, do not be afraid of the Assyrian when he strikes you with the rod and lifts his staff against you as Egypt did.'",
      "M": "Therefore this is what the Lord GOD of hosts says: 'O my people who live in Zion, do not be afraid of Assyria, even when he strikes you with his rod and raises his staff against you as Egypt once did.'",
      "T": "So — hear this word from the Lord Yahweh of hosts:\n'My people in Zion, do not be terrorised by Assyria.\nYes, he will strike with his rod, raise his staff against you — exactly as Egypt did.\nDo not be afraid.'"
    },
    "25": {
      "L": "For in a very little while my indignation will come to an end, and my anger will turn to their destruction.",
      "M": "For in a very little while my fury will be spent, and my anger will turn against their destruction.",
      "T": "It will not last long.\nIn a very little while my indignation will exhaust itself —\nand then my anger will wheel around and fall on them."
    },
    "26": {
      "L": "And the LORD of hosts will wield a whip against them as when he struck Midian at the rock of Oreb; and his staff will be over the sea and he will lift it as he did to Egypt.",
      "M": "The LORD of hosts will lash out against them as he defeated Midian at the rock of Oreb; and he will raise his staff over the sea as he raised it against Egypt.",
      "T": "Yahweh of hosts will crack the whip against Assyria —\nthe same decisive blow as at the rock of Oreb when Midian fell.\nHis rod will stretch out over the sea,\nraised again as it was raised against Egypt."
    },
    "27": {
      "L": "And in that day his burden will be removed from your shoulder and his yoke from your neck, and the yoke will be destroyed because of fatness.",
      "M": "In that day his load will be lifted from your shoulder and his yoke from your neck; the yoke will be shattered because of the anointing.",
      "T": "In that day the oppressor's burden will be lifted from your shoulder,\nhis yoke broken from your neck —\nshattered by the anointed one."
    },
    "28": {
      "L": "He has come to Aiath; he has passed through Migron; at Michmash he stores his baggage.",
      "M": "He advances to Aiath, passes through Migron, and stores his equipment at Michmash.",
      "T": "He reaches Aiath. Passes through Migron. Depots his gear at Michmash."
    },
    "29": {
      "L": "They have crossed the pass; at Geba they lodge for the night; Ramah trembles; Gibeah of Saul has fled.",
      "M": "They cross the mountain pass; at Geba they camp for the night; Ramah shakes with fear; Gibeah of Saul has abandoned its position.",
      "T": "The pass is crossed. They bed down at Geba.\nRamah is shaking. Gibeah of Saul — already gone."
    },
    "30": {
      "L": "Cry aloud, O daughter of Gallim! Give ear, O Laishah! Answer her, O Anathoth!",
      "M": "Cry out loudly, O daughter of Gallim! Listen, O Laishah! O Anathoth, answer her!",
      "T": "Gallim's daughter — scream it!\nLaishah, hear it!\nAnathoth, cry back the warning!"
    },
    "31": {
      "L": "Madmenah is in flight; the inhabitants of Gebim gather to flee.",
      "M": "Madmenah has fled; the people of Gebim are running for cover.",
      "T": "Madmenah bolts. Gebim's people scatter for their lives."
    },
    "32": {
      "L": "This very day he will halt at Nob; he will shake his hand against the mount of the daughter of Zion, the hill of Jerusalem.",
      "M": "That same day he will halt at Nob and shake his fist toward the hill of Zion, the mount of Jerusalem.",
      "T": "He stops at Nob — one hill away.\nFrom there he raises his fist against Zion's mountain,\nthe hill of Jerusalem."
    },
    "33": {
      "L": "Behold, the Sovereign, the LORD of hosts, will lop the boughs with terrifying power; the lofty in height will be hewn down, and the high will be brought low.",
      "M": "But see — the Sovereign LORD of hosts is about to lop off the branches with terrifying force; the towering will be cut down and the lofty brought low.",
      "T": "But watch:\nthe Sovereign Lord — Yahweh of hosts —\nwill lop the branches in one terrifying swing.\nEvery towering tree will be hacked down.\nEvery high thing brought to the ground."
    },
    "34": {
      "L": "He will cut down the forest thickets with iron, and Lebanon will fall by the Mighty One.",
      "M": "He will slash down the dense forest with iron, and Lebanon will fall before a powerful one.",
      "T": "The dense thickets of Assyria's pride —\nfelled with iron.\nAnd Lebanon itself will go down before the Mighty One."
    }
  },
  "11": {
    "1": {
      "L": "There shall come forth a shoot from the stump of Jesse, and a branch from his roots shall bear fruit.",
      "M": "A shoot will come up from the stump of Jesse, and a branch from his roots will bear fruit.",
      "T": "From Jesse's felled stump a green shoot will push up;\nfrom his roots a Branch will grow and bear fruit."
    },
    "2": {
      "L": "And the Spirit of the LORD shall rest upon him — the Spirit of wisdom and understanding, the Spirit of counsel and might, the Spirit of knowledge and the fear of the LORD.",
      "M": "The Spirit of the LORD will rest on him — the Spirit of wisdom and understanding, the Spirit of counsel and strength, the Spirit of knowledge and the fear of the LORD.",
      "T": "The Spirit of Yahweh will settle and rest on him:\nthe Spirit of wisdom and understanding,\nthe Spirit of counsel and might,\nthe Spirit of knowledge and the reverent fear of Yahweh."
    },
    "3": {
      "L": "And his delight shall be in the fear of the LORD. He shall not judge by what his eyes see, nor decide disputes by what his ears hear,",
      "M": "He will take delight in the fear of the LORD. He will not judge by what his eyes see or decide cases by what his ears hear,",
      "T": "His greatest delight will be the fear of Yahweh.\nHe will not pronounce judgment based on outward appearances,\nnor settle a case merely by what he is told,"
    },
    "4": {
      "L": "but with righteousness he shall judge the poor, and decide with equity for the meek of the earth; he shall strike the earth with the rod of his mouth, and with the breath of his lips he shall kill the wicked.",
      "M": "but with righteousness he will judge the poor and with fairness he will decide for the humble of the earth; he will strike the earth with the rod of his mouth, and with the breath of his lips he will put the wicked to death.",
      "T": "but he will judge for the poor with full righteousness,\nand for the earth's humble ones with equity that cannot be bought.\nHe will strike the earth with nothing but a spoken word,\nand with a single breath from his lips he will put the wicked to death."
    },
    "5": {
      "L": "Righteousness shall be the belt of his waist, and faithfulness the belt of his loins.",
      "M": "Righteousness will be the belt around his waist, and faithfulness the girdle around his hips.",
      "T": "Righteousness buckled at his waist,\nfaithfulness wrapped close around his hips —\nthese are what he wears."
    },
    "6": {
      "L": "The wolf shall dwell with the lamb, and the leopard shall lie down with the young goat; the calf and the young lion and the fattened calf shall be together, and a little child shall lead them.",
      "M": "The wolf will live peacefully with the lamb, and the leopard will lie down with the young goat; the calf and the young lion and the fatling will be together, and a little child will lead them.",
      "T": "The wolf will live beside the lamb;\nthe leopard will bed down with the young goat;\ncalf and lion cub and fatted beast together —\nand a small child will be their keeper."
    },
    "7": {
      "L": "The cow and the bear shall graze; their young shall lie down together; and the lion shall eat straw like the ox.",
      "M": "The cow and the bear will graze together; their calves will lie down side by side; and the lion will eat straw like the ox.",
      "T": "Cow and bear grazing in the same field;\ntheir calves and cubs sleeping side by side.\nEven the lion will eat straw like an ox."
    },
    "8": {
      "L": "The nursing child shall play over the hole of the asp, and the weaned child shall put his hand on the adder's den.",
      "M": "The nursing infant will play at the viper's burrow, and the toddler will reach his hand into the adder's den.",
      "T": "A nursing baby playing at the cobra's hole;\na weaned toddler reaching into the adder's den —\nand neither will come to harm."
    },
    "9": {
      "L": "They shall not hurt or destroy in all my holy mountain, for the earth shall be full of the knowledge of the LORD as the waters cover the sea.",
      "M": "Nothing will harm or destroy anywhere on my holy mountain, for the earth will be filled with the knowledge of the LORD as completely as the waters cover the sea.",
      "T": "No harm, no destruction on all my holy mountain —\nfor the whole earth will be saturated with the knowledge of Yahweh\nthe way water saturates every last inch of the sea."
    },
    "10": {
      "L": "In that day the root of Jesse, who stands as a signal for the peoples — to him shall the nations seek, and his resting place shall be glorious.",
      "M": "In that day the Root of Jesse will stand as a banner for the peoples; the nations will seek him, and his resting place will be filled with glory.",
      "T": "In that day the Root of Jesse will stand up as a signal-banner for all the peoples;\nthe nations will come seeking him,\nand the place where he dwells will be radiant with glory."
    },
    "11": {
      "L": "In that day the Lord will reach out his hand a second time to recover the remnant of his people who remain — from Assyria, from Egypt, from Pathros, from Cush, from Elam, from Shinar, from Hamath, and from the coastlands of the sea.",
      "M": "In that day the Lord will extend his hand a second time to reclaim the remnant of his people who are left — from Assyria, from Egypt, from Pathros, from Cush, from Elam, from Shinar, from Hamath, and from the islands of the sea.",
      "T": "In that day the Lord will reach out his hand a second time\nto reclaim the scattered remnant of his people —\ngathering them from Assyria and Egypt,\nfrom Pathros, Cush, and Elam,\nfrom Shinar, Hamath, and the far coastlands of the sea."
    },
    "12": {
      "L": "He will raise a signal for the nations and will assemble the dispersed of Israel; he will gather the scattered of Judah from the four corners of the earth.",
      "M": "He will raise a banner for the nations and gather the exiled of Israel; he will assemble the scattered of Judah from the four corners of the earth.",
      "T": "He will hoist his banner before all the nations\nand gather every scattered Israelite;\nhe will assemble Judah's diaspora\nfrom the four corners of the earth."
    },
    "13": {
      "L": "And the jealousy of Ephraim shall depart, and those who harass Judah shall be cut off; Ephraim shall not be jealous of Judah, and Judah shall not harass Ephraim.",
      "M": "Ephraim's jealousy will come to an end, and those who antagonise Judah will be cut off; Ephraim will not envy Judah, and Judah will not vex Ephraim.",
      "T": "The ancient rivalry dissolves:\nEphraim's envy of Judah gone,\nJudah's hostility toward Ephraim finished.\nNeither will taunt the other — the old wound healed at last."
    },
    "14": {
      "L": "But they shall swoop down on the western slope of the Philistines; together they shall plunder the people of the east; they shall lay their hands on Edom and Moab, and the Ammonites shall be subject to them.",
      "M": "Together they will swoop down on the Philistines to the west and jointly plunder the peoples of the east; they will reach out against Edom and Moab, and the Ammonites will submit to them.",
      "T": "United at last, they will sweep down on Philistia to the west,\nplunder the eastern peoples together;\nEdom and Moab will fall under their hand,\nthe Ammonites bowing in submission."
    },
    "15": {
      "L": "And the LORD will utterly destroy the tongue of the Sea of Egypt, and will wave his hand over the River with his scorching wind and strike it into seven channels, so that people may cross in sandals.",
      "M": "The LORD will dry up the gulf of the Egyptian Sea and wave his hand over the Euphrates with his scorching wind, breaking it into seven streams so that men can cross it in sandals.",
      "T": "Yahweh will split the tongue of Egypt's sea\nand fan the Euphrates with his scorching breath —\nbreaking it into seven crossable streams\nthat people will walk through in sandals."
    },
    "16": {
      "L": "And there will be a highway from Assyria for the remnant of his people who remain, just as there was for Israel when they came up from the land of Egypt.",
      "M": "There will be a highway from Assyria for the remnant of his people who survive, just as there was for Israel when they came up out of the land of Egypt.",
      "T": "And there will be a great road from Assyria for his remaining people —\nthe same kind of road that Israel walked\nwhen they came up out of Egypt."
    }
  },
  "12": {
    "1": {
      "L": "And you will say in that day: 'I will give thanks to you, O LORD, for though you were angry with me, your anger turned away and you comforted me.'",
      "M": "In that day you will say: 'I praise you, O LORD; though you were angry with me, your anger has turned and you have comforted me.'",
      "T": "In that day you will say:\n'Yahweh, I give you praise!\nYou were angry with me — truly angry —\nbut your anger has turned,\nand you have become my comfort.'"
    },
    "2": {
      "L": "'Behold, God is my salvation; I will trust and will not be afraid; for Yah, the LORD, is my strength and my song, and he has become my salvation.'",
      "M": "'Look — God is my salvation! I will trust and will not be afraid; for the LORD, the LORD himself, is my strength and my song; he has become my deliverance.'",
      "T": "'Look — God is my salvation!\nI will trust and not be afraid —\nfor Yah, Yahweh himself, is my strength and my song,\nand he is the one who has saved me.'\n(The words deliberately echo Moses's song at the sea: Exodus 15:2. The new exodus of chapters 11–12 culminates in the same confession.)"
    },
    "3": {
      "L": "With joy you will draw water from the wells of salvation.",
      "M": "With joy you will draw water from the springs of salvation.",
      "T": "Come — draw water from the wells of salvation\nwith great joy in every bucket."
    },
    "4": {
      "L": "And you will say in that day: 'Give thanks to the LORD; call upon his name; make known his deeds among the peoples; proclaim that his name is exalted.'",
      "M": "In that day you will also say: 'Give thanks to the LORD; call on his name; make his deeds known among the nations; proclaim that his name is lifted high above all.'",
      "T": "In that day you will call out:\n'Praise Yahweh! Invoke his name!\nBroadcast his deeds among all the nations —\ndeclare that his name towers above everything!'"
    },
    "5": {
      "L": "Sing praises to the LORD, for he has done gloriously; let this be made known in all the earth.",
      "M": "Sing praises to the LORD, for he has done glorious things; make this known throughout all the earth!",
      "T": "Sing to Yahweh — he has done magnificent things!\nMake it ring in every corner of the earth."
    },
    "6": {
      "L": "Cry out and shout for joy, you inhabitants of Zion, for great in your midst is the Holy One of Israel!",
      "M": "Cry aloud and shout for joy, you who dwell in Zion, for great is the Holy One of Israel in your midst!",
      "T": "Shout! Break into singing, you who live in Zion —\nfor the Holy One of Israel stands great in your midst!"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 10–12 written.')

if __name__ == '__main__':
    main()
