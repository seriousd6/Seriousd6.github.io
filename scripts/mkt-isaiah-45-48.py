"""
MKT Isaiah chapters 45–48 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-45-48.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts;
  the divine personal name is surfaced in T throughout this unit.
- H430 (אֱלֹהִים): "God" in all tiers — context is monotheistic declaration throughout chs. 45–48.
- H4899 (מָשִׁיחַ): 45:1 — "his anointed" in all tiers. Cyrus is the only non-Israelite in
  scripture called meshiach. T preserves the full weight of the title without interpretation.
- H6635 (צְבָאוֹת): "of hosts" — cosmic sovereignty marker, consistent with all prior Isaiah scripts.
  Appears at 45:13; 47:4; 48:2.
- H6918 (קָדוֹשׁ יִשְׂרָאֵל): "Holy One of Israel" — capitalised throughout Isaiah, consistent
  with prior scripts. Appears at 45:11; 47:4; 48:17.
- H7307 (רוּחַ): 48:16 — "his Spirit" — the closing clause ("the Lord GOD has sent me, and his Spirit")
  is rendered with capital S in all tiers; this is a theologically charged moment and the ambiguity
  is preserved rather than flattened. Some interpreters read the final clause as the Servant speaking
  (anticipating Isa 49–53); T notes this implicitly with its rendering of the voice shift.
- H5315 (נֶפֶשׁ): does not appear with significance in these chapters.
- H2617 (חֶסֶד): does not appear in these chapters.
- H7451 (רַע): 45:7 — "calamity" (L) / "disaster" (M/T). In this cosmological context the word
  denotes physical/historical catastrophe, not moral evil; using "evil" here would mislead.
  Isaiah is asserting that even destructive events are within Yahweh's sovereign order, not attributing
  moral evil to God.
- H6664 (צֶדֶק) / H6666 (צְדָקָה): "righteousness" (L/M); T uses "saving right" or "righteous
  purpose" where the covenantal-vindicating sense is prominent (45:8, 45:13, 46:13).
- H3468 (יֶשַׁע) / H3444 (יְשׁוּעָה): "salvation" (L/M); T varies between "salvation" and
  "rescue/deliverance" depending on whether the communal-eschatological or immediate-historical
  sense is primary.
- H1078 (בֵּל) / H5015 (נְבוֹ): "Bel" and "Nebo" — transliterated, not translated. These are
  the chief Babylonian deities. Their ironic bowing/stooping in 46:1 is the structural pivot of ch. 46.
- Structural notes:
  Ch. 45 — The great Cyrus oracle (vv. 1–7) leads into a creation-theology section (vv. 8–13) and
  then the universal monotheism declaration (vv. 14–25), climaxing at v. 22 ("Turn to me and be saved,
  all the ends of the earth") and v. 23 ("every knee shall bow"). Paul quotes v. 23 in Romans 14:11
  and Philippians 2:10–11 in a Christ-application context; T preserves the universal scope without
  narrowing it to a NT frame.
  Ch. 46 — A tight contrast poem: Bel and Nebo fall (vv. 1–2) vs. the God who carries his people
  (vv. 3–4). The idols are burdens; Yahweh is the carrier. Short, punchy verses; T honours the
  epigrammatic quality throughout.
  Ch. 47 — A taunt song against Babylon, the only sustained "lament over a city" oracle in Isaiah.
  Structured as courtroom-humiliation scene (vv. 1–5) → accusation (vv. 6–7) → ironic pride exposed
  (vv. 8–9) → divine counter (vv. 10–11) → sorcery mocked (vv. 12–15). This chapter is substantially
  poetry throughout; T uses full line-break treatment for every verse.
  Ch. 48 — Address to stubborn Israel as the unit closes; explains the pedagogical function of the
  Babylonian captivity. The chapter ends with a double-movement: summons to exodus (vv. 20–21) and
  the refrain "no peace for the wicked" (v. 22), closing the whole Babylon-section before the
  Servant Songs of ch. 49.
- 48:16 voice-shift note: Verse 48:16 contains an abrupt switch to first-person speech ("the Lord GOD
  has sent me, and his Spirit"). This is widely understood as either the prophet identifying himself
  or — more importantly for the structure of Isa 40–55 — the Servant of the LORD beginning to speak,
  anticipating the Servant Songs of chs. 49–53. All three tiers preserve the text as-is; T's phrasing
  ("And now the Lord Yahweh has sent me, and his Spirit") keeps the theological weight open.
- Aspect notes:
  45:1–7 verbs: futures rendered as confident futures (Yahweh's word is as good as done).
  45:22–23 "Turn to me" — present imperative; "every knee shall bow" — the sworn word makes it
  prophetic perfect = "will certainly bow."
  46:10–11 "I have spoken / I will bring it to pass" — Yahweh's speaking and accomplishing are
  in parallel; the past speaking guarantees the future fulfillment.
  47 verbs: a mix of imperatives (address to Babylon) and indicatives (the judgment announced);
  T distinguishes them clearly throughout.
  48:3 "suddenly I acted" — the waw-consecutive narrative past honored by all tiers.
- OT echoes:
  45:7 "I form light and create darkness" — echoes Gen 1:2–3; Yahweh is the creator of all, including
  the darkness Cyrus will penetrate in 45:3.
  45:23 "every knee shall bow, every tongue shall swear" — echoes the enthronement Psalms (Ps 2, 22,
  72); Paul's use in Rom 14:11 and Phil 2:10–11 is a deliberate extension. T does not add NT gloss.
  47:1 "sit in the dust" — reversal of Babylon's 47:8 ("I sit as queen"); the imagery inverts
  Babylon's self-description. T makes the irony explicit in the later verses.
  48:18 "peace like a river, righteousness like the waves" — the counterfactual vision of what
  could have been; this image recurs at 66:12 as a future promise, completing the arc. T uses the
  flowing imagery fully in both places.
  48:20–21 "Go out from Babylon... he made water flow from the rock" — the new exodus motif; the
  desert-water miracle of Exod 17:6 and Num 20:11 is invoked as the pattern for the return from
  Babylon. T surfaces this explicitly.
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
  "45": {
    "1": {
      "L": "Thus says the LORD to his anointed, to Cyrus, whose right hand I have grasped, to subdue nations before him and to loosen the belts of kings, to open doors before him so that gates shall not be closed:",
      "M": "Thus says the LORD to Cyrus, his anointed, whose right hand he has grasped to subdue nations before him and strip kings of their armor — to throw open doors before him so that gates shall not be shut:",
      "T": "Yahweh says this to Cyrus — his anointed, his chosen instrument — the one whose right hand Yahweh himself has taken hold of, to flatten nations before him and strip kings of their defenses, to throw open every door so that no gate stays shut:"
    },
    "2": {
      "L": "I will go before you and level the mountains; the gates of bronze I will break in pieces, and the bars of iron I will cut through.",
      "M": "I will go before you and make the rough places smooth; I will break the gates of bronze in pieces and cut through the bars of iron.",
      "T": "I will march before you and level every obstacle. Bronze gates — I will shatter them. Iron bars — I will cut through them."
    },
    "3": {
      "L": "I will give you the treasures of darkness and the hoards hidden in secret places, so that you may know that it is I, the LORD, the God of Israel, who calls you by your name.",
      "M": "I will give you the treasures stored in darkness and the wealth hoarded in secret places, so that you may know that I, the LORD, am the God of Israel who has called you by name.",
      "T": "I will hand you the treasures stashed away in darkness, the riches hidden in secret vaults — all so that you may come to know that I, Yahweh, the God of Israel, am the one who called you by name."
    },
    "4": {
      "L": "For the sake of Jacob my servant, and Israel my chosen, I called you by your name; I gave you a title of honor, though you did not know me.",
      "M": "For the sake of my servant Jacob, and Israel my chosen, I called you by your name; I gave you a title of honor, though you did not know me.",
      "T": "I did it for the sake of Jacob my servant — for Israel my chosen. I called you by name, I gave you your title — though you had no knowledge of me at all."
    },
    "5": {
      "L": "I am the LORD, and there is no other; besides me there is no God. I girded you, though you did not know me,",
      "M": "I am the LORD, and there is no other; besides me there is no God. I equipped you, though you did not know me,",
      "T": "I am Yahweh, and there is no other. No god exists beside me. I armed you for this — though you never knew me —"
    },
    "6": {
      "L": "so that from the rising of the sun and from its setting they may know that there is none besides me; I am the LORD, and there is no other.",
      "M": "so that from the rising of the sun to where it sets, people may know there is no one besides me; I am the LORD, and there is no other.",
      "T": "so that from sunrise to sunset every people on earth may come to know there is no one beside me. I am Yahweh — and there is no other."
    },
    "7": {
      "L": "I form light and create darkness; I make peace and create calamity; I, the LORD, do all these things.",
      "M": "I form light and create darkness; I make peace and create disaster; I, the LORD, do all these things.",
      "T": "I shape light and create darkness; I make peace and bring disaster. I, Yahweh, do all these things."
    },
    "8": {
      "L": "Rain down, you heavens, from above, and let the skies pour down righteousness; let the earth open up, and let salvation spring up, and let righteousness sprout forth also; I, the LORD, have created it.",
      "M": "Rain down, O heavens, from above, and let the skies pour down righteousness; let the earth open up and salvation spring forth, and let righteousness grow up with it; I, the LORD, have created it.",
      "T": "Rain down from above, O heavens — let the skies shower righteousness. Let the earth open wide and salvation spring up; let righteousness spring up alongside it. I, Yahweh, have created all of this."
    },
    "9": {
      "L": "Woe to him who strives with his Maker — a potsherd among potsherds of the earth! Does the clay say to the one who forms it, 'What are you making?' or 'Your work has no handles?'",
      "M": "Woe to him who quarrels with his Maker — a mere potsherd among potsherds of earth! Does the clay say to the one who shapes it, 'What are you making?' or 'Your work has no handles?'",
      "T": "Woe to the one who fights with the one who made him — a clay shard demanding answers from other shards. Does the clay interrogate the potter: 'What do you think you're making?' or 'You left it without handles'?"
    },
    "10": {
      "L": "Woe to him who says to a father, 'What are you begetting?' or to a woman, 'What are you giving birth to?'",
      "M": "Woe to him who says to a father, 'What are you fathering?' or to a woman, 'What are you in labor with?'",
      "T": "Woe to the one who demands of a father, 'Why are you having this child?' or says to a woman in labor, 'Why are you giving birth to this?'"
    },
    "11": {
      "L": "Thus says the LORD, the Holy One of Israel, and the one who formed him: Will you question me about my children, or give me orders about the work of my hands?",
      "M": "Thus says the LORD, the Holy One of Israel, and his Maker: Will you question me about my children, or give me orders about the work of my hands?",
      "T": "Yahweh says this — the Holy One of Israel, the one who formed him: 'Are you going to interrogate me about my own children? Are you going to issue orders about what my hands have made?'"
    },
    "12": {
      "L": "I made the earth and created man upon it; it was my hands that stretched out the heavens, and I commanded all their host.",
      "M": "I made the earth and created mankind upon it; with my own hands I stretched out the heavens, and I commanded all their starry host.",
      "T": "I made this earth. I created humanity on it. With these hands I stretched out the sky, and I issued the command that set every star in its place."
    },
    "13": {
      "L": "I have stirred him up in righteousness, and I will make all his ways level; he shall build my city and set my exiles free, not for price or reward, says the LORD of hosts.",
      "M": "I have stirred him up in righteousness, and I will make all his paths straight; he shall build my city and set my exiles free — not for price or reward, declares the LORD of hosts.",
      "T": "I roused Cyrus in my own righteous purpose, and I will level every road before him. He will rebuild my city and release my exiles — not for payment, not for a bribe. Yahweh of hosts says so."
    },
    "14": {
      "L": "Thus says the LORD: The labor of Egypt and the merchandise of Cush, and the Sabeans, men of stature, shall come over to you and be yours; they shall follow you; they shall come over in chains and bow down to you; they shall plead with you, saying, 'Surely God is in you, and there is no other, no god besides him.'",
      "M": "Thus says the LORD: The wealth of Egypt and the merchandise of Cush, and the Sabeans — tall men — shall come over to you and be yours; they shall follow you; they shall come over in chains and bow down to you, pleading, 'Surely God is in you, and there is no other, no god besides him.'",
      "T": "Yahweh says: Egypt's wealth and the trade of Cush, and the tall men of Seba — they will all come over to you, yours by right. They will walk behind you in chains, bowing down, and plead: 'Surely God is with you — and there is no one else, no other god at all.'"
    },
    "15": {
      "L": "Truly you are a God who hides himself, O God of Israel, the Savior.",
      "M": "Truly you are a God who conceals himself, O God of Israel, the Savior.",
      "T": "You are indeed a God who hides himself — O God of Israel, the one who saves."
    },
    "16": {
      "L": "They are put to shame and also confounded, all of them; together they go into confusion, the makers of idols.",
      "M": "They are all put to shame and confounded; together all the makers of idols go off in disgrace.",
      "T": "They are all shamed and humiliated, together. Every maker of idols walks away in disgrace."
    },
    "17": {
      "L": "But Israel is saved by the LORD with everlasting salvation; you shall not be put to shame or confounded to ages everlasting.",
      "M": "But Israel is saved by the LORD with an everlasting salvation; you will not be ashamed or confounded for ages everlasting.",
      "T": "But Israel — Israel is saved by Yahweh with a salvation that lasts forever. You will never again be ashamed or humiliated — not for ages without end."
    },
    "18": {
      "L": "For thus says the LORD, who created the heavens — he is God — who formed the earth and made it, who established it; he did not create it a waste, he formed it to be inhabited: I am the LORD, and there is no other.",
      "M": "For thus says the LORD, who created the heavens — he is God — who formed the earth and made it, who established it and did not create it a chaos but formed it to be inhabited: I am the LORD, and there is no other.",
      "T": "For Yahweh says this — the one who created the heavens (he is God), the one who shaped the earth and made it, who set it in place, who did not create it as a void but formed it to be lived in: I am Yahweh, and there is no other."
    },
    "19": {
      "L": "I did not speak in secret, in a land of darkness; I did not say to the offspring of Jacob, 'Seek me in vain.' I the LORD speak truth; I declare what is right.",
      "M": "I did not speak in secret, in a land of darkness; I did not say to the offspring of Jacob, 'Seek me in a waste.' I, the LORD, speak truth; I declare things that are right.",
      "T": "I never spoke in secret, from some dark hidden place. I never told Jacob's children, 'Look for me in the void.' I, Yahweh, speak what is true; I declare what is right."
    },
    "20": {
      "L": "Assemble yourselves and come; draw near together, you survivors of the nations; they have no knowledge who carry about their wooden idols and keep on praying to a god that cannot save.",
      "M": "Assemble and come; draw near together, you survivors of the nations. Those who carry around their wooden idols and pray to a god that cannot save have no understanding.",
      "T": "Come together and gather — draw near, all you who survived among the nations. Those who lug wooden idols around and pray to gods that cannot save — they are without understanding."
    },
    "21": {
      "L": "Declare and present your case; let them take counsel together. Who told this long ago? Who declared it of old? Was it not I, the LORD? And there is no other god besides me — a righteous God and a Savior; there is none besides me.",
      "M": "Declare your case and present your arguments; let them consult together. Who foretold this from long ago? Who declared it from of old? Was it not I, the LORD? There is no other god besides me — a God who is righteous and saves; there is none besides me.",
      "T": "State your case. Bring your evidence. Let the nations put their heads together. Who announced this beforehand? Who proclaimed it long ago? Was it not I, Yahweh? There is no other god beside me — a God who is both righteous and saving. No one else."
    },
    "22": {
      "L": "Turn to me and be saved, all the ends of the earth! For I am God, and there is no other.",
      "M": "Turn to me and be saved, all the ends of the earth! For I am God, and there is no other.",
      "T": "Turn to me — be saved, every corner of the earth. I am God, and there is no other."
    },
    "23": {
      "L": "By myself I have sworn; from my mouth has gone out in righteousness a word that shall not return: 'To me every knee shall bow, every tongue shall swear.'",
      "M": "I have sworn by myself; a righteous word has gone out from my mouth, and it will not turn back: 'To me every knee shall bow, every tongue shall swear allegiance.'",
      "T": "I have sworn by my own name — and the righteous word that left my mouth will not return empty: every knee will bow to me, every tongue will swear its allegiance."
    },
    "24": {
      "L": "Only in the LORD, it shall be said of me, are righteousness and strength; to him shall come and be ashamed all who were incensed against him.",
      "M": "Only in the LORD, it will be said, are righteousness and strength; all who were angry with him will come to him and be ashamed.",
      "T": "'Only in Yahweh,' they will say, 'is there righteousness and power.' Everyone who raged against him will come to him — and find themselves ashamed."
    },
    "25": {
      "L": "In the LORD all the offspring of Israel shall be justified and shall glory.",
      "M": "In the LORD all the offspring of Israel shall be found righteous and shall exult.",
      "T": "In Yahweh — in Yahweh alone — all the descendants of Israel will be made right, and they will boast in him."
    }
  },
  "46": {
    "1": {
      "L": "Bel bows down; Nebo stoops; their idols are on beasts and livestock; the things you carry are loaded as burdens on weary animals.",
      "M": "Bel bows down; Nebo stoops; their idols are loaded onto animals and cattle; the things you bear are burdens on exhausted beasts.",
      "T": "Bel falls to his knees; Nebo crumbles. Their images are strapped onto animals, loaded onto oxen — the gods you carry have become a load too heavy for exhausted beasts."
    },
    "2": {
      "L": "They stoop and bow down together; they cannot save the burden, but themselves go into captivity.",
      "M": "They stoop and bow down together; they cannot save the load — they themselves go into captivity.",
      "T": "They collapse together — gods going down with the rest. They cannot save the very load they are. They too go into captivity."
    },
    "3": {
      "L": "Hear me, O house of Jacob, all the remnant of the house of Israel, who have been carried from before birth, borne from the womb,",
      "M": "Listen to me, O house of Jacob, and all the remnant of the house of Israel, you who have been carried since before birth, borne since the womb,",
      "T": "Listen to me, house of Jacob — all the remaining ones of the house of Israel — you whom I have been carrying since before you were born, lifting since the womb,"
    },
    "4": {
      "L": "even to your old age I am he, and to gray hairs I will carry you. I have made, and I will bear; I will carry and will save.",
      "M": "even to your old age I am he, and even to gray hairs I will carry you. I have made you, and I will sustain you; I will carry you and save you.",
      "T": "even when you are old — I am the one. Even when your hair is white, I will carry you. I made you; I will carry you. I will hold you up and bring you safe through."
    },
    "5": {
      "L": "To whom will you liken me and make me equal, and compare me, that we may be alike?",
      "M": "To whom will you compare me and make me equal, and liken me, that we may be alike?",
      "T": "Who is my equal? Who can you put beside me? Name one who compares."
    },
    "6": {
      "L": "Those who lavish gold from the purse and weigh out silver in the scales hire a goldsmith, and he makes it into a god; they fall down and worship.",
      "M": "Those who pour out gold from their purses and weigh out silver in the scales hire a goldsmith, who makes it into a god; then they fall down and worship it.",
      "T": "They pour out gold from their pouches, weigh silver on the scale, and hire a goldsmith to hammer it into a god — then fall flat on their faces to worship it."
    },
    "7": {
      "L": "They lift it to their shoulder, they carry it, they set it in its place, and it stands there; it cannot move from its place. If one cries to it, it does not answer or save him from his trouble.",
      "M": "They hoist it onto their shoulder, they carry it and set it in its place, and there it stands; it cannot move from its spot. If someone cries out to it, it gives no answer and rescues no one from trouble.",
      "T": "They heave it up on their shoulders, lug it into the house, set it down — and there it stays. It cannot take a single step. Cry out to it — silence. It cannot deliver anyone from anything."
    },
    "8": {
      "L": "Remember this and stand firm; bring it back to mind, you transgressors.",
      "M": "Remember this and stand firm; bring it to mind, you rebels.",
      "T": "Take note of this. Hold it firm. Let it come back to you, every one of you who has turned away."
    },
    "9": {
      "L": "Remember the former things of old; for I am God, and there is no other; I am God, and there is none like me,",
      "M": "Remember the former things of long ago; for I am God, and there is no other; I am God, and there is none like me,",
      "T": "Remember what happened long before — I am God and there is no other. I am God, and nothing is like me —"
    },
    "10": {
      "L": "declaring the end from the beginning and from ancient times things not yet done, saying, 'My counsel shall stand, and I will accomplish all my purpose,'",
      "M": "declaring the end from the beginning, and from ancient times things not yet done, saying, 'My plan shall stand, and I will carry out my purpose,'",
      "T": "I declared the end before the beginning even happened. I announced things not yet done, from ancient times. My purpose will stand. I will do everything I intend."
    },
    "11": {
      "L": "calling a bird of prey from the east, the man of my purpose from a far country. I have spoken, and I will bring it to pass; I have purposed, and I will do it.",
      "M": "calling a bird of prey from the east, the man of my purpose from a far country. I have spoken, and I will bring it about; I have planned, and I will do it.",
      "T": "I called a bird of prey from the east — the man I have chosen, from a distant land. I said it — I will bring it to pass. I purposed it — I will carry it out."
    },
    "12": {
      "L": "Hear me, you who are stubborn of heart, you who are far from righteousness:",
      "M": "Listen to me, you stubborn of heart, you who are far from righteousness:",
      "T": "Listen to me, you hardened ones — you who have stayed far from righteousness:"
    },
    "13": {
      "L": "I bring near my righteousness; it is not far off; and my salvation will not delay; I will put salvation in Zion, for Israel my glory.",
      "M": "I am bringing my righteousness near — it is not far off — and my salvation will not linger; I will put salvation in Zion, for Israel my glory.",
      "T": "I am bringing my righteous purpose close — it is not distant. My salvation will not dawdle. I am planting salvation in Zion, my glory in Israel."
    }
  },
  "47": {
    "1": {
      "L": "Come down and sit in the dust, O virgin daughter of Babylon; sit on the ground without a throne, O daughter of the Chaldeans! For you shall no more be called tender and delicate.",
      "M": "Come down and sit in the dust, O virgin daughter of Babylon; sit on the ground without a throne, O daughter of the Chaldeans! For you will no longer be called tender and delicate.",
      "T": "Come down — sit in the dust,\nO virgin daughter of Babylon.\nSit on the ground, with no throne —\nO daughter of the Chaldeans.\nYou will never again be called\ntender and delicate."
    },
    "2": {
      "L": "Take the millstones and grind flour; remove your veil, strip off your robe, uncover your leg, pass through the rivers.",
      "M": "Take the millstones and grind flour; remove your veil, take off your robe, bare your legs, and wade through the rivers.",
      "T": "Seize the millstones and grind your own grain.\nPull off your veil.\nStrip off your fine robe.\nBare your legs — wade through the rivers."
    },
    "3": {
      "L": "Your nakedness shall be uncovered, and your shame shall be seen. I will take vengeance, and I will spare no one.",
      "M": "Your nakedness shall be exposed, and your disgrace shall be visible. I will take vengeance, and I will not relent.",
      "T": "Your nakedness will be exposed;\nyour shame will be seen.\nI will take vengeance.\nI will spare no one."
    },
    "4": {
      "L": "Our Redeemer — the LORD of hosts is his name — the Holy One of Israel.",
      "M": "(Our Redeemer — the LORD of hosts is his name — the Holy One of Israel.)",
      "T": "(Our Redeemer —\nYahweh of hosts is his name —\nthe Holy One of Israel.)"
    },
    "5": {
      "L": "Sit in silence and go into darkness, O daughter of the Chaldeans; for you shall no more be called the mistress of kingdoms.",
      "M": "Sit in silence and go into darkness, O daughter of the Chaldeans; for you will no longer be called the mistress of kingdoms.",
      "T": "Sit in silence.\nGo into the dark,\nO daughter of the Chaldeans.\nNever again will anyone call you\nthe mistress of kingdoms."
    },
    "6": {
      "L": "I was angry with my people; I profaned my heritage; I gave them into your hand; you showed them no mercy; on the aged you made your yoke very heavy.",
      "M": "I was angry with my people; I desecrated my heritage; I handed them over to you; but you showed them no mercy; on the elderly you laid a very heavy yoke.",
      "T": "I was angry with my people.\nI gave away my own inheritance —\nhanded them to you.\nBut you showed them no mercy.\nOn the old and frail\nyou laid your heaviest yoke."
    },
    "7": {
      "L": "You said, 'I shall be mistress forever,' so that you did not lay these things to heart or remember their end.",
      "M": "You said, 'I will be mistress forever,' so that you did not take these things to heart or consider how it would end.",
      "T": "You said, 'I will be mistress forever.' So you never gave a thought to any of this — never considered how it might end."
    },
    "8": {
      "L": "Now therefore hear this, you lover of pleasures, who sit securely, who say in your heart, 'I am, and there is none besides me; I shall not sit as a widow or know the loss of children':",
      "M": "Now therefore hear this, you lover of pleasures, who sit so securely, who say in your heart, 'I am, and there is no one besides me; I will never sit as a widow or know the loss of children':",
      "T": "So hear this now,\nyou pleasure-drunk one,\nyou who sit so secure —\nyou who say in your heart,\n'I am, and there is no one but me.\nI will never be a widow.\nI will never lose my children.'"
    },
    "9": {
      "L": "These two things shall come to you in a moment, in one day: loss of children and widowhood — they shall come upon you in full measure, in spite of your many sorceries and the great power of your enchantments.",
      "M": "Both of these things shall come upon you in a moment, in a single day: loss of children and widowhood — they shall come on you in full, despite your many sorceries and the great power of your spells.",
      "T": "Both of these\nshall come on you in a single moment —\nin one day:\nloss of children and widowhood,\ncoming upon you in full force —\nfor all your spells,\nfor all the power of your enchantments."
    },
    "10": {
      "L": "You trusted in your wickedness; you said, 'No one sees me'; your wisdom and your knowledge led you astray, and you said in your heart, 'I am, and there is none besides me.'",
      "M": "You trusted in your wickedness; you said, 'No one sees me'; your wisdom and your knowledge led you astray, and you said in your heart, 'I am, and there is no one besides me.'",
      "T": "You felt safe in your wickedness.\nYou told yourself: 'No one can see me.'\nYour cleverness and your knowledge\ncorrupted you —\nand you said in your heart,\n'I am, and there is no one else.'"
    },
    "11": {
      "L": "But evil shall come upon you, which you will not know how to charm away; disaster shall fall upon you, for which you will not be able to atone; and ruin shall come upon you suddenly, of which you know nothing.",
      "M": "But evil shall come upon you, which you will not know how to conjure away; disaster shall fall on you, which you will be powerless to avert; and ruin shall come upon you suddenly, which you never saw coming.",
      "T": "But disaster will come upon you —\nno spell can drive it away.\nCalamity will fall on you —\nyou will not know how to buy it off.\nRuin will come on you suddenly,\nout of nowhere."
    },
    "12": {
      "L": "Stand fast in your enchantments and your many sorceries, with which you have labored from your youth; perhaps you may be able to profit; perhaps you may inspire terror.",
      "M": "Stand by your enchantments and your many sorceries, which you have practiced since your youth; perhaps you will succeed; perhaps you can inspire fear.",
      "T": "Stand by your spells then —\nall those enchantments\nyou have practiced since you were young.\nPerhaps they will do you some good.\nPerhaps they will actually frighten someone."
    },
    "13": {
      "L": "You are wearied with your many counsels; let them stand forth and save you, those who divide the heavens, who gaze at the stars, who at the new moons make known what shall come upon you.",
      "M": "You are worn out by all your advisers; let them stand up and save you — those who divide the sky, who gaze at the stars, who at each new moon predict what will happen to you.",
      "T": "You have worn yourself out\nwith all your advisers.\nLet them step up and rescue you —\nthe sky-dividers,\nthe star-gazers,\nthe ones who, month by month,\nclaim to know what is coming."
    },
    "14": {
      "L": "Behold, they are like stubble; the fire consumes them; they cannot deliver themselves from the power of the flame. This is no coal for warming, no fire to sit before.",
      "M": "Look — they are like straw; the fire devours them; they cannot save themselves from the power of the flame. There is no coal for warmth, no fire to sit by.",
      "T": "Look at them — they are stubble.\nThe fire will consume them.\nThey cannot save themselves\nfrom the power of the flames —\nno coal left for warmth,\nno fire to huddle around."
    },
    "15": {
      "L": "Such shall they be to you — those with whom you have labored, who have traded with you from your youth; they each wander off in their own direction; there is no one to save you.",
      "M": "Such are those you have dealt with, who have been your trading partners since your youth; they each go off in their own direction; there is no one to save you.",
      "T": "That is what becomes of them —\nall those you did business with,\nyour trading partners since you were young.\nEach one turns and goes his own way.\nNo one saves you. No one."
    }
  },
  "48": {
    "1": {
      "L": "Hear this, O house of Jacob, who are called by the name of Israel, and who came from the waters of Judah, who swear by the name of the LORD and confess the God of Israel — but not in truth or right.",
      "M": "Hear this, O house of Jacob — those who are called by the name of Israel and came from the waters of Judah — who swear by the name of the LORD and invoke the God of Israel, but not in sincerity or truth.",
      "T": "Hear this, house of Jacob — you who bear the name of Israel, who came from the line of Judah — you who invoke the name of Yahweh and call on the God of Israel, but not in truth, not from the heart."
    },
    "2": {
      "L": "For they call themselves after the holy city, and lean upon the God of Israel; the LORD of hosts is his name.",
      "M": "For they call themselves after the holy city and claim to rest on the God of Israel; the LORD of hosts is his name.",
      "T": "You call yourselves people of the holy city. You claim to lean on the God of Israel — whose name is Yahweh of hosts."
    },
    "3": {
      "L": "The former things I declared of old; they went out from my mouth and I announced them; then suddenly I acted, and they came to pass.",
      "M": "The former things I declared long ago; they went out from my mouth and I proclaimed them; then suddenly I acted, and they came to pass.",
      "T": "Long ago I announced the former things. They came out of my mouth; I proclaimed them. Then I acted — suddenly — and they happened."
    },
    "4": {
      "L": "Because I knew that you are obstinate, and your neck is an iron sinew and your forehead brass,",
      "M": "Because I knew that you are stubborn, and your neck is an iron muscle and your forehead bronze,",
      "T": "Because I knew you — how stubborn you are. Your neck is an iron cable. Your forehead is bronze."
    },
    "5": {
      "L": "I declared it to you from of old; before it came to pass I announced it to you, lest you should say, 'My idol did these things, my carved image and my metal image commanded them.'",
      "M": "I announced it to you from long ago; before it happened I proclaimed it to you, so that you could not say, 'My idol did these things, my carved image and my cast idol commanded them.'",
      "T": "That is why I told you everything beforehand — before it happened, I proclaimed it — so you could never say, 'My idol made all this happen. My carved image, my cast metal god, gave the orders.'"
    },
    "6": {
      "L": "You have heard; now see all this; and will you not declare it? From this time I announce to you new things, hidden things you have not known.",
      "M": "You have heard; now look at all this; and will you not declare it? From now on I announce to you new things, hidden things that you have not known.",
      "T": "You have heard it. Now see it. Will you not say so? From this moment I am announcing new things — things hidden, things you have never known."
    },
    "7": {
      "L": "They are created now, not long ago; before today you have never heard of them, lest you should say, 'Behold, I knew them.'",
      "M": "They are being created now, not long ago; before today you had never heard of them, so that you cannot say, 'Yes, I knew that already.'",
      "T": "They are being created right now — not long ago. Before today you had never heard of them. I will not let you say, 'I knew this all along.'"
    },
    "8": {
      "L": "You have never heard; you have never known; from of old your ear was not opened. For I knew that you would deal very treacherously, and that you were called a rebel from birth.",
      "M": "You have not heard, you have not known; from of old your ear has not been opened. For I knew that you would surely betray me, and that you have been called a rebel since before you were born.",
      "T": "You never heard; you never knew; from the beginning your ear was shut. I knew it — I knew how treacherous you would be. You were called a rebel even before you came into the world."
    },
    "9": {
      "L": "For my name's sake I defer my anger; for the sake of my praise I restrain it for you, that I may not cut you off.",
      "M": "For the sake of my name I hold back my anger; for my own honor I restrain it for your sake, so that I do not cut you off.",
      "T": "For the sake of my own name I hold my anger back. For the sake of my own reputation I restrain myself — so that I do not wipe you out."
    },
    "10": {
      "L": "Behold, I have refined you, but not as silver; I have tried you in the furnace of affliction.",
      "M": "See, I have refined you, but not as silver is refined; I have tested you in the furnace of affliction.",
      "T": "Look — I have refined you, but not like silver. I have tested you in the furnace of affliction."
    },
    "11": {
      "L": "For my own sake, for my own sake, I do it, for how should my name be profaned? My glory I will not give to another.",
      "M": "For my own sake, for my own sake, I act — for how could my name be profaned? My glory I will not share with another.",
      "T": "For my own sake — for my own sake — I act. How could I let my name be dragged through the mud? I will not give my glory to anyone else."
    },
    "12": {
      "L": "Hear me, O Jacob, and Israel, whom I called; I am he; I am the first; I am also the last.",
      "M": "Listen to me, O Jacob, and Israel, whom I called: I am he; I am the first; I am also the last.",
      "T": "Listen, Jacob — Israel, whom I called — listen to me. I am the one. I am the first. I am the last."
    },
    "13": {
      "L": "My hand laid the foundation of the earth, and my right hand spread out the heavens; when I call to them, they stand forth together.",
      "M": "My hand laid the foundation of the earth, and my right hand spread out the heavens; when I summon them, they take their stand together.",
      "T": "This hand laid the foundation of the earth. This right hand spread out the heavens. When I call out to them, they stand at attention — every one of them."
    },
    "14": {
      "L": "Assemble, all of you, and hear! Who among them has declared these things? The LORD loves him; he shall perform his purpose against Babylon, and his arm shall be against the Chaldeans.",
      "M": "Assemble together and hear! Which of their idols declared these things? The LORD loves him; he shall carry out his will against Babylon, and his power shall be against the Chaldeans.",
      "T": "Gather and listen, all of you. Which of those gods declared any of this? Yahweh loves Cyrus — he will carry out Yahweh's will against Babylon, and his arm will strike the Chaldeans."
    },
    "15": {
      "L": "I, even I, have spoken; yes, I have called him; I have brought him, and he will prosper in his way.",
      "M": "I, even I, have spoken; I have called him; I have brought him; and he will succeed in his mission.",
      "T": "I — I myself — have spoken it. I called him. I brought him. And he will succeed in everything I sent him to do."
    },
    "16": {
      "L": "Draw near to me, hear this: from the beginning I have not spoken in secret; from the time it came to be I was there. And now the Lord GOD has sent me, and his Spirit.",
      "M": "Draw near to me, hear this: I did not speak in secret from the beginning; from the time it came to be, I was there. And now the Lord GOD has sent me, and his Spirit.",
      "T": "Come close and hear this: I never spoke from hiding — from the moment things were set in motion, I was there. And now the Lord Yahweh has sent me, and his Spirit."
    },
    "17": {
      "L": "Thus says the LORD, your Redeemer, the Holy One of Israel: I am the LORD your God, who teaches you to profit, who leads you in the way you should go.",
      "M": "Thus says the LORD, your Redeemer, the Holy One of Israel: 'I am the LORD your God, who teaches you what is good for you, who directs you in the way you should go.'",
      "T": "Yahweh says this — your Redeemer, the Holy One of Israel: 'I am Yahweh your God. I teach you what truly benefits you. I lead you in the way you should walk.'"
    },
    "18": {
      "L": "Oh, that you had paid attention to my commandments! Then your peace would have been like a river, and your righteousness like the waves of the sea;",
      "M": "If only you had listened to my commandments! Then your peace would have been like a river, and your righteousness like the waves of the sea;",
      "T": "If only you had listened to my commandments — then your peace would be flowing like a river, your righteousness surging like the ocean's waves;"
    },
    "19": {
      "L": "your offspring would have been like the sand, and your descendants like its grains; their name would never be cut off or destroyed before me.",
      "M": "your descendants would have been like the sand, and your children like its grains; their name would never have been cut off or blotted out from before me.",
      "T": "your children would be as numberless as grains of sand; their name would never be cut off, never erased from my sight."
    },
    "20": {
      "L": "Go out from Babylon, flee from Chaldea; declare this with a shout of joy, proclaim it, send it out to the end of the earth; say, 'The LORD has redeemed his servant Jacob.'",
      "M": "Go out from Babylon, flee from Chaldea; declare this with a cry of joy, proclaim it, let it go out to the ends of the earth; say, 'The LORD has redeemed his servant Jacob!'",
      "T": "Go out from Babylon! Flee from Chaldea! Shout it with joy — proclaim it — send the word to the farthest corner of the earth: 'Yahweh has redeemed his servant Jacob!'"
    },
    "21": {
      "L": "And they were not thirsty when he led them through the deserts; he made water flow from the rock for them; he split the rock and the waters gushed out.",
      "M": "They did not thirst when he led them through the deserts; he made water flow from the rock for them; he split the rock and water gushed out.",
      "T": "They were not thirsty when he led them through the desert. He made water come from the rock — he cracked it open and it poured out."
    },
    "22": {
      "L": "There is no peace, says the LORD, for the wicked.",
      "M": "There is no peace, says the LORD, for the wicked.",
      "T": "There is no peace for the wicked — Yahweh says it."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 45–48 written.')

if __name__ == '__main__':
    main()
