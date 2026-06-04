"""
MKT Ezekiel chapters 25–27 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-25-27.py

=== CHAPTER OVERVIEW ===
Chapter 25: Four brief oracles against surrounding nations — Ammon (vv. 1–7), Moab/Seir
(vv. 8–11), Edom (vv. 12–14), Philistia (vv. 15–17). Each follows a consistent pattern:
accusation (because you...) → judgment sentence (therefore I...) → recognition formula
(you/they shall know that I am the LORD). These oracles form the first half of a larger
block of seven nation-oracles (chs. 25–32) that bracket the fall of Jerusalem.

Chapter 26: Extended oracle against Tyre — the great Phoenician trading city on a
Mediterranean island. Three phases: (1) vv. 1–6, general proclamation of judgment;
(2) vv. 7–14, Nebuchadnezzar as instrument; (3) vv. 15–21, the response of the
coastlands and Tyre's descent to the Pit. Historically Nebuchadnezzar besieged Tyre
for 13 years (585–573 BC) with limited success; the ultimate fulfillment came under
Alexander the Great (332 BC) who built a causeway and completely destroyed the island city.

Chapter 27: A funeral dirge (qînāh) over Tyre in the form of an extended ship metaphor.
The city is a magnificent merchant vessel whose cargo manifest (vv. 12–25) reads like
an economic encyclopedia of the ancient world. Then the ship is wrecked (vv. 26–36)
and all who depended on it mourn. The T tier preserves the poetic structure with line
breaks for the lament sections.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T — especially in the recognition
  formula and narrative pivot points. Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Lord GOD): "Lord GOD" in L/M (small-caps GOD following
  convention). "Lord Yahweh" in T. Consistent with prior Ezekiel scripts.

- Recognition formula (וְיָדְעוּ כִּי אֲנִי יְהוָה): L/M "you/they shall know that I am
  the LORD." T "you/they shall know that I am Yahweh." Used at 25:5, 7, 11, 17; 26:6.

- H5315 (נֶפֶשׁ): Embied person/self, not Greek immaterial soul. L: "soul." M: "life/person."
  T: context-driven — "life" or "person." Not present prominently in these chapters.

- H2617 (חֶסֶד): Not prominent in these chapters (judgment oracles). Not relevant here.

- H5315 (נֶפֶשׁ): Not prominent in these chapters.

- Tyre geography: Tyre was a Phoenician city on a rocky island (H6865, צֹר = "rock") off the
  coast of modern Lebanon. "Rock" is the literal meaning of the city name and Ezekiel exploits
  this: the judgment makes Tyre literally "a bare rock" (26:4, 14). T surfaces this wordplay.

- H5594 (qînāh / dirge): Chapter 27 is a formal funeral lament — written for a city that has
  not yet died, treating the future as already accomplished. The T tier acknowledges this
  literary form explicitly in the preamble.

- H7362 (רַהַב / Rahab): Not present in these chapters.

- H7070 (קָנֶה / reed/calamus): 27:19 — "calamus" = aromatic reed, a luxury spice.
  L: "calamus." M: "calamus/aromatic cane." T: "fragrant calamus — the perfumer's cane."

- H4901 (מֶשֶׁך / Meshech, also draw/drag): Meshech in 27:13 is the people/nation, not the
  semantic range of the verb. L/M/T: "Meshech."

- H5650/H120 (אָדָם / human beings): 27:13 — trading in "souls of men" = human beings as
  slaves. L: "souls of men." M: "human beings" (slave trade). T: "human lives as merchandise"
  — the slave trade is what this means; the T tier names it.

- H6788 (צַמֶּרֶת / treetop/topmost branch): Not present in these chapters.

- H1004 (בַּיִת / house): Generic. No special decision needed.

- H3383 (יַרְדֵּן / Jordan): Not present.

- H4191 (מוּת / death) and H7585 (שְׁאוֹל / Sheol/Pit): 26:20 — יוֹרְדֵי בוֹר ("those who
  go down to the pit"). L: "the pit." M: "the pit/underworld." T: "the realm of the dead"
  or "the Pit" — Sheol as the place of the dead, not eternal damnation but the shadowy
  underworld of all the dead (cognate with Mesopotamian kur/irkalla).

- H3822 (לְבָנוֹן / Lebanon) cedars: 27:5 — used metaphorically. The cedars of Lebanon
  were the most prized timber of the ancient world. L: "Lebanon." M: "Lebanon." T: expanded.

- H6097 (עֵץ / tree/wood): Generic in the ship metaphor. L/M/T: contextual.

- H3605 (כֹּל / all/every): The word "all" (kol) appears with extreme frequency in ch. 27's
  cargo list as a rhetorical device of totality. Preserved in all tiers.

=== ASPECT / TENSE NOTES ===

- Chapter 25: The oracles use "because" (יַעַן) + past sins + "therefore" (לָכֵן) + future
  judgments. The past sins use perfect forms (completed acts). The judgment sentences use
  future imperfect (certainty). Preserved in all tiers.

- Chapter 26: Mixed forms. The first judgment oracle is proclamatory future. The Nebuchadnezzar
  section (vv. 7–14) shifts to detailed future description. The coastland response (vv. 15–21)
  uses present/future.

- Chapter 27: The ship-building section (vv. 3–11) uses past tense ("they made..."). The
  cargo list (vv. 12–25) uses imperfect "traded with you" — iterative/habitual past. The
  wreck and mourning (vv. 26–36) uses perfect + future mix. The L tier preserves this
  tense distribution.

=== OT INTERTEXTUALITY ===

- Ezekiel 25's oracle pattern ("because...therefore...you shall know") is a judicial
  sentence formula used throughout the prophets (Amos 1–2, Jer 25). T notes when relevant.

- Tyre's gloating over Jerusalem (26:2 "Aha!") echoes the Ammonite "Aha!" of 25:3 — both
  were enemies who rejoiced at Jerusalem's destruction. The same sin receives the same
  judgment structure.

- The "descent to the Pit" motif (26:20) is developed more fully in Ezekiel 32 (the
  underworld scene). The Pit (בּוֹר) echoes Joseph in the pit (Gen 37), but here is the
  cosmic underworld.

- Chapter 27's ship-wreck as judgment echoes Ps 107:23–30 (those who go to sea in ships,
  whom God brings low). T surfaces this in the concluding verses.

- The slave trade in 27:13 (Javan/Tubal/Meshech trading in "souls of men") anticipates
  Revelation 18:13 which quotes this verse in the judgment on Rome/Babylon.
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
  "25": {
    "1": {
      "L": "The word of the LORD came again unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, set thy face against the Ammonites, and prophesy against them;",
      "M": "Son of man, set your face toward the Ammonites and prophesy against them.",
      "T": "Son of man, turn and face Ammon. Speak against them — there is a word of judgment due."
    },
    "3": {
      "L": "And say unto the Ammonites: Hear the word of the Lord GOD. Thus saith the Lord GOD: Because thou saidst, Aha, against my sanctuary, when it was profaned; and against the land of Israel, when it was made desolate; and against the house of Judah, when they went into captivity;",
      "M": "Say to the Ammonites: Hear the word of the Lord GOD. Thus says the Lord GOD: Because you said 'Aha!' over my sanctuary when it was profaned, and over the land of Israel when it was made desolate, and over the house of Judah when they went into exile —",
      "T": "Say to the Ammonites: Hear the word of the Lord Yahweh. Thus says the Lord Yahweh: You said 'Aha!' — the exclamation of gleeful contempt — when my sanctuary fell, when the holy place was desecrated. You said it again when Israel's land was stripped bare, and again when Judah's people were marched into exile. You rejoiced at what was the worst day in Israel's history. That is what you are charged with."
    },
    "4": {
      "L": "Behold, therefore I will deliver thee to the men of the east for a possession, and they shall set their palaces in thee, and make their dwellings in thee: they shall eat thy fruit, and they shall drink thy milk.",
      "M": "Therefore I am handing you over to the people of the East as a possession. They will set up their encampments among you and make their dwellings in you; they will eat your fruit and drink your milk.",
      "T": "Therefore, I am giving you to the desert peoples of the East — you will become their possession, their pasture, their dwelling place. Your fields and flocks that you thought were yours will feed them. What Ammon celebrated as Israel's loss, Ammon will now experience as its own."
    },
    "5": {
      "L": "And I will make Rabbah a stable for camels, and the Ammonites a couching place for flocks: and ye shall know that I am the LORD.",
      "M": "I will make Rabbah a pasture for camels and Ammon a resting place for flocks, and you shall know that I am the LORD.",
      "T": "Rabbah — Ammon's capital city, its pride — I will make it a camel pasture. The Ammonite heartland will become a resting place for nomads' flocks. And through this humiliation you will know that I am Yahweh: the God of Israel whose judgment on Israel you mocked is also your judge."
    },
    "6": {
      "L": "For thus saith the Lord GOD: Because thou hast clapped thine hands, and stamped with the feet, and rejoiced in heart with all thy despite against the land of Israel;",
      "M": "For thus says the Lord GOD: Because you clapped your hands and stamped your feet and rejoiced with all your contempt against the land of Israel —",
      "T": "For thus says the Lord Yahweh: You did not merely stand by passively when Israel fell. You clapped your hands in celebration. You stamped your feet in triumph. You let out all the pent-up contempt you had nursed against Israel, reveling in their ruin with every gesture of mockery."
    },
    "7": {
      "L": "Behold, therefore I will stretch out mine hand upon thee, and will deliver thee for a spoil to the heathen; and I will cut thee off from the peoples, and I will cause thee to perish out of the countries: I will destroy thee; and thou shalt know that I am the LORD.",
      "M": "Therefore, behold, I will stretch out my hand against you and hand you over as plunder to the nations. I will cut you off from the peoples and cause you to perish from the lands. I will destroy you, and you shall know that I am the LORD.",
      "T": "Therefore I stretch out my hand against you. You will be plundered by the very nations among whom you thought yourself secure. I will cut you off from the community of peoples — no longer a nation with a future. You will perish from the lands. I will bring you to nothing. And through it all, you will know that I am Yahweh — the one whose judgment is not random, whose hand does not miss."
    },
    "8": {
      "L": "Thus saith the Lord GOD: Because that Moab and Seir do say, Behold, the house of Judah is like unto all the heathen;",
      "M": "Thus says the Lord GOD: Because Moab and Seir say, 'Behold, the house of Judah is like all the other nations' —",
      "T": "Thus says the Lord Yahweh: Moab and Seir have drawn a conclusion from Judah's fall — the same conclusion Israel's enemies always want to draw: 'Look, Judah is just like all the other nations. Their God is like all the other gods. There is nothing distinctive here. Nothing special was ever at stake.'"
    },
    "9": {
      "L": "Therefore, behold, I will open the side of Moab from the cities, from his cities which are on his frontiers, the glory of the country, Bethjeshimoth, Baalmeon, and Kiriathaim,",
      "M": "Therefore I will open the flank of Moab from its cities — from its frontier cities, the glory of the land: Beth-jeshimoth, Baal-meon, and Kiriathaim —",
      "T": "Therefore I will peel open Moab from its frontier — from the border cities that are the pride and gateway of the land: Beth-jeshimoth, Baal-meon, Kiriathaim — the fortified places that defined Moab's eastern edge and made its territory feel secure."
    },
    "10": {
      "L": "Unto the men of the east with the Ammonites, and will give them in possession, that the Ammonites may not be remembered among the nations.",
      "M": "To the men of the East — I will give it to them along with Ammon as a possession, so that the Ammonites may not be remembered among the nations.",
      "T": "I will open that territory to the peoples of the East and hand it over to them — Ammon and Moab alike. The Ammonites, who gloated over Israel's erasure from history, will themselves be erased from history: not remembered, not counted among the nations, not present at the table of peoples."
    },
    "11": {
      "L": "And I will execute judgments upon Moab; and they shall know that I am the LORD.",
      "M": "And I will execute judgments against Moab, and they shall know that I am the LORD.",
      "T": "And on Moab too I will execute my judgments — the sentence passed by the one who governs all nations, not only Israel. They will know that I am Yahweh."
    },
    "12": {
      "L": "Thus saith the Lord GOD: Because that Edom hath dealt against the house of Judah by taking vengeance, and hath greatly offended, and revenged himself upon them;",
      "M": "Thus says the Lord GOD: Because Edom acted revengefully against the house of Judah and is greatly guilty for taking vengeance on them —",
      "T": "Thus says the Lord Yahweh: Edom did not merely stand at a distance. Edom moved against Judah in the hour of Judah's collapse and took personal revenge — acting out of the long bitterness of a brotherly rivalry that went back to Jacob and Esau. Edom was not merely an opportunist; Edom was specifically guilty, intentionally vindictive, and the guilt is severe."
    },
    "13": {
      "L": "Therefore thus saith the Lord GOD: I will also stretch out mine hand upon Edom, and will cut off man and beast from it; and I will make it desolate from Teman; and they of Dedan shall fall by the sword.",
      "M": "Therefore thus says the Lord GOD: I will stretch out my hand against Edom and cut off from it man and beast, and I will make it desolate from Teman — and those of Dedan shall fall by the sword.",
      "T": "Therefore, thus says the Lord Yahweh: My hand goes out against Edom. I will cut off man and beast from its territory — making it as empty as any wilderness. From Teman in the south to Dedan in the east, the sword will sweep through. The pride of Edom — its warriors, its independence, its sense of invulnerability in the rocky heights — will not protect it."
    },
    "14": {
      "L": "And I will lay my vengeance upon Edom by the hand of my people Israel: and they shall do in Edom according to mine anger and according to my fury; and they shall know my vengeance, saith the Lord GOD.",
      "M": "I will lay my vengeance upon Edom by the hand of my people Israel; they will act in Edom according to my anger and my wrath, and they shall know my vengeance, declares the Lord GOD.",
      "T": "My instrument of judgment on Edom will be Israel. The nation that Edom attacked in its moment of weakness will be the agent through whom Edom faces the wrath of God. In Israel's actions against Edom, my own anger and my own fury will be expressed — and Edom will know, beyond any doubt, what divine vengeance feels like. The Lord Yahweh declares it."
    },
    "15": {
      "L": "Thus saith the Lord GOD: Because the Philistines have dealt by revenge, and have taken vengeance with a despiteful heart, to destroy it for the old hatred;",
      "M": "Thus says the Lord GOD: Because the Philistines have acted with vengeance and taken revenge with malice of heart, with ancient enmity seeking to destroy —",
      "T": "Thus says the Lord Yahweh: The Philistines — Israel's oldest, most persistent enemy, the enemy before there was a king in Israel — acted in vengeance when Judah fell. But this was not a spontaneous response to a recent offense. This was ancient hatred, nursing a grudge across centuries, seizing the moment to finally settle it. The 'despiteful heart' is a heart that has been keeping score for a very long time."
    },
    "16": {
      "L": "Therefore thus saith the Lord GOD: Behold, I will stretch out mine hand upon the Philistines, and I will cut off the Cherethites, and destroy the remnant of the sea coast.",
      "M": "Therefore thus says the Lord GOD: I will stretch out my hand against the Philistines and cut off the Cherethites and destroy the remnant of the seacoast.",
      "T": "Therefore, thus says the Lord Yahweh: My hand goes out against the Philistines. The Cherethites — the coastal people who had served as David's bodyguard and whose presence along the Philistine coast represents the whole of that coastal culture — I will cut them off. What remains of the seacoast civilization will be destroyed."
    },
    "17": {
      "L": "And I will execute great vengeance upon them with furious rebukes; and they shall know that I am the LORD, when I shall lay my vengeance upon them.",
      "M": "I will execute great vengeance on them with wrathful rebukes, and they shall know that I am the LORD when I lay my vengeance upon them.",
      "T": "I will execute great vengeance upon them — not merely correction, but the full sentence of a divine judge who has heard every case. In the fury of my rebuke they will know that I am Yahweh: not the regional god of a defeated nation, but the Lord of all nations, who executes justice on every people that acts in malice."
    }
  },
  "26": {
    "1": {
      "L": "And it came to pass in the eleventh year, in the first day of the month, that the word of the LORD came unto me, saying:",
      "M": "In the eleventh year, on the first day of the month, the word of the LORD came to me:",
      "T": "In the eleventh year of Jehoiachin's exile, on the first day of the month — the month is not named, which is unusual; some scholars suggest a scribal omission — Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, because that Tyrus hath said against Jerusalem, Aha, she is broken that was the gate of the peoples: she is turned unto me: I shall be replenished, now she is laid waste;",
      "M": "Son of man, because Tyre has said against Jerusalem, 'Aha! The gate of the peoples is broken; it has swung open to me — now that she is laid waste I shall be filled.'",
      "T": "Son of man, here is Tyre's crime: Tyre looked at Jerusalem's fall and said 'Aha!' — the same word of gloating contempt that Ammon used. But Tyre's calculation was economic. Jerusalem had been 'the gate of the peoples' — the major junction of trade routes connecting Egypt, Arabia, and Mesopotamia. With Jerusalem broken, that traffic would divert northward. Tyre's harbors would fill. Tyre would profit from Judah's ruin."
    },
    "3": {
      "L": "Therefore thus saith the Lord GOD: Behold, I am against thee, O Tyrus, and will cause many nations to come up against thee, as the sea causeth his waves to come up.",
      "M": "Therefore thus says the Lord GOD: I am against you, Tyre, and I will bring many nations against you as the sea brings up its waves.",
      "T": "Therefore, thus says the Lord Yahweh: I am against you, Tyre. Not one nation — not just Babylon — but wave after wave of nations will come against you, as the sea sends its waves in endless succession against a shore. The image is deliberate: Tyre sits on the sea and has mastered it; now the sea itself becomes the image of its destruction."
    },
    "4": {
      "L": "And they shall destroy the walls of Tyrus, and break down her towers: I will also scrape her dust from her, and make her like the top of a rock.",
      "M": "They will destroy the walls of Tyre and tear down her towers; I will also scrape the soil from her and make her a bare rock.",
      "T": "They will bring down the walls, shatter the towers. And then I will do something the conquerors alone cannot — I will scrape her clean to the bedrock. Tyre means 'rock'; by the time I am done, that will be literally all that remains: bare limestone swept bare of soil, buildings, people, memory. Tyre the impregnable island fortress will become nothing but the rock it was built on."
    },
    "5": {
      "L": "It shall be a place for the spreading of nets in the midst of the sea: for I have spoken it, saith the Lord GOD: and it shall become a spoil to the nations.",
      "M": "She will become a place in the middle of the sea for the spreading of nets; for I have spoken, declares the Lord GOD — she will become plunder for the nations.",
      "T": "Where great ships once docked and merchants haggled and wealth accumulated, fishermen will spread their nets to dry in the sun. That is the future of Tyre — a bare rock in the sea, useful only as a surface on which to lay out fishing nets. I, the Lord Yahweh, have spoken it, and what I speak becomes history."
    },
    "6": {
      "L": "And her daughters which are in the field shall be slain by the sword; and they shall know that I am the LORD.",
      "M": "Her daughters on the mainland will be slain by the sword, and they shall know that I am the LORD.",
      "T": "The settlements on the mainland — the 'daughters' of Tyre, the dependent towns along the Phoenician coast — will fall to the sword before the island city is even reached. And through this destruction, the survivors will know that I am Yahweh: the God who spoke, the God whose word is now audible in the sound of their cities falling."
    },
    "7": {
      "L": "For thus saith the Lord GOD: Behold, I will bring upon Tyrus Nebuchadrezzar king of Babylon, a king of kings, from the north, with horses, and with chariots, and with horsemen, and companies, and much people.",
      "M": "For thus says the Lord GOD: I am bringing against Tyre from the north Nebuchadnezzar king of Babylon, king of kings, with horses, chariots, horsemen, troops, and a great army.",
      "T": "For thus says the Lord Yahweh: The instrument of my judgment is named. From the north comes Nebuchadnezzar of Babylon — the text calls him 'king of kings,' the title claimed by the great empires: the one to whom all other kings submit. He comes with the full apparatus of imperial military power: cavalry, chariots, columns of infantry, a host beyond counting."
    },
    "8": {
      "L": "He shall slay with the sword thy daughters in the field: and he shall make a fort against thee, and cast a mount against thee, and lift up the buckler against thee.",
      "M": "He will slay your mainland daughters with the sword and erect siege works against you — he will raise a mound, set up siege engines, and raise the shield against you.",
      "T": "He will cut down the mainland towns first — clearing the coast before turning to the island. Then the siege machinery is erected: earthworks piled up, battering platforms, the great leather-covered shields that protect attackers as they advance on the walls. The methodical violence of ancient siege warfare, turned against the most fortified city of the ancient world."
    },
    "9": {
      "L": "And he shall set engines of war against thy walls, and with his axes he shall break down thy towers.",
      "M": "He will direct his battering rams against your walls and break down your towers with his axes.",
      "T": "Battering rams against walls that were built to be impenetrable. Axes against towers that have withstood every previous enemy. The mechanical certainty of the description reflects Ezekiel's prophetic certainty: this is not speculation but announcement."
    },
    "10": {
      "L": "By reason of the abundance of his horses their dust shall cover thee: thy walls shall shake at the noise of the horsemen, and of the wheels, and of the chariots, when he shall enter into thy gates, as men enter into a city wherein is made a breach.",
      "M": "Because of his many horses their dust will cover you; your walls will shake at the noise of horsemen, wheels, and chariots when he enters your gates as men enter a breached city.",
      "T": "The sheer scale of the army will be its own weapon — so many horses that their dust cloud alone covers the city. The noise of the approach: the hammering of chariot wheels on stone, the thundering of cavalry, the shouting of troops, the walls trembling with it. The imagery of breaking through a breached gate was the ancient image of irreversible conquest; once the wall is breached, it is over."
    },
    "11": {
      "L": "With the hoofs of his horses shall he tread down all thy streets: he shall slay thy people by the sword, and thy strong garrisons shall go down to the ground.",
      "M": "His horses' hooves will trample all your streets; he will slaughter your people with the sword and your strong pillars will collapse to the ground.",
      "T": "When the breach is made, the cavalry rides through every street. The people are cut down where they stand. The famous standing stones of Tyre — the sacred pillars that marked its temples and proclaimed its religious prestige — will be toppled to the ground. Nothing will be left standing."
    },
    "12": {
      "L": "And they shall make a spoil of thy riches, and make a prey of thy merchandise: and they shall break down thy walls, and destroy thy pleasant houses: and they shall lay thy stones and thy timber and thy dust in the midst of the water.",
      "M": "They will plunder your wealth and loot your merchandise; they will break down your walls and destroy your fine houses, and they will cast your stones, your timber, and your soil into the sea.",
      "T": "The spoil of centuries of accumulated trade wealth — stripped. The merchandise stockpiled in Tyre's famous warehouses — carried off. The walls demolished stone by stone. The houses — the 'delightful houses,' the beautiful Phoenician architecture — destroyed. And then, in the act that proves this is not just conquest but annihilation: the very stones and timbers and dust are thrown into the sea. The causeway Alexander would build, casting Tyre's own ruins into the water to reach the island, is historically the fulfillment of this verse."
    },
    "13": {
      "L": "And I will cause the noise of thy songs to cease; and the sound of thy harps shall be no more heard.",
      "M": "I will put an end to the noise of your songs, and the sound of your harps will be heard no more.",
      "T": "Tyre was a city of music — the great cosmopolitan port city where the sound of feasting and entertainment was constant. I will silence it. The songs, the harps, the noise of prosperity — all of it cut off. Silence where there was always sound is its own kind of judgment."
    },
    "14": {
      "L": "And I will make thee like the top of a rock: thou shalt be a place to spread nets upon; thou shalt be built no more: for I the LORD have spoken it, saith the Lord GOD.",
      "M": "I will make you a bare rock; you will be a place for the spreading of nets and will never be rebuilt, for I the LORD have spoken, declares the Lord GOD.",
      "T": "Bare rock for fish nets. Not rebuilt — ever. The finality of this is total. 'I, Yahweh, have spoken it' — the Lord Yahweh adds his seal to the declaration. What God speaks into history is not reversible. The decree against Tyre is permanent. The rock will remain bare."
    },
    "15": {
      "L": "Thus saith the Lord GOD to Tyrus: Shall not the isles shake at the sound of thy fall, when the wounded cry, when the slaughter is made in the midst of thee?",
      "M": "Thus says the Lord GOD to Tyre: Will not the coastlands tremble at the sound of your fall — at the cry of the wounded, the slaughter in your midst?",
      "T": "Thus says the Lord Yahweh to Tyre: Your fall will send shockwaves through every coastland. The cry of the wounded, the sound of the massacre — it will carry across the sea. Every island kingdom, every coastal city that has traded with you and depended on you, will feel the trembling of the day you go down."
    },
    "16": {
      "L": "Then all the princes of the sea shall come down from their thrones, and lay away their robes, and put off their broidered garments: they shall clothe themselves with trembling; they shall sit upon the ground, and shall tremble at every moment, and be astonished at thee.",
      "M": "Then all the princes of the sea will descend from their thrones, remove their robes, and strip off their embroidered garments; they will clothe themselves with trembling, sit on the ground, tremble continually, and be appalled at you.",
      "T": "Every king of the Mediterranean coastlands — every ruler of every seafaring nation that depended on the order Tyre represented — will step down from their thrones in a formal gesture of mourning. The embroidered royal robes come off. They sit on the ground — the ancient posture of lamentation and shock. They tremble. They cannot stop trembling. Not merely grief, but the existential fear of someone who has just watched the most secure thing they knew collapse. If Tyre can fall, nothing is safe."
    },
    "17": {
      "L": "And they shall take up a lamentation for thee, and say to thee, How art thou destroyed, that wast inhabited of seafaring men, the renowned city, which wast strong in the sea, she and her inhabitants, which cause their terror to be on all that haunt it!",
      "M": "They will raise a lamentation over you and say to you: 'How you are destroyed, you who were inhabited by seafarers — you renowned city, mighty on the sea! You and your citizens spread your terror over all who dwell there.'",
      "T": "And they will raise a lament — the formal funeral song, spoken over someone already dead:\n'How you are destroyed!\nYou were home to all who sail the seas;\nyou were the famous city, strong on the water.\nYou and your citizens made the whole sea tremble.\nWhere have you gone?'\nThe past tense of the lament is the voice of disbelief: the city that was the permanent fixture of the ancient world has become a memory."
    },
    "18": {
      "L": "Now shall the isles tremble in the day of thy fall; yea, the isles that are in the sea shall be troubled at thy departure.",
      "M": "Now the coastlands tremble on the day of your fall; the islands in the sea are dismayed at your end.",
      "T": "Now — on the actual day of your fall — the trembling the kings anticipated becomes real. Every island in the sea is dismayed. The trembling is not merely geopolitical calculation; it is the visceral terror of populations who understood their security to rest on the stability of Tyre's system of trade and power. Tyre's end is the end of a world."
    },
    "19": {
      "L": "For thus saith the Lord GOD: When I shall make thee a desolate city, like the cities that are not inhabited; when I shall bring up the deep upon thee, and great waters shall cover thee;",
      "M": "For thus says the Lord GOD: When I make you a desolate city like cities that are not inhabited, when I bring up the deep over you and the great waters cover you —",
      "T": "For thus says the Lord Yahweh: When I make you desolate — not merely conquered and rebuilt, but emptied like the ancient ruined cities that stand without inhabitants — when I bring the deep itself up over you, when the great primordial waters cover you, that is when you will understand the full dimension of what has happened. The sea does not merely lap at your shores; it reclaims you."
    },
    "20": {
      "L": "When I shall bring thee down with them that descend into the pit, with the people of old time, and shall set thee in the low parts of the earth, in places desolate of old, with them that go down to the pit, that thou be not inhabited; and I shall set glory in the land of the living;",
      "M": "I will bring you down with those who descend to the pit, to the ancient peoples, and I will place you in the depths of the earth, in ancient desolate places, with those who go down to the pit, so that you will not be inhabited — but I will set glory in the land of the living.",
      "T": "I will bring you down into the Pit — into the realm of the dead, with all the ancient nations and empires that preceded you and are now silent. The depths of the earth, the ancient desolate places where the great dead kingdoms dwell — Assyria, old Egypt, civilizations older still — you will join them there. You will not be inhabited. While the land of the living receives its glory — Israel restored, the covenant honored — Tyre will dwell among the ruins of everything that tried to replace God's purposes with its own power."
    },
    "21": {
      "L": "I will make thee a terror, and thou shalt be no more: though thou be sought for, yet shalt thou never be found again, saith the Lord GOD.",
      "M": "I will make you an object of terror, and you will be no more. Though you are sought, you will never be found again, declares the Lord GOD.",
      "T": "I will make you a terror — a byword spoken to make people shudder, the example invoked when people want to name the most devastating fall they know. And then you will simply not exist. If someone looks for you — searches for the great Tyre on its rock in the sea — they will not find it. The Lord Yahweh declares it: sought, and never found."
    }
  },
  "27": {
    "1": {
      "L": "The word of the LORD came again unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Now, thou son of man, take up a lamentation for Tyrus;",
      "M": "Now, son of man, raise a lamentation over Tyre.",
      "T": "Now, son of man, raise a funeral lament over Tyre. The form matters: a qînāh is the song sung at a death. Ezekiel is commanded to sing Tyre's funeral song while the city still stands — prophetic speech that treats the future as accomplished fact, because when God has spoken it, it is."
    },
    "3": {
      "L": "And say unto Tyrus, O thou that art situate at the entry of the sea, which art a merchant of the people for many isles, Thus saith the Lord GOD: O Tyrus, thou hast said, I am of perfect beauty.",
      "M": "Say to Tyre, you who are situated at the gateway of the sea, merchant to many coastlands: Thus says the Lord GOD: O Tyre, you have said, 'I am perfect in beauty.'",
      "T": "Say this to Tyre — the city that stands at the entrance to the sea, that has served as merchant to every coastland, that has traded with every nation the Mediterranean world contains:\nThus says the Lord Yahweh:\nO Tyre, you have declared yourself perfectly beautiful.\nYou have made your magnificence your identity, your pride, your boast.\nThat claim is what this lament now answers."
    },
    "4": {
      "L": "Thy borders are in the midst of the seas, thy builders have perfected thy beauty.",
      "M": "Your territory is in the heart of the seas; your builders have perfected your beauty.",
      "T": "Your borders are the sea itself — the water is your territory, your defense, your identity.\nYour builders were artists:\nthey built you to be beautiful, and they succeeded."
    },
    "5": {
      "L": "They have made all thy ship boards of fir trees of Senir: they have taken cedars from Lebanon to make masts for thee.",
      "M": "They made all your planks of fir trees from Senir; they took cedars from Lebanon to make your mast.",
      "T": "Your planking: fir trees from Senir — the slopes of Hermon, the finest timber of the upland forests.\nYour mast: cedar from Lebanon — the great cedar, the king of trees, the wood that built Solomon's temple.\nTyre is built from the best materials the world offers."
    },
    "6": {
      "L": "Of the oaks of Bashan have they made thine oars; the company of the Ashurites have made thy benches of ivory, brought out of the isles of Chittim.",
      "M": "They made your oars from oaks of Bashan; they made your deck of cypress wood inlaid with ivory from the coasts of Cyprus.",
      "T": "Oars of Bashan oak — hard, dense wood from the great forests east of the Jordan.\nDecking of cypress inlaid with ivory from Cyprus:\nthe luxury materials of the ancient world fitted into a working ship.\nTyre does not merely trade in beauty; Tyre embodies it."
    },
    "7": {
      "L": "Fine linen with broidered work from Egypt was that which thou spreadest forth to be thy sail; blue and purple from the isles of Elishah was that which covered thee.",
      "M": "Your sail was of fine embroidered linen from Egypt; your awning was of blue and purple from the coasts of Elishah.",
      "T": "Your sail: embroidered linen from Egypt — not ordinary canvas but decorated cloth, a sail that proclaimed your prestige at sea.\nYour awning: blue and purple dye from the coasts of Elishah — the precious Tyrian purple, the color of royalty, shading the deck of Tyre's own ship.\nEven the colors are expensive."
    },
    "8": {
      "L": "The inhabitants of Zidon and Arvad were thy mariners: thy wise men, O Tyrus, that were in thee, were thy pilots.",
      "M": "The inhabitants of Sidon and Arvad were your oarsmen; your own skilled men, O Tyre, served as your pilots.",
      "T": "The rowers: men from Sidon and Arvad — fellow Phoenician cities, Tyre's neighbors and kin.\nThe pilots: Tyre's own skilled men, trained navigators who knew every harbor and current of the Mediterranean.\nThe crew reflects the breadth of Phoenician maritime civilization."
    },
    "9": {
      "L": "The ancients of Gebal and the wise men thereof were in thee thy calkers: all the ships of the sea with their mariners were in thee to occupy thy merchandise.",
      "M": "The elders of Gebal and its skilled craftsmen were in you as caulkers; all the ships of the sea with their sailors were in you to trade your merchandise.",
      "T": "The master craftsmen of Gebal — the ancient Phoenician city known to Greeks as Byblos — served as Tyre's shipwrights, the ones who caulked the seams and kept the hull watertight.\nAnd from every port of the sea, ships and their crews came to Tyre:\nthe entire maritime world made Tyre its center."
    },
    "10": {
      "L": "They of Persia and of Lud and of Phut were in thine army, thy men of war: they hanged the shield and helmet in thee; they set forth thy comeliness.",
      "M": "Persia, Lud, and Put served as soldiers in your army; they hung shield and helmet in you, adding to your splendor.",
      "T": "Even Tyre's military was a display of its reach:\nPersians from the far east, Lydians from Asia Minor, Libyans from Africa —\nforeign mercenaries whose weapons and armor were hung on Tyre's walls like trophies,\nmaking Tyre's very military might into a visual demonstration of its international power."
    },
    "11": {
      "L": "The men of Arvad with thine army were upon thy walls round about, and the Gammadims were in thy towers: they hanged their shields upon thy walls round about; they have made thy beauty perfect.",
      "M": "The men of Arvad and your army were all around on your walls, and the Gammadim were in your towers; they hung their shields on your walls all around, making your beauty perfect.",
      "T": "Along the walls: men of Arvad, the Gammadim — garrison troops from every direction,\ntheir shields hung decoratively on the battlements,\na ring of military art around the perimeter.\nEverything about Tyre was perfect — designed, deliberate, beautiful.\nThat is the point of this entire catalogue:\nthe more perfect the beauty, the more absolute the loss."
    },
    "12": {
      "L": "Tarshish was thy merchant by reason of the multitude of all kind of riches; with silver, iron, tin, and lead, they traded in thy fairs.",
      "M": "Tarshish was your merchant because of your abundant wealth of every kind; with silver, iron, tin, and lead they traded at your markets.",
      "T": "Now the cargo manifest begins — and it reads like an atlas of the ancient world.\nTarshish: the far western Mediterranean, perhaps Tartessos in Spain — the edge of the known world.\nThey brought the raw metals of the western mines: silver, iron, tin, lead.\nTyre drew the wealth of the west."
    },
    "13": {
      "L": "Javan, Tubal, and Meshech, they were thy merchants: they traded the persons of men and vessels of brass in thy market.",
      "M": "Javan, Tubal, and Meshech were your traders; they traded human beings and vessels of bronze in your markets.",
      "T": "Javan — the Greeks. Tubal and Meshech — peoples of Asia Minor and the Black Sea region.\nThey traded in two commodities: bronze vessels and human lives.\nThe text does not soften it: אָדָם, 'persons of men' — the slave trade.\nTyre's magnificent wealth was partly built on human trafficking.\nRevelation 18:13 will quote this verse in the judgment on Rome.\nWhat Tyre did, every great trading empire has done."
    },
    "14": {
      "L": "They of the house of Togarmah traded in thy fairs with horses and horsemen and mules.",
      "M": "From Beth-togarmah they traded horses, war horses, and mules at your markets.",
      "T": "Beth-togarmah — Armenia, or the region east of Anatolia — supplied the horse trade:\nwork mules, cavalry horses, war horses.\nThe ancient world ran on horses; Tyre was the exchange through which that power was distributed."
    },
    "15": {
      "L": "The men of Dedan were thy merchants; many isles were the merchandise of thine hand: they brought thee for a present horns of ivory and ebony.",
      "M": "The men of Dedan were your traders; many coastlands were your markets — they brought you tribute of ivory tusks and ebony.",
      "T": "Dedan — the traders of northwest Arabia — and the coastlands brought tribute:\nivory tusks, ebony wood —\nthe luxury materials of sub-Saharan Africa and the Indian Ocean trade,\nfunneled through Arabia to Tyre."
    },
    "16": {
      "L": "Syria was thy merchant by reason of the multitude of the wares of thy making: they occupied in thy fairs with emeralds, purple, and broidered work, and fine linen, and coral, and agate.",
      "M": "Syria was your merchant because of your many products; they traded at your markets with emeralds, purple, embroidered cloth, fine linen, coral, and rubies.",
      "T": "Syria — Aram, Tyre's eastern neighbor — traded luxury goods:\nprecious stones, the purple dye for which Phoenicia was famous,\nembroidered cloth, fine linen, coral, and agate.\nThe luxury textile and gem trade of the ancient Near East, concentrated at Tyre."
    },
    "17": {
      "L": "Judah, and the land of Israel, they were thy merchants: they traded in thy market wheat of Minnith, and Pannag, and honey, and oil, and balm.",
      "M": "Judah and the land of Israel were your traders; they traded wheat from Minnith, cakes, honey, olive oil, and balm at your markets.",
      "T": "Judah and Israel — the covenant people — also traded with Tyre.\nThey brought what the land of promise produced:\nwheat from Minnith in Gilead, sweet cakes or millet-grain, honey, olive oil, and the healing balm of Gilead.\nSolomon had established this trade (1 Kings 5); it persisted for centuries.\nEven Israel was drawn into Tyre's economic orbit."
    },
    "18": {
      "L": "Damascus was thy merchant in the multitude of the wares of thy making, for the multitude of all riches; in the wine of Helbon, and white wool.",
      "M": "Damascus was your merchant for your many products because of your abundant wealth — with the wine of Helbon and white wool.",
      "T": "Damascus — the great inland city, hub of the northern overland routes —\ntraded the famous wine of Helbon, a luxury vintage prized across the ancient world,\nand the fine white wool of the Syrian highlands.\nEvery direction of the compass fed into Tyre."
    },
    "19": {
      "L": "Dan also and Javan going to and fro occupied in thy fairs: bright iron, cassia, and calamus, were in thy market.",
      "M": "Dan and Javan from Uzal traded at your markets; wrought iron, cassia, and fragrant calamus were among your wares.",
      "T": "From the north: Dan and the Greeks of Uzal (perhaps in South Arabia),\ntrading wrought iron, cassia — the spice used in sacred anointing oil (Exodus 30:24),\nand fragrant calamus — the perfumer's cane, the aromatic reed prized for incense and medicine.\nThe spice trade: the ancient world's most valuable commerce by weight."
    },
    "20": {
      "L": "Dedan was thy merchant in precious clothes for chariots.",
      "M": "Dedan traded with you in saddlecloths for riding.",
      "T": "Dedan appears again — the Arabian traders who supplied the luxury cloth\nused as saddlecloths for horses and riding animals.\nEven the comfort of the riders who drove the trade routes was provisioned through Tyre."
    },
    "21": {
      "L": "Arabia, and all the princes of Kedar, they occupied with thee in lambs, and rams, and goats: in these were they thy merchants.",
      "M": "Arabia and all the princes of Kedar traded with you in lambs, rams, and goats; these were your merchants.",
      "T": "Arabia and the princes of Kedar — the great pastoral tribes of the desert —\nbrought the livestock wealth of the steppe:\nlambs, rams, goats.\nThe pastoral economy of the desert and the merchant economy of the sea city\nmet at Tyre's markets."
    },
    "22": {
      "L": "The merchants of Sheba and Raamah, they were thy merchants: they occupied in thy fairs with chief of all spices, and with all precious stones, and gold.",
      "M": "The merchants of Sheba and Raamah traded with you; they traded in the finest of all spices, all kinds of precious stones, and gold.",
      "T": "Sheba and Raamah — the incense traders of South Arabia, perhaps modern Yemen,\nthe source of frankincense and myrrh and the finest spice varieties known to the ancient world.\nThey brought the choicest spices, every precious stone, and gold.\nThe luxury goods at the top of the ancient trade hierarchy all passed through Tyre."
    },
    "23": {
      "L": "Haran, and Canneh, and Eden, the merchants of Sheba, Asshur, and Chilmad, were thy merchants.",
      "M": "Haran, Canneh, Eden, the traders of Sheba, Asshur, and Chilmad were your merchants.",
      "T": "The list widens to the Mesopotamian world:\nHaran — the city where Abraham's family settled,\nCanneh and Eden — northern Mesopotamian trading centers,\nAsshur — the original Assyrian city on the Tigris, ancient heart of empire,\nChilmad — perhaps near modern Mosul.\nBabylon, Assyria, the whole Fertile Crescent arc: all roads led to Tyre."
    },
    "24": {
      "L": "These were thy merchants in all sorts of things, in blue clothes, and broidered work, and in chests of rich apparel, bound with cords, and made of cedar, among thy merchandise.",
      "M": "These traded with you in choice garments, in blue and embroidered cloth, in chests of fine clothing bound with cords — among your merchandise.",
      "T": "These Mesopotamian merchants brought the textiles of the great inland cities:\npremium garments in blue and embroidered work,\nluxury clothing packed in cedar chests and bound with cords —\nthe way wealthy merchandise was shipped across the desert.\nEven the packaging was expensive."
    },
    "25": {
      "L": "The ships of Tarshish did sing of thee in thy market: and thou wast replenished, and made very glorious in the midst of the seas.",
      "M": "The ships of Tarshish carried your merchandise; you were filled and made very glorious in the heart of the seas.",
      "T": "The great Tarshish ships — the ocean-going vessels that made the longest voyages —\ncarried Tyre's merchandise to the ends of the earth.\nAnd Tyre was filled:\nfilled with wealth, filled with glory, the most magnificent city in the heart of the most central sea.\nThis is the peak of the description — beauty and wealth and fame at their absolute height.\nHere the ship is perfectly built, perfectly crewed, perfectly loaded.\nNow the wind shifts."
    },
    "26": {
      "L": "Thy rowers have brought thee into great waters: the east wind hath broken thee in the midst of the seas.",
      "M": "Your rowers have brought you out into the great waters; the east wind has wrecked you in the heart of the seas.",
      "T": "Your rowers brought you into the deep — out into the open waters where the storms are.\nAnd there the east wind struck.\nThe east wind in Hebrew poetry is the wind of judgment, the wind of the desert that desiccates and destroys\n(see Ps 48:7; Jer 18:17).\nIn the heart of the seas — at the very center of Tyre's domain —\nTyre was wrecked.\nThe ship that had survived every voyage broke on the judgment of God."
    },
    "27": {
      "L": "Thy riches, and thy fairs, thy merchandise, thy mariners, and thy pilots, thy calkers, and the occupiers of thy merchandise, and all thy men of war, that are in thee, and in all thy company which is in the midst of thee, shall fall into the midst of the seas in the day of thy ruin.",
      "M": "Your wealth, your merchandise, your goods, your mariners and pilots, your caulkers and dealers, all your men of war, and the whole assembly within you — all will sink into the heart of the seas on the day of your ruin.",
      "T": "Everything enumerated in the cargo manifest now sinks:\nthe wealth — gone.\nThe merchandise — gone.\nThe mariners who knew every sea — gone.\nThe pilots who navigated every coast — gone.\nThe craftsmen who built the ship — gone.\nThe merchants who filled the hold — gone.\nThe soldiers who defended it — gone.\nThe entire company, the whole magnificent assembly:\non the day of the wreck, it all sinks together\nto the heart of the seas."
    },
    "28": {
      "L": "The suburbs shall shake at the sound of the cry of thy pilots.",
      "M": "At the sound of the cry of your pilots the countryside shakes.",
      "T": "When the pilots of Tyre cry out — the trained navigators, the most skilled sailors in the world,\nthe ones who never panic —\nwhen they cry out in terror,\nthe very coastlands tremble at the sound."
    },
    "29": {
      "L": "And all that handle the oar, the mariners, and all the pilots of the sea, shall come down from their ships, they shall stand upon the land;",
      "M": "All who handle the oar — the mariners and all the pilots of the sea — will come down from their ships and stand on the shore.",
      "T": "Every sailor, every captain, every harbor pilot hears the news and comes ashore.\nThey cannot stay on their ships.\nThey stand on the land — the land they normally left behind —\nand from the shore they watch what has happened to Tyre."
    },
    "30": {
      "L": "And shall cause their voice to be heard against thee, and shall cry bitterly, and shall cast up dust upon their heads, they shall wallow themselves in the ashes:",
      "M": "They will raise their voices over you and cry out bitterly; they will throw dust on their heads and roll in ashes.",
      "T": "They cry out — the wordless cry of witnesses to catastrophe.\nThey throw dust on their heads:\nthe ancient gesture of mourning, of being overwhelmed, of having no adequate response.\nThey wallow in ashes:\nnot mere ceremony but the physical expression of grief that will not be contained.\nThese are the men who never weep. They are weeping."
    },
    "31": {
      "L": "And they shall make themselves utterly bald for thee, and gird them with sackcloth, and they shall weep for thee with bitterness of heart and bitter wailing.",
      "M": "They will shave their heads completely for you and put on sackcloth; they will weep for you with bitter grief and bitter lamentation.",
      "T": "They shave their heads — total mourning, the sign of extreme grief.\nSackcloth replaces the fine clothing they wore as wealthy sea captains.\nAnd they weep:\nnot quietly, not composed,\nbut with the bitter wailing that acknowledges a loss too great to accept.\nTyre's death is their death too.\nEverything they built their lives on has sunk with the ship."
    },
    "32": {
      "L": "And in their wailing they shall take up a lamentation for thee, and lament over thee, saying: What city is like Tyrus, like the destroyed in the midst of the sea?",
      "M": "In their wailing they will raise a lament over you and sing over you: 'Who was ever destroyed like Tyre, like one silenced in the midst of the sea?'",
      "T": "Out of their weeping comes the formal lament — the qînāh they now actually sing:\n'What city was like Tyre?\nWhat city has ever been destroyed like Tyre?\nSilenced in the middle of the sea —\nthe place that was supposed to be its kingdom\nbecame its grave.'"
    },
    "33": {
      "L": "When thy wares went forth out of the seas, thou filledst many people; thou didst enrich the kings of the earth with the multitude of thy riches and of thy merchandise.",
      "M": "When your merchandise went out over the seas, you satisfied many peoples; with your great wealth and goods you enriched the kings of the earth.",
      "T": "They remember what Tyre was:\nWhen your ships put out — when the holds were full and the sails were set —\nyou fed nations. You satisfied peoples who depended on your trade.\nYou enriched kings.\nThe kings of the earth measured their wealth by what they received from Tyre.\nThat was what you were.\nThat is what is gone."
    },
    "34": {
      "L": "In the time when thou shalt be broken by the seas in the depths of the waters thy merchandise and all thy company in the midst of thee shall fall.",
      "M": "Now you are wrecked by the seas, in the depths of the waters; your merchandise and all your company have sunk with you.",
      "T": "But now:\nbroken by the seas you once commanded,\nsunk into the depths you once crossed in triumph.\nThe merchandise — all of it catalogued, all of it gone.\nThe company — every person named in those lists — sunk with you.\nThe depth of the sea that was Tyre's highway is now Tyre's tomb."
    },
    "35": {
      "L": "All the inhabitants of the isles shall be astonished at thee, and their kings shall be sore afraid, they shall be troubled in their countenance.",
      "M": "All the inhabitants of the coastlands are appalled at you; their kings shudder with horror and their faces are convulsed with fear.",
      "T": "Every coastal people stares in appalled silence.\nThe kings — the ones who traded with Tyre, who depended on Tyre, who feared Tyre —\nshudder with a fear that twists their faces.\nWhat they are looking at is not just the fall of a city.\nThey are looking at the demonstration that nothing is permanent,\nthat power and beauty and wealth can sink without warning\nto the bottom of the sea."
    },
    "36": {
      "L": "The merchants among the people shall hiss at thee; thou shalt be a terror, and never shalt be any more.",
      "M": "The merchants among the peoples hiss at you; you have come to a horrible end and will be no more forever.",
      "T": "The merchants — the people who knew Tyre best, who had done business with Tyre for generations —\nhiss.\nThe hiss is the sound of horror and disbelief, the sound of someone witnessing something they cannot process.\nYou have come to a terrible end.\nAnd you will be no more — forever.\nThat is the last word of the lament:\nnot 'until you are rebuilt'\nnot 'until your glory returns'\nbut: forever.\nThe Lord Yahweh has the last word, and the last word is silence."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 25–27 written.')

if __name__ == '__main__':
    main()
