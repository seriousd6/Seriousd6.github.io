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
  },
  "5": {
    "1": "<p><strong>presbyterous tous en hymin parakalō ho sympresbyteros kai martys ton tou Christou pathēmatōn</strong>: 'To the elders among you, I appeal as a fellow elder and a witness of Christ's sufferings.' <em>Sympresbyteros</em> (fellow elder) is a NT hapax — Peter places himself alongside rather than above the elders he addresses. <em>Martys tōn tou Christou pathēmatōn</em> (witness of Christ's sufferings) — <em>martys</em> is the legal term for a courtroom witness whose testimony is based on direct observation; Peter's witness grounds his authority in eyewitness proximity to the passion. The witness-language anticipates the later technical sense of <em>martys</em> as martyr (one who witnesses to Christ at the cost of life).</p>",

    "2": "<p><strong>poimanate to en hymin poimnion tou theou episkopountes mē anankastōs alla hekousiōs kata theon mēde aischrokerdōs alla prothumōs</strong>: 'Shepherd the flock of God that is among you, exercising oversight — not under compulsion, but willingly, as God would have you; not for shameful gain, but eagerly.' <em>Poimanate</em> (shepherd) is the imperative of <em>poimainō</em> — the same word Jesus uses in John 21:16 ('tend my sheep') in his post-resurrection commission to Peter. <em>Episkopountes</em> (exercising oversight) — the elder/shepherd/<em>episkopos</em> overlap is explicit: the three office-terms are functionally synonymous in the Pastoral and General Epistles (cf. Acts 20:28; Titus 1:5-7). The three contrasting pairs frame Christian leadership as voluntary, non-commercial, and non-coercive.</p>",

    "3": "<p><strong>mēde hōs katakyrienontes tōn klērōn all' typoi ginomenoi tou poimniou</strong>: 'not domineering over those in your charge, but being examples to the flock.' <em>Katakyrienontes</em> (domineering, lording it over) — the identical compound Jesus uses in Mark 10:42 ('those who are considered rulers lord it over them') to contrast worldly power with servant-leadership. <em>Klērōn</em> — <em>klēros</em> is the lot or allotted portion; the flock-members are God's property assigned to the elder, not the elder's own possession. <em>Typos</em> (example, pattern, type) — the elder's authority is embodied demonstration, not institutional power; the community is shaped by what they see in the leader, not merely by what they are commanded to do.</p>",

    "4": "<p><strong>kai phanerōthentos tou archipoimenos komisesthe ton amarantinon tēs doxēs stephanon</strong>: 'And when the Chief Shepherd appears, you will receive the crown of unfading glory.' <em>Archipoimēn</em> (Chief Shepherd) — a NT hapax legomenon, found nowhere in prior Greek literature; it places all local elders as sub-shepherds under the supreme Shepherd whose appearing is the parousia. <em>Amarantinon</em> (unfading, from <em>amarantos</em>, the flower that does not wither) — contrasted with the perishable laurel or celery wreaths of Greek athletic victories, which wilted within days. The crown of glory is the eschatological reward at the appearing (<em>phanerōthentos</em>, aorist passive participle of <em>phaneroō</em>, the epiphany-word) of the Chief Shepherd.</p>",

    "5": "<p><strong>pantes de allēlois tēn tapeinophrosynēn enkombōsasthe</strong> — <em>enkombōsasthe</em> (clothe yourselves with, tie on) is the verb for tying on a garment by knotting it; specifically associated with tying on the <em>encomboma</em>, the apron or loincloth of a slave's work-garment. The word appears to echo Jesus's action at the Last Supper (John 13:4-5: 'he laid aside his outer garments... and tied a towel around himself'). The quotation of Prov 3:34 LXX (<em>ho theos hyperēphanois antitassetai tapeinois de didōsin charin</em>) is verbatim with James 4:6, indicating this was a widely circulated community warrant for humility under pressure. <em>Tapeinophrosynē</em> (humility, lowly-mindedness) — a compound the Greek world regarded as servile and shameful; the NT rehabilitates it as the primary virtue of the community that follows the humble Servant.</p>",

    "6": "<p><strong>tapeinōthēte oun hypo tēn krataian cheira tou theou hina hymas hypsōsē en kairō</strong>: 'Humble yourselves, therefore, under the mighty hand of God, so that at the proper time he may exalt you.' <em>Krataia cheir tou theou</em> (mighty hand of God) — the Exodus formula (Deut 3:24; Exod 6:1; 1 Kgs 8:42 LXX): the same hand that rescued Israel from Egypt is the hand under which the community submits in the present. Submission to this hand is not oppression but the posture that positions for eschatological lifting-up. <em>En kairō</em> (at the proper time) — <em>kairos</em> is the divinely appointed moment, not clock-time; the exaltation is certain but the timing belongs to God's sovereign calendar.</p>",

    "7": "<p><strong>pasan tēn merimnan hymōn epiripsontes ep' auton hoti autō melei peri hymōn</strong>: 'casting all your anxieties on him, because he cares for you.' <em>Epiripsontes</em> (casting, throwing upon) — the aorist participle of <em>epiriptō</em>, the same word in LXX Ps 55:22: 'Cast your burden on the LORD, and he will sustain you.' Grammatically the participle is dependent on <em>tapeinōthēte</em> (v. 6) — the means of humbling oneself under God's hand is the active transfer of anxiety to him. <em>Melei autō peri hymōn</em> (it matters to him concerning you) — the verb <em>melō</em> expresses personal caring interest; God is not an indifferent sovereign but a shepherd who attends to the flock's welfare.</p>",

    "8": "<p><strong>nēpsate grēgorēsate ho antidikos hymōn diabolos hōs leōn ōryomenos peripatei zētōn tina katapiein</strong>: 'Be sober-minded, be watchful. Your adversary the devil prowls around like a roaring lion, seeking someone to devour.' <em>Nēpsate, grēgorēsate</em> (be sober, be watchful) — the standard NT pair for spiritual vigilance (1 Thess 5:6-8; Mark 13:33-37). <em>Antidikos</em> (adversary) — the legal term for the opposing party in a lawsuit; the <em>diabolos</em> as accuser in the heavenly court (Job 1-2; Zech 3:1; Rev 12:10: 'the accuser of our brothers has been thrown down'). <em>Leōn ōryomenos</em> (roaring lion) — draws on Ps 22:13 ('they open wide their mouths at me, like a ravening and roaring lion') and Ps 91:13 ('you will tread on the lion and the cobra').</p>",

    "9": "<p><strong>hō antistēte stereoi tē pistei eidotes ta auta tōn pathēmatōn tē en tō kosmō hymōn adelphotēti epiteleisthai</strong>: 'Resist him, firm in your faith, knowing that the same kinds of suffering are being experienced by your brotherhood throughout the world.' <em>Antistēte</em> (resist) — the same imperative as James 4:7; the shared use of Prov 3:34 LXX and this devil-resistance command suggests a common tradition circulating in the General Epistles community. <em>Stereoi</em> (firm, solid) — architectural language for load-bearing masonry; faith as the structural member that sustains pressure without collapsing. <em>Adelphotēs</em> (brotherhood) — a NT rare word (only here and 1 Pet 2:17); it names the universal community of believers as a single kinship-network spread across the Roman Empire's geography but unified in suffering and faith.</p>",

    "10": "<p><strong>ho de theos pasēs charitos ho kalesas hymas eis tēn aiōnion autou doxan en Christō oligon pathontas autos katartisai hymas stērixai sthenōsai themeliosei</strong>: 'And the God of all grace... will himself restore, confirm, strengthen, and establish you.' <em>Ho theos pasēs charitos</em> (the God of all grace) — a unique divine title in the NT; <em>pasēs charitos</em> (of all grace) declares that every variety and quantity of grace has a single divine source. <em>Oligon</em> (a little while) — the temporal brevity of suffering placed against eternal glory (cf. 2 Cor 4:17). The four aorist infinitives express God's own restorative action: <em>katartisai</em> (restore/equip — the word for mending torn fishing nets, Mark 1:19, and restoring a fallen person, Gal 6:1), <em>stērixai</em> (establish), <em>sthenōsai</em> (strengthen), <em>themeliosei</em> (lay a foundation under) — each is a building or structural term for God's post-suffering reconstruction.</p>",

    "11": "<p><strong>autō to kratos eis tous aiōnas tōn aiōnōn amēn</strong>: 'To him be the dominion forever and ever. Amen.' <em>Kratos</em> (dominion, ruling power) is the doxological term for God's sovereign authority: Rev 1:6 ('to him be glory and dominion forever'), Jude 25, 1 Tim 6:16. The brief doxology closes the letter's body before the epistolary conclusion of vv. 12-14. Its brevity concentrates all the letter's theology into the simple declaration that the God of grace (v. 10) who rescues and restores is the one who holds sovereign power — a counter-claim against imperial pretensions to divine dominion.</p>",

    "12": "<p><strong>dia Silouanou hymin tou pistou adelphou hōs logizomai di' oligōn egraxa parakalōn kai epimarturōn tautēn einai alēthē charin tou theou eis hēn stēte</strong>: 'Through Silvanus... I have written briefly, encouraging you and testifying that this is the true grace of God. Stand firm in it.' <em>Silouanos</em> (Silvanus/Silas) — Paul's co-worker (2 Thess 1:1; 1 Thess 1:1; Acts 15:22, 40), whose association with both Peter and Paul bridges the Petrine and Pauline traditions. <em>Di' Silouanou egraxa</em> (through Silvanus I have written) — <em>dia</em> with the genitive may mean he was amanuensis (took dictation), scribe who drafted in polished Greek from Peter's Aramaic, or letter-carrier. <em>Epimarturōn</em> (testifying, bearing witness to) returns the letter to its opening witness-language (v. 1): the same apostolic authority grounds both personal appeal and doctrinal affirmation.</p>",

    "13": "<p><strong>aspazetai hymas hē en Babylōni syneklektē kai Markos ho huios mou</strong>: 'She who is in Babylon, chosen together with you, sends you greetings, and so does my son Mark.' <em>Hē en Babylōni</em> — the personified local church at Peter's location; in Christian apocalyptic, Babylon = Rome (Rev 14:8; 17:5; 18:2; 4 Ezra 3:1-2 where Babylon = Rome in Jewish apocalyptic contemporary with 1 Peter). The code-name functions as both discretion under Roman persecution and theological commentary: Rome is Babylon, the empire of captivity from which God delivers. <em>Markos ho huios mou</em> (Mark my son) — Papias (in Eusebius HE 3.39) records that Mark composed his Gospel from Peter's preaching: 'Mark, having become the interpreter of Peter, wrote down accurately everything he remembered of the things said and done by the Lord.'</p>",

    "14": "<p><strong>aspasasthe allēlous en philēmati agapēs eirēnē pasin tois en Christō</strong>: 'Greet one another with a kiss of love. Peace to all of you who are in Christ.' <em>Philēmati agapēs</em> (kiss of love) — the liturgical community greeting established in the Pauline letters (Rom 16:16; 1 Cor 16:20; 2 Cor 13:12; 1 Thess 5:26) and later formalized in the eucharistic liturgy (Justin Martyr, <em>Apology</em> 1.65, ca. 155 CE). The <em>agapēs</em> qualifier distinguishes it from ordinary social greetings — it is the enacted expression of the community's distinctive love for one another. <em>En Christō</em> (in Christ) — the final incorporative formula: peace is not merely wished but located; the community exists <em>in</em> Christ as its social and spiritual space, and peace characterizes that shared location.</p>"
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
    "18": "<p>A direct revelation: 'You were ransomed from the futile ways inherited from your forefathers, not with perishable things such as silver or gold, but with the precious blood of Christ, like that of a lamb without blemish or spot.' The ransom-price Christology: Christ's blood is the currency of redemption from inherited futility. The Passover-lamb imagery connects the death of Christ to the entire Exodus-redemption narrative — as the Passover blood protected Israel from the destroying angel, Christ's blood ransoms believers from the bondage of empty ancestral religion. The lamb is not merely a metaphor for innocence but a liturgical category that places the cross within the sacrificial system's culmination.</p>"
  },
  "2": {
    "24": "<p>A fulfillment: 'He himself bore our sins in his body on the tree, that we might die to sin and live to righteousness. By his wounds you have been healed.' 1 Peter 2:22-25 is the most sustained application of Isa 53 to the passion in the NT outside the Gospel traditions. Peter works through the Servant Song verse by verse: v. 22 (Isa 53:9: no sin in his mouth), v. 23 (Isa 53:7: did not retaliate), v. 24 (Isa 53:4-5: bore our griefs, wounded for our iniquities, by his stripes we are healed), v. 25 (Isa 53:6: we all went astray like sheep). The suffering community (1:6-7; 2:19-21; 4:12-16) is invited to understand their own suffering through the Servant-Christ who bore sins and called them to follow his pattern.</p>"
  },
  "3": {
    "18": "<p>A direct revelation: 'Christ also suffered once for sins, the righteous for the unrighteous, that he might bring us to God, being put to death in the flesh but made alive in the spirit.' The uniqueness and finality of the atonement: <em>hapax</em> (once, for all time) marks the non-repeatability of Christ's sin-bearing death. The substitutionary logic: the righteous (<em>dikaios</em>) for the unrighteous (<em>adikous</em>) — the morally qualified dies for the morally disqualified. The telos: 'that he might bring us to God' (<em>hina hemas prosagagē to theo</em>) — access to God is the goal of the cross, not merely forgiveness as a legal transaction.</p>"
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
