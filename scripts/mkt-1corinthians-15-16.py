"""
MKT 1 Corinthians chapters 15–16 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1corinthians-15-16.py

Translation decisions:
- G386 ἀνάστασις: "resurrection" across all tiers — the central term of ch 15; no deviation
- G4102 πίστις (faith): "faith" (L/M); "faith/trust" (T) — consistent with Romans/Galatians decisions
- G4561 σάρξ (flesh): "flesh" (L always); "physical bodies" (M/T in 15:50 where the point is mortality,
    not fallen human nature); ch 15:39 keeps "flesh" throughout for biological sense
- G4151 πνεῦμα (Spirit/spirit): capitalized where the divine Spirit is the referent (15:45 "life-giving
    Spirit" = Christ as eschatological Adam, capitalized); 16:18 "spirit" lowercase (human spirit)
- G5590 ψυχή / G5591 ψυχικός: "natural" (L/M) for ψυχικός — the word means "of-the-soul/psyche"
    but "natural" is the established English rendering for this anthropological antithesis; T adds
    "the earthly-souled body" gloss to preserve the psychē register
- G2962 κύριος (Lord): "Lord" all tiers — no deviation; 15:47 "the Lord" in KJV is not in NA28/most
    MSS; rendered simply "from heaven" following better-attested text
- G166 αἰώνιος: not prominent in these chapters
- G1343 δικαιοσύνη: 15:34 "righteousness" (L); "what is right" (M); "doing right" (T)
- G26 ἀγάπη (love): "love" all tiers; 16:14 "let all things be done in love"; 16:24 closing "my love"
- G1577 ἐκκλησία (church): "church" (M/T); "assembly" only in L where formal structure is the point
- G3466 μυστήριον: "mystery" (L/M); "wonderful secret" (T) — following Paul's own rhetorical buildup
- G536 ἀπαρχή (firstfruits): "firstfruits" (L/M); "first of the great harvest" (T) — OT harvest echo
- G3952 παρουσία (coming): "coming" (L/M); "return" (T) — emphasises the eschatological event
- 15:5 "Cephas" kept (Aramaic form, early kerygmatic tradition); "Peter" in T for clarity
- 15:22 "all… all" — universal scope is the text; T qualifies by making the union ("in Adam/in Christ")
    do the limiting work, rather than adding glosses not in Paul
- 15:29 "baptized for the dead" — kept literally in L/M; T withholds interpretive resolution since the
    practice is historically uncertain; Paul's argument is a fortiori regardless of what the practice was
- 15:32 "fought with beasts at Ephesus" — likely metaphorical (opponents); T makes this explicit
- 15:45 "last Adam became a life-giving Spirit" — ζωοποιοῦν πνεῦμα; "Spirit" capitalized: the risen
    Christ in his pneumatic mode pours out the Spirit; this is Paul's Christological move
- 15:47 KJV "the Lord from heaven" — "the Lord" (κύριος) is not in the best MSS (P46, א, B, C, D);
    rendered "the second man is from heaven" following NA28
- 15:55 Quotes Hos 13:14 LXX with "O death" doubled (not "O grave"/"Hades") following NA28
- 16:1 "collection" (λογεία) — the Jerusalem relief fund; "offering" in T to capture the worshipful frame
- 16:2 "first day of the week" — Sunday gathering implied; "as he may prosper" = proportional giving
- 16:22 "Maranatha" — Aramaic אֲמַרַן אֲתָא / מָרַן אֲתָא, "Our Lord, come!"; kept transliterated in L/M
    with translation in T; the anathema formula is a covenantal curse, not mere condemnation
- 16:24 The scribal colophon ("The first epistle… written from Philippi") is not part of the original;
    it appears in some MSS but is excluded here as a later addition
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

CORINTHIANS1 = {
  "15": {
    "1": {
      "L": "Now I make known to you, brothers, the gospel which I proclaimed to you, which also you received, in which also you stand,",
      "M": "Now, brothers and sisters, I want to remind you of the gospel I preached to you, which you received and on which you have taken your stand.",
      "T": "Brothers and sisters, let me remind you of the Good News I preached to you. You welcomed it then, and you still stand on it today."
    },
    "2": {
      "L": "through which also you are being saved, if you hold fast the word I proclaimed to you—unless you believed in vain.",
      "M": "By this gospel you are saved, if you hold firmly to the word I preached to you. Otherwise, you have believed in vain.",
      "T": "It is this message that saves you—but only if you keep holding to it as I proclaimed it. Otherwise your faith has been for nothing."
    },
    "3": {
      "L": "For I delivered to you as of first importance what I also received: that Christ died for our sins according to the Scriptures,",
      "M": "For what I received I passed on to you as of first importance: that Christ died for our sins according to the Scriptures,",
      "T": "What I passed on to you was what had first been handed on to me—the very heart of the message: that Christ died for our sins, exactly as the Scriptures foretold."
    },
    "4": {
      "L": "and that he was buried, and that he was raised on the third day according to the Scriptures,",
      "M": "that he was buried, that he was raised on the third day according to the Scriptures,",
      "T": "He was buried, and then on the third day he rose from the dead, just as the Scriptures said he would."
    },
    "5": {
      "L": "and that he appeared to Cephas, then to the twelve.",
      "M": "and that he appeared to Cephas, and then to the Twelve.",
      "T": "After that he appeared to Peter and then to the rest of the twelve disciples."
    },
    "6": {
      "L": "After that he appeared to more than five hundred brothers at one time, most of whom are still alive, though some have fallen asleep.",
      "M": "After that, he appeared to more than five hundred of the brothers and sisters at the same time, most of whom are still living, though some have fallen asleep.",
      "T": "After that he appeared at one time to more than five hundred of his followers, most of whom are still alive—though some have since died."
    },
    "7": {
      "L": "Then he appeared to James, then to all the apostles.",
      "M": "Then he appeared to James, then to all the apostles.",
      "T": "Then he appeared to James and later to all the apostles."
    },
    "8": {
      "L": "Last of all, as to one untimely born, he appeared also to me.",
      "M": "and last of all he appeared to me also, as to one abnormally born.",
      "T": "Last of all, as though to someone born at the wrong time, he also appeared to me."
    },
    "9": {
      "L": "For I am the least of the apostles, unworthy to be called an apostle, because I persecuted the church of God.",
      "M": "For I am the least of the apostles and do not even deserve to be called an apostle, because I persecuted the church of God.",
      "T": "For I am the least deserving of all the apostles. I don't even deserve to be called an apostle, because I persecuted God's church."
    },
    "10": {
      "L": "But by the grace of God I am what I am, and his grace toward me was not in vain. On the contrary, I worked harder than any of them—though it was not I, but the grace of God that is with me.",
      "M": "But by the grace of God I am what I am, and his grace to me was not without effect. No, I worked harder than all of them—yet not I, but the grace of God that was with me.",
      "T": "Yet whatever I am now, it is all because God poured out his special favor on me—and not without result. I have worked harder than any of the other apostles; though it was not I, but God's grace working through me."
    },
    "11": {
      "L": "Whether then it was I or they, so we preach and so you believed.",
      "M": "Whether, then, it is I or they, this is what we preach, and this is what you believed.",
      "T": "So whether I preached to you or they did, the message is the same—and you believed it."
    },
    "12": {
      "L": "Now if Christ is proclaimed as raised from the dead, how can some of you say there is no resurrection of the dead?",
      "M": "But if it is preached that Christ has been raised from the dead, how can some of you say that there is no resurrection of the dead?",
      "T": "But tell me this—since we preach that Christ rose from the dead, why are some of you saying there will be no resurrection of the dead?"
    },
    "13": {
      "L": "But if there is no resurrection of the dead, then not even Christ has been raised.",
      "M": "If there is no resurrection of the dead, then not even Christ has been raised.",
      "T": "For if there is no resurrection of the dead, then Christ has not been raised either."
    },
    "14": {
      "L": "And if Christ has not been raised, then our preaching is empty and your faith is empty.",
      "M": "And if Christ has not been raised, our preaching is useless and so is your faith.",
      "T": "And if Christ has not been raised, then all our preaching is pointless, and your faith is pointless as well."
    },
    "15": {
      "L": "We are even found to be misrepresenting God, because we testified about God that he raised Christ, whom he did not raise if it is true that the dead are not raised.",
      "M": "More than that, we are then found to be false witnesses about God, for we have testified about God that he raised Christ from the dead. But he did not raise him if in fact the dead are not raised.",
      "T": "And we apostles would all be lying about God—for we have said that God raised Christ from the dead. That cannot be true if there is no resurrection of the dead."
    },
    "16": {
      "L": "For if the dead are not raised, not even Christ has been raised.",
      "M": "For if the dead are not raised, then Christ has not been raised either.",
      "T": "And if there is no resurrection of the dead, then Christ has not been raised."
    },
    "17": {
      "L": "And if Christ has not been raised, your faith is futile and you are still in your sins.",
      "M": "And if Christ has not been raised, your faith is futile; you are still in your sins.",
      "T": "And if Christ has not been raised, then your faith is useless and you are still guilty of your sins."
    },
    "18": {
      "L": "Then also those who have fallen asleep in Christ have perished.",
      "M": "Then those also who have fallen asleep in Christ are lost.",
      "T": "In that case, all who have died believing in Christ are utterly lost."
    },
    "19": {
      "L": "If in Christ we have hope in this life only, we are of all people most to be pitied.",
      "M": "If only for this life we have hope in Christ, we are of all people most to be pitied.",
      "T": "And if our hope in Christ is only for this life, we are more to be pitied than anyone in the world."
    },
    "20": {
      "L": "But in fact Christ has been raised from the dead, the firstfruits of those who have fallen asleep.",
      "M": "But Christ has indeed been raised from the dead, the firstfruits of those who have fallen asleep.",
      "T": "But in fact, Christ has been raised from the dead. He is the first of the great harvest of all who have died."
    },
    "21": {
      "L": "For as by a man came death, by a man has come also the resurrection of the dead.",
      "M": "For since death came through a man, the resurrection of the dead comes also through a man.",
      "T": "Just as death came into the world through a man, now the resurrection from the dead has begun through another man."
    },
    "22": {
      "L": "For as in Adam all die, so also in Christ shall all be made alive.",
      "M": "For as in Adam all die, so in Christ all will be made alive.",
      "T": "Just as everyone dies because we all belong to Adam, everyone who belongs to Christ will be given new life."
    },
    "23": {
      "L": "But each in his own order: Christ the firstfruits, then at his coming those who belong to Christ.",
      "M": "But each in turn: Christ, the firstfruits; then, when he comes, those who belong to him.",
      "T": "But this will happen in the right order: Christ was raised as the first of the harvest; then all who belong to Christ will be raised when he returns."
    },
    "24": {
      "L": "Then comes the end, when he delivers the kingdom to God the Father after destroying every rule and every authority and power.",
      "M": "Then the end will come, when he hands over the kingdom to God the Father after he has destroyed all dominion, authority and power.",
      "T": "After that the end will come, when he will turn the Kingdom over to God the Father, having destroyed every ruler and authority and power."
    },
    "25": {
      "L": "For he must reign until he has put all his enemies under his feet.",
      "M": "For he must reign until he has put all his enemies under his feet.",
      "T": "For Christ must reign until he humbles all his enemies beneath his feet."
    },
    "26": {
      "L": "The last enemy to be destroyed is death.",
      "M": "The last enemy to be destroyed is death.",
      "T": "And the last enemy to be destroyed is death itself."
    },
    "27": {
      "L": "For 'God has put all things in subjection under his feet.' But when it says 'all things are put in subjection,' it is plain that he is excepted who put all things in subjection under him.",
      "M": "For he 'has put everything under his feet.' Now when it says that 'everything' has been put under him, it is clear that this does not include God himself, who put everything under Christ.",
      "T": "The Scripture says, 'God has put all things under his authority.' Of course, when it says 'all things are under his authority,' that does not include God himself, who gave Christ his authority over all things."
    },
    "28": {
      "L": "When all things are subjected to him, then the Son himself will also be subjected to him who put all things in subjection under him, that God may be all in all.",
      "M": "When he has done this, then the Son himself will be made subject to him who put everything under him, so that God may be all in all.",
      "T": "Then, when all things are under his authority, the Son will put himself under God's authority, so that God, who gave his Son authority over all things, will be utterly supreme over everything everywhere."
    },
    "29": {
      "L": "Otherwise, what will those do who are baptized for the dead? If the dead are not raised at all, why then are they baptized for the dead?",
      "M": "Now if there is no resurrection, what will those do who are baptized for the dead? If the dead are not raised at all, why are people baptized for them?",
      "T": "If the dead will not be raised at all, what point is there in people being baptized on behalf of those who have died? Why do it at all?"
    },
    "30": {
      "L": "Why are we in danger every hour?",
      "M": "And as for us, why do we endanger ourselves every hour?",
      "T": "And why should we ourselves risk our lives hour by hour?"
    },
    "31": {
      "L": "I protest, brothers, by my pride in you, which I have in Christ Jesus our Lord, I die every day!",
      "M": "I face death every day—yes, just as surely as I boast about you in Christ Jesus our Lord.",
      "T": "For I swear, dear brothers and sisters, that I face death daily. This is as certain as my pride in what Christ Jesus our Lord has done in you."
    },
    "32": {
      "L": "What do I gain if, humanly speaking, I fought with beasts at Ephesus? If the dead are not raised, 'Let us eat and drink, for tomorrow we die.'",
      "M": "If I fought wild beasts in Ephesus with no more than human hopes, what have I gained? If the dead are not raised, 'Let us eat and drink, for tomorrow we die.'",
      "T": "And what value was there in fighting those ferocious opponents in Ephesus—if there will be no resurrection from the dead? If there is no resurrection, then as the Scripture says, 'Let's feast and drink, for tomorrow we die!'"
    },
    "33": {
      "L": "Do not be deceived: 'Bad company ruins good morals.'",
      "M": "Do not be misled: 'Bad company corrupts good character.'",
      "T": "Don't be fooled by those who say such things, for 'bad company corrupts good character.'"
    },
    "34": {
      "L": "Wake up from your stupor, as is right, and do not go on sinning. For some have no knowledge of God. I say this to your shame.",
      "M": "Come back to your senses as you ought, and stop sinning; for there are some who are ignorant of God—I say this to your shame.",
      "T": "Think clearly about what is right and stop sinning. For to your shame I say that some of you have no knowledge of God at all."
    },
    "35": {
      "L": "But someone will ask, 'How are the dead raised? With what kind of body do they come?'",
      "M": "But someone will ask, 'How are the dead raised? With what kind of body will they come?'",
      "T": "But someone may ask, 'How will the dead be raised? What kind of bodies will they have?'"
    },
    "36": {
      "L": "You fool! What you sow does not come to life unless it dies.",
      "M": "How foolish! What you sow does not come to life unless it dies.",
      "T": "What a foolish question! When you put a seed into the ground, it doesn't grow into a plant unless it dies first."
    },
    "37": {
      "L": "And what you sow is not the body that is to be, but a bare kernel, perhaps of wheat or of some other grain.",
      "M": "When you sow, you do not plant the body that will be, but just a seed, perhaps of wheat or of something else.",
      "T": "And what you put in the ground is not the plant that will grow, but only a bare seed of wheat or whatever you are planting."
    },
    "38": {
      "L": "But God gives it a body as he has chosen, and to each kind of seed its own body.",
      "M": "But God gives it a body as he has determined, and to each kind of seed he gives its own body.",
      "T": "Then God gives it the new body he wants it to have. A different plant grows from each kind of seed."
    },
    "39": {
      "L": "Not all flesh is the same flesh, but there is one kind for humans, another for animals, another for birds, and another for fish.",
      "M": "Not all flesh is the same: people have one kind of flesh, animals have another, birds another and fish another.",
      "T": "Similarly there are different kinds of flesh—one kind for humans, another for animals, another for birds, and another for fish."
    },
    "40": {
      "L": "There are heavenly bodies and earthly bodies, but the glory of the heavenly is of one kind, and the glory of the earthly is of another.",
      "M": "There are also heavenly bodies and there are earthly bodies; but the splendor of the heavenly bodies is one kind, and the splendor of the earthly bodies is another.",
      "T": "There are also bodies in the heavens and bodies on the earth. The glory of the heavenly bodies is different from the beauty of the earthly bodies."
    },
    "41": {
      "L": "There is one glory of the sun, and another glory of the moon, and another glory of the stars; for star differs from star in glory.",
      "M": "The sun has one kind of splendor, the moon another and the stars another; and star differs from star in splendor.",
      "T": "The sun has one kind of glory, while the moon shines with a different glory, and the stars shine with yet another. Even the stars differ from each other in their beauty and brilliance."
    },
    "42": {
      "L": "So is it with the resurrection of the dead. What is sown is perishable; what is raised is imperishable.",
      "M": "So will it be with the resurrection of the dead. The body that is sown is perishable, it is raised imperishable;",
      "T": "It is the same way with the resurrection of the dead. Our earthly bodies are planted in the ground when we die, but they will be raised to live forever."
    },
    "43": {
      "L": "It is sown in dishonor; it is raised in glory. It is sown in weakness; it is raised in power.",
      "M": "it is sown in dishonor, it is raised in glory; it is sown in weakness, it is raised in power;",
      "T": "Our bodies are buried in brokenness, but they will be raised in glory. They are buried in weakness, but they will be raised in strength."
    },
    "44": {
      "L": "It is sown a natural body; it is raised a spiritual body. If there is a natural body, there is also a spiritual body.",
      "M": "it is sown a natural body, it is raised a spiritual body. If there is a natural body, there is also a spiritual body.",
      "T": "They are buried as natural, earthly bodies, but they will be raised as spiritual bodies. For just as there are natural bodies, there are also spiritual bodies."
    },
    "45": {
      "L": "Thus it is written, 'The first man Adam became a living being'; the last Adam became a life-giving Spirit.",
      "M": "So it is written: 'The first man Adam became a living being'; the last Adam, a life-giving Spirit.",
      "T": "The Scriptures tell us, 'The first man, Adam, became a living person.' But the last Adam—that is, Christ—is a life-giving Spirit."
    },
    "46": {
      "L": "But it is not the spiritual that is first but the natural, and then the spiritual.",
      "M": "The spiritual did not come first, but the natural, and after that the spiritual.",
      "T": "What comes first is the natural body, then the spiritual body comes later."
    },
    "47": {
      "L": "The first man was from the earth, a man of dust; the second man is from heaven.",
      "M": "The first man was of the dust of the earth; the second man is of heaven.",
      "T": "Adam, the first man, was made from the dust of the earth, while Christ, the second man, came from heaven."
    },
    "48": {
      "L": "As was the man of dust, so also are those who are of the dust, and as is the man of heaven, so also are those who are of heaven.",
      "M": "As was the earthly man, so are those who are of the earth; and as is the heavenly man, so also are those who are of heaven.",
      "T": "Earthly people are like the earthly man, and heavenly people are like the heavenly man."
    },
    "49": {
      "L": "Just as we have borne the image of the man of dust, we shall also bear the image of the man of heaven.",
      "M": "And just as we have borne the image of the earthly man, so shall we bear the image of the heavenly man.",
      "T": "Just as we are now like the earthly man, we will someday be like the heavenly man."
    },
    "50": {
      "L": "I tell you this, brothers: flesh and blood cannot inherit the kingdom of God, nor does the perishable inherit the imperishable.",
      "M": "I declare to you, brothers and sisters, that flesh and blood cannot inherit the kingdom of God, nor does the perishable inherit the imperishable.",
      "T": "What I am saying, dear brothers and sisters, is that our physical bodies cannot inherit the Kingdom of God. These dying bodies cannot inherit what will last forever."
    },
    "51": {
      "L": "Behold! I tell you a mystery. We shall not all sleep, but we shall all be changed,",
      "M": "Listen, I tell you a mystery: We will not all sleep, but we will all be changed—",
      "T": "But let me reveal to you a wonderful secret. We will not all die, but we will all be transformed!"
    },
    "52": {
      "L": "in a moment, in the twinkling of an eye, at the last trumpet. For the trumpet will sound, and the dead will be raised imperishable, and we shall be changed.",
      "M": "in a flash, in the twinkling of an eye, at the last trumpet. For the trumpet will sound, the dead will be raised imperishable, and we will be changed.",
      "T": "It will happen in a moment, in the blink of an eye, when the last trumpet is blown. For when the trumpet sounds, those who have died will be raised to live forever, and we who are living will also be transformed."
    },
    "53": {
      "L": "For this perishable body must put on the imperishable, and this mortal body must put on immortality.",
      "M": "For the perishable must clothe itself with the imperishable, and the mortal with immortality.",
      "T": "For our dying bodies must be transformed into bodies that will never die; our mortal bodies must be transformed into immortal bodies."
    },
    "54": {
      "L": "When the perishable puts on the imperishable, and the mortal puts on immortality, then shall come to pass the saying that is written: 'Death is swallowed up in victory.'",
      "M": "When the perishable has been clothed with the imperishable, and the mortal with immortality, then the saying that is written will come true: 'Death has been swallowed up in victory.'",
      "T": "Then, when our dying bodies have been transformed into bodies that will never die, this Scripture will be fulfilled: 'Death is swallowed up in victory.'"
    },
    "55": {
      "L": "'O death, where is your victory? O death, where is your sting?'",
      "M": "'Where, O death, is your victory? Where, O death, is your sting?'",
      "T": "'O death, where is your victory? O death, where is your sting?'"
    },
    "56": {
      "L": "The sting of death is sin, and the power of sin is the law.",
      "M": "The sting of death is sin, and the power of sin is the law.",
      "T": "For sin is the sting that results in death, and the law gives sin its power."
    },
    "57": {
      "L": "But thanks be to God, who gives us the victory through our Lord Jesus Christ.",
      "M": "But thanks be to God! He gives us the victory through our Lord Jesus Christ.",
      "T": "But thank God! He gives us victory over sin and death through our Lord Jesus Christ."
    },
    "58": {
      "L": "Therefore, my beloved brothers, be steadfast, immovable, always abounding in the work of the Lord, knowing that in the Lord your labor is not in vain.",
      "M": "Therefore, my dear brothers and sisters, stand firm. Let nothing move you. Always give yourselves fully to the work of the Lord, because you know that your labor in the Lord is not in vain.",
      "T": "So, my dear brothers and sisters, be strong and immovable. Always work enthusiastically for the Lord, for you know that nothing you do for the Lord is ever useless."
    }
  },
  "16": {
    "1": {
      "L": "Now concerning the collection for the saints: as I directed the churches of Galatia, so you also are to do.",
      "M": "Now about the collection for the Lord's people: Do what I told the Galatian churches to do.",
      "T": "Now regarding the offering being collected for God's people in Jerusalem. You should follow the same procedure I gave to the churches in Galatia."
    },
    "2": {
      "L": "On the first day of every week, each of you is to put something aside and store it up, as he may prosper, so that there will be no collecting when I come.",
      "M": "On the first day of every week, each one of you should set aside a sum of money in keeping with your income, saving it up, so that when I come no collections will have to be made.",
      "T": "On the first day of each week, you should each put aside a portion of the money you have earned, saving it up. Don't wait until I arrive and then try to collect it all at once."
    },
    "3": {
      "L": "And when I arrive, I will send those whom you accredit by letter to carry your gift to Jerusalem.",
      "M": "Then, when I arrive, I will give letters of introduction to the men you approve and send them with your gift to Jerusalem.",
      "T": "When I come, I will write letters of recommendation for the messengers you choose to carry your gift to Jerusalem."
    },
    "4": {
      "L": "If it seems advisable that I should go also, they will accompany me.",
      "M": "If it seems advisable for me to go also, they will accompany me.",
      "T": "If it seems appropriate for me to go along, they can travel with me."
    },
    "5": {
      "L": "I will visit you after passing through Macedonia, for I intend to pass through Macedonia.",
      "M": "After I go through Macedonia, I will come to you—for I will be going through Macedonia.",
      "T": "I am coming to visit you after I have been to Macedonia, for I am planning to travel through Macedonia first."
    },
    "6": {
      "L": "and perhaps I will stay with you or even spend the winter, so that you may help me on my journey, wherever I go.",
      "M": "Perhaps I will stay with you for a while, or even spend the winter, so that you can help me on my journey, wherever I go.",
      "T": "I may stay there the rest of the winter so you can send me on my way to wherever I go next."
    },
    "7": {
      "L": "For I do not want to see you now just in passing. I hope to spend some time with you, if the Lord permits.",
      "M": "For I do not want to see you now and make only a passing visit; I hope to spend some time with you, if the Lord permits.",
      "T": "I don't want to stop by for just a short visit on my way through. I want to come and stay awhile, if the Lord will let me."
    },
    "8": {
      "L": "But I will stay in Ephesus until Pentecost,",
      "M": "But I will stay on at Ephesus until Pentecost,",
      "T": "In the meantime, I will be staying here at Ephesus until the Festival of Pentecost."
    },
    "9": {
      "L": "for a wide and effective door has been opened to me, and there are many adversaries.",
      "M": "because a great door for effective work has opened to me, and there are many who oppose me.",
      "T": "There is a wide-open door here for a great work, even though many oppose me."
    },
    "10": {
      "L": "When Timothy comes, see that you put him at ease among you, for he is doing the work of the Lord, as I am.",
      "M": "When Timothy comes, see to it that he has nothing to fear while he is with you, for he is carrying on the work of the Lord, just as I am.",
      "T": "If Timothy comes, make him feel welcome and at ease, for he is doing the Lord's work, just as I am."
    },
    "11": {
      "L": "So let no one despise him. Help him on his way in peace, that he may return to me, for I am expecting him with the brothers.",
      "M": "No one, then, should treat him with contempt. Send him on his way in peace so that he may return to me. I am expecting him along with the brothers.",
      "T": "Don't let anyone treat him with contempt. Send him on his way with your blessing when he returns to me. I am looking forward to seeing him soon, along with the other believers."
    },
    "12": {
      "L": "Now concerning our brother Apollos, I strongly urged him to visit you with the other brothers, but it was not at all his will to come now. He will come when he has opportunity.",
      "M": "Now about our brother Apollos: I strongly urged him to go to you with the brothers. He was quite unwilling to go now, but he will go when he has the opportunity.",
      "T": "Now about our brother Apollos—I urged him strongly to visit you with the other believers, but he was not willing to come right now. He will see you later when he has the opportunity."
    },
    "13": {
      "L": "Be watchful, stand firm in the faith, act like men, be strong.",
      "M": "Be on your guard; stand firm in the faith; be courageous; be strong.",
      "T": "Be on guard. Stand firm in the faith. Be courageous. Be strong."
    },
    "14": {
      "L": "Let all that you do be done in love.",
      "M": "Do everything in love.",
      "T": "And do everything with love."
    },
    "15": {
      "L": "Now I urge you, brothers—you know that the household of Stephanas were the first converts in Achaia, and that they have devoted themselves to the service of the saints—",
      "M": "You know that the household of Stephanas were the first converts in Achaia, and they have devoted themselves to the service of the Lord's people. I urge you, brothers and sisters,",
      "T": "You know that Stephanas and his household were the first of the believers in Greece, and they have devoted themselves to serving God's people. Dear brothers and sisters, I urge you"
    },
    "16": {
      "L": "to be subject to such as these, and to every fellow worker and laborer.",
      "M": "to submit to such people and to everyone who joins in the work and labors at it.",
      "T": "to honor the leadership of everyone like them, and of all who work and labor alongside them."
    },
    "17": {
      "L": "I rejoice at the coming of Stephanas and Fortunatus and Achaicus, because they have made up for your absence,",
      "M": "I was glad when Stephanas, Fortunatus and Achaicus arrived, because they have supplied what was lacking from you.",
      "T": "I am very glad that Stephanas, Fortunatus, and Achaicus have come here. They have been making up for the support you were not able to give me."
    },
    "18": {
      "L": "for they refreshed my spirit as well as yours. Give recognition to such people.",
      "M": "For they refreshed my spirit and yours also. Such men deserve recognition.",
      "T": "They have been a wonderful encouragement to me, as they have been to you. You must show your appreciation to all who serve like this."
    },
    "19": {
      "L": "The churches of Asia send you greetings. Aquila and Prisca, together with the church in their house, send you hearty greetings in the Lord.",
      "M": "The churches in the province of Asia send you greetings. Aquila and Priscilla greet you warmly in the Lord, and so does the church that meets at their house.",
      "T": "The churches here in the province of Asia send greetings in the Lord, as do our brother and sister Aquila and Prisca, along with the church that meets in their home."
    },
    "20": {
      "L": "All the brothers send you greetings. Greet one another with a holy kiss.",
      "M": "All the brothers and sisters here send you greetings. Greet one another with a holy kiss.",
      "T": "All the brothers and sisters here send their greetings. Greet each other with a holy kiss."
    },
    "21": {
      "L": "I, Paul, write this greeting with my own hand.",
      "M": "I, Paul, write this greeting in my own hand.",
      "T": "Here is my greeting in my own handwriting—Paul."
    },
    "22": {
      "L": "If anyone has no love for the Lord, let him be accursed. Maranatha!",
      "M": "If anyone does not love the Lord, let that person be cursed! Come, Lord!",
      "T": "If anyone does not love the Lord, a curse be on them. Our Lord, come!"
    },
    "23": {
      "L": "The grace of the Lord Jesus be with you.",
      "M": "The grace of the Lord Jesus be with you.",
      "T": "May the grace of the Lord Jesus be with you."
    },
    "24": {
      "L": "My love be with you all in Christ Jesus. Amen.",
      "M": "My love to all of you in Christ Jesus. Amen.",
      "T": "My love to all of you in Christ Jesus."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1corinthians')
        merge_tier(existing, CORINTHIANS1, tier_key)
        save(tier_dir, '1corinthians', existing)
    print('1 Corinthians 15–16 written.')

if __name__ == '__main__':
    main()
