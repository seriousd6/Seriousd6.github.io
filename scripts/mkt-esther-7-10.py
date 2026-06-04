"""
MKT Esther chapters 7–10 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-esther-7-10.py

Translation decisions (carrying forward all prior-script decisions from mkt-esther-1-2.py):

- H3068 / H430 (יהוה / אֱלֹהִים): ABSENT from the entire book — divine names never appear in the
  Hebrew text of Esther. This hiddenness is theologically deliberate. No LORD/God insertion.
  However, T tier may note divine reversal in the narrative (e.g., 9:1 "the situation was reversed"
  uses the passive, implying the hand of providence without naming the agent — consistent with the
  book's own restraint).

- H325 (Ahasuerus): "Ahasuerus" in L/M/T throughout. No "Xerxes" substitution.

- H7800 (שׁוּשַׁן, Shushan): "Shushan" in L; "Susa" in M/T — consistent with prior chapters.

- H1002 (בִּירָה, birah): "palace" L; "citadel" M/T — the fortified royal acropolis at Susa.

- H5315 (נֶפֶשׁ, nephesh) at 7:3, 7:7, 8:11: "life" across all tiers in these contexts.
  The word means the embodied self; here it is the life under threat of annihilation. No
  "soul" in the Greek-immortality sense; the person's living existence is what is at stake.

- H6332 (פּוּר, Pur): transliterated "Pur" in all tiers. Explained as "the lot" in L ("that is
  the lot") and glossed in M. T surfaces the irony: Haman's own luck-casting device became the
  name of the festival celebrating his defeat.

- H4521 (מָנוֹת, manot): "portions" (of food sent as gifts) in all tiers — L: "portions";
  M/T: "portions of food." The giving of mishloach manot (sending portions) is a defining Purim
  practice established here.

- H7965 (שָׁלוֹם, shalom) at 9:30 and 10:3: L: "peace"; M: "peace"; T: "peace" — in these
  contexts the word carries its full sense of wholeness and communal welfare. T notes at 10:3.

- H2617 (חֶסֶד, hesed): does not appear in chapters 7–10 in this text.

- H4960 (מִשְׁתֶּה, mishteh): "feast" L; "banquet/feast" M/T — continuing prior chapters.

- H5631 (סָרִיס, saris) at 7:9 (Harbonah): "eunuch/chamberlain" — rendered "eunuch" in L,
  "official" in M/T (Harbonah is one of the king's personal attendants from ch. 1).

- H1881 (דָּת, dat): "law/decree" throughout — Persian loanword for royal edict.

- H6366 (פְּרָזִי, perazi) at 9:19: "those in unwalled towns / rural Jews" — the technical
  distinction between Jews in Susa (walled city) who rest the 15th and those in unwalled towns
  who rest the 14th is preserved in all tiers.

- Chapter 9 names (vv. 7–9): Haman's ten sons are listed consecutively. In L all three verses
  appear as bare lists (matching the terse Hebrew); M/T connect them to the narrative frame.

- The counter-edict (8:9–13): The irrevocability of Persian law (1:19, 3:13) creates a legal
  puzzle: the first edict cannot be repealed; the second edict grants Jews the right to defend
  themselves. T surfaces this tension.

- 9:1 "it was turned to the contrary" (Hebrew: נַהֲפוֹךְ הוּא, nahaphokh hu): divine passive —
  an agent-less reversal. The book does not name God, but the grammar points toward unseen
  direction. T notes this without overriding the book's literary restraint.

- 10:3 "second to King Ahasuerus": Mordecai's role echoes Joseph (Gen 41:40) and Daniel
  (Dan 2:48) — the faithful exile exalted to second-in-command in a Gentile empire. T notes
  this intertextual echo.

- Chapter 9 death tolls: rendered straightforwardly in all tiers. The narrative presents the
  violence without apology as the reversal of Haman's decree; T does not editorialize.
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
  "7": {
    "1": {
      "L": "So the king and Haman came to banquet with Esther the queen.",
      "M": "So the king and Haman came to banquet with Queen Esther.",
      "T": "The king and Haman came to Queen Esther's banquet — the second one. Whatever Esther had been waiting for, she would wait no longer."
    },
    "2": {
      "L": "And the king said again unto Esther on the second day at the banquet of wine, What is thy petition, queen Esther? and it shall be granted thee: and what is thy request? and it shall be performed, even to the half of the kingdom.",
      "M": "Again on the second day, at the banquet of wine, the king said to Esther, 'What is your petition, Queen Esther? It shall be granted to you. And what is your request? Even to the half of the kingdom it shall be fulfilled.'",
      "T": "For the third time the king offered the half-kingdom — now at the second banquet, wine-warmed and expansive, with no suspicion of what was coming. It was time."
    },
    "3": {
      "L": "Then Esther the queen answered and said, If I have found favour in thy sight, O king, and if it please the king, let my life be given me at my petition, and my people at my request:",
      "M": "Queen Esther replied, 'If I have found favor in your sight, O king, and if it pleases the king — let my life be given me at my petition, and my people at my request.'",
      "T": "Esther finally asked. Not for wealth, not for position — for her life. 'If I have found favor in your sight, O king, grant me my life at my petition — and my people at my request.' The words must have landed like a stone in still water."
    },
    "4": {
      "L": "For we are sold, I and my people, to be destroyed, to be slain, and to perish. But if we had been sold for bondmen and bondwomen, I had held my tongue, although the enemy could not countervail the king's damage.",
      "M": "For we have been sold — I and my people — to be destroyed, to be killed, and to be annihilated. Had we only been sold into slavery, I would have kept silent, for that trouble would not have warranted disturbing the king.",
      "T": "'We have been sold — I and my people — to be wiped out. Killed. Annihilated. Had it been mere enslavement, I would have swallowed the indignity rather than trouble you. But this is not inconvenience. This is extermination.' The secret was out. Esther was a Jew. And a decree of death hung over her people."
    },
    "5": {
      "L": "Then the king Ahasuerus answered and said unto Esther the queen, Who is he, and where is he, that durst presume in his heart to do so?",
      "M": "Then King Ahasuerus answered Queen Esther, 'Who is he, and where is he, who has presumed in his heart to do this?'",
      "T": "The king's face changed. 'Who has dared to do this? Who is he, and where is he?' He did not yet know that the answer was sitting at his own table."
    },
    "6": {
      "L": "And Esther said, The adversary and enemy is this wicked Haman. Then Haman was afraid before the king and the queen.",
      "M": "Esther said, 'The adversary and enemy is this wicked Haman!' Then Haman was terrified before the king and the queen.",
      "T": "Esther pointed straight at him. 'The enemy. The one who would destroy us. This wicked Haman, right here.' The room froze. Haman's face went white with terror — he had nowhere to look but at the king, and the king's eyes were something he could not meet."
    },
    "7": {
      "L": "And the king arising from the banquet of wine in his wrath went into the palace garden: and Haman stood up to make request for his life to Esther the queen; for he saw that there was evil determined against him by the king.",
      "M": "The king arose in his fury from the banquet and went into the palace garden. Haman stood to plead for his life with Queen Esther, for he could see that the king had determined evil against him.",
      "T": "Ahasuerus stormed out into the garden — he needed to think, or to rage where no one could see. Haman was left alone with Esther, and he understood exactly what it meant. He threw himself at her mercy, begging for his life, because the king's face had already announced the verdict."
    },
    "8": {
      "L": "Then the king returned out of the palace garden into the place of the banquet of wine; and Haman was fallen upon the bed whereon Esther was. Then said the king, Will he force the queen also before me in the house? As the word went out of the king's mouth, they covered Haman's face.",
      "M": "When the king returned from the palace garden to the banquet hall, Haman had thrown himself on the couch where Esther was reclining. The king said, 'Will he even assault the queen before me in my own house?' As the words left the king's mouth, they covered Haman's face.",
      "T": "When the king came back from the garden, he found Haman collapsed across the couch where Esther reclined — groveling for mercy. Ahasuerus chose the most damning interpretation: 'He assaults the queen in my own house, before my very eyes?' The accusation was all that was needed. The servants covered Haman's face — the ancient gesture of a condemned man. It was over."
    },
    "9": {
      "L": "And Harbonah, one of the chamberlains, said before the king, Behold also, the gallows fifty cubits high, which Haman made for Mordecai, who had spoken good for the king, standeth in the house of Haman. Then the king said, Hang him thereon.",
      "M": "Then Harbonah, one of the eunuchs attending the king, said, 'There is also the gallows, fifty cubits high, that Haman had built for Mordecai, who spoke to save the king — it stands right in Haman's house.' The king said, 'Hang him on it.'",
      "T": "One of the court officials — Harbonah, who had been there since chapter one — stepped in with a perfectly timed observation: 'There happens to be a gallows in Haman's courtyard, seventy-five feet high, built for Mordecai — the man who saved your life.' The king's reply was immediate: 'Hang him on it.' Haman would die on the instrument he had built for another man."
    },
    "10": {
      "L": "So they hanged Haman on the gallows that he had prepared for Mordecai. Then was the king's wrath pacified.",
      "M": "So they hanged Haman on the gallows he had prepared for Mordecai, and the king's wrath was appeased.",
      "T": "Haman was hanged on his own gallows — the one designed for Mordecai. The reversal could not have been more complete. And the king's fury, which had been building since Esther's revelation, was finally spent."
    }
  },
  "8": {
    "1": {
      "L": "On that day did the king Ahasuerus give the house of Haman the Jews' enemy unto Esther the queen. And Mordecai came before the king; for Esther had told what he was unto her.",
      "M": "That same day King Ahasuerus gave Queen Esther the estate of Haman, the enemy of the Jews. And Mordecai came before the king, for Esther had told the king what he was to her.",
      "T": "On the same day, the reckoning continued: the king transferred Haman's entire estate to Esther. And Mordecai was brought before the king at last — Esther had finally told Ahasuerus who Mordecai was to her. The protector emerged from the gate into the palace."
    },
    "2": {
      "L": "And the king took off his ring, which he had taken from Haman, and gave it unto Mordecai. And Esther set Mordecai over the house of Haman.",
      "M": "The king removed his signet ring — which he had recovered from Haman — and gave it to Mordecai. And Esther appointed Mordecai over the household of Haman.",
      "T": "The king placed his signet ring — the ring stripped from Haman's finger — on Mordecai's hand. The power to act in the king's name passed from Haman's memory to Mordecai's authority. Esther completed the transfer by appointing Mordecai administrator of the entire estate. The reversal was now institutional."
    },
    "3": {
      "L": "And Esther spake yet again before the king, and fell down at his feet, and besought him with tears to put away the mischief of Haman the Agagite, and his device that he had devised against the Jews.",
      "M": "And Esther spoke once more before the king, falling at his feet and weeping and pleading with him to avert the evil scheme of Haman the Agagite and the plot he had devised against the Jews.",
      "T": "But Haman's death did not undo Haman's decree. Esther fell at the king's feet — weeping now, the composed mask finally dropped — and pleaded with him to stop what had been set in motion. The edict naming every Jew in the empire for destruction was still in force. This was not finished."
    },
    "4": {
      "L": "Then the king held out the golden sceptre toward Esther. So Esther arose, and stood before the king,",
      "M": "The king held out the golden scepter to Esther, and she rose and stood before the king.",
      "T": "The golden scepter extended — the same gesture that had let her live on her first unauthorized entry. Esther rose from the floor and stood before him, ready to make her case."
    },
    "5": {
      "L": "and said, If it please the king, and if I have found favour in his sight, and the thing seem right before the king, and I be pleasing in his eyes, let it be written to reverse the letters devised by Haman the son of Hammedatha the Agagite, which he wrote to destroy the Jews which are in all the king's provinces:",
      "M": "And she said, 'If it pleases the king, and if I have found favor in his sight, and if the matter seems right to the king and I am acceptable to him — let an order be written to revoke the letters devised by Haman son of Hammedatha the Agagite, which he wrote to destroy the Jews throughout all the king's provinces.'",
      "T": "'If I have found any favor with you at all,' Esther said, 'let the letters be revoked — those letters Haman the Agagite wrote to destroy every Jew in every province of your kingdom.' She piled up every formula of courtly deference because the stakes were as high as they had ever been."
    },
    "6": {
      "L": "For how can I endure to see the evil that shall come unto my people? or how can I endure to see the destruction of my kindred?",
      "M": "'For how can I endure to see the disaster that will come upon my people? How can I bear to see the destruction of my kindred?'",
      "T": "'How could I watch my people be slaughtered? How could I bear to see my own family destroyed?' It was the simplest and most honest thing Esther had said since the crisis began. Not strategy now — just love, and fear."
    },
    "7": {
      "L": "Then the king Ahasuerus said unto Esther the queen and to Mordecai the Jew, Behold, I have given Esther the house of Haman, and him they have hanged upon the gallows, because he laid his hand on the Jews:",
      "M": "King Ahasuerus said to Queen Esther and to Mordecai the Jew, 'Behold, I have given Esther the estate of Haman, and they have hanged him on the gallows because he laid his hand against the Jews.'",
      "T": "The king laid out what he had already done — Haman's estate to Esther, Haman hanged on his own gallows — and now he handed the problem back: 'I have done what I can do. The rest is yours.'"
    },
    "8": {
      "L": "Write ye also for the Jews, as it liketh you, in the king's name, and seal it with the king's ring: for the writing which is written in the king's name, and sealed with the king's ring, may no man reverse.",
      "M": "'Now write on behalf of the Jews as you see fit, in the king's name, and seal it with the king's signet ring — for no document written in the king's name and sealed with his ring can be revoked.'",
      "T": "'Write whatever you need to write — in my name, with my seal. I cannot undo the first edict; the law of the Medes and Persians cannot be revoked. But a second edict, sealed with the same ring, can answer it. That is as far as my power goes. The rest is yours.' It was a remarkable admission of legal constraint from the most powerful man in the world."
    },
    "9": {
      "L": "Then were the king's scribes called at that time in the third month, that is, the month Sivan, on the three and twentieth day thereof; and it was written according to all that Mordecai commanded unto the Jews, and to the lieutenants, and the deputies and rulers of the provinces which are from India unto Ethiopia, an hundred twenty and seven provinces, unto every province according to the writing thereof, and unto every people after their language, and to the Jews according to their writing, and according to their language.",
      "M": "The king's scribes were summoned at that time, on the twenty-third day of the third month — the month of Sivan. Everything was written exactly as Mordecai dictated: to the Jews, to the satraps, governors, and officials of the provinces from India to Ethiopia — a hundred and twenty-seven provinces — to each province in its own script, to each people in their own language, and to the Jews in their own script and language.",
      "T": "The scribal machine of the empire was put into motion again — the same machine that had spread Haman's decree. Now it served the opposite purpose. Mordecai dictated, and his words went out in the script and tongue of every people in the empire, including the Jews' own Hebrew. Two months and ten days had passed since Haman's edict. Now its answer began to be written."
    },
    "10": {
      "L": "And he wrote in the king Ahasuerus' name, and sealed it with the king's ring, and sent letters by posts on horseback, and riders on mules, camels, and young dromedaries:",
      "M": "He wrote in the name of King Ahasuerus, sealed it with the king's signet ring, and sent the letters by mounted couriers riding on fast horses, royal thoroughbreds bred for speed.",
      "T": "Mordecai sealed the counter-edict with the king's own ring — the seal that had authorized the original death warrant — and dispatched the letters by the fastest horses in the royal stables. Speed was everything: the Jews needed time to prepare."
    },
    "11": {
      "L": "Wherein the king granted the Jews which were in every city to gather themselves together, and to stand for their life, to destroy, to slay, and to cause to perish, all the power of the people and province that would assault them, both little ones and women, and to take the spoil of them for a prey,",
      "M": "The letters granted the Jews in every city the right to assemble and defend their lives — to destroy, to kill, and to annihilate any armed force of any people or province that attacked them, including their women and children, and to plunder their possessions.",
      "T": "The counter-edict granted the Jews exactly what Haman's decree had granted their enemies: the right to kill, destroy, and plunder any who came against them. It was not permission to attack — it was the legal right of self-defense, in the Persian legal framework. The language mirrors Haman's decree almost word for word. What had been designed against them was now turned in their hands."
    },
    "12": {
      "L": "Upon one day in all the provinces of king Ahasuerus, namely, upon the thirteenth day of the twelfth month, which is the month Adar.",
      "M": "This was to be on one day throughout all the provinces of King Ahasuerus: on the thirteenth day of the twelfth month, the month of Adar.",
      "T": "One day. The same day that had been set for the Jews' annihilation. On the thirteenth of Adar, the decree of Haman and the counter-decree of Mordecai would collide."
    },
    "13": {
      "L": "The copy of the writing for a commandment to be given in every province was published unto all people, and that the Jews should be ready against that day to avenge themselves on their enemies.",
      "M": "A copy of the document was to be issued as law in every province, publicly announced to all peoples, so that the Jews would be ready on that day to take vengeance on their enemies.",
      "T": "The decree was published everywhere — not in secret, not quietly. The Jews were to know about it. Their enemies were to know the Jews knew about it. The psychological shift had already begun before a single sword was drawn."
    },
    "14": {
      "L": "So the posts that rode upon mules and camels went out, being hastened and pressed on by the king's commandment. And the decree was given at Shushan the palace.",
      "M": "The mounted couriers went out urgently, pressed on by the king's command. The decree was also issued in Susa the citadel.",
      "T": "The couriers rode out at full speed, driven by the urgency of the king's command. And in Susa itself, the citadel that had been stunned and confused by Haman's edict, the new decree was proclaimed."
    },
    "15": {
      "L": "And Mordecai went out from the presence of the king in royal apparel of blue and white, and with a great crown of gold, and with a garment of fine linen and purple: and the city of Shushan rejoiced and was glad.",
      "M": "Mordecai left the king's presence wearing royal robes of blue and white, with a large golden crown and a cloak of fine linen and purple. And the city of Susa shouted and rejoiced.",
      "T": "Mordecai walked out of the palace gates in royal regalia — blue and white robes, a great golden crown, fine linen and purple. Not long ago he had walked those streets in sackcloth. The city of Susa erupted. What they were celebrating, many of them may not have fully understood — but Mordecai's transformation from mourner to minister was visible to everyone."
    },
    "16": {
      "L": "The Jews had light, and gladness, and joy, and honour.",
      "M": "For the Jews there was light and gladness, joy and honor.",
      "T": "For the Jews: light. Gladness. Joy. Honor. Four words in the Hebrew, each a world in itself. The darkness was not yet over — the thirteenth of Adar had not come — but the shadow had lifted."
    },
    "17": {
      "L": "And in every province, and in every city, whithersoever the king's commandment and his decree came, the Jews had joy and gladness, a feast and a good day. And many of the people of the land became Jews; for the fear of the Jews fell upon them.",
      "M": "And in every province and in every city, wherever the king's command and decree arrived, there was gladness and joy among the Jews — a feast and a holiday. And many of the peoples of the land declared themselves Jews, because the fear of the Jews had fallen upon them.",
      "T": "Across the empire, in every city where the counter-decree arrived, the Jewish community erupted in celebration — feasts, holidays, the sudden return of a future. And something unprecedented happened: people who had never been Jewish began to identify themselves as Jewish. The tide of power had shifted so visibly that some chose to stand with the people who had been, hours before, condemned to extinction. The fear of Haman had given way to the fear of the God — unnamed in this book — who protected his people."
    }
  },
  "9": {
    "1": {
      "L": "Now in the twelfth month, that is, the month Adar, on the thirteenth day of the same, when the king's commandment and his decree drew near to be put in execution, in the day that the enemies of the Jews hoped to have power over them, though it was turned to the contrary, that the Jews had rule over them that hated them;",
      "M": "On the thirteenth day of the twelfth month — the month of Adar — when the king's command and decree were to be carried out, on the very day when the enemies of the Jews had hoped to overpower them, the situation was reversed: the Jews themselves gained power over those who hated them.",
      "T": "The thirteenth of Adar arrived. The day Haman had chosen by lot — the day the whole machinery of Persian law had pointed toward — was here. But something had changed everything. The enemies of the Jews had expected easy prey; they found an armed and legally protected people. The situation was reversed — a phrase that says everything without naming the one who turned it."
    },
    "2": {
      "L": "The Jews gathered themselves together in their cities throughout all the provinces of the king Ahasuerus, to lay hand on such as sought their hurt: and no man could withstand them; for the fear of them fell upon all people.",
      "M": "The Jews assembled in their cities throughout all the provinces of King Ahasuerus to strike at those who sought their harm. No one could stand against them, for the fear of the Jews had fallen on all the peoples.",
      "T": "In city after city, the Jews gathered — organized, ready, backed by a royal decree. Those who had planned to attack them now found the legal landscape had completely changed. No one could withstand them. The fear that had been weaponized against the Jews had changed direction."
    },
    "3": {
      "L": "And all the rulers of the provinces, and the lieutenants, and the deputies, and officers of the king, helped the Jews; because the fear of Mordecai fell upon them.",
      "M": "And all the provincial officials, the satraps, the governors, and the king's agents were helping the Jews, because the fear of Mordecai had fallen upon them.",
      "T": "The Persian bureaucracy that had been the instrument of Haman's plot now aligned itself with the Jews — because Mordecai's name carried the weight of the king's ring, and no official in the empire wanted to be on the wrong side of that."
    },
    "4": {
      "L": "For Mordecai was great in the king's house, and his fame went out throughout all the provinces: for this man Mordecai waxed greater and greater.",
      "M": "For Mordecai was now great in the king's palace, and his reputation spread throughout all the provinces. The man Mordecai grew greater and greater.",
      "T": "Mordecai's rise was now public and undeniable. The man who had sat at the gate in sackcloth was now second only to the king, and his authority radiated outward across the empire. Every official who had hedged could see which way the wind had permanently turned."
    },
    "5": {
      "L": "Thus the Jews smote all their enemies with the stroke of the sword, and slaughter, and destruction, and did what they would unto those that hated them.",
      "M": "The Jews struck down all their enemies with the sword — killing, destroying, and doing as they pleased with those who hated them.",
      "T": "On the day that had been intended as the day of their death, the Jews fought back. The text does not flinch from the violence; neither should the reader. This was not aggression — it was the execution of a right to survive that had very nearly been extinguished."
    },
    "6": {
      "L": "And in Shushan the palace the Jews slew and destroyed five hundred men.",
      "M": "In Susa the citadel, the Jews killed and destroyed five hundred men.",
      "T": "In the capital itself — the seat of power where everything had begun — five hundred men who had come to attack the Jews were killed."
    },
    "7": {
      "L": "And Parshandatha, and Dalphon, and Aspatha,",
      "M": "They also killed Parshandatha, Dalphon, Aspatha,",
      "T": "Among the dead were Haman's ten sons: Parshandatha, Dalphon, Aspatha,"
    },
    "8": {
      "L": "And Poratha, and Adalia, and Aridatha,",
      "M": "Poratha, Adalia, Aridatha,",
      "T": "Poratha, Adalia, Aridatha,"
    },
    "9": {
      "L": "And Parmashta, and Arisai, and Aridai, and Vajezatha,",
      "M": "Parmashta, Arisai, Aridai, and Vajezatha —",
      "T": "Parmashta, Arisai, Aridai, and Vajezatha."
    },
    "10": {
      "L": "The ten sons of Haman the son of Hammedatha, the enemy of the Jews, slew they; but on the spoil laid they not their hand.",
      "M": "The ten sons of Haman son of Hammedatha, the enemy of the Jews — they killed. But they laid no hand on the plunder.",
      "T": "Ten sons. Haman's entire line. The Agagite's legacy ended in a single day. And the Jews did not touch the plunder — not in Susa, not anywhere in the provinces. This is noted three times in this chapter. It was a deliberate choice, distinguishing their act from mere opportunism. The echo of Saul's failure at Amalek — who took the plunder when he should not have (1 Sam 15) — may be intentional."
    },
    "11": {
      "L": "On that day the number of those that were slain in Shushan the palace was brought before the king.",
      "M": "That day the number of those killed in Susa the citadel was reported to the king.",
      "T": "By evening, the casualty figures from Susa had reached the king. He summoned Esther."
    },
    "12": {
      "L": "And the king said unto Esther the queen, The Jews have slain and destroyed five hundred men in Shushan the palace, and the ten sons of Haman; what have they done in the rest of the king's provinces? now what is thy petition? and it shall be granted thee: or what is thy request further? and it shall be done.",
      "M": "The king said to Queen Esther, 'The Jews have killed and destroyed five hundred men in Susa the citadel, along with the ten sons of Haman. What have they done in the rest of the king's provinces? Now what is your petition? It shall be granted. What further is your request? It shall be fulfilled.'",
      "T": "The king gave her the news and then — for the fourth time — offered her whatever she wished. The offer was genuine, and the narrative has been building to this final request. Esther had one more thing to ask."
    },
    "13": {
      "L": "Then said Esther, If it please the king, let it be granted to the Jews which are in Shushan to do to morrow also according unto this day's decree, and let Haman's ten sons be hanged upon the gallows.",
      "M": "Esther said, 'If it please the king, let the Jews who are in Susa be permitted to do tomorrow also according to today's edict, and let the ten sons of Haman be hanged on the gallows.'",
      "T": "Esther asked for two things: one more day for the Jews of Susa to defend themselves, and the public display of Haman's sons on the gallows. The second request is jarring to modern sensibilities — but in the ancient world, the public hanging of the bodies of defeated enemies was a declaration that the threat was truly over. It was the final visual confirmation of the reversal."
    },
    "14": {
      "L": "And the king commanded it so to be done: and a decree was given at Shushan; and they hanged Haman's ten sons.",
      "M": "The king commanded it to be done. A decree was issued in Susa, and the ten sons of Haman were hanged.",
      "T": "The king agreed. A new decree went out, and the bodies of Haman's sons were displayed on the gallows — the instrument their father had built for Mordecai, now serving as the monument of his family's complete defeat."
    },
    "15": {
      "L": "For the Jews that were in Shushan gathered themselves together on the fourteenth day also of the month Adar, and slew three hundred men at Shushan; but on the prey they laid not their hand.",
      "M": "The Jews in Susa also gathered on the fourteenth day of Adar and killed three hundred more men in Susa — but they laid no hand on the plunder.",
      "T": "The Jews of Susa took their second day, killing three hundred more of those who came against them. Again, no plunder taken. The restraint was consistent and deliberate."
    },
    "16": {
      "L": "But the other Jews that were in the king's provinces gathered themselves together, and stood for their lives, and had rest from their enemies, and slew of their foes seventy and five thousand, but they laid not their hand on the prey,",
      "M": "Meanwhile the rest of the Jews throughout the king's provinces had gathered to defend their lives. They gained relief from their enemies and killed seventy-five thousand of those who hated them — but they laid no hands on the plunder.",
      "T": "Across the entire empire, the same pattern unfolded: Jewish communities defended themselves, killed those who had come to kill them, and took no spoil. Seventy-five thousand enemies dead. The victory was total. The restraint regarding plunder was equally total."
    },
    "17": {
      "L": "On the thirteenth day of the month Adar; and on the fourteenth day of the same rested they, and made it a day of feasting and gladness.",
      "M": "This was on the thirteenth day of the month of Adar. On the fourteenth day they rested and made it a day of feasting and gladness.",
      "T": "The fighting was done by the end of the thirteenth. The fourteenth was rest — and then celebration. The day after survival became the first feast of Purim."
    },
    "18": {
      "L": "But the Jews that were at Shushan assembled together on the thirteenth day thereof, and on the fourteenth thereof; and on the fifteenth day of the same they rested, and made it a day of feasting and gladness.",
      "M": "But the Jews in Susa had assembled on both the thirteenth and fourteenth days of Adar, so they rested on the fifteenth and made that their day of feasting and gladness.",
      "T": "The Jews of Susa were the exception: they had fought for two days, so they celebrated a day later — on the fifteenth. This difference between Susa and the provinces is the origin of the two-day observance of Purim: the fifteenth for walled cities, the fourteenth for everywhere else."
    },
    "19": {
      "L": "Therefore the Jews of the villages, that dwelt in the unwalled towns, made the fourteenth day of the month Adar a day of gladness and feasting, and a good day, and of sending portions one to another.",
      "M": "That is why the rural Jews — those who live in unwalled villages — keep the fourteenth day of Adar as a day of gladness and feasting, a holiday and a day for sending portions of food to one another.",
      "T": "The difference in celebration dates became codified: Jews in unwalled communities observe the fourteenth; Jews in cities that had walls in Joshua's day observe the fifteenth. The practice of sending portions of food to one another — mishloach manot — is established here as a defining mark of the feast."
    },
    "20": {
      "L": "And Mordecai wrote these things, and sent letters unto all the Jews that were in all the provinces of the king Ahasuerus, both nigh and far,",
      "M": "Mordecai recorded these events and sent letters to all the Jews throughout all the provinces of King Ahasuerus, both near and far,",
      "T": "Mordecai did what wise leaders do after a crisis: he wrote it down. Letters went to every Jewish community in the empire, preserving the record of what had happened and establishing what should be done with its memory."
    },
    "21": {
      "L": "To stablish this among them, that they should keep the fourteenth day of the month Adar, and the fifteenth day of the same, yearly,",
      "M": "To establish among them that they should observe the fourteenth and fifteenth days of the month of Adar every year,",
      "T": "The two days — the fourteenth and the fifteenth — were to be kept every year. Both of them, every year, by all the Jews in all the lands."
    },
    "22": {
      "L": "As the days wherein the Jews rested from their enemies, and the month which was turned unto them from sorrow to joy, and from mourning into a good day: that they should make them days of feasting and joy, and of sending portions one to another, and gifts to the poor.",
      "M": "As the days on which the Jews gained relief from their enemies, and the month that was turned for them from sorrow into gladness and from mourning into a holiday — they were to make them days of feasting and joy, of sending portions of food to one another and gifts to the poor.",
      "T": "The meaning of the feast was built into its description: these were the days when mourning became celebration, when the month appointed for death became the month appointed for life. The feast's two visible signs — sharing food with neighbors and giving to the poor — ensured that the reversal was felt not just privately but communally, and that it extended even to those who might otherwise have nothing to celebrate."
    },
    "23": {
      "L": "And the Jews undertook to do as they had begun, and as Mordecai had written unto them;",
      "M": "So the Jews accepted what they had already begun to practice, along with what Mordecai had written to them.",
      "T": "The community ratified what the crisis had already produced: the practice of Purim was not imposed from above — it was affirmed from within. The Jews had already begun to celebrate; Mordecai's letter gave the celebration its permanent form."
    },
    "24": {
      "L": "Because Haman the son of Hammedatha, the Agagite, the enemy of all the Jews, had devised against the Jews to destroy them, and had cast Pur, that is, the lot, to consume them, and to destroy them;",
      "M": "For Haman son of Hammedatha the Agagite, the enemy of all the Jews, had devised a plot against the Jews to destroy them and had cast the Pur — that is, the lot — to crush and destroy them.",
      "T": "The name of the feast explains itself: Pur. The lot. Haman had cast lots to find the most auspicious day for genocide. The lot fell on the thirteenth of Adar — and the thirteenth of Adar became the day of his own defeat. The feast is named after the tool of his planning, which became the monument of his failure."
    },
    "25": {
      "L": "But when Esther came before the king, he commanded by letters that his wicked device, which he devised against the Jews, should return upon his own head, and that he and his sons should be hanged on the gallows.",
      "M": "But when Esther came before the king, he ordered by letter that Haman's evil scheme against the Jews should fall back on his own head, and that he and his sons should be hanged on the gallows.",
      "T": "Everything Haman had planned turned back on himself. His letters authorized destruction; the king's letters reversed that destruction. His gallows were built for another man; they held Haman. His sons were the pride of his dynasty; they died on the same wood. The reversal was complete at every level."
    },
    "26": {
      "L": "Wherefore they called these days Purim after the name of Pur. Therefore for all the words of this letter, and of that which they had seen concerning this matter, and which had come unto them,",
      "M": "Therefore they called these days Purim, after the word Pur. And because of everything written in this letter, and because of what they had witnessed and experienced in this matter,",
      "T": "The name was chosen deliberately. Not 'the days of Esther,' not 'the days of Mordecai,' but Purim — the lots Haman had cast. The festival bears the name of the enemy's instrument, forever commemorating the fact that his own planning device was turned against him."
    },
    "27": {
      "L": "The Jews ordained, and took upon them, and upon their seed, and upon all such as joined themselves unto them, so as it should not fail, that they would keep these two days according to their writing, and according to their appointed time every year;",
      "M": "The Jews established and accepted for themselves, for their descendants, and for all who joined their community — without exception — that they would observe these two days as prescribed and at their appointed time, year after year.",
      "T": "The Jews — including those who had joined themselves to the covenant community — formally committed to the observance. The language is legally binding: this was not a suggestion but an adopted obligation, passed to every generation and every proselyte. Purim would not be forgotten."
    },
    "28": {
      "L": "And that these days should be remembered and kept throughout every generation, every family, every province, and every city; and that these days of Purim should not fail from among the Jews, nor the memorial of them perish from their seed.",
      "M": "These days were to be remembered and kept in every generation, every family, every province, and every city — and these days of Purim must never cease among the Jews, nor their remembrance perish from their descendants.",
      "T": "The four-fold repetition — every generation, every family, every province, every city — was deliberate. No gap was to be left. No community, no family, no individual generation could claim exemption. The memory of near-extinction and miraculous survival was to be embedded in Jewish communal life permanently."
    },
    "29": {
      "L": "Then Esther the queen, the daughter of Abihail, and Mordecai the Jew, wrote with all authority, to confirm this second letter of Purim.",
      "M": "Then Queen Esther daughter of Abihail, along with Mordecai the Jew, wrote with full authority to confirm this second letter about Purim.",
      "T": "Mordecai had written first; now Esther added her own authority — her full name and lineage invoked, her royal title claimed. Together, the queen and the man at the gate put their names to the institution of the feast. The woman who had concealed her identity for years now declared it publicly, permanently, in a letter that would be read in every generation."
    },
    "30": {
      "L": "And he sent the letters unto all the Jews, to the hundred twenty and seven provinces of the kingdom of Ahasuerus, with words of peace and truth,",
      "M": "And Mordecai sent letters to all the Jews throughout the hundred and twenty-seven provinces of the kingdom of Ahasuerus, with words of peace and truth,",
      "T": "The letters went out to every corner of the empire — a hundred and twenty-seven provinces, the same number given at the book's opening. The empire that had nearly been the instrument of Jewish destruction now carried the letters that established Jewish survival as an annual celebration. The words were 'peace and truth' — shalom and emet — the covenantal language of integrity and wholeness."
    },
    "31": {
      "L": "To confirm these days of Purim in their times appointed, according as Mordecai the Jew and Esther the queen had enjoined them, and as they had decreed for themselves and for their seed, the matters of the fastings and their cry.",
      "M": "To confirm these days of Purim at their appointed times, as Mordecai the Jew and Queen Esther had prescribed — and as they had established for themselves and for their descendants, with regard to their fasting and their lamenting.",
      "T": "The feast of Purim was inseparable from the fast that preceded it — the three-day fast of Esther (ch. 4:16) was woven into the commemorative fabric of the celebration. Joy without remembered sorrow is not the same feast. The fast and the feast together told the complete story: the danger had been real, the deliverance had been miraculous, and both deserved to be commemorated."
    },
    "32": {
      "L": "And the decree of Esther confirmed these matters of Purim; and it was written in the book.",
      "M": "The command of Esther confirmed these regulations of Purim, and it was recorded in the book.",
      "T": "Esther's decree sealed it. The feast established by the events of the story was now confirmed by the authority of the woman at the center of those events. And it was written in the book — a phrase that echoes the royal chronicles throughout Esther, placing this act alongside the great records of the empire. The story of the Jewish people's deliverance was now part of the permanent record of history."
    }
  },
  "10": {
    "1": {
      "L": "And the king Ahasuerus laid a tribute upon the land, and upon the isles of the sea.",
      "M": "King Ahasuerus imposed tribute on the land and on the islands of the sea.",
      "T": "The epilogue opens with the empire back to its routine: Ahasuerus collecting tribute from the land and the islands. Business as usual. The machinery of empire runs on, indifferent to the drama that nearly destroyed a people within it."
    },
    "2": {
      "L": "And all the acts of his power and of his might, and the declaration of the greatness of Mordecai, whereunto the king advanced him, are they not written in the book of the chronicles of the kings of Media and Persia?",
      "M": "And all the acts of the king's power and strength, and the full account of the greatness of Mordecai, to which the king had advanced him — are they not written in the Book of the Chronicles of the Kings of Media and Persia?",
      "T": "The narrator points to the royal archives — the same chronicles whose chance reading had set off the chain of events in chapter six. Mordecai's story was in those records, alongside the acts of kings. A Jewish exile, the descendant of deportees, had written himself into the imperial record. The book of Esther invites comparison to those other exilic stories of faithful Jews exalted to second-in-command: Joseph in Egypt, Daniel in Babylon. The pattern recurs."
    },
    "3": {
      "L": "For Mordecai the Jew was next unto king Ahasuerus, and great among the Jews, and accepted of the multitude of his brethren, seeking the wealth of his people, and speaking peace to all his seed.",
      "M": "For Mordecai the Jew was second only to King Ahasuerus and was great among the Jews, beloved by the multitude of his people, for he sought the welfare of his people and spoke peace to all his descendants.",
      "T": "The book ends where it could only end: with Mordecai. Second only to the king — the same phrase used of Joseph (Gen 41:40). Great in the empire, but never alienated from his own people. Beloved, not feared. Seeking their welfare — shalom, the Hebrew wholeness that encompasses safety, prosperity, and flourishing. The book that never names God closes with a man whose life was shaped by the unseen hand that turned everything to the contrary — and who used his position not for self-enrichment but for the peace of his people."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'esther')
        merge_tier(existing, ESTHER, tier_key)
        save(tier_dir, 'esther', existing)
    print('Esther 7–10 written.')

if __name__ == '__main__':
    main()
