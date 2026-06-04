"""
MKT Ezekiel chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-7-9.py

Translation decisions (carrying forward all conventions from mkt-ezekiel-4-6.py):

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T for the recognition formula
  ("you shall know that I am the LORD" — the defining Ezekiel refrain at 7:4, 7:9, 7:27,
  9:4, etc.) and divine-speech introductions. Maintains EZK-1b convention.

- H136 + H3069 (אֲדֹנָי יְהוִה / Adonai-Yahweh): "Lord GOD" in L/M (small-caps GOD per
  convention); "Lord Yahweh" in T. The combined form dominates Ezekiel's oracle style.

- H7093 (קֵץ / qets, "end"): In chapter 7 this word tolls like a bell — twice in v2,
  then again in v3, v6 (twice again), v7. The staccato repetition is the rhetorical heart
  of the oracle. L preserves it word-for-word; M allows modest sentence variation;
  T dramatizes the cumulative weight without adding vocabulary.

- H6843 (צְפִירָה): "morning" in L (following the MT surface reading; cf. KJV). In M/T
  rendered contextually as "doom" or "hour of doom" — the dawn that breaks is the dawn
  of disaster. The same word appears in both 7:7 and 7:10.

- H6974 (יָקַץ / "it has awakened"): In 7:6 the end is personified as a sleeping enemy
  that suddenly wakes. L: "it has awakened"; M: "it has roused itself"; T expands the
  image slightly.

- H8420 (תָּו / tāw, "mark/sign"): In 9:4 the LORD commands a "mark" (ת, tāw) to be set
  on the foreheads of the grieving. In ancient Paleo-Hebrew and early Phoenician script,
  tāw was written as an X (or + shape). Origen, Tertullian, and Jerome read it as a type
  of the cross. The T tier names the letter and its significance without being dogmatic.

- H3519 (כָּבוֹד / glory): "the glory of the God of Israel" — preserved in all tiers as
  "glory." The glory present in 8:4 is the same kavod-presence of the chariot-throne
  (ch 1); its withdrawal in 9:3 (to the threshold) begins the departure sequence that
  culminates in ch 11. T tier surfaces this theological trajectory.

- H7307 (רוּחַ): In 8:3 the Spirit lifts Ezekiel between earth and heaven — divine agency,
  clearly the Spirit of God. Capitalized "Spirit" in all tiers. (Different from 5:2
  "wind" in the prior script, where context was physical dispersal.)

- H3742 (כְּרוּב / cherub): "cherub" throughout. The glory "rested on the cherub" (9:3)
  — the throne-chariot of ch 1. "Cherub" in L/M; "the cherub-throne" in T where helpful.

- H7068 (קִנְאָה / jealousy): "jealousy" in L/M for the idol-name ("image of jealousy"
  8:3, 5). In T: "the idol of jealousy" or unpacked as "the image that provokes
  Yahweh's jealous wrath."

- H1544 (גִּלּוּל / idols): "idols" throughout, per EZK-1b. Ezekiel's contemptuous term.

- H5771 (עָוֹן / iniquity): "iniquity" in L/M; "guilt" in T — per EZK-1b.

- H8441 (תּוֹעֵבָה / abominations): "abominations" in L; "abominations" in M;
  T may use "abominations" or "detestable practices" or specific description, depending
  on whether specificity adds meaning. Never softened to "sins" or "wrongs."

- H8542 (תַּמּוּז / Tammuz): Proper name preserved. The Babylonian/Sumerian god of
  vegetation; mourned annually in midsummer when he "descends to the underworld." The
  sixth month (August-September by Hebrew reckoning) is precisely the Tammuz mourning
  season. T tier names this context explicitly.

- Sun worship (8:16): Twenty-five men with backs to the temple, faces east toward the
  sunrise. The most brazen of the four abominations — they turned their backs on the Holy
  of Holies while worshipping within the sacred precincts. T tier names the full horror.

- "Put the branch to the nose" (8:17): H2156 (זְמוֹרָה, branch/vine-shoot). The exact
  ritual is debated — possibly a Persian or Zoroastrian rite with a haoma bundle, possibly
  a contemptuous gesture. All tiers preserve the obscure act; T tier names the ambiguity.

- "Begin at my sanctuary" (9:6): cf. 1 Pet 4:17 ("judgment begins at the household of
  God"). Ezekiel's vision is the OT ground for that NT principle. T tier surfaces this.

- H2970 (יַאֲזַנְיָה / Jaazaniah): Proper name — "Jaazaniah son of Shaphan" — preserved.
  (Note: a different Jaazaniah son of Shaphan appears in Jer 35:3; this may be a son of
  the Shaphan who supported Josiah's reform — adding bitter irony if so.)

- Poetry/prose note: Chs 7–9 are elevated prophetic prose. Ch 7 approaches poetry in its
  staccato repetitions. T tier uses short, percussive sentences in ch 7 to mirror the
  Hebrew rhetorical style. No formal line-break versification.
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
  "7": {
    "1": {
      "L": "Moreover the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me again:"
    },
    "2": {
      "L": "And you, son of man, thus says the Lord GOD to the land of Israel: An end — the end has come upon the four corners of the land.",
      "M": "Son of man, this is what the Lord GOD says to the land of Israel: An end! The end has come upon the four corners of the land.",
      "T": "Son of man, here is the Lord Yahweh's word to the land of Israel: The end. The end has come — to every corner of the land."
    },
    "3": {
      "L": "Now the end is upon you, and I will send my anger upon you and will judge you according to your ways, and I will recompense upon you all your abominations.",
      "M": "Now the end is upon you; I will unleash my anger against you, judge you according to your ways, and repay you for all your abominations.",
      "T": "The end has arrived. I will send my anger against you, judge you by your own conduct, and make you answer for every abomination you have committed."
    },
    "4": {
      "L": "And my eye shall not spare you, neither will I have pity; but I will recompense your ways upon you, and your abominations shall be in your midst; and you shall know that I am the LORD.",
      "M": "My eye will not spare you, nor will I have pity; I will repay you for your ways, and your abominations will rest upon you; then you will know that I am the LORD.",
      "T": "I will not flinch. I will not soften. Your own conduct and your own abominations will be the weight that falls on you. And when it is over, you will know that I am Yahweh."
    },
    "5": {
      "L": "Thus says the Lord GOD: An evil — a unique evil — behold, it is coming.",
      "M": "This is what the Lord GOD says: A disaster — a singular disaster — look, it is coming!",
      "T": "The Lord Yahweh says: One disaster — unlike any other — is on its way."
    },
    "6": {
      "L": "An end has come; the end has come; it has awakened against you. Behold, it is coming.",
      "M": "An end has come; the end has come; it has roused itself against you. Look, it is coming!",
      "T": "End — end — the end has shaken itself awake and is moving against you. It is coming."
    },
    "7": {
      "L": "The morning has come upon you, O inhabitant of the land; the time has come, the day is near — a day of tumult, and not of joyful shouting on the mountains.",
      "M": "Doom has come upon you, O inhabitant of the land; the time has arrived, the day is near — a day of chaos, not of jubilant cries echoing through the mountains.",
      "T": "The hour of doom is breaking over you. The time has come. The day is here — not a bright morning of celebration, but a day of chaos and dread, with no festival shout echoing from the hills."
    },
    "8": {
      "L": "Now I will shortly pour out my fury upon you, and accomplish my anger upon you; and I will judge you according to your ways, and I will recompense you for all your abominations.",
      "M": "Now I will soon pour out my fury upon you and exhaust my anger against you; I will judge you according to your ways and repay you for all your abominations.",
      "T": "Very soon I will pour my fury over you and burn through my anger completely. I will judge you by your own track record and make you answer for every abomination."
    },
    "9": {
      "L": "And my eye shall not spare, neither will I have pity: I will recompense you according to your ways and your abominations that are in your midst; and you shall know that I am the LORD who strikes.",
      "M": "My eye will not spare, nor will I show pity; I will repay you for your ways and for the abominations among you; then you will know that I am the LORD who strikes.",
      "T": "No mercy. No softening. Your own ways and abominations will be repaid in full. You will know, then, that I am Yahweh — the one who strikes."
    },
    "10": {
      "L": "Behold the day; behold, it has come; the morning has gone forth. The rod has budded; arrogance has blossomed.",
      "M": "See — the day has come; doom's morning has broken. The rod has sprouted; pride has blossomed.",
      "T": "The day has arrived. The dawn of doom has broken. The rod of punishment has sprouted from the ground. Arrogance has burst into full flower — and now it will be cut down."
    },
    "11": {
      "L": "Violence has risen up into a rod of wickedness; none of them shall remain, nor their multitude, nor anything of theirs; and there shall be no wailing for them.",
      "M": "Violence has grown into a rod of wickedness; none of them will survive — not the crowd, not their wealth, not a trace — and no one will mourn for them.",
      "T": "The violence Israel bred has grown into the very rod that will strike them. Nothing will remain — not the mass of people, not their wealth, not a memory. No one will be left to mourn."
    },
    "12": {
      "L": "The time has come; the day draws near. Let not the buyer rejoice, nor the seller mourn; for wrath is upon all their multitude.",
      "M": "The time has come; the day is close. Let the buyer not rejoice, nor the seller lament — for the wrath of God rests on their whole multitude.",
      "T": "Time is up. The day is here. It does not matter anymore who bought property and who sold it — the buyer will never enjoy his purchase, the seller will never recover his loss. The wrath of God falls on all of them."
    },
    "13": {
      "L": "For the seller shall not return to what was sold, though they were yet alive; for the vision concerning all their multitude shall not be revoked, and no one shall strengthen himself through his iniquity.",
      "M": "For the seller will not recover what was sold, even if he lives — the vision against their whole multitude will not be reversed, and no one will be able to sustain himself through his iniquity.",
      "T": "The seller who lost land will never recover it — not even if he survives. The prophetic judgment against this whole people will not be reversed. No one will be able to prop himself up on accumulated guilt; it will only drag him down."
    },
    "14": {
      "L": "They have blown the trumpet and made everything ready; but no one goes to battle, for my wrath is upon all their multitude.",
      "M": "They have blown the trumpet and prepared everything for battle, but no one marches out — for my wrath rests upon their whole multitude.",
      "T": "The trumpet has sounded. Everything is in order for war. But no one marches out. My wrath has fallen on every last one of them, and there is no heart left to fight."
    },
    "15": {
      "L": "The sword is outside, and pestilence and famine within. The one who is in the field shall die by the sword; and those in the city shall be devoured by famine and pestilence.",
      "M": "The sword is outside; pestilence and famine are within. Whoever is out in the open will die by the sword; those inside the city will be consumed by famine and disease.",
      "T": "Outside the walls: the sword. Inside the walls: plague and starvation. There is no escape in any direction. The field offers the sword; the city offers slow death."
    },
    "16": {
      "L": "But those of them who escape shall escape and be on the mountains like doves of the valleys, all of them mourning, each for his iniquity.",
      "M": "Those who escape will be scattered on the mountains, moaning like doves of the valleys — each one mourning his own iniquity.",
      "T": "Those who slip through will scatter into the hills — each one alone, like a dove far from its valley, each one mourning the weight of his own guilt."
    },
    "17": {
      "L": "All hands shall be feeble, and all knees shall run as water.",
      "M": "All hands will grow limp, and every knee will go weak as water.",
      "T": "Every hand will go limp. Every knee will dissolve. Total collapse."
    },
    "18": {
      "L": "They shall also gird themselves with sackcloth, and horror shall cover them; and shame shall be upon all faces, and baldness upon all their heads.",
      "M": "They will put on sackcloth; terror will cover them; shame will be written on every face; every head shaved in mourning.",
      "T": "Sackcloth will be all they wear. Terror will settle over them like a shroud. Every face will be marked with shame. Every head shaved — the ancient sign of grief beyond grief."
    },
    "19": {
      "L": "They shall cast their silver into the streets, and their gold shall be as an unclean thing; their silver and their gold shall not be able to deliver them in the day of the wrath of the LORD; they shall not satisfy their hunger nor fill their stomachs with it, for it has become the stumbling block of their iniquity.",
      "M": "They will throw their silver into the streets, and their gold will be treated as unclean; their silver and gold cannot rescue them on the day of the LORD's wrath; they cannot satisfy their hunger or fill their stomachs with it — for it has become the stumbling block of their iniquity.",
      "T": "They will hurl their silver into the gutters. Gold will be worthless — unclean, untouchable. On the day of Yahweh's fury, no treasure will buy their escape. They cannot eat their gold. They cannot fill their stomachs with it. The very wealth they trusted became the idol that tripped them."
    },
    "20": {
      "L": "As for the beauty of his ornament, he set it in majesty; but they made their abominable images and their detestable things in it; therefore I have made it a thing unclean to them.",
      "M": "As for their fine jewelry, they wore it with pride; but out of it they fashioned images of abomination and detestable things — therefore I have made it unclean to them.",
      "T": "The gold and ornament that God gave them as beauty — they melted it into idols. They took what was magnificent and made it monstrous. So now it is declared unclean: the beauty they defiled can no longer help them."
    },
    "21": {
      "L": "And I will give it into the hands of strangers for a prey, and to the wicked of the earth for a spoil; and they shall defile it.",
      "M": "I will hand it over to foreigners as plunder, and to the wicked of the earth as spoil; they will defile it.",
      "T": "I will give their treasure to foreign nations as plunder, to the worst of the earth as spoil. Strangers will desecrate what Israel would not protect."
    },
    "22": {
      "L": "My face will I also turn from them, and they shall defile my secret place; for the violent ones shall enter into it and defile it.",
      "M": "I will turn my face away from them; they will profane my treasured sanctuary; robbers will break in and desecrate it.",
      "T": "I will look away. When I avert my face, the desecration can begin. Violent marauders will force their way into the most sacred space — the place where my presence once rested — and defile it."
    },
    "23": {
      "L": "Make a chain! For the land is full of bloody crimes, and the city is full of violence.",
      "M": "Prepare chains! For the land is filled with bloodshed and violent crimes, and the city is full of violence.",
      "T": "Forge the chains. The land is soaked in blood — crime upon crime. The city runs with violence. It is time for the captives to be bound and marched away."
    },
    "24": {
      "L": "Wherefore I will bring the worst of the nations, and they shall possess their houses; I will also make the pride of the strong to cease, and their holy places shall be defiled.",
      "M": "Therefore I will bring the most ruthless of the nations, and they will take possession of their houses; I will end the arrogance of the strong, and their sacred places will be profaned.",
      "T": "I will bring the most brutal nation on earth and hand Israel's homes to them. I will put an end to the arrogance of the powerful. Even the places Israel called sacred will be defiled."
    },
    "25": {
      "L": "Anguish comes; and they shall seek peace, but there shall be none.",
      "M": "Anguish is coming; they will search for peace, but there will be none.",
      "T": "Destruction arrives. They will search desperately for some way out, some word of peace — but there is no exit."
    },
    "26": {
      "L": "Disaster shall come upon disaster, and rumour upon rumour; then shall they seek a vision from the prophet, but the law shall perish from the priest, and counsel from the elders.",
      "M": "Disaster upon disaster will come, and report after report of calamity; then they will seek a vision from the prophet, but the law will be lost to the priest and counsel to the elders.",
      "T": "Disaster will pile on disaster. Reports of catastrophe will follow without pause. In desperation they will look to the prophets for a word — but the prophets will have nothing. The priests will have no Torah to speak. The elders will have no wisdom to offer. Every source of guidance will go silent at once."
    },
    "27": {
      "L": "The king shall mourn, and the prince shall be clothed with desolation, and the hands of the people of the land shall be troubled; according to their conduct I will deal with them, and according to their judgments I will judge them; and they shall know that I am the LORD.",
      "M": "The king will mourn; the prince will be wrapped in desolation; the hands of the people of the land will tremble. I will deal with them according to their own conduct and judge them by their own standards; then they will know that I am the LORD.",
      "T": "The king will sit in mourning. The prince will be draped in desolation. The people will tremble with hands too weak to act. I will repay everyone according to what they did — their own deeds become the measure of their sentence. And when it all comes true, they will know that I am Yahweh."
    }
  },
  "8": {
    "1": {
      "L": "And it came to pass in the sixth year, in the sixth month, on the fifth day of the month, as I sat in my house and the elders of Judah sat before me, that the hand of the Lord GOD fell upon me there.",
      "M": "In the sixth year, in the sixth month, on the fifth day of the month, while I was sitting in my house and the elders of Judah were seated before me, the hand of the Lord GOD fell upon me there.",
      "T": "Sixth year, sixth month, fifth day — I was sitting at home with the elders of Judah gathered in front of me. Then the hand of the Lord Yahweh seized me."
    },
    "2": {
      "L": "Then I looked, and behold, a likeness as the appearance of fire — from the appearance of his loins and downward, fire; and from his loins and upward as the appearance of brightness, as the colour of amber.",
      "M": "I looked, and there was a form that appeared like fire — from what looked like his waist downward, fire; and from his waist upward, the brightness of gleaming amber.",
      "T": "I saw a form — human in outline but consuming. From the waist down: fire. From the waist up: blazing amber, the colour of polished metal in the forge. The divine presence stood before me."
    },
    "3": {
      "L": "And he put forth the form of a hand and took me by a lock of my head; and the Spirit lifted me up between earth and heaven and brought me in visions of God to Jerusalem, to the entrance of the inner gate that faces north, where was the seat of the image of jealousy that provokes to jealousy.",
      "M": "He stretched out what appeared to be a hand and took me by a lock of my hair; the Spirit then lifted me between earth and heaven and brought me in visions of God to Jerusalem — to the entrance of the inner gate facing north, where stood the image of jealousy that arouses jealousy.",
      "T": "He reached out a hand — the form of a hand — and took hold of me by a lock of hair. The Spirit then lifted me between earth and heaven and carried me in a divine vision to Jerusalem: to the north gate of the inner court, where the idol stood — the image of jealousy, provoking Yahweh's jealous wrath by its very existence."
    },
    "4": {
      "L": "And behold, the glory of the God of Israel was there, according to the vision that I saw in the plain.",
      "M": "And there was the glory of the God of Israel — just as I had seen in the vision by the plain.",
      "T": "And there was the glory of Israel's God — the same blazing presence I had seen in the valley. Yahweh was already there, waiting, watching."
    },
    "5": {
      "L": "Then said he to me: Son of man, lift up your eyes toward the north. So I lifted up my eyes toward the north, and behold northward at the gate of the altar was this image of jealousy at the entrance.",
      "M": "He said to me: 'Son of man, look north.' I looked north, and there at the entrance of the altar gate, at the north side, stood the image that provokes jealousy.",
      "T": "He said: Son of man, look north. I looked — and there, at the entrance of the altar gate, openly displayed, stood the idol of jealousy."
    },
    "6": {
      "L": "He said furthermore to me: Son of man, do you see what they are doing — the great abominations that the house of Israel is committing here, to drive me far from my sanctuary? But turn, and you shall see greater abominations still.",
      "M": "He said to me: 'Son of man, do you see what they are doing — the great abominations that the house of Israel commits here, driving me far from my sanctuary? Turn around; you will see even greater abominations.'",
      "T": "He said: Son of man — are you seeing this? These are the abominations Israel is committing here, pushing me out of my own sanctuary. And this is only the beginning. Turn around. What you are about to see is worse."
    },
    "7": {
      "L": "And he brought me to the entrance of the court; and I looked, and behold a hole in the wall.",
      "M": "He brought me to the entrance of the court; I looked, and there was a hole in the wall.",
      "T": "He led me to the outer court's entrance. There I noticed something: a breach in the wall."
    },
    "8": {
      "L": "Then said he to me: Son of man, dig now in the wall. And when I had dug in the wall, behold a door.",
      "M": "He said to me: 'Son of man, dig into the wall.' I dug through the wall, and there was a doorway.",
      "T": "He said: Son of man, dig into the wall. I dug — and behind the wall was a hidden door."
    },
    "9": {
      "L": "And he said to me: Go in and see the wicked abominations that they are doing here.",
      "M": "He said: 'Go in and see the evil abominations they are committing here.'",
      "T": "Enter, he said. See what is being done here in secret."
    },
    "10": {
      "L": "So I went in and saw; and behold, every form of creeping things and abominable beasts, and all the idols of the house of Israel — portrayed all around on the wall.",
      "M": "I went in and looked: carved all around the walls were every kind of creeping animal and detestable creature, along with all the idols of the house of Israel.",
      "T": "I went in. Carved on every wall: serpents, vermin, every sort of unclean creature — and the idols of Israel. The room was a gallery of everything forbidden, from floor to ceiling."
    },
    "11": {
      "L": "And before them stood seventy men of the elders of the house of Israel, and in the midst of them stood Jaazaniah son of Shaphan, with every man his censer in his hand; and a thick cloud of incense went up.",
      "M": "Before these images stood seventy men of the elders of the house of Israel; Jaazaniah son of Shaphan stood in the center, each man holding his own censer, as a thick cloud of incense rose up.",
      "T": "Seventy elders of Israel — the whole council — stood there, each holding a censer, burning incense before the carved walls. At the center stood Jaazaniah son of Shaphan. The air was thick with smoke rising to images of demons."
    },
    "12": {
      "L": "Then said he to me: Son of man, have you seen what the elders of the house of Israel do in the dark, each man in the chambers of his imagery? For they say: The LORD does not see us; the LORD has forsaken the land.",
      "M": "He said to me: 'Son of man, have you seen what the elders of the house of Israel are doing in the dark — each in his own chamber with his carved idols? They are saying, The LORD cannot see us; the LORD has abandoned the land.'",
      "T": "He said: Son of man, see what Israel's leaders do in the dark — each in his private chamber with his carved images. This is their theology: Yahweh cannot see us. Yahweh has abandoned his land. So they reason themselves into deliberate, considered idolatry — each man in his own room, each man with his own gods."
    },
    "13": {
      "L": "He said also to me: Turn again, and you shall see greater abominations that they do.",
      "M": "He said to me: 'Turn around again; you will see still greater abominations they commit.'",
      "T": "He said: Turn around. There is more — and worse."
    },
    "14": {
      "L": "Then he brought me to the entrance of the gate of the LORD's house which was toward the north; and, behold, there sat women weeping for Tammuz.",
      "M": "He brought me to the entrance of the north gate of the LORD's house, and there women were sitting and weeping for Tammuz.",
      "T": "He brought me to the north gate of the LORD's own temple. There women sat weeping — weeping for Tammuz, the Babylonian god of fertility whose death was mourned each summer. They had carried Babylon's mourning rites into Yahweh's own house."
    },
    "15": {
      "L": "Then said he to me: Have you seen this, O son of man? Turn yet again, and you shall see greater abominations than these.",
      "M": "He said: 'Have you seen this, son of man? Turn again; you will see abominations greater than these.'",
      "T": "Have you seen enough, son of man? No. Turn again. It only gets worse."
    },
    "16": {
      "L": "And he brought me into the inner court of the LORD's house; and, behold, at the entrance of the temple of the LORD, between the porch and the altar, were about twenty-five men, with their backs toward the temple of the LORD and their faces toward the east; and they were bowing down toward the east, worshipping the sun.",
      "M": "He brought me into the inner court of the LORD's house. There between the porch and the altar, at the very entrance to the LORD's temple, stood about twenty-five men — their backs to the LORD's temple, their faces turned east, bowing down in worship toward the sun.",
      "T": "He brought me into the inner court — the holiest space in the complex. And there, between the porch and the altar, stood twenty-five men. Their backs were turned on the Holy of Holies. Their faces were toward the east. They were prostrate before the rising sun. In Yahweh's own temple, with his glory behind them, they had chosen to worship the sun."
    },
    "17": {
      "L": "Then he said to me: Have you seen this, O son of man? Is it a trivial thing to the house of Judah to commit the abominations that they commit here? For they have filled the land with violence, and have returned to provoke me to anger; and behold, they put the branch to their nose.",
      "M": "He said to me: 'Have you seen this, son of man? Is it a small thing for the house of Judah to commit the abominations they commit here? They have filled the land with violence and continue to provoke me to anger; and look — they even put the branch to their nose.'",
      "T": "He said: Is this a small thing, son of man? Judah fills the land with blood and then brings Babylonian rites into my house. And now watch — they raise the ritual branch under their own noses, as if I am the one to be dismissed. Every act has become an act of contempt."
    },
    "18": {
      "L": "Therefore will I also deal in fury; my eye shall not spare, neither will I have pity; and though they cry in my ears with a loud voice, I will not hear them.",
      "M": "Therefore I will act in fury; my eye will not spare, nor will I have pity; even if they shout in my ears with a loud cry, I will not hear them.",
      "T": "So I will respond in kind — with fury. No mercy. No restraint. When the disaster falls and they cry to me at the top of their lungs, I will not listen. They chose not to hear me; I will not hear them."
    }
  },
  "9": {
    "1": {
      "L": "He cried also in my ears with a loud voice, saying: Bring near those who have charge over the city, each with his destroying weapon in his hand.",
      "M": "He cried out loudly in my hearing: 'Let the enforcers of the city draw near, each with his weapon of destruction in his hand.'",
      "T": "Then he called out in my hearing with a voice like thunder: Bring forward those appointed to punish the city — every one of them, each with his instrument of destruction."
    },
    "2": {
      "L": "And behold, six men came from the direction of the upper gate that faces north, each with his weapon of slaughter in his hand; and one man among them was clothed in linen, with a writing case by his side. And they came in and stood beside the bronze altar.",
      "M": "Six men came from the direction of the upper gate facing north, each with his weapon of slaughter in hand; one man among them was clothed in linen, with a writing kit at his side. They came in and stood beside the bronze altar.",
      "T": "Six figures came from the north — from the upper gate — each carrying a weapon made for killing. Among them was one dressed in linen, a scribe's writing kit at his side. They took their places beside the bronze altar. Seven had arrived."
    },
    "3": {
      "L": "And the glory of the God of Israel had gone up from the cherub, whereupon he was, to the threshold of the house. And he called to the man clothed in linen who had the writing case by his side.",
      "M": "The glory of the God of Israel had moved from the cherub on which it rested to the threshold of the temple. He called to the man clothed in linen who had the writing case at his side.",
      "T": "The glory of Israel's God had already shifted — it had risen from the cherub-throne where it rested and moved to the threshold of the temple, beginning its withdrawal. From there, Yahweh called to the man in linen."
    },
    "4": {
      "L": "And the LORD said to him: Go through the midst of the city, through the midst of Jerusalem, and set a mark upon the foreheads of the men who sigh and cry over all the abominations that are done in its midst.",
      "M": "The LORD said to him: 'Go through the city, through Jerusalem, and mark a sign on the foreheads of the men who sigh and groan over all the abominations being committed in it.'",
      "T": "Yahweh said to him: Walk through Jerusalem — every street — and mark with the sign every person who grieves and mourns over the abominations being done in this city. The mark is the letter tāw — the last letter of the alphabet, written in the ancient script as an X, the shape of a cross. Those who bear it will be spared."
    },
    "5": {
      "L": "And to the others he said in my hearing: Go through the city after him and strike; let not your eye spare, neither have pity.",
      "M": "To the others he said in my hearing: 'Follow him through the city and strike; do not spare, have no pity.'",
      "T": "To the six destroyers he said — loud enough for me to hear: Follow the man in linen through the city and kill. Do not hold back. Show no mercy."
    },
    "6": {
      "L": "Kill old men, young men, maidens, little children, and women — utterly; but come not near anyone on whom is the mark; and begin at my sanctuary. So they began with the elders who were before the house.",
      "M": "Cut down old men, young men, maidens, little children, and women without mercy; but do not touch anyone who has the mark. Begin at my sanctuary. So they began with the elders standing before the temple.",
      "T": "Old and young, women and children — all of them, without exception, except the marked ones. And begin here — begin at my sanctuary. Judgment starts at God's own house. They began with the elders standing at the temple entrance."
    },
    "7": {
      "L": "And he said to them: Defile the house and fill the courts with the slain. Go out. And they went out and slew in the city.",
      "M": "He said to them: 'Defile the temple and fill its courts with the slain. Go.' They went out and killed throughout the city.",
      "T": "He said: Desecrate the temple — fill its courts with the dead. Then go out into the streets. They obeyed. The killing spread through the city."
    },
    "8": {
      "L": "And it came to pass that while they were slaying them, and I was left, I fell on my face and cried out and said: Ah, Lord GOD! Will you destroy all the remnant of Israel in pouring out your fury upon Jerusalem?",
      "M": "As they were striking the people down, I alone was left. I fell on my face and cried out: 'Ah, Lord GOD! Are you going to wipe out all that remains of Israel by pouring out your fury upon Jerusalem?'",
      "T": "While the killing was happening around me — and I alone had been left untouched — I fell on my face. I cried out: Lord Yahweh, please — will you wipe out everyone left in Israel? Is there nothing but fury left for Jerusalem?"
    },
    "9": {
      "L": "Then said he to me: The iniquity of the house of Israel and Judah is exceedingly great; the land is full of blood and the city is full of perverseness; for they say: The LORD has forsaken the land, and the LORD does not see.",
      "M": "He said to me: 'The iniquity of the house of Israel and Judah is extremely great; the land is filled with bloodshed and the city with injustice; for they say, The LORD has abandoned the land, and the LORD cannot see.'",
      "T": "He answered me: The guilt of both Israel and Judah is beyond measuring. Blood has soaked into the land. Injustice has filled the city. And underneath all of it — the lie they tell themselves: Yahweh has abandoned his land; Yahweh cannot see what we do. That lie gave them permission for everything else."
    },
    "10": {
      "L": "And as for me also, my eye shall not spare, neither will I have pity, but I will recompense their way upon their head.",
      "M": "As for me, my eye will not spare, nor will I have pity; I will bring their conduct down upon their own heads.",
      "T": "So no mercy from me either. No exceptions. Their own deeds will fall back on them."
    },
    "11": {
      "L": "And behold, the man clothed in linen, who had the writing case by his side, reported back the matter, saying: I have done as you commanded me.",
      "M": "Then the man clothed in linen, who had the writing case at his side, came back and reported: 'I have done as you commanded.'",
      "T": "The man in linen — the scribe of mercy — returned and reported: I have done what you commanded. Every forehead marked. Every mourner for Yahweh's honour, protected."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 7–9 written.')

if __name__ == '__main__':
    main()
