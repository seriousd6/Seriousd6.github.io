"""
MKT Jeremiah chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-4-6.py

Translation decisions (carried forward from mkt-jeremiah-1-3.py unless noted):
- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name force is
  significant — especially in oracle-introduction formulas and direct-address passages.
- H430 (אֱלֹהִים): "God" in all tiers throughout.
- H1697 (דָּבָר): "word" in all tiers — the prophetic-word formula is load-bearing theologically.
- H7307 (רוּחַ): In 4:11–12 clearly a meteorological sirocco wind — "wind" (lower case) in all
  tiers. In 5:13 "the prophets shall become wind" — metaphorical, lower case. No divine-Spirit
  occurrence in these chapters.
- H5315 (נֶפֶשׁ): Context-sensitive:
    4:10 "reacheth unto the soul" → "to the very soul/life" — the sword penetrates to the core;
    4:19 "O my soul" → prophet's embodied self in anguish; L "my soul"; T "my whole being";
    5:9, 5:29 "shall not my soul be avenged" → divine self/desire for justice; T "shall I not
      take my due";
    6:8 "lest my soul depart" → divine revulsion turning away; T "lest I turn from you in
      revulsion."
- H4941 (מִשְׁפָּט): "justice/judgment" — context-sensitive: legal usage → "justice"; general
  "ordinance/requirement" → "requirements of their God."
- H7965 (שָׁלוֹם): 6:14 (and refrain in 8:11) "Peace, peace" — L/M: "Peace, peace"; T: "All
  is well, all is well" — to capture the false-optimism register while avoiding the theological
  weight-word "peace" in a context of empty reassurance.
- H7451 (רָעָה): context-sensitive — "evil" for moral wickedness; "disaster/calamity" for
  divine judgment-event coming from the north (consistent with JER-1-3).
- H4878 (מְשׁוּבָה): "backsliding" (L); "faithlessness/turning away" (M/T) — a key Jeremiah
  term first established in chs 1–3; rendered here as "turnings away" (5:6) for variety.
- H2181 (זָנָה): 5:7 "committed adultery" in the context of spiritual unfaithfulness; L: "committed
  adultery"; T: surfaces the covenant-betrayal dimension explicitly.
- H8414 + H922 (תֹּהוּ וָבֹהוּ): 4:23 — direct verbatim echo of Genesis 1:2; L: "without form
  and void" (preserving the KJV formula known to readers); M: "formless and void"; T: adds
  explanatory cadence: "waste and void — the chaos of creation undone." The de-creation vision
  in 4:23–26 is the most powerful literary echo in these chapters — Jeremiah sees the cosmos
  returning to pre-creation chaos as divine judgment. T must give it full weight.
- H1820 (דָּמָה) in 6:2: Textual crux — KJV renders "I have likened the daughter of Zion to a
  comely and delicate woman" but BHS and most modern scholars read the verb as "I will destroy /
  cut off" (cognate to Arabic and Ugaritic). Given the siege context (vv. 3–6), the sense of
  destruction fits better. L/M follow the destruction reading; T makes it explicit.
- H6726 (צִיּוֹן): "Zion" / "Daughter Zion" unchanged throughout.
- H3389 (יְרוּשָׁלַם): "Jerusalem" unchanged.
- H3063 (יְהוּדָה): "Judah" unchanged.
- H3478 (יִשְׂרָאֵל): "Israel" unchanged.
- H6635 (צְבָאוֹת): "LORD of Armies" / "LORD of hosts" — carried from prior scripts; T "Yahweh
  of Armies" for 6:6 where the military context is explicit.

OT echo and NT resonance notes:
- 4:4 "circumcise your hearts" — the metaphor of inner covenant transformation anticipates Deut
  10:16; 30:6; Jer 31:33 (new covenant); Rom 2:29; Phil 3:3. T surfaces the inner-transformation
  register.
- 4:23–26 "without form and void" (תֹּהוּ וָבֹהוּ) — the single most charged intertextual echo
  in these chapters. Jeremiah describes the land returned to Edenic formlessness as judgment; the
  fruitful place becomes wilderness, every city in ruins. The repetition "I looked" (four times)
  creates a prophetic walkthrough of de-creation. T gives each vision its own line.
- 5:1 — The search for one just person echoes Genesis 18:22–32 (Abraham's intercession for
  Sodom). Where Abraham bargained down to ten righteous, here Yahweh needs only one — but
  cannot find even that. The stakes are inverted.
- 5:22 — The divine boundary-setter of the sea anticipates Job 38:8–11; Ps 104:9. The creation-
  order appeal grounds the covenant lawsuit: the God who orders nature also orders history.
- 5:24 — "former and latter rain" — the agricultural cycle as covenant blessing (Deut 11:14;
  28:12). Withholding rain is covenant curse (Deut 28:23–24). NT echo: James 5:7 uses the same
  harvest-rain image.
- 6:14 — "Peace, peace, when there is no peace" — perhaps the most quoted line in Jeremiah;
  repeated at 8:11. The false prophets' easy reassurance against Jeremiah's costly warnings
  becomes a touchstone for discerning false prophecy. NT echo: 1 Thess 5:3 ("when they say
  'Peace and safety'").
- 6:16 — "Stand at the crossroads and ask for the ancient paths" — a key wisdom-call that
  anticipates Jeremiah's theology of covenant memory. The "rest for your souls" language is
  quoted by Jesus in Matt 11:29 ("you will find rest for your souls").
- 6:29–30 — The metallurgical image of rejected silver (dross that cannot be refined) provides
  the chapter's closing verdict on Judah's irreformability. The same image underlies Ezek 22:18–
  22 and Mal 3:2–3 (refiner's fire). T renders "reprobate silver" as "dross silver" — the
  technical by-product of failed smelting that gets discarded.

Structural notes:
  Ch. 4 — Two movements: call to repentance (vv. 1–4) → the invasion unleashed (vv. 5–31).
    The invasion section moves through trumpet-alarm (vv. 5–8), leadership panic (v. 9), prophetic
    protest (v. 10), the hot wind of judgment (vv. 11–12), the enemy's speed (vv. 13–18), the
    prophet's personal anguish (vv. 19–22), and the de-creation vision (vv. 23–26), closing with
    the divine word and the harlot-city image (vv. 27–31). The prophet's anguish in vv. 19–22
    is one of the most psychologically penetrating passages in the OT; T must preserve its urgency.
  Ch. 5 — The covenant lawsuit continued: the failed search (vv. 1–9), the vine metaphor
    (vv. 10–13), divine fire in the prophet's mouth (v. 14), the enemy from afar (vv. 15–17),
    the catechism of covenant (vv. 18–25), the human trappers (vv. 26–29), the appalling state
    of prophets and priests (vv. 30–31).
  Ch. 6 — The siege oracle: alarm calls (vv. 1–8), the gleaning of the vine (vv. 9–15), the
    crossroads call (vv. 16–17), cosmic summons of nations as witnesses (vv. 18–21), the terrible
    army from the north (vv. 22–26), and the assayer's verdict (vv. 27–30).

Aspect notes:
  4:1–4 — conditionals (ʾim-clauses) + imperfects: ongoing conditional, not past command.
  4:23–26 — "I beheld" — perfect forms reporting completed visionary acts; T preserves the
    past-visionary register ("I looked").
  5:22 — "which have placed" — participial phrase (ongoing creative act), not past.
  6:14 — "they heal" — present ongoing — the false healing is a current practice.
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
  "4": {
    "1": {
      "L": "If you will return, O Israel, declares the LORD, return to me; and if you will remove your abominations from before my face, you shall not wander.",
      "M": "If you will return, O Israel, declares the LORD, return to me. If you will remove your detestable idols from before me, you will not be driven away.",
      "T": "If you will return, O Israel — Yahweh declares — then return to me. Remove your vile idols from before my face, and you will not be uprooted."
    },
    "2": {
      "L": "And you shall swear, 'As the LORD lives,' in truth, in justice, and in righteousness; and the nations shall bless themselves in him, and in him shall they glory.",
      "M": "Then you shall swear, 'As the LORD lives,' in truth, in justice, and in righteousness; and the nations will pronounce blessings by him and boast in him.",
      "T": "Then you will swear by Yahweh's living name — and mean it: in truth, in justice, in righteousness. And the nations will invoke his blessing; they will find their boast in him."
    },
    "3": {
      "L": "For thus says the LORD to the men of Judah and Jerusalem: Break up your fallow ground, and do not sow among thorns.",
      "M": "For this is what the LORD says to the men of Judah and Jerusalem: Break up your untilled ground, and do not sow among thorns.",
      "T": "For this is what Yahweh says to Judah and Jerusalem: Break open your untilled soil — stop sowing in thornfields."
    },
    "4": {
      "L": "Circumcise yourselves to the LORD, and remove the foreskins of your hearts, O men of Judah and inhabitants of Jerusalem; lest my wrath go forth like fire, and burn with none to quench it, because of the evil of your deeds.",
      "M": "Circumcise yourselves to the LORD, and remove the foreskins of your hearts, you men of Judah and inhabitants of Jerusalem; or my wrath will go out like fire and burn with no one to quench it, because of your evil deeds.",
      "T": "Circumcise yourselves to Yahweh — circumcise your hearts, you people of Judah, you citizens of Jerusalem. Or my fury will burst out like fire, burning with no one to quench it — because of the evil you have done."
    },
    "5": {
      "L": "Declare in Judah, and publish in Jerusalem; say, Blow the trumpet in the land; cry aloud and say, Assemble yourselves, and let us go into the fortified cities.",
      "M": "Announce it in Judah, proclaim it in Jerusalem; sound the trumpet throughout the land and shout: gather together and go into the fortified cities.",
      "T": "Cry the alarm through Judah! Proclaim it in Jerusalem! Blow the trumpet through the land — shout it out: Gather together! Flee to the fortified cities!"
    },
    "6": {
      "L": "Raise the signal toward Zion; flee for safety, do not stand still; for I am bringing disaster from the north, and great destruction.",
      "M": "Raise the signal flag toward Zion; flee to safety, do not delay; for I am bringing disaster from the north — a great calamity.",
      "T": "Hoist the signal toward Zion — run, don't linger! For I am bringing disaster from the north, a great destruction."
    },
    "7": {
      "L": "The lion has gone up from his thicket, and the destroyer of nations has set out; he has gone forth from his place to make your land a waste; your cities will be laid waste, without inhabitant.",
      "M": "The lion has come out of his thicket, and the destroyer of nations has set out; he has gone forth from his place to make your land a desolation; your cities will be laid waste, left without inhabitant.",
      "T": "The lion has leapt from his thicket — the destroyer of nations has set out. He has left his lair to turn your land into a wasteland; your cities will be left empty, their inhabitants gone."
    },
    "8": {
      "L": "For this gird yourself with sackcloth, lament and wail; for the fierce anger of the LORD has not turned back from us.",
      "M": "Because of this, put on sackcloth, and wail and howl; for the fierce anger of the LORD has not turned away from us.",
      "T": "So gird yourselves with sackcloth — wail and howl. Yahweh's burning anger has not turned from us."
    },
    "9": {
      "L": "And it shall be in that day, declares the LORD, that the heart of the king shall fail, and the heart of the princes; the priests shall be appalled, and the prophets astonished.",
      "M": "In that day, declares the LORD, the king's courage will fail, along with the courage of the officials; the priests will be horrified and the prophets stunned.",
      "T": "On that day — Yahweh declares — the king's heart will fail him, and his officials' hearts too. The priests will stand aghast; the prophets will be struck dumb."
    },
    "10": {
      "L": "Then I said, 'Ah, Lord GOD, truly you have utterly deceived this people and Jerusalem, saying, \"You shall have peace,\" whereas the sword has reached to the soul.'",
      "M": "Then I said, 'Ah, Lord GOD! You have truly deceived this people and Jerusalem, saying, \"You shall have peace,\" when in fact the sword has reached to the very soul.'",
      "T": "Then I cried out: 'Alas, Lord GOD! Have you truly deceived this people and Jerusalem, saying \"Peace is coming\" — when the sword has pierced to the very life?'"
    },
    "11": {
      "L": "At that time it shall be said to this people and to Jerusalem: A scorching wind from the bare heights in the wilderness toward the daughter of my people — not to winnow or cleanse,",
      "M": "At that time it will be said to this people and to Jerusalem: A scorching wind from the bare heights of the wilderness is blowing toward my people — not to winnow grain or to cleanse,",
      "T": "At that time the word will come to this people and Jerusalem: A searing wind from the desert heights — blowing straight at my people. Not a winnowing wind, not a threshing wind —"
    },
    "12": {
      "L": "A wind too strong for these comes at my word; now I also will pronounce judgments against them.",
      "M": "A wind stronger than these will come at my command; now I will pronounce judgment against them.",
      "T": "A full gale — stronger than any threshing wind — comes at my word. Now I pronounce their sentence."
    },
    "13": {
      "L": "Behold, he comes up like clouds, and his chariots like the whirlwind; his horses are swifter than eagles. Woe to us, for we are ruined!",
      "M": "Look — he advances like storm clouds; his chariots are like a whirlwind, his horses swifter than eagles. We are doomed, for we are destroyed!",
      "T": "Look — he sweeps up like thunderclouds; his chariots are a whirlwind, his horses swifter than eagles. We are doomed! We are ruined!"
    },
    "14": {
      "L": "O Jerusalem, wash your heart from wickedness, that you may be saved. How long shall your vain thoughts lodge within you?",
      "M": "O Jerusalem, wash the evil from your heart, so that you may be saved. How long will you harbor your wicked schemes?",
      "T": "Jerusalem — wash the evil from your heart! Only then can you be saved. How long will you nurse these deadly schemes?"
    },
    "15": {
      "L": "For a voice declares from Dan, and proclaims disaster from Mount Ephraim.",
      "M": "For a voice proclaims from Dan and announces disaster from Mount Ephraim.",
      "T": "A voice cries out from Dan; disaster is announced from Mount Ephraim."
    },
    "16": {
      "L": "Warn the nations; behold, declare against Jerusalem: Besiegers are coming from a distant land, they raise their voice against the cities of Judah.",
      "M": "Tell the nations, announce concerning Jerusalem: Besiegers are coming from a distant land, raising their battle cry against the cities of Judah.",
      "T": "Signal to the nations — let them hear: Besiegers come from afar! They shout their war cry against Jerusalem, against Judah's cities."
    },
    "17": {
      "L": "Like watchmen of a field they are against her all around, because she has rebelled against me, declares the LORD.",
      "M": "Like guards surrounding a field, so they surround her on every side, because she has rebelled against me, declares the LORD.",
      "T": "They ring her like sentinels ringing a field — because she has defied me, Yahweh declares."
    },
    "18": {
      "L": "Your way and your deeds have brought these things upon you. This is your evil; how bitter it is! How it has reached to your very heart!",
      "M": "Your conduct and your actions have brought this on you. This is your punishment; how bitter it is! How it has pierced to your very heart!",
      "T": "Your own ways and deeds have brought this on you — this is your punishment. How bitter it is! It has struck you to the heart."
    },
    "19": {
      "L": "My bowels! My bowels! I writhe in pain! The walls of my heart! My heart is raging within me; I cannot be silent; for I have heard, O my soul, the sound of the trumpet, the alarm of war.",
      "M": "My anguish, my anguish! I writhe in pain! The chambers of my heart are throbbing; I cannot keep silent, for I have heard the sound of the trumpet — the alarm of war!",
      "T": "My anguish, my anguish — I am in agony!\nMy heart pounds within me; I cannot keep silent.\nFor I have heard the trumpet's blast — the war alarm —\nas it pierces my whole being."
    },
    "20": {
      "L": "Disaster upon disaster is proclaimed, for the whole land is laid waste; suddenly my tents are destroyed, my tent curtains in an instant.",
      "M": "Crash after crash — the whole land is laid waste! In a flash my tents are destroyed, my tent-curtains gone in an instant.",
      "T": "Ruin upon ruin! The whole land is in ruins!\nIn an instant my tents are destroyed,\nmy tent-curtains torn down in a moment."
    },
    "21": {
      "L": "How long must I see the signal flag and hear the sound of the trumpet?",
      "M": "How long must I see the battle standard and hear the blare of the trumpet?",
      "T": "How long must I see the battle standard, hear the trumpet's blare?"
    },
    "22": {
      "L": "For my people are foolish; they do not know me; they are senseless children, with no understanding; they are skilled in doing evil, but doing good they do not know.",
      "M": "For my people are foolish — they do not know me; they are stupid children; they have no understanding. They are clever at doing evil, but they do not know how to do good.",
      "T": "My people are fools — they do not know me; they are witless children with no understanding. They are experts at evil, but doing good they have never learned."
    },
    "23": {
      "L": "I looked at the earth, and behold, it was without form and void; and at the heavens, and they had no light.",
      "M": "I looked at the earth and it was formless and void; I looked at the heavens and their light was gone.",
      "T": "I looked at the earth — and it was waste and void,\nthe chaos of creation undone.\nI looked at the heavens — and their light was extinguished."
    },
    "24": {
      "L": "I looked at the mountains, and behold, they were quaking, and all the hills were swaying.",
      "M": "I looked at the mountains and they were quaking; all the hills were swaying.",
      "T": "I looked at the mountains — they were convulsing;\nall the hills shook and staggered."
    },
    "25": {
      "L": "I looked, and behold, there was no man, and all the birds of the air had fled.",
      "M": "I looked — there was no human being, and all the birds of the sky had flown away.",
      "T": "I looked — there was no human being left;\nevery bird of the sky had flown."
    },
    "26": {
      "L": "I looked, and behold, the fruitful land was a wilderness, and all its cities were laid in ruins before the LORD, before his fierce anger.",
      "M": "I looked — the fertile land was a desert; all its cities lay in ruins before the LORD, because of his fierce anger.",
      "T": "I looked — the garden land was desert;\nevery city lay in ruins.\nBefore Yahweh's face, before his burning anger."
    },
    "27": {
      "L": "For thus says the LORD: The whole land shall be desolate; yet I will not make a full end.",
      "M": "For this is what the LORD says: The whole land will be desolate, yet I will not make a complete end.",
      "T": "For this is what Yahweh has said: The whole land will be laid waste — yet I will not make a full end."
    },
    "28": {
      "L": "For this the earth shall mourn, and the heavens above be dark; for I have spoken, I have purposed, and I have not relented, nor will I turn back from it.",
      "M": "For this the earth will mourn and the heavens above grow dark; for I have spoken, I have decided, and I will not relent or turn back from it.",
      "T": "For this the earth mourns, the heavens grow dark above — for I have spoken it, I have purposed it. I will not relent; I will not turn back."
    },
    "29": {
      "L": "The whole city flees from the noise of horsemen and archers; they go into the thickets and climb among the rocks; every city is forsaken, and no one dwells in them.",
      "M": "Every city is abandoned; they flee from the noise of horsemen and archers; they hide in thickets and climb up among the rocks; every city is deserted, with no one living in them.",
      "T": "The whole city flees — at the thunder of horsemen and archers they scatter into the thickets, climb among the rocks. Every city is abandoned; not a soul remains in them."
    },
    "30": {
      "L": "And you, O devastated one, what will you do? Though you clothe yourself in scarlet, though you adorn yourself with ornaments of gold, though you enlarge your eyes with paint, you adorn yourself in vain. Your lovers despise you; they seek your life.",
      "M": "And you, O desolate one — what will you do? Though you clothe yourself in crimson, though you adorn yourself with golden jewelry, though you paint your eyes with kohl, you make yourself attractive in vain. Your lovers reject you; they want your life.",
      "T": "What will you do now, O ruined city? You dress yourself in scarlet, you put on gold jewelry, you paint your eyes wide — all in vain. Your lovers despise you; they are after your life."
    },
    "31": {
      "L": "For I have heard a voice as of a woman in labor, the anguish as of one bearing her first child — the voice of the daughter of Zion gasping for breath, spreading her hands: 'Woe is me! My soul faints before the murderers.'",
      "M": "For I heard a cry like a woman in labor, anguish like a first-time mother — the cry of Daughter Zion, gasping and reaching out her hands: 'Woe to me! I am faint before the murderers!'",
      "T": "I heard a cry — the cry of a woman giving birth,\nanguish like a first-time mother.\nThe voice of Daughter Zion, gasping, arms stretched out:\n'Woe to me — I am faint! The murderers are upon me!'"
    }
  },
  "5": {
    "1": {
      "L": "Run to and fro through the streets of Jerusalem, look and take note, search her squares; if you can find a man, if there is one who does justice and seeks faithfulness, that I may pardon her.",
      "M": "Go up and down the streets of Jerusalem, look around and consider; search through her public squares to see whether you can find even one person who acts justly and seeks honesty — then I will forgive this city.",
      "T": "Walk the streets of Jerusalem — look, take notice, search the open squares. Can you find one person — one who practices justice, who seeks truth? For that one, I would pardon the whole city."
    },
    "2": {
      "L": "And though they say, 'As the LORD lives,' yet they swear falsely.",
      "M": "Even when they say 'As the LORD lives,' they are swearing falsely.",
      "T": "They mouth the words 'As Yahweh lives' — and every oath is a lie."
    },
    "3": {
      "L": "O LORD, do not your eyes look for faithfulness? You struck them, but they felt no pain; you consumed them, but they refused correction. They made their faces harder than a rock; they refused to return.",
      "M": "LORD, do not your eyes look for faithfulness? You struck them, but they felt nothing; you crushed them, but they refused to be corrected. They set their faces harder than stone; they refused to return.",
      "T": "Yahweh, don't your eyes look for honesty? You struck them — they felt nothing. You broke them — they refused correction. They set their faces harder than flint; they would not come back."
    },
    "4": {
      "L": "Then I said, 'These are only the poor; they are foolish, for they do not know the way of the LORD, the justice of their God.'",
      "M": "Then I thought, 'These are only the poor; they are ignorant; they do not know the way of the LORD, the requirements of their God.'",
      "T": "Then I thought: 'These are only the poor — they do not know any better. They have never learned the way of Yahweh, the requirements of their God.'"
    },
    "5": {
      "L": "Let me go to the great men and speak to them; for they know the way of the LORD, the justice of their God. But they all alike have broken the yoke and burst the bonds.",
      "M": "So I went to the leaders and spoke to them, for they surely know the way of the LORD, the requirements of their God. But they too had together broken the yoke and torn off the bands.",
      "T": "So I went to the powerful — surely they know Yahweh's way, the requirements of God. But every one of them had broken the yoke and snapped the harness."
    },
    "6": {
      "L": "Therefore a lion from the forest will kill them; a wolf from the desert will ravage them; a leopard lies in wait near their cities — whoever goes out will be torn in pieces. For their transgressions are many; their backslidings are great.",
      "M": "Therefore a lion from the forest will attack them, a wolf from the desert will ravage them, a leopard will lurk near their towns — anyone who goes out will be torn to pieces. For their rebellions are many and their turnings away are great.",
      "T": "Therefore a forest lion will tear them, a desert wolf will ravage them, a leopard crouches near their towns — no one who ventures out will escape. For their rebellions are countless, their wayward departures beyond numbering."
    },
    "7": {
      "L": "How shall I pardon you for this? Your children have forsaken me and sworn by those who are no gods. When I satisfied them, they committed adultery and trooped to the prostitutes' houses.",
      "M": "How can I forgive you for this? Your children have abandoned me and sworn oaths by gods that are no gods at all. When I satisfied their every need, they committed adultery and flocked to the brothels.",
      "T": "How can I forgive you for this? Your children left me and swore by gods that are not gods. I filled them — and they repaid me with adultery, swarming into the houses of prostitutes."
    },
    "8": {
      "L": "They were lusty, well-fed horses; each one neighs after his neighbor's wife.",
      "M": "They are like well-fed, lusty stallions — each neighing after another man's wife.",
      "T": "They are stallions fattened on grain — each one neighing after his neighbor's wife."
    },
    "9": {
      "L": "Shall I not punish for these things? declares the LORD; and shall not my soul take vengeance on a nation such as this?",
      "M": "Should I not call them to account for these things? declares the LORD. Should I not take vengeance on a nation like this?",
      "T": "Shall I not reckon with this? Yahweh declares. On a nation like this — shall I not take my due?"
    },
    "10": {
      "L": "Go up through her vine rows and destroy, but do not make a full end; strip away her branches, for they are not the LORD's.",
      "M": "Advance through her vineyards and ravage them, but do not destroy them completely; strip off her branches, for they do not belong to the LORD.",
      "T": "Climb into her vineyard rows — strip them bare! But do not make a complete end. Tear off her tendrils, for they do not belong to Yahweh."
    },
    "11": {
      "L": "For the house of Israel and the house of Judah have been utterly treacherous against me, declares the LORD.",
      "M": "For the house of Israel and the house of Judah have acted completely faithlessly toward me, declares the LORD.",
      "T": "Both Israel and Judah have betrayed me utterly — Yahweh declares."
    },
    "12": {
      "L": "They have denied the LORD and said, 'He will do nothing; no disaster will come upon us, nor shall we see sword or famine.'",
      "M": "They have lied about the LORD and said, 'He will do nothing; no disaster will come upon us; we will not face sword or famine.'",
      "T": "They have lied about Yahweh: 'He will do nothing — no disaster will come our way. We will never see sword or famine.'"
    },
    "13": {
      "L": "The prophets will become wind, and the word is not in them; so shall it be done to them.",
      "M": "The prophets are nothing but wind; the word of God is not in them. What they threatened will now happen to them.",
      "T": "As for the prophets — they are just wind; the word is not in them. What they predicted for others will come on themselves."
    },
    "14": {
      "L": "Therefore thus says the LORD, the God of hosts: Because they speak this word, I am making my words in your mouth a fire, and this people wood, and the fire shall consume them.",
      "M": "Therefore, this is what the LORD God of Armies says: Because you have spoken like this, I will make my words in your mouth a fire and these people the wood it will consume.",
      "T": "Therefore this is what Yahweh, the God of Armies, says: Because you have spoken such words, I am putting my words in your mouth like fire — and this people will be the wood that burns."
    },
    "15": {
      "L": "Behold, I am bringing against you a nation from afar, O house of Israel, declares the LORD. It is an enduring nation, it is an ancient nation, a nation whose language you do not know, nor can you understand what they say.",
      "M": "Listen: I am bringing a nation against you from far away, O house of Israel, declares the LORD. It is a powerful nation, an ancient nation, a nation whose language you do not know, whose speech you cannot understand.",
      "T": "Hear this, Israel — Yahweh declares: I am bringing a nation from far away against you. A mighty nation, an ancient nation — whose language is foreign to you, whose speech you cannot understand."
    },
    "16": {
      "L": "Their quiver is like an open tomb; they are all warriors.",
      "M": "Their quivers are like open graves; they are all mighty men.",
      "T": "Their quiver is an open grave; every one of them is a warrior."
    },
    "17": {
      "L": "They shall eat up your harvest and your food, which your sons and daughters should eat; they shall eat up your flocks and herds; they shall eat up your vines and fig trees; with the sword they shall destroy your fortified cities in which you trust.",
      "M": "They will devour your harvests and your food — what your sons and daughters depend on for life. They will devour your flocks and herds, your vines and fig trees. With the sword they will demolish the fortified cities you trust in.",
      "T": "They will eat everything: your harvests, your food, your flocks and herds, your vines and fig trees. With the sword they will demolish the walled cities where you put your trust."
    },
    "18": {
      "L": "But in those days, declares the LORD, I will not make a full end of you.",
      "M": "Yet even in those days, declares the LORD, I will not make a complete end of you.",
      "T": "Yet even then — Yahweh declares — I will not make a full end of you."
    },
    "19": {
      "L": "And when they say, 'Why has the LORD our God done all these things to us?' you shall tell them, 'As you forsook me and served foreign gods in your land, so you shall serve foreigners in a land that is not yours.'",
      "M": "When they ask, 'Why has the LORD our God done all this to us?' tell them, 'As you abandoned me and served foreign gods in your own land, so now you will serve foreigners in a land that is not your own.'",
      "T": "When they ask, 'Why has Yahweh our God done all this to us?' give them this answer: 'As you abandoned me and served foreign gods in your own land, so you will serve strangers in a land that is not yours.'"
    },
    "20": {
      "L": "Declare this in the house of Jacob, and proclaim it in Judah, saying:",
      "M": "Announce this to the house of Jacob; proclaim it in Judah, saying:",
      "T": "Announce it to Jacob's household; proclaim it throughout Judah:"
    },
    "21": {
      "L": "Hear this, O foolish and senseless people, who have eyes, but see not; who have ears, but hear not:",
      "M": "Listen to this, you foolish and senseless people — you have eyes but do not see; you have ears but do not hear:",
      "T": "Hear this, you foolish people without understanding — eyes that do not see, ears that do not hear:"
    },
    "22": {
      "L": "Do you not fear me? declares the LORD. Will you not tremble before me? I who placed the sand as the boundary of the sea, a perpetual limit it cannot cross. Though its waves toss, they cannot prevail; though they roar, they cannot pass over it.",
      "M": "Should you not fear me? declares the LORD. Should you not tremble before me? I am the one who set the sand as the boundary of the sea, an eternal limit that it cannot cross. Its waves may surge, but they cannot prevail; they may roar, but they cannot pass over it.",
      "T": "Will you not fear me? — Yahweh declares. Will you not tremble before me? I set the sand as the sea's boundary — an everlasting limit the waves cannot cross. They surge — but cannot prevail. They roar — but cannot pass."
    },
    "23": {
      "L": "But this people has a stubborn and rebellious heart; they have turned aside and gone away.",
      "M": "But this people has a stubborn, rebellious heart; they have turned away and left.",
      "T": "But this people — they have a stubborn and rebellious heart. They have turned and gone."
    },
    "24": {
      "L": "They do not say in their heart, 'Let us now fear the LORD our God, who gives rain in its season, both the autumn rain and the spring rain, and who keeps for us the appointed weeks of the harvest.'",
      "M": "They do not even say in their hearts, 'Let us now fear the LORD our God, who gives the autumn and spring rains in season and keeps for us the weeks appointed for harvest.'",
      "T": "It never occurs to them to say: 'Let us now revere Yahweh our God, who gives autumn rain and spring rain in their season — who keeps for us the weeks of harvest.'"
    },
    "25": {
      "L": "Your iniquities have turned these things away, and your sins have kept good from you.",
      "M": "Your iniquities have diverted these good things, and your sins have kept them from you.",
      "T": "Your sins have driven these blessings away; your rebellions have cut you off from what is good."
    },
    "26": {
      "L": "For among my people are found wicked men; they lurk like fowlers crouching in ambush; they set traps; they catch human beings.",
      "M": "For among my people there are wicked men — they lurk like hunters who set traps; they lay snares and catch people.",
      "T": "Among my people there are wicked hunters — they crouch like trappers in hiding; they lay their snares and catch human beings."
    },
    "27": {
      "L": "As a cage is full of birds, so their houses are full of deceit; therefore they have become great and rich.",
      "M": "As a cage is full of birds, so their houses are full of goods gotten by deceit; that is how they became great and rich.",
      "T": "Their houses are crammed with the fruits of fraud — like a cage packed with birds. That is how they became great and grew fat with wealth."
    },
    "28": {
      "L": "They have grown fat and sleek. They have also exceeded in deeds of evil; they do not plead the cause, the cause of the fatherless, to make it prosper; and the right of the needy they do not defend.",
      "M": "They have grown fat and sleek; they surpass all limits in their evil deeds. They do not defend the rights of the fatherless, and they do not champion the cause of the needy.",
      "T": "Fat and smug, they push past every limit in wickedness. They do not take up the orphan's case or champion the rights of the poor."
    },
    "29": {
      "L": "Shall I not punish for these things? declares the LORD; and shall not my soul take vengeance on a nation such as this?",
      "M": "Should I not call them to account for these things? declares the LORD. Should I not take vengeance on a nation like this?",
      "T": "Shall I not reckon with this? Yahweh declares. On a nation like this — shall I not take my due?"
    },
    "30": {
      "L": "A horrible and shocking thing has happened in the land:",
      "M": "A horrible and shocking thing has occurred in the land:",
      "T": "Something appalling, something monstrous, has happened in this land:"
    },
    "31": {
      "L": "The prophets prophesy lies; the priests rule by their own authority; and my people love it so. But what will you do when the end comes?",
      "M": "The prophets prophesy what is false, the priests exercise authority on their own terms, and my people love it this way. But what will you do when the end comes?",
      "T": "The prophets speak lies; the priests grab power for themselves; and my people love it so. But what will you do when it is all over?"
    }
  },
  "6": {
    "1": {
      "L": "Flee for safety, O children of Benjamin, from the midst of Jerusalem! Blow the trumpet in Tekoa, and raise a fire signal over Beth-haccerem, for disaster looms from the north, and great destruction.",
      "M": "Flee to safety, people of Benjamin — get out of Jerusalem! Sound the trumpet at Tekoa, and raise the smoke signal over Beth-haccerem; for disaster threatens from the north — a great calamity.",
      "T": "Flee for your lives, O people of Benjamin — escape from Jerusalem! Sound the trumpet at Tekoa, raise the fire signal over Beth-haccerem. For disaster threatens from the north — great destruction is coming."
    },
    "2": {
      "L": "I will destroy the fair and delicate daughter of Zion.",
      "M": "I will destroy the fair and delicate Daughter Zion.",
      "T": "Fair and delicate Daughter Zion — I will cut her down."
    },
    "3": {
      "L": "Shepherds come against her with their flocks; they pitch their tents around her; each grazes his portion.",
      "M": "Shepherds with their flocks will come to her and pitch their tents around her; each will pasture his portion.",
      "T": "Enemy shepherds come with their flocks — they pitch their tents all around her. Each one grazes his sector."
    },
    "4": {
      "L": "Consecrate war against her; arise, and let us attack at noon. Woe to us, for the day has turned; the shadows of evening are lengthening.",
      "M": "Prepare for holy war against her; arise, let us attack at noon. Alas for us, for the day is fading — the evening shadows grow long.",
      "T": "Dedicate the battle against her — arise, let us attack at noon! Alas, the day is waning, the evening shadows stretch long."
    },
    "5": {
      "L": "Arise, and let us attack by night and destroy her fortresses.",
      "M": "Let us rise up and attack by night and demolish her fortified towers.",
      "T": "Then: Rise up! We attack by night — we will demolish her palaces!"
    },
    "6": {
      "L": "For thus says the LORD of hosts: Cut down her trees; cast up a siege mound against Jerusalem. This is the city that must be punished; within her is nothing but oppression.",
      "M": "For this is what the LORD of Armies says: Cut down trees and build a siege ramp against Jerusalem. This city must be punished; within her is nothing but oppression.",
      "T": "For this is what Yahweh of Armies says: Cut timber; build the siege ramp against Jerusalem. This is the city that must be called to account — she is full of oppression from within."
    },
    "7": {
      "L": "As a well pours out its water, so she pours out her wickedness; sounds of violence and destruction are heard in her; before me continually are sickness and wounds.",
      "M": "As a well keeps pouring out water, so she keeps pouring out wickedness; sounds of violence and devastation are heard in her; before me constantly are sickness and wounds.",
      "T": "Like a spring that never stops, she pours out her evil — violence and destruction echo through her streets. Sickness and wounds lie before me without end."
    },
    "8": {
      "L": "Take warning, O Jerusalem, lest I turn from you in disgust; lest I make you a desolation, a land without inhabitant.",
      "M": "Take warning, O Jerusalem, or I will turn away from you; I will make you a ruin, a land where no one lives.",
      "T": "Take warning, Jerusalem — or I will turn from you in revulsion. I will reduce you to rubble, a land no one inhabits."
    },
    "9": {
      "L": "Thus says the LORD of hosts: Glean thoroughly as a vine the remnant of Israel; pass your hand again over the branches like a grape harvester.",
      "M": "This is what the LORD of Armies says: Carefully glean the remnant of Israel as a vinedresser gleans a vine; pass your hand over the branches again, like a harvester.",
      "T": "This is what Yahweh of Armies says: Glean what remains of Israel as a vinedresser gleans — run your hand back over the branches; pick the harvest clean."
    },
    "10": {
      "L": "To whom shall I speak and give warning, that they may hear? Behold, their ear is uncircumcised, and they cannot listen; behold, the word of the LORD is to them an object of reproach; they have no delight in it.",
      "M": "To whom shall I speak and give warning so that they will listen? Look, their ears are closed, and they cannot pay attention; the word of the LORD has become an object of scorn to them; they take no pleasure in it.",
      "T": "Whom can I speak to, who will listen? Their ears are uncircumcised — they cannot hear. The word of Yahweh has become a reproach to them; they want no part of it."
    },
    "11": {
      "L": "Therefore I am full of the fury of the LORD; I am weary with holding it in. I will pour it out upon the children in the street, and upon the company of young men together; for husband and wife alike shall be taken, the elderly along with the very aged.",
      "M": "So I am full of the LORD's fury; I am worn out with holding it in. Pour it out on the children playing in the street and on the young men gathered together; for husband and wife will be taken, even the old and the very aged.",
      "T": "So I am full of Yahweh's wrath — I am exhausted with holding it back. Pour it out on the children in the street, on the gathering of young men; husband and wife together, the old and the very old alike."
    },
    "12": {
      "L": "Their houses shall be turned over to others, their fields and wives together; for I will stretch out my hand against the inhabitants of the land, declares the LORD.",
      "M": "Their houses will be given to others, along with their fields and wives, because I will stretch out my hand against those who live in this land, declares the LORD.",
      "T": "Their houses will be given to others — fields and wives alike — for I will stretch out my hand against the people of this land. Yahweh declares."
    },
    "13": {
      "L": "For from the least to the greatest of them, everyone is greedy for unjust gain; and from prophet to priest, everyone deals falsely.",
      "M": "For from the least to the greatest of them, everyone is greedy for dishonest gain; from prophet to priest, everyone acts deceitfully.",
      "T": "From the least to the greatest — everyone chases dishonest gain. From prophet to priest — everyone deals in lies."
    },
    "14": {
      "L": "They have healed the wound of the daughter of my people lightly, saying, 'Peace, peace,' when there is no peace.",
      "M": "They treat the wound of my people as though it were minor, saying, 'Peace, peace,' when there is no peace.",
      "T": "They dress the wound of my people as though it were nothing — 'All is well! All is well!' But nothing is well."
    },
    "15": {
      "L": "Were they ashamed when they committed abomination? No, they were not at all ashamed; they did not know how to blush. Therefore they shall fall among those who fall; at the time I punish them, they shall be brought down, says the LORD.",
      "M": "Are they ashamed of their detestable conduct? No, they have no shame at all; they do not even know how to blush. Therefore they will fall among the fallen; when I punish them they will be brought down, says the LORD.",
      "T": "Were they ashamed of their disgusting conduct? Not at all — shame is foreign to them; they cannot blush. So they will fall with all who fall; when I call them to account, they will be brought down. Yahweh has spoken."
    },
    "16": {
      "L": "Thus says the LORD: Stand at the crossroads, and look; ask for the ancient paths, where the good way is; walk in it, and you will find rest for your souls. But they said, 'We will not walk in it.'",
      "M": "This is what the LORD says: Stand at the crossroads and look; ask for the ancient paths, ask where the good way is, and walk in it. You will find rest for your souls. But they said, 'We will not walk in it.'",
      "T": "This is what Yahweh says:\nStand at the crossroads and look.\nAsk for the ancient paths: 'Where is the good way?'\nWalk in it, and you will find rest for your souls.\nBut they said, 'We will not walk in it.'"
    },
    "17": {
      "L": "I also set watchmen over you: 'Listen to the sound of the trumpet.' But they said, 'We will not listen.'",
      "M": "I appointed watchmen over you and said, 'Listen to the sound of the trumpet!' But they said, 'We will not listen.'",
      "T": "I set sentinels over you: 'Listen for the trumpet!' But they said, 'We will not listen.'"
    },
    "18": {
      "L": "Therefore hear, O nations, and know, O congregation, what is among them.",
      "M": "Therefore, you nations, hear; you witnesses, know what has happened among them.",
      "T": "Therefore, hear this, O nations! Witnesses, take note of what is happening among them."
    },
    "19": {
      "L": "Hear, O earth: behold, I am bringing disaster upon this people, the fruit of their own schemes, because they have not listened to my words and have rejected my law.",
      "M": "Listen, O earth: I am going to bring disaster on this people — the direct result of their own schemes — because they have not listened to my words and have rejected my law.",
      "T": "Hear, O earth: I am bringing disaster on this people — the fruit of their own plotting. For they have not listened to my words; they have despised my law."
    },
    "20": {
      "L": "To what purpose does frankincense come to me from Sheba, or sweet cane from a distant land? Your burnt offerings are not acceptable, and your sacrifices are not pleasing to me.",
      "M": "What good is it if incense is brought to me from Sheba and fragrant cane from a distant land? Your burnt offerings are not acceptable to me; your sacrifices do not please me.",
      "T": "Why bring me incense from Sheba, or costly cane from a far country? Your burnt offerings have no value to me; your sacrifices give me no pleasure."
    },
    "21": {
      "L": "Therefore thus says the LORD: Behold, I will lay before this people obstacles, and they shall stumble over them — fathers and sons together; neighbor and friend shall perish.",
      "M": "Therefore this is what the LORD says: I am going to put obstacles before this people, and they will stumble over them — fathers and sons together, neighbors and friends will all perish.",
      "T": "Therefore this is what Yahweh says: I am setting stumbling blocks before this people. Fathers and sons together will trip over them; neighbor and friend together will go down."
    },
    "22": {
      "L": "Thus says the LORD: Behold, a people is coming from the north country, and a great nation is being stirred up from the remote parts of the earth.",
      "M": "This is what the LORD says: Look, an army is coming from the northern country, a great nation is being roused from the far ends of the earth.",
      "T": "This is what Yahweh says: A people is on the march from the north — a great nation aroused from the farthest corners of the earth."
    },
    "23": {
      "L": "They grasp bow and spear; they are cruel and have no mercy. The sound of them is like the roaring sea; they ride on horses, arrayed like warriors for battle against you, O daughter of Zion.",
      "M": "They are armed with bow and spear; they are ruthless and without mercy. They sound like the roaring sea as they come riding on horses, lined up for battle against you, O Daughter Zion.",
      "T": "They grip bow and spear — relentless, without mercy.\nTheir roar is like the sea.\nThey ride on horses, drawn up in battle order against you,\nO Daughter Zion."
    },
    "24": {
      "L": "We have heard the report of it; our hands fall limp; anguish has seized us, pain as of a woman in labor.",
      "M": "We have heard the report — our hands go limp; distress has seized us, pain like a woman in labor.",
      "T": "We have heard the news — our hands go limp. Anguish seizes us — the pain of a woman in labor."
    },
    "25": {
      "L": "Do not go out into the field, nor walk on the road, for the enemy has a sword; terror is on every side.",
      "M": "Do not go out into the fields or walk along the roads, for the enemy is armed with a sword; terror is on every side.",
      "T": "Do not go out into the fields; do not walk on the roads. The enemy has a sword — terror on every side."
    },
    "26": {
      "L": "O daughter of my people, put on sackcloth, and roll in ashes; make mourning as for an only son, most bitter lamentation; for the destroyer will suddenly come upon us.",
      "M": "O my dear people, put on sackcloth and roll in the ashes; mourn with bitter weeping as for an only child, because the destroyer is about to come upon us suddenly.",
      "T": "O my dear people — put on sackcloth, roll in the ashes.\nMourn as for an only son — bitter, bitter weeping.\nFor the destroyer comes upon us without warning."
    },
    "27": {
      "L": "I have made you a tester and a fortress among my people, that you may know and test their way.",
      "M": "I have made you an assayer and a tester among my people, so that you may know and test their conduct.",
      "T": "I have appointed you as an assayer among my people — a fortress-tester. Know their ways and test them."
    },
    "28": {
      "L": "They are all hardened rebels, going about as slanderers; they are bronze and iron; they are all corrupt.",
      "M": "They are all rebellious troublemakers, going about spreading slander; they are bronze and iron — utterly corrupt.",
      "T": "All of them are hardened rebels — going about with slander on their lips. Bronze and iron, every one of them — all corrupt."
    },
    "29": {
      "L": "The bellows blow fiercely; the lead is consumed by the fire; in vain the refiner refines, for the evil is not removed.",
      "M": "The bellows blow fiercely; the lead is consumed in the flames; the smelter smelts in vain — the wicked are not drawn off.",
      "T": "The bellows blast, the lead melts in the fire — the refiner works in vain: the dross is not removed. The wicked remain."
    },
    "30": {
      "L": "Rejected silver they are called, for the LORD has rejected them.",
      "M": "They will be called rejected silver, for the LORD has rejected them.",
      "T": "They shall be called 'dross silver' — for Yahweh has rejected them."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 4–6 written.')

if __name__ == '__main__':
    main()
