"""
MKT Genesis chapters 37-43 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-genesis-37-43.py

Covers the Joseph narrative: his coat and dreams, sale into slavery, Judah and Tamar,
Joseph in Potiphar's house, the prison dreams, Pharaoh's dreams and Joseph's rise,
and the first two journeys of the brothers to Egypt.

Translation decisions:
- H3068 (יהוה): "the LORD" throughout — personal divine name rendered with small-caps convention
- H430 (אֱלֹהִים): "God" — standard rendering
- H2617 (חֶסֶד) at 39:21: L="steadfast love", M="unfailing love", T="faithful covenant loyalty"
- H5315 (נֶפֶשׁ) at 42:21: rendered as "anguish/distress/suffering" — embodied self, not immaterial soul
- כְּתֹנֶת פַּסִּים (37:3): "robe of many colors" (traditional) / "long-sleeved robe" also attested;
  retains the traditional rendering since the narrative weight is the gift itself, not the garment type
- אַבְרֵךְ (41:43): "Bow the knee!" — ancient salutation of uncertain etymology; sense is "make way / give honor"
- Potiphar's title: "captain of the guard" — consistent with Gen 37:36
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
  "37": {
    "1": {
      "L": "And Jacob dwelt in the land of his father's sojournings, in the land of Canaan.",
      "M": "Jacob lived in the land where his father had stayed, the land of Canaan.",
      "T": "Jacob settled in the land of Canaan, where his father had lived as a foreigner."
    },
    "2": {
      "L": "These are the generations of Jacob. Joseph, being seventeen years old, was pasturing the flock with his brothers. He was a boy with the sons of Bilhah and the sons of Zilpah, his father's wives. And Joseph brought a bad report of them to their father.",
      "M": "This is the account of Jacob's family line. Joseph, a young man of seventeen, was tending the flocks with his brothers, the sons of Bilhah and the sons of Zilpah, his father's wives, and he brought their father a bad report about them.",
      "T": "This is the story of Jacob's family. Joseph was seventeen years old and worked as a shepherd alongside his brothers—the sons of Bilhah and Zilpah, his father's wives. He brought his father bad reports about them."
    },
    "3": {
      "L": "Now Israel loved Joseph more than any other of his sons, because he was the son of his old age. And he made him a robe of many colors.",
      "M": "Now Israel loved Joseph more than any of his other sons, because he had been born to him in his old age; and he made an ornate robe for him.",
      "T": "Now Israel loved Joseph more than any of his other sons, because Joseph had been born to him in his old age. He gave him a richly ornamented robe."
    },
    "4": {
      "L": "But when his brothers saw that their father loved him more than all his brothers, they hated him and could not speak peaceably to him.",
      "M": "When his brothers saw that their father loved him more than any of them, they hated him and could not say a kind word to him.",
      "T": "When his brothers saw that their father loved Joseph more than all of them, they hated Joseph so deeply that they could not speak a civil word to him."
    },
    "5": {
      "L": "Now Joseph dreamed a dream and told it to his brothers, and they hated him even more.",
      "M": "Joseph had a dream, and when he told it to his brothers, they hated him all the more.",
      "T": "Joseph had a dream, and when he told his brothers about it, their hatred for him grew even deeper."
    },
    "6": {
      "L": "He said to them, 'Hear this dream that I have dreamed:'",
      "M": "He said to them, 'Listen to this dream I had:'",
      "T": "He said, 'Listen to what I dreamed:'"
    },
    "7": {
      "L": "'Behold, we were binding sheaves in the field, and behold, my sheaf arose and stood upright. And behold, your sheaves gathered around it and bowed down to my sheaf.'",
      "M": "'We were binding sheaves of grain out in the field when suddenly my sheaf rose and stood upright, while your sheaves gathered around mine and bowed down to it.'",
      "T": "'We were out in the field binding bundles of grain. Suddenly my bundle stood up straight, and all your bundles gathered around it and bowed down to mine.'"
    },
    "8": {
      "L": "His brothers said to him, 'Are you indeed to reign over us? Or are you indeed to rule over us?' So they hated him even more for his dreams and for his words.",
      "M": "His brothers said to him, 'Do you intend to reign over us? Will you actually rule us?' And they hated him all the more because of his dream and what he had said.",
      "T": "His brothers shot back, 'So you think you're going to rule over us? You think you'll be our king?' They hated him even more because of his dreams and the things he said."
    },
    "9": {
      "L": "Then he dreamed another dream and told it to his brothers and said, 'Behold, I have dreamed another dream. Behold, the sun, the moon, and eleven stars were bowing down to me.'",
      "M": "Then he had another dream, and he told it to his brothers. 'Listen,' he said, 'I had another dream, and this time the sun and moon and eleven stars were bowing down to me.'",
      "T": "He had another dream and told his brothers about it. 'I had another dream,' he said. 'This time the sun, the moon, and eleven stars all bowed down to me.'"
    },
    "10": {
      "L": "But when he told it to his father and to his brothers, his father rebuked him and said to him, 'What is this dream that you have dreamed? Shall I and your mother and your brothers indeed come to bow ourselves to the ground before you?'",
      "M": "When he told his father as well as his brothers, his father rebuked him and said, 'What is this dream you had? Will your mother and I and your brothers actually come and bow down to the ground before you?'",
      "T": "When he told his father and his brothers, his father scolded him. 'What kind of dream is that?' he said. 'Do you really think your mother and I and your brothers will come and bow down before you?'"
    },
    "11": {
      "L": "And his brothers were jealous of him, but his father kept the saying in mind.",
      "M": "His brothers were jealous of him, but his father kept the matter in mind.",
      "T": "His brothers were filled with jealousy. But his father kept thinking about it."
    },
    "12": {
      "L": "Now his brothers went to pasture their father's flock near Shechem.",
      "M": "Now his brothers had gone to graze their father's flocks near Shechem,",
      "T": "Some time later, his brothers went to graze their father's flocks near Shechem."
    },
    "13": {
      "L": "And Israel said to Joseph, 'Are not your brothers pasturing the flock at Shechem? Come, I will send you to them.' And he said to him, 'Here I am.'",
      "M": "and Israel said to Joseph, 'As you know, your brothers are grazing the flocks near Shechem. Come, I am going to send you to them.' 'Very well,' he replied.",
      "T": "Israel said to Joseph, 'Your brothers are grazing the flocks near Shechem. Come, I'll send you to them.' Joseph replied, 'I'm ready.'"
    },
    "14": {
      "L": "So he said to him, 'Go now, see if it is well with your brothers and well with the flock, and bring me word.' So he sent him from the Valley of Hebron, and he came to Shechem.",
      "M": "So he said to him, 'Go and see how your brothers and the flocks are getting on and bring word back to me.' Then he sent him off from the Valley of Hebron. When Joseph arrived at Shechem,",
      "T": "His father told him, 'Go and see how your brothers and the flocks are doing, and come back and tell me.' He sent Joseph from the Valley of Hebron. When Joseph arrived at Shechem,"
    },
    "15": {
      "L": "a man found him wandering in the fields. And the man asked him, 'What are you seeking?'",
      "M": "a man found him wandering around in the fields and asked him, 'What are you looking for?'",
      "T": "a man found him wandering in the open country. 'What are you looking for?' the man asked."
    },
    "16": {
      "L": "'I am seeking my brothers,' he said. 'Tell me, please, where they are pasturing the flock.'",
      "M": "He replied, 'I'm looking for my brothers. Can you tell me where they are grazing their flocks?'",
      "T": "Joseph said, 'I'm trying to find my brothers. Can you tell me where they are grazing their flocks?'"
    },
    "17": {
      "L": "And the man said, 'They have gone away, for I heard them say, \"Let us go to Dothan.\"' So Joseph went after his brothers and found them at Dothan.",
      "M": "'They have moved on from here,' the man answered. 'I heard them say, \"Let's go to Dothan.\"' So Joseph went after his brothers and found them near Dothan.",
      "T": "'They've moved on,' the man said. 'I heard them say they were going to Dothan.' So Joseph went after his brothers and found them at Dothan."
    },
    "18": {
      "L": "They saw him from afar, and before he came near to them they conspired against him to kill him.",
      "M": "But they saw him in the distance, and before he reached them, they plotted to kill him.",
      "T": "They spotted him in the distance, and before he even reached them they were already plotting to kill him."
    },
    "19": {
      "L": "They said to one another, 'Here comes this dreamer.'",
      "M": "'Here comes that dreamer!' they said to each other.",
      "T": "They said to each other, 'Here comes the dreamer!'"
    },
    "20": {
      "L": "'Come now, let us kill him and throw him into one of the pits. Then we will say that a fierce animal has devoured him, and we will see what will become of his dreams.'",
      "M": "'Come now, let's kill him and throw him into one of these cisterns and say that a ferocious animal devoured him. Then we'll see what comes of his dreams.'",
      "T": "'Let's kill him and throw him into one of these cisterns. We can say a wild animal ate him. Then we'll see what becomes of his precious dreams!'"
    },
    "21": {
      "L": "But when Reuben heard it, he rescued him out of their hands, saying, 'Let us not take his life.'",
      "M": "When Reuben heard this, he tried to rescue him from their hands. 'Let's not take his life,' he said.",
      "T": "But Reuben heard the plan and tried to save Joseph. 'Let's not kill him,' he said."
    },
    "22": {
      "L": "And Reuben said to them, 'Shed no blood; throw him into this pit here in the wilderness, but do not lay a hand on him'—that he might rescue him out of their hand to restore him to his father.",
      "M": "'Don't shed any blood. Throw him into this cistern here in the wilderness, but don't lay a hand on him.' Reuben said this to rescue him from them and take him back to his father.",
      "T": "'Don't shed his blood,' Reuben said. 'Throw him into this cistern out here in the wilderness, but don't lay a hand on him.' He planned to come back later and rescue Joseph and return him to their father."
    },
    "23": {
      "L": "So when Joseph came to his brothers, they stripped him of his robe, the robe of many colors that he wore.",
      "M": "So when Joseph came to his brothers, they stripped him of his robe—the ornate robe he was wearing—",
      "T": "When Joseph arrived, his brothers tore off his ornate robe"
    },
    "24": {
      "L": "And they took him and threw him into a pit. The pit was empty; there was no water in it.",
      "M": "and they took him and threw him into the cistern. Now the cistern was empty; there was no water in it.",
      "T": "and threw him into a cistern. It was empty—no water, just a dry pit."
    },
    "25": {
      "L": "Then they sat down to eat. And looking up they saw a caravan of Ishmaelites coming from Gilead, with their camels bearing gum, balm, and myrrh, on their way to carry it down to Egypt.",
      "M": "As they sat down to eat their meal, they looked up and saw a caravan of Ishmaelites coming from Gilead. Their camels were loaded with spices, balm and myrrh, and they were on their way to take them down to Egypt.",
      "T": "Then they sat down to eat. Looking up, they saw a caravan of Ishmaelite traders approaching from Gilead, their camels loaded with spices, balm, and myrrh, bound for Egypt."
    },
    "26": {
      "L": "Then Judah said to his brothers, 'What profit is it if we kill our brother and conceal his blood?'",
      "M": "Judah said to his brothers, 'What will we gain if we kill our brother and cover up his blood?'",
      "T": "Judah said to his brothers, 'What do we gain by killing our brother and hiding his blood?'"
    },
    "27": {
      "L": "'Come, let us sell him to the Ishmaelites, and let not our hand be upon him, for he is our brother, our own flesh.' And his brothers listened to him.",
      "M": "'Come, let's sell him to the Ishmaelites and not lay our hands on him; after all, he is our brother, our own flesh and blood.' His brothers agreed.",
      "T": "'Let's sell him to the Ishmaelites instead. That way we won't have blood on our hands—he is our brother, our own flesh and blood.' His brothers agreed."
    },
    "28": {
      "L": "Then Midianite traders passed by. And they drew Joseph up and lifted him out of the pit, and sold him to the Ishmaelites for twenty pieces of silver. They took Joseph to Egypt.",
      "M": "So when the Midianite merchants came by, his brothers pulled Joseph up out of the cistern and sold him for twenty shekels of silver to the Ishmaelites, who took him to Egypt.",
      "T": "So when the Midianite traders came by, his brothers hauled Joseph up from the cistern and sold him to the Ishmaelites for twenty pieces of silver. The traders took Joseph to Egypt."
    },
    "29": {
      "L": "When Reuben returned to the pit and saw that Joseph was not in the pit, he tore his clothes",
      "M": "When Reuben returned to the cistern and saw that Joseph was not there, he tore his clothes.",
      "T": "When Reuben came back to the cistern and found Joseph gone, he tore his clothes in grief."
    },
    "30": {
      "L": "and returned to his brothers and said, 'The boy is gone, and I, where shall I go?'",
      "M": "He went back to his brothers and said, 'The boy isn't there! Where can I turn now?'",
      "T": "He went back to his brothers and cried, 'The boy is gone! What am I going to do?'"
    },
    "31": {
      "L": "Then they took Joseph's robe and slaughtered a goat and dipped the robe in the blood.",
      "M": "Then they got Joseph's robe, slaughtered a goat and dipped the robe in the blood.",
      "T": "They took Joseph's robe, slaughtered a goat, and dipped the robe in the blood."
    },
    "32": {
      "L": "And they sent the robe of many colors and brought it to their father and said, 'This we have found; please identify whether it is your son's robe or not.'",
      "M": "They took the ornate robe back to their father and said, 'We found this. Examine it to see whether it is your son's robe.'",
      "T": "They brought the robe to their father and said, 'We found this. Is it your son's robe?'"
    },
    "33": {
      "L": "He identified it and said, 'It is my son's robe. A fierce animal has devoured him. Joseph is surely torn to pieces.'",
      "M": "He recognized it and said, 'It is my son's robe! Some ferocious animal has devoured him. Joseph has surely been torn to pieces.'",
      "T": "Jacob recognized it immediately. 'It is my son's robe!' he cried. 'A wild animal has devoured him—Joseph has been torn to pieces!'"
    },
    "34": {
      "L": "Then Jacob tore his garments and put sackcloth on his loins and mourned for his son many days.",
      "M": "Then Jacob tore his clothes, put on sackcloth and mourned for his son many days.",
      "T": "Jacob tore his own clothes, put on sackcloth, and mourned for his son for many days."
    },
    "35": {
      "L": "All his sons and all his daughters rose up to comfort him, but he refused to be comforted and said, 'No, I shall go down to Sheol to my son, mourning.' Thus his father wept for him.",
      "M": "All his sons and daughters came to comfort him, but he refused to be comforted. 'No,' he said, 'I will continue to mourn until I join my son in the grave.' So his father wept for him.",
      "T": "All his sons and daughters came to comfort him, but he refused to be consoled. 'No,' he said, 'I will go to my grave mourning for my son.' And his father wept bitterly for him."
    },
    "36": {
      "L": "Meanwhile the Midianites had sold him in Egypt to Potiphar, an officer of Pharaoh, the captain of the guard.",
      "M": "Meanwhile, the Midianites sold Joseph in Egypt to Potiphar, one of Pharaoh's officials, the captain of the guard.",
      "T": "Meanwhile, the Midianites had sold Joseph in Egypt to a man named Potiphar, one of Pharaoh's officials—the captain of the guard."
    }
  },
  "38": {
    "1": {
      "L": "It happened at that time that Judah went down from his brothers and turned aside to a certain Adullamite, whose name was Hirah.",
      "M": "At that time, Judah left his brothers and went down to stay with a man of Adullam named Hirah.",
      "T": "Around that time, Judah left his brothers and settled with a man from Adullam named Hirah."
    },
    "2": {
      "L": "There Judah saw the daughter of a certain Canaanite whose name was Shua. He took her and went in to her,",
      "M": "There Judah met the daughter of a Canaanite man named Shua. He married her and slept with her;",
      "T": "There Judah met and married the daughter of a Canaanite man named Shua."
    },
    "3": {
      "L": "and she conceived and bore a son, and he called his name Er.",
      "M": "she became pregnant and gave birth to a son, who was named Er.",
      "T": "She became pregnant and gave birth to a son, whom Judah named Er."
    },
    "4": {
      "L": "She conceived again and bore a son, and she called his name Onan.",
      "M": "She conceived again and gave birth to a son and named him Onan.",
      "T": "She conceived again and gave birth to a son she named Onan."
    },
    "5": {
      "L": "Yet again she bore a son, and she called his name Shelah. Judah was in Chezib when she bore him.",
      "M": "She gave birth to still another son and named him Shelah. It was at Chezib that she gave birth to him.",
      "T": "She had a third son and named him Shelah. Judah was at Chezib when Shelah was born."
    },
    "6": {
      "L": "And Judah took a wife for Er his firstborn, and her name was Tamar.",
      "M": "Judah got a wife for Er, his firstborn, and her name was Tamar.",
      "T": "Judah found a wife for his firstborn Er. Her name was Tamar."
    },
    "7": {
      "L": "But Er, Judah's firstborn, was wicked in the sight of the LORD, and the LORD put him to death.",
      "M": "But Er, Judah's firstborn, was wicked in the LORD's sight; so the LORD put him to death.",
      "T": "But Er was wicked in the LORD's eyes, and the LORD put him to death."
    },
    "8": {
      "L": "Then Judah said to Onan, 'Go in to your brother's wife and perform the duty of a brother-in-law to her, and raise up offspring for your brother.'",
      "M": "Then Judah said to Onan, 'Sleep with your brother's wife and fulfill your duty to her as a brother-in-law to raise up offspring for your brother.'",
      "T": "Judah said to Onan, 'Sleep with your brother's wife and fulfill your duty as her brother-in-law, to carry on your brother's line.'"
    },
    "9": {
      "L": "But Onan knew that the offspring would not be his. So whenever he went in to his brother's wife he would waste the semen on the ground, so as not to give offspring to his brother.",
      "M": "But Onan knew that the child would not be his; so whenever he slept with his brother's wife, he spilled his semen on the ground to keep from providing offspring for his brother.",
      "T": "But Onan knew that any child born would not be counted as his heir. So every time he slept with his brother's wife, he prevented conception, refusing to give his brother a descendant."
    },
    "10": {
      "L": "And what he did was wicked in the sight of the LORD, and he put him to death also.",
      "M": "What he did was wicked in the LORD's sight; so the LORD put him to death also.",
      "T": "What Onan did was evil in the LORD's eyes, so the LORD put him to death as well."
    },
    "11": {
      "L": "Then Judah said to Tamar his daughter-in-law, 'Remain a widow in your father's house, till Shelah my son grows up'—for he feared that he would die, like his brothers. So Tamar went and remained in her father's house.",
      "M": "Judah then said to his daughter-in-law Tamar, 'Live as a widow in your father's household until my son Shelah grows up.' For he thought, 'He may die too, just like his brothers.' So Tamar went to live in her father's household.",
      "T": "Judah said to his daughter-in-law Tamar, 'Go back to your father's house and remain a widow until my son Shelah is old enough to marry.' He was afraid that Shelah would die like his brothers. So Tamar went to live in her father's house."
    },
    "12": {
      "L": "In the course of time the wife of Judah, Shua's daughter, died. When Judah was comforted, he went up to Timnah to his sheepshearers, he and his friend Hirah the Adullamite.",
      "M": "After a long time Judah's wife, the daughter of Shua, died. When Judah had recovered from his grief, he went up to Timnah, to the men who were shearing his sheep, and his friend Hirah the Adullamite went with him.",
      "T": "After some time, Judah's wife—the daughter of Shua—died. When Judah had finished his mourning, he went up to Timnah to oversee the shearing of his sheep, accompanied by his friend Hirah the Adullamite."
    },
    "13": {
      "L": "And when Tamar was told, 'Your father-in-law is going up to Timnah to shear his sheep,'",
      "M": "When Tamar was told, 'Your father-in-law is on his way to Timnah to shear his sheep,'",
      "T": "When Tamar learned that her father-in-law was going up to Timnah to shear his sheep,"
    },
    "14": {
      "L": "she took off her widow's garments and covered herself with a veil, wrapping herself up, and sat at the entrance to Enaim, which is on the road to Timnah. For she saw that Shelah was grown up, and she had not been given to him in marriage.",
      "M": "she took off her widow's clothes, covered herself with a veil to disguise herself, and then sat down at the entrance to Enaim, which is on the road to Timnah. For she saw that, though Shelah had now grown up, she had not been given to him as his wife.",
      "T": "she took off her widow's clothes, put on a veil to disguise herself, and sat down at the entrance to Enaim along the road to Timnah. She had realized that Shelah was now grown up but she had not been given to him as his wife."
    },
    "15": {
      "L": "When Judah saw her, he thought she was a prostitute, for she had covered her face.",
      "M": "When Judah saw her, he thought she was a prostitute, for she had covered her face.",
      "T": "When Judah saw her, he thought she was a prostitute, because she had covered her face."
    },
    "16": {
      "L": "He turned to her at the roadside and said, 'Come, let me come in to you,' for he did not know that she was his daughter-in-law. She said, 'What will you give me, that you may come in to me?'",
      "M": "Not realizing that she was his daughter-in-law, he went over to her by the roadside and said, 'Come now, let me sleep with you.' 'And what will you give me to sleep with you?' she asked.",
      "T": "Not knowing she was his daughter-in-law, he approached her and said, 'Come, let me sleep with you.' She asked, 'What will you give me?'"
    },
    "17": {
      "L": "'I will send you a young goat from the flock,' he said. She said, 'If you give me a pledge, until you send it.'",
      "M": "'I'll send you a young goat from my flock,' he said. 'Will you give me something as a pledge until you send it?' she asked.",
      "T": "'I'll send you a goat from my flock,' he said. She replied, 'Only if you give me a pledge until it arrives.'"
    },
    "18": {
      "L": "He said, 'What pledge shall I give you?' She replied, 'Your signet and your cord and your staff that is in your hand.' So he gave them to her and went in to her, and she conceived by him.",
      "M": "He said, 'What pledge should I give you?' 'Your seal and its cord, and the staff in your hand,' she answered. So he gave them to her and slept with her, and she became pregnant by him.",
      "T": "'What kind of pledge?' he asked. 'Your seal with its cord, and the staff you're carrying,' she said. He gave them to her and slept with her, and she became pregnant by him."
    },
    "19": {
      "L": "Then she arose and went away, and taking off her veil she put on the garments of her widowhood.",
      "M": "After she left, she took off her veil and put on her widow's clothes again.",
      "T": "After he left, she removed her veil and put her widow's clothes back on."
    },
    "20": {
      "L": "When Judah sent the young goat by his friend the Adullamite to take back the pledge from the woman's hand, he did not find her.",
      "M": "Meanwhile Judah sent the young goat by his friend the Adullamite in order to get his pledge back from the woman, but he did not find her.",
      "T": "Judah sent his Adullamite friend back with the young goat to reclaim his pledge, but the man could not find the woman."
    },
    "21": {
      "L": "And he asked the men of the place, 'Where is the cult prostitute who was at Enaim at the roadside?' And they said, 'No cult prostitute has been here.'",
      "M": "He asked the men who lived there, 'Where is the shrine prostitute who was beside the road at Enaim?' 'There hasn't been any shrine prostitute here,' they said.",
      "T": "He asked the men of that place, 'Where is the woman who was sitting by the road at Enaim?' They said, 'There has been no such woman here.'"
    },
    "22": {
      "L": "So he returned to Judah and said, 'I did not find her. Also, the men of the place said, \"No cult prostitute has been here.\"'",
      "M": "So he went back to Judah and said, 'I didn't find her. Besides, the men who lived there said, \"There hasn't been any shrine prostitute here.\"'",
      "T": "He returned to Judah and said, 'I couldn't find her. The men of the place even told me there was no such woman there.'"
    },
    "23": {
      "L": "And Judah said, 'Let her keep the things as her own, or we shall be laughed at. You see, I sent this young goat, and you did not find her.'",
      "M": "Then Judah said, 'Let her keep what she has, or we will become a laughingstock. After all, I did send her this young goat, but you didn't find her.'",
      "T": "Judah said, 'Then let her keep what she has. We don't want to be made a laughingstock. I sent the goat as agreed, but you couldn't find her.'"
    },
    "24": {
      "L": "About three months later Judah was told, 'Tamar your daughter-in-law has been immoral. Moreover, she is pregnant by immorality.' And Judah said, 'Bring her out, and let her be burned.'",
      "M": "About three months later Judah was told, 'Your daughter-in-law Tamar is guilty of prostitution, and as a result she is now pregnant.' Judah said, 'Bring her out and have her burned to death!'",
      "T": "About three months later Judah received this report: 'Your daughter-in-law Tamar has acted like a prostitute—in fact, she is pregnant.' Judah said, 'Bring her out and have her burned!'"
    },
    "25": {
      "L": "As she was being brought out, she sent word to her father-in-law, 'By the man to whom these belong, I am pregnant.' And she said, 'Please identify whose these are, the signet and the cord and the staff.'",
      "M": "As she was being brought out, she sent a message to her father-in-law. 'I am pregnant by the man who owns these,' she said. And she added, 'See if you recognize whose seal and cord and staff these are.'",
      "T": "As they were bringing her out, she sent a message to her father-in-law: 'I am pregnant by the man who owns these things.' She added, 'Do you recognize this seal and cord and staff?'"
    },
    "26": {
      "L": "Judah identified them and said, 'She is more righteous than I, since I did not give her to my son Shelah.' And he did not know her again.",
      "M": "Judah recognized them and said, 'She is more righteous than I, since I wouldn't give her to my son Shelah.' And he did not sleep with her again.",
      "T": "Judah recognized them and said, 'She is more in the right than I am, because I withheld my son Shelah from her.' He did not sleep with her again."
    },
    "27": {
      "L": "When the time of her labor came, there were twins in her womb.",
      "M": "When the time came for her to give birth, there were twin boys in her womb.",
      "T": "When it was time for her to give birth, there were twins in her womb."
    },
    "28": {
      "L": "And when she was in labor, one put out a hand, and the midwife took and tied a scarlet thread on his hand, saying, 'This one came out first.'",
      "M": "As she was giving birth, one of them put out his hand; so the midwife took a scarlet thread and tied it on his wrist and said, 'This one came out first.'",
      "T": "During the birth, one of them reached out his hand, and the midwife tied a scarlet thread on his wrist, saying, 'This one came out first.'"
    },
    "29": {
      "L": "But as he drew back his hand, behold, his brother came out. And she said, 'What a breach you have made for yourself!' Therefore his name was called Perez.",
      "M": "But when he drew back his hand, his brother came out, and she said, 'So this is how you have broken out!' And he was named Perez.",
      "T": "But he pulled his hand back, and his brother came out instead. 'What a break you've made for yourself!' the midwife exclaimed. So he was named Perez—meaning 'breaking out.'"
    },
    "30": {
      "L": "And afterward his brother came out with the scarlet thread on his hand, and he was called Zerah.",
      "M": "Then his brother, who had the scarlet thread on his wrist, came out. And he was named Zerah.",
      "T": "Then his brother came out with the scarlet thread on his wrist, and he was named Zerah."
    }
  },
  "39": {
    "1": {
      "L": "Now Joseph had been brought down to Egypt, and Potiphar, an officer of Pharaoh, the captain of the guard, an Egyptian, had bought him from the Ishmaelites who had brought him down there.",
      "M": "Now Joseph had been taken down to Egypt. Potiphar, an Egyptian who was one of Pharaoh's officials, the captain of the guard, bought him from the Ishmaelites who had taken him there.",
      "T": "Joseph had been taken down to Egypt, where Potiphar—one of Pharaoh's officials, the captain of the guard—had purchased him from the Ishmaelites."
    },
    "2": {
      "L": "The LORD was with Joseph, and he became a successful man, and he was in the house of his Egyptian master.",
      "M": "The LORD was with Joseph so that he prospered, and he lived in the house of his Egyptian master.",
      "T": "The LORD was with Joseph, and he became a man of remarkable success. He lived in the household of his Egyptian master."
    },
    "3": {
      "L": "His master saw that the LORD was with him and that the LORD caused all that he did to succeed in his hands.",
      "M": "When his master saw that the LORD was with him and that the LORD gave him success in everything he did,",
      "T": "His master could see that the LORD was with him—that the LORD made everything Joseph did succeed."
    },
    "4": {
      "L": "So Joseph found favor in his sight and attended him, and he made him overseer of his house and put him in charge of all that he had.",
      "M": "Joseph found favor in his eyes and became his attendant. Potiphar put him in charge of his household, and he entrusted to his care everything he owned.",
      "T": "Joseph won his master's trust and became his personal attendant. Potiphar put him in charge of his entire household and entrusted everything he owned to Joseph's care."
    },
    "5": {
      "L": "From the time that he made him overseer in his house and over all that he had, the LORD blessed the Egyptian's house for Joseph's sake; the blessing of the LORD was on all that he had, in house and field.",
      "M": "From the time Potiphar put him in charge of his household and of all that he owned, the LORD blessed the household of the Egyptian because of Joseph. The blessing of the LORD was on everything Potiphar had, both in the house and in the field.",
      "T": "From the moment Potiphar put Joseph in charge, the LORD blessed the Egyptian's household for Joseph's sake. The LORD's blessing rested on everything Potiphar owned—his house, his fields, everything."
    },
    "6": {
      "L": "So he left all that he had in Joseph's charge, and because of him he had no concern about anything but the food he ate. Now Joseph was handsome in form and appearance.",
      "M": "So Potiphar left everything he had in Joseph's care; with Joseph in charge, he did not concern himself with anything except the food he ate. Now Joseph was well-built and handsome,",
      "T": "Potiphar handed everything over to Joseph's management and concerned himself with nothing except what he ate for dinner. Joseph was well-built and handsome."
    },
    "7": {
      "L": "And after a time his master's wife cast her eyes on Joseph and said, 'Lie with me.'",
      "M": "and after a while his master's wife took notice of Joseph and said, 'Come to bed with me!'",
      "T": "After a while, his master's wife set her eyes on Joseph and said, 'Come to bed with me.'"
    },
    "8": {
      "L": "But he refused and said to his master's wife, 'Behold, because of me my master has no concern about anything in the house, and he has put everything that he has in my charge.'",
      "M": "But he refused. 'With me in charge,' he told her, 'my master does not concern himself with anything in the house; everything he owns he has entrusted to my care.'",
      "T": "But Joseph refused. 'My master has handed everything in this house over to me,' he said. 'He trusts me completely with everything he owns.'"
    },
    "9": {
      "L": "'He is not greater in this house than I am, nor has he kept back anything from me except you, because you are his wife. How then can I do this great wickedness and sin against God?'",
      "M": "'No one is greater in this house than I am. My master has withheld nothing from me except you, because you are his wife. How then could I do such a wicked thing and sin against God?'",
      "T": "'He has not kept anything back from me except you—because you are his wife. How could I do something so wicked? I would be sinning against God.'"
    },
    "10": {
      "L": "And as she spoke to Joseph day after day, he would not listen to her, to lie beside her or to be with her.",
      "M": "And though she spoke to Joseph day after day, he refused to go to bed with her or even to be with her.",
      "T": "Though she pressed him day after day, he refused to sleep with her or even to be alone with her."
    },
    "11": {
      "L": "But one day, when he went into the house to do his work and none of the men of the house was there in the house,",
      "M": "One day he went into the house to attend to his duties, and none of the household servants was inside.",
      "T": "One day Joseph went into the house to do his work, and none of the other household servants were around."
    },
    "12": {
      "L": "she caught him by his garment, saying, 'Lie with me.' But he left his garment in her hand and fled and got out of the house.",
      "M": "She caught him by his cloak and said, 'Come to bed with me!' But he left his cloak in her hand and ran out of the house.",
      "T": "She grabbed him by his cloak and said, 'Come to bed with me!' But Joseph left his cloak in her hand and ran out of the house."
    },
    "13": {
      "L": "And as soon as she saw that he had left his garment in her hand and had fled out of the house,",
      "M": "When she saw that he had left his cloak in her hand and had run out of the house,",
      "T": "When she realized he had left his cloak in her hand and fled,"
    },
    "14": {
      "L": "she called to the men of her household and said to them, 'See, he has brought among us a Hebrew to laugh at us. He came in to me to lie with me, and I cried out with a loud voice.'",
      "M": "she called her household servants. 'Look,' she said to them, 'this Hebrew has been brought to us to make sport of us! He came in here to sleep with me, but I screamed.'",
      "T": "she called the household servants and told them, 'This Hebrew slave was brought in here to make fools of us! He tried to sleep with me, and I screamed.'"
    },
    "15": {
      "L": "'And as soon as he heard that I lifted up my voice and cried out, he left his garment beside me and fled and got out of the house.'",
      "M": "'When he heard me scream for help, he left his cloak beside me and ran out of the house.'",
      "T": "'When he heard me scream, he ran out, leaving his cloak right here.'"
    },
    "16": {
      "L": "Then she laid up his garment by her until his master came home,",
      "M": "She kept his cloak beside her until his master came home.",
      "T": "She kept the cloak beside her until Potiphar came home."
    },
    "17": {
      "L": "and she told him the same story, saying, 'The Hebrew servant, whom you have brought among us, came in to me to laugh at me.'",
      "M": "Then she told him this story: 'That Hebrew slave you brought us came to me to make sport of me.'",
      "T": "Then she told him the same story: 'That Hebrew slave you brought to us came in to make a mockery of me.'"
    },
    "18": {
      "L": "'But as soon as I lifted up my voice and cried, he left his garment beside me and fled out of the house.'",
      "M": "'But as soon as I screamed for help, he left his cloak beside me and ran out of the house.'",
      "T": "'When I screamed, he ran off and left his cloak right there.'"
    },
    "19": {
      "L": "As soon as his master heard the words that his wife spoke to him, saying, 'This is what your servant did to me,' his anger was kindled.",
      "M": "When his master heard the story his wife told him, saying, 'This is how your slave treated me,' he burned with anger.",
      "T": "When Potiphar heard his wife's account—'This is what your slave did to me'—his anger blazed."
    },
    "20": {
      "L": "And Joseph's master took him and put him into the prison, the place where the king's prisoners were confined, and he was there in prison.",
      "M": "Joseph's master took him and put him in prison, the place where the king's prisoners were confined. But while Joseph was there in the prison,",
      "T": "Potiphar had Joseph arrested and thrown into the prison where the king's prisoners were held. And there Joseph remained in prison."
    },
    "21": {
      "L": "But the LORD was with Joseph and showed him steadfast love and gave him favor in the sight of the keeper of the prison.",
      "M": "But the LORD was with him; he showed him unfailing love and granted him favor in the eyes of the prison warden.",
      "T": "But the LORD was with Joseph. He showed Joseph his faithful covenant loyalty and gave him favor in the eyes of the prison warden."
    },
    "22": {
      "L": "And the keeper of the prison put Joseph in charge of all the prisoners who were in the prison. Whatever was done there, he was the one doing it.",
      "M": "So the warden put Joseph in charge of all those held in the prison, and he was made responsible for all that was done there.",
      "T": "The warden put Joseph in charge of all the other prisoners and made him responsible for everything that happened in the prison."
    },
    "23": {
      "L": "The keeper of the prison paid no attention to anything that was in Joseph's charge, because the LORD was with him. And whatever he did, the LORD made it succeed.",
      "M": "The warden paid no attention to anything under Joseph's care, because the LORD was with Joseph and gave him success in whatever he did.",
      "T": "The warden stopped paying close attention to anything under Joseph's care, because the LORD was with Joseph and made everything he did succeed."
    }
  },
  "40": {
    "1": {
      "L": "Some time after this, the cupbearer of the king of Egypt and his baker committed an offense against their lord the king of Egypt.",
      "M": "Some time later, the cupbearer and the baker of the king of Egypt offended their master, the king of Egypt.",
      "T": "Sometime later, the king of Egypt's cupbearer and his baker both offended their master the king."
    },
    "2": {
      "L": "And Pharaoh was angry with his two officers, the chief cupbearer and the chief baker,",
      "M": "Pharaoh was angry with his two officials, the chief cupbearer and the chief baker,",
      "T": "Pharaoh was furious with his two officers—the chief cupbearer and the chief baker—"
    },
    "3": {
      "L": "and he put them in custody in the house of the captain of the guard, in the prison where Joseph was confined.",
      "M": "and put them in custody in the house of the captain of the guard, in the same prison where Joseph was confined.",
      "T": "and had them imprisoned in the house of the captain of the guard—the same prison where Joseph was held."
    },
    "4": {
      "L": "The captain of the guard appointed Joseph to be with them, and he attended them. They continued for some time in custody.",
      "M": "The captain of the guard assigned them to Joseph, and he attended them. After they had been in custody for some time,",
      "T": "The captain of the guard put Joseph in charge of them, and he served them. They remained in prison for some time."
    },
    "5": {
      "L": "And one night they both dreamed—the cupbearer and the baker of the king of Egypt, who were confined in the prison—each his own dream, and each dream with its own interpretation.",
      "M": "each of the two men—the cupbearer and the baker of the king of Egypt, who were being held in prison—had a dream the same night, and each dream had a meaning of its own.",
      "T": "One night both of them—the cupbearer and the baker of the king of Egypt, both held in the prison—had dreams. Each dream had its own distinct meaning."
    },
    "6": {
      "L": "When Joseph came to them in the morning, he saw that they were troubled.",
      "M": "When Joseph came to them the next morning, he saw that they were dejected.",
      "T": "When Joseph came to them the next morning, he could see they were upset."
    },
    "7": {
      "L": "So he asked Pharaoh's officers who were with him in custody in his master's house, 'Why are your faces downcast today?'",
      "M": "So he asked Pharaoh's officials who were in custody with him in his master's house, 'Why do you look so sad today?'",
      "T": "He asked Pharaoh's officials, 'Why do you both look so troubled today?'"
    },
    "8": {
      "L": "They said to him, 'We have had dreams, and there is no one to interpret them.' And Joseph said to them, 'Do not interpretations belong to God? Please tell them to me.'",
      "M": "'We both had dreams,' they answered, 'but there is no one to interpret them.' Then Joseph said to them, 'Do not interpretations belong to God? Tell me your dreams.'",
      "T": "'We both had dreams,' they said, 'but there is no one here to interpret them.' Joseph said, 'Interpretations belong to God. Tell me your dreams.'"
    },
    "9": {
      "L": "So the chief cupbearer told his dream to Joseph and said to him, 'In my dream there was a vine before me,'",
      "M": "So the chief cupbearer told Joseph his dream. He said to him, 'In my dream I saw a vine in front of me,'",
      "T": "The chief cupbearer told Joseph his dream: 'In my dream I saw a vine in front of me.'"
    },
    "10": {
      "L": "'and on the vine there were three branches. As soon as it budded, its blossoms shot forth, and the clusters ripened into grapes.'",
      "M": "'and on the vine were three branches. As soon as it budded, it blossomed, and its clusters ripened into grapes.'",
      "T": "'The vine had three branches. As soon as it budded, it blossomed, and its clusters ripened into grapes.'"
    },
    "11": {
      "L": "'Pharaoh's cup was in my hand, and I took the grapes and pressed them into Pharaoh's cup and placed the cup in Pharaoh's hand.'",
      "M": "'Pharaoh's cup was in my hand, and I took the grapes, squeezed them into Pharaoh's cup and put the cup in his hand.'",
      "T": "'I was holding Pharaoh's cup. I took the grapes, squeezed them into Pharaoh's cup, and placed it in his hand.'"
    },
    "12": {
      "L": "Then Joseph said to him, 'This is its interpretation: the three branches are three days.'",
      "M": "'This is what it means,' Joseph said to him. 'The three branches are three days.'",
      "T": "Joseph said to him, 'Here is its meaning: the three branches are three days.'"
    },
    "13": {
      "L": "'In three days Pharaoh will lift up your head and restore you to your office, and you shall place Pharaoh's cup in his hand as formerly, when you were his cupbearer.'",
      "M": "'Within three days Pharaoh will lift up your head and restore you to your position, and you will put Pharaoh's cup in his hand, just as you used to do when you were his cupbearer.'",
      "T": "'Within three days Pharaoh will release you and restore you to your position. You will place Pharaoh's cup in his hand, just as you used to do.'"
    },
    "14": {
      "L": "'Only remember me, when it is well with you, and please do me the kindness to mention me to Pharaoh, and so get me out of this house.'",
      "M": "'But when all goes well with you, remember me and show me kindness; mention me to Pharaoh and get me out of this prison.'",
      "T": "'When things go well for you, please remember me. Do me this favor—mention me to Pharaoh and help get me out of this place.'"
    },
    "15": {
      "L": "'For I was indeed stolen out of the land of the Hebrews, and here also I have done nothing that they should put me into the pit.'",
      "M": "'I was forcibly carried off from the land of the Hebrews, and even here I have done nothing to deserve being put in a dungeon.'",
      "T": "'I was kidnapped from the land of the Hebrews, and here I have done nothing to deserve being thrown into prison.'"
    },
    "16": {
      "L": "When the chief baker saw that the interpretation was favorable, he said to Joseph, 'I also had a dream: there were three cake baskets on my head,'",
      "M": "When the chief baker saw that Joseph had given a favorable interpretation, he said to Joseph, 'I too had a dream: On my head were three baskets of bread.'",
      "T": "When the chief baker saw that the interpretation had been favorable, he said to Joseph, 'I also had a dream. On my head were three baskets of bread.'"
    },
    "17": {
      "L": "'and in the uppermost basket there were all sorts of baked food for Pharaoh, but the birds were eating it out of the basket on my head.'",
      "M": "'In the top basket were all kinds of baked goods for Pharaoh, but the birds were eating them out of the basket on my head.'",
      "T": "'The top basket was full of baked goods for Pharaoh, but the birds kept eating them right out of the basket on my head.'"
    },
    "18": {
      "L": "And Joseph answered and said, 'This is its interpretation: the three baskets are three days.'",
      "M": "'This is what it means,' Joseph said. 'The three baskets are three days.'",
      "T": "Joseph said, 'Here is its meaning: the three baskets are three days.'"
    },
    "19": {
      "L": "'In three days Pharaoh will lift up your head—from you!—and hang you on a tree. And the birds will eat the flesh from you.'",
      "M": "'Within three days Pharaoh will lift off your head and impale your body on a pole. And the birds will eat away your flesh.'",
      "T": "'Within three days Pharaoh will lift off your head—he will execute you and hang your body on a pole, and the birds will eat your flesh.'"
    },
    "20": {
      "L": "On the third day, which was Pharaoh's birthday, he made a feast for all his servants and lifted up the head of the chief cupbearer and the head of the chief baker among his servants.",
      "M": "Now the third day was Pharaoh's birthday, and he gave a feast for all his officials. He lifted up the heads of the chief cupbearer and the chief baker in the presence of his officials:",
      "T": "The third day was Pharaoh's birthday, and he held a feast for all his servants. He made an announcement about the chief cupbearer and the chief baker in front of everyone."
    },
    "21": {
      "L": "He restored the chief cupbearer to his position, and he placed the cup in Pharaoh's hand.",
      "M": "He restored the chief cupbearer to his position, so that he once again put the cup into Pharaoh's hand—",
      "T": "He restored the chief cupbearer to his former position, and the cupbearer placed the cup in Pharaoh's hand once more."
    },
    "22": {
      "L": "But he hanged the chief baker, as Joseph had interpreted to them.",
      "M": "but he impaled the chief baker, just as Joseph had said would happen.",
      "T": "But he had the chief baker executed, exactly as Joseph had interpreted."
    },
    "23": {
      "L": "Yet the chief cupbearer did not remember Joseph, but forgot him.",
      "M": "The chief cupbearer, however, did not remember Joseph; he forgot him.",
      "T": "The chief cupbearer, however, forgot all about Joseph."
    }
  },
  "41": {
    "1": {
      "L": "After two whole years, Pharaoh dreamed that he was standing by the Nile,",
      "M": "When two full years had passed, Pharaoh had a dream: He was standing by the Nile,",
      "T": "Two full years passed. Then Pharaoh had a dream. He was standing by the Nile River"
    },
    "2": {
      "L": "and behold, there came up out of the Nile seven cows, attractive and plump, and they fed in the reed grass.",
      "M": "when out of the river there came up seven cows, sleek and fat, and they grazed among the reeds.",
      "T": "when seven sleek, fat cows came up out of the river and grazed among the reeds."
    },
    "3": {
      "L": "And behold, seven other cows, ugly and thin, came up out of the Nile after them, and stood by the other cows on the bank of the Nile.",
      "M": "After them, seven other cows, ugly and gaunt, came up out of the Nile and stood beside those on the riverbank.",
      "T": "Then seven other cows came up after them—ugly and gaunt—and they stood beside the fat cows on the riverbank."
    },
    "4": {
      "L": "And the ugly, thin cows ate up the seven attractive, plump cows. And Pharaoh awoke.",
      "M": "And the cows that were ugly and gaunt ate up the seven sleek, fat cows. Then Pharaoh woke up.",
      "T": "The ugly, gaunt cows devoured the seven sleek, fat cows. Then Pharaoh woke up."
    },
    "5": {
      "L": "And he fell asleep and dreamed a second time. And behold, seven ears of grain, plump and good, were growing on one stalk.",
      "M": "He fell asleep again and had a second dream: Seven heads of grain, healthy and good, were growing on a single stalk.",
      "T": "He fell asleep again and had a second dream: Seven heads of grain—healthy and full—grew on a single stalk."
    },
    "6": {
      "L": "And behold, after them sprouted seven ears, thin and blighted by the east wind.",
      "M": "After them, seven other heads of grain sprouted—thin and scorched by the east wind.",
      "T": "Then seven other heads of grain sprouted—thin and scorched by the east wind."
    },
    "7": {
      "L": "And the thin ears swallowed up the seven plump, full ears. And Pharaoh awoke, and behold, it was a dream.",
      "M": "The thin heads of grain swallowed up the seven healthy, full heads. Then Pharaoh woke up; it had been a dream.",
      "T": "The thin heads of grain swallowed up the seven full, healthy heads. Pharaoh woke up and realized it had been a dream."
    },
    "8": {
      "L": "So in the morning his spirit was troubled, and he sent and called for all the magicians of Egypt and all its wise men. Pharaoh told them his dreams, but there was none who could interpret them to Pharaoh.",
      "M": "In the morning his mind was troubled, so he sent for all the magicians and wise men of Egypt. Pharaoh told them his dreams, but no one could interpret them for him.",
      "T": "In the morning Pharaoh was deeply troubled. He summoned all the magicians and wise men of Egypt and told them his dreams, but no one could interpret them."
    },
    "9": {
      "L": "Then the chief cupbearer said to Pharaoh, 'I remember my offenses today.'",
      "M": "Then the chief cupbearer said to Pharaoh, 'Today I am reminded of my shortcomings.'",
      "T": "Then the chief cupbearer spoke up: 'I must confess my failure today.'"
    },
    "10": {
      "L": "'Pharaoh was angry with his servants and put me and the chief baker in custody in the house of the captain of the guard.'",
      "M": "'Pharaoh was once angry with his servants, and he imprisoned me and the chief baker in the house of the captain of the guard.'",
      "T": "'Pharaoh was once angry with his servants and had me and the chief baker imprisoned in the captain of the guard's house.'"
    },
    "11": {
      "L": "'And we dreamed on the same night, he and I, each having a dream with its own interpretation.'",
      "M": "'Each of us had a dream the same night, and each dream had a meaning of its own.'",
      "T": "'One night we each had a dream, and each dream had its own meaning.'"
    },
    "12": {
      "L": "'A young Hebrew was there with us, a servant of the captain of the guard. When we told him, he interpreted our dreams to us, giving an interpretation to each man according to his dream.'",
      "M": "'Now a young Hebrew was there with us, a servant of the captain of the guard. We told him our dreams, and he interpreted them for us, giving each man the interpretation of his dream.'",
      "T": "'There was a young Hebrew man there with us—a servant of the captain of the guard. We told him our dreams, and he interpreted each one correctly.'"
    },
    "13": {
      "L": "'And as he interpreted to us, so it came about. I was restored to my office, and the baker was hanged.'",
      "M": "'And things turned out exactly as he interpreted them to us: I was restored to my position, and the other man was impaled.'",
      "T": "'And it happened exactly as he said—I was restored to my position, and the baker was executed.'"
    },
    "14": {
      "L": "Then Pharaoh sent and called Joseph, and they quickly brought him out of the pit. And when he had shaved himself and changed his clothes, he came in before Pharaoh.",
      "M": "So Pharaoh sent for Joseph, and he was quickly brought from the dungeon. When he had shaved and changed his clothes, he came before Pharaoh.",
      "T": "Pharaoh sent for Joseph at once. They hurried him out of the dungeon. He shaved, put on fresh clothes, and appeared before Pharaoh."
    },
    "15": {
      "L": "And Pharaoh said to Joseph, 'I have had a dream, and there is no one who can interpret it. I have heard it said of you that when you hear a dream you can interpret it.'",
      "M": "Pharaoh said to Joseph, 'I had a dream, and no one can interpret it. But I have heard it said of you that when you hear a dream you can interpret it.'",
      "T": "Pharaoh said to him, 'I had a dream, and no one can interpret it. But I have heard that when you hear a dream, you can interpret it.'"
    },
    "16": {
      "L": "Joseph answered Pharaoh, 'It is not in me; God will give Pharaoh a favorable answer.'",
      "M": "'I cannot do it,' Joseph replied to Pharaoh, 'but God will give Pharaoh the answer he desires.'",
      "T": "Joseph replied, 'I cannot do it myself—but God will give Pharaoh the answer that he needs.'"
    },
    "17": {
      "L": "Then Pharaoh said to Joseph, 'Behold, in my dream I was standing on the banks of the Nile.'",
      "M": "Then Pharaoh said to Joseph, 'In my dream I was standing on the bank of the Nile,'",
      "T": "Pharaoh told Joseph his dream: 'In my dream I was standing on the bank of the Nile.'"
    },
    "18": {
      "L": "'And behold, seven cows, plump and attractive, came up out of the Nile and fed in the reed grass.'",
      "M": "'when out of the river there came up seven cows, fat and sleek, and they grazed among the reeds.'",
      "T": "'Seven sleek, fat cows came up out of the river and grazed among the reeds.'"
    },
    "19": {
      "L": "'And behold, seven other cows came up after them, poor and very ugly and thin, such as I had never seen in all the land of Egypt.'",
      "M": "'After them, seven other cows came up—scrawny and very ugly and lean. I had never seen such ugly cows in all the land of Egypt.'",
      "T": "'Then seven other cows came up after them—scrawny, very ugly, and thin. I had never seen such wretched cows in all of Egypt.'"
    },
    "20": {
      "L": "'And the thin, ugly cows ate up the first seven plump cows,'",
      "M": "'The lean and ugly cows ate up the seven fat cows that came up first.'",
      "T": "'The gaunt, ugly cows devoured the seven fat cows.'"
    },
    "21": {
      "L": "'but when they had eaten them it could not be known that they had eaten them, for they were still as ugly as at the beginning. Then I awoke.'",
      "M": "'But even after they ate them, no one could tell that they had done so; they looked just as ugly as before. Then I woke up.'",
      "T": "'But even after eating them, you could not tell they had done so—they looked just as gaunt as before. Then I woke up.'"
    },
    "22": {
      "L": "'I also saw in my dream seven ears growing on one stalk, full and good.'",
      "M": "'In my dream I also saw seven heads of grain, full and good, growing on a single stalk.'",
      "T": "'Then I had another dream: seven heads of grain, full and good, were growing on a single stalk.'"
    },
    "23": {
      "L": "'And behold, seven ears, withered, thin, and blighted by the east wind, sprouted after them,'",
      "M": "'After them, seven other heads sprouted—withered and thin and scorched by the east wind.'",
      "T": "'Then seven other heads sprouted after them—withered, thin, and scorched by the east wind.'"
    },
    "24": {
      "L": "'and the thin ears swallowed up the seven good ears. And I told it to the magicians, but there was no one who could explain it to me.'",
      "M": "'The thin heads of grain swallowed up the seven good heads. I told this to the magicians, but none of them could explain it to me.'",
      "T": "'The thin heads swallowed up the seven good heads. I told this to the magicians, but none of them could explain it.'"
    },
    "25": {
      "L": "Then Joseph said to Pharaoh, 'The dreams of Pharaoh are one; God has revealed to Pharaoh what he is about to do.'",
      "M": "Then Joseph said to Pharaoh, 'The dreams of Pharaoh are one and the same. God has revealed to Pharaoh what he is about to do.'",
      "T": "Joseph said to Pharaoh, 'Both dreams mean the same thing. God has shown Pharaoh what he is about to do.'"
    },
    "26": {
      "L": "'The seven good cows are seven years, and the seven good ears are seven years; the dreams are one.'",
      "M": "'The seven good cows are seven years, and the seven good heads of grain are seven years; it is one and the same dream.'",
      "T": "'The seven fat cows and the seven full heads of grain both represent seven years—they are one and the same dream.'"
    },
    "27": {
      "L": "'The seven lean and ugly cows that came up after them are seven years, and the seven empty ears blighted by the east wind are also seven years of famine.'",
      "M": "'The seven lean, ugly cows that came up afterward are seven years, and so are the seven worthless heads of grain scorched by the east wind: They are seven years of famine.'",
      "T": "'The seven gaunt cows that came after them and the seven scorched, empty heads of grain both represent seven years of famine.'"
    },
    "28": {
      "L": "'It is as I told Pharaoh; God has shown to Pharaoh what he is about to do.'",
      "M": "'It is just as I said to Pharaoh: God has shown Pharaoh what he is about to do.'",
      "T": "'This is what I said to Pharaoh: God has revealed what he is about to do.'"
    },
    "29": {
      "L": "'There will come seven years of great plenty throughout all the land of Egypt,'",
      "M": "'Seven years of great abundance are coming throughout the land of Egypt,'",
      "T": "'Seven years of great abundance are coming to the whole land of Egypt.'"
    },
    "30": {
      "L": "'but after them there will arise seven years of famine, and all the plenty will be forgotten in the land of Egypt. The famine will consume the land,'",
      "M": "'but seven years of famine will follow them. Then all the abundance in Egypt will be forgotten, and the famine will ravage the land.'",
      "T": "'After them will come seven years of terrible famine. All the abundance will be forgotten; the famine will devastate the land.'"
    },
    "31": {
      "L": "'and the plenty will be unknown in the land by reason of the famine that will follow, for it will be very severe.'",
      "M": "'The abundance in the land will not be remembered, because the famine that follows it will be so severe.'",
      "T": "'The abundance will be completely forgotten when the famine arrives, because it will be so severe.'"
    },
    "32": {
      "L": "'And the doubling of Pharaoh's dream means that the thing is fixed by God, and God will shortly bring it about.'",
      "M": "'The reason the dream was given to Pharaoh in two forms is that the matter has been firmly decided by God, and God will do it soon.'",
      "T": "'The reason the dream came to Pharaoh twice is that God has firmly decided to do this, and he will make it happen very soon.'"
    },
    "33": {
      "L": "'Now therefore let Pharaoh select a discerning and wise man, and set him over the land of Egypt.'",
      "M": "'And now let Pharaoh look for a discerning and wise man and put him in charge of the land of Egypt.'",
      "T": "'Therefore, Pharaoh should find a wise and discerning man and put him in charge of the land of Egypt.'"
    },
    "34": {
      "L": "'Let Pharaoh proceed to appoint overseers over the land and take one-fifth of the produce of the land of Egypt during the seven plentiful years.'",
      "M": "'Let Pharaoh appoint commissioners over the land to take a fifth of the harvest of Egypt during the seven years of abundance.'",
      "T": "'Let Pharaoh appoint administrators over the land and collect one-fifth of all the harvest during the seven years of abundance.'"
    },
    "35": {
      "L": "'And let them gather all the food of these good years that are coming and store up grain under the authority of Pharaoh for food in the cities, and let them keep it.'",
      "M": "'They should collect all the food of these good years that are coming and store up the grain under the authority of Pharaoh, to be kept in the cities for food.'",
      "T": "'Let them collect all the food produced in those good years and store the grain under Pharaoh's authority, keeping it in the cities.'"
    },
    "36": {
      "L": "'That food shall be a reserve for the land against the seven years of famine that are to occur in the land of Egypt, so that the land may not perish through the famine.'",
      "M": "'This food should be held in reserve for the country, to be used during the seven years of famine that will come upon Egypt, so that the country may not be ruined by the famine.'",
      "T": "'This stored food will be a reserve for the country, to be used during the seven years of famine ahead—so that Egypt will survive and not be destroyed by the famine.'"
    },
    "37": {
      "L": "This proposal pleased Pharaoh and all his servants.",
      "M": "The plan seemed good to Pharaoh and to all his officials.",
      "T": "Pharaoh and all his officials approved of this plan."
    },
    "38": {
      "L": "And Pharaoh said to his servants, 'Can we find a man like this, in whom is the Spirit of God?'",
      "M": "So Pharaoh asked them, 'Can we find anyone like this man, one in whom is the spirit of God?'",
      "T": "Pharaoh said to his officials, 'Can we find anyone else like this man—someone in whom the Spirit of God lives?'"
    },
    "39": {
      "L": "Then Pharaoh said to Joseph, 'Since God has shown you all this, there is none so discerning and wise as you are.'",
      "M": "Then Pharaoh said to Joseph, 'Since God has made all this known to you, there is no one so discerning and wise as you.'",
      "T": "Pharaoh said to Joseph, 'Since God has revealed all this to you, there is no one as discerning and wise as you.'"
    },
    "40": {
      "L": "'You shall be over my house, and all my people shall order themselves as you command. Only as regards the throne will I be greater than you.'",
      "M": "'You shall be in charge of my palace, and all my people are to submit to your orders. Only with respect to the throne will I be greater than you.'",
      "T": "'You will be in charge of my palace. All my people will obey your commands. Only in the matter of the throne will I rank above you.'"
    },
    "41": {
      "L": "And Pharaoh said to Joseph, 'See, I have set you over all the land of Egypt.'",
      "M": "So Pharaoh said to Joseph, 'I hereby put you in charge of the whole land of Egypt.'",
      "T": "Pharaoh declared, 'I hereby place you in charge of the entire land of Egypt.'"
    },
    "42": {
      "L": "Then Pharaoh took his signet ring from his hand and put it on Joseph's hand, and clothed him in garments of fine linen and put a gold chain about his neck.",
      "M": "Then Pharaoh took his signet ring from his finger and put it on Joseph's finger. He dressed him in robes of fine linen and put a gold chain around his neck.",
      "T": "Pharaoh removed his signet ring and placed it on Joseph's finger. He dressed him in robes of fine linen and put a gold chain around his neck."
    },
    "43": {
      "L": "And he made him ride in his second chariot. And they called out before him, 'Bow the knee!' Thus he set him over all the land of Egypt.",
      "M": "He had him ride in a chariot as his second-in-command, and people shouted before him, 'Make way!' Thus he put him in charge of the whole land of Egypt.",
      "T": "He had Joseph ride in the chariot of his second-in-command, and men ran ahead crying, 'Bow the knee!' In this way Pharaoh set Joseph over all of Egypt."
    },
    "44": {
      "L": "Moreover, Pharaoh said to Joseph, 'I am Pharaoh, and without your consent no one shall lift up hand or foot in all the land of Egypt.'",
      "M": "Then Pharaoh said to Joseph, 'I am Pharaoh, but without your word no one will lift hand or foot in all Egypt.'",
      "T": "Pharaoh said to Joseph, 'I am Pharaoh, but without your approval no one in all Egypt will make a move.'"
    },
    "45": {
      "L": "And Pharaoh called Joseph's name Zaphenath-paneah. And he gave him in marriage Asenath, the daughter of Potiphera priest of On. So Joseph went out over the land of Egypt.",
      "M": "Pharaoh gave Joseph the name Zaphenath-Paneah and gave him Asenath daughter of Potiphera, priest of On, to be his wife. And Joseph went throughout the land of Egypt.",
      "T": "Pharaoh gave Joseph the Egyptian name Zaphenath-paneah and gave him Asenath—daughter of Potiphera, priest of On—as his wife. Joseph then traveled throughout the land of Egypt."
    },
    "46": {
      "L": "Joseph was thirty years old when he entered the service of Pharaoh king of Egypt. And Joseph went out from the presence of Pharaoh and went through all the land of Egypt.",
      "M": "Joseph was thirty years old when he entered the service of Pharaoh king of Egypt. And Joseph went out from Pharaoh's presence and traveled throughout Egypt.",
      "T": "Joseph was thirty years old when he entered the service of Pharaoh king of Egypt. He left Pharaoh's presence and traveled throughout the land."
    },
    "47": {
      "L": "During the seven plentiful years the earth produced abundantly,",
      "M": "During the seven years of abundance the land produced plentifully.",
      "T": "During the seven years of abundance the land produced extraordinary harvests."
    },
    "48": {
      "L": "and he gathered up all the food of these seven years, which occurred in the land of Egypt, and put the food in the cities. He put in every city the food from the fields around it.",
      "M": "Joseph collected all the food produced in those seven years of abundance in Egypt and stored it in the cities. In each city he put the food grown in the fields surrounding it.",
      "T": "Joseph gathered all the food produced throughout those seven years and stored it in the cities—keeping in each city the food from the surrounding fields."
    },
    "49": {
      "L": "And Joseph stored up grain in great abundance, like the sand of the sea, until he ceased to measure it, for it could not be measured.",
      "M": "Joseph stored up huge quantities of grain, like the sand of the sea; it was so much that he stopped keeping records because it was beyond measure.",
      "T": "Joseph stockpiled grain in such enormous quantities—like the sand of the sea—that eventually he stopped keeping records; it was simply beyond measure."
    },
    "50": {
      "L": "Before the year of famine came, two sons were born to Joseph. Asenath, the daughter of Potiphera priest of On, bore them to him.",
      "M": "Before the years of famine came, two sons were born to Joseph by Asenath daughter of Potiphera, priest of On.",
      "T": "Before the famine years arrived, two sons were born to Joseph through his wife Asenath, daughter of Potiphera, priest of On."
    },
    "51": {
      "L": "Joseph called the name of the firstborn Manasseh. 'For,' he said, 'God has made me forget all my hardship and all my father's house.'",
      "M": "Joseph named his firstborn Manasseh and said, 'It is because God has made me forget all my trouble and all my father's household.'",
      "T": "Joseph named his firstborn Manasseh—meaning 'God has made me forget'—because God had caused him to forget all his suffering and all his father's household."
    },
    "52": {
      "L": "The name of the second he called Ephraim, 'For God has made me fruitful in the land of my affliction.'",
      "M": "The second son he named Ephraim and said, 'It is because God has made me fruitful in the land of my suffering.'",
      "T": "He named his second son Ephraim—meaning 'God has made me fruitful'—because God had made him fruitful in the very land where he had suffered."
    },
    "53": {
      "L": "The seven years of plenty that occurred in the land of Egypt came to an end,",
      "M": "The seven years of abundance in Egypt came to an end,",
      "T": "The seven years of abundance in Egypt came to an end,"
    },
    "54": {
      "L": "and the seven years of famine began to come, as Joseph had said. There was famine in all lands, but in all the land of Egypt there was bread.",
      "M": "and the seven years of famine began, just as Joseph had said. There was famine in all the other lands, but in the whole land of Egypt there was food.",
      "T": "and the seven years of famine began—just as Joseph had predicted. Famine struck every surrounding land, but throughout Egypt there was food."
    },
    "55": {
      "L": "When all the land of Egypt was famished, the people cried to Pharaoh for bread. Pharaoh said to all the Egyptians, 'Go to Joseph. What he says to you, do.'",
      "M": "When all Egypt began to feel the famine, the people cried to Pharaoh for food. Then Pharaoh told all the Egyptians, 'Go to Joseph and do what he tells you.'",
      "T": "When the famine spread throughout Egypt and the people cried out to Pharaoh for food, Pharaoh said to all the Egyptians, 'Go to Joseph and do whatever he tells you.'"
    },
    "56": {
      "L": "When the famine had spread over all the face of the earth, Joseph opened all the storehouses and sold to the Egyptians, for the famine was severe in the land of Egypt.",
      "M": "When the famine had spread over the whole country, Joseph opened all the storehouses and sold grain to the Egyptians, for the famine was severe throughout Egypt.",
      "T": "As the famine spread over the entire region, Joseph opened the storehouses and sold grain to the Egyptians—for the famine was severe throughout Egypt."
    },
    "57": {
      "L": "Moreover, all the earth came to Egypt to Joseph to buy grain, because the famine was severe over all the earth.",
      "M": "And all the world came to Egypt to buy grain from Joseph, because the famine was severe everywhere.",
      "T": "People from all over the world came to Egypt to buy grain from Joseph, because the famine was severe throughout the earth."
    }
  },
  "42": {
    "1": {
      "L": "When Jacob learned that there was grain for sale in Egypt, he said to his sons, 'Why do you look at one another?'",
      "M": "When Jacob learned that there was grain in Egypt, he said to his sons, 'Why do you just keep looking at each other?'",
      "T": "When Jacob heard there was grain available in Egypt, he said to his sons, 'Why are you all standing around looking at each other?'"
    },
    "2": {
      "L": "And he said, 'Behold, I have heard that there is grain in Egypt. Go down and buy grain for us there, that we may live and not die.'",
      "M": "He continued, 'I have heard that there is grain in Egypt. Go down there and buy some for us, so that we may live and not die.'",
      "T": "'I have heard there is grain in Egypt. Go down and buy some for us, so that we can survive and not starve.'"
    },
    "3": {
      "L": "So ten of Joseph's brothers went down to buy grain in Egypt.",
      "M": "Then ten of Joseph's brothers went down to buy grain from Egypt.",
      "T": "So ten of Joseph's brothers went down to Egypt to buy grain."
    },
    "4": {
      "L": "But Jacob did not send Benjamin, Joseph's brother, with his brothers, for he feared that harm might happen to him.",
      "M": "But Jacob did not send Benjamin, Joseph's brother, with the others, because he was afraid that harm might come to him.",
      "T": "Jacob did not send Benjamin, Joseph's full brother, with the others. He was afraid something bad might happen to him."
    },
    "5": {
      "L": "Thus the sons of Israel came to buy among the others who came, for the famine was in the land of Canaan.",
      "M": "So Israel's sons were among those who went to buy grain, for the famine was in the land of Canaan also.",
      "T": "Israel's sons came as part of the crowds seeking grain, for the famine had struck Canaan as well."
    },
    "6": {
      "L": "Now Joseph was governor over the land. He was the one who sold to all the people of the land. And Joseph's brothers came and bowed themselves before him with their faces to the ground.",
      "M": "Now Joseph was the governor of the land, the person who sold grain to all its people. So when Joseph's brothers arrived, they bowed down to him with their faces to the ground.",
      "T": "Now Joseph was the governor of the land—the one who sold grain to everyone who came. When his brothers arrived, they bowed down before him with their faces to the ground."
    },
    "7": {
      "L": "Joseph saw his brothers and recognized them, but he made himself strange to them and spoke roughly to them. 'Where do you come from?' he said. They said, 'From the land of Canaan, to buy food.'",
      "M": "As soon as Joseph saw his brothers, he recognized them, but he pretended to be a stranger and spoke harshly to them. 'Where do you come from?' he asked. 'From the land of Canaan,' they replied, 'to buy food.'",
      "T": "Joseph recognized his brothers the moment he saw them. But he pretended to be a stranger and spoke harshly to them. 'Where do you come from?' he demanded. 'From the land of Canaan, to buy food,' they answered."
    },
    "8": {
      "L": "And Joseph recognized his brothers, but they did not recognize him.",
      "M": "Although Joseph recognized his brothers, they did not recognize him.",
      "T": "Joseph recognized them, but they had no idea who he was."
    },
    "9": {
      "L": "And Joseph remembered the dreams that he had dreamed of them. And he said to them, 'You are spies; you have come to see the nakedness of the land.'",
      "M": "Then he remembered his dreams about them and said to them, 'You are spies! You have come to see where our land is undefended.'",
      "T": "Joseph remembered the dreams he had dreamed about them. He said, 'You are spies! You have come to find the weaknesses of our land.'"
    },
    "10": {
      "L": "They said to him, 'No, my lord, your servants have come to buy food.'",
      "M": "'No, my lord,' they answered. 'Your servants have come to buy food.'",
      "T": "'No, my lord!' they protested. 'Your servants have come only to buy food.'"
    },
    "11": {
      "L": "'We are all sons of one man. We are honest men. Your servants have never been spies.'",
      "M": "'We are all the sons of one man. Your servants are honest men, not spies.'",
      "T": "'We are all sons of one man. We are honest—we are not spies.'"
    },
    "12": {
      "L": "He said to them, 'No, it is the nakedness of the land that you have come to see.'",
      "M": "'No!' he said to them. 'You have come to see where our land is undefended.'",
      "T": "But he insisted, 'No—you have come to find our vulnerabilities.'"
    },
    "13": {
      "L": "And they said, 'We, your servants, are twelve brothers, the sons of one man in the land of Canaan, and behold, the youngest is this day with our father, and one is no more.'",
      "M": "And they said, 'Your servants were twelve brothers, the sons of one man, who lives in the land of Canaan. The youngest is now with our father, and one is no more.'",
      "T": "They replied, 'We are twelve brothers, sons of one man in the land of Canaan. The youngest is still with our father, and one of our brothers is gone.'"
    },
    "14": {
      "L": "But Joseph said to them, 'It is as I said to you. You are spies.'",
      "M": "Joseph said to them, 'It is just as I told you: You are spies!'",
      "T": "Joseph said, 'It is just as I said—you are spies.'"
    },
    "15": {
      "L": "'By this you shall be tested: by the life of Pharaoh, you shall not go from this place unless your youngest brother comes here.'",
      "M": "'And this is how you will be tested: As surely as Pharaoh lives, you will not leave this place unless your youngest brother comes here.'",
      "T": "'Here is how I will test you: As Pharaoh lives, you will not leave this place unless your youngest brother comes here.'"
    },
    "16": {
      "L": "'Send one of you, and let him bring your brother, while you remain confined, that your words may be tested, whether there is truth in you. Or else, by the life of Pharaoh, surely you are spies.'",
      "M": "'Send one of your number to get your brother; the rest of you will be kept in prison, so that your words can be tested to see if you are telling the truth. If you are not, then as surely as Pharaoh lives, you are spies!'",
      "T": "'Send one of you to bring your brother while the rest of you stay in prison. Your story will be put to the test. If you are lying, then—as Pharaoh lives—you are spies!'"
    },
    "17": {
      "L": "And he put them all together in custody for three days.",
      "M": "And he put them all in custody for three days.",
      "T": "He had all of them locked up for three days."
    },
    "18": {
      "L": "On the third day Joseph said to them, 'Do this and you will live, for I fear God:'",
      "M": "On the third day, Joseph said to them, 'Do this and you will live, for I fear God:'",
      "T": "On the third day Joseph said to them, 'Do what I say and you will live—I am a man who fears God.'"
    },
    "19": {
      "L": "'If you are honest men, let one of your brothers remain confined where you are in custody, and let the rest go and carry grain for the famine of your households,'",
      "M": "'If you are honest men, let one of your brothers stay here in prison, while the rest of you go and take grain back for your starving households.'",
      "T": "'If you are telling the truth, let one of your brothers stay here in prison while the rest of you go home and bring grain to your starving families.'"
    },
    "20": {
      "L": "'and bring your youngest brother to me. So your words will be verified, and you shall not die.' And they did so.",
      "M": "'But you must bring your youngest brother to me, so that your words may be verified and that you may not die.' This they proceeded to do.",
      "T": "'But you must bring your youngest brother back to me. That will prove your story, and you won't die.' They agreed to do this."
    },
    "21": {
      "L": "Then they said to one another, 'In truth we are guilty concerning our brother, in that we saw the distress of his soul, when he begged us and we did not listen. That is why this distress has come upon us.'",
      "M": "They said to one another, 'Surely we are being punished because of our brother. We saw how distressed he was when he pleaded with us for his life, but we would not listen; that's why this distress has come on us.'",
      "T": "They said to each other, 'We are being punished for what we did to our brother. We saw his anguish when he begged us—and we refused to listen. That is why this suffering has come on us.'"
    },
    "22": {
      "L": "And Reuben answered them, 'Did I not tell you not to sin against the boy? But you did not listen. So now there comes a reckoning for his blood.'",
      "M": "Reuben replied, 'Didn't I tell you not to sin against the boy? But you wouldn't listen! Now we must give an accounting for his blood.'",
      "T": "Reuben replied, 'Didn't I tell you not to harm the boy? But you refused to listen! Now we are paying the price for his blood.'"
    },
    "23": {
      "L": "They did not know that Joseph understood them, for there was an interpreter between them.",
      "M": "They did not realize that Joseph could understand them, since he was using an interpreter.",
      "T": "They did not know that Joseph could understand them, since he had been speaking through an interpreter."
    },
    "24": {
      "L": "Then he turned away from them and wept. And he returned to them and spoke to them. And he took Simeon from them and bound him before their eyes.",
      "M": "He turned away from them and began to weep, but then came back and spoke to them again. He had Simeon taken from them and bound before their eyes.",
      "T": "Joseph turned away from them and wept. Then he turned back, spoke to them again, and had Simeon taken and bound before their eyes."
    },
    "25": {
      "L": "And Joseph gave orders to fill their bags with grain, and to replace every man's money in his sack, and to give them provisions for the journey. This was done for them.",
      "M": "Joseph gave orders to fill their bags with grain, to put each man's silver back in his sack, and to give them provisions for their journey. After this was done for them,",
      "T": "Joseph ordered that their sacks be filled with grain and that each man's money be put back in his sack, and that they be given provisions for the journey. These instructions were carried out."
    },
    "26": {
      "L": "Then they loaded their donkeys with their grain and departed.",
      "M": "they loaded their grain on their donkeys and left.",
      "T": "They loaded their grain onto their donkeys and set out."
    },
    "27": {
      "L": "And as one of them opened his sack to give his donkey fodder at the lodging place, he saw his money in the mouth of his sack.",
      "M": "At the place where they stopped for the night one of them opened his sack to get feed for his donkey, and he saw his silver in the mouth of his sack.",
      "T": "At the place where they stopped for the night, one of them opened his sack to feed his donkey and saw his money right there at the top of the sack."
    },
    "28": {
      "L": "He said to his brothers, 'My money has been put back; here it is in my sack!' At this their hearts failed them, and they turned trembling to one another, saying, 'What is this that God has done to us?'",
      "M": "'My silver has been returned,' he said to his brothers. 'Here it is in my sack.' Their hearts sank and they turned to each other trembling and said, 'What is this that God has done to us?'",
      "T": "'My money has been returned!' he called to his brothers. 'Here it is in my sack!' Their hearts sank. They looked at each other, trembling. 'What is this that God has done to us?'"
    },
    "29": {
      "L": "When they came to Jacob their father in the land of Canaan, they told him all that had happened to them, saying,",
      "M": "When they came to their father Jacob in the land of Canaan, they told him all that had happened to them.",
      "T": "When they arrived back in Canaan, they told their father Jacob everything that had happened."
    },
    "30": {
      "L": "'The man, the lord of the land, spoke roughly to us and took us to be spies of the land.'",
      "M": "'The man who is lord over the land spoke harshly to us and treated us as though we were spying on the land.'",
      "T": "'The man who governs that land spoke harshly to us and accused us of spying.'"
    },
    "31": {
      "L": "'But we said to him, \"We are honest men; we have never been spies.'\"",
      "M": "'But we said to him, \"We are honest men; we are not spies.\"'",
      "T": "'We told him, \"We are honest men—we are not spies.\"'"
    },
    "32": {
      "L": "'\"We are twelve brothers, sons of our father. One is no more, and the youngest is this day with our father in the land of Canaan.\"'",
      "M": "'\"We were twelve brothers, sons of one father. One is no more, and the youngest is now with our father in Canaan.\"'",
      "T": "'\"We are twelve brothers, sons of one father. One is dead, and the youngest is still with our father in Canaan.\"'"
    },
    "33": {
      "L": "'Then the man, the lord of the land, said to us, \"By this I shall know that you are honest men: leave one of your brothers with me, and take grain for the famine of your households, and go.'\"",
      "M": "'Then the man who is lord over the land said to us, \"This is how I will know whether you are honest men: Leave one of your brothers here with me, and take food for your starving households and go.\"'",
      "T": "'Then the man said, \"Here is how I will know if you are telling the truth: leave one of your brothers here with me. Take grain for your hungry families and go.\"'"
    },
    "34": {
      "L": "'\"And bring your youngest brother to me. Then I shall know that you are not spies but honest men, and I will deliver your brother to you, and you shall trade in the land.\"'",
      "M": "'\"But bring your youngest brother to me so I will know that you are not spies but honest men. Then I will give your brother back to you, and you can trade in the land.\"'",
      "T": "'\"But bring your youngest brother to me—then I will know you are not spies, and I will return your other brother to you, and you can move freely in this land.\"'"
    },
    "35": {
      "L": "As they emptied their sacks, behold, every man's bundle of money was in his sack. And when they and their father saw their bundles of money, they were afraid.",
      "M": "As they were emptying their sacks, there in each man's sack was his pouch of silver! When they and their father saw the money pouches, they were frightened.",
      "T": "As they emptied their sacks, each man found his pouch of money at the top. When they and their father saw the money, they were all frightened."
    },
    "36": {
      "L": "And Jacob their father said to them, 'You have bereaved me of my children: Joseph is no more, and Simeon is no more, and now you would take Benjamin. All this has come against me.'",
      "M": "Their father Jacob said to them, 'You have deprived me of my children. Joseph is no more and Simeon is no more, and now you want to take Benjamin. Everything is against me!'",
      "T": "Their father Jacob said to them, 'You are robbing me of my children! Joseph is gone, Simeon is gone, and now you want to take Benjamin too. Everything is against me!'"
    },
    "37": {
      "L": "Then Reuben said to his father, 'Kill my two sons if I do not bring him back to you. Put him in my hands, and I will bring him back to you.'",
      "M": "Then Reuben said to his father, 'You may put both of my sons to death if I do not bring him back to you. Entrust him to my care, and I will bring him back.'",
      "T": "Reuben said to his father, 'You can put my two sons to death if I fail to bring Benjamin back. Trust him to my care, and I will return him safely.'"
    },
    "38": {
      "L": "But he said, 'My son shall not go down with you, for his brother is dead, and he is the only one left. If harm should happen to him on the journey that you are to make, you would bring down my gray hairs with sorrow to Sheol.'",
      "M": "But Jacob said, 'My son will not go down there with you; his brother is dead and he is the only one left. If harm comes to him on the journey you are taking, you will bring my gray head down to the grave in sorrow.'",
      "T": "But Jacob said, 'My son will not go down with you. His brother is dead, and he is the only one I have left from Rachel. If anything happened to him on the way, you would send this old man to his grave in grief.'"
    }
  },
  "43": {
    "1": {
      "L": "Now the famine was severe in the land.",
      "M": "Now the famine was still severe in the land.",
      "T": "The famine remained severe throughout the land."
    },
    "2": {
      "L": "And when they had eaten the grain that they had brought from Egypt, their father said to them, 'Go again, buy us a little food.'",
      "M": "And when they had eaten all the grain they had brought from Egypt, their father said to them, 'Go back and buy us a little more food.'",
      "T": "When they had eaten all the grain they had brought from Egypt, their father said to them, 'Go back and buy us some more food.'"
    },
    "3": {
      "L": "But Judah said to him, 'The man solemnly warned us, saying, \"You shall not see my face unless your brother is with you.\"'",
      "M": "But Judah said to him, 'The man warned us solemnly, \"You will not see my face again unless your brother is with you.\"'",
      "T": "But Judah said to him, 'The man gave us a strict warning: \"You will not see my face again unless your brother is with you.\"'"
    },
    "4": {
      "L": "'If you will send our brother with us, we will go down and buy you food.'",
      "M": "'If you will send our brother along with us, we will go down and buy food for you.'",
      "T": "'If you are willing to send our brother with us, we will go down and buy food for you.'"
    },
    "5": {
      "L": "'But if you will not send him, we will not go down, for the man said to us, \"You shall not see my face unless your brother is with you.\"'",
      "M": "'But if you will not send him, we will not go down, because the man said to us, \"You will not see my face unless your brother is with you.\"'",
      "T": "'But if you won't send him, we won't go—because the man told us clearly, \"You will not see my face unless your brother is with you.\"'"
    },
    "6": {
      "L": "Israel said, 'Why did you treat me so badly as to tell the man that you had another brother?'",
      "M": "Israel asked, 'Why did you bring this trouble on me by telling the man you had another brother?'",
      "T": "Israel said, 'Why did you cause me this trouble by telling the man you had another brother?'"
    },
    "7": {
      "L": "They replied, 'The man questioned us carefully about ourselves and our kindred, saying, \"Is your father still alive? Do you have another brother?\" What we told him was in answer to these questions. Could we in any way know that he would say, \"Bring your brother down\"?'",
      "M": "They replied, 'The man questioned us closely about ourselves and our family. \"Is your father still living?\" he asked us. \"Do you have another brother?\" We simply answered his questions. How were we to know he would say, \"Bring your brother down here\"?'",
      "T": "They said, 'He questioned us closely about ourselves and our family—\"Is your father still alive? Do you have another brother?\" We simply answered what he asked. How could we have known he would say, \"Bring your brother here\"?'"
    },
    "8": {
      "L": "And Judah said to Israel his father, 'Send the boy with me, and we will arise and go, that we may live and not die, both we and you and also our little ones.'",
      "M": "Then Judah said to Israel his father, 'Send the boy along with me and we will go at once, so that we and you and our children may live and not die.'",
      "T": "Judah said to his father Israel, 'Send the boy with me. Let us get moving so that we—you, us, and our children—can survive and not die.'"
    },
    "9": {
      "L": "'I will be a pledge of his safety. From my hand you shall require him. If I do not bring him back to you and set him before you, then let me bear the blame forever.'",
      "M": "'I myself will guarantee his safety; you can hold me personally responsible for him. If I do not bring him back to you and set him here before you, I will bear the blame before you all my life.'",
      "T": "'I will personally guarantee his safety. If I fail to bring him back and set him before you, I will bear the blame my entire life.'"
    },
    "10": {
      "L": "'For if we had not delayed, we would now have returned twice.'",
      "M": "'As it is, if we had not delayed, we could have gone and returned twice.'",
      "T": "'If we had not wasted all this time, we could have made the trip twice over by now.'"
    },
    "11": {
      "L": "Then their father Israel said to them, 'If it must be so, then do this: take some of the choice fruits of the land in your bags, and carry a present down to the man—a little balm and a little honey, gum, myrrh, pistachio nuts, and almonds.'",
      "M": "Then their father Israel said to them, 'If it must be, then do this: Put some of the best products of the land in your bags and take them down to the man as a gift—a little balm and a little honey, some spices and myrrh, some pistachio nuts and almonds.'",
      "T": "Their father Israel said to them, 'If that is how it must be, then do this: take some of the finest produce of the land as a gift for the man—some balm, a little honey, spices, myrrh, pistachio nuts, and almonds.'"
    },
    "12": {
      "L": "'Take double the money with you. Carry back with you the money that was returned in the mouth of your sacks. Perhaps it was an oversight.'",
      "M": "'Take double the amount of silver with you, for you must return the silver that was put back into the mouths of your sacks. Perhaps it was a mistake.'",
      "T": "'Also take double the money—bring back the money that was returned in your sacks, in case it was an error.'"
    },
    "13": {
      "L": "'Take also your brother, and arise, go again to the man.'",
      "M": "'Take your brother also and go back to the man at once.'",
      "T": "'Take your brother and go back to the man right away.'"
    },
    "14": {
      "L": "'May God Almighty grant you mercy before the man, and may he send back your other brother and Benjamin. And as for me, if I am bereaved of my children, I am bereaved.'",
      "M": "'And may God Almighty grant you mercy before the man so that he will let your other brother and Benjamin come back with you. As for me, if I am bereaved, I am bereaved.'",
      "T": "'May God Almighty give you favor before the man, so that he releases your other brother and allows Benjamin to come home. As for me—if I lose my children, then I lose them.'"
    },
    "15": {
      "L": "So the men took this present, and they took double the money with them, and Benjamin. They arose and went down to Egypt and stood before Joseph.",
      "M": "So the men took the gifts and double the amount of silver, and Benjamin also. They hurried down to Egypt and presented themselves to Joseph.",
      "T": "The men took the gifts, double the money, and Benjamin, and hurried down to Egypt. They presented themselves before Joseph."
    },
    "16": {
      "L": "When Joseph saw Benjamin with them, he said to the steward of his house, 'Bring the men into the house, and slaughter an animal and make ready, for the men are to dine with me at noon.'",
      "M": "When Joseph saw Benjamin with them, he said to the steward of his house, 'Take these men to my house, slaughter an animal and prepare dinner; they are to eat with me at noon.'",
      "T": "When Joseph saw Benjamin with them, he said to the steward of his house, 'Bring these men inside. Slaughter an animal and prepare a meal—they will dine with me at noon.'"
    },
    "17": {
      "L": "The man did as Joseph told him and brought the men to Joseph's house.",
      "M": "The man did as Joseph told him and took the men to Joseph's house.",
      "T": "The steward did as Joseph said and brought the men to Joseph's house."
    },
    "18": {
      "L": "And the men were afraid because they were brought to Joseph's house, and they said, 'It is because of the money, which was replaced in our sacks the first time, that we are brought in, so that he may assault us and fall upon us to make us servants and seize our donkeys.'",
      "M": "Now the men were frightened when they were taken to his house. They thought, 'We were brought here because of the silver that was put back in our sacks the first time. He wants to attack us and overpower us and seize us as slaves and take our donkeys.'",
      "T": "The men were terrified to be brought into Joseph's house. They thought, 'It's because of the money returned in our sacks last time. He is going to use it as an excuse to seize us as slaves and take our donkeys.'"
    },
    "19": {
      "L": "So they went up to the steward of Joseph's house and spoke with him at the door of the house,",
      "M": "So they went up to Joseph's steward and spoke to him at the entrance to the house.",
      "T": "So they approached the steward at the entrance of the house and spoke to him."
    },
    "20": {
      "L": "and said, 'Oh, my lord, we came down the first time to buy food.'",
      "M": "'We beg your pardon, our lord,' they said, 'we came down here the first time to buy food.'",
      "T": "'Please, sir,' they said, 'we came down before to buy food.'"
    },
    "21": {
      "L": "'And when we came to the lodging place we opened our sacks, and there was each man's money in the mouth of his sack, our money in full weight. So we have brought it back with us.'",
      "M": "'But at the place where we stopped for the night we opened our sacks and each of us found his silver—the exact weight—in the mouth of his sack. So we have brought it back with us.'",
      "T": "'When we stopped for the night and opened our sacks, each man's money was there in full—right at the top of his sack. We have brought it all back with us.'"
    },
    "22": {
      "L": "'And we have brought additional money with us to buy food. We do not know who put our money in our sacks.'",
      "M": "'And we have brought additional silver with us to buy food. We don't know who put our silver in our sacks.'",
      "T": "'And we have brought more money to buy food. We have no idea who put the money in our sacks.'"
    },
    "23": {
      "L": "He said, 'Peace to you, do not be afraid. Your God and the God of your father has put treasure in your sacks for you. I received your money.' Then he brought Simeon out to them.",
      "M": "'It's all right,' he said. 'Don't be afraid. Your God, the God of your father, has given you treasure in your sacks; I received your payment.' Then he brought Simeon out to them.",
      "T": "'It's all right—don't be afraid,' the steward said. 'Your God, the God of your father, must have put treasure in your sacks. I received your full payment.' Then he brought Simeon out to them."
    },
    "24": {
      "L": "And when the man had brought the men into Joseph's house and given them water, and they had washed their feet, and when he had given their donkeys fodder,",
      "M": "The steward took the men into Joseph's house, gave them water to wash their feet and provided fodder for their donkeys.",
      "T": "The steward brought them inside, gave them water to wash their feet, and provided fodder for their donkeys."
    },
    "25": {
      "L": "they prepared the present for Joseph's coming at noon, for they heard that they would eat bread there.",
      "M": "They prepared their gifts for Joseph's arrival at noon, because they had heard that they were to eat there.",
      "T": "They arranged their gifts, ready for when Joseph arrived at noon—for they had been told they would eat a meal there."
    },
    "26": {
      "L": "When Joseph came home, they brought into the house to him the present that they had with them and bowed down to him to the ground.",
      "M": "When Joseph came home, they presented to him the gifts they had brought inside, and they bowed down before him to the ground.",
      "T": "When Joseph came home, they brought their gifts inside and bowed down to him to the ground."
    },
    "27": {
      "L": "And he inquired about their welfare and said, 'Is your father well, the old man of whom you spoke? Is he still alive?'",
      "M": "He asked them how they were, and then he said, 'How is your aged father you told me about? Is he still living?'",
      "T": "He greeted them and then asked, 'How is your father—the old man you mentioned? Is he still alive and well?'"
    },
    "28": {
      "L": "They said, 'Your servant our father is well; he is still alive.' And they bowed their heads and prostrated themselves.",
      "M": "They replied, 'Your servant our father is still alive and well.' And they bowed down, prostrating themselves before him.",
      "T": "'Your servant our father is well—he is still alive,' they answered. And they bowed low in respect."
    },
    "29": {
      "L": "And he lifted up his eyes and saw his brother Benjamin, his mother's son, and said, 'Is this your youngest brother, of whom you spoke to me? God be gracious to you, my son!'",
      "M": "As he looked about and saw his brother Benjamin, his own mother's son, he asked, 'Is this your youngest brother, the one you told me about?' And he said, 'God be gracious to you, my son.'",
      "T": "Joseph looked up and saw his brother Benjamin—his own mother's son. 'Is this your youngest brother, the one you told me about?' he asked. Then he said, 'God be gracious to you, my son.'"
    },
    "30": {
      "L": "Then Joseph hurried out, for his compassion grew warm for his brother, and he sought a place to weep. And he entered his chamber and wept there.",
      "M": "Deeply moved at the sight of his brother, Joseph hurried out and looked for a place to weep. He went into his private room and wept there.",
      "T": "Joseph hurried out of the room—his heart was overwhelmed with love for his brother. He went into his private chamber and wept there."
    },
    "31": {
      "L": "Then he washed his face and came out. And controlling himself he said, 'Serve the food.'",
      "M": "After washing his face, he came out and, controlling himself, said, 'Serve the food.'",
      "T": "After washing his face, he came back out. Composing himself, he ordered, 'Serve the meal.'"
    },
    "32": {
      "L": "They served him by himself, and them by themselves, and the Egyptians who ate with him by themselves, because the Egyptians could not eat with the Hebrews, for that is an abomination to the Egyptians.",
      "M": "They served him by himself, the brothers by themselves, and the Egyptians who ate with him by themselves, because Egyptians could not eat with Hebrews, for that is detestable to Egyptians.",
      "T": "Joseph was served at his own table, the brothers at their own table, and the Egyptians at a separate table—because Egyptians considered it an abomination to eat with Hebrews."
    },
    "33": {
      "L": "The men were seated before him, the firstborn according to his birthright and the youngest according to his youth. And the men looked at one another in amazement.",
      "M": "The men had been seated before him in the order of their ages, from the firstborn to the youngest; and they looked at each other in astonishment.",
      "T": "The brothers were seated before Joseph in order of their ages from oldest to youngest—and they stared at each other in bewilderment."
    },
    "34": {
      "L": "Portions were taken to them from Joseph's table, but Benjamin's portion was five times as much as any of theirs. And they drank and were merry with him.",
      "M": "When portions of food were served to them from Joseph's table, Benjamin's portion was five times as much as anyone else's. So they feasted and drank freely with him.",
      "T": "Portions were brought to them from Joseph's own table, but Benjamin received five times as much as anyone else. And they all drank freely and were merry with him."
    }
  }
}

def main():
    print('Writing Genesis chapters 37–43...')
    for tier_key, tier_folder in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_folder, 'genesis')
        merge_tier(existing, GENESIS, tier_key)
        save(tier_folder, 'genesis', existing)
    print('Done.')

if __name__ == '__main__':
    main()
