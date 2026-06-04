"""
MKT Ezekiel chapters 19–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-19-21.py

Translation decisions (carrying forward all conventions from mkt-ezekiel-13-15.py
and mkt-ezekiel-17-18.py):

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T for oracle introductions,
  recognition formula ("you will know that I am Yahweh"), and the divine-oath formula
  ("as I live"). Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Adonai-Yahweh): "Lord GOD" in L/M (small-caps GOD);
  "Lord Yahweh" in T. The combined form dominates Ezekiel's oracle style.

- H7307 (רוּחַ): In 21:7 "every spirit shall be feeble" = human inner resolve; "spirit"
  (lowercase) in all tiers. Consistent with earlier use of lowercase for human spirit.

- H5315 (נֶפֶשׁ): Does not appear prominently in these chapters.

- H1544 (גִּלּוּלִים / idols): Occurs extensively in ch. 20. "Idols" in all tiers; the
  contemptuous force of Ezekiel's characteristic dung-idol term is preserved by
  consistent use throughout. In 20:39 the "heart-idols" dimension is surfaced in T.

- H1285 (בְּרִית / covenant): 20:37 — "bond of the covenant." L/M: "bond of the covenant";
  T: "the binding covenant" to surface the formal, oath-structured character of the
  relationship. The shepherd-rod image of counting/inspecting the flock is preserved.

- H8441 (תּוֹעֵבָה / abomination): Recurs in ch. 20. "Abominations" in L/M; T may render
  "detestable practices" or "what defiles" depending on rhythm.

- H4604 (מָעַל / trespass/faithlessness): 20:27 — covenant unfaithfulness. L: "committed
  a trespass"; M/T: "faithlessness" or "committed faithlessness" to surface the relational-
  betrayal dimension.

- H6666 (צְדָקָה / righteousness): Not prominent in these chapters.

- H2617 (חֶסֶד): Absent from these chapters.

- H7965 (שָׁלוֹם): Absent from these chapters.

- H6664/H7307 (spirit/wind): 20:12, 20 — sabbaths as sign. Not the spirit/wind term here;
  "sabbaths" is the key covenant-sign term.

- Chapter 19 — A formal qinah (lamentation, קִינָה): Ezekiel identifies this as a lament
  (19:1, 19:14). The poem uses two extended metaphors: the lioness and her cubs (vv. 1–9,
  most likely Jehoahaz in v.4 and Jehoiachin in v.9), and the vine and its branch (vv. 10–14).
  The kinah meter (3:2 stress pattern) in Hebrew gives the poem a falling, grief-heavy
  cadence. L renders the two metaphors faithfully; T preserves the elegiac quality with
  line rhythm and brief, punchy clauses.
  Historical note: v.4 "taken to Egypt" = Jehoahaz (2 Kgs 23:33); v.9 "brought to the king
  of Babylon" = most likely Jehoiachin (2 Kgs 24:15) though the second lion's exact identity
  is disputed. The text presents a literary sequence, not strict chronology.

- Chapter 20 — Historical survey of rebellion, the longest single historical recital in
  Ezekiel. Structure: refusal to be consulted (vv. 1–4) → Egypt (vv. 5–9) → first
  wilderness generation (vv. 10–17) → second wilderness generation (vv. 18–26) → in
  the land (vv. 27–29) → present charge (vv. 30–31) → you-will-not-be-like-the-nations
  (v.32) → new wilderness confrontation (vv. 33–38) → holy mountain restoration (vv. 39–44)
  → south-forest oracle (vv. 45–49, which 21:1ff decodes as Jerusalem).

  v. 25 ("statutes that were not good, judgments by which they could not live"): This is
  one of the most theologically difficult verses in Ezekiel. The plain reading is judicial
  hardening — God giving over a persistently rebellious people to lethal practices (primarily
  child sacrifice, v.26) as a form of covenant curse. L/M render the clause literally; T
  identifies it as judicial abandonment: because they refused the life-giving way, God
  permitted them to have the death-dealing way.

  The recognition formula "and you shall know that I am the LORD/Yahweh" appears in
  20:38, 42, 44 within the restoration oracle — a striking use of the formula that
  usually marks judgment, here applied to grace.

- Chapter 21 — The sword oracle (Hebrew: חֶרֶב, the drawn sword). Three sections:
  (a) vv. 1–7: oracle against Jerusalem, sign-act of sighing;
  (b) vv. 8–17: the sword song, incantatory and rhythmic — T preserves the cadence
      and the sign-acts (smiting thigh, clapping hands);
  (c) vv. 18–27: Babylon at the crossroads — Nebuchadnezzar's divination between
      Rabbah and Jerusalem; the three methods (arrow-divination, teraphim, hepatoscopy)
      are preserved in L/M and explained in T;
  (d) vv. 28–32: oracle against Ammon.

  v. 25 ("profane wicked prince of Israel"): This is Zedekiah, the last Davidic king of
  Jerusalem, whose coronation oath to Babylon he broke (17:15–19).

  v. 27 ("until he comes whose right it is"): The triple הֲפָכָה (overturn) is the most
  formally dramatic repetition in Ezekiel. The clause "until he comes whose right it is"
  (עַד-בֹּא אֲשֶׁר-לוֹ הַמִּשְׁפָּט) echoes Genesis 49:10 (Shiloh, "until he comes to
  whom it belongs"). L/M render it literally, preserving the ambiguity; T surfaces the
  messianic waiting note explicitly.

- Aspect notes:
  - Ch. 19's verbs are predominantly perfect/past (the lament looks back on what has
    already been begun); the vine section (vv. 10–14) moves into prophetic perfect
    (future events described as complete).
  - Ch. 20's historical survey uses Hebrew past narrative throughout; the restoration
    promises in vv. 33–44 use the future.
  - Ch. 21's oracle uses a mix of prophetic future (the sword is coming) and divine
    declaration (I have commanded the sword). The triple "overturn" is imperative-
    declarative in Hebrew — God performing and commanding simultaneously.

- The "south forest" oracle (20:45–49) is treated as the final section of ch. 20
  in the Hebrew verse numbering used here (which follows the MT where these verses
  are 20:45–49, not 21:1–5 as in some English traditions). Ch. 21 begins at
  the sword-against-Jerusalem oracle.
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
  "19": {
    "1": {
      "L": "And you, raise up a lamentation for the princes of Israel.",
      "M": "Raise up a lament for the princes of Israel:",
      "T": "Lift your voice in a lament — a burial song — for the princes of Israel:"
    },
    "2": {
      "L": "And say: What was your mother? A lioness! Among lions she lay down; among young lions she reared her whelps.",
      "M": "Say: What was your mother? A lioness! She lay down among lions, she reared her cubs among young lions.",
      "T": "Sing it this way: What was your mother? A lioness. She made her home among lions — lay down with them, raised her young in their company."
    },
    "3": {
      "L": "And she brought up one of her whelps; he became a young lion, and he learned to catch prey; he devoured men.",
      "M": "She raised one of her cubs; he became a young lion, learned to catch prey, and devoured men.",
      "T": "She raised one cub. He grew into a young lion — learned the hunt, learned to take prey. He began to eat men."
    },
    "4": {
      "L": "And the nations heard of him; he was caught in their pit; and they brought him with hooks to the land of Egypt.",
      "M": "The nations heard about him; he was caught in their pit; they brought him in chains to the land of Egypt.",
      "T": "Word spread among the nations. They laid a trap and caught him in their pit. They brought him with chains to Egypt — the first great humiliation."
    },
    "5": {
      "L": "Now when she saw that her hope was lost, that her waiting had come to nothing, she took another of her whelps and made him a young lion.",
      "M": "When she saw that her hope was gone and her waiting had come to nothing, she took another of her cubs and raised him as a young lion.",
      "T": "She waited for the first cub to return. The waiting came to nothing. Her hope evaporated. So she turned to another cub and raised him in the same way."
    },
    "6": {
      "L": "He walked about among the lions; he became a young lion; he learned to catch prey; he devoured men.",
      "M": "He prowled among the lions; he became a young lion, learned to catch prey, and devoured men.",
      "T": "This cub too prowled among the great predators, grew into a young lion, learned the hunt, and devoured men."
    },
    "7": {
      "L": "And he destroyed their strongholds and laid waste their cities; and the land, with all that was in it, was appalled at the noise of his roaring.",
      "M": "He ravaged their strongholds and laid waste their cities; the land and all it contained was appalled at the sound of his roaring.",
      "T": "He shattered their fortresses. He devastated city after city. The land itself — everything living in it — fell silent, paralyzed by the terror of his roar."
    },
    "8": {
      "L": "Then the nations set against him from the surrounding regions and spread their net over him; he was taken in their pit.",
      "M": "Then the nations gathered against him from surrounding regions, spread their net over him, and he was caught in their pit.",
      "T": "But the nations coordinated. They came at him from every direction — surrounding provinces closing in — spread their net over him. He fell into their pit."
    },
    "9": {
      "L": "And they put him in a cage with hooks and brought him to the king of Babylon; they brought him into a stronghold, so that his voice should no more be heard on the mountains of Israel.",
      "M": "They put him in a cage in chains and brought him to the king of Babylon; they brought him into a fortress, so that his voice would no longer be heard on the mountains of Israel.",
      "T": "Into a cage. In chains. Brought before the king of Babylon. Locked away in a fortress. The roar that had shaken the mountains of Israel — silenced. He would never be heard in his homeland again."
    },
    "10": {
      "L": "Your mother was like a vine in your blood, planted by the waters; she was fruitful and full of branches because of many waters.",
      "M": "Your mother was like a vine transplanted beside the waters — fruitful and full of branches because of abundant water.",
      "T": "Now the image shifts: your mother — the dynasty, the nation — was like a vine planted by water's edge. Rich soil, abundant water. She thrived. Branch after branch, fruit abundant."
    },
    "11": {
      "L": "She had strong rods for the scepters of those who rule; her stature was exalted among the thick branches, and she appeared in her height amid the multitude of her branches.",
      "M": "She had strong branches that served as rulers' scepters; her stature towered among the thick branches, her height visible above all the rest.",
      "T": "Her branches were strong enough for scepters — they became the staffs of rulers. She rose above the surrounding trees. Visible, established, exalted in the thicket. A dynasty in full leaf."
    },
    "12": {
      "L": "But she was plucked up in fury, cast down to the ground; the east wind dried up her fruit; her strong rods were broken and dried up; fire consumed them.",
      "M": "But she was torn up in fury and thrown to the ground; the east wind dried up her fruit; her strong branches broke and withered; fire consumed them.",
      "T": "Then wrath arrived. She was torn up by the roots — thrown down. The east wind blew in from the desert, dry and pitiless, drying up her fruit. Her strong branches — the scepters, the rulers — were snapped and withered. Fire consumed what remained."
    },
    "13": {
      "L": "And now she is planted in the wilderness, in a dry and thirsty ground.",
      "M": "Now she is planted in the wilderness — in a dry and thirsty land.",
      "T": "Now she is replanted — but in the wilderness. Dry ground. Thirsty ground. Exile. No living water, no abundance, no height."
    },
    "14": {
      "L": "Fire has gone out from a rod of her branches and has devoured her fruit, so that she has no strong rod, no scepter to rule. This is a lamentation and shall serve as a lamentation.",
      "M": "Fire has spread from one of her own branches and devoured her fruit — she has no strong branch left, no scepter to rule with. This is a lament, and it shall be used as a lament.",
      "T": "The fire came from within — from one of her own branches, one of her own rulers, ignited and turned against her. Her fruit consumed. No strong branch remains. No scepter. No one to rule. The dynasty is ended. This is a burial song. It was written to be sung at a funeral — and the funeral has come."
    }
  },
  "20": {
    "1": {
      "L": "And it came to pass in the seventh year, in the fifth month, on the tenth day of the month, that certain of the elders of Israel came to inquire of the LORD and sat before me.",
      "M": "In the seventh year, in the fifth month, on the tenth day of the month, some of the elders of Israel came to inquire of the LORD and sat before me.",
      "T": "The seventh year of exile — the fifth month, the tenth day. Some of the elders of Israel came and sat before me, seeking a word from Yahweh. They arrived with a question. They would not get the answer they expected."
    },
    "2": {
      "L": "And the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "3": {
      "L": "Son of man, speak to the elders of Israel and say to them: Thus says the Lord GOD: Have you come to inquire of me? As I live, declares the Lord GOD, I will not be inquired of by you.",
      "M": "Son of man, speak to the elders of Israel and say: Thus says the Lord GOD: Have you come to inquire of me? As I live, declares the Lord GOD, I will not be inquired of by you.",
      "T": "Son of man, address these elders directly. The Lord Yahweh says: So you have come to inquire of me? By my own life — the Lord Yahweh swears it — I will not be consulted by you. Not now. Not while you are what you are."
    },
    "4": {
      "L": "Will you judge them, son of man, will you judge them? Make known to them the abominations of their fathers.",
      "M": "Will you pass judgment on them, son of man — will you judge them? Make known to them the abominations of their fathers.",
      "T": "Will you confront them, son of man? Will you really set the charge before them? Then do it. Make them face the abominations of their ancestors — not as distant history, but as the pattern they have inherited and continued."
    },
    "5": {
      "L": "And say to them: Thus says the Lord GOD: On the day when I chose Israel and lifted my hand to the offspring of the house of Jacob, and made myself known to them in the land of Egypt — when I lifted my hand to them, saying: I am the LORD your God —",
      "M": "Say to them: Thus says the Lord GOD: On the day I chose Israel and swore to the offspring of the house of Jacob, making myself known to them in Egypt — when I swore to them: I am the LORD your God —",
      "T": "Say it from the Lord Yahweh: I will tell you when this began. On the day I chose Israel — lifted my hand in covenant oath to the offspring of Jacob's house — and revealed myself to them in Egypt, swearing: I am Yahweh your God —"
    },
    "6": {
      "L": "On that day I lifted my hand to them, to bring them out of the land of Egypt into a land I had selected for them, flowing with milk and honey — the glory of all lands —",
      "M": "On that day I swore to bring them out of Egypt into a land I had chosen for them — flowing with milk and honey, the glory of all lands —",
      "T": "On that day I pledged to bring them out of Egypt into a land I had already scouted for them — flowing with milk and honey, the most magnificent piece of earth in the world —"
    },
    "7": {
      "L": "And I said to them: Each of you, cast away the abominations of his eyes, and do not defile yourselves with the idols of Egypt; I am the LORD your God.",
      "M": "I said to them: Each of you must cast away the detestable things his eyes love, and do not defile yourselves with Egypt's idols; I am the LORD your God.",
      "T": "And with that pledge I gave them a command: Every one of you — throw away the abominations you have been looking at with desire. Do not make yourselves unclean with Egypt's idols. I am Yahweh your God."
    },
    "8": {
      "L": "But they rebelled against me and would not listen to me; not a man cast away the abominations of his eyes, nor did they forsake the idols of Egypt. Then I said: I will pour out my fury upon them, to spend my anger against them in the midst of the land of Egypt.",
      "M": "But they rebelled against me and would not listen; not one cast away the detestable things of his eyes or forsook the idols of Egypt. Then I said: I will pour out my fury on them, spending my anger against them in the midst of Egypt.",
      "T": "But they rebelled. They would not listen. Not one man threw away the detestable things he had been drawn to. Not one forsook Egypt's idols. And I said: I will pour out my fury on them — right there in Egypt, in the very land of their bondage, I will spend my anger against them."
    },
    "9": {
      "L": "But I acted for my name's sake, that it should not be profaned in the sight of the nations among whom they were — in whose sight I had made myself known to them by bringing them out of Egypt.",
      "M": "But I acted for the sake of my name — that it should not be profaned before the nations among whom they lived, in whose sight I had revealed myself by bringing them out of Egypt.",
      "T": "But I stayed my hand — not for their sake, but for my name's sake. I had revealed myself to them in front of the watching nations. To have destroyed them in Egypt would have dishonored the name I had publicly sworn to redeem them. I brought them out — for my name, not for their worthiness."
    },
    "10": {
      "L": "So I brought them out of the land of Egypt and led them into the wilderness.",
      "M": "So I brought them out of Egypt and led them into the wilderness.",
      "T": "So I led them out of Egypt and into the wilderness."
    },
    "11": {
      "L": "And I gave them my statutes and showed them my judgments, which if a man does, he shall live by them.",
      "M": "I gave them my statutes and made known my judgments — which, if a person does them, he will live by them.",
      "T": "In the wilderness I gave them my statutes and made my judgments known to them — the way of life: if a person does these things, he will live by them. Life was on offer."
    },
    "12": {
      "L": "Moreover I gave them my sabbaths, to be a sign between me and them, that they might know that I am the LORD who sanctifies them.",
      "M": "I also gave them my sabbaths as a sign between me and them — so they would know that I am the LORD who sanctifies them.",
      "T": "More than that: I gave them my sabbaths. Not merely as a rest day — but as a covenant sign between us, a recurring weekly declaration that I am Yahweh who sets them apart as holy. The sabbath was the embodied symbol of the relationship."
    },
    "13": {
      "L": "But the house of Israel rebelled against me in the wilderness; they did not walk in my statutes and they despised my judgments — which if a man does, he shall live by them — and my sabbaths they greatly defiled. Then I said I would pour out my fury upon them in the wilderness, to consume them.",
      "M": "But the house of Israel rebelled against me in the wilderness; they did not walk in my statutes or keep my judgments — by which a person who does them will live — and they grossly profaned my sabbaths. Then I said I would pour out my wrath on them in the wilderness and consume them.",
      "T": "But Israel rebelled in the wilderness. They did not walk in my statutes. They despised my judgments — the very path of life. And my sabbaths, the covenant sign itself, they profaned openly. I said: I will pour out my fury on them in the wilderness. I will consume them there."
    },
    "14": {
      "L": "But I acted for my name's sake, that it should not be profaned before the nations, in whose sight I had brought them out.",
      "M": "But I acted for the sake of my name — that it not be profaned before the nations in whose sight I had brought them out.",
      "T": "And again: I restrained myself. For my name's sake. The nations who had watched the Exodus were still watching. I had staked my name on Israel's redemption. To consume them in the wilderness would have profaned that public commitment."
    },
    "15": {
      "L": "Yet also I lifted my hand to them in the wilderness, swearing that I would not bring them into the land I had given them — flowing with milk and honey, the glory of all lands —",
      "M": "But I also swore to them in the wilderness that I would not bring them into the land I had given them — flowing with milk and honey, the most glorious of all lands —",
      "T": "But even as I spared them, I swore an oath — in the wilderness itself — that I would not bring that generation into the promised land. The very generation redeemed from Egypt would not enter the inheritance. Flowing with milk and honey though it was — the most glorious land on earth — they would not see it."
    },
    "16": {
      "L": "Because they despised my judgments and did not walk in my statutes and profaned my sabbaths — for their heart went after their idols.",
      "M": "Because they despised my judgments, did not walk in my statutes, and profaned my sabbaths — their hearts were set on their idols.",
      "T": "The reason: they despised my judgments. They abandoned my statutes. They profaned my sabbaths. The root cause: their hearts had already gone to their idols. The outward rebellion was only the surface of an inward abandonment."
    },
    "17": {
      "L": "Nevertheless my eye spared them from destroying them; I did not make an end of them in the wilderness.",
      "M": "Nevertheless my eye had pity on them; I did not destroy them or make an end of them in the wilderness.",
      "T": "And yet my eye showed them pity. Something in my own mercy stayed the hand of my justice. I did not wipe them out in the wilderness. I let them finish their days."
    },
    "18": {
      "L": "But I said to their children in the wilderness: Do not walk in the statutes of your fathers, nor observe their judgments, nor defile yourselves with their idols.",
      "M": "And I said to their children in the wilderness: Do not follow your fathers' statutes, do not observe their judgments, and do not defile yourselves with their idols.",
      "T": "I turned to the next generation — their children, still in the wilderness. I said: Do not repeat your fathers. Do not follow their path. Do not observe the judgments they lived by. Do not defile yourselves with their idols. You have seen what their choices cost them. Choose differently."
    },
    "19": {
      "L": "I am the LORD your God; walk in my statutes, keep my judgments, and do them.",
      "M": "I am the LORD your God; walk in my statutes, keep my judgments, and carry them out.",
      "T": "I am Yahweh your God. Walk in my statutes. Keep my judgments. Do them. Not know them — do them."
    },
    "20": {
      "L": "And keep my sabbaths holy; they shall be a sign between me and you, so that you may know that I am the LORD your God.",
      "M": "Keep my sabbaths holy; they will be a sign between me and you, so you will know that I am the LORD your God.",
      "T": "And honor my sabbaths. Keep them holy. They are the sign between us — the recurring covenant marker that makes visible what we are to each other. In the sabbath you will know that I am Yahweh your God."
    },
    "21": {
      "L": "But the children rebelled against me; they did not walk in my statutes or keep my judgments to do them — which if a man does, he shall live by them — and they profaned my sabbaths. Then I said I would pour out my fury upon them, to spend my anger against them in the wilderness.",
      "M": "But the children rebelled against me; they did not walk in my statutes or carry out my judgments — by which a person will live — and they profaned my sabbaths. Then I said I would pour out my fury and spend my anger against them in the wilderness.",
      "T": "But the second generation did the same thing. They too rebelled. They too refused to walk in my statutes. They too despised my judgments — the path of life. They too profaned my sabbaths. Again I said: I will pour out my fury, spend my anger — in the wilderness, against them. The pattern repeated without interruption."
    },
    "22": {
      "L": "But I withdrew my hand and acted for my name's sake, so that it should not be profaned in the sight of the nations in whose sight I had brought them forth.",
      "M": "But I withdrew my hand and acted for the sake of my name, so it would not be profaned before the nations in whose sight I had brought them out.",
      "T": "And again — I pulled back. For my name. Again. The nations who watched the Exodus still watched. My name was staked to Israel's survival. I withheld the destruction. Not for their merit — for the integrity of my own public commitment."
    },
    "23": {
      "L": "I also lifted my hand to them in the wilderness, swearing that I would scatter them among the nations and disperse them through the countries —",
      "M": "But I also swore to them in the wilderness that I would scatter them among the nations and disperse them through foreign lands —",
      "T": "Yet alongside the mercy, I swore another oath — also in the wilderness. That I would scatter them among the nations. Disperse them through foreign lands. The exile we are living now is not an accident; it was sworn in the wilderness."
    },
    "24": {
      "L": "Because they had not carried out my judgments, had despised my statutes, had profaned my sabbaths, and their eyes went after their fathers' idols.",
      "M": "Because they had not carried out my judgments, had despised my statutes, profaned my sabbaths, and set their eyes on their fathers' idols.",
      "T": "The reason for that oath of exile: they refused to carry out my judgments. They despised my statutes. They profaned my sabbaths. Their eyes went after the same idols their fathers had chased. Generation after generation — the same idolatry, the same rebellion, the same consequence."
    },
    "25": {
      "L": "And I also gave them statutes that were not good, and judgments by which they could not live —",
      "M": "And I also gave them statutes that were not good and judgments by which they could not live —",
      "T": "And so I gave them over — I gave them statutes that were not good. Judgments by which they could not live. A judicial abandonment: because they refused my life-giving way, I permitted the way of death to govern them. What you persist in choosing, I will let you have."
    },
    "26": {
      "L": "And I defiled them through their own gifts, in that they caused all who open the womb to pass through the fire, so that I might make them desolate, in order that they might know that I am the LORD.",
      "M": "I made them unclean through their own offerings — in that they caused every firstborn to pass through the fire — so that I might make them desolate, that they might know that I am the LORD.",
      "T": "I rendered them unclean through their own cultic acts — they were passing their firstborn children through the fire to their idols. I permitted this horror as part of the judicial abandonment. The desolation that followed was the appointed consequence. They would know, through devastation, that I am Yahweh."
    },
    "27": {
      "L": "Therefore, son of man, speak to the house of Israel and say to them: Thus says the Lord GOD: In this your fathers blasphemed me, in that they committed faithlessness against me.",
      "M": "Therefore, son of man, speak to the house of Israel and say: Thus says the Lord GOD: In this your fathers blasphemed me — they committed faithlessness against me.",
      "T": "So speak to the house of Israel, son of man. The Lord Yahweh says: Even after all of this — in the land itself — your fathers continued to blaspheme me. They committed sustained covenant faithlessness."
    },
    "28": {
      "L": "For when I brought them into the land which I had lifted my hand to give to them, wherever they saw a high hill or a leafy tree, they offered their sacrifices there — they presented their provoking offerings there, set their soothing aromas there, and poured out their drink offerings there.",
      "M": "When I brought them into the land I had sworn to give them, they saw every high hill and leafy tree and offered their sacrifices there — presenting their provoking offerings, producing their pleasing aromas, and pouring out their drink offerings.",
      "T": "I brought them into the promised land — the very land I had sworn in the wilderness to give them. And what did they do the moment they saw it? Every high hill caught their eye. Every leafy tree. And there they went: sacrifices, provocation-offerings, soothing aromas — the whole worship apparatus diverted to the high places. The land I gave them became the platform for their idolatry."
    },
    "29": {
      "L": "Then I said to them: What is this high place to which you go? And its name has been called Bamah to this day.",
      "M": "Then I said to them: What is this high place where you go? And its name has been called Bamah to this day.",
      "T": "And I asked them: What is this high place you are going to? The ironic answer lives on in the name itself — Bamah. High place. Still called that to this day: a monument to their stubborn idolatry."
    },
    "30": {
      "L": "Therefore say to the house of Israel: Thus says the Lord GOD: Are you defiling yourselves after the manner of your fathers? And do you go whoring after their abominations?",
      "M": "Therefore say to the house of Israel: Thus says the Lord GOD: Are you making yourselves unclean in the same way as your fathers? Do you go whoring after their detestable things?",
      "T": "So say to present-day Israel — the Lord Yahweh asks it directly: Are you doing what your fathers did? Defiling yourselves the same way? Chasing the same abominations with the same idolatrous desire? The question is rhetorical. The answer is obvious."
    },
    "31": {
      "L": "For when you present your gifts, when you make your sons pass through the fire, you are defiling yourselves with all your idols to this day. And shall I be inquired of by you, O house of Israel? As I live, declares the Lord GOD, I will not be inquired of by you.",
      "M": "When you present your gifts and make your sons pass through the fire, you defile yourselves with all your idols to this day — and you expect me to be consulted by you, O house of Israel? As I live, declares the Lord GOD, I will not be inquired of by you.",
      "T": "At this very moment, as these elders sit before me — you are still presenting these gifts. Still passing your sons through the fire. Still defiling yourselves with idols. Today. And you came to ask me something? As I live — the Lord Yahweh swears it — I will not be consulted by you. Not like this."
    },
    "32": {
      "L": "And that which comes into your mind shall not come to pass, when you say: We will be like the nations, like the families of the lands, serving wood and stone.",
      "M": "What you are thinking shall not happen — what you say: We will be like the nations, like the families of the countries, worshiping wood and stone.",
      "T": "And this thought that is forming in your minds — this fantasy — it will not happen. The idea: Let us just be like every other nation. Fit in, worship what everyone worships — wood and stone — and drop the burden of being different. That will not happen. You are not free to un-choose what I chose you to be."
    },
    "33": {
      "L": "As I live, declares the Lord GOD, surely with a mighty hand and with a stretched-out arm and with fury poured out I will reign over you.",
      "M": "As I live, declares the Lord GOD, I will surely reign over you with a mighty hand, an outstretched arm, and outpoured fury.",
      "T": "As I live — the Lord Yahweh swears it — I will rule over you with a strong hand, a stretched-out arm, and outpoured fury. If you will not receive my kingship in love, you will receive it in judgment. But you will not escape it."
    },
    "34": {
      "L": "And I will bring you out from the peoples and gather you from the countries where you have been scattered — with a mighty hand and with a stretched-out arm and with fury poured out.",
      "M": "I will bring you out from the peoples and gather you from the countries where you have been scattered — with a mighty hand and an outstretched arm and outpoured fury.",
      "T": "I will bring you out. Out of all the nations where you have been scattered. Out from every land where exile has taken you. With a strong hand, with an outstretched arm, with outpoured fury — the way I brought your ancestors out of Egypt. A new Exodus. An unwilling redemption, if that is what it takes."
    },
    "35": {
      "L": "And I will bring you into the wilderness of the peoples, and there I will enter into judgment with you face to face.",
      "M": "And I will bring you into the wilderness of the peoples, and there I will contend with you face to face.",
      "T": "I will bring you into the wilderness — not the desert of Sinai this time, but the wilderness of the nations, the place between the old home and the new. And there I will confront you face to face. No intermediaries. The reckoning will be direct."
    },
    "36": {
      "L": "As I entered into judgment with your fathers in the wilderness of the land of Egypt, so I will enter into judgment with you, declares the Lord GOD.",
      "M": "As I contended with your fathers in the wilderness of Egypt, so I will contend with you, declares the Lord GOD.",
      "T": "I did this before — with your ancestors in the Egyptian wilderness — and that confrontation cost the entire first generation the promised land. The Lord Yahweh says: I will do it again with you."
    },
    "37": {
      "L": "And I will cause you to pass under the rod, and I will bring you into the bond of the covenant.",
      "M": "I will cause you to pass under the shepherd's rod, and I will bring you into the bond of the covenant.",
      "T": "You will pass under my shepherd's rod — each one counted, inspected, claimed or rejected. And I will bring you into the binding covenant. Covenant is not only grace; it is also obligation. Every one of you will be examined."
    },
    "38": {
      "L": "And I will purge out from among you the rebels and those who transgress against me; I will bring them out from the land where they sojourn, but they shall not enter the land of Israel — and you will know that I am the LORD.",
      "M": "I will purge out from among you the rebels and those who sin against me; I will bring them out of the land where they are living, but they will not enter the land of Israel — and you will know that I am the LORD.",
      "T": "The rebels — those who persist in transgression against me — will be purged. I will bring them out from wherever they are living in exile. But they will not enter the land of Israel. The wilderness will be their end. And then you will know — the survivors who passed under the rod — that I am Yahweh."
    },
    "39": {
      "L": "As for you, O house of Israel, thus says the Lord GOD: Go, serve each one his idols, and hereafter also, if you will not listen to me — but defile my holy name no more with your gifts and your idols.",
      "M": "As for you, O house of Israel, thus says the Lord GOD: Go, serve your idols — every one of you — but afterward, if you will not listen to me, defile my holy name no more with your gifts and idols.",
      "T": "The Lord Yahweh says to you, Israel: If that is your choice — go, serve your idols, every one of you. Make your allegiance explicit. But then stop dragging my name into it. Stop defiling my holy name with your idolatrous gifts while pretending to inquire of me. Be openly what you are, or come to me genuinely. I will not receive this double allegiance."
    },
    "40": {
      "L": "For on my holy mountain, on the high mountain of Israel, declares the Lord GOD, there all the house of Israel, all of them in the land, shall serve me; there I will accept them, and there I will require your contributions and the firstfruits of your gifts, with all your holy things.",
      "M": "For on my holy mountain — the high mountain of Israel, declares the Lord GOD — there all the house of Israel will serve me in the land; there I will accept them; and there I will require your offerings and the firstfruits of your gifts, with all your holy things.",
      "T": "But the future I am building toward: on my holy mountain — Zion, the mountain of Israel's height — there the whole house of Israel will gather to serve me. In the land. All of them. There I will accept them. There the offerings will be right: given freely, received gladly, the firstfruits of everything holy. Not the coerced tribute of rebels, but the grateful worship of a restored people."
    },
    "41": {
      "L": "I will accept you with a pleasing aroma when I bring you out from the peoples and gather you from the countries where you have been scattered — and I will show my holiness through you before the nations.",
      "M": "I will accept you as a pleasing aroma when I bring you out from the peoples and gather you from the countries where you have been scattered — and I will show my holiness through you before the nations.",
      "T": "When I bring you out — out of every nation, gathered from every land of exile — I will receive you like a fragrant offering. Pleasant. Accepted. And in that gathering, in your restoration, I will display my holiness before the watching nations. My name, dishonored by your exile, will be vindicated by your return."
    },
    "42": {
      "L": "And you will know that I am the LORD when I bring you into the land of Israel — the country for which I lifted my hand to give to your fathers.",
      "M": "You will know that I am the LORD when I bring you into the land of Israel — the country I swore to give to your fathers.",
      "T": "And in that moment — when I bring you into the land of Israel, into the very land I swore in oath to give your ancestors — you will know. Finally know, with all ambiguity gone: I am Yahweh."
    },
    "43": {
      "L": "And there you shall remember your ways and all your doings by which you defiled yourselves; and you shall loathe yourselves in your own sight for all the evils you have committed.",
      "M": "There you will remember your ways and all your deeds by which you defiled yourselves; and you will loathe yourselves for all the evils you have done.",
      "T": "And in the land, the memory will come. You will remember everything — how you lived, what you chose, the ways you made yourselves unclean. And the remembering will produce self-loathing. Not guilt imposed from outside — genuine revulsion at what you were, what you did. This is the repentance that comes after restoration, not before. The grace precedes the grief."
    },
    "44": {
      "L": "And you will know that I am the LORD when I have dealt with you for my name's sake and not according to your wicked ways or your corrupt deeds, O house of Israel, declares the Lord GOD.",
      "M": "You will know that I am the LORD when I have dealt with you for my name's sake and not according to your evil ways or corrupt deeds, O house of Israel, declares the Lord GOD.",
      "T": "And you will know that I am Yahweh — precisely because I will have acted for my name's sake, not according to what you deserved. Your ways were wicked. Your deeds were corrupt. But my faithfulness to my own name exceeded your faithlessness to me. The Lord Yahweh has declared it."
    },
    "45": {
      "L": "Moreover the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me again:"
    },
    "46": {
      "L": "Son of man, set your face toward the south and speak toward the south, and prophesy against the forest of the Negev.",
      "M": "Son of man, set your face toward the south, speak toward the south, and prophesy against the forest of the Negev.",
      "T": "Son of man — turn south. Speak southward. Your prophetic word points toward the forest of the Negev."
    },
    "47": {
      "L": "And say to the southern forest: Hear the word of the LORD! Thus says the Lord GOD: I will kindle a fire in you and it shall devour every green tree and every dry tree; the blazing flame shall not be quenched, and every face from south to north shall be scorched by it.",
      "M": "Say to the southern forest: Hear the word of the LORD! Thus says the Lord GOD: I will kindle a fire in you that will consume every green tree and every dry tree; the blazing flame will not be quenched, and every face from south to north will be scorched.",
      "T": "Say to the southern forest: Hear Yahweh's word! The Lord Yahweh says: I am going to light a fire in you that will take everything — green tree and dry tree alike. The flame will not be quenched. Every face, from the southernmost point to the north, will be burned in it. Nothing unscathed."
    },
    "48": {
      "L": "And all flesh shall see that I the LORD have kindled it; it shall not be quenched.",
      "M": "All flesh will see that I the LORD have lit this fire; it will not be quenched.",
      "T": "Every living person will see it — and know that I, Yahweh, lit this fire. No one will put it out."
    },
    "49": {
      "L": "Then I said: Ah, Lord GOD! They are saying of me: Is he not just speaking in parables?",
      "M": "Then I said: Ah, Lord GOD! They are saying of me: Is he not just speaking in parables?",
      "T": "And I said: Ah, Lord Yahweh — they are saying I speak in riddles. Everything I say they take as metaphor, allegory, dark speech. They do not believe the fire is real."
    }
  },
  "21": {
    "1": {
      "L": "And the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, set your face toward Jerusalem, speak against the holy places, and prophesy against the land of Israel.",
      "M": "Son of man, set your face toward Jerusalem, speak against the holy places, and prophesy against the land of Israel.",
      "T": "Son of man — the riddle of the forest is now decoded. Turn your face toward Jerusalem. Speak against the holy places themselves. Prophesy against the land of Israel."
    },
    "3": {
      "L": "And say to the land of Israel: Thus says the LORD: I am against you and will draw my sword from its sheath and cut off from you both the righteous and the wicked.",
      "M": "Say to the land of Israel: Thus says the LORD: I am against you; I will draw my sword from its sheath and cut off from you both the righteous and the wicked.",
      "T": "Say to the land of Israel: The LORD says — I am set against you. My sword is coming out of its sheath. Both righteous and wicked will be cut off. The sword of national judgment does not distinguish the way individual discipline does. The covenant community falls as a whole."
    },
    "4": {
      "L": "Since I will cut off from you both the righteous and the wicked, therefore my sword shall go forth from its sheath against all flesh from south to north.",
      "M": "Since I will cut off both the righteous and the wicked from you, my sword will go out from its sheath against all flesh from south to north.",
      "T": "Because both righteous and wicked are cut off — the sword sweeps the whole nation — my sword goes out from south to north. No quarter of the land escapes. This is not surgical judgment; it is total."
    },
    "5": {
      "L": "So that all flesh may know that I the LORD have drawn my sword from its sheath; it shall not return.",
      "M": "So that all flesh may know that I the LORD have drawn my sword from its sheath; it will not return.",
      "T": "The purpose of the totality: every living person must know that I, Yahweh, have drawn this sword. And this sword will not be sheathed again until the work is done."
    },
    "6": {
      "L": "Therefore sigh, son of man, with the breaking of your loins; and with bitterness sigh before their eyes.",
      "M": "Therefore sigh, son of man — sigh with a broken back, with bitterness, before their eyes.",
      "T": "Therefore, son of man — sigh. Not quietly, not inwardly. Sigh visibly, with your whole body — the way a person sighs from something physically overwhelming, something that breaks you. Sigh bitterly, in front of them. Let the grief be visible before they ask why."
    },
    "7": {
      "L": "And it shall be, when they ask you: Why are you sighing? you shall say: Because of the news that is coming. When it comes, every heart will melt, all hands will go limp, every spirit will faint, and every knee will run like water. Behold, it is coming and it will come to pass, declares the Lord GOD.",
      "M": "When they ask you: Why are you sighing? — say: Because of the news that is coming. When it arrives, every heart will melt, every hand will go limp, every spirit will faint, and every knee will turn to water. It is coming — it will happen, declares the Lord GOD.",
      "T": "When they see you and ask why — and they will ask — say: Because of the news. The news that is on its way. When it arrives: hearts will melt. Hands will hang useless. Every inner resolve will collapse. Every knee will buckle and run like water. It is coming. It will come to pass. The Lord Yahweh has declared it."
    },
    "8": {
      "L": "Again the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me again:",
      "T": "Yahweh's word came to me again:"
    },
    "9": {
      "L": "Son of man, prophesy and say: Thus says the LORD. Say: A sword, a sword is sharpened, and also polished.",
      "M": "Son of man, prophesy and say: Thus says the LORD: A sword, a sword — sharpened and polished.",
      "T": "Son of man, prophesy. Speak from the LORD. Say: A sword. A sword is being sharpened. A sword is being polished to brightness."
    },
    "10": {
      "L": "It is sharpened to make a great slaughter; it is polished to flash like lightning. Should we then make mirth? The rod of my son despises every tree.",
      "M": "Sharpened for a great slaughter, polished to flash like lightning — shall we rejoice? It scorns the rod of my son, along with every other scepter.",
      "T": "Sharpened for maximum slaughter. Polished to a blinding flash. Is there room for celebration when this sword is being readied? It scorns every scepter — including the rod of my own son, the Davidic dynasty. It overrules everything."
    },
    "11": {
      "L": "And he has given it to be polished, that it may be handled; this sword is sharpened and polished to be given into the hand of the slayer.",
      "M": "He has given the sword to be polished so it can be wielded; it has been sharpened and polished to be placed in the slayer's hand.",
      "T": "It has been commissioned for polishing so it can be gripped and used. The sharpening, the polishing — all preparation to place it in the slayer's hand. Every preparation has been made. The weapon is ready."
    },
    "12": {
      "L": "Cry out and wail, son of man, for it comes against my people, against all the princes of Israel — sword-terrors are upon my people. Therefore strike your thigh.",
      "M": "Cry out and wail, son of man, for it comes against my people — against all the princes of Israel. Terrors because of the sword are upon my people. Therefore strike your thigh.",
      "T": "Cry out, son of man. Wail. This sword is coming for my people — for all the princes of Israel. It comes as terror. Strike your thigh — the sign-act of grief and horror, the ancient gesture for devastating news. There is nothing in this that calls for silence."
    },
    "13": {
      "L": "Because testing is coming — and what if the sword despises even the scepter? It will be no more, declares the Lord GOD.",
      "M": "For testing has come — and what if the sword despises even the scepter? It will be no more, declares the Lord GOD.",
      "T": "This is a testing — and what if the sword overturns even the royal scepter, the thing that was supposed to represent supreme power? If the dynasty itself cannot withstand the sword, the scepter of Judah is at an end. The Lord Yahweh has said so."
    },
    "14": {
      "L": "You therefore, son of man, prophesy and clap your hands together; let the sword strike twice, three times — the sword for those slain, the sword of great slaughter that enters their innermost chambers.",
      "M": "Therefore, son of man, prophesy and clap your hands together; let the sword strike twice, three times — the sword of the slain, the sword of great slaughter entering their innermost chambers.",
      "T": "So prophesy, son of man — and clap your hands together in the sign of divine wrath. The sword falls twice, three times, multiplying. The slaughter is for the great men — the leaders, the princes — and it follows them into the innermost rooms of their houses. There is no sanctuary."
    },
    "15": {
      "L": "I have placed the threatening sword against all their gates, so that hearts may melt and ruins multiply — it flashes bright, prepared for slaughter.",
      "M": "I have placed the sword against all their gates so that hearts melt and destruction multiplies — it flashes bright, prepared for slaughter.",
      "T": "I have stationed the gleaming sword against every gate of every city. Hearts will melt. Ruins will multiply. The sword gleams, wrapped for the moment of use. Everything is in position."
    },
    "16": {
      "L": "Go to the right or go to the left — whichever way your face is set.",
      "M": "Slash to the right or to the left — whichever direction you face.",
      "T": "Sword — strike right or left. Any direction you face, go that way. The freedom of the sword in God's hand: unconstrained, striking wherever it turns."
    },
    "17": {
      "L": "I also will clap my hands together and I will let my fury rest; I the LORD have spoken.",
      "M": "I too will clap my hands together and satisfy my fury; I the LORD have spoken.",
      "T": "I too will clap my hands — the divine echo of the prophet's sign-act. My fury will be spent. The blow will land, the anger will be satisfied. I, Yahweh, have spoken this."
    },
    "18": {
      "L": "The word of the LORD came to me again, saying:",
      "M": "The word of the LORD came to me again:",
      "T": "Yahweh's word came to me again:"
    },
    "19": {
      "L": "And you, son of man, mark out two roads for the sword of the king of Babylon to come; both shall go out from one land. And make a signpost; make it at the head of the road to the city.",
      "M": "And you, son of man, mark out two roads for the sword of the king of Babylon to travel — both going out from one land. Make a signpost at the fork in the road to the city.",
      "T": "Son of man, draw a map. Two roads, both starting from the same place, both routes the sword of Babylon's king could take. At the fork in the road, mark the signpost — the decision point where the roads divide and the direction of judgment will be chosen."
    },
    "20": {
      "L": "Mark one road for the sword to come to Rabbah of the Ammonites, and one for Judah — to fortified Jerusalem.",
      "M": "Mark one road for the sword to come to Rabbah of the Ammonites, and one for Judah — to fortified Jerusalem.",
      "T": "One road leads to Rabbah — capital of the Ammonites. The other leads to Jerusalem, fortified Jerusalem. These are Babylon's two options. Both cities live under the pressure of this decision."
    },
    "21": {
      "L": "For the king of Babylon stands at the parting of the way, at the head of the two roads, to use divination; he shakes the arrows, he consults the household idols, he examines the liver.",
      "M": "For the king of Babylon stands at the fork in the road, at the head of the two ways, to use divination — shaking arrows, consulting household idols, examining the liver.",
      "T": "The king of Babylon stands at the crossroads — literally, at the head of the fork — and uses divination to choose his direction. He shakes the arrows. He consults his household idols, his teraphim. He reads the patterns in a sacrificial liver. Three divination methods, all at once. He wants certainty before he moves."
    },
    "22": {
      "L": "Into his right hand came the divination for Jerusalem — to set battering rams, to call for a massacre, to raise a battle shout, to set battering rams against the gates, to build a siege ramp, to erect a siege wall.",
      "M": "The divination fell to his right hand — Jerusalem: to set up battering rams, to command a massacre, to raise the battle shout, to set rams against the gates, to build a siege ramp, to erect a siege wall.",
      "T": "The divination pointed his right hand toward Jerusalem. And the right-hand lot means: deploy the battering rams. Shout the battle cry. Build the siege ramp. Erect the siege wall. Jerusalem's name came up in Babylon's divination. The city will be besieged."
    },
    "23": {
      "L": "But to them it will seem as a false divination — they who have sworn solemn oaths before him. But he will bring their iniquity to remembrance, so that they may be seized.",
      "M": "To those in Jerusalem who have sworn oaths, this will seem like a false oracle. But he will bring their iniquity to mind, so that they are captured.",
      "T": "To Jerusalem's inhabitants — who have sworn treaty oaths to Babylon — this will seem like a false oracle. Surely the lots are wrong; surely Babylon won't really come for us. But Nebuchadnezzar will remember their covenant violations, their conspiracies with Egypt. Their iniquity will be recalled. And they will be taken."
    },
    "24": {
      "L": "Therefore thus says the Lord GOD: Because you have caused your iniquity to be remembered — in that your transgressions are uncovered, your sins visible in all your actions — because you have been brought to remembrance, you shall be seized by the hand.",
      "M": "Therefore thus says the Lord GOD: Because you have caused your iniquity to be remembered — because your transgressions are exposed and your sins visible in all your deeds — because you have come to remembrance, you shall be seized.",
      "T": "Therefore the Lord Yahweh says: You have done this to yourselves. Your iniquity has surfaced — visible, exposed, undeniable in every action you take. The memory of your violations has been called up — by me, through Babylon's divination. You will be seized. The instrument of judgment is already choosing his road."
    },
    "25": {
      "L": "And you, O defiled and wicked prince of Israel, whose day has come — the time when iniquity shall have an end —",
      "M": "And you, O profaned and wicked prince of Israel, whose day has come, the time when iniquity reaches its end —",
      "T": "And you — you profaned, defiled prince of Israel. You, Zedekiah. Your day has arrived: the moment when your iniquity finds its end, when the account runs out."
    },
    "26": {
      "L": "Thus says the Lord GOD: Remove the turban and take off the crown; this shall be no more. Exalt what is low and bring low what is high.",
      "M": "Thus says the Lord GOD: Take off the turban and remove the crown; it will be the same no longer. Lift up the lowly and bring down the exalted.",
      "T": "The Lord Yahweh says: The turban off. The crown off. The royal office as it has been is over. The order is inverted: what was low will be lifted; what was high will be brought down. Zedekiah's dynasty ends here."
    },
    "27": {
      "L": "Overturned, overturned, overturned I will make it — and it shall be no more until he comes whose right it is, and I will give it to him.",
      "M": "I will overturn it, overturn it, overturn it — and it will be no more until he comes to whom it belongs, and I will give it to him.",
      "T": "Overthrown. Overthrown. Overthrown. The triple decree: the dynasty as it has stood is ended. But not forever. It will wait — overturned and empty — until he comes whose rightful possession it is. I will give it to him. The kingship waits for its true heir, the one whose right it is by ancient promise."
    },
    "28": {
      "L": "And you, son of man, prophesy and say: Thus says the Lord GOD concerning the Ammonites and their reproach. Say: A sword, a sword is drawn; polished for slaughter, to consume, to flash —",
      "M": "And you, son of man, prophesy and say: Thus says the Lord GOD concerning the Ammonites and their contempt. Say: A sword — a sword is drawn; polished for slaughter, to flash like lightning —",
      "T": "And now, son of man, the Ammonites. They gloated over Jerusalem's fall. Prophesy against them too. Say from the Lord Yahweh: Their sword is also drawn — polished, flashing, ready for slaughter."
    },
    "29": {
      "L": "While false visions are seen concerning you and lies are divined about you — to lay you alongside the necks of the wicked slain, whose day has come, when their iniquity reaches its end.",
      "M": "While false visions are being seen about you and lies are divined for you — to place you alongside the slain wicked, whose day has come, when their iniquity reaches its end.",
      "T": "While Ammon's prophets see false visions of safety and divine comforting lies for her — Ammon's fate is being decided. She will be laid alongside the wicked slain. Her day also has a final reckoning: the moment when the iniquity accumulates to its full measure and the end arrives."
    },
    "30": {
      "L": "Return it to its sheath! In the place where you were created, in the land of your birth, I will judge you.",
      "M": "Return the sword to its sheath! In the place where you were created, in the land of your birth, I will judge you.",
      "T": "Should the sword return to its sheath? Not for Ammon. The judgment will come in Ammon's own land, in the place of her origin. She will not escape by hiding behind Jerusalem's fall."
    },
    "31": {
      "L": "I will pour out my indignation upon you; I will blow the fire of my wrath upon you and deliver you into the hands of brutal men, skilled in destruction.",
      "M": "I will pour out my indignation on you; I will blow the fire of my wrath upon you and deliver you into the hands of brutal men who are skilled in destruction.",
      "T": "I will pour my indignation out on Ammon. I will blow the fire of my wrath against her. I will hand her over to brutal men — men with no restraint and every skill for destroying. There will be nothing gentle in what comes."
    },
    "32": {
      "L": "You will become fuel for the fire; your blood will be in the midst of the land; you will be remembered no more — for I the LORD have spoken.",
      "M": "You will be fuel for the fire; your blood will be shed in the midst of the land; you will be remembered no more — for I the LORD have spoken.",
      "T": "Ammon will be consumed — fuel for the fire. Her blood will soak the ground of her own land. And then: not even a memory. Forgotten. Gone. I, Yahweh, have spoken this."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 19–21 written.')

if __name__ == '__main__':
    main()
