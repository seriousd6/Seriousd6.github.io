"""
MKT Isaiah chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-13-18.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — consistent with mkt-isaiah-1-2 and 3-6
- H136 (אֲדֹנָי): "Lord" (L/M/T) — the title Adonai, distinct from the Tetragrammaton
- H6635 (צְבָאוֹת): "of hosts" (L/M/T) throughout — Isaiah's signature title for YHWH
- H4853 (מַשָּׂא): "burden" (L) / "oracle" (M) / "oracle" or "the oracle against" (T)
  — the massa oracles are judgment speeches against foreign nations; T names the adversarial
  direction explicitly in headings
- H7706 (שַׁדַּי): "Almighty" (L/M/T, 13:6) — Shaddai; the "destruction from the Almighty"
  wordplay (shod from Shaddai) is noted but untranslatable; T names it
- H7585 (שְׁאוֹל): "Sheol" (L/M/T) — transliterated throughout; first occurrence in 14:9
  adds brief descriptive framing in T
- H1966 (הֵילֵל, 14:12): "shining one" (L) / "Day Star" (M) / "Day Star" (T) — the Hebrew
  helel means 'shining one / day star'; the Latin Vulgate's "Lucifer" has dominated tradition
  but the Hebrew root is about brightness; T retains "Day Star" and notes the tradition;
  the passage is an extended taunt against the king of Babylon, not a direct statement about
  Satan, though the NT echoes it (Luke 10:18, Rev 22:16)
- H5945 (עֶלְיוֹן, 14:14): "Most High" (L/M) / "El Elyon — the Most High" (T) — the divine
  title; T makes the audacity of the claim vivid by naming the Canaanite epithet
- H2617 (חֶסֶד, 16:5): "steadfast love" (L) / "covenant faithfulness" (M) / "hesed" (T) —
  transliterated in T for the single appearance here; the messianic throne oracle in 16:5
  makes the covenantal dimension central
- H4941 (מִשְׁפָּט): "justice" / "judgment" throughout — covenantal standard, not merely
  procedural; same convention as mkt-isaiah-3-6
- H842 (אֲשֵׁרָה / אֲשֵׁרִים, 17:8): "Asherim" — transliterated; Canaanite fertility
  cult poles; T does not domesticate the term
- H430 (אֱלֹהִים): "God" throughout
- Poetry structure: chapters 13–18 are almost entirely prophetic poetry / oracular verse.
  T tier uses line breaks throughout. L and M use prose sentences.
- Aspect: waw-consecutive imperfects rendered as narrative past/future depending on context;
  prophecies in chapters 13–14 are future from Isaiah's perspective, rendered in future tense
- Divine passive: 14:19 "you are cast out" — the agent is YHWH; noted in T
- The fall of Lucifer taunt (14:12–15): treated as an extended poetic taunt against the king
  of Babylon; the cosmic imagery reflects ANE mythological language for royal hubris
- Isaiah 16:13–14: an editorial note distinguishing a prior oracle from a new, time-stamped
  word of Yahweh; both tiers preserve this editorial structure
- Chapter 17:12–14 ("woe to the rushing of nations"): an appended oracle; the sudden shift
  from the Damascus/Israel material to a cosmic enemy is preserved in all tiers
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
  "13": {
    "1": {
      "L": "The burden of Babylon, which Isaiah the son of Amoz saw.",
      "M": "The oracle concerning Babylon, which Isaiah son of Amoz saw in vision.",
      "T": "The oracle against Babylon — what Isaiah son of Amoz saw."
    },
    "2": {
      "L": "Upon a bare mountain raise a banner; lift the voice to them, wave the hand, that they may enter the gates of the nobles.",
      "M": "Raise a banner on the bare mountain! Lift your voice to them! Wave your hand, so that they may march through the gates of the rulers!",
      "T": "Up — plant the battle standard on the windswept peak!\nRaise your voice to them, wave them forward —\nlet them pour through the gates of the princes!"
    },
    "3": {
      "L": "I have commanded my consecrated ones; I have also called my warriors for my anger, those who rejoice in my exaltation.",
      "M": "I have given orders to my consecrated troops; I have summoned my warriors to carry out my wrath — those who exult in my majesty.",
      "T": "I have called out my consecrated ones by name;\nmy mighty warriors are assembled for the work of my anger —\nthose who take fierce joy in my supremacy."
    },
    "4": {
      "L": "Hark, the noise of a multitude on the mountains, like a great people! Hark, the tumultuous noise of the kingdoms of the nations gathering! The LORD of hosts is mustering a host for battle.",
      "M": "Listen — the roar of multitudes on the mountains, like a vast army! The clamour of kingdoms and nations massing together! The LORD of hosts is assembling his battle force.",
      "T": "Hear the thunder of it — multitudes on the mountains like a vast army,\nthe uproar of kingdoms and nations massing together.\nYahweh of hosts is mustering his army for war."
    },
    "5": {
      "L": "They come from a far country, from the end of the heavens — the LORD and the weapons of his indignation — to destroy the whole earth.",
      "M": "They are coming from a distant land, from the far end of the heavens — the LORD himself with the instruments of his wrath — to lay waste to the whole earth.",
      "T": "They come from the far horizon, from the end of the sky —\nYahweh himself, with every weapon his wrath requires —\nto reduce the whole earth to rubble."
    },
    "6": {
      "L": "Howl, for the day of the LORD is near; as destruction from the Almighty it will come.",
      "M": "Wail, for the day of the LORD is close at hand — it will come as devastation from the Almighty.",
      "T": "Wail — the day of Yahweh is almost here!\nIt comes as destruction straight from the Almighty —\nShaddai himself, the name echoed in the ruin he sends."
    },
    "7": {
      "L": "Therefore all hands will fall limp and every man's heart will melt.",
      "M": "At this every hand will go limp and every human heart will melt with fear.",
      "T": "At that — every hand goes slack,\nevery human heart dissolves."
    },
    "8": {
      "L": "And they will be in anguish; pangs and sorrows will take hold of them; like a woman in labour they will writhe; they will look in amazement each at his neighbour; their faces will be as flames.",
      "M": "They will be seized with anguish; pangs and agony will grip them; they will writhe like a woman in labour. They will look at one another in horror, their faces burning red.",
      "T": "Anguish seizes them — the pangs of a woman in hard labour.\nThey look at one another in disbelief;\ntheir faces blaze with terror."
    },
    "9": {
      "L": "Behold, the day of the LORD comes, cruel with wrath and fierce anger, to make the land a desolation and to destroy its sinners from it.",
      "M": "See, the day of the LORD is coming — relentless in wrath and burning anger — to turn the land into a ruin and wipe out every sinner from it.",
      "T": "Here it comes — the day of Yahweh:\ncruel, full of wrath, blazing with fierce anger.\nThe land will be made desolate;\nevery sinner will be swept from its face."
    },
    "10": {
      "L": "For the stars of heaven and their constellations will not flash forth their light; the sun will be dark at its rising, and the moon will not cause its light to shine.",
      "M": "The stars of heaven and their constellations will not give their light; the sun will be dark when it rises and the moon will not shed its glow.",
      "T": "The stars of heaven go dark — constellations and all.\nThe sun rises in darkness;\nthe moon withholds its light."
    },
    "11": {
      "L": "And I will punish the world for its evil and the wicked for their iniquity; I will put an end to the arrogance of the proud and lay low the haughtiness of the ruthless.",
      "M": "I will punish the world for its evil and the wicked for their guilt; I will put an end to the arrogance of the proud and cut down the insolence of tyrants.",
      "T": "I will visit the world for its evil\nand the wicked for the full measure of their guilt.\nThe pride of the arrogant — I will end it.\nThe swagger of the violent — I will bring it to the ground."
    },
    "12": {
      "L": "I will make a man more rare than pure gold, even mankind more than the gold of Ophir.",
      "M": "Human life will become rarer than pure gold — rarer even than the gold of Ophir.",
      "T": "Survivors will be rarer than pure gold —\nrarer than Ophir's finest ore;\nwhat was common will become priceless."
    },
    "13": {
      "L": "Therefore I will make the heavens tremble, and the earth will be shaken out of its place, at the wrath of the LORD of hosts and in the day of his fierce anger.",
      "M": "I will make the heavens tremble, and the earth will be displaced from its foundations by the wrath of the LORD of hosts on the day of his burning anger.",
      "T": "I will shake the heavens;\nthe earth will lurch from its place —\nthis is what the wrath of Yahweh of hosts looks like\non the day his anger burns to its height."
    },
    "14": {
      "L": "And like a chased gazelle or like sheep with none to gather them, each man will turn to his own people and each will flee to his own land.",
      "M": "Like a hunted gazelle or like sheep scattered with no one to round them up, each person will flee back to his own people, each run to his own homeland.",
      "T": "They will bolt like a hunted gazelle,\nscatter like sheep with no one to herd them —\nevery man rushing back to his own people,\nevery one fleeing to his own land."
    },
    "15": {
      "L": "Every one who is found will be thrust through, and every one who is captured will fall by the sword.",
      "M": "Anyone who is caught will be run through with a sword; anyone taken prisoner will fall by the blade.",
      "T": "Every one they catch — stabbed through.\nEvery one they take — cut down by the sword."
    },
    "16": {
      "L": "Their children will be dashed to pieces before their eyes; their houses will be plundered and their wives violated.",
      "M": "Their children will be dashed to pieces in front of them; their homes will be looted and their wives raped.",
      "T": "Their children will be smashed to death before their eyes;\ntheir homes stripped bare;\ntheir wives taken by force."
    },
    "17": {
      "L": "Behold, I am stirring up the Medes against them, who have no regard for silver and do not delight in gold.",
      "M": "I am rousing the Medes against Babylon — a people who care nothing for silver and feel no pull toward gold.",
      "T": "See how I am stirring up the Medes against them —\na people whose ambition runs deeper than silver,\nwho feel no pull toward gold."
    },
    "18": {
      "L": "And their bows will cut down the young men; they will have no pity on the fruit of the womb; their eye will not spare children.",
      "M": "Their bows will cut the young men down; they will show no mercy on newborn infants; they will have no pity for children.",
      "T": "Their arrows will mow down the young men;\nno mercy on the newborn,\nno pity in their eyes for children."
    },
    "19": {
      "L": "And Babylon, the glory of kingdoms, the beauty and pride of the Chaldeans, will be like Sodom and Gomorrah when God overthrew them.",
      "M": "Babylon — the glory of kingdoms, the pride and beauty of the Chaldeans — will be like Sodom and Gomorrah when God overturned them.",
      "T": "Babylon — crown of kingdoms, jewel of Chaldean splendour —\nwill become like Sodom and Gomorrah\nthe day God turned them upside down."
    },
    "20": {
      "L": "It will never be inhabited, and it will not be dwelt in from generation to generation; neither will the Arab pitch tent there, nor will shepherds make their flocks lie down there.",
      "M": "It will never be lived in or settled again through all generations; no Bedouin will pitch a tent there, no shepherds will let their flocks rest there.",
      "T": "Never again will it be inhabited —\nnot for a single generation will anyone settle there.\nNo desert nomad will pitch a tent on that ground;\nno shepherd will bed down his flock within its ruins."
    },
    "21": {
      "L": "But wild beasts of the desert will lie there, and their houses will be full of mournful creatures; ostriches will dwell there and wild goats will dance there.",
      "M": "Desert creatures will take up residence there; their empty houses will be full of owls; ostriches will make their home there and wild goats will frolic there.",
      "T": "Desert jackals will laze in the ruins;\nthe empty palaces will echo with screech owls.\nOstriches will nest there;\nwild goats will leap among the fallen stones."
    },
    "22": {
      "L": "Wild beasts will howl in its towers and jackals in the luxurious palaces; its time is near to come and its days will not be prolonged.",
      "M": "Hyenas will cry out in her citadels and jackals in her splendid palaces. Her time is about to come; her days will not be drawn out.",
      "T": "Wolves will howl from the towers;\njackals will fill the pleasure palaces with their cries.\nHer end is almost here — her days will not stretch out."
    }
  },
  "14": {
    "1": {
      "L": "For the LORD will have compassion on Jacob and will again choose Israel, and will settle them in their own land; sojourners will join them and attach themselves to the house of Jacob.",
      "M": "For the LORD will show compassion to Jacob and once again choose Israel, and will settle them in their own land. Foreigners will join them and attach themselves to the house of Jacob.",
      "T": "For Yahweh will have compassion on Jacob;\nhe will choose Israel again and settle them in their own land.\nStrangers will attach themselves to them,\ncleaving to the house of Jacob."
    },
    "2": {
      "L": "And the peoples will take them and bring them to their place; and the house of Israel will possess them in the land of the LORD as male and female servants; and they will be their captors who had been their captors, and they will rule over their oppressors.",
      "M": "Peoples will escort them back to their homeland; the house of Israel will possess them as servants in the LORD's land. They will take captive those who once held them captive and rule over those who once oppressed them.",
      "T": "Nations will bring them back and set them in their own place;\nthe house of Israel will inherit them as servants in Yahweh's land —\nthey who were once slaves will master their former masters,\nruling over those who drove them."
    },
    "3": {
      "L": "And it shall come to pass on the day that the LORD gives you rest from your sorrow and turmoil and from the hard bondage in which you were made to serve,",
      "M": "On the day when the LORD gives you rest from your pain and suffering and from the cruel servitude you were forced to endure,",
      "T": "When that day comes — when Yahweh gives you rest at last\nfrom the grief and terror and grinding forced labour —"
    },
    "4": {
      "L": "you will take up this taunt against the king of Babylon and say: 'How the oppressor has ceased, the exacting one has ceased!'",
      "M": "you will take up this song of mockery against the king of Babylon: 'How the tyrant has come to his end! How his insolent fury is over!'",
      "T": "— then you will lift this taunt against the king of Babylon and sing:\n'How the oppressor has met his end!\nThe golden city's fury — all of it, gone!'"
    },
    "5": {
      "L": "The LORD has broken the staff of the wicked, the sceptre of rulers,",
      "M": "The LORD has shattered the rod of the wicked, the sceptre of rulers,",
      "T": "Yahweh has snapped the rod of the wicked,\nthe sceptre that bruised the nations —"
    },
    "6": {
      "L": "that struck down peoples in wrath with unceasing blows, that ruled the nations in anger with unrelenting pursuit.",
      "M": "the rod that beat down peoples in furious, relentless blows, that kept nations under the heel of tyranny without relief.",
      "T": "the one that thrashed peoples in its rage without ceasing,\nthat ground nations under its heel with no mercy and no end."
    },
    "7": {
      "L": "The whole earth is at rest and quiet; they break forth into singing.",
      "M": "The whole earth rests quietly in peace; they burst into song.",
      "T": "The whole earth exhales —\nstill at last, at rest —\nand breaks out singing."
    },
    "8": {
      "L": "Even the cypress trees rejoice over you, and the cedars of Lebanon, saying: 'Since you lay down, no woodcutter comes against us.'",
      "M": "The very cypress trees rejoice over you, as do the cedars of Lebanon: 'Since you have been brought low, no axeman has risen against us.'",
      "T": "Even the cypress trees exult over you,\nand the great cedars of Lebanon cry out:\n'Since the day you were cut down,\nnot one woodcutter has come up against us!'"
    },
    "9": {
      "L": "Sheol beneath is stirred up to meet you when you come; it rouses the shades for you, all the rulers of the earth; it raises from their thrones all the kings of the nations.",
      "M": "Sheol below stirs itself to meet you at your arrival; it rouses the spirits of the dead — all who were rulers of the earth; it lifts every king of the nations from their thrones.",
      "T": "Sheol below seethes with excitement at your arrival —\nrousing the shades of the dead to greet you,\nall who were once kings and chiefs of the earth,\nlifted from their thrones for the occasion."
    },
    "10": {
      "L": "All of them will respond and say to you: 'You too have become weak as we! You have become like us!'",
      "M": "They will all speak up and say to you: 'You too have been brought to nothing, just as we were — you are exactly like us!'",
      "T": "And every one of them speaks:\n'So — you have joined us at last!\nYou who were so great — you have become like us.\nWeak. Just like us.'"
    },
    "11": {
      "L": "Your pomp is brought down to Sheol, the noise of your harps; under you is spread a bed of worms, and worms cover you.",
      "M": "Your magnificence has been dragged down to Sheol — the music of your harps along with it. Maggots are spread beneath you as your mattress, and worms are your blanket.",
      "T": "All that pomp — dragged down to Sheol.\nThe noise of your harps — silenced in the pit.\nMaggots are your mattress;\nworms are your blanket."
    },
    "12": {
      "L": "How you have fallen from heaven, O shining one, son of the dawn! How you are cut down to the ground, you who laid nations low!",
      "M": "How you have fallen from heaven, O Day Star, son of the Dawn! You have been hurled to the ground — you who laid nations prostrate!",
      "T": "How you have plummeted from heaven —\nO Day Star, brilliant son of the dawn!\nHurled to earth, flat on the ground —\nyou who once forced nations to their knees!"
    },
    "13": {
      "L": "For you said in your heart: 'I will ascend to heaven; above the stars of God I will exalt my throne; I will sit on the mount of assembly in the far reaches of the north;'",
      "M": "For you said in your heart: 'I will climb up to heaven; I will set my throne higher than the stars of God; I will sit enthroned on the mount of assembly, in the far north;'",
      "T": "In your heart you made these boasts:\n'I will storm the heavens;\nI will set my throne above the very stars of God;\nI will sit on the mount of the divine assembly,\nenthroned at the northern heights of the cosmos —'"
    },
    "14": {
      "L": "'I will ascend above the heights of the clouds; I will make myself like the Most High.'",
      "M": "'I will rise above the topmost layers of cloud; I will become like the Most High.'",
      "T": "'I will climb above the topmost clouds;\nI will be like El Elyon — the Most High himself.'"
    },
    "15": {
      "L": "But you are brought down to Sheol, to the far reaches of the pit.",
      "M": "But you have been brought down to Sheol, to the deepest depths of the pit.",
      "T": "Instead — you are thrown down to Sheol,\ndown to the lowest reaches of the pit."
    },
    "16": {
      "L": "Those who see you will gaze at you and reflect on you: 'Is this the man who made the earth tremble, who shook kingdoms,'",
      "M": "Those who see you will scrutinise you and consider: 'Is this really the man who made the earth shake, who rattled kingdoms,'",
      "T": "Those who see you will stare long and hard,\nthen say with disbelief:\n'Is this the man — this wretched thing —\nwho made the whole earth tremble,\nwho shook the thrones of kingdoms?'"
    },
    "17": {
      "L": "who made the world like a desert and overthrew its cities, who would not release his prisoners to go home?",
      "M": "who turned the whole world into a wasteland and demolished its cities, who never released his prisoners to go home?",
      "T": "'The one who turned the world into a wasteland,\nwho smashed city after city to rubble,\nwho never opened the prison door for a single captive?'"
    },
    "18": {
      "L": "All the kings of the nations lie in honour, each in his own tomb;",
      "M": "All the kings of the nations lie in state, each in his own burial place;",
      "T": "Every other king lies in dignity —\neach one buried with honour in his own tomb."
    },
    "19": {
      "L": "but you are cast out from your tomb like an abhorred branch, clothed in the slain who are pierced by the sword, who go down to the stones of the pit, like a trampled corpse.",
      "M": "but you are thrown out of your grave like a rejected branch — surrounded by the bodies of those cut down by the sword, who sink to the rocky pit like a carcass trampled underfoot.",
      "T": "But you — thrown out, away from your tomb,\nlike a revolting twig nobody wants,\nwrapped in the bodies of those run through by the sword,\nspilling down to the stony pit like a carcass crushed underfoot."
    },
    "20": {
      "L": "You will not be joined with them in burial, because you have ruined your land and slaughtered your people; the offspring of evildoers will never be named again.",
      "M": "You will never be buried with them, because you destroyed your own country and murdered your own people. The seed of evildoers will never again be mentioned.",
      "T": "No grave for you beside the other kings —\nyou who devastated your own land,\nyou who slaughtered your own people.\nThe line of evildoers will be blotted from every record."
    },
    "21": {
      "L": "Prepare slaughter for his sons because of the iniquity of their fathers; they are not to rise and take possession of the earth and fill the face of the world with cities.",
      "M": "Ready the execution ground for his sons on account of their fathers' guilt — so that they never rise to possess the land and overrun the face of the earth with cities.",
      "T": "Make ready the execution ground for his sons —\nthe guilt of the fathers falls on them —\nlest they rise and reclaim the earth,\ncovering the whole world's face with rebuilt cities."
    },
    "22": {
      "L": "'I will rise up against them,' declares the LORD of hosts, 'and I will cut off from Babylon name and remnant, offspring and posterity,' declares the LORD.",
      "M": "'I will rise up against them,' declares the LORD of hosts. 'I will cut off from Babylon its name and its survivors, its offspring and descendants,' declares the LORD.",
      "T": "'I myself will rise against them,' declares Yahweh of hosts.\n'I will erase from Babylon every name, every remnant,\nevery child and grandchild,' declares Yahweh."
    },
    "23": {
      "L": "'I will make it a possession for the porcupine and pools of water, and I will sweep it with the broom of destruction,' declares the LORD of hosts.",
      "M": "'I will make it a haunt for the hedgehog and turn it to stagnant marshes, and I will sweep what remains with the broom of annihilation,' declares the LORD of hosts.",
      "T": "'I will hand it over to the hedgehog and fill it with standing pools —\nthen sweep what remains away with the broom of destruction,' declares Yahweh of hosts."
    },
    "24": {
      "L": "The LORD of hosts has sworn: 'Surely, as I have planned, so shall it be; and as I have purposed, so shall it stand:'",
      "M": "The LORD of hosts has taken an oath: 'Exactly as I have planned, so it will happen; exactly as I have purposed, so it will stand:'",
      "T": "Yahweh of hosts has sworn with an oath:\n'Whatever I have planned — it will happen.\nWhatever I have purposed — it will stand.'"
    },
    "25": {
      "L": "'that I will break the Assyrian in my land, and upon my mountains I will trample him; and his yoke will be removed from them and his burden removed from their shoulders.'",
      "M": "'I will crush the Assyrian in my own land; I will trample him on my mountains. His yoke will be lifted from my people and his burden taken from their shoulders.'",
      "T": "'I will break Assyria in my own land —\ntrample him on my own mountains.\nThen his yoke will be lifted from my people's necks\nand his crushing load from their shoulders.'"
    },
    "26": {
      "L": "This is the purpose that is purposed concerning all the earth, and this is the hand that is stretched out over all the nations.",
      "M": "This is the plan purposed for the whole earth, and this is the hand stretched out over all the nations.",
      "T": "This is the plan laid out for the whole earth;\nthis is the hand stretched out over every nation."
    },
    "27": {
      "L": "For the LORD of hosts has purposed, and who shall annul it? And his hand is stretched out, and who shall turn it back?",
      "M": "For the LORD of hosts has made this purpose, and who can overturn it? His hand is extended, and who can force it back?",
      "T": "Yahweh of hosts has decided — who will cancel it?\nHis hand is outstretched — who will force it back?"
    },
    "28": {
      "L": "In the year that King Ahaz died, this burden came:",
      "M": "In the year when King Ahaz died, this oracle came:",
      "T": "In the year of King Ahaz's death, this word arrived:"
    },
    "29": {
      "L": "Do not rejoice, all of Philistia, that the rod that struck you is broken; for from the root of the serpent will come forth an adder, and its fruit will be a flying fiery serpent.",
      "M": "Do not rejoice, O Philistia — none of you — because the rod that beat you down is broken. For from the serpent's root a viper will grow, and its fruit will be a darting, venomous serpent.",
      "T": "Do not celebrate, O Philistia — every part of you —\nbecause the rod that struck you has been broken.\nFor from that serpent's root another serpent will rise,\nand its offspring — a winged, venomous terror."
    },
    "30": {
      "L": "The firstborn of the poor will feed and the needy will lie down in safety; but I will kill your root with famine and your remnant will die.",
      "M": "The poorest of the poor will have pasture and the needy will rest in safety; but I will put your root to death with famine and your survivors will perish.",
      "T": "The most destitute of the poor will graze in safety;\nthe needy will lie down without fear.\nBut your root — I will kill it with famine,\nand every last survivor will be cut down."
    },
    "31": {
      "L": "Howl, O gate; cry out, O city; melt with fear, O Philistia! For from the north a smoke comes, and there is no straggler in his ranks.",
      "M": "Wail, O gate! Cry out, O city! Dissolve with terror, all of Philistia! For a column of smoke rises from the north and there is not one straggler in that advancing army.",
      "T": "Wail at the gates! Cry out from the walls!\nPhilistia — every part of you — melt in terror!\nFor from the north a column of smoke rises —\nand in that advancing army, not a single straggler."
    },
    "32": {
      "L": "And what will one answer the messengers of the nations? That the LORD has founded Zion, and in her the afflicted of his people will take refuge.",
      "M": "What answer will be given to the envoys of the nations? This: 'The LORD has established Zion, and in her the poor of his people will find their shelter.'",
      "T": "What will you say when the envoys of the nations demand an answer?\nThis: Yahweh has laid Zion's foundations —\nand in her the weakest of his people have their sure refuge."
    }
  },
  "15": {
    "1": {
      "L": "The burden of Moab: because Ar of Moab is laid waste in a night, Moab is undone; because Kir of Moab is laid waste in a night, Moab is undone.",
      "M": "The oracle concerning Moab: Because Ar of Moab is destroyed in a single night, Moab is ruined; because Kir of Moab is destroyed in a night, Moab is ruined.",
      "T": "The oracle against Moab:\nBecause Ar of Moab is laid waste in a single night — Moab is undone.\nBecause Kir of Moab is laid waste in a single night — Moab is undone."
    },
    "2": {
      "L": "Moab has gone up to the temple and to Dibon, to the high places to weep; over Nebo and over Medeba Moab wails; on every head is baldness and every beard is shorn.",
      "M": "The people go up to the temple and to Dibon, to the hilltop shrines to weep; they wail over Nebo and over Medeba — every head shaved bald and every beard cut off.",
      "T": "They go up to the temple and to Dibon,\nclimbing to the high places to weep.\nOver Nebo and over Medeba — wailing.\nEvery head shaved bald, every beard cut in mourning."
    },
    "3": {
      "L": "In their streets they gird themselves with sackcloth; on their rooftops and in their squares everyone wails and falls down weeping.",
      "M": "In the streets they wear sackcloth; on the rooftops and in the public squares everyone mourns and weeps uncontrollably.",
      "T": "In every street sackcloth is all they wear;\non every rooftop, in every open square —\nweeping, wailing, tears running free."
    },
    "4": {
      "L": "Heshbon and Elealeh cry out; their voice is heard even to Jahaz; therefore the armed men of Moab shout aloud; his soul trembles within him.",
      "M": "Heshbon and Elealeh raise their cry — it can be heard all the way to Jahaz. At this even Moab's soldiers cry out; each one shudders within.",
      "T": "The shout from Heshbon and Elealeh carries all the way to Jahaz;\nat the sound even Moab's own soldiers cry out —\nevery soul within them trembling."
    },
    "5": {
      "L": "My heart cries out for Moab; her fugitives flee to Zoar, to Eglath-shelishiyah. For at the ascent of Luhith they go up weeping; on the road to Horonaim they raise up a cry of destruction.",
      "M": "My heart cries out for Moab. Her fugitives flee to Zoar, to Eglath-shelishiyah. At the climb up Luhith they go up in tears; on the Horonaim road they raise a desperate cry of ruin.",
      "T": "My heart aches for Moab —\nhis refugees fleeing to Zoar, to Eglath-shelishiyah.\nUp the slope of Luhith they trudge, weeping at every step;\non the Horonaim road the shout of ruin rises up."
    },
    "6": {
      "L": "For the waters of Nimrim are a desolation; for the grass has dried up, the tender grass has failed, there is nothing green.",
      "M": "For the pools of Nimrim have dried up; the grass is withered, the new growth is gone, there is nothing green left.",
      "T": "The waters of Nimrim have gone dry —\nthe grass scorched, the young shoots dead,\nnot a trace of green remaining."
    },
    "7": {
      "L": "Therefore what they have gained and what they have laid up they carry away over the brook of the willows.",
      "M": "So whatever they have accumulated and saved they carry away across the Brook of the Willows.",
      "T": "Whatever they have stored and laid by —\nthey carry it all across the Brook of the Willows into exile."
    },
    "8": {
      "L": "For the cry has gone around the whole border of Moab; the wailing reaches to Eglaim and the wailing reaches to Beer-elim.",
      "M": "The sound of weeping has encircled the whole border of Moab — the wailing reaches Eglaim, the wailing reaches Beer-elim.",
      "T": "The wailing has encircled every border of Moab —\nit rings out as far as Eglaim,\nit carries all the way to Beer-elim."
    },
    "9": {
      "L": "For the waters of Dimon are full of blood; for I will bring upon Dimon yet more — a lion for the fugitives of Moab and for the remnant of the land.",
      "M": "For the waters of Dimon run red with blood; and I will bring more upon Dimon — a lion against the fugitives of Moab and against what remains of the land.",
      "T": "The waters of Dimon are already full of blood —\nbut I will bring more upon Dimon yet:\na lion waiting for those who flee from Moab,\na lion for every survivor left in the land."
    }
  },
  "16": {
    "1": {
      "L": "Send the tribute lamb to the ruler of the land, from Sela by way of the desert, to the mount of the daughter of Zion.",
      "M": "Send the tribute lamb to the ruler of the land, dispatched from Sela across the desert to the mount of Daughter Zion.",
      "T": "Send the tribute lamb to the ruler of the land —\nfrom Sela, across the desert road,\nto the mount of Daughter Zion."
    },
    "2": {
      "L": "And it shall be as a wandering bird, as scattered nestlings, so the daughters of Moab shall be at the fords of the Arnon.",
      "M": "The women of Moab will be like a fluttering bird, like scattered nestlings, stranded at the fords of the Arnon.",
      "T": "Like a bird flushed from its nest —\nlike young ones scattered with nowhere to land —\nthat is what Moab's daughters are like at the fords of the Arnon."
    },
    "3": {
      "L": "'Bring counsel, execute justice; make your shadow as the night in the midst of noon; shelter the outcasts; do not betray the fugitive;'",
      "M": "'Offer counsel, dispense justice; make your shade as dark as midnight at midday; shelter the refugees; do not betray the one who is fleeing;'",
      "T": "'Give us your counsel — act justly!\nLet your shadow fall like midnight at noon;\nhide the scattered outcasts;\ndo not give away the fugitive —'"
    },
    "4": {
      "L": "'Let my outcasts dwell with you, Moab; be a shelter to them from the face of the destroyer. For the oppressor is no more, destruction has ceased, the trampler has vanished from the land.'",
      "M": "'Let my displaced people take shelter with you; be a refuge for them from the ravager. For the tyrant is gone, destruction is over, and the one who trampled is out of the land.'",
      "T": "'Let my scattered people settle with you —\nbe their cover against the destroyer.\nFor the tyrant is finished;\nthe devastation is done;\nthe one who ground people underfoot is gone from the land.'"
    },
    "5": {
      "L": "Then a throne will be established in steadfast love, and on it will sit in faithfulness in the tent of David one who judges and seeks justice and is swift to do righteousness.",
      "M": "Then a throne will be set up in covenant faithfulness; one will sit on it in truth in the tent of David — one who judges and actively pursues justice and is swift to act with righteousness.",
      "T": "Then a throne will be established in hesed — in covenant faithfulness —\nand on it, in the tent of David, one will sit in truth:\njudging, pursuing justice,\nswift to do what is right."
    },
    "6": {
      "L": "We have heard of the pride of Moab, how exceedingly proud he is, of his arrogance, his pride, and his wrath; his boastings are empty.",
      "M": "We have heard of Moab's arrogance — his immense pride, his haughtiness and conceit and fury — his empty boasting amounts to nothing.",
      "T": "Everyone has heard of Moab's pride — how utterly puffed up he is,\nhis arrogance, his insolence, his seething fury.\nAll his boasting is hollow air."
    },
    "7": {
      "L": "Therefore Moab shall wail for Moab, everyone shall wail; for the raisin cakes of Kir-hareseth you shall mourn, surely stricken.",
      "M": "So let Moab wail over Moab — let everyone wail; mourn, utterly stricken, over the loss of Kir-hareseth.",
      "T": "So let Moab mourn for Moab — all of it, mourning.\nCry for the delicacies of Kir-hareseth;\ngroan with real grief."
    },
    "8": {
      "L": "For the terraces of Heshbon have languished; the vine of Sibmah whose branches once spread over the lords of the nations reached to Jazer and wandered into the desert; its shoots spread out and passed over the sea.",
      "M": "For the terraces of Heshbon have withered; the vine of Sibmah — whose branches once stretched as far as Jazer, wandered through the desert, and reached to the sea — its finest vines have been struck down by the rulers of the nations.",
      "T": "The terraces of Heshbon languish;\nthe vine of Sibmah — whose branches once arched\nall the way to Jazer and out across the desert,\nreaching even to the sea —\nits rulers have been struck down, its vines laid waste."
    },
    "9": {
      "L": "Therefore I will weep with the weeping of Jazer for the vine of Sibmah; I will drench you with my tears, O Heshbon and Elealeh; for over your summer fruit and your harvest the battle cry has fallen.",
      "M": "I weep for the vine of Sibmah with the tears of Jazer; I drench you with my own grief, O Heshbon and Elealeh — because the war cry has crashed down over your summer harvest and ripe grapes.",
      "T": "So I weep for Sibmah's vine with Jazer's own tears;\nI drench you with my grief, O Heshbon, O Elealeh —\nfor the battle shout has crashed down\nupon your summer fruit and your gathered harvest."
    },
    "10": {
      "L": "And gladness and joy are taken away from the garden land; in the vineyards no singing is heard, no shouts of joy; no treader treads out wine in the presses; I have put an end to the vintage shout.",
      "M": "Gladness and joy have been stripped from the orchards; in the vineyards no one sings, no one shouts for joy; no one treads grapes in the winepresses. I have silenced the harvest songs.",
      "T": "Joy and gladness are stripped from the fertile fields.\nIn the vineyards — no song, no harvest shout.\nNo one treads the winepress;\nI have silenced the shout of the vintage."
    },
    "11": {
      "L": "Therefore my heart mourns like a lyre for Moab, and my inmost being for Kir-hareseth.",
      "M": "My heart resonates like a lyre in mourning for Moab; my deepest self aches for Kir-hareseth.",
      "T": "My heart vibrates like a harp in grief for Moab;\nmy innermost being mourns for Kir-hareseth."
    },
    "12": {
      "L": "And when Moab appears and wearies himself on the high place, and comes to his sanctuary to pray, he will not prevail.",
      "M": "When Moab shows himself at the high place, wears himself out in prayer, and comes to his sanctuary to plead, he will not succeed.",
      "T": "When Moab drags himself to the high place,\ntiring himself out with prayer at the sanctuary —\nhe will get nothing. He cannot prevail."
    },
    "13": {
      "L": "This is the word that the LORD spoke concerning Moab in time past.",
      "M": "This is the word the LORD pronounced concerning Moab in the past.",
      "T": "This was the word Yahweh spoke concerning Moab long before."
    },
    "14": {
      "L": "But now the LORD speaks, saying: 'Within three years, as the years of a hired worker, the glory of Moab will be dishonoured with all his great multitude; and the remnant will be very small and feeble.'",
      "M": "But now the LORD declares: 'Within three years — no more than the term of a hired labourer — Moab's glory will be brought into contempt, for all its vast numbers; what is left will be very small and of no account.'",
      "T": "But now Yahweh speaks with new precision:\n'In three years — counted as precisely as a hired worker counts his contract —\nMoab's glory will be despised, for all its great multitude.\nThe remnant will be pathetically small, weak, and of no account.'"
    }
  },
  "17": {
    "1": {
      "L": "The burden of Damascus: Behold, Damascus is removed from being a city, and it will become a heap of ruins.",
      "M": "The oracle concerning Damascus: Behold, Damascus is about to cease being a city; it will become a pile of rubble.",
      "T": "The oracle against Damascus:\nDamascus will be stripped of its city-status —\nreduced to a heap of rubble."
    },
    "2": {
      "L": "The cities of Aroer are forsaken; they will be for flocks, which will lie down, and none will make them afraid.",
      "M": "The towns of Aroer are abandoned — left for flocks to graze, and they will lie down there with no one to disturb them.",
      "T": "The towns of Aroer will stand empty —\nwild flocks will bed down there\nand nothing will frighten them away."
    },
    "3": {
      "L": "The fortress also will cease from Ephraim, and the kingdom from Damascus; and the remnant of Syria will be as the glory of the children of Israel, declares the LORD of hosts.",
      "M": "The fortified city will disappear from Ephraim and the royal power from Damascus; and what remains of Syria will share the same fate as the diminished glory of the Israelites, declares the LORD of hosts.",
      "T": "The fortresses of Ephraim will be gone;\nDamascus will lose its sovereignty —\nand what is left of Syria will be as diminished\nas the fading glory of Israel herself,\ndeclares Yahweh of hosts."
    },
    "4": {
      "L": "And in that day the glory of Jacob will be brought low, and the fatness of his flesh will become lean.",
      "M": "In that day the splendour of Jacob will fade and his well-nourished frame will waste away.",
      "T": "In that day Jacob's glory will dim\nand the richness of his flesh will waste to bone."
    },
    "5": {
      "L": "And it shall be as when the reaper gathers the standing grain and harvests the ears with his arm; yes, it shall be as when one gleans ears of grain in the Valley of Rephaim.",
      "M": "It will be like a reaper sweeping in the grain, gathering up the ears with his arm — like someone gleaning what is left in the Valley of Rephaim.",
      "T": "Think of a reaper sweeping the standing grain,\nhis arm gathering the ears —\nlike a gleaner working the last rows\nafter the harvest in the Valley of Rephaim."
    },
    "6": {
      "L": "Yet some gleanings will be left in it, as when an olive tree is beaten: two or three berries on the topmost bough, four or five on the branches of the fruitful tree, declares the LORD God of Israel.",
      "M": "Only gleanings will remain, as when an olive tree is beaten — two or three olives at the very top of the highest branch, four or five on the outlying boughs — declares the LORD, the God of Israel.",
      "T": "A few gleanings will remain —\nlike the last olives after the beating:\ntwo or three at the tip of the topmost branch,\nfour or five on the outer limbs —\ndeclares Yahweh, the God of Israel."
    },
    "7": {
      "L": "In that day man will look to his Maker, and his eyes will look to the Holy One of Israel.",
      "M": "In that day people will look to their Creator, and their eyes will be fixed on the Holy One of Israel.",
      "T": "In that day — stripped of everything —\npeople will turn their gaze to the One who made them;\ntheir eyes will find the Holy One of Israel."
    },
    "8": {
      "L": "He will not look to the altars, the work of his hands; and he will not regard what his own fingers have made, neither the Asherim nor the incense altars.",
      "M": "He will have no regard for the altars he made, or for the Asherim poles or incense altars that his own hands fashioned.",
      "T": "He will not go back to the altars his own hands built;\nhe will not look to what his fingers made —\nno more Asherim, no more incense shrines."
    },
    "9": {
      "L": "In that day their strong cities will be like the forsaken places of the forest and the hilltop, which were forsaken before the children of Israel; and it will be a desolation.",
      "M": "In that day their fortified cities will be like abandoned woodland shrines and deserted hilltops that were left vacant before the Israelites — utter desolation.",
      "T": "In that day their fortress cities will be like the abandoned high places in the forest —\ndeserted as those hilltops the Israelites once left behind —\nnothing but desolation."
    },
    "10": {
      "L": "For you have forgotten the God of your salvation and have not remembered the Rock of your refuge; therefore you plant pleasant plants and set out foreign slips.",
      "M": "For you have forgotten the God who saves you and have not remembered the Rock who shelters you; so you plant ornamental gardens and set in shoots from foreign vines,",
      "T": "Because you have forgotten the God of your salvation —\nyou have not remembered the Rock, your fortress —\nso now you plant decorative gardens\nand set in cuttings from pagan vines,"
    },
    "11": {
      "L": "In the day you plant it you make it grow, and in the morning you make your seed blossom; but the harvest flees away in the day of grief and incurable pain.",
      "M": "though you force them to sprout the very day you plant them and blossom the morning you sow — yet come the day of grief and desperate pain the harvest will be gone.",
      "T": "You can make them shoot up the morning after planting;\nyou can force them into blossom by dawn —\nbut on the day of grief, on the day of pain that cannot be healed,\nthe harvest will vanish."
    },
    "12": {
      "L": "Woe! The noise of many peoples, who roar like the roaring of the seas; and the rushing of nations, who rush like the rushing of mighty waters!",
      "M": "Woe — the uproar of many peoples! They roar like the roaring of the seas! And the crashing of nations — they crash like the surge of mighty waters!",
      "T": "Woe to the thunder of many peoples —\nthey roar like the crashing of the seas!\nWoe to the surge of nations —\nthey rush and boom like the torrents of mighty waters!"
    },
    "13": {
      "L": "The nations roar like the roaring of many waters; but he will rebuke them and they will flee far away, chased like chaff on the mountains before the wind and like whirling dust before the storm.",
      "M": "The nations surge like surging water — but he rebukes them and they scatter far away, driven like chaff off the mountains before the wind, like a dust cloud spinning away before the gale.",
      "T": "They surge — but he rebukes them,\nand they flee to the far distance:\nchased like chaff blown off a mountain in the wind,\nlike a column of dust that a storm whips away to nothing."
    },
    "14": {
      "L": "At the time of evening — behold, terror; and before morning it is no more. This is the portion of those who plunder us and the lot of those who prey upon us.",
      "M": "Evening comes — sudden terror. Before morning, there is nothing left. This is the destiny of those who loot us, the fate reserved for those who plunder us.",
      "T": "Evening falls — terror.\nBefore dawn — nothing remains.\nThis is the share of those who pillage us;\nthis is the lot of those who plunder us."
    }
  },
  "18": {
    "1": {
      "L": "Woe to the land of the whirring of wings, which is beyond the rivers of Cush!",
      "M": "Woe to the land buzzing with wings beyond the rivers of Cush!",
      "T": "Woe to the land of whirring wings —\nthe land that lies beyond the rivers of Cush!"
    },
    "2": {
      "L": "That sends ambassadors by the sea, in vessels of papyrus on the waters, saying: 'Go, swift messengers, to a nation tall and smooth-skinned, to a people dreaded near and far — a nation mighty and conquering, whose land the rivers divide.'",
      "M": "It sends envoys by sea, in papyrus boats skimming the waters. Go, swift messengers, to a people tall and smooth-skinned, dreaded everywhere near and far — a mighty, dominating nation whose land is cut by rivers.",
      "T": "This land sends its messengers by sea —\npapyrus boats skimming the waterways —\n'Go, swift ones, to the tall and smooth-skinned people,\nthe nation feared everywhere near and far,\nmighty and aggressive, whose land the great rivers divide.'"
    },
    "3": {
      "L": "All you inhabitants of the world, all you who dwell on the earth, when a banner is lifted up on the mountains, look! And when a trumpet is blown, hear!",
      "M": "All inhabitants of the world and all who dwell on earth — when a signal is hoisted on the mountains, look! When a trumpet is sounded, listen!",
      "T": "All inhabitants of the world, all who dwell upon the earth —\nwhen the standard is raised on the mountains: look!\nWhen the trumpet sounds: listen!"
    },
    "4": {
      "L": "For thus the LORD said to me: 'I will quietly look from my dwelling place, like clear heat in the sunshine, like a cloud of dew in the heat of harvest.'",
      "M": "For this is what the LORD said to me: 'I will stay quiet in my dwelling place and watch — like shimmering heat in the bright sun, like a cloud of dew in the heat of harvest.'",
      "T": "For Yahweh told me this:\n'I will be still in my dwelling place — watching, without a word —\nlike the clear heat that glimmers in the sunshine,\nlike a cloud of dew forming in the heat of the harvest.'"
    },
    "5": {
      "L": "For before the harvest, when the blossom is finished and the flower becomes a ripening grape, he will cut off the shoots with pruning hooks, and the spreading branches he will remove and cut down.",
      "M": "For before the harvest, once the blossom is done and the flower turns into a maturing grape, he will trim off the shoots with pruning knives and strip away and cut down the spreading branches.",
      "T": "Then — before the harvest,\nwhen the flower has given way to a ripening grape —\nhe will take the pruning hook to the shoots;\nhe will lop off and clear away every spreading branch."
    },
    "6": {
      "L": "They shall all be left together to the birds of prey of the mountains and to the beasts of the earth; and the birds of prey will summer on them, and all the beasts of the earth will winter on them.",
      "M": "They will all be abandoned to the mountain birds of prey and to the wild animals; the birds will summer on the carcasses and the beasts will winter on them.",
      "T": "All of it left behind —\nfor the mountain birds of prey and for the beasts of the field.\nThe vultures will summer on the carrion;\nthe wild beasts will winter on it."
    },
    "7": {
      "L": "In that time a gift will be brought to the LORD of hosts from a people tall and smooth, from a people feared near and far — a mighty and conquering nation whose land the rivers divide — to the place of the name of the LORD of hosts, Mount Zion.",
      "M": "At that time a tribute offering will be brought to the LORD of hosts from the tall and smooth-skinned people — the nation feared everywhere, the mighty and dominating people whose land the great rivers divide — to Mount Zion, where the LORD of hosts has placed his name.",
      "T": "In that time, a gift will be brought to Yahweh of hosts:\nfrom the tall and smooth-skinned people,\nfrom the nation feared near and far —\nmighty and dominant, their land cut by great rivers —\nbrought to Mount Zion,\nthe place where the name of Yahweh of hosts dwells."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 13–18 written.')

if __name__ == '__main__':
    main()
