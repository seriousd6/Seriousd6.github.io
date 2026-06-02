"""
MKT Judges chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-judges-13-18.py

Covers: Samson's birth announcement — the angel of the LORD to Manoah's wife (ch. 13);
Samson's Philistine marriage, the lion and the riddle (ch. 14); the fox-firebrand revenge,
the jawbone of a donkey, twenty years judging (ch. 15); Delilah, the secret of Samson's
strength, his capture and death in the temple of Dagon (ch. 16); Micah's household shrine
in Ephraim (ch. 17); the Danites steal Micah's idols and priest, destroy Laish, found Dan
(ch. 18).

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps) in L/M; "the LORD" in T — consistent with all prior OT
  scripts. The divine personal name is retained as LORD throughout.
- H430 (אֱלֹהִים): "God" all tiers when singular divine; "gods" when clearly pagan (17:5
  "house of gods"; 18:24 "my gods"). Note irony in 17:13 where Micah uses "LORD" and
  "God" language about an idol-shrine — the text does not correct him; T surfaces the
  contradiction.
- H7307 (רוּחַ): "Spirit" (capitalized) in every occurrence of the formula "the Spirit of
  the LORD came upon/rushed upon" (13:25, 14:6, 14:19, 15:14) — these are prophetic/military
  anointing events; standard formula matching Gideon (6:34) and Jephthah (11:29) in the
  prior script. In 15:19 "his spirit came again" — lowercase, referring to Samson's physical
  reviving, not a fresh anointing.
- H5139 (נָזִיר): "Nazirite" all tiers — a person set apart to God by vow from Numbers 6:
  no razor, no wine or strong drink, no contact with a corpse. The narrative irony is that
  Samson violates two of the three (corpse contact in 14:9 with the lion honey; promiscuity
  throughout) before Delilah causes the third violation. T surfaces this where exegetically
  significant.
- H4397 (מַלְאָךְ): "angel" in L/M; T uses "angel of the LORD" / "the messenger" as context
  allows. The angel of the LORD in ch. 13 is a theophanic figure — pre-incarnate divine
  messenger; T notes the ascending-in-flame as the divine departure marker.
- H6383 (פִּלְאִי): 13:18 — the angel's name is "Wonderful / Incomprehensible." L renders
  "wonderful" (word-for-word); M "beyond understanding"; T explicitly notes the connection
  to Isaiah 9:6 (פֶּלֶא, same root), where "Wonderful Counselor" is a name for the Coming
  One. The angel refuses to name himself but the word chosen is a title.
- H1712 (דָּגוֹן): "Dagon" all tiers — the Philistine deity (associated with grain or fish);
  the irony in ch. 16 is that Dagon's worshippers boast he has delivered Samson, but the
  final act is Samson's — and the LORD's — not Dagon's.
- H646 (אֵפוֹד): "ephod" all tiers — in ch. 17–18 this is a cult object in an unauthorized
  shrine, not the high priestly ephod; T notes the illegitimacy.
- H8655 (תְּרָפִים): "teraphim" all tiers — household divination idols; T glosses as
  "household idols" in parenthetical where clarity requires.
- H6459 (פֶּסֶל): "carved image" L; "carved idol" M/T.
- H4541 (מַסֵּכָה): "molten image" L; "cast idol" M; "cast metal idol" T.
- H5315 (נֶפֶשׁ): 16:16 "his soul was vexed unto death" — H7114 (shortened soul/distress) +
  H4191 (death) = "worn down to the point of death." L "his soul was worn out to death";
  M "he was worn down to death"; T "he was exhausted to the point of death."
- H4960 (מִשְׁתֶּה): "feast" all tiers — the wedding feast of ch. 14 is a seven-day
  drinking banquet; the word implies celebration with wine, fitting the Timnah context.
- 13:18 note: The angel's name being "Wonderful" (פִּלְאִי) anticipates the divine
  name-theology of the Hebrew Bible. That the angel ascends in the sacrificial flame
  (13:20) echoes Elijah's angel and theophanic fire traditions. T surfaces the theological
  freight.
- 14:9 note: Samson's taking honey from the lion's carcass is a Nazirite violation (contact
  with a corpse, Num. 6:6). He conceals it from his parents. This begins the pattern of
  Samson's self-destruction through hidden compromise. T notes this once (at v9).
- 16:20 note: "He did not know that the LORD had departed from him" — one of the most
  theologically weighty verses in Judges. The divine presence does not loudly withdraw; it
  simply is no longer there. T renders with appropriate weight.
- 16:28 note: Samson's prayer is motivated by personal vengeance ("for my two eyes"), not
  covenant faithfulness. Yet God answers it. T preserves the ambiguity — Samson is used
  by God even in his flawed motivations.
- 17:6 / 18:1 note: The refrain "In those days there was no king in Israel; everyone did
  what was right in his own eyes" frames chs. 17–21 as the moral abyss of the period.
  T renders with the full weight of the structural indictment.
- 18:30 note: "Jonathan son of Gershom son of Manasseh" — the Hebrew scribes suspended a
  letter (nun) to write Manasseh (מנשה) where the original was Moses (משה), to protect
  Moses' reputation from the shame of a grandson becoming an idol-priest. T notes this
  textual decision.
- Jotham's fable style from ch. 9 (prior script) used line breaks in T; that chapter is
  not in this range. Samson's riddle (14:14) and boast (15:16) receive slight poetic
  treatment in T to honor their verse-like quality.
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

JUDGES = {
  "13": {
    "1": {
      "L": "And the children of Israel did evil again in the sight of the LORD, and the LORD delivered them into the hand of the Philistines forty years.",
      "M": "The people of Israel again did what was evil in the sight of the LORD, and the LORD gave them into the hand of the Philistines for forty years.",
      "T": "Israel fell back into evil—again—in the LORD's sight. And the LORD handed them over to the Philistines for forty years."
    },
    "2": {
      "L": "And there was a certain man of Zorah, of the family of the Danites, whose name was Manoah; and his wife was barren and had borne no children.",
      "M": "There was a man named Manoah, from Zorah, from the clan of the Danites, whose wife was barren and had borne no children.",
      "T": "In the town of Zorah there lived a man named Manoah, from the tribe of Dan. His wife was barren—she had never conceived."
    },
    "3": {
      "L": "And the angel of the LORD appeared to the woman and said to her, 'Behold, you are barren and have not borne; but you shall conceive and bear a son.'",
      "M": "The angel of the LORD appeared to the woman and said to her, 'Look, you are barren and have not borne a child, but you shall conceive and bear a son.'",
      "T": "The angel of the LORD appeared to the woman and said: 'You are barren—you have never conceived—but you will conceive and give birth to a son.'"
    },
    "4": {
      "L": "Now therefore beware and drink not wine nor strong drink, and eat not any unclean thing.",
      "M": "Therefore be careful not to drink wine or strong drink, and eat nothing unclean.",
      "T": "From this moment: drink no wine, no beer, eat nothing ritually unclean."
    },
    "5": {
      "L": "For behold, you shall conceive and bear a son; and no razor shall come upon his head, for the child shall be a Nazirite to God from the womb; and he shall begin to deliver Israel from the hand of the Philistines.",
      "M": "For you shall conceive and bear a son. No razor shall touch his head, for the child will be a Nazirite to God from the womb. He will begin to deliver Israel from the hand of the Philistines.",
      "T": "You will conceive and give birth to a son. No razor must ever touch his head, because from the womb this child will be set apart to God as a Nazirite. He will be the one who begins to rescue Israel from the Philistines."
    },
    "6": {
      "L": "Then the woman came and told her husband, saying, 'A man of God came to me, and his countenance was like the countenance of the angel of God, very awesome; but I did not ask him where he was from, nor did he tell me his name.'",
      "M": "The woman came and told her husband, 'A man of God came to me, and his appearance was like the appearance of the angel of God—very awesome. I did not ask him where he came from, and he did not tell me his name.'",
      "T": "The woman hurried to tell her husband: 'A man of God came to me. His face was like the face of an angel—terrifying in its majesty. I didn't think to ask where he came from, and he didn't tell me his name.'"
    },
    "7": {
      "L": "But he said to me, 'Behold, you shall conceive and bear a son; now drink no wine nor strong drink, and eat nothing unclean, for the child shall be a Nazirite to God from the womb to the day of his death.'",
      "M": "But he said to me, 'You shall conceive and bear a son. Now drink no wine or strong drink, and eat nothing unclean, for the child will be a Nazirite to God from the womb to the day of his death.'",
      "T": "But he told me: 'You will conceive and bear a son. From now on drink no wine, no beer, eat nothing unclean—because this child will be a Nazirite to God from the moment he is conceived until the day he dies.'"
    },
    "8": {
      "L": "Then Manoah prayed to the LORD and said, 'O Lord, please let the man of God whom you sent come again to us and teach us what we are to do with the child who will be born.'",
      "M": "Then Manoah prayed to the LORD and said, 'O Lord, please let the man of God you sent come again to us and teach us what to do for the child who will be born.'",
      "T": "Manoah prayed to the LORD: 'Lord, please—send the man of God back to us. Let him teach us how to raise the child who is coming.'"
    },
    "9": {
      "L": "And God hearkened to the voice of Manoah, and the angel of God came again to the woman while she sat in the field, but Manoah her husband was not with her.",
      "M": "And God listened to the voice of Manoah, and the angel of God came again to the woman as she sat in the field, though Manoah her husband was not with her.",
      "T": "God heard Manoah's prayer. The angel of God returned to the woman while she was sitting alone in the field—Manoah was not with her."
    },
    "10": {
      "L": "And the woman quickly arose and ran and told her husband and said to him, 'Behold, the man who came to me the other day has appeared to me.'",
      "M": "The woman quickly arose and ran and told her husband, 'The man who came to me that other day has appeared to me!'",
      "T": "She ran to find Manoah and said, 'He's back—the man who appeared to me before!'"
    },
    "11": {
      "L": "Then Manoah arose and followed his wife and came to the man and said to him, 'Are you the man who spoke to the woman?' And he said, 'I am.'",
      "M": "Manoah arose and followed his wife to the man and said to him, 'Are you the man who spoke to this woman?' He said, 'I am.'",
      "T": "Manoah got up and followed his wife to the man and asked, 'Are you the one who spoke to my wife?' 'I am,' he said."
    },
    "12": {
      "L": "And Manoah said, 'Now when your words come to pass, what is to be the child's manner of life and his work?'",
      "M": "And Manoah said, 'Now when your words come true, what shall be the child's manner of life and his work?'",
      "T": "Manoah asked, 'When your word comes true—what are the rules for raising this child? How should we rear him?'"
    },
    "13": {
      "L": "And the angel of the LORD said to Manoah, 'All that I said to the woman let her beware of.'",
      "M": "The angel of the LORD said to Manoah, 'Let her beware of everything I said to the woman.'",
      "T": "The angel of the LORD answered Manoah: 'Everything I said to the woman, she must observe.'"
    },
    "14": {
      "L": "She may not eat of anything that comes from the vine, nor drink wine or strong drink, nor eat anything unclean. All that I commanded her let her observe.",
      "M": "She may eat nothing that comes from the vine, and she shall drink no wine or strong drink, and she shall eat nothing unclean. Let her observe everything I commanded her.",
      "T": "She must eat nothing from the vine, drink no wine or beer, and eat nothing ritually unclean. Let her keep every one of my commands."
    },
    "15": {
      "L": "And Manoah said to the angel of the LORD, 'Please let us detain you while we prepare a young goat for you.'",
      "M": "And Manoah said to the angel of the LORD, 'Please stay while we prepare a young goat for you.'",
      "T": "Manoah said to the angel of the LORD, 'Let us prepare a young goat for you—please, stay.'"
    },
    "16": {
      "L": "And the angel of the LORD said to Manoah, 'Though you detain me, I will not eat of your bread; but if you make a burnt offering, offer it to the LORD.' For Manoah did not know that he was the angel of the LORD.",
      "M": "The angel of the LORD said to Manoah, 'Though you detain me, I will not eat your food; but if you prepare a burnt offering, offer it to the LORD.' For Manoah did not know that he was the angel of the LORD.",
      "T": "'Even if you kept me here, I would not eat your food,' the angel replied. 'But if you want to make a burnt offering, offer it to the LORD.' Manoah did not yet realize he was speaking with the angel of the LORD."
    },
    "17": {
      "L": "And Manoah said to the angel of the LORD, 'What is your name, so that when your words come to pass we may honor you?'",
      "M": "And Manoah said to the angel of the LORD, 'What is your name, so that when your words come true we may honor you?'",
      "T": "Manoah asked the angel, 'What is your name? When your word comes true we want to honor you.'"
    },
    "18": {
      "L": "And the angel of the LORD said to him, 'Why do you ask my name, seeing it is wonderful?'",
      "M": "The angel of the LORD said to him, 'Why do you ask my name? It is beyond understanding.'",
      "T": "The angel answered: 'Why ask my name? It is Wonderful—beyond all telling.' The word is the same root as the name in Isaiah 9:6: Wonderful Counselor. The angel keeps his name hidden, but the word he uses is itself a title."
    },
    "19": {
      "L": "So Manoah took a kid and the grain offering and offered it on the rock to the LORD, and the angel did wondrously while Manoah and his wife looked on.",
      "M": "So Manoah took the young goat and the grain offering and offered them on the rock to the LORD, and the angel worked a wonder as Manoah and his wife watched.",
      "T": "Manoah took the young goat and the grain offering and laid them on the rock as a sacrifice to the LORD. And the angel did something wondrous—as Manoah and his wife looked on."
    },
    "20": {
      "L": "For it came to pass, when the flame went up from the altar toward heaven, that the angel of the LORD ascended in the flame of the altar, and Manoah and his wife looked on and fell on their faces to the ground.",
      "M": "When the flame went up toward heaven from the altar, the angel of the LORD ascended in the flame. Manoah and his wife watched and fell facedown to the ground.",
      "T": "As the flame leapt upward from the altar toward heaven, the angel of the LORD rose with it—ascending in the fire. Manoah and his wife fell with their faces to the ground."
    },
    "21": {
      "L": "And the angel of the LORD appeared no more to Manoah and his wife. Then Manoah knew that he was the angel of the LORD.",
      "M": "The angel of the LORD did not appear again to Manoah and his wife. Then Manoah realized that he had been the angel of the LORD.",
      "T": "The angel of the LORD never appeared to them again. And Manoah finally understood: he had been the angel of the LORD."
    },
    "22": {
      "L": "And Manoah said to his wife, 'We shall surely die, for we have seen God.'",
      "M": "Manoah said to his wife, 'We are certainly going to die, for we have seen God.'",
      "T": "Manoah was terrified: 'We are going to die—we have seen God!'"
    },
    "23": {
      "L": "But his wife said to him, 'If the LORD were pleased to kill us, he would not have accepted the burnt offering and the grain offering from our hands, nor shown us all these things, nor at this time announced to us such things as these.'",
      "M": "But his wife said to him, 'If the LORD had wanted to kill us, he would not have accepted the burnt offering and the grain offering from our hands, nor would he have shown us all these things or at this time announced to us such things.'",
      "T": "His wife steadied him: 'Think. If the LORD wanted to kill us, he would not have accepted our offering, nor shown us all this—and he certainly would not have spoken this promise to us.'"
    },
    "24": {
      "L": "And the woman bore a son and called his name Samson. And the child grew, and the LORD blessed him.",
      "M": "The woman bore a son and named him Samson. The child grew, and the LORD blessed him.",
      "T": "The woman gave birth to a son and named him Samson. He grew, and the LORD was with him."
    },
    "25": {
      "L": "And the Spirit of the LORD began to move him at times in the camp of Dan, between Zorah and Eshtaol.",
      "M": "And the Spirit of the LORD began to stir him at times in the camp of Dan, between Zorah and Eshtaol.",
      "T": "The Spirit of the LORD began to stir in him at intervals—at the camp of Dan between Zorah and Eshtaol. A flame was being kindled."
    }
  },
  "14": {
    "1": {
      "L": "And Samson went down to Timnah and saw a woman, one of the daughters of the Philistines.",
      "M": "Samson went down to Timnah and saw a Philistine woman there.",
      "T": "Samson went down to Timnah and saw a Philistine woman living there."
    },
    "2": {
      "L": "And he came up and told his father and his mother, 'I have seen a woman in Timnah, one of the daughters of the Philistines; now get her for me as a wife.'",
      "M": "He came back and told his father and mother, 'I have seen a woman in Timnah—a Philistine woman. Now get her for me as my wife.'",
      "T": "He came home and told his parents, 'I saw a Philistine woman in Timnah. Get her for me—I want to marry her.'"
    },
    "3": {
      "L": "Then his father and mother said to him, 'Is there no woman among the daughters of your relatives, or among all our people, that you must go to take a wife from the uncircumcised Philistines?' But Samson said to his father, 'Get her for me, for she is right in my eyes.'",
      "M": "His father and mother said to him, 'Is there not a woman among your relatives, or among all our people, that you should go and take a wife from the uncircumcised Philistines?' But Samson said to his father, 'Get her for me, for she pleases me well.'",
      "T": "His parents objected: 'Isn't there a woman among our own people—your own kin—that you have to marry a Philistine? The uncircumcised!' But Samson answered his father: 'Get her. She is the one I want.'"
    },
    "4": {
      "L": "His father and his mother did not know that it was of the LORD, for he was seeking an occasion against the Philistines. At that time the Philistines had dominion over Israel.",
      "M": "His father and mother did not know that this was from the LORD, who was seeking an occasion against the Philistines. At that time the Philistines were ruling over Israel.",
      "T": "His parents did not know that this was the LORD's doing—God was using Samson's desire as a pretext to move against the Philistines, who at that time ruled over Israel."
    },
    "5": {
      "L": "Then Samson went down with his father and his mother to Timnah. And when he came to the vineyards of Timnah, behold, a young lion came roaring toward him.",
      "M": "Samson went down with his father and mother to Timnah. As they came to the vineyards of Timnah, a young lion came roaring toward him.",
      "T": "Samson traveled with his parents toward Timnah. As he came into the Timnah vineyards, a full-grown young lion suddenly roared toward him."
    },
    "6": {
      "L": "And the Spirit of the LORD came mightily upon him, and he tore it apart with his bare hands as one tears a young goat. But he did not tell his father or his mother what he had done.",
      "M": "The Spirit of the LORD rushed upon him, and he tore the lion apart with his bare hands as one tears a young goat. He told neither his father nor his mother what he had done.",
      "T": "The Spirit of the LORD rushed upon him with power, and he tore the lion apart with his bare hands as if it were a young goat. He had no weapon. He told neither his father nor his mother what had happened."
    },
    "7": {
      "L": "Then he went down and spoke with the woman, and she pleased Samson well.",
      "M": "He went down and talked with the woman, and she pleased Samson.",
      "T": "He went down and spoke with the woman—and she pleased him."
    },
    "8": {
      "L": "After some time he returned to take her, and he turned aside to look at the carcass of the lion, and behold, there was a swarm of bees and honey in the carcass.",
      "M": "After some time he returned to take her as his wife. He turned aside to look at the carcass of the lion, and there was a swarm of bees and honey in the lion's carcass.",
      "T": "Later, when he went back to marry the woman, he detoured to look at the lion's carcass—and found a swarm of bees inside it, and honey."
    },
    "9": {
      "L": "He scooped it out into his hands and went along eating, and he came to his father and mother and gave some to them, and they ate. But he did not tell them that he had taken the honey from the carcass of the lion.",
      "M": "He scraped the honey into his hands and ate as he went. He brought some to his father and mother, and they also ate. But he did not tell them that he had taken the honey from the lion's carcass.",
      "T": "He scooped the honey out and ate it as he walked, and brought some to his parents. They ate too—but he said nothing about where it came from. He had touched a corpse, a violation of his Nazirite vow, and he kept that hidden."
    },
    "10": {
      "L": "So his father went down to the woman, and Samson made a feast there, for so the young men customarily did.",
      "M": "So his father went down to the woman, and Samson made a feast there, as was the custom for young men.",
      "T": "His father went to the woman's family to arrange the marriage, and Samson prepared a seven-day feast—the customary wedding celebration."
    },
    "11": {
      "L": "And when the people saw him, they brought thirty companions to be with him.",
      "M": "When the Philistines saw him, they brought thirty companions to accompany him.",
      "T": "When the local Philistines saw him, they brought thirty young men to be his wedding companions."
    },
    "12": {
      "L": "And Samson said to them, 'Let me now put forth a riddle to you. If you can solve it for me within the seven days of the feast and find it out, I will give you thirty linen garments and thirty changes of clothing.'",
      "M": "Samson said to them, 'Let me put a riddle to you. If you can solve it within the seven days of the feast, I will give you thirty linen garments and thirty sets of clothing.'",
      "T": "Samson said to them, 'Let me give you a riddle. Solve it within the seven days of the feast, and I'll give you thirty fine shirts and thirty sets of clothes.'"
    },
    "13": {
      "L": "But if you cannot tell me the answer, then you shall give me thirty linen garments and thirty changes of clothing.' And they said to him, 'Put forth your riddle, so we may hear it.'",
      "M": "But if you cannot tell me the answer, you shall give me thirty linen garments and thirty sets of clothing.' They said, 'Tell us your riddle—let's hear it.'",
      "T": "But if you cannot solve it, you owe me thirty shirts and thirty sets of clothes.' They said, 'Let's hear it.'"
    },
    "14": {
      "L": "And he said to them, 'Out of the eater came food, and out of the strong came sweetness.' And they could not explain the riddle in three days.",
      "M": "He said to them, 'Out of the eater came food, and out of the strong came sweetness.' They could not solve the riddle in three days.",
      "T": "He said: 'Out of the eater came food;\nout of the strong came sweetness.'\nThey were stumped for three days."
    },
    "15": {
      "L": "On the seventh day they said to Samson's wife, 'Entice your husband to tell us the riddle, or we will burn you and your father's house with fire. Have you called us here to make us poor?'",
      "M": "On the seventh day they said to Samson's wife, 'Coax your husband into telling us the riddle, or we will burn you and your father's house. Did you invite us here to make us poor?'",
      "T": "On the seventh day they turned to Samson's wife with a threat: 'Get the answer from your husband, or we will burn you and your father's house. Did you invite us to your wedding to strip us of our money?'"
    },
    "16": {
      "L": "And Samson's wife wept before him and said, 'You only hate me and do not love me. You have put forth a riddle to my people and have not told me the answer.' And he said to her, 'Behold, I have not told my father or my mother; why should I tell you?'",
      "M": "And Samson's wife wept before him and said, 'You hate me and don't love me. You told my people a riddle but haven't told me the answer.' He said, 'Look, I haven't even told my father or mother—why should I tell you?'",
      "T": "Samson's wife wept in front of him: 'You hate me. If you loved me, you'd tell me.' She kept at it. 'You gave my people a riddle you haven't shared with me!' He said, 'I haven't told my own parents—why would I tell you?'"
    },
    "17": {
      "L": "She wept before him for all seven days while their feast lasted, and on the seventh day he told her, because she pressed him hard. Then she told the riddle to her people.",
      "M": "She wept before him for all seven days of the feast, and on the seventh day he told her, because she pressed him so hard. She then told the riddle to her countrymen.",
      "T": "She wept the entire seven days. He held out until the seventh day—then he cracked under her pressure and told her. She immediately passed the answer to her people."
    },
    "18": {
      "L": "And the men of the city said to him before sunset on the seventh day, 'What is sweeter than honey? What is stronger than a lion?' And he said to them, 'If you had not plowed with my heifer, you would not have found out my riddle.'",
      "M": "The men of the city said to him before sunset on the seventh day, 'What is sweeter than honey? What is stronger than a lion?' He said to them, 'If you had not plowed with my heifer, you would not have solved my riddle.'",
      "T": "Before the sun set on the seventh day, the men answered: 'What is sweeter than honey? What is stronger than a lion?' Samson said bitterly: 'If you had not plowed with my heifer, you never would have cracked my riddle.'"
    },
    "19": {
      "L": "And the Spirit of the LORD came upon him, and he went down to Ashkelon and struck down thirty men of the city and took their garments, and gave the changes of clothing to those who had solved the riddle. And his anger burned, and he went up to his father's house.",
      "M": "The Spirit of the LORD rushed upon him, and he went down to Ashkelon and struck down thirty men of the city and took their clothing, and gave the garments to those who had solved the riddle. Burning with anger, he went up to his father's house.",
      "T": "The Spirit of the LORD rushed upon him. He went to Ashkelon, killed thirty men, stripped their clothing, and brought the garments back to pay the debt. His anger blazing, he went home to his father—without his bride."
    },
    "20": {
      "L": "But Samson's wife was given to his companion who had been his best man.",
      "M": "But Samson's wife was given to his companion, who had been his wedding companion.",
      "T": "While he was gone, Samson's wife was given to the man who had been his best man."
    }
  },
  "15": {
    "1": {
      "L": "But after some time, in the days of wheat harvest, Samson visited his wife with a young goat. He said, 'I will go into my wife in her room.' But her father would not allow him to enter.",
      "M": "After some time, during the wheat harvest, Samson visited his wife with a young goat. He said, 'I will go to my wife in her room.' But her father would not let him in.",
      "T": "Some time later, during wheat harvest, Samson went to visit his wife, bringing a young goat as a gift. 'I'm going to my wife's room,' he said. But her father blocked the way."
    },
    "2": {
      "L": "Her father said, 'I really thought you had come to hate her, so I gave her to your companion. Is not her younger sister more beautiful than she? Please take her instead.'",
      "M": "Her father said, 'I was sure you completely hated her, so I gave her to your companion. Isn't her younger sister more beautiful? Take her instead.'",
      "T": "Her father said, 'I was certain you hated her—so I gave her to your companion. Her younger sister is even prettier. Take her.'"
    },
    "3": {
      "L": "And Samson said to them, 'This time I will be blameless before the Philistines when I do them harm.'",
      "M": "Samson said to them, 'This time I will be blameless in what I do to the Philistines.'",
      "T": "'Whatever I do to the Philistines now, I'm in the right,' Samson said. 'They've given me every reason.'"
    },
    "4": {
      "L": "And Samson went and caught three hundred foxes and took torches, and he turned them tail to tail and put a torch between each pair of tails.",
      "M": "Samson went and caught three hundred foxes, tied them in pairs tail to tail, and fastened a torch between each pair of tails.",
      "T": "Samson caught three hundred foxes, paired them tail to tail, and fixed a burning torch between each pair."
    },
    "5": {
      "L": "And when he had set the torches on fire, he released them into the standing grain of the Philistines and burned up the grain sheaves and the standing grain, along with the vineyards and olive groves.",
      "M": "He set the torches on fire and released the foxes into the Philistine grain fields, burning up the harvested grain, the standing grain, the vineyards, and the olive groves.",
      "T": "He set the torches ablaze and released the foxes into the Philistine fields. Fire swept through everything: the stacked sheaves, the standing crops, the vineyards, the olive trees."
    },
    "6": {
      "L": "Then the Philistines said, 'Who has done this?' And they answered, 'Samson, the son-in-law of the Timnite, because he took his wife and gave her to his companion.' And the Philistines came up and burned her and her father.",
      "M": "The Philistines asked, 'Who did this?' They were told, 'Samson, the son-in-law of the Timnite, because his father-in-law took his wife and gave her to another man.' So the Philistines came up and burned her and her father.",
      "T": "When the Philistines learned who had done it and why, they came and burned the woman and her father. The woman caught in the middle of a feud paid the price."
    },
    "7": {
      "L": "And Samson said to them, 'If this is what you do, I will surely be avenged against you, and after that I will stop.'",
      "M": "Samson said to them, 'If this is what you do, I will surely be avenged against you, and only then will I stop.'",
      "T": "'Since you did this,' Samson said, 'I will not stop until I have had my revenge—and then I'm done.'"
    },
    "8": {
      "L": "And he struck them hip and thigh with a great slaughter, and then he went down and lived in the cleft of the rock of Etam.",
      "M": "He attacked them and struck them hip and thigh with a great slaughter. Then he went down and stayed in the cave of the rock of Etam.",
      "T": "He attacked the Philistines with savage force—hip and thigh, a massive slaughter. Then he withdrew and settled in the cave at the rock of Etam."
    },
    "9": {
      "L": "Then the Philistines went up and camped in Judah and spread out at Lehi.",
      "M": "The Philistines went up and camped in Judah and raided Lehi.",
      "T": "The Philistines responded by invading Judah and deploying their forces at Lehi."
    },
    "10": {
      "L": "And the men of Judah said, 'Why have you come up against us?' And they answered, 'We have come to bind Samson, to do to him as he has done to us.'",
      "M": "The men of Judah said, 'Why have you come up against us?' They answered, 'We have come to bind Samson, to do to him as he did to us.'",
      "T": "The men of Judah asked, 'Why have you invaded us?' They answered, 'We've come for Samson—to give him what he gave us.'"
    },
    "11": {
      "L": "Then three thousand men of Judah went down to the cave of the rock of Etam and said to Samson, 'Do you not know that the Philistines rule over us? What then is this that you have done to us?' And he said to them, 'As they did to me, so I have done to them.'",
      "M": "Then three thousand men of Judah went down to the cave at Etam and said to Samson, 'Don't you know that the Philistines rule over us? What is this you have done to us?' He said, 'As they did to me, so I did to them.'",
      "T": "Three thousand men of Judah went down to the rock of Etam. 'Don't you know the Philistines are our rulers?' they said. 'What have you done to us?' Samson answered: 'I gave them exactly what they gave me.'"
    },
    "12": {
      "L": "And they said to him, 'We have come to bind you and hand you over to the Philistines.' And Samson said to them, 'Swear to me that you yourselves will not attack me.'",
      "M": "They said to him, 'We have come to bind you and hand you over to the Philistines.' Samson said to them, 'Swear to me that you will not attack me yourselves.'",
      "T": "'We're here to tie you up and hand you to the Philistines,' they said. Samson said, 'Swear to me first—swear you won't attack me yourselves.'"
    },
    "13": {
      "L": "And they said to him, 'No, we will only bind you fast and give you into their hands, but we will not kill you.' So they bound him with two new ropes and brought him up from the rock.",
      "M": "They said, 'No, we will only bind you and give you into their hands, but we will not kill you.' They bound him with two new ropes and brought him up from the rock.",
      "T": "'We will tie you and hand you over—but we will not kill you,' they promised. They bound him with two new ropes and brought him up from the rock."
    },
    "14": {
      "L": "When he came to Lehi, the Philistines came shouting to meet him. And the Spirit of the LORD came mightily upon him, and the ropes on his arms became like flax burned with fire, and his bonds fell off his hands.",
      "M": "When he came to Lehi, the Philistines came shouting out to meet him. The Spirit of the LORD rushed upon him, and the ropes on his arms became like flax that catches fire, and his bonds fell from his hands.",
      "T": "When they brought him to Lehi, the Philistines shouted in triumph. At that moment the Spirit of the LORD came upon him with power. The ropes on his arms burned away like flax touched by flame, and the bonds fell from his hands."
    },
    "15": {
      "L": "And he found a fresh jawbone of a donkey, reached out and took it, and struck down a thousand men with it.",
      "M": "He found a fresh jawbone of a donkey, reached out and took it, and struck down a thousand men with it.",
      "T": "He picked up a fresh donkey's jawbone and with it killed a thousand men."
    },
    "16": {
      "L": "And Samson said, 'With the jawbone of a donkey, heap upon heap—with the jawbone of a donkey I have struck down a thousand men.'",
      "M": "And Samson said, 'With the jawbone of a donkey, heap upon heap—with the jawbone of a donkey I have struck down a thousand men.'",
      "T": "Samson sang out:\n'With a donkey's jaw—heap on heap—\nwith a donkey's jaw I have killed a thousand men!'"
    },
    "17": {
      "L": "When he had finished speaking, he threw the jawbone from his hand, and that place was called Ramath-lehi.",
      "M": "When he had finished speaking, he threw away the jawbone, and that place was called Ramath-lehi.",
      "T": "When he had finished, he threw down the jawbone. The place was named Ramath-lehi—'the height of the jawbone.'"
    },
    "18": {
      "L": "And he was very thirsty, and he called on the LORD and said, 'You have given this great salvation into the hand of your servant, and now shall I die of thirst and fall into the hand of the uncircumcised?'",
      "M": "He was extremely thirsty, and he called out to the LORD and said, 'You have given this great salvation into the hand of your servant, and now must I die of thirst and fall into the hands of the uncircumcised?'",
      "T": "Then terrible thirst hit him. He cried out to the LORD: 'You gave your servant this great victory—and now I'm going to die of thirst? Fall into the hands of the uncircumcised?'"
    },
    "19": {
      "L": "And God split the hollow place that was in Lehi, and water came out of it. He drank, and his spirit returned and he revived. Therefore the name of that place is called En-hakkore, which is in Lehi to this day.",
      "M": "God split open a hollow place in the Lehi, and water gushed out. He drank, and his spirit revived and he was refreshed. Therefore the name of that place is called En-hakkore, which is in Lehi to this day.",
      "T": "God split open a hollow in the rocky ground and water gushed out. Samson drank, his strength returned, and he came back to life. He named the spring En-hakkore—'the Spring of the One Who Called'—and it is in Lehi to this day."
    },
    "20": {
      "L": "And he judged Israel in the days of the Philistines twenty years.",
      "M": "He judged Israel for twenty years in the days of the Philistines.",
      "T": "He governed Israel in the era of Philistine oppression for twenty years."
    }
  },
  "16": {
    "1": {
      "L": "Then Samson went to Gaza and saw a prostitute there, and he went in to her.",
      "M": "Samson went to Gaza, where he saw a prostitute and went in to her.",
      "T": "Samson went to Gaza and slept with a prostitute there."
    },
    "2": {
      "L": "The Gazites were told, 'Samson has come here.' And they surrounded him and lay in wait for him all night at the city gate, keeping silent all night and saying, 'At morning light we will kill him.'",
      "M": "It was reported to the people of Gaza, 'Samson has come here.' They surrounded him and set an ambush for him all night at the city gate, keeping silent all night and saying, 'At dawn we will kill him.'",
      "T": "Word spread through Gaza: 'Samson is here.' They surrounded the city gate and lay in ambush all night, waiting. 'At daybreak,' they said, 'we'll kill him.'"
    },
    "3": {
      "L": "Samson lay until midnight, and at midnight he arose and took hold of the doors of the city gate and the two posts, and pulled them up—bar and all—and put them on his shoulders and carried them to the top of the hill that faces Hebron.",
      "M": "Samson lay until midnight. Then he rose at midnight and took hold of the doors of the city gate and both posts, and pulled them up—bar and all—and carried them on his shoulders to the top of the hill that faces Hebron.",
      "T": "Samson slept until midnight. Then he got up, seized the city gates—doors, posts, bar and all—hoisted them on his shoulders, and carried them to the top of the hill overlooking Hebron."
    },
    "4": {
      "L": "After this he loved a woman in the Valley of Sorek, whose name was Delilah.",
      "M": "After this he fell in love with a woman in the Valley of Sorek, whose name was Delilah.",
      "T": "After this Samson fell in love with a woman in the Valley of Sorek. Her name was Delilah."
    },
    "5": {
      "L": "And the lords of the Philistines came up to her and said, 'Seduce him and see where his great strength lies, and by what means we can overpower him so that we may bind him and subdue him. Each one of us will give you eleven hundred pieces of silver.'",
      "M": "The lords of the Philistines came to her and said, 'Seduce him, and find out where his great strength comes from and how we can overpower him so that we can bind and subdue him. Each of us will pay you eleven hundred pieces of silver.'",
      "T": "The Philistine warlords came to Delilah with a proposition: 'Seduce him. Find out the secret of his strength—how we can capture and subdue him. Each one of us will pay you eleven hundred pieces of silver.' Five lords: five thousand five hundred pieces in all."
    },
    "6": {
      "L": "And Delilah said to Samson, 'Please tell me where your great strength lies and how you could be bound to subdue you.'",
      "M": "Delilah said to Samson, 'Please tell me where your great strength lies and how you could be bound to subdue you.'",
      "T": "So Delilah asked Samson, 'Tell me—where does your great strength come from? What would it take to overpower you?'"
    },
    "7": {
      "L": "And Samson said to her, 'If they bind me with seven fresh bowstrings that have not been dried, then I shall be weak and be like any other man.'",
      "M": "Samson said to her, 'If they bind me with seven fresh bowstrings that have not been dried, I will become weak and be like any other man.'",
      "T": "Samson said, 'If someone ties me with seven fresh bowstrings that haven't dried out, I'd be as weak as any man.'"
    },
    "8": {
      "L": "Then the lords of the Philistines brought her seven fresh bowstrings that had not been dried, and she bound him with them.",
      "M": "The lords of the Philistines brought her seven fresh bowstrings that had not been dried, and she bound him with them.",
      "T": "The Philistine lords brought her seven fresh bowstrings, and she tied him up."
    },
    "9": {
      "L": "Now there were men lying in ambush in the inner room. And she said to him, 'The Philistines are upon you, Samson!' But he snapped the bowstrings as a strand of flax snaps when it touches the fire. So the secret of his strength was not known.",
      "M": "There were men hiding in the inner room. She said to him, 'The Philistines are upon you, Samson!' But he snapped the bowstrings as a strand of flax snaps when it touches fire. And his strength remained secret.",
      "T": "Men were hiding in the room with her. 'Samson! The Philistines!' she cried. He snapped the bowstrings like a thread of tow breaking in fire. His secret was still safe."
    },
    "10": {
      "L": "And Delilah said to Samson, 'Behold, you have mocked me and told me lies. Now please tell me how you could be bound.'",
      "M": "Delilah said to Samson, 'You have mocked me and told me lies. Now please tell me how you could be bound.'",
      "T": "Delilah said to him, 'You lied to me. You made a fool of me. Tell me the real answer.'"
    },
    "11": {
      "L": "And he said to her, 'If they bind me tightly with new ropes that have never been used, then I shall be weak and be like any other man.'",
      "M": "He said to her, 'If they bind me with new ropes that have never been used, I will become weak and be like any other man.'",
      "T": "He said, 'New ropes—ones that have never been used on anything. Tie me with those, and I'd be helpless.'"
    },
    "12": {
      "L": "So Delilah took new ropes and bound him with them and said to him, 'The Philistines are upon you, Samson!' The men in ambush were hidden in the inner room. And he snapped the ropes from his arms like thread.",
      "M": "Delilah took new ropes, bound him with them, and said, 'The Philistines are upon you, Samson!' Again there were men hiding in the inner room. He snapped the ropes off his arms like thread.",
      "T": "Delilah got new ropes and tied him again. 'Samson! The Philistines!' Again the hidden men were there. He snapped the ropes from his arms like thread."
    },
    "13": {
      "L": "Then Delilah said to Samson, 'Until now you have mocked me and told me lies. Tell me how you could be bound.' And he said to her, 'If you weave the seven locks of my hair into the weaving on a loom—'",
      "M": "Delilah said to Samson, 'Until now you have mocked me and told me lies. Tell me how you could be bound.' He said to her, 'If you weave the seven locks of my hair into the weaving on a loom—'",
      "T": "'You keep lying to me,' Delilah said. 'Tell me the truth.' He said, 'Weave the seven braids of my hair into the loom—'"
    },
    "14": {
      "L": "And she fastened the braids with the pin and said to him, 'The Philistines are upon you, Samson!' But he woke from his sleep and pulled out the loom pin along with the web.",
      "M": "She fastened the braids with the pin and said, 'The Philistines are upon you, Samson!' He woke from his sleep and pulled out the loom pin along with the web.",
      "T": "She pinned the loom and called out, 'Samson! The Philistines!' He woke and pulled the whole thing loose—the pin, the weaving, everything."
    },
    "15": {
      "L": "And she said to him, 'How can you say, I love you, when your heart is not with me? You have mocked me these three times and have not told me where your great strength lies.'",
      "M": "She said to him, 'How can you say you love me when your heart is not with me? You have mocked me three times and not told me where your great strength lies.'",
      "T": "'How can you say you love me when you won't trust me?' she said. 'Three times now you've mocked me. Three times you've refused to tell me the truth.'"
    },
    "16": {
      "L": "And when she pressed him daily with her words and urged him, his soul was worn out to death.",
      "M": "And when she pressed him day after day with her words and urged him, he was worn down to the point of death.",
      "T": "She pressed him day after day, never letting up, until he was exhausted to the point of death."
    },
    "17": {
      "L": "And he told her all his heart and said to her, 'A razor has never come upon my head, for I have been a Nazirite to God from my mother's womb. If my head is shaved, my strength will leave me, and I will become weak and be like any other man.'",
      "M": "He told her all his heart and said, 'A razor has never touched my head, for I have been a Nazirite to God from my mother's womb. If my head is shaved, my strength will leave me, and I will become weak and be like any other man.'",
      "T": "He finally told her everything. 'A razor has never touched my head,' he said. 'I have been a Nazirite to God since before I was born. If my hair is shaved off, my strength will leave me—I'll be like anyone else.' He had given away the one secret that mattered."
    },
    "18": {
      "L": "When Delilah saw that he had told her all his heart, she sent and called the lords of the Philistines, saying, 'Come up this once, for he has told me all his heart.' Then the lords of the Philistines came up to her and brought the money in their hands.",
      "M": "When Delilah saw that he had told her everything, she sent for the lords of the Philistines, saying, 'Come up this time, for he has told me everything.' The lords of the Philistines came up to her and brought the silver in their hands.",
      "T": "Delilah saw that he had finally told the truth. She sent word to the Philistine lords: 'Come now—this time he's told me everything.' The lords came up, bringing the silver payment."
    },
    "19": {
      "L": "And she made him sleep on her knees and called for a man and had him shave off the seven locks of his head. Then she began to torment him, and his strength left him.",
      "M": "She lulled him to sleep on her lap and called in a man to shave off the seven locks of his head. She began to torment him, and his strength left him.",
      "T": "She lulled him to sleep in her lap and summoned a man to shave his head. Seven braids gone. She began to torment him—and his strength drained away."
    },
    "20": {
      "L": "And she said, 'The Philistines are upon you, Samson!' And he awoke from his sleep and said, 'I will go out as at other times and shake myself free.' But he did not know that the LORD had departed from him.",
      "M": "She said, 'The Philistines are upon you, Samson!' He woke from his sleep and said, 'I will go out as before and shake myself free.' But he did not know that the LORD had departed from him.",
      "T": "'Samson! The Philistines!' He woke and thought, 'I'll do what I always do—shake them off.' He did not know that the LORD had left him."
    },
    "21": {
      "L": "But the Philistines seized him and gouged out his eyes and brought him down to Gaza and bound him with bronze shackles, and he ground grain in the prison house.",
      "M": "The Philistines seized him and gouged out his eyes. They brought him down to Gaza, bound him with bronze shackles, and he ground grain in the prison.",
      "T": "The Philistines seized him, put out his eyes, and brought him down to Gaza in bronze chains. He spent his days grinding grain in the prison—a champion reduced to a slave."
    },
    "22": {
      "L": "However, the hair of his head began to grow again after it was shaved.",
      "M": "But the hair of his head began to grow back after it had been shaved.",
      "T": "In the darkness of the prison, his hair began to grow."
    },
    "23": {
      "L": "Then the lords of the Philistines gathered to offer a great sacrifice to Dagon their god and to celebrate, saying, 'Our god has given Samson our enemy into our hand.'",
      "M": "The lords of the Philistines gathered to offer a great sacrifice to Dagon their god and to celebrate, saying, 'Our god has given Samson our enemy into our hand.'",
      "T": "The Philistine warlords assembled for a great sacrifice to Dagon, their god, and to celebrate. 'Our god has given us Samson—our enemy—into our power!' they cried."
    },
    "24": {
      "L": "And when the people saw him, they praised their god and said, 'Our god has given our enemy into our hands, the one who laid waste our land and killed many of us.'",
      "M": "When the people saw him, they praised their god and said, 'Our god has given our enemy into our hands—the one who ravaged our land and killed many of our people.'",
      "T": "The crowd cheered when they saw Samson. They praised Dagon: 'Our god has given us the one who devastated our land and slaughtered our people!'"
    },
    "25": {
      "L": "And it came to pass, when their hearts were merry, that they said, 'Call for Samson, so he may entertain us.' So they called Samson out of the prison, and he performed for them. They stationed him between the pillars.",
      "M": "When their hearts were merry, they said, 'Call for Samson, so he may perform for us.' So they called Samson out of the prison, and he performed for them. They stationed him between the pillars.",
      "T": "When the crowd was drunk with celebration, they called for Samson: 'Bring out the blind man—let him entertain us!' They brought him from the prison and made him perform. They stood him between the pillars."
    },
    "26": {
      "L": "And Samson said to the young man who was leading him by the hand, 'Let me touch the pillars that support the house so I can lean against them.'",
      "M": "Samson said to the young man who was leading him by the hand, 'Let me feel the pillars that support the house so I can lean against them.'",
      "T": "Samson said to the boy leading him by the hand, 'Let me lean against the pillars—let me feel them.'"
    },
    "27": {
      "L": "Now the house was full of men and women; all the lords of the Philistines were there, and on the roof about three thousand men and women were watching while Samson performed.",
      "M": "The house was filled with men and women; all the lords of the Philistines were there, and on the roof about three thousand men and women watched Samson perform.",
      "T": "The great hall was packed—all the Philistine warlords present. Three thousand more men and women watched from the roof above."
    },
    "28": {
      "L": "And Samson called out to the LORD and said, 'O Lord GOD, remember me and strengthen me only this once, O God, that I may be avenged on the Philistines for my two eyes.'",
      "M": "Samson called out to the LORD and said, 'O Lord GOD, please remember me and please give me strength only this once, O God, that I may avenge myself on the Philistines for my two eyes.'",
      "T": "Samson prayed to the LORD: 'O Lord GOD, remember me. Give me strength one more time—just this once, God. Let me have my revenge on the Philistines for the loss of my eyes.'"
    },
    "29": {
      "L": "And Samson grasped the two middle pillars on which the house rested and braced himself against them, one in his right hand and one in his left.",
      "M": "Samson grasped the two middle pillars on which the house rested and braced himself against them, one in his right hand and one in his left.",
      "T": "Samson found the two central pillars and pressed his hands against them—right hand on one, left hand on the other."
    },
    "30": {
      "L": "And Samson said, 'Let me die with the Philistines.' He pushed with all his might, and the house fell on the lords and on all the people in it. So those he killed at his death were more than those he had killed during his life.",
      "M": "Samson said, 'Let me die with the Philistines!' He pushed with all his might, and the house fell on the lords and on all the people in it. So those he killed at his death were more than those he had killed during his life.",
      "T": "Samson said, 'Let me die with the Philistines.' He pushed with everything he had. The pillars buckled. The roof came down on the lords, on the crowd, on everyone in the building. The dead he killed in his death outnumbered all he had killed in his life."
    },
    "31": {
      "L": "Then his brothers and all his father's household came down, took him, and brought him up and buried him between Zorah and Eshtaol in the tomb of Manoah his father. He had judged Israel twenty years.",
      "M": "Then his brothers and all his father's family came down, took him, and buried him between Zorah and Eshtaol in the tomb of Manoah his father. He had judged Israel twenty years.",
      "T": "His brothers and his father's family came down and brought his body home, burying him between Zorah and Eshtaol in the tomb of his father Manoah. He had governed Israel for twenty years."
    }
  },
  "17": {
    "1": {
      "L": "And there was a man of the hill country of Ephraim whose name was Micah.",
      "M": "There was a man in the hill country of Ephraim whose name was Micah.",
      "T": "In the hill country of Ephraim there lived a man named Micah."
    },
    "2": {
      "L": "And he said to his mother, 'The eleven hundred pieces of silver that were taken from you—about which you cursed, and which you also spoke of in my hearing—behold, the silver is with me; I took it.' And his mother said, 'Blessed be my son by the LORD.'",
      "M": "He said to his mother, 'The eleven hundred pieces of silver that were taken from you, about which you put a curse, and which you also mentioned in my hearing—I took it. It is with me.' And his mother said, 'May my son be blessed by the LORD.'",
      "T": "He said to his mother, 'The eleven hundred pieces of silver that were stolen from you—the curse you spoke in my hearing—I took it. It's here.' His mother said, 'Bless you, my son—the LORD bless you.'"
    },
    "3": {
      "L": "And when he returned the eleven hundred pieces of silver to his mother, his mother said, 'I solemnly dedicate the silver to the LORD from my hand for my son, to make a carved image and a cast idol. Now I will restore it to you.'",
      "M": "When he returned the eleven hundred pieces of silver to his mother, she said, 'I solemnly dedicate this silver to the LORD for my son, to make a carved image and a cast idol. Now I return it to you.'",
      "T": "When he returned the silver, his mother said, 'I had already dedicated this silver to the LORD—for my son—to make a carved idol and a cast image.' She gave it back to him."
    },
    "4": {
      "L": "So he gave the money back to his mother, and his mother took two hundred pieces of silver and gave them to the metalworker, who made a carved image and a cast idol. And they were placed in the house of Micah.",
      "M": "So he restored the money to his mother. She took two hundred pieces of silver and gave them to the metalworker, who made them into a carved image and a cast idol. And they were placed in the house of Micah.",
      "T": "His mother took two hundred of the silver pieces and gave them to a craftsman, who made a carved image and a cast idol. These were installed in Micah's house."
    },
    "5": {
      "L": "Now the man Micah had a shrine, and he made an ephod and teraphim, and he installed one of his sons as his priest.",
      "M": "Now Micah had a shrine. He had made an ephod and teraphim, and he installed one of his sons as his priest.",
      "T": "Micah set up a complete household shrine—an ephod, household divination idols (teraphim)—and ordained one of his own sons as the family priest."
    },
    "6": {
      "L": "In those days there was no king in Israel; everyone did what was right in his own eyes.",
      "M": "In those days there was no king in Israel; each person did what was right in his own eyes.",
      "T": "In those days Israel had no king—and every person did whatever seemed right to themselves."
    },
    "7": {
      "L": "Now there was a young man from Bethlehem in Judah, from the clan of Judah, who was a Levite, and he was sojourning there.",
      "M": "There was a young man from Bethlehem in Judah, from the family of Judah, who was a Levite, and he was staying there.",
      "T": "A young man from Bethlehem in Judah—a Levite who had been living there—was looking for a place."
    },
    "8": {
      "L": "And the man left the city of Bethlehem in Judah to find a place to settle. And as he journeyed, he came to the hill country of Ephraim, to the house of Micah.",
      "M": "The man left Bethlehem in Judah to find a suitable place to stay. On his journey he came to the hill country of Ephraim, to the house of Micah.",
      "T": "The Levite left Bethlehem in search of a place to settle. His travels brought him to the hill country of Ephraim and to the house of Micah."
    },
    "9": {
      "L": "And Micah said to him, 'Where do you come from?' And he said to him, 'I am a Levite from Bethlehem in Judah, and I am going to find a place to settle.'",
      "M": "Micah said to him, 'Where are you from?' He replied, 'I am a Levite from Bethlehem in Judah, and I am looking for a place to settle.'",
      "T": "Micah asked, 'Where are you from?' 'I'm a Levite from Bethlehem in Judah,' he said, 'looking for a place to live.'"
    },
    "10": {
      "L": "And Micah said to him, 'Stay with me and be to me a father and a priest, and I will give you ten pieces of silver a year, a set of clothing, and your food.' So the Levite went in.",
      "M": "Micah said to him, 'Stay with me and be my father and priest. I will give you ten pieces of silver a year, a set of clothing, and your food.' So the Levite accepted.",
      "T": "Micah said, 'Live with me. Be my father and my priest. I'll pay you ten silver a year, provide your clothing and food.' The Levite agreed."
    },
    "11": {
      "L": "And the Levite agreed to live with the man, and the young man became to him like one of his own sons.",
      "M": "The Levite agreed to stay with Micah, and the young man became to him like one of his own sons.",
      "T": "The Levite was content. Micah treated him like one of his own sons."
    },
    "12": {
      "L": "And Micah consecrated the Levite, and the young man became his priest and lived in the house of Micah.",
      "M": "Micah ordained the Levite, and the young man became his priest and lived in Micah's house.",
      "T": "Micah formally ordained the Levite, who became the household priest living in Micah's shrine."
    },
    "13": {
      "L": "Then Micah said, 'Now I know that the LORD will do good to me, because I have a Levite as my priest.'",
      "M": "Then Micah said, 'Now I know that the LORD will do good to me, for I have a Levite as my priest.'",
      "T": "Micah said with satisfaction, 'Now I know the LORD will bless me—I have a real Levite as my priest.' He did not notice the contradiction: invoking the LORD's blessing upon a shrine built on stolen silver, filled with carved idols."
    }
  },
  "18": {
    "1": {
      "L": "In those days there was no king in Israel. And in those days the tribe of the Danites was seeking an inheritance for itself to settle in, for to that day no inheritance had been allotted to them among the tribes of Israel.",
      "M": "In those days there was no king in Israel. In those days the tribe of the Danites was seeking an inheritance for themselves to settle in, for until that day no inheritance had been allotted to them among the tribes of Israel.",
      "T": "In those days Israel had no king. The tribe of Dan was still without a settled territory—no portion had fallen to them among the tribes—and they were looking for land to call their own."
    },
    "2": {
      "L": "So the people of Dan sent five capable men from their whole number, from Zorah and Eshtaol, to spy out and search the land. They said to them, 'Go and search the land.' When they came to the hill country of Ephraim, to the house of Micah, they lodged there.",
      "M": "So the people of Dan sent five capable men from the whole of their number, from Zorah and Eshtaol, to explore and spy out the land. They said to them, 'Go and spy out the land.' They came to the hill country of Ephraim and to the house of Micah, and they spent the night there.",
      "T": "The Danites sent five warriors from their clans—from Zorah and Eshtaol—to scout out land for them to settle. 'Go reconnoiter the land,' they were told. When the scouts reached the Ephraimite highlands they spent the night at Micah's house."
    },
    "3": {
      "L": "While they were at the house of Micah, they recognized the voice of the young Levite. They turned aside and said to him, 'Who brought you here? What are you doing in this place? What is your business here?'",
      "M": "When they were at Micah's house, they recognized the voice of the young Levite. They went in and said to him, 'Who brought you here? What are you doing in this place? What do you have here?'",
      "T": "They recognized the young Levite's voice. They went in and said, 'What are you doing here? Who brought you? What's your arrangement?'"
    },
    "4": {
      "L": "And he said to them, 'Such and such Micah has done for me—he has hired me, and I am his priest.'",
      "M": "He said to them, 'Micah has done such and such for me—he has hired me and I am his priest.'",
      "T": "'Micah hired me,' he said. 'I serve as his household priest.'"
    },
    "5": {
      "L": "And they said to him, 'Please inquire of God for us, so that we may know whether the journey we are going on will succeed.'",
      "M": "They said to him, 'Please inquire of God for us—we want to know whether the journey we are undertaking will succeed.'",
      "T": "'Ask God for us,' they said. 'We need to know—will this mission succeed?'"
    },
    "6": {
      "L": "And the priest said to them, 'Go in peace. The journey you are on is before the LORD.'",
      "M": "The priest said to them, 'Go in peace. Your journey is before the LORD.'",
      "T": "'Go in peace,' the priest said. 'The LORD is with your way.' He spoke with confidence he had no grounds for—an idol-priest pronouncing the divine name."
    },
    "7": {
      "L": "Then the five men departed and came to Laish and saw the people there, how they lived in safety after the manner of the Sidonians, quiet and secure, with no one in authority over them in any matter, far from the Sidonians and having no dealings with anyone.",
      "M": "So the five men departed and came to Laish. They saw the people there living carelessly, like the Sidonians, quiet and secure. There was no one in authority to disturb them in any matter, and they were far from the Sidonians and had no dealings with anyone.",
      "T": "The scouts came to Laish and found a people living without a care—like the Sidonians in their ways, quiet and secure, with no strong ruler and no ally nearby. They were far from Sidon, isolated, defenseless."
    },
    "8": {
      "L": "They came back to their relatives at Zorah and Eshtaol. And their relatives said to them, 'What is your report?'",
      "M": "They returned to their relatives at Zorah and Eshtaol. Their relatives said to them, 'What is your report?'",
      "T": "They returned to their kinsmen at Zorah and Eshtaol. 'What did you find?' their people asked."
    },
    "9": {
      "L": "And they said, 'Arise, let us go up against them, for we have seen the land and it is very good. Are you doing nothing? Do not be slow to go, to enter in and possess the land.'",
      "M": "They said, 'Arise, let us go up against them, for we have seen the land—it is excellent. And you sit here doing nothing? Do not hesitate to go in and take possession of the land.'",
      "T": "'Get up—let's go! We've seen the land and it's excellent. What are you waiting for? Don't just sit there. Go in and take it.'"
    },
    "10": {
      "L": "When you go, you will come to a people at ease, and the land is spacious. For God has given it into your hands—a place where there is no lack of anything that is on the earth.",
      "M": "When you go, you will come to a secure people, and the land is very large. God has given it into your hands—a place where there is no shortage of anything on earth.",
      "T": "'You'll find a people at ease, wide-open land, and God has given it into your hands—a place that lacks nothing this earth produces.'"
    },
    "11": {
      "L": "And six hundred men of the clan of the Danites, armed with weapons of war, set out from Zorah and Eshtaol.",
      "M": "So six hundred men of the clan of the Danites, armed with weapons of war, departed from Zorah and Eshtaol.",
      "T": "Six hundred armed Danite warriors set out from Zorah and Eshtaol."
    },
    "12": {
      "L": "They went up and camped at Kiriath-jearim in Judah. Therefore that place is called Mahaneh-dan to this day—it lies west of Kiriath-jearim.",
      "M": "They went up and camped at Kiriath-jearim in Judah. This is why that place is called Mahaneh-dan to this day; it lies west of Kiriath-jearim.",
      "T": "They camped at Kiriath-jearim in Judah—the place still called Mahaneh-dan, 'the Camp of Dan,' to the west of Kiriath-jearim."
    },
    "13": {
      "L": "From there they continued to the hill country of Ephraim and came to the house of Micah.",
      "M": "From there they continued to the hill country of Ephraim and came to the house of Micah.",
      "T": "From there they moved on into the Ephraimite highlands and arrived at the house of Micah."
    },
    "14": {
      "L": "Then the five men who had gone to spy out the land of Laish spoke up and said to their kinsmen, 'Do you know that in these houses there is an ephod, household idols, a carved image, and a cast idol? Consider what you should do.'",
      "M": "Then the five men who had gone to spy out the land of Laish spoke up and said to their kinsmen, 'Do you know that in these houses there is an ephod, teraphim, a carved image, and a cast idol? Consider what you should do.'",
      "T": "The five scouts spoke up: 'You know there's a shrine in that house—an ephod, household idols, a carved image, a cast idol. Think about what you want to do with that.'"
    },
    "15": {
      "L": "So they turned aside there and came to the house of the young Levite—which was in the house of Micah—and greeted him.",
      "M": "They turned in there and came to the house of the young Levite—which was in the house of Micah—and greeted him.",
      "T": "They turned toward the house and went to the young Levite at Micah's shrine and greeted him."
    },
    "16": {
      "L": "And the six hundred Danite men, armed with their weapons of war, stood at the entrance of the gate.",
      "M": "The six hundred Danite men, armed with their weapons of war, stood at the entrance of the gate.",
      "T": "While they talked, the six hundred armed Danites stood guard at the gate."
    },
    "17": {
      "L": "And the five men who had spied out the land went in and took the carved idol, the ephod, the teraphim, and the cast idol. The priest stood at the gate entrance with the six hundred armed men.",
      "M": "The five men who had spied out the land went in and took the carved idol, the ephod, the teraphim, and the cast idol. The priest stood at the gate entrance with the six hundred armed men.",
      "T": "The five scouts went in and took the carved idol, the ephod, the teraphim, and the cast image. The Levite priest stood at the gate while the six hundred soldiers held the entrance."
    },
    "18": {
      "L": "When they went into Micah's house and took the carved image, the ephod, the teraphim, and the cast idol, the priest said to them, 'What are you doing?'",
      "M": "When they went into Micah's house and took the carved image, the ephod, the teraphim, and the cast idol, the priest said to them, 'What are you doing?'",
      "T": "They went into Micah's shrine and carried everything out. The priest said, 'What are you doing?'"
    },
    "19": {
      "L": "And they said to him, 'Be quiet! Put your hand over your mouth and come with us. Is it better for you to be a priest to one man's household, or to be priest for a whole tribe and clan in Israel?'",
      "M": "They said to him, 'Quiet! Put your hand over your mouth and come with us. Is it better for you to be a priest to one man's household, or to be priest for a whole tribe and clan in Israel?'",
      "T": "'Be quiet,' they said. 'Put your hand over your mouth and come with us. Is it better to be a priest for one household, or priest to an entire tribe of Israel?'"
    },
    "20": {
      "L": "And the priest's heart was glad. He took the ephod and the teraphim and the carved image and went with the people.",
      "M": "The priest's heart was glad. He took the ephod, the teraphim, and the carved image and joined the people.",
      "T": "The priest's heart leapt at the offer. He took the ephod, the teraphim, and the carved image and fell in with the people."
    },
    "21": {
      "L": "Then they turned and set out, putting the children, the livestock, and the goods ahead of them.",
      "M": "Then they turned and set out, placing the children, livestock, and goods ahead of them.",
      "T": "They turned back with their plunder—women and children and cattle and goods placed in front, the armed men forming the rear guard."
    },
    "22": {
      "L": "When they had gone some distance from the house of Micah, the men who were in the houses near Micah gathered and caught up with the Danites.",
      "M": "When they had gone some distance from Micah's house, the men who were in the houses near Micah gathered and caught up with the Danites.",
      "T": "When they were well past Micah's house, his neighbors rallied and caught up with the Danite column."
    },
    "23": {
      "L": "They called out to the Danites, and the Danites turned around and said to Micah, 'What is the matter with you, that you come with such a company?'",
      "M": "They called out to the Danites. The Danites turned and said to Micah, 'What is the matter with you, that you come with such a force?'",
      "T": "They called after the Danites. The column halted. 'What's your problem, Micah?' they said. 'Why the mob?'"
    },
    "24": {
      "L": "And he said, 'You have taken my gods that I made, and the priest, and gone away. What do I have left? How can you say to me, What is the matter with you?'",
      "M": "He said, 'You have taken my gods that I made, and the priest, and gone your way. What do I have left? How can you ask me what is the matter with me?'",
      "T": "'You took my gods—the gods I made—and my priest,' Micah said, 'and you walk away. What do I have left? How can you ask what's wrong with me?'"
    },
    "25": {
      "L": "And the Danites said to him, 'Do not let your voice be heard among us, or violent men will attack you and you will lose your life along with the lives of your household.'",
      "M": "The Danites said to him, 'Don't raise your voice against us, or hot-tempered men will attack you and you will lose your life and the lives of your household.'",
      "T": "'Keep your mouth shut,' the Danites said. 'There are men here with short tempers. Keep pushing and you'll lose your life—and your family with you.'"
    },
    "26": {
      "L": "And the Danites went on their way. And when Micah saw that they were stronger than he was, he turned around and went back home.",
      "M": "The Danites went on their way. And when Micah saw that they were stronger than he was, he turned around and went home.",
      "T": "The Danites marched on. Micah stood and looked at the column. They were too many. He turned around and went home."
    },
    "27": {
      "L": "And they took what Micah had made and the priest he had, and came to Laish—to a people quiet and secure—and struck them with the sword and burned the city with fire.",
      "M": "They took what Micah had made and the priest he had, and came to Laish—a people quiet and secure. They struck them with the sword and burned the city.",
      "T": "Carrying Micah's idols and his priest, the Danites came to Laish—a people living at peace, with no warning and no defense. They put them to the sword and burned the city to the ground."
    },
    "28": {
      "L": "And there was no one to rescue them, for the city was far from Sidon and they had no dealings with anyone. It was in the valley near Beth-rehob. They rebuilt the city and settled in it.",
      "M": "There was no one to rescue them, for the city was far from Sidon, and they had no alliance with anyone. It was in the valley near Beth-rehob. The Danites rebuilt the city and settled in it.",
      "T": "There was no rescuer—the city was far from Sidon, isolated and without ally. It lay in the valley near Beth-rehob. The Danites rebuilt it and settled in their new home."
    },
    "29": {
      "L": "And they named the city Dan, after the name of their ancestor Dan, who was born to Israel, though the city had formerly been called Laish.",
      "M": "They named the city Dan, after the name of their ancestor Dan, who was born to Israel, though the city had formerly been called Laish.",
      "T": "They named the city Dan, after their ancestor Dan, son of Israel—though it had been called Laish before. The northernmost city of Israel now bore the tribal name, acquired through violence."
    },
    "30": {
      "L": "And the Danites set up the carved image for themselves. And Jonathan son of Gershom, son of Manasseh, and his sons were priests to the tribe of Dan until the day of the exile of the land.",
      "M": "The Danites set up the carved image. Jonathan son of Gershom, son of Manasseh, and his sons served as priests to the tribe of Dan until the day of the exile of the land.",
      "T": "The Danites installed Micah's carved idol. Jonathan son of Gershom served as priest—a descendant of Moses (Hebrew scribes suspended a letter to write 'Manasseh' where the original name was 'Moses,' to spare the lawgiver's name the shame of a grandson who became an idol-priest). His sons continued the priesthood until the day of exile."
    },
    "31": {
      "L": "And they maintained Micah's carved image all the time that the house of God was at Shiloh.",
      "M": "They maintained Micah's carved image all the years that the house of God was at Shiloh.",
      "T": "They maintained that unauthorized idol throughout all the years the legitimate sanctuary stood at Shiloh—the true house of God and this false one coexisting in an era when everyone did what was right in their own eyes."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'judges')
        merge_tier(existing, JUDGES, tier_key)
        save(tier_dir, 'judges', existing)
    print('Judges 13–18 written.')

if __name__ == '__main__':
    main()
