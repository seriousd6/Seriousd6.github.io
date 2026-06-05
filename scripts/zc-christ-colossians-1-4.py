"""
Combined script: Philippians (echo + original + context + christ) and
Colossians (echo + original + context + christ) — all 4 chapters each.

This script writes all 8 output files. It is idempotent via merge functions.
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
# PHILIPPIANS
# ============================================================

PHIL_ECHO = {
  "2": {
    "5": [
      {"type": "allusion", "target": "Isa 53:12", "note": "Have this mind among yourselves, which is yours in Christ Jesus — the self-emptying of the Christ-hymn echoes the Servant who poured himself out to death (Isa 53:12); the humiliation-exaltation pattern of the hymn is the Servant trajectory"},
      {"type": "allusion", "target": "Isa 45:23", "note": "Every knee shall bow and every tongue confess — Phil 2:10-11 cites Isa 45:23 directly (as I live, every knee shall bow to me and every tongue shall swear allegiance to YHWH); Paul applies this YHWH-universal-homage text to Jesus, making the confession of Jesus's lordship the fulfillment of YHWH's eschatological claim on all creation"}
    ]
  },
  "3": {
    "9": [
      {"type": "allusion", "target": "Jer 9:23-24", "note": "Not having a righteousness of my own that comes from the law — Jeremiah's warning not to boast in wisdom, might, or riches; Paul's not-boasting in Torah credentials echoes the prophetic critique of self-sufficiency; the only boast is knowing YHWH (and for Paul: Christ)"},
      {"type": "allusion", "target": "Hab 2:4", "note": "A righteousness from God that depends on faith — the Habakkuk anchor of Pauline faith-righteousness; the righteous one shall live by faith; Phil 3:9 applies the same faith-vs-works distinction as Gal 3:11 and Rom 1:17"}
    ],
    "21": [
      {"type": "fulfillment", "target": "Dan 7:13-14", "note": "The Lord Jesus Christ will transform our lowly body to be like his glorious body, by the power that enables him even to subject all things to himself — the Danielic authority of the Son of Man to whom dominion is given (Dan 7:14) is the basis for Paul's confidence in the bodily transformation at the parousia"}
    ]
  }
}

PHIL_ORIGINAL = {
  "2": {
    "6": "<p><strong>hos en morphe theou hyparchon ouch harpagmon hegesato to einai isa theo</strong> (<em>hos en morphē theou hyparchōn ouch harpagmon hēgēsato to einai isa theō</em>): the most debated sentence in Philippians. <em>Morphe theou</em> (form/mode of God) is not mere appearance (doxa/eidos) but the actual mode of existence — the divine being's characteristic reality. <em>Harpagmon</em> (HARPAGMOS): the crux. Older interpretation: 'did not regard equality with God as something to be grasped (and held onto)' — the pre-existent Son relinquished divine prerogatives. Newer consensus (N.T. Wright, R. Hoover): 'did not regard equality with God as something to exploit for his own advantage' — already possessing it, he did not use it selfishly. The second reading requires no ontological descent at incarnation — the Son freely chose not to exploit his divine position. Either way, the <em>kenosis</em> (self-emptying, v. 7) is voluntary and constitutes the pattern for Christian ethics (v. 5).</p>",

    "9": "<p><strong>dio kai ho theos auton hyperypsosen kai echarisato auto to onoma to hyper pan onoma</strong> (<em>dio kai ho theos auton hyperypsōsen kai echarisato autō to onoma to hyper pan onoma</em>): 'Therefore God has highly exalted him and bestowed on him the name that is above every name.' <em>Hyperypsōsen</em> (super-exalted) is a hapax-legomenon in the NT — the <em>hyper</em> prefix intensifies beyond normal exaltation. The 'name above every name' that is then used in v. 10 is YHWH (<em>Kyrios</em>): by giving Jesus the name Lord-of-all, God applies Isa 45:23 (every knee bows to YHWH) to Jesus. The highest OT claim — universal homage to YHWH alone — is now predicated of the crucified and exalted Jesus.</p>",

    "11": "<p><strong>kai pasa glossa exomologesetai hoti Kyrios Iesous Christos eis doxan Theou patros</strong> (<em>kai pāsa glōssa exomologēsetai hoti Kyrios Iēsous Christos eis doxan Theou patros</em>): 'every tongue confess that Jesus Christ is Lord, to the glory of God the Father.' The confession <em>Kyrios Iesous Christos</em> is the earliest Christian creed (cf. Rom 10:9; 1 Cor 12:3). Its application of Isa 45:23 to Jesus is the most explicit equation of Jesus with YHWH in the undisputed Pauline letters. The <em>eis doxan Theou patros</em> (to the glory of God the Father) prevents the Christology from displacing the Father: Jesus's lordship is the Father's glory, not a rival to it — a proto-Trinitarian formulation.</p>"
  },
  "3": {
    "8": "<p><strong>alla men oun kai hegoumai panta zemia einai dia to hyperechon tes gnoseos Christou Iesou tou kyriou mou</strong>: 'Indeed, I count everything as loss because of the surpassing worth of knowing Christ Jesus my Lord.' <em>Zemia</em> (loss) and <em>skybala</em> (v. 8: dung/rubbish — a deliberately coarse word, the strongest available Greek term for something worthless or repulsive) balance against <em>to hyperechon</em> (the surpassing value). Paul revalues his entire pre-conversion Jewish curriculum vitae — circumcision, Benjaminite lineage, Pharisaic zeal, Torah-righteousness — as <em>skybala</em> compared to the knowing (<em>gnōsis</em>) of Christ. This is not anti-Judaism but a Christological superordination: Christ is worth more than everything else combined.</p>",

    "20": "<p><strong>hemon de to politeuma en ouranois hyparchei</strong> (<em>hēmōn de to politeuma en ouranois hyparchei</em>): 'Our citizenship (<em>politeuma</em>) is in heaven.' <em>Politeuma</em> is a technical term for a community's civic identity — Philippi was a Roman colony whose citizens held Roman citizenship with its legal privileges (Acts 16:21). Paul uses the very term for civic identity to relocate the Philippians' primary belonging: they are residents in a Roman colony but their true <em>politeuma</em> is heavenly. The word also evokes the Jewish diaspora institution of a <em>politeuma</em> — a recognized community of foreigners living under their own governance within a host city (attested in Egypt and Cyrene).</p>"
  }
}

PHIL_CONTEXT = {
  "1": {
    "1": "<p>Philippi was a Roman colony (colonia Iulia Augusta Philippensis, named for Philip II of Macedon and refounded by Augustus) in the province of Macedonia, on the Via Egnatia — the major east-west Roman road. Its citizens held Roman citizenship and its society closely modeled Roman institutions (the <em>duoviri</em> rather than Greek <em>stratēgoi</em> of Acts 16:20). Paul founded the church ca. 49-50 CE (Acts 16) — the first European church. The congregation had significant female leadership (Lydia, Euodia, Syntyche) and military members. Philippians is written from prison (1:7, 13, 17) — probably Rome (ca. 60-62 CE) or Ephesus (ca. 54-55 CE, supported by proximity implied by Philippians 2:19-30).</p>",

    "13": "<p>The Praetorium (<em>praitorion</em>, 1:13) most naturally refers to the Praetorian Guard — the elite imperial bodyguard of 9,000 soldiers headquartered at Rome. If this is the Roman imprisonment, Paul's gospel has penetrated the household troops of the emperor — and Caesar's household is specifically mentioned (4:22: 'those of Caesar's household'). This is the remarkable irony: the imprisoned apostle has evangelized the imperial palace guard while awaiting trial before the emperor.</p>"
  },
  "3": {
    "5": "<p>Paul's Jewish credentials (3:5-6) are the most complete self-description in his letters: circumcised on the eighth day (Torah-observant from birth; not a proselyte); of the people of Israel (full ethnic Israelite, not a convert); tribe of Benjamin (the prestige tribe that gave Israel its first king, Saul; Paul's Jewish name); Hebrew of Hebrews (Aramaic-speaking, Palestinian Jewish heritage, not a Diaspora Hellenist); as to the law a Pharisee (the most rigorous Torah-observance movement); as to zeal a persecutor of the church (demonstrating active Jewish loyalty); as to righteousness under the law, blameless. This is the curriculum vitae of a first-generation Pharisaic scholar of the highest standing — which Paul then categorizes as <em>skybala</em>.</p>"
  }
}

PHIL_CHRIST = {
  "2": {
    "8": "<p>A direct revelation: 'He humbled himself by becoming obedient to the point of death, even death on a cross.' The descending movement of the Christ-hymn (form of God → form of a servant → death on a cross) reaches its nadir in the cross — the most shameful death in Roman society. The cross is not an accident that interrupted Christ's mission but the deliberate end-point of his voluntary self-humiliation. Crucifixion as the mode of death is theologically load-bearing: God's ultimate self-revelation occurs precisely at the place of maximum human shame. The Christological pattern is the template for Paul's ministry (3:10: I want to know him and the fellowship of his sufferings).</p>",

    "11": "<p>A direct revelation: 'Every tongue confess that Jesus Christ is Lord, to the glory of God the Father.' The universal confession of Jesus as Lord (applying Isa 45:23's YHWH-homage text to Jesus) is the eschatological goal of all creation. This is not merely a future prediction but the normative Christological claim that shapes present discipleship: Jesus is Lord now, before every knee bows; the community that confesses this lives in counter-cultural obedience to a different sovereign than Caesar. The Christological center of Philippians: the crucified and exalted Jesus is the Lord of all creation.</p>"
  },
  "3": {
    "10": "<p>A direct revelation: 'That I may know him and the power of his resurrection, and may share his sufferings, becoming like him in his death, that by any means possible I may attain the resurrection from the dead.' Paul's Christological-participatory formula: knowing Christ includes knowing both the power of his resurrection and the fellowship of his suffering. The resurrection is the pole that defines the suffering as meaningful — suffering is not masochism but Servant-pattern participation. <em>Summorphizomenos to thanatō autou</em> (being conformed to his death) applies the Christ-hymn (2:8) to Paul's own experience: his suffering is a Christomorphic process.</p>",

    "20": "<p>A direct revelation: 'Our citizenship is in heaven, and from it we await a Savior, the Lord Jesus Christ, who will transform our lowly body to be like his glorious body.' The parousia will accomplish the final Christological transformation: the resurrection-body of Christ becomes the template for the redeemed body of believers. This is the personal eschatological application of 1 Cor 15:49 (we shall bear the image of the man of heaven). Christ's glorious resurrection body is not merely an isolated miracle but the prototype of the new creation in which believers will share at his coming.</p>"
  }
}

# ============================================================
# COLOSSIANS
# ============================================================

COL_ECHO = {
  "1": {
    "15": [
      {"type": "allusion", "target": "Prov 8:22-31", "note": "The firstborn of all creation — Wisdom's self-description in Prov 8:22 ('the LORD possessed me at the beginning of his work, the first of his acts of old') resonates with Christ as the firstborn; what Wisdom claimed as pre-creation origin Paul attributes to Christ as the agent of all creation"},
      {"type": "allusion", "target": "Gen 1:26-27", "note": "The image of the invisible God — Adam was made in the image of God (tselem elohim); Christ is the image of the invisible God in whom the Adamic image-bearing reaches its perfect, unfallen expression"}
    ],
    "20": [
      {"type": "allusion", "target": "Isa 52:7", "note": "Making peace through the blood of his cross — the beautiful feet that bring good news of peace (Isa 52:7) are the feet of Christ's mission; the peace is accomplished not merely proclaimed, grounded in the blood of the cross"},
      {"type": "allusion", "target": "Ezek 37:1-14", "note": "Reconciling all things to himself — the valley of dry bones and YHWH's breath restoring life; the cosmic reconciliation of Col 1:20 exceeds even Ezekiel's national restoration to encompass all creation"}
    ]
  },
  "2": {
    "14": [
      {"type": "fulfillment", "target": "Isa 43:25", "note": "Having canceled the record of debt that stood against us — YHWH's declaration 'I am he who blots out your transgressions for my own sake' (Isa 43:25) finds its mechanism in the cross: the debt-document nailed to the cross is the vehicle of the blotting-out"},
      {"type": "fulfillment", "target": "Exod 31:18", "note": "Nailing it to the cross — the tablets written by God's finger that Moses shattered at the golden calf; the law's written demands, now used against us, are rendered powerless by being nailed to the cross where Christ absorbed their condemnation"}
    ]
  },
  "3": {
    "10": [
      {"type": "allusion", "target": "Gen 1:26-27", "note": "Being renewed in knowledge after the image of its creator — the new creation restores the original imago Dei; the knowledge lost at the Fall (Gen 3, where the desire for knowledge outside of God broke the relationship) is restored in the new creation"}
    ]
  }
}

COL_ORIGINAL = {
  "1": {
    "15": "<p><strong>hos estin eikon tou theou tou aoratou prototokos pases ktiseos</strong> (<em>hos estin eikōn tou theou tou aoratou, prōtotokos pasēs ktiseōs</em>): 'who is the image of the invisible God, the firstborn of all creation.' The Colossian hymn (1:15-20) is one of the highest Christological statements in the NT. <em>Eikon</em> (image) denotes not a copy of an absent original but the precise visible representation of an invisible reality — Christ is the icon in whom the otherwise-invisible God is seen (cf. John 1:18; Heb 1:3: <em>apaugasma</em> + <em>charakter</em>). <em>Prōtotokos pasēs ktiseōs</em>: 'firstborn of all creation' — <em>prōtotokos</em> is not 'first created' (which would be <em>prōtoktistos</em>) but the one who holds the firstborn's status of priority and authority over all creation; Col 1:16-17 confirms he is the creator, not a creature.</p>",

    "19": "<p><strong>hoti en auto eudokesen pan to pleroma katoikesai</strong> (<em>hoti en autō eudokēsen pan to plērōma katoikēsai</em>): 'for in him all the fullness was pleased to dwell.' <em>Pleroma</em> (fullness) in Gnostic usage (slightly later than Colossians) denotes the totality of divine attributes distributed among aeons. Paul uses the term to assert the counter-claim: the entire divine fullness (not a portion distributed among spiritual intermediaries) resides bodily (<em>somatikos</em>, 2:9) in Christ. The Colossian false teaching apparently proposed a hierarchy of spiritual powers mediating access to God; the hymn's response is that Christ contains the whole without remainder.</p>"
  },
  "2": {
    "14": "<p><strong>exaleipsas to kath' hemon cheirographon tois dogmasin ho en hypenantios hemin</strong> (<em>exaleipsas to kath' hēmōn cheirographon tois dogmasin ho ēn hypenantios hēmin</em>): 'having canceled the record of debt (<em>cheirographon</em>) that stood against us with its legal demands.' <em>Cheirographon</em> (handwritten document/bond) was a legal IOU — a debtor's acknowledgment of what was owed. The metaphor: humanity's accumulated debt of sin-obligations constituted a document that indicted us. <strong>proseilosas auto to staurō</strong>: 'nailing it to the cross.' The practice of affixing a notice of charges (<em>titulus</em>) to the cross of a condemned person (John 19:19-22: 'Jesus of Nazareth, King of the Jews') provides the image: our indicting debt-document was nailed to the cross with Christ, absorbing its condemnation in his death.</p>",

    "15": "<p><strong>apekdysamenos tas archas kai tas exousias edeigmatisen en parresia thriambeusas autous en auto</strong> (<em>apekdysamenos tas archas kai tas exousias edeigmatisen en parrēsia, thriambeusas autous en autō</em>): 'disarming the rulers and authorities and putting them to open shame, by triumphing over them in him.' The cosmic powers (<em>archai kai exousiai</em>) that featured in the Colossian false teaching as spiritual intermediaries are publicly stripped of their authority by the cross. The triumphal procession image: in a Roman triumph, defeated enemies were displayed as captives behind the general's chariot. Christ's cross is the paradoxical triumph: precisely in what looks like defeat, the powers are disarmed and publicly humiliated.</p>"
  },
  "3": {
    "3": "<p><strong>apethanete gar kai he zoe hymon kekryptai syn to Christo en to theo</strong> (<em>apethanete gar kai hē zōē hymōn kekryptai syn tō Christō en tō theō</em>): 'for you have died, and your life is hidden with Christ in God.' The perfect passive <em>kekryptai</em> (is and remains hidden) describes the present state: the believer's true life is concealed within the divine-Christological reality, not visible to external observation. This 'hiddenness' will be resolved at the parousia (v. 4: 'when Christ who is your life appears, you also will appear with him in glory') — eschatological glory is the unveiling of what is now hidden. The mystical union language ('with Christ in God') positions the believer's ontological security within the relationship between the Son and the Father.</p>"
  }
}

COL_CONTEXT = {
  "1": {
    "2": "<p>Colossae was a city in the Lycus River valley of Phrygia (western Turkey), about 160 km east of Ephesus, near Laodicea and Hierapolis. In the classical period it was a significant city; by the mid-first century CE it had been eclipsed by its neighbors but remained a substantial wool-trading town. Paul did not found the Colossian church himself (2:1: 'those who have not seen me face to face'); it was apparently founded by Epaphras during Paul's Ephesian ministry (1:7; 4:12-13). The letter (written ca. 60-62 CE from Rome, or possibly Ephesus or Caesarea) addresses a 'philosophy' (<em>philosophia</em>, 2:8) threatening the congregation.</p>",

    "16": "<p>The powers mentioned in the Colossian hymn and polemic (<em>archai, exousiai, thronoi, kyriotetes, angels</em>) reflect a rich Second Temple Jewish angelology that assigned cosmic governance of nations, natural forces, and celestial bodies to angelic intermediaries. 1 Enoch's Watchers, the 'Sons of God' of Deut 32:8 LXX, and the Qumran 'Prince of the congregation' all reflect this angelological world. The Colossian false teaching apparently involved veneration of these powers as necessary intermediaries — perhaps combined with Jewish calendar observances (2:16: new moons and Sabbaths) and ascetic practices (2:21: Do not handle, do not taste, do not touch). Scholars debate whether this is Jewish mysticism, proto-Gnosticism, or a local syncretistic mixture.</p>"
  },
  "2": {
    "8": "<p>The 'philosophy and empty deceit according to human tradition, according to the elemental spirits of the world (<em>stoicheia tou kosmou</em>)' opposed in 2:8 has generated enormous scholarly debate. <em>Stoicheia</em> can mean: (1) the basic elements (earth, water, fire, air) of Greco-Roman cosmology; (2) the ABCs / elementary principles of instruction; (3) the elemental spiritual beings associated with the cosmos (astral spirits, planetary powers). The context (2:15-18: powers, angels, calendars) and the Galatian parallel (Gal 4:3, 9) where Paul equates <em>stoicheia</em> with slavish pre-Christian religious observance suggest option (3) or a combination: cosmic powers that enforced the old religious order Christ has superseded.</p>"
  }
}

COL_CHRIST = {
  "1": {
    "15": "<p>A direct revelation: 'He is the image of the invisible God, the firstborn of all creation.' The Colossian hymn's Christological thesis: Christ is not an emanation from God, not an angelic mediator, not one power among many, but the very image of the otherwise-invisible God. The entire OT struggle to represent the unrepresentable God — the burning bush, the cloud-pillar, the Shekinah-glory, the prophetic visions — finds its resolution in Christ: in him the invisible God is fully and finally visible. The image-claim is not an accommodation for weak minds but the definitive disclosure of divine reality.</p>",

    "20": "<p>A direct revelation: 'And through him to reconcile to himself all things, whether on earth or in heaven, making peace by the blood of his cross.' The scope of reconciliation is cosmic — not merely human spiritual relationships with God, but 'all things' in heaven and on earth. The cross is not a local transaction affecting individual souls but the resolution of a cosmic disruption (Rom 8:19-22: the creation groaning for redemption). The peace made through the blood of the cross is the eschatological shalom YHWH promised through the prophets, now grounded in the specific historical event of Christ's death.</p>"
  },
  "2": {
    "9": "<p>A direct revelation: 'For in him the whole fullness of deity dwells bodily.' <em>Somatikos</em> (bodily) is the decisive word that distinguishes Paul's Christology from all Gnostic alternatives: the fullness of deity is not distributed among spiritual intermediaries but concentrated in the bodily, incarnate, crucified, and risen Jesus. The false teaching of Colossae proposed a spectrum of spiritual powers mediating access to the divine fullness; Paul's response is that you have the fullness in Christ already (v. 10: 'you have been filled in him') — no further spiritual program, calendar, or ascetic discipline is needed to access divine reality.</p>",

    "15": "<p>A direct revelation: 'He disarmed the rulers and authorities and put them to open shame by triumphing over them in him.' The cross — which appeared to be Rome's and the powers' triumph over Jesus — was in fact Christ's triumph over the powers. The Christological paradox of Colossians: the moment of apparent defeat is the moment of definitive victory. The powers are not destroyed at the cross (they continue to act in history, Eph 6:12) but they are decisively disarmed — their authority is broken, their indictment-power (the cheirographon) is canceled, their ability to condemn is gone.</p>"
  },
  "3": {
    "4": "<p>A direct revelation: 'When Christ who is your life appears, then you also will appear with him in glory.' Christ is not merely the source of life or the example of life but is himself the believer's life — a participatory identification so radical that the believer's appearance at the parousia is simultaneous with and inseparable from Christ's own appearing. The eschatological hope of Colossians is not individual survival after death but corporate appearing with Christ at his coming — the believer's hidden life (3:3) unveiled in glory. The Christological frame encompasses both the hiddenness of the present and the glory of the future.</p>"
  }
}

def main():
    # Philippians
    e = load_echo('philippians')
    merge_echo(e, PHIL_ECHO)
    save_echo('philippians', e)

    c = load_comm('mkt-original', 'philippians')
    merge_comm(c, PHIL_ORIGINAL)
    save_comm('mkt-original', 'philippians', c)
    print(f'Phil original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', 'philippians')
    merge_comm(c, PHIL_CONTEXT)
    save_comm('mkt-context', 'philippians', c)
    print(f'Phil context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', 'philippians')
    merge_comm(c, PHIL_CHRIST)
    save_comm('mkt-christ', 'philippians', c)
    print(f'Phil christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    # Colossians
    e = load_echo('colossians')
    merge_echo(e, COL_ECHO)
    save_echo('colossians', e)

    c = load_comm('mkt-original', 'colossians')
    merge_comm(c, COL_ORIGINAL)
    save_comm('mkt-original', 'colossians', c)
    print(f'Col original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', 'colossians')
    merge_comm(c, COL_CONTEXT)
    save_comm('mkt-context', 'colossians', c)
    print(f'Col context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', 'colossians')
    merge_comm(c, COL_CHRIST)
    save_comm('mkt-christ', 'colossians', c)
    print(f'Col christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

if __name__ == '__main__':
    main()
