"""
MKT 1 Corinthians chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1corinthians-1-3.py

These chapters address the division-by-teacher problem in the Corinthian church and pivot
immediately into Paul's theological response: the cross as God's wisdom, which overturns all
human wisdom hierarchies. The section climaxes (3:16-17) with the church-as-temple image.

Translation decisions:
- G3056 (λόγος): "word" in L (preserving the Johannine/Pauline range); "message" in M/T when
  the sense is proclamation (1:17,18; 2:1,4); "speech" in L for σοφία λόγου (1:17).
- G4678 (σοφία): "wisdom" throughout all tiers — the word must be felt in every occurrence
  because the wisdom/foolishness antithesis is the structural spine of these chapters.
- G4716 (σταυρός): "cross" throughout all tiers — not softened; the offensiveness is the point.
- G4561 (σάρξ): "flesh" in L always; "worldly standards" in M for 1:26 (kata sarka idiom);
  "sinful nature" avoided since 1:26 is sociological not soteriological.
- G4559/G4560 (σαρκικός/σάρκινος): "carnal" in L; "worldly" in M; "controlled by your earthly
  nature" in T — Paul's critique of the Corinthians is that their party spirit is sub-Christian.
- G4151 (πνεῦμα): "Spirit" (capitalized) for the Holy Spirit throughout ch 2 and 3:16-17;
  "spirit" (lowercase) for the human spirit in 2:11a ("the spirit of man"). Greek has no
  capitals — capitalization is a theological interpretation, documented here.
- G5591 (ψυχικός): L: "natural man"; M: "person without the Spirit"; T: "person who lives apart
  from the Spirit" — the ψυχικός/πνευματικός contrast is the axis of 2:14-15. ψυχικός is the
  un-regenerate person whose animating principle is the soul (psyche) not the Spirit; "natural"
  in L is the closest English cognate without adding interpretation.
- G4152 (πνευματικός): "spiritual" throughout.
- G1343 (δικαιοσύνη): L/M: "righteousness"; T: "right standing with God" at 1:30 — the
  forensic/relational sense is primary in the Christ-as-righteousness formula.
- G80 (ἀδελφοί): L: "brothers"; M/T: "brothers and sisters" — mixed congregation.
- G1577 (ἐκκλησία): "church" throughout — consistent with all other Pauline MKT scripts.
- G2842 (κοινωνία): "fellowship" L/M; "partnership" T at 1:9 — the commercial/covenant
  partnership sense (sharing in common enterprise) suits the context.
- G652 (ἀπόστολος): "apostle" throughout.
- G3485 (ναός): "temple" throughout — the inner sanctuary (ναός), not the whole temple complex
  (ἱερόν); the collective "you" (plural) is the corporate body in 3:16.
- G2782 (κήρυγμα): L: "proclamation"; M/T: "preaching" — the public heralding act.
- G3474 (μωρός/μωρία): "fool/foolish/foolishness" throughout.
- G40 (ἅγιος) applied to believers: "sanctified" (L at 1:2); "holy people" M/T — both the
  positional and progressive senses are present; "saints" is avoided in T as it implies a
  later ecclesiastical rank.
- G5486 (χάρισμα): "gift" L/M; "spiritual gift" T at 1:7 — the broader gift/grace range is
  preserved in L; T makes explicit the Spirit-origin.
- Textual note 1:1: Sosthenes is likely the synagogue ruler of Acts 18:17, later converted.
  Named as co-sender; L/M render "our brother" as per Greek; T unpacks "fellow believer."
- Textual note 2:1: Some MSS read μαρτύριον (testimony) rather than μυστήριον (mystery);
  the harder reading μαρτύριον is adopted, consistent with Paul's elsewhere established usage
  of "testimony" for the gospel proclamation (cf. 1:6). M/T use "testimony about God."
- Textual note 2:13: "comparing spiritual things with spiritual" (πνευματικοῖς πνευματικὰ
  συγκρίνοντες) — the verb can mean either "combining/matching" or "interpreting/explaining."
  L preserves ambiguity; M/T lean toward "explaining spiritual realities with Spirit-taught words."
- Aspect note: Perfect tense verbs in 1:6 (ἐβεβαιώθη), 2:12 (ἐλάβομεν) and elsewhere
  mark completed acts with ongoing results — rendered with English perfect where possible.
- OT echoes: 1:19 quotes Isa 29:14 (I will destroy the wisdom of the wise). 1:31 quotes
  Jer 9:24 (let him who boasts boast in the Lord). 2:9 alludes to Isa 64:4. 2:16 quotes
  Isa 40:13. 3:19 quotes Job 5:13. 3:20 quotes Ps 94:11. These OT citations give 1 Cor 1-3
  its dense scriptural texture; T surfaces the quotation character in translation.
- Honour-shame note: The shame/boasting vocabulary (καυχάομαι, αἰσχύνη) is pervasive.
  Greek society ran on public honour; Paul systematically inverts the honour code by
  locating honour in the cross and shame in worldly status. T surfaces this dynamic.
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
  "1": {
    "1": {
      "L": "Paul, called as an apostle of Christ Jesus through the will of God, and Sosthenes our brother,",
      "M": "Paul, called to be an apostle of Christ Jesus by the will of God, and our brother Sosthenes,",
      "T": "From Paul, appointed an apostle of Christ Jesus by God's own will, and from Sosthenes, our fellow believer."
    },
    "2": {
      "L": "to the church of God that is in Corinth, to those sanctified in Christ Jesus, called to be saints, together with all who in every place call upon the name of our Lord Jesus Christ, both their Lord and ours:",
      "M": "To the church of God in Corinth, to those sanctified in Christ Jesus and called to be his holy people, together with all those everywhere who call on the name of our Lord Jesus Christ—their Lord and ours:",
      "T": "To God's church in Corinth—to all who have been set apart in Christ Jesus and called as his holy people—and to everyone everywhere who calls on the name of our Lord Jesus Christ, who is their Lord and ours."
    },
    "3": {
      "L": "Grace to you and peace from God our Father and the Lord Jesus Christ.",
      "M": "Grace and peace to you from God our Father and the Lord Jesus Christ.",
      "T": "May God our Father and the Lord Jesus Christ grant you grace and peace."
    },
    "4": {
      "L": "I give thanks to my God always for you, for the grace of God that was given to you in Christ Jesus,",
      "M": "I always thank my God for you because of his grace given you in Christ Jesus.",
      "T": "I give thanks to God constantly for you, because of the grace God poured out on you through Christ Jesus."
    },
    "5": {
      "L": "that in every way you were enriched in him, in all speech and all knowledge—",
      "M": "For in him you have been enriched in every way—with all kinds of speech and with all knowledge—",
      "T": "Through your union with Christ you have been made rich in every way: in every kind of speech and in all depth of understanding."
    },
    "6": {
      "L": "even as the testimony of Christ was confirmed among you—",
      "M": "God thus confirming our testimony about Christ among you.",
      "T": "This confirms that what we testified about Christ is true in your experience."
    },
    "7": {
      "L": "so that you are not lacking in any gift, as you wait for the revealing of our Lord Jesus Christ,",
      "M": "Therefore you do not lack any spiritual gift as you eagerly wait for our Lord Jesus Christ to be revealed.",
      "T": "As a result you have received every spiritual gift and lack nothing while you wait for the return of our Lord Jesus Christ."
    },
    "8": {
      "L": "who will also confirm you to the end, blameless in the day of our Lord Jesus Christ.",
      "M": "He will also keep you firm to the end, so that you will be blameless on the day of our Lord Jesus Christ.",
      "T": "He will keep you strong right up to the end so that you stand blameless on the day when our Lord Jesus Christ is revealed."
    },
    "9": {
      "L": "God is faithful, through whom you were called into the fellowship of his Son, Jesus Christ our Lord.",
      "M": "God is faithful, who has called you into fellowship with his Son, Jesus Christ our Lord.",
      "T": "God keeps every promise he makes—and it was he who called you into this partnership with his Son, Jesus Christ our Lord."
    },
    "10": {
      "L": "Now I appeal to you, brothers, through the name of our Lord Jesus Christ, that you all speak the same thing, and that there be no divisions among you, but that you be perfectly restored in the same mind and in the same judgment.",
      "M": "I appeal to you, brothers and sisters, in the name of our Lord Jesus Christ, that all of you agree with one another in what you say and that there be no divisions among you, but that you be perfectly united in mind and thought.",
      "T": "I urge you, brothers and sisters, by the authority of our Lord Jesus Christ—stop the quarreling! Let there be no factions among you. Be knit together in perfect harmony, united in your thinking and your purpose."
    },
    "11": {
      "L": "For it was made clear to me about you, my brothers, by those of Chloe, that there are contentions among you.",
      "M": "My brothers and sisters, some from Chloe's household have informed me that there are quarrels among you.",
      "T": "Some of Chloe's people have told me about your disputes, dear brothers and sisters, and I must address it directly."
    },
    "12": {
      "L": "Now I say this: that each of you is saying, 'I am of Paul,' or 'I of Apollos,' or 'I of Cephas,' or 'I of Christ.'",
      "M": "What I mean is this: One of you says, 'I follow Paul'; another, 'I follow Apollos'; another, 'I follow Cephas'; still another, 'I follow Christ.'",
      "T": "Each of you is taking sides: 'I am a follower of Paul,' or 'I follow Apollos,' or 'I follow Peter,' or 'I follow only Christ.'"
    },
    "13": {
      "L": "Has Christ been divided? Was Paul crucified for you? Or into the name of Paul were you baptized?",
      "M": "Is Christ divided? Was Paul crucified for you? Were you baptized in the name of Paul?",
      "T": "Has Christ been split into factions? Was it Paul who was crucified for you? Were you baptized in Paul's name? Of course not!"
    },
    "14": {
      "L": "I thank God that I baptized none of you except Crispus and Gaius,",
      "M": "I thank God that I did not baptize any of you except Crispus and Gaius,",
      "T": "I am thankful that I baptized none of you except Crispus and Gaius,"
    },
    "15": {
      "L": "lest anyone say that you were baptized into my name.",
      "M": "so no one can say that you were baptized in my name.",
      "T": "for now no one can claim they were baptized in my name."
    },
    "16": {
      "L": "But I also baptized the household of Stephanas; for the rest, I do not know whether I baptized anyone else.",
      "M": "(Yes, I also baptized the household of Stephanas; beyond that, I don't remember if I baptized anyone else.)",
      "T": "Oh yes—I also baptized the household of Stephanas. I honestly cannot recall baptizing anyone else."
    },
    "17": {
      "L": "For Christ did not send me to baptize, but to preach the gospel, not in wisdom of speech, lest the cross of Christ be emptied of its power.",
      "M": "For Christ did not send me to baptize, but to preach the gospel—not with wisdom of words, lest the cross of Christ be emptied of its power.",
      "T": "Christ did not send me to perform baptisms, but to proclaim the good news—and not with clever rhetoric, for that would empty the cross of Christ of its power."
    },
    "18": {
      "L": "For the word of the cross is foolishness to those who are perishing, but to us who are being saved it is the power of God.",
      "M": "For the message of the cross is foolishness to those who are perishing, but to us who are being saved it is the power of God.",
      "T": "The message about the cross sounds like sheer nonsense to those who are headed for destruction. But to us who are being saved, it is nothing less than the power of God at work."
    },
    "19": {
      "L": "For it is written: 'I will destroy the wisdom of the wise, and the understanding of the understanding I will set aside.'",
      "M": "For it is written: 'I will destroy the wisdom of the wise; the intelligence of the intelligent I will frustrate.'",
      "T": "As Scripture says, 'I will destroy the wisdom of the wise and make the intelligence of the intelligent utterly pointless.'"
    },
    "20": {
      "L": "Where is the wise? Where is the scribe? Where is the disputer of this age? Did not God make foolish the wisdom of the world?",
      "M": "Where is the wise person? Where is the teacher of the law? Where is the philosopher of this age? Has not God made foolish the wisdom of the world?",
      "T": "So where does that leave the brilliant thinkers, the scholars, and the world's great debaters? God has made the wisdom of this world look utterly foolish."
    },
    "21": {
      "L": "For since in the wisdom of God the world through wisdom did not know God, God was pleased through the foolishness of the proclamation to save those who believe.",
      "M": "For since in the wisdom of God the world through its wisdom did not know him, God was pleased through the foolishness of what was preached to save those who believe.",
      "T": "Since God in his wisdom ensured that human wisdom could never bring the world to know him, he chose to use what sounds like a foolish message to save those who trust in him."
    },
    "22": {
      "L": "For Jews ask for signs and Greeks seek wisdom,",
      "M": "Jews demand signs and Greeks look for wisdom,",
      "T": "The Jews demand spectacular signs, and the Greeks go looking for philosophical wisdom,"
    },
    "23": {
      "L": "but we preach Christ crucified, a stumbling block to Jews and foolishness to Gentiles,",
      "M": "but we preach Christ crucified: a stumbling block to Jews and foolishness to Gentiles,",
      "T": "but we proclaim Christ crucified—a scandal to the Jews and sheer nonsense to the Gentiles."
    },
    "24": {
      "L": "but to those who are called, both Jews and Greeks, Christ the power of God and the wisdom of God.",
      "M": "but to those whom God has called, both Jews and Greeks, Christ the power of God and the wisdom of God.",
      "T": "Yet to those who have been called by God—Jews and Gentiles alike—Christ himself is the power of God and the wisdom of God."
    },
    "25": {
      "L": "For the foolishness of God is wiser than men, and the weakness of God is stronger than men.",
      "M": "For the foolishness of God is wiser than human wisdom, and the weakness of God is stronger than human strength.",
      "T": "What God does that looks foolish to us is wiser than the greatest human wisdom, and what looks weak in God is stronger than the mightiest human force."
    },
    "26": {
      "L": "For consider your calling, brothers: not many were wise according to the flesh, not many were powerful, not many were of noble birth.",
      "M": "Brothers and sisters, think of what you were when you were called. Not many of you were wise by human standards; not many were influential; not many were of noble birth.",
      "T": "Think about your own calling, brothers and sisters. By the world's standards, not many of you were wise, not many were powerful, and not many came from prominent families."
    },
    "27": {
      "L": "But God chose the foolish things of the world to shame the wise; God chose the weak things of the world to shame the strong;",
      "M": "But God chose the foolish things of the world to shame the wise; God chose the weak things of the world to shame the strong.",
      "T": "But God deliberately chose what the world considers foolish in order to shame those who think themselves wise. He chose what the world considers powerless to shame those who are strong."
    },
    "28": {
      "L": "God chose the base things of the world and the despised, the things that are not, to bring to nothing the things that are,",
      "M": "God chose the lowly things of this world and the despised things—and the things that are not—to nullify the things that are,",
      "T": "God chose those the world counts as nothing—the despised, the overlooked, the powerless—to bring to nothing what the world regards as something."
    },
    "29": {
      "L": "so that no flesh might boast before God.",
      "M": "so that no one may boast before him.",
      "T": "He did all this so that no human being could ever stand before God and claim credit for themselves."
    },
    "30": {
      "L": "And because of him you are in Christ Jesus, who became to us wisdom from God—righteousness and sanctification and redemption—",
      "M": "It is because of him that you are in Christ Jesus, who has become for us wisdom from God—that is, our righteousness, holiness and redemption.",
      "T": "God united you with Christ Jesus. Christ himself has become our wisdom—he has made us right with God, set us apart as holy, and freed us from sin."
    },
    "31": {
      "L": "so that, as it is written: 'Let him who boasts, boast in the Lord.'",
      "M": "Therefore, as it is written: 'Let the one who boasts boast in the Lord.'",
      "T": "Therefore, as Scripture says, 'If you want to boast, boast only about what the Lord has done.'"
    }
  },
  "2": {
    "1": {
      "L": "And I, brothers, when I came to you, came not with superiority of speech or wisdom, proclaiming to you the testimony of God.",
      "M": "And so it was with me, brothers and sisters. When I came to you, I did not come with eloquence or superior wisdom as I proclaimed to you the testimony about God.",
      "T": "When I first came to you, brothers and sisters, I did not bring brilliant arguments or high-sounding philosophy. I simply proclaimed to you the truth about God."
    },
    "2": {
      "L": "For I decided to know nothing among you except Jesus Christ, and him crucified.",
      "M": "For I resolved to know nothing while I was with you except Jesus Christ and him crucified.",
      "T": "I deliberately kept my message simple—nothing but Jesus Christ, and him crucified."
    },
    "3": {
      "L": "And I was with you in weakness and in fear and much trembling,",
      "M": "I came to you in weakness with great fear and trembling.",
      "T": "I arrived among you feeling weak and nervous, quite overwhelmed by the task."
    },
    "4": {
      "L": "and my word and my preaching were not in persuasive words of wisdom, but in demonstration of the Spirit and of power,",
      "M": "My message and my preaching were not with wise and persuasive words, but with a demonstration of the Spirit's power,",
      "T": "My message and my preaching carried no clever argument or polished rhetoric—only the Spirit's own convincing power."
    },
    "5": {
      "L": "so that your faith might not rest in the wisdom of men but in the power of God.",
      "M": "so that your faith might not rest on human wisdom, but on God's power.",
      "T": "I wanted your faith to stand on God's power alone, not on any human reasoning."
    },
    "6": {
      "L": "Yet wisdom we do speak among the mature, but not a wisdom of this age, nor of the rulers of this age, who are being brought to nothing.",
      "M": "We do, however, speak a message of wisdom among the mature, but not the wisdom of this age or of the rulers of this age, who are coming to nothing.",
      "T": "There is a genuine wisdom we share with those who are spiritually mature—but it is not the wisdom of this present age, nor of this world's rulers, who are rapidly losing their grip on things."
    },
    "7": {
      "L": "But we speak God's wisdom in a mystery, the hidden wisdom, which God ordained before the ages for our glory.",
      "M": "No, we declare God's wisdom, a mystery that has been hidden and that God destined for our glory before time began.",
      "T": "We speak of God's secret wisdom—kept hidden through all the ages, yet planned by God before time itself began, destined to bring us into glory."
    },
    "8": {
      "L": "None of the rulers of this age knew this, for if they had known it, they would not have crucified the Lord of glory.",
      "M": "None of the rulers of this age understood it, for if they had, they would not have crucified the Lord of glory.",
      "T": "Not one of this world's rulers grasped this hidden wisdom. If they had, they would never have crucified the Lord of glory."
    },
    "9": {
      "L": "But as it is written: 'Eye has not seen, nor ear heard, nor has it entered into the heart of man what things God has prepared for those who love him'—",
      "M": "However, as it is written: 'What no eye has seen, what no ear has heard, and what no human mind has conceived'—the things God has prepared for those who love him—",
      "T": "But as Scripture hints: 'No eye has seen it, no ear has heard it, no mind can fully conceive it—all that God has prepared for those who love him.'"
    },
    "10": {
      "L": "but God has revealed them to us through the Spirit; for the Spirit searches all things, even the depths of God.",
      "M": "these are the things God has revealed to us by his Spirit. The Spirit searches all things, even the deep things of God.",
      "T": "Yet God has revealed these very things to us by his Spirit—for the Spirit probes all depths, even the deepest mysteries of God."
    },
    "11": {
      "L": "For who among men knows the things of a man except the spirit of man which is in him? So also no one has known the things of God except the Spirit of God.",
      "M": "For who knows a person's thoughts except their own spirit within them? In the same way no one knows the thoughts of God except the Spirit of God.",
      "T": "No one can know another person's innermost thoughts except that person's own spirit. In the same way, no one can know God's thoughts except God's own Spirit."
    },
    "12": {
      "L": "But we have received not the spirit of the world, but the Spirit which is from God, so that we might know the things freely given to us by God.",
      "M": "What we have received is not the spirit of the world, but the Spirit who is from God, so that we may understand what God has freely given us.",
      "T": "We have not received the spirit of this world—we have received the Spirit who comes from God himself, so that we can truly understand and receive everything God has so freely given us."
    },
    "13": {
      "L": "which we also speak—not in words taught by human wisdom, but in words taught by the Spirit—comparing spiritual things with spiritual.",
      "M": "This is what we speak, not in words taught us by human wisdom but in words taught by the Spirit, explaining spiritual realities with Spirit-taught words.",
      "T": "When we tell you these things, we do not use words invented by human wisdom. Instead, we use words the Spirit himself teaches us, interpreting spiritual realities in Spirit-given language."
    },
    "14": {
      "L": "But the natural man does not receive the things of the Spirit of God, for they are foolishness to him, and he is not able to know them, because they are spiritually discerned.",
      "M": "The person without the Spirit does not accept the things that come from the Spirit of God but considers them foolishness, and cannot understand them because they are discerned only through the Spirit.",
      "T": "But a person who lives apart from the Spirit cannot receive the gifts of God's Spirit—they seem like nonsense to such a person, and they cannot be understood without a spiritual mind to perceive them."
    },
    "15": {
      "L": "But the spiritual man judges all things, but he himself is judged by no one.",
      "M": "The person with the Spirit makes judgments about all things, but such a person is not subject to merely human judgments:",
      "T": "The person who is truly spiritual can evaluate all things rightly, yet no merely human standard of judgment can evaluate such a person."
    },
    "16": {
      "L": "'For who has known the mind of the Lord, that he will instruct him?' But we have the mind of Christ.",
      "M": "for, 'Who has known the mind of the Lord so as to instruct him?' But we have the mind of Christ.",
      "T": "For as Scripture asks, 'Who can know the Lord's thoughts well enough to advise him?' But we have been given the mind of Christ—we think and discern with his wisdom."
    }
  },
  "3": {
    "1": {
      "L": "And I, brothers, was not able to speak to you as to spiritual ones, but as to fleshly ones—as to infants in Christ.",
      "M": "Brothers and sisters, I could not address you as people who live by the Spirit but as people who are still worldly—mere infants in Christ.",
      "T": "But I could not address you as people matured by the Spirit. You were still like infants in the faith, still controlled by your earthly nature."
    },
    "2": {
      "L": "With milk I fed you and not with solid food, for you were not yet able; but not even now are you able,",
      "M": "I gave you milk, not solid food, for you were not yet ready for it. Indeed, you are still not ready.",
      "T": "I gave you spiritual milk, not solid teaching, because you were not mature enough for it. And you are still not ready,"
    },
    "3": {
      "L": "for you are still fleshly. For since there is jealousy and strife among you, are you not fleshly and walking according to man?",
      "M": "You are still worldly. For since there is jealousy and quarreling among you, are you not worldly? Are you not acting like mere humans?",
      "T": "because you are still controlled by your earthly nature. When you are jealous of one another and quarreling among yourselves, doesn't that prove it? You are living by purely human standards."
    },
    "4": {
      "L": "For when one says, 'I am of Paul,' and another, 'I am of Apollos,' are you not merely men?",
      "M": "For when one says, 'I follow Paul,' and another, 'I follow Apollos,' are you not mere human beings?",
      "T": "When one of you says, 'I am a follower of Paul,' and another says, 'I follow Apollos,' you are acting just like ordinary, un-spiritual people."
    },
    "5": {
      "L": "What then is Apollos? And what is Paul? Servants through whom you believed, as the Lord assigned to each.",
      "M": "What, after all, is Apollos? And what is Paul? Only servants, through whom you came to believe—as the Lord has assigned to each his task.",
      "T": "Who are Apollos and Paul anyway? We are merely God's servants who brought you to faith. Each of us did whatever task the Lord assigned."
    },
    "6": {
      "L": "I planted, Apollos watered, but God gave the growth.",
      "M": "I planted the seed, Apollos watered it, but God has been making it grow.",
      "T": "I planted the seed, Apollos watered it—but it was God who made it grow."
    },
    "7": {
      "L": "So then neither the one who plants nor the one who waters is anything, but God who gives the growth.",
      "M": "So neither the one who plants nor the one who waters is anything, but only God, who makes things grow.",
      "T": "It is not the planter or the waterer who matters—only God, who gives the growth."
    },
    "8": {
      "L": "Now he who plants and he who waters are one, and each will receive his own wage according to his own labor.",
      "M": "The one who plants and the one who waters have one purpose, and they will each be rewarded according to their own labor.",
      "T": "The planter and the waterer work together as partners with a single goal, and each will be rewarded in proportion to their own work."
    },
    "9": {
      "L": "For we are God's fellow workers; you are God's field, God's building.",
      "M": "For we are co-workers in God's service; you are God's field, God's building.",
      "T": "We are all God's partners in his work—and you are God's farm and God's house."
    },
    "10": {
      "L": "According to the grace of God given to me, as a wise master builder I laid a foundation, and another is building upon it. But let each one take care how he builds upon it.",
      "M": "By the grace God has given me, I laid a foundation as a wise builder, and someone else is building on it. But each one should build with care.",
      "T": "Because of the grace God gave me, I laid the foundation as a skilled master builder. Now others are building on it—but every builder must be careful how he builds."
    },
    "11": {
      "L": "For no other foundation can anyone lay than that which is laid, which is Jesus Christ.",
      "M": "For no one can lay any foundation other than the one already laid, which is Jesus Christ.",
      "T": "For no one can lay any other foundation than the one that has already been laid: Jesus Christ himself."
    },
    "12": {
      "L": "Now if anyone builds on this foundation with gold, silver, precious stones, wood, hay, straw—",
      "M": "If anyone builds on this foundation using gold, silver, costly stones, wood, hay or straw,",
      "T": "Anyone who builds on that foundation may use a variety of materials—gold, silver, jewels, wood, hay, or straw."
    },
    "13": {
      "L": "each man's work will be made manifest; for the Day will declare it, because it is revealed in fire; and the fire will test each man's work, of what sort it is.",
      "M": "their work will be shown for what it is, because the Day will bring it to light. It will be revealed with fire, and the fire will test the quality of each person's work.",
      "T": "But on the day of judgment, fire will reveal what kind of work each builder has done. That fire will test whether the work was worth keeping."
    },
    "14": {
      "L": "If the work of anyone remains which he has built on, he will receive a reward.",
      "M": "If what has been built survives, the builder will receive a reward.",
      "T": "If the work survives the fire, that builder will be rewarded."
    },
    "15": {
      "L": "If the work of anyone is burned up, he will suffer loss, but he himself will be saved—yet so as through fire.",
      "M": "If it is burned up, the builder will suffer loss but yet will be saved—even though only as one escaping through the flames.",
      "T": "But if the work is burned up, the builder will suffer great loss. The builder will be saved—but like someone who barely escapes through a wall of flames."
    },
    "16": {
      "L": "Do you not know that you are a temple of God, and that the Spirit of God dwells in you?",
      "M": "Don't you know that you yourselves are God's temple and that God's Spirit dwells in your midst?",
      "T": "Don't you realize that all of you together are the temple of God, and that God's Spirit lives in you?"
    },
    "17": {
      "L": "If anyone destroys the temple of God, God will destroy him; for the temple of God is holy, which you are.",
      "M": "If anyone destroys God's temple, God will destroy that person; for God's temple is sacred, and you together are that temple.",
      "T": "God will destroy anyone who destroys this temple—for God's own temple is holy, and you are that temple."
    },
    "18": {
      "L": "Let no one deceive himself. If anyone among you thinks he is wise in this age, let him become a fool so that he may become wise.",
      "M": "Do not deceive yourselves. If any of you think you are wise by the standards of this age, you should become 'fools' so that you may become wise.",
      "T": "Stop deceiving yourselves! If you think you are wise by this world's standards, you need to become a fool in the world's eyes before you can be truly wise."
    },
    "19": {
      "L": "For the wisdom of this world is foolishness with God. For it is written: 'He is the one who catches the wise in their craftiness;'",
      "M": "For the wisdom of this world is foolishness in God's sight. As it is written: 'He catches the wise in their craftiness;'",
      "T": "For what the world calls wisdom is foolishness before God. As Scripture says, 'He traps the wise in the snare of their own cleverness;'"
    },
    "20": {
      "L": "and again: 'The Lord knows the thoughts of the wise, that they are futile.'",
      "M": "and again, 'The Lord knows that the thoughts of the wise are futile.'",
      "T": "and again, 'The Lord sees through the reasoning of the wise—all their brilliant thoughts lead nowhere.'"
    },
    "21": {
      "L": "So then, let no one boast in men. For all things are yours,",
      "M": "So then, no more boasting about human leaders! All things are yours,",
      "T": "So stop boasting about following particular human teachers. Everything belongs to you—"
    },
    "22": {
      "L": "whether Paul or Apollos or Cephas or the world or life or death or things present or things to come—all are yours,",
      "M": "whether Paul or Apollos or Cephas or the world or life or death or the present or the future—all are yours,",
      "T": "Paul, Apollos, Peter, the entire world, life itself, death, the present and the future—all of it is yours."
    },
    "23": {
      "L": "and you are Christ's, and Christ is God's.",
      "M": "and you are of Christ, and Christ is of God.",
      "T": "And you belong to Christ, and Christ belongs to God."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1corinthians')
        merge_tier(existing, CORINTHIANS1, tier_key)
        save(tier_dir, '1corinthians', existing)
    print('1 Corinthians 1–3 written.')

if __name__ == '__main__':
    main()
