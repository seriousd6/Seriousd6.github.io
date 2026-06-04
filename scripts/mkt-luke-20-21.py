"""
MKT Luke chapters 20–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-luke-20-21.py

Translation decisions:
- G165 (αἰών, vv. 20:34–35): "this age" (L/M) / "this present world" (T) — the contrast is
  between the current age where marriage structures society and the resurrection age where it does
  not; "sons of this age" = those who belong to the current order of things
- G2962 (κύριος, vv. 20:41–44, 21:3): "Lord" throughout — both divine address and Psalm 110:1
  citation; the wordplay in 20:42–44 turns on David calling the Messiah κύριος ("Lord"),
  which the T tier makes explicit by noting the son/Lord paradox
- G5207 (υἱός, 20:13, 21:27): "son" (lowercase) for the vineyard parable; "Son" (capitalised)
  for "Son of Man" in 21:27 — divine Christological title distinguished from ordinary usage
- G3624 (οἶκος, 20:47): "houses" in L/M; T "homes" — the devouring of widows' property;
  same rendered as "house" where building-sense is foregrounded (Temple)
- G444 (ἄνθρωπος, 20:9): "man" (L/M/T) — a human being who planted a vineyard, not God;
  the allegorical identity emerges from context, not the word
- G1093 (γῆ, 21:25): "earth" in L/M; T "the world" where global scope is intended; "land"
  where territorial meaning applies (21:23 "great distress on the land")
- G3772 (οὐρανός, 21:11, 26, 33): "heaven" when referring to the divine realm / sky-space;
  "sky" in 21:26 where cosmic/astronomical phenomena are in view — both are in the chapter
  and the context distinguishes them; T uses "heavens" (plural) for cosmic plural form
- G1588 (ἐκλεκτός, 21:36): not present in Luke 21; the verse speaks of those counted worthy
  to stand before the Son of Man — the T tier expresses this as "found worthy"
- G5046 (τέλος, 21:9): "end" (L/M/T) — the immediate referent is the eschatological end,
  not simply a finish; all three tiers use "end" to preserve the eschatological weight
- G1411 (δύναμις, 21:26, 27): "powers" (L/M/T) — cosmic powers being shaken; plural noun;
  consistent rendering with Lukan usage in Acts
- G2588 (καρδία, 21:34): "hearts" throughout — consistent with prior chapters
- Textual-critical note: Luke 20:43 "footstool for your feet" (LXX Ps 109:1) — the citation
  in all manuscripts follows the LXX closely; no disputed readings in this section
- Luke 21:4 — "out of her poverty / want (G5303 ὑστέρημα)" — L "want"; M "poverty"; T
  "all she had to live on" (the T tier unpacks the economic sacrifice)
- Luke 21:20–24 — Jerusalem destruction (70 CE) in prospective form; the T tier makes the
  double-fulfilment (near: 70 CE; far: eschatological) clear through careful phrasing
- Luke 21:25 "signs in sun, moon, and stars" — all three luminaries named; T: "in the sun,
  moon, and stars" preserving the cosmic triple
- Aspect notes: The aorist in 20:14 (ἴδωσιν, "when they saw him") is punctiliar — "seeing
  him"; the future forms in 21:25–28 are genuine predictive futures rendered accordingly
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

LUKE_20_21 = {
 "20": {
  "1": {
   "L": "And it came to pass on one of those days, as he was teaching the people in the temple and proclaiming the gospel, that the chief priests and the scribes came up with the elders,",
   "M": "One day as Jesus was teaching the people in the temple courts and proclaiming the good news, the chief priests and the teachers of the law, together with the elders, came up to him.",
   "T": "One day while Jesus was teaching in the temple courts and announcing the good news, the chief priests, teachers of the law, and elders came up to him."
  },
  "2": {
   "L": "and they spoke, saying to him: Tell us by what authority you do these things, or who it is who gave you this authority.",
   "M": "Tell us by what authority you are doing these things, they said. Who gave you this authority?",
   "T": "They demanded: Tell us — by what authority are you doing these things? Who gave you this authority?"
  },
  "3": {
   "L": "He answered and said to them: I also will ask you a word, and you tell me:",
   "M": "He replied: I will also ask you a question. Tell me:",
   "T": "Jesus replied: I will also ask you a question. Answer me this:"
  },
  "4": {
   "L": "The baptism of John — was it from heaven or from men?",
   "M": "John's baptism — was it from heaven, or of human origin?",
   "T": "John's baptism — did it come from God, or was it merely human?"
  },
  "5": {
   "L": "And they reasoned with one another, saying: If we say, From heaven, he will say, Why then did you not believe him?",
   "M": "They discussed it among themselves and said: If we say, From heaven, he will ask, Why didn't you believe him?",
   "T": "They talked it over among themselves: If we say, From God, he will ask why we didn't believe John."
  },
  "6": {
   "L": "But if we say, From men, all the people will stone us, for they are persuaded that John was a prophet.",
   "M": "But if we say, Of human origin, all the people will stone us, because they are persuaded that John was a prophet.",
   "T": "But if we say, It was merely human, the whole crowd will stone us—they are all convinced John was a prophet."
  },
  "7": {
   "L": "And they answered that they did not know from where it was.",
   "M": "So they answered that they did not know where it came from.",
   "T": "So they said they did not know where it came from."
  },
  "8": {
   "L": "And Jesus said to them: Neither will I tell you by what authority I do these things.",
   "M": "Jesus said: Neither will I tell you by what authority I am doing these things.",
   "T": "Jesus said: Then neither will I tell you by what authority I am doing these things."
  },
  "9": {
   "L": "And he began to tell the people this parable: A man planted a vineyard and let it out to tenant farmers and traveled abroad for a long time.",
   "M": "He went on to tell the people this parable: A man planted a vineyard, rented it to some farmers and went away for a long time.",
   "T": "He began to tell the people this parable: A man planted a vineyard, rented it to tenant farmers, and went away on a long journey."
  },
  "10": {
   "L": "And at the appointed time he sent a servant to the tenants, so that they would give him some of the fruit of the vineyard. But the tenants beat him and sent him away empty-handed.",
   "M": "At harvest time he sent a servant to the tenants so they would give him some of the fruit of the vineyard. But the tenants beat him and sent him away empty-handed.",
   "T": "When the time came, he sent a servant to the farmers to collect his share of the harvest. But they beat the servant and sent him away with nothing."
  },
  "11": {
   "L": "And he proceeded to send another servant. They also beat that one and treated him shamefully and sent him away empty-handed.",
   "M": "He sent another servant, but that one also they beat and treated shamefully and sent away empty-handed.",
   "T": "He sent another servant. They beat that one too, treated him shamefully, and sent him away with nothing."
  },
  "12": {
   "L": "And he proceeded to send a third. This one too they wounded and drove out.",
   "M": "He sent a third, and they wounded him and threw him out.",
   "T": "He sent a third. They wounded him and threw him out."
  },
  "13": {
   "L": "Then the owner of the vineyard said: What shall I do? I will send my beloved son; perhaps they will respect him.",
   "M": "Then the owner of the vineyard said: What shall I do? I will send my son, whom I love; perhaps they will respect him.",
   "T": "Then the owner of the vineyard said: What shall I do? I will send my beloved son. Surely they will respect him."
  },
  "14": {
   "L": "But when the tenants saw him, they reasoned with one another, saying: This is the heir; let us kill him, so that the inheritance may become ours.",
   "M": "But when the tenants saw him, they talked the matter over. This is the heir, they said. Let us kill him, and the inheritance will be ours.",
   "T": "But when the farmers saw him, they said to one another: This is the heir! Let us kill him, and the inheritance will be ours."
  },
  "15": {
   "L": "And throwing him out of the vineyard, they killed him. What therefore will the owner of the vineyard do to them?",
   "M": "So they threw him out of the vineyard and killed him. What then will the owner of the vineyard do to them?",
   "T": "So they threw him out of the vineyard and killed him. What will the owner do to those farmers?"
  },
  "16": {
   "L": "He will come and destroy those tenants and give the vineyard to others. When they heard this, they said: May it never be!",
   "M": "He will come and kill those tenants and give the vineyard to others. When the people heard this, they said: God forbid!",
   "T": "He will come and destroy those farmers and give the vineyard to others. When the crowd heard this, they said: No — God forbid!"
  },
  "17": {
   "L": "But he looked at them and said: What then is this that is written: The stone that the builders rejected, this has become the cornerstone?",
   "M": "Jesus looked directly at them and asked: Then what is the meaning of that which is written: The stone the builders rejected has become the cornerstone?",
   "T": "Jesus looked at them and said: Then what does this scripture mean? — The stone the builders rejected has become the cornerstone."
  },
  "18": {
   "L": "Everyone who falls on that stone will be broken to pieces, and on whomever it falls, it will crush him.",
   "M": "Everyone who falls on that stone will be broken to pieces; anyone on whom it falls will be crushed.",
   "T": "Everyone who falls on that stone will be shattered; whoever it falls on will be crushed."
  },
  "19": {
   "L": "And the scribes and the chief priests sought to lay hands on him at that hour, but they feared the people, for they perceived that he had told this parable against them.",
   "M": "The teachers of the law and the chief priests looked for a way to arrest him immediately, because they knew he had spoken this parable against them. But they were afraid of the people.",
   "T": "The teachers of the law and the chief priests looked for a way to arrest him right then, because they knew the parable was aimed at them. But they were afraid of the people."
  },
  "20": {
   "L": "And watching him closely, they sent spies who pretended to be righteous, in order to catch him in his word, so as to hand him over to the rule and to the authority of the governor.",
   "M": "Keeping a close watch on him, they sent spies who pretended to be sincere. They hoped to catch Jesus in something he said so that they might hand him over to the power and authority of the governor.",
   "T": "They watched closely and sent agents who posed as sincere questioners. Their plan was to trap him in his words and hand him over to the authority of the Roman governor."
  },
  "21": {
   "L": "And they questioned him, saying: Teacher, we know that you speak and teach rightly, and show no partiality but truly teach the way of God.",
   "M": "So the spies questioned him: Teacher, we know that you speak and teach what is right, and that you do not show partiality but teach the way of God in accordance with the truth.",
   "T": "So they asked him: Teacher, we know that you speak and teach truthfully. You show no partiality — you teach the way of God honestly."
  },
  "22": {
   "L": "Is it lawful for us to give tribute to Caesar, or not?",
   "M": "Is it right for us to pay taxes to Caesar or not?",
   "T": "Is it right for us to pay taxes to Caesar or not?"
  },
  "23": {
   "L": "But perceiving their craftiness, he said to them:",
   "M": "He saw through their duplicity and said to them:",
   "T": "He saw through their scheme and said:"
  },
  "24": {
   "L": "Show me a denarius. Whose image and inscription does it have? They said: Caesar's.",
   "M": "Show me a denarius. Whose image and inscription are on it? Caesar's, they replied.",
   "T": "Show me a denarius. Whose image and inscription are on it? They said: Caesar's."
  },
  "25": {
   "L": "And he said to them: Then render to Caesar the things that are Caesar's, and to God the things that are God's.",
   "M": "He said to them: Then give back to Caesar what is Caesar's, and to God what is God's.",
   "T": "Then he said: Give to Caesar what belongs to Caesar, and give to God what belongs to God."
  },
  "26": {
   "L": "And they were not able to catch him in his saying before the people, and marveling at his answer, they fell silent.",
   "M": "They were unable to trap him in what he had said there in public. And astonished by his answer, they became silent.",
   "T": "Unable to catch him in anything he said before the people, they were astonished by his answer and fell silent."
  },
  "27": {
   "L": "And certain Sadducees came to him, those who say there is no resurrection,",
   "M": "Some of the Sadducees, who say there is no resurrection, came to Jesus with a question.",
   "T": "Some Sadducees — who deny the resurrection — came and questioned him."
  },
  "28": {
   "L": "and they questioned him, saying: Teacher, Moses wrote to us that if a man's brother dies, having a wife but childless, the man must take the wife and raise up offspring for his brother.",
   "M": "Teacher, they said, Moses wrote for us that if a man's brother dies and leaves a wife but no children, the man must marry the widow and raise up offspring for his brother.",
   "T": "Teacher, they said, Moses wrote that if a man's brother dies leaving a wife but no children, the surviving brother must marry the widow and raise children for his brother."
  },
  "29": {
   "L": "There were therefore seven brothers; and the first, taking a wife, died childless.",
   "M": "Now there were seven brothers. The first one married a woman and died childless.",
   "T": "Now there were seven brothers. The first married a woman and died without children."
  },
  "30": {
   "L": "And the second,",
   "M": "The second",
   "T": "The second"
  },
  "31": {
   "L": "and the third took her, and likewise all seven also left no children and died.",
   "M": "and then the third married her, and in the same way the seven died, leaving no children.",
   "T": "and then the third married her. In the same way all seven died, leaving no children."
  },
  "32": {
   "L": "Finally the woman also died.",
   "M": "Finally, the woman died too.",
   "T": "Last of all, the woman died too."
  },
  "33": {
   "L": "Therefore, in the resurrection, whose wife will she be? For the seven had her as wife.",
   "M": "Now then, at the resurrection whose wife will she be, since the seven were all married to her?",
   "T": "At the resurrection — whose wife will she be? For all seven had married her."
  },
  "34": {
   "L": "And Jesus said to them: The sons of this age marry and are given in marriage,",
   "M": "Jesus replied: The people of this age marry and are given in marriage.",
   "T": "Jesus answered: The people of this present age marry and are given in marriage."
  },
  "35": {
   "L": "but those who are counted worthy to attain to that age and to the resurrection from the dead neither marry nor are given in marriage,",
   "M": "But those who are considered worthy of taking part in the age to come and in the resurrection from the dead will neither marry nor be given in marriage,",
   "T": "But those found worthy to share in the age to come — in the resurrection from the dead — will neither marry nor be given in marriage."
  },
  "36": {
   "L": "for they cannot die any more, for they are equal to angels, and are sons of God, being sons of the resurrection.",
   "M": "and they can no longer die; for they are like the angels. They are God's children, since they are children of the resurrection.",
   "T": "They cannot die anymore, for they are like the angels — and as children of the resurrection, they are children of God."
  },
  "37": {
   "L": "But that the dead are raised, Moses also showed in the passage about the bush, when he calls the Lord the God of Abraham and God of Isaac and God of Jacob.",
   "M": "But in the account of the burning bush, even Moses showed that the dead rise, for he calls the Lord the God of Abraham, and the God of Isaac, and the God of Jacob.",
   "T": "Even Moses showed that the dead are raised, in the passage about the burning bush, where he calls the Lord the God of Abraham, the God of Isaac, and the God of Jacob."
  },
  "38": {
   "L": "Now he is not the God of the dead but of the living, for all live to him.",
   "M": "He is not the God of the dead, but of the living, for to him all are alive.",
   "T": "He is not the God of the dead but of the living — for in his sight, all are alive."
  },
  "39": {
   "L": "And some of the scribes answered, saying: Teacher, you have spoken well.",
   "M": "Some of the teachers of the law responded: Well said, teacher!",
   "T": "Some of the teachers of the law said: Well answered, Teacher!"
  },
  "40": {
   "L": "For they no longer dared to ask him anything.",
   "M": "And no one dared to ask him any more questions.",
   "T": "After that, no one dared ask him any more questions."
  },
  "41": {
   "L": "And he said to them: How do they say that the Christ is David's son?",
   "M": "Then Jesus said to them: Why is it said that the Messiah is the son of David?",
   "T": "Then Jesus said to them: How can people say the Messiah is David's son?"
  },
  "42": {
   "L": "For David himself says in the Book of Psalms: The LORD said to my Lord, Sit at my right hand,",
   "M": "David himself declares in the Book of Psalms: The Lord said to my Lord: Sit at my right hand",
   "T": "David himself writes in the Book of Psalms: The LORD said to my Lord: Sit at my right hand"
  },
  "43": {
   "L": "until I place your enemies as a footstool for your feet.",
   "M": "until I make your enemies a footstool for your feet.",
   "T": "until I make your enemies a footstool under your feet."
  },
  "44": {
   "L": "David therefore calls him Lord. How then is he his son?",
   "M": "David calls him Lord. How then can he be his son?",
   "T": "David calls him Lord — so how can he be David's son? He is greater than his ancestor."
  },
  "45": {
   "L": "And in the hearing of all the people he said to his disciples:",
   "M": "While all the people were listening, Jesus said to his disciples:",
   "T": "In the hearing of all the people, Jesus said to his disciples:"
  },
  "46": {
   "L": "Beware of the scribes, who like to walk about in long robes, and love greetings in the marketplaces and the best seats in the synagogues and places of honor at feasts,",
   "M": "Beware of the teachers of the law. They like to walk around in flowing robes and love to be greeted with respect in the marketplaces and have the most important seats in the synagogues and the places of honour at banquets.",
   "T": "Watch out for the teachers of the law. They love to parade around in long robes and enjoy being greeted with respect in the marketplaces. They take the best seats in the synagogues and the places of honour at banquets."
  },
  "47": {
   "L": "who devour widows' houses, and for a pretense pray at length. These will receive greater condemnation.",
   "M": "They devour widows' houses and for a show make lengthy prayers. These men will be punished most severely.",
   "T": "They prey on widows and take their homes, while putting on a show of long prayers. These men will face the harshest judgment."
  }
 },
 "21": {
  "1": {
   "L": "And looking up he saw the rich putting their gifts into the treasury.",
   "M": "As Jesus looked up, he saw the rich putting their gifts into the temple treasury.",
   "T": "Looking up, he saw wealthy people dropping their gifts into the temple treasury."
  },
  "2": {
   "L": "And he saw a certain poor widow putting in there two small copper coins.",
   "M": "He also saw a poor widow put in two very small copper coins.",
   "T": "He also saw a poor widow drop in two small copper coins."
  },
  "3": {
   "L": "And he said: Truly I say to you that this poor widow has put in more than all of them.",
   "M": "Truly I tell you, he said, this poor widow has put in more than all the others.",
   "T": "He said: Truly I tell you — this poor widow has given more than all of them."
  },
  "4": {
   "L": "For all these out of their abundance have put in gifts, but she out of her want has put in all the living that she had.",
   "M": "All these people gave their gifts out of their wealth; but she out of her poverty put in all she had to live on.",
   "T": "They all gave out of their surplus. She gave out of her poverty — everything she had to live on."
  },
  "5": {
   "L": "And as some were speaking about the temple, that it was adorned with fine stones and offerings, he said:",
   "M": "Some of his disciples were remarking about how the temple was adorned with beautiful stones and with gifts dedicated to God. But Jesus said:",
   "T": "Some disciples were admiring the temple — its beautiful stones and its gifts dedicated to God. Jesus said:"
  },
  "6": {
   "L": "As for these things which you see, the days will come in which there will not be left here stone upon stone that will not be thrown down.",
   "M": "As for what you see here, the time will come when not one stone will be left on another; every one of them will be thrown down.",
   "T": "As for all this you see — the days are coming when not one stone will be left on another. Every stone will be torn down."
  },
  "7": {
   "L": "And they asked him, saying: Teacher, when therefore will these things be, and what will be the sign when these things are about to happen?",
   "M": "Teacher, they asked, when will these things happen? And what will be the sign that they are about to take place?",
   "T": "Teacher, they asked, when will this happen? And what sign will tell us it is about to take place?"
  },
  "8": {
   "L": "And he said: See that you are not deceived. For many will come in my name, saying: I am he, and: The time is near. Do not go after them.",
   "M": "He replied: Watch out that you are not deceived. For many will come in my name, claiming: I am he, and: The time is near. Do not follow them.",
   "T": "He said: Be careful not to be deceived. Many will come in my name claiming, I am the one, and, The time is near. Do not follow them."
  },
  "9": {
   "L": "And when you hear of wars and disturbances, do not be terrified; for these things must happen first, but the end will not come immediately.",
   "M": "When you hear of wars and uprisings, do not be frightened. These things must happen first, but the end will not come right away.",
   "T": "When you hear of wars and revolts, do not panic. These things must happen first — but the end will not follow immediately."
  },
  "10": {
   "L": "Then he said to them: Nation will rise against nation, and kingdom against kingdom.",
   "M": "Then he said to them: Nation will rise against nation, and kingdom against kingdom.",
   "T": "Then he continued: Nation will rise against nation, kingdom against kingdom."
  },
  "11": {
   "L": "There will be great earthquakes and in various places plagues and famines, and there will be terrors and great signs from heaven.",
   "M": "There will be great earthquakes, famines and pestilences in various places, and fearful events and great signs from heaven.",
   "T": "There will be great earthquakes, famines, and plagues in various places — and terrifying events and great signs in the sky."
  },
  "12": {
   "L": "But before all these things, they will lay their hands on you and persecute you, handing you over to the synagogues and prisons, bringing you before kings and governors for my name's sake.",
   "M": "But before all this, they will seize you and persecute you. They will hand you over to synagogues and put you in prison, and you will be brought before kings and governors, and all on account of my name.",
   "T": "But before any of this, they will arrest you and persecute you. They will hand you over to synagogues and throw you in prison — you will be brought before kings and governors because of my name."
  },
  "13": {
   "L": "It will be an opportunity for you to testify.",
   "M": "And so you will bear testimony to me.",
   "T": "This will be your opportunity to testify about me."
  },
  "14": {
   "L": "Settle it therefore in your hearts not to premeditate how to defend yourself,",
   "M": "But make up your mind not to worry beforehand how you will defend yourselves.",
   "T": "So settle this in your hearts: do not prepare your defense in advance."
  },
  "15": {
   "L": "for I will give you a mouth and wisdom which all your adversaries will not be able to withstand or contradict.",
   "M": "For I will give you words and wisdom that none of your adversaries will be able to resist or contradict.",
   "T": "I will give you words and wisdom that none of your opponents will be able to stand against or refute."
  },
  "16": {
   "L": "And you will be delivered up even by parents and brothers and relatives and friends, and some of you they will put to death.",
   "M": "You will be betrayed even by parents, brothers and sisters, relatives and friends, and they will put some of you to death.",
   "T": "You will be betrayed — even by parents, brothers, relatives, and friends. Some of you will be put to death."
  },
  "17": {
   "L": "And you will be hated by all because of my name.",
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
   "T": "By your patient endurance you will secure your lives."
  },
  "20": {
   "L": "But when you see Jerusalem surrounded by armies, then know that its desolation has drawn near.",
   "M": "When you see Jerusalem being surrounded by armies, you will know that its desolation is near.",
   "T": "When you see Jerusalem surrounded by armies, know that its destruction is near."
  },
  "21": {
   "L": "Then let those in Judea flee to the mountains, and let those inside it depart, and let those in the country not enter into it,",
   "M": "Then let those in Judea flee to the mountains, let those in the city get out, and let those in the country not enter the city.",
   "T": "At that point, those in Judea must flee to the mountains. Those inside the city must get out. Those in the countryside must not go in."
  },
  "22": {
   "L": "because these are days of vengeance, to fulfill all things that are written.",
   "M": "For this is the time of punishment in fulfillment of all that has been written.",
   "T": "For these are days of judgment — the fulfillment of everything written in the Scriptures."
  },
  "23": {
   "L": "Woe to those who are pregnant and to those nursing in those days! For there will be great distress upon the land and wrath against this people.",
   "M": "How dreadful it will be in those days for pregnant women and nursing mothers! There will be great distress in the land and wrath against this people.",
   "T": "How terrible for pregnant women and nursing mothers in those days! There will be great suffering in the land and divine judgment on this people."
  },
  "24": {
   "L": "And they will fall by the edge of the sword and be led captive among all the nations, and Jerusalem will be trampled by the Gentiles until the times of the Gentiles are fulfilled.",
   "M": "They will fall by the sword and will be taken as prisoners to all the nations. Jerusalem will be trampled on by the Gentiles until the times of the Gentiles are fulfilled.",
   "T": "They will be killed by the sword and taken captive to all the nations. Jerusalem will be trampled by the Gentiles until the time appointed for the Gentiles comes to its end."
  },
  "25": {
   "L": "And there will be signs in sun and moon and stars, and on earth distress of nations in perplexity at the roaring of the sea and the waves,",
   "M": "There will be signs in the sun, moon and stars. On the earth, nations will be in anguish and perplexity at the roaring and tossing of the sea.",
   "T": "There will be signs in the sun, moon, and stars. On earth, nations will be in agony and bewilderment at the roaring of the sea and its crashing waves."
  },
  "26": {
   "L": "people fainting from fear and foreboding of what is coming on the world, for the powers of the heavens will be shaken.",
   "M": "People will faint from terror, apprehensive of what is coming on the world, for the heavenly bodies will be shaken.",
   "T": "People will faint from fear, terrified by what is coming upon the world — for the powers of the heavens will be shaken."
  },
  "27": {
   "L": "And then they will see the Son of Man coming in a cloud with power and great glory.",
   "M": "At that time they will see the Son of Man coming in a cloud with power and great glory.",
   "T": "Then they will see the Son of Man coming on the clouds with power and great glory."
  },
  "28": {
   "L": "But when these things begin to happen, stand up and lift up your heads, because your redemption is drawing near.",
   "M": "When these things begin to take place, stand up and lift up your heads, because your redemption is drawing near.",
   "T": "When these things begin to unfold, stand up and raise your heads — because your redemption is near."
  },
  "29": {
   "L": "And he told them a parable: Look at the fig tree, and all the trees.",
   "M": "He told them this parable: Look at the fig tree and all the trees.",
   "T": "He told them a parable: Look at the fig tree and every tree."
  },
  "30": {
   "L": "When they put forth their leaves, you already see and know for yourselves that summer is now near.",
   "M": "When they sprout leaves, you can see for yourselves and know that summer is near.",
   "T": "When they leaf out, you can see it and know for yourselves that summer is approaching."
  },
  "31": {
   "L": "So also you, when you see these things happening, know that the kingdom of God is near.",
   "M": "Even so, when you see these things happening, you know that the kingdom of God is near.",
   "T": "In the same way, when you see these things happening, know that the kingdom of God is close at hand."
  },
  "32": {
   "L": "Truly I say to you, this generation will not pass away until all things have taken place.",
   "M": "Truly I tell you, this generation will certainly not pass away until all these things have happened.",
   "T": "Truly I tell you: this generation will not pass away until all these things have taken place."
  },
  "33": {
   "L": "Heaven and earth will pass away, but my words will not pass away.",
   "M": "Heaven and earth will pass away, but my words will never pass away.",
   "T": "Heaven and earth will pass away, but my words will never pass away."
  },
  "34": {
   "L": "But take heed to yourselves, lest your hearts be weighed down with dissipation and drunkenness and cares of life, and that day come upon you suddenly like a trap.",
   "M": "Be careful, or your hearts will be weighed down with carousing, drunkenness and the anxieties of life, and that day will close on you suddenly like a trap.",
   "T": "Guard yourselves, or your hearts will be dulled by debauchery, drunkenness, and the worries of daily life — and that day will catch you off guard like a trap."
  },
  "35": {
   "L": "For it will come upon all who dwell on the face of all the earth.",
   "M": "For it will come on all those who live on the face of the whole earth.",
   "T": "For it will come upon everyone living on the face of the earth."
  },
  "36": {
   "L": "But stay awake at all times, praying that you may have strength to escape all these things that are about to happen, and to stand before the Son of Man.",
   "M": "Be always on the watch, and pray that you may be able to escape all that is about to happen, and that you may be able to stand before the Son of Man.",
   "T": "So be always alert, and pray for the strength to escape all these coming events and to stand before the Son of Man."
  },
  "37": {
   "L": "And every day he was teaching in the temple, but at night going out he lodged on the mount called the Mount of Olives.",
   "M": "Each day Jesus was teaching at the temple, and each evening he went out to spend the night on the hill called the Mount of Olives.",
   "T": "Each day Jesus taught in the temple, and each evening he went out to spend the night on the Mount of Olives."
  },
  "38": {
   "L": "And all the people came early in the morning to hear him in the temple.",
   "M": "And all the people came early in the morning to hear him at the temple.",
   "T": "All the people came early each morning to listen to him in the temple."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'luke')
        merge_tier(existing, LUKE_20_21, tier_key)
        save(tier_dir, 'luke', existing)
    print('Luke 20–21 written.')

if __name__ == '__main__':
    main()
