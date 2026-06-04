"""
MKT Isaiah chapters 19–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-19-21.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from chs 1–9; the divine
  personal name is surfaced in T throughout Isaiah to restore its directness.
- H136 (אֲדֹנָי): "Lord" (L/M/T); in 19:4 "אֲדֹנָי יְהוָה צְבָאוֹת" = "the Lord, the LORD
  of hosts" (L/M) / "the Lord, Yahweh of hosts" (T).
- H6635 (צְבָאוֹת): "of hosts" across all tiers — cosmic sovereignty designation, consistent
  with all prior Isaiah scripts.
- H4853 (מַשָּׂא): "burden" (L) / "oracle" (M/T) — the Hebrew means "a heavy load/lifting";
  L preserves the concrete force of prophetic speech as weight.
- H7307 (רוּחַ) in 19:3,14: lowercase "spirit" — not the divine Spirit; in 19:3 it is
  Egypt's own national resolve that drains away; in 19:14 it is a spirit of confusion
  poured into Egypt by the LORD as judgment.
- H8419 (תַּהְפֻּכוֹת) in 19:14: "perverseness" (L) / "confusion" (M/T).
- H4156 (מֹעֵצָה) in 19:3: "counsel" (L/M) / "strategy" (T).
- H4941 (מִשְׁפָּט): "judgment" (L) / "justice" (M/T) — consistent with chs 1–9.
- H6666 (צְדָקָה): "righteousness" (L/M/T) — consistent.
- 19:18 textual note: MT reads עִיר הַהֶרֶס ("City of Destruction"); many MSS, the LXX,
  and the Qere read עִיר הַחֶרֶס ("City of the Sun" = Heliopolis). Modern scholarship
  slightly favors the Q reading (a city of the sun-god swearing to Yahweh carries sharper
  theological irony). L follows the MT ("City of Destruction"); M/T follow the Q reading
  ("City of the Sun").
- 19:25 theological note: Yahweh calls Egypt "my people" and Assyria "the work of my hands"
  — the same honorifics applied to Israel elsewhere. This eschatological universalism is
  preserved without softening in all three tiers. H5971 (עַם) = "my people" is exact.
- 19:6: "rivers" and "channels" refer to the Nile's distributary branches and irrigation
  canals — Egypt's agricultural lifeline; their failure is total economic collapse.
- Chapter 20: Isaiah's three-year naked sign-act (H6174 = naked, stripped; not metaphorical
  but a literal public shaming display). All tiers convey the stark physical reality.
  "Cush/Ethiopia" throughout ch. 20 = the land south of Egypt (modern Sudan/Ethiopia);
  the sign covers both nations because they formed a joint defensive coalition against Assyria.
- Chapter 21: Three separate oracles: vv. 1–10 (Babylon = "Desert of the Sea"), vv. 11–12
  (Dumah = Edom; Hebrew dumah also means "silence"), vv. 13–17 (Arabia/Kedar).
  The "Desert of the Sea" refers to Babylon in lower Mesopotamia's marshland plain.
  The anguish in vv. 3–4 is the prophet's own visceral response to the vision.
- 21:5: The scene (table set, princes drinking) echoes Belshazzar's feast in Dan 5 — the
  irony that Babylon's destruction comes amid a banquet is deliberate. "Anoint the shields"
  means prepare for imminent battle while still at the table.
- "Watchman" motif (chs. 21:6–12): connects to the watchtower theology in Isa 62:6.
- 21:10 "O my threshing": Israel is addressed as grain that has been trampled; the prophet
  declares what he has received so that threshed Israel may also hear Babylon's end.
- Poetry/prose structure: Ch. 19:1–15 is prose oracle. Ch. 19:16–25 is eschatological
  prose (repeated "in that day" structure). Ch. 20 is narrative prose. Ch. 21:1–4 has
  strong visionary poetry; vv. 11–12 are an enigmatic exchange in poetic form; otherwise
  ch. 21 is prose. T uses line breaks for the most poetic/visionary passages throughout.
- Aspect: Prophetic presents in 19:1–15 rendered as vivid present-tense certainties;
  19:16–25 futures are eschatological promises. Ch. 20 narrative = simple past throughout.
  21:1–10 alternates between visionary present and sudden reported speech (v. 9, fallen!).
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
  "19": {
    "1": {
      "L": "The burden of Egypt. Behold, the LORD rideth upon a swift cloud, and cometh into Egypt; and the idols of Egypt shall tremble at his presence, and the heart of Egypt shall melt within it.",
      "M": "The oracle of Egypt. See, the LORD is coming on a swift cloud to Egypt; the idols of Egypt will tremble before him, and the heart of Egypt will melt within it.",
      "T": "Oracle against Egypt.\nYahweh rides in on a swift cloud, coming into Egypt —\nthe idols of Egypt shudder at his approach,\nand Egypt's courage dissolves within her."
    },
    "2": {
      "L": "And I will stir up the Egyptians against the Egyptians, and they shall fight, every one against his brother, and every one against his neighbour; city against city, and kingdom against kingdom.",
      "M": "I will stir up Egyptians against Egyptians, and they will fight each other — brother against brother, neighbor against neighbor, city against city, region against region.",
      "T": "I will pit Egyptian against Egyptian — brother against brother, neighbor against neighbor, city against city, faction against faction."
    },
    "3": {
      "L": "And the spirit of Egypt shall be poured out in the midst of it, and I will swallow up its counsel; and they shall seek unto the idols, and unto the enchanters, and unto them that have familiar spirits, and unto the wizards.",
      "M": "Egypt's spirit will drain away within it; I will confound its plans; the Egyptians will turn to idols, enchanters, mediums, and spiritists.",
      "T": "Egypt's spirit will drain away;\nI will confound their strategy —\nthey will turn in desperation to idols, sorcerers, mediums, and spiritists."
    },
    "4": {
      "L": "And I will give over the Egyptians into the hand of a hard lord; and a fierce king shall rule over them, saith the Lord, the LORD of hosts.",
      "M": "I will hand Egypt over to a harsh master; a cruel king will rule over them, declares the Lord, the LORD of hosts.",
      "T": "I will surrender Egypt into the grip of a harsh master;\na ruthless king will rule over them —\nso declares the Lord, Yahweh of hosts."
    },
    "5": {
      "L": "And the waters shall fail from the sea, and the river shall be wasted and dried up.",
      "M": "The water of the Nile will dry up, and the river will be parched and drained.",
      "T": "The Nile's waters will fail;\nthe river parched and drained dry."
    },
    "6": {
      "L": "And the rivers shall stink; the canals of Egypt shall be diminished and dried up; the reeds and rushes shall wither.",
      "M": "The channels will become foul; the branches of Egypt's Nile will shrink and dry up; reeds and rushes will wither.",
      "T": "The river channels will turn foul;\nthe Nile's many branches will shrink and dry;\nreeds and rushes will wither away."
    },
    "7": {
      "L": "The papyrus reeds at the mouth of the Nile, by the Nile, and everything sown by the Nile, shall wither, be driven away, and be no more.",
      "M": "The papyrus reeds along the Nile, at its outflows, and all crops planted along its banks will wither, blow away, and cease to exist.",
      "T": "The papyrus along the Nile, at every mouth and outflow,\nand all the cropland planted along its banks —\nwill wither, scatter, and disappear."
    },
    "8": {
      "L": "And the fishers shall mourn, and all they that cast a hook in the Nile shall lament; and they that spread nets upon the waters shall pine away.",
      "M": "The fishermen will mourn; all who cast a hook into the Nile will lament; those who spread nets on the water will languish.",
      "T": "The fishermen will mourn —\nthose who cast their lines into the Nile will lament,\nand those who spread their nets on the water will languish."
    },
    "9": {
      "L": "Moreover they that work in combed flax, and they that weave fine cloth, shall be put to shame.",
      "M": "Those who work with combed flax and those who weave fine linen will be put to shame.",
      "T": "The workers of combed flax,\nthe weavers of fine white linen —\nthey will be put to shame."
    },
    "10": {
      "L": "And they shall be shattered in their purposes; all that work for hire shall be grieved in soul.",
      "M": "Egypt's foundations will be crushed; all who work for hire will be sick at heart.",
      "T": "Egypt's very foundations will crumble;\nevery wage-worker will be sick with grief."
    },
    "11": {
      "L": "Surely the princes of Zoan are fools; the counsel of the wisest counsellors of Pharaoh is become brutish; how say ye unto Pharaoh, I am the son of the wise, the son of ancient kings?",
      "M": "The princes of Zoan are utter fools; the wisest of Pharaoh's counselors give worthless advice. How can they say to Pharaoh, 'I am a descendant of the sages, a son of ancient kings'?",
      "T": "Zoan's princes are fools —\nPharaoh's wisest advisors give nothing but stupid counsel.\nHow dare they boast to Pharaoh: 'I am a son of the sages, a descendant of ancient kings'?"
    },
    "12": {
      "L": "Where are they? Where are thy wise men? And let them tell thee now, and let them know what the LORD of hosts hath purposed concerning Egypt.",
      "M": "Where are your wise men now? Let them tell you; let them make known what the LORD of hosts has planned against Egypt.",
      "T": "Where are they — your wise men?\nLet them tell you! Let them declare\nwhat Yahweh of hosts has determined against Egypt."
    },
    "13": {
      "L": "The princes of Zoan are become fools; the princes of Noph are deceived; and the chiefs of the tribes of Egypt have caused her to err.",
      "M": "The princes of Zoan have made themselves fools; the princes of Memphis are deluded; the leaders of Egypt's clans have led the nation astray.",
      "T": "Zoan's princes have made themselves fools;\nMemphis's princes are utterly deceived;\nthe chiefs of Egypt's clans have led the whole country astray."
    },
    "14": {
      "L": "The LORD hath mingled in her midst a spirit of perverseness; and they have caused Egypt to stagger in all her works, as a drunken man staggereth in his vomit.",
      "M": "The LORD has poured into Egypt a spirit of confusion; the Egyptians err in everything they do, like a drunkard reeling in his vomit.",
      "T": "Yahweh has poured into Egypt a spirit of confusion —\nthey stagger in everything they undertake,\nlike a drunkard stumbling through his own vomit."
    },
    "15": {
      "L": "Neither shall there be any work for Egypt which the head or tail, branch or rush, may do.",
      "M": "There will be nothing Egypt can accomplish — neither head nor tail, neither palm branch nor reed.",
      "T": "Egypt will find nothing to do —\nhead or tail, towering palm or lowly reed —\nnot one of them will accomplish anything."
    },
    "16": {
      "L": "In that day shall Egypt be like unto women; and it shall tremble and fear because of the shaking of the hand of the LORD of hosts which he shaketh over it.",
      "M": "In that day the Egyptians will be like frightened women, trembling with fear because of the hand of the LORD of hosts that he raises against them.",
      "T": "On that day Egypt will be like frightened women,\nshaking with terror at the hand Yahweh of hosts raises against her."
    },
    "17": {
      "L": "And the land of Judah shall be a terror unto Egypt; every one that maketh mention of it shall be afraid, because of the counsel of the LORD of hosts which he hath determined against it.",
      "M": "The land of Judah will become a source of dread to Egypt; whenever Judah is mentioned, they will tremble because of what the LORD of hosts has determined against Egypt.",
      "T": "The very mention of Judah will terrify Egypt —\nanyone who speaks the name will fill Egyptian hearts with dread,\nbecause of what Yahweh of hosts has determined against her."
    },
    "18": {
      "L": "In that day shall five cities in the land of Egypt speak the language of Canaan, and swear to the LORD of hosts; one shall be called, The city of destruction.",
      "M": "In that day five cities in Egypt will speak the language of Canaan and swear loyalty to the LORD of hosts. One will be called the City of the Sun.",
      "T": "On that day five Egyptian cities will speak the language of Canaan and swear allegiance to Yahweh of hosts. One will be called the City of the Sun."
    },
    "19": {
      "L": "In that day shall there be an altar to the LORD in the midst of the land of Egypt, and a pillar at the border thereof to the LORD.",
      "M": "In that day there will be an altar to the LORD in the heart of Egypt, and a standing stone at its border dedicated to the LORD.",
      "T": "On that day there will be an altar to Yahweh\nin the very heart of Egypt,\nand a memorial pillar to Yahweh at its border."
    },
    "20": {
      "L": "And it shall be for a sign and for a witness unto the LORD of hosts in the land of Egypt; for they shall cry unto the LORD because of oppressors, and he shall send them a saviour, even a great one, and he shall deliver them.",
      "M": "It will serve as a sign and witness to the LORD of hosts in the land of Egypt. When they cry out to the LORD because of their oppressors, he will send them a savior and champion who will rescue them.",
      "T": "It will stand as a sign and witness to Yahweh of hosts in the land of Egypt —\nand when they cry to Yahweh because of their oppressors,\nhe will send them a rescuer and champion who will deliver them."
    },
    "21": {
      "L": "And the LORD shall be known to Egypt, and the Egyptians shall know the LORD in that day, and shall worship with sacrifice and grain offering; they shall vow a vow unto the LORD, and shall perform it.",
      "M": "The LORD will make himself known to Egypt, and the Egyptians will acknowledge the LORD in that day. They will worship him with sacrifices and grain offerings; they will make vows to the LORD and keep them.",
      "T": "Yahweh will reveal himself to Egypt,\nand Egypt will acknowledge Yahweh on that day —\nthey will worship with sacrifice and grain offering,\nmake vows to Yahweh and keep them."
    },
    "22": {
      "L": "And the LORD shall smite Egypt, smiting and healing; and they shall return unto the LORD, and he shall be entreated of them, and shall heal them.",
      "M": "The LORD will strike Egypt — striking and healing — and they will turn back to the LORD. He will hear their pleas and heal them.",
      "T": "Yahweh will strike Egypt — strike and then heal.\nThey will turn back to Yahweh;\nhe will hear their plea and heal them."
    },
    "23": {
      "L": "In that day shall there be a highway from Egypt to Assyria; and the Assyrian shall come into Egypt, and the Egyptian into Assyria; and the Egyptians shall serve with the Assyrians.",
      "M": "In that day there will be a highway from Egypt to Assyria. The Assyrians will come into Egypt and the Egyptians into Assyria, and the Egyptians will worship together with the Assyrians.",
      "T": "On that day a highway will run from Egypt all the way to Assyria —\nAssyrians coming into Egypt, Egyptians going to Assyria,\nand both peoples worshipping Yahweh together."
    },
    "24": {
      "L": "In that day shall Israel be the third with Egypt and with Assyria, a blessing in the midst of the earth;",
      "M": "In that day Israel will be the third alongside Egypt and Assyria, a blessing in the midst of the earth,",
      "T": "On that day Israel will take its place alongside Egypt and Assyria —\na triad of blessing at the center of the earth —"
    },
    "25": {
      "L": "whom the LORD of hosts shall bless, saying, Blessed be Egypt my people, and Assyria the work of my hands, and Israel mine inheritance.",
      "M": "whom the LORD of hosts will bless, saying, 'Blessed be Egypt my people, and Assyria the work of my hands, and Israel my inheritance.'",
      "T": "whom Yahweh of hosts will bless, declaring:\n'Blessed be Egypt, my people;\nAssyria, the work of my hands;\nand Israel, my inheritance.'"
    }
  },
  "20": {
    "1": {
      "L": "In the year that Tartan came unto Ashdod, when Sargon the king of Assyria sent him, and he fought against Ashdod and took it;",
      "M": "In the year that the commander-in-chief came to Ashdod — when Sargon king of Assyria sent him — and he attacked Ashdod and captured it,",
      "T": "The year Sargon king of Assyria sent his commander-in-chief against Ashdod — the year Ashdod fell —"
    },
    "2": {
      "L": "at that time the LORD spake by Isaiah the son of Amoz, saying, Go, loose the sackcloth from off thy loins, and put thy shoe from off thy foot. And he did so, walking naked and barefoot.",
      "M": "at that time the LORD spoke through Isaiah son of Amoz, saying, 'Go, take the sackcloth off your waist and remove the sandal from your foot.' He obeyed, walking naked and barefoot.",
      "T": "at that time Yahweh spoke through Isaiah son of Amoz:\n'Go — strip off your sackcloth, take your sandal from your foot.'\nHe obeyed, going about naked and barefoot."
    },
    "3": {
      "L": "And the LORD said, Like as my servant Isaiah hath walked naked and barefoot three years for a sign and wonder upon Egypt and upon Ethiopia;",
      "M": "Then the LORD said, 'Just as my servant Isaiah has walked naked and barefoot for three years as a sign and portent against Egypt and Cush —'",
      "T": "Then Yahweh said: 'Just as my servant Isaiah has walked naked and barefoot for three years as a sign and omen against Egypt and Cush —'"
    },
    "4": {
      "L": "so shall the king of Assyria lead away the Egyptians as captives, and the Ethiopians as exiles, young and old, naked and barefoot, with buttocks uncovered, to the shame of Egypt.",
      "M": "so the king of Assyria will lead away the Egyptian captives and the Cushite exiles, young and old alike, naked and barefoot, with their buttocks exposed — Egypt's humiliation laid bare.",
      "T": "so the king of Assyria will march Egypt and Cush into exile —\nyoung and old together, naked, barefoot, buttocks exposed —\nEgypt's shame laid bare for every nation to see."
    },
    "5": {
      "L": "And they shall be dismayed and ashamed of Ethiopia their expectation, and of Egypt their glory.",
      "M": "Those who looked to Cush with expectation and took pride in Egypt will be terrified and put to shame.",
      "T": "Those who pinned their hope on Cush\nand took pride in Egypt\nwill be terrified and put to shame."
    },
    "6": {
      "L": "And the inhabitant of this coastland shall say in that day, Behold, such is our expectation, whither we fled for help to be delivered from the king of Assyria; and how shall we escape?",
      "M": "In that day the people of this coastland will say, 'This is what has happened to those we relied on, to whom we fled for help and rescue from the king of Assyria. How then shall we escape?'",
      "T": "On that day the people of this coastland will say:\n'Look what has happened to those we counted on —\nwe ran to them to escape the king of Assyria!\nNow how will we get away?'"
    }
  },
  "21": {
    "1": {
      "L": "The burden of the desert of the sea. As whirlwinds in the Negeb sweep through, so it cometh from the desert, from a terrible land.",
      "M": "The oracle of the Desert of the Sea. Like whirlwinds sweeping through the Negeb, it comes from the desert, from a dreadful land.",
      "T": "Oracle of the Desert of the Sea.\nLike cyclones raging across the Negeb,\nit sweeps in — out of the desert, out of a terrible land."
    },
    "2": {
      "L": "A hard vision is declared unto me: the treacherous one dealeth treacherously, and the destroyer destroyeth. Go up, O Elam; besiege, O Media; all the sighing thereof have I brought to an end.",
      "M": "A grim vision has been shown to me: the traitor betrays, the plunderer plunders. March, O Elam! Besiege, O Media! All the groaning Babylon caused I will bring to an end.",
      "T": "A grim vision has been laid before me:\nthe traitor betrays, the plunderer plunders.\nCharge, O Elam! Besiege, O Media!\nAll the groaning Babylon caused — I have brought it to its end."
    },
    "3": {
      "L": "Therefore are my loins filled with anguish; pangs have seized me, as the pangs of a woman in labour; I am bowed down at the hearing; I am dismayed at the seeing.",
      "M": "Therefore my body is racked with anguish; labor pains have seized me like those of a woman giving birth; I am too shaken to hear, too shattered to see.",
      "T": "Therefore my whole body writhes in anguish —\ncramps like a woman in labor have seized me.\nI am too overcome to hear, too shattered to see."
    },
    "4": {
      "L": "My heart staggers; fearfulness hath seized me; the night of my pleasure hath he turned to trembling for me.",
      "M": "My mind reels; a shuddering terror grips me; the evening I had longed for has been turned into dread.",
      "T": "My mind reels; terror has seized me —\nthe evening I longed for\nhas been turned into dread."
    },
    "5": {
      "L": "Prepare the table; set the watch; eat, drink! Arise, O princes, and anoint the shields.",
      "M": "Set the table, spread the rugs, eat and drink! Rise up, O princes, and oil the shields.",
      "T": "Set the table! Spread the feast!\nEat and drink!\nPrinces, get up — oil the shields for battle!"
    },
    "6": {
      "L": "For thus the Lord said unto me, Go, post a watchman; let him declare what he seeth.",
      "M": "For this is what the Lord said to me: 'Go, station a watchman; let him report what he sees.'",
      "T": "The Lord said to me: 'Go — station a watchman; let him report whatever he sees.'"
    },
    "7": {
      "L": "And he saw a troop of riders, horsemen in pairs, a caravan of donkeys, a caravan of camels; and he hearkened attentively with great heed.",
      "M": "The watchman saw a column of cavalry — riders in pairs, a caravan of donkeys, a caravan of camels — and he listened intently, with close attention.",
      "T": "The watchman spotted a column of riders — cavalry in pairs, a train of donkeys, a train of camels —\nand strained to hear with every ounce of attention."
    },
    "8": {
      "L": "And he cried out like a lion: My lord, I stand continually upon the watchtower in the daytime; and I am set at my guard post every night.",
      "M": "Then the lookout called out: 'My lord, I stand on the watchtower continually by day, and I keep my post every night.'",
      "T": "Then the lookout cried out like a lion:\n'My lord! I have stood at the watchtower all day long\nand kept my post through every night —'"
    },
    "9": {
      "L": "And behold, here cometh a troop of men, horsemen in pairs. And he answered and said, Fallen, fallen is Babylon! And all the carved images of her gods he hath shattered to the ground.",
      "M": "Here comes a column of men, horsemen in pairs! Then the watcher answered: 'Fallen, fallen is Babylon! All the carved images of her gods are shattered to the ground!'",
      "T": "'Look — here comes a column of men, horsemen riding in pairs!'\nThen came the answer:\n'Fallen! Fallen is Babylon!\nEvery image of her gods\nlies shattered on the ground!'"
    },
    "10": {
      "L": "O my threshing, the grain of my floor! What I have heard from the LORD of hosts, the God of Israel, I have declared unto you.",
      "M": "O my people, crushed and winnowed — what I have heard from the LORD of hosts, the God of Israel, I now declare to you.",
      "T": "O Israel — my threshed and winnowed people —\nwhat I have heard from Yahweh of hosts, the God of Israel,\nI now declare to you."
    },
    "11": {
      "L": "The burden of Dumah. He calleth to me out of Seir, Watchman, what of the night? Watchman, what of the night?",
      "M": "The oracle of Dumah. A voice calls to me from Seir: 'Watchman, what is left of the night? Watchman, what is left of the night?'",
      "T": "Oracle of Dumah.\nA voice calls to me out of Seir:\n'Watchman, how much of the night is gone?\nWatchman, how much of the night is gone?'"
    },
    "12": {
      "L": "The watchman said, The morning cometh, and also the night; if ye will inquire, inquire ye; return and come.",
      "M": "The watchman said, 'Morning is coming, but so is the night. If you would inquire, inquire; come back again.'",
      "T": "The watchman answers:\n'Morning is coming — but night comes after it.\nIf you want to ask, then ask —\nbut come back again.'"
    },
    "13": {
      "L": "The burden upon Arabia. In the thickets of Arabia shall ye lodge, O ye caravans of Dedanites.",
      "M": "The oracle concerning Arabia. You caravans of the Dedanites, take shelter in the thickets of Arabia.",
      "T": "Oracle concerning Arabia.\nO caravans of the Dedanites,\nseek shelter in the thickets of Arabia."
    },
    "14": {
      "L": "O inhabitants of the land of Tema, bring water to meet the thirsty; with your bread meet the fugitive.",
      "M": "Bring water to the thirsty, O people of Tema; go out with food to meet the fugitives.",
      "T": "O people of Tema, bring water to the fugitives;\ngo out to meet those who are fleeing — bring them bread."
    },
    "15": {
      "L": "For they have fled from the swords, from the drawn sword, and from the bent bow, and from the press of war.",
      "M": "For they have fled from the swords, from the drawn sword, from the bent bow, and from the fury of battle.",
      "T": "They are fleeing the sword — the drawn blade,\nthe bent bow, the full fury of war."
    },
    "16": {
      "L": "For thus the Lord said unto me, Within a year, according to the years of a hired labourer, all the glory of Kedar shall fail.",
      "M": "For this is what the Lord said to me: 'Within a year, reckoned as a hired worker counts a year, all the wealth of Kedar will come to nothing.'",
      "T": "The Lord told me: 'Within one year —\nmeasured precisely, the way a hired laborer counts his contract —\nall of Kedar's glory will be gone.'"
    },
    "17": {
      "L": "And the remainder of the archers, the mighty men of the sons of Kedar, shall be few; for the LORD, the God of Israel, hath spoken.",
      "M": "The remaining archers — the warriors of Kedar — will be greatly diminished, for the LORD, the God of Israel, has spoken.",
      "T": "The archers of Kedar — Kedar's warriors —\nwill dwindle to almost nothing.\nYahweh, the God of Israel, has declared it."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 19–21 written.')

if __name__ == '__main__':
    main()
