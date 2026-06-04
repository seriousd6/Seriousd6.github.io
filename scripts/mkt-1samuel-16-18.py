"""
MKT 1 Samuel chapters 16–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1samuel-16-18.py

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — small-caps convention maintained from prior 1 Samuel scripts.
- H430 (אֱלֹהִים): "God" throughout; all occurrences refer unambiguously to the God of Israel.
- H7307 (רוּחַ): "Spirit of the LORD" (capitalized) for the divine anointing/empowerment;
  "evil spirit" (lowercase) for the tormenting spirit sent from God. Same convention as chs 7–12.
- The evil spirit from the LORD (16:14): the Hebrew rûaḥ rāʿāh mēʾēt YHWH is theologically stark —
  God is the direct agent of Saul's psychological torment. L renders literally, M "harmful spirit sent
  from the LORD," T surfaces the theological weight without softening it.
- H3658 (כִּנּוֹר, kinnor): "lyre" in all tiers — the kinnor was a lyre-type instrument, not a harp;
  rendering "harp" (KJV tradition) is inaccurate; "lyre" is retained throughout.
- H4886 (מָשַׁח, masah): "anoint" in all tiers — the technical term for royal/prophetic installation.
- H5338 (נצל, natsal): "deliver" in L, "rescue/deliver" in M, "pull through/save" in T — 17:37
  David's confession of trust echoes prior deliverances from lion and bear.
- H1285 (בְּרִית): "covenant" in all tiers — 18:3 Jonathan's covenant is a formal, oath-bound bond;
  T surfaces the royal-status-transfer aspect of the robe-giving ceremony.
- Women's song (18:7): antiphonal refrain given poetic line-break form in T tier;
  "thousands/ten thousands" preserved (not modernized to "hundreds/thousands").
- Foreskins (18:25–27): translated accurately without euphemism; the bride-price is historically
  specific and the narrative's brutal irony depends on it.
- Goliath's height "six cubits and a span" (~9ft 9in): kept as literal measure in all tiers;
  T adds interpretive note via "otherworldly figure" language rather than a modern gloss.
- David's spear-avoiding (18:11): "twice" — David eluded both throws; L "avoided out of his presence
  twice," M "eluded him twice," T "once, then again."
- Aspect notes: narrative waw-consecutive imperfects throughout are past tense. The Spirit verbs
  in 16:13 and 18:10 use tsalach/tsalach-pattern — rendered "came powerfully upon."
- "Uncircumcised Philistine" (17:26, 36): preserved in all tiers; the insult activates the
  covenant-boundary dimension — Goliath stands outside the people of God.
- Jonathan's robe-giving (18:4): T explicitly surfaces the royal-transfer symbolism — Jonathan
  is divesting himself of his inheritance and clothing David with it.
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
  "16": {
    "1": {
      "L": "And the LORD said unto Samuel, How long wilt thou mourn for Saul, seeing I have rejected him from being king over Israel? Fill thine horn with oil and go; I will send thee to Jesse the Bethlehemite, for I have provided me a king among his sons.",
      "M": "The LORD said to Samuel, 'How long will you mourn for Saul, now that I have rejected him as king over Israel? Fill your horn with oil and set out—I am sending you to Jesse the Bethlehemite, for I have chosen a king for myself among his sons.'",
      "T": "The LORD broke through Samuel's grief: 'How long will you mourn for Saul? I have rejected him as king of Israel—the decision is made. Fill your horn with oil and go to Bethlehem, to a man named Jesse. I have already chosen my king from among his sons.'"
    },
    "2": {
      "L": "And Samuel said, How can I go? For if Saul hear it, he will kill me. And the LORD said, Take a heifer of the herd with thee and say, I am come to sacrifice to the LORD.",
      "M": "Samuel said, 'How can I go? If Saul hears, he will kill me.' The LORD answered, 'Take a young cow with you and say, \"I have come to sacrifice to the LORD.\"'",
      "T": "Samuel answered: 'How can I go? If Saul gets word of it, he'll have me killed.' The LORD replied, 'Take a young cow with you and say you've come to offer sacrifice to the LORD. That will serve as your cover.'"
    },
    "3": {
      "L": "And call Jesse to the sacrifice, and I will shew thee what thou shalt do; and thou shalt anoint unto me him whom I name unto thee.",
      "M": "Invite Jesse to the sacrifice, and I will show you what you must do. You are to anoint for me the one I indicate to you.",
      "T": "Invite Jesse to join the sacrifice—I will guide you from there. When I identify the one, you will anoint him as my king."
    },
    "4": {
      "L": "And Samuel did that which the LORD spake, and came to Bethlehem. And the elders of the town trembled at his coming and said, Comest thou peaceably?",
      "M": "Samuel did what the LORD commanded and went to Bethlehem. The elders of the town came out trembling to meet him and asked, 'Do you come in peace?'",
      "T": "Samuel did as the LORD directed and traveled to Bethlehem. The town elders came out trembling—a visit from the prophet carried unpredictable weight—and asked anxiously, 'Is this a peaceful visit?'"
    },
    "5": {
      "L": "And he said, Peaceably. I am come to sacrifice to the LORD. Sanctify yourselves and come with me to the sacrifice. And he sanctified Jesse and his sons and called them to the sacrifice.",
      "M": "He said, 'In peace. I have come to sacrifice to the LORD. Purify yourselves and come with me to the sacrifice.' He then consecrated Jesse and his sons and summoned them to the sacrifice.",
      "T": "'Yes, a peaceful errand,' Samuel said. 'I have come to offer sacrifice to the LORD. Purify yourselves and come along.' He consecrated Jesse and his sons and invited them to the offering."
    },
    "6": {
      "L": "And it came to pass when they were come that he looked on Eliab and said, Surely the LORD'S anointed is before him.",
      "M": "When they arrived, Samuel looked at Eliab and thought, 'Surely the LORD's anointed stands before him.'",
      "T": "When they arrived, Samuel's eyes fixed on Eliab—tall, impressive—and he assumed at once: 'Surely this is the man the LORD has chosen.'"
    },
    "7": {
      "L": "But the LORD said unto Samuel, Look not on his countenance or on the height of his stature; because I have refused him. For the LORD seeth not as man seeth; for man looketh on the outward appearance, but the LORD looketh on the heart.",
      "M": "But the LORD said to Samuel, 'Do not look at his appearance or the height of his stature, because I have rejected him. The LORD does not see as man sees: man looks at the outward appearance, but the LORD looks at the heart.'",
      "T": "But the LORD corrected Samuel: 'Stop judging by appearance—by height and bearing. I have already rejected him. The difference between your vision and mine runs deep: you see the surface; I see the interior. Man reads the face; I read the heart.'"
    },
    "8": {
      "L": "Then Jesse called Abinadab and made him pass before Samuel. And he said, Neither hath the LORD chosen this.",
      "M": "Jesse then called Abinadab and had him walk before Samuel. Samuel said, 'Nor has the LORD chosen this one.'",
      "T": "Jesse brought Abinadab forward. Samuel shook his head: 'Not this one either.'"
    },
    "9": {
      "L": "Then Jesse made Shammah to pass by. And he said, Neither hath the LORD chosen this.",
      "M": "Then Jesse brought Shammah forward. Samuel said, 'Nor has the LORD chosen this one.'",
      "T": "Then Shammah walked before Samuel. Again: 'Not this one.'"
    },
    "10": {
      "L": "Again Jesse made seven of his sons to pass before Samuel. And Samuel said unto Jesse, The LORD hath not chosen these.",
      "M": "Jesse had seven of his sons pass before Samuel. Samuel told Jesse, 'The LORD has not chosen any of these.'",
      "T": "One by one—seven sons in all—passed before Samuel, and with each one the LORD gave the same silent answer. Samuel turned to Jesse: 'None of these is the one the LORD has chosen.'"
    },
    "11": {
      "L": "And Samuel said unto Jesse, Are here all thy children? And he said, There remaineth yet the youngest, and behold he keepeth the sheep. And Samuel said unto Jesse, Send and fetch him; for we will not sit down till he come hither.",
      "M": "Samuel asked Jesse, 'Are all your sons here?' Jesse replied, 'The youngest is still out—he is tending the sheep.' Samuel said, 'Send for him at once; we will not take our places until he arrives.'",
      "T": "Samuel pressed him: 'Is this everyone?' Jesse admitted, 'There is still the youngest—he is out with the sheep, not considered worth summoning.' Samuel said, 'Send for him immediately. We will not start until he arrives.'"
    },
    "12": {
      "L": "And he sent and brought him in. Now he was ruddy and withal of a beautiful countenance and goodly to look to. And the LORD said, Arise, anoint him; for this is he.",
      "M": "Jesse sent and had him brought in. He was ruddy—handsome of face and appearance. The LORD said to Samuel, 'Rise and anoint him; this is the one.'",
      "T": "They sent for him, and when David walked in—fresh-faced, bright-eyed, striking in appearance—the LORD said to Samuel: 'Stand up and anoint him. This is the one.'"
    },
    "13": {
      "L": "Then Samuel took the horn of oil and anointed him in the midst of his brethren; and the Spirit of the LORD came upon David from that day forward. So Samuel rose up and went to Ramah.",
      "M": "Samuel took the horn of oil and anointed him in the midst of his brothers. The Spirit of the LORD came powerfully upon David from that day onward. Samuel then rose and left for Ramah.",
      "T": "Samuel poured the oil over David's head in front of all his brothers. From that moment, the Spirit of the LORD came powerfully upon David and did not depart. Samuel rose and returned to Ramah—his work here was done."
    },
    "14": {
      "L": "But the Spirit of the LORD departed from Saul, and an evil spirit from the LORD troubled him.",
      "M": "Now the Spirit of the LORD had departed from Saul, and a harmful spirit sent from the LORD tormented him.",
      "T": "What came upon David had departed Saul. The Spirit of the LORD left him, and in its place came a tormenting spirit—the text is unsparing: it was sent by the LORD—that plunged Saul into terror and anguish."
    },
    "15": {
      "L": "And Saul's servants said unto him, Behold now, an evil spirit from God troubleth thee.",
      "M": "Saul's servants said to him, 'An evil spirit from God is troubling you.'",
      "T": "Saul's attendants saw what was happening and spoke plainly: 'A tormenting spirit sent by God has taken hold of you.'"
    },
    "16": {
      "L": "Let our lord now command thy servants before thee to seek out a man who is a cunning player on a lyre; and it shall come to pass when the evil spirit from God is upon thee that he shall play with his hand and thou shalt be well.",
      "M": "Let our lord command his servants to search for a man skilled at playing the lyre. When the harmful spirit from God comes upon you, he will play and you will be relieved.",
      "T": "They proposed a remedy: 'Command your servants to find a skilled lyre player. When the tormenting spirit seizes you, his music may bring relief.'"
    },
    "17": {
      "L": "And Saul said unto his servants, Provide me now a man that can play well and bring him to me.",
      "M": "Saul said to his servants, 'Find me a man who plays well and bring him to me.'",
      "T": "Saul agreed: 'Find me someone who plays well, and bring him here.'"
    },
    "18": {
      "L": "Then one of the servants answered and said, Behold I have seen a son of Jesse the Bethlehemite who is cunning in playing and a mighty valiant man and a man of war and prudent in matters and a comely person and the LORD is with him.",
      "M": "One of the servants answered, 'I know of a son of Jesse the Bethlehemite—skilled in playing, brave and a man of war, prudent in speech, handsome, and the LORD is with him.'",
      "T": "One attendant spoke up: 'I know the very man—a son of Jesse in Bethlehem. He plays beautifully. He is also brave, a proven fighter, wise in counsel, good-looking, and the LORD is plainly with him.'"
    },
    "19": {
      "L": "Wherefore Saul sent messengers unto Jesse and said, Send me David thy son who is with the sheep.",
      "M": "So Saul sent messengers to Jesse and said, 'Send me your son David, who tends the sheep.'",
      "T": "Saul dispatched messengers to Jesse: 'Send your son David—the one who looks after the sheep.'"
    },
    "20": {
      "L": "And Jesse took an ass laden with bread and a bottle of wine and a kid and sent them by David his son unto Saul.",
      "M": "Jesse took a donkey loaded with bread, a skin of wine, and a young goat and sent them with his son David to Saul.",
      "T": "Jesse prepared a fitting gift—bread, wine, and a young goat loaded onto a donkey—and sent David to present it to the king."
    },
    "21": {
      "L": "And David came to Saul and stood before him; and he loved him greatly and he became his armourbearer.",
      "M": "David came to Saul and entered his service. Saul loved him deeply, and David became his armor-bearer.",
      "T": "David arrived at court, came before Saul, and impressed him immediately. Saul developed a deep affection for him and made him his personal armor-bearer."
    },
    "22": {
      "L": "And Saul sent to Jesse saying, Let David I pray thee stand before me; for he hath found favour in my sight.",
      "M": "Saul sent word to Jesse: 'Please let David remain in my service, for he has found favor with me.'",
      "T": "Saul sent Jesse a message: 'Please release David to stay at my side—I have found great value in him.'"
    },
    "23": {
      "L": "And it came to pass when the evil spirit from God was upon Saul that David took a lyre and played with his hand; so Saul was refreshed and was well and the evil spirit departed from him.",
      "M": "Whenever the harmful spirit from God came upon Saul, David took the lyre and played. Then Saul would be calmed and feel well, and the harmful spirit would leave him.",
      "T": "In this way a pattern was established: when the tormenting spirit descended on Saul, David would take his lyre and play. The music soothed Saul and brought him relief, and the spirit would withdraw."
    }
  },
  "17": {
    "1": {
      "L": "Now the Philistines gathered their armies to battle and were gathered together at Shochoh which belongeth to Judah and pitched between Shochoh and Azekah in Ephesdammim.",
      "M": "The Philistines gathered their forces for war and assembled at Socoh, which belongs to Judah. They camped between Socoh and Azekah, at Ephes-dammim.",
      "T": "The Philistines mustered for war and made camp at Socoh in Judah's territory—specifically between Socoh and Azekah, at a place called Ephes-dammim."
    },
    "2": {
      "L": "And Saul and the men of Israel were gathered together and pitched by the valley of Elah and set the battle in array against the Philistines.",
      "M": "Saul and the Israelites assembled and encamped in the Valley of Elah, drawing up their battle lines against the Philistines.",
      "T": "Saul and the forces of Israel took up their position in the Valley of Elah, facing the Philistine army across the valley floor."
    },
    "3": {
      "L": "And the Philistines stood on a mountain on the one side and Israel stood on a mountain on the other side and there was a valley between them.",
      "M": "The Philistines were standing on the hill on one side, and Israel stood on the hill on the other side, with the valley between them.",
      "T": "Two hills faced each other across a ravine—Philistines on one slope, Israel on the other, the valley between them an open killing ground that neither side was willing to cross."
    },
    "4": {
      "L": "And there went out a champion out of the camp of the Philistines named Goliath of Gath whose height was six cubits and a span.",
      "M": "A champion stepped out from the Philistine camp—Goliath of Gath—whose height was six cubits and a span.",
      "T": "Then the Philistines sent out their champion: Goliath of Gath, who stood six cubits and a span tall—an almost otherworldly figure of a man."
    },
    "5": {
      "L": "And he had an helmet of brass upon his head and he was armed with a coat of mail; and the weight of the coat was five thousand shekels of brass.",
      "M": "He wore a bronze helmet and was clad in a coat of scale armor weighing five thousand shekels of bronze.",
      "T": "His head was covered by a bronze helmet, and he wore scale armor—five thousand bronze shekels of it, roughly 125 pounds—an almost immovable wall of metal."
    },
    "6": {
      "L": "And he had greaves of brass upon his legs and a target of brass between his shoulders.",
      "M": "He wore bronze greaves on his legs and carried a bronze javelin slung between his shoulders.",
      "T": "Bronze greaves protected his legs, and a javelin was strapped across his back between his shoulders—he was armored from head to heel."
    },
    "7": {
      "L": "And the staff of his spear was like a weaver's beam and his spear's head weighed six hundred shekels of iron; and one bearing a shield went before him.",
      "M": "The shaft of his spear was as thick as a weaver's beam, with an iron head weighing six hundred shekels. A shield-bearer walked in front of him.",
      "T": "His spear shaft was as thick as a weaver's beam, with an iron tip weighing fifteen pounds. A man walked ahead of him carrying his shield—Goliath needed someone just to bear his equipment."
    },
    "8": {
      "L": "And he stood and cried unto the armies of Israel and said unto them, Why are ye come out to set your battle in array? Am not I a Philistine and ye servants to Saul? Choose you a man for you and let him come down to me.",
      "M": "He stood and shouted to the ranks of Israel: 'Why have you come out to draw up for battle? Am I not a Philistine, and are you not servants of Saul? Choose a man and send him down to me.'",
      "T": "Goliath stepped forward and bellowed at Israel's battle lines: 'Why bother deploying for battle? I am a Philistine—and you are Saul's servants! Pick your best man and send him out to face me.'"
    },
    "9": {
      "L": "If he be able to fight with me and to kill me then will we be your servants; but if I prevail against him and kill him then shall ye be our servants and serve us.",
      "M": "'If he is able to fight me and kill me, we will be your servants. But if I prevail and kill him, you shall be our servants and serve us.'",
      "T": "'The terms are simple: if your man can beat me, we become your slaves. But if I beat him, you become ours. Winner takes all—no armies needed.'"
    },
    "10": {
      "L": "And the Philistine said, I defy the armies of Israel this day; give me a man that we may fight together.",
      "M": "The Philistine continued: 'I challenge the armies of Israel today! Give me a man and let us fight.'",
      "T": "He raised his voice even louder: 'I throw down my challenge to every soldier Israel has! Send me your champion!'"
    },
    "11": {
      "L": "When Saul and all Israel heard those words of the Philistine they were dismayed and greatly afraid.",
      "M": "When Saul and all Israel heard the Philistine's words, they were dismayed and terrified.",
      "T": "Saul and every man of Israel heard the challenge—and fear swept through the camp."
    },
    "12": {
      "L": "Now David was the son of that Ephrathite of Bethlehemjudah whose name was Jesse; and he had eight sons; and the man was old and advanced in years in the days of Saul.",
      "M": "David was the son of an Ephrathite from Bethlehem of Judah named Jesse. Jesse had eight sons and was old and well advanced in age in Saul's time.",
      "T": "Meanwhile—David. He was the son of Jesse, a man of Bethlehem in Judah, of Ephrathite stock. Jesse had eight sons and was by this time an old man."
    },
    "13": {
      "L": "And the three eldest sons of Jesse went and followed Saul to the battle; and the names of his three sons that went to the battle were Eliab the firstborn and next unto him Abinadab and the third Shammah.",
      "M": "Jesse's three oldest sons had gone to follow Saul into battle. Their names were Eliab the firstborn, Abinadab the second, and Shammah the third.",
      "T": "His three oldest sons—Eliab, Abinadab, and Shammah—were all in Saul's army at the front."
    },
    "14": {
      "L": "And David was the youngest; and the three eldest followed Saul.",
      "M": "David was the youngest. The three oldest had gone with Saul.",
      "T": "David was the youngest of them all—too young, apparently, to be at the front."
    },
    "15": {
      "L": "But David went and returned from Saul to feed his father's sheep at Bethlehem.",
      "M": "But David went back and forth between Saul's service and tending his father's sheep at Bethlehem.",
      "T": "He shuttled between Saul's court and Bethlehem, returning home whenever needed to tend the family flock."
    },
    "16": {
      "L": "And the Philistine drew near morning and evening and presented himself forty days.",
      "M": "The Philistine came forward morning and evening for forty days and took his stand.",
      "T": "Day after day—morning shift and evening shift—for forty days straight, Goliath stepped out and issued his challenge. No one answered him."
    },
    "17": {
      "L": "And Jesse said unto David his son, Take now for thy brethren an ephah of this parched corn and these ten loaves and run to the camp to thy brethren.",
      "M": "Jesse said to his son David, 'Take this ephah of roasted grain and these ten loaves to your brothers at the camp—hurry to them.'",
      "T": "Then Jesse called David: 'Run to the camp with supplies for your brothers—an ephah of roasted grain and ten loaves of bread. Get going.'"
    },
    "18": {
      "L": "And carry these ten cheeses unto the captain of their thousand and look how thy brethren fare and take their pledge.",
      "M": "Take these ten portions of cheese to their unit commander, and check on your brothers. Bring back some token from them.",
      "T": "And take ten cuts of cheese to their commanding officer. See that your brothers are alright and bring back word from them."
    },
    "19": {
      "L": "Now Saul and they and all the men of Israel were in the valley of Elah fighting with the Philistines.",
      "M": "Saul and Jesse's sons and all the men of Israel were in the Valley of Elah fighting the Philistines.",
      "T": "Saul and David's brothers were at the front in the Valley of Elah, locked in a standoff with the Philistines."
    },
    "20": {
      "L": "And David rose up early in the morning and left the sheep with a keeper and took and went as Jesse had commanded him; and he came to the trench as the host was going forth to the fight and shouted for the battle.",
      "M": "David rose early in the morning, left the sheep with a keeper, and went as Jesse had instructed. He arrived at the camp just as the army was going out to take up battle positions with a shout.",
      "T": "David was up at first light, left the flock with a hired hand, and set off with Jesse's provisions. He reached the camp just as the army was advancing to battle with their war cry."
    },
    "21": {
      "L": "For Israel and the Philistines had put the battle in array army against army.",
      "M": "Israel and the Philistines were drawing up in battle formation, army facing army.",
      "T": "The two armies had taken their positions, each drawn up on its ridge, facing the other across the valley."
    },
    "22": {
      "L": "And David left his carriage in the hand of the keeper of the carriage and ran into the army and came and saluted his brethren.",
      "M": "David left his supplies with the keeper of supplies, ran to the battle line, and went to greet his brothers.",
      "T": "David handed his supplies to the supply master and ran down to the line, pushing through until he found his brothers."
    },
    "23": {
      "L": "And as he talked with them behold there came up the champion the Philistine of Gath Goliath by name out of the armies of the Philistines and spake according to the same words; and David heard them.",
      "M": "While he was speaking with them, the champion Goliath of Gath stepped out from the Philistine ranks and repeated his usual challenge. David heard it.",
      "T": "While David was talking with his brothers, out stepped Goliath—the Philistine champion from Gath—and shouted his familiar defiance. David heard every word."
    },
    "24": {
      "L": "And all the men of Israel when they saw the man fled from him and were sore afraid.",
      "M": "All the men of Israel saw Goliath and fled before him in great fear.",
      "T": "Every man in Israel who saw Goliath turned and ran. The fear was visceral."
    },
    "25": {
      "L": "And the men of Israel said, Have ye seen this man that is come up? Surely to defy Israel is he come up; and it shall be that the man who killeth him the king will enrich him with great riches and will give him his daughter and make his father's house free in Israel.",
      "M": "The men of Israel were saying, 'Have you seen this man who has come out? He has come to defy Israel. The king will richly reward the man who kills him—give him his daughter and exempt his father's house from taxes in Israel.'",
      "T": "The troops were talking: 'Did you see him? This Philistine comes to humiliate Israel's entire army. The king has promised to load the man who kills him with wealth, give him his daughter in marriage, and make his whole family tax-exempt.'"
    },
    "26": {
      "L": "And David spake to the men that stood by him saying, What shall be done to the man that killeth this Philistine and taketh away the reproach from Israel? For who is this uncircumcised Philistine that he should defy the armies of the living God?",
      "M": "David asked the men standing near him, 'What will be done for the man who kills this Philistine and removes this disgrace from Israel? Who is this uncircumcised Philistine, that he should defy the armies of the living God?'",
      "T": "David turned to the men around him: 'What does the man who kills this Philistine and removes Israel's shame actually receive?' And then, with a different energy altogether: 'Who does this uncircumcised Philistine think he is, throwing his insults at the armies of the living God?'"
    },
    "27": {
      "L": "And the people answered him after this manner saying, So shall it be done to the man that killeth him.",
      "M": "The men told him the same thing: 'This is what will be done for the man who kills him.'",
      "T": "They repeated the same terms. David absorbed the information."
    },
    "28": {
      "L": "And Eliab his eldest brother heard when he spake unto the men; and Eliab's anger was kindled against David and he said, Why camest thou down hither? And with whom hast thou left those few sheep in the wilderness? I know thy pride and the naughtiness of thine heart; for thou art come down that thou mightest see the battle.",
      "M": "Eliab, his eldest brother, heard what David was saying to the men, and his anger flared against David. He said, 'Why did you come down here? Who did you leave those few sheep with in the wilderness? I know how proud and insolent you are—you came down just to watch the fighting.'",
      "T": "Eliab—David's eldest brother—heard it all, and his temper broke. 'What are you doing here? Who is watching that tiny little flock back in the wilderness? I know exactly what you are—arrogant and restless—you came here just to gawk at the battle.'"
    },
    "29": {
      "L": "And David said, What have I now done? Is there not a cause?",
      "M": "David answered, 'What have I done now? Is there not a reason to ask?'",
      "T": "David replied calmly: 'What did I do wrong? Can't I even ask a question?'"
    },
    "30": {
      "L": "And he turned from him toward another and spake after the same manner; and the people answered him again after the former manner.",
      "M": "He turned away and spoke with someone else in the same way, and the men gave him the same answer.",
      "T": "David let it go and turned to someone else, asking the same questions. He got the same answers."
    },
    "31": {
      "L": "And when the words were heard which David spake they rehearsed them before Saul; and he sent for him.",
      "M": "What David had been saying was reported to Saul, who sent for him.",
      "T": "Word of what David was saying made its way up the chain to Saul, and Saul sent for him."
    },
    "32": {
      "L": "And David said to Saul, Let no man's heart fail because of him; thy servant will go and fight with this Philistine.",
      "M": "David said to Saul, 'Let no one's heart fail because of him. Your servant will go and fight this Philistine.'",
      "T": "David stood before the king: 'Don't let anyone lose heart over this Philistine. I will go and fight him.'"
    },
    "33": {
      "L": "And Saul said to David, Thou art not able to go against this Philistine to fight with him; for thou art but a youth and he a man of war from his youth.",
      "M": "Saul said to David, 'You cannot go against this Philistine to fight him—you are only a young man, and he has been a warrior from his youth.'",
      "T": "Saul was blunt: 'You can't do this. You're a boy, and he has been a professional soldier his entire life.'"
    },
    "34": {
      "L": "And David said unto Saul, Thy servant kept his father's sheep and there came a lion and a bear and took a lamb out of the flock.",
      "M": "David told Saul, 'Your servant has been tending his father's sheep. When a lion or a bear came and took a lamb from the flock,'",
      "T": "David answered: 'My lord, I have been keeping my father's flock. A lion came once, a bear another time—each of them grabbed a lamb from the flock.'"
    },
    "35": {
      "L": "And I went out after him and smote him and delivered it out of his mouth; and when he arose against me I caught him by his beard and smote him and slew him.",
      "M": "I went after it, struck it, and recovered the lamb from its mouth. When it turned on me, I seized it by the beard, struck it, and killed it.",
      "T": "I went after each one, struck it, and tore the lamb from its mouth. When they turned on me, I grabbed them by the jaw and beat them to death."
    },
    "36": {
      "L": "Thy servant slew both the lion and the bear; and this uncircumcised Philistine shall be as one of them seeing he hath defied the armies of the living God.",
      "M": "Your servant has killed both lion and bear. This uncircumcised Philistine will be like one of them, for he has defied the armies of the living God.",
      "T": "I killed both—lion and bear. This uncircumcised Philistine will get the same treatment. He has insulted the armies of the living God, and that is something I will not leave unanswered."
    },
    "37": {
      "L": "David said moreover, The LORD that delivered me out of the paw of the lion and out of the paw of the bear he will deliver me out of the hand of this Philistine. And Saul said unto David, Go, and the LORD be with thee.",
      "M": "David added, 'The LORD who rescued me from the claws of the lion and the bear will rescue me from the hand of this Philistine.' Saul said to David, 'Go, and may the LORD be with you.'",
      "T": "David pressed his case: 'The LORD who pulled me out of the jaws of a lion and the grip of a bear—that same LORD will pull me through this fight.' Saul relented: 'Go then. May the LORD be with you.'"
    },
    "38": {
      "L": "And Saul armed David with his armour and he put an helmet of brass upon his head; also he armed him with a coat of mail.",
      "M": "Saul dressed David in his own armor, placing a bronze helmet on his head and fitting him with a coat of mail.",
      "T": "Saul outfitted David with his own battle gear—bronze helmet on his head, a coat of scale armor around his body."
    },
    "39": {
      "L": "And David girded his sword upon his armour and he assayed to go; for he had not proved it. And David said unto Saul, I cannot go with these; for I have not proved them. And David put them off him.",
      "M": "David fastened on the sword over the armor and tried to walk, but had not tested it before. He said to Saul, 'I cannot move in these—I have no experience with them.' So David took the armor off.",
      "T": "David strapped on the sword and tried to walk—but he had never worn armor before, and he could barely move in it. He said plainly to Saul, 'I can't fight in this—I'm not used to it.' He took it all off."
    },
    "40": {
      "L": "And he took his staff in his hand and chose him five smooth stones out of the brook and put them in a shepherd's bag which he had even in a scrip; and his sling was in his hand; and he drew near to the Philistine.",
      "M": "He took his staff in his hand, selected five smooth stones from the brook and put them in his shepherd's pouch, and with his sling in his hand he advanced toward the Philistine.",
      "T": "Instead he picked up his shepherd's staff, chose five smooth stones from the streambed and dropped them in his pouch, slung his sling over his shoulder, and walked toward Goliath."
    },
    "41": {
      "L": "And the Philistine came on and drew near unto David; and the man that bare the shield went before him.",
      "M": "The Philistine came forward toward David, with his shield-bearer walking ahead of him.",
      "T": "Goliath advanced toward David, the shield-bearer out in front—the full spectacle of Philistine military power."
    },
    "42": {
      "L": "And when the Philistine looked about and saw David he disdained him; for he was but a youth and ruddy and of a fair countenance.",
      "M": "When the Philistine looked David over and saw that he was just a youth—ruddy and handsome—he despised him.",
      "T": "Goliath looked David over: a boy, red-cheeked and bright-eyed. He despised what he saw."
    },
    "43": {
      "L": "And the Philistine said unto David, Am I a dog that thou comest to me with staves? And the Philistine cursed David by his gods.",
      "M": "The Philistine said to David, 'Am I a dog that you come at me with a stick?' And the Philistine cursed David by his gods.",
      "T": "'What's this?' Goliath shouted. 'Am I a dog, that you come after me with a stick?' He cursed David by every god he knew."
    },
    "44": {
      "L": "And the Philistine said to David, Come to me and I will give thy flesh unto the fowls of the air and to the beasts of the field.",
      "M": "Then the Philistine said to David, 'Come here to me, and I will give your flesh to the birds of the sky and the beasts of the field.'",
      "T": "He pressed the insult: 'Come closer, boy, and I will feed your carcass to the vultures and the jackals.'"
    },
    "45": {
      "L": "Then said David to the Philistine, Thou comest to me with a sword and with a spear and with a shield; but I come to thee in the name of the LORD of hosts the God of the armies of Israel whom thou hast defied.",
      "M": "David said to the Philistine, 'You come against me with sword and spear and javelin, but I come against you in the name of the LORD of Hosts, the God of the armies of Israel, whom you have defied.'",
      "T": "David answered him straight: 'You come to this fight with sword, spear, and javelin. I come in the name of the LORD of Hosts—the God of Israel's armies—the very one you have been insulting.'"
    },
    "46": {
      "L": "This day will the LORD deliver thee into mine hand; and I will smite thee and take thine head from thee; and I will give the carcases of the host of the Philistines this day unto the fowls of the air and to the wild beasts of the earth; that all the earth may know that there is a God in Israel.",
      "M": "This day the LORD will hand you over to me. I will strike you down and cut off your head. I will give the corpses of the Philistine camp to the birds of the sky and the beasts of the earth, so that all the world may know that there is a God in Israel.",
      "T": "Today the LORD will give you into my hand. I will cut off your head and leave your army's bodies for the birds and the scavengers—because the whole earth needs to know there is a God in Israel."
    },
    "47": {
      "L": "And all this assembly shall know that the LORD saveth not with sword and spear; for the battle is the LORD'S and he will give you into our hands.",
      "M": "And this whole assembly will know that the LORD does not save by sword and spear. The battle belongs to the LORD, and he will deliver you into our hands.",
      "T": "This crowd—every soldier watching—will learn today that the LORD does not need sword or spear to save. The battle belongs to him, and he will hand you over to us."
    },
    "48": {
      "L": "And it came to pass when the Philistine arose and came and drew nigh to meet David that David hasted and ran toward the army to meet the Philistine.",
      "M": "When the Philistine started moving to advance against David, David ran quickly toward the battle line to meet the Philistine.",
      "T": "Then Goliath began his advance, and David—instead of waiting—broke into a sprint straight toward the Philistine."
    },
    "49": {
      "L": "And David put his hand in his bag and took thence a stone and slang it and smote the Philistine in his forehead and the stone sunk into his forehead; and he fell upon his face to the earth.",
      "M": "David reached into his pouch, took out a stone, and slung it. It struck the Philistine in the forehead, and the stone sank into his forehead. He fell face forward onto the ground.",
      "T": "David reached into his pouch mid-stride, loaded the sling, and released. The stone found the one gap in all that armor—Goliath's exposed forehead—and drove home. The giant pitched forward and hit the ground, face down."
    },
    "50": {
      "L": "So David prevailed over the Philistine with a sling and with a stone and smote the Philistine and slew him; but there was no sword in the hand of David.",
      "M": "So David prevailed over the Philistine with a sling and a stone—he struck the Philistine down and killed him, though David had no sword in his hand.",
      "T": "David had felled the mightiest warrior the Philistines possessed—using a shepherd's sling and a river stone. He had no sword."
    },
    "51": {
      "L": "Therefore David ran and stood upon the Philistine and took his sword and drew it out of the sheath thereof and slew him and cut off his head therewith. And when the Philistines saw their champion was dead they fled.",
      "M": "David ran and stood over the Philistine, drew Goliath's own sword from its sheath, killed him, and cut off his head with it. When the Philistines saw their champion was dead, they fled.",
      "T": "David ran and stood over the fallen Goliath, grabbed the giant's own sword from its scabbard, and finished the job—taking his head. The moment the Philistines saw their champion fall, their courage broke and they ran."
    },
    "52": {
      "L": "And the men of Israel and of Judah arose and shouted and pursued the Philistines until thou come to the valley and to the gates of Ekron. And the wounded of the Philistines fell down by the way to Shaaraim even unto Gath and unto Ekron.",
      "M": "The men of Israel and Judah rose up with a shout and pursued the Philistines to the entrance of the valley and to the gates of Ekron. The Philistines' wounded fell all along the road to Shaaraim, as far as Gath and Ekron.",
      "T": "Israel and Judah erupted with a battle cry and poured after the fleeing Philistines—all the way to the gates of Ekron. Philistine bodies lined the road to Shaaraim, scattered between there and Gath and Ekron."
    },
    "53": {
      "L": "And the children of Israel returned from chasing after the Philistines and they spoiled their tents.",
      "M": "When the Israelites returned from pursuing the Philistines, they plundered their camp.",
      "T": "When the chase was over, Israel's soldiers came back to the deserted Philistine camp and stripped it bare."
    },
    "54": {
      "L": "And David took the head of the Philistine and brought it to Jerusalem; but he put his armour in his tent.",
      "M": "David took the head of the Philistine and brought it to Jerusalem, and he put the Philistine's armor in his own tent.",
      "T": "David carried Goliath's head to Jerusalem and stowed the giant's armor in his personal tent."
    },
    "55": {
      "L": "And when Saul saw David go forth against the Philistine he said unto Abner the captain of the host, Abner whose son is this youth? And Abner said, As thy soul liveth O king I cannot tell.",
      "M": "As Saul watched David march out against the Philistine, he asked Abner, the commander of the army, 'Abner, whose son is this young man?' Abner said, 'As surely as you live, my king, I do not know.'",
      "T": "Saul had been watching as David strode out toward Goliath, and he turned to his general Abner: 'Who is that boy's father?' Abner replied, 'I have no idea, my lord.'"
    },
    "56": {
      "L": "And the king said, Enquire thou whose son the stripling is.",
      "M": "The king said, 'Find out whose son this young man is.'",
      "T": "'Find out,' Saul said."
    },
    "57": {
      "L": "And as David returned from the slaughter of the Philistine Abner took him and brought him before Saul with the head of the Philistine in his hand.",
      "M": "When David returned from striking down the Philistine, Abner brought him before Saul with the Philistine's head still in his hand.",
      "T": "As David returned from the battlefield, Abner brought him before Saul—David still holding Goliath's severed head."
    },
    "58": {
      "L": "And Saul said to him, Whose son art thou thou young man? And David answered, I am the son of thy servant Jesse the Bethlehemite.",
      "M": "Saul asked him, 'Whose son are you, young man?' David answered, 'I am the son of your servant Jesse the Bethlehemite.'",
      "T": "Saul asked him directly: 'Whose son are you?' David replied simply: 'I am the son of your servant Jesse, from Bethlehem.'"
    }
  },
  "18": {
    "1": {
      "L": "And it came to pass when he had made an end of speaking unto Saul that the soul of Jonathan was knit with the soul of David and Jonathan loved him as his own soul.",
      "M": "After David had finished speaking with Saul, the soul of Jonathan was bound to the soul of David, and Jonathan loved him as his own soul.",
      "T": "When David finished speaking with Saul, something had happened in Jonathan: his heart was bound to David's—an immediate, total loyalty of soul. He loved David as himself."
    },
    "2": {
      "L": "And Saul took him that day and would let him go no more home to his father's house.",
      "M": "Saul kept David with him from that day on and would not let him return to his father's house.",
      "T": "Saul took David into his household that same day and would not release him back to his father."
    },
    "3": {
      "L": "Then Jonathan and David made a covenant because he loved him as his own soul.",
      "M": "Jonathan made a covenant with David, because he loved him as his own soul.",
      "T": "Jonathan formalized what his heart had already decided—he made a covenant with David, sealing the bond of loyalty his soul had already formed."
    },
    "4": {
      "L": "And Jonathan stripped himself of the robe that was upon him and gave it to David and his garments even to his sword and to his bow and to his girdle.",
      "M": "Jonathan took off the robe he was wearing and gave it to David, along with his armor, his sword, his bow, and his belt.",
      "T": "Then Jonathan did something extraordinary: he stripped off his royal robe and gave it to David—and with it his tunic, sword, bow, and belt. He was handing David his identity, his status, his future."
    },
    "5": {
      "L": "And David went out whithersoever Saul sent him and behaved himself wisely; and Saul set him over the men of war and he was accepted in the sight of all the people and also in the sight of Saul's servants.",
      "M": "David went out wherever Saul sent him and succeeded in everything he did. Saul placed him in command of the fighting men, and he was accepted by all the people and by Saul's own servants.",
      "T": "David served wherever Saul deployed him, and every mission succeeded. Saul promoted him to command of his soldiers, and David was popular with the people and respected among Saul's own staff."
    },
    "6": {
      "L": "And it came to pass as they came when David returned from the slaughter of the Philistine that the women came out of all the cities of Israel singing and dancing to meet king Saul with tabrets with joy and with instruments of musick.",
      "M": "As they were returning home after David had struck down the Philistine, women came out from all the towns of Israel to greet King Saul with singing and dancing, with tambourines and joyful music.",
      "T": "When the army came home after Goliath's death, women poured out of every town in Israel to welcome King Saul—singing, dancing, tambourines, instruments, joy."
    },
    "7": {
      "L": "And the women answered one another as they played and said, Saul hath slain his thousands and David his ten thousands.",
      "M": "As they celebrated, the women called back and forth to one another: 'Saul has struck down his thousands, and David his ten thousands.'",
      "T": "The women sang in alternating choruses, their refrain traveling through the crowd:\n    Saul has struck down his thousands,\n    and David his ten thousands."
    },
    "8": {
      "L": "And Saul was very wroth and the saying displeased him; and he said, They have ascribed unto David ten thousands and to me they have ascribed but thousands; and what can he have more but the kingdom?",
      "M": "Saul became very angry, and the song displeased him greatly. He said, 'They have credited David with ten thousands, but me with only thousands. What more can he have but the kingdom?'",
      "T": "The song infuriated Saul. He fixed on the arithmetic: ten thousands for David, thousands for him. 'They have already given him everything—what is left for him to take but the crown?'"
    },
    "9": {
      "L": "And Saul eyed David from that day and forward.",
      "M": "From that day Saul watched David with suspicion.",
      "T": "From that moment, Saul never looked at David the same way again."
    },
    "10": {
      "L": "And it came to pass on the morrow that the evil spirit from God came upon Saul and he prophesied in the midst of the house; and David played with his hand as at other times; and there was a javelin in Saul's hand.",
      "M": "The next day an evil spirit from God came powerfully upon Saul, and he went into a frenzy in the middle of the house. David was playing the lyre as usual, and Saul had a spear in his hand.",
      "T": "The very next day it happened: the tormenting spirit descended on Saul again, and he fell into a frenzy inside the palace. David was playing the lyre as he always did—and Saul had a spear in his hand."
    },
    "11": {
      "L": "And Saul cast the javelin; for he said, I will smite David even to the wall with it. And David avoided out of his presence twice.",
      "M": "Saul hurled the spear, thinking, 'I will pin David to the wall.' But David eluded him twice.",
      "T": "Saul threw the spear—intending to nail David to the wall—but David stepped aside, once, then again. Twice he escaped."
    },
    "12": {
      "L": "And Saul was afraid of David because the LORD was with him and was departed from Saul.",
      "M": "Saul was afraid of David, because the LORD was with him but had departed from Saul.",
      "T": "Saul's fury turned to fear: the LORD was visibly with David—and had just as visibly left Saul."
    },
    "13": {
      "L": "Therefore Saul removed him from him and made him his captain over a thousand; and he went out and came in before the people.",
      "M": "So Saul removed David from his personal service and made him commander of a thousand men. David went out on campaigns and returned with the people.",
      "T": "So Saul pushed David away—made him a field commander over a thousand men, kept him occupied and out of the palace. David went on campaign and came back, over and over."
    },
    "14": {
      "L": "And David behaved himself wisely in all his ways; and the LORD was with him.",
      "M": "David had success in all his undertakings, for the LORD was with him.",
      "T": "And everywhere David went, he succeeded—because the LORD was with him."
    },
    "15": {
      "L": "Wherefore when Saul saw that he behaved himself very wisely he was afraid of him.",
      "M": "When Saul saw how consistently successful David was, he was afraid of him.",
      "T": "Every success David had only deepened Saul's terror of him."
    },
    "16": {
      "L": "But all Israel and Judah loved David because he went out and came in before them.",
      "M": "All Israel and Judah loved David, for he was the one who led them on campaigns.",
      "T": "Israel and Judah adored him—he was the one who led them, who went ahead of them into danger and brought them home."
    },
    "17": {
      "L": "And Saul said to David, Behold my elder daughter Merab; her will I give thee to wife: only be thou valiant for me and fight the LORD'S battles. For Saul said, Let not mine hand be upon him but let the hand of the Philistines be upon him.",
      "M": "Saul said to David, 'Here is my eldest daughter Merab—I will give her to you in marriage. Only be courageous for me and fight the LORD's battles.' For Saul was thinking, 'I will not lay a hand on him myself; let the Philistines do it.'",
      "T": "Saul made his move: 'I will give you my eldest daughter Merab as your wife—all I ask is that you keep fighting bravely for me, fighting the LORD's battles.' What he was actually thinking: 'I won't kill him myself. I will let the Philistines take care of it.'"
    },
    "18": {
      "L": "And David said unto Saul, Who am I and what is my life or my father's family in Israel that I should be son in law to the king?",
      "M": "David said to Saul, 'Who am I? And what is my life, or my father's family in Israel, that I should become the king's son-in-law?'",
      "T": "David demurred: 'Who am I? What is my family? We are nobody—not the kind of people who marry into royal houses.'"
    },
    "19": {
      "L": "But it came to pass at the time when Merab Saul's daughter should have been given to David that she was given unto Adriel the Meholathite to wife.",
      "M": "But when the time came for Merab, Saul's daughter, to be given to David, she was instead given to Adriel the Meholathite as his wife.",
      "T": "When the time came, Saul gave Merab to someone else—Adriel of Meholah. The promise evaporated."
    },
    "20": {
      "L": "And Michal Saul's daughter loved David; and they told Saul and the thing pleased him.",
      "M": "Now Michal, Saul's daughter, had fallen in love with David. When Saul was told, the news pleased him.",
      "T": "Then Michal—Saul's other daughter—fell in love with David. Saul was told, and it pleased him: another opportunity."
    },
    "21": {
      "L": "And Saul said, I will give him her that she may be a snare to him and that the hand of the Philistines may be against him. Wherefore Saul said to David, Thou shalt this day be my son in law in the one of the twain.",
      "M": "Saul said to himself, 'I will give her to him; she will be a trap for him so that the Philistines may strike him.' So Saul said to David, 'You shall be my son-in-law today through one of the two.'",
      "T": "Saul told himself: 'I will use her. Let her be his snare—let his own wife's love send him into Philistine territory enough times that they kill him.' He told David openly: 'You will be my son-in-law—through one of my daughters.'"
    },
    "22": {
      "L": "And Saul commanded his servants saying, Commune with David secretly and say, Behold the king hath delight in thee and all his servants love thee; now therefore be the king's son in law.",
      "M": "Saul instructed his servants: 'Speak to David privately—tell him the king is pleased with him and all his servants love him. Encourage him to become the king's son-in-law.'",
      "T": "He gave his servants secret instructions: 'Go to David and tell him privately—the king approves of him, the whole court loves him, and this is the time to become the king's son-in-law.'"
    },
    "23": {
      "L": "And Saul's servants spake those words in the ears of David. And David said, Seemeth it to you a light thing to be a king's son in law seeing that I am a poor man and lightly esteemed?",
      "M": "Saul's servants spoke these words to David, and David replied, 'Does it seem a small thing to you to be the king's son-in-law, when I am a poor man of no importance?'",
      "T": "The servants relayed Saul's message. David answered honestly: 'Do you think it costs nothing to marry into the royal house? I am a poor man—nobody. I cannot afford this.'"
    },
    "24": {
      "L": "And the servants of Saul told him saying, On this manner spake David.",
      "M": "Saul's servants reported back to him, saying, 'This is what David said.'",
      "T": "The servants went back to Saul and reported what David had said."
    },
    "25": {
      "L": "And Saul said, Thus shall ye say to David, The king desireth not any dowry but an hundred foreskins of the Philistines to be avenged of the king's enemies. But Saul thought to make David fall by the hand of the Philistines.",
      "M": "Saul replied, 'Say this to David: the king wants no dowry but a hundred foreskins of the Philistines, as vengeance against the king's enemies.' Saul was planning to have David fall by the hand of the Philistines.",
      "T": "Saul sent back his answer: 'The king has no interest in a traditional bride-price. What he wants is a hundred Philistine foreskins—proof of his enemies killed.' The subtext was clear in Saul's own mind: send David into enough battles and the Philistines will do the killing for him."
    },
    "26": {
      "L": "And when his servants told David these words it pleased David well to be the king's son in law; and the days were not expired.",
      "M": "When Saul's servants told David these terms, it seemed good to David to become the king's son-in-law. The time allotted had not yet passed.",
      "T": "David heard the terms and accepted them—being the king's son-in-law was worth the risk. He set out before the deadline."
    },
    "27": {
      "L": "Wherefore David arose and went he and his men and slew of the Philistines two hundred men; and David brought their foreskins and they gave them in full tale to the king that he might be the king's son in law. And Saul gave him Michal his daughter to wife.",
      "M": "David and his men went out and struck down two hundred Philistines. He brought their foreskins and presented them in full count to the king, so that he could become the king's son-in-law. Saul gave him his daughter Michal as his wife.",
      "T": "David led his men out and killed two hundred Philistines—double the required number. He brought the foreskins back and laid them before the king, count verified. Saul had no choice but to give Michal to David as his wife."
    },
    "28": {
      "L": "And Saul saw and knew that the LORD was with David; and Michal Saul's daughter loved him.",
      "M": "Saul recognized that the LORD was with David and that his daughter Michal loved him.",
      "T": "Saul could see it plainly: the LORD was with David. And Michal—his own daughter—loved him deeply. Every tie between Saul and safety was drawing closer to David."
    },
    "29": {
      "L": "And Saul was yet the more afraid of David; and Saul became David's enemy continually.",
      "M": "Saul became even more afraid of David, and Saul was David's enemy from then on.",
      "T": "Saul's fear deepened, hardened, and settled into something permanent: Saul became David's enemy—not in a moment of rage, but as a fixed disposition of his soul."
    },
    "30": {
      "L": "Then the princes of the Philistines went forth; and it came to pass after they went forth that David behaved himself more wisely than all the servants of Saul; so that his name was much set by.",
      "M": "The Philistine commanders continued to go out on raids. Whenever they did, David performed more successfully than all of Saul's other officers, and his reputation grew greatly.",
      "T": "Campaign after campaign, whenever the Philistine commanders launched raids into Israel, David outperformed every other officer in Saul's service. His name grew and grew—and with it, Saul's dread."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '1samuel', existing)
    print('1 Samuel 16–18 written.')

if __name__ == '__main__':
    main()
