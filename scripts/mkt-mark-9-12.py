"""
MKT Mark chapters 9-12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-mark-9-12.py
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
  "9": {
    "1": {
      "L": "And he said to them, 'Truly, I say to you, there are some standing here who will not taste death until they see the kingdom of God after it has come with power.'",
      "M": "And he said to them, 'Truly I tell you, some who are standing here will not taste death before they see that the kingdom of God has come with power.'",
      "T": "He told them, 'I tell you the truth: some of you standing here will not die before you see God's kingdom arriving with power.'"
    },
    "2": {
      "L": "And after six days Jesus took with him Peter and James and John, and led them up a high mountain by themselves. And he was transfigured before them,",
      "M": "After six days Jesus took Peter, James and John with him and led them up a high mountain, where they were all alone. There he was transfigured before them.",
      "T": "Six days later Jesus took Peter, James, and John and led them up a high mountain by themselves. There he was transformed before their eyes—"
    },
    "3": {
      "L": "and his clothes became radiant, intensely white, as no one on earth could bleach them.",
      "M": "His clothes became dazzling white, whiter than anyone in the world could bleach them.",
      "T": "his clothes became intensely, brilliantly white—whiter than any bleach on earth could make them."
    },
    "4": {
      "L": "And there appeared to them Elijah with Moses, and they were talking with Jesus.",
      "M": "And there appeared before them Elijah and Moses, who were talking with Jesus.",
      "T": "And there appeared before them Elijah and Moses, talking with Jesus."
    },
    "5": {
      "L": "And Peter said to Jesus, 'Rabbi, it is good that we are here. Let us make three tents, one for you and one for Moses and one for Elijah.'",
      "M": "Peter said to Jesus, 'Rabbi, it is good for us to be here. Let us put up three shelters—one for you, one for Moses and one for Elijah.'",
      "T": "Peter blurted out to Jesus, 'Rabbi, it's wonderful to be here! Let us put up three shelters—one for you, one for Moses, and one for Elijah.'"
    },
    "6": {
      "L": "For he did not know what to say, for they were terrified.",
      "M": "He did not know what to say, they were so frightened.",
      "T": "He didn't know what he was saying—they were all overwhelmed with fear."
    },
    "7": {
      "L": "And a cloud overshadowed them, and a voice came out of the cloud, 'This is my beloved Son; listen to him.'",
      "M": "Then a cloud appeared and covered them, and a voice came from the cloud: 'This is my Son, whom I love. Listen to him!'",
      "T": "A cloud moved in and covered them, and a voice came from the cloud: 'This is my Son, my own beloved—listen to him!'"
    },
    "8": {
      "L": "And suddenly, looking around, they no longer saw anyone with them but Jesus only.",
      "M": "Suddenly, when they looked around, they no longer saw anyone with them except Jesus.",
      "T": "Then suddenly, looking around, they saw no one—only Jesus."
    },
    "9": {
      "L": "And as they were coming down the mountain, he charged them to tell no one what they had seen, until the Son of Man had risen from the dead.",
      "M": "As they were coming down the mountain, Jesus gave them orders not to tell anyone what they had seen until the Son of Man had risen from the dead.",
      "T": "Coming down the mountain, he instructed them to tell no one what they had seen until the Son of Man had risen from the dead."
    },
    "10": {
      "L": "So they kept the matter to themselves, questioning what this rising from the dead meant.",
      "M": "They kept the matter to themselves, discussing what 'rising from the dead' meant.",
      "T": "They kept it to themselves but debated among themselves what 'rising from the dead' meant."
    },
    "11": {
      "L": "And they asked him, 'Why do the scribes say that first Elijah must come?'",
      "M": "And they asked him, 'Why do the teachers of the law say that Elijah must come first?'",
      "T": "Then they asked him, 'Why do the Bible teachers say that Elijah must come first?'"
    },
    "12": {
      "L": "And he said to them, 'Elijah does come first to restore all things. And how is it written of the Son of Man that he should suffer many things and be treated with contempt?'",
      "M": "Jesus replied, 'To be sure, Elijah does come first, and restores all things. Why then is it written that the Son of Man must suffer much and be rejected?'",
      "T": "He answered, 'Yes, Elijah does come first to restore everything. But why does Scripture also say that the Son of Man must suffer greatly and be treated with contempt?'"
    },
    "13": {
      "L": "'But I tell you that Elijah has come, and they did to him whatever they pleased, as it is written of him.'",
      "M": "'But I tell you, Elijah has come, and they have done to him everything they wished, just as it is written about him.'",
      "T": "'I tell you, Elijah has already come, and they treated him exactly as they pleased—just as it was written about him.'"
    },
    "14": {
      "L": "And when they came to the disciples, they saw a great crowd around them, and scribes arguing with them.",
      "M": "When they came to the other disciples, they saw a large crowd around them and the teachers of the law arguing with them.",
      "T": "When they came back to the other disciples, they saw a large crowd surrounding them and Bible teachers arguing with them."
    },
    "15": {
      "L": "And immediately all the crowd, when they saw him, were greatly amazed and ran up to him and greeted him.",
      "M": "As soon as all the people saw Jesus, they were overwhelmed with wonder and ran to greet him.",
      "T": "When the crowd saw Jesus, they were filled with wonder and ran to greet him."
    },
    "16": {
      "L": "And he asked them, 'What are you arguing about with them?'",
      "M": "'What are you arguing with them about?' he asked.",
      "T": "'What are you arguing about with them?' he asked."
    },
    "17": {
      "L": "And someone from the crowd answered him, 'Teacher, I brought my son to you, for he has a spirit that makes him mute.'",
      "M": "A man in the crowd answered, 'Teacher, I brought you my son, who is possessed by a spirit that has robbed him of speech.'",
      "T": "A man from the crowd answered, 'Teacher, I brought my son to you. He is controlled by a spirit that makes him unable to speak.'"
    },
    "18": {
      "L": "'And whenever it seizes him, it throws him down, and he foams and grinds his teeth and becomes rigid. So I asked your disciples to cast it out, and they were not able.'",
      "M": "'Whenever it seizes him, it throws him to the ground. He foams at the mouth, gnashes his teeth and becomes rigid. I asked your disciples to drive out the spirit, but they could not.'",
      "T": "'Whenever it seizes him, it throws him to the ground. He foams at the mouth, grinds his teeth, and goes rigid. I asked your disciples to drive it out, but they couldn't.'"
    },
    "19": {
      "L": "And he answered them, 'O faithless generation, how long am I to be with you? How long am I to bear with you? Bring him to me.'",
      "M": "'You unbelieving generation,' Jesus replied, 'how long shall I stay with you? How long shall I put up with you? Bring the boy to me.'",
      "T": "'O faithless generation!' Jesus said. 'How long must I stay among you? How long must I put up with you? Bring the boy to me.'"
    },
    "20": {
      "L": "And they brought the boy to him. And when the spirit saw him, immediately it convulsed the boy, and he fell on the ground and rolled about, foaming at the mouth.",
      "M": "So they brought him. When the spirit saw Jesus, it immediately threw the boy into a convulsion. He fell to the ground and rolled around, foaming at the mouth.",
      "T": "They brought the boy to him. The moment the spirit saw Jesus, it threw the boy into a violent convulsion. He fell to the ground and rolled around, foaming at the mouth."
    },
    "21": {
      "L": "And Jesus asked his father, 'How long has this been happening to him?' And he said, 'From childhood.'",
      "M": "Jesus asked the boy's father, 'How long has he been like this?' 'From childhood,' he answered.",
      "T": "Jesus asked the boy's father, 'How long has this been happening to him?' 'Since childhood,' he answered."
    },
    "22": {
      "L": "'And it has often cast him into fire and into water, to destroy him. But if you can do anything, have compassion on us and help us.'",
      "M": "'It has often thrown him into fire or water to kill him. But if you can do anything, take pity on us and help us.'",
      "T": "'It has often thrown him into fire and into water, trying to kill him. But if there's anything you can do—please, have mercy on us and help us!'"
    },
    "23": {
      "L": "And Jesus said to him, '\"If you can\"! All things are possible for one who believes.'",
      "M": "'\"If you can\"?' said Jesus. 'Everything is possible for one who believes.'",
      "T": "Jesus said to him, '\"If you can\"? All things are possible for the one who trusts!'"
    },
    "24": {
      "L": "Immediately the father of the child cried out and said, 'I believe; help my unbelief!'",
      "M": "Immediately the boy's father exclaimed: 'I do believe; help me overcome my unbelief!'",
      "T": "The boy's father cried out at once: 'I believe! Help my failing faith!'"
    },
    "25": {
      "L": "And when Jesus saw that a crowd came running together, he rebuked the unclean spirit, saying to it, 'You mute and deaf spirit, I command you, come out of him and never enter him again.'",
      "M": "When Jesus saw that a crowd was running to the scene, he rebuked the impure spirit. 'You deaf and mute spirit,' he said, 'I command you, come out of him and never enter him again.'",
      "T": "Seeing a crowd rushing toward them, Jesus rebuked the evil spirit: 'You deaf and mute spirit—I command you: come out of him and never go back in!'"
    },
    "26": {
      "L": "And after crying out and convulsing him terribly, it came out, and the boy was like a corpse, so that most of them said, 'He is dead.'",
      "M": "The spirit shrieked, convulsed him violently and came out. The boy looked so much like a corpse that many said, 'He's dead.'",
      "T": "The spirit let out a shriek, shook the boy violently, and came out. The boy lay so still that many people said, 'He's dead.'"
    },
    "27": {
      "L": "But Jesus took him by the hand and lifted him up, and he arose.",
      "M": "But Jesus took him by the hand and lifted him to his feet, and he stood up.",
      "T": "But Jesus took him by the hand and lifted him to his feet. The boy stood up."
    },
    "28": {
      "L": "And when he had entered the house, his disciples asked him privately, 'Why could we not cast it out?'",
      "M": "After Jesus had gone indoors, his disciples asked him privately, 'Why couldn't we drive it out?'",
      "T": "When Jesus was inside the house, his disciples asked him privately, 'Why couldn't we drive it out?'"
    },
    "29": {
      "L": "And he said to them, 'This kind cannot be driven out by anything but prayer.'",
      "M": "He replied, 'This kind can come out only by prayer.'",
      "T": "He said to them, 'This kind can only be driven out by prayer.'"
    },
    "30": {
      "L": "They went on from there and passed through Galilee. And he did not want anyone to know,",
      "M": "They left that place and passed through Galilee. Jesus did not want anyone to know where they were,",
      "T": "They left that area and traveled through Galilee. Jesus didn't want anyone to know where they were,"
    },
    "31": {
      "L": "for he was teaching his disciples, saying to them, 'The Son of Man is going to be delivered into the hands of men, and they will kill him. And when he is killed, after three days he will rise.'",
      "M": "because he was teaching his disciples. He said to them, 'The Son of Man is going to be delivered into the hands of men. They will kill him, and after three days he will rise.'",
      "T": "because he was teaching his disciples. He told them, 'The Son of Man is going to be handed over into the power of human beings. They will kill him—and after three days he will rise.'"
    },
    "32": {
      "L": "But they did not understand the saying, and were afraid to ask him.",
      "M": "But they did not understand what he meant and were afraid to ask him about it.",
      "T": "But they didn't understand what he was saying, and were afraid to ask him."
    },
    "33": {
      "L": "And they came to Capernaum. And when he was in the house he asked them, 'What were you discussing on the way?'",
      "M": "They came to Capernaum. When he was in the house, he asked them, 'What were you arguing about on the road?'",
      "T": "They came to Capernaum. When he was inside the house, he asked them, 'What were you arguing about on the way?'"
    },
    "34": {
      "L": "But they kept silent, for on the way they had argued with one another about who was the greatest.",
      "M": "But they kept quiet because on the way they had argued about who was the greatest.",
      "T": "They went silent—on the way they had been arguing about who was the greatest."
    },
    "35": {
      "L": "And he sat down and called the twelve. And he said to them, 'If anyone would be first, he must be last of all and servant of all.'",
      "M": "Sitting down, Jesus called the Twelve and said, 'Anyone who wants to be first must be the very last, and the servant of all.'",
      "T": "He sat down, called the Twelve, and said to them, 'If anyone wants to be first, they must be last of all and servant of all.'"
    },
    "36": {
      "L": "And he took a child and put him in the midst of them, and taking him in his arms, he said to them,",
      "M": "He took a little child whom he placed among them. Taking the child in his arms, he said to them,",
      "T": "He took a small child and placed the child among them. Taking the child in his arms, he said,"
    },
    "37": {
      "L": "'Whoever receives one such child in my name receives me, and whoever receives me, receives not me but him who sent me.'",
      "M": "'Whoever welcomes one of these little children in my name welcomes me; and whoever welcomes me does not welcome me but the one who sent me.'",
      "T": "'Whoever welcomes a child like this in my name welcomes me—and whoever welcomes me welcomes not just me, but the one who sent me.'"
    },
    "38": {
      "L": "John said to him, 'Teacher, we saw someone casting out demons in your name, and we tried to stop him, because he was not following us.'",
      "M": "'Teacher,' said John, 'we saw someone driving out demons in your name and we told him to stop, because he was not one of us.'",
      "T": "John said to him, 'Teacher, we saw someone driving out demons in your name, and we tried to stop him, because he wasn't one of our group.'"
    },
    "39": {
      "L": "But Jesus said, 'Do not stop him, for no one who does a mighty work in my name will be able soon afterward to speak evil of me.'",
      "M": "'Do not stop him,' Jesus said. 'For no one who does a miracle in my name can in the next moment say anything bad about me,'",
      "T": "'Don't stop him,' Jesus said. 'No one who performs a miracle in my name can turn around and easily speak against me.'"
    },
    "40": {
      "L": "'For the one who is not against us is for us.'",
      "M": "'for whoever is not against us is for us.'",
      "T": "'Whoever is not against us is on our side.'"
    },
    "41": {
      "L": "'For truly, I say to you, whoever gives you a cup of water to drink because you belong to Christ will by no means lose his reward.'",
      "M": "'Truly I tell you, anyone who gives you a cup of water in my name because you belong to the Messiah will certainly not lose their reward.'",
      "T": "'I tell you the truth: anyone who gives you even a cup of water because you belong to the Messiah—they will certainly receive their reward.'"
    },
    "42": {
      "L": "'Whoever causes one of these little ones who believe in me to sin, it would be better for him if a great millstone were hung around his neck and he were thrown into the sea.'",
      "M": "'If anyone causes one of these little ones—those who believe in me—to stumble, it would be better for them if a large millstone were hung around their neck and they were thrown into the sea.'",
      "T": "'If anyone causes one of these little ones who trust in me to stumble, it would be far better for them to have a massive millstone hung around their neck and be thrown into the sea.'"
    },
    "43": {
      "L": "'And if your hand causes you to sin, cut it off. It is better for you to enter life crippled than with two hands to go to hell, to the unquenchable fire.'",
      "M": "'If your hand causes you to stumble, cut it off. It is better for you to enter life maimed than with two hands to go into hell, where the fire never goes out.'",
      "T": "'If your hand makes you fall into sin, cut it off. It is better to enter life with one hand than to go into hell with two—into that fire that can never be put out.'"
    },
    "44": {
      "L": "'Where their worm does not die and the fire is not quenched.'",
      "M": "'where the worms that eat them do not die, and the fire is not quenched.'",
      "T": "'where the worm never dies and the fire is never put out.'"
    },
    "45": {
      "L": "'And if your foot causes you to sin, cut it off. It is better for you to enter life lame than with two feet to be thrown into hell.'",
      "M": "'And if your foot causes you to stumble, cut it off. It is better for you to enter life crippled than to have two feet and be thrown into hell.'",
      "T": "'If your foot makes you fall into sin, cut it off. It is better to enter life with one foot than to be thrown into hell with two.'"
    },
    "46": {
      "L": "'Where their worm does not die and the fire is not quenched.'",
      "M": "'where the worms that eat them do not die, and the fire is not quenched.'",
      "T": "'where the worm never dies and the fire is never put out.'"
    },
    "47": {
      "L": "'And if your eye causes you to sin, tear it out. It is better for you to enter the kingdom of God with one eye than with two eyes to be thrown into hell,'",
      "M": "'And if your eye causes you to stumble, pluck it out. It is better for you to enter the kingdom of God with one eye than to have two eyes and be thrown into hell,'",
      "T": "'If your eye makes you fall into sin, tear it out. It is better to enter God's kingdom with one eye than to be thrown into hell with two—'"
    },
    "48": {
      "L": "'where their worm does not die and the fire is not quenched.'",
      "M": "'where the worms that eat them do not die, and the fire is not quenched.'",
      "T": "'where the worm never dies and the fire is never put out.'"
    },
    "49": {
      "L": "'For everyone will be salted with fire.'",
      "M": "'Everyone will be salted with fire.'",
      "T": "'For everyone will be tested with fire, as salt preserves.'"
    },
    "50": {
      "L": "'Salt is good, but if the salt has lost its saltiness, how will you make it salty again? Have salt in yourselves, and be at peace with one another.'",
      "M": "'Salt is good, but if it loses its saltiness, how can you make it salty again? Have salt among yourselves, and be at peace with each other.'",
      "T": "'Salt is valuable—but if salt loses its saltiness, how can you make it salty again? Keep the salt of your faithfulness, and live at peace with each other.'"
    }
  },
  "10": {
    "1": {
      "L": "And rising from there he went to the region of Judea and beyond the Jordan, and crowds gathered to him again, and as was his custom, he taught them again.",
      "M": "Jesus then left that place and went into the region of Judea and across the Jordan. Again crowds of people came to him, and as was his custom, he taught them.",
      "T": "Jesus left there and traveled to the region of Judea and across the Jordan. Crowds gathered around him again, and as was his practice, he taught them."
    },
    "2": {
      "L": "And Pharisees came up and in order to test him asked, 'Is it lawful for a man to divorce his wife?'",
      "M": "Some Pharisees came and tested him by asking, 'Is it lawful for a man to divorce his wife?'",
      "T": "Some Pharisees came to test him with the question: 'Is it lawful for a man to divorce his wife?'"
    },
    "3": {
      "L": "He answered them, 'What did Moses command you?'",
      "M": "'What did Moses command you?' he replied.",
      "T": "He answered their question with a question: 'What did Moses command you?'"
    },
    "4": {
      "L": "They said, 'Moses allowed a man to write a certificate of divorce and to send her away.'",
      "M": "They said, 'Moses permitted a man to write a certificate of divorce and send her away.'",
      "T": "They replied, 'Moses permitted a man to write a certificate of divorce and send her away.'"
    },
    "5": {
      "L": "And Jesus said to them, 'Because of your hardness of heart he wrote you this commandment.'",
      "M": "'It was because your hearts were hard that Moses wrote you this law,' Jesus replied.",
      "T": "Jesus replied, 'He wrote that command for you because of the hardness of your hearts.'"
    },
    "6": {
      "L": "'But from the beginning of creation, \"God made them male and female.\"'",
      "M": "'But at the beginning of creation God made them male and female.'",
      "T": "'But from the very beginning of creation, God made them male and female.'"
    },
    "7": {
      "L": "'\"Therefore a man shall leave his father and mother and hold fast to his wife,\"'",
      "M": "'\"For this reason a man will leave his father and mother and be united to his wife,\"'",
      "T": "'\"For this reason a man will leave his father and mother and be joined to his wife,\"'"
    },
    "8": {
      "L": "'\"and the two shall become one flesh.\" So they are no longer two but one flesh.'",
      "M": "'\"and the two will become one flesh.\" So they are no longer two, but one flesh.'",
      "T": "'\"and the two will become one flesh.\" They are no longer two—they are one flesh.'"
    },
    "9": {
      "L": "'What therefore God has joined together, let not man separate.'",
      "M": "'Therefore what God has joined together, let no one separate.'",
      "T": "'So what God has joined together, no human being must separate.'"
    },
    "10": {
      "L": "And in the house the disciples asked him again about this matter.",
      "M": "When they were in the house again, the disciples asked Jesus about this.",
      "T": "When they were back in the house, the disciples asked him about this again."
    },
    "11": {
      "L": "And he said to them, 'Whoever divorces his wife and marries another commits adultery against her,'",
      "M": "He answered, 'Anyone who divorces his wife and marries another woman commits adultery against her.'",
      "T": "He said to them, 'Anyone who divorces his wife and marries another woman commits adultery against her.'"
    },
    "12": {
      "L": "'and if she divorces her husband and marries another, she commits adultery.'",
      "M": "'And if she divorces her husband and marries another man, she commits adultery.'",
      "T": "'And if a woman divorces her husband and marries another man, she commits adultery.'"
    },
    "13": {
      "L": "And they were bringing children to him that he might touch them, and the disciples rebuked them.",
      "M": "People were bringing little children to Jesus for him to place his hands on them, but the disciples rebuked them.",
      "T": "People were bringing small children to Jesus so he would touch them, but the disciples told them to stop."
    },
    "14": {
      "L": "But when Jesus saw it, he was indignant and said to them, 'Let the children come to me; do not hinder them, for to such belongs the kingdom of God.'",
      "M": "When Jesus saw this, he was indignant. He said to them, 'Let the little children come to me, and do not hinder them, for the kingdom of God belongs to such as these.'",
      "T": "When Jesus saw this, he was indignant. 'Let the children come to me,' he said. 'Don't stop them—God's kingdom belongs to people like these.'"
    },
    "15": {
      "L": "'Truly, I say to you, whoever does not receive the kingdom of God like a child shall not enter it.'",
      "M": "'Truly I tell you, anyone who will not receive the kingdom of God like a little child will never enter it.'",
      "T": "'I tell you the truth: whoever doesn't receive God's kingdom with the trust of a child will never enter it.'"
    },
    "16": {
      "L": "And he took them in his arms and blessed them, laying his hands on them.",
      "M": "And he took the children in his arms, placed his hands on them and blessed them.",
      "T": "He took them in his arms, placed his hands on them, and blessed them."
    },
    "17": {
      "L": "And as he was setting out on his journey, a man ran up and knelt before him and asked him, 'Good Teacher, what must I do to inherit eternal life?'",
      "M": "As Jesus started on his way, a man ran up to him and fell on his knees before him. 'Good teacher,' he asked, 'what must I do to inherit eternal life?'",
      "T": "As Jesus was setting out again, a man ran up and fell on his knees before him. 'Good Teacher,' he asked, 'what must I do to inherit eternal life?'"
    },
    "18": {
      "L": "And Jesus said to him, 'Why do you call me good? No one is good except God alone.'",
      "M": "'Why do you call me good?' Jesus answered. 'No one is good—except God alone.'",
      "T": "'Why do you call me good?' Jesus replied. 'Only God is truly good.'"
    },
    "19": {
      "L": "'You know the commandments: \"Do not murder, Do not commit adultery, Do not steal, Do not bear false witness, Do not defraud, Honor your father and mother.\"'",
      "M": "'You know the commandments: \"You shall not murder, you shall not commit adultery, you shall not steal, you shall not give false testimony, you shall not defraud, honor your father and mother.\"'",
      "T": "'You know the commandments: \"Do not murder, do not commit adultery, do not steal, do not lie in court, do not defraud, honor your father and mother.\"'"
    },
    "20": {
      "L": "And he said to him, 'Teacher, all these I have kept from my youth.'",
      "M": "'Teacher,' he declared, 'all these I have kept since I was a boy.'",
      "T": "He said, 'Teacher, I have kept all these from the time I was young.'"
    },
    "21": {
      "L": "And Jesus, looking at him, loved him, and said to him, 'You lack one thing: go, sell all that you have and give to the poor, and you will have treasure in heaven; and come, follow me.'",
      "M": "Jesus looked at him and loved him. 'One thing you lack,' he said. 'Go, sell everything you have and give to the poor, and you will have treasure in heaven. Then come, follow me.'",
      "T": "Jesus looked at him with love. 'One thing you're missing,' he said. 'Go and sell everything you own, give the money to the poor—you'll have treasure in heaven—then come, follow me.'"
    },
    "22": {
      "L": "Disheartened by the saying, he went away sorrowful, for he had great possessions.",
      "M": "At this the man's face fell. He went away sad, because he had great wealth.",
      "T": "His face fell at that, and he went away deeply sad—for he had many possessions."
    },
    "23": {
      "L": "And Jesus looked around and said to his disciples, 'How difficult it will be for those who have wealth to enter the kingdom of God!'",
      "M": "Jesus looked around and said to his disciples, 'How hard it is for the rich to enter the kingdom of God!'",
      "T": "Jesus looked around at his disciples and said, 'How difficult it is for wealthy people to enter God's kingdom!'"
    },
    "24": {
      "L": "And the disciples were amazed at his words. But Jesus said to them again, 'Children, how difficult it is to enter the kingdom of God!'",
      "M": "The disciples were amazed at his words. But Jesus said again, 'Children, how hard it is to enter the kingdom of God!'",
      "T": "The disciples were astonished at his words. But Jesus said again, 'My children, how hard it is to enter God's kingdom!'"
    },
    "25": {
      "L": "'It is easier for a camel to go through the eye of a needle than for a rich person to enter the kingdom of God.'",
      "M": "'It is easier for a camel to go through the eye of a needle than for someone who is rich to enter the kingdom of God.'",
      "T": "'It's easier for a camel to squeeze through the eye of a needle than for a rich person to enter God's kingdom.'"
    },
    "26": {
      "L": "And they were exceedingly astonished, and said to him, 'Then who can be saved?'",
      "M": "The disciples were even more amazed, and said to each other, 'Who then can be saved?'",
      "T": "The disciples were completely staggered and asked each other, 'Then who on earth can be saved?'"
    },
    "27": {
      "L": "Jesus looked at them and said, 'With man it is impossible, but not with God. For all things are possible with God.'",
      "M": "Jesus looked at them and said, 'With man this is impossible, but not with God; all things are possible with God.'",
      "T": "Jesus looked at them and said, 'It is impossible for human beings—but not for God. Everything is possible for God.'"
    },
    "28": {
      "L": "Peter began to say to him, 'See, we have left everything and followed you.'",
      "M": "Then Peter spoke up, 'We have left everything to follow you!'",
      "T": "Peter spoke up: 'Look—we have left everything and followed you.'"
    },
    "29": {
      "L": "Jesus said, 'Truly, I say to you, there is no one who has left house or brothers or sisters or mother or father or children or lands, for my sake and for the gospel,'",
      "M": "'Truly I tell you,' Jesus replied, 'no one who has left home or brothers or sisters or mother or father or children or fields for me and the gospel'",
      "T": "Jesus replied, 'I tell you the truth: no one who has left home, brothers, sisters, mother, father, children, or land for my sake and for the good news'"
    },
    "30": {
      "L": "'who will not receive a hundredfold now in this time, houses and brothers and sisters and mothers and children and lands, with persecutions, and in the age to come eternal life.'",
      "M": "'will fail to receive a hundred times as much in this present age: homes, brothers, sisters, mothers, children and fields—along with persecutions—and in the age to come eternal life.'",
      "T": "'will fail to receive back a hundred times over in this present age—houses, brothers, sisters, mothers, children, and land, together with persecutions—and in the coming age, eternal life.'"
    },
    "31": {
      "L": "'But many who are first will be last, and the last first.'",
      "M": "'But many who are first will be last, and the last first.'",
      "T": "'But many who are first will end up last, and those who are last will end up first.'"
    },
    "32": {
      "L": "And they were on the road, going up to Jerusalem, and Jesus was walking ahead of them. And they were amazed, and those who followed were afraid. And taking the twelve again, he began to tell them what was to happen to him,",
      "M": "They were on their way up to Jerusalem, with Jesus leading the way, and the disciples were astonished, while those who followed were afraid. Again he took the Twelve aside and told them what was going to happen to him.",
      "T": "They were on the road going up to Jerusalem, with Jesus walking ahead of them. The disciples were bewildered, and those following behind were afraid. He took the Twelve aside again and began to tell them what was about to happen to him:"
    },
    "33": {
      "L": "saying, 'See, we are going up to Jerusalem, and the Son of Man will be delivered over to the chief priests and the scribes, and they will condemn him to death and deliver him over to the Gentiles.'",
      "M": "'We are going up to Jerusalem,' he said, 'and the Son of Man will be delivered over to the chief priests and the teachers of the law. They will condemn him to death and will hand him over to the Gentiles,'",
      "T": "'Listen: we are going up to Jerusalem. The Son of Man will be handed over to the chief priests and the Bible teachers. They will condemn him to death and hand him over to the Gentiles,'"
    },
    "34": {
      "L": "'And they will mock him and spit on him, and flog him and kill him. And after three days he will rise.'",
      "M": "'who will mock him and spit on him, flog him and kill him. Three days later he will rise.'",
      "T": "'who will mock him, spit on him, flog him, and kill him. But after three days he will rise.'"
    },
    "35": {
      "L": "And James and John, the sons of Zebedee, came up to him and said to him, 'Teacher, we want you to do for us whatever we ask of you.'",
      "M": "Then James and John, the sons of Zebedee, came to him. 'Teacher,' they said, 'we want you to do for us whatever we ask.'",
      "T": "James and John, the sons of Zebedee, came to him. 'Teacher,' they said, 'we want you to do something for us—whatever we ask.'"
    },
    "36": {
      "L": "And he said to them, 'What do you want me to do for you?'",
      "M": "'What do you want me to do for you?' he asked.",
      "T": "'What do you want me to do for you?' he asked."
    },
    "37": {
      "L": "And they said to him, 'Grant us to sit, one at your right hand and one at your left, in your glory.'",
      "M": "They replied, 'Let one of us sit at your right and the other at your left in your glory.'",
      "T": "They answered, 'Let one of us sit at your right and the other at your left when you come into your glory.'"
    },
    "38": {
      "L": "Jesus said to them, 'You do not know what you are asking. Are you able to drink the cup that I drink, or to be baptized with the baptism with which I am baptized?'",
      "M": "'You don't know what you are asking,' Jesus said. 'Can you drink the cup I drink or be baptized with the baptism I am baptized with?'",
      "T": "'You don't know what you're asking,' Jesus said. 'Can you drink the cup I'm going to drink? Can you undergo the baptism I'm going through?'"
    },
    "39": {
      "L": "And they said to him, 'We are able.' And Jesus said to them, 'The cup that I drink you will drink, and with the baptism with which I am baptized, you will be baptized,'",
      "M": "'We can,' they answered. Jesus said to them, 'You will drink the cup I drink and be baptized with the baptism I am baptized with,'",
      "T": "'We can,' they said. Jesus replied, 'You will drink the cup I drink and undergo the baptism I undergo,'"
    },
    "40": {
      "L": "'but to sit at my right hand or at my left is not mine to grant, but it is for those for whom it has been prepared.'",
      "M": "'but to sit at my right or left is not for me to grant. These places belong to those for whom they have been prepared.'",
      "T": "'but who sits at my right or left is not mine to decide—those places belong to whoever God has prepared them for.'"
    },
    "41": {
      "L": "And when the ten heard it, they began to be indignant at James and John.",
      "M": "When the ten heard about this, they became indignant with James and John.",
      "T": "When the other ten heard about this, they became angry with James and John."
    },
    "42": {
      "L": "And Jesus called them to him and said to them, 'You know that those who are considered rulers of the Gentiles lord it over them, and their great ones exercise authority over them.'",
      "M": "Jesus called them together and said, 'You know that those who are regarded as rulers of the Gentiles lord it over them, and their high officials exercise authority over them.'",
      "T": "Jesus called them together and said, 'You know how it works among the Gentiles: those in power lord it over others, and great leaders make everyone feel their authority.'"
    },
    "43": {
      "L": "'But it shall not be so among you. But whoever would be great among you must be your servant,'",
      "M": "'Not so with you. Instead, whoever wants to become great among you must be your servant,'",
      "T": "'That is not how it works among you. Whoever wants to be great must be your servant,'"
    },
    "44": {
      "L": "'and whoever would be first among you must be slave of all.'",
      "M": "'and whoever wants to be first must be slave of all.'",
      "T": "'and whoever wants to be first must be everyone's slave.'"
    },
    "45": {
      "L": "'For even the Son of Man came not to be served but to serve, and to give his life as a ransom for many.'",
      "M": "'For even the Son of Man did not come to be served, but to serve, and to give his life as a ransom for many.'",
      "T": "'For the Son of Man himself did not come to be served—he came to serve, and to give his life as a ransom in place of many.'"
    },
    "46": {
      "L": "And they came to Jericho. And as he was leaving Jericho with his disciples and a great crowd, Bartimaeus, a blind beggar, the son of Timaeus, was sitting by the roadside.",
      "M": "Then they came to Jericho. As Jesus and his disciples, together with a large crowd, were leaving the city, a blind man, Bartimaeus (which means 'son of Timaeus'), was sitting by the roadside begging.",
      "T": "They came to Jericho. And as Jesus was leaving the city with his disciples and a large crowd, a blind man named Bartimaeus—son of Timaeus—was sitting beside the road, begging."
    },
    "47": {
      "L": "And when he heard that it was Jesus of Nazareth, he began to cry out and say, 'Jesus, Son of David, have mercy on me!'",
      "M": "When he heard that it was Jesus of Nazareth, he began to shout, 'Jesus, Son of David, have mercy on me!'",
      "T": "When he heard that it was Jesus of Nazareth, he began to shout, 'Jesus! Son of David! Have mercy on me!'"
    },
    "48": {
      "L": "And many rebuked him, telling him to be silent. But he cried out all the more, 'Son of David, have mercy on me!'",
      "M": "Many rebuked him and told him to be quiet, but he shouted all the more, 'Son of David, have mercy on me!'",
      "T": "Many people told him to be quiet, but he shouted all the louder, 'Son of David! Have mercy on me!'"
    },
    "49": {
      "L": "And Jesus stopped and said, 'Call him.' And they called the blind man, saying to him, 'Take heart. Get up; he is calling you.'",
      "M": "Jesus stopped and said, 'Call him.' So they called to the blind man, 'Cheer up! On your feet! He's calling you.'",
      "T": "Jesus stopped. 'Call him,' he said. So they called the blind man: 'Cheer up! Get up—he's calling you!'"
    },
    "50": {
      "L": "And throwing off his cloak, he sprang up and came to Jesus.",
      "M": "Throwing his cloak aside, he jumped to his feet and came to Jesus.",
      "T": "The man threw off his cloak, jumped to his feet, and came to Jesus."
    },
    "51": {
      "L": "And Jesus said to him, 'What do you want me to do for you?' And the blind man said to him, 'Rabbi, let me recover my sight.'",
      "M": "'What do you want me to do for you?' Jesus asked him. The blind man said, 'Rabbi, I want to see.'",
      "T": "'What do you want me to do for you?' Jesus asked. 'Rabboni,' the man said, 'I want to see again.'"
    },
    "52": {
      "L": "And Jesus said to him, 'Go your way; your faith has made you well.' And immediately he recovered his sight and followed him on the way.",
      "M": "'Go,' said Jesus, 'your faith has healed you.' Immediately he received his sight and followed Jesus along the road.",
      "T": "'Go,' Jesus said. 'Your faith has healed you.' Immediately the man could see, and he followed Jesus down the road."
    }
  },
  "11": {
    "1": {
      "L": "Now when they drew near to Jerusalem, to Bethphage and Bethany, at the Mount of Olives, Jesus sent two of his disciples",
      "M": "As they approached Jerusalem and came to Bethphage and Bethany at the Mount of Olives, Jesus sent two of his disciples,",
      "T": "As they approached Jerusalem and came to Bethphage and Bethany near the Mount of Olives, Jesus sent two of his disciples on ahead,"
    },
    "2": {
      "L": "and said to them, 'Go into the village in front of you, and immediately as you enter it you will find a colt tied, on which no one has ever sat. Untie it and bring it.'",
      "M": "saying to them, 'Go to the village ahead of you, and just as you enter it, you will find a colt tied there, which no one has ever ridden. Untie it and bring it here.'",
      "T": "saying, 'Go to the village ahead. As soon as you enter, you'll find a young donkey tied there—one that has never been ridden. Untie it and bring it.'"
    },
    "3": {
      "L": "'If anyone says to you, \"Why are you doing this?\" say, \"The Lord has need of it and will send it back here immediately.\"'",
      "M": "'If anyone asks you, \"Why are you doing this?\" say, \"The Lord needs it and will send it back here shortly.\"'",
      "T": "'If anyone asks why you're doing this, say: \"The Lord needs it and will return it promptly.\"'"
    },
    "4": {
      "L": "And they went away and found a colt tied at a door outside in the street, and they untied it.",
      "M": "They went and found a colt outside in the street, tied at a doorway. As they untied it,",
      "T": "They went and found a young donkey tied outside a door in the street. As they untied it,"
    },
    "5": {
      "L": "And some of those standing there said to them, 'What are you doing, untying the colt?'",
      "M": "some people standing there asked, 'What are you doing, untying that colt?'",
      "T": "some bystanders asked, 'What are you doing, untying that donkey?'"
    },
    "6": {
      "L": "And they told them what Jesus had said, and they let them go.",
      "M": "They answered as Jesus had told them to, and the people let them go.",
      "T": "They answered just as Jesus had told them, and the people let them take it."
    },
    "7": {
      "L": "And they brought the colt to Jesus and threw their cloaks on it, and he sat on it.",
      "M": "When they brought the colt to Jesus and threw their cloaks over it, he sat on it.",
      "T": "They brought the young donkey to Jesus, laid their cloaks over it, and he sat on it."
    },
    "8": {
      "L": "And many spread their cloaks on the road, and others spread leafy branches that they had cut from the fields.",
      "M": "Many people spread their cloaks on the road, while others spread branches they had cut in the fields.",
      "T": "Many people spread their cloaks on the road; others cut branches from the fields and spread them down."
    },
    "9": {
      "L": "And those who went before and those who followed were shouting, 'Hosanna! Blessed is he who comes in the name of the Lord!'",
      "M": "Those who went ahead and those who followed shouted, 'Hosanna!' 'Blessed is he who comes in the name of the Lord!'",
      "T": "Those in front and those behind were shouting, 'Hosanna! Blessed is the one who comes in the name of the Lord!'"
    },
    "10": {
      "L": "'Blessed is the coming kingdom of our father David! Hosanna in the highest!'",
      "M": "'Blessed is the coming kingdom of our father David!' 'Hosanna in the highest heaven!'",
      "T": "'Blessed is the coming kingdom of our ancestor David! Hosanna in the highest heavens!'"
    },
    "11": {
      "L": "And he entered Jerusalem and went into the temple. And when he had looked around at everything, as it was already late, he went out to Bethany with the twelve.",
      "M": "Jesus entered Jerusalem and went into the temple courts. He looked around at everything, but since it was already late, he went out to Bethany with the Twelve.",
      "T": "Jesus entered Jerusalem and went into the temple. He looked around at everything there, but since it was already late in the day, he went out to Bethany with the Twelve."
    },
    "12": {
      "L": "On the following day, when they came from Bethany, he was hungry.",
      "M": "The next day as they were leaving Bethany, Jesus was hungry.",
      "T": "The next morning as they left Bethany, Jesus was hungry."
    },
    "13": {
      "L": "And seeing in the distance a fig tree in leaf, he went to see if he could find anything on it. When he came to it, he found nothing but leaves, for it was not the season for figs.",
      "M": "Seeing in the distance a fig tree in leaf, he went to find out if it had any fruit. When he reached it, he found nothing but leaves, because it was not the season for figs.",
      "T": "He noticed a fig tree in the distance, covered in leaves. He went to see if it had any fruit. When he got to it, he found nothing but leaves—it wasn't the season for figs."
    },
    "14": {
      "L": "And he said to it, 'May no one ever eat fruit from you again.' And his disciples heard it.",
      "M": "Then he said to the tree, 'May no one ever eat fruit from you again.' And his disciples heard him say it.",
      "T": "He said to the tree, 'May no one ever eat fruit from you again.' And his disciples heard him say it."
    },
    "15": {
      "L": "And they came to Jerusalem. And he entered the temple and began to drive out those who sold and those who bought in the temple, and he overturned the tables of the money-changers and the seats of those who sold pigeons.",
      "M": "On reaching Jerusalem, Jesus entered the temple courts and began driving out those who were buying and selling there. He overturned the tables of the money changers and the benches of those selling doves,",
      "T": "When they reached Jerusalem, Jesus entered the temple courts and began driving out those who were buying and selling there. He overturned the money changers' tables and the seats of those selling doves,"
    },
    "16": {
      "L": "And he would not allow anyone to carry goods through the temple.",
      "M": "and would not allow anyone to carry merchandise through the temple courts.",
      "T": "and he would not let anyone carry merchandise through the temple."
    },
    "17": {
      "L": "And he was teaching them and saying to them, 'Is it not written, \"My house shall be called a house of prayer for all the nations\"? But you have made it a den of robbers.'",
      "M": "And as he taught them, he said, 'Is it not written: \"My house will be called a house of prayer for all nations\"? But you have made it \"a den of robbers.\"'",
      "T": "And he began to teach them: 'Is it not written: \"My house will be called a house of prayer for all nations\"? But you have turned it into a hideout for thieves!'"
    },
    "18": {
      "L": "And the chief priests and the scribes heard it and were seeking a way to destroy him, for they feared him, because all the crowd was astonished at his teaching.",
      "M": "The chief priests and the teachers of the law heard this and began looking for a way to kill him, for they feared him, because the whole crowd was amazed at his teaching.",
      "T": "The chief priests and the Bible teachers heard this and began plotting how to kill him—for they feared him, because the entire crowd was overwhelmed by his teaching."
    },
    "19": {
      "L": "And when evening came they went out of the city.",
      "M": "When evening came, Jesus and his disciples went out of the city.",
      "T": "When evening came, Jesus and his disciples left the city."
    },
    "20": {
      "L": "As they passed by in the morning, they saw the fig tree withered away to its roots.",
      "M": "In the morning, as they went along, they saw the fig tree withered from the roots.",
      "T": "In the morning, as they passed by, they saw the fig tree had withered from its very roots."
    },
    "21": {
      "L": "And Peter remembered and said to him, 'Rabbi, look! The fig tree that you cursed has withered.'",
      "M": "Peter remembered and said to Jesus, 'Rabbi, look! The fig tree you cursed has withered!'",
      "T": "Peter remembered and said to him, 'Rabbi, look! The fig tree you cursed has withered!'"
    },
    "22": {
      "L": "And Jesus answered them, 'Have faith in God.'",
      "M": "'Have faith in God,' Jesus answered.",
      "T": "Jesus answered, 'Have faith in God.'"
    },
    "23": {
      "L": "'Truly, I say to you, whoever says to this mountain, \"Be taken up and thrown into the sea,\" and does not doubt in his heart, but believes that what he says will come to pass, it will be done for him.'",
      "M": "'Truly I tell you, if anyone says to this mountain, \"Go, throw yourself into the sea,\" and does not doubt in their heart but believes that what they say will happen, it will be done for them.'",
      "T": "'I tell you the truth: if anyone says to this mountain, \"Go, throw yourself into the sea,\" and doesn't waver in their heart but trusts that what they say will happen—it will be done for them.'"
    },
    "24": {
      "L": "'Therefore I tell you, whatever you ask in prayer, believe that you have received it, and it will be yours.'",
      "M": "'Therefore I tell you, whatever you ask for in prayer, believe that you have received it, and it will be yours.'",
      "T": "'So I tell you: whatever you pray and ask for—believe that you have received it, and it will be yours.'"
    },
    "25": {
      "L": "'And whenever you stand praying, forgive, if you have anything against anyone, so that your Father also who is in heaven may forgive you your trespasses.'",
      "M": "'And when you stand praying, if you hold anything against anyone, forgive them, so that your Father in heaven may forgive you your sins.'",
      "T": "'And when you stand to pray, if you hold anything against anyone, forgive them—so that your Father in heaven will also forgive your sins.'"
    },
    "27": {
      "L": "And they came again to Jerusalem. And as he was walking in the temple, the chief priests and the scribes and the elders came to him,",
      "M": "They arrived again in Jerusalem, and while Jesus was walking in the temple courts, the chief priests, the teachers of the law and the elders came to him.",
      "T": "They returned to Jerusalem. As Jesus was walking in the temple courts, the chief priests, the Bible teachers, and the elders came to him."
    },
    "28": {
      "L": "and they said to him, 'By what authority are you doing these things, or who gave you this authority to do them?'",
      "M": "'By what authority are you doing these things?' they asked. 'And who gave you authority to do this?'",
      "T": "'By what authority are you doing these things?' they demanded. 'Who gave you this authority?'"
    },
    "29": {
      "L": "Jesus said to them, 'I will ask you one question; answer me, and I will tell you by what authority I do these things.'",
      "M": "Jesus replied, 'I will ask you one question. Answer me, and I will tell you by what authority I am doing these things.'",
      "T": "Jesus answered, 'Let me ask you one question. Answer it, and I'll tell you by what authority I do these things.'"
    },
    "30": {
      "L": "'John's baptism—was it from heaven or from man? Answer me.'",
      "M": "'John's baptism—was it from heaven, or of human origin? Tell me!'",
      "T": "'John's baptism—was it from heaven, or was it merely human in origin? Tell me!'"
    },
    "31": {
      "L": "And they discussed it with one another, saying, 'If we say, \"From heaven,\" he will say, \"Why then did you not believe him?\"'",
      "M": "They discussed it among themselves and said, 'If we say, \"From heaven,\" he will ask, \"Then why didn't you believe him?\"'",
      "T": "They reasoned among themselves: 'If we say \"From heaven,\" he'll ask, \"Then why didn't you believe him?\"'"
    },
    "32": {
      "L": "'But shall we say, \"From man\"?'—they were afraid of the people, for they all held that John really was a prophet.",
      "M": "'But if we say, \"Of human origin\" ...' (They feared the people, for everyone held that John really was a prophet.)",
      "T": "'But if we say \"From people\"...' They were afraid of the crowd—for everyone believed John was a genuine prophet."
    },
    "33": {
      "L": "So they answered Jesus, 'We do not know.' And Jesus said to them, 'Neither will I tell you by what authority I do these things.'",
      "M": "So they answered Jesus, 'We don't know.' Jesus said, 'Neither will I tell you by what authority I am doing these things.'",
      "T": "So they answered Jesus, 'We don't know.' Jesus replied, 'Then I'm not going to tell you by what authority I do these things.'"
    }
  },
  "12": {
    "1": {
      "L": "And he began to speak to them in parables. 'A man planted a vineyard and put a fence around it and dug a pit for the winepress and built a tower, and leased it to tenants and went into another country.'",
      "M": "Jesus then began to speak to them in parables: 'A man planted a vineyard. He put a wall around it, dug a pit for the winepress and built a watchtower. Then he rented the vineyard to some farmers and moved to another place.'",
      "T": "He began speaking to them in parables: 'A man planted a vineyard. He built a wall around it, dug a pit for the winepress, and erected a watchtower. Then he rented it out to tenant farmers and went on a journey.'"
    },
    "2": {
      "L": "'When the season came, he sent a servant to the tenants to get from them some of the fruit of the vineyard.'",
      "M": "'At harvest time he sent a servant to the tenants to collect from them some of the fruit of the vineyard.'",
      "T": "'When harvest time came, he sent a servant to the tenants to collect his share of the fruit.'"
    },
    "3": {
      "L": "'And they took him and beat him and sent him away empty-handed.'",
      "M": "'But they seized him, beat him and sent him away empty-handed.'",
      "T": "'But the tenants seized him, beat him, and sent him away with nothing.'"
    },
    "4": {
      "L": "'Again he sent to them another servant, and they struck him on the head and treated him shamefully.'",
      "M": "'Then he sent another servant to them; they struck this man on the head and treated him shamefully.'",
      "T": "'He sent another servant. They struck him on the head and treated him with contempt.'"
    },
    "5": {
      "L": "'And he sent another, and him they killed. And so with many others: some they beat, and some they killed.'",
      "M": "'He sent still another, and that one they killed. He sent many others; some of them they beat, others they killed.'",
      "T": "'He sent yet another, and him they killed. He sent many others—some they beat, some they killed.'"
    },
    "6": {
      "L": "'He had still one other, a beloved son. Finally he sent him to them, saying, \"They will respect my son.\"'",
      "M": "'He had one left to send, a son, whom he loved. He sent him last of all, saying, \"They will respect my son.\"'",
      "T": "'He had one more to send—his own dear son. He sent him last of all, thinking, \"They will respect my son.\"'"
    },
    "7": {
      "L": "'But those tenants said to one another, \"This is the heir. Come, let us kill him, and the inheritance will be ours.\"'",
      "M": "'But the tenants said to one another, \"This is the heir. Come, let's kill him, and the inheritance will be ours.\"'",
      "T": "'But the tenants said to each other, \"This is the heir. Come on—let's kill him, and the inheritance will be ours!\"'"
    },
    "8": {
      "L": "'And they took him and killed him and threw him out of the vineyard.'",
      "M": "'So they took him and killed him, and threw him out of the vineyard.'",
      "T": "'So they seized him, killed him, and threw his body out of the vineyard.'"
    },
    "9": {
      "L": "'What will the owner of the vineyard do? He will come and destroy the tenants and give the vineyard to others.'",
      "M": "'What then will the owner of the vineyard do? He will come and kill those tenants and give the vineyard to others.'",
      "T": "'What will the owner do? He will come and destroy those tenants and give the vineyard to others.'"
    },
    "10": {
      "L": "'Have you not read this Scripture: \"The stone that the builders rejected has become the cornerstone;'",
      "M": "'Haven't you read this passage of Scripture: \"The stone the builders rejected has become the cornerstone;'",
      "T": "'Haven't you read this scripture: \"The stone the builders threw away has become the cornerstone—'"
    },
    "11": {
      "L": "'this was the Lord's doing, and it is marvelous in our eyes\"?'",
      "M": "'this is the Lord's doing, and it is marvelous in our eyes\"?'",
      "T": "'this is the Lord's doing, and it is wonderful to see!\"?'"
    },
    "12": {
      "L": "And they were seeking to arrest him but feared the people, for they perceived that he had told the parable against them. So they left him and went away.",
      "M": "Then the chief priests, the teachers of the law and the elders looked for a way to arrest him because they knew he had spoken the parable against them. But they were afraid of the crowd; so they left him and went away.",
      "T": "They wanted to arrest him but feared the crowd—because they realized he had told the parable against them. So they left him and went away."
    },
    "13": {
      "L": "And they sent to him some of the Pharisees and some of the Herodians, to trap him in his talk.",
      "M": "Later they sent some of the Pharisees and Herodians to Jesus to catch him in his words.",
      "T": "They sent some Pharisees and Herodians to Jesus, hoping to trap him in something he said."
    },
    "14": {
      "L": "And they came and said to him, 'Teacher, we know that you are true and do not care about anyone's opinion. For you are not swayed by appearances, but truly teach the way of God. Is it lawful to pay taxes to Caesar, or not? Should we pay them, or should we not?'",
      "M": "They came to him and said, 'Teacher, we know that you are a man of integrity. You aren't swayed by others, because you pay no attention to who they are; but you teach the way of God in accordance with the truth. Is it right to pay the imperial tax to Caesar or not? Should we pay or shouldn't we?'",
      "T": "They came and said, 'Teacher, we know you are a man of integrity who is swayed by no one. You don't play favorites—you teach God's way honestly. Is it right to pay the Roman tax to Caesar, or not? Should we pay or refuse?'"
    },
    "15": {
      "L": "But knowing their hypocrisy, he said to them, 'Why put me to the test? Bring me a denarius and let me look at it.'",
      "M": "But Jesus knew their hypocrisy. 'Why are you trying to trap me?' he asked. 'Bring me a denarius and let me look at it.'",
      "T": "Seeing through their hypocrisy, he said, 'Why are you testing me? Bring me a denarius—let me look at it.'"
    },
    "16": {
      "L": "And they brought one. And he said to them, 'Whose likeness and inscription is this?' They said to him, 'Caesar's.'",
      "M": "They brought the coin, and he asked them, 'Whose image is this? And whose inscription?' 'Caesar's,' they replied.",
      "T": "They brought one. He asked, 'Whose face is this? Whose inscription?' They said, 'Caesar's.'"
    },
    "17": {
      "L": "Jesus said to them, 'Render to Caesar the things that are Caesar's, and to God the things that are God's.' And they marveled at him.",
      "M": "Then Jesus said to them, 'Give back to Caesar what is Caesar's and to God what is God's.' And they were amazed at him.",
      "T": "Jesus said to them, 'Give to Caesar what belongs to Caesar—and give to God what belongs to God.' And they were astonished at him."
    },
    "18": {
      "L": "And Sadducees came to him, who say that there is no resurrection. And they asked him a question, saying,",
      "M": "Then the Sadducees, who say there is no resurrection, came to him with a question.",
      "T": "Then the Sadducees—who claim there is no resurrection—came to him with a question."
    },
    "19": {
      "L": "'Teacher, Moses wrote for us that if a man's brother dies and leaves a wife, but leaves no child, the man must take the widow and raise up offspring for his brother.'",
      "M": "'Teacher,' they said, 'Moses wrote for us that if a man's brother dies and leaves a wife but no children, the man must marry the widow and raise up offspring for his brother.'",
      "T": "'Teacher,' they said, 'Moses wrote for us that if a man's brother dies leaving a wife but no child, the man must marry the widow and produce an heir for his brother.'"
    },
    "20": {
      "L": "'There were seven brothers; the first took a wife, and when he died left no offspring.'",
      "M": "'Now there were seven brothers. The first one married and died without leaving any children.'",
      "T": "'Now suppose there were seven brothers. The first married a woman and died, leaving no children.'"
    },
    "21": {
      "L": "'And the second took her, and died, leaving no offspring. And the third likewise.'",
      "M": "'The second one married the widow, but he also died, leaving no child. The third man married her,'",
      "T": "'The second married her and died, leaving no children. Then the third married her—'"
    },
    "22": {
      "L": "'And the seven left no offspring. Last of all the woman also died.'",
      "M": "'and it was the same with all seven. Last of all, the woman died too.'",
      "T": "'and so it went through all seven. Last of all, the woman died too.'"
    },
    "23": {
      "L": "'In the resurrection, when they rise again, whose wife will she be? For the seven had her as wife.'",
      "M": "'At the resurrection whose wife will she be, since the seven were married to her?'",
      "T": "'When they all rise at the resurrection, whose wife will she be? All seven were married to her!'"
    },
    "24": {
      "L": "Jesus said to them, 'Is this not the reason you are wrong, because you know neither the Scriptures nor the power of God?'",
      "M": "Jesus replied, 'Are you not in error because you do not know the Scriptures or the power of God?'",
      "T": "Jesus replied, 'Isn't your error due to your ignorance of Scripture and of God's power?'"
    },
    "25": {
      "L": "'For when they rise from the dead, they neither marry nor are given in marriage, but are like angels in heaven.'",
      "M": "'When the dead rise, they will neither marry nor be given in marriage; they will be like the angels in heaven.'",
      "T": "'When people rise from the dead, they don't marry or become anyone's spouse—they are like the angels in heaven.'"
    },
    "26": {
      "L": "'And as for the dead being raised, have you not read in the book of Moses, in the passage about the bush, how God spoke to him, saying, \"I am the God of Abraham, and the God of Isaac, and the God of Jacob\"?'",
      "M": "'Now about the dead rising—have you not read in the Book of Moses, in the account of the burning bush, how God said to him, \"I am the God of Abraham, the God of Isaac, and the God of Jacob\"?'",
      "T": "'As for the dead being raised—haven't you read in Moses' writings, in the account of the burning bush, how God said to him, \"I am the God of Abraham, the God of Isaac, and the God of Jacob\"?'"
    },
    "27": {
      "L": "'He is not God of the dead, but of the living. You are quite wrong.'",
      "M": "'He is not the God of the dead, but of the living. You are badly mistaken!'",
      "T": "'He is not the God of the dead but of the living. You are completely wrong!'"
    },
    "28": {
      "L": "And one of the scribes came up and heard them disputing with one another, and seeing that he answered them well, asked him, 'Which commandment is the most important of all?'",
      "M": "One of the teachers of the law came and heard them debating. Noticing that Jesus had given them a good answer, he asked him, 'Of all the commandments, which is the most important?'",
      "T": "One of the Bible teachers had been listening to the debate. Noticing that Jesus had given excellent answers, he asked, 'Of all the commandments, which one is the most important?'"
    },
    "29": {
      "L": "Jesus answered, 'The most important is, \"Hear, O Israel: The Lord our God, the Lord is one.'",
      "M": "'The most important one,' answered Jesus, 'is this: \"Hear, O Israel: The Lord our God, the Lord is one.'",
      "T": "Jesus answered, 'The most important is this: \"Hear, O Israel: The Lord our God, the Lord is one.'"
    },
    "30": {
      "L": "'And you shall love the Lord your God with all your heart and with all your soul and with all your mind and with all your strength.\"'",
      "M": "'Love the Lord your God with all your heart and with all your soul and with all your mind and with all your strength.\"'",
      "T": "'Love the Lord your God with all your heart, all your soul, all your mind, and all your strength.\"'"
    },
    "31": {
      "L": "'The second is this: \"You shall love your neighbor as yourself.\" There is no other commandment greater than these.'",
      "M": "'The second is this: \"Love your neighbor as yourself.\" There is no commandment greater than these.'",
      "T": "'The second is: \"Love your neighbor as yourself.\" No commandment is greater than these two.'"
    },
    "32": {
      "L": "And the scribe said to him, 'You are right, Teacher. You have truly said that he is one, and there is no other besides him.'",
      "M": "'Well said, teacher,' the man replied. 'You are right in saying that God is one and there is no other but him.'",
      "T": "The teacher said to him, 'Well said, Teacher. You are right—God is one, and there is no other.'"
    },
    "33": {
      "L": "'And to love him with all the heart and with all the understanding and with all the strength, and to love one's neighbor as oneself, is much more than all whole burnt offerings and sacrifices.'",
      "M": "'To love him with all your heart, with all your understanding and with all your strength, and to love your neighbor as yourself is more important than all burnt offerings and sacrifices.'",
      "T": "'To love him with all your heart, understanding, and strength, and to love your neighbor as yourself—that is far more important than all burnt offerings and sacrifices combined.'"
    },
    "34": {
      "L": "And when Jesus saw that he answered wisely, he said to him, 'You are not far from the kingdom of God.' And after that no one dared to ask him any more questions.",
      "M": "When Jesus saw that he had answered wisely, he said to him, 'You are not far from the kingdom of God.' And from then on no one dared ask him any more questions.",
      "T": "Seeing that he had answered with wisdom, Jesus said to him, 'You are not far from God's kingdom.' After that, no one dared to ask him any more questions."
    },
    "35": {
      "L": "And as Jesus taught in the temple, he said, 'How can the scribes say that the Christ is the son of David?'",
      "M": "While Jesus was teaching in the temple courts, he asked, 'Why do the teachers of the law say that the Messiah is the son of David?'",
      "T": "While teaching in the temple courts, Jesus asked, 'How can the Bible teachers say that the Messiah is the son of David?'"
    },
    "36": {
      "L": "'David himself, in the Holy Spirit, declared, \"The Lord said to my Lord, Sit at my right hand, until I put your enemies under your feet.\"'",
      "M": "'David himself, speaking by the Holy Spirit, declared: \"The Lord said to my Lord: \"Sit at my right hand until I put your enemies under your feet.\"\"'",
      "T": "'David himself, moved by the Holy Spirit, declared: \"The Lord said to my Lord: Sit at my right hand until I make your enemies a footstool for your feet.\"'"
    },
    "37": {
      "L": "'David himself calls him Lord. So how is he his son?' And the great throng heard him gladly.",
      "M": "'David himself calls him \"Lord.\" How then can he be his son?' The large crowd listened to him with delight.",
      "T": "'David himself calls him \"Lord\" — so how can he be his son?' The large crowd listened to him with great delight."
    },
    "38": {
      "L": "And in his teaching he said, 'Beware of the scribes, who like to walk around in long robes and like greetings in the marketplaces'",
      "M": "As he taught, Jesus said, 'Watch out for the teachers of the law. They like to walk around in flowing robes and be greeted with respect in the marketplaces,'",
      "T": "As he was teaching, he said, 'Beware of the Bible teachers. They love walking around in flowing robes and being greeted with honor in the marketplaces,'"
    },
    "39": {
      "L": "'and have the best seats in the synagogues and the places of honor at feasts,'",
      "M": "'and have the most important seats in the synagogues and the places of honor at banquets.'",
      "T": "'and taking the front seats in the synagogues and the best places at banquets.'"
    },
    "40": {
      "L": "'who devour widows' houses and for a pretense make long prayers. They will receive the greater condemnation.'",
      "M": "'They devour widows' houses and for a show make lengthy prayers. These men will be punished most severely.'",
      "T": "'They swallow up the property of widows and put on a show of long prayers. Such people will face the heaviest judgment.'"
    },
    "41": {
      "L": "And he sat down opposite the treasury and watched the people putting money into the offering box. Many rich people put in large sums.",
      "M": "Jesus sat down opposite the place where the offerings were put and watched the crowd putting their money into the temple treasury. Many rich people threw in large amounts.",
      "T": "Jesus sat down across from the temple treasury and watched as people dropped money into the offering boxes. Many wealthy people gave large amounts."
    },
    "42": {
      "L": "And a poor widow came and put in two small copper coins, which make a penny.",
      "M": "But a poor widow came and put in two very small copper coins, worth only a few cents.",
      "T": "Then a poor widow came and dropped in two small copper coins—worth barely anything."
    },
    "43": {
      "L": "And he called his disciples to him and said to them, 'Truly, I say to you, this poor widow has put in more than all those who are contributing to the offering box.'",
      "M": "Calling his disciples to him, Jesus said, 'Truly I tell you, this poor widow has put more into the treasury than all the others.'",
      "T": "He called his disciples over and said, 'I tell you the truth: this poor widow has given more than all the others combined.'"
    },
    "44": {
      "L": "'For they all contributed out of their abundance, but she out of her poverty has put in everything she had, all she had to live on.'",
      "M": "'They all gave out of their wealth; but she, out of her poverty, put in everything—all she had to live on.'",
      "T": "'All the others gave out of their surplus wealth. But she gave out of her poverty—she put in everything she had, her entire livelihood.'"
    }
  }
}

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'mark')
    merge_tier(data, MARK, key)
    save(tier, 'mark', data)

print('\nMark 9–12 written to all three tiers.')
print('Chapters covered:', sorted(MARK.keys(), key=int))
