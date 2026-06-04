"""
MKT Jeremiah chapters 13–15 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-13-15.py

Translation decisions (consistent with mkt-jeremiah-1-3.py and mkt-jeremiah-10-12.py):
- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where personal-name force is significant
  (oracles, covenant declarations, divine soliloquy, lament address). Narrative formulas use
  "Yahweh" in T for immediacy.
- H430 (אֱלֹהִים): "God" in all tiers; "gods" when referring to foreign deities (14:22).
- H136+H3069 (אֲדֹנָי יְהוִה): "Lord GOD" in L/M (standard rendering of Adonai YHWH);
  "Lord Yahweh" in T (preserving the compound form's weight without small-caps obscuring it).
  Appears at 14:13.
- H232 (אֵזוֹר): "belt" in L (word-for-word); "sash" in M/T — the Hebrew denotes a fabric
  waistband/loincloth tied against the skin, not a leather military belt; "sash" captures
  the intimate-wrapping image that the parable requires.
- H7307 (רוּחַ): 13:24 = "desert wind" — physical wind scattering chaff; 14:6 = "air" — donkeys
  panting for breath. Neither occurrence is Spirit.
- H5315 (נֶפֶשׁ): 13:17 "my soul" (L) / "I" (M) / Jeremiah's anguished inner self (T);
  15:1 used of Yahweh's "mind / inner being" — rendered "my heart" in M, "my heart would feel
  nothing" in T to capture the divine rejection without anachronistic psychology.
- H7451 (רָעָה): context-sensitive throughout. Divine judgment arriving: "disaster" (11:11 pattern
  maintained at 15:11). Human moral state: "evil/wickedness" (13:10, 14:16).
- H1226 (בַּצֹּרֶת): "drought/dearth" — the header title of ch. 14's liturgy. Rendered "drought"
  throughout; the LXX and Vulgate read "concerning the matters of the drought."
- H4490/H4055 (מְנָת מִדָּה): 13:25 "the portion I have measured out" — lot/allotted share;
  both nouns point to a measured allocation; rendered as "portion measured out" in L,
  "allotted portion" in M, "inheritance" / "the measure Yahweh assigned" in T.
- H8281 (שְׁאֵרִית): 15:11 "remnant/survivors" — follows the pattern of 15:9 (H7611); rendered
  "your remnant" in L, "what remains of you" in M, "whatever remains of you" in T.

Textual note — 14:1:
  The verse title "concerning the drought" (H1226 הַבַּצֹּרֶת) is unusual — it functions as a
  superscription for the drought-liturgy of chs. 14:1–15:4. Rendered as a heading phrase.

Textual note — 15:11:
  The Hebrew is difficult: MT אִם-לֹא שֵׁרוֹתִיךָ (if not I have ministered / set you free) with
  variants. The thrust is a divine counter-assurance: Jeremiah will be released/vindicated;
  enemies will come to him in the hour of disaster. The T tier renders the rhetorical effect.

Structural notes:
  Ch. 13 — Sign-act: the linen belt (vv. 1–11); the wine-jar oracle (vv. 12–14); call to humility
  before darkness falls (vv. 15–17); lamentation addressed to king and queen-mother (vv. 18–19);
  the city's shame and helplessness (vv. 20–27). The belt parable is the key: what had once
  clung close to Yahweh (belt to loins) is now completely ruined — this is what Israel has become.

  Ch. 14 — The Drought Liturgy. A formal lament sequence: description of disaster (vv. 1–6);
  communal prayer of confession and appeal (vv. 7–9); Yahweh's rejection of the people (v. 10);
  divine prohibition on intercession (v. 11); Jeremiah's intercession interrupted by the false-
  prophet problem (vv. 13–16); Jeremiah resumes lament as Yahweh's voice (vv. 17–18); a second
  prayer (vv. 19–22). The drought functions as both literal crisis and theological sign.

  Ch. 15 — The third "confession" of Jeremiah (15:10–21), the most psychologically intense.
  Yahweh refuses to be moved even by Moses or Samuel (v. 1). The fourfold judgment (vv. 2–3).
  Citation of Manasseh's guilt as the ultimate cause (v. 4). Lament over Jerusalem's
  abandonment (vv. 5–9). Then Jeremiah's anguished outcry (vv. 10–18) and Yahweh's
  recommission — stern, conditional, but ultimately a restoration of calling (vv. 19–21).

OT echoes:
  13:11 — the belt-clinging image picks up the intimacy language of Deut 10:20 ("hold fast")
    and Ps 63:8 ("my soul clings to you").
  13:23 — "Ethiopian / leopard spots" — one of the most quoted aphorisms from Jeremiah; the
    impossibility of self-transformation anticipates Paul's "no one does good" in Rom 3.
  14:8 — "hope of Israel" = a divine title that recurs in Jer 17:13 and Acts 28:20; the prayer
    addresses Yahweh by a name that accuses him of acting contrary to his own identity.
  14:21 — "the throne of your glory" — the ark/temple as Yahweh's earthly throne; the same
    phrase at 17:12 and echoed in Matt 19:28.
  15:1 — Moses and Samuel as supreme intercessors: Moses at Exod 32:11–14 and Num 14:13–24;
    Samuel at 1 Sam 7:5–9 and 12:23. The point is that even the greatest possible human
    advocates could not move Yahweh now.
  15:16 — "I found your words and ate them" — echoed in Ezek 3:1–3 (the scroll Ezekiel eats)
    and Rev 10:9–10 (the sweet-bitter scroll); a shared prophetic-commissioning motif.
  15:20 — "a fortified bronze wall" — picks up Jeremiah's original call in 1:18 ("iron pillar
    and bronze walls against the whole land"); the recommission restates the original commission.
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
  "13": {
    "1": {
      "L": "Thus says the LORD to me: Go and buy a linen belt and put it on your loins; do not dip it in water.",
      "M": "This is what the LORD said to me: Go and buy a linen sash and put it around your waist; do not put it in water.",
      "T": "Yahweh told me: Go and buy a linen sash. Tie it around your waist — and do not wash it."
    },
    "2": {
      "L": "So I bought the belt according to the word of the LORD and put it on my loins.",
      "M": "So I bought the sash, as the LORD directed, and put it around my waist.",
      "T": "I bought the sash and wore it, exactly as Yahweh had said."
    },
    "3": {
      "L": "And the word of the LORD came to me a second time, saying:",
      "M": "Then the word of the LORD came to me a second time:",
      "T": "Then Yahweh's word came to me a second time:"
    },
    "4": {
      "L": "Take the belt that you have and which is on your loins, and arise, go to the Euphrates and hide it there in a cleft of the rock.",
      "M": "Take the sash you bought, the one around your waist, and go to the Euphrates. Hide it there in a crack in the rock.",
      "T": "Take the sash off your waist and go to the Euphrates. Hide it there, in a crevice in the rock."
    },
    "5": {
      "L": "So I went and hid it at the Euphrates, as the LORD commanded me.",
      "M": "So I went and hid it at the Euphrates, as the LORD commanded.",
      "T": "I went and hid it at the Euphrates, just as Yahweh had commanded."
    },
    "6": {
      "L": "And after many days the LORD said to me: Arise, go to the Euphrates and take from there the belt that I commanded you to hide there.",
      "M": "Many days later, the LORD told me: Get up and go to the Euphrates; retrieve the sash I told you to hide there.",
      "T": "A long time later, Yahweh told me: Go back to the Euphrates. Dig up the sash I had you hide there."
    },
    "7": {
      "L": "Then I went to the Euphrates and dug, and I took the belt from the place where I had hidden it; and behold, the belt was ruined — it was fit for nothing.",
      "M": "So I went to the Euphrates and dug it up. I took the sash from the place where I had hidden it — and it was ruined; it was completely useless.",
      "T": "I went to the Euphrates, dug it up, and retrieved the sash from where I had buried it. It was rotted — completely ruined, good for nothing at all."
    },
    "8": {
      "L": "Then the word of the LORD came to me, saying:",
      "M": "Then the word of the LORD came to me:",
      "T": "Then Yahweh's word came to me:"
    },
    "9": {
      "L": "Thus says the LORD: So will I mar the pride of Judah and the great pride of Jerusalem.",
      "M": "This is what the LORD says: In just this way I will ruin the great pride of Judah and Jerusalem.",
      "T": "Yahweh says: This is exactly how I will rot the pride of Judah — the great swollen pride of Jerusalem."
    },
    "10": {
      "L": "This evil people who refuse to hear my words, who walk in the stubbornness of their heart and walk after other gods to serve and worship them — they shall be as this belt which is fit for nothing.",
      "M": "This wicked people who refuse to listen to my words, who follow the stubbornness of their heart and go after other gods to serve and worship them — they will be just like this sash, completely useless.",
      "T": "This is what will happen to this wicked people. They will not hear my words. They walk in the hardness of their own heart, chasing after other gods to serve and bow down to. They will end up like that sash — fit for nothing, of no use to anyone."
    },
    "11": {
      "L": "For as a belt clings to the loins of a man, so I caused the whole house of Israel and the whole house of Judah to cling to me, that they might be to me for a people, for a name, for a praise, and for a glory; but they would not listen.",
      "M": "For just as a sash clings to a person's waist, so I bound the whole house of Israel and the whole house of Judah to myself, so that they would be my people, my renown, my praise, and my glory — but they would not listen.",
      "T": "Think about what a sash does — it wraps close against the body, intimate and inseparable. That was the closeness Yahweh intended when he bound all of Israel and Judah to himself: that they would be his people, his renown, his praise, his glory. But they would not listen."
    },
    "12": {
      "L": "Therefore you shall speak to them this word: Thus says the LORD, the God of Israel — every wineskin shall be filled with wine. And they will say to you: Do we not certainly know that every wineskin is filled with wine?",
      "M": "Therefore speak this word to them: This is what the LORD, the God of Israel, says — every wineskin will be filled with wine. And they will answer: Of course we know that every wineskin is filled with wine!",
      "T": "Then say this to them: Yahweh, God of Israel, says — every wineskin will be filled with wine. They will answer back: 'Obviously. Everyone knows wineskins are for wine.'"
    },
    "13": {
      "L": "Then say to them: Thus says the LORD — Behold, I will fill all the inhabitants of this land, even the kings sitting on David's throne, the priests, and the prophets, and all the inhabitants of Jerusalem, with drunkenness.",
      "M": "Then say to them: This is what the LORD says — I am going to fill all who live in this land — the kings sitting on David's throne, the priests, the prophets, and all the people of Jerusalem — with stupefying drunkenness.",
      "T": "Then explain what Yahweh means: I am going to pour a stupefying wine over this entire land — into every king who sits on David's throne, into every priest, every prophet, every inhabitant of Jerusalem. I will fill them all with a drunkenness that undoes them."
    },
    "14": {
      "L": "And I will dash them one against another, even the fathers and the sons together — I will not pity or spare or have mercy, but will destroy them, says the LORD.",
      "M": "I will smash them against each other — fathers and sons together — showing no pity, no compassion, and no mercy. I will destroy them, declares the LORD.",
      "T": "I will hurl them against each other — fathers into sons — without pity, without mercy, without holding back. I will destroy them. Yahweh declares it."
    },
    "15": {
      "L": "Hear, and give ear; do not be proud; for the LORD has spoken.",
      "M": "Hear and pay attention; do not be arrogant; for the LORD has spoken.",
      "T": "Listen. Pay attention. Stop being proud. Yahweh has spoken."
    },
    "16": {
      "L": "Give glory to the LORD your God before he brings darkness, before your feet stumble on the twilight mountains, and while you hope for light he turns it into deep shadow and makes it pitch dark.",
      "M": "Give honor to the LORD your God before he brings darkness — before your feet stumble on the darkening mountains. While you still look for light, he will turn it into gloom and make it pitch black.",
      "T": "Honor Yahweh your God while there is still time — before the darkness comes, before you are stumbling on the hills at twilight, reaching for light that turns to dense shadow under your hand."
    },
    "17": {
      "L": "But if you will not hear it, my soul shall weep in secret over your pride; my eye shall weep bitterly and run down with tears, because the LORD's flock has been carried away captive.",
      "M": "But if you will not listen, I will weep in private for your pride; my eyes will overflow with bitter tears, because the LORD's flock will be taken into exile.",
      "T": "But if you will not listen — I will go away and weep in private over your stubborn pride. My eyes will stream with tears, because Yahweh's own flock is being led away into exile."
    },
    "18": {
      "L": "Say to the king and to the queen mother: Humble yourselves, sit down; for your positions of leadership shall come down, even the crown of your glory.",
      "M": "Say to the king and to the queen mother: Take a lower place and sit down; your positions of authority will be stripped away — even the crown of your glory.",
      "T": "Tell the king and the queen mother: Come down from your thrones. Take the low seat. The authority you hold is being stripped away — even the crown of your magnificence will fall."
    },
    "19": {
      "L": "The cities of the south shall be shut up with none to open them; Judah shall be carried away captive — all of it wholly taken into exile.",
      "M": "The towns of the Negev will be locked shut with no one to open them; all of Judah will be taken into captivity — every last person carried away.",
      "T": "The towns of the Negev will be sealed — locked, with no one to open them. Judah will go into exile — not some of it, all of it, taken away completely."
    },
    "20": {
      "L": "Lift up your eyes and see those who come from the north; where is the flock that was given to you, your beautiful flock?",
      "M": "Look up and see those who are coming from the north. Where is the flock that was entrusted to you — your prized flock?",
      "T": "Look north. Do you see what is coming? Where is the flock that was placed in your care — your beautiful flock? Where is it now?"
    },
    "21": {
      "L": "What will you say when he sets over you those whom you yourself trained to be chiefs? Shall not pain seize you like a woman in travail?",
      "M": "What will you say when he punishes you — when those you trained as your allies are placed over you as rulers? Will not agony seize you like a woman in labor?",
      "T": "What will you say when he brings judgment? You trained those nations as your allies — now they will be set over you as your masters. The anguish that comes will grip you like labor pains."
    },
    "22": {
      "L": "And if you say in your heart: Why have these things come upon me? — For the greatness of your iniquity your skirts are stripped away and your heels are exposed.",
      "M": "And if you ask yourself: Why have all these things happened to me? — it is because of the magnitude of your guilt that your skirts are lifted and your nakedness exposed.",
      "T": "And if you ask yourself, 'Why has this happened to me?' — the answer is your own sin, vast and accumulated. Your shame is being stripped bare before everyone. This is what your guilt has earned."
    },
    "23": {
      "L": "Can the Ethiopian change his skin or the leopard his spots? Then also you can do good, you who are accustomed to doing evil.",
      "M": "Can a Cushite change the color of his skin, or a leopard its spots? Neither can you do good, you who are so practiced at doing evil.",
      "T": "Can an Ethiopian change his skin? Can a leopard change its spots? No more can you do good — you who have trained yourselves so thoroughly in evil."
    },
    "24": {
      "L": "Therefore I will scatter them as stubble that passes away before the desert wind.",
      "M": "Therefore I will scatter them like chaff blown away by a desert wind.",
      "T": "So I will scatter them like dry chaff before the desert wind — gone without a trace."
    },
    "25": {
      "L": "This is your lot, the portion I have measured out to you, says the LORD; because you have forgotten me and trusted in falsehood.",
      "M": "This is your lot — the allotted portion I have assigned to you, declares the LORD — because you have forgotten me and put your trust in lies.",
      "T": "This is the portion Yahweh has measured out and assigned to you. You forgot him. You put your trust in lies. This is what that earns."
    },
    "26": {
      "L": "I will therefore lift your skirts over your face so that your shame may be seen.",
      "M": "So I will pull your skirts up over your face and expose your shameful nakedness.",
      "T": "So I will strip you bare — your own skirts pulled up over your face, your shame on display before all."
    },
    "27": {
      "L": "I have seen your adulteries and your neighings, the lewdness of your whoredom and your abominations on the hills and in the fields. Woe to you, O Jerusalem! How long will it be before you are made clean?",
      "M": "I have seen your adulteries and your lustful cries, the obscene acts of your prostitution, and your detestable practices on the hills and in the fields. Woe to you, Jerusalem! Will you never be clean? When will it ever happen?",
      "T": "I have seen it all — your acts of unfaithfulness, your panting lust, the lewd shamelessness of your idol-worship on every hill and in every field. Woe to you, Jerusalem! Will you ever be clean? Will that day ever come?"
    }
  },
  "14": {
    "1": {
      "L": "The word of the LORD that came to Jeremiah concerning the drought:",
      "M": "The word that came to Jeremiah from the LORD concerning the drought:",
      "T": "This is the word Yahweh spoke to Jeremiah about the great drought:"
    },
    "2": {
      "L": "Judah mourns and her gates languish; they are in mourning on the ground, and the cry of Jerusalem has gone up.",
      "M": "Judah mourns; her city gates droop in gloom; the people sit on the ground in dark mourning, and the cry of Jerusalem goes up.",
      "T": "Judah mourns. The gates of her cities droop — dressed in mourning, slumped to the ground. Jerusalem's cry of anguish rises up."
    },
    "3": {
      "L": "Their nobles send their servants to the cisterns; they come to the pits and find no water; they return with empty vessels; they are ashamed and confounded and cover their heads.",
      "M": "Their officials send servants to the cisterns for water; they come to the pits and find them dry; they return with empty jars — in shame and confusion they cover their heads.",
      "T": "The nobles send their servants to fetch water. The servants come to the cisterns — dry. They return with empty jars, bowed in shame, covering their heads."
    },
    "4": {
      "L": "Because the ground is cracked, for there has been no rain in the land, the farmers are dismayed; they cover their heads.",
      "M": "Because the ground is cracked open — there has been no rain — the farmers are dismayed; they too cover their heads.",
      "T": "The ground is split open in cracks — no rain has fallen. The farmers stand looking at it in despair, covering their heads in grief."
    },
    "5": {
      "L": "Even the doe in the field forsakes her newborn fawn because there is no grass.",
      "M": "Even the doe in the open field abandons her newborn fawn because there is no grass.",
      "T": "Even the deer in the open field abandons her fawn. There is nothing to eat. She cannot stay with what she has no strength to feed."
    },
    "6": {
      "L": "The wild donkeys stand on the bare heights; they pant for air like jackals; their eyes fail because there is no vegetation.",
      "M": "The wild donkeys stand on the barren ridges; they gasp for air like jackals; their eyes grow dim because there is no grass.",
      "T": "Wild donkeys stand on the bare hilltops, gasping for breath like jackals, their eyes going hollow because there is nothing green anywhere."
    },
    "7": {
      "L": "O LORD, though our iniquities testify against us, act for your name's sake; for our backslidings are many; we have sinned against you.",
      "M": "O LORD, though our sins testify against us, act for the sake of your name; for our unfaithfulness is many times over; we have sinned against you.",
      "T": "LORD, our sins speak against us — we know it. But act anyway, for your name's sake. We have strayed again and again; we have sinned against you."
    },
    "8": {
      "L": "O hope of Israel, its savior in time of trouble — why do you act like a stranger in the land, like a traveler who turns aside to stay only for a night?",
      "M": "O hope of Israel, its deliverer in times of trouble — why are you acting like a foreigner in the land, like a traveler who only stops for a night?",
      "T": "Israel's hope, Israel's rescuer in times of disaster — why are you behaving like a stranger here, like a passing traveler who only stops for one night and then moves on?"
    },
    "9": {
      "L": "Why should you be as a man in a stupor, as a warrior who cannot save? Yet you, O LORD, are in the midst of us, and we are called by your name; do not forsake us!",
      "M": "Why are you like a man suddenly confused, like a warrior who is powerless to save? You are still in the midst of us, LORD, and we bear your name — do not abandon us!",
      "T": "Why do you stand there stunned, like a warrior with his hands tied? You are here, LORD, among us. We carry your name. Do not walk away from us."
    },
    "10": {
      "L": "Thus says the LORD to this people: They have loved to wander in this way; they have not restrained their feet; therefore the LORD does not accept them; he will now remember their iniquity and punish their sins.",
      "M": "This is what the LORD says about this people: They have loved to wander; they have not restrained their feet; therefore the LORD takes no pleasure in them. He will now call their guilt to account and punish their sins.",
      "T": "Yahweh says this about these people: They have chosen to wander — again and again, never pulling themselves back. So Yahweh will not accept them. He is bringing their guilt to mind right now, and he will call them to account for every sin."
    },
    "11": {
      "L": "Then the LORD said to me: Do not pray for this people for their good.",
      "M": "Then the LORD said to me: Do not pray for the welfare of this people.",
      "T": "Then Yahweh said to me: Do not pray for these people's well-being. Not anymore."
    },
    "12": {
      "L": "When they fast, I will not hear their cry; and when they offer burnt offering and grain offering, I will not accept them; but I will consume them by the sword, by famine, and by pestilence.",
      "M": "When they fast, I will not listen to their crying. When they bring burnt offerings and grain offerings, I will not accept them. I will destroy them by the sword, by famine, and by plague.",
      "T": "When they fast, I will not hear their cries. When they bring burnt offerings and grain offerings, I will not accept a single one. I will finish them — by the sword, by starvation, by disease."
    },
    "13": {
      "L": "Then I said: Ah, Lord GOD! Behold, the prophets are saying to them: You will not see the sword, and you will have no famine; but I will give you lasting peace in this place.",
      "M": "Then I said: Oh, Lord GOD! The prophets are telling them: You will not face war, and famine will not come to you — I will give you certain and lasting peace in this place.",
      "T": "Then I said: Lord Yahweh, the prophets are telling them the exact opposite of what you told me. They say: 'You will not face the sword. No famine is coming. Yahweh is giving you real and lasting peace right here.'"
    },
    "14": {
      "L": "Then the LORD said to me: The prophets are prophesying lies in my name; I did not send them, nor did I command them, nor did I speak to them; they are prophesying to you a false vision, divination, a worthless thing, and the deceit of their own hearts.",
      "M": "Then the LORD said to me: The prophets are prophesying falsehoods in my name. I did not send them, I did not command them, and I did not speak to them. They are giving you a false vision, empty divination, the delusion of their own imagination.",
      "T": "Yahweh answered me: Those prophets are lying in my name. I never sent them. I never commanded them. I never spoke to them. What they offer you is false vision, empty divination, the tricks of their own minds — a web of self-deception."
    },
    "15": {
      "L": "Therefore thus says the LORD concerning the prophets who prophesy in my name, whom I did not send — yet who say: Sword and famine will not come to this land — those prophets will be consumed by sword and famine.",
      "M": "Therefore this is what the LORD says about the prophets who prophesy in my name — whom I did not send — and who say: No sword or famine will touch this land. Those very prophets will die by sword and famine.",
      "T": "So Yahweh says this about those prophets who preach in his name — whom he never sent — who keep saying: No sword, no famine will touch this land. Those prophets will die by the very sword and famine they said would never come."
    },
    "16": {
      "L": "And the people to whom they prophesy will be cast out in the streets of Jerusalem because of famine and sword; and there will be no one to bury them — them, their wives, their sons, and their daughters; for I will pour their wickedness out upon them.",
      "M": "And the people they are prophesying to will be thrown into the streets of Jerusalem, killed by famine and sword; no one will be left to bury them — them, their wives, their sons, their daughters; for I will pour their own wickedness back on them.",
      "T": "And those who believe these false prophets will end up thrown into the streets of Jerusalem, dead from famine and sword — with no one left to bury them. Not them, not their wives, not their sons, not their daughters. Their wickedness is coming back down on them — poured straight from Yahweh's hand."
    },
    "17": {
      "L": "Therefore speak this word to them: Let my eyes run down with tears night and day and not cease; for the virgin daughter of my people is broken with a great breach, with a very grievous blow.",
      "M": "Say this word to them: Let my eyes overflow with tears night and day without stopping; for the virgin daughter of my people is shattered with a terrible wound — a blow beyond healing.",
      "T": "Say this to them: My eyes cannot stop weeping — night and day, without rest — because the virgin daughter of my people has been shattered. The blow is devastating, the wound beyond healing."
    },
    "18": {
      "L": "If I go out into the field, behold, those slain by the sword! And if I enter the city, behold, those sick with famine! Both prophet and priest have gone about to a land they do not know.",
      "M": "If I go out to the countryside, I see those slain by the sword; if I go into the city, I see those wasted by famine. Both prophet and priest go wandering in a land they no longer know.",
      "T": "If I walk out into the fields — bodies slain by the sword. If I go into the city — people wasting away from hunger. Prophet and priest alike stumble through a land they no longer recognize."
    },
    "19": {
      "L": "Have you utterly rejected Judah? Does your soul loathe Zion? Why have you struck us so that there is no healing for us? We looked for peace but there was no good; for a time of healing but behold, trouble!",
      "M": "Have you completely rejected Judah? Does your very being recoil from Zion? Why did you strike us with no healing left? We hoped for peace, but nothing good came; we waited for a time of healing, but only terror followed.",
      "T": "Have you cast Judah away for good? Does Zion disgust you to the core? Why did you strike us with a wound that no one can heal? We hoped for peace — nothing came. We waited for healing — and trouble came instead."
    },
    "20": {
      "L": "We acknowledge, O LORD, our wickedness and the iniquity of our fathers, for we have sinned against you.",
      "M": "We acknowledge, O LORD, our own wickedness and the sins of our ancestors; for we have sinned against you.",
      "T": "We confess it, LORD. Our own wickedness, our fathers' iniquity — we own all of it. We have sinned against you."
    },
    "21": {
      "L": "Do not abhor us, for your name's sake; do not disgrace the throne of your glory; remember, and do not break your covenant with us.",
      "M": "For the sake of your name, do not despise us; do not dishonor the throne of your glory; remember your covenant with us — do not break it.",
      "T": "Do not cast us off, Yahweh — not for our sake but for your own name's sake. Do not let your glorious throne be brought to shame. Remember your covenant. Do not shatter it."
    },
    "22": {
      "L": "Are there any among the idols of the nations that can bring rain? Or can the heavens of themselves give showers? Is it not you, O LORD our God? Therefore we will wait on you, for you have made all these things.",
      "M": "Are there any among the idols of the nations that can make it rain? Or can the sky send showers by itself? You are the one, O LORD our God. We will wait on you, for you have made all these things.",
      "T": "Can any idol of any nation make it rain? Can the sky decide on its own to send showers? Only you can do it, LORD our God. So we will wait on you. You made all of this — you can restore it."
    }
  },
  "15": {
    "1": {
      "L": "Then the LORD said to me: Though Moses and Samuel stood before me, my soul would not be toward this people; cast them out of my sight and let them go forth.",
      "M": "Then the LORD said to me: Even if Moses and Samuel stood before me, my heart would not be moved toward this people. Send them away from my presence; let them go.",
      "T": "Then Yahweh said to me: Even if Moses himself stood before me — even Samuel — my heart would feel nothing toward this people. Send them away. Let them go."
    },
    "2": {
      "L": "And when they say to you: Where shall we go? — then you shall tell them: Thus says the LORD: Those for death, to death; those for the sword, to the sword; those for famine, to famine; those for captivity, to captivity.",
      "M": "When they ask you: Where are we supposed to go? tell them: This is what the LORD says — Those destined for death will face death; those for the sword, the sword; those for famine, famine; those for captivity, captivity.",
      "T": "When they ask you — 'Where are we supposed to go?' — give them Yahweh's answer: The ones meant for death will die. The ones meant for the sword will fall by the sword. The ones meant for famine will starve. The ones meant for exile will go into exile."
    },
    "3": {
      "L": "I will appoint over them four kinds, says the LORD: the sword to kill, and dogs to drag away, and the birds of the sky and the beasts of the earth to devour and to destroy.",
      "M": "I will send four kinds of destroyers against them, declares the LORD: the sword to kill, dogs to drag away the bodies, birds of the sky and wild animals to devour and finish them off.",
      "T": "I will unleash four agents of destruction against them, says Yahweh: the sword to kill, dogs to drag away the bodies, birds of the sky and wild beasts to devour and leave nothing behind."
    },
    "4": {
      "L": "And I will make them an object of horror to all the kingdoms of the earth because of Manasseh son of Hezekiah, king of Judah, for what he did in Jerusalem.",
      "M": "I will make them a terrifying sight to all the kingdoms of the earth, because of Manasseh son of Hezekiah, king of Judah, and what he did in Jerusalem.",
      "T": "I will make them an object of terror to every nation on earth — because of what Manasseh son of Hezekiah did in Jerusalem. His sins set all of this in motion."
    },
    "5": {
      "L": "For who will pity you, O Jerusalem? Who will mourn for you? Who will turn aside to ask how you are?",
      "M": "For who will feel sorry for you, O Jerusalem? Who will grieve over you? Who will stop to ask how you are doing?",
      "T": "Who will have any pity on you, Jerusalem? Who will mourn for you? Who will even pause long enough to ask if you are all right?"
    },
    "6": {
      "L": "You have forsaken me, says the LORD; you have gone backward; therefore I will stretch out my hand against you and destroy you — I am weary of relenting.",
      "M": "You have abandoned me, declares the LORD; you keep going backward; so I will stretch out my hand against you and destroy you. I am tired of changing my mind about you.",
      "T": "You have walked away from me, says Yahweh. You keep retreating further. So I am stretching out my hand against you — to destroy you. I am exhausted with relenting."
    },
    "7": {
      "L": "I will fan them with a winnowing fan in the gates of the land; I will bereave them of children and destroy my people, since they do not return from their ways.",
      "M": "I will winnow them with a fan in the gateways of the land; I will strip them of their children and destroy my people, since they refuse to turn from their ways.",
      "T": "I will scatter them like grain tossed to the wind, winnowing them in every gateway of this land. I will take their children from them. I will destroy my people — because they will not turn back from their ways."
    },
    "8": {
      "L": "Their widows have become more numerous to me than the sand of the seas; I have brought against the mother of young men a destroyer at noonday; I have suddenly caused anguish and terrors to fall upon her, upon the city.",
      "M": "Their widows have become more numerous to me than the sand of the sea; I have brought a destroyer at midday against the mother of young men; suddenly I have made anguish and terror fall upon her — upon the city.",
      "T": "Their widows outnumber the sand of the sea — that is how many young men I have taken. I brought a destroyer down on them at noonday, in broad daylight, without warning. Terror fell on that city all at once."
    },
    "9": {
      "L": "She who bore seven has breathed her last; her sun has gone down while it was yet day; she has been shamed and humiliated; and the survivors I will give over to the sword before their enemies, says the LORD.",
      "M": "The mother of seven gasps her last breath; her sun goes down while it is still midday; she is left in shame and disgrace; and whatever survives I will hand over to the sword before their enemies, declares the LORD.",
      "T": "The woman who bore seven sons collapses — her sun goes down in the middle of the afternoon. She is left in shame and ruin. And whatever survivors remain, I will hand over to the sword before their enemies. Yahweh declares it."
    },
    "10": {
      "L": "Woe to me, my mother, that you bore me a man of strife and contention to the whole earth! I have neither lent at interest nor borrowed at interest; yet every one of them curses me.",
      "M": "Woe to me, my mother, that you gave birth to me as a man of contention and strife to the whole world! I have neither loaned money at interest nor borrowed it — yet everyone curses me.",
      "T": "Woe to me, Mother, that you ever gave birth to me — a man set against the whole world, with every hand against me. I never loaned money at interest, never borrowed it either. And yet everyone curses me."
    },
    "11": {
      "L": "The LORD said: Truly it will be well with your remnant; truly I will make your enemies entreat you in a time of disaster and in a time of distress.",
      "M": "The LORD said: Surely I will set what remains of you free for good purposes; surely I will make your enemies appeal to you in times of disaster and distress.",
      "T": "Yahweh answered: I will not waste whatever remains of you. I will put you to good purpose. And in the time of disaster and distress, your very enemies will come to you and plead."
    },
    "12": {
      "L": "Can iron break iron from the north, and bronze?",
      "M": "Can iron shatter iron from the north — or even bronze?",
      "T": "Can ordinary iron shatter northern iron — forged harder, mixed with bronze? It cannot."
    },
    "13": {
      "L": "Your wealth and your treasures I will give as plunder, without payment, because of all your sins throughout all your territory.",
      "M": "Your wealth and your treasures I will hand over to plunder — free of charge — because of all your sins, throughout all your borders.",
      "T": "Your wealth and all your treasures — I will give them as plunder, not as ransom, not for any price — simply because of the weight of your sins across this entire land."
    },
    "14": {
      "L": "I will make you pass with your enemies into a land you do not know; for a fire is kindled in my anger that will burn against you.",
      "M": "I will send you into exile with your enemies, into a land you have never known; for a fire has been kindled by my anger, and it will burn against you.",
      "T": "I will carry you away with your enemies into a land you have never set foot in. For a fire has been lit by my anger — and it is burning toward you."
    },
    "15": {
      "L": "You know, O LORD; remember me and visit me and avenge me on my persecutors; in your patience do not take me away; know that for your sake I bear reproach.",
      "M": "You know, O LORD; remember me and care for me, and take vengeance for me against those who persecute me; do not in your forbearance let me be swept away — know that for your sake I endure reproach.",
      "T": "You know, LORD — you know everything. Remember me. Come to me. Take vengeance on those who hunt me down. Do not in your long patience let me be destroyed before you act. Know this: it is for your sake that I carry this reproach."
    },
    "16": {
      "L": "Your words were found and I ate them; and your word was to me the joy and delight of my heart; for I am called by your name, O LORD, God of hosts.",
      "M": "When I found your words, I devoured them; your word was my joy and the delight of my heart; for I bear your name, O LORD, God of hosts.",
      "T": "When your words came, I took them in like food — I ate them up. Your word was my joy, the deep delight of my heart. For I bear your name, LORD God of hosts. That is who I am."
    },
    "17": {
      "L": "I did not sit in the assembly of those who make merry, nor did I rejoice; I sat alone because of your hand; for you have filled me with indignation.",
      "M": "I did not sit in the company of those who celebrate, nor did I join their rejoicing; I sat alone because your hand was on me, for you have filled me with holy indignation.",
      "T": "I never sat with the crowd of merrymakers, never joined in their laughter. I sat alone — because your hand was on me, because you had filled me to the brim with righteous anger."
    },
    "18": {
      "L": "Why is my pain perpetual and my wound incurable, refusing to be healed? Will you be to me altogether like a deceptive brook, like waters that fail?",
      "M": "Why is my pain unending and my wound incurable, refusing to heal? Are you really going to be to me like a deceptive stream — like waters that run dry?",
      "T": "Why does my pain never end? Why does my wound refuse to heal? Are you really going to be to me what a dry wadi is to a thirsty traveler — a promise of water that disappears when you need it most?"
    },
    "19": {
      "L": "Therefore thus says the LORD: If you return, then I will restore you; you shall stand before me; and if you take the precious from the worthless, you shall be as my mouth; they shall return to you, but you shall not return to them.",
      "M": "Therefore this is what the LORD says: If you return to me, I will restore you; you will stand before me; and if you distinguish the precious from the worthless, you will serve as my spokesman; let them turn to you, but do not you turn to them.",
      "T": "So Yahweh says: If you come back to me, I will bring you back. You will stand before me again. But you must be able to separate the precious from the worthless — only then will you be my voice. They must come around to you. You must not go around to them."
    },
    "20": {
      "L": "And I will make you before this people a fortified wall of bronze; they will fight against you, but they shall not prevail over you; for I am with you to save you and to deliver you, says the LORD.",
      "M": "I will make you to this people like a fortified bronze wall; they will attack you but will not overcome you; for I am with you to save and deliver you, declares the LORD.",
      "T": "I will make you a wall of solid bronze before this people — fortified, immovable. They will attack you, but they will not break through. For I am with you, says Yahweh, to rescue you and pull you through."
    },
    "21": {
      "L": "And I will deliver you out of the hand of the wicked, and I will redeem you from the grip of the ruthless.",
      "M": "I will deliver you from the power of the wicked and rescue you from the grasp of the ruthless.",
      "T": "I will pull you out of the hands of the wicked. I will redeem you from the grip of the violent and the cruel."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 13–15 written.')

if __name__ == '__main__':
    main()
