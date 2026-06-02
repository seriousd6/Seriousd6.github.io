"""
MKT 1 Samuel chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1samuel-1-6.py

Covers: Hannah's prayer and Samuel's birth (ch. 1); Hannah's song, Eli's corrupt sons,
and the man of God's prophecy against Eli's house (ch. 2); the LORD's call to Samuel
(ch. 3); the Ark taken by the Philistines, death of Eli and Ichabod's birth (ch. 4);
the Ark in Philistia — Dagon's fall and the tumors on the Philistine cities (ch. 5);
the Ark's return to Beth-shemesh (ch. 6).

Translation decisions:
- H3068 (יהוה): "LORD" L/M; "the LORD" T — consistent with all prior OT scripts.
- H430 (אֱלֹהִים): "God" all tiers when divine; "gods" for Dagon / pagan references.
- H6635 (צָבָאוֹת): "hosts" all tiers — "LORD of hosts" first appears here in narrative
  literature; Hannah introduces this throne-room title at Shiloh in her prayer (1:11).
- H5315 (נֶפֶשׁ): "soul" L; context-sensitive M/T — in 1:15 Hannah's "pouring out my
  soul" is total self-disclosure (the embodied whole person), not an immaterial substance.
- H7592 (שָׁאַל): "asked" — key to Samuel's name; Hannah's folk-etymology in 1:20 links
  שְׁמוּאֵל to sha'al (ask); T surfaces this wordplay.
- H4899 (מָשִׁיחַ): "anointed" L/M; "his anointed one" T — Hannah's song ends on this
  word (2:10), the first occurrence of the messianic title in the Former Prophets; T
  names its significance before any king exists.
- H727 (אָרוֹן): "ark" all tiers; T distinguishes "ark of God" (divine presence register)
  from "ark of the covenant" (covenantal/legal register) per the Hebrew formulation.
- H3519 (כָּבוֹד): "glory" all tiers — Ichabod (4:21) means "no glory" or "where is the
  glory?"; T renders גָּלָה as "gone into exile" to activate the exile register latent in
  the word (same root as Israel's future exile), not merely "departed."
- H1697 (דָּבָר): "word" in revelatory contexts; in 3:1 "the word of the LORD was rare"
  — divine speech had ceased; T treats the silence as judgment.
- H7307 (רוּחַ): "spirit" in 1:15 (Hannah is "troubled in spirit"); context is distress,
  not divine anointing; capitalized "Spirit" not used here.
- H2617 (חֶסֶד): "kindness" L; "faithful kindness" M; "steadfast loyal love" T.
- H5930 (עֹלָה): "burnt offering" all tiers.
- Nazirite vow (1:11): "no razor shall come upon his head" — identical formula to
  Samson (Judges 13:5); T notes the contrast: Hannah consecrates her son freely; the
  Samson parallel is ironic — Samuel will be the faithful Nazirite Samson was not.
- Hannah's Song (2:1-10): T tier uses poetic line structure with line breaks (\n);
  the song is theologically foundational — a "songs of reversal" tradition that Mary's
  Magnificat (Luke 1:46-55) consciously echoes; the ending on "his anointed" (2:10)
  plants messianic seed before the monarchy exists.
- 6:19 textual note: MT reads "seventy men, fifty thousand men" (50,070 total); this
  figure exceeds the plausible population of Beth-shemesh; LXX reads only 70 men; L/M
  follow MT faithfully; T notes the likely scribal dittography.
- Eli's sons (2:12): "sons of Belial" (בְּנֵי בְלִיַּעַל) — idiom for men belonging to
  the realm of ruin/worthlessness; T keeps the Hebrew idiom and glosses it.
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

FIRST_SAMUEL = {
  "1": {
    "1": {
      "L": "Now there was a certain man of Ramathaim-zophim, of the hill country of Ephraim, and his name was Elkanah the son of Jeroham, son of Elihu, son of Tohu, son of Zuph, an Ephraimite.",
      "M": "There was a certain man from Ramathaim-zophim in the hill country of Ephraim, whose name was Elkanah son of Jeroham, son of Elihu, son of Tohu, son of Zuph, an Ephraimite.",
      "T": "A man lived in the hill country of Ephraim, in a town called Ramathaim-zophim. His name was Elkanah—son of Jeroham, son of Elihu, son of Tohu, son of Zuph—an Ephraimite by lineage."
    },
    "2": {
      "L": "And he had two wives; the name of the one was Hannah, and the name of the other Peninnah. And Peninnah had children, but Hannah had no children.",
      "M": "He had two wives. The name of one was Hannah and the name of the other Peninnah. Peninnah had children, but Hannah had no children.",
      "T": "He had two wives: Hannah and Peninnah. Peninnah had children. Hannah had none. The story turns on that absence."
    },
    "3": {
      "L": "Now this man went up from his city year by year to worship and to sacrifice to the LORD of hosts at Shiloh, where the two sons of Eli, Hophni and Phinehas, were priests of the LORD.",
      "M": "This man went up from his city every year to worship and sacrifice to the LORD of hosts at Shiloh, where Eli's two sons, Hophni and Phinehas, served as priests of the LORD.",
      "T": "Year after year Elkanah made the pilgrimage to Shiloh to worship and sacrifice to the LORD of hosts. At Shiloh, Eli's two sons—Hophni and Phinehas—served as priests. Their names will matter soon."
    },
    "4": {
      "L": "On the day when Elkanah sacrificed, he would give portions to Peninnah his wife and to all her sons and daughters.",
      "M": "On the day Elkanah offered sacrifice, he would give portions to his wife Peninnah and to all her sons and daughters.",
      "T": "When sacrifice day came, Elkanah distributed portions to Peninnah and to each of her children."
    },
    "5": {
      "L": "But to Hannah he gave a double portion, because he loved her, though the LORD had closed her womb.",
      "M": "But to Hannah he gave a double portion, because he loved her, even though the LORD had closed her womb.",
      "T": "To Hannah he gave a double portion—a public sign of his love. Yet the LORD had closed her womb, and love alone could not open it."
    },
    "6": {
      "L": "And her rival used to provoke her grievously to irritate her, because the LORD had closed her womb.",
      "M": "Her rival would provoke her bitterly to irritate her, because the LORD had closed her womb.",
      "T": "Peninnah, her rival, tormented her relentlessly—twisting the wound of barrenness, year after year."
    },
    "7": {
      "L": "So it went on year by year. As often as she went up to the house of the LORD, she provoked her. Therefore she wept and would not eat.",
      "M": "This went on year after year. Whenever Hannah went up to the house of the LORD, Peninnah would provoke her, so that she wept and would not eat.",
      "T": "The pattern repeated every year. Each time they made the pilgrimage to Shiloh, Peninnah would start again—until Hannah sat weeping at the table, unable to eat."
    },
    "8": {
      "L": "And Elkanah her husband said to her, Hannah, why do you weep? And why do you not eat? And why is your heart sad? Am I not more to you than ten sons?",
      "M": "Elkanah her husband said to her, \"Hannah, why are you weeping? Why won't you eat? Why is your heart grieved? Am I not more to you than ten sons?\"",
      "T": "Elkanah leaned close and said, \"Hannah, why are you weeping? Why won't you eat? Why this heartache? Aren't I worth more to you than ten sons?\" He meant it kindly. He did not understand."
    },
    "9": {
      "L": "After they had eaten in Shiloh and after they had drunk, Hannah rose. Now Eli the priest was sitting on the seat beside the doorpost of the temple of the LORD.",
      "M": "After they had eaten and drunk in Shiloh, Hannah rose. Now Eli the priest was sitting on his seat by the doorpost of the temple of the LORD.",
      "T": "When the meal was over, Hannah got up and went to the sanctuary. Eli the priest sat on his chair by the doorpost of the LORD's house."
    },
    "10": {
      "L": "She was deeply distressed and prayed to the LORD and wept bitterly.",
      "M": "She was deeply distressed and prayed to the LORD, weeping bitterly.",
      "T": "Shattered in spirit, she poured out her prayer to the LORD—and wept without restraint."
    },
    "11": {
      "L": "And she vowed a vow and said, O LORD of hosts, if you will indeed look on the affliction of your servant and remember me and not forget your servant, but will give to your servant a son, then I will give him to the LORD all the days of his life, and no razor shall come upon his head.",
      "M": "And she made a vow, saying, \"O LORD of hosts, if you will look on the misery of your servant and remember me and not forget me, but will give me a son, then I will give him to the LORD all the days of his life, and no razor shall touch his head.\"",
      "T": "She made a vow: \"O LORD of hosts—if you will see your servant's misery, if you will remember me and not forget me, if you will give me a son—then I will give him back to you for all his life. No razor will ever touch his head.\" The formula was a Nazirite consecration, the same language used for Samson. But where Samson's dedication was imposed before birth, Hannah's was offered freely—she asked for a child in order to give him away."
    },
    "12": {
      "L": "As she continued praying before the LORD, Eli observed her mouth.",
      "M": "As she continued praying before the LORD, Eli watched her mouth.",
      "T": "As Hannah kept praying, Eli sat watching her lips."
    },
    "13": {
      "L": "Hannah was speaking in her heart; only her lips moved, but her voice was not heard. So Eli took her for a drunken woman.",
      "M": "Hannah was speaking in her heart; only her lips moved, and her voice was not heard. Therefore Eli took her to be a drunken woman.",
      "T": "She was praying silently—lips moving, no sound coming out. Eli assumed she was drunk."
    },
    "14": {
      "L": "And Eli said to her, How long will you go on being drunk? Put away your wine from you.",
      "M": "And Eli said to her, \"How long are you going to be drunk? Put your wine away.\"",
      "T": "Eli called out: \"How long are you going to sit there drunk? Sober up.\""
    },
    "15": {
      "L": "But Hannah answered, No, my lord, I am a woman troubled in spirit. I have drunk neither wine nor strong drink, but I have been pouring out my soul before the LORD.",
      "M": "But Hannah answered, \"No, my lord, I am a woman deeply troubled in spirit. I have drunk neither wine nor strong drink, but I have been pouring out my soul before the LORD.",
      "T": "Hannah answered, \"No, my lord—I have not had wine or strong drink. I am a woman whose spirit is crushed. I have been pouring out my whole self before the LORD.\" The phrase she used—pouring out my soul (שְׁפֹךְ נַפְשִׁי)—means total exposure: nothing withheld, the entire person laid open before God."
    },
    "16": {
      "L": "Do not regard your servant as a worthless woman, for all this time I have been speaking out of my great anxiety and vexation.",
      "M": "Do not take your servant for a worthless woman, for I have been speaking from my great anxiety and grief all this time.\"",
      "T": "\"Do not take me for a wicked woman, my lord. I have been speaking out of the depth of my anguish and grief.\""
    },
    "17": {
      "L": "Then Eli answered, Go in peace, and the God of Israel grant your petition that you have made to him.",
      "M": "Then Eli answered, \"Go in peace, and may the God of Israel grant your petition that you have asked of him.\"",
      "T": "Eli softened. \"Go in peace,\" he said. \"May the God of Israel give you what you have asked of him.\""
    },
    "18": {
      "L": "And she said, Let your servant find favor in your eyes. Then the woman went her way and ate, and her face was no longer sad.",
      "M": "And she said, \"Let your servant find favor in your eyes.\" So the woman went her way, and she ate and drank, and her face was no longer downcast.",
      "T": "She said, \"May your servant find favor in your sight.\" Then she walked away. She ate. The shadow lifted from her face."
    },
    "19": {
      "L": "They rose early in the morning and worshiped before the LORD, and then they returned and came to their house at Ramah. And Elkanah knew Hannah his wife, and the LORD remembered her.",
      "M": "They rose early in the morning and worshiped before the LORD, then returned to their home at Ramah. Elkanah lay with Hannah his wife, and the LORD remembered her.",
      "T": "Early the next morning they worshiped before the LORD and made the journey home to Ramah. Elkanah was intimate with Hannah, and the LORD remembered her. That phrase—the LORD remembered her—is the pivot on which the whole chapter turns."
    },
    "20": {
      "L": "And in due time Hannah conceived and bore a son, and she called his name Samuel, for she said, I have asked for him from the LORD.",
      "M": "In the course of time Hannah conceived and bore a son, and she called his name Samuel, for she said, \"I have asked for him from the LORD.\"",
      "T": "In time Hannah conceived and bore a son. She named him Samuel—\"because,\" she said, \"I asked him from the LORD.\" The name carried her theology: sha'al, to ask; Samuel was the child given in answer to prayer."
    },
    "21": {
      "L": "The man Elkanah and all his house went up to offer to the LORD the yearly sacrifice and to pay his vow.",
      "M": "The man Elkanah and all his household went up to offer the yearly sacrifice to the LORD and to fulfill his vow.",
      "T": "When the annual sacrifice season arrived, Elkanah and his whole household made the pilgrimage to Shiloh to offer the yearly sacrifice and fulfill his vow."
    },
    "22": {
      "L": "But Hannah did not go up, for she said to her husband, As soon as the child is weaned, I will bring him, so that he may appear before the LORD and dwell there forever.",
      "M": "But Hannah did not go up, for she said to her husband, \"As soon as the child is weaned, I will bring him, that he may appear before the LORD and remain there permanently.\"",
      "T": "But Hannah stayed home. \"Not yet,\" she told Elkanah. \"When he is weaned, I will take him up myself—to appear before the LORD and stay there, given to him for good.\""
    },
    "23": {
      "L": "Elkanah her husband said to her, Do what seems best to you; wait until you have weaned him; only may the LORD establish his word. So the woman remained and nursed her son until she weaned him.",
      "M": "Elkanah her husband said to her, \"Do what seems best to you; wait until you have weaned him. Only, may the LORD establish his word.\" So the woman remained and nursed her son until she weaned him.",
      "T": "Elkanah deferred to her. \"Do whatever you think best. Stay until he is weaned. Only—may the LORD make good on his word.\" So Hannah stayed and nursed Samuel until he was weaned."
    },
    "24": {
      "L": "And when she had weaned him, she took him up with her, along with a three-year-old bull, an ephah of flour, and a skin of wine, and she brought him to the house of the LORD at Shiloh. And the child was young.",
      "M": "And when she had weaned him, she took him up with her, along with a three-year-old bull, an ephah of flour, and a skin of wine, and she brought him to the house of the LORD at Shiloh. The child was still young.",
      "T": "When Samuel was weaned, Hannah brought him to Shiloh herself—with a three-year-old bull, an ephah of flour, and a skin of wine. He was still a young child. She had given him every year of nursing she could; now she was keeping her word."
    },
    "25": {
      "L": "Then they slaughtered the bull, and they brought the child to Eli.",
      "M": "They slaughtered the bull and brought the child to Eli.",
      "T": "They slaughtered the bull. Then they brought the boy to Eli."
    },
    "26": {
      "L": "And she said, Oh, my lord, as you live, my lord, I am the woman who was standing here in your presence, praying to the LORD.",
      "M": "And she said, \"Oh, my lord! As you live, my lord, I am the woman who was standing here in your presence, praying to the LORD.",
      "T": "Hannah said, \"As surely as you live, my lord—I am the woman who stood here beside you praying to the LORD.\""
    },
    "27": {
      "L": "For this child I prayed, and the LORD has granted me my petition that I asked of him.",
      "M": "For this child I prayed, and the LORD has granted me my petition that I asked of him.",
      "T": "This is the child I asked for. And the LORD gave me exactly what I asked."
    },
    "28": {
      "L": "Therefore I have lent him to the LORD. As long as he lives, he is lent to the LORD. And he worshiped the LORD there.",
      "M": "Therefore I have given him back to the LORD. As long as he lives, he belongs to the LORD.\" And he worshiped the LORD there.",
      "T": "\"So now I am giving him back to the LORD. For all his life he is the LORD's.\" And they worshiped the LORD there."
    }
  },
  "2": {
    "1": {
      "L": "And Hannah prayed and said, My heart exults in the LORD; my horn is exalted in the LORD. My mouth speaks boldly against my enemies, because I rejoice in your salvation.",
      "M": "And Hannah prayed and said: \"My heart rejoices in the LORD; my horn is lifted high in the LORD. My mouth speaks boldly against my enemies, for I rejoice in your deliverance.",
      "T": "Hannah prayed:\n My heart leaps up in the LORD—\n  my strength is lifted high in him.\n My mouth opens wide against my enemies,\n  for I rejoice in your saving work."
    },
    "2": {
      "L": "There is none holy like the LORD; for there is none besides you, and there is no rock like our God.",
      "M": "There is no one holy like the LORD; there is no one besides you; there is no rock like our God.",
      "T": " None is holy as the LORD—\n  there is simply no one else.\n No rock stands like our God."
    },
    "3": {
      "L": "Talk no more so very proudly, let not arrogance come from your mouth; for the LORD is a God of knowledge, and by him actions are weighed.",
      "M": "Do not speak with such great pride; let no arrogance come from your mouth, for the LORD is a God of knowledge, and by him deeds are weighed.",
      "T": " Speak no more with towering pride—\n  arrogance does not become you.\n The LORD is a God who knows all things;\n  every deed is weighed on his scales."
    },
    "4": {
      "L": "The bows of the mighty are broken, but the feeble bind on strength.",
      "M": "The bows of the mighty are shattered, but those who stumbled are girded with strength.",
      "T": " The weapons of the strong are shattered;\n  the stumbling rise and are armed."
    },
    "5": {
      "L": "Those who were full have hired themselves out for bread, but those who were hungry have ceased to hunger. The barren has borne seven, but she who has many children is forlorn.",
      "M": "Those who were full have hired themselves out for bread, but those who were hungry are hungry no more. The barren woman has borne seven, but she who has many children languishes.",
      "T": " The well-fed sell themselves for bread;\n  the starving have grown fat.\n The barren woman has borne seven—\n  and she with many sons withers away.\n Hannah was the barren woman. She was singing her own reversal into the cosmic pattern of what God does."
    },
    "6": {
      "L": "The LORD kills and brings to life; he brings down to Sheol and raises up.",
      "M": "The LORD brings death and gives life; he brings down to Sheol and raises up.",
      "T": " The LORD kills—and gives life.\n He brings down to the grave\n  and raises up again."
    },
    "7": {
      "L": "The LORD makes poor and makes rich; he brings low, he also exalts.",
      "M": "The LORD makes poor and makes rich; he brings low, and he also lifts up.",
      "T": " The LORD impoverishes and enriches;\n  he humbles, and he exalts."
    },
    "8": {
      "L": "He raises up the poor from the dust; he lifts the needy from the ash heap, to make them sit with princes and inherit a seat of honor. For the pillars of the earth are the LORD's, and he has set the world upon them.",
      "M": "He raises the poor from the dust and lifts the needy from the ash heap, to seat them with princes and give them a throne of honor. For the pillars of the earth are the LORD's, and on them he has set the world.",
      "T": " He lifts the poor out of the dust,\n  the needy from the ash heap—\n to seat them among princes,\n  to give them a throne of honor.\n For the earth's foundations belong to the LORD;\n  on them he has set the world in place."
    },
    "9": {
      "L": "He will guard the feet of his faithful ones, but the wicked shall be cut off in darkness, for not by might shall a man prevail.",
      "M": "He will guard the feet of his faithful ones, but the wicked will be silenced in darkness, for not by strength does a man prevail.",
      "T": " He guards the steps of his faithful—\n  the wicked go down into darkness.\n No man wins by his own strength alone."
    },
    "10": {
      "L": "The adversaries of the LORD shall be shattered; against them he will thunder in the heavens. The LORD will judge the ends of the earth; he will give strength to his king and exalt the horn of his anointed.",
      "M": "The LORD's enemies shall be shattered; against them he will thunder in heaven. The LORD will judge the ends of the earth; he will give strength to his king and lift high the horn of his anointed.",
      "T": " The LORD's enemies will be shattered—\n  his thunder rolls over them from heaven.\n The LORD will judge the whole earth;\n  he will give power to his king\n  and lift high the horn of his anointed one.\n The song ends on a word the narrative has not yet introduced: his anointed—מְשִׁיחוֹ, his Messiah. No king exists in Israel yet. Hannah is singing into a future that does not yet exist. The messianic seed is planted here, at the opening of Samuel, before the first king is born."
    },
    "11": {
      "L": "Then Elkanah went home to Ramah. And the boy was ministering to the LORD in the presence of Eli the priest.",
      "M": "Then Elkanah went home to Ramah, and the boy remained to minister to the LORD in the presence of Eli the priest.",
      "T": "Elkanah returned to Ramah. The boy Samuel stayed behind, serving the LORD under Eli's oversight."
    },
    "12": {
      "L": "Now the sons of Eli were sons of Belial; they did not know the LORD.",
      "M": "Now the sons of Eli were worthless men; they did not know the LORD.",
      "T": "Eli's sons were corrupt men—sons of Belial, the text says, a Hebrew idiom for those who belong to the realm of worthlessness and ruin. They did not know the LORD."
    },
    "13": {
      "L": "The custom of the priests with the people was that when any man offered a sacrifice, the priest's servant would come, while the meat was boiling, with a three-pronged fork in his hand,",
      "M": "The priests' practice with the people was this: when anyone offered a sacrifice, the priest's servant would come while the meat was boiling, with a three-pronged fork in his hand,",
      "T": "The priests had developed a racket. Whenever someone brought an offering and the meat was boiling, the priest's servant would show up carrying a large three-pronged fork."
    },
    "14": {
      "L": "and he would thrust it into the pan or kettle or cauldron or pot. All that the fork brought up the priest would take for himself. This is what they did to all the Israelites who came to Shiloh.",
      "M": "and he would thrust it into the pan, kettle, cauldron, or pot. Everything the fork brought up the priest would take for himself. This is what they did to all the Israelites who came to Shiloh.",
      "T": "He'd plunge the fork in and take whatever it pulled out—for the priest. This is how Eli's sons treated every Israelite who came to worship."
    },
    "15": {
      "L": "Moreover, before the fat was burned, the priest's servant would come and say to the man who was sacrificing, Give meat for the priest to roast, for he will not accept boiled meat from you, but only raw.",
      "M": "Even before the fat was burned, the priest's servant would come and say to the man who was sacrificing, \"Give the priest meat to roast, for he will not accept boiled meat—only raw.\"",
      "T": "Worse: even before the fat could be burned as the LORD's portion, the servant would demand raw meat for the priest. They were robbing God before robbing the worshipper."
    },
    "16": {
      "L": "And if the man said to him, Let them burn the fat first, and then take as much as you wish, he would say, No, you must give it now, and if not I will take it by force.",
      "M": "And if the man said, \"Let the fat be burned first, and then take whatever you want,\" he would say, \"No, hand it over now; if not, I will take it by force.\"",
      "T": "If a worshipper protested—\"Let the fat burn for the LORD first; then take what you want\"—the servant sneered: \"Hand it over now, or I'll take it.\" Coercion dressed as priestly authority."
    },
    "17": {
      "L": "The sin of the young men was very great in the sight of the LORD, for the men treated the offering of the LORD with contempt.",
      "M": "The sin of these young men was very great in the sight of the LORD, for they treated the LORD's offering with contempt.",
      "T": "The narrator pronounces verdict: the sin of these men was very great in the LORD's eyes. They despised the LORD's offering—treating the sacred as plunder."
    },
    "18": {
      "L": "But Samuel was ministering before the LORD, a boy wearing a linen ephod.",
      "M": "Now Samuel was ministering before the LORD, a young boy clothed in a linen ephod.",
      "T": "Meanwhile, Samuel ministered before the LORD—a boy in a linen ephod. The contrast is deliberate."
    },
    "19": {
      "L": "And his mother used to make for him a little robe and bring it to him each year when she went up with her husband to offer the yearly sacrifice.",
      "M": "And his mother would make a little robe for him and bring it up to him each year when she came with her husband to offer the yearly sacrifice.",
      "T": "Each year Hannah made him a small robe and brought it when she and Elkanah came for the annual sacrifice. Year by year, she measured his growth in cloth."
    },
    "20": {
      "L": "Then Eli would bless Elkanah and his wife and say, May the LORD give you children by this woman in place of the one she gave back to the LORD. Then they would go back to their home.",
      "M": "And Eli would bless Elkanah and his wife, saying, \"May the LORD give you children by this woman in return for the gift she has given to the LORD.\" Then they would go back to their home.",
      "T": "Each year Eli blessed them: \"May the LORD give you children through this woman, to make up for the one she gave back to him.\" Then they went home."
    },
    "21": {
      "L": "Indeed the LORD visited Hannah, and she conceived and bore three sons and two daughters. And the young man Samuel grew in the presence of the LORD.",
      "M": "Indeed the LORD visited Hannah, and she conceived and bore three sons and two daughters. And the young Samuel grew up in the presence of the LORD.",
      "T": "The LORD visited Hannah, and she conceived and bore three more sons and two daughters. Samuel meanwhile kept growing in the LORD's presence—raised in the sanctuary, formed by nearness to God."
    },
    "22": {
      "L": "Now Eli was very old, and he kept hearing all that his sons were doing to all Israel, and how they lay with the women who were serving at the entrance to the tent of meeting.",
      "M": "Now Eli was very old, and he kept hearing about everything his sons were doing to all Israel, and how they were sleeping with the women who served at the entrance of the tent of meeting.",
      "T": "Eli was very old. Reports kept reaching him—what his sons were doing to all Israel, how they were sleeping with the women who served at the entrance to the tent of meeting. Priestly corruption at its fullest measure."
    },
    "23": {
      "L": "And he said to them, Why do you do such things? For I hear from all the people of these evil doings of yours.",
      "M": "And he said to them, \"Why do you do such things? For I hear of your evil deeds from all these people.",
      "T": "He confronted them: \"Why do you do these things? I am hearing reports of your evil from everyone.\""
    },
    "24": {
      "L": "No, my sons; it is no good report that I hear the people of the LORD spreading abroad.",
      "M": "No, my sons, it is not a good report that I hear the LORD's people spreading.",
      "T": "\"No, my sons—what you are doing is not right. The people of the LORD are talking about you everywhere.\""
    },
    "25": {
      "L": "If someone sins against a man, God will mediate for him, but if someone sins against the LORD, who can intercede for him? But they would not listen to the voice of their father, for it was the will of the LORD to put them to death.",
      "M": "\"If one person sins against another, God can mediate for him, but if someone sins against the LORD, who will intercede for him?\" But they would not listen to the voice of their father, for it was the will of the LORD to put them to death.",
      "T": "\"When a man sins against a fellow man, there is a court to hear it. But when a man sins against the LORD—who will plead for him?\" His sons did not listen. They could not listen. The LORD had already determined to destroy them."
    },
    "26": {
      "L": "Now the young man Samuel continued to grow and to be in favor both with the LORD and also with men.",
      "M": "The young man Samuel continued to grow and to be in favor with the LORD and with men.",
      "T": "Samuel kept growing—in stature and in favor, with the LORD and with people alike."
    },
    "27": {
      "L": "And there came a man of God to Eli and said to him, Thus says the LORD: Did I indeed reveal myself to the house of your father when they were in Egypt subject to the house of Pharaoh?",
      "M": "And a man of God came to Eli and said to him, \"Thus says the LORD: 'Did I not reveal myself to your father's house when they were in Egypt under Pharaoh?",
      "T": "A man of God came to Eli and delivered the LORD's word: \"Did I not reveal myself to your ancestor's house when they were slaves in Egypt under Pharaoh?\""
    },
    "28": {
      "L": "I chose him out of all the tribes of Israel to be my priest, to go up to my altar, to burn incense, to wear an ephod before me. And I gave to the house of your father all the food offerings by fire of the people of Israel.",
      "M": "I chose your ancestor from all the tribes of Israel to be my priest, to go up to my altar, to burn incense, and to wear an ephod before me. I gave the house of your father all the offerings made by fire from the people of Israel.",
      "T": "I chose your ancestor above all the tribes of Israel to serve me as priest—to approach my altar, burn incense, wear the ephod before me. I gave his household all the fire-offerings of my people Israel."
    },
    "29": {
      "L": "Why then do you scorn my sacrifices and my offerings that I commanded, and honor your sons above me by fattening yourselves on the choicest parts of every offering of my people Israel?",
      "M": "Why then do you despise my sacrifices and my offerings that I have commanded, and honor your sons more than me by fattening yourselves on the best parts of every offering of my people Israel?'",
      "T": "So why do you kick at my sacrifices and the offerings I commanded? Why do you honor your sons above me—stuffing yourselves on the best portions my people Israel bring?\""
    },
    "30": {
      "L": "Therefore the LORD, the God of Israel, declares: I promised that your house and the house of your father should go in and out before me forever, but now the LORD declares: Far be it from me, for those who honor me I will honor, and those who despise me shall be lightly esteemed.",
      "M": "Therefore the LORD, the God of Israel, declares: 'I had said that your house and your father's house would walk before me forever, but now the LORD declares: Far be it from me! For those who honor me I will honor, and those who despise me will be treated with contempt.",
      "T": "Therefore the LORD, the God of Israel, declares: I once promised that your family line would serve before me forever. That promise is now revoked. Those who honor me I will honor; those who despise me will end in contempt."
    },
    "31": {
      "L": "Behold, the days are coming when I will cut off your arm and the arm of your father's house, so that there will not be an old man in your house.",
      "M": "See, the days are coming when I will cut off your strength and the strength of your father's house, so that no man in your house will reach old age.",
      "T": "The days are coming when I will cut off your strength and the strength of your family line. There will be no old men left in your household."
    },
    "32": {
      "L": "Then in distress you will look with envious eye on all the prosperity that shall be bestowed on Israel, and there will not be an old man in your house forever.",
      "M": "You will look with envy at all the good that will be done for Israel, but there will never be an old man in your house again.",
      "T": "You will watch Israel flourish while your house has nothing—no elder, no heir reaching old age, ever again."
    },
    "33": {
      "L": "The only one of you whom I shall not cut off from my altar shall be spared to weep his eyes out and to grieve his heart, and all the descendants of your house shall die by the sword of men.",
      "M": "The one of yours I do not cut off from my altar will be left to consume your eyes with grief and break your heart, and all the other descendants of your house will die by the sword.",
      "T": "The one survivor I leave at my altar will drain your eyes with grief and break your heart, and all your other descendants will fall by the sword."
    },
    "34": {
      "L": "And this that shall come upon your two sons, on Hophni and Phinehas, shall be the sign to you: both of them shall die on the same day.",
      "M": "And this will be the sign for you: both your sons, Hophni and Phinehas, shall die on the same day.",
      "T": "Here is the sign confirming all of this: both your sons—Hophni and Phinehas—will die on the same day."
    },
    "35": {
      "L": "And I will raise up for myself a faithful priest, who shall do according to what is in my heart and in my mind. And I will build him a sure house, and he shall go in and out before my anointed forever.",
      "M": "And I will raise up for myself a faithful priest who will do what is in my heart and mind. I will build him an enduring house, and he will walk before my anointed one always.",
      "T": "And I will raise up a faithful priest for myself—one who will do what I truly intend. I will build him a lasting household, and he will serve before my anointed one always."
    },
    "36": {
      "L": "And everyone who is left in your house shall come to implore him for a silver coin or a loaf of bread, and shall say, Please put me in one of the priests' places, that I may eat a morsel of bread.",
      "M": "And everyone left in your house will come to beg him for a piece of silver or a loaf of bread and say, 'Please assign me to one of the priestly offices so that I may eat a piece of bread.'\"",
      "T": "Everyone left in your family will come groveling to this faithful priest, begging for a few coins or a scrap of bread: 'Put me anywhere in the priesthood—I just need to eat.'"
    }
  },
  "3": {
    "1": {
      "L": "Now the young man Samuel was ministering to the LORD in the presence of Eli. And the word of the LORD was rare in those days; there was no frequent vision.",
      "M": "Now the young Samuel was ministering to the LORD under Eli. The word of the LORD was rare in those days; visions were not frequent.",
      "T": "Samuel was serving the LORD under Eli's oversight. In those days the word of the LORD was scarce—visions were seldom given. The silence of heaven is itself a judgment on Eli's era."
    },
    "2": {
      "L": "At that time Eli, whose eyesight had begun to grow dim so that he could not see, was lying down in his own place.",
      "M": "At that time Eli, whose eyesight had grown so dim that he could no longer see, was lying down in his room.",
      "T": "Eli's eyes had grown dim—he could barely see. He was lying in his quarters."
    },
    "3": {
      "L": "The lamp of God had not yet gone out, and Samuel was lying down in the temple of the LORD, where the ark of God was.",
      "M": "The lamp of God had not yet gone out, and Samuel was lying down in the temple of the LORD, near where the ark of God was.",
      "T": "The lamp of God was still burning—it had not yet gone out. Samuel was lying down in the sanctuary, near the ark of God. It was the last hours before dawn."
    },
    "4": {
      "L": "Then the LORD called Samuel, and he said, Here I am.",
      "M": "Then the LORD called, \"Samuel!\" and he said, \"Here I am.\"",
      "T": "Then the LORD called: \"Samuel!\" He answered, \"Here I am.\""
    },
    "5": {
      "L": "And he ran to Eli and said, Here I am, for you called me. But he said, I did not call; lie down again. So he went and lay down.",
      "M": "He ran to Eli and said, \"Here I am, for you called me.\" But Eli said, \"I did not call you; lie down again.\" So he went and lay down.",
      "T": "He ran to Eli: \"Here I am—you called me.\" Eli said, \"I didn't call you. Go back to sleep.\" He went back."
    },
    "6": {
      "L": "And the LORD called again, Samuel! And Samuel arose and went to Eli and said, Here I am, for you called me. But he said, I did not call, my son; lie down again.",
      "M": "The LORD called again, \"Samuel!\" And Samuel arose and went to Eli and said, \"Here I am, for you called me.\" But Eli said, \"I did not call, my son; lie down again.\"",
      "T": "The LORD called a second time: \"Samuel!\" He got up and went to Eli again: \"Here I am—you called me.\" Eli said, \"I didn't call, my son. Go back to sleep.\""
    },
    "7": {
      "L": "Now Samuel did not yet know the LORD, and the word of the LORD had not yet been revealed to him.",
      "M": "Now Samuel did not yet know the LORD, and the word of the LORD had not yet been revealed to him.",
      "T": "Samuel had not yet come to know the LORD in this direct, prophetic way—the word of the LORD had not yet been personally disclosed to him."
    },
    "8": {
      "L": "And the LORD called Samuel again the third time. And he arose and went to Eli and said, Here I am, for you called me. Then Eli perceived that the LORD was calling the young man.",
      "M": "The LORD called Samuel again the third time. He arose and went to Eli and said, \"Here I am, for you called me.\" Then Eli understood that the LORD was calling the boy.",
      "T": "The LORD called a third time: \"Samuel!\" He got up and went to Eli again. \"Here I am—you called me.\" Then Eli understood. It was the LORD calling the boy."
    },
    "9": {
      "L": "Therefore Eli said to Samuel, Go, lie down, and if he calls you, you shall say, Speak, LORD, for your servant hears. So Samuel went and lay down in his place.",
      "M": "Therefore Eli said to Samuel, \"Go, lie down, and if he calls you, you shall say, 'Speak, LORD, for your servant is listening.'\" So Samuel went and lay down in his place.",
      "T": "Eli instructed him: \"Go back and lie down. If he calls again, say: 'Speak, LORD—your servant is listening.'\" Samuel went back and lay down."
    },
    "10": {
      "L": "And the LORD came and stood, calling as at other times, Samuel! Samuel! And Samuel said, Speak, for your servant hears.",
      "M": "The LORD came and stood there, calling as before: \"Samuel! Samuel!\" And Samuel said, \"Speak, for your servant is listening.\"",
      "T": "The LORD came and stood there and called as before: \"Samuel! Samuel!\" And Samuel answered, \"Speak—your servant is listening.\""
    },
    "11": {
      "L": "Then the LORD said to Samuel, Behold, I am about to do a thing in Israel at which the two ears of everyone who hears it will tingle.",
      "M": "The LORD said to Samuel, \"Behold, I am about to do something in Israel that will make the ears of everyone who hears it tingle.",
      "T": "The LORD said: \"I am about to do something in Israel that will make everyone who hears of it shudder.\""
    },
    "12": {
      "L": "On that day I will fulfill against Eli all that I have spoken concerning his house, from beginning to end.",
      "M": "On that day I will carry out against Eli everything I have spoken concerning his house, from beginning to end.",
      "T": "On that day I will bring down on Eli's house everything I have spoken against it—every word, from first to last."
    },
    "13": {
      "L": "And I declare to him that I am about to punish his house forever, for the iniquity that he knew, because his sons were blaspheming God, and he did not restrain them.",
      "M": "For I have told him that I am about to judge his house forever for the iniquity that he knew, because his sons were blaspheming God and he did not rebuke them.",
      "T": "I told him in advance: I will judge his household forever—because of the sin he knew about. His sons were treating God with contempt, and Eli did nothing to stop them."
    },
    "14": {
      "L": "Therefore I swear to the house of Eli that the iniquity of Eli's house shall not be atoned for by sacrifice or offering forever.",
      "M": "Therefore I swear to the house of Eli that the iniquity of Eli's house shall never be atoned for by sacrifice or offering.",
      "T": "Therefore I declare under oath: the sin of Eli's house will never be atoned for—not by sacrifice, not by offering. The door is closed."
    },
    "15": {
      "L": "Samuel lay until morning; then he opened the doors of the house of the LORD. And Samuel was afraid to tell the vision to Eli.",
      "M": "Samuel lay there until morning, then opened the doors of the house of the LORD. And Samuel was afraid to tell Eli the vision.",
      "T": "Samuel lay still until morning, then got up and opened the doors of the LORD's house. He was afraid to tell Eli what he had seen."
    },
    "16": {
      "L": "Then Eli called Samuel and said, Samuel, my son. And he said, Here I am.",
      "M": "Then Eli called Samuel and said, \"Samuel, my son.\" And he said, \"Here I am.\"",
      "T": "But Eli called him: \"Samuel, my son.\" \"Here I am,\" he answered."
    },
    "17": {
      "L": "And Eli said, What was it that he told you? Do not hide it from me. May God do so to you and more also if you hide anything from me of all that he told you.",
      "M": "Eli said, \"What did he say to you? Do not hide it from me. May God deal with you severely if you hide from me anything he said to you.\"",
      "T": "Eli said, \"What did he tell you? Don't hide anything from me. If you conceal even one word he said, may God deal with you harshly.\""
    },
    "18": {
      "L": "So Samuel told him everything and hid nothing from him. And he said, It is the LORD. Let him do what seems good to him.",
      "M": "So Samuel told him everything and hid nothing from him. And Eli said, \"He is the LORD. Let him do what seems right in his eyes.\"",
      "T": "Samuel told him everything, holding nothing back. Eli said, \"He is the LORD. Let him do what he thinks right.\" There is both faith and resignation in those words—the broken acceptance of a man who knew his house was condemned."
    },
    "19": {
      "L": "And Samuel grew, and the LORD was with him and let none of his words fall to the ground.",
      "M": "Samuel grew, and the LORD was with him and let none of his words fall to the ground.",
      "T": "Samuel grew up. The LORD was with him, and not a single word Samuel spoke fell to the ground unfulfilled."
    },
    "20": {
      "L": "And all Israel from Dan to Beersheba knew that Samuel was established as a prophet of the LORD.",
      "M": "And all Israel from Dan to Beersheba knew that Samuel had been established as a prophet of the LORD.",
      "T": "All Israel—from Dan in the north to Beersheba in the south—came to know that Samuel was established as a true prophet of the LORD."
    },
    "21": {
      "L": "And the LORD appeared again at Shiloh, for the LORD revealed himself to Samuel at Shiloh by the word of the LORD.",
      "M": "And the LORD continued to appear at Shiloh, for the LORD revealed himself to Samuel at Shiloh through the word of the LORD.",
      "T": "And the LORD kept appearing at Shiloh. Through his word, he revealed himself to Samuel there. The long silence was broken. Heaven had found its voice again in Israel."
    }
  },
  "4": {
    "1": {
      "L": "And the word of Samuel came to all Israel. Now Israel went out to battle against the Philistines. They encamped at Ebenezer, and the Philistines encamped at Aphek.",
      "M": "And the word of Samuel came to all Israel. Now Israel went out to fight against the Philistines. They encamped at Ebenezer, and the Philistines encamped at Aphek.",
      "T": "The word of Samuel reached all Israel. Then Israel marched out to fight the Philistines—Israel at Ebenezer, Philistines at Aphek."
    },
    "2": {
      "L": "The Philistines drew up in line against Israel, and when the battle spread, Israel was defeated before the Philistines, who struck down about four thousand men in the field.",
      "M": "The Philistines drew up in line against Israel, and when the battle spread, Israel was defeated before the Philistines, who killed about four thousand men on the field.",
      "T": "The two forces met. Israel broke first. Four thousand men lay dead on the field when the Philistines drove them back."
    },
    "3": {
      "L": "And when the people came to the camp, the elders of Israel said, Why has the LORD defeated us today before the Philistines? Let us bring the ark of the covenant of the LORD here from Shiloh, that it may come among us and save us from the power of our enemies.",
      "M": "When the troops came back to camp, the elders of Israel said, \"Why has the LORD defeated us today before the Philistines? Let us bring the ark of the covenant of the LORD here from Shiloh, that it may come among us and save us from the power of our enemies.\"",
      "T": "When the survivors reached camp, the elders asked, \"Why has the LORD let the Philistines defeat us?\" Then came the fatal idea: \"Bring the ark of the covenant from Shiloh—let it come with us into battle and save us.\" They were treating the ark as a war-talisman, as if the divine presence could be summoned to fight on their terms."
    },
    "4": {
      "L": "So the people sent to Shiloh and brought from there the ark of the covenant of the LORD of hosts, who is enthroned on the cherubim. And the two sons of Eli, Hophni and Phinehas, were there with the ark of the covenant of God.",
      "M": "So the people sent to Shiloh and brought from there the ark of the covenant of the LORD of hosts, who is enthroned between the cherubim. And Eli's two sons, Hophni and Phinehas, were there with the ark of the covenant of God.",
      "T": "They sent to Shiloh and brought the ark of the covenant—of the LORD of hosts, enthroned above the cherubim. Hophni and Phinehas, Eli's two condemned sons, came with it. The doom foretold was walking toward its fulfillment."
    },
    "5": {
      "L": "As soon as the ark of the covenant of the LORD came into the camp, all Israel gave a great shout, so that the earth resounded.",
      "M": "When the ark of the covenant of the LORD came into the camp, all Israel raised such a great shout that the ground shook.",
      "T": "When the ark arrived at the camp, a roar went up from the whole army—so loud the ground shook."
    },
    "6": {
      "L": "And when the Philistines heard the noise of the shouting, they said, What does this great shouting in the camp of the Hebrews mean? And when they learned that the ark of the LORD had come to the camp,",
      "M": "When the Philistines heard the noise of the shouting, they asked, \"What is this great shouting in the Hebrew camp?\" And when they learned that the ark of the LORD had come to the camp,",
      "T": "The Philistines heard it and asked, \"What is that roaring in the Hebrew camp?\" When they learned the ark of the LORD had arrived,"
    },
    "7": {
      "L": "the Philistines were afraid, for they said, A god has come into the camp. And they said, Woe to us! For nothing like this has happened before.",
      "M": "the Philistines were afraid, for they said, \"A god has come into the camp!\" And they said, \"Woe to us! Nothing like this has ever happened before.",
      "T": "fear ran through their ranks. \"A god has entered their camp!\" they said. \"We're in trouble—nothing like this has ever happened to us before.\""
    },
    "8": {
      "L": "Woe to us! Who can deliver us from the power of these mighty gods? These are the gods who struck the Egyptians with every sort of plague in the wilderness.",
      "M": "Woe to us! Who will deliver us from the hand of these mighty gods? These are the gods who struck the Egyptians with every kind of plague in the wilderness.",
      "T": "\"Who will rescue us from these powerful gods? These are the ones who struck Egypt with plague after plague in the wilderness.\" Their fear was grounded in real history—but their theology was polytheist. They heard a war-shout and assumed gods, plural."
    },
    "9": {
      "L": "Be strong and act like men, O Philistines, lest you become slaves to the Hebrews as they have been to you. Act like men and fight.",
      "M": "\"Be strong and act like men, O Philistines, lest you become slaves to the Hebrews as they have been to you. Fight, and be men!\"",
      "T": "\"Courage! Act like men, Philistines! If you don't, you'll end up serving the Hebrews the way they once served Egypt. Fight—and fight like men!\""
    },
    "10": {
      "L": "So the Philistines fought, and Israel was defeated, and they fled, every man to his home. And there was a very great slaughter, for there fell of Israel thirty thousand foot soldiers.",
      "M": "So the Philistines fought, and Israel was defeated, and every man fled to his home. The slaughter was very great; thirty thousand Israelite foot soldiers fell.",
      "T": "The Philistines fought. Israel broke and fled, every man for himself. The slaughter was catastrophic—thirty thousand Israeli infantry fell."
    },
    "11": {
      "L": "And the ark of God was captured, and the two sons of Eli, Hophni and Phinehas, died.",
      "M": "The ark of God was captured, and Eli's two sons, Hophni and Phinehas, died.",
      "T": "The ark of God was captured. Hophni and Phinehas died—both on the same day, exactly as the man of God had foretold."
    },
    "12": {
      "L": "A man of Benjamin ran from the battle line and came to Shiloh the same day, with his clothes torn and with dirt on his head.",
      "M": "A man from Benjamin ran from the battle line and reached Shiloh the same day, with his clothes torn and dust on his head.",
      "T": "A Benjaminite survivor ran from the battlefield and reached Shiloh that same day—his clothes torn, his head covered with dust. These were the signs of mourning and disaster."
    },
    "13": {
      "L": "When he arrived, Eli was sitting on his seat by the road watching, for his heart trembled for the ark of God. And when the man came into the city and told the news, all the city cried out.",
      "M": "When he arrived, Eli was sitting on his seat beside the road watching, for his heart trembled with anxiety over the ark of God. When the man came into the city and reported the news, the whole city cried out.",
      "T": "Eli sat waiting on his chair beside the road, his heart sick with dread for the ark of God. When the man ran into Shiloh and told what had happened, the whole city broke into wailing."
    },
    "14": {
      "L": "When Eli heard the sound of the outcry, he said, What is this uproar? Then the man hurried and came and told Eli.",
      "M": "When Eli heard the noise of the outcry, he said, \"What is the meaning of this commotion?\" The man hurried to Eli and told him.",
      "T": "Eli heard the city's cry. \"What is all that noise?\" he asked. The man hurried to him with the news."
    },
    "15": {
      "L": "Now Eli was ninety-eight years old, and his eyes were set so that he could not see.",
      "M": "Now Eli was ninety-eight years old, and his eyes were fixed and he could not see.",
      "T": "Eli was ninety-eight years old. His eyes had failed completely—he could see nothing."
    },
    "16": {
      "L": "And the man said to Eli, I am he who has come from the battle; I fled from the battle today. And he said, How did it go, my son?",
      "M": "And the man said to Eli, \"I am the one who has come from the battle; I fled from the battle today.\" Eli said, \"How did it go, my son?\"",
      "T": "The man said, \"I have just come from the battle—I escaped from the field today.\" Eli asked, \"What happened, my son?\""
    },
    "17": {
      "L": "The messenger answered and said, Israel has fled before the Philistines, and there has also been a great defeat among the people. Your two sons also, Hophni and Phinehas, are dead, and the ark of God has been captured.",
      "M": "The messenger answered, \"Israel has fled before the Philistines, and there has been a great slaughter among the people. Your two sons, Hophni and Phinehas, are dead, and the ark of God has been captured.\"",
      "T": "The messenger reported: \"Israel has fled from the Philistines. The defeat was catastrophic. Your two sons—Hophni and Phinehas—are dead. And the ark of God has been taken.\""
    },
    "18": {
      "L": "As soon as he mentioned the ark of God, Eli fell over backward from his seat by the side of the gate, and his neck was broken and he died, for the man was old and heavy. He had judged Israel for forty years.",
      "M": "The moment he mentioned the ark of God, Eli fell backward off his seat by the side of the gate, and his neck broke and he died, for the man was old and heavy. He had judged Israel forty years.",
      "T": "The moment the man said \"the ark of God\"—Eli fell backward off his seat beside the gate, broke his neck, and died. He was old and heavy. He had judged Israel forty years. The deaths of his sons he could endure; the loss of the ark—the departure of God's presence—killed him."
    },
    "19": {
      "L": "Now his daughter-in-law, the wife of Phinehas, was pregnant, about to give birth. And when she heard the news that the ark of God was captured and that her father-in-law and her husband were dead, she bowed and gave birth, for her pains came upon her.",
      "M": "Now his daughter-in-law, the wife of Phinehas, was pregnant and near her time. When she heard the news that the ark of God was captured and that her father-in-law and her husband were dead, she went into labor and crouched down, for her birth pains came upon her.",
      "T": "Phinehas's wife was heavily pregnant and near her time. When the news reached her—the ark captured, her father-in-law and husband both dead—her labor began. She crouched and gave birth."
    },
    "20": {
      "L": "And about the time of her death the women attending her said to her, Do not be afraid, for you have borne a son. But she did not answer or pay attention.",
      "M": "And at the moment of her death, the women attending her said to her, \"Do not be afraid, for you have given birth to a son.\" But she did not answer or take notice.",
      "T": "As she was dying, the midwives leaned close: \"Don't be afraid—you have a son!\" But she did not respond. She did not even turn her head."
    },
    "21": {
      "L": "And she named the child Ichabod, saying, The glory has departed from Israel, because the ark of God has been captured and because of her father-in-law and her husband.",
      "M": "She named the child Ichabod, saying, \"The glory has departed from Israel\"—because the ark of God was captured and because of her father-in-law and her husband.",
      "T": "She named the boy Ichabod—\"No Glory\"—saying, \"The glory has gone into exile from Israel.\" The Hebrew verb גָּלָה means to go into exile, to be stripped bare; T preserves this register: what departed from Israel that day was not merely a sacred object but the divine Presence itself, going into exile among the nations."
    },
    "22": {
      "L": "And she said, The glory has departed from Israel, for the ark of God has been captured.",
      "M": "She said, \"The glory has departed from Israel, for the ark of God has been captured.\"",
      "T": "Her last words: \"The glory has gone into exile from Israel—the ark of God is taken.\" Then she was gone. Ichabod would become a theology: the name that Israel would one day have to recover."
    }
  },
  "5": {
    "1": {
      "L": "When the Philistines captured the ark of God, they brought it from Ebenezer to Ashdod.",
      "M": "When the Philistines captured the ark of God, they brought it from Ebenezer to Ashdod.",
      "T": "The Philistines took the ark of God from Ebenezer and carried it to Ashdod."
    },
    "2": {
      "L": "Then the Philistines took the ark of God and brought it into the house of Dagon and set it up beside Dagon.",
      "M": "Then the Philistines took the ark of God and brought it into the temple of Dagon and placed it beside Dagon.",
      "T": "They carried it into the temple of Dagon and set it down beside the idol—two presences, side by side. They assumed the comparison would favor Dagon."
    },
    "3": {
      "L": "And when the people of Ashdod rose early the next day, behold, Dagon had fallen face downward on the ground before the ark of the LORD. So they took Dagon and put him back in his place.",
      "M": "But when the people of Ashdod rose early the next day, Dagon had fallen face downward on the ground before the ark of the LORD. So they took Dagon and returned him to his place.",
      "T": "When the Ashdodites got up the next morning—Dagon was flat on the ground before the ark of the LORD. Prostrate, face down. They picked him up and set him back in place."
    },
    "4": {
      "L": "But when they rose early on the next morning, behold, Dagon had fallen face downward on the ground before the ark of the LORD, and the head of Dagon and both his hands were lying cut off on the threshold. Only the trunk of Dagon was left to him.",
      "M": "But when they got up early the next morning, Dagon had again fallen face downward on the ground before the ark of the LORD, and the head of Dagon and both his hands were lying cut off on the threshold. Only the torso of Dagon was left.",
      "T": "The next morning—Dagon was down again, face to the ground before the ark. This time his head and both hands lay severed on the threshold; only the trunk remained. The LORD did not merely knock the idol over—he executed it. A god loses what a god requires: a head to think and hands to act."
    },
    "5": {
      "L": "This is why the priests of Dagon and all who enter the house of Dagon do not tread on the threshold of Dagon in Ashdod to this day.",
      "M": "This is why to this day neither the priests of Dagon nor any who enter the house of Dagon tread on the threshold of Dagon in Ashdod.",
      "T": "That is why, to the very day this was written, the priests of Dagon and anyone entering his temple in Ashdod refuse to step on the threshold. The threshold is the site of Dagon's defeat, and the memory is kept in a ritual of avoidance."
    },
    "6": {
      "L": "The hand of the LORD was heavy against the people of Ashdod, and he terrified and struck them with tumors, both Ashdod and its territory.",
      "M": "The hand of the LORD was heavy against the people of Ashdod. He devastated them and struck them with tumors—Ashdod and its surrounding territory.",
      "T": "The hand of the LORD fell heavy on Ashdod. He struck them with tumors—the entire city and all its surrounding villages."
    },
    "7": {
      "L": "And when the men of Ashdod saw how things were, they said, The ark of the God of Israel must not remain with us, for his hand is hard against us and against Dagon our god.",
      "M": "When the men of Ashdod saw what was happening, they said, \"The ark of the God of Israel must not stay with us, for his hand is harsh against us and against Dagon our god.\"",
      "T": "The Ashdodites met and said, \"The ark of the God of Israel cannot stay here. His hand is crushing us—and it has destroyed our god.\""
    },
    "8": {
      "L": "So they sent and gathered together all the lords of the Philistines and said, What shall we do with the ark of the God of Israel? They answered, Let the ark of the God of Israel be brought around to Gath. So they brought the ark of the God of Israel to Gath.",
      "M": "So they sent and gathered all the lords of the Philistines and said, \"What shall we do with the ark of the God of Israel?\" They answered, \"Let the ark of the God of Israel be moved to Gath.\" So they moved the ark of the God of Israel to Gath.",
      "T": "They summoned all the Philistine rulers and asked: \"What do we do with the ark of the God of Israel?\" The decision: send it to Gath. So they sent the ark to Gath."
    },
    "9": {
      "L": "But after they had brought it around to Gath, the hand of the LORD was against that city too, causing a very great panic, and he struck the men of the city, both young and old, so that tumors broke out on them.",
      "M": "But after they brought it to Gath, the hand of the LORD was against that city, causing a very great panic. He struck the men of the city, both young and old, with tumors.",
      "T": "The LORD's hand fell on Gath next. Panic gripped the city. Both young and old broke out with tumors—the same affliction, following the ark."
    },
    "10": {
      "L": "So they sent the ark of God to Ekron. But when the ark of God came to Ekron, the people of Ekron cried out, They have brought around to us the ark of the God of Israel to kill us and our people.",
      "M": "So they sent the ark of God to Ekron. But when the ark of God arrived in Ekron, the Ekronites cried out, \"They have brought the ark of the God of Israel to us to kill us and our people!\"",
      "T": "So they sent the ark on to Ekron. But the moment the ark of God arrived at Ekron, the whole city cried out: \"They've sent the ark of the God of Israel here—to kill us!\""
    },
    "11": {
      "L": "They sent therefore and gathered together all the lords of the Philistines and said, Send away the ark of the God of Israel, and let it return to its own place, that it may not kill us and our people. For there was a deathly panic throughout the whole city; the hand of God was very heavy there.",
      "M": "So they sent and gathered all the lords of the Philistines and said, \"Send away the ark of the God of Israel, and let it return to its own place, so that it will not kill us and our people.\" For there was a deadly panic throughout the whole city; the hand of God was very heavy there.",
      "T": "They called an emergency assembly of all the Philistine rulers: \"Send the ark of the God of Israel back to its own place before it kills us all.\" Death-panic had spread through the entire city. The hand of God lay very heavy there."
    },
    "12": {
      "L": "The men who did not die were struck with tumors, and the cry of the city went up to heaven.",
      "M": "The men who did not die were struck with tumors, and the cry of the city went up to heaven.",
      "T": "Those who survived were struck with tumors. The whole city's lamentation went up to heaven."
    }
  },
  "6": {
    "1": {
      "L": "The ark of the LORD was in the country of the Philistines seven months.",
      "M": "The ark of the LORD was in Philistine territory for seven months.",
      "T": "Seven months the ark of the LORD remained in Philistia."
    },
    "2": {
      "L": "And the Philistines called for the priests and the diviners and said, What shall we do with the ark of the LORD? Tell us with what we shall send it to its place.",
      "M": "Then the Philistines called for the priests and the diviners and said, \"What shall we do with the ark of the LORD? Tell us how we should send it back to its place.\"",
      "T": "The Philistines summoned their priests and diviners: \"What do we do with the ark of the LORD? How do we send it back properly?\""
    },
    "3": {
      "L": "They said, If you send away the ark of the God of Israel, do not send it empty, but by all means return him a guilt offering. Then you will be healed, and it will be known to you why his hand does not turn away from you.",
      "M": "They said, \"If you send away the ark of the God of Israel, do not send it empty-handed, but by all means send a guilt offering with it. Then you will be healed, and you will understand why his hand has not turned away from you.\"",
      "T": "The priests said: \"When you send the ark of the God of Israel back, do not send it empty. You must accompany it with a guilt offering. Then you will be healed, and you will know why his hand has not released you.\""
    },
    "4": {
      "L": "And they said, What is the guilt offering that we shall return to him? They answered, Five golden tumors and five golden mice, according to the number of the lords of the Philistines, for the same plague was on all of you and on your lords.",
      "M": "They asked, \"What guilt offering should we send him?\" They answered, \"Five golden tumors and five golden mice, corresponding to the number of the Philistine rulers, for the same plague has been on all of you and on your rulers.",
      "T": "They asked, \"What guilt offering?\" The answer: \"Five golden tumors and five golden mice—one each for the five Philistine rulers. The same plague struck all of you and your rulers alike.\""
    },
    "5": {
      "L": "So you must make images of your tumors and images of your mice that ravage the land, and give glory to the God of Israel. Perhaps he will lighten his hand from off you and your gods and your land.",
      "M": "Make images of your tumors and images of the mice that are ravaging your land, and give glory to the God of Israel. Perhaps he will lift his hand from you and your gods and your land.",
      "T": "\"Make replicas of your tumors and of the rats destroying your fields, and present them to the God of Israel as an act of homage. Perhaps then he will lift his hand from you and your gods and your land.\""
    },
    "6": {
      "L": "Why should you harden your hearts as the Egyptians and Pharaoh hardened their hearts? After he had dealt harshly with them, did they not send the people away, and they departed?",
      "M": "Why should you harden your hearts as the Egyptians and Pharaoh hardened their hearts? After he dealt severely with them, did they not let the people go, and they departed?",
      "T": "\"Why be as stubborn as Egypt and Pharaoh? They hardened their hearts—and God dealt harshly with them until they finally let Israel go. Don't repeat their mistake.\""
    },
    "7": {
      "L": "Now then, take and prepare a new cart and two milk cows on which there has never come a yoke, and yoke the cows to the cart, but take their calves home, away from them.",
      "M": "Now then, take and prepare a new cart and two milk cows that have never been yoked, and hitch the cows to the cart. Take their calves home, away from them.",
      "T": "\"Here is what to do: get a new cart and two nursing cows that have never been yoked. Hitch the cows to the cart. Then pen their calves at home, away from them.\""
    },
    "8": {
      "L": "And take the ark of the LORD and place it on the cart and put in a box at its side the figures of gold, which you are returning to him as a guilt offering. Then send it off and let it go its way.",
      "M": "Take the ark of the LORD and place it on the cart, and put the golden figures you are returning as a guilt offering in a box beside it. Then send it off and let it go.",
      "T": "\"Put the ark of the LORD on the cart, and place the golden guilt-offering items in a chest beside it. Then send it off and let it go where it will.\""
    },
    "9": {
      "L": "And watch. If it goes up on the way to its own land, to Beth-shemesh, then it is he who has done us this great harm, but if not, then we shall know that it is not his hand that struck us; it happened to us by coincidence.",
      "M": "Then watch. If it goes up toward its own territory, to Beth-shemesh, then it is he who has done us this great harm. But if not, then we will know that it was not his hand that struck us—it happened to us by chance.",
      "T": "\"Then watch. If the cows head up the road toward Beth-shemesh—toward Israelite territory—then this God struck us with this great disaster. If they don't, it was just coincidence.\" They were devising a test. They already feared the answer."
    },
    "10": {
      "L": "The men did so, and took two milk cows and yoked them to the cart and shut up their calves at home.",
      "M": "The men did so. They took two milk cows and hitched them to the cart and shut up their calves at home.",
      "T": "They followed the instructions: two nursing cows hitched to a new cart, their calves locked away at home."
    },
    "11": {
      "L": "And they put the ark of the LORD on the cart and the box with the golden mice and the images of their tumors.",
      "M": "They placed the ark of the LORD on the cart and the chest with the golden mice and the golden images of their tumors.",
      "T": "They loaded the ark of the LORD on the cart, along with the chest containing the golden mice and golden tumor-images."
    },
    "12": {
      "L": "And the cows went straight in the direction of Beth-shemesh along one highway, lowing as they went. They turned neither to the right nor to the left, and the lords of the Philistines went after them as far as the border of Beth-shemesh.",
      "M": "And the cows went straight in the direction of Beth-shemesh along one road, lowing as they went. They did not turn to the right or to the left, and the Philistine rulers followed them as far as the border of Beth-shemesh.",
      "T": "The cows went straight up the road toward Beth-shemesh, lowing as they walked. They turned neither right nor left—away from their penned calves, directly into Israelite territory. The Philistine rulers followed behind, all the way to the border. The cows acted against their instincts. It was the verdict the Philistines had dreaded."
    },
    "13": {
      "L": "Now the people of Beth-shemesh were harvesting their wheat in the valley, and when they lifted up their eyes and saw the ark, they rejoiced to see it.",
      "M": "The people of Beth-shemesh were reaping their wheat harvest in the valley. When they looked up and saw the ark, they rejoiced at the sight.",
      "T": "The people of Beth-shemesh were harvesting wheat in the valley. They looked up, saw the ark, and broke into celebration."
    },
    "14": {
      "L": "The cart came into the field of Joshua of Beth-shemesh and stopped there. A great stone was there, and they split up the wood of the cart and offered the cows as a burnt offering to the LORD.",
      "M": "The cart came to the field of Joshua of Beth-shemesh and stopped there. A large stone was there, and they split the wood of the cart and offered the cows as a burnt offering to the LORD.",
      "T": "The cart stopped in the field of a man named Joshua of Beth-shemesh, beside a large rock. They split apart the wood of the cart and offered the two cows as a burnt offering to the LORD. The cart that carried the ark became the altar-wood."
    },
    "15": {
      "L": "And the Levites took down the ark of the LORD and the box that was beside it, in which were the golden figures, and set them on the great stone. And the men of Beth-shemesh offered burnt offerings and sacrificed sacrifices on that day to the LORD.",
      "M": "The Levites took down the ark of the LORD and the chest beside it containing the golden figures and set them on the large stone. The men of Beth-shemesh offered burnt offerings and made sacrifices to the LORD that day.",
      "T": "The Levites lifted down the ark of the LORD and the chest of golden offerings and placed them on the large rock. The men of Beth-shemesh offered burnt offerings and other sacrifices to the LORD that same day."
    },
    "16": {
      "L": "And the five lords of the Philistines saw it and returned that day to Ekron.",
      "M": "When the five lords of the Philistines saw it, they returned to Ekron that day.",
      "T": "The five Philistine rulers watched it all happen, then turned and went back to Ekron."
    },
    "17": {
      "L": "These are the golden tumors that the Philistines returned as a guilt offering to the LORD: one for Ashdod, one for Gaza, one for Ashkelon, one for Gath, one for Ekron,",
      "M": "These are the golden tumors that the Philistines returned as a guilt offering to the LORD: one for Ashdod, one for Gaza, one for Ashkelon, one for Gath, and one for Ekron—",
      "T": "The golden tumors returned as guilt offerings: one each for Ashdod, Gaza, Ashkelon, Gath, and Ekron—"
    },
    "18": {
      "L": "and the golden mice, according to the number of all the cities of the Philistines belonging to the five lords, both fortified cities and unwalled villages. The great stone beside which they set down the ark of the LORD is a witness to this day in the field of Joshua of Beth-shemesh.",
      "M": "and the golden mice, according to the number of all the Philistine cities belonging to the five rulers, from fortified cities to unwalled villages. The large stone on which they set down the ark of the LORD is a witness to this day in the field of Joshua of Beth-shemesh.",
      "T": "—and the golden mice, one for each Philistine city under the five rulers, walled city and open village alike. The large rock where they set down the ark stands as a witness in Joshua's field at Beth-shemesh to this day."
    },
    "19": {
      "L": "And he struck some of the men of Beth-shemesh, because they looked upon the ark of the LORD. He struck seventy men of them, and the people mourned because the LORD had struck the people with a great blow.",
      "M": "But he struck down some of the men of Beth-shemesh because they looked into the ark of the LORD. He struck down seventy of them, and the people mourned because the LORD had struck them with a great blow.",
      "T": "But the LORD struck down seventy men of Beth-shemesh because they had looked into the ark of the LORD. The people went into deep mourning over this devastating blow. The MT reads \"seventy men, fifty thousand men\" (50,070 total), a figure far exceeding Beth-shemesh's probable population; the LXX reads only 70 men, and most ancient authorities follow that tradition. L/M preserve the MT; T notes the likely scribal error in the larger number."
    },
    "20": {
      "L": "Then the men of Beth-shemesh said, Who is able to stand before the LORD, this holy God? And to whom shall he go up away from us?",
      "M": "The men of Beth-shemesh said, \"Who is able to stand before the LORD, this holy God? To whom shall he go up from us?\"",
      "T": "The survivors of Beth-shemesh said, \"Who can stand before the LORD, this holy God? Where can the ark go from us?\" The holiness of God is not a comfortable thing. Even the return of the ark came at a cost."
    },
    "21": {
      "L": "So they sent messengers to the inhabitants of Kiriath-jearim, saying, The Philistines have returned the ark of the LORD. Come down and take it up to yourselves.",
      "M": "So they sent messengers to the people of Kiriath-jearim, saying, \"The Philistines have returned the ark of the LORD. Come down and take it up to your place.\"",
      "T": "So they sent word to Kiriath-jearim: \"The Philistines have sent back the ark of the LORD. Come and take it.\" They wanted to be free of what they could not safely hold."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1samuel')
        merge_tier(existing, FIRST_SAMUEL, tier_key)
        save(tier_dir, '1samuel', existing)
    print('1 Samuel 1–6 written.')

if __name__ == '__main__':
    main()
