"""
MKT Jeremiah chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-10-12.py

Translation decisions (all consistent with mkt-jeremiah-1-3.py):
- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name force is
  significant (oracles, covenant declarations, lament address). Narrative quotation formulas
  use "Yahweh says" or "Yahweh told me" in T for immediacy.
- H430 (אֱלֹהִים): "God" in all tiers; "gods" when referring to foreign deities.
- H1697 (דָּבָר): "word" in all tiers — the prophetic-word formula is theologically load-bearing.
- H1285 (בְּרִית): "covenant" in all tiers throughout ch. 11 — the formal covenant-lawsuit
  structure requires this weight everywhere it appears.
- H7307 (רוּחַ): 10:13 "wind" — physical wind from Yahweh's storehouses, not Spirit; not
  capitalised. No divine-Spirit usage in these three chapters.
- H5315 (נֶפֶשׁ): 12:7 "the one I deeply love" (L: "the dearly beloved of my soul") — divine
  use of the term to express Yahweh's attachment to Israel; renders the full personal weight.
- H7451 (רָעָה): context-sensitive throughout. When denoting divine judgment coming: "disaster"
  (11:11, 11:17, 11:23, 12:14); when Israel's moral state: "wickedness" / "evil" (11:8, 11:15).
- H1168 (בַּעַל): proper name "Baal" in all tiers — no gloss substitution (11:13, 11:17, 12:16).
- H1322 (בֹּשֶׁת): 11:13 "shameful thing / Shameful Thing" — the prophetic nickname for Baal;
  T capitalises to signal the ironic epithet, carrying through from 3:24.
- H571 (אֱמֶת): 10:10 "true God" — אֱלֹהִים אֱמֶת: the adjective means "truth / faithfulness";
  "true God" is the standard English rendering and captures both senses.
- H2416 (חַי): 10:10 "living God" — the divine vitality contrasted with the lifeless idol.
- H4941 (מִשְׁפָּט): 12:1 "judgments / justice" — in the lament context Jeremiah uses this to
  say both 'your rulings are righteous' and 'I want to dispute your verdict'; T surfaces the
  double force explicitly.

Textual note — 10:11 (Aramaic):
  This verse is the only Aramaic verse in Jeremiah (and one of very few in the entire Hebrew
  Bible). The surrounding text is Hebrew; v.11 is in Aramaic — apparently a stock polemic
  addressed to the nations in their own trade language. This is noted in the T tier with a
  brief scholarly flag. The content is a formulaic refutation of foreign gods.

Textual note — 11:15:
  The Hebrew of 11:15 is partially corrupt or compressed, making reconstruction uncertain.
  The verse appears to ask what Israel ("my beloved") is doing in the temple while practicing
  wickedness, and whether she thinks ritual sacrifice forestalls doom. The T tier renders the
  rhetorical thrust; L/M follow a defensible text close to the MT.

Structural notes:
  Ch. 10 — Idol polemic and lament. vv. 1-16: the great idol-polemic (compare Isa 40-44, written
  in the same period). vv. 17-25: the city prepares for siege (vv. 17-18), Jeremiah's lament
  over his wounds and lost tent (vv. 19-20), a diagnosis of failed leadership (v. 21), the
  northern threat (v. 22), a wisdom saying about human limits (v. 23), and a closing petition
  (vv. 24-25). The "portion of Jacob" refrain (v. 16) also appears at 51:19 as a structural
  bookend to the book.

  Ch. 11 — The Covenant Sermon. Yahweh charges Jeremiah to re-proclaim the Sinai covenant
  (vv. 1-8), then reveals that Judah has broken it again in a new conspiracy (vv. 9-13). The
  divine prohibition on intercession recurs (v. 14; cf. 7:16). A biographical turn: Anathoth,
  Jeremiah's home village, has plotted his death (vv. 18-23). This is the first of the
  "confessions of Jeremiah" — deeply personal lament-prayers woven through chs. 11-20.

  Ch. 12 — The Theodicy Lament. Jeremiah presses his complaint to God about the prosperity of
  the wicked (vv. 1-4). God's jarring response does not comfort but challenges: if you cannot
  manage on foot, what will you do against horses? (v. 5). Then unexpectedly, Yahweh himself
  laments over his forsaken inheritance (vv. 7-13) — one of the most emotionally raw divine
  speeches in the OT. Closes with conditional promise of restoration for the nations (vv. 14-17),
  revisiting the six verbs of Jer 1:10 ("uproot... pluck up... destroy... build up").

OT echoes:
  10:12-13 — echoed nearly verbatim in 51:15-16; creation-theology close to Ps 104 and Isa 40.
  10:23 — echoes Prov 16:9 and 20:24; the wisdom tradition on human limits.
  11:4 — "iron furnace" = Deut 4:20; cf. 1 Kings 8:51.
  11:19 — "like a gentle lamb to the slaughter" — the servant-song echo (Isa 53:7) is real
  though in reverse direction; both draw on the same cultural image of sacrificial innocence.
  12:3 — "pull them out like sheep for slaughter" — echoes Ps 44:22, picked up in Rom 8:36.
  12:7 — "I have forsaken my house" — the divine abandonment of the temple; anticipates
  Ezek 10-11 and the Spirit-departure vision.
  12:14-17 — the six verbs of 1:10 recur structurally; the nations are now included in the
  uprooting-and-planting promise, anticipating Jer 31:28 and the new covenant vision.
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

JEREMIAH = {
  "10": {
    "1": {
      "L": "Hear the word which the LORD speaks to you, O house of Israel:",
      "M": "Hear the word that the LORD speaks to you, O house of Israel:",
      "T": "Listen to Yahweh's word, house of Israel:"
    },
    "2": {
      "L": "Thus says the LORD: Do not learn the way of the nations, and be not dismayed at the signs of the heavens, for the nations are dismayed at them.",
      "M": "This is what the LORD says: Do not follow the practices of the nations, and do not be terrified by the signs in the sky, even though the nations are terrified by them.",
      "T": "Yahweh says this: Do not live the way the nations live. Do not cower before omens in the sky — though the nations are cowering. Their panic is not yours to carry."
    },
    "3": {
      "L": "For the customs of the peoples are vanity; a workman cuts it from the forest with an axe, the work of the hands.",
      "M": "For the customs of the peoples are worthless; a craftsman cuts down a tree from the forest with an axe — it is the work of human hands.",
      "T": "The religious customs of the nations are hollow from the start: someone takes an axe into the forest, cuts down a tree — and that is the beginning of a god."
    },
    "4": {
      "L": "They adorn it with silver and gold; they fasten it with nails and with hammers so that it cannot move.",
      "M": "They adorn it with silver and gold and secure it with nails and hammers so it will not topple.",
      "T": "They drape it with silver and gold, nail it to the floor so it will not fall over — and call it a deity."
    },
    "5": {
      "L": "They are like a scarecrow in a cucumber field — they cannot speak; they must be carried, for they cannot walk. Do not be afraid of them, for they cannot do harm, and neither is it in them to do good.",
      "M": "They are like a scarecrow in a melon patch — they cannot speak; they have to be carried, for they cannot walk. Do not fear them: they cannot do harm, and neither can they do any good.",
      "T": "An idol is like a scarecrow in a garden patch — it cannot say a word; it has to be carried because it cannot walk. Fear it? You could not be harmed by anything less. It cannot hurt you. It cannot help you either."
    },
    "6": {
      "L": "There is none like you, O LORD; you are great, and great is your name in might.",
      "M": "There is no one like you, O LORD; you are great, and your name is great in power.",
      "T": "There is no one like you, Yahweh. You are great, and your name is great in power."
    },
    "7": {
      "L": "Who would not fear you, O King of the nations? For this is your due; for among all the wise men of the nations and in all their kingdoms there is none like you.",
      "M": "Who should not fear you, O King of the nations? It is what you deserve; for among all the wise of every nation, in all their kingdoms, there is no one like you.",
      "T": "Who would not fear you, King of the nations? Fear is your due. Among all the wise men of every nation, in every kingdom in the world, there is no one like you."
    },
    "8": {
      "L": "But they are altogether brutish and foolish; the teaching of idols is a doctrine of vanity.",
      "M": "But they are all dull and senseless; the instruction that comes from idols is nothing but worthless nonsense.",
      "T": "But these idol-makers are all dull and stupid. Instruction from a carved block of wood — what a worthless doctrine that is."
    },
    "9": {
      "L": "Beaten silver is brought from Tarshish and gold from Uphaz, the work of the craftsman and of the goldsmith's hands; blue and purple are their garments — they are all the work of skilled workers.",
      "M": "Silver sheets are imported from Tarshish and gold from Uphaz, the work of craftsman and goldsmith; their clothing is of blue and purple — all of it the work of skilled artisans.",
      "T": "They import hammered silver from Tarshish, gold from Uphaz — crafted by skilled hands, clothed in blue and purple fabric. All that skill, all that wealth, in the service of worthlessness."
    },
    "10": {
      "L": "But the LORD is the true God; he is the living God and an everlasting King. At his wrath the earth quakes, and the nations cannot endure his indignation.",
      "M": "But the LORD is the true God; he is the living God and the eternal King. At his anger the earth quakes, and the nations cannot withstand his wrath.",
      "T": "But Yahweh is the true God — the living God, the eternal King. When he is angry, the earth quakes; the nations cannot hold their ground when his wrath breaks loose."
    },
    "11": {
      "L": "The gods who did not make the heavens and the earth — they shall perish from the earth and from under the heavens.",
      "M": "The gods who did not make the heavens and the earth shall perish from the earth and from under the heavens.",
      "T": "These so-called gods never made the heavens or the earth — and they will be swept away from the earth, swept away from under the very skies they never created. [This verse is in Aramaic in the original — a refutation addressed to the nations in their own tongue.]"
    },
    "12": {
      "L": "He who made the earth by his power, who established the world by his wisdom, and by his understanding stretched out the heavens.",
      "M": "He made the earth by his power; he established the world by his wisdom and stretched out the heavens by his understanding.",
      "T": "He shaped the earth by sheer power. He set the world on its foundations by wisdom. By his understanding he stretched out the sky."
    },
    "13": {
      "L": "At the sound of his voice there is a tumult of waters in the heavens, and he makes vapors rise from the ends of the earth; he makes lightning for the rain and brings forth the wind from his storehouses.",
      "M": "When he speaks, the waters in the sky roar; he causes clouds to rise from the ends of the earth. He makes lightning for the rain and brings out the wind from his storehouses.",
      "T": "He speaks and the heavens thunder with rain; clouds billow up from the far ends of the earth. He splits lightning open for the rain and throws wide the doors of his treasury of winds."
    },
    "14": {
      "L": "Every man is brutish and without knowledge; every goldsmith is put to shame by his image, for his molten images are falsehood, and there is no breath in them.",
      "M": "Every man is stupid and ignorant; every goldsmith is shamed by his idol, for the images he casts are a fraud — there is no breath in them.",
      "T": "Every idol-maker is a fool with no real knowledge. Every goldsmith is put to shame by the very thing he made: a cast image that is a lie, an object with no breath of life in it at all."
    },
    "15": {
      "L": "They are vanity, a work of errors; in the time of their visitation they shall perish.",
      "M": "They are worthless, a product of delusion; when they are called to account, they will be destroyed.",
      "T": "Worthless — every one of them. Works of delusion. And when the day of reckoning comes, they will perish."
    },
    "16": {
      "L": "Not like these is the portion of Jacob, for he is the one who formed all things, and Israel is the tribe of his inheritance; the LORD of hosts is his name.",
      "M": "He who is Jacob's portion is not like them, for he is the maker of all things, and Israel is the people of his inheritance; the LORD of hosts is his name.",
      "T": "But Jacob's God is nothing like them — he made everything there is. Israel is his own people, his chosen inheritance. The LORD of hosts is his name."
    },
    "17": {
      "L": "Gather up your bundle from the ground, O inhabitant of the siege!",
      "M": "Gather your belongings from the ground, O inhabitant of the besieged city!",
      "T": "Pack what you can carry and go — you who live in a city about to fall!"
    },
    "18": {
      "L": "For thus says the LORD: Behold, I am slinging out the inhabitants of the land at this time, and I will bring distress upon them, that they may find it so.",
      "M": "For this is what the LORD says: I am about to hurl the inhabitants of the land out at this very time, and I will bring such distress on them that they feel every bit of it.",
      "T": "For Yahweh says: I am about to fling the people of this land away — all at once. I will press down on them until they feel the full weight of it."
    },
    "19": {
      "L": "Woe is me for my hurt! My wound is grievous. But I said: Truly this is a grief, and I must bear it.",
      "M": "Woe to me for my wound! My injury is severe. But I said to myself: This is truly my burden, and I must endure it.",
      "T": "Woe to me — I am wounded! The hurt is deep. And yet I told myself: this is mine to carry. I will bear it."
    },
    "20": {
      "L": "My tent is destroyed, and all my cords are broken; my children have gone from me and are no more; there is no one to spread my tent again or set up my curtains.",
      "M": "My tent is ruined, all its ropes have snapped; my children have left me and are gone; there is no one to pitch my tent again or hang the curtains.",
      "T": "My tent is gone — every rope snapped. My children have left and will not come back. There is no one to pitch the tent again, no one to hang the curtains. The camp is empty."
    },
    "21": {
      "L": "For the shepherds have become brutish and do not seek the LORD; therefore they have not prospered, and all their flock is scattered.",
      "M": "For the leaders have been foolish; they have not sought the LORD, and so they have not prospered, and all their people are scattered.",
      "T": "The shepherds — the leaders — were fools. They never sought the LORD, so nothing they did succeeded. Their flocks scattered in every direction."
    },
    "22": {
      "L": "Hark, a report! Behold, it comes — a great tumult out of the north country to make the cities of Judah desolate, a den of jackals.",
      "M": "Listen! A report is coming — a great commotion from the north — to turn the cities of Judah into a wasteland, a haunt of jackals.",
      "T": "Can you hear it? A rumble from the north — a massive force — coming to turn every city of Judah into rubble, leaving them to the jackals."
    },
    "23": {
      "L": "I know, O LORD, that the way of a man is not in himself; it is not in man who walks to direct his steps.",
      "M": "I know, O LORD, that a person's way is not their own; it is not within the power of those who walk to direct their steps.",
      "T": "LORD, I know this: no human being truly charts their own course. The one who walks cannot determine where his feet will take him."
    },
    "24": {
      "L": "Correct me, O LORD, but with justice; not in your anger, lest you bring me to nothing.",
      "M": "Discipline me, LORD, but with fairness; not in anger, or you will reduce me to nothing.",
      "T": "Correct me, Yahweh — but do it with measured justice, not with the full weight of your anger. If you come at me in wrath, there will be nothing of me left."
    },
    "25": {
      "L": "Pour out your wrath on the nations that know you not, and on the peoples that call not on your name; for they have devoured Jacob — devoured him and consumed him — and have made his habitation desolate.",
      "M": "Pour out your wrath on the nations that do not know you, on the peoples that do not call on your name; for they have devoured Jacob — devoured and consumed him — and have turned his homeland into a wasteland.",
      "T": "Pour your wrath on the nations who have never known you, on the peoples who have never called on your name. They are the ones who devoured Jacob — consumed him whole — and left his home a wasteland."
    }
  },
  "11": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD, saying:",
      "M": "The word that came to Jeremiah from the LORD:",
      "T": "This is the word that came to Jeremiah from Yahweh:"
    },
    "2": {
      "L": "Hear the words of this covenant, and speak them to the men of Judah and the inhabitants of Jerusalem.",
      "M": "Hear the terms of this covenant and announce them to the people of Judah and to the inhabitants of Jerusalem.",
      "T": "Hear the terms of this covenant — and then go and announce them to the men of Judah and all who live in Jerusalem."
    },
    "3": {
      "L": "Say to them: Thus says the LORD, the God of Israel: Cursed is the man who does not hear the words of this covenant,",
      "M": "Tell them: This is what the LORD, the God of Israel, says: Cursed is anyone who does not obey the terms of this covenant,",
      "T": "'Tell them this,' Yahweh says, the God of Israel: Cursed is anyone who refuses to hear and keep the words of this covenant."
    },
    "4": {
      "L": "which I commanded your fathers when I brought them out of the land of Egypt, out of the iron furnace, saying: Obey my voice and do according to all that I command you, so shall you be my people and I will be your God,",
      "M": "which I commanded your ancestors when I brought them out of Egypt, out of the iron smelting furnace, saying: Obey my voice and do everything I command you, and you will be my people and I will be your God,",
      "T": "Those are the terms I laid down for your ancestors when I pulled them out of Egypt — out of that iron furnace. 'Obey my voice,' I said. 'Do everything I command, and you will be my people, and I will be your God.'"
    },
    "5": {
      "L": "that I might establish the oath I swore to your fathers, to give them a land flowing with milk and honey, as it is this day. Then I answered: So be it, O LORD.",
      "M": "I said this in order to fulfill the oath I swore to your ancestors, to give them a land flowing with milk and honey, as it still is today. I answered: Amen, LORD.",
      "T": "This is how I would fulfill the oath I swore to your ancestors — to give them a land overflowing with milk and honey, as it still is today. 'So be it, LORD,' I said."
    },
    "6": {
      "L": "And the LORD said to me: Proclaim all these words in the cities of Judah and in the streets of Jerusalem, saying: Hear the words of this covenant and do them.",
      "M": "The LORD told me: Proclaim all these words in the towns of Judah and in the streets of Jerusalem: Hear the terms of this covenant and carry them out.",
      "T": "Then Yahweh told me: 'Go and proclaim these words in every city of Judah, in every street of Jerusalem: Hear the covenant. Keep the covenant.'"
    },
    "7": {
      "L": "For I earnestly warned your fathers when I brought them out of the land of Egypt, warning them persistently to this day, saying: Obey my voice.",
      "M": "For I repeatedly warned your ancestors when I brought them out of Egypt, warning them urgently right up to this day: Obey my voice.",
      "T": "From the moment I brought them out of Egypt I was warning them — again and again, persistently, right down to today: 'Obey my voice.'"
    },
    "8": {
      "L": "Yet they did not obey or incline their ear, but walked every one in the stubbornness of his evil heart. So I brought upon them all the words of this covenant which I commanded them to do and which they did not do.",
      "M": "Yet they did not listen or pay attention; each one followed the stubbornness of his evil heart. So I brought on them all the penalties of this covenant that I had commanded them to keep but that they refused to follow.",
      "T": "They would not listen. They would not bend. Every one of them followed the hardness of his own evil heart. So I brought down on them every penalty spelled out in the covenant — all the consequences they had been warned about and still ignored."
    },
    "9": {
      "L": "And the LORD said to me: A conspiracy is found among the men of Judah and the inhabitants of Jerusalem.",
      "M": "The LORD said to me: There is a conspiracy among the people of Judah and the inhabitants of Jerusalem.",
      "T": "Then Yahweh said to me: 'I have found a conspiracy — it is among the men of Judah, among the people of Jerusalem.'"
    },
    "10": {
      "L": "They have turned back to the iniquities of their forefathers who refused to hear my words; they have gone after other gods to serve them; the house of Israel and the house of Judah have broken my covenant that I made with their fathers.",
      "M": "They have returned to the sins of their ancestors who refused to listen to my words. They have followed other gods to serve them. Both the house of Israel and the house of Judah have violated the covenant I made with their ancestors.",
      "T": "They have turned back to the old sins of their ancestors who refused to hear my word. They are running after other gods to serve them. Both Israel and Judah have broken the covenant I made with their fathers — shattered it completely."
    },
    "11": {
      "L": "Therefore thus says the LORD: Behold, I will bring evil upon them which they shall not be able to escape; and though they shall cry out to me, I will not hearken to them.",
      "M": "Therefore this is what the LORD says: I am going to bring disaster on them that they cannot escape. Even when they cry out to me, I will not listen.",
      "T": "So Yahweh says: I am bringing disaster on them — unavoidable, inescapable. When they cry out to me, I will not hear them."
    },
    "12": {
      "L": "Then the cities of Judah and the inhabitants of Jerusalem shall go and cry out to the gods to whom they make offerings, but they shall not save them at all in the time of their trouble.",
      "M": "Then the towns of Judah and the people of Jerusalem will go and cry out to the gods they have been burning incense to — but those gods will not save them at all in the time of their trouble.",
      "T": "The cities of Judah and the people of Jerusalem will run to the gods they have been burning incense to. Let them cry out. Those gods will not save them. Not one."
    },
    "13": {
      "L": "For according to the number of your cities are your gods, O Judah; and according to the number of the streets of Jerusalem have you set up altars to the shameful thing — altars to burn incense to Baal.",
      "M": "For you have as many gods as you have cities, O Judah; and you have set up as many altars to the Shameful Thing — altars to burn incense to Baal — as there are streets in Jerusalem.",
      "T": "Look at the count, Judah: you have as many gods as cities. And every street of Jerusalem has its own altar to the Shameful Thing — to Baal. That is what you have built."
    },
    "14": {
      "L": "Therefore do not pray for this people, nor lift up a cry or prayer on their behalf, for I will not hear them in the time when they cry to me in their trouble.",
      "M": "Therefore do not pray for this people; do not raise a cry or prayer for them, for I will not listen when they cry out to me in the time of their distress.",
      "T": "'Do not pray for these people,' Yahweh told me. 'Do not plead or cry out on their behalf. When they call to me in their hour of disaster, I will not hear them.'"
    },
    "15": {
      "L": "What has my beloved to do in my house, when she has done vile deeds? Can the sacred offerings avert your disaster? Then you might well rejoice.",
      "M": "What claim does my beloved have in my house when she has done so many wicked things? Can sacrificial offerings remove your doom? You might as well rejoice in your evil.",
      "T": "What claim does my beloved have in my house now? All she has done is wickedness. Can she think that ritual sacrifice will forestall her doom? She might as well celebrate her evil for all the good it will do her."
    },
    "16": {
      "L": "The LORD called your name: A green olive tree, beautiful in form and with goodly fruit; with the noise of a great tumult he has set fire to it, and its branches are broken.",
      "M": "The LORD once called you a flourishing olive tree, beautiful with fine fruit; but with the roar of a violent storm he has kindled fire against it, and its branches are shattered.",
      "T": "Yahweh once gave you a name: 'A thriving olive tree, beautiful with good fruit.' But now, with a roaring and violent tempest, he has set fire to it — and the branches are breaking off."
    },
    "17": {
      "L": "And the LORD of hosts, who planted you, has pronounced disaster against you because of the evil that the house of Israel and the house of Judah have done, provoking me to anger by burning incense to Baal.",
      "M": "The LORD of hosts, who planted you, has pronounced disaster on you because of the evil that the house of Israel and the house of Judah have done — provoking me to anger by burning incense to Baal.",
      "T": "Yahweh of hosts — the very one who planted you — has pronounced this disaster on you, because of all the wickedness the houses of Israel and Judah have done, provoking his anger by burning offerings to Baal."
    },
    "18": {
      "L": "And the LORD made it known to me, and I knew; then you showed me their doings.",
      "M": "The LORD revealed it to me, and I knew; you opened my eyes to their actions.",
      "T": "Yahweh told me — and then I knew. He opened my eyes and showed me what they were doing."
    },
    "19": {
      "L": "But I was like a gentle lamb led to the slaughter; I knew not that they had devised schemes against me, saying: Let us destroy the tree with its fruit, and let us cut him off from the land of the living, that his name be remembered no more.",
      "M": "I had been like a gentle lamb led to slaughter. I did not know they had plotted against me, saying: Let us destroy the tree along with its fruit; let us cut him off from the land of the living, so that his name will be remembered no more.",
      "T": "I had been like an unsuspecting lamb led to slaughter — I did not know. They had been plotting behind my back: 'Let us cut down the tree with all its fruit. Let us wipe him out from the land of the living so that his very name disappears.'"
    },
    "20": {
      "L": "But, O LORD of hosts, who judges righteously, who tests the kidneys and the heart, let me see your vengeance upon them, for to you have I revealed my cause.",
      "M": "But, O LORD of hosts, you who judge justly and examine the innermost person, let me see your vengeance on them, for to you I have committed my cause.",
      "T": "But you, Yahweh of hosts, you judge with complete justice. You search the deepest recesses of a person — the thoughts, the desires. Let me see you vindicate me against them. I have placed my case entirely in your hands."
    },
    "21": {
      "L": "Therefore thus says the LORD concerning the men of Anathoth who seek your life, saying: Do not prophesy in the name of the LORD, or you will die by our hand —",
      "M": "Therefore this is what the LORD says about the men of Anathoth who are trying to kill you, who say: Stop prophesying in the name of the LORD, or we will kill you ourselves —",
      "T": "So Yahweh says this about the men of Anathoth — the men who want you dead, who tell you: 'Stop prophesying in the LORD's name, or we will kill you with our own hands' —"
    },
    "22": {
      "L": "Therefore thus says the LORD of hosts: Behold, I will punish them; the young men among them shall die by the sword; their sons and their daughters shall die by famine.",
      "M": "therefore this is what the LORD of hosts says: I am going to punish them. Their young men will die by the sword; their sons and daughters will die by famine.",
      "T": "Yahweh of hosts says: I will bring judgment on them. Their young men will fall by the sword; their sons and daughters will die of starvation."
    },
    "23": {
      "L": "And there shall be no remnant of them, for I will bring evil upon the men of Anathoth, even the year of their punishment.",
      "M": "There will be no survivors among them, for I will bring disaster on the men of Anathoth in the year of their reckoning.",
      "T": "Not one will survive. I will bring disaster on the men of Anathoth — in the very year of their reckoning."
    }
  },
  "12": {
    "1": {
      "L": "Righteous are you, O LORD, when I plead with you; yet I would speak with you concerning your judgments: Why does the way of the wicked prosper? Why do all who deal treacherously thrive?",
      "M": "You are righteous, LORD, when I bring a complaint to you; yet I want to argue my case before you. Why does the way of the wicked succeed? Why do all the treacherous flourish?",
      "T": "You are in the right, LORD — always — even when I bring a case against you. Still, I want to put my question: Why do the wicked thrive? Why does life go well for everyone who betrays their covenant obligations?"
    },
    "2": {
      "L": "You have planted them; they have also taken root; they grow; they bring forth fruit; you are near in their mouth and far from their heart.",
      "M": "You planted them, and they have taken root; they grow and produce fruit; yet you are near to their lips but far from their heart.",
      "T": "You planted them, and they have put down deep roots; they grow; they bear fruit. Your name is on their lips — but you are nowhere near their hearts."
    },
    "3": {
      "L": "But you, O LORD, know me; you see me, and you have tried my heart toward you; pull them out like sheep for the slaughter, and prepare them for the day of killing.",
      "M": "But you, LORD, know me; you see me; you have tested my heart, which is set toward you. Set them apart like sheep for slaughter; prepare them for the day of killing.",
      "T": "But you know me, LORD. You see everything about me. You have examined my heart and found it oriented toward you. Then pull them out like sheep headed for slaughter — set them apart for the day of the knife."
    },
    "4": {
      "L": "How long shall the land mourn and the herbs of every field wither? Because of the wickedness of those who dwell in it the beasts and birds are swept away, for they say: He shall not see our last end.",
      "M": "How long will the land mourn and the grass of every field dry up? Because of the wickedness of its inhabitants, the animals and birds have been swept away, for the people say: He will not see what becomes of us.",
      "T": "How long will the land lie in mourning, the crops of every field shriveling up? Because of the wickedness of those who live there, even the animals and birds are disappearing. And still they say, 'He does not see how this turns out.'"
    },
    "5": {
      "L": "If you have run with footmen and they have wearied you, then how will you contend with horses? And if in a land of peace you are so trusting, then what will you do in the swelling of the Jordan?",
      "M": "If you have raced against men on foot and have been worn out, how can you hope to compete with horses? And if you stumble in a peaceful country, how will you manage in the flooded thickets of the Jordan?",
      "T": "You have run with men on foot and worn yourself out — how do you expect to keep pace with horses? If you cannot hold your own in a quiet land, what will you do when the Jordan floods and the thicket rises? Hard days are ahead. Much harder days are coming."
    },
    "6": {
      "L": "For even your brothers and the house of your father, even they have dealt treacherously with you; even they have called a full cry after you; do not believe them, though they speak fair words to you.",
      "M": "Even your own brothers and your father's household have betrayed you; even they have raised a loud cry against you. Do not trust them, even when they speak kindly to you.",
      "T": "Your own brothers — your father's own household — have turned on you. They are the ones who raised the mob against you. Do not trust them, even when their words are smooth and their tone is gentle."
    },
    "7": {
      "L": "I have forsaken my house; I have abandoned my heritage; I have given the dearly beloved of my soul into the hand of her enemies.",
      "M": "I have abandoned my house; I have forsaken my inheritance; I have handed the one I deeply love over to her enemies.",
      "T": "I have walked out of my own house. I have left my inheritance behind. I have handed over the one most dear to me — given her over to her enemies."
    },
    "8": {
      "L": "My heritage is become to me as a lion in the forest; it crieth out against me; therefore have I hated it.",
      "M": "My heritage has become like a lion in the forest to me; she has raised her voice against me; therefore I have come to hate her.",
      "T": "My own inheritance has turned on me like a lion in the forest — roaring against me. That is why I have had to let her go."
    },
    "9": {
      "L": "Is my heritage a speckled bird of prey? Are birds of prey against her all around? Go, assemble all the beasts of the field; bring them to devour.",
      "M": "Is my heritage like a speckled bird of prey to me, with birds of prey all around attacking her? Go and gather all the wild animals; bring them to feed on her.",
      "T": "Has my inheritance become a strange, spotted bird — attacked from every side by every bird of prey? Then let all the wild animals come. I will call them in to devour her."
    },
    "10": {
      "L": "Many shepherds have destroyed my vineyard; they have trodden my portion underfoot; they have made my pleasant portion a desolate wilderness.",
      "M": "Many shepherds have ruined my vineyard; they have trampled my allotment; they have turned my beloved land into a barren wasteland.",
      "T": "Careless, self-serving leaders have ruined my vineyard. They have trampled the land I love into the ground and turned my precious portion into a desolate waste."
    },
    "11": {
      "L": "They have made it desolate; desolate it mourns to me; the whole land is made desolate, because no man lays it to heart.",
      "M": "They have made it a wasteland; it lies desolate before me in mourning. The whole land is laid waste, and no one takes it to heart.",
      "T": "They have left it completely desolate. It lies there mourning before me. The entire land is ruined — and no one cares. No one lets it break their heart."
    },
    "12": {
      "L": "The spoilers have come upon all bare heights through the wilderness, for the sword of the LORD devours from the one end of the land even to the other; no flesh shall have peace.",
      "M": "Across all the barren hilltops in the desert, invaders have come; the sword of the LORD devours from one end of the land to the other; no one has peace.",
      "T": "Across every barren ridge, invaders have swept through the wasteland. The sword of Yahweh is consuming this land from end to end. There is no peace for anyone."
    },
    "13": {
      "L": "They have sown wheat but shall reap thorns; they have put themselves to pain but shall not profit; and they shall be ashamed of their revenues because of the fierce anger of the LORD.",
      "M": "They planted wheat but harvested thorns; they wore themselves out for nothing. They will be ashamed of what they produced because of the burning anger of the LORD.",
      "T": "They planted wheat. They harvested thorns. They broke their backs for nothing. The shame of their ruined harvest comes from Yahweh's blazing anger."
    },
    "14": {
      "L": "Thus says the LORD against all my evil neighbors who touch the inheritance that I have caused my people Israel to inherit: Behold, I will pluck them up out of their land, and pluck out the house of Judah from among them.",
      "M": "This is what the LORD says against all my wicked neighbors who seize the inheritance I gave to my people Israel: I will uproot them from their land, and I will also uproot the house of Judah from among them.",
      "T": "This is what Yahweh says about all the wicked nations bordering his land — the ones who have seized the inheritance he gave to Israel: I will uproot them from their own lands. And I will uproot the house of Judah from among them as well."
    },
    "15": {
      "L": "And it shall come to pass, after that I have plucked them up, I will return and have compassion on them, and will bring them again every man to his heritage and every man to his land.",
      "M": "But after I have uprooted them, I will again have compassion on them and bring them back, each person to their own heritage and their own land.",
      "T": "But when I have uprooted them, I will turn back to them with compassion. I will bring each one home — to their own inheritance, their own land."
    },
    "16": {
      "L": "And it shall come to pass, if they will diligently learn the ways of my people, to swear by my name, saying, The LORD lives, as they taught my people to swear by Baal; then shall they be built up in the midst of my people.",
      "M": "And if they will diligently learn the ways of my people — to swear by my name, saying, As the LORD lives, just as they once taught my people to swear by Baal — then they will be established in the midst of my people.",
      "T": "And if they truly learn the ways of my people — if they swear by my name, 'As Yahweh lives,' in the same way they once taught my people to swear by Baal — then they too will be welcomed and built up among my people."
    },
    "17": {
      "L": "But if they will not hear, then will I utterly pluck up and destroy that nation, says the LORD.",
      "M": "But if any nation will not listen, I will completely uproot and destroy it, declares the LORD.",
      "T": "But any nation that will not listen — I will uproot it completely and destroy it. Yahweh declares it."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 10–12 written.')

if __name__ == '__main__':
    main()
