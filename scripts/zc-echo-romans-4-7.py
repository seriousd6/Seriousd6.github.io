"""
MKT Echo Layer — Romans chapters 4–7
Run: python3 scripts/zc-echo-romans-4-7.py

Source data used:
- data/interlinear/romans.json
- data/translation/glossary-greek.json (pistis, dikaiosyne, nomos, hagiasmos, apolytrosis)
- data/translation/draft/mediating/romans.json
- data/parallels/romans.json (absorbed: 4:3 Gen 15:6; 4:7-8 Ps 32:1-2; 4:17 Gen 17:5;
  4:18 Gen 15:5; 5:6-8 Isa 53:5 — all gained note fields below)

Key decisions in this range:
- 4:3 Gen 15:6: classified quote — Paul introduces it with "What does Scripture say?" and
  cites the LXX verbatim; the core proof-text for the faith-righteousness argument
- 4:7-8 Ps 32:1-2: classified quote — Paul cites David's beatitude on forgiveness as the
  second scriptural witness; LXX is followed closely
- 4:17 Gen 17:5: classified quote — "I have made you a father of many nations," Paul's
  explicit citation from the Abrahamic covenant name-change
- 4:18 Gen 15:5: classified quote — "so shall your offspring be," the star-counting promise
- 4:19 (Abraham's body, Sarah's womb): Gen 17:17 + Gen 18:11 as factual background,
  not quotes; classified allusion
- 4:25 Isa 53:4-5 + 53:11-12: allusion — the Servant language is activated but Paul does
  not cite formally; the "delivered over" (paredothē) and "raised for justification" both
  echo Isa 53:12 and 53:11; classified allusion rather than fulfillment because Paul's
  formulation is compressed and does not use citation language
- 5:5 (Spirit poured out): Joel 2:28-29 + Ezek 36:26-27 — both classified allusion;
  the pouring-out language is Joel's specific contribution, the new-heart content is Ezekiel's
- 5:12 (sin entered through one man): Gen 3:17-19 is the foundational text; Gen 2:17 adds
  the death-command; classified type for the Adam-Christ parallelism that follows
- 5:14 ("Adam, who is a pattern of the one to come"): Paul's own typological statement —
  the Adam-type is named directly; echo entry references Gen 2-3 as the source
- 5:18-19 (one trespass → condemnation / one righteous act → justification): Gen 3:6 as
  the trespass source + Isa 53:11 as the righteous act/justification source; classified as
  separate allusion entries
- 6:3-4 (baptism into death, raised through the Father's glory): Ps 16:10 as the
  resurrection anchor; Exod 14 (Red Sea) as the shadow for baptism (1 Cor 10:2 makes
  this explicit); both classified allusion
- 7:7 ("You shall not covet"): classified quote — Paul cites the tenth commandment verbatim
  (Exod 20:17 = Deut 5:21), the only commandment that targets desire rather than act
- 7:9-11 (commandment came → sin sprang to life → death): Gen 2:16-17 classified as type —
  the structural parallel between the garden commandment activating sin's power and Paul's
  autobiographical account is Paul's own conceptual framing of the Fall
- 7:12 (law is holy, righteous, good): Ps 19:7-9 allusion — the psalmist's triple praise
  of the law's perfection, righteousness, and purity maps directly
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

ROMANS_ECHOES = {
  "4": {
    "3": [
      {"type": "quote", "target": "Gen 15:6", "note": "Paul cites the LXX of Genesis 15:6 verbatim: 'Abraham believed God, and it was credited to him as righteousness.' The verse is the anchor of his argument — righteousness by faith predates and thus cannot depend on circumcision (Gen 17) or the Mosaic law (Exod 19), both of which came later. The faith of which Paul speaks is Abraham's trust in the God who promises resurrection from the dead (v17) — the same faith that now justifies those who believe in Christ."}
    ],
    "7": [
      {"type": "quote", "target": "Ps 32:1-2", "note": "Paul quotes the LXX of Ps 32:1-2 (David's beatitude on forgiven sin) as a second scriptural witness to righteousness credited apart from works: 'Blessed are those whose transgressions are forgiven, whose sins are covered; blessed is the one whose sin the Lord will never count against them.' David's blessing on the forgiven — not on the law-keeper — confirms that credited righteousness operates by divine non-counting of sin, not by moral achievement."}
    ],
    "9": [
      {"type": "allusion", "target": "Gen 15:6", "note": "Paul returns to the Genesis 15:6 text to press a chronological argument: the crediting of righteousness to Abraham happened in chapter 15, before circumcision was instituted in chapter 17. The allusion to the sequence in Genesis is the argument — the text's narrative order becomes the logical proof that faith-righteousness is not a circumcised-Jew-only blessing."}
    ],
    "11": [
      {"type": "allusion", "target": "Gen 17:10-11", "note": "The circumcision of Genesis 17 is the covenant sign Paul calls a 'seal' (sphragis) of the righteousness Abraham already had by faith. Paul's reading is exegetically precise: Genesis 17 describes circumcision as a 'sign' (oth) of the covenant, and Paul treats it as certifying something already established — the faith-righteousness of Genesis 15 that preceded it by decades."}
    ],
    "13": [
      {"type": "allusion", "target": "Gen 22:17-18", "note": "The promise that Abraham and his offspring would 'be heir of the world' is Paul's summary of the cumulative Abrahamic land and blessing promises: Gen 12:3 ('all peoples on earth will be blessed through you'), Gen 17:4 ('father of many nations'), and Gen 22:17-18 ('your descendants will take possession of the cities of their enemies'). Paul reads this global scope as always-already-intended, not a later expansion."}
    ],
    "17": [
      {"type": "quote", "target": "Gen 17:5", "note": "Paul quotes the divine naming of Abraham: 'I have made you a father of many nations.' The covenant name-change (from Abram to Abraham) is God's self-binding to a universal promise — not merely the father of Israel but of many nations. Paul reads 'many nations' as including the Gentiles who will come to faith in Christ, the seed through whom the blessing arrives (cf. Gal 3:16)."},
      {"type": "theme", "target": "Isa 48:13", "note": "God 'who gives life to the dead and calls into being things that were not' — Paul's description of the God Abraham trusted invokes the creation-from-nothing power also celebrated in Isa 48:13 and Ps 33:6. The same divine creative word that called the cosmos from nothing is the word that will call life from Abraham's as-good-as-dead body and Sarah's barren womb. Faith in this God is resurrection-faith."}
    ],
    "18": [
      {"type": "quote", "target": "Gen 15:5", "note": "Paul quotes God's promise to Abraham at the covenant-making of Genesis 15: 'So shall your offspring be' — the comparison to the uncountable stars. Abraham believed this promise 'against all hope' (par' elpida ep' elpidi), which Paul presents as the paradigm of faith: trusting the God who promises when all natural evidence contradicts the possibility. The star-counting promise is about to be fulfilled not only biologically but cosmically, through the many-nations offspring."}
    ],
    "19": [
      {"type": "allusion", "target": "Gen 17:17", "note": "Genesis 17:17 records Abraham's laughter at the thought of a son at age one hundred, and Sarah's laughter in Gen 18:12 — both confronting the physiological impossibility Paul names ('his body was as good as dead'). Paul presents Abraham as 'not weakening in his faith' despite fully facing these facts (Gen 17:17 shows he reckoned with them); his faith was not denial of reality but trust in the God who transcends it."}
    ],
    "22": [
      {"type": "allusion", "target": "Gen 15:6", "note": "Paul returns to the foundational text a third time to anchor his conclusion: this is why it was credited as righteousness — because the faith Abraham exercised is precisely the resurrection-trusting faith that corresponds to the character of God who raises the dead (v17). The repetition drives home the argument: the Genesis text establishes the principle, not the exception."}
    ],
    "25": [
      {"type": "allusion", "target": "Isa 53:12", "note": "Paul's compressed creedal statement — 'delivered over (paredothē) to death for our sins' — uses the same Greek verb (paradidōmi) as the LXX of Isa 53:12 ('he poured out his life to death, and was numbered with the transgressors'). The 'delivered over' language activates the Servant who is handed over to death for the sins of the many; Paul's formulation in v25a is the Isaianic Servant pattern applied to the death of Christ."},
      {"type": "allusion", "target": "Isa 53:11", "note": "Paul's 'raised to life for our justification' parallels the Servant's justifying work in Isa 53:11 — 'by his knowledge my righteous servant will justify many, and he will bear their iniquities.' The combination of death-for-sins (v25a) and justification (v25b) in Paul's couplet mirrors the Servant's death-bearing and justifying work in Isa 53:11-12; the resurrection is Paul's addition — it is the event through which the Servant's justifying power is applied."}
    ]
  },
  "5": {
    "1": [
      {"type": "allusion", "target": "Isa 53:5", "note": "Isaiah's Servant song declares that 'the punishment that brought us peace (shalom) was on him' — Paul's 'peace with God through our Lord Jesus Christ' is the realized version of the peace Isa 53:5 anticipates. The shalom of the new covenant comes through the one who bore the punishment, precisely as Isaiah foresaw."},
      {"type": "allusion", "target": "Isa 32:17", "note": "Isaiah prophesies that 'the fruit of that righteousness will be peace; its effect will be quietness and confidence forever' — Paul's 'we have peace with God through our Lord Jesus Christ' is the arrival of the righteousness-producing-peace that Isaiah locates in the messianic age, when the Spirit is poured out and justice reigns."}
    ],
    "2": [
      {"type": "allusion", "target": "Ps 65:4", "note": "The psalmist declares 'Blessed are those you choose and bring near to live in your courts' — access to God's presence was mediated through temple proximity, priestly intercession, and sacrificial ritual. Paul's 'we have gained access (prosagōgēn) by faith into this grace' presents Christ as the new access point: the one who brings believers into the presence of God without the temple mediating structures."}
    ],
    "5": [
      {"type": "allusion", "target": "Joel 2:28-29", "note": "Joel's promise that God would 'pour out my Spirit on all people' — Paul's 'the love of God has been poured out into our hearts through the Holy Spirit who has been given to us' uses the identical outpouring language. Joel's eschatological pouring-out is the OT announcement; Paul's indicative ('has been given') is the announcement that the age Joel foresaw has arrived."},
      {"type": "allusion", "target": "Ezek 36:26-27", "note": "Ezekiel's new covenant promise: 'I will put my Spirit in you and move you to follow my decrees' — the content of the Spirit's work Paul describes (the love of God present in the believer through the indwelling Spirit) realizes the Ezekielian new heart, animated by the Spirit that makes covenant obedience possible from the inside."}
    ],
    "6": [
      {"type": "allusion", "target": "Isa 53:6", "note": "Isaiah's lament that 'we all, like sheep, have gone astray, each of us has turned to our own way; and the LORD has laid on him the iniquity of us all' — Paul's 'when we were still powerless, Christ died for the ungodly' activates this register of substitutionary bearing: the ungodly for whom Christ dies are precisely those who have gone astray. The 'still powerless' state is the Isaiah 53:6 condition of total lostness before God's initiative."}
    ],
    "8": [
      {"type": "allusion", "target": "Isa 53:4-6", "note": "Paul's 'while we were still sinners, Christ died for us' concentrates the Isaianic Servant's vicarious suffering for the ungodly: 'he took up our infirmities... he was pierced for our transgressions, he was crushed for our iniquities' (Isa 53:4-5). God's love demonstrated in Christ's death is the enactment of the Servant's mission — bearing the penalty that those who were enemies deserved."}
    ],
    "9": [
      {"type": "allusion", "target": "Lev 17:11", "note": "The Levitical principle that 'the life of a creature is in the blood, and I have given it to you to make atonement for yourselves on the altar; it is the blood that makes atonement for one's life' — Paul's 'justified by his blood' activates this foundational Levitical theology. The blood of Christ accomplishes what the sacrificial blood of Leviticus prefigured: the atonement that satisfies God's righteous requirement."},
      {"type": "allusion", "target": "Exod 12:13", "note": "At the Passover, blood applied to the doorframes meant that 'when I see the blood, I will pass over you; no destructive plague will touch you when I strike Egypt' — Paul's 'saved from God's wrath through him' invokes this Passover structure: the blood applied averts the wrath that would otherwise fall. Christ's blood is the Passover blood that causes divine judgment to pass over the believing household."}
    ],
    "10": [
      {"type": "allusion", "target": "Isa 53:5", "note": "'By his wounds we are healed' — Paul's 'reconciled to him through the death of his Son' activates the same Isaianic logic: the Servant's suffering is what bridges the estrangement between God and his people. Reconciliation (katallassō) is Paul's relational term for what Isa 53:5 describes as healing; both point to the same underlying event — the death of the one who bore the hostility on our behalf."}
    ],
    "11": [
      {"type": "allusion", "target": "Jer 9:23-24", "note": "Jeremiah declares that the only legitimate boasting is 'that he understands and knows me, that I am the LORD, who exercises kindness, justice and righteousness on earth' — Paul's 'we also boast in God through our Lord Jesus Christ' realizes this prophetic criterion: the boasting that remains after grace-through-faith is the boasting in the God who has acted in Christ, not in human moral performance."}
    ],
    "12": [
      {"type": "type", "target": "Gen 2:17", "note": "God's warning in the garden: 'when you eat from it you will certainly die' — Paul's 'sin entered the world through one man, and death through sin' traces the origin of the condition he has been describing since 1:18. Adam is the type whose disobedience introduced the universal death-reign Paul will describe in vv14-21; the garden commandment and its violation are the OT event Paul is unpacking as the structural counterpart to Christ's obedience."},
      {"type": "allusion", "target": "Gen 3:17-19", "note": "The curse pronounced over Adam — 'cursed is the ground because of you... you will surely return to dust' — is the OT description of death entering the created order through human sin. Paul's 'death spread to all people, because all sinned' generalizes the Adamic curse as the universal human inheritance, the condition that the 'second Adam' will reverse."}
    ],
    "14": [
      {"type": "type", "target": "Gen 2:15-17", "note": "Paul names Adam explicitly as 'a pattern (typos) of the one to come' — the only place in the NT where Adam is formally designated a type of Christ. The type-antitype relationship is structural: one man's act with universal consequences (for all under him) and one man's act with universal consequences (for all in him). The Garden commandment, the act of disobedience, and the death-consequence form the template that Christ inverts with obedience and life."}
    ],
    "17": [
      {"type": "allusion", "target": "Dan 7:27", "note": "Daniel's vision that 'the kingdom and the dominion and the greatness of the kingdoms under the whole heaven shall be given to the people of the saints of the Most High' — Paul's 'those who receive God's abundant provision of grace and of the gift of righteousness will reign in life through the one man, Jesus Christ' realizes this Danielic vision of the saints' eschatological reign; the reigning comes through righteousness-as-gift, not through military conquest."}
    ],
    "18": [
      {"type": "allusion", "target": "Gen 3:6", "note": "The 'one trespass' that 'resulted in condemnation for all people' is the eating in Genesis 3:6 — the single act of disobedience by the one man through whom condemnation spread. Paul's legal-forensic framing (one trespass → condemnation) is the negative half of the Adam-Christ parallel, grounded in the Genesis narrative as the historical event Paul reads as the origin of the universal human condition."},
      {"type": "allusion", "target": "Isa 53:11", "note": "The 'one righteous act' that 'resulted in justification and life for all people' activates the Servant's justifying work: 'by his knowledge my righteous servant will justify many, and he will bear their iniquities.' Paul's 'one righteous act' (dikaiōma) compresses the Servant's substitutionary obedience and death into a single event — the antitype of Adam's single act of disobedience."}
    ],
    "19": [
      {"type": "allusion", "target": "Gen 3:6", "note": "'Through the disobedience of the one man the many were made sinners' — Genesis 3:6 ('she took some and ate it; she also gave some to her husband, who was with her, and he ate it') is the event Paul is interpreting as the constitution of 'the many' as sinners. The Adamic disobedience is not merely an example of sin but the act by which sin became the defining condition of human nature."},
      {"type": "allusion", "target": "Isa 53:11", "note": "'Through the obedience of the one man the many will be made righteous' — Isa 53:11 LXX: 'and he will justify the righteous one who serves many well, and he himself will carry their sins.' The structural parallel is between the Servant's obedience and its justifying outcome for the many — precisely the pattern Paul applies to Christ's obedience as the ground of the many's righteousness."}
    ],
    "20": [
      {"type": "allusion", "target": "Exod 19:5-6", "note": "The Mosaic law was introduced at Sinai as the instrument of the covenant relationship — but Paul's 'the law was brought in so that the trespass might increase' turns the expected purpose on its head. The Sinai law that was meant to constitute the covenant people also produced, by exposing and multiplying transgression (cf. 7:7-11), the full visibility of sin's depth. Where sin increased, grace 'increased all the more' — the law's unexpected function served the purpose of making the abundance of grace more evident."}
    ]
  },
  "6": {
    "3": [
      {"type": "shadow", "target": "Exod 14:21-22", "note": "Israel's passage through the Red Sea is the OT shadow of baptism into death that 1 Corinthians 10:2 makes explicit ('they were all baptized into Moses in the cloud and in the sea'). Paul's 'baptized into Christ Jesus' carries this typological structure: as Israel passed through the waters to escape Pharaoh's dominion into freedom, believers pass through baptism-into-death to escape sin's dominion into new life."}
    ],
    "4": [
      {"type": "allusion", "target": "Ps 16:10", "note": "The psalmist's confession that God will not 'let your faithful one see decay' — applied by Peter and Paul to Christ's resurrection (Acts 2:27-31; 13:35) — is the scriptural ground for Paul's claim that Christ 'was raised from the dead through the glory of the Father.' The Psalm establishes that the one in whom the Father delights will not remain in death; the resurrection is the Father's vindication of the Son."}
    ],
    "5": [
      {"type": "allusion", "target": "Isa 53:10-11", "note": "Isaiah's Servant who, after 'making his life an offering for sin... will see his offspring and prolong his days' and 'out of the anguish of his soul he shall see and be satisfied' — Paul's 'if we have been united with him in a death like his, we will certainly also be united with him in a resurrection like his' participates in the Isaianic post-mortem life of the Servant: suffering leads to resurrection-life, and those who share in the death share in the life."}
    ],
    "9": [
      {"type": "allusion", "target": "Hos 13:14", "note": "Hosea's declaration that God will 'ransom them from the power of the grave' and 'redeem them from death' — Paul applies this to Christ's resurrection in the sense that 'death no longer has mastery over him.' The death whose power Hosea invokes as subject to divine ransom is precisely the death whose power over Christ is permanently broken by the resurrection; Paul's 'cannot die again' is the completion of what Hosea's ransom-language anticipates."}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 26:19", "note": "'Your dead will live, LORD; their bodies will rise' — the prophetic vision of resurrection as the defeat of death that Isaiah 26 proclaims. Paul's appeal to 'offer yourselves to God as those who have been brought from death to life' grounds ethical transformation in the resurrection-status: believers are those who have passed through death into life, and their moral life should correspond to this eschatological reality."}
    ],
    "14": [
      {"type": "allusion", "target": "Jer 31:31-33", "note": "Jeremiah's new covenant promise that God will make a new covenant 'not like the covenant I made with their ancestors' — Paul's 'you are not under the law, but under grace' articulates the structural shift Jeremiah foresaw. The Mosaic covenant (law-based, externally imposed) has been superseded by the new covenant (grace-based, internally written by the Spirit); not under law means living in the Jeremianic new covenant age."}
    ],
    "16": [
      {"type": "allusion", "target": "Deut 30:15-20", "note": "Moses sets before Israel 'life and prosperity, death and destruction' as the consequences of the two ways — obedience leading to life, disobedience leading to death. Paul's 'whether you are slaves to sin, which leads to death, or to obedience, which leads to righteousness' restructures the Deuteronomic two-ways within the new covenant frame: the obedience Paul commends is not law-keeping but the obedience of faith in Christ."}
    ],
    "17": [
      {"type": "allusion", "target": "Jer 31:33", "note": "'I will put my law in their minds and write it on their hearts' — Paul's 'you have come to obey from your heart the pattern of teaching that has now claimed your allegiance' is the fulfillment of the Jeremianic new covenant: the obedience is from the heart, not merely external compliance. The gospel's 'pattern of teaching' (typos didachēs) has done what Jeremiah promised the Spirit would do — inscribed obedience at the level of desire and will."}
    ],
    "22": [
      {"type": "allusion", "target": "Ezek 36:27", "note": "God's promise in the new covenant: 'I will put my Spirit in you and move you to follow my decrees and be careful to keep my laws' — Paul's 'benefit you reap leads to holiness, and the outcome is eternal life' describes the fruit of Spirit-led obedience that Ezekiel foresaw as the new covenant's distinctive: not law-compliance driven by fear but Spirit-moved holiness leading to life."}
    ],
    "23": [
      {"type": "allusion", "target": "Gen 2:17", "note": "'When you eat from it you will certainly die' — the death that is 'the wages of sin' in Paul's declaration has its OT ground in the garden commandment: sin's consequence is death, established at the first prohibition. Paul's axiom ('the wages of sin is death') is the universal generalization of the garden pronouncement; the gift of eternal life is the reversal of what death brought in at the Fall."}
    ]
  },
  "7": {
    "2": [
      {"type": "allusion", "target": "Num 5:12-19", "note": "The Mosaic legislation on the husband's authority over a wife — the marriage bond as the legal frame for Paul's analogy of law-bondage. Paul uses the universal principle of marriage-dissolution-by-death to explain the believer's release from the law: as a widow is free to remarry when her husband dies, the believer who has 'died' through union with Christ is free to be 'married to another' — the risen Lord."}
    ],
    "4": [
      {"type": "allusion", "target": "Hos 2:19-20", "note": "God's covenant declaration: 'I will betroth you to me forever; I will betroth you in righteousness and justice, in love and compassion' — Paul's 'you also died to the law through the body of Christ, that you might belong to another, to him who was raised from the dead' activates the new-covenant betrothal imagery of Hosea. The new relationship ('belong to another') is the Hosean betrothal-to-God language, now applied to the union with Christ that the resurrection makes possible."}
    ],
    "6": [
      {"type": "allusion", "target": "Jer 31:31-34", "note": "The new covenant promise of a different mode of covenant life — 'not like the covenant I made with their ancestors... I will put my law in their minds and write it on their hearts' — is what Paul invokes when he writes 'we serve in the new way of the Spirit, and not in the old way of the written code.' The 'written code' (gramma) is the Mosaic law externally inscribed; the 'new way of the Spirit' is the Jeremianic new covenant now present."},
      {"type": "allusion", "target": "Ezek 36:26-27", "note": "Ezekiel's promise of a new spirit within, replacing the heart of stone with a heart of flesh, and the indwelling Spirit moving covenant obedience from within — Paul's 'new way of the Spirit' is the Ezekielian new heart made actual. The contrast between old-code and Spirit-way corresponds exactly to Ezekiel's contrast between stony-heart compliance and Spirit-animated response."}
    ],
    "7": [
      {"type": "quote", "target": "Exod 20:17", "note": "Paul quotes the tenth commandment verbatim: 'You shall not covet' — the only commandment that targets desire rather than external act. Paul's choice of this commandment is theologically precise: it exposes the depth of sin as not merely behavioral but constitutive of the will itself. The commandment that names the internal motion of desire is the one sin exploits to produce 'every kind of coveting' (v8), showing that the law's power to reveal sin operates at the level of desire, not only action."}
    ],
    "9": [
      {"type": "type", "target": "Gen 2:16-17", "note": "The garden commandment — 'you are free to eat from any tree in the garden; but you must not eat from the tree of the knowledge of good and evil' — is the original structural parallel to what Paul describes: 'once I was alive apart from the law; but when the commandment came, sin sprang to life and I died.' In Eden, the prohibition activated desire; when transgressed, it brought death. Paul's autobiographical account recapitulates the Adamic pattern — the commandment that defined life became the occasion of sin's activation and death's arrival."}
    ],
    "10": [
      {"type": "allusion", "target": "Lev 18:5", "note": "'Keep my decrees and laws, for the person who obeys them will live by them' — Paul's 'the very commandment that was intended to bring life actually brought death' stands in deliberate tension with Lev 18:5's life-promise. The law was designed for life; sin corrupted the relationship, turning the instrument of life into the occasion of death. The failure is not the commandment's but sin's, which seized the commandment as its weapon (v11)."}
    ],
    "11": [
      {"type": "allusion", "target": "Gen 3:13", "note": "Eve's confession: 'The serpent deceived me, and I ate' — Paul's 'sin, seizing the opportunity afforded by the commandment, deceived me' uses the same vocabulary (exapatāō, to deceive thoroughly). Sin as an active personal force operating through the commandment to bring death is Paul's restatement of the serpent's operation in Genesis 3: the commandment intended for life was used by an alien power to bring death. The Adamic pattern is recapitulated in every human encounter with the law."}
    ],
    "12": [
      {"type": "allusion", "target": "Ps 19:7-9", "note": "The psalmist's triple praise: 'the law of the LORD is perfect, refreshing the soul; the statutes of the LORD are trustworthy; the commands of the LORD are radiant... the precepts of the LORD are right' — Paul's 'the law is holy, and the commandment is holy, righteous and good' restates the psalmist's threefold characterization. Having identified sin as the problem (not the law), Paul affirms what the psalm has always declared about the Torah's character."}
    ],
    "14": [
      {"type": "allusion", "target": "Isa 50:1", "note": "God's indictment: 'you were sold because of your sins' — Paul's 'I am unspiritual, sold as a slave to sin' uses the same slave-by-sale metaphor Isaiah applies to Israel's exile. The condition of being sold under sin's power is the Isaianic condition of covenant breach: the people who belong to God have been alienated from him and are in bondage to a foreign power, a bondage only God can reverse."}
    ],
    "22": [
      {"type": "allusion", "target": "Ps 119:97", "note": "'Oh, how I love your law! I meditate on it all day long' — Paul's 'in my inner being I delight in God's law' echoes the psalmist's affective love for the Torah. The conflict Paul describes — delight in the law at the level of the inner person, but slavery to sin in the flesh — recapitulates the psalmist's orientation. The one who loves the law and the one who cannot keep it are the same person, and that tension is the condition the gospel resolves."}
    ],
    "24": [
      {"type": "allusion", "target": "Ps 130:1-8", "note": "The psalm's cry from 'the depths' for the Lord's rescue: 'Out of the depths I cry to you, LORD... with you there is forgiveness... he himself will redeem Israel from all their sins' — Paul's 'What a wretched man I am! Who will rescue me from this body that is subject to death?' is the psalm's cry internalized. The desperate acknowledgment of the depths, followed by the confidence in divine rescue (v25), is the psalm's structure compressed into Paul's exclamation and its immediate answer."}
    ],
    "25": [
      {"type": "allusion", "target": "Isa 25:8-9", "note": "Isaiah's eschatological triumph: 'he will swallow up death forever... this is the LORD, we trusted in him; let us rejoice and be glad in his salvation' — Paul's 'thanks be to God, who delivers me through Jesus Christ our Lord!' is the spontaneous doxology that corresponds to Isaiah's eschatological joy. The rescue from the body-of-death that Paul announces is the Isaianic swallowing-of-death, now present through the resurrection of Christ and the Spirit's work in the believer."}
    ]
  }
}

def main():
    existing = load_echo('romans')
    merge_echo(existing, ROMANS_ECHOES)
    save_echo('romans', existing)
    print('Romans 4–7 echoes written.')

if __name__ == '__main__':
    main()
