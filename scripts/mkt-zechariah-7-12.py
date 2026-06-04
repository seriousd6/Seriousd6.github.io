"""
MKT Zechariah chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-zechariah-7-12.py

=== BOOK OVERVIEW ===

Zechariah prophesied in Jerusalem during the reign of Darius I (520–518 BCE),
contemporary with Haggai. The book divides sharply:

  Chapters 1–8  — Dated oracles with eight night visions (520–518 BCE)
  Chapters 9–14 — Two undated "burdens" (massa', oracles); most scholars call
                  these Deutero-Zechariah; canonical reading treats them as the
                  same book's eschatological climax.

This script covers chapters 7–12:

  7:1–14   — Question about fasting; the prophetic indictment (fourth year of Darius)
  8:1–23   — Promise of restoration: Jerusalem repopulated, the nations drawn in
  9:1–17   — First oracle: Yahweh's advance on the nations; the king on the donkey
  10:1–12  — Condemnation of false shepherds; gathering of the scattered
  11:1–17  — The two-staff allegory; the thirty pieces of silver
  12:1–14  — Second oracle: siege of Jerusalem; the pierced one; national mourning

=== TEXTUAL NOTES ===

- 7:9: H2617 (ḥesed) — "steadfast love." The word denotes covenant loyalty that
  expresses itself in active kindness; no English word captures both dimensions.
- 8:2: H7065 (qin'ah, jealousy/zeal) — covenant jealousy, the language of
  marriage fidelity. Not pettiness but exclusive covenantal claim.
- 9:9: H6662 (tsaddiq) + H3467 passive ptcp. (nôsha', "having salvation /
  victorious") — the king is both just and the beneficiary of divine deliverance.
  The passive "having salvation" (KJV) is more precise than "victorious" but both
  are defensible. I render L as the Hebrew syntax; M/T clarify the sense.
- 9:13: H3120 (Yavan, Greece/Javan) — the historical Greeks. In context this is
  the Hellenistic powers; the oracle looks beyond Persia to the next empire.
- 11:12–13: The thirty pieces of silver thrown to the potter in the house of the
  LORD. Cited in Matt 27:9–10 (attributed to "Jeremiah," which is a famous crux —
  Matthew may be following a canonical order in which Jeremiah headed the Prophets,
  or conflating Jer 32 with Zech 11). The translation makes the Zechariah text plain.
- 12:1: H7307 (ruach) — "spirit of man within him." This is the human inner life
  that Yahweh forms; lowercase throughout in this verse.
- 12:10: H1856 (daqar, to pierce/thrust through). The pronoun shift "look on me...
  mourn for him" is in the MT and is not smoothed over. The T tier notes the NT
  citation (John 19:37, Rev 1:7). The antecedent of "him" (the pierced one) is
  intentionally compressed in the MT; the T tier reflects that compression.
- 12:11: Hadadrimmon in the valley of Megiddo — a mourning rite for a slain deity
  (Hadad/Rimmon) or for King Josiah's death at Megiddo (2 Chr 35:24–25). Either
  reading points to the deepest grief the culture knew.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention) throughout.
  T: "Yahweh" in direct speech, oracle closings, and theological high points;
     "the LORD" in narrative transitions. Consistent with Haggai, Zephaniah,
     Habakkuk, and all prior Minor Prophets in this series.

- H6635 (צְבָאוֹת / tseba'ot, hosts):
  L/M: "of hosts" (standard formula: "LORD of hosts").
  T: "of Armies" — the divine warrior epithet made concrete. Consistent with prior
     Minor Prophet scripts.

- H430 (אֱלֹהִים / Elohim):
  Rendered "God" throughout. Context does not require tier differentiation.

- H7307 (רוּחַ / ruach):
  12:1 — "spirit of man within him" (human inner life God forms) — lowercase.
  12:10 — "spirit of grace and supplications" (divine gift poured out) — lowercase
  "spirit" because the text points to a disposition/outpouring, not to the
  Spirit as a person. Capitalized "Spirit" would over-read the Hebrew at this point,
  though the NT applies it christologically (John 7:39 context).

- H2617 (חֶסֶד / ḥesed):
  7:9 — L/M: "steadfast love"; T: "covenant loyalty."

- H4853 (מַשָּׂא / massa'):
  9:1, 12:1 — L: "burden"; M/T: "oracle." The burden-oracle formula opens the two
  major eschatological sections; "oracle" is more transparent in M/T.

- H7965 (שָׁלוֹם / shalom):
  Rendered "peace" in L/M; T expands when the context requires wholeness/flourishing
  rather than just cessation of conflict (e.g., 8:19: "love truth and peace").

- Covenant-curse echoes in ch. 7: The rhetoric of refused hearing and scattering
  echoes Deut 28–29 and is conveyed by accurate rendering without paraphrase.
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

ZECHARIAH = {
  "7": {
    "1": {
      "L": "And it came to pass in the fourth year of King Darius, on the fourth day of the ninth month — that is, Chislev — that the word of the LORD came to Zechariah.",
      "M": "In the fourth year of King Darius, on the fourth day of the ninth month — Chislev — the word of the LORD came to Zechariah.",
      "T": "Two years after the visions of chapters 1–6 — in the fourth year of Darius, on the fourth day of the ninth month, Chislev — the word of Yahweh came to Zechariah."
    },
    "2": {
      "L": "Now Bethel had sent Sharezer and Regemmelech and their men to entreat the favor of the LORD,",
      "M": "The people of Bethel had sent Sharezer and Regemmelech, together with their men, to seek the LORD's favor,",
      "T": "The community of Bethel had dispatched two envoys — Sharezer and Regemmelech — along with their delegation, to make supplication before Yahweh,"
    },
    "3": {
      "L": "and to speak to the priests of the house of the LORD of hosts and to the prophets, saying, 'Should I weep and fast in the fifth month, as I have done these many years?'",
      "M": "to speak to the priests of the house of the LORD of Hosts and to the prophets with this question: 'Should I mourn and fast in the fifth month as I have done for so many years?'",
      "T": "bearing a question for the priests of the temple of Yahweh of Armies and for the prophets: 'Should I continue the fast of the fifth month — the fast I have kept, year after year, through all these decades since Jerusalem fell?'"
    },
    "4": {
      "L": "Then the word of the LORD of hosts came to me, saying,",
      "M": "Then the word of the LORD of Hosts came to me:",
      "T": "Yahweh of Armies had an answer. His word came to me:"
    },
    "5": {
      "L": "'Speak to all the people of the land and to the priests: When you fasted and mourned in the fifth and seventh months these seventy years, was it indeed for me that you fasted?'",
      "M": "'Tell all the people of the land and the priests: When you fasted and mourned in the fifth and the seventh months for these seventy years, was it truly for me that you were fasting?'",
      "T": "'Say this to all the people of the land and to the priests: For seventy years you have kept the fast of the fifth month and wept through the seventh. But was any of it really for me? Or was it, all along, for yourselves?'"
    },
    "6": {
      "L": "And when you eat and when you drink, is it not you who eat, and you who drink?",
      "M": "When you eat and when you drink, is it not for yourselves that you eat and drink?",
      "T": "Your feasts are for yourselves. Your fasts are for yourselves. Every ritual turned inward. I was never the audience."
    },
    "7": {
      "L": "Are these not the words that the LORD proclaimed through the former prophets, when Jerusalem was inhabited and at ease, with its surrounding cities, and the Negev and the Shephelah were inhabited?",
      "M": "Are these not the words the LORD announced through the earlier prophets when Jerusalem was inhabited and prosperous, along with the surrounding towns, the Negev, and the Shephelah?",
      "T": "What I am saying is not new. The former prophets said exactly this when Jerusalem was full and thriving, when the towns of the Negev and the Shephelah were alive with people. You had the same choice then."
    },
    "8": {
      "L": "And the word of the LORD came to Zechariah, saying,",
      "M": "The word of the LORD came to Zechariah:",
      "T": "The word of Yahweh came to Zechariah:"
    },
    "9": {
      "L": "Thus says the LORD of hosts: Render true judgments, show steadfast love and mercy to one another,",
      "M": "This is what the LORD of Hosts says: Administer true justice; show steadfast love and compassion to one another.",
      "T": "Yahweh of Armies said this: Judge honestly. Practice covenant loyalty and tender mercy toward each other."
    },
    "10": {
      "L": "do not oppress the widow, the fatherless, the sojourner, or the poor, and do not devise evil against one another in your hearts.",
      "M": "Do not oppress the widow or the fatherless, the immigrant or the poor. Do not plot evil in your hearts against your neighbor.",
      "T": "Stop crushing the vulnerable — the widow, the orphan, the immigrant, the poor. Stop nursing schemes against your neighbor in the private quiet of your own heart."
    },
    "11": {
      "L": "But they refused to pay attention and turned a stubborn shoulder, and stopped their ears that they might not hear.",
      "M": "But they refused to listen; they turned a stubborn shoulder and stopped their ears against hearing.",
      "T": "But they would not listen. They pulled away, stiff-necked. They covered their ears against the word."
    },
    "12": {
      "L": "They made their hearts like flint lest they should hear the law and the words that the LORD of hosts had sent by his Spirit through the former prophets. Therefore great wrath came from the LORD of hosts.",
      "M": "They made their hearts as hard as flint, refusing to hear the law and the words that the LORD of Hosts sent by his Spirit through the former prophets. So the LORD of Hosts poured out his fierce anger.",
      "T": "They turned their hearts to stone — harder than flint — so that the law could not penetrate, so that the words Yahweh's own Spirit had sent through the former prophets could find no entrance. And so: great wrath, from Yahweh of Armies himself."
    },
    "13": {
      "L": "As I called and they would not hear, so they called and I would not hear, says the LORD of hosts,",
      "M": "Just as they did not listen when I called, so I did not listen when they called, says the LORD of Hosts,",
      "T": "They would not answer when I called. I did not answer when they cried. The symmetry is exact. Yahweh of Armies has spoken."
    },
    "14": {
      "L": "and I scattered them with a whirlwind among all the nations they had not known. Thus the land was desolate behind them, so that no one went to or fro, for they had made the pleasant land a desolation.",
      "M": "so I scattered them with a whirlwind among all the nations they had not known. The land they left behind was desolated — no one passed through, no one came back — for they had turned a delightful land into wasteland.",
      "T": "I swept them away — a whirlwind scattering them to nations they had never heard of. And the land they left behind fell silent. No one traveled through it. No one returned. The land they had called delightful lay empty and ruined. They had made it so."
    }
  },
  "8": {
    "1": {
      "L": "And the word of the LORD of hosts came, saying,",
      "M": "The word of the LORD of Hosts came:",
      "T": "The word of Yahweh of Armies came:"
    },
    "2": {
      "L": "Thus says the LORD of hosts: I am jealous for Zion with great jealousy, and I am jealous for her with great wrath.",
      "M": "This is what the LORD of Hosts says: I am burning with jealousy for Zion — great jealousy — and I am stirred with great fury on her behalf.",
      "T": "Yahweh of Armies says: I burn for Zion with the fire of a husband who will not release his claim. My jealousy is enormous. My fury on her behalf is fierce."
    },
    "3": {
      "L": "Thus says the LORD: I have returned to Zion and will dwell in the midst of Jerusalem. Jerusalem shall be called the city of faithfulness, and the mountain of the LORD of hosts, the holy mountain.",
      "M": "This is what the LORD says: I have returned to Zion and will live in Jerusalem. Jerusalem will be called the faithful city, and the mountain of the LORD of Hosts will be called the holy mountain.",
      "T": "Yahweh says: I have come back to Zion. I will make my home in Jerusalem. And the city will carry the name it truly deserves: the faithful city. The mountain where I dwell will be called what it truly is: the holy mountain, the mountain of Yahweh of Armies."
    },
    "4": {
      "L": "Thus says the LORD of hosts: Old men and old women shall again sit in the streets of Jerusalem, each with staff in hand because of great age.",
      "M": "This is what the LORD of Hosts says: Old men and old women will once again sit in the streets of Jerusalem, each with a staff in hand because of their age.",
      "T": "Yahweh of Armies says: Old men and women, white-haired and unhurried, will sit in Jerusalem's streets again — staffs in hand, simply because they have lived long enough to need them."
    },
    "5": {
      "L": "And the streets of the city shall be full of boys and girls playing in its streets.",
      "M": "The streets of the city will be full of boys and girls playing in the streets.",
      "T": "And the streets that were empty will ring again with children's voices — boys and girls running and playing, unafraid."
    },
    "6": {
      "L": "Thus says the LORD of hosts: If it is marvelous in the eyes of the remnant of this people in those days, should it also be marvelous in my eyes? declares the LORD of hosts.",
      "M": "This is what the LORD of Hosts says: Even if this seems impossible to the remnant of this people in those days, should it therefore seem impossible to me? declares the LORD of Hosts.",
      "T": "Yahweh of Armies says: Yes — to the remnant, to people who have seen what they have seen, this sounds too good to be true. But is anything too difficult for me? The question hangs in the air. Yahweh of Armies has asked it."
    },
    "7": {
      "L": "Thus says the LORD of hosts: Behold, I will save my people from the east country and from the west country,",
      "M": "This is what the LORD of Hosts says: I will rescue my people from the lands of the east and the lands of the west.",
      "T": "Yahweh of Armies says: Watch. I am going to bring my people home — from the east, from the west, from every direction they were scattered."
    },
    "8": {
      "L": "and I will bring them to dwell in the midst of Jerusalem. And they shall be my people, and I will be their God, in faithfulness and in righteousness.",
      "M": "I will bring them home to live in Jerusalem. They will be my people, and I will be their God, in faithfulness and righteousness.",
      "T": "I will bring them back. They will live in Jerusalem. And the covenant formula will be fulfilled at last — they will be my people and I will be their God — grounded not in aspiration but in faithfulness and right-standing before me."
    },
    "9": {
      "L": "Thus says the LORD of hosts: Let your hands be strong, you who in these days are hearing these words from the mouths of the prophets who were present on the day that the foundation of the house of the LORD of hosts was laid, that the temple might be built.",
      "M": "This is what the LORD of Hosts says: Be strong, all of you who are hearing these words today from the prophets who were present when the foundation of the house of the LORD of Hosts was laid, so that the temple might be built.",
      "T": "Yahweh of Armies says: Take courage — every one of you listening to these words, spoken by the prophets who were there when the foundation of this house was laid. You are not starting from nothing. You are finishing something."
    },
    "10": {
      "L": "For before those days there was no wage for man or beast, nor was there any safety from the foe for him who went out or came in, for I set every man against his neighbor.",
      "M": "Before those days, there was no wages for people or animals, no security for anyone who came or went — because I had set everyone against their neighbors.",
      "T": "Before those days — you remember — no one earned enough. Neither worker nor beast saw a fair return. No one was safe stepping outside or coming home. I myself had set neighbor against neighbor. Those were the consequences of abandonment. They are finished."
    },
    "11": {
      "L": "But now I will not deal with the remnant of this people as in the former days, declares the LORD of hosts.",
      "M": "But from now on I will not deal with the remnant of this people as I did in the past, declares the LORD of Hosts.",
      "T": "But that is done. Yahweh of Armies declares it: I will not treat this remnant the way I treated those who came before them. The past does not repeat."
    },
    "12": {
      "L": "For there shall be a sowing of peace. The vine shall give its fruit, the ground shall give its produce, and the heavens shall give their dew. And I will cause the remnant of this people to possess all these things.",
      "M": "For there will be a sowing of peace. The vine will yield its fruit, the ground will produce its crops, and the sky will give its dew. I will cause the remnant of this people to inherit all these things.",
      "T": "In place of the curse: a seed of wholeness planted in the ground. The vine will produce again. The earth will release what it had withheld. The sky will give its dew. And this remnant — these survivors — will receive it all as their inheritance."
    },
    "13": {
      "L": "And as you have been a byword of cursing among the nations, O house of Judah and house of Israel, so will I save you, and you shall be a blessing. Fear not; let your hands be strong.",
      "M": "Just as you, house of Judah and house of Israel, were a curse among the nations, so I will save you, and you will be a blessing. Do not be afraid; let your hands be strong.",
      "T": "You became a byword of disaster — 'May you end up like Judah and Israel.' That curse is about to reverse. I will save you. You will become the blessing — the nations will say, 'May you flourish as they do.' So: do not be afraid. Strengthen your hands."
    },
    "14": {
      "L": "For thus says the LORD of hosts: As I purposed to bring disaster upon you when your fathers provoked me to anger, and I did not relent, says the LORD of hosts,",
      "M": "For this is what the LORD of Hosts says: Just as I determined to bring disaster upon you when your ancestors provoked me to anger, and I did not relent, says the LORD of Hosts,",
      "T": "Here is the logic Yahweh of Armies presents: When your ancestors provoked me, I set myself to bring calamity on them. I said it and I did not turn back."
    },
    "15": {
      "L": "so again in these days I have purposed to do good to Jerusalem and to the house of Judah. Fear not.",
      "M": "so in these days I have determined again to do good to Jerusalem and the house of Judah. Do not be afraid.",
      "T": "By that same resolve — that same unyielding purpose — I have now determined to do good to Jerusalem and Judah. The very quality that made the judgment certain makes the promise sure. Do not be afraid."
    },
    "16": {
      "L": "These are the things that you shall do: Speak truth to one another; render judgments in your gates that are true and that make for peace;",
      "M": "These are the things you must do: Speak the truth to one another. Render honest judgments that lead to peace in your courts.",
      "T": "And here is what you are to do in response: Tell each other the truth. In your courts, judge with integrity — judgments that are true and that build peace, not judgments that protect the powerful or settle old scores."
    },
    "17": {
      "L": "do not devise evil in your hearts against one another, and love no false oath, for all these things I hate, declares the LORD.",
      "M": "Do not plot evil against your neighbor in your heart, and do not love perjury, for all these things I hate, declares the LORD.",
      "T": "Stop nursing evil schemes against your neighbors in the quiet of your own heart. Stop taking false oaths. I hate all of this — Yahweh declares it — with a deep and settled hatred."
    },
    "18": {
      "L": "And the word of the LORD of hosts came to me, saying,",
      "M": "The word of the LORD of Hosts came to me:",
      "T": "The word of Yahweh of Armies came to me:"
    },
    "19": {
      "L": "Thus says the LORD of hosts: The fast of the fourth month, and the fast of the fifth, and the fast of the seventh, and the fast of the tenth shall be to the house of Judah seasons of joy and gladness and cheerful feasts. Therefore love truth and peace.",
      "M": "This is what the LORD of Hosts says: The fasts of the fourth, fifth, seventh, and tenth months will become occasions of joy, gladness, and happy festivals for the house of Judah. So love truth and peace.",
      "T": "Yahweh of Armies says: Those four fasts — the calendar of grief and commemoration — they will all become feasts. Gladness. Celebration. Joy. So love truth. Love peace. That is where the transformation begins."
    },
    "20": {
      "L": "Thus says the LORD of hosts: Peoples shall yet come, even the inhabitants of many cities;",
      "M": "This is what the LORD of Hosts says: Peoples will yet come — inhabitants of many cities —",
      "T": "Yahweh of Armies says: The day is coming. Peoples will come. Cities upon cities will send their residents on pilgrimage."
    },
    "21": {
      "L": "the inhabitants of one city shall go to another, saying, 'Let us go at once to entreat the favor of the LORD and to seek the LORD of hosts; I myself am going.'",
      "M": "The inhabitants of one city will go to another, saying, 'Let us go immediately to seek the LORD's favor and to seek the LORD of Hosts. I'm going too.'",
      "T": "One city will call to another: 'Let's go — right now — to seek Yahweh's favor, to seek Yahweh of Armies. I am not waiting. I am going.' And they will go."
    },
    "22": {
      "L": "Many peoples and strong nations shall come to seek the LORD of hosts in Jerusalem and to entreat the favor of the LORD.",
      "M": "Many peoples and powerful nations will come to seek the LORD of Hosts in Jerusalem and to seek the LORD's favor.",
      "T": "Nation after nation — mighty nations — will come to Jerusalem to seek Yahweh of Armies, to entreat his favor."
    },
    "23": {
      "L": "Thus says the LORD of hosts: In those days ten men from all the nations of every tongue shall take hold of the robe of a Jew, saying, 'Let us go with you, for we have heard that God is with you.'",
      "M": "This is what the LORD of Hosts says: In those days ten men from every nation and language will take hold of the robe of one Jew, saying, 'Let us go with you, for we have heard that God is with you.'",
      "T": "Yahweh of Armies says: When that day comes, ten men from every tongue on earth will grab the coat of one Jewish person and say: 'Take us with you. We have heard it — God is with you.' That is how this age ends."
    }
  },
  "9": {
    "1": {
      "L": "The burden of the word of the LORD: against the land of Hadrach, and Damascus is its resting place. For the eyes of all people, even of all the tribes of Israel, are toward the LORD,",
      "M": "An oracle — the word of the LORD against the land of Hadrach; Damascus is where it comes to rest. For the eyes of all humanity, and of all Israel's tribes, are fixed on the LORD,",
      "T": "An oracle: the word of Yahweh hangs heavy over the land of Hadrach. It will settle and rest on Damascus — for every human eye, and every eye in Israel, is fixed on Yahweh."
    },
    "2": {
      "L": "as well as Hamath, which borders on it, Tyre and Sidon, though they are very wise.",
      "M": "and also Hamath, which borders Damascus, Tyre and Sidon, though they are very clever.",
      "T": "The word reaches Hamath on the border, and south to Tyre and Sidon — those shrewd cities, wise in their own estimation."
    },
    "3": {
      "L": "Tyre has built herself a stronghold and heaped up silver like dust and fine gold like the mud of the streets.",
      "M": "Tyre has built herself a fortress and amassed silver like dust and gold like the mud of the streets.",
      "T": "Tyre built herself into an island fortress. She stacked silver like dirt, piled gold like street mud. She thought wealth could be a wall."
    },
    "4": {
      "L": "But behold, the Lord will strip her of her possessions and strike down her power in the sea, and she shall be consumed by fire.",
      "M": "But look — the Lord will dispossess her and hurl her wealth into the sea, and she will be consumed by fire.",
      "T": "But the Lord has seen it. He will seize what she hoarded and cast her power into the sea. Fire will finish what remains."
    },
    "5": {
      "L": "Ashkelon shall see it and be afraid; Gaza too, and shall writhe in anguish; Ekron also, for its hope has withered. The king shall perish from Gaza; Ashkelon shall not be inhabited;",
      "M": "Ashkelon will see it and be terrified; Gaza too, writhing in anguish; and Ekron, for its hope has withered. Gaza will lose its king, and Ashkelon will be deserted.",
      "T": "Ashkelon will watch and tremble. Gaza will see it and convulse. Ekron's confidence will collapse — all it had hoped for, gone. Gaza's king will vanish. Ashkelon will empty out."
    },
    "6": {
      "L": "a mixed people shall dwell in Ashdod, and I will cut off the pride of the Philistines.",
      "M": "a mixed people will settle in Ashdod, and I will cut off Philistia's pride.",
      "T": "A mongrel population will fill Ashdod. The ancestral pride of the Philistines will be sheared away."
    },
    "7": {
      "L": "I will take away its blood from its mouth, and its abominations from between its teeth; it too shall be a remnant for our God; it shall be like a clan in Judah, and Ekron shall be like the Jebusites.",
      "M": "I will strip the blood from its mouth and the forbidden offerings from between its teeth. Even they will belong to our God; they will become like a clan within Judah, and Ekron will be like the Jebusites.",
      "T": "I will take the blood-offerings from their mouths, the idol-food from between their teeth. And even this people — even the Philistines — can become part of what belongs to our God. Absorbed like a clan of Judah. Ekron will be like the Jebusites of old: once outside, then woven in."
    },
    "8": {
      "L": "Then I will encamp around my house as a guard, so that none shall march to and fro; no oppressor shall again pass over them, for now I see with my own eyes.",
      "M": "I will take up position around my house as a garrison, so that no army marches through it again. No oppressor will overrun them again, for I am watching with my own eyes.",
      "T": "And I will take my post around my own house — a guard of one, yet sufficient. No army will sweep through again. No oppressor will march over my people. I am watching now with my own eyes open."
    },
    "9": {
      "L": "Rejoice greatly, O daughter of Zion! Shout aloud, O daughter of Jerusalem! Behold, your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey, on a colt, the foal of a donkey.",
      "M": "Rejoice greatly, Daughter Zion! Shout aloud, Daughter Jerusalem! See — your king is coming to you, righteous and victorious, humble and riding on a donkey, on a colt, the foal of a donkey.",
      "T": "Shout for joy, Daughter Zion! Cry it aloud, Jerusalem! Your king is on his way — and look at how he comes: just, and saved by God himself; humble, not on a warhorse but on a donkey's colt. This is what a true king looks like."
    },
    "10": {
      "L": "I will cut off the chariot from Ephraim and the war horse from Jerusalem; and the battle bow shall be cut off, and he shall speak peace to the nations; his rule shall be from sea to sea, and from the River to the ends of the earth.",
      "M": "He will cut off the chariot from Ephraim and the war horse from Jerusalem; the battle bow will be cut off. He will proclaim peace to the nations; his dominion will extend from sea to sea, from the River to the ends of the earth.",
      "T": "The instruments of war will be dismantled: chariots, warhorses, battle bows — all taken away. Not because peace was negotiated but because it was given. He will speak peace to every nation, and his reign will stretch from ocean to ocean, from the great River to the edges of the earth."
    },
    "11": {
      "L": "As for you also, because of the blood of my covenant with you, I will set your prisoners free from the waterless pit.",
      "M": "As for you — because of the blood of my covenant with you — I will free your prisoners from the waterless pit.",
      "T": "And for you, Jerusalem — for the sake of the covenant sealed in blood — I will release your prisoners from the dry pit where there is no water. The covenant holds. The blood speaks."
    },
    "12": {
      "L": "Return to the stronghold, O prisoners of hope; today I declare that I will restore to you double.",
      "M": "Return to the stronghold, you prisoners who still have hope; today I declare that I will restore double to you.",
      "T": "Come back — come back to the fortress, you who are captives but still carry hope. Yahweh declares it today: double will be restored. For everything taken, twice as much returned."
    },
    "13": {
      "L": "For I have bent Judah as my bow; I have made Ephraim its arrow. I will stir up your sons, O Zion, against your sons, O Greece, and wield you like a warrior's sword.",
      "M": "For I have bent Judah like a bow; I have made Ephraim its arrow. I will rouse your sons, Zion, against the sons of Greece, and wield you like a warrior's sword.",
      "T": "Judah is the bow I have bent. Ephraim is the arrow I have set to the string. Zion's sons I will rouse against the sons of Greece — and I will wield you like the sword of a warrior. You are my weapon."
    },
    "14": {
      "L": "Then the LORD will appear over them, and his arrow will go forth like lightning; the Lord GOD will sound the trumpet and march forth in the whirlwinds of the south.",
      "M": "The LORD will appear over them; his arrow will flash like lightning. The Lord GOD will sound the trumpet and advance in the windstorms of the south.",
      "T": "Then Yahweh himself will appear above them — his arrow shooting like lightning from the sky. The Lord Yahweh will sound the ram's horn and march forward in the storm winds of the south. The divine warrior has entered the field."
    },
    "15": {
      "L": "The LORD of hosts will shield them, and they shall devour and tread down the sling stones, and they shall drink and roar as if drunk with wine, and be full like a bowl, drenched like the corners of the altar.",
      "M": "The LORD of Hosts will shield them. They will devour and trample the sling stones; they will drink and shout as with wine, full as a sacrificial basin, drenched like the corners of the altar.",
      "T": "Yahweh of Armies stands over them as a shield. They will surge forward — consuming, trampling — exultant as warriors flush with wine. They will be filled like the blood-bowls of the altar, saturated like the altar's corners at the great sacrifice."
    },
    "16": {
      "L": "On that day the LORD their God will save them as the flock of his people; for like the jewels of a crown they shall shine on his land.",
      "M": "On that day the LORD their God will save them as his people's flock. They will gleam like gems in a crown over his land.",
      "T": "On that day Yahweh their God will rescue them — the flock he has always owned. And they will be displayed over the land like gemstones set in a crown, catching the light for all to see."
    },
    "17": {
      "L": "For how great is his goodness, and how great is his beauty! Grain shall make the young men flourish, and new wine the young women.",
      "M": "How great is his goodness, how great is his beauty! Grain will strengthen the young men, and new wine will cheer the young women.",
      "T": "What goodness — what beauty — belongs to Yahweh! Grain will give the young men strength to grow tall. New wine will bring the young women to joy. Life, flourishing, abundance — all from his hand."
    }
  },
  "10": {
    "1": {
      "L": "Ask rain from the LORD in the season of the spring rain, from the LORD who makes the storm clouds, and he will give showers of rain, to everyone the vegetation of the field.",
      "M": "Ask rain from the LORD in the season of the spring rain. The LORD is the one who makes the storm clouds; he will give them showers of rain, growth to everyone in the field.",
      "T": "Ask Yahweh for rain — ask in the season when rain is needed, when the spring rains are due. He is the one who builds the storm clouds. He will answer with showers, with green across every field."
    },
    "2": {
      "L": "For the household idols speak vanity, and the diviners see lying visions and tell false dreams and give empty consolation. Therefore the people wander like sheep; they are afflicted for lack of a shepherd.",
      "M": "For the household idols speak worthlessness, and the diviners see false visions; they tell lying dreams and give empty comfort. Therefore the people wander like sheep; they suffer because there is no shepherd.",
      "T": "But instead they have been going to the household idols — gods that speak only nonsense. The diviners see visions that are false, dream dreams that are lies, and give comfort that leaves everyone empty. And so the people drift, bewildered as sheep with no one to lead them — and they have suffered for it."
    },
    "3": {
      "L": "My anger is hot against the shepherds, and I will punish the leaders; for the LORD of hosts cares for his flock, the house of Judah, and will make them like his majestic horse in battle.",
      "M": "My anger burns against the shepherds, and I will punish the leaders; for the LORD of Hosts tends his flock, the house of Judah, and will make them like his majestic steed in battle.",
      "T": "My anger burns against those who were supposed to shepherd — the leaders who fed themselves instead of the flock. I will deal with them. Because Yahweh of Armies has not abandoned Judah — they are still his flock — and he will transform them into a magnificent warhorse."
    },
    "4": {
      "L": "From him shall come the cornerstone, from him the tent peg, from him the battle bow, from him every ruler — all of them together.",
      "M": "From Judah will come the cornerstone, from him the tent peg, from him the battle bow, from him every ruler — all of them together.",
      "T": "From Judah — from this very people — the cornerstone will come: the founding stone of what is built. From him the tent peg that holds the structure firm. From him the battle bow. From him every leader that matters. All that the nation needs rises from within."
    },
    "5": {
      "L": "They shall be like mighty warriors in battle, treading down the foe in the mud of the streets; they shall fight because the LORD is with them, and they shall shame the riders on horses.",
      "M": "Together they will be like mighty warriors in battle, trampling their enemies in the street mud. They will fight because the LORD is with them, and they will put the horsemen to shame.",
      "T": "Together they will be warriors — trampling enemies into the mud. They will fight, and they will win, because Yahweh is with them. Even the proud cavalry will be put to shame."
    },
    "6": {
      "L": "I will strengthen the house of Judah, and I will save the house of Joseph. I will bring them back because I have mercy on them, and they shall be as though I had not rejected them, for I am the LORD their God and I will answer them.",
      "M": "I will strengthen the house of Judah and save the house of Joseph. I will bring them back, for I have compassion on them. They will be as though I had never rejected them, for I am the LORD their God and I will answer them.",
      "T": "I will give Judah its strength back. I will rescue the house of Joseph. I will bring them home, because my compassion for them has not dried up. They will be restored as if the rejection had never happened — as if they had never been cast away. For I am Yahweh their God. And I will hear them when they call."
    },
    "7": {
      "L": "Then Ephraim shall be like a mighty warrior, and their heart shall rejoice as with wine. Their children shall see it and be glad; their hearts shall rejoice in the LORD.",
      "M": "Ephraim will be like a mighty warrior, and their hearts will rejoice as with wine. Their children will see it and rejoice; their hearts will exult in the LORD.",
      "T": "Ephraim will become a warrior nation again — hearts bursting with joy like a man who has drunk deeply. Their children will witness it and join the exultation. Their hearts will overflow in Yahweh."
    },
    "8": {
      "L": "I will whistle for them and gather them in, for I have redeemed them, and they shall be as many as they were before.",
      "M": "I will signal for them and gather them, for I have redeemed them; they will be as numerous as before.",
      "T": "I will whistle — one signal — and they will come. I have already redeemed them. They will multiply again until they are as numerous as they ever were."
    },
    "9": {
      "L": "Though I scattered them among the nations, yet in far countries they shall remember me, and with their children they shall live and return.",
      "M": "Though I scattered them among the nations, they will remember me even in distant countries; they will survive with their children and return.",
      "T": "I scattered them — yes — but even in the distant countries, even in exile, memory will hold them. They will remember me. They will raise children. And they will come back."
    },
    "10": {
      "L": "I will bring them home from the land of Egypt, and gather them from Assyria, and I will bring them to the land of Gilead and to Lebanon, until there is no room for them.",
      "M": "I will bring them back from Egypt and gather them from Assyria. I will settle them in Gilead and Lebanon until there is no room for them.",
      "T": "From Egypt I will bring them. From Assyria I will gather them. I will settle them in Gilead and Lebanon — until the land cannot hold them all."
    },
    "11": {
      "L": "He shall pass through the sea of trouble and strike down the waves of the sea, and all the depths of the Nile shall dry up. The pride of Assyria shall be brought down, and the scepter of Egypt shall depart.",
      "M": "He will pass through the sea of distress and strike down the waves; all the depths of the Nile will dry up. The pride of Assyria will be brought low, and the scepter of Egypt will depart.",
      "T": "He will march through the sea of anguish — striking the waves, parting the waters again as at the Exodus. The Nile's deepest channels will go dry. The pride of Assyria will be crushed to earth. Egypt's staff of power will be stripped away. The old oppressors will yield."
    },
    "12": {
      "L": "I will make them strong in the LORD, and they shall walk in his name, declares the LORD.",
      "M": "I will strengthen them in the LORD, and they will walk in his name, declares the LORD.",
      "T": "I will give them strength — and it will be strength rooted in Yahweh himself. They will live inside his name, move inside his name. Yahweh has declared it."
    }
  },
  "11": {
    "1": {
      "L": "Open your doors, O Lebanon, that the fire may devour your cedars!",
      "M": "Open your doors, Lebanon, so that fire may devour your cedars!",
      "T": "Lebanon — throw open your gates! Fire is coming for your cedars."
    },
    "2": {
      "L": "Wail, O cypress, for the cedar has fallen, for the glorious trees are ruined! Wail, O oaks of Bashan, for the dense forest has come down!",
      "M": "Wail, cypress tree, for the cedar has fallen; the majestic trees are destroyed! Wail, oaks of Bashan, for the dense forest has come down!",
      "T": "Cry, cypress trees — the cedar has fallen. Grieve what once was glorious and is now wreckage. Wail, oaks of Bashan — the whole thick forest has come down."
    },
    "3": {
      "L": "The sound of the wail of the shepherds, for their glory is ruined! The sound of the roar of the lions, for the thicket of the Jordan is ruined!",
      "M": "Listen to the cry of the shepherds — their splendor is destroyed! Listen to the roar of the young lions — the jungle of the Jordan is devastated!",
      "T": "That sound is the shepherds wailing — their lush pastures, their pride, gone. That other sound is the lions roaring — the dense thickets of the Jordan, their home, stripped bare."
    },
    "4": {
      "L": "Thus says the LORD my God: Shepherd the flock doomed to slaughter.",
      "M": "This is what the LORD my God says: Shepherd the flock marked for slaughter.",
      "T": "Yahweh my God said this to me: 'Take up the staff. Shepherd the flock. But know what you are walking into — this is the flock already marked for slaughter.'"
    },
    "5": {
      "L": "Their buyers slay them and go unpunished, and those who sell them say, 'Blessed be the LORD, for I have become rich,' and their own shepherds do not pity them.",
      "M": "Their buyers slaughter them without guilt. Those who sell them say, 'Praise the LORD — I have become rich!' And their own shepherds show them no mercy.",
      "T": "The buyers butcher them and feel no guilt. The sellers pocket the profit and thank God for their wealth. And the ones who should have protected them — their very own shepherds — have not a drop of compassion."
    },
    "6": {
      "L": "For I will no longer have pity on the inhabitants of the land, declares the LORD. Behold, I will cause each person to fall into the hand of his neighbor and into the hand of his king, and they shall crush the land, and I will deliver none from their hand.",
      "M": "For I will no longer spare the inhabitants of the land, declares the LORD. I am about to hand each person over to his neighbor and his king. They will devastate the land, and I will not rescue anyone from their hand.",
      "T": "Yahweh declares: I am withdrawing my protection from the people of this land. I will hand them over — neighbor to neighbor, subject to king. The land will be shattered. And I will not reach down to pull anyone out."
    },
    "7": {
      "L": "So I shepherded the flock doomed to slaughter, for the sake of the sheep dealers. And I took two staffs: one I named Favor, and the other I named Union. And I shepherded the flock.",
      "M": "So I shepherded the flock marked for slaughter — the flock the dealers exploited. I took two staffs, calling one Favor and the other Union, and I shepherded the flock.",
      "T": "So I did it. I took up the shepherd's work for the flock heading to slaughter — I tended them for the sake of the merchants who had been exploiting them. I carried two staffs: I named one Grace and the other Unity. And I tended the flock."
    },
    "8": {
      "L": "In one month I annihilated three shepherds. But I became impatient with them, and they also detested me.",
      "M": "In one month I did away with three shepherds. But I grew impatient with them, and they loathed me in return.",
      "T": "In the space of a single month I removed three shepherds — three false leaders swept away. But by then my patience with the people was spent, and they had come to despise me."
    },
    "9": {
      "L": "So I said, 'I will not shepherd you. Let what is to die, die. Let what is to be destroyed, be destroyed. And let those who are left devour the flesh of one another.'",
      "M": "So I said, 'I will no longer shepherd you. What is dying, let it die; what is to be destroyed, let it be destroyed. Those who remain, let them devour one another.'",
      "T": "So I said: I am done. I resign from shepherding you. What is dying — let it die. What is being destroyed — let it be destroyed. What is left — let them turn on each other and feed. I am finished."
    },
    "10": {
      "L": "And I took my staff Favor and broke it, annulling the covenant that I had made with all the peoples.",
      "M": "Then I took my staff called Favor and broke it, canceling the covenant I had made with all the peoples.",
      "T": "I took the staff I had named Grace and snapped it in two. The covenant I had made with all the nations — to protect this people — was annulled."
    },
    "11": {
      "L": "So it was annulled on that day, and the sheep dealers who were watching me knew that it was the word of the LORD.",
      "M": "It was canceled on that day. The sheep merchants who were watching understood that this was the word of the LORD.",
      "T": "It was broken that day. And the sheep-traders who had watched the whole performance suddenly understood: this was not theater. This was the word of Yahweh."
    },
    "12": {
      "L": "Then I said to them, 'If it seems good to you, give me my wages; but if not, keep them.' And they weighed out my wages: thirty pieces of silver.",
      "M": "I said to them, 'If you think it right, pay me my wages; if not, keep them.' So they weighed out thirty pieces of silver as my wages.",
      "T": "I asked them to settle accounts: 'If you think I have been worth anything, pay me. If not, never mind.' They weighed out thirty pieces of silver."
    },
    "13": {
      "L": "Then the LORD said to me, 'Throw it to the potter' — the lordly price at which I was priced by them. So I took the thirty pieces of silver and threw them to the potter in the house of the LORD.",
      "M": "But the LORD said to me, 'Throw it to the potter' — this magnificent sum at which they valued me. So I took the thirty pieces of silver and threw them to the potter in the house of the LORD.",
      "T": "'Throw it to the potter,' Yahweh said — and the irony in the command was like thunder: 'this magnificent sum they have assigned me.' So I took the thirty pieces of silver and hurled them toward the potter in the house of Yahweh. A price had been paid. A judgment had been rendered."
    },
    "14": {
      "L": "Then I broke my second staff Union, annulling the brotherhood between Judah and Israel.",
      "M": "Then I broke my second staff called Union, canceling the bond of brotherhood between Judah and Israel.",
      "T": "Then I snapped the second staff — Unity — and with it the bond of brotherhood between Judah and Israel was severed. Two peoples that had been held together: now apart."
    },
    "15": {
      "L": "The LORD said to me, 'Take once more the equipment of a foolish shepherd.'",
      "M": "The LORD said to me, 'Take again the gear of a foolish shepherd.'",
      "T": "Then Yahweh said: 'Take it up again — this time, the full equipment of a foolish shepherd. Play the role through to the end.'"
    },
    "16": {
      "L": "For behold, I am raising up in the land a shepherd who does not care for the perishing, or seek the young, or heal the maimed, or nourish the healthy, but devours the flesh of the fat ones, tearing off even their hooves.",
      "M": "For I am about to raise up a shepherd in the land who will not care for those that are perishing, or seek the straying, or heal the injured, or sustain the healthy — but will devour the flesh of the fat sheep, tearing off even their hooves.",
      "T": "Because what is coming is a shepherd raised up in the land who abandons the dying, ignores the wandering, neglects the broken, and leaves the healthy to fend for themselves — who instead strips the fat sheep down to their very hooves, feeding himself on the flock. The anti-shepherd. The one who takes instead of gives."
    },
    "17": {
      "L": "Woe to my worthless shepherd who deserts the flock! May the sword strike his arm and his right eye! Let his arm be wholly withered, his right eye utterly blinded!",
      "M": "Woe to the worthless shepherd who abandons the flock! May a sword strike his arm and his right eye! Let his arm be completely withered, his right eye totally blinded!",
      "T": "Judgment falls on the hollow, useless shepherd who abandons his flock. The sword will come for his arm — his strength will wither to nothing. The sword will come for his right eye — his sight will go dark. He will be stripped of the very things a shepherd needs."
    }
  },
  "12": {
    "1": {
      "L": "The burden of the word of the LORD concerning Israel: Thus declares the LORD, who stretched out the heavens and founded the earth and formed the spirit of man within him:",
      "M": "An oracle — the word of the LORD concerning Israel. This is the declaration of the LORD, who stretched out the heavens, who laid the foundation of the earth, and who formed the human spirit within a person:",
      "T": "An oracle: the word of Yahweh over Israel. This is the voice of the one who stretched the sky like a canopy, who set the earth on its foundation, who formed the human spirit and breathed it into the chest of every person born:"
    },
    "2": {
      "L": "Behold, I am about to make Jerusalem a cup of staggering to all the surrounding peoples. The siege of Jerusalem will also involve Judah.",
      "M": "I am going to make Jerusalem a cup that sends all the surrounding peoples reeling. Judah too will be caught up in the siege against Jerusalem.",
      "T": "I am making Jerusalem into a cup of reeling — a vessel that sends the surrounding nations stumbling. And Judah itself will be swept into the siege of Jerusalem."
    },
    "3": {
      "L": "On that day I will make Jerusalem a heavy stone for all the peoples. All who lift it shall badly injure themselves. And all the nations of the earth shall gather against it.",
      "M": "On that day I will make Jerusalem a heavy stone for all the nations. Everyone who tries to lift it will injure themselves severely. All the nations of the earth will assemble against it.",
      "T": "On that day Jerusalem becomes an immovable stone — all who try to move it will tear themselves open. Every nation under heaven will converge on it. Every one of them will be broken by it."
    },
    "4": {
      "L": "On that day, declares the LORD, I will strike every horse with panic, and every rider with madness. I will open my eyes over the house of Judah, but every horse of the peoples I will strike with blindness.",
      "M": "On that day, declares the LORD, I will strike every horse with panic and every rider with madness. I will watch over the house of Judah, but every horse of the nations I will strike with blindness.",
      "T": "On that day — Yahweh declares it — every horse that comes will be seized with blind panic, every rider struck mad. But on the house of Judah my eyes will be open, watchful. And the horses of the nations: blind."
    },
    "5": {
      "L": "Then the clans of Judah shall say in their hearts, 'The inhabitants of Jerusalem have strength through the LORD of hosts, their God.'",
      "M": "Then the clans of Judah will say in their hearts, 'The inhabitants of Jerusalem draw their strength from the LORD of Hosts, their God.'",
      "T": "And the clan-leaders of Judah will say it in their own hearts: 'The people of Jerusalem are strong — not because of their walls, but because Yahweh of Armies, their God, stands with them.'"
    },
    "6": {
      "L": "On that day I will make the clans of Judah like a burning pot among logs and like a flaming torch among sheaves. And they shall devour to the right and to the left all the surrounding peoples, while Jerusalem shall again be inhabited in its own place, in Jerusalem.",
      "M": "On that day I will make the clans of Judah like a fire pot among logs, like a flaming torch among sheaves. They will devour all the surrounding peoples on the right and on the left, while Jerusalem remains inhabited in its own place.",
      "T": "On that day I will make Judah's clans like a firepot dropped into a woodpile, like a burning torch thrown into a wheat field. They will burn through the surrounding nations — right, left — consuming. And all the while, Jerusalem will stand, inhabited, in her place."
    },
    "7": {
      "L": "And the LORD will give victory to the tents of Judah first, that the glory of the house of David and the glory of the inhabitants of Jerusalem may not surpass that of Judah.",
      "M": "The LORD will save the settlements of Judah first, so that the prestige of the house of David and of Jerusalem's inhabitants does not overshadow Judah.",
      "T": "Yahweh will rescue Judah's rural settlements first — ahead of Jerusalem — so that neither the house of David nor the city's population can look down on those outside the walls. The countryside matters to him."
    },
    "8": {
      "L": "On that day the LORD will protect the inhabitants of Jerusalem, so that the one who is feeble among them on that day shall be like David, and the house of David shall be like God, like the angel of the LORD, going before them.",
      "M": "On that day the LORD will protect the inhabitants of Jerusalem; even the weakest among them will be like David on that day, and the house of David will be like God — like the angel of the LORD going before them.",
      "T": "On that day Yahweh will throw his shield over every person in Jerusalem. The most stumbling among them will fight like David. The house of David will be like a divine presence — like the angel of Yahweh going before the army. Weakness transformed. Smallness made great."
    },
    "9": {
      "L": "And on that day I will seek to destroy all the nations that come against Jerusalem.",
      "M": "On that day I will set out to destroy all the nations that attack Jerusalem.",
      "T": "On that day I will make it my purpose — my sustained intention — to destroy every nation that has moved against Jerusalem."
    },
    "10": {
      "L": "And I will pour out on the house of David and the inhabitants of Jerusalem a spirit of grace and pleas for mercy, so that, when they look on me, on him whom they have pierced, they shall mourn for him, as one mourns for an only child, and weep bitterly over him, as one weeps over a firstborn.",
      "M": "And I will pour out on the house of David and the inhabitants of Jerusalem a spirit of grace and supplication, so that they look on me — on the one they have pierced — and mourn for him, as one mourns for an only son, and weep bitterly over him, as one weeps over a firstborn.",
      "T": "Then I will pour out on the house of David and the people of Jerusalem a spirit of grace and earnest prayer. And when they look — when they truly look — at the one they have pierced, they will mourn. The mourning will be as deep as grief for an only child, as bitter as weeping for a firstborn son. The MT's pronoun shift — 'look on me... mourn for him' — is maintained: the pierced one and Yahweh speak in compressed, overlapping voice. The NT reads this as fulfilled in Christ (John 19:37; Rev 1:7)."
    },
    "11": {
      "L": "On that day the mourning in Jerusalem shall be as great as the mourning for Hadad-rimmon in the plain of Megiddo.",
      "M": "On that day the mourning in Jerusalem will be as intense as the mourning for Hadad-rimmon in the plain of Megiddo.",
      "T": "On that day, Jerusalem's mourning will reach the depth of the grief of Megiddo — likely the lamentation over Josiah, slain there (2 Chr 35:24–25), a grief by which all other grief was measured."
    },
    "12": {
      "L": "The land shall mourn, each family by itself: the family of the house of David by itself, and their wives by themselves; the family of the house of Nathan by itself, and their wives by themselves;",
      "M": "The land will mourn, each family privately: the family of the house of David in private, with the women separately; the family of Nathan in private, with the women separately;",
      "T": "The whole land will grieve — and the grief will be intimate, individual, not shared in crowd. The royal line of David: apart. Their wives: apart. The line of Nathan: apart. Their wives: apart."
    },
    "13": {
      "L": "the family of the house of Levi by itself, and their wives by themselves; the family of the Shimeites by itself, and their wives by themselves;",
      "M": "the family of the house of Levi in private, with the women separately; the family of Shimei in private, with the women separately;",
      "T": "The priestly line of Levi: apart. Their wives: apart. The family of Shimei: apart. Their wives: apart."
    },
    "14": {
      "L": "and all the remaining families, each by itself, and their wives by themselves.",
      "M": "and all the remaining families, each in private, with the women separately.",
      "T": "Every family that remains — each one alone, each wife in her own sorrow. The mourning is too large for crowds. It must be borne in private, face by face."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'zechariah')
        merge_tier(existing, ZECHARIAH, tier_key)
        save(tier_dir, 'zechariah', existing)
    print('Zechariah 7–12 written.')

if __name__ == '__main__':
    main()
