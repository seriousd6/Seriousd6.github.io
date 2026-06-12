"""
MKT Christ Commentary — Judges chapters 4–6
Run: python3 scripts/zc-christ-judges-4-6.py

Every verse receives an entry connecting it to the trajectory toward Christ.

Ch4: Deborah/Barak — prophetess-judge type; Sisera's defeat; Jael's tent-peg;
     no-glory-to-Barak → glory to a woman → ultimately glory to the despised Christ
Ch5: Song of Deborah — theophany poetry, stars fighting for YHWH, solar benediction
Ch6: Gideon's call — Angel of YHWH theophany, weakness as the locus of divine power,
     YHWH-Shalom altar, Spirit-clothing, fleece signs

Typological/Christological keys:
- Deborah as prophetess-judge: Christ as prophet, priest, and king (all three offices)
- Jael's tent-peg: unexpected agent crushing the enemy's head (Gen 3:15; Heb 2:14)
- Song ch5 v31: the righteous shining like the sun — Matt 13:43 / Rev 1:16
- The YHWH-Shalom altar (6:24): Christ as our peace (Eph 2:14)
- Spirit-clothing Gideon (6:34): the Spirit without measure on Christ (John 3:34)
- Fleece: patient divine accommodation of weak faith (John 20:27 — Thomas)
- Gideon's inadequacy (6:15): the pattern of chosen weakness (1 Cor 1:27-29)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

CHRIST = {
  "4": {
    "1": "<p>Israel 'again did evil' — the cycle of apostasy that Judges chronicles is the lived proof that no human deliverer breaks the pattern permanently. Each judge saves Israel for a generation; after the judge dies, the cycle resets. This recurring failure points structurally toward the need for a deliverer who does not die, whose saving work is not undone by his absence. Jesus addresses this directly: 'I am the living one. I died, and behold I am alive forevermore' (Rev 1:18). The once-for-all nature of Christ's death and the permanence of his resurrection means the cycle is permanently broken — he does not die and leave Israel without a deliverer.</p>",
    "4": "<p>Deborah is a prophetess who judges Israel — the only judge who exercises prophetic authority before military action. She prefigures Christ who holds all three mediatorial offices permanently: prophet (John 1:45 — Moses wrote of him; Deut 18:15 — the prophet like Moses), priest (Heb 4:14 — our great high priest), and king (Rev 19:16 — King of kings). That Deborah must fill this role in the absence of adequate male leadership is the text's critique of her generation — and it points forward to the one man who will perfectly fulfill all three offices, leaving no gap requiring exceptional individuals to fill.</p>",
    "9": "<p>'The road you are going on will not lead to your glory, for YHWH will sell Sisera into the hand of a woman.' The transfer of glory from Barak to an unexpected agent anticipates the cross: 'God chose what is foolish in the world to shame the wise; God chose what is weak in the world to shame the strong' (1 Cor 1:27). The Messiah came 'not to be served but to serve, and to give his life as a ransom for many' (Matt 20:28). The glory in Judges shifts to a woman with a tent peg; in the gospel it shifts to a carpenter's son on a Roman cross. The pattern is the same: divine victory through the agent no one expected.</p>",
    "14": "<p>'Rise, for this is the day on which YHWH has given Sisera into your hand.' The prophetic perfect — YHWH speaks future deliverance as accomplished — is the mode of all OT prophecy about Christ: 'He was wounded for our transgressions' (Isa 53:5, perfect tense). YHWH's certainty about the outcome precedes the battle; Christ's certainty about his victory precedes the cross: 'Take heart; I have overcome the world' (John 16:33). The 'this is the day' formula (cf. Ps 118:24 — 'This is the day that YHWH has made') is the language of decisive covenant action — the day of YHWH arriving in saving power.</p>",
    "15": "<p>'YHWH routed Sisera' — the divine warrior acts directly while the human army pursues. This pattern anticipates the gospel: Christ defeats sin, death, and the devil on the cross, and the church's role is to pursue and announce that victory, not to accomplish it. 'The weapons of our warfare are not of the flesh but have divine power to destroy strongholds' (2 Cor 10:4). The victory has already been won; the mission of the church is the mopping-up operation after the decisive battle of the resurrection.</p>",
    "21": "<p>Jael's tent peg through Sisera's temple is the most graphic fulfillment of the Gen 3:15 principle in the pre-monarchic period: the enemy is brought down by an unexpected agent through a blow to the head. Heb 2:14-15: 'that through death he might destroy the one who has the power of death, that is, the devil, and deliver all those who through fear of death were subject to lifelong slavery.' Sisera fled thinking he had found refuge; Christ enters death itself and destroys it from within. 'The stone the builders rejected has become the cornerstone' (Ps 118:22) — the decisive victory comes through the despised, unexpected instrument.</p>",
    "23": "<p>'God humbled Jabin king of Canaan before the sons of Israel.' In Christ, the ultimate humbling of the powers happens: 'He disarmed the rulers and authorities and put them to open shame, by triumphing over them in him' (Col 2:15). Sisera's defeat is a type of the definitive defeat of 'the rulers and authorities in the heavenly places' (Eph 6:12) that Christ accomplished at the cross — not through military force but through the unexpected weapon of substitutionary death and resurrection.</p>"
  },
  "5": {
    "2": "<p>The Song of Deborah opens with praise for voluntary consecration — those who 'offered themselves willingly.' The NT develops this as the grammar of self-giving: Christ 'offered himself without blemish to God' (Heb 9:14); 'he gave himself for us' (Gal 1:4; 2:20). The worshipers in Ps 110:3 offer themselves willingly 'on the day of your power.' Deborah's song begins where the gospel begins: with free, unconstrained self-giving as the basis of deliverance.</p>",
    "4": "<p>The theophanic march of YHWH from Seir (vv4-5) is one of the OT's most ancient pictures of the divine warrior — the Lord marching through creation to rescue his people. This imagery reaches its NT fulfillment in Rev 19:11-16: 'He is clothed in a robe dipped in blood... From his mouth comes a sharp sword... He will tread the winepress of the fury of the wrath of God.' The theophanic warrior of the Exodus and Judges tradition returns in the final act of history as the crucified-and-risen Christ who fights the ultimate battle.</p>",
    "11": "<p>'There they rehearse the righteous acts of YHWH' — the victory song at the watering place is a type of the church's eucharistic proclamation: 'For as often as you eat this bread and drink the cup, you proclaim the Lord's death until he comes' (1 Cor 11:26). <em>Ṣiḏqôt YHWH</em> (righteous acts of YHWH) encompasses both his justice and his saving intervention — in Christ the 'righteous act' (<em>dikaiōma</em>, Rom 5:18) that justifies many is both the just judgment against sin and the saving deliverance from it.</p>",
    "20": "<p>'The stars fought from heaven, from their courses they fought against Sisera.' The heavenly host arrayed against YHWH's enemies anticipates the heavenly warfare of the NT: 'Then I saw heaven opened, and behold, a white horse!... The armies of heaven, arrayed in fine linen, white and pure, were following him' (Rev 19:11,14). The stars of Deborah's song are the angelic armies that fight alongside the divine warrior. Christ's final victory involves the mobilization of all heaven against the powers of darkness — the Song of Deborah is the early-poetry form of the Revelation 19 vision.</p>",
    "31": "<p>'So shall all your enemies perish, O YHWH! But let those who love him be like the sun as it rises in its might.' The Song's closing benediction is the OT's clearest anticipation of the resurrection-glory of Christ's people: 'Then the righteous will shine like the sun in the kingdom of their Father' (Matt 13:43). The 'sun rising in its might' is the image of unstoppable, growing glory — what the resurrection body will be. Paul: 'The body is sown in dishonor; it is raised in glory' (1 Cor 15:43). The covenant-lovers who participate in YHWH's victory will share in his radiant glory — the ultimate answer to the dying-judge cycle: a glory that does not fade.</p>"
  },
  "6": {
    "11": "<p>The Angel of YHWH sitting under the oak at Ophrah is a theophany — a pre-incarnate appearance of the Son in many patristic readings (Justin Martyr, Dialogue with Trypho 56; Irenaeus, Against Heresies III.6). The Angel speaks as YHWH in the first person (v16 — 'I will be with you'), yet is distinguishable from YHWH (v14 — 'YHWH turned to him'). This is the same figure as the Angel at the burning bush (Exod 3:2-6), at Peniel (Gen 32:24-30), and with Joshua (Josh 5:13-15). John 8:56 — 'Your father Abraham rejoiced that he would see my day; he saw it and was glad' — suggests Christ's pre-incarnate appearances to the patriarchs were real encounters with the eternal Son who would become incarnate.</p>",
    "12": "<p>'YHWH is with you, O mighty warrior' — addressed to a man hiding wheat from Midian. God calls things that are not as though they are (Rom 4:17). The same naming-into-being occurs at the annunciation: 'You will conceive and bear a son, and you shall call his name Jesus. He will be great and will be called the Son of the Most High' (Luke 1:31-32). YHWH sees Gideon not as he is (a frightened farmer) but as he will be (deliverer of Israel). Christ sees Simon not as he is (an impetuous fisherman) but as he will be (Peter, the rock, John 1:42) — the grammar of grace speaks future identity.</p>",
    "13": "<p>Gideon's theodicy question — 'If YHWH is with us, why has all this happened to us?' — is not rebuked but answered with commission. Christ himself prays the lament of Ps 22 from the cross (Matt 27:46) — not because he doubted the Father but because he was identifying with every person who has ever asked this question in the depths of suffering. The lament is covenant speech; it presupposes the relationship it protests. The God who answers lament with commission rather than explanation is the God revealed at Calvary: the cross is not an explanation of suffering but the God who enters it.</p>",
    "14": "<p>'Go in this might of yours and save Israel... Have I not sent you?' YHWH's answer to human inadequacy is always the same: not a credential but a commission backed by divine presence. Moses: 'I AM has sent me' (Exod 3:14); Gideon: 'Have I not sent you?'; the apostles: 'Go therefore... I am with you always' (Matt 28:19-20). Christ's own authority was derived: 'The Son can do nothing of his own accord, but only what he sees the Father doing' (John 5:19). The commission-plus-presence pattern culminates in Christ who is both the one sent (John 3:17) and the abiding presence (Matt 28:20).</p>",
    "15": "<p>'My clan is the weakest in Manasseh, and I am the least in my father's house' — the double self-diminishment establishes YHWH's consistent pattern of choosing the unlikely. 'God chose what is foolish in the world to shame the wise; God chose what is weak to shame the strong; God chose what is low and despised... so that no human being might boast in the presence of God' (1 Cor 1:27-29). This pattern runs from Abel, Jacob, Joseph, Moses, and David through to Christ himself — the carpenter's son from Galilee, of whom Nathanael asked 'Can anything good come out of Nazareth?' (John 1:46).</p>",
    "16": "<p>'I will be with you' — the <em>ʾehyeh ʿimmāk</em> formula from Exod 3:12 is YHWH's answer to every human objection. Its NT fulfillment is the Immanuel prophecy (Isa 7:14 → Matt 1:23 — 'God with us') and its incarnate realization: 'The Word became flesh and dwelt among us' (John 1:14). YHWH's presence-with reaches its ultimate form in Christ — not merely divine accompaniment but divine incarnation. The Gideon commissioning formula finds its deepest meaning in the Christmas announcement: YHWH-with-us is no longer a promise about support but a statement about the Son taking on human flesh.</p>",
    "22": "<p>Gideon's terror at seeing the Angel face-to-face reflects the ancient truth that direct divine encounter brings death (Exod 33:20). Christ's incarnation resolves this permanently: 'No one has ever seen God; the only God, who is at the Father's side, he has made him known' (John 1:18). The inaccessibility of the divine face that made every theophany potentially lethal is overcome in Christ who is the face of God made visible and touchable. 'That which we have seen with our eyes, which we looked upon and have touched with our hands, concerning the word of life' (1 John 1:1) — the incarnation is the permanent solution to the Gideon terror.</p>",
    "24": "<p>'YHWH-Shalom' — 'YHWH is Peace' — inscribed on Gideon's altar identifies the specific aspect of YHWH revealed at this encounter. Paul identifies Christ as the fulfillment: 'He himself is our peace, who has made us both one and has broken down in his flesh the dividing wall of hostility' (Eph 2:14). The YHWH-Shalom altar at Ophrah points forward to the cross where the ultimate peace-making occurs — not a temporary cessation of hostilities but the structural resolution of enmity between God and humanity, accomplished in the body of Christ.</p>",
    "34": "<p>'The Spirit of YHWH clothed Gideon' — the Spirit-clothing metaphor is the OT's most intimate description of charismatic empowerment. The anointing Spirit that 'rests upon' the Messiah (Isa 11:2; 61:1) and 'descends like a dove' at Jesus's baptism (Matt 3:16) is the same Spirit. The difference is degree and permanence: Gideon's clothing was for a crisis; Christ's anointing is without measure (John 3:34 — 'for he gives the Spirit without measure'). Gideon's Spirit-clothing shows what the coming Messiah's permanent Spirit-possession will accomplish on a cosmic scale.</p>",
    "36": "<p>The fleece test — seeking signs after already receiving a divine commission and miraculous fire (v21) — shows YHWH accommodating persistent human weakness without rebuke. This patience with doubting faith finds its clearest NT expression in Christ's response to Thomas: 'Put your finger here, and see my hands... Do not disbelieve, but believe' (John 20:27). Christ provides tangible proof for the doubter — the fleece principle extended into the resurrection appearances. Divine patience with weak faith is not theological embarrassment but covenant grace.</p>",
    "40": "<p>God's compliance with the second fleece test — the deliberate reversal that eliminates natural explanations — shows YHWH's willingness to provide repeated confirmation for genuine seekers. The man who needs two fleece tests will later need only an overheard dream (7:13-15) to go immediately into battle. Growth in faith is the trajectory: from requiring supernatural signs to trusting a providentially overheard word. 'Blessed are those who have not seen and yet have believed' (John 20:29) — the fleece stage is not permanent but the beginning of faith's journey toward trust without tangible confirmation.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', 'judges')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', 'judges', c)
    print(f'judges mkt-christ: wrote {sum(len(v) for v in CHRIST.values())} verses across ch 4-6')

if __name__ == '__main__':
    main()
