"""
MKT Jeremiah chapters 19–22 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-19-22.py

Translation decisions (consistent with mkt-jeremiah-1-3.py, mkt-jeremiah-10-12.py,
mkt-jeremiah-13-15.py, and mkt-jeremiah-16-18.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where personal-name force
  is significant — oracle delivery, divine soliloquy, address of lament. Narrative
  formulas use "Yahweh" in T for immediacy.
- H430 (אֱלֹהִים): "God" in all tiers; "other gods" when referring to foreign deities.
- H136+H3069 (אֲדֹנָי יְהוִה): "Lord GOD" in L/M; "Lord Yahweh" in T (20:4 not present,
  but the pattern from prior chapters stands).
- H5019 (נְבוּכַדְרֶאצַּר / Nebuchadrezzar): Hebrew has the Aramaic-influenced spelling.
  Preserved as "Nebuchadnezzar" in M/T for recognizability; L uses "Nebuchadrezzar" to
  reflect the Hebrew text. Both forms refer to the same king (Nebuchadnezzar II).
- H4036 (מָגוֹר מִסָּבִיב, Magor-Missabib): 20:3 — Jeremiah renames Pashhur "Terror-All-
  Around." L preserves the Hebrew name transliterated; M uses "Terror on Every Side" as
  an explanatory phrase; T unpacks the prophetic weight of the renaming.
- H8612 (תֹּפֶת, Tophet): preserved as a proper noun in all tiers. The site in the valley
  of Ben-hinnom where child sacrifice occurred; became a figure for ultimate divine
  judgment. The word may derive from "fireplace" or from a term of horror and shame.
- H6098 (עֵצָה, counsel/plan): 19:7 — "I will void/empty out the counsel of Judah."
  The same verb (H1238, bāqaq) used for emptying a bottle; plays on the pottery image of
  the chapter. Rendered "make void / empty out / drain away."
- H7307 (רוּחַ): 22:22 — "the wind shall eat up your shepherds" — physical wind, not Spirit.
- H7665 (שָׁבַר): 19:10 — "break the bottle" — the same root as "shattered/broken" in
  19:11; the sign-act and the oracle share vocabulary deliberately.
- H5769 (עוֹלָם): 20:17 — "always/perpetually" — her womb great always/for ever; rendered
  "perpetually" in L, "forever" in M, and unpacked in T as the permanent grave it became.
- H6662 (צַדִּיק): "righteous" in all tiers for the divine attribute; "just" when describing
  human action in social-justice contexts (22:3, 22:15).
- H2617 (חֶסֶד): Not directly in this range, but closely related to the justice language
  of chapter 22. The justice Josiah executed (22:15-16) embodies covenant loyalty.
- H3045 (יָדַע): 22:16 — "was not this to know me?" — knowing Yahweh is doing justice;
  the T tier makes this explicit: knowing God is not doctrinal but enacted.
- H2745 (חַנַּנְתִּי / H2603 חָנַן): 21:7 — "shall not spare / have pity / show mercy" —
  triple negation of divine compassion rendered as stacking denials in T.
- H3724 (כֹּפֶר): not present here but the justice / blood-price theme of 22:17 echoes it.

Textual notes:
- 19:9 — Siege cannibalism: this verse explicitly describes parents eating their children,
  drawing on the covenant curse of Deut 28:53-57 and Lev 26:29. The T tier notes the
  Deuteronomic echo without softening the horror.
- 20:7 — "You have deceived/enticed me" (H6601, pātâ): the same verb used for seduction
  in Exod 22:16 and the deceiving of a prophet in 1 Kgs 22:20-22. Jeremiah accuses God
  of the divine equivalent of entrapment. The T tier preserves the shocking force.
- 20:9 — "Fire shut up in my bones": one of the most psychologically intense self-
  revelations in all prophetic literature. Cannot suppress the compulsion to speak even
  when speech costs everything.
- 21:2 — "Nebuchadrezzar": the Babylonian king's name in this chapter introduces a
  historical anchoring point: this oracle comes during the final siege of Jerusalem
  (588-587 BCE), making it among the last Jeremianic oracles.
- 22:10 — The king not to weep for is Josiah (died 609 BCE); the one going away and
  never returning is Shallum (= Jehoahaz), taken to Egypt by Pharaoh Necho (22:11-12).
- 22:18-19 — Jehoiakim's burial "like a donkey": historically uncertain whether this
  happened literally; the prophecy functions as a declaration of total dishonor — no
  formal mourning, no royal burial, cast out beyond the city.
- 22:24-30 — Coniah (= Jehoiachin/Jeconiah): taken captive to Babylon 597 BCE. Despite
  his royal descent, the line through him is declared non-throne-inheriting. This creates
  a genuine messianic puzzle resolved in NT genealogy (Matt 1:12; Luke 3:27 takes the
  Nathan line through Mary, bypassing the curse on Coniah's line).

Structural notes:
  Ch. 19 — Sign-act: the broken potter's flask. Jeremiah goes to Tophet with witnesses,
  proclaims judgment, breaks the flask — a physical enactment of irreversible ruin. The
  imagery picks up the potter passage of ch. 18 but inverts it: if ch. 18 showed clay
  still being worked, ch. 19 shows the fired, hardened vessel beyond reformation, shattered.

  Ch. 20 — Persecution and inner crisis. Pashhur's assault on Jeremiah triggers the
  prophet's most anguished meditation. The fourth "confession" (20:7-18) moves from
  accusation of God (v. 7), through resolution to stay silent (v. 9a), to inability to
  keep silent (v. 9b), through confident praise (vv. 11-13) — and then collapses into
  the bitterest curse in the Hebrew Bible (vv. 14-18). The structure mirrors the psalmist's
  lament/praise pattern, but does not resolve there.

  Ch. 21 — Oracle in the teeth of the siege. Zedekiah's desperate embassy to Jeremiah
  during Nebuchadnezzar's final attack (588 BCE) receives not rescue but the announcement
  that Yahweh is now fighting on the Babylonian side. The holy-war metaphor is inverted:
  instead of Yahweh fighting for Israel against enemies, Yahweh fights against Israel
  through the enemy.

  Ch. 22 — The royal indictment: three kings judged. A general summons to justice
  (vv. 1-9), then three specific oracles — on Shallum/Jehoahaz (vv. 10-12), on
  Jehoiakim (vv. 13-19), on Coniah/Jehoiachin (vv. 20-30). Each oracle escalates in
  severity. The standard against which all three are measured is Josiah's practice of
  justice (22:15-16): knowing Yahweh equals doing justice.

OT echoes:
  19:4 — "filled this place with the blood of innocents" echoes 2 Kgs 21:16 on Manasseh,
    whom Jer 15:4 has already named as the ultimate cause.
  19:5 — Child sacrifice to Baal echoes Deut 12:31 (forbidden) and 2 Kgs 16:3 (done
    by Ahaz). The T tier links the vocabulary.
  20:9 — "fire shut up in my bones" anticipates Luke 24:32 ("hearts burning within us")
    — the same image of irrepressible divine word.
  21:5 — "outstretched hand and mighty arm" reverses the Exodus formula (Deut 4:34;
    5:15; 26:8): in the Exodus God fought FOR Israel with his outstretched arm; now he
    fights AGAINST Israel with the same arm.
  22:3 — "Execute justice, deliver the oppressed, do no wrong to stranger/fatherless/widow"
    — the standard Deuteronomic triad (Deut 10:18; 24:17-22; 27:19); Jeremiah's ethics
    are rooted entirely in covenant obligation.
  22:15-16 — Josiah as the model king: eating, drinking, and doing justice — an allusion
    to the ancient Near Eastern royal ideal AND to the covenant meal (eating/drinking before
    Yahweh). Knowing God is covenant-enacted, not merely cerebral.
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
  "19": {
    "1": {
      "L": "Thus says the LORD: Go and buy a potter's earthen flask, and take some of the elders of the people and some of the senior priests,",
      "M": "This is what the LORD says: Go and buy a potter's clay flask. Take some of the elders of the people and some of the senior priests with you,",
      "T": "Yahweh said: Go and buy an earthenware flask from the potter. Take with you some of the elders of the people and some of the senior priests —"
    },
    "2": {
      "L": "and go out to the valley of the son of Hinnom, which is at the entry of the Potsherd Gate, and proclaim there the words that I tell you.",
      "M": "and go out to the valley of Ben-hinnom, at the entrance of the Potsherd Gate, and proclaim there the words I speak to you.",
      "T": "then go out to the valley of Ben-hinnom, to the entrance of the Potsherd Gate. There, proclaim the words I give you."
    },
    "3": {
      "L": "And say: Hear the word of the LORD, O kings of Judah and inhabitants of Jerusalem. Thus says the LORD of hosts, the God of Israel: Behold, I am bringing such disaster upon this place that the ears of whoever hears of it will tingle.",
      "M": "Say: Hear the word of the LORD, O kings of Judah and people of Jerusalem. This is what the LORD of hosts, the God of Israel, says: I am going to bring such a disaster on this place that the ears of everyone who hears about it will ring.",
      "T": "Declare this: Kings of Judah, people of Jerusalem — hear the word of Yahweh. Yahweh of hosts, God of Israel, says: I am about to bring such calamity on this place that anyone who hears of it will feel the shock in their ears."
    },
    "4": {
      "L": "Because they have forsaken me and made this place foreign, and have burned incense in it to other gods whom neither they nor their fathers nor the kings of Judah have known, and have filled this place with the blood of innocents,",
      "M": "Because they have abandoned me and made this a foreign place, burning incense here to other gods that neither they nor their ancestors nor the kings of Judah ever knew, and have filled this place with the blood of the innocent —",
      "T": "They abandoned me. They turned this sacred place into a stranger's territory, burning incense to gods they never knew — gods their ancestors never knew, gods no king of Judah ever worshiped. And they filled this valley with innocent blood."
    },
    "5": {
      "L": "and have built the high places of Baal to burn their sons in the fire as burnt offerings to Baal — which I did not command or decree, and which never entered my mind —",
      "M": "and have built the high places of Baal to burn their sons in the fire as burnt offerings to Baal — something I never commanded, never decreed, something that never even entered my mind —",
      "T": "They built shrines to Baal and burned their own sons in the fire as offerings — something Yahweh never commanded, never thought of, never once suggested."
    },
    "6": {
      "L": "therefore behold, days are coming, declares the LORD, when this place shall no more be called Tophet, or the valley of the son of Hinnom, but the valley of Slaughter.",
      "M": "therefore the days are coming, declares the LORD, when this place will no longer be called Tophet or the valley of Ben-hinnom, but the valley of Slaughter.",
      "T": "So the days are coming, says Yahweh, when this place — Tophet, the valley of Ben-hinnom — will be renamed. It will be called the Valley of Slaughter."
    },
    "7": {
      "L": "And I will make void the counsel of Judah and Jerusalem in this place, and will cause them to fall by the sword before their enemies and by the hand of those who seek their life. And I will give their dead bodies as food for the birds of the sky and the beasts of the earth.",
      "M": "I will empty out the plans of Judah and Jerusalem in this place; I will make them fall by the sword before their enemies and by the hand of those who seek their lives, and I will give their bodies as food for the birds of the sky and the beasts of the earth.",
      "T": "I will drain away every plan and strategy Judah and Jerusalem have — pour them out right here like water. They will fall before their enemies at this very place, cut down by the sword of those hunting them. Their corpses will lie here for the birds and the wild animals to eat."
    },
    "8": {
      "L": "And I will make this city a desolation and a hissing; everyone who passes by it will be appalled and hiss because of all its wounds.",
      "M": "I will make this city a scene of horror and contempt; all who pass by it will be horrified and will hiss in scorn at all its wounds.",
      "T": "This city will become a thing of horror — people will hiss through their teeth and shake their heads in revulsion as they pass by, stunned at the ruin they see."
    },
    "9": {
      "L": "And I will cause them to eat the flesh of their sons and the flesh of their daughters, and everyone shall eat the flesh of his neighbor in the siege and in the distress with which their enemies and those who seek their life shall distress them.",
      "M": "I will make them eat the flesh of their sons and daughters; they will devour one another's flesh in the desperate siege and distress inflicted on them by the enemies who seek their lives.",
      "T": "In the anguish of the siege, I will drive them to eat the flesh of their own sons and daughters. Neighbor will devour neighbor. What the curse of the covenant threatened has arrived — and it has arrived complete."
    },
    "10": {
      "L": "Then you shall break the flask in the sight of the men who go with you,",
      "M": "Then break the flask in front of the men who have come with you,",
      "T": "Then shatter the flask — right there, in front of all the witnesses you brought with you."
    },
    "11": {
      "L": "and shall say to them: Thus says the LORD of hosts: So will I break this people and this city, as one breaks a potter's vessel, so that it can be repaired no more; and they shall bury in Tophet until there is no more room to bury.",
      "M": "and say to them: This is what the LORD of hosts says — I will smash this people and this city just as one smashes a potter's vessel, so that it can never be repaired again; and they will bury their dead in Tophet until there is no room left for burial.",
      "T": "Say to them: Yahweh of hosts says this — I will shatter this people and this city the way you shatter a clay jar: irrevocably, beyond all repair. They will bury their dead in Tophet until there is no more room."
    },
    "12": {
      "L": "Thus will I do to this place, declares the LORD, and to its inhabitants, making this city like Tophet.",
      "M": "This is what I will do to this place and its inhabitants, declares the LORD — I will make this whole city like Tophet.",
      "T": "This is what I will do to this city and everyone in it, says Yahweh: I will make Jerusalem into one vast Tophet."
    },
    "13": {
      "L": "The houses of Jerusalem and the houses of the kings of Judah shall be defiled like the place of Tophet — all the houses on whose roofs they burned incense to all the host of heaven and poured out drink offerings to other gods.",
      "M": "The houses of Jerusalem and the houses of the kings of Judah will be defiled just like Tophet — all the houses on whose rooftops they burned incense to all the starry host of heaven and poured out drink offerings to other gods.",
      "T": "Every house in Jerusalem — every house of every king of Judah — will be as defiled as Tophet: because on those rooftops they burned incense to the whole array of heaven and poured out offerings to foreign gods."
    },
    "14": {
      "L": "Then Jeremiah came from Tophet, where the LORD had sent him to prophesy, and stood in the court of the LORD's house, and said to all the people:",
      "M": "Jeremiah came back from Tophet, where the LORD had sent him to prophesy, and stood in the court of the LORD's temple and spoke to all the people:",
      "T": "Jeremiah returned from Tophet — where Yahweh had sent him to deliver that oracle — and stood in the court of the temple and addressed all the people there:"
    },
    "15": {
      "L": "Thus says the LORD of hosts, the God of Israel: Behold, I am bringing upon this city and upon all its towns all the disaster that I have pronounced against it, because they have stiffened their necks and have not listened to my words.",
      "M": "This is what the LORD of hosts, the God of Israel, says: I am going to bring upon this city and all its surrounding towns every disaster I have announced against them, because they have stubbornly refused to listen to my words.",
      "T": "Yahweh of hosts, God of Israel, says this: Every word of disaster I have pronounced against this city and every town around it — I am bringing it. All of it. Because they have hardened their necks like iron and would not listen."
    }
  },
  "20": {
    "1": {
      "L": "Now Pashhur the priest, son of Immer, who was chief officer in the house of the LORD, heard Jeremiah prophesying these things.",
      "M": "Pashhur son of Immer, the priest who was the chief officer in the temple of the LORD, heard Jeremiah prophesying these things.",
      "T": "Pashhur son of Immer, a priest who held the senior administrative position in the temple, heard Jeremiah delivering that prophecy."
    },
    "2": {
      "L": "Then Pashhur struck Jeremiah the prophet and put him in the stocks that were in the upper Benjamin Gate of the house of the LORD.",
      "M": "Pashhur had Jeremiah the prophet beaten and put in the stocks at the Upper Benjamin Gate of the LORD's temple.",
      "T": "Pashhur had Jeremiah flogged and locked in the stocks at the Upper Benjamin Gate of the temple."
    },
    "3": {
      "L": "The next day, when Pashhur released Jeremiah from the stocks, Jeremiah said to him: The LORD has not called your name Pashhur, but Magor-Missabib — Terror on Every Side.",
      "M": "The next day, when Pashhur released Jeremiah from the stocks, Jeremiah said to him: The LORD has not named you Pashhur, but Magor-Missabib — Terror-on-Every-Side.",
      "T": "The next morning, when Pashhur released Jeremiah from the stocks, Jeremiah said to him: Yahweh has renamed you. Your name is no longer Pashhur. Your name is now Magor-Missabib — Terror All Around."
    },
    "4": {
      "L": "For thus says the LORD: Behold, I will make you a terror to yourself and to all your friends. They will fall by the sword of their enemies while your eyes are watching, and I will give all Judah into the hand of the king of Babylon. He will carry them captive to Babylon and will strike them with the sword.",
      "M": "For this is what the LORD says: I am going to make you a terror to yourself and to all your friends. They will fall by the sword of their enemies before your eyes, and I will hand all Judah over to the king of Babylon, who will deport them to Babylon or put them to the sword.",
      "T": "For Yahweh says this: I am making you a living terror — a terror to yourself and to every friend you have. You will watch your friends fall to the sword of their enemies. I am handing all of Judah over to the king of Babylon. He will deport them or kill them."
    },
    "5": {
      "L": "Moreover, I will give all the wealth of this city, all its gains and all its precious things, all the treasures of the kings of Judah into the hand of their enemies, who shall plunder them and carry them off to Babylon.",
      "M": "I will also hand over all the wealth of this city — all its goods, all its valuables, all the treasures of the kings of Judah — to their enemies, who will plunder it and carry it all off to Babylon.",
      "T": "Every treasure in this city — every luxury, every storehouse, every possession of every king of Judah — I will put into the hands of their enemies. It will all be looted and hauled away to Babylon."
    },
    "6": {
      "L": "And you, Pashhur, and all who live in your house, shall go into captivity. To Babylon you shall go; and there you shall die, and there you shall be buried — you and all your friends to whom you have prophesied lies.",
      "M": "And you, Pashhur, with everyone in your household, will go into exile. You will go to Babylon, and there you will die, and there you will be buried — you and all your friends to whom you have given false prophecies.",
      "T": "And you, Pashhur — you and everyone in your household — will go into exile. Babylon is where you are going, and Babylon is where you will die and be buried. You and every friend you have filled with lies."
    },
    "7": {
      "L": "O LORD, you have deceived me, and I was deceived; you are stronger than I, and you have prevailed. I have become a laughingstock all day long; everyone mocks me.",
      "M": "O LORD, you deceived me, and I let myself be deceived; you overpowered me and you won. I have become a laughingstock all day long — everyone mocks me.",
      "T": "LORD, you lured me in, and I was lured. You were too strong for me, and you prevailed. I have become a joke — day after day, every person who sees me mocks me."
    },
    "8": {
      "L": "For whenever I speak, I cry out; I shout, 'Violence and destruction!' For the word of the LORD has become for me a reproach and a derision all day long.",
      "M": "Every time I speak, I have to cry out — 'Violence! Destruction!' — and the word of the LORD has become for me nothing but reproach and mockery all day long.",
      "T": "Every time I open my mouth, I have to cry out about violence and destruction. And the word of Yahweh that I carry has brought me nothing but contempt — mocked, reproached, every day without relief."
    },
    "9": {
      "L": "If I say, 'I will not mention him, or speak any more in his name,' there is in my heart as it were a burning fire shut up in my bones, and I am weary of holding it in, and I cannot.",
      "M": "When I think, 'I will not mention him, I will speak in his name no more,' then there is in my heart something like a burning fire shut up in my bones. I grow weary trying to hold it in, and I simply cannot.",
      "T": "I tell myself: Stop. Do not mention his name again. Say nothing more. But then his word is like a fire locked inside my bones — burning, pressing outward. I exhaust myself trying to contain it. I cannot."
    },
    "10": {
      "L": "For I hear many whispering, 'Terror on every side! Denounce him! Let us denounce him!' All my close friends are watching for my stumbling. 'Perhaps he will be deceived, then we can overpower him and take our revenge on him.'",
      "M": "For I hear many people whispering, 'Terror on every side! Report him — let us report him!' All my trusted friends are waiting for me to slip. 'Perhaps he will be tricked; then we can overpower him and get our revenge.'",
      "T": "I can hear them whispering: Terror on every side — that is what they call me now, throwing my own words back at me. Report him! Denounce him! Even my closest friends are waiting for me to stumble, hoping to catch me in something and settle the score."
    },
    "11": {
      "L": "But the LORD is with me as a mighty warrior; therefore my persecutors will stumble and will not prevail. They will be greatly ashamed, for they will not succeed; their everlasting disgrace will not be forgotten.",
      "M": "But the LORD is with me like a mighty and terrible warrior; therefore my persecutors will stumble and not prevail. They will be utterly shamed because they will fail — a disgrace that will never be forgotten.",
      "T": "But Yahweh is with me — like a fearsome, battle-hardened warrior. My persecutors will stumble and fall. They will not win. They will be crushed with shame because they failed, and that failure will follow them forever."
    },
    "12": {
      "L": "O LORD of hosts, you who test the righteous, who see the kidneys and the heart, let me see your vengeance upon them, for to you have I committed my cause.",
      "M": "O LORD of hosts, who tests the righteous and sees the innermost being — the heart and mind — let me see your vengeance on them, for to you I have committed my case.",
      "T": "Yahweh of hosts — you who test the righteous, who see into the deepest recesses of thought and desire — let me see you take vengeance on them. I have laid my case before you. It is yours to judge."
    },
    "13": {
      "L": "Sing to the LORD; praise the LORD! For he has delivered the life of the needy from the hand of evildoers.",
      "M": "Sing to the LORD! Praise the LORD! For he has rescued the life of the poor from the hand of evildoers.",
      "T": "Sing to Yahweh — praise him! For he has pulled the life of the poor out of the hands of those who would destroy them."
    },
    "14": {
      "L": "Cursed be the day on which I was born; the day when my mother bore me — let it not be blessed!",
      "M": "Cursed be the day I was born! May the day my mother gave birth to me never be blessed!",
      "T": "Cursed be the day I was born. Let there be no blessing on the day my mother brought me into the world."
    },
    "15": {
      "L": "Cursed be the man who brought the news to my father, saying, 'A child is born to you, a son,' making him very glad.",
      "M": "Cursed be the man who brought the news to my father — 'A son has been born to you!' — and made him so happy.",
      "T": "Cursed be the man who ran to my father and said, 'Good news — a son has been born to you!' and made my father's face light up."
    },
    "16": {
      "L": "Let that man be like the cities that the LORD overthrew without relenting; let him hear a cry in the morning and an alarm at noon,",
      "M": "Let that man be like the cities the LORD destroyed without pity; let him hear a cry of distress in the morning and a battle alarm at noon,",
      "T": "Let that man end up like the cities Yahweh destroyed without mercy — hearing the sound of alarm at dawn and the battle cry at noon,"
    },
    "17": {
      "L": "because he did not kill me in the womb; so my mother would have been my grave and her womb forever great.",
      "M": "because he did not kill me in the womb, so that my mother would have been my grave, and her womb forever large with me.",
      "T": "because he did not let death take me in the womb. Had he done so, my mother's womb would have been my grave, and she would have carried me forever."
    },
    "18": {
      "L": "Why did I come forth from the womb to see toil and sorrow, and to spend my days in shame?",
      "M": "Why did I ever come out of the womb? All I have known is trouble and sorrow, and my life will end in disgrace.",
      "T": "Why did I come out of the womb at all? All I have ever seen is struggle and grief, and I will end my days in shame."
    }
  },
  "21": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD, when King Zedekiah sent to him Pashhur the son of Melchiah and Zephaniah the son of Maaseiah the priest, saying:",
      "M": "This is the word that came to Jeremiah from the LORD when King Zedekiah sent Pashhur son of Malkijah and the priest Zephaniah son of Maaseiah to him with this message:",
      "T": "This is the word Yahweh gave to Jeremiah when King Zedekiah sent a delegation to him — Pashhur son of Malkijah and the priest Zephaniah son of Maaseiah — with this question:"
    },
    "2": {
      "L": "Please inquire of the LORD for us, for Nebuchadrezzar king of Babylon is making war against us. Perhaps the LORD will deal with us according to all his wonderful deeds and will make him withdraw from us.",
      "M": "Please seek a word from the LORD for us, because Nebuchadnezzar king of Babylon is attacking us. Perhaps the LORD will do something miraculous for us and make him withdraw.",
      "T": "Ask Yahweh for us. Nebuchadnezzar is at war against us. Maybe Yahweh will intervene in one of his great saving acts and make Nebuchadnezzar pull back."
    },
    "3": {
      "L": "Then Jeremiah said to them: Thus you shall say to Zedekiah:",
      "M": "Jeremiah answered them: Tell Zedekiah this:",
      "T": "Jeremiah answered: This is what you are to tell Zedekiah:"
    },
    "4": {
      "L": "Thus says the LORD, the God of Israel: Behold, I will turn back the weapons of war that are in your hands, with which you are fighting against the king of Babylon and the Chaldeans who are besieging you outside the walls, and I will assemble them into the midst of this city.",
      "M": "This is what the LORD, the God of Israel, says: I am going to turn back the weapons in your hands — the very weapons with which you are fighting the king of Babylon and the Chaldeans who besiege you outside the walls — and I will drive them into the center of this city.",
      "T": "Yahweh, God of Israel, says this: The weapons in your hands — the ones you are using to fight Babylon and the Chaldeans outside your walls — I am going to turn those around. I will drive the battle inside this city."
    },
    "5": {
      "L": "And I myself will fight against you with outstretched hand and strong arm, in anger and in fury and in great wrath.",
      "M": "And I myself will fight against you with an outstretched hand and a mighty arm, in burning anger and fury and great wrath.",
      "T": "And I myself will fight against you — with outstretched hand, with mighty arm, in burning anger, in relentless fury, in great and terrible wrath."
    },
    "6": {
      "L": "And I will strike down the inhabitants of this city, both man and beast; they shall die of a great pestilence.",
      "M": "I will strike down everyone living in this city — both people and animals — and they will die from a terrible plague.",
      "T": "I will strike down everyone in this city — every human being, every animal. They will die from a great plague."
    },
    "7": {
      "L": "And afterward, declares the LORD, I will give Zedekiah king of Judah and his servants and the people — those in this city who survive the pestilence, the sword, and the famine — into the hand of Nebuchadrezzar king of Babylon, into the hand of their enemies, into the hand of those who seek their lives. He will strike them with the edge of the sword; he will not pity them or spare them or have mercy.",
      "M": "After that, declares the LORD, I will hand over Zedekiah king of Judah, his officials, and those in this city who survive the plague, the sword, and the famine — all of them — to Nebuchadnezzar king of Babylon, to their enemies who seek their lives. He will put them to the sword without pity, without mercy, without compassion.",
      "T": "After all that, says Yahweh, I will deliver Zedekiah and his court and whoever in this city survives the plague and the sword and the famine — I will hand them all over to Nebuchadnezzar, into the hands of their enemies, into the hands of those who want to kill them. He will cut them down without pity, without sparing anyone, without a drop of mercy."
    },
    "8": {
      "L": "And to this people you shall say: Thus says the LORD: Behold, I set before you the way of life and the way of death.",
      "M": "Say this to the people: This is what the LORD says — I am setting before you the way of life and the way of death.",
      "T": "And say this to the people: Yahweh says — I am putting two roads before you: the way of life and the way of death."
    },
    "9": {
      "L": "He who stays in this city shall die by the sword, by famine, and by pestilence; but he who goes out and surrenders to the Chaldeans who are besieging you shall live and shall have his life as a prize of war.",
      "M": "Whoever stays in this city will die by the sword, famine, or plague; but whoever goes out and surrenders to the Chaldeans who besiege you will live — his life will be his prize.",
      "T": "Whoever stays inside this city will die — by sword, by famine, or by plague. But whoever goes out and surrenders to the Chaldeans besieging you will live. Life itself will be his prize."
    },
    "10": {
      "L": "For I have set my face against this city for harm and not for good, declares the LORD. It shall be given into the hand of the king of Babylon, and he shall burn it with fire.",
      "M": "For I have fixed my gaze on this city for disaster and not for good, declares the LORD. It will be handed over to the king of Babylon, who will burn it to the ground.",
      "T": "I have fixed my gaze on this city, says Yahweh — and what I intend for it is not good. I am handing it to the king of Babylon, and he will burn it down."
    },
    "11": {
      "L": "And to the house of the king of Judah say: Hear the word of the LORD,",
      "M": "And to the house of the king of Judah, say: Hear the word of the LORD —",
      "T": "To the royal house of Judah, say: Hear what Yahweh says —"
    },
    "12": {
      "L": "O house of David! Thus says the LORD: Execute justice in the morning, and deliver from the hand of the oppressor him who has been robbed, lest my wrath go forth like fire and burn with none to quench it, because of your evil deeds.",
      "M": "House of David! This is what the LORD says: Administer justice every morning; rescue from the oppressor those who have been robbed, or my anger will break out like an unquenchable fire because of your evil deeds.",
      "T": "House of David! Yahweh says: Administer justice — every morning, as the first act of the day. Pull the victims of oppression out of the hands of those who rob them. If you do not, my fury will break out like fire, and nothing will be able to stop it. Your own evil deeds will have lit that blaze."
    },
    "13": {
      "L": "Behold, I am against you, O inhabitant of the valley, O rock of the plain, declares the LORD — you who say, 'Who shall come down against us, or who shall enter our habitations?'",
      "M": "I am against you, Jerusalem — you who sit enthroned in the valley, on your rocky plateau, declares the LORD — who say, 'Who can attack us? Who can breach our strongholds?'",
      "T": "I am against you, city perched on the valley, city that sits on its rock and says: Who can reach us? Who can possibly get in here? Yahweh says it: I am against you."
    },
    "14": {
      "L": "I will punish you according to the fruit of your deeds, declares the LORD, and I will kindle a fire in her forest, and it shall devour all that is around her.",
      "M": "I will punish you as your deeds deserve, declares the LORD. I will set fire to your forest — and it will burn up everything around you.",
      "T": "I will repay you according to what you have done, says Yahweh. I will set fire to the forests within your walls, and the fire will consume everything around you."
    }
  },
  "22": {
    "1": {
      "L": "Thus says the LORD: Go down to the house of the king of Judah and speak there this word,",
      "M": "This is what the LORD says: Go down to the palace of the king of Judah and deliver this message there:",
      "T": "Yahweh says: Go down to the royal palace and deliver this word there:"
    },
    "2": {
      "L": "and say, 'Hear the word of the LORD, O king of Judah who sits on the throne of David — you, and your servants, and your people who enter by these gates.",
      "M": "'Hear the word of the LORD, O king of Judah — you who sit on David's throne — and your officials and your people who enter through these gates.'",
      "T": "'King of Judah — you who sit on David's throne — and your court and all your people who pass through these gates: hear the word of Yahweh.'"
    },
    "3": {
      "L": "Thus says the LORD: Do justice and righteousness, and deliver from the hand of the oppressor him who has been robbed. And do no wrong or violence to the resident alien, the fatherless, and the widow, and shed no innocent blood in this place.",
      "M": "This is what the LORD says: Do what is just and right. Rescue from the oppressor those who have been robbed. Do not wrong or oppress the foreigner, the fatherless, or the widow, and shed no innocent blood in this place.",
      "T": "Yahweh says: Do what is just and right. Rescue from the oppressor those who have been robbed. Stop wronging the foreigner, the orphan, and the widow. Stop shedding innocent blood in this city."
    },
    "4": {
      "L": "For if you do indeed obey this word, then there shall enter by the gates of this house kings who sit on the throne of David, riding in chariots and on horses — they and their servants and their people.",
      "M": "For if you carefully obey this command, then kings who sit on David's throne will continue to pass through the gates of this palace — riding in chariots and on horses, with their officials and their people.",
      "T": "If you will actually obey this — kings sitting on David's throne will continue to enter through these very gates, in chariots and on horseback, with all their court and all their people."
    },
    "5": {
      "L": "But if you will not listen to these words, I swear by myself, declares the LORD, that this house shall become a desolation.",
      "M": "But if you refuse to listen to these words, I swear by myself, declares the LORD, that this house will become a ruin.",
      "T": "But if you will not listen — I swear by myself, says Yahweh, that this palace will become a heap of rubble."
    },
    "6": {
      "L": "For thus says the LORD concerning the house of the king of Judah: You are like Gilead to me, like the summit of Lebanon; yet surely I will make you a wilderness, cities not inhabited.",
      "M": "For this is what the LORD says about the palace of the king of Judah: You are Gilead to me, the heights of Lebanon — yet I will surely make you a wasteland, towns that no one lives in.",
      "T": "Yahweh says this about the royal house of Judah: You are like Gilead to me — like the peaks of Lebanon. And yet I will absolutely make you a wilderness — deserted cities, no inhabitant."
    },
    "7": {
      "L": "I will prepare destroyers against you, each with his weapons, and they shall cut down your choice cedars and cast them into the fire.",
      "M": "I will send destroyers against you, each armed with weapons; they will fell your finest cedar trees and throw them into the fire.",
      "T": "I am readying those who will destroy you — armed, methodical. They will cut down your finest cedar beams and throw them into the fire."
    },
    "8": {
      "L": "And many nations will pass by this city, and every man will say to his neighbor, 'Why has the LORD done thus to this great city?'",
      "M": "Many nations will pass by this city, and they will ask one another, 'Why has the LORD done this to such a great city?'",
      "T": "People from many nations will pass by this city and ask each other: Why did Yahweh do this to such a great city?"
    },
    "9": {
      "L": "And they will answer: Because they forsook the covenant of the LORD their God and worshiped other gods and served them.",
      "M": "And they will answer: Because they abandoned the covenant of the LORD their God and worshiped and served other gods.",
      "T": "And the answer will be: Because they broke faith with Yahweh their God — abandoned his covenant, turned to other gods and served them."
    },
    "10": {
      "L": "Weep not for him who is dead, nor grieve for him; but weep bitterly for him who goes away, for he shall return no more and see the land of his birth.",
      "M": "Do not weep for the dead king or mourn for him; but weep bitterly for the one who goes into exile, for he will never come back to see his native land again.",
      "T": "Do not weep for the one who is dead — grieve is wasted there. Weep for the one going away, for he will never come back. He will never see this land again."
    },
    "11": {
      "L": "For thus says the LORD concerning Shallum the son of Josiah, king of Judah, who reigned instead of Josiah his father, and who went away from this place: He shall return here no more,",
      "M": "For this is what the LORD says about Shallum son of Josiah, who succeeded his father Josiah as king of Judah and has now left this place: He will never come back.",
      "T": "Yahweh says this about Shallum son of Josiah — who succeeded his father as king of Judah and has now gone away from this city: He is not coming back."
    },
    "12": {
      "L": "but in the place where they have carried him captive, there shall he die, and he shall never see this land again.",
      "M": "He will die in the place he has been taken captive, and he will never see this land again.",
      "T": "He will die in the place they have taken him captive. He will never see this land again."
    },
    "13": {
      "L": "Woe to him who builds his house by unrighteousness and his upper rooms by injustice, who makes his neighbor serve him for nothing and does not give him his wages,",
      "M": "Woe to him who builds his palace through injustice and his upper rooms through unrighteousness — who makes his countrymen work for nothing and does not pay them their wages,",
      "T": "Woe to him who builds his palace through injustice, room by room through exploitation — who forces his neighbors into unpaid labor and refuses to pay what he owes them."
    },
    "14": {
      "L": "who says, 'I will build myself a great house with spacious upper rooms,' and who cuts out windows for it, paneling it with cedar and painting it with vermilion.",
      "M": "who says, 'I will build myself a grand palace with large upper rooms,' cutting out windows for it, paneling it with cedar, and painting it with red paint.",
      "T": "He says: I will build myself a magnificent palace — great vaulted rooms, windows cut into the walls, lined with cedar, painted in red. All while paying the workers nothing."
    },
    "15": {
      "L": "Do you think you are a king because you compete in cedar? Did not your father eat and drink and do justice and righteousness? Then it was well with him.",
      "M": "Do you think that making yourself a rival in cedar proves you are a king? Your father ate and drank, but he also practiced justice and righteousness — and things went well for him.",
      "T": "Does accumulating cedar make you a king? Your father ate and drank too. But he also did what was right and just — and things went well for him because of it."
    },
    "16": {
      "L": "He judged the cause of the poor and needy; then it was well. Is not this to know me? declares the LORD.",
      "M": "He defended the cause of the poor and needy; then it went well. Is that not what it means to know me? declares the LORD.",
      "T": "He took up the cause of the poor and the needy — and things went well. That is what it means to know me, says Yahweh. Not doctrine. Not ceremony. Action on behalf of the poor."
    },
    "17": {
      "L": "But your eyes and your heart are only on your dishonest gain, and for shedding innocent blood, and for practicing oppression and violence.",
      "M": "But you have no eyes or heart for anything except your own dishonest gain, and for shedding innocent blood, and for practicing oppression and violence.",
      "T": "But your eyes and your heart are fixed on one thing only: personal gain by any means, the shedding of innocent blood, the practice of oppression and violence."
    },
    "18": {
      "L": "Therefore thus says the LORD concerning Jehoiakim the son of Josiah, king of Judah: They shall not lament for him, saying, 'Ah, my brother!' or 'Ah, sister!' They shall not lament for him, saying, 'Ah, lord!' or 'Ah, his glory!'",
      "M": "Therefore this is what the LORD says about Jehoiakim son of Josiah, king of Judah: No one will mourn for him, crying, 'Ah, my brother!' or 'Ah, my sister!' No one will mourn for him, crying, 'Ah, my lord!' or 'Alas, his glory!'",
      "T": "So Yahweh says this about Jehoiakim son of Josiah, king of Judah: No one will grieve for him. No one will cry, 'My brother! My sister!' No one will lament, 'My lord! His splendor!' None of the formal mourning rites will be performed for him."
    },
    "19": {
      "L": "He shall be buried with the burial of a donkey — dragged and thrown outside the gates of Jerusalem.",
      "M": "He will be buried like a donkey — dragged away and thrown outside the gates of Jerusalem.",
      "T": "He will have the burial of a donkey: dragged away and dumped outside the gates of Jerusalem. That will be the end of him."
    },
    "20": {
      "L": "Go up to Lebanon and cry out, and lift up your voice in Bashan; cry out from Abarim, for all your lovers are destroyed.",
      "M": "Go up to Lebanon and cry out; lift your voice in Bashan; cry from the passes of Abarim — for all your allies have been shattered.",
      "T": "Go up to Lebanon and wail. Cry out from Bashan. Send your voice from the mountain passes of Abarim — because every ally you depended on has been destroyed."
    },
    "21": {
      "L": "I spoke to you in your prosperity, but you said, 'I will not listen.' This has been your way from your youth, that you have not obeyed my voice.",
      "M": "I warned you when you were at ease, but you said, 'I will not listen.' This has been your habit from your youth — you have never obeyed my voice.",
      "T": "I warned you when everything was going well. You said: I will not listen. That has been your pattern from childhood. You have never obeyed my voice — not once."
    },
    "22": {
      "L": "The wind shall shepherd all your shepherds, and your lovers shall go into captivity; then you shall be ashamed and confounded because of all your evil.",
      "M": "The wind will sweep away all your rulers, and your allies will go into captivity; then you will be ashamed and disgraced because of all your wickedness.",
      "T": "The wind will devour your shepherds — every leader you have. Your allies will go into exile. And then the full weight of your own wickedness will fall on you, and shame will be all that is left."
    },
    "23": {
      "L": "O inhabitant of Lebanon, nested in the cedars, how you will groan when pangs come upon you, pain like a woman in labor!",
      "M": "You who live in Lebanon, nestled among the cedars — how you will groan when birth pangs seize you, pain like a woman in labor!",
      "T": "You who perch in Lebanon, who think yourself secure in the cedars — when the pangs come, how you will cry out. The pain will be like labor, and there will be no escaping it."
    },
    "24": {
      "L": "As I live, declares the LORD, even if Coniah the son of Jehoiakim, king of Judah, were the signet ring on my right hand, yet I would tear you off",
      "M": "As surely as I live, declares the LORD, even if Coniah son of Jehoiakim, king of Judah, were the signet ring on my right hand, I would still pull you off",
      "T": "As I live, says Yahweh — even if Coniah son of Jehoiakim were the signet ring on my own right hand, the ring that bears my seal, I would pull him off and throw him away."
    },
    "25": {
      "L": "and give you into the hand of those who seek your life, into the hand of those you fear, into the hand of Nebuchadrezzar king of Babylon and into the hand of the Chaldeans.",
      "M": "and hand you over to those who seek your life and whom you dread — to Nebuchadnezzar king of Babylon and to the Chaldeans.",
      "T": "I would hand him over to those who want to kill him — to Nebuchadnezzar, to the Chaldeans, to the very men he fears most."
    },
    "26": {
      "L": "I will hurl you and the mother who bore you into another country, where you were not born, and there you shall die.",
      "M": "I will hurl you and the mother who gave birth to you into another country — a land where neither of you was born — and there you will both die.",
      "T": "I will throw both him and his mother into a foreign country — a land where neither of them was ever born. And there they will die."
    },
    "27": {
      "L": "But to the land to which they will long to return, there they shall not return.",
      "M": "As for the land they long to return to — they will never return there.",
      "T": "The land they will long for, the land they will ache to come home to — they will never see it again."
    },
    "28": {
      "L": "Is this man Coniah a despised, shattered pot, a vessel no one wants? Why are he and his children hurled and thrown into a land they do not know?",
      "M": "Is this man Coniah nothing but a broken, despised clay pot — something no one wants? Why are he and his children being hurled away into a land they do not know?",
      "T": "Is this man Coniah just a worthless broken jar — cracked, cast aside, fit for nothing? Why are he and his children being thrown away into a land they have never known?"
    },
    "29": {
      "L": "O earth, earth, earth, hear the word of the LORD!",
      "M": "O land, land, land, hear the word of the LORD!",
      "T": "Earth, earth, earth — hear the word of Yahweh!"
    },
    "30": {
      "L": "Thus says the LORD: Write this man down as childless, a man who shall not prosper in his days; for none of his offspring shall succeed in sitting on the throne of David and ruling again in Judah.",
      "M": "This is what the LORD says: Record this man as though childless — a man who will not prosper in his lifetime; for none of his descendants will succeed in sitting on the throne of David and ruling over Judah.",
      "T": "Yahweh says: Register this man as if he were childless — a man whose days bring no success. Not one of his descendants will sit on the throne of David or rule over Judah ever again."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 19–22 written.')

if __name__ == '__main__':
    main()
