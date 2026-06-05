"""
Combined script: 1 Thessalonians (original + context + christ) and
2 Thessalonians (echo + original + context + christ) — all chapters.

1 Thess echo already complete; this adds the other three layers for 1 Thess
and all four layers for 2 Thess.
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
# 1 THESSALONIANS — original / context / christ
# ============================================================

ONETHESS_ORIGINAL = {
  "1": {
    "9": "<p><strong>eis to douleuein theo zōnti kai alēithinō kai anameinai ton huion autou ek ton ouranon</strong>: 'to serve a living and true God and to wait for his Son from heaven.' The Thessalonian conversion summary (turned from idols → serve the living God → await the Son) is Paul's earliest explicit parousia-expectation statement. The three-fold movement frames the Christian life: conversion, present service, and eschatological waiting. <em>Anamenein</em> (to await/wait for) is a word of eager, sustained expectation — not passive resignation but active orientation toward the returning Son."
  },
  "4": {
    "14": "<p><strong>ei gar pisteuomen hoti Iesous apethanen kai aneste houtōs kai ho theos tous koimēthentas dia tou Iesou axei syn auto</strong>: 'For since we believe that Jesus died and rose again, even so, through Jesus, God will bring with him those who have fallen asleep.' The first explicit eschatological argument in Paul's letters grounds the resurrection of believers in the resurrection of Jesus: the same God who raised Jesus will raise the dead. The verb sequence — <em>apethanen</em> (died) + <em>aneste</em> (rose) — is the primitive creedal formula (cf. 1 Cor 15:3-4), here applied to the parousia-hope.</p>",

    "16": "<p><strong>en keleusmati en phōnē archangelou kai en salpinggi theou katabēsetai</strong>: 'with a cry of command, with the voice of an archangel, and with the sound of the trumpet of God, he will descend.' Three apocalyptic signals accompany the parousia: <em>keleuema</em> (a command-shout, used of military orders and of the divine word of creation), <em>archaggelou phōnē</em> (archangel's voice — the archangel Michael as warrior-herald in Dan 10:13, 21; 12:1; Rev 12:7), and <em>salpinx theou</em> (the trumpet of God — the shofar-gadol of Isa 27:13; Matt 24:31; 1 Cor 15:52 — the eschatological signal for gathering). All three signals assert the unmistakable, cosmic, publicly announced character of the return.</p>"
  },
  "5": {
    "2": "<p><strong>he hemera kyriou hos kleptes en nykti houtōs erchetai</strong>: 'the day of the Lord comes like a thief in the night.' The 'Day of the Lord' (<em>hemera kyriou</em>) is Paul's use of the prophetic Day-of-YHWH tradition (Amos 5:18-20; Isa 2:12-22; Joel 2:11; Zeph 1:14-18) — originally a day of divine judgment. The 'thief in the night' image for its unexpectedness appears also in Jesus's eschatological teaching (Matt 24:43-44; Luke 12:39-40) and later NT texts (2 Pet 3:10; Rev 3:3; 16:15), indicating a shared tradition. Paul applies it to the parousia: its timing is unknown, its arrival will be sudden, and preparedness (not calculation of dates) is the appropriate response.</p>"
  }
}

ONETHESS_CONTEXT = {
  "2": {
    "1": "<p>Thessalonica (modern Thessaloniki) was the capital of the Roman province of Macedonia, its largest city (population ca. 40,000-65,000), and a major port on the Via Egnatia. As a 'free city' (<em>civitas libera</em>) with its own civic assembly (<em>demos</em>), it had significant autonomy within the Roman provincial system. Paul's accusers before the city authorities (Acts 17:6: 'these who have turned the world upside down') charge him with treason: 'they are all acting against the decrees of Caesar, saying that there is another king, Jesus.' The messianic claim of Jesus's kingship was politically dangerous in a city with a significant imperial cult presence (worshippers of Julius Caesar, Augustus, and the emperors were established in Thessalonica).</p>"
  },
  "4": {
    "13": "<p>The specific concern Paul addresses (those who have died before the parousia, vv. 13-18) arose because the Thessalonian community expected the parousia imminently and was distressed that some of their number had died before it arrived. This is the earliest written evidence of Christians struggling with delayed parousia and the death of community members. Paul's response does not retreat from imminent expectation but uses it to comfort: the dead have not missed the parousia — they will be raised first at the Lord's descent. The passage gave rise to later controversies about soul-sleep vs intermediate state, but Paul's primary concern is comfort (<em>parakaleite</em>, v. 18), not metaphysical precision about the intermediate state.</p>"
  }
}

ONETHESS_CHRIST = {
  "4": {
    "14": "<p>A direct revelation: 'Since we believe that Jesus died and rose again, even so, through Jesus, God will bring with him those who have fallen asleep.' The resurrection of the dead is grounded directly in the resurrection of Jesus — not as an analogy but as a causal mechanism. The same God who raised Jesus exercises the same resurrection-power toward those who died in Jesus. The eschatological hope of 1 Thessalonians is not abstract immortality but the specific, Jesus-mediated, bodily resurrection that the first Christian creed announced. Christology is the foundation of eschatology.</p>",

    "16": "<p>A direct revelation: 'The Lord himself will descend from heaven with a cry of command.' <em>Autos ho Kyrios</em> (the Lord himself) — Paul emphasizes personal presence: the parousia is not a divine energy-event or angelic visitation but the personal return of the same Lord who ascended. The 'Lord' (<em>Kyrios</em>) is Jesus, the risen and ascended one, now enthroned at the right hand of the Father (Phil 2:9-11), who will come personally to complete his saving work. The three apocalyptic signals (cry, archangel, trumpet) frame the personal return in cosmic-eschatological context.</p>"
  },
  "5": {
    "9": "<p>A direct revelation: 'God has not destined us for wrath but to obtain salvation through our Lord Jesus Christ, who died for us so that whether we are awake or asleep we might live with him.' The Christological ground of assurance: the Day-of-the-Lord warning (vv. 2-3) does not apply to believers because God's purpose for them is not wrath but salvation. The mechanism: Christ died for us (<em>hyper hemon</em>) — the substitutionary death is the basis for the assurance. 'Live with him' (<em>hama syn auto zōmen</em>) — the eschatological communion with Christ is both the goal and the ground of present courage in the face of the Day.</p>"
  }
}

# ============================================================
# 2 THESSALONIANS — echo + original + context + christ
# ============================================================

TWOTHESS_ECHO = {
  "1": {
    "7": [
      {"type": "fulfillment", "target": "Isa 66:15", "note": "When the Lord Jesus is revealed from heaven with his mighty angels in flaming fire — the Day-of-the-Lord theophany of Isa 66:15 (the LORD will come in fire and his chariots like the whirlwind) is applied to the parousia of Jesus; the YHWH-theophany becomes the Christ-parousia"},
      {"type": "allusion", "target": "Dan 7:10", "note": "A thousand thousands served him and ten thousand times ten thousand stood before him — the Danielic throne-room with innumerable angels; Paul's 'mighty angels' at the parousia echoes the angelic army of Daniel's vision"}
    ]
  },
  "2": {
    "4": [
      {"type": "allusion", "target": "Dan 11:36", "note": "Who opposes and exalts himself against every so-called god — Daniel's description of the willful king who exalts himself above every god; the man of lawlessness of 2 Thess 2 is Paul's application of the Danielic anti-God figure to the eschatological opponent"},
      {"type": "allusion", "target": "Ezek 28:2", "note": "I am a god, I sit in the seat of the gods — the prince of Tyre's self-deification in Ezekiel; the man of lawlessness who seats himself in God's temple echoes this prophetic type of human self-exaltation"}
    ],
    "8": [
      {"type": "fulfillment", "target": "Isa 11:4", "note": "The Lord Jesus will kill him with the breath of his mouth — YHWH's messianic king who smites the earth with the rod of his mouth and with the breath of his lips kills the wicked; Paul applies this messianic judgment-action directly to the parousia of Jesus destroying the lawless one"}
    ]
  }
}

TWOTHESS_ORIGINAL = {
  "2": {
    "3": "<p><strong>he apostasia prōton kai apokaluphthē ho anthropos tes anomias ho huios tes apōleias</strong> (<em>hē apostasia prōton kai apokaluphthē ho anthrōpos tēs anomias ho huios tēs apōleias</em>): 'the rebellion (<em>apostasia</em>) comes first, and the man of lawlessness, the son of destruction, is revealed.' <em>Apostasia</em> — in LXX political rebellion and religious apostasy are both covered by this word; whether Paul means a final cosmic falling-away from faith or a political rebellion is debated. <em>Ho huios tes apōleias</em> (son of destruction) is the same phrase used of Judas in John 17:12 — linking the ultimate opponent to the prototypical betrayer. <em>Apokaluphthē</em> (is revealed): the passive suggests God controls even the timing of the opponent's disclosure.</p>",

    "6": "<p><strong>to katechon / ho katechon</strong>: 'what is restraining / he who restrains' — the most debated phrase in 2 Thessalonians. The neuter (<em>to katechon</em>, v. 6) and masculine (<em>ho katechon</em>, v. 7) alternate, suggesting either a power/principle and a personal restrainer, or a rhetorical variation for the same referent. Major interpretive proposals: (1) the Roman empire/emperor (the power that prevents chaos — Tertullian, Chrysostom); (2) Paul's own missionary preaching that must be completed first; (3) the Holy Spirit who restrains evil until the end; (4) a divine decree or angel. The deliberate vagueness may be security-conscious rhetoric — naming the restrainer directly in a letter could be politically dangerous.</p>"
  }
}

TWOTHESS_CONTEXT = {
  "2": {
    "1": "<p>2 Thessalonians was apparently written shortly after 1 Thessalonians (ca. 50-51 CE) to address a new crisis: someone had claimed (perhaps with a forged letter from Paul, v. 2) that 'the day of the Lord has come'. This eschatological collapse-of-tense caused some Thessalonians to abandon work (<em>ataktōs peripatountas</em>, 3:11: living in idleness) in anticipation of the immediate end. Paul's response establishes preconditions for the Day: the apostasia and the revelation of the lawless one must come first. Whether 2 Thessalonians is authentically Pauline or deutero-Pauline is contested; stylistic differences from 1 Thessalonians and the elaborate eschatological schema have led some scholars to posit a later pseudonymous author, though early attestation and close similarity to 1 Thess language support Pauline authorship.</p>",

    "9": "<p>The 'signs and wonders and false miracles' (<em>sēmeia kai terata kai dynameis</em>) of the lawless one mirror the authentic apostolic credentials Paul cites for his own ministry (2 Cor 12:12: signs, wonders, and mighty works). The mirror-imagery is deliberate: the eschatological opponent operates as a satanic parody of apostolic ministry, complete with sign-works that deceive those who refuse to love the truth (v. 10). Second Temple Jewish literature (4 Ezra; the Testament of Moses; and later rabbinic material) preserves traditions of a final demonic figure who deceives Israel before divine deliverance — Paul's 'man of lawlessness' belongs to this tradition.</p>"
  }
}

TWOTHESS_CHRIST = {
  "1": {
    "7": "<p>A direct revelation: 'When the Lord Jesus is revealed from heaven with his mighty angels in flaming fire, inflicting vengeance on those who do not know God and on those who do not obey the gospel of our Lord Jesus.' The parousia of Jesus is described using the vocabulary of YHWH's theophanic judgment in Isa 66 and Daniel — the same fire, angels, and judgment associated with YHWH's Day of the Lord are now associated with Jesus's return. The Christological identification is complete: the Day of the Lord is the Day of the Lord Jesus; the theophanic judge is Christ.</p>"
  },
  "2": {
    "8": "<p>A direct revelation: 'The Lord Jesus will kill him with the breath of his mouth and bring him to nothing by the appearance of his coming.' Paul applies the messianic victory-text of Isa 11:4 (the rod of his mouth, the breath of his lips) to Jesus at his parousia. The eschatological adversary — however powerful his signs and wonders and however extensive his deception — is annihilated by the mere breath-word of Jesus. The Christological power asymmetry is absolute: the lawless one's satanic-energy miracles against the breath of Christ's mouth. The parousia is therefore not a cosmic battle in which the outcome is uncertain but a disclosure that definitively ends the charade of the opponent's authority.</p>",

    "14": "<p>A direct revelation: 'To this end God called you through our gospel, so that you may obtain the glory of our Lord Jesus Christ.' The goal of calling is sharing Christ's glory (<em>peripoiēsin doxēs tou kyriou hemon Iesou Christou</em>). This echoes the Christological trajectory of Romans 8:30 (glorified) and Philippians 3:21 (conformed to Christ's glorious body). Christ's glory is not merely admired from outside but participated in — the eschatological destiny of believers is Christomorphic glory. The calling-gospel-glory chain frames Christian identity as Christologically determined from initiation to consummation.</p>"
  }
}

def main():
    # 1 Thessalonians (echo already exists; add original/context/christ)
    c = load_comm('mkt-original', '1thessalonians')
    merge_comm(c, ONETHESS_ORIGINAL)
    save_comm('mkt-original', '1thessalonians', c)
    print(f'1Thess original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', '1thessalonians')
    merge_comm(c, ONETHESS_CONTEXT)
    save_comm('mkt-context', '1thessalonians', c)
    print(f'1Thess context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', '1thessalonians')
    merge_comm(c, ONETHESS_CHRIST)
    save_comm('mkt-christ', '1thessalonians', c)
    print(f'1Thess christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    # 2 Thessalonians (all four layers)
    e = load_echo('2thessalonians')
    merge_echo(e, TWOTHESS_ECHO)
    save_echo('2thessalonians', e)

    c = load_comm('mkt-original', '2thessalonians')
    merge_comm(c, TWOTHESS_ORIGINAL)
    save_comm('mkt-original', '2thessalonians', c)
    print(f'2Thess original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', '2thessalonians')
    merge_comm(c, TWOTHESS_CONTEXT)
    save_comm('mkt-context', '2thessalonians', c)
    print(f'2Thess context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', '2thessalonians')
    merge_comm(c, TWOTHESS_CHRIST)
    save_comm('mkt-christ', '2thessalonians', c)
    print(f'2Thess christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

if __name__ == '__main__':
    main()
