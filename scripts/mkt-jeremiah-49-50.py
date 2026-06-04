"""
MKT Jeremiah chapters 49–50 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-49-50.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-43-46.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name
  force matters — oracle delivery, confrontation, divine oath.

- H430 (אֱלֹהִים): "God" in all three tiers.

- H6635 (צְבָאוֹת): "of hosts" retained in all three tiers.

- H4428 (מַלְכָּם) in 49:1,3: rendered "Milcom" (the Ammonite national deity) rather
  than the literal "their king." The Hebrew מַלְכָּם functions as a divine name for
  Molech/Milcom (cf. 1 Kgs 11:5,33; Zeph 1:5). The rhetorical point of v.1 is that
  Ammon's god has displaced Israel's inheritance — not merely Ammon's human king.

- H1347 (גָּאוֹן) in 49:19 and 50:44: rendered "thickets of the Jordan" (not "pride").
  In these lion-emergence similes the word denotes the luxuriant overgrowth of the
  Jordan floodplain — the tangled brush where lions sheltered before surging to pasture.
  Most modern versions follow this reading.

- H7307 (רוּחַ) in 49:32,36: "winds" in all three tiers — clearly the four cardinal
  atmospheric winds, not Spirit. No ambiguity in this context.

- H1285 (בְּרִית) in 50:5: "covenant" in L/M; T "unbreakable covenant." The phrase
  בְּרִית עוֹלָם = perpetual/everlasting covenant — echoes Jer 31:31-34 new covenant.

- H1350 (גָּאַל) in 50:34: "Redeemer" (capitalized) in all three tiers — functioning as
  a divine title for Yahweh as Israel's kinsman-redeemer, as in Isa 41:14; 44:6.

- H2087 (זָדוֹן) in 50:31-32: "most arrogant" — L/M "O most arrogant"; T "you who
  are most proud of all nations." Babylon as the apex of human pride against God.

- Merathaim (50:21): "double rebellion" — wordplay on Marratu (a Babylonian marsh
  district); Pekod = wordplay on Puqudu (an Aramean tribe in eastern Babylonia) and
  the Hebrew root for "punishment/visitation." All three tiers transliterate the proper
  names to preserve the dual referent.

- Bel (H1078) and Merodach (H4781) in 50:2: Bel = "Lord" (title of Marduk, chief
  Babylonian deity); Merodach = Marduk (his personal name). Both rendered by proper
  name in all three tiers.

- H907 (בַּד) in 50:36: "her false prophets" in M/T; L "her liars." The term designates
  empty boasters/diviners — the professional prognosticators of the Babylonian court
  who predicted Babylon's permanence.

- H5315 (נֶפֶשׁ) in 50:37: "courage/fighting spirit" — soldiers becoming "like women"
  (a standard ANE idiom for complete military collapse). T surfaces the idiom as meaning.

- Edom oracle (49:7-22): extensive parallel with Obadiah 1-9. Especially vv.14-16 ≈
  Obad 1-4. The priority direction is debated; all three tiers treat the material as
  part of the unified Jeremian oracle corpus.

- Nebuchadrezzar: consistent Jeremian form throughout (not "Nebuchadnezzar").

- "Full end" / "utterly destroy" (כָּלָה, 50:21,26): the חֵרֶם (devotion to destruction)
  formula — L: "devote to destruction"; M: "completely destroy"; T: "wipe out entirely."

- 50:40 ≈ 49:18 (Sodom comparison applied first to Edom, then to Babylon): intentional
  literary bracketing — the same formula of total abandonment frames both oracles.

OT intertextuality:
- 49:14-16 ≈ Obad 1-4 (Edom oracle — nearly identical wording).
- 49:19 = 50:44 (lion from Jordan thicket — identical simile applied first to Edom,
  then repeated for Babylon; the repetition is deliberate).
- 49:18 = 50:40 (Sodom comparison — applied to Edom then Babylon).
- 49:20 = 50:45 (the "counsel of the LORD against" formula — also repeated verbatim).
- 50:3 echoes Jer 1:13-15 (foe from the north).
- 50:5 echoes Jer 31:31-34 (perpetual covenant / new covenant).
- 50:6 echoes Ezek 34 (lost sheep, negligent shepherds).
- 50:23 — "hammer of the whole earth" echoes Jer 25:9 (Babylon as divine instrument).
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


JEREMIAH = {
  "49": {
    "1": {
      "L": "Concerning the Ammonites: thus says the LORD. Has Israel no sons? Has he no heir? Why then has Milcom dispossessed Gad, and his people settled in its cities?",
      "M": "Concerning the Ammonites: thus says the LORD. Has Israel no sons? Has he no heir? Why then has Milcom taken possession of Gad, and his people settled in its cities?",
      "T": "Concerning the Ammonites — Yahweh says this: Has Israel no sons? No heir to the land? Why then has Milcom seized Gad's inheritance and his people occupied its towns?"
    },
    "2": {
      "L": "Therefore behold, the days are coming, declares the LORD, when I will make the tumult of war heard against Rabbah of the Ammonites. It shall become a desolate mound, and its towns shall be burned with fire. Then Israel shall dispossess those who dispossessed him, says the LORD.",
      "M": "Therefore the days are coming, declares the LORD, when I will cause the war cry to be heard against Rabbah of the Ammonites. It shall become a desolate heap, and its surrounding villages shall be burned with fire. Then Israel will dispossess those who dispossessed him, says the LORD.",
      "T": "The days are coming — Yahweh declares it — when the war cry will ring out against Rabbah in Ammon. That city will be turned into a ruined heap and its surrounding towns burned to the ground. Then Israel will take back what was taken from her."
    },
    "3": {
      "L": "Wail, O Heshbon, for Ai is laid waste! Cry out, O daughters of Rabbah! Gird yourselves with sackcloth; lament and run to and fro along the hedges, for Milcom shall go into exile with his priests and his princes.",
      "M": "Wail, O Heshbon, for Ai is laid waste! Cry out, O daughters of Rabbah! Put on sackcloth and lament; run back and forth along the fences, for Milcom shall go into exile, along with his priests and his princes.",
      "T": "Wail, Heshbon — Ai is destroyed! Daughters of Rabbah, break out in mourning! Wrap yourselves in sackcloth; wail and run back and forth along the hedgerows. For Milcom himself is going into exile, priests and princes swept away with him."
    },
    "4": {
      "L": "Why do you glory in your valleys, O faithless daughter? Your valley flows away — you who trust in your treasures, saying: Who will come against me?",
      "M": "Why do you boast about your valleys, O faithless daughter? Your valley is flowing away; you who trusted in your treasures, saying: Who will come against me?",
      "T": "Why are you so proud of your abundant valleys, O daughter who keeps turning away? You trusted in your riches and thought: Who could ever reach me?"
    },
    "5": {
      "L": "Behold, I am bringing a terror upon you, declares the Lord GOD of hosts, from all those around you; and you shall be driven out, every man straight ahead, with no one to gather the fugitives.",
      "M": "Behold, I am about to bring terror upon you, declares the Lord GOD of hosts, from all your surrounding neighbors; and you shall be driven out, every man heading straight forward, with no one to gather the scattered.",
      "T": "I am bringing a terror down on you — the Lord Yahweh of hosts declares it — from every direction, from all your neighbors. You will be driven out, every person fleeing headlong, with no one to round up the refugees."
    },
    "6": {
      "L": "But afterward I will restore the fortunes of the Ammonites, declares the LORD.",
      "M": "But afterward I will restore the fortunes of the Ammonites, declares the LORD.",
      "T": "But after this, I will restore Ammon's fortunes. Yahweh declares it."
    },
    "7": {
      "L": "Concerning Edom: thus says the LORD of hosts. Is wisdom no more in Teman? Has counsel perished from the prudent? Has their wisdom vanished?",
      "M": "Concerning Edom: thus says the LORD of hosts. Is there no longer wisdom in Teman? Has counsel perished from the discerning? Has their wisdom dissolved?",
      "T": "Concerning Edom — Yahweh of hosts says this: Is there no wisdom left in Teman? Has sound counsel disappeared from those who were once wise? Has their understanding simply evaporated?"
    },
    "8": {
      "L": "Flee! Turn back! Dwell in the depths, O inhabitants of Dedan! For I will bring the calamity of Esau upon him — the time when I punish him.",
      "M": "Flee! Turn and withdraw into the depths, O inhabitants of Dedan! For I will bring the disaster of Esau upon him — the time when I visit him with punishment.",
      "T": "Flee! Turn back! Take cover in the wilderness depths, you people of Dedan! For I am bringing Esau's disaster on him — the moment of his reckoning has arrived."
    },
    "9": {
      "L": "If grape-gatherers came to you, would they not leave some gleanings? If thieves came by night, would they not steal only until they had enough?",
      "M": "If grape-gatherers came to you, would they not leave some gleanings? If thieves came by night, they would steal only what they wanted.",
      "T": "When grape-pickers work through a vineyard, they always leave something behind. When thieves break in at night, they take only what they need. But Edom will not be left even that much."
    },
    "10": {
      "L": "But I myself have stripped Esau bare; I have uncovered his secret places, so that he is not able to conceal himself. His offspring are destroyed, his brothers and his neighbors — he is no more.",
      "M": "But I myself have stripped Esau bare; I have exposed his hiding places, so he cannot conceal himself. His children are destroyed, along with his brothers and his neighbors — he is gone.",
      "T": "But I have stripped Esau completely bare. I have exposed every hiding place — there is nowhere left for him to conceal himself. His children are gone, his brothers gone, his neighbors gone. There is nothing left."
    },
    "11": {
      "L": "Leave your orphans — I will keep them alive; and let your widows trust in me.",
      "M": "Leave your orphans; I will keep them alive. Your widows may trust in me.",
      "T": "Leave your orphaned children — I will care for them. Your widows can put their trust in me."
    },
    "12": {
      "L": "For thus says the LORD: If those who did not deserve to drink the cup must still drink it, will you go entirely unpunished? You will not go unpunished; you shall surely drink it.",
      "M": "For thus says the LORD: If those who did not deserve to drink the cup have had to drink it, will you go without punishment? You will not go unpunished; you shall certainly drink it.",
      "T": "Yahweh says this: Those who were not even supposed to drink the cup of judgment have had to drink it. Do you think you will escape without drinking? You will not. You will drain it."
    },
    "13": {
      "L": "For I have sworn by myself, declares the LORD, that Bozrah shall become a desolation and a reproach, a ruin and a curse; and all its cities shall become perpetual ruins.",
      "M": "For I have sworn by myself, declares the LORD, that Bozrah shall become a desolation, an object of reproach, a ruin, and a curse; all its towns shall be ruined forever.",
      "T": "I have sworn by my own name — Yahweh declares it — that Bozrah will become a desolation, a reproach, a ruin, and a curse. Every one of its towns will lie in permanent ruin."
    },
    "14": {
      "L": "I have heard a message from the LORD, and an envoy has been sent among the nations: Gather together and come against her! Rise up for battle!",
      "M": "I have heard a message from the LORD; an envoy has been sent among the nations: Gather yourselves together and come against her! Rise up for battle!",
      "T": "I have heard a dispatch from Yahweh. A messenger is going out among the nations: Muster your forces and march against her! Prepare for battle!"
    },
    "15": {
      "L": "For behold, I will make you small among the nations, despised among mankind.",
      "M": "For I will make you least among the nations, despised among human beings.",
      "T": "I will cut you down to the smallest of nations — despised among all peoples."
    },
    "16": {
      "L": "Your fearsome reputation has deceived you — the pride of your heart — O you who dwell in the clefts of the rock and hold the heights of the hill. Though you make your nest as high as the eagle, from there I will bring you down, declares the LORD.",
      "M": "Your fearsome reputation has deceived you — the pride of your heart — O you who live in the clefts of the rock and occupy the heights of the hill. Though you set your nest as high as the eagle, I will bring you down from there, declares the LORD.",
      "T": "Your reputation for terror has seduced you — that arrogance at the core of you. You live in the crannies of the cliffs; you hold the high ground. You have built your nest higher than the eagle — but I will drag you down from there. Yahweh declares it."
    },
    "17": {
      "L": "Edom shall become a horror; everyone who passes by it will be appalled and will hiss at all its disasters.",
      "M": "Edom shall become a horror; everyone who passes by it will be appalled and will hiss at all its calamities.",
      "T": "Edom will be left a horror. Everyone who passes through will recoil and hiss in disbelief at everything that has happened to it."
    },
    "18": {
      "L": "As when Sodom and Gomorrah and their neighboring cities were overthrown, says the LORD, no one shall dwell there, and no son of man shall sojourn in her.",
      "M": "As in the overthrow of Sodom and Gomorrah and their neighboring towns, says the LORD, no one will dwell there, and no human being will settle there.",
      "T": "Like the catastrophic end of Sodom and Gomorrah and the towns around them — Yahweh says it — no one will ever settle there again. Not a single person will live there."
    },
    "19": {
      "L": "Behold, like a lion coming up from the thickets of the Jordan against the strong pasture, I will suddenly make Edom run from her; and I will appoint over her whomever I choose. For who is like me? Who will summon me? What shepherd can stand before me?",
      "M": "Behold, like a lion coming up from the thickets of the Jordan against the strong meadow, I will suddenly drive Edom away; and I will appoint over her whomever I choose. For who is like me? Who can challenge me? What shepherd can stand before me?",
      "T": "A lion rises from the tangled undergrowth of the Jordan valley and surges toward the rich pastureland — and just as suddenly I will drive Edom off. I will appoint whoever I choose to rule over her. For who is my equal? Who could summon me to account? What shepherd could face me and survive?"
    },
    "20": {
      "L": "Therefore hear the counsel of the LORD that he has taken against Edom, and his purposes that he has purposed against the inhabitants of Teman: Surely the little ones of the flock shall be dragged away; surely he shall make their pastures desolate over them.",
      "M": "Therefore hear the plan the LORD has made against Edom and the purposes he has decided against the inhabitants of Teman: Surely even the weakest of the flock will be dragged away; surely he will make their pastures a desolation.",
      "T": "Hear, then, the strategy Yahweh has formed against Edom — the purposes he has shaped against the people of Teman: Even the weakest lamb will be dragged off, and the very pastures will be turned into wasteland around them."
    },
    "21": {
      "L": "At the sound of their fall the earth quakes; the sound of their cry is heard at the Red Sea.",
      "M": "At the noise of their fall the earth trembles; the cry of their collapse is heard as far as the Red Sea.",
      "T": "The earth will tremble at the noise of Edom's collapse. Their cry will be heard as far away as the Red Sea."
    },
    "22": {
      "L": "Behold, he shall come up and fly like an eagle and spread his wings over Bozrah; and the heart of Edom's mighty men shall be in that day like the heart of a woman in her labor pangs.",
      "M": "Behold, he shall come up and sweep like an eagle, spreading his wings over Bozrah; and the heart of Edom's warriors shall on that day be like the heart of a woman in labor.",
      "T": "He rises and swoops like an eagle, spreading his wings over Bozrah. On that day the hearts of Edom's bravest warriors will be like the heart of a woman writhing in the anguish of childbirth."
    },
    "23": {
      "L": "Concerning Damascus: Hamath and Arpad are dismayed, for they have heard evil news; they melt in anxiety. There is anguish on the sea — it cannot be calm.",
      "M": "Concerning Damascus: Hamath and Arpad are dismayed, for they have heard bad news; they are troubled. There is anguish like the restless sea — it cannot be stilled.",
      "T": "Concerning Damascus: Hamath and Arpad are thrown into confusion by the terrible news; they are sick with dread. Anxiety churns through them like a sea that will not quiet itself."
    },
    "24": {
      "L": "Damascus has become feeble; she has turned to flee, and panic has seized her; anguish and sorrows have taken hold of her like a woman in labor.",
      "M": "Damascus has grown feeble; she has turned to run away; panic has seized her, and anguish and torment have gripped her like a woman in labor.",
      "T": "Damascus has gone limp. She turned to flee and was seized by panic. Anguish and birth-pangs have gripped her; she cannot stand."
    },
    "25": {
      "L": "How is the city of praise not forsaken, the city of my joy!",
      "M": "How is the renowned city not abandoned, the city of my delight!",
      "T": "How can the city that was once celebrated — the city that was my delight — end up like this?"
    },
    "26": {
      "L": "Therefore her young men shall fall in her streets, and all the men of war shall be silenced in that day, declares the LORD of hosts.",
      "M": "Therefore her young men will fall in her streets, and all the soldiers will be struck down on that day, declares the LORD of hosts.",
      "T": "That is why her young men are falling in the streets, and all her soldiers will be cut down on that day. Yahweh of hosts declares it."
    },
    "27": {
      "L": "And I will kindle a fire in the wall of Damascus, and it shall devour the strongholds of Ben-hadad.",
      "M": "I will set fire to the wall of Damascus, and it shall consume the palaces of Ben-hadad.",
      "T": "I will set Damascus's walls ablaze, and the fire will devour every palace of Ben-hadad."
    },
    "28": {
      "L": "Concerning Kedar and the kingdoms of Hazor that Nebuchadrezzar king of Babylon struck down: thus says the LORD. Rise up! Advance against Kedar! Destroy the people of the east!",
      "M": "Concerning Kedar and the kingdoms of Hazor that Nebuchadrezzar king of Babylon struck down: thus says the LORD. Rise! Advance against Kedar! Plunder the people of the east!",
      "T": "Concerning Kedar and the kingdoms of Hazor that Nebuchadrezzar king of Babylon crushed — Yahweh says this: Rise up! March against Kedar! Strip the eastern peoples bare!"
    },
    "29": {
      "L": "Their tents and their flocks shall be taken; their curtains and all their possessions and their camels shall be carried off; and men shall cry to them: Terror on every side!",
      "M": "Their tents and their flocks shall be taken; their curtains and all their belongings and their camels shall be taken away; and they shall cry out to them: Terror on every side!",
      "T": "Their tents and their flocks will be seized; their tent curtains, all their equipment, and their camels will be carried off — and someone will shout over them: Terror on every side!"
    },
    "30": {
      "L": "Flee! Withdraw far away! Dwell in the depths, O inhabitants of Hazor, declares the LORD. For Nebuchadrezzar king of Babylon has made a plan against you and devised a scheme against you.",
      "M": "Flee! Get far away! Go and hide in the depths, O inhabitants of Hazor, declares the LORD. For Nebuchadrezzar king of Babylon has formed a plan against you and devised a strategy against you.",
      "T": "Flee! Get out! Take cover in the wilderness, you people of Hazor — Yahweh declares it — for Nebuchadrezzar king of Babylon has made his plans against you and set his strategy in motion."
    },
    "31": {
      "L": "Rise up! Advance against a nation at ease, that dwells in security, declares the LORD — that has neither gates nor bars, living alone.",
      "M": "Rise and advance against a nation living in ease — that dwells in security, declares the LORD — that has no gates and no bars, living in isolation.",
      "T": "March against a nation that lives in ease — smug and secure, Yahweh declares — with no city gates, no bars, living out there alone in open country."
    },
    "32": {
      "L": "Their camels shall become plunder and their abundant herds a spoil; I will scatter to every wind those who cut the corners of their hair, and I will bring disaster upon them from every direction, declares the LORD.",
      "M": "Their camels shall become plunder and their many cattle a spoil; I will scatter to every wind those who clip the hair on their temples, and I will bring calamity upon them from every direction, declares the LORD.",
      "T": "Their camels will become plunder and their great herds a prize of war. I will scatter those who trim their hair at the temples into every wind — and their disaster will come from every direction. Yahweh declares it."
    },
    "33": {
      "L": "Hazor shall become a lair of jackals, a desolation forever. No one shall dwell there; no son of man shall sojourn there.",
      "M": "Hazor shall become a haunt of jackals, a desolation forever. No one will live there; no human being will settle there.",
      "T": "Hazor will become a den of jackals, a permanent wasteland. No one will ever live there again — no one, ever."
    },
    "34": {
      "L": "The word of the LORD that came to Jeremiah the prophet concerning Elam, at the beginning of the reign of Zedekiah king of Judah, saying:",
      "M": "The word of the LORD that came to Jeremiah the prophet concerning Elam, at the beginning of the reign of Zedekiah king of Judah:",
      "T": "This is the word Yahweh gave to Jeremiah the prophet concerning Elam, at the start of Zedekiah king of Judah's reign:"
    },
    "35": {
      "L": "Thus says the LORD of hosts: Behold, I am going to break the bow of Elam — the chief of their might.",
      "M": "Thus says the LORD of hosts: I am going to break the bow of Elam — the foremost source of their strength.",
      "T": "Yahweh of hosts says this: I am going to break the bow of Elam — the weapon that is the very heart of their power."
    },
    "36": {
      "L": "I will bring against Elam the four winds from the four corners of heaven, and I will scatter them to all those winds; and there shall be no nation to which the outcasts of Elam will not come.",
      "M": "I will bring the four winds from the four corners of heaven against Elam and will scatter them in all directions; there shall be no nation where the outcasts of Elam do not reach.",
      "T": "I will summon the four winds from the four corners of heaven against Elam and scatter its people in every direction. There will not be a single nation on earth that does not receive Elam's refugees."
    },
    "37": {
      "L": "I will shatter Elam before their enemies and before those who seek their life; I will bring disaster upon them, even my fierce anger, declares the LORD. I will send the sword after them until I have consumed them.",
      "M": "I will terrify Elam before their enemies and before those who seek their lives; I will bring disaster upon them — my fierce anger — declares the LORD. I will send the sword after them until I have finished them off.",
      "T": "I will break Elam apart before their enemies — before every faction that wants them destroyed. I am bringing disaster on them, the full force of my fury. Yahweh declares it. I will send the sword after them until I have finished what I started."
    },
    "38": {
      "L": "And I will set my throne in Elam and destroy their king and officials from there, declares the LORD.",
      "M": "I will place my throne in Elam and destroy their king and his officials from there, declares the LORD.",
      "T": "I will set up my throne in Elam and sweep away their king and all his officials from there. Yahweh declares it."
    },
    "39": {
      "L": "But in the latter days I will restore the fortunes of Elam, declares the LORD.",
      "M": "But in the latter days I will restore the fortunes of Elam, declares the LORD.",
      "T": "But in the days to come I will restore Elam's fortunes. Yahweh declares it."
    }
  },
  "50": {
    "1": {
      "L": "The word that the LORD spoke concerning Babylon and the land of the Chaldeans, by the hand of Jeremiah the prophet:",
      "M": "The word that the LORD spoke concerning Babylon and the land of the Chaldeans, through Jeremiah the prophet:",
      "T": "This is the word Yahweh spoke concerning Babylon and the land of the Chaldeans, through Jeremiah the prophet:"
    },
    "2": {
      "L": "Declare among the nations and proclaim; lift up a banner and proclaim; do not conceal it. Say: Babylon is captured; Bel is put to shame; Merodach is dismayed. Her images are put to shame; her idols are dismayed.",
      "M": "Announce it among the nations and proclaim it! Raise the signal banner; proclaim it and do not hide it. Say: Babylon is captured; Bel is put to shame; Merodach is overthrown. Her images are shamed; her idols are shattered.",
      "T": "Broadcast it to the nations — proclaim it! Raise the signal banner and shout it out — hold nothing back: Babylon has fallen! Bel is shamed! Merodach is overthrown! Every idol disgraced, every image smashed!"
    },
    "3": {
      "L": "For a nation has come up against her from the north; it will make her land a desolation, and none shall dwell in it — both man and beast have fled; they are gone.",
      "M": "For a nation has come up from the north against her; it will make her land a desolation, and neither man nor beast will dwell in it — they shall flee and be gone.",
      "T": "A nation is coming up from the north against her — it will leave her land a desolation. No one will live there. Man and beast alike will flee; all will be gone."
    },
    "4": {
      "L": "In those days and at that time, declares the LORD, the people of Israel shall come, they and the people of Judah together; they shall come weeping and shall seek the LORD their God.",
      "M": "In those days and at that time, declares the LORD, the people of Israel will come, together with the people of Judah; they will come weeping and will seek the LORD their God.",
      "T": "In those days and at that time — Yahweh declares it — the people of Israel and the people of Judah will come together, weeping as they go, seeking Yahweh their God."
    },
    "5": {
      "L": "They shall ask the way to Zion, with their faces turned toward it: Come, let us join ourselves to the LORD in a perpetual covenant that shall not be forgotten.",
      "M": "They will ask the way to Zion, their faces turned toward it, saying: Come, let us attach ourselves to the LORD in a permanent covenant that will never be forgotten.",
      "T": "They will ask directions to Zion with their faces set toward home: Come — let us bind ourselves to Yahweh in an unbreakable covenant that will never be forgotten."
    },
    "6": {
      "L": "My people have been lost sheep; their shepherds have led them astray, turning them loose on the mountains; they went from mountain to hill, forgetting their resting place.",
      "M": "My people have been like lost sheep; their shepherds have led them astray, letting them wander on the mountains; they went from mountain to hill, forgetting where they belonged.",
      "T": "My people have been lost sheep. Their shepherds led them off the path — sent them wandering across the mountains, from peak to hill, with no memory of where home was."
    },
    "7": {
      "L": "All who found them devoured them; and their enemies said: We are not guilty, because they sinned against the LORD, the true habitation, even the LORD, the hope of their fathers.",
      "M": "All who found them devoured them; and their enemies said: We are not guilty, for they sinned against the LORD, the true resting place, even the LORD, the hope of their ancestors.",
      "T": "Everyone who found them devoured them. Their enemies said: 'We are not guilty — they sinned against Yahweh, the true home and resting place, Yahweh, the hope of their ancestors.'"
    },
    "8": {
      "L": "Flee from the midst of Babylon and go out from the land of the Chaldeans, and be as goats before the flock.",
      "M": "Flee from the midst of Babylon; go out from the land of the Chaldeans, and be like the he-goats that lead the flock.",
      "T": "Get out of Babylon! Leave the land of the Chaldeans! Be the first ones out — like the lead goats heading up the flock."
    },
    "9": {
      "L": "For behold, I am going to stir up and bring against Babylon an assembly of great nations from the land of the north; they shall set themselves in array against her; from there she shall be captured. Their arrows are like those of an expert warrior — none shall return empty.",
      "M": "For I am going to stir up and bring against Babylon an assembly of great nations from the north; they will array themselves against her, and from there she shall be captured. Their arrows fly like those of an expert who does not return empty-handed.",
      "T": "For I am rousing an assembly of great nations from the north and marshaling them against Babylon. They will take their positions; she will be captured from that direction. Their arrows are those of a master warrior — not one will fly back unspent."
    },
    "10": {
      "L": "Chaldea shall be plundered; all who plunder her shall be satisfied, declares the LORD.",
      "M": "Chaldea will be plundered; all who strip her will be satisfied, declares the LORD.",
      "T": "Chaldea will be thoroughly looted. Everyone who plunders her will have their fill. Yahweh declares it."
    },
    "11": {
      "L": "Because you rejoiced, because you exulted, O you who plundered my inheritance, because you pranced like a heifer in the grass and neighed like stallions —",
      "M": "Because you rejoiced and exulted, you plunderers of my inheritance — because you gamboled like a heifer on grass and bellowed like bulls —",
      "T": "You plundered my inheritance and celebrated. You frolicked like a well-fed calf on fresh grass and roared like bulls in their prime —"
    },
    "12": {
      "L": "your mother shall be utterly ashamed; she who bore you shall be disgraced. Behold, she shall be the last among the nations — a wilderness, a dry land, a desert.",
      "M": "your mother will be utterly ashamed; the one who bore you will be disgraced. She will become the least of the nations — a wilderness, a dry land, a barren desert.",
      "T": "— your mother is ashamed. The nation that bore you will be humiliated. She will end up the most despised among all nations — a wilderness, a parched land, a desert."
    },
    "13": {
      "L": "Because of the wrath of the LORD she shall not be inhabited but shall be wholly desolate; everyone who passes by Babylon shall be appalled and hiss because of all her disasters.",
      "M": "Because of the LORD's wrath she will not be inhabited, but will be completely desolate; everyone who passes by Babylon will be appalled and hiss at all her disasters.",
      "T": "Babylon will be uninhabited — Yahweh's fury will make sure of that — completely desolate. Everyone who passes through will recoil and hiss at everything that has struck her."
    },
    "14": {
      "L": "Set yourselves in array against Babylon all around, all you who bend the bow; shoot at her; spare no arrows, for she has sinned against the LORD.",
      "M": "Deploy yourselves against Babylon from every side, all you who draw the bow; shoot at her; do not spare your arrows, for she has sinned against the LORD.",
      "T": "Take your positions around Babylon — every archer in place — and shoot! Don't hold back a single arrow, for she has sinned against Yahweh."
    },
    "15": {
      "L": "Shout against her all around! She has surrendered; her bastions have fallen; her walls are thrown down. For this is the vengeance of the LORD: take vengeance on her; do to her as she has done.",
      "M": "Shout against her from every side! She has surrendered; her towers have fallen; her walls are thrown down. For this is the LORD's vengeance: take vengeance on her; do to her as she has done.",
      "T": "Raise the battle shout against her on every side! She has surrendered. Her defenses have crumbled; her walls have been torn down. This is Yahweh's vengeance — take it. Give her exactly what she gave everyone else."
    },
    "16": {
      "L": "Cut off the sower from Babylon, and the one who handles the sickle at harvest time; before the sword of the oppressor every one shall turn to his own people, and every one shall flee to his own land.",
      "M": "Cut off the sower from Babylon and the one who wields the sickle at harvest time; before the sword of the oppressor, everyone will turn to their own people and flee to their own land.",
      "T": "Cut off every sower from Babylon, every harvester who swings the sickle at reaping time — before the oppressor's sword, every foreigner will break and run for home."
    },
    "17": {
      "L": "Israel is a scattered sheep; the lions have driven him away. First the king of Assyria devoured him, and then at last Nebuchadrezzar king of Babylon has gnawed his bones.",
      "M": "Israel is a scattered sheep; lions have driven it away. First the king of Assyria devoured it, and last this Nebuchadrezzar king of Babylon has broken its bones.",
      "T": "Israel is a scattered flock — lions have been driving it apart. First it was the king of Assyria who devoured them; and last of all came Nebuchadrezzar king of Babylon and crushed their bones."
    },
    "18": {
      "L": "Therefore thus says the LORD of hosts, the God of Israel: Behold, I am about to punish the king of Babylon and his land, as I punished the king of Assyria.",
      "M": "Therefore thus says the LORD of hosts, the God of Israel: I am going to punish the king of Babylon and his land, just as I punished the king of Assyria.",
      "T": "Therefore Yahweh of hosts, the God of Israel, says this: I am going to punish the king of Babylon and his land, just as I punished the king of Assyria."
    },
    "19": {
      "L": "And I will restore Israel to his pasture, and he shall graze on Carmel and in Bashan; and his appetite shall be satisfied on the hills of Ephraim and in Gilead.",
      "M": "I will bring Israel back to his pasture, and he shall graze on Carmel and in Bashan; his appetite will be satisfied on the hills of Ephraim and in Gilead.",
      "T": "And I will bring Israel home — back to the pasture that belongs to him. He will graze on Carmel and Bashan; he will eat his fill on the hills of Ephraim and in Gilead."
    },
    "20": {
      "L": "In those days and at that time, declares the LORD, the iniquity of Israel shall be sought and there shall be none, and the sins of Judah — they shall not be found, for I will pardon those whom I leave as a remnant.",
      "M": "In those days and at that time, declares the LORD, the iniquity of Israel will be searched for, but there will be none; and the sins of Judah will not be found, for I will pardon those whom I spare.",
      "T": "In those days and at that time — Yahweh declares it — someone will search for Israel's iniquity and find nothing. Someone will look for Judah's sins and they will not exist. For I will forgive everyone I have preserved."
    },
    "21": {
      "L": "Go up against the land of Merathaim, and against the inhabitants of Pekod. Slay and devote them to destruction, declares the LORD, and do all that I have commanded you.",
      "M": "Go up against the land of Merathaim and against the inhabitants of Pekod. Strike them down and completely destroy them, declares the LORD, and carry out everything I have commanded you.",
      "T": "March against the land of Merathaim and against the people of Pekod. Cut them down and devote every last thing to destruction — Yahweh declares it — carry out every order I have given."
    },
    "22": {
      "L": "A sound of battle is in the land, and great destruction!",
      "M": "The sound of battle is in the land, and a great destruction!",
      "T": "The battle is raging across the land — destruction on a massive scale!"
    },
    "23": {
      "L": "How the hammer of the whole earth is cut down and broken! How Babylon has become a horror among the nations!",
      "M": "How the hammer of the whole earth has been cut in pieces and broken! How Babylon has become a desolation among the nations!",
      "T": "The hammer of the whole earth — shattered and broken to pieces! How has Babylon become a horror among the nations?"
    },
    "24": {
      "L": "I set a snare for you and you were caught, O Babylon, before you knew it; you were found and seized, for you contended against the LORD.",
      "M": "I laid a snare for you and you were caught, O Babylon, before you knew it; you were found and taken, because you strove against the LORD.",
      "T": "I set a trap for you and you fell in, Babylon — you never even knew it was there. You were caught and seized. That is what you get for going to war against Yahweh."
    },
    "25": {
      "L": "The LORD has opened his armory and brought out the weapons of his wrath, for the Lord GOD of hosts has a work to do in the land of the Chaldeans.",
      "M": "The LORD has opened his armory and brought out the weapons of his anger, for the Lord GOD of hosts has a task to accomplish in the land of the Chaldeans.",
      "T": "Yahweh has thrown open his armory and brought out the weapons of his fury — because the Lord Yahweh of hosts has a task to complete in the land of the Chaldeans."
    },
    "26": {
      "L": "Come against her from the farthest border; open her granaries; pile her up like heaps of grain and devote her to destruction; let nothing of her be left.",
      "M": "Attack her from every end; throw open her granaries; pile her up like heaps and utterly destroy her; let nothing of her remain.",
      "T": "Come against her from the outermost edge! Break open her storehouses! Heap her up and wipe out every last bit — leave absolutely nothing!"
    },
    "27": {
      "L": "Strike down all her bulls; let them go down to the slaughter. Woe to them, for their day has come, the time of their punishment.",
      "M": "Slaughter all her bulls; let them go down to the killing. Woe to them, for their day has come, the time of their reckoning.",
      "T": "Cut down every last one of her bulls — drive them down to slaughter! Woe to them — their day has arrived, the hour of their final accounting!"
    },
    "28": {
      "L": "The voice of those who flee and escape from the land of Babylon, declaring in Zion the vengeance of the LORD our God, the vengeance for his temple.",
      "M": "Hear the voice of those who flee and escape from the land of Babylon — they are declaring in Zion the vengeance of the LORD our God, the vengeance for his temple.",
      "T": "Listen — the sound of the fugitives, the people escaping from Babylon, making their way to Zion to announce Yahweh our God's vengeance: his vengeance for his temple."
    },
    "29": {
      "L": "Summon archers against Babylon, all those who draw the bow! Encamp around her; let no one escape. Repay her according to her deeds; do to her just as she has done. For she has shown arrogance against the LORD, against the Holy One of Israel.",
      "M": "Call up the archers against Babylon, all who draw the bow! Encamp around her; let none escape. Give her what she deserves; do to her as she has done. For she has acted with pride against the LORD, against the Holy One of Israel.",
      "T": "Summon every archer against Babylon — every bowstring drawn! Surround her completely; no one escapes. Pay her back in full for everything she has done. She has been arrogant against Yahweh himself — against the Holy One of Israel."
    },
    "30": {
      "L": "Therefore her young men shall fall in her streets, and all her warriors shall be silenced in that day, declares the LORD.",
      "M": "Therefore her young men shall fall in the streets, and all her soldiers will be struck down on that day, declares the LORD.",
      "T": "That is why her young men will fall in the streets and all her soldiers will be silenced on that day. Yahweh declares it."
    },
    "31": {
      "L": "Behold, I am against you, O most arrogant, declares the Lord GOD of hosts, for your day has come, the time when I will punish you.",
      "M": "Behold, I am against you, O most arrogant, declares the Lord GOD of hosts; for your day has come, the time when I will punish you.",
      "T": "I am against you — you who are the most arrogant of all — the Lord Yahweh of hosts declares it. Your day has arrived; the moment of your reckoning has come."
    },
    "32": {
      "L": "And the most arrogant shall stumble and fall, with no one to raise him up; and I will kindle a fire in his cities, and it will devour all his surroundings.",
      "M": "The most arrogant shall stumble and fall, with no one to raise him up; I will set fire to his cities, and it will consume everything around him.",
      "T": "The most arrogant one will stumble and fall — and no one will be there to help him up. I will set his cities ablaze, and the fire will devour everything around him."
    },
    "33": {
      "L": "Thus says the LORD of hosts: The people of Israel are oppressed, and the people of Judah with them; all who took them captive have held them fast; they have refused to let them go.",
      "M": "Thus says the LORD of hosts: The people of Israel are oppressed, and the people of Judah with them; all their captors have held them fast and refuse to release them.",
      "T": "Yahweh of hosts says this: The people of Israel are oppressed, and so are the people of Judah — held tight in the grip of every one of their captors, who refuse to let them go."
    },
    "34": {
      "L": "Their Redeemer is strong; the LORD of hosts is his name. He will surely plead their cause, that he may give rest to the earth but unrest to the inhabitants of Babylon.",
      "M": "Their Redeemer is mighty; the LORD of hosts is his name. He will certainly plead their cause, giving rest to the land but unrest to the inhabitants of Babylon.",
      "T": "But their Redeemer is powerful — Yahweh of hosts is his name. He will argue their case with full force. He will bring rest to the land — but turmoil without end to the people of Babylon."
    },
    "35": {
      "L": "A sword against the Chaldeans, declares the LORD, and against the inhabitants of Babylon — against her officials and her wise men!",
      "M": "A sword against the Chaldeans, declares the LORD, and against the inhabitants of Babylon — against her officials and her wise men!",
      "T": "The sword is drawn against the Chaldeans — Yahweh declares it — against the people of Babylon, against her officials and her wise counselors!"
    },
    "36": {
      "L": "A sword against her liars — that they may become fools! A sword against her warriors — that they may be dismayed!",
      "M": "A sword against her false prophets, so that they become fools! A sword against her warriors, so that they become terrified!",
      "T": "The sword comes for her court diviners — they will rave like madmen! The sword for her warriors — they will collapse in terror!"
    },
    "37": {
      "L": "A sword against her horses and against her chariots, and against all the mixed people in her midst — that they may become like women! A sword against her treasures — that they may be plundered!",
      "M": "A sword against her horses and chariots, against all the foreign troops in her midst — that they become as weak as women! A sword against her treasures — and they will be plundered!",
      "T": "The sword against her horses, against her chariots, against every mercenary in her ranks — they will lose every drop of their fighting spirit! The sword against her treasuries — they will be looted!"
    },
    "38": {
      "L": "A drought against her waters — that they may dry up! For it is a land of idols, and they are mad over their images.",
      "M": "A drought upon her waters, and they shall dry up! For it is a land of idols, and they are driven mad by their images.",
      "T": "Drought on her waters — let them be drained dry! For this is a land of idols, and her idols have driven its people out of their minds."
    },
    "39": {
      "L": "Therefore wild beasts of the desert shall dwell with jackals, and ostriches shall inhabit her; she shall never again be inhabited or lived in from generation to generation.",
      "M": "Therefore wild desert creatures and jackals shall inhabit her, and ostriches shall live there; she shall never again be inhabited or dwelt in from generation to generation.",
      "T": "Wild desert animals will nest in Babylon alongside jackals; ostriches will make their home there. It will never be inhabited again — never, for generation after generation."
    },
    "40": {
      "L": "As when God overthrew Sodom and Gomorrah and their neighboring cities, declares the LORD, no one shall dwell there, and no son of man shall sojourn there.",
      "M": "As when God overthrew Sodom and Gomorrah and their neighboring towns, declares the LORD, no one shall dwell there, and no human being shall settle there.",
      "T": "Just as God overthrew Sodom and Gomorrah and the towns around them — Yahweh declares it — no one will ever live in Babylon again. Not ever."
    },
    "41": {
      "L": "Behold, a people comes from the north, a great nation, and many kings shall be stirred up from the far parts of the earth.",
      "M": "Behold, a people is coming from the north — a great nation and many kings roused up from the ends of the earth.",
      "T": "Look — a people is coming from the north: a great nation and many kings, roused from the farthest corners of the earth."
    },
    "42": {
      "L": "They grip bow and spear; they are cruel and show no mercy. Their voice roars like the sea; they ride on horses, arrayed as one man for battle against you, O daughter of Babylon.",
      "M": "They hold bow and spear; they are cruel, showing no mercy. Their voices roar like the sea; they ride on horses, all arrayed for battle against you, O daughter of Babylon.",
      "T": "They grip their bows and their spears — cruel soldiers without a trace of mercy. Their voices thunder like the sea. They come mounted on horses, every one in battle formation — against you, daughter of Babylon."
    },
    "43": {
      "L": "The king of Babylon heard the news of them, and his hands fell limp; anguish seized him — pangs like a woman in labor.",
      "M": "The king of Babylon heard the report about them, and his hands went limp; anguish seized him — torment like a woman in labor.",
      "T": "When the king of Babylon heard the reports about them, his hands fell limp. Anguish gripped him — writhing like a woman in the throes of labor."
    },
    "44": {
      "L": "Behold, like a lion coming up from the thickets of the Jordan against the strong pasture, I will suddenly make them run from her; and I will appoint over her whomever I choose. For who is like me? Who will summon me? What shepherd can stand before me?",
      "M": "Behold, like a lion coming up from the thickets of the Jordan against the strong meadow, I will suddenly drive them from her and appoint over her whomever I choose. For who is like me? Who can challenge me? What shepherd can stand against me?",
      "T": "A lion rises from the tangled undergrowth of the Jordan valley and surges toward rich pastureland — and just as suddenly I will drive Babylon's rulers off. I will appoint whoever I choose to rule over her. For who is my equal? Who could call me to account? What shepherd could face me and live?"
    },
    "45": {
      "L": "Therefore hear the plan that the LORD has formed against Babylon and the purposes that he has purposed against the land of the Chaldeans: Surely the little ones of the flock shall be dragged away; surely he shall make their pasture desolate over them.",
      "M": "Therefore hear the strategy the LORD has formed against Babylon and his purposes against the land of the Chaldeans: Surely even the weakest of the flock will be dragged away; surely he will make their pasture a desolation.",
      "T": "So hear the strategy Yahweh has formed against Babylon — the purposes he has shaped against the land of the Chaldeans: Even the weakest lamb will be dragged off, and their very pastures will be turned into wasteland around them."
    },
    "46": {
      "L": "At the sound of Babylon's capture the earth quakes; a cry is heard among the nations.",
      "M": "At the sound of Babylon's capture the earth will quake; and the cry will be heard among the nations.",
      "T": "At the noise of Babylon's fall, the earth itself will shake. Her cry will echo among all the nations."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 49–50 written.')

if __name__ == '__main__':
    main()
