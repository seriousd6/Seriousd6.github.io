"""
MKT Mark chapters 5-8 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-mark-5-8.py
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

MARK = {
  "5": {
    "1": {
      "L": "They came to the other side of the sea, to the region of the Gerasenes.",
      "M": "They went across the lake to the region of the Gerasenes.",
      "T": "They crossed the lake and came to the region of the Gerasenes."
    },
    "2": {
      "L": "And when he had stepped out of the boat, immediately a man from the tombs with an unclean spirit met him.",
      "M": "When Jesus got out of the boat, a man with an impure spirit came from the tombs to meet him.",
      "T": "As soon as Jesus got out of the boat, a man with an evil spirit came out of the tombs to meet him."
    },
    "3": {
      "L": "He lived among the tombs. And no one was able to bind him anymore, not even with a chain;",
      "M": "This man lived in the tombs, and no one could bind him anymore, not even with a chain.",
      "T": "This man lived among the tombs. No one could restrain him—not even with chains."
    },
    "4": {
      "L": "for he had often been bound with shackles and chains, and the chains he had wrenched apart and the shackles broken in pieces. No one had the strength to subdue him.",
      "M": "For he had often been chained hand and foot, but he tore the chains apart and broke the irons on his feet. No one was strong enough to subdue him.",
      "T": "He had been bound hand and foot many times, but he snapped the chains and smashed the shackles. No one could tame him."
    },
    "5": {
      "L": "Night and day among the tombs and in the mountains he was always crying out and cutting himself with stones.",
      "M": "Night and day among the tombs and in the hills he would cry out and cut himself with stones.",
      "T": "Day and night he roamed the tombs and the hills, screaming and gashing himself with stones."
    },
    "6": {
      "L": "And seeing Jesus from afar, he ran and fell down before him.",
      "M": "When he saw Jesus from a distance, he ran and fell on his knees in front of him.",
      "T": "When he spotted Jesus from a distance, he ran and threw himself at Jesus' feet."
    },
    "7": {
      "L": "And crying out with a loud voice, he said, 'What have you to do with me, Jesus, Son of the Most High God? I adjure you by God, do not torment me.'",
      "M": "He shouted at the top of his voice, 'What do you want with me, Jesus, Son of the Most High God? In God's name don't torture me!'",
      "T": "He screamed at the top of his voice: 'What do you want with me, Jesus, Son of the Most High God? I beg you—in God's name—don't torture me!'"
    },
    "8": {
      "L": "For he was saying to him, 'Come out of the man, you unclean spirit!'",
      "M": "For Jesus had said to him, 'Come out of this man, you impure spirit!'",
      "T": "Jesus had been commanding him: 'Come out of this man, you evil spirit!'"
    },
    "9": {
      "L": "And Jesus asked him, 'What is your name?' He replied, 'My name is Legion, for we are many.'",
      "M": "Then Jesus asked him, 'What is your name?' 'My name is Legion,' he replied, 'for we are many.'",
      "T": "Jesus asked him, 'What is your name?' He said, 'My name is Legion—there are thousands of us.'"
    },
    "10": {
      "L": "And he pleaded with him earnestly not to send them out of the region.",
      "M": "And he begged Jesus again and again not to send them out of the area.",
      "T": "He begged Jesus desperately not to send them out of the region."
    },
    "11": {
      "L": "Now there on the hillside a great herd of pigs was feeding,",
      "M": "A large herd of pigs was feeding on the nearby hillside.",
      "T": "A large herd of pigs was grazing on the hillside nearby."
    },
    "12": {
      "L": "and they begged him, saying, 'Send us to the pigs; let us enter them.'",
      "M": "The demons begged Jesus, 'Send us among the pigs; allow us to go into them.'",
      "T": "The demons begged him: 'Send us into the pigs—let us go into them!'"
    },
    "13": {
      "L": "So he gave them permission. And the unclean spirits came out and entered the pigs, and the herd, numbering about two thousand, rushed down the steep bank into the sea and were drowned in the sea.",
      "M": "He gave them permission, and the impure spirits came out and went into the pigs. The herd, about two thousand in number, rushed down the steep bank into the lake and were drowned.",
      "T": "Jesus gave permission. The evil spirits came out and went into the pigs, and the whole herd—about two thousand animals—stampeded down the steep bank into the lake and drowned."
    },
    "14": {
      "L": "The herdsmen fled and told it in the city and in the surrounding region. And they came to see what it was that had happened.",
      "M": "Those tending the pigs ran off and reported this in the town and countryside, and the people went out to see what had happened.",
      "T": "The pig herders ran and told everyone in town and in the countryside. People came out to see what had happened."
    },
    "15": {
      "L": "And they came to Jesus and saw the demon-possessed man, the one who had had the legion, sitting there, clothed and in his right mind, and they were afraid.",
      "M": "When they came to Jesus, they saw the man who had been possessed by the legion of demons, sitting there, dressed and in his right mind; and they were afraid.",
      "T": "When they got to Jesus, they saw the man who had been terrorized by the demon horde—sitting calmly, fully dressed, and completely sane. They were terrified."
    },
    "16": {
      "L": "And those who had seen it described to them what had happened to the demon-possessed man and to the pigs.",
      "M": "Those who had seen it told the people what had happened to the demon-possessed man—and told about the pigs as well.",
      "T": "Those who had seen it told the full story—what had happened to the man and to the pigs."
    },
    "17": {
      "L": "And they began to beg him to depart from their region.",
      "M": "Then the people began to plead with Jesus to leave their region.",
      "T": "Then the people began urging Jesus to leave their area."
    },
    "18": {
      "L": "As he was getting into the boat, the man who had been possessed with demons begged him that he might be with him.",
      "M": "As Jesus was getting into the boat, the man who had been demon-possessed begged to go with him.",
      "T": "As Jesus was climbing into the boat, the man who had been set free begged to go with him."
    },
    "19": {
      "L": "And he did not permit him but said to him, 'Go home to your people and tell them how much the Lord has done for you, and how he has had mercy on you.'",
      "M": "Jesus did not let him, but said, 'Go home to your own people and tell them how much the Lord has done for you, and how he has had mercy on you.'",
      "T": "But Jesus didn't allow it. 'Go back home to your people,' he said, 'and tell them how much the Lord has done for you—how he showed you mercy.'"
    },
    "20": {
      "L": "And he went away and began to proclaim in the Decapolis how much Jesus had done for him, and everyone marveled.",
      "M": "So the man went away and began to tell in the Decapolis how much Jesus had done for him. And all the people were amazed.",
      "T": "The man went away and began announcing throughout the Decapolis everything Jesus had done for him. Everyone was astonished."
    },
    "21": {
      "L": "And when Jesus had crossed again in the boat to the other side, a great crowd gathered to him, and he was beside the sea.",
      "M": "When Jesus had again crossed over by boat to the other side of the lake, a large crowd gathered around him while he was by the lake.",
      "T": "When Jesus crossed back to the other side in the boat, a large crowd gathered around him at the lakeshore."
    },
    "22": {
      "L": "And there came one of the rulers of the synagogue, Jairus by name, and seeing him, he fell at his feet",
      "M": "Then one of the synagogue leaders, named Jairus, came, and when he saw Jesus, he fell at his feet.",
      "T": "Then a synagogue leader named Jairus arrived. When he saw Jesus, he fell at his feet"
    },
    "23": {
      "L": "and implored him earnestly, saying, 'My little daughter is at the point of death. Come and lay your hands on her, so that she may be saved and live.'",
      "M": "and pleaded earnestly with him, 'My little daughter is dying. Please come and put your hands on her so that she will be healed and live.'",
      "T": "and begged him urgently, 'My little daughter is at death's door. Please come and lay your hands on her so she can be healed and live.'"
    },
    "24": {
      "L": "And he went with him. And a great crowd followed him and was pressing around him.",
      "M": "So Jesus went with him. A large crowd followed and pressed around him.",
      "T": "Jesus went with him. A massive crowd followed, pressing in all around him."
    },
    "25": {
      "L": "And a woman who had a discharge of blood for twelve years,",
      "M": "And a woman was there who had been subject to bleeding for twelve years.",
      "T": "In the crowd was a woman who had been suffering from chronic bleeding for twelve years."
    },
    "26": {
      "L": "and who had suffered much under many physicians, and had spent all that she had, and was no better but rather grew worse.",
      "M": "She had suffered a great deal under the care of many doctors and had spent all she had, yet instead of getting better she grew worse.",
      "T": "She had endured much at the hands of many doctors and had spent everything she had on treatment—but instead of improving, she only grew worse."
    },
    "27": {
      "L": "She had heard the reports about Jesus and came up behind him in the crowd and touched his garment,",
      "M": "When she heard about Jesus, she came up behind him in the crowd and touched his cloak,",
      "T": "She had heard about Jesus. She came up from behind in the crowd and touched his cloak,"
    },
    "28": {
      "L": "for she said, 'If I touch even his garments, I will be saved.'",
      "M": "because she thought, 'If I just touch his clothes, I will be healed.'",
      "T": "because she kept thinking, 'If I can just touch his clothes, I'll be healed.'"
    },
    "29": {
      "L": "And immediately the flow of her blood dried up, and she felt in her body that she was healed of her affliction.",
      "M": "Immediately her bleeding stopped and she felt in her body that she was freed from her suffering.",
      "T": "The bleeding stopped at once. She felt it in her body—she was healed of her condition."
    },
    "30": {
      "L": "And Jesus, perceiving in himself that power had gone out from him, immediately turned about in the crowd and said, 'Who touched my garments?'",
      "M": "At once Jesus realized that power had gone out from him. He turned around in the crowd and asked, 'Who touched my clothes?'",
      "T": "At that same moment Jesus was aware that power had gone out of him. He turned around in the crowd and asked, 'Who touched my clothes?'"
    },
    "31": {
      "L": "And his disciples said to him, 'You see the crowd pressing around you, and yet you say, \"Who touched me?\"'",
      "M": "'You see the people crowding against you,' his disciples answered, 'and yet you can ask, \"Who touched me?\"'",
      "T": "His disciples replied, 'Look at this crowd pressing in on you! How can you ask who touched you?'"
    },
    "32": {
      "L": "And he kept looking around to see who had done it.",
      "M": "But Jesus kept looking around to see who had done it.",
      "T": "But Jesus kept looking around to see who had done it."
    },
    "33": {
      "L": "But the woman, knowing what had happened to her, came in fear and trembling and fell down before him and told him the whole truth.",
      "M": "Then the woman, knowing what had happened to her, came and fell at his feet and, trembling with fear, told him the whole truth.",
      "T": "Knowing what had happened to her, the woman came trembling with fear and fell before him. She told him the whole story."
    },
    "34": {
      "L": "And he said to her, 'Daughter, your faith has made you well; go in peace, and be healed of your affliction.'",
      "M": "He said to her, 'Daughter, your faith has healed you. Go in peace and be freed from your suffering.'",
      "T": "He said to her, 'Daughter, your trust in me has healed you. Go in peace—you are free from your suffering.'"
    },
    "35": {
      "L": "While he was still speaking, there came from the ruler of the synagogue's house some who said, 'Your daughter is dead. Why trouble the Teacher any further?'",
      "M": "While Jesus was still speaking, some people came from the house of Jairus, the synagogue leader. 'Your daughter is dead,' they said. 'Why bother the teacher anymore?'",
      "T": "While Jesus was still talking, messengers arrived from Jairus' house. 'Your daughter is dead,' they said. 'Why trouble the Teacher any further?'"
    },
    "36": {
      "L": "But Jesus, overhearing the word that was spoken, said to the ruler of the synagogue, 'Do not fear, only believe.'",
      "M": "Overhearing what they said, Jesus told him, 'Don't be afraid; just believe.'",
      "T": "Jesus overheard the message. 'Don't be afraid,' he told Jairus. 'Just believe.'"
    },
    "37": {
      "L": "And he allowed no one to follow him except Peter and James and John the brother of James.",
      "M": "He did not let anyone follow him except Peter, James and John the brother of James.",
      "T": "He let no one come with him except Peter, James, and John the brother of James."
    },
    "38": {
      "L": "They came to the house of the ruler of the synagogue, and he saw the commotion and people weeping and wailing loudly.",
      "M": "When they came to the home of the synagogue leader, Jesus saw a commotion, with people crying and wailing loudly.",
      "T": "When they arrived at the synagogue leader's house, Jesus saw the commotion—people weeping and wailing loudly."
    },
    "39": {
      "L": "And entering, he said to them, 'Why are you making a commotion and weeping? The child is not dead but sleeping.'",
      "M": "He went in and said to them, 'Why all this commotion and wailing? The child is not dead but asleep.'",
      "T": "He went inside and said, 'Why this uproar and weeping? The child is not dead—she is asleep.'"
    },
    "40": {
      "L": "And they laughed at him. But he put them all outside and took the child's father and mother and those who were with him and went in where the child was.",
      "M": "But they laughed at him. After he put them all out, he took the child's father and mother and the disciples who were with him, and went in where the child was.",
      "T": "They laughed at him. But he sent them all out, took the child's father and mother and his three disciples, and went into the room where the child lay."
    },
    "41": {
      "L": "Taking her by the hand he said to her, 'Talitha koum,' which means, 'Little girl, I say to you, get up.'",
      "M": "He took her by the hand and said to her, 'Talitha koum!' (which means 'Little girl, I say to you, get up!').",
      "T": "He took her by the hand and said to her, 'Talitha koum!'—which means, 'Little girl, get up!'"
    },
    "42": {
      "L": "And immediately the girl got up and began walking, for she was twelve years old. And immediately they were overcome with great amazement.",
      "M": "Immediately the girl stood up and began to walk around (she was twelve years old). At this they were completely astonished.",
      "T": "The girl stood up at once and began walking around—she was twelve years old. They were completely overwhelmed with amazement."
    },
    "43": {
      "L": "And he strictly ordered them that no one should know this, and told them to give her something to eat.",
      "M": "He gave strict orders not to let anyone know about this, and told them to give her something to eat.",
      "T": "He gave them strict orders not to tell anyone what had happened, and said to give her something to eat."
    }
  },
  "6": {
    "1": {
      "L": "He went away from there and came to his hometown, and his disciples followed him.",
      "M": "Jesus left there and went to his hometown, accompanied by his disciples.",
      "T": "Jesus left that place and returned to his hometown, and his disciples followed him."
    },
    "2": {
      "L": "And when the Sabbath came, he began to teach in the synagogue, and many who heard him were astonished, saying, 'Where did this man get these things? What is the wisdom given to him? How are such mighty works done by his hands?'",
      "M": "When the Sabbath came, he began to teach in the synagogue, and many who heard him were amazed. 'Where did this man get these things?' they asked. 'What's this wisdom that has been given him? What are these remarkable miracles he is performing?'",
      "T": "When the Sabbath came, he began teaching in the synagogue. Many who heard him were astonished. 'Where did he get all this?' they asked. 'What's this wisdom he has received? How does he perform such miracles?'"
    },
    "3": {
      "L": "'Is not this the carpenter, the son of Mary and brother of James and Joses and Judas and Simon? And are not his sisters here with us?' And they were taking offense at him.",
      "M": "'Isn't this the carpenter? Isn't this Mary's son and the brother of James, Joseph, Judas and Simon? Aren't his sisters here with us?' And they took offense at him.",
      "T": "'Isn't this the carpenter? Mary's son? The brother of James, Joses, Judas, and Simon? Don't his sisters live here among us?' And they were deeply offended."
    },
    "4": {
      "L": "And Jesus said to them, 'A prophet is not without honor except in his hometown and among his relatives and in his own household.'",
      "M": "Jesus said to them, 'A prophet is not without honor except in his own town, among his relatives and in his own home.'",
      "T": "Jesus told them, 'A prophet is honored everywhere except in his own hometown, among his own relatives, and in his own household.'"
    },
    "5": {
      "L": "And he was not able to do any mighty work there, except that he laid his hands on a few sick people and healed them.",
      "M": "He could not do any miracles there, except lay his hands on a few sick people and heal them.",
      "T": "He was not able to do any miracle there except lay his hands on a few sick people and heal them."
    },
    "6": {
      "L": "And he marveled because of their unbelief. And he went about among the villages teaching.",
      "M": "He was amazed at their lack of faith. Then Jesus went around teaching from village to village.",
      "T": "He was astonished by their unbelief. Then he went on, teaching through the surrounding villages."
    },
    "7": {
      "L": "And he called the twelve and began to send them out two by two, and gave them authority over the unclean spirits.",
      "M": "Calling the Twelve to him, he began to send them out two by two and gave them authority over impure spirits.",
      "T": "He called the Twelve and began sending them out two by two, giving them authority over evil spirits."
    },
    "8": {
      "L": "He charged them to take nothing for their journey except a staff—no bread, no bag, no money in their belts—",
      "M": "These were his instructions: 'Take nothing for the journey except a staff—no bread, no bag, no money in your belts.'",
      "T": "He instructed them to take nothing for the journey except a walking stick—no bread, no pack, no money."
    },
    "9": {
      "L": "but to wear sandals and not to put on two tunics.",
      "M": "'Wear sandals but not an extra shirt.'",
      "T": "'Wear sandals, but don't take an extra shirt.'"
    },
    "10": {
      "L": "And he said to them, 'Whenever you enter a house, remain there until you leave that place.'",
      "M": "'Whenever you enter a house, stay there until you leave that town.'",
      "T": "'Whenever you enter a home, stay there until you move on from that town.'"
    },
    "11": {
      "L": "'And whatever place will not receive you and will not hear you, when you leave there, shake off the dust that is on your feet as a testimony against them.'",
      "M": "'And if any place will not welcome you or listen to you, leave that place and shake the dust off your feet as a testimony against them.'",
      "T": "'If a place refuses to welcome you and won't listen, leave and shake the dust off your feet as a witness against them.'"
    },
    "12": {
      "L": "And they went out and proclaimed that people should repent.",
      "M": "They went out and preached that people should repent.",
      "T": "So they went out and proclaimed that people should turn from their sins."
    },
    "13": {
      "L": "And they cast out many demons and anointed with oil many who were sick and healed them.",
      "M": "They drove out many demons and anointed many sick people with oil and healed them.",
      "T": "They drove out many evil spirits and anointed many sick people with oil and healed them."
    },
    "14": {
      "L": "King Herod heard of it, for his name had become known. And he was saying, 'John the Baptist has been raised from the dead; that is why miraculous powers are at work in him.'",
      "M": "King Herod heard about this, for Jesus' name had become well known. Some were saying, 'John the Baptist has been raised from the dead, and that is why miraculous powers are at work in him.'",
      "T": "King Herod heard about this, for Jesus' name had become widely known. Some were saying, 'John the Baptist has been raised from the dead—that's why these miraculous powers are working through him.'"
    },
    "15": {
      "L": "But others said, 'He is Elijah.' And others said, 'He is a prophet, like one of the prophets.'",
      "M": "Others said, 'He is Elijah.' And still others claimed, 'He is a prophet, like one of the prophets of long ago.'",
      "T": "Others said, 'He is Elijah.' Still others said, 'He is a prophet—like one of the ancient prophets.'"
    },
    "16": {
      "L": "But when Herod heard of it, he said, 'John, whom I beheaded, has been raised from the dead.'",
      "M": "But when Herod heard this, he said, 'John, whom I beheaded, has been raised from the dead!'",
      "T": "But Herod, hearing this, said, 'It is John—the man I had beheaded. He has risen from the dead!'"
    },
    "17": {
      "L": "For Herod himself had sent and seized John and bound him in prison, on account of Herodias, the wife of Philip his brother, because he had married her.",
      "M": "For Herod himself had given orders to have John arrested, and he had him bound and put in prison. He did this because of Herodias, his brother Philip's wife, whom he had married.",
      "T": "For Herod had sent soldiers to arrest John and had him bound and put in prison, all because of Herodias, his brother Philip's wife—Herod had married her."
    },
    "18": {
      "L": "For John had been saying to Herod, 'It is not lawful for you to have your brother's wife.'",
      "M": "For John had been saying to Herod, 'It is not lawful for you to have your brother's wife.'",
      "T": "John had repeatedly told Herod, 'It is against God's law for you to have your brother's wife.'"
    },
    "19": {
      "L": "So Herodias bore a grudge against him and wanted to kill him. But she could not,",
      "M": "So Herodias nursed a grudge against John and wanted to kill him. But she was not able to,",
      "T": "Herodias held a deep grudge against John and wanted to kill him, but she couldn't—"
    },
    "20": {
      "L": "for Herod feared John, knowing that he was a righteous and holy man, and he kept him safe. When he heard him, he was greatly troubled, and yet he heard him gladly.",
      "M": "because Herod feared John and protected him, knowing him to be a righteous and holy man. When Herod heard John, he was greatly puzzled; yet he liked to listen to him.",
      "T": "because Herod stood in awe of John. He knew him to be a righteous and holy man, and he kept him under his protection. Whenever he heard John speak, he was deeply unsettled—yet he kept listening to him eagerly."
    },
    "21": {
      "L": "But an opportunity came when Herod on his birthday gave a banquet for his nobles and military commanders and the leading men of Galilee.",
      "M": "Finally the opportune time came. On his birthday Herod gave a banquet for his high officials and military commanders and the leading men of Galilee.",
      "T": "An opportunity finally came on Herod's birthday, when he hosted a lavish dinner for his officials, military commanders, and the leading men of Galilee."
    },
    "22": {
      "L": "And when the daughter of Herodias came in and danced, she pleased Herod and his guests. The king said to the girl, 'Ask me for whatever you wish, and I will give it to you.'",
      "M": "When the daughter of Herodias came in and danced, she pleased Herod and his dinner guests. The king said to the girl, 'Ask me for anything you want, and I'll give it to you.'",
      "T": "When Herodias' daughter came in and danced, she delighted Herod and his guests. The king said to the girl, 'Ask me for anything you want—I'll give it to you.'"
    },
    "23": {
      "L": "And he vowed to her, 'Whatever you ask me, I will give you, up to half of my kingdom.'",
      "M": "And he promised her with an oath, 'Whatever you ask I will give you, up to half my kingdom.'",
      "T": "He swore an oath: 'Whatever you ask, I'll give it—even up to half my kingdom!'"
    },
    "24": {
      "L": "And she went out and said to her mother, 'For what should I ask?' And she said, 'The head of John the Baptist.'",
      "M": "She went out and said to her mother, 'What shall I ask for?' 'The head of John the Baptist,' she answered.",
      "T": "She went out and asked her mother, 'What should I ask for?' Her mother answered, 'The head of John the Baptist.'"
    },
    "25": {
      "L": "And she came in immediately with haste to the king and asked, saying, 'I want you to give me at once the head of John the Baptist on a platter.'",
      "M": "At once the girl hurried in to the king with the request: 'I want you to give me right now the head of John the Baptist on a dish.'",
      "T": "She rushed straight back to the king and demanded, 'I want you to give me, right now, the head of John the Baptist on a serving dish.'"
    },
    "26": {
      "L": "And the king was exceedingly sorry, but because of his oath and those reclining with him, he did not want to refuse her.",
      "M": "The king was greatly distressed, but because of his oaths and his dinner guests, he did not want to refuse her.",
      "T": "The king was deeply sorry, but because of his oath and his guests, he didn't want to refuse her."
    },
    "27": {
      "L": "And immediately the king sent a soldier of the guard with orders to bring John's head. He went and beheaded him in the prison",
      "M": "So he immediately sent an executioner with orders to bring John's head. The man went, beheaded John in the prison,",
      "T": "The king immediately sent a soldier with orders to bring John's head. The soldier went and beheaded him in the prison."
    },
    "28": {
      "L": "and brought his head on a platter and gave it to the girl, and the girl gave it to her mother.",
      "M": "and brought back his head on a dish. He presented it to the girl, and she gave it to her mother.",
      "T": "He brought the head back on a dish and gave it to the girl, and she gave it to her mother."
    },
    "29": {
      "L": "When his disciples heard of it, they came and took his body and laid it in a tomb.",
      "M": "On hearing of this, John's disciples came and took his body and laid it in a tomb.",
      "T": "When John's disciples heard what had happened, they came and took his body and laid it in a tomb."
    },
    "30": {
      "L": "The apostles gathered together with Jesus and reported to him all that they had done and taught.",
      "M": "The apostles gathered around Jesus and reported to him all they had done and taught.",
      "T": "The apostles regrouped with Jesus and gave him a full report of everything they had done and taught."
    },
    "31": {
      "L": "And he said to them, 'Come away by yourselves to a desolate place and rest a while.' For many were coming and going, and they had no leisure even to eat.",
      "M": "Then, because so many people were coming and going that they did not even have a chance to eat, he said to them, 'Come with me by yourselves to a quiet place and get some rest.'",
      "T": "Because so many people were coming and going that they didn't even have time to eat, Jesus said to them, 'Come away with me to a quiet place and rest for a while.'"
    },
    "32": {
      "L": "And they went away in the boat to a desolate place by themselves.",
      "M": "So they went away by themselves in a boat to a solitary place.",
      "T": "So they went off in the boat to a remote place by themselves."
    },
    "33": {
      "L": "Now many saw them going and recognized them, and they ran there on foot from all the towns and arrived there ahead of them.",
      "M": "But many who saw them leaving recognized them and ran on foot from all the towns and got there ahead of them.",
      "T": "But many people saw them leaving and recognized them. They ran on foot from all the surrounding towns and arrived before Jesus' boat did."
    },
    "34": {
      "L": "When he went ashore he saw a great crowd, and he had compassion on them, because they were like sheep without a shepherd. And he began to teach them many things.",
      "M": "When Jesus landed and saw a large crowd, he had compassion on them, because they were like sheep without a shepherd. So he began teaching them many things.",
      "T": "When Jesus stepped ashore and saw the massive crowd, his heart was moved with compassion for them, because they were like sheep without a shepherd. And he began to teach them at length."
    },
    "35": {
      "L": "And when the hour was already late, his disciples came to him and said, 'This is a desolate place, and the hour is already late.'",
      "M": "By this time it was late in the day, so his disciples came to him. 'This is a remote place,' they said, 'and it's already very late.'",
      "T": "By late afternoon his disciples came to him: 'This place is remote and it's getting late.'"
    },
    "36": {
      "L": "'Send them away to go into the surrounding countryside and villages to buy themselves something to eat.'",
      "M": "'Send the people away so that they can go to the surrounding countryside and villages and buy themselves something to eat.'",
      "T": "'Send the crowd away so they can go to the nearby farms and villages and buy themselves some food.'"
    },
    "37": {
      "L": "But he answered them, 'You give them something to eat.' And they said to him, 'Shall we go and buy two hundred denarii worth of bread and give it to them to eat?'",
      "M": "'You give them something to eat,' he said. They replied, 'That would take more than half a year's wages! Are we to go and spend that much on bread and give it to them to eat?'",
      "T": "But he said to them, 'You give them something to eat.' They answered, 'Should we go and spend eight months' wages on bread and feed all these people?'"
    },
    "38": {
      "L": "'How many loaves do you have?' he asked. 'Go and see.' And when they had found out, they said, 'Five, and two fish.'",
      "M": "'How many loaves do you have?' he asked. 'Go and see.' When they found out, they said, 'Five—and two fish.'",
      "T": "'Go look,' he said. 'How many loaves do you have?' They checked and came back: 'Five—and two fish.'"
    },
    "39": {
      "L": "Then he commanded them all to sit down in groups on the green grass.",
      "M": "Then Jesus directed them to have all the people sit down in groups on the green grass.",
      "T": "He ordered them to have everyone sit down in groups on the green grass."
    },
    "40": {
      "L": "So they sat down in groups, by hundreds and by fifties.",
      "M": "So they sat down in groups of hundreds and fifties.",
      "T": "They sat down in groups of hundreds and fifties."
    },
    "41": {
      "L": "And taking the five loaves and the two fish, he looked up to heaven and blessed and broke the loaves and gave them to the disciples to set before the people. And he divided the two fish among them all.",
      "M": "Taking the five loaves and the two fish and looking up to heaven, he gave thanks and broke the loaves. Then he gave them to his disciples to distribute to the people. He also divided the two fish among them all.",
      "T": "He took the five loaves and the two fish, looked up to heaven, gave thanks, broke the loaves, and handed them to his disciples to distribute. He also divided the two fish among everyone."
    },
    "42": {
      "L": "And they all ate and were satisfied.",
      "M": "They all ate and were satisfied,",
      "T": "Everyone ate until they were full."
    },
    "43": {
      "L": "And they took up twelve basketfuls of broken pieces and of the fish.",
      "M": "and the disciples picked up twelve basketfuls of broken pieces of bread and fish.",
      "T": "Afterward, they gathered twelve baskets full of leftover pieces of bread and fish."
    },
    "44": {
      "L": "And those who ate the loaves were five thousand men.",
      "M": "The number of the men who had eaten was five thousand.",
      "T": "The number of men who ate was five thousand."
    },
    "45": {
      "L": "And immediately he compelled his disciples to get into the boat and go ahead to the other side, to Bethsaida, while he himself dismissed the crowd.",
      "M": "Immediately Jesus made his disciples get into the boat and go on ahead of him to Bethsaida, while he dismissed the crowd.",
      "T": "Right away Jesus made his disciples get into the boat and head to the other side toward Bethsaida, while he stayed behind to dismiss the crowd."
    },
    "46": {
      "L": "And after he had taken leave of them, he went up on the mountain to pray.",
      "M": "After leaving them, he went up on a mountainside to pray.",
      "T": "After saying goodbye to them, he went up the hillside to pray."
    },
    "47": {
      "L": "And when evening came, the boat was in the middle of the sea, and he was alone on the land.",
      "M": "Later that night, the boat was in the middle of the lake, and he was alone on land.",
      "T": "When evening came, the boat was far out on the water, and he was alone on the shore."
    },
    "48": {
      "L": "And seeing them straining at the oars, for the wind was against them, about the fourth watch of the night he came to them, walking on the sea. He meant to pass by them,",
      "M": "He saw the disciples straining at the oars, because the wind was against them. Shortly before dawn he went out to them, walking on the lake. He was about to pass by them,",
      "T": "He could see them straining at the oars, fighting a headwind. About three in the morning he came toward them, walking on the water. He was about to pass them by,"
    },
    "49": {
      "L": "but when they saw him walking on the sea they thought it was a ghost, and cried out;",
      "M": "but when they saw him walking on the lake, they thought he was a ghost. They cried out,",
      "T": "but when they saw him walking on the water they thought he was a ghost and screamed."
    },
    "50": {
      "L": "for they all saw him and were terrified. But immediately he spoke with them and said to them, 'Take heart; it is I. Do not be afraid.'",
      "M": "because they all saw him and were terrified. Immediately he spoke to them and said, 'Take courage! It is I. Don't be afraid.'",
      "T": "They all saw him and were terrified. But at once he spoke to them: 'Take heart—it is I. Don't be afraid.'"
    },
    "51": {
      "L": "And he got into the boat with them, and the wind ceased. And they were utterly astounded,",
      "M": "Then he climbed into the boat with them, and the wind died down. They were completely amazed,",
      "T": "He climbed into the boat with them, and the wind dropped. They were completely overwhelmed with shock,"
    },
    "52": {
      "L": "for they did not understand about the loaves, but their hearts were hardened.",
      "M": "for they had not understood about the loaves; their hearts were hardened.",
      "T": "because they had not grasped the significance of the loaves—their hearts were closed."
    },
    "53": {
      "L": "When they had crossed over, they came to land at Gennesaret and moored to the shore.",
      "M": "When they had crossed over, they landed at Gennesaret and anchored there.",
      "T": "After crossing the lake, they landed at Gennesaret and tied up the boat."
    },
    "54": {
      "L": "And when they got out of the boat, immediately the people recognized him",
      "M": "As soon as they got out of the boat, people recognized Jesus.",
      "T": "As soon as they stepped out of the boat, the people recognized Jesus."
    },
    "55": {
      "L": "and ran about the whole region and began to bring the sick on their mats to wherever they heard he was.",
      "M": "They ran throughout that whole region and carried the sick on mats to wherever they heard he was.",
      "T": "They ran throughout the whole region and brought the sick on mats to wherever they heard he was."
    },
    "56": {
      "L": "And wherever he went, into villages or cities or farms, they laid the sick in the marketplaces and begged him that they might touch even the fringe of his garment. And as many as touched it were made well.",
      "M": "And wherever he went—into villages, towns or countryside—they placed the sick in the marketplaces. They begged him to let them touch even the edge of his cloak, and all who touched it were healed.",
      "T": "Everywhere he went—villages, towns, or farms—they brought the sick to the marketplaces and begged him to let them touch even the fringe of his cloak. And all who touched it were healed."
    }
  },
  "7": {
    "1": {
      "L": "Now the Pharisees gathered to him, along with some of the scribes who had come from Jerusalem.",
      "M": "The Pharisees and some of the teachers of the law who had come from Jerusalem gathered around Jesus",
      "T": "The Pharisees and some Bible teachers who had come down from Jerusalem gathered around Jesus."
    },
    "2": {
      "L": "And they saw that some of his disciples ate their bread with defiled, that is, unwashed hands.",
      "M": "and saw some of his disciples eating food with hands that were defiled, that is, unwashed.",
      "T": "They noticed that some of his disciples were eating with ritually unwashed—that is, unclean—hands."
    },
    "3": {
      "L": "(For the Pharisees and all the Jews do not eat unless they wash their hands carefully, holding to the tradition of the elders,",
      "M": "(The Pharisees and all the Jews do not eat unless they give their hands a ceremonial washing, holding to the tradition of the elders.",
      "T": "(The Pharisees and all Jews never eat without first performing the ritual hand washing—following the tradition of the elders."
    },
    "4": {
      "L": "And when they come from the marketplace, they do not eat unless they wash. And there are many other things that they have received and hold to: the washing of cups and pots and copper vessels and dining couches.)",
      "M": "When they come from the marketplace they do not eat unless they wash. And they observe many other traditions, such as the washing of cups, pitchers and kettles.)",
      "T": "When they return from the marketplace, they do not eat without first washing. And they follow many other traditions: the ritual washing of cups, jugs, and copper bowls.)"
    },
    "5": {
      "L": "And the Pharisees and the scribes asked him, 'Why do your disciples not walk according to the tradition of the elders, but eat with defiled hands?'",
      "M": "So the Pharisees and teachers of the law asked Jesus, 'Why don't your disciples live according to the tradition of the elders instead of eating their food with defiled hands?'",
      "T": "So the Pharisees and the Bible teachers asked him, 'Why don't your disciples follow the tradition of the elders? They eat with ritually unclean hands!'"
    },
    "6": {
      "L": "And he said to them, 'Well did Isaiah prophesy of you hypocrites, as it is written, \"This people honors me with their lips, but their heart is far from me;'",
      "M": "He replied, 'Isaiah was right when he prophesied about you hypocrites; as it is written: \"These people honor me with their lips, but their hearts are far from me.'",
      "T": "He replied, 'Isaiah described you hypocrites precisely. As it is written: \"This people honors me with their lips, but their hearts are far away from me.'"
    },
    "7": {
      "L": "'\"In vain do they worship me, teaching as doctrines the commandments of men.\"'",
      "M": "'\"Their worship of me is in vain; their teachings are merely human rules.\"'",
      "T": "'\"Their worship is empty—they teach human rules as if they were God's commands.\"'"
    },
    "8": {
      "L": "'You leave the commandment of God and hold to the tradition of men.'",
      "M": "'You have let go of the commands of God and are holding on to human traditions.'",
      "T": "'You abandon God's commands while clinging to human tradition.'"
    },
    "9": {
      "L": "And he said to them, 'You have a fine way of setting aside the commandment of God in order to establish your tradition!'",
      "M": "And he continued, 'You have a fine way of setting aside the commands of God in order to observe your own traditions!'",
      "T": "'You're experts at setting aside God's commandment so you can uphold your own traditions!'"
    },
    "10": {
      "L": "'For Moses said, \"Honor your father and your mother,\" and, \"Whoever speaks evil of father or mother, let him certainly die.\"'",
      "M": "'For Moses said, \"Honor your father and mother,\" and, \"Anyone who curses their father or mother is to be put to death.\"'",
      "T": "'Moses commanded: \"Honor your father and your mother,\" and: \"Anyone who curses father or mother is to be put to death.\"'"
    },
    "11": {
      "L": "'But you say, \"If a man says to his father or his mother, 'Whatever support you would have received from me is Corban' (that is, given to God)—'",
      "M": "'But you say that if anyone declares that what might have been used to help their father or mother is Corban (that is, devoted to God)—'",
      "T": "'But you teach that if a man says to his parents, \"Whatever help you might have received from me is Corban\"—meaning it belongs to God—'"
    },
    "12": {
      "L": "'then you no longer permit him to do anything for his father or mother,'",
      "M": "'then you no longer let them do anything for their father or mother.'",
      "T": "'—then you let him off from doing anything for his father or mother.'"
    },
    "13": {
      "L": "'thus making void the word of God through your tradition that you have handed down. And many such things you do.'",
      "M": "'Thus you nullify the word of God by your tradition that you have handed down. And you do many things like that.'",
      "T": "'In this way you cancel God's word through the tradition you have inherited. And you do many other things just like this.'"
    },
    "14": {
      "L": "And calling the crowd to him again, he said to them, 'Hear me, all of you, and understand:'",
      "M": "Again Jesus called the crowd to him and said, 'Listen to me, everyone, and understand this.'",
      "T": "He called the crowd to him again and said, 'Listen to me, all of you, and understand what I'm saying:'"
    },
    "15": {
      "L": "'There is nothing outside a person that by entering him is able to defile him; but the things that come out of a person are what defile him.'",
      "M": "'Nothing outside a person can defile them by going into them. Rather, it is what comes out of a person that defiles them.'",
      "T": "'Nothing that enters a person from outside can make them unclean. It is what comes out of a person that makes them unclean.'"
    },
    "17": {
      "L": "And when he had entered the house and left the crowd, his disciples asked him about the parable.",
      "M": "After he had left the crowd and entered the house, his disciples asked him about this parable.",
      "T": "When he had left the crowd and entered the house, his disciples asked him to explain the parable."
    },
    "18": {
      "L": "And he said to them, 'Then are you also without understanding? Do you not perceive that whatever enters into a person from outside cannot defile him,'",
      "M": "'Are you so dull?' he asked. 'Don't you see that nothing that enters a person from the outside can defile them?'",
      "T": "'So you're still not getting it?' he said. 'Don't you see that nothing that goes into a person from outside can make them unclean?'"
    },
    "19": {
      "L": "'since it enters not his heart but his stomach, and is expelled?' (Thus he declared all foods clean.)",
      "M": "'For it doesn't go into their heart but into their stomach, and then out of the body.' (In saying this, Jesus declared all foods clean.)",
      "T": "'It goes into the stomach, not the heart—and then out of the body.' (In saying this, Jesus declared all foods clean.)"
    },
    "20": {
      "L": "And he said, 'What comes out of a person is what defiles him.'",
      "M": "He went on: 'What comes out of a person is what defiles them.'",
      "T": "He continued: 'It is what comes out of a person that makes them unclean.'"
    },
    "21": {
      "L": "'For from within, out of the heart of man, come evil thoughts, sexual immorality, theft, murder, adultery,'",
      "M": "'For it is from within, out of a person's heart, that evil thoughts come—sexual immorality, theft, murder, adultery,'",
      "T": "'From within—from the human heart—come evil thoughts: sexual immorality, theft, murder, adultery,'"
    },
    "22": {
      "L": "'coveting, wickedness, deceit, sensuality, envy, slander, pride, foolishness.'",
      "M": "'greed, malice, deceit, lewdness, envy, slander, arrogance and folly.'",
      "T": "'greed, evil, deception, lustful behavior, envy, slander, arrogance, and foolishness.'"
    },
    "23": {
      "L": "'All these evil things come from within, and they defile a person.'",
      "M": "'All these evils come from inside and defile a person.'",
      "T": "'All these evil things come from inside and make a person unclean.'"
    },
    "24": {
      "L": "And from there he arose and went into the region of Tyre. And he entered a house and did not want anyone to know, yet he was not able to be hidden.",
      "M": "Jesus left that place and went to the vicinity of Tyre. He entered a house and did not want anyone to know it; yet he could not keep his presence secret.",
      "T": "He left that region and went to the area around Tyre. He entered a house, wanting to keep his presence quiet—but he couldn't stay hidden."
    },
    "25": {
      "L": "But immediately a woman whose little daughter had an unclean spirit heard of him and came and fell down at his feet.",
      "M": "In fact, as soon as she heard about him, a woman whose little daughter was possessed by an impure spirit came and fell at his feet.",
      "T": "A woman who had heard about him came right away and fell at his feet. Her little daughter was controlled by an evil spirit."
    },
    "26": {
      "L": "Now the woman was a Gentile, a Syrophoenician by birth. And she was asking him to cast the demon out of her daughter.",
      "M": "The woman was a Greek, born in Syrian Phoenicia. She begged Jesus to drive the demon out of her daughter.",
      "T": "The woman was a Greek—a Syrophoenician by ethnicity. She kept pleading with him to drive the demon out of her daughter."
    },
    "27": {
      "L": "And he said to her, 'Let the children be fed first, for it is not right to take the children's bread and throw it to the dogs.'",
      "M": "'First let the children eat all they want,' he told her, 'for it is not right to take the children's bread and toss it to the dogs.'",
      "T": "'Let the children eat first,' he said. 'It isn't right to take the children's food and throw it to the dogs.'"
    },
    "28": {
      "L": "But she answered him, 'Yes, Lord; yet even the dogs under the table eat the children's crumbs.'",
      "M": "'Lord,' she replied, 'even the dogs under the table eat the children's crumbs.'",
      "T": "'Lord,' she replied, 'but even the dogs under the table eat the children's fallen crumbs.'"
    },
    "29": {
      "L": "And he said to her, 'Because of this saying, go; the demon has left your daughter.'",
      "M": "Then he told her, 'For such a reply, you may go; the demon has left your daughter.'",
      "T": "He said to her, 'Because of that answer, you may go. The demon has left your daughter.'"
    },
    "30": {
      "L": "And she went away to her home and found the child lying in bed and the demon gone.",
      "M": "She went home and found her child lying on the bed, and the demon gone.",
      "T": "She returned home and found her daughter lying peacefully in bed—the demon had left."
    },
    "31": {
      "L": "Then he returned from the region of Tyre and went through Sidon to the Sea of Galilee, through the region of the Decapolis.",
      "M": "Then Jesus left the vicinity of Tyre and went through Sidon, down to the Sea of Galilee and into the region of the Decapolis.",
      "T": "Jesus then left the area around Tyre and traveled through Sidon, down to the Sea of Galilee through the region of the Decapolis."
    },
    "32": {
      "L": "And they brought to him a man who was deaf and had a speech impediment, and they begged him to lay his hand on him.",
      "M": "There some people brought to him a man who was deaf and could hardly talk, and they begged Jesus to place his hand on him.",
      "T": "People brought him a man who was deaf and could barely speak, and they begged Jesus to lay his hand on him."
    },
    "33": {
      "L": "And taking him aside from the crowd privately, he put his fingers into his ears, and after spitting touched his tongue.",
      "M": "After he took him aside, away from the crowd, Jesus put his fingers into the man's ears. Then he spit and touched the man's tongue.",
      "T": "Jesus took him away from the crowd privately. He put his fingers in the man's ears, then spat and touched the man's tongue."
    },
    "34": {
      "L": "And looking up to heaven, he sighed deeply and said to him, 'Ephphatha,' that is, 'Be opened.'",
      "M": "He looked up to heaven and with a deep sigh said to him, 'Ephphatha!' (which means 'Be opened!').",
      "T": "He looked up to heaven, let out a deep sigh, and said, 'Ephphatha!'—which means, 'Open up!'"
    },
    "35": {
      "L": "And his ears were opened, his tongue was released, and he spoke plainly.",
      "M": "At this, the man's ears were opened, his tongue was loosened and he began to speak plainly.",
      "T": "At that moment his ears opened, his tongue was freed, and he began to speak clearly."
    },
    "36": {
      "L": "And Jesus charged them to tell no one. But the more he charged them, the more zealously they proclaimed it.",
      "M": "Jesus commanded them not to tell anyone. But the more he did so, the more they kept talking about it.",
      "T": "Jesus ordered them to tell no one. But the more strictly he charged them, the more they spread the news."
    },
    "37": {
      "L": "And they were astonished beyond measure, saying, 'He has done all things well. He even makes the deaf hear and the mute speak.'",
      "M": "People were overwhelmed with amazement. 'He has done everything well,' they said. 'He even makes the deaf hear and the mute speak.'",
      "T": "The people were beyond themselves with amazement. 'Everything he does is perfect!' they kept saying. 'He even makes the deaf hear and the speechless speak!'"
    }
  },
  "8": {
    "1": {
      "L": "In those days, when again a great crowd had gathered, and they had nothing to eat, he called his disciples to him and said to them,",
      "M": "During those days another large crowd gathered. Since they had nothing to eat, Jesus called his disciples to him and said,",
      "T": "Around that time, another large crowd had gathered and they had nothing to eat. Jesus called his disciples and said to them,"
    },
    "2": {
      "L": "'I have compassion on the crowd, because they have been with me now three days and have nothing to eat.'",
      "M": "'I have compassion for these people; they have already been with me three days and have nothing to eat.'",
      "T": "'My heart goes out to this crowd—they've been with me three days now and have nothing to eat.'"
    },
    "3": {
      "L": "'And if I send them away hungry to their homes, they will faint on the way. And some of them have come from far away.'",
      "M": "'If I send them home hungry, they will collapse on the way, because some of them have come a long distance.'",
      "T": "'If I send them home hungry, they'll collapse on the way—some of them have come from a great distance.'"
    },
    "4": {
      "L": "And his disciples answered him, 'How can one feed these people with bread here in this desolate place?'",
      "M": "His disciples answered, 'But where in this remote place can anyone get enough bread to feed them?'",
      "T": "His disciples answered, 'Where in this remote place would anyone find enough bread to feed all these people?'"
    },
    "5": {
      "L": "'How many loaves do you have?' he asked them. They said, 'Seven.'",
      "M": "'How many loaves do you have?' Jesus asked. 'Seven,' they replied.",
      "T": "'How many loaves do you have?' he asked. 'Seven,' they answered."
    },
    "6": {
      "L": "And he commanded the crowd to sit down on the ground. And taking the seven loaves, he gave thanks and broke them and gave them to his disciples to set before the people; and they set them before the crowd.",
      "M": "He told the crowd to sit down on the ground. When he had taken the seven loaves and given thanks, he broke them and gave them to his disciples to distribute to the people, and they did so.",
      "T": "He ordered the crowd to sit on the ground. Then he took the seven loaves, gave thanks, broke them, and gave them to his disciples to distribute. They passed them out to the crowd."
    },
    "7": {
      "L": "And they had a few small fish. And having blessed them, he commanded that these also should be set before them.",
      "M": "They had a few small fish as well; he gave thanks for them also and told the disciples to distribute them.",
      "T": "They also had a few small fish. He gave thanks for these too and told the disciples to hand them out."
    },
    "8": {
      "L": "And they ate and were satisfied. And they took up the broken pieces left over, seven basketfuls.",
      "M": "The people ate and were satisfied. Afterward the disciples picked up seven basketfuls of broken pieces that were left over.",
      "T": "Everyone ate until they were full. The disciples gathered the leftover pieces—seven large baskets full."
    },
    "9": {
      "L": "And there were about four thousand people. And he sent them away.",
      "M": "About four thousand were present. After he had sent them away,",
      "T": "There were about four thousand people. Jesus sent them home."
    },
    "10": {
      "L": "And immediately getting into the boat with his disciples, he went to the district of Dalmanutha.",
      "M": "he got into the boat with his disciples and went to the region of Dalmanutha.",
      "T": "He got into the boat with his disciples and crossed to the region of Dalmanutha."
    },
    "11": {
      "L": "The Pharisees came and began to argue with him, seeking from him a sign from heaven to test him.",
      "M": "The Pharisees came and began to question Jesus. To test him, they asked him for a sign from heaven.",
      "T": "The Pharisees arrived and began arguing with him. Trying to trap him, they asked for a miraculous sign from heaven."
    },
    "12": {
      "L": "And sighing deeply in his spirit, he said, 'Why does this generation seek a sign? Truly I say to you, no sign will be given to this generation.'",
      "M": "He sighed deeply and said, 'Why does this generation ask for a sign? Truly I tell you, no sign will be given to it.'",
      "T": "With a deep groan he said, 'Why does this generation demand a miraculous sign? I tell you the truth—no sign will be given to this generation.'"
    },
    "13": {
      "L": "And leaving them, he again embarked and went to the other side.",
      "M": "Then he left them, got back into the boat and crossed to the other side.",
      "T": "He left them, got back in the boat, and crossed to the other side."
    },
    "14": {
      "L": "Now they had forgotten to bring bread, and they had only one loaf with them in the boat.",
      "M": "The disciples had forgotten to bring bread, except for one loaf they had with them in the boat.",
      "T": "The disciples had forgotten to bring bread—they only had one loaf with them in the boat."
    },
    "15": {
      "L": "And he cautioned them, saying, 'Watch out; beware of the leaven of the Pharisees and the leaven of Herod.'",
      "M": "'Be careful,' Jesus warned them. 'Watch out for the yeast of the Pharisees and that of Herod.'",
      "T": "'Be on your guard,' Jesus warned them. 'Watch out for the yeast of the Pharisees and the yeast of Herod.'"
    },
    "16": {
      "L": "And they were discussing with one another the fact that they had no bread.",
      "M": "They discussed this with one another and said, 'It is because we have no bread.'",
      "T": "They started talking among themselves: 'It must be because we have no bread.'"
    },
    "17": {
      "L": "And Jesus, aware of this, said to them, 'Why are you discussing the fact that you have no bread? Do you not yet perceive or understand? Have your hearts been hardened?'",
      "M": "Aware of their discussion, Jesus asked them: 'Why are you talking about having no bread? Do you still not see or understand? Are your hearts hardened?'",
      "T": "Knowing what they were discussing, Jesus said, 'Why are you talking about not having bread? Don't you see yet? Don't you understand? Are your hearts that closed?'"
    },
    "18": {
      "L": "'Having eyes, do you not see? And having ears, do you not hear? And do you not remember?'",
      "M": "'Do you have eyes but fail to see, and ears but fail to hear? And don't you remember?'",
      "T": "'You have eyes—can't you see? You have ears—can't you hear? Have you no memory?'"
    },
    "19": {
      "L": "'When I broke the five loaves for the five thousand, how many basketfuls of broken pieces did you take up?' They said to him, 'Twelve.'",
      "M": "'When I broke the five loaves for the five thousand, how many basketfuls of pieces did you pick up?' 'Twelve,' they replied.",
      "T": "'When I broke five loaves for five thousand people, how many baskets of pieces did you collect?' 'Twelve,' they said."
    },
    "20": {
      "L": "'And the seven for the four thousand, how many basketfuls of broken pieces did you take up?' And they said to him, 'Seven.'",
      "M": "'And when I broke the seven loaves for the four thousand, how many basketfuls of pieces did you pick up?' They answered, 'Seven.'",
      "T": "'And when I broke seven loaves for four thousand, how many baskets did you collect?' 'Seven,' they answered."
    },
    "21": {
      "L": "And he said to them, 'Do you not yet understand?'",
      "M": "He said to them, 'Do you still not understand?'",
      "T": "He said to them, 'And you still don't understand?'"
    },
    "22": {
      "L": "And they came to Bethsaida. And they brought to him a blind man and begged him to touch him.",
      "M": "They came to Bethsaida, and some people brought a blind man and begged Jesus to touch him.",
      "T": "They came to Bethsaida. Some people brought a blind man to Jesus and begged him to touch the man."
    },
    "23": {
      "L": "And taking the blind man by the hand, he led him out of the village, and when he had spit on his eyes and laid his hands on him, he asked him, 'Do you see anything?'",
      "M": "He took the blind man by the hand and led him outside the village. When he had spit on the man's eyes and put his hands on him, Jesus asked, 'Do you see anything?'",
      "T": "Jesus took the man by the hand and led him outside the village. He spit on the man's eyes, laid his hands on him, and asked, 'Can you see anything?'"
    },
    "24": {
      "L": "And he looked up and said, 'I see people, but they look like trees, walking.'",
      "M": "He looked up and said, 'I can see people; they look like trees walking around.'",
      "T": "The man looked up and said, 'I can see people—but they look like trees, moving around.'"
    },
    "25": {
      "L": "Then again he laid his hands on his eyes; and he opened his eyes, his sight was restored, and he saw everything clearly.",
      "M": "Once more Jesus put his hands on the man's eyes. Then his eyes were opened, his sight was restored, and he saw everything clearly.",
      "T": "Jesus put his hands on the man's eyes again. This time the man's sight was fully restored—he could see everything clearly."
    },
    "26": {
      "L": "And he sent him home, saying, 'Do not even enter the village.'",
      "M": "Jesus sent him home, saying, 'Don't even go into the village.'",
      "T": "Jesus sent him home with a warning: 'Don't even go into the village.'"
    },
    "27": {
      "L": "And Jesus went on with his disciples to the villages of Caesarea Philippi. And on the way he asked his disciples, 'Who do people say that I am?'",
      "M": "Jesus and his disciples went on to the villages around Caesarea Philippi. On the way he asked them, 'Who do people say I am?'",
      "T": "Jesus and his disciples traveled to the villages around Caesarea Philippi. On the way he asked them, 'Who do people say I am?'"
    },
    "28": {
      "L": "And they told him, 'John the Baptist; and others say, Elijah; and others, one of the prophets.'",
      "M": "They replied, 'Some say John the Baptist; others say Elijah; and still others, one of the prophets.'",
      "T": "They answered, 'Some say John the Baptist, others Elijah, others say you're one of the ancient prophets.'"
    },
    "29": {
      "L": "And he asked them, 'But who do you say that I am?' Peter answered him, 'You are the Christ.'",
      "M": "'But what about you?' he asked. 'Who do you say I am?' Peter answered, 'You are the Messiah.'",
      "T": "'But what about you?' he pressed. 'Who do you say I am?' Peter answered, 'You are the Messiah.'"
    },
    "30": {
      "L": "And he strictly charged them to tell no one about him.",
      "M": "Jesus warned them not to tell anyone about him.",
      "T": "Jesus gave them strict orders to tell no one about him."
    },
    "31": {
      "L": "And he began to teach them that the Son of Man must suffer many things and be rejected by the elders and the chief priests and the scribes and be killed, and after three days rise again.",
      "M": "He then began to teach them that the Son of Man must suffer many things and be rejected by the elders, the chief priests and the teachers of the law, and that he must be killed and after three days rise again.",
      "T": "He began to teach them openly: the Son of Man must go through great suffering, be rejected by the elders, the chief priests, and the Bible teachers, be killed—and after three days, rise again."
    },
    "32": {
      "L": "And he was saying this openly. And Peter took him aside and began to rebuke him.",
      "M": "He spoke plainly about this, and Peter took him aside and began to rebuke him.",
      "T": "He said all this openly. Peter took him aside and began to push back sharply."
    },
    "33": {
      "L": "But turning and seeing his disciples, he rebuked Peter and said, 'Get behind me, Satan! For you are not thinking about the things of God, but the things of man.'",
      "M": "But when Jesus turned and looked at his disciples, he rebuked Peter. 'Get behind me, Satan!' he said. 'You do not have in mind the concerns of God, but merely human concerns.'",
      "T": "Jesus turned, looked at his disciples, and sharply rebuked Peter: 'Get behind me, Satan! You are not thinking about what matters to God—only what matters to people.'"
    },
    "34": {
      "L": "And calling the crowd to him with his disciples, he said to them, 'If anyone wishes to come after me, let him deny himself and take up his cross and follow me.'",
      "M": "Then he called the crowd to him along with his disciples and said: 'Whoever wants to be my disciple must deny themselves and take up their cross and follow me.'",
      "T": "He called the crowd together with his disciples and said, 'If any of you want to follow me, you must say no to yourselves, take up your cross, and come after me.'"
    },
    "35": {
      "L": "'For whoever wants to save his life will lose it, but whoever loses his life for my sake and the gospel's will save it.'",
      "M": "'For whoever wants to save their life will lose it, but whoever loses their life for me and for the gospel will save it.'",
      "T": "'Whoever tries to keep their life will lose it. But whoever surrenders their life for my sake and for the good news will save it.'"
    },
    "36": {
      "L": "'For what does it profit a man to gain the whole world and forfeit his life?'",
      "M": "'What good is it for someone to gain the whole world, yet forfeit their soul?'",
      "T": "'What good is it if you gain the whole world but lose your very life?'"
    },
    "37": {
      "L": "'For what can a man give in exchange for his life?'",
      "M": "'Or what can anyone give in exchange for their soul?'",
      "T": "'What would you exchange for your own life?'"
    },
    "38": {
      "L": "'For whoever is ashamed of me and my words in this adulterous and sinful generation, the Son of Man will also be ashamed of him when he comes in the glory of his Father with the holy angels.'",
      "M": "'If anyone is ashamed of me and my words in this adulterous and sinful generation, the Son of Man will be ashamed of them when he comes in his Father's glory with the holy angels.'",
      "T": "'Whoever is ashamed of me and my words in this unfaithful, sinful generation—the Son of Man will be ashamed of them when he comes in the glory of his Father with the holy angels.'"
    }
  }
}

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'mark')
    merge_tier(data, MARK, key)
    save(tier, 'mark', data)

print('\nMark 5–8 written to all three tiers.')
print('Chapters covered:', sorted(MARK.keys(), key=int))
