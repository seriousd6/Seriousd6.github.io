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
  "1": {
    "1": "<p>2 Thessalonians appears to be the second letter to the same congregation, written shortly after 1 Thessalonians (ca. 50-51 CE) from Corinth. The identical letter-opening (Paul, Silas, Timothy; grace and peace) signals continuity with the first letter while the body addresses a new and more acute crisis. Writing a second letter to the same community was unusual in ancient correspondence — the urgency of the eschatological confusion in Thessalonica required direct follow-up beyond the first letter's teaching.</p>",
    "2": "<p>'Grace and peace to you from God the Father and the Lord Jesus Christ' — the Pauline benediction combines <em>charis</em> (grace — the Hellenistic letter's conventional greeting word, transformed into a theological term) with <em>eirēnē</em> (peace — the Hebrew shalom, the LXX equivalent of the Jewish letter-opening). The two-source formula 'from God the Father and the Lord Jesus Christ' treats both as a single divine source of the greeting — an early Christological affirmation embedded in liturgical convention.</p>",
    "3": "<p>'Your faith is growing more and more and the love all of you have for one another is increasing' — Paul's observation of growth in a community enduring persecution functions as both encouragement and evidence. In ancient moral philosophy, virtue was thought to be strengthened by practice under difficulty; Paul reframes this: the faith and love growing under pressure are not the Thessalonians' achievement but God's work in them. The thanksgiving in vv.3-4 establishes their perseverance as praiseworthy before the churches, activating the honor-recognition mechanism in an ancient Mediterranean community.</p>",
    "4": "<p>'Among God's churches we boast about your perseverance and faith' — <em>enkauchasthai</em> (to boast/glory in) was normally considered a vice in Greco-Roman ethics — self-promotion at others' expense. Paul inverts it: the boast is not about himself but about the Thessalonians, and the audience is not a civic gathering but a network of communities. The Maccabean literature (2 Macc 6-7; 4 Macc) celebrated Jewish martyrs who maintained faithfulness under persecution; Paul's framing of the Thessalonians' suffering places them in this tradition of honored sufferers.</p>",
    "5": "<p>'Evidence that God's judgment is right, and as a result you will be counted worthy of the kingdom of God' — the question of why the righteous suffer was a central theodicy problem in Second Temple Judaism. The book of Job, 4 Ezra, and the Apocalypse of Baruch all wrestle with it. Paul's answer here is not philosophical but eschatological: the suffering is the evidence (<em>endeigma</em> — proof, demonstration) that God's judgment will vindicate the afflicted and punish the afflictors — the lex talionis applied eschatologically.</p>",
    "6": "<p>'God is just: he will pay back trouble to those who trouble you' — the principle of divine retributive justice (YHWH repays in kind) is rooted in the Torah (Deut 32:35; 'Vengeance is mine, I will repay') and the Psalms of lament (Ps 94:1-3). The expectation that God will vindicate the persecuted was not a Christian innovation but a foundational Jewish conviction that Jesus applied to his disciples (Matt 5:10-12; Luke 6:20-23) and Paul inherits. The comfort is not that revenge is permitted but that justice is guaranteed.</p>",
    "7": "<p>'Relief to you who are troubled, and to us as well. This will happen when the Lord Jesus is revealed from heaven in blazing fire with his powerful angels' — the parousia as the moment of <em>anesis</em> (relief, relaxation of tension — like a bowstring released) grounds the comfort in eschatology. The language of revelation (apokalypsis) from heaven draws on Jewish apocalyptic theophanies: YHWH's descent in fire (Exod 19:18; Isa 66:15; Dan 7:9-10). That these theophanic attributes are applied to Jesus's parousia is the Christological move.</p>",
    "8": "<p>'He will punish those who do not know God and do not obey the gospel of our Lord Jesus' — 'not knowing God' (<em>tois mē eidosin theon</em>) is the Jewish description of Gentile paganism (Jer 10:25; Ps 79:6) — moral failure rooted in theological ignorance. 'Not obeying the gospel' addresses those who heard and refused — a different category. The two phrases may address two groups (pagan Gentiles; Jewish opponents) or be a comprehensive description of all who reject the divine revelation. The combination of knowing and obeying treats the gospel as both information and demand.</p>",
    "9": "<p>'Everlasting destruction and shut out from the presence of the Lord and from the glory of his might' — <em>aionios olethros</em> (everlasting/age-long destruction) is not the annihilation of existence but the destruction of relationship: being 'shut out' (<em>apo prosōpou tou kyriou</em> — away from the face of the Lord) is the content of the punishment. The face of YHWH was the source of blessing and life in Jewish thought (Num 6:25-26; Ps 80:3); to be excluded from it is to be excluded from the source of life itself. The glory of his might echoes the theophany tradition (Exod 15:6; Isa 2:10, 19, 21).</p>",
    "10": "<p>'On the day he comes to be glorified in his holy people and to be marveled at among all those who have believed' — the parousia is the day of Christ's glorification in and through his community. The Shekinah-glory tradition (God's presence dwelling in his people — Exod 29:43; Ezek 43:4-5) is here applied to Christ's coming: the holy ones become the venue of his manifest glory. 'To be marveled at' (<em>thaumasthēnai</em>) echoes the LXX psalms where the nations marvel at YHWH's works — the audience of the parousia is cosmic, not private.</p>",
    "11": "<p>'We constantly pray for you, that our God may make you worthy of his calling' — the prayer for worthiness (<em>axiōsē</em> — make worthy, count worthy) reflects Jewish traditions about being found worthy of the age to come (Pirke Avot 4:1; 4 Ezra 9:7-8; the Dead Sea Scrolls community's self-understanding as the righteous remnant). Paul's prayer is not that the Thessalonians will achieve worthiness by effort but that God will effect it — the passive divine action on the community is the mechanism.</p>",
    "12": "<p>'That the name of our Lord Jesus may be glorified in you, and you in him' — the mutual glorification formula reflects the Isaianic servant and servant-community relationship: YHWH is glorified in his servant (Isa 49:3) and the servant shares in YHWH's glory (Isa 60:1-2). Paul applies this OT covenant-community pattern to Christ and the church. The phrase 'according to the grace of our God and the Lord Jesus Christ' treats grace as the ground of the entire mutual-glorification relationship — it is received, not achieved.</p>"
  },
  "2": {
    "1": "<p>2 Thessalonians was apparently written shortly after 1 Thessalonians (ca. 50-51 CE) to address a new crisis: someone had claimed (perhaps with a forged letter from Paul, v. 2) that 'the day of the Lord has come'. This eschatological collapse-of-tense caused some Thessalonians to abandon work (<em>ataktōs peripatountas</em>, 3:11: living in idleness) in anticipation of the immediate end. Paul's response establishes preconditions for the Day: the apostasia and the revelation of the lawless one must come first. Whether 2 Thessalonians is authentically Pauline or deutero-Pauline is contested; stylistic differences from 1 Thessalonians and the elaborate eschatological schema have led some scholars to posit a later pseudonymous author, though early attestation and close similarity to 1 Thess language support Pauline authorship.</p>",
    "2": "<p>'Not to become easily unsettled or alarmed by the teaching allegedly from us — whether by a prophecy or by word of mouth or by letter' — the three channels (prophetic word, oral report, letter) represent the full range of apostolic communication. The alarm apparently came from one of these, possibly a forged letter (Paul explicitly counters forgery with his autograph in 3:17). The word <em>saleuthēnai</em> (to shake, as in shaking a boat) conveys the disorienting effect of the false teaching: the community had been destabilized. The false claim ('the day of the Lord has come') would explain the ataktos behavior of ch 3 — why work if the eschaton has arrived?</p>",
    "3": "<p>'For that day will not come until the rebellion occurs and the man of lawlessness is revealed' — Paul establishes two preconditions for the Day. The 'rebellion' (<em>apostasia</em>) drew on Second Temple eschatological expectation of a great falling-away before the End (4 Ezra 5:1-2; CD 1:13-14; Matt 24:10-12). The 'man of lawlessness' (<em>ho anthrōpos tēs anomias</em>) is shaped by the Danielic anti-God figure (Dan 7-12) and the historical template of Antiochus IV Epiphanes, who desecrated the Jerusalem temple in 167 BCE (Dan 11:31; 1 Macc 1:54) — the prototypical sacrilegious ruler whose pattern anticipates the eschatological opponent.</p>",
    "4": "<p>'He will oppose and exalt himself over everything that is called God or is worshiped, so that he sets himself up in God's temple, proclaiming himself to be God' — the self-deifying language directly echoes Daniel's 'willful king' (Dan 11:36) and the prince of Tyre's claim 'I am a god' (Ezek 28:2). Antiochus IV Epiphanes fulfilled an earlier version of this pattern: he installed an altar to Zeus Olympios in the Jerusalem temple (1 Macc 1:54; 2 Macc 6:2) — the 'abomination of desolation' referenced in Dan 9:27 and Jesus's apocalyptic discourse (Matt 24:15). Paul's 'man of lawlessness' represents the eschatological fulfillment of this recurring historical pattern of sacrilegious self-deification.</p>",
    "5": "<p>'Don't you remember that when I was with you I used to tell you these things?' — Paul's appeal to foundational teaching given during the founding visit is significant: the Thessalonians already had catechetical instruction about the preconditions for the Day of the Lord. This was standard eschatological teaching in the early church, shaped by Daniel and the apocalyptic tradition, not a Pauline innovation. The rhetorical question — 'don't you remember?' — signals that the current crisis stems not from ignorance of the teaching but from allowing a false claim to override what they already knew.</p>",
    "6": "<p>'You know what is holding him back' — the 'restrainer' (<em>to katechon</em>, v.6 neuter; <em>ho katechon</em>, v.7 masculine) was known to the Thessalonians but is deliberately left unspecified for the letter's other readers. Primary interpretations: (1) the Roman empire/emperor — the political order that prevents chaos (Tertullian, Chrysostom); this fits the political context of writing under Rome and may explain the vagueness as self-censorship. (2) Paul's own mission — the preaching must reach all nations before the End (cf. Matt 24:14); Paul is the restraining force until his work is complete. (3) The Holy Spirit. (4) Michael the archangel (from Daniel 12). The deliberate ambiguity is itself a clue that specificity would have been politically dangerous.</p>",
    "7": "<p>'The secret power of lawlessness is already at work' — <em>mystērion tēs anomias</em> (mystery of lawlessness) adapts the mystery-religion vocabulary that permeated the Hellenistic world: a hidden reality with cosmic significance, known only to initiates. Paul had already used <em>mystērion</em> for the hidden plan of God now revealed in Christ (Rom 16:25; Eph 1:9). The mystery of lawlessness is the counter-mystery: the eschatological opponent's power is already active, hidden, waiting for its full disclosure when the restrainer is removed. The pattern of hidden vs. revealed is the apocalyptic framework for understanding history's present ambiguity.</p>",
    "8": "<p>'The Lord Jesus will overthrow with the breath of his mouth and destroy by the splendor of his coming' — Paul draws on Isa 11:4 (the messianic king who kills the wicked with the rod of his mouth, with the breath of his lips). The verb <em>analōsei</em> (consume, destroy) from the same tradition appears in LXX Isa 11:4. The 'splendor of his coming' (<em>epiphaneia tēs parousias</em>) combines the <em>epiphany</em> vocabulary of Hellenistic ruler-cult (the divine appearance of the king) with the Pauline parousia-theology: the lawless one's parody-parousia (his own arrival in power) is annihilated by the genuine parousia of the Lord Jesus.</p>",
    "9": "<p>The 'signs and wonders and false miracles' (<em>sēmeia kai terata kai dynameis</em>) of the lawless one mirror the authentic apostolic credentials Paul cites for his own ministry (2 Cor 12:12: signs, wonders, and mighty works). The mirror-imagery is deliberate: the eschatological opponent operates as a satanic parody of apostolic ministry, complete with sign-works that deceive those who refuse to love the truth (v. 10). Second Temple Jewish literature (4 Ezra; the Testament of Moses; and later rabbinic material) preserves traditions of a final demonic figure who deceives Israel before divine deliverance — Paul's 'man of lawlessness' belongs to this tradition.</p>",
    "10": "<p>'All the ways that wickedness deceives those who are perishing. They perish because they refused to love the truth and so be saved' — the mechanism of deception is moral, not intellectual: those who perish did not merely fail to understand but actively 'refused' (<em>ouk edexanto</em> — did not receive/welcome) the love of truth. In ancient rhetoric, the hardened heart that refuses to receive truth was a recognized ethical category (cf. Plato's treatment of the tyrant whose soul is disordered; the Stoic who rejects rational self-governance). Paul's is the theological version: rejection of the gospel has moral roots, not merely epistemic ones.</p>",
    "11": "<p>'For this reason God sends them a powerful delusion so that they will believe the lie' — the divine judicial hardening is an OT pattern applied eschatologically. YHWH hardened Pharaoh's heart (Exod 4:21; 7:3) after Pharaoh hardened his own; YHWH sent Isaiah to blind a people who had already closed their own eyes (Isa 6:9-10; cited in John 12:40; Acts 28:26-27). The delusion God sends is a response to, not the cause of, the prior rejection of truth. Paul applies this pattern to the eschatological moment: those who refused the gospel are confirmed in their rejection by divine judgment.</p>",
    "12": "<p>'All will be condemned who have not believed the truth but have delighted in wickedness' — the active verb 'delighted' (<em>eudokēsantes</em> — took pleasure in, were well pleased with) marks the condemnation as morally earned rather than arbitrarily imposed. Those condemned did not merely fail to believe; they actively enjoyed wickedness. The polarity truth/lie, belief/unbelief, pleasure-in-goodness/pleasure-in-wickedness frames the eschatological division as rooted in the dispositions people cultivated during their lives.</p>",
    "13": "<p>'God chose you as firstfruits (<em>aparche</em>) to be saved through the sanctifying work of the Spirit and through belief in the truth' — <em>aparche</em> (firstfruits) was the technical term for the first portion of the harvest consecrated to God in Levitical law (Lev 23:10-11; Num 15:20-21). Paul uses it to locate the Thessalonian community within the eschatological harvest: they are the first installment of the larger gathering of the redeemed. The double mechanism — Spirit's sanctifying work and the community's believing response — reflects Paul's characteristic combination of divine initiative and human response without subordinating either.</p>",
    "14": "<p>'He called you to this through our gospel, that you might share in the glory of our Lord Jesus Christ' — the calling (<em>ekaleō</em>) vocabulary is covenantal: YHWH calling Israel is the foundational OT act (Isa 41:9; 43:1). Paul places the gospel in this role: the apostolic proclamation is the instrument through which God's eschatological call reaches the Gentiles. The goal of the calling is participatory glory (<em>peripoiēsin doxēs</em> — obtaining of glory): the Thessalonians are not merely delivered from wrath but drawn into the glory that Christ possesses (cf. John 17:22; Rom 8:18; 2 Cor 3:18).</p>",
    "15": "<p>'Stand firm and hold fast to the teachings we passed on to you, whether by word of mouth or by letter' — <em>paradoseis</em> (traditions, teachings passed on) was the technical Jewish term for the oral transmission of authoritative teaching (Torah she-be'al peh — the oral Torah alongside the written Torah). Paul claims the same status for apostolic tradition: a body of teaching transmitted through both oral and written channels that the community is to hold as authoritative. The command 'stand firm' (<em>stēkete</em>) returns to the military posture of 1:3's 'perseverance' — doctrinal stability under eschatological pressure.</p>",
    "16": "<p>'May our Lord Jesus Christ himself and God our Father, who loved us and by his grace gave us eternal encouragement and good hope' — the wish-prayer form addressed jointly to Christ and the Father (as in 1 Thess 3:11) again uses a singular verb for the joint action of two persons. 'Eternal encouragement' (<em>paraklēsin aiōnion</em>) and 'good hope' (<em>elpida agathēn</em>) are eschatological qualities: encouragement that does not end with present circumstances and hope grounded in the coming age rather than present outcomes.</p>",
    "17": "<p>'Encourage your hearts and strengthen you in every good deed and word' — the eschatological teaching of vv.1-16 is given an explicitly moral end: the knowledge of the Day's preconditions and God's electing purposes is meant to produce stability (<em>stērixai</em> — strengthen, make firm) in action and speech. This is the paraenetic function of apocalyptic: eschatological disclosure that makes moral demands. The goal is not speculative knowledge about the End but a life shaped by the certainty of God's purposes.</p>"
  },
  "3": {
    "1": "<p>'Pray for us that the message of the Lord may spread rapidly and be honored' — the prayer request for the gospel's rapid spread (<em>trechē</em> — run) uses the athletic imagery that Paul applies elsewhere to the apostolic mission (1 Cor 9:24-26; Gal 2:2; Phil 2:16). Thessalonica, as a city on the Via Egnatia, was itself a node in the network through which the gospel had spread (1 Thess 1:8); Paul's prayer points outward to the continued diffusion of the message from community to community along the Roman road network.</p>",
    "2": "<p>'Pray that we may be delivered from wicked and evil people, for not everyone has faith' — Paul's request for protection from opponents reflects the actual dangers of itinerant mission in the Roman world: hostility from synagogue communities, civic authorities, and local power brokers. The phrase 'not everyone has faith' (<em>ou gar pantōn hē pistis</em>) is an understatement with a sardonic edge — Paul's missionary experience had shown that the gospel was not universally welcomed. The prayer request assumes that human opposition and divine protection operate simultaneously within a single providential framework.</p>",
    "3": "<p>'The Lord is faithful, and he will strengthen you and protect you from the evil one' — the divine faithfulness (<em>pistos</em>) is contrasted with the human unfaithfulness of v.2 ('not everyone has faith' — <em>pistis</em>). YHWH's <em>emet</em> (faithfulness, reliability) was the covenantal foundation: what God commits to doing, he does (Deut 7:9; Lam 3:23). The protection 'from the evil one' (<em>apo tou ponērou</em>) may be 'from evil' (neuter) or 'from the evil one' (masculine — Satan); Paul's concern about Satan's obstruction of the mission (1 Thess 2:18) favors the personal reading.</p>",
    "4": "<p>'We have confidence in the Lord that you are doing and will continue to do the things we command' — <em>peithō</em> (confidence, trust) in the Lord (not in the Thessalonians directly) locates the ground of apostolic confidence in divine faithfulness rather than community track record. This is a pastoral strategy: by expressing confidence the apostle creates social pressure toward compliance through the honor-shame mechanism — the community must now either fulfill the expectation or face the shame of disappointing the apostle's expressed trust.</p>",
    "5": "<p>'May the Lord direct your hearts into God's love and Christ's perseverance' — <em>hupomone Christou</em> (the endurance/perseverance of Christ) is best read as Christ's own perseverance modeled for believers, not perseverance toward Christ. The Christological pattern of endurance was central to early Christian paraenesis: Jesus's patient suffering became the template for the community's response to persecution (Heb 12:1-3; 1 Pet 2:21-23). 'God's love' and 'Christ's endurance' together define the community's character: loved by God and shaped by Christ's pattern of faithful suffering.</p>",
    "6": "<p>'In the name of the Lord Jesus Christ, we command you, brothers and sisters, to keep away from every believer who is idle and disruptive' — the military term <em>ataktōs</em> (out of rank/disorderly) appears in ancient papyri for workers who abandoned their duties or walked off a job. In the Thessalonian context the ataktoi were likely those who had abandoned work in anticipation of the imminent End. The community-discipline command 'keep away from' (<em>stellesthai</em> — to withdraw from) falls short of full excommunication (cf. 1 Cor 5:2, 13) — it is social distancing meant to produce shame without severing the relationship entirely.</p>",
    "7": "<p>'You yourselves know how you ought to follow our example. We were not idle when we were with you' — the imitation-of-the-apostle motif (<em>mimēsthai</em>) was a standard educational method: students were expected to observe and replicate the teacher's way of life. Paul's labor was not merely economic necessity but a deliberate demonstration: the apostle who works with his hands models the life he commands. The founding visit was simultaneously a preaching event and a living display of the apostolic pattern.</p>",
    "8": "<p>'Nor did we eat anyone's food without paying for it. On the contrary, we worked night and day, laboring and toiling so that we would not be a burden' — manual labor (<em>kopos kai mochthos</em> — toil and hardship) was socially degrading for educated males in Greco-Roman culture. Artisans and craftsmen occupied a lower rung than educated men who used their minds. Paul's tent-making (Acts 18:3) in Thessalonica was a deliberate choice to accept social degradation in order to model what he commanded and to refuse the patron-client dynamic that would have given wealthy community members leverage over the apostolic message.</p>",
    "9": "<p>'Not because we do not have the right to such help, but in order to offer ourselves as a model for you to imitate' — Paul asserts his apostolic right to financial support (the right of the one who proclaims the gospel, 1 Cor 9:14, citing Deut 25:4 and the Lord's instructions) while explaining his deliberate non-use of that right as a pedagogical choice. The waiver of a legitimate right for the community's benefit is itself a modeling of the pattern he commends (cf. 1 Cor 9:12; 2 Cor 11:7-9).</p>",
    "10": "<p>'The one who is unwilling to work shall not eat' — this rule may echo a Jewish wisdom principle (Prov 10:4; 12:11; 13:4) but its specific application to community food-sharing is distinctly early Christian: the early Jerusalem community shared resources (Acts 2:44-45), and Paul likely coordinated similar community provision in his Gentile churches. The rule 'unwilling to work' not 'unable to work' — it addresses voluntary idleness, not incapacity. Those who had chosen not to work because of eschatological enthusiasm were to be refused community meals, not as punishment but as correction.</p>",
    "11": "<p>'We hear that some among you are idle and disruptive. They are not busy; they are busybodies' — Paul's wordplay (<em>mēden ergazomenous alla periergazomenous</em> — working nothing but working around) is a rhetorical <em>paronomasia</em> that is difficult to reproduce in English. The 'busybodies' were apparently interfering in others' affairs, perhaps exhorting them to prepare for the End, stop working, and join them in eschatological expectation. The disruption was social as well as economic: such behavior violated the community norms of minding one's own business (1 Thess 4:11) and maintaining the respect of outsiders.</p>",
    "12": "<p>'Such people we command and urge in the Lord Jesus Christ to settle down and earn the food they eat' — the command is simultaneously apostolic (<em>parangellomen</em> — we command) and pastoral (<em>parakalomen</em> — we urge). The double register reflects the urgency: these community members were disrupting the social fabric and bringing the community into disrepute. 'Earn the food they eat' (<em>esthiōsin ton heautōn arton</em> — eat their own bread) was a Hellenistic idiom for financial self-sufficiency — the person who eats their own bread owes nothing to others and is a full social agent.</p>",
    "13": "<p>'Never tire of doing what is good' — the brief command to the non-ataktoi addresses a different risk: compassion fatigue or discouragement from having to support idle community members. The word <em>enkakēsēte</em> (grow weary, lose heart) appears also in Gal 6:9 ('let us not grow weary of doing good, for in due season we will reap if we do not give up') and Luke 18:1 ('always to pray and not give up'). The perseverance in good work is itself an eschatological posture: doing good now in light of the coming harvest.</p>",
    "14": "<p>'Take special note of anyone who does not obey our instruction in this letter. Do not associate with them, in order that they may feel ashamed' — the community-discipline mechanism is shame (<em>entrape</em> — to be turned in on oneself, to feel shame). In an honor-shame culture, social exclusion was a powerful corrective: the person marked and shunned by the community loses the public honor that is essential to their identity. The goal is not punishment but restoration — shame produces self-examination and potential repentance. The instruction assumes the letter will be read publicly (5:27 of 1 Thess established this practice).</p>",
    "15": "<p>'Yet do not regard them as an enemy, but warn them as you would a fellow believer' — the crucial qualifier: the discipline is remedial, not punitive. <em>Nouthetein</em> (admonish, warn — the same word used in 1 Thess 5:12 for community leaders' function) is pastoral speech aimed at correction. The offender remains a 'brother' (<em>adelphon</em>) — the familial language is maintained even in discipline. Ancient moral philosophers distinguished between punishing enemies and correcting friends; Paul applies the friend-correction model to intra-community discipline.</p>",
    "16": "<p>'Now may the Lord of peace himself give you peace at all times and in every way' — the closing benediction invoking the 'Lord of peace' (<em>Kyrios tēs eirēnēs</em>) recalls the Jewish shalom-benediction: the priestly blessing of Num 6:24-26 (YHWH lift up his face upon you and give you peace) and the Isaiah vision of the Prince of Peace (Isa 9:6). The peace being sought is not absence of conflict — 2 Thessalonians has been a letter about conflict, both external (persecution) and internal (the ataktoi) — but the eschatological shalom that is YHWH's gift alone.</p>",
    "17": "<p>'I, Paul, write this greeting in my own hand, which is the distinguishing mark in all my letters. This is how I write' — the explicit mention of autograph (<em>idiochirou</em> — my own hand) as a verification mark directly addresses the concern of 2:2 (being deceived by a letter 'from us'). In antiquity, letters were normally dictated to a secretary (<em>amanuensis</em>) who wrote in a standard hand; the sender's personal signature or postscript in their own handwriting authenticated the letter. Paul's claim that this is his practice in all letters (also mentioned in Gal 6:11; 1 Cor 16:21) establishes a verifiable standard against forgery.</p>",
    "18": "<p>'The grace of our Lord Jesus Christ be with you all' — the closing formula matches the pattern established in the first letter (1 Thess 5:28), creating a recognizable Pauline signature that itself contributes to authentication. The addition of 'all' (<em>pantōn</em>) may be deliberate: the letter's discipline of the ataktoi could create the impression that some are excluded from grace. The inclusive 'all' ensures that even the ataktoi are addressed in the benediction — they remain within the community's sphere even while being disciplined.</p>"
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
