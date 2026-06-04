"""
MKT 1 Kings chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1kings-13-18.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T.
  Consistent with mkt-1kings-1-6.py.
- H430 (אֱלֹהִים): "God" in all tiers.
- H1168 (Baal): Preserved as proper name throughout. In T at 16:31 and 18:21 the naming
  dynamics are noted; the term means "lord/master" in Canaanite religion — significant
  contrast with the LORD as Israel's true Lord.
- H5315 (נֶפֶשׁ): 17:21-22 "soul/life/breath." L: "soul" (source-literal); M: "life";
  T: "breath of life" — in 17:21-22 the idiom "let this child's soul/life come into him
  again" is about breath returning, not a Greek immortal soul. Context demands this.
- H7307 (רוּחַ): 18:12 "Spirit of the LORD" — Spirit (capitalized) in all tiers. This is
  clearly the divine ruach acting as agent, not wind or breath.
- H5030 (nābî'): "prophet" throughout all tiers.
- H1116 (bāmôt / high places): "high places" in L/M; T occasionally varies to "hilltop
  shrines" where the cultic critique is in view (14:23; 15:14).
- H6918 + H6945 (qādēsh / male cult prostitutes, "sodomites"): Rendered "male cult
  prostitutes" in L/M; T "male shrine prostitutes." The older translation "sodomites" is
  avoided — the Hebrew refers to men dedicated to cultic sexual service in Canaanite
  fertility shrines, not to the city of Sodom.
- H842 (ʾăšērāh): "Asherah" / "Asherah pole" — Asherah is the Canaanite goddess; her
  cult image/pole (H842) is rendered "Asherah pole" or "sacred pole" in M/T.
- H4906 (maṣṣēbôt / sacred pillars): "sacred pillars" in L/M; T "standing-stones" where
  appropriate to preserve the cultic sense.
- H4428 (melek / king): "king" throughout; no variation.
- H2617 (חֶסֶד): Not prominent in chs 13–18. Does not appear.
- H1285 (בְּרִית / covenant): 15:19 "league" in L (treaty); M/T "treaty" — this is a
  political covenant between Ben-hadad and Asa, not a divine covenant.
  In v.19 the word is "league/treaty/covenant" (berît). L keeps "league" (older idiom that
  preserves the formal character); M/T use "treaty."
- Elijah: His name (H452, ʾĒliyyāhû) means "My God is Yahweh" — highly significant in
  chapters 17–18 where Yahweh versus Baal is the central conflict. T notes this at 17:1.
- Obadiah: His name (H5662, ʿObadyāh) means "servant of Yahweh." T notes this at 18:3.
- "Man of God" (H376 + H430, ʾîsh hāʾělōhîm): Consistent title throughout ch 13.
- H3027 (yad / hand): In 18:46 "the hand of the LORD was on Elijah" — L "hand of the
  LORD"; M "power of the LORD"; T "the LORD's power came upon Elijah."
- Aspect notes for chs 13–18: Waw-consecutive imperfects throughout = narrative past.
  Divine speech (14:7-11; 16:1-4; 17:2-4, 8-9, 13-14) uses future/promise forms.
  Elijah's prayer in 18:36-37 = vocative + perfect + imperfect in petition.
- Chapter 13 literary-critical note: The story of the "old prophet" who deceives the
  "man of God" is deliberately paradoxical — the liar speaks a true judgment (v.21-22)
  and buries the man of God with genuine grief (v.29-31). The narrative resists easy
  moralizing. The man of God's failure was disobeying the LORD's specific command, even
  for a seemingly pious reason (obeying a supposed prophetic word). T surfaces this.
- Chapter 16 note: Zimri's 7-day reign (v.15) is the shortest in the Hebrew Bible.
  Hiel's rebuilding of Jericho (16:34) deliberately echoes Josh 6:26 — the fulfillment
  is described as "according to the word of the LORD which he spoke by Joshua son of Nun."
  T makes this echo explicit.
- Chapters 17–18 note: Elijah narrative marks a sharp turn in the Deuteronomistic History.
  The drought announcement (17:1) is based on the covenant curse of Lev 26:19 and
  Deut 28:23-24. The contest on Carmel inverts the fertility claims of Baal worship —
  Baal was supposedly the storm and rain god; Yahweh proves to be the true rainmaker.
  T surfaces these dynamics throughout.
- OT echoes in these chapters:
  - 13:2: The prophecy "a son named Josiah will be born to the house of David" is
    fulfilled in 2 Kings 23:15-20 — approximately 300 years later, one of the most
    remarkable predictive prophecies in the OT. T notes this explicitly.
  - 14:15: "as a reed shaken in water" — imagery of fragility under divine judgment.
  - 15:4-5: David is the measure of kingship throughout; "for David's sake" is the
    Deuteronomistic grace-formula for Judah's survival.
  - 16:34: Joshua 6:26 curse fulfilled. T marks this.
  - 17:1: Elijah's name and his role echo the Mosaic tradition. The drought announcement
    echoes Deut 11:16-17 and Lev 26:19.
  - 18:31-32: The 12 stones echo the original 12-tribe unity; a pointed act in the
    context of the divided kingdom.
  - 18:36: "God of Abraham, Isaac, and Israel" — Elijah deliberately uses "Israel" (not
    "Jacob") to evoke the covenant name and national identity.
  - 18:39: "The LORD, he is God" — the confession echoes the meaning of Elijah's own name
    (ʾĒliyyāhû = My God is Yahweh). T makes this explicit.
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

KINGS = {
  "13": {
    "1": {
      "L": "And behold, a man of God came from Judah by the word of the LORD to Bethel. And Jeroboam was standing by the altar to burn incense.",
      "M": "A man of God came from Judah by the word of the LORD to Bethel, just as Jeroboam was standing by the altar to burn incense.",
      "T": "By the word of the LORD, a man of God came from Judah to Bethel. Jeroboam was standing at the altar about to burn incense."
    },
    "2": {
      "L": "And he cried against the altar by the word of the LORD and said, 'O altar, altar, thus says the LORD: Behold, a son shall be born to the house of David, Josiah by name, and he shall sacrifice upon you the priests of the high places who burn incense upon you, and human bones shall be burned upon you.'",
      "M": "He cried out against the altar by the word of the LORD: 'O altar, altar, thus says the LORD: A son will be born to the house of David—Josiah is his name—and he will sacrifice on you the priests of the high places who burn incense on you, and human bones will be burned on you.'",
      "T": "He called out against the altar by the word of the LORD: 'Altar! Altar! This is what the LORD says: A son will be born to the house of David—his name will be Josiah—and he will sacrifice on you the very priests of the high places who burn incense here, and human bones will be burned on you.' (This prophecy would be fulfilled some three hundred years later, in the reign of Josiah of Judah.)"
    },
    "3": {
      "L": "He gave a sign the same day, saying, 'This is the sign that the LORD has spoken: Behold, the altar shall be split, and the ashes that are on it shall be poured out.'",
      "M": "He also gave a sign that same day: 'This is the sign the LORD has spoken: The altar will be split and the ashes on it will be poured out.'",
      "T": "He gave a sign that very day: 'This is the sign the LORD has declared: the altar will split apart and the ashes on it will spill to the ground.'"
    },
    "4": {
      "L": "And when King Jeroboam heard the saying of the man of God which he cried against the altar at Bethel, he stretched out his hand from the altar, saying, 'Seize him!' And his hand that he stretched out against him dried up, so that he could not pull it back to himself.",
      "M": "When King Jeroboam heard what the man of God cried against the altar at Bethel, he stretched out his hand from the altar and said, 'Seize him!' But his outstretched hand withered so that he could not draw it back.",
      "T": "When King Jeroboam heard what the man of God cried out against the altar at Bethel, he thrust out his hand from the altar and shouted, 'Seize him!' But his hand shriveled up and he could not pull it back."
    },
    "5": {
      "L": "The altar also was split, and the ashes poured out from the altar, according to the sign which the man of God had given by the word of the LORD.",
      "M": "The altar also split apart and the ashes spilled from it, according to the sign the man of God had given by the word of the LORD.",
      "T": "The altar split apart and the ashes spilled from it, just as the man of God had declared by the word of the LORD."
    },
    "6": {
      "L": "And the king said to the man of God, 'Entreat now the favor of the LORD your God, and pray for me, that my hand may be restored to me.' And the man of God entreated the LORD, and the king's hand was restored to him and became as it was before.",
      "M": "The king said to the man of God, 'Please pray to the LORD your God and ask his favor for me, that my hand may be restored.' The man of God prayed to the LORD, and the king's hand was restored and became as it was before.",
      "T": "The king said to the man of God: 'Please, entreat the LORD your God and pray for me, that my hand might be restored.' The man of God prayed to the LORD, and the king's hand was restored—just as it had been."
    },
    "7": {
      "L": "And the king said to the man of God, 'Come home with me and refresh yourself, and I will give you a reward.'",
      "M": "The king said to the man of God, 'Come home with me and have some food, and I will give you a gift.'",
      "T": "The king said to the man of God: 'Come home with me, eat something, and I will give you a reward.'"
    },
    "8": {
      "L": "And the man of God said to the king, 'If you give me half your house, I will not go in with you, nor will I eat bread or drink water in this place.'",
      "M": "But the man of God said to the king, 'Even if you gave me half your palace, I would not go with you, nor eat bread nor drink water in this place.'",
      "T": "The man of God answered the king: 'Even if you gave me half your palace, I would not go with you, nor eat bread nor drink water here.'"
    },
    "9": {
      "L": "'For so was I commanded by the word of the LORD, saying, You shall not eat bread or drink water, nor return by the way that you came.'",
      "M": "'For the LORD commanded me by his word: You shall not eat bread nor drink water, nor return by the way you came.'",
      "T": "'The LORD commanded me by his word: Do not eat bread, do not drink water, and do not go back by the way you came.'"
    },
    "10": {
      "L": "So he went another way and did not return by the way that he had come to Bethel.",
      "M": "So he went home by a different route and did not return the way he had come to Bethel.",
      "T": "So he left by a different road and did not return the way he had come to Bethel."
    },
    "11": {
      "L": "Now there dwelt an old prophet in Bethel. And his sons came and told him all the works that the man of God had done that day in Bethel, the words also which he had spoken to the king, and they told them to their father.",
      "M": "Now an old prophet lived in Bethel. His sons came and told him everything the man of God had done that day in Bethel—the words he had spoken to the king—and they reported it all to their father.",
      "T": "An old prophet was living in Bethel. His sons came home and told him everything the man of God had done that day in Bethel—every word he had spoken to the king."
    },
    "12": {
      "L": "And their father said to them, 'Which way did he go?' And his sons showed him the way that the man of God who came from Judah had gone.",
      "M": "Their father asked them, 'Which way did he go?' His sons showed him the road the man of God from Judah had taken.",
      "T": "Their father asked: 'Which way did he go?' His sons pointed out the road the man of God from Judah had taken."
    },
    "13": {
      "L": "And he said to his sons, 'Saddle the donkey for me.' So they saddled the donkey for him and he rode on it.",
      "M": "He said to his sons, 'Saddle the donkey for me.' They saddled it and he rode off.",
      "T": "He said: 'Saddle the donkey.' They saddled it, and he rode away."
    },
    "14": {
      "L": "And he went after the man of God and found him sitting under an oak. And he said to him, 'Are you the man of God who came from Judah?' And he said, 'I am.'",
      "M": "He rode after the man of God and found him sitting under an oak tree. He asked, 'Are you the man of God who came from Judah?' 'I am,' he answered.",
      "T": "He rode after the man of God and found him sitting under an oak tree. 'Are you the man of God who came from Judah?' he asked. 'I am,' he said."
    },
    "15": {
      "L": "Then he said to him, 'Come home with me and eat bread.'",
      "M": "Then he said to him, 'Come home with me and have something to eat.'",
      "T": "The old prophet said: 'Come home with me and eat.'"
    },
    "16": {
      "L": "And he said, 'I may not return with you, nor go in with you, neither will I eat bread nor drink water with you in this place.'",
      "M": "He answered, 'I cannot go back with you or go in with you, nor will I eat bread or drink water with you here.'",
      "T": "The man of God answered: 'I cannot return with you or go in with you. I will not eat bread or drink water with you in this place.'"
    },
    "17": {
      "L": "'For it was said to me by the word of the LORD, You shall not eat bread or drink water there, nor turn again to go by the way that you came.'",
      "M": "'For the LORD commanded me by his word: You shall not eat bread or drink water there, nor go back by the way you came.'",
      "T": "'The LORD's word to me was this: Do not eat bread there, do not drink water there, and do not go back the way you came.'"
    },
    "18": {
      "L": "He said to him, 'I also am a prophet as you are, and an angel spoke to me by the word of the LORD, saying, Bring him back with you into your house, that he may eat bread and drink water.' But he was lying to him.",
      "M": "The old prophet said to him, 'I too am a prophet like you, and an angel spoke to me by the word of the LORD, saying, Bring him back with you so he can eat bread and drink water.' But he was lying to him.",
      "T": "The old prophet said: 'I am also a prophet like you, and an angel told me by the word of the LORD: Bring him back home so he can eat and drink.' But he was lying."
    },
    "19": {
      "L": "So he went back with him and ate bread in his house and drank water.",
      "M": "So the man of God went back with him and ate and drank at his house.",
      "T": "So the man of God turned back with him and ate and drank at his house."
    },
    "20": {
      "L": "And as they sat at the table, the word of the LORD came to the prophet who had brought him back.",
      "M": "While they were sitting at the table, the word of the LORD came to the prophet who had brought him back.",
      "T": "While they were sitting at the table, the word of the LORD came to the prophet who had brought him back."
    },
    "21": {
      "L": "And he cried to the man of God who came from Judah, 'Thus says the LORD: Because you have disobeyed the command of the LORD and have not kept the commandment that the LORD your God commanded you,'",
      "M": "He called out to the man of God who came from Judah: 'Thus says the LORD: Because you have disobeyed the word of the LORD and have not kept the commandment the LORD your God commanded you,'",
      "T": "He cried out to the man of God from Judah: 'This is what the LORD says: Because you defied the word of the LORD and did not keep the command the LORD your God gave you—'"
    },
    "22": {
      "L": "'but have come back and have eaten bread and drunk water in the place of which he said to you, Eat no bread and drink no water, your body shall not come to the tomb of your fathers.'",
      "M": "'but came back and ate bread and drank water in the place where he told you, Eat no bread and drink no water—your body will not come to the tomb of your ancestors.'",
      "T": "'because you came back and ate bread and drank water in the very place where he said, Do not eat, do not drink—your body will not be buried in the tomb of your fathers.'"
    },
    "23": {
      "L": "And after he had eaten bread and drunk water, he saddled the donkey for the prophet whom he had brought back.",
      "M": "After the man of God had eaten and drunk, the old prophet saddled the donkey for him.",
      "T": "After he had eaten and drunk, the old prophet saddled the donkey for the man of God he had brought back."
    },
    "24": {
      "L": "And as he went, a lion met him on the road and killed him. And his body was thrown in the road, and the donkey stood beside it, and the lion also stood beside the body.",
      "M": "As the man of God went on his way, a lion met him on the road and killed him. His body lay thrown on the road, and the donkey stood beside it, and the lion also stood beside the body.",
      "T": "On the road a lion met him and killed him. His body lay on the road; the donkey stood beside it, and the lion stood beside the body."
    },
    "25": {
      "L": "And behold, men passed by and saw the body thrown in the road with the lion standing beside the body. And they came and told it in the city where the old prophet lived.",
      "M": "Some men who passed by saw the body on the road with the lion standing beside it. They went and reported it in the city where the old prophet lived.",
      "T": "Passersby saw the body on the road and the lion standing beside it. They went and reported it in the city where the old prophet lived."
    },
    "26": {
      "L": "And when the prophet who had brought him back from the way heard it, he said, 'It is the man of God who disobeyed the word of the LORD. Therefore the LORD has given him to the lion, which has torn him and killed him, according to the word of the LORD which he spoke to him.'",
      "M": "When the prophet who had brought him back heard it, he said, 'It is the man of God who disobeyed the word of the LORD. Therefore the LORD gave him to the lion, which tore and killed him, according to the word the LORD had spoken to him.'",
      "T": "When the old prophet who had brought him back heard it, he said: 'It is the man of God who defied the word of the LORD. The LORD gave him to the lion, and the lion tore him and killed him—exactly as the LORD had warned him.'"
    },
    "27": {
      "L": "And he spoke to his sons, saying, 'Saddle the donkey for me.' And they saddled it.",
      "M": "He told his sons, 'Saddle the donkey for me.' They saddled it.",
      "T": "He said to his sons: 'Saddle the donkey.' They saddled it."
    },
    "28": {
      "L": "And he went and found the body thrown in the road with the donkey and the lion standing beside the body. The lion had not eaten the body and had not torn the donkey.",
      "M": "He went and found the body on the road with the donkey and the lion still standing there. The lion had not eaten the body or torn the donkey.",
      "T": "He went and found the body lying on the road, with the donkey and the lion still standing beside it. The lion had not eaten the body, nor had it touched the donkey."
    },
    "29": {
      "L": "And the prophet took up the body of the man of God and laid it on the donkey and brought it back to the city to mourn and to bury him.",
      "M": "The old prophet picked up the man of God's body, laid it on the donkey, and brought it back to the city to mourn over it and bury it.",
      "T": "The old prophet lifted the body of the man of God, laid it on the donkey, and brought it back to the city to mourn over him and bury him."
    },
    "30": {
      "L": "And he laid the body in his own grave, and they mourned over him, saying, 'Alas, my brother!'",
      "M": "He buried the body in his own tomb, and they mourned over him, saying, 'Alas, my brother!'",
      "T": "He laid the body in his own tomb, and they mourned over him, crying, 'Alas, my brother!'"
    },
    "31": {
      "L": "And after he had buried him, he said to his sons, 'When I die, bury me in the grave where the man of God is buried. Lay my bones beside his bones.'",
      "M": "After he had buried him, he said to his sons, 'When I die, bury me in the same grave where the man of God is buried. Lay my bones beside his bones.'",
      "T": "After the burial, the old prophet said to his sons: 'When I die, bury me in this same grave. Lay my bones beside the bones of the man of God.'"
    },
    "32": {
      "L": "'For the saying that he cried by the word of the LORD against the altar in Bethel and against all the houses of the high places that are in the cities of Samaria shall surely come to pass.'",
      "M": "'For the oracle he declared by the word of the LORD against the altar in Bethel and against all the shrines of the high places in the cities of Samaria will certainly be fulfilled.'",
      "T": "'For the word he proclaimed by the LORD against the altar in Bethel and against all the hilltop shrines in the cities of Samaria will certainly come true.'"
    },
    "33": {
      "L": "After this Jeroboam did not turn from his evil way, but made priests for the high places again from among all the people. Whoever wished, he ordained as priests of the high places.",
      "M": "Even after this, Jeroboam did not turn from his evil ways. He continued appointing priests for the high places from all sorts of people. Anyone who wanted to could become a priest of the high places.",
      "T": "Even after all this, Jeroboam did not turn from his evil ways. He kept consecrating priests for the high places from all kinds of people. Anyone who wanted to be could become a priest of the high places."
    },
    "34": {
      "L": "And this thing became sin to the house of Jeroboam, so as to cut it off and to destroy it from the face of the earth.",
      "M": "This became the sin of the house of Jeroboam that would cut it off and wipe it from the face of the earth.",
      "T": "This became the sin that would bring down the house of Jeroboam—the sin that would cut it off and wipe it from the face of the earth."
    }
  },
  "14": {
    "1": {
      "L": "At that time Abijah the son of Jeroboam fell sick.",
      "M": "At that time Jeroboam's son Abijah became ill.",
      "T": "At that time Abijah, Jeroboam's son, became ill."
    },
    "2": {
      "L": "And Jeroboam said to his wife, 'Arise, and disguise yourself, that you will not be known as the wife of Jeroboam, and go to Shiloh. Behold, Ahijah the prophet is there, who told me that I should be king over this people.'",
      "M": "Jeroboam said to his wife, 'Get up and disguise yourself so no one will know you are the wife of Jeroboam, then go to Shiloh. Ahijah the prophet is there—the one who told me I would be king over this people.'",
      "T": "Jeroboam said to his wife: 'Get up and disguise yourself so you won't be recognized as my wife. Go to Shiloh—Ahijah the prophet is there, the one who told me I would be king over this people.'"
    },
    "3": {
      "L": "'And take with you ten loaves, some cakes, and a jar of honey, and go to him. He will tell you what shall happen to the child.'",
      "M": "'Take with you ten loaves of bread, some cakes, and a jar of honey, and go to him. He will tell you what will happen to the child.'",
      "T": "'Take ten loaves of bread, some cakes, and a jar of honey. He will tell you what will happen to the boy.'"
    },
    "4": {
      "L": "So Jeroboam's wife did so. She arose and went to Shiloh and came to the house of Ahijah. Now Ahijah could not see, for his eyes were dim because of his age.",
      "M": "So Jeroboam's wife did as he said. She went to Shiloh and entered Ahijah's house. But Ahijah could not see—his eyes had grown dim with age.",
      "T": "Jeroboam's wife did as he said. She went to Shiloh and came to Ahijah's house. But Ahijah could not see—his eyes had gone dim with age."
    },
    "5": {
      "L": "But the LORD said to Ahijah, 'Behold, the wife of Jeroboam is coming to inquire of you concerning her son, for he is sick. Thus and thus shall you say to her.' Now when she came in she pretended to be another woman.",
      "M": "But the LORD had told Ahijah, 'The wife of Jeroboam is coming to ask you about her son—he is sick. You shall say such and such to her.' When she came in, she was disguised.",
      "T": "But the LORD had said to Ahijah: 'The wife of Jeroboam is on her way to ask you about her son—he is sick. Tell her this and this.' When she arrived, she was in disguise."
    },
    "6": {
      "L": "When Ahijah heard the sound of her feet as she came in at the door, he said, 'Come in, wife of Jeroboam. Why do you pretend to be another? For I am charged with heavy news for you.'",
      "M": "When Ahijah heard her footsteps at the door, he said, 'Come in, wife of Jeroboam. Why do you pretend to be someone else? I have been sent to you with difficult news.'",
      "T": "When Ahijah heard her footsteps at the door, he said: 'Come in, wife of Jeroboam. Why are you pretending to be someone else? I have been sent to you with a hard message.'"
    },
    "7": {
      "L": "'Go, tell Jeroboam, Thus says the LORD the God of Israel: Because I exalted you from among the people and made you leader over my people Israel,'",
      "M": "'Go, say to Jeroboam: Thus says the LORD the God of Israel: I raised you up from among the people and made you ruler over my people Israel,'",
      "T": "'Go, tell Jeroboam: This is what the LORD, the God of Israel, says: I lifted you up from among the people and made you ruler over my people Israel.'"
    },
    "8": {
      "L": "'and I tore the kingdom away from the house of David and gave it to you, and yet you have not been like my servant David, who kept my commandments and who followed me with all his heart, doing only what was right in my eyes,'",
      "M": "'I tore the kingdom away from the house of David and gave it to you. Yet you have not been like my servant David, who kept my commandments and followed me wholeheartedly, doing only what was right in my eyes.'",
      "T": "'I tore the kingdom from the house of David and gave it to you. But you have not been like my servant David, who kept my commandments and followed me with his whole heart, doing only what was right in my sight.'"
    },
    "9": {
      "L": "'but you have done more evil than all who were before you and have gone and made for yourself other gods and metal images, provoking me to anger, and have cast me behind your back.'",
      "M": "'Instead you have done more evil than all who came before you. You have made for yourself other gods and cast images, provoking me to anger, and have thrown me behind your back.'",
      "T": "'Instead you have done more evil than anyone before you. You made other gods and cast metal images to provoke me, and you have thrown me aside as if I did not exist.'"
    },
    "10": {
      "L": "'Therefore behold, I will bring evil upon the house of Jeroboam and will cut off from Jeroboam every male, bond or free, in Israel, and will burn up the house of Jeroboam as a man burns up dung until it is all gone.'",
      "M": "'Therefore I am bringing disaster on the house of Jeroboam. I will cut off from Jeroboam every male, slave or free, in Israel. I will sweep away the house of Jeroboam as one sweeps away dung, until nothing is left.'",
      "T": "'Therefore I am bringing disaster on the house of Jeroboam. I will cut off every male, slave or free, in Israel. I will sweep away the house of Jeroboam like dung that is swept away until nothing remains.'"
    },
    "11": {
      "L": "'Anyone belonging to Jeroboam who dies in the city the dogs shall eat, and anyone who dies in the open country the birds of the heavens shall eat, for the LORD has spoken it.'",
      "M": "'Anyone from Jeroboam's house who dies in the city the dogs will eat, and anyone who dies in the countryside the birds of the air will eat. The LORD has spoken.'",
      "T": "'Anyone of Jeroboam's house who dies in the city, the dogs will eat. Anyone who dies in the open field, the birds of the sky will eat. The LORD has spoken.'"
    },
    "12": {
      "L": "'Arise therefore, go to your house. When your feet enter the city the child shall die.'",
      "M": "'Get up now and go home. The moment your feet enter the city, the child will die.'",
      "T": "'Go home now. The moment your feet cross the city threshold, the child will die.'"
    },
    "13": {
      "L": "'And all Israel shall mourn for him and bury him, for he alone of Jeroboam shall come to the grave, because in him there is found something pleasing to the LORD the God of Israel in the house of Jeroboam.'",
      "M": "'All Israel will mourn for him and bury him—he is the only one of Jeroboam's house who will be given a proper burial, because in him the LORD the God of Israel has found something good.'",
      "T": "'All Israel will mourn for him and give him a proper burial. He is the only one in Jeroboam's house whom the LORD the God of Israel has found to have any goodness in him.'"
    },
    "14": {
      "L": "'Moreover the LORD will raise up for himself a king over Israel who shall cut off the house of Jeroboam today. And henceforth what?—even now.'",
      "M": "'And the LORD will raise up for himself a king over Israel who will cut off the house of Jeroboam—yes, even today. But what has already begun?—it has already begun.'",
      "T": "'The LORD will raise up for himself a king over Israel who will destroy the house of Jeroboam. And that day is coming—it has already begun.'"
    },
    "15": {
      "L": "'And the LORD will strike Israel as a reed is shaken in the water, and root up Israel out of this good land that he gave to their fathers, and scatter them beyond the Euphrates, because they have made their Asherah poles, provoking the LORD to anger.'",
      "M": "'The LORD will strike Israel as a reed is shaken in the water. He will uproot Israel from this good land he gave their ancestors and scatter them beyond the Euphrates, because they provoked him to anger by making Asherah poles.'",
      "T": "'The LORD will strike Israel—shaking her like a reed in the water. He will uproot Israel from this good land he gave their fathers and scatter them beyond the Euphrates River, because they have provoked him to anger by making their Asherah poles.'"
    },
    "16": {
      "L": "'And he will give Israel up because of the sins of Jeroboam, who sinned and who made Israel to sin.'",
      "M": "'He will abandon Israel because of the sins of Jeroboam, who sinned and caused Israel to sin.'",
      "T": "'He will hand Israel over—because of the sins of Jeroboam, who sinned and who led all Israel into sin.'"
    },
    "17": {
      "L": "Then Jeroboam's wife arose and departed and came to Tirzah. And as she came to the threshold of the house, the child died.",
      "M": "Jeroboam's wife got up and went back to Tirzah. As she crossed the threshold of the house, the child died.",
      "T": "Jeroboam's wife got up and left. She came to Tirzah, and the moment she stepped across the threshold, the child died."
    },
    "18": {
      "L": "And they buried him, and all Israel mourned for him, according to the word of the LORD that he spoke by his servant Ahijah the prophet.",
      "M": "They buried him, and all Israel mourned for him, as the LORD had said through his servant Ahijah the prophet.",
      "T": "They buried him, and all Israel mourned—just as the LORD had spoken through his servant Ahijah the prophet."
    },
    "19": {
      "L": "Now the rest of the acts of Jeroboam, how he warred and how he reigned, behold, they are written in the Book of the Chronicles of the Kings of Israel.",
      "M": "The rest of the acts of Jeroboam—how he made war and how he reigned—are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "As for the rest of Jeroboam's acts—his wars and his reign—they are recorded in the Book of the Chronicles of the Kings of Israel."
    },
    "20": {
      "L": "And the time that Jeroboam reigned was twenty-two years. And he slept with his fathers, and Nadab his son reigned in his place.",
      "M": "Jeroboam reigned twenty-two years. He rested with his ancestors, and his son Nadab reigned in his place.",
      "T": "Jeroboam reigned twenty-two years. He rested with his fathers, and his son Nadab succeeded him."
    },
    "21": {
      "L": "Now Rehoboam the son of Solomon reigned in Judah. Rehoboam was forty-one years old when he began to reign, and he reigned seventeen years in Jerusalem, the city that the LORD had chosen out of all the tribes of Israel to put his name there. His mother's name was Naamah the Ammonitess.",
      "M": "Rehoboam son of Solomon reigned in Judah. He was forty-one years old when he became king and reigned seventeen years in Jerusalem, the city the LORD had chosen from all the tribes of Israel as the place for his name. His mother was Naamah the Ammonite.",
      "T": "Rehoboam son of Solomon reigned in Judah. He was forty-one years old when he came to the throne and reigned seventeen years in Jerusalem—the city the LORD had chosen from all the tribes of Israel to place his name there. His mother was Naamah, an Ammonite."
    },
    "22": {
      "L": "And Judah did what was evil in the sight of the LORD, and they provoked him to jealousy with their sins that they committed, more than all that their fathers had done.",
      "M": "Judah did what was evil in the sight of the LORD. With their sins they provoked him to jealousy more than all that their ancestors had done.",
      "T": "Judah did what was evil in the sight of the LORD. Their sins provoked him to jealousy more than anything their ancestors had done."
    },
    "23": {
      "L": "For they also built for themselves high places and pillars and Asherah poles on every high hill and under every green tree,",
      "M": "They built high places, sacred pillars, and Asherah poles on every high hill and under every spreading tree.",
      "T": "They built hilltop shrines, standing-stones, and Asherah poles on every high hill and under every leafy tree."
    },
    "24": {
      "L": "and there were also male cult prostitutes in the land. They did according to all the abominations of the nations that the LORD drove out before the people of Israel.",
      "M": "There were also male cult prostitutes in the land. Judah practiced all the abominations of the nations the LORD had driven out before the Israelites.",
      "T": "There were also male shrine prostitutes in the land. Judah committed all the abominations of the nations the LORD had driven out before Israel."
    },
    "25": {
      "L": "In the fifth year of King Rehoboam, Shishak king of Egypt came up against Jerusalem.",
      "M": "In the fifth year of King Rehoboam, Shishak king of Egypt marched against Jerusalem.",
      "T": "In the fifth year of King Rehoboam, Shishak king of Egypt attacked Jerusalem."
    },
    "26": {
      "L": "He took away the treasures of the house of the LORD and the treasures of the king's house. He took everything. He also took away all the shields of gold that Solomon had made.",
      "M": "He carried off the treasures of the house of the LORD and the treasures of the royal palace—he took everything. He also took all the gold shields Solomon had made.",
      "T": "He stripped the temple treasury and the royal palace treasury. He took everything—including all the gold shields Solomon had made."
    },
    "27": {
      "L": "And in their place King Rehoboam made shields of bronze and committed them to the hands of the officers of the guard who kept the door of the king's house.",
      "M": "In their place King Rehoboam made bronze shields and put them in the care of the commanders of the guard who kept watch at the entrance to the palace.",
      "T": "In their place Rehoboam made bronze shields and entrusted them to the commanders of the guard who stood watch at the palace entrance."
    },
    "28": {
      "L": "And as often as the king went into the house of the LORD, the guard bore them and brought them back to the guardroom.",
      "M": "Whenever the king went to the house of the LORD, the guard carried the shields and then brought them back to the guardroom.",
      "T": "Whenever the king went to the house of the LORD, the guard carried the shields out—and brought them back to the guardroom afterward."
    },
    "29": {
      "L": "Now the rest of the acts of Rehoboam and all that he did, are they not written in the Book of the Chronicles of the Kings of Judah?",
      "M": "The rest of the acts of Rehoboam and all that he did are written in the Book of the Chronicles of the Kings of Judah.",
      "T": "As for the rest of Rehoboam's acts and all that he did, they are recorded in the Book of the Chronicles of the Kings of Judah."
    },
    "30": {
      "L": "And there was war between Rehoboam and Jeroboam all their days.",
      "M": "There was war between Rehoboam and Jeroboam throughout their reigns.",
      "T": "War continued between Rehoboam and Jeroboam throughout their lifetimes."
    },
    "31": {
      "L": "And Rehoboam slept with his fathers and was buried with his fathers in the city of David. His mother's name was Naamah the Ammonitess. And Abijam his son reigned in his place.",
      "M": "Rehoboam rested with his ancestors and was buried with them in the city of David. His mother was Naamah the Ammonite. His son Abijam reigned in his place.",
      "T": "Rehoboam rested with his fathers and was buried in the city of David. His mother was Naamah, an Ammonite. His son Abijam succeeded him."
    }
  },
  "15": {
    "1": {
      "L": "Now in the eighteenth year of King Jeroboam the son of Nebat, Abijam began to reign over Judah.",
      "M": "In the eighteenth year of King Jeroboam son of Nebat, Abijam became king of Judah.",
      "T": "In the eighteenth year of King Jeroboam son of Nebat, Abijam became king of Judah."
    },
    "2": {
      "L": "He reigned for three years in Jerusalem. His mother's name was Maacah the daughter of Abishalom.",
      "M": "He reigned three years in Jerusalem. His mother was Maacah daughter of Abishalom.",
      "T": "He reigned three years in Jerusalem. His mother was Maacah daughter of Abishalom."
    },
    "3": {
      "L": "And he walked in all the sins of his father, which he had done before him, and his heart was not perfect with the LORD his God, as the heart of David his father.",
      "M": "He committed all the sins of his father and did not have a heart fully devoted to the LORD his God, as David his ancestor had.",
      "T": "He walked in all the sins his father had committed before him. His heart was not fully devoted to the LORD his God, as the heart of David had been."
    },
    "4": {
      "L": "Nevertheless for David's sake the LORD his God gave him a lamp in Jerusalem, setting up his son after him, and establishing Jerusalem,",
      "M": "Nevertheless, for David's sake the LORD his God gave him a lamp in Jerusalem by raising up his son after him and by establishing Jerusalem.",
      "T": "Nevertheless, for David's sake the LORD his God gave him a lamp in Jerusalem—he kept a successor on the throne and preserved Jerusalem."
    },
    "5": {
      "L": "because David did what was right in the eyes of the LORD and did not turn aside from anything that he commanded him all the days of his life, except in the matter of Uriah the Hittite.",
      "M": "David had done what was right in the LORD's sight and had not turned aside from anything he commanded throughout his life—except in the matter of Uriah the Hittite.",
      "T": "David had done what was right in the LORD's eyes and had not turned aside from any of his commands all his life—except in the matter of Uriah the Hittite."
    },
    "6": {
      "L": "Now there was war between Rehoboam and Jeroboam all the days of his life.",
      "M": "There was war between Rehoboam and Jeroboam throughout Abijam's life.",
      "T": "War between Rehoboam's line and Jeroboam continued throughout Abijam's reign."
    },
    "7": {
      "L": "The rest of the acts of Abijam and all that he did, are they not written in the Book of the Chronicles of the Kings of Judah? And there was war between Abijam and Jeroboam.",
      "M": "The rest of the acts of Abijam and all that he did are written in the Book of the Chronicles of the Kings of Judah. There was war between Abijam and Jeroboam.",
      "T": "As for the rest of Abijam's acts and all he did, they are recorded in the Book of the Chronicles of the Kings of Judah. There was war between Abijam and Jeroboam."
    },
    "8": {
      "L": "And Abijam slept with his fathers, and they buried him in the city of David. And Asa his son reigned in his place.",
      "M": "Abijam rested with his ancestors and was buried in the city of David. His son Asa reigned in his place.",
      "T": "Abijam rested with his fathers and was buried in the city of David. His son Asa succeeded him."
    },
    "9": {
      "L": "In the twentieth year of Jeroboam king of Israel, Asa began to reign over Judah,",
      "M": "In the twentieth year of Jeroboam king of Israel, Asa became king of Judah.",
      "T": "In the twentieth year of Jeroboam king of Israel, Asa became king of Judah."
    },
    "10": {
      "L": "and he reigned forty-one years in Jerusalem. His mother's name was Maacah the daughter of Abishalom.",
      "M": "He reigned forty-one years in Jerusalem. His grandmother's name was Maacah daughter of Abishalom.",
      "T": "He reigned forty-one years in Jerusalem. His mother's name was Maacah daughter of Abishalom."
    },
    "11": {
      "L": "And Asa did what was right in the eyes of the LORD, as David his father had done.",
      "M": "Asa did what was right in the eyes of the LORD, as his ancestor David had done.",
      "T": "Asa did what was right in the eyes of the LORD, just as his ancestor David had done."
    },
    "12": {
      "L": "He put away the male cult prostitutes out of the land and removed all the idols that his fathers had made.",
      "M": "He expelled the male cult prostitutes from the land and removed all the idols his ancestors had made.",
      "T": "He expelled the male shrine prostitutes from the land and cleared out all the idols his predecessors had made."
    },
    "13": {
      "L": "He also removed Maacah his mother from being queen mother because she had made an abominable image for Asherah. And Asa cut down her image and burned it at the brook Kidron.",
      "M": "He also removed his grandmother Maacah from her position as queen mother because she had made a repulsive Asherah pole. Asa cut down the pole and burned it in the Kidron Valley.",
      "T": "He even removed his mother Maacah from being queen mother because she had made an obscene image for Asherah. Asa cut down the image and burned it in the Kidron Valley."
    },
    "14": {
      "L": "But the high places were not taken away. Nevertheless the heart of Asa was wholly true to the LORD all his days.",
      "M": "The high places, however, were not removed. Still, Asa's heart was fully committed to the LORD throughout his life.",
      "T": "The hilltop shrines were not removed—yet Asa's heart was fully devoted to the LORD all his days."
    },
    "15": {
      "L": "And he brought into the house of the LORD the sacred gifts of his father and his own sacred gifts, silver, and gold, and vessels.",
      "M": "He brought into the house of the LORD the things his father had dedicated and the things he himself had dedicated—silver, gold, and vessels.",
      "T": "He brought into the house of the LORD the sacred gifts his father had dedicated and the gifts he himself had dedicated—silver and gold and vessels."
    },
    "16": {
      "L": "And there was war between Asa and Baasha king of Israel all their days.",
      "M": "There was war between Asa and Baasha king of Israel throughout their reigns.",
      "T": "War between Asa and Baasha king of Israel continued throughout their lifetimes."
    },
    "17": {
      "L": "Baasha king of Israel went up against Judah and built Ramah, that he might permit no one to go out or come in to Asa king of Judah.",
      "M": "Baasha king of Israel marched against Judah and fortified Ramah so that no one could leave or enter the territory of Asa king of Judah.",
      "T": "Baasha king of Israel marched against Judah and fortified Ramah, cutting off all movement in or out of Asa's territory."
    },
    "18": {
      "L": "Then Asa took all the silver and the gold that were left in the treasures of the house of the LORD and the treasures of the king's house and gave them into the hands of his servants. And King Asa sent them to Ben-hadad the son of Tabrimmon, the son of Hezion, king of Syria, who lived in Damascus, saying,",
      "M": "Asa took all the silver and gold that remained in the treasuries of the house of the LORD and the royal palace and gave them to his servants. He sent them to Ben-hadad son of Tabrimmon, the son of Hezion, king of Syria in Damascus, with this message:",
      "T": "Asa took all the silver and gold still in the temple treasury and the palace treasury and handed it to his servants. He sent it to Ben-hadad son of Tabrimmon, son of Hezion, king of Syria in Damascus, with this message:"
    },
    "19": {
      "L": "'There is a treaty between me and you, as there was between my father and your father. Behold, I am sending you a present of silver and gold. Go, break your treaty with Baasha king of Israel, that he may withdraw from me.'",
      "M": "'There is a treaty between me and you, as there was between my father and your father. I am sending you a gift of silver and gold. Go and break your treaty with Baasha king of Israel so he will withdraw from me.'",
      "T": "'There is a treaty between me and you, just as there was between my father and your father. I am sending you a gift of silver and gold. Break your treaty with Baasha king of Israel so he will pull back from me.'"
    },
    "20": {
      "L": "And Ben-hadad listened to King Asa and sent the commanders of his armies against the cities of Israel and struck Ijon, Dan, Abel-beth-maacah, and all Chinneroth, with all the land of Naphtali.",
      "M": "Ben-hadad agreed to King Asa's request and sent his army commanders against the cities of Israel. They struck Ijon, Dan, Abel-beth-maacah, all Chinneroth, and all the land of Naphtali.",
      "T": "Ben-hadad agreed with King Asa and sent his army commanders against the cities of Israel. They struck Ijon, Dan, Abel-beth-maacah, all Chinneroth, and all the territory of Naphtali."
    },
    "21": {
      "L": "And when Baasha heard of it, he stopped building Ramah and lived in Tirzah.",
      "M": "When Baasha heard of it, he stopped building Ramah and went back to Tirzah.",
      "T": "When Baasha heard this, he stopped building Ramah and withdrew to Tirzah."
    },
    "22": {
      "L": "Then King Asa made a proclamation to all Judah—none was exempt—and they carried away the stones of Ramah and its timber with which Baasha had been building. And with them King Asa built Geba of Benjamin and Mizpah.",
      "M": "Then King Asa issued a decree to all Judah—no one was exempt—and they carried away the stones and timber Baasha had used to build Ramah. King Asa used them to build Geba of Benjamin and Mizpah.",
      "T": "Then King Asa issued a levy on all Judah—no exceptions—and they carried away the stones and timber Baasha had been using to build Ramah. With these materials Asa built Geba of Benjamin and Mizpah."
    },
    "23": {
      "L": "Now the rest of all the acts of Asa, all his might, and all that he did, and the cities that he built, are they not written in the Book of the Chronicles of the Kings of Judah? But in his old age he was diseased in his feet.",
      "M": "The rest of all Asa's acts, all his might, and all that he did, and the cities he built, are written in the Book of the Chronicles of the Kings of Judah. But in his old age his feet became diseased.",
      "T": "As for all the rest of Asa's acts—his strength, all he did, the cities he built—they are recorded in the Book of the Chronicles of the Kings of Judah. But in his old age his feet became diseased."
    },
    "24": {
      "L": "And Asa slept with his fathers and was buried with his fathers in the city of David his father. And Jehoshaphat his son reigned in his place.",
      "M": "Asa rested with his ancestors and was buried with them in the city of his ancestor David. His son Jehoshaphat reigned in his place.",
      "T": "Asa rested with his fathers and was buried in the city of his ancestor David. His son Jehoshaphat succeeded him."
    },
    "25": {
      "L": "Nadab the son of Jeroboam began to reign over Israel in the second year of Asa king of Judah, and he reigned over Israel two years.",
      "M": "Nadab son of Jeroboam became king of Israel in the second year of Asa king of Judah, and he reigned over Israel two years.",
      "T": "Nadab son of Jeroboam became king of Israel in the second year of Asa king of Judah. He reigned over Israel two years."
    },
    "26": {
      "L": "He did what was evil in the sight of the LORD and walked in the way of his father, and in his sin which he made Israel to sin.",
      "M": "He did what was evil in the sight of the LORD, walking in the way of his father and in the sin by which his father had led Israel into sin.",
      "T": "He did what was evil in the sight of the LORD. He walked in the footsteps of his father and in the sin by which Jeroboam had led Israel into sin."
    },
    "27": {
      "L": "Baasha the son of Ahijah, of the house of Issachar, conspired against him, and Baasha struck him down at Gibbethon, which belonged to the Philistines, for Nadab and all Israel were laying siege to Gibbethon.",
      "M": "Baasha son of Ahijah, from the tribe of Issachar, conspired against Nadab and struck him down at Gibbethon, which belonged to the Philistines—Nadab and all Israel were besieging Gibbethon at the time.",
      "T": "Baasha son of Ahijah, from the tribe of Issachar, conspired against Nadab and struck him down at Gibbethon, which belonged to the Philistines. Nadab and all Israel had been laying siege to Gibbethon."
    },
    "28": {
      "L": "So Baasha killed him in the third year of Asa king of Judah and reigned in his place.",
      "M": "Baasha killed him in the third year of Asa king of Judah and reigned in his place.",
      "T": "Baasha killed him in the third year of Asa king of Judah and took the throne."
    },
    "29": {
      "L": "And as soon as he was king, he killed all the house of Jeroboam. He left to Jeroboam not one that breathed, until he had destroyed him, according to the word of the LORD that he spoke by his servant Ahijah the Shilonite.",
      "M": "As soon as he became king, he struck down the entire house of Jeroboam, leaving no one alive. He wiped out every last one, in fulfillment of the word the LORD had spoken through his servant Ahijah the Shilonite.",
      "T": "The moment Baasha was king, he struck down the entire house of Jeroboam—he left not a single survivor. He destroyed them all, just as the LORD had spoken through his servant Ahijah the Shilonite."
    },
    "30": {
      "L": "It was for the sins of Jeroboam that he sinned and that he made Israel to sin, and because of the provocation with which he provoked the LORD the God of Israel to anger.",
      "M": "This happened because of the sins Jeroboam had committed and had caused Israel to commit—the provocation by which he had angered the LORD the God of Israel.",
      "T": "This happened because of the sins Jeroboam had committed and led Israel into—the provocation by which he had angered the LORD the God of Israel."
    },
    "31": {
      "L": "Now the rest of the acts of Nadab and all that he did, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of the acts of Nadab and all that he did are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "As for the rest of Nadab's acts and all he did, they are recorded in the Book of the Chronicles of the Kings of Israel."
    },
    "32": {
      "L": "And there was war between Asa and Baasha king of Israel all their days.",
      "M": "There was war between Asa and Baasha king of Israel throughout their reigns.",
      "T": "War between Asa and Baasha king of Israel continued throughout their lifetimes."
    },
    "33": {
      "L": "In the third year of Asa king of Judah, Baasha the son of Ahijah began to reign over all Israel at Tirzah, and he reigned twenty-four years.",
      "M": "In the third year of Asa king of Judah, Baasha son of Ahijah became king of all Israel at Tirzah. He reigned twenty-four years.",
      "T": "In the third year of Asa king of Judah, Baasha son of Ahijah became king of all Israel at Tirzah. He reigned twenty-four years."
    },
    "34": {
      "L": "He did what was evil in the sight of the LORD and walked in the way of Jeroboam and in his sin which he made Israel to sin.",
      "M": "He did what was evil in the sight of the LORD, walking in the way of Jeroboam and in the sin by which Jeroboam had led Israel into sin.",
      "T": "He did what was evil in the sight of the LORD. He walked in the way of Jeroboam and in the sin by which Jeroboam had led Israel into sin."
    }
  },
  "16": {
    "1": {
      "L": "And the word of the LORD came to Jehu the son of Hanani against Baasha, saying,",
      "M": "The word of the LORD came to Jehu son of Hanani against Baasha:",
      "T": "The word of the LORD came to Jehu son of Hanani against Baasha:"
    },
    "2": {
      "L": "'Since I exalted you out of the dust and made you leader over my people Israel, and you have walked in the way of Jeroboam and have made my people Israel to sin, provoking me to anger with their sins,'",
      "M": "'Since I raised you from the dust and made you ruler over my people Israel, and yet you have walked in the way of Jeroboam and have led my people Israel into sin—provoking me to anger with their sins—'",
      "T": "'I lifted you from the dust and made you ruler over my people Israel. Yet you walked in the way of Jeroboam and led my people Israel into sin, provoking me to anger with their sins.'"
    },
    "3": {
      "L": "'behold, I will utterly sweep away Baasha and his house, and I will make your house like the house of Jeroboam the son of Nebat.'",
      "M": "'I am about to sweep away Baasha and his house, and I will make your house like the house of Jeroboam son of Nebat.'",
      "T": "'I am about to sweep away Baasha and his entire house. I will make your dynasty like the house of Jeroboam son of Nebat.'"
    },
    "4": {
      "L": "'Anyone belonging to Baasha who dies in the city the dogs shall eat, and anyone of his who dies in the field the birds of the heavens shall eat.'",
      "M": "'Anyone from Baasha's family who dies in the city the dogs will eat, and anyone who dies in the countryside the birds of the air will eat.'",
      "T": "'Anyone of Baasha's house who dies in the city, the dogs will eat. Anyone who dies in the open field, the birds of the sky will eat.'"
    },
    "5": {
      "L": "Now the rest of the acts of Baasha and what he did, and his might, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of the acts of Baasha, all he did, and his might are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "As for the rest of Baasha's acts and all he did and his military might, they are recorded in the Book of the Chronicles of the Kings of Israel."
    },
    "6": {
      "L": "And Baasha slept with his fathers and was buried at Tirzah, and Elah his son reigned in his place.",
      "M": "Baasha rested with his ancestors and was buried at Tirzah. His son Elah reigned in his place.",
      "T": "Baasha rested with his fathers and was buried at Tirzah. His son Elah succeeded him."
    },
    "7": {
      "L": "Moreover, the word of the LORD came by the hand of Jehu the son of Hanani the prophet against Baasha and against his house, both because of all the evil that he did in the sight of the LORD, provoking him to anger with the work of his hands, in being like the house of Jeroboam, and also because he struck it down.",
      "M": "Moreover, the word of the LORD came through Jehu son of Hanani the prophet against Baasha and his house, because of all the evil he had done in the sight of the LORD, provoking him to anger by his actions—making himself like the house of Jeroboam—and also because he had destroyed it.",
      "T": "The word of the LORD also came through Jehu son of Hanani against Baasha and his house, because of all the evil Baasha had done in the LORD's sight, provoking him to anger with everything he did—making himself like the house of Jeroboam—and also because he had struck down that dynasty."
    },
    "8": {
      "L": "In the twenty-sixth year of Asa king of Judah, Elah the son of Baasha began to reign over Israel at Tirzah, and he reigned two years.",
      "M": "In the twenty-sixth year of Asa king of Judah, Elah son of Baasha became king of Israel at Tirzah. He reigned two years.",
      "T": "In the twenty-sixth year of Asa king of Judah, Elah son of Baasha became king of Israel at Tirzah. He reigned two years."
    },
    "9": {
      "L": "But his servant Zimri, commander of half his chariots, conspired against him. When he was at Tirzah, drinking himself drunk in the house of Arza, who was over the household in Tirzah,",
      "M": "His servant Zimri, commander of half his chariot force, conspired against him while he was at Tirzah, drinking himself drunk in the house of Arza, who was in charge of the palace at Tirzah.",
      "T": "His servant Zimri—commander of half his chariot forces—conspired against him. While Elah was at Tirzah drinking himself drunk in the house of Arza, the palace steward at Tirzah,"
    },
    "10": {
      "L": "Zimri came in and struck him down and killed him, in the twenty-seventh year of Asa king of Judah, and reigned in his place.",
      "M": "Zimri came in and struck him down and killed him, in the twenty-seventh year of Asa king of Judah. Then Zimri reigned in his place.",
      "T": "Zimri came in and struck him down and killed him. It was the twenty-seventh year of Asa king of Judah. Then Zimri took the throne."
    },
    "11": {
      "L": "When he began to reign, as soon as he had seated himself on his throne, he struck down all the house of Baasha. He did not leave him a single male of his relatives or his friends.",
      "M": "As soon as he was seated on the throne, he struck down the whole house of Baasha. He left not one male, whether relative or friend.",
      "T": "The moment he sat on the throne, he struck down the entire house of Baasha—not a single male survived, whether kinsman or friend."
    },
    "12": {
      "L": "Thus Zimri destroyed all the house of Baasha, according to the word of the LORD that he spoke against Baasha through Jehu the prophet,",
      "M": "Zimri destroyed the entire house of Baasha in fulfillment of the word of the LORD that he had spoken against Baasha through Jehu the prophet—",
      "T": "Zimri wiped out the entire house of Baasha, just as the LORD had spoken against Baasha through Jehu the prophet—"
    },
    "13": {
      "L": "for all the sins of Baasha and the sins of Elah his son, which they sinned and which they made Israel to sin, provoking the LORD the God of Israel to anger with their idols.",
      "M": "because of all the sins of Baasha and his son Elah—the sins they committed and caused Israel to commit, by which they provoked the LORD the God of Israel to anger with their worthless idols.",
      "T": "because of all the sins of Baasha and his son Elah—the sins they committed and led Israel into, provoking the LORD the God of Israel to anger with their empty idols."
    },
    "14": {
      "L": "Now the rest of the acts of Elah and all that he did, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of Elah's acts and all he did are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "As for the rest of Elah's acts and all he did, they are recorded in the Book of the Chronicles of the Kings of Israel."
    },
    "15": {
      "L": "In the twenty-seventh year of Asa king of Judah, Zimri reigned seven days at Tirzah. Now the people were encamped against Gibbethon, which belonged to the Philistines,",
      "M": "In the twenty-seventh year of Asa king of Judah, Zimri reigned seven days at Tirzah. The army was encamped against Gibbethon, which belonged to the Philistines,",
      "T": "In the twenty-seventh year of Asa king of Judah, Zimri reigned seven days at Tirzah—the shortest reign in Israel's history. The army was encamped against Gibbethon, a Philistine town,"
    },
    "16": {
      "L": "and the people who were encamped heard it said, 'Zimri has conspired, and he has killed the king.' Therefore all Israel made Omri, the commander of the army, king over Israel that day in the camp.",
      "M": "and when the encamped troops heard that Zimri had conspired and had killed the king, all Israel made Omri the army commander king over Israel right there in the camp.",
      "T": "when word reached the camp that Zimri had conspired and killed the king. Right there in the camp, all Israel made Omri—the army commander—king over Israel."
    },
    "17": {
      "L": "So Omri went up from Gibbethon, and all Israel with him, and they besieged Tirzah.",
      "M": "So Omri marched up from Gibbethon with all Israel and besieged Tirzah.",
      "T": "Omri marched up from Gibbethon with all Israel and laid siege to Tirzah."
    },
    "18": {
      "L": "And when Zimri saw that the city was taken, he went into the citadel of the king's house and burned the king's house over him with fire and died,",
      "M": "When Zimri saw that the city was captured, he went into the inner fortress of the palace and set it on fire over himself. He died,",
      "T": "When Zimri saw that the city was taken, he went into the inner stronghold of the palace and burned it down over himself. He died,"
    },
    "19": {
      "L": "because of his sins that he sinned, doing what was evil in the sight of the LORD, walking in the way of Jeroboam, and for his sin which he had done, making Israel to sin.",
      "M": "because of the sins he committed by doing what was evil in the sight of the LORD and walking in the way of Jeroboam—the sin by which he led Israel into sin.",
      "T": "because of the sins he had committed—doing what was evil in the LORD's sight, walking in the way of Jeroboam and in the sin by which Jeroboam had led Israel into sin."
    },
    "20": {
      "L": "Now the rest of the acts of Zimri and his conspiracy that he made, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of Zimri's acts and the conspiracy he carried out are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "As for the rest of Zimri's acts and the conspiracy he carried out, they are recorded in the Book of the Chronicles of the Kings of Israel."
    },
    "21": {
      "L": "Then the people of Israel were divided into two parts. Half of the people followed Tibni the son of Ginath, to make him king, and half followed Omri.",
      "M": "Then the people of Israel split into two factions. Half supported Tibni son of Ginath and wanted to make him king; the other half supported Omri.",
      "T": "Then the people of Israel split into two camps. Half followed Tibni son of Ginath to make him king; the other half followed Omri."
    },
    "22": {
      "L": "But the people who followed Omri overcame the people who followed Tibni the son of Ginath. So Tibni died, and Omri became king.",
      "M": "The people who supported Omri prevailed over those who supported Tibni son of Ginath. Tibni died, and Omri became king.",
      "T": "The people behind Omri proved stronger than those behind Tibni son of Ginath. Tibni died, and Omri became king."
    },
    "23": {
      "L": "In the thirty-first year of Asa king of Judah, Omri began to reign over Israel, and he reigned for twelve years. Six years he reigned at Tirzah.",
      "M": "In the thirty-first year of Asa king of Judah, Omri became king of Israel. He reigned twelve years, the first six at Tirzah.",
      "T": "In the thirty-first year of Asa king of Judah, Omri became king of Israel and reigned twelve years—the first six at Tirzah."
    },
    "24": {
      "L": "He bought the hill of Samaria from Shemer for two talents of silver, and he built on the hill and called the name of the city that he built Samaria, after the name of Shemer, the owner of the hill.",
      "M": "He bought the hill of Samaria from Shemer for two talents of silver and built a city on the hill, naming it Samaria after Shemer, the previous owner of the hill.",
      "T": "He bought the hill of Samaria from a man named Shemer for two talents of silver and built a city on it. He named it Samaria after Shemer, the former owner."
    },
    "25": {
      "L": "Omri did what was evil in the sight of the LORD, and did more evil than all who were before him.",
      "M": "Omri did what was evil in the sight of the LORD, doing more evil than all who came before him.",
      "T": "Omri did what was evil in the sight of the LORD—worse than all who had come before him."
    },
    "26": {
      "L": "For he walked in all the way of Jeroboam the son of Nebat, and in the sins that he made Israel to sin, provoking the LORD the God of Israel to anger with their idols.",
      "M": "He walked fully in the way of Jeroboam son of Nebat and in the sins by which Jeroboam had led Israel into sin, provoking the LORD the God of Israel to anger with their worthless idols.",
      "T": "He walked completely in the way of Jeroboam son of Nebat, in the sins by which Jeroboam had led Israel into sin—provoking the LORD the God of Israel to anger with their empty idols."
    },
    "27": {
      "L": "Now the rest of the acts of Omri that he did, and the might that he showed, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of Omri's acts and the might he showed are written in the Book of the Chronicles of the Kings of Israel.",
      "T": "As for the rest of Omri's acts and the power he displayed, they are recorded in the Book of the Chronicles of the Kings of Israel."
    },
    "28": {
      "L": "And Omri slept with his fathers and was buried in Samaria, and Ahab his son reigned in his place.",
      "M": "Omri rested with his ancestors and was buried in Samaria. His son Ahab reigned in his place.",
      "T": "Omri rested with his fathers and was buried in Samaria. His son Ahab succeeded him."
    },
    "29": {
      "L": "And Ahab the son of Omri began to reign over Israel in the thirty-eighth year of Asa king of Judah, and Ahab the son of Omri reigned over Israel twenty-two years.",
      "M": "Ahab son of Omri became king of Israel in the thirty-eighth year of Asa king of Judah. Ahab son of Omri reigned over Israel twenty-two years.",
      "T": "Ahab son of Omri became king of Israel in the thirty-eighth year of Asa king of Judah. He reigned twenty-two years."
    },
    "30": {
      "L": "And Ahab the son of Omri did evil in the sight of the LORD, more than all who were before him.",
      "M": "Ahab son of Omri did what was evil in the sight of the LORD, more than all who were before him.",
      "T": "Ahab son of Omri did what was evil in the sight of the LORD—more than all who had come before him."
    },
    "31": {
      "L": "And as if it had been a light thing for him to walk in the sins of Jeroboam the son of Nebat, he took for his wife Jezebel the daughter of Ethbaal king of the Sidonians, and went and served Baal and worshiped him.",
      "M": "As if it were not enough to walk in the sins of Jeroboam son of Nebat, he married Jezebel daughter of Ethbaal king of the Sidonians, and he went to serve and worship Baal.",
      "T": "As if walking in the sins of Jeroboam son of Nebat were a small thing, he married Jezebel daughter of Ethbaal king of the Sidonians—and went to serve Baal and bow down to him."
    },
    "32": {
      "L": "He erected an altar for Baal in the house of Baal that he built in Samaria.",
      "M": "He set up an altar for Baal in the temple of Baal that he built in Samaria.",
      "T": "He set up an altar for Baal in the temple of Baal that he built in Samaria."
    },
    "33": {
      "L": "And Ahab made an Asherah pole. Ahab did more to provoke the LORD the God of Israel to anger than all the kings of Israel who were before him.",
      "M": "Ahab also made an Asherah pole. Ahab did more to provoke the LORD the God of Israel to anger than all the kings of Israel before him.",
      "T": "Ahab also made an Asherah pole. Ahab did more to provoke the LORD the God of Israel to anger than any king of Israel before him."
    },
    "34": {
      "L": "In his days Hiel the Bethelite built Jericho. He laid its foundation at the cost of Abiram his firstborn, and set up its gates at the cost of his youngest son Segub, according to the word of the LORD which he spoke by Joshua the son of Nun.",
      "M": "During his reign Hiel the Bethelite rebuilt Jericho. He laid its foundations at the cost of his firstborn son Abiram, and set up its gates at the cost of his youngest son Segub, in accordance with the word of the LORD that he had spoken through Joshua son of Nun.",
      "T": "During Ahab's reign, Hiel the Bethelite rebuilt Jericho. He laid its foundations at the cost of his firstborn son Abiram, and he set up its gates at the cost of his youngest son Segub—fulfilling to the letter the word the LORD had spoken through Joshua son of Nun centuries before."
    }
  },
  "17": {
    "1": {
      "L": "Now Elijah the Tishbite, of the inhabitants of Gilead, said to Ahab, 'As the LORD the God of Israel lives, before whom I stand, there shall be neither dew nor rain these years, except by my word.'",
      "M": "Now Elijah the Tishbite, from the settlers of Gilead, said to Ahab, 'As the LORD the God of Israel lives—before whom I stand—there will be neither dew nor rain in these years except by my word.'",
      "T": "Then Elijah the Tishbite, from the settlers of Gilead—whose very name means 'My God is Yahweh'—declared to Ahab: 'As the LORD the God of Israel lives—the one before whom I stand—there will be no dew or rain in the coming years except at my word.'"
    },
    "2": {
      "L": "And the word of the LORD came to him, saying,",
      "M": "Then the word of the LORD came to him:",
      "T": "The word of the LORD came to Elijah:"
    },
    "3": {
      "L": "'Depart from here and turn eastward and hide yourself by the brook Cherith, which is east of the Jordan.'",
      "M": "'Leave here, turn eastward, and hide yourself by the brook Cherith east of the Jordan.'",
      "T": "'Leave here. Turn east and hide yourself by the brook Cherith, east of the Jordan.'"
    },
    "4": {
      "L": "'It shall be that you shall drink from the brook, and I have commanded the ravens to feed you there.'",
      "M": "'You will drink from the brook, and I have commanded the ravens to feed you there.'",
      "T": "'You will drink from the brook. I have commanded the ravens to feed you there.'"
    },
    "5": {
      "L": "So he went and did according to the word of the LORD. He went and lived by the brook Cherith that is east of the Jordan.",
      "M": "So he went and did as the LORD commanded. He went and lived by the brook Cherith east of the Jordan.",
      "T": "He went and did exactly as the LORD commanded—he went and settled by the brook Cherith east of the Jordan."
    },
    "6": {
      "L": "And the ravens brought him bread and meat in the morning, and bread and meat in the evening, and he drank from the brook.",
      "M": "The ravens brought him bread and meat in the morning, and bread and meat in the evening, and he drank from the brook.",
      "T": "The ravens brought him bread and meat in the morning, and bread and meat in the evening, and he drank from the brook."
    },
    "7": {
      "L": "And after a while the brook dried up, because there was no rain in the land.",
      "M": "After some time the brook dried up, because there had been no rain in the land.",
      "T": "After a while the brook dried up—there had been no rain in the land."
    },
    "8": {
      "L": "Then the word of the LORD came to him, saying,",
      "M": "Then the word of the LORD came to him again:",
      "T": "The word of the LORD came to him again:"
    },
    "9": {
      "L": "'Arise, go to Zarephath, which belongs to Sidon, and dwell there. Behold, I have commanded a widow woman there to sustain you.'",
      "M": "'Go at once to Zarephath, which belongs to Sidon, and live there. I have commanded a widow there to provide for you.'",
      "T": "'Go now to Zarephath, which belongs to Sidon, and stay there. I have commanded a widow there to provide for you.'"
    },
    "10": {
      "L": "So he arose and went to Zarephath. And when he came to the gate of the city, behold, a widow was there gathering sticks. And he called to her and said, 'Bring me a little water in a vessel, that I may drink.'",
      "M": "So he got up and went to Zarephath. When he arrived at the city gate, a widow was there gathering sticks. He called to her and said, 'Please bring me a little water in a vessel, so I may drink.'",
      "T": "He got up and went to Zarephath. When he arrived at the city gate, a widow was there gathering sticks. He called to her: 'Please bring me a little water in a vessel so I can drink.'"
    },
    "11": {
      "L": "And as she was going to get it, he called to her and said, 'Bring me a morsel of bread in your hand.'",
      "M": "As she was going to get it, he called again and said, 'Please bring me a piece of bread as well.'",
      "T": "As she was going to get it, he called after her: 'Please bring me a piece of bread too.'"
    },
    "12": {
      "L": "And she said, 'As the LORD your God lives, I have nothing baked, only a handful of flour in a jar and a little oil in a jug. And now I am gathering a couple of sticks that I may go in and prepare it for myself and my son, that we may eat it and die.'",
      "M": "She said, 'As the LORD your God lives, I have nothing baked. I have only a handful of flour in a jar and a little oil in a jug. I am gathering a few sticks so I can go home and make a last meal for my son and me—and then we will die.'",
      "T": "She said: 'As the LORD your God lives, I have nothing baked. I have only a handful of flour in a jar and a little oil in a jug. I am gathering a few sticks to go home and cook one last meal for my son and me—and then we will die.'"
    },
    "13": {
      "L": "And Elijah said to her, 'Do not fear. Go and do as you have said. But first make me a little cake of it and bring it out to me, and afterward make something for yourself and your son.'",
      "M": "Elijah said to her, 'Do not be afraid. Go and do as you planned. But first make me a small cake from what you have and bring it to me. After that, make something for yourself and your son.'",
      "T": "Elijah said: 'Do not be afraid. Go and do as you said—but first make a small cake for me and bring it out. Then make something for yourself and your son.'"
    },
    "14": {
      "L": "'For thus says the LORD the God of Israel: The jar of flour shall not be spent, and the jug of oil shall not be empty, until the day that the LORD sends rain upon the earth.'",
      "M": "'For this is what the LORD the God of Israel says: The jar of flour will not be used up, and the jug of oil will not run dry, until the day the LORD sends rain on the earth.'",
      "T": "'For this is what the LORD the God of Israel says: The jar of flour will not be exhausted and the jug of oil will not run dry until the day the LORD sends rain on the land.'"
    },
    "15": {
      "L": "And she went and did as Elijah said. And she and he and her household ate for many days.",
      "M": "She went and did as Elijah said, and she and Elijah and her household ate for many days.",
      "T": "She went and did exactly as Elijah said—and she and Elijah and her household ate for many days."
    },
    "16": {
      "L": "The jar of flour was not spent, neither did the jug of oil become empty, according to the word of the LORD that he spoke by Elijah.",
      "M": "The jar of flour was not used up, and the jug of oil did not run dry, in accordance with the word the LORD had spoken through Elijah.",
      "T": "The jar of flour was never exhausted and the jug of oil never ran dry—just as the LORD had spoken through Elijah."
    },
    "17": {
      "L": "After this the son of the woman, the mistress of the house, became ill. And his illness was so severe that there was no breath left in him.",
      "M": "After this the son of the woman who owned the house became ill. His illness was so severe that there was no breath left in him.",
      "T": "After these things, the son of the woman—the mistress of the house—became ill. His illness grew so severe that he stopped breathing."
    },
    "18": {
      "L": "And she said to Elijah, 'What have you against me, O man of God? You have come to me to bring my sin to remembrance and to cause the death of my son!'",
      "M": "She said to Elijah, 'What do you have against me, man of God? Did you come here to remind God of my sin and cause the death of my son?'",
      "T": "She said to Elijah: 'What do you have against me, man of God? Did you come here to bring my sin to remembrance and kill my son?'"
    },
    "19": {
      "L": "And he said to her, 'Give me your son.' And he took him from her arms and carried him up into the upper chamber where he stayed, and laid him on his own bed.",
      "M": "He said to her, 'Give me your son.' He took the boy from her arms, carried him up to the upper room where he was staying, and laid him on his own bed.",
      "T": "He said: 'Give me your son.' He took the boy from her arms, carried him up to the room where he was staying, and laid him on his own bed."
    },
    "20": {
      "L": "And he cried to the LORD, 'O LORD my God, have you brought calamity even upon the widow with whom I sojourn, by killing her son?'",
      "M": "Then he cried to the LORD: 'O LORD my God, have you brought tragedy on this widow I am staying with by killing her son?'",
      "T": "He cried out to the LORD: 'O LORD my God, have you brought disaster even upon this widow I am staying with, by killing her son?'"
    },
    "21": {
      "L": "Then he stretched himself upon the child three times and cried to the LORD, 'O LORD my God, let this child's life come into him again.'",
      "M": "Then he stretched himself over the boy three times and cried to the LORD: 'O LORD my God, let this child's life return to him!'",
      "T": "He stretched himself over the boy three times and cried out to the LORD: 'O LORD my God, let this child's breath of life come into him again!'"
    },
    "22": {
      "L": "And the LORD listened to the voice of Elijah. And the life of the child came into him again, and he revived.",
      "M": "The LORD heard Elijah's prayer. The child's life returned to him, and he revived.",
      "T": "The LORD heard Elijah's voice. The breath of life returned to the boy, and he came back to life."
    },
    "23": {
      "L": "And Elijah took the child and brought him down from the upper chamber into the house and delivered him to his mother. And Elijah said, 'See, your son lives.'",
      "M": "Elijah took the child and brought him down from the upper room into the house and gave him to his mother. 'See, your son is alive,' said Elijah.",
      "T": "Elijah took the child and brought him down from the upper room and handed him to his mother. 'Look,' said Elijah, 'your son is alive.'"
    },
    "24": {
      "L": "And the woman said to Elijah, 'Now I know that you are a man of God, and that the word of the LORD in your mouth is truth.'",
      "M": "The woman said to Elijah, 'Now I know that you are a man of God, and that the word of the LORD in your mouth is truth.'",
      "T": "The woman said to Elijah: 'Now I know for certain that you are a man of God—and that the word of the LORD on your lips is truth.'"
    }
  },
  "18": {
    "1": {
      "L": "After many days the word of the LORD came to Elijah, in the third year, saying, 'Go, show yourself to Ahab, and I will send rain upon the earth.'",
      "M": "After a long time, in the third year, the word of the LORD came to Elijah: 'Go and present yourself to Ahab, and I will send rain on the land.'",
      "T": "After a long time—in the third year—the word of the LORD came to Elijah: 'Go and present yourself to Ahab. I will send rain on the land.'"
    },
    "2": {
      "L": "So Elijah went to show himself to Ahab. Now the famine was severe in Samaria.",
      "M": "So Elijah went to present himself to Ahab. The famine was severe in Samaria.",
      "T": "Elijah went to meet Ahab. The famine was severe in Samaria."
    },
    "3": {
      "L": "And Ahab called Obadiah, who was over the household. Now Obadiah feared the LORD greatly.",
      "M": "Ahab summoned Obadiah, who was in charge of the palace. Now Obadiah greatly feared the LORD.",
      "T": "Ahab summoned Obadiah—whose name means 'servant of Yahweh'—who was in charge of the palace. Obadiah was a man who deeply feared the LORD."
    },
    "4": {
      "L": "And it was so, when Jezebel cut off the prophets of the LORD, that Obadiah took a hundred prophets and hid them by fifties in a cave and fed them with bread and water.",
      "M": "When Jezebel had been killing the LORD's prophets, Obadiah took a hundred prophets and hid them fifty to a cave, and supplied them with bread and water.",
      "T": "When Jezebel was killing the LORD's prophets, Obadiah had taken a hundred of them and hidden them in two caves—fifty to a cave—and kept them alive with bread and water."
    },
    "5": {
      "L": "And Ahab said to Obadiah, 'Go through the land to all the springs of water and to all the valleys. Perhaps we may find grass and save the horses and mules alive, and not lose some of the animals.'",
      "M": "Ahab said to Obadiah, 'Go through the land to every spring and every valley. Maybe we can find enough grass to keep the horses and mules alive and not lose all our animals.'",
      "T": "Ahab said to Obadiah: 'Let us go through the land to every spring and every valley. Perhaps we can find enough grass to keep the horses and mules alive and spare our animals.'"
    },
    "6": {
      "L": "So they divided the land between them to pass through it. Ahab went in one direction by himself, and Obadiah went in another direction by himself.",
      "M": "They divided the land between them: Ahab went one way by himself, and Obadiah went another way by himself.",
      "T": "They divided the land between them. Ahab went one way, and Obadiah went another."
    },
    "7": {
      "L": "And as Obadiah was on the way, behold, Elijah met him. And Obadiah recognized him and fell on his face and said, 'Is it you, my lord Elijah?'",
      "M": "As Obadiah was on the road, Elijah met him. When Obadiah recognized him, he fell on his face and said, 'Is it really you, my lord Elijah?'",
      "T": "As Obadiah was on the road, Elijah met him. Obadiah recognized him and fell face-down before him. 'Is it really you, my lord Elijah?' he asked."
    },
    "8": {
      "L": "And he answered him, 'It is I. Go, tell your lord, Behold, Elijah is here.'",
      "M": "Elijah answered, 'Yes, it is. Go tell your master: Elijah is here.'",
      "T": "'It is I,' Elijah said. 'Go tell your master: Elijah is here.'"
    },
    "9": {
      "L": "And he said, 'How have I sinned, that you would give your servant into the hand of Ahab to kill me?'",
      "M": "Obadiah said, 'What wrong have I done that you would hand your servant over to Ahab to be killed?'",
      "T": "Obadiah said: 'What have I done to deserve this? Why would you hand your servant over to Ahab to be killed?'"
    },
    "10": {
      "L": "'As the LORD your God lives, there is no nation or kingdom where my lord has not sent to seek you. And when they would say, He is not here, he would take an oath of the kingdom or nation, that they had not found you.'",
      "M": "'As the LORD your God lives, there is no nation or kingdom where my master has not sent searching for you. And when they said, He is not here, he made the kingdom or nation swear an oath that they had not found you.'",
      "T": "'As the LORD your God lives, Ahab has sent to every nation and kingdom looking for you. And when they said, He is not here—he made each kingdom and nation swear an oath that they could not find you.'"
    },
    "11": {
      "L": "'And now you say, Go tell your lord, Elijah is here.'",
      "M": "'And now you say, Go tell your master: Elijah is here.'",
      "T": "'And now you tell me to go say to my master: Elijah is here.'"
    },
    "12": {
      "L": "'And as soon as I have gone from you, the Spirit of the LORD will carry you I know not where. And so when I come and tell Ahab and he cannot find you, he will kill me, though I your servant have feared the LORD from my youth.'",
      "M": "'As soon as I leave you, the Spirit of the LORD will carry you off to who knows where. When I go and tell Ahab and he cannot find you, he will kill me—though I your servant have feared the LORD from my youth.'",
      "T": "'The moment I leave you, the Spirit of the LORD will carry you away to who knows where. I will go tell Ahab, he will not find you, and he will kill me—though I have feared the LORD from my youth.'"
    },
    "13": {
      "L": "'Has it not been told my lord what I did when Jezebel killed the prophets of the LORD, how I hid a hundred men of the LORD's prophets by fifties in a cave and fed them with bread and water?'",
      "M": "'Has my lord not been told what I did when Jezebel was killing the LORD's prophets—how I hid a hundred of them by fifties in a cave and fed them with bread and water?'",
      "T": "'Has no one told my lord what I did when Jezebel was killing the LORD's prophets? I hid a hundred of them in two caves, fifty to a cave, and kept them alive with bread and water.'"
    },
    "14": {
      "L": "'And now you say, Go tell your lord, Elijah is here. He will kill me.'",
      "M": "'And now you say, Go tell your master: Elijah is here. He will kill me.'",
      "T": "'And now you tell me to go say: Elijah is here. He will kill me.'"
    },
    "15": {
      "L": "And Elijah said, 'As the LORD of hosts lives, before whom I stand, I will surely show myself to him today.'",
      "M": "Elijah replied, 'As the LORD of hosts lives—before whom I stand—I will certainly present myself to Ahab today.'",
      "T": "Elijah answered: 'As the LORD of hosts lives—before whom I stand—I will surely present myself to Ahab today.'"
    },
    "16": {
      "L": "So Obadiah went to meet Ahab and told him. And Ahab went to meet Elijah.",
      "M": "So Obadiah went and told Ahab, and Ahab went to meet Elijah.",
      "T": "So Obadiah went and told Ahab, and Ahab went to meet Elijah."
    },
    "17": {
      "L": "And when Ahab saw Elijah, Ahab said to him, 'Is it you, you troubler of Israel?'",
      "M": "When Ahab saw Elijah, Ahab said to him, 'Is that you, you troubler of Israel?'",
      "T": "When Ahab saw Elijah, he said: 'Is that you—you troubler of Israel?'"
    },
    "18": {
      "L": "And he answered, 'I have not troubled Israel, but you have, and your father's house, because you have abandoned the commandments of the LORD and followed the Baals.'",
      "M": "He answered, 'I have not troubled Israel—you and your father's house have, because you abandoned the commandments of the LORD and followed the Baals.'",
      "T": "He answered: 'I have not troubled Israel—you have. You and your father's house, because you abandoned the commandments of the LORD and went after the Baals.'"
    },
    "19": {
      "L": "'Now therefore send and gather all Israel to me at Mount Carmel, and the four hundred and fifty prophets of Baal and the four hundred prophets of Asherah, who eat at Jezebel's table.'",
      "M": "'Now send and assemble all Israel to meet me at Mount Carmel, along with the four hundred and fifty prophets of Baal and the four hundred prophets of Asherah who eat at Jezebel's table.'",
      "T": "'Now send word and assemble all Israel before me at Mount Carmel—and bring the four hundred and fifty prophets of Baal and the four hundred prophets of Asherah who eat at Jezebel's table.'"
    },
    "20": {
      "L": "So Ahab sent to all the people of Israel and gathered the prophets together at Mount Carmel.",
      "M": "So Ahab sent word throughout all Israel and assembled the prophets at Mount Carmel.",
      "T": "Ahab sent word throughout all Israel and gathered the prophets at Mount Carmel."
    },
    "21": {
      "L": "And Elijah came near to all the people and said, 'How long will you go limping between two different opinions? If the LORD is God, follow him; but if Baal, then follow him.' And the people did not answer him a word.",
      "M": "Elijah came before all the people and said, 'How long will you waver between two opinions? If the LORD is God, follow him; but if Baal, then follow him.' The people said nothing.",
      "T": "Elijah stepped before all the people and said: 'How long will you limp between two positions? If the LORD is God, follow him. If Baal, then follow him.' The people said nothing."
    },
    "22": {
      "L": "Then Elijah said to the people, 'I, even I only, am left as a prophet of the LORD, but Baal's prophets are four hundred and fifty men.'",
      "M": "Elijah said to the people, 'I am the only prophet of the LORD left, but Baal's prophets number four hundred and fifty.'",
      "T": "Elijah said to the people: 'I am the only prophet of the LORD remaining. Baal's prophets number four hundred and fifty.'"
    },
    "23": {
      "L": "'Let two bulls be given to us, and let them choose one bull for themselves and cut it in pieces and lay it on the wood, but put no fire to it. And I will prepare the other bull and lay it on the wood and put no fire to it.'",
      "M": "'Bring us two bulls. Let them choose one for themselves, cut it up, and lay it on the wood—without setting fire to it. I will prepare the other bull, lay it on the wood, and put no fire under it either.'",
      "T": "'Bring two bulls. Let them choose one, cut it in pieces, and lay it on the wood—but put no fire to it. I will prepare the other bull, lay it on the wood, and put no fire to it either.'"
    },
    "24": {
      "L": "'And you call upon the name of your god, and I will call upon the name of the LORD, and the God who answers by fire, he is God.' And all the people answered, 'It is well spoken.'",
      "M": "'Then you call on the name of your god, and I will call on the name of the LORD. The God who answers by fire—he is God.' All the people answered, 'What you say is good.'",
      "T": "'You call on the name of your god, and I will call on the name of the LORD. The God who answers by fire—he is God.' All the people said: 'It is well spoken.'"
    },
    "25": {
      "L": "Then Elijah said to the prophets of Baal, 'Choose for yourselves one bull and prepare it first, for you are many, and call upon the name of your god, but put no fire to it.'",
      "M": "Then Elijah said to the prophets of Baal, 'Choose your bull and prepare it first—you are the larger group. Call on the name of your god, but put no fire under it.'",
      "T": "Elijah said to the prophets of Baal: 'Choose your bull and prepare it first—you have the numbers. Call on the name of your god. But put no fire under it.'"
    },
    "26": {
      "L": "And they took the bull that was given them, and they prepared it and called upon the name of Baal from morning until noon, saying, 'O Baal, answer us!' But there was no voice, and no one answered. And they limped around the altar that they had made.",
      "M": "They took the bull that was given to them, prepared it, and called on the name of Baal from morning until noon. 'O Baal, answer us!' they cried. But there was no voice, no answer—and they leaped and danced around the altar they had made.",
      "T": "They took the bull, prepared it, and called on the name of Baal from morning until noon. 'O Baal, answer us!' they cried. But there was no voice—no answer. They leaped around the altar they had made."
    },
    "27": {
      "L": "And at noon Elijah mocked them, saying, 'Cry aloud, for he is a god. Either he is musing, or he is relieving himself, or he is on a journey, or perhaps he is asleep and must be awakened.'",
      "M": "At noon Elijah mocked them: 'Call louder—he is a god! Maybe he is deep in thought, or busy, or traveling. Perhaps he is asleep and must be woken up!'",
      "T": "At noon Elijah mocked them: 'Shout louder! Surely he is a god! Maybe he is thinking, or busy with something, or off on a journey. Maybe he is asleep and needs to be woken up!'"
    },
    "28": {
      "L": "And they cried aloud and cut themselves after their custom with swords and lances, until the blood gushed out upon them.",
      "M": "So they shouted louder and slashed themselves with swords and spears as was their custom, until the blood poured down on them.",
      "T": "They shouted louder and slashed themselves with swords and spears as was their practice, until the blood streamed down over them."
    },
    "29": {
      "L": "And as midday passed they raved on until the time of the offering of the oblation, but there was no voice, and no one answered, and no one paid attention.",
      "M": "Midday passed, and they raved on until the time of the evening offering. But there was no voice, no answer, and no one paid attention.",
      "T": "Midday passed, and they kept raving until the time of the evening sacrifice. But there was no voice, no answer, no one who took notice."
    },
    "30": {
      "L": "Then Elijah said to all the people, 'Come near to me.' And all the people came near to him. And he repaired the altar of the LORD that had been thrown down.",
      "M": "Then Elijah said to all the people, 'Come close to me.' They all came near to him. He repaired the altar of the LORD that had been torn down.",
      "T": "Then Elijah said to all the people: 'Come near to me.' They all came. He repaired the altar of the LORD that had been broken down."
    },
    "31": {
      "L": "Elijah took twelve stones, according to the number of the tribes of the sons of Jacob, to whom the word of the LORD came, saying, 'Israel shall be your name,'",
      "M": "Elijah took twelve stones, one for each tribe of Jacob's sons, to whom the word of the LORD had come saying, 'Your name shall be Israel.'",
      "T": "Elijah took twelve stones—one for each tribe of the sons of Jacob, to whom the word of the LORD had come saying, 'Israel shall be your name.'"
    },
    "32": {
      "L": "and with the stones he built an altar in the name of the LORD. And he made a trench around the altar, as great as would contain two measures of seed.",
      "M": "With these stones he built an altar in the name of the LORD. He dug a trench around the altar large enough to hold about two seahs of seed.",
      "T": "With these stones he built an altar in the name of the LORD and dug a trench around it large enough to hold about two seahs of seed."
    },
    "33": {
      "L": "And he put the wood in order and cut the bull in pieces and laid it on the wood. And he said, 'Fill four jars with water and pour it on the burnt offering and on the wood.'",
      "M": "He arranged the wood, cut the bull in pieces, and laid it on the wood. Then he said, 'Fill four jars with water and pour it on the burnt offering and the wood.'",
      "T": "He arranged the wood, cut the bull in pieces, and laid it on the wood. Then he said: 'Fill four large jars with water and pour them on the offering and the wood.'"
    },
    "34": {
      "L": "And he said, 'Do it a second time.' And they did it a second time. And he said, 'Do it a third time.' And they did it a third time.",
      "M": "'Do it again,' he said. They did it a second time. 'Do it a third time,' he said. And they did it a third time.",
      "T": "'Do it again,' he said. They did. 'Do it a third time,' he said. And they did."
    },
    "35": {
      "L": "And the water ran around the altar and filled the trench also with water.",
      "M": "The water ran down around the altar and filled the trench.",
      "T": "Water ran down all around the altar and filled the trench."
    },
    "36": {
      "L": "And at the time of the offering of the oblation, Elijah the prophet came near and said, 'O LORD, God of Abraham, Isaac, and Israel, let it be known this day that you are God in Israel, and that I am your servant, and that I have done all these things at your word.'",
      "M": "At the time of the evening offering, Elijah the prophet came near and said, 'O LORD, God of Abraham, Isaac, and Israel, let it be known this day that you are God in Israel and that I am your servant and have done all these things at your command.'",
      "T": "At the time of the evening offering, Elijah came near and prayed: 'O LORD, God of Abraham, Isaac, and Israel—let it be known today that you are God in Israel, and that I am your servant, and that I have done all this at your word.'"
    },
    "37": {
      "L": "'Answer me, O LORD, answer me, that this people may know that you, LORD, are God, and that you have turned their hearts back.'",
      "M": "'Answer me, O LORD, answer me, so that this people will know that you, LORD, are God, and that you are turning their hearts back.'",
      "T": "'Answer me, LORD! Answer me! Let this people know that you, the LORD, are God—and that you are the one turning their hearts back to you.'"
    },
    "38": {
      "L": "Then the fire of the LORD fell and consumed the burnt offering and the wood and the stones and the dust, and licked up the water that was in the trench.",
      "M": "Then the fire of the LORD fell and consumed the burnt offering, the wood, the stones, and the dust, and licked up the water that was in the trench.",
      "T": "The fire of the LORD fell and consumed the burnt offering, the wood, the stones, and the dust—and it licked up every drop of water in the trench."
    },
    "39": {
      "L": "And when all the people saw it, they fell on their faces and said, 'The LORD, he is God! The LORD, he is God!'",
      "M": "When all the people saw it, they fell facedown and cried, 'The LORD, he is God! The LORD, he is God!'",
      "T": "When all the people saw it, they fell on their faces and cried: 'The LORD—he is God! The LORD—he is God!' (The very cry that echoes the meaning of Elijah's own name: My God is Yahweh.)"
    },
    "40": {
      "L": "And Elijah said to them, 'Seize the prophets of Baal. Let not one of them escape.' And they seized them. And Elijah brought them down to the brook Kishon and slaughtered them there.",
      "M": "Then Elijah said to them, 'Seize the prophets of Baal—do not let one of them escape.' They seized them, and Elijah brought them down to the brook Kishon and slaughtered them there.",
      "T": "Elijah said to the people: 'Seize the prophets of Baal—do not let one escape.' They seized them, and Elijah brought them down to the brook Kishon and slaughtered them there."
    },
    "41": {
      "L": "And Elijah said to Ahab, 'Go up, eat and drink, for there is a sound of the rushing of rain.'",
      "M": "Then Elijah said to Ahab, 'Go up, eat and drink, for there is the sound of heavy rain.'",
      "T": "Elijah said to Ahab: 'Go up, eat and drink—I can hear the sound of heavy rain coming.'"
    },
    "42": {
      "L": "So Ahab went up to eat and to drink. And Elijah went up to the top of Mount Carmel. And he bowed himself down on the earth and put his face between his knees.",
      "M": "So Ahab went up to eat and drink, while Elijah climbed to the top of Mount Carmel. He crouched down on the ground and put his face between his knees.",
      "T": "Ahab went up to eat and drink. Elijah climbed to the top of Carmel and crouched down on the ground, his face between his knees."
    },
    "43": {
      "L": "And he said to his servant, 'Go up now, look toward the sea.' And he went up and looked and said, 'There is nothing.' And he said, 'Go again,' seven times.",
      "M": "He said to his servant, 'Go and look toward the sea.' The servant went and looked and said, 'There is nothing.' He said, 'Go back again.' This happened seven times.",
      "T": "He said to his servant: 'Go up and look toward the sea.' The servant went and looked. 'There is nothing,' he said. 'Go again,' said Elijah. This happened seven times."
    },
    "44": {
      "L": "At the seventh time he said, 'Behold, a little cloud like a man's hand is rising from the sea.' And he said, 'Go up, say to Ahab, Prepare your chariot and go down, lest the rain stop you.'",
      "M": "At the seventh time the servant said, 'A small cloud, about the size of a man's hand, is rising from the sea.' Elijah said, 'Go and tell Ahab, Harness your chariot and go down now before the rain stops you.'",
      "T": "At the seventh time the servant said: 'A small cloud is rising from the sea—no bigger than a man's hand.' Elijah said: 'Go tell Ahab: Hitch your chariot and go down before the rain traps you.'"
    },
    "45": {
      "L": "And in a little while the heavens grew black with clouds and wind, and there was a great rain. And Ahab rode and went to Jezreel.",
      "M": "In a short time the sky grew dark with clouds and wind, and a great rain fell. Ahab rode and headed for Jezreel.",
      "T": "Within a short while the sky turned black with clouds and wind, and a heavy rain began to fall. Ahab mounted his chariot and rode for Jezreel."
    },
    "46": {
      "L": "And the hand of the LORD was on Elijah, and he gathered up his garment and ran before Ahab to the entrance of Jezreel.",
      "M": "The power of the LORD came on Elijah, and he tucked his cloak into his belt and ran ahead of Ahab all the way to Jezreel.",
      "T": "The LORD's power came upon Elijah. He girded up his robe and ran ahead of Ahab's chariot all the way to the entrance of Jezreel."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1kings')
        merge_tier(existing, KINGS, tier_key)
        save(tier_dir, '1kings', existing)
    print('1 Kings 13–18 written.')

if __name__ == '__main__':
    main()
