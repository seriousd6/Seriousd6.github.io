"""
MKT Genesis chapters 44-50 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-genesis-44-50.py

Covers the climax of the Joseph narrative: the silver cup test, Joseph's self-disclosure,
Jacob's migration to Egypt, Joseph's land policy, Jacob's blessings of Ephraim/Manasseh,
the Blessing of Jacob (Gen 49 — ancient Hebrew poetry), Jacob's death and burial,
and Joseph's death.

Translation decisions:
- H3068 (יהוה): "the LORD" throughout
- H430 (אֱלֹהִים): "God"
- H2617 (חֶסֶד) at 47:29: L="steadfast love", M="unfailing loyalty", T="faithful covenant loyalty"
- H5315 (נֶפֶשׁ) at 44:30: "life" — the embodied self, not an immaterial soul;
  "his life is bound up with the boy's life" preserves the force of the idiom
- H7886 (שִׁילֹה) at 49:10 is the most disputed term in the chapter:
    L: "until Shiloh comes" — preserves the Masoretic consonants as a proper noun
    M: "until the one to whom it belongs comes" — reading שֶׁ-לֹּו (he whose it is),
       supported by LXX and Ezek 21:27 parallel
    T: "until he comes to whom kingship belongs" — makes the messianic resonance explicit
- H7706 (שַׁדַּי) = "the Almighty" / "God Almighty" (El Shaddai)
- H46 (אֲבִיר יַעֲקֹב) at 49:24 = "the Mighty One of Jacob" — a divine title
- H68 (אֶבֶן יִשְׂרָאֵל) at 49:24 = "the Stone of Israel" — a rare divine title
- H2803 (חָשַׁב) at 50:20 appears twice: "you planned evil / God planned it for good" —
  the same verb for human scheming and divine purpose is the theological heart of the Joseph story
- Genesis 49 (the Blessing of Jacob) is ancient Hebrew poetry; semicolons mark
  poetic line breaks in L; T uses vivid English with some rhythmic compression
- Gen 48:22 שְׁכֶם is a wordplay: both "mountain slope" and the city of Shechem
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
  "44": {
    "1": {
      "L": "Then he commanded the steward of his house, saying, 'Fill the men's sacks with food, as much as they can carry, and put each man's money in the mouth of his sack.'",
      "M": "Now Joseph gave these instructions to the steward of his house: 'Fill the men's sacks with as much food as they can carry, and put each man's silver in the mouth of his sack.'",
      "T": "Joseph gave his steward orders: 'Fill the men's sacks with as much food as they can carry, and put each man's money back in the top of his sack.'"
    },
    "2": {
      "L": "'And put my cup, the silver cup, in the mouth of the sack of the youngest, with his grain money.' And he did as Joseph told him.",
      "M": "'Also put my cup—the silver cup—in the mouth of the youngest one's sack, along with the silver for his grain.' And he did as Joseph said.",
      "T": "'And put my silver cup in the opening of the youngest one's sack, along with his grain money.' The steward did exactly as Joseph instructed."
    },
    "3": {
      "L": "As soon as the morning was light, the men were sent away with their donkeys.",
      "M": "At daybreak the men were sent on their way with their donkeys.",
      "T": "At first light, the men were sent off with their donkeys."
    },
    "4": {
      "L": "They had gone out of the city and were not yet far off, when Joseph said to his steward, 'Up, follow after the men, and when you overtake them, say to them, \"Why have you repaid evil for good?\"'",
      "M": "They had not gone far from the city when Joseph said to his steward, 'Go after those men at once, and when you catch up with them, say to them, \"Why have you repaid good with evil?\"'",
      "T": "They had barely left the city when Joseph said to his steward, 'Go after those men! When you catch up to them, say, \"Why have you repaid good with evil?\"'"
    },
    "5": {
      "L": "'Is it not from this that my lord drinks, and by this that he practices divination? You have done evil in doing this.'",
      "M": "'Isn't this the cup my master drinks from and also uses for divination? This is a wicked thing you have done.'",
      "T": "'That is the cup my master drinks from—and uses for divination. What you have done is wicked!'"
    },
    "6": {
      "L": "He overtook them and spoke to them these words.",
      "M": "When he caught up with them, he repeated these words to them.",
      "T": "The steward caught up with them and confronted them with these words."
    },
    "7": {
      "L": "They said to him, 'Why does my lord speak such words as these? Far be it from your servants to do such a thing!'",
      "M": "'Why does my lord say such things?' they replied. 'Far be it from your servants to do anything like that!'",
      "T": "'How can you say this?' they protested. 'Your servants would never do such a thing!'"
    },
    "8": {
      "L": "'Behold, the money that we found in the mouths of our sacks we brought back to you from the land of Canaan. How then could we steal silver or gold from your lord's house?'",
      "M": "'We even brought back to you from the land of Canaan the silver we found in the mouths of our sacks. Why would we steal silver or gold from your master's house?'",
      "T": "'We brought back from Canaan every coin we found in our sacks—why on earth would we steal silver or gold from your master's house?'"
    },
    "9": {
      "L": "'Whichever of your servants is found with it shall die, and we also will be my lord's servants.'",
      "M": "'If any of your servants is found to have it, he will die; and the rest of us will become my lord's slaves.'",
      "T": "'If any one of us is found with it, let him die—and the rest of us will become your master's slaves.'"
    },
    "10": {
      "L": "He said, 'Let it be as you say: he who is found with it shall be my servant, and the rest of you shall be innocent.'",
      "M": "'Very well, then,' he said, 'let it be as you say. Whoever is found to have it will become my slave; the rest of you will be free from blame.'",
      "T": "'Very well,' the steward replied. 'It will be as you say: whoever is found to have it will become my slave—but the rest of you will go free.'"
    },
    "11": {
      "L": "Then each man quickly lowered his sack to the ground, and each man opened his sack.",
      "M": "Each of them quickly lowered his sack to the ground and opened it.",
      "T": "Each man quickly set his sack on the ground and opened it."
    },
    "12": {
      "L": "He searched, beginning with the eldest and ending with the youngest. And the cup was found in Benjamin's sack.",
      "M": "Then the steward proceeded to search, beginning with the oldest and ending with the youngest. And the cup was found in Benjamin's sack.",
      "T": "The steward searched each sack in order, starting with the oldest and working down to the youngest. The cup was found in Benjamin's sack."
    },
    "13": {
      "L": "Then they tore their clothes. And every man loaded his donkey, and they returned to the city.",
      "M": "At this, they tore their clothes. Then they all loaded their donkeys and returned to the city.",
      "T": "At that, they all tore their clothes in anguish. Each man reloaded his donkey, and they turned back to the city."
    },
    "14": {
      "L": "When Judah and his brothers came to Joseph's house, he was still there. They fell before him to the ground.",
      "M": "When Judah and his brothers arrived at Joseph's house, Joseph was still there. They threw themselves to the ground before him.",
      "T": "When Judah and his brothers reached Joseph's house, Joseph was still there. They fell to the ground before him."
    },
    "15": {
      "L": "Joseph said to them, 'What deed is this that you have done? Do you not know that a man like me can indeed practice divination?'",
      "M": "Joseph said to them, 'What is this you have done? Don't you know that a man like me can find things out by divination?'",
      "T": "'What have you done?' Joseph demanded. 'Did you not know that a man like me has ways of finding out the truth?'"
    },
    "16": {
      "L": "And Judah said, 'What shall we say to my lord? What shall we speak? Or how shall we clear ourselves? God has found out the guilt of your servants; behold, we are my lord's servants, both we and he also in whose hand the cup has been found.'",
      "M": "Then Judah replied, 'What can we say to my lord? What can we speak? How can we prove our innocence? God has uncovered your servants' guilt. We are now my lord's slaves—we ourselves and the one who was found to have the cup.'",
      "T": "Judah said, 'What can we say? What argument can we make? How can we prove our innocence? God himself has exposed the guilt of your servants. We are all your slaves—both those who are innocent and the one found with the cup.'"
    },
    "17": {
      "L": "But he said, 'Far be it from me to do so! Only the man in whose hand the cup was found shall be my servant. But as for you, go up in peace to your father.'",
      "M": "But Joseph said, 'Far be it from me to do such a thing! Only the man who was found to have the cup will become my slave. The rest of you, go back to your father in peace.'",
      "T": "But Joseph said, 'I would never do that. Only the man in whose sack the cup was found will be my slave. The rest of you—go back to your father in peace.'"
    },
    "18": {
      "L": "Then Judah went up to him and said, 'Oh, my lord, please let your servant speak a word in my lord's ears, and let not your anger burn against your servant, for you are like Pharaoh himself.'",
      "M": "Then Judah went up to him and said: 'Please, my lord, let your servant speak a word to my lord. Do not be angry with your servant, though you are equal to Pharaoh himself.'",
      "T": "Then Judah stepped forward and said, 'My lord, please let your servant speak a word in your ear. Do not be angry with me—for you have authority equal to Pharaoh himself.'"
    },
    "19": {
      "L": "'My lord asked his servants, saying, \"Have you a father, or a brother?\"'",
      "M": "'My lord asked his servants, \"Do you have a father or a brother?\"'",
      "T": "'My lord asked us, \"Do you have a father or a brother?\"'"
    },
    "20": {
      "L": "'And we said to my lord, \"We have a father, an old man, and a young brother, the child of his old age. His brother is dead, and he alone is left of his mother's children, and his father loves him.\"'",
      "M": "'And we told my lord, \"We have an aged father, and there is a young son born to him in his old age. His full brother is dead, and he is the only one of his mother's sons left, and his father loves him dearly.\"'",
      "T": "'We told you: \"We have an elderly father, and a young brother born to him in his old age. His brother is dead—he alone remains of his mother's children, and his father loves him deeply.\"'"
    },
    "21": {
      "L": "'Then you said to your servants, \"Bring him down to me, that I may set my eyes on him.\"'",
      "M": "'Then you said to your servants, \"Bring him down to me so I can see him myself.\"'",
      "T": "'Then you told your servants, \"Bring him down to me so I can see him with my own eyes.\"'"
    },
    "22": {
      "L": "'We said to my lord, \"The boy cannot leave his father, for if he should leave his father, his father would die.\"'",
      "M": "'And we said to my lord, \"The boy cannot leave his father; if he leaves him, his father will die.\"'",
      "T": "'We told you, \"The boy cannot leave his father. If he were to leave him, his father would die.\"'"
    },
    "23": {
      "L": "'Then you said to your servants, \"Unless your youngest brother comes down with you, you shall not see my face again.\"'",
      "M": "'But you told your servants, \"Unless your youngest brother comes down with you, you will not see my face again.\"'",
      "T": "'But you said to us, \"Unless your youngest brother comes with you, you will never see my face again.\"'"
    },
    "24": {
      "L": "'When we went back to your servant my father, we told him the words of my lord.'",
      "M": "'When we went back to your servant my father, we told him everything my lord had said.'",
      "T": "'When we returned to our father—your servant—we told him everything you had said.'"
    },
    "25": {
      "L": "'And when our father said, \"Go again, buy us a little food,\"'",
      "M": "'Later, when our father said, \"Go back and buy us a little more food,\"'",
      "T": "'When our father told us, \"Go back and buy some more food,\"'"
    },
    "26": {
      "L": "'we said, \"We cannot go down. If our youngest brother goes with us, then we will go down. For we cannot see the man's face unless our youngest brother is with us.\"'",
      "M": "'we told him, \"We cannot go down. Only if our youngest brother is with us will we go. We cannot see the man's face unless our youngest brother is with us.\"'",
      "T": "'we told him, \"We cannot go without our youngest brother. We cannot face that man unless he is with us.\"'"
    },
    "27": {
      "L": "'Then your servant my father said to us, \"You know that my wife bore me two sons.\"'",
      "M": "'Your servant my father said to us, \"You know that my wife bore me two sons.\"'",
      "T": "'Then your servant—our father—said to us, \"You know that my wife bore me two sons.\"'"
    },
    "28": {
      "L": "'One left me, and I said, \"Surely he has been torn to pieces,\" and I have never seen him since.'",
      "M": "'\"One of them went away from me, and I said, \"He has surely been torn to pieces.\" And I have not seen him since.'",
      "T": "'\"One of them left me, and I said, \"He must have been torn to pieces.\" I have never seen him again.'"
    },
    "29": {
      "L": "'If you take this one also from me, and harm happens to him, you will bring down my gray hairs in evil to Sheol.'",
      "M": "'\"If you take this one from me too, and harm comes to him, you will bring my gray head down to the grave in misery.\"'",
      "T": "'\"If you take this one from me as well and something happens to him, you will send this old man to his grave in utter grief.\"'"
    },
    "30": {
      "L": "'Now therefore, as soon as I come to your servant my father, and the boy is not with us, then, as his life is bound up in the boy's life,'",
      "M": "'So now, if the boy is not with me when I go back to your servant my father—and his life is bound up with the boy's life—'",
      "T": "'So now, when I return to my father without the boy—and his very life is wrapped up in the boy's life—'"
    },
    "31": {
      "L": "'as soon as he sees that the boy is not with us, he will die, and your servants will bring down the gray hairs of your servant our father with sorrow to Sheol.'",
      "M": "'when he sees that the boy is not there, he will die. Your servants will have caused the gray head of our father to go down to the grave in grief.'",
      "T": "'the moment he sees the boy is gone, he will die. Your servants will have sent our father—a broken old man—down to his grave.'"
    },
    "32": {
      "L": "'For your servant became a pledge of safety for the boy to my father, saying, \"If I do not bring him back to you, then I shall bear the blame before my father all my life.\"'",
      "M": "'Your servant guaranteed the boy's safety to my father. I said, \"If I do not bring him back to you, I will bear the blame before you, my father, all my life.\"'",
      "T": "'I personally vouched for the boy's safety to my father. I said, \"If I do not bring him back, I will bear the blame before you for the rest of my life.\"'"
    },
    "33": {
      "L": "'Now therefore, please let your servant remain instead of the boy as a servant to my lord, and let the boy go back with his brothers.'",
      "M": "'Now then, please let your servant stay here as my lord's slave in place of the boy, and let the boy return with his brothers.'",
      "T": "'So please—let me remain here as your slave in place of the boy. Let him go home with his brothers.'"
    },
    "34": {
      "L": "'For how can I go back to my father if the boy is not with me? I fear to see the evil that would find my father.'",
      "M": "'How can I go back to my father if the boy is not with me? No—do not let me see the misery that would come upon my father.'",
      "T": "'How could I face my father without the boy? I could not bear to see the grief it would bring him.'"
    }
  },
  "45": {
    "1": {
      "L": "Then Joseph could not control himself before all those who stood by him. He cried, 'Make everyone go out from me.' So no one stayed with him when Joseph made himself known to his brothers.",
      "M": "Then Joseph could no longer control himself before all his attendants, and he cried out, 'Have everyone leave my presence!' So there was no one with Joseph when he made himself known to his brothers.",
      "T": "Joseph could hold himself back no longer. With all his attendants present, he cried out, 'Clear the room!' And everyone withdrew. He was alone with his brothers when he revealed who he was."
    },
    "2": {
      "L": "And he wept aloud, so that the Egyptians heard it, and the household of Pharaoh heard it.",
      "M": "And he wept so loudly that the Egyptians heard him, and Pharaoh's household heard about it.",
      "T": "He wept so loudly that the Egyptians outside heard it, and word spread through Pharaoh's entire palace."
    },
    "3": {
      "L": "And Joseph said to his brothers, 'I am Joseph! Is my father still alive?' But his brothers could not answer him, for they were dismayed at his presence.",
      "M": "Joseph said to his brothers, 'I am Joseph! Is my father still living?' But his brothers were not able to answer him, because they were terrified at his presence.",
      "T": "Joseph said to his brothers, 'I am Joseph. Is my father still alive?' But his brothers could not say a word—they were too shaken at the sight of him."
    },
    "4": {
      "L": "So Joseph said to his brothers, 'Come near to me, please.' And they came near. And he said, 'I am your brother, Joseph, whom you sold into Egypt.'",
      "M": "Then Joseph said to his brothers, 'Come close to me.' When they had done so, he said, 'I am your brother Joseph, the one you sold into Egypt!'",
      "T": "Joseph said, 'Come closer.' They came near. He said, 'I am your brother Joseph—the one you sold into Egypt.'"
    },
    "5": {
      "L": "'And now do not be distressed or angry with yourselves because you sold me here, for God sent me before you to preserve life.'",
      "M": "'And now, do not be distressed and do not be angry with yourselves for selling me here, because it was to save lives that God sent me ahead of you.'",
      "T": "'Do not be grieved or angry with yourselves for what you did. God sent me ahead of you to save lives.'"
    },
    "6": {
      "L": "'For the famine has been in the land these two years, and there are yet five years in which there will be neither plowing nor harvest.'",
      "M": "'For two years now there has been famine in the land, and for the next five years there will be no plowing and reaping.'",
      "T": "'The famine has been in the land for two years now, and five more years are coming with no plowing or harvest.'"
    },
    "7": {
      "L": "'And God sent me before you to preserve for you a remnant on earth, and to keep alive for you many survivors.'",
      "M": "'But God sent me ahead of you to preserve for you a remnant on earth and to save your lives by a great deliverance.'",
      "T": "'God sent me ahead of you to preserve a remnant for you in the land and to keep you alive through a great rescue.'"
    },
    "8": {
      "L": "'So it was not you who sent me here, but God. He has made me a father to Pharaoh, and lord of all his house and ruler over all the land of Egypt.'",
      "M": "'So then, it was not you who sent me here, but God. He made me a father figure to Pharaoh, lord of his entire household and ruler of all Egypt.'",
      "T": "'So it was not you who sent me here—it was God. He has made me a chief counselor to Pharaoh, lord of his whole household, and ruler over all of Egypt.'"
    },
    "9": {
      "L": "'Hurry and go up to my father and say to him, \"Thus says your son Joseph, God has made me lord of all Egypt. Come down to me; do not tarry.'\"",
      "M": "'Now hurry back to my father and say to him, \"This is what your son Joseph says: God has made me lord of all Egypt. Come down to me; don't delay.'\"",
      "T": "'Hurry back to my father and tell him: \"Your son Joseph says this—God has made me lord of all Egypt. Come down to me right away; do not delay.\"'"
    },
    "10": {
      "L": "'You shall dwell in the land of Goshen, and you shall be near me, you and your children and your children's children, and your flocks, your herds, and all that you have.'",
      "M": "'You shall live in the region of Goshen and be near me—you and your children and grandchildren, your flocks and herds, and all you have.'",
      "T": "'You will settle in the land of Goshen, close to me—you and your children and grandchildren, your flocks, your herds, everything you own.'"
    },
    "11": {
      "L": "'There I will provide for you, for there are yet five years of famine to come, so that you and your household, and all that you have, do not come to poverty.'",
      "M": "'I will provide for you there, because five years of famine are still to come. Otherwise you and your household and all who belong to you will become destitute.'",
      "T": "'I will take care of you there, because five years of famine still remain. I do not want you and your household—everyone belonging to you—to be reduced to poverty.'"
    },
    "12": {
      "L": "'And now your eyes see, and the eyes of my brother Benjamin see, that it is my mouth that speaks to you.'",
      "M": "'You can see for yourselves, and so can my brother Benjamin, that it is really I who am speaking to you.'",
      "T": "'You can see with your own eyes—and Benjamin can see—that it is truly I, Joseph, speaking to you.'"
    },
    "13": {
      "L": "'You must tell my father of all my honor in Egypt, and of all that you have seen. Hurry and bring my father down here.'",
      "M": "'Tell my father about all the honor accorded me in Egypt and about everything you have seen. And bring my father down here quickly.'",
      "T": "'Tell my father about all my honor here in Egypt, everything you have seen. And bring him here to me—quickly!'"
    },
    "14": {
      "L": "Then he fell upon his brother Benjamin's neck and wept, and Benjamin wept upon his neck.",
      "M": "Then he threw his arms around his brother Benjamin and wept, and Benjamin embraced him, weeping.",
      "T": "He threw his arms around his brother Benjamin and wept. Benjamin wept on his neck."
    },
    "15": {
      "L": "And he kissed all his brothers and wept upon them. After that his brothers talked with him.",
      "M": "And he kissed all his brothers and wept over them. Afterward his brothers talked with him.",
      "T": "He kissed each of his brothers and wept over them. After that, his brothers were able to speak with him."
    },
    "16": {
      "L": "When the report was heard in Pharaoh's house, 'Joseph's brothers have come,' it pleased Pharaoh and his servants.",
      "M": "When the news reached Pharaoh's palace that Joseph's brothers had come, Pharaoh and all his officials were pleased.",
      "T": "When word spread through Pharaoh's palace that Joseph's brothers had arrived, Pharaoh and all his officials were delighted."
    },
    "17": {
      "L": "And Pharaoh said to Joseph, 'Say to your brothers, \"Do this: load your beasts and go back to the land of Canaan,'\"",
      "M": "Pharaoh said to Joseph, 'Tell your brothers, \"Do this: Load your animals and return to the land of Canaan,'\"",
      "T": "Pharaoh said to Joseph, 'Tell your brothers: \"Do this—load up your animals and return to Canaan.\"'"
    },
    "18": {
      "L": "'and take your father and your households, and come to me, and I will give you the best of the land of Egypt, and you shall eat the fat of the land.'\"",
      "M": "'\"and bring your father and your families back to me. I will give you the best of the land of Egypt, and you can enjoy the fat of the land.\"'",
      "T": "'\"Bring your father and your families back to me. I will give you the finest land in Egypt, and you will enjoy all its richness.\"'"
    },
    "19": {
      "L": "'And you, Joseph, are commanded to say, \"Do this: take wagons from the land of Egypt for your little ones and for your wives, and bring your father, and come.'\"",
      "M": "'You are also directed to tell them, \"Take some carts from Egypt for your children and your wives, and get your father and come.'\"",
      "T": "'Also tell them: \"Take wagons from Egypt for your wives and your children. Bring your father and come.\"'"
    },
    "20": {
      "L": "'Have no concern for your goods, for the best of all the land of Egypt is yours.'\"",
      "M": "'\"Never mind about your belongings, because the best of all Egypt will be yours.\"'",
      "T": "'\"Do not worry about your possessions—the finest of all Egypt will be waiting for you.\"'"
    },
    "21": {
      "L": "The sons of Israel did so: and Joseph gave them wagons, according to the command of Pharaoh, and gave them provisions for the journey.",
      "M": "The sons of Israel did as they were told. Joseph gave them carts, as Pharaoh had commanded, and he also gave them provisions for their journey.",
      "T": "Israel's sons did as they were told. Joseph gave them wagons as Pharaoh had ordered, and he provided them with supplies for the road."
    },
    "22": {
      "L": "To each and all of them he gave a change of clothes, but to Benjamin he gave three hundred shekels of silver and five changes of clothes.",
      "M": "To each of them he gave new clothing, but to Benjamin he gave three hundred shekels of silver and five sets of clothes.",
      "T": "He gave each brother a fresh set of clothing, but to Benjamin he gave three hundred pieces of silver and five sets of clothing."
    },
    "23": {
      "L": "To his father he sent as follows: ten donkeys loaded with the good things of Egypt, and ten female donkeys loaded with grain, bread, and provision for his father on the journey.",
      "M": "And this is what he sent to his father: ten donkeys loaded with the finest things of Egypt, and ten female donkeys loaded with grain and bread and other provisions for his journey.",
      "T": "For his father he sent ten donkeys loaded with the finest things from Egypt, and ten female donkeys carrying grain, bread, and provisions for the journey."
    },
    "24": {
      "L": "Then he sent his brothers away, and as they departed, he said to them, 'Do not quarrel on the way.'",
      "M": "Then he sent his brothers away, and as they were leaving he said to them, 'Don't quarrel on the way!'",
      "T": "He sent his brothers on their way. As they left, he told them, 'Don't argue with each other along the way!'"
    },
    "25": {
      "L": "So they went up out of Egypt and came to the land of Canaan to their father Jacob.",
      "M": "So they went up out of Egypt and came to their father Jacob in the land of Canaan.",
      "T": "So they went up from Egypt and arrived in the land of Canaan, back to their father Jacob."
    },
    "26": {
      "L": "And they told him, 'Joseph is still alive, and he is ruler over all the land of Egypt.' And his heart became numb, for he did not believe them.",
      "M": "They told him, 'Joseph is still alive! In fact, he is ruler of all Egypt.' Jacob was stunned; he did not believe them.",
      "T": "'Joseph is still alive!' they told him. 'In fact, he is ruler over all of Egypt.' Jacob's heart went numb—he could not believe it."
    },
    "27": {
      "L": "But when they told him all the words of Joseph, which he had said to them, and when he saw the wagons that Joseph had sent to carry him, the spirit of their father Jacob revived.",
      "M": "But when they told him everything Joseph had said to them, and when he saw the carts Joseph had sent to carry him, the spirit of their father Jacob revived.",
      "T": "But when they reported everything Joseph had said, and when Jacob saw the wagons Joseph had sent to bring him—his spirit came back to life."
    },
    "28": {
      "L": "Israel said, 'It is enough; Joseph my son is still alive. I will go and see him before I die.'",
      "M": "And Israel said, 'I'm convinced! My son Joseph is still alive. I will go and see him before I die.'",
      "T": "Israel said, 'Enough! My son Joseph is alive! I will go and see him before I die.'"
    }
  },
  "46": {
    "1": {
      "L": "So Israel took his journey with all that he had and came to Beersheba, and offered sacrifices to the God of his father Isaac.",
      "M": "So Israel set out with all that was his, and when he reached Beersheba, he offered sacrifices to the God of his father Isaac.",
      "T": "Israel set out with everything he owned and came to Beersheba, where he offered sacrifices to the God of his father Isaac."
    },
    "2": {
      "L": "And God spoke to Israel in visions of the night and said, 'Jacob, Jacob.' And he said, 'Here I am.'",
      "M": "And God spoke to Israel in a vision at night and said, 'Jacob! Jacob!' 'Here I am,' he replied.",
      "T": "God spoke to Israel in a vision in the night: 'Jacob! Jacob!' 'Here I am,' he answered."
    },
    "3": {
      "L": "Then he said, 'I am God, the God of your father. Do not be afraid to go down to Egypt, for there I will make you into a great nation.'",
      "M": "'I am God, the God of your father,' he said. 'Do not be afraid to go down to Egypt, for I will make you into a great nation there.'",
      "T": "'I am God—the God of your father. Do not be afraid to go down to Egypt. There I will make you into a great nation.'"
    },
    "4": {
      "L": "'I myself will go down with you to Egypt, and I will also bring you up again, and Joseph's hand shall close your eyes.'",
      "M": "'I will go down to Egypt with you, and I will surely bring you back again. And Joseph's own hand will close your eyes.'",
      "T": "'I will go down to Egypt with you, and I will surely bring you back again. Joseph himself will close your eyes at the end.'"
    },
    "5": {
      "L": "Then Jacob set out from Beersheba. The sons of Israel carried Jacob their father, their little ones, and their wives, in the wagons that Pharaoh had sent to carry him.",
      "M": "Then Jacob left Beersheba, and Israel's sons took their father Jacob and their children and their wives in the carts that Pharaoh had sent to transport him.",
      "T": "Jacob left Beersheba, and his sons brought their father Jacob, their children, and their wives in the wagons Pharaoh had sent."
    },
    "6": {
      "L": "They also took their livestock and their goods, which they had gained in the land of Canaan, and came into Egypt, Jacob and all his offspring with him,",
      "M": "They also took with them their livestock and the possessions they had acquired in Canaan, and Jacob and all his descendants went to Egypt.",
      "T": "They also brought their livestock and everything they had accumulated in Canaan. Jacob and all his descendants went to Egypt."
    },
    "7": {
      "L": "his sons, and his sons' sons with him, his daughters, and his sons' daughters. All his offspring he brought with him into Egypt.",
      "M": "He took his sons and grandsons with him to Egypt—his daughters and granddaughters—all his descendants.",
      "T": "He brought his sons and grandsons, his daughters and granddaughters—all his descendants—to Egypt."
    },
    "8": {
      "L": "Now these are the names of the descendants of Israel, who came into Egypt, Jacob and his sons: Reuben, Jacob's firstborn,",
      "M": "These are the names of the sons of Israel—Jacob and his descendants—who went to Egypt: Reuben, the firstborn of Jacob;",
      "T": "These are the names of Jacob's descendants who went to Egypt: Reuben, Jacob's firstborn;"
    },
    "9": {
      "L": "and the sons of Reuben: Hanoch, Pallu, Hezron, and Carmi.",
      "M": "the sons of Reuben: Hanoch, Pallu, Hezron and Carmi.",
      "T": "the sons of Reuben: Hanoch, Pallu, Hezron, and Carmi."
    },
    "10": {
      "L": "The sons of Simeon: Jemuel, Jamin, Ohad, Jachin, Zohar, and Shaul, the son of a Canaanite woman.",
      "M": "The sons of Simeon: Jemuel, Jamin, Ohad, Jachin, Zohar and Shaul the son of a Canaanite woman.",
      "T": "the sons of Simeon: Jemuel, Jamin, Ohad, Jachin, Zohar, and Shaul the son of a Canaanite woman."
    },
    "11": {
      "L": "The sons of Levi: Gershon, Kohath, and Merari.",
      "M": "The sons of Levi: Gershon, Kohath and Merari.",
      "T": "the sons of Levi: Gershon, Kohath, and Merari."
    },
    "12": {
      "L": "The sons of Judah: Er, Onan, Shelah, Perez, and Zerah (but Er and Onan died in the land of Canaan); and the sons of Perez were Hezron and Hamul.",
      "M": "The sons of Judah: Er, Onan, Shelah, Perez and Zerah (but Er and Onan had died in the land of Canaan). The sons of Perez: Hezron and Hamul.",
      "T": "the sons of Judah: Er, Onan, Shelah, Perez, and Zerah—though Er and Onan had died in Canaan. The sons of Perez: Hezron and Hamul."
    },
    "13": {
      "L": "The sons of Issachar: Tola, Puvah, Yob, and Shimron.",
      "M": "The sons of Issachar: Tola, Puah, Jashub and Shimron.",
      "T": "the sons of Issachar: Tola, Puah, Jashub, and Shimron."
    },
    "14": {
      "L": "The sons of Zebulun: Sered, Elon, and Jahleel.",
      "M": "The sons of Zebulun: Sered, Elon and Jahleel.",
      "T": "the sons of Zebulun: Sered, Elon, and Jahleel."
    },
    "15": {
      "L": "(These are the sons of Leah, whom she bore to Jacob in Paddan-aram, together with his daughter Dinah; altogether his sons and his daughters numbered thirty-three.)",
      "M": "(These were the sons Leah had borne to Jacob in Paddan Aram, besides his daughter Dinah. These sons and daughters of his were thirty-three in all.)",
      "T": "(These were the children Leah bore to Jacob in Paddan-aram, along with his daughter Dinah—thirty-three in all.)"
    },
    "16": {
      "L": "The sons of Gad: Ziphion, Haggi, Shuni, Ezbon, Eri, Arodi, and Areli.",
      "M": "The sons of Gad: Zephon, Haggi, Shuni, Ezbon, Eri, Arodi and Areli.",
      "T": "the sons of Gad: Zephon, Haggi, Shuni, Ezbon, Eri, Arodi, and Areli."
    },
    "17": {
      "L": "The sons of Asher: Imnah, Ishvah, Ishvi, Beriah, and their sister Serah. The sons of Beriah: Heber and Malchiel.",
      "M": "The sons of Asher: Imnah, Ishvah, Ishvi and Beriah. Their sister was Serah. The sons of Beriah: Heber and Malkiel.",
      "T": "the sons of Asher: Imnah, Ishvah, Ishvi, and Beriah, and their sister Serah. The sons of Beriah: Heber and Malchiel."
    },
    "18": {
      "L": "(These are the sons of Zilpah, whom Laban gave to his daughter Leah, and these she bore to Jacob—sixteen persons.)",
      "M": "(These were the children born to Jacob by Zilpah, whom Laban had given to his daughter Leah—sixteen in all.)",
      "T": "(These were the children born to Jacob through Zilpah, whom Laban gave to his daughter Leah—sixteen in all.)"
    },
    "19": {
      "L": "The sons of Rachel, Jacob's wife: Joseph and Benjamin.",
      "M": "The sons of Jacob's wife Rachel: Joseph and Benjamin.",
      "T": "the sons of Jacob's wife Rachel: Joseph and Benjamin."
    },
    "20": {
      "L": "And to Joseph in the land of Egypt were born Manasseh and Ephraim, whom Asenath, the daughter of Potiphera the priest of On, bore to him.",
      "M": "In Egypt, Manasseh and Ephraim were born to Joseph by Asenath daughter of Potiphera, priest of On.",
      "T": "In Egypt, Joseph's wife Asenath—daughter of Potiphera, priest of On—bore him Manasseh and Ephraim."
    },
    "21": {
      "L": "And the sons of Benjamin: Bela, Becher, Ashbel, Gera, Naaman, Ehi, Rosh, Muppim, Huppim, and Ard.",
      "M": "The sons of Benjamin: Bela, Beker, Ashbel, Gera, Naaman, Ehi, Rosh, Muppim, Huppim and Ard.",
      "T": "the sons of Benjamin: Bela, Beker, Ashbel, Gera, Naaman, Ehi, Rosh, Muppim, Huppim, and Ard."
    },
    "22": {
      "L": "(These are the sons of Rachel, who were born to Jacob—fourteen persons in all.)",
      "M": "(These were the children born to Jacob by Rachel—fourteen in all.)",
      "T": "(These were the children born to Jacob through Rachel—fourteen in all.)"
    },
    "23": {
      "L": "The son of Dan: Hushim.",
      "M": "The son of Dan: Hushim.",
      "T": "the son of Dan: Hushim."
    },
    "24": {
      "L": "The sons of Naphtali: Jahzeel, Guni, Jezer, and Shillem.",
      "M": "The sons of Naphtali: Jahzeel, Guni, Jezer and Shillem.",
      "T": "the sons of Naphtali: Jahzeel, Guni, Jezer, and Shillem."
    },
    "25": {
      "L": "(These are the sons of Bilhah, whom Laban gave to his daughter Rachel, and these she bore to Jacob—seven persons in all.)",
      "M": "(These were the children born to Jacob by Bilhah, whom Laban had given to his daughter Rachel—seven in all.)",
      "T": "(These were the children born to Jacob through Bilhah, whom Laban gave to his daughter Rachel—seven in all.)"
    },
    "26": {
      "L": "All the persons belonging to Jacob who came into Egypt, who were his own descendants, not including Jacob's sons' wives, were sixty-six persons in all.",
      "M": "All those who went to Egypt with Jacob—those who were his direct descendants, not counting his sons' wives—numbered sixty-six persons in all.",
      "T": "All the people who went to Egypt with Jacob—his own direct descendants, not counting the wives of his sons—numbered sixty-six."
    },
    "27": {
      "L": "And the sons of Joseph, who were born to him in Egypt, were two. All the persons of the house of Jacob who came into Egypt were seventy.",
      "M": "With the two sons who had been born to Joseph in Egypt, the members of Jacob's family who went to Egypt totaled seventy.",
      "T": "Including the two sons born to Joseph in Egypt, the total of Jacob's household who came to Egypt was seventy."
    },
    "28": {
      "L": "He had sent Judah ahead of him to Joseph to show the way before him in Goshen, and they came into the land of Goshen.",
      "M": "Now Jacob had sent Judah ahead of him to Joseph to get directions to Goshen. When they arrived in the region of Goshen,",
      "T": "Jacob had sent Judah ahead to Joseph to prepare the way to Goshen. They arrived in the land of Goshen."
    },
    "29": {
      "L": "Then Joseph prepared his chariot and went up to meet Israel his father in Goshen. He presented himself to him and fell on his neck and wept on his neck a good while.",
      "M": "Joseph had his chariot made ready and went to Goshen to meet his father Israel. As soon as Joseph appeared before him, he threw his arms around his father and wept for a long time.",
      "T": "Joseph had his chariot readied and went up to Goshen to meet his father Israel. He fell on his father's neck and wept there for a long time."
    },
    "30": {
      "L": "Israel said to Joseph, 'Now let me die, since I have seen your face and know that you are still alive.'",
      "M": "Israel said to Joseph, 'Now I am ready to die, since I have seen for myself that you are still alive.'",
      "T": "Israel said to Joseph, 'Now I can die content—I have seen your face and know you are alive.'"
    },
    "31": {
      "L": "Joseph said to his brothers and to his father's household, 'I will go up and tell Pharaoh and will say to him, \"My brothers and my father's household, who were in the land of Canaan, have come to me.'\"",
      "M": "Then Joseph said to his brothers and to his father's household, 'I will go up and speak to Pharaoh and will say to him, \"My brothers and my father's household, who were living in Canaan, have come to me.'\"",
      "T": "Joseph said to his brothers and to his father's household, 'I am going to speak to Pharaoh and tell him: \"My brothers and my father's household from Canaan have come to me.\"'"
    },
    "32": {
      "L": "'And the men are shepherds, for they have been keepers of livestock, and they have brought their flocks and their herds and all that they have.'",
      "M": "'The men are shepherds; they tend livestock, and they have brought along their flocks and herds and everything they own.'",
      "T": "'These men are shepherds who have always herded livestock. They have brought their flocks, their herds, and all their possessions.'"
    },
    "33": {
      "L": "'When Pharaoh calls you and says, \"What is your occupation?\"'",
      "M": "'When Pharaoh calls you in and asks, \"What is your occupation?\"'",
      "T": "'When Pharaoh summons you and asks what your occupation is,'"
    },
    "34": {
      "L": "'you shall say, \"Your servants have been keepers of livestock from our youth even until now, both we and our fathers,\" in order that you may dwell in the land of Goshen, for every shepherd is an abomination to the Egyptians.'",
      "M": "'you should answer, \"Your servants have tended livestock from our boyhood on, just as our fathers did.\" Then you will be allowed to settle in Goshen, for all shepherds are detestable to the Egyptians.'",
      "T": "'tell him: \"Your servants have been herdsmen from our youth until now—as our fathers were before us.\" This way you will be given the land of Goshen to live in, since Egyptians consider all shepherds an abomination.'"
    }
  },
  "47": {
    "1": {
      "L": "So Joseph went in and told Pharaoh, 'My father and my brothers, with their flocks and herds and all that they possess, have come from the land of Canaan. They are now in the land of Goshen.'",
      "M": "Joseph went and told Pharaoh, 'My father and brothers, with their flocks and herds and everything they own, have come from Canaan and are now in Goshen.'",
      "T": "Joseph went to Pharaoh and said, 'My father and brothers have arrived from Canaan with their flocks, their herds, and all they own. They are now in the land of Goshen.'"
    },
    "2": {
      "L": "And from among his brothers he took five men and presented them to Pharaoh.",
      "M": "He chose five of his brothers and presented them before Pharaoh.",
      "T": "He selected five of his brothers and brought them before Pharaoh."
    },
    "3": {
      "L": "Pharaoh said to his brothers, 'What is your occupation?' And they said to Pharaoh, 'Your servants are shepherds, as our fathers were.'",
      "M": "Pharaoh asked the brothers, 'What is your occupation?' 'Your servants are shepherds,' they replied to Pharaoh, 'just as our fathers were.'",
      "T": "Pharaoh asked the brothers, 'What is your occupation?' They answered, 'Your servants are shepherds, as our fathers were before us.'"
    },
    "4": {
      "L": "They said to Pharaoh, 'We have come to sojourn in the land, for there is no pasture for your servants' flocks, for the famine is severe in the land of Canaan. And now, please let your servants dwell in the land of Goshen.'",
      "M": "They also said to him, 'We have come to live here for a while, because the famine is severe in Canaan and there is no pasture for your servants' flocks. So please let your servants settle in Goshen.'",
      "T": "They also said, 'We have come to live here for a time, because the famine is severe in Canaan and there is no grazing for our flocks. Please allow your servants to settle in the land of Goshen.'"
    },
    "5": {
      "L": "Then Pharaoh said to Joseph, 'Your father and your brothers have come to you.'",
      "M": "Pharaoh said to Joseph, 'Your father and your brothers have come to you,'",
      "T": "Pharaoh said to Joseph, 'Your father and brothers have come to you.'"
    },
    "6": {
      "L": "'The land of Egypt is before you. Settle your father and your brothers in the best of the land. Let them settle in the land of Goshen, and if you know any able men among them, put them in charge of my livestock.'",
      "M": "'and the land of Egypt is before you; settle your father and your brothers in the best part of the land. Let them live in Goshen. And if you know of any among them with special ability, put them in charge of my own livestock.'",
      "T": "'The land of Egypt is open to you. Settle your father and brothers in the best part of the land—let them live in Goshen. And if any of them are particularly capable, put them in charge of my own herds.'"
    },
    "7": {
      "L": "Then Joseph brought in Jacob his father and stood him before Pharaoh, and Jacob blessed Pharaoh.",
      "M": "Joseph brought his father Jacob in and presented him before Pharaoh. After Jacob had blessed Pharaoh,",
      "T": "Then Joseph brought his father Jacob in and presented him to Pharaoh. Jacob blessed Pharaoh."
    },
    "8": {
      "L": "And Pharaoh said to Jacob, 'How many are the days of the years of your life?'",
      "M": "Pharaoh asked him, 'How old are you?'",
      "T": "Pharaoh asked him, 'How old are you?'"
    },
    "9": {
      "L": "And Jacob said to Pharaoh, 'The days of the years of my sojourning are 130 years. Few and evil have been the days of the years of my life, and they have not attained to the days of the years of the life of my fathers in the days of their sojourning.'",
      "M": "And Jacob said to Pharaoh, 'The years of my pilgrimage are a hundred and thirty. My years have been few and difficult, and they do not equal the years of the pilgrimage of my fathers.'",
      "T": "Jacob said to Pharaoh, 'The years of my pilgrimage are one hundred and thirty—few in number and filled with hardship. I have not reached the years my fathers lived during their sojourning.'"
    },
    "10": {
      "L": "And Jacob blessed Pharaoh and went out from the presence of Pharaoh.",
      "M": "Then Jacob blessed Pharaoh and went out from his presence.",
      "T": "Then Jacob blessed Pharaoh and withdrew from his presence."
    },
    "11": {
      "L": "Then Joseph settled his father and his brothers and gave them a possession in the land of Egypt, in the best of the land, in the land of Rameses, as Pharaoh had commanded.",
      "M": "So Joseph settled his father and his brothers in Egypt and gave them property in the best part of the land, the district of Rameses, as Pharaoh directed.",
      "T": "Joseph settled his father and brothers and gave them a holding in the finest part of Egypt—the district of Rameses—exactly as Pharaoh had commanded."
    },
    "12": {
      "L": "And Joseph provided his father, his brothers, and all his father's household with food, according to the number of their dependents.",
      "M": "Joseph also provided his father and his brothers and all his father's household with food, according to the number of their children.",
      "T": "Joseph provided food for his father, his brothers, and everyone in his father's household, according to how many children each family had."
    },
    "13": {
      "L": "Now there was no food in all the land, for the famine was very severe, so that the land of Egypt and the land of Canaan languished by reason of the famine.",
      "M": "There was no food, however, in the whole region because the famine was severe; both Egypt and Canaan wasted away because of the famine.",
      "T": "There was no food anywhere in the region. The famine was so severe that both Egypt and Canaan were wasting away."
    },
    "14": {
      "L": "And Joseph gathered up all the money that was found in the land of Egypt and in the land of Canaan, in exchange for the grain that they bought. And Joseph brought the money into Pharaoh's house.",
      "M": "Joseph collected all the money that was to be found in Egypt and Canaan in payment for the grain they were buying, and he brought it to Pharaoh's palace.",
      "T": "Joseph collected all the silver in Egypt and Canaan in exchange for grain, and he brought it all into Pharaoh's treasury."
    },
    "15": {
      "L": "And when the money was all spent in the land of Egypt and in the land of Canaan, all the Egyptians came to Joseph and said, 'Give us food. Why should we die before your eyes? For our money is gone.'",
      "M": "When the money of the people of Egypt and Canaan was gone, all Egypt came to Joseph and said, 'Give us food. Why should we die before your eyes? Our money is used up.'",
      "T": "When all the money in Egypt and Canaan was gone, all the Egyptians came to Joseph. 'Give us food!' they said. 'Why should we die right in front of you? Our money is gone.'"
    },
    "16": {
      "L": "And Joseph answered, 'Give your livestock, and I will give you food in exchange for your livestock, if your money is gone.'",
      "M": "'Then bring your livestock,' said Joseph. 'I will sell you food in exchange for your livestock, since your money is gone.'",
      "T": "Joseph said, 'If your money is gone, bring your livestock. I will accept your animals in exchange for food.'"
    },
    "17": {
      "L": "So they brought their livestock to Joseph, and Joseph gave them food in exchange for the horses, the flocks, the herds, and the donkeys. He supplied them with food in exchange for all their livestock that year.",
      "M": "So they brought their livestock to Joseph, and he gave them food in exchange for their horses, their sheep and goats, their cattle and donkeys. And he brought them through that year with food in exchange for all their livestock.",
      "T": "So they brought their livestock—horses, sheep, cattle, donkeys—and Joseph gave them food in return. He got them through that year by accepting all their animals in exchange for grain."
    },
    "18": {
      "L": "And when that year was ended, they came to him the following year and said to him, 'We will not hide from my lord that our money is all spent. The herds of livestock are my lord's. There is nothing left in the sight of my lord but our bodies and our land.'",
      "M": "When that year was over, they came to him the following year and said, 'We cannot hide from our lord the fact that since our money is gone and our livestock belongs to you, there is nothing left for our lord except our bodies and our land.'",
      "T": "When that year ended, they came back the next year. 'We will not hide this from you, my lord,' they said. 'Our money is gone. Our livestock belongs to you. All we have left is our bodies and our land.'"
    },
    "19": {
      "L": "'Why should we die before your eyes, both we and our land? Buy us and our land for food, and we with our land will be servants to Pharaoh. And give us seed that we may live and not die, and that the land may not be desolate.'",
      "M": "'Why should we perish before your eyes—we and our land as well? Buy us and our land in exchange for food, and we with our land will be in bondage to Pharaoh. Give us seed so that we may live and not die, and that the land may not become desolate.'",
      "T": "'Why should we die before your eyes—us and our land both? Buy us and our land in exchange for food, and we and our land will become Pharaoh's. Just give us seed so we can live and not die—so the land does not return to wasteland.'"
    },
    "20": {
      "L": "So Joseph bought all the land of Egypt for Pharaoh, for all the Egyptians sold their fields, because the famine was severe on them. The land became Pharaoh's.",
      "M": "So Joseph bought all the land in Egypt for Pharaoh. The Egyptians, one and all, sold their fields, because the famine was too severe for them. The land became Pharaoh's,",
      "T": "So Joseph bought up all the land in Egypt for Pharaoh. The Egyptians sold their fields one by one—the famine was too severe. All the land became Pharaoh's."
    },
    "21": {
      "L": "As for the people, he made servants of them from one end of Egypt to the other.",
      "M": "and Joseph reduced the people to servitude, from one end of Egypt to the other.",
      "T": "And Joseph reduced the people to servants throughout the length of Egypt."
    },
    "22": {
      "L": "Only the land of the priests he did not buy, for the priests had a fixed allowance from Pharaoh and lived on the allowance that Pharaoh gave them; therefore they did not sell their land.",
      "M": "However, he did not buy the land of the priests, because they received a regular allotment from Pharaoh and had food enough from the allotment Pharaoh gave them. That is why they did not sell their land.",
      "T": "The only land he did not buy was the priestly land, because the priests received a regular allotment from Pharaoh and had enough to eat from what Pharaoh gave them. So they did not need to sell their land."
    },
    "23": {
      "L": "Then Joseph said to the people, 'Behold, I have this day bought you and your land for Pharaoh. Now here is seed for you, and you shall sow the land.'",
      "M": "Joseph said to the people, 'Now that I have bought you and your land today for Pharaoh, here is seed for you so you can plant the ground.'",
      "T": "Joseph said to the people, 'Today I have purchased you and your land for Pharaoh. Here is seed for you—plant the land.'"
    },
    "24": {
      "L": "'And at the harvests you shall give a fifth to Pharaoh, and four fifths shall be your own, as seed for the field and as food for yourselves and your households, and as food for your little ones.'",
      "M": "'But when the crop comes in, give a fifth of it to Pharaoh. The other four-fifths you may keep as seed for the fields and as food for yourselves and your households and your children.'",
      "T": "'At harvest time, give one-fifth to Pharaoh. The remaining four-fifths are yours—for seed, for yourselves, your households, and your children.'"
    },
    "25": {
      "L": "And they said, 'You have saved our lives; may it please my lord, we will be servants to Pharaoh.'",
      "M": "'You have saved our lives,' they said. 'May we find favor in the eyes of our lord; we will be in bondage to Pharaoh.'",
      "T": "'You have saved our lives!' they said. 'May we find favor with you, my lord—we will serve Pharaoh.'"
    },
    "26": {
      "L": "So Joseph made it a statute concerning the land of Egypt, and it stands to this day, that Pharaoh should have the fifth; the land of the priests alone did not become Pharaoh's.",
      "M": "So Joseph established it as a law concerning land in Egypt—still in force today—that a fifth of the produce belongs to Pharaoh. It was only the land of the priests that did not become Pharaoh's.",
      "T": "So Joseph established a law throughout Egypt—which stands to this day—that one-fifth of all produce belongs to Pharaoh. Only the priestly land was never transferred to Pharaoh."
    },
    "27": {
      "L": "Thus Israel settled in the land of Egypt, in the land of Goshen. And they gained possessions in it and were fruitful and multiplied greatly.",
      "M": "Now the Israelites settled in Egypt in the region of Goshen. They acquired property there and were fruitful and increased greatly in number.",
      "T": "So Israel settled in the land of Egypt—in the land of Goshen. They acquired property there, were fruitful, and grew in number greatly."
    },
    "28": {
      "L": "And Jacob lived in the land of Egypt seventeen years. So the days of Jacob, the years of his life, were 147 years.",
      "M": "Jacob lived in Egypt seventeen years, and the years of his life were a hundred and forty-seven.",
      "T": "Jacob lived in Egypt for seventeen years, so that the full span of his life was one hundred and forty-seven years."
    },
    "29": {
      "L": "When the time drew near that Israel must die, he called his son Joseph and said to him, 'If now I have found favor in your sight, put your hand under my thigh and promise to deal with me in steadfast love and faithfulness. Do not bury me in Egypt,'",
      "M": "When the time drew near for Israel to die, he called for his son Joseph and said to him, 'If I have found favor in your eyes, put your hand under my thigh and promise that you will show me unfailing loyalty and faithfulness. Do not bury me in Egypt,'",
      "T": "When the time drew near for Israel to die, he called for his son Joseph and said, 'If I have found favor with you, put your hand under my thigh and swear to show me faithful covenant loyalty and truth. Do not bury me in Egypt.'"
    },
    "30": {
      "L": "'but let me lie with my fathers. Carry me out of Egypt and bury me in their burying place.' He answered, 'I will do as you have said.'",
      "M": "'but when I rest with my fathers, carry me out of Egypt and bury me where they are buried.' 'I will do as you say,' he said.",
      "T": "'When I sleep with my fathers, carry me out of Egypt and bury me in their burial place.' Joseph answered, 'I will do what you ask.'"
    },
    "31": {
      "L": "And he said, 'Swear to me'; and he swore to him. Then Israel bowed himself upon the head of his staff.",
      "M": "'Swear to me,' he said. And Joseph swore to him. Then Israel worshiped as he leaned on the top of his staff.",
      "T": "'Swear it to me,' Jacob said. Joseph swore. And Israel bowed in worship at the head of his bed."
    }
  },
  "48": {
    "1": {
      "L": "After this, Joseph was told, 'Behold, your father is ill.' So he took with him his two sons, Manasseh and Ephraim.",
      "M": "Some time later Joseph was told, 'Your father is ill.' So he took his two sons Manasseh and Ephraim along with him.",
      "T": "Some time later, Joseph received word: 'Your father is ill.' He took his two sons Manasseh and Ephraim with him."
    },
    "2": {
      "L": "And it was told to Jacob, 'Your son Joseph has come to you.' Then Israel summoned his strength and sat up in bed.",
      "M": "When Jacob was told, 'Your son Joseph has come to you,' Israel rallied his strength and sat up on the bed.",
      "T": "When Jacob was told, 'Your son Joseph has come,' Israel gathered his strength and sat up in bed."
    },
    "3": {
      "L": "And Jacob said to Joseph, 'God Almighty appeared to me at Luz in the land of Canaan and blessed me,'",
      "M": "Jacob said to Joseph, 'God Almighty appeared to me at Luz in the land of Canaan, and there he blessed me'",
      "T": "Jacob said to Joseph, 'God Almighty appeared to me at Luz in Canaan and blessed me.'"
    },
    "4": {
      "L": "'and said to me, \"Behold, I will make you fruitful and multiply you, and I will make of you a company of peoples and will give this land to your offspring after you for an everlasting possession.\"'",
      "M": "'and said to me, \"I am going to make you fruitful and increase your numbers. I will make you a community of peoples, and I will give this land as an everlasting possession to your descendants after you.\"'",
      "T": "'He said to me, \"I will make you fruitful and multiply your numbers. I will make you into a community of peoples, and I will give this land to your descendants as a permanent possession.\"'"
    },
    "5": {
      "L": "'And now your two sons, who were born to you in the land of Egypt before I came to you in Egypt, are mine; Ephraim and Manasseh shall be mine, as Reuben and Simeon are mine.'",
      "M": "'Now then, your two sons born to you in Egypt before I came to you here will be reckoned as mine; Ephraim and Manasseh will be mine, just as Reuben and Simeon are mine.'",
      "T": "'Now your two sons born to you in Egypt before I came here—Ephraim and Manasseh—are mine. They are counted as my sons, just as Reuben and Simeon are mine.'"
    },
    "6": {
      "L": "'And the children that you fathered after them shall be yours. They shall be called by the name of their brothers in their inheritance.'",
      "M": "'Any children born to you after them will be yours; in the territory they inherit they will be reckoned under the names of their brothers.'",
      "T": "'Any children you have after them will be yours. But in matters of inheritance they will be counted under the names of their two brothers.'"
    },
    "7": {
      "L": "'As for me, when I came from Paddan, Rachel died to my grief in the land of Canaan on the way, when there was still some distance to go to Ephrath, and I buried her there on the way to Ephrath (that is, Bethlehem).'",
      "M": "'As I was returning from Paddan, to my sorrow Rachel died in the land of Canaan while we were still on the way, a little distance from Ephrath. So I buried her there beside the road to Ephrath (that is, Bethlehem).'",
      "T": "'As I was coming from Paddan, Rachel died—and it was a grief to me—in the land of Canaan, while we were on the road, still some distance from Ephrath. I buried her there, right by the road to Ephrath, which is Bethlehem.'"
    },
    "8": {
      "L": "When Israel saw Joseph's sons, he said, 'Who are these?'",
      "M": "When Israel saw the sons of Joseph, he asked, 'Who are these?'",
      "T": "Israel noticed Joseph's sons and asked, 'Who are these boys?'"
    },
    "9": {
      "L": "Joseph said to his father, 'They are my sons, whom God has given me here.' And he said, 'Bring them to me, please, that I may bless them.'",
      "M": "'They are the sons God has given me here,' Joseph said to his father. Then Israel said, 'Bring them to me so I may bless them.'",
      "T": "'These are my sons, whom God has given me here in Egypt,' Joseph said. Israel said, 'Bring them to me so I can bless them.'"
    },
    "10": {
      "L": "Now the eyes of Israel were dim with age, so that he could not see. Joseph brought them near him, and he kissed them and embraced them.",
      "M": "Now Israel's eyes were failing because of old age, and he could hardly see. So Joseph brought his sons close to him, and his father kissed them and embraced them.",
      "T": "Israel's eyes were dim with age and he could barely see. Joseph brought the boys close, and Jacob kissed them and held them."
    },
    "11": {
      "L": "And Israel said to Joseph, 'I never expected to see your face; and behold, God has let me see your offspring also.'",
      "M": "Israel said to Joseph, 'I never expected to see your face again, and now God has allowed me to see your children too.'",
      "T": "Israel said to Joseph, 'I never thought I would see your face again—and now God has even let me see your children.'"
    },
    "12": {
      "L": "Then Joseph removed them from his knees, and he bowed himself with his face to the earth.",
      "M": "Then Joseph removed them from Israel's knees and bowed down with his face to the ground.",
      "T": "Joseph drew them away from Jacob's knees and bowed down to the ground before him."
    },
    "13": {
      "L": "And Joseph took them both, Ephraim in his right hand toward Israel's left hand, and Manasseh in his left hand toward Israel's right hand, and brought them near him.",
      "M": "And Joseph took both of them, Ephraim on his right toward Israel's left hand and Manasseh on his left toward Israel's right hand, and brought them close to him.",
      "T": "Joseph took both boys—Ephraim on his right, positioned toward Israel's left, and Manasseh on his left, toward Israel's right—and brought them close."
    },
    "14": {
      "L": "And Israel stretched out his right hand and laid it on the head of Ephraim, who was the younger, and his left hand on the head of Manasseh, crossing his hands (for Manasseh was the firstborn).",
      "M": "But Israel reached out his right hand and put it on Ephraim's head, though he was the younger, and crossing his arms, he put his left hand on Manasseh's head, even though Manasseh was the firstborn.",
      "T": "But Israel deliberately crossed his arms—placing his right hand on Ephraim's head, the younger one, and his left hand on Manasseh's head, even though Manasseh was the firstborn."
    },
    "15": {
      "L": "And he blessed Joseph and said, 'The God before whom my fathers Abraham and Isaac walked, the God who has been my shepherd all my life long to this day,'",
      "M": "Then he blessed Joseph and said: 'May the God before whom my fathers Abraham and Isaac walked, the God who has been my shepherd all my life to this day,'",
      "T": "He blessed Joseph and said: 'May the God before whom my fathers Abraham and Isaac walked— the God who has been my shepherd all my life long to this very day—'"
    },
    "16": {
      "L": "'the angel who has redeemed me from all evil, bless the boys; and in them let my name be carried on, and the name of my fathers Abraham and Isaac; and let them grow into a multitude in the midst of the earth.'",
      "M": "'the Angel who has delivered me from all harm—may he bless these boys. May they be called by my name and the names of my fathers Abraham and Isaac, and may they increase greatly on the earth.'",
      "T": "'and the Angel who has redeemed me from every harm— bless these boys. May my name live on in them, and the name of my fathers Abraham and Isaac. May they grow into a great multitude throughout the earth.'"
    },
    "17": {
      "L": "When Joseph saw that his father laid his right hand on the head of Ephraim, it displeased him, and he took his father's hand to move it from Ephraim's head to Manasseh's head.",
      "M": "When Joseph saw his father placing his right hand on Ephraim's head he was displeased; so he took hold of his father's hand to move it from Ephraim's head to Manasseh's head.",
      "T": "When Joseph saw that his father had placed his right hand on Ephraim's head, he was displeased. He reached out to move his father's hand from Ephraim's head to Manasseh's."
    },
    "18": {
      "L": "And Joseph said to his father, 'Not this way, my father; since this one is the firstborn, put your right hand on his head.'",
      "M": "Joseph said to him, 'No, my father, this one is the firstborn; put your right hand on his head.'",
      "T": "'No, Father,' Joseph said. 'This one is the firstborn. Put your right hand on his head.'"
    },
    "19": {
      "L": "But his father refused and said, 'I know, my son, I know. He also shall become a people, and he also shall be great. Nevertheless, his younger brother shall be greater than he, and his offspring shall become a multitude of nations.'",
      "M": "But his father refused and said, 'I know, my son, I know. He too will become a people, and he too will become great. Nevertheless, his younger brother will be greater than he, and his descendants will become a group of nations.'",
      "T": "But his father refused. 'I know, my son, I know,' he said. 'Manasseh will also become a great people. But his younger brother will be greater—his descendants will become a multitude of nations.'"
    },
    "20": {
      "L": "So he blessed them that day, saying, 'By you Israel will pronounce blessings, saying, \"God make you as Ephraim and as Manasseh.\"' Thus he put Ephraim before Manasseh.",
      "M": "He blessed them that day and said, 'In your name will Israel pronounce this blessing: \"May God make you like Ephraim and Manasseh.\"' So he put Ephraim ahead of Manasseh.",
      "T": "He blessed them that day with these words: 'In your names, Israel will give blessings, saying, \"May God make you like Ephraim and Manasseh.\"' In this way he placed Ephraim before Manasseh."
    },
    "21": {
      "L": "Then Israel said to Joseph, 'Behold, I am about to die, but God will be with you and will bring you again to the land of your fathers.'",
      "M": "Then Israel said to Joseph, 'I am about to die, but God will be with you and take you back to the land of your fathers.'",
      "T": "Then Israel said to Joseph, 'I am about to die. But God will be with you and will bring you back to the land of your fathers.'"
    },
    "22": {
      "L": "'Moreover, I have given to you rather than to your brothers one mountain slope that I took from the hand of the Amorites with my sword and with my bow.'",
      "M": "'And to you I give one more ridge of land than to your brothers, the ridge I took from the Amorites with my sword and my bow.'",
      "T": "'And to you above your brothers I give the ridge of land—Shechem—that I took from the Amorites with my sword and bow.'"
    }
  },
  "49": {
    "1": {
      "L": "Then Jacob called his sons and said, 'Gather yourselves together, that I may tell you what shall happen to you in days to come.'",
      "M": "Then Jacob called for his sons and said: 'Gather around so I can tell you what will happen to you in days to come.'",
      "T": "Jacob called for his sons. 'Come together,' he said, 'so I may tell you what lies ahead in the days to come.'"
    },
    "2": {
      "L": "'Assemble and listen, O sons of Jacob, listen to Israel your father.'",
      "M": "'Assemble and listen, sons of Jacob; listen to your father Israel.'",
      "T": "'Gather and hear, O sons of Jacob; listen to Israel your father.'"
    },
    "3": {
      "L": "'Reuben, you are my firstborn, my might, and the firstfruits of my strength, excelling in honor and excelling in power.'",
      "M": "'Reuben, you are my firstborn, my might, the first sign of my strength, excelling in honor, excelling in power.'",
      "T": "'Reuben, my firstborn— my strength, the firstfruits of my vigor; first in honor, first in power.'"
    },
    "4": {
      "L": "'Turbulent as water, you shall not excel, because you went up to your father's bed; then you defiled it—he went up to my couch!'",
      "M": "'Turbulent as the floods, you will no longer excel, for you went up onto your father's bed, onto my couch and defiled it.'",
      "T": "'Reckless as floodwaters, you shall not have preeminence— for you climbed into your father's bed and defiled his couch. You went up!'"
    },
    "5": {
      "L": "'Simeon and Levi are brothers; weapons of violence are their swords.'",
      "M": "'Simeon and Levi are brothers—their swords are weapons of violence.'",
      "T": "'Simeon and Levi are brothers— their very weapons are instruments of brutality.'"
    },
    "6": {
      "L": "'Let my soul not come into their council; O my honor, be not joined to their company. For in their anger they killed men, and in their willfulness they hamstrung oxen.'",
      "M": "'Let me not enter their council, let me not join their assembly, for they have killed men in their anger and hamstrung oxen as they pleased.'",
      "T": "'Let me have no part in their council; let my honor not be joined to their company— for in their rage they murdered men, and in their recklessness they hamstrung oxen.'"
    },
    "7": {
      "L": "'Cursed be their anger, for it is fierce, and their wrath, for it is cruel! I will divide them in Jacob and scatter them in Israel.'",
      "M": "'Cursed be their anger, so fierce, and their fury, so cruel! I will scatter them in Jacob and disperse them in Israel.'",
      "T": "'Cursed be their ferocious anger, their brutal fury! I will scatter them throughout Jacob and disperse them across Israel.'"
    },
    "8": {
      "L": "'Judah, your brothers shall praise you; your hand shall be on the neck of your enemies; your father's sons shall bow down before you.'",
      "M": "'Judah, your brothers will praise you; your hand will be on the neck of your enemies; your father's sons will bow down to you.'",
      "T": "'Judah—your brothers will praise you; your hand will grip the necks of your enemies; your father's sons will bow before you.'"
    },
    "9": {
      "L": "'Judah is a lion's cub; from the prey, my son, you have gone up. He stooped down; he crouched as a lion and as a lioness; who dares rouse him?'",
      "M": "'You are a lion's cub, Judah; you return from the prey, my son. Like a lion he crouches and lies down, like a lioness—who dares to rouse him?'",
      "T": "'Judah is a lion's cub— he climbs back from the kill, my son. He crouches, he lies down like a lion, like a great lioness— who would dare rouse him?'"
    },
    "10": {
      "L": "'The scepter shall not depart from Judah, nor the ruler's staff from between his feet, until Shiloh comes; and to him shall be the obedience of the peoples.'",
      "M": "'The scepter will not depart from Judah, nor the ruler's staff from between his feet, until the one to whom it belongs comes; and the obedience of the nations will be his.'",
      "T": "'The scepter will not leave Judah, nor the ruler's staff from between his feet— until he comes to whom kingship belongs; and the peoples will gather to obey him.'"
    },
    "11": {
      "L": "'Binding his foal to the vine and his donkey's colt to the choice vine, he has washed his garments in wine and his vesture in the blood of grapes.'",
      "M": "'He will tether his donkey to a vine, his colt to the choicest branch; he will wash his garments in wine, his robes in the blood of grapes.'",
      "T": "'He ties his donkey to the vine, his colt to the finest branch— he washes his robes in wine, his garments in the juice of grapes.'"
    },
    "12": {
      "L": "'His eyes are darker than wine, and his teeth whiter than milk.'",
      "M": "'His eyes will be darker than wine, his teeth whiter than milk.'",
      "T": "'His eyes are darker than wine, his teeth brighter than milk.'"
    },
    "13": {
      "L": "'Zebulun shall dwell at the shore of the sea; he shall become a haven for ships, and his border shall be at Sidon.'",
      "M": "'Zebulun will live by the seashore and become a haven for ships; his border will extend toward Sidon.'",
      "T": "'Zebulun will dwell at the seashore, a harbor for ships, with his border reaching toward Sidon.'"
    },
    "14": {
      "L": "'Issachar is a strong donkey, crouching between the sheepfolds.'",
      "M": "'Issachar is a rawboned donkey lying down between two saddlebags.'",
      "T": "'Issachar is a sturdy donkey crouching between two loaded panniers.'"
    },
    "15": {
      "L": "'He saw that a resting place was good, and that the land was pleasant, so he bowed his shoulder to bear, and became a servant at forced labor.'",
      "M": "'When he sees how good is his resting place and how pleasant is his land, he will bend his shoulder to the burden and submit to forced labor.'",
      "T": "'He saw the resting place was good and the land was pleasant— so he bent his back to the load and became a laborer under tribute.'"
    },
    "16": {
      "L": "'Dan shall judge his people as one of the tribes of Israel.'",
      "M": "'Dan will provide justice for his people as one of the tribes of Israel.'",
      "T": "'Dan will judge his people like any other tribe in Israel.'"
    },
    "17": {
      "L": "'Dan shall be a serpent in the way, a viper by the path, that bites the horse's heels so that his rider falls backward.'",
      "M": "'Dan will be a serpent by the roadside, a viper along the path, that bites the horse's heels so that its rider tumbles backward.'",
      "T": "'Dan will be a serpent on the road, a viper on the path— striking the horse's heel so its rider falls backward.'"
    },
    "18": {
      "L": "'I wait for your salvation, O LORD.'",
      "M": "'I look for your deliverance, LORD.'",
      "T": "'LORD, I look to you for salvation!'"
    },
    "19": {
      "L": "'Raiders shall raid Gad, but he shall raid at their heels.'",
      "M": "'Gad will be attacked by a band of raiders, but he will attack them at their heels.'",
      "T": "'Gad—raiders will raid him, but he will raid at their heels.'"
    },
    "20": {
      "L": "'Asher's food shall be rich, and he shall yield royal delicacies.'",
      "M": "'Asher's food will be rich; he will provide delicacies fit for a king.'",
      "T": "'Asher will eat from rich soil and furnish delicacies worthy of a king's table.'"
    },
    "21": {
      "L": "'Naphtali is a doe let loose that bears beautiful fawns.'",
      "M": "'Naphtali is a doe set free that bears beautiful fawns.'",
      "T": "'Naphtali is a swift doe released to the open— she bears beautiful fawns.'"
    },
    "22": {
      "L": "'Joseph is a fruitful bough, a fruitful bough by a spring; his branches run over the wall.'",
      "M": "'Joseph is a fruitful vine, a fruitful vine near a spring, whose branches climb over a wall.'",
      "T": "'Joseph is a fruitful vine growing beside a spring— his branches climb and spread over the wall.'"
    },
    "23": {
      "L": "'The archers bitterly attacked him, shot at him, and harassed him severely,'",
      "M": "'With bitterness archers attacked him; they shot at him with hostility.'",
      "T": "'Archers attacked him with bitterness, they shot at him and pressed him hard—'"
    },
    "24": {
      "L": "'yet his bow remained unmoved; his arms were made agile by the hands of the Mighty One of Jacob (from there is the Shepherd, the Stone of Israel),'",
      "M": "'But his bow remained steady, his strong arms stayed limber, because of the hand of the Mighty One of Jacob, because of the Shepherd, the Rock of Israel,'",
      "T": "'yet his bow held steady and his arms stayed strong— by the hands of the Mighty One of Jacob, by the Shepherd and Stone of Israel—'"
    },
    "25": {
      "L": "'by the God of your father who will help you, by the Almighty who will bless you with blessings of heaven above, blessings of the deep that crouches beneath, blessings of the breasts and of the womb.'",
      "M": "'because of your father's God, who helps you, because of the Almighty, who blesses you with blessings of the skies above, blessings of the deep springs below, blessings of the breast and womb.'",
      "T": "'by your father's God who helps you, by the Almighty who blesses you— with blessings from the heavens above, blessings from the deep below, blessings of the breast and the womb.'"
    },
    "26": {
      "L": "'The blessings of your father are mighty beyond the blessings of my parents, up to the bounties of the everlasting hills. May they be on the head of Joseph, and on the brow of him who was set apart from his brothers.'",
      "M": "'Your father's blessings are greater than the blessings of the ancient mountains, than the bounty of the age-old hills. Let all these rest on the head of Joseph, on the brow of the prince among his brothers.'",
      "T": "'The blessings of your father surpass those of the ancient mountains, the gifts of the eternal hills— may they rest on the head of Joseph, on the brow of the one set apart from his brothers.'"
    },
    "27": {
      "L": "'Benjamin is a ravenous wolf; in the morning devouring the prey and at evening dividing the plunder.'",
      "M": "'Benjamin is a ravenous wolf; in the morning he devours the prey, in the evening he divides the plunder.'",
      "T": "'Benjamin is a ravenous wolf— in the morning he devours his prey, at evening he divides the spoil.'"
    },
    "28": {
      "L": "All these are the twelve tribes of Israel. This is what their father said to them as he blessed them, blessing each with the blessing suitable to him.",
      "M": "All these are the twelve tribes of Israel, and this is what their father said to them when he blessed them, giving each the blessing appropriate to him.",
      "T": "These are the twelve tribes of Israel. This is what their father spoke over them when he blessed them, giving to each the blessing that fit him."
    },
    "29": {
      "L": "Then he commanded them and said to them, 'I am to be gathered to my people; bury me with my fathers in the cave that is in the field of Ephron the Hittite,'",
      "M": "Then he gave them these instructions: 'I am about to be gathered to my people. Bury me with my fathers in the cave in the field of Ephron the Hittite,'",
      "T": "Then he gave them their final instructions: 'I am about to be gathered to my people. Bury me with my fathers in the cave in the field of Ephron the Hittite—'"
    },
    "30": {
      "L": "'in the cave that is in the field at Machpelah, to the east of Mamre, in the land of Canaan, which Abraham bought with the field from Ephron the Hittite to possess as a burying place.'",
      "M": "'in the cave in the field of Machpelah, near Mamre in Canaan, which Abraham bought along with the field as a burial place from Ephron the Hittite.'",
      "T": "'the cave at Machpelah, east of Mamre in Canaan—the cave Abraham bought from Ephron the Hittite as a burial ground.'"
    },
    "31": {
      "L": "'There they buried Abraham and Sarah his wife. There they buried Isaac and Rebekah his wife, and there I buried Leah—'",
      "M": "'There Abraham and his wife Sarah were buried, there Isaac and his wife Rebekah were buried, and there I buried Leah.'",
      "T": "'Abraham and Sarah are buried there, Isaac and Rebekah are buried there, and there I buried Leah.'"
    },
    "32": {
      "L": "'the field and the cave that is in it were bought from the Hittites.'",
      "M": "'The field and the cave in it were bought from the Hittites.'",
      "T": "'The field and the cave were purchased from the Hittites.'"
    },
    "33": {
      "L": "When Jacob finished commanding his sons, he drew up his feet into the bed and breathed his last and was gathered to his people.",
      "M": "When Jacob had finished giving instructions to his sons, he drew his feet up into the bed, breathed his last and was gathered to his people.",
      "T": "When Jacob had finished his final words to his sons, he drew his feet up into the bed, breathed his last breath, and was gathered to his people."
    }
  },
  "50": {
    "1": {
      "L": "Then Joseph fell on his father's face and wept over him and kissed him.",
      "M": "Joseph threw himself on his father and wept over him and kissed him.",
      "T": "Joseph fell on his father's face, wept over him, and kissed him."
    },
    "2": {
      "L": "And Joseph commanded his servants the physicians to embalm his father. So the physicians embalmed Israel.",
      "M": "Then Joseph directed the physicians in his service to embalm his father Israel. So the physicians embalmed him,",
      "T": "Joseph ordered the physicians who served him to embalm his father. They embalmed Israel."
    },
    "3": {
      "L": "Forty days were required for it, for that is how many are required for embalming. And the Egyptians wept for him seventy days.",
      "M": "taking a full forty days, for that was the time required for embalming. And the Egyptians mourned for him seventy days.",
      "T": "The embalming took the full forty days required. And the Egyptians mourned him for seventy days."
    },
    "4": {
      "L": "And when the days of weeping for him were past, Joseph spoke to the household of Pharaoh, saying, 'If now I have found favor in your eyes, please speak in the ears of Pharaoh, saying,'",
      "M": "When the days of mourning had passed, Joseph said to Pharaoh's household, 'If I have found favor in your eyes, speak to Pharaoh for me. Tell him,'",
      "T": "When the mourning period was over, Joseph spoke to Pharaoh's household: 'If I have found favor with you, please speak to Pharaoh on my behalf. Tell him:'"
    },
    "5": {
      "L": "'\"My father made me swear, saying, \"I am about to die: in my tomb that I hewed out for myself in the land of Canaan, there shall you bury me.\" Now therefore, let me please go up and bury my father. Then I will return.\"'",
      "M": "'\"My father made me swear an oath and said, \"I am about to die; bury me in the tomb I dug for myself in the land of Canaan.\" Now please let me go up and bury my father; then I will return.\"'",
      "T": "'\"My father made me swear: he said, \"I am about to die—bury me in the tomb I cut for myself in Canaan.\" Please allow me to go and bury my father, and then I will return.\"'"
    },
    "6": {
      "L": "And Pharaoh answered, 'Go up, and bury your father, as he made you swear.'",
      "M": "Pharaoh said, 'Go up and bury your father, as he made you swear to do.'",
      "T": "Pharaoh answered, 'Go and bury your father, as you swore to him.'"
    },
    "7": {
      "L": "So Joseph went up to bury his father. With him went up all the servants of Pharaoh, the elders of his household, and all the elders of the land of Egypt,",
      "M": "So Joseph went up to bury his father. All Pharaoh's officials accompanied him—the dignitaries of his court and all the dignitaries of Egypt—",
      "T": "So Joseph went up to bury his father. All of Pharaoh's officials accompanied him—the elders of his palace and all the senior officials of Egypt—"
    },
    "8": {
      "L": "as well as all the household of Joseph, his brothers, and his father's household. Only their children, their flocks, and their herds were left in the land of Goshen.",
      "M": "together with all the members of Joseph's household and his brothers and those belonging to his father's household. Only their children and their flocks and herds were left in Goshen.",
      "T": "along with all of Joseph's household, his brothers, and his father's household. Only their children, their flocks, and their herds were left behind in Goshen."
    },
    "9": {
      "L": "And there went up with him both chariots and horsemen. It was a very great company.",
      "M": "Chariots and horsemen also went up with him. It was a very large company.",
      "T": "Chariots and cavalry went with them as well. It was an enormous company."
    },
    "10": {
      "L": "When they came to the threshing floor of Atad, which is beyond the Jordan, they lamented there with a very great and grievous lamentation, and he made a mourning for his father seven days.",
      "M": "When they reached the threshing floor of Atad, near the Jordan, they lamented loudly and bitterly; and there Joseph observed a seven-day period of mourning for his father.",
      "T": "When they came to the threshing floor of Atad, beyond the Jordan, they mourned with a great and bitter lamentation. Joseph observed a seven-day mourning period for his father there."
    },
    "11": {
      "L": "When the inhabitants of the land, the Canaanites, saw the mourning on the threshing floor of Atad, they said, 'This is a grievous mourning by the Egyptians.' Therefore the place was named Abel-mizraim; it is beyond the Jordan.",
      "M": "When the Canaanites who lived there saw the mourning at the threshing floor of Atad, they said, 'The Egyptians are holding a solemn ceremony of mourning.' That is why that place near the Jordan is called Abel Mizraim.",
      "T": "When the Canaanites who lived there saw the mourning at the threshing floor of Atad, they said, 'What solemn mourning by the Egyptians!' So the place was named Abel-mizraim—it is beyond the Jordan."
    },
    "12": {
      "L": "Thus his sons did for him as he had commanded them.",
      "M": "So Jacob's sons did as he had commanded them:",
      "T": "Jacob's sons did exactly as he had instructed them."
    },
    "13": {
      "L": "For his sons carried him to the land of Canaan and buried him in the cave of the field at Machpelah, to the east of Mamre, which Abraham bought with the field from Ephron the Hittite to possess as a burying place.",
      "M": "They carried him to the land of Canaan and buried him in the cave in the field of Machpelah, near Mamre, which Abraham had bought along with the field as a burial place from Ephron the Hittite.",
      "T": "They carried him to Canaan and buried him in the cave at Machpelah east of Mamre—the cave Abraham had bought from Ephron the Hittite as a burial ground."
    },
    "14": {
      "L": "After he had buried his father, Joseph returned to Egypt with his brothers and all who had gone up with him to bury his father.",
      "M": "After burying his father, Joseph returned to Egypt, together with his brothers and all the others who had gone with him to bury his father.",
      "T": "After burying his father, Joseph returned to Egypt with his brothers and all who had come up with him."
    },
    "15": {
      "L": "When Joseph's brothers saw that their father was dead, they said, 'It may be that Joseph will hate us and pay us back for all the evil that we did to him.'",
      "M": "When Joseph's brothers saw that their father was dead, they said, 'What if Joseph holds a grudge against us and pays us back for all the wrongs we did to him?'",
      "T": "When Joseph's brothers saw that their father was dead, they said, 'What if Joseph is holding a grudge and decides to pay us back for everything we did to him?'"
    },
    "16": {
      "L": "So they sent a message to Joseph, saying, 'Your father gave this command before he died,'",
      "M": "So they sent word to Joseph, saying, 'Your father left these instructions before he died:'",
      "T": "They sent a message to Joseph: 'Before your father died, he gave this instruction:'"
    },
    "17": {
      "L": "'\"Say to Joseph, Please forgive the transgression of your brothers and their sin, because they did evil to you.\" And now, please forgive the transgression of the servants of the God of your father.' Joseph wept when they spoke to him.",
      "M": "'\"Say to Joseph: I ask you to forgive your brothers the sins and the wrongs they committed in treating you so badly.\" Now please forgive the sins of the servants of the God of your father.' When their message came to him, Joseph wept.",
      "T": "'\"Tell Joseph: please forgive the transgression of your brothers and the sin they committed against you.\" Now we also ask you to forgive the sin of the servants of the God of your father.' When this reached Joseph, he wept."
    },
    "18": {
      "L": "His brothers also came and fell down before him and said, 'Behold, we are your servants.'",
      "M": "His brothers then came and threw themselves down before him. 'We are your slaves,' they said.",
      "T": "His brothers came and fell down before him. 'We are your servants,' they said."
    },
    "19": {
      "L": "But Joseph said to them, 'Do not fear, for am I in the place of God?'",
      "M": "But Joseph said to them, 'Don't be afraid. Am I in the place of God?'",
      "T": "But Joseph said to them, 'Do not be afraid. Am I in the place of God?'"
    },
    "20": {
      "L": "'As for you, you meant evil against me, but God meant it for good, to bring it about that many people should be kept alive, as they are today.'",
      "M": "'You intended to harm me, but God intended it for good to accomplish what is now being done—the saving of many lives.'",
      "T": "'You plotted evil against me—but God wove those very plans into good, so that many people would be kept alive. And so it is today.'"
    },
    "21": {
      "L": "'So do not fear; I will provide for you and your little ones.' Thus he comforted them and spoke kindly to them.",
      "M": "'So then, don't be afraid. I will provide for you and your children.' And he reassured them and spoke kindly to them.",
      "T": "'So do not be afraid. I will provide for you and your children.' He comforted them and spoke tenderly to them."
    },
    "22": {
      "L": "Joseph lived in Egypt, he and his father's house. Joseph lived 110 years.",
      "M": "Joseph stayed in Egypt, along with all his father's family. He lived a hundred and ten years",
      "T": "Joseph remained in Egypt, he and all his father's household. Joseph lived one hundred and ten years."
    },
    "23": {
      "L": "And Joseph saw Ephraim's children of the third generation. The children also of Machir the son of Manasseh were counted as Joseph's own.",
      "M": "and saw the third generation of Ephraim's children. Also the children of Makir son of Manasseh were placed at birth on Joseph's knees.",
      "T": "He lived to see Ephraim's children to the third generation. The children of Makir, the son of Manasseh, were also counted as his own."
    },
    "24": {
      "L": "And Joseph said to his brothers, 'I am about to die, but God will visit you and bring you up out of this land to the land that he swore to Abraham, to Isaac, and to Jacob.'",
      "M": "Then Joseph said to his brothers, 'I am about to die. But God will surely come to your aid and take you up out of this land to the land he promised on oath to Abraham, Isaac and Jacob.'",
      "T": "Joseph said to his brothers, 'I am about to die. But God will surely come to your aid and bring you up out of this land to the land he swore to give Abraham, Isaac, and Jacob.'"
    },
    "25": {
      "L": "Then Joseph made the sons of Israel swear, saying, 'God will surely visit you, and you shall carry up my bones from here.'",
      "M": "And Joseph made the Israelites swear an oath and said, 'God will surely come to your aid, and then you must carry my bones up from this place.'",
      "T": "Joseph made the sons of Israel swear an oath: 'God will surely come to your aid—when he does, you must carry my bones up from this place.'"
    },
    "26": {
      "L": "So Joseph died, being 110 years old. They embalmed him, and he was put in a coffin in Egypt.",
      "M": "And Joseph died at the age of a hundred and ten. And after they embalmed him, he was placed in a coffin in Egypt.",
      "T": "Joseph died at the age of one hundred and ten. They embalmed him, and he was placed in a coffin in Egypt."
    }
  }
}

def main():
    print('Writing Genesis chapters 44–50...')
    for tier_key, tier_folder in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_folder, 'genesis')
        merge_tier(existing, GENESIS, tier_key)
        save(tier_folder, 'genesis', existing)
    print('Done.')

if __name__ == '__main__':
    main()
