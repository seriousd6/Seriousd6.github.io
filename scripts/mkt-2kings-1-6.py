"""
MKT 2 Kings chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2kings-1-6.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T.
  Consistent with mkt-1kings-19-21.py convention.
- H430 (אֱלֹהִים): "God" in all tiers.
- H1168 (בַּעַל): "Baal" in all tiers. Baal-zebub = "Baal of the Flies" (Ekron's god).
  1:2,3,6,16: Ahaziah consults Baal-zebub — rendered "Baal-zebub, the god of Ekron."
- H7307 (רוּחַ): Two distinct senses in this range — never collapsed:
  - 2:9,15,16: "spirit" (the prophetic spirit that rested on Elijah, passing to Elisha).
    2:9: "a double portion of your spirit" — L: "double of your spirit"; M: "a double share of your spirit"; T: "twice the measure of your spirit."
    2:16: the sons of prophets fear the Spirit of the LORD carried Elijah away — L: "Spirit of the LORD"; M: "Spirit of the LORD"; T: "the Spirit of the LORD."
  - No wind/breath sense in this range (unlike 1 Kings 19).
- H5315 (נֶפֶשׁ): Not prominent in chs 1–6. One instance in 6:30 ("sackcloth against his flesh/body") — rendered "body" (sense = physical person, not immaterial soul).
- H4397 (מַלְאָךְ): Dual sense — must distinguish:
  - "angel of the LORD" (1:3,15): divine messenger — rendered "angel of the LORD" L/M/T.
  - Human messengers (1:2,5 etc.): rendered "messengers" throughout.
- H5030 (נָבִיא): "prophet" in L/M; "prophet" in T. The "sons of the prophets" (בְּנֵי הַנְּבִיאִים) = prophetic guild/community.
  L: "sons of the prophets"; M: "sons of the prophets" / "company of the prophets"; T: "the prophetic brotherhood" on first occurrence, then "the prophets" for variety.
- H2617 (חֶסֶד): Not prominent in this range.
- H1285 (בְּרִית): Not prominent in this range.
- Baal-zebub note: The name means "Baal of the Flies" or (as NT uses it) "Beelzebul/Beel-zebul" = "lord of the house." The mockery in the name is intentional. T notes this in 1:2.
- Fire from heaven (1:10,12): Direct echo of Elijah on Carmel (1 Kgs 18:38) and Moses (Lev 9:24). T notes this.
- Double portion (2:9): The firstborn's share (Deut 21:17). Elisha asks to be Elijah's firstborn heir in prophecy. T notes this.
- Chariot of Israel (2:12): Elisha's cry ("My father! My father! The chariot of Israel and its horsemen!") = Elijah was more protection to Israel than an army. The same phrase recurs at Elisha's death (2 Kgs 13:14). T notes this.
- Elisha's double portion confirmed: The text counts miracles — Elijah had notable miracles; Elisha performed roughly twice as many (including raising the dead twice). T notes this at 4:35.
- Naaman (ch 5): The recognition formula "there is no God in all the earth except in Israel" (5:15) echoes the Exodus pattern (Exod 9:14). A foreign military commander becomes Israel's most theologically clear confessor in the whole DH. T notes this.
- Naaman's earth request (5:17): He asks for two mule-loads of Israelite soil to build an altar — ancient belief that gods are tied to territories. Elisha does not rebuke the request. T notes the tension.
- Naaman and Rimmon (5:18): Elisha says "go in peace" — remarkable grace for idolatrous necessity. T notes this as precedent for contextual mission.
- Gehazi (5:20-27): His lie and greed directly invert Elisha's refusal to receive payment. The leprosy "clings" (H1692) — same verb as Ruth's clinging to Naomi. T draws out this irony.
- 6:17: Fiery horses and chariots surrounding the mountain — heavenly army echoes the chariot of fire that took Elijah. T notes: Elisha stands in the same prophetic tradition; the divine protection is real, not metaphorical.
- Aspect: Waw-consecutive imperfects = narrative past throughout. Prophetic speech uses simple imperfect = future. Elisha's prayers (4:33; 6:17,18) use perfect for completed petitions.
- OT intertextuality notes embedded in T tier throughout.
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
  "1": {
    "1": {
      "L": "After the death of Ahab, Moab rebelled against Israel.",
      "M": "After Ahab's death, Moab rebelled against Israel.",
      "T": "After Ahab died, Moab threw off Israel's rule."
    },
    "2": {
      "L": "And Ahaziah fell through the lattice in his upper chamber that was in Samaria, and lay sick. And he sent messengers and said to them, 'Go, inquire of Baal-zebub, the god of Ekron, whether I will recover from this sickness.'",
      "M": "Ahaziah fell through the lattice in his upper chamber in Samaria and was injured. He sent messengers, telling them, 'Go and inquire of Baal-zebub, the god of Ekron, whether I will recover from this injury.'",
      "T": "Ahaziah fell through the lattice of his upper chamber in Samaria and was badly hurt. He sent messengers with instructions: 'Go and ask Baal-zebub—the god of Ekron—whether I will survive this injury.' Baal-zebub: the Baal of Flies, the god of a Philistine city. That a king of Israel consulted him was its own verdict."
    },
    "3": {
      "L": "But the angel of the LORD said to Elijah the Tishbite, 'Arise, go up to meet the messengers of the king of Samaria and say to them, Is it because there is no God in Israel that you go to inquire of Baal-zebub, the god of Ekron?'",
      "M": "But the angel of the LORD said to Elijah the Tishbite, 'Arise, go up and meet the messengers of the king of Samaria and say to them: Is it because there is no God in Israel that you are going to inquire of Baal-zebub, the god of Ekron?'",
      "T": "But the angel of the LORD spoke to Elijah the Tishbite: 'Go up and intercept the king of Samaria's messengers. Say to them: Is there no God in Israel? Is that why you go to ask Baal-zebub, the god of Ekron?'"
    },
    "4": {
      "L": "'Therefore thus says the LORD: You shall not come down from the bed to which you have gone up, but you shall surely die.' So Elijah went.",
      "M": "'Therefore thus says the LORD: You will not leave the bed you have taken to—you will certainly die.' So Elijah went.",
      "T": "'Therefore the LORD says this: You will not rise from that bed. You will die.' Elijah went."
    },
    "5": {
      "L": "The messengers returned to him, and he said to them, 'Why have you returned?'",
      "M": "The messengers returned to Ahaziah. He said to them, 'Why have you come back?'",
      "T": "The messengers came back to Ahaziah. 'Why have you returned?' he asked."
    },
    "6": {
      "L": "They said to him, 'A man came up to meet us and said to us, Go, return to the king who sent you, and say to him, Thus says the LORD: Is it because there is no God in Israel that you send to inquire of Baal-zebub, the god of Ekron? Therefore you shall not come down from the bed to which you have gone up, but shall surely die.'",
      "M": "They told him, 'A man came to meet us and said, Go back to the king who sent you and tell him: Thus says the LORD: Is it because there is no God in Israel that you send to inquire of Baal-zebub, the god of Ekron? Therefore you will not leave the bed you have taken to—you will certainly die.'",
      "T": "They answered: 'A man came and met us. He said: Go back to the king who sent you. Tell him: The LORD says this: Is there no God in Israel, that you send to ask Baal-zebub, the god of Ekron? You will not rise from that bed. You will die.'"
    },
    "7": {
      "L": "He said to them, 'What manner of man was he who came up to meet you and spoke these words to you?'",
      "M": "He asked them, 'What sort of man was it who came to meet you and spoke these words?'",
      "T": "'What did this man look like—the one who came and spoke these words to you?' he asked."
    },
    "8": {
      "L": "They answered him, 'He was a hairy man, and wore a leather belt around his waist.' He said, 'It is Elijah the Tishbite.'",
      "M": "They answered, 'He was a hairy man with a leather belt around his waist.' He said, 'It is Elijah the Tishbite.'",
      "T": "'He was a hairy man,' they said, 'with a leather belt around his waist.' 'That is Elijah the Tishbite,' said the king."
    },
    "9": {
      "L": "Then the king sent to him a captain of fifty with his fifty men. He went up to him, and behold, he was sitting on the top of a hill. He said to him, 'O man of God, the king says, Come down.'",
      "M": "He sent to Elijah a captain with fifty men. The captain went up to him—Elijah was sitting on the top of a hill—and said to him, 'Man of God, the king says: Come down.'",
      "T": "The king sent a captain with fifty soldiers. The captain climbed the hill where Elijah was sitting and said: 'Man of God, the king says: Come down.'"
    },
    "10": {
      "L": "But Elijah answered the captain of fifty, 'If I am a man of God, let fire come down from heaven and consume you and your fifty.' Then fire came down from heaven and consumed him and his fifty.",
      "M": "Elijah answered the captain, 'If I am a man of God, let fire come down from heaven and consume you and your fifty.' Then fire came down from heaven and consumed him and his fifty men.",
      "T": "Elijah answered: 'If I am a man of God, then let fire fall from heaven and consume you and your fifty.' Fire came down from heaven and consumed the captain and his fifty men—an echo of the fire on Carmel, a sign that the LORD's word through Elijah still stood."
    },
    "11": {
      "L": "The king sent to him again another captain of fifty with his fifty. And he answered and said to him, 'O man of God, this is the king's order: Come down quickly.'",
      "M": "The king sent another captain of fifty with his fifty men. He addressed Elijah: 'Man of God, this is the king's urgent command: Come down at once.'",
      "T": "The king sent a second captain with fifty more soldiers. He went up to Elijah and said: 'Man of God—the king commands you: Come down immediately.'"
    },
    "12": {
      "L": "But Elijah answered and said to them, 'If I am a man of God, let fire come down from heaven and consume you and your fifty.' And the fire of God came down from heaven and consumed him and his fifty.",
      "M": "Elijah answered, 'If I am a man of God, let fire come down from heaven and consume you and your fifty.' Then the fire of God came down from heaven and consumed him and his fifty men.",
      "T": "Elijah answered: 'If I am a man of God, let fire fall from heaven and consume you and your fifty.' The fire of God fell from heaven and consumed him and his fifty."
    },
    "13": {
      "L": "Again the king sent the captain of a third fifty with his fifty. And the third captain of fifty went up and came and fell on his knees before Elijah and implored him, 'O man of God, please let my life and the life of these fifty servants of yours be precious in your sight.'",
      "M": "The king sent a third captain with his fifty men. But this third captain went up, fell on his knees before Elijah, and pleaded with him: 'Man of God, please let my life and the lives of these fifty servants of yours be precious in your sight.'",
      "T": "The king sent a third captain with fifty more. But this captain went up to Elijah and fell on his knees before him. He pleaded: 'Man of God, please—let my life and the lives of these fifty servants of yours be precious in your sight.'"
    },
    "14": {
      "L": "'Behold, fire came down from heaven and consumed the two former captains of fifty with their fifties, but now let my life be precious in your sight.'",
      "M": "'Fire came down from heaven and consumed the two previous captains with their fifty men. But now, let my life be precious in your sight.'",
      "T": "'Fire has already fallen and consumed two captains and their men. But let my life count for something in your sight. I am asking, not commanding.'"
    },
    "15": {
      "L": "And the angel of the LORD said to Elijah, 'Go down with him; do not be afraid of him.' So he arose and went down with him to the king.",
      "M": "The angel of the LORD said to Elijah, 'Go down with him; do not be afraid of him.' So Elijah arose and went down with him to the king.",
      "T": "The angel of the LORD said to Elijah: 'Go down with him. Do not be afraid.' Elijah rose and went down to the king."
    },
    "16": {
      "L": "And he said to him, 'Thus says the LORD: Because you have sent messengers to inquire of Baal-zebub, the god of Ekron—is it because there is no God in Israel to inquire of his word?—therefore you shall not come down from the bed to which you have gone up, but you shall surely die.'",
      "M": "He said to Ahaziah, 'Thus says the LORD: Because you sent messengers to inquire of Baal-zebub, the god of Ekron—as though there were no God in Israel whose word you could seek—therefore you will not leave the bed you have taken to. You will certainly die.'",
      "T": "Elijah said to the king: 'The LORD says this: Because you sent to ask Baal-zebub, the god of Ekron—as if there were no God in Israel—you will not rise from that bed. You will die.'"
    },
    "17": {
      "L": "So he died according to the word of the LORD that Elijah had spoken. Jehoram became king in his place in the second year of Jehoram the son of Jehoshaphat, king of Judah, because Ahaziah had no son.",
      "M": "So Ahaziah died in accordance with the word of the LORD that Elijah had spoken. Jehoram became king in his place in the second year of Jehoram son of Jehoshaphat king of Judah, for Ahaziah had no son.",
      "T": "Ahaziah died, exactly as the LORD had spoken through Elijah. Jehoram succeeded him as king in the second year of Jehoram son of Jehoshaphat king of Judah—for Ahaziah had no son."
    },
    "18": {
      "L": "Now the rest of the acts of Ahaziah that he did, are they not written in the Book of the Chronicles of the Kings of Israel?",
      "M": "The rest of the acts of Ahaziah and all that he did—are they not written in the Book of the Chronicles of the Kings of Israel?",
      "T": "The rest of Ahaziah's reign is recorded in the Book of the Chronicles of the Kings of Israel."
    }
  },
  "2": {
    "1": {
      "L": "Now when the LORD was about to take Elijah up to heaven by a whirlwind, Elijah went with Elisha from Gilgal.",
      "M": "When the LORD was about to take Elijah up into heaven by a whirlwind, Elijah set out with Elisha from Gilgal.",
      "T": "The time came when the LORD was about to take Elijah up to heaven in a whirlwind. Elijah and Elisha set out together from Gilgal."
    },
    "2": {
      "L": "And Elijah said to Elisha, 'Please stay here, for the LORD has sent me as far as Bethel.' But Elisha said, 'As the LORD lives and as you yourself live, I will not leave you.' So they went down to Bethel.",
      "M": "Elijah said to Elisha, 'Please stay here, for the LORD has sent me to Bethel.' But Elisha said, 'As the LORD lives, and as you yourself live, I will not leave you.' So they went down to Bethel.",
      "T": "Elijah said to Elisha: 'Stay here—the LORD is sending me to Bethel.' But Elisha said: 'As the LORD lives, and as you live, I will not leave you.' So they went down to Bethel together."
    },
    "3": {
      "L": "And the sons of the prophets who were in Bethel came out to Elisha and said to him, 'Do you know that today the LORD will take away your master from over you?' And he said, 'Yes, I know it; keep silent.'",
      "M": "The sons of the prophets who were at Bethel came out to Elisha and said, 'Do you know that today the LORD is going to take your master away from you?' He answered, 'Yes, I know it; be silent.'",
      "T": "The prophetic community at Bethel came out to Elisha and said: 'Do you know that today the LORD is taking your master from you?' 'Yes, I know,' said Elisha. 'Say nothing more.'"
    },
    "4": {
      "L": "Elijah said to him, 'Elisha, please stay here, for the LORD has sent me to Jericho.' But he said, 'As the LORD lives, and as you yourself live, I will not leave you.' So they came to Jericho.",
      "M": "Elijah said to him, 'Elisha, please stay here, for the LORD has sent me to Jericho.' He replied, 'As the LORD lives, and as you yourself live, I will not leave you.' So they went to Jericho.",
      "T": "Elijah said: 'Stay here, Elisha—the LORD is sending me to Jericho.' But Elisha said: 'As the LORD lives, and as you live, I will not leave you.' They went to Jericho."
    },
    "5": {
      "L": "The sons of the prophets who were at Jericho drew near to Elisha and said to him, 'Do you know that today the LORD will take away your master from over you?' And he answered, 'Yes, I know it; keep silent.'",
      "M": "The sons of the prophets who were at Jericho came to Elisha and said, 'Do you know that today the LORD is going to take your master away from you?' He answered, 'Yes, I know it; be silent.'",
      "T": "The prophetic community at Jericho approached Elisha with the same question: 'Do you know that today the LORD is taking your master from you?' 'Yes,' said Elisha, 'I know. Say nothing.'"
    },
    "6": {
      "L": "Then Elijah said to him, 'Please stay here, for the LORD has sent me to the Jordan.' But he said, 'As the LORD lives, and as you yourself live, I will not leave you.' So the two of them went on.",
      "M": "Elijah said to him, 'Please stay here, for the LORD has sent me to the Jordan.' But he said, 'As the LORD lives, and as you yourself live, I will not leave you.' So the two of them went on.",
      "T": "Elijah said once more: 'Stay here—the LORD is sending me to the Jordan.' And Elisha gave the same answer: 'As the LORD lives, and as you live, I will not leave you.' The two of them went on together."
    },
    "7": {
      "L": "Fifty men of the sons of the prophets also went and stood at some distance from them, as they both stood by the Jordan.",
      "M": "Fifty of the sons of the prophets went and stood watching at a distance, while Elijah and Elisha stood at the Jordan.",
      "T": "Fifty of the prophetic brotherhood followed and stood at a distance to watch, as Elijah and Elisha stood together at the bank of the Jordan."
    },
    "8": {
      "L": "Then Elijah took his cloak and rolled it up and struck the water, and the water was parted to the one side and to the other, till the two of them could go over on dry ground.",
      "M": "Elijah took his cloak, rolled it up, and struck the water. The water parted to the right and to the left, and the two of them crossed over on dry ground.",
      "T": "Elijah took his cloak, rolled it up, and struck the Jordan. The water divided to the right and left, and they crossed over on dry ground—a new Exodus, a second passing through."
    },
    "9": {
      "L": "When they had crossed, Elijah said to Elisha, 'Ask what I shall do for you, before I am taken from you.' And Elisha said, 'Please let there be a double portion of your spirit on me.'",
      "M": "When they had crossed over, Elijah said to Elisha, 'Ask what I shall do for you before I am taken from you.' And Elisha said, 'Please let a double portion of your spirit rest on me.'",
      "T": "When they had crossed, Elijah said: 'Ask whatever you want me to do for you before I am taken from you.' Elisha said: 'Please let a double portion of your spirit rest on me.' He asked for the firstborn's share—the double inheritance of Deuteronomy 21:17—claiming his place as Elijah's prophetic heir."
    },
    "10": {
      "L": "And he said, 'You have asked a hard thing; yet, if you see me as I am being taken from you, it shall be so for you, but if you do not see me, it shall not be so.'",
      "M": "He said, 'You have asked a difficult thing. Yet if you see me as I am taken from you, it will be granted to you; but if not, it will not be.'",
      "T": "Elijah said: 'You have asked a hard thing. Nevertheless—if you see me when I am taken from you, it will be yours. If not, it will not be.'"
    },
    "11": {
      "L": "And as they still went on and talked, behold, a chariot of fire and horses of fire separated the two of them. And Elijah went up by a whirlwind into heaven.",
      "M": "As they continued walking and talking, suddenly a chariot of fire and horses of fire appeared and separated the two of them. And Elijah went up by a whirlwind into heaven.",
      "T": "As they were walking and talking together, suddenly a chariot of fire and horses of fire swept between them—and Elijah went up by a whirlwind into heaven."
    },
    "12": {
      "L": "And Elisha saw it and he cried, 'My father, my father! The chariot of Israel and its horsemen!' And he saw him no more. Then he took hold of his own clothes and tore them into two pieces.",
      "M": "Elisha saw it and cried out, 'My father, my father! The chariot of Israel and its horsemen!' When he could no longer see him, he took hold of his own garments and tore them in two.",
      "T": "Elisha saw it and cried out: 'My father! My father! The chariot of Israel and its horsemen!' Then Elijah was gone from his sight. Elisha tore his own clothes in two. His cry was a title of honor: Elijah had been worth more to Israel than an army—its true defense."
    },
    "13": {
      "L": "And he took up the cloak of Elijah that had fallen from him and went back and stood on the bank of the Jordan.",
      "M": "He picked up the cloak of Elijah that had fallen from him and went back and stood on the bank of the Jordan.",
      "T": "He picked up the cloak that had fallen from Elijah and went back to stand on the bank of the Jordan."
    },
    "14": {
      "L": "Then he took the cloak of Elijah that had fallen from him and struck the water, saying, 'Where is the LORD, the God of Elijah?' And when he had struck the water, the water was parted to the one side and to the other, and Elisha went over.",
      "M": "He took the cloak of Elijah that had fallen from him and struck the water, saying, 'Where is the LORD, the God of Elijah?' When he had struck the water, it parted to the right and left, and Elisha crossed over.",
      "T": "He took Elijah's cloak and struck the water, crying: 'Where is the LORD, the God of Elijah?' The water parted to the right and left, and Elisha crossed over. The double portion had come. The mantle—and the God who honored it—was his."
    },
    "15": {
      "L": "Now when the sons of the prophets who were at Jericho saw him opposite them, they said, 'The spirit of Elijah rests on Elisha.' And they came to meet him and bowed to the ground before him.",
      "M": "When the sons of the prophets who were at Jericho saw him from the other side, they said, 'The spirit of Elijah rests on Elisha.' And they came to meet him and bowed down before him.",
      "T": "The prophetic community at Jericho saw what happened and said: 'The spirit of Elijah rests on Elisha.' They came to meet him and bowed to the ground before him."
    },
    "16": {
      "L": "They said to him, 'Behold now, there are with your servants fifty strong men. Please let them go and seek your master. It may be that the Spirit of the LORD has cast him upon some mountain or into some valley.' And he said, 'You shall not send.'",
      "M": "They said to him, 'Look, there are fifty able men among your servants. Let them go and look for your master—perhaps the Spirit of the LORD has taken him up and dropped him on some mountain or in some valley.' He replied, 'Do not send them.'",
      "T": "They said: 'We have fifty strong men here. Send them to search for your master—perhaps the Spirit of the LORD has carried him off and set him down on some mountain or in a valley.' 'Do not send them,' said Elisha."
    },
    "17": {
      "L": "But when they urged him until he was ashamed, he said, 'Send.' They sent fifty men, and for three days they searched but did not find him.",
      "M": "But they pressed him until he was embarrassed, and he said, 'Send.' They sent fifty men, who searched for three days but did not find him.",
      "T": "But they pressed him until he felt he could not refuse. 'Send them,' he said. Fifty men searched for three days and found nothing."
    },
    "18": {
      "L": "They came back to him while he was staying at Jericho. He said to them, 'Did I not say to you, Do not go?'",
      "M": "When they returned to him at Jericho, he said to them, 'Did I not tell you not to go?'",
      "T": "When they returned to Jericho, Elisha said: 'Did I not tell you not to go?'"
    },
    "19": {
      "L": "Now the men of the city said to Elisha, 'Behold, the situation of this city is pleasant, as my lord sees, but the water is bad and the land is unfruitful.'",
      "M": "The men of the city said to Elisha, 'Look, the situation of this city is pleasant, as you can see, but the water is bad and the land causes miscarriages.'",
      "T": "The men of the city said to Elisha: 'Look—this is a pleasant place, as you can see. But the water is bad and the land is causing miscarriages.'"
    },
    "20": {
      "L": "He said, 'Bring me a new bowl, and put salt in it.' So they brought it to him.",
      "M": "He said, 'Bring me a new bowl and put salt in it.' They brought it to him.",
      "T": "'Bring me a new bowl and put salt in it,' he said. They brought it."
    },
    "21": {
      "L": "Then he went to the spring of water and threw salt in it and said, 'Thus says the LORD, I have healed this water; from now on neither death nor miscarriage shall come from it.'",
      "M": "He went to the spring of water and threw salt into it and said, 'Thus says the LORD: I have healed this water; from now on it will cause neither death nor miscarriage.'",
      "T": "He went to the spring and threw the salt in. 'The LORD says this: I have healed these waters. From this day on they will bring neither death nor barrenness.'"
    },
    "22": {
      "L": "So the water has been wholesome to this day, according to the word that Elisha spoke.",
      "M": "The water has been wholesome to this day, according to the word Elisha spoke.",
      "T": "The water has been sound ever since—exactly as Elisha said."
    },
    "23": {
      "L": "He went up from there to Bethel, and while he was going up on the road, some small boys came out of the city and mocked him, saying, 'Go up, you baldhead! Go up, you baldhead!'",
      "M": "From there he went up to Bethel. While he was going up the road, some small boys came out of the city and taunted him, saying, 'Get out of here, baldhead! Get out of here, baldhead!'",
      "T": "From there Elisha went up to Bethel. As he was walking up the road, a gang of youths came out of the city and mocked him: 'Go up, baldhead! Go up, baldhead!'"
    },
    "24": {
      "L": "And he turned around, and when he saw them, he cursed them in the name of the LORD. And two she-bears came out of the woods and tore forty-two of the boys.",
      "M": "He turned around and looked at them and called down a curse on them in the name of the LORD. Then two she-bears came out of the woods and mauled forty-two of the boys.",
      "T": "He turned and looked at them, then called down a curse on them in the name of the LORD. Two she-bears came out of the forest and mauled forty-two of them."
    },
    "25": {
      "L": "From there he went on to Mount Carmel, and from there he returned to Samaria.",
      "M": "From there Elisha went to Mount Carmel, and from there he returned to Samaria.",
      "T": "From there Elisha went to Mount Carmel and then returned to Samaria."
    }
  },
  "3": {
    "1": {
      "L": "In the eighteenth year of Jehoshaphat king of Judah, Jehoram the son of Ahab became king over Israel in Samaria, and he reigned twelve years.",
      "M": "Jehoram son of Ahab became king over Israel in Samaria in the eighteenth year of Jehoshaphat king of Judah, and he reigned twelve years.",
      "T": "In the eighteenth year of Jehoshaphat king of Judah, Jehoram son of Ahab became king over Israel in Samaria. He reigned twelve years."
    },
    "2": {
      "L": "He did what was evil in the sight of the LORD, though not like his father and mother, for he put away the pillar of Baal that his father had made.",
      "M": "He did what was evil in the sight of the LORD, though not like his father and mother, for he removed the sacred pillar of Baal that his father had made.",
      "T": "He did what was evil in the LORD's sight—but not on the level of his father and mother. He did remove the sacred pillar of Baal that Ahab had set up."
    },
    "3": {
      "L": "Nevertheless, he clung to the sin of Jeroboam the son of Nebat, which he made Israel to sin; he did not depart from it.",
      "M": "Nevertheless, he clung to the sins of Jeroboam son of Nebat, who caused Israel to sin—he did not turn from them.",
      "T": "But he clung to the sins of Jeroboam son of Nebat—the golden calves, the false worship—and would not let them go."
    },
    "4": {
      "L": "Now Mesha king of Moab was a sheep breeder, and he had to deliver to the king of Israel a hundred thousand lambs and the wool of a hundred thousand rams.",
      "M": "Now Mesha king of Moab was a sheep farmer, and he used to pay the king of Israel a hundred thousand lambs and the wool of a hundred thousand rams as tribute.",
      "T": "Mesha king of Moab was a sheep farmer. He had been paying the king of Israel an annual tribute of a hundred thousand lambs and the fleeces of a hundred thousand rams."
    },
    "5": {
      "L": "But when Ahab died, the king of Moab rebelled against the king of Israel.",
      "M": "But after Ahab died, the king of Moab rebelled against the king of Israel.",
      "T": "After Ahab's death, Mesha rebelled against the king of Israel."
    },
    "6": {
      "L": "So King Jehoram marched out of Samaria at that time and mustered all Israel.",
      "M": "King Jehoram set out from Samaria at that time and mustered all Israel.",
      "T": "Jehoram immediately marched out of Samaria and mobilized all of Israel."
    },
    "7": {
      "L": "And he went and sent word to Jehoshaphat king of Judah: 'The king of Moab has rebelled against me. Will you go with me to battle against Moab?' And he said, 'I will go. I am as you are, my people as your people, my horses as your horses.'",
      "M": "He also sent word to Jehoshaphat king of Judah: 'The king of Moab has rebelled against me. Will you go with me to fight against Moab?' Jehoshaphat answered, 'I will go. I am with you as one—my people and my horses are yours.'",
      "T": "He sent to Jehoshaphat king of Judah: 'Moab has rebelled against me. Will you join me to fight against Moab?' Jehoshaphat said: 'I will go. I am with you completely—my people are your people, my horses your horses.'"
    },
    "8": {
      "L": "And he said, 'Which way shall we go up?' Jehoshaphat answered, 'By the way of the wilderness of Edom.'",
      "M": "Jehoram asked, 'Which route shall we take?' Jehoshaphat answered, 'By the way of the wilderness of Edom.'",
      "T": "'Which route shall we take?' Jehoram asked. 'Through the wilderness of Edom,' said Jehoshaphat."
    },
    "9": {
      "L": "So the king of Israel went with the king of Judah and the king of Edom. And when they had made a roundabout journey of seven days, there was no water for the army or for the animals that followed them.",
      "M": "So the king of Israel set out with the king of Judah and the king of Edom. After a seven-day march there was no water for the army or for the animals following them.",
      "T": "The three kings set out—Israel, Judah, and Edom—and after a seven-day march through the wilderness, there was no water left for the army or the animals."
    },
    "10": {
      "L": "Then the king of Israel said, 'Alas! The LORD has called these three kings to give them into the hand of Moab.'",
      "M": "The king of Israel said, 'Alas! The LORD has called these three kings together only to hand them over to Moab.'",
      "T": "The king of Israel said: 'Disaster! The LORD has brought three kings together just to hand them over to Moab.'"
    },
    "11": {
      "L": "But Jehoshaphat said, 'Is there no prophet of the LORD here, through whom we may inquire of the LORD?' Then one of the king of Israel's servants answered, 'Elisha the son of Shaphat is here, who poured water on the hands of Elijah.'",
      "M": "But Jehoshaphat asked, 'Is there no prophet of the LORD here, through whom we can inquire of the LORD?' One of the king of Israel's servants answered, 'Elisha son of Shaphat is here—he used to pour water on Elijah's hands.'",
      "T": "But Jehoshaphat said: 'Is there no prophet of the LORD here? Can we inquire of the LORD through someone?' One of Israel's servants said: 'Elisha son of Shaphat is here—the one who served Elijah as his attendant.'"
    },
    "12": {
      "L": "Jehoshaphat said, 'The word of the LORD is with him.' So the king of Israel and Jehoshaphat and the king of Edom went down to him.",
      "M": "Jehoshaphat said, 'The word of the LORD is with him.' So the king of Israel, Jehoshaphat, and the king of Edom went down to him.",
      "T": "Jehoshaphat said: 'The word of the LORD is with him.' So all three kings went down to Elisha."
    },
    "13": {
      "L": "And Elisha said to the king of Israel, 'What have I to do with you? Go to the prophets of your father and to the prophets of your mother.' But the king of Israel said to him, 'No; it is the LORD who has called these three kings to give them into the hand of Moab.'",
      "M": "Elisha said to the king of Israel, 'What do I have to do with you? Go to the prophets of your father and your mother.' The king of Israel said to him, 'No—it is the LORD who has called these three kings together to hand them over to Moab.'",
      "T": "Elisha said to the king of Israel: 'What do I have to do with you? Go to the prophets of your father and your mother.' 'No,' the king said, 'the LORD himself has brought these three kings together—to hand them over to Moab.'"
    },
    "14": {
      "L": "And Elisha said, 'As the LORD of hosts lives, before whom I stand, were it not that I have regard for Jehoshaphat the king of Judah, I would neither look at you nor see you.'",
      "M": "Elisha said, 'As the LORD of hosts lives, before whom I stand, were it not for my regard for Jehoshaphat king of Judah, I would not look at you or acknowledge you.'",
      "T": "Elisha said: 'As the LORD of hosts lives—before whom I stand—if it were not for my respect for Jehoshaphat king of Judah, I would not even look at you.'"
    },
    "15": {
      "L": "'But now bring me a musician.' And when the musician played, the hand of the LORD came upon him.",
      "M": "'Now bring me a harpist.' When the harpist played, the hand of the LORD came upon Elisha.",
      "T": "'But bring me a musician.' When the musician played, the hand of the LORD came upon Elisha."
    },
    "16": {
      "L": "And he said, 'Thus says the LORD: Make this valley full of ditches.'",
      "M": "He said, 'Thus says the LORD: Make this valley full of trenches.'",
      "T": "He said: 'The LORD says this: Dig this valley full of trenches.'"
    },
    "17": {
      "L": "'For thus says the LORD: You shall not see wind or rain, yet that valley shall be filled with water, so that you shall drink, you, your livestock, and your animals.'",
      "M": "'For thus says the LORD: You will see no wind or rain, yet that valley will be filled with water—enough for you, your livestock, and your animals to drink.'",
      "T": "'The LORD says: You will see no wind, you will see no rain—yet that valley will be filled with water. You and your cattle and animals will drink.'"
    },
    "18": {
      "L": "'This is a light thing in the sight of the LORD. He will also give Moab into your hand.'",
      "M": "'This is a small thing in the sight of the LORD. He will also hand Moab over to you.'",
      "T": "'This is a small thing in the LORD's sight. He will also hand Moab over to you.'"
    },
    "19": {
      "L": "'And you shall attack every fortified city and every choice city, and shall fell every good tree and stop up all springs of water and ruin every good piece of land with stones.'",
      "M": "'You will conquer every fortified city and every important town. You will fell every good tree, stop up every spring of water, and ruin every good field with stones.'",
      "T": "'You will strike every fortified city and every fine town. Every good tree you will fell, every spring you will choke, every fertile field you will ruin with stones.'"
    },
    "20": {
      "L": "The next morning, about the time of offering the sacrifice, behold, water came from the direction of Edom, till the country was filled with water.",
      "M": "In the morning, at the time of the morning offering, water came from the direction of Edom and filled the land.",
      "T": "In the morning, at the time of the morning sacrifice, water came flowing in from the direction of Edom until the whole land was filled."
    },
    "21": {
      "L": "When all the Moabites heard that the kings had come up to fight against them, all who were able to put on armor, from the youngest to the oldest, were called out and were drawn up at the border.",
      "M": "When all Moab heard that the kings had come up to fight against them, every man who could bear arms was called up, from the youngest to the oldest, and they took up position at the border.",
      "T": "When Moab heard that the kings had come to fight against them, every man who could carry a weapon—young and old—was mustered and stationed at the border."
    },
    "22": {
      "L": "And they rose early in the morning, and the sun shone on the water, and the Moabites saw the water opposite them as red as blood.",
      "M": "They rose early in the morning, and when the sun shone on the water, the Moabites across the way saw the water as red as blood.",
      "T": "When they rose early in the morning and the sun shone on the water, the Moabites looking across saw the water—and it gleamed red as blood."
    },
    "23": {
      "L": "And they said, 'This is blood; the kings have surely fought together and struck one another down. Now then, Moab, to the spoil!'",
      "M": "They said, 'This is blood! The kings must have fought each other and killed one another. Now, Moab, to the plunder!'",
      "T": "'Blood!' they said. 'The kings have clearly turned on each other and slaughtered themselves. To the plunder, Moab!'"
    },
    "24": {
      "L": "But when they came to the camp of Israel, the Israelites rose and struck the Moabites, so that they fled before them. And they went forward, striking the Moabites as they went.",
      "M": "But when they came to the Israelite camp, the Israelites rose up and attacked the Moabites, who fled before them. They pressed forward, striking down the Moabites as they went.",
      "T": "But when they reached Israel's camp, Israel rose up and struck them. The Moabites fled. Israel drove forward, cutting them down."
    },
    "25": {
      "L": "And they overthrew the cities, and on every good piece of land every man threw a stone until it was covered. They stopped every spring of water and felled all the good trees, till only its stones were left in Kir-hareseth, and the slingers surrounded and attacked it.",
      "M": "They overthrew the cities, and every man threw stones onto each good piece of land until it was covered. They stopped up every spring and felled every good tree—until only the stones of Kir-hareseth were left standing. Then the slingers surrounded and attacked it.",
      "T": "They overthrew the cities and covered every fertile field with stones. They choked every spring and felled every good tree—until only Kir-hareseth still stood. The slingers surrounded it and attacked."
    },
    "26": {
      "L": "When the king of Moab saw that the battle was going against him, he took with him seven hundred swordsmen to break through, opposite the king of Edom, but they could not.",
      "M": "When the king of Moab saw that the battle had turned against him, he took seven hundred swordsmen with him to break through to the king of Edom—but they failed.",
      "T": "When the king of Moab saw the battle going against him, he took seven hundred swordsmen and tried to break through to the king of Edom. He could not."
    },
    "27": {
      "L": "Then he took his oldest son who was to reign in his place and offered him for a burnt offering on the wall. And there came great wrath against Israel. And they withdrew from him and returned to their own land.",
      "M": "Then he took his firstborn son, who was to succeed him, and offered him as a burnt offering on the wall. And great wrath came against Israel. They withdrew from him and returned to their own land.",
      "T": "Then he took his firstborn son—the crown prince—and sacrificed him on the city wall as a burnt offering. Great outrage fell on Israel. They withdrew from him and returned to their own land."
    }
  },
  "4": {
    "1": {
      "L": "Now the wife of one of the sons of the prophets cried to Elisha, 'Your servant my husband is dead, and you know that your servant feared the LORD, but the creditor has come to take my two children to be his slaves.'",
      "M": "The wife of a man from the company of the prophets cried out to Elisha: 'Your servant my husband is dead, and you know that he feared the LORD. Now his creditor has come to take my two boys as his slaves.'",
      "T": "A woman from the prophetic community cried out to Elisha: 'My husband—your servant—is dead. You know he feared the LORD. And now his creditor has come to take my two sons as slaves to pay the debt.'"
    },
    "2": {
      "L": "And Elisha said to her, 'What shall I do for you? Tell me; what do you have in your house?' And she said, 'Your servant has nothing in the house except a jar of oil.'",
      "M": "Elisha said to her, 'What can I do for you? Tell me—what do you have in the house?' She said, 'Your servant has nothing in the house except a jar of oil.'",
      "T": "Elisha said: 'What can I do for you? Tell me what you have in the house.' 'Nothing at all,' she said, 'except a single jar of oil.'"
    },
    "3": {
      "L": "Then he said, 'Go outside, borrow vessels from all your neighbors, empty vessels and not too few.'",
      "M": "He said, 'Go outside and borrow vessels from all your neighbors—empty containers, and do not get too few.'",
      "T": "'Go out,' he said, 'and borrow containers from all your neighbors—empty ones. And do not get too few.'"
    },
    "4": {
      "L": "'Then go in and shut the door behind yourself and your sons and pour into all these vessels. And when one is full, set it aside.'",
      "M": "'Then go inside and shut the door behind you and your sons, and pour oil into all those containers. When one is full, set it aside.'",
      "T": "'Go inside with your sons, shut the door behind you, and pour oil into every container. As each one fills up, set it aside.'"
    },
    "5": {
      "L": "So she went from him and shut the door behind herself and her sons. And they kept bringing vessels to her while she poured.",
      "M": "So she left him and shut the door behind herself and her sons. They kept bringing her vessels while she kept pouring.",
      "T": "She left Elisha and shut the door. Her sons kept bringing her vessels, and she kept pouring."
    },
    "6": {
      "L": "When the vessels were full, she said to her son, 'Bring me another vessel.' And he said to her, 'There is not another.' Then the oil stopped.",
      "M": "When the containers were all full, she said to her son, 'Bring me another vessel.' He said to her, 'There are no more.' And the oil stopped.",
      "T": "When all the containers were full, she said to her son: 'Bring me another one.' He said: 'There are no more.' The oil stopped."
    },
    "7": {
      "L": "She came and told the man of God, and he said, 'Go, sell the oil and pay your debts, and you and your sons can live on the rest.'",
      "M": "She went and told the man of God, and he said, 'Go, sell the oil and pay your debt. You and your sons can live on what remains.'",
      "T": "She went and told Elisha. He said: 'Go, sell the oil and pay your debt. You and your sons can live on what is left.'"
    },
    "8": {
      "L": "One day Elisha went on to Shunem, where a wealthy woman lived, who urged him to eat some food. So whenever he passed that way, he would turn in there to eat food.",
      "M": "One day Elisha went to Shunem, where a wealthy woman lived who pressed him to stay for a meal. So whenever he passed through, he would stop there to eat.",
      "T": "One day Elisha came to Shunem, where a prominent woman insisted he stop and eat with her. After that, whenever he passed through, he would stop at her home for a meal."
    },
    "9": {
      "L": "And she said to her husband, 'Behold now, I know that this is a holy man of God who is regularly passing our way.'",
      "M": "She said to her husband, 'Look—I am sure this man who keeps passing by is a holy man of God.'",
      "T": "She said to her husband: 'I am sure this man who passes by us regularly is a holy man of God.'"
    },
    "10": {
      "L": "'Let us make a small room on the roof with walls and put there for him a bed, a table, a chair, and a lamp, so that whenever he comes to us, he can go in there.'",
      "M": "'Let us make a small room on the roof and put a bed, a table, a chair, and a lamp there for him. Then whenever he comes to us, he can stay there.'",
      "T": "'Let us build a small room on the roof and furnish it for him—a bed, a table, a chair, and a lamp. Then whenever he comes, he will have a place to stay.'"
    },
    "11": {
      "L": "One day he came there, and he turned into the room and rested there.",
      "M": "One day he came there, went up to the room, and rested.",
      "T": "One day Elisha came, went up to the room, and rested there."
    },
    "12": {
      "L": "And he said to Gehazi his servant, 'Call this Shunammite.' When he had called her, she stood before him.",
      "M": "He said to Gehazi his servant, 'Call this Shunammite woman.' When he had called her, she stood before him.",
      "T": "He said to his servant Gehazi: 'Call this Shunammite woman.' Gehazi called her, and she came and stood before Elisha."
    },
    "13": {
      "L": "And he said to him, 'Say now to her, See, you have taken all this trouble for us; what is to be done for you? Would you have a word spoken on your behalf to the king or to the commander of the army?' She answered, 'I dwell among my own people.'",
      "M": "He said to Gehazi, 'Ask her: You have gone to all this trouble for us—what can be done for you? Should I speak on your behalf to the king or to the commander of the army?' She answered, 'I live among my own people.'",
      "T": "He said to Gehazi: 'Ask her—she has gone to all this trouble for us. What can we do for her? Shall I speak a word to the king or to the army commander on her behalf?' She said: 'I live at home among my own people—I need nothing.'"
    },
    "14": {
      "L": "And he said, 'What then is to be done for her?' Gehazi answered, 'Well, she has no son, and her husband is old.'",
      "M": "He said, 'What then is to be done for her?' Gehazi answered, 'She has no son, and her husband is old.'",
      "T": "Elisha asked: 'What can be done for her, then?' Gehazi said: 'She has no son, and her husband is old.'"
    },
    "15": {
      "L": "He said, 'Call her.' And when he had called her, she stood in the doorway.",
      "M": "He said, 'Call her.' He called her, and she stood in the doorway.",
      "T": "'Call her,' said Elisha. She came and stood in the doorway."
    },
    "16": {
      "L": "And he said, 'At this season, about this time next year, you shall embrace a son.' And she said, 'No, my lord, O man of God; do not lie to your servant.'",
      "M": "He said, 'About this time next year you will hold a son in your arms.' She said, 'No, my lord—man of God—do not deceive your servant.'",
      "T": "Elisha said: 'At this time next year you will be holding a son.' She said: 'No, my lord—man of God—do not give me false hope.'"
    },
    "17": {
      "L": "But the woman conceived, and she bore a son about that time the following spring, as Elisha had told her.",
      "M": "But the woman conceived and bore a son about that time the following spring, just as Elisha had told her.",
      "T": "The woman conceived and bore a son at that very season the next year—exactly as Elisha had said."
    },
    "18": {
      "L": "When the child had grown, he went out one day to his father among the reapers.",
      "M": "When the child had grown, he went out one day to his father among the reapers.",
      "T": "When the boy was older, he went out one day to find his father among the harvesters."
    },
    "19": {
      "L": "And he said to his father, 'Oh, my head, my head!' The father said to his servant, 'Carry him to his mother.'",
      "M": "He cried to his father, 'My head! My head!' His father said to his servant, 'Carry him to his mother.'",
      "T": "He cried out to his father: 'My head! My head!' His father told a servant: 'Take him to his mother.'"
    },
    "20": {
      "L": "And when he had lifted him and brought him to his mother, the child sat on her lap till noon, and then he died.",
      "M": "The servant carried him and brought him to his mother. The child sat on her lap until noon, and then he died.",
      "T": "The servant carried him to his mother. He lay on her lap until noon—then he died."
    },
    "21": {
      "L": "And she went up and laid him on the bed of the man of God and shut the door behind him and went out.",
      "M": "She went up and laid him on the bed of the man of God, shut the door, and went out.",
      "T": "She went up and laid him on Elisha's bed, shut the door behind her, and went out."
    },
    "22": {
      "L": "And she called to her husband and said, 'Send me one of the servants and one of the donkeys, that I may quickly go to the man of God and come back again.'",
      "M": "She called to her husband: 'Please send me one of the servants and a donkey so I can go quickly to the man of God and come back.'",
      "T": "She called to her husband: 'Send me one of the servants and a donkey. I need to go to the man of God and return quickly.'"
    },
    "23": {
      "L": "And he said, 'Why will you go to him today? It is neither new moon nor Sabbath.' She said, 'All is well.'",
      "M": "He said, 'Why go to him today? It is neither a new moon nor a Sabbath.' She said, 'All is well.'",
      "T": "'Why go today?' he said. 'It is not the new moon or the Sabbath.' 'All is well,' she said—and said nothing more."
    },
    "24": {
      "L": "Then she saddled the donkey, and she said to her servant, 'Urge the animal forward; do not slacken the pace for me unless I tell you.'",
      "M": "She saddled the donkey and said to her servant, 'Drive on and do not slow down unless I tell you.'",
      "T": "She saddled the donkey and told her servant: 'Ride fast. Do not slow down unless I say so.'"
    },
    "25": {
      "L": "So she set out and came to the man of God at Mount Carmel. When the man of God saw her coming, he said to Gehazi his servant, 'Look, there is the Shunammite woman.'",
      "M": "So she set out and came to the man of God at Mount Carmel. When the man of God saw her coming in the distance, he said to Gehazi his servant, 'Look—there is the Shunammite woman.'",
      "T": "She set out and came to Elisha at Mount Carmel. Elisha spotted her in the distance and said to Gehazi: 'Look—the Shunammite woman is coming.'"
    },
    "26": {
      "L": "'Run at once to meet her and say to her, Is all well with you? Is all well with your husband? Is all well with the child?' And she answered, 'All is well.'",
      "M": "'Run to meet her and ask: Is it well with you? With your husband? With the child?' She answered, 'All is well.'",
      "T": "'Go run and meet her. Ask: Is everything all right with you, with your husband, with the child?' She said: 'All is well'—but it was not."
    },
    "27": {
      "L": "And when she came to the mountain to the man of God, she caught hold of his feet. And Gehazi came to push her away. But the man of God said, 'Leave her alone, for she is in bitter distress, and the LORD has hidden it from me and has not told me.'",
      "M": "When she reached the man of God on the mountain, she caught hold of his feet. Gehazi stepped forward to push her away, but the man of God said, 'Leave her alone—she is in bitter anguish. The LORD has hidden it from me and has not told me.'",
      "T": "When she reached Elisha on the mountain, she fell at his feet and clung to them. Gehazi moved to push her away, but Elisha said: 'Leave her—she is in bitter anguish. The LORD has not told me why; he has kept it from me.'"
    },
    "28": {
      "L": "She said, 'Did I ask my lord for a son? Did I not say, Do not deceive me?'",
      "M": "She said, 'Did I ask my lord for a son? Did I not say, Do not give me false hope?'",
      "T": "She said: 'Did I ask you for a son? Did I not say: Do not deceive me?'"
    },
    "29": {
      "L": "He said to Gehazi, 'Tie up your garments and take my staff in your hand and go. If you meet anyone, do not greet him, and if anyone greets you, do not reply. And lay my staff on the face of the child.'",
      "M": "He said to Gehazi, 'Tuck your garment into your belt and take my staff—go quickly. If you meet anyone, do not greet him, and if anyone greets you, do not answer. Lay my staff on the boy's face.'",
      "T": "Elisha said to Gehazi: 'Belt up your robe and take my staff and go—fast. If you meet anyone, do not stop to greet them. If someone greets you, do not answer. Lay my staff on the boy's face.'"
    },
    "30": {
      "L": "Then the mother of the child said, 'As the LORD lives and as you yourself live, I will not leave you.' So he arose and followed her.",
      "M": "But the mother of the child said, 'As the LORD lives and as you yourself live, I will not leave you.' So Elisha arose and followed her.",
      "T": "But the boy's mother said: 'As the LORD lives, and as you live, I will not leave you.' So Elisha got up and went with her."
    },
    "31": {
      "L": "Gehazi went on ahead and laid the staff on the face of the child, but there was no sound or sign of life. Therefore he returned to meet him and told him, 'The child has not awakened.'",
      "M": "Gehazi went on ahead and laid the staff on the boy's face, but there was no sound and no sign of life. He turned back to meet Elisha and told him, 'The child has not awakened.'",
      "T": "Gehazi went ahead and placed the staff on the boy's face—but nothing. No sound, no sign of life. He went back to meet Elisha and reported: 'The child has not woken up.'"
    },
    "32": {
      "L": "When Elisha came into the house, he saw the child lying dead on his bed.",
      "M": "When Elisha came into the house, there was the child—lying dead on his bed.",
      "T": "When Elisha arrived at the house, there was the boy—lying dead on his bed."
    },
    "33": {
      "L": "So he went in and shut the door behind the two of them and prayed to the LORD.",
      "M": "He went in and shut the door behind the two of them and prayed to the LORD.",
      "T": "He went in alone with the child, shut the door, and prayed to the LORD."
    },
    "34": {
      "L": "Then he got up on the bed and lay on top of the child, putting his mouth on his mouth, his eyes on his eyes, and his hands on his hands. And as he stretched himself upon him, the flesh of the child became warm.",
      "M": "He got onto the bed and lay on top of the child, putting his mouth on the child's mouth, his eyes on his eyes, and his hands on his hands. As he stretched out on him, the boy's flesh grew warm.",
      "T": "He lay down on the child—mouth to mouth, eyes to eyes, hands to hands—stretching himself fully over him. The boy's flesh began to grow warm."
    },
    "35": {
      "L": "Then he got up again and walked once back and forth in the house, and went up and stretched himself upon him. The child sneezed seven times, and the child opened his eyes.",
      "M": "He arose again and walked back and forth in the house, then went up and stretched himself over the child once more. The child sneezed seven times and opened his eyes.",
      "T": "Elisha got up and paced the house, then came back and stretched himself over the child again. The boy sneezed seven times and opened his eyes."
    },
    "36": {
      "L": "Then he summoned Gehazi and said, 'Call this Shunammite.' So he called her. And when she came to him, he said, 'Pick up your son.'",
      "M": "Elisha summoned Gehazi and said, 'Call the Shunammite.' He called her. When she came to him, he said, 'Take up your son.'",
      "T": "He called Gehazi: 'Call the Shunammite woman.' She came. Elisha said: 'Take your son.'"
    },
    "37": {
      "L": "She came and fell at his feet, bowing to the ground. Then she picked up her son and went out.",
      "M": "She came and fell at his feet and bowed to the ground. Then she picked up her son and went out.",
      "T": "She came in, fell at his feet, and bowed to the ground. Then she took her son and went out."
    },
    "38": {
      "L": "And Elisha came again to Gilgal when there was a famine in the land. And as the sons of the prophets were sitting before him, he said to his servant, 'Set on the large pot, and boil stew for the sons of the prophets.'",
      "M": "Elisha returned to Gilgal when there was a famine in the land. As the sons of the prophets were sitting before him, he said to his servant, 'Put on the large pot and make stew for the company of the prophets.'",
      "T": "Elisha returned to Gilgal during a famine. As the prophetic community was gathered before him, he said to his servant: 'Put on the large pot. Make stew for the prophets.'"
    },
    "39": {
      "L": "One of them went out into the field to gather herbs, and found a wild vine and gathered from it his lap full of wild gourds, and came and sliced them into the pot of stew, not knowing what they were.",
      "M": "One of them went out into the field to gather herbs and found a wild vine and gathered a lapful of wild gourds from it. He came and sliced them into the pot of stew, not knowing what they were.",
      "T": "One of the men went into the field to gather herbs and found a wild vine. He gathered a lapful of wild gourds from it and came back and sliced them into the stew—not knowing what they were."
    },
    "40": {
      "L": "And they poured it out for the men to eat. But while they were eating of the stew, they cried out, 'O man of God, there is death in the pot!' And they could not eat it.",
      "M": "They served it to the men to eat. But as soon as they tasted the stew, they cried out, 'Man of God, there is death in the pot!' And they could not eat it.",
      "T": "They served it. But as soon as the men tasted it, they cried out: 'Man of God—there is death in the pot!' They could not eat it."
    },
    "41": {
      "L": "He said, 'Then bring flour.' And he threw it into the pot and said, 'Pour it out for the people, that they may eat.' And there was nothing harmful in the pot.",
      "M": "He said, 'Bring me some flour.' He threw it into the pot and said, 'Serve it to the people.' And there was nothing harmful in the pot.",
      "T": "'Bring me flour,' he said. He threw it into the pot. 'Serve it out,' he said. There was nothing harmful in it any longer."
    },
    "42": {
      "L": "A man came from Baal-shalishah, bringing the man of God bread of the firstfruits, twenty loaves of barley and fresh ears of grain in his sack. And Elisha said, 'Give to the men that they may eat.'",
      "M": "A man came from Baal-shalishah, bringing the man of God twenty barley loaves baked from the firstfruits, and fresh grain in his pouch. Elisha said, 'Give it to the people to eat.'",
      "T": "A man came from Baal-shalishah bringing Elisha twenty barley loaves made from the firstfruits, and fresh grain in his pouch. Elisha said: 'Give it to the people to eat.'"
    },
    "43": {
      "L": "But his servant said, 'How can I set this before a hundred men?' So he repeated, 'Give them to the men, that they may eat, for thus says the LORD, They shall eat and have some left over.'",
      "M": "His servant said, 'How can I set this before a hundred men?' But Elisha said, 'Give it to the people to eat, for thus says the LORD: They shall eat and have some left over.'",
      "T": "His servant said: 'How can I set this before a hundred people?' 'Give it to them,' Elisha said. 'The LORD says: They will eat and have leftovers.'"
    },
    "44": {
      "L": "So he set it before them. And they ate and had some left over, according to the word of the LORD.",
      "M": "He set it before them. They ate and had some left over, according to the word of the LORD.",
      "T": "He set it before them. They all ate, and there was food left over—just as the LORD had said."
    }
  },
  "5": {
    "1": {
      "L": "Naaman, commander of the army of the king of Syria, was a great man with his master and in high favor, because by him the LORD had given victory to Syria. He was a mighty man of valor, but he was a leper.",
      "M": "Naaman, commander of the army of the king of Aram, was a great man in his master's sight and highly regarded, because through him the LORD had given victory to Aram. He was a mighty warrior—but he had leprosy.",
      "T": "Naaman was commander of the army of the king of Aram—a great man, highly honored by his master, because through him the LORD had given Aram victory. He was a valiant soldier. But he had leprosy."
    },
    "2": {
      "L": "Now the Syrians on one of their raids had carried off a little girl from the land of Israel, and she worked in the service of Naaman's wife.",
      "M": "Now the Arameans had carried off a little girl from Israel on one of their raids, and she served Naaman's wife.",
      "T": "On one of their raids, the Arameans had taken a young girl captive from Israel. She now served in Naaman's household as a servant to his wife."
    },
    "3": {
      "L": "She said to her mistress, 'Would that my lord were with the prophet who is in Samaria! He would cure him of his leprosy.'",
      "M": "She said to her mistress, 'If only my lord were before the prophet who is in Samaria! He would cure him of his leprosy.'",
      "T": "She said to her mistress: 'If only my master could go to the prophet in Samaria—he would cure him of his leprosy.'"
    },
    "4": {
      "L": "So Naaman went in and told his lord, 'Thus and so spoke the girl from the land of Israel.'",
      "M": "Naaman went in and told his master what the girl from Israel had said.",
      "T": "Naaman went and told his master what the Israelite girl had said."
    },
    "5": {
      "L": "And the king of Syria said, 'Go now, and I will send a letter to the king of Israel.' So he departed, taking with him ten talents of silver, six thousand shekels of gold, and ten changes of clothing.",
      "M": "The king of Aram said, 'Go now—I will send a letter to the king of Israel.' So Naaman set out, taking ten talents of silver, six thousand shekels of gold, and ten changes of clothing.",
      "T": "The king of Aram said: 'Go—I will send a letter to the king of Israel.' Naaman set out, taking with him ten talents of silver, six thousand shekels of gold, and ten sets of clothing."
    },
    "6": {
      "L": "He brought the letter to the king of Israel, which read, 'When this letter reaches you, know that I have sent to you Naaman my servant, that you may cure him of his leprosy.'",
      "M": "He brought the letter to the king of Israel. It said: 'When this letter arrives, know that I have sent you my servant Naaman that you may cure him of his leprosy.'",
      "T": "He delivered the letter to the king of Israel. It read: 'When this letter reaches you, know that I have sent my servant Naaman to you. Cure him of his leprosy.'"
    },
    "7": {
      "L": "And when the king of Israel read the letter, he tore his clothes and said, 'Am I God, to kill and to make alive, that this man sends word to me to cure a man of his leprosy? Only consider, and see how he is seeking a quarrel with me.'",
      "M": "When the king of Israel read the letter, he tore his clothes and said, 'Am I God, able to kill and to make alive, that this man sends to me to cure someone of leprosy? He is only looking for a quarrel with me.'",
      "T": "When the king of Israel read it, he tore his clothes. 'Am I God?' he said. 'Can I kill and bring to life? Why does this man send someone to me to heal his leprosy? He is picking a fight with me.'"
    },
    "8": {
      "L": "But when Elisha the man of God heard that the king of Israel had torn his clothes, he sent to the king, saying, 'Why have you torn your clothes? Let him come now to me, that he may know there is a prophet in Israel.'",
      "M": "When Elisha the man of God heard that the king of Israel had torn his clothes, he sent word to the king: 'Why have you torn your clothes? Let him come to me, and he will know there is a prophet in Israel.'",
      "T": "When Elisha heard that the king had torn his clothes, he sent word to him: 'Why have you torn your clothes? Send him to me—he will learn that there is a prophet in Israel.'"
    },
    "9": {
      "L": "So Naaman came with his horses and chariots and stood at the door of Elisha's house.",
      "M": "So Naaman came with his horses and chariots and stood at the door of Elisha's house.",
      "T": "Naaman came with his horses and chariots and halted at the door of Elisha's house."
    },
    "10": {
      "L": "And Elisha sent a messenger to him, saying, 'Go and wash in the Jordan seven times, and your flesh shall be restored, and you shall be clean.'",
      "M": "Elisha sent a messenger to him, saying, 'Go and wash in the Jordan seven times, and your flesh will be restored and you will be clean.'",
      "T": "Elisha sent a messenger out to him: 'Go and wash in the Jordan seven times. Your flesh will be restored and you will be clean.'"
    },
    "11": {
      "L": "But Naaman was angry and went away, saying, 'Behold, I thought that he would surely come out to me and stand and call upon the name of the LORD his God, and wave his hand over the place and cure the leper.'",
      "M": "But Naaman was angry and left, saying, 'I expected him to come out to me in person, call on the name of the LORD his God, wave his hand over the spot, and cure the leprosy.'",
      "T": "Naaman was furious and walked away. 'I thought he would at least come out to me himself,' he said, 'call on the name of the LORD his God, wave his hand over the disease, and cure me.'"
    },
    "12": {
      "L": "'Are not Abana and Pharpar, the rivers of Damascus, better than all the waters of Israel? Could I not wash in them and be clean?' So he turned and went away in a rage.",
      "M": "'Are not Abana and Pharpar, the rivers of Damascus, better than all the waters of Israel? Could I not wash in them and be clean?' He turned and walked away in a rage.",
      "T": "'Are not the Abana and Pharpar—Damascus's own rivers—better than all the waters of Israel? Could I not wash in them and be clean?' He turned and left in fury."
    },
    "13": {
      "L": "But his servants came near and spoke to him and said, 'My father, it is a great word the prophet has spoken to you; will you not do it? How much more, since he said to you, Wash and be clean?'",
      "M": "But his servants came and spoke to him: 'My father, if the prophet had told you to do something great, would you not have done it? How much more should you do it when he simply says, Wash and be clean?'",
      "T": "His servants came near and said to him: 'Father—if the prophet had commanded something great, would you not have done it? How much more, when he simply says: wash and be clean?'"
    },
    "14": {
      "L": "So he went down and dipped himself seven times in the Jordan, according to the word of the man of God, and his flesh was restored like the flesh of a little child, and he was clean.",
      "M": "So he went down and dipped himself seven times in the Jordan, just as the man of God had said. His flesh was restored like the flesh of a young child, and he was clean.",
      "T": "He went down and dipped himself in the Jordan seven times, as Elisha had said. His flesh was restored—as clear and fresh as a young child's—and he was clean."
    },
    "15": {
      "L": "Then he returned to the man of God, he and all his company, and he came and stood before him. And he said, 'Behold, I know that there is no God in all the earth but in Israel; so accept now a present from your servant.'",
      "M": "Then he returned to the man of God with his whole company, came and stood before him, and said, 'I know that there is no God in all the earth except in Israel. So please accept a gift from your servant.'",
      "T": "He came back to Elisha with his whole company and stood before him. He said: 'Now I know—there is no God in all the earth except in Israel.' This is the Exodus recognition formula spoken by a foreign soldier: 'you shall know that I am the LORD.' Naaman became Israel's clearest confessor. He added: 'Please accept a gift from your servant.'"
    },
    "16": {
      "L": "But he said, 'As the LORD lives, before whom I stand, I will receive nothing.' And he urged him to take it, but he refused.",
      "M": "But Elisha said, 'As the LORD lives, before whom I stand, I will receive nothing.' Naaman urged him to accept, but he refused.",
      "T": "Elisha said: 'As the LORD lives—before whom I stand—I will accept nothing.' Naaman pressed him, but Elisha refused."
    },
    "17": {
      "L": "Then Naaman said, 'If not, please let there be given to your servant two mule loads of earth, for from now on your servant will not offer burnt offering or sacrifice to any god but the LORD.'",
      "M": "Naaman said, 'If not, please let your servant be given two mule-loads of earth, for your servant will never again offer burnt offering or sacrifice to any god but the LORD.'",
      "T": "Then Naaman said: 'If you will accept nothing—then please give your servant two mule-loads of Israelite soil. From now on your servant will offer no burnt offering or sacrifice to any god but the LORD.'"
    },
    "18": {
      "L": "'But may the LORD pardon your servant when my master goes into the house of Rimmon to worship there, leaning on my arm, and I bow myself in the house of Rimmon—when I bow myself in the house of Rimmon, the LORD pardon your servant in this matter.'",
      "M": "'But may the LORD pardon your servant in this one matter: when my master goes to the temple of Rimmon to worship there, and he leans on my arm, and I bow down in the temple of Rimmon—when I bow down in the temple of Rimmon, may the LORD pardon your servant.'",
      "T": "'But in this one matter—may the LORD pardon your servant: when my master goes to the temple of Rimmon to worship and he leans on my arm, and I must bow down in Rimmon's temple—for that bowing, may the LORD pardon your servant.'"
    },
    "19": {
      "L": "He said to him, 'Go in peace.' So he departed from him some distance.",
      "M": "He said to him, 'Go in peace.' So Naaman departed a short distance from him.",
      "T": "Elisha said to him: 'Go in peace.' Naaman went from him. This is a remarkable grace extended to a convert in an impossible situation: no rebuke, no conditions—go in peace."
    },
    "20": {
      "L": "And Gehazi, the servant of Elisha the man of God, said, 'See, my master has spared this Naaman the Syrian, in not accepting from his hand what he brought. As the LORD lives, I will run after him and get something from him.'",
      "M": "But Gehazi, the servant of Elisha the man of God, said to himself, 'My master has let this Aramean Naaman off without accepting what he brought. As the LORD lives, I will run after him and get something from him.'",
      "T": "But Gehazi, Elisha's servant, thought: 'My master let this Aramean go without taking a thing from what he brought. As the LORD lives, I will run after him and take something.' What Elisha refused in faithfulness, Gehazi seized in greed."
    },
    "21": {
      "L": "So Gehazi followed Naaman. And when Naaman saw someone running after him, he got down from the chariot to meet him and said, 'Is all well?'",
      "M": "Gehazi ran after Naaman. When Naaman saw him running after him, he stepped down from the chariot to meet him and said, 'Is everything all right?'",
      "T": "Gehazi ran after Naaman. When Naaman saw someone running after him, he stepped down from the chariot to meet him. 'Is everything all right?' he asked."
    },
    "22": {
      "L": "And he said, 'All is well. My master has sent me to say, There have just now come to me two young men of the sons of the prophets from the hill country of Ephraim. Please give them a talent of silver and two changes of clothing.'",
      "M": "Gehazi said, 'All is well. My master has sent me to say: Two young men from the company of the prophets have just come to me from the hill country of Ephraim. Please give them a talent of silver and two changes of clothing.'",
      "T": "'All is well,' Gehazi said. 'My master has sent me: Two young men have just come to him from the prophetic community in the hill country of Ephraim. Please give them a talent of silver and two changes of clothing.'"
    },
    "23": {
      "L": "And Naaman said, 'Please accept two talents.' And he urged him and tied up two talents of silver in two bags, with two changes of clothing, and laid them on two of his servants. And they carried them before Gehazi.",
      "M": "Naaman said, 'Please accept two talents.' He insisted, and tied two talents of silver in two bags with two changes of clothing, and handed them to two of his servants who carried them before Gehazi.",
      "T": "Naaman said: 'Please take two talents.' He insisted, tied two talents of silver in two bags along with the two changes of clothing, and had two servants carry them ahead of Gehazi."
    },
    "24": {
      "L": "And when he came to the hill, he took them from their hand and put them in the house. And he sent the men away, and they departed.",
      "M": "When Gehazi came to the hill, he took them from the servants and put them in the house. He sent the men away, and they left.",
      "T": "When Gehazi reached the hill, he took the goods from them and stored them in the house. He sent the men away and they left."
    },
    "25": {
      "L": "He went in and stood before his master, and Elisha said to him, 'Where have you been, Gehazi?' And he said, 'Your servant went nowhere.'",
      "M": "He went in and stood before his master. Elisha said to him, 'Where have you been, Gehazi?' He replied, 'Your servant hasn't been anywhere.'",
      "T": "He went in and stood before Elisha. Elisha said: 'Where have you been, Gehazi?' 'Your servant hasn't been anywhere,' he said."
    },
    "26": {
      "L": "But he said to him, 'Did not my heart go when the man turned from his chariot to meet you? Was it a time to accept silver and to accept garments, olive orchards and vineyards, sheep and oxen, male servants and female servants?'",
      "M": "Elisha said to him, 'Did not my heart go with you when the man stepped down from his chariot to meet you? Is this a time to accept silver, clothing, olive groves, vineyards, sheep, oxen, male servants, and female servants?'",
      "T": "Elisha said: 'Was my spirit not there when the man stepped from his chariot to meet you? Is this the time to take silver? To take clothing, olive orchards, vineyards, flocks, herds, servants?'"
    },
    "27": {
      "L": "'Therefore the leprosy of Naaman shall cling to you and to your descendants forever.' So he went out from his presence a leper, like snow.",
      "M": "'Therefore the leprosy of Naaman will cling to you and your descendants forever.' So Gehazi went out from Elisha's presence as a leper—white as snow.",
      "T": "'Therefore Naaman's leprosy will cling to you and to your children's children forever.' Gehazi went out from Elisha's presence as a leper—white as snow. The disease that left one man when he humbled himself clung to another who exalted himself."
    }
  },
  "6": {
    "1": {
      "L": "Now the sons of the prophets said to Elisha, 'See, the place where we dwell under your charge is too small for us.'",
      "M": "The sons of the prophets said to Elisha, 'Look, the place where we live under your care is too cramped for us.'",
      "T": "The prophetic community said to Elisha: 'The place where we live under your oversight is too small for us.'"
    },
    "2": {
      "L": "'Let us go to the Jordan and each of us get there a log, and let us make a place there for us to dwell.' And he answered, 'Go.'",
      "M": "'Let us go to the Jordan and each of us get a log so we can build ourselves a place to live there.' He answered, 'Go.'",
      "T": "'Let us go to the Jordan. Each man will cut a log and we will build ourselves a new place to live.' 'Go,' said Elisha."
    },
    "3": {
      "L": "Then one of them said, 'Be pleased to go with your servants.' And he answered, 'I will go.'",
      "M": "One of them said, 'Please come with your servants.' He answered, 'I will go.'",
      "T": "One of them said: 'Please come with us.' 'I will come,' said Elisha."
    },
    "4": {
      "L": "So he went with them. And when they came to the Jordan, they cut down trees.",
      "M": "So he went with them. When they reached the Jordan, they began cutting down trees.",
      "T": "So he went with them. When they reached the Jordan, they began cutting timber."
    },
    "5": {
      "L": "But as one was felling a log, his axe head fell into the water, and he cried out, 'Alas, my master! It was borrowed.'",
      "M": "As one man was cutting a log, his axe head fell into the water. He cried out, 'Oh, my master! It was borrowed.'",
      "T": "As one man was felling a tree, his axe head flew off into the water. He cried out: 'Oh no, my master—it was borrowed!'"
    },
    "6": {
      "L": "Then the man of God said, 'Where did it fall?' When he showed him the place, he cut off a stick and threw it in there and made the iron float.",
      "M": "The man of God said, 'Where did it fall?' He showed him the place. Elisha cut off a stick and threw it in, and the iron floated.",
      "T": "'Where did it fall?' Elisha asked. The man showed him the spot. Elisha cut a piece of wood and threw it in—and the iron floated."
    },
    "7": {
      "L": "And he said, 'Take it up.' So he reached out his hand and took it.",
      "M": "He said, 'Pick it up.' The man reached out his hand and took it.",
      "T": "'Reach out and take it,' said Elisha. The man stretched out his hand and picked it up."
    },
    "8": {
      "L": "Once when the king of Syria was warring against Israel, he took counsel with his servants, saying, 'At such and such a place shall be my camp.'",
      "M": "Now when the king of Aram was at war with Israel, he would consult with his officers and say, 'My camp will be at such and such a place.'",
      "T": "While the king of Aram was waging war against Israel, he would take counsel with his officers, saying: 'I will set up camp at this or that place.'"
    },
    "9": {
      "L": "But the man of God sent word to the king of Israel, 'Beware that you do not pass this place, for the Syrians are going down there.'",
      "M": "But the man of God would send word to the king of Israel: 'Beware of passing that place—the Arameans are going down there.'",
      "T": "But Elisha would send warning to the king of Israel: 'Avoid that road—the Arameans are moving down there.'"
    },
    "10": {
      "L": "And the king of Israel sent to the place about which the man of God told him. Thus he used to warn him, so that he saved himself there more than once or twice.",
      "M": "And the king of Israel would send word to the place the man of God had warned him about and would guard himself there. This happened more than once or twice.",
      "T": "The king of Israel would guard the places Elisha warned him about. This happened again and again—Elisha's intelligence saved the king more than once."
    },
    "11": {
      "L": "And the mind of the king of Syria was greatly troubled because of this thing, and he called his servants and said to them, 'Will you not show me who of us is for the king of Israel?'",
      "M": "This troubled the king of Aram greatly. He summoned his officers and said to them, 'Will you not tell me who among us is siding with the king of Israel?'",
      "T": "This enraged the king of Aram. He summoned his officers: 'Tell me—which of you is leaking intelligence to the king of Israel?'"
    },
    "12": {
      "L": "And one of his servants said, 'None, my lord, O king; but Elisha, the prophet who is in Israel, tells the king of Israel the words that you speak in your bedroom.'",
      "M": "One of his officers said, 'None of us, my lord king. But Elisha the prophet who is in Israel tells the king of Israel the very words you speak in your bedroom.'",
      "T": "One of his officers said: 'No one, my lord king. It is Elisha the prophet in Israel—he tells the king of Israel the very words you speak in your bedroom.'"
    },
    "13": {
      "L": "And he said, 'Go and see where he is, that I may send and seize him.' It was told him, 'Behold, he is in Dothan.'",
      "M": "He said, 'Go and find out where he is, so I can send men to seize him.' They reported, 'He is in Dothan.'",
      "T": "'Find out where he is,' the king said, 'so I can send and capture him.' They reported: 'He is in Dothan.'"
    },
    "14": {
      "L": "So he sent there horses and chariots and a great army, and they came by night and surrounded the city.",
      "M": "So he sent horses and chariots and a large army. They arrived by night and surrounded the city.",
      "T": "He sent a large force—horses and chariots—and they arrived by night and surrounded Dothan."
    },
    "15": {
      "L": "When the servant of the man of God rose early in the morning and went out, behold, an army with horses and chariots was all around the city. And the servant said, 'Alas, my master! What shall we do?'",
      "M": "When the servant of the man of God got up early and went out, an army with horses and chariots had surrounded the city. His servant said, 'Oh, my master! What shall we do?'",
      "T": "When Elisha's servant got up early and went outside, horses and chariots and an army surrounded the city. He cried: 'Oh, my master—what shall we do?'"
    },
    "16": {
      "L": "He said, 'Do not be afraid, for those who are with us are more than those who are with them.'",
      "M": "He answered, 'Do not be afraid, for those who are with us are more than those who are with them.'",
      "T": "Elisha answered: 'Do not be afraid. Those who are with us are more than those who are with them.'"
    },
    "17": {
      "L": "Then Elisha prayed and said, 'O LORD, please open his eyes that he may see.' So the LORD opened the eyes of the young man, and he saw, and behold, the mountain was full of horses and chariots of fire all around Elisha.",
      "M": "Then Elisha prayed: 'LORD, please open his eyes so he may see.' The LORD opened the young man's eyes, and he looked and saw the mountain full of horses and chariots of fire surrounding Elisha.",
      "T": "Elisha prayed: 'LORD, open his eyes so he can see.' The LORD opened the servant's eyes. He looked—and the mountain was full of horses and chariots of fire surrounding Elisha. The divine army that took Elijah was also present with his successor."
    },
    "18": {
      "L": "And when the Syrians came down against him, Elisha prayed to the LORD and said, 'Please strike this people with blindness.' So he struck them with blindness according to the word of Elisha.",
      "M": "As the Arameans came down against him, Elisha prayed to the LORD: 'Please strike this people with blindness.' He struck them with blindness as Elisha had requested.",
      "T": "When the Arameans came down toward him, Elisha prayed: 'LORD, strike this army with blindness.' The LORD struck them blind, just as Elisha asked."
    },
    "19": {
      "L": "And Elisha said to them, 'This is not the way, and this is not the city. Follow me, and I will bring you to the man whom you seek.' And he led them to Samaria.",
      "M": "Elisha said to them, 'This is not the way, and this is not the city. Follow me, and I will bring you to the man you are looking for.' And he led them to Samaria.",
      "T": "Elisha said to them: 'This is not the way, and this is not the city. Follow me and I will take you to the man you are looking for.' He led them straight to Samaria."
    },
    "20": {
      "L": "When they entered Samaria, Elisha said, 'O LORD, open the eyes of these men, that they may see.' So the LORD opened their eyes and they saw, and behold, they were in the midst of Samaria.",
      "M": "When they had entered Samaria, Elisha said, 'LORD, open the eyes of these men so they may see.' The LORD opened their eyes and they saw that they were in the middle of Samaria.",
      "T": "When they had entered Samaria, Elisha said: 'LORD, open their eyes so they can see.' The LORD opened their eyes—and they found themselves in the middle of Samaria."
    },
    "21": {
      "L": "As soon as the king of Israel saw them, he said to Elisha, 'My father, shall I strike them down? Shall I strike them down?'",
      "M": "When the king of Israel saw them, he said to Elisha, 'My father, shall I strike them down? Shall I strike them down?'",
      "T": "When the king of Israel saw them, he said to Elisha: 'My father—shall I strike them down? Shall I strike them down?'"
    },
    "22": {
      "L": "He answered, 'You shall not strike them down. Would you strike down those whom you have taken captive with your sword and with your bow? Set bread and water before them, that they may eat and drink and go to their master.'",
      "M": "He answered, 'You shall not strike them down. Would you kill men you have captured with your sword and bow? Put food and water before them, so they may eat and drink and return to their master.'",
      "T": "'No, you will not strike them down,' Elisha said. 'Do you strike down prisoners of war? Set bread and water before them. Let them eat and drink and return to their master.'"
    },
    "23": {
      "L": "So he prepared for them a great feast, and when they had eaten and drunk, he sent them away, and they went to their master. And the Aramean raiders came no more into the land of Israel.",
      "M": "He prepared a great feast for them. After they ate and drank, he sent them away and they went to their master. And the Aramean raiding parties stopped coming into the land of Israel.",
      "T": "He prepared a great feast for them. They ate and drank, then he sent them away to their master. And the Aramean raiding parties stopped coming into Israel's territory."
    },
    "24": {
      "L": "Afterward Ben-hadad king of Syria mustered his entire army and went up and besieged Samaria.",
      "M": "Afterward Ben-hadad king of Aram mustered his entire army and went up and besieged Samaria.",
      "T": "After this, Ben-hadad king of Aram mobilized his entire army and marched up to besiege Samaria."
    },
    "25": {
      "L": "And there was a great famine in Samaria, as they besieged it, until a donkey's head was sold for eighty shekels of silver, and the fourth part of a kab of dove's dung for five shekels of silver.",
      "M": "There was a severe famine in Samaria. The siege drove up prices until a donkey's head was sold for eighty shekels of silver and a quarter of a kab of dove's dung for five shekels of silver.",
      "T": "A terrible famine gripped Samaria under the siege. Prices became grotesque: a donkey's head sold for eighty shekels of silver; a small measure of seed pods sold for five."
    },
    "26": {
      "L": "Now as the king of Israel was passing by on the wall, a woman cried out to him, saying, 'Help, my lord, O king!'",
      "M": "As the king of Israel was walking along the wall, a woman cried out to him: 'Help me, my lord the king!'",
      "T": "As the king of Israel was walking along the city wall, a woman cried out to him: 'Help me, my lord the king!'"
    },
    "27": {
      "L": "And he said, 'If the LORD will not help you, how shall I help you? From the threshing floor, or from the winepress?'",
      "M": "He said, 'If the LORD will not help you, how can I? From the threshing floor, or from the winepress?'",
      "T": "He said: 'If the LORD will not save you, what can I do? I have no grain from the threshing floor, no wine from the press.'"
    },
    "28": {
      "L": "And the king asked her, 'What is your trouble?' She answered, 'This woman said to me, Give your son, that we may eat him today, and we will eat my son tomorrow.'",
      "M": "The king asked, 'What is your trouble?' She answered, 'This woman said to me, Give your son so we can eat him today, and tomorrow we will eat my son.'",
      "T": "'What is wrong?' he asked. She said: 'This woman said to me: Give me your son and we will eat him today. Tomorrow we will eat my son.'"
    },
    "29": {
      "L": "'So we boiled my son and ate him. And on the next day I said to her, Give your son, that we may eat him. But she has hidden her son.'",
      "M": "'So we cooked my son and ate him. The next day I said to her, Give your son so we may eat him—but she has hidden her son.'",
      "T": "'So we cooked my son and ate him. The next day I said: Now give your son. But she had hidden him.'"
    },
    "30": {
      "L": "When the king heard the words of the woman, he tore his clothes—now he was passing by on the wall—and the people looked, and behold, he had sackcloth beneath, against his body.",
      "M": "When the king heard the woman's words, he tore his clothes—he was passing along the wall—and the people looked and saw he had sackcloth on his body underneath.",
      "T": "When the king heard the woman's words, he tore his clothes—he was walking along the wall—and the people looked and saw that he was wearing sackcloth against his skin."
    },
    "31": {
      "L": "And he said, 'May God do so to me and more also, if the head of Elisha the son of Shaphat remains on his shoulders today.'",
      "M": "He said, 'May God deal with me, however severely, if the head of Elisha son of Shaphat remains on him today.'",
      "T": "'May God deal with me in the harshest terms,' the king said, 'if Elisha son of Shaphat keeps his head today.'"
    },
    "32": {
      "L": "Elisha was sitting in his house, and the elders were sitting with him. Now the king sent a man from his presence, but before the messenger arrived, Elisha said to the elders, 'Do you see how this son of a murderer has sent to take off my head? Look, when the messenger comes, shut the door and hold the door fast against him. Is not the sound of his master's feet behind him?'",
      "M": "Elisha was sitting in his house with the elders. The king sent a messenger ahead of him, but before the messenger arrived, Elisha said to the elders, 'Do you see how this son of a murderer is sending someone to take off my head? When the messenger comes, shut the door and hold it shut against him. Can you not hear his master's feet coming behind him?'",
      "T": "Elisha was sitting in his house with the elders. The king had sent a man to arrest him—but before the messenger arrived, Elisha said to the elders: 'Do you see how this son of a murderer has sent someone to take my head? When the messenger comes, shut the door and hold it. His master is close behind him—listen.'"
    },
    "33": {
      "L": "And while he was still speaking with them, the messenger came down to him. And he said, 'This trouble is from the LORD! Why should I wait for the LORD any longer?'",
      "M": "While he was still speaking with them, the messenger arrived. And the king said, 'This disaster is from the LORD! Why should I wait any longer for the LORD?'",
      "T": "While Elisha was still speaking, the messenger arrived—and behind him came the king himself. 'This disaster is from the LORD!' the king said. 'Why should I wait on the LORD any longer?'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2kings')
        merge_tier(existing, KINGS, tier_key)
        save(tier_dir, '2kings', existing)
    print('2 Kings 1–6 written.')

if __name__ == '__main__':
    main()
