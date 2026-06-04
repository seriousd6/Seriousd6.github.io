"""
MKT Ezekiel chapters 34–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-34-36.py

=== CHAPTER OVERVIEW ===
Chapter 34: The Shepherd Oracle — Ezekiel's most extended shepherd-and-flock metaphor.
  vv. 1–10: Woe against Israel's shepherds (kings/leaders) who exploited rather than cared;
  God announces he will remove them and personally take over the flock.
  vv. 11–16: God himself goes out to search for and gather the scattered sheep.
  vv. 17–22: God judges between the sheep — the strong who pushed out the weak.
  vv. 23–24: Promise of one shepherd, "my servant David" — a future Davidic ruler-prince.
  vv. 25–31: Covenant of peace (berit shalom) — security, fertility, divine presence.
  This chapter is an explicit OT background for John 10 (Good Shepherd) and Matt 9:36.

Chapter 35: Oracle against Mount Seir / Edom — Edom nursed "perpetual enmity" against
  Israel (v. 5) and gloated when Jerusalem fell and claimed its territory (v. 10). God
  pronounces a mirror-judgment: Edom will become perpetually desolate as it wished for Israel.
  The chapter forms a structural pivot — the oracle against Edom (ch. 35) frames the oracle
  for Israel's land (ch. 36), making the pair a reversal: enemy desolate, homeland restored.

Chapter 36: Oracle to the Mountains of Israel — the land itself is addressed.
  vv. 1–15: The mountains of Israel will flourish again as the enemy nations are shamed.
  vv. 16–21: Historical retrospect — Israel defiled the land; exile was just punishment,
  but the exile itself shamed God's name ("these are Yahweh's people, and look at them").
  vv. 22–32: The "for my name's sake" restoration — not for Israel's merit but to vindicate
  God's reputation among the nations.
  vv. 24–28: The new exodus and transformation: gathering + cleansing + new heart/spirit
  (H3820 לֵב / H7307 רוּחַ). This is one of the theological peaks of Ezekiel and the
  whole OT — the promise that underpins Jer 31:31–34 and is fulfilled in NT Pentecost.
  vv. 29–38: Agricultural restoration and recognition formula.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה): "LORD" in L/M (small-caps convention). "Yahweh" in T — especially in
  the recognition formula ("you shall know that I am Yahweh"), the shepherd narrative,
  and the "for my name's sake" passage in 36:22-32 where the divine name is the
  theological subject. Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Lord GOD): "Lord GOD" in L/M (following small-caps
  convention). "Lord Yahweh" in T. Consistent throughout all Ezekiel scripts.

- Recognition formula (וְיָדְעוּ כִּי אֲנִי יְהוָה): L/M "you/they shall know that I am
  the LORD." T: "you/they shall know that I am Yahweh." Used at 34:27, 30; 35:4, 9,
  12, 15; 36:11, 23, 36, 38.

- H7307 (רוּחַ / spirit/wind/breath): Chapter 36:26-27 — God's own Spirit put within the
  people. Capitalised "Spirit" in all tiers for the divine Spirit given by God. The term
  is used unambiguously here as the divine Spirit (not wind or breath — context makes this
  clear). Consistent with prior Ezekiel handling.

- H3820 / H3824 (לֵב / heart): 36:26 — "heart of stone" vs. "heart of flesh" — the
  opposition is rendered literally in all tiers; the T tier unpacks the transformation
  without losing the concrete imagery.

- H7462 (רָעָה / to shepherd, pasture): Chapter 34 uses this as both noun (shepherd) and
  verb (to feed/pasture). L preserves the verbal force where possible: "feed" for the verb,
  "shepherd" for the noun. M/T use "shepherd" freely as verb also. The play between "feeding
  themselves" vs. "feeding the flock" is central to the passage and preserved in all tiers.

- H5315 (נֶפֶשׁ / soul/embodied self): Used in 34:31 in the phrase "sheep of my pasture —
  men" (אָדָם / humans). The verse distinguishes God's human flock from literal sheep.
  L: "human sheep," M/T: "human sheep of my pasture." The embodied self nuance is present
  but the dominant sense here is "human beings."

- H1285 (בְּרִית / covenant): 34:25 — "covenant of peace" (בְּרִית שָׁלוֹם). Rendered
  "covenant of peace" in L/M. T: "covenant of shalom" — the Hebrew word shalom carries
  more than peace (wholeness, well-being, flourishing); the T tier uses the Hebrew where
  it communicates more precisely than the English gloss.

- H7965 (שָׁלוֹם / peace/shalom): 34:25 and 36:26 area. In the "covenant of peace" phrase
  (34:25) the T tier uses "shalom" to surface the richness. Elsewhere rendered "peace" or
  "safety" depending on context.

- H5414 + H3820 + H1320 (give / heart / flesh): 36:26 — "a heart of flesh" as opposed to
  "heart of stone." All tiers render literally: "heart of stone" / "heart of flesh." T
  adds the interpretive note about what the exchange means without losing the imagery.

- "My servant David" (34:23-24): This is eschatological language pointing beyond the
  historical David (already dead for ~400 years by Ezekiel's time) to a future Davidic
  king/Messiah. L/M render literally "my servant David." T surfaces the messianic dimension:
  "my servant David" is rendered with a note in the verse text that this looks forward;
  the T phrasing makes the horizon-pointing function explicit.

- H5869 (עֵין / eye, spring, look): 34:6 — "upon every high hill" (עַל כָּל-גִּבְעָה
  גְּבֹהָה). Standard idiom. No special decision needed.

- H7080 + H5861 (desolation-related terms): Chapter 35 uses שְׁמָמָה (shemamah,
  desolation) repeatedly. L/M: "desolation." T: "wasteland" or "ruin" depending on context,
  to avoid mechanical repetition that deadens the rhetorical force.

- H2714 + shame/reproach terms (36:6, 7, 15, 30): חֶרְפָּה (reproach/disgrace) and related
  terms. This is honour-shame vocabulary central to the logic of chapter 36. L: "reproach."
  M: "disgrace/reproach." T: "shame" — explicitly naming the honour-shame dynamics at work
  in Israel's exile profaning God's name.

- "For my name's sake" (36:22): לְמַעַן שְׁמִי הַגָּדוֹל — the theological pivot of the
  chapter. God acts not from Israel's merit but to vindicate his own honour (name) which
  Israel's exile had publicly shamed. T makes this honour-restoration logic explicit.

=== ASPECT / TENSE NOTES ===

- Chapter 34 uses imperfect verbs for God's future actions ("I will search," "I will bring,"
  "I will make"). The L tier preserves future tense throughout. The accusation section
  (vv. 2-6) uses perfects and negated perfects for past failures — preserved in all tiers.

- "As I live" oath formula (34:8; 35:6, 11): Divine self-oath introducing solemn judgment.
  All tiers preserve this oath formula.

- Chapter 35: The accusation (vv. 5, 10) uses perfect verbs for Edom's completed crimes.
  The judgment oracle uses imperfect verbs for future punishment. Preserved in L/M; T
  makes the cause-and-effect logic more explicit.

- Chapter 36:16-21 is retrospective narrative — perfect verbs throughout. 36:22-38 pivots
  to future tense (imperfect). The tense shift marks the structural pivot from accusation
  to promise. L/M preserve the tense distribution.

=== OT INTERTEXTUALITY ===

- 34:23-24 ("my servant David") echoes 2 Sam 7 (Davidic covenant), Ps 89, Jer 23:5-6
  ("Branch of righteousness"). T surfaces this echo.
- 34:25 ("covenant of peace") echoes Num 25:12 (Phinehas) and Isa 54:10. T notes the
  berit shalom as a redemptive-historical category.
- 36:26-27 is the OT source behind Jer 31:31-34 (the new covenant), and both are
  picked up in Rom 8:4, 2 Cor 3:3, Heb 8. T notes the trajectory in v. 27.
- Ch. 35's "perpetual enmity" (v. 5, שִׂנְאַת עוֹלָם) echoes Num 20 and Obad 1:10-14.
- 36:35 ("like the garden of Eden") echoes Gen 2-3 explicitly — the restoration as a
  new creation/new Eden. T surfaces this.
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
  "34": {
    "1": {
      "L": "And the word of the LORD came to me, saying,",
      "M": "The word of the LORD came to me:",
      "T": "The word of Yahweh came to me:"
    },
    "2": {
      "L": "Son of man, prophesy against the shepherds of Israel; prophesy and say to them — to the shepherds: Thus says the Lord GOD: Woe to the shepherds of Israel who feed themselves! Should not shepherds feed the flock?",
      "M": "Son of man, prophesy against the shepherds of Israel; prophesy and say to them — to the shepherds: Thus says the Lord GOD: Woe to the shepherds of Israel who feed themselves! Should not shepherds feed the flock?",
      "T": "Son of man, speak against Israel's shepherds — its leaders. Say to them: Thus says the Lord Yahweh: A curse on the shepherds who graze only themselves! Are not shepherds there to feed the flock?"
    },
    "3": {
      "L": "The fat you eat, and with the wool you clothe yourselves; the well-fed you slaughter — but the flock you do not feed.",
      "M": "You eat the fat, you clothe yourselves with the wool, you slaughter the fatlings; but the flock you do not feed.",
      "T": "You take the richest cut of meat, wrap yourselves in wool, and slaughter the choice animals — while the flock goes unfed."
    },
    "4": {
      "L": "The weak you have not strengthened, and the sick you have not healed, and the injured you have not bound up, and the strayed you have not brought back, and the lost you have not sought; but with force and with harshness you have ruled over them.",
      "M": "You have not strengthened the weak, healed the sick, or bound up the injured. You have not brought back the strayed or sought the lost; but with force and harshness you have ruled them.",
      "T": "The frail you left to weaken further, the sick you never healed, the wounded you never bandaged, the wanderer you never turned back, the lost you never searched for. Instead you drove them with brute force and brutality."
    },
    "5": {
      "L": "And they were scattered for lack of a shepherd, and they became food for every beast of the field — and they were scattered.",
      "M": "So they were scattered, because there was no shepherd, and they became food for every wild beast. They were scattered,",
      "T": "With no shepherd to hold them together they scattered — easy prey for every wild animal. They were simply driven out,"
    },
    "6": {
      "L": "My sheep wandered through all the mountains and on every high hill. My flock was scattered over all the face of the earth, with none seeking and none searching for them.",
      "M": "my sheep wandered over all the mountains and on every high hill. My flock was scattered over all the face of the earth, with no one to search or seek for them.",
      "T": "my sheep roaming every mountain ridge and every high hillside, my flock dispersed across the face of the earth — with no one out looking for them, no one asking where they had gone."
    },
    "7": {
      "L": "Therefore, you shepherds, hear the word of the LORD:",
      "M": "Therefore, you shepherds, hear the word of the LORD:",
      "T": "Now hear this, you shepherds — hear the word of Yahweh:"
    },
    "8": {
      "L": "As I live, declares the Lord GOD — surely because my flock has become a prey, and my flock has become food for every beast of the field, because there was no shepherd, and because my shepherds did not search for my flock, but the shepherds fed themselves and did not feed my flock —",
      "M": "As I live, declares the Lord GOD — because my flock has become a prey and food for all the wild beasts, since there was no shepherd, and because my shepherds have not searched for my flock but have fed themselves and not fed my flock —",
      "T": "As surely as I live, declares the Lord Yahweh: my flock has become prey, fodder for every beast of the field, because there was no shepherd. My own shepherds never went looking for them. They fed themselves and left my flock to starve."
    },
    "9": {
      "L": "therefore, you shepherds, hear the word of the LORD:",
      "M": "therefore, you shepherds, hear the word of the LORD:",
      "T": "Therefore — you shepherds, listen to the word of Yahweh:"
    },
    "10": {
      "L": "Thus says the Lord GOD: Behold, I am against the shepherds, and I will require my flock from their hand, and I will put a stop to their shepherding the flock. The shepherds shall no longer feed themselves. I will rescue my flock from their mouths, so that it may no longer be food for them.",
      "M": "Thus says the Lord GOD: Behold, I am against the shepherds. I will hold them accountable for my flock and put an end to their feeding the flock. The shepherds shall feed themselves no more. I will rescue my flock from their mouths, so that it may no longer be food for them.",
      "T": "This is what the Lord Yahweh declares: I am against those shepherds. I will call them to account for what they have done to my flock. I will strip them of their role — they will no longer pasture themselves at my flock's expense. I will tear my sheep out of their mouths. My flock will not be their feed."
    },
    "11": {
      "L": "For thus says the Lord GOD: Behold, I myself will search for my sheep and will seek them out.",
      "M": "For thus says the Lord GOD: Behold, I myself will search for my sheep and seek them out.",
      "T": "For this is Yahweh's own word: I will go looking for my sheep myself. I will track them down."
    },
    "12": {
      "L": "As a shepherd seeks out his flock on a day when he is among his scattered sheep, so will I seek out my sheep and rescue them from all the places where they were scattered on a day of clouds and thick darkness.",
      "M": "As a shepherd seeks out his flock when some of his sheep have been scattered, so will I seek out my sheep. I will rescue them from all the places where they have been scattered on a day of clouds and thick darkness.",
      "T": "Just as a shepherd sets out to find his flock when the sheep have been driven apart, I will go out to find mine — and I will pull them back from every place they were scattered when that dark and clouded day of disaster came."
    },
    "13": {
      "L": "And I will bring them out from the peoples and gather them from the countries and bring them into their own land. And I will feed them on the mountains of Israel, by the watercourses, and in all the inhabited places of the land.",
      "M": "I will bring them out from the peoples and gather them from the countries and bring them into their own land. I will feed them on the mountains of Israel, by the streams, and in all the inhabited places of the country.",
      "T": "I will bring them back — out of every nation, gathered from every country — and return them to their own land. There I will feed them on Israel's mountains, beside its streams, in every settled place in the land."
    },
    "14": {
      "L": "In good pasture I will feed them, and on the mountain heights of Israel their fold shall be. There they shall lie down in good grazing land, and on rich pasture they shall feed on the mountains of Israel.",
      "M": "I will feed them in good pasture, and their fold shall be on the mountain heights of Israel. There they shall lie down in good grazing land, and on rich pasture they shall feed on the mountains of Israel.",
      "T": "I will give them the best pastureland, high in the mountains of Israel — a secure fold where they can rest, rich grazing land where they will truly be fed."
    },
    "15": {
      "L": "I myself will shepherd my flock, and I myself will make them lie down, declares the Lord GOD.",
      "M": "I myself will be the shepherd of my flock, and I myself will make them lie down, declares the Lord GOD.",
      "T": "I will be their shepherd — personally. I will lay them down to rest. This is the word of the Lord Yahweh."
    },
    "16": {
      "L": "The lost I will seek, and the strayed I will bring back, and the injured I will bind up, and the weak I will strengthen. But the fat and the strong I will destroy; I will feed them with justice.",
      "M": "I will seek the lost, bring back the strayed, bind up the injured, and strengthen the weak. But the fat and the strong I will destroy; I will feed them in justice.",
      "T": "Every lost one I will find, every stray I will bring home, every wound I will dress, every weak one I will strengthen. But the sleek and the powerful — those I will bring to account. I will shepherd with justice."
    },
    "17": {
      "L": "And as for you, my flock, thus says the Lord GOD: Behold, I judge between sheep and sheep, between rams and male goats.",
      "M": "As for you, my flock, thus says the Lord GOD: Behold, I judge between sheep and sheep, between rams and male goats.",
      "T": "But now I turn to you, my flock. Hear the word of the Lord Yahweh: I am going to judge — between sheep and sheep, between the rams and the goats."
    },
    "18": {
      "L": "Is it too small a thing for you that you feed on the good pasture, that you must tread down with your feet the rest of your pasture? And that you drink of the clear water, that you must muddy the rest with your feet?",
      "M": "Is it not enough for you to feed on the good pasture, that you must tread down with your feet the rest of your pasture? Or to drink of clear water, that you must muddy the rest with your feet?",
      "T": "Is it not enough to eat the best and drink the cleanest? Must you trample what is left with your hooves and foul the remaining water with your feet?"
    },
    "19": {
      "L": "And my flock — they eat what you have trodden with your feet, and drink what you have muddied with your feet.",
      "M": "And must my flock eat what you have trodden with your feet, and drink what you have muddied with your feet?",
      "T": "And then my flock has to eat the trampled scraps and drink the fouled water — the mess the strong ones left behind."
    },
    "20": {
      "L": "Therefore thus says the Lord GOD to them: Behold, I myself will judge between the fat sheep and the lean sheep.",
      "M": "Therefore, thus says the Lord GOD to them: Behold, I myself will judge between the fat sheep and the lean sheep.",
      "T": "Therefore this is what the Lord Yahweh says: I myself will judge between the well-fed and the hungry, between those who took everything and those left with nothing."
    },
    "21": {
      "L": "Because you push with side and with shoulder, and thrust all the weak with your horns, until you have scattered them abroad,",
      "M": "Because you push with side and shoulder, and thrust at all the weak with your horns, until you have scattered them abroad,",
      "T": "You have shoved the weak aside with your shoulders, driven them off with your horns, shoulder-blocked and gored until the vulnerable had nowhere left to go."
    },
    "22": {
      "L": "I will rescue my flock; they shall no longer be a prey. And I will judge between sheep and sheep.",
      "M": "I will rescue my flock; they shall no longer be a prey. And I will judge between sheep and sheep.",
      "T": "So I will rescue my flock — no more easy prey. And I will render judgment between one sheep and another."
    },
    "23": {
      "L": "And I will set up over them one shepherd, my servant David, and he shall feed them; he shall feed them and be their shepherd.",
      "M": "And I will set up over them one shepherd, my servant David, and he shall feed them: he shall feed them and be their shepherd.",
      "T": "I will appoint over them a single shepherd — my servant David. He will pasture them, tend them, be the shepherd they were always meant to have."
    },
    "24": {
      "L": "And I, the LORD, will be their God, and my servant David shall be prince among them. I, the LORD, have spoken.",
      "M": "And I, the LORD, will be their God, and my servant David shall be prince among them. I, the LORD, have spoken.",
      "T": "I — Yahweh — will be their God, and my servant David will stand among them as their ruler-prince. I, Yahweh, have pledged my word."
    },
    "25": {
      "L": "And I will make with them a covenant of peace, and I will banish wild beasts from the land, so that they may dwell securely in the wilderness and sleep in the woods.",
      "M": "I will make a covenant of peace with them and banish wild beasts from the land, so that they may dwell securely in the wilderness and sleep in the woods.",
      "T": "I will establish with them a covenant of shalom — and I will rid the land of dangerous animals, so they can live safely in the open wilderness and sleep in the forest without fear."
    },
    "26": {
      "L": "And I will make them and the places around my hill a blessing, and I will send down the showers in their season; they shall be showers of blessing.",
      "M": "I will make them and the places around my hill a blessing, and I will send down the showers in their season; they shall be showers of blessing.",
      "T": "I will make them and all the land around my holy hill a source of blessing. I will send rain in its season — not just rain, but showers of blessing."
    },
    "27": {
      "L": "And the trees of the field shall yield their fruit, and the earth shall yield its produce, and they shall be secure in their land. And they shall know that I am the LORD, when I break the bars of their yoke and deliver them from the hand of those who enslaved them.",
      "M": "The trees of the field shall yield their fruit, and the earth shall yield its increase, and they shall be secure in their land. And they shall know that I am the LORD, when I break the bars of their yoke and deliver them from the hand of those who enslaved them.",
      "T": "Every tree will bear its fruit, every field its harvest — and they will be safe in their own land. They will know that I am Yahweh when I snap the yoke bars off their necks and pull them free from those who made them slaves."
    },
    "28": {
      "L": "And they shall no longer be a prey to the nations, nor shall the beasts of the land devour them. They shall dwell securely, and none shall make them afraid.",
      "M": "They shall no longer be a prey to the nations, nor shall the beasts of the land devour them. They shall dwell securely, and none shall make them afraid.",
      "T": "Never again prey for foreign nations, never again hunted by wild beasts. They will live in safety — no more terror, no more panic."
    },
    "29": {
      "L": "And I will raise up for them a renowned planting, and they shall no more be consumed with famine in the land, and no longer bear the disgrace of the nations.",
      "M": "And I will provide for them a renowned planting, so that they shall no more be consumed with famine in the land, and no longer suffer the disgrace of the nations.",
      "T": "I will give them a famous land, flourishing and fruitful — no more dying of hunger, no more the shame of being the nation that cannot feed itself."
    },
    "30": {
      "L": "And they shall know that I, the LORD their God, am with them, and that they, the house of Israel, are my people, declares the Lord GOD.",
      "M": "And they shall know that I, the LORD their God, am with them, and that they, the house of Israel, are my people, declares the Lord GOD.",
      "T": "Then they will know — beyond all doubt — that I, Yahweh their God, am with them. They are my people; I am their God. This is the word of the Lord Yahweh."
    },
    "31": {
      "L": "You are my sheep, human sheep of my pasture, and I am your God, declares the Lord GOD.",
      "M": "You are my sheep, human sheep of my pasture, and I am your God, declares the Lord GOD.",
      "T": "You are my flock — the human flock of my own pasturing — and I am your God. This is the word of the Lord Yahweh."
    }
  },
  "35": {
    "1": {
      "L": "And the word of the LORD came to me, saying,",
      "M": "The word of the LORD came to me:",
      "T": "The word of Yahweh came to me:"
    },
    "2": {
      "L": "Son of man, set your face toward Mount Seir and prophesy against it,",
      "M": "Son of man, set your face toward Mount Seir and prophesy against it,",
      "T": "Son of man, turn your face toward Mount Seir and speak against it."
    },
    "3": {
      "L": "and say to it: Thus says the Lord GOD: Behold, I am against you, Mount Seir, and I will stretch out my hand against you and make you a desolation and a waste.",
      "M": "Say to it: Thus says the Lord GOD: Behold, I am against you, Mount Seir, and I will stretch out my hand against you and make you a desolation and a waste.",
      "T": "Say this: Thus says the Lord Yahweh — I am your adversary, Mount Seir. My hand is raised against you. I will reduce you to ruin, a wasteland."
    },
    "4": {
      "L": "Your cities I will lay in ruins, and you shall become a desolation, and you shall know that I am the LORD.",
      "M": "Your cities I will lay waste, and you shall become a desolation, and you shall know that I am the LORD.",
      "T": "City after city I will flatten into rubble. You will be left empty — and you will know that I am Yahweh."
    },
    "5": {
      "L": "Because you cherished a perpetual enmity and gave over the people of Israel to the power of the sword at the time of their calamity, at the time of their final punishment,",
      "M": "Because you cherished perpetual enmity and gave over the people of Israel to the power of the sword at the time of their calamity, at the time of their final punishment,",
      "T": "Because you nursed an ancient, unrelenting hatred — and when Israel's moment of catastrophe came, when their punishment reached its climax, you handed them over to the sword —"
    },
    "6": {
      "L": "therefore, as I live, declares the Lord GOD, I will destine you for blood, and blood shall pursue you. Since you did not hate blood, therefore blood shall pursue you.",
      "M": "therefore, as I live, declares the Lord GOD, I will destine you for blood, and blood shall pursue you. Since you did not hate bloodshed, bloodshed shall pursue you.",
      "T": "therefore — as I live, declares the Lord Yahweh — I will make blood your portion. Because you loved bloodshed, blood will be your fate. It will hunt you down."
    },
    "7": {
      "L": "And I will make Mount Seir a waste and a desolation, and I will cut off from it all who come and go.",
      "M": "I will make Mount Seir a waste and a desolation, and I will cut off from it all who come and go.",
      "T": "Mount Seir I will reduce to a barren waste — and I will eliminate every living soul from it, everyone who comes or goes."
    },
    "8": {
      "L": "And I will fill its mountains with the slain. On your hills and in your valleys and in all your ravines those slain by the sword shall fall.",
      "M": "I will fill its mountains with the slain. On your hills and in your valleys and in all your ravines those slain by the sword shall fall.",
      "T": "Your mountains I will heap with the dead. Your hills, your valleys, your ravines — all filled with those cut down by the sword."
    },
    "9": {
      "L": "I will make you a perpetual desolation, and your cities shall not return to be inhabited. Then you shall know that I am the LORD.",
      "M": "I will make you a perpetual desolation, and your cities shall not return to be inhabited. Then you shall know that I am the LORD.",
      "T": "You will become a ruin that stays ruined forever — your cities empty, never resettled. Then you will know that I am Yahweh."
    },
    "10": {
      "L": "Because you said, 'These two nations and these two countries shall be mine, and we will take possession of them' — although the LORD was there —",
      "M": "Because you said, 'These two nations and these two countries shall be mine, and we will possess them' — although the LORD was there —",
      "T": "You said, 'These two nations, these two territories — they will be ours. We will take possession of them.' Never mind that Yahweh was still there."
    },
    "11": {
      "L": "therefore, as I live, declares the Lord GOD, I will deal with you according to your anger and according to your envy that you showed out of your hatred against them. And I will make myself known among them when I judge you.",
      "M": "therefore, as I live, declares the Lord GOD, I will deal with you according to the anger and envy that you showed through your hatred of them. And I will make myself known among them when I judge you.",
      "T": "therefore — as I live, declares the Lord Yahweh — I will treat you exactly as your anger and jealousy and hatred treated them. And when I judge you, Israel will see who I am."
    },
    "12": {
      "L": "And you shall know that I am the LORD. I have heard all your revilings that you uttered against the mountains of Israel, saying, 'They are laid desolate; they are given to us to devour.'",
      "M": "And you shall know that I am the LORD. I have heard all the insults you hurled against the mountains of Israel, saying, 'They are laid desolate; they are given to us to devour.'",
      "T": "You will know that I am Yahweh. I heard every insult you hurled at Israel's mountains — 'They have been laid waste; they are ours now, a meal handed to us.'"
    },
    "13": {
      "L": "And you magnified yourselves against me with your mouth and multiplied your words against me; I heard it.",
      "M": "And you spoke arrogantly against me with your mouth and multiplied your words against me; I heard it.",
      "T": "You made big speeches against me, boasting on and on. I heard every word."
    },
    "14": {
      "L": "Thus says the Lord GOD: While the whole earth rejoices, I will make you a desolation.",
      "M": "Thus says the Lord GOD: While the whole earth rejoices, I will make you a desolation.",
      "T": "The Lord Yahweh says: When the whole world celebrates the restoration, you will be a wasteland."
    },
    "15": {
      "L": "As you rejoiced over the inheritance of the house of Israel because it was desolate, so I will deal with you. You shall be desolate, Mount Seir, and all Edom, all of it. Then they shall know that I am the LORD.",
      "M": "As you rejoiced over the inheritance of the house of Israel because it was desolate, so I will deal with you. You shall be desolate, Mount Seir, and all Edom, all of it. Then they shall know that I am the LORD.",
      "T": "You gloated when Israel's inheritance was stripped bare. I will give you the same. All of Mount Seir, all of Edom — stripped bare in return. Then they will know that I am Yahweh."
    }
  },
  "36": {
    "1": {
      "L": "And you, son of man, prophesy to the mountains of Israel and say: O mountains of Israel, hear the word of the LORD.",
      "M": "And you, son of man, prophesy to the mountains of Israel, and say: O mountains of Israel, hear the word of the LORD.",
      "T": "Now you, son of man — prophesy to the mountains of Israel. Say: Mountains of Israel, hear the word of Yahweh."
    },
    "2": {
      "L": "Thus says the Lord GOD: Because the enemy said of you, 'Aha!' and, 'The ancient high places have become our possession,'",
      "M": "Thus says the Lord GOD: Because the enemy said of you, 'Aha!' and 'The ancient high places have become our possession,'",
      "T": "The Lord Yahweh says: Because your enemy taunted you — 'Look at that! Those ancient high places are ours now!'"
    },
    "3": {
      "L": "therefore prophesy, and say: Thus says the Lord GOD: Because they made you desolate and crushed you from all sides, so that you became the possession of the rest of the nations, and you became the talk and taunt of the peoples,",
      "M": "therefore prophesy, and say: Thus says the Lord GOD: Because they made you desolate and crushed you from all sides, so that you became the possession of the rest of the nations, and became the talk and taunt of the peoples,",
      "T": "therefore prophesy. Say: This is what the Lord Yahweh declares — Because they stripped you bare from every side, turned you into a prize for the surrounding nations, made you the subject of rumors and mockery —"
    },
    "4": {
      "L": "therefore, O mountains of Israel, hear the word of the Lord GOD: Thus says the Lord GOD to the mountains and to the hills, to the ravines and to the valleys, to the desolate wastes and to the deserted cities, which have become a prey and derision to the rest of the nations all around,",
      "M": "therefore, O mountains of Israel, hear the word of the Lord GOD. Thus says the Lord GOD to the mountains and hills, to the ravines and valleys, to the desolate wastes and the deserted cities, which have become a prey and derision to the rest of the nations round about,",
      "T": "therefore, mountains of Israel, hear the word of the Lord Yahweh. To you all — mountains, hills, ravines, valleys, abandoned ruins, desolate cities, all that the surrounding nations have turned into spoil and a laughingstock —"
    },
    "5": {
      "L": "therefore thus says the Lord GOD: Surely in the fire of my jealousy I have spoken against the rest of the nations and against all Edom, who gave my land to themselves as a possession with wholehearted joy and with contemptuous disdain, to make its pasturelands their prey.",
      "M": "therefore thus says the Lord GOD: Surely in the fire of my jealousy I have spoken against the rest of the nations and against all Edom, who with wholehearted joy and utter contempt seized my land as their possession, making its pasturelands their prey.",
      "T": "this is what the Lord Yahweh declares, burning with jealous wrath: I am speaking against all those nations — especially against all of Edom — who seized my land for themselves with smug delight and bottomless contempt, looting its pastures like prey."
    },
    "6": {
      "L": "Therefore, prophesy concerning the land of Israel, and say to the mountains and hills, to the ravines and valleys: Thus says the Lord GOD: Behold, in my jealousy and in my wrath I have spoken, because you have borne the reproach of the nations.",
      "M": "Therefore, prophesy concerning the land of Israel, and say to the mountains and hills, to the ravines and valleys: Thus says the Lord GOD: Behold, I have spoken in my jealousy and in my wrath, because you have suffered the reproach of the nations.",
      "T": "Therefore prophesy over the land of Israel. Tell the mountains and hills, the valleys and ravines: The Lord Yahweh declares — out of my burning jealousy, out of my wrath — because you have been made to carry the nations' shame:"
    },
    "7": {
      "L": "Therefore thus says the Lord GOD: I have lifted up my hand and sworn — Surely the nations that are all around you shall themselves bear their shame.",
      "M": "Therefore thus says the Lord GOD: I swear with uplifted hand that the nations round about you shall themselves suffer reproach.",
      "T": "Therefore the Lord Yahweh swears — hand raised, oath binding: The nations surrounding you will taste shame themselves."
    },
    "8": {
      "L": "But you, O mountains of Israel, shall shoot forth your branches and yield your fruit to my people Israel, for they will soon come.",
      "M": "But you, O mountains of Israel, shall shoot forth your branches and yield your fruit to my people Israel, for they will soon come home.",
      "T": "But you, mountains of Israel — you will flourish again. You will spread your branches and bear fruit for my people Israel. They are coming home soon."
    },
    "9": {
      "L": "For behold, I am for you, and I will turn to you, and you shall be tilled and sown.",
      "M": "For behold, I am for you, and I will turn to you, and you shall be tilled and sown.",
      "T": "I have turned my face toward you. I am on your side. You will be plowed and planted again."
    },
    "10": {
      "L": "And I will multiply people upon you, all the house of Israel, all of it. The cities shall be inhabited and the waste places rebuilt.",
      "M": "And I will multiply people upon you, the whole house of Israel, all of it. The cities shall be inhabited and the waste places rebuilt.",
      "T": "I will fill you with people — the whole house of Israel, every part of it. The cities will have inhabitants again; the ruins will be rebuilt."
    },
    "11": {
      "L": "And I will multiply upon you man and beast, and they shall multiply and be fruitful. And I will settle you as in your former times and will do more good to you than at your beginnings. Then you shall know that I am the LORD.",
      "M": "And I will multiply upon you man and beast, and they shall multiply and be fruitful. I will settle you as in your former times and will do more good to you than at your beginnings. Then you shall know that I am the LORD.",
      "T": "People and animals alike will swarm over you, multiplying, thriving. I will restore you to what you once were — and then do even better than before. You will know that I am Yahweh."
    },
    "12": {
      "L": "And I will let people walk upon you, even my people Israel. And they shall possess you, and you shall be their inheritance, and you shall no longer bereave them of children.",
      "M": "I will let people walk on you, even my people Israel. They shall possess you, and you shall be their inheritance, and you shall no longer bereave them of children.",
      "T": "My own people Israel will walk on your soil again. They will possess you, inherit you — and you will no longer swallow up their children."
    },
    "13": {
      "L": "Thus says the Lord GOD: Because they say to you, 'You devour people and you bereaved your nation of children,'",
      "M": "Thus says the Lord GOD: Because they say to you, 'You devour people and bereave your nation of children,'",
      "T": "The Lord Yahweh says: Because they accuse you — 'This land eats people alive; it has swallowed up its own nation's children' —"
    },
    "14": {
      "L": "therefore you shall no longer devour people and no longer bereave your nation of children, declares the Lord GOD.",
      "M": "therefore you shall no longer devour people or bereave your nation of children, declares the Lord GOD.",
      "T": "therefore the curse is broken. You will no longer swallow people, no longer rob the nation of its children. The word of the Lord Yahweh."
    },
    "15": {
      "L": "And I will not let you hear anymore the reproach of the nations, and you shall no longer bear the disgrace of the peoples, and your nation you shall no longer cause to stumble, declares the Lord GOD.",
      "M": "And I will not let you hear anymore the reproach of the nations, and you shall no longer bear the disgrace of the peoples, and your nation you shall no longer cause to stumble, declares the Lord GOD.",
      "T": "I will silence the taunts of the nations so you never hear them again. You will no longer carry the peoples' disgrace, and you will no longer be the ruin of your own nation. The word of the Lord Yahweh."
    },
    "16": {
      "L": "And the word of the LORD came to me, saying,",
      "M": "The word of the LORD came to me:",
      "T": "The word of Yahweh came to me:"
    },
    "17": {
      "L": "Son of man, when the house of Israel lived in their own land, they defiled it by their ways and their deeds. Their conduct before me was like the uncleanness of a woman in her menstrual impurity.",
      "M": "Son of man, when the house of Israel lived in their own land, they defiled it by their conduct and their deeds. Their way before me was like the uncleanness of a woman in her menstrual impurity.",
      "T": "Son of man — when Israel lived in its own land, it polluted that land through its behavior and its practices. The way they conducted themselves before me was like the ritual impurity of a woman in her monthly cycle."
    },
    "18": {
      "L": "So I poured out my wrath upon them for the blood they had shed in the land and for the idols with which they had defiled it.",
      "M": "So I poured out my wrath upon them for the blood they had shed in the land and for the idols with which they had defiled it.",
      "T": "So I unleashed my fury on them — for the bloodshed they had committed on the land, for the idols with which they had polluted it."
    },
    "19": {
      "L": "I scattered them among the nations, and they were dispersed through the countries. In accordance with their ways and their deeds I judged them.",
      "M": "I scattered them among the nations, and they were dispersed through the countries. In accordance with their conduct and their deeds I judged them.",
      "T": "I flung them out among the nations, scattered them across every country. Their judgment matched their deeds."
    },
    "20": {
      "L": "And when they came to the nations, wherever they came, they profaned my holy name, in that people said of them, 'These are the people of the LORD, and yet they had to go out of his land.'",
      "M": "But when they came to the nations, wherever they came, they profaned my holy name, in that people said of them, 'These are the people of the LORD, and yet they had to go out of his land.'",
      "T": "But everywhere they went in exile, they desecrated my holy name. People looked at them and said, 'These are supposed to be Yahweh's people — and look, their own God has expelled them from his land.'"
    },
    "21": {
      "L": "But I had concern for my holy name, which the house of Israel had profaned among the nations to which they came.",
      "M": "But I had concern for my holy name, which the house of Israel had profaned among the nations to which they came.",
      "T": "But it was my own holy name I was concerned about — the name that Israel had dragged through the mud in every nation they had entered."
    },
    "22": {
      "L": "Therefore say to the house of Israel: Thus says the Lord GOD: It is not for your sake, O house of Israel, that I am about to act, but for the sake of my holy name, which you have profaned among the nations to which you came.",
      "M": "Therefore say to the house of Israel: Thus says the Lord GOD: It is not for your sake, O house of Israel, that I am about to act, but for the sake of my holy name, which you have profaned among the nations to which you came.",
      "T": "So tell the house of Israel: The Lord Yahweh declares — What I am about to do, I am not doing for your benefit. I am doing it for the sake of my holy name — the name you shamed in every nation you entered."
    },
    "23": {
      "L": "And I will vindicate the holiness of my great name, which has been profaned among the nations, and which you have profaned among them. And the nations shall know that I am the LORD, declares the Lord GOD, when through you I vindicate my holiness before their eyes.",
      "M": "I will vindicate the holiness of my great name, which has been profaned among the nations, and which you have profaned among them. And the nations shall know that I am the LORD, declares the Lord GOD, when through you I vindicate my holiness before their eyes.",
      "T": "I will demonstrate the holiness of my great name — the name so long dishonored among the nations, the name you yourselves dishonored among them. The nations will know that I am Yahweh — the word of the Lord Yahweh — when they see me vindicate my holiness through what I do to you and for you, before their eyes."
    },
    "24": {
      "L": "I will take you from the nations and gather you from all the countries and bring you into your own land.",
      "M": "I will take you from the nations and gather you from all the countries and bring you into your own land.",
      "T": "I will draw you out from every nation, gather you from every country, and bring you back into your own land."
    },
    "25": {
      "L": "And I will sprinkle clean water upon you, and you shall be clean. From all your uncleannesses and from all your idols I will cleanse you.",
      "M": "I will sprinkle clean water on you, and you shall be clean from all your uncleannesses, and from all your idols I will cleanse you.",
      "T": "I will pour clean water over you and you will be clean — clean from every defilement, cleansed of every idol."
    },
    "26": {
      "L": "And a new heart I will give you, and a new spirit I will put within you. And I will remove the heart of stone from your flesh and give you a heart of flesh.",
      "M": "And I will give you a new heart, and a new spirit I will put within you. I will remove the heart of stone from your flesh and give you a heart of flesh.",
      "T": "I will give you a new heart — a heart of flesh to replace the stone that is in you now — and I will plant a new spirit within you."
    },
    "27": {
      "L": "And my Spirit I will put within you, and I will cause you to walk in my statutes and to be careful to observe my rules.",
      "M": "And I will put my Spirit within you, and cause you to walk in my statutes and be careful to obey my rules.",
      "T": "I will put my own Spirit inside you — and that Spirit will move you to follow my statutes and take care to keep my decrees."
    },
    "28": {
      "L": "And you shall dwell in the land that I gave to your fathers, and you shall be my people, and I will be your God.",
      "M": "You shall dwell in the land that I gave to your fathers, and you shall be my people, and I will be your God.",
      "T": "You will live in the land I gave to your ancestors. You will be my people; I will be your God."
    },
    "29": {
      "L": "And I will save you from all your uncleannesses. And I will summon the grain and make it abundant, and I will bring no famine upon you.",
      "M": "And I will deliver you from all your uncleannesses. I will summon the grain and make it abundant and bring no famine upon you.",
      "T": "I will deliver you from every impurity. I will call up the grain to abundance — no more famine sent against you."
    },
    "30": {
      "L": "And I will make the fruit of the tree and the produce of the field abundant, so that you will no longer suffer the disgrace of famine among the nations.",
      "M": "I will make the fruit of the tree and the produce of the field abundant, so that you may never again suffer the disgrace of famine among the nations.",
      "T": "Tree and field will burst with abundance — so that famine's shame will never be laid against you among the nations again."
    },
    "31": {
      "L": "Then you will remember your evil ways and your deeds that were not good, and you will loathe yourselves for your iniquities and for your abominations.",
      "M": "Then you will remember your evil ways and your deeds that were not good, and you will loathe yourselves for your iniquities and for your abominations.",
      "T": "Then — in the midst of all that restoration — you will recall your own wicked history, the terrible choices you made. And you will despise what you once were."
    },
    "32": {
      "L": "It is not for your sake that I act, declares the Lord GOD — let that be known to you. Be ashamed and confounded for your ways, O house of Israel.",
      "M": "It is not for your sake that I am doing this, declares the Lord GOD; let that be known to you. Be ashamed and confounded for your ways, O house of Israel.",
      "T": "Be clear on this — the Lord Yahweh declares it plainly: I am not doing this for your sake. Be ashamed, Israel. Let the shame of what you were settle on you."
    },
    "33": {
      "L": "Thus says the Lord GOD: On the day I cleanse you from all your iniquities, I will cause the cities to be inhabited, and the waste places shall be rebuilt.",
      "M": "Thus says the Lord GOD: On the day that I cleanse you from all your iniquities, I will cause the cities to be inhabited, and the waste places shall be rebuilt.",
      "T": "The Lord Yahweh says: On the day I wash away all your guilt, I will fill the cities with people again — and every ruin will be rebuilt."
    },
    "34": {
      "L": "And the desolate land shall be tilled, whereas it was a desolation in the sight of every passerby.",
      "M": "And the desolate land shall be tilled, instead of being the desolation that it was in the sight of all who passed by.",
      "T": "The land that has lain empty will be under the plow again — no longer the scene of devastation that every traveler once stopped to stare at."
    },
    "35": {
      "L": "And they shall say, 'This land that was desolate has become like the garden of Eden, and the waste and desolate and ruined cities are now fortified and inhabited.'",
      "M": "And they will say, 'This land that was desolate has become like the garden of Eden, and the waste and desolate and ruined cities are now fortified and inhabited.'",
      "T": "And people will say, 'This was the wasteland — and now it looks like the garden of Eden. Those ruined, abandoned cities are walled and full of people.'"
    },
    "36": {
      "L": "Then the nations that are left all around you shall know that I, the LORD, have rebuilt the ruined places and replanted that which was desolate. I, the LORD, have spoken, and I will do it.",
      "M": "Then the nations that are left all around you shall know that I, the LORD, have rebuilt the ruined places and replanted that which was desolate. I, the LORD, have spoken, and I will do it.",
      "T": "Then the nations still standing around you will know: I — Yahweh — rebuilt those ruins; I — Yahweh — replanted that wasteland. I have spoken. I will do it."
    },
    "37": {
      "L": "Thus says the Lord GOD: This also I will let the house of Israel ask me to do for them: to multiply their people like a flock.",
      "M": "Thus says the Lord GOD: This also I will let the house of Israel ask me to do for them: to multiply their people like a flock.",
      "T": "The Lord Yahweh says: And there is something more I will grant the house of Israel if they ask — I will multiply them like a flock."
    },
    "38": {
      "L": "Like the flocks set apart for sacrifice, like the flock of Jerusalem at her appointed feasts, so shall the ruined cities be filled with flocks of people. Then they shall know that I am the LORD.",
      "M": "Like the flocks set apart for sacrifice, like the flock at Jerusalem during her appointed feasts, so shall the waste cities be filled with flocks of people. Then they shall know that I am the LORD.",
      "T": "Like the dense flocks that fill Jerusalem at the great festivals, like herds gathered for the sacred offerings — so will the ruined cities fill with people. Then they will know that I am Yahweh."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 34–36 written.')

if __name__ == '__main__':
    main()
