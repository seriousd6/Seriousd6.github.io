"""
MKT 2 Samuel chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2samuel-19-24.py

Translation decisions (continuing conventions from mkt-2samuel-1-6.py):
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout. T uses "the LORD" in narrative;
  in ch22 poetry T follows the psalm's own voice — "the LORD" as invoked deity.
- H430 (אֱלֹהִים): "God" in all tiers. In ch22 "the God of my rock" (v3) preserved as divine title.
- H6697 (ṣûr, "rock"): Major divine epithet in ch22. L/M "Rock"; T "Rock" (capitalised as title).
  In 22:47 "blessed be my rock" = divine title. In 23:3 "the Rock of Israel" = same. Consistent cap.
- H2617 (חֶסֶד): "steadfast love" in L/M; T "covenant faithfulness" or "steadfast loyalty" per context.
  In 22:51 "sheweth mercy to his anointed" = the great closing line — T renders it
  "shows covenant faithfulness to his anointed." Continues from prior script.
- H5315 (נֶפֶשׁ): "soul" in L; "life" in M/T where the embodied self is meant (19:5, 24:17).
- H7307 (רוּחַ): In 23:2 "The Spirit of the LORD spoke by me" — clear prophetic-Spirit context.
  L "Spirit"; M "Spirit"; T "Spirit." Capitalised throughout as divine agent.
- H1285 (בְּרִית): In 23:5 "everlasting covenant" — the Davidic covenant. "covenant" in all tiers;
  T adds the theological weight: "everlasting covenant, ordered in all things and sure."
- H4899 (māšîaḥ, "anointed"): 22:51 and 23:1. L "anointed"; M "anointed"; T "anointed one" in 23:1
  to mark its messianic resonance; "anointed" in 22:51 to preserve the covenant-closure force.
- H5650 (ʿebed, "servant"): Continues from prior script — "servant" in L; M/T contextual.
- H1100 (Belial): 23:6 "sons of Belial" = worthless/wicked men. L "sons of Belial"; M "worthless men";
  T "men of no worth" — preserving the sense of utter moral emptiness.
- H5971 (ʿam, "people"): "people" throughout; in ch22 poetic context can be "nations/peoples."
- H1471 (gôy, "nation/Gentiles"): 22:44,50 = "nations/heathen." L "nations"; M "nations"; T "nations."
- H1343 (ṣĕdāqāh) / H6664 (ṣedeq) righteousness: Ch22 "according to my righteousness" — these are
  covenant-fidelity terms, not moral perfection claims. T surfaces this: "faithfulness to the
  covenant" or "clean hands before him." See v21-25 note below.
- H3444 (yĕšûʿāh, "salvation/victory"): 22:51 "tower of salvation" = tower of victories/saves.
  L "salvation"; M "salvation"; T "great victories."
- Poetic structure: Ch22 and 23:1–7 are Hebrew poetry. T tier uses line breaks throughout both.
  L and M are elevated prose for ch22, preserving the parallelism but without forcing line breaks.
- Ch22 v21–25 (righteousness passages): David's claim to righteousness is a covenant-fidelity claim
  (he kept the terms of his relationship with God), not a claim to sinlessness. T makes this clear.
- Ch21:1–9 (Gibeonites): The execution of Saul's sons is a blood-guilt atonement demanded by the
  Gibeonites — not arbitrary violence. L/M present straightforwardly; T notes the atonement structure.
- Ch24:1 (the census): The theological problem — God's anger leads him to incite David to take a
  census, which is then punished. 1 Chr 21:1 says Satan incited him. L/M render the text as it stands;
  T notes the theological tension without resolving it.
- H6160 (ʿărābāh) = the Arabah/Jordan valley. Place-name preserved throughout.
- Aspect: waw-consecutive imperfects = narrative past (simple past in English). Perfect = completed
  states. Jussives in ch22/23 = wishes/declarations, rendered with modal force.
- OT echo notes: Ch22 = Psalm 18 (nearly verbatim). The shared text is the great royal thanksgiving.
  23:1–7 = royal oracle in the style of the Balaam oracles (Num 24). The Davidic covenant here
  anticipates Isaiah's Servant Songs and ultimately the messianic expectation.
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

SAMUEL = {
  "19": {
    "1": {
      "L": "And it was told Joab, 'Behold, the king is weeping and mourning for Absalom.'",
      "M": "Joab was told, 'The king is weeping and mourning for Absalom.'",
      "T": "Word reached Joab: the king was weeping. Mourning for Absalom."
    },
    "2": {
      "L": "And the victory that day was turned into mourning for all the people, for the people heard that day, 'The king is grieving for his son.'",
      "M": "The victory that day was turned to mourning for all the people, for they heard that day, 'The king is in grief over his son.'",
      "T": "The day's victory collapsed into mourning. Word spread through all the army: the king was in grief over his son."
    },
    "3": {
      "L": "And the people stole back into the city that day as people steal in who are ashamed when they flee in battle.",
      "M": "The people crept back into the city that day like soldiers slipping in under cover of shame after a rout in battle.",
      "T": "The troops crept back into the city that day like men who had fled a battle in disgrace—skulking in, not marching."
    },
    "4": {
      "L": "But the king covered his face, and the king cried out with a loud voice, 'O my son Absalom! O Absalom, my son, my son!'",
      "M": "The king had covered his face and was crying out loudly, 'O my son Absalom! O Absalom, my son, my son!'",
      "T": "The king had covered his face and was crying out with a broken voice: 'Absalom! O Absalom, my son—my son!'"
    },
    "5": {
      "L": "Then Joab came into the house to the king and said, 'You have today put to shame the faces of all your servants, who have this day saved your life and the lives of your sons and your daughters and the lives of your wives and the lives of your concubines,",
      "M": "Then Joab went into the house to the king and said, 'Today you have shamed all your servants who saved your life today, and the lives of your sons, your daughters, your wives, and your concubines,",
      "T": "Joab came in to the king and said bluntly: 'You have shamed every man who saved your life today—your sons, your daughters, your wives, your concubines—"
    },
    "6": {
      "L": "'by loving those who hate you and hating those who love you. For you have declared today that commanders and servants are nothing to you, for I know today that if Absalom were alive and all of us were dead today, then it would please you.'",
      "M": "'by loving those who hate you and hating those who love you. You have made clear today that your commanders and servants mean nothing to you. I know that if Absalom were alive and all of us dead today, it would please you.'",
      "T": "'—by loving those who hate you and hating those who love you. You have made it plain: your commanders and your men count for nothing. If Absalom were alive and we were all dead today, you would be satisfied.'"
    },
    "7": {
      "L": "'Now therefore arise, go out and speak kindly to your servants, for I swear by the LORD, if you do not go out, not a man will stay with you this night; and that will be worse for you than all the evil that has come upon you from your youth until now.'",
      "M": "'Now get up, go out, and speak encouragingly to your servants. I swear by the LORD, if you do not go out, not one man will remain with you tonight. That will be worse for you than any disaster that has befallen you from your youth until now.'",
      "T": "'Get up. Go out and speak a word of encouragement to your men. I swear by the LORD: if you do not go out, not a single man will be with you by morning. That will be worse for you than every evil that has ever come on you from your earliest days until now.'"
    },
    "8": {
      "L": "So the king arose and sat in the gate. And they told all the people, saying, 'Behold, the king is sitting in the gate.' And all the people came before the king. Now Israel had fled, every man to his own tent.",
      "M": "So the king got up and sat in the gate. When all the people were told, 'The king is sitting in the gate,' they all came before him. Meanwhile Israel had fled, every man to his own home.",
      "T": "The king got up and took his seat at the city gate. Word went out: the king is at the gate. The people came, every one of them. But all Israel had already scattered—each man to his own tent."
    },
    "9": {
      "L": "And all the people were arguing throughout all the tribes of Israel, saying, 'The king delivered us from the hand of our enemies and saved us from the hand of the Philistines, and now he has fled out of the land from Absalom.'",
      "M": "All the people throughout all the tribes of Israel were disputing, saying, 'The king rescued us from our enemies and saved us from the Philistines, and now he has fled the land because of Absalom.'",
      "T": "All across the tribes of Israel, the people were arguing: 'The king is the one who rescued us from our enemies, who saved us from the Philistines. Now he has fled the land because of Absalom.'"
    },
    "10": {
      "L": "'And Absalom, whom we anointed over us, has died in battle. Now therefore why are you silent about bringing the king back?'",
      "M": "'But Absalom, whom we anointed over us, is dead in battle. Why are you saying nothing about bringing the king back?'",
      "T": "'And Absalom—the man we anointed as king—is dead. So why is no one saying a word about bringing David back?'"
    },
    "11": {
      "L": "And King David sent to Zadok and Abiathar the priests, saying, 'Speak to the elders of Judah, saying, \"Why are you the last to bring the king back to his house? The word of all Israel has come to the king, even to his house.\"'",
      "M": "King David sent word to the priests Zadok and Abiathar: 'Say to the elders of Judah, \"Why should you be the last to bring the king back to his own house? All Israel has spoken; word has reached the king at his quarters.\"'",
      "T": "King David sent word to the priests Zadok and Abiathar: 'Tell the elders of Judah: why should you be the last to bring the king home? All Israel is already talking. Why is Judah slow?'"
    },
    "12": {
      "L": "'You are my brothers; you are my bone and my flesh. Why then should you be the last to bring back the king?'",
      "M": "'You are my kinsmen—my own bone and flesh. Why should you be last to bring the king back?'",
      "T": "'You are my brothers. My own bone and blood. Why should you be the last to bring your king home?'"
    },
    "13": {
      "L": "'And say to Amasa, \"Are you not my bone and my flesh? God do so to me and more also, if you are not commander of my army before me continually in place of Joab.\"'",
      "M": "'And say to Amasa, \"Are you not my own flesh and blood? God do so to me and more if you are not the commander of my army from now on, in place of Joab.\"'",
      "T": "'And say to Amasa: You are my own flesh and blood. God deal with me as he sees fit if you are not commander of my army from this day on, in Joab's place.'"
    },
    "14": {
      "L": "And he swayed the heart of all the men of Judah as one man, and they sent word to the king, 'Return, you and all your servants.'",
      "M": "He won over the hearts of all the men of Judah as one man, and they sent word to the king, 'Return, you and all your servants.'",
      "T": "He turned the hearts of all the men of Judah—as one man—and they sent to the king: 'Come back, you and all who are with you.'"
    },
    "15": {
      "L": "So the king returned and came to the Jordan. And Judah came to Gilgal to go to meet the king, to bring the king over the Jordan.",
      "M": "The king returned and reached the Jordan. Judah had come to Gilgal to meet the king and escort him across the Jordan.",
      "T": "The king turned back and came to the Jordan. Judah had assembled at Gilgal to meet him and bring him across."
    },
    "16": {
      "L": "And Shimei the son of Gera, the Benjaminite, from Bahurim, hurried and came down with the men of Judah to meet King David.",
      "M": "Shimei son of Gera the Benjaminite, from Bahurim, hurried down with the men of Judah to meet King David.",
      "T": "Shimei son of Gera the Benjaminite—from Bahurim, the man who had cursed David—came hurrying down with the men of Judah to meet the king."
    },
    "17": {
      "L": "With him were a thousand men from Benjamin, and Ziba the servant of the house of Saul, with his fifteen sons and his twenty servants, and they rushed to the Jordan before the king.",
      "M": "With him were a thousand Benjaminites, and Ziba the servant of Saul's household with his fifteen sons and twenty servants. They waded across the Jordan ahead of the king.",
      "T": "A thousand men from Benjamin were with him, and Ziba the steward of Saul's household—his fifteen sons and twenty servants—all crossing the Jordan to get to the king first."
    },
    "18": {
      "L": "And they crossed the ford to bring over the king's household and to do what seemed good to him. And Shimei the son of Gera fell down before the king when he was about to cross the Jordan.",
      "M": "They crossed the ford to help bring the king's household over and to serve the king as he wished. Shimei son of Gera fell prostrate before the king just as he was crossing the Jordan.",
      "T": "They crossed the ford to help move the king's household and to serve him in any way he required. Shimei son of Gera threw himself down before the king just as David reached the ford."
    },
    "19": {
      "L": "And he said to the king, 'Let not my lord reckon to me the guilt, or remember how your servant did wrong on the day my lord the king left Jerusalem, so that the king should take it to heart.'",
      "M": "He said to the king, 'May my lord not hold me guilty or remember the wrong your servant did on the day my lord the king left Jerusalem. May the king put it out of his mind.'",
      "T": "'My lord the king—do not count it against me. Do not remember what your servant did wrong on the day you left Jerusalem. Let the king put it from his heart.'"
    },
    "20": {
      "L": "'For your servant knows that I have sinned. And behold, I have come today as the first of all the house of Joseph to go down to meet my lord the king.'",
      "M": "'Your servant knows he sinned. And see—I have come today, the first of all the house of Joseph, to come down and meet my lord the king.'",
      "T": "'I know what I did was sin. But look—today I am the first of all Joseph's house to come down to meet my lord the king.'"
    },
    "21": {
      "L": "But Abishai the son of Zeruiah answered and said, 'Should not Shimei be put to death for this, because he cursed the LORD's anointed?'",
      "M": "Abishai son of Zeruiah spoke up: 'Should not Shimei be put to death for this? He cursed the LORD's anointed.'",
      "T": "But Abishai son of Zeruiah cut in: 'Should Shimei not die for this? He cursed the LORD's anointed.'"
    },
    "22": {
      "L": "But David said, 'What have I to do with you, you sons of Zeruiah, that you should this day be my adversaries? Should anyone be put to death in Israel this day? For do I not know that today I am king over Israel?'",
      "M": "David replied, 'What business is this between you and me, you sons of Zeruiah? Why should you be my adversaries today? Should anyone be executed in Israel today? Do I not know that today I am king over Israel?'",
      "T": "David said: 'What is it with you sons of Zeruiah? Why do you become my opponents today? Should any man die in Israel today? Do I not know that today I am king over Israel?'"
    },
    "23": {
      "L": "And the king said to Shimei, 'You shall not die.' And the king gave him his oath.",
      "M": "The king said to Shimei, 'You shall not die.' And the king swore it to him.",
      "T": "The king said to Shimei, 'You will not die.' He gave him his word under oath."
    },
    "24": {
      "L": "And Mephibosheth the son of Saul came down to meet the king. He had not cared for his feet, nor trimmed his beard, nor washed his clothes, from the day the king departed until the day he came home in safety.",
      "M": "Mephibosheth son of Saul came down to meet the king. He had not cared for his feet, trimmed his beard, or washed his clothes from the day the king left until the day he returned safely.",
      "T": "Mephibosheth son of Saul came down to meet the king. He had not trimmed his beard, or washed his clothes, or tended his feet from the day David left until the day he came back safe."
    },
    "25": {
      "L": "When he came to Jerusalem to meet the king, the king said to him, 'Why did you not go with me, Mephibosheth?'",
      "M": "When he came from Jerusalem to meet the king, the king asked him, 'Why did you not come with me, Mephibosheth?'",
      "T": "When he came to meet the king at Jerusalem, David asked him, 'Mephibosheth—why didn't you come with me?'"
    },
    "26": {
      "L": "He answered, 'My lord, O king, my servant deceived me, for your servant said to him, \"Saddle a donkey for me that I may ride on it and go with the king,\" for your servant is lame.'",
      "M": "He answered, 'My lord the king, my servant Ziba deceived me. I told him, \"Saddle a donkey for me so I can ride and go with the king\"—for your servant is lame.'",
      "T": "'My lord the king—my servant deceived me. I told him to saddle a donkey so I could ride and go with you. I am lame; I could not go on foot.'"
    },
    "27": {
      "L": "'And he has slandered your servant to my lord the king. But my lord the king is like the angel of God; do therefore what is good in your eyes.'",
      "M": "'He slandered me to my lord the king. But my lord the king is like an angel of God—do whatever seems right to you.'",
      "T": "'He slandered me to you, my lord. But you are like an angel of God—do what is right in your eyes.'"
    },
    "28": {
      "L": "'For all my father's house were nothing but dead men before my lord the king, yet you set your servant among those who eat at your table. What further right have I to cry to the king?'",
      "M": "'All of my father's household deserved nothing but death from my lord the king, yet you placed your servant among those who eat at your table. What right do I have to complain further to the king?'",
      "T": "'All my father's house deserved death from you, my lord. Yet you gave me a place at your table. What further claim could I make to the king?'"
    },
    "29": {
      "L": "The king said to him, 'Why speak any more of your affairs? I have decided: you and Ziba shall divide the land.'",
      "M": "The king said to him, 'Why go on talking about this? I have decided: you and Ziba will divide the land between you.'",
      "T": "'Enough,' the king said. 'The matter is settled: you and Ziba divide the land.'"
    },
    "30": {
      "L": "And Mephibosheth said to the king, 'Even let him take it all, since my lord the king has come safely home.'",
      "M": "Mephibosheth said to the king, 'Let him have it all, since my lord the king has returned home safely.'",
      "T": "Mephibosheth said, 'Let him take everything—since my lord the king has come home in peace.'"
    },
    "31": {
      "L": "Now Barzillai the Gileadite had come down from Rogelim, and he went on with the king to the Jordan to escort him over the Jordan.",
      "M": "Barzillai the Gileadite had come down from Rogelim, and he accompanied the king to the Jordan to see him across.",
      "T": "Barzillai the Gileadite had come down from Rogelim and escorted the king to the Jordan to see him safely across."
    },
    "32": {
      "L": "Now Barzillai was very aged, eighty years old. He had provided the king with provisions while he was at Mahanaim, for he was a very wealthy man.",
      "M": "Barzillai was a very old man, eighty years old. He had provided for the king during his stay at Mahanaim, for he was a man of great wealth.",
      "T": "Barzillai was eighty years old—a very old man. He had supplied the king throughout his stay at Mahanaim, being a man of great means."
    },
    "33": {
      "L": "And the king said to Barzillai, 'Come over with me, and I will provide for you while you are with me in Jerusalem.'",
      "M": "The king said to Barzillai, 'Cross over with me and I will look after you in Jerusalem.'",
      "T": "'Come across with me,' the king said to Barzillai. 'I will provide for you in Jerusalem.'"
    },
    "34": {
      "L": "But Barzillai said to the king, 'How many years do I still have, that I should go up with the king to Jerusalem?'",
      "M": "But Barzillai replied to the king, 'How many years do I have left that I should go up with the king to Jerusalem?'",
      "T": "Barzillai answered: 'How many years do I have left? Why should I go up to Jerusalem with the king?'"
    },
    "35": {
      "L": "'I am this day eighty years old. Can I discern between good and bad? Can your servant taste what he eats or what he drinks? Can I still hear the voice of singing men and singing women? Why then should your servant be an added burden to my lord the king?'",
      "M": "'I am eighty years old today. Can I tell the difference between what is pleasant and what is not? Can your servant taste what he eats or drinks? Can I still hear the voices of singers? Why should your servant become a burden to my lord the king?'",
      "T": "'I am eighty years old. I can no longer taste food or drink or tell good from bad. I can't even hear the voices of singers. Why should I be a burden to my lord the king?'"
    },
    "36": {
      "L": "'Your servant will go a little way over the Jordan with the king. Why should the king repay me with such a reward?'",
      "M": "'Your servant will cross the Jordan with the king for a little way. Why should the king give me such a reward?'",
      "T": "'I will cross the Jordan with you just a little way. Why should the king recompense me so?'"
    },
    "37": {
      "L": "'Please let your servant turn back, that I may die in my own city near the grave of my father and my mother. But here is your servant Chimham; let him go over with my lord the king, and do for him whatever seems good to you.'",
      "M": "'Let your servant turn back, so that I may die in my own city by the tombs of my father and mother. But here is your servant Chimham—let him go over with my lord the king, and do for him whatever pleases you.'",
      "T": "'Let me turn back and die in my own city, near the graves of my father and mother. But here is your servant Chimham—let him go with my lord the king. Do for him whatever seems right to you.'"
    },
    "38": {
      "L": "And the king answered, 'Chimham shall go over with me, and I will do for him whatever seems good to you. And everything you desire from me I will do for you.'",
      "M": "The king answered, 'Chimham will cross with me and I will do for him whatever pleases you. And anything you want from me I will do for you.'",
      "T": "The king said, 'Chimham will come with me. I will do for him whatever you ask. And anything you desire from me, I will do.'"
    },
    "39": {
      "L": "Then all the people went over the Jordan, and the king crossed over. And the king kissed Barzillai and blessed him, and he returned to his own home.",
      "M": "All the people crossed the Jordan, and the king crossed over. The king kissed Barzillai and blessed him, and Barzillai returned to his own home.",
      "T": "All the people crossed the Jordan; the king crossed over. The king kissed Barzillai and gave him his blessing. Then Barzillai went home."
    },
    "40": {
      "L": "The king went on to Gilgal, and Chimham went on with him. All the people of Judah, and also half the people of Israel, escorted the king.",
      "M": "The king went on to Gilgal with Chimham at his side. All the people of Judah and half the people of Israel accompanied the king.",
      "T": "The king moved on to Gilgal, Chimham with him. All the people of Judah and half of Israel escorted the king."
    },
    "41": {
      "L": "And behold, all the men of Israel came to the king and said to the king, 'Why have our brothers the men of Judah stolen you away and brought the king and his household over the Jordan, and all David's men with him?'",
      "M": "Then all the men of Israel came to the king and said, 'Why did our brothers, the men of Judah, spirit you away and bring the king and his household over the Jordan, along with all David's men?'",
      "T": "All the men of Israel came to the king with their complaint: 'Why did our brothers of Judah steal you away—bringing the king and his household across the Jordan, and all his men—without us?'"
    },
    "42": {
      "L": "And all the men of Judah answered the men of Israel, 'Because the king is our close relative. Why then are you angry over this matter? Have we eaten anything at the king's expense? Or has he given us any gift?'",
      "M": "All the men of Judah answered the men of Israel, 'Because the king is our kinsman. Why are you angry over this? Have we eaten anything at the king's expense, or received any gift from him?'",
      "T": "The men of Judah answered Israel: 'The king is our kinsman. Why are you angry? Have we taken anything from him? Has he given us a single gift?'"
    },
    "43": {
      "L": "And the men of Israel answered the men of Judah and said, 'We have ten shares in the king, and in David also we have more than you. Why then did you despise us? Was it not our advice first to bring back our king?' But the words of the men of Judah were fiercer than the words of the men of Israel.",
      "M": "The men of Israel answered the men of Judah, 'We have ten shares in the king, and in David we have more claim than you! Why then did you despise us? Were we not the first to speak of bringing back our king?' But the words of the men of Judah were fiercer than the words of the men of Israel.",
      "T": "Israel shot back: 'We have ten shares in the king—we have greater claim on David than you do. Why did you despise us? Were we not the first to speak about bringing the king home?' But the men of Judah spoke more harshly than the men of Israel."
    }
  },
  "20": {
    "1": {
      "L": "Now there happened to be there a worthless man whose name was Sheba the son of Bichri, a Benjaminite. And he blew the trumpet and said, 'We have no portion in David, and we have no inheritance in the son of Jesse; every man to his tents, O Israel!'",
      "M": "There happened to be there a worthless man named Sheba son of Bichri, a Benjaminite. He blew the trumpet and declared, 'We have no portion in David, and no inheritance in the son of Jesse! Every man to his tent, Israel!'",
      "T": "There was a worthless man there named Sheba son of Bichri, a Benjaminite. He blew the horn and called out: 'We have no share in David, no inheritance in Jesse's son! Every man back to his own tent—Israel, go home!'"
    },
    "2": {
      "L": "So all the men of Israel withdrew from David and followed Sheba the son of Bichri. But the men of Judah followed their king steadfastly from the Jordan to Jerusalem.",
      "M": "So all the men of Israel left David and followed Sheba son of Bichri. But the men of Judah stayed with their king all the way from the Jordan to Jerusalem.",
      "T": "All the men of Israel abandoned David and went after Sheba son of Bichri. But the men of Judah stayed loyal to their king from the Jordan all the way to Jerusalem."
    },
    "3": {
      "L": "And David came to his house at Jerusalem. And the king took the ten concubines whom he had left to care for the house and put them in a house under guard and provided for them, but did not go in to them. So they were shut up until the day of their death, living as widows.",
      "M": "David arrived at his palace in Jerusalem. He took the ten concubines whom he had left to look after the palace and put them in a protected house, where he provided for them but did not sleep with them. They were confined until the day they died, living as if in widowhood.",
      "T": "When David reached his palace in Jerusalem, he took the ten concubines he had left behind to keep the household. He placed them in a guarded house and provided for them, but he never again went in to them. They lived there, shut away, for the rest of their lives—as if widowed but not widowed."
    },
    "4": {
      "L": "Then the king said to Amasa, 'Call up the men of Judah for me within three days, and be here yourself.'",
      "M": "The king said to Amasa, 'Summon the men of Judah for me within three days, and be here yourself.'",
      "T": "The king ordered Amasa: 'Muster the men of Judah—three days. And be here yourself.'"
    },
    "5": {
      "L": "So Amasa went to call up Judah, but he delayed beyond the appointed time that had been set for him.",
      "M": "Amasa went to call up Judah, but he took longer than the set time allotted to him.",
      "T": "Amasa went to muster Judah, but he was late—he missed the deadline."
    },
    "6": {
      "L": "And David said to Abishai, 'Now Sheba the son of Bichri will do us more harm than Absalom. Take your lord's servants and pursue him, lest he find for himself fortified cities and escape our sight.'",
      "M": "David said to Abishai, 'Sheba son of Bichri will do us more harm than Absalom. Take your lord's men and pursue him before he finds walled cities to shelter in and slips away from us.'",
      "T": "David said to Abishai, 'Sheba son of Bichri will do us more damage than Absalom ever did. Take the men and go after him now—before he finds fortified cities to hide in and escapes us.'"
    },
    "7": {
      "L": "And there went out after him Joab's men and the Cherethites and the Pelethites and all the mighty men. They went out from Jerusalem to pursue Sheba the son of Bichri.",
      "M": "So Joab's men went out with the Cherethites and the Pelethites and all the warriors. They marched out from Jerusalem to pursue Sheba son of Bichri.",
      "T": "Joab's men went out along with the Cherethites and Pelethites and all the fighting men—out from Jerusalem in pursuit of Sheba son of Bichri."
    },
    "8": {
      "L": "When they were at the large stone that is in Gibeon, Amasa came to meet them. Now Joab was wearing a soldier's garment, and over it was a belt with a sword in its sheath fastened at his hip, and as he went forward it fell out.",
      "M": "When they were at the great stone in Gibeon, Amasa came to meet them. Joab was dressed in military clothes, with a belt strapped around him; a sword in its sheath was at his thigh, and as he stepped forward it slipped out.",
      "T": "They were at the great stone in Gibeon when Amasa came to meet them. Joab was in military dress, with a sword belted at his thigh—and as he moved forward, it slipped from the sheath."
    },
    "9": {
      "L": "And Joab said to Amasa, 'Is it well with you, my brother?' And Joab took Amasa by the beard with his right hand to kiss him.",
      "M": "Joab said to Amasa, 'Are you well, my brother?' And with his right hand Joab grabbed Amasa by the beard to kiss him.",
      "T": "'Are you well, brother?' Joab said to Amasa—and grabbed him by the beard with his right hand to give him a kiss."
    },
    "10": {
      "L": "But Amasa did not notice the sword that was in Joab's hand. And Joab struck him with it in the stomach and spilled his intestines to the ground without striking him a second time, and he died. Then Joab and Abishai his brother pursued Sheba the son of Bichri.",
      "M": "Amasa did not notice the sword in Joab's hand. Joab drove it into his stomach and his intestines poured out onto the ground. He did not need to strike him again, and he died. Then Joab and his brother Abishai continued the pursuit of Sheba son of Bichri.",
      "T": "Amasa did not see the sword in Joab's hand. Joab drove it into his stomach—and his intestines spilled out on the ground. One blow was enough. He died. Then Joab and Abishai pressed on after Sheba son of Bichri."
    },
    "11": {
      "L": "And one of Joab's young men stood by him and said, 'Whoever favors Joab, and whoever is for David, let him follow Joab.'",
      "M": "One of Joab's men stood over Amasa and called out, 'Whoever supports Joab and whoever is for David—follow Joab!'",
      "T": "One of Joab's men stood over the body and called out: 'If you are for Joab and for David, follow Joab!'"
    },
    "12": {
      "L": "And Amasa lay wallowing in his blood in the middle of the road. And the man saw that all the people stood still, so he moved Amasa from the road into the field and threw a garment over him, because he saw that all who came by him stopped.",
      "M": "Amasa was lying, wallowing in his blood, in the middle of the road. The man saw that all the troops were stopping there, so he dragged Amasa off the road into the field and threw a cloth over him, since everyone who came near him stopped.",
      "T": "Amasa lay in the middle of the road, soaked in his own blood. Every man who came by stopped to look. So Joab's man dragged the body off the road into the field and threw a garment over it—and once it was covered, the men moved on."
    },
    "13": {
      "L": "When he was removed from the road, all the men went on after Joab to pursue Sheba the son of Bichri.",
      "M": "Once he was off the road, every man went on after Joab to pursue Sheba son of Bichri.",
      "T": "With the body out of sight, all the men followed Joab in the pursuit of Sheba son of Bichri."
    },
    "14": {
      "L": "And Sheba passed through all the tribes of Israel to Abel Beth-maacah, and all the Bichrites assembled and followed him in.",
      "M": "Sheba passed through all the tribes of Israel to Abel Beth-maacah, and all the Bichrites assembled and followed him there.",
      "T": "Sheba moved through all the tribes of Israel and came to Abel Beth-maacah. All the Bichrites assembled there and followed him into the city."
    },
    "15": {
      "L": "And all the men with Joab came and besieged him in Abel Beth-maacah. They cast up a siege mound against the city, and it stood against the outer rampart. And they were battering the wall to throw it down.",
      "M": "Joab's forces came and laid siege to him at Abel Beth-maacah. They built a siege ramp against the city, and it stood against the outer wall. They were battering the wall to bring it down.",
      "T": "Joab's men came and besieged him at Abel Beth-maacah. They built a siege ramp against the city wall and were pounding it down."
    },
    "16": {
      "L": "Then a wise woman called from the city, 'Listen! Listen! Please say to Joab, \"Come near, so that I may speak to you.\"'",
      "M": "Then a wise woman in the city called out, 'Listen! Listen! Tell Joab to come near so I can speak to him.'",
      "T": "Then a wise woman called out from the city: 'Listen! Tell Joab to come closer—I want to speak to him.'"
    },
    "17": {
      "L": "And he came near to her, and the woman said, 'Are you Joab?' He answered, 'I am.' She said to him, 'Hear the words of your servant.' And he answered, 'I am listening.'",
      "M": "He came near her. The woman asked, 'Are you Joab?' He answered, 'I am.' She said, 'Hear the words of your servant.' He replied, 'I am listening.'",
      "T": "He came near. 'Are you Joab?' she said. 'I am,' he said. 'Then hear what your servant has to say.' 'I am listening,' said Joab."
    },
    "18": {
      "L": "Then she said, 'They used to say in former times, \"Let them seek guidance at Abel,\" and so they would settle a matter.'",
      "M": "She said, 'In the old days people used to say, \"Get your answer at Abel,\" and that is how they settled things.'",
      "T": "'In the old days,' she said, 'people used to say: go to Abel for an answer. And matters were settled. This city has always been a place of wise counsel.'"
    },
    "19": {
      "L": "'I am one of the peaceable and faithful in Israel. You seek to destroy a city that is a mother in Israel. Why will you swallow up the inheritance of the LORD?'",
      "M": "'I am one of the peaceable and faithful in Israel. You are trying to destroy a city that is like a mother in Israel. Why do you want to swallow up the LORD's inheritance?'",
      "T": "'I represent the peaceful and faithful of Israel. You are trying to destroy a city that is a mother-city in Israel. Why would you devour the LORD's own inheritance?'"
    },
    "20": {
      "L": "Joab answered, 'Far be it from me, far be it, that I should swallow up or destroy!'",
      "M": "Joab replied, 'Far be it from me, far be it indeed, that I should swallow up or destroy!'",
      "T": "'God forbid,' Joab answered. 'Swallow up or destroy? Never.'"
    },
    "21": {
      "L": "'That is not the case. But a man of the hill country of Ephraim, called Sheba the son of Bichri, has lifted up his hand against King David. Give up him alone, and I will withdraw from the city.' And the woman said to Joab, 'His head will be thrown to you over the wall.'",
      "M": "'That is not the case at all. But a man from the hill country of Ephraim, named Sheba son of Bichri, has raised his hand against King David. Hand him over—just him—and I will withdraw from the city.' The woman said to Joab, 'His head will be thrown to you over the wall.'",
      "T": "'Not at all. A man named Sheba son of Bichri, from the hill country of Ephraim, has lifted his hand against King David. Give him to us, and we will leave the city alone.' 'His head will come over the wall to you,' the woman said."
    },
    "22": {
      "L": "Then the woman went to all the people in her wisdom. And they cut off the head of Sheba the son of Bichri and threw it out to Joab. So he blew the trumpet, and they dispersed from the city, every man to his home. And Joab returned to Jerusalem to the king.",
      "M": "Then the woman in her wisdom went to all the people. They cut off the head of Sheba son of Bichri and threw it out to Joab. He blew the trumpet, and they dispersed from the city, each man going home. Joab returned to the king in Jerusalem.",
      "T": "The wise woman took her counsel to the people of the city. They cut off Sheba's head and threw it over the wall to Joab. He blew the horn, his men dispersed from the city—every man to his own home—and Joab returned to Jerusalem to the king."
    },
    "23": {
      "L": "Now Joab was over all the army of Israel; and Benaiah the son of Jehoiada was over the Cherethites and the Pelethites;",
      "M": "Joab was over all the army of Israel; Benaiah son of Jehoiada was over the Cherethites and the Pelethites;",
      "T": "Joab commanded all Israel's army. Benaiah son of Jehoiada commanded the Cherethites and Pelethites."
    },
    "24": {
      "L": "and Adoram was in charge of the forced labor; and Jehoshaphat the son of Ahilud was the recorder;",
      "M": "Adoram was in charge of forced labor; Jehoshaphat son of Ahilud was the royal recorder;",
      "T": "Adoram oversaw the forced labor. Jehoshaphat son of Ahilud was the court recorder."
    },
    "25": {
      "L": "and Sheva was the secretary; and Zadok and Abiathar were the priests;",
      "M": "Sheva was the secretary; Zadok and Abiathar were the priests;",
      "T": "Sheva was the royal secretary. Zadok and Abiathar were the priests."
    },
    "26": {
      "L": "and Ira the Jairite was also David's priest.",
      "M": "and Ira the Jairite was David's personal priest.",
      "T": "And Ira the Jairite was David's own priest."
    }
  },
  "21": {
    "1": {
      "L": "Now there was a famine in the days of David for three years, year after year. And David sought the face of the LORD. And the LORD said, 'There is bloodguilt on Saul and on his house, because he put the Gibeonites to death.'",
      "M": "During David's reign there was a famine for three years in succession. David sought the LORD's face, and the LORD said, 'There is bloodguilt on Saul and his house because he put the Gibeonites to death.'",
      "T": "In David's time there was a famine—three years in a row. David sought the LORD, and the LORD told him: 'Bloodguilt rests on Saul and his house, because he put the Gibeonites to death.'"
    },
    "2": {
      "L": "So the king called the Gibeonites and spoke to them. Now the Gibeonites were not of the people of Israel but of the remnant of the Amorites. Though the people of Israel had sworn to spare them, Saul had sought to strike them down in his zeal for the people of Israel and Judah.",
      "M": "The king summoned the Gibeonites and spoke to them. The Gibeonites were not Israelites but a remnant of the Amorites; the Israelites had sworn to spare them, yet Saul in his zeal for Israel and Judah had tried to wipe them out.",
      "T": "The king summoned the Gibeonites. They were not Israelites—they were a surviving remnant of the Amorites, a people Israel had sworn to protect. Yet Saul, in his zeal for Israel and Judah, had tried to destroy them."
    },
    "3": {
      "L": "David said to the Gibeonites, 'What shall I do for you? And how shall I make atonement, that you may bless the inheritance of the LORD?'",
      "M": "David said to the Gibeonites, 'What should I do for you? How shall I make atonement, so that you will bless the LORD's inheritance?'",
      "T": "David asked the Gibeonites, 'What can I do for you? How can atonement be made, so that you will bless the LORD's inheritance?'"
    },
    "4": {
      "L": "The Gibeonites said to him, 'It is not a matter of silver or gold between us and Saul or his house; neither is it for us to put any man to death in Israel.' And he said, 'What do you say that I shall do for you?'",
      "M": "The Gibeonites answered him, 'It is not a question of silver or gold between us and Saul or his house, and it is not ours to put any man to death in Israel.' He said, 'Whatever you say, I will do for you.'",
      "T": "The Gibeonites said, 'This is not a matter of silver and gold between us and Saul. And it is not for us to put anyone in Israel to death.' David said, 'Whatever you ask, I will do.'"
    },
    "5": {
      "L": "They said to the king, 'The man who consumed us and who planned to destroy us, so that we should have no place in all the territory of Israel—",
      "M": "They said to the king, 'The man who destroyed us and planned to annihilate us so that we would have no place in all Israel's territory—",
      "T": "'The man who devoured us,' they said, 'the man who planned to exterminate us so that we would have no place left in all of Israel—'"
    },
    "6": {
      "L": "'let seven of his sons be given to us, so that we may hang them before the LORD at Gibeah of Saul, the chosen of the LORD.' And the king said, 'I will give them.'",
      "M": "'let seven of his male descendants be handed over to us, so we may hang them before the LORD at Gibeah of Saul, the LORD's chosen.' The king said, 'I will hand them over.'",
      "T": "'—give us seven of his male descendants so we can execute them before the LORD at Gibeah of Saul, the one the LORD chose.' The king said, 'I will give them.'"
    },
    "7": {
      "L": "But the king spared Mephibosheth, the son of Saul's son Jonathan, because of the oath of the LORD that was between them, between David and Jonathan the son of Saul.",
      "M": "But the king spared Mephibosheth son of Jonathan son of Saul, because of the oath sworn before the LORD between David and Jonathan son of Saul.",
      "T": "The king spared Mephibosheth, Jonathan's son—Saul's grandson—because of the oath sworn before the LORD between David and Jonathan."
    },
    "8": {
      "L": "The king took the two sons of Rizpah the daughter of Aiah, whom she bore to Saul, Armoni and Mephibosheth, and the five sons of Merab the daughter of Saul, whom she bore to Adriel the son of Barzillai the Meholathite.",
      "M": "The king took Armoni and Mephibosheth, the two sons of Rizpah daughter of Aiah, whom she had borne to Saul, and the five sons of Merab daughter of Saul, whom she had borne to Adriel son of Barzillai the Meholathite.",
      "T": "The king took Armoni and Mephibosheth—the two sons Rizpah daughter of Aiah had borne to Saul—along with five sons of Merab daughter of Saul, born to Adriel son of Barzillai the Meholathite."
    },
    "9": {
      "L": "He gave them into the hands of the Gibeonites, and they hanged them on the mountain before the LORD. The seven of them fell together. They were put to death in the first days of harvest, at the beginning of barley harvest.",
      "M": "He handed them over to the Gibeonites, who hanged them on the mountain before the LORD. All seven fell together. They were put to death in the first days of harvest, at the beginning of the barley harvest.",
      "T": "He handed them to the Gibeonites, who executed them on the mountain before the LORD. All seven fell together, at the start of the barley harvest—the very first days of harvest time."
    },
    "10": {
      "L": "Then Rizpah the daughter of Aiah took sackcloth and spread it for herself on the rock, from the beginning of harvest until water fell upon them from the heavens. And she did not allow the birds of the air to come upon them by day, or the beasts of the field by night.",
      "M": "Then Rizpah daughter of Aiah took sackcloth and spread it on a rock for herself. She kept watch from the beginning of harvest until rain fell on them from the sky, keeping the birds away by day and the wild animals away by night.",
      "T": "Rizpah daughter of Aiah took sackcloth and spread it on the rock. From the beginning of harvest until the rains came from heaven, she kept her watch—driving the birds away by day and the wild animals away by night."
    },
    "11": {
      "L": "And David was told what Rizpah the daughter of Aiah, the concubine of Saul, had done.",
      "M": "David was told what Rizpah daughter of Aiah, Saul's concubine, had done.",
      "T": "Word reached David of what Rizpah daughter of Aiah had done."
    },
    "12": {
      "L": "And David went and took the bones of Saul and the bones of his son Jonathan from the men of Jabesh-gilead, who had stolen them from the public square of Beth-shan, where the Philistines had hanged them, on the day the Philistines killed Saul on Gilboa.",
      "M": "David went and retrieved the bones of Saul and his son Jonathan from the men of Jabesh-gilead, who had secretly taken them from the public square of Beth-shan, where the Philistines had hung them on the day they killed Saul at Gilboa.",
      "T": "David went and recovered the bones of Saul and his son Jonathan from the men of Jabesh-gilead—men who had taken them secretly from the open square at Beth-shan, where the Philistines had hung them on the day they killed Saul at Gilboa."
    },
    "13": {
      "L": "And he brought up from there the bones of Saul and the bones of his son Jonathan; and they gathered the bones of those who had been hanged.",
      "M": "He brought up from there the bones of Saul and Jonathan, and they also gathered the bones of those who had been hanged.",
      "T": "He brought back the bones of Saul and Jonathan, and they gathered the bones of the seven who had been hanged."
    },
    "14": {
      "L": "And they buried the bones of Saul and his son Jonathan in Zela, in the land of Benjamin, in the tomb of Kish his father. And they did all that the king commanded. And after that God responded to the plea for the land.",
      "M": "They buried the bones of Saul and his son Jonathan in Zela of Benjamin, in the tomb of his father Kish. They carried out everything the king commanded. After that, God answered prayer on behalf of the land.",
      "T": "They buried the bones of Saul and Jonathan in Zela of Benjamin, in the tomb of Kish his father. They did everything the king commanded. And after that, God heard the plea for the land—the plague was lifted."
    },
    "15": {
      "L": "There was war again between the Philistines and Israel, and David went down together with his servants. They fought against the Philistines. And David grew weary.",
      "M": "There was war again between the Philistines and Israel. David and his men went down and fought the Philistines. David became exhausted.",
      "T": "War broke out again between the Philistines and Israel. David went down with his men to fight, and David grew exhausted in the battle."
    },
    "16": {
      "L": "And Ishbi-benob, one of the descendants of the giants, whose spear weighed three hundred shekels of bronze, and who was armed with a new sword, thought to kill David.",
      "M": "Ishbi-benob, one of the descendants of the giants, whose bronze spearhead weighed three hundred shekels and who carried a new sword, intended to kill David.",
      "T": "Ishbi-benob—one of the Rephaite giants, carrying a spear with a bronze head weighing three hundred shekels and armed with a new sword—was about to kill David."
    },
    "17": {
      "L": "But Abishai the son of Zeruiah came to his aid and attacked the Philistine and killed him. Then David's men swore to him, 'You shall not go out with us to battle any longer, lest you quench the lamp of Israel.'",
      "M": "But Abishai son of Zeruiah came to his aid, struck the Philistine, and killed him. Then David's men swore to him, 'You must not go out with us to battle again, or you will put out the lamp of Israel.'",
      "T": "Abishai son of Zeruiah came to his rescue, struck the Philistine down and killed him. Then David's men swore an oath to him: 'You will not go out to battle with us again. You must not extinguish the lamp of Israel.'"
    },
    "18": {
      "L": "After this there was again a battle with the Philistines at Gob. Then Sibbecai the Hushathite struck down Saph, who was one of the descendants of the giants.",
      "M": "After this there was another battle with the Philistines at Gob. At that time Sibbecai the Hushathite struck down Saph, who was one of the descendants of the giants.",
      "T": "After this another battle was fought against the Philistines at Gob. Sibbecai the Hushathite struck down Saph—one of the Rephaite giants."
    },
    "19": {
      "L": "And there was again a battle with the Philistines at Gob, and Elhanan the son of Jaare-oregim, the Bethlehemite, struck down Goliath the Gittite, the shaft of whose spear was like a weaver's beam.",
      "M": "There was another battle with the Philistines at Gob, and Elhanan son of Jaare-oregim the Bethlehemite struck down Goliath the Gittite, whose spear shaft was like a weaver's beam.",
      "T": "Another battle at Gob with the Philistines: Elhanan son of Jaare-oregim the Bethlehemite struck down Goliath of Gath, whose spear shaft was like a weaver's beam."
    },
    "20": {
      "L": "And there was again war at Gath, where there was a man of great stature, who had six fingers on each hand and six toes on each foot, twenty-four in number, and he also was descended from the giants.",
      "M": "There was another battle at Gath, where there was a man of great size who had six fingers on each hand and six toes on each foot—twenty-four in all. He too was descended from the giants.",
      "T": "Another battle at Gath—and there was a man of extraordinary size: six fingers on each hand, six toes on each foot—twenty-four in all. He too was of Rephaite descent."
    },
    "21": {
      "L": "And when he defied Israel, Jonathan the son of Shimei, David's brother, struck him down.",
      "M": "When he taunted Israel, Jonathan son of Shimei, David's brother, struck him down.",
      "T": "He taunted Israel, and Jonathan son of Shimei, David's own brother, struck him down."
    },
    "22": {
      "L": "These four were descended from the giants in Gath, and they fell by the hand of David and by the hand of his servants.",
      "M": "These four were descendants of the giants in Gath, and they fell by the hand of David and his servants.",
      "T": "These four were descendants of the Rephaite giants of Gath. They all fell at the hands of David and his men."
    }
  },
  "22": {
    "1": {
      "L": "And David spoke to the LORD the words of this song on the day when the LORD delivered him from the hand of all his enemies, and from the hand of Saul.",
      "M": "David spoke to the LORD the words of this song on the day the LORD delivered him from the hand of all his enemies and from the hand of Saul.",
      "T": "David sang this song to the LORD on the day the LORD rescued him from the grip of all his enemies and from the hand of Saul."
    },
    "2": {
      "L": "He said: 'The LORD is my rock, and my fortress, and my deliverer,",
      "M": "He said: 'The LORD is my rock, my fortress, and my deliverer;",
      "T": "He said:\nThe LORD is my rock,\nmy fortress, my deliverer—"
    },
    "3": {
      "L": "'The God of my rock; in him I trust. He is my shield, and the horn of my salvation, my high tower, and my refuge, my savior; you save me from violence.",
      "M": "'The God of my rock—in him I take refuge. He is my shield, the horn of my salvation, my stronghold, my refuge, my savior who saves me from violence.",
      "T": "the God who is my Rock—in him I hide.\nMy shield, the horn of my salvation,\nmy fortress, my refuge,\nmy savior who rescues me from violence."
    },
    "4": {
      "L": "'I call upon the LORD, who is worthy to be praised, and I am saved from my enemies.",
      "M": "'I call on the LORD, who is worthy of praise, and I am saved from my enemies.",
      "T": "I call to the LORD—he is worthy of all praise—\nand I am saved from my enemies."
    },
    "5": {
      "L": "'For the waves of death encompassed me; the torrents of destruction assailed me;",
      "M": "'The waves of death engulfed me; the torrents of destruction terrified me;",
      "T": "The waves of death closed over me,\nthe torrents of chaos swept at me;"
    },
    "6": {
      "L": "'the cords of Sheol entangled me; the snares of death confronted me.",
      "M": "'the cords of Sheol wrapped around me; the snares of death set themselves before me.",
      "T": "the cords of Sheol tightened around me,\nthe snares of death were laid before me."
    },
    "7": {
      "L": "'In my distress I called upon the LORD; to my God I called. From his temple he heard my voice, and my cry came to his ears.",
      "M": "'In my distress I called to the LORD; I called to my God. From his temple he heard my voice, and my cry reached his ears.",
      "T": "In my distress I cried to the LORD,\nI called out to my God—\nand from his temple he heard my voice;\nmy cry reached his very ears."
    },
    "8": {
      "L": "'Then the earth reeled and rocked; the foundations of the heavens trembled and quaked, because he was angry.",
      "M": "'Then the earth reeled and shook; the foundations of the heavens trembled and quaked, because he was angry.",
      "T": "Then the earth shook and trembled;\nthe foundations of heaven quaked and reeled—\nbecause he was angry."
    },
    "9": {
      "L": "'Smoke went up from his nostrils, and devouring fire from his mouth; glowing coals flamed from him.",
      "M": "'Smoke went up from his nostrils, devouring fire from his mouth; blazing coals were kindled by it.",
      "T": "Smoke poured from his nostrils,\ndevouring fire from his mouth—\nglowing coals blazing before him."
    },
    "10": {
      "L": "'He bowed the heavens and came down; thick darkness was under his feet.",
      "M": "'He parted the heavens and came down; dark storm clouds were under his feet.",
      "T": "He split the heavens and came down;\nthick darkness was beneath his feet."
    },
    "11": {
      "L": "'He rode on a cherub and flew; he was seen on the wings of the wind.",
      "M": "'He rode on a cherub and flew; he appeared on the wings of the wind.",
      "T": "He rode upon a cherub and flew;\nhe swept in on the wings of the wind."
    },
    "12": {
      "L": "'He made darkness around him his canopy, a mass of waters, thick clouds of the sky.",
      "M": "'He made darkness his canopy around him—a gathering of waters, thick storm clouds.",
      "T": "He wrapped himself in darkness,\nhis canopy of massed cloud and storm water,\nthick clouds of the sky."
    },
    "13": {
      "L": "'Out of the brightness before him coals of fire flamed.",
      "M": "'Out of the brightness before him, coals of fire blazed forth.",
      "T": "Out of the brightness before him\ncoals of fire burst into flame."
    },
    "14": {
      "L": "'The LORD thundered from heaven, and the Most High uttered his voice.",
      "M": "'The LORD thundered from heaven; the Most High raised his voice.",
      "T": "The LORD thundered from heaven;\nthe Most High spoke in thunder."
    },
    "15": {
      "L": "'And he sent out arrows and scattered them; lightning, and routed them.",
      "M": "'He shot his arrows and scattered them; lightning bolts and threw them into disorder.",
      "T": "He shot his arrows—they scattered.\nLightning bolts—and they were routed."
    },
    "16": {
      "L": "'Then the channels of the sea were seen; the foundations of the world were laid bare, at the rebuke of the LORD, at the blast of the breath of his nostrils.",
      "M": "'Then the channels of the sea were exposed and the foundations of the world laid bare, at the LORD's rebuke, at the blast of the breath of his nostrils.",
      "T": "The depths of the sea were exposed;\nthe foundations of the world laid bare—\nat the LORD's rebuke,\nat the blast of his breath from his nostrils."
    },
    "17": {
      "L": "'He sent from on high; he took me; he drew me out of many waters.",
      "M": "'He reached down from on high and took me; he drew me out of many waters.",
      "T": "He reached down from on high and took me;\nhe pulled me out of deep waters."
    },
    "18": {
      "L": "'He rescued me from my strong enemy, from those who hated me, for they were too mighty for me.",
      "M": "'He rescued me from my powerful enemy, from those who hated me—for they were stronger than I.",
      "T": "He rescued me from my powerful enemy,\nfrom those who hated me—\nthey were too strong for me."
    },
    "19": {
      "L": "'They came against me in the day of my calamity, but the LORD was my support.",
      "M": "'They confronted me in the day of my disaster, but the LORD was my support.",
      "T": "They came at me in my hour of collapse—\nbut the LORD was my support."
    },
    "20": {
      "L": "'He brought me out into a broad place; he rescued me, because he delighted in me.",
      "M": "'He brought me out into a spacious place; he rescued me, because he delighted in me.",
      "T": "He brought me out to a wide, open place;\nhe saved me—because he delighted in me."
    },
    "21": {
      "L": "'The LORD dealt with me according to my righteousness; according to the cleanness of my hands he rewarded me.",
      "M": "'The LORD rewarded me according to my righteousness; according to the cleanness of my hands he repaid me.",
      "T": "The LORD dealt with me as my faithfulness deserved;\nhe repaid me as my clean hands required."
    },
    "22": {
      "L": "'For I have kept the ways of the LORD and have not wickedly departed from my God.",
      "M": "'For I have kept the ways of the LORD and have not turned wickedly from my God.",
      "T": "For I have kept the LORD's ways\nand not turned treacherously from my God."
    },
    "23": {
      "L": "'For all his rules were before me, and from his statutes I did not turn aside.",
      "M": "'For all his ordinances were before me, and I did not turn away from his statutes.",
      "T": "All his ordinances were before me;\nI did not put his statutes aside."
    },
    "24": {
      "L": "'I was blameless before him, and I kept myself from my guilt.",
      "M": "'I was blameless before him and kept myself from wrongdoing.",
      "T": "I was blameless before him\nand kept myself from deliberate sin."
    },
    "25": {
      "L": "'And the LORD has recompensed me according to my righteousness, according to my cleanness in his sight.",
      "M": "'So the LORD has repaid me according to my righteousness, according to my cleanness in his sight.",
      "T": "So the LORD repaid me as my faithfulness deserved—\nmy cleanness of hands before his eyes."
    },
    "26": {
      "L": "'With the merciful you show yourself merciful; with the blameless man you show yourself blameless;",
      "M": "'To the faithful you show yourself faithful; to the blameless you show yourself blameless;",
      "T": "To the faithful you show yourself faithful;\nto the blameless you show yourself blameless;"
    },
    "27": {
      "L": "'with the pure you show yourself pure, and with the crooked you make yourself seem tortuous.",
      "M": "'to the pure you show yourself pure, but with the devious you show yourself shrewd.",
      "T": "to the pure you show yourself pure—\nbut with the twisted you show yourself a match for their twisting."
    },
    "28": {
      "L": "'You save a humble people, but your eyes are on the haughty to bring them down.",
      "M": "'You deliver a humble people, but your eyes are on the proud to bring them low.",
      "T": "You save the lowly;\nbut your eyes are on the proud—to bring them down."
    },
    "29": {
      "L": "'For you are my lamp, O LORD, and the LORD lightens my darkness.",
      "M": "'For you are my lamp, O LORD, and the LORD lights up my darkness.",
      "T": "For you are my lamp, O LORD;\nthe LORD turns my darkness to light."
    },
    "30": {
      "L": "'For by you I can run against a troop, and by my God I can leap over a wall.",
      "M": "'By your help I can charge a troop; by my God I can leap over a wall.",
      "T": "With your help I can charge a troop;\nwith my God I can leap over a wall."
    },
    "31": {
      "L": "'This God—his way is perfect; the word of the LORD proves true; he is a shield for all those who take refuge in him.",
      "M": "'As for God, his way is perfect; the word of the LORD is flawless. He is a shield for all who take refuge in him.",
      "T": "This God—his way is perfect.\nThe word of the LORD is proved true;\nhe is a shield to all who shelter in him."
    },
    "32": {
      "L": "'For who is God but the LORD? And who is a rock except our God?",
      "M": "'For who is God except the LORD? And who is a rock besides our God?",
      "T": "Who is God but the LORD?\nWho is the Rock except our God?"
    },
    "33": {
      "L": "'This God is my strong refuge and has made my way blameless.",
      "M": "'God is my strong refuge and has made my way blameless.",
      "T": "This God is my strong refuge;\nhe makes my way sure."
    },
    "34": {
      "L": "'He made my feet like the feet of a deer and set me secure on the heights.",
      "M": "'He made my feet like the feet of a deer and set me secure on the heights.",
      "T": "He gives me feet like a deer's\nand sets me secure on the mountain heights."
    },
    "35": {
      "L": "'He trains my hands for war so that my arms can bend a bow of bronze.",
      "M": "'He trains my hands for battle so that my arms can draw a bow of bronze.",
      "T": "He trains my hands for battle;\nmy arms bend a bow of bronze."
    },
    "36": {
      "L": "'You have given me the shield of your salvation, and your gentleness made me great.",
      "M": "'You have given me the shield of your salvation, and your condescension has made me great.",
      "T": "You give me the shield of your salvation;\nyour stooping-down to me has made me great."
    },
    "37": {
      "L": "'You gave a wide place for my steps under me, and my feet did not slip.",
      "M": "'You gave a wide path for my feet so that my ankles did not give way.",
      "T": "You widen the path beneath my feet;\nmy feet do not slip."
    },
    "38": {
      "L": "'I pursued my enemies and destroyed them, and did not turn back until they were consumed.",
      "M": "'I pursued my enemies and destroyed them; I did not turn back until I had consumed them.",
      "T": "I pursued my enemies and destroyed them;\nI did not turn back until they were finished."
    },
    "39": {
      "L": "'I consumed them; I thrust them through, so that they did not rise; they fell under my feet.",
      "M": "'I consumed them; I struck them through so that they could not rise; they fell beneath my feet.",
      "T": "I crushed them; they fell—\nstruck through, unable to rise,\nbroken beneath my feet."
    },
    "40": {
      "L": "'For you equipped me with strength for the battle; you made those who rise against me sink under me.",
      "M": "'For you armed me with strength for battle; you made those who rose against me bow down under me.",
      "T": "You armed me with strength for the battle;\nyou brought down under me those who rose against me."
    },
    "41": {
      "L": "'You made my enemies turn their backs to me, those who hated me, and I destroyed them.",
      "M": "'You made my enemies turn and flee; I destroyed those who hated me.",
      "T": "You made my enemies turn their backs to me;\nthose who hated me—I annihilated them."
    },
    "42": {
      "L": "'They looked, but there was none to save; they cried to the LORD, but he did not answer them.",
      "M": "'They looked for help, but there was no one to save; they cried to the LORD, but he did not answer them.",
      "T": "They looked for help—no one was there.\nThey cried to the LORD—he did not answer them."
    },
    "43": {
      "L": "'I beat them fine as the dust of the earth; I crushed them and stamped them down like the mire of the streets.",
      "M": "'I ground them fine as dust before the wind; I crushed and stamped them down like the mire in the streets.",
      "T": "I ground them fine as the dust of the earth;\ncrushed them, stamped them down\nlike mud in the streets."
    },
    "44": {
      "L": "'You delivered me from strife with my people; you kept me as the head of nations; people whom I had not known served me.",
      "M": "'You delivered me from the quarrels of my people; you kept me as the head of nations; a people I had not known served me.",
      "T": "You saved me from the strife of my own people;\nyou made me the head of nations.\nPeoples I never knew came to serve me."
    },
    "45": {
      "L": "'Foreigners came cringing to me; as soon as they heard of me, they submitted to me.",
      "M": "'Foreigners came cringing to me; as soon as they heard of me they obeyed me.",
      "T": "Foreigners came cowering to me;\nthe moment they heard of me, they submitted."
    },
    "46": {
      "L": "'Foreigners lost heart and came trembling out of their fortresses.",
      "M": "'Foreigners lost heart and came trembling from their strongholds.",
      "T": "Foreigners lost their courage\nand came staggering from their strongholds."
    },
    "47": {
      "L": "'The LORD lives, and blessed be my rock, and exalted be my God, the rock of my salvation,",
      "M": "'The LORD lives! Blessed be my Rock! Exalted be my God, the Rock of my salvation,",
      "T": "The LORD lives!\nBlessed be my Rock!\nExalted be the God of my salvation—"
    },
    "48": {
      "L": "'the God who gave me vengeance and brought down peoples under me,",
      "M": "'the God who gives me vengeance and brings down peoples under me,",
      "T": "the God who gives me justice,\nwho brings peoples down under me,"
    },
    "49": {
      "L": "'who brought me out from my enemies; you exalted me above those who rose against me; you rescued me from the man of violence.",
      "M": "'who brought me out from my enemies. You exalted me above those who rose against me; you rescued me from the violent man.",
      "T": "who brought me out from my enemies.\nYou raised me above those who rose against me;\nyou rescued me from the violent man."
    },
    "50": {
      "L": "'Therefore I will give thanks to you, O LORD, among the nations, and I will sing praises to your name.",
      "M": "'Therefore I will praise you, O LORD, among the nations, and sing praises to your name.",
      "T": "Therefore I will praise you, LORD, among the nations;\nI will sing to your name."
    },
    "51": {
      "L": "'Great salvation he brings to his king, and shows steadfast love to his anointed, to David and his offspring forever.'",
      "M": "'He gives great victories to his king and shows steadfast love to his anointed—to David and his descendants forever.'",
      "T": "Great victories he gives to his king;\nhe shows covenant faithfulness to his anointed—\nto David and his seed, forever."
    }
  },
  "23": {
    "1": {
      "L": "Now these are the last words of David: The declaration of David the son of Jesse, the declaration of the man raised up on high, the anointed of the God of Jacob, the sweet singer of Israel:",
      "M": "These are the last words of David: The declaration of David son of Jesse, the declaration of the man God raised to prominence, the anointed of the God of Jacob, the beloved singer of Israel's psalms:",
      "T": "These are the last words of David—\nthe declaration of David son of Jesse,\nthe declaration of the man raised to the heights,\nthe anointed one of the God of Jacob,\nIsrael's beloved singer of songs:"
    },
    "2": {
      "L": "'The Spirit of the LORD speaks through me; his word is on my tongue.",
      "M": "'The Spirit of the LORD speaks through me; his word is on my tongue.",
      "T": "The Spirit of the LORD speaks through me;\nhis word is on my tongue."
    },
    "3": {
      "L": "'The God of Israel has spoken; the Rock of Israel has said to me: When one rules over men righteously, when he rules in the fear of God,",
      "M": "'The God of Israel has spoken; the Rock of Israel has said to me: Whoever rules over men with justice, who rules in the fear of God,",
      "T": "The God of Israel has spoken;\nthe Rock of Israel said to me:\nthe one who rules over people with justice,\nwho rules in the fear of God—"
    },
    "4": {
      "L": "'he is like the light of morning when the sun rises, a morning without clouds, like the bright gleam after rain that brings grass from the earth.",
      "M": "'he is like the light of morning, like sunrise on a cloudless day, like the gleam of rain on green grass after showers.",
      "T": "—is like the light of morning,\nlike sunrise on a cloudless day,\nlike the bright gleaming after rain\nwhen grass springs from the earth."
    },
    "5": {
      "L": "'For is not my house so with God? For he has made with me an everlasting covenant, ordered in all things and secure. For will he not cause to prosper all my salvation and my desire?",
      "M": "'Is it not true that my house stands so before God? For he has made with me an everlasting covenant, ordered and secured in every way. Will he not indeed bring about all my salvation and all my desire?",
      "T": "Is my house not so with God?\nHe has made with me an everlasting covenant—\nordered in all things and sure.\nFor this is all my salvation and all my desire:\nwill he not make it flourish?"
    },
    "6": {
      "L": "'But worthless men are all like thorns that are thrown away, for they cannot be taken with the hand;",
      "M": "'But worthless men are like thorns that are cast away, for they cannot be taken up with the hand;",
      "T": "But men of Belial are like thorns thrown aside—\nthey cannot be grasped with the bare hand;"
    },
    "7": {
      "L": "'whoever touches them arms himself with iron and the shaft of a spear, and they are utterly consumed with fire in their place.'",
      "M": "'whoever touches them must be armed with iron and the shaft of a spear, and they are utterly burned up where they stand.'",
      "T": "whoever handles them takes iron in hand,\na spear-shaft—\nand in their place they are burned to nothing."
    },
    "8": {
      "L": "These are the names of the mighty men whom David had: Josheb-basshebeth a Tahchemonite was chief of the three. He wielded his spear against eight hundred whom he killed at one time.",
      "M": "These are the names of David's mighty men: Josheb-basshebeth the Tahchemonite, chief of the Three. He raised his spear against eight hundred men and killed them in a single battle.",
      "T": "These are the names of David's mighty warriors: Josheb-basshebeth the Tahchemonite, head of the Three. He faced eight hundred men with his spear and killed them all in one engagement."
    },
    "9": {
      "L": "And next to him among the three mighty men was Eleazar the son of Dodo, son of Ahohi. He was with David when they defied the Philistines who were gathered there for battle, and the men of Israel withdrew.",
      "M": "Next to him among the three warriors was Eleazar son of Dodo son of Ahohi. He was with David when they taunted the Philistines gathered for battle at Pas-dammim. When the men of Israel retreated,",
      "T": "Next among the three was Eleazar son of Dodo son of Ahohi. He was with David when they challenged the Philistines at Pas-dammim—where Israel had assembled for battle and the men of Israel began to fall back."
    },
    "10": {
      "L": "He rose and struck down Philistines until his hand was weary and his hand clung to the sword. And the LORD brought about a great victory that day, and the men returned after him only to strip the slain.",
      "M": "he held his ground and struck down Philistines until his hand grew tired and his hand froze to the sword. The LORD brought about a great victory that day. The men returned after him only to strip the slain.",
      "T": "Eleazar stood his ground and struck down the Philistines until his hand was exhausted and had to be pried from the sword. The LORD won a great victory that day. The men came back—but only to plunder the dead."
    },
    "11": {
      "L": "And next to him was Shammah, the son of Agee the Hararite. The Philistines gathered together at Lehi, where there was a plot of ground full of lentils, and the men fled from the Philistines.",
      "M": "Next was Shammah son of Agee the Hararite. The Philistines had gathered at Lehi, where there was a field full of lentils. The men of Israel fled from the Philistines,",
      "T": "Next was Shammah son of Agee the Hararite. The Philistines had gathered at Lehi, where there was a field full of lentils. The men of Israel ran."
    },
    "12": {
      "L": "But he took his stand in the midst of the plot and defended it and struck down the Philistines, and the LORD worked a great victory.",
      "M": "but he planted himself in the middle of the field, defended it, and struck down the Philistines. The LORD brought about a great victory.",
      "T": "But Shammah stood in the middle of that field and defended it and killed the Philistines. The LORD won a great victory."
    },
    "13": {
      "L": "And three of the thirty chief men went down and came about harvest time to David at the cave of Adullam, when a band of Philistines was encamped in the Valley of Rephaim.",
      "M": "Three of the thirty chief warriors went down at harvest time and came to David at the cave of Adullam, while a Philistine raiding band was encamped in the Valley of Rephaim.",
      "T": "Three of the thirty chiefs went down at harvest time to David at the cave of Adullam, while a Philistine force was camped in the Valley of Rephaim."
    },
    "14": {
      "L": "David was then in the stronghold, and the garrison of the Philistines was then at Bethlehem.",
      "M": "David was in the stronghold at the time, and the Philistine garrison was at Bethlehem.",
      "T": "David was in the stronghold; the Philistines held Bethlehem."
    },
    "15": {
      "L": "And David said longingly, 'O that someone would give me water to drink from the well of Bethlehem that is by the gate!'",
      "M": "David was overcome with longing and said, 'O that someone would bring me water to drink from the well at Bethlehem's gate!'",
      "T": "David was seized by longing and said, 'If only someone would give me water to drink from the well at the gate of Bethlehem!'"
    },
    "16": {
      "L": "Then the three mighty men broke through the camp of the Philistines and drew water out of the well of Bethlehem that was by the gate and carried and brought it to David. But he would not drink of it. He poured it out to the LORD",
      "M": "Then the three warriors broke through the Philistine lines, drew water from the well at Bethlehem's gate, and carried it back to David. But he refused to drink it. He poured it out to the LORD",
      "T": "The three broke through the Philistine lines, drew water from the well at Bethlehem's gate, and brought it to David. But he would not drink it. He poured it out before the LORD—"
    },
    "17": {
      "L": "and said, 'Far be it from me, O LORD, that I should do this. Shall I drink the blood of the men who went at the risk of their lives?' Therefore he would not drink it. These things the three mighty men did.",
      "M": "and said, 'Far be it from me, O LORD, to do this! Is this not the blood of the men who went at the risk of their own lives?' So he would not drink it. These were the things the three warriors did.",
      "T": "'The LORD forbid that I drink this,' he said. 'Is this not the blood of men who put their lives in danger to bring it?' He would not drink it. This is what the three did."
    },
    "18": {
      "L": "Now Abishai, the brother of Joab, the son of Zeruiah, was chief of the thirty. And he wielded his spear against three hundred men and killed them and won a name beside the three.",
      "M": "Abishai, the brother of Joab son of Zeruiah, was head of the Thirty. He raised his spear against three hundred men, killed them, and earned a name alongside the Three.",
      "T": "Abishai, Joab's brother, was head of the Thirty. He faced three hundred men with his spear and killed them all. He won fame alongside the Three—"
    },
    "19": {
      "L": "He was the most renowned of the thirty and became their commander, but he did not attain to the three.",
      "M": "He was the most honored of the Thirty and became their commander, but he did not attain to the Three.",
      "T": "—the most honored of the Thirty and their captain. But he was not counted among the Three."
    },
    "20": {
      "L": "And Benaiah the son of Jehoiada was a valiant man of Kabzeel, a doer of great deeds. He struck down two heroes of Moab. He also went down and struck down a lion in a pit on a day when snow had fallen.",
      "M": "Benaiah son of Jehoiada was a valiant warrior from Kabzeel, a man of great deeds. He struck down two warriors of Moab. He also went down and killed a lion in a pit on a day when snow had fallen.",
      "T": "Benaiah son of Jehoiada was a courageous man from Kabzeel, a man of great exploits. He struck down two of Moab's champions. He went down into a pit on a snowy day and killed a lion."
    },
    "21": {
      "L": "And he struck down an Egyptian, a handsome man. The Egyptian had a spear in his hand, but Benaiah went down to him with a staff and snatched the spear out of the Egyptian's hand and killed him with his own spear.",
      "M": "He also struck down a formidable Egyptian. The Egyptian had a spear in his hand, but Benaiah went against him with a club, snatched the spear from his hand, and killed him with his own spear.",
      "T": "He also killed an imposing Egyptian—the man had a spear; Benaiah went at him with a staff, wrenched the spear away from him, and killed him with his own weapon."
    },
    "22": {
      "L": "These things did Benaiah the son of Jehoiada, and won a name beside the three mighty men.",
      "M": "These were the things Benaiah son of Jehoiada did, and he won a name alongside the three warriors.",
      "T": "These were the deeds of Benaiah son of Jehoiada. He won a name alongside the Three."
    },
    "23": {
      "L": "He was renowned among the thirty, but he did not attain to the three. And David set him over his bodyguard.",
      "M": "He was more honored than the Thirty, but he did not attain to the Three. David placed him in charge of his bodyguard.",
      "T": "He was more honored than the Thirty, but not among the Three. David appointed him over his personal bodyguard."
    },
    "24": {
      "L": "Asahel the brother of Joab was one of the thirty; Elhanan the son of Dodo of Bethlehem,",
      "M": "Asahel the brother of Joab was one of the Thirty; Elhanan son of Dodo of Bethlehem,",
      "T": "Asahel, Joab's brother, was among the Thirty. Elhanan son of Dodo of Bethlehem,"
    },
    "25": {
      "L": "Shammah of Harod, Elika of Harod,",
      "M": "Shammah of Harod, Elika of Harod,",
      "T": "Shammah of Harod, Elika of Harod,"
    },
    "26": {
      "L": "Helez the Paltite, Ira the son of Ikkesh of Tekoa,",
      "M": "Helez the Paltite, Ira son of Ikkesh of Tekoa,",
      "T": "Helez the Paltite, Ira son of Ikkesh of Tekoa,"
    },
    "27": {
      "L": "Abiezer of Anathoth, Mebunnai the Hushathite,",
      "M": "Abiezer of Anathoth, Mebunnai the Hushathite,",
      "T": "Abiezer of Anathoth, Mebunnai the Hushathite,"
    },
    "28": {
      "L": "Zalmon the Ahohite, Maharai of Netophah,",
      "M": "Zalmon the Ahohite, Maharai of Netophah,",
      "T": "Zalmon the Ahohite, Maharai of Netophah,"
    },
    "29": {
      "L": "Heleb the son of Baanah of Netophah, Ittai the son of Ribai of Gibeah of the people of Benjamin,",
      "M": "Heleb son of Baanah of Netophah, Ittai son of Ribai of Gibeah of Benjamin,",
      "T": "Heleb son of Baanah of Netophah, Ittai son of Ribai of Gibeah of Benjamin,"
    },
    "30": {
      "L": "Benaiah of Pirathon, Hiddai of the brooks of Gaash,",
      "M": "Benaiah of Pirathon, Hiddai of the wadis of Gaash,",
      "T": "Benaiah of Pirathon, Hiddai of the wadis of Gaash,"
    },
    "31": {
      "L": "Abi-albon the Arbathite, Azmaveth of Bahurim,",
      "M": "Abi-albon the Arbathite, Azmaveth of Bahurim,",
      "T": "Abi-albon the Arbathite, Azmaveth of Bahurim,"
    },
    "32": {
      "L": "Eliahba the Shaalbonite, the sons of Jashen, Jonathan,",
      "M": "Eliahba the Shaalbonite, the sons of Jashen, Jonathan,",
      "T": "Eliahba the Shaalbonite, the sons of Jashen, Jonathan,"
    },
    "33": {
      "L": "Shammah the Hararite, Ahiam the son of Sharar the Hararite,",
      "M": "Shammah the Hararite, Ahiam son of Sharar the Hararite,",
      "T": "Shammah the Hararite, Ahiam son of Sharar the Hararite,"
    },
    "34": {
      "L": "Eliphelet the son of Ahasbai of Maacah, Eliam the son of Ahithophel the Gilonite,",
      "M": "Eliphelet son of Ahasbai of Maacah, Eliam son of Ahithophel the Gilonite,",
      "T": "Eliphelet son of Ahasbai of Maacah, Eliam son of Ahithophel the Gilonite,"
    },
    "35": {
      "L": "Hezro of Carmel, Paarai the Arbite,",
      "M": "Hezro of Carmel, Paarai the Arbite,",
      "T": "Hezro of Carmel, Paarai the Arbite,"
    },
    "36": {
      "L": "Igal the son of Nathan of Zobah, Bani the Gadite,",
      "M": "Igal son of Nathan of Zobah, Bani the Gadite,",
      "T": "Igal son of Nathan of Zobah, Bani the Gadite,"
    },
    "37": {
      "L": "Zelek the Ammonite, Naharai of Beeroth, the armor-bearer of Joab the son of Zeruiah,",
      "M": "Zelek the Ammonite, Naharai of Beeroth—the armor-bearer of Joab son of Zeruiah—",
      "T": "Zelek the Ammonite, Naharai of Beeroth—Joab son of Zeruiah's armor-bearer—"
    },
    "38": {
      "L": "Ira the Ithrite, Gareb the Ithrite,",
      "M": "Ira the Ithrite, Gareb the Ithrite,",
      "T": "Ira the Ithrite, Gareb the Ithrite,"
    },
    "39": {
      "L": "Uriah the Hittite: thirty-seven in all.",
      "M": "Uriah the Hittite—thirty-seven in all.",
      "T": "Uriah the Hittite. Thirty-seven in all."
    }
  },
  "24": {
    "1": {
      "L": "Again the anger of the LORD was kindled against Israel, and he incited David against them, saying, 'Go, number Israel and Judah.'",
      "M": "Again the LORD's anger was kindled against Israel, and he incited David against them, saying, 'Go, take a census of Israel and Judah.'",
      "T": "Again the LORD's anger burned against Israel, and he moved David against them, saying: 'Go and count Israel and Judah.'"
    },
    "2": {
      "L": "So the king said to Joab, the commander of the army, who was with him, 'Go through all the tribes of Israel, from Dan to Beersheba, and number the people, that I may know the number of the people.'",
      "M": "The king said to Joab, the army commander who was with him, 'Go through all the tribes of Israel from Dan to Beersheba and take a census of the people, so I may know how many there are.'",
      "T": "The king told Joab, the army commander at his side: 'Go through all the tribes of Israel—from Dan to Beersheba—and count the people. I want to know the number.'"
    },
    "3": {
      "L": "But Joab said to the king, 'May the LORD your God add to the people a hundred times as many as they are, while the eyes of my lord the king still see it, but why does my lord the king delight in this thing?'",
      "M": "But Joab said to the king, 'May the LORD your God add to the people a hundredfold—enough for my lord the king to see with his own eyes. But why does my lord the king want to do this?'",
      "T": "Joab said to the king, 'May the LORD your God multiply the people a hundredfold—enough for my lord the king to see it himself. But why does my lord the king want this?'"
    },
    "4": {
      "L": "But the king's word prevailed against Joab and against the commanders of the army. And Joab and the commanders of the army went out from before the king to number the people of Israel.",
      "M": "But the king's command overruled Joab and the army commanders. Joab and the army commanders went out from the king to count the people of Israel.",
      "T": "The king's word overruled Joab and the commanders. So Joab and the army commanders left the king's presence to count the people of Israel."
    },
    "5": {
      "L": "They crossed the Jordan and began from Aroer, on the right side of the city that is in the middle of the valley of Gad and on toward Jazer.",
      "M": "They crossed the Jordan and camped at Aroer, south of the city in the middle of the Gadite valley, and toward Jazer.",
      "T": "They crossed the Jordan and started at Aroer, on the south side of the city in the middle of the Gadite valley, working toward Jazer."
    },
    "6": {
      "L": "Then they came to Gilead, and to Kadesh in the land of the Hittites; and they came to Dan, and from Dan they went around to Sidon,",
      "M": "They went to Gilead and to Kadesh in the land of the Hittites; then they came to Dan, and from Dan they made their way around to Sidon,",
      "T": "From there to Gilead, to Kadesh in the land of the Hittites, then to Dan, then around toward Sidon—"
    },
    "7": {
      "L": "and came to the fortress of Tyre and to all the cities of the Hivites and Canaanites. And they went out to the Negeb of Judah at Beersheba.",
      "M": "and came to the fortified city of Tyre and all the cities of the Hivites and Canaanites. Then they went out into the Negeb of Judah at Beersheba.",
      "T": "—and came to the fortress of Tyre and all the cities of the Hivites and Canaanites. They finished at Beersheba in the Negeb of Judah."
    },
    "8": {
      "L": "So when they had gone through all the land, they came to Jerusalem at the end of nine months and twenty days.",
      "M": "When they had gone through the whole land, they came back to Jerusalem after nine months and twenty days.",
      "T": "They covered the whole land and came back to Jerusalem after nine months and twenty days."
    },
    "9": {
      "L": "And Joab gave the sum of the numbering of the people to the king: in Israel there were eight hundred thousand valiant men who drew the sword, and the men of Judah were five hundred thousand.",
      "M": "Joab reported the census totals to the king: Israel had eight hundred thousand fighting men capable of bearing arms, and Judah had five hundred thousand.",
      "T": "Joab reported the count to the king: eight hundred thousand fighting men in Israel who could draw the sword, and five hundred thousand in Judah."
    },
    "10": {
      "L": "But David's heart struck him after he had numbered the people. And David said to the LORD, 'I have sinned greatly in what I have done. But now, O LORD, please take away the iniquity of your servant, for I have done very foolishly.'",
      "M": "After David had counted the people, his conscience struck him. David said to the LORD, 'I have sinned greatly in what I have done. Now, LORD, please take away the guilt of your servant, for I have acted very foolishly.'",
      "T": "After the census, David's heart condemned him. He said to the LORD, 'I have sinned greatly in what I have done. Now, LORD, take away the guilt of your servant. I have been very foolish.'"
    },
    "11": {
      "L": "And when David arose in the morning, the word of the LORD came to the prophet Gad, David's seer, saying,",
      "M": "When David got up in the morning, the word of the LORD had come to the prophet Gad, David's seer:",
      "T": "When David rose the next morning, the word of the LORD had come to Gad the prophet—David's own seer:"
    },
    "12": {
      "L": "'Go and say to David, \"Thus says the LORD, Three things I offer you. Choose one of them, that I may do it to you.\"'",
      "M": "'Go and tell David, \"This is what the LORD says: I am offering you three options. Choose one of them and I will carry it out.\"'",
      "T": "'Go tell David: the LORD says this—I lay three choices before you. Choose one, and I will do it.'"
    },
    "13": {
      "L": "So Gad came to David and told him, and said to him, 'Shall three years of famine come to you in your land? Or will you flee three months before your foes while they pursue you? Or shall there be three days' pestilence in your land? Now consider and decide what answer I shall return to him who sent me.'",
      "M": "Gad came to David and told him, saying, 'Shall three years of famine come on your land? Or will you flee three months before your enemies while they pursue you? Or shall there be three days of plague in your land? Now think it over and decide what answer I should give to the one who sent me.'",
      "T": "Gad came to David and laid out the options: 'Three years of famine in your land? Or three months of fleeing from your enemies while they pursue you? Or three days of plague in your land? Think it over. What shall I tell the one who sent me?'"
    },
    "14": {
      "L": "Then David said to Gad, 'I am in great distress. Let us fall into the hand of the LORD, for his mercy is great; but let me not fall into the hand of man.'",
      "M": "David said to Gad, 'I am in terrible distress. Let us fall into the hand of the LORD, for his mercy is great; but do not let me fall into the hand of man.'",
      "T": "David said to Gad, 'I am in anguish. Let us fall into the LORD's hands—his mercy is great. But let me not fall into human hands.'"
    },
    "15": {
      "L": "So the LORD sent a pestilence upon Israel from the morning until the appointed time. And there died of the people from Dan to Beersheba seventy thousand men.",
      "M": "So the LORD sent a plague on Israel from that morning until the end of the appointed time. From Dan to Beersheba, seventy thousand men died.",
      "T": "The LORD sent a plague on Israel from that morning until the end of the appointed time. Seventy thousand men died—from Dan to Beersheba."
    },
    "16": {
      "L": "And when the angel stretched out his hand toward Jerusalem to destroy it, the LORD relented from the calamity and said to the angel who was working destruction among the people, 'It is enough; now stay your hand.' And the angel of the LORD was by the threshing floor of Araunah the Jebusite.",
      "M": "When the angel stretched out his hand toward Jerusalem to destroy it, the LORD relented from the disaster and said to the angel who was destroying the people, 'Enough! Stay your hand.' The angel of the LORD was at the threshing floor of Araunah the Jebusite.",
      "T": "When the angel stretched out his hand toward Jerusalem to destroy it, the LORD relented from the disaster. He said to the angel who was bringing devastation: 'Enough. Pull back your hand.' The angel of the LORD was standing at the threshing floor of Araunah the Jebusite."
    },
    "17": {
      "L": "Then David spoke to the LORD when he saw the angel who was striking the people, and said, 'Behold, I have sinned, and I have done wickedly. But these sheep, what have they done? Please let your hand be against me and against my father's house.'",
      "M": "When David saw the angel who was striking the people, he said to the LORD, 'I am the one who sinned, I the one who did wrong. These are but sheep—what have they done? Let your hand fall on me and my father's house.'",
      "T": "When David saw the angel who was striking the people down, he cried out to the LORD: 'I am the one who sinned. I am the one who did wrong. These are sheep—what did they do? Let your hand be against me and my father's house, not against them.'"
    },
    "18": {
      "L": "And Gad came that day to David and said to him, 'Go up, raise an altar to the LORD on the threshing floor of Araunah the Jebusite.'",
      "M": "That day Gad came to David and said to him, 'Go up and build an altar to the LORD on the threshing floor of Araunah the Jebusite.'",
      "T": "That day Gad came to David: 'Go up and build an altar to the LORD on the threshing floor of Araunah the Jebusite.'"
    },
    "19": {
      "L": "So David went up at Gad's word, as the LORD commanded.",
      "M": "David went up at Gad's word, just as the LORD had commanded.",
      "T": "David went up at Gad's word, just as the LORD had commanded."
    },
    "20": {
      "L": "And Araunah looked down and saw the king and his servants coming on toward him. And Araunah went out and paid homage to the king with his face to the ground.",
      "M": "Araunah looked up and saw the king and his servants approaching. He went out and bowed before the king with his face to the ground.",
      "T": "Araunah looked up and saw the king coming toward him with his servants. He went out and bowed to the ground before the king."
    },
    "21": {
      "L": "And Araunah said, 'Why has my lord the king come to his servant?' David said, 'To buy the threshing floor from you, in order to build an altar to the LORD, that the plague may be averted from the people.'",
      "M": "Araunah said, 'Why has my lord the king come to his servant?' David answered, 'To buy the threshing floor from you, to build an altar to the LORD, so that the plague may be lifted from the people.'",
      "T": "'Why has my lord the king come to his servant?' Araunah asked. David said, 'To buy your threshing floor and build an altar to the LORD—so the plague on the people may stop.'"
    },
    "22": {
      "L": "Then Araunah said to David, 'Let my lord the king take and offer up what seems good to him. Here are the oxen for the burnt offering and the threshing sledges and the yokes of the oxen for the wood.'",
      "M": "Araunah said to David, 'Let my lord the king take and offer whatever seems good to him. Here are the oxen for the burnt offering, and the threshing sledges and the ox yokes for wood.'",
      "T": "Araunah said to David, 'Take whatever you need, my lord the king, and offer it. Here are the oxen for the burnt offering, and the threshing sledges and ox yokes for the wood.'"
    },
    "23": {
      "L": "All this, O king, Araunah gives to the king. And Araunah said to the king, 'May the LORD your God accept you.'",
      "M": "All this, O king, Araunah gives to the king. Araunah also said to the king, 'May the LORD your God be favorable to you.'",
      "T": "'All of it, my lord the king—Araunah gives it all to the king.' And he added: 'May the LORD your God receive you with favor.'"
    },
    "24": {
      "L": "But the king said to Araunah, 'No, but I will buy it from you for a price. I will not offer burnt offerings to the LORD my God that cost me nothing.' So David bought the threshing floor and the oxen for fifty shekels of silver.",
      "M": "But the king replied to Araunah, 'No, I insist on buying it from you at full price. I will not offer to the LORD my God burnt offerings that cost me nothing.' David bought the threshing floor and the oxen for fifty shekels of silver.",
      "T": "But the king said, 'No. I will buy it from you at the full price. I will not offer to the LORD my God burnt offerings that cost me nothing.' David paid fifty shekels of silver for the threshing floor and the oxen."
    },
    "25": {
      "L": "And David built there an altar to the LORD and offered burnt offerings and peace offerings. So the LORD responded to the plea for the land, and the plague was averted from Israel.",
      "M": "David built an altar to the LORD there and offered burnt offerings and fellowship offerings. The LORD responded to the plea for the land, and the plague was lifted from Israel.",
      "T": "David built the altar there and offered burnt offerings and peace offerings. The LORD heard the plea for the land, and the plague over Israel was stayed."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '2samuel', existing)
    print('2 Samuel 19–24 written.')

if __name__ == '__main__':
    main()
