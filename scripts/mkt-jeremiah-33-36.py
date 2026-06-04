"""
MKT Jeremiah chapters 33–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-33-36.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-28-30.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name force matters
  — oracle delivery, divine address, confrontation scenes. The formula "declares the LORD"
  consistently becomes "Yahweh declares it" or "Yahweh's word" in T.

- H6780 (צֶמַח, ṣemaḥ, "Branch/sprout"): ch. 33:15 — the messianic "Branch of David."
  Capitalized in all three tiers ("Branch") because it is a technical messianic designation
  in Jeremiah (cf. 23:5; Zech 3:8; 6:12). The capitalization is a theological decision:
  Greek has no capitals, but English must choose.

- H6666/H6664 (צְדָקָה/צֶדֶק, ṣĕdāqâ/ṣedeq, "righteousness/justice"): 33:15 — "justice
  and righteousness" — the covenant dyad (mišpāṭ + ṣĕdāqâ). L/M: "justice and righteousness";
  T: "doing what is right and just." 33:16 — "The LORD is our righteousness" applied to
  Jerusalem (cf. 23:6 where applied to the king). L/M: "The LORD is our righteousness";
  T: "Yahweh himself is our righteousness."

- H2617 (חֶסֶד, ḥesed): 33:11 — the liturgical refrain "for his steadfast love endures
  forever" (כִּי לְעוֹלָם חַסְדּוֹ). This is the canonical refrain of Ps 136; 1 Chr 16:34;
  Ps 107:1; 118:1-4. Rendered "steadfast love" in all tiers — the fixed refrain carries
  intertextual weight that paraphrase would disrupt.

- H1865 (דְּרוֹר, dĕrôr, "liberty/release"): ch. 34:8,15,17 — the Jubilee-echo freedom
  proclamation (Lev 25:10). L/M: "liberty"; T: "freedom" — surfacing the Jubilee resonance.
  The ironic counter-proclamation in v.17 ("I proclaim liberty to the sword/plague/famine")
  is preserved in all tiers.

- H5695 (עֵגֶל, ʿēgel, "calf"): ch. 34:18-19 — the covenant-cutting ritual: parties walk
  between two halves of a slaughtered animal, invoking self-imprecation ("may I be cut like
  this if I break the covenant"). L/M: "calf"; T surfaces the imprecatory force explicitly.

- Rechabites (ch. 35): The Rechabite clan maintained strict nomadism and abstinence from
  wine as protest against Canaanite agrarian corruption. Their multi-generational obedience
  to Jonadab's command functions as a parable of what Israel owed Yahweh. The theological
  contrast is the structural point of the chapter.

- Ch. 36 — Jehoiakim's burned scroll: each "column" (section) is cut and burned as Jehudi
  reads. Jehoiakim's unflinching destruction — without fear or garment-tearing (v.24) — is
  the deliberate anti-type of Josiah's response to the Law scroll (2 Kgs 22:11-13). The
  scroll is rewritten with additions: Yahweh's word cannot be extinguished.

Structural and textual notes:

- Ch. 33:1-3 — "Call to me and I will answer you": Jeremiah in prison, city under siege.
  The paradox: darkest circumstances occasion the greatest revelation.

- Ch. 33:14-26 — The Davidic covenant section. vv.14-16 parallel 23:5-6 but apply the
  "LORD our righteousness" name to the city rather than just the king. vv.17-18: the promise
  extends to the Levitical priesthood. vv.19-22: as certain as day and night (echoing 31:35-37).
  vv.23-26: the oath to Abraham/Isaac/Jacob stands.

- Ch. 34:8-22 — The slave-release reversal. Historical setting: during the siege Zedekiah
  enacted Sabbatical-year manumission; when Babylon briefly withdrew (to fight Egypt), the
  slave-owners reneged. Yahweh's response is mordant: they proclaimed liberty to their slaves;
  he will proclaim liberty for them — to the sword, plague, and famine.

- Ch. 35 — Structured as a two-panel parable: (A) Rechabites obey Jonadab (vv.1-11);
  (B) Israel has not obeyed Yahweh (vv.12-17); (C) Promise to the Rechabites (vv.18-19).

- Ch. 36:30 — "Cast out to heat and frost": an unburied death. In ancient honor-shame
  culture, burial = dignity; exposure = ultimate shame. Jehoiakim = anti-Josiah throughout.

OT intertextuality:
- 33:11 — liturgical refrain: Ps 136, 1 Chr 16:34, Ps 107:1, 118:1.
- 33:15-16 — the Branch: 23:5-6; Isa 11:1; Zech 3:8; 6:12.
- 33:20-21 — "covenant with day and night": Gen 8:22; Jer 31:35-36.
- 34:8-14 — slave-release law: Exod 21:2; Deut 15:12-15; Lev 25:39-41.
- 34:18 — covenant-cutting ceremony: Gen 15:9-18.
- 36:23-24 — Jehoiakim burns the scroll; contrast Josiah tears garments: 2 Kgs 22:11.
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
  "33": {
    "1": {
      "L": "Moreover, the word of the LORD came to Jeremiah a second time while he was still shut up in the court of the guard, saying:",
      "M": "The word of the LORD came to Jeremiah a second time, while he was still confined in the court of the guard:",
      "T": "While Jeremiah was still shut up in the prison court, Yahweh's word came to him a second time:"
    },
    "2": {
      "L": "Thus says the LORD who made it, the LORD who formed it in order to establish it — the LORD is his name:",
      "M": "Thus says the LORD who made the earth, the LORD who formed it and established it — the LORD is his name:",
      "T": "This is what Yahweh says — the one who made this earth, who shaped it and set it firm. Yahweh is his name:"
    },
    "3": {
      "L": "Call to me and I will answer you, and will tell you great and hidden things that you have not known.",
      "M": "Call to me and I will answer you, and will tell you great and hidden things that you have not known.",
      "T": "Call out to me and I will answer you. I will disclose to you great, unsearchable things — things you have never reached on your own."
    },
    "4": {
      "L": "For thus says the LORD, the God of Israel, concerning the houses of this city and the houses of the kings of Judah that are torn down for the siege mounds and for the sword:",
      "M": "For thus says the LORD, the God of Israel, concerning the houses of this city and the houses of the kings of Judah that were torn down for the siege ramps and before the sword:",
      "T": "This is what Yahweh, the God of Israel, says about the houses of Jerusalem and the palace buildings of Judah's kings — torn down to provide timber for the siege ramps, exposed to the sword:"
    },
    "5": {
      "L": "The Chaldeans are coming in to fight and to fill them with the corpses of the men whom I struck down in my anger and in my wrath, for I have hidden my face from this city because of all their evil.",
      "M": "The Chaldeans are coming to fight and to fill those houses with the corpses of men whom I struck down in my anger and wrath, for I have hidden my face from this city because of all their wickedness.",
      "T": "The Chaldeans are advancing to fight, and they will pack those torn-down houses with the bodies of the men I have struck down in my fury — because I turned my face away from this city on account of all its evil."
    },
    "6": {
      "L": "Behold, I am about to bring to it health and healing, and I will heal them and reveal to them abundance of peace and security.",
      "M": "Behold, I will bring health and healing to it; I will heal them and reveal to them an abundance of prosperity and security.",
      "T": "But watch: I am bringing this city health and wholeness. I will heal my people and open up to them a full river of peace and faithfulness."
    },
    "7": {
      "L": "And I will restore the fortunes of Judah and the fortunes of Israel, and will rebuild them as at the first.",
      "M": "I will restore the fortunes of Judah and Israel and rebuild them as they were at the beginning.",
      "T": "I will reverse the captivity of Judah and of Israel and build them back to what they were at the beginning."
    },
    "8": {
      "L": "And I will cleanse them from all the guilt of their sin against me, and I will forgive all the guilt of their sin and their rebellion against me.",
      "M": "I will cleanse them from all the iniquity by which they sinned against me, and I will forgive all the iniquity and rebellion by which they sinned against me.",
      "T": "I will wash them clean of every sin they committed against me. Every act of rebellion, every iniquity — I will forgive the whole account."
    },
    "9": {
      "L": "And it shall become to me a name of joy, a praise, and a glory before all the nations of the earth who shall hear of all the good that I do for them, and they shall be afraid and tremble because of all the good and all the prosperity that I bring to it.",
      "M": "This city will be to me a name of joy, a praise, and a glory before all the nations of the earth who will hear of all the good I do for them. They will be in awe and tremble at all the goodness and prosperity I bring to it.",
      "T": "This city will become my trophy — a name of joy and praise and honor before every nation on earth. They will hear what I have done here, and they will tremble in awe at the overflowing goodness and prosperity I pour out on my people."
    },
    "10": {
      "L": "Thus says the LORD: In this place of which you say, 'It is a waste, without man or beast,' in the cities of Judah and the streets of Jerusalem that are desolate, without man, without inhabitant, without beast, there shall be heard again",
      "M": "Thus says the LORD: In this place that you are calling a waste — without man or beast — and in the cities of Judah and the streets of Jerusalem that are desolate, without man, without inhabitant, without beast, there shall again be heard",
      "T": "This is what Yahweh says: In this very place that you are now calling a wasteland — empty of people, empty of animals — in all the towns of Judah and Jerusalem's streets that lie silent and abandoned, there will once again be heard"
    },
    "11": {
      "L": "the voice of joy and the voice of gladness, the voice of the bridegroom and the voice of the bride, the voice of those who sing, 'Give thanks to the LORD of hosts, for the LORD is good, for his steadfast love endures forever!' as they bring thank offerings to the house of the LORD. For I will restore the fortunes of the land as at the first, says the LORD.",
      "M": "the voice of joy and the voice of gladness, the voice of the bridegroom and the voice of the bride, the voice of those who sing, 'Give thanks to the LORD of hosts, for the LORD is good, for his steadfast love endures forever!' as they bring thank offerings to the house of the LORD. For I will restore the fortunes of the land as they were at the first, declares the LORD.",
      "T": "the sound of joy and rejoicing, of bride and bridegroom singing, and the voices of those bringing thank offerings to Yahweh's temple, singing: 'Give thanks to Yahweh of hosts — for he is good! His steadfast love never ends!' I will turn this land's captivity around, just as it was at the beginning. Yahweh declares it."
    },
    "12": {
      "L": "Thus says the LORD of hosts: In this place that is waste, without man or beast, and in all its cities, there shall again be habitations of shepherds who cause flocks to lie down.",
      "M": "Thus says the LORD of hosts: In this place that is desolate — without man or beast — and in all its cities, there will again be pastures where shepherds rest their flocks.",
      "T": "Yahweh of hosts says this: In this land lying empty and silent — no person, no animal — in every last town, there will again be grazing grounds where shepherds bring their flocks to rest."
    },
    "13": {
      "L": "In the cities of the hill country, in the cities of the Shephelah, in the cities of the Negeb, in the land of Benjamin, the places around Jerusalem, and in the cities of Judah, flocks shall again pass under the hands of the one who counts them, says the LORD.",
      "M": "In the cities of the hill country, in the cities of the Shephelah, and in the cities of the Negeb, in the land of Benjamin, in the places around Jerusalem, and in the cities of Judah, the flocks shall once more pass under the hands of the one who counts them, declares the LORD.",
      "T": "From the hill country towns to the Shephelah lowlands, from the Negeb to the land of Benjamin, from the villages around Jerusalem to every city of Judah — in all of them, flocks will once more file past the hands of the shepherd counting them. Yahweh declares it."
    },
    "14": {
      "L": "Behold, the days are coming, declares the LORD, when I will perform the good word that I promised to the house of Israel and the house of Judah.",
      "M": "The days are coming, declares the LORD, when I will fulfill the good promise I made to the house of Israel and the house of Judah.",
      "T": "Days are coming — Yahweh declares it — when I will make good every word of promise I spoke over Israel and over Judah."
    },
    "15": {
      "L": "In those days and at that time I will cause a righteous Branch to spring up for David, and he shall execute justice and righteousness in the land.",
      "M": "In those days and at that time I will cause a righteous Branch to spring up for David, and he shall execute justice and righteousness in the land.",
      "T": "In those days, at that very time, I will cause a righteous Branch to shoot up from David's line — one who will govern with justice and righteousness throughout the land."
    },
    "16": {
      "L": "In those days Judah shall be saved and Jerusalem shall dwell securely. And this is the name by which it shall be called: 'The LORD is our righteousness.'",
      "M": "In those days Judah will be saved and Jerusalem will dwell in safety. And this is the name by which it will be called: 'The LORD is our righteousness.'",
      "T": "In those days Judah will be rescued and Jerusalem will live in safety. And the name this city will carry is: 'Yahweh himself is our righteousness.'"
    },
    "17": {
      "L": "For thus says the LORD: David shall never lack a man to sit on the throne of the house of Israel,",
      "M": "For thus says the LORD: There will never fail to be a man from David's line to sit on the throne of the house of Israel,",
      "T": "This is what Yahweh says: David's line will never go extinct — there will always be one from his descendants seated on Israel's throne,"
    },
    "18": {
      "L": "and the Levitical priests shall never lack a man in my presence to offer burnt offerings, to burn grain offerings, and to make sacrifices forever.",
      "M": "and the Levitical priests shall never lack a man in my presence to offer burnt offerings, to burn grain offerings, and to make sacrifices continually.",
      "T": "and among the Levitical priests, there will always be someone standing in my presence — offering burnt offerings, presenting grain offerings, performing sacrifices — always, without interruption."
    },
    "19": {
      "L": "The word of the LORD came to Jeremiah:",
      "M": "The word of the LORD came to Jeremiah:",
      "T": "Yahweh's word came to Jeremiah again:"
    },
    "20": {
      "L": "Thus says the LORD: If you can break my covenant with the day and my covenant with the night, so that day and night will not come at their appointed time,",
      "M": "Thus says the LORD: If you can break my covenant with the day and my covenant with the night, so that day and night no longer come at their appointed time,",
      "T": "This is what Yahweh says: If you could somehow break my covenant with the day and my covenant with the night — stop day and night from arriving on schedule —"
    },
    "21": {
      "L": "then also my covenant with David my servant may be broken, so that he will not have a son to reign on his throne, and my covenant with the Levitical priests my ministers.",
      "M": "then my covenant with my servant David could also be broken, so that he would no longer have a son to reign on his throne, and so also my covenant with the Levitical priests who minister to me.",
      "T": "— only then could my covenant with David my servant be broken, only then could his line be stripped of a son on the throne. And only then could my covenant with the Levitical priests who serve me be undone."
    },
    "22": {
      "L": "As the host of heaven cannot be numbered and the sand of the sea cannot be measured, so I will multiply the offspring of David my servant and the Levites who minister to me.",
      "M": "As the host of heaven cannot be numbered and the sand of the sea cannot be measured, so I will multiply the offspring of David my servant and the Levites who minister to me.",
      "T": "As the stars of heaven are uncountable and the sand of the sea cannot be measured out, so I will make the descendants of David my servant and the Levites who serve me beyond all reckoning."
    },
    "23": {
      "L": "The word of the LORD came to Jeremiah:",
      "M": "The word of the LORD came to Jeremiah:",
      "T": "Yahweh's word came to Jeremiah once more:"
    },
    "24": {
      "L": "Have you not considered what this people is saying? 'The two clans that the LORD chose, he has rejected them'; thus they have despised my people so that they are no longer a nation in their sight.",
      "M": "Have you not noticed what these people are saying? 'The LORD has rejected the two families he chose.' Thus they have despised my people as though they were no longer a nation in their eyes.",
      "T": "Have you paid attention to what people are saying? 'Yahweh has rejected the two families he chose.' That is how they have come to despise my people — treating Israel as if it were no longer a nation at all."
    },
    "25": {
      "L": "Thus says the LORD: If I have not established my covenant with day and night and the fixed orders of heaven and earth,",
      "M": "Thus says the LORD: If I have not established my covenant with day and night and the fixed orders of heaven and earth,",
      "T": "This is what Yahweh says: If I have not put in place my covenant with day and night — the fixed patterns of heaven and earth —"
    },
    "26": {
      "L": "then I will reject the offspring of Jacob and David my servant and will not choose from his descendants rulers over the offspring of Abraham, Isaac, and Jacob. For I will restore their fortunes and have mercy on them.",
      "M": "then I would reject the descendants of Jacob and my servant David, and not choose from David's line rulers over the descendants of Abraham, Isaac, and Jacob. But I will restore their fortunes and have mercy on them.",
      "T": "— only then would I cast off the descendants of Jacob and of David my servant, only then would I refuse to raise up rulers from his line over the offspring of Abraham, Isaac, and Jacob. But I will turn their captivity around. I will show them mercy. Yahweh's word."
    }
  },
  "34": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD, when Nebuchadnezzar king of Babylon and all his army and all the kingdoms of the earth under his dominion and all the peoples were fighting against Jerusalem and all its cities:",
      "M": "The word that came to Jeremiah from the LORD when Nebuchadnezzar king of Babylon and all his army, along with all the kingdoms and peoples under his dominion, were fighting against Jerusalem and all its cities:",
      "T": "This is the word Yahweh gave to Jeremiah when Nebuchadnezzar king of Babylon — with his entire army, every kingdom under his command, every subject people — was waging war against Jerusalem and every town around it:"
    },
    "2": {
      "L": "Thus says the LORD, the God of Israel: Go and speak to Zedekiah king of Judah and tell him: Thus says the LORD: Behold, I am going to give this city into the hand of the king of Babylon, and he shall burn it with fire.",
      "M": "Thus says the LORD, the God of Israel: Go, speak to Zedekiah king of Judah, and say to him: Thus says the LORD — I am going to hand this city over to the king of Babylon, and he will burn it with fire.",
      "T": "Yahweh, the God of Israel, says this: Go find Zedekiah king of Judah and deliver this word: Yahweh says — I am putting this city into the hands of Babylon's king. He will burn it to the ground."
    },
    "3": {
      "L": "You shall not escape from his hand but shall surely be captured and delivered into his hand; your eyes shall see the eyes of the king of Babylon and he shall speak with you mouth to mouth, and you shall go to Babylon.",
      "M": "You will not escape his grasp but will certainly be captured and handed over to him. Your eyes will look into the eyes of the king of Babylon, and he will speak with you in person. Then you will go to Babylon.",
      "T": "You will not escape him. You will be captured, handed over to him. You will look Babylon's king in the eyes, and he will speak with you face to face. Then you will go to Babylon."
    },
    "4": {
      "L": "Yet hear the word of the LORD, O Zedekiah king of Judah: Thus says the LORD concerning you — you shall not die by the sword.",
      "M": "Yet hear the word of the LORD, O Zedekiah king of Judah. Thus says the LORD concerning you: You will not die by the sword.",
      "T": "But hear one more word from Yahweh, King Zedekiah of Judah. This is what Yahweh says about you personally: You will not die by the sword."
    },
    "5": {
      "L": "In peace you shall die, and with the burnings of spices for your fathers, the former kings who were before you, so they shall burn spices for you and lament you, saying, 'Alas, lord!' For I have spoken the word, declares the LORD.",
      "M": "You will die in peace. And as spices were burned in honor of your ancestors, the kings who preceded you, so they will burn spices for you and mourn for you, crying, 'Alas, lord!' For I have spoken the word, declares the LORD.",
      "T": "You will die in peace. They will light burial spices for you, just as they did for the kings who came before you. And the people will mourn, crying: 'Oh, our lord!' I have spoken it. Yahweh's word."
    },
    "6": {
      "L": "Then Jeremiah the prophet spoke all these words to Zedekiah king of Judah, in Jerusalem,",
      "M": "Then the prophet Jeremiah spoke all these words to Zedekiah king of Judah, in Jerusalem,",
      "T": "Jeremiah the prophet delivered every one of these words to King Zedekiah in Jerusalem,"
    },
    "7": {
      "L": "while the army of the king of Babylon was fighting against Jerusalem and against all the remaining cities of Judah — against Lachish and against Azekah — for these were the only fortified cities of Judah that remained.",
      "M": "while the army of the king of Babylon was fighting against Jerusalem and against all the remaining cities of Judah — Lachish and Azekah — for these were the only fortified cities of Judah still holding out.",
      "T": "while Babylon's army was still hammering Jerusalem and the last towns of Judah — Lachish and Azekah — the only fortified cities left in all Judah that had not yet fallen."
    },
    "8": {
      "L": "The word that came to Jeremiah from the LORD, after King Zedekiah had made a covenant with all the people in Jerusalem to proclaim liberty to them:",
      "M": "The word that came to Jeremiah from the LORD after King Zedekiah had made a covenant with all the people in Jerusalem to proclaim liberty to them:",
      "T": "This is the word Yahweh gave to Jeremiah after King Zedekiah made a covenant with all the people of Jerusalem to proclaim freedom for the slaves:"
    },
    "9": {
      "L": "that everyone should set free his Hebrew male slave and his Hebrew female slave, so that no one should keep a fellow Jew in bondage.",
      "M": "Everyone was to release his Hebrew male slave and his Hebrew female slave, so that no one would keep a fellow Hebrew in slavery.",
      "T": "Every person was to release their Hebrew male and female slaves — no Jew was to be kept in bondage to another Jew."
    },
    "10": {
      "L": "And all the officials and all the people who had entered into the covenant heard — everyone was to set free his male slave and his female slave so as to not keep them in bondage any longer; they obeyed and they set them free.",
      "M": "All the officials and all the people who had entered into the covenant obeyed — each released his male and female slave so as not to keep them in bondage any longer. They listened and set them free.",
      "T": "All the officials and all the people who had made this covenant obeyed: they released their slaves, male and female, and no longer held them in servitude. They listened, and they did it."
    },
    "11": {
      "L": "But afterward they turned and took back the male slaves and female slaves whom they had set free and brought them back into bondage as male and female slaves.",
      "M": "But afterward they turned back and took back the male and female slaves they had freed, forcing them back into slavery.",
      "T": "But then they turned around. They went back and seized the slaves they had just freed — men and women both — and dragged them back into bondage."
    },
    "12": {
      "L": "Then the word of the LORD came to Jeremiah from the LORD:",
      "M": "Then the word of the LORD came to Jeremiah from the LORD:",
      "T": "Then Yahweh's word came to Jeremiah:"
    },
    "13": {
      "L": "Thus says the LORD, the God of Israel: I myself made a covenant with your fathers when I brought them out of the land of Egypt, out of the house of slavery, saying:",
      "M": "Thus says the LORD, the God of Israel: I made a covenant with your ancestors when I brought them out of Egypt, out of the house of slavery, saying:",
      "T": "Yahweh, the God of Israel, says this: When I brought your ancestors out of Egypt, out of that house of slavery, I made a covenant with them. I said:"
    },
    "14": {
      "L": "'At the end of seven years each of you must set free the fellow Hebrew who has been sold to you and has served you six years. You must set him free from your service.' But your fathers did not listen to me or incline their ear to me.",
      "M": "'At the end of seven years, every one of you must release a fellow Hebrew who has been sold to you; after six years of service, you must set him free.' But your fathers did not listen to me or give me their attention.",
      "T": "'When a fellow Hebrew has served you for six years, you must release him at the end of seven.' But your ancestors would not listen to me. They tuned me out entirely."
    },
    "15": {
      "L": "You yourselves recently repented and did what was right in my eyes by proclaiming liberty, each to his neighbor, and you made a covenant before me in the house that is called by my name.",
      "M": "And you — just recently you turned back and did what was right in my eyes, each of you proclaiming liberty to your neighbor. You made a covenant before me in the house that bears my name.",
      "T": "You — just recently, you actually turned around. You did what is right in my sight: each of you proclaimed freedom for your neighbor. You made a covenant on this in the temple that bears my name."
    },
    "16": {
      "L": "But then you turned and profaned my name when each of you took back his male and female slave whom you had set free according to their desire, and you brought them back into bondage to be your male and female slaves.",
      "M": "But then you turned back and profaned my name: each of you took back the male and female slaves you had set free, and you forced them back into slavery.",
      "T": "But you turned back and desecrated my name. You went and retrieved every slave you had freed — men and women both — and dragged them back into servitude. You went back on your word in the house where my name lives."
    },
    "17": {
      "L": "Therefore thus says the LORD: You did not obey me by proclaiming liberty, everyone to his brother and everyone to his neighbor; behold, I am proclaiming to you a liberty, declares the LORD — to the sword, to the pestilence, and to the famine; and I will make you a horror to all the kingdoms of the earth.",
      "M": "Therefore thus says the LORD: You have not obeyed me by proclaiming liberty, each to his brother and to his neighbor. So now I am proclaiming liberty for you, declares the LORD — liberty to the sword, to pestilence, and to famine. And I will make you a horror to all the kingdoms of the earth.",
      "T": "Therefore this is what Yahweh says: You would not proclaim freedom — to your brothers, to your neighbors. So now I am proclaiming freedom over you — Yahweh declares it — freedom to meet the sword, the plague, and the famine. I will make you an object of horror to every kingdom on earth."
    },
    "18": {
      "L": "And the men who transgressed my covenant, who did not keep the terms of the covenant that they made before me — when they cut the calf in two and passed between its parts —",
      "M": "And I will hand over the men who violated my covenant and did not keep the terms of the covenant they made before me, when they cut the calf in two and passed between its parts —",
      "T": "As for the men who broke my covenant and refused to keep the terms they agreed to in my presence — who cut a calf in two and walked between the pieces, calling down on themselves what happened to that animal if they ever broke faith —"
    },
    "19": {
      "L": "the officials of Judah, the officials of Jerusalem, the court officials, the priests, and all the people of the land who passed between the parts of the calf —",
      "M": "the officials of Judah, the officials of Jerusalem, the court officials, the priests, and all the people of the land who passed between the parts of the calf —",
      "T": "the officials of Judah, the officials of Jerusalem, the court eunuchs, the priests, and all the people of the land who walked through that slaughtered calf —"
    },
    "20": {
      "L": "I will give them into the hand of their enemies and into the hand of those who seek their lives; their dead bodies shall be food for the birds of the air and the beasts of the earth.",
      "M": "I will give them into the hands of their enemies and into the hands of those who seek their lives. Their dead bodies will become food for the birds of the sky and the beasts of the earth.",
      "T": "I will hand them over to their enemies, to every faction that wants them dead. Their bodies will lie in the open — carrion for the birds of the air and the animals of the field."
    },
    "21": {
      "L": "And Zedekiah king of Judah and his officials I will give into the hand of their enemies and into the hand of those who seek their lives, into the hand of the army of the king of Babylon that has withdrawn from you.",
      "M": "And Zedekiah king of Judah and his officials I will give into the hand of their enemies and into the hand of those who seek their lives — into the hand of the army of the king of Babylon that has pulled back from you.",
      "T": "Zedekiah king of Judah and his court — I will hand them to their enemies, to every faction that wants them dead, right into the hands of Babylon's army that pulled back from you only temporarily."
    },
    "22": {
      "L": "Behold, I am going to command, declares the LORD, and will bring them back to this city; and they will fight against it and take it and burn it with fire. And the cities of Judah I will make a desolation without inhabitant.",
      "M": "I am about to give the command, declares the LORD, and I will bring them back to this city. They will fight against it, take it, and burn it with fire. I will make the cities of Judah a desolation without inhabitant.",
      "T": "I am issuing the order — Yahweh declares it. I am turning Babylon's army around and pointing it back at this city. They will come, they will take it, they will burn it. Every city of Judah will be left empty and desolate."
    }
  },
  "35": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD in the days of Jehoiakim the son of Josiah, king of Judah:",
      "M": "The word that came to Jeremiah from the LORD in the days of Jehoiakim son of Josiah, king of Judah:",
      "T": "This is the word Yahweh gave to Jeremiah in the days of Jehoiakim son of Josiah, king of Judah:"
    },
    "2": {
      "L": "Go to the house of the Rechabites and speak with them, and bring them to the house of the LORD, into one of the chambers, and give them wine to drink.",
      "M": "Go to the house of the Rechabites, speak with them, and bring them to the house of the LORD, into one of the inner rooms, and offer them wine to drink.",
      "T": "Go to the Rechabite clan. Speak with them. Bring them into the temple, into one of the side rooms, and offer them wine to drink."
    },
    "3": {
      "L": "So I took Jaazaniah the son of Jeremiah, son of Habaziniah, and his brothers and all his sons and the whole house of the Rechabites.",
      "M": "So I took Jaazaniah son of Jeremiah, son of Habaziniah, together with his brothers and all his sons and the whole house of the Rechabites.",
      "T": "So I brought Jaazaniah son of Jeremiah son of Habaziniah, along with his brothers, all his sons, and the entire Rechabite household."
    },
    "4": {
      "L": "And I brought them into the house of the LORD, into the chamber of the sons of Hanan the son of Igdaliah, the man of God, which was near the chamber of the officials, which was above the chamber of Maaseiah the son of Shallum, keeper of the threshold.",
      "M": "I brought them into the house of the LORD, into the chamber of the sons of Hanan son of Igdaliah, the man of God, which was adjacent to the chamber of the officials and above the chamber of Maaseiah son of Shallum, keeper of the entrance.",
      "T": "I brought them into Yahweh's temple, into the room belonging to the sons of Hanan son of Igdaliah, the man of God — the room beside the officials' chamber, above the room of Maaseiah son of Shallum, who kept the threshold."
    },
    "5": {
      "L": "Then I set before the members of the house of the Rechabites pitchers full of wine and cups, and I said to them: Drink wine.",
      "M": "Then I placed before the members of the Rechabite household pitchers full of wine and cups, and I said to them: Drink wine.",
      "T": "I set out pitchers of wine and cups before them and said: Drink wine."
    },
    "6": {
      "L": "But they answered: We will drink no wine, for Jonadab the son of Rechab, our father, commanded us: You shall not drink wine, neither you nor your sons, forever.",
      "M": "But they replied: We will not drink wine, for Jonadab son of Rechab, our father, commanded us: You shall not drink wine, you or your sons, ever.",
      "T": "But they answered: We will not drink wine. Our ancestor Jonadab son of Rechab commanded us: You and your sons must never drink wine."
    },
    "7": {
      "L": "You shall not build a house; you shall not sow seed; you shall not plant a vineyard or have one; but in tents you shall dwell all your days, so that you may live many days in the land where you dwell as sojourners.",
      "M": "You shall not build a house, sow seed, or plant a vineyard or own one. You shall live in tents all your days, so that you may live long in the land where you are strangers.",
      "T": "Build no house. Sow no field. Plant no vineyard — own none. Live in tents all your days. That way you will live long in whatever land you pass through as strangers."
    },
    "8": {
      "L": "And we have obeyed the voice of Jonadab the son of Rechab, our father, in all that he commanded us — to drink no wine all our days, ourselves, our wives, our sons, or our daughters,",
      "M": "We have obeyed the voice of Jonadab son of Rechab, our father, in everything he commanded us — never drinking wine, we ourselves or our wives or our sons or our daughters,",
      "T": "And we have done exactly what our ancestor Jonadab son of Rechab commanded us. We drink no wine — not us, not our wives, not our sons, not our daughters."
    },
    "9": {
      "L": "and not to build houses to dwell in; we have no vineyard or field or seed,",
      "M": "We have not built houses to live in, and we have no vineyard, field, or seed.",
      "T": "We have built no houses, owned no vineyard, farmed no field, planted no crop."
    },
    "10": {
      "L": "but we have dwelt in tents and have obeyed and done all that Jonadab our father commanded us.",
      "M": "We have lived in tents and have obeyed and done all that our father Jonadab commanded us.",
      "T": "We have lived in tents and kept every single command our ancestor Jonadab laid on us."
    },
    "11": {
      "L": "But when Nebuchadrezzar king of Babylon came up against the land, we said: Come, let us go to Jerusalem for fear of the army of the Chaldeans and for fear of the army of the Syrians. So we have been living in Jerusalem.",
      "M": "But when Nebuchadrezzar king of Babylon came up against the land, we said: Come, let us go to Jerusalem for fear of the Chaldean army and the Syrian army. That is why we are living in Jerusalem now.",
      "T": "Then Nebuchadrezzar king of Babylon invaded the land, and we said to each other: Come — let us get to Jerusalem. The Chaldean army and the Aramean forces are out there. That is why we are here in Jerusalem now."
    },
    "12": {
      "L": "Then the word of the LORD came to Jeremiah:",
      "M": "Then the word of the LORD came to Jeremiah:",
      "T": "Then Yahweh's word came to Jeremiah:"
    },
    "13": {
      "L": "Thus says the LORD of hosts, the God of Israel: Go and say to the people of Judah and the inhabitants of Jerusalem: Will you not receive instruction to listen to my words? declares the LORD.",
      "M": "Thus says the LORD of hosts, the God of Israel: Go and say to the people of Judah and the inhabitants of Jerusalem: Will you not receive instruction and listen to my words? declares the LORD.",
      "T": "Yahweh of hosts, the God of Israel, says this: Go tell the people of Judah and the inhabitants of Jerusalem — Will you not take correction? Will you not listen to my words? Yahweh's word."
    },
    "14": {
      "L": "The command of Jonadab the son of Rechab, which he commanded his sons to drink no wine, has been kept, for to this day they drink none, for they have obeyed their father's command. But I have spoken to you persistently, and you have not listened to me.",
      "M": "The command that Jonadab son of Rechab gave to his sons — to drink no wine — has been kept. To this day they drink none, because they have obeyed their ancestor's command. But I have spoken to you persistently, and you have not listened to me.",
      "T": "The command Jonadab son of Rechab gave his sons — never drink wine — is still being kept. Not one of them has touched it to this day. They obey a dead man's word. But I have spoken to you urgently, again and again — and you have not listened to me."
    },
    "15": {
      "L": "I have sent to you all my servants the prophets, sending them persistently, saying: Turn now every one of you from his evil way, and amend your doings, and do not go after other gods to serve them, and you shall dwell in the land that I gave to you and your fathers. But you did not incline your ear or listen to me.",
      "M": "I have sent you all my servants the prophets, again and again, saying: Turn now, each of you, from your evil way, make your actions right, and do not follow other gods to serve them — then you may dwell in the land I gave to you and your fathers. But you did not incline your ear or listen to me.",
      "T": "I have sent you my servants the prophets — every one of them, sent early and sent often — saying: Turn back, each of you, from your wicked path. Straighten your conduct. Stop chasing other gods. Do that, and you will remain in the land I gave you and your ancestors. But you would not listen. You would not even turn your head toward me."
    },
    "16": {
      "L": "The sons of Jonadab the son of Rechab have kept the command their father gave them, but this people has not obeyed me.",
      "M": "The descendants of Jonadab son of Rechab have kept their father's command, but this people has not obeyed me.",
      "T": "The descendants of Jonadab son of Rechab have honored their ancestor's word. But this people — they will not obey me."
    },
    "17": {
      "L": "Therefore thus says the LORD, the God of hosts, the God of Israel: Behold, I am bringing on Judah and on all the inhabitants of Jerusalem all the disaster that I have pronounced against them, because I have spoken to them and they have not listened, and I have called to them and they have not answered.",
      "M": "Therefore thus says the LORD, the God of hosts, the God of Israel: I am going to bring on Judah and all the inhabitants of Jerusalem all the disaster I have pronounced against them, because I spoke to them and they did not listen, because I called to them and they did not answer.",
      "T": "Therefore this is what Yahweh, the God of hosts, the God of Israel, says: I am bringing every disaster I pronounced against them down on Judah and on all who live in Jerusalem. I spoke — they did not listen. I called — they did not answer."
    },
    "18": {
      "L": "But to the house of the Rechabites Jeremiah said: Thus says the LORD of hosts, the God of Israel: Because you have obeyed the command of Jonadab your father and kept all his precepts and done all that he commanded you,",
      "M": "Then Jeremiah said to the house of the Rechabites: Thus says the LORD of hosts, the God of Israel: Because you have obeyed the command of Jonadab your father and kept all his instructions and done all that he commanded you,",
      "T": "Then Jeremiah turned to the Rechabite household: Yahweh of hosts, the God of Israel, says this: Because you obeyed your ancestor Jonadab's command, kept all his rules, and did everything he required —"
    },
    "19": {
      "L": "therefore thus says the LORD of hosts, the God of Israel: Jonadab the son of Rechab shall never lack a man to stand before me.",
      "M": "therefore thus says the LORD of hosts, the God of Israel: Jonadab son of Rechab shall never fail to have a man standing before me.",
      "T": "therefore this is what Yahweh of hosts, the God of Israel, says: Jonadab son of Rechab will never lack a descendant who stands in my presence."
    }
  },
  "36": {
    "1": {
      "L": "And it came to pass in the fourth year of Jehoiakim the son of Josiah, king of Judah, that this word came to Jeremiah from the LORD:",
      "M": "In the fourth year of Jehoiakim son of Josiah, king of Judah, this word came to Jeremiah from the LORD:",
      "T": "In the fourth year of King Jehoiakim son of Josiah of Judah, Yahweh gave this word to Jeremiah:"
    },
    "2": {
      "L": "Take a scroll and write in it all the words that I have spoken to you against Israel and against Judah and against all the nations, from the day I spoke to you, from the days of Josiah, until this day.",
      "M": "Take a scroll and write in it all the words I have spoken to you against Israel, against Judah, and against all the nations, from the day I first spoke to you in the days of Josiah until this day.",
      "T": "Take a scroll and write down every word I have spoken to you — against Israel, against Judah, against every nation — from the day I first spoke to you in Josiah's time right up to now."
    },
    "3": {
      "L": "It may be that the house of Judah will hear all the disaster that I intend to do to them, so that every man may turn from his evil way, and I may forgive their iniquity and their sin.",
      "M": "Perhaps the house of Judah will hear of all the disaster I intend to bring on them, so that each person will turn from his evil way, and I will forgive their iniquity and their sin.",
      "T": "Perhaps when Judah hears spelled out in full all the disaster I am planning for them, every person will turn back from their evil path — and I will forgive their guilt and their sin."
    },
    "4": {
      "L": "Then Jeremiah called Baruch the son of Neriah, and Baruch wrote on a scroll at the dictation of Jeremiah all the words of the LORD that he had spoken to him.",
      "M": "So Jeremiah summoned Baruch son of Neriah, and Baruch wrote on a scroll everything Jeremiah dictated to him — all the words of the LORD that had been spoken to Jeremiah.",
      "T": "So Jeremiah called in Baruch son of Neriah, and Baruch wrote down everything Jeremiah dictated — every word Yahweh had given to Jeremiah."
    },
    "5": {
      "L": "And Jeremiah commanded Baruch, saying: I am restricted; I cannot go to the house of the LORD.",
      "M": "Jeremiah gave Baruch these instructions: I am banned; I cannot go to the house of the LORD.",
      "T": "Jeremiah gave Baruch his instructions: I am barred from entering Yahweh's temple."
    },
    "6": {
      "L": "So you go and read from the scroll that you have written at my dictation the words of the LORD in the ears of the people in the LORD's house on the day of fasting. Also you shall read them in the ears of all the men of Judah who come out of their cities.",
      "M": "So you go and read from the scroll you wrote at my dictation — the words of the LORD — to all the people in the LORD's house on a day of fasting. Read them also to all the people of Judah who come in from their towns.",
      "T": "So you go. On a fasting day, read from the scroll you wrote — Yahweh's words — to everyone in the temple. Read them also to all the people of Judah who come in from the towns."
    },
    "7": {
      "L": "Perhaps their plea will come before the LORD and every man will turn from his evil way, for the anger and the wrath that the LORD has pronounced against this people is great.",
      "M": "Perhaps they will bring their petition before the LORD and each person will turn from his evil way, for great is the anger and wrath that the LORD has pronounced against this people.",
      "T": "Perhaps they will take their case before Yahweh and turn back from their evil paths — for the anger and fury Yahweh has pronounced against this people is immense."
    },
    "8": {
      "L": "And Baruch the son of Neriah did according to all that Jeremiah the prophet commanded him, reading from the scroll the words of the LORD in the LORD's house.",
      "M": "Baruch son of Neriah did exactly what the prophet Jeremiah commanded him, reading the words of the LORD from the scroll in the house of the LORD.",
      "T": "Baruch son of Neriah did exactly as Jeremiah the prophet commanded: he went and read Yahweh's words from the scroll in Yahweh's house."
    },
    "9": {
      "L": "And it came to pass in the fifth year of Jehoiakim the son of Josiah, king of Judah, in the ninth month, that all the people in Jerusalem and all the people who came to Jerusalem from the cities of Judah proclaimed a fast before the LORD.",
      "M": "In the fifth year of Jehoiakim son of Josiah, king of Judah, in the ninth month, all the people in Jerusalem and all the people who had come from the towns of Judah to Jerusalem proclaimed a fast before the LORD.",
      "T": "In the fifth year of King Jehoiakim son of Josiah of Judah, in the ninth month, a solemn fast was proclaimed before Yahweh — observed by all Jerusalem and everyone who had come in from the towns of Judah."
    },
    "10": {
      "L": "Then Baruch read from the scroll the words of Jeremiah in the house of the LORD, in the chamber of Gemariah the son of Shaphan the scribe, in the upper court, at the entry of the New Gate of the LORD's house, in the ears of all the people.",
      "M": "Then Baruch read the words of Jeremiah from the scroll in the house of the LORD, in the chamber of Gemariah son of Shaphan the secretary — in the upper court, at the entrance to the New Gate of the LORD's house — in the hearing of all the people.",
      "T": "Baruch stood in the chamber of Gemariah son of Shaphan the royal secretary — in the upper court, at the entry to the New Gate of Yahweh's temple — and read Jeremiah's words from the scroll in the hearing of all the people."
    },
    "11": {
      "L": "And when Micaiah the son of Gemariah, son of Shaphan, heard all the words of the LORD from the scroll,",
      "M": "When Micaiah son of Gemariah, son of Shaphan, heard all the words of the LORD from the scroll,",
      "T": "When Micaiah son of Gemariah son of Shaphan heard every word of Yahweh from the scroll,"
    },
    "12": {
      "L": "he went down to the king's house, into the secretary's chamber; and all the officials were sitting there — Elishama the secretary, and Delaiah the son of Shemaiah, and Elnathan the son of Achbor, and Gemariah the son of Shaphan, and Zedekiah the son of Hananiah, and all the other officials.",
      "M": "he went down to the king's house, into the secretary's chamber. All the officials were sitting there: Elishama the secretary, Delaiah son of Shemaiah, Elnathan son of Achbor, Gemariah son of Shaphan, Zedekiah son of Hananiah, and all the other officials.",
      "T": "he went straight to the king's palace, to the secretary's chamber. The entire council was assembled: Elishama the royal secretary; Delaiah son of Shemaiah; Elnathan son of Achbor; Gemariah son of Shaphan; Zedekiah son of Hananiah — all the senior officials."
    },
    "13": {
      "L": "And Micaiah told them all the words that he had heard when Baruch read the scroll in the hearing of the people.",
      "M": "Micaiah reported to them all the words he had heard when Baruch read the scroll in the hearing of the people.",
      "T": "Micaiah told them everything he had heard — every word Baruch had read aloud to the crowds."
    },
    "14": {
      "L": "Then all the officials sent Jehudi the son of Nethaniah, son of Shelemiah, son of Cushi, to Baruch, saying: Take in your hand the scroll from which you read in the hearing of the people and come. And Baruch the son of Neriah took the scroll in his hand and went to them.",
      "M": "Then all the officials sent Jehudi son of Nethaniah, son of Shelemiah, son of Cushi, to Baruch with this message: Take the scroll from which you read to the people and come here. So Baruch son of Neriah picked up the scroll and went to them.",
      "T": "The officials sent Jehudi son of Nethaniah son of Shelemiah son of Cushi with a message for Baruch: Bring the scroll you read to the people and come here. Baruch son of Neriah picked up the scroll and came."
    },
    "15": {
      "L": "And they said to him: Sit down and read it in our ears. And Baruch read it in their ears.",
      "M": "They said to him: Sit down and read it to us. So Baruch read it to them.",
      "T": "They said: Sit down. Read it to us. And Baruch read every word to them."
    },
    "16": {
      "L": "And when they had heard all the words, they turned one to another in fear, and said to Baruch: We must surely report all these words to the king.",
      "M": "When they heard all the words, they turned to one another in alarm and said to Baruch: We must report all these words to the king.",
      "T": "When they had heard every word, they looked at one another in genuine alarm. Then they said to Baruch: We have to take this to the king — every word of it."
    },
    "17": {
      "L": "And they asked Baruch: Tell us, how did you write all these words? Was it from his mouth?",
      "M": "They asked Baruch: Tell us now — how did you write all these words? At his dictation?",
      "T": "Then they asked Baruch: Tell us — how did you write all this? Did Jeremiah dictate every word to you?"
    },
    "18": {
      "L": "And Baruch answered them: He pronounced all these words to me with his mouth, and I wrote them with ink in the scroll.",
      "M": "Baruch answered them: He dictated all these words to me, and I wrote them in ink on the scroll.",
      "T": "Baruch answered: Yes — he spoke every word to me, and I wrote it all down in ink on the scroll."
    },
    "19": {
      "L": "Then the officials said to Baruch: Go, hide yourself — you and Jeremiah — and let no man know where you are.",
      "M": "Then the officials said to Baruch: Go and hide — you and Jeremiah — and let no one know where you are.",
      "T": "The officials said to Baruch: Get out. Hide — you and Jeremiah both. Do not let anyone know where you have gone."
    },
    "20": {
      "L": "So they went into the court to the king, having deposited the scroll in the chamber of Elishama the secretary, and reported all the words in the ears of the king.",
      "M": "Then they went into the court to the king, after storing the scroll in the chamber of Elishama the secretary, and reported all the words to the king.",
      "T": "They stored the scroll in Elishama the secretary's chamber, then went into the inner court and reported everything to the king."
    },
    "21": {
      "L": "And the king sent Jehudi to get the scroll, and he took it from the chamber of Elishama the secretary; and Jehudi read it in the ears of the king and in the ears of all the officials who stood beside the king.",
      "M": "The king sent Jehudi to get the scroll, and he retrieved it from the chamber of Elishama the secretary. Jehudi read it in the hearing of the king and all the officials standing beside him.",
      "T": "The king sent Jehudi to get the scroll. Jehudi retrieved it from Elishama's chamber and read it aloud before the king and all the officials standing at his side."
    },
    "22": {
      "L": "Now the king was sitting in the winter house in the ninth month, and there was a fire burning before him on the fire pot.",
      "M": "The king was sitting in the winter apartment in the ninth month, and there was a fire burning before him in the fire pot.",
      "T": "It was the ninth month — midwinter. The king sat in his winter quarters with a fire burning in the fire pot before him."
    },
    "23": {
      "L": "And whenever Jehudi had read three or four columns, the king cut it with the scribe's knife and threw it into the fire that was in the fire pot, until all the scroll was consumed in the fire.",
      "M": "Each time Jehudi had read three or four columns, the king would cut the section off with a scribe's knife and throw it into the fire, until the entire scroll had been consumed in the fire.",
      "T": "Every three or four columns Jehudi read, the king took a scribe's knife, cut that section off, and threw it into the fire pot. Column by column, until the entire scroll was ash."
    },
    "24": {
      "L": "Yet neither the king nor any of his servants who heard all these words was afraid, nor did they tear their garments.",
      "M": "Yet neither the king nor any of his servants who heard all these words was afraid, nor did they tear their garments.",
      "T": "Not once did the king or any of his attendants flinch. Not one person tore their clothing. No one was afraid."
    },
    "25": {
      "L": "Even though Elnathan and Delaiah and Gemariah urged the king not to burn the scroll, he would not listen to them.",
      "M": "Even though Elnathan and Delaiah and Gemariah pleaded with the king not to burn the scroll, he would not listen to them.",
      "T": "Elnathan, Delaiah, and Gemariah urged the king not to burn the scroll — but he ignored them."
    },
    "26": {
      "L": "But the king commanded Jerahmeel the king's son and Seraiah the son of Azriel and Shelemiah the son of Abdeel to seize Baruch the scribe and Jeremiah the prophet; but the LORD hid them.",
      "M": "The king commanded Jerahmeel a royal prince, Seraiah son of Azriel, and Shelemiah son of Abdeel to seize Baruch the scribe and Jeremiah the prophet. But the LORD hid them.",
      "T": "Instead, the king ordered Jerahmeel — a prince of the court — along with Seraiah son of Azriel and Shelemiah son of Abdeel, to arrest Baruch the scribe and Jeremiah the prophet. But Yahweh had hidden them."
    },
    "27": {
      "L": "Now the word of the LORD came to Jeremiah, after the king had burned the scroll and the words that Baruch had written at the dictation of Jeremiah, saying:",
      "M": "After the king had burned the scroll with the words that Baruch had written at Jeremiah's dictation, the word of the LORD came to Jeremiah:",
      "T": "After the king burned the scroll — the one Baruch had written from Jeremiah's dictation — Yahweh's word came to Jeremiah:"
    },
    "28": {
      "L": "Take another scroll and write on it all the former words that were in the first scroll, which Jehoiakim king of Judah burned.",
      "M": "Take another scroll and write on it all the same words that were in the first scroll, the one Jehoiakim king of Judah burned.",
      "T": "Take another scroll. Write on it every word that was in the first scroll — the one Jehoiakim king of Judah burned."
    },
    "29": {
      "L": "And you shall say to Jehoiakim king of Judah: Thus says the LORD — You have burned this scroll, saying: Why have you written in it that the king of Babylon will certainly come and destroy this land and will cut off from it man and beast?",
      "M": "And concerning Jehoiakim king of Judah you shall say: Thus says the LORD — You burned this scroll, asking: Why have you written in it that the king of Babylon will certainly come and destroy this land, cutting off from it man and beast?",
      "T": "And to Jehoiakim king of Judah, say this: Yahweh says — You burned that scroll. You asked: Why did he write that Babylon's king will come and devastate this land and wipe out every person and animal from it?"
    },
    "30": {
      "L": "Therefore thus says the LORD concerning Jehoiakim king of Judah: He shall have no one to sit on the throne of David, and his dead body shall be cast out to the heat of the day and the frost of the night.",
      "M": "Therefore thus says the LORD concerning Jehoiakim king of Judah: He will have no one to sit on the throne of David, and his dead body will be cast out to the heat of the day and the frost of the night.",
      "T": "So this is what Yahweh says about Jehoiakim king of Judah: Not one of his line will sit on David's throne. His body will be flung out — exposed to the burning heat by day and the hard frost by night."
    },
    "31": {
      "L": "And I will punish him and his seed and his servants for their iniquity, and I will bring upon them and upon the inhabitants of Jerusalem and upon the men of Judah all the disaster that I have pronounced against them, but they have not listened.",
      "M": "I will punish him and his offspring and his servants for their iniquity. I will bring upon them, and upon the inhabitants of Jerusalem, and upon the people of Judah, all the disaster I have pronounced against them — for they would not listen.",
      "T": "I will bring punishment on him, on his descendants, and on his court for their iniquity. Every disaster I pronounced against them — on them, on all Jerusalem, on all Judah — I will bring it. Because they would not listen."
    },
    "32": {
      "L": "Then Jeremiah took another scroll and gave it to Baruch the son of Neriah the scribe, who wrote on it at the dictation of Jeremiah all the words of the scroll that Jehoiakim king of Judah had burned in the fire; and many similar words were added to them.",
      "M": "Then Jeremiah took another scroll and gave it to Baruch son of Neriah the scribe, who wrote on it at Jeremiah's dictation all the words of the scroll that Jehoiakim king of Judah had burned. And many similar words were added to them.",
      "T": "Jeremiah took another scroll and gave it to Baruch son of Neriah the scribe. Baruch wrote down at Jeremiah's dictation every word that had been in the scroll Jehoiakim king of Judah burned. And many more words of the same kind were added."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 33–36 written.')

if __name__ == '__main__':
    main()
