"""
Combined script: 1 Timothy, 2 Timothy, Titus, Philemon — all four layers.
Output: echoes + mkt-original + mkt-context + mkt-christ for all four letters.

The Pastoral Epistles (ca. 60-67 CE or deutero-Pauline ca. 80-100 CE)
address church order, ministry qualifications, sound doctrine, and personal
discipleship. Key theological contributions: the faithful sayings (pistoi logoi),
the appearing (epiphaneia) Christology, and the portrait of Paul as exemplary sufferer.
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
# 1 TIMOTHY
# ============================================================

ONETIM_ECHO = {
  "2": {
    "5": [
      {"type": "fulfillment", "target": "Job 9:33", "note": "There is one mediator between God and people, the man Christ Jesus — Job's lament 'there is no arbiter between us who might lay his hand on us both' is answered: the mediator Job could not find is Christ, who as the man Christ Jesus bridges the divine-human gap"},
      {"type": "fulfillment", "target": "Isa 53:12", "note": "Who gave himself as a ransom for all — the Servant who poured out his soul to death and bore the sin of many; the ransom-giving fulfills the Servant's self-offering on behalf of the many"}
    ]
  },
  "3": {
    "16": [
      {"type": "allusion", "target": "Ps 24:3-4", "note": "He was manifested in the flesh, vindicated by the Spirit — the hymn of 1 Tim 3:16 celebrates the incarnation-exaltation pattern; the Psalm's ascent to YHWH's holy hill resonates with the vindicated Christ ascending to the heavenly Zion"},
      {"type": "allusion", "target": "Isa 52:15", "note": "Proclaimed among the nations, believed on in the world — the Servant's proclamation that would cause kings to shut their mouths; the worldwide proclamation of the exalted Christ fulfills the Servant's mission reaching to all nations"}
    ]
  }
}

ONETIM_ORIGINAL = {
  "2": {
    "5": "<p><strong>heis gar theos heis kai mesites theou kai anthropon anthropos Christos Iesous</strong> (<em>heis gar theos, heis kai mesitēs theou kai anthrōpōn, anthrōpos Christos Iēsous</em>): 'For there is one God and one mediator between God and people, the man Christ Jesus.' The <em>mesites</em> (mediator) terminology was used in both Hellenistic contract law (a third party who guarantees a transaction) and in LXX usage for Moses's mediating role at Sinai (Gal 3:19-20). The Christological uniqueness: there is <em>one</em> mediator — contra the Greco-Roman polytheistic model of multiple divine intermediaries, and contra any Jewish or emerging Gnostic scheme of angelic mediators. The qualifier <em>anthrōpos</em> (man) before Christ Jesus emphasizes the genuine humanity that enables the mediation: the mediator must be able to touch both parties.</p>"
  },
  "3": {
    "16": "<p><strong>homologoumenos mega estin to tes eusebeias mysterion</strong>: 'Great indeed, as we confess, is the mystery of godliness.' What follows (vv. 16b-c) is almost certainly a pre-Pauline hymn or creedal fragment in six lines, possibly arranged in two strophes of three: (1) manifested in flesh / vindicated by Spirit / seen by angels; (2) proclaimed among nations / believed in the world / taken up in glory. The six verbs are all aorist passives — divine actions done to Christ. The structure mirrors Phil 2:6-11's humiliation-exaltation pattern: the first triad (incarnation, vindication, heavenly witness) parallels the descending and ascending of the Christ-hymn.</p>"
  },
  "6": {
    "15": "<p><strong>ho makarios kai monos dynamastes ho basileus ton basileonton kai kyrios ton kyrieonton</strong> (<em>ho makarios kai monos dynastēs, ho basileus tōn basileuontōn kai kyrios tōn kyrieuontōn</em>): 'the blessed and only Sovereign, the King of kings and Lord of lords.' The doxology of 6:15-16 applies to the epiphaneia of Jesus the titles that Hellenistic rulers and the Roman emperor claimed. <em>Dynastēs</em> (Sovereign/potentate) was used of divine-right rulers in the Hellenistic east. <em>King of kings and Lord of lords</em> echoes Deut 10:17 (YHWH as God of gods and Lord of lords) and Daniel 2:37, 47 (the God of heaven as King over kings). The doxology places the Roman emperor's pretensions under the sovereignty of Christ.</p>"
  }
}

ONETIM_CONTEXT = {
  "1": {
    "3": "<p>1 Timothy is addressed to Timothy in Ephesus — Paul's extended base of ministry (Acts 19, ca. 52-55 CE; and likely again ca. 60-65 CE if the Pastoral Epistles reflect a release from Roman imprisonment). Ephesus was the largest city in the province of Asia and the site of the Artemis temple; it had a large Jewish community, numerous mystery cult associations, and by the late first century a substantial Christian community (see Revelation 2:1-7). The false teachers Timothy must address are described as teaching 'different doctrine' (<em>heterodidaskale</em>), focusing on 'myths and endless genealogies' (1:4) and 'what they call knowledge' (<em>pseudonymos gnōsis</em>, 6:20), possibly an early form of Jewish-Gnostic speculation.</p>"
  },
  "5": {
    "17": "<p>The 'double honor' for elders who rule well (v. 17) — especially those who labor in preaching and teaching — reflects the early church's emerging distinction between lay elders and teaching-preaching elders. The citation of Deut 25:4 (do not muzzle an ox when it treads grain) and the dominical saying 'the laborer deserves his wages' (Luke 10:7) as dual warrant for paying ministers indicates that by the Pastoral period, apostolic-era oral tradition (Jesus's teaching) was already cited alongside Torah as authoritative Scripture.</p>"
  }
}

ONETIM_CHRIST = {
  "1": {
    "15": "<p>A direct revelation: 'The saying is trustworthy and deserving of full acceptance, that Christ Jesus came into the world to save sinners, of whom I am the foremost.' The first of the Pastoral Epistles' five 'faithful sayings' (<em>pistos ho logos</em>) is a Christological mission-statement: the incarnation's purpose is soteriological — Christ came into the world (implying pre-existence, like John 1:14) specifically to save sinners. Paul's self-designation as 'the foremost of sinners' makes the statement an autobiographical proof: if Christ saved me (the persecutor of the church), his saving purpose is as wide as the worst sinner.</p>"
  },
  "2": {
    "5": "<p>A direct revelation: 'There is one mediator between God and people, the man Christ Jesus, who gave himself as a ransom for all.' The two Christological claims together: (1) Christ is the unique, sole mediator — no competing spiritual hierarchy is needed or valid; (2) his mediation was accomplished through self-giving as a ransom (<em>antilytron</em>, substitutionary ransom-payment). <em>Antilytron</em> (found only here in NT) intensifies <em>lytron</em> (ransom, Mark 10:45) with the <em>anti</em> prefix indicating substitution: a ransom given in place of others. The universality ('for all', <em>hyper pantōn</em>) combined with the singularity ('one mediator') is the Christological center of 1 Timothy's soteriology.</p>"
  },
  "3": {
    "16": "<p>A direct revelation: 'He was manifested in the flesh, vindicated by the Spirit, seen by angels, proclaimed among the nations, believed on in the world, taken up in glory.' The Christological hymn traces the entire arc of Christ's work in six compressed phrases: incarnation → resurrection-vindication → heavenly acknowledgment → worldwide proclamation → faith-response → ascension. The hymn is the doctrinal center of the household-of-God section (3:14-16): sound church order and ministry is grounded in the Christological mystery that the church has received and proclaims.</p>"
  }
}

# ============================================================
# 2 TIMOTHY
# ============================================================

TWOTIM_ECHO = {
  "2": {
    "8": [
      {"type": "fulfillment", "target": "2 Sam 7:12-13", "note": "Jesus Christ, risen from the dead, the offspring of David — the Davidic promise (I will raise up your offspring after you and establish his throne forever) is fulfilled in the resurrection of David's descendant Jesus; the risen Christ is the Davidic heir whose kingdom will have no end"}
    ]
  },
  "3": {
    "16": [
      {"type": "allusion", "target": "Deut 31:19-22", "note": "All Scripture is breathed out by God — the divine-origin claim for Scripture echoes YHWH's instruction to Moses to write down the Song (Deut 31:19) as a witness; the written word as YHWH's own testimony against and for Israel; now extended to all Scripture"}
    ]
  },
  "4": {
    "8": [
      {"type": "allusion", "target": "Isa 40:10", "note": "Henceforth there is laid up for me the crown of righteousness which the Lord, the righteous judge, will award — YHWH coming with his reward, his recompense before him; Paul's awaited crown from the righteous judge at the parousia echoes the Isaianic expectation of the Lord's coming with vindication for the righteous"}
    ]
  }
}

TWOTIM_ORIGINAL = {
  "2": {
    "15": "<p><strong>spoudason seauton dokimon parastēsai to theo ergaten anepaiskunton orthotomounta ton logon tes aletheias</strong> (<em>spoudason seauton dokimon parastēsai tō theō, ergatēn anepaiskunton, orthotomounta ton logon tēs alētheias</em>): 'Do your best to present yourself to God as one approved, a worker who has no need to be ashamed, rightly handling the word of truth.' <em>Orthotomounta</em> (rightly dividing/handling/cutting): used in LXX Prov 3:6 ('he will make straight your paths') and 11:5. The word evokes a craftsman cutting or laying material in a straight line — a road-builder, a carpenter, a surgeon. The image: the handling of the word of truth requires the precision and skill of a craftsman who cuts straight rather than crooked. Historically, the King James 'rightly dividing' was applied dispensationally; the original metaphor is about competent, accurate, straight-course exposition.</p>"
  },
  "3": {
    "16": "<p><strong>pasa graphe theopneustos kai ophelimos</strong> (<em>pāsa graphē theopneustos kai ōphelimos</em>): 'All Scripture is God-breathed (<em>theopneustos</em>) and profitable.' <em>Theopneustos</em> is a Pauline coinage (hapax legomenon) combining <em>theos</em> (God) and <em>pneō</em> (breathe) — 'God-breathed' or 'breathed out by God.' The breath-metaphor echoes Gen 2:7 (YHWH breathed into Adam's nostrils) and the Spirit-wind of Ezekiel's valley of bones: the Scriptures are alive with divine breath, not merely human compositions. The primary referent is the OT (which Timothy was taught from childhood, v. 15); the claim's extension to apostolic writings is implicit in 2 Pet 3:16's treatment of Paul's letters as <em>graphe</em>.</p>"
  }
}

TWOTIM_CONTEXT = {
  "1": {
    "8": "<p>2 Timothy is widely regarded as Paul's final letter — written from a second Roman imprisonment ca. 66-67 CE, shortly before his death (4:6-8). The tone differs markedly from 1 Timothy: more personal, more urgent, more reflective of approaching death. The suffering-motif pervades the letter: Paul's chains (1:8, 16; 2:9), his abandonment by former associates (1:15; 4:10-16), his awareness of impending execution (4:6-8). If authentic (and most scholars accept 2 Timothy as more likely Pauline than 1 Timothy or Titus), it is the most personal surviving Pauline document. The mention of specific people (Hymenaeus, Philetus, Alexander the coppersmith, Demas, Luke, Mark) and personal items (the cloak at Troas, the books and parchments, 4:13) suggests authentic personal memory.</p>"
  },
  "3": {
    "1": "<p>The 'last days' (<em>eschatais hēmerais</em>) characterized by moral collapse (vv. 1-9: lovers of self, lovers of money, proud, arrogant, abusive, disobedient to parents, ungrateful, unholy, heartless, unappeasable...) represents a conventional form in Jewish and early Christian eschatological literature called the 'signs of the end' tradition — cf. 1 Enoch 91-93 (the Apocalypse of Weeks), 2 Baruch 27-30, and rabbinic descriptions of the era before Messiah's coming. Paul's use of this tradition applies it to the present crisis in Timothy's ministry, not a distant future: the last days have already begun in the false teachers' behavior.</p>"
  }
}

TWOTIM_CHRIST = {
  "1": {
    "10": "<p>A direct revelation: 'Our Savior Christ Jesus abolished death and brought life and immortality to light through the gospel.' The Christological declaration concentrates the gospel: Christ 'abolished' (<em>katargēsantos</em>) death — not merely defeated it but rendered it inoperative; brought life and immortality 'to light' (<em>phōtisantos</em>) — these were previously hidden in God's eternal purpose (v. 9) but are now disclosed through the proclamation. The Christology of 2 Timothy: the epiphany of the Savior is the historical moment when death's power was broken and life was made publicly visible.</p>"
  },
  "2": {
    "8": "<p>A direct revelation: 'Remember Jesus Christ, risen from the dead, the offspring of David, as preached in my gospel.' Paul's summary of the gospel in one sentence unites the two great OT streams: Davidic messiahship (the royal covenant of 2 Sam 7) and resurrection (the prophetic expectation of Isa 26:19; Dan 12:2). 'Remember' (<em>mnemoneue</em>) is imperative — not a passive recollection but an active, sustaining focus on the Christological fact that generates Paul's willingness to suffer (v. 9-10: I endure everything for the sake of the elect). The risen Davidic Christ is the content of endurance.</p>"
  },
  "4": {
    "8": "<p>A direct revelation: 'Henceforth there is laid up for me the crown of righteousness, which the Lord, the righteous judge, will award to me on that Day — and not only to me but also to all who have loved his appearing.' The parousia of Christ (the <em>epiphaneia</em> that Paul loved) is the moment of final vindication. The 'crown of righteousness' is not earned by Paul's sufferings but 'laid up' (<em>apokeitai</em>) — already determined, awaiting award. The righteous judge who will confer it is Christ himself. The Christological movement of 2 Timothy: from the first epiphaneia (incarnation, 1:10) through present endurance to the final epiphaneia where the judge vindicates the faithful.</p>"
  }
}

# ============================================================
# TITUS
# ============================================================

TITUS_ECHO = {
  "2": {
    "14": [
      {"type": "fulfillment", "target": "Exod 19:5", "note": "To purify for himself a people of his own possession — YHWH's Sinai declaration 'you shall be my treasured possession' (LXX: laos periousios, exactly the term used here); the new covenant community is the fulfillment of what the Sinai covenant pointed toward"},
      {"type": "fulfillment", "target": "Ezek 37:23", "note": "Who gave himself to redeem us from all lawlessness — YHWH's promise to cleanse Israel from all their backslidings; the redemption from lawlessness fulfills Ezekiel's new covenant cleansing promise"}
    ]
  },
  "3": {
    "5": [
      {"type": "fulfillment", "target": "Ezek 36:25-27", "note": "Renewing of the Holy Spirit whom he poured out on us richly — YHWH's promise to sprinkle clean water, put his Spirit within, and cause Israel to walk in his statutes; the new birth through the Spirit fulfills Ezekiel's new covenant restoration"}
    ]
  }
}

TITUS_ORIGINAL = {
  "2": {
    "13": "<p><strong>prosdechomenoi ten makarian elpida kai epiphaneian tes doxes tou megalou theou kai soteros hemon Iesou Christou</strong> (<em>prosdechomenoi tēn makarian elpida kai epiphaneian tēs doxēs tou megalou theou kai sōtēros hēmōn Iēsou Christou</em>): 'waiting for our blessed hope, the appearing of the glory of our great God and Savior Jesus Christ.' The Greek syntax — <em>tou megalou theou kai soteros hemon Iesou Christou</em> — with the single definite article governing both 'God' and 'Savior' (the Granville Sharp rule) most naturally refers to one person: 'our great God and Savior, Jesus Christ.' This is one of the most explicit divine predications of Jesus in the NT — calling him directly 'our great God.' <em>Epiphaneia</em> (appearing/manifestation) is the distinctive Pastoral Christological term for the Incarnation (1 Tim 3:16; 2 Tim 1:10) and the parousia (1 Tim 6:14; 2 Tim 4:1, 8) — a term the Hellenistic world used for the appearance of a deity or the arrival of a king.</p>"
  }
}

TITUS_CONTEXT = {
  "1": {
    "1": "<p>Paul opens as 'servant of God and apostle of Jesus Christ' (<em>doulos theou, apostolos de Iēsou Christou</em>). The double title is unique — elsewhere Paul uses 'servant of Christ Jesus' (Rom 1:1, Phil 1:1). 'Servant of God' (<em>doulos theou</em>) is the LXX designation for Israel's great leaders: Moses (Josh 14:7), Joshua (Judg 2:8), and the prophets (Amos 3:7; Dan 9:11). By claiming it here Paul places his apostolate in the tradition of the OT prophets and mediators, lending his authority over the Cretan churches the weight of the prophetic office. The purpose clause — 'for the faith of God's elect and their knowledge of the truth that leads to godliness' — frames the entire letter: apostolic authority serves a specific telos of community character formation.</p>",

    "2": "<p>'In hope of eternal life, which God, who does not lie, promised before the beginning of time.' The phrase <em>ho apseudēs theos</em> (the non-lying God) stands in deliberate contrast with the Cretan cultural environment, since Greek-Roman deities were well-known for deception: Zeus disguised himself repeatedly, Apollo gave ambiguous oracles, Hermes was the god of trickery. The Cretan site of the tomb of Zeus — the mythological claim that Zeus was born and buried on Crete — made the island a byword for impiety even among pagans. Against this backdrop, the reliability of God's pre-temporal promise (<em>pro chronōn aiōniōn</em>, literally 'before ages of time') grounds the Christian hope not in cultic manipulation but in the character of a God who cannot deceive.</p>",

    "3": "<p>'He revealed his word through the proclamation (<em>kērugma</em>) entrusted to me by the command of God our Savior.' <em>Kērugma</em> (proclamation, herald's announcement) is the technical term for the authoritative public declaration of a ruler's message. In the Hellenistic world, the <em>kērux</em> (herald) spoke not his own word but the word of the authority who commissioned him — the herald's personal character was irrelevant to the binding force of the message. Paul's use here underscores that his proclamation is not rhetorical performance but the official herald-announcement of the divine king, entrusted 'by the command' (<em>kat' epitagēn</em>) of God — the same language used for imperial decrees. The 'appointed time' (<em>kairois idiois</em>) frames the gospel as the moment in God's sovereign calendar when the long-promised word finally broke into history.</p>",

    "4": "<p>'To Titus, my true son in our common faith.' Titus is not mentioned in Acts, but appears in Galatians (2:1-3) as a Gentile whom Paul deliberately brought to Jerusalem as a test case against compulsory circumcision — he was not circumcised (Gal 2:3). As a Gentile convert, Titus embodies the very truth the letter defends: that Gentiles stand equally in the faith without the Torah-boundary markers. Ancient letters used the greeting to establish relationship and credibility with letter-carriers and recipients; calling Titus 'genuine son' (<em>gnēsion teknon</em>) serves as both an affectionate address and a letter of introduction vouching for his authority to carry out the instructions that follow.</p>",

    "5": "<p>Titus in Crete: the island of Crete had a significant Jewish community (Acts 2:11; Josephus mentions Cretan Jews). Paul's description of Cretans — citing the Cretan poet Epimenides ('Cretans are always liars, evil beasts, lazy gluttons', v. 12) — uses an ancient ethnic stereotype familiar to his Greco-Roman audience. The church-planting task in Crete required appointing elders in 'every town' (<em>kata polin</em>), indicating a widespread but organizationally young mission. The Pastoral Epistles' emphasis on <em>episkopos</em> (overseer), <em>presbyteros</em> (elder), and <em>diakonos</em> (deacon) reflects the institutionalization of church leadership as the apostolic generation aged and died.</p>",

    "6": "<p>'Blameless, faithful to his wife, and whose children are believers' — the elder's household is the qualification. In Mediterranean honor-shame culture, a man's public reputation was inseparable from his household's conduct: an elder who could not maintain order and faith within his own family demonstrated unfitness to oversee the <em>oikos</em> (household) of God (v. 7). The phrase <em>mias gynaikos andra</em> (literally 'a one-woman man') is debated — whether it excludes polygamists, remarried widowers, or merely those with concurrent sexual relationships — but in context it signals undivided loyalty and household propriety. The requirement that children 'believe' (<em>tekna echōn pista</em>) reflects the ancient household-solidarity model: a family's conversion was typically understood as collective (cf. Acts 16:15, 31-34).</p>",

    "7": "<p>'An overseer, as God's steward, must be blameless — not overbearing, not quick-tempered, not given to drunkenness, not violent, not pursuing dishonest gain.' The title <em>episkopos</em> (overseer) was a Greek civic administrative term for a financial superintendent or inspector of public accounts; by the Pastoral Epistles it has become the standard term for the church's chief officer. The vice-list reflects the known abuses of patron-client relationships in antiquity: overbearing patrons exploited their clients, quick-tempered masters beat their slaves, drunkenness was the mark of an unruly symposium-host, violence was the tool of the powerful, and dishonest gain (<em>aischrokerdēs</em>) was the specific charge brought against itinerant sophists and corrupt magistrates. The elder must be what the typical powerful man in the Cretan social world was not.</p>",

    "8": "<p>'Rather he must be hospitable, one who loves what is good, who is self-controlled, upright, holy and disciplined.' The virtue-list mirrors the Hellenistic ideal of the honorable civic leader while filling it with specifically Christian content. Hospitality (<em>philoxenos</em>, love of the stranger) was a cardinal virtue in the ancient Mediterranean, where inns were dangerous and the traveler's safety depended on private hospitality networks; for the church it was essential to the movement of apostles, letter-carriers, and missionaries. <em>Sōphrōn</em> (self-controlled/temperate) was the foundational Platonic virtue, the mastery of appetite by reason — in the Pastorals it appears six times as the hallmark of Christian character formation across all social groups. The <em>enkratēs</em> (disciplined, self-mastered) draws from the Stoic vocabulary of mastery over one's impulses as the basis of civic virtue.</p>",

    "9": "<p>'He must hold firmly to the trustworthy message as it has been taught, so that he can encourage others by sound doctrine and refute those who oppose it.' The double task — encourage and refute — reflects the structure of ancient philosophical pedagogy, where the teacher both attracted students with positive vision and debated opponents to protect the school's teaching. <em>Didachē hugiainousē</em> (sound doctrine, health-giving teaching) uses the medical metaphor standard in the Pastorals: false teaching is a sickness (cf. 2 Tim 2:17 — it 'spreads like gangrene') while true teaching produces the health of godly character. The requirement to 'hold firmly' (<em>antechomenon</em>) to the received message rather than to speculate or innovate reflects the Pastoral Epistles' conservatism: the apostolic tradition is a <em>parathēkē</em> (deposit, trust) to be guarded, not developed.</p>",

    "10": "<p>'For there are many rebellious people, full of meaningless talk and deception, especially those of the circumcision group.' The 'circumcision group' (<em>hoi ek tēs peritomēs</em>) points to Jewish-Christian teachers insisting that Gentile converts observe Torah boundary-markers (circumcision, food laws, purity regulations). This was the same controversy Paul faced in Galatia and Colossae. Crete had a large Diaspora Jewish population, and the Cretan churches appear to have been penetrated by itinerant Jewish-Christian teachers who combined the gospel with Torah-observance requirements. The charge of 'meaningless talk' (<em>mataiologoi</em>) and 'deception' echoes the standard Hellenistic polemic against rival philosophical schools — the very language used by Stoics and Epicureans against sophists who taught for pay and personal influence rather than genuine wisdom.</p>",

    "11": "<p>'They must be silenced, because they are disrupting whole households and teaching things they ought not to teach — and that for the sake of dishonest gain.' The household (<em>oikos</em>) was the basic social and economic unit of Cretan society: a 'disrupted household' was not just a domestic quarrel but a social and economic catastrophe. False teachers who infiltrated households were targeting the very institutions that organized all of ancient Mediterranean life. 'Dishonest gain' (<em>aischrou kerdous charin</em>) is the charge Plato and other philosophers leveled against the sophists — itinerant teachers who charged fees for rhetorical skill and philosophical instruction. By contrast, Socrates famously refused to charge for his teaching. Paul's critique situates the false teachers as the ancient equivalent of fee-charging sophists whose motive is economic rather than pastoral.</p>",

    "12": "<p>'One of Crete's own prophets has said it: Cretans are always liars, evil brutes, lazy gluttons.' The quotation is from Epimenides of Cnossos (ca. 6th-5th century BCE), a semi-legendary figure who was reportedly sent for by the Athenians ca. 500 BCE to purify the city after religious pollution; Plato mentions him (Laws 1:642d) as an Athenian guest. The original context of the quote was Epimenides arguing that Zeus could not be dead (as Cretans claimed — they showed his tomb on the island) because Zeus is immortal: therefore all Cretans who say Zeus is dead are liars. The quotation creates a self-referential paradox known to logicians as the Epimenides paradox: if all Cretans are liars, then Epimenides (a Cretan) is also a liar, making his claim that all Cretans are liars possibly false. Paul uses it not as logic but as a recognized cultural critique from within: an insider's indictment of the cultural patterns the false teachers embody.</p>",

    "13": "<p>'This saying is true. Therefore rebuke them sharply, so that they will be sound in the faith.' The instruction to 'rebuke sharply' (<em>elenche apotomōs</em>) draws on the ancient philosophical tradition of <em>parrhesia</em> (frank speech, boldness of speaking truth). Hellenistic moral philosophers — especially the Cynics and Stoics — were known for blunt public rebukes of vice: Diogenes famously told Alexander the Great to get out of his sunlight. Socratic <em>elenchos</em> (the method of refutation through questioning) was considered the philosopher's therapeutic tool for exposing false opinion. Paul endorses this mode of sharp pastoral confrontation as the appropriate response to the Cretan false teachers — not in order to win an argument but to achieve a medical result: that the rebuked will become 'sound in the faith.'</p>",

    "14": "<p>'And will pay no attention to Jewish myths or to the merely human commands of those who reject the truth.' 'Jewish myths' (<em>Ioudaikois mythois</em>) likely refers to the elaborated haggadic traditions built around the OT narratives — speculative expansions of biblical stories that circulated in Second Temple Judaism: the Book of Jubilees, 1 Enoch, the Genesis Apocryphon, and similar literature that filled gaps in the biblical narrative with legendary material. 'Merely human commands' (<em>entolais anthrōpōn</em>) echoes Isa 29:13 (quoted by Jesus in Mark 7:7) — the rabbinic tradition of the 'fence around the Torah,' halakhic regulations built on top of the biblical commandments. Both charges — speculative mythology and legal elaboration — point to the same problem: adding to the apostolic <em>parathēkē</em> (deposit) rather than faithfully transmitting it.</p>",

    "15": "<p>'To the pure, all things are pure, but to those who are corrupted and do not believe, nothing is pure — in fact, both their minds and consciences are corrupted.' The principle 'to the pure, all things are pure' addresses the Levitical purity system — the classification of foods, objects, and persons as clean or unclean under the Torah. The false teachers in Crete apparently reinstated these purity distinctions (cf. the parallel situation in Colossae: Col 2:16 — 'Do not let anyone judge you by what you eat or drink'); their teaching divided the community by requiring Torah-observant food practice. Paul's counter-principle echoes his argument in Rom 14:20 ('Everything is clean') and 1 Cor 10:25-26 ('Eat anything sold in the meat market... for the earth is the Lord's'): for those in Christ, the Levitical purity code no longer determines what defiles, since defilement is a matter of the conscience and the moral will, not the ritual category of food.</p>",

    "16": "<p>'They claim to know God, but by their actions they deny him. They are detestable, disobedient, and unfit for doing anything good.' The charge that the false teachers 'claim to know God' (<em>homologousin eidénai theon</em>) while denying him by their actions invokes the Greek concept of the gap between theoretical knowledge and practical wisdom. Hellenistic philosophers distinguished <em>epistēmē</em> (theoretical knowledge) from <em>phronēsis</em> (practical wisdom / ethical discernment): knowing the good in theory was worthless without its embodiment in action. The Stoics were particularly sharp on this: the person who claims to be a philosopher but lives vice is not a philosopher at all but an impostor. Paul applies the same criterion to the false teachers: their claim to know God is invalidated by conduct that is 'detestable' (<em>bdelyktoi</em>, the same word used in LXX for the abominations of idolatry) and 'unfit for every good work' (<em>adokimoi</em>, the metallurgical term for metal that fails the assay-test and is rejected).</p>"
  },

  "2": {
    "1": "<p>'You, however, must teach what is appropriate to sound doctrine.' The contrast is emphatic — <em>su de</em> (you, however) sets Titus directly against the false teachers described in ch. 1. <em>Didaskalia hugiainousē</em> (sound doctrine, literally 'health-producing teaching') is the Pastoral Epistles' distinctive medical metaphor: the Greek medical tradition conceived of disease as imbalance and health as proper functioning of the body's systems. False teaching is a pathology that corrupts character; sound teaching restores the moral health of the community. The entire ch. 2 household code that follows is the practical content of this 'sound doctrine' — not an abstract system of beliefs but a concrete pattern of household relationships ordered by the gospel.</p>",

    "2": "<p>'Teach the older men to be temperate, worthy of respect, self-controlled, and sound in faith, in love and in endurance.' The instruction to older men (<em>presbyteras</em>) engages the Greco-Roman ideal of the honorable elder. In Hellenistic moral philosophy, age was supposed to bring the <em>sōphrosynē</em> (self-control) and <em>aidos</em> (dignity/respect) that younger men lacked. Aristotle's <em>Rhetoric</em> describes the old as cynical, petty, and suspicious — the stereotype Paul's instruction counters by demanding that Christian elders embody the positive ideal. The triad 'sound in faith, love and endurance' (<em>pistei, agapē, hypomonē</em>) is Paul's characteristic theological summary of the Christian life (cf. 1 Thess 1:3 — 'work of faith, labor of love, endurance of hope') — the elder must model not just civic virtue but specifically Christian character.</p>",

    "3": "<p>'Likewise, teach the older women to be reverent in the way they live, not to be slanderers or addicted to much wine, but to teach what is good.' Older women (<em>presbytidas</em>) in the ancient household occupied a socially ambiguous position: they had relative freedom from the supervision required of younger women (whose sexual fidelity was a family-honor matter), but this freedom could manifest in excessive drinking at household celebrations, gossiping at the market or baths, and malicious speech. The vice 'slanderers' (<em>diabolous</em>) — literally 'devil-like,' from <em>diabolos</em> (the accuser/slanderer) — reflects a recognized social pattern: ancient moral literature frequently cautions against older women as gossips and troublemakers. The instruction to 'teach what is good' (<em>kalodidaskalous</em>) — a compound found only here in the NT — gives older women a specific pedagogical role: the informal training of younger women that no male elder could carry out.</p>",

    "4": "<p>'Then they can urge the younger women to love their husbands and children.' The instruction for younger women (<em>neas</em>) is directed through the older women — a recognition that cross-gender instruction in the ancient household required the mediation of women in the women's domestic space. The verbs 'love their husbands' (<em>philandrous</em>) and 'love their children' (<em>philoteknous</em>) are compound adjectives found only here in the NT; they specify affectionate relational attachment, not merely formal duty. In the context of Greco-Roman marriages — which were often arranged, sometimes between much older men and very young women, with little expectation of emotional warmth — the instruction to cultivate genuine love is itself counter-cultural. The ancient <em>Haustafeln</em> (household-code) tradition (found also in Eph 5-6, Col 3-4, 1 Pet 2-3) typically addresses duties; here the Titus code emphasizes formed affections.</p>",

    "5": "<p>'To be self-controlled and pure, to be busy at home, to be kind, and to be subject to their husbands, so that no one will malign the word of God.' The rationale 'so that no one will malign the word of God' (<em>hina mē ho logos tou theou blasphēmētai</em>) makes the household ethics explicitly missional. In Roman provincial society, a respectable woman was defined by her domestic competence, sexual fidelity, and proper subordination to household authority — public gossip about a community whose women violated these norms would be a scandal that discredited their god and their message. 'Busy at home' (<em>oikourous</em>) does not restrict women to domestic work as an absolute norm but addresses the specific accusation that Christian women were abandoning household responsibilities. The entire ethical code is driven by witness logic: the church's credibility in the ancient city depended on its households being recognizably well-ordered by the standards of Greco-Roman society.</p>",

    "6": "<p>'Similarly, encourage the young men to be self-controlled.' <em>Sōphrōn</em> (self-controlled) is the sole and repeated instruction to young men — the summary virtue that encompasses all the rest. The Greek-Roman moral tradition was deeply concerned about young men's passions: Plato's <em>Republic</em> argued that the education of the young was the most critical political task, since uncontrolled passions in young men destroyed both households and cities. Aristotle's <em>Nicomachean Ethics</em> treats <em>sōphrosynē</em> as the mastery of the appetites for pleasure (especially sexual pleasure and food) by reason. The Stoics made <em>sōphrosynē</em> one of the four cardinal virtues. By condensing all instruction to young men into this single word, Titus signals that self-control is not merely a virtue but the pre-condition for every other virtue — the young man who cannot govern his passions cannot build a stable household, hold public office, or model the gospel.</p>",

    "7": "<p>'In everything set them an example by doing what is good. In your teaching show integrity, seriousness.' The instruction that Titus himself embody <em>typos kalōn ergōn</em> (a pattern/type of good works) draws on the ancient philosophical ideal of the teacher as living model. In Hellenistic moral philosophy, the teacher's life was the primary pedagogical text — Socrates taught by his manner of living as much as by his arguments; Epictetus's students were expected to imitate the philosopher's character. The concept of <em>typos</em> (pattern, type) carries the sense of a mold or stamp that leaves its impression on others: Titus is to be the impression that forms the young men around him. 'Integrity' (<em>aphthoria</em>, incorruption) and 'seriousness' (<em>semnotēta</em>) are the specific virtues of the Hellenistic teacher who refuses the sophists' compromises — not adapting the message to please the audience or to gain income.</p>",

    "8": "<p>'And soundness of speech that cannot be condemned, so that those who oppose you may be ashamed because they have nothing bad to say about us.' 'Soundness of speech that cannot be condemned' (<em>logon hugiē akatakoristos</em>) places Titus's public teaching under the scrutiny of the Greco-Roman rhetorical tradition: a speaker who could be condemned was one who could be caught in logical fallacy, ethical inconsistency, or factual error. The goal is that opponents — both the false teachers within the church and skeptical outsiders — will find no handle for legitimate criticism. This reflects the standard Hellenistic apologetic strategy: the best defense is a life and a message that cannot be attacked. The phrase 'those who oppose' (<em>ho ex enantias</em>, the one from the opposite side) suggests a formal rhetorical contest — the public debates that characterized philosophical schools in the ancient city.</p>",

    "9": "<p>'Teach slaves to be subject to their masters in everything, to try to please them, not to talk back to them.' Estimates of the enslaved population in the first-century Roman Empire range from one-fifth to one-third of the total population; in some urban areas (Rome, Corinth) the proportion was even higher. Enslaved persons in Greco-Roman households performed every conceivable service: agricultural labor, manufacturing, domestic service, accounting, teaching, medicine. The Pastoral Epistles address the enslaved as full moral agents capable of virtuous conduct — a significant counter-cultural move in a world that often denied slaves the capacity for virtue (Aristotle: <em>Politics</em> 1.5, 'the slave has no deliberative faculty'). The instruction to 'not talk back' (<em>mē antilégontas</em>) addresses the pattern of enslaved persons undermining household authority through passive resistance, gossip, and verbal insubordination — recognized management challenges in ancient slave-holding societies.</p>",

    "10": "<p>'And not to steal from them, but to show that they can be fully trusted, so that in every way they will make the teaching about God our Savior attractive.' The phrase 'make the teaching attractive' (<em>kosmōsin tēn didaskalian</em>, literally 'adorn the teaching') is the heart of the instruction: the enslaved Christian's conduct is a form of public theology. <em>Kosmeō</em> (to adorn, to put in good order) is the root of <em>kosmos</em> (the ordered world, beauty); the enslaved person who demonstrates trustworthiness and integrity 'adorns' the gospel like jewelry adorns a dress. This is the most missionally explicit statement in the Titus household code — the ethics of the enslaved is not merely about personal virtue or social order but about the credibility of the gospel message in the eyes of watching masters, neighbors, and the wider Roman world. The person who has least social power becomes the primary witness to the power of the gospel to transform character.</p>",

    "11": "<p>'For the grace of God has appeared that offers salvation to all people.' The word 'appeared' (<em>epephanē</em>) — the same root as <em>epiphaneia</em> (appearing, epiphany) — was the standard Hellenistic vocabulary for the arrival of a divine being in the world: the gods appeared (<em>epiphanē</em>) in cultic apparitions, oracles, and divine rescue events. The Hellenistic ruler-cult applied the same language to the arrival of a king or emperor in a city: the emperor's <em>epiphaneia</em> was celebrated with festivals, coins, and inscriptions. Paul deliberately deploys this loaded vocabulary to proclaim that the true divine epiphany — superior to any imperial arrival — has occurred in the Incarnation. 'To all people' (<em>pasin anthrōpois</em>) makes the universal scope explicit: not the epiphany of a local deity for its cultic community, or the imperial epiphany for Roman citizens, but the appearance of divine grace for all humanity without ethnic or social distinction.</p>",

    "12": "<p>'It teaches us to say no to ungodliness and worldly passions, and to live self-controlled, upright and godly lives in this present age.' The 'two-age' schema — this present age (<em>nun aiōni</em>) and the coming age — is the fundamental framework of Jewish eschatology, rooted in the prophets' expectation of a future transformation of the world. The present age is characterized by sin, suffering, and the dominion of worldly powers; the coming age is the new creation in which God's kingdom is fully established. In the NT, the new age has been inaugurated by Christ's resurrection (it has 'appeared' already in the epiphany of grace, v. 11) but the present age continues: Christians live at the overlap of the two ages, governed by the power of the inaugurated kingdom while still inhabiting the structures of the present age. The triad 'self-controlled, upright and godly' (<em>sōphronōs kai dikaiōs kai eusebōs</em>) maps exactly onto the three relationships that structure ancient moral philosophy: self-control governs one's relation to oneself, uprightness governs relations with other people, and godliness governs relation to God.</p>",

    "13": "<p>'While we wait for the blessed hope — the appearing of the glory of our great God and Savior, Jesus Christ.' The 'appearing' (<em>epiphaneia</em>) here is the second and final epiphany — the eschatological arrival of Christ in glory, contrasted with the first epiphany of grace (v. 11). The Roman imperial epiphany-theology reached its apogee in the emperor's triumphal arrival (<em>parousia</em>) at a city: the city would send a delegation out to meet the emperor, escort him in, and celebrate his presence. The NT deliberately deploys both <em>parousia</em> (arrival) and <em>epiphaneia</em> (appearing) for Christ's return, subverting the imperial theology by applying its highest categories to Jesus rather than Caesar. The disputed phrase 'our great God and Savior, Jesus Christ' (<em>tou megalou theou kai sōtēros hēmōn Iēsou Christou</em>) is grammatically most naturally read as applying both 'God' and 'Savior' to Jesus — a high Christological claim made more striking by its use of language (great god, savior) that was applied to Hellenistic rulers and gods.</p>",

    "14": "<p>'Who gave himself for us to redeem us from all wickedness and to purify for himself a people that are his very own, eager to do what is good.' The phrase 'a people that are his very own' (<em>laon periousios</em>) is the LXX translation of the Hebrew <em>am segullah</em> (treasured possession) in Exod 19:5 — God's covenant declaration at Sinai: 'you will be my treasured possession.' By applying the Exodus covenant-language to the community formed by Christ's self-giving, Paul presents the church as the new Israel constituted not by Torah-keeping but by the Messiah's redeeming act. 'Redeem' (<em>lytrōsētai</em>) uses the vocabulary of the slave-market (buying free a slave) and the Exodus (God's ransom of Israel from Egypt, Exod 6:6; Deut 7:8) — both resonances apply: Christ ransoms his people from the slavery of lawlessness and leads them in a new Exodus into community with God.</p>",

    "15": "<p>'These, then, are the things you should teach. Encourage and rebuke with all authority. Do not let anyone despise you.' Titus's authority in Crete was precarious: he was not the founder of the Cretan churches, and he was a delegate rather than a resident apostle — his mandate was temporary and his authority delegated. The instruction 'do not let anyone despise you' (<em>mēdeis sou perifroneitō</em>) reflects the challenge of exercising authority in a community where one's personal standing has not been established by long relationship. In ancient Mediterranean honor-culture, authority derived from recognized social status, kinship, or demonstrated competence: an outsider exercising authority in a community risked being dismissed as overreaching. Paul's instruction is that Titus must speak and act with the full weight of apostolic commission — his authority is not his own but Paul's, and behind Paul's, God's.</p>"
  },

  "3": {
    "1": "<p>'Remind the people to be subject to rulers and authorities, to be obedient, to be ready to do whatever is good.' The Roman provincial government of Crete (established as a Roman province in 67 BCE after Pompey's conquest) was administered by a proconsul appointed by the Senate. Roman provincial life involved constant interaction with civic institutions: the collection of taxes, enforcement of local laws, mandatory civic religious ceremonies, and participation in the imperial cult. The early church's counter-cultural character — meeting in private households, rejecting the gods, claiming a king other than Caesar — created regular suspicion of civic disloyalty. Paul's instruction to submit to civic authorities echoes Rom 13:1-7 and 1 Pet 2:13-17: the church's political stance is not revolutionary resistance but engaged civic cooperation, demonstrating that Christians are model citizens even while their ultimate loyalty is to a different king.</p>",

    "2": "<p>'To slander no one, to be peaceable and considerate, always to be gentle toward everyone.' The virtue <em>epieikēs</em> (considerate, gentle, equitable) was one of the prized political virtues in Hellenistic ethics — Aristotle devoted a section of the <em>Nicomachean Ethics</em> (5.10) to it as the quality that corrects the harshness of strict legal justice: the <em>epieikēs</em> person knows when to apply the spirit of the law rather than the letter. In the political context, it marked the ruler or magistrate who was not tyrannically rigid but humanly responsive. The instruction to be peaceable (<em>amachous</em>, non-combative) directly contrasts with the combativeness of the false teachers (1:9 — 'refute those who oppose it'; 3:9-11 — 'avoid foolish controversies'): the Christian community's engagement with the wider world is characterized by gentleness, not the rhetorical warfare of philosophical schools.</p>",

    "3": "<p>'At one time we too were foolish, disobedient, deceived and enslaved by all kinds of passions and pleasures. We lived in malice and envy, being hated and hating one another.' The pre-conversion catalogue is a standard feature of Pauline paraenesis (ethical instruction), functioning as a <em>before-and-after</em> contrast that grounds the ethical instruction in the radical transformation of conversion (cf. 1 Cor 6:11 — 'And that is what some of you were... but you were washed'). The vices listed — foolishness, disobedience, deception, passion-enslavement, malice, envy, hatred — map onto the Stoic and Platonic analysis of the unphilosophical life: reason enslaved to passion rather than governing it. The first-person plural 'we' (including Paul himself) is rhetorically significant: it places the author and his readers on the same footing, undermining any self-righteous attitude toward the world outside the church and grounding the call to gentleness (v. 2) in the memory of one's own prior condition.</p>",

    "4": "<p>'But when the kindness and love of God our Savior appeared...' <em>Chrēstotēs</em> (kindness, benevolence) and <em>philanthropia</em> (love of humanity, philanthropy) were the standard Hellenistic vocabulary for the benevolent concern of a good ruler for his subjects. <em>Philanthropia</em> was a technical political term: the ideal king's care for his people expressed through gifts, games, building projects, and just administration — the Roman emperors were regularly praised for their <em>philanthropia</em>. By attributing both terms to God ('our Savior'), Paul appropriates the highest vocabulary of Hellenistic political theology and applies it to the divine act of salvation: the true <em>philanthropia</em> is not an emperor's games but God's sending of his Son. The 'appearance' (<em>epephanē</em>) again evokes the epiphany-theology of divine or royal arrival — the Incarnation as God's definitive act of benevolent royal intervention in human history.</p>",

    "5": "<p>The 'washing of regeneration and renewing of the Holy Spirit' (<em>loutron palingenesias kai anakainōseōs Pneumatos Hagiou</em>) combines Jewish purification-immersion imagery (<em>mikveh</em>) with the OT new-covenant Spirit-promise (Ezek 36:25-27; Joel 2:28-29). <em>Palingenesia</em> (regeneration/new birth) appears only here and Matt 19:28 (the renewal of all things at the eschatological restoration) in the NT — linking individual new birth with cosmic new creation. <em>Palingenesia</em> was also a Stoic term for the cyclical renewal of the cosmos after the ekpyrosis (cosmic fire) — Paul's use may deliberately appropriate the Stoic vocabulary and fill it with Christological content: the Spirit's renewal is the eschatological new creation arriving in individual conversion.</p>",

    "6": "<p>'Whom he poured out on us generously through Jesus Christ our Savior.' The language of the Spirit 'poured out' (<em>execheen</em>) deliberately echoes the Pentecost event (Acts 2:17-18, quoting Joel 2:28-29: 'I will pour out my Spirit on all people') and the OT promise of the eschatological Spirit-outpouring. The Spirit is not merely given but 'poured out generously' (<em>plousiōs</em>, abundantly, richly) — the divine gift without measure (cf. John 3:34 — 'God gives the Spirit without limit'). The Trinitarian structure of the passage is precise: God the Savior saves (v. 5) by the washing of regeneration and renewing of the Spirit (v. 5), whom he poured out through Jesus Christ our Savior (v. 6) — Father, Spirit, and Son each active in a single saving event. This is one of the NT's most compressed Trinitarian soteriology statements.</p>",

    "7": "<p>'So that, having been justified by his grace, we might become heirs having the hope of eternal life.' The legal-relational term 'justified' (<em>dikaiōthentes</em>) — declared righteous by a judicial verdict — is the courtroom image Paul uses in Romans and Galatians for God's act of accepting sinners through the gospel. 'Heirs' (<em>klēronomoi</em>) adds the testamentary language of Roman inheritance law: the <em>klēronmos</em> (heir) receives the full estate of the deceased. In Roman law, adoption (<em>adoptio</em>) was a formal legal act that made a non-biological child the heir with full rights; Paul's theology of adoption (huiothesia) regularly draws on this Roman legal reality. To be 'justified' is to be declared innocent; to be made 'heirs' is to be given a share in God's estate — the two images together describe both the forensic and the relational dimensions of salvation.</p>",

    "8": "<p>'This is a trustworthy saying. And I want you to stress these things, so that those who have trusted in God may be careful to devote themselves to doing what is good.' 'Trustworthy saying' (<em>pistos ho logos</em>) is a formula that appears five times in the Pastoral Epistles (1 Tim 1:15, 3:1, 4:9; 2 Tim 2:11; Titus 3:8) — a marker that the preceding statement carries the weight of a confessional formula or credal affirmation. The phrase suggests that the Trinitarian-soteriological statement of vv. 4-7 may have been a recognized liturgical or catechetical formulation in the early churches, which Paul cites and endorses. The instruction to 'devote themselves to doing what is good' (<em>proistasthai kalōn ergōn</em>, literally 'to be foremost in good works') grounds the entire letter's ethical instruction in the theological reality of v. 7: justified heirs of eternal life express their new status through the productive energy of good works — not to earn salvation but as its natural fruit.</p>",

    "9": "<p>'But avoid foolish controversies and genealogies and arguments and quarrels about the law, because these are unprofitable and useless.' 'Genealogies' (<em>genealogiai</em>) in this context likely refers to the elaborate speculative traditions in Second Temple Judaism that traced the ancestry and descent of biblical figures — traditions that generated extensive midrashic elaboration (the Book of Jubilees recounts biblical history in terms of Jubilee-periods and genealogical sequences; 1 Chronicles was mined for genealogical speculation). 'Quarrels about the law' (<em>machas nomikas</em>) points to the halakhic debates among Jewish-Christian teachers — arguments about which Torah commands were binding on Gentiles, how the sabbath should be observed, and what the 'works of the law' required. Paul's instruction to avoid these is not anti-intellectual but strategic: the controversies are 'unprofitable' (<em>anōpheleis</em>) because they divide the community and distract from the practical ethics of v. 8.</p>",

    "10": "<p>'Warn a divisive person once, and then warn him a second time. After that, have nothing to do with him.' <em>Hairetikon anthrōpon</em> (a divisive person, a faction-maker) — the word from which 'heresy' is derived (<em>hairesis</em>: a sect or party) — in its original Greek sense meant simply someone who chooses a particular position or forms a partisan group. In the context of the early church, the problem was not primarily doctrinal heterodoxy in the later sense but communal division — the formation of factions around rival teachers that fractured the household-church community. The two-warning protocol before complete social exclusion reflects a structured pastoral procedure: the first warning gives opportunity for reflection, the second confirms the pattern, and rejection of both demonstrates that the person is not open to correction and is actively choosing division over community.</p>",

    "11": "<p>'You may be sure that such people are warped and sinful; they are self-condemned.' <em>Autokatakritos</em> (self-condemned) — a hapax legomenon (found only here in the NT) — expresses the Stoic concept that the person whose reasoning is corrupted condemns themselves by their own internal logic: they know what right conduct is (the two warnings have made this explicit) and have rejected it, making their own reasoning the instrument of their condemnation. The word 'warped' (<em>exestraptai</em>, literally 'turned inside out') uses the imagery of a distorted or perverted thing — the divisive person's moral reasoning has been inverted, choosing faction over truth. This theological judgment (they are 'sinful', <em>hamartan&#333;n</em>, a present participle indicating ongoing action) grounds the community's exclusion of the divisive person not in social preference but in the recognition that continued engagement enables rather than corrects the sin.</p>",

    "12": "<p>'As soon as I send Artemas or Tychicus to you, do your best to come to me at Nicopolis, because I have decided to winter there.' Nicopolis ('City of Victory') was founded by Augustus to commemorate his decisive naval victory over Antony and Cleopatra at the Battle of Actium in 31 BCE — the battle that made Augustus sole ruler of the Roman world. The city was built on the promontory of Epirus overlooking the site of the battle, settled with veterans, and made a major administrative center for northwestern Greece. It was positioned on the Via Egnatia (the road connecting Rome to the East) and the Adriatic coast, making it an ideal winter base for travel between Italy and the eastern Mediterranean. Wintering was a practical necessity in antiquity: sea travel became dangerous or impossible from mid-November to mid-March, requiring travelers to establish a fixed base for the winter months.</p>",

    "13": "<p>'Do everything you can to help Zenas the lawyer and Apollos on their way and see that they have everything they need.' Zenas is otherwise unknown — the name is Latin (possibly short for Zenodorus), and 'the lawyer' (<em>nomikos</em>) may indicate either a Roman legal expert (<em>iurisperitus</em>) trained in Roman law, or a Jewish legal scholar (<em>sofer</em>, Torah-expert, the regular NT usage of <em>nomikos</em>). Apollos is the well-known Alexandrian Jewish Christian of Acts 18:24-28 and 1 Corinthians (where factional attachment to Apollos is one of Paul's concerns, 1 Cor 1:12). That Apollos appears here as a co-worker of Paul and Titus — without any hint of the Corinthian rivalry — suggests the tensions in 1 Corinthians had been resolved and the Alexandrian was now fully integrated into the Pauline mission network. The instruction to 'send them on their way' (<em>propempson</em>) is the technical term for providing traveling companions, supplies, and letters of introduction for apostolic emissaries.</p>",

    "14": "<p>'Our people must learn to devote themselves to doing what is good, in order to provide for urgent needs and not live unproductive lives.' The repetition of 'doing what is good' (<em>kalōn ergōn</em>) — already stated in v. 8 — frames the conclusion of the letter with the practical telos that has governed the entire instruction. 'Urgent needs' (<em>anagkaias chreias</em>) is probably a deliberate reference to the traveling missionaries mentioned in v. 13 (Zenas and Apollos need provisions) and more generally to the economic support of the apostolic network. Ancient churches operated as patronage networks: wealthier members provided hospitality, travel funds, and material support for itinerant workers. The instruction that 'our people' — the Cretan Christians collectively — must learn productive engagement with good works connects the theological argument of vv. 4-7 (God's grace makes us heirs) with the practical community life of v. 14 (heirs express their inheritance through generosity and productive good works).</p>",

    "15": "<p>'Everyone with me sends you greetings. Greet those who love us in the faith. Grace be with you all.' The closing greeting establishes the communal nature of the Pastoral Epistles: despite being addressed to an individual (Titus), the letter was intended for public reading in the assembled community — 'you all' (<em>pantōn hymōn</em>) is plural. Ancient letters were typically read aloud in the recipient's presence to all gathered; a letter to a community leader functioned as a letter to the community. The phrase 'those who love us in the faith' (<em>tous philountas hēmas en pistei</em>) acknowledges the network of personal relationships that held the early church together across geographical distance — the bonds of Christian friendship and loyalty in the shared commitment to the gospel. The final word 'grace' (<em>charis</em>) closes the letter with the same divine gift that opened it (1:4 — 'Grace and peace') and was proclaimed as its theological center (2:11 — 'the grace of God has appeared').</p>"
  }
}

TITUS_CHRIST = {
  "2": {
    "14": "<p>A direct revelation: 'Who gave himself for us to redeem us from all lawlessness and to purify for himself a people of his own possession who are zealous for good works.' The Christological mission-statement of Titus: the self-giving of Christ (<em>edōken heauton</em>) accomplishes two things — ransom from lawlessness and purification-for-possession. The people-of-God language (laos periousios = treasured possession, Exod 19:5) is deliberately applied to the new covenant community formed by Christ's self-gift. Christ does not merely save individuals but creates a community that embodies his purposes — 'zealous for good works' completes the Christological transaction with an ethical telos.</p>"
  },
  "3": {
    "4": "<p>A direct revelation: 'But when the goodness and loving kindness of God our Savior appeared, he saved us, not because of works done by us in righteousness, but according to his own mercy, by the washing of regeneration and renewing of the Holy Spirit.' The 'appearance' (<em>epephanē</em>) of God's goodness is the Incarnation — the divine character made visible in Jesus. The Christological-Trinitarian movement: God the Savior's goodness appeared → he saved by mercy (not merit) → through the washing of the Spirit → poured out richly through Jesus Christ our Savior. The threefold divine action (God, Spirit, Christ) grounds salvation entirely outside human achievement.</p>"
  }
}

# ============================================================
# PHILEMON
# ============================================================

PHILEMON_ECHO = {
  "1": {
    "16": [
      {"type": "allusion", "target": "Lev 19:34", "note": "No longer as a slave but more than a slave, as a dear brother — the Levitical command to treat the alien among you as the native; the Onesimus-Philemon relationship after conversion exceeds the Torah's ethnic solidarity by requiring brotherly love between master and enslaved person"},
      {"type": "allusion", "target": "Deut 23:15-16", "note": "Receive him no longer as a slave but as a dear brother — Deuteronomy's command not to return a runaway slave to his master but to let him dwell wherever he chooses; Paul's appeal works within Roman law while nudging toward a more radical Christian brotherhood that subverts the institution"}
    ]
  }
}

PHILEMON_ORIGINAL = {
  "1": {
    "16": "<p><strong>ouketi hos doulon alla hyper doulon adelphon agapeton</strong> (<em>ouketi hōs doulon alla hyper doulon, adelphon agapēton</em>): 'no longer as a slave but more than a slave, as a dear brother.' The grammatical structure — <em>ouketi ... alla hyper</em> (no longer ... but beyond) — expresses a qualitative transformation, not just a label change. Onesimus remains in a social relationship with Philemon but that relationship is now defined by a different primary category: <em>adelphos agapētos</em> (beloved brother). Paul does not directly command emancipation, but the logic of brotherhood makes slavery an anomaly: how can you own your brother? The letter is the most politically charged use of household-code language in Paul — Christian kinship (<em>adelphos</em>) is placed in deliberate tension with Roman social institution (<em>doulos</em>).</p>",

    "18": "<p><strong>ei de ti edikesen se e opheilei touto emoi ellogei</strong> (<em>ei de ti ēdikēsen se ē opheilei, touto emoi ellogei</em>): 'If he has wronged you at all or owes you anything, charge that to my account.' <em>Ellogei</em> (charge to my account / impute) is a commercial-accounting term used only here and Rom 5:13 (sin is not <em>ellogeitai</em> when there is no law) in the NT. Paul offers to absorb Onesimus's debt as a surety. The theological parallel is explicit in the letter's rhetoric: as Paul stands in for Onesimus absorbing his debt-liability, Christ stands in for sinners absorbing their debt before God. Philemon is the NT's most compressed illustration of imputed righteousness in a human-relational register.</p>"
  }
}

PHILEMON_CONTEXT = {
  "1": {
    "10": "<p>Onesimus was enslaved in Philemon's household in Colossae (cf. Col 4:9: 'Onesimus, our faithful and dear brother, who is one of you'). The traditional reading: Onesimus ran away from Philemon, somehow encountered Paul in prison (Rome or Ephesus), was converted, and is now being returned. A minority reading (B. Winter, A. Callahan): Onesimus was sent by Philemon to assist Paul in prison (a known practice, cf. Phil 2:25-30 — Epaphroditus sent to serve Paul), and Paul now appeals for him to be released permanently for gospel ministry. Either way, the letter navigates Roman slave-law (the <em>Lex Petronia</em> of ca. 61 CE and related legislation governed runaways) while applying theological pressure through the rhetoric of Christian brotherhood.</p>",

    "16": "<p>Roman slavery in the first century CE: approximately 1-2 million enslaved people in Italy alone (roughly 30-35% of the Italian population, Scheidel's estimate); enslaved persons could be freed by manumission (<em>manumissio</em>) through various legal mechanisms. Freed persons became Roman citizens with some legal restrictions. The distinction Paul makes — 'both in the flesh and in the Lord' — is the Christian social ontology: Onesimus has both a new spiritual identity (brother in Christ) and an unchanged social location (in Philemon's household). Paul does not directly call for legal manumission, but the category 'dear brother' both in the flesh and in the Lord strains against the institution's dehumanizing premise.</p>"
  }
}

PHILEMON_CHRIST = {
  "1": {
    "17": "<p>A revelation of God: 'If you consider me your partner, receive him as you would receive me.' Paul's intercession for Onesimus reveals a pattern of representative substitution: the apostle places himself in the position of the offender and asks to be treated as Onesimus's surety. This is not strictly a direct Christological statement, but Paul consciously patterns his intercession on the Christological movement of divine advocacy — as Christ stands for sinners before the Father, Paul stands for Onesimus before Philemon. The letter reveals the social logic of atonement-theology as it should reshape human relationships.</p>",

    "18": "<p>A direct revelation: 'If he has wronged you at all, or owes you anything, charge that to my account.' The imputation-language (<em>ellogei</em>) makes this the most concrete illustration in the NT of the substitutionary logic that governs Paul's soteriology. The Christ-event logic: Christ receives the charge of our debt against God's account; Paul enacts this same logic with Onesimus's debt to Philemon. The atonement is not merely a doctrinal formula but a relational pattern that should generate analogous acts of substitutionary absorption of another's debt. Philemon is called to receive Onesimus 'as you would receive me' (v. 17) — Christ-likeness enacted in the ordinary economy of first-century household relationships.</p>"
  }
}

def main():
    books = [
        ('1timothy', ONETIM_ECHO, ONETIM_ORIGINAL, ONETIM_CONTEXT, ONETIM_CHRIST),
        ('2timothy', TWOTIM_ECHO, TWOTIM_ORIGINAL, TWOTIM_CONTEXT, TWOTIM_CHRIST),
        ('titus', TITUS_ECHO, TITUS_ORIGINAL, TITUS_CONTEXT, TITUS_CHRIST),
        ('philemon', PHILEMON_ECHO, PHILEMON_ORIGINAL, PHILEMON_CONTEXT, PHILEMON_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books:
        e = load_echo(book)
        merge_echo(e, echo_d)
        save_echo(book, e)

        c = load_comm('mkt-original', book)
        merge_comm(c, orig_d)
        save_comm('mkt-original', book, c)
        print(f'{book} original: {len(c)} chs, {sum(len(v) for v in c.values())} vs')

        c = load_comm('mkt-context', book)
        merge_comm(c, ctx_d)
        save_comm('mkt-context', book, c)
        print(f'{book} context: {len(c)} chs, {sum(len(v) for v in c.values())} vs')

        c = load_comm('mkt-christ', book)
        merge_comm(c, chr_d)
        save_comm('mkt-christ', book, c)
        print(f'{book} christ: {len(c)} chs, {sum(len(v) for v in c.values())} vs')

if __name__ == '__main__':
    main()
