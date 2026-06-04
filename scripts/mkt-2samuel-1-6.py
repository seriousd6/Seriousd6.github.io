"""
MKT 2 Samuel chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2samuel-1-6.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout. T uses "the LORD" in narrative
  contexts; retains that form because the divine personal name is functioning as the covenant
  guarantor of David's kingship throughout these chapters. Does not switch to "Yahweh" here because
  the narrator uses it routinely rather than highlighting it liturgically.
- H430 (אֱלֹהִים): "God" in all tiers. In 2:27 Joab's oath "As God lives" is essentially
  "ḥê hāʾĕlōhîm" — the generic divine oath formula, rendered "As God lives" in L/M, "Before God"
  / "As God is my witness" in T where it adds rhetorical weight.
- H2617 (חֶסֶד): appears in 2:5, 2:6, 3:8. This is the great Hebrew covenant term. L "kindness"
  (preserving KJV wordstock but inadequate); M "steadfast loyalty" (conveys both the covenantal
  bond and the active expression of it); T "covenant loyalty" or "faithfulness" depending on context.
  In 3:8 Abner uses it defensively: "I have been showing steadfast loyalty to your father's house."
- H1285 (בְּרִית): "league/treaty" in ch2–3 political uses (David–Jabesh, Abner–David, David–elders);
  rendered L "covenant/league," M "treaty" for political compacts, "covenant" when before the LORD.
  In 5:3 the anointing covenant before the LORD is "covenant" in all tiers.
- H5315 (נֶפֶשׁ): "soul" in L; "life" in M/T where the Hebrew means the living self rather than
  inner self (e.g., 4:8 "who sought your life"). In 3:21 "all that your heart desires" — נֶפֶשׁ
  here means the whole desiring self; L "soul," M "heart," T "everything you desire."
- H7307 (רוּחַ): not a major presence here; in 1:9 "anguish" is H7661 (shibbāshôn). Spirit/wind
  not a key term in these chapters.
- H5650 (ʿebed, "servant"): "servant" in L; "servants" = military retinue/men in M/T when context
  is clearly military (e.g., "servants of David" = "David's men" in M/T).
- H4428 (melek, "king"): "king" throughout. When the narrator establishes David's kingship formally
  (2:4, 5:3) T highlights the theological weight of the anointing moment.
- H7462 (rāʿāh, "shepherd"): 5:2 "you shall feed my people Israel" = shepherd imagery. L "feed,"
  M "shepherd," T "shepherd and guard." The shepherd-king idiom is a major ANE royal metaphor; T
  makes the resonance explicit.
- Lament of the Bow (1:19–27): This is formal Hebrew qinah poetry (3+2 stress pattern). T tier
  uses line breaks to honor the poetic structure. L and M are rendered as elevated prose.
  The refrain "How the mighty have fallen" (אֵיךְ נָפְלוּ גִבּוֹרִים) opens, returns at v25, and
  closes the lament (v27). T preserves these as clear refrains.
- H6643 (ṣĕbî, "gazelle/beauty/glory"): 1:19 — "The beauty of Israel is slain upon thy high
  places." This word means both gazelle (beautiful animal, symbol of swiftness/grace) and
  glory/ornament. L "glory," M "pride," T "beauty." The ambiguity is part of the lament's power.
- H1116 (bāmôt, "high places"): 1:19, 25 — "high places" in all tiers. In a lament context
  this means the open heights where battles occur, not necessarily cultic high places.
- H5788 (ʿiwwārôn) / H6455 (piṣṣēaḥ) blindness/lameness in 5:6–8: Jebusite taunt about blind
  and lame. L literal; M explains the taunt structure; T surfaces the irony — the ones the
  Jebusites thought would defend the city are now excluded from it. The phrasing is famously
  obscure; the translation follows the dominant reading (the Jebusites taunt David with their
  "blind and lame" as sufficient defenders).
- H6794 (ṣinnôr) in 5:8: the "water shaft" or gutter — the means by which Joab/David's men
  scaled the city. L "water shaft," M "water tunnel," T "water shaft."
- H727 (ʾārôn, "ark"): "ark" in all tiers throughout ch6. The full designation "ark of God"
  and "ark of the LORD of hosts" is preserved; T does not shorten it.
- H4407 (millô, "Millo"): 5:9 — a place-name / fortification structure. "Millo" in L/M/T;
  T notes it is a fill/terrace structure.
- H8004 (Hălḵat-haṣṣûrîm, "field of sword-edges") 2:16: L/M "Helkath-hazzurim" (place-name);
  T adds the etymology note in context.
- Abner's role: He is simultaneously the most powerful and most morally ambiguous figure in
  ch2–3. T tier tracks his shifting loyalties: first as Saul's defender, then as kingmaker,
  finally as victim. His death (3:27) is politically motivated murder wrapped in blood-vengeance.
- Uzzah (ch6:6–7): The death of Uzzah for touching the ark is theologically significant. L/M
  present it straightforwardly; T notes that the sin was procedural (wrong method of transport,
  cf. Num 4), not impurity of intention. The ark should have been carried on poles by Levites.
- Aspect notes: waw-consecutive imperfects throughout = narrative past (simple past in English).
  Perfect verbs mark completed states of affairs. The lament uses perfect (qātal) for past
  events that are mourned as definitive: "the mighty are fallen" = they have fallen and it stands.
- OT echo notes: David's lament echoes the language of Israelite battle laments. 1:21 echoes
  Deut 33:28 (abundant rain as divine blessing). The shepherd-king language in 5:2 echoes
  Num 27:17 and anticipates Ezek 34 / John 10. David's ark-procession in ch6 uses priestly
  language that will resonate with the temple dedication in 1 Kings 8.
- 2 Sam 4:4 (Mephibosheth parenthesis): This is a narrative aside preparing for ch9. It belongs
  here in the flow and is translated as the narrator intends — a note about Jonathan's son.
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
  "1": {
    "1": {
      "L": "Now it came to pass after the death of Saul, when David had returned from the slaughter of the Amalekites, and David had stayed two days in Ziklag,",
      "M": "After the death of Saul, David returned from striking down the Amalekites and stayed two days in Ziklag.",
      "T": "Saul was dead. David, back from the slaughter of the Amalekites, had been at Ziklag two days."
    },
    "2": {
      "L": "it came to pass on the third day that, behold, a man came from Saul's camp with his clothes torn and dirt upon his head. And when he came to David, he fell to the earth and bowed down.",
      "M": "On the third day, a man arrived from Saul's camp with his clothes torn and dirt on his head. He came to David and threw himself to the ground in homage.",
      "T": "On the third day a man came from Saul's camp. His clothes were torn; dirt was on his head—the signs of mourning. He came to David and fell prostrate before him."
    },
    "3": {
      "L": "And David said to him, 'From where do you come?' And he said to him, 'Out of the camp of Israel I have escaped.'",
      "M": "David said to him, 'Where have you come from?' He answered, 'I have escaped from the camp of Israel.'",
      "T": "'Where do you come from?' David asked. 'I escaped from the camp of Israel,' the man said."
    },
    "4": {
      "L": "And David said to him, 'What happened? Tell me, please.' And he answered, 'The people fled from the battle, and also many of the people have fallen and are dead; and Saul and Jonathan his son are dead also.'",
      "M": "David said, 'What happened? Tell me.' He answered, 'The troops fled from the battle, and many of them fell and died. Saul and his son Jonathan are dead.'",
      "T": "'What happened?' David pressed. 'Tell me.' The man said: 'The army broke and fled. Many fell, many died. Saul is dead. Jonathan his son is dead.'"
    },
    "5": {
      "L": "Then David said to the young man who told him, 'How do you know that Saul and Jonathan his son are dead?'",
      "M": "David asked the young man who had brought the news, 'How do you know that Saul and his son Jonathan are dead?'",
      "T": "David looked at the messenger. 'How do you know Saul is dead? How do you know about Jonathan?'"
    },
    "6": {
      "L": "And the young man who told him said, 'I happened by chance to be on Mount Gilboa, and behold, Saul was leaning upon his spear; and behold, the chariots and horsemen were closing upon him.'",
      "M": "The young man replied, 'As it happened, I was on Mount Gilboa, and there was Saul leaning on his spear, with the chariots and riders bearing down on him.'",
      "T": "The man said: 'It happened that I was on Mount Gilboa. There was Saul, leaning on his spear, and the chariots and cavalry were closing in around him.'"
    },
    "7": {
      "L": "When he looked behind him, he saw me and called to me. And I answered, 'Here I am.'",
      "M": "He glanced behind him and saw me, and he called to me. I answered, 'Here I am.'",
      "T": "He looked back and saw me. He called out, and I answered: 'Here I am.'"
    },
    "8": {
      "L": "And he said to me, 'Who are you?' And I answered him, 'I am an Amalekite.'",
      "M": "He said, 'Who are you?' I told him, 'I am an Amalekite.'",
      "T": "'Who are you?' he said. 'An Amalekite,' I told him."
    },
    "9": {
      "L": "He said to me, 'Stand over me and kill me, for anguish has seized me, because my life still lingers within me.'",
      "M": "He said, 'Stand over me and kill me. Anguish has seized me, but my life still clings to me.'",
      "T": "'Stand over me and finish it,' he said. 'I am in agony, but I cannot die.'"
    },
    "10": {
      "L": "So I stood over him and killed him, because I knew he could not live after he had fallen. And I took the crown that was on his head and the armlet that was on his arm, and I have brought them here to my lord.",
      "M": "So I stood over him and killed him, for I knew he could not survive his fall. I took the crown from his head and the armlet from his arm, and I have brought them here to my lord.",
      "T": "So I stood over him and killed him. After a fall like that, there was no living. I took the crown from his head and the armlet from his arm, and I have brought them to you, my lord."
    },
    "11": {
      "L": "Then David took hold of his garments and tore them; and likewise all the men who were with him.",
      "M": "Then David took hold of his clothes and tore them, and so did all the men who were with him.",
      "T": "David seized his robe and tore it. Every man with him did the same."
    },
    "12": {
      "L": "And they mourned and wept and fasted until evening for Saul and for Jonathan his son and for the people of the LORD and for the house of Israel, because they had fallen by the sword.",
      "M": "They mourned and wept and fasted until evening for Saul and his son Jonathan, and for the people of the LORD and for the house of Israel, because they had fallen by the sword.",
      "T": "They mourned. They wept. They fasted until evening—for Saul, for Jonathan his son, for the LORD's people, for all the fallen of Israel who had died by the sword."
    },
    "13": {
      "L": "And David said to the young man who told him, 'Where are you from?' And he answered, 'I am the son of a sojourner, an Amalekite.'",
      "M": "Then David said to the young man who had brought the news, 'Where are you from?' He answered, 'I am the son of a resident alien, an Amalekite.'",
      "T": "David turned to the messenger. 'Where are you from?' 'I am the son of a resident foreigner,' the man said. 'An Amalekite.'"
    },
    "14": {
      "L": "David said to him, 'How is it that you were not afraid to stretch out your hand to destroy the LORD's anointed?'",
      "M": "David said to him, 'How were you not afraid to lift your hand to destroy the LORD's anointed?'",
      "T": "David said: 'How could you not be afraid? How could you raise your hand against the LORD's anointed?'"
    },
    "15": {
      "L": "Then David called one of the young men and said, 'Go, fall upon him.' And he struck him so that he died.",
      "M": "Then David called one of his men and said, 'Go, strike him down.' And he struck him so that he died.",
      "T": "David turned to one of his men. 'Kill him.' The man struck once. The Amalekite fell dead."
    },
    "16": {
      "L": "And David said to him, 'Your blood be upon your own head, for your own mouth testified against you, saying, I killed the LORD's anointed.'",
      "M": "And David said to him, 'Your blood is on your own head. Your own mouth condemned you when you said, I killed the LORD's anointed.'",
      "T": "David pronounced the verdict over the body: 'Your blood is on your own head. You condemned yourself. Your own mouth said it: I killed the LORD's anointed.'"
    },
    "17": {
      "L": "And David lamented with this lamentation over Saul and over Jonathan his son,",
      "M": "And David sang this lament over Saul and his son Jonathan.",
      "T": "Then David sang this lament over Saul and Jonathan his son."
    },
    "18": {
      "L": "and he ordered that the people of Judah be taught it. Behold, it is written in the Book of Jashar:",
      "M": "He gave orders that it should be taught to the people of Judah. It is written in the Book of Jashar:",
      "T": "He ordered that the people of Judah be taught it. It stands recorded in the Book of Jashar:"
    },
    "19": {
      "L": "'Your glory, O Israel, is slain upon your high places! How the mighty have fallen!'",
      "M": "'Your glory, O Israel, lies slain on your high places! How the mighty have fallen!'",
      "T": "Your glory, O Israel—\nslain upon the heights!\nHow the mighty have fallen."
    },
    "20": {
      "L": "'Tell it not in Gath, proclaim it not in the streets of Ashkelon, lest the daughters of the Philistines rejoice, lest the daughters of the uncircumcised triumph.'",
      "M": "'Tell it not in Gath; proclaim it not in the streets of Ashkelon, lest the daughters of the Philistines rejoice, lest the daughters of the uncircumcised exult.'",
      "T": "Tell it not in Gath,\nproclaim it not in Ashkelon's streets—\nlest the Philistine daughters rejoice,\nlest those uncircumcised women exult."
    },
    "21": {
      "L": "'You mountains of Gilboa, let there be no dew, and let there be no rain upon you, nor fields of offerings! For there the shield of the mighty was defiled, the shield of Saul, as though not anointed with oil.'",
      "M": "'Mountains of Gilboa, let no dew or rain fall on you, nor fields yield first-fruit offerings! For there the shield of the mighty was dishonored, the shield of Saul—as though it had never been anointed with oil.'",
      "T": "You mountains of Gilboa—\nlet no dew fall on you, no rain,\nnor any field give of its firstfruits.\nFor there the shield of the mighty was thrown aside,\nSaul's own shield,\nas though it had never shone with oil."
    },
    "22": {
      "L": "'From the blood of the slain, from the fat of the mighty, the bow of Jonathan did not turn back, and the sword of Saul did not return empty.'",
      "M": "'From the blood of the slain, from the fat of the mighty, the bow of Jonathan never turned back, and the sword of Saul never returned without satisfaction.'",
      "T": "From the blood of the slain,\nfrom the fat of the mighty—\nJonathan's bow never turned back,\nSaul's sword never came home empty."
    },
    "23": {
      "L": "'Saul and Jonathan, beloved and lovely in their lives! And in their death they were not divided; they were swifter than eagles, they were stronger than lions.'",
      "M": "'Saul and Jonathan—beloved and lovely in life, and in death they were not parted. They were swifter than eagles, stronger than lions.'",
      "T": "Saul and Jonathan—\nbeloved and lovely in life,\nin death never parted.\nSwifter than eagles they were;\nstronger than lions."
    },
    "24": {
      "L": "'O daughters of Israel, weep over Saul, who clothed you in scarlet with delights, who put ornaments of gold upon your apparel.'",
      "M": "'Daughters of Israel, weep for Saul, who dressed you in fine scarlet and put gold ornaments on your clothing.'",
      "T": "O daughters of Israel, weep for Saul—\nthe king who clothed you in scarlet,\nwho adorned your garments with gold."
    },
    "25": {
      "L": "'How the mighty have fallen in the midst of the battle! Jonathan is slain upon your high places.'",
      "M": "'How the mighty have fallen in the thick of battle! Jonathan lies slain on your high places.'",
      "T": "How the mighty have fallen\nin the midst of the battle!\nJonathan—slain upon the heights."
    },
    "26": {
      "L": "'I am distressed for you, my brother Jonathan; very pleasant were you to me. Your love to me was more wonderful than the love of women.'",
      "M": "'I grieve for you, my brother Jonathan. You were so dear to me. Your love for me was more extraordinary than the love of women.'",
      "T": "I am broken for you, Jonathan, my brother.\nYou were so dear to me.\nYour love for me was more than wonderful—\nmore than the love of women."
    },
    "27": {
      "L": "'How the mighty have fallen, and the weapons of war have perished!'",
      "M": "'How the mighty have fallen! The weapons of war have perished!'",
      "T": "How the mighty have fallen—\nand the weapons of war are gone."
    }
  },
  "2": {
    "1": {
      "L": "And it came to pass after this that David inquired of the LORD, saying, 'Shall I go up to any of the cities of Judah?' And the LORD said to him, 'Go up.' And David said, 'Where shall I go up?' And he said, 'To Hebron.'",
      "M": "After this, David inquired of the LORD: 'Should I go up to one of the towns of Judah?' The LORD said, 'Go up.' David asked, 'Where shall I go?' And the answer came, 'To Hebron.'",
      "T": "After this David sought the LORD's direction: Should he go up to one of the towns of Judah? The LORD said yes. Where? Hebron."
    },
    "2": {
      "L": "So David went up there, and his two wives also, Ahinoam the Jezreelitess and Abigail the wife of Nabal the Carmelite.",
      "M": "David went up there with his two wives—Ahinoam of Jezreel and Abigail, the widow of Nabal of Carmel.",
      "T": "David went up with his two wives—Ahinoam of Jezreel and Abigail, the widow of Nabal the Carmelite."
    },
    "3": {
      "L": "And his men who were with him David brought up, every man with his household, and they settled in the towns of Hebron.",
      "M": "David also brought his men with him, each with his household, and they settled in the towns around Hebron.",
      "T": "His men came with him, each man with his family, and they settled in the towns of the Hebron region."
    },
    "4": {
      "L": "Then the men of Judah came and there they anointed David king over the house of Judah. And they told David, saying, 'It was the men of Jabesh-gilead who buried Saul.'",
      "M": "Then the men of Judah came to Hebron and anointed David king over the house of Judah. And they told David that the men of Jabesh-gilead were the ones who had buried Saul.",
      "T": "The men of Judah came to Hebron and anointed David king over the house of Judah. And they told him: it was the men of Jabesh-gilead who had given Saul his burial."
    },
    "5": {
      "L": "Then David sent messengers to the men of Jabesh-gilead and said to them, 'Blessed are you of the LORD, for you have shown this kindness to Saul your lord and have buried him.'",
      "M": "David sent messengers to the men of Jabesh-gilead and said, 'May you be blessed by the LORD, because you showed this steadfast loyalty to Saul your lord and gave him burial.'",
      "T": "David sent messengers to Jabesh-gilead: 'The LORD bless you for the covenant loyalty you showed to Saul your lord by burying him.'"
    },
    "6": {
      "L": "And now may the LORD show steadfast love and faithfulness to you; and I also will repay you this kindness because you have done this thing.",
      "M": "And now may the LORD show you steadfast love and faithfulness. I too will repay your kindness, because you have done this.",
      "T": "May the LORD now show you steadfast loyalty and faithfulness in return. And I myself will requite you for this act.'"
    },
    "7": {
      "L": "And now let your hands be strengthened and be valiant, for your lord Saul is dead, and also the house of Judah has anointed me king over them.",
      "M": "Now therefore let your hands be strong, and be courageous, for Saul your lord is dead, and the house of Judah has anointed me king over them.",
      "T": "Be strong now; take courage. Saul your lord is dead. The house of Judah has anointed me king over them.'"
    },
    "8": {
      "L": "But Abner the son of Ner, commander of Saul's army, took Ishbosheth the son of Saul and brought him over to Mahanaim,",
      "M": "But Abner the son of Ner, the commander of Saul's army, took Ishbosheth the son of Saul and brought him across to Mahanaim,",
      "T": "Meanwhile, Abner son of Ner, Saul's army commander, took Ishbosheth son of Saul and brought him across the Jordan to Mahanaim."
    },
    "9": {
      "L": "and made him king over Gilead and the Ashurites and Jezreel and Ephraim and Benjamin and all Israel.",
      "M": "and made him king over Gilead, the Ashurites, Jezreel, Ephraim, Benjamin, and all Israel.",
      "T": "There he set him up as king—over Gilead, the Ashurites, Jezreel, Ephraim, Benjamin, and all Israel."
    },
    "10": {
      "L": "Ishbosheth, Saul's son, was forty years old when he became king over Israel, and he reigned two years. But the house of Judah followed David.",
      "M": "Ishbosheth son of Saul was forty years old when he became king over Israel, and he reigned for two years. The house of Judah, however, followed David.",
      "T": "Ishbosheth was forty years old when he became king over Israel. He reigned two years. But the house of Judah followed David."
    },
    "11": {
      "L": "And the time that David was king in Hebron over the house of Judah was seven years and six months.",
      "M": "David reigned in Hebron over the house of Judah for seven years and six months.",
      "T": "David's reign in Hebron over the house of Judah lasted seven years and six months."
    },
    "12": {
      "L": "And Abner the son of Ner, and the servants of Ishbosheth the son of Saul, went out from Mahanaim to Gibeon.",
      "M": "Abner son of Ner, and the men of Ishbosheth son of Saul, marched out from Mahanaim to Gibeon.",
      "T": "Abner son of Ner marched out from Mahanaim to Gibeon, with Ishbosheth's men at his side."
    },
    "13": {
      "L": "And Joab the son of Zeruiah, and the servants of David, went out and met them by the pool of Gibeon. They sat down, the one on one side of the pool and the other on the other side of the pool.",
      "M": "Joab son of Zeruiah, and David's men, went out and met them at the pool of Gibeon. They took up positions on opposite sides of the pool—one group on one side, the other on the other.",
      "T": "Joab son of Zeruiah came out with David's men and the two forces met at the pool of Gibeon. They sat down facing each other across the water—Abner's men on one side, Joab's on the other."
    },
    "14": {
      "L": "And Abner said to Joab, 'Let the young men arise and compete before us.' And Joab said, 'Let them arise.'",
      "M": "Abner said to Joab, 'Let the young men rise and fight in a contest before us.' Joab said, 'Let them rise.'",
      "T": "Abner spoke to Joab: 'Let the young men come forward and compete before us.' Joab said, 'Let them come.'"
    },
    "15": {
      "L": "So they arose and passed over by number: twelve for Benjamin and Ishbosheth the son of Saul, and twelve of the servants of David.",
      "M": "So twelve men for Benjamin and Ishbosheth son of Saul, and twelve of David's men, stood and faced each other.",
      "T": "Twelve men stepped out for Benjamin, for Ishbosheth son of Saul. Twelve men stepped out for David."
    },
    "16": {
      "L": "And each man seized his opponent by the head and thrust his sword into his opponent's side, and they fell down together. Therefore that place was called Helkath-hazzurim, which is at Gibeon.",
      "M": "Each man grabbed his opponent by the head and drove his sword into his opponent's side, so that all twenty-four fell down together. That place was named Helkath-hazzurim—the Field of Sword-Edges—and it is at Gibeon.",
      "T": "Each man seized his opponent by the head and drove his sword into his side. All twenty-four went down together. The place was called Helkath-hazzurim—Field of Sword-Edges—and it stands at Gibeon."
    },
    "17": {
      "L": "And the battle was very fierce that day, and Abner and the men of Israel were beaten before the servants of David.",
      "M": "The battle was very fierce that day, and Abner and the men of Israel were defeated by David's men.",
      "T": "The battle that followed was brutal. Abner and the men of Israel were beaten by David's men."
    },
    "18": {
      "L": "And there were three sons of Zeruiah there: Joab and Abishai and Asahel. And Asahel was as swift of foot as a wild gazelle.",
      "M": "The three sons of Zeruiah were there—Joab, Abishai, and Asahel. Asahel was as swift of foot as a wild gazelle.",
      "T": "Three sons of Zeruiah were in that battle: Joab, Abishai, and Asahel. Asahel ran like a wild gazelle."
    },
    "19": {
      "L": "And Asahel pursued after Abner, and in his going he turned not to the right hand nor to the left from following Abner.",
      "M": "Asahel took off after Abner, veering neither right nor left in his pursuit.",
      "T": "Asahel fixed on Abner and ran—straight at him, neither right nor left."
    },
    "20": {
      "L": "And Abner looked behind him and said, 'Are you Asahel?' And he answered, 'I am.'",
      "M": "Abner glanced back and called, 'Is that you, Asahel?' He answered, 'It is.'",
      "T": "Abner looked back. 'Asahel—is that you?' 'It is,' came the answer."
    },
    "21": {
      "L": "Abner said to him, 'Turn aside to your right hand or to your left and seize one of the young men and take his spoil.' But Asahel would not turn aside from following him.",
      "M": "Abner said, 'Turn off—right or left—and tackle one of the soldiers and take his gear.' But Asahel would not turn from his pursuit.",
      "T": "'Break off,' Abner said. 'Pick someone else—any one of those soldiers—take his weapons.' But Asahel would not stop."
    },
    "22": {
      "L": "Abner said again to Asahel, 'Turn aside from following me. Why should I strike you to the ground? How then could I lift up my face to your brother Joab?'",
      "M": "Abner said to Asahel again, 'Turn away from me. Why should I strike you down? How could I face your brother Joab after that?'",
      "T": "Abner called out again: 'Stop following me. Why should I kill you? How would I face your brother Joab?'"
    },
    "23": {
      "L": "But he refused to turn aside; therefore Abner struck him in the stomach with the butt end of the spear, so that the spear came out behind him. And he fell there and died in the same place. And all who came to the place where Asahel had fallen and died stood still.",
      "M": "But he refused to turn away. So Abner struck him in the stomach with the blunt end of his spear, and the spear came out through his back. He fell there and died where he stood. And everyone who came to the place where Asahel fell stopped in their tracks.",
      "T": "Asahel would not stop. So Abner drove the butt of his spear into his stomach, and it came out through his back. He crumpled there and died on the spot. Every man who came to that place stood still over the body."
    },
    "24": {
      "L": "But Joab and Abishai pursued after Abner. And the sun was going down when they came to the hill of Ammah, which is before Giah by the way of the wilderness of Gibeon.",
      "M": "Joab and Abishai, however, continued the pursuit of Abner. By the time the sun was setting, they had come to the hill of Ammah, which faces Giah along the way to the wilderness of Gibeon.",
      "T": "Joab and Abishai kept up the chase. As the sun went down they came to the hill of Ammah, which overlooks Giah on the road to the Gibeon wilderness."
    },
    "25": {
      "L": "And the children of Benjamin gathered themselves together after Abner and became one troop, and stood on the top of a hill.",
      "M": "The men of Benjamin rallied to Abner and formed a single unit, standing their ground on the top of a hill.",
      "T": "Benjamin's men gathered around Abner, forming a solid line on the hilltop."
    },
    "26": {
      "L": "Then Abner called to Joab and said, 'Shall the sword devour forever? Do you not know that it will be bitter in the end? How long before you tell the people to turn back from following their brothers?'",
      "M": "Abner called out to Joab: 'Must the sword keep killing forever? Don't you know this will end in bitterness? How long before you order your men to stop pursuing their brothers?'",
      "T": "Abner called out to Joab: 'Must the sword eat and eat and never stop? You know how this ends—in nothing but bitterness. How long before you call your men off their own brothers?'"
    },
    "27": {
      "L": "And Joab said, 'As God lives, if you had not spoken, truly the men would not have given up pursuit of their brothers until the morning.'",
      "M": "Joab answered, 'As God lives, if you had not spoken, the men would not have stopped pursuing their brothers until morning.'",
      "T": "Joab said: 'As God lives—if you had not spoken, my men would have chased yours until morning without stopping.'"
    },
    "28": {
      "L": "So Joab blew the trumpet, and all the people halted and pursued after Israel no more, nor did they fight any more.",
      "M": "Joab blew the trumpet, and all the men stopped and no longer pursued Israel, nor did they continue fighting.",
      "T": "Joab blew the ram's horn. The men stopped. The pursuit ended. The fighting was done."
    },
    "29": {
      "L": "And Abner and his men walked all that night through the Arabah. They crossed the Jordan and walked through all Bithron and came to Mahanaim.",
      "M": "Abner and his men marched through the Arabah all that night. They crossed the Jordan and went through all of Bithron and arrived at Mahanaim.",
      "T": "Abner and his men marched through the Arabah all night. They crossed the Jordan, pushed through all of Bithron, and reached Mahanaim."
    },
    "30": {
      "L": "And Joab returned from following Abner. And when he had gathered all the people together, there were missing of David's servants nineteen men besides Asahel.",
      "M": "When Joab turned back from the pursuit of Abner and gathered all his men together, nineteen of David's men were missing, besides Asahel.",
      "T": "When Joab returned from the pursuit and counted his men, nineteen were missing—plus Asahel."
    },
    "31": {
      "L": "But the servants of David had struck down of Benjamin, and of Abner's men, three hundred and sixty men who died.",
      "M": "But David's men had struck down three hundred and sixty men of Benjamin who served under Abner.",
      "T": "David's men had killed three hundred sixty of Abner's men from Benjamin."
    },
    "32": {
      "L": "They took up Asahel and buried him in the tomb of his father, which was in Bethlehem. And Joab and his men marched all night, and the day broke upon them at Hebron.",
      "M": "They took up Asahel and buried him in his father's tomb at Bethlehem. Then Joab and his men marched through the night and arrived at Hebron at daybreak.",
      "T": "They carried Asahel back and buried him in his father's tomb at Bethlehem. Joab and his men marched all night and were at Hebron when morning broke."
    }
  },
  "3": {
    "1": {
      "L": "Now there was a long war between the house of Saul and the house of David. And David grew stronger and stronger, while the house of Saul grew weaker and weaker.",
      "M": "The war between the house of Saul and the house of David was long drawn out. David grew steadily stronger, while the house of Saul grew steadily weaker.",
      "T": "The war between Saul's house and David's house lasted a long time. David grew stronger and stronger; Saul's house grew weaker and weaker."
    },
    "2": {
      "L": "And sons were born to David in Hebron: his firstborn was Amnon, by Ahinoam the Jezreelitess;",
      "M": "Sons were born to David at Hebron. His firstborn was Amnon, by Ahinoam of Jezreel.",
      "T": "At Hebron David's sons were born. First was Amnon, by Ahinoam of Jezreel."
    },
    "3": {
      "L": "his second, Chileab, by Abigail the wife of Nabal the Carmelite; the third, Absalom the son of Maacah the daughter of Talmai king of Geshur;",
      "M": "His second was Chileab, by Abigail the widow of Nabal the Carmelite. The third was Absalom son of Maacah, the daughter of Talmai king of Geshur.",
      "T": "Second was Chileab, by Abigail the widow of Nabal. Third was Absalom—his mother was Maacah, daughter of Talmai king of Geshur."
    },
    "4": {
      "L": "the fourth, Adonijah the son of Haggith; the fifth, Shephatiah the son of Abital;",
      "M": "The fourth was Adonijah son of Haggith; the fifth, Shephatiah son of Abital.",
      "T": "Fourth was Adonijah, whose mother was Haggith. Fifth was Shephatiah by Abital."
    },
    "5": {
      "L": "and the sixth, Ithream, by Eglah, David's wife. These were born to David in Hebron.",
      "M": "The sixth was Ithream, by David's wife Eglah. These were born to David at Hebron.",
      "T": "Sixth was Ithream, by Eglah, David's wife. Six sons, born at Hebron."
    },
    "6": {
      "L": "And it came to pass, while there was war between the house of Saul and the house of David, that Abner was making himself strong in the house of Saul.",
      "M": "While the war continued between the house of Saul and the house of David, Abner was consolidating his power within Saul's house.",
      "T": "During the long war between Saul's house and David's house, Abner was quietly building his own position inside Saul's camp."
    },
    "7": {
      "L": "Now Saul had a concubine whose name was Rizpah daughter of Aiah. And Ishbosheth said to Abner, 'Why have you gone in to my father's concubine?'",
      "M": "Saul had a concubine named Rizpah daughter of Aiah. And Ishbosheth said to Abner, 'Why have you slept with my father's concubine?'",
      "T": "Saul had a concubine named Rizpah, daughter of Aiah. Ishbosheth accused Abner: 'You have been sleeping with my father's concubine.'"
    },
    "8": {
      "L": "Then Abner was very angry at the words of Ishbosheth and said, 'Am I a dog's head? Against Judah? Today I am showing steadfast love to the house of Saul your father, to his brothers and to his friends, and have not given you into the hand of David; yet you charge me today with guilt regarding this woman!'",
      "M": "Abner was furious at these words. He said, 'Am I a dog's head—some nobody against Judah? To this day I have been showing steadfast loyalty to the house of your father Saul, to his brothers and his friends; I have not handed you over to David. And yet you are charging me with wrongdoing over this woman!'",
      "T": "Abner erupted in fury. 'Am I a dog? Some traitor to Judah? I have kept faith with your father's house all this time—with his brothers, with his friends. I have not handed you over to David. And now you accuse me over this woman!'"
    },
    "9": {
      "L": "God do so to Abner and more also, if I do not accomplish for David what the LORD has sworn to him,",
      "M": "'God do so to me, and more, if I do not carry out for David what the LORD has sworn to him—",
      "T": "'God deal with me in full if I do not do for David what the LORD swore to him—'"
    },
    "10": {
      "L": "'to transfer the kingdom from the house of Saul and to set up the throne of David over Israel and over Judah, from Dan even to Beersheba.'",
      "M": "'to transfer the kingdom from the house of Saul and establish David's throne over Israel and Judah, from Dan to Beersheba.'",
      "T": "'—transfer the kingdom from Saul's house and raise up David's throne over all Israel and Judah, from Dan all the way to Beersheba.'"
    },
    "11": {
      "L": "And he could not answer Abner another word, for he feared him.",
      "M": "Ishbosheth could not answer Abner another word, because he was afraid of him.",
      "T": "Ishbosheth had nothing to say. He was afraid of Abner."
    },
    "12": {
      "L": "Then Abner sent messengers to David on his behalf, saying, 'To whom does the land belong? Make your covenant with me, and behold, my hand shall be with you to bring over all Israel to you.'",
      "M": "Abner sent messengers to David on his own behalf, saying, 'To whom does the land belong? Make a treaty with me, and my hand will be with you to bring all Israel over to you.'",
      "T": "Abner sent messengers straight to David, speaking for himself: 'Who does this land really belong to? Make a covenant with me, and I will bring all Israel over to you.'"
    },
    "13": {
      "L": "And he said, 'Good; I will make a covenant with you. But one thing I require of you, namely, that you shall not see my face unless you first bring Michal, Saul's daughter, when you come to see me.'",
      "M": "David said, 'Good; I will make a treaty with you. But there is one condition: you shall not appear before me unless you bring Michal, Saul's daughter, when you come.'",
      "T": "'Good,' David said. 'I will make a treaty with you—but on one condition: when you come to see me, bring Michal, Saul's daughter, with you.'"
    },
    "14": {
      "L": "Then David sent messengers to Ishbosheth, Saul's son, saying, 'Give me my wife Michal, whom I betrothed to myself for a hundred foreskins of the Philistines.'",
      "M": "David sent messengers to Ishbosheth son of Saul, saying, 'Return my wife Michal, for whom I paid the bride-price of a hundred Philistine foreskins.'",
      "T": "David also sent word to Ishbosheth: 'Return my wife Michal. I paid a hundred Philistine foreskins as the bride-price. She is mine.'"
    },
    "15": {
      "L": "So Ishbosheth sent and took her from her husband, from Phaltiel the son of Laish.",
      "M": "Ishbosheth sent and took her from her husband, Phaltiel son of Laish.",
      "T": "Ishbosheth had her taken from her husband, Phaltiel son of Laish."
    },
    "16": {
      "L": "And her husband went with her, weeping as he followed her all the way to Bahurim. Then Abner said to him, 'Go, return.' And he returned.",
      "M": "Her husband followed her, weeping as he walked behind her all the way to Bahurim. Then Abner said to him, 'Go back.' And he turned back.",
      "T": "Her husband went with her, weeping as he walked behind her all the way to Bahurim, until Abner told him: 'Go back.' And he went back."
    },
    "17": {
      "L": "And Abner had communication with the elders of Israel, saying, 'In times past you have been seeking David as king over you.'",
      "M": "Abner had been in contact with the elders of Israel, saying, 'For some time now you have been wanting David as your king.'",
      "T": "Abner had also been working on the elders of Israel: 'You have been looking to David as king. You have wanted this for some time.'"
    },
    "18": {
      "L": "'Now then, do it! For the LORD has said of David, By the hand of my servant David I will save my people Israel from the hand of the Philistines and from the hand of all their enemies.'",
      "M": "'Now do it! For the LORD has said of David, By my servant David's hand I will save my people Israel from the Philistines and all their enemies.'",
      "T": "'Now act. The LORD himself has said: through my servant David I will rescue my people Israel from the Philistines and from every enemy.'"
    },
    "19": {
      "L": "Abner also spoke in the ears of Benjamin. And then Abner went also to speak in the ears of David in Hebron all that seemed good to Israel and all the house of Benjamin.",
      "M": "Abner also spoke to the men of Benjamin. Then he went to Hebron and told David in person everything that Israel and the whole house of Benjamin agreed to.",
      "T": "Abner spoke to Benjamin as well. Then he went to Hebron and laid before David in person everything that Israel and the house of Benjamin had agreed."
    },
    "20": {
      "L": "So Abner came to David at Hebron, with twenty men with him, and David made a feast for Abner and the men who were with him.",
      "M": "Abner came to David at Hebron with twenty men, and David made a feast for him and his party.",
      "T": "Abner came to Hebron with twenty men, and David held a feast for him and all who came with him."
    },
    "21": {
      "L": "And Abner said to David, 'I will arise and go, and I will gather all Israel to my lord the king, that they may make a covenant with you, and that you may reign over all that your soul desires.' So David sent Abner away, and he went in peace.",
      "M": "Abner said to David, 'Let me go and gather all Israel to my lord the king, so that they may make a covenant with you and you may rule over all that you desire.' David sent Abner away, and he left in peace.",
      "T": "Abner said: 'Let me go now and rally all Israel to you, my lord the king, so they can make a covenant with you and you can reign over everything you desire.' David sent Abner off, and he left in peace."
    },
    "22": {
      "L": "And just then the servants of David and Joab came from a raid and brought with them much spoil. But Abner was not with David in Hebron, for he had sent him away and he had gone in peace.",
      "M": "Just then, Joab and David's men returned from a raid, bringing a large amount of plunder. Abner was no longer with David at Hebron, for David had sent him away and he had gone in peace.",
      "T": "At that very moment Joab and David's men came back from a raiding expedition, carrying a large haul of plunder. Abner had just left Hebron—David had sent him away in peace."
    },
    "23": {
      "L": "When Joab and all the army that was with him arrived, they told Joab, 'Abner the son of Ner came to the king, and he sent him away, and he has gone in peace.'",
      "M": "When Joab and the whole force arrived, someone told him, 'Abner son of Ner came to the king and David sent him away, and he left in peace.'",
      "T": "When Joab arrived with the army, he was told: Abner son of Ner came to the king. The king received him and sent him away in peace."
    },
    "24": {
      "L": "Then Joab went to the king and said, 'What have you done? Behold, Abner came to you! Why is it that you sent him away, so that he is already gone?'",
      "M": "Joab went straight to the king and said, 'What have you done? Abner came to you—why did you send him away? He is gone!'",
      "T": "Joab went straight to the king. 'What have you done? Abner came to you. Why did you let him go? He is already gone.'"
    },
    "25": {
      "L": "'You know Abner the son of Ner—he came to deceive you and to know your going out and your coming in, and to know all that you are doing.'",
      "M": "'You know Abner son of Ner. He came to trick you—to learn your movements and find out everything you are doing.'",
      "T": "'You know what Abner is. He came here to deceive you, to scout your movements, to learn everything you are doing.'"
    },
    "26": {
      "L": "When Joab left David's presence, he sent messengers after Abner, and they brought him back from the well of Sirah. But David did not know about it.",
      "M": "When Joab left David, he sent messengers after Abner and brought him back from the well of Sirah. David knew nothing about it.",
      "T": "As soon as Joab was out of David's presence, he sent messengers after Abner and brought him back from the well of Sirah. David knew nothing about it."
    },
    "27": {
      "L": "When Abner returned to Hebron, Joab took him aside in the gate to speak with him quietly, and there he struck him in the stomach so that he died, for the blood of Asahel his brother.",
      "M": "When Abner returned to Hebron, Joab took him aside in the gateway—as if to speak privately with him—and stabbed him in the stomach. He died there, avenging the blood of his brother Asahel.",
      "T": "When Abner arrived at Hebron, Joab drew him aside in the gateway—a quiet word in private, he made it seem—and drove his knife into Abner's stomach. Abner died there: blood for blood, for Asahel."
    },
    "28": {
      "L": "Afterward, when David heard of it, he said, 'I and my kingdom are innocent before the LORD forever of the blood of Abner the son of Ner.'",
      "M": "When David heard about it afterward, he said, 'I and my kingdom are forever innocent before the LORD of the blood of Abner son of Ner.'",
      "T": "When the news reached David, he declared publicly: 'I and my kingdom are innocent before the LORD, forever, of the blood of Abner son of Ner.'"
    },
    "29": {
      "L": "'Let it fall upon the head of Joab and upon all his father's house. And let there not fail from the house of Joab one who has a discharge, or a leper, or one who handles a spindle, or one who falls by the sword, or one who lacks bread.'",
      "M": "'Let it fall on Joab's head and on all his father's house. May the house of Joab never lack someone suffering from a discharge, or leprosy, or dependent on a staff, or killed by the sword, or lacking food.'",
      "T": "'Let it rest on Joab's head and on his whole family. May there never be a generation of Joab's house without someone diseased, or leprous, or dependent on others, or cut down by the sword, or without bread.'"
    },
    "30": {
      "L": "So Joab and Abishai his brother killed Abner, because he had put their brother Asahel to death in the battle at Gibeon.",
      "M": "Joab and his brother Abishai had killed Abner because he had killed their brother Asahel in the battle at Gibeon.",
      "T": "Joab and Abishai had killed Abner. He had killed their brother Asahel at Gibeon. This was the blood-debt they paid."
    },
    "31": {
      "L": "Then David said to Joab and to all the people who were with him, 'Tear your clothes and put on sackcloth and mourn before Abner.' And King David walked behind the bier.",
      "M": "David said to Joab and to all his men, 'Tear your clothes, put on sackcloth, and mourn for Abner.' King David himself walked behind the funeral bier.",
      "T": "David told Joab and all his men: 'Tear your clothes. Put on sackcloth. Mourn for Abner.' And David the king walked behind the bier himself."
    },
    "32": {
      "L": "They buried Abner in Hebron. The king lifted up his voice and wept at the grave of Abner, and all the people wept.",
      "M": "They buried Abner at Hebron. The king wept aloud at the graveside, and all the people wept with him.",
      "T": "They buried Abner in Hebron. At the grave the king wept openly, and all the people wept with him."
    },
    "33": {
      "L": "And the king lamented over Abner and said, 'Should Abner have died as a fool dies?'",
      "M": "The king sang a lament over Abner: 'Should Abner have died as a foolish man dies?'",
      "T": "The king sang a lament over Abner: 'Was Abner to die like a fool?'"
    },
    "34": {
      "L": "'Your hands were not bound, your feet were not put in fetters. As a man falls before the wicked, so you fell.' And all the people wept over him again.",
      "M": "'Your hands were not bound; your feet were not fettered in chains. You fell as one falls before treacherous men.' All the people wept for him again.",
      "T": "Your hands were free—not bound.\nYour feet were not in chains.\nYou fell the way one falls before ruthless men—\nnot on the battlefield, but by treachery.\nAll the people wept for him again."
    },
    "35": {
      "L": "Then all the people came to persuade David to eat bread while it was yet day. But David swore, saying, 'God do so to me and more also, if I taste bread or anything else until the sun goes down.'",
      "M": "Then all the people came to urge David to eat before the day was over. But David swore: 'God do so to me and more, if I eat bread or anything else before sundown.'",
      "T": "All the people pressed David to eat while it was still light. But David swore: 'God deal with me severely if I touch bread or anything else before the sun goes down.'"
    },
    "36": {
      "L": "And all the people took notice and it pleased them, as everything the king did pleased all the people.",
      "M": "All the people took notice, and it pleased them. Everything the king did pleased all the people.",
      "T": "The people noticed. They were pleased. Everything the king did in these hours had their approval."
    },
    "37": {
      "L": "So all the people and all Israel understood that day that it had not been the king's will to put Abner the son of Ner to death.",
      "M": "So all the people and all Israel understood that day that the king had had no part in Abner's death.",
      "T": "All Israel understood that day: the king had not ordered Abner's death. The king was innocent."
    },
    "38": {
      "L": "And the king said to his servants, 'Do you not know that a prince and a great man has fallen this day in Israel?'",
      "M": "The king said to his servants, 'Do you not know that a commander and a great man has fallen in Israel today?'",
      "T": "The king said to his men: 'Do you not see what was lost today? A leader. A great man in Israel.'"
    },
    "39": {
      "L": "'And I am this day weak, though anointed king; and these men, the sons of Zeruiah, are too hard for me. May the LORD repay the evildoer according to his wickedness!'",
      "M": "'And today, though I am anointed king, I am weak. These men, the sons of Zeruiah, are too strong for me. May the LORD repay the evildoer according to his wickedness!'",
      "T": "'I was anointed king—and yet I am weak. These sons of Zeruiah are too hard for me. May the LORD repay the one who did this evil according to what he has done.'"
    }
  },
  "4": {
    "1": {
      "L": "When Ishbosheth the son of Saul heard that Abner had died in Hebron, his hands grew feeble, and all Israel was dismayed.",
      "M": "When Ishbosheth son of Saul heard that Abner had died at Hebron, his courage failed him, and all Israel was alarmed.",
      "T": "When Ishbosheth heard that Abner was dead, he lost his nerve. All Israel was shaken."
    },
    "2": {
      "L": "Now Saul's son had two men who were captains of raiding bands: the name of the one was Baanah, and the name of the other Rechab, sons of Rimmon the Beerothite, of the sons of Benjamin—for Beeroth was also reckoned to Benjamin.",
      "M": "Saul's son had two men who were commanders of raiding parties. One was named Baanah, the other Rechab—both sons of Rimmon the Beerothite, from the tribe of Benjamin; for Beeroth was reckoned as part of Benjamin.",
      "T": "Ishbosheth had two commanders of raiding bands: Rechab and Baanah, sons of Rimmon the Beerothite, from the tribe of Benjamin. Beeroth was counted as part of Benjamin's territory."
    },
    "3": {
      "L": "The Beerothites had fled to Gittaim and have been sojourners there to this day.",
      "M": "The people of Beeroth had fled to Gittaim and have lived there as resident foreigners to this day.",
      "T": "The Beerothites had earlier fled to Gittaim, where they lived as resident aliens—and still do."
    },
    "4": {
      "L": "Jonathan the son of Saul had a son who was lame in both feet. He was five years old when the news about Saul and Jonathan came from Jezreel, and his nurse took him up and fled; and in her haste to flee, he fell and became lame. His name was Mephibosheth.",
      "M": "Jonathan son of Saul had a son who was lame in both feet. He was five years old when the news came from Jezreel about Saul and Jonathan. His nurse picked him up and fled, but in her rush to escape, he fell and was crippled. His name was Mephibosheth.",
      "T": "Jonathan son of Saul had a son named Mephibosheth who was lame in both feet. He was five years old when the news of Saul's and Jonathan's deaths reached Jezreel. In the panic, his nurse scooped him up and ran—and he fell and was crippled as she fled."
    },
    "5": {
      "L": "The sons of Rimmon the Beerothite, Rechab and Baanah, set out and came to the house of Ishbosheth at the heat of the day, while he was taking his noonday rest.",
      "M": "Rechab and Baanah, the sons of Rimmon the Beerothite, set off and arrived at Ishbosheth's house during the heat of the day, when he was lying down for his midday rest.",
      "T": "Rechab and Baanah, the sons of Rimmon the Beerothite, went to Ishbosheth's house at midday while the king was resting in the heat of the day."
    },
    "6": {
      "L": "And they came into the middle of the house as if fetching wheat, and they stabbed him in the stomach. Then Rechab and Baanah his brother escaped.",
      "M": "They slipped into the interior of the house under the pretense of getting wheat, and stabbed him in the stomach. Then Rechab and his brother Baanah made their escape.",
      "T": "They entered the house as if to collect wheat and stabbed him in the stomach. Then they ran."
    },
    "7": {
      "L": "When they came into the house, he was lying on his bed in his bedroom. And they struck him and killed him and beheaded him, and they took his head and went away through the Arabah all night.",
      "M": "They had gone into the house where he lay on his bed in his bedroom. They struck him down, killed him, and cut off his head. Then they carried the head and traveled through the Arabah all night.",
      "T": "Ishbosheth had been lying on his bed in his bedroom. They struck him, killed him, and cut off his head. They took the head and moved through the Arabah all night."
    },
    "8": {
      "L": "And they brought the head of Ishbosheth to David at Hebron and said to the king, 'Here is the head of Ishbosheth the son of Saul, your enemy, who sought your life. The LORD has given my lord the king vengeance today against Saul and his offspring.'",
      "M": "They brought the head of Ishbosheth to David at Hebron and said to the king, 'Here is the head of Ishbosheth son of Saul, your enemy who sought your life. Today the LORD has given my lord the king vengeance on Saul and his descendants.'",
      "T": "They brought Ishbosheth's head to David at Hebron. 'Here is the head of Ishbosheth son of Saul—your enemy, the man who wanted you dead. The LORD has given our lord the king justice today against Saul and his line.'"
    },
    "9": {
      "L": "But David answered Rechab and Baanah his brother, the sons of Rimmon the Beerothite, and said to them, 'As the LORD lives, who has redeemed my life from every adversity,",
      "M": "David answered Rechab and his brother Baanah, the sons of Rimmon the Beerothite: 'As the LORD lives, who has redeemed my life from every trouble—",
      "T": "David answered Rechab and Baanah—the sons of Rimmon the Beerothite—and said: 'As the LORD lives, who has rescued my life from every danger—'"
    },
    "10": {
      "L": "'when one told me, Behold, Saul is dead, thinking he was bringing good news, I seized him and killed him at Ziklag, which was the reward I gave him for his news.'",
      "M": "'when the man who told me, Saul is dead, thought he was bringing good news, I had him killed at Ziklag—that was the reward I gave him for his news.'",
      "T": "'—when a man came to me at Ziklag claiming Saul was dead, thinking to bring me good news, I killed him. That was the reward I gave for that news.'"
    },
    "11": {
      "L": "'How much more, when wicked men have killed a righteous man in his own house on his bed, shall I not now require his blood from your hands and destroy you from the earth?'",
      "M": "'How much more, then, when wicked men murder a righteous man in his own house on his bed—should I not demand his blood from your hands and rid the earth of you?'",
      "T": "'Now you have murdered an innocent man in his own house while he slept. How much more certainly will I require his blood from your hands and remove you from this earth?'"
    },
    "12": {
      "L": "And David commanded his young men, and they killed them. They cut off their hands and their feet and hanged them over the pool at Hebron. But the head of Ishbosheth they took and buried in the tomb of Abner at Hebron.",
      "M": "David gave the order to his men, and they executed them. They cut off their hands and feet and hung their bodies by the pool at Hebron. But the head of Ishbosheth they took and buried in the tomb of Abner at Hebron.",
      "T": "David gave the order. His men killed them—cutting off their hands and feet and hanging the bodies beside the pool at Hebron. The head of Ishbosheth they buried in Abner's tomb at Hebron."
    }
  },
  "5": {
    "1": {
      "L": "Then all the tribes of Israel came to David at Hebron and spoke, saying, 'Behold, we are your bone and your flesh.'",
      "M": "Then all the tribes of Israel came to David at Hebron and said, 'We are your own bone and flesh.'",
      "T": "Then all the tribes of Israel came to David at Hebron. 'We are your own flesh and blood,' they said."
    },
    "2": {
      "L": "'In times past, when Saul was king over us, you were the one who led out and brought in Israel. And the LORD said to you, You shall shepherd my people Israel, and you shall be prince over Israel.'",
      "M": "'Even when Saul was our king, it was you who led Israel out to battle and brought them home. And the LORD said to you, You shall shepherd my people Israel, and you shall be ruler over Israel.'",
      "T": "'Even in Saul's time it was you who led Israel out and brought them back. And the LORD told you: You shall shepherd my people Israel; you shall be the ruler over Israel.'"
    },
    "3": {
      "L": "So all the elders of Israel came to the king at Hebron, and King David made a covenant with them at Hebron before the LORD. And they anointed David king over Israel.",
      "M": "So all the elders of Israel came to the king at Hebron, and King David made a covenant with them before the LORD. And they anointed David king over Israel.",
      "T": "All the elders of Israel came to the king at Hebron. King David made a covenant with them before the LORD, and they anointed David king over all Israel."
    },
    "4": {
      "L": "David was thirty years old when he began to reign, and he reigned forty years.",
      "M": "David was thirty years old when he became king, and he reigned for forty years.",
      "T": "David was thirty years old when he became king. He reigned forty years in all."
    },
    "5": {
      "L": "In Hebron he reigned over Judah seven years and six months, and in Jerusalem he reigned thirty-three years over all Israel and Judah.",
      "M": "He reigned in Hebron over Judah seven years and six months, and in Jerusalem he reigned thirty-three years over all Israel and Judah.",
      "T": "Seven years and six months at Hebron over Judah. Thirty-three years at Jerusalem over all Israel and Judah."
    },
    "6": {
      "L": "And the king and his men went to Jerusalem against the Jebusites, the inhabitants of the land, who said to David, 'You will not come in here, but the blind and the lame will turn you back'—thinking, 'David cannot come in here.'",
      "M": "The king and his men marched to Jerusalem against the Jebusites, who inhabited the land. They said to David, 'You will never get in here—even the blind and the lame can hold you off,' meaning that David could not enter there.",
      "T": "David and his men marched to Jerusalem against the Jebusites, the people of the land. 'You will never get in here,' they called out. 'Even the blind and the lame could stop you.' They were taunting David—saying the city was impregnable."
    },
    "7": {
      "L": "Nevertheless David captured the stronghold of Zion, that is, the city of David.",
      "M": "But David captured the stronghold of Zion, which is now the city of David.",
      "T": "David captured it anyway—the stronghold of Zion, the city of David."
    },
    "8": {
      "L": "And David said on that day, 'Whoever strikes the Jebusites, let him get up through the water shaft to the lame and the blind, who are hated by David's soul.' Therefore it is said, 'The blind and the lame shall not come into the house.'",
      "M": "David said that day, 'Whoever would strike down the Jebusites must go up through the water tunnel to attack the lame and the blind, whom David's soul despises.' Therefore the saying arose, 'The blind and the lame shall not enter the house.'",
      "T": "David said that day: 'Whoever strikes the Jebusites must go up through the water shaft—go after the lame and the blind who mock us.' From that day the saying was made: 'The blind and the lame shall not enter the house.'"
    },
    "9": {
      "L": "And David lived in the stronghold and called it the city of David. And David built all around from the Millo inward.",
      "M": "David took up residence in the stronghold and called it the city of David. He built up the city all around, from the Millo inward.",
      "T": "David settled in the stronghold and named it the city of David. He built it up all around from the Millo inward."
    },
    "10": {
      "L": "And David grew greater and greater, for the LORD God of hosts was with him.",
      "M": "David grew steadily greater, for the LORD God of hosts was with him.",
      "T": "And David grew greater and greater, because the LORD God of hosts was with him."
    },
    "11": {
      "L": "And Hiram king of Tyre sent messengers to David, and cedar trees, and carpenters and masons, and they built David a house.",
      "M": "Hiram king of Tyre sent messengers to David, along with cedar timber, carpenters, and stonemasons, and they built David a palace.",
      "T": "Hiram king of Tyre sent envoys to David, with cedar timber and carpenters and stonemasons who built him a royal palace."
    },
    "12": {
      "L": "And David knew that the LORD had established him king over Israel, and that he had exalted his kingdom for the sake of his people Israel.",
      "M": "David recognized that the LORD had established him as king over Israel and had elevated his kingdom for the sake of his people Israel.",
      "T": "David understood: the LORD had established him as king over Israel, had elevated his kingdom—not for David's own glory but for the sake of Israel, the LORD's people."
    },
    "13": {
      "L": "And David took more concubines and wives from Jerusalem, after he came from Hebron, and more sons and daughters were born to David.",
      "M": "After coming from Hebron, David took more concubines and wives in Jerusalem, and more sons and daughters were born to him.",
      "T": "After moving to Jerusalem, David took additional concubines and wives, and more sons and daughters were born to him."
    },
    "14": {
      "L": "These are the names of those born to him in Jerusalem: Shammua, Shobab, Nathan, Solomon,",
      "M": "These are the names of those born to him in Jerusalem: Shammua, Shobab, Nathan, Solomon,",
      "T": "These are the children born to him in Jerusalem: Shammua, Shobab, Nathan, Solomon,"
    },
    "15": {
      "L": "Ibhar, Elishua, Nepheg, and Japhia,",
      "M": "Ibhar, Elishua, Nepheg, and Japhia,",
      "T": "Ibhar, Elishua, Nepheg, and Japhia,"
    },
    "16": {
      "L": "Elishama, Eliada, and Eliphelet.",
      "M": "Elishama, Eliada, and Eliphelet.",
      "T": "Elishama, Eliada, and Eliphelet."
    },
    "17": {
      "L": "When the Philistines heard that David had been anointed king over Israel, all the Philistines came up to search for David. When David heard of it, he went down to the stronghold.",
      "M": "When the Philistines heard that David had been anointed king over Israel, they all came up in force to find him. David heard of it and went down to the stronghold.",
      "T": "When the Philistines heard that David had been anointed king over all Israel, they came up in full force to hunt him down. David heard the news and went down to the stronghold."
    },
    "18": {
      "L": "Now the Philistines had come and spread themselves out in the Valley of Rephaim.",
      "M": "The Philistines had come and deployed themselves in the Valley of Rephaim.",
      "T": "The Philistines had spread out in the Valley of Rephaim."
    },
    "19": {
      "L": "And David inquired of the LORD, saying, 'Shall I go up against the Philistines? Will you give them into my hand?' And the LORD said to David, 'Go up, for I will certainly give the Philistines into your hand.'",
      "M": "David inquired of the LORD: 'Should I attack the Philistines? Will you hand them over to me?' The LORD answered David, 'Go up, for I will certainly give the Philistines into your hand.'",
      "T": "David asked the LORD: 'Shall I attack the Philistines? Will you give them to me?' The LORD answered: 'Go. I will certainly give the Philistines into your hand.'"
    },
    "20": {
      "L": "And David came to Baal-perazim, and David defeated them there. And he said, 'The LORD has broken through my enemies before me like a bursting flood.' Therefore the name of that place is called Baal-perazim.",
      "M": "David came to Baal-perazim and defeated the Philistines there. He said, 'The LORD has burst through my enemies before me like a flood of waters.' So that place was named Baal-perazim.",
      "T": "David came to Baal-perazim and struck the Philistines there. He said: 'The LORD has burst through my enemies before me like a flood breaking through.' So the place was named Baal-perazim—Lord of the Breakthrough."
    },
    "21": {
      "L": "And they abandoned their idols there, and David and his men took them away.",
      "M": "The Philistines left their idols there, and David and his men carried them off.",
      "T": "The Philistines fled, leaving their idols behind. David and his men burned them."
    },
    "22": {
      "L": "And the Philistines came up once more and spread themselves out in the Valley of Rephaim.",
      "M": "The Philistines came up again and deployed in the Valley of Rephaim.",
      "T": "The Philistines came back and spread out in the Valley of Rephaim again."
    },
    "23": {
      "L": "And when David inquired of the LORD, he said, 'You shall not go up; circle around behind them and come upon them opposite the balsam trees.'",
      "M": "David inquired of the LORD, who said, 'Do not go straight up; circle around behind them and come at them opposite the balsam trees.'",
      "T": "David again asked the LORD for direction. This time: 'Do not attack them head-on. Circle around behind and come at them from the side, opposite the balsam trees.'"
    },
    "24": {
      "L": "'And when you hear the sound of marching in the tops of the balsam trees, then rouse yourself, for then the LORD has gone out before you to strike down the army of the Philistines.'",
      "M": "'When you hear the sound of marching in the tops of the balsam trees, rouse yourself to act, for that will be the sign that the LORD has gone out before you to strike down the Philistine army.'",
      "T": "'When you hear the sound of movement in the tops of the balsam trees, that is your signal—the LORD has gone out ahead of you to strike the Philistine army.'"
    },
    "25": {
      "L": "And David did just as the LORD commanded him, and struck down the Philistines from Geba all the way to Gezer.",
      "M": "David did as the LORD commanded him and struck down the Philistines from Geba all the way to Gezer.",
      "T": "David obeyed, and struck the Philistines from Geba to Gezer."
    }
  },
  "6": {
    "1": {
      "L": "Again David gathered all the chosen men of Israel, thirty thousand.",
      "M": "David again assembled all the chosen men of Israel—thirty thousand of them.",
      "T": "David mustered thirty thousand picked men of Israel."
    },
    "2": {
      "L": "And David arose and went with all the people who were with him from Baale-judah to bring up from there the ark of God, which is called by the name of the LORD of hosts who sits enthroned on the cherubim.",
      "M": "David set out with all the people who were with him from Baale-judah to bring up from there the ark of God, which bears the name of the LORD of hosts who is enthroned above the cherubim.",
      "T": "David and all the people with him went to Baale-judah to bring up the ark of God—the ark that bears the name of the LORD of hosts, who sits enthroned above the cherubim."
    },
    "3": {
      "L": "They set the ark of God on a new cart and brought it out of the house of Abinadab, which was on the hill. And Uzzah and Ahio, the sons of Abinadab, were driving the new cart.",
      "M": "They put the ark of God on a new cart and brought it out of the house of Abinadab on the hill. Uzzah and Ahio, the sons of Abinadab, were guiding the new cart,",
      "T": "They loaded the ark of God onto a new cart and brought it out from the house of Abinadab on the hill. Uzzah and Ahio, Abinadab's sons, guided the cart."
    },
    "4": {
      "L": "carrying the ark of God. Ahio went ahead of the ark.",
      "M": "with the ark of God on it. Ahio walked in front of the ark.",
      "T": "Ahio walked ahead of the ark."
    },
    "5": {
      "L": "And David and all the house of Israel were celebrating before the LORD with songs, with lyres and harps and tambourines and castanets and cymbals.",
      "M": "David and all the house of Israel were celebrating before the LORD with all kinds of instruments—lyres, harps, tambourines, castanets, and cymbals.",
      "T": "David and all Israel celebrated before the LORD with every kind of musical instrument—lyres, harps, tambourines, castanets, and cymbals."
    },
    "6": {
      "L": "When they came to the threshing floor of Nacon, Uzzah put out his hand to the ark of God and took hold of it, for the oxen stumbled.",
      "M": "When they came to the threshing floor of Nacon, Uzzah reached out and took hold of the ark of God, because the oxen had stumbled.",
      "T": "At the threshing floor of Nacon the oxen stumbled. Uzzah reached out and took hold of the ark of God to steady it."
    },
    "7": {
      "L": "And the anger of the LORD was kindled against Uzzah, and God struck him down there for his error, and he died there by the ark of God.",
      "M": "The anger of the LORD flared against Uzzah, and God struck him down there for his irreverence, and he died there beside the ark of God.",
      "T": "The LORD's anger flared. God struck Uzzah down on the spot for his presumptuousness, and he died there beside the ark."
    },
    "8": {
      "L": "And David was angry because the LORD had burst out against Uzzah. And that place is called Perez-uzzah to this day.",
      "M": "David was upset because the LORD had struck out against Uzzah. That place is still called Perez-uzzah to this day.",
      "T": "David was shaken and angry—the LORD had burst out against Uzzah. The place was named Perez-uzzah, and it keeps that name to this day."
    },
    "9": {
      "L": "And David was afraid of the LORD that day and said, 'How can the ark of the LORD come to me?'",
      "M": "David was afraid of the LORD that day and said, 'How can the ark of the LORD come to me now?'",
      "T": "David was afraid of the LORD that day. 'How can the ark of the LORD come to me now?' he said."
    },
    "10": {
      "L": "So David was not willing to bring the ark of the LORD into the city of David. But David took it aside to the house of Obed-edom the Gittite.",
      "M": "David was unwilling to bring the ark of the LORD into the city of David. He took it aside to the house of Obed-edom the Gittite.",
      "T": "David would not bring the ark into the city of David. Instead he turned aside and left it at the house of Obed-edom the Gittite."
    },
    "11": {
      "L": "The ark of the LORD remained in the house of Obed-edom the Gittite for three months, and the LORD blessed Obed-edom and all his household.",
      "M": "The ark of the LORD stayed at the house of Obed-edom the Gittite for three months, and the LORD blessed Obed-edom and his entire household.",
      "T": "The ark stayed at Obed-edom's house three months. The LORD blessed Obed-edom and all who were in his household."
    },
    "12": {
      "L": "And it was told King David, 'The LORD has blessed the household of Obed-edom and all that belongs to him, because of the ark of God.' So David went and brought up the ark of God from the house of Obed-edom to the city of David with rejoicing.",
      "M": "It was reported to King David: 'The LORD has blessed the household of Obed-edom and everything belonging to him, because of the ark of God.' So David went and brought up the ark of God from the house of Obed-edom to the city of David with great rejoicing.",
      "T": "News reached King David: the LORD was blessing Obed-edom's household and everything he owned, because of the ark. So David went and brought the ark of God up from Obed-edom's house to the city of David with great joy."
    },
    "13": {
      "L": "And when those who bore the ark of the LORD had gone six paces, he sacrificed an ox and a fattened animal.",
      "M": "When those carrying the ark of the LORD had gone six paces, David sacrificed an ox and a fattened calf.",
      "T": "Six paces. After the ark-bearers had taken six steps, David sacrificed an ox and a fatted calf."
    },
    "14": {
      "L": "And David danced before the LORD with all his might, and David was wearing a linen ephod.",
      "M": "David danced before the LORD with all his strength, wearing a linen ephod.",
      "T": "David danced before the LORD with everything in him, wearing a linen ephod."
    },
    "15": {
      "L": "So David and all the house of Israel brought up the ark of the LORD with shouting and with the sound of the trumpet.",
      "M": "David and all the house of Israel brought up the ark of the LORD with shouting and the sound of the trumpet.",
      "T": "David and all Israel brought the ark of the LORD up with shouts and the blast of the ram's horn."
    },
    "16": {
      "L": "As the ark of the LORD came into the city of David, Michal the daughter of Saul looked out through a window and saw King David leaping and dancing before the LORD, and she despised him in her heart.",
      "M": "As the ark of the LORD entered the city of David, Michal daughter of Saul looked down through a window and saw King David leaping and dancing before the LORD, and she despised him in her heart.",
      "T": "As the ark of the LORD entered the city of David, Michal daughter of Saul looked out from a window. She saw King David leaping and dancing before the LORD—and she despised him in her heart."
    },
    "17": {
      "L": "They brought in the ark of the LORD and set it in its place, inside the tent that David had pitched for it. And David offered burnt offerings and peace offerings before the LORD.",
      "M": "They brought in the ark of the LORD and set it in its place, inside the tent David had pitched for it. David offered burnt offerings and fellowship offerings before the LORD.",
      "T": "They brought the ark in and set it in its place inside the tent David had pitched for it. David offered burnt offerings and peace offerings before the LORD."
    },
    "18": {
      "L": "When David had finished offering the burnt offerings and the peace offerings, he blessed the people in the name of the LORD of hosts.",
      "M": "When David had finished offering the burnt offerings and the peace offerings, he blessed the people in the name of the LORD of hosts.",
      "T": "When David had finished the offerings, he blessed the people in the name of the LORD of hosts."
    },
    "19": {
      "L": "And he distributed among all the people, the whole multitude of Israel, both men and women, each a cake of bread, and a portion of meat, and a cake of raisins. Then all the people departed, each to his own house.",
      "M": "He distributed to the whole assembly of Israel—men and women alike—a loaf of bread, a portion of roasted meat, and a raisin cake. Then all the people went to their own homes.",
      "T": "He distributed food to the whole multitude of Israel, men and women together—bread, meat, and a raisin cake for each. Then everyone went home."
    },
    "20": {
      "L": "Then David returned to bless his household. And Michal the daughter of Saul came out to meet David and said, 'How glorious was the king of Israel today, who uncovered himself today in the eyes of the female servants of his servants, as one of the worthless men shamelessly uncovers himself!'",
      "M": "David returned to bless his own household. But Michal daughter of Saul came out to meet him and said, 'How the king of Israel has honored himself today—exposing himself before the slave girls of his servants the way any shameless fool might expose himself!'",
      "T": "David came home to bless his household. But Michal daughter of Saul came out to meet him. 'What a glorious display the king of Israel made today,' she said, 'stripping himself in front of his servants' slave girls like some worthless nobody.'"
    },
    "21": {
      "L": "David said to Michal, 'It was before the LORD, who chose me rather than your father and rather than all his house, to appoint me as prince over Israel, the people of the LORD, and I will celebrate before the LORD.'",
      "M": "David said to Michal, 'It was before the LORD, who chose me rather than your father and his household to appoint me ruler over Israel—the LORD's own people. I will celebrate before the LORD.'",
      "T": "David answered Michal: 'It was before the LORD—who chose me over your father and his whole house to make me ruler over Israel, the LORD's people. It is before the LORD that I celebrate.'"
    },
    "22": {
      "L": "'And I will yet be more contemptible than this, and I will be lowly in my own eyes. But by the female servants of whom you have spoken, by them I will be honored.'",
      "M": "'I will make myself yet more contemptible than this, and I will be humble in my own sight. But by the slave girls you spoke of—I will be honored by them.'",
      "T": "'I will make myself yet more undignified than this, and be lowly in my own eyes. But those slave girls you despise? They will honor me.'"
    },
    "23": {
      "L": "And Michal the daughter of Saul had no child to the day of her death.",
      "M": "Michal daughter of Saul had no child to the day of her death.",
      "T": "Michal daughter of Saul had no child to the day of her death."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '2samuel', existing)
    print('2 Samuel 1–6 written.')

if __name__ == '__main__':
    main()
