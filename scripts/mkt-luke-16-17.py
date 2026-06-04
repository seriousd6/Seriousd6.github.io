"""
MKT Luke chapters 16–17 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-luke-16-17.py

Translation decisions:
- G3126 (μαμωνᾶς): "mammon" (L) / "wealth"/"Money" (M) / "money" (T) — Aramaic loanword
  preserved in L for its foreignness; M uses natural English; T uses "money" to show
  the personification implicit in the original
- G86 (ᾅδης): "Hades" (L/M) / "the realm of the dead" (T) — NOT "hell"; "hell" imports
  later theological freight; Hades is the Greek underworld = place of the dead
- G2859 (κόλπος): "bosom" (L) / "side" (M/T) — Abraham's bosom evokes the place of
  honour at a banquet table; "side" is natural English
- G166 (αἰώνιος 16:9): "eternal" throughout — denotes age-to-come quality, not only
  endless duration; "eternal homes/dwellings" = the permanent realm of the resurrection age
- G5430 (φρόνιμος/φρονίμως 16:8): "shrewd/shrewdly" (L/M); T uses "street-smart" to
  capture the worldly savvy Jesus is commending (not the dishonesty)
- G5207/G5457 (υἱοὶ τοῦ αἰῶνος/φωτός 16:8): L: "sons of this age / sons of light";
  M/T: "people of this world / people of light"
- G4102 (πίστις 17:5,6,19): "faith" throughout all three tiers
- G4982 (σῴζω 17:19): L: "has saved you"; M: "has made you well"; T: "has healed you" —
  σῴζω covers both healing and salvation; the physical healing is foregrounded here
- G1787 (ἐντὸς ὑμῶν 17:21): L/M/T: "in your midst" — addressed to hostile Pharisees,
  so "among you" (Jesus' own presence = kingdom inauguration) is more defensible than
  "within you" (interior spiritual experience)
- G105 (ἀετοί 17:37): "eagles" in L/M/T — follows the Greek literally; some read this
  as Roman military imagery (eagle standards); "vultures" would be contextually natural
  but departs from the Greek word ἀετός
- G4625 (σκάνδαλα 17:1): L: "stumbling blocks"; M: "things that cause people to stumble";
  T: "stumbling blocks" — the social-harm sense is primary
- Luke 17:36 is absent from the best manuscripts (P75, Vaticanus) but present in Western
  tradition (paralleling Matt 24:40); included because the interlinear source contains it
- Aspect notes: aorists in the Flood/Lot comparisons (17:26-29) render as simple past
  narrative; the iterative imperfects (eating, drinking, marrying) rendered as simple past
  to preserve the sequential feel without over-stressing the ongoing action
- OT echo: Rich man/Lazarus (16:19-31) reverses Deuteronomy's prosperity-blessing
  equation; T tier surfaces this reversal
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

LUKE_16_17 = {
 "16": {
  "1": {
   "L": "And he said also to his disciples: There was a certain rich man who had a steward, and this one was accused before him of wasting his possessions.",
   "M": "Jesus also said to his disciples: There was a rich man whose manager was accused of wasting his possessions.",
   "T": "He said to his disciples: There was a rich man whose manager was charged with squandering his property."
  },
  "2": {
   "L": "And calling him he said to him: What is this I hear about you? Give an account of your stewardship, for you can no longer be steward.",
   "M": "So he called him in and asked him: What is this I hear about you? Give an account of your management, because you cannot be manager any longer.",
   "T": "He called him in and said: What is this I hear about you? Turn in your accounts—you can no longer be my manager."
  },
  "3": {
   "L": "And the steward said within himself: What shall I do, since my master takes away the stewardship from me? To dig I am not strong enough; to beg I am ashamed.",
   "M": "The manager said to himself: What shall I do now? My master is taking away my job. I'm not strong enough to dig, and I'm too ashamed to beg.",
   "T": "The manager said to himself: What am I going to do? My master is removing me from this position. I'm not strong enough to dig—and I'm ashamed to beg."
  },
  "4": {
   "L": "I have decided what to do, so that when I am removed from the stewardship they may receive me into their houses.",
   "M": "I know what I'll do so that, when I lose my job here, people will welcome me into their homes.",
   "T": "I know exactly what I'll do—so that when I am put out of this position, people will welcome me into their homes."
  },
  "5": {
   "L": "And summoning each one of his master's debtors, he said to the first: How much do you owe my master?",
   "M": "So he called in each one of his master's debtors. He asked the first: How much do you owe my master?",
   "T": "He called in each of his master's debtors one by one. To the first he said: How much do you owe my master?"
  },
  "6": {
   "L": "He said: A hundred baths of oil. And he said to him: Take your bill, and sit down quickly and write fifty.",
   "M": "A hundred jars of oil, he replied. The manager told him: Take your bill, sit down quickly, and write fifty.",
   "T": "A hundred jars of oil, the man said. The manager told him: Take your bill—sit down quickly and make it fifty."
  },
  "7": {
   "L": "Then he said to another: And you, how much do you owe? He said: A hundred kors of wheat. He said to him: Take your bill and write eighty.",
   "M": "Then he asked another: And how much do you owe? A hundred sacks of wheat, he replied. He told him: Take your bill and write eighty.",
   "T": "He said to another: And how much do you owe? A hundred sacks of wheat. Write eighty, he told him."
  },
  "8": {
   "L": "And the master commended the steward of unrighteousness because he had acted shrewdly; for the sons of this age are more shrewd toward their own generation than the sons of light.",
   "M": "The master commended the dishonest manager because he had acted shrewdly. For the people of this world are more shrewd in dealing with their own kind than are the people of light.",
   "T": "The master praised the dishonest manager for acting with such street-smart shrewdness. The people of this world are wiser in dealing with their own kind than the people of light."
  },
  "9": {
   "L": "And I say to you: Make for yourselves friends by means of the mammon of unrighteousness, so that when it fails they may receive you into eternal dwellings.",
   "M": "I tell you, use worldly wealth to gain friends for yourselves, so that when it is gone, you will be welcomed into eternal homes.",
   "T": "I tell you—use your worldly wealth to make friends, so that when it runs out, you will be welcomed into homes that last forever."
  },
  "10": {
   "L": "The one faithful in the least is also faithful in much, and the one unrighteous in the least is also unrighteous in much.",
   "M": "Whoever can be trusted with very little can also be trusted with much, and whoever is dishonest with very little will also be dishonest with much.",
   "T": "Whoever is trustworthy in the smallest things is trustworthy in larger ones—and whoever is dishonest in small matters will be dishonest in larger ones too."
  },
  "11": {
   "L": "If therefore you have not been faithful in the unrighteous mammon, who will entrust to you the true riches?",
   "M": "So if you have not been trustworthy in handling worldly wealth, who will trust you with true riches?",
   "T": "If you haven't been faithful with dishonest wealth, who will entrust you with what is genuinely valuable?"
  },
  "12": {
   "L": "And if you have not been faithful in that which belongs to another, who will give you that which is your own?",
   "M": "And if you have not been trustworthy with someone else's property, who will give you property of your own?",
   "T": "And if you haven't been faithful with what belongs to someone else, who will give you anything that is truly yours?"
  },
  "13": {
   "L": "No household servant can serve two masters; for either he will hate the one and love the other, or he will hold to the one and despise the other. You cannot serve God and mammon.",
   "M": "No one can serve two masters. Either you will hate the one and love the other, or you will be devoted to the one and despise the other. You cannot serve both God and Money.",
   "T": "No servant can serve two masters. Either you will hate one and love the other, or you will be devoted to one and despise the other. You cannot serve both God and money."
  },
  "14": {
   "L": "And the Pharisees, being lovers of money, heard all these things, and they were sneering at him.",
   "M": "The Pharisees, who loved money, heard all this and were sneering at Jesus.",
   "T": "The Pharisees—lovers of money—heard all this and scoffed at him."
  },
  "15": {
   "L": "And he said to them: You are those who justify yourselves before men, but God knows your hearts; for what is exalted among men is an abomination before God.",
   "M": "He said to them: You are the ones who justify yourselves in the eyes of others, but God knows your hearts. What people value highly is detestable in God's sight.",
   "T": "He said to them: You are the ones who make yourselves look righteous before people—but God sees your hearts. What human beings prize is an abomination in God's sight."
  },
  "16": {
   "L": "The Law and the Prophets were until John; since then the kingdom of God is proclaimed, and everyone is pressing into it.",
   "M": "The Law and the Prophets were proclaimed until John. Since that time, the good news of the kingdom of God is being preached, and everyone is forcing their way into it.",
   "T": "The Law and the Prophets pointed forward until John. From then on, the good news of God's kingdom is being announced—and everyone presses urgently into it."
  },
  "17": {
   "L": "But it is easier for heaven and earth to pass away than for one stroke of a letter of the Law to fall.",
   "M": "It is easier for heaven and earth to disappear than for the least stroke of a pen to drop out of the Law.",
   "T": "It is easier for heaven and earth to pass away than for the smallest stroke of the Law to become void."
  },
  "18": {
   "L": "Everyone who divorces his wife and marries another commits adultery, and the one who marries a woman divorced from her husband commits adultery.",
   "M": "Anyone who divorces his wife and marries another woman commits adultery, and the man who marries a divorced woman commits adultery.",
   "T": "Anyone who divorces his wife and marries another commits adultery—and whoever marries a woman divorced from her husband commits adultery."
  },
  "19": {
   "L": "Now there was a certain rich man, and he was clothed in purple and fine linen, and he feasted sumptuously every day.",
   "M": "There was a rich man who was dressed in purple and fine linen and who lived in luxury every day.",
   "T": "There was a rich man who dressed in purple and fine linen and feasted lavishly every single day."
  },
  "20": {
   "L": "And a certain poor man named Lazarus was laid at his gate, covered with sores,",
   "M": "At his gate was laid a beggar named Lazarus, covered with sores",
   "T": "At his gate lay a poor man named Lazarus—covered with sores,"
  },
  "21": {
   "L": "and desiring to be fed with what fell from the rich man's table. Moreover, even the dogs came and licked his sores.",
   "M": "and longing to eat what fell from the rich man's table. Even the dogs came and licked his sores.",
   "T": "longing to be fed with whatever scraps fell from the rich man's table. Even the dogs came and licked his sores."
  },
  "22": {
   "L": "And it came to pass that the poor man died and was carried by the angels into Abraham's bosom. The rich man also died and was buried.",
   "M": "The time came when the beggar died and the angels carried him to Abraham's side. The rich man also died and was buried.",
   "T": "The beggar died, and the angels carried him to Abraham's side. The rich man also died—and was buried."
  },
  "23": {
   "L": "And in Hades he lifted up his eyes, being in torment, and sees Abraham far off and Lazarus in his bosom.",
   "M": "In Hades, where he was in torment, he looked up and saw Abraham far away, with Lazarus beside him.",
   "T": "In Hades, in the depths of his torment, he looked up and saw Abraham—far away—with Lazarus at his side."
  },
  "24": {
   "L": "And calling out he said: Father Abraham, have mercy on me and send Lazarus, that he may dip the tip of his finger in water and cool my tongue; for I am in anguish in this flame.",
   "M": "So he called to him: Father Abraham, have pity on me and send Lazarus to dip the tip of his finger in water and cool my tongue, because I am in agony in this fire.",
   "T": "He called out: Father Abraham, have mercy on me! Send Lazarus to dip the tip of his finger in water and cool my tongue—I am in agony in this fire!"
  },
  "25": {
   "L": "But Abraham said: Child, remember that you in your lifetime received your good things, and likewise Lazarus the bad things; but now he is comforted here, and you are in anguish.",
   "M": "But Abraham replied: Son, remember that in your lifetime you received your good things, while Lazarus received bad things, but now he is comforted here and you are in agony.",
   "T": "But Abraham said: Child, remember—in your lifetime you received every good thing, and Lazarus received every hard thing. Now he is comforted here, and you are in agony."
  },
  "26": {
   "L": "And besides all this, between us and you a great chasm has been fixed, so that those wishing to pass from here to you are not able, and none may cross from there to us.",
   "M": "And besides all this, between us and you a great chasm has been set in place, so that those who want to go from here to you cannot, nor can anyone cross over from there to us.",
   "T": "And besides all this, a great chasm has been fixed between us and you—so that no one who wishes to cross from here to you is able, and no one can cross from there to reach us."
  },
  "27": {
   "L": "And he said: Then I ask you, father, that you would send him to my father's house—",
   "M": "He answered: Then I beg you, father, send Lazarus to my family,",
   "T": "He said: Then I beg you, father—send him to my father's household."
  },
  "28": {
   "L": "for I have five brothers—so that he may warn them, lest they also come into this place of torment.",
   "M": "for I have five brothers. Let him warn them, so that they will not also come to this place of torment.",
   "T": "I have five brothers—let him warn them, so they will not also end up in this place of torment."
  },
  "29": {
   "L": "But Abraham says: They have Moses and the Prophets; let them hear them.",
   "M": "Abraham replied: They have Moses and the Prophets; let them listen to them.",
   "T": "Abraham said: They have Moses and the Prophets—let them listen to them."
  },
  "30": {
   "L": "But he said: No, father Abraham, but if someone from the dead goes to them, they will repent.",
   "M": "No, father Abraham, he said, but if someone from the dead goes to them, they will repent.",
   "T": "No, father Abraham, he said—but if someone from the dead goes to them, they will turn back to God."
  },
  "31": {
   "L": "He said to him: If they do not hear Moses and the Prophets, neither will they be persuaded if someone rises from the dead.",
   "M": "He said to him: If they do not listen to Moses and the Prophets, they will not be convinced even if someone rises from the dead.",
   "T": "He replied: If they will not hear Moses and the Prophets, they will not be convinced even if someone rises from the dead."
  }
 },
 "17": {
  "1": {
   "L": "And he said to his disciples: It is impossible that stumbling blocks not come, but woe to him through whom they come!",
   "M": "Jesus said to his disciples: Things that cause people to stumble are bound to come, but woe to anyone through whom they come.",
   "T": "He said to his disciples: It is inevitable that stumbling blocks will come—but woe to the one through whom they come."
  },
  "2": {
   "L": "It would be better for him if a millstone were hung around his neck and he were thrown into the sea, than that he should cause one of these little ones to stumble.",
   "M": "It would be better for them to be thrown into the sea with a millstone tied round their neck than to cause one of these little ones to stumble.",
   "T": "Better to be thrown into the sea with a millstone around your neck than to cause one of these little ones to fall."
  },
  "3": {
   "L": "Pay attention to yourselves. If your brother sins, rebuke him, and if he repents, forgive him.",
   "M": "So watch yourselves. If a brother or sister sins against you, rebuke them; and if they repent, forgive them.",
   "T": "Watch yourselves carefully. If a brother or sister sins, rebuke them—and if they repent, forgive them."
  },
  "4": {
   "L": "And if he sins against you seven times in the day, and turns to you seven times saying: I repent, you shall forgive him.",
   "M": "Even if they sin against you seven times in a day and seven times come back to you saying, I repent, you must forgive them.",
   "T": "Even if they sin against you seven times in a single day—and seven times turn back saying: I repent—you must forgive them."
  },
  "5": {
   "L": "And the apostles said to the Lord: Increase our faith.",
   "M": "The apostles said to the Lord: Increase our faith!",
   "T": "The apostles said to the Lord: Give us more faith."
  },
  "6": {
   "L": "And the Lord said: If you had faith like a grain of mustard seed, you would say to this mulberry tree: Be uprooted and be planted in the sea, and it would obey you.",
   "M": "He replied: If you have faith as small as a mustard seed, you can say to this mulberry tree, Be uprooted and planted in the sea, and it will obey you.",
   "T": "The Lord said: If you had faith even as small as a mustard seed, you could say to this mulberry tree: Be pulled up and planted in the sea—and it would obey you."
  },
  "7": {
   "L": "But who among you, having a servant plowing or tending sheep, will say to him when he has come in from the field: Come at once and recline at table?",
   "M": "Suppose one of you has a servant ploughing or looking after the sheep. Will he say to the servant when he comes in from the field: Come along now and sit down to eat?",
   "T": "Suppose one of you has a servant ploughing or tending sheep. When the servant comes in from the field, would you say: Come in right now and sit down to eat?"
  },
  "8": {
   "L": "But will he not say to him: Prepare something for my supper, and girding yourself serve me while I eat and drink, and after these things you yourself shall eat and drink?",
   "M": "Won't he rather say: Prepare my supper, get yourself ready and wait on me while I eat and drink; after that you may eat and drink?",
   "T": "No—you would say: Prepare my supper, get yourself ready, and serve me while I eat and drink. After that you may eat and drink."
  },
  "9": {
   "L": "Does he have any gratitude to the servant because he did the things commanded? I think not.",
   "M": "Will he thank the servant because he did what he was told to do? I think not.",
   "T": "Does he thank the servant for doing what he was told to do? Of course not."
  },
  "10": {
   "L": "So you also, when you have done all the things commanded you, say: We are unprofitable servants; we have only done what we were obligated to do.",
   "M": "So you also, when you have done everything you were told to do, should say: We are unworthy servants; we have only done our duty.",
   "T": "In the same way, when you have done everything you were ordered to do, say: We are unworthy servants—we have only done what was required of us."
  },
  "11": {
   "L": "And it came to pass, as he was going to Jerusalem, that he was passing through the midst of Samaria and Galilee.",
   "M": "Now on his way to Jerusalem, Jesus travelled along the border between Samaria and Galilee.",
   "T": "As he made his way to Jerusalem, Jesus traveled along the border region between Samaria and Galilee."
  },
  "12": {
   "L": "And as he entered into a certain village, there met him ten leprous men, who stood at a distance",
   "M": "As he was going into a village, ten men who had leprosy met him. They stood at a distance",
   "T": "Entering a village, he was met by ten men with leprosy. They stood at a distance"
  },
  "13": {
   "L": "and they lifted up their voice, saying: Jesus, Master, have mercy on us.",
   "M": "and called out in a loud voice: Jesus, Master, have pity on us!",
   "T": "and called out with one voice: Jesus, Master, have mercy on us!"
  },
  "14": {
   "L": "And when he saw them, he said to them: Go and show yourselves to the priests. And it came to pass, as they were going, they were cleansed.",
   "M": "When he saw them, he said: Go, show yourselves to the priests. And as they went, they were cleansed.",
   "T": "When he saw them, he said: Go—show yourselves to the priests. And as they went, they were cleansed."
  },
  "15": {
   "L": "And one of them, when he saw that he was healed, returned, glorifying God with a loud voice.",
   "M": "One of them, when he saw he was healed, came back, praising God in a loud voice.",
   "T": "One of them, seeing that he had been healed, turned back—praising God with a loud voice."
  },
  "16": {
   "L": "And he fell on his face before his feet, giving him thanks. And he was a Samaritan.",
   "M": "He threw himself at Jesus' feet and thanked him—and he was a Samaritan.",
   "T": "He fell at Jesus' feet, face down, and gave him thanks. He was a Samaritan."
  },
  "17": {
   "L": "And Jesus answering said: Were not ten cleansed? But where are the nine?",
   "M": "Jesus asked: Were not all ten cleansed? Where are the other nine?",
   "T": "Jesus said: Were not all ten cleansed? Where are the other nine?"
  },
  "18": {
   "L": "Was no one found who returned to give glory to God except this foreigner?",
   "M": "Has no one returned to give praise to God except this foreigner?",
   "T": "Was no one found to turn back and give glory to God—except this outsider?"
  },
  "19": {
   "L": "And he said to him: Rise and go; your faith has saved you.",
   "M": "Then he said to him: Rise and go; your faith has made you well.",
   "T": "He said to him: Rise and go—your faith has healed you."
  },
  "20": {
   "L": "And being asked by the Pharisees when the kingdom of God was coming, he answered them and said: The kingdom of God does not come with observation,",
   "M": "Once, on being asked by the Pharisees when the kingdom of God would come, Jesus replied: The coming of the kingdom of God is not something that can be observed,",
   "T": "The Pharisees asked him when the kingdom of God would come. He answered: The kingdom of God does not come in ways that can be tracked and watched;"
  },
  "21": {
   "L": "nor will they say: Look, here! or: There! For behold, the kingdom of God is in the midst of you.",
   "M": "nor will people say, Here it is, or There it is, because the kingdom of God is in your midst.",
   "T": "no one will say: Look, here it is! or There! For the kingdom of God is already in your midst."
  },
  "22": {
   "L": "And he said to the disciples: Days will come when you will desire to see one of the days of the Son of Man, and you will not see it.",
   "M": "Then he said to his disciples: The time is coming when you will long to see one of the days of the Son of Man, but you will not see it.",
   "T": "He said to his disciples: Days are coming when you will long to see just one of the days of the Son of Man—and you will not see it."
  },
  "23": {
   "L": "And they will say to you: Look, there! or: Look, here! Do not go away or follow after them.",
   "M": "People will tell you, There he is! or Here he is! Do not go running off after them.",
   "T": "They will say: Look, there! or Look, here! Don't go running after them."
  },
  "24": {
   "L": "For as the lightning, when it flashes, shines from one end of the sky to the other end under the sky, so will the Son of Man be in his day.",
   "M": "For the Son of Man in his day will be like the lightning, which flashes and lights up the sky from one end to the other.",
   "T": "For just as lightning flashes and lights up the sky from one horizon to the other, so will the Son of Man be in his day."
  },
  "25": {
   "L": "But first he must suffer many things and be rejected by this generation.",
   "M": "But first he must suffer many things and be rejected by this generation.",
   "T": "But first he must suffer many things and be rejected by this generation."
  },
  "26": {
   "L": "And just as it was in the days of Noah, so also will it be in the days of the Son of Man.",
   "M": "Just as it was in the days of Noah, so also will it be in the days of the Son of Man.",
   "T": "Just as things were in the days of Noah, so it will be in the days of the Son of Man."
  },
  "27": {
   "L": "They were eating, they were drinking, they were marrying, they were being given in marriage, until the day Noah entered the ark, and the flood came and destroyed them all.",
   "M": "People were eating, drinking, marrying and being given in marriage up to the day Noah entered the ark. Then the flood came and destroyed them all.",
   "T": "They ate, they drank, they married and were given in marriage—right up to the day Noah entered the ark. Then the flood came and swept them all away."
  },
  "28": {
   "L": "Likewise, just as it was in the days of Lot: they were eating, they were drinking, they were buying, they were selling, they were planting, they were building;",
   "M": "It was the same in the days of Lot. People were eating and drinking, buying and selling, planting and building.",
   "T": "It was the same in the days of Lot. They ate and drank, bought and sold, planted and built—"
  },
  "29": {
   "L": "but on the day Lot went out from Sodom, fire and sulfur rained from heaven and destroyed them all.",
   "M": "But the day Lot left Sodom, fire and sulphur rained down from heaven and destroyed them all.",
   "T": "but on the day Lot walked out of Sodom, fire and sulfur rained from heaven and destroyed them all."
  },
  "30": {
   "L": "So will it be on the day the Son of Man is revealed.",
   "M": "It will be just like this on the day the Son of Man is revealed.",
   "T": "So it will be on the day the Son of Man is revealed."
  },
  "31": {
   "L": "On that day, the one who is on the housetop and his belongings are in the house, let him not come down to take them; and likewise the one in the field, let him not turn back.",
   "M": "On that day no one who is on the housetop, with possessions inside, should go down to get them. Likewise, no one in the field should go back for anything.",
   "T": "On that day, if you are on the roof, don't go down to take anything from inside. And if you are in the field, don't turn back."
  },
  "32": {
   "L": "Remember Lot's wife.",
   "M": "Remember Lot's wife!",
   "T": "Remember Lot's wife."
  },
  "33": {
   "L": "Whoever seeks to preserve his life will lose it, but whoever loses his life will keep it alive.",
   "M": "Whoever tries to keep their life will lose it, and whoever loses their life will preserve it.",
   "T": "Whoever tries to hold on to their life will lose it—but whoever lets their life go will keep it."
  },
  "34": {
   "L": "I tell you, on that night there will be two men on one bed; the one will be taken and the other will be left.",
   "M": "I tell you, on that night two people will be in one bed; one will be taken and the other left.",
   "T": "I tell you—in that night, two will be lying in one bed. One will be taken, the other left."
  },
  "35": {
   "L": "There will be two women grinding together; the one will be taken and the other will be left.",
   "M": "Two women will be grinding grain together; one will be taken and the other left.",
   "T": "Two women will be grinding grain together—one will be taken, the other left."
  },
  "36": {
   "L": "Two men will be in the field; the one will be taken and the other will be left.",
   "M": "Two men will be in the field; one will be taken and the other left.",
   "T": "Two men will be in the field—one will be taken, the other left."
  },
  "37": {
   "L": "And answering they say to him: Where, Lord? And he said to them: Where the body is, there also the eagles will be gathered.",
   "M": "Where, Lord? they asked. He replied: Where there is a dead body, there the eagles will gather.",
   "T": "Where will this happen, Lord? they asked. He said: Where the corpse is, there the eagles will flock together."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'luke')
        merge_tier(existing, LUKE_16_17, tier_key)
        save(tier_dir, 'luke', existing)
    print('Luke 16–17 written.')

if __name__ == '__main__':
    main()
