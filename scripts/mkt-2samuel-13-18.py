"""
MKT 2 Samuel chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2samuel-13-18.py

Translation decisions:
- H3068 (יהוה): "LORD" in L/M throughout; "the LORD" in T — consistent with mkt-2samuel-1-6.py
- H430 (אֱלֹהִים): "God" in all tiers throughout
- H2617 (חֶסֶד): "kindness" (L) / "steadfast loyalty" (M) / "faithful love" or "covenant love" (T)
  — ch 15:20 David to Ittai; consistent with prior script
- H6031 (ʿinnāh): "violated" (L) / "raped" (M/T) — the Hebrew term specifically denotes sexual
  humiliation and violence. Older rendering "humbled" obscures the assault. T makes the violation
  explicit. This is the same word used of Dinah in Genesis 34.
- H5038 (nĕbālāh): "folly" (L) / "outrage" (M) / "vile thing / disgrace" (T) — this is the OT
  legal term for sexual violation that defiles the community (cf. Gen 34:7, Deut 22:21). Tamar
  uses it deliberately in 13:12 to name what Amnon is contemplating as a communal crime, not
  merely a personal failing. T surfaces this weight.
- H5315 (נֶפֶשׁ): "soul" (L) / "heart" or "desire" or "life" in M/T depending on context —
  13:39 "the soul of King David was consumed/exhausted" = his longing was spent; 16:11 "my son
  who came from my own body seeks my life."
- H8130 (śānēʾ, "hate"): 13:15 — the reversal of Amnon's stated "love" to "hatred" is stark and
  narratively central. L "hated," M "hated," T conveys the shock of the reversal.
- Ch 13:21 follows MT: "David was very angry" — the MT clause about not punishing Amnon because
  he loved him (present in some LXX manuscripts) is not in MT and not translated here.
- Ch 15:7 "forty years": MT reads forty (ארבעים). Contextually four years is far more likely
  (Josephus, most MSS), but the interlinear follows MT. L renders "forty," M/T render "four" with
  a note that MT reads "forty" — the narrative chronology makes forty impossible.
- H17:25 Ithra's nationality: MT "Israelite" (יִשְׂרְאֵלִי), but 1 Chr 2:17 reads "Ishmaelite."
  L/M/T follow MT ("Israelite"), noting the variant.
- H2525 (Absalom monument, 18:18): T surfaces the bitter irony — Absalom raised the pillar
  because he had no son to carry his name; his name is now remembered chiefly for his shameful
  death.
- David's mourning cry 18:33: The Hebrew repetition of "my son" (בְּנִי) seven times is
  deliberate, anguished, liturgical. T tier uses line breaks to honor this as a grief-cry
  parallel to a lament. L/M render as elevated prose.
- H17:23 (Ahithophel's suicide): A shame-honor death — his counsel was rejected publicly;
  he cannot survive that humiliation. T notes this dynamic. He sets his house in order first
  (a last act of dignity) before hanging himself.
- Hushai's counter-counsel (ch 17): T surfaces his rhetorical strategy — he exploits Absalom's
  vanity by flattering the scale of his army and promising glory.
- H18:8 "the forest devoured more than the sword": T makes the irony explicit — the wilderness
  that David fled into became Absalom's killer.
- OT echoes: The Tamar narrative (ch 13) echoes Dinah (Gen 34) — same word ʿinnāh, same
  outrage-term nĕbālāh, same pattern of political inaction and private vengeance. T tier notes
  where resonant. Absalom's flight to Geshur echoes Jacob's flight to Laban after Esau's
  threatened vengeance. David's weeping ascent of the Mount of Olives (15:30) is a shadow of
  the passion narrative (cf. Luke 22:39 echo anticipated here). David's command "deal gently
  with Absalom" echoes Abraham's plea for Ishmael (Gen 21:11) — the same anguish of a father
  for a son who must be sent away.
- Aspect notes: waw-consecutive imperfects throughout = narrative past. The repeated "sent"
  (šālaḥ) and "went" (hālak) carry the driving momentum of the narrative. The stative "was
  enraged / was afraid" = perfect of state.
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
  "13": {
    "1": {
      "L": "Now it came to pass after this that Absalom the son of David had a beautiful sister whose name was Tamar, and Amnon the son of David loved her.",
      "M": "After this, Absalom son of David had a beautiful sister named Tamar, and Amnon son of David fell in love with her.",
      "T": "After this, David's son Absalom had a beautiful sister named Tamar. And David's son Amnon became obsessed with her."
    },
    "2": {
      "L": "And Amnon was so vexed that he fell sick on account of his sister Tamar, for she was a virgin and it seemed hard to Amnon to do anything to her.",
      "M": "Amnon was so tormented by desire for his sister Tamar that he became ill, for she was a virgin and it seemed impossible for him to do anything to her.",
      "T": "Amnon was consumed with longing for Tamar—consumed to the point of sickness. She was a virgin, protected by the court; there was nothing he could do. Or so it seemed."
    },
    "3": {
      "L": "But Amnon had a friend whose name was Jonadab, the son of Shimeah, David's brother; and Jonadab was a very shrewd man.",
      "M": "But Amnon had a friend named Jonadab, son of Shimeah, David's brother; and Jonadab was a very shrewd man.",
      "T": "But Amnon had a friend: Jonadab son of Shimeah, David's brother. Jonadab was clever—dangerously clever."
    },
    "4": {
      "L": "He said to him, 'Why are you, the king's son, so lean from day to day? Will you not tell me?' And Amnon said to him, 'I love Tamar, my brother Absalom's sister.'",
      "M": "He said to Amnon, 'Why are you, the king's son, growing thinner day after day? Won't you tell me?' Amnon said, 'I love Tamar, my brother Absalom's sister.'",
      "T": "Jonadab said to him, 'Why are you getting thinner day by day, prince? Tell me.' Amnon said: 'I am in love with Tamar—my brother Absalom's sister.'"
    },
    "5": {
      "L": "Jonadab said to him, 'Lie down on your bed and pretend to be ill. And when your father comes to see you, say to him, \"Please let my sister Tamar come and give me food to eat, and let her prepare the food in my sight so that I may see it and eat it from her hand.\"'",
      "M": "Jonadab said to him, 'Lie down on your bed and pretend to be ill. When your father comes to visit you, say to him, \"Please let my sister Tamar come and prepare food for me in my sight, so that I may see it and eat it from her hand.\"'",
      "T": "Jonadab had a plan. 'Take to your bed. Pretend you are sick. When your father comes, say to him: Let my sister Tamar come and prepare food for me—in my sight, so I can watch her, and eat from her hand.'"
    },
    "6": {
      "L": "So Amnon lay down and pretended to be ill. When the king came to see him, Amnon said to the king, 'Please let my sister Tamar come and make a couple of cakes in my sight, that I may eat from her hand.'",
      "M": "So Amnon lay down and made himself appear ill. When the king came to see him, Amnon said to the king, 'Please let my sister Tamar come and make a couple of cakes for me here, so that I may eat from her hand.'",
      "T": "Amnon did it. He took to his bed and played sick. When David came to visit, Amnon said: 'Please let my sister Tamar come and bake a few cakes for me in my room. I want to eat from her own hand.'"
    },
    "7": {
      "L": "Then David sent home to Tamar, saying, 'Go now to your brother Amnon's house and prepare food for him.'",
      "M": "David sent word to Tamar at her house, saying, 'Go to your brother Amnon's house and prepare food for him.'",
      "T": "David sent a message to Tamar at home: 'Go to your brother Amnon's house and prepare food for him.' He had no idea."
    },
    "8": {
      "L": "So Tamar went to her brother Amnon's house, where he was lying down. She took dough and kneaded it and made cakes in his sight and baked them.",
      "M": "So Tamar went to her brother Amnon's house, where he was lying down. She took dough and kneaded it and made cakes in his sight and baked them.",
      "T": "Tamar went to Amnon's house. He was lying in bed. She took the dough, kneaded it, and shaped the cakes before his eyes, then put them in the fire."
    },
    "9": {
      "L": "Then she took the pan and poured them out before him, but he refused to eat. Amnon said, 'Send everyone out from me.' So all the men went out from him.",
      "M": "She took the pan and served them to him, but he refused to eat. Amnon said, 'Send everyone away from me.' So all the men left.",
      "T": "She took the pan and served him. He refused to eat. 'Everyone out,' Amnon said. They all went."
    },
    "10": {
      "L": "Then Amnon said to Tamar, 'Bring the food into the chamber, that I may eat from your hand.' And Tamar took the cakes she had made and brought them into the chamber to her brother Amnon.",
      "M": "Then Amnon said to Tamar, 'Bring the food into the bedroom, so that I may eat from your hand.' Tamar took the cakes she had made and brought them to her brother Amnon in the bedroom.",
      "T": "Then Amnon said to Tamar: 'Bring the food into the inner room. I want to eat from your hand.' Tamar took the cakes she had made and brought them to him in the inner room."
    },
    "11": {
      "L": "But when she brought them near to him to eat, he took hold of her and said to her, 'Come lie with me, my sister.'",
      "M": "But when she brought them close to him to eat, he grabbed hold of her and said, 'Come to bed with me, my sister.'",
      "T": "As she brought the food close, he seized her. 'Come to bed with me, my sister,' he said."
    },
    "12": {
      "L": "She answered him, 'No, my brother, do not force me, for no such thing ought to be done in Israel. Do not do this folly.'",
      "M": "She answered him, 'No, my brother! Do not violate me—for no such outrage should be done in Israel. Do not do this disgraceful thing.'",
      "T": "'No, my brother!' she said. 'Do not force me. This is not done in Israel—this is a vile disgrace. Do not do this thing.'"
    },
    "13": {
      "L": "'And I, where would I carry my shame? And as for you, you would be as one of the disgraced fools in Israel. Now therefore, speak to the king, for he will not withhold me from you.'",
      "M": "'As for me, where would I take my shame? And as for you, you would be like one of the disgraced fools in Israel. Please speak to the king—he will not refuse you.'",
      "T": "'Where would I go with my shame? And you—you would become one of the fools who disgrace Israel. Speak to the king. He will not refuse you.'"
    },
    "14": {
      "L": "But he would not listen to her. And being stronger than she, he violated her and lay with her.",
      "M": "But he would not listen to her. And being stronger than she was, he raped her.",
      "T": "He would not listen. He was stronger than she was. He raped her."
    },
    "15": {
      "L": "Then Amnon hated her with a very great hatred, so that the hatred with which he hated her was greater than the love with which he had loved her. And Amnon said to her, 'Arise and go.'",
      "M": "Then Amnon was seized with a very great hatred for her; the hatred with which he hated her was greater than the love with which he had loved her. Amnon said to her, 'Get up and go.'",
      "T": "Then Amnon hated her—violently, suddenly. The hatred that came over him was greater than the obsession that had consumed him. 'Get up,' he said. 'Get out.'"
    },
    "16": {
      "L": "But she said to him, 'No, this wrong of sending me away is greater than the other wrong you did to me.' But he would not listen to her.",
      "M": "She said to him, 'No—sending me away now is a worse wrong than what you already did to me.' But he would not listen to her.",
      "T": "'No,' she said. 'Sending me away like this is even worse than what you just did.' But he would not listen."
    },
    "17": {
      "L": "He called the young man who served him and said, 'Put this woman out from my presence and bolt the door after her.'",
      "M": "He called the servant who waited on him and said, 'Put this woman outside and bolt the door behind her.'",
      "T": "He called his servant. 'Get this woman out of my sight. Bolt the door after her.'"
    },
    "18": {
      "L": "Now she had a long robe with sleeves, for such were the garments the virgin daughters of the king wore. So his servant put her out and bolted the door behind her.",
      "M": "She had been wearing the long ornamented robe that was worn by the virgin daughters of the king. His servant put her out and bolted the door behind her.",
      "T": "She was wearing the ornamented robe worn by the royal virgin daughters. The servant put her out and bolted the door."
    },
    "19": {
      "L": "And Tamar put ashes on her head and tore the long robe that was on her, and she put her hand on her head and went away, crying aloud as she went.",
      "M": "Tamar put ashes on her head and tore the long robe she was wearing. She put her hand on her head and walked away, crying aloud as she went.",
      "T": "Tamar put ashes on her head. She tore the ornamented robe. She pressed her hand to her head and walked, weeping loudly, out into the open."
    },
    "20": {
      "L": "And her brother Absalom said to her, 'Has your brother Amnon been with you? Now hold your peace, my sister; he is your brother. Do not take this matter to heart.' So Tamar remained desolate in her brother Absalom's house.",
      "M": "Her brother Absalom said to her, 'Has your brother Amnon been with you? Be quiet for now, my sister; he is your brother—do not take this to heart.' So Tamar remained, desolate, in her brother Absalom's house.",
      "T": "Absalom saw her and knew. 'Was it Amnon?' he said. 'Be quiet now, sister. He is your brother. Do not dwell on it.' So Tamar lived in Absalom's house—ruined, silent, alone."
    },
    "21": {
      "L": "But when King David heard of all these things, he was very angry.",
      "M": "When King David heard of all these things, he was furious.",
      "T": "When King David heard what had happened, he was furious. And he did nothing."
    },
    "22": {
      "L": "But Absalom spoke to Amnon neither good nor bad, for Absalom hated Amnon because he had violated his sister Tamar.",
      "M": "Absalom said nothing to Amnon, either good or bad; for Absalom hated Amnon, because he had raped his sister Tamar.",
      "T": "Absalom said nothing to Amnon—not a word, good or bad. But he hated him. Amnon had raped Tamar his sister. Absalom remembered."
    },
    "23": {
      "L": "And after two full years, Absalom had sheepshearers at Baal-hazor, which is beside Ephraim. And Absalom invited all the king's sons.",
      "M": "Two years later, Absalom was holding a shearing at Baal-hazor, near Ephraim, and he invited all the king's sons.",
      "T": "Two years passed. Absalom held a shearing feast at Baal-hazor, near Ephraim, and invited all the king's sons."
    },
    "24": {
      "L": "And Absalom came to the king and said, 'Your servant has sheepshearers. Please let the king and his servants go with your servant.'",
      "M": "Absalom came to the king and said, 'Your servant is holding a shearing. Please let the king and his servants come with me.'",
      "T": "Absalom came to the king. 'Your servant is holding a shearing. Come with me—you and your men.'"
    },
    "25": {
      "L": "But the king said to Absalom, 'No, my son, let us not all go, or else we will be a burden to you.' He pressed him, but he would not go; however, he gave him his blessing.",
      "M": "But the king said, 'No, my son—we should not all come; we would be too great a burden to you.' Absalom pressed him, but he would not go; he blessed him and sent him away.",
      "T": "David said, 'No, my son—we would all be a burden to you.' Absalom pressed him. David would not go. He gave him his blessing."
    },
    "26": {
      "L": "Then Absalom said, 'If not, please let my brother Amnon go with us.' The king said to him, 'Why should he go with you?'",
      "M": "Then Absalom said, 'If you won't come, please let my brother Amnon come with us.' The king asked, 'Why should he go with you?'",
      "T": "'Then at least let my brother Amnon go with us.' David asked, 'Why should Amnon go?'"
    },
    "27": {
      "L": "But Absalom pressed him, and he let Amnon and all the king's sons go with him.",
      "M": "But Absalom pressed him until he let Amnon and all the king's sons go with him.",
      "T": "Absalom pressed until David agreed. Amnon went—and all the king's sons with him."
    },
    "28": {
      "L": "Then Absalom commanded his servants, saying, 'Mark now, when Amnon's heart is merry with wine, and when I say to you, \"Strike Amnon,\" then kill him. Fear not; have I not commanded you? Be courageous and valiant.'",
      "M": "Absalom ordered his servants: 'Watch for when Amnon is drunk on wine. When I say, \"Strike Amnon,\" kill him. Do not be afraid—I have commanded you. Be courageous and act.'",
      "T": "Absalom had instructed his men beforehand: 'When Amnon is drunk—when I give the word, Strike Amnon—kill him. Do not hesitate. I take full responsibility. Be brave and do it.'"
    },
    "29": {
      "L": "So the servants of Absalom did to Amnon as Absalom had commanded. Then all the king's sons rose up, and each mounted his mule and fled.",
      "M": "So Absalom's servants killed Amnon just as Absalom had commanded. Then all the king's sons sprang up, each mounted his mule, and fled.",
      "T": "Absalom's men struck Amnon dead, exactly as ordered. Every one of the king's sons leapt up, got on his mule, and fled."
    },
    "30": {
      "L": "While they were on the way, a report came to David, saying, 'Absalom has struck down all the king's sons, and not one of them is left.'",
      "M": "While they were still on their way, a report reached David: 'Absalom has killed all the king's sons—not one of them is left.'",
      "T": "While they were still on the road, the news reached David: 'Absalom has killed all your sons. Not one is left.'"
    },
    "31": {
      "L": "Then the king arose and tore his garments and lay on the ground, and all his servants were standing by with their garments torn.",
      "M": "The king rose, tore his garments, and threw himself on the ground. All his servants stood around him with their garments torn.",
      "T": "The king stood up, tore his robes, and threw himself to the ground. All his servants stood there, their robes torn."
    },
    "32": {
      "L": "But Jonadab the son of Shimeah, David's brother, answered and said, 'Let not my lord suppose that they have killed all the young men, the king's sons, for Amnon alone is dead. For this has been determined by Absalom from the day he violated his sister Tamar.'",
      "M": "But Jonadab son of Shimeah, David's brother, said, 'Let not my lord think that all the king's sons have been killed—only Amnon is dead. For Absalom has had this planned since the day Amnon raped his sister Tamar.'",
      "T": "Then Jonadab son of Shimeah—David's brother—spoke. 'My lord must not think all the princes are dead. Only Amnon is dead. Absalom has been planning this since the day Amnon raped Tamar his sister. He has been waiting two years for this moment.'"
    },
    "33": {
      "L": "Now therefore let not my lord the king take the matter to heart, to think that all the king's sons are dead, for Amnon alone is dead.",
      "M": "So my lord the king should not take to heart the report that all the king's sons are dead, for only Amnon is dead.",
      "T": "'Do not grieve for all of them, my lord. Only Amnon is dead.'"
    },
    "34": {
      "L": "But Absalom had fled. And the young man who kept the watch lifted up his eyes and looked, and behold, many people were coming from the road behind him by the side of the hill.",
      "M": "Absalom had already fled. The watchman looked up and saw a large crowd coming along the road from the hillside.",
      "T": "Absalom had fled. The lookout raised his eyes: a great crowd was coming down the road along the hillside."
    },
    "35": {
      "L": "And Jonadab said to the king, 'Behold, the king's sons are coming! As your servant said, so it is.'",
      "M": "Jonadab said to the king, 'Look—the king's sons are coming! It is just as your servant said.'",
      "T": "Jonadab said: 'Look—the king's sons are coming. It is as I said.'"
    },
    "36": {
      "L": "And as soon as he had finished speaking, behold, the king's sons came and lifted up their voice and wept. And the king also and all his servants wept very bitterly.",
      "M": "Just as he finished speaking, the king's sons arrived and wept aloud. And the king and all his servants wept bitterly.",
      "T": "He had barely finished speaking when the princes came in and broke into weeping. The king and all his men wept with them—loud, uncontrolled grief."
    },
    "37": {
      "L": "But Absalom fled and went to Talmai the son of Ammihud, king of Geshur. And David mourned for his son day after day.",
      "M": "Absalom fled and went to Talmai son of Ammihud, king of Geshur. And David mourned for his son every day.",
      "T": "Absalom had fled to Talmai son of Ammihud, king of Geshur—his mother's people. And David mourned for his son, day after day."
    },
    "38": {
      "L": "So Absalom fled and went to Geshur, and was there three years.",
      "M": "Absalom fled to Geshur and lived there three years.",
      "T": "Absalom lived in Geshur three years."
    },
    "39": {
      "L": "And the soul of King David longed to go out to Absalom, for he had been comforted concerning Amnon, since he was dead.",
      "M": "The heart of King David burned with longing to go to Absalom, for he had been comforted about Amnon, who was dead.",
      "T": "The king's longing to go to Absalom grew unbearable. The grief for Amnon had run its course—Amnon was gone. But Absalom was out there, unreachable."
    }
  },
  "14": {
    "1": {
      "L": "Now Joab the son of Zeruiah perceived that the king's heart was fixed on Absalom.",
      "M": "Joab son of Zeruiah saw that the king's heart was set on Absalom.",
      "T": "Joab son of Zeruiah read the king's mind: David's heart had gone to Absalom."
    },
    "2": {
      "L": "And Joab sent to Tekoa and fetched from there a wise woman, and said to her, 'Please pretend to be a mourning woman; put on mourning garments, do not anoint yourself with oil, but be like a woman who has been long mourning for the dead.'",
      "M": "Joab sent to Tekoa and brought a wise woman from there. He said to her, 'Please act the part of a mourning woman; put on mourning clothes, do not anoint yourself with oil, but behave as a woman who has long been grieving for the dead.'",
      "T": "Joab sent to Tekoa and brought a wise woman from there. He told her: 'Play the part of a woman in mourning—wear mourning clothes, no oil, the look of someone who has grieved a long time.'"
    },
    "3": {
      "L": "'And go to the king and speak these words to him.' So Joab put the words in her mouth.",
      "M": "'Go to the king and speak like this.' And Joab put the words in her mouth.",
      "T": "'Go to the king and say what I tell you.' He coached her word by word."
    },
    "4": {
      "L": "When the woman of Tekoa came to the king, she fell on her face to the ground and did obeisance and said, 'Help, O king!'",
      "M": "The woman of Tekoa came to the king, fell on her face to the ground, bowed low, and said, 'Help me, O king!'",
      "T": "The woman of Tekoa came before the king. She fell to the ground in obeisance and cried: 'Help me, O king!'"
    },
    "5": {
      "L": "The king said to her, 'What is your trouble?' She answered, 'Truly I am a widow; my husband died.'",
      "M": "The king asked her, 'What is your trouble?' She said, 'I am a widow. My husband has died.'",
      "T": "'What troubles you?' the king asked. 'I am a widow,' she said. 'My husband is dead.'"
    },
    "6": {
      "L": "'Your servant had two sons, and they quarreled together in the field. And there was no one to part them, and one struck the other and killed him.'",
      "M": "'Your servant had two sons. They got into a fight in the field, with no one to separate them, and one struck the other and killed him.'",
      "T": "'I had two sons. They quarreled in the field—no one was there to stop them—and one killed the other.'"
    },
    "7": {
      "L": "'And now the whole family has risen against your servant, and they say, \"Give up the man who struck his brother, that we may put him to death for the life of his brother whom he killed, and so destroy the heir also.\" Thus they would quench my one remaining coal and leave to my husband neither name nor remnant on the face of the earth.'",
      "M": "'Now the whole clan has risen against your servant. They say, \"Hand over the one who killed his brother, that we may execute him for his brother's death, even if we destroy the heir.\" They want to quench the one ember I have left and leave my husband no name or remnant on earth.'",
      "T": "'Now the whole family has turned on me. Give us the killer, they say—give him over so we can execute him for his brother's blood, even if it destroys the heir. They want to snuff out the one coal I have left—leave my husband with no name, no trace, anywhere on this earth.'"
    },
    "8": {
      "L": "Then the king said to the woman, 'Go to your house, and I will give orders concerning you.'",
      "M": "The king said to the woman, 'Go home, and I will give orders on your behalf.'",
      "T": "The king said: 'Go home. I will give instructions on your behalf.'"
    },
    "9": {
      "L": "The woman of Tekoa said to the king, 'My lord the king, let the guilt be on me and on my father's house, and let the king and his throne be guiltless.'",
      "M": "The woman of Tekoa said to the king, 'My lord the king, let the guilt fall on me and my father's house. Let the king and his throne be free of blame.'",
      "T": "'My lord,' the woman said, 'let any guilt fall on me and on my father's house. The king and his throne must be kept clean.'"
    },
    "10": {
      "L": "The king said, 'Whoever says anything to you, bring him to me, and he shall not touch you again.'",
      "M": "The king said, 'If anyone says anything more to you, bring him to me and he shall not touch you again.'",
      "T": "'If anyone threatens you further,' the king said, 'bring him to me. He will not lay a hand on you.'"
    },
    "11": {
      "L": "Then she said, 'Please let the king remember the LORD your God, that the avenger of blood not destroy, lest they destroy my son.' He said, 'As the LORD lives, not one hair of your son shall fall to the ground.'",
      "M": "She said, 'Please let the king invoke the LORD your God, so that the avenger of blood may not add to the destruction—they must not kill my son.' He said, 'As the LORD lives, not one hair of your son shall fall to the ground.'",
      "T": "'Please,' she said, 'let the king swear by the LORD your God—so that the blood-avenger does not destroy my son.' He said: 'As the LORD lives, not a hair of your son shall touch the ground.'"
    },
    "12": {
      "L": "Then the woman said, 'Please let your servant speak a word to my lord the king.' He said, 'Speak.'",
      "M": "Then the woman said, 'Please let your servant say one more word to my lord the king.' He said, 'Say it.'",
      "T": "The woman said: 'May your servant say one more word to my lord the king?' 'Say it,' he said."
    },
    "13": {
      "L": "The woman said, 'Why then have you devised such a thing against the people of God? For in giving this ruling the king convicts himself, in that the king does not bring back his banished one.'",
      "M": "The woman said, 'Why then have you made such a plan against the people of God? For in making this ruling you convict yourself—the king does not bring back the one he has banished.'",
      "T": "'Then why have you done the same thing to God's own people? By making this ruling, you have convicted yourself—you, the king, will not bring home the one you have banished.'"
    },
    "14": {
      "L": "'For we will all surely die; we are like water spilled on the ground that cannot be gathered up again. But God does not take away life; he devises means so that the outcast will not be permanently banished from him.'",
      "M": "'We all must die; we are like water poured out on the ground that cannot be gathered back. But God does not take away life; rather, he makes plans so that the banished one is not kept away from him forever.'",
      "T": "'We all die. We are like water poured on the ground—it cannot be gathered back. But God does not sweep away a life; he finds a way to bring the outcast home. He does not want anyone permanently cut off from his presence.'"
    },
    "15": {
      "L": "'Now I have come to say this to my lord the king because the people have made me afraid. Your servant thought, \"I will speak to the king; perhaps the king will act on his servant's request.\"'",
      "M": "'And now I have come to say this to my lord the king because the people frightened me. Your servant thought, \"I will speak to the king; perhaps the king will do what his servant asks.\"'",
      "T": "'I have come to say this because the people have frightened me. I thought: I will speak to the king. Perhaps he will do what his servant asks.'"
    },
    "16": {
      "L": "'For the king will hear and deliver his servant from the hand of the man who would destroy both me and my son together from the inheritance of God.'",
      "M": "'For the king will listen and rescue his servant from the hand of the man who would destroy both me and my son from God's inheritance.'",
      "T": "'The king will hear and rescue his servant from the hand of those who would cut off both me and my son from God's inheritance.'"
    },
    "17": {
      "L": "Then your servant said, 'Please let the word of my lord the king be comforting; for as the angel of God, so is my lord the king in discerning good and evil. The LORD your God be with you!'",
      "M": "'Your servant said, \"Let the word of my lord the king bring comfort; for my lord the king is like the angel of God in discerning good and evil. The LORD your God be with you!\"'",
      "T": "'I thought: the word of my lord the king will give me rest—for he is like an angel of God in knowing good from evil. May the LORD your God be with you.'"
    },
    "18": {
      "L": "Then the king answered and said to the woman, 'Do not hide from me anything I ask you.' And the woman said, 'Let my lord the king speak.'",
      "M": "The king replied to the woman, 'Do not hide from me what I am about to ask you.' The woman said, 'Let my lord the king speak.'",
      "T": "The king said to her: 'Answer me one thing. Hide nothing.' 'Let my lord speak,' she said."
    },
    "19": {
      "L": "And the king said, 'Is the hand of Joab with you in all this?' The woman answered and said, 'As your soul lives, my lord the king, one cannot turn right or left from anything my lord the king has said. For it was your servant Joab who commanded me; it was he who put all these words into the mouth of your servant.'",
      "M": "The king said, 'Is Joab behind all of this?' The woman answered, 'As surely as you live, my lord the king, no one can turn right or left from what my lord the king has said. Yes, it was your servant Joab who ordered this; it was he who put all these words in my mouth.'",
      "T": "The king said: 'Was Joab behind this?' The woman said: 'As you live, my lord, no one can turn right or left from a word my lord has spoken. Yes—it was Joab who sent me. He put every one of these words in my mouth.'"
    },
    "20": {
      "L": "'In order to change the form of affairs your servant Joab did this. But my lord has wisdom like the wisdom of the angel of God to know all things that are on the earth.'",
      "M": "'Your servant Joab did this to bring a change in the situation. My lord is wise, like the wisdom of an angel of God, knowing everything that happens in the land.'",
      "T": "'He did it to change the direction of things. But my lord has wisdom like the wisdom of an angel of God—there is nothing happening in this land that escapes him.'"
    },
    "21": {
      "L": "Then the king said to Joab, 'Behold, I grant this; go and bring back the young man Absalom.'",
      "M": "The king said to Joab, 'I have decided: go and bring back the young man Absalom.'",
      "T": "The king said to Joab: 'I have made my decision. Go—bring Absalom back.'"
    },
    "22": {
      "L": "And Joab fell on his face to the ground and did obeisance and blessed the king. Then Joab said, 'Today your servant knows that I have found favor in your sight, my lord the king, in that the king has done what his servant asked.'",
      "M": "Joab fell on his face to the ground, bowed low, and blessed the king. Joab said, 'Today your servant knows that I have found favor in your eyes, my lord the king—because the king has done what his servant asked.'",
      "T": "Joab fell with his face to the ground in obeisance and blessed the king. 'Today your servant knows he has found favor in your sight, my lord,' Joab said. 'You have done what I asked.'"
    },
    "23": {
      "L": "So Joab arose and went to Geshur and brought Absalom to Jerusalem.",
      "M": "Joab set out, went to Geshur, and brought Absalom back to Jerusalem.",
      "T": "Joab went to Geshur and brought Absalom back to Jerusalem."
    },
    "24": {
      "L": "And the king said, 'Let him go to his own house, but my face he shall not see.' So Absalom went to his own house and did not see the king's face.",
      "M": "The king said, 'He may go to his own house, but he shall not appear before me.' So Absalom went to his own house and did not come before the king.",
      "T": "'Let him go to his own house,' the king said. 'He is not to see my face.' So Absalom came home to Jerusalem—but remained cut off from his father."
    },
    "25": {
      "L": "Now in all Israel there was no one so much to be praised for his beauty as Absalom; from the sole of his foot to the crown of his head there was no blemish in him.",
      "M": "In all Israel no one was as widely admired for his beauty as Absalom; from the sole of his foot to the crown of his head there was no flaw in him.",
      "T": "In all Israel there was no man as celebrated for his looks as Absalom. From his feet to his head there was not a single flaw."
    },
    "26": {
      "L": "When he cut the hair of his head—for at the end of every year he used to cut it, because it was heavy on him—he weighed the hair of his head at two hundred shekels by the king's weight.",
      "M": "At the end of every year he cut his hair, because it grew too heavy. When he weighed it, it came to two hundred shekels by the royal standard.",
      "T": "He cut his hair once a year—it grew too heavy. When he weighed it, it came to two hundred shekels by the royal standard. Even his hair was extraordinary."
    },
    "27": {
      "L": "And there were born to Absalom three sons and one daughter, whose name was Tamar; she was a beautiful woman.",
      "M": "Absalom had three sons and one daughter. His daughter's name was Tamar, and she was a beautiful woman.",
      "T": "Absalom had three sons and a daughter. The daughter was named Tamar—a beautiful woman, named for her violated aunt."
    },
    "28": {
      "L": "So Absalom lived two full years in Jerusalem without seeing the king's face.",
      "M": "Absalom lived in Jerusalem two full years without coming before the king.",
      "T": "Two full years Absalom lived in Jerusalem without being allowed into his father's presence."
    },
    "29": {
      "L": "Then Absalom sent for Joab, to send him to the king, but Joab would not come to him. And he sent again a second time, but Joab would not come.",
      "M": "Absalom sent for Joab, wanting to send him to the king, but Joab would not come. He sent for him a second time, but Joab still refused to come.",
      "T": "Absalom sent for Joab—he wanted Joab to take a message to the king. Joab would not come. He sent again. Joab would not come."
    },
    "30": {
      "L": "Then Absalom said to his servants, 'See, Joab's field is next to mine, and he has barley there; go and set it on fire.' So Absalom's servants set the field on fire.",
      "M": "Then Absalom said to his servants, 'Look—Joab's field is next to mine, and he has barley growing there. Go set it on fire.' Absalom's servants set the field ablaze.",
      "T": "Absalom told his servants: 'Joab's field is right next to mine. There is barley in it. Burn it.' They burned it."
    },
    "31": {
      "L": "Then Joab arose and came to Absalom's house and said to him, 'Why have your servants set my field on fire?'",
      "M": "Joab came to Absalom's house and said, 'Why did your servants set my field on fire?'",
      "T": "Joab came to Absalom's house. 'Why did your men burn my field?'"
    },
    "32": {
      "L": "Absalom answered Joab, 'Look, I sent word to you, saying, \"Come here, so that I may send you to the king to say, Why have I come from Geshur? It would be better for me if I were still there.\" Now let me see the king's face; and if there is guilt in me, let him kill me.'",
      "M": "Absalom answered Joab, 'I sent for you and said, \"Come here so I can send you to the king to ask: Why did I come from Geshur? It would have been better to stay there.\" Now let me see the king's face. If there is any fault in me, let him put me to death.'",
      "T": "'I sent for you,' Absalom said. 'I wanted you to go to the king and ask: why did I come back from Geshur? I would have been better off staying there. Now let me see the king's face. If I am guilty, let him kill me.'"
    },
    "33": {
      "L": "So Joab went to the king and told him. And he summoned Absalom, so he came to the king and bowed himself on his face to the ground before the king. And the king kissed Absalom.",
      "M": "Joab went to the king and reported this. The king summoned Absalom, and he came and bowed with his face to the ground before the king. And the king kissed Absalom.",
      "T": "Joab went and reported to the king. David summoned Absalom. Absalom came and bowed with his face to the ground. The king kissed him."
    }
  },
  "15": {
    "1": {
      "L": "And after this it came to pass that Absalom prepared for himself a chariot and horses, and fifty men to run before him.",
      "M": "After this, Absalom provided himself with a chariot and horses, and fifty men to run before him.",
      "T": "After this Absalom got himself a chariot and horses, with fifty men to run ahead of him. The performance of kingship."
    },
    "2": {
      "L": "And Absalom used to rise early and stand beside the way at the gate. And whenever any man had a dispute to come before the king for judgment, Absalom would call to him and say, 'From what city are you?' And when he said, 'Your servant is from such and such a tribe in Israel,'",
      "M": "Absalom would get up early and stand beside the road at the gate. Whenever a man had a dispute and was coming to the king for a ruling, Absalom would call out to him and say, 'From what city are you?' When the man answered, 'Your servant is from such and such a tribe in Israel,'",
      "T": "He would rise early and stand at the gate road. Whenever someone came to the king for a legal judgment, Absalom would call out: 'Where are you from?' 'Your servant is from one of the tribes of Israel,' the man would say."
    },
    "3": {
      "L": "Absalom would say to him, 'See, your matters are good and right; but there is no one deputed by the king to hear you.'",
      "M": "Absalom would say to him, 'Your case is good and just, but there is no one assigned by the king to hear it.'",
      "T": "Absalom would say: 'Your claim is just and right. But there is no one appointed by the king to hear it.'"
    },
    "4": {
      "L": "Absalom said, 'Oh that I were made judge in the land, so that every man with a dispute or a cause might come to me, and I would give him justice!'",
      "M": "Then Absalom would say, 'If only I were made judge in the land! Everyone with a lawsuit or cause could come to me, and I would give him justice.'",
      "T": "'If only I were judge in this land,' Absalom would say. 'Anyone with a case could come to me. I would give him justice.'"
    },
    "5": {
      "L": "And when any man came near to do obeisance to him, he would put out his hand and take hold of him and kiss him.",
      "M": "Whenever a man approached to bow before him, Absalom would reach out, take hold of him, and kiss him.",
      "T": "When a man would bow before him, Absalom would reach out, pull him close, and kiss him."
    },
    "6": {
      "L": "Thus Absalom did to all of Israel who came to the king for judgment. So Absalom stole the hearts of the men of Israel.",
      "M": "This is what Absalom did to every Israelite who came to the king for justice; and so Absalom stole the hearts of the people of Israel.",
      "T": "This was his pattern with every Israelite who came for justice before the king. And so Absalom stole the hearts of Israel."
    },
    "7": {
      "L": "And at the end of forty years, Absalom said to the king, 'Please let me go and pay my vow which I have vowed to the LORD in Hebron.'",
      "M": "After four years, Absalom said to the king, 'Please let me go to Hebron and pay the vow I made to the LORD.' (The Hebrew reads 'forty years,' but four years fits the narrative context.)",
      "T": "Four years into this, Absalom said to the king: 'Let me go to Hebron and keep the vow I made to the LORD.'"
    },
    "8": {
      "L": "'For your servant made a vow while I lived at Geshur in Aram: If the LORD truly brings me back to Jerusalem, then I will serve the LORD.'",
      "M": "'While I was living at Geshur in Aram, I made a vow: if the LORD brings me back to Jerusalem, I will worship the LORD.'",
      "T": "'When I was in Geshur, I made a vow: if the LORD brings me back to Jerusalem, I will worship him in Hebron.' A lie dressed as devotion."
    },
    "9": {
      "L": "The king said to him, 'Go in peace.' So he arose and went to Hebron.",
      "M": "The king said to him, 'Go in peace.' So he arose and went to Hebron.",
      "T": "The king said: 'Go in peace.' Absalom rose and went to Hebron."
    },
    "10": {
      "L": "But Absalom sent spies throughout all the tribes of Israel, saying, 'As soon as you hear the sound of the trumpet, then say, \"Absalom is king at Hebron.\"'",
      "M": "But Absalom sent secret messengers throughout all the tribes of Israel, saying, 'As soon as you hear the trumpet blast, shout: Absalom has become king at Hebron!'",
      "T": "But Absalom had already sent agents throughout every tribe of Israel with this message: 'When you hear the ram's horn, shout: Absalom reigns in Hebron!'"
    },
    "11": {
      "L": "With Absalom went two hundred men from Jerusalem who were invited; and they went in their innocence and did not know anything.",
      "M": "Two hundred men from Jerusalem went with Absalom as invited guests; they went in all innocence, knowing nothing.",
      "T": "Two hundred men from Jerusalem went with him—invited guests, completely unsuspecting. They knew nothing of the plan."
    },
    "12": {
      "L": "And Absalom sent for Ahithophel the Gilonite, David's counselor, from his city Giloh, while he was offering sacrifices. And the conspiracy grew strong, and the people with Absalom kept increasing.",
      "M": "Absalom also sent for Ahithophel the Gilonite, David's counselor, summoning him from his city Giloh while the sacrifices were being offered. The conspiracy grew powerful, and the people supporting Absalom kept increasing.",
      "T": "Absalom had sent for Ahithophel the Gilonite—David's own counselor—calling him from Giloh while the sacrificial smoke was still rising. The conspiracy was gaining strength. The people kept coming over to Absalom."
    },
    "13": {
      "L": "And a messenger came to David, saying, 'The hearts of the men of Israel have gone after Absalom.'",
      "M": "A messenger came to David with the news: 'The hearts of the Israelites have turned to Absalom.'",
      "T": "A messenger reached David: 'The hearts of Israel have gone after Absalom.'"
    },
    "14": {
      "L": "Then David said to all his servants who were with him at Jerusalem, 'Arise, and let us flee, for there will be no escape for us from Absalom. Go quickly, lest he overtake us and bring disaster upon us and strike the city with the edge of the sword.'",
      "M": "David said to all his servants with him in Jerusalem, 'Rise up—we must flee, or none of us will escape from Absalom. We must go at once, before he overtakes us and brings disaster on us and strikes the city with the sword.'",
      "T": "David said to all his servants in Jerusalem: 'Get up. We flee—now. There is no escaping Absalom if we stay. He will overwhelm us, and the city will be put to the sword.'"
    },
    "15": {
      "L": "The king's servants said to the king, 'Your servants are ready to do whatever my lord the king decides.'",
      "M": "The king's servants said to him, 'We are ready to do whatever my lord the king decides.'",
      "T": "His servants said: 'Whatever our lord the king decides, we are ready.'"
    },
    "16": {
      "L": "So the king went out, and all his household after him. The king left ten concubines to keep the house.",
      "M": "The king left, with all his household following him. He left ten concubines behind to keep the palace.",
      "T": "The king walked out, his whole household after him. He left ten concubines to keep the palace."
    },
    "17": {
      "L": "The king went out, and all the people after him; and they halted at the last house.",
      "M": "The king went out, followed by all the people, and they stopped at the edge of the city.",
      "T": "The king went out, all the people streaming after him. They stopped at the last house at the city's edge."
    },
    "18": {
      "L": "And all his servants passed by him; and all the Cherethites, and all the Pelethites, and all the six hundred Gittites who had come with him from Gath, passed before the king.",
      "M": "All his servants marched past him—all the Cherethites, all the Pelethites, and all six hundred Gittites who had followed him from Gath—they all marched before the king.",
      "T": "His servants marched past—the Cherethites, the Pelethites, and all six hundred Gittites who had followed him from Gath. Every one of them."
    },
    "19": {
      "L": "Then the king said to Ittai the Gittite, 'Why do you also go with us? Return and stay with the king, for you are a foreigner and also an exile from your place.'",
      "M": "The king said to Ittai the Gittite, 'Why are you also coming with us? Go back and stay with the new king—you are a foreigner and also an exile from your homeland.'",
      "T": "The king stopped Ittai the Gittite. 'Why are you coming with us? Go back to whoever is king now. You are a foreigner—an exile from your own land.'"
    },
    "20": {
      "L": "'You came only yesterday, and shall I today make you wander about with us, since I must go wherever I can? Return, and take your kinsmen with you; and may the LORD show you steadfast love and faithfulness.'",
      "M": "'You arrived only yesterday—should I today make you wander with us, going I do not know where? Go back, and take your kinsmen with you. May the LORD show you steadfast love and faithfulness.'",
      "T": "'You only arrived yesterday. Should I drag you into this uncertainty with me? Go back. Take your people with you. May the LORD show you covenant loyalty and faithfulness.'"
    },
    "21": {
      "L": "But Ittai answered the king and said, 'As the LORD lives, and as my lord the king lives, in whatever place my lord the king is, whether in death or in life, even there also will your servant be.'",
      "M": "Ittai answered the king, 'As the LORD lives, and as my lord the king lives, wherever my lord the king may be—whether in death or in life—there your servant will be as well.'",
      "T": "Ittai answered: 'As the LORD lives and as my lord the king lives—wherever you are, in life or in death, I will be there too.'"
    },
    "22": {
      "L": "And David said to Ittai, 'Go on, march on.' So Ittai the Gittite marched on, with all his men and all the little ones who were with him.",
      "M": "David said to Ittai, 'Then march on.' So Ittai the Gittite marched on with all his men and all the families that were with him.",
      "T": "David said: 'Then march.' And Ittai the Gittite marched—his men, the families, everyone with him."
    },
    "23": {
      "L": "And all the country wept aloud as all the people passed over, and the king crossed over the Wadi Kidron, and all the people passed on in the direction of the wilderness.",
      "M": "All the countryside wept aloud as all the people crossed over. The king crossed the Wadi Kidron, and all the people moved on toward the wilderness.",
      "T": "The whole countryside wept aloud as the people passed. The king crossed the Kidron. Everyone moved toward the wilderness."
    },
    "24": {
      "L": "And Zadok was there also, and all the Levites were with him, carrying the ark of the covenant of God. They set down the ark of God until all the people had finished crossing out of the city; and Abiathar came up.",
      "M": "Zadok was there too, and all the Levites with him, carrying the ark of the covenant of God. They set the ark down until all the people had finished coming out of the city. Abiathar also came up.",
      "T": "Zadok was there with all the Levites, carrying the ark of the covenant of God. They set the ark down and waited until all the people had come out of the city. Abiathar came up as well."
    },
    "25": {
      "L": "Then the king said to Zadok, 'Carry the ark of God back into the city. If I find favor in the eyes of the LORD, he will bring me back and show me both it and his dwelling place.'",
      "M": "Then the king said to Zadok, 'Carry the ark of God back into the city. If I find favor in the LORD's eyes, he will bring me back and let me see it and his dwelling place again.'",
      "T": "The king said to Zadok: 'Bring the ark back into the city. If the LORD favors me, he will bring me back and let me see the ark and his dwelling again.'"
    },
    "26": {
      "L": "'But if he says, \"I have no pleasure in you,\" behold, here I am; let him do to me what seems good to him.'",
      "M": "'But if he says, \"I take no pleasure in you\"—then here I am. Let him do with me whatever seems good to him.'",
      "T": "'But if he says he wants none of me—then here I am. Let him do what is right in his eyes.'"
    },
    "27": {
      "L": "The king also said to the priest Zadok, 'Are you not a seer? Return to the city in safety, you and Abiathar, with your two sons—Ahimaaz your son and Jonathan the son of Abiathar.'",
      "M": "The king also said to the priest Zadok, 'Go back to the city in safety—you and Abiathar—with your two sons, Ahimaaz your son and Jonathan son of Abiathar.'",
      "T": "The king said to Zadok: 'Return to the city in safety—you and Abiathar, and your sons with you: Ahimaaz your son and Jonathan son of Abiathar.'"
    },
    "28": {
      "L": "'See, I will wait at the crossing places in the wilderness until a word comes from you to inform me.'",
      "M": "'Look, I will wait at the crossings of the wilderness until word comes from you to tell me what is happening.'",
      "T": "'I will wait at the ford in the wilderness until you send me word.'"
    },
    "29": {
      "L": "So Zadok and Abiathar carried the ark of God back to Jerusalem, and they stayed there.",
      "M": "Zadok and Abiathar carried the ark of God back to Jerusalem and remained there.",
      "T": "Zadok and Abiathar took the ark back into Jerusalem and stayed."
    },
    "30": {
      "L": "But David went up the ascent of the Mount of Olives, weeping as he went; his head was covered and he was walking barefoot. And all the people who were with him covered their heads and went up, weeping as they went.",
      "M": "David went up the ascent of the Mount of Olives, weeping as he went, his head covered and his feet bare. All the people with him covered their heads and went up weeping.",
      "T": "David went up the Mount of Olives weeping as he climbed. His head was covered; his feet were bare. Every person with him had their head covered, weeping as they went."
    },
    "31": {
      "L": "And someone told David, 'Ahithophel is among the conspirators with Absalom.' And David said, 'O LORD, please turn the counsel of Ahithophel into foolishness.'",
      "M": "David was told that Ahithophel was among Absalom's conspirators. And David said, 'O LORD, please make the counsel of Ahithophel foolish.'",
      "T": "David was told: Ahithophel is among the conspirators. David prayed: 'O LORD—make Ahithophel's counsel into foolishness.'"
    },
    "32": {
      "L": "When David came to the summit where God was worshiped, Hushai the Archite came to meet him with his coat torn and dirt on his head.",
      "M": "When David reached the summit where God was worshiped, Hushai the Archite met him with his coat torn and dirt on his head.",
      "T": "When David reached the top—the place of worship—Hushai the Archite was there to meet him, his robe torn and dirt on his head."
    },
    "33": {
      "L": "David said to him, 'If you go on with me, then you will be a burden to me.'",
      "M": "David said to him, 'If you go on with me, you will only be a burden to me.'",
      "T": "David said to him: 'If you come with me, you will be a burden.'"
    },
    "34": {
      "L": "'But if you return to the city and say to Absalom, \"I will be your servant, O king; as I have been your father's servant in time past, so I will now be your servant,\" then you will defeat for me the counsel of Ahithophel.'",
      "M": "'But if you return to the city and say to Absalom, \"I will be your servant, O king; I served your father before and I will serve you now,\" then you can help me by undermining the counsel of Ahithophel.'",
      "T": "'But if you go back into the city and tell Absalom: I am your servant, O king—as I served your father, so I will serve you—then you can work against Ahithophel from the inside.'"
    },
    "35": {
      "L": "'Are not Zadok and Abiathar the priests there with you? So whatever you hear from the king's house, you shall tell to the priests Zadok and Abiathar.'",
      "M": "'Zadok and Abiathar the priests are there with you, aren't they? Whatever you hear from the king's household, report it to them.'",
      "T": "'Zadok and Abiathar the priests are there—whatever you hear from the palace, tell them.'"
    },
    "36": {
      "L": "'Look, their two sons are with them—Ahimaaz, Zadok's son, and Jonathan, Abiathar's son; and by them you shall send me everything you hear.'",
      "M": "'Their two sons are there with them—Ahimaaz, Zadok's son, and Jonathan, Abiathar's son. Use them to send me everything you learn.'",
      "T": "'Ahimaaz son of Zadok and Jonathan son of Abiathar—their two sons are there. Use them to pass everything on to me.'"
    },
    "37": {
      "L": "So Hushai, David's friend, came into the city just as Absalom was entering Jerusalem.",
      "M": "So Hushai, David's friend, returned to the city just as Absalom was arriving in Jerusalem.",
      "T": "Hushai, David's friend, went back into the city. He arrived just as Absalom was entering Jerusalem."
    }
  },
  "16": {
    "1": {
      "L": "When David had passed a little beyond the summit, behold, Ziba the servant of Mephibosheth met him with a couple of donkeys saddled and carrying on them two hundred loaves of bread, a hundred clusters of raisins, a hundred of summer fruit, and a skin of wine.",
      "M": "When David had gone a little past the summit, Ziba the servant of Mephibosheth met him with a pair of saddled donkeys loaded with two hundred loaves of bread, a hundred raisin clusters, a hundred summer figs, and a skin of wine.",
      "T": "Just past the summit, Ziba the servant of Mephibosheth met David. Two donkeys, saddled, loaded: two hundred loaves of bread, a hundred clusters of raisins, a hundred summer figs, a skin of wine."
    },
    "2": {
      "L": "The king said to Ziba, 'Why have you brought these?' Ziba answered, 'The donkeys are for the king's household to ride, and the bread and summer fruit for the young men to eat, and the wine for those who grow faint in the wilderness to drink.'",
      "M": "The king said to Ziba, 'What is all this for?' Ziba answered, 'The donkeys are for the king's household to ride, the bread and fruit are for the young men to eat, and the wine is for those who become exhausted in the wilderness.'",
      "T": "The king asked: 'What is all this?' Ziba said: 'The donkeys for the royal household to ride. The bread and fruit for the men. The wine for anyone who collapses in the wilderness.'"
    },
    "3": {
      "L": "And the king said, 'And where is your master's son?' Ziba said to the king, 'Behold, he remains in Jerusalem; for he said, \"Today the house of Israel will restore my grandfather's kingdom to me.\"'",
      "M": "The king said, 'And where is your master's grandson?' Ziba answered the king, 'He is staying in Jerusalem; he said, \"Today the house of Israel will give back my grandfather's kingdom to me.\"'",
      "T": "The king asked: 'Where is your master's son?' Ziba said: 'He stayed in Jerusalem. He said: Today Israel will restore my grandfather's kingdom to me.'"
    },
    "4": {
      "L": "Then the king said to Ziba, 'All that belonged to Mephibosheth is now yours.' And Ziba said, 'I bow before you; let me find favor in your sight, my lord the king.'",
      "M": "The king said to Ziba, 'All that belongs to Mephibosheth is yours.' Ziba said, 'I bow before you; may I find favor in your eyes, my lord the king.'",
      "T": "'Everything that belonged to Mephibosheth is yours,' the king said. 'I bow before you,' Ziba said. 'May I find favor in your sight, my lord.'"
    },
    "5": {
      "L": "When King David came to Bahurim, there came out from there a man from the family of the house of Saul, whose name was Shimei the son of Gera, and he came out, cursing continually as he came.",
      "M": "When King David reached Bahurim, a man of the family of Saul's house came out from there—Shimei son of Gera. He came out cursing as he went.",
      "T": "As David came to Bahurim, a man came out of the town—Shimei son of Gera, from Saul's own family. He came out cursing, and he kept on cursing."
    },
    "6": {
      "L": "He threw stones at David and at all the servants of King David; but all the people and all the mighty men were on his right hand and on his left.",
      "M": "He pelted David and all the king's servants with stones, even as the troops and all the warriors were there on either side of David.",
      "T": "He threw stones at David and at all his servants—even with the warriors flanking David on both sides."
    },
    "7": {
      "L": "And Shimei said as he cursed, 'Out! Out! You man of blood! You man of worthlessness!'",
      "M": "Shimei shouted as he cursed: 'Get out! Get out! You man of blood! You worthless wretch!'",
      "T": "'Out! Out!' Shimei was shouting. 'You man of blood! You contemptible nobody!'"
    },
    "8": {
      "L": "'The LORD has repaid you for all the blood of the house of Saul, in whose place you have reigned; and the LORD has given the kingdom into the hand of your son Absalom. And behold, you are taken in your own calamity, because you are a man of blood!'",
      "M": "'The LORD has repaid you for all the blood of the house of Saul, in whose place you have reigned. The LORD has given the kingdom to your son Absalom. Look at you now—caught in your own disaster, you bloody man!'",
      "T": "'The LORD is repaying you for all the blood of Saul's house—the family you replaced! Now the LORD has given the kingdom to your own son Absalom. And here you are, ruined by your own guilt—you man of blood!'"
    },
    "9": {
      "L": "Then Abishai the son of Zeruiah said to the king, 'Why should this dead dog curse my lord the king? Please let me go over and cut off his head.'",
      "M": "Abishai son of Zeruiah said to the king, 'Why should this dead dog curse my lord the king? Let me go and cut off his head.'",
      "T": "Abishai son of Zeruiah said: 'Why should this dead dog curse my lord the king? Let me go over and take off his head.'"
    },
    "10": {
      "L": "But the king said, 'What have I to do with you, O sons of Zeruiah? If he is cursing because the LORD has said to him, \"Curse David,\" who then shall say, \"Why have you done so?\"'",
      "M": "The king said, 'What does this have to do with me and you, sons of Zeruiah? If the LORD has told him, \"Curse David,\" who are you to say, \"Why are you doing this?\"'",
      "T": "The king said: 'What is this to me, sons of Zeruiah? If the LORD has said to him, Curse David—who am I to stop him?'"
    },
    "11": {
      "L": "And David said to Abishai and to all his servants, 'Behold, my own son who came forth from my body seeks my life; how much more now may this Benjaminite? Leave him alone, and let him curse, for the LORD has bidden him.'",
      "M": "David said to Abishai and all his servants, 'My own son, my flesh and blood, is trying to kill me. How much more, then, this Benjaminite? Leave him alone; let him curse—the LORD has told him to.'",
      "T": "'My own son—my own flesh—wants me dead. How much more this man? Leave him. Let him curse. The LORD has given him this assignment.'"
    },
    "12": {
      "L": "'Perhaps the LORD will look on my affliction and the LORD will repay me with good for his cursing me today.'",
      "M": "'Perhaps the LORD will see my suffering and repay me with good for the cursing I receive today.'",
      "T": "'Perhaps the LORD will see the wrong being done to me and repay me with something good in exchange for this cursing.'"
    },
    "13": {
      "L": "So David and his men went along the road, while Shimei went on the hillside opposite him and cursed as he went and threw stones at him and flung dust.",
      "M": "So David and his men continued along the road, while Shimei moved along the opposite hillside, cursing and throwing stones and flinging dirt as he went.",
      "T": "David and his men walked on. Shimei walked along the facing hillside, level with them, still cursing, throwing stones, throwing dust."
    },
    "14": {
      "L": "And the king and all the people who were with him arrived weary at the Jordan; and there he refreshed himself.",
      "M": "The king and all the people with him arrived exhausted at the Jordan and rested there.",
      "T": "The king and all his people arrived at the Jordan exhausted. They rested there."
    },
    "15": {
      "L": "Now Absalom and all the people, the men of Israel, came to Jerusalem, and Ahithophel was with him.",
      "M": "Absalom and all the Israelites arrived in Jerusalem, and Ahithophel was with him.",
      "T": "Absalom entered Jerusalem with all Israel, and Ahithophel at his side."
    },
    "16": {
      "L": "And when Hushai the Archite, David's friend, came to Absalom, Hushai said to Absalom, 'Long live the king! Long live the king!'",
      "M": "When Hushai the Archite, David's friend, came to Absalom, he said to him, 'Long live the king! Long live the king!'",
      "T": "When Hushai the Archite—David's friend—came to Absalom, he cried out: 'Long live the king! Long live the king!'"
    },
    "17": {
      "L": "And Absalom said to Hushai, 'Is this your steadfast love to your friend? Why did you not go with your friend?'",
      "M": "Absalom said to Hushai, 'Is this your loyalty to your friend? Why didn't you go with your friend?'",
      "T": "Absalom said: 'Is this how you show loyalty to your friend? Why did you not go with David?'"
    },
    "18": {
      "L": "And Hushai said to Absalom, 'No; but the one whom the LORD and this people and all the men of Israel have chosen—his I will be, and with him I will remain.'",
      "M": "Hushai said to Absalom, 'No—the one whom the LORD and this people and all Israel have chosen—to him I belong, and with him I will stay.'",
      "T": "Hushai said: 'No. The one the LORD has chosen—and this people, and all Israel—to him I belong. With him I stay.'"
    },
    "19": {
      "L": "'And again, whom should I serve? Should it not be his son? As I have served in your father's presence, so will I be in your presence.'",
      "M": "'Besides, whom should I serve? Should it not be his son? As I served your father, so I will serve you.'",
      "T": "'And who else should I serve but his son? As I served your father, so I will serve you.'"
    },
    "20": {
      "L": "Then Absalom said to Ahithophel, 'Give your counsel; what shall we do?'",
      "M": "Absalom said to Ahithophel, 'Give us your advice. What should we do?'",
      "T": "Absalom turned to Ahithophel: 'Give your counsel. What should we do?'"
    },
    "21": {
      "L": "Ahithophel said to Absalom, 'Go in to your father's concubines, whom he has left to keep the house. Then all Israel will hear that you have made yourself odious to your father, and the hands of all who are with you will be strengthened.'",
      "M": "Ahithophel said to Absalom, 'Go in to your father's concubines whom he left to keep the palace. All Israel will hear that you have made yourself repugnant to your father, and that will strengthen the resolve of all who are with you.'",
      "T": "Ahithophel said: 'Sleep with your father's concubines—the ones he left to keep the palace. All Israel will hear that you have become permanently estranged from your father. That will steel the nerves of everyone with you.'"
    },
    "22": {
      "L": "So they pitched a tent for Absalom on the roof, and Absalom went in to his father's concubines in the sight of all Israel.",
      "M": "So they set up a tent for Absalom on the roof, and Absalom went in to his father's concubines in the sight of all Israel.",
      "T": "They erected a tent for Absalom on the palace roof. In the sight of all Israel, Absalom went in to his father's concubines. The public violation was the point."
    },
    "23": {
      "L": "Now the counsel that Ahithophel gave in those days was as if one consulted the oracle of God; so was all the counsel of Ahithophel esteemed both by David and by Absalom.",
      "M": "In those days the counsel Ahithophel gave was treated as if one had sought God's own word; that was how both David and Absalom regarded all his counsel.",
      "T": "In those days Ahithophel's counsel was as authoritative as a word from God himself. That was how both David and Absalom had always treated it."
    }
  },
  "17": {
    "1": {
      "L": "Moreover, Ahithophel said to Absalom, 'Let me choose twelve thousand men, and I will arise and pursue David tonight.'",
      "M": "Ahithophel said to Absalom, 'Let me choose twelve thousand men and I will set out tonight to pursue David.'",
      "T": "Ahithophel said to Absalom: 'Give me twelve thousand men. I will go after David tonight.'"
    },
    "2": {
      "L": "'I will come upon him while he is weary and weak-handed, and throw him into a panic; and all the people who are with him will flee. I will strike down only the king,'",
      "M": "'I will come on him while he is weary and discouraged. I will throw him into a panic, and all his men will flee. Then I will strike down only the king—'",
      "T": "'He is weary and demoralized. I will fall on him, throw him into panic, scatter his men—and strike down the king alone.'"
    },
    "3": {
      "L": "'and I will bring all the people back to you as a bride returns to her husband. You seek the life of only one man; all the people will be at peace.'",
      "M": "'Then I will bring all the people back to you—as a bride comes home to her husband. You are after only one man's life; the rest of the people can be at peace.'",
      "T": "'Then I bring everyone back to you—like a bride returning to her husband. One man is all you need. The rest of the people will be unharmed.'"
    },
    "4": {
      "L": "This plan pleased Absalom and all the elders of Israel.",
      "M": "The proposal pleased Absalom and all the elders of Israel.",
      "T": "The plan pleased Absalom and every elder of Israel."
    },
    "5": {
      "L": "Then Absalom said, 'Call Hushai the Archite also, and let us hear what he has to say.'",
      "M": "Then Absalom said, 'Summon Hushai the Archite as well, and let us hear what he has to say.'",
      "T": "Then Absalom said: 'Call Hushai the Archite. Let us hear him too.'"
    },
    "6": {
      "L": "And when Hushai came to Absalom, Absalom said to him, 'Ahithophel has said this. Shall we act on his advice? If not, speak.'",
      "M": "When Hushai came to Absalom, Absalom said, 'Ahithophel has said this. Shall we follow his advice? If not, tell us.'",
      "T": "When Hushai arrived, Absalom told him what Ahithophel had proposed. 'Shall we act on it? What do you say?'"
    },
    "7": {
      "L": "And Hushai said to Absalom, 'The counsel that Ahithophel has given is not good this time.'",
      "M": "Hushai said to Absalom, 'The advice Ahithophel has given is not good this time.'",
      "T": "Hushai said: 'The counsel Ahithophel has given is wrong—this time it is wrong.'"
    },
    "8": {
      "L": "Hushai said, 'You know that your father and his men are warriors, and they are enraged in their minds, like a bear robbed of her cubs in the open country. And your father is an expert in war; he will not spend the night with the people.'",
      "M": "Hushai said, 'You know your father and his men—they are warriors, and now they are furious, like a bear robbed of her cubs in the field. Your father is a seasoned fighter; he will not stay with the troops overnight.'",
      "T": "'You know your father and his men. They are warriors, and right now they are like a bear who has lost her cubs in the open field—wild with rage. Your father has fought wars his whole life. He will not camp with the people.'"
    },
    "9": {
      "L": "'Even now he has hidden himself in one of the pits or in some other place. And when he attacks first, whoever hears of it will say, \"There has been a slaughter among the troops following Absalom.\"'",
      "M": "'Even now he is hiding in some cave or somewhere. And when he falls on your men first, whoever hears of it will say, \"There was a massacre among Absalom's forces.\"'",
      "T": "'Right now he has hidden somewhere—a pit, a cave, who knows. When he falls on your men first, and the news goes out—There was a slaughter among Absalom's troops—even the bravest hearts will crack.'"
    },
    "10": {
      "L": "'And even the valiant man, whose heart is like the heart of a lion, will melt with fear; for all Israel knows that your father is a mighty man, and those who are with him are valiant men.'",
      "M": "'And even the brave man with the heart of a lion will lose his nerve; for all Israel knows your father is a mighty warrior and that his men are bold fighters.'",
      "T": "'The bravest man—heart of a lion—will melt. All Israel knows who David is. They know his men. One ambush from him and the army dissolves.'"
    },
    "11": {
      "L": "'But I counsel that all Israel be gathered together to you, from Dan to Beersheba, as the sand by the sea in multitude, and that you go to battle in person.'",
      "M": "'My counsel is this: let all Israel be assembled to you, from Dan to Beersheba, as many as the sand by the sea, and that you go into battle in person.'",
      "T": "'My counsel: gather all Israel to yourself—from Dan to Beersheba, numberless as sand—and go into battle yourself.'"
    },
    "12": {
      "L": "'Then we will come upon him in whatever place he is found, and we will light on him as the dew falls on the ground; and of him and all the men with him, not one will be left.'",
      "M": "'We will come down on him wherever he is, like dew on the ground. Of him and all his men, not one will survive.'",
      "T": "'We will come on him in whatever place he is found—like dew falling everywhere at once. Not one of him or his men will be left.'"
    },
    "13": {
      "L": "'And if he withdraws into a city, then all Israel will bring ropes to that city, and we will drag it into the valley until not even a pebble is found there.'",
      "M": "'And if he retreats into a city, all Israel will bring ropes to that city and drag it into the valley, until not even a stone can be found there.'",
      "T": "'If he takes refuge in a city, all Israel will bring ropes and drag that city into the ravine—not a stone will be left.'"
    },
    "14": {
      "L": "And Absalom and all the men of Israel said, 'The counsel of Hushai the Archite is better than the counsel of Ahithophel.' For the LORD had ordained to defeat the good counsel of Ahithophel, in order that the LORD might bring disaster upon Absalom.",
      "M": "Absalom and all the Israelites said, 'The counsel of Hushai the Archite is better than Ahithophel's counsel.' For the LORD had determined to frustrate Ahithophel's sound advice, in order to bring disaster on Absalom.",
      "T": "Absalom and all the men of Israel said: 'The counsel of Hushai is better.' But it was the LORD who had ordained it—the LORD had decided to frustrate Ahithophel's advice, which was genuinely good, because the LORD intended disaster for Absalom."
    },
    "15": {
      "L": "Then Hushai said to the priests Zadok and Abiathar, 'This is what Ahithophel counseled Absalom and the elders of Israel, and this is what I counseled.'",
      "M": "Hushai told the priests Zadok and Abiathar, 'Ahithophel counseled Absalom and the elders of Israel in this and this way, and I countered with this and that.'",
      "T": "Hushai went at once to Zadok and Abiathar: 'Ahithophel counseled this. I countered with that. Here is what was said.'"
    },
    "16": {
      "L": "'Now therefore send quickly and tell David, \"Do not spend the night at the crossing places of the wilderness, but by all means cross over, lest the king and all the people with him be swallowed up.\"'",
      "M": "'Now send quickly and tell David: do not spend the night at the wilderness crossings—cross the Jordan at once, or the king and everyone with him will be destroyed.'",
      "T": "'Send word to David immediately: Do not spend the night at the desert ford. Cross the Jordan now—or the king and everyone with him will be swallowed up.'"
    },
    "17": {
      "L": "Now Jonathan and Ahimaaz were staying at En-rogel; and a female servant was to go and tell them, and they would go and tell King David; for they could not be seen entering the city.",
      "M": "Jonathan and Ahimaaz were waiting at En-rogel; a servant girl would go and inform them, and they would go on to tell King David, since they could not risk being seen entering the city.",
      "T": "Jonathan and Ahimaaz were waiting at En-rogel. A servant girl would carry word to them; they would carry it to David. They could not be seen going into the city."
    },
    "18": {
      "L": "But a young man saw them and told Absalom. So both of them went away quickly and came to the house of a man in Bahurim who had a well in his courtyard; and they went down into it.",
      "M": "But a young man saw them and informed Absalom. So they went quickly and came to the house of a man in Bahurim who had a well in his courtyard. They climbed down into it.",
      "T": "But a young man saw them and reported to Absalom. The two of them ran—to Bahurim, to the house of a man who had a well in his courtyard. They went down into it."
    },
    "19": {
      "L": "And the woman took a covering and spread it over the mouth of the well and scattered ground grain on it, so the thing was not known.",
      "M": "The man's wife took a covering and spread it over the well's mouth, scattering ground grain over it, so that nothing was discovered.",
      "T": "The woman of the house spread a covering over the well's mouth and scattered grain on top. Nothing was seen."
    },
    "20": {
      "L": "When Absalom's servants came to the woman at the house, they said, 'Where are Ahimaaz and Jonathan?' And the woman said to them, 'They have crossed over the brook of water.' And when they had searched and could not find them, they returned to Jerusalem.",
      "M": "When Absalom's servants came to the woman and asked, 'Where are Ahimaaz and Jonathan?' the woman said, 'They have crossed the brook.' They searched but could not find them, and returned to Jerusalem.",
      "T": "Absalom's men came to the woman: 'Where are Ahimaaz and Jonathan?' She said: 'They crossed the stream.' They searched. They found nothing. They returned to Jerusalem."
    },
    "21": {
      "L": "After they had gone, the men came up out of the well and went and told King David. They said to David, 'Arise and cross the water quickly; for this is what Ahithophel has counseled against you.'",
      "M": "After they left, the men climbed up out of the well and went and told King David. They said, 'Arise and cross the water quickly—this is what Ahithophel has advised against you.'",
      "T": "When the coast was clear they climbed out of the well, went to David, and told him: 'Get up. Cross the water now. This is what Ahithophel has planned against you.'"
    },
    "22": {
      "L": "Then David arose, and all the people with him, and they crossed the Jordan. By daybreak not one of them had failed to cross the Jordan.",
      "M": "David and all his men arose and crossed the Jordan. By daybreak not a single person was left who had not crossed over.",
      "T": "David rose. All his people rose. They crossed the Jordan. By dawn there was not one left on the near bank."
    },
    "23": {
      "L": "When Ahithophel saw that his counsel was not followed, he saddled his donkey and went home to his own city. He put his house in order and hanged himself, and he died and was buried in the tomb of his father.",
      "M": "When Ahithophel saw that his advice had not been taken, he saddled his donkey and rode home to his own city. He set his household in order and hanged himself. He died and was buried in his father's tomb.",
      "T": "When Ahithophel saw that his counsel had been rejected, he saddled his donkey and went home to his city. He put his household in order—the last act of a man who knew his life was finished—and hanged himself. He died and was buried in his father's tomb. His counsel had been sound; it was rejected anyway. That was more than he could bear."
    },
    "24": {
      "L": "Then David came to Mahanaim, and Absalom crossed the Jordan, he and all the men of Israel with him.",
      "M": "David arrived at Mahanaim, while Absalom crossed the Jordan with all the men of Israel.",
      "T": "David reached Mahanaim. Absalom crossed the Jordan with all Israel behind him."
    },
    "25": {
      "L": "Now Absalom had set Amasa over the army instead of Joab. Amasa was the son of a man named Ithra the Israelite, who had gone in to Abigail the daughter of Nahash, sister of Zeruiah, Joab's mother.",
      "M": "Absalom had put Amasa in command of the army in place of Joab. Amasa was the son of a man named Ithra the Israelite, who had married Abigail daughter of Nahash, the sister of Zeruiah, Joab's mother.",
      "T": "Absalom had given Amasa command of the army in place of Joab. Amasa was the son of Ithra the Israelite, who had married Abigail daughter of Nahash—the sister of Zeruiah, Joab's mother. A family connection: David's nephew commanding against David."
    },
    "26": {
      "L": "And Israel and Absalom encamped in the land of Gilead.",
      "M": "Israel and Absalom camped in the land of Gilead.",
      "T": "Israel and Absalom camped in Gilead."
    },
    "27": {
      "L": "When David came to Mahanaim, Shobi the son of Nahash from Rabbah of the Ammonites, and Machir the son of Ammiel from Lo-debar, and Barzillai the Gileadite from Rogelim,",
      "M": "When David arrived at Mahanaim, Shobi son of Nahash from Rabbah of the Ammonites, and Machir son of Ammiel from Lo-debar, and Barzillai the Gileadite from Rogelim,",
      "T": "When David arrived at Mahanaim, three men came to meet him: Shobi son of Nahash from Rabbah of the Ammonites, Machir son of Ammiel from Lo-debar, and Barzillai the Gileadite from Rogelim."
    },
    "28": {
      "L": "brought beds and basins and earthen vessels and wheat and barley and flour and parched grain and beans and lentils and honey,",
      "M": "brought beds, basins, and clay vessels, along with wheat, barley, flour, roasted grain, beans, lentils, honey,",
      "T": "They brought beds, basins, clay pots, wheat, barley, flour, parched grain, beans, lentils, honey—"
    },
    "29": {
      "L": "and curds and sheep and cheese from the herd, for David and for the people with him to eat; for they said, 'The people are hungry and weary and thirsty in the wilderness.'",
      "M": "and curds, sheep, and cheese, for David and his men to eat. They said, 'The people are hungry and weary and thirsty in the wilderness.'",
      "T": "—and curds and sheep and cheese. 'The people are hungry, exhausted, and thirsty in the wilderness,' they said. So they fed them."
    }
  },
  "18": {
    "1": {
      "L": "And David mustered the people who were with him and set commanders of thousands and commanders of hundreds over them.",
      "M": "David mustered the troops with him and appointed commanders of thousands and commanders of hundreds.",
      "T": "David counted his men and organized them—commanders of thousands, commanders of hundreds."
    },
    "2": {
      "L": "And David sent out the army, a third under the command of Joab and a third under the command of Abishai the son of Zeruiah, Joab's brother, and a third under the command of Ittai the Gittite. The king said to the troops, 'I myself will also go out with you.'",
      "M": "David sent out the army in three divisions—one under Joab, one under Abishai son of Zeruiah, Joab's brother, and one under Ittai the Gittite. The king said to the troops, 'I will march out with you.'",
      "T": "He sent the army out in three columns: one under Joab, one under Abishai son of Zeruiah, one under Ittai the Gittite. The king said: 'I will march with you.'"
    },
    "3": {
      "L": "But the troops said, 'You shall not go out. For if we flee, they will not care about us; if half of us die, they will not care about us. But you are worth ten thousand of us; therefore it is better that you stay in the city and give us support.'",
      "M": "But the troops said, 'You must not go out. If we flee, they won't care. If half of us die, they won't care. But you are worth ten thousand of us—so it is better for you to stay in the city and send us support from there.'",
      "T": "But the men said: 'You must not come. If we run, they will not pursue us—only you. If half of us die, no one will care—only you matter. You are worth ten thousand of us. Stay in the city and support us from there.'"
    },
    "4": {
      "L": "The king said to them, 'Whatever seems best to you I will do.' So the king stood at the side of the gate, while all the army marched out by hundreds and by thousands.",
      "M": "The king said, 'I will do whatever you think is best.' So he stood at the side of the gate while all the troops marched out by hundreds and by thousands.",
      "T": "The king said: 'I will do what seems best to you.' He stood by the gate and watched them march out—hundreds, then thousands."
    },
    "5": {
      "L": "The king commanded Joab and Abishai and Ittai, saying, 'Deal gently for my sake with the young man Absalom.' And all the people heard when the king gave all the commanders orders about Absalom.",
      "M": "The king commanded Joab, Abishai, and Ittai: 'Deal gently with the young man Absalom, for my sake.' All the troops heard the king give his commanders this order about Absalom.",
      "T": "'Deal gently with the young man Absalom—for my sake.' The king said it to Joab, to Abishai, to Ittai—and all the people heard. For my sake. They all heard it."
    },
    "6": {
      "L": "So the army went out into the field against Israel, and the battle took place in the forest of Ephraim.",
      "M": "The army marched out into the field against Israel, and the battle was fought in the forest of Ephraim.",
      "T": "The army marched out to meet Israel. The battle was fought in the forest of Ephraim."
    },
    "7": {
      "L": "And the men of Israel were defeated there before the servants of David, and the slaughter there was great on that day—twenty thousand men.",
      "M": "The Israelites were defeated by David's men, and the slaughter that day was massive—twenty thousand men.",
      "T": "Israel was routed by David's men. Twenty thousand fell that day. The defeat was catastrophic."
    },
    "8": {
      "L": "The battle spread over the face of all the country, and the forest devoured more people that day than the sword devoured.",
      "M": "The battle ranged over the whole countryside, and the forest took more lives that day than the sword.",
      "T": "The fighting scattered across the whole country—and the forest swallowed more men that day than the sword did. The wilderness that David had fled into became Absalom's executioner."
    },
    "9": {
      "L": "And Absalom happened to meet the servants of David. Absalom was riding on his mule, and the mule went under the thick branches of a great oak. His head caught in the oak, and he was left hanging between heaven and earth, while the mule that was under him went on.",
      "M": "Absalom happened to come across some of David's men. He was riding a mule, and the mule went under the dense branches of a great oak. His head became caught in the oak, and he was left hanging in midair while the mule continued on without him.",
      "T": "Absalom came across David's men while riding a mule. The mule went under a great oak—and Absalom's head caught in the branches. The mule kept going. Absalom hung there between heaven and earth."
    },
    "10": {
      "L": "A man saw it and told Joab, 'I saw Absalom hanging in an oak.'",
      "M": "A man saw it and told Joab, 'I just saw Absalom hanging in an oak tree.'",
      "T": "A soldier saw it and reported to Joab: 'I just saw Absalom—hanging in an oak.'"
    },
    "11": {
      "L": "Joab said to the man who told him, 'And behold, you saw him! Why then did you not strike him there to the ground? I would have given you ten pieces of silver and a belt.'",
      "M": "Joab said to the man, 'You saw him! Why didn't you strike him down on the spot? I would have given you ten pieces of silver and a belt.'",
      "T": "Joab said: 'You saw him and did nothing? I would have given you ten pieces of silver and a belt for killing him.'"
    },
    "12": {
      "L": "The man said to Joab, 'Even if I received a thousand pieces of silver in my hand, I would not reach out my hand against the king's son; for in our hearing the king charged you and Abishai and Ittai, \"Guard the young man Absalom for my sake.\"'",
      "M": "The man said to Joab, 'Even if a thousand pieces of silver were weighed out in my hand, I would not raise my hand against the king's son—for we all heard the king charge you and Abishai and Ittai: Protect the young man Absalom for my sake.'",
      "T": "The man said: 'A thousand pieces of silver would not make me raise my hand against the king's son. We all heard it—we all heard the king tell you and Abishai and Ittai: Protect the young man Absalom, for my sake.'"
    },
    "13": {
      "L": "'Otherwise, if I had dealt treacherously against his life—and there is nothing hidden from the king—then you yourself would have stood aloof.'",
      "M": "'And if I had acted treacherously against his life—and nothing is hidden from the king—you yourself would have kept your distance.'",
      "T": "'And if I had done it—taken his life in defiance of the king's direct order—do you think you would have stood by me? Nothing is hidden from the king. You would have left me to answer for it alone.'"
    },
    "14": {
      "L": "Joab said, 'I will not waste time like this with you.' He took three darts in his hand and thrust them into the heart of Absalom while he was still alive in the oak.",
      "M": "Joab said, 'I'm not going to stand here arguing with you.' He took three javelins in his hand and drove them into Absalom's chest while he was still alive in the tree.",
      "T": "Joab said: 'I will not waste more words with you.' He took three darts and drove them into Absalom's chest—still alive, still hanging in the tree."
    },
    "15": {
      "L": "And ten young men who carried Joab's armor surrounded Absalom and struck him and killed him.",
      "M": "Then ten of Joab's armor-bearers surrounded Absalom and finished him off.",
      "T": "Ten of Joab's armor-bearers closed in around Absalom and struck him until he was dead."
    },
    "16": {
      "L": "Then Joab blew the trumpet, and the troops came back from pursuing Israel, for Joab held back the troops.",
      "M": "Joab blew the trumpet, and the troops turned back from pursuing Israel, for Joab called a halt.",
      "T": "Joab blew the ram's horn. The troops turned back from pursuing Israel. Joab stopped the chase."
    },
    "17": {
      "L": "They took Absalom and threw him into a great pit in the forest, and raised over him a very great heap of stones. And all Israel fled, each to his own home.",
      "M": "They took Absalom and threw him into a large pit in the forest, and heaped a great mound of stones over him. All the Israelites fled to their own homes.",
      "T": "They took Absalom's body and threw it into a great pit in the forest and heaped a massive pile of stones over him. All Israel scattered, each man to his own home."
    },
    "18": {
      "L": "Now Absalom in his lifetime had taken and set up for himself the pillar that is in the King's Valley, for he said, 'I have no son to keep my name in remembrance.' He named the pillar after himself, and it is called Absalom's Monument to this day.",
      "M": "During his lifetime Absalom had taken and erected for himself the pillar that stands in the King's Valley, for he said, 'I have no son to preserve my name.' He named the pillar after himself, and it is called Absalom's Monument to this day.",
      "T": "Absalom had erected a pillar for himself in the King's Valley while he was still alive. 'I have no son to carry my name,' he had said—so he built the monument himself. He named it after himself. It is called Absalom's Monument to this day. The monument outlasted its builder by a few hours."
    },
    "19": {
      "L": "Then Ahimaaz the son of Zadok said, 'Let me run and carry the tidings to the king, how that the LORD has vindicated him against his enemies.'",
      "M": "Then Ahimaaz son of Zadok said, 'Let me run and bring the king the news—how the LORD has delivered him from his enemies.'",
      "T": "Ahimaaz son of Zadok said: 'Let me run and bring the king the news—how the LORD has delivered him from his enemies.'"
    },
    "20": {
      "L": "Joab said to him, 'You are not to carry the tidings today. You may carry tidings another day, but today you shall carry no tidings, because the king's son is dead.'",
      "M": "Joab said to him, 'You are not to bring tidings today. You may bring tidings another day, but not today—the king's son is dead.'",
      "T": "Joab said: 'Not today. Another day you may carry news—but not today. The king's son is dead.'"
    },
    "21": {
      "L": "Then Joab said to the Cushite, 'Go, tell the king what you have seen.' The Cushite bowed to Joab and ran.",
      "M": "Joab said to a Cushite, 'Go, tell the king what you have seen.' The Cushite bowed before Joab and ran.",
      "T": "Then Joab said to the Cushite: 'Go—tell the king what you have seen.' The Cushite bowed and ran."
    },
    "22": {
      "L": "Then Ahimaaz the son of Zadok said again to Joab, 'Come what may, please let me also run after the Cushite.' And Joab said, 'Why will you run, my son, since you have no reward for the tidings?'",
      "M": "Ahimaaz son of Zadok said again to Joab, 'Whatever happens, please let me run after the Cushite.' Joab said, 'Why do you want to run, my son? You have no good news to bring.'",
      "T": "Ahimaaz said to Joab again: 'Let me run after the Cushite—whatever comes of it.' Joab said: 'Why run, son? There is no reward waiting for you in this news.'"
    },
    "23": {
      "L": "'But come what may, let me run.' And he said to him, 'Run.' Then Ahimaaz ran by the way of the plain and outran the Cushite.",
      "M": "'But come what may, I want to run.' 'Then run,' Joab said. And Ahimaaz ran by the way of the plain and outran the Cushite.",
      "T": "'Whatever comes—let me run.' 'Run then,' said Joab. Ahimaaz took the plain road and outran the Cushite."
    },
    "24": {
      "L": "Now David was sitting between the two gates. And the watchman went up to the roof of the gate over the wall, and when he lifted up his eyes and looked, he saw a man running alone.",
      "M": "David was sitting between the two gates. The watchman climbed to the roof of the gate by the wall, looked up, and saw a man running alone.",
      "T": "David sat between the two gates. The watchman had gone up to the roof above the gate wall. He looked out and saw a man running—alone."
    },
    "25": {
      "L": "The watchman called out and told the king. The king said, 'If he is alone, there is tidings in his mouth.' And he came on and drew near.",
      "M": "The watchman called out and told the king. The king said, 'If he is alone, he brings news.' The man kept coming, drawing closer.",
      "T": "The watchman called down to the king. The king said: 'If he is alone, he carries news.' The runner kept coming."
    },
    "26": {
      "L": "Then the watchman saw another man running, and the watchman called to the gatekeeper, 'See, another man running alone.' The king said, 'He also brings tidings.'",
      "M": "Then the watchman saw another man running and called to the gatekeeper, 'Look—another man running alone!' The king said, 'He brings news too.'",
      "T": "The watchman saw a second man running and called to the porter: 'Another man, running alone.' The king said: 'He brings news too.'"
    },
    "27": {
      "L": "The watchman said, 'I think the running of the first one is like the running of Ahimaaz the son of Zadok.' The king said, 'He is a good man and comes with good tidings.'",
      "M": "The watchman said, 'The running of the first one looks like the running of Ahimaaz son of Zadok.' The king said, 'He is a good man and will come with good news.'",
      "T": "The watchman said: 'The running of the first one looks like Ahimaaz son of Zadok.' The king said: 'He is a good man. He will bring good news.'"
    },
    "28": {
      "L": "Then Ahimaaz called out to the king, 'All is well!' And he bowed before the king with his face to the ground and said, 'Blessed be the LORD your God, who has delivered up the men who raised their hand against my lord the king!'",
      "M": "Ahimaaz called out to the king, 'All is well!' He bowed before the king with his face to the ground and said, 'Blessed be the LORD your God, who has delivered up those who rebelled against my lord the king!'",
      "T": "Ahimaaz cried out: 'All is well!' He bowed with his face to the ground before the king. 'Blessed be the LORD your God,' he said, 'who has delivered up the men who raised their hand against my lord the king!'"
    },
    "29": {
      "L": "The king said, 'Is it well with the young man Absalom?' And Ahimaaz answered, 'When Joab sent your servant, I saw a great tumult but did not know what it was.'",
      "M": "The king said, 'Is the young man Absalom all right?' Ahimaaz answered, 'When Joab sent me, I saw a great commotion but did not know what it was.'",
      "T": "The king said: 'Is the young man Absalom safe?' Ahimaaz said: 'When Joab sent me I saw a great disturbance—but I did not know what it was.'"
    },
    "30": {
      "L": "The king said, 'Turn aside and stand here.' So he turned aside and stood still.",
      "M": "The king said, 'Step aside and stand over there.' He stepped aside and stood there.",
      "T": "The king said: 'Step aside. Stand there.' He stepped aside and stood still."
    },
    "31": {
      "L": "And behold, the Cushite came, and the Cushite said, 'Good tidings for my lord the king! For the LORD has delivered you today from all those who rose up against you.'",
      "M": "Then the Cushite arrived and said, 'Good news for my lord the king! The LORD has given you justice today against all who rose up against you.'",
      "T": "Then the Cushite came. 'Good news, my lord the king! The LORD has delivered you today from all who rose against you.'"
    },
    "32": {
      "L": "The king said to the Cushite, 'Is it well with the young man Absalom?' The Cushite answered, 'May the enemies of my lord the king, and all who rise up against you to do you evil, be as that young man is.'",
      "M": "The king said to the Cushite, 'Is the young man Absalom all right?' The Cushite answered, 'May the enemies of my lord the king, and all who rise against you for evil, be like that young man.'",
      "T": "The king said: 'Is the young man Absalom safe?' The Cushite answered: 'May all the enemies of my lord the king, all who rise against you to do you harm—may they be as that young man is.'"
    },
    "33": {
      "L": "The king was shaken and went up to the chamber over the gate and wept. And as he went, he said: 'O my son Absalom! My son, my son Absalom! Would I had died instead of you, O Absalom, my son, my son!'",
      "M": "The king was deeply shaken and went up to the chamber above the gate and wept. As he went, he said: 'O my son Absalom! My son, my son Absalom! If only I had died instead of you—O Absalom, my son, my son!'",
      "T": "The king staggered. He went up to the chamber above the gate and wept.\nMy son Absalom—\nmy son, my son Absalom!\nWould I had died instead of you—\nO Absalom, my son,\nmy son!"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '2samuel', existing)
    print('2 Samuel 13–18 written.')

if __name__ == '__main__':
    main()
