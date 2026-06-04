"""
MKT Isaiah chapters 37–39 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-37-39.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts;
  divine personal name surfaced in T throughout Isaiah.
- H136 (אֲדֹנָי): Does not appear prominently in these chapters; where "Lord" appears alone
  it translates H136 and is lower-case in all tiers.
- H6635 (צְבָאוֹת): "of hosts" — cosmic sovereignty designation, consistent with all
  prior Isaiah scripts. Appears in 37:16, 37:32, 39:5.
- H6918 (קָדוֹשׁ יִשְׂרָאֵל): "Holy One of Israel" — 37:23 only; capitalized throughout
  Isaiah; consistent with prior scripts.
- H4397 (מַלְאָך): 37:36 "the angel of the LORD" — the divine envoy who strikes 185,000.
  All tiers render "angel of the LORD" / "angel of Yahweh" (T). No reinterpretation.
- H7307 (רוּחַ): 37:7 — not "Spirit" here but "a spirit" = a divinely-sent disposition
  or disturbance in Sennacherib's mind; lowercase in all tiers.
- H5315 (נֶפֶשׁ): 38:17 "to my soul" = the embodied self; not the immaterial Greek soul.
  L/M: "soul"; T: "life" where the embodied sense is primary.
- H2617 (חֶסֶד): Does not appear in these chapters.
- H4941 (מִשְׁפָּט): Does not appear in these chapters.
- H7585 (שְׁאוֹל): 38:10, 38:18 — transliterated "Sheol" in all tiers; not "grave" or
  "hell." The realm of the dead, place of shadows, no presence of Yahweh.
- H5612 (מִכְתָּב): 38:9 "The writing of Hezekiah" — the section heading for the psalm;
  all tiers preserve "The writing of Hezekiah" or "A writing."
- Structural notes:
  Ch. 37 — Prose narrative (vv. 1–13) → Hezekiah's prayer (vv. 14–20) → Isaiah's taunt
  oracle against Sennacherib (vv. 21–35, mostly poetry) → narrative conclusion (vv. 36–38).
  The taunt oracle (vv. 22–29) is Yahweh's own voice mocking the Assyrian; T uses line
  breaks throughout vv. 22–32 to honor the poetry.
  Ch. 38 — Narrative frame (vv. 1–8, 21–22) surrounds Hezekiah's psalm (vv. 9–20), which
  is one of the finest personal lament-to-thanksgiving poems in the Hebrew Bible. T uses
  full line-break treatment for all of vv. 10–20. Note: vv. 21–22 appear after the psalm
  in Isaiah (unlike 2 Kings 20:7–8, where they precede the sign); the Isaiah ordering is
  likely a liturgical collection placing the sign narrative after the poem.
  Ch. 39 — Entirely prose; the hinge chapter turning toward Babylonian exile. Isaiah 40–55
  addresses an audience in Babylon; this chapter explains why: Hezekiah's proud display
  sealed the future. T surfaces the irony of Hezekiah's final response (39:8) — "at least
  there will be peace in my days" — without adding polemic; the words carry their own edge.
- Aspect notes:
  37:22–29 prophetic perfect rendered as present/vivid future; the taunt is already certain.
  38:10–20 psalm: past description of near-death experience, shifting to present praise
  (vv. 17–20); the Hebrew tense shifts are honored in all three tiers.
  39:6–7 future prophecy about Babylon: rendered as genuine future throughout.
- OT echoes:
  37:16 "you alone are God over all the kingdoms" — echoes Deut 6:4 (Shema); T notes this
  implicitly by keeping the "you alone" emphasis prominent.
  37:32 "the zeal of the LORD of hosts" — identical formula to Isa 9:7 (Immanuel passage);
  signals messianic-restoration frame around Hezekiah's deliverance.
  38:17 "cast all my sins behind your back" — unique image in the OT; forgiveness as
  spatial act: God puts them behind where he cannot see them. T makes the spatial vividness
  explicit.
  39:8 "Good is the word of the LORD" + "peace in my days" — the Chronicler later omits
  Hezekiah's self-serving addition (2 Chron 32 has no equivalent). Isaiah preserves the
  full ambiguity of this response.
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
  "37": {
    "1": {
      "L": "And it came to pass, when King Hezekiah heard it, that he tore his clothes and covered himself with sackcloth and went into the house of the LORD.",
      "M": "When King Hezekiah heard the report, he tore his clothes, covered himself with sackcloth, and went into the house of the LORD.",
      "T": "The moment King Hezekiah heard the news, he tore his clothes, wrapped himself in sackcloth, and went straight to the house of Yahweh."
    },
    "2": {
      "L": "And he sent Eliakim, who was over the household, and Shebna the scribe, and the elders of the priests, covered with sackcloth, to Isaiah the prophet, the son of Amoz.",
      "M": "He sent Eliakim the palace administrator, Shebna the royal secretary, and the senior priests — all of them covered in sackcloth — to the prophet Isaiah son of Amoz.",
      "T": "He dispatched Eliakim the palace administrator, Shebna the royal secretary, and the senior priests — all wrapped in sackcloth — to the prophet Isaiah son of Amoz."
    },
    "3": {
      "L": "And they said to him: Thus says Hezekiah — This day is a day of distress and of rebuke and of contempt; for the children have come to the point of birth, and there is no strength to bring forth.",
      "M": "They said to him: 'Thus says Hezekiah: This day is a day of distress, rebuke, and disgrace. We are like a woman in labor who has no strength to deliver.'",
      "T": "They said to him: 'This is Hezekiah's word: Today is a day of catastrophe, of rebuke, of contempt. We are like a woman who has reached the birth canal with no strength left to push.'"
    },
    "4": {
      "L": "It may be the LORD your God will hear the words of Rabshakeh, whom the king of Assyria his master has sent to mock the living God, and will rebuke the words which the LORD your God has heard; therefore lift up your prayer for the remnant that is left.",
      "M": "Perhaps the LORD your God will hear the words of Rabshakeh, whom the king of Assyria his master sent to mock the living God, and will rebuke those words. The LORD your God has heard them — so lift up a prayer for the remnant that survives.",
      "T": "Perhaps Yahweh your God has heard every insult Rabshakeh hurled against the living God on his master's orders — and will answer those words with judgment. He is your God; lift up your prayer for the few who still remain."
    },
    "5": {
      "L": "So the servants of King Hezekiah came to Isaiah.",
      "M": "So the servants of King Hezekiah came to Isaiah.",
      "T": "The servants of King Hezekiah came to Isaiah."
    },
    "6": {
      "L": "And Isaiah said to them: Thus shall you say to your master — Thus says the LORD: Do not be afraid of the words you have heard, with which the servants of the king of Assyria have blasphemed me.",
      "M": "Isaiah said to them: 'Say this to your master: Thus says the LORD — Do not be afraid of the words you have heard, with which the servants of the king of Assyria have reviled me.'",
      "T": "Isaiah told them: 'Tell your master this — Yahweh says: Do not be afraid of the words that have reached you, the insults the servants of Assyria's king have hurled at me.'"
    },
    "7": {
      "L": "Behold, I will put a spirit in him, and he will hear a report and return to his own land, and I will cause him to fall by the sword in his own land.",
      "M": "Watch — I will put a disturbing spirit in him so that he hears a rumor and returns to his own land, and I will bring him down by the sword in his own land.",
      "T": "Watch what I do: I will send a disturbing report into his ear, and he will turn back to his own land — and there I will bring him down by the sword."
    },
    "8": {
      "L": "So Rabshakeh returned and found the king of Assyria fighting against Libnah, for he had heard that the king had moved on from Lachish.",
      "M": "Rabshakeh turned back and found the king of Assyria fighting at Libnah, for he had heard that the king had moved on from Lachish.",
      "T": "Rabshakeh withdrew and found the king of Assyria engaged at Libnah — the king had moved up from Lachish."
    },
    "9": {
      "L": "And he heard concerning Tirhakah king of Cush: He has come out to fight against you. And when he heard it, he sent messengers to Hezekiah, saying:",
      "M": "Then word reached Sennacherib about Tirhakah king of Cush: 'He has marched out to fight you.' When Sennacherib heard it, he sent messengers again to Hezekiah, saying:",
      "T": "Then word reached him about Tirhakah king of Cush: 'He has come out to fight you.' When Sennacherib heard it, he sent another message to Hezekiah:"
    },
    "10": {
      "L": "Thus shall you say to Hezekiah king of Judah: Do not let your God, in whom you trust, deceive you, saying, Jerusalem will not be given into the hand of the king of Assyria.",
      "M": "'Say this to Hezekiah king of Judah: Do not let your God, in whom you are trusting, deceive you by saying that Jerusalem will not be given into the hand of the king of Assyria.'",
      "T": "'Tell Hezekiah king of Judah: Do not let the God you are trusting fool you with the promise that Jerusalem will be spared from the king of Assyria.'"
    },
    "11": {
      "L": "Behold, you have heard what the kings of Assyria have done to all the lands, devoting them to destruction; and shall you be delivered?",
      "M": "'You have certainly heard what the kings of Assyria have done to every land — they destroyed them completely. Do you think you alone will be delivered?'",
      "T": "'You have heard what Assyria's kings have done to every land they touched — total destruction. Do you imagine you will escape?'"
    },
    "12": {
      "L": "Have the gods of the nations delivered them which my fathers destroyed — Gozan, and Haran, and Rezeph, and the people of Eden who were in Telassar?",
      "M": "'Did the gods of the nations rescue the peoples my fathers destroyed — Gozan, Haran, Rezeph, and the people of Eden who were in Telassar?'",
      "T": "'Where were the gods of those nations when my fathers destroyed them — Gozan, Haran, Rezeph, the people of Eden in Telassar? Not one of their gods did a thing.'"
    },
    "13": {
      "L": "Where is the king of Hamath, and the king of Arphad, and the king of the city of Sepharvaim, of Hena, and of Ivah?",
      "M": "'Where is the king of Hamath now? The king of Arphad? The king of the city of Sepharvaim, of Hena, and of Ivah?'",
      "T": "'Where is the king of Hamath now? Where is the king of Arphad? Where are the kings of Sepharvaim, Hena, and Ivah?'"
    },
    "14": {
      "L": "And Hezekiah received the letter from the hand of the messengers, and read it; and Hezekiah went up to the house of the LORD, and spread it before the LORD.",
      "M": "Hezekiah received the letter from the messengers and read it. Then he went up to the house of the LORD and spread it out before the LORD.",
      "T": "Hezekiah took the letter from the messengers and read it. Then he went up to the house of Yahweh and spread it open before Yahweh."
    },
    "15": {
      "L": "And Hezekiah prayed to the LORD, saying:",
      "M": "And Hezekiah prayed to the LORD:",
      "T": "And Hezekiah prayed to Yahweh:"
    },
    "16": {
      "L": "O LORD of hosts, God of Israel, who is enthroned above the cherubim, you are the God, even you alone, of all the kingdoms of the earth; you have made heaven and earth.",
      "M": "O LORD of hosts, God of Israel, enthroned above the cherubim — you alone are God over all the kingdoms of the earth. You made heaven and earth.",
      "T": "'O Yahweh of hosts, God of Israel, enthroned above the cherubim — you, you alone, are God over all the kingdoms of the earth. You made heaven and earth."
    },
    "17": {
      "L": "Incline your ear, O LORD, and hear; open your eyes, O LORD, and see; and hear all the words of Sennacherib, who has sent them to mock the living God.",
      "M": "Incline your ear, LORD, and hear; open your eyes, LORD, and see; hear all the words Sennacherib has sent to mock the living God.",
      "T": "Bend down, Yahweh — hear us. Open your eyes and see. Listen to every word Sennacherib has sent to insult the living God."
    },
    "18": {
      "L": "Truly, LORD, the kings of Assyria have laid waste all the nations and their lands,",
      "M": "It is true, LORD, that the kings of Assyria have devastated all the nations and their lands,",
      "T": "It is true, Yahweh — Assyria's kings have destroyed nation after nation, land after land,"
    },
    "19": {
      "L": "and have cast their gods into the fire; for they were no gods, but the work of men's hands, wood and stone; therefore they destroyed them.",
      "M": "and thrown their gods into the fire. For they were not gods at all, only things men made with their hands — wood and stone — so they were able to destroy them.",
      "T": "and thrown their gods into the fire — because those so-called gods were nothing, things men made from wood and stone; of course they could be burned."
    },
    "20": {
      "L": "So now, O LORD our God, save us from his hand, so that all the kingdoms of the earth may know that you, LORD, are God alone.",
      "M": "So now, LORD our God, deliver us from his hand, so that all the kingdoms of the earth may know that you, LORD, are God and you alone.'",
      "T": "So now, Yahweh our God, rescue us from his grip — so that every kingdom on earth will know that you, Yahweh, are God, and you alone.'"
    },
    "21": {
      "L": "Then Isaiah the son of Amoz sent to Hezekiah, saying: Thus says the LORD, the God of Israel — Because you have prayed to me about Sennacherib king of Assyria,",
      "M": "Then Isaiah son of Amoz sent word to Hezekiah: 'Thus says the LORD, the God of Israel: Because you have prayed to me about Sennacherib king of Assyria,'",
      "T": "Then Isaiah son of Amoz sent a message to Hezekiah: 'Yahweh, the God of Israel, says this: Your prayer about Sennacherib king of Assyria has been heard."
    },
    "22": {
      "L": "this is the word that the LORD has spoken concerning him: She despises you, she laughs you to scorn — the virgin daughter of Zion; she wags her head behind you — the daughter of Jerusalem.",
      "M": "this is the word the LORD has spoken concerning him: 'The virgin daughter of Zion despises you and laughs you to scorn; daughter Jerusalem shakes her head at your retreating back.",
      "T": "'This is what Yahweh says about him:\nThe virgin daughter of Zion despises you —\nshe laughs you to scorn.\nDaughter Jerusalem shakes her head as you flee."
    },
    "23": {
      "L": "Whom have you mocked and blasphemed? Against whom have you raised your voice and lifted your eyes on high? Against the Holy One of Israel.",
      "M": "Whom did you mock and blaspheme? Against whom did you raise your voice and lift your eyes with pride? Against the Holy One of Israel.",
      "T": "Whom did you insult? Whom did you blaspheme?\nAgainst whom did you raise your voice,\nlifting your eyes high in arrogance?\nAgainst the Holy One of Israel."
    },
    "24": {
      "L": "By your servants you have mocked the Lord, and said: With the multitude of my chariots I have climbed the heights of the mountains, the far sides of Lebanon; I will cut down its tall cedars and its finest cypresses; I will come to its utmost peak, its forest thickness.",
      "M": "By your servants you mocked the Lord and boasted: 'With my vast forces of chariots I have scaled the mountain heights, the far slopes of Lebanon; I have felled its tallest cedars and finest cypresses; I reached its highest summit, its deepest forests.'",
      "T": "Through your servants you mocked the Lord — you boasted:\n'With my vast chariots I climbed the peaks of the mountains,\nthe far reaches of Lebanon.\nI cut down its tallest cedars, its finest cypresses.\nI reached the summit of its heights,\nthe thickest depths of its forests.'"
    },
    "25": {
      "L": "I dug wells and drank water; with the sole of my feet I dried up all the rivers of Egypt.",
      "M": "I dug wells and drank water; with the tread of my feet I dried up all the streams of Egypt.",
      "T": "'I dug wells and drank wherever I pleased;\nwith the sole of my foot I drained\nevery stream in Egypt.'"
    },
    "26": {
      "L": "Have you not heard? From long ago I shaped it; from ancient times I formed it; now I have brought it to pass, that fortified cities should be laid in ruins.",
      "M": "Have you not heard? I planned this long ago; in ancient times I formed it; now I have brought it to pass, that you should turn fortified cities into heaps of ruins.",
      "T": "'Have you not heard?\nLong ago I drew up this plan;\nI formed it in ancient days.\nNow I have carried it out —\nyou are only the instrument\nby which I reduce fortified cities to rubble.'"
    },
    "27": {
      "L": "So their inhabitants were of little strength, they were dismayed and ashamed; they were like plants of the field and tender grass, like grass on the rooftops and grain scorched before it is grown up.",
      "M": "So their inhabitants had little strength; they were shattered and ashamed; they were like plants of the field, like tender shoots, like grass on the rooftops — blighted before it could grow.",
      "T": "'Their people had no real strength —\nshattered, humiliated,\nlike field plants, like tender shoots,\nlike rooftop grass that scorches before it can grow,\nblasted before it reaches its height.'"
    },
    "28": {
      "L": "But I know your dwelling place, and your going out and your coming in, and your raging against me.",
      "M": "But I know your dwelling place, your going out and coming in, and your rage against me.",
      "T": "'But I know where you live.\nI know your coming and going.\nI know your raging against me.'"
    },
    "29": {
      "L": "Because your raging against me and your arrogance have come up into my ears, I will put my hook in your nose and my bridle on your lips, and I will turn you back by the way by which you came.",
      "M": "Because your rage against me and your arrogance have reached my ears, I will put my hook through your nose and my bit between your lips, and I will send you back the way you came.",
      "T": "'Because your raging and your insolence\nhave reached my ears,\nI will put my hook in your nose\nand my bridle between your lips —\nand drag you back the way you came.'"
    },
    "30": {
      "L": "And this shall be the sign for you: This year you shall eat what grows of itself, and in the second year what springs from that; but in the third year sow and reap, and plant vineyards, and eat their fruit.",
      "M": "And this will be the sign for you: This year you will eat what grows on its own, and next year what springs up from that; but in the third year you will sow and reap, plant vineyards and eat their fruit.",
      "T": "'And this is your sign:\nThis year you eat what grows wild;\nnext year, what springs up on its own.\nBut the third year — sow and reap,\nplant vineyards, eat their fruit again.'"
    },
    "31": {
      "L": "And the surviving remnant of the house of Judah shall again take root downward and bear fruit upward;",
      "M": "And the remnant of the house of Judah that has escaped will once more take root downward and bear fruit upward —",
      "T": "'The surviving remnant of the house of Judah\nwill take root again in the soil\nand bear fruit toward the sky —'"
    },
    "32": {
      "L": "for out of Jerusalem shall go forth a remnant, and out of Mount Zion those who escape. The zeal of the LORD of hosts will do this.",
      "M": "for a remnant will go out from Jerusalem, and survivors from Mount Zion. The zeal of the LORD of hosts will accomplish this.",
      "T": "'for from Jerusalem a remnant will come forth,\na company of survivors from Mount Zion.\nThe zeal of Yahweh of hosts will bring this to pass.'"
    },
    "33": {
      "L": "Therefore thus says the LORD concerning the king of Assyria: He shall not come into this city, nor shoot an arrow there, nor advance on it with a shield, nor cast up a siege ramp against it.",
      "M": "Therefore thus says the LORD concerning the king of Assyria: He will not enter this city, nor shoot an arrow into it, nor advance on it with a shield, nor build a siege ramp against it.",
      "T": "Therefore Yahweh says about the king of Assyria:\n'He will not set foot in this city.\nHe will not fire a single arrow into it.\nHe will not come at it with a shield.\nHe will not build a siege ramp against it.'"
    },
    "34": {
      "L": "By the way that he came, by the same he shall return, and he shall not come into this city, declares the LORD.",
      "M": "He will go back the same road he came. He will not enter this city, declares the LORD.",
      "T": "'By the road he came, by that road he goes back. He will not enter this city.' Yahweh's own word."
    },
    "35": {
      "L": "For I will defend this city to save it, for my own sake and for the sake of my servant David.",
      "M": "For I will defend this city and save it — for my own sake and for the sake of my servant David.",
      "T": "'I will defend this city and save it — for my own sake and for the sake of my servant David.'"
    },
    "36": {
      "L": "Then the angel of the LORD went out and struck down a hundred and eighty-five thousand in the camp of the Assyrians. And when they arose early in the morning, behold, all of them were dead corpses.",
      "M": "Then the angel of the LORD went out and struck down one hundred and eighty-five thousand in the Assyrian camp. When the survivors arose early in the morning, there were corpses everywhere.",
      "T": "That night the angel of Yahweh went out and struck down a hundred and eighty-five thousand in the Assyrian camp. When the survivors woke at dawn, there were nothing but dead bodies everywhere."
    },
    "37": {
      "L": "Then Sennacherib king of Assyria departed and returned and dwelt at Nineveh.",
      "M": "Then Sennacherib king of Assyria broke camp, returned home, and settled in Nineveh.",
      "T": "Sennacherib king of Assyria broke camp and went home to Nineveh."
    },
    "38": {
      "L": "And it came to pass, as he was worshiping in the house of Nisroch his god, that his sons Adrammelech and Sharezer struck him down with the sword, and they escaped to the land of Ararat. And his son Esarhaddon reigned in his place.",
      "M": "While he was worshiping in the temple of his god Nisroch, his sons Adrammelech and Sharezer cut him down with the sword and escaped to the land of Ararat. His son Esarhaddon became king in his place.",
      "T": "Then while he was at worship in the temple of his god Nisroch, his own sons Adrammelech and Sharezer killed him with the sword and fled to Ararat. His son Esarhaddon succeeded him as king."
    }
  },
  "38": {
    "1": {
      "L": "In those days Hezekiah was sick unto death. And Isaiah the prophet, the son of Amoz, came to him and said to him: Thus says the LORD — Set your house in order, for you shall die and not live.",
      "M": "In those days Hezekiah became mortally ill. The prophet Isaiah son of Amoz came to him and said: 'Thus says the LORD: Set your house in order, for you shall die — you will not recover.'",
      "T": "In those same days Hezekiah fell deathly sick. The prophet Isaiah son of Amoz came to him and said: 'Yahweh says this: Set your house in order. You are going to die — you will not recover.'"
    },
    "2": {
      "L": "Then Hezekiah turned his face to the wall and prayed to the LORD.",
      "M": "Then Hezekiah turned his face to the wall and prayed to the LORD.",
      "T": "Hezekiah turned his face to the wall and prayed to Yahweh."
    },
    "3": {
      "L": "And said: Remember now, O LORD, I beseech you, how I have walked before you in faithfulness and with a whole heart, and have done what is good in your sight. And Hezekiah wept bitterly.",
      "M": "He prayed: 'Please, LORD, remember how I have walked before you in faithfulness and with a whole heart, and have done what is good in your sight.' And Hezekiah wept bitterly.",
      "T": "He prayed: 'Remember, Yahweh — please — how I have walked before you in truth and with an undivided heart, and done what is good in your eyes.' And Hezekiah wept and wept."
    },
    "4": {
      "L": "Then the word of the LORD came to Isaiah, saying:",
      "M": "Then the word of the LORD came to Isaiah:",
      "T": "Then the word of Yahweh came to Isaiah:"
    },
    "5": {
      "L": "Go and say to Hezekiah: Thus says the LORD, the God of your father David — I have heard your prayer, I have seen your tears; behold, I will add fifteen years to your days.",
      "M": "Go and tell Hezekiah: This is what the LORD says, the God of your father David: I have heard your prayer; I have seen your tears. I will add fifteen years to your life.",
      "T": "'Go, tell Hezekiah: Yahweh says — I, the God of your father David — I have heard your prayer. I have seen your tears. I am adding fifteen years to your life.'"
    },
    "6": {
      "L": "And I will deliver you and this city from the hand of the king of Assyria, and I will defend this city.",
      "M": "I will rescue you and this city from the hand of the king of Assyria, and I will defend this city.",
      "T": "'I will rescue you and this city from the king of Assyria. I will defend this city.'"
    },
    "7": {
      "L": "And this shall be the sign to you from the LORD, that the LORD will do this thing that he has promised:",
      "M": "And this will be the sign from the LORD to you that the LORD will carry out what he has said:",
      "T": "'And this is the sign Yahweh gives you to confirm that he will do what he has promised:'"
    },
    "8": {
      "L": "Behold, I will make the shadow on the steps of Ahaz, which has gone down with the sun, turn back ten steps. So the sun turned back ten steps on the steps by which it had gone down.",
      "M": "I will make the shadow on the sundial of Ahaz — the shadow that has already gone down ten steps — go back ten steps. And the sun reversed itself on the steps by ten degrees.",
      "T": "'I will reverse the shadow on the sundial of Ahaz — those ten steps it has already descended — ten steps backward.' And the sun went back the ten steps it had gone down."
    },
    "9": {
      "L": "The writing of Hezekiah king of Judah, after he had been sick and had recovered from his sickness:",
      "M": "The writing of Hezekiah king of Judah, composed after his illness, when he recovered.",
      "T": "The writing of Hezekiah king of Judah — composed after his illness, when he recovered:"
    },
    "10": {
      "L": "I said: In the prime of my days I must depart; I am consigned to the gates of Sheol for the remainder of my years.",
      "M": "I said: In the prime of my life I must enter the gates of Sheol, deprived of the rest of my years.",
      "T": "I said:\nIn the noontide of my years I must go —\nconsigned to the gates of Sheol,\nmy remaining years stripped away."
    },
    "11": {
      "L": "I said: I shall not see the LORD, the LORD, in the land of the living; I shall look on man no more among the inhabitants of the world.",
      "M": "I said: I will not see the LORD again, even the LORD, in the land of the living; I will gaze on no human face again among those who dwell in the world.",
      "T": "I said:\nI will never see Yahweh again —\nnever, in the land of the living.\nI will look on human faces no more\namong those who walk in this world."
    },
    "12": {
      "L": "My dwelling is plucked up and removed from me like a shepherd's tent; I have cut off my life like a weaver; he cuts me off from the loom; from day to night you bring me to an end.",
      "M": "My home has been pulled up and taken from me like a shepherd's tent; I have rolled up my life like a weaver; he cuts me from the loom. From day to night you bring me to an end.",
      "T": "My home is struck and gone —\npulled up like a shepherd's tent.\nLike a weaver I have rolled up my life;\nhe cuts me from the loom.\nFrom morning to night you are finishing me."
    },
    "13": {
      "L": "I waited until morning; but like a lion he was breaking all my bones; from day to night you bring me to an end.",
      "M": "I held on through the night, but like a lion he was crushing all my bones. From day to night you bring me to an end.",
      "T": "I endured till morning —\nbut like a lion he was grinding my bones.\nFrom morning to night you were finishing me."
    },
    "14": {
      "L": "Like a crane or a swallow, so did I chatter; I moaned like a dove; my eyes grew weary from looking upward. O LORD, I am oppressed; stand surety for me.",
      "M": "Like a swift or a crane, so did I chatter; I moaned like a dove; my eyes grew weary gazing upward. LORD, I am in distress — be my pledge of safety.",
      "T": "Like a swift, like a crane —\nthat was the sound of my crying.\nI moaned like a dove.\nMy eyes grew weary straining upward.\nYahweh, I am crushed — be my surety."
    },
    "15": {
      "L": "What shall I say? He has spoken to me, and he himself has done it. I will walk humbly all my years because of the bitterness of my soul.",
      "M": "What can I say? He spoke — and he himself did it. I will walk slowly all my years, weighted down by the bitterness of my soul.",
      "T": "What can I say?\nHe spoke — and he himself brought it to pass.\nI will walk quietly, weighed down,\nall my years under the bitterness of my soul."
    },
    "16": {
      "L": "O Lord, by these things men live, and in all these things is the life of my spirit; so restore me to health and make me live.",
      "M": "O Lord, by such things people live, and through all these things is the life of my spirit. So restore my health and let me live.",
      "T": "O Lord, it is by such things —\nthese hard things — that people truly live.\nIn all of this is the life of my spirit.\nRestore me; let me live."
    },
    "17": {
      "L": "Behold, for my welfare I had great bitterness; but you held back my life from the pit of destruction, for you have cast all my sins behind your back.",
      "M": "See — it was for my welfare that I suffered such bitter anguish; but you held my life back from the pit of destruction, and you have cast all my sins behind your back.",
      "T": "I see it now:\nthat bitterness was for my good.\nYou pulled my life back from the pit —\nyou loved me enough to do that —\nand you have thrown every one of my sins\nbehind your back, where you cannot see them."
    },
    "18": {
      "L": "For Sheol cannot thank you; death cannot praise you; those who go down to the pit cannot hope in your faithfulness.",
      "M": "For Sheol cannot thank you; death cannot praise you; those who descend to the pit cannot hope in your faithfulness.",
      "T": "For Sheol cannot praise you.\nDeath cannot give you thanks.\nThose who go down to the pit\ncannot hope in your faithfulness."
    },
    "19": {
      "L": "The living, the living, they give you thanks, as I do this day; the father makes known your faithfulness to the children.",
      "M": "Only the living, the living, give you thanks — as I do today. A father makes known your faithfulness to his children.",
      "T": "The living — only the living — give you thanks.\nAs I do today.\nA father tells his children of your faithfulness."
    },
    "20": {
      "L": "The LORD will save me, and we will play my songs on stringed instruments all the days of our life in the house of the LORD.",
      "M": "The LORD was ready to save me. And we will play my songs of praise to stringed instruments all the days of our life in the house of the LORD.",
      "T": "Yahweh was ready to save me —\nand we will sing my praise songs\nwith strings ringing out\nall the days of our lives\nin the house of Yahweh."
    },
    "21": {
      "L": "Now Isaiah had said, Let them take a cake of figs and apply it as a poultice on the boil, that he may recover.",
      "M": "Now Isaiah had said, 'Let them take a pressed cake of figs and apply it as a poultice on the sore, and he will recover.'",
      "T": "Now Isaiah had said: 'Take a poultice of pressed figs and lay it on the sore — he will recover.'"
    },
    "22": {
      "L": "Hezekiah also had said, What shall be the sign that I shall go up to the house of the LORD?",
      "M": "And Hezekiah had asked, 'What will be the sign that I shall go up to the house of the LORD?'",
      "T": "And Hezekiah had asked: 'What will be the sign that I can go up to the house of Yahweh?'"
    }
  },
  "39": {
    "1": {
      "L": "At that time Merodach-baladan the son of Baladan, king of Babylon, sent letters and a present to Hezekiah, for he had heard that he had been sick and had recovered.",
      "M": "At that time Merodach-baladan son of Baladan, king of Babylon, sent letters and a gift to Hezekiah — because he had heard that Hezekiah had been sick and had recovered.",
      "T": "At that time Merodach-baladan son of Baladan, king of Babylon, sent envoys with letters and a gift to Hezekiah. He had heard that Hezekiah had been sick and recovered."
    },
    "2": {
      "L": "And Hezekiah was glad because of them, and he showed them the house of his treasures — the silver, the gold, the spices, and the precious ointment, and his whole armory, and everything found in his storehouses; there was nothing in his house or in all his domain that Hezekiah did not show them.",
      "M": "Hezekiah received them gladly and showed them the storehouse of his treasures — the silver, the gold, the spices, the fine oil, his entire armory, everything found in his storerooms. There was nothing in his palace or in all his realm that Hezekiah did not show them.",
      "T": "Hezekiah welcomed them eagerly and showed them everything — his treasury, his silver and gold, his spices and precious oils, his whole armory, everything in all his storehouses. There was not a single thing in his palace or anywhere in his kingdom that he did not put on display."
    },
    "3": {
      "L": "Then came Isaiah the prophet to King Hezekiah and said to him: What did these men say, and from where did they come to you? And Hezekiah said: They came from a far country, to me, from Babylon.",
      "M": "Then the prophet Isaiah came to King Hezekiah and asked him: 'What did these men say, and where did they come from?' Hezekiah replied: 'They came from a far country — from Babylon.'",
      "T": "Then the prophet Isaiah came to King Hezekiah and asked: 'What did those men say? Where did they come from?' Hezekiah answered: 'They came from far away — from Babylon.'"
    },
    "4": {
      "L": "Then he said: What have they seen in your house? And Hezekiah answered: They have seen everything in my house; there is nothing in my storehouses that I did not show them.",
      "M": "Isaiah asked: 'What have they seen in your palace?' Hezekiah answered: 'They have seen everything. There is nothing in my storehouses that I did not show them.'",
      "T": "'What have they seen in your palace?' Isaiah pressed him. 'Everything,' Hezekiah said. 'There is nothing in my storehouses I did not show them.'"
    },
    "5": {
      "L": "Then Isaiah said to Hezekiah: Hear the word of the LORD of hosts:",
      "M": "Then Isaiah said to Hezekiah: 'Hear the word of the LORD of hosts:'",
      "T": "Then Isaiah said: 'Hear the word of Yahweh of hosts:'"
    },
    "6": {
      "L": "Behold, days are coming when all that is in your house, and what your fathers have stored up until this day, shall be carried off to Babylon; nothing shall be left, says the LORD.",
      "M": "'Watch — days are coming when everything in your palace, everything your ancestors stored up until today, will be carried off to Babylon. Nothing will be left, declares the LORD.'",
      "T": "'Days are coming when everything in this palace — everything your ancestors accumulated down to this very day — will be carried off to Babylon. Nothing will be left. Yahweh says so.'"
    },
    "7": {
      "L": "And some of your own sons, who will issue from you, whom you will father, shall be taken away, and they shall be officials in the palace of the king of Babylon.",
      "M": "And some of your own sons — your own descendants, whom you will father — will be taken away and serve as court officials in the palace of the king of Babylon.",
      "T": "'And some of the sons born to you — your own flesh — will be taken away and become servants in the palace of Babylon's king.'"
    },
    "8": {
      "L": "Then Hezekiah said to Isaiah: The word of the LORD that you have spoken is good. For he said: There will be peace and security in my days.",
      "M": "Then Hezekiah said to Isaiah: 'The word of the LORD that you have spoken is good.' And he added: 'At least there will be peace and security during my own lifetime.'",
      "T": "Hezekiah said to Isaiah: 'The word of Yahweh you have spoken is good.' And then he added: 'At least there will be peace and security in my own days.'"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 37–39 written.')

if __name__ == '__main__':
    main()
