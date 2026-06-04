"""
MKT Jeremiah chapters 37–39 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-37-39.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-28-30.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name force is
  significant — oracle delivery, divine address, and oath contexts. Narrative connector
  formulas ("declares the LORD") use "Yahweh" in T for immediacy.

- H6635 (צְבָאוֹת, ṣĕbāʾôt, "hosts/armies"): "hosts" in L/M; retained in T. Appears in
  38:17 only — Yahweh as divine military commander frames the surrender oracle sharply.

- H5315 (נֶפֶשׁ, nepeš, "soul/life/person"): In 38:2,16,17,20 and 39:18, the idiom
  "his nepeš shall be spoil/plunder" (נַפְשׁוֹ לְשָׁלָל) is a survival formula: "he will
  escape with his life." L preserves the literal "his life shall be his plunder"; M/T
  render the idiom naturally as "he will escape with his life / come away alive."

- H7503 (רָפָה, rāpâ, "weaken/slacken"): 38:4 — "weakening the hands of the warriors."
  Hebrew idiom for sapping morale and courage. L: "weakening the hands"; M: "demoralizing";
  T: "cutting the nerve of courage" — surfaces the honor-shame dimension: the charge is that
  Jeremiah is publicly dissolving the will to resist.

- H4428 (מֶלֶךְ, melek): standard "king" throughout. Where "king of Babylon" recurs, L/M
  keep full title; T abbreviates to "Babylon's king" after first use for prose rhythm.

- H4421 (מִלְחָמָה, milḥāmâ, "war/fighting/battle"): rendered "war" or "fight" per context.

- "Ebed-melech" (38:7ff.) — the name means "servant of the king." Not glossed in the text
  but noted here; he is an Ethiopian court official (eunuch/officer) who saves Jeremiah and
  receives his own salvation oracle (39:15-18) as reward for trusting Yahweh.

- "Weakening the hands" (38:4): retained in L as a Hebraism; smoothed in M/T to convey
  the demoralizing, courage-sapping effect on troops and civilians alike.

- "Your life shall be your plunder" (38:2; 39:18): the idiom נַפְשׁ לְשָׁלָל pictures survival
  as capturing the most prized booty from a battle — your own life. L preserves the literal
  form; M renders idiomatically; T surfaces the paradox — to live through this is itself the
  prize.

- 37:12 — "to receive his share/portion among the people" (לַחֲלֹק מִשָּׁם): Jeremiah was
  going to participate in a property division or inheritance transaction in Benjamin. This
  detail matters: he was not fleeing but conducting legal family business — which makes his
  arrest as a defector all the more unjust.

- 39:3 — The list of Babylonian officials is textually uncertain (names appear to be in
  disarray in the MT, with "Nergalsharezer Samgarnebo" likely a dittography or corruption).
  L preserves the MT form; M/T note them as "the senior commanders of Babylon" without
  forcing a smooth list that may misrepresent the text.

- 39:9 — "those who remained" (הַנֹּתָרִים, "the remainder"): the people who had survived
  the siege but not surrendered. Rendered "the survivors" in L/M; T: "all who remained."

- 39:18 — "because you trusted in me" (בָּטַחְתָּ בִּי): H982 (בָּטַח, bāṭaḥ) = confidence,
  reliance, trust that rests full weight on something. This is the same word as Psalm 22:4-5.
  Rendered "trusted in me" in L/M; T: "put your whole trust in me" — warranted by the
  emphatic personal pronoun.

Structural and textual notes:

- Ch. 37 — Jeremiah imprisoned during the siege lull (after 588 BCE).
  The narrative pivots on irony: the one moment the Babylonians withdraw, Jeremiah attempts
  to leave — not to defect, but on family business. The arrest collapses public and private
  motives. The royal request for prayer (vv. 3-4) shows Zedekiah's desperate ambiguity:
  he wants divine help but will not act on divine instruction.

- Ch. 37:17 — Zedekiah's secret consultation is the pivot scene: the king knows Jeremiah
  speaks truth, but his fear of the court will not let him act on it. The single-word answer
  "There is" (יֵשׁ) is devastating — followed immediately by the verdict: you go to Babylon.

- Ch. 38 — Jeremiah in the cistern; Ebed-melech as counter-figure.
  The officials' charge (v.4) frames Jeremiah's ministry in political/military terms:
  "weakening the hands" is the language of treason. The king's abdication ("he is in your
  hands; the king can do nothing against you") shows a monarch trapped between court
  factions and divine word. Ebed-melech — a foreign courtier — acts where the Israelite
  king cannot, embodying the prophetic principle that outsiders often see what insiders refuse.

- Ch. 38:22 — The women's lament taunt is a prophecy: if Zedekiah refuses to surrender,
  the women of the palace will taunt him as they are led away — "your trusted friends have
  set you in the mire and abandoned you." The word-picture (שָׁקַע בַּבֹּץ, sinking in mud)
  echoes Jeremiah's own recent experience in the cistern. The irony is deliberate.

- Ch. 39 — The fall of Jerusalem (586 BCE).
  The chapter is economical: no lament, no extended reflection, just the narrated events.
  Zedekiah's flight and capture (vv. 4-7) are reported as simple sequence. The blinding is
  the final horror: the last thing Zedekiah sees is the execution of his sons. Then darkness.
  This fulfills Ezekiel's double prophecy: Zedekiah would "go to Babylon" (Ezek 12:13) yet
  "not see Babylon" (Ezek 12:13). He arrives there blind.

- Ch. 39:10 — The survival of the poor is not incidental. Nebuchadnezzar's land redistribution
  to the Judean poor mirrors the land theology of the prophets (Isa 61; Jer 32): exile strips
  the landed aristocracy; the poor inherit the land. Provisional, incomplete — but a sign.

- Ch. 39:15-18 — The Ebed-melech oracle (inserted in a flashback to ch. 38's timeframe)
  closes the unit with a personal salvation: the foreign servant who risked his position
  to save Jeremiah now receives Jeremiah's blessing. His life will be "his plunder" —
  the same idiom of 38:2. Trust in Yahweh produces exactly the outcome Jeremiah promised
  the surrendering soldier.

OT intertextuality:
- 37:9 — "Do not deceive yourselves" echoes the anti-false-prophet formula of 29:8-9.
- 38:4 — "weakening the hands" echoes Ezra 4:4; Neh 6:9 (enemies using the same tactic).
- 38:22 — "sunk in the mud" (בֹּץ) echoes Ps 69:2,14 — the psalmist's cistern/mud imagery.
- 39:9 — "remnant of the people" echoes Jer 15:9; Ezek 5:10 (the scattered remnant theme).
- 39:18 — "escape with your life" / "trust in me" echoes Ps 22:4-5; Jer 17:7-8.
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
  "37": {
    "1": {
      "L": "And Zedekiah the son of Josiah was made king instead of Coniah the son of Jehoiakim, whom Nebuchadnezzar king of Babylon had made king in the land of Judah.",
      "M": "Zedekiah son of Josiah was made king in place of Coniah son of Jehoiakim, whom Nebuchadnezzar king of Babylon had appointed to rule over the land of Judah.",
      "T": "Zedekiah son of Josiah was installed as king in place of Coniah son of Jehoiakim — installed by Nebuchadnezzar, king of Babylon, over the land of Judah."
    },
    "2": {
      "L": "But neither he nor his servants nor the people of the land listened to the words of the LORD which he spoke through the prophet Jeremiah.",
      "M": "But he, his servants, and the people of the land refused to listen to the words of the LORD that he spoke through the prophet Jeremiah.",
      "T": "But Zedekiah, his court, and the people of the land all refused to hear the words Yahweh was speaking through Jeremiah the prophet."
    },
    "3": {
      "L": "And Zedekiah the king sent Jehucal the son of Shelemiah and Zephaniah the son of Maaseiah the priest to the prophet Jeremiah, saying: Pray now to the LORD our God on our behalf.",
      "M": "King Zedekiah sent Jehucal son of Shelemiah and the priest Zephaniah son of Maaseiah to the prophet Jeremiah with this message: Please pray to the LORD our God on our behalf.",
      "T": "King Zedekiah sent Jehucal son of Shelemiah and Zephaniah the priest son of Maaseiah to Jeremiah with one request: Pray to Yahweh our God for us."
    },
    "4": {
      "L": "Now Jeremiah was coming in and going out among the people, for they had not yet put him in prison.",
      "M": "At this time Jeremiah was still moving freely among the people, for he had not yet been imprisoned.",
      "T": "At this point Jeremiah still came and went freely among the people — no one had yet put him under arrest."
    },
    "5": {
      "L": "And Pharaoh's army had come out from Egypt; and when the Chaldeans who were besieging Jerusalem heard news of them, they withdrew from Jerusalem.",
      "M": "Meanwhile Pharaoh's army had marched out from Egypt. When the Chaldeans besieging Jerusalem heard the report about them, they pulled back from the city.",
      "T": "At that time Pharaoh's army had marched up from Egypt. When the Chaldean forces besieging Jerusalem got word of it, they lifted the siege and withdrew."
    },
    "6": {
      "L": "Then the word of the LORD came to the prophet Jeremiah, saying:",
      "M": "Then the word of the LORD came to the prophet Jeremiah:",
      "T": "Then Yahweh's word came to Jeremiah the prophet:"
    },
    "7": {
      "L": "Thus says the LORD, the God of Israel: This is what you shall say to the king of Judah, who sent you to me to inquire of me: Behold, Pharaoh's army which has set out to help you will return to its own land, to Egypt.",
      "M": "Thus says the LORD, the God of Israel: Say to the king of Judah who sent you to inquire of me: Pharaoh's army, which came out to help you, is going to turn back to its own land — to Egypt.",
      "T": "This is what Yahweh, the God of Israel, says: Tell the king of Judah who sent you to ask me — Pharaoh's army that came out to rescue you is going to turn around and go home to Egypt."
    },
    "8": {
      "L": "And the Chaldeans shall come back and fight against this city; they shall capture it and burn it with fire.",
      "M": "And the Chaldeans will return and attack this city; they will capture it and burn it with fire.",
      "T": "And the Chaldeans will come back. They will attack this city, take it, and burn it to the ground."
    },
    "9": {
      "L": "Thus says the LORD: Do not deceive yourselves, saying, The Chaldeans will surely leave us; for they will not leave.",
      "M": "Thus says the LORD: Do not deceive yourselves by saying, 'The Chaldeans will certainly leave us,' for they will not leave.",
      "T": "This is what Yahweh says: Stop lying to yourselves — 'The Chaldeans are definitely leaving us.' They are not leaving."
    },
    "10": {
      "L": "For even if you had struck down the whole army of Chaldeans that fight against you, and only wounded men remained among them, every man in his tent, they would rise up and burn this city with fire.",
      "M": "For even if you had defeated the entire Chaldean army fighting against you, and only the wounded were left — every man lying in his tent — they would still rise up and burn this city with fire.",
      "T": "Even if you managed to cut down the entire Chaldean army and nothing was left but wounded men lying in their tents — those wounded men would drag themselves up and burn this city down."
    },
    "11": {
      "L": "And it came to pass, when the army of the Chaldeans had withdrawn from Jerusalem because of Pharaoh's army,",
      "M": "When the Chaldean army withdrew from Jerusalem because of Pharaoh's army,",
      "T": "When the Chaldean army pulled back from Jerusalem because of Pharaoh's advance,"
    },
    "12": {
      "L": "that Jeremiah went out from Jerusalem to go to the land of Benjamin to receive his portion there in the midst of the people.",
      "M": "Jeremiah set out from Jerusalem to travel to the territory of Benjamin to receive his share of a property division among the people there.",
      "T": "Jeremiah left Jerusalem and headed for the territory of Benjamin to take part in a property transaction among his family."
    },
    "13": {
      "L": "When he was at the Gate of Benjamin, a sentinel there named Irijah the son of Shelemiah, the son of Hananiah, arrested the prophet Jeremiah, saying: You are deserting to the Chaldeans.",
      "M": "When he reached the Benjamin Gate, a sentinel named Irijah son of Shelemiah son of Hananiah arrested the prophet Jeremiah and accused him: You are defecting to the Chaldeans.",
      "T": "At the Benjamin Gate, a sentry named Irijah son of Shelemiah son of Hananiah seized Jeremiah and charged him: You are going over to the Chaldeans."
    },
    "14": {
      "L": "And Jeremiah said: It is a lie! I am not deserting to the Chaldeans. But Irijah did not listen to him; so Irijah arrested Jeremiah and brought him to the officials.",
      "M": "Jeremiah replied: That is not true! I am not defecting to the Chaldeans. But Irijah refused to listen, arrested him, and brought him to the officials.",
      "T": "Jeremiah said: That is a lie — I am not going to the Chaldeans. But Irijah would not hear it. He arrested Jeremiah and handed him over to the court officials."
    },
    "15": {
      "L": "And the officials were angry at Jeremiah, and they beat him and put him in prison in the house of Jonathan the scribe, for it had been made into a prison.",
      "M": "The officials were furious with Jeremiah. They had him beaten and imprisoned in the house of Jonathan the scribe, which had been converted into a prison.",
      "T": "The officials were enraged. They had Jeremiah beaten and thrown into the house of Jonathan the scribe, which had been turned into a jail."
    },
    "16": {
      "L": "For when Jeremiah had entered the vaulted cell and remained there many days,",
      "M": "After Jeremiah had been put in the vaulted dungeon cell and had remained there for many days,",
      "T": "After Jeremiah had been dropped into the vaulted dungeon and had been there for days on end,"
    },
    "17": {
      "L": "Zedekiah the king sent and took him. And the king questioned him secretly in his house and said: Is there any word from the LORD? Jeremiah said: There is. And he said: You will be given into the hand of the king of Babylon.",
      "M": "King Zedekiah sent for him and had him brought to his house. The king questioned him privately: Is there any word from the LORD? Jeremiah said: There is. Then he said: You will be handed over to the king of Babylon.",
      "T": "King Zedekiah sent for him and had him brought to the palace. Privately, behind closed doors, the king asked: Is there any word from Yahweh? Jeremiah said: There is. And then: You will be handed over to Babylon's king."
    },
    "18": {
      "L": "And Jeremiah said to King Zedekiah: What wrong have I done to you or your servants or this people, that you have put me in prison?",
      "M": "Jeremiah also said to King Zedekiah: What wrong have I done to you, your servants, or this people, that you have put me in prison?",
      "T": "Jeremiah also pressed the king: What have I actually done to you, to your court, or to this people, that you have imprisoned me?"
    },
    "19": {
      "L": "And where are your prophets who prophesied to you, saying: The king of Babylon will not come against you and against this land?",
      "M": "And where are your prophets who prophesied to you, 'The king of Babylon will not attack you or this land'?",
      "T": "Where are those prophets of yours who promised you: 'Babylon's king will not come against you or this land'? Where are they now?"
    },
    "20": {
      "L": "But now hear me, please, my lord the king; let my plea come before you, and do not send me back to the house of Jonathan the scribe, lest I die there.",
      "M": "Please, my lord the king — hear me now: let my plea be accepted. Do not send me back to the house of Jonathan the scribe, or I will die there.",
      "T": "But now — my lord the king — please listen to me. One request: do not send me back to the house of Jonathan the scribe. I will die there."
    },
    "21": {
      "L": "Then King Zedekiah commanded, and they put Jeremiah in the court of the guard. And they gave him a loaf of bread daily from the bakers' street until all the bread in the city was gone. And Jeremiah remained in the court of the guard.",
      "M": "So King Zedekiah gave the order, and Jeremiah was transferred to the court of the guard. He was given a loaf of bread daily from the bakers' street for as long as there was bread in the city. And Jeremiah remained in the court of the guard.",
      "T": "Zedekiah gave the order, and Jeremiah was moved to the court of the guard — a measure of mercy. He received a daily ration of bread from the bakers' quarter for as long as the city's bread supply lasted. And there Jeremiah stayed."
    }
  },
  "38": {
    "1": {
      "L": "Now Shephatiah the son of Mattan, and Gedaliah the son of Pashhur, and Jucal the son of Shelemiah, and Pashhur the son of Malchiah heard the words that Jeremiah was speaking to all the people, saying:",
      "M": "Shephatiah son of Mattan, Gedaliah son of Pashhur, Jucal son of Shelemiah, and Pashhur son of Malchiah heard the words that Jeremiah was speaking to all the people:",
      "T": "Four of the king's officials — Shephatiah son of Mattan, Gedaliah son of Pashhur, Jucal son of Shelemiah, and Pashhur son of Malchiah — heard what Jeremiah was telling the people:"
    },
    "2": {
      "L": "Thus says the LORD: He who stays in this city shall die by sword, by famine, and by pestilence. But he who goes out to the Chaldeans shall live; his life shall be his plunder, and he shall live.",
      "M": "Thus says the LORD: Whoever stays in this city will die by sword, famine, or pestilence. But whoever goes out to the Chaldeans will live; he will escape with his life.",
      "T": "This is what Yahweh says: Whoever stays in this city will die — by sword, starvation, or plague. Whoever goes out and surrenders to the Chaldeans will live. His life will be his prize. He will survive."
    },
    "3": {
      "L": "Thus says the LORD: This city shall surely be given into the hand of the army of the king of Babylon, and it shall be taken.",
      "M": "Thus says the LORD: This city will certainly be handed over to the army of the king of Babylon, and it will be taken.",
      "T": "This is what Yahweh says: This city will absolutely be handed over to Babylon's army. It will fall."
    },
    "4": {
      "L": "And the officials said to the king: Let this man be put to death, for he is weakening the hands of the warriors who are left in this city, and the hands of all the people, by speaking such words to them. For this man is not seeking the welfare of this people, but their harm.",
      "M": "The officials said to the king: This man must be put to death. He is demoralizing the soldiers who remain in this city and all the people by speaking these words to them. This man is not seeking the welfare of this people, but their ruin.",
      "T": "The officials told the king: This man must die. He is cutting the nerve of courage in every soldier left in this city, and in the whole population, by saying what he says. He is not working for the good of this people — he is working for their destruction."
    },
    "5": {
      "L": "Then King Zedekiah said: Behold, he is in your hands; for the king can do nothing against you.",
      "M": "King Zedekiah replied: He is in your hands, for the king can do nothing against you.",
      "T": "King Zedekiah replied: He is in your hands. There is nothing the king can do to stop you."
    },
    "6": {
      "L": "So they took Jeremiah and threw him into the cistern of Malchiah the king's son, which was in the court of the guard, letting him down by ropes. Now there was no water in the cistern, only mud, and Jeremiah sank into the mud.",
      "M": "So they took Jeremiah and threw him into the cistern of Malchiah the king's son, which was in the court of the guard. They lowered him down with ropes. There was no water in the cistern, only mud, and Jeremiah sank into the mud.",
      "T": "So they took Jeremiah and lowered him by ropes into the cistern of Malchiah the king's son, which stood in the court of the guard. There was no water in the cistern — only mud. Jeremiah sank down into it."
    },
    "7": {
      "L": "Now Ebed-melech the Ethiopian, a eunuch who was in the king's house, heard that they had put Jeremiah into the cistern. The king was sitting at the Benjamin Gate at the time.",
      "M": "But Ebed-melech the Ethiopian, a court official in the king's palace, heard that they had thrown Jeremiah into the cistern. The king was sitting at the Benjamin Gate at the time.",
      "T": "But Ebed-melech, an Ethiopian who served in the royal palace, heard that they had thrown Jeremiah into the cistern. At that moment the king was sitting in session at the Benjamin Gate."
    },
    "8": {
      "L": "Ebed-melech went out of the king's house and spoke to the king, saying:",
      "M": "Ebed-melech left the king's house and went to speak to the king:",
      "T": "Ebed-melech left the palace and went straight to the king and said:"
    },
    "9": {
      "L": "My lord the king, these men have done evil in all that they have done to Jeremiah the prophet by throwing him into the cistern, and he will die there from hunger, since there is no bread left in the city.",
      "M": "My lord the king, these men have done wrong in everything they did to Jeremiah the prophet by throwing him into the cistern. He is going to die of hunger there, for there is no more bread left in the city.",
      "T": "My lord the king — what these men have done to Jeremiah the prophet is wicked. They threw him into a cistern. He is going to die of starvation down there, because the city has run out of bread."
    },
    "10": {
      "L": "Then the king commanded Ebed-melech the Ethiopian: Take thirty men with you from here and bring up Jeremiah the prophet from the cistern before he dies.",
      "M": "Then the king commanded Ebed-melech the Ethiopian: Take thirty men with you and pull Jeremiah the prophet out of the cistern before he dies.",
      "T": "The king gave the order to Ebed-melech: Take thirty men with you and get Jeremiah out of that cistern before he dies."
    },
    "11": {
      "L": "So Ebed-melech took the men with him and went to the house of the king, to a place under the treasury, and took from there old rags and worn-out garments, and let them down to Jeremiah in the cistern by ropes.",
      "M": "So Ebed-melech took the men with him and went into the king's house, to the storeroom under the treasury. He collected some old rags and worn garments and lowered them by ropes to Jeremiah in the cistern.",
      "T": "Ebed-melech took the men and went to a storeroom under the palace treasury. He gathered old rags and worn-out garments and let them down by ropes to Jeremiah in the cistern."
    },
    "12": {
      "L": "And Ebed-melech the Ethiopian said to Jeremiah: Place these old rags and worn garments under your armpits under the ropes. And Jeremiah did so.",
      "M": "Ebed-melech the Ethiopian called down to Jeremiah: Put these old rags and worn garments under your armpits where the ropes will go. And Jeremiah did as he was told.",
      "T": "Ebed-melech called down to Jeremiah: Pad your armpits with these rags and worn cloth before the ropes go under them. Jeremiah did it."
    },
    "13": {
      "L": "Then they drew Jeremiah up with the ropes and pulled him out of the cistern. And Jeremiah remained in the court of the guard.",
      "M": "They pulled Jeremiah up with the ropes and lifted him out of the cistern. And Jeremiah remained in the court of the guard.",
      "T": "They hauled Jeremiah up out of the cistern. He remained in the court of the guard."
    },
    "14": {
      "L": "Then King Zedekiah sent and had Jeremiah the prophet brought to him at the third entrance of the temple of the LORD. And the king said to Jeremiah: I am going to ask you something; do not hide anything from me.",
      "M": "King Zedekiah summoned Jeremiah the prophet and received him at the third entrance of the LORD's temple. The king said to Jeremiah: I am going to ask you something — hide nothing from me.",
      "T": "King Zedekiah sent for Jeremiah and received him at the third entrance to Yahweh's temple. He said: I have a question for you. Hide nothing."
    },
    "15": {
      "L": "Then Jeremiah said to Zedekiah: If I tell you, will you not surely put me to death? And if I give you counsel, you will not listen to me.",
      "M": "Jeremiah said to Zedekiah: If I tell you, you will certainly put me to death. And if I give you counsel, you will not take it.",
      "T": "Jeremiah answered: If I tell you the truth, you will have me killed. And if I give you counsel, you will not follow it."
    },
    "16": {
      "L": "Then King Zedekiah swore secretly to Jeremiah, saying: As the LORD lives, who made our very lives, I will not put you to death, nor will I hand you over to these men who are seeking your life.",
      "M": "Then King Zedekiah swore to Jeremiah in secret: As the LORD lives, who gave us the breath of life, I will not kill you and I will not hand you over to these men who want you dead.",
      "T": "So King Zedekiah swore to him in private: As Yahweh lives — the one who breathed this life into us — I will not kill you, and I will not put you in the hands of those who want you dead."
    },
    "17": {
      "L": "Then Jeremiah said to Zedekiah: Thus says the LORD, the God of hosts, the God of Israel: If you will indeed surrender to the officials of the king of Babylon, then your life shall be spared and this city shall not be burned with fire, and you and your house shall live.",
      "M": "Then Jeremiah said to Zedekiah: Thus says the LORD, the God of hosts, the God of Israel: If you will surrender to the officials of the king of Babylon, you will live, this city will not be burned, and you and your household will survive.",
      "T": "Then Jeremiah spoke: This is what Yahweh of hosts, the God of Israel, says: If you go out and surrender to Babylon's officials, you will live. This city will not be burned. You and your household will come through."
    },
    "18": {
      "L": "But if you do not surrender to the officials of the king of Babylon, this city will be given into the hand of the Chaldeans and they will burn it with fire, and you yourself will not escape from their hand.",
      "M": "But if you refuse to surrender to the officials of the king of Babylon, this city will be handed over to the Chaldeans and they will burn it with fire, and you will not escape their grip.",
      "T": "But if you refuse to surrender, this city will be handed to the Chaldeans and they will burn it. You will not get out."
    },
    "19": {
      "L": "And King Zedekiah said to Jeremiah: I am afraid of the Jews who have deserted to the Chaldeans, lest they hand me over to them and they mistreat me.",
      "M": "King Zedekiah said to Jeremiah: I am afraid of the Judeans who have already gone over to the Chaldeans — they might hand me over to them and they will abuse me.",
      "T": "King Zedekiah said: I am terrified of the Judeans who have already defected to the Chaldeans. What if they hand me over to them and they brutalize me?"
    },
    "20": {
      "L": "But Jeremiah said: They will not hand you over. Obey the voice of the LORD in what I am saying to you, and it will go well with you and your life shall be spared.",
      "M": "Jeremiah said: They will not hand you over. Obey the voice of the LORD in what I am telling you, and it will go well with you and you will survive.",
      "T": "Jeremiah said: They will not hand you over. Trust Yahweh's voice — do what I am telling you. It will go well with you. You will come away alive."
    },
    "21": {
      "L": "But if you refuse to surrender, this is the word that the LORD has shown me:",
      "M": "But if you refuse to surrender, this is what the LORD has revealed to me:",
      "T": "But if you refuse, this is what Yahweh has shown me:"
    },
    "22": {
      "L": "Behold, all the women who are left in the house of the king of Judah will be led out to the officials of the king of Babylon, and they will say: Your trusted friends have deceived you and have prevailed against you; your feet are sunk in the mud and they have turned away from you.",
      "M": "All the women remaining in the palace of the king of Judah will be led out to the officials of the king of Babylon, and they will say: Your friends have deceived you and overcome you; your feet are sunk in the mud, and they have turned their backs on you.",
      "T": "Every woman left in the palace of Judah's king will be paraded before Babylon's officials. And they will taunt you: Your closest allies deceived you and got the better of you. Your feet are sunk in the mire — and they have already turned and walked away."
    },
    "23": {
      "L": "All your wives and your children will be led out to the Chaldeans, and you yourself will not escape from their hand, but will be seized by the hand of the king of Babylon, and this city will be burned with fire.",
      "M": "All your wives and children will be brought out to the Chaldeans. You yourself will not escape — you will be captured by the king of Babylon, and this city will be burned with fire.",
      "T": "All your wives, all your children — they will be taken by the Chaldeans. And you will not escape. Babylon's king will have you in his grip, and this city will burn."
    },
    "24": {
      "L": "Then Zedekiah said to Jeremiah: Let no one know of these words and you shall not die.",
      "M": "Then Zedekiah said to Jeremiah: Let no one learn of these words, and you will not die.",
      "T": "Then Zedekiah said to Jeremiah: Tell no one about this conversation, and I will let you live."
    },
    "25": {
      "L": "But if the officials hear that I have spoken with you and they come to you and say: Tell us what you said to the king; do not hide it from us and we will not put you to death — also what the king said to you —",
      "M": "But if the officials hear that I spoke with you and they come and say: Tell us what you said to the king and what the king said to you — hide nothing or we will kill you —",
      "T": "If the officials find out that I talked with you and they come demanding: Tell us what passed between you and the king — every word, nothing held back, or we will kill you —"
    },
    "26": {
      "L": "then you shall say to them: I was presenting my plea before the king, that he would not send me back to the house of Jonathan to die there.",
      "M": "then say to them: I was appealing to the king not to send me back to Jonathan's house to die there.",
      "T": "then you are to say: I was asking the king not to send me back to Jonathan's house, because I would die there."
    },
    "27": {
      "L": "Then all the officials came to Jeremiah and questioned him. And he answered them in accordance with all these words that the king had commanded. So they left off speaking with him, for the conversation had not been heard.",
      "M": "All the officials came to Jeremiah and questioned him. He answered them exactly as the king had instructed, and they stopped pressing him, for no one had overheard the conversation.",
      "T": "Sure enough, all the officials came to Jeremiah and interrogated him. He answered them exactly as the king had told him, and they stopped pushing — no one had heard what was actually said."
    },
    "28": {
      "L": "So Jeremiah remained in the court of the guard until the day Jerusalem was taken. And he was there when Jerusalem was taken.",
      "M": "So Jeremiah remained in the court of the guard until the day Jerusalem was captured. He was still there when Jerusalem was taken.",
      "T": "Jeremiah stayed in the court of the guard until the day Jerusalem fell. He was still there when the city was taken."
    }
  },
  "39": {
    "1": {
      "L": "In the ninth year of Zedekiah king of Judah, in the tenth month, Nebuchadnezzar king of Babylon came with all his army against Jerusalem and besieged it.",
      "M": "In the ninth year of Zedekiah king of Judah, in the tenth month, Nebuchadnezzar king of Babylon came with all his army against Jerusalem and laid siege to it.",
      "T": "In the ninth year of Zedekiah's reign over Judah, in the tenth month, Nebuchadnezzar king of Babylon arrived with his whole army and encircled Jerusalem."
    },
    "2": {
      "L": "And in the eleventh year of Zedekiah, in the fourth month, on the ninth day of the month, a breach was made in the city.",
      "M": "In the eleventh year of Zedekiah, in the fourth month, on the ninth day of the month, the city wall was breached.",
      "T": "In the eleventh year of Zedekiah — the fourth month, the ninth day — the city wall was broken through."
    },
    "3": {
      "L": "Then all the officials of the king of Babylon came and took their seats in the middle gate: Nergalsharezer, Samgarnebo, Sarsekim the Rab-saris, Nergalsharezer the Rab-mag, and all the rest of the officials of the king of Babylon.",
      "M": "All the officials of the king of Babylon came and took their seats at the middle gate: Nergalsharezer, Samgarnebo, Sarsekim the Rab-saris, Nergalsharezer the Rab-mag, and all the other officials of the king of Babylon.",
      "T": "All the senior commanders of Babylon's king came and took their positions at the middle gate — Nergalsharezer, Samgarnebo, Sarsekim the chief officer, Nergalsharezer the Rab-mag, and the rest of Babylon's command."
    },
    "4": {
      "L": "When Zedekiah king of Judah and all the soldiers saw them, they fled and went out of the city at night by the way of the king's garden, by the gate between the two walls; and he went by the way of the Arabah.",
      "M": "When Zedekiah king of Judah and all his soldiers saw them, they fled. They left the city at night through the king's garden by way of the gate between the two walls, heading toward the Arabah.",
      "T": "When Zedekiah and his soldiers saw them, they ran. Under cover of darkness they slipped out through the royal garden, through the gate between the two walls, and headed toward the Arabah."
    },
    "5": {
      "L": "But the Chaldean army pursued them and overtook Zedekiah in the plains of Jericho; and when they had captured him, they brought him up to Nebuchadnezzar king of Babylon at Riblah in the land of Hamath, where he pronounced judgment on him.",
      "M": "But the Chaldean army pursued them and caught up with Zedekiah on the plains of Jericho. They seized him and brought him up to Nebuchadnezzar king of Babylon at Riblah in the land of Hamath, where he passed sentence on him.",
      "T": "But the Chaldean army ran them down. They caught Zedekiah on the plains of Jericho, seized him, and brought him to Nebuchadnezzar at Riblah in the land of Hamath, where the king pronounced his sentence."
    },
    "6": {
      "L": "The king of Babylon slaughtered the sons of Zedekiah at Riblah before his eyes; also the king of Babylon slaughtered all the nobles of Judah.",
      "M": "At Riblah the king of Babylon killed Zedekiah's sons before his eyes, and also executed all the nobles of Judah.",
      "T": "Before Zedekiah's own eyes, Nebuchadnezzar killed his sons at Riblah. Then he killed every noble of Judah."
    },
    "7": {
      "L": "He put out the eyes of Zedekiah and bound him in bronze chains to bring him to Babylon.",
      "M": "Then he put out Zedekiah's eyes, bound him in bronze chains, and took him to Babylon.",
      "T": "Then he blinded Zedekiah. The last thing Zedekiah saw was the death of his sons. They put him in bronze chains and took him to Babylon."
    },
    "8": {
      "L": "The Chaldeans burned the king's house and the houses of the people with fire and broke down the walls of Jerusalem.",
      "M": "The Chaldeans burned the royal palace and the people's houses and tore down the walls of Jerusalem.",
      "T": "The Chaldeans burned the royal palace and the houses of the people and demolished the walls of Jerusalem."
    },
    "9": {
      "L": "Then Nebuzaradan the captain of the guard carried into exile to Babylon the rest of the people who remained in the city, the deserters who had gone over to him, and the rest of the people who remained.",
      "M": "Then Nebuzaradan the captain of the guard took into exile in Babylon the survivors who remained in the city, the deserters who had gone over to him, and the rest of the people who were left.",
      "T": "Then Nebuzaradan, the captain of the guard, deported to Babylon everyone left in the city — the survivors, the deserters who had already come over, and the remaining population."
    },
    "10": {
      "L": "But Nebuzaradan the captain of the guard left in the land of Judah some of the poor people who owned nothing, and gave them vineyards and fields at the same time.",
      "M": "But Nebuzaradan the captain of the guard left in the land of Judah some of the poorest people, who had nothing, and gave them vineyards and fields at that time.",
      "T": "Nebuzaradan the captain of the guard left behind the poorest of the poor — those who had nothing — and gave them vineyards and fields right then and there."
    },
    "11": {
      "L": "Nebuchadnezzar king of Babylon gave orders about Jeremiah through Nebuzaradan the captain of the guard, saying:",
      "M": "Nebuchadnezzar king of Babylon had given orders concerning Jeremiah through Nebuzaradan the captain of the guard:",
      "T": "Nebuchadnezzar king of Babylon had issued specific orders about Jeremiah through Nebuzaradan the captain of the guard:"
    },
    "12": {
      "L": "Take him and watch over him; do him no harm, but do with him as he tells you.",
      "M": "Take him and look after him; do him no harm, but treat him however he requests.",
      "T": "Find him, protect him, and do him no harm. Give him whatever he asks."
    },
    "13": {
      "L": "So Nebuzaradan the captain of the guard, Nebushazban the Rab-saris, Nergalsharezer the Rab-mag, and all the chief officers of the king of Babylon sent",
      "M": "So Nebuzaradan the captain of the guard, Nebushazban the Rab-saris, Nergalsharezer the Rab-mag, and all the chief officers of the king of Babylon",
      "T": "So Nebuzaradan the captain of the guard, Nebushazban the Rab-saris, Nergalsharezer the Rab-mag, and all of Babylon's senior commanders"
    },
    "14": {
      "L": "and took Jeremiah from the court of the guard and entrusted him to Gedaliah the son of Ahikam, the son of Shaphan, to take him home. So he dwelt among the people.",
      "M": "had Jeremiah taken from the court of the guard and handed over to Gedaliah son of Ahikam son of Shaphan to be brought home. And he settled among the people.",
      "T": "had Jeremiah brought out of the court of the guard and released to Gedaliah son of Ahikam son of Shaphan, who took him home. And Jeremiah settled among his own people."
    },
    "15": {
      "L": "The word of the LORD had come to Jeremiah while he was still shut up in the court of the guard, saying:",
      "M": "The word of the LORD had come to Jeremiah while he was still confined in the court of the guard:",
      "T": "While Jeremiah was still confined in the court of the guard, Yahweh's word had come to him:"
    },
    "16": {
      "L": "Go and say to Ebed-melech the Ethiopian: Thus says the LORD of hosts, the God of Israel: Behold, I will bring my words against this city for harm and not for good, and they shall be accomplished before you on that day.",
      "M": "Go and say to Ebed-melech the Ethiopian: Thus says the LORD of hosts, the God of Israel: I am about to bring my words against this city for disaster and not for good, and they will be fulfilled before your eyes on that day.",
      "T": "Go and tell Ebed-melech the Ethiopian: This is what Yahweh of hosts, the God of Israel, says — I am bringing everything I said against this city — disaster, not salvation — and it will be accomplished before your eyes on that day."
    },
    "17": {
      "L": "But I will deliver you on that day, says the LORD, and you shall not be given into the hand of the men of whom you are afraid.",
      "M": "But I will rescue you on that day, declares the LORD, and you will not be handed over to the men you fear.",
      "T": "But on that day I will rescue you — Yahweh declares it — and you will not be handed over to the men you are afraid of."
    },
    "18": {
      "L": "For I will surely save you, and you shall not fall by the sword, but you shall have your life as plunder, because you have put your trust in me, says the LORD.",
      "M": "I will certainly save you; you will not fall by the sword. You will escape with your life, because you have trusted in me, declares the LORD.",
      "T": "I will absolutely save you. You will not die by the sword. Your life will be your prize — because you put your whole trust in me. Yahweh's word."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 37–39 written.')

if __name__ == '__main__':
    main()
