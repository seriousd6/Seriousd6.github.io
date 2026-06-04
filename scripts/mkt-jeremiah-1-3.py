"""
MKT Jeremiah chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-1-3.py

Translation decisions:
- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name force is
  significant (call narrative, oracles, covenant declarations). "the LORD" in T for narrative
  quotation formulas. Consistent with all completed Isaiah scripts.
- H136 (אֲדֹנָי) + H3069 (יֱהוִה) compound: "Lord GOD" in L/M (GOD marks the
  tetragrammaton variant); "Lord GOD" maintained in T except 1:6 where "Lord GOD" is the
  cry of the newly-called prophet — kept verbatim for its emotional weight.
- H430 (אֱלֹהִים): "God" in all tiers throughout.
- H1697 (דָּבָר): "word" in L/M; "word" retained in T — the prophetic-word formula is too
  load-bearing theologically to paraphrase.
- H2617 (חֶסֶד): appears at 2:2 ("the kindness/love of your espousals"). L: "kindness";
  M: "devotion"; T: "tenderness" — the courtship-love nuance in context is captured by
  "tenderness" rather than the fuller covenant-loyalty sense that dominates elsewhere.
- H5315 (נֶפֶשׁ): 2:34 "souls of the innocent poor" — L: "souls"; M: "lifeblood" (capturing
  the nexus of life-force and blood in OT death contexts); T: "blood of the innocent" — the
  rhetorical thrust is the stain on the clothing.
- H7307 (רוּחַ): 2:24 "snuffing up the wind" — literal wind/breath; not capitalised. No
  divine-Spirit use in these three chapters.
- H1285 (בְּרִית): 3:16 "covenant" in all tiers — the full weight of the formal covenant
  structure is theologically required.
- H4878 (מְשׁוּבָה): "backsliding/faithlessness/apostasy" — a key Jeremiah term. L: "backsliding"
  (the KJV-tradition word most readers recognise); M: "faithlessness"; T: "faithless" / "wayward"
  — varying to avoid monotony while keeping the defection-from-covenant sense.
- H7451 (רָעָה): "evil" / "disaster" / "wickedness" — context-sensitive. When describing
  divine judgment coming, L/M "disaster" (national calamity); when describing Israel's moral
  state, "wickedness" or "evil."
- H5030 (נָבִיא): "prophet" in all tiers.
- H2181 (זָנָה): "play the harlot" (L); "commit prostitution/live as a prostitute" (M);
  "gave herself away / played the whore / spiritual adultery" (T) — the metaphor is covenant
  infidelity figured as sexual betrayal; T surfaces this explicitly.
- H1168 (בַּעַל / Baalim): proper name "Baal/Baals/Baalim" in all tiers — no gloss substitution.
- H2623 (חָסִיד): 3:12 "merciful" (adj. of one who shows hesed). L: "merciful"; M: "faithful
  in love"; T: "a God of steadfast love."
- H1322 (בֹּשֶׁת): 3:24 "shame" — this is the prophetic nickname for Baal (the Shameful Thing);
  documented explicitly in T.

Structural notes:
  Ch. 1 — The Call Narrative. One of the OT's most theologically dense commissions: divine
  foreknowledge (v. 5), prophetic reluctance (v. 6), divine empowerment (v. 9), the scope of the
  mandate (v. 10), two visions (almond rod vv. 11–12, boiling pot vv. 13–14), and the charge
  (vv. 17–19). The almond-rod vision (vv. 11–12) contains a Hebrew pun: שָׁקֵד (shaqed,
  "almond") sounds like שֹׁקֵד (shoqed, "watching/hastening"). The boiling pot facing north
  anticipates the Babylonian threat that dominates the book. The call structure parallels Moses
  (Exod 3–4) and Isaiah (Isa 6) in its movement: vision → objection → divine reassurance.

  Ch. 2 — The Covenant Lawsuit (rib). Verses 4–37 are a formal covenant legal dispute (Hebrew
  rib) in which Yahweh as plaintiff indicts Israel as defendant before a cosmic court (heavens, v.
  12). Structure: summons (vv. 4–5) → historical indictment (vv. 6–8) → astonishment of heavens
  (vv. 10–13) → double evidence (broken cisterns + geopolitical shame, vv. 13–18) → self-
  incriminating confession of innocence (vv. 23–35) → final verdict (vv. 36–37). The
  broken-cisterns image (v. 13) is among the most quoted in Jeremiah: Israel exchanged the
  living spring of Yahweh for cisterns she hewed herself — already cracked.

  Ch. 3 — Return, O Faithless Israel. Structured as an alternation of accusation and appeal:
  divorce-law impossibility (vv. 1–5) → comparison of Israel and Judah (vv. 6–11) → appeal to
  northern Israel to return (vv. 12–18) → Zion-gathering vision (vv. 14–18) → Judah's heart
  (vv. 19–25). The chapter ends with Israel's penitential confession (vv. 22–25) — the only
  such extended corporate confession of guilt in the early chapters of Jeremiah. Verse 16's
  promise that the ark of the covenant will be forgotten (superseded, not mourned) is
  theologically startling: the new covenant will not need the old cult furniture.

OT echoes and NT resonances:
  1:5 — "before I formed you in the womb I knew you" — echoed in Ps 139:13–16; Paul applies
  the same calling-in-the-womb language to himself in Gal 1:15.
  1:9 — "I have put my words in your mouth" — echoes Deut 18:18 (the prophet like Moses).
  1:10 — "to root out and to pull down… to build and to plant" — these six verbs recur as a
  structural refrain across the book (e.g., 12:14–17; 18:7–9; 24:6; 31:28; 42:10; 45:4).
  2:2 — "love of your espousals in the wilderness" — echoes the wilderness-betrothal motif of
  Hosea 2:14–15; Ezekiel 16 extends it at length.
  2:13 — "fountain of living waters / broken cisterns" — echoed in John 4:10–14; 7:38.
  3:1 — Deuteronomy 24:1–4 is the law being cited.
  3:16–17 — the ark superseded by Jerusalem as throne — anticipates the new-covenant vision of
  Jer 31:31–34; the throne-of-the-LORD image foreshadows Ezek 43 and Rev 22:3.

Aspect notes:
  1:5 — the yiqtol forms ("I formed," "I knew," "I sanctified") in the context of beforehand
  divine action render as English simple past; "ordained" is a perfect aspect with permanent
  effect ("it stands appointed").
  2:20 — the Hebrew is a first-person imperfect with negation: "I will not serve/transgress"
  — Israel's arrogant self-declaration. Aorist-equivalent: a decisive, completed declaration.
  3:12 — the hiphil imperfect "I will not cause my anger to fall" — ongoing conditional
  promise; T gives it its full covenantal weight.
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
  "1": {
    "1": {
      "L": "The words of Jeremiah son of Hilkiah, of the priests who were in Anathoth in the land of Benjamin,",
      "M": "The words of Jeremiah son of Hilkiah, of the priests in Anathoth in the land of Benjamin,",
      "T": "These are the words of Jeremiah — son of Hilkiah, a priest from Anathoth in the territory of Benjamin."
    },
    "2": {
      "L": "to whom the word of the LORD came in the days of Josiah son of Amon, king of Judah, in the thirteenth year of his reign,",
      "M": "The word of the LORD came to him in the days of Josiah son of Amon, king of Judah, in the thirteenth year of his reign,",
      "T": "Yahweh's word first came to him in the thirteenth year of King Josiah son of Amon of Judah."
    },
    "3": {
      "L": "It came also in the days of Jehoiakim son of Josiah, king of Judah, until the end of the eleventh year of Zedekiah son of Josiah, king of Judah, until the carrying away of Jerusalem captive in the fifth month.",
      "M": "It came again in the days of Jehoiakim son of Josiah, king of Judah, continuing through the eleventh year of Zedekiah son of Josiah, king of Judah, until Jerusalem was carried away captive in the fifth month.",
      "T": "The word kept coming through the days of Jehoiakim son of Josiah, right up to the eleventh year of Zedekiah son of Josiah — until Jerusalem went into exile in the fifth month."
    },
    "4": {
      "L": "Then the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "5": {
      "L": "Before I formed you in the belly I knew you, and before you came forth from the womb I sanctified you; I ordained you a prophet to the nations.",
      "M": "Before I formed you in the womb I knew you, and before you were born I consecrated you; I appointed you a prophet to the nations.",
      "T": "Before I shaped you in the womb I chose you. Before you drew your first breath I set you apart — I appointed you to be a prophet to the nations."
    },
    "6": {
      "L": "Then I said: 'Ah, Lord GOD! Behold, I cannot speak, for I am a child.'",
      "M": "I said: 'Ah, Lord GOD! I do not know how to speak, for I am only a child.'",
      "T": "'Ah, Lord GOD,' I said, 'I do not know how to speak — I am too young for this.'"
    },
    "7": {
      "L": "But the LORD said to me: 'Do not say, \"I am a child,\" for you shall go to all to whom I send you, and whatever I command you you shall speak.'",
      "M": "But the LORD said to me: 'Do not say, \"I am a child,\" for you shall go to everyone I send you to, and you shall speak everything I command you.'",
      "T": "'Do not say you are too young,' the LORD answered. 'You will go to everyone I send you to, and every word I give you, you will speak.'"
    },
    "8": {
      "L": "Do not be afraid of their faces, for I am with you to deliver you, says the LORD.",
      "M": "Do not be afraid of them, for I am with you to rescue you, declares the LORD.",
      "T": "Do not fear them. I will be with you to rescue you — Yahweh's promise."
    },
    "9": {
      "L": "Then the LORD put forth his hand and touched my mouth. And the LORD said to me: 'Behold, I have put my words in your mouth.'",
      "M": "Then the LORD reached out his hand and touched my mouth. The LORD said to me: 'See, I have placed my words in your mouth.'",
      "T": "Then Yahweh reached out and touched my mouth. 'Look,' he said, 'I have put my very words in your mouth.'"
    },
    "10": {
      "L": "See, I have this day set you over the nations and over the kingdoms, to root out and to pull down, and to destroy and to throw down, to build and to plant.",
      "M": "See, I have appointed you this day over nations and kingdoms, to uproot and to tear down, to destroy and to demolish, to build and to plant.",
      "T": "Today I am setting you over nations and kingdoms — to uproot and tear down, to destroy and demolish, but also to build and to plant."
    },
    "11": {
      "L": "Moreover the word of the LORD came to me, saying: 'Jeremiah, what do you see?' And I said: 'I see a rod of an almond tree.'",
      "M": "The word of the LORD came to me: 'What do you see, Jeremiah?' I replied: 'I see a branch of an almond tree.'",
      "T": "Then the LORD's word came to me: 'What do you see, Jeremiah?' 'I see a branch from an almond tree,' I answered."
    },
    "12": {
      "L": "Then the LORD said to me: 'You have seen well, for I am watching over my word to perform it.'",
      "M": "The LORD said to me: 'You have seen rightly, for I am watching over my word to carry it out.'",
      "T": "The LORD said: 'You have seen rightly. I am watching — alert and awake — to make certain my word comes to pass.'"
    },
    "13": {
      "L": "And the word of the LORD came to me the second time, saying: 'What do you see?' And I said: 'I see a seething pot, and its face is toward the north.'",
      "M": "The word of the LORD came to me a second time: 'What do you see?' I said: 'I see a boiling pot, with its mouth turned from the north.'",
      "T": "The word of the LORD came to me a second time: 'What do you see?' 'I see a boiling pot,' I replied, 'and it is tilted toward us from the north.'"
    },
    "14": {
      "L": "Then the LORD said to me: 'Out of the north an evil shall break forth upon all the inhabitants of the land.'",
      "M": "The LORD said to me: 'Disaster will break out from the north against all who live in this land.'",
      "T": "'Out of the north disaster will pour over everyone who lives in this land,' the LORD told me."
    },
    "15": {
      "L": "For behold, I will call all the families of the kingdoms of the north, says the LORD; and they shall come and every one shall set his throne at the entering of the gates of Jerusalem, and against all the walls thereof round about, and against all the cities of Judah.",
      "M": "For see, I am summoning all the peoples of the kingdoms of the north, declares the LORD. They will come and will each set up his throne at the entrance to the gates of Jerusalem, surrounding its walls on all sides and advancing against all the cities of Judah.",
      "T": "I am summoning every kingdom of the north — Yahweh declares it. They will come, and every king will plant his throne right at Jerusalem's gates, surrounding her walls and bearing down on every city of Judah."
    },
    "16": {
      "L": "And I will utter my judgments against them touching all their wickedness, who have forsaken me, and have burned incense to other gods, and worshipped the works of their own hands.",
      "M": "I will pronounce my judgments against them for all their wickedness — they have forsaken me, burned incense to other gods, and bowed down to the works of their own hands.",
      "T": "I will declare my verdict against them for everything they have done: they have abandoned me, offered incense to foreign gods, and prostrated themselves before what their own hands have made."
    },
    "17": {
      "L": "You therefore gird up your loins, and arise and speak unto them all that I command you; be not dismayed at their faces, lest I confound you before them.",
      "M": "As for you, get yourself ready. Arise and speak to them everything I command you. Do not be terrified by them, or I will terrify you before them.",
      "T": "Now — brace yourself. Stand up and speak to them everything I command you. Do not lose your nerve in front of them, or I will make you lose it. They must see no fear in you."
    },
    "18": {
      "L": "For behold, I have made you this day a fortified city, and an iron pillar, and walls of bronze against the whole land — against the kings of Judah, against its princes, against its priests, and against the people of the land.",
      "M": "See, I have made you today a fortified city, an iron pillar, and bronze walls to stand against the whole land — against Judah's kings and officials, against its priests and all the people of the land.",
      "T": "I have made you into something indestructible: a fortress city, an iron post, a wall of bronze — facing the whole country, facing Judah's kings and princes, its priests and all its people."
    },
    "19": {
      "L": "And they shall fight against you; but they shall not prevail against you, for I am with you, says the LORD, to deliver you.",
      "M": "They will fight against you, but they will not overcome you, for I am with you to rescue you, declares the LORD.",
      "T": "They will come at you, but they will not break you — for I am with you, and I will rescue you. This is Yahweh's word."
    }
  },
  "2": {
    "1": {
      "L": "Moreover the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Go and cry in the ears of Jerusalem, saying: Thus says the LORD — 'I remember for you the kindness of your youth, the love of your espousals, how you walked after me in the wilderness, in a land that was not sown.'",
      "M": "Go and call out to Jerusalem: This is what the LORD says: 'I remember the devotion of your youth, the love of your bridal days, how you followed me through the wilderness, through a land that was not sown.'",
      "T": "'Go and shout this into Jerusalem's ears,' Yahweh said. 'I remember how you loved me when you were young — the tenderness of your early days, how you followed me through that trackless, unsown wilderness.'"
    },
    "3": {
      "L": "Israel was holiness to the LORD, the firstfruits of his increase; all who devour him shall be found guilty; evil shall come upon them, says the LORD.",
      "M": "Israel was holy to the LORD, the firstfruits of his harvest; all who consumed them were held guilty, and disaster came upon them, declares the LORD.",
      "T": "Israel was sacred to Yahweh, like the firstfruits of a harvest — set apart, untouchable. Any nation that devoured them brought guilt on itself and faced disaster."
    },
    "4": {
      "L": "Hear the word of the LORD, O house of Jacob, and all the families of the house of Israel:",
      "M": "Hear the word of the LORD, O house of Jacob, all the families of Israel:",
      "T": "Listen to Yahweh's word, house of Jacob — every family of Israel:"
    },
    "5": {
      "L": "Thus says the LORD: What iniquity did your fathers find in me, that they went far from me and walked after vanity and became empty?",
      "M": "This is what the LORD says: What fault did your fathers find in me, that they went so far from me, following worthless idols and becoming worthless themselves?",
      "T": "Yahweh asks: What wrong did your ancestors find in me that drove them this far away? They chased after empty things — and became empty themselves."
    },
    "6": {
      "L": "And they did not say, 'Where is the LORD who brought us up out of the land of Egypt, who led us through the wilderness, through a land of deserts and pits, through a land of drought and deep darkness, through a land that no man passes through and where no man dwells?'",
      "M": "They did not ask, 'Where is the LORD who brought us up out of Egypt, who led us through the wilderness — through a land of deserts and ravines, through a land of drought and deep darkness, a land no one crosses and no one lives in?'",
      "T": "Not once did they ask: 'Where is Yahweh who led us out of Egypt? Who walked us through that desert — through ravines and deep darkness, through the parched and lifeless land that no human being crosses?' They never asked."
    },
    "7": {
      "L": "And I brought you into a plentiful land, to eat its fruit and its goodness; but when you entered you defiled my land and made my heritage an abomination.",
      "M": "I brought you into a land of plenty, to enjoy its fruit and abundance. But when you entered, you defiled my land and made my heritage loathsome.",
      "T": "I brought you into a rich, fruitful land to feast on its abundance. But the moment you arrived, you made it foul. You turned my inheritance into something disgusting."
    },
    "8": {
      "L": "The priests did not say, 'Where is the LORD?' Those who handle the law did not know me; the shepherds also transgressed against me, and the prophets prophesied by Baal, and walked after things that do not profit.",
      "M": "The priests did not ask, 'Where is the LORD?' Those who deal with the law did not know me; the rulers transgressed against me; the prophets prophesied by Baal and followed things that cannot help.",
      "T": "The priests never asked 'Where is the LORD?' Those trained in the law never actually knew me. The leaders betrayed me. The prophets spoke for Baal and chased after gods that are useless."
    },
    "9": {
      "L": "Therefore I will yet plead with you, says the LORD, and with your children's children will I plead.",
      "M": "Therefore I will bring charges against you again, declares the LORD, and against your grandchildren will I bring charges.",
      "T": "So I am pressing this case against you — Yahweh declares — and against your grandchildren after you."
    },
    "10": {
      "L": "For pass over to the isles of Chittim and see; and send to Kedar and consider diligently, and see if there has been such a thing.",
      "M": "Cross to the shores of Cyprus and look; send to Kedar and examine carefully; see if there has ever been anything like this.",
      "T": "Cross the sea to Cyprus and look; send messengers east to Kedar and examine carefully — has any nation done what you have done?"
    },
    "11": {
      "L": "Has a nation changed its gods, which are yet no gods? But my people have changed their glory for that which does not profit.",
      "M": "Has any nation changed its gods, even though they are not real gods? But my people have exchanged their glory for things that are worthless.",
      "T": "No nation in history has swapped out its gods — even gods that are not gods. But my own people have traded away their glory for something utterly worthless."
    },
    "12": {
      "L": "Be appalled, O heavens, at this, and be horribly afraid; be very desolate, says the LORD.",
      "M": "Be appalled at this, O heavens; shudder with great horror, declares the LORD.",
      "T": "Heavens, stare in disbelief. Shudder. Reel back in horror — Yahweh's verdict."
    },
    "13": {
      "L": "For my people have committed two evils: they have forsaken me, the fountain of living waters, and hewed out for themselves cisterns — broken cisterns that can hold no water.",
      "M": "My people have committed two evils: they have abandoned me, the spring of living water, and dug their own cisterns — cracked cisterns that cannot hold water.",
      "T": "My people have committed two crimes. First: they have walked away from me — the only fountain of fresh, living water. Second: they have dug their own cisterns — broken, cracked things that cannot hold a drop."
    },
    "14": {
      "L": "Is Israel a servant? Is he a homeborn slave? Why then is he a prey?",
      "M": "Is Israel a slave? Was he born into slavery? Then why has he become plunder?",
      "T": "Is Israel a slave by nature? Was he born to be owned? Then why is he being looted?"
    },
    "15": {
      "L": "The young lions roared upon him and yelled; they made his land waste; his cities are burned without inhabitant.",
      "M": "Young lions have roared against him and growled; they have laid his land waste; his cities have been burned and left without inhabitants.",
      "T": "Enemy kings have roared over him like young lions and left his land a ruin — cities burned, no one left in them."
    },
    "16": {
      "L": "Also the children of Noph and Tahapanes have broken the crown of your head.",
      "M": "The people of Memphis and Tahpanhes have shaved the top of your head.",
      "T": "Even Egypt — Memphis and Tahpanhes — has humiliated you, shaving the crown of your head like a slave."
    },
    "17": {
      "L": "Have you not procured this unto yourself in that you have forsaken the LORD your God when he led you by the way?",
      "M": "Have you not brought this on yourself by forsaking the LORD your God when he led you on the way?",
      "T": "Is this not entirely your own doing — that you abandoned Yahweh your God precisely when he was guiding you on the road?"
    },
    "18": {
      "L": "And now what have you to do in the way to Egypt, to drink the waters of Shihor? Or what have you to do in the way to Assyria, to drink the waters of the River?",
      "M": "And now why go down to Egypt to drink from the waters of the Nile? Or why go to Assyria to drink from the Euphrates?",
      "T": "So why are you trekking to Egypt to drink Nile water? Why to Assyria to drink from the Euphrates? What do you hope to find there that you abandoned when you left me?"
    },
    "19": {
      "L": "Your own wickedness shall correct you, and your apostasies shall reprove you; know therefore and see that it is an evil thing and bitter that you have forsaken the LORD your God, and that the fear of me is not in you, says the Lord GOD of hosts.",
      "M": "Your own wickedness will punish you, and your turning away will rebuke you. Know and see that it is evil and bitter to forsake the LORD your God and to have no fear of me, declares the Lord GOD of hosts.",
      "T": "Your own wickedness will come back on you like a correction; your own apostasy will indict you. Learn this, and see it plainly: forsaking Yahweh your God is bitter poison. The reverential fear of me is gone from you — the Lord GOD of hosts declares it."
    },
    "20": {
      "L": "For of old time I broke your yoke and burst your bands; and you said, 'I will not transgress'; yet upon every high hill and under every green tree you wandered, playing the harlot.",
      "M": "For long ago I broke your yoke and tore off your chains. But you said, 'I will not serve!' And on every high hill and under every spreading tree you gave yourself like a prostitute.",
      "T": "Long ago I shattered the yoke that held you — I snapped your chains. But your answer was: 'I refuse to serve.' And there you were, under every hilltop altar and every leafy tree, sprawling in spiritual prostitution."
    },
    "21": {
      "L": "Yet I had planted you a noble vine, a wholly right seed; how then have you turned before me into the degenerate plant of a strange vine?",
      "M": "I had planted you as a choice vine, of pure and wholesome seed. How then have you turned against me into the wild shoots of a foreign vine?",
      "T": "I planted you as a choice vine — a pure, true-bred stock. How have you gone so utterly wild on me, turning into some rank, foreign weed?"
    },
    "22": {
      "L": "For though you wash yourself with nitre and take much soap, yet your iniquity is marked before me, says the Lord GOD.",
      "M": "Even if you scrubbed yourself with lye and used much soap, the stain of your guilt would still be before me, declares the Lord GOD.",
      "T": "No amount of scrubbing will remove this. Lye and soap will not help. The mark of your guilt is right there in front of me — the Lord GOD."
    },
    "23": {
      "L": "How can you say, 'I am not polluted, I have not gone after the Baals'? See your way in the valley; know what you have done. You are a swift young camel traversing her ways.",
      "M": "How can you say, 'I am not defiled, I have not chased after the Baals'? Look at your tracks in the valley; acknowledge what you have done. You are a swift young camel running in every direction.",
      "T": "How dare you say 'I am clean — I never chased the Baals'? Look at the tracks you have left in the valley. You know what you have done. You are like a restless young camel bolting off in every direction."
    },
    "24": {
      "L": "A wild ass used to the wilderness, that snuffs up the wind in her desire; in her time of heat who can turn her away? All who seek her will not weary themselves; in her month they shall find her.",
      "M": "Like a wild donkey at home in the desert, sniffing the wind in her craving — who can hold her back when she is in heat? All who look for her need not tire themselves; they will find her in her mating season.",
      "T": "You are like a wild donkey born to the desert, sniffing the wind with open nostrils, driven by desire. Who could stop her when she runs? The men who want her do not even need to search — they will find her when the season comes."
    },
    "25": {
      "L": "Withhold your foot from being unshod, and your throat from thirst; but you said, 'There is no hope! No, for I have loved strangers, and after them I will go.'",
      "M": "Keep your feet from going bare and your throat from being dry. But you said, 'It is hopeless! I love other gods, and after them I will go.'",
      "T": "You are running yourself barefoot, running yourself parched — and you will not stop. 'It is no use,' you say. 'I love these foreign gods; I am committed to them.'"
    },
    "26": {
      "L": "As the thief is ashamed when he is found, so is the house of Israel ashamed — they, their kings, their princes, their priests, and their prophets.",
      "M": "As a thief is put to shame when caught, so the house of Israel will be shamed — they, their kings, their officials, their priests, and their prophets.",
      "T": "Like a thief caught in the act, the whole house of Israel will be exposed in disgrace — their kings, their officials, their priests, their prophets — every one of them."
    },
    "27": {
      "L": "Saying to a tree, 'You are my father'; and to a stone, 'You have brought me forth'; for they have turned their back to me and not their face; yet in the time of their trouble they will say, 'Arise, and save us.'",
      "M": "They say to a tree, 'You are my father,' and to a stone, 'You gave me birth.' They have turned their backs to me and not their faces. Yet in the time of their trouble they will cry, 'Rise up and save us!'",
      "T": "They call a tree 'Father' and a stone 'Mother.' They have turned their backs on me — their faces point away. But the moment disaster comes, watch them: 'Rise up! Save us!'"
    },
    "28": {
      "L": "But where are your gods that you have made for yourself? Let them arise, if they can save you in the time of your trouble; for according to the number of your cities are your gods, O Judah.",
      "M": "But where are the gods you made for yourself? Let them rise up, if they can rescue you in the time of your trouble — for you have as many gods as you have cities, O Judah.",
      "T": "Then let those gods you made answer. Let them rise up and rescue you — if they can. You have as many gods as cities in Judah; every town has its own deity. Let them do something."
    },
    "29": {
      "L": "Why do you plead with me? You have all transgressed against me, says the LORD.",
      "M": "Why do you bring a complaint against me? You have all rebelled against me, declares the LORD.",
      "T": "Why are you filing a grievance against me? Every one of you has rebelled — Yahweh declares it."
    },
    "30": {
      "L": "In vain have I struck your children; they received no correction; your own sword has devoured your prophets, like a destroying lion.",
      "M": "I have struck your people in vain; they accepted no correction. Your own sword has consumed your prophets like a ravaging lion.",
      "T": "I struck your people time and again — nothing changed. Correction bounced off them. They took their own prophets and cut them down with their own sword, like a ravaging lion."
    },
    "31": {
      "L": "O generation, consider the word of the LORD: Have I been a wilderness to Israel? A land of darkness? Why do my people say, 'We are lords; we will come to you no more'?",
      "M": "O generation, take heed of the word of the LORD: Have I been a desert to Israel or a land of thick darkness? Why do my people say, 'We are free; we will come to you no more'?",
      "T": "Listen to Yahweh's word, this generation: Was I ever a desert to Israel? A land of darkness and death? Then why do my people say, 'We are done — we are free — we will not come back to you'?"
    },
    "32": {
      "L": "Can a maid forget her ornaments, or a bride her attire? Yet my people have forgotten me days without number.",
      "M": "Does a young woman forget her jewelry, or a bride her wedding attire? Yet my people have forgotten me — for more days than can be counted.",
      "T": "Does a young woman forget her jewels? Does a bride walk to her groom without her wedding dress? Yet my people have forgotten me — not for a day or a week, but beyond counting."
    },
    "33": {
      "L": "Why do you trim your way to seek love? Therefore you have also taught the wicked your ways.",
      "M": "How skilled you are at pursuing love; you have become expert enough to teach the wicked your ways.",
      "T": "How practiced you are at making yourself attractive — how clever at seeking your lovers. You have become so skilled at sin that you are now teaching wicked people new tricks."
    },
    "34": {
      "L": "Also in your skirts is found the blood of the souls of innocent poor; I have not found it by secret search, but upon all these.",
      "M": "On your garments is found the lifeblood of innocent poor people — you did not catch them breaking in; it is on all these.",
      "T": "And there on your clothes is the blood of the innocent poor. You did not even have the excuse of catching them breaking in at night — this blood cries out openly against you."
    },
    "35": {
      "L": "Yet you say, 'Because I am innocent, surely his anger shall turn from me.' Behold, I will plead with you, because you say, 'I have not sinned.'",
      "M": "Yet you say, 'I am innocent; surely his anger has turned from me.' But I will bring judgment against you because you say, 'I have not sinned.'",
      "T": "'I did nothing wrong,' you say. 'His anger must be past by now.' But I am pressing this case against you precisely because you say that. The first requirement for mercy is to tell the truth."
    },
    "36": {
      "L": "Why do you go about so much to change your way? You also shall be ashamed of Egypt, as you were ashamed of Assyria.",
      "M": "Why do you rush about so much, changing course? You will be disappointed by Egypt just as you were disappointed by Assyria.",
      "T": "Why all this frantic switching of alliances? Egypt will let you down the same way Assyria did. You will walk away from that alliance too, shamed and empty-handed."
    },
    "37": {
      "L": "Indeed you will go forth from him with your hands upon your head, for the LORD has rejected your confidences, and you shall not prosper in them.",
      "M": "You will leave Egypt too with your hands on your head in defeat, for the LORD has rejected the ones you are trusting, and you will not succeed through them.",
      "T": "You will leave Egypt the way captives leave a battlefield — hands clasped on your head in defeat. Yahweh has repudiated every alliance you are trusting. None of them will work."
    }
  },
  "3": {
    "1": {
      "L": "They say, 'If a man puts away his wife and she goes from him and becomes another man's, will he return to her again? Shall not that land be greatly polluted?' But you have played the harlot with many lovers; yet return to me, says the LORD.",
      "M": "It is said: If a man divorces his wife and she goes and marries another, can he take her back? Would not the land be totally defiled? But you have given yourself to many lovers — yet return to me, declares the LORD.",
      "T": "The law is clear: if a man divorces his wife and she marries someone else, he cannot take her back — the land would be defiled. But you have given yourself to countless lovers. Would you really come back to me now? Yahweh asks."
    },
    "2": {
      "L": "Lift up your eyes to the bare heights and see; where have you not been lain with? By the roads you have sat waiting for them, like an Arab in the wilderness; and you have polluted the land with your whoredoms and with your wickedness.",
      "M": "Raise your eyes to the bare hilltops and look — is there any place you have not been violated? You have sat by the roads waiting for lovers, like a nomad lurking in the desert; you have polluted the land with your prostitution and your wickedness.",
      "T": "Look up at those bare hill shrines — every single one of them. Is there a hilltop where you were not given over to idolatry? You sat by the roads like a desert bandit, waiting for any passerby. You have soaked the land in your spiritual adultery and wickedness."
    },
    "3": {
      "L": "Therefore the showers have been withheld, and there has been no latter rain; yet you had a harlot's forehead; you refused to be ashamed.",
      "M": "Therefore the rain has been withheld, and the spring rain has not come; yet you have a prostitute's brazenness — you refuse to be ashamed.",
      "T": "So the rains have been cut off; the spring rains failed to come. Yet even the drought did not move you. You have the brazen forehead of a prostitute — utterly unashamed."
    },
    "4": {
      "L": "Will you not from this time cry to me, 'My Father, you are the guide of my youth'?",
      "M": "Have you not just been calling out to me, 'My Father, you are my closest companion from my youth'?",
      "T": "And yet even now you call out: 'Father! You were my closest companion from my youngest days!'"
    },
    "5": {
      "L": "Will he keep his anger forever? Will he reserve it to the end? Behold, you have spoken and done evil things as you could.",
      "M": "Will he be angry forever? Will he stay angry to the end? But see — you have spoken, and you have done all the evil you could.",
      "T": "You count on him to relent: 'Can he really stay angry forever? Surely he will not?' But look at what you have done. You have said every empty word and done every evil thing within your power."
    },
    "6": {
      "L": "The LORD said to me in the days of Josiah the king: 'Have you seen what backsliding Israel has done? She has gone up upon every high mountain and under every green tree, and there played the harlot.'",
      "M": "The LORD said to me in the days of King Josiah: 'Have you seen what faithless Israel has done? She has gone up to every high mountain and under every spreading tree and committed adultery there.'",
      "T": "In the days of King Josiah, Yahweh said to me: 'Have you seen what faithless Israel has been doing? Every high hill, every green tree — she went to them all and played the whore there.'"
    },
    "7": {
      "L": "And I said after she had done all these things, 'Turn to me'; but she did not return. And her treacherous sister Judah saw it.",
      "M": "I said, after she had done all this, 'Return to me,' but she did not return. Then her unfaithful sister Judah saw it.",
      "T": "'Come back to me,' I told her after everything she had done. She did not come back. And her sister Judah was watching it all."
    },
    "8": {
      "L": "And I saw that for all the causes for which backsliding Israel committed adultery I had put her away and given her a bill of divorce; yet her treacherous sister Judah feared not, but went and played the harlot also.",
      "M": "I saw that because faithless Israel had committed adultery, I had sent her away and given her a certificate of divorce; yet her unfaithful sister Judah had no fear, but went and became a prostitute too.",
      "T": "I had done it: I served faithless Israel with a certificate of divorce and sent her away. Her sister Judah saw every bit of it. And she was not afraid. She went right out and did the same thing."
    },
    "9": {
      "L": "And it came to pass through the lightness of her whoredom that she defiled the land and committed adultery with stones and with stocks.",
      "M": "She defiled the land by the brazen ease of her prostitution, committing adultery with stones and wooden posts.",
      "T": "So cheaply, so carelessly did she give herself away — she polluted the whole land, throwing herself at every stone idol and wooden post."
    },
    "10": {
      "L": "And yet for all this her treacherous sister Judah has not turned to me with her whole heart, but feignedly, says the LORD.",
      "M": "In spite of all this, Judah, her unfaithful sister, did not return to me with all her heart — only in pretense, declares the LORD.",
      "T": "And yet — for all that — her treacherous sister Judah still did not return to me with genuine heart. Only a performance. Yahweh says it plainly."
    },
    "11": {
      "L": "And the LORD said to me: 'The backsliding Israel has justified herself more than treacherous Judah.'",
      "M": "The LORD said to me: 'Faithless Israel has shown herself more in the right than unfaithful Judah.'",
      "T": "Then Yahweh said to me: 'Faithless Israel comes off better than treacherous Judah. At least Israel never pretended.'"
    },
    "12": {
      "L": "Go and proclaim these words toward the north, and say: 'Return, O backsliding Israel,' says the LORD; 'I will not cause my anger to fall upon you, for I am merciful,' says the LORD; 'I will not keep anger forever.'",
      "M": "Go and proclaim this to the north: 'Return, O faithless Israel,' declares the LORD; 'I will not look on you in anger, for I am faithful in love,' declares the LORD; 'I will not keep my anger forever.'",
      "T": "Go and shout these words toward the north: 'Come back, faithless Israel — Yahweh declares it. I will not keep my face turned against you in anger, for I am a God of steadfast love. My anger will not last forever.'"
    },
    "13": {
      "L": "Only acknowledge your iniquity, that you have transgressed against the LORD your God and have scattered your ways to the strangers under every green tree, and you have not obeyed my voice, says the LORD.",
      "M": "Only acknowledge your guilt — that you have rebelled against the LORD your God and given yourself to foreign lovers under every spreading tree, and that you have not listened to my voice, declares the LORD.",
      "T": "Just own it. Admit you have rebelled against Yahweh your God, that you have thrown yourself at every foreign god under every leafy tree, that you have refused to listen to my voice. That is all I require."
    },
    "14": {
      "L": "Return, O backsliding children, says the LORD; for I am married to you, and I will take you one from a city and two from a family and I will bring you to Zion.",
      "M": "Return, faithless children, declares the LORD, for I am your husband. I will take you, one from a city and two from a family, and bring you to Zion.",
      "T": "Come back, wayward children — Yahweh declares it. I am still your husband. I will gather you — one here, two there — and bring you home to Zion."
    },
    "15": {
      "L": "And I will give you shepherds according to my own heart, who shall feed you with knowledge and understanding.",
      "M": "I will give you shepherds after my own heart, who will lead you with knowledge and wisdom.",
      "T": "And I will give you leaders who genuinely know my heart — shepherds who will feed you with true understanding and real wisdom."
    },
    "16": {
      "L": "And it shall come to pass, when you are multiplied and increased in the land, in those days, says the LORD, they shall say no more, 'The ark of the covenant of the LORD'; neither shall it come to mind; neither shall they remember it; neither shall they visit it; neither shall that be done any more.",
      "M": "When you have become numerous and multiplied in the land in those days, declares the LORD, no one will say any longer, 'The ark of the covenant of the LORD.' It will not come to mind; no one will remember it; no one will look for it; it will not be made again.",
      "T": "In those days, when you fill the land again and are multiplied, no one will speak of the ark of the covenant — Yahweh declares it. No one will even think of it, miss it, or go searching for it. It will not be remade. Something greater will have come."
    },
    "17": {
      "L": "At that time they shall call Jerusalem the throne of the LORD; and all the nations shall be gathered to it, to the name of the LORD, to Jerusalem; neither shall they walk any more after the imagination of their evil heart.",
      "M": "At that time Jerusalem will be called the throne of the LORD, and all nations will gather to it, to honor the name of the LORD in Jerusalem; they will no longer follow the stubborn inclination of their evil hearts.",
      "T": "In that day Jerusalem itself will be called the throne of Yahweh. Every nation will stream to her to honor his name. And the old hardness of heart — the stubborn pull of self and sin — will be broken at last."
    },
    "18": {
      "L": "In those days the house of Judah shall walk with the house of Israel, and they shall come together out of the land of the north to the land that I have given for an inheritance to your fathers.",
      "M": "In those days the house of Judah will join the house of Israel, and together they will come from the northern land to the land I gave your ancestors as an inheritance.",
      "T": "In that day Judah and Israel will walk side by side — united at last — and they will come together out of the north into the land I promised to your ancestors."
    },
    "19": {
      "L": "But I said, 'How shall I put you among the children and give you a pleasant land, a goodly heritage of the hosts of nations?' And I said: 'You shall call me, My Father; and you shall not turn away from me.'",
      "M": "I had thought, 'How gladly I would treat you as my children and give you a desirable land, the most beautiful inheritance among the nations.' I had expected you to call me \"My Father\" and never turn from me.",
      "T": "I had said to myself: 'How I want to receive you as my children and give you the most beautiful land in the world — the finest inheritance among all nations.' I expected you to call me Father and never leave. That was my hope for you."
    },
    "20": {
      "L": "Surely as a wife treacherously departs from her husband, so have you dealt treacherously with me, O house of Israel, says the LORD.",
      "M": "But like a woman who is unfaithful to her husband, you have been unfaithful to me, O house of Israel, declares the LORD.",
      "T": "But like a faithless wife who walks out on her husband, that is what you did to me, house of Israel — Yahweh declares it."
    },
    "21": {
      "L": "A voice was heard upon the bare heights, weeping and supplications of the children of Israel; for they have perverted their way, and they have forgotten the LORD their God.",
      "M": "A cry is heard on the bare hilltops — the weeping and pleading of the children of Israel — because they have perverted their ways and forgotten the LORD their God.",
      "T": "A sound rises from the bare hilltops — weeping and desperate prayers from the children of Israel. They have twisted every path they took; they have forgotten Yahweh their God."
    },
    "22": {
      "L": "Return, you backsliding children, and I will heal your backslidings. 'Behold, we come to you, for you are the LORD our God.'",
      "M": "Return, faithless children, and I will heal your faithlessness. 'Here we are — we come to you, for you are the LORD our God.'",
      "T": "'Come back, wayward children, and I will heal every one of your wanderings.' 'Here we are — we are coming! For you are Yahweh our God.'"
    },
    "23": {
      "L": "Truly in vain is salvation hoped for from the hills, and from the multitude of mountains; truly in the LORD our God is the salvation of Israel.",
      "M": "Surely the commotion on the hills and mountains is a delusion; surely in the LORD our God is the salvation of Israel.",
      "T": "We see it now: all that noise on the hills was a lie. All those mountain shrines — empty. Salvation belongs to Yahweh our God alone, and to no one else."
    },
    "24": {
      "L": "For shame has devoured the labour of our fathers from our youth — their flocks and their herds, their sons and their daughters.",
      "M": "For the shameful thing has consumed from our youth what our fathers worked for — their flocks and herds, their sons and daughters.",
      "T": "The Shameful One — Baal — has eaten everything our fathers built from the beginning: flocks and cattle, sons and daughters, all consumed by our idolatry."
    },
    "25": {
      "L": "We lie down in our shame, and our confusion covers us; for we have sinned against the LORD our God, we and our fathers, from our youth even unto this day, and have not obeyed the voice of the LORD our God.",
      "M": "Let us lie down in our shame, for our dishonor covers us; for we have sinned against the LORD our God, both we and our fathers, from our youth until today, and we have not obeyed the voice of the LORD our God.",
      "T": "We lie down in our shame; we pull our disgrace over us like a blanket. For we have sinned against Yahweh our God — we and our fathers before us — from our earliest days until this very moment. We have never truly obeyed his voice."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 1–3 written.')

if __name__ == '__main__':
    main()
