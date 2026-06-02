"""
MKT Genesis chapters 26–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-genesis-26-30.py

Translation principles applied:
- H3068 יהוה → "the LORD" (all tiers; small-caps convention)
- H430 אֱלֹהִים → "God" (grammatically plural, context-singular)
- H2617 חֶסֶד → "steadfast love" (L), "unfailing love" (M), "covenant faithfulness" (T)
- H1285 בְּרִית → "covenant" (all tiers)
- H5315 נֶפֶשׁ → context-driven: "soul"/"self"/"life"/"being"
- H7307 רוּחַ → context-driven (not present in these chapters)
- פַּחַד יִצְחָק (31:42,53) → "the Fear of Isaac" (L), "the Awe of Isaac" (M/T) — a divine title
- סֻלָּם (28:12) → "stairway" not "ladder" (ANE ziggurat ramp; sets up John 1:51)
- יִשְׂרָאֵל (32:28) → T tier glosses the etymology "One Who Strives with God"
- פְּנִיאֵל (32:30) → T tier glosses "Face of God"
- Blessings (27:27-29, 27:39-40) rendered as verse with line breaks
- Honor-shame dynamics noted in speech patterns (ch. 27, 33, 34)
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

GENESIS = {
  "26": {
    "1": {
      "L": "Now there was a famine in the land, besides the former famine that was in the days of Abraham. And Isaac went to Gerar to Abimelech king of the Philistines.",
      "M": "Now there was a famine in the land—besides the earlier famine in Abraham's time—and Isaac went to Abimelech king of the Philistines in Gerar.",
      "T": "A famine struck the land—not the one in Abraham's day, but a new one—and Isaac traveled to Gerar, to the Philistine king Abimelech."
    },
    "2": {
      "L": "And the LORD appeared to him and said, 'Do not go down to Egypt; dwell in the land of which I shall tell you.'",
      "M": "The LORD appeared to Isaac and said, 'Do not go down to Egypt; live in the land where I tell you to live.'",
      "T": "The LORD appeared to Isaac and said, 'Do not go down to Egypt. Stay in the land I will show you.'"
    },
    "3": {
      "L": "'Sojourn in this land, and I will be with you and will bless you, for to you and to your offspring I will give all these lands, and I will establish the oath that I swore to Abraham your father.'",
      "M": "'Stay in this land for a while, and I will be with you and will bless you. For to you and your descendants I will give all these lands and will confirm the oath I swore to your father Abraham.'",
      "T": "'Live as a sojourner in this land, and I will be with you and bless you. I will give all these lands to you and your descendants, and I will fulfil the oath I made to your father Abraham.'"
    },
    "4": {
      "L": "'I will multiply your offspring as the stars of heaven and will give to your offspring all these lands. And in your offspring all the nations of the earth shall be blessed,'",
      "M": "'I will make your descendants as numerous as the stars in the sky and will give them all these lands, and through your offspring all nations on earth will be blessed,'",
      "T": "'I will multiply your descendants until they are as countless as the stars, and I will give all these lands to them. Through your offspring, every nation on earth will find blessing—'"
    },
    "5": {
      "L": "'because Abraham obeyed my voice and kept my charge, my commandments, my statutes, and my laws.'",
      "M": "'because Abraham obeyed me and kept my requirements, my commands, my decrees and my instructions.'",
      "T": "'all because Abraham listened to my voice and faithfully kept my requirements, commands, decrees, and teachings.'"
    },
    "6": {
      "L": "So Isaac settled in Gerar.",
      "M": "So Isaac stayed in Gerar.",
      "T": "So Isaac settled in Gerar."
    },
    "7": {
      "L": "When the men of the place asked him about his wife, he said, 'She is my sister,' for he feared to say, 'My wife,' thinking, 'lest the men of the place should kill me because of Rebekah,' because she was attractive in appearance.",
      "M": "When the men of that place asked him about his wife, he said, 'She is my sister,' because he was afraid to say, 'She is my wife.' He thought, 'The men of this place might kill me on account of Rebekah, because she is beautiful.'",
      "T": "When the local men asked about Rebekah, Isaac said, 'She is my sister.' He was too afraid to say 'my wife,' fearing they would kill him to take her—she was that beautiful."
    },
    "8": {
      "L": "When he had been there a long time, Abimelech king of the Philistines looked out of a window and saw Isaac laughing with Rebekah his wife.",
      "M": "When Isaac had been there a long time, Abimelech king of the Philistines looked down from a window and saw Isaac caressing his wife Rebekah.",
      "T": "After Isaac had lived there for some time, Abimelech the Philistine king happened to look out a window and saw Isaac being affectionate with Rebekah."
    },
    "9": {
      "L": "So Abimelech called Isaac and said, 'Behold, she is your wife. How then could you say, \"She is my sister\"?' Isaac said to him, 'Because I thought, \"Lest I die because of her.\"'",
      "M": "So Abimelech summoned Isaac and said, 'She is really your wife! Why did you say, \"She is my sister\"?' Isaac answered him, 'Because I thought I might lose my life on account of her.'",
      "T": "Abimelech summoned Isaac and confronted him: 'She is obviously your wife! Why did you claim she was your sister?' Isaac said, 'Because I was afraid of being killed on account of her.'"
    },
    "10": {
      "L": "Abimelech said, 'What is this you have done to us? One of the people might easily have lain with your wife, and you would have brought guilt upon us.'",
      "M": "Then Abimelech said, 'What is this you have done to us? One of the men might well have slept with your wife, and you would have brought guilt upon us.'",
      "T": "Abimelech said, 'What have you done to us? Any of my men could easily have slept with your wife, and you would have brought great guilt upon us.'"
    },
    "11": {
      "L": "So Abimelech warned all the people, saying, 'Whoever touches this man or his wife shall surely be put to death.'",
      "M": "So Abimelech gave orders to all the people: 'Anyone who harms this man or his wife shall certainly be put to death.'",
      "T": "So Abimelech issued a public decree: 'Anyone who harms this man or his wife will be put to death.'"
    },
    "12": {
      "L": "And Isaac sowed in that land and reaped in the same year a hundredfold. The LORD blessed him,",
      "M": "Isaac planted crops in that land and the same year reaped a hundredfold, because the LORD blessed him.",
      "T": "Isaac planted crops in that land and harvested a hundredfold that same year—because the LORD blessed him."
    },
    "13": {
      "L": "and the man became rich, and gained more and more until he became very wealthy.",
      "M": "The man became rich, and his wealth continued to grow until he became very wealthy.",
      "T": "He grew increasingly wealthy, more and more prosperous, until he was enormously rich."
    },
    "14": {
      "L": "He had possessions of flocks and herds and many servants, so that the Philistines envied him.",
      "M": "He had so many flocks and herds and servants that the Philistines envied him.",
      "T": "His flocks and herds and household staff were so vast that the Philistines grew jealous of him."
    },
    "15": {
      "L": "Now the Philistines had stopped and filled with earth all the wells that his father's servants had dug in the days of Abraham his father.",
      "M": "(Now the Philistines had stopped up all the wells that Abraham's servants had dug, filling them with earth.)",
      "T": "(The Philistines had already filled in with dirt every well that Abraham's servants had dug during Abraham's lifetime.)"
    },
    "16": {
      "L": "And Abimelech said to Isaac, 'Go away from us, for you are much mightier than we.'",
      "M": "Then Abimelech said to Isaac, 'Move away from us; you have become too powerful for us.'",
      "T": "Then Abimelech said to Isaac, 'Leave us—you have become far too powerful for us to have you here.'"
    },
    "17": {
      "L": "So Isaac departed from there and encamped in the Valley of Gerar and settled there.",
      "M": "So Isaac moved away from there and encamped in the Valley of Gerar, where he settled.",
      "T": "So Isaac left and set up camp in the Valley of Gerar, where he made his home."
    },
    "18": {
      "L": "And Isaac dug again the wells of water that had been dug in the days of Abraham his father, which the Philistines had stopped after the death of Abraham. And he gave them the names that his father had given them.",
      "M": "Isaac reopened the wells that had been dug in the time of his father Abraham, which the Philistines had stopped up after Abraham died, and he gave them the same names his father had given them.",
      "T": "Isaac reopened the wells dug in Abraham's time—the ones the Philistines had blocked after Abraham died—and he gave them back the names his father had used."
    },
    "19": {
      "L": "But when Isaac's servants dug in the valley and found there a well of spring water,",
      "M": "Isaac's servants dug in the valley and discovered a well of fresh water there.",
      "T": "When Isaac's servants dug in the valley and struck a spring of fresh water,"
    },
    "20": {
      "L": "the herdsmen of Gerar quarreled with Isaac's herdsmen, saying, 'The water is ours.' So he called the name of the well Esek, because they contended with him.",
      "M": "the herders of Gerar quarreled with those of Isaac and said, 'The water is ours!' So he named the well Esek, because they disputed with him.",
      "T": "the herdsmen of Gerar quarreled with Isaac's herdsmen, claiming, 'The water is ours!' So Isaac named the well Esek—'Dispute'—because of the argument."
    },
    "21": {
      "L": "Then they dug another well, and they quarreled over that also, so he called its name Sitnah.",
      "M": "Then they dug another well, but they quarreled over that one too; so he named it Sitnah.",
      "T": "His men dug another well, and they quarreled over that one too. He named it Sitnah—'Hostility.'"
    },
    "22": {
      "L": "And he moved from there and dug another well, and they did not quarrel over it. So he called its name Rehoboth, saying, 'For now the LORD has made room for us, and we shall be fruitful in the land.'",
      "M": "He moved on from there and dug another well, and no one quarreled over it. He named it Rehoboth, saying, 'Now the LORD has given us room and we will flourish in the land.'",
      "T": "He moved on and dug yet another well, and this time no one contested it. He named it Rehoboth—'Open Country'—saying, 'At last the LORD has made room for us, and we will thrive in this land.'"
    },
    "23": {
      "L": "From there he went up to Beersheba.",
      "M": "From there he went up to Beersheba.",
      "T": "From there Isaac traveled to Beersheba."
    },
    "24": {
      "L": "And the LORD appeared to him the same night and said, 'I am the God of Abraham your father. Fear not, for I am with you and will bless you and multiply your offspring for my servant Abraham's sake.'",
      "M": "That night the LORD appeared to him and said, 'I am the God of your father Abraham. Do not be afraid, for I am with you; I will bless you and increase the number of your descendants for the sake of my servant Abraham.'",
      "T": "That same night the LORD appeared to Isaac and said, 'I am the God of your father Abraham. Do not be afraid—I am with you. I will bless you and multiply your descendants, for the sake of my servant Abraham.'"
    },
    "25": {
      "L": "So he built an altar there and called upon the name of the LORD and pitched his tent there. And there Isaac's servants dug a well.",
      "M": "Isaac built an altar there and called on the name of the LORD. There he pitched his tent, and there his servants dug a well.",
      "T": "Isaac built an altar there, called on the name of the LORD, and pitched his tent. His servants also dug a well at that place."
    },
    "26": {
      "L": "When Abimelech went to him from Gerar with Ahuzzath his adviser and Phicol the commander of his army,",
      "M": "Meanwhile, Abimelech had come to him from Gerar, with Ahuzzath his personal adviser and Phicol the commander of his forces.",
      "T": "Then Abimelech came to visit Isaac from Gerar, accompanied by his adviser Ahuzzath and his army commander Phicol."
    },
    "27": {
      "L": "Isaac said to them, 'Why have you come to me, seeing that you hate me and have sent me away from you?'",
      "M": "Isaac asked them, 'Why have you come to me, since you were hostile to me and sent me away?'",
      "T": "Isaac said to them, 'Why have you come? You made it clear you resented me and sent me away.'"
    },
    "28": {
      "L": "They said, 'We see plainly that the LORD has been with you. So we said, let there be a sworn oath between us, between you and us, and let us make a covenant with you,'",
      "M": "They answered, 'We saw clearly that the LORD was with you; so we said there ought to be a sworn agreement between us. Let us make a covenant with you'",
      "T": "They answered, 'We have seen clearly that the LORD is with you. So we thought, let there be a solemn agreement between us—a covenant—'"
    },
    "29": {
      "L": "'so that you will do us no harm, just as we have not touched you and have done to you nothing but good and have sent you away in peace. You are now the blessed of the LORD.'",
      "M": "'that you will do us no harm, just as we did not harm you but always treated you well and sent you away in peace. And now you are the blessed of the LORD.'",
      "T": "'guaranteeing that you will not harm us, just as we have not harmed you but treated you well and sent you away in peace. For you are clearly a man blessed by the LORD.'"
    },
    "30": {
      "L": "So he made them a feast, and they ate and drank.",
      "M": "Isaac then made a feast for them, and they ate and drank.",
      "T": "Isaac prepared a feast for them, and they ate and drank together."
    },
    "31": {
      "L": "In the morning they rose early and exchanged oaths. And Isaac sent them on their way, and they departed from him in peace.",
      "M": "Early the next morning the men swore an oath to each other. Then Isaac sent them on their way, and they went away peacefully.",
      "T": "Early the next morning they swore their oaths to each other. Isaac sent them off, and they left in peace."
    },
    "32": {
      "L": "That same day Isaac's servants came and told him about the well that they had dug and said to him, 'We have found water.'",
      "M": "That day Isaac's servants came and told him about the well they had dug. They said, 'We've found water!'",
      "T": "That same day Isaac's servants came with good news: 'We have found water!' They reported on the well they had dug."
    },
    "33": {
      "L": "He called it Shibah; therefore the name of the city is Beersheba to this day.",
      "M": "He called the well Shibah, and to this day the name of the town has been Beersheba.",
      "T": "Isaac named the well Shibah—'Oath.' That is why the city has been called Beersheba ever since."
    },
    "34": {
      "L": "When Esau was forty years old, he took Judith the daughter of Beeri the Hittite to be his wife, and Basemath the daughter of Elon the Hittite,",
      "M": "When Esau was forty years old, he married Judith daughter of Beeri the Hittite, and also Basemath daughter of Elon the Hittite.",
      "T": "When Esau was forty years old, he married Judith the daughter of Beeri the Hittite, and also Basemath the daughter of Elon the Hittite."
    },
    "35": {
      "L": "and they made life bitter for Isaac and Rebekah.",
      "M": "They were a source of grief to Isaac and Rebekah.",
      "T": "These marriages were a constant grief to Isaac and Rebekah."
    }
  },
  "27": {
    "1": {
      "L": "When Isaac was old and his eyes were dim so that he could not see, he called Esau his older son and said to him, 'My son'; and he answered, 'Here I am.'",
      "M": "When Isaac was old and his eyes were so weak that he could no longer see, he called for Esau his older son and said to him, 'My son.' 'Here I am,' he answered.",
      "T": "When Isaac was old and nearly blind, he called for his older son Esau. 'My son,' he said. 'Yes, here I am,' Esau answered."
    },
    "2": {
      "L": "He said, 'Behold, I am old; I do not know the day of my death.'",
      "M": "Isaac said, 'I am now an old man and don't know the day of my death.'",
      "T": "Isaac said, 'I am old now, and I do not know how many days I have left.'"
    },
    "3": {
      "L": "'Now then, take your weapons, your quiver and your bow, and go out to the field and hunt game for me,'",
      "M": "'Now then, get your weapons—your quiver and bow—and go out to the open country to hunt some wild game for me.'",
      "T": "'Take your hunting gear—your quiver and bow—and go out to the fields to hunt some game for me.'"
    },
    "4": {
      "L": "'and prepare for me delicious food, such as I love, and bring it to me so that I may eat, that my soul may bless you before I die.'",
      "M": "'Prepare me the kind of tasty food I like and bring it to me to eat, so that I may give you my blessing before I die.'",
      "T": "'Then prepare the savory food I love and bring it to me, so that I may eat and give you my blessing before I die.'"
    },
    "5": {
      "L": "Now Rebekah was listening when Isaac spoke to his son Esau. So when Esau went to the field to hunt for game and bring it,",
      "M": "Now Rebekah was listening as Isaac spoke to his son Esau. When Esau left for the open country to hunt game and bring it back,",
      "T": "Rebekah had been listening to this whole conversation. As soon as Esau left for the fields to hunt,"
    },
    "6": {
      "L": "Rebekah said to her son Jacob, 'I heard your father speak to your brother Esau,'",
      "M": "Rebekah said to her son Jacob, 'Look, I overheard your father say to your brother Esau,'",
      "T": "Rebekah said to her son Jacob, 'I just heard your father tell Esau:'"
    },
    "7": {
      "L": "'\"Bring me game and prepare for me delicious food, that I may eat it and bless you before the LORD before I die.\"'",
      "M": "'\"Bring me some game and prepare me some tasty food to eat, so that I may give you my blessing in the presence of the LORD before I die.\"'",
      "T": "'\\'Bring me game and make me savory food to eat, so that I may bless you before the LORD before I die.\\''"
    },
    "8": {
      "L": "'Now therefore, my son, obey my voice as I command you.'",
      "M": "'Now, my son, listen carefully and do what I tell you.'",
      "T": "'Now, my son, listen to me carefully and do exactly what I say.'"
    },
    "9": {
      "L": "'Go to the flock and bring me two good young goats, so that I may prepare from them delicious food for your father, such as he loves.'",
      "M": "'Go out to the flock and bring me two choice young goats, so I can prepare some tasty food for your father, just the way he likes it.'",
      "T": "'Go to the flock and bring me two choice young goats. I will make your father his favorite savory dish from them.'"
    },
    "10": {
      "L": "'And you shall bring it to your father to eat, so that he may bless you before he dies.'",
      "M": "'Then take it to your father to eat, so that he may give you his blessing before he dies.'",
      "T": "'You will take the food to your father, and he will eat it and give you his blessing before he dies.'"
    },
    "11": {
      "L": "But Jacob said to Rebekah his mother, 'Behold, my brother Esau is a hairy man, and I am a smooth man.'",
      "M": "Jacob said to his mother Rebekah, 'But my brother Esau is a hairy man while I have smooth skin.'",
      "T": "Jacob said to his mother, 'But Esau is a hairy man and I am smooth-skinned.'"
    },
    "12": {
      "L": "'Perhaps my father will feel me, and I shall seem to be mocking him and bring a curse upon myself and not a blessing.'",
      "M": "'What if my father touches me? I would appear to be tricking him and would bring down a curse on myself rather than a blessing.'",
      "T": "'If my father touches me, he will realize I am deceiving him, and I will bring a curse on myself instead of a blessing.'"
    },
    "13": {
      "L": "His mother said to him, 'Let your curse be on me, my son; only obey my voice, and go, bring them to me.'",
      "M": "His mother said to him, 'My son, let the curse fall on me. Just do what I say; go and get them for me.'",
      "T": "His mother said, 'My son, let any curse fall on me. Just obey my voice—go and get the goats.'"
    },
    "14": {
      "L": "So he went and took them and brought them to his mother, and his mother prepared delicious food, such as his father loved.",
      "M": "So he went and got them and brought them to his mother, and she prepared some tasty food, just the way his father liked it.",
      "T": "So Jacob went and got the goats and brought them to his mother, who made the savory dish his father loved."
    },
    "15": {
      "L": "Then Rebekah took the best garments of Esau her older son, which were with her in the house, and put them on Jacob her younger son.",
      "M": "Then Rebekah took the best clothes of Esau her older son, which she had in the house, and put them on her younger son Jacob.",
      "T": "Then Rebekah took Esau's finest clothes, which she kept in the house, and dressed Jacob in them."
    },
    "16": {
      "L": "And the skins of the young goats she put on his hands and on the smooth part of his neck.",
      "M": "She also covered his hands and the smooth part of his neck with the goatskins.",
      "T": "She wrapped the goatskins around his hands and over the smooth skin of his neck."
    },
    "17": {
      "L": "And she put the delicious food and the bread, which she had prepared, into the hand of her son Jacob.",
      "M": "Then she handed to her son Jacob the tasty food and the bread she had made.",
      "T": "Then she placed the savory food and fresh bread she had made into Jacob's hands."
    },
    "18": {
      "L": "So he went in to his father and said, 'My father.' And he said, 'Here I am. Who are you, my son?'",
      "M": "He went to his father and said, 'My father.' 'Yes, my son,' he answered. 'Who is it?'",
      "T": "Jacob went to his father and said, 'Father.' 'Yes?' said Isaac. 'Which of my sons are you?'"
    },
    "19": {
      "L": "Jacob said to his father, 'I am Esau your firstborn. I have done as you told me; now sit up and eat of my game, that your soul may bless me.'",
      "M": "Jacob said to his father, 'I am Esau your firstborn. I have done what you asked. Please sit up and eat some of my game so that you may give me your blessing.'",
      "T": "Jacob said to his father, 'I am Esau, your firstborn. I have done what you asked. Please sit up and eat my game, so that you can give me your blessing.'"
    },
    "20": {
      "L": "But Isaac said to his son, 'How is it that you have found it so quickly, my son?' He answered, 'Because the LORD your God granted me success.'",
      "M": "Isaac asked his son, 'How did you find it so quickly, my son?' 'The LORD your God gave me success,' he answered.",
      "T": "Isaac asked, 'How did you find game so quickly, my son?' Jacob answered, 'The LORD your God made it happen for me.'"
    },
    "21": {
      "L": "Then Isaac said to Jacob, 'Please come near, that I may feel you, my son, to know whether you are really my son Esau or not.'",
      "M": "Then Isaac said to Jacob, 'Come near so I can touch you, my son, to know whether you really are my son Esau or not.'",
      "T": "Then Isaac said, 'Come closer, my son, so I can touch you and know for certain whether you are really Esau or not.'"
    },
    "22": {
      "L": "So Jacob went near to Isaac his father, who felt him and said, 'The voice is Jacob's voice, but the hands are the hands of Esau.'",
      "M": "Jacob went close to his father Isaac, who touched him and said, 'The voice is the voice of Jacob, but the hands are the hands of Esau.'",
      "T": "Jacob moved close, and Isaac felt him and said, 'The voice sounds like Jacob, but the hands—the hands are Esau's.'"
    },
    "23": {
      "L": "And he did not recognize him, because his hands were hairy like his brother Esau's hands. So he blessed him.",
      "M": "He did not recognize him, for his hands were hairy like those of his brother Esau; so he proceeded to bless him.",
      "T": "He did not recognize Jacob, because his hands were as hairy as Esau's. So he blessed him."
    },
    "24": {
      "L": "He said, 'Are you really my son Esau?' He answered, 'I am.'",
      "M": "He asked, 'Are you really my son Esau?' 'I am,' he replied.",
      "T": "'Are you really my son Esau?' he asked. 'I am,' Jacob answered."
    },
    "25": {
      "L": "Then he said, 'Bring it near to me, that I may eat of my son's game and bless you.' So he brought it near to him, and he ate; and he brought him wine, and he drank.",
      "M": "Then he said, 'Bring me some of your game to eat, my son, so that I may give you my blessing.' Jacob brought it to him and he ate; and he brought some wine and he drank.",
      "T": "He said, 'Bring the food near, my son, and let me eat. Then I will give you my blessing.' Jacob brought it to him, and he ate. He also brought wine, and Isaac drank."
    },
    "26": {
      "L": "Then his father Isaac said to him, 'Come near and kiss me, my son.'",
      "M": "Then his father Isaac said to him, 'Come here, my son, and kiss me.'",
      "T": "Then his father Isaac said, 'Come close and kiss me, my son.'"
    },
    "27": {
      "L": "So he came near and kissed him. And Isaac smelled the smell of his garments and blessed him and said,\n'See, the smell of my son\nis as the smell of a field that the LORD has blessed!'",
      "M": "So he went to him and kissed him. When Isaac caught the smell of his clothes, he blessed him and said,\n'Ah, the smell of my son\nis like the smell of a field that the LORD has blessed!'",
      "T": "Jacob came close and kissed him. When Isaac smelled his clothing, he spoke the blessing:\n'The fragrance of my son\nis like the scent of a field the LORD himself has blessed!'"
    },
    "28": {
      "L": "'May God give you of the dew of heaven\nand of the fatness of the earth\nand plenty of grain and wine.'",
      "M": "'May God give you heaven's dew\nand earth's richness—\nan abundance of grain and new wine.'",
      "T": "'May God grant you the dew of heaven\nand the richness of the earth—\nabundant grain and overflowing wine.'"
    },
    "29": {
      "L": "'Let peoples serve you,\nand nations bow down to you.\nBe lord over your brothers,\nand may your mother's sons bow down to you.\nCursed be everyone who curses you,\nand blessed be everyone who blesses you!'",
      "M": "'May nations serve you\nand peoples bow down to you.\nBe lord over your brothers,\nand may the sons of your mother bow down to you.\nMay those who curse you be cursed\nand those who bless you be blessed!'",
      "T": "'May nations serve you\nand peoples bow at your feet.\nBe master over your brothers;\nlet your mother's sons kneel before you.\nAll who curse you—cursed they will be;\nall who bless you—blessed!'"
    },
    "30": {
      "L": "As soon as Isaac had finished blessing Jacob, when Jacob had scarcely gone out from the presence of Isaac his father, Esau his brother came in from his hunting.",
      "M": "After Isaac finished blessing him, and Jacob had scarcely left his father's presence, his brother Esau came in from hunting.",
      "T": "The moment Isaac finished blessing Jacob—Jacob had barely stepped outside—Esau came in from hunting."
    },
    "31": {
      "L": "He also prepared delicious food and brought it to his father. And he said to his father, 'Let my father arise and eat of his son's game, that you may bless me.'",
      "M": "He too prepared some tasty food and brought it to his father. Then he said to him, 'My father, please sit up and eat some of my game, so that you may give me your blessing.'",
      "T": "Esau also prepared savory food and brought it to his father. 'Please sit up and eat my game, father,' he said, 'so that you can give me your blessing.'"
    },
    "32": {
      "L": "His father Isaac said to him, 'Who are you?' He answered, 'I am your son, your firstborn, Esau.'",
      "M": "His father Isaac asked him, 'Who are you?' 'I am your son,' he answered, 'your firstborn, Esau.'",
      "T": "His father Isaac asked, 'Who are you?' 'I am your son,' he answered, 'your firstborn—Esau.'"
    },
    "33": {
      "L": "Then Isaac trembled very violently and said, 'Who was it then that hunted game and brought it to me, and I ate it all before you came, and I have blessed him? Yes, and he shall be blessed.'",
      "M": "Isaac trembled violently and said, 'Who was it, then, that hunted game and brought it to me? I ate it just before you came and I blessed him—and indeed he will be blessed!'",
      "T": "Isaac shook uncontrollably and said, 'Who was it, then, who just brought me game and whom I just blessed? He will stay blessed—there is nothing I can do about it.'"
    },
    "34": {
      "L": "As soon as Esau heard the words of his father, he cried out with an exceedingly great and bitter cry and said to his father, 'Bless me, even me also, O my father!'",
      "M": "When Esau heard his father's words, he burst out with a loud and bitter cry and said to his father, 'Bless me—me too, my father!'",
      "T": "When Esau heard his father's words, he let out a loud, anguished cry and begged, 'Bless me too, Father! Bless me too!'"
    },
    "35": {
      "L": "But he said, 'Your brother came deceitfully, and he has taken away your blessing.'",
      "M": "But he said, 'Your brother came deceitfully and took your blessing.'",
      "T": "But Isaac said, 'Your brother came and deceived me, and he has taken your blessing.'"
    },
    "36": {
      "L": "Esau said, 'Is he not rightly named Jacob? For he has cheated me these two times. He took away my birthright, and behold, now he has taken away my blessing.' Then he said, 'Have you not reserved a blessing for me?'",
      "M": "Esau said, 'Isn't he rightly named Jacob? This is the second time he has taken advantage of me: He took my birthright, and now he's taken my blessing!' Then he asked, 'Haven't you reserved any blessing for me?'",
      "T": "Esau exclaimed, 'His name says it all—Jacob, the Deceiver! He has tripped me up twice now: first he took my birthright, and now he has stolen my blessing!' Then he pleaded, 'Have you not kept back even one blessing for me?'"
    },
    "37": {
      "L": "Isaac answered and said to Esau, 'Behold, I have made him lord over you, and all his brothers I have given to him for servants, and with grain and wine I have sustained him. What then can I do for you, my son?'",
      "M": "Isaac answered Esau, 'I have made him lord over you and have made all his relatives his servants, and I have sustained him with grain and new wine. So what can I possibly do for you, my son?'",
      "T": "Isaac answered Esau, 'I have already made him your master and given him all his brothers as servants. I have granted him grain and wine. What is there left that I can do for you, my son?'"
    },
    "38": {
      "L": "Esau said to his father, 'Have you but one blessing, my father? Bless me, even me also, O my father.' And Esau lifted up his voice and wept.",
      "M": "Esau said to his father, 'Do you have only one blessing, my father? Bless me too, my father!' Then Esau wept aloud.",
      "T": "Esau said to his father, 'Have you only one blessing, Father? Bless me too!' And Esau broke down and wept."
    },
    "39": {
      "L": "Then Isaac his father answered and said to him:\n'Behold, away from the fatness of the earth shall your dwelling be,\nand away from the dew of heaven on high.'",
      "M": "His father Isaac answered him:\n'Your dwelling will be\naway from the earth's richness,\naway from the dew of heaven above.'",
      "T": "His father Isaac answered him:\n'Your home will be\nfar from the earth's richness,\nfar from the dew of the skies above.'"
    },
    "40": {
      "L": "'By your sword you shall live,\nand you shall serve your brother;\nbut when you grow restless\nyou shall break his yoke from your neck.'",
      "M": "'You will live by the sword\nand you will serve your brother.\nBut when you grow restless,\nyou will throw his yoke from off your neck.'",
      "T": "'You will live by your sword\nand serve your brother.\nBut when you can bear it no longer,\nyou will shake his yoke from your neck.'"
    },
    "41": {
      "L": "Now Esau hated Jacob because of the blessing with which his father had blessed him, and Esau said to himself, 'The days of mourning for my father are approaching; then I will kill my brother Jacob.'",
      "M": "Esau held a grudge against Jacob because of the blessing his father had given him. He said to himself, 'The days of mourning for my father are near; then I will kill my brother Jacob.'",
      "T": "From that day on, Esau hated Jacob because of the blessing his father had given. Esau told himself, 'When the time of mourning for my father comes, I will kill my brother Jacob.'"
    },
    "42": {
      "L": "But the words of Esau her older son were told to Rebekah. So she sent and called Jacob her younger son and said to him, 'Behold, your brother Esau comforts himself about you by planning to kill you.'",
      "M": "When Rebekah was told what her older son Esau had said, she sent for her younger son Jacob and told him, 'Your brother Esau is consoling himself with the thought of killing you.'",
      "T": "When Rebekah learned what Esau was planning, she summoned Jacob and said, 'Your brother Esau is consoling himself by planning to kill you.'"
    },
    "43": {
      "L": "'Now therefore, my son, obey my voice. Arise, flee to Laban my brother in Haran'",
      "M": "'Now then, my son, do what I say: Flee at once to my brother Laban in Haran.'",
      "T": "'Listen to me, my son—flee to my brother Laban in Haran, and do it now.'"
    },
    "44": {
      "L": "'and stay with him a while, until your brother's fury turns away—'",
      "M": "'Stay with him for a while until your brother's fury subsides.'",
      "T": "'Stay with him until your brother's rage cools down.'"
    },
    "45": {
      "L": "'until your brother's anger turns away from you, and he forgets what you have done to him. Then I will send and bring you from there. Why should I be bereft of you both in one day?'",
      "M": "'When your brother is no longer angry with you and forgets what you did to him, I'll send word for you to come back from there. Why should I lose both of you in one day?'",
      "T": "'Once his anger has faded and he has forgotten what you did, I will send for you to come home. Why should I lose both of you in a single day?'"
    },
    "46": {
      "L": "Then Rebekah said to Isaac, 'I loathe my life because of the Hittite women. If Jacob marries one of the Hittite women like these, one of the women of the land, what good will my life be to me?'",
      "M": "Then Rebekah said to Isaac, 'I'm disgusted with living because of these Hittite women. If Jacob takes a wife from among the women of this land, from Hittite women like these, my life will not be worth living.'",
      "T": "Rebekah said to Isaac, 'These Hittite women are making my life unbearable. If Jacob marries one of these local Hittite women, I might as well be dead.'"
    }
  },
  "28": {
    "1": {
      "L": "Then Isaac called Jacob and blessed him and directed him, 'You must not take a wife from the Canaanite women.'",
      "M": "So Isaac called for Jacob and blessed him. Then he commanded him: 'Do not marry a Canaanite woman.'",
      "T": "So Isaac called Jacob, blessed him, and gave him this command: 'Do not marry a Canaanite woman.'"
    },
    "2": {
      "L": "'Arise, go to Paddan-aram to the house of Bethuel your mother's father, and take as your wife from there one of the daughters of Laban your mother's brother.'",
      "M": "'Go at once to Paddan Aram, to the house of your mother's father Bethuel. Take a wife for yourself there, from among the daughters of Laban, your mother's brother.'",
      "T": "'Go to Paddan-aram, to the household of your grandfather Bethuel, and find a wife there from among the daughters of your uncle Laban.'"
    },
    "3": {
      "L": "'God Almighty bless you and make you fruitful and multiply you, that you may become a company of peoples.'",
      "M": "'May God Almighty bless you and make you fruitful and increase your numbers until you become a community of peoples.'",
      "T": "'May God Almighty bless you, make you fruitful, and multiply you until you become a great nation.'"
    },
    "4": {
      "L": "'May he give the blessing of Abraham to you and to your offspring with you, that you may take possession of the land of your sojournings that God gave to Abraham!'",
      "M": "'May he give you and your descendants the blessing given to Abraham, so that you may take possession of the land where you now reside as a foreigner, the land God gave to Abraham.'",
      "T": "'May he pass on to you and your descendants the blessing he gave to Abraham—so that you may one day possess the land where you now live as a stranger, the land God promised Abraham.'"
    },
    "5": {
      "L": "Thus Isaac sent Jacob away. And he went to Paddan-aram, to Laban, the son of Bethuel the Aramean, the brother of Rebekah, Jacob's and Esau's mother.",
      "M": "So Isaac sent Jacob on his way, and he went to Paddan Aram, to Laban son of Bethuel the Aramean, the brother of Rebekah, who was the mother of Jacob and Esau.",
      "T": "Isaac sent Jacob away, and he traveled to Paddan-aram, to Laban the son of Bethuel the Aramean—the brother of Rebekah, who was the mother of both Jacob and Esau."
    },
    "6": {
      "L": "Now Esau saw that Isaac had blessed Jacob and sent him away to Paddan-aram to take a wife from there, and that as he blessed him he directed him, 'You must not take a wife from the Canaanite women,'",
      "M": "Now Esau learned that Isaac had blessed Jacob and had sent him to Paddan Aram to take a wife from there, and that when he blessed him he commanded him, 'Do not marry a Canaanite woman,'",
      "T": "When Esau learned that Isaac had blessed Jacob and sent him away to Paddan-aram to find a wife there—commanding him not to marry a Canaanite woman—"
    },
    "7": {
      "L": "and that Jacob had obeyed his father and his mother and gone to Paddan-aram.",
      "M": "and that Jacob had obeyed his father and mother and had gone to Paddan Aram,",
      "T": "and that Jacob had obeyed his father and mother and gone to Paddan-aram,"
    },
    "8": {
      "L": "So when Esau saw that the Canaanite women did not please Isaac his father,",
      "M": "Esau then realized how displeasing the Canaanite women were to his father Isaac;",
      "T": "Esau realized that his father Isaac disapproved of Canaanite women."
    },
    "9": {
      "L": "Esau went to Ishmael and took as his wife, besides the wives he had, Mahalath the daughter of Ishmael, Abraham's son, the sister of Nebaioth.",
      "M": "so he went to Ishmael and married Mahalath, the sister of Nebaioth and daughter of Ishmael son of Abraham, in addition to the wives he already had.",
      "T": "So Esau went to Ishmael and took Mahalath—Ishmael's daughter, the sister of Nebaioth—as an additional wife."
    },
    "10": {
      "L": "Jacob left Beersheba and went toward Haran.",
      "M": "Jacob left Beersheba and set out for Haran.",
      "T": "Jacob left Beersheba and set out for Haran."
    },
    "11": {
      "L": "And he came to a certain place and stayed there that night, because the sun had set. Taking one of the stones of the place, he put it under his head and lay down in that place to sleep.",
      "M": "When he reached a certain place, he stopped for the night because the sun had set. Taking one of the stones there, he put it under his head and lay down to sleep.",
      "T": "He came to a certain place and stopped for the night because the sun had set. Taking a stone from the ground, he put it under his head as a pillow and lay down to sleep."
    },
    "12": {
      "L": "And he dreamed, and behold, there was a stairway set up on the earth, and the top of it reached to heaven. And behold, the angels of God were ascending and descending on it!",
      "M": "He had a dream in which he saw a stairway resting on the earth, with its top reaching to heaven, and the angels of God were ascending and descending on it.",
      "T": "He dreamed of a great stairway rising from the earth and reaching up to heaven, with God's messengers ascending and descending on it."
    },
    "13": {
      "L": "And behold, the LORD stood above it and said, 'I am the LORD, the God of Abraham your father and the God of Isaac. The land on which you lie I will give to you and to your offspring.'",
      "M": "There above it stood the LORD, and he said: 'I am the LORD, the God of your father Abraham and the God of Isaac. I will give you and your descendants the land on which you are lying.'",
      "T": "The LORD himself stood at the top, and said, 'I am the LORD, the God of Abraham your father and the God of Isaac. This land where you are lying—I will give it to you and to your descendants.'"
    },
    "14": {
      "L": "'Your offspring shall be like the dust of the earth, and you shall spread abroad to the west and to the east and to the north and to the south, and in you and your offspring shall all the families of the earth be blessed.'",
      "M": "'Your descendants will be like the dust of the earth, and you will spread out to the west and to the east, to the north and to the south. All peoples on earth will be blessed through you and your offspring.'",
      "T": "'Your descendants will be as countless as the dust of the earth. You will spread out in every direction—west, east, north, and south. Through you and your offspring, every family on earth will find blessing.'"
    },
    "15": {
      "L": "'Behold, I am with you and will keep you wherever you go, and will bring you back to this land. For I will not leave you until I have done what I have promised you.'",
      "M": "'I am with you and will watch over you wherever you go, and I will bring you back to this land. I will not leave you until I have done what I have promised you.'",
      "T": "'I am with you and will guard you wherever you go. I will bring you back to this land, and I will not abandon you until I have kept every promise I have made.'"
    },
    "16": {
      "L": "Then Jacob awoke from his sleep and said, 'Surely the LORD is in this place, and I did not know it.'",
      "M": "When Jacob awoke from his sleep, he thought, 'Surely the LORD is in this place, and I was not aware of it.'",
      "T": "Jacob woke from his sleep and said, 'Surely the LORD is in this place, and I never knew it!'"
    },
    "17": {
      "L": "And he was afraid and said, 'How awesome is this place! This is none other than the house of God, and this is the gate of heaven.'",
      "M": "He was afraid and said, 'How awesome is this place! This is none other than the house of God; this is the gate of heaven.'",
      "T": "He was filled with awe and said, 'What a terrifying, holy place! This is nothing less than the house of God—the very gateway to heaven.'"
    },
    "18": {
      "L": "So early in the morning Jacob took the stone that he had put under his head and set it up for a pillar and poured oil on the top of it.",
      "M": "Early the next morning Jacob took the stone he had placed under his head and set it up as a pillar and poured oil on top of it.",
      "T": "Early the next morning Jacob took the stone he had used as a pillow, set it upright as a sacred pillar, and poured oil over the top of it."
    },
    "19": {
      "L": "He called the name of that place Bethel, but the name of the city was Luz at the first.",
      "M": "He called that place Bethel, though the city used to be called Luz.",
      "T": "He named that place Bethel—'House of God'—though the town had formerly been called Luz."
    },
    "20": {
      "L": "Then Jacob made a vow, saying, 'If God will be with me and will keep me in this way that I go, and will give me bread to eat and clothing to wear,'",
      "M": "Then Jacob made a vow, saying, 'If God will be with me and will watch over me on this journey I am taking and will give me food to eat and clothes to wear'",
      "T": "Then Jacob made a vow: 'If God will be with me and protect me on this journey, and give me food to eat and clothes to wear,'"
    },
    "21": {
      "L": "'so that I come again to my father's house in peace, then the LORD shall be my God,'",
      "M": "'so that I return safely to my father's household, then the LORD will be my God'",
      "T": "'and if I return safely to my father's home, then the LORD will be my God.'"
    },
    "22": {
      "L": "'and this stone, which I have set up for a pillar, shall be God's house. And of all that you give me I will give a full tenth to you.'",
      "M": "'and this stone that I have set up as a pillar will be God's house, and of all that you give me I will give you a tenth.'",
      "T": "'This stone I have set up as a pillar will become God's house, and of everything you give me I will return a tenth to you.'"
    }
  },
  "29": {
    "1": {
      "L": "Then Jacob went on his journey and came to the land of the people of the east.",
      "M": "Then Jacob continued on his journey and came to the land of the eastern peoples.",
      "T": "Jacob continued his journey and arrived in the land of the eastern peoples."
    },
    "2": {
      "L": "As he looked, he saw a well in the field, and behold, three flocks of sheep were lying beside it, for out of that well the flocks were watered. The stone on the well's mouth was large.",
      "M": "There he saw a well in the open country, with three flocks of sheep lying near it because the flocks were watered from that well. The stone over the mouth of the well was large.",
      "T": "There he saw a well in the open country, with three flocks of sheep resting beside it—this was where the flocks were watered. A large stone covered the mouth of the well."
    },
    "3": {
      "L": "When all the flocks were gathered there, the shepherds would roll the stone from the mouth of the well and water the sheep, and put the stone back in its place over the mouth of the well.",
      "M": "When all the flocks were gathered there, the shepherds would roll the stone away from the well's mouth and water the sheep. Then they would return the stone to its place over the mouth of the well.",
      "T": "The shepherds would wait until all the flocks had gathered, then roll the stone away and water the sheep before replacing the stone."
    },
    "4": {
      "L": "Jacob said to them, 'My brothers, where do you come from?' They said, 'We are from Haran.'",
      "M": "Jacob asked the shepherds, 'My brothers, where are you from?' 'We're from Haran,' they replied.",
      "T": "Jacob said to the shepherds, 'Where are you from, friends?' They said, 'We are from Haran.'"
    },
    "5": {
      "L": "He said to them, 'Do you know Laban the son of Nahor?' They said, 'We know him.'",
      "M": "He said to them, 'Do you know Laban, Nahor's grandson?' 'Yes, we know him,' they answered.",
      "T": "'Do you know Laban, the grandson of Nahor?' he asked. 'Yes, we know him,' they replied."
    },
    "6": {
      "L": "He said to them, 'Is it well with him?' They said, 'It is well; and see, Rachel his daughter is coming with the sheep!'",
      "M": "'Is he well?' Jacob asked. 'Yes, he is,' they said, 'and here comes his daughter Rachel with the sheep.'",
      "T": "'Is he doing well?' Jacob asked. 'He is,' they said. 'And look—here comes his daughter Rachel with the sheep now!'"
    },
    "7": {
      "L": "He said, 'Behold, it is still high day; it is not time for the livestock to be gathered together. Water the sheep and go, pasture them.'",
      "M": "'Look,' he said, 'the sun is still high; it's not time for the flocks to be gathered. Water the sheep and take them back to pasture.'",
      "T": "Jacob said, 'It is still the middle of the day—too early to bring the flocks in. Why not water the sheep and take them back to pasture?'"
    },
    "8": {
      "L": "But they said, 'We cannot until all the flocks are gathered together and the stone is rolled from the mouth of the well; then we water the sheep.'",
      "M": "'We can't,' they replied, 'until all the flocks are gathered and the stone has been rolled away from the well's mouth; then we will water the sheep.'",
      "T": "'We cannot,' they said, 'until all the flocks have assembled and we roll the stone from the mouth of the well. Only then do we water the sheep.'"
    },
    "9": {
      "L": "While he was still speaking with them, Rachel came with her father's sheep, for she was a shepherdess.",
      "M": "While he was still talking with them, Rachel came with her father's flock, for she tended them.",
      "T": "While Jacob was still talking with them, Rachel arrived with her father's sheep—she was the one who tended them."
    },
    "10": {
      "L": "Now as soon as Jacob saw Rachel the daughter of Laban his mother's brother, and the sheep of Laban his mother's brother, Jacob came near and rolled the stone from the well's mouth and watered the flock of Laban his mother's brother.",
      "M": "When Jacob saw Rachel daughter of his uncle Laban, and Laban's sheep, he went over and rolled the stone away from the mouth of the well and watered his uncle's sheep.",
      "T": "The moment Jacob saw Rachel—Laban's daughter, his own cousin—and the sheep in her care, he stepped forward, rolled the stone from the mouth of the well, and watered the whole flock."
    },
    "11": {
      "L": "Then Jacob kissed Rachel and wept aloud.",
      "M": "Then Jacob kissed Rachel and began to weep aloud.",
      "T": "Then Jacob kissed Rachel and burst into tears."
    },
    "12": {
      "L": "And Jacob told Rachel that he was her father's kinsman, and that he was Rebekah's son, and she ran and told her father.",
      "M": "He had told Rachel that he was a relative of her father and a son of Rebekah. So she ran and told her father.",
      "T": "He told Rachel that he was her father's relative, the son of Rebekah. She ran to tell her father."
    },
    "13": {
      "L": "As soon as Laban heard the news about Jacob, his sister's son, he ran to meet him and embraced him and kissed him and brought him to his house. Jacob told Laban all these things,",
      "M": "As soon as Laban heard the news about Jacob, his sister's son, he hurried to meet him. He embraced him and kissed him and brought him to his home, and there Jacob told him all these things.",
      "T": "When Laban heard that his nephew Jacob had arrived, he ran to meet him, embraced him warmly, kissed him, and brought him home. Jacob told him everything that had happened."
    },
    "14": {
      "L": "and Laban said to him, 'Surely you are my bone and my flesh!' And he stayed with him a month.",
      "M": "Then Laban said to him, 'You are my own flesh and blood.' After Jacob had stayed with him for a whole month,",
      "T": "Laban said, 'You are truly my own flesh and blood!' Jacob stayed with him for a full month."
    },
    "15": {
      "L": "Then Laban said to Jacob, 'Because you are my kinsman, should you therefore serve me for nothing? Tell me, what shall your wages be?'",
      "M": "Laban said to him, 'Just because you are a relative of mine, should you work for me for nothing? Tell me what your wages should be.'",
      "T": "Then Laban said to Jacob, 'You shouldn't work for nothing just because you're family. Tell me what you want as your wages.'"
    },
    "16": {
      "L": "Now Laban had two daughters. The name of the older was Leah, and the name of the younger was Rachel.",
      "M": "Now Laban had two daughters; the name of the older was Leah, and the name of the younger was Rachel.",
      "T": "Laban had two daughters—the older was named Leah and the younger was Rachel."
    },
    "17": {
      "L": "Leah's eyes were tender, but Rachel was beautiful in form and appearance.",
      "M": "Leah had soft eyes, but Rachel had a lovely figure and was beautiful.",
      "T": "Leah's eyes were soft and gentle, while Rachel was strikingly beautiful in every way."
    },
    "18": {
      "L": "Jacob loved Rachel. And he said, 'I will serve you seven years for your younger daughter Rachel.'",
      "M": "Jacob was in love with Rachel and said, 'I'll work for you seven years in return for your younger daughter Rachel.'",
      "T": "Jacob had fallen in love with Rachel, so he said, 'I will work for you seven years in exchange for your younger daughter Rachel.'"
    },
    "19": {
      "L": "Laban said, 'It is better that I give her to you than that I should give her to any other man; stay with me.'",
      "M": "Laban said, 'It's better that I give her to you than to some other man. Stay here with me.'",
      "T": "Laban said, 'Better to give her to you than to a stranger. Stay here with me.'"
    },
    "20": {
      "L": "So Jacob served seven years for Rachel, and they seemed to him but a few days because of the love he had for her.",
      "M": "So Jacob served seven years to get Rachel, but they seemed like only a few days to him because of his love for her.",
      "T": "Jacob worked seven years to win Rachel, but the years felt like only a few days to him because of his love for her."
    },
    "21": {
      "L": "Then Jacob said to Laban, 'Give me my wife that I may go in to her, for my time is completed.'",
      "M": "Then Jacob said to Laban, 'Give me my wife. My time is completed, and I want to make her my wife.'",
      "T": "When the seven years were up, Jacob said to Laban, 'Give me my wife. My time is complete—I am ready to marry her.'"
    },
    "22": {
      "L": "So Laban gathered together all the people of the place and made a feast.",
      "M": "So Laban brought together all the people of the place and gave a feast.",
      "T": "So Laban gathered everyone in the area and held a wedding feast."
    },
    "23": {
      "L": "But in the evening he took his daughter Leah and brought her to Jacob, and he went in to her.",
      "M": "But when evening came, he took his daughter Leah and brought her to Jacob, and Jacob made love to her.",
      "T": "But when night fell, Laban brought his daughter Leah to Jacob, and Jacob was intimate with her."
    },
    "24": {
      "L": "(Laban gave his female servant Zilpah to his daughter Leah to be her servant.)",
      "M": "(Laban gave his servant Zilpah to his daughter as her attendant.)",
      "T": "(Laban gave his servant Zilpah to Leah as her personal attendant.)"
    },
    "25": {
      "L": "And in the morning, behold, it was Leah! And Jacob said to Laban, 'What is this you have done to me? Did I not serve with you for Rachel? Why then have you deceived me?'",
      "M": "When morning came, there was Leah! So Jacob said to Laban, 'What is this you have done to me? I served you for Rachel, didn't I? Why have you deceived me?'",
      "T": "When morning came, Jacob discovered it was Leah. He confronted Laban: 'What have you done to me? I worked for Rachel! Why did you deceive me?'"
    },
    "26": {
      "L": "Laban said, 'It is not so done in our place to give the younger before the firstborn.'",
      "M": "Laban replied, 'It is not our custom here to give the younger daughter in marriage before the older one.'",
      "T": "Laban said, 'In our country we don't give the younger daughter in marriage before the older.'"
    },
    "27": {
      "L": "'Complete the week of this one, and we will give you the other also in return for serving me another seven years.'",
      "M": "'Finish this daughter's bridal week; then we will give you the younger one also, in return for another seven years of work.'",
      "T": "'Finish out this wedding week, and I will give you Rachel too—in exchange for another seven years of work.'"
    },
    "28": {
      "L": "Jacob did so, and completed her week. Then Laban gave him his daughter Rachel to be his wife.",
      "M": "And Jacob did so. He finished the week with Leah, and then Laban gave him his daughter Rachel to be his wife.",
      "T": "Jacob agreed, and when the wedding week was over, Laban gave him his daughter Rachel as his wife."
    },
    "29": {
      "L": "(Laban gave his female servant Bilhah to his daughter Rachel to be her servant.)",
      "M": "(Laban gave his servant Bilhah to his daughter Rachel as her attendant.)",
      "T": "(Laban gave his servant Bilhah to Rachel as her personal attendant.)"
    },
    "30": {
      "L": "So Jacob went in to Rachel also, and he loved Rachel more than Leah, and served Laban for another seven years.",
      "M": "Jacob made love to Rachel also, and his love for Rachel was greater than his love for Leah. And he worked for Laban another seven years.",
      "T": "Jacob was intimate with Rachel also, and he loved Rachel far more than Leah. He worked for Laban for another seven years."
    },
    "31": {
      "L": "When the LORD saw that Leah was hated, he opened her womb, but Rachel was barren.",
      "M": "When the LORD saw that Leah was not loved, he enabled her to conceive, but Rachel remained childless.",
      "T": "The LORD saw that Leah was unloved and opened her womb. Rachel, meanwhile, remained unable to conceive."
    },
    "32": {
      "L": "And Leah conceived and bore a son, and she called his name Reuben, for she said, 'Because the LORD has looked upon my affliction; for now my husband will love me.'",
      "M": "Leah became pregnant and gave birth to a son. She named him Reuben, for she said, 'It is because the LORD has seen my misery. Surely my husband will love me now.'",
      "T": "Leah became pregnant and gave birth to a son. She named him Reuben—'See, a Son!'—saying, 'The LORD has seen my suffering. Surely now my husband will love me.'"
    },
    "33": {
      "L": "She conceived again and bore a son, and said, 'Because the LORD has heard that I am hated, he has given me this son also.' And she called his name Simeon.",
      "M": "She conceived again, and when she gave birth to a son she said, 'Because the LORD heard that I am not loved, he gave me this one too.' So she named him Simeon.",
      "T": "She conceived again and bore a son. She said, 'The LORD heard that I am unloved, and he gave me this son too.' She named him Simeon—'God Has Heard.'"
    },
    "34": {
      "L": "Again she conceived and bore a son, and said, 'Now this time my husband will be attached to me, because I have borne him three sons.' Therefore his name was called Levi.",
      "M": "Again she conceived, and when she gave birth to a son she said, 'Now at last my husband will become attached to me, because I have borne him three sons.' So he was named Levi.",
      "T": "She conceived again and bore a third son. She said, 'Now surely my husband will be joined to me—I have given him three sons!' She named him Levi—'Joined.'"
    },
    "35": {
      "L": "And she conceived again and bore a son, and said, 'This time I will praise the LORD.' Therefore she called his name Judah. Then she ceased bearing.",
      "M": "She conceived again, and when she gave birth to a son she said, 'This time I will praise the LORD.' So she named him Judah. Then she stopped having children.",
      "T": "She conceived once more and bore a fourth son. This time she said, 'Now I will simply praise the LORD.' She named him Judah—'Praise.' Then she stopped bearing children."
    }
  },
  "30": {
    "1": {
      "L": "When Rachel saw that she bore Jacob no children, she envied her sister. She said to Jacob, 'Give me children, or I shall die!'",
      "M": "When Rachel saw that she was not bearing Jacob any children, she became jealous of her sister. So she said to Jacob, 'Give me children, or I'll die!'",
      "T": "When Rachel saw that she was not giving Jacob any children, she became jealous of her sister. She said to Jacob, 'Give me children, or I will die!'"
    },
    "2": {
      "L": "Jacob's anger was kindled against Rachel, and he said, 'Am I in the place of God, who has withheld from you the fruit of the womb?'",
      "M": "Jacob became angry with her and said, 'Am I in the place of God, who has kept you from having children?'",
      "T": "Jacob's anger flared against Rachel. He said, 'Am I God? It is he who has kept you from having children, not me!'"
    },
    "3": {
      "L": "Then she said, 'Here is my servant Bilhah; go in to her, so that she may give birth on my behalf, that even I may have children through her.'",
      "M": "Then she said, 'Here is Bilhah, my servant. Sleep with her so that she can bear children for me and I too can have a family through her.'",
      "T": "'Here is my servant Bilhah,' she said. 'Be intimate with her so that she can bear children as my surrogate—I can build a family through her.'"
    },
    "4": {
      "L": "So she gave him her servant Bilhah as a wife, and Jacob went in to her.",
      "M": "So she gave him her servant Bilhah as a wife. Jacob slept with her,",
      "T": "So she gave her servant Bilhah to Jacob as a wife, and he was intimate with her."
    },
    "5": {
      "L": "And Bilhah conceived and bore Jacob a son.",
      "M": "and she became pregnant and bore him a son.",
      "T": "Bilhah conceived and bore Jacob a son."
    },
    "6": {
      "L": "Then Rachel said, 'God has judged me, and has also heard my voice and given me a son.' Therefore she called his name Dan.",
      "M": "Then Rachel said, 'God has vindicated me; he has listened to my plea and given me a son.' Because of this she named him Dan.",
      "T": "Rachel said, 'God has vindicated me! He heard my plea and gave me a son.' She named him Dan—'He Judged' or 'Vindicated.'"
    },
    "7": {
      "L": "Rachel's servant Bilhah conceived again and bore Jacob a second son.",
      "M": "Rachel's servant Bilhah conceived again and bore Jacob a second son.",
      "T": "Bilhah conceived again and bore Jacob a second son."
    },
    "8": {
      "L": "Then Rachel said, 'With mighty wrestlings I have wrestled with my sister and have prevailed.' So she called his name Naphtali.",
      "M": "Then Rachel said, 'I have had a great struggle with my sister, and I have won.' So she named him Naphtali.",
      "T": "Rachel said, 'I have wrestled mightily with my sister, and I have won!' She named him Naphtali—'My Wrestling.'"
    },
    "9": {
      "L": "When Leah saw that she had ceased bearing children, she took her servant Zilpah and gave her to Jacob as a wife.",
      "M": "When Leah saw that she had stopped having children, she took her servant Zilpah and gave her to Jacob as a wife.",
      "T": "When Leah saw that she had stopped bearing children, she gave her servant Zilpah to Jacob as a wife."
    },
    "10": {
      "L": "Then Leah's servant Zilpah bore Jacob a son.",
      "M": "Leah's servant Zilpah bore Jacob a son.",
      "T": "Leah's servant Zilpah bore Jacob a son."
    },
    "11": {
      "L": "And Leah said, 'Good fortune has come!' so she called his name Gad.",
      "M": "Then Leah said, 'What good fortune!' So she named him Gad.",
      "T": "Leah said, 'What good fortune has come!' She named him Gad—'Fortune' or 'Good Luck.'"
    },
    "12": {
      "L": "Leah's servant Zilpah bore Jacob a second son.",
      "M": "Leah's servant Zilpah bore Jacob a second son.",
      "T": "Zilpah bore Jacob a second son."
    },
    "13": {
      "L": "And Leah said, 'Happy am I! For women have called me happy.' So she called his name Asher.",
      "M": "Then Leah said, 'How happy I am! The women will call me happy.' So she named him Asher.",
      "T": "Leah said, 'How blessed I am! The women around me will call me blessed.' She named him Asher—'Happy' or 'Blessed.'"
    },
    "14": {
      "L": "In the days of wheat harvest Reuben went and found mandrakes in the field and brought them to his mother Leah. Then Rachel said to Leah, 'Please give me some of your son's mandrakes.'",
      "M": "During wheat harvest, Reuben went out into the fields and found some mandrake plants, which he brought to his mother Leah. Rachel said to Leah, 'Please give me some of your son's mandrakes.'",
      "T": "During the wheat harvest, Reuben found some mandrake plants in the field and brought them to his mother Leah. Rachel said to Leah, 'Please share some of those mandrakes with me.'"
    },
    "15": {
      "L": "But she said to her, 'Is it a small matter that you have taken away my husband? Would you take away my son's mandrakes also?' Rachel said, 'Then he may lie with you tonight in exchange for your son's mandrakes.'",
      "M": "'Wasn't it enough that you took away my husband? Will you take my son's mandrakes too?' 'Very well,' Rachel said, 'he can sleep with you tonight in return for your son's mandrakes.'",
      "T": "Leah shot back, 'Was it not enough to take my husband from me? Now you want my son's mandrakes too?' Rachel said, 'All right—Jacob can sleep with you tonight in exchange for your son's mandrakes.'"
    },
    "16": {
      "L": "When Jacob came from the field in the evening, Leah went out to meet him and said, 'You must come in to me, for I have hired you with my son's mandrakes.' So he lay with her that night.",
      "M": "So when Jacob came in from the fields that evening, Leah went out to meet him. 'You must sleep with me,' she said. 'I have hired you with my son's mandrakes.' So he slept with her that night.",
      "T": "When Jacob came in from the fields that evening, Leah went out to meet him. 'You are coming to me tonight,' she said. 'I have paid for you with my son's mandrakes.' So he slept with her that night."
    },
    "17": {
      "L": "And God listened to Leah, and she conceived and bore Jacob a fifth son.",
      "M": "God listened to Leah, and she became pregnant and bore Jacob a fifth son.",
      "T": "God heard Leah's prayer, and she conceived and bore Jacob a fifth son."
    },
    "18": {
      "L": "Leah said, 'God has given me my wages because I gave my servant to my husband.' So she called his name Issachar.",
      "M": "Then Leah said, 'God has rewarded me for giving my servant to my husband.' So she named him Issachar.",
      "T": "Leah said, 'God has given me my reward for giving my servant to my husband.' She named him Issachar—'Reward.'"
    },
    "19": {
      "L": "And Leah conceived again, and she bore Jacob a sixth son.",
      "M": "Leah conceived again and bore Jacob a sixth son.",
      "T": "Leah conceived again and bore Jacob a sixth son."
    },
    "20": {
      "L": "Then Leah said, 'God has endowed me with a good endowment; now my husband will honor me, because I have borne him six sons.' So she called his name Zebulun.",
      "M": "Then Leah said, 'God has presented me with a precious gift. This time my husband will treat me with honor, because I have borne him six sons.' So she named him Zebulun.",
      "T": "Leah said, 'God has given me a precious gift. Now my husband will surely honor me—I have given him six sons!' She named him Zebulun—'Honor' or 'Gift.'"
    },
    "21": {
      "L": "Afterward she bore a daughter and called her name Dinah.",
      "M": "Some time later she gave birth to a daughter and named her Dinah.",
      "T": "Later, Leah gave birth to a daughter and named her Dinah."
    },
    "22": {
      "L": "Then God remembered Rachel, and God listened to her and opened her womb.",
      "M": "Then God remembered Rachel; he listened to her and enabled her to conceive.",
      "T": "Then God remembered Rachel. He heard her prayer and opened her womb."
    },
    "23": {
      "L": "She conceived and bore a son and said, 'God has taken away my reproach.'",
      "M": "She became pregnant and gave birth to a son and said, 'God has taken away my disgrace.'",
      "T": "She conceived and bore a son and said, 'God has removed my shame.'"
    },
    "24": {
      "L": "And she called his name Joseph, saying, 'May the LORD add to me another son!'",
      "M": "She named him Joseph, and said, 'May the LORD add to me another son.'",
      "T": "She named him Joseph—'May He Add'—saying, 'May the LORD give me yet another son!'"
    },
    "25": {
      "L": "As soon as Rachel had borne Joseph, Jacob said to Laban, 'Send me away, that I may go to my own home and country.'",
      "M": "After Rachel gave birth to Joseph, Jacob said to Laban, 'Send me on my way so I can go back to my own homeland.'",
      "T": "After Rachel gave birth to Joseph, Jacob said to Laban, 'Let me go home to my own country.'"
    },
    "26": {
      "L": "'Give me my wives and my children for whom I have served you, that I may go, for you know the service I have rendered you.'",
      "M": "'Give me my wives and children, for whom I have served you, and I will be on my way. You know how much work I've done for you.'",
      "T": "'Let me take my wives and children—I have earned them through my service to you. You know very well how hard I have worked for you.'"
    },
    "27": {
      "L": "But Laban said to him, 'If I have found favor in your sight, I have learned by divination that the LORD has blessed me because of you.'",
      "M": "But Laban said to him, 'If I have found favor in your eyes, please stay. I have learned by divination that the LORD has blessed me because of you.'",
      "T": "But Laban said, 'If I have found favor with you, please stay. I have discovered through divination that the LORD has blessed me because of you.'"
    },
    "28": {
      "L": "He added, 'Name your wages, and I will give it.'",
      "M": "He added, 'Name your price, and I will pay it.'",
      "T": "'Name whatever wages you want,' he added, 'and I will pay them.'"
    },
    "29": {
      "L": "Jacob said to him, 'You yourself know how I have served you, and how your livestock has fared with me.'",
      "M": "Jacob said to him, 'You know how I have worked for you and how your livestock has fared under my care.'",
      "T": "Jacob said, 'You yourself know how faithfully I have served you, and how your flocks have prospered under my care.'"
    },
    "30": {
      "L": "'For you had little before I came, and it has increased abundantly, and the LORD has blessed you wherever I turned. But now when shall I provide for my own household also?'",
      "M": "'The little you had before I came has increased greatly, and the LORD has blessed you wherever I have been. But now, when am I going to do something for my own family?'",
      "T": "'You had little before I arrived, and now your wealth has grown enormously—because the LORD has blessed you through me. But now it is time for me to provide for my own family.'"
    },
    "31": {
      "L": "Laban said, 'What shall I give you?' Jacob said, 'You shall not give me anything. If you will do this for me, I will again pasture your flock and keep it:'",
      "M": "'What shall I give you?' asked Laban. 'Don't give me anything,' Jacob replied. 'But if you will do this one thing for me, I will go on tending your flocks and watching over them:'",
      "T": "'What do you want?' Laban asked. 'Nothing you have to give outright,' said Jacob. 'But if you agree to this one arrangement, I will keep tending your flocks:'"
    },
    "32": {
      "L": "'let me pass through all your flock today, removing from it every speckled and spotted sheep and every black lamb, and the spotted and speckled among the goats, and they shall be my wages.'",
      "M": "'Let me go through all your flocks today and remove from them every speckled or spotted sheep, every dark-colored lamb and every spotted or speckled goat. They will be my wages.'",
      "T": "'Let me go through all your flocks today and set aside every speckled or spotted sheep, every dark-colored lamb, and every spotted or speckled goat. Those will be my wages.'"
    },
    "33": {
      "L": "'So my honesty will answer for me later, when you come to look into my wages with you. Every one that is not speckled and spotted among the goats and black among the lambs, if found with me, shall be counted stolen.'",
      "M": "'And my honesty will testify for me in the future, whenever you check on the wages you have paid me. Any goat in my possession that is not speckled or spotted, or any lamb that is not dark-colored, will be considered stolen.'",
      "T": "'This way my integrity will be evident to you: whenever you check my wages, any unspeckled goat or non-dark lamb in my possession will have been stolen from you—that is the agreement.'"
    },
    "34": {
      "L": "Laban said, 'Good! Let it be as you have said.'",
      "M": "'Agreed,' said Laban. 'Let it be as you have said.'",
      "T": "'Agreed,' said Laban. 'Let it be exactly as you say.'"
    },
    "35": {
      "L": "But that day Laban removed the male goats that were striped and spotted, and all the female goats that were speckled and spotted, every one that had white on it, and every lamb that was black, and put them in the charge of his sons.",
      "M": "That same day he removed all the male goats that were streaked or spotted, and all the speckled or spotted female goats—all that had white on them—and all the dark-colored lambs, and he had them tended by his sons.",
      "T": "But that very day, Laban removed all the streaked and spotted male goats, all the speckled and spotted female goats, and every dark-colored lamb—every animal that might produce Jacob's wages—and gave them to his sons to tend."
    },
    "36": {
      "L": "And he set a distance of three days' journey between himself and Jacob, and Jacob pastured the rest of Laban's flock.",
      "M": "Then he put a three-day journey between himself and Jacob, while Jacob continued to tend the rest of Laban's flocks.",
      "T": "He put three days' journey between himself and Jacob, leaving Jacob to tend the remaining animals."
    },
    "37": {
      "L": "Then Jacob took fresh sticks of poplar and almond and plane trees, and peeled white stripes in them, exposing the white of the sticks.",
      "M": "Jacob, however, took fresh-cut branches from poplar, almond and plane trees and made white stripes on them by peeling the bark and exposing the white inner wood of the branches.",
      "T": "Jacob took freshly cut branches from poplar, almond, and plane trees and peeled back the bark in white streaks, exposing the pale wood beneath."
    },
    "38": {
      "L": "He set the sticks that he had peeled in front of the flocks in the troughs, that is, the watering places, where the flocks came to drink. And since they bred when they came to drink,",
      "M": "Then he placed the peeled branches in all the watering troughs, so that they would be directly in front of the flocks when they came to drink. When the flocks were in heat and came to drink,",
      "T": "He placed these peeled branches in the watering troughs where the flocks came to drink, so that the animals would see them when they mated."
    },
    "39": {
      "L": "the flocks bred in front of the sticks and so the flocks brought forth striped, speckled, and spotted.",
      "M": "they mated in front of the branches. And they bore young that were streaked or speckled or spotted.",
      "T": "The flocks mated in front of the branches and gave birth to streaked, speckled, and spotted young."
    },
    "40": {
      "L": "And Jacob separated the lambs and set the faces of the flocks toward the striped and all the black in the flock of Laban. He put his own droves apart and did not put them with Laban's flock.",
      "M": "Jacob set apart the young of the flock and had the flocks face in the direction of the streaked and dark-colored animals that belonged to Laban. This way he made separate flocks for himself and did not put them with Laban's animals.",
      "T": "Jacob then separated the streaked and dark animals, and he made the rest of the flock face toward the striped and dark animals in Laban's flock. In this way he built up his own separate flocks, keeping them apart from Laban's."
    },
    "41": {
      "L": "Whenever the stronger of the flock were breeding, Jacob would lay the sticks in the troughs before the eyes of the flock, that they might breed among the sticks,",
      "M": "Whenever the stronger females were in heat, Jacob would place the branches in the troughs in front of the animals so they would mate near the branches.",
      "T": "Whenever the stronger animals mated, Jacob placed the branches before them at the troughs, so they would conceive while looking at the branches."
    },
    "42": {
      "L": "but for the feebler of the flock he would not lay them there. So the feebler would be Laban's, and the stronger Jacob's.",
      "M": "But if the animals were weak, he would not place the branches there. So the weak animals went to Laban and the strong ones to Jacob.",
      "T": "But when the weaker animals mated, he did not put the branches out. So the weaker animals went to Laban and the stronger ones became Jacob's."
    },
    "43": {
      "L": "Thus the man increased greatly and had large flocks, female servants and male servants, and camels and donkeys.",
      "M": "In this way the man grew exceedingly prosperous and came to own large flocks, and female and male servants, and camels and donkeys.",
      "T": "In this way Jacob grew enormously prosperous: large flocks, male and female servants, camels and donkeys."
    }
  }
}

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'genesis')
    merge_tier(data, GENESIS, key)
    save(tier, 'genesis', data)

print('\nGenesis 26–30 written to all three tiers. Run mkt-genesis-31-36.py for chapters 31–36.')
print('Chapters covered:', sorted(GENESIS.keys(), key=int))
