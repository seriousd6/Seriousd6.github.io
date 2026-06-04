"""
MKT Isaiah chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-7-9.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from chs 1–6; the divine personal
  name is surfaced in T throughout Isaiah to restore the directness the Tetragrammaton carries.
- H136 (אֲדֹנָי): "Lord" (L/M/T) — the title Adonai; in 7:7, 8:7 paired with יהוה = "Lord GOD";
  in 9:8,17 stands alone as "the Lord" (Adonai). In 7:14 it is אֲדֹנָי not יהוה — "the Lord."
- H6635 (צְבָאוֹת): "of hosts" across all tiers — Isaiah's signature designation for YHWH as
  cosmic sovereign; appears in 8:13,18; 9:7,13,19.
- H5959 (עַלְמָה) in 7:14: rendered "young woman" in all three tiers. The Hebrew means a young
  woman of marriageable age (cf. Gen 24:43, Song 1:3); it does not require virginity. The LXX
  renders it παρθένος (parthenos, virgin) and Matthew 1:23 applies the verse to Mary. The L/M
  tiers follow the Hebrew precisely; T acknowledges the fuller horizon of the name "Immanuel"
  (God-with-us) without inserting later exegesis into the text proper. The decision is
  documented here so readers know it was not accidental.
- H410 (אֵל) in 7:14 as part of Immanuel / 9:6 as "Mighty God": In 7:14 Immanuel = עִמָּנוּ אֵל
  "God with us" — transliterated in all tiers. In 9:6 H1368+H410 (גִּבּוֹר אֵל) = "Mighty God"
  — a divine title applied to the promised child; rendered "Mighty God" across all tiers.
- H6382+H3289 (פֶּלֶא יוֹעֵץ) in 9:6: "Wonderful Counselor" — one compound name, following the
  MT accent (athnach), not two separate titles. L/M/T all render as "Wonderful Counselor."
- H5703+H1 (אֲבִי-עַד) in 9:6: literally "Father of Eternity." L renders literally as
  "Father of Eternity"; M renders idiomatically as "Everlasting Father"; T stays with "Father
  of Eternity" to preserve the strangeness of applying this eternal-fatherhood title to the child.
- H8269+H7965 (שַׂר-שָׁלוֹם) in 9:6: "Prince of Peace" across all tiers — standard and
  appropriate; H7965 (shalom) is peace as comprehensive well-being, not just absence of conflict.
- H7068 (קִנְאָה) in 9:7: "zeal" (L/M/T) — the ardent commitment of YHWH to fulfil the promise;
  "The zeal of the LORD of hosts will accomplish this."
- H4122 (מַהֵר שָׁלָל חָשׁ בַּז) in 8:1,3: Proper name "Maher-shalal-hash-baz" (all tiers);
  T glosses the meaning at 8:3: "Swift-plunder, Quick-prey" — the child-sign of imminent Assyrian
  plunder of Damascus and Samaria.
- H7975 (שִׁלֹחַ) in 8:6: "Shiloah" (L/M) / "Siloam" (T) — the gently flowing channel south
  of Jerusalem; T uses the NT-familiar form to anchor the geography.
- H8451 (תּוֹרָה) in 8:16,20: "instruction/law" (L) / "teaching" (M) / "Torah" (T) — the full
  Mosaic covenant deposit; "seal the Torah" signals Isaiah's intent to preserve the prophetic
  word within the larger covenant charter.
- H8584 (תְּעוּדָה) in 8:16,20: "testimony" (L/M/T).
- H178 (אוֹב) in 8:19: "familiar spirits" (L) / "mediums" (M/T).
- H3049 (יִדְּעֹנִי) in 8:19: "wizards" (L) / "spiritists" (M/T).
- H6757 (צַלְמָוֶת) in 9:2: "shadow of death" (L) / "deep darkness" (M) — the Hebrew
  compound can mean "darkness like death" or "death-shadow"; M follows modern lexical consensus;
  L preserves the more vivid traditional rendering; T uses "death's shadow" for its cadence.
- H4941 (מִשְׁפָּט) in 9:7: "judgment" (L) / "justice" (M/T) — covenantal ordering, consistent
  with chs 1–6.
- H6666 (צְדָקָה) in 9:7: "righteousness" (L/M/T) — consistent with chs 1–6.
- Isaiah 9:3 textual note: MT has לֹא ("not") before הִגְדַּלְתָּ הַשִּׂמְחָה, yielding
  "you have not increased the joy" — but several MSS and the LXX lack the negation. In context
  (the surrounding celebration of light and harvest) the negative reading is anomalous. M/T
  follow the positive reading; L preserves the MT with a note.
- Isaiah 9:20 "flesh of his own arm": zərôʿô can mean "his arm" or "his kinsman"; the image
  is of social disintegration so complete that tribal neighbors cannibalize each other. L renders
  literally; T renders the social sense.
- Poetry: Chapters 7–9 contain both narrative prose (chs 7–8) and high prophetic poetry (9:1-7,
  the woe-cycle refrain 9:8-21). In T, the poetic sections use line breaks; narrative prose does
  not. The four-name list in 9:6 is given one name per line in T.
- Aspect: Prophetic perfects in 9:1-7 (the child has been born, the yoke has been broken) are
  rendered as vivid certainty — these are events as real as past events from the prophetic vantage.
  The waw-consecutive imperfects in the narrative sections (7:1, 8:3) are rendered as narrative past.
- Shear-jashub (7:3): means "a remnant shall return" — a sign embodied in the child's name; not
  translated in the verse text but acknowledged here as part of Isaiah's sign-language to Ahaz.
- The "razor" image (7:20): the king of Assyria as a hired razor is one of Isaiah's most vivid
  metaphors; "beyond the River" = the Euphrates; T makes the instrumentality explicit.
- 8:6-8 structural note: the gentle Shiloah vs. the Euphrates flood creates a deliberate contrast
  between the soft provision of Yahweh and the devastating power he will release through Assyria.
  The climactic "O Immanuel" at the end of 8:8 pivots — the land that Assyria will flood is still
  Immanuel's land; the threat does not cancel the promise.
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
  "7": {
    "1": {
      "L": "And it came to pass in the days of Ahaz the son of Jotham, the son of Uzziah, king of Judah, that Rezin the king of Syria and Pekah the son of Remaliah, king of Israel, went up toward Jerusalem to war against it, but could not prevail against it.",
      "M": "In the days of Ahaz son of Jotham son of Uzziah, king of Judah, Rezin king of Syria and Pekah son of Remaliah king of Israel came up to attack Jerusalem, but they could not conquer it.",
      "T": "In the reign of Ahaz — grandson of Uzziah, king of Judah — Rezin of Syria and Pekah son of Remaliah of Israel marched on Jerusalem to besiege it, but they could not take the city."
    },
    "2": {
      "L": "And it was told the house of David, saying, Syria is confederate with Ephraim. And his heart was moved, and the heart of his people, as the trees of the wood are moved with the wind.",
      "M": "When the house of David was told that Syria had allied with Ephraim, the heart of Ahaz and the hearts of his people shook like the trees of the forest trembling in the wind.",
      "T": "Word reached the royal house: Syria has joined forces with Ephraim. At once Ahaz's heart, and the hearts of all his people, shook like forest trees tossing in the wind."
    },
    "3": {
      "L": "Then said the LORD unto Isaiah, Go forth now to meet Ahaz, thou, and Shearjashub thy son, at the end of the conduit of the upper pool in the highway of the fuller's field.",
      "M": "Then the LORD said to Isaiah, 'Go out now to meet Ahaz, you and your son Shear-jashub, at the end of the conduit of the upper pool, on the road to the Fuller's Field.'",
      "T": "Yahweh said to Isaiah: 'Go meet Ahaz — take your son Shear-jashub with you — at the end of the channel from the upper reservoir, on the Fuller's Field road.'"
    },
    "4": {
      "L": "And say unto him, Take heed, and be quiet; fear not, neither be fainthearted for the two tails of these smoking firebrands, for the fierce anger of Rezin with Syria, and of the son of Remaliah.",
      "M": "Say to him: Be careful, stay calm, and do not be afraid; do not lose heart because of these two smoldering stubs of firewood — the fierce anger of Rezin and Syria and of the son of Remaliah.",
      "T": "'Tell him: Hold steady — calm down and do not be afraid. Do not let these two smoldering stumps frighten you, the spent rage of Rezin and Syria and of Remaliah's son.'"
    },
    "5": {
      "L": "Because Syria, Ephraim, and the son of Remaliah have taken evil counsel against thee, saying,",
      "M": "Because Syria, Ephraim, and the son of Remaliah have devised evil against you, saying,",
      "T": "Syria has conspired with Ephraim and Remaliah's son against you, saying:"
    },
    "6": {
      "L": "Let us go up against Judah, and vex it, and let us make a breach therein for us, and set a king in the midst of it, even the son of Tabeal.",
      "M": "Let us march against Judah, terrify it, breach its walls, and set the son of Tabeal as king over it.",
      "T": "'Let us invade Judah, crack it open, install our puppet — the son of Tabeal — as its king.'"
    },
    "7": {
      "L": "Thus saith the Lord GOD, It shall not stand, neither shall it come to pass.",
      "M": "Thus says the Lord GOD: It will not happen; it will not come to pass.",
      "T": "But the Lord Yahweh says: It will not happen. It will never stand."
    },
    "8": {
      "L": "For the head of Syria is Damascus, and the head of Damascus is Rezin; and within threescore and five years shall Ephraim be broken, that it be not a people.",
      "M": "For the head of Syria is Damascus, and the head of Damascus is Rezin; and within sixty-five years Ephraim will be shattered so that it is no longer a people.",
      "T": "Syria's capital is Damascus; Damascus has only Rezin. And within sixty-five years Ephraim will be so thoroughly broken it will no longer exist as a nation."
    },
    "9": {
      "L": "And the head of Ephraim is Samaria, and the head of Samaria is Remaliah's son. If ye will not believe, surely ye shall not be established.",
      "M": "The head of Ephraim is Samaria, and the head of Samaria is Remaliah's son. If you do not stand firm in faith, you will not stand at all.",
      "T": "Ephraim's capital is Samaria; Samaria has only Remaliah's son. If you will not trust, you cannot last."
    },
    "10": {
      "L": "Moreover the LORD spake again unto Ahaz, saying,",
      "M": "Again the LORD spoke to Ahaz, saying,",
      "T": "Again Yahweh addressed Ahaz:"
    },
    "11": {
      "L": "Ask thee a sign of the LORD thy God; ask it either in the depth, or in the height above.",
      "M": "Ask a sign from the LORD your God; let it be as deep as Sheol or as high as the heavens above.",
      "T": "Ask Yahweh your God for a sign — anything you choose: as deep as the grave below or as high as the heavens above."
    },
    "12": {
      "L": "But Ahaz said, I will not ask, neither will I tempt the LORD.",
      "M": "But Ahaz said, 'I will not ask, and I will not put the LORD to the test.'",
      "T": "Ahaz replied: 'I will not ask. I refuse to test Yahweh.'"
    },
    "13": {
      "L": "And he said, Hear ye now, O house of David; Is it a small thing for you to weary men, but will ye weary my God also?",
      "M": "Then Isaiah said, 'Hear now, O house of David! Is it too small a thing for you to weary men? Must you weary my God as well?'",
      "T": "Isaiah answered: 'Listen to me, house of David. Is it not enough that you exhaust human patience — must you also exhaust the patience of my God?'"
    },
    "14": {
      "L": "Therefore the Lord himself shall give you a sign; Behold, a young woman shall conceive, and bear a son, and shall call his name Immanuel.",
      "M": "Therefore the Lord himself will give you a sign: Behold, the young woman shall conceive and bear a son, and she shall call his name Immanuel.",
      "T": "Therefore the Lord himself will give you a sign: Look — a young woman is with child and will give birth to a son; she will name him Immanuel, God-with-us."
    },
    "15": {
      "L": "Butter and honey shall he eat, that he may know to refuse the evil, and choose the good.",
      "M": "He shall eat curds and honey until he knows how to refuse evil and choose good.",
      "T": "He will live on curds and honey until he is old enough to reject what is evil and choose what is good."
    },
    "16": {
      "L": "For before the child shall know to refuse the evil, and choose the good, the land that thou abhorrest shall be forsaken of both her kings.",
      "M": "For before the child knows how to refuse evil and choose good, the land whose two kings you dread will be forsaken.",
      "T": "Even before this child knows right from wrong, the land of those two kings you fear will be abandoned by both its rulers."
    },
    "17": {
      "L": "The LORD shall bring upon thee, and upon thy people, and upon thy father's house, days that have not come, from the day that Ephraim departed from Judah; even the king of Assyria.",
      "M": "The LORD will bring on you, your people, and your father's house such days as have not come since the day Ephraim departed from Judah — the king of Assyria.",
      "T": "Yahweh will bring on you, your people, and your entire dynasty days unlike any since the day Israel broke away from Judah — he will bring the king of Assyria."
    },
    "18": {
      "L": "And it shall come to pass in that day, that the LORD shall hiss for the fly that is in the uttermost part of the rivers of Egypt, and for the bee that is in the land of Assyria.",
      "M": "In that day the LORD will whistle for the fly from the farthest reaches of the rivers of Egypt, and for the bee from the land of Assyria.",
      "T": "On that day Yahweh will whistle up the flies from Egypt's farthest rivers and summon the bees from Assyria's homeland."
    },
    "19": {
      "L": "And they shall come, and shall rest all of them in the desolate valleys, and in the holes of the rocks, and upon all thorns, and upon all bushes.",
      "M": "They will all come and settle in the steep ravines, in the crevices of the rocks, on all the thornbushes, and on all the pastures.",
      "T": "They will swarm in — covering every rocky gully, every crevice, every thornbush and every open pasture."
    },
    "20": {
      "L": "In the same day shall the Lord shave with a razor that is hired, namely, by them beyond the river, by the king of Assyria, the head, and the hair of the feet: and it shall also consume the beard.",
      "M": "In that day the Lord will shave with a hired razor — with those from beyond the Euphrates, with the king of Assyria — shaving the head, the hair of the legs, and the beard as well.",
      "T": "On that day the Lord will hire Assyria as his razor — those people from beyond the Euphrates — and shave Israel completely bare: head, body hair, and beard all gone."
    },
    "21": {
      "L": "And it shall come to pass in that day, that a man shall nourish a young cow, and two sheep;",
      "M": "In that day a man will keep alive one young cow and two sheep.",
      "T": "That day a man will count himself fortunate to keep one young cow and two sheep."
    },
    "22": {
      "L": "And it shall come to pass, for the abundance of milk that they shall give, he shall eat butter: for butter and honey shall every one eat that is left in the land.",
      "M": "And because of the abundance of milk they produce, he will eat curds; curds and honey will be the diet of everyone left in the land.",
      "T": "Those few animals will give enough milk that everyone remaining in the land will live on curds and honey — the diet of a stripped and emptied country."
    },
    "23": {
      "L": "And it shall come to pass in that day, that every place where there were a thousand vines at a thousand silverlings, it shall even be for briers and thorns.",
      "M": "In that day every place that once held a thousand vines, worth a thousand silver pieces, will become briers and thorns.",
      "T": "On that day every vineyard that once commanded a thousand pieces of silver will be overrun with briers and thorns."
    },
    "24": {
      "L": "With arrows and with bows shall men come thither; because all the land shall become briers and thorns.",
      "M": "Men will come there with bow and arrows, for all the land will be briers and thorns.",
      "T": "Hunters with bows will roam what was once farmland, now given over entirely to briers and thorns."
    },
    "25": {
      "L": "And on all hills that shall be digged with the mattock, there shall not come thither the fear of briers and thorns: but it shall be for the sending forth of oxen, and for the treading of lesser cattle.",
      "M": "But all the hills once cultivated with the hoe — no one will go there for fear of briers and thorns; they will be given over to cattle and trampled by sheep.",
      "T": "Every hillside once broken open with a hoe — no one will enter them for fear of the thorns. Those once-tended slopes will be handed over to cattle and trampled by flocks."
    }
  },
  "8": {
    "1": {
      "L": "Moreover the LORD said unto me, Take thee a great roll, and write in it with a man's pen concerning Mahershalalhashbaz.",
      "M": "Then the LORD said to me, 'Take a large writing tablet and write on it in common script: Maher-shalal-hash-baz.'",
      "T": "Yahweh told me: 'Get a large tablet and inscribe on it in plain letters: Maher-shalal-hash-baz.'"
    },
    "2": {
      "L": "And I took unto me faithful witnesses to record, Uriah the priest, and Zechariah the son of Jeberechiah.",
      "M": "And I called in reliable witnesses, Uriah the priest and Zechariah son of Jeberechiah.",
      "T": "I then summoned two reliable witnesses: Uriah the priest and Zechariah son of Jeberechiah."
    },
    "3": {
      "L": "And I went unto the prophetess; and she conceived, and bare a son. Then said the LORD to me, Call his name Mahershalalhashbaz.",
      "M": "Then I went to the prophetess, and she conceived and bore a son. The LORD said to me, 'Name him Maher-shalal-hash-baz.'",
      "T": "I was intimate with the prophetess; she conceived and bore a son. And Yahweh said: 'Name him Maher-shalal-hash-baz — Swift-plunder, Quick-prey.'"
    },
    "4": {
      "L": "For before the child shall have knowledge to cry, My father, and my mother, the riches of Damascus and the spoil of Samaria shall be taken away before the king of Assyria.",
      "M": "For before the child knows how to say 'My father' or 'My mother,' the wealth of Damascus and the plunder of Samaria will be carried off before the king of Assyria.",
      "T": "Before this child can say 'Daddy' or 'Mama,' the riches of Damascus and the spoil of Samaria will be hauled away by the king of Assyria."
    },
    "5": {
      "L": "The LORD spake also unto me again, saying,",
      "M": "The LORD spoke to me again, saying:",
      "T": "Yahweh continued to speak to me:"
    },
    "6": {
      "L": "Forasmuch as this people refuseth the waters of Shiloah that go softly, and rejoice in Rezin and Remaliah's son;",
      "M": "Because this people has rejected the waters of Shiloah that flow gently, and rejoice over Rezin and the son of Remaliah,",
      "T": "Because this people has spurned the gently flowing waters of Siloam and instead delights in Rezin and Remaliah's son,"
    },
    "7": {
      "L": "Now therefore, behold, the Lord bringeth up upon them the waters of the river, strong and many, even the king of Assyria, and all his glory: and he shall come up over all his channels, and go over all his banks:",
      "M": "therefore, behold, the Lord is bringing up against them the mighty floodwaters of the River — the king of Assyria and all his power. It will rise over all its channels and overflow all its banks,",
      "T": "therefore the Lord is bringing the Euphrates in full flood against them — the king of Assyria with all his might, surging over every channel and overflowing every bank —"
    },
    "8": {
      "L": "And he shall pass through Judah; he shall overflow and go over, he shall reach even to the neck; and the stretching out of his wings shall fill the breadth of thy land, O Immanuel.",
      "M": "sweeping through Judah, overflowing as it goes, reaching even to the neck; and with its outspread wings it will fill the entire breadth of your land, O Immanuel.",
      "T": "sweeping through Judah in a torrent, rising until it reaches the throat, and spreading like a great bird's wings over the whole breadth of your land. Immanuel — this is still your land, God-with-us."
    },
    "9": {
      "L": "Associate yourselves, O ye people, and ye shall be broken in pieces; and give ear, all ye of far countries: gird yourselves, and ye shall be broken in pieces; gird yourselves, and ye shall be broken in pieces.",
      "M": "Band yourselves together, O peoples, and you will be broken in pieces; give ear, all you distant lands: arm yourselves and you will be broken in pieces; arm yourselves and you will be broken in pieces!",
      "T": "Band together, you nations — you will still be shattered!\nRally your distant peoples — arm for war and be crushed!\nGird yourselves again — you will be crushed!"
    },
    "10": {
      "L": "Take counsel together, and it shall come to nought; speak the word, and it shall not stand: for God is with us.",
      "M": "Devise your plans — they will come to nothing; speak your word — it will not stand, for God is with us.",
      "T": "Plot your strategy — it will fall apart.\nIssue your orders — they will never hold.\nFor God is with us — Immanuel."
    },
    "11": {
      "L": "For the LORD spake thus to me with a strong hand, and instructed me that I should not walk in the way of this people, saying,",
      "M": "For the LORD spoke to me with his strong hand upon me, and warned me not to walk in the way of this people, saying:",
      "T": "Yahweh gripped me with his hand and warned me: do not walk the path this people walks. He said:"
    },
    "12": {
      "L": "Say ye not, A confederacy, to all them to whom this people shall say, A confederacy; neither fear ye their fear, nor be afraid.",
      "M": "Do not call a conspiracy everything this people calls a conspiracy; do not fear what they fear, and do not dread it.",
      "T": "Do not cry 'Conspiracy!' every time they do.\nDo not fear what they fear;\ndo not be in dread."
    },
    "13": {
      "L": "Sanctify the LORD of hosts himself; and let him be your fear, and let him be your dread.",
      "M": "But the LORD of hosts — him you shall regard as holy; let him be your fear, and let him be your dread.",
      "T": "Set apart Yahweh of hosts as the one who is holy —\nlet him be your fear,\nlet him be your dread."
    },
    "14": {
      "L": "And he shall be for a sanctuary; but for a stone of stumbling and for a rock of offence to both the houses of Israel, for a gin and for a snare to the inhabitants of Jerusalem.",
      "M": "He will be a sanctuary, but also a stone that people stumble over, a rock that makes them fall — a trap and a snare for both houses of Israel and for the inhabitants of Jerusalem.",
      "T": "He will be a sanctuary for those who trust him — but for both houses of Israel he will be a stone people trip over, a rock they fall against, a trap and a snare for the inhabitants of Jerusalem."
    },
    "15": {
      "L": "And many among them shall stumble, and fall, and be broken, and be snared, and be taken.",
      "M": "And many among them will stumble; they will fall and be broken; they will be snared and captured.",
      "T": "Many will trip on that stone — they will fall and break, be caught and taken."
    },
    "16": {
      "L": "Bind up the testimony, seal the law among my disciples.",
      "M": "Bind up the testimony; seal the teaching among my disciples.",
      "T": "Bind up this testimony;\nseal this Torah among my disciples."
    },
    "17": {
      "L": "And I will wait upon the LORD, that hideth his face from the house of Jacob, and I will look for him.",
      "M": "I will wait for the LORD, who is hiding his face from the house of Jacob, and I will hope in him.",
      "T": "I will wait on Yahweh,\nwho has hidden his face from the house of Jacob.\nI will watch for him."
    },
    "18": {
      "L": "Behold, I and the children whom the LORD hath given me are for signs and for wonders in Israel from the LORD of hosts, which dwelleth in mount Zion.",
      "M": "Here am I, and the children the LORD has given me. We are signs and wonders in Israel from the LORD of hosts who dwells on Mount Zion.",
      "T": "Look: I and the children Yahweh has given me —\nwe are signs and wonders in Israel\nfrom Yahweh of hosts who dwells on Mount Zion."
    },
    "19": {
      "L": "And when they shall say unto you, Seek unto them that have familiar spirits, and unto wizards that peep, and that mutter: should not a people seek unto their God? for the living to the dead?",
      "M": "When people say to you, 'Consult the mediums and the spiritists who whisper and mutter' — should not a people consult their God? Why should the living seek guidance from the dead?",
      "T": "When people tell you: 'Go consult the mediums and spiritists — those who whisper and mutter their dark words' — ask them: Should a people not seek their God? Why would the living turn to the dead?"
    },
    "20": {
      "L": "To the law and to the testimony: if they speak not according to this word, it is because there is no light in them.",
      "M": "To the teaching and to the testimony! If anyone does not speak according to this word, it is because there is no light in them.",
      "T": "Back to the Torah! Back to the testimony!\nAny word that contradicts this has no light in it at all."
    },
    "21": {
      "L": "And they shall pass through it, hardly bestead and hungry: and it shall come to pass, that when they shall be hungry, they shall fret themselves, and curse their king and their God, and look upward.",
      "M": "They will roam through the land, hard-pressed and famished; and when hunger seizes them, they will be enraged and will curse their king and their God, and look upward —",
      "T": "They will wander through the land, exhausted and starving;\nwhen the hunger bites, rage will flare up — they will curse their king, curse their God, and look upward —"
    },
    "22": {
      "L": "And they shall look unto the earth; and behold trouble and darkness, dimness of anguish; and they shall be driven to darkness.",
      "M": "and then look to the earth and see nothing but distress and darkness, the gloom of anguish, and they will be thrust into thick darkness.",
      "T": "and then look to the earth and find nothing but distress, darkness, the gloomy black of anguish — driven at last into an outer dark with no way out."
    }
  },
  "9": {
    "1": {
      "L": "Nevertheless the dimness shall not be such as was in her vexation, when at the first he lightly afflicted the land of Zebulun and the land of Naphtali, and afterward did more grievously afflict her by the way of the sea, beyond Jordan, in Galilee of the nations.",
      "M": "But there will be no more gloom for her who was in anguish. In the former time he humbled the land of Zebulun and the land of Naphtali, but in the latter time he will honor the way of the sea, the land beyond the Jordan, Galilee of the nations.",
      "T": "Yet the darkness that lay on Zebulun and Naphtali will not remain forever. In the first time Yahweh brought shame on those northern lands, but in the latter time he will honor the coastal road, Transjordan, and Galilee — the country of the nations."
    },
    "2": {
      "L": "The people that walked in darkness have seen a great light: they that dwell in the land of the shadow of death, upon them hath the light shined.",
      "M": "The people who walked in darkness have seen a great light; those who lived in a land of deep darkness — on them the light has dawned.",
      "T": "The people who walked in darkness\nhave seen a blazing light;\nthose who lived in the land of death's shadow —\non them the light has broken through."
    },
    "3": {
      "L": "Thou hast multiplied the nation, and not increased the joy: they joy before thee according to the joy in harvest, and as men rejoice when they divide the spoil.",
      "M": "You have multiplied the nation; you have increased its joy; they rejoice before you as with joy at the harvest, as warriors celebrate when they divide the plunder.",
      "T": "You have swelled the nation's numbers and multiplied its joy —\nthey rejoice before you as at harvest time,\nas soldiers celebrate when they divide what they have won."
    },
    "4": {
      "L": "For thou hast broken the yoke of his burden, and the staff of his shoulder, the rod of his oppressor, as in the day of Midian.",
      "M": "For you have broken the yoke of his burden, the staff on his shoulder, the rod of his oppressor, as on the day of Midian.",
      "T": "For you have shattered the yoke that weighed on Israel's shoulder,\nsnapped the staff the oppressor wielded against them,\nas you broke Midian's power on that ancient day."
    },
    "5": {
      "L": "For every battle of the warrior is with confused noise, and garments rolled in blood; but this shall be with burning and fuel of fire.",
      "M": "For every boot of the trampling warrior and every garment soaked in blood will be burned as fuel for the fire.",
      "T": "Every soldier's boot worn in the thunder of battle,\nevery uniform caked in blood —\nall of it will be fuel for the fire,\nburned up and gone."
    },
    "6": {
      "L": "For unto us a child is born, unto us a son is given: and the government shall be upon his shoulder: and his name shall be called Wonderful, Counsellor, The mighty God, The everlasting Father, The Prince of Peace.",
      "M": "For to us a child is born, to us a son is given; and the government will rest on his shoulders. His name will be called: Wonderful Counselor, Mighty God, Father of Eternity, Prince of Peace.",
      "T": "For a child is born to us — a son is given!\nThe government rests on his shoulders.\nHis name is:\nWonderful Counselor,\nMighty God,\nFather of Eternity,\nPrince of Peace."
    },
    "7": {
      "L": "Of the increase of his government and peace there shall be no end, upon the throne of David, and upon his kingdom, to order it, and to establish it with judgment and with justice from henceforth even for ever. The zeal of the LORD of hosts will perform this.",
      "M": "Of the increase of his government and of peace there will be no end, on the throne of David and over his kingdom, to establish it and uphold it with justice and righteousness from this time forth and forevermore. The zeal of the LORD of hosts will accomplish this.",
      "T": "His reign will keep expanding, and peace will never stop —\nseated on the throne of David,\nruling his kingdom, sustaining it,\nupholding it with justice and righteousness\nfrom now and forever.\nThe zeal of Yahweh of hosts will make it so."
    },
    "8": {
      "L": "The Lord sent a word into Jacob, and it hath lighted upon Israel.",
      "M": "The Lord has sent a word against Jacob, and it has fallen upon Israel.",
      "T": "The Lord dispatched a word against Jacob — it has landed on Israel."
    },
    "9": {
      "L": "And all the people shall know, even Ephraim and the inhabitant of Samaria, that say in the pride and stoutness of heart,",
      "M": "And all the people will know it — Ephraim and the inhabitants of Samaria — who say in pride and arrogance of heart:",
      "T": "All the people of Ephraim will know it — Samaria's inhabitants too — though they say with proud, stubborn hearts:"
    },
    "10": {
      "L": "The bricks are fallen down, but we will build with hewn stones: the sycomores are cut down, but we will change them into cedars.",
      "M": "The bricks have fallen, but we will rebuild with dressed stone; the sycamores have been cut down, but we will plant cedars in their place.",
      "T": "Our mud bricks have crumbled — we will rebuild with dressed stone!\nThe sycamores are down — we will plant cedars in their place!"
    },
    "11": {
      "L": "Therefore the LORD shall set up the adversaries of Rezin against him, and join his enemies together;",
      "M": "Therefore the LORD raises up the adversaries of Rezin against Israel and stirs up their enemies to attack —",
      "T": "So Yahweh has strengthened Rezin's enemies against them and roused their foes to strike —"
    },
    "12": {
      "L": "The Syrians before, and the Philistines behind; and they shall devour Israel with open mouth. For all this his anger is not turned away, but his hand is stretched out still.",
      "M": "the Syrians in front and the Philistines behind, and they devour Israel with open mouth. For all this his anger has not turned away; his hand is stretched out still.",
      "T": "Arameans from the east, Philistines from the west —\nthey swallow Israel whole.\nYet for all of this, his anger is not spent;\nhis hand is still raised to strike."
    },
    "13": {
      "L": "For the people turneth not unto him that smiteth them, neither do they seek the LORD of hosts.",
      "M": "But the people have not returned to him who struck them, nor have they sought the LORD of hosts.",
      "T": "Still the people did not turn to the one who was striking them;\nthey would not seek Yahweh of hosts."
    },
    "14": {
      "L": "Therefore the LORD will cut off from Israel head and tail, branch and rush, in one day.",
      "M": "So the LORD cut off from Israel head and tail, palm branch and reed, in a single day —",
      "T": "So Yahweh severed from Israel in a single day\nboth head and tail, both towering palm and lowly reed —"
    },
    "15": {
      "L": "The ancient and honourable, he is the head; and the prophet that teacheth lies, he is the tail.",
      "M": "the elder and honored man is the head, and the prophet who teaches lies is the tail.",
      "T": "the honored elder is the head;\nthe prophet who peddles lies is the tail."
    },
    "16": {
      "L": "For the leaders of this people cause them to err; and they that are led of them are destroyed.",
      "M": "For the guides of this people have led them astray, and those whom they lead are swallowed up.",
      "T": "The leaders of this people have led them into confusion,\nand those they guide are consumed."
    },
    "17": {
      "L": "Therefore the Lord shall have no joy in their young men, neither shall have mercy on their fatherless and widows: for every one is an hypocrite and an evildoer, and every mouth speaketh folly. For all this his anger is not turned away, but his hand is stretched out still.",
      "M": "Therefore the Lord does not rejoice over their young men, and has no compassion on their fatherless and widows, for everyone is godless and an evildoer, and every mouth speaks folly. For all this his anger has not turned away; his hand is stretched out still.",
      "T": "Therefore the Lord takes no delight in their young men,\nshows no mercy to their orphans and widows —\nfor every one of them is profane, a doer of evil,\nevery mouth full of senseless words.\nYet for all of this, his anger is not spent;\nhis hand is still raised to strike."
    },
    "18": {
      "L": "For wickedness burneth as the fire: it shall devour the briers and thorns, and shall kindle in the thickets of the forest, and they shall mount up like the lifting up of smoke.",
      "M": "For wickedness burns like a fire; it devours briers and thorns; it kindles the dense forest thickets, and they roll up in columns of smoke.",
      "T": "Wickedness blazes like fire —\nit burns through briers and thorns;\nit catches in the forest thickets\nand billows up in columns of smoke."
    },
    "19": {
      "L": "Through the wrath of the LORD of hosts is the land darkened, and the people shall be as the fuel of the fire: no man shall spare his brother.",
      "M": "Through the wrath of the LORD of hosts the land is scorched, and the people are like fuel for the fire; no one spares his brother.",
      "T": "By the fury of Yahweh of hosts the land is scorched;\nthe people themselves become the fire's own fuel —\nnot one man spares his brother."
    },
    "20": {
      "L": "And he shall snatch on the right hand, and be hungry; and he shall eat on the left hand, and they shall not be satisfied: they shall eat every man the flesh of his own arm:",
      "M": "They snatch food on the right but are still hungry; they eat on the left but are not satisfied; each one devours the flesh of his own kinsman.",
      "T": "They grab on the right and still go hungry;\nthey devour on the left and are not satisfied —\neach one consuming the flesh of those closest to him."
    },
    "21": {
      "L": "Manasseh, Ephraim; and Ephraim, Manasseh: and they together shall be against Judah. For all this his anger is not turned away, but his hand is stretched out still.",
      "M": "Manasseh devours Ephraim, and Ephraim devours Manasseh, and both together are against Judah. For all this his anger has not turned away; his hand is stretched out still.",
      "T": "Manasseh turns on Ephraim, Ephraim turns on Manasseh,\nand both together tear at Judah.\nYet for all of this, his anger is not spent;\nhis hand is still raised to strike."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 7–9 written.')

if __name__ == '__main__':
    main()
