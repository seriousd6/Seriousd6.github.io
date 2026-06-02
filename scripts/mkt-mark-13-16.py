"""
MKT Mark chapters 13-16 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-mark-13-16.py
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
  "13": {
    "1": {
      "L": "And as he came out of the temple, one of his disciples said to him, 'Look, Teacher, what wonderful stones and what wonderful buildings!'",
      "M": "As Jesus was leaving the temple, one of his disciples said to him, 'Look, Teacher! What massive stones! What magnificent buildings!'",
      "T": "As Jesus was leaving the temple, one of his disciples said to him, 'Look, Teacher—what enormous stones! What magnificent buildings!'"
    },
    "2": {
      "L": "And Jesus said to him, 'Do you see these great buildings? There will not be left here one stone upon another that will not be thrown down.'",
      "M": "'Do you see all these great buildings?' replied Jesus. 'Not one stone here will be left on another; every one will be thrown down.'",
      "T": "'You see all these great buildings?' Jesus replied. 'Not one stone here will be left standing on another—every single one will be thrown down.'"
    },
    "3": {
      "L": "And as he sat on the Mount of Olives opposite the temple, Peter and James and John and Andrew asked him privately,",
      "M": "As Jesus was sitting on the Mount of Olives opposite the temple, Peter, James, John and Andrew asked him privately,",
      "T": "As Jesus sat on the Mount of Olives across from the temple, Peter, James, John, and Andrew asked him privately,"
    },
    "4": {
      "L": "'Tell us, when will these things be, and what will be the sign when all these things are about to be accomplished?'",
      "M": "'Tell us, when will these things happen? And what will be the sign that they are all about to be fulfilled?'",
      "T": "'Tell us—when will all this happen? And what will be the sign that it is all about to take place?'"
    },
    "5": {
      "L": "And Jesus began to say to them, 'See that no one leads you astray.'",
      "M": "Jesus said to them: 'Watch out that no one deceives you.'",
      "T": "Jesus began to tell them: 'Be careful that no one misleads you.'"
    },
    "6": {
      "L": "'Many will come in my name, saying, \"I am he!\" and they will lead many astray.'",
      "M": "'Many will come in my name, claiming, \"I am he,\" and will deceive many.'",
      "T": "'Many will come in my name, claiming \"I am the one,\" and they will deceive many people.'"
    },
    "7": {
      "L": "'And when you hear of wars and rumors of wars, do not be alarmed. This must take place, but the end is not yet.'",
      "M": "'When you hear of wars and rumors of wars, do not be alarmed. Such things must happen, but the end is still to come.'",
      "T": "'When you hear of wars and rumors of wars, don't panic. These things must happen, but that is not yet the end.'"
    },
    "8": {
      "L": "'For nation will rise against nation, and kingdom against kingdom. There will be earthquakes in various places; there will be famines. These are but the beginning of the birth pains.'",
      "M": "'Nation will rise against nation, and kingdom against kingdom. There will be earthquakes in various places, and famines. These are the beginning of birth pains.'",
      "T": "'Nation will rise against nation, kingdom against kingdom. Earthquakes will break out in various places. There will be famines. But these are only the early contractions—the beginning of birth pains.'"
    },
    "9": {
      "L": "'But be on your guard. For they will deliver you over to councils, and you will be beaten in synagogues, and you will stand before governors and kings for my sake, to bear witness before them.'",
      "M": "'You must be on your guard. You will be handed over to the local councils and flogged in the synagogues. On account of me you will stand before governors and kings as witnesses to them.'",
      "T": "'But be alert—you will be handed over to local courts and beaten in synagogues. You will stand before governors and kings on my account, to bear witness to them.'"
    },
    "10": {
      "L": "'And the gospel must first be proclaimed to all nations.'",
      "M": "'And the gospel must first be preached to all nations.'",
      "T": "'But the good news must first be proclaimed to all nations.'"
    },
    "11": {
      "L": "'And when they bring you to trial and deliver you over, do not be anxious beforehand what you are to say, but say whatever is given you in that hour, for it is not you who speak, but the Holy Spirit.'",
      "M": "'Whenever you are arrested and brought to trial, do not worry beforehand about what to say. Just say whatever is given you at the time, for it is not you speaking, but the Holy Spirit.'",
      "T": "'When they arrest you and bring you to trial, don't worry in advance about what to say. Say whatever is given you in that moment—because it is not you speaking, but the Holy Spirit.'"
    },
    "12": {
      "L": "'And brother will deliver brother over to death, and the father his child, and children will rise against parents and have them put to death.'",
      "M": "'Brother will betray brother to death, and a father his child. Children will rebel against their parents and have them put to death.'",
      "T": "'Brother will hand over brother to be killed, and a father his child. Children will rise against their parents and have them executed.'"
    },
    "13": {
      "L": "'And you will be hated by all for my name's sake. But the one who endures to the end will be saved.'",
      "M": "'Everyone will hate you because of me, but the one who stands firm to the end will be saved.'",
      "T": "'You will be hated by everyone on my account. But the one who holds on to the end will be rescued.'"
    },
    "14": {
      "L": "'But when you see the abomination of desolation standing where he ought not to be (let the reader understand), then let those who are in Judea flee to the mountains.'",
      "M": "'When you see \"the abomination that causes desolation\" standing where it does not belong—let the reader understand—then let those who are in Judea flee to the mountains.'",
      "T": "'When you see \"the abomination that causes desolation\" standing where it must not stand—the reader must understand—then those in Judea must flee to the mountains.'"
    },
    "15": {
      "L": "'Let the one who is on the housetop not go down, nor enter his house, to take anything out,'",
      "M": "'Let no one on the housetop go down or enter the house to take anything out.'",
      "T": "'Let no one on the rooftop go back inside or stop to take anything out.'"
    },
    "16": {
      "L": "'and let the one who is in the field not turn back to take his cloak.'",
      "M": "'Let no one in the field go back to get their cloak.'",
      "T": "'Let no one in the field go back to get their coat.'"
    },
    "17": {
      "L": "'And alas for women who are pregnant and for those who are nursing infants in those days!'",
      "M": "'How dreadful it will be in those days for pregnant women and nursing mothers!'",
      "T": "'How terrible it will be in those days for women who are pregnant or nursing!'"
    },
    "18": {
      "L": "'Pray that it may not happen in winter.'",
      "M": "'Pray that this will not take place in winter,'",
      "T": "'Pray that this doesn't happen in winter.'"
    },
    "19": {
      "L": "'For in those days there will be such tribulation as has not been from the beginning of the creation that God created until now, and never will be.'",
      "M": "'because those will be days of distress unequaled from the beginning, when God created the world, until now—and never to be equaled again.'",
      "T": "'because those will be days of suffering unlike anything since God first created the world—and nothing like it will ever happen again.'"
    },
    "20": {
      "L": "'And if the Lord had not cut short the days, no human being would be saved. But for the sake of the elect, whom he chose, he shortened the days.'",
      "M": "'If the Lord had not cut short those days, no one would survive. But for the sake of the elect, whom he has chosen, he has shortened them.'",
      "T": "'If the Lord had not cut those days short, no one would survive. But for the sake of his chosen ones, he has shortened them.'"
    },
    "21": {
      "L": "'And then if anyone says to you, \"Look, here is the Christ!\" or \"Look, there he is!\" do not believe it.'",
      "M": "'At that time if anyone says to you, \"Look, here is the Messiah!\" or, \"Look, there he is!\" do not believe it.'",
      "T": "'If anyone says to you then, \"Look—here is the Messiah!\" or \"There he is!\"—don't believe them.'"
    },
    "22": {
      "L": "'For false christs and false prophets will arise and perform signs and wonders, to lead astray, if possible, the elect.'",
      "M": "'For false messiahs and false prophets will appear and perform signs and wonders to deceive, if possible, even the elect.'",
      "T": "'For false messiahs and false prophets will appear and perform miraculous signs and wonders in order to deceive, if it were possible, even God's chosen ones.'"
    },
    "23": {
      "L": "'But be on guard; I have told you all things beforehand.'",
      "M": "'So be on your guard; I have told you everything ahead of time.'",
      "T": "'But be alert—I have warned you about everything in advance.'"
    },
    "24": {
      "L": "'But in those days, after that tribulation, the sun will be darkened, and the moon will not give its light,'",
      "M": "'But in those days, following that distress, \"the sun will be darkened, and the moon will not give its light;'",
      "T": "'But in those days, after that time of suffering, the sun will be darkened and the moon will give no light;'"
    },
    "25": {
      "L": "'and the stars will be falling from heaven, and the powers in the heavens will be shaken.'",
      "M": "'the stars will fall from the sky, and the heavenly bodies will be shaken.'\"'",
      "T": "'the stars will fall from the sky, and the powers in the heavens will be shaken.'"
    },
    "26": {
      "L": "'And then they will see the Son of Man coming in clouds with great power and glory.'",
      "M": "'At that time people will see the Son of Man coming in clouds with great power and glory.'",
      "T": "'Then they will see the Son of Man coming on the clouds with great power and glory.'"
    },
    "27": {
      "L": "'And then he will send out the angels and gather his elect from the four winds, from the ends of the earth to the ends of heaven.'",
      "M": "'And he will send his angels and gather his elect from the four winds, from the ends of the earth to the ends of the heavens.'",
      "T": "'And then he will send out his angels and gather his chosen ones from the four winds, from the farthest ends of earth to the farthest ends of heaven.'"
    },
    "28": {
      "L": "'From the fig tree learn its lesson: as soon as its branch becomes tender and puts out its leaves, you know that summer is near.'",
      "M": "'Now learn this lesson from the fig tree: As soon as its twigs get tender and its leaves come out, you know that summer is near.'",
      "T": "'Learn a lesson from the fig tree: the moment its branches grow tender and sprout leaves, you know summer is coming.'"
    },
    "29": {
      "L": "'So also, when you see these things taking place, you know that he is near, at the very gates.'",
      "M": "'Even so, when you see these things happening, you know that it is near, right at the door.'",
      "T": "'In the same way, when you see these things happening, you know the time is close—right at the door.'"
    },
    "30": {
      "L": "'Truly, I say to you, this generation will not pass away until all these things take place.'",
      "M": "'Truly I tell you, this generation will certainly not pass away until all these things have happened.'",
      "T": "'I tell you the truth: this generation will not pass away before all these things take place.'"
    },
    "31": {
      "L": "'Heaven and earth will pass away, but my words will not pass away.'",
      "M": "'Heaven and earth will pass away, but my words will never pass away.'",
      "T": "'The sky and the earth will vanish—but my words will never disappear.'"
    },
    "32": {
      "L": "'But concerning that day or that hour, no one knows, not even the angels in heaven, nor the Son, but only the Father.'",
      "M": "'But about that day or hour no one knows, not even the angels in heaven, nor the Son, but only the Father.'",
      "T": "'But no one knows the day or the hour—not the angels in heaven, not even the Son—only the Father knows.'"
    },
    "33": {
      "L": "'Be on guard, keep awake. For you do not know when the time will come.'",
      "M": "'Be on guard! Be alert! You do not know when that time will come.'",
      "T": "'Stay alert! Stay watchful! You don't know when that time will come.'"
    },
    "34": {
      "L": "'It is like a man going on a journey, when he leaves home and puts his servants in charge, each with his work, and commands the doorkeeper to stay awake.'",
      "M": "'It's like a man going away: He leaves his house and puts his servants in charge, each with their assigned task, and tells the one at the door to keep watch.'",
      "T": "'It's like a man who went on a journey. He left home, put his servants in charge with each assigned their responsibilities, and told the doorkeeper to stay on watch.'"
    },
    "35": {
      "L": "'Therefore stay awake—for you do not know when the master of the house will come, in the evening, or at midnight, or when the rooster crows, or in the morning—'",
      "M": "'Therefore keep watch because you do not know when the owner of the house will come back—whether in the evening, or at midnight, or when the rooster crows, or at dawn.'",
      "T": "'So keep watch! You don't know when the master of the house will come back—whether at evening, midnight, when the rooster crows, or at dawn—'"
    },
    "36": {
      "L": "'lest he come suddenly and find you asleep.'",
      "M": "'If he comes suddenly, do not let him find you sleeping.'",
      "T": "'in case he comes suddenly and finds you sleeping.'"
    },
    "37": {
      "L": "'And what I say to you I say to all: Stay awake.'",
      "M": "'What I say to you, I say to everyone: \"Watch!\"'",
      "T": "'What I'm telling you, I'm telling everyone: Stay awake!'"
    }
  },
  "14": {
    "1": {
      "L": "It was now two days before the Passover and the Feast of Unleavened Bread. And the chief priests and the scribes were seeking how to arrest him by stealth and kill him,",
      "M": "Now the Passover and the Festival of Unleavened Bread were only two days away, and the chief priests and the teachers of the law were scheming to arrest Jesus secretly and kill him.",
      "T": "The Passover and the Festival of Unleavened Bread were two days away. The chief priests and the Bible teachers were scheming how to arrest Jesus secretly and kill him."
    },
    "2": {
      "L": "for they said, 'Not during the feast, lest there be an uproar from the people.'",
      "M": "'But not during the festival,' they said, 'or the people may riot.'",
      "T": "'But not during the festival,' they said, 'or the people might riot.'"
    },
    "3": {
      "L": "And while he was at Bethany in the house of Simon the leper, as he was reclining at table, a woman came with an alabaster flask of ointment of pure nard, very costly, and she broke the flask and poured it over his head.",
      "M": "While he was in Bethany, reclining at the table in the home of Simon the Leper, a woman came with an alabaster jar of very expensive perfume, made of pure nard. She broke the jar and poured the perfume on his head.",
      "T": "While Jesus was at Bethany reclining at the table in the home of Simon the Leper, a woman came in with an alabaster flask of very expensive perfume made from pure nard. She broke the flask and poured it over his head."
    },
    "4": {
      "L": "There were some who said to themselves indignantly, 'Why was the ointment wasted like that?'",
      "M": "Some of those present were saying indignantly to one another, 'Why this waste of perfume?'",
      "T": "Some of those present were angry and grumbled: 'Why this waste of expensive perfume?'"
    },
    "5": {
      "L": "'For this ointment could have been sold for more than three hundred denarii and given to the poor.' And they scolded her.",
      "M": "'It could have been sold for more than a year's wages and the money given to the poor.' And they rebuked her harshly.",
      "T": "'It could have been sold for more than a year's wages and the money given to the poor!' And they turned on her angrily."
    },
    "6": {
      "L": "But Jesus said, 'Leave her alone. Why do you trouble her? She has done a beautiful thing to me.'",
      "M": "'Leave her alone,' said Jesus. 'Why are you bothering her? She has done a beautiful thing to me.'",
      "T": "'Leave her alone,' Jesus said. 'Why are you upsetting her? She has done something beautiful for me.'"
    },
    "7": {
      "L": "'For you always have the poor with you, and whenever you want, you can do good for them. But you will not always have me.'",
      "M": "'The poor you will always have with you, and you can help them any time you want. But you will not always have me.'",
      "T": "'The poor will always be with you—you can help them whenever you choose. But you will not always have me.'"
    },
    "8": {
      "L": "'She has done what she could; she has anointed my body beforehand for burial.'",
      "M": "'She did what she could. She poured perfume on my body beforehand to prepare for my burial.'",
      "T": "'She did what she could. She has anointed my body ahead of time for burial.'"
    },
    "9": {
      "L": "'And truly, I say to you, wherever the gospel is proclaimed in the whole world, what she has done will be told in memory of her.'",
      "M": "'Truly I tell you, wherever the gospel is preached throughout the world, what she has done will also be told, in memory of her.'",
      "T": "'I tell you the truth: wherever the good news is proclaimed throughout the whole world, what this woman has done will be told in her memory.'"
    },
    "10": {
      "L": "Then Judas Iscariot, who was one of the twelve, went to the chief priests in order to betray him to them.",
      "M": "Then Judas Iscariot, one of the Twelve, went to the chief priests to betray Jesus to them.",
      "T": "Then Judas Iscariot, one of the Twelve, went to the chief priests to hand Jesus over to them."
    },
    "11": {
      "L": "And when they heard it, they were glad and promised to give him money. And he sought an opportunity to betray him.",
      "M": "They were delighted to hear this and promised to give him money. So he watched for an opportunity to hand him over.",
      "T": "When they heard it, they were delighted and promised to pay him. He began looking for the right moment to betray Jesus."
    },
    "12": {
      "L": "And on the first day of Unleavened Bread, when they sacrificed the Passover lamb, his disciples said to him, 'Where will you have us go and prepare for you to eat the Passover?'",
      "M": "On the first day of the Festival of Unleavened Bread, when it was customary to sacrifice the Passover lamb, Jesus' disciples asked him, 'Where do you want us to go and make preparations for you to eat the Passover?'",
      "T": "On the first day of the Festival of Unleavened Bread, when the Passover lamb was sacrificed, his disciples asked him, 'Where do you want us to go and prepare the Passover meal for you?'"
    },
    "13": {
      "L": "And he sent two of his disciples and said to them, 'Go into the city, and a man carrying a jar of water will meet you. Follow him,'",
      "M": "So he sent two of his disciples, telling them, 'Go into the city, and a man carrying a jar of water will meet you. Follow him.'",
      "T": "He sent two of his disciples and told them, 'Go into the city. A man carrying a water jar will meet you—follow him.'"
    },
    "14": {
      "L": "'and wherever he enters, say to the master of the house, \"The Teacher says, Where is my guest room, where I may eat the Passover with my disciples?\"'",
      "M": "'Say to the owner of the house he enters, \"The Teacher asks: Where is my guest room, where I may eat the Passover with my disciples?\"'",
      "T": "'Say to the owner of the house he enters: \"The Teacher asks: Where is the room where I can eat the Passover with my disciples?\"'"
    },
    "15": {
      "L": "'And he will show you a large upper room furnished and ready; there prepare for us.'",
      "M": "'He will show you a large room upstairs, furnished and ready. Make preparations for us there.'",
      "T": "'He will take you upstairs and show you a large room, already furnished and ready. Prepare the meal there for us.'"
    },
    "16": {
      "L": "And the disciples set out and went to the city and found it just as he had told them, and they prepared the Passover.",
      "M": "The disciples left, went into the city and found things just as Jesus had told them. So they prepared the Passover.",
      "T": "The disciples left, went into the city, and found everything just as Jesus had said. So they prepared the Passover meal."
    },
    "17": {
      "L": "And when it was evening, he came with the twelve.",
      "M": "When evening came, Jesus arrived with the Twelve.",
      "T": "When evening came, Jesus arrived with the Twelve."
    },
    "18": {
      "L": "And as they were reclining at table and eating, Jesus said, 'Truly, I say to you, one of you will betray me, one who is eating with me.'",
      "M": "While they were reclining at the table eating, he said, 'Truly I tell you, one of you will betray me—one who is eating with me.'",
      "T": "While they were reclining at table and eating, Jesus said, 'I tell you the truth: one of you is going to betray me—someone who is eating with me right now.'"
    },
    "19": {
      "L": "They began to be sorrowful and to say to him one after another, 'Is it I?'",
      "M": "They were saddened, and one by one they said to him, 'Surely you don't mean me?'",
      "T": "They were deeply grieved and began asking one by one, 'Surely not me?'"
    },
    "20": {
      "L": "He said to them, 'It is one of the twelve, one who is dipping bread into the dish with me.'",
      "M": "'It is one of the Twelve,' he replied, 'one who dips bread into the bowl with me.'",
      "T": "'It is one of the Twelve,' he said, 'one who is dipping his bread in the bowl with me.'"
    },
    "21": {
      "L": "'For the Son of Man goes as it is written of him, but woe to that man by whom the Son of Man is betrayed! It would have been better for that man if he had not been born.'",
      "M": "'The Son of Man will go just as it is written about him. But woe to that man who betrays the Son of Man! It would be better for him if he had not been born.'",
      "T": "'The Son of Man goes as it is written about him—but woe to the man who hands him over! It would have been better for that man if he had never been born.'"
    },
    "22": {
      "L": "And as they were eating, he took bread, and after blessing it broke it and gave it to them, and said, 'Take; this is my body.'",
      "M": "While they were eating, Jesus took bread, and when he had given thanks, he broke it and gave it to his disciples, saying, 'Take it; this is my body.'",
      "T": "As they were eating, Jesus took bread. He gave thanks, broke it, gave it to them, and said, 'Take it—this is my body.'"
    },
    "23": {
      "L": "And he took a cup, and when he had given thanks he gave it to them, and they all drank of it.",
      "M": "Then he took a cup, and when he had given thanks, he gave it to them, and they all drank from it.",
      "T": "Then he took a cup. He gave thanks and gave it to them, and they all drank from it."
    },
    "24": {
      "L": "And he said to them, 'This is my blood of the covenant, which is poured out for many.'",
      "M": "'This is my blood of the covenant, which is poured out for many,' he said to them.",
      "T": "He said to them, 'This is my blood of the covenant, which is poured out for many.'"
    },
    "25": {
      "L": "'Truly, I say to you, I will not drink again of the fruit of the vine until that day when I drink it new in the kingdom of God.'",
      "M": "'Truly I tell you, I will not drink again from the fruit of the vine until that day when I drink it new in the kingdom of God.'",
      "T": "'I tell you the truth: I will not drink wine again until the day I drink it—new—in God's kingdom.'"
    },
    "26": {
      "L": "And when they had sung a hymn, they went out to the Mount of Olives.",
      "M": "When they had sung a hymn, they went out to the Mount of Olives.",
      "T": "After singing a hymn, they went out to the Mount of Olives."
    },
    "27": {
      "L": "And Jesus said to them, 'You will all fall away, for it is written, \"I will strike the shepherd, and the sheep will be scattered.\"'",
      "M": "'You will all fall away,' Jesus told them, 'for it is written: \"I will strike the shepherd, and the sheep will be scattered.\"'",
      "T": "Jesus told them, 'You will all abandon me—for it is written: \"I will strike the shepherd, and the sheep will be scattered.\"'"
    },
    "28": {
      "L": "'But after I am raised up, I will go before you to Galilee.'",
      "M": "'But after I have risen, I will go ahead of you into Galilee.'",
      "T": "'But after I am raised, I will go ahead of you to Galilee.'"
    },
    "29": {
      "L": "Peter said to him, 'Even though they all fall away, I will not.'",
      "M": "Peter declared, 'Even if all fall away, I will not.'",
      "T": "Peter declared, 'Even if everyone else abandons you—I will not.'"
    },
    "30": {
      "L": "And Jesus said to him, 'Truly, I say to you, this very night, before the rooster crows twice, you will deny me three times.'",
      "M": "'Truly I tell you,' Jesus answered, 'today—yes, tonight—before the rooster crows twice you yourself will disown me three times.'",
      "T": "Jesus replied, 'I tell you the truth: tonight, before the rooster crows twice, you yourself will deny me three times.'"
    },
    "31": {
      "L": "But he said emphatically, 'If I must die with you, I will not deny you.' And they all said the same.",
      "M": "But Peter insisted emphatically, 'Even if I have to die with you, I will never disown you.' And all the others said the same.",
      "T": "But Peter insisted all the more emphatically, 'Even if I have to die with you, I will never deny you!' And all the others said the same."
    },
    "32": {
      "L": "And they went to a place called Gethsemane. And he said to his disciples, 'Sit here while I pray.'",
      "M": "They went to a place called Gethsemane, and Jesus said to his disciples, 'Sit here while I pray.'",
      "T": "They came to a place called Gethsemane, and Jesus said to his disciples, 'Sit here while I pray.'"
    },
    "33": {
      "L": "And he took with him Peter and James and John, and began to be greatly distressed and troubled.",
      "M": "He took Peter, James and John along with him, and he began to be deeply distressed and troubled.",
      "T": "He took Peter, James, and John with him, and began to be overcome with deep distress and anguish."
    },
    "34": {
      "L": "And he said to them, 'My soul is very sorrowful, even to death. Remain here and watch.'",
      "M": "'My soul is overwhelmed with sorrow to the point of death,' he said to them. 'Stay here and keep watch.'",
      "T": "He said to them, 'My soul is crushed with grief—even to the point of death. Stay here and keep watch.'"
    },
    "35": {
      "L": "And going a little farther, he fell on the ground and prayed that, if it were possible, the hour might pass from him.",
      "M": "Going a little farther, he fell to the ground and prayed that if possible the hour might pass from him.",
      "T": "He went a little farther, fell to the ground, and prayed that if it were possible, this hour might be taken from him."
    },
    "36": {
      "L": "And he said, 'Abba, Father, all things are possible for you. Remove this cup from me. Yet not what I will, but what you will.'",
      "M": "'Abba, Father,' he said, 'everything is possible for you. Take this cup from me. Yet not what I will, but what you will.'",
      "T": "'Abba, Father,' he said, 'all things are possible for you. Take this cup from me. But not what I want—what you want.'"
    },
    "37": {
      "L": "And he came and found them sleeping, and he said to Peter, 'Simon, are you asleep? Could you not watch one hour?'",
      "M": "Then he returned to his disciples and found them sleeping. 'Simon,' he said to Peter, 'are you asleep? Couldn't you keep watch for one hour?'",
      "T": "He came back and found them asleep. He said to Peter, 'Simon, are you sleeping? Couldn't you stay awake for even one hour?'"
    },
    "38": {
      "L": "'Watch and pray that you may not enter into temptation. The spirit indeed is willing, but the flesh is weak.'",
      "M": "'Watch and pray so that you will not fall into temptation. The spirit is willing, but the flesh is weak.'",
      "T": "'Stay awake and pray so that you don't fall into temptation. The spirit wants to, but the body is weak.'"
    },
    "39": {
      "L": "And again he went away and prayed, saying the same words.",
      "M": "Once more he went away and prayed the same thing.",
      "T": "He went away again and prayed the same prayer."
    },
    "40": {
      "L": "And again he came and found them sleeping, for their eyes were very heavy, and they did not know what to answer him.",
      "M": "When he came back, he again found them sleeping, because their eyes were heavy. They did not know what to say to him.",
      "T": "He came back and again found them asleep—their eyes were heavy. They didn't know what to say to him."
    },
    "41": {
      "L": "And he came the third time and said to them, 'Are you still sleeping and taking your rest? It is enough; the hour has come. The Son of Man is betrayed into the hands of sinners.'",
      "M": "Returning the third time, he said to them, 'Are you still sleeping and resting? Enough! The hour has come. Look, the Son of Man is delivered into the hands of sinners.'",
      "T": "He came a third time and said, 'Are you still sleeping and resting? Enough! The hour has come. Look—the Son of Man is being handed over to sinners.'"
    },
    "42": {
      "L": "'Rise, let us be going; see, my betrayer is at hand.'",
      "M": "'Rise! Let us go! Here comes my betrayer!'",
      "T": "'Get up! Let's go! Here comes my betrayer!'"
    },
    "43": {
      "L": "And immediately, while he was still speaking, Judas came, one of the twelve, and with him a crowd with swords and clubs, from the chief priests and the scribes and the elders.",
      "M": "Just as he was speaking, Judas, one of the Twelve, appeared. With him was a crowd armed with swords and clubs, sent from the chief priests, the teachers of the law, and the elders.",
      "T": "While he was still speaking, Judas—one of the Twelve—arrived. With him came a crowd armed with swords and clubs, sent from the chief priests, the Bible teachers, and the elders."
    },
    "44": {
      "L": "Now the betrayer had given them a sign, saying, 'The one I will kiss is the man. Seize him and lead him away under guard.'",
      "M": "Now the betrayer had arranged a signal with them: 'The one I kiss is the man; arrest him and lead him away under guard.'",
      "T": "The betrayer had given them a prearranged signal: 'The one I kiss—that's the man. Arrest him and take him away securely.'"
    },
    "45": {
      "L": "And when he came, he went up to him at once and said, 'Rabbi!' And he kissed him.",
      "M": "Going at once to Jesus, Judas said, 'Rabbi!' and kissed him.",
      "T": "He went straight to Jesus, said 'Rabbi!' and kissed him."
    },
    "46": {
      "L": "And they laid hands on him and seized him.",
      "M": "The men seized Jesus and arrested him.",
      "T": "The men grabbed Jesus and arrested him."
    },
    "47": {
      "L": "But one of those who stood by drew his sword and struck the servant of the high priest and cut off his ear.",
      "M": "Then one of those standing near drew his sword and struck the servant of the high priest, cutting off his ear.",
      "T": "One of those standing nearby drew his sword and struck the high priest's servant, cutting off his ear."
    },
    "48": {
      "L": "And Jesus said to them, 'Have you come out as against a robber, with swords and clubs to capture me?'",
      "M": "'Am I leading a rebellion,' said Jesus, 'that you have come out with swords and clubs to capture me?'",
      "T": "Jesus said to them, 'Have you come out with swords and clubs to arrest me as if I were an outlaw?'"
    },
    "49": {
      "L": "'Day after day I was with you in the temple teaching, and you did not seize me. But let the Scriptures be fulfilled.'",
      "M": "'Every day I was with you, teaching in the temple courts, and you did not arrest me. But the Scriptures must be fulfilled.'",
      "T": "'Day after day I sat teaching in the temple, and you didn't arrest me. But let the Scriptures be fulfilled.'"
    },
    "50": {
      "L": "And they all left him and fled.",
      "M": "Then everyone deserted him and fled.",
      "T": "Then all his disciples abandoned him and ran."
    },
    "51": {
      "L": "And a young man followed him, with nothing but a linen cloth about his body. And they seized him,",
      "M": "A young man, wearing nothing but a linen garment, was following Jesus. When they seized him,",
      "T": "A young man was following, wearing nothing but a linen cloth. When they grabbed him,"
    },
    "52": {
      "L": "but he left the linen cloth and ran away naked.",
      "M": "he fled naked, leaving his garment behind.",
      "T": "he left the cloth behind and ran away naked."
    },
    "53": {
      "L": "And they led Jesus to the high priest. And all the chief priests and the elders and the scribes came together.",
      "M": "They took Jesus to the high priest, and all the chief priests, the elders and the teachers of the law came together.",
      "T": "They led Jesus away to the high priest, where all the chief priests, elders, and Bible teachers had assembled."
    },
    "54": {
      "L": "And Peter had followed him at a distance, right into the courtyard of the high priest. And he was sitting with the guards and warming himself at the fire.",
      "M": "Peter followed him at a distance, right into the courtyard of the high priest. There he sat with the guards and warmed himself at the fire.",
      "T": "Peter followed at a distance, all the way into the courtyard of the high priest. He sat down with the guards and warmed himself at the fire."
    },
    "55": {
      "L": "Now the chief priests and the whole council were seeking testimony against Jesus to put him to death, but they found none.",
      "M": "The chief priests and the whole Sanhedrin were looking for evidence against Jesus so that they could put him to death, but they did not find any.",
      "T": "The chief priests and the whole Sanhedrin were looking for evidence against Jesus to justify a death sentence, but they couldn't find any."
    },
    "56": {
      "L": "For many bore false witness against him, but their testimony did not agree.",
      "M": "Many testified falsely against him, but their statements did not agree.",
      "T": "Many gave false testimony against him, but their stories contradicted each other."
    },
    "57": {
      "L": "And some stood up and bore false witness against him, saying,",
      "M": "Then some stood up and gave this false testimony against him:",
      "T": "Then some stood up and gave this false testimony:"
    },
    "58": {
      "L": "'We heard him say, \"I will destroy this temple that is made with hands, and in three days I will build another, not made with hands.\"'",
      "M": "'We heard him say, \"I will destroy this temple made with human hands and in three days will build another, not made with hands.\"'",
      "T": "'We heard him say, \"I will destroy this temple made by human hands, and in three days build another, not made by human hands.\"'"
    },
    "59": {
      "L": "Yet even about this their testimony did not agree.",
      "M": "Yet even then their testimony did not agree.",
      "T": "But even on this point their testimony didn't match."
    },
    "60": {
      "L": "And the high priest stood up in the midst and asked Jesus, 'Have you no answer to make? What is it that these men testify against you?'",
      "M": "Then the high priest stood up before them and asked Jesus, 'Are you not going to answer? What is this testimony that these men are bringing against you?'",
      "T": "The high priest stood up before the assembly and demanded of Jesus, 'Have you nothing to say in your defense? What about all this testimony against you?'"
    },
    "61": {
      "L": "But he remained silent and made no answer. Again the high priest asked him, 'Are you the Christ, the Son of the Blessed?'",
      "M": "But Jesus remained silent and gave no answer. Again the high priest asked him, 'Are you the Messiah, the Son of the Blessed One?'",
      "T": "Jesus remained silent and said nothing. Again the high priest asked him, 'Are you the Messiah, the Son of the Blessed One?'"
    },
    "62": {
      "L": "And Jesus said, 'I am, and you will see the Son of Man seated at the right hand of Power, and coming with the clouds of heaven.'",
      "M": "'I am,' said Jesus. 'And you will see the Son of Man sitting at the right hand of the Mighty One and coming on the clouds of heaven.'",
      "T": "'I am,' said Jesus. 'And you will see the Son of Man seated at the right hand of the Almighty, coming on the clouds of heaven.'"
    },
    "63": {
      "L": "And the high priest tore his garments and said, 'What further witnesses do we need?'",
      "M": "The high priest tore his clothes. 'Why do we need any more witnesses?' he asked.",
      "T": "The high priest tore his robes and said, 'Why do we need any more witnesses?'"
    },
    "64": {
      "L": "'You have heard his blasphemy. What is your decision?' And they all condemned him as deserving death.",
      "M": "'You have heard the blasphemy. What do you think?' They all condemned him as worthy of death.",
      "T": "'You've heard the blasphemy. What is your verdict?' They all condemned him as deserving death."
    },
    "65": {
      "L": "And some began to spit on him and to cover his face and to strike him, saying to him, 'Prophesy!' And the guards received him with blows.",
      "M": "Then some began to spit at him; they blindfolded him, struck him with their fists, and said, 'Prophesy!' And the guards took him and beat him.",
      "T": "Then some began spitting on him. They blindfolded him, hit him with their fists, and said, 'Prophesy!' And the guards slapped him around."
    },
    "66": {
      "L": "And as Peter was below in the courtyard, one of the servant girls of the high priest came,",
      "M": "While Peter was below in the courtyard, one of the servant girls of the high priest came by.",
      "T": "While Peter was down below in the courtyard, one of the high priest's servant girls came by."
    },
    "67": {
      "L": "and seeing Peter warming himself, she looked at him and said, 'You also were with the Nazarene, Jesus.'",
      "M": "When she saw Peter warming himself, she looked closely at him. 'You also were with that Nazarene, Jesus,' she said.",
      "T": "She looked closely at Peter warming himself. 'You were also with that Nazarene, Jesus,' she said."
    },
    "68": {
      "L": "But he denied it, saying, 'I neither know nor understand what you mean.' And he went out into the gateway and the rooster crowed.",
      "M": "But he denied it. 'I don't know or understand what you're talking about,' he said, and went out into the entryway. When a rooster crowed,",
      "T": "But he denied it. 'I don't know what you're talking about,' he said, and moved out to the entryway. Then a rooster crowed."
    },
    "69": {
      "L": "And the servant girl saw him and began again to say to the bystanders, 'This man is one of them.'",
      "M": "the servant girl saw him there and began again to say to those standing around, 'This fellow is one of them.'",
      "T": "When the servant girl saw him there, she again said to those standing nearby, 'This man is one of them.'"
    },
    "70": {
      "L": "But again he denied it. And after a little while the bystanders again said to Peter, 'Certainly you are one of them, for you are a Galilean.'",
      "M": "Again he denied it. After a little while, those standing near said to Peter, 'Surely you are one of them, for you are a Galilean.'",
      "T": "He denied it again. A little later those standing nearby said to Peter, 'You are definitely one of them—you're a Galilean!'"
    },
    "71": {
      "L": "But he began to invoke a curse on himself and to swear, 'I do not know this man of whom you speak.'",
      "M": "He began to call down curses, and he swore to them, 'I don't know this man you're talking about.'",
      "T": "He began to curse and swear: 'I don't know the man you're talking about!'"
    },
    "72": {
      "L": "And immediately the rooster crowed a second time. And Peter remembered how Jesus had said to him, 'Before the rooster crows twice, you will deny me three times.' And he broke down and wept.",
      "M": "Immediately the rooster crowed the second time. Then Peter remembered the word Jesus had spoken to him: 'Before the rooster crows twice you will disown me three times.' And he broke down and wept.",
      "T": "At that moment the rooster crowed a second time. Peter remembered what Jesus had said: 'Before the rooster crows twice, you will deny me three times.' And he broke down and wept."
    }
  },
  "15": {
    "1": {
      "L": "And as soon as it was morning, the chief priests held a consultation with the elders and scribes and the whole council. And they bound Jesus and led him away and delivered him over to Pilate.",
      "M": "Very early in the morning, the chief priests, with the elders, the teachers of the law and the whole Sanhedrin, made their plans. So they bound Jesus, led him away and handed him over to Pilate.",
      "T": "Very early in the morning, the chief priests, elders, Bible teachers, and the full Sanhedrin reached a decision. They bound Jesus, led him away, and handed him over to Pilate."
    },
    "2": {
      "L": "And Pilate asked him, 'Are you the King of the Jews?' And he answered him, 'You have said so.'",
      "M": "'Are you the king of the Jews?' asked Pilate. 'You have said so,' Jesus replied.",
      "T": "Pilate asked him, 'Are you the king of the Jews?' Jesus answered, 'You have said so.'"
    },
    "3": {
      "L": "And the chief priests accused him of many things.",
      "M": "The chief priests accused him of many things.",
      "T": "The chief priests brought many accusations against him."
    },
    "4": {
      "L": "And Pilate again asked him, 'Have you no answer to make? See how many charges they bring against you.'",
      "M": "So again Pilate asked him, 'Aren't you going to answer? See how many things they are accusing you of.'",
      "T": "Pilate asked him again, 'Have you nothing to say? Look at how many charges they're bringing against you!'"
    },
    "5": {
      "L": "But Jesus made no further answer, so that Pilate was amazed.",
      "M": "But Jesus still made no reply, and Pilate was amazed.",
      "T": "But Jesus still said nothing more—and Pilate was astonished."
    },
    "6": {
      "L": "Now at the feast he used to release for them one prisoner for whom they asked.",
      "M": "Now it was the custom at the festival to release a prisoner whom the people requested.",
      "T": "It was the custom at the festival to release one prisoner—whoever the crowd chose."
    },
    "7": {
      "L": "And among the rebels in prison, who had committed murder in the insurrection, there was a man called Barabbas.",
      "M": "A man called Barabbas was in prison with the insurrectionists who had committed murder in the uprising.",
      "T": "A man named Barabbas was in prison with the rebels who had committed murder during the uprising."
    },
    "8": {
      "L": "And the crowd came up and began to ask Pilate to do as he usually did for them.",
      "M": "The crowd came up and asked Pilate to do for them what he usually did.",
      "T": "The crowd came up and began asking Pilate to do what he always did for them."
    },
    "9": {
      "L": "And he answered them, saying, 'Do you want me to release for you the King of the Jews?'",
      "M": "'Do you want me to release to you the king of the Jews?' asked Pilate,",
      "T": "Pilate answered, 'Do you want me to release to you the king of the Jews?'"
    },
    "10": {
      "L": "For he perceived that it was out of envy that the chief priests had delivered him up.",
      "M": "knowing it was out of self-interest that the chief priests had handed Jesus over to him.",
      "T": "He knew it was out of envy that the chief priests had handed Jesus over."
    },
    "11": {
      "L": "But the chief priests stirred up the crowd to have him release for them Barabbas instead.",
      "M": "But the chief priests stirred up the crowd to have Pilate release Barabbas instead.",
      "T": "But the chief priests worked the crowd to get them to demand Barabbas instead."
    },
    "12": {
      "L": "And Pilate again said to them, 'Then what shall I do with the man you call the King of the Jews?'",
      "M": "'What shall I do, then, with the one you call the king of the Jews?' Pilate asked them.",
      "T": "Pilate asked them again, 'Then what should I do with the one you call the king of the Jews?'"
    },
    "13": {
      "L": "And they cried out again, 'Crucify him.'",
      "M": "'Crucify him!' they shouted.",
      "T": "'Crucify him!' they shouted."
    },
    "14": {
      "L": "And Pilate said to them, 'Why? What evil has he done?' But they shouted all the more, 'Crucify him.'",
      "M": "'Why? What crime has he committed?' asked Pilate. But they shouted all the louder, 'Crucify him!'",
      "T": "'Why?' Pilate asked. 'What crime has he committed?' But they shouted all the louder, 'Crucify him!'"
    },
    "15": {
      "L": "So Pilate, wishing to satisfy the crowd, released for them Barabbas, and having scourged Jesus, he delivered him to be crucified.",
      "M": "Wanting to satisfy the crowd, Pilate released Barabbas to them. He had Jesus flogged, and handed him over to be crucified.",
      "T": "Wanting to satisfy the crowd, Pilate released Barabbas to them. He had Jesus flogged, then handed him over to be crucified."
    },
    "16": {
      "L": "And the soldiers led him away inside the palace (that is, the governor's headquarters), and they called together the whole battalion.",
      "M": "The soldiers led Jesus away into the palace (that is, the Praetorium) and called together the whole company of soldiers.",
      "T": "The soldiers led Jesus inside the palace—the Praetorium—and called the whole battalion together."
    },
    "17": {
      "L": "And they clothed him in a purple cloak, and twisting together a crown of thorns, they put it on him.",
      "M": "They put a purple robe on him, then twisted together a crown of thorns and set it on him.",
      "T": "They put a purple robe on him, twisted together a crown of thorns, and set it on his head."
    },
    "18": {
      "L": "And they began to salute him, 'Hail, King of the Jews!'",
      "M": "And they began to call out to him, 'Hail, king of the Jews!'",
      "T": "Then they began saluting him: 'Hail, king of the Jews!'"
    },
    "19": {
      "L": "And they were striking his head with a reed and spitting on him and kneeling down in homage to him.",
      "M": "Again and again they struck him on the head with a staff and spit on him. Falling on their knees, they paid homage to him.",
      "T": "They kept striking him on the head with a stick, spitting on him, and dropping to their knees in mockery."
    },
    "20": {
      "L": "And when they had mocked him, they stripped him of the purple cloak and put his own clothes on him. And they led him out to crucify him.",
      "M": "And when they had mocked him, they took off the purple robe and put his own clothes on him. Then they led him out to crucify him.",
      "T": "When they had finished mocking him, they removed the purple robe and dressed him in his own clothes. Then they led him out to crucify him."
    },
    "21": {
      "L": "And they compelled a passerby, Simon of Cyrene, who was coming in from the country, the father of Alexander and Rufus, to carry his cross.",
      "M": "A certain man from Cyrene, Simon, the father of Alexander and Rufus, was passing by on his way in from the country, and they forced him to carry the cross.",
      "T": "A man named Simon from Cyrene—the father of Alexander and Rufus—was passing by on his way in from the countryside, and they forced him to carry the cross."
    },
    "22": {
      "L": "And they brought him to the place called Golgotha (which means Place of a Skull).",
      "M": "They brought Jesus to the place called Golgotha (which means 'the place of the skull').",
      "T": "They brought Jesus to the place called Golgotha—which means 'the Place of the Skull.'"
    },
    "23": {
      "L": "And they offered him wine mixed with myrrh, but he did not take it.",
      "M": "Then they offered him wine mixed with myrrh, but he did not take it.",
      "T": "They offered him wine mixed with myrrh, but he refused it."
    },
    "24": {
      "L": "And they crucified him and divided his garments among them, casting lots for them, to decide what each should take.",
      "M": "And they crucified him. Dividing up his clothes, they cast lots to see what each would get.",
      "T": "Then they crucified him. They divided up his clothes, casting lots to decide who would get what."
    },
    "25": {
      "L": "And it was the third hour when they crucified him.",
      "M": "It was nine in the morning when they crucified him.",
      "T": "It was nine in the morning when they crucified him."
    },
    "26": {
      "L": "And the inscription of the charge against him read, 'The King of the Jews.'",
      "M": "The written notice of the charge against him read: THE KING OF THE JEWS.",
      "T": "The written notice of the charge against him read: THE KING OF THE JEWS."
    },
    "27": {
      "L": "And with him they crucified two robbers, one on his right and one on his left.",
      "M": "They crucified two rebels with him, one on his right and one on his left.",
      "T": "They crucified two insurgents with him—one on his right, one on his left."
    },
    "29": {
      "L": "And those who passed by derided him, wagging their heads and saying, 'Aha! You who would destroy the temple and rebuild it in three days,'",
      "M": "Those who passed by hurled insults at him, shaking their heads and saying, 'So! You who are going to destroy the temple and build it in three days,'",
      "T": "Those passing by hurled insults at him, shaking their heads: 'Ha! You were going to destroy the temple and rebuild it in three days—'"
    },
    "30": {
      "L": "'save yourself, and come down from the cross!'",
      "M": "'come down from the cross and save yourself!'",
      "T": "'save yourself and come down from the cross!'"
    },
    "31": {
      "L": "So also the chief priests with the scribes mocked him to one another, saying, 'He saved others; he cannot save himself.'",
      "M": "In the same way the chief priests and the teachers of the law mocked him among themselves. 'He saved others,' they said, 'but he can't save himself!'",
      "T": "The chief priests and Bible teachers mocked him among themselves: 'He saved others—but he can't save himself!'"
    },
    "32": {
      "L": "'Let the Christ, the King of Israel, come down now from the cross that we may see and believe.' Those who were crucified with him also reviled him.",
      "M": "'Let this Messiah, this king of Israel, come down now from the cross, that we may see and believe.' Those crucified with him also heaped insults on him.",
      "T": "'Let this Messiah, this king of Israel, come down now from the cross so we can see and believe!' Even those crucified with him heaped insults on him."
    },
    "33": {
      "L": "And when the sixth hour had come, there was darkness over the whole land until the ninth hour.",
      "M": "At noon, darkness came over the whole land until three in the afternoon.",
      "T": "At noon, darkness came over the whole land and lasted until three in the afternoon."
    },
    "34": {
      "L": "And at the ninth hour Jesus cried with a loud voice, 'Eloi, Eloi, lema sabachthani?' which means, 'My God, my God, why have you forsaken me?'",
      "M": "And at three in the afternoon Jesus cried out in a loud voice, 'Eloi, Eloi, lema sabachthani?' (which means 'My God, my God, why have you forsaken me?').",
      "T": "At three in the afternoon Jesus cried out with a loud voice: 'Eloi, Eloi, lema sabachthani?'—which means, 'My God, my God, why have you forsaken me?'"
    },
    "35": {
      "L": "And some of the bystanders hearing it said, 'Behold, he is calling Elijah.'",
      "M": "When some of those standing near heard this, they said, 'Listen, he's calling Elijah.'",
      "T": "When some of those standing nearby heard it, they said, 'Listen—he's calling on Elijah!'"
    },
    "36": {
      "L": "And someone ran and filled a sponge with sour wine, put it on a reed and gave it to him to drink, saying, 'Wait, let us see whether Elijah will come to take him down.'",
      "M": "Someone ran, filled a sponge with wine vinegar, put it on a staff, and offered it to Jesus to drink. 'Now leave him alone. Let's see if Elijah comes to take him down,' he said.",
      "T": "Someone ran, soaked a sponge in wine vinegar, put it on a stick, and offered it to Jesus to drink. 'Let's see if Elijah comes to take him down,' he said."
    },
    "37": {
      "L": "And Jesus uttered a loud cry and breathed his last.",
      "M": "With a loud cry, Jesus breathed his last.",
      "T": "With a loud cry, Jesus breathed his last."
    },
    "38": {
      "L": "And the curtain of the temple was torn in two, from top to bottom.",
      "M": "The curtain of the temple was torn in two from top to bottom.",
      "T": "The curtain of the temple was torn in two, from top to bottom."
    },
    "39": {
      "L": "And when the centurion, who stood facing him, saw that in this way he breathed his last, he said, 'Truly this man was the Son of God!'",
      "M": "And when the centurion, who stood there in front of Jesus, saw how he died, he said, 'Surely this man was the Son of God!'",
      "T": "When the Roman centurion standing there in front of Jesus saw how he died, he said, 'This man truly was the Son of God!'"
    },
    "40": {
      "L": "There were also women watching from a distance, among whom were Mary Magdalene, and Mary the mother of James the younger and of Joses, and Salome.",
      "M": "Some women were watching from a distance. Among them were Mary Magdalene, Mary the mother of James the younger and of Joseph, and Salome.",
      "T": "Some women were watching from a distance. Among them were Mary Magdalene, Mary the mother of James the younger and of Joses, and Salome."
    },
    "41": {
      "L": "When he was in Galilee, they followed him and ministered to him, and there were also many other women who came up with him to Jerusalem.",
      "M": "In Galilee these women had followed him and cared for his needs. Many other women who had come up with him to Jerusalem were also there.",
      "T": "When he was in Galilee, these women had followed him and cared for him. Many other women had also come up with him to Jerusalem."
    },
    "42": {
      "L": "And when evening had come, since it was the day of Preparation, that is, the day before the Sabbath,",
      "M": "It was Preparation Day (that is, the day before the Sabbath). So as evening approached,",
      "T": "It was Preparation Day—the day before the Sabbath. As evening approached,"
    },
    "43": {
      "L": "Joseph of Arimathea, a respected member of the council, who was also himself looking for the kingdom of God, took courage and went to Pilate and asked for the body of Jesus.",
      "M": "Joseph of Arimathea, a prominent member of the Council, who was himself waiting for the kingdom of God, went boldly to Pilate and asked for Jesus' body.",
      "T": "Joseph of Arimathea—a respected member of the Sanhedrin who was also waiting for God's kingdom—went boldly to Pilate and asked for the body of Jesus."
    },
    "44": {
      "L": "Pilate was surprised to hear that he should have already died. And summoning the centurion, he asked him whether he was already dead.",
      "M": "Pilate was surprised to hear that he was already dead. Summoning the centurion, he asked him if Jesus had already died.",
      "T": "Pilate was surprised to hear that Jesus was already dead. He summoned the centurion and asked whether he had been dead long."
    },
    "45": {
      "L": "And when he learned from the centurion that he was dead, he granted the corpse to Joseph.",
      "M": "When he learned from the centurion that it was so, he gave the body to Joseph.",
      "T": "When he confirmed it with the centurion, he released the body to Joseph."
    },
    "46": {
      "L": "And Joseph bought a linen shroud, and taking him down, wrapped him in the linen shroud and laid him in a tomb that had been cut out of the rock. And he rolled a stone against the entrance of the tomb.",
      "M": "So Joseph bought some linen cloth, took down the body, wrapped it in the linen, and placed it in a tomb cut out of rock. Then he rolled a stone against the entrance of the tomb.",
      "T": "Joseph bought a linen cloth, took the body down, wrapped it in the linen, and laid it in a tomb cut from rock. Then he rolled a stone across the entrance."
    },
    "47": {
      "L": "Mary Magdalene and Mary the mother of Joses saw where he was laid.",
      "M": "Mary Magdalene and Mary the mother of Joseph saw where he was laid.",
      "T": "Mary Magdalene and Mary the mother of Joses saw where he was laid."
    }
  },
  "16": {
    "1": {
      "L": "When the Sabbath was past, Mary Magdalene, Mary the mother of James, and Salome bought spices, so that they might go and anoint him.",
      "M": "When the Sabbath was over, Mary Magdalene, Mary the mother of James, and Salome bought spices so that they might go to anoint Jesus' body.",
      "T": "After the Sabbath was over, Mary Magdalene, Mary the mother of James, and Salome bought aromatic spices so they could go and anoint Jesus' body."
    },
    "2": {
      "L": "And very early on the first day of the week, when the sun had risen, they went to the tomb.",
      "M": "Very early on the first day of the week, just after sunrise, they were on their way to the tomb",
      "T": "Very early on the first day of the week, just after sunrise, they went to the tomb."
    },
    "3": {
      "L": "And they were saying to one another, 'Who will roll away the stone for us from the entrance of the tomb?'",
      "M": "and they asked each other, 'Who will roll the stone away from the entrance of the tomb?'",
      "T": "They were asking each other, 'Who will roll away the stone from the entrance of the tomb?'"
    },
    "4": {
      "L": "And looking up, they saw that the stone had been rolled back—it was very large.",
      "M": "But when they looked up, they saw that the stone, which was very large, had been rolled away.",
      "T": "But when they looked up, they saw that the stone—which was enormous—had already been rolled away."
    },
    "5": {
      "L": "And entering the tomb, they saw a young man sitting on the right side, dressed in a white robe, and they were alarmed.",
      "M": "As they entered the tomb, they saw a young man dressed in a white robe sitting on the right side, and they were alarmed.",
      "T": "When they entered the tomb, they saw a young man dressed in a white robe sitting on the right side—and they were overwhelmed with fear."
    },
    "6": {
      "L": "And he said to them, 'Do not be alarmed. You seek Jesus of Nazareth, who was crucified. He has risen; he is not here. See the place where they laid him.'",
      "M": "'Don't be alarmed,' he said. 'You are looking for Jesus the Nazarene, who was crucified. He has risen! He is not here. See the place where they laid him.'",
      "T": "'Don't be afraid,' he said. 'You're looking for Jesus of Nazareth, who was crucified. He is risen! He is not here—see the place where they laid him.'"
    },
    "7": {
      "L": "'But go, tell his disciples and Peter that he is going before you to Galilee. There you will see him, just as he told you.'",
      "M": "'But go, tell his disciples and Peter, \"He is going ahead of you into Galilee. There you will see him, just as he told you.\"'",
      "T": "'But go and tell his disciples—and Peter—that he is going ahead of you to Galilee. You will see him there, just as he told you.'"
    },
    "8": {
      "L": "And they went out and fled from the tomb, for trembling and astonishment had seized them, and they said nothing to anyone, for they were afraid.",
      "M": "Trembling and bewildered, the women went out and fled from the tomb. They said nothing to anyone, because they were afraid.",
      "T": "They fled from the tomb, trembling and overcome with astonishment. They said nothing to anyone—they were too afraid."
    },
    "9": {
      "L": "Now when he rose early on the first day of the week, he appeared first to Mary Magdalene, from whom he had cast out seven demons.",
      "M": "When Jesus rose early on the first day of the week, he appeared first to Mary Magdalene, out of whom he had driven seven demons.",
      "T": "After Jesus rose early on the first day of the week, he appeared first to Mary Magdalene, from whom he had driven out seven demons."
    },
    "10": {
      "L": "She went and told those who had been with him, as they mourned and wept.",
      "M": "She went and told those who had been with him and who were mourning and weeping.",
      "T": "She went and told those who had been with him—who were weeping and grieving."
    },
    "11": {
      "L": "But when they heard that he was alive and had been seen by her, they would not believe it.",
      "M": "When they heard that Jesus was alive and that she had seen him, they did not believe it.",
      "T": "When they heard that he was alive and that she had seen him, they didn't believe it."
    },
    "12": {
      "L": "After these things he appeared in another form to two of them, as they were walking into the country.",
      "M": "Afterward Jesus appeared in a different form to two of them while they were walking in the country.",
      "T": "Afterward he appeared in a different form to two of them as they were walking in the countryside."
    },
    "13": {
      "L": "And they went back and told the rest, but they did not believe them either.",
      "M": "These returned and reported it to the rest; but they did not believe them either.",
      "T": "They went back and told the others—but they didn't believe them either."
    },
    "14": {
      "L": "Afterward he appeared to the eleven themselves as they were reclining at table, and he rebuked their unbelief and hardness of heart, because they had not believed those who saw him after he had risen.",
      "M": "Later Jesus appeared to the Eleven as they were eating; he rebuked them for their lack of faith and their stubborn refusal to believe those who had seen him after he had risen.",
      "T": "Later Jesus appeared to the Eleven while they were eating. He rebuked them for their unbelief and stubborn hearts, because they had refused to believe those who had seen him risen."
    },
    "15": {
      "L": "And he said to them, 'Go into all the world and proclaim the gospel to the whole creation.'",
      "M": "He said to them, 'Go into all the world and preach the gospel to all creation.'",
      "T": "He said to them, 'Go into all the world and proclaim the good news to every creature.'"
    },
    "16": {
      "L": "'Whoever believes and is baptized will be saved, but whoever does not believe will be condemned.'",
      "M": "'Whoever believes and is baptized will be saved, but whoever does not believe will be condemned.'",
      "T": "'Whoever believes and is baptized will be rescued—but whoever refuses to believe will be condemned.'"
    },
    "17": {
      "L": "'And these signs will accompany those who believe: in my name they will cast out demons; they will speak in new tongues;'",
      "M": "'And these signs will accompany those who believe: In my name they will drive out demons; they will speak in new tongues;'",
      "T": "'And these miraculous signs will accompany those who believe: In my name they will drive out demons; they will speak in new languages;'"
    },
    "18": {
      "L": "'they will pick up serpents with their hands; and if they drink any deadly poison, it will not hurt them; they will lay their hands on the sick, and they will recover.'",
      "M": "'they will pick up snakes with their hands; and when they drink deadly poison, it will not hurt them at all; they will place their hands on sick people, and they will get well.'",
      "T": "'they will handle snakes safely; and if they drink any deadly poison, it will not harm them; they will lay hands on the sick, and the sick will recover.'"
    },
    "19": {
      "L": "So then the Lord Jesus, after he had spoken to them, was taken up into heaven and sat down at the right hand of God.",
      "M": "After the Lord Jesus had spoken to them, he was taken up into heaven and he sat at the right hand of God.",
      "T": "After the Lord Jesus had spoken to them, he was taken up into heaven and sat down at the right hand of God."
    },
    "20": {
      "L": "And they went out and preached everywhere, while the Lord worked with them and confirmed the message by accompanying signs.",
      "M": "Then the disciples went out and preached everywhere, and the Lord worked with them and confirmed his word by the signs that accompanied it.",
      "T": "Then they went out and proclaimed the good news everywhere. The Lord worked with them and confirmed the message through the miraculous signs that accompanied it."
    }
  }
}

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'mark')
    merge_tier(data, MARK, key)
    save(tier, 'mark', data)

print('\nMark 13–16 written to all three tiers.')
print('Chapters covered:', sorted(MARK.keys(), key=int))
