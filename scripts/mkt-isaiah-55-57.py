"""
MKT Isaiah chapters 55–57 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-55-57.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
  The divine personal name is surfaced in T throughout.
- H430 (אֱלֹהִים): "God" in all tiers throughout.
- H6918 (קָדוֹשׁ יִשְׂרָאֵל): "Holy One of Israel" — capitalised throughout Isaiah, consistent
  with prior scripts. Appears at 55:5; 57:15 has a standalone "Holy" as a divine name-descriptor.
- H6635 (צְבָאוֹת): does not appear significantly in these chapters.
- H5315 (נֶפֶשׁ): 55:2,3 — rendered "soul" (L) / the embodied self/appetite sense. In 55:2 it
  means the whole person's inner appetite ("delight yourselves"); in 55:3 "your soul shall live"
  means the whole person, not an immaterial soul. M and T render as "yourselves / you will live."
- H2617 (חֶסֶד): 55:3 — "the steadfast, sure mercies of David." This phrase (ḥasdê dāwid
  hanne'emānîm) is one of the most important in Isa 40–55: the Davidic covenant faithfulness
  now offered to all. L: "sure mercies of David"; M: "sure mercies I promised to David";
  T: "all the sure and steadfast love I showed David." Acts 13:34 quotes this in a
  resurrection-of-Jesus context; T does not add NT gloss but preserves the full covenantal weight.
  Appears also at 57:1 as H2617 alone ("faithful men" / men of ḥesed) — rendered "faithful men"
  (L/M) / "men of faithful love" (T).
- H1285 (בְּרִית): "covenant" in all tiers — 55:3; 56:4,6.
- H7676 (שַׁבָּת): "sabbath" in all tiers — 56:2,4,6. Capitalised since it is the proper
  institution name.
- H5631 (סָרִיס): "eunuch" — 56:3,4. Retained: the inclusion of eunuchs (physically excluded by
  Deut 23:1 from the assembly) is a deliberate reversal of Mosaic law in the eschatological age.
  T preserves the term rather than softening.
- H5236 (נֵכָר): "foreigner" (L/M) / "foreigner" (T) — 56:3,6. Same term throughout.
- H8605 (תְּפִלָּה): "prayer" in all tiers — 56:7. The verse "my house shall be called a house
  of prayer for all peoples" is quoted by Jesus at the Temple cleansing (Mark 11:17). T does not
  add NT gloss; the universal scope ("all peoples") is already in the Hebrew.
- H7307 (רוּחַ): 57:13 — "wind" (lower case); 57:15 — "spirit" (lower case in L; "Spirit" could
  be defended but the context is human contrite spirit, not divine Spirit); 57:16 — "spirit" with
  "breath of life" (the created breath/spirit God made). All lower case throughout ch. 57.
- H6664/H6666 (צֶדֶק/צְדָקָה): "righteousness" (L/M). T uses "right" or "righteous purpose"
  where the saving-vindication sense is primary (56:1 "my righteousness is about to be revealed";
  57:12 "your righteousness" = the idolatrous deeds Israel calls righteous).
- H4941 (מִשְׁפָּט): "justice" (L/M) / "justice" (T) — 56:1.
- H7563 (רָשָׁע): "wicked" in all tiers — 57:20,21. The closing refrain "There is no peace for
  the wicked" repeats 48:22 exactly, marking the structural end of the second major unit of
  Isa 40–57. T keeps the refrain terse.
- H7965 (שָׁלוֹם): "peace" in all tiers — 55:12; 57:2,19(×2),21.
- H1697 (דָּבָר): "word" — 55:11. This is the Hebrew dabar, parallel in function to the Greek
  logos: the effective, creative speech of God. L: "my word"; M: "my word"; T: "my word —"
  with emphasis on its going-out and not returning empty.
- H5057 (נָגִיד): "leader/prince" — 55:4, rendered "leader and commander" following the paired
  nouns (nāgîd and mĕṣawweh = commander). David as the paradigm shifts in v.5 to Zion/the people
  calling unknown nations to themselves.
- H4791/H5375 (מָרוֹם/נָשָׂא): "high and lofty One" — 57:15. This is one of the most majestic
  divine self-descriptions in all of Isaiah. L: "the high and lofty One"; M: same; T: preserves
  the cadence with line breaks. The paradox is that this same transcendent God also dwells with
  the contrite and lowly — T honours the structural paradox without flattening.
- H1793/H1792 (דַּכָּה/דָּכָא): "contrite" — 57:15. Both words in v.15 mean crushed, ground down,
  humiliated. L/M: "contrite"; T: "crushed" in second occurrence to register the physical force of
  the root, and "contrite" in the first (more spiritualised) occurrence.
- Structural notes:
  Ch. 55 — The climactic invitation of Isa 40–55: water, food, wine and milk freely given (vv. 1–5).
  The section on divine transcendence (vv. 8–9) and the parable of the effective word (vv. 10–11)
  conclude the theological argument of the whole "Book of Comfort." The chapter ends with the
  jubilant new exodus (vv. 12–13), echoing the promise of 40:3–5 and 52:11–12.
  Ch. 56 — A sharp structural hinge: the universal invitation previously offered (chs. 40–55) is
  now grounded in covenant practice (vv. 1–8), then immediately undercut by an oracle against
  the corrupt leaders who should be gatekeepers but are instead blind, sleeping, greedy dogs
  (vv. 9–12). The contrast is deliberate and jarring.
  Ch. 57 — Continues the judgment oracle against corrupt leaders and idolaters (vv. 1–13), with
  a closing reversal oracle of comfort for the humble and contrite (vv. 14–21). The chapter ends
  with the closing refrain of Isa 48:22 repeated verbatim, marking the structural end of the
  "Servant" unit (chs. 40–57). T uses line breaks extensively in the poetic oracles (vv. 6–15).
- Aspect notes:
  55:1–5 imperatives: "come," "buy," "eat," "hear" — present imperatives, urgent and open-ended.
  55:10–11 simile: the rain/snow verb sequence is in perfect aspect (completed, reliable process)
  followed by imperfects for the word of God (ongoing, certain future). L preserves the flow.
  55:12–13 futures: "you shall go out / the trees shall clap" — confident prophetic futures.
  56:1 "my salvation is coming" — qārôb (near/about to come) + imperfect = imminent action.
  57:1 perfects: "the righteous perishes / are taken away" — completed acts viewed as typical
  ongoing pattern; M treats them as generalised present facts.
  57:15–19: the long divine speech shifts from statives ("I dwell") to perfects of past act
  ("I saw / I struck") to confident futures ("I will heal / I will lead"). All tiers honour the
  shift from declaration to history to promise.
- OT echoes:
  55:1 — Echoes Prov 9:5 (Wisdom's invitation to her feast) and prefigures John 7:37
  (Jesus's "If anyone thirsts, let him come to me"). T does not add NT gloss; the invitation
  stands on its own terms.
  55:3 — "sure mercies of David" (ḥasdê dāwid hanne'emānîm) is echoed in Acts 13:34 by Paul,
  applied to the resurrection of Jesus as the fulfilment of the Davidic covenant promise.
  55:10–11 — The word going out and not returning empty has been described as the most
  concentrated statement of divine-speech efficacy in the Hebrew Bible; parallels Ps 147:15–18.
  56:7 — "house of prayer for all peoples" echoes the universalist thrust of 1 Kgs 8:41–43
  (Solomon's prayer for the foreigner at the Temple). Jesus's cleansing of the Temple (Mark 11:17)
  is a direct quotation of this verse.
  57:14 — "Prepare the way" echoes 40:3 (the opening cry of Isa 40–55), creating an inclusio.
  57:19 — "Peace to him who is far and peace to him who is near" is echoed in Eph 2:17
  (Paul applying it to Jew and Gentile). T does not apply the NT reading but preserves the
  full scope ("far and near" likely encompasses Diaspora Jews and eventually Gentiles).
  57:21 — Repeats 48:22 verbatim, closing the structural unit.
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
  "55": {
    "1": {
      "L": "Ho! Everyone who thirsts, come to the waters; and he who has no money, come, buy and eat! Come, buy wine and milk without money and without price.",
      "M": "Come, all who are thirsty — come to the waters; and you who have no money, come, buy and eat! Come, buy wine and milk without money and without cost.",
      "T": "Come — come to the water,\nevery one who thirsts!\nYou with no money — come!\nBuy and eat!\nCome — buy wine and milk\nwithout money, without cost."
    },
    "2": {
      "L": "Why do you spend your money for that which is not bread, and your labor for that which does not satisfy? Listen diligently to me, and eat what is good, and let your soul delight itself in richness.",
      "M": "Why do you spend money on what is not bread, and your wages on what does not satisfy? Listen carefully to me, eat what is good, and let yourselves enjoy the richest fare.",
      "T": "Why trade your silver for what is not bread —\nyour wages for what leaves you empty?\nListen — listen to me.\nEat what is good.\nLet your whole self delight in the richest feast."
    },
    "3": {
      "L": "Incline your ear, and come to me; hear, and your soul shall live; and I will make with you an everlasting covenant, the steadfast, sure mercies of David.",
      "M": "Incline your ear and come to me; hear, and you will live; and I will make an everlasting covenant with you — the sure mercies I promised to David.",
      "T": "Lean in and come to me.\nListen — and you will live.\nI will make an everlasting covenant with you:\nall the sure and steadfast love I showed David —\nthat is what I am offering you now."
    },
    "4": {
      "L": "Behold, I made him a witness to the peoples, a leader and commander for the peoples.",
      "M": "See, I made him a witness to the nations, a leader and commander for the peoples.",
      "T": "I made David a witness to the nations — a prince and commander set over the peoples."
    },
    "5": {
      "L": "Behold, you shall call a nation you do not know, and a nation that did not know you shall run to you, because of the LORD your God, and of the Holy One of Israel, for he has glorified you.",
      "M": "See, you will summon a nation you did not know, and a nation that did not know you will run to you, because of the LORD your God and the Holy One of Israel, for he has glorified you.",
      "T": "You will call a nation you never knew, and nations that never knew you will come running — because of Yahweh your God, because of the Holy One of Israel, who has crowned you with honor."
    },
    "6": {
      "L": "Seek the LORD while he may be found; call upon him while he is near.",
      "M": "Seek the LORD while he may be found; call on him while he is near.",
      "T": "Seek Yahweh while he may be found.\nCall on him while he is still near."
    },
    "7": {
      "L": "Let the wicked forsake his way, and the unrighteous man his thoughts; let him return to the LORD, that he may have compassion on him, and to our God, for he will abundantly pardon.",
      "M": "Let the wicked forsake his way and the unrighteous man his thoughts; let him return to the LORD, who will have compassion on him, and to our God, who will abundantly pardon.",
      "T": "Let the wicked man leave his road.\nLet the unrighteous man abandon his schemes.\nLet him return to Yahweh — who will have compassion on him —\nto our God, who pardons with open hands."
    },
    "8": {
      "L": "For my thoughts are not your thoughts, neither are your ways my ways, declares the LORD.",
      "M": "For my thoughts are not your thoughts, and your ways are not my ways, declares the LORD.",
      "T": "My thoughts are not your thoughts.\nMy ways are not your ways —\nYahweh declares it."
    },
    "9": {
      "L": "For as the heavens are higher than the earth, so are my ways higher than your ways and my thoughts than your thoughts.",
      "M": "For as the heavens are higher than the earth, so are my ways higher than your ways and my thoughts higher than your thoughts.",
      "T": "As the heavens tower over the earth,\nso my ways tower over your ways —\nmy thoughts over your thoughts."
    },
    "10": {
      "L": "For as the rain and the snow come down from heaven and do not return there but water the earth, making it bring forth and sprout, giving seed to the sower and bread to the eater,",
      "M": "For as the rain and the snow come down from heaven and do not return there until they have watered the earth, making it sprout and bear fruit, giving seed to the farmer and bread to the one who eats,",
      "T": "As the rain and the snow fall from the sky\nand do not go back up\nuntil they have watered the earth —\nuntil it has budded and sprouted,\nuntil it gives seed to the farmer\nand bread to the hungry —"
    },
    "11": {
      "L": "so shall my word be that goes out from my mouth; it shall not return to me void, but it shall accomplish that which I please, and shall prosper in the thing for which I sent it.",
      "M": "so shall my word be that goes out from my mouth; it shall not return to me empty, but it shall accomplish what I intend, and succeed in what I send it to do.",
      "T": "so my word — going out of my mouth —\nwill not return to me empty.\nIt will accomplish what I intend.\nIt will succeed in what I send it to do."
    },
    "12": {
      "L": "For you shall go out with joy and be led forth with peace; the mountains and the hills shall break forth before you into singing, and all the trees of the field shall clap their hands.",
      "M": "For you will go out with joy and be led forth in peace; the mountains and the hills shall burst into song before you, and all the trees of the field shall clap their hands.",
      "T": "You will leave with joy.\nYou will be led out in peace.\nThe mountains and hills will break into singing before you,\nand all the trees of the field will clap their hands."
    },
    "13": {
      "L": "Instead of the thorn shall come up the cypress; instead of the brier shall come up the myrtle; and it shall be to the LORD for a name, for an everlasting sign that shall not be cut off.",
      "M": "Instead of the thorn the cypress shall come up, and instead of the brier the myrtle shall come up; and it shall be a memorial to the LORD, an everlasting sign that will never be cut off.",
      "T": "Where thorns grew — cypress will rise.\nWhere briers spread — myrtle will bloom.\nIt will be a name for Yahweh,\nan everlasting sign that will never be cut off."
    }
  },
  "56": {
    "1": {
      "L": "Thus says the LORD: Keep justice, and do righteousness, for soon my salvation will come, and my deliverance will be revealed.",
      "M": "Thus says the LORD: Maintain justice and do what is right, for my salvation is coming soon, and my righteousness is about to be revealed.",
      "T": "Yahweh says this: Keep justice. Do what is right. My salvation is about to arrive — my righteousness is on the verge of being revealed."
    },
    "2": {
      "L": "Blessed is the man who does this, and the son of man who holds it fast, who keeps the sabbath, not profaning it, and keeps his hand from doing any evil.",
      "M": "Blessed is the man who does this, and the person who holds to it — who keeps the sabbath without profaning it and refrains from doing any evil.",
      "T": "Blessed is the one who does this — the person who holds to it firm: who keeps the sabbath and does not violate it, who keeps his hands back from every evil."
    },
    "3": {
      "L": "Let not the foreigner who has joined himself to the LORD say, 'The LORD will surely separate me from his people'; and let not the eunuch say, 'Behold, I am a dry tree.'",
      "M": "Let not the foreigner who has joined himself to the LORD say, 'The LORD will surely exclude me from his people'; and let not the eunuch say, 'I am a withered tree.'",
      "T": "The foreigner who has joined himself to Yahweh should not say, 'Yahweh will surely cut me off from his people.' The eunuch should not say, 'I am a dry and withered tree.'"
    },
    "4": {
      "L": "For thus says the LORD: To the eunuchs who keep my sabbaths, who choose the things that please me and hold fast my covenant,",
      "M": "For thus says the LORD: To the eunuchs who keep my sabbaths, who choose what pleases me and hold fast to my covenant —",
      "T": "For Yahweh says this: To the eunuchs who keep my sabbaths, who choose what I delight in and hold fast to my covenant —"
    },
    "5": {
      "L": "I will give in my house and within my walls a memorial and a name better than sons and daughters; I will give them an everlasting name that shall not be cut off.",
      "M": "I will give them, within my house and within my walls, a memorial and a name better than sons and daughters; I will give them an everlasting name that will never be cut off.",
      "T": "I will give them — within my house, within my walls — a place and a name better than sons and daughters. I will give them an everlasting name that will never be cut off."
    },
    "6": {
      "L": "And the foreigners who join themselves to the LORD, to minister to him, to love the name of the LORD, and to be his servants, everyone who keeps the sabbath and does not profane it, and holds fast my covenant —",
      "M": "And the foreigners who join themselves to the LORD, to serve him, to love the name of the LORD, and to be his servants — everyone who keeps the sabbath without profaning it and holds fast my covenant —",
      "T": "And the foreigners who join themselves to Yahweh — to serve him, to love the name of Yahweh, to be his servants — everyone who keeps the sabbath and does not profane it, who holds fast my covenant —"
    },
    "7": {
      "L": "even them I will bring to my holy mountain, and make them joyful in my house of prayer; their burnt offerings and their sacrifices will be accepted on my altar; for my house shall be called a house of prayer for all peoples.",
      "M": "even them I will bring to my holy mountain and make them glad in my house of prayer; their burnt offerings and sacrifices will be accepted on my altar; for my house shall be called a house of prayer for all peoples.",
      "T": "I will bring them to my holy mountain and fill them with joy in my house of prayer. Their burnt offerings and sacrifices will be welcomed on my altar. My house will be called a house of prayer for all peoples."
    },
    "8": {
      "L": "The Lord GOD, who gathers the outcasts of Israel, declares: I will gather yet others to him besides those already gathered.",
      "M": "The Lord GOD, who gathers the outcasts of Israel, declares: I will gather yet others to him besides those already gathered to him.",
      "T": "The Lord Yahweh — who gathers the scattered of Israel — says: I will gather still more to him, beyond those already brought in."
    },
    "9": {
      "L": "All you beasts of the field, come to devour — all you beasts in the forest.",
      "M": "All you wild animals of the field, come to devour — all you beasts of the forest.",
      "T": "Come, all you wild beasts of the field — come and feed. Come, all you beasts of the forest."
    },
    "10": {
      "L": "His watchmen are blind; they are all without knowledge; they are all dumb dogs; they cannot bark; dreaming, lying down, loving to slumber.",
      "M": "Israel's watchmen are all blind; none of them understand; they are all silent dogs that cannot bark — they dream, lie down, and love to sleep.",
      "T": "His watchmen are all blind. None of them understand. They are all silent dogs — they cannot bark. They dream, they lounge, they love to sleep."
    },
    "11": {
      "L": "The dogs are greedy; they can never have enough; the shepherds themselves have no understanding; they have all turned to their own way, each to his own gain, one and all.",
      "M": "The dogs are ravenous; they are never satisfied; the shepherds have no understanding; they have all gone their own way, each after his own profit, every last one of them.",
      "T": "The dogs are insatiable — never enough. These shepherds have no understanding. Every one of them has gone his own way, chasing his own profit from his own direction."
    },
    "12": {
      "L": "Come, let me get wine; let us fill ourselves with strong drink; and tomorrow will be like today, great beyond measure.",
      "M": "Come, they say, let us get wine; let us fill ourselves with strong drink; and tomorrow will be like today, even more abundant.",
      "T": "Come, they say — let us get wine. Let us fill ourselves with beer. And tomorrow? Tomorrow will be just like today. Even better."
    }
  },
  "57": {
    "1": {
      "L": "The righteous man perishes, and no one lays it to heart; faithful men are taken away, and no one understands. For the righteous man is taken away from calamity;",
      "M": "The righteous man perishes, and no one takes it to heart; faithful men are taken away, and no one understands. The righteous man is taken away from the evil to come;",
      "T": "The righteous perish — and no one gives it a thought. Men of faithful love are taken away, and no one understands. The righteous man is being removed from the evil that is coming;"
    },
    "2": {
      "L": "he enters into peace; they rest in their beds, each one who walked in his uprightness.",
      "M": "he enters into peace; they rest in their resting places, each one who walked uprightly.",
      "T": "he enters into peace — he rests in his resting place — each one who walked in uprightness."
    },
    "3": {
      "L": "But as for you, draw near here, sons of the sorceress, offspring of the adulterer and the loose woman.",
      "M": "But you — come here, you children of the sorceress, offspring of the adulterer and the prostitute.",
      "T": "But you — come here, children of the sorceress, seed of the adulterer and the harlot."
    },
    "4": {
      "L": "Against whom are you making sport? Against whom do you open your mouth wide and stick out your tongue? Are you not children of transgression, the offspring of deceit?",
      "M": "Whom are you mocking? Against whom do you open your mouth wide and stick out your tongue? Are you not children of rebellion, the offspring of lies?",
      "T": "Who is it you are mocking? At whom do you stretch your mouth wide and stick out your tongue? You are children of rebellion — offspring of deceit."
    },
    "5": {
      "L": "You who burn with lust among the oaks, under every green tree, who slaughter children in the valleys, under the clefts of the rocks?",
      "M": "You who inflame yourselves among the trees, under every leafy tree, who slaughter children in the ravines, under the crevices of the rocks?",
      "T": "You who inflame yourselves with idols beneath every leafy tree — who slaughter children in the ravines, under the crevices of the rocks?"
    },
    "6": {
      "L": "Among the smooth stones of the valley is your portion; they, they are your lot; to them you have poured out a drink offering, you have brought a grain offering. Shall I relent for these things?",
      "M": "Your lot is among the smooth stones of the streambeds; they are your portion; you have poured out drink offerings to them and brought grain offerings. Should I be appeased by these things?",
      "T": "The smooth stones of the ravine — those are your portion.\nYour lot.\nTo them you have poured your drink offerings;\nto them you have brought your grain.\nShould I relent because of these things?"
    },
    "7": {
      "L": "On a high and lofty mountain you have set your bed; you went up there to offer sacrifice.",
      "M": "On a high and lofty mountain you set your bed; you went up there to offer sacrifice.",
      "T": "On a high and lofty mountain you made your bed —\nyou went up there to sacrifice."
    },
    "8": {
      "L": "Behind the door and the doorpost you have set up your memorial; for, away from me, you uncovered yourself; you went up and made your bed wide; you made a bargain with them; you loved their bed; you looked upon nakedness.",
      "M": "Behind the door and the doorpost you placed your memorial — for away from me you uncovered yourself; you went up and spread your bed wide; you struck a deal with them; you loved their bed and looked upon what was exposed.",
      "T": "Behind the door and the doorpost you put up your memorials.\nFor you turned from me — you uncovered yourself.\nYou went up and spread your bed wide.\nYou struck your bargain with them.\nYou loved their bed;\nyou gazed on what was exposed."
    },
    "9": {
      "L": "You journeyed to the king with oil and multiplied your perfumes; you sent your envoys far off, and sent them down even to Sheol.",
      "M": "You traveled to the king with oil and multiplied your fragrances; you sent your messengers far off, even down to Sheol.",
      "T": "You went to the king with oil\nand heaped up your perfumes.\nYou sent your envoys far off —\nall the way down to Sheol."
    },
    "10": {
      "L": "You were weary with the length of your way, but you did not say, 'It is hopeless'; you found new life for your strength, and so you were not faint.",
      "M": "You grew weary from your many journeys, but you did not say, 'It is hopeless'; you found renewed strength, and so you were not weak.",
      "T": "You wore yourself out with all your wandering,\nbut you never said, 'There is no hope.'\nYou found renewed strength —\nso you kept going, not faint."
    },
    "11": {
      "L": "Whom did you fear and dread, so that you lied, and did not remember me, nor set it to your heart? Have I not been silent even for a long time, and so you do not fear me?",
      "M": "Whom did you fear and dread, that you lied and did not remember me, nor call it to mind? Was it not because I was silent and looked away that you have not feared me?",
      "T": "Who was it you feared — who terrified you — that you lied and forgot me,\nnever turning a thought to me?\nWas it because I kept silent so long\nthat you stopped fearing me?"
    },
    "12": {
      "L": "I will proclaim your righteousness and your deeds, but they will not profit you.",
      "M": "I will expose your righteousness and your deeds — but they will not benefit you.",
      "T": "I will announce your righteousness — all your deeds.\nThey will not help you."
    },
    "13": {
      "L": "When you cry out, let your collection of idols deliver you! The wind will carry them all off; a breath will take them away. But he who takes refuge in me shall possess the land and inherit my holy mountain.",
      "M": "When you cry out, let your collection of idols rescue you! The wind will carry them all off; a breath will sweep them away. But whoever takes refuge in me will possess the land and inherit my holy mountain.",
      "T": "Cry out then — let your crowd of idols save you!\nThe wind will carry them all away;\na single breath will scatter them.\nBut the one who takes refuge in me —\nhe will possess the land;\nhe will inherit my holy mountain."
    },
    "14": {
      "L": "And it shall be said, 'Build up, build up, prepare the road; remove the obstacle from the road of my people.'",
      "M": "A voice will say: 'Build up, build up, prepare the way; clear every obstruction from the road for my people.'",
      "T": "A voice will say: Build up, build up — prepare the road!\nClear every stumbling block from the way for my people."
    },
    "15": {
      "L": "For thus says the high and lofty One who inhabits eternity, whose name is Holy: I dwell in the high and holy place, and also with him who is of a contrite and lowly spirit, to revive the spirit of the lowly, and to revive the heart of the contrite.",
      "M": "For thus says the One who is high and lifted up, who inhabits eternity, whose name is Holy: I dwell in the high and holy place, and also with the one who has a contrite and humble spirit, to revive the spirit of the humble and to revive the heart of the contrite.",
      "T": "For the high and lofty One says this —\nthe one who inhabits eternity,\nwhose name is Holy:\nI live in the high and holy place —\nand also with the one who is crushed and lowly in spirit,\nto revive the spirit of the lowly,\nto revive the heart of the contrite."
    },
    "16": {
      "L": "For I will not contend forever, nor will I always be angry; for the spirit would grow faint before me, and the breath of life that I made.",
      "M": "For I will not contend forever, nor will I be angry forever; for the spirit would faint before me, and the breath of life that I have created.",
      "T": "I will not strive forever,\nnor will I always be angry —\nfor the spirit would give out before me:\nthe very breath of life I created."
    },
    "17": {
      "L": "Because of the iniquity of his unjust gain I was angry; I struck him; I hid my face and was angry; but he went on backsliding in the way of his own heart.",
      "M": "Because of the iniquity of his greed I was angry; I struck him; I hid my face and was angry — but he kept going, backsliding along the way of his own heart.",
      "T": "I was angry because of his greedy iniquity.\nI struck him.\nI hid my face — I was angry.\nAnd yet he kept going,\nbacksliding along the road of his own heart."
    },
    "18": {
      "L": "I have seen his ways, but I will heal him; I will lead him and restore comfort to him and his mourners,",
      "M": "I have seen his ways, yet I will heal him; I will lead him and restore comfort to him and to those who mourn with him —",
      "T": "I have seen his ways — and I will heal him.\nI will lead him and restore comfort to him,\nto him and to those who mourn with him —"
    },
    "19": {
      "L": "creating the fruit of the lips. Peace, peace, to the far and to the near, says the LORD, and I will heal him.",
      "M": "creating the fruit of the lips. Peace, peace, to the far and to the near, says the LORD, and I will heal them.",
      "T": "creating the fruit of the lips:\nPeace — peace to the far and to the near —\nYahweh says it —\nand I will heal them."
    },
    "20": {
      "L": "But the wicked are like the tossing sea; for it cannot be quiet, and its waters toss up mire and dirt.",
      "M": "But the wicked are like the churning sea, for it cannot be still, and its waters stir up mire and mud.",
      "T": "But the wicked are like the sea in a storm —\nit cannot be still.\nIts waters churn up mire and mud."
    },
    "21": {
      "L": "There is no peace, says my God, for the wicked.",
      "M": "There is no peace, says my God, for the wicked.",
      "T": "There is no peace for the wicked — my God says it."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 55–57 written.')

if __name__ == '__main__':
    main()
