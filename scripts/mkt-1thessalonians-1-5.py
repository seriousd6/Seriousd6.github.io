"""
MKT 1 Thessalonians chapters 1–5 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1thessalonians-1-5.py

Translation decisions:
- G80 (ἀδελφοί): L: "brothers"; M/T: "brothers and sisters" — Paul addresses mixed congregations
- G3952 (παρουσία): "coming" throughout — technical term for the Second Advent; not "return"
  or "appearance"; L/M/T all use "coming" since it is Paul's own established vocabulary here
- G38 (ἁγιασμός): L: "sanctification"; M: "sanctification"; T: "holy living" (5:23) or
  "holiness" — the process and state of being set apart, not merely positional
- G3709 (ὀργή): "wrath" throughout — divine judicial anger; not softened to "anger"
- G4991 (σωτηρία): "salvation" throughout all tiers
- G4982 (σῴζω): "save/saved" throughout
- G2837 (κοιμάω): L/M: "fallen asleep" — Paul's euphemism for Christian death preserves the
  resurrection hope embedded in the metaphor; T: "who have died" explicates in 4:13 but
  the "sleep" language is retained in 4:14-15 for theological weight
- G1323 (παρουσία) vs G666 (ἀπουσία): distinguished carefully in context
- G2250 + G2962 (ἡμέρα κυρίου): "day of the Lord" — OT prophetic phrase; not altered
- G2812 (κλέπτης): "thief" — the "thief in the night" image preserved literally
- G26 (ἀγάπη): "love" throughout
- G4102 (πίστις): "faith" throughout
- G1680 (ἐλπίς): "hope" throughout
- Greeting formula (1:1): "grace and peace" — standard Pauline greeting preserved
- G2316 (θεός) + G3962 (πατήρ): "God the Father" — capitalized compound title
- G4151 ἅγιον: "Holy Spirit" throughout
- G1577 (ἐκκλησία): "church" throughout
- G18 (ἀγαθός) vs G2570 (καλός): both "good" unless context demands distinction
- "we" vs "I": Paul uses first person plural throughout; reflect plurality in translation
- G2588 (καρδία): "heart" throughout
- G5590 (ψυχή): "soul" / "life" — context sensitive; 5:23 "soul" in tripartite formula
- G4983 (σῶμα): "body" throughout
- G4151 (πνεῦμα): "spirit" (human) / "Spirit" (Holy Spirit) — capitalization key
- Tripartite formula (5:23): "spirit, soul, and body" — preserve the three-part structure in all tiers
- G3956 (πᾶς): "every/all" as context requires
- Eschatological passage (4:13-18): The Rapture passage — careful to render sequence clearly:
  those who have died first, then those who are alive; "meet" (G529 ἀπάντησις) = formal
  civic welcome procession; L: "meeting"; M: "meet"; T: "welcome"
- G4246 (πρεσβύτης): "elder" in pastoral context
- G2588 (καρδία) + G4151 (πνεῦμα): not confused
- G96 (ἀδόκιμος): "disqualified" / "failed the test"
- "blameless" (G273 ἄμεμπτος): important in 3:13 and 5:23; "blameless" throughout
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

THESSALONIANS_1 = {
 "1": {
  "1": {
   "L": "Paul and Silvanus and Timothy, to the church of the Thessalonians in God the Father and the Lord Jesus Christ: Grace to you and peace.",
   "M": "Paul, Silas and Timothy, to the church of the Thessalonians in God the Father and the Lord Jesus Christ: Grace and peace to you.",
   "T": "From Paul, Silas, and Timothy. To the church of the Thessalonians—a community rooted in God our Father and the Lord Jesus Christ. Grace and peace to you."
  },
  "2": {
   "L": "We give thanks to God always for all of you, making mention of you in our prayers,",
   "M": "We always thank God for all of you and continually mention you in our prayers.",
   "T": "We thank God for all of you continually, and we keep bringing you before him in our prayers."
  },
  "3": {
   "L": "remembering without ceasing your work of faith and labor of love and endurance of hope in our Lord Jesus Christ, before our God and Father,",
   "M": "We remember before our God and Father your work produced by faith, your labour motivated by love, and your endurance inspired by hope in our Lord Jesus Christ.",
   "T": "Before our God and Father, we constantly recall the work your faith produces, the effort your love drives, and the endurance that comes from your hope in our Lord Jesus Christ."
  },
  "4": {
   "L": "knowing, brothers beloved by God, your election,",
   "M": "For we know, brothers and sisters loved by God, that he has chosen you,",
   "T": "Brothers and sisters, we know that God loves you and has chosen you—"
  },
  "5": {
   "L": "because our gospel came to you not in word only, but also in power and in the Holy Spirit and in much assurance, even as you know what manner of men we showed ourselves to be among you for your sake.",
   "M": "because our gospel came to you not simply with words but also with power, with the Holy Spirit and deep conviction. You know how we lived among you for your sake.",
   "T": "because our message came to you not just as words, but with real power—the Holy Spirit brought deep conviction with it. You saw how we lived among you, and it was all for your benefit."
  },
  "6": {
   "L": "And you became imitators of us and of the Lord, having received the word in much affliction with joy of the Holy Spirit,",
   "M": "You became imitators of us and of the Lord, for you welcomed the message in the midst of severe suffering with the joy given by the Holy Spirit.",
   "T": "You followed our example—and the Lord's—by receiving the word in the middle of great suffering, yet with the joy the Holy Spirit gives."
  },
  "7": {
   "L": "so that you became an example to all the believers in Macedonia and in Achaia.",
   "M": "And so you became a model to all the believers in Macedonia and Achaia.",
   "T": "As a result, you became a model for all the believers throughout Macedonia and Achaia."
  },
  "8": {
   "L": "For from you the word of the Lord has sounded out, not only in Macedonia and Achaia, but in every place your faith toward God has gone out, so that we have no need to say anything.",
   "M": "The Lord's message rang out from you not only in Macedonia and Achaia—your faith in God has become known everywhere. Therefore we do not need to say anything about it;",
   "T": "The Lord's message has echoed out from you—not just across Macedonia and Achaia, but everywhere. People are talking about your faith in God. We don't even need to mention it,"
  },
  "9": {
   "L": "for they themselves report concerning us what sort of entrance we had toward you, and how you turned to God from idols to serve the living and true God,",
   "M": "for they themselves report what kind of reception you gave us. They tell how you turned to God from idols to serve the living and true God,",
   "T": "because people everywhere are telling the story themselves—how you welcomed us, and how you turned away from idols to serve the living and true God."
  },
  "10": {
   "L": "and to wait for his Son from heaven, whom he raised from the dead—Jesus, who delivers us from the coming wrath.",
   "M": "and to wait for his Son from heaven, whom he raised from the dead—Jesus, who rescues us from the coming wrath.",
   "T": "And you are waiting for his Son to come from heaven—Jesus, whom God raised from the dead, who rescues us from the wrath that is coming."
  }
 },
 "2": {
  "1": {
   "L": "For you yourselves know, brothers, that our entry to you has not proved empty,",
   "M": "You know, brothers and sisters, that our visit to you was not without results.",
   "T": "You know this yourselves, brothers and sisters—our visit to you was not a failure."
  },
  "2": {
   "L": "but having suffered before and been treated shamefully, as you know, in Philippi, we were bold in our God to speak to you the gospel of God in much conflict.",
   "M": "We had previously suffered and been treated outrageously in Philippi, as you know, but with the help of our God we dared to tell you his gospel in the face of strong opposition.",
   "T": "We had just been beaten and humiliated in Philippi—as you know—but our God gave us courage to tell you his good news despite fierce resistance."
  },
  "3": {
   "L": "For our exhortation is not from error nor from impure motive, nor in deceit,",
   "M": "For the appeal we make does not spring from error or impure motives, nor are we trying to trick you.",
   "T": "The message we bring to you doesn't come from delusion, selfish ambition, or any attempt to deceive you."
  },
  "4": {
   "L": "but just as we have been approved by God to be entrusted with the gospel, so we speak, not as pleasing men but God, who tests our hearts.",
   "M": "On the contrary, we speak as those approved by God to be entrusted with the gospel. We are not trying to please people but God, who tests our hearts.",
   "T": "We have been approved by God and entrusted with the good news—so we speak not to win human approval but to please God, who examines every heart."
  },
  "5": {
   "L": "For we were never seen using flattering speech, as you know, nor with a pretext for greed—God is witness—",
   "M": "You know we never used flattery, nor did we put on a mask to cover up greed—God is our witness.",
   "T": "You know we never used flattery—and we never hid behind smooth words to cover our greed. God is our witness."
  },
  "6": {
   "L": "nor seeking glory from men, neither from you nor from others, when we might have been a burden as apostles of Christ.",
   "M": "We were not looking for praise from people, not from you or anyone else, even though as apostles of Christ we could have asserted our authority.",
   "T": "We were not looking for praise from anyone—not from you, not from anyone else—even though as apostles of Christ we had the right to make demands of you."
  },
  "7": {
   "L": "But we were gentle among you, like a nursing mother caring for her own children.",
   "M": "Instead, we were like young children among you. Just as a nursing mother cares for her little children,",
   "T": "Instead, we were gentle with you—like a nursing mother tenderly caring for her own babies."
  },
  "8": {
   "L": "Being thus affectionately desirous of you, we were pleased to share with you not only the gospel of God but also our own lives, because you have become very dear to us.",
   "M": "so we cared for you. Because we loved you so much, we were delighted to share with you not only the gospel of God but our lives as well.",
   "T": "We came to love you so much that we were glad to share not only God's good news with you but our very lives. You had become that precious to us."
  },
  "9": {
   "L": "For you remember, brothers, our labor and hardship; working night and day so as not to put a burden on any of you, we proclaimed to you the gospel of God.",
   "M": "Surely you remember, brothers and sisters, our toil and hardship; we worked night and day in order not to be a burden to anyone while we preached the gospel of God to you.",
   "T": "Brothers and sisters, you remember our hard work—laboring night and day so that we would not be a financial burden to any of you while we proclaimed God's good news."
  },
  "10": {
   "L": "You are witnesses, and God also, how devoutly and righteously and blamelessly we conducted ourselves toward you who believe.",
   "M": "You are witnesses, and so is God, of how holy, righteous and blameless we were among you who believed.",
   "T": "You are witnesses—and so is God—of how holy, righteous, and blameless our conduct was toward you who believed."
  },
  "11": {
   "L": "Just as you know how, like a father with his own children, we were exhorting each one of you and encouraging and charging you",
   "M": "For you know that we dealt with each of you as a father deals with his own children,",
   "T": "You know that we treated each of you the way a father treats his own children—"
  },
  "12": {
   "L": "to walk in a manner worthy of God, who calls you into his own kingdom and glory.",
   "M": "encouraging, comforting and urging you to live lives worthy of God, who calls you into his kingdom and glory.",
   "T": "encouraging, comforting, and urging you to live lives that honor God, who calls you into his kingdom and glory."
  },
  "13": {
   "L": "And for this reason we also thank God without ceasing, because when you received the word of God which you heard from us, you received it not as a word of men but as it truly is, the word of God, which also works effectively in you who believe.",
   "M": "And we also thank God continually because, when you received the word of God, which you heard from us, you accepted it not as a human word, but as it actually is, the word of God, which is indeed at work in you who believe.",
   "T": "We thank God constantly for this: when you heard the message from us, you didn't receive it as a merely human word—you accepted it as what it truly is, the word of God. And it is actively working in you who believe."
  },
  "14": {
   "L": "For you, brothers, became imitators of the churches of God in Christ Jesus that are in Judea, because you also suffered the same things from your own fellow citizens as they indeed from the Jews,",
   "M": "For you, brothers and sisters, became imitators of God's churches in Judea, which are in Christ Jesus: you suffered from your own people the same things those churches suffered from the Jews",
   "T": "Brothers and sisters, you followed the example of the churches of God in Judea that are in Christ Jesus—because you suffered the same things from your own countrymen that those churches suffered from the Jewish people."
  },
  "15": {
   "L": "who also killed the Lord Jesus and the prophets, and drove us out, and are not pleasing to God, and are hostile to all men,",
   "M": "who killed the Lord Jesus and the prophets and also drove us out. They displease God and are hostile to everyone",
   "T": "Those who killed the Lord Jesus and the prophets, who drove us out—they displease God and stand against all humanity."
  },
  "16": {
   "L": "forbidding us to speak to the Gentiles so that they may be saved, so as to fill up their sins always. But the wrath has come upon them to the end.",
   "M": "in their effort to keep us from speaking to the Gentiles so that they may be saved. In this way they always heap up their sins to the limit. The wrath of God has come upon them at last.",
   "T": "In their effort to stop us from speaking to the Gentiles the good news of salvation, they keep heaping up their sins. But God's wrath has caught up with them at last."
  },
  "17": {
   "L": "But we, brothers, being torn away from you for a short time—in person, not in heart—were all the more eager with great desire to see your face.",
   "M": "But, brothers and sisters, when we were orphaned by being separated from you for a short time (in person, not in thought), out of our intense longing we made every effort to see you.",
   "T": "Brothers and sisters, when we were suddenly torn away from you—in body, not in heart—we felt like orphans separated from their family. Our longing to see you again was overwhelming."
  },
  "18": {
   "L": "Because we wanted to come to you—I, Paul, once and again—but Satan hindered us.",
   "M": "For we wanted to come to you—certainly I, Paul, did, again and again—but Satan blocked our way.",
   "T": "We wanted to come to you—I, Paul, tried more than once—but Satan stopped us."
  },
  "19": {
   "L": "For what is our hope or joy or crown of boasting? Is it not even you, before our Lord Jesus at his coming?",
   "M": "For what is our hope, our joy, or the crown in which we will glory in the presence of our Lord Jesus when he comes? Is it not you?",
   "T": "After all, what is our hope, our joy, the crown we will boast about when we stand before our Lord Jesus at his coming? It's you."
  },
  "20": {
   "L": "For you are our glory and our joy.",
   "M": "Indeed, you are our glory and joy.",
   "T": "You are our glory and our joy."
  }
 },
 "3": {
  "1": {
   "L": "Therefore, when we could bear it no longer, we thought it good to be left behind in Athens alone,",
   "M": "So when we could stand it no longer, we thought it best to be left by ourselves in Athens.",
   "T": "When we could stand the separation no longer, we decided to stay in Athens by ourselves"
  },
  "2": {
   "L": "and we sent Timothy, our brother and co-worker of God in the gospel of Christ, to establish you and encourage you on behalf of your faith,",
   "M": "We sent Timothy, who is our brother and co-worker in God's service in spreading the gospel of Christ, to strengthen and encourage you in your faith,",
   "T": "and send Timothy to you. He is our brother, a fellow worker in God's service for the gospel of Christ. We sent him to strengthen you and encourage your faith,"
  },
  "3": {
   "L": "so that no one would be shaken in these afflictions. For you yourselves know that we are appointed to this.",
   "M": "so that no one would be unsettled by these trials. For you know quite well that we are destined for them.",
   "T": "so that none of you would be shaken by these trials. You know perfectly well that this is our calling—"
  },
  "4": {
   "L": "For indeed, when we were with you, we were telling you beforehand that we were about to suffer affliction, just as it also happened, as you know.",
   "M": "In fact, when we were with you, we kept telling you that we would be persecuted. And it turned out that way, as you well know.",
   "T": "Even while we were still with you, we told you we would face persecution. And that is exactly what happened, as you well know."
  },
  "5": {
   "L": "For this reason, when I also could no longer bear it, I sent to know your faith, lest perhaps the tempter had tempted you and our labor had proved vain.",
   "M": "For this reason, when I could stand it no longer, I sent to find out about your faith. I was afraid that in some way the tempter had tempted you and that our efforts might have been useless.",
   "T": "That's why, when I couldn't stand the uncertainty any longer, I sent Timothy to find out how your faith was holding up. I was afraid the tempter might have gotten to you and made our work worthless."
  },
  "6": {
   "L": "But now Timothy has come to us from you and brought us the good news of your faith and love, and that you always have fond remembrance of us, longing to see us, even as we also long to see you—",
   "M": "But Timothy has just now come to us from you and has brought good news about your faith and love. He has told us that you always have pleasant memories of us and that you long to see us, just as we also long to see you.",
   "T": "But now Timothy has just returned to us from you, and he brought wonderful news about your faith and love. He tells us that you have fond memories of us and that you long to see us as much as we long to see you."
  },
  "7": {
   "L": "for this reason, brothers, in all our distress and affliction we were encouraged about you through your faith.",
   "M": "Therefore, brothers and sisters, in all our distress and persecution we were encouraged about you because of your faith.",
   "T": "So in the middle of all our distress and hardship, brothers and sisters, your faith encouraged us."
  },
  "8": {
   "L": "Because now we live, if you are standing firm in the Lord.",
   "M": "For now we really live, since you are standing firm in the Lord.",
   "T": "We really feel alive now—as long as you are standing firm in the Lord."
  },
  "9": {
   "L": "For what thanksgiving can we render back to God for you, for all the joy with which we rejoice because of you before our God,",
   "M": "How can we thank God enough for you in return for all the joy we have in the presence of our God because of you?",
   "T": "How can we ever thank God enough for you? The joy you bring us before our God—we can barely put it into words."
  },
  "10": {
   "L": "night and day praying earnestly to see your face and to complete what is lacking in your faith?",
   "M": "Night and day we pray most earnestly that we may see you again and supply what is lacking in your faith.",
   "T": "Day and night we pray with all our heart to see you again and to fill in whatever is still lacking in your faith."
  },
  "11": {
   "L": "Now may our God and Father himself, and our Lord Jesus, direct our way to you.",
   "M": "Now may our God and Father himself and our Lord Jesus clear the way for us to come to you.",
   "T": "May our God and Father himself, and our Lord Jesus, open the way for us to come to you."
  },
  "12": {
   "L": "And may the Lord cause you to increase and overflow in love for one another and for all, just as we also for you,",
   "M": "May the Lord make your love increase and overflow for each other and for everyone else, just as ours does for you.",
   "T": "And may the Lord make your love for one another—and for all people—grow and overflow, just as our love for you does."
  },
  "13": {
   "L": "so as to establish your hearts blameless in holiness before our God and Father, at the coming of our Lord Jesus with all his holy ones.",
   "M": "May he strengthen your hearts so that you will be blameless and holy in the presence of our God and Father when our Lord Jesus comes with all his holy ones.",
   "T": "May he strengthen your hearts so that you will stand blameless and holy before our God and Father when our Lord Jesus comes with all his holy people."
  }
 },
 "4": {
  "1": {
   "L": "Finally therefore, brothers, we ask and urge you in the Lord Jesus, that just as you received from us how you ought to walk and to please God, just as you are walking, that you abound still more.",
   "M": "As for other matters, brothers and sisters, we instructed you how to live in order to please God, as in fact you are living. Now we ask you and urge you in the Lord Jesus to do this more and more.",
   "T": "Finally, brothers and sisters, we taught you how to live in a way that pleases God—and that is how you are living. Now we urge you in the Lord Jesus to keep doing this more and more."
  },
  "2": {
   "L": "For you know what instructions we gave you through the Lord Jesus.",
   "M": "For you know what instructions we gave you by the authority of the Lord Jesus.",
   "T": "You know the instructions we gave you by the authority of the Lord Jesus."
  },
  "3": {
   "L": "For this is the will of God: your sanctification—that you abstain from sexual immorality,",
   "M": "It is God's will that you should be sanctified: that you should avoid sexual immorality;",
   "T": "God's will for you is your sanctification—that you stay away from sexual immorality;"
  },
  "4": {
   "L": "that each of you know how to possess his own vessel in sanctification and honor,",
   "M": "that each of you should learn to control your own body in a way that is holy and honourable,",
   "T": "that each of you should learn to control your own body in a way that is holy and honoring to God,"
  },
  "5": {
   "L": "not in the passion of lust like the Gentiles who do not know God;",
   "M": "not in passionate lust like the pagans, who do not know God;",
   "T": "not driven by lustful passion like people who don't know God."
  },
  "6": {
   "L": "that no one transgress and defraud his brother in this matter, because the Lord is an avenger regarding all these things, as we also told you beforehand and testified.",
   "M": "and that in this matter no one should wrong or take advantage of a brother or sister. The Lord will punish all those who commit such sins, as we told you and warned you before.",
   "T": "No one should wrong a brother or sister or take advantage of them in this area. The Lord punishes all who do such things—we told you this before and warned you about it."
  },
  "7": {
   "L": "For God did not call us to impurity but in sanctification.",
   "M": "For God did not call us to be impure, but to live a holy life.",
   "T": "God didn't call us to an impure life—he called us to a holy one."
  },
  "8": {
   "L": "Therefore the one who rejects this rejects not man but God, who gives his Holy Spirit into you.",
   "M": "Therefore, anyone who rejects this instruction does not reject a human being but God, the very God who gives you his Holy Spirit.",
   "T": "So anyone who disregards this instruction isn't rejecting a human rule—they are rejecting God himself, who gives you his very own Holy Spirit."
  },
  "9": {
   "L": "Now concerning brotherly love, you have no need for us to write to you, for you yourselves are taught by God to love one another,",
   "M": "Now about your love for one another we do not need to write to you, for you yourselves have been taught by God to love each other.",
   "T": "Now, about loving your fellow believers: you don't need us to write to you about this, because God himself has taught you to love one another."
  },
  "10": {
   "L": "and indeed you are doing it toward all the brothers in all Macedonia. But we urge you, brothers, to abound still more,",
   "M": "And in fact, you do love all of God's family throughout Macedonia. Yet we urge you, brothers and sisters, to do so more and more,",
   "T": "And that's exactly what you are doing—loving all the believers throughout Macedonia. We urge you, brothers and sisters, to keep doing this more and more."
  },
  "11": {
   "L": "and to aspire to live quietly, and to attend to your own affairs, and to work with your own hands, as we instructed you,",
   "M": "and to make it your ambition to lead a quiet life: you should mind your own business and work with your hands, just as we told you,",
   "T": "Make it your aim to live a quiet life, take care of your own affairs, and work with your own hands—as we directed you."
  },
  "12": {
   "L": "so that you may walk properly toward outsiders and have need of nothing.",
   "M": "so that your daily life may win the respect of outsiders and so that you will not be dependent on anybody.",
   "T": "This way your life will earn the respect of those outside the faith, and you will not be dependent on anyone."
  },
  "13": {
   "L": "But we do not want you to be ignorant, brothers, concerning those who have fallen asleep, so that you do not grieve as even the rest who have no hope.",
   "M": "Brothers and sisters, we do not want you to be uninformed about those who sleep in death, so that you do not grieve like the rest of mankind, who have no hope.",
   "T": "Brothers and sisters, we don't want you to be in the dark about those who have died. We don't want you to grieve the way people grieve who have no hope."
  },
  "14": {
   "L": "For if we believe that Jesus died and rose again, even so God will bring with him those who have fallen asleep through Jesus.",
   "M": "For we believe that Jesus died and rose again, and so we believe that God will bring with Jesus those who have fallen asleep in him.",
   "T": "Because we believe that Jesus died and rose again, we also believe that God will bring with Jesus all who have fallen asleep in him."
  },
  "15": {
   "L": "For this we say to you by the word of the Lord, that we who are alive and remaining until the coming of the Lord will not precede those who have fallen asleep.",
   "M": "According to the Lord's word, we tell you that we who are still alive, who are left until the coming of the Lord, will certainly not precede those who have fallen asleep.",
   "T": "Here is what we tell you by the word of the Lord: We who are still alive at the coming of the Lord will not go ahead of those who have already died."
  },
  "16": {
   "L": "For the Lord himself will descend from heaven with a shout of command, with the voice of an archangel, and with the trumpet of God, and the dead in Christ will rise first.",
   "M": "For the Lord himself will come down from heaven, with a loud command, with the voice of the archangel and with the trumpet call of God, and the dead in Christ will rise first.",
   "T": "The Lord himself will come down from heaven with a commanding shout—with the voice of the archangel and the blast of God's trumpet. And those who have died in Christ will rise first."
  },
  "17": {
   "L": "Then we who are alive and remaining will be caught up together with them in the clouds to meet the Lord in the air, and so we will always be with the Lord.",
   "M": "After that, we who are still alive and are left will be caught up together with them in the clouds to meet the Lord in the air. And so we will be with the Lord for ever.",
   "T": "Then we who are still alive will be swept up together with them in the clouds to welcome the Lord in the air. And we will be with the Lord forever."
  },
  "18": {
   "L": "Therefore comfort one another with these words.",
   "M": "Therefore encourage one another with these words.",
   "T": "So use these words to encourage one another."
  }
 },
 "5": {
  "1": {
   "L": "Now concerning the times and the seasons, brothers, you have no need for anything to be written to you.",
   "M": "Now, brothers and sisters, about times and dates we do not need to write to you,",
   "T": "Brothers and sisters, you don't need us to write to you about the timing and circumstances—"
  },
  "2": {
   "L": "For you yourselves know accurately that the day of the Lord will come like a thief in the night.",
   "M": "for you know very well that the day of the Lord will come like a thief in the night.",
   "T": "you already know very well that the day of the Lord will arrive without warning, like a thief in the night."
  },
  "3": {
   "L": "When people are saying, Peace and security, then sudden destruction will come upon them like birth pains on a pregnant woman, and they will not escape.",
   "M": "While people are saying, Peace and safety, destruction will come on them suddenly, as labour pains on a pregnant woman, and they will not escape.",
   "T": "While people are saying everything is safe and secure, sudden destruction will fall on them—as suddenly as labor pains on a pregnant woman. There will be no escaping it."
  },
  "4": {
   "L": "But you, brothers, are not in darkness, so that the day should catch you like a thief.",
   "M": "But you, brothers and sisters, are not in darkness so that this day should surprise you like a thief.",
   "T": "But you, brothers and sisters, are not living in darkness—this day will not catch you off guard like a thief."
  },
  "5": {
   "L": "For you are all sons of light and sons of day. We are not of night nor of darkness.",
   "M": "You are all children of the light and children of the day. We do not belong to the night or to the darkness.",
   "T": "You are all children of the light and of the day—not of the night or the darkness."
  },
  "6": {
   "L": "So then let us not sleep as the rest do, but let us be awake and sober.",
   "M": "So then, let us not be like others, who are asleep, but let us be awake and sober.",
   "T": "So let's not sleep like the others do—let's be wide awake and clear-headed."
  },
  "7": {
   "L": "For those who sleep sleep at night, and those who are drunk get drunk at night.",
   "M": "For those who sleep, sleep at night, and those who get drunk, get drunk at night.",
   "T": "Sleeping and getting drunk happen at night."
  },
  "8": {
   "L": "But we, being of the day, let us be sober, putting on the breastplate of faith and love, and as a helmet the hope of salvation.",
   "M": "But since we belong to the day, let us be sober, putting on faith and love as a breastplate, and the hope of salvation as a helmet.",
   "T": "But since we belong to the day, let's be clear-headed. Let's put on faith and love as our armor—a breastplate—and make the hope of salvation our helmet."
  },
  "9": {
   "L": "Because God did not appoint us to wrath but to obtain salvation through our Lord Jesus Christ,",
   "M": "For God did not appoint us to suffer wrath but to receive salvation through our Lord Jesus Christ.",
   "T": "God did not destine us for wrath—he destined us to receive salvation through our Lord Jesus Christ."
  },
  "10": {
   "L": "who died for us so that whether we are awake or asleep, we may live together with him.",
   "M": "He died for us so that, whether we are awake or asleep, we may live together with him.",
   "T": "He died for us so that whether we are alive or have already died, we will live together with him."
  },
  "11": {
   "L": "Therefore encourage one another and build up one another, just as you also are doing.",
   "M": "Therefore encourage one another and build each other up, just as in fact you are doing.",
   "T": "So keep encouraging one another and building each other up—as you are already doing."
  },
  "12": {
   "L": "Now we ask you, brothers, to acknowledge those who labor among you and lead you in the Lord and admonish you,",
   "M": "Now we ask you, brothers and sisters, to acknowledge those who work hard among you, who care for you in the Lord and who admonish you.",
   "T": "Brothers and sisters, we ask you to appreciate those who work hard among you—those who lead you in the Lord and correct you when needed."
  },
  "13": {
   "L": "and to regard them very highly in love because of their work. Be at peace among yourselves.",
   "M": "Hold them in the highest regard in love because of their work. Live in peace with each other.",
   "T": "Give them deep respect and love because of their work. Live at peace with one another."
  },
  "14": {
   "L": "We urge you, brothers: warn those who are idle and disorderly, encourage the discouraged, help the weak, be patient with all.",
   "M": "And we urge you, brothers and sisters, warn those who are idle and disruptive, encourage the disheartened, help the weak, be patient with everyone.",
   "T": "Brothers and sisters, we urge you: warn those who are lazy, encourage the timid, help those who are weak—and be patient with everyone."
  },
  "15": {
   "L": "See that no one repays evil for evil, but always pursue what is good for one another and for all.",
   "M": "Make sure that nobody pays back wrong for wrong, but always strive to do what is good for each other and for everyone else.",
   "T": "Make sure no one retaliates—wrong for wrong. Always pursue what is good, both for each other and for everyone."
  },
  "16": {
   "L": "Rejoice always,",
   "M": "Rejoice always,",
   "T": "Always be joyful."
  },
  "17": {
   "L": "pray without ceasing,",
   "M": "pray continually,",
   "T": "Pray constantly."
  },
  "18": {
   "L": "give thanks in everything; for this is the will of God in Christ Jesus for you.",
   "M": "give thanks in all circumstances; for this is God's will for you in Christ Jesus.",
   "T": "Give thanks in every situation—this is God's will for you in Christ Jesus."
  },
  "19": {
   "L": "Do not quench the Spirit.",
   "M": "Do not quench the Spirit.",
   "T": "Don't suppress the Spirit's work."
  },
  "20": {
   "L": "Do not despise prophecies.",
   "M": "Do not treat prophecies with contempt",
   "T": "Don't dismiss what the Spirit says through prophets."
  },
  "21": {
   "L": "But test all things; hold fast to what is good.",
   "M": "but test them all; hold on to what is good,",
   "T": "But test everything—hold on to what is good."
  },
  "22": {
   "L": "abstain from every form of evil.",
   "M": "reject every kind of evil.",
   "T": "Stay away from every kind of evil."
  },
  "23": {
   "L": "Now may the God of peace himself sanctify you completely, and may your whole spirit and soul and body be kept blameless at the coming of our Lord Jesus Christ.",
   "M": "May God himself, the God of peace, sanctify you through and through. May your whole spirit, soul and body be kept blameless at the coming of our Lord Jesus Christ.",
   "T": "May God himself—the God of peace—make you completely holy. May your whole spirit, soul, and body be kept blameless until the coming of our Lord Jesus Christ."
  },
  "24": {
   "L": "Faithful is he who calls you, who will also do it.",
   "M": "The one who calls you is faithful, and he will do it.",
   "T": "The one who calls you is faithful—he will do what he promised."
  },
  "25": {
   "L": "Brothers, pray for us also.",
   "M": "Brothers and sisters, pray for us.",
   "T": "Brothers and sisters, pray for us."
  },
  "26": {
   "L": "Greet all the brothers with a holy kiss.",
   "M": "Greet all God's people with a holy kiss.",
   "T": "Greet all the brothers and sisters with a holy embrace."
  },
  "27": {
   "L": "I charge you by the Lord to have this letter read to all the brothers.",
   "M": "I charge you before the Lord to have this letter read to all the brothers and sisters.",
   "T": "I solemnly charge you before the Lord: make sure this letter is read to all the brothers and sisters."
  },
  "28": {
   "L": "The grace of our Lord Jesus Christ be with you.",
   "M": "The grace of our Lord Jesus Christ be with you.",
   "T": "The grace of our Lord Jesus Christ be with you."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1thessalonians')
        merge_tier(existing, THESSALONIANS_1, tier_key)
        save(tier_dir, '1thessalonians', existing)
    print('1 Thessalonians 1–5 written.')

if __name__ == '__main__':
    main()
