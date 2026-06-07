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
    "1": "<p>The theme of the promise of life: Paul is 'an apostle of Christ Jesus by the will of God, in keeping with the promise of life that is in Christ Jesus.' The apostolic commission exists to announce this promise. The entire letter is oriented toward it: Paul faces death, but the life promised in Christ transcends that death. The commission is inseparable from the content — apostleship serves the promise of life in Christ Jesus.</p>",
    "2": "<p>The revelation of God in the double-sourced benediction: grace, mercy, and peace flow from 'God the Father and Christ Jesus our Lord' — Christ is co-source alongside the Father. This standard NT formula (repeated in 1 Tim 1:2; Titus 1:4) places Christ within the divine identity as the joint-giver of all covenantal blessing.</p>",
    "3": "<p>The revelation of God in gratitude and prayer: Paul thanks the God he serves 'with a clear conscience' while constantly praying for Timothy. Prayer is directed to the God who stands behind both Paul's calling and Timothy's continuation in it. The conscience clear before God (the same standard as 1 Tim 1:5, 19) is the fruit of ministry oriented around the gospel of Christ.</p>",
    "4": "<p>The theme of longing for fellowship: the tears Paul recalls and the joy he anticipates in reunion reflect the covenantal depth of the relationship between Paul and Timothy, shaped by their shared participation in Christ. As Christ prayed for his own to be with him (John 17:24), the fellowship of the new-covenant community is marked by longing for presence with those who share the same Lord.</p>",
    "5": "<p>The revelation of God in generational faith: Lois and Eunice are the soil in which Timothy's 'sincere faith' grew. Faith is not self-generated but transmitted — coming from hearing (Rom 10:17), and God works through human networks of testimony. The faith that Timothy now exercises is the same faith that his grandmother and mother exercised — continuous, genuine, uncounterfeit (<em>anupokritou</em>).</p>",
    "6": "<p>The theme of the Spirit-given gift maintained through apostolic commission: the charism in Timothy, given through the laying on of Paul's hands, is to be fanned into flame. The same Spirit who anointed Christ at his baptism (Luke 3:22) distributes gifts through commissioned ministers. The gift can diminish if neglected — not because the Spirit withdraws but because the human recipient fails to tend it.</p>",
    "7": "<p>The revelation of God: 'the Spirit God gave us does not make us timid, but gives us power, love and self-discipline.' The Spirit's three gifts (power, love, self-discipline) are the character of the risen Christ made available in the believer. The timidity that the Spirit does not give is the fear of suffering — which 2 Timothy addresses throughout. The Spirit transforms the minister into conformity with the crucified-and-risen Lord who endured suffering in love.</p>",
    "8": "<p>The theme of suffering as participation in Christ: 'join with me in suffering for the gospel, by the power of God.' To suffer for the gospel is to share in Christ's own suffering (Phil 3:10). The power that enables this suffering is resurrection-power — the same power that raised Christ (Eph 1:19-20) is the power that sustains endurance in his servants. Suffering for Christ is not exceptional but structural to ministry between the two appearances.</p>",
    "9": "<p>A direct revelation: 'This grace was given us in Christ Jesus before the beginning of time.' Pre-temporal election: saving grace was determined and given in Christ before the ages began, as part of God's eternal purpose. This is the deepest Christological foundation of salvation — it precedes creation, history, and human choice. The call to holiness and the gift of grace are both located in Christ Jesus, not in human achievement.</p>",
    "10": "<p>A direct revelation: 'Our Savior Christ Jesus abolished death and brought life and immortality to light through the gospel.' The Christological declaration concentrates the gospel: Christ 'abolished' (<em>katargēsantos</em>) death — not merely defeated it but rendered it inoperative; brought life and immortality 'to light' (<em>phōtisantos</em>) — these were previously hidden in God's eternal purpose (v. 9) but are now disclosed through the proclamation. The Christology of 2 Timothy: the epiphany of the Savior is the historical moment when death's power was broken and life was made publicly visible.</p>",
    "11": "<p>The theme of apostolic function as gospel-service: Paul was appointed herald, apostle, and teacher — all three roles defined by the content of vv. 9-10 (the grace given in Christ, now revealed through his appearing). Ministry derives its entire meaning from the Christological proclamation it serves. The three titles (herald, apostle, teacher) describe the same task from different angles: announcement, authorization, and explanation of the Christ-event.</p>",
    "12": "<p>The revelation of God in personal trust: 'I know whom I have believed, and am convinced that he is able to guard what I have entrusted to him until that day.' The certainty of Paul's faith rests not on his own endurance but on the person and competence of Christ — 'whom I have believed.' The same deposit-language (<em>parathēkē</em>) used of the gospel entrusted to Timothy is here applied to Paul's own life: Paul has deposited himself into Christ's keeping until the parousia.</p>",
    "13": "<p>The theme of the pattern of sound words: the standard of orthodoxy ('the pattern of sound teaching') is inhabited by 'faith and love in Christ Jesus' — doctrinal fidelity and relational virtue are inseparable in the Pastoral vision. The formal content (sound teaching) is only maintained by those who hold it in the manner Christ himself demonstrated: with faith and love.</p>",
    "14": "<p>The revelation of God in the Spirit's role as guardian: 'guard the good deposit with the help of the Holy Spirit who lives in us.' The preservation of the gospel-tradition is a Trinitarian act: the content is the gospel of Christ; the human steward is Timothy; the divine agent of preservation is the Holy Spirit. No human effort alone preserves the deposit — the Spirit who indwells the community is the ultimate guardian of the truth entrusted to it.</p>",
    "15": "<p>The revelation of God in abandonment: 'everyone in the province of Asia has deserted me.' Even in desertion the Lord remains faithful (contrast with 4:17: 'the Lord stood at my side'). The parallel with Christ's Gethsemane abandonment is implicit (Mark 14:50: 'they all left him and fled'). The abandoned apostle participates in the experience of the abandoned Messiah — and the same Lord who vindicated Christ will vindicate Paul.</p>",
    "16": "<p>The revelation of God: the Lord's mercy invoked on Onesiphorus's household. Those who minister to the suffering servant of Christ are honored by covenantal prayer for divine mercy. Onesiphorus's boldness in finding Paul 'in chains' — the shame of Roman imprisonment — without being ashamed (v. 16) mirrors the pattern of those who do not abandon Christ's suffering servants as the world might expect.</p>",
    "17": "<p>The theme of persistent seeking as covenant faithfulness: Onesiphorus 'searched hard for me until he found me.' The diligent seeking-until-found illustrates the parable logic of Luke 15 in the register of human loyalty. The minister's fidelity to suffering co-workers is one of the concrete expressions of the love that the gospel creates in those it transforms.</p>",
    "18": "<p>The revelation of God in eschatological mercy: 'May the Lord grant that he will find mercy from the Lord on that day.' The 'day' is the parousia — the moment of Christ's judgment. The Christological dimension: the mercy that Onesiphorus showed Paul will be remembered before the Lord who is the righteous judge (4:8). God's economy of grace reciprocates acts of covenant faithfulness with acts of eschatological mercy.</p>"
  },
  "2": {
    "1": "<p>The revelation of God in grace as the source of strength: 'be strong in the grace that is in Christ Jesus.' The strength for ministry is not Timothy's personal resolve but the grace dwelling in Christ Jesus and accessible through union with him. The grace that saved (1:9: grace given in Christ Jesus before the ages) also sustains for service — the same divine favor that initiated the relationship now enables its continuation.</p>",
    "2": "<p>The theme of apostolic succession in teaching: 'entrust to reliable people who will also be qualified to teach others.' The chain (Paul → Timothy → reliable teachers → others) is the human mechanism of gospel transmission. Ultimately preservation is God's work (1:12), but it operates through this network of commissioned teachers who have both received and embodied the content they pass on.</p>",
    "3": "<p>The theme of solidarity in suffering as discipleship: 'join with me in suffering, like a good soldier of Christ Jesus.' The soldier metaphor defines ministry as absolute loyalty to Christ the commanding officer, which necessarily involves sharing in the suffering of the crucified Lord. The soldier suffers not as an aberration but as the expected mode of service to a Lord whose own path was through suffering to glory.</p>",
    "4": "<p>The theme of undivided allegiance to the commanding officer: 'no one serving as a soldier gets entangled in civilian affairs, but rather tries to please his commanding officer.' The commanding officer is Christ — ministry is oriented entirely toward pleasing him, not managing civilian opinion or comfort. The Christological frame: the minister who is distracted by peripheral concerns cannot give the whole-hearted service that Christ's commission requires.</p>",
    "5": "<p>The theme of the athlete's crown as eschatological reward: 'anyone who competes as an athlete does not receive the victor's crown except by competing according to the rules.' The victor's crown anticipates 4:8 (the crown of righteousness). Legitimate striving according to the gospel's norms — enduring in truth, not taking shortcuts — is the path to the eschatological prize that Christ the righteous judge will award.</p>",
    "6": "<p>The theme of the hardworking farmer receiving the harvest first: the agricultural metaphor in a Christological key — the present suffering of faithful ministry corresponds to sowing; the eschatological reward corresponds to harvest. Jesus's agricultural parables (the sower, Mark 4) and his promise of a hundredfold return for those who leave all to follow him (Mark 10:29-30) underlie this figure of patient labor and future fruit.</p>",
    "7": "<p>The revelation of God in divine illumination: 'the Lord will give you insight into all this.' The three metaphors (soldier, athlete, farmer) require Spirit-given wisdom to apply to the minister's concrete situation. The Lord's gift of insight is the same illuminating work that enables Timothy to rightly handle the word of truth (2:15). Reflection on metaphor and application to life are both divinely enabled.</p>",
    "8": "<p>A direct revelation: 'Remember Jesus Christ, risen from the dead, the offspring of David, as preached in my gospel.' Paul's summary of the gospel in one sentence unites the two great OT streams: Davidic messiahship (the royal covenant of 2 Sam 7) and resurrection (the prophetic expectation of Isa 26:19; Dan 12:2). 'Remember' (<em>mnemoneue</em>) is imperative — not a passive recollection but an active, sustaining focus on the Christological fact that generates Paul's willingness to suffer. The risen Davidic Christ is the content of endurance.</p>",
    "9": "<p>The theme of the unchained word: 'I am suffering even to the point of being chained like a criminal. But God's word is not chained.' The power of the gospel is independent of the freedom of its human messengers. The Christological parallel: Christ was executed as a criminal, yet his death became the power of God for salvation (1 Cor 1:18). The imprisonment of the apostle, like the death of Christ, does not arrest the word's saving power.</p>",
    "10": "<p>A direct revelation: 'that they too may obtain the salvation that is in Christ Jesus, with eternal glory.' The soteriological scope of Paul's endurance: his suffering serves the elect, so that those God has chosen will hear the gospel and be saved. The salvation is specifically 'in Christ Jesus' — located in union with him, not in apostolic effort as such. 'Eternal glory' is the eschatological completion of a salvation that begins now and ends in the full revelation of Christ's glory.</p>",
    "11": "<p>A direct revelation: 'If we died with him, we will also live with him.' The first clause of the faithful saying: baptismal dying-with-Christ (Rom 6:3-8) guarantees resurrection-living-with-Christ. The conditional form is not uncertain but illustrative: the dying-with is the ground; the living-with is the guaranteed result. The union with Christ in death produces union with Christ in life — the two are inseparable.</p>",
    "12": "<p>A direct revelation: 'if we endure, we will also reign with him.' Endurance as the path to co-reign: the promise of Rev 2:26-27 (authority over the nations to the one who overcomes) and Luke 22:29-30 (a kingdom assigned to those who have remained with Christ in his trials). The alternative clause — 'if we disown him, he will also disown us' — quotes Jesus's own warning (Matt 10:33), making apostasy a Christological contradiction: to disown the one who gave himself is to be disowned by the one who judges.</p>",
    "13": "<p>A direct revelation: 'if we are faithless, he remains faithful, for he cannot disown himself.' The unconditional Christological ground beneath all the conditional clauses: Christ's faithfulness is not contingent on human faithfulness. He cannot be false to himself — his character (faithful, 2 Tim 2:2; Rev 19:11) is self-consistent. This is not a license for apostasy but the theological foundation beneath endurance: the believer's continuation rests finally on Christ's self-consistency, not their own strength.</p>",
    "14": "<p>The theme of all teaching as coram Deo: 'Warn them before God against quarreling about words.' The divine presence witnesses all instruction and debate. The Christological dimension: all teaching occurs before the face of God and of Christ the coming Judge (4:1). The quarreling about words that Paul prohibits is judged by the standard of whether it serves or undermines the proclamation of Christ.</p>",
    "15": "<p>The theme of correct handling of the word of truth: the word of truth is the gospel of Christ (Eph 1:13: the word of truth, the gospel of your salvation). Correct handling requires knowing and applying the Christological content accurately — cutting it straight (orthotomounta) rather than twisting it toward controversy. The worker approved before God is the one whose exposition serves the gospel's saving intent.</p>",
    "16": "<p>The revelation of God in the trajectory of godless speech: those who indulge in godless chatter 'will become more and more ungodly.' The direction of false teaching is away from Christ — the pattern of godliness revealed in Christ and reproduced by the Spirit — and toward the self-directed chaos of the last days (3:1-9). True speech about Christ produces godliness; godless speech corrodes it.</p>",
    "17": "<p>The revelation of God in the medical metaphor: 'Their teaching will spread like gangrene.' What grows determines whether the result is life or death. The false teaching of Hymenaeus and Philetus is specifically about the resurrection (v. 18) — denying the future-bodily reality that is the Christological ground of all hope. False resurrection-doctrine is particularly lethal because it cuts the cord between Christ's resurrection and the believer's hope.</p>",
    "18": "<p>The revelation of God in resurrection-denialism: 'they say that the resurrection has already taken place.' Against the realized-eschatology position that the resurrection is already complete (spiritual or metaphorical), the entire Christological argument of 2 Timothy insists on future bodily resurrection: the risen Christ (2:8) is the firstfruits (1 Cor 15:23) whose resurrection guarantees and precedes the believers' future resurrection. To deny the future resurrection is to deny the meaning of Christ's own raising.</p>",
    "19": "<p>A direct revelation: 'The Lord knows those who are his' (Num 16:5). The firm foundation stands inscribed with two texts: God's sovereign knowledge of his elect (the Korah narrative — YHWH distinguishes the true from the false in Israel), and the covenantal obligation that follows (everyone who confesses the Lord's name turns from wickedness). Divine election and human accountability are both inscribed on the foundation — the one who knows his own calls them to holiness.</p>",
    "20": "<p>The theme of the large house with vessels of different use: the household (<em>oikos</em>) is the church — the household of God (1 Tim 3:15). The Master of the house is Christ — the <em>despotēs</em> who determines what use he makes of his vessels. Those who cleanse themselves from dishonorable use become instruments made ready for the Master's purposes — available for whatever service the Lord requires.</p>",
    "21": "<p>The theme of prepared holiness for Christ's service: 'made holy, useful to the Master and prepared to do any good work.' The holiness-and-usefulness pattern recurs across the Pastoral Epistles (Titus 2:14; Eph 2:10: created in Christ Jesus for good works). Those whom Christ has cleansed become available for the comprehensive service of the kingdom — 'prepared to do any good work' is the telos of redemption.</p>",
    "22": "<p>The revelation of God: 'pursue righteousness, faith, love and peace, along with those who call on the Lord out of a pure heart.' The phrase 'call on the Lord' quotes Joel 2:32 (everyone who calls on the name of YHWH will be saved) as applied to Christ in Rom 10:13. The community of those who call on the Lord is the new-covenant assembly gathered around the risen Christ — and Timothy is called to pursue the virtues of that community together with them, not in isolation.</p>",
    "23": "<p>The revelation of God in the fruitlessness of foolish controversy: 'foolish and stupid arguments produce quarrels.' The Christological standard: genuine ministry produces peace, salvation, and edification; these quarrels produce nothing. The contrast with the fruitfulness of patient instruction (vv. 24-25) — which can lead opponents to repentance — underscores that only the Spirit-enabled, gospel-oriented engagement bears fruit.</p>",
    "24": "<p>The theme of the Lord's servant shaped by the Lord's character: 'the Lord's servant must not be quarrelsome but must be kind to everyone, able to teach, not resentful.' The profile of the Lord's servant is shaped by Christ himself: 'I am gentle and humble in heart' (Matt 11:29). The minister who represents Christ in his manner and method, not merely his message, embodies the Lord's own approach to those he came to save.</p>",
    "25": "<p>The revelation of God in repentance as divine gift: 'in the hope that God will grant them repentance leading them to a knowledge of the truth.' Repentance is God's gift (Acts 11:18: God has granted repentance that leads to life), not the outcome of rhetorical success. The minister instructs gently while trusting the divine power — through the Spirit's work — to effect the change of mind that opens the door to saving knowledge of Christ.</p>",
    "26": "<p>The revelation of God in captivity-release: 'escape from the trap of the devil, who has taken them captive to do his will.' The Christological background: Christ came to destroy the works of the devil (1 John 3:8) and to release those held in captivity to the fear of death (Heb 2:14-15). The repentance of v. 25 is the mechanism through which those the devil has captured are released into the freedom of the gospel — a liberation accomplished by Christ and mediated through patient instruction.</p>"
  },
  "3": {
    "1": "<p>The theme of the last days as the present age: 'in the last days there will be terrible times.' The eschatological framework of 2 Timothy: the perilous times of moral collapse characterize the period between Christ's first and second appearance. The 'last days' began at Pentecost (Acts 2:17: 'in the last days I will pour out my Spirit') and intensify toward the Parousia — Timothy lives in these days now, not in a distant future.</p>",
    "2": "<p>The revelation of God in the anatomy of idolatry: the catalogue of vices (lovers of themselves, lovers of money, proud...) is the inversion of the Christ-character — 'who did not please himself' (Rom 15:3), who 'emptied himself' (Phil 2:7), who 'did not count equality with God a thing to be grasped' (Phil 2:6). The last-days moral collapse is characterized by the self-directed worship that properly belongs to the triune God.</p>",
    "3": "<p>The revelation of God in relational breakdown: the accumulation of relational vices (without love, unforgiving, slanderous, without self-control, brutal...) is the structural opposite of the love Christ commands and embodies (John 13:34-35). These vices mark the collapse of the relational fabric that Christ's new commandment was designed to create. Where Christ-shaped love retreats, these vices fill the vacuum.</p>",
    "4": "<p>The revelation of God in the either/or of devotion: 'lovers of pleasure rather than lovers of God.' The contrast echoes Jesus's teaching on two masters — you cannot love pleasure and love God simultaneously (Matt 6:24). True love is directed toward God, expressed through love of neighbor, and modeled in Christ's own self-giving. The last-days person has inverted this order: pleasure displaces God as the organizing center of the self.</p>",
    "5": "<p>The revelation of God in empty religion: 'having a form of godliness but denying its power.' The 'power' of godliness is the transforming presence of the Spirit through the gospel of Christ (Rom 1:16). Denying this power means denying the Christological content that gives godliness its transformative capacity — accepting the external form of religion while evacuating its life-giving center. This is the ecclesiastical form of the broader rejection of the gospel.</p>",
    "6": "<p>The revelation of God in predatory false teaching: the teachers exploit 'gullible women loaded with sins and swayed by all kinds of evil desires.' This is the inversion of Christ's ministry — Jesus sought the vulnerable and sinful in order to heal and free them (Luke 7:37-50; John 4; 8:1-11). The false teachers exploit vulnerability where Christ healed it; they increase the burden of sin where Christ removed it.</p>",
    "7": "<p>The theme of perpetual learning without arriving at truth: 'always learning but never able to come to a knowledge of the truth.' The Pastoral Epistles' saving knowledge (epignōsis alētheias) is specifically Christological — the truth that Timothy knew from infancy is the truth that leads to salvation through faith in Christ Jesus (3:15). Perpetual learning without arriving at this knowledge is the symptom of teaching that lacks the Christological center that is itself the truth (John 14:6: I am the truth).</p>",
    "8": "<p>The revelation of God in the pattern of opposition: Jannes and Jambres opposed Moses — God's appointed deliverer — as the false teachers oppose the apostolic truth. The pattern runs through Scripture: opposition to God's authorized mediators is opposition to the God who sent them (John 13:20: whoever receives the one I send receives me). Rejection of the apostolic gospel-tradition recapitulates the Egyptian magicians' opposition to YHWH's word.</p>",
    "9": "<p>The revelation of God in the self-exposure of falsehood: 'their folly will be clear to everyone.' The eschatological unveiling of hidden things (1 Cor 4:5: the Lord will bring to light what is hidden in darkness) operates partially in history (the magicians of Egypt were eventually exposed, Exod 8:18-19) and fully at the parousia. The confidence that error will be exposed is grounded in the character of the God who is himself truth.</p>",
    "10": "<p>The revelation of God in apostolic character as transparent witness: 'you know all about my teaching, my way of life, my purpose, faith, patience, love, endurance.' Paul presents himself not as the object of imitation for his own sake but as a transparency through which Christ's character is visible. The apostle's enumeration of virtues reflects the character of Christ (faithful, patient, loving, enduring) — Timothy is called to imitate Paul precisely because Paul imitates Christ (1 Cor 11:1).</p>",
    "11": "<p>The revelation of God in rescue-from-suffering: 'the Lord rescued me from all of them.' The pattern of apostolic suffering and divine deliverance runs through Paul's ministry (2 Cor 11:23-28; Acts passim) and through the OT narrative of YHWH's deliverance of his servants. The Lord who rescued Paul is the same God who raised Christ from the suffering of the cross — the rescue of Paul participates in the rescue-pattern established by the resurrection.</p>",
    "12": "<p>A direct revelation: 'everyone who wants to live a godly life in Christ Jesus will be persecuted.' The Christological corollary of suffering: those who are in Christ Jesus (<em>en Christō Iēsou</em>) share the experience of the crucified one. Jesus warned his disciples: 'if they persecuted me, they will persecute you' (John 15:20). Persecution of the godly is not an aberration but a structural feature of the period between the two appearances — the world's reaction to Christ is repeated in its reaction to those in Christ.</p>",
    "13": "<p>The revelation of God in the downward trajectory of falsehood: 'evildoers and impostors will go from bad to worse, deceiving and being deceived.' The contrast with the upward movement of faithful ministry: false teaching is self-accelerating corruption, while the gospel produces progressively deeper knowledge of the truth (Col 1:10). Two opposed trajectories characterize the present age — the way of Christ and the way of the deceiver.</p>",
    "14": "<p>The theme of continuance in the received teaching: 'continue in what you have learned and have become convinced about, because you know those from whom you learned it.' The apostolic tradition is transmitted through persons — Timothy learned from Paul, and from Lois and Eunice before that (1:5). What he learned is the gospel of Christ; the personal relational grounding of his conviction is part of what makes his faith sincere rather than secondhand.</p>",
    "15": "<p>A direct revelation: 'the Holy Scriptures, which are able to make you wise for salvation through faith in Christ Jesus.' The OT Scriptures (which Timothy knew from infancy through his Jewish family) exist to generate saving wisdom — and their saving function is actualized specifically through faith in Christ Jesus. The Scriptures' telos is Christ (Rom 10:4: Christ is the goal of the law). The 'holy writings' Timothy knows are the Christological preparation for the gospel he has now received.</p>",
    "16": "<p>The revelation of God in the divine breath of Scripture: 'All Scripture is breathed out by God and profitable for teaching, rebuking, correcting and training in righteousness.' The <em>theopneustos</em> (God-breathed) character of Scripture ensures it bears the authority and life-giving capacity of the divine breath. The four purposes (teaching, rebuking, correcting, training) are the means through which the word of Christ accomplishes its saving telos (v. 15). Scripture is the instrument that serves the proclamation of the Christ it anticipates.</p>",
    "17": "<p>The revelation of God in the goal of scriptural equipping: 'so that the servant of God may be thoroughly equipped for every good work.' The telos of Scripture's equipping is continuous with the telos of Christ's work: people 'prepared for every good work' (Titus 2:14; Eph 2:10: created in Christ Jesus for good works). Scripture is not an end in itself but an instrument that forms God's servants into the likeness of Christ and equips them for his mission.</p>"
  },
  "4": {
    "1": "<p>A direct revelation: 'In the presence of God and of Christ Jesus, who will judge the living and the dead, and in view of his appearing and his kingdom.' The most explicit Christological eschatology in 2 Timothy: Christ Jesus is the Judge of the living and the dead (Acts 10:42; 1 Pet 4:5). His appearing (<em>epiphaneia</em>) and kingdom are the events toward which all ministry is oriented. The charge to Timothy is issued in the presence of this coming judge — all ministry occurs coram Christo.</p>",
    "2": "<p>The theme of urgency grounded in eschatology: 'Preach the word; be prepared in season and out of season.' The preaching of the word is the proclamation of Christ — the word of truth (2:15), the word of God that is not chained (2:9). The urgency ('in season and out of season') reflects the eschatological horizon of v. 1: with the judge about to appear, the proclamation cannot await favorable conditions. Every moment is charged with eschatological weight.</p>",
    "3": "<p>The revelation of God in the rejection of sound doctrine: 'the time will come when people will not put up with sound doctrine.' Sound doctrine (<em>hugiainousēs didaskalias</em>) is the teaching oriented around the gospel of Christ. Its rejection means accumulating teachers who project a god of one's own imagination — the ecclesiastical form of idolatry. As Israel made a golden calf when the true God's representative was absent (Exod 32), the church that rejects Christ-centered teaching manufactures a substitute.</p>",
    "4": "<p>The revelation of God in the turn from truth to myth: 'they will turn their ears away from the truth and turn aside to myths.' Truth in the Johannine-Pauline vocabulary is specifically Christological (John 14:6: I am the truth; Eph 4:21: truth is in Jesus). Myths are the alternatives — speculative constructions that lack the Christological center. The turn from truth to myths is the epistemological dimension of apostasy.</p>",
    "5": "<p>The theme of comprehensive ministerial faithfulness: 'keep your head in all situations, endure hardship, do the work of an evangelist, discharge all the duties of your ministry.' The comprehensive call — every dimension of ministry exercised in every condition — reflects the comprehensiveness of Christ's own ministry (teaching, healing, suffering, rising). The minister's full discharge of duty serves the same Lord who himself held nothing back.</p>",
    "6": "<p>The revelation of God in Paul's death as priestly offering: 'I am already being poured out like a drink offering.' The libation-offering (<em>spendō</em>) accompanied the burnt offering in Israel's worship (Num 15:5-10; Phil 2:17 uses the same verb). Paul's approaching death is not mere martyrdom but priestly self-offering — ministry lived in Christ becomes a kind of drink-offering poured alongside Christ's own finished sacrifice, not repeating it but participating in its pattern.</p>",
    "7": "<p>The revelation of God in completion: 'I have fought the good fight, I have finished the race, I have kept the faith.' The three perfect tenses express completed actions with lasting effects: Paul's contest is finished, his course is run, his trust is kept. The three metaphors (contest, race, faith-keeping) mirror the three images given to Timothy at the start of ch. 2 (soldier, athlete, farmer). Paul's completion is the testimony that the endurance he called Timothy to is achievable — the Lord enabled Paul and will enable Timothy.</p>",
    "8": "<p>A direct revelation: 'Henceforth there is laid up for me the crown of righteousness, which the Lord, the righteous judge, will award to me on that Day — and not only to me but also to all who have loved his appearing.' The parousia of Christ is the moment of final vindication. The 'crown of righteousness' is not earned by Paul's sufferings but 'laid up' (<em>apokeitai</em>) — already determined, awaiting award. The righteous judge who will confer it is Christ himself. The Christological movement of 2 Timothy: from the first epiphaneia (1:10) through present endurance to the final epiphaneia where the judge vindicates the faithful.</p>",
    "9": "<p>The theme of personal presence as covenant faithfulness: 'Do your best to come to me quickly.' Paul is alone and near death (v. 6). The personal urgency of the letter demonstrates that apostolic ministry is embodied in person-to-person relationships, not merely in doctrinal transmission. The Christ who called Paul did not call an abstraction but a person; Timothy's presence with Paul in his dying is an act of the same covenantal loyalty that Christ himself showed (John 10:11: I lay down my life for the sheep).</p>",
    "10": "<p>The revelation of God in world-love as the root of desertion: 'Demas, because he loved this world, has deserted me.' The love of the world (1 John 2:15) replaces love of Christ, the same idolatrous substitution warned of in 3:4 (lovers of pleasure rather than lovers of God). Demas's desertion is the individual enactment of the last-days apostasy pattern — when comfort and safety are preferred to suffering with the apostle, world-love has won.</p>",
    "11": "<p>The theme of restoration as gospel pattern: 'Only Luke is with me. Get Mark and bring him with you, because he is helpful to me in my ministry.' Mark's rehabilitation — after the conflict of Acts 15:36-40 that split Paul and Barnabas — illustrates the gospel's power to restore broken relationships and rehabilitate those who have stumbled. The mark of the gospel community is not permanent exclusion of those who failed but reconciliation through renewed faithful service.</p>",
    "12": "<p>The revelation of God in the apostolic network: 'I sent Tychicus to Ephesus.' The deployment of co-workers across Paul's mission-network (Eph 6:21; Titus 3:12; Col 4:7) reveals the structure of the apostolic church as a coordinated network of commissioned agents carrying the word that is not chained (2:9). The network exists to serve the Christ whose gospel must reach all the Gentiles (4:17).</p>",
    "13": "<p>The revelation of God in embodied ministry: 'bring the cloak... and my scrolls, especially the parchments.' Paul's material needs as he faces death — warmth, reading material, and especially the Scriptures — are a reminder that apostolic ministry is embodied and material, not purely spiritual. That Paul specifically requests the Scriptures reveals the Christological dependence of the apostle on the word that bears witness to Christ (John 5:39).</p>",
    "14": "<p>The revelation of God in eschatological justice: 'The Lord will repay him for what he has done.' Alexander's opposition is left to divine judgment (Rom 12:19: vengeance is mine, says the Lord). The eschatological confidence that grounds Paul's restraint: the judge of the living and the dead (4:1) will adjudicate all human opposition to the gospel. Paul does not need to vindicate himself — the righteous judge will do so at the day of Christ's appearing.</p>",
    "15": "<p>The theme of opposition to the message as opposition to Christ: Alexander 'strongly opposed our message.' The gospel-message (<em>logos</em>) is the word of Christ (2:9). To oppose it systematically is to oppose Christ himself, who is inseparable from the gospel that announces him. The apostolic network must be alert to such opposition, not because human success is at stake, but because the proclamation of Christ is.</p>",
    "16": "<p>The revelation of God in abandonment transformed by grace: 'At my first defense, no one came to my support... May it not be held against them.' The parallel with Gethsemane (Mark 14:50: they all left him and fled) and with Christ's cross-prayer (Luke 23:34: Father, forgive them) is striking. The apostle conformed to Christ in abandonment extends the same forgiveness that Christ extended — the grace of the gospel reshapes even the experience of betrayal into an occasion for intercession.</p>",
    "17": "<p>A direct revelation: 'the Lord stood at my side and gave me strength, so that through me the message might be fully proclaimed and all the Gentiles might hear it. And I was delivered from the lion's mouth.' The divine presence in Paul's trial: the Lord stood with Paul as YHWH stood with Moses before Pharaoh. The purpose is Christological and missional: even Paul's trial before Caesar becomes an occasion for Gentile witness. 'Delivered from the lion's mouth' echoes Ps 22:21 — the psalm of Christ's dereliction and vindication — placing Paul's deliverance within the Christ-pattern of suffering followed by divine rescue.</p>",
    "18": "<p>A direct revelation: 'The Lord will rescue me from every evil attack and will bring me safely to his heavenly kingdom. To him be glory for ever and ever. Amen.' The eschatological confidence: not deliverance from death (Paul knows his departure is near, v. 6) but deliverance through death into the heavenly kingdom of Christ. 'His heavenly kingdom' is the kingdom whose coming Paul charged Timothy to proclaim (4:1). The closing doxology directed to Christ — 'to him be glory' — makes this the letter's Christological climax.</p>",
    "19": "<p>The revelation of God in the named community: greetings to Priscilla, Aquila, and the household of Onesiphorus. The people named are not merely co-workers but members of the body of Christ gathered in specific places. The Incarnation's pattern — God dwelling in particular places through particular persons — continues in the apostolic mission's deployment of named people in named cities, forming local communities of those who call on the Lord's name.</p>",
    "20": "<p>The theme of the embodied particularity of the mission: 'Erastus stayed in Corinth, and I left Trophimus sick in Miletus.' The apostolic mission takes root in specific cities (Corinth, Miletus, Ephesus) through specific people, including those whose illness means they cannot travel. The gospel is not disembodied or abstract — it is enacted by persons with bodies, in particular places, with real limitations and vulnerabilities.</p>",
    "21": "<p>The revelation of God in the urgency of embodied fellowship: 'Do your best to get here before winter.' The physical presence of Timothy with Paul in his dying — before the sea lanes close — is the final expression of the covenantal human fellowship that the gospel creates. The community of those in Christ is not merely institutional but bodily and relational — Paul's desire to see Timothy 'face to face' (1:4) is about to be fulfilled or missed forever.</p>",
    "22": "<p>A direct revelation: 'The Lord be with your spirit. Grace be with you all.' The closing benediction invokes the presence of Christ with Timothy's spirit — the personal fulfillment of the Immanuel promise (Matt 28:20: I am with you always, to the end of the age). The letter that opened with grace, mercy, and peace from Christ Jesus (1:2) closes with the same grace — the divine favor that flows from the gospel frames the entire letter and every ministry it commissions.</p>"
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
    "5": "<p>Titus in Crete: the island of Crete had a significant Jewish community (Acts 2:11; Josephus mentions Cretan Jews). Paul's description of Cretans — citing the Cretan poet Epimenides ('Cretans are always liars, evil beasts, lazy gluttons', v. 12) — uses an ancient ethnic stereotype familiar to his Greco-Roman audience. The church-planting task in Crete required appointing elders in 'every town' (<em>kata polin</em>), indicating a widespread but organizationally young mission. The Pastoral Epistles' emphasis on <em>episkopos</em> (overseer), <em>presbyteros</em> (elder), and <em>diakonos</em> (deacon) reflects the institutionalization of church leadership as the apostolic generation aged and died.</p>"
  },
  "3": {
    "5": "<p>The 'washing of regeneration and renewing of the Holy Spirit' (<em>loutron palingenesias kai anakainōseōs Pneumatos Hagiou</em>) combines Jewish purification-immersion imagery (<em>mikveh</em>) with the OT new-covenant Spirit-promise (Ezek 36:25-27; Joel 2:28-29). <em>Palingenesia</em> (regeneration/new birth) appears only here and Matt 19:28 (the renewal of all things at the eschatological restoration) in the NT — linking individual new birth with cosmic new creation. <em>Paliggenesia</em> was also a Stoic term for the cyclical renewal of the cosmos after the ekpyrosis (cosmic fire) — Paul's use may deliberately appropriate the Stoic vocabulary and fill it with Christological content: the Spirit's renewal is the eschatological new creation arriving in individual conversion.</p>"
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
