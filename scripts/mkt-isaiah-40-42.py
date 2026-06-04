"""
MKT Isaiah chapters 40–42 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-40-42.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
- H430 (אֱלֹהִים): "God" throughout; "our God" / "your God" per context; no special deviation.
- H7307 (רוּחַ): Context-dependent:
    40:7 — "breath of the LORD" (L: "spirit"; M/T: "breath") — the wind that withers grass;
    40:13 — "Spirit of the LORD" (uppercase, all tiers) — the divine mind/Spirit;
    41:16 — "wind" (lower, all tiers) — the wind that scatters chaff;
    42:1 — "my Spirit" (uppercase, all tiers) — divine Spirit placed on the Servant;
    42:5 — "spirit" (lower, M/T) — breath/spirit given to those who walk the earth.
- H4941 (מִשְׁפָּט): "judgment" (L) / "justice" (M/T) — consistent with prior Isaiah scripts.
- H5650 (עֶבֶד): "servant" — consistent across all tiers; Isaiah 42:1–9 is the First Servant Song.
- H5315 (נֶפֶשׁ): 42:1 "my soul" (L/M) / "my heart" (T) — God's own self delights in the Servant;
    "soul" is literal Hebrew; T uses "heart" for natural English without losing the intimacy.
- H1285 (בְּרִית): 42:6 "covenant" (all tiers) — the Servant is given *as* a covenant to the people.
- H2617 (חֶסֶד): 40:6 "goodliness/beauty" — in this context the word means beauty/glory of the
    field flower, not covenant loyalty; L uses "goodliness" (traditional), M/T use "glory/beauty."
- H6918 (קָדוֹשׁ): "Holy One" (of Israel) — capitalized title throughout, all tiers.
- H136 + H3069 (אֲדֹנָי יְהוִה): 40:10 "Lord GOD" (L/M) / "Lord Yahweh" (T).
- H6664 (צֶדֶק): 41:2 contextual — the figure from the east is raised "in righteousness"
    (i.e., to serve God's righteous purpose); L: "the righteous man from the east";
    M/T: "the one from the east" with implicit divine purpose.
- H1350 (גָּאַל): 41:14 "Redeemer" — covenantal redemption; Yahweh as kinsman-redeemer.
- Poetry/prose: Chs. 40–42 are poetry throughout (Second Isaiah opens here); T uses line breaks.
    Ch. 40 = great comfort oracle; Ch. 41 = lawsuit against the nations + reassurance of Israel;
    Ch. 42 = First Servant Song (vv. 1–9) + new song (vv. 10–17) + Israel's blindness (vv. 18–25).
- 40:11 "those that are with young" = nursing ewes / mothers with young; M/T: "nursing mothers."
- 40:26 — The stars called by name: divine sovereignty over creation; T makes the march explicit.
- 41:2 — The "righteous man from the east" is widely understood as Cyrus of Persia (cf. 44:28,
    45:1); the translation does not name him here (Isaiah does not) but the context implies
    a conqueror raised by God.
- 41:8 — "Abraham my friend" (H157 אָהֵב = one who loves / beloved); L/M "friend"; T "my friend."
- 42:3 — "smoking flax" (H6594 פִּשְׁתָּה + H3544 כֵּהֶה) = a dimly burning wick; T: "guttering wick."
- 42:14 — God as woman in labor: a striking image preserved in all tiers; T makes the birth-cry vivid.
- 42:19 — "he that is perfect" (H7999 שָׁלֵם) = the dedicated/commissioned one; M/T: "dedicated one."
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
  "40": {
    "1": {
      "L": "Comfort ye, comfort ye my people, saith your God.",
      "M": "Comfort, comfort my people, says your God.",
      "T": "Comfort, comfort my people —\nsays your God."
    },
    "2": {
      "L": "Speak ye to the heart of Jerusalem, and cry unto her, that her warfare is accomplished, that her iniquity is pardoned; for she hath received of the LORD's hand double for all her sins.",
      "M": "Speak tenderly to Jerusalem and declare to her that her time of service is ended, that her iniquity is pardoned, that she has received from the LORD's hand double for all her sins.",
      "T": "Speak to Jerusalem's heart — announce to her:\nher hard service is over,\nher guilt is pardoned.\nFrom Yahweh's own hand she has received\ndouble payment for all her sins."
    },
    "3": {
      "L": "The voice of one crying in the wilderness: Prepare ye the way of the LORD; make straight in the desert a highway for our God.",
      "M": "A voice cries in the wilderness: 'Prepare the way of the LORD; make straight in the desert a highway for our God.'",
      "T": "A voice cries in the wilderness:\nPrepare the way of Yahweh!\nMake straight through the desert\na highway for our God."
    },
    "4": {
      "L": "Every valley shall be exalted, and every mountain and hill shall be made low; and the crooked shall be made straight, and the rough places plain.",
      "M": "Every valley will be raised up and every mountain and hill leveled; the crooked will be made straight and the rough ground a plain.",
      "T": "Every valley will be raised,\nevery mountain and hill brought low —\ncrooked terrain made level,\nrugged ground a smooth plain."
    },
    "5": {
      "L": "And the glory of the LORD shall be revealed, and all flesh shall see it together; for the mouth of the LORD hath spoken.",
      "M": "The glory of the LORD will be revealed, and all flesh will see it together; for the mouth of the LORD has spoken.",
      "T": "The glory of Yahweh will be unveiled,\nand all humanity will see it together —\nfor the mouth of Yahweh has spoken."
    },
    "6": {
      "L": "The voice said, Cry. And he said, What shall I cry? All flesh is grass, and all the goodliness thereof is as the flower of the field.",
      "M": "A voice says, 'Cry!' And someone asks, 'What shall I cry?' 'All flesh is grass, and all its beauty is like the flower of the field.'",
      "T": "A voice says: Cry!\nWhat shall I cry? he asked.\nAll humanity is grass;\nall its glory is like a wildflower."
    },
    "7": {
      "L": "The grass withereth, the flower fadeth, because the spirit of the LORD bloweth upon it; surely the people is grass.",
      "M": "The grass withers and the flower fades when the breath of the LORD blows on them; the people are surely grass.",
      "T": "Grass withers, the flower fades\nwhen the breath of Yahweh blows over them —\nyes, the people are grass."
    },
    "8": {
      "L": "The grass withereth, the flower fadeth; but the word of our God shall stand for ever.",
      "M": "The grass withers, the flower fades, but the word of our God stands forever.",
      "T": "Grass withers, flowers fade —\nbut the word of our God\nstands forever."
    },
    "9": {
      "L": "O Zion, that bringest good tidings, get thee up into the high mountain; O Jerusalem, that bringest good tidings, lift up thy voice with strength; lift it up, be not afraid; say unto the cities of Judah, Behold your God.",
      "M": "Get up onto a high mountain, O Zion, messenger of good news! Lift your voice with strength, O Jerusalem, herald of good news! Lift it up; do not fear! Say to the cities of Judah: 'Look — your God!'",
      "T": "Climb the high mountain, O Zion —\nyou who carry this good news!\nShout without fear, O Jerusalem —\nyou who herald this good news!\nCall out to the cities of Judah:\nLook — your God is here!"
    },
    "10": {
      "L": "Behold, the Lord GOD will come with strong arm, and his arm shall rule for him; behold, his reward is with him, and his recompense before his face.",
      "M": "See — the Lord GOD comes with strength, and his arm rules on his behalf; see — his reward is with him, and his recompense before him.",
      "T": "See — the Lord Yahweh comes in strength;\nhis arm holds the power.\nLook — he carries his reward with him;\nhis recompense goes before him."
    },
    "11": {
      "L": "He shall feed his flock like a shepherd; he shall gather the lambs with his arm, and carry them in his bosom, and shall gently lead those that are with young.",
      "M": "He tends his flock like a shepherd; he gathers the lambs in his arm and carries them in his bosom; he gently leads the nursing ewes.",
      "T": "He tends his flock like a shepherd —\ngathering the lambs in his arms,\ncarrying them against his chest,\ngently leading the nursing mothers."
    },
    "12": {
      "L": "Who hath measured the waters in the hollow of his hand, and meted out heaven with the span, and comprehended the dust of the earth in a measure, and weighed the mountains in scales, and the hills in a balance?",
      "M": "Who has measured the waters in the hollow of his hand, marked off the heavens with a span, gathered up the dust of the earth in a measure, weighed the mountains in scales and the hills in a balance?",
      "T": "Who has scooped the oceans into his palm,\nmeasured the heavens with a handspan,\npacked the earth's dust into a cup,\nweighed mountains on a scale\nand hills in a balance?"
    },
    "13": {
      "L": "Who hath directed the Spirit of the LORD, or being his counsellor hath taught him?",
      "M": "Who has guided the Spirit of the LORD, or who has been his counselor to instruct him?",
      "T": "Who has directed the Spirit of Yahweh?\nWho has served as his counselor to instruct him?"
    },
    "14": {
      "L": "With whom took he counsel, and who instructed him, and taught him in the path of judgment, and taught him knowledge, and shewed him the way of understanding?",
      "M": "With whom did he consult? Who instructed him and taught him the path of justice, who taught him knowledge and showed him the way of understanding?",
      "T": "Who was his advisor?\nWho taught him how to act justly?\nWho gave him knowledge\nor showed him the way of understanding?"
    },
    "15": {
      "L": "Behold, the nations are as a drop of a bucket, and are counted as the small dust of the balance; behold, he taketh up the isles as a very little thing.",
      "M": "See — the nations are like a drop in a bucket and are counted as dust on the scales; see — he lifts up the coastlands like a grain of fine dust.",
      "T": "The nations are a drop in a bucket to him —\nweighed on his scales they are dust.\nHe picks up the coastlands\nlike a pinch of fine powder."
    },
    "16": {
      "L": "And Lebanon is not sufficient to burn, nor the beasts thereof sufficient for a burnt offering.",
      "M": "Even Lebanon is not sufficient for firewood, nor are its animals enough for a burnt offering.",
      "T": "All of Lebanon's forests would not suffice for fuel,\nnor would all its animals make an adequate burnt offering."
    },
    "17": {
      "L": "All nations before him are as nothing; and they are counted to him less than nothing, and vanity.",
      "M": "All the nations are as nothing before him; they are counted by him as less than nothing and futility.",
      "T": "Before him, every nation is nothing —\nless than nothing he counts them,\na breath of vapor."
    },
    "18": {
      "L": "To whom then will ye liken God? or what likeness will ye compare unto him?",
      "M": "To whom will you compare God? What likeness will you set beside him?",
      "T": "So to whom will you compare God?\nWhat image could come close?"
    },
    "19": {
      "L": "The workman melteth a graven image, and the goldsmith spreadeth it over with gold, and casteth silver chains.",
      "M": "A craftsman casts an idol, and the goldsmith overlays it with gold and fashions silver chains for it.",
      "T": "A craftsman casts an idol.\nThe goldsmith plates it with gold,\nshaping silver chains to adorn it."
    },
    "20": {
      "L": "He that is so impoverished that he hath no oblation chooseth a tree that will not rot; he seeketh unto him a cunning workman to prepare a graven image, that shall not be moved.",
      "M": "He who is too poor to bring a proper offering selects wood that will not rot; he looks for a skilled craftsman to set up an idol that will not topple.",
      "T": "A man too poor for a proper offering\nchooses a wood that will not rot;\nhe hunts for a skilled craftsman\nto set up an idol that will not fall."
    },
    "21": {
      "L": "Have ye not known? have ye not heard? hath it not been told you from the beginning? have ye not understood from the foundations of the earth?",
      "M": "Do you not know? Have you not heard? Has it not been declared to you from the beginning? Have you not understood from the foundations of the earth?",
      "T": "Don't you know?\nHaven't you heard?\nHasn't this been told you from the very beginning?\nHaven't you understood from the moment the earth was founded?"
    },
    "22": {
      "L": "It is he that sitteth upon the circle of the earth, and the inhabitants thereof are as grasshoppers; that stretcheth out the heavens as a curtain, and spreadeth them out as a tent to dwell in;",
      "M": "It is he who sits enthroned above the circle of the earth, whose inhabitants are like grasshoppers; who stretches out the heavens like a curtain and spreads them like a tent to live in;",
      "T": "He is the one who sits enthroned above the circle of the earth,\nwhose inhabitants look up like grasshoppers —\nwho stretches out the heavens like a curtain\nand spreads them like a tent to live in."
    },
    "23": {
      "L": "That bringeth the princes to nothing; he maketh the judges of the earth as vanity.",
      "M": "He brings princes to nothing and reduces the rulers of the earth to emptiness.",
      "T": "He reduces princes to nothing\nand makes earth's rulers vanish like vapor."
    },
    "24": {
      "L": "Yea, they shall not be planted; yea, they shall not be sown; yea, their stock shall not take root in the earth; and he shall also blow upon them, and they shall wither, and the whirlwind shall take them away as stubble.",
      "M": "Scarcely have they been planted, scarcely sown, their root scarcely taken in the earth, when he blows on them and they wither, and the whirlwind sweeps them away like chaff.",
      "T": "Barely planted, barely sown —\ntheir roots have barely taken hold —\nhe breathes on them and they wither.\nThe whirlwind carries them off like stubble."
    },
    "25": {
      "L": "To whom then will ye liken me, or shall I be equal? saith the Holy One.",
      "M": "'To whom will you compare me? Who is my equal?' says the Holy One.",
      "T": "'So — to whom will you compare me?\nWho is my equal?' says the Holy One."
    },
    "26": {
      "L": "Lift up your eyes on high, and behold who hath created these things, that bringeth out their host by number; he calleth them all by names, by the greatness of his might, for that he is strong in power; not one faileth.",
      "M": "Lift up your eyes on high and see: who created all these? He leads out their army by number, calling each one by name. Because of his great power and mighty strength, not one of them is missing.",
      "T": "Lift your eyes up and look:\nWho created all these?\nHe marches out their ranks by number,\ncalling each one by name.\nSo great is his power and mighty his strength\nthat not one of them goes missing."
    },
    "27": {
      "L": "Why sayest thou, O Jacob, and speakest, O Israel, My way is hid from the LORD, and my judgment is passed over from my God?",
      "M": "Why do you say, O Jacob, and why do you speak, O Israel, 'My way is hidden from the LORD, and my cause is overlooked by my God'?",
      "T": "Why do you say this, Jacob —\nwhy do you insist, Israel —\n'My path is hidden from Yahweh;\nmy God takes no notice of my case'?"
    },
    "28": {
      "L": "Hast thou not known? hast thou not heard, that the everlasting God, the LORD, the Creator of the ends of the earth, fainteth not, neither is weary? there is no searching of his understanding.",
      "M": "Do you not know? Have you not heard? The LORD is the everlasting God, the Creator of the ends of the earth. He does not grow faint or weary; his understanding cannot be searched out.",
      "T": "Don't you know?\nHaven't you heard?\nYahweh is the everlasting God —\nCreator of the far ends of the earth.\nHe never grows faint or weary;\nhis understanding no one can fathom."
    },
    "29": {
      "L": "He giveth power to the faint; and to them that have no might he increaseth strength.",
      "M": "He gives strength to the weary and increases the power of those who have no might.",
      "T": "He gives power to the weary\nand multiplies strength for those who have none."
    },
    "30": {
      "L": "Even the youths shall faint and be weary, and the young men shall utterly fall;",
      "M": "Even youths grow faint and weary, and young men stumble and fall —",
      "T": "Even young men grow faint and weary;\neven the strong ones stumble and collapse —"
    },
    "31": {
      "L": "But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; and they shall walk, and not faint.",
      "M": "but those who wait for the LORD will renew their strength; they will soar on wings like eagles; they will run and not grow weary; they will walk and not faint.",
      "T": "but those who wait on Yahweh will renew their strength.\nThey will soar on wings like eagles;\nthey will run and not grow weary,\nthey will walk and not faint."
    }
  },
  "41": {
    "1": {
      "L": "Keep silence before me, O islands; and let the peoples renew their strength; let them come near; then let them speak; let us come near together for judgment.",
      "M": "Be silent before me, O coastlands; let the nations renew their strength; let them come near and then speak; let us together draw near for judgment.",
      "T": "Fall silent before me, O coastlands;\nlet the peoples gather their strength.\nLet them come forward — let them speak.\nLet us come near together for the verdict."
    },
    "2": {
      "L": "Who raised up the righteous man from the east, called him to his foot, gave the nations before him, and made him rule over kings? He gave them as the dust to his sword, and as driven stubble to his bow.",
      "M": "Who has roused the conqueror from the east, whom victory meets at every step? He delivers nations before him and makes him trample kings; his sword makes them like dust, his bow like driven stubble.",
      "T": "Who roused that conqueror from the east\nand summoned victory to meet him at every step?\nHe delivers nations before him;\nkings fall beneath his feet.\nHis sword makes them dust;\nhis bow scatters them like driven stubble."
    },
    "3": {
      "L": "He pursued them, and passed safely; even by the way that he had not gone with his feet.",
      "M": "He pursues them and passes on safely, traveling paths his feet have never trodden before.",
      "T": "He pursues, passes on, unharmed —\nacross terrain his feet have never traveled."
    },
    "4": {
      "L": "Who hath wrought and done it, calling the generations from the beginning? I the LORD, the first, and with the last; I am he.",
      "M": "Who has done this, calling the generations from the beginning? I, the LORD — I was first, and I am with the last; I am he.",
      "T": "Who has done all this,\ncalling the generations into being from the beginning?\nI, Yahweh — I am the first,\nand with the last I am the same. I am he."
    },
    "5": {
      "L": "The isles saw it, and feared; the ends of the earth were afraid, and drew near, and came.",
      "M": "The coastlands saw it and were afraid; the ends of the earth trembled; they drew near and came forward.",
      "T": "The coastlands saw it and trembled;\nthe ends of the earth shook with fear.\nThey drew near and came."
    },
    "6": {
      "L": "They helped every one his neighbour; and every one said to his brother, Be of good courage.",
      "M": "Each one helps the other, and says to his companion, 'Take courage!'",
      "T": "Each craftsman encourages his fellow;\nbrother says to brother, 'Hold firm!'"
    },
    "7": {
      "L": "So the carpenter encouraged the goldsmith, and he that smootheth with the hammer him that smote the anvil, saying, It is ready for the sodering; and he fastened it with nails, that it should not be moved.",
      "M": "The craftsman encourages the goldsmith; the one who smooths with the hammer encourages the one striking the anvil, saying of the soldering, 'It is good'; and they fasten it with nails so that it cannot wobble.",
      "T": "Craftsman cheers on goldsmith;\nthe one who hammers smooth encourages\nthe one who strikes the anvil:\n'The join is solid!' they say.\nThey nail it down so it cannot move."
    },
    "8": {
      "L": "But thou, Israel, art my servant, Jacob whom I have chosen, the seed of Abraham my friend.",
      "M": "But you, Israel, my servant, Jacob, whom I have chosen, offspring of Abraham my friend —",
      "T": "But you, Israel — you are my servant,\nJacob, whom I have chosen,\noffspring of Abraham, my friend —"
    },
    "9": {
      "L": "Thou whom I have taken from the ends of the earth, and called thee from the chief men thereof, and said unto thee, Thou art my servant; I have chosen thee, and not cast thee away.",
      "M": "you whom I took from the ends of the earth and called from its farthest regions, saying to you, 'You are my servant; I have chosen you and not rejected you' —",
      "T": "you whom I took from the ends of the earth\nand called from its farthest corners,\nsaying: You are my servant,\nI have chosen you and not cast you aside."
    },
    "10": {
      "L": "Fear thou not; for I am with thee; be not dismayed; for I am thy God; I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.",
      "M": "Do not fear, for I am with you; do not be dismayed, for I am your God; I will strengthen you; I will help you; I will uphold you with my righteous right hand.",
      "T": "Do not fear — I am with you.\nDo not be dismayed — I am your God.\nI will strengthen you, I will help you,\nI will hold you up with my righteous right hand."
    },
    "11": {
      "L": "Behold, all they that were incensed against thee shall be ashamed and confounded; they shall be as nothing; and they that strive with thee shall perish.",
      "M": "See — all who are enraged against you will be put to shame and disgraced; those who oppose you will come to nothing and perish.",
      "T": "Every one who rages against you\nwill end in shame and disgrace.\nThose who fight you will come to nothing —\nthey will perish."
    },
    "12": {
      "L": "Thou shalt seek them, and shalt not find them, even them that contended with thee; they that war against thee shall be as nothing, and as a thing of nought.",
      "M": "You will seek your adversaries but will not find them; those who make war against you will be as nothing at all.",
      "T": "You will look for those who fight you\nand not find them.\nThose who make war on you\nwill be nothing — utterly gone."
    },
    "13": {
      "L": "For I the LORD thy God will hold thy right hand, saying unto thee, Fear not; I will help thee.",
      "M": "For I, the LORD your God, hold your right hand; I am the one who says to you, 'Do not fear; I will help you.'",
      "T": "For I, Yahweh your God, am gripping your right hand,\nsaying to you: Do not fear — I am the one who helps you."
    },
    "14": {
      "L": "Fear not, thou worm Jacob, and ye men of Israel; I will help thee, saith the LORD, and thy redeemer, the Holy One of Israel.",
      "M": "Do not be afraid, O Jacob, you worm; you few men of Israel! I am the one who helps you, declares the LORD; your Redeemer is the Holy One of Israel.",
      "T": "Do not be afraid, worm Jacob —\nyou who feel so small, O people of Israel!\nI am your helper — Yahweh declares it.\nYour Redeemer is the Holy One of Israel."
    },
    "15": {
      "L": "Behold, I will make thee a new sharp threshing instrument having teeth; thou shalt thresh the mountains, and beat them small, and shalt make the hills as chaff.",
      "M": "See — I will make you a new, sharp threshing sledge with many cutting edges; you will thresh the mountains and crush them, and reduce the hills to chaff.",
      "T": "Look — I will make you a new threshing sledge,\nsharp with many teeth.\nYou will thresh the mountains and grind them to dust;\nyou will reduce the hills to chaff."
    },
    "16": {
      "L": "Thou shalt fan them, and the wind shall carry them away, and the whirlwind shall scatter them; and thou shalt rejoice in the LORD, and shalt glory in the Holy One of Israel.",
      "M": "You will winnow them, and the wind will carry them away and the gale will scatter them; you will rejoice in the LORD and glory in the Holy One of Israel.",
      "T": "You will winnow them;\nthe wind will carry them away,\nthe gale will scatter them.\nThen you will rejoice in Yahweh;\nyou will glory in the Holy One of Israel."
    },
    "17": {
      "L": "When the poor and needy seek water, and there is none, and their tongue faileth for thirst, I the LORD will hear them, I the God of Israel will not forsake them.",
      "M": "When the poor and the needy seek water and there is none, when their tongue is parched with thirst, I, the LORD, will answer them; I, the God of Israel, will not forsake them.",
      "T": "When the poor and needy seek water\nand there is none,\nwhen their tongues are cracked with thirst —\nI, Yahweh, will answer them;\nI, the God of Israel, will not abandon them."
    },
    "18": {
      "L": "I will open rivers in high places, and fountains in the midst of the valleys; I will make the wilderness a pool of water, and the dry land springs of water.",
      "M": "I will open rivers on the bare heights and fountains in the middle of the valleys; I will turn the wilderness into a pool of water and the dry ground into springs.",
      "T": "I will open rivers on the bare heights\nand springs in the valley floors.\nI will turn the wilderness into a standing pool\nand the parched ground into flowing springs."
    },
    "19": {
      "L": "I will plant in the wilderness the cedar, the shittah tree, and the myrtle, and the oil tree; I will set in the desert the fir tree, and the pine, and the box tree together;",
      "M": "I will plant in the wilderness cedar, acacia, myrtle, and olive trees; I will set in the desert cypress, plane tree, and pine together —",
      "T": "In the wilderness I will plant\ncedar, acacia, myrtle, and olive.\nIn the desert I will set\ncypress, plane, and pine side by side —"
    },
    "20": {
      "L": "That they may see, and know, and consider, and understand together, that the hand of the LORD hath done this, and the Holy One of Israel hath created it.",
      "M": "so that they may see and know, consider and understand together, that the hand of the LORD has done this, and the Holy One of Israel has created it.",
      "T": "— so that all may see and know,\nconsider and understand together,\nthat the hand of Yahweh has done this,\nthat the Holy One of Israel has created it."
    },
    "21": {
      "L": "Produce your cause, saith the LORD; bring forth your strong reasons, saith the King of Jacob.",
      "M": "Present your case, says the LORD; bring forward your strongest arguments, says the King of Jacob.",
      "T": "State your case — Yahweh demands it.\nBring your strongest arguments —\nsays the King of Jacob."
    },
    "22": {
      "L": "Let them bring them forth, and shew us what shall happen; let them shew the former things, what they be, that we may consider them, and know the latter end of them; or declare us things for to come.",
      "M": "Let them come forward and tell us what will happen; let them declare the former things, what they were, so we may consider them and know their outcome; or announce to us what is to come.",
      "T": "Let them step forward and tell us what will happen.\nLet them explain the former things — what they were —\nso we can trace where they led.\nOr let them announce what is coming."
    },
    "23": {
      "L": "Shew the things that are to come hereafter, that we may know that ye are gods; yea, do good, or do evil, that we may be dismayed, and behold it together.",
      "M": "Tell us what is to come in the future, so that we may know you are gods. Do good or do evil — do something — so that we may see it and stand in awe together.",
      "T": "Foretell what is coming, so we may know\nyou actually are gods.\nDo something — good or bad —\nso we may stare at it and tremble."
    },
    "24": {
      "L": "Behold, ye are of nothing, and your work of nought; an abomination is he that chooseth you.",
      "M": "See — you are nothing and your work amounts to nothing; whoever chooses you is an abomination.",
      "T": "You are nothing.\nYour works are nothing.\nWhoever chooses you is revolting."
    },
    "25": {
      "L": "I have raised up one from the north, and he shall come; from the rising of the sun shall he call upon my name; and he shall come upon princes as upon morter, and as the potter treadeth clay.",
      "M": "I have stirred up one from the north, and he comes; from the east he comes, calling on my name; he will trample rulers as if they were mortar, as a potter treads clay.",
      "T": "I have roused one from the north — he comes;\nfrom the east he calls on my name.\nHe treads on rulers as on mud,\ntramples them as a potter works his clay."
    },
    "26": {
      "L": "Who hath declared from the beginning, that we may know? and beforetime, that we may say, He is righteous? yea, there is none that sheweth, yea, there is none that declareth, yea, there is none that heareth your words.",
      "M": "Who declared this from the beginning, so we could know? Who foretold it beforehand, so we could say, 'He is right'? Not one declared it; not one announced it; not one heard you say it.",
      "T": "Who declared this beforehand, so we could know?\nWho foretold it, so we could say, 'Right!'?\nNo one declared it.\nNo one announced it.\nNo one heard a word from you."
    },
    "27": {
      "L": "The first shall say to Zion, Behold, behold them; and I will give to Jerusalem one that bringeth good tidings.",
      "M": "I was the first to say to Zion, 'Look — here they are!' and I give Jerusalem a messenger of good news.",
      "T": "I was the first to announce to Zion:\nLook — here they come!\nI am giving Jerusalem one who brings the good news."
    },
    "28": {
      "L": "For I beheld, and there was no man; even among them, and there was no counsellor, that, when I asked of them, could answer a word.",
      "M": "For I looked, and there was no one; among them there was no counselor; when I asked them, not one could answer.",
      "T": "I looked — there was no one.\nAmong all these, not a counselor to be found.\nI asked, and not one of them could answer."
    },
    "29": {
      "L": "Behold, they are all vanity; their works are nothing; their molten images are wind and confusion.",
      "M": "See — they are all emptiness; their works come to nothing; their cast images are just wind and futility.",
      "T": "There they all are — vapor, every one.\nTheir works: nothing.\nTheir cast images: wind and confusion."
    }
  },
  "42": {
    "1": {
      "L": "Behold my servant, whom I uphold; mine elect, in whom my soul delighteth; I have put my spirit upon him; he shall bring forth judgment to the Gentiles.",
      "M": "Here is my servant, whom I uphold; my chosen one, in whom I delight; I have placed my Spirit on him; he will bring justice to the nations.",
      "T": "Here is my servant, whom I uphold —\nmy chosen one, in whom my heart delights.\nI have placed my Spirit upon him;\nhe will bring forth justice to the nations."
    },
    "2": {
      "L": "He shall not cry, nor lift up, nor cause his voice to be heard in the street.",
      "M": "He will not shout or raise his voice, or make himself heard in the streets.",
      "T": "He will not shout or raise his voice\nor make himself heard in the streets."
    },
    "3": {
      "L": "A bruised reed shall he not break, and the smoking flax shall he not quench; he shall bring forth judgment unto truth.",
      "M": "A bruised reed he will not break, and a smoldering wick he will not snuff out; he will bring forth justice faithfully.",
      "T": "A bent reed he will not snap;\na guttering wick he will not snuff out.\nHe will carry out justice faithfully."
    },
    "4": {
      "L": "He shall not fail nor be discouraged, till he have set judgment in the earth; and the isles shall wait for his law.",
      "M": "He will not grow faint or be discouraged until he has established justice in the earth; and the coastlands will wait for his law.",
      "T": "He will not falter or lose heart\nuntil he has planted justice in the earth —\nand the coastlands wait in hope for his instruction."
    },
    "5": {
      "L": "Thus saith God the LORD, he that created the heavens, and stretched them out; he that spread forth the earth, and that which cometh out of it; he that giveth breath unto the people upon it, and spirit to them that walk therein:",
      "M": "This is what God the LORD says — he who created the heavens and stretched them out, who spread out the earth and everything it produces, who gives breath to the people on it and spirit to those who walk on it:",
      "T": "This is what God Yahweh says —\nhe who created the heavens and stretched them out,\nwho spread out the earth and all that grows from it,\nwho gives breath to the people on it\nand spirit to those who walk on it:"
    },
    "6": {
      "L": "I the LORD have called thee in righteousness, and will hold thine hand, and will keep thee, and give thee for a covenant of the people, for a light of the Gentiles;",
      "M": "I, the LORD, have called you in righteousness; I will take hold of your hand and keep you; I will make you a covenant for the people, a light for the nations,",
      "T": "I, Yahweh, have called you in righteousness;\nI have taken hold of your hand and I will keep you.\nI will make you a covenant for the people,\na light for the nations —"
    },
    "7": {
      "L": "To open the blind eyes, to bring out the prisoners from the prison, and them that sit in darkness out of the prison house.",
      "M": "to open eyes that are blind, to bring prisoners out of the dungeon, to release from prison those who sit in darkness.",
      "T": "to open eyes that are blind,\nto bring out prisoners from the dungeon,\nto release from the dark cell those who have been bound."
    },
    "8": {
      "L": "I am the LORD; that is my name; and my glory will I not give to another, neither my praise to graven images.",
      "M": "I am the LORD; that is my name; I will not give my glory to another nor my praise to carved idols.",
      "T": "I am Yahweh — that is my name.\nMy glory I will not share with anyone.\nMy praise I will not give to carved idols."
    },
    "9": {
      "L": "Behold, the former things are come to pass, and new things do I declare; before they spring forth I tell you of them.",
      "M": "See — the former things have come to pass, and new things I now declare; before they spring up I announce them to you.",
      "T": "The former things have come to pass —\nnew things I now declare.\nBefore they spring up, I am telling you."
    },
    "10": {
      "L": "Sing unto the LORD a new song, and his praise from the end of the earth, ye that go down to the sea, and all that is therein; the isles, and the inhabitants thereof.",
      "M": "Sing to the LORD a new song, his praise from the ends of the earth — you who sail the sea and all its creatures, you coastlands and their inhabitants.",
      "T": "Sing to Yahweh a new song —\nhis praise from the ends of the earth!\nYou who sail the seas and all that fills them,\nyou coastlands and all who live on them."
    },
    "11": {
      "L": "Let the wilderness and the cities thereof lift up their voice, the villages that Kedar doth inhabit; let the inhabitants of the rock sing, let them shout from the top of the mountains.",
      "M": "Let the wilderness and its towns raise their voice, the villages where Kedar dwells; let the inhabitants of Sela sing for joy; let them shout from the tops of the mountains.",
      "T": "Let the wilderness and its settlements shout,\nthe villages where Kedar's people live.\nLet the people of Sela sing for joy;\nlet them shout from the mountain peaks."
    },
    "12": {
      "L": "Let them give glory unto the LORD, and declare his praise in the islands.",
      "M": "Let them ascribe glory to the LORD and proclaim his praise in the coastlands.",
      "T": "Let them give glory to Yahweh\nand proclaim his praise in the coastlands."
    },
    "13": {
      "L": "The LORD shall go forth as a mighty man, he shall stir up jealousy like a man of war; he shall cry, yea, roar; he shall prevail against his enemies.",
      "M": "The LORD marches out like a warrior, like a man of war he arouses his zeal; he cries out, he shouts aloud, he shows himself mighty against his enemies.",
      "T": "Yahweh marches out like a warrior,\nlike a soldier of war he fans his fury.\nHe shouts — he roars —\nhe prevails over his enemies."
    },
    "14": {
      "L": "I have long time holden my peace; I have been still, and refrained myself; now will I cry like a travailing woman; I will destroy and devour at once.",
      "M": "For a long time I have kept silent; I have been still and held myself back; now I will cry out like a woman in labor; I will gasp and pant.",
      "T": "For so long I have been silent,\nstill, holding myself back.\nBut now I will cry out like a woman in labor —\ngasping, panting."
    },
    "15": {
      "L": "I will make waste mountains and hills, and dry up all their herbs; and I will make the rivers islands, and I will dry up the pools.",
      "M": "I will lay waste mountains and hills and dry up all their vegetation; I will turn rivers into dry land and drain the pools.",
      "T": "I will lay mountains and hills waste,\ndrying up all their vegetation.\nI will make rivers into dry land\nand drain the pools."
    },
    "16": {
      "L": "And I will bring the blind by a way that they knew not; I will lead them in paths that they have not known; I will make darkness light before them, and crooked things straight. These things will I do unto them, and not forsake them.",
      "M": "I will lead the blind along a road they have not known; I will guide them on paths they have never walked. I will turn darkness into light before them, and rough terrain into level ground. These are the things I will do, and I will not abandon them.",
      "T": "I will lead the blind on roads they have never walked,\nguide them on paths they have never known.\nDarkness I will turn into light before them;\nrough terrain into level ground.\nThese things I will do —\nI will not abandon them."
    },
    "17": {
      "L": "They shall be turned back, they shall be greatly ashamed, that trust in graven images, that say to the molten images, Ye are our gods.",
      "M": "Those who trust in carved idols and say to cast images, 'You are our gods,' will be turned back and completely disgraced.",
      "T": "Those who trust in carved idols,\nwho say to cast images, 'You are our gods' —\nthey will be driven back in utter disgrace."
    },
    "18": {
      "L": "Hear, ye deaf; and look, ye blind, that ye may see.",
      "M": "Hear, you deaf! Look, you blind, and see!",
      "T": "Hear, you who are deaf!\nLook, you who are blind — see!"
    },
    "19": {
      "L": "Who is blind, but my servant? or deaf, as my messenger that I sent? who is blind as he that is perfect, and blind as the LORD's servant?",
      "M": "Who is blind but my servant, or deaf like my messenger whom I send? Who is blind as my dedicated one, or blind as the servant of the LORD?",
      "T": "Who is as blind as my servant?\nAs deaf as the messenger I send?\nBlind as the one I have set apart —\nblind as Yahweh's own servant?"
    },
    "20": {
      "L": "Seeing many things, but thou observest not; opening the ears, but he heareth not.",
      "M": "He sees many things but does not take them in; his ears are open but he does not hear.",
      "T": "Seeing much but noticing nothing;\nears open but not listening."
    },
    "21": {
      "L": "The LORD is well pleased for his righteousness' sake; he will magnify the law, and make it honourable.",
      "M": "It pleased the LORD, for the sake of his righteousness, to make his law great and glorious.",
      "T": "It was Yahweh's pleasure, for the sake of his own righteousness,\nto make his law great and magnificent."
    },
    "22": {
      "L": "But this is a people robbed and spoiled; they are all of them snared in holes, and they are hid in prison houses; they are for a prey, and none delivereth; for a spoil, and none saith, Restore.",
      "M": "But this is a people robbed and plundered; they are all trapped in holes and hidden in dungeons; they have been made prey and there is no one to rescue them, made spoil and no one says, 'Give them back.'",
      "T": "But this is a people robbed and stripped —\nall of them caught in holes,\nhidden in dungeons.\nMade prey, and no one rescues.\nMade plunder, and no one says, 'Give them back.'"
    },
    "23": {
      "L": "Who among you will give ear to this? who will hearken and hear for the time to come?",
      "M": "Who among you will pay attention to this? Who will listen and hear for what is to come?",
      "T": "Who among you will truly listen to this?\nWho will pay close attention for what is coming?"
    },
    "24": {
      "L": "Who gave Jacob for a spoil, and Israel to the robbers? did not the LORD, he against whom we have sinned? for they would not walk in his ways, neither were they obedient unto his law.",
      "M": "Who handed Jacob over to plunderers, and Israel to robbers? Was it not the LORD, against whom we have sinned? For they refused to walk in his ways and were not obedient to his law.",
      "T": "Who handed Jacob over to robbers?\nWho gave Israel up to plunderers?\nWas it not Yahweh — he against whom we sinned?\nThey refused to walk in his ways;\nthey would not obey his law."
    },
    "25": {
      "L": "Therefore he hath poured upon him the fury of his anger, and the strength of battle; and it hath set him on fire round about, yet he knew not; and it burned him, yet he laid it not to heart.",
      "M": "So he poured his burning anger and the force of battle upon him; it set him ablaze all around, but he did not understand; it burned him, but he took no notice.",
      "T": "So Yahweh poured his fury and the force of war upon him —\nset him ablaze on every side —\nbut he did not understand.\nBurned — and he never took it to heart."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 40–42 written.')

if __name__ == '__main__':
    main()
