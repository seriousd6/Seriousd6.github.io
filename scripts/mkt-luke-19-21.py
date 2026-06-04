"""
MKT Luke chapters 19–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-luke-19-21.py

Building on Luke 1–18 key-term decisions:
- G2424 (Ἰησοῦς): "Jesus" throughout
- G2962 (κύριος): "Lord" throughout (messianic title); "master" in parables when human referent
- G5547 (Χριστός): "Christ" (L/M/T)
- G932 (βασιλεία): "kingdom" throughout
- G935 (βασιλεύς): "king" in narrative; "King" in royal/messianic contexts
- G4151 (πνεῦμα): "Spirit" (divine) / "spirit" (human)
- G26 (ἀγάπη): "love" (not prominent in 19-21)
- G4982 (σῴζω): L: "saved/save"; M: "saved/make well" depending on context;
  T: "saved/healed" — 19:10 "save" (cosmic rescue, not healing)
- G1342 (δίκαιος): "righteous" (L/M/T) — consistent throughout
- G4716 (σταυρός): "cross" — not yet in these chapters
- G166 (αἰώνιος): "eternal" / "age-to-come" quality — 18:30 pattern continues
- G2992 (λαός): "people" (often "the people" with definite article)
- G749 (ἀρχιερεύς): "chief priest" / "high priest" — context determines
- G1122 (γραμματεύς): "scribe" (L) / "teacher of the law" (M/T)
- G5330 (Φαρισαῖος): "Pharisee" throughout
- G3588+G2992 (ὁ λαός): "the people" — the crowd often distinguished from leaders
- G5613 (ὡς): "as" / "like" / "when" — context sensitive
- G4334 (προσέρχομαι): "came" / "came up" in temple/teaching contexts

Chapter 19 notes:
- G2195 (Ζακχαῖος): Zacchaeus story unique to Luke; name means "pure/righteous"
- G5052 (τελέω) / G754 (ἀρχιτελώνης): "chief tax collector" — note the irony of the
  righteous name with the despised profession
- G1328 (διερμηνεύω): not in these chapters
- Minas parable (19:11-27): mina (μνᾶ) = about 3 months' wages; not "talents" (different)
  parable; L: "mina"; M/T: "mina" with note — keep the specific amount
- G268 (ἁμαρτωλός): "sinner" throughout
- G1342 (δίκαιος): in 19:8, Zacchaeus uses δίκαιος implicitly; context important
- Triumphal Entry (19:28-44): the colt (G4454 πῶλος) is Luke's only "colt" — not "donkey"
  explicitly; follows ZechG 9:9 connection
- G3177 (μεθερμηνεύω): not in these chapters
- "The stone will cry out" (19:40): distinctive Lukan saying
- G2799 (κλαίω): "wept" — Jesus weeping over Jerusalem (19:41) — important; render
  with emotional weight; L/M: "wept"; T: "wept" — no need to elaborate

Chapter 20 notes:
- Temple debates: authority, tribute coin, resurrection, and the greatest commandment
- G1849 (ἐξουσία): "authority" throughout in temple question
- G2778 (κῆνσος): L: "census tax"; M: "imperial tax"; T: "taxes" — the coin is the
  actual Greek δηνάριον (denarius); the tax is κήνσον
- G1325 (ἀποδίδωμι): "render/give back" — the famous "render to Caesar" phrasing;
  L: "render"; M: "give back"; T: "give" — preserve the "give back" idea if possible
- G1589 (ἐκλεκτός) / G1096 (γίνομαι): not prominent in ch 20
- Resurrection debate (20:27-40): Sadducees do not believe in resurrection;
  G4891 (συναναβαίνω) / G1484 (ἔθνη): not prominent here
- "Son of David" controversy (20:41-44): Ps 110:1 quotation; κύριος (Lord) appears twice;
  note the difference: David calls the Messiah "my Lord" — this is Christological

Chapter 21 notes (Olivet Discourse in Luke):
- G2413 (ἱερόν): "temple" — the Jerusalem temple complex
- G3485 (ναός): "sanctuary" / "temple" — inner shrine vs. outer courts
- G5059 (τέρας): "wonder" (L) / "portent" (M/T) in signs passages
- G4592 (σημεῖον): "sign" throughout
- G4171 (πόλεμος): "war" throughout
- G1093 (γῆ): "earth" / "land" — context: 21:23 is "the land" (Israel); 21:25 is "earth"
- G2540 (καιρός): "time" / "appointed time" — "seasons" in some contexts
- G1484 (ἔθνη): "nations" / "Gentiles" — 21:24 "times of the Gentiles"; not "nations"
  here but rather the Gentile nations dominating Jerusalem; M/T use "Gentiles"
- G2865 (κομίζω): "receive" in eschatological contexts
- G3348 (μετέχω): not prominent
- The widow's offering (21:1-4): G3009 (λειτουργία) / G1074 (γενεά): "generation"
- G1626 (ἔκτρωμα): not in this section
- G3814 (παιδίσκη): "servant girl" — not in these chapters
- "Stand before the Son of Man" (21:36): G5207 (υἱός) + G444 (ἄνθρωπος) = "Son of Man"
  as apocalyptic title; not "human being"
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
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

LUKE_19_21 = {
 "19": {
  "1": {
   "L": "And he entered and was passing through Jericho.",
   "M": "Jesus entered Jericho and was passing through.",
   "T": "Jesus entered Jericho and was making his way through."
  },
  "2": {
   "L": "And behold, there was a man called by the name Zacchaeus, and he was a chief tax collector, and he was rich.",
   "M": "A man was there by the name of Zacchaeus; he was a chief tax collector and was wealthy.",
   "T": "A man named Zacchaeus was there—a chief tax collector, and very wealthy."
  },
  "3": {
   "L": "And he was seeking to see who Jesus was, but was not able because of the crowd, since he was small in stature.",
   "M": "He wanted to see who Jesus was, but because he was short he could not see over the crowd.",
   "T": "He was eager to get a look at Jesus, but he couldn't see him through the crowd because he was too short."
  },
  "4": {
   "L": "And running ahead, he climbed up into a sycamore-fig tree in order to see him, because he was about to pass through that way.",
   "M": "So he ran ahead and climbed a sycamore-fig tree to see him, since Jesus was coming that way.",
   "T": "So he ran on ahead and climbed a sycamore-fig tree to see Jesus, who was about to pass that way."
  },
  "5": {
   "L": "And when Jesus came to the place, he looked up and said to him: Zacchaeus, hurry and come down, for today I must stay at your house.",
   "M": "When Jesus reached the spot, he looked up and said to him: Zacchaeus, come down immediately. I must stay at your house today.",
   "T": "When Jesus reached the spot, he looked up and said: Zacchaeus, come down right away—I need to stay at your house today!"
  },
  "6": {
   "L": "And he hurried and came down, and received him joyfully.",
   "M": "So he came down at once and welcomed him gladly.",
   "T": "Zacchaeus scrambled down at once and welcomed Jesus into his home with great joy."
  },
  "7": {
   "L": "And when they all saw it, they were grumbling, saying that he has gone in to lodge with a sinful man.",
   "M": "All the people saw this and began to mutter: He has gone to be the guest of a sinner.",
   "T": "Everyone who saw this grumbled: He's gone to be the guest of a sinner!"
  },
  "8": {
   "L": "But Zacchaeus stood and said to the Lord: Behold, Lord, half of my possessions I give to the poor, and if I have defrauded anyone of anything, I restore it fourfold.",
   "M": "But Zacchaeus stood up and said to the Lord: Look, Lord! Here and now I give half of my possessions to the poor, and if I have cheated anybody out of anything, I will pay back four times the amount.",
   "T": "But Zacchaeus stood up and announced to the Lord: Lord, I'm giving half my possessions to the poor right now. And if I have cheated anyone out of anything, I'll pay them back four times the amount."
  },
  "9": {
   "L": "And Jesus said to him: Today salvation has come to this house, since even he is a son of Abraham.",
   "M": "Jesus said to him: Today salvation has come to this house, because this man, too, is a son of Abraham.",
   "T": "Jesus said to him: Today salvation has come to this household—for this man, too, is a son of Abraham."
  },
  "10": {
   "L": "For the Son of Man came to seek and to save the lost.",
   "M": "For the Son of Man came to seek and to save the lost.",
   "T": "The Son of Man came to seek out and save those who are lost."
  },
  "11": {
   "L": "And as they were hearing these things, he proceeded to tell a parable, because he was near Jerusalem and they supposed that the kingdom of God was about to appear immediately.",
   "M": "While they were listening to this, he went on to tell them a parable, because he was near Jerusalem and the people thought that the kingdom of God was going to appear at once.",
   "T": "As the crowd was listening, he went on to tell them a parable—for he was near Jerusalem, and people thought the kingdom of God was going to appear immediately."
  },
  "12": {
   "L": "He said therefore: A certain nobleman went to a distant country to receive for himself a kingdom and to return.",
   "M": "He said: A man of noble birth went to a distant country to have himself appointed king and then to return.",
   "T": "He said: A man of noble birth traveled to a distant country to receive a kingdom for himself and then return."
  },
  "13": {
   "L": "And calling ten of his servants, he gave them ten minas and said to them: Do business until I come.",
   "M": "So he called ten of his servants and gave them ten minas. Put this money to work, he said, until I come back.",
   "T": "Before leaving, he called ten of his servants and gave each one a mina. He said: Invest this and put it to work until I return."
  },
  "14": {
   "L": "But his citizens hated him and sent a delegation after him, saying: We do not want this man to reign over us.",
   "M": "But his subjects hated him and sent a delegation after him to say: We don't want this man to be our king.",
   "T": "But his subjects hated him and sent a delegation after him to say: We refuse to have this man rule over us."
  },
  "15": {
   "L": "And it came to pass when he returned, having received the kingdom, that he ordered these servants to whom he had given the money to be called to him, in order to find out what they had gained by trading.",
   "M": "He was made king, however, and returned home. Then he sent for the servants to whom he had given the money, in order to find out what they had gained with it.",
   "T": "When he returned as king, he summoned the servants to whom he had entrusted the money, to find out how much each had earned."
  },
  "16": {
   "L": "And the first appeared, saying: Lord, your mina has earned ten more minas.",
   "M": "The first one came and said: Sir, your mina has earned ten more.",
   "T": "The first servant came and reported: Master, your mina has earned ten more minas!"
  },
  "17": {
   "L": "And he said to him: Well done, good servant! Because you were faithful in a very little, you shall have authority over ten cities.",
   "M": "Well done, my good servant! his master replied. Because you have been trustworthy in a very small matter, take charge of ten cities.",
   "T": "Well done, good servant! the master said. You were faithful in a very small thing—so take charge of ten cities."
  },
  "18": {
   "L": "And the second came, saying: Your mina, Lord, has made five minas.",
   "M": "The second came and said: Sir, your mina has earned five more.",
   "T": "The second servant said: Master, your mina has earned five more minas."
  },
  "19": {
   "L": "And he said to this one also: And you be over five cities.",
   "M": "His master answered: You take charge of five cities.",
   "T": "He answered: You will be over five cities."
  },
  "20": {
   "L": "Then another came, saying: Lord, here is your mina, which I kept laid away in a handkerchief,",
   "M": "Then another servant came and said: Sir, here is your mina; I have kept it laid away in a piece of cloth.",
   "T": "Then another servant came and said: Master, here is your mina—I kept it stored away wrapped in a cloth."
  },
  "21": {
   "L": "for I was afraid of you, because you are a severe man: you take up what you did not lay down and harvest what you did not sow.",
   "M": "I was afraid of you, because you are a hard man. You take out what you did not put in and reap what you did not sow.",
   "T": "I was afraid of you, because you are a demanding man—you take what you didn't deposit and harvest what you didn't plant."
  },
  "22": {
   "L": "He said to him: Out of your own mouth I will judge you, wicked servant! You knew that I was a severe man, taking up what I did not lay down and harvesting what I did not sow.",
   "M": "His master replied: I will judge you by your own words, you wicked servant! You knew, did you, that I am a hard man, taking out what I did not put in, and reaping what I did not sow?",
   "T": "The master answered: I'll judge you by your own words, you useless servant! You knew I was a demanding man—that I take what I didn't deposit and harvest what I didn't plant."
  },
  "23": {
   "L": "Then why did you not give my money to the bank, and I, on returning, would have collected it with interest?",
   "M": "Why then didn't you put my money on deposit, so that when I came back, I could have collected it with interest?",
   "T": "Then why didn't you at least put my money in the bank? When I came back I could have collected it with interest."
  },
  "24": {
   "L": "And he said to those standing by: Take the mina from him and give it to the one who has ten minas.",
   "M": "Then he said to those standing by: Take his mina away from him and give it to the one who has ten minas.",
   "T": "He said to those standing nearby: Take the mina away from him and give it to the servant who has ten."
  },
  "25": {
   "L": "And they said to him: Lord, he has ten minas.",
   "M": "Sir, they said, he already has ten!",
   "T": "But Master, they said, he already has ten minas!"
  },
  "26": {
   "L": "I tell you that to everyone who has, more will be given; but from the one who has not, even what he has will be taken away.",
   "M": "He replied: I tell you that to everyone who has, more will be given, but as for the one who has nothing, even what they have will be taken away.",
   "T": "He answered: I tell you—to everyone who has, more will be given. But from the one who has nothing, even what little he has will be taken."
  },
  "27": {
   "L": "But those enemies of mine who did not want me to reign over them—bring them here and slay them before me.",
   "M": "But those enemies of mine who did not want me to be king over them—bring them here and kill them in front of me.",
   "T": "Now as for those enemies of mine who refused to have me as their king—bring them here and execute them in front of me."
  },
  "28": {
   "L": "And having said these things, he was going on ahead, ascending to Jerusalem.",
   "M": "After Jesus had said this, he went on ahead, going up to Jerusalem.",
   "T": "After saying this, Jesus went on ahead, heading up to Jerusalem."
  },
  "29": {
   "L": "And it came to pass, as he approached Bethphage and Bethany, near the mountain that is called Olivet, he sent two of his disciples,",
   "M": "As he approached Bethphage and Bethany at the hill called the Mount of Olives, he sent two of his disciples, saying to them:",
   "T": "As he came near Bethphage and Bethany at the hill called the Mount of Olives, he sent two disciples ahead."
  },
  "30": {
   "L": "saying: Go into the village ahead of you, in which on entering you will find a colt tied, on which no one has ever sat; untie it and bring it here.",
   "M": "Go to the village ahead of you, and as you enter it, you will find a colt tied there, which no one has ever ridden. Untie it and bring it here.",
   "T": "He said: Go into the village ahead. As you enter, you will find a young colt tied up that no one has ever ridden. Untie it and bring it back."
  },
  "31": {
   "L": "And if anyone asks you: Why are you untying it? thus you shall say: The Lord has need of it.",
   "M": "If anyone asks you, Why are you untying it? say, The Lord needs it.",
   "T": "If anyone asks why you're untying it, say: The Lord needs it."
  },
  "32": {
   "L": "And those who were sent went away and found it just as he had told them.",
   "M": "Those who were sent ahead went and found it just as he had told them.",
   "T": "The two went and found everything exactly as he had said."
  },
  "33": {
   "L": "And as they were untying the colt, its owners said to them: Why are you untying the colt?",
   "M": "As they were untying the colt, its owners asked them: Why are you untying the colt?",
   "T": "As they untied it, its owners asked: Why are you untying the colt?"
  },
  "34": {
   "L": "And they said: The Lord has need of it.",
   "M": "They replied: The Lord needs it.",
   "T": "They answered: The Lord needs it."
  },
  "35": {
   "L": "And they brought it to Jesus, and throwing their cloaks on the colt, they mounted Jesus on it.",
   "M": "They brought it to Jesus, threw their cloaks on the colt and put Jesus on it.",
   "T": "They brought the colt to Jesus, threw their cloaks over it, and helped Jesus mount."
  },
  "36": {
   "L": "And as he was going, they were spreading their cloaks on the road.",
   "M": "As he went along, people spread their cloaks on the road.",
   "T": "As he rode along, people kept spreading their cloaks on the road ahead of him."
  },
  "37": {
   "L": "And as he was already approaching, at the descent of the Mount of Olives, all the multitude of the disciples began rejoicing to praise God with a loud voice for all the mighty works they had seen,",
   "M": "When he came near the place where the road goes down the Mount of Olives, the whole crowd of disciples began joyfully to praise God in loud voices for all the miracles they had seen:",
   "T": "As he reached the place where the road goes down the Mount of Olives, the whole crowd of disciples burst into joyful praise—shouting aloud to God for all the miracles they had witnessed:"
  },
  "38": {
   "L": "saying: Blessed is the King who comes in the name of the Lord! Peace in heaven and glory in the highest!",
   "M": "Blessed is the king who comes in the name of the Lord! Peace in heaven and glory in the highest!",
   "T": "Blessed is the King who comes in the name of the Lord! Peace in heaven—and glory in the highest!"
  },
  "39": {
   "L": "And some of the Pharisees from the crowd said to him: Teacher, rebuke your disciples.",
   "M": "Some of the Pharisees in the crowd said to Jesus: Teacher, rebuke your disciples!",
   "T": "Some of the Pharisees in the crowd said to him: Teacher, tell your disciples to be quiet!"
  },
  "40": {
   "L": "And answering, he said: I tell you, if these are silent, the stones will cry out.",
   "M": "I tell you, he replied, if they keep quiet, the stones will cry out.",
   "T": "He replied: I tell you—if they kept quiet, the very stones would cry out."
  },
  "41": {
   "L": "And as he drew near and saw the city, he wept over it,",
   "M": "As he approached Jerusalem and saw the city, he wept over it",
   "T": "As he came near Jerusalem and saw the city spread before him, he wept over it"
  },
  "42": {
   "L": "saying: If you had known in this day, even you, the things that make for peace! But now they are hidden from your eyes.",
   "M": "and said: If you, even you, had only known on this day what would bring you peace—but now it is hidden from your eyes.",
   "T": "and said: If only you had recognized today what would bring you peace! But now it is hidden from your sight."
  },
  "43": {
   "L": "For the days will come upon you when your enemies will throw up a rampart against you and surround you and hem you in on every side,",
   "M": "The days will come upon you when your enemies will build an embankment against you and encircle you and hem you in on every side.",
   "T": "The days are coming when your enemies will throw up siege works around you, surround you, and close in on you from every direction."
  },
  "44": {
   "L": "and they will level you to the ground, you and your children within you, and they will not leave one stone upon another in you, because you did not recognize the time of your visitation.",
   "M": "They will dash you to the ground, you and the children within your walls. They will not leave one stone on another, because you did not recognise the time of God's coming to you.",
   "T": "They will crush you and your children to the ground—not leaving one stone on another—because you did not recognize the moment when God came to you."
  },
  "45": {
   "L": "And entering the temple, he began to drive out those who were selling,",
   "M": "When Jesus entered the temple courts, he began driving out those who were selling.",
   "T": "Then he entered the temple courts and began driving out those who were selling there."
  },
  "46": {
   "L": "saying to them: It is written: My house shall be a house of prayer, but you have made it a den of robbers.",
   "M": "It is written, he said to them, My house will be a house of prayer; but you have made it a den of robbers.",
   "T": "He said: It is written, My house will be a house of prayer—but you have turned it into a den of robbers!"
  },
  "47": {
   "L": "And he was teaching daily in the temple. But the chief priests and the scribes and the leaders of the people were seeking to destroy him,",
   "M": "Every day he was teaching at the temple. But the chief priests, the teachers of the law and the leaders among the people were trying to kill him.",
   "T": "Each day he taught in the temple courts. The chief priests, the teachers of the law, and the leaders of the people kept looking for a way to kill him."
  },
  "48": {
   "L": "and they could not find anything they might do, for all the people were hanging on him listening.",
   "M": "Yet they could not find any way to do it, because all the people hung on his words.",
   "T": "But they couldn't find a way to do it, because all the people hung on his every word."
  }
 },
 "20": {
  "1": {
   "L": "And it came to pass on one of those days, as he was teaching the people in the temple and proclaiming the gospel, that the chief priests and the scribes with the elders stood before him",
   "M": "One day as Jesus was teaching the people in the temple courts and proclaiming the good news, the chief priests and the teachers of the law, together with the elders, came up to him.",
   "T": "One of those days, while he was teaching and announcing the good news in the temple courts, the chief priests, teachers of the law, and elders confronted him."
  },
  "2": {
   "L": "and said, saying to him: Tell us, by what authority are you doing these things? Or who is it who gave you this authority?",
   "M": "Tell us by what authority you are doing these things, they said. Who gave you this authority?",
   "T": "They demanded: Tell us—by what authority are you doing these things? Who gave you this authority?"
  },
  "3": {
   "L": "And answering, he said to them: I also will ask you a question, and tell me:",
   "M": "He replied: I will also ask you a question. Tell me:",
   "T": "He answered: I have a question for you as well. Tell me—"
  },
  "4": {
   "L": "The baptism of John—was it from heaven or from men?",
   "M": "John's baptism—was it from heaven, or of human origin?",
   "T": "Was John's baptism from God, or was it merely human in origin?"
  },
  "5": {
   "L": "And they reasoned among themselves, saying: If we say, From heaven, he will say: Why did you not believe him?",
   "M": "They discussed it among themselves and said: If we say, From heaven, he will ask, Why didn't you believe him?",
   "T": "They debated it among themselves: If we say, From God, he'll ask, Then why didn't you believe John?"
  },
  "6": {
   "L": "But if we say, From men, all the people will stone us, for they are persuaded that John was a prophet.",
   "M": "But if we say, Of human origin, all the people will stone us, because they are persuaded that John was a prophet.",
   "T": "But if we say, It was merely human, the people will stone us—because they all believe John was a prophet."
  },
  "7": {
   "L": "And they answered that they did not know where it was from.",
   "M": "So they answered that they did not know where it was from.",
   "T": "So they replied that they didn't know."
  },
  "8": {
   "L": "And Jesus said to them: Neither am I telling you by what authority I do these things.",
   "M": "Jesus said: Neither will I tell you by what authority I am doing these things.",
   "T": "Jesus said: Then neither will I tell you by what authority I do these things."
  },
  "9": {
   "L": "And he began to tell this parable to the people: A man planted a vineyard and leased it to tenant farmers, and went away for a long time.",
   "M": "He went on to tell the people this parable: A man planted a vineyard, rented it to some farmers and went away for a long time.",
   "T": "Then he told the people this parable: A man planted a vineyard, leased it to tenant farmers, and went away for a long time."
  },
  "10": {
   "L": "And at the season he sent a servant to the tenant farmers, so that they would give him his share of the fruit of the vineyard. But the tenant farmers beat him and sent him away empty-handed.",
   "M": "At harvest time he sent a servant to the tenants so they would give him some of the fruit of the vineyard. But the tenants beat him and sent him away empty-handed.",
   "T": "At harvest time he sent a servant to collect his share of the fruit. But the tenants beat him and sent him back empty-handed."
  },
  "11": {
   "L": "And he continued to send another servant; but they beat that one also and treated him shamefully and sent him away empty-handed.",
   "M": "He sent another servant, but that one also they beat and treated shamefully and sent away empty-handed.",
   "T": "He sent another servant, who was also beaten, humiliated, and sent away empty-handed."
  },
  "12": {
   "L": "And he continued to send a third; but this one also they wounded and threw out.",
   "M": "He sent still a third, and they wounded him and threw him out.",
   "T": "He sent a third, and they wounded him and threw him out."
  },
  "13": {
   "L": "Then the owner of the vineyard said: What shall I do? I will send my beloved son; perhaps they will respect him.",
   "M": "Then the owner of the vineyard said: What shall I do? I will send my son, whom I love; perhaps they will respect him.",
   "T": "Then the owner of the vineyard said: What should I do? I'll send my beloved son—surely they will respect him."
  },
  "14": {
   "L": "But when the tenant farmers saw him, they reasoned with one another, saying: This is the heir; let us kill him, so that the inheritance may be ours.",
   "M": "But when the tenants saw him, they talked the matter over. This is the heir, they said. Let's kill him, and the inheritance will be ours.",
   "T": "But when the tenants saw him, they said to each other: This is the heir—let's kill him, and the inheritance will be ours!"
  },
  "15": {
   "L": "And casting him outside the vineyard, they killed him. What therefore will the owner of the vineyard do to them?",
   "M": "So they threw him out of the vineyard and killed him. What then will the owner of the vineyard do to them?",
   "T": "So they threw him out of the vineyard and killed him. What then will the owner do to those tenants?"
  },
  "16": {
   "L": "He will come and destroy these tenant farmers and give the vineyard to others. When they heard this, they said: May it never be!",
   "M": "He will come and kill those tenants and give the vineyard to others. When the people heard this, they said: God forbid!",
   "T": "He will come and put those tenants to death and give the vineyard to others. When the crowd heard this, they said: God forbid!"
  },
  "17": {
   "L": "But looking at them, he said: What then is this that is written: The stone that the builders rejected has become the cornerstone?",
   "M": "Jesus looked directly at them and asked: Then what is the meaning of that which is written: The stone the builders rejected has become the cornerstone?",
   "T": "But he looked at them and said: Then what does this Scripture mean? The stone the builders rejected has become the very cornerstone."
  },
  "18": {
   "L": "Everyone who falls on that stone will be broken to pieces, but on whomever it falls, it will crush him.",
   "M": "Everyone who falls on that stone will be broken to pieces; anyone on whom it falls will be crushed.",
   "T": "Anyone who falls on that stone will be shattered—and anyone it falls on will be crushed to powder."
  },
  "19": {
   "L": "And the scribes and the chief priests sought to lay hands on him at that very hour, and they feared the people; for they perceived that he had spoken this parable against them.",
   "M": "The teachers of the law and the chief priests looked for a way to arrest him immediately, because they knew he had spoken this parable against them. But they were afraid of the people.",
   "T": "At that very moment the teachers of the law and the chief priests wanted to arrest him—they knew the parable was aimed at them—but they feared the people."
  },
  "20": {
   "L": "And watching him closely, they sent spies who pretended to be righteous, in order to seize him in some word, so as to hand him over to the rule and authority of the governor.",
   "M": "Keeping a close watch on him, they sent spies, who pretended to be sincere. They hoped to catch Jesus in something he said, so that they might hand him over to the power and authority of the governor.",
   "T": "So they watched closely and sent spies pretending to be sincere. They hoped to trap him in his words so they could hand him over to the authority of the governor."
  },
  "21": {
   "L": "And they questioned him, saying: Teacher, we know that you speak and teach rightly, and you do not show partiality, but you teach the way of God in truth.",
   "M": "So the spies questioned him: Teacher, we know that you speak and teach what is right, and that you do not show partiality but teach the way of God in accordance with the truth.",
   "T": "They asked him: Teacher, we know you speak and teach what is true—you don't play favorites but genuinely teach God's ways."
  },
  "22": {
   "L": "Is it lawful for us to pay taxes to Caesar, or not?",
   "M": "Is it right for us to pay taxes to Caesar or not?",
   "T": "Is it right for us to pay taxes to Caesar, or not?"
  },
  "23": {
   "L": "But he perceived their craftiness and said to them:",
   "M": "He saw through their duplicity and said to them:",
   "T": "He saw right through their scheming and said:"
  },
  "24": {
   "L": "Show me a denarius. Whose image and inscription does it have? And they said: Caesar's.",
   "M": "Show me a denarius. Whose image and inscription are on it? Caesar's, they replied.",
   "T": "Show me a denarius. Whose portrait and inscription are on it? Caesar's, they said."
  },
  "25": {
   "L": "And he said to them: Then render to Caesar the things that are Caesar's, and to God the things that are God's.",
   "M": "He said to them: Then give back to Caesar what is Caesar's, and to God what is God's.",
   "T": "Then give to Caesar what belongs to Caesar—and give to God what belongs to God."
  },
  "26": {
   "L": "And they were unable to catch him in a word before the people; and marveling at his answer, they were silent.",
   "M": "They were unable to trap him in what he had said there in public. And astonished by his answer, they became silent.",
   "T": "They failed to trap him in his words before the people. Astonished by his answer, they fell silent."
  },
  "27": {
   "L": "And some of the Sadducees came—those who say there is no resurrection—and they questioned him,",
   "M": "Some of the Sadducees, who say there is no resurrection, came to Jesus with a question.",
   "T": "Some Sadducees—the ones who deny the resurrection—came to Jesus with a question."
  },
  "28": {
   "L": "saying: Teacher, Moses wrote for us that if a man's brother should die having a wife, and he be childless, that his brother should take the wife and raise up offspring for his brother.",
   "M": "Teacher, they said, Moses wrote for us that if a man's brother dies and leaves a wife but no children, the man must marry the widow and raise up offspring for his brother.",
   "T": "Teacher, Moses wrote for us that if a man dies leaving a wife but no children, his brother should marry her and have children to carry on his brother's name."
  },
  "29": {
   "L": "Now there were seven brothers; and the first took a wife and died childless.",
   "M": "Now there were seven brothers. The first one married a woman and died childless.",
   "T": "Now suppose there were seven brothers. The first one married and died without children."
  },
  "30": {
   "L": "And the second",
   "M": "The second",
   "T": "The second"
  },
  "31": {
   "L": "and the third took her; and similarly the seven also; they left no children and died.",
   "M": "and then the third married her, and in the same way the seven died, leaving no children.",
   "T": "and then the third married her—and the same thing happened with all seven. They died without leaving children."
  },
  "32": {
   "L": "Afterward the woman also died.",
   "M": "Finally, the woman died too.",
   "T": "Finally, the woman also died."
  },
  "33": {
   "L": "In the resurrection, therefore, whose wife of them does she become? For the seven had her as wife.",
   "M": "Now then, at the resurrection whose wife will she be, since the seven were married to her?",
   "T": "At the resurrection, then, whose wife will she be? All seven had married her."
  },
  "34": {
   "L": "And Jesus said to them: The sons of this age marry and are given in marriage,",
   "M": "Jesus replied: The people of this age marry and are given in marriage.",
   "T": "Jesus said: The people of this present age marry and are given in marriage."
  },
  "35": {
   "L": "but those who are considered worthy of that age and of the resurrection from the dead neither marry nor are given in marriage,",
   "M": "But those who are considered worthy of taking part in the age to come and in the resurrection from the dead will neither marry nor be given in marriage,",
   "T": "But those who are considered worthy to share in the coming age and in the resurrection from the dead will not marry or be given in marriage."
  },
  "36": {
   "L": "for they can no longer die, because they are equal to angels and are sons of God, being sons of the resurrection.",
   "M": "and they can no longer die; for they are like the angels. They are God's children, since they are children of the resurrection.",
   "T": "They cannot die anymore, for they are like the angels—they are children of God because they share in the resurrection."
  },
  "37": {
   "L": "But that the dead are raised, even Moses showed at the bush, when he calls the Lord the God of Abraham and the God of Isaac and the God of Jacob.",
   "M": "But in the account of the burning bush, even Moses showed that the dead rise, for he calls the Lord the God of Abraham, and the God of Isaac, and the God of Jacob.",
   "T": "But that the dead are raised—Moses himself showed this in the account of the burning bush. He calls the Lord the God of Abraham, the God of Isaac, and the God of Jacob."
  },
  "38": {
   "L": "Now he is not the God of the dead but of the living; for all live to him.",
   "M": "He is not the God of the dead, but of the living, for to him all are alive.",
   "T": "He is not the God of the dead but of the living—because to him, all are alive."
  },
  "39": {
   "L": "And some of the scribes answering said: Teacher, you have spoken well.",
   "M": "Some of the teachers of the law responded: Well said, teacher!",
   "T": "Some of the teachers of the law said: Well answered, teacher!"
  },
  "40": {
   "L": "For they no longer dared to ask him anything.",
   "M": "And no one dared to ask him any more questions.",
   "T": "After that, no one dared to question him further."
  },
  "41": {
   "L": "And he said to them: How do they say that the Christ is the son of David?",
   "M": "Then Jesus said to them: Why is it said that the Messiah is the son of David?",
   "T": "Then Jesus said to them: How can they say the Messiah is the son of David?"
  },
  "42": {
   "L": "For David himself says in the Book of Psalms: The Lord said to my Lord, Sit at my right hand,",
   "M": "David himself declares in the Book of Psalms: The Lord said to my Lord: Sit at my right hand",
   "T": "David himself says in the Book of Psalms: The Lord said to my Lord: Sit at my right hand"
  },
  "43": {
   "L": "until I make your enemies a footstool for your feet.",
   "M": "until I make your enemies a footstool for your feet.",
   "T": "until I make your enemies a footstool under your feet."
  },
  "44": {
   "L": "David therefore calls him Lord; so how is he his son?",
   "M": "David calls him Lord. How then can he be his son?",
   "T": "David calls him Lord—so how can he be David's son?"
  },
  "45": {
   "L": "And in the hearing of all the people he said to his disciples:",
   "M": "While all the people were listening, Jesus said to his disciples:",
   "T": "While all the people were listening, he said to his disciples:"
  },
  "46": {
   "L": "Beware of the scribes who like to walk around in long robes and love greetings in the marketplaces and the seats of honor in the synagogues and the places of honor at feasts,",
   "M": "Beware of the teachers of the law. They like to walk around in flowing robes and love to be greeted with respect in the market-places and have the most important seats in the synagogues and the places of honour at banquets.",
   "T": "Watch out for the teachers of the law. They love to parade around in flowing robes, enjoy being greeted respectfully in the marketplace, and crave the best seats in the synagogue and the places of honor at banquets."
  },
  "47": {
   "L": "who devour the houses of widows and for a pretense make long prayers. These will receive the greater condemnation.",
   "M": "They devour widows' houses and for a show make lengthy prayers. These men will be punished most severely.",
   "T": "They eat up widows' property and offer long prayers just for show. These men will face the severest judgment."
  }
 },
 "21": {
  "1": {
   "L": "And looking up, he saw the rich putting their gifts into the treasury.",
   "M": "As Jesus looked up, he saw the rich putting their gifts into the temple treasury.",
   "T": "Looking up, Jesus saw wealthy people dropping their gifts into the temple treasury."
  },
  "2": {
   "L": "And he saw a certain poor widow putting in two small coins.",
   "M": "He also saw a poor widow put in two very small copper coins.",
   "T": "He also noticed a poor widow drop in two small copper coins."
  },
  "3": {
   "L": "And he said: Truly I say to you, this poor widow has put in more than all of them.",
   "M": "Truly I tell you, he said, this poor widow has put in more than all the others.",
   "T": "He said: I tell you the truth—this poor widow has given more than all the others."
  },
  "4": {
   "L": "For all these put in gifts out of their abundance, but she out of her poverty put in all the living she had.",
   "M": "All these people gave their gifts out of their wealth; but she out of her poverty put in all she had to live on.",
   "T": "All the others gave out of their surplus wealth. But she, out of her poverty, put in everything she had to live on."
  },
  "5": {
   "L": "And as some were speaking about the temple, how it was adorned with beautiful stones and offerings, he said:",
   "M": "Some of his disciples were remarking about how the temple was adorned with beautiful stones and with gifts dedicated to God. But Jesus said:",
   "T": "Some of his disciples were admiring the temple—its beautiful stones and the offerings decorating it. Jesus said:"
  },
  "6": {
   "L": "As for these things that you are looking at, days will come in which there will not be left here one stone upon another that will not be thrown down.",
   "M": "As for what you see here, the time will come when not one stone will be left on another; every one of them will be thrown down.",
   "T": "All this you see—days are coming when not one stone will be left on another. Every one will be thrown down."
  },
  "7": {
   "L": "And they questioned him, saying: Teacher, when therefore will these things be? And what will be the sign when these things are about to take place?",
   "M": "Teacher, they asked, when will these things happen? And what will be the sign that they are about to take place?",
   "T": "Teacher, they asked, when will this happen? And what sign will warn us these things are about to occur?"
  },
  "8": {
   "L": "And he said: Watch out that you are not deceived; for many will come in my name, saying: I am he! and: The time is near! Do not go after them.",
   "M": "He replied: Watch out that you are not deceived. For many will come in my name, claiming, I am he, and, The time is near. Do not follow them.",
   "T": "He said: Watch out—don't be deceived. Many will come claiming to be me, saying: I am he! or The time is here! Don't follow them."
  },
  "9": {
   "L": "And when you hear of wars and upheavals, do not be terrified; for these things must happen first, but the end will not come immediately.",
   "M": "When you hear of wars and uprisings, do not be frightened. These things must happen first, but the end will not come right away.",
   "T": "When you hear about wars and revolutions, don't be alarmed. These things must happen first, but the end isn't coming yet."
  },
  "10": {
   "L": "Then he said to them: Nation will rise against nation, and kingdom against kingdom.",
   "M": "Then he said to them: Nation will rise against nation, and kingdom against kingdom.",
   "T": "Then he continued: Nation will go to war against nation, and kingdom against kingdom."
  },
  "11": {
   "L": "There will be great earthquakes, and in various places famines and plagues; and there will be terrors and great signs from heaven.",
   "M": "There will be great earthquakes, famines and pestilences in various places, and fearful events and great signs from heaven.",
   "T": "There will be massive earthquakes, famines, and plagues in various places—terrifying events and great signs from heaven."
  },
  "12": {
   "L": "But before all these things, they will lay their hands on you and persecute you, delivering you to the synagogues and prisons, and bringing you before kings and governors for my name's sake.",
   "M": "But before all this, they will seize you and persecute you. They will hand you over to synagogues and put you in prison, and you will be brought before kings and governors, and all on account of my name.",
   "T": "But before all that happens, they will arrest you and persecute you—dragging you before synagogues and throwing you into prison. You will be brought before kings and governors, all because of me."
  },
  "13": {
   "L": "This will result in an opportunity for your testimony.",
   "M": "And so you will bear testimony to me.",
   "T": "This will be your opportunity to testify."
  },
  "14": {
   "L": "Make up your minds therefore not to prepare your defense beforehand,",
   "M": "But make up your mind not to worry beforehand how you will defend yourselves.",
   "T": "So make up your mind not to prepare your defense in advance."
  },
  "15": {
   "L": "for I will give you a mouth and wisdom that all your opponents will not be able to withstand or contradict.",
   "M": "For I will give you words and wisdom that none of your adversaries will be able to resist or contradict.",
   "T": "I will give you the words and wisdom that none of your opponents will be able to counter or contradict."
  },
  "16": {
   "L": "And you will be delivered up even by parents and brothers and relatives and friends, and they will put some of you to death.",
   "M": "You will be betrayed even by parents, brothers and sisters, relatives and friends, and they will put some of you to death.",
   "T": "You will be betrayed even by parents, brothers and sisters, relatives, and friends—and some of you will be put to death."
  },
  "17": {
   "L": "And you will be hated by all on account of my name.",
   "M": "Everyone will hate you because of me.",
   "T": "Everyone will hate you because of me."
  },
  "18": {
   "L": "But not a hair of your head will perish.",
   "M": "But not a hair of your head will perish.",
   "T": "Yet not a single hair of your head will be lost."
  },
  "19": {
   "L": "By your endurance you will gain your lives.",
   "M": "Stand firm, and you will win life.",
   "T": "By standing firm, you will save your lives."
  },
  "20": {
   "L": "But when you see Jerusalem surrounded by armies, then know that its desolation has come near.",
   "M": "When you see Jerusalem being surrounded by armies, you will know that its desolation is near.",
   "T": "When you see Jerusalem surrounded by armies, you will know that its destruction is near."
  },
  "21": {
   "L": "Then those in Judea must flee to the mountains, and those in the middle of the city must depart, and those out in the country must not enter into her,",
   "M": "Then let those who are in Judea flee to the mountains, let those in the city get out, and let those in the country not enter the city.",
   "T": "Then those in Judea must flee to the mountains. Those inside the city must get out. And those in the countryside must not go back in."
  },
  "22": {
   "L": "because these are days of vengeance, to fulfill all that is written.",
   "M": "For this is the time of punishment in fulfilment of all that has been written.",
   "T": "For these are days of divine punishment—the fulfillment of everything that is written."
  },
  "23": {
   "L": "Woe to those who are pregnant and to those who are nursing in those days! For there will be great distress on the land and wrath against this people.",
   "M": "How dreadful it will be in those days for pregnant women and nursing mothers! There will be great distress in the land and wrath against this people.",
   "T": "How terrible it will be for pregnant women and nursing mothers in those days! There will be great suffering throughout the land and God's wrath against this people."
  },
  "24": {
   "L": "And they will fall by the edge of the sword and be led captive into all the nations, and Jerusalem will be trampled by the Gentiles until the times of the Gentiles are fulfilled.",
   "M": "They will fall by the sword and will be taken as prisoners to all the nations. Jerusalem will be trampled on by the Gentiles until the times of the Gentiles are fulfilled.",
   "T": "They will be cut down by the sword and taken as prisoners to every nation. Jerusalem will be trampled under foot by the Gentiles until their era comes to its end."
  },
  "25": {
   "L": "And there will be signs in sun and moon and stars, and on the earth distress of nations in perplexity at the roaring and surging of the sea,",
   "M": "There will be signs in the sun, moon and stars. On the earth, nations will be in anguish and perplexity at the roaring and tossing of the sea.",
   "T": "Then there will be signs in the sun, moon, and stars. On the earth, the nations will be in despair—bewildered by the roaring and surging sea."
  },
  "26": {
   "L": "people fainting with fear and with expectation of what is coming upon the inhabited earth; for the powers of the heavens will be shaken.",
   "M": "People will faint from terror, apprehensive of what is coming on the world, for the heavenly bodies will be shaken.",
   "T": "People will faint in terror, dreading what is coming on the world—for the very powers of heaven will be shaken."
  },
  "27": {
   "L": "And then they will see the Son of Man coming in a cloud with power and great glory.",
   "M": "At that time they will see the Son of Man coming in a cloud with power and great glory.",
   "T": "Then they will see the Son of Man coming on a cloud, with power and great glory."
  },
  "28": {
   "L": "But when these things begin to take place, stand up and lift up your heads, because your redemption is drawing near.",
   "M": "When these things begin to take place, stand up and lift up your heads, because your redemption is drawing near.",
   "T": "When these things begin to happen, stand up tall and lift your heads—because your redemption is getting close."
  },
  "29": {
   "L": "And he told them a parable: Look at the fig tree and all the trees.",
   "M": "He told them this parable: Look at the fig tree and all the trees.",
   "T": "He taught them with a parable: Look at the fig tree—and all the trees."
  },
  "30": {
   "L": "When they are already budding, you see it yourselves and know that summer is already near.",
   "M": "When they sprout leaves, you can see for yourselves and know that summer is near.",
   "T": "When they leaf out, you can see for yourselves and know that summer is close."
  },
  "31": {
   "L": "Even so you also, when you see these things taking place, know that the kingdom of God is near.",
   "M": "Even so, when you see these things happening, you know that the kingdom of God is near.",
   "T": "In the same way, when you see these things happening, you know that God's kingdom is near."
  },
  "32": {
   "L": "Truly I say to you that this generation will not pass away until all things take place.",
   "M": "Truly I tell you, this generation will certainly not pass away until all these things have happened.",
   "T": "I tell you with certainty—this generation will not pass away until all these things have taken place."
  },
  "33": {
   "L": "Heaven and earth will pass away, but my words will not pass away.",
   "M": "Heaven and earth will pass away, but my words will never pass away.",
   "T": "Heaven and earth will disappear—but my words will never disappear."
  },
  "34": {
   "L": "But watch yourselves lest at any time your hearts be weighed down with dissipation and drunkenness and anxieties of life, and that day should come upon you suddenly like a snare.",
   "M": "Be careful, or your hearts will be weighed down with carousing, drunkenness and the anxieties of life, and that day will close on you suddenly like a trap.",
   "T": "But watch yourselves—don't let your hearts get weighed down with indulgence, drinking, and the worries of this life, or that day will spring on you like a trap."
  },
  "35": {
   "L": "For it will come upon all who dwell on the face of all the earth.",
   "M": "For it will come on all those who live on the face of the whole earth.",
   "T": "It will come upon everyone who lives on the face of the earth."
  },
  "36": {
   "L": "Be watchful at all times, praying that you may have strength to escape all these things that are about to take place, and to stand before the Son of Man.",
   "M": "Be always on the watch, and pray that you may be able to escape all that is about to happen, and that you may be able to stand before the Son of Man.",
   "T": "Stay alert at all times—and pray that you will have the strength to escape everything that is about to happen, and that you will be able to stand before the Son of Man."
  },
  "37": {
   "L": "And during the days he was teaching in the temple; but going out, he was spending the nights on the mountain that is called Olivet.",
   "M": "Each day Jesus was teaching at the temple, and each evening he went out to spend the night on the hill called the Mount of Olives,",
   "T": "Each day Jesus taught in the temple courts, and each evening he went out to spend the night on the Mount of Olives."
  },
  "38": {
   "L": "And all the people were coming early in the morning to him in the temple to hear him.",
   "M": "and all the people came early in the morning to hear him at the temple.",
   "T": "And all the people came early each morning to hear him at the temple."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'luke')
        merge_tier(existing, LUKE_19_21, tier_key)
        save(tier_dir, 'luke', existing)
    print('Luke 19–21 written.')

if __name__ == '__main__':
    main()
