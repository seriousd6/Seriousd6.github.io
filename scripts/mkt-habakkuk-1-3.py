"""
MKT Habakkuk chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-habakkuk-1-3.py

=== BOOK OVERVIEW ===

Habakkuk is a dialogue/lament between the prophet and God — unique among the Twelve in
having no direct address to Israel, only to Yahweh himself. Structure:

  Ch 1:1–4   First complaint: Why does God permit injustice in Judah?
  Ch 1:5–11  God's first answer: the Chaldeans are coming.
  Ch 1:12–17 Second complaint: How can a holy God use wicked Babylon as his instrument?
  Ch 2:1     The prophet's watchpost — waiting for God's reply.
  Ch 2:2–4   God's second answer: write the vision; the righteous live by faithfulness.
  Ch 2:5–20  Five woes against the Chaldean oppressor.
  Ch 3:1–19  A theophanic prayer: God's past conquests remembered; closing confession of
             faith despite total agricultural desolation (vv.17–19).

The book moves from crisis-of-theodicy → divine answer → radical faith without resolution
of circumstances. Ch 3 is written as a formal psalm with Selah notations and a musical
postscript.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (standard small-caps convention).
  T: "Yahweh" in personal address, theophanic contexts, and the climactic doxology (3:18–19);
  "the LORD" in narrative clauses.
  Reason: T surfaces the covenant name where intimacy or climax demands it.

- H430 (אֱלֹהִים / Elohim):
  All three tiers: "God". In 1:11 (pagan usage) context makes the lowercase sense clear.
  In 3:3 "God" translates H433 (Eloah — singular form), which is the same rendering.
  In 3:19 H3069 (Adonai YHWH) rendered "Lord GOD" in L/M; "Yahweh, my Lord" in T.

- H6918 (קָדוֹשׁ / qadosh / Holy One):
  All three tiers: "Holy One" — the characteristic title in the Minor Prophets.

- H530 (אֱמוּנָה / emunah) in 2:4 — the single most theologically loaded word in the book:
  L: "faithfulness" — emunah denotes active, steadied reliability, not merely belief.
  M: "faithfulness" — the Greek πίστις in the NT quotations (Rom 1:17, Gal 3:11, Heb 10:38)
     covers both faith and faithfulness; the Hebrew weight is on character/practice.
  T: "steady faithfulness" — the T tier makes explicit what emunah requires: living by
     covenant fidelity, not simply holding a mental attitude.
  Note: the suffix "his" (בֶּאֱמוּנָתוֹ) is ambiguous — is it the righteous person's own
  faithfulness, or faithfulness directed toward God? Most Hebrew scholars read it as the
  person's own faithfulness/reliability. Documented here; future review may adjust.

- H2555 (חָמָס / chamas / violence):
  All three tiers: "violence" — the key word of ch. 1 and central to Habakkuk's complaint.
  It is the same word used of pre-flood violence in Gen 6:11. Do not soften.

- H4941 (מִשְׁפָּט / mishpat):
  L: "judgment" (lexical gloss).
  M: "justice" (natural English when the context is legal/social equity).
  T: context-driven — "justice", "verdict", or "ruling" depending on passage.

- H7307 (רוּחַ / ruach) in 1:11 and 2:19:
  1:11: "spirit" (L/M) — here it refers to the Chaldean's inner disposition/resolve
  sweeping forward; not the Holy Spirit, not physical wind. T: "inner drive/pride".
  2:19: "breath" (all tiers) — the idol has no breath/spirit in it; the contrast with
  the living LORD in 2:20 is intentional.

- H5315 (נֶפֶשׁ / nephesh):
  2:4 "soul" (L/M) — the puffed-up person's interior self.
  2:5 "appetite/desire" (L/M — nephesh as craving); T: "insatiable desire".
  2:10: "soul/self" — consistent with prior OT scripts.
  Carried forward from Micah scripts: nephesh = the embodied whole self, not a Greek soul.

- H2617 (חֶסֶד / chesed):
  Not explicit in Habakkuk text, but the concept is present in 3:2 ("mercy/compassion")
  via H7355 (racham) — rendered "mercy" L/M, "compassion" T.

- OT echoes noted:
  3:3 echoes the Sinai theophany (Deut 33:2; Judg 5:4-5; Ps 68:8).
  3:13 "your anointed" (mashiach) echoes Davidic covenant and is Messianic in later reading.
  3:17-19 is one of the most celebrated faith confessions in the entire Twelve.

- Textual notes:
  1:12b "we shall not die" — a scribal tradition (tiqqun sopherim) suggests the original
  read "you shall not die" (addressing God); the received text is "we shall not die".
  Both readings are theologically coherent; L/M preserve the received text.
  3:1 "Shigionoth" — a rare musical term, cognate with Ps 7 "Shiggaion"; likely indicates
  an impassioned or irregular meter. T renders interpretively.
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

HABAKKUK = {
  "1": {
    "1": {
      "L": "The burden which Habakkuk the prophet did see.",
      "M": "The oracle that Habakkuk the prophet received.",
      "T": "The vision-burden that Habakkuk the prophet received."
    },
    "2": {
      "L": "How long shall I cry to you, O LORD, and you will not hear? I cry out to you, 'Violence!' and you will not save.",
      "M": "How long, O LORD, must I call for help and you will not hear? I cry out to you 'Violence!' and you do not save.",
      "T": "How long, LORD? I shout to you and you stay silent. I cry out 'Violence!' — and you do not come to the rescue."
    },
    "3": {
      "L": "Why do you show me iniquity and cause me to look on trouble? Spoiling and violence are before me; strife arises and contention lifts up its head.",
      "M": "Why do you make me see injustice and stare at wickedness? Before me is destruction and violence; strife and conflict keep rising.",
      "T": "Why do you force me to watch wickedness and do nothing? Destruction and violence fill my sight; discord and quarreling surge everywhere — and you look on."
    },
    "4": {
      "L": "Therefore the law is slacked and justice never goes forth; for the wicked surround the righteous, and so perverted judgment proceeds.",
      "M": "Therefore the law is paralyzed and justice never prevails; the wicked have encircled the righteous, so justice comes out twisted.",
      "T": "The result: Torah is paralyzed. Justice never gets through — the wicked have hemmed in the righteous on every side, and every ruling that emerges is corrupt."
    },
    "5": {
      "L": "Look among the nations and behold; wonder and be astonished! For I am working a work in your days that you would not believe even if it were told.",
      "M": "Look out among the nations and pay attention; be utterly astonished! For I am doing something in your own days that you would not believe even if someone told you.",
      "T": "Turn and look at the nations — you will be stunned, staggering in disbelief. I am about to do something in your own lifetime so extraordinary that you would dismiss it as impossible if you heard it described beforehand."
    },
    "6": {
      "L": "For behold, I am raising up the Chaldeans, that bitter and swift nation, which marches through the breadth of the earth to possess dwellings that are not their own.",
      "M": "For look — I am raising up the Chaldeans, that fierce and impetuous nation, who sweep across the earth seizing territory that does not belong to them.",
      "T": "I am the one raising up the Chaldeans — that ruthless and reckless people who sweep across the whole face of the earth, seizing land no one gave them."
    },
    "7": {
      "L": "It is terrible and dreadful; its judgment and dignity proceed from itself.",
      "M": "They are fearsome and terrifying; they answer to no authority but their own.",
      "T": "They are a terror to behold. They recognize no law above themselves — they write their own code and enforce it by force alone."
    },
    "8": {
      "L": "Their horses are swifter than leopards and fiercer than evening wolves; their horsemen gallop forward; their horsemen come from afar; they fly like an eagle swooping to devour.",
      "M": "Their horses are faster than leopards and fiercer than wolves at dusk; their cavalry charges ahead, coming from far away; they swoop in like an eagle diving to feed.",
      "T": "Their warhorses outrun leopards; they are more savage than wolves hunting at dusk. Their cavalry rides in from the horizon and arrives like an eagle plummeting onto its prey."
    },
    "9": {
      "L": "All of them come for violence; the forward thrust of their faces is like the east wind, and they gather captives as the sand.",
      "M": "They all come for violence; their faces press forward like the east wind, and they scoop up captives like sand.",
      "T": "Everything about them is violence. Their faces push forward like a searing east wind, and they sweep up prisoners the way the sea sweeps up sand — endlessly, effortlessly."
    },
    "10": {
      "L": "At kings they scoff, and rulers are a laughingstock to them; they deride every fortress and heap up earth and take it.",
      "M": "They mock kings and scoff at rulers; they laugh at every fortress, pile up siege ramps against it, and take it.",
      "T": "Kings mean nothing to them — they sneer at royalty, ridicule every fortified city. They pile up earthworks, breach the walls, and move on."
    },
    "11": {
      "L": "Then his spirit sweeps on, and he passes through and offends — imputing this power to his god.",
      "M": "Then his spirit charges ahead; he sweeps through and transgresses, ascribing his might to his own god.",
      "T": "But pride is the crack in his armour. His inner drive surges forward, he sweeps on and conquers — and then he attributes all of it to his idol. That fatal attribution is the transgression that will undo him."
    },
    "12": {
      "L": "Are you not from everlasting, O LORD my God, my Holy One? We shall not die. O LORD, you have appointed them for judgment; O Rock, you have established them for correction.",
      "M": "Are you not from everlasting, O LORD my God, my Holy One? We will not die. LORD, you have appointed them as an instrument of judgment; O Rock, you have established them for correction.",
      "T": "You are the Eternal One, Yahweh my God, my Holy One — and because of that, we will not perish. You yourself, LORD, have set the Chaldeans in motion as a judicial instrument, as correction. You, the Rock, decreed this."
    },
    "13": {
      "L": "You are of eyes too pure to behold evil and cannot look on trouble; why do you look on those who deal treacherously and hold your silence when the wicked swallows up the man more righteous than he?",
      "M": "Your eyes are too pure to approve of evil; you cannot look upon wickedness. Why then do you tolerate those who act treacherously? Why are you silent while the wicked swallows up someone more righteous than himself?",
      "T": "You are too holy to look at evil with approval — your eyes are utterly clean. Yet here you are, watching treachery unfold and staying silent. Why? The wicked are swallowing up those more righteous than themselves, and you say nothing."
    },
    "14": {
      "L": "Why do you make mankind like the fish of the sea, like crawling things that have no ruler over them?",
      "M": "Why have you made humanity like the fish of the sea, like creeping things that have no one to rule over them?",
      "T": "You have reduced people to the level of fish — creatures with no king, no shepherd, just prey for whatever power is bigger."
    },
    "15": {
      "L": "He brings all of them up with a hook; he drags them out in his net; he gathers them in his dragnet; therefore he rejoices and exults.",
      "M": "He hauls all of them up with a fishhook; he drags them away in his net; he collects them in his dragnet; so he rejoices and is glad.",
      "T": "The Chaldean hauls nations up like fish — hook, net, dragnet. Then he celebrates over the catch. To him it is sport."
    },
    "16": {
      "L": "Therefore he sacrifices to his net and burns incense to his dragnet; for by them his portion is fat and his food is sumptuous.",
      "M": "So he offers sacrifices to his net and burns incense to his dragnet; for by them his portion is rich and his food is plentiful.",
      "T": "He worships his own military machine — sacrifices to the net, burns offerings to the dragnet. His weapons are his gods; they keep him fed and prosperous. The creature bows to its own tools."
    },
    "17": {
      "L": "Shall he therefore keep emptying his net and continue slaying nations without mercy?",
      "M": "Will he keep on emptying his net, slaying nations without pity, forever?",
      "T": "And is this simply going to continue? Will he keep casting the net, hauling in nation after nation, and never face a reckoning?"
    }
  },
  "2": {
    "1": {
      "L": "I will stand at my watch-post and station myself on the tower; I will keep watch to see what he will say to me, and what I shall answer when I am rebuked.",
      "M": "I will take my post at the watchtower and station myself on the rampart; I will watch to see what he will say to me, and what reply I am to give when I am corrected.",
      "T": "I will take my stand at the watchpost. I will go up to the rampart and wait — watching to see what God will say, and what answer I am to make when he turns the question back on me."
    },
    "2": {
      "L": "And the LORD answered me: 'Write the vision; make it plain upon tablets, so that the one who reads it may run with it.'",
      "M": "Then the LORD answered me: 'Write down the vision; inscribe it plainly on tablets so that the one who reads it can carry the message at a run.'",
      "T": "The LORD answered: 'Write this vision down — engrave it on tablets, make it unmistakable, so that a messenger can carry it at a run and every reader can grasp it instantly.'"
    },
    "3": {
      "L": "For the vision is yet for the appointed time; it speaks to the end and will not lie. Though it tarry, wait for it; it will surely come; it will not delay.",
      "M": "For the vision awaits its appointed time; it speaks of the final outcome and will not prove false. Though it lingers, wait for it — it will certainly come; it will not be late.",
      "T": "The vision has its own appointed moment. It points to the final outcome and will not disappoint. Even if it seems to stall — wait. It will arrive exactly on schedule. It does not know how to be late."
    },
    "4": {
      "L": "Behold, his soul is puffed up and is not upright in him; but the righteous shall live by his faithfulness.",
      "M": "Behold, the soul of the one who is lifted up is not upright within him; but the righteous shall live by his faithfulness.",
      "T": "Look: the one whose soul is swollen with pride has no uprightness in him. But the one who is righteous — who holds steady, who lives by covenant faithfulness — that person will live."
    },
    "5": {
      "L": "Moreover, wine is treacherous; the arrogant man will not abide. He makes his desire as wide as Sheol; and like death he is not satisfied. He gathers all nations to himself and assembles all peoples to himself.",
      "M": "Furthermore, wine is a deceiver; the proud man cannot stay put. He opens his appetite as wide as Sheol; like death he is never satisfied. He gathers all nations to himself and assembles all peoples for himself.",
      "T": "Wine proves as treacherous as the man who drinks it. The arrogant cannot rest — something keeps driving them outward. Their desire is as bottomless as the grave; like death, they are never full. Nation after nation, people after people — they consume them all and still want more."
    },
    "6": {
      "L": "Shall not all of them take up a taunt against him, with proverbs and riddles? They shall say, 'Woe to him who heaps up what is not his — how long? — and loads himself down with pledges!'",
      "M": "Will not all of them take up a mocking song against him — a proverb and a taunt? They will say, 'Woe to the one who piles up wealth that is not his, loading himself down with pledges — how long can this go on?'",
      "T": "The day is coming when all those he plundered will take up a mocking chorus against him: 'Woe to the one who piles up stolen wealth and lives on other people's blood pledged as his security! How long do you think this can last?'"
    },
    "7": {
      "L": "Will not your creditors suddenly arise, and those who make you tremble awake? Then you will become their plunder.",
      "M": "Will not your debtors suddenly turn on you? Will not those you terrified rise against you? Then you will become their spoil.",
      "T": "The very people you bled dry will rise against you — suddenly, without warning. The ones you terrorized will turn and make you tremble. You will become the plunder."
    },
    "8": {
      "L": "Because you have plundered many nations, all the remnant of the peoples will plunder you — for the blood of men and violence to the land, to the city and all who dwell in it.",
      "M": "Because you have plundered many nations, all the surviving peoples will plunder you — for the blood shed against humanity and for the violence done to the land, to the cities and all who live in them.",
      "T": "You have looted nation after nation — so what remains of those nations will loot you. Blood demands blood. The violence you inflicted on every land and city and everyone who lived there will come back on your own head."
    },
    "9": {
      "L": "Woe to him who gets evil gain for his house, to set his nest on high, to deliver himself from the grip of calamity!",
      "M": "Woe to him who makes unjust profit for his household, to place his nest on high, to save himself from the reach of disaster!",
      "T": "Woe to the one who rakes in ill-gotten wealth for the sake of his own household — building his nest so high that no disaster can reach him, thinking himself secure above the fray."
    },
    "10": {
      "L": "You have devised shame for your house by cutting off many peoples, and have sinned against your own soul.",
      "M": "You have plotted the disgrace of your own household by destroying many peoples, and have brought guilt upon yourself.",
      "T": "In trying to secure your household you have only disgraced it. By annihilating peoples you have sinned against your own life — you have forged the instrument of your own ruin."
    },
    "11": {
      "L": "For the stone will cry out from the wall, and the beam out of the timber will answer it.",
      "M": "For the very stone in the wall will cry out against you, and the wooden beam will echo the charge.",
      "T": "The very house you built with blood will testify against you — the stones will cry out from the walls, and the roof beams will answer back in chorus."
    },
    "12": {
      "L": "Woe to him who builds a city with bloodshed and establishes a town on iniquity!",
      "M": "Woe to the one who builds a city on bloodshed and founds a town by injustice!",
      "T": "Woe to the city-builder whose mortar is blood and whose foundations are laid in injustice!"
    },
    "13": {
      "L": "Behold, is it not from the LORD of hosts that peoples labor only for fire, and nations weary themselves for nothing?",
      "M": "Is it not indeed from the LORD of hosts that peoples labor only to fuel the flames, and nations exhaust themselves for nothing?",
      "T": "Has it not been decreed by the LORD of hosts? All their labor will go up in smoke; all their straining will end in nothing. The great empire is building its own bonfire."
    },
    "14": {
      "L": "For the earth shall be filled with the knowledge of the glory of the LORD as the waters cover the sea.",
      "M": "For the earth will be filled with the knowledge of the glory of the LORD, as the waters cover the sea.",
      "T": "For the whole earth will one day be filled — saturated, as the sea is covered by water — with the knowledge of the glory of the LORD. Every empire is temporary; that filling is not."
    },
    "15": {
      "L": "Woe to him who makes his neighbor drink — pouring out your wrath to make him drunk — so that you may gaze on their nakedness!",
      "M": "Woe to the one who makes his neighbor drink — pouring out your wrath mixed in a cup, making him drunk — so that you may stare at his nakedness!",
      "T": "Woe to the one who gets his neighbors drunk — pouring out humiliation mixed with wine — just to expose and exploit them in their shame. Violence wearing the mask of hospitality."
    },
    "16": {
      "L": "You will be filled with shame instead of glory. Drink yourself, and let your foreskin be uncovered! The cup in the LORD's right hand will come around to you, and disgrace will cover your glory.",
      "M": "You will be glutted with shame instead of glory. Drink in turn — and let your own nakedness be exposed! The cup in the LORD's right hand will come to you, and shameful disgrace will overtake your glory.",
      "T": "You wanted glory — you will get shame poured to the brim. The cup is coming to you now; your own shameful nakedness will be uncovered. The LORD's own right hand holds the cup — and what he pours out on the nations, he pours out on you."
    },
    "17": {
      "L": "For the violence done to Lebanon will cover you, and the destruction of the animals will terrify you — because of the blood of men and the violence done to the land, to the city and all who dwell in it.",
      "M": "For the violence you did to Lebanon will overwhelm you, and the terror you brought upon its wildlife will recoil on you — because of the blood of humanity and the violence done to the land, to the cities and all their inhabitants.",
      "T": "Lebanon's stripped forests will bury you; the terror you drove into the wildlife will drive back into you. All the blood of the people, all the violence heaped on every land, every city, everyone living there — it all comes home."
    },
    "18": {
      "L": "What does a carved image profit when its maker has shaped it — a molten image, a teacher of lies? For its maker trusts in his own making when he fashions speechless idols.",
      "M": "What use is a carved idol when its maker has shaped it? It is a cast image, a teacher of lies. For its maker trusts in his own creation when he forms gods that cannot speak.",
      "T": "What is the point of a carved image? The craftsman made it — then bows to what he himself fashioned. A cast idol that teaches only lies. He trusts the work of his own hands; he worships the mute."
    },
    "19": {
      "L": "Woe to him who says to a piece of wood, 'Awake!' and to a silent stone, 'Arise!' Can this teach? Behold, it is overlaid with gold and silver, and there is no breath at all in it.",
      "M": "Woe to the one who says to a wooden idol, 'Awake!' and to a mute stone, 'Rise up!' Can it really teach? See — it is overlaid with gold and silver, yet there is no breath in it at all.",
      "T": "Woe to the one who shakes a block of wood and commands it, 'Wake up!' — or prods a dumb stone: 'Get up and do something!' These gilded objects covered in gold and silver are absolutely lifeless. There is no breath, no spirit, nothing in them."
    },
    "20": {
      "L": "But the LORD is in his holy temple; let all the earth keep silence before him.",
      "M": "But the LORD is in his holy temple; let all the earth be silent before him.",
      "T": "But the LORD is present in his holy sanctuary. The entire earth — every empire, every idol-maker, every woe-worthy nation — let them all fall silent before him."
    }
  },
  "3": {
    "1": {
      "L": "A prayer of Habakkuk the prophet upon Shigionoth.",
      "M": "A prayer of Habakkuk the prophet, set to Shigionoth.",
      "T": "A prayer of Habakkuk the prophet — set to a passionate, irregular melody."
    },
    "2": {
      "L": "O LORD, I have heard your report and was afraid. O LORD, revive your work in the midst of the years; in the midst of the years make it known; in wrath remember mercy.",
      "M": "O LORD, I have heard your report and stood in awe. O LORD, carry out your work in the midst of these years; in the midst of these years make it known. In your wrath, remember compassion.",
      "T": "LORD, I have heard what you are doing — and it shook me to the core. O LORD, do your great work now, in our own lifetime; make yourself known in our own days. And when your wrath moves — remember mercy."
    },
    "3": {
      "L": "God came from Teman, and the Holy One from Mount Paran. Selah. His glory covered the heavens, and the earth was full of his praise.",
      "M": "God came from Teman; the Holy One came from Mount Paran. Selah. His glory covered the heavens, and the earth was filled with his praise.",
      "T": "God swept in from Teman; the Holy One blazed down from Paran. [Selah.] His glory cloaked the sky from horizon to horizon; every corner of the earth rang with his praise."
    },
    "4": {
      "L": "His brightness was like the light; rays came forth from his hand; and there was the veiling of his power.",
      "M": "His radiance shone like light; rays of brightness came from his hand; and there was the hiding place of his power.",
      "T": "Light poured from him like the sun at full strength. What appeared to be mere rays was his hand reaching out — and even then, the full depth of his power remained hidden behind that brightness."
    },
    "5": {
      "L": "Before him went pestilence, and burning plague went out at his feet.",
      "M": "Pestilence marched before him, and burning plague went out at his feet.",
      "T": "Pestilence marched ahead of him like a vanguard; at his heels, burning sickness spread wherever he walked."
    },
    "6": {
      "L": "He stood and measured the earth; he looked and caused the nations to tremble; the ancient mountains were shattered; the everlasting hills bowed down. His ways are everlasting.",
      "M": "He stopped and shook the earth; with a look he scattered the nations; the ancient mountains crumbled; the eternal hills bowed low. His paths are age-old.",
      "T": "He stopped — and the whole earth shook with the impact of his standing still. One glance and the nations scattered. Mountains that had stood since before memory crumbled; hills that had been there forever buckled. His ways outlast all of them."
    },
    "7": {
      "L": "I saw the tents of Cushan in affliction; the curtains of the land of Midian trembled.",
      "M": "I saw the tents of Cushan in distress; the tent-curtains of the land of Midian trembled.",
      "T": "I looked and saw it: the tent-villages of Cushan convulsing in anguish; the hanging curtains of Midian shaking — nations struck with a terror they could not name."
    },
    "8": {
      "L": "Was your wrath against the rivers, O LORD? Was your anger against the rivers, or your fury against the sea — that you rode upon your horses, your chariots of salvation?",
      "M": "Were you angry at the rivers, O LORD? Was your wrath against the rivers, or your fury against the sea? Is that why you mounted your horses and drove your chariots of victory?",
      "T": "Was it the rivers you were angry at, LORD? Was it the sea that provoked your fury — when you mounted your warhorses and drove your chariots of salvation across the water? No — it was never the river. Never the sea."
    },
    "9": {
      "L": "Your bow was stripped naked; the sworn oaths to the tribes were a word. Selah. You split the earth open with rivers.",
      "M": "Your bow was unsheathed and made bare; your sworn oaths to the tribes stood firm. Selah. You split the earth open with rivers.",
      "T": "Your bow was unsheathed, string pulled taut — not from anger at nature, but in faithfulness to the covenant oaths sworn to the tribes of your people. [Selah.] The earth split open at your passage; rivers poured through."
    },
    "10": {
      "L": "The mountains saw you and writhed; the rushing waters swept through; the deep uttered its voice and lifted its hands on high.",
      "M": "The mountains saw you and convulsed; the floodwaters swept past; the deep roared out its voice and raised its waves high.",
      "T": "The mountains caught sight of you and convulsed. The floodwaters surged and swept past. Even the great deep bellowed out its voice, hurling its waves upward like arms raised in awe."
    },
    "11": {
      "L": "Sun and moon stood still in their places at the light of your flying arrows, at the flash of your glittering spear.",
      "M": "The sun and moon stood still in their places at the gleam of your flying arrows and the flash of your glittering spear.",
      "T": "The sun and the moon froze in their tracks — stopped by the brightness of your arrows in flight, by the blinding flash of your spear. Even the great lights of heaven yielded to your light."
    },
    "12": {
      "L": "In indignation you marched through the earth; in anger you threshed the nations.",
      "M": "In your fury you strode through the earth; in your anger you trampled the nations.",
      "T": "You marched through the earth in blazing fury; you threshed the nations like grain under your wrath."
    },
    "13": {
      "L": "You went out for the salvation of your people, for the salvation of your anointed. You struck the head of the wicked house, laying bare the foundation to the neck. Selah.",
      "M": "You went out to save your people, to save your anointed one. You struck the head from the wicked household, stripping it bare from foundation to neck. Selah.",
      "T": "All of it — the earthquake, the flood, the stopped sun — was for your people. You came out to rescue them; your anointed was what you were fighting for. And you crushed the head of the wicked regime — stripped its power from neck down to foundation. [Selah.]"
    },
    "14": {
      "L": "You pierced with his own staves the head of his warriors; they came as a whirlwind to scatter me, their rejoicing as if to devour the poor in secret.",
      "M": "You pierced the head of his warlords with their own weapons; they had charged like a whirlwind to scatter us, exulting as if to devour the helpless in a hidden ambush.",
      "T": "You turned their own weapons against them — pierced the commanders' heads with their own spears. They had come storming in like a tornado, whooping with joy at the thought of swallowing the helpless in some hidden ambush. Instead, you destroyed them."
    },
    "15": {
      "L": "You trampled the sea with your horses, through the surging of mighty waters.",
      "M": "You trod through the sea with your horses, churning through great mounds of water.",
      "T": "Your warhorses rode through the sea itself — trampling through the heaped-up mountains of water."
    },
    "16": {
      "L": "I heard, and my belly trembled; my lips quivered at the sound; rottenness entered into my bones and I trembled where I stood. I will quietly wait for the day of trouble to come upon the people who invade us.",
      "M": "When I heard, my whole body trembled; at the sound my lips quivered; rottenness crept into my bones and my legs gave way beneath me. I will quietly wait for the day of trouble to come on the people who attack us.",
      "T": "When I heard all this — the account of your power, the coming judgment — my body fell apart with fear. My lips quivered; decay seemed to seep into my very bones; my legs shook beneath me. And yet — I will stand still and wait. Let the day of trouble come. Let it fall on those who are coming against us."
    },
    "17": {
      "L": "Though the fig tree should not blossom, nor fruit be on the vines; though the produce of the olive fail, and the fields yield no food; though the flock be cut off from the fold, and there be no herd in the stalls —",
      "M": "Though the fig tree does not blossom and there is no fruit on the vine; though the olive harvest fails and the fields produce no food; though the flock is cut off from the fold and there is no herd in the stalls —",
      "T": "Even if — the fig tree puts out no blossoms, the vine bears no grapes, the olive trees yield nothing, the terraced fields produce no food, the sheep are all gone from the pen, and the cattle stalls stand empty —"
    },
    "18": {
      "L": "Yet I will rejoice in the LORD; I will exult in the God of my salvation.",
      "M": "Yet I will exult in the LORD; I will rejoice in the God of my salvation.",
      "T": "Even then — I will rejoice in Yahweh. I will burst into joy over the God who rescues me."
    },
    "19": {
      "L": "The Lord GOD is my strength; he makes my feet like the deer's and makes me tread on my high places. To the choirmaster: with stringed instruments.",
      "M": "The Lord GOD is my strength; he gives me feet like a deer and makes me walk on the heights. For the choir director: on stringed instruments.",
      "T": "Yahweh, my Lord, is my strength. He will make my feet light and sure as a deer's, and lead me to walk the high places. [For the choir director: with stringed instruments.]"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'habakkuk')
        merge_tier(existing, HABAKKUK, tier_key)
        save(tier_dir, 'habakkuk', existing)
    print('Habakkuk 1–3 written.')

if __name__ == '__main__':
    main()
