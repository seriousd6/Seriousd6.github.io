"""
MKT Esther chapters 3–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-esther-3-6.py

Translation decisions:
- H3068 (יהוה): Does not appear in Esther 3–6 (nor in the book at all — Esther and Song
  of Solomon are the only OT books without an explicit divine name). The T tier surfaces
  God's providence implicitly where the narrative structure implies it (esp. 6:1 — the
  king's insomnia is a classic divine-passive "coincidence"; 4:14 — "from another place"
  is widely read as a veiled reference to God).
- H430 (אֱלֹהִים): Also absent from the book. No rendering needed.
- H7307 (רוּחַ): Not in these chapters.
- H2617 (חֶסֶד): Not in these chapters.
- H5315 (נֶפֶשׁ): Appears in 4:13 — "not with your nephesh." L renders "soul," M renders
  "yourself," T renders "in your own heart" to surface the self-deceptive rationalization
  Mordecai is warning against.
- H6332 (Pur/lot): 3:7 — kept as "Pur (that is, the lot)" in all three tiers, preserving
  the Persian loanword that gives the Purim festival its name.
- H325 (Ahasuerus): This is almost certainly Xerxes I (486–465 BC). Rendered "Ahasuerus"
  throughout per traditional OT convention; the T tier does not editorialize with "Xerxes."
- Aspect notes: Hebrew narrative uses waw-consecutive imperfect throughout; rendered as
  simple past in all three tiers. Perfect forms in direct speech rendered as simple past or
  present perfect as English idiom requires.
- OT intertextual note (4:14): "relief and deliverance will arise from another place" —
  widely recognized as a veiled allusion to divine providence. T tier makes this explicit.
- Irony in ch. 6: The entire chapter turns on dramatic irony — Haman designs the honor
  ceremony for himself and it falls on Mordecai. The T tier surfaces this irony, especially
  at the moment Haman enters the court (6:4–6).
- "For such a time as this" (4:14): One of the most memorable phrases in the book. T tier
  gives it full rhetorical weight.
- H1881 (dāt, "law/decree"): Rendered "law" in legal contexts and "decree" when referring
  to specific royal edicts. Consistent across all tiers.
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

ESTHER = {
  "3": {
    "1": {
      "L": "After these things King Ahasuerus promoted Haman son of Hammedatha the Agagite, and advanced him and set his seat above all the princes who were with him.",
      "M": "After these events, King Ahasuerus promoted Haman the son of Hammedatha the Agagite, elevating him and giving him a seat of honor above all the princes who served with him.",
      "T": "In the wake of all these events, King Ahasuerus singled out Haman—son of Hammedatha the Agagite—for advancement, raising him to a seat of honor above all the other officials at court."
    },
    "2": {
      "L": "And all the king's servants who were in the king's gate bowed and paid homage to Haman, for the king had so commanded concerning him. But Mordecai did not bow and did not pay homage.",
      "M": "All the king's servants at the king's gate bowed down and paid homage to Haman, for the king had ordered this regarding him. But Mordecai would not bow or pay homage.",
      "T": "Every royal official at the palace gate prostrated themselves before Haman—the king had commanded it—but Mordecai refused. He would not bow; he would not honor him."
    },
    "3": {
      "L": "Then the king's servants who were in the king's gate said to Mordecai, 'Why do you transgress the king's commandment?'",
      "M": "The king's servants at the king's gate asked Mordecai, 'Why do you disobey the king's command?'",
      "T": "Day after day the palace gate officials challenged him: 'Why are you defying the king's order?'"
    },
    "4": {
      "L": "Now it came to pass when they spoke to him day by day and he would not listen to them, that they told Haman, to see whether Mordecai's words would stand, for he had told them that he was a Jew.",
      "M": "When they had been speaking to him day after day and he would not listen, they reported the matter to Haman to see whether Mordecai's defiance would be tolerated, for he had told them that he was a Jew.",
      "T": "They pressed him daily, and he never budged. Finally they reported it to Haman—curious whether this stand would be allowed to hold—for Mordecai had told them plainly that he was a Jew."
    },
    "5": {
      "L": "And when Haman saw that Mordecai did not bow and did not pay him homage, Haman was filled with wrath.",
      "M": "When Haman saw that Mordecai would not bow or show him reverence, Haman was filled with rage.",
      "T": "The moment Haman saw that Mordecai refused to bow—refused even to acknowledge him—fury consumed him."
    },
    "6": {
      "L": "But it was contemptible in his eyes to lay hands on Mordecai alone, for they had told him the people of Mordecai. So Haman sought to destroy all the Jews who were throughout the whole kingdom of Ahasuerus—even the people of Mordecai.",
      "M": "Yet it seemed beneath him to lay hands on Mordecai alone, for they had told him what people Mordecai belonged to. So Haman set out to destroy all the Jews throughout Ahasuerus's kingdom—they were Mordecai's people.",
      "T": "But killing one man was too small a revenge for Haman. Once he learned that Mordecai was a Jew, he decided that nothing short of exterminating the entire Jewish people across the empire would satisfy him."
    },
    "7": {
      "L": "In the first month, which is the month of Nisan, in the twelfth year of King Ahasuerus, they cast Pur—that is the lot—before Haman, from day to day and from month to month, until the twelfth month, which is the month of Adar.",
      "M": "In the first month, that is, the month of Nisan, in the twelfth year of King Ahasuerus, the lot—called Pur—was cast before Haman from day to day and from month to month, and it fell on the twelfth month, that is, the month of Adar.",
      "T": "Haman turned to divination to choose the perfect day. In the first month of Ahasuerus's twelfth year, lots—Pur in Persian—were cast before him day after day, month after month, until the oracle settled on the twelfth month: Adar."
    },
    "8": {
      "L": "And Haman said to King Ahasuerus, 'There is a certain people scattered and dispersed among the peoples in all the provinces of your kingdom, and their laws are different from all other peoples, and the king's laws they do not keep. It is not in the king's interest to let them remain.'",
      "M": "Then Haman said to King Ahasuerus, 'There is a certain people scattered and dispersed throughout all the provinces of your kingdom. Their customs differ from those of every other people, and they do not obey the king's laws. It is not in the king's interest to tolerate them.'",
      "T": "Haman brought his case to the king: 'Your Majesty, there is a people spread across every province of the empire—isolated, clannish, bound by laws that set them apart from every other nation, laws that take precedence over yours. They are a liability the crown cannot afford to carry.'"
    },
    "9": {
      "L": "If it pleases the king, let it be written that they be destroyed, and I will weigh out ten thousand talents of silver into the hands of those who do the work, to bring it into the king's treasuries.",
      "M": "If it pleases the king, let a decree be issued for their destruction. I will deposit ten thousand talents of silver into the royal treasury, into the hands of those who carry out the business.",
      "T": "'If your majesty agrees, issue the order for their extermination. I will personally underwrite the entire cost—ten thousand talents of silver into the royal treasury—so that not a shekel falls on the crown.'"
    },
    "10": {
      "L": "So the king removed his signet ring from his hand and gave it to Haman son of Hammedatha the Agagite, the enemy of the Jews.",
      "M": "The king removed his signet ring from his hand and gave it to Haman the son of Hammedatha the Agagite, the enemy of the Jews.",
      "T": "Without hesitation, the king pulled the royal signet from his own hand and placed it in Haman's—the hand of Haman son of Hammedatha the Agagite, the enemy of the Jewish people."
    },
    "11": {
      "L": "And the king said to Haman, 'The silver is given to you, and the people also, to do with them as it seems good in your eyes.'",
      "M": "The king said to Haman, 'The silver is yours, and the people also—do with them as you see fit.'",
      "T": "'Keep the money,' the king said. 'And keep the people. Do with them whatever seems right to you.'"
    },
    "12": {
      "L": "Then the king's scribes were summoned on the thirteenth day of the first month, and it was written, according to all that Haman commanded, to the king's satraps and to the governors over every province and to the officials of every people—each province in its own script and each people in their own language—in the name of King Ahasuerus and sealed with the king's ring.",
      "M": "The king's scribes were summoned on the thirteenth day of the first month, and the letters were written exactly as Haman dictated—to the king's satraps, the governors of each province, and the officials of each people, in the script and language of every province and people—written in the name of King Ahasuerus and sealed with the royal signet ring.",
      "T": "On the thirteenth of Nisan, royal scribes were assembled and the letters went out in every script, every tongue—to satraps, provincial governors, and local officials across the empire. Haman dictated every word; the king's name stood at the top and his signet sealed each one."
    },
    "13": {
      "L": "And letters were sent by couriers into all the king's provinces, to destroy, to kill, and to annihilate all Jews—young and old, women and children—in one day, on the thirteenth day of the twelfth month, which is the month of Adar, and to seize their possessions as plunder.",
      "M": "Letters were sent by couriers to all the king's provinces, ordering the destruction, killing, and annihilation of all Jews—young and old, women and children—on a single day, the thirteenth of the twelfth month, that is, the month of Adar, and the plundering of their possessions.",
      "T": "Sealed death warrants were dispatched by royal courier to every corner of the empire: on the thirteenth of Adar—a single day—every Jew in Persia, young and old, man, woman, and child, was to be killed and their property seized."
    },
    "14": {
      "L": "A copy of the writing was to be given as a decree in every province, published to all the peoples, so that they should be ready for that day.",
      "M": "A copy of the edict was to be issued as law in every province and made known to all peoples, so that they would be prepared for that day.",
      "T": "The edict was to be posted publicly in every province so that every subject of the empire would know the date and be ready to act."
    },
    "15": {
      "L": "The couriers went out, hastened by the king's word, and the decree was given in Shushan the citadel. And the king and Haman sat down to drink, but the city of Shushan was in confusion.",
      "M": "The couriers rode out under urgent royal orders, and the decree was issued in the citadel of Susa. While the king and Haman sat down to drink, the city of Susa was thrown into confusion.",
      "T": "The royal couriers galloped out. Inside the palace, the king and Haman settled in to drink. Outside, the city of Susa reeled in confusion."
    }
  },
  "4": {
    "1": {
      "L": "When Mordecai knew all that was done, Mordecai tore his clothes and put on sackcloth and ashes, and went out into the midst of the city and cried with a loud and bitter cry.",
      "M": "When Mordecai learned all that had been done, he tore his clothes, put on sackcloth and ashes, and went out into the middle of the city, crying aloud with a loud and bitter cry.",
      "T": "The moment Mordecai grasped what had been done, he tore his clothes apart, wrapped himself in sackcloth, poured ashes over his head, and walked into the heart of the city wailing—a wail so raw and loud it carried through every street."
    },
    "2": {
      "L": "He went as far as the front of the king's gate, for no one might enter the king's gate clothed in sackcloth.",
      "M": "He came as far as the entrance of the king's gate, for no one was permitted to enter the king's gate wearing sackcloth.",
      "T": "He went to the very entrance of the palace gate—and no further, because mourning clothes could not cross that threshold."
    },
    "3": {
      "L": "And in every province, wherever the king's command and his decree reached, there was great mourning among the Jews, with fasting, weeping, and wailing; many lay in sackcloth and ashes.",
      "M": "In every province where the king's command and decree arrived, there was great mourning among the Jews—fasting, weeping, and lamentation; multitudes lay in sackcloth and ashes.",
      "T": "Across the empire, wherever the royal decree reached, Jewish communities broke into mourning. People fasted. They wept and wailed. They lay in sackcloth and ashes—grief with nowhere to hide."
    },
    "4": {
      "L": "Then Esther's maids and her eunuchs came and told her, and the queen was deeply distressed. She sent garments to clothe Mordecai and to remove his sackcloth from him, but he would not accept them.",
      "M": "When Esther's maids and eunuchs came and told her, the queen was deeply distressed. She sent garments to clothe Mordecai and to take away his sackcloth, but he refused to accept them.",
      "T": "Word reached Esther through her attendants and she was shaken to her core. She immediately sent clean clothing to Mordecai to replace the sackcloth—but he sent it back untouched."
    },
    "5": {
      "L": "Then Esther called Hatach, one of the king's eunuchs whom he had appointed to serve her, and gave him a command to go to Mordecai, to know what it was and why it was.",
      "M": "So Esther summoned Hatach, one of the king's eunuchs assigned to attend her, and charged him to go to Mordecai and find out what was happening and why.",
      "T": "Esther summoned Hatach, a palace eunuch assigned to her personal service, and sent him to Mordecai with orders: find out what is happening and why."
    },
    "6": {
      "L": "So Hatach went out to Mordecai in the open square of the city in front of the king's gate.",
      "M": "Hatach went out to Mordecai in the city square in front of the king's gate.",
      "T": "Hatach found Mordecai in the public square just outside the palace gate."
    },
    "7": {
      "L": "And Mordecai told him all that had happened to him, and the exact sum of silver that Haman had promised to pay into the king's treasuries for the Jews, to destroy them.",
      "M": "Mordecai told him everything that had happened to him, including the precise sum of money Haman had offered to deposit in the royal treasury in exchange for the order to destroy the Jews.",
      "T": "Mordecai laid it all out: everything that had happened to him, and the staggering bribe Haman had pledged to the royal treasury in exchange for the warrant to exterminate his people."
    },
    "8": {
      "L": "He also gave him a copy of the written decree that had been issued in Shushan for their destruction, to show Esther and to inform her, and to charge her to go in to the king to make supplication to him and to plead with him for her people.",
      "M": "He also handed him a copy of the written edict issued in Susa for their destruction, to show Esther and explain it to her, and to charge her to go before the king to plead for her people.",
      "T": "He pressed into Hatach's hands a copy of the death warrant itself—the actual edict, issued in Susa—with orders to show it to Esther, explain everything, and charge her to go before the king and intercede for her people."
    },
    "9": {
      "L": "And Hatach went and told Esther the words of Mordecai.",
      "M": "Hatach went back and reported Mordecai's words to Esther.",
      "T": "Hatach returned and delivered Mordecai's message word for word."
    },
    "10": {
      "L": "And Esther spoke to Hatach and commanded him to go to Mordecai:",
      "M": "Then Esther spoke to Hatach and sent him back to Mordecai with this message:",
      "T": "Esther sent Hatach back to Mordecai with her reply:"
    },
    "11": {
      "L": "'All the king's servants and the people of the king's provinces know that any person—man or woman—who enters the king's inner court without being summoned, there is one law: death. Only the one to whom the king holds out the golden scepter may live. And I myself have not been called to come in to the king for these thirty days.'",
      "M": "'All the king's servants and the people of the provinces know that if anyone—man or woman—enters the king's inner court without being summoned, there is but one penalty: death. The sole exception is if the king extends the golden scepter, by which they may live. And I have not been called to the king for thirty days.'",
      "T": "'Everyone in the palace—every servant, every subject in every province—knows the law: approach the king in his inner court without a summons and you die. The single exception is if the king extends his golden scepter; that alone grants life. And the king has not sent for me in thirty days.'"
    },
    "12": {
      "L": "And they told Mordecai the words of Esther.",
      "M": "They reported Esther's words to Mordecai.",
      "T": "The message was delivered to Mordecai."
    },
    "13": {
      "L": "And Mordecai commanded to reply to Esther: 'Do not imagine in your soul that you alone among all the Jews will escape in the king's household.'",
      "M": "Then Mordecai sent back this answer to Esther: 'Do not think in your heart that you will escape among all the Jews just because you are in the king's palace.'",
      "T": "Mordecai's reply cut through every illusion: 'Don't deceive yourself in your own heart—being inside the palace walls will not save you when the rest of your people die. You are not exempt.'"
    },
    "14": {
      "L": "'For if you keep utterly silent at this time, relief and deliverance will arise for the Jews from another place, but you and your father's house will perish. And who knows whether you have not come to royal position for just such a time as this?'",
      "M": "'For if you remain completely silent at this critical time, relief and deliverance will come to the Jews from another source, but you and your father's family will perish. And who knows—perhaps you came to royal position for precisely such a time as this?'",
      "T": "'If you stay silent now, rescue for the Jewish people will come—it will come from somewhere, because these people cannot be destroyed—but you and your father's house will be swept away with the silence. And consider this: who is to say you did not come to be queen for this exact moment?'"
    },
    "15": {
      "L": "Then Esther sent this reply to Mordecai:",
      "M": "Then Esther sent this reply to Mordecai:",
      "T": "Esther's answer came back:"
    },
    "16": {
      "L": "'Go, gather all the Jews who are found in Shushan, and hold a fast for me. Do not eat or drink for three days, night or day. I and my maidens will likewise fast. And so I will go in to the king, which is not according to the law. And if I perish, I perish.'",
      "M": "'Go, gather all the Jews who are in Susa, and fast on my behalf. Do not eat or drink for three days, night or day. My maids and I will fast as well. Then I will go in to the king, even though it is against the law. And if I perish, I perish.'",
      "T": "'Go. Gather every Jew in Susa and fast for me—three days without food or water, day or night. My women and I will do the same. Then I will go to the king, though the law forbids it. And if I die, I die.'"
    },
    "17": {
      "L": "So Mordecai passed on and did all that Esther had charged him.",
      "M": "Mordecai went away and did everything Esther had commanded him.",
      "T": "Mordecai went and carried out every part of Esther's instructions."
    }
  },
  "5": {
    "1": {
      "L": "Now it came to pass on the third day that Esther put on royal apparel and stood in the inner court of the king's house, across from the king's house. The king was sitting on his royal throne in the royal house, opposite the entrance to the house.",
      "M": "On the third day Esther put on her royal robes and stood in the inner court of the palace, facing the king's hall. The king was seated on the royal throne in the throne room, facing the entrance of the hall.",
      "T": "On the third day, Esther dressed herself in the full splendor of her royal robes and took her place in the inner court of the palace, directly across from the king's throne room. Inside, the king sat enthroned in full royal state."
    },
    "2": {
      "L": "And it was so, when the king saw Esther the queen standing in the court, she found favor in his eyes. The king held out to Esther the golden scepter that was in his hand, and Esther drew near and touched the top of the scepter.",
      "M": "When the king saw Queen Esther standing in the court, she found favor in his eyes. He extended the golden scepter in his hand toward Esther, and Esther approached and touched the tip of the scepter.",
      "T": "The king looked up and saw Esther standing there. Favor moved in him. He extended the golden scepter—the gesture that meant life—and Esther came forward and touched its tip."
    },
    "3": {
      "L": "Then the king said to her, 'What is it, Queen Esther, and what is your request? To the half of the kingdom it will be given to you.'",
      "M": "The king said to her, 'What is the matter, Queen Esther? What is your request? It shall be granted to you, even to half the kingdom.'",
      "T": "'What brings you here, Queen Esther?' the king asked. 'Name what you want—up to half the kingdom, it is yours.'"
    },
    "4": {
      "L": "And Esther said, 'If it seems good to the king, let the king and Haman come today to the banquet that I have prepared for him.'",
      "M": "Esther answered, 'If it pleases the king, let the king and Haman come today to the banquet I have prepared.'",
      "T": "'If it pleases your majesty,' Esther said, 'let the king and Haman come today to a banquet I have prepared.'"
    },
    "5": {
      "L": "And the king said, 'Bring Haman quickly so that what Esther has said may be done.' So the king and Haman came to the banquet that Esther had prepared.",
      "M": "The king said, 'Bring Haman at once, so that what Esther desires may be done.' So the king and Haman came to the banquet Esther had prepared.",
      "T": "'Bring Haman immediately!' the king ordered. And so the king and Haman came together to the banquet Esther had prepared."
    },
    "6": {
      "L": "And the king said to Esther at the banquet of wine, 'What is your petition? It will be granted to you. And what is your request? Even to the half of the kingdom it will be fulfilled.'",
      "M": "At the wine banquet the king said to Esther, 'What is your petition? It shall be granted. What is your request? Even to half the kingdom it shall be fulfilled.'",
      "T": "Over wine the king pressed her again: 'Tell me what you want, Esther. Whatever your petition, whatever your request—even half my kingdom—it is done.'"
    },
    "7": {
      "L": "And Esther answered and said, 'My petition and my request—'",
      "M": "Esther answered, 'My petition and my request—'",
      "T": "Esther began carefully:"
    },
    "8": {
      "L": "'If I have found favor in the eyes of the king, and if it pleases the king to grant my petition and to fulfill my request, let the king and Haman come to the banquet that I will prepare for them, and tomorrow I will do as the king has spoken.'",
      "M": "'If I have found favor in the king's eyes, and if it pleases the king to grant my petition and fulfill my request, let the king and Haman come to the banquet I will prepare for them. Tomorrow I will answer the king's question.'",
      "T": "'If I have found favor with you, and if my king is willing to grant what I am about to ask—let the king and Haman come tomorrow to a second banquet I will prepare. Tomorrow I will speak plainly.'"
    },
    "9": {
      "L": "Then Haman went out that day joyful and with a glad heart. But when Haman saw Mordecai in the king's gate, and that he did not rise nor stir on his account, Haman was filled with rage against Mordecai.",
      "M": "Haman left that day glad and in high spirits. But when he saw Mordecai at the king's gate—sitting unmoved, refusing to rise or show fear—Haman was filled with rage against Mordecai.",
      "T": "Haman walked out of the banquet elated, his heart soaring. Then he passed the gate and saw Mordecai—still sitting there, not rising, not flinching—and the joy curdled instantly into fury."
    },
    "10": {
      "L": "Nevertheless Haman restrained himself and went home. He sent and brought his friends and Zeresh his wife.",
      "M": "Haman controlled himself and went home, where he sent for his friends and his wife Zeresh.",
      "T": "Haman forced himself to hold it in and went home, where he gathered his friends and his wife Zeresh around him."
    },
    "11": {
      "L": "And Haman recounted to them the glory of his wealth, the multitude of his sons, and all the things in which the king had promoted him and how he had elevated him above the officials and servants of the king.",
      "M": "Haman boasted to them about his enormous wealth, his many sons, and all the ways the king had honored him—how he had been exalted above all the officials and servants of the king.",
      "T": "Haman laid out his achievements before them: his extraordinary wealth, his many sons, the honors the king had showered on him—how he had been raised above every prince and official in the empire."
    },
    "12": {
      "L": "And Haman said, 'Moreover, Queen Esther let no one come with the king to the banquet she prepared except me; and tomorrow also I am invited with the king.'",
      "M": "'Furthermore,' Haman said, 'Queen Esther invited no one but me to accompany the king to the banquet she gave. And I am invited again tomorrow with the king.'",
      "T": "'And more than that,' he added, 'Queen Esther herself—no one but me was invited with the king to her banquet. Tomorrow the invitation stands again. Just me and the king.'"
    },
    "13": {
      "L": "'Yet all this is worth nothing to me every time I see Mordecai the Jew sitting in the king's gate.'",
      "M": "'But none of this satisfies me as long as I see Mordecai the Jew sitting at the king's gate.'",
      "T": "'And yet—none of it means a thing to me. Every time I walk past that gate and see that Jew sitting there, it all turns to ash.'"
    },
    "14": {
      "L": "Then Zeresh his wife and all his friends said to him, 'Let a gallows be made fifty cubits high, and in the morning speak to the king that Mordecai be hanged on it; then go joyfully with the king to the banquet.' The suggestion pleased Haman, and he had the gallows made.",
      "M": "His wife Zeresh and all his friends said to him, 'Have a gallows built fifty cubits high. In the morning, speak to the king and have Mordecai hanged on it; then you can go to the banquet with the king in good spirits.' The proposal pleased Haman, and he had the gallows constructed.",
      "T": "Zeresh and his friends offered the solution: 'Build a gallows—fifty cubits tall, impossible to miss. Tomorrow morning, get the king's permission and have Mordecai hanged on it before breakfast. Then you can go to the banquet with nothing on your mind.' The plan thrilled Haman. He ordered the gallows built that very night."
    }
  },
  "6": {
    "1": {
      "L": "On that night the sleep of the king fled, and he commanded that the book of records, the chronicles, be brought; and they were read before the king.",
      "M": "That night the king could not sleep. He ordered the book of the records of the chronicles to be brought, and it was read aloud to him.",
      "T": "That night sleep eluded the king. He sent for the royal chronicles to be read aloud to him—and so, in the unseen workings of providence, the night unraveled toward morning."
    },
    "2": {
      "L": "And it was found written that Mordecai had reported Bigthana and Teresh, two of the king's eunuchs from the keepers of the threshold, who had sought to lay hands on King Ahasuerus.",
      "M": "It was found recorded that Mordecai had exposed Bigthana and Teresh, two of the king's eunuchs who guarded the entrance and had plotted to assassinate King Ahasuerus.",
      "T": "By what could only be called a remarkable coincidence, the reader came to the account of how Mordecai had once uncovered an assassination plot—two palace doorkeepers, Bigthana and Teresh, who had planned to kill the king."
    },
    "3": {
      "L": "And the king said, 'What honor and dignity has been done to Mordecai for this?' Then the king's servants who attended him said, 'Nothing has been done for him.'",
      "M": "The king asked, 'What honor and recognition were given to Mordecai for this?' His attendants replied, 'Nothing has been done for him.'",
      "T": "'What reward was given to Mordecai for this?' the king demanded. 'Nothing,' his servants told him. 'Nothing was ever done.'"
    },
    "4": {
      "L": "And the king said, 'Who is in the court?' Now Haman had come into the outer court of the king's house to speak to the king about hanging Mordecai on the gallows he had prepared for him.",
      "M": "The king asked, 'Who is in the court?' Haman had just entered the outer court of the palace, coming to ask the king to have Mordecai hanged on the gallows he had already built.",
      "T": "'Who is in the outer court right now?' the king asked. As it happened, Haman had arrived at that very moment—coming to request the king's permission to hang Mordecai on the gallows already waiting for him."
    },
    "5": {
      "L": "The king's servants said to him, 'Haman is standing in the court.' And the king said, 'Let him enter.'",
      "M": "The king's servants told him, 'Haman is standing in the court.' The king said, 'Bring him in.'",
      "T": "'Haman is here, your majesty—in the outer court.' 'Send him in,' said the king."
    },
    "6": {
      "L": "So Haman came in, and the king said to him, 'What should be done for the man whom the king desires to honor?' And Haman said in his heart, 'Whom would the king desire to honor more than me?'",
      "M": "Haman came in, and the king asked him, 'What should be done for the man whom the king wishes to honor?' Haman thought to himself, 'Who would the king want to honor more than me?'",
      "T": "Haman entered, and before he could say a word, the king asked: 'What should be done for a man the king wants to honor?' Haman's heart leaped—who else could the king possibly mean but him?"
    },
    "7": {
      "L": "And Haman said to the king, 'For the man whom the king desires to honor—'",
      "M": "So Haman said to the king, 'For the man the king wishes to honor—'",
      "T": "So Haman began laying out an elaborate answer, speaking as if designing his own triumph:"
    },
    "8": {
      "L": "'Let royal garments be brought that the king himself wears, and the horse on which the king himself rides, and on whose head a royal crown is set.'",
      "M": "'Let royal robes be brought—those the king himself wears—and the horse the king himself rides, with the royal crown placed on its head.'",
      "T": "'Bring the royal robes—the ones the king himself wears. Bring the horse the king himself rides—the one that bears the royal crown on its head.'"
    },
    "9": {
      "L": "'And let the garments and the horse be delivered into the hand of one of the king's most noble officials, and let them clothe the man whom the king desires to honor and lead him on horseback through the square of the city, and proclaim before him: \"Thus shall it be done for the man whom the king desires to honor.\"'",
      "M": "'Then let this robe and horse be handed over to one of the king's most distinguished nobles. Have him clothe the man the king wishes to honor, lead him on horseback through the city square, and cry out before him: \"This is what is done for the man the king delights to honor!\"'",
      "T": "'Place those robes on one of the king's noblest princes, have him dress the honored man with his own hands, and lead him through the main street of the city on that horse—with a herald crying ahead: \"This is what the king does for the man he delights to honor!\"'"
    },
    "10": {
      "L": "Then the king said to Haman, 'Hurry, take the garments and the horse as you have said, and do so for Mordecai the Jew who sits at the king's gate. Do not let fall anything of all that you have spoken.'",
      "M": "The king said to Haman, 'Hurry—take the robe and the horse exactly as you have described, and do all this for Mordecai the Jew who sits at the king's gate. Leave out nothing you have said.'",
      "T": "'Excellent,' said the king. 'Take the robe. Take the horse. Do every single thing you described—for Mordecai the Jew at the palace gate. Not one detail may be omitted.'"
    },
    "11": {
      "L": "So Haman took the garments and the horse and robed Mordecai and led him on horseback through the square of the city, and proclaimed before him, 'Thus shall it be done for the man whom the king desires to honor.'",
      "M": "So Haman took the robe and the horse, dressed Mordecai, and led him through the city square on horseback, proclaiming before him, 'This is what is done for the man the king delights to honor.'",
      "T": "Haman took the robe. He dressed Mordecai with his own hands. He led Mordecai on horseback through the streets of the city while calling out, 'This is what the king does for the man he delights to honor!'"
    },
    "12": {
      "L": "Then Mordecai returned to the king's gate, but Haman hurried to his house, mourning and with his head covered.",
      "M": "Mordecai returned to the king's gate, while Haman rushed home in mourning, his head covered.",
      "T": "Mordecai walked back through the palace gate as before. Haman fled home—head covered, utterly humiliated."
    },
    "13": {
      "L": "And Haman recounted to Zeresh his wife and to all his friends all that had befallen him. Then his wise men and Zeresh his wife said to him, 'If Mordecai, before whom you have begun to fall, is of the seed of the Jews, you will not prevail against him but will surely fall before him.'",
      "M": "Haman told his wife Zeresh and all his friends everything that had happened to him. Then his advisors and his wife Zeresh said to him, 'If Mordecai—this man before whom you have begun to fall—is of Jewish descent, you will not prevail against him; you will surely fall.'",
      "T": "Back home, Haman poured out the whole humiliating story to Zeresh and his friends. Their verdict was ominous: 'If this Mordecai is Jewish—and he is—your downfall has already begun. You cannot win against him. What has started will not stop.'"
    },
    "14": {
      "L": "While they were still speaking with him, the king's eunuchs arrived and hastened to bring Haman to the banquet that Esther had prepared.",
      "M": "While they were still speaking with him, the king's chamberlains arrived and hurried to escort Haman to the banquet Esther had prepared.",
      "T": "Before anyone could say another word, the royal escort arrived—and Haman was swept away to Esther's banquet."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'esther')
        merge_tier(existing, ESTHER, tier_key)
        save(tier_dir, 'esther', existing)
    print('Esther 3–6 written.')

if __name__ == '__main__':
    main()
