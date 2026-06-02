"""
MKT 1 Samuel chapters 25–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1samuel-25-30.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M); "the LORD" in T — small-caps convention maintained from prior scripts.
- H430 (אֱלֹהִים): "God" throughout; EXCEPT 28:13 where elohim is used for the apparition the medium
  sees — there rendered "a divine figure/divine being" (L: "divine beings", M: "a divine figure",
  T: "an otherworldly figure") since the plural elohim here denotes the supernatural, not the deity.
- H5315 (נֶפֶשׁ): "soul" in L; "life" in M/T where it means "life/self." In 25:29 the poetic phrase
  "bound in the bundle of the living" is preserved in all tiers but glossed differently: L "soul",
  M "life", T surfaces the full image.
- H5037 (נָבָל): Both the proper name Nabal and the word for "fool/worthless one." In 25:25 T
  explicitly surfaces the name-meaning: "Nabal — Fool — is his name and foolishness his nature."
- H2617 (חֶסֶד): Not prominent in these chapters as a divine attribute; where it appears (26:23
  re: David's conduct) it is rendered "faithfulness" (L), "loyal faithfulness" (M/T) — covenantal
  fidelity in the context of honoring the LORD's anointed.
- H4428 (מלך): "king" throughout all tiers.
- H5234 (נָגִיד): Not in these chapters; H5057 (nagid) from prior scripts not needed here.
- H178 (ʾôb): "familiar spirit" in 28 — L "medium/who had a familiar spirit", M "medium",
  T "woman who could summon the dead/the ghost." The woman at Endor is described as ba'alat-ôb,
  "mistress of the ob-spirit."
- H3049 (yiddeoni): "necromancer/wizard" alongside H178; L "necromancers", M "mediums and
  necromancers", T "those who consult the dead."
- H646 (ʾêphôd): "ephod" retained in all tiers — a priestly object used for divine inquiry.
- H5036 (nābāl): The adjective "foolish/churlish" — rendered "churlish" (L), "harsh" (M),
  "brutish" (T) in 25:3.
- Achish (Philistine king): swears "as the LORD lives" in 29:6 — a Philistine using the Israelite
  covenant formula; T surfaces the irony.
- 25:26 divine passive: "the LORD has withheld you" — God is the active restrainer; surfaces in T.
- 28:17 "torn the kingdom": aorist-equivalent — complete, decisive act; rendered as past perfect
  in M/T.
- 30:6 "David strengthened himself in the LORD his God": key spiritual turning point; T gives it
  fuller weight.
- OT echo: 25:29 "bundle of the living" echoes later use in Jewish memorial prayer (El Malei
  Rachamim); T gestures toward the enduring theological resonance.
- Honor-shame: Nabal's refusal (ch 25) and Abigail's intercession operate on honor-shame dynamics;
  T surfaces them. David's forbearance toward Saul (ch 26) is an honor act. The Philistine lords'
  suspicion of David (ch 29) reflects patron-client anxieties.
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
  "25": {
    "1": {
      "L": "And Samuel died; and all Israel gathered and lamented him and buried him in his house at Ramah. And David arose and went down to the wilderness of Paran.",
      "M": "Samuel died, and all Israel gathered to mourn him and buried him at his home in Ramah. Then David set out and went down to the wilderness of Paran.",
      "T": "Samuel died. All Israel gathered to mourn and buried him at his home in Ramah. With Israel's judge gone, David moved further south into the wilderness of Paran—a man without a protector in a dangerous land."
    },
    "2": {
      "L": "And there was a man in Maon whose property was in Carmel, and the man was very great; and he had three thousand sheep and a thousand goats; and he was shearing his sheep in Carmel.",
      "M": "There was a man in Maon whose property was in Carmel—a very wealthy man with three thousand sheep and a thousand goats. He was at Carmel shearing his sheep.",
      "T": "In Maon, a man of great wealth had his grazing estates at Carmel—three thousand sheep and a thousand goats. He was there at the shearing, a time of celebration and prosperity."
    },
    "3": {
      "L": "The name of the man was Nabal and the name of his wife Abigail; the woman was of good understanding and beautiful in form, but the man was churlish and evil in his doings; and he was a Calebite.",
      "M": "His name was Nabal and his wife's name was Abigail. The woman had good understanding and was beautiful, but the man was harsh and wicked in his conduct—a Calebite.",
      "T": "His name was Nabal—Fool—and his character matched his name: harsh, wicked in his dealings, a Calebite of Caleb's lineage. His wife Abigail was his precise opposite: a woman of keen intelligence and striking beauty."
    },
    "4": {
      "L": "David heard in the wilderness that Nabal was shearing his sheep.",
      "M": "David heard in the wilderness that Nabal was shearing his sheep.",
      "T": "Word reached David in the wilderness that Nabal was holding a shearing—the customary occasion for generosity and feasting."
    },
    "5": {
      "L": "David sent ten young men, and David said to the young men, Go up to Carmel and go to Nabal and greet him in my name.",
      "M": "David sent ten young men and instructed them, 'Go up to Carmel, find Nabal, and greet him in my name.'",
      "T": "David sent ten young men with instructions: 'Go up to Carmel, find Nabal, and bring him my greetings in proper form.'"
    },
    "6": {
      "L": "And thus shall you say to him who lives: Peace be to you, and peace to your house, and peace to all that you have.",
      "M": "Say this to him: 'Long life to you! Peace to you, peace to your household, and peace to all that you have!'",
      "T": "The greeting was to be: 'Long life to you and yours! May all be well with you—you, your household, everything you own.'"
    },
    "7": {
      "L": "And now I have heard that you have shearers; now your shepherds were with us, and we did not harm them, nor did they miss anything all the time they were in Carmel.",
      "M": "I hear that you are shearing. Your shepherds have been with us, and we have not harassed them or taken anything from them all the time they were at Carmel.",
      "T": "'I hear you're shearing. Know this: your shepherds were among us in the wilderness, and we never harmed them—not a single thing went missing the entire time they were with us at Carmel.'"
    },
    "8": {
      "L": "Ask your young men and they will tell you. Therefore let my young men find favor in your eyes, for we come on a feast day; please give whatever you have at hand to your servants and to your son David.",
      "M": "Ask your servants—they will confirm it. So please let my young men find favor with you, since we come on a feast day. Give whatever you have at hand to your servants and to your son David.",
      "T": "'Ask your own servants—they'll confirm everything. We come at a feast time, so let my men find favor in your eyes. Give your servants whatever you can spare—and extend it to your son David.'"
    },
    "9": {
      "L": "When David's young men came, they spoke to Nabal all these words in David's name; and they waited.",
      "M": "David's young men arrived and delivered all these words to Nabal in David's name, then waited.",
      "T": "The men came to Nabal, delivered David's greeting and request word for word, and stood waiting for a response."
    },
    "10": {
      "L": "Nabal answered David's servants and said, Who is David? Who is the son of Jesse? There are many servants today who break away from their masters.",
      "M": "Nabal answered David's servants, 'Who is David? Who is the son of Jesse? These days there are many servants breaking away from their masters.'",
      "T": "Nabal's response was contemptuous. 'David? The son of Jesse? Who is he? There are plenty of runaway servants these days trying to make something of themselves.'"
    },
    "11": {
      "L": "Shall I take my bread and my water and my meat that I slaughtered for my shearers and give it to men who come from I do not know where?",
      "M": "Why should I take my bread, my water, and the meat I have slaughtered for my shearers and give it to men who come from who knows where?",
      "T": "'Why should I take food and drink I've prepared for my own men and hand it over to some strangers I've never heard of? I don't know you or your master.'"
    },
    "12": {
      "L": "So David's young men turned on their way and went back and came and told him all these words.",
      "M": "David's young men turned and went back, reporting everything Nabal had said.",
      "T": "The men returned to David and repeated every word of Nabal's insult."
    },
    "13": {
      "L": "David said to his men, Every man strap on his sword. And every man strapped on his sword; and David also strapped on his sword; and about four hundred men went up after David, while two hundred stayed by the baggage.",
      "M": "David ordered his men, 'Every man strap on your sword!' Every man strapped on his sword, and David did the same. About four hundred men went with David while two hundred remained with the supplies.",
      "T": "David's response was immediate and furious. 'Arm yourselves—every man!' They buckled on their swords, David included. Four hundred marched out with him; two hundred stayed to guard the supplies."
    },
    "14": {
      "L": "But one of Nabal's young men told Abigail, Nabal's wife, saying, Behold, David sent messengers from the wilderness to greet our master, and he railed at them.",
      "M": "But one of Nabal's servants told Abigail, Nabal's wife, 'David sent messengers from the wilderness to greet our master, and Nabal screamed insults at them.'",
      "T": "One of Nabal's servants, knowing what was coming, went straight to Abigail: 'David sent men from the wilderness with a respectful greeting for our master—and Nabal heaped abuse on them.'"
    },
    "15": {
      "L": "Yet the men were very good to us, and we were not harmed nor did we miss anything all the time we went about with them when we were in the field.",
      "M": "Those men were very good to us; we were not harmed and nothing went missing all the time we were in the field with them.",
      "T": "'Those men were outstanding—genuinely good to us. The whole time we were in the field together, we suffered no harm and not a thing went missing.'"
    },
    "16": {
      "L": "They were a wall to us both by night and by day all the time we were with them keeping the sheep.",
      "M": "They were a wall of protection for us, night and day, all the time we were with them tending the flock.",
      "T": "'They were like a wall around us—day and night—while we were out with the flock. We never had better protection.'"
    },
    "17": {
      "L": "Now therefore know and consider what you will do; for harm is determined against our master and against all his household, and he is such a worthless man that no one can speak to him.",
      "M": "So now think about what you are going to do, because harm is coming against our master and his entire household. He is such a difficult man that no one can reason with him.",
      "T": "'You need to act quickly—disaster is heading for our master and his whole household. But he's impossible to talk to—no one can get through to him. You're the only hope.'"
    },
    "18": {
      "L": "Then Abigail made haste and took two hundred loaves and two skins of wine and five dressed sheep and five seahs of parched grain and a hundred clusters of raisins and two hundred cakes of figs, and laid them on donkeys.",
      "M": "Abigail moved quickly. She took two hundred loaves of bread, two skins of wine, five dressed sheep, five seahs of parched grain, a hundred clusters of raisins, and two hundred fig cakes, and loaded them on donkeys.",
      "T": "Abigail wasted no time. She assembled a substantial gift: two hundred loaves, two skins of wine, five dressed sheep, five seahs of grain, a hundred raisin clusters, two hundred fig cakes—and loaded it all onto donkeys."
    },
    "19": {
      "L": "She said to her young men, Go on before me; behold, I am coming after you. But she did not tell her husband Nabal.",
      "M": "She told her servants, 'Go on ahead of me—I will follow you.' She said nothing to her husband Nabal.",
      "T": "'Go ahead,' she told her servants. 'I'll follow behind.' She said nothing to Nabal—there was no time, and no point."
    },
    "20": {
      "L": "She was riding on a donkey and coming down by a cover of the mountain; and behold, David and his men were coming down toward her, and she met them.",
      "M": "She was riding her donkey coming down the sheltered side of the mountain when she met David and his men coming toward her.",
      "T": "She came down the hidden side of the mountain on her donkey—and there was David, four hundred armed men coming straight at her, fury in their march."
    },
    "21": {
      "L": "Now David had said, Surely in vain I have guarded all that this fellow has in the wilderness, and nothing was missed of all that belonged to him; and he has returned me evil for good.",
      "M": "David had been saying, 'I have been guarding everything this man has in the wilderness for nothing—not a thing went missing—and he has repaid my good with evil!'",
      "T": "David was fuming as he marched: 'I've protected everything this man owns in the wilderness—not one loss on my watch—and this is how he repays it. Good for evil.'"
    },
    "22": {
      "L": "God do so to me, and more also, if I leave even one male of all who belong to Nabal by morning light.",
      "M": "He had sworn, 'May God deal with me, and more, if I leave even one male of Nabal's household alive by morning.'",
      "T": "He had taken an oath: 'God strike me down if I leave a single male of Nabal's household alive by dawn.'"
    },
    "23": {
      "L": "When Abigail saw David, she hurried and got down from the donkey and fell before David on her face and bowed to the ground.",
      "M": "When Abigail saw David, she quickly got down from her donkey and fell face down before him, bowing to the ground.",
      "T": "The moment Abigail saw David, she dismounted from her donkey, fell to the ground before him, and bowed low—a full act of homage."
    },
    "24": {
      "L": "She fell at his feet and said, On me alone, my lord, be the guilt; please let your servant speak in your ears and hear the words of your servant.",
      "M": "She fell at his feet and said, 'Let the blame fall on me alone, my lord. Please let your servant speak, and hear me out.'",
      "T": "'Let whatever guilt there is fall on me, my lord,' she said, still on the ground. 'Please—just hear me out. Let your servant speak.'"
    },
    "25": {
      "L": "Let not my lord regard this worthless man Nabal; for as his name is, so is he—Nabal is his name and folly is with him; but I your servant did not see the young men of my lord whom you sent.",
      "M": "Do not let my lord pay attention to this worthless man Nabal. His name means Fool, and folly is exactly what he is. I, your servant, did not see the young men my lord sent.",
      "T": "'Don't waste your wrath on Nabal—Fool is his name and it fits him perfectly. That's his character, not mine. I never saw the men you sent, my lord; I knew nothing of it until too late.'"
    },
    "26": {
      "L": "Now therefore, my lord, as the LORD lives and as your soul lives, since the LORD has held you back from coming to bloodshed and from saving yourself with your own hand, now let your enemies and those who seek to harm my lord be as Nabal.",
      "M": "And now, my lord, as the LORD lives and as you yourself live—the LORD has kept you from bloodshed and from taking vengeance with your own hand. Now let your enemies and those who seek to harm my lord become like Nabal.",
      "T": "'My lord, as the LORD lives and as you live—it is the LORD who has held you back from bloodshed today, kept your hand clean. Now let your enemies—all who seek your ruin—find Nabal's fate. The LORD will deal with them, not your sword.'"
    },
    "27": {
      "L": "And now this gift which your servant has brought to my lord, let it be given to the young men who follow in my lord's footsteps.",
      "M": "Let this gift that your servant has brought be distributed to the young men who follow my lord.",
      "T": "'Accept this gift—let it go to the young men who march with you. Consider it from a friend of your mission.'"
    },
    "28": {
      "L": "Please forgive the trespass of your servant; for the LORD will certainly make a sure house for my lord, because my lord fights the battles of the LORD, and evil has not been found in you all your days.",
      "M": "Please forgive your servant's offense. The LORD will certainly establish a lasting house for my lord, because my lord fights the LORD's battles, and no wrong has been found in you throughout your life.",
      "T": "'Please overlook my presumption, my lord. The LORD is going to build you an enduring house—I am certain of it—because you fight his battles and your conduct has been clean throughout. You carry no hidden evil.'"
    },
    "29": {
      "L": "If a man rises to pursue you and to seek your soul, the soul of my lord shall be bound in the bundle of the living in the care of the LORD your God; and the souls of your enemies he will sling out from the hollow of a sling.",
      "M": "If anyone rises to pursue you and take your life, the life of my lord will be kept safe and secure in the LORD your God's protection—like something precious bound in a bundle of the living. But the lives of your enemies he will hurl away like a stone from a sling.",
      "T": "'If someone comes to hunt you down, the LORD your God holds your life—bound up among the living, kept safe like a treasure in his care. Your enemies' lives? Those he flings away like a stone whipped from a sling—gone without a trace.'"
    },
    "30": {
      "L": "And when the LORD does for my lord according to all the good that he has spoken concerning you and appoints you prince over Israel,",
      "M": "When the LORD has done for my lord all the good he has promised and has appointed you ruler over Israel,",
      "T": "'And when the LORD fulfills every good thing he has spoken over you—when he establishes you as ruler over Israel—'"
    },
    "31": {
      "L": "this shall not be to you an occasion for grief or a stumbling block to my lord, for having shed blood without cause or for my lord having saved himself; and when the LORD deals well with my lord, then remember your servant.",
      "M": "—you will not have this on your conscience: the guilt of needless bloodshed or of taking vengeance yourself. And when the LORD has dealt well with my lord, please remember your servant.",
      "T": "'—you will not carry the weight of needless blood, no grievance from self-willed vengeance. Your hands will be clean when you take the throne. And when the LORD has been good to you, my lord—remember me.'",
    },
    "32": {
      "L": "And David said to Abigail, Blessed be the LORD God of Israel who sent you this day to meet me!",
      "M": "David said to Abigail, 'Blessed be the LORD, the God of Israel, who sent you today to meet me!'",
      "T": "David's anger broke. 'Blessed be the LORD, the God of Israel, who sent you to meet me today!'"
    },
    "33": {
      "L": "And blessed be your discernment, and blessed be you who have kept me this day from coming to bloodshed and from saving myself by my own hand.",
      "M": "Blessed is your good judgment, and blessed are you yourself—you have kept me from coming to bloodshed today and from taking vengeance with my own hand.",
      "T": "'And blessed be your wisdom—blessed be you—for stopping me from bloodshed and self-willed vengeance. What you have done today is no small thing.'"
    },
    "34": {
      "L": "Nevertheless, as the LORD God of Israel lives, who has restrained me from harming you, unless you had hurried and come to meet me, surely by morning light there would not have been left to Nabal even one male.",
      "M": "For truly, as the LORD God of Israel lives, who has held me back from harming you, if you had not come quickly to meet me, not one male of Nabal's household would have been left alive by morning.",
      "T": "'As the LORD God of Israel lives—the one who kept my hand back—if you had not come when you did, not a man of Nabal's household would have seen dawn. You came just in time.'"
    },
    "35": {
      "L": "So David received from her hand what she had brought him and said to her, Go up in peace to your house; see, I have listened to your voice and have granted your petition.",
      "M": "David accepted from her hand what she had brought and said, 'Go home in peace. I have heard your voice and granted your request.'",
      "T": "David received her gifts and stood her down with words of honor: 'Go home in peace. I have heard you. Your petition is granted.'"
    },
    "36": {
      "L": "And Abigail came to Nabal, and behold, he was holding a feast in his house like the feast of a king; and Nabal's heart was merry within him, for he was very drunk; so she told him nothing at all until the morning light.",
      "M": "Abigail returned to Nabal, and there he was, feasting in his house like a king. He was in high spirits—very drunk—so she said nothing to him until morning.",
      "T": "She came home to find Nabal hosting a feast fit for a king—drunk and celebrating, completely unaware of how close death had come to every man in his household. She held her peace until morning."
    },
    "37": {
      "L": "In the morning, when the wine had gone out of Nabal, his wife told him these things, and his heart died within him and he became like a stone.",
      "M": "In the morning, when Nabal had sobered up, his wife told him everything. His heart failed him and he became like stone.",
      "T": "In the morning when the wine was gone and his head was clear, Abigail told him everything. The blood drained from him. His heart stopped—or nearly—and he sat there like stone."
    },
    "38": {
      "L": "About ten days later the LORD struck Nabal and he died.",
      "M": "About ten days later the LORD struck Nabal, and he died.",
      "T": "Ten days later, the LORD struck Nabal dead. The fool had met his end—not by David's sword but by the hand of God."
    },
    "39": {
      "L": "When David heard that Nabal was dead, he said, Blessed be the LORD who has avenged the insult I received from Nabal's hand and has kept his servant from evil. The LORD has returned Nabal's evil on his own head. And David sent and spoke to Abigail, to take her as his wife.",
      "M": "David heard that Nabal was dead and said, 'Blessed be the LORD, who has avenged the insult I received at Nabal's hand and kept his servant from doing evil. The LORD has repaid Nabal's wickedness on his own head.' Then David sent word to Abigail, proposing to take her as his wife.",
      "T": "When word came that Nabal was dead, David said: 'Blessed be the LORD, who has vindicated me against Nabal's insult and kept me from taking it into my own hands. The LORD settled the account.' Then he sent a marriage proposal to Abigail."
    },
    "40": {
      "L": "When David's servants came to Abigail at Carmel, they spoke to her, saying, David has sent us to you to take you to him as his wife.",
      "M": "David's servants came to Abigail at Carmel and said, 'David has sent us to take you to him as his wife.'",
      "T": "The messengers found Abigail at Carmel. 'David has sent us. He wants to take you as his wife.'"
    },
    "41": {
      "L": "She arose and bowed with her face to the ground and said, Behold, your servant is a maidservant to wash the feet of the servants of my lord.",
      "M": "She arose, bowed to the ground, and said, 'Your servant is a maidservant ready to wash the feet of my lord's servants.'",
      "T": "She rose, bowed to the ground, and replied with deliberate humility: 'I am your lord's servant—ready to wash the feet of his servants.' She accepted."
    },
    "42": {
      "L": "Abigail hurried and arose and rode on a donkey with five girls who attended her; she went after the messengers of David and became his wife.",
      "M": "Abigail rose quickly, mounted her donkey with five of her serving women, and followed David's messengers. She became his wife.",
      "T": "Abigail wasted no time. She mounted her donkey with five attendants and rode to David's messengers. She became his wife."
    },
    "43": {
      "L": "David also took Ahinoam of Jezreel; and both of them became his wives.",
      "M": "David had also taken Ahinoam of Jezreel; both women were his wives.",
      "T": "David had also married Ahinoam of Jezreel; he now had two wives."
    },
    "44": {
      "L": "But Saul had given Michal, David's wife, to Palti son of Laish who was from Gallim.",
      "M": "Meanwhile Saul had given David's wife Michal to Palti son of Laish, who was from Gallim.",
      "T": "Back in Gibeah, Saul had given David's first wife Michal to Palti son of Laish from Gallim—an act of political spite, erasing the bond between David and the royal household."
    }
  },
  "26": {
    "1": {
      "L": "And the Ziphites came to Saul at Gibeah, saying, Is not David hiding himself on the hill of Hachilah before the Jeshimon?",
      "M": "The Ziphites came to Saul at Gibeah and said, 'Isn't David hiding on the hill of Hachilah, east of the Jeshimon?'",
      "T": "The Ziphites betrayed David's location again, coming to Saul at Gibeah: 'David is hiding on Hachilah's ridge, east of the Jeshimon.'"
    },
    "2": {
      "L": "Saul arose and went down to the wilderness of Ziph with three thousand chosen men of Israel to seek David in the wilderness of Ziph.",
      "M": "Saul set out with three thousand specially chosen Israelite soldiers to hunt for David in the wilderness of Ziph.",
      "T": "Saul mobilized three thousand of his best men and marched south into the wilderness of Ziph after David."
    },
    "3": {
      "L": "Saul camped on the hill of Hachilah by the road before the Jeshimon; but David was staying in the wilderness. When he saw that Saul came after him into the wilderness,",
      "M": "Saul pitched camp on the hill of Hachilah along the road east of the Jeshimon. David was in the wilderness and saw that Saul had come after him.",
      "T": "Saul set up camp on Hachilah's ridge along the road. David, watching from the wilderness, saw Saul's army come in."
    },
    "4": {
      "L": "David sent out spies and learned that Saul had in very deed come.",
      "M": "David sent out scouts and confirmed that Saul had truly arrived.",
      "T": "David sent scouts to verify—yes, Saul himself had come."
    },
    "5": {
      "L": "Then David arose and came to the place where Saul had camped; and David saw the place where Saul lay, and Abner son of Ner the commander of his army. Saul lay within the camp enclosure, and the army was encamped around him.",
      "M": "David went to the site of Saul's camp and saw where Saul was sleeping—with Abner son of Ner, the army commander, at his side. Saul was lying in the center of the enclosure with the troops camped around him.",
      "T": "David reconnoitered the camp himself and located Saul's position: sleeping in the center of the encampment, Abner son of Ner beside him, the entire army ringing them."
    },
    "6": {
      "L": "Then David said to Ahimelech the Hittite and to Abishai son of Zeruiah, Joab's brother, saying, Who will go down with me to Saul into the camp? Abishai said, I will go down with you.",
      "M": "David said to Ahimelech the Hittite and to Abishai son of Zeruiah, Joab's brother, 'Who will go down into the camp with me to Saul?' Abishai said, 'I will.'",
      "T": "David turned to his men: 'Who will go into the camp with me to Saul?' Abishai—Joab's brother, a warrior of nerve—stepped forward. 'I'll go.'"
    },
    "7": {
      "L": "So David and Abishai went to the army by night; and there Saul lay sleeping within the camp enclosure with his spear stuck in the ground at his head; and Abner and the army lay around him.",
      "M": "David and Abishai moved through the army at night. Saul was lying asleep in the camp, his spear thrust into the ground at his head, with Abner and the soldiers sleeping around him.",
      "T": "They slipped through the sleeping army in the dark. Saul lay there—spear planted in the ground beside his head, Abner and the whole force sleeping around him. A perfect target."
    },
    "8": {
      "L": "Then Abishai said to David, God has delivered your enemy into your hand this day; now let me pin him to the earth with the spear at one stroke; I will not need a second.",
      "M": "Abishai whispered to David, 'God has handed your enemy over to you today! Let me pin him to the ground with his own spear—one thrust, that's all it will take.'",
      "T": "Abishai seized the moment. 'God has delivered him to you,' he whispered. 'One stroke. I'll pin him to the ground with his own spear and won't need a second.'"
    },
    "9": {
      "L": "But David said to Abishai, Do not destroy him! For who can put out his hand against the LORD's anointed and be guiltless?",
      "M": "David said, 'No—don't destroy him! Who can lay a hand on the LORD's anointed and not be guilty?'",
      "T": "'Don't touch him,' David said. 'No one can strike the LORD's anointed and come away clean.'"
    },
    "10": {
      "L": "David also said, As the LORD lives, the LORD will strike him down; or his day will come and he will die; or he will go down into battle and be swept away.",
      "M": "David continued, 'As the LORD lives, the LORD himself will strike him down—either his appointed time will come and he'll die naturally, or he'll fall in battle.'",
      "T": "'The LORD lives—and the LORD will deal with him in his own time. His day will come. He'll die naturally, or he'll fall in battle. But that judgment is the LORD's to make, not mine.'"
    },
    "11": {
      "L": "Far be it from me, in the LORD's sight, to put out my hand against the LORD's anointed! Now take the spear at his head and the water jug, and let us go.",
      "M": "The LORD forbid that I should stretch out my hand against the LORD's anointed. Now take the spear and the water jug from his head, and let's go.",
      "T": "'God forbid I lift my hand against the one the LORD anointed. Take the spear and the water jug from beside his head. That's all. We're leaving.'"
    },
    "12": {
      "L": "So David took the spear and the water jug from beside Saul's head, and they went away; no man saw it or knew it or woke up, for they were all asleep, for a deep sleep from the LORD had fallen on them.",
      "M": "David took the spear and the water jug from Saul's head, and they slipped away. No one saw them, no one knew, no one woke up—they were all in a deep sleep, for the LORD had put them into a heavy slumber.",
      "T": "David lifted the spear and the water jug from beside Saul's sleeping head, and they walked out. Not a soul stirred. No one saw. No one woke. The LORD had cast a deep sleep over the entire camp."
    },
    "13": {
      "L": "Then David crossed to the other side and stood on top of the mountain far off; a great distance was between them.",
      "M": "David crossed to the other side and stood on the top of a hill far away, a great distance between him and the camp.",
      "T": "David crossed to the far side and climbed the opposite hill—a wide valley between him and Saul's sleeping army."
    },
    "14": {
      "L": "And David called to the army and to Abner son of Ner, saying, Will you not answer, Abner? Then Abner answered and said, Who are you who calls to the king?",
      "M": "David shouted across to the troops and to Abner son of Ner, 'Abner! Are you going to answer?' Abner called back, 'Who are you, calling out to the king?'",
      "T": "David called across the valley: 'Abner! Wake up! Answer me, Abner!' Abner's voice came back, groggy and indignant: 'Who's calling for the king?'"
    },
    "15": {
      "L": "David said to Abner, Are you not a man? And who is your equal in Israel? Why then have you not guarded your lord the king? For one of the people came in to destroy the king your lord.",
      "M": "David called back, 'You are a man, aren't you? Who in Israel compares to you? So why haven't you guarded your lord the king? Someone came in to kill the king your lord.'",
      "T": "'Are you not the great Abner?' David called. 'Who is your equal in Israel? Then explain this: someone walked into your camp tonight to kill the king—and you never woke up. Some guard you are.'"
    },
    "16": {
      "L": "This thing that you have done is not good! As the LORD lives, you deserve death, you men—because you have not guarded your lord the LORD's anointed! And now see where the king's spear is and the water jug that was at his head!",
      "M": "'This is not good what you have done! As the LORD lives, you all deserve death for not guarding your lord, the LORD's anointed! Now look—where is the king's spear? Where is the water jug that was by his head?'",
      "T": "'What you have done is not good—it's a death-worthy failure! As the LORD lives, you men deserve to die for leaving the LORD's anointed unguarded. Look around you: where is the king's spear? Where is his water jug?'"
    },
    "17": {
      "L": "Saul recognized David's voice and said, Is that your voice, my son David? David said, It is my voice, my lord the king.",
      "M": "Saul recognized David's voice and called out, 'Is that your voice, David my son?' David answered, 'It is my voice, my lord the king.'",
      "T": "Saul's voice cut across the valley—he had recognized David. 'Is that you, David? My son?' David answered without flinching: 'It is, my lord the king.'"
    },
    "18": {
      "L": "He said, Why does my lord pursue his servant? For what have I done? What evil is in my hand?",
      "M": "David said, 'Why is my lord pursuing his servant? What have I done? What harm is in my hands?'",
      "T": "'Why do you hunt me, my lord? What have I done to you? What evil can you lay to my charge?'"
    },
    "19": {
      "L": "Now therefore please let my lord the king hear the words of his servant. If it is the LORD who has stirred you against me, let him accept an offering; but if it is men, cursed are they before the LORD! For they have driven me out this day so that I have no share in the heritage of the LORD, saying, Go serve other gods.",
      "M": "Please let my lord the king hear his servant out. If the LORD has moved you against me, may he accept an offering. But if men have done this, may they be cursed before the LORD! They have driven me away today so I have no portion in the LORD's inheritance—as if they were telling me to go worship other gods.",
      "T": "'Hear me out, my lord. If the LORD himself has moved you against me—then I will bring an offering and seek his face. But if it is men who have poisoned you against me—God curse them! Because what they have done is drive me from the LORD's land, from his people, as if to say: \"Go find another god to serve.\" To exile an Israelite is to cut him off from the LORD. That is what they have done to me.'"
    },
    "20": {
      "L": "Now therefore let not my blood fall to the earth away from the presence of the LORD; for the king of Israel has come out to seek a single flea, as when one hunts a partridge in the mountains.",
      "M": "Do not let my blood fall on the ground far from the LORD's presence. The king of Israel has come out to look for a single flea—like someone hunting a partridge in the hills.",
      "T": "'Do not let my blood soak into foreign ground, far from the LORD. The king of Israel has mobilized his army to hunt—what? A single flea. A partridge flushing in the hills. Is this what the king does with his time?'"
    },
    "21": {
      "L": "Then Saul said, I have sinned; return, my son David, for I will not harm you again because my life was precious in your sight this day; behold, I have played the fool and have made a great mistake.",
      "M": "Saul said, 'I have sinned. Come back, David my son—I will not harm you again because you held my life precious today. I have played the fool and made a terrible mistake.'",
      "T": "Saul broke. 'I have sinned. Come back to me, David—my son. I will not harm you again. You had my life in your hands tonight and you kept it precious. I have been a fool. A terrible, costly fool.'"
    },
    "22": {
      "L": "David answered and said, Here is the king's spear! Let one of the young men come over and take it.",
      "M": "David called back, 'Here is the king's spear! Send one of your men to come get it.'",
      "T": "'Here is your spear, my lord! Send someone to fetch it.' David was gracious in victory—but he was not coming back."
    },
    "23": {
      "L": "The LORD rewards every man for his righteousness and faithfulness; for the LORD gave you into my hand today, and I would not put out my hand against the LORD's anointed.",
      "M": "The LORD rewards every man for his righteousness and loyalty. The LORD handed you over to me today, and I would not lay a hand on the LORD's anointed.",
      "T": "'The LORD repays each man according to his righteousness and faithfulness—and the LORD himself put you into my hand tonight. I would not touch what the LORD has set apart. That is for him to judge, not me.'"
    },
    "24": {
      "L": "And as your life was precious in my sight today, so may my life be precious in the sight of the LORD, and may he deliver me from all distress.",
      "M": "Just as I valued your life today, may the LORD value my life and rescue me from all distress.",
      "T": "'I spared your life because it was precious to me. May the LORD count my life precious in return, and may he rescue me from every danger I face.'"
    },
    "25": {
      "L": "Then Saul said to David, Blessed be you, my son David! You will both do great things and will surely prevail. And David went his way, and Saul returned to his place.",
      "M": "Saul said to David, 'Blessed be you, my son David! You will accomplish great things and will surely succeed.' David went on his way, and Saul returned home.",
      "T": "Saul called across the valley one last time: 'Blessed are you, David my son. You will do great things—you will succeed.' Then the two men parted: David into the wilderness, Saul back to Gibeah. Each went his way."
    }
  },
  "27": {
    "1": {
      "L": "David said in his heart, Now I shall perish one day by the hand of Saul; there is nothing better for me than to escape to the land of the Philistines; then Saul will despair of seeking me any more in all the territory of Israel, and I shall escape out of his hand.",
      "M": "David thought to himself, 'I am going to die by Saul's hand one of these days. My best option is to escape into Philistia. Then Saul will stop searching for me throughout Israel, and I will be out of his reach.'",
      "T": "David's faith faltered. He reasoned it through in his heart: 'Saul will catch me eventually. My best chance of survival is to disappear into Philistine territory. Let Saul chase someone else—he'll give up on me, and I'll be beyond his reach.'"
    },
    "2": {
      "L": "So David arose and went over, he and the six hundred men who were with him, to Achish son of Maoch, king of Gath.",
      "M": "So David set out with his six hundred men and crossed over to Achish son of Maoch, king of Gath.",
      "T": "David acted on his decision. He and his six hundred men crossed the border into Philistine territory and presented themselves to Achish son of Maoch, king of Gath."
    },
    "3": {
      "L": "David lived with Achish at Gath, he and his men, each man with his household; David with his two wives, Ahinoam of Jezreel and Abigail the Carmelitess, the wife of Nabal.",
      "M": "David settled at Gath with Achish, he and his men, each with his household. David brought his two wives—Ahinoam of Jezreel and Abigail, the widow of Nabal of Carmel.",
      "T": "David and his six hundred settled in Gath under Achish's protection—each man with his family. David had his two wives with him: Ahinoam of Jezreel and Abigail, Nabal's widow."
    },
    "4": {
      "L": "When Saul was told that David had fled to Gath, he sought him no more.",
      "M": "When Saul heard that David had fled to Gath, he stopped searching for him.",
      "T": "News reached Saul that David was in Gath. The search ended. A man living among Israel's enemies was beyond reach—and beyond embarrassment."
    },
    "5": {
      "L": "And David said to Achish, If I have found favor in your eyes, let a place be given me in one of the country towns that I may live there; for why should your servant live in the royal city with you?",
      "M": "David said to Achish, 'If you are pleased with me, assign me a place in one of the country towns to live there. Why should your servant live in the royal city with you?'",
      "T": "David made a calculated request: 'If I've found favor with you, give me a town of my own in the countryside. Why should a servant like me take up space in the royal city?'"
    },
    "6": {
      "L": "So Achish gave him Ziklag that day; therefore Ziklag has belonged to the kings of Judah to this day.",
      "M": "Achish gave him Ziklag that day. That is why Ziklag has belonged to the kings of Judah to this day.",
      "T": "Achish gave him Ziklag—a grant of territory that would later pass to the Davidic kings. Ziklag belonged to the kings of Judah from that day forward."
    },
    "7": {
      "L": "And the time that David lived in the country of the Philistines was a year and four months.",
      "M": "David lived in Philistine territory for a year and four months.",
      "T": "David remained in Philistine country for a year and four months—living in exile from his own people."
    },
    "8": {
      "L": "Now David and his men went up and raided the Geshurites, the Girzites, and the Amalekites; for these were the inhabitants of the land from of old, from the approach to Shur as far as the land of Egypt.",
      "M": "David and his men would raid the Geshurites, the Girzites, and the Amalekites—peoples who had long inhabited the region from the direction of Shur toward Egypt.",
      "T": "David occupied his time raiding the Geshurites, Girzites, and Amalekites—ancient inhabitants of the Negeb between Shur and Egypt, enemies of Israel."
    },
    "9": {
      "L": "And David struck the land and did not leave a man or woman alive, and he took away the sheep, the oxen, the donkeys, the camels, and the clothing; and he came back to Achish.",
      "M": "Whenever David attacked a region he left no one alive—man or woman—taking the sheep, oxen, donkeys, camels, and clothing before returning to Achish.",
      "T": "David left no survivors—no witnesses. He took the livestock and goods and returned to Achish. The silence was deliberate."
    },
    "10": {
      "L": "And Achish would ask, Where have you raided today? And David would say, Against the Negeb of Judah, or against the Negeb of the Jerahmeelites, or against the Negeb of the Kenites.",
      "M": "Achish would ask, 'Where did you raid today?' And David would say, 'Against the Negeb of Judah,' or 'Against the Negeb of the Jerahmeelites,' or 'Against the Negeb of the Kenites.'",
      "T": "Achish would ask where they had been. David's answers were calculated deceptions: 'Against the Negeb of Judah,' or 'The Jerahmeelites,' or 'The Kenites'—all Israelite allies, none of whom he had actually attacked."
    },
    "11": {
      "L": "And David left neither man nor woman alive to bring back to Gath, thinking, Lest they tell about us and say, So David did. Such was his custom all the time he lived in the country of the Philistines.",
      "M": "David never brought back any prisoners to Gath; he thought, 'If survivors reached Gath, they would tell what David really did.' This was his regular practice throughout his time in Philistine territory.",
      "T": "No one was left alive to contradict the story. David knew what he was doing: survivors would blow his cover. So he left none. This was his pattern for the entire sixteen months."
    },
    "12": {
      "L": "And Achish trusted David, thinking, He has made himself utterly odious to his people Israel; therefore he will be my servant forever.",
      "M": "Achish completely trusted David, thinking, 'He has made himself utterly repulsive to his own people Israel; he will be my servant permanently.'",
      "T": "Achish was completely deceived. He believed David had burned his bridges with Israel—that his own people now despised him as a traitor. 'He is mine forever,' Achish thought. He was wrong."
    }
  },
  "28": {
    "1": {
      "L": "In those days the Philistines gathered their forces for war against Israel; and Achish said to David, Know for certain that you and your men will go out with me in the army.",
      "M": "In those days the Philistines gathered their forces to fight Israel. Achish told David, 'Understand clearly—you and your men are going out with me into battle.'",
      "T": "The Philistines were mustering for a major campaign against Israel. Achish summoned David: 'You and your men are with me on this one. No ambiguity.'"
    },
    "2": {
      "L": "David said to Achish, Very well! You shall know what your servant can do. And Achish said to David, Very well, then I will make you my bodyguard for life.",
      "M": "David said, 'Then you will see what your servant can do.' Achish replied, 'Good—I will appoint you as my permanent bodyguard.'",
      "T": "David gave nothing away: 'You'll see what I can do.' Achish, misreading the ambiguity as loyalty, replied: 'Then I'm making you my personal bodyguard—permanently.'"
    },
    "3": {
      "L": "Now Samuel had died, and all Israel had mourned him and buried him in Ramah, his own city. And Saul had put the mediums and the necromancers out of the land.",
      "M": "Samuel was dead—all Israel had mourned him and buried him in Ramah, his own city. Saul had previously expelled mediums and necromancers from the land.",
      "T": "The narrator pauses to remind us: Samuel was dead and buried in Ramah, mourned by all Israel. And Saul himself had once expelled every medium and necromancer from the land—an irony that is about to become devastating."
    },
    "4": {
      "L": "The Philistines assembled and came and camped at Shunem; and Saul gathered all Israel, and they camped at Gilboa.",
      "M": "The Philistines assembled and camped at Shunem; Saul gathered all Israel and camped at Gilboa.",
      "T": "The Philistine army set up at Shunem in the Jezreel Valley. Saul marshaled all Israel and camped on the slopes of Mount Gilboa across from them."
    },
    "5": {
      "L": "When Saul saw the Philistine army, he was afraid, and his heart trembled greatly.",
      "M": "Saul looked at the Philistine forces and was terrified—his heart shaking with dread.",
      "T": "Saul looked at what was facing him and the fear that seized him was beyond anything he had known. His heart shook."
    },
    "6": {
      "L": "When Saul inquired of the LORD, the LORD did not answer him, either by dreams or by Urim or by prophets.",
      "M": "Saul inquired of the LORD, but the LORD did not answer him—not through dreams, not through the Urim, not through prophets.",
      "T": "Saul turned to every legitimate channel—dreams, the Urim, the prophets. Silence. The LORD had stopped speaking to him. The weight of that silence was its own verdict."
    },
    "7": {
      "L": "Then Saul said to his servants, Seek out for me a woman who is a medium, that I may go to her and inquire of her. His servants said to him, There is a medium at Endor.",
      "M": "Saul told his servants, 'Find me a woman who is a medium, so I can go consult her.' His servants replied, 'There is a medium at Endor.'",
      "T": "In his desperation Saul turned to what he had forbidden. 'Find me a medium,' he told his servants. 'I need to consult one.' They knew of one—a woman at Endor who had escaped his purge."
    },
    "8": {
      "L": "So Saul disguised himself and put on other clothes and went, he and two men with him; they came to the woman by night and he said, Divine for me by the spirit and bring up for me whoever I shall name to you.",
      "M": "Saul disguised himself, changed his clothes, and went with two men to the woman at night. He said, 'Consult a spirit for me, and bring up whoever I tell you.'",
      "T": "Saul came at night in disguise, stripped of his royal clothing. He told her: 'Consult the dead for me. Bring up whoever I name.'"
    },
    "9": {
      "L": "The woman said to him, Surely you know what Saul has done, how he has cut off the mediums and the necromancers from the land. Why then are you laying a snare for my life to bring about my death?",
      "M": "The woman said, 'Surely you know what Saul has done—he has eliminated all the mediums and necromancers from the land. Why are you setting a trap for my life to get me killed?'",
      "T": "The woman was cautious. 'You know what Saul has done—he's purged every medium and necromancer from Israel. Why are you trying to get me killed?'"
    },
    "10": {
      "L": "Saul swore to her by the LORD, As the LORD lives, no punishment will come upon you for this thing.",
      "M": "Saul swore to her by the LORD, 'As the LORD lives, no punishment will come to you for this.'",
      "T": "Saul swore by the very name of the LORD he had been abandoned by: 'As the LORD lives, you will not be punished for this.' The irony was thick."
    },
    "11": {
      "L": "The woman said, Whom shall I bring up for you? He said, Bring up Samuel for me.",
      "M": "The woman asked, 'Who shall I bring up for you?' He answered, 'Bring up Samuel.'",
      "T": "'Who do you want?' she asked. 'Samuel,' he said. The prophet who had condemned him. The man he needed most."
    },
    "12": {
      "L": "When the woman saw Samuel, she cried out with a loud voice; and the woman said to Saul, Why have you deceived me? You are Saul!",
      "M": "When the woman saw Samuel, she cried out with a loud voice and said to Saul, 'Why did you deceive me? You are Saul!'",
      "T": "Something appeared—and the woman screamed. Whatever she expected, this was different. She turned on her client: 'You tricked me! You're Saul!'"
    },
    "13": {
      "L": "The king said to her, Do not be afraid; what do you see? The woman said to Saul, I see divine beings coming up out of the earth.",
      "M": "The king said, 'Do not be afraid. What do you see?' The woman said, 'I see a divine figure rising up from the earth.'",
      "T": "'Don't be afraid,' Saul said. 'What do you see?' She steadied herself: 'I see an otherworldly figure—coming up from the ground.'"
    },
    "14": {
      "L": "He said to her, What is his form? She said, An old man is coming up, and he is wrapped in a robe. And Saul knew it was Samuel, and he bowed with his face to the ground and did homage.",
      "M": "He asked, 'What does he look like?' She said, 'An old man, wrapped in a robe.' Saul knew it was Samuel and bowed with his face to the ground.",
      "T": "'What does he look like?' 'An old man, wearing a robe.' Saul knew. He fell on his face to the ground, full prostration before the prophet who had never stopped being his judge."
    },
    "15": {
      "L": "Then Samuel said to Saul, Why have you disturbed me by bringing me up? And Saul answered, I am in great distress; for the Philistines are fighting against me and God has turned away from me and answers me no more, either by prophets or by dreams; therefore I have called you, that you may make known to me what I shall do.",
      "M": "Samuel said to Saul, 'Why have you disturbed me by bringing me up?' Saul answered, 'I am in desperate straits. The Philistines are fighting me, and God has turned away and no longer answers me—not by prophets, not by dreams. So I called you to tell me what to do.'",
      "T": "Samuel's voice, from wherever he had come: 'Why have you disturbed me?' Saul poured out his desperation: 'I have no one else. The Philistines are at my throat, God has abandoned me—no prophets, no dreams, nothing. I had to call you. Tell me what to do.'"
    },
    "16": {
      "L": "Samuel said, Why then do you ask me, since the LORD has turned from you and has become your adversary?",
      "M": "Samuel replied, 'Why ask me? The LORD has turned away from you and become your adversary.'",
      "T": "Samuel gave no comfort. 'Why are you asking me? The LORD has left you. He is your adversary now—not your helper.'"
    },
    "17": {
      "L": "The LORD has done to you as he spoke by me; for the LORD has torn the kingdom out of your hand and given it to your neighbor David,",
      "M": "The LORD has done to you exactly what he said through me—he has torn the kingdom out of your hand and given it to your neighbor David.",
      "T": "'The LORD has done exactly what he announced through me. He has torn the kingdom from your hand—finally, completely—and given it to David, your neighbor.'"
    },
    "18": {
      "L": "because you did not obey the voice of the LORD and did not carry out his fierce anger against Amalek; therefore the LORD has done this thing to you this day.",
      "M": "Because you did not obey the LORD and did not carry out his fierce judgment against Amalek—that is why the LORD has done this to you today.",
      "T": "'The reason is not mysterious. You disobeyed the LORD's command against Amalek—you did not execute his full judgment. That act of disobedience is why you are here, now, at the end.'"
    },
    "19": {
      "L": "Moreover the LORD will give Israel also with you into the hand of the Philistines; and tomorrow you and your sons shall be with me. The LORD will give the army of Israel into the hand of the Philistines.",
      "M": "The LORD will hand Israel along with you over to the Philistines. Tomorrow you and your sons will be with me. The LORD will give Israel's army into the Philistines' hand.",
      "T": "'And tomorrow: Israel falls to the Philistines. You and your sons will be dead by tomorrow night—you will be here where I am. The army of Israel will be broken.'"
    },
    "20": {
      "L": "Then Saul immediately fell full length on the ground, filled with fear because of Samuel's words; and there was no strength in him, for he had eaten nothing all day and all night.",
      "M": "Saul immediately fell full length on the ground, overwhelmed with fear at Samuel's words. There was no strength left in him—he had eaten nothing all day or all night.",
      "T": "Saul collapsed—full length on the ground. The fear that broke him was total. He had eaten nothing all day, all night; there was nothing left in him. Samuel's words had emptied him out."
    },
    "21": {
      "L": "The woman came to Saul, and seeing that he was badly frightened, she said to him, Look, your servant has obeyed you; I have taken my life in my hands and have listened to what you said to me.",
      "M": "The woman came to Saul, and seeing how shaken he was, she said, 'Look, your servant has done what you asked. I put my life at risk to obey you.'",
      "T": "The woman came to him. She could see the state he was in—king of Israel lying on the floor in a stranger's house. 'I obeyed you,' she said gently. 'I risked my life to do what you asked.'"
    },
    "22": {
      "L": "Now therefore also listen to the voice of your servant; let me set before you a piece of bread, that you may eat and have strength when you go on your way.",
      "M": "Now please listen to me—let me set some food before you so you have the strength to go on your way.",
      "T": "'Now let me take care of you. Eat something—you need strength for the road ahead.'"
    },
    "23": {
      "L": "He refused and said, I will not eat. But his servants, together with the woman, urged him; and he listened to their voice. So he arose from the earth and sat on the bed.",
      "M": "He refused, saying 'I will not eat.' But his servants and the woman pressed him until he gave in. He got up from the ground and sat on the bed.",
      "T": "Saul refused at first. But his servants and the woman kept urging him, and finally he let them help him up from the floor and onto the bed."
    },
    "24": {
      "L": "The woman had a fatted calf in the house, and she quickly slaughtered it; and she took flour, kneaded it, and baked unleavened bread from it.",
      "M": "The woman had a fattened calf in the house; she quickly slaughtered it, took flour, kneaded it, and baked unleavened bread.",
      "T": "The woman killed a fatted calf—generous hospitality for a terrified king—and baked unleavened bread from flour she kneaded by hand. It was a mercy."
    },
    "25": {
      "L": "She brought it before Saul and his servants, and they ate. Then they arose and went away that night.",
      "M": "She set the food before Saul and his servants, and they ate. Then they rose and left that same night.",
      "T": "She put the food before him and his men, and they ate. Then they went out into the dark. Saul left Endor knowing what the next day would bring."
    }
  },
  "29": {
    "1": {
      "L": "The Philistines gathered all their forces at Aphek; and Israel was encamped by the spring that is in Jezreel.",
      "M": "The Philistines assembled all their forces at Aphek while Israel was encamped by the spring at Jezreel.",
      "T": "The Philistine army massed at Aphek. Israel was camped beside the spring at Jezreel—the two armies converging toward Gilboa."
    },
    "2": {
      "L": "As the lords of the Philistines were passing on by hundreds and by thousands, David and his men were passing on in the rear with Achish.",
      "M": "The Philistine lords were passing in review by hundreds and thousands. David and his men were marching at the rear with Achish.",
      "T": "The Philistine lords paraded their forces in review—by hundreds, by thousands. And there, at the rear with Achish, marched David and his men."
    },
    "3": {
      "L": "The Philistine commanders said, What are these Hebrews doing here? Achish said to the commanders, Is this not David, the servant of Saul king of Israel? He has been with me these days and years, and I have found no fault in him from the day he deserted to me to this day.",
      "M": "The Philistine commanders objected, 'What are these Hebrews doing here?' Achish defended him: 'Is this not David, who served Saul king of Israel? He has been with me for years now—I have found nothing against him since the day he came over to me.'",
      "T": "The Philistine commanders pulled Achish aside: 'What are Hebrews doing in this army?' Achish vouched for David: 'That's David—the man who defected from Saul of Israel. He's been with me for over a year. I have found nothing against him—not once.'"
    },
    "4": {
      "L": "But the commanders of the Philistines were angry with him and said to him, Send the man back so that he returns to the place you assigned him. He shall not go down with us into battle, lest in the battle he become an adversary to us. For how could he win back his lord's favor? Would it not be with the heads of the men here?",
      "M": "But the commanders were angry and said, 'Send him back to the place you gave him—he must not march with us into battle. He could turn against us in the fight. How better to win back his lord's favor than with our heads?'",
      "T": "The commanders were not persuaded. 'Send him back. He has no business in this battle. Once swords are drawn, what's to stop him switching sides? And what better gift to offer Saul than Philistine heads? Send him home.'"
    },
    "5": {
      "L": "Is this not David, of whom they sing to one another in dances, Saul has struck down his thousands, and David his ten thousands?",
      "M": "Is this not the David they sing about in their dances: 'Saul has killed his thousands, and David his ten thousands'?",
      "T": "'Is this not the same David? The one the Israelite women sang about: Saul—a thousand; David—ten thousand? Do you trust this man in your army?'"
    },
    "6": {
      "L": "Then Achish called David and said to him, As the LORD lives, you have been honest and it seems good to me that you should march out and march in with me in the campaign, for I have found nothing wrong in you from the day you came to me to this day; nevertheless the lords do not approve of you.",
      "M": "Achish called David and said, 'As the LORD lives, you have been trustworthy—I would be glad to have you in the campaign, for I have found nothing wrong with you since the day you came to me. But the lords will not allow it.'",
      "T": "Achish called David privately. He swore by Israel's own God—a Philistine king invoking the LORD—to convey his sincerity: 'You have been nothing but loyal. I would take you into battle gladly. But the lords have spoken. They won't have you.'"
    },
    "7": {
      "L": "Return now, and go in peace, that you may not displease the lords of the Philistines.",
      "M": "So go back now in peace, so as not to offend the Philistine lords.",
      "T": "'Go home in peace. Don't give the lords a reason to move against you.'"
    },
    "8": {
      "L": "David said to Achish, But what have I done? What have you found in your servant from the day I came before you until this day, that I should not go and fight against the enemies of my lord the king?",
      "M": "David protested to Achish, 'But what have I done? What have you found against me from the day I came to you until now, that I shouldn't fight against the enemies of my lord the king?'",
      "T": "David played his part with conviction: 'What have I done? You've found nothing against me—not once. Why can't I go and fight the enemies of my lord the king?' The protest was masterful. His true feelings about fighting Israel he kept entirely hidden."
    },
    "9": {
      "L": "Achish answered David and said, I know that you are as pleasing to me as an angel of God; yet the Philistine commanders have said, He shall not go up with us to battle.",
      "M": "Achish replied, 'I know—you are as good in my sight as a messenger from God. But the Philistine commanders have decided: you are not going into this battle.'",
      "T": "'I know your worth,' Achish said. 'In my eyes you're beyond reproach—like a messenger from God. But the commanders have decided, and I cannot overrule them. You don't march.'"
    },
    "10": {
      "L": "So rise early in the morning, you and the servants of your lord who came with you, and go to the place I assigned to you. Do not harbor any evil thought, for you are good in my sight. Set out early in the morning when you have light.",
      "M": "So rise early in the morning—you and your lord's servants who came with you—and return to the place I assigned you. Hold no ill will, for you are good in my sight. Set out at first light.",
      "T": "'At dawn, take your men and go back to Ziklag. No hard feelings—you are honorable in my eyes. Leave at first light.'"
    },
    "11": {
      "L": "So David arose early, he and his men, to depart in the morning to return to the land of the Philistines; and the Philistines went up to Jezreel.",
      "M": "David and his men rose early and set out in the morning to return to Philistia, while the Philistines marched up to Jezreel.",
      "T": "David and his men rose at dawn and turned south toward Ziklag. The Philistines continued north toward Jezreel and their appointment with Saul."
    }
  },
  "30": {
    "1": {
      "L": "When David and his men came to Ziklag on the third day, the Amalekites had raided the Negeb and Ziklag; they had attacked Ziklag and burned it with fire.",
      "M": "When David and his men arrived at Ziklag on the third day, they found that the Amalekites had raided the Negeb and Ziklag—they had attacked Ziklag and burned it to the ground.",
      "T": "Three days' march south, David and his men came home to Ziklag—and found it in ashes. The Amalekites had swept through the Negeb and hit Ziklag hard, burning it to the ground."
    },
    "2": {
      "L": "They had taken captive the women and all who were in it, both small and great; they killed no one but carried them off and went their way.",
      "M": "They had taken all the women and everyone else captive—young and old alike—killing no one, but carrying them off as they went.",
      "T": "Everyone was gone—women, children, the old. The Amalekites had taken them all captive. No bodies: they wanted slaves, not a massacre."
    },
    "3": {
      "L": "When David and his men came to the city and found it burned with fire and their wives and their sons and their daughters taken captive,",
      "M": "When David and his men came to the city, they found it burned with fire, and their wives, sons, and daughters taken captive.",
      "T": "David and his men walked into the ruins—fire, ash, emptiness. Their wives, their children: taken."
    },
    "4": {
      "L": "David and the people who were with him raised their voices and wept, until they had no more strength to weep.",
      "M": "David and his men wept aloud until they had no more strength to weep.",
      "T": "They wept. All of them—David and every one of his six hundred men—until there were no more tears and no more strength."
    },
    "5": {
      "L": "David's two wives also had been taken captive: Ahinoam of Jezreel and Abigail the widow of Nabal of Carmel.",
      "M": "David's two wives had also been taken captive—Ahinoam of Jezreel and Abigail the widow of Nabal of Carmel.",
      "T": "David's own wives were among the captives—Ahinoam of Jezreel and Abigail, Nabal's widow."
    },
    "6": {
      "L": "And David was greatly distressed, for the people spoke of stoning him, because the soul of all the people was bitter, each for his sons and daughters; but David strengthened himself in the LORD his God.",
      "M": "David was in great distress, for the people were talking of stoning him—all of them bitter over the loss of their sons and daughters. But David strengthened himself in the LORD his God.",
      "T": "David faced the worst possible moment: his men's grief had curdled into rage, and the talk was of stoning him. He had no human support. He had no Samuel to consult. But David found something Saul had not—he turned to the LORD his God and drew strength from him."
    },
    "7": {
      "L": "And David said to Abiathar the priest, the son of Ahimelech, Please bring me the ephod. So Abiathar brought the ephod to David.",
      "M": "David said to Abiathar the priest, son of Ahimelech, 'Bring me the ephod.' Abiathar brought the ephod to David.",
      "T": "He called for Abiathar the priest: 'Bring the ephod.' Abiathar brought it. This was what Saul had refused to do at Gilgal and could not do at Endor—David would inquire of the LORD properly."
    },
    "8": {
      "L": "And David inquired of the LORD, Shall I pursue after this raiding party? Shall I overtake them? He answered him, Pursue, for you shall surely overtake and you shall surely rescue.",
      "M": "David inquired of the LORD, 'Should I pursue this raiding party? Will I overtake them?' The LORD answered him, 'Pursue—you will certainly overtake them and certainly rescue the captives.'",
      "T": "David asked the LORD directly: 'Should I go after them? Will I catch them?' The answer came back clear: 'Pursue. You will catch them. You will get everyone back.'"
    },
    "9": {
      "L": "So David set out, he and the six hundred men who were with him, and they came to the brook Besor, where those who were left behind remained.",
      "M": "David set out with his six hundred men and came to the brook Besor, where some stayed behind.",
      "T": "David moved out immediately with all six hundred men. They pushed hard and reached the brook Besor—and there some men broke."
    },
    "10": {
      "L": "But David and four hundred men continued the pursuit; two hundred men stayed, who were too exhausted to cross the brook Besor.",
      "M": "David went on with four hundred men; the other two hundred were too exhausted to cross the Besor and stayed behind.",
      "T": "Two hundred could go no further—spent, unable to cross the brook. David pressed on with four hundred."
    },
    "11": {
      "L": "They found an Egyptian in the open country and brought him to David; and they gave him bread and he ate, and they gave him water to drink.",
      "M": "They came across an Egyptian in the field and brought him to David. They gave him bread to eat and water to drink.",
      "T": "Out in the open country they found an Egyptian man—collapsed, abandoned. They brought him to David, gave him food and water."
    },
    "12": {
      "L": "And they gave him a piece of fig cake and two clusters of raisins; and when he had eaten, his spirit revived, for he had not eaten any food or drunk any water for three days and three nights.",
      "M": "They gave him a piece of fig cake and two clusters of raisins. When he had eaten, his strength returned, for he had not eaten or drunk anything for three days and three nights.",
      "T": "Fig cake and raisins—simple food—and the man came back to life. He had had nothing for three days and nights. Providence had put him exactly where David's men would find him."
    },
    "13": {
      "L": "David said to him, To whom do you belong? And where are you from? He said, I am a young man of Egypt, servant to an Amalekite; my master left me behind when I became ill three days ago.",
      "M": "David asked him, 'Who are you? Where are you from?' He answered, 'I am Egyptian, a slave of an Amalekite. My master abandoned me when I fell sick three days ago.'",
      "T": "'Who are you? Where do you come from?' David asked. 'I am Egyptian—a slave of an Amalekite. He left me behind when I got sick. Three days ago.'"
    },
    "14": {
      "L": "We raided the Negeb of the Cherethites, and what belongs to Judah, and the Negeb of Caleb; and we burned Ziklag with fire.",
      "M": "We raided the Negeb of the Cherethites, the Negeb of Judah, and the Negeb of Caleb, and we burned Ziklag.',",
      "T": "'We raided the Cherethite Negeb, Judah's Negeb, Caleb's Negeb—and we burned Ziklag.'"
    },
    "15": {
      "L": "And David said to him, Will you take me down to this raiding party? He said, Swear to me by God that you will not kill me or hand me over to my master, and I will take you down to this raiding party.",
      "M": "David asked, 'Can you take me to this raiding party?' He replied, 'Swear to me by God that you won't kill me or hand me back to my master, and I will take you to them.'",
      "T": "David saw what he had. 'Can you lead me to them?' The Egyptian had his own terms: 'Swear to me by God—you won't kill me and you won't hand me back to my master. Then I'll take you straight to them.'"
    },
    "16": {
      "L": "He led them down, and there they were, spread over all the land, eating and drinking and celebrating, because of all the great spoil they had taken from the land of the Philistines and from the land of Judah.",
      "M": "He led them to the Amalekites, who were spread out across the land, eating, drinking, and celebrating because of the enormous plunder they had taken from the Philistine and Judahite territories.",
      "T": "The Egyptian led them there. The Amalekites were scattered across the landscape—feasting, drinking, celebrating. The plunder from Philistia and Judah was spread around them. They had no idea what was coming."
    },
    "17": {
      "L": "And David struck them from twilight until the evening of the next day; and not a man of them escaped except four hundred young men who rode on camels and fled.",
      "M": "David attacked them from twilight until the evening of the following day. Not one of them escaped except four hundred young men who mounted camels and fled.",
      "T": "David attacked at dusk and fought through to the following evening—a battle that lasted more than twenty-four hours. Every Amalekite was killed or captured, except four hundred young men who mounted camels and escaped into the desert."
    },
    "18": {
      "L": "And David recovered everything the Amalekites had taken; and David rescued his two wives.",
      "M": "David recovered everything the Amalekites had taken, including his two wives.",
      "T": "David got back everything. Every person. Every possession. Including Ahinoam and Abigail—his two wives, safe."
    },
    "19": {
      "L": "Nothing was missing, whether small or great, sons or daughters, spoil or anything that had been taken; David brought it all back.",
      "M": "Nothing was missing—young or old, sons or daughters, any plunder or anything that had been taken—David brought it all back.",
      "T": "The LORD had said: you will certainly rescue. He was right. Not one person missing. Not one item of spoil unaccounted for."
    },
    "20": {
      "L": "David also captured all the flocks and herds, which were driven before the other livestock; and they said, This is David's spoil.",
      "M": "David also seized all the flocks and herds, driving them ahead of the other livestock. The men said, 'This is David's spoil.'",
      "T": "David also seized the Amalekite herds and flocks—driven separately from the rest. His men declared it: 'This is David's booty.'"
    },
    "21": {
      "L": "Then David came to the two hundred men who had been too exhausted to follow David and who had been left at the brook Besor; they went out to meet David and to meet the people who were with him; and David came near the people and greeted them.",
      "M": "David returned to the two hundred men who had been too exhausted to follow and had stayed at the brook Besor. They came out to meet David and his people. David approached them and greeted them warmly.",
      "T": "When David came back to the Besor, the two hundred who had been too spent to cross came out to meet them. David greeted them as full members of the company."
    },
    "22": {
      "L": "Then all the wicked and worthless men among those who had gone with David said, Because they did not go with us, we will not give them any of the spoil that we have recovered, except that each man may take his wife and his children and go.",
      "M": "But the wicked and worthless men among those who had fought with David said, 'Since they didn't come with us, they get none of the spoil we recovered—just their wives and children, and then they can go.'",
      "T": "Then the hard men spoke up—the ones who had fought and wanted their reward recognized: 'They didn't march with us. They get nothing from the spoil. Give them back their families and send them home.'"
    },
    "23": {
      "L": "But David said, You shall not do so, my brothers, with what the LORD has given us; he has preserved us and given into our hand the raiding party that came against us.",
      "M": "But David said, 'No, my brothers—that is not right with what the LORD has given us. He kept us safe and handed our enemies over to us.'",
      "T": "David stopped it. 'Brothers—no. You don't get to divide what the LORD gave us. He protected every one of us. He put those men into our hands. We didn't earn this; he gave it.'"
    },
    "24": {
      "L": "Who would listen to you in this matter? For as his share is who goes down into battle, so shall his share be who stays by the baggage; they shall share alike.",
      "M": "Who could agree with you on this? The share of the one who goes into battle is the same as the share of the one who stays with the supplies—they share equally.",
      "T": "'The man who stays behind to guard the supplies is doing a soldier's job just as much as the man who fights. Equal risk of the mission, equal share of the reward. They are the same.'"
    },
    "25": {
      "L": "From that day forward he made it a statute and an ordinance for Israel to this day.",
      "M": "From that day David made it a fixed rule for Israel, and it has remained so to this day.",
      "T": "David codified it as law that day—a statute for Israel that endured. The battle belongs to the LORD; the spoil belongs to all."
    },
    "26": {
      "L": "When David came to Ziklag, he sent some of the spoil to the elders of Judah, to his friends, saying, Here is a gift for you from the spoil of the enemies of the LORD.",
      "M": "When David arrived at Ziklag, he sent portions of the spoil to the elders of Judah—his friends—with the message: 'Here is a gift for you from the spoil of the LORD's enemies.'",
      "T": "Back in Ziklag, David began distributing gifts across Judah—to the elders, to communities that had sheltered him in his years of flight. 'Here is a share from the spoil of the LORD's enemies.' He was building a kingdom, one act of generosity at a time."
    },
    "27": {
      "L": "He sent it to those in Bethel, in Ramoth of the Negeb, and in Jattir;",
      "M": "He sent to those in Bethel, Ramoth-negeb, and Jattir;",
      "T": "Bethel, Ramoth-negeb, Jattir—"
    },
    "28": {
      "L": "in Aroer, in Siphmoth, in Eshtemoa;",
      "M": "in Aroer, Siphmoth, and Eshtemoa;",
      "T": "Aroer, Siphmoth, Eshtemoa—"
    },
    "29": {
      "L": "in Racal, in the cities of the Jerahmeelites, in the cities of the Kenites;",
      "M": "in Racal, the towns of the Jerahmeelites, the towns of the Kenites;",
      "T": "Racal, the Jerahmeelite towns, the Kenite towns—"
    },
    "30": {
      "L": "in Hormah, in Bor-ashan, in Athach;",
      "M": "in Hormah, Bor-ashan, and Athach;",
      "T": "Hormah, Bor-ashan, Athach—"
    },
    "31": {
      "L": "in Hebron, and in all the places where David and his men had roamed.",
      "M": "in Hebron—everywhere David and his men had wandered.",
      "T": "and Hebron—everywhere David had ever taken shelter during his years of flight. He remembered every kindness. He was coming home."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '1samuel', existing)
    print('1 Samuel 25–30 written.')

if __name__ == '__main__':
    main()
