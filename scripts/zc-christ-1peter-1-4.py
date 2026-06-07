"""
Combined script: James, 1 Peter, 2 Peter, 2 John, 3 John, Jude — all four layers.
Output: echoes + mkt-original + mkt-context + mkt-christ for each letter.

The General Epistles span wisdom tradition (James), suffering-theology (1 Peter),
eschatological warning (2 Peter, Jude), and community discernment (2-3 John).
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

# ============================================================
# JAMES
# ============================================================

JAMES_ECHO = {
  "1": {
    "17": [
      {"type": "allusion", "target": "Num 23:19", "note": "With whom there is no variation or shadow due to change — God is not a man that he should lie or change his mind; YHWH's immutability as the ground of trust echoes in James's description of the Father of lights"},
      {"type": "allusion", "target": "Mal 3:6", "note": "I the LORD do not change — YHWH's immutability guarantees the covenant; James's 'no variation' language in describing the Father draws from the prophetic declaration of divine constancy"}
    ]
  },
  "2": {
    "23": [
      {"type": "fulfillment", "target": "Gen 15:6", "note": "Abraham believed God and it was counted to him as righteousness, and he was called a friend of God — James cites Gen 15:6 (as does Paul in Rom 4 and Gal 3) but applies it to the Abraham of Gen 22 (the Aqedah); the faith that justified Abraham was not bare intellectual belief but the active trust that obeyed unto the ultimate test"}
    ]
  },
  "4": {
    "6": [
      {"type": "quote", "target": "Prov 3:34", "note": "God opposes the proud but gives grace to the humble — James quotes Prov 3:34 LXX exactly (as does 1 Pet 5:5); the wisdom tradition's insistence that YHWH resists the arrogant and upholds the lowly is the hermeneutical key to James's social ethics"}
    ]
  },
  "5": {
    "4": [
      {"type": "allusion", "target": "Isa 5:9", "note": "Behold the pay of the laborers who mowed your fields, which you kept back by fraud, is crying out — YHWH's ear hears the cry of the oppressed wages; James's eschatological indictment of wealthy landowners echoes the Isaianic woe-oracles against exploitative landowners"}
    ]
  }
}

JAMES_ORIGINAL = {
  "1": {
    "2": "<p><strong>pasan charan hegesasthe adelphoi mou hotan peirasmois peripesete poikilois</strong> (<em>pāsan charān hēgēsasthe, adelphoi mou, hotan peirasmois peripesēte poikilois</em>): 'Count it all joy when you fall into various trials.' <em>Hegeomai</em> (count/consider) is a deliberate act of valuation — joy is not a natural reaction to trials but a chosen re-evaluation. <em>Peirasmoi</em> (trials/temptations) covers both external testing by circumstances (v. 2-4) and internal temptation by desire (v. 13-14) — James distinguishes them but uses the same word, showing that external pressure and internal desire interact in the same human experience of testing.</p>",

    "22": "<p><strong>ginesthe de poietai logou kai me monon akroatai paralogizomenoi heautous</strong> (<em>ginesthe de poiētai logou kai mē monon akroatai paralogizomenoi heautous</em>): 'Be doers of the word and not hearers only, deceiving yourselves.' <em>Poietes logou</em> (doer of the word): the verbal-moral contrast between hearing and doing is fundamental to both the wisdom tradition (Prov 2:1-6) and the dominical teaching (Matt 7:24-27: the wise and foolish builders). <em>Paralogizomenoi</em> (deceiving, reasoning falsely alongside) implies a syllogistic self-deception: 'I heard the word, therefore I have received it and its benefits' — the error of intellectual reception without moral transformation.</p>"
  },
  "2": {
    "14": "<p><strong>ti ophelos adelphoi mou ean pistin lege tis echein erga de me eche</strong> (<em>ti ophelos, adelphoi mou, ean pistin legē tis echein, erga de mē echē</em>): 'What good is it, my brothers, if someone says he has faith but does not have works?' The famous James-Paul tension: Luther notoriously called James 'an epistle of straw' for seeming to contradict Paul's faith-righteousness. The resolution lies in different uses of <em>pistis</em>: Paul's 'faith' is the whole person's trust in and surrender to God; James's target is a merely verbal profession (<em>legē tis echein</em>, 'says he has faith') without ethical corollary. James and Paul agree that genuine faith produces works (cf. Gal 5:6: 'faith working through love'); their different opponents require different emphases.</p>"
  },
  "3": {
    "1": "<p><strong>me polloi didaskaloi ginesthe adelphoi mou eidotes hoti meizon krima lepsometha</strong> (<em>mē polloi didaskaloi ginesthe, adelphoi mou, eidotes hoti meizon krima lēpsometha</em>): 'Not many of you should become teachers, my brothers, knowing that we who teach will be judged with greater strictness.' The <em>meizon krima</em> (greater judgment) for teachers reflects the Jewish wisdom tradition's high estimation of the Torah-teacher's responsibility (m. Avot 2:7: 'the more Torah, the more life; the more study, the more wisdom; the more counsel, the more understanding; the more righteousness, the more peace; ... the more Torah, the more life') and its warning about the consequences of teaching falsehood. James is aware of his own exposure to this judgment.</p>"
  }
}

JAMES_CONTEXT = {
  "1": {
    "1": "<p>James is addressed 'to the twelve tribes in the Dispersion' — framing the audience as the diaspora Jewish-Christian community. Whether 'James the brother of the Lord' (Gal 1:19; Josephus Ant. 20.200) is the author (martyred 62 CE) or a pseudonymous use of his authority (ca. 80-100 CE) is debated, but the letter's decidedly Jewish-Christian character (the synagogue imagery of 2:2; the explicit wisdom-tradition shaping; the prophetic social ethics) is consistent with Jerusalem's Jewish-Christian leader. Josephus describes James as 'the brother of Jesus who was called Christ' and records his death by stoning at the instigation of the high priest Ananus II, ca. 62 CE. If authentic, James is among the earliest NT writings.</p>"
  },
  "2": {
    "1": "<p>The community James addresses assembles in a <em>synagoge</em> (2:2) — the term for a Jewish gathering-place, not yet the distinctly Christian <em>ekklesia</em> (church building). The social stratification problem (wealthy visitor with gold rings and fine clothing given the good seat; poor visitor told to stand or sit on the floor) reflects the patron-client dynamics of both the Roman and the Palestinian Jewish world. James's condemnation of partiality (<em>prosopolepsia</em>) is grounded in the same divine-impartiality tradition Paul invokes (Rom 2:11; Acts 10:34) — YHWH who shows no partiality to the rich over the poor is the standard for the community's hospitality.</p>"
  }
}

JAMES_CHRIST = {
  "1": {
    "17": "<p>A revelation of God: 'Every good gift and every perfect gift is from above, coming down from the Father of lights, with whom there is no variation or shadow due to change.' James's God-centered theology (without yet making a Christological application) shows the Father's immutable character as the ground of human trust and patience in trial. The Christological trajectory: this unchanging Father of lights is the one who sent his Son (not yet named in ch.1, but cf. 2:1: 'the faith in our Lord Jesus Christ, the Lord of glory'). The stability of the Father underwrites the whole counsel of the letter.</p>"
  },
  "2": {
    "1": "<p>A direct revelation: 'The faith of our Lord Jesus Christ, the Lord of glory.' James's only explicit Christological title is <em>Kyrios tes doxes</em> — 'the Lord of glory.' In LXX Ps 24:7-10, the 'King of glory' (<em>basileus tes doxes</em>) is YHWH himself. James transfers this divine glory-title to Jesus: to hold 'the faith of the Lord of glory' while showing partiality to the rich is a theological contradiction — the one who identifies with the poor (the Magnificat's God; the Beatitudes' Christ) cannot be honored by honoring the rich over the poor.</p>"
  },
  "5": {
    "7": "<p>A direct revelation: 'Be patient, therefore, brothers, until the coming of the Lord.' James ends with the parousia as the motive for patience in suffering (vv. 7-11) and restraint of speech (vv. 12). The 'coming of the Lord' (<em>parousia tou Kyriou</em>) frames the whole letter's ethics eschatologically: the injustice of the rich oppressors, the suffering of the righteous, the unanswered prayers — all are held before the coming Judge (v. 9: 'the Judge is standing at the door'). The standing judge at the door is the Christ whose coming is imminent.</p>"
  }
}

# ============================================================
# 1 PETER
# ============================================================

ONEPET_ECHO = {
  "1": {
    "16": [
      {"type": "quote", "target": "Lev 11:44", "note": "You shall be holy, for I am holy — the Levitical holiness-imperative is directly quoted as the foundation for Peter's ethics; the holiness character of YHWH is the standard for covenant-community behavior in both the old and new covenants"}
    ],
    "24": [
      {"type": "fulfillment", "target": "Isa 40:6-8", "note": "All flesh is like grass and all its glory like the flower of grass; the grass withers and the flower falls, but the word of the Lord remains forever — Peter applies Isa 40:6-8 to the imperishable seed of the gospel-word; the word that endures is the good news preached to them, fulfilling Isaiah's consolation-proclamation"}
    ]
  },
  "2": {
    "6": [
      {"type": "fulfillment", "target": "Isa 28:16", "note": "Behold I am laying in Zion a stone, a cornerstone chosen and precious, and whoever believes in him will not be put to shame — Peter cites Isa 28:16 LXX as fulfilled in Christ; the Zion-foundation stone of Isaiah is identified with the rejected-and-vindicated Christ"},
      {"type": "fulfillment", "target": "Ps 118:22", "note": "The stone that the builders rejected has become the cornerstone — the second OT stone text: the rejected cornerstone of Ps 118 is Christ crucified and raised; the very rejection that qualified him as victim becomes his exaltation-identity"},
      {"type": "fulfillment", "target": "Isa 8:14", "note": "A stone of stumbling and a rock of offense — Isa 8:14 LXX (YHWH as both sanctuary and stone of stumbling for Israel); Peter applies the dual effect to Christ: to believers, the cornerstone; to unbelievers, the stumbling stone"}
    ],
    "9": [
      {"type": "fulfillment", "target": "Exod 19:6", "note": "A royal priesthood, a holy nation — Peter applies the Sinai covenant's identity-markers (Exod 19:6: a kingdom of priests and a holy nation) directly to the church; the new covenant community is the Sinai identity realized and expanded beyond ethnic Israel"},
      {"type": "fulfillment", "target": "Isa 43:20-21", "note": "A people for his own possession, that you may proclaim the excellencies of him who called you — Isa 43:21 LXX (my people whom I formed for myself, to declare my praise); Peter completes the new-community description with the Isaianic mission: called-out-from-darkness people who exist to proclaim the God who called them"}
    ]
  },
  "3": {
    "10": [
      {"type": "quote", "target": "Ps 34:12-16", "note": "Whoever desires to love life and see good days, let him keep his tongue from evil — Peter quotes Ps 34:12-16 LXX directly as the biblical foundation for his ethics of suffering and peace-seeking; Psalm 34 (the acrostic of David's deliverance) becomes the wisdom-framework for the community's response to hostility"}
    ]
  },
  "5": {
    "5": [
      {"type": "quote", "target": "Prov 3:34", "note": "God opposes the proud but gives grace to the humble — same Prov 3:34 LXX quotation as James 4:6; the shared citation indicates it was a widely known community warrant for humility in the face of suffering and opposition"}
    ]
  }
}

ONEPET_ORIGINAL = {
  "1": {
    "3": "<p><strong>anagennesas hemas eis elpida zosan di anastaseos Iesou Christou ek nekron</strong> (<em>anagennēsas hēmas eis elpida zōsan di anastaseōs Iēsou Christou ek nekrōn</em>): 'who has caused us to be born again to a living hope through the resurrection of Jesus Christ from the dead.' <em>Anagennao</em> (born again/anew) appears only here and v. 23 in the NT; John 3 uses <em>gennethenai anothen</em> (born from above/again). The new birth is not an isolated spiritual event but a directed new genesis: <em>eis elpida zosan</em> (into a living hope). The resurrection of Christ is not merely the means but the content of the hope — living hope because the Resurrected One lives.</p>",

    "18": "<p><strong>ou phthartois argyrio e chruso oi elytrothete ... alla timio haimati has amnos amomou kai aspilon Christou</strong> (<em>ou phthartois, argyriō ē chrysō, oi elytrōthēte ... alla timiō haimati hōs amnos amōmou kai aspilou Christou</em>): 'not with perishable things such as silver or gold, but with the precious blood of Christ, like that of a lamb without blemish or spot.' The ransom-metaphor (<em>lytroō</em>, redeem/ransom) is grounded in the Exodus-redemption of Israel (Exod 6:6: 'I will redeem you with an outstretched arm') and the Servant's self-pouring in Isa 53. The lamb-without-blemish terminology is directly cultic: the Passover lamb (Exod 12:5) and the sacrificial requirements of Lev 22:19-25 — Christ fulfills the sacrificial requirements as the perfect offering.</p>"
  },
  "2": {
    "24": "<p><strong>hos tas hamartias hemon autos anenegken en to somati autou epi to xylon</strong> (<em>hos tas hamartias hēmōn autos anēnenken en tō sōmati autou epi to xylon</em>): 'He himself bore our sins in his body on the tree.' The language is saturated with Isa 53: <em>anaphero</em> is the LXX word for the priestly act of lifting/bearing an offering to the altar; <em>epi to xylon</em> (on the tree) echoes Deut 21:23 (a hanged man is cursed) and Gal 3:13 (Christ redeemed us from the curse of the law by becoming a curse for us). The phrase 'in his body' is a deliberate anti-Docetic marker: the sin-bearing was physical, not merely spiritual — the crucifixion was real.</p>"
  }
}

ONEPET_CONTEXT = {
  "1": {
    "1": "<p>1 Peter is addressed to the diaspora of Pontus, Galatia, Cappadocia, Asia, and Bithynia — a geographic sweep of the northern half of Asia Minor (modern Turkey). The term <em>parepidemos</em> (sojourner/temporary resident, v. 1) and <em>paroikos</em> (alien/resident without citizenship, 2:11) had legal specificity: resident aliens without full citizenship rights, dependent on local good will. Peter applies these social categories to the spiritual situation of believers: they are not truly at home in this age, regardless of their legal status. The five provinces listed correspond roughly to the area of a Bithynian governor's jurisdiction, suggesting a single administrative document.</p>"
  },
  "2": {
    "13": "<p>Peter's 'submit to every human institution' (<em>hypotassō pase anthropine ktisei</em>) parallels Paul's Romans 13, but the social context is different: 1 Peter addresses communities facing active hostility and false accusation, not merely civic obligation. The political submission is part of the apologetic strategy: by visibly good behavior (v. 15: <em>agathopoia</em>, doing good), the community silences the ignorance of foolish critics. The 'honor everyone, love the brotherhood, fear God, honor the emperor' (v. 17) places the emperor in the fourth position — honored, but not uniquely so, and subordinate to God-fear.</p>"
  }
}

ONEPET_CHRIST = {
  "1": {
    "1": "<p>A theme: 'exiles scattered throughout' — the diaspora-sojourner identity is the Christological frame for the entire letter. Believers are exiles because their true homeland is the kingdom Christ inaugurated; they are 'chosen' (<em>eklektois</em>) because election in Christ precedes and governs their temporal displacement. The community's alien status is not a misfortune but a Christological vocation: as Christ was rejected by the world and by the religious establishment (2:4), those who belong to him share his outsider status.</p>",

    "2": "<p>A direct revelation: 'through the sanctifying work of the Spirit, for obedience to Jesus Christ and sprinkling by his blood.' The Trinitarian framework of salvation (foreknowledge of the Father, sanctifying Spirit, blood of Christ) maps the entire saving event onto its threefold divine source. 'Sprinkling by his blood' (<em>rhantismon haimatos</em>) invokes the covenant-ratification ceremony of Exod 24:6-8 (Moses sprinkled the blood on the people to seal the covenant) and the Levitical purification rites of Num 19 — Christ's blood ratifies and enacts the new covenant.</p>",

    "3": "<p>A direct revelation: 'In his great mercy he has given us new birth into a living hope through the resurrection of Jesus Christ from the dead.' The living hope is grounded entirely in the resurrection — a hope that lives because the Resurrected One lives. The new birth (<em>anagennēsas</em>) is the Christological re-creation: as Christ passed through death and emerged in resurrection life, those united to him are born from above into that same resurrection order. The entire soteriological vocabulary (new birth, living hope, resurrection) converges on the risen Christ as both the basis and the content of Christian hope.</p>",

    "4": "<p>A direct revelation: 'an inheritance that can never perish, spoil, or fade — kept in heaven for you.' The three alpha-privatives (<em>aphtharton, amianton, amaranton</em> — imperishable, unstained, unfading) define the inheritance by contrast with every earthly inheritance. The inheritance is Christ himself and participation in his kingdom: Paul equates 'heirs of God and co-heirs with Christ' (Rom 8:17), and Rev 21:3-7 describes the inheritance as God dwelling with his people. The heaven-kept inheritance is the state into which the risen and glorified Christ has already entered as the firstfruits.</p>",

    "5": "<p>A theme: believers 'shielded by God's power through faith for the salvation ready to be revealed.' The salvation that is coming is the fullness of what Christ's resurrection has already secured — the final unveiling of what was inaugurated at the resurrection. The divine shielding (<em>phrouroumenous</em>, guarded like a military garrison) is exercised through Christ's intercession and the Spirit's sealing. The 'last time' (<em>eschatō kairō</em>) is the parousia of Christ when the hidden inheritance becomes manifest.</p>",

    "6": "<p>A theme: 'you rejoice, though now for a little while you may have had to suffer grief in all kinds of trials.' The pattern of joy-through-suffering is the Christological pattern: Christ 'for the joy set before him endured the cross' (Heb 12:2). The community's capacity to rejoice amid suffering (<em>agalliasthe</em>) is a participation in Christ's own eschatological orientation — the present suffering is interpreted through the frame of the coming revelation. 'A little while' places the trial in eschatological proportion: the eternal weight of glory makes the momentary affliction relativized.</p>",

    "7": "<p>A direct revelation: 'when Jesus Christ is revealed.' The testing of faith — like gold refined by fire — is oriented toward the moment of Christ's appearing (<em>apokalypsei Iēsou Christou</em>). The proven genuineness of faith results in 'praise, glory, and honor at the revelation of Jesus Christ' — the community's tested faith will be the occasion of glory-worship when Christ appears. The refiner's fire of Mal 3:2-3, which tested Israel for purification, is applied to the community's suffering as the crucible that prepares them for the glorious unveiling.</p>",

    "8": "<p>A direct revelation: 'Though you have not seen him, you love him; and even though you do not see him now, you believe in him and are filled with an inexpressible and glorious joy.' The faith that loves the unseen Christ is the distinctive mark of the post-resurrection community: Thomas needed to see (John 20:27-29), but Jesus pronounced a beatitude on those who believe without seeing. The 'inexpressible and glorious joy' (<em>chara aneklalētō kai dedoxasmenē</em>) is the eschatological joy of the Kingdom already tasted in the present — the joy of those who are receiving the end of their faith (v. 9).</p>",

    "9": "<p>A direct revelation: 'for you are receiving the end result of your faith, the salvation of your souls.' 'Receiving' (<em>komizomenoi</em>, present participle) indicates a salvation already being received in the present, not merely awaited. The 'salvation of souls' is not the rescue of a disembodied spirit but the comprehensive rescue of the person — the same word (<em>psychē</em>) that Jesus uses in Mark 8:35 ('whoever loses their life for my sake will save it'). The salvation that Christ secured by his death and resurrection is already flowing to those who believe.</p>",

    "10": "<p>A direct revelation: 'the prophets... spoke of the grace that was to come to you, searched intently and with the greatest care.' The prophets searched (<em>exēzētēsan kai exēreunēsan</em>) for the salvation they announced but did not experience — their ministry was in service of a future they could not fully see. The grace they searched for is the grace that has appeared in Christ (Titus 2:11). The entire prophetic tradition is Christologically oriented: the prophets were unknowingly writing about the Messiah and the sufferings and glories that would follow.</p>",

    "11": "<p>A direct revelation: 'the Spirit of Christ in them was pointing when he predicted the sufferings of Christ and the glories that would follow.' The 'Spirit of Christ' (<em>to tou Christou pneuma</em>) — the Spirit who inspired the prophets is explicitly identified as the Spirit of Christ, making Christ the divine author of the OT prophetic witness. The prophetic pattern — sufferings then glory — is the exact structure of the paschal mystery: cross then resurrection, humiliation then exaltation (Phil 2:8-9; Luke 24:26: 'Did not the Christ have to suffer these things and then enter his glory?').</p>",

    "12": "<p>A direct revelation: 'things into which angels long to look.' The gospel proclaimed about Christ's sufferings and glory is so transcendent that the angelic order — who witnessed creation and attend the divine throne — desire to understand it. The Christological mystery of the Incarnation, cross, and resurrection exceeded the angels' own experience (1 Cor 2:8; Eph 3:10: 'through the church, the manifold wisdom of God should be made known to the rulers and authorities in the heavenly realms'). The gospel is the supreme disclosure of divine wisdom.</p>",

    "13": "<p>A direct revelation: 'set your hope fully on the grace to be brought to you when Jesus Christ is revealed.' The ethical imperative (sober minds, alert hope) flows from the Christological horizon: the grace that is coming is the final manifestation of what Christ secured. 'When Jesus Christ is revealed' (<em>en apokalypsei Iēsou Christou</em>) is the eschatological frame for all present conduct — moral formation is shaped by the coming revelation. The hope is not generic future optimism but specific trust in the returning Christ whose grace will arrive with him.</p>",

    "14": "<p>A theme: 'As obedient children, do not conform to the evil desires you had when you lived in ignorance.' The new identity as 'obedient children' is the Christological identity — Christ as the obedient Son (Phil 2:8: 'obedient to death') defines the pattern of filial obedience. The former ignorance (<em>agnoian</em>) is the pre-Christ condition (Acts 17:30: 'in the past God overlooked such ignorance'); the new obedience is the condition of those who have been illuminated by the gospel. The transformation from ignorance-driven desire to Spirit-led obedience is the mark of Christ's new creation.</p>",

    "15": "<p>A revelation of God: 'But just as he who called you is holy, so be holy in all you do.' The holy God who calls is the Father of Jesus Christ — the one whose holiness Peter has grounded in the Christological redemption of vv. 18-20. The holiness-imperative of Leviticus (quoted in v. 16) is re-issued in the new covenant through the mediation of Christ: those ransomed by the blood of the holy Lamb (v. 19) are called to embody the holiness of the one who ransomed them. The sanctification that Christ's blood inaugurates (Heb 10:10) creates the capacity for the holiness-obedience the verse commands.</p>",

    "16": "<p>A revelation of God: 'Be holy, because I am holy' (Lev 11:44, 19:2). The Levitical holiness-command quoted by Peter is re-issued in the context of the new covenant community — the same divine imperative applied to a new covenant people ransomed by Christ's blood. The Christological transformation: in Leviticus the holiness-standard was maintained by purity laws and sacrificial rituals; in 1 Peter the same standard is pursued by those who have been permanently cleansed by 'the precious blood of Christ' (v. 19), enabling an internalized holiness rather than a merely ritual one.</p>",

    "17": "<p>A revelation of God: 'a Father who judges each person's work impartially.' The Father who judges is also the Father of Jesus Christ (v. 3) — making the judgment not an abstract divine tribunal but the eschatological accounting before the Father who sent the Son. The fear (<em>phobō</em>) with which the community conducts its exile-life is not craven terror but the reverent awe appropriate to those who know that the Father's judgment is real and impartial. Christ's own warnings about judgment (Matt 7:21-23; 25:31-46) ground the Father's impartiality in the specific accountability of discipleship.</p>",

    "18": "<p>A direct revelation: 'You were ransomed from the futile ways inherited from your forefathers, not with perishable things such as silver or gold, but with the precious blood of Christ, like that of a lamb without blemish or spot.' The ransom-price Christology: Christ's blood is the currency of redemption from inherited futility. The Passover-lamb imagery connects the death of Christ to the entire Exodus-redemption narrative — as the Passover blood protected Israel from the destroying angel, Christ's blood ransoms believers from the bondage of empty ancestral religion. The lamb is not merely a metaphor for innocence but a liturgical category that places the cross within the sacrificial system's culmination.</p>",

    "19": "<p>A direct revelation: 'the precious blood of Christ, a lamb without blemish or defect.' The blood of the unblemished lamb is the cultic language of Exod 12:5 (the Passover lamb must be without defect) and Lev 22:19-25 (sacrificial animals must be without blemish). Christ fulfills both requirements: the Passover typology (liberation from death-judgment) and the Levitical typology (acceptable sacrifice for atonement). John the Baptist's identification of Jesus as 'the Lamb of God who takes away the sin of the world' (John 1:29) is here applied to the ransom-price of redemption.</p>",

    "20": "<p>A direct revelation: 'He was chosen before the creation of the world, but was revealed in these last times for your sake.' The pre-temporal election of Christ (<em>proegnōsmenou pro katabolēs kosmou</em>) grounds his saving work in the eternal counsel of God — the Incarnation was not a contingency plan but the execution of a pre-creation decision. 'Revealed in these last times' (<em>phanerōthentos ep' eschatou tōn chronōn</em>) places the Incarnation at the eschatological center of history: Christ's appearing inaugurates the last age. The community addressed is living in the decisive era for which Christ was always destined.</p>",

    "21": "<p>A direct revelation: 'Through him you believe in God, who raised him from the dead and glorified him, and so your faith and hope are in God.' Christ is the mediator of faith in God — faith is not directed at God in general but at the God who specifically raised Jesus from the dead and glorified him. The resurrection-and-glorification formula (raised + glorified) is the standard early Christian summary of the paschal event (Acts 3:13-15; Phil 2:9-11). Faith and hope that are not grounded in the resurrection are not distinctively Christian; the resurrection is the specific object-event that makes faith rationally and theologically coherent.</p>",

    "22": "<p>A theme: 'you have purified yourselves by obeying the truth so that you have sincere love for each other.' The purification through truth-obedience is the fruit of the gospel's reception — the same cleansing that Peter attributed to Christ's blood (v. 19) now produces the ethical transformation of sincere love. The Christological trajectory: 'a new command I give you: love one another. As I have loved you, so you must love one another' (John 13:34). The community's love is the fruit of a purification that Christ's work makes possible.</p>",

    "23": "<p>A direct revelation: 'For you have been born again, not of perishable seed, but of imperishable, through the living and enduring word of God.' The living and enduring word of God (<em>logos theou</em>) is, in John's Gospel, the incarnate Christ himself (John 1:1, 14). Peter uses the same term for the gospel-proclamation (v. 25: 'the word that was preached to you'), which is the word about Christ. The new birth (already introduced in v. 3 as resurrection-mediated) is now described as seed-germination — the imperishable seed of the gospel word producing imperishable life.</p>",

    "24": "<p>A fulfillment: Isaiah 40:6-8 quoted as the backdrop for the contrast between perishable human existence and the enduring word of God. The Christological trajectory: in John 1:14 'the Word became flesh' — the divine word that endures forever took on the very flesh that withers like grass. The enduring word of God that Peter cites as the seed of new birth is thus the Christ who became mortal, died, and rose — the word that endures even through death. The dried-up grass of human mortality is the condition that Christ assumed and overcame through resurrection.</p>",

    "25": "<p>A direct revelation: 'the word of the Lord endures forever' (Isa 40:8). 'And this is the word that was preached to you' — the gospel-proclamation is identified as the enduring word of YHWH from Isa 40. The Christological identification: the word (<em>rhēma Kyriou</em>) that endures is the word about Jesus Christ, and in Johannine theology Christ is the Word himself. The seed of new birth (v. 23), the enduring divine word (v. 25), and the gospel proclamation are all one: Jesus Christ proclaimed as the risen Lord.</p>"
  },

  "2": {
    "1": "<p>A theme: 'rid yourselves of all malice and all deceit, hypocrisy, envy, and slander.' The list of vices to be stripped off is the wardrobe of the old self — the garment-exchange image (cf. Col 3:8-10: 'take off... put on'). The Christological ground: those who have been born again (1:23) through the imperishable word and purified by truth (1:22) are called to embody the character of Christ, in whom 'no deceit was found' (v. 22, Isa 53:9). The vices listed are the specific negation of Christ's character: where he was honest, non-deceitful, and non-slanderous, his community must be the same.</p>",

    "2": "<p>A direct revelation: 'crave pure spiritual milk, so that by it you may grow up in your salvation.' 'Pure spiritual milk' (<em>to logikon adolon gala</em>) — <em>logikon</em> (of the word/rational/spiritual) associates the milk with the <em>logos</em> of 1:23-25: the word-of-God that is the seed of new birth is also the nourishment for growth. The Christological connection: Jesus himself is the living bread (John 6:35), the living water (John 4:10), and through 1:25 the word-seed — growth in salvation is growth in knowledge of and union with Christ.</p>",

    "3": "<p>A direct revelation: 'now that you have tasted that the Lord is good.' The quotation of Ps 34:8 ('taste and see that the LORD is good') applied to Christ — the Lord whose goodness the community has 'tasted' is Jesus Christ. The taste-metaphor is experiential: the community has had a direct experience of Christ's goodness through the gospel. The Psalm of David that becomes a Christological testimony: the LORD who proved good to the persecuted psalmist is identified with the Christ whose mercy and grace the new-birth community has received.</p>",

    "4": "<p>A direct revelation: 'As you come to him, the living Stone — rejected by humans but chosen by God and precious to him.' Christ as the living Stone who is simultaneously rejected and chosen — the paradox of the cross and resurrection in architectural metaphor. The 'living stone' places Christ's death and resurrection in one phrase: stones are dead, but this one lives. The rejection by humans (<em>hypo anthrōpōn men apodedokimasmenon</em>) is the passion; the choice by God (<em>para de theō eklekton entimion</em>) is the resurrection-vindication. The cornerstone of Isa 28:16 and the rejected cornerstone of Ps 118:22 meet in the one person.</p>",

    "5": "<p>A direct revelation: 'you also, like living stones, are being built into a spiritual house to be a holy priesthood, offering spiritual sacrifices acceptable to God through Jesus Christ.' The community's identity is participatory: they are 'living stones' because they are united to the living Stone. The spiritual house is the new temple — the community of Christ-followers replacing the Jerusalem temple as the locus of divine presence (cf. John 2:21: 'the temple he had spoken of was his body'). Their 'spiritual sacrifices' offered through Christ are the praise, prayer, and whole-life service that replace the Levitical cult.</p>",

    "6": "<p>A fulfillment: Isa 28:16 (chosen cornerstone) applied to Christ. The stone that God lays in Zion is the Messiah — Peter's citation completes the Isaianic trajectory: the foundation promised to Zion has been laid in the person of Christ crucified and raised. 'Whoever believes in him will never be put to shame' — the promise of vindication attaches to those who trust the same stone that was apparently shamefully rejected on the cross but then vindicated in resurrection. Faith in the rejected-but-vindicated cornerstone is the path to eschatological security.</p>",

    "7": "<p>A direct revelation: 'The stone the builders rejected has become the cornerstone' (Ps 118:22). The builders who rejected the stone are the religious leadership of Israel (Acts 4:11: Peter applies this text directly to the chief priests and teachers after healing the lame man in Jesus's name). The Christological irony: the stone that looked most disqualified — the crucified Jesus — became the structurally central member of the new temple. The resurrection is the divine reversal that transforms rejection into cornerstone-status.</p>",

    "8": "<p>A fulfillment: Isa 8:14 (stone of stumbling). The same stone that is cornerstone to believers is a stone of offense to unbelievers — Christ is either foundation or stumbling-block, never neutral. The Christological significance: unbelief is not merely a failure of cognition but a structural collision — the unbeliever trips over the very one who would otherwise support them. 'They stumble because they disobey the message — which is also what they were destined for' (v. 8b) — the Christological stumbling-block is the eschatological divide between those being saved and those perishing (1 Cor 1:18).</p>",

    "9": "<p>A direct revelation: 'But you are a chosen people, a royal priesthood, a holy nation, God's special possession, that you may declare the praises of him who called you out of darkness into his wonderful light.' The four Sinai-covenant identity markers (Exod 19:5-6; Isa 43:20-21) are applied to the community of Christ-followers — they are the new Israel constituted by Christ's mediation. 'Called out of darkness into his wonderful light' is the language of the new Exodus: as Israel was called out of Egypt's darkness by the Passover, the church is called out of spiritual darkness by the blood of the Passover Lamb (1:18-19).</p>",

    "10": "<p>A fulfillment: Hos 1:9-10; 2:23 — 'once you were not a people... but now you are the people of God.' Hosea's prophecy of Israel's restoration (a people declared 'not my people' called back to covenant status) is applied to the Gentile believers who were outside Israel's covenant but are now incorporated into the new covenant community through Christ. The Christological mediation: the 'not-my-people' become God's people through the blood of Christ that established the new covenant (Matt 26:28: 'my blood of the covenant, which is poured out for many for the forgiveness of sins').</p>",

    "11": "<p>A theme: 'as foreigners and exiles, to abstain from sinful desires.' The alien-sojourner identity (grounded in the Christological framework of 1:1) governs the community's ethical posture toward the world. The sinful desires that war against the soul are the desires of the old age from which Christ ransomed them (1:18); the Christological liberation creates both the new identity (aliens in the present age) and the new vocation (abstaining from the old desires). The community's foreignness is the social form of their eschatological citizenship in Christ's coming kingdom.</p>",

    "12": "<p>A theme: 'Live such good lives among the pagans that, though they accuse you of doing wrong, they may see your good deeds and glorify God on the day he visits us.' The day of divine visitation (<em>hēmera episkopēs</em>) is the day of Christ's parousia — the day when those who observed the community's good works will themselves give glory to God, having been drawn toward faith by what they witnessed. The community's ethical life is a form of pre-evangelism, oriented toward the eschatological judgment when the watching pagans' response to what they observed will be assessed.</p>",

    "13": "<p>A theme: 'Submit yourselves for the Lord's sake to every human authority.' The submission is 'for the Lord's sake' (<em>dia ton Kyrion</em>) — the motive is Christological. Christ himself submitted to Roman authority at his trial (John 19:11: 'you would have no authority over me if it were not given to you from above') and to Roman execution. The community's civic submission is an imitation of Christ's own posture toward the governing structures of his day. The theme of suffering under unjust authority (vv. 18-25) will soon apply the Christ-pattern directly.</p>",

    "14": "<p>A theme: 'to governors, who are sent by him to punish those who do wrong and to commend those who do right.' The providential ordering of civil authority (as in Rom 13:1-7) is the background for the community's civic engagement. The Christological frame: Christ who submitted to Pilate's authority (which Pilate held only by divine permission) is the model for the community's submission to the providential structures of the present age — not because the structures are just, but because God is working his purposes through them even when they are used against Christ's followers.</p>",

    "15": "<p>A theme: 'For it is God's will that by doing good you should silence the ignorant talk of foolish people.' The apologetic function of good works — silencing accusation through conduct rather than argument. The Christological parallel: Christ silenced his accusers not by rebuttal but by the transparent goodness of his life (v. 22: 'no sin... no deceit'). The community's good works extend the pattern of Christ's sinless life into the social testimony of the persecuted community, making the accusation of wrong-doing untenable to any fair-minded observer.</p>",

    "16": "<p>A theme: 'Live as free people, but do not use your freedom as a cover-up for evil; live as God's slaves.' The freedom and slavery paradox — freedom from sin, slavery to God — mirrors Paul's language (Rom 6:18-22: freed from sin, enslaved to righteousness). The Christological ground: Christ himself took the form of a slave (<em>morphēn doulou</em>, Phil 2:7), voluntarily entering the condition of service that defines the community's freedom-in-slavery. True freedom is not absence of obligation but proper relationship — the community freed by Christ's blood now serves the God who ransomed them.</p>",

    "17": "<p>A theme: 'Show proper respect to everyone, love the family of believers, fear God, honor the emperor.' The four-fold relational map — universal respect, community love, God-fear, emperor-honor — places the emperor in the fourth position. The Christological priority: God-fear comes before emperor-honor; the community whose allegiance belongs first to the Lord Jesus Christ (3:15: 'set apart Christ as Lord') cannot give the emperor the god-status he claimed. The letter was written under Nero — the very ruler who would execute Peter — making the qualified civic honor a witness under pressure.</p>",

    "18": "<p>A theme: 'Submit yourselves to your masters with all respect, not only to those who are good and considerate, but also to those who are harsh.' The ethics of submission under unjust authority begins the Christological section of ch. 2 (vv. 18-25) that will apply the Servant of Isaiah 53 to Christ as the model for unjust suffering. The enslaved person who bears unjust suffering consciously (<em>dia syneidesin theou</em>, because of consciousness of God) is already walking in the pattern of Christ's passion — not accidentally, but as a participation in the form Christ's own suffering took.</p>",

    "19": "<p>A theme: 'For it is commendable if someone bears up under the pain of unjust suffering because they are conscious of God.' The commendable suffering is suffering that follows Christ's own pattern (v. 21: 'Christ suffered for you, leaving you an example'). The consciousness of God (<em>syneidesin theou</em>) that makes unjust suffering bearable is the Christological consciousness — the awareness that the Father who did not spare his Son from unjust suffering is working through this suffering too (Rom 8:28-32). The cross is the paradigm that makes sense of all unjust suffering.</p>",

    "20": "<p>A theme: 'But how is it to your credit if you receive a beating for doing wrong and endure it? But if you suffer for doing good and you endure it, this is commendable before God.' The distinction between deserved and undeserved suffering is the Christological distinction: Christ suffered for doing good, not for doing wrong (v. 22: 'he committed no sin'). The community's undeserved suffering is the form that Christological suffering takes in their social location — it mirrors the innocent suffering of the Servant. Deserved suffering has no redemptive significance; undeserved suffering in Christ's pattern participates in the cross.</p>",

    "21": "<p>A direct revelation: 'To this you were called, because Christ suffered for you, leaving you an example, that you should follow in his steps.' The community's suffering-vocation is grounded in Christ's suffering — their call is not merely to believe in Christ but to follow in his suffering footsteps. <em>Hypogrammon</em> (example, copybook letters to trace) — the image of the child's writing lesson: the teacher writes the letters for the student to trace. Christ's passion is the script; the community's suffering-life traces over it. The solidarity between Christ's suffering and the believer's suffering is not incidental but constitutive of Christian identity.</p>",

    "22": "<p>A fulfillment: 'He committed no sin, and no deceit was found in his mouth' (Isa 53:9). Peter applies the Servant's innocence directly to Jesus — the Servant who suffered despite sinlessness is identified with the crucified and risen Christ. The innocence of Christ is the foundation of his substitutionary suffering: only the sinless one can bear another's sin (v. 24). This verse is the beginning of Peter's sustained Isa 53 application (vv. 22-25) — the most extended NT passage explicitly applying the Servant Song to Christ's passion.</p>",

    "23": "<p>A fulfillment: 'When they hurled their insults at him, he did not retaliate' (Isa 53:7). The Servant's non-retaliating suffering is applied to Christ's conduct during the passion — the silence before Pilate and Herod (Matt 26:63; 27:12-14), the refusal to call down angelic rescue (Matt 26:53). 'He entrusted himself to him who judges justly' — in the face of unjust human judgment, Christ's recourse was the Father's just judgment, not self-defense. This entrusting pattern is the model for the community's response to unjust suffering (v. 23 grounds the imperative of v. 19-21).</p>",

    "24": "<p>A fulfillment: 'He himself bore our sins in his body on the tree, that we might die to sin and live to righteousness. By his wounds you have been healed.' 1 Peter 2:22-25 is the most sustained application of Isa 53 to the passion in the NT outside the Gospel traditions. Peter works through the Servant Song verse by verse: v. 22 (Isa 53:9: no sin in his mouth), v. 23 (Isa 53:7: did not retaliate), v. 24 (Isa 53:4-5: bore our griefs, wounded for our iniquities, by his stripes we are healed), v. 25 (Isa 53:6: we all went astray like sheep). The suffering community is invited to understand their own suffering through the Servant-Christ who bore sins and called them to follow his pattern.</p>",

    "25": "<p>A fulfillment: 'For you were like sheep going astray' (Isa 53:6). The scattering sheep of Isaiah's Servant Song becomes the community's own pre-conversion condition — they were the wandering flock before they 'returned to the Shepherd and Overseer of your souls.' Christ as Shepherd (<em>poimēn</em>) and Overseer (<em>episkopon</em>) of souls completes the Servant identification with a pastoral one: the Servant who bore the iniquity of all the wandering sheep (Isa 53:6) is also the Shepherd who brings them back. The church's elders (5:1-4) are sub-shepherds under this Chief Shepherd.</p>"
  },

  "3": {
    "1": "<p>A theme: 'Wives, in the same way submit yourselves to your own husbands so that, if any of them do not believe the word, they may be won over without words by the behavior of their wives.' The 'in the same way' connects wives' submission to Christ's own submission under unjust authority (2:21-25) — the household code is framed by the Christological pattern of suffering-submission. The witness-by-conduct strategy (winning without words) is the domestic form of the community's broader apologetic (2:12: 'good deeds... seen by the pagans') — the Christological transformation of character visible in daily household life.</p>",

    "2": "<p>A theme: 'when they see the purity and reverence of your lives.' The purity (<em>hagnēn</em>) and reverence (<em>phobon</em>) of the wife's life are the Christological virtues visible in the household: the same purity Christ demonstrated (2:22) and the reverence toward God that characterizes the community's conduct (1:17; 2:17). The watching husband who observes these qualities is being evangelized by the enacted gospel — character bearing witness where words cannot reach.</p>",

    "3": "<p>A theme: inner versus outer adornment — the beauty that comes from the Spirit rather than external ornamentation. The Christological ground: Christ 'had no beauty or majesty to attract us to him' (Isa 53:2) — the Servant's glory was internal and spiritual, not externally impressive. The 'gentle and quiet spirit' (v. 4) is the spirit of the one who was 'meek and humble in heart' (Matt 11:29), whose external ordinariness concealed the glory of the incarnate Son. The community that values inner over outer beauty is formed in the pattern of the incarnate Christ.</p>",

    "4": "<p>A revelation of God: 'the unfading beauty of a gentle and quiet spirit, which is of great worth in God's sight.' <em>Apranthon</em> (unfading) — the same word used for the crown of unfading glory in 5:4 (<em>amarantinon</em>) and the imperishable inheritance in 1:4 (<em>aphtharton</em>). The inner beauty that does not fade is the beauty that God values — and it is the beauty that is being conformed to Christ's image by the Spirit (2 Cor 3:18: 'being transformed into his image with ever-increasing glory'). The Spirit's formation of Christlike character is the unfading adornment.</p>",

    "5": "<p>A type: 'the holy women of the past who put their hope in God used to adorn themselves.' The matriarchs of Israel as types of the community's inner-beauty ethic — their hope in God produced the character that defined true feminine honor in the covenant tradition. The Christological trajectory: the hope that these holy women had (in God's promised redemption) has been fulfilled in Christ; the community now places its hope in the same God who has definitively revealed his faithfulness through the resurrection (1:21: 'your faith and hope are in God').</p>",

    "6": "<p>A type: 'like Sarah, who obeyed Abraham and called him her lord.' Sarah as a type of the community's faithful trust in God's promises — her obedience to Abraham was rooted in her faith in the God who had made covenant promises to them (Gen 18:10-14). The Christological trajectory: as Sarah trusted God's word about the impossible birth of Isaac (the son of promise who became a type of Christ), the community trusts God's word about the resurrection of Christ — both are trusting the God who gives life to the dead (4:5; cf. Rom 4:19-25).</p>",

    "7": "<p>A theme: 'Husbands, in the same way be considerate as you live with your wives, and treat them with respect as the weaker partner and as heirs together with the grace of life.' 'Heirs together' (<em>synklēronomois</em>) — the women are co-heirs of the grace of life alongside their husbands. The Christological ground: Christ's redemption makes women equally heirs with men (Gal 3:28: 'neither... male and female, for you are all one in Christ Jesus'). The husband's consideration is grounded in Christ's equal treatment of women — he spoke to the Samaritan woman, honored Mary of Bethany, first appeared to women at the resurrection.</p>",

    "8": "<p>A theme: 'be like-minded, be sympathetic, love one another, be compassionate and humble.' The five community-virtues map onto Christ's own character: like-minded in sharing Christ's eschatological orientation; sympathetic as he was moved with compassion (Matt 9:36); loving one another as he loved (John 13:34); compassionate as he wept at Lazarus's tomb (John 11:35); humble as the one who took the form of a servant (Phil 2:7). The community ethics is the Christological character distributed across all community members.</p>",

    "9": "<p>A theme: 'Do not repay evil with evil or insult with insult. On the contrary, repay evil with blessing.' The non-retaliation ethic returns to the Christological pattern of 2:23 ('when they hurled their insults at him, he did not retaliate'). The blessing-for-insult response is Christ's own teaching (Matt 5:44: 'bless those who curse you') applied to the community's daily relational practice. 'Because to this you were called so that you may inherit a blessing' — the community's suffering-under-insult is the path to eschatological blessing, as Christ's non-retaliating suffering was the path to resurrection-glory.</p>",

    "10": "<p>A fulfillment: Ps 34:12-16 quoted — 'whoever would love life and see good days must keep their tongue from evil.' The Psalmist's covenant-wisdom about the righteous life takes on Christological significance in context: the 'good days' are the eschatological days of salvation that Christ has inaugurated; the tongue-restraint is the imitation of Christ who 'committed no sin and no deceit was found in his mouth' (2:22). The Psalm of David applied to the community of Christ-followers as wisdom for how to live between resurrection and parousia.</p>",

    "11": "<p>A theme: 'they must turn from evil and do good; they must seek peace and pursue it.' The peace that the community seeks and pursues is ultimately the peace that Christ has made: 'he himself is our peace' (Eph 2:14). The ethical pursuit of peace is a participation in and embodiment of the peace Christ achieved through the cross — reconciliation with God (Rom 5:1: 'we have peace with God through our Lord Jesus Christ') overflows into reconciliation and peace-seeking in horizontal human relationships.</p>",

    "12": "<p>A revelation of God: 'For the eyes of the Lord are on the righteous and his ears are attentive to their cry.' The Psalmist's assurance that God watches over the righteous becomes, in the NT context, the assurance mediated by Christ: those who are 'righteous' in Christ (2 Cor 5:21) are the objects of the Father's attentive care. The prayer that the righteous cry to the attentive Lord is now offered through Christ (4:7: 'so that you can pray'), whose own prayers were heard (Heb 5:7: 'he was heard because of his reverent submission').</p>",

    "13": "<p>A theme: 'Who is going to harm you if you are eager to do good?' The rhetorical security of the good-works ethic — those who do good have nothing ultimately to fear even in a hostile social environment. The Christological irony: Christ was the one most 'eager to do good' and was harmed fatally — yet death could not ultimately harm him (death held no power over the one who was righteous, Acts 2:24: 'it was impossible for death to keep its hold on him'). The community's security is not immunity from earthly harm but ultimate safety in the risen Christ who overcame the ultimate harm.</p>",

    "14": "<p>A direct revelation: 'But even if you should suffer for what is right, you are blessed.' The beatitude for suffering in the cause of righteousness (Matt 5:10-11: 'blessed are those who are persecuted because of righteousness') is applied here — Christ's Beatitude from the Sermon on the Mount governs the community's experience of persecution. 'Do not fear what they fear' — the community that fears God (1:17; 2:17) does not need to fear human opposition: the Christological reorientation of fear is the practical fruit of setting Christ apart as Lord (v. 15).</p>",

    "15": "<p>A direct revelation: 'But in your hearts revere Christ as Lord.' The Christological foundation of the community's fearlessness: to 'set apart Christ as Lord' (<em>hagiasate de Christon Kyrion</em> — sanctify/consecrate Christ as Lord in your hearts) is the act that displaces the fear of human opposition. The Isa 8:13 text ('the LORD Almighty is the one you are to regard as holy') is applied to Christ — YHWH Sabaoth of Isaiah is identified with the Lord Jesus Christ. Christ's Lordship in the heart is the alternative to fear.</p>",

    "16": "<p>A theme: 'keeping a clear conscience, so that those who speak maliciously against your good behavior in Christ may be ashamed of their slander.' The clean conscience is the Christological conscience — one shaped by Christ's own non-deceitfulness (2:22) and maintained by living transparently before the God who judges impartially (1:17). 'Your good behavior in Christ' (<em>tēn agathēn en Christō anastrophēn</em>) — the good conduct is 'in Christ,' meaning it arises from and is shaped by the Christ-union. The shameful reversal of slanderers echoes the rejected stone's vindication (2:7).</p>",

    "17": "<p>A theme: 'For it is better, if it is God's will, to suffer for doing good than for doing evil.' The Christological framework: Christ's innocent suffering was 'God's will' (Acts 4:28: 'they did what your power and will had decided beforehand should happen'). The community's innocent suffering under God's will participates in the same providential structure — it is not an accident or a sign of divine abandonment but a divinely purposed participation in the paschal mystery. The 'if it is God's will' guards against masochism or needless provocation while affirming that undeserved suffering can be within divine purpose.</p>",

    "18": "<p>A direct revelation: 'Christ also suffered once for sins, the righteous for the unrighteous, to bring you to God. He was put to death in the body but made alive in the Spirit.' The uniqueness and finality of the atonement: <em>hapax</em> (once, for all time) marks the non-repeatability of Christ's sin-bearing death. The substitutionary logic: the righteous (<em>dikaios</em>) for the unrighteous (<em>adikous</em>) — the morally qualified dies for the morally disqualified. The telos: 'to bring you to God' (<em>hina hemas prosagagē tō theō</em>) — access to God is the goal of the cross, not merely forgiveness as a legal transaction. Made alive in the Spirit — the resurrection as the Spirit's vindicating action (Rom 8:11).</p>",

    "19": "<p>A direct revelation: 'he went and made proclamation to the imprisoned spirits.' Christ's proclamation to the imprisoned spirits (debated exegetically: fallen angels from Gen 6? the dead who heard the gospel? the disobedient of Noah's generation?) is a declaration of his victory over the powers. Whether this is the preaching of the gospel or the announcement of defeat (Col 2:15: 'having disarmed the powers and authorities, he made a public spectacle of them, triumphing over them by the cross'), it is Christ's victorious proclamation after resurrection. The risen and triumphant Christ announces his cosmic lordship over imprisoned spiritual powers.</p>",

    "20": "<p>A type: the days of Noah and the flood as the typological backdrop for baptism (v. 21). The eight people saved through water in the ark are a type of the new-covenant community saved through the water of baptism. The patience of God in Noah's time (the long window before the flood) is a type of the divine patience before the final judgment (2 Pet 3:9). The Christological typology: as Noah and his family were saved through the flood-waters while others perished in the same waters, those united to Christ in baptism pass through death-and-resurrection waters into salvation.</p>",

    "21": "<p>A direct revelation: 'this water symbolizes baptism that now saves you also — not the removal of dirt from the body but the pledge of a clear conscience toward God. It saves you by the resurrection of Jesus Christ.' Baptism saves not by the water's physical action but 'by the resurrection of Jesus Christ' — the resurrection is the saving event; baptism is the union with that event. The 'pledge of a clear conscience toward God' (<em>syneidēseōs agathēs eperōtēma</em>) — the believer's appeal to God from within the new-covenant relationship established by Christ's resurrection. Baptism is the rite of incorporation into the resurrected Christ.</p>",

    "22": "<p>A direct revelation: 'who has gone into heaven and is at God's right hand — with angels, authorities and powers in submission to him.' The ascended and enthroned Christ — the exaltation language of Ps 110:1 ('Sit at my right hand until I make your enemies a footstool for your feet') applied to the risen Jesus. The submission of angels, authorities, and powers to Christ is the cosmic scope of the resurrection-victory: not merely individual salvation but the subjugation of the entire spiritual order to the risen Lord. Eph 1:20-23 and Col 2:15 express the same cosmic enthronement.</p>"
  },

  "4": {
    "1": "<p>A direct revelation: 'Therefore, since Christ suffered in his body, arm yourselves also with the same attitude, because whoever suffers in the body is done with sin.' The Christological imitation principle: Christ's bodily suffering is the model and motive for the community's suffering-posture. 'Arm yourselves' (<em>hoplisasthe</em>) with the same mindset — the military metaphor for equipping oneself with Christ's own disposition toward suffering. The connection between bodily suffering and freedom from sin draws on the crucifixion-logic of Rom 6:6-7: the old self crucified with Christ is freed from sin's domination.</p>",

    "2": "<p>A theme: 'As a result, they do not live the rest of their earthly lives for evil human desires, but rather for the will of God.' The Christological reorientation: 'for the will of God' rather than human desires mirrors Christ's own prayer-disposition ('not my will, but yours,' Luke 22:42) and his entire life-orientation ('I have come down from heaven not to do my will but to do the will of him who sent me,' John 6:38). The community's transition from self-will to God-will is a participation in the Son's own voluntary submission to the Father's will.</p>",

    "3": "<p>A theme: the pre-conversion lifestyle catalogued — 'debauchery, lust, drunkenness, orgies, carousing and detestable idolatry.' The former way of life from which Christ ransomed the community (1:18: 'from the futile ways inherited from your forefathers'). The pre-conversion catalogue serves to make visible what the ransom-price of Christ's blood accomplished: liberation from this entire complex of bondage. The 'enough time' judgment signals that the decisive turning has happened — the Christ-event creates a before-and-after in the community's biography.</p>",

    "4": "<p>A theme: 'They are surprised that you do not join them in their reckless, wild living, and they heap abuse on you.' The community's holy difference becomes a social offense — not by aggressive moralizing but simply by living differently. The Christological pattern: Christ's holiness was itself an implicit judgment on the world (John 7:7: 'the world... hates me because I testify that its works are evil'). The community's refusal of the old life is a form of testimony that draws hostile response — the same dynamic that Christ's presence created in the world.</p>",

    "5": "<p>A direct revelation: 'But they will have to give account to him who is ready to judge the living and the dead.' Christ as judge of the living and the dead — this is one of the earliest and most universal early Christian creedal affirmations (Acts 10:42: 'he is the one whom God appointed as judge of the living and the dead'; 2 Tim 4:1: 'Christ Jesus, who will judge the living and the dead'; Acts 17:31). The 'him who is ready to judge' is Christ, whose readiness (present tense) signals imminent accountability. The community's restraint in the face of abuse is sustained by the certainty of eschatological justice.</p>",

    "6": "<p>A direct revelation: 'For this is the reason the gospel was preached even to those who are now dead, so that they might be judged according to human standards in regard to the body, but live according to God in regard to the spirit.' The gospel preached to those now dead — whether this refers to the community members who have died since conversion or to a more cosmic gospel-proclamation — the point is that Christ's saving work is not nullified by death. 'Live according to God in regard to the spirit' — the resurrection life of Christ is available to those who received the gospel even though they have died, vindicating the gospel's power over death.</p>",

    "7": "<p>A direct revelation: 'The end of all things is near.' The eschatological horizon — identical to James 5:8 ('the coming of the Lord is near') and Phil 4:5 ('the Lord is near') — shapes all ethical instruction in the letter. The nearness is the nearness of the parousia of Christ; the community lives in the compressed time between resurrection and return. 'Be alert and of sober mind so that you may pray' — the prayer-life of the community is governed by eschatological urgency, and the eschatological urgency is the nearness of Christ's coming.</p>",

    "8": "<p>A theme: 'love each other deeply, because love covers over a multitude of sins.' The citation of Prov 10:12 ('love covers all offenses') applied to the community's eschatological love ethic. The Christological ground: Christ's love covers the community's sins — his atonement is the supreme love-that-covers (Rom 5:8: 'God demonstrates his own love for us in this: while we were still sinners, Christ died for us'). The community's love for one another is the social refraction of Christ's atoning love, creating an analogous structure of forgiveness-through-love in human relationships.</p>",

    "9": "<p>A theme: 'Offer hospitality to one another without grumbling.' Hospitality (<em>philoxenoi</em>, love of strangers) was the practical mechanism of early Christian mission — traveling apostles and missionaries depended on the hospitality of local households. The Christological ground: Christ himself was homeless ('the Son of Man has no place to lay his head,' Matt 8:20) and depends on the hospitality of his people; welcoming the traveling stranger in Christ's name is welcoming Christ himself (Matt 25:35-40: 'I was a stranger and you invited me in').</p>",

    "10": "<p>A theme: 'Each of you should use whatever gift you have received to serve others, as faithful stewards of God's grace in its various forms.' The spiritual gifts as stewardship of divine grace — the gifts are not personal achievements but allocated resources of 'God's grace in its various forms' (<em>poikilēs charitos theou</em>). The Christological ground: the varied gifts are the distributed gifts of the ascended Christ (Eph 4:7-11: 'to each one of us grace has been given as Christ apportioned it... he ascended on high and gave gifts to his people'). The community's gift-life is Christ's ongoing ministry through his body.</p>",

    "11": "<p>A direct revelation: 'If anyone speaks, they should do so as one who speaks the very words of God... so that in all things God may be praised through Jesus Christ.' The doxological conclusion — 'through Jesus Christ' — makes Christ the mediator of all praise that reaches God. The community's speech (as oracles of God) and service (with God-given strength) are both offered through Christ, whose mediation ensures that even the community's gifts are presented to the Father through the Son. 'To him be the glory and the power for ever and ever' — the doxology closes the exhortation by grounding all service in Christ's own receiving of glory.</p>",

    "12": "<p>A theme: 'do not be surprised at the fiery ordeal that has come on you to test you, as though something strange were happening to you.' The fiery ordeal — possible reference to Nero's persecutions in which Christians were burned alive — is placed in the Christological framework of participation in Christ's sufferings (v. 13). 'As though something strange were happening' — the Christological theology of suffering makes the ordeal expected rather than strange: Christ warned his disciples that the world would hate them (John 15:18-20), so persecution is the expected experience of those who follow the crucified Lord.</p>",

    "13": "<p>A direct revelation: 'But rejoice inasmuch as you participate in the sufferings of Christ, so that you may be overjoyed when his glory is revealed.' The participatory suffering-and-glory structure: present participation in Christ's sufferings → future participation in his revealed glory. The joy that is possible in suffering is the anticipatory joy of the glory that is coming with Christ's revelation. Rom 8:17 states the same principle: 'co-heirs with Christ, if indeed we share in his sufferings in order that we may also share in his glory.' The community's suffering is not merely analogous to Christ's but participatory in it — a sharing of the same cosmic drama.</p>",

    "14": "<p>A direct revelation: 'If you are insulted because of the name of Christ, you are blessed, for the Spirit of glory and of God rests on you.' The beatitude for Christ-name insults mirrors Matt 5:11-12 directly ('blessed are you when people insult you... because of me'). The Spirit of glory (<em>to tēs doxēs... pneuma</em>) rests on those who are insulted — the same Spirit who glorified Christ in the resurrection now pre-glorifies the suffering community. The insult 'because of the name of Christ' is the specific marker that distinguishes redemptive from deserved suffering (v. 15-16).</p>",

    "15": "<p>A theme: 'If you suffer, it should not be as a murderer or thief or any other kind of criminal.' The negative boundary of redemptive suffering — only undeserved suffering participates in the Christological pattern. Christ who committed no sin (2:22) models suffering that is wholly innocent; suffering caused by genuine wrongdoing has no Christological significance. The community's suffering must be 'for doing good' (3:17) or 'because of the name of Christ' (v. 14) to carry Christological weight. The distinction matters because the letter's entire theology of suffering depends on the suffering being innocent.</p>",

    "16": "<p>A direct revelation: 'However, if you suffer as a Christian, do not be ashamed, but praise God that you bear that name.' The name 'Christian' (<em>Christianos</em>) — bearing the name of Christ as an identification — was itself the ground for Roman legal proceedings against the early church (the so-called <em>nomen ipsum</em> question: was the name itself a crime?). To 'praise God that you bear that name' is to recognize that the shame of being identified with the crucified Christ is, in the reversal that characterizes the entire letter, actually an honor: sharing the name of the rejected stone who became cornerstone (2:7).</p>",

    "17": "<p>A theme: 'For it is time for judgment to begin with God's household; and if it begins with us, what will the outcome be for those who do not obey the gospel of God?' The eschatological judgment beginning with God's household echoes Ezek 9:6 (judgment beginning at the temple sanctuary) and Amos 3:2 (YHWH's special judgment of those who know him). The Christological frame: Christ is the judge (v. 5) and his household is being refined by fiery trial (v. 12) before the final accountability. The community under the refiner's fire now stands before the final judgment that will come upon all.</p>",

    "18": "<p>A theme: 'If it is hard for the righteous to be saved, what will become of the ungodly and the sinner?' (Prov 11:31 LXX). The difficulty of salvation for the righteous is not because Christ's work is insufficient but because the path of conformity to Christ (through suffering, self-denial, and perseverance) is demanding. The Christological logic: the one who was righteous had to suffer and die before entering glory (Luke 24:26: 'Did not the Christ have to suffer these things and then enter his glory?'). If the righteous Messiah himself went through suffering to glory, the community that follows him will find the same demanding but salvific path.</p>",

    "19": "<p>A theme: 'those who suffer according to God's will should commit themselves to their faithful Creator and continue to do good.' The final verse of the chapter grounds patient suffering in Christological trust: 'commit themselves' (<em>paratithesthōsan</em>) is the word Jesus used on the cross in Luke 23:46 ('into your hands I commit my spirit') — the same act of self-entrusting to the faithful God that Christ performed in his death is the model for the community's suffering-trust. The 'faithful Creator' (<em>pistō Ktistē</em>) is the God who was faithful to raise Christ from the dead and will be faithful to raise those who entrust themselves to him.</p>"
  }
}

# ============================================================
# 2 PETER
# ============================================================

TWOPET_ECHO = {
  "1": {
    "16": [
      {"type": "allusion", "target": "Dan 7:13-14", "note": "The power and coming of our Lord Jesus Christ — the Danielic 'power and great glory' of the Son of Man's coming; Peter grounds the Transfiguration as the preview of the parousia-power and glory that Daniel anticipated"},
      {"type": "allusion", "target": "Ps 2:7", "note": "This is my beloved Son with whom I am well pleased — the divine voice at the Transfiguration echoes Ps 2:7's royal adoption formula; Peter as eyewitness to this Father-to-Son declaration grounds his eschatological teaching"}
    ]
  },
  "3": {
    "13": [
      {"type": "fulfillment", "target": "Isa 65:17", "note": "New heavens and a new earth in which righteousness dwells — Peter cites the Isaianic new creation promise (Isa 65:17; 66:22) as the eschatological expectation; the new creation where righteousness dwells (not merely exists but inhabits fully) is the goal toward which the present cosmos is moving"}
    ]
  }
}

TWOPET_ORIGINAL = {
  "3": {
    "9": "<p><strong>ou bradynei Kyrios tes epangelias hos tines bradyteta hegountai alla makrothymei eis hymas me boulomenos tinas apolesai alla pantas eis metanoian chorein</strong> (<em>ou bradynei Kyrios tēs epangelias, hōs tines bradytēta hēgountai, alla makrothymei eis hymas, mē boulomenos tinas apolesthai alla pantas eis metanoian chōrein</em>): 'The Lord is not slow to fulfill his promise as some count slowness, but is patient toward you, not wishing that any should perish but that all should reach repentance.' <em>Makrothymia</em> (patience/longsuffering) reframes the delayed parousia as a divine mercy-extension rather than a failed prediction. The universalistic-sounding 'not wishing that any should perish' is balanced by 'toward you' — the patience is specifically exercised toward the addressees, inviting them toward repentance. The passage is one of the key texts on divine patience and the purpose of eschatological delay.</p>"
  }
}

TWOPET_CONTEXT = {
  "3": {
    "3": "<p>The 'scoffers' who mock the parousia promise ('Where is the promise of his coming? For ever since the fathers fell asleep, all things are continuing as they were from the beginning', vv. 3-4) reflect an Epicurean-style skepticism about divine intervention in the regularities of nature: if God were going to act, why hasn't he? The Epicurean doctrine of <em>ataraxia</em> (undisturbed natural regularity, governed by atoms, not divine providence) provided intellectual cover for dismissing apocalyptic expectations. Peter's response: the uniformitarians forget that the past was not uniform — the flood was God's catastrophic intervention in the 'natural order' (vv. 5-6), and the coming fire will be the next. The argument uses Genesis to rebut Epicurean naturalism.</p>"
  }
}

TWOPET_CHRIST = {
  "1": {
    "1": "<p>A direct revelation: 'To those who have obtained a faith of equal standing with ours by the righteousness of our God and Savior Jesus Christ.' The phrase 'our God and Savior Jesus Christ' (<em>tou theou hemon kai soteros Iesou Christou</em>) — following the same Granville Sharp single-article construction as Titus 2:13 — directly predicates deity of Jesus Christ. 2 Peter opens with its highest Christological claim: Jesus is God and Savior. This framing situates the entire letter's authority under the person of the divine Savior whose return the scoffers mock.</p>"
  },
  "3": {
    "10": "<p>A direct revelation: 'The day of the Lord will come like a thief, and then the heavens will pass away with a roar, and the heavenly bodies will be burned up and dissolved, and the earth and the works that are done on it will be exposed.' The Day of the Lord (the YHWH theophany-judgment tradition; Amos 5:18-20; Joel 2; Zeph 1:14-18) is identified with the Day of Jesus Christ (v. 12: 'waiting for and hastening the coming of the day of God'). The cosmic dissolution is not the end of material existence but its purification — leading to the new heavens and new earth of v. 13. The Christological judgment: the Lord Jesus presides over this dissolution as the eschatological judge whose day arrives unexpectedly.</p>"
  }
}

# ============================================================
# 2 JOHN, 3 JOHN, JUDE
# ============================================================

TWOJOHN_ECHO = {
  "1": {
    "7": [
      {"type": "allusion", "target": "1 John 4:2", "note": "Those who do not confess the coming of Jesus Christ in the flesh are the deceiver and the antichrist — the same anti-Docetic test as 1 John 4:2 (every spirit that confesses Jesus Christ has come in the flesh is from God); 2 John applies the same doctrinal test to traveling teachers"}
    ]
  }
}

TWOJOHN_ORIGINAL = {
  "1": {
    "7": "<p><strong>hoti polloi planoi exelthon eis ton kosmon hoi me homologountes Iesoun Christon erchomenon en sarki houtos estin ho planos kai ho antichristos</strong> (<em>hoti polloi planoi exēlthon eis ton kosmon, hoi mē homologountes Iēsoun Christon erchomenon en sarki</em>): 'For many deceivers have gone out into the world, those who do not confess the coming of Jesus Christ in the flesh.' The present participle <em>erchomenon</em> (coming) rather than the perfect <em>elēlythota</em> (having come, 1 John 4:2) may signal a future reference — not the Incarnation but the parousia. Either way, the test is the same: affirm the bodily reality of Jesus's existence, whether past (Incarnation) or future (Return). The Docetic denial of Christ's flesh eliminates both the atonement and the resurrection-body hope.</p>"
  }
}

TWOJOHN_CONTEXT = {
  "1": {
    "1": "<p>2 John is addressed from 'the elder' to 'the elect lady and her children' — most likely a metaphor for a particular congregation and its members (cf. 1 Pet 5:13 where 'Babylon' = Rome; 'she' = the church in Babylon). The 'elder' is commonly identified with John the Apostle or John the Elder of Ephesus (Papias distinguishes these; Eusebius records the tradition of two Johns in Asia). The letter is a brief (13 verses) traveling advisory: the practice of Greco-Roman hospitality created real danger for Christian communities — traveling teachers could exploit the obligation of hospitality to spread heresy. 2 John's 'do not receive him into your house' (v. 10) restricts the normal hospitality-obligation for doctrinal cause.</p>"
  }
}

TWOJOHN_CHRIST = {
  "1": {
    "3": "<p>A direct revelation: 'Grace, mercy, and peace will be with us from God the Father and from Jesus Christ the Father's Son.' The Trinitarian greeting (Father and Son together as the source of grace, mercy, and peace) frames 2 John's doctrinal concern: the Christ of the greeting (the Son of the Father) is the same Christ whose bodily reality the deceivers deny (v. 7). Christology determines fellowship (vv. 9-11): to go beyond Christ's teaching is to lose the Father; to hold the Son's teaching is to have both the Son and the Father. The Christological and Trinitarian are inseparable in 2 John.</p>"
  }
}

THREEJOHN_ECHO = {
  "1": {
    "11": [
      {"type": "allusion", "target": "Gen 1:4", "note": "Whoever does good is from God; whoever does evil has not seen God — the fundamental creation-theology judgment: good comes from God, evil does not; 3 John applies this creation-ethics criterion to the community conflict between the hospitable Gaius and the domineering Diotrephes"}
    ]
  }
}

THREEJOHN_ORIGINAL = {
  "1": {
    "4": "<p><strong>meizotera toutōn ouk echo charan hina akouo ta ema tekna en te aletheia peripatounta</strong> (<em>meizoteran toutōn ouk echō charan, hina akouō ta ema tekna en tē alētheia peripatounta</em>): 'I have no greater joy than to hear that my children are walking in the truth.' The elder's pastoral identity is entirely defined by the spiritual progress of his 'children' — those he has led to faith. <em>Peripatountas en te aletheia</em> (walking in truth) is the Johannine idiom for the whole-life embodiment of the gospel: truth is not merely intellectual assent but an ambulatory practice that shapes the whole life.</p>"
  }
}

THREEJOHN_CONTEXT = {
  "1": {
    "9": "<p>Diotrephes 'who likes to put himself first' (<em>philoproteuo</em>, v. 9) represents the emergence of local congregational autonomy that resisted the authority of the itinerant apostolic elder. The conflict between the elder's authority (rooted in the apostolic tradition) and Diotrephes's local authority (rooted in congregational control) anticipates the later tension between episcopal and local governance structures. Diotrephes's practices — refusing the elder's letter, refusing to receive traveling brothers, and expelling those who do — constitute a miniature local church coup. 3 John is the NT's only document addressing intra-Christian church politics at this granular level.</p>"
  }
}

THREEJOHN_CHRIST = {
  "1": {
    "7": "<p>A direct revelation: 'For they have gone out for the sake of the name, accepting nothing from the Gentiles.' The missionaries who deserve hospitality go out 'for the sake of the Name' (<em>hyper tou onomatos</em>) — the Name of Jesus, YHWH's eschatological Name in the NT (Acts 4:12; Phil 2:9-10). They are supported not by the Gentile world's resources but by the community of believers. The missional church is defined by: (1) the Name as motivation, (2) non-worldly financial support, and (3) mutual community support (<em>synergoi</em>, v. 8). The entire brief letter is framed within this Christological missiology.</p>"
  }
}

JUDE_ECHO = {
  "1": {
    "9": [
      {"type": "allusion", "target": "Zech 3:2", "note": "The Lord rebuke you — Michael's rebuke of the devil in Jude's midrash on the Assumption of Moses echoes YHWH's rebuke of Satan in Zech 3:2 ('The LORD rebuke you, O Satan'); the heavenly court's handling of demonic accusation follows the same pattern"}
    ],
    "14": [
      {"type": "quote", "target": "1 Enoch 1:9", "note": "Behold the Lord comes with ten thousands of his holy ones to execute judgment — Jude quotes 1 Enoch 1:9 as prophetic authority; this is the only direct quotation of 1 Enoch in the NT, indicating the apocalyptic tradition's authority in some early Christian communities"},
      {"type": "allusion", "target": "Deut 33:2", "note": "He came from Sinai ... with holy ones at his right hand — the Sinai theophany with the myriads of holy ones (angels/saints); both Deut 33:2 and 1 Enoch 1:9 draw from the same theophany tradition that Jude applies to the parousia of Christ"}
    ]
  }
}

JUDE_ORIGINAL = {
  "1": {
    "3": "<p><strong>parakalo agapetoi pasan spoude poioumenos graphein hymin peri tes koines soteries anagkaion egesamen grapsai hymin parakalon epagonizesthai te hapax paradotheise tois hagiois pistei</strong>: 'I found it necessary to write appealing to you to contend for the faith that was once for all delivered to the saints.' <em>Hapax paradotheise</em> (once for all delivered): the single, unrepeatable handing-over of the faith — <em>paradidomi</em> is the technical tradition-transmission verb (as in 1 Cor 11:23, 15:3). The faith is not a developing deposit that each generation revises but a fixed, delivered tradition that needs defending, not augmenting. <em>Epagonizomai</em> (contend earnestly for) is the athletic-contest word applied to doctrinal fidelity — not aggressive attack of opponents but vigorous defense of what was given.</p>"
  }
}

JUDE_CONTEXT = {
  "1": {
    "4": "<p>The opponents Jude addresses are 'certain people who have crept in unnoticed' (<em>pareisedysan</em>) — using the technical language of infiltration. They are described as 'perverting the grace of our God into sensuality and denying our only Master and Lord Jesus Christ.' The combination of antinomian sexual license ('sensuality') with Christological denial suggests a proto-Gnostic group that used the grace-freedom of the gospel (cf. Rom 6:1: 'shall we continue in sin so that grace may abound?') as license for moral license. Jude's use of 1 Enoch and the Assumption of Moses (v. 9) indicates familiarity with the wider Jewish apocalyptic tradition and suggests a Jewish-Christian context for both author and audience.</p>"
  }
}

JUDE_CHRIST = {
  "1": {
    "25": "<p>A direct revelation: 'To the only God, our Savior, through Jesus Christ our Lord, be glory, majesty, dominion, and authority before all time and now and forever.' Jude's doxology is the most comprehensive Christological doxology in the NT — ascribing glory, majesty, dominion, and authority (four throne-room attributes of YHWH in Daniel and Isaiah) to God through Christ, and extending this across all three tenses of time (before, now, forever). The Christ through whom this glory is ascribed is the Lord whose 'love you keep yourselves in' (v. 21) and who presents believers blameless with rejoicing (v. 24). The letter's defense of the faith is framed by this doxological Christology.</p>"
  }
}

def main():
    books_data = [
        ('james', JAMES_ECHO, JAMES_ORIGINAL, JAMES_CONTEXT, JAMES_CHRIST),
        ('1peter', ONEPET_ECHO, ONEPET_ORIGINAL, ONEPET_CONTEXT, ONEPET_CHRIST),
        ('2peter', TWOPET_ECHO, TWOPET_ORIGINAL, TWOPET_CONTEXT, TWOPET_CHRIST),
        ('2john', TWOJOHN_ECHO, TWOJOHN_ORIGINAL, TWOJOHN_CONTEXT, TWOJOHN_CHRIST),
        ('3john', THREEJOHN_ECHO, THREEJOHN_ORIGINAL, THREEJOHN_CONTEXT, THREEJOHN_CHRIST),
        ('jude', JUDE_ECHO, JUDE_ORIGINAL, JUDE_CONTEXT, JUDE_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books_data:
        e = load_echo(book)
        merge_echo(e, echo_d)
        save_echo(book, e)

        c = load_comm('mkt-original', book)
        merge_comm(c, orig_d)
        save_comm('mkt-original', book, c)

        c = load_comm('mkt-context', book)
        merge_comm(c, ctx_d)
        save_comm('mkt-context', book, c)

        c = load_comm('mkt-christ', book)
        merge_comm(c, chr_d)
        save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
