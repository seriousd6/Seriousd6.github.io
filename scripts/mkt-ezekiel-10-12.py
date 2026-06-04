"""
MKT Ezekiel chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-10-12.py

Translation decisions (carrying forward all conventions from mkt-ezekiel-7-9.py):

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T, especially for the recognition
  formula and divine-speech introductions. Maintains convention from EZK-1b, EZK-2a.

- H136 + H3069 (אֲדֹנָי יְהוִה / Adonai-Yahweh): "Lord GOD" in L/M (small-caps GOD);
  "Lord Yahweh" in T. The combined form dominates Ezekiel's oracle style.

- H3519 (כָּבוֹד / glory): "glory" in all three tiers. The departure sequence begun in 9:3
  (glory moves to threshold) continues through ch 10 and culminates in 11:23.
  T tier surfaces the theological weight of each movement: threshold (9:3), above cherubim
  (10:4), east gate (10:19), mountain east of city (11:23 = Mount of Olives).

- H3742 (כְּרוּב / cherub): "cherub/cherubim" throughout. The chariot-throne creatures of
  ch 1 are here explicitly identified as cherubim (10:15, 10:20). Chapter 1 called them
  "living creatures" (חַיּוֹת); Ezekiel's later theology names them directly.

- H212 (אוֹפַן / wheel): "wheel/wheels" throughout — the chariot wheels that move in unity
  with the cherubim, animated by their spirit (10:17). The cry "O wheel!" (10:13) renders
  H1534 (גַּלְגַּל / galgal, "whirling wheel"), an onomatopoeic term.

- H7307 (רוּחַ / Spirit): "Spirit" (capitalized) throughout chs 10–11 — always divine agency
  (10:17 animating the wheels; 11:1, 11:5, 11:24 lifting and possessing Ezekiel). No
  ambiguity in this passage. Consistent with EZK-2a convention.

- The face discrepancy (10:14 vs 1:10): In 1:10 the four faces are man/lion/ox/eagle.
  In 10:14 the ox is replaced by "a cherub." This is widely read as a retrospective
  clarification: the "ox face" of the living creatures is the face of a cherub. T tier
  names this connection explicitly. L and M translate the text as given.

- H3820/H68 (לֵב/לֵבָב / heart; אֶבֶן / stone): The promise of 11:19 — stone heart removed,
  heart of flesh (H1320 בָּשָׂר) given — parallels 36:26 and Jer 31:33. This is Ezekiel's
  core new-covenant promise. T tier surfaces the full theological significance and the
  parallel with Jeremiah. "Heart of flesh" = responsive, pliable, alive to God (contrast
  stone = hard, unresponsive, dead to God).

- H4853 (מַשָּׂא / burden/oracle): Rendered "oracle" in M/T for 12:10 — "this burden concerns
  the prince" = this oracle is about Zedekiah. The word carries prophetic pronouncement
  weight. L preserves "burden" per the Hebrew double-meaning (a burden carried = a word
  that must be delivered).

- Zedekiah typology (12:12-13): The sign-act of Ezekiel covering his face and going through
  a hole in the wall (12:5-7) is explicitly applied to the prince (vv. 10-13). The detail
  "he will not see the land" (12:13) and "he shall die there" without seeing Babylon —
  fulfilled in 2 Kgs 25:7: Nebuchadnezzar blinded Zedekiah at Riblah, then brought him
  to Babylon where he died. T tier names this fulfillment explicitly.

- 11:23 (Mount of Olives): "The mountain east of the city" is the Mount of Olives. T tier
  names it. This geographic detail carries enormous canonical weight — the same mountain
  from which, in Zech 14 and the NT, the LORD will return.

- H1540 (גָּלָה / exile/captivity): "captivity" in L/M; "exile" in T where the word flows
  better in English narrative prose.

- The "rebellious house" refrain (chs 11–12): H4805 (מֶרִי / rebellion/stubborn). "Rebellious
  house" in all tiers — Ezekiel's signature label for Israel.

- Proverb of delay (12:22-28): Two versions of the same fatalist theology: (a) "the days
  are prolonged and every vision fails" — vision as prophecy never comes true; (b) "the
  vision is for distant times." God refutes both. T tier names the psychological strategy
  of each proverb: the first denies prophetic truth entirely; the second concedes truth
  but postpones it indefinitely.

- Aspect notes: Imperatives throughout chs 10–12 are pointed; aorist-aspect oracles in
  ch 12 (LXX aorist subjunctive in key vv.) are translated as completed or imminent future
  in English. The sign-acts of ch 12 are narrated in past tense (perfect aspect) in 12:7.
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

EZEKIEL = {
  "10": {
    "1": {
      "L": "Then I looked, and behold: in the firmament that was over the head of the cherubims, as it were a sapphire stone, there appeared above them the likeness of a throne.",
      "M": "I looked, and above the cherubim in the expanse over their heads there appeared, as it were, a sapphire stone throne above them.",
      "T": "I looked up: above the cherubim, in the great vault overhead, hovered what appeared to be a throne — sapphire-blue, blazing with clarity. The chariot-throne of chapter one stood over the temple."
    },
    "2": {
      "L": "And he spoke to the man clothed in linen and said: Go in between the wheels, even under the cherub, and fill thine hand with coals of fire from between the cherubims, and scatter them over the city. And he went in in my sight.",
      "M": "He spoke to the man clothed in linen: 'Go in among the wheels beneath the cherub; fill your hands with burning coals from between the cherubim and scatter them over the city.' He went in before my eyes.",
      "T": "He commanded the man in linen: Go into the space between the wheels, beneath the cherub. Scoop up burning coals from between the cherubim and scatter them over the city. Fire from the divine chariot itself was to fall on Jerusalem. The man went in — I watched him go."
    },
    "3": {
      "L": "Now the cherubims stood on the right side of the house when the man went in; and the cloud filled the inner court.",
      "M": "The cherubim were standing on the south side of the temple when the man went in, and the cloud filled the inner court.",
      "T": "The cherubim were stationed on the south side of the temple as the man entered. The cloud — the visible sign of the divine presence — filled the inner court."
    },
    "4": {
      "L": "Then the glory of the LORD went up from the cherub and stood over the threshold of the house; and the house was filled with the cloud, and the court was full of the brightness of the LORD's glory.",
      "M": "The glory of the LORD rose from the cherub and moved to the threshold of the temple. The temple filled with cloud, and the court blazed with the brightness of the LORD's glory.",
      "T": "The glory lifted from the cherub-throne and moved to the threshold — a first step outward, away from the inner sanctuary. The entire temple filled with cloud. The court blazed with the brightness of Yahweh's glory. The departure had begun."
    },
    "5": {
      "L": "And the sound of the wings of the cherubims was heard even to the outer court, as the voice of God Almighty when he speaks.",
      "M": "The sound of the cherubim's wings was heard even in the outer court, like the voice of God Almighty when he speaks.",
      "T": "The sound of those wings carried all the way to the outer court — a sound like the voice of El Shaddai himself. Nothing in creation compares to it."
    },
    "6": {
      "L": "And it came to pass, when he commanded the man clothed in linen, saying: Take fire from between the wheels, from between the cherubims; then he went in and stood beside the wheels.",
      "M": "When he commanded the man in linen, 'Take fire from between the wheels, from between the cherubim,' he went in and stood beside the wheels.",
      "T": "When the command went out to the man in linen — Take fire from between the wheels, from within the cherubim — he walked in and took his position at the wheels."
    },
    "7": {
      "L": "And one cherub stretched forth his hand from between the cherubims unto the fire that was between the cherubims, and took thereof, and put it into the hands of him that was clothed in linen; who took it and went out.",
      "M": "One of the cherubim reached in from among the cherubim toward the fire between them, took some, and placed it in the hands of the man in linen; he received it and went out.",
      "T": "One of the cherubim reached into the fire burning between them, took a handful of those blazing coals, and placed them in the hands of the man in linen. He received them — and went out to do what he was sent to do."
    },
    "8": {
      "L": "And there appeared in the cherubims the form of a man's hand under their wings.",
      "M": "There appeared beneath the wings of the cherubim the form of a human hand.",
      "T": "Beneath each wing of the cherubim, a human hand was visible. The creatures were not purely animal or purely divine — they bore the form of human hands as well. Three orders in one body."
    },
    "9": {
      "L": "And when I looked, behold the four wheels by the cherubims, one wheel by one cherub and another wheel by another cherub; and the appearance of the wheels was as the colour of a beryl stone.",
      "M": "I looked and saw four wheels beside the cherubim — one wheel beside each cherub. The wheels had the colour of beryl stone.",
      "T": "I took in the full scene: four wheels, each one stationed at a cherub. They shone with the colour of beryl — blue-green and translucent, like light held inside mineral."
    },
    "10": {
      "L": "And as for their appearances, they four had one likeness, as if a wheel had been in the midst of a wheel.",
      "M": "As for their appearance, all four looked alike — as if a wheel were set inside a wheel.",
      "T": "All four wheels had the same design: a wheel set within a wheel — a gyroscopic construction able to turn in any direction without reorienting the whole."
    },
    "11": {
      "L": "When they went, they went upon their four sides; they turned not as they went; but to the place whither the head looked they followed it; they turned not as they went.",
      "M": "When they moved, they could go in any of the four directions without turning — wherever the leading cherub faced, all followed without pivoting.",
      "T": "They moved in four directions simultaneously — or in any one of them — without ever needing to wheel around. The head determined direction; all followed instantly. No pivot, no hesitation."
    },
    "12": {
      "L": "And their whole body, and their backs, and their hands, and their wings, and the wheels were full of eyes round about, even the wheels that they four had.",
      "M": "Their entire bodies — backs, hands, wings, and the four wheels — were covered all around with eyes.",
      "T": "Every surface alive with eyes. Backs, hands, wings, and all four wheels — covered in eyes looking in every direction at once. Nothing could approach unseen. Nothing could hide."
    },
    "13": {
      "L": "As for the wheels, it was cried unto them in my hearing: O wheel.",
      "M": "As for the wheels, I heard them called by name: 'O whirling wheel!'",
      "T": "As I listened, the wheels were directly addressed — called out by name: O galgal, O whirling wheel! The word is the sound of turning, and the chariot's motion answered."
    },
    "14": {
      "L": "And every one had four faces: the first face was the face of a cherub, and the second face was the face of a man, and the third the face of a lion, and the fourth the face of an eagle.",
      "M": "Each one had four faces: the first was the face of a cherub, the second the face of a man, the third the face of a lion, and the fourth the face of an eagle.",
      "T": "Each cherub had four faces: the face of a cherub, the face of a man, the face of a lion, the face of an eagle. In chapter one the same position was held by an ox. Here it is named directly: that ox face is a cherub's face. The two visions read each other."
    },
    "15": {
      "L": "And the cherubims were lifted up. This is the living creature that I saw by the river of Chebar.",
      "M": "The cherubim rose up. These were the living creatures I had seen by the Chebar River.",
      "T": "The cherubim rose — and I knew: these were the living creatures from the Chebar vision. The chariot-throne I had seen in Babylon was the same throne that had rested in Jerusalem's temple. What I once witnessed on foreign soil was now departing from home."
    },
    "16": {
      "L": "And when the cherubims went, the wheels went by them; and when the cherubims lifted up their wings to mount up from the earth, the same wheels also turned not from beside them.",
      "M": "When the cherubim moved, the wheels moved alongside them; when the cherubim lifted their wings to rise from the earth, the wheels did not leave their sides.",
      "T": "When the cherubim moved, the wheels moved with them. When the cherubim spread their wings to lift from the ground, the wheels rose with them — inseparable, one unified vehicle."
    },
    "17": {
      "L": "When they stood, these stood; and when they were lifted up, these lifted up themselves also; for the spirit of the living creature was in them.",
      "M": "When the cherubim stood still, the wheels stood still; when they rose, the wheels rose with them — for the spirit of the living creature was in the wheels.",
      "T": "Still when they were still. Rising when they rose. The wheels were not mechanical additions — the spirit of the living creature animated them. One life moved through all eight."
    },
    "18": {
      "L": "Then the glory of the LORD departed from off the threshold of the house and stood over the cherubims.",
      "M": "Then the glory of the LORD moved from the threshold of the temple and rested over the cherubim.",
      "T": "The glory of the LORD lifted from the threshold — that last position of reluctant withdrawal — and came to rest above the cherubim. The time had come to leave."
    },
    "19": {
      "L": "And the cherubims lifted up their wings and mounted up from the earth in my sight; when they went out, the wheels also were beside them; and every one stood at the door of the east gate of the LORD's house; and the glory of the God of Israel was over them above.",
      "M": "The cherubim spread their wings and rose from the earth before my eyes; as they moved, the wheels were alongside them. They halted at the entrance of the east gate of the LORD's house, with the glory of the God of Israel above them.",
      "T": "The cherubim spread their wings and lifted from the earth — I watched with my own eyes. The wheels rose with them. They stopped at the east gate of the LORD's temple, the glory of Israel's God blazing above them. The divine presence now stood at the gate that faced toward Babylon."
    },
    "20": {
      "L": "This is the living creature that I saw under the God of Israel by the river of Chebar; and I knew that they were the cherubims.",
      "M": "These were the living creatures I had seen beneath the God of Israel by the Chebar River, and I knew they were the cherubim.",
      "T": "I recognized them now with certainty — the living creatures from the Chebar vision. They were cherubim. The same ones. And their God was here too — and now departing."
    },
    "21": {
      "L": "Every one had four faces apiece and every one four wings; and the likeness of the hands of a man was under their wings.",
      "M": "Each had four faces and four wings, and beneath their wings was the likeness of human hands.",
      "T": "Four faces. Four wings. And beneath those wings, human hands. Every order represented: creature, human, divine — in one form."
    },
    "22": {
      "L": "And the likeness of their faces was the same faces which I saw by the river of Chebar, their appearances and themselves; they went every one straight forward.",
      "M": "The appearance of their faces was the same as the faces I had seen by the Chebar River — the same in appearance and form; they each moved straight forward.",
      "T": "Their faces — exactly as I had seen them at the Chebar. The same vision, confirmed. They moved straight ahead without turning, without hesitation."
    }
  },
  "11": {
    "1": {
      "L": "Moreover the spirit lifted me up and brought me unto the east gate of the LORD's house, which looketh eastward; and behold at the door of the gate five and twenty men; and I saw among them Jaazaniah the son of Azur and Pelatiah the son of Benaiah, princes of the people.",
      "M": "The Spirit lifted me up and brought me to the east gate of the LORD's house, which faces east. There at the entrance of the gate were twenty-five men; among them I saw Jaazaniah son of Azur and Pelatiah son of Benaiah, princes of the people.",
      "T": "The Spirit lifted me and carried me to the east gate of the LORD's temple — the gate that faces toward Babylon. Twenty-five men were gathered there. Among them I recognized Jaazaniah son of Azur and Pelatiah son of Benaiah — princes, leaders of the people."
    },
    "2": {
      "L": "Then said he unto me: Son of man, these are the men that devise mischief and give wicked counsel in this city.",
      "M": "He said to me: 'Son of man, these are the men who plan harm and give wicked counsel in this city.'",
      "T": "He said: Son of man, these are the architects of the city's ruin. They are the ones advising Jerusalem — and their counsel is poison."
    },
    "3": {
      "L": "Which say: It is not near; let us build houses. This city is the caldron and we are the flesh.",
      "M": "They are the ones who say, 'The time of judgment is not coming soon; let us build houses — this city is the caldron and we are the flesh in it.'",
      "T": "Their slogan: No need to panic. Let's build. We are the flesh in the pot — the city walls protect us, the heat preserves us. They imagined the caldron was a refuge. It was not."
    },
    "4": {
      "L": "Therefore prophesy against them, prophesy, O son of man.",
      "M": "Therefore prophesy against them — prophesy, son of man!",
      "T": "So prophesy against them. Now. Son of man — speak."
    },
    "5": {
      "L": "And the Spirit of the LORD fell upon me, and said unto me: Speak; Thus saith the LORD: Thus have ye said, O house of Israel; for I know the things that come into your mind, every one of them.",
      "M": "The Spirit of the LORD came upon me, and he said: 'Speak. Thus says the LORD: That is what you have said, house of Israel — I know every thought that rises in your mind.'",
      "T": "The Spirit of the LORD came on me. Say this — Yahweh's word: I know what you think, Israel. Every private calculation. Every line of reasoning. I have heard it all."
    },
    "6": {
      "L": "Ye have multiplied your slain in this city, and ye have filled the streets thereof with the slain.",
      "M": "You have multiplied your slain in this city and filled its streets with the dead.",
      "T": "You have filled this city with corpses — body after body, street after street. You call yourselves the preserved flesh. You have made your city a slaughterhouse."
    },
    "7": {
      "L": "Therefore thus saith the Lord GOD: Your slain whom ye have laid in the midst of it, they are the flesh and this city is the caldron; but I will bring you forth out of the midst of it.",
      "M": "Therefore this is what the Lord GOD says: The people you have slain and laid in the city — they are the flesh in the caldron; this city is the caldron. But you yourselves I will bring out of its midst.",
      "T": "The Lord Yahweh says: You got the image right — this city is a caldron. But the flesh in it is the people you murdered and left in the streets. As for you, the murderers — I will drag you out of it."
    },
    "8": {
      "L": "Ye have feared the sword; and I will bring a sword upon you, saith the Lord GOD.",
      "M": "You feared the sword, and I will bring the sword upon you, declares the Lord GOD.",
      "T": "You were afraid of the sword — so you hid inside your pot. The Lord Yahweh says: I will bring the sword to you."
    },
    "9": {
      "L": "And I will bring you out of the midst of it and deliver you into the hands of strangers, and will execute judgments among you.",
      "M": "I will bring you out of it and hand you over to foreigners, and I will execute judgment on you.",
      "T": "I will pull you out of your city and place you in foreign hands. Out of the caldron — and into judgment."
    },
    "10": {
      "L": "Ye shall fall by the sword; I will judge you in the border of Israel; and ye shall know that I am the LORD.",
      "M": "You shall fall by the sword. I will judge you at the border of Israel, and you will know that I am the LORD.",
      "T": "The sword will take you — not in your city, not in comfort. I will judge you at the border of Israel. And there you will know that I am Yahweh."
    },
    "11": {
      "L": "This city shall not be your caldron, neither shall ye be the flesh in the midst of it; I will judge you in the border of Israel.",
      "M": "This city will not be your caldron, nor will you be the flesh inside it; I will judge you at the border of Israel.",
      "T": "The caldron will not save you. This city will not be what you imagined — a refuge that preserves its contents while outsiders burn. I will judge you in the open, at the border."
    },
    "12": {
      "L": "And ye shall know that I am the LORD: for ye have not walked in my statutes, neither executed my judgments, but have done after the manners of the heathen that are round about you.",
      "M": "You will know that I am the LORD, for you have not walked in my statutes or carried out my judgments — instead you have followed the customs of the nations around you.",
      "T": "Then you will know I am Yahweh. You did not walk by my statutes. You did not follow my justice. Instead you copied the nations around you — and the nations' judgment will now be yours."
    },
    "13": {
      "L": "And it came to pass, when I prophesied, that Pelatiah the son of Benaiah died. Then fell I down upon my face and cried with a loud voice and said: Ah, Lord GOD! Wilt thou make a full end of the remnant of Israel?",
      "M": "While I was prophesying, Pelatiah son of Benaiah died. I fell on my face and cried out: 'Ah, Lord GOD! Are you going to make a complete end of the remnant of Israel?'",
      "T": "Mid-prophecy, Pelatiah son of Benaiah died. Right there, as I spoke. I fell on my face and cried: Lord Yahweh — is this the end? Will you wipe out every last survivor of Israel?"
    },
    "14": {
      "L": "Again the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me again:",
      "T": "Yahweh's word came to me:"
    },
    "15": {
      "L": "Son of man, thy brethren, even thy brethren, the men of thy kindred and all the house of Israel wholly, are they unto whom the inhabitants of Jerusalem have said: Get you far from the LORD; unto us is this land given in possession.",
      "M": "Son of man, it is your brothers — your own kinsmen — and all the house of Israel, those the inhabitants of Jerusalem have dismissed, saying: 'Keep far from the LORD; this land has been given to us as our possession.'",
      "T": "Son of man: your brothers — your kinsmen — and all the house of Israel, the exiles in Babylon — these are the people Jerusalem has written off. 'Stay away,' Jerusalem says. 'Yahweh has removed you; this land belongs to us now.' That is what the city tells itself."
    },
    "16": {
      "L": "Therefore say: Thus saith the Lord GOD; Although I have cast them far off among the heathen, and although I have scattered them among the countries, yet will I be to them as a little sanctuary in the countries where they shall come.",
      "M": "Therefore say: This is what the Lord GOD says: Although I sent them far away among the nations and scattered them among the countries, I have been a small sanctuary to them in the countries where they went.",
      "T": "So say from the Lord Yahweh: Yes — I drove them far away, scattered them to foreign nations and strange lands. But there, in every country where they have gone, I have been a sanctuary to them. A smaller one, a quieter one, without a temple building. But still a holy presence, still Yahweh with them."
    },
    "17": {
      "L": "Therefore say: Thus saith the Lord GOD; I will even gather you from the people, and assemble you out of the countries where ye have been scattered, and I will give you the land of Israel.",
      "M": "Therefore say: This is what the Lord GOD says: I will gather you from among the peoples, collect you from the countries where you have been scattered, and give you the land of Israel.",
      "T": "And more: I will gather you back from every nation, collect the scattered from every country, and bring you home to the land of Israel."
    },
    "18": {
      "L": "And they shall come thither, and they shall take away all the detestable things thereof and all the abominations thereof from it.",
      "M": "When they come there, they will remove all its detestable things and all its abominations.",
      "T": "When they return, they will sweep the land clean — every idol, every abomination removed. The return will come with purification."
    },
    "19": {
      "L": "And I will give them one heart, and I will put a new spirit within you; and I will take the stony heart out of their flesh and will give them a heart of flesh.",
      "M": "I will give them one heart and put a new spirit within them; I will remove the heart of stone from their flesh and give them a heart of flesh.",
      "T": "I will give them one undivided heart — no more split loyalties — and put a new spirit inside them. The heart of stone — hard, unresponsive, closed to me — I will remove. In its place: a heart of flesh. Alive. Pliable. Capable of receiving what I give. This is the promise Jeremiah spoke of; Ezekiel gives it the same voice."
    },
    "20": {
      "L": "That they may walk in my statutes and keep mine ordinances and do them; and they shall be my people and I will be their God.",
      "M": "Then they will walk in my statutes, keep my ordinances, and obey them; they will be my people, and I will be their God.",
      "T": "Then they will walk in my statutes. Keep my ordinances. Live in the covenant they were made for. They will be my people and I will be their God — the covenant renewed from the inside out."
    },
    "21": {
      "L": "But as for them whose heart walketh after the heart of their detestable things and their abominations, I will recompense their way upon their own heads, saith the Lord GOD.",
      "M": "But as for those whose hearts pursue their detestable idols and abominations, I will bring their conduct down upon their own heads, declares the Lord GOD.",
      "T": "But those who have handed their hearts over to their idols and abominations — the Lord Yahweh says: I will repay them exactly as their own deeds deserve."
    },
    "22": {
      "L": "Then did the cherubims lift up their wings, and the wheels beside them; and the glory of the God of Israel was over them above.",
      "M": "Then the cherubim spread their wings, with the wheels alongside them, and the glory of the God of Israel was above them.",
      "T": "Then the cherubim spread their wings. The wheels rose with them. The glory of Israel's God blazed above them all — lifted, moving, departing."
    },
    "23": {
      "L": "And the glory of the LORD went up from the midst of the city and stood upon the mountain which is on the east side of the city.",
      "M": "The glory of the LORD ascended from within the city and stood on the mountain to the east of the city.",
      "T": "The glory of the LORD rose from the city — completely, finally — away from its walls and courts and gates. It came to rest on the mountain east of the city: the Mount of Olives. Yahweh's presence stood there, pausing, looking back at Jerusalem from across the Kidron valley. The departure was complete."
    },
    "24": {
      "L": "Afterwards the spirit took me up and brought me in a vision by the Spirit of God into Chaldea, to them of the captivity. So the vision that I had seen went up from me.",
      "M": "Afterward the Spirit lifted me and brought me in a vision by the Spirit of God to Chaldea, to the exiles. Then the vision I had seen rose away from me.",
      "T": "Then the Spirit lifted me and, in the vision by God's Spirit, carried me back to Chaldea — back to the exiles in Babylon. The vision ended. Everything I had seen lifted and was gone."
    },
    "25": {
      "L": "Then I spake unto them of the captivity all the things that the LORD had shewed me.",
      "M": "I then told the exiles everything the LORD had shown me.",
      "T": "I told the exiles everything — every vision, every word, everything Yahweh had shown me about the temple, the departure of the glory, and the promise of a new heart."
    }
  },
  "12": {
    "1": {
      "L": "The word of the LORD also came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, thou dwellest in the midst of a rebellious house, which have eyes to see and see not; which have ears to hear and hear not; for they are a rebellious house.",
      "M": "Son of man, you live among a rebellious people who have eyes but do not see, who have ears but do not hear — for they are a rebellious house.",
      "T": "Son of man, you are living with people who have every capacity to understand — and refuse to use it. Eyes open, but unseeing. Ears intact, but unhearing. This is what rebellion looks like at its core: chosen blindness."
    },
    "3": {
      "L": "Therefore, thou son of man, prepare thee stuff for removing and remove by day in their sight; and thou shalt remove from thy place to another place in their sight; it may be they will consider, though they be a rebellious house.",
      "M": "Therefore, son of man, prepare your exile baggage by day in their sight; move from your place to another place before their eyes — perhaps they will take notice, though they are a rebellious house.",
      "T": "So do this, son of man: pack your exile bundle. Do it in daylight, where they can see every move. Then move yourself from one place to another — all in plain sight. Perhaps — just perhaps — they will register what they see, even though they are rebels who refuse to understand."
    },
    "4": {
      "L": "Then shalt thou bring forth thy stuff by day in their sight, as stuff for removing; and thou shalt go forth at even in their sight, as they that go forth into captivity.",
      "M": "Bring out your baggage by day in their sight, as for going into exile; then in the evening, before their eyes, go out as those going into captivity.",
      "T": "In the day: bring out the baggage where they can see. In the evening: go out yourself — in their sight, moving like those being marched into exile."
    },
    "5": {
      "L": "Dig thou through the wall in their sight and carry out thereby.",
      "M": "Dig through the wall in their sight and carry your things out through it.",
      "T": "Dig through the wall — let them watch — and carry your things out through the gap you make."
    },
    "6": {
      "L": "In their sight shalt thou bear it upon thy shoulders and carry it forth in the twilight; thou shalt cover thy face that thou see not the ground; for I have set thee for a sign unto the house of Israel.",
      "M": "Carry it out on your shoulder in their sight as dusk falls; cover your face so that you cannot see the land — for I have made you a sign to the house of Israel.",
      "T": "Carry it on your shoulder in the twilight, in their sight. Cover your face — don't look at the ground, don't take in the land around you. That covered face is part of the sign: the exile goes out without seeing what he leaves behind. You are the living prophecy, the sign Yahweh is speaking through your body."
    },
    "7": {
      "L": "And I did so as I was commanded: I brought forth my stuff by day as stuff for captivity, and in the even I digged through the wall with mine hand; I brought it forth in the twilight and I bare it upon my shoulder in their sight.",
      "M": "I did as I was commanded: I brought out my baggage by day as the goods of an exile; in the evening I dug through the wall with my hands; I brought it out in the twilight and carried it on my shoulder before their eyes.",
      "T": "I obeyed. In the day I brought out my bundle — the baggage of exile. In the evening I broke through the wall with my own hands. At twilight I carried the load on my shoulder where they could all see me. The body enacts the prophecy before the mouth can speak it."
    },
    "8": {
      "L": "And in the morning came the word of the LORD unto me, saying:",
      "M": "In the morning the word of the LORD came to me:",
      "T": "Morning came, and with it Yahweh's word:"
    },
    "9": {
      "L": "Son of man, hath not the house of Israel, the rebellious house, said unto thee: What doest thou?",
      "M": "Son of man, has the rebellious house of Israel not asked you, 'What are you doing?'",
      "T": "Son of man — did the rebellious house of Israel ask you what you were doing?"
    },
    "10": {
      "L": "Say thou unto them: Thus saith the Lord GOD; This burden concerneth the prince in Jerusalem and all the house of Israel that are among them.",
      "M": "Say to them: 'This is what the Lord GOD says: This oracle concerns the prince in Jerusalem and all the house of Israel who are there.'",
      "T": "Tell them: The Lord Yahweh says — this is an oracle. It concerns the prince in Jerusalem — the king — and the whole house of Israel gathered around him."
    },
    "11": {
      "L": "Say: I am your sign; as I have done, so shall it be done unto them; they shall remove and go into captivity.",
      "M": "Say: 'I am your sign. As I have done, so shall it be done to them — they will be uprooted and go into exile.'",
      "T": "Say: I am your sign. What you watched me do — that is what is coming for them. They will be uprooted. They will be marched into exile."
    },
    "12": {
      "L": "And the prince that is among them shall bear upon his shoulder in the twilight and shall go forth; they shall dig through the wall to carry out thereby; he shall cover his face that he see not the ground with his eyes.",
      "M": "The prince among them will carry his things on his shoulder in the dark and go out; they will dig through the wall to get out through it; he will cover his face so that he cannot see the land with his eyes.",
      "T": "The prince himself will carry his load on his shoulder in the darkness and slip out through a gap they dig in the wall. He will cover his face — so his own eyes do not see the land he is leaving. Zedekiah will flee like a fugitive, blinded to what he is losing."
    },
    "13": {
      "L": "My net also will I spread upon him and he shall be taken in my snare; and I will bring him to Babylon to the land of the Chaldeans; yet shall he not see it though he shall die there.",
      "M": "I will spread my net over him and catch him in my snare; I will bring him to Babylon, to the land of the Chaldeans — yet he will not see it, though he will die there.",
      "T": "I will cast my net over him and catch him in my snare. He will be taken to Babylon — the land of the Chaldeans. He will die there. But he will never see it: his eyes will be put out before he arrives. My judgment, complete in every detail."
    },
    "14": {
      "L": "And I will scatter toward every wind all that are about him to help him and all his bands; and I will draw out the sword after them.",
      "M": "I will scatter to every wind all his supporters and all his troops; I will pursue them with the sword.",
      "T": "His guard, his allies, everyone around him — scattered to every wind. I will draw the sword after them and pursue them wherever they run."
    },
    "15": {
      "L": "And they shall know that I am the LORD when I shall scatter them among the nations and disperse them in the countries.",
      "M": "They will know that I am the LORD when I scatter them among the nations and disperse them throughout the countries.",
      "T": "Scattered among the nations, dispersed through foreign lands — that is when they will know that I am Yahweh. The recognition comes through exile."
    },
    "16": {
      "L": "But I will leave a few men of them from the sword, from the famine and from the pestilence; that they may declare all their abominations among the heathen whither they come; and they shall know that I am the LORD.",
      "M": "But I will spare a small number of them from sword, famine, and plague, so that they may confess all their abominations among the nations where they go — and they will know that I am the LORD.",
      "T": "A remnant I will spare — a few who survive sword, famine, and plague. Not saved for their own sake, but to carry a testimony among the nations: that Israel's abominations brought this on them. They will speak it. The nations will hear. And all will know that I am Yahweh."
    },
    "17": {
      "L": "Moreover the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me again:",
      "T": "Yahweh's word came to me again:"
    },
    "18": {
      "L": "Son of man, eat thy bread with quaking and drink thy water with trembling and with carefulness.",
      "M": "Son of man, eat your bread with trembling and drink your water with shaking and dread.",
      "T": "Son of man, eat your bread shaking with fear. Drink your water with trembling hands and a racing heart."
    },
    "19": {
      "L": "And say unto the people of the land: Thus saith the Lord GOD of the inhabitants of Jerusalem and of the land of Israel; They shall eat their bread with carefulness and drink their water with astonishment, that her land may be desolate from all that is therein, because of the violence of all them that dwell therein.",
      "M": "Say to the people of the land: This is what the Lord GOD says about the inhabitants of Jerusalem and the land of Israel: They will eat their bread with anxiety and drink their water in horror — because the land will be stripped bare on account of the violence of all who live in it.",
      "T": "Say this to the people of the land — the Lord Yahweh's word about Jerusalem and all of Israel: They will eat in panic. They will drink in horror. Their land will be emptied of everything in it, because violence is what filled it. The violence they chose will be what strips the land bare."
    },
    "20": {
      "L": "And the cities that are inhabited shall be laid waste and the land shall be desolate; and ye shall know that I am the LORD.",
      "M": "The inhabited cities will be laid waste and the land made desolate; then you will know that I am the LORD.",
      "T": "Every populated city: ruins. The land: desolation. And then — you will know that I am Yahweh."
    },
    "21": {
      "L": "And the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "22": {
      "L": "Son of man, what is that proverb that ye have in the land of Israel, saying: The days are prolonged and every vision faileth?",
      "M": "Son of man, what is this proverb you keep hearing in the land of Israel: 'The days drag on and every vision comes to nothing'?",
      "T": "Son of man, there is a proverb circulating in Israel. It goes: The days keep stretching out, and every vision fizzles. What the prophets threaten never arrives. This is what fatalism sounds like — denying prophetic truth one delayed fulfillment at a time."
    },
    "23": {
      "L": "Tell them therefore: Thus saith the Lord GOD; I will make this proverb to cease and they shall no more use it as a proverb in Israel; but say unto them: The days are at hand and the effect of every vision.",
      "M": "Therefore say to them: This is what the Lord GOD says: I will put an end to this proverb; it will no longer be used in Israel. Say instead: The days are at hand — every vision will take effect.",
      "T": "So say from the Lord Yahweh: That proverb ends now. I will retire it; it will no longer be on anyone's lips in Israel. Substitute this instead: The days are at hand. Every vision is about to come true."
    },
    "24": {
      "L": "For there shall be no more any vain vision nor flattering divination within the house of Israel.",
      "M": "For there will be no more empty visions or flattering divination within the house of Israel.",
      "T": "No more empty visions. No more prophets who smooth things over and speak peace when there is none. The age of comfortable lying is over."
    },
    "25": {
      "L": "For I am the LORD; I will speak, and the word that I shall speak shall come to pass; it shall be no more prolonged; for in your days, O rebellious house, will I say the word and will perform it, saith the Lord GOD.",
      "M": "For I am the LORD; I will speak, and what I speak will happen — it will not be delayed any further. In your own days, rebellious house, I will speak the word and fulfill it, declares the Lord GOD.",
      "T": "I am Yahweh. When I speak, the thing happens — not sometime, not eventually, not after long delays. In your own days — the very generation I am speaking to now — I will say the word and I will do it. The Lord Yahweh has declared it."
    },
    "26": {
      "L": "Again the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me again:",
      "T": "Again Yahweh's word came to me:"
    },
    "27": {
      "L": "Son of man, behold, they of the house of Israel say: The vision that he seeth is for many days to come, and he prophesieth of the times that are far off.",
      "M": "Son of man, the house of Israel is saying, 'The vision he sees is for the distant future, and he prophesies of times far off.'",
      "T": "Son of man — Israel is using a different version of the same strategy. They say: Yes, the vision may be genuine — but it is for a distant day, times far from now. We are safe in the present. This concedes prophetic truth while evacuating its urgency."
    },
    "28": {
      "L": "Therefore say unto them: Thus saith the Lord GOD; There shall none of my words be prolonged any more, but the word which I have spoken shall be done, saith the Lord GOD.",
      "M": "Therefore say to them: This is what the Lord GOD says: None of my words will be put off any longer — the word I have spoken will be done, declares the Lord GOD.",
      "T": "So say from the Lord Yahweh: Nothing I have said will be postponed. Not by proverb, not by theology, not by delay. The word has been spoken. The word will be done. The Lord Yahweh declares it — and there is nothing more to say."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 10–12 written.')

if __name__ == '__main__':
    main()
