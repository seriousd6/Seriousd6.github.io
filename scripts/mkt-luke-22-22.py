"""
MKT Luke chapter 22 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-luke-22-22.py

Translation decisions:
- G3957 (πάσχα, vv. 1, 7, 8, 11, 13, 15): "Passover" throughout — technical term, not
  translated; same approach as Matthew and Mark scripts
- G2169 (εὐχαριστέω, v. 17, 19): "giving thanks" (L/M/T) — the eucharistic word; L preserves
  the participial form, T renders as an action
- G4983 (σῶμα, v. 19): "body" throughout — the eucharistic institution narrative; rendered
  plainly as "body" in all three tiers to let the statement speak for itself
- G1242 (διαθήκη, v. 20): "covenant" in L/M; T "the covenant sealed in my blood" — the word is
  legal/covenantal and the T tier makes the sealing act explicit
- G120 (αἷμα, v. 20): "blood" throughout — both literal (covenant ratification) and
  sacrificial; all three tiers use "blood" without substitution
- G2516 (ἐκχύννομαι, v. 20): "poured out" in all tiers — the sacrificial overtone of blood
  poured out (as in Exodus 24:8 LXX) must be preserved; "shed" (L) / "poured out" (M/T)
- G3173 (μέγας, v. 24): "greatest" in the dispute about greatness — consistent with Luke 9
  rendering
- G2962 (κύριος, vv. 31, 33, 34, 38, 49, 61): "Lord" throughout — Jesus as Lord; Peter's
  address in v33; the Lord's look in v61
- G4151 (πνεῦμα in v3): "Satan entered into Judas" — no πνεῦμα in this verse; it is Satan
  himself entering; no pneuma translation issue here
- G3986 (πειρασμός, vv. 28, 40, 46): "temptations / trials" (L); "trials" (M); "tests /
  times of testing" (T) — in v40/46 "into temptation" means "into testing / trial";
  the prayer context (Lord's Prayer echo) governs
- G5590 (ψυχή, v. 43): not present here; the strengthening angel passage uses "angel"
- G1518 (εἰρηνοποιός): not in chapter; cf. the sword passage (v38)
- G3162 (μάχαιρα, vv. 36, 38, 49, 52): "sword" throughout — the disciples literally have
  swords; the T tier for v38 "It is enough" treats Jesus' "Enough!" as closure of a
  misunderstanding, not theological sanction for violence
- G2206 (ζηλόω): not present; cf. "zealots" background in disciples list (Luke 6)
- Textual note (v. 43–44): The angel and the bloody sweat are disputed (absent in key MSS:
  p75, Codex B, Codex A). They appear in the majority tradition. All three tiers translate
  them, but the L tier is especially careful to render the rare word ἱδρώς (sweat) literally
- Textual note (v. 19b–20): "which is given for you…" and "in my blood" (the longer text)
  follow the received text; Codex D and a few Old Latin MSS have the shorter text (only v19a),
  but the longer text is in p75 and the great majority; all three tiers use the longer text
- Aspect notes: v54 "they seized him" aorist — punctiliar; v55 imperfect "were sitting
  together" — ongoing scene; v60 "immediately" + aorist rooster crow — punctiliar completion
- G622 (ἀπόλλυμι, vv. 33, 56): not present; the relevant term in v56 is "he was with him" —
  the denial is set up by recognition; no special term needed
- G27 (ἀγαπητός): not present in ch22; beloved → prior chapters
- Thematic note: The cup shared twice (vv. 17, 20) — first cup is the Passover cup; second
  is the covenant cup after supper. Luke preserves both. The T tier makes the distinction
  by noting "After supper" for v20 and the new covenant language
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

LUKE_22 = {
 "22": {
  "1": {
   "L": "Now the Feast of Unleavened Bread drew near, which is called the Passover.",
   "M": "Now the Festival of Unleavened Bread, called the Passover, was approaching.",
   "T": "The Festival of Unleavened Bread — called the Passover — was drawing near."
  },
  "2": {
   "L": "And the chief priests and the scribes were seeking how to put him to death, for they were afraid of the people.",
   "M": "And the chief priests and the teachers of the law were looking for some way to get rid of Jesus, for they were afraid of the people.",
   "T": "The chief priests and teachers of the law were searching for a way to kill Jesus, but they were afraid of the people."
  },
  "3": {
   "L": "Then Satan entered into Judas, who was called Iscariot, being of the number of the twelve.",
   "M": "Then Satan entered Judas, called Iscariot, one of the Twelve.",
   "T": "At this point, Satan entered Judas called Iscariot — one of the Twelve."
  },
  "4": {
   "L": "And going away he conferred with the chief priests and captains about how he might deliver him up to them.",
   "M": "And Judas went to the chief priests and the officers of the temple guard and discussed with them how he might betray Jesus.",
   "T": "Judas went to the chief priests and temple officers to discuss how he could hand Jesus over to them."
  },
  "5": {
   "L": "And they were glad and agreed to give him silver.",
   "M": "They were delighted and agreed to give him money.",
   "T": "They were glad and offered him money."
  },
  "6": {
   "L": "And he consented, and was seeking an opportunity to deliver him up to them apart from the crowd.",
   "M": "He consented, and watched for an opportunity to hand Jesus over to them when no crowd was present.",
   "T": "He agreed, and from then on looked for a chance to hand Jesus over when no crowd was around."
  },
  "7": {
   "L": "Then came the day of Unleavened Bread, on which the Passover lamb had to be sacrificed.",
   "M": "Then came the day of Unleavened Bread on which the Passover lamb had to be sacrificed.",
   "T": "Then came the day of Unleavened Bread, when the Passover lamb had to be slaughtered."
  },
  "8": {
   "L": "And he sent Peter and John, saying: Go and prepare the Passover for us, that we may eat.",
   "M": "Jesus sent Peter and John, saying: Go and make preparations for us to eat the Passover.",
   "T": "Jesus sent Peter and John ahead: Go and prepare the Passover meal for us to eat."
  },
  "9": {
   "L": "And they said to him: Where do you want us to prepare?",
   "M": "Where do you want us to prepare for it? they asked.",
   "T": "Where do you want us to prepare it? they asked."
  },
  "10": {
   "L": "And he said to them: Behold, when you have entered the city, a man carrying a jar of water will meet you; follow him into the house into which he enters.",
   "M": "He replied: As you enter the city, a man carrying a jar of water will meet you. Follow him to the house that he enters,",
   "T": "He said: When you enter the city, a man carrying a water jar will meet you. Follow him to the house he enters."
  },
  "11": {
   "L": "And you will say to the master of that house: The Teacher says to you: Where is the guest room where I may eat the Passover with my disciples?",
   "M": "and say to the owner of the house: The Teacher asks: Where is the guest room, where I may eat the Passover with my disciples?",
   "T": "Tell the owner of the house: The Teacher asks — Where is the guest room where I may eat the Passover with my disciples?"
  },
  "12": {
   "L": "And that one will show you a large upper room that is furnished; prepare there.",
   "M": "He will show you a large room upstairs, all furnished. Make preparations there.",
   "T": "He will show you a large upper room, already furnished. Make your preparations there."
  },
  "13": {
   "L": "And going they found it just as he had told them, and they prepared the Passover.",
   "M": "They left and found things just as Jesus had told them. So they prepared the Passover.",
   "T": "They went and found everything exactly as he had said. And they prepared the Passover."
  },
  "14": {
   "L": "And when the hour came, he reclined at table, and the apostles with him.",
   "M": "When the hour came, Jesus and his apostles reclined at the table.",
   "T": "When the hour arrived, Jesus took his place at the table with his apostles."
  },
  "15": {
   "L": "And he said to them: With longing I have desired to eat this Passover with you before I suffer.",
   "M": "And he said to them: I have eagerly desired to eat this Passover with you before I suffer.",
   "T": "He said to them: I have deeply longed to share this Passover with you before my suffering."
  },
  "16": {
   "L": "For I say to you that I will not eat it until it is fulfilled in the kingdom of God.",
   "M": "For I tell you, I will not eat it again until it finds fulfillment in the kingdom of God.",
   "T": "For I tell you: I will not eat it again until it finds its fulfillment in the kingdom of God."
  },
  "17": {
   "L": "And taking a cup, giving thanks, he said: Take this and divide it among yourselves.",
   "M": "After taking the cup, he gave thanks and said: Take this and divide it among you.",
   "T": "He took the cup, gave thanks, and said: Take this and share it among yourselves."
  },
  "18": {
   "L": "For I say to you that I will not drink from the fruit of the vine from now on until the kingdom of God comes.",
   "M": "For I tell you I will not drink again from the fruit of the vine until the kingdom of God comes.",
   "T": "For I tell you: I will not drink from the fruit of the vine again until the kingdom of God comes."
  },
  "19": {
   "L": "And taking bread, giving thanks, he broke it and gave it to them, saying: This is my body which is given for you. Do this in remembrance of me.",
   "M": "And he took bread, gave thanks and broke it, and gave it to them, saying: This is my body given for you; do this in remembrance of me.",
   "T": "He took bread, gave thanks, broke it, and gave it to them, saying: This is my body — given for you. Do this in remembrance of me."
  },
  "20": {
   "L": "And likewise the cup after supper, saying: This cup is the new covenant in my blood, which is poured out for you.",
   "M": "In the same way, after the supper he took the cup, saying: This cup is the new covenant in my blood, which is poured out for you.",
   "T": "After supper he took the cup in the same way, saying: This cup is the new covenant — sealed in my blood that is poured out for you."
  },
  "21": {
   "L": "But behold, the hand of the one who betrays me is with me on the table.",
   "M": "But the hand of him who is going to betray me is with mine on the table.",
   "T": "But look — the hand of the one who will betray me is here at the table with mine."
  },
  "22": {
   "L": "For the Son of Man goes as it has been determined, but woe to that man through whom he is betrayed!",
   "M": "The Son of Man will go as it has been decreed. But woe to that man who betrays him!",
   "T": "The Son of Man goes as it is written — but woe to that man through whom he is betrayed!"
  },
  "23": {
   "L": "And they began to inquire among themselves which of them it was who was about to do this thing.",
   "M": "They began to question among themselves which of them it might be who would do this.",
   "T": "They began to ask one another which of them it could possibly be who would do this."
  },
  "24": {
   "L": "And there also arose a dispute among them, which of them was considered to be greatest.",
   "M": "A dispute also arose among them as to which of them was considered to be greatest.",
   "T": "A dispute also broke out among them — which of them should be regarded as the greatest."
  },
  "25": {
   "L": "And he said to them: The kings of the nations lord it over them, and those who exercise authority over them are called benefactors.",
   "M": "Jesus said to them: The kings of the Gentiles lord it over them; and those who exercise authority over them call themselves Benefactors.",
   "T": "He said to them: Among the nations, kings dominate their subjects, and those who hold authority are called Benefactors."
  },
  "26": {
   "L": "But it is not so with you; rather, let the greatest among you become as the youngest, and the leader as one who serves.",
   "M": "But you are not to be like that. Instead, the greatest among you should be like the youngest, and the one who rules like the one who serves.",
   "T": "But with you it must be different. The greatest among you must become like the youngest, and the leader like the one who serves."
  },
  "27": {
   "L": "For who is greater: the one reclining at table or the one who serves? Is it not the one reclining at table? But I am among you as the one who serves.",
   "M": "For who is greater, the one who is at the table or the one who serves? Is it not the one who is at the table? But I am among you as one who serves.",
   "T": "Which is greater — the one reclining at the table, or the one serving? Surely the one at the table. Yet I am here among you as the one who serves."
  },
  "28": {
   "L": "You are those who have stayed with me in my trials.",
   "M": "You are those who have stood by me in my trials.",
   "T": "You are the ones who have stood with me through all my trials."
  },
  "29": {
   "L": "And I assign to you, just as my Father has assigned to me, a kingdom,",
   "M": "And I confer on you a kingdom, just as my Father conferred one on me,",
   "T": "And I grant you a kingdom, just as my Father granted one to me —"
  },
  "30": {
   "L": "that you may eat and drink at my table in my kingdom and sit on thrones judging the twelve tribes of Israel.",
   "M": "so that you may eat and drink at my table in my kingdom and sit on thrones, judging the twelve tribes of Israel.",
   "T": "so that you will eat and drink at my table in my kingdom and sit on thrones governing the twelve tribes of Israel."
  },
  "31": {
   "L": "Simon, Simon, behold, Satan has demanded to sift you all like wheat.",
   "M": "Simon, Simon, Satan has asked to sift all of you as wheat.",
   "T": "Simon, Simon — Satan has demanded to sift you all like wheat."
  },
  "32": {
   "L": "But I have prayed for you that your faith may not fail. And when you have turned again, strengthen your brothers.",
   "M": "But I have prayed for you, Simon, that your faith may not fail. And when you have turned back, strengthen your brothers.",
   "T": "But I have prayed for you, Simon, that your faith would not fail. And when you have come back, strengthen your brothers."
  },
  "33": {
   "L": "And he said to him: Lord, I am ready to go with you both to prison and to death.",
   "M": "But he replied: Lord, I am ready to go with you to prison and to death.",
   "T": "Peter said: Lord, I am ready to go with you both to prison and to death."
  },
  "34": {
   "L": "And he said: I tell you, Peter, the rooster will not crow today until you have denied three times that you know me.",
   "M": "Jesus answered: I tell you, Peter, before the rooster crows today, you will deny three times that you know me.",
   "T": "Jesus said: I tell you, Peter — before the rooster crows today, you will deny three times that you know me."
  },
  "35": {
   "L": "And he said to them: When I sent you out without money bag or knapsack or sandals, did you lack anything? They said: Nothing.",
   "M": "Then Jesus asked them: When I sent you without purse, bag or sandals, did you lack anything? Nothing, they answered.",
   "T": "He asked them: When I sent you out without purse, bag, or sandals, did you lack anything? Nothing, they replied."
  },
  "36": {
   "L": "He said to them: But now, let the one who has a money bag take it, and likewise a knapsack. And let the one who has no sword sell his cloak and buy one.",
   "M": "He said to them: But now if you have a purse, take it, and also a bag; and if you don't have a sword, sell your cloak and buy one.",
   "T": "But now, he said, if you have a purse, take it — and a bag. And if you have no sword, sell your cloak and buy one."
  },
  "37": {
   "L": "For I tell you that this scripture must be fulfilled in me: And he was numbered with the transgressors. For indeed what is written about me has its fulfillment.",
   "M": "It is written: And he was numbered with the transgressors; and I tell you that this must be fulfilled in me. Yes, what is written about me is reaching its fulfillment.",
   "T": "For I tell you: this scripture must be fulfilled in me — He was counted among the lawless. What is written about me is coming to its fulfillment."
  },
  "38": {
   "L": "And they said: Lord, look, here are two swords. And he said to them: It is enough.",
   "M": "The disciples said: See, Lord, here are two swords. That is enough! he replied.",
   "T": "They said: Lord, look — we have two swords here. Enough of this! he said."
  },
  "39": {
   "L": "And going out, he proceeded as was his custom to the Mount of Olives, and the disciples also followed him.",
   "M": "Jesus went out as usual to the Mount of Olives, and his disciples followed him.",
   "T": "He went out as was his custom to the Mount of Olives, and his disciples followed him."
  },
  "40": {
   "L": "And when he arrived at the place, he said to them: Pray that you may not enter into temptation.",
   "M": "On reaching the place, he said to them: Pray that you will not fall into temptation.",
   "T": "When they reached the place, he said to them: Pray that you will not be brought to the test."
  },
  "41": {
   "L": "And he was withdrawn from them about a stone's throw, and kneeling down he prayed,",
   "M": "He withdrew about a stone's throw beyond them, knelt down and prayed,",
   "T": "He withdrew about a stone's throw, knelt down, and prayed:"
  },
  "42": {
   "L": "saying: Father, if you are willing, remove this cup from me. Nevertheless, not my will, but yours, be done.",
   "M": "Father, if you are willing, take this cup from me; yet not my will, but yours be done.",
   "T": "Father, if you are willing, take this cup from me — yet not my will, but yours be done."
  },
  "43": {
   "L": "And an angel from heaven appeared to him, strengthening him.",
   "M": "An angel from heaven appeared to him and strengthened him.",
   "T": "An angel from heaven appeared to him and gave him strength."
  },
  "44": {
   "L": "And being in agony he prayed more earnestly, and his sweat became like drops of blood falling down on the ground.",
   "M": "And being in anguish, he prayed more earnestly, and his sweat was like drops of blood falling to the ground.",
   "T": "And in his anguish he prayed even more intensely, and his sweat fell like drops of blood onto the ground."
  },
  "45": {
   "L": "And rising from prayer, coming to his disciples, he found them sleeping from grief,",
   "M": "When he rose from prayer and went back to the disciples, he found them asleep, exhausted from sorrow.",
   "T": "When he rose from prayer and returned to his disciples, he found them asleep — worn out from grief."
  },
  "46": {
   "L": "and he said to them: Why are you sleeping? Rise and pray, that you may not enter into temptation.",
   "M": "Why are you sleeping? he asked them. Get up and pray so that you will not fall into temptation.",
   "T": "Why are you sleeping? he said. Get up and pray, so that you will not be brought to the test."
  },
  "47": {
   "L": "While he was still speaking, behold, a crowd came, and the one called Judas, one of the twelve, was going before them; and he drew near to Jesus to kiss him.",
   "M": "While he was still speaking a crowd came up, and the man who was called Judas, one of the Twelve, was leading them. He approached Jesus to kiss him,",
   "T": "While he was still speaking, a crowd arrived — led by Judas, one of the Twelve. He came up to Jesus to kiss him."
  },
  "48": {
   "L": "But Jesus said to him: Judas, are you betraying the Son of Man with a kiss?",
   "M": "but Jesus asked him: Judas, are you betraying the Son of Man with a kiss?",
   "T": "Jesus said to him: Judas — are you betraying the Son of Man with a kiss?"
  },
  "49": {
   "L": "And when those around him saw what was about to happen, they said: Lord, shall we strike with the sword?",
   "M": "When Jesus' followers saw what was going to happen, they said: Lord, should we strike with our swords?",
   "T": "When those around him saw what was about to happen, they asked: Lord, shall we strike with our swords?"
  },
  "50": {
   "L": "And one of them struck the servant of the high priest and cut off his right ear.",
   "M": "And one of them struck the servant of the high priest, cutting off his right ear.",
   "T": "One of them struck the high priest's servant and cut off his right ear."
  },
  "51": {
   "L": "But Jesus answered and said: Stop! No more of this. And he touched his ear and healed him.",
   "M": "But Jesus answered: No more of this! And he touched the man's ear and healed him.",
   "T": "But Jesus said: No more of this! He touched the man's ear and healed him."
  },
  "52": {
   "L": "Then Jesus said to the chief priests and captains of the temple and elders who had come against him: Have you come out as against a robber, with swords and clubs?",
   "M": "Then Jesus said to the chief priests, the officers of the temple guard, and the elders, who had come for him: Am I leading a rebellion, that you have come with swords and clubs?",
   "T": "Then Jesus said to the chief priests, temple officers, and elders who had come for him: Have you come out with swords and clubs as though I were a revolutionary?"
  },
  "53": {
   "L": "When I was with you every day in the temple, you did not stretch out your hands against me. But this is your hour, and the power of darkness.",
   "M": "Every day I was with you in the temple courts, and you did not lay a hand on me. But this is your hour — when darkness reigns.",
   "T": "Day after day I was with you in the temple and you never laid a hand on me. But this is your hour — the hour of darkness."
  },
  "54": {
   "L": "And seizing him, they led him away and brought him into the house of the high priest. And Peter was following at a distance.",
   "M": "Then seizing him, they led him away and took him into the house of the high priest. Peter followed at a distance.",
   "T": "They seized him and led him away to the house of the high priest. Peter followed at a distance."
  },
  "55": {
   "L": "And when they had kindled a fire in the middle of the courtyard and sat down together, Peter was sitting among them.",
   "M": "And when some there had kindled a fire in the middle of the courtyard and had sat down together, Peter sat down with them.",
   "T": "They kindled a fire in the middle of the courtyard and sat together, and Peter sat among them."
  },
  "56": {
   "L": "And a servant girl, seeing him seated in the firelight and looking intently at him, said: This man was with him too.",
   "M": "A servant girl saw him seated there in the firelight. She looked closely at him and said: This man was with him.",
   "T": "A servant girl saw him sitting in the firelight, stared at him, and said: This man was with him too."
  },
  "57": {
   "L": "But he denied it, saying: Woman, I do not know him.",
   "M": "But he denied it. Woman, I don't know him, he said.",
   "T": "He denied it: Woman, I don't know him."
  },
  "58": {
   "L": "And shortly afterward someone else saw him and said: You also are one of them. But Peter said: Man, I am not.",
   "M": "A little later someone else saw him and said: You also are one of them. Man, I am not! Peter replied.",
   "T": "A little later, someone else noticed him: You are one of them too! Man, I am not! Peter said."
  },
  "59": {
   "L": "And about an hour later still another insisted, saying: In truth this man also was with him, for he is a Galilean too.",
   "M": "About an hour later another asserted: Certainly this fellow was with him, for he is a Galilean.",
   "T": "About an hour later another person insisted: This man really was with him — you can tell by his Galilean accent."
  },
  "60": {
   "L": "But Peter said: Man, I do not know what you are saying. And immediately, while he was still speaking, a rooster crowed.",
   "M": "Peter replied: Man, I don't know what you're talking about! Just as he was speaking, the rooster crowed.",
   "T": "Peter said: Man, I don't know what you're talking about! At that very moment, as he was still speaking, a rooster crowed."
  },
  "61": {
   "L": "And the Lord turned and looked at Peter. And Peter remembered the word of the Lord, how he had said to him: Before a rooster crows today, you will deny me three times.",
   "M": "The Lord turned and looked straight at Peter. Then Peter remembered the word the Lord had spoken to him: Before the rooster crows today, you will disown me three times.",
   "T": "The Lord turned and looked directly at Peter. And Peter remembered the Lord's words — Before the rooster crows today, you will deny me three times."
  },
  "62": {
   "L": "And he went out and wept bitterly.",
   "M": "And he went outside and wept bitterly.",
   "T": "He went outside and broke down weeping."
  },
  "63": {
   "L": "And the men who were holding Jesus mocked him and beat him.",
   "M": "The men who were guarding Jesus began mocking and beating him.",
   "T": "The men guarding Jesus began mocking him and beating him."
  },
  "64": {
   "L": "And blindfolding him, they kept asking him, saying: Prophesy! Who is it who struck you?",
   "M": "They blindfolded him and demanded: Prophesy! Who hit you?",
   "T": "They blindfolded him and demanded: Prophesy! Tell us — who just hit you?"
  },
  "65": {
   "L": "And they spoke many other things against him, blaspheming.",
   "M": "And they said many other insulting things to him.",
   "T": "And they hurled many other insults at him."
  },
  "66": {
   "L": "And when day came, the council of elders of the people gathered together, both chief priests and scribes; and they led him into their council, saying:",
   "M": "At daybreak the council of the elders of the people, both the chief priests and the teachers of the law, met together, and Jesus was led before them.",
   "T": "At daybreak the elders of the people — chief priests and teachers of the law — assembled. Jesus was brought before their council."
  },
  "67": {
   "L": "If you are the Christ, tell us. But he said to them: If I tell you, you will not believe,",
   "M": "If you are the Messiah, tell us. Jesus answered: If I tell you, you will not believe me,",
   "T": "If you are the Messiah, tell us! He answered: If I tell you, you will not believe."
  },
  "68": {
   "L": "and if I ask you, you will not answer.",
   "M": "and if I asked you, you would not answer.",
   "T": "And if I ask you, you will not answer."
  },
  "69": {
   "L": "But from now on the Son of Man will be seated at the right hand of the power of God.",
   "M": "But from now on, the Son of Man will be seated at the right hand of the mighty God.",
   "T": "But from this moment on, the Son of Man will be seated at the right hand of the power of God."
  },
  "70": {
   "L": "And they all said: Are you then the Son of God? And he said to them: You say that I am.",
   "M": "They all asked: Are you then the Son of God? He replied: You say that I am.",
   "T": "They all demanded: So you are the Son of God? He said: You are right to say I am."
  },
  "71": {
   "L": "And they said: What further need do we have of testimony? For we ourselves have heard it from his own mouth.",
   "M": "Then they said: Why do we need any more testimony? We have heard it from his own lips.",
   "T": "They said: What more testimony do we need? We have heard it from his own mouth."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'luke')
        merge_tier(existing, LUKE_22, tier_key)
        save(tier_dir, 'luke', existing)
    print('Luke 22 written.')

if __name__ == '__main__':
    main()
