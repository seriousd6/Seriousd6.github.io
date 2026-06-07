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
  "1": {
    "2": "<p>The thanksgiving period opening a Hellenistic letter was a conventional formula, typically addressed to the gods for the recipient's health. Paul transforms it: thanks go to God (not the Olympians), and the content is theological — the Thessalonians' faith, not their physical welfare. The continual prayer (<em>adialeiptōs</em> — without interruption) language suggests the synagogue pattern of fixed daily prayer, adapted into Christian community rhythm.</p>",
    "7": "<p>Macedonia and Achaia were the two Roman provinces covering modern Greece — Macedonia in the north, Achaia in the south. Thessalonica was the capital of Macedonia; Corinth was the administrative seat of Achaia. That a newly founded community in Thessalonica could become a <em>typos</em> (pattern, model) known across both provinces within weeks of Paul's departure signals the Via Egnatia's role as a news corridor: travelers constantly moved between cities, carrying reports of the new community.</p>"
  },
  "2": {
    "1": "<p>Thessalonica (modern Thessaloniki) was the capital of the Roman province of Macedonia, its largest city (population ca. 40,000-65,000), and a major port on the Via Egnatia. As a 'free city' (<em>civitas libera</em>) with its own civic assembly (<em>demos</em>), it had significant autonomy within the Roman provincial system. Paul's accusers before the city authorities (Acts 17:6: 'these who have turned the world upside down') charge him with treason: 'they are all acting against the decrees of Caesar, saying that there is another king, Jesus.' The messianic claim of Jesus's kingship was politically dangerous in a city with a significant imperial cult presence (worshippers of Julius Caesar, Augustus, and the emperors were established in Thessalonica).</p>",
    "4": "<p>'Approved by God to be entrusted with the gospel' (<em>dedokimasmetha</em> — tested and approved) uses the metallurgical language of assaying precious metals. In Greco-Roman culture, credentials were established by examining a philosopher's conduct and results — the proof was in the <em>tropos</em> (character and way of life). Paul reframes the test: the examiner is God, not human opinion, and the criterion is faithfulness to commission, not public applause.</p>",
    "5": "<p>The charges Paul preemptively denies — flattery (<em>kolakeia</em>), greed (<em>pleonexia</em>), and wearing a mask (<em>en prophasei pleonexias</em> — under pretext of greed) — were the standard accusations lodged against itinerant Sophists, wandering philosophers, and wonder-workers in the first century. Lucian of Samosata and Dio Chrysostom document these critiques extensively. Paul's defense is not an innovation; it is a deliberate engagement with the recognized criteria for distinguishing authentic teachers from charlatans in Greco-Roman public culture.</p>",
    "8": "<p>The sharing of 'our lives as well' (<em>tas heautōn psychas</em>) moves beyond ancient hospitality conventions into something more intimate. In patron-client culture, benefactors gave material resources; what set the Pauline mission apart was the offer of personal solidarity — eating, working, suffering alongside the community rather than dispensing goods from above. The nursing-mother image (v.7) and this verse together construct a counter-cultural portrait of leadership deliberately opposed to the social hierarchy that governed most relationships between teachers and students.</p>",
    "10": "<p>'Holy, righteous, and blameless' (<em>hosiōs kai dikaiōs kai amemptōs</em>) — the triad maps onto Jewish and Hellenistic virtue language simultaneously. <em>Hosios</em> (holy, pious) carried religious connotations; <em>dikaios</em> (just, righteous) covered civic and relational ethics; <em>amemptos</em> (blameless, without fault) was the language of formal legal or social review. Paul's appeal to the Thessalonians as witnesses (<em>martyres</em>) mirrors legal testimony: the community can testify to what they observed, just as God is the final witness to what was hidden.</p>",
    "11": "<p>The father-children metaphor (<em>patēr tekna</em>) activates the <em>patria potestas</em> structure of ancient households — the father had legal authority, obligations of provision and instruction, and the responsibility of moral formation. Jewish fathers were expected to instruct their sons in Torah; Hellenistic fathers were responsible for their sons' philosophical and civic formation. Paul's paternal role was not sentimental — it carried the weight of a recognized social institution that both Jewish and Gentile Thessalonians would have understood.</p>",
    "13": "<p>The distinction between a human word (<em>logos anthrōpōn</em>) and the word of God (<em>logos theou</em>) reflects the prophetic tradition: in Israel, the prophet's words were authoritative because they were YHWH's words, not the prophet's own opinion (Amos 1:3; Jer 23:16-22). Paul claims the same prophetic category for the apostolic proclamation. The phrase 'which is indeed at work' (<em>energeitai</em> — operating, actively at work) treats the word as an agent, not merely a message — a theme rooted in Isa 55:11 where the word accomplishes what God sends it to do.</p>",
    "15": "<p>'Who killed the Lord Jesus and the prophets' — the pattern of Israelite prophets being killed by their own people was a standard trope in Jewish self-critique (Neh 9:26; Jer 26:20-23; 2 Chr 36:15-16). The same tradition appears in Jesus' lament over Jerusalem (Luke 13:34). Paul places the death of Jesus within this already-established pattern of prophetic rejection, not as a novel charge against Jews as a group. The Judean churches (v.14) suffered from 'their own people' — the same intra-community conflict pattern Paul is invoking.</p>",
    "16": "<p>'The wrath has come upon them at last' (<em>ephthasen de ep' autous hē orgē eis telos</em>) — 'come upon' (<em>ephthasen</em> aorist) describes something that has already arrived, not merely future judgment. Some interpreters read this as a reference to the destruction of Jerusalem (70 CE, which would post-date Paul); others see a proleptic use of the aorist viewing the judgment as certain. In Jewish apocalyptic tradition, the measure of sin being 'filled up' (Gen 15:16; Dan 8:23) signals that divine patience has reached its limit — a recognized eschatological motif.</p>",
    "18": "<p>'Satan blocked our way' — the figure of the adversary (<em>Satanas</em>, from Hebrew <em>śāṭān</em> — the accuser or obstructer) obstructing divine purposes appears in Jewish and early Christian thought as a coherent agency responsible for resistance to God's work (Job 1-2; Zech 3:1-2; 1 Chr 21:1). Paul does not identify the specific mechanism of obstruction — illness, opposition, legal barriers, travel difficulties — but frames it theologically. The practical obstacle is given a cosmic interpretation.</p>",
    "20": "<p>'You are our glory and joy' — the <em>kauchēsis</em> (boasting/glory) language in Paul consistently refers to what one can legitimately display before God and others as evidence of one's apostolic labor (cf. Phil 4:1, 1 Cor 15:31). In the Hellenistic honor system, a teacher's glory was his students' achievement. Paul transforms this: the Thessalonians are his <em>stephanos</em> (crown) not before men but before the Lord at his coming. The eschatological frame makes the community itself the currency of apostolic honor.</p>"
  },
  "3": {
    "4": "<p>'We kept telling you that we would be persecuted' — the predictive element is significant: Paul apparently taught during the founding visit that suffering was not a sign of divine abandonment but a structural feature of the new age (cf. Acts 14:22). This was catechetical preparation (<em>prokategelloumen</em> — we told beforehand), not improvised theodicy after the fact. The expectation of tribulation before the End was part of Second Temple eschatological teaching (Dan 12:1; 4 Ezra 7:12-14; the 'birth pangs' tradition).</p>",
    "6": "<p>Timothy's return as a courier with news was the primary means of community contact across the ancient world. Letters could be sent, but face-to-face news from a trusted envoy was more reliable and more emotionally resonant — the envoy could convey tone, physical health, emotional state. The 'good news' (<em>euangelisamenou</em> — gospel-announced) that Paul uses for Timothy's report is the same verb as for proclaiming the gospel; Paul deliberately echoes the language to signal how significant this news was to him.</p>",
    "7": "<p>'Distress and persecution' (<em>anankē kai thlipsis</em>) — <em>anankē</em> (compulsion, constraint, distress) refers to external necessity that presses in on a person; <em>thlipsis</em> (pressure, affliction) is the physical and social pressure of persecution. Together they describe the actual experience of the Pauline mission: financial precarity, social ostracism, legal threats. That the Thessalonians' steadfastness provided encouragement (<em>parekletheimen</em>) in such circumstances illustrates the genuinely mutual nature of Pauline pastoral relationships.</p>",
    "8": "<p>'Now we really live since you are standing firm' — the conditional life-dependence Paul expresses mirrors ancient friendship conventions (<em>philia</em>) where a friend's welfare was genuinely one's own. Aristotle's treatment of friendship as a second self (<em>allos autos</em>) is the background framework. Paul pushes beyond philosophical friendship into something eschatologically charged: the Thessalonians' faithfulness is evidence that his labor was not in vain (<em>eis kenon</em>), which in apostolic terms means their standing firm validates his mission.</p>",
    "9": "<p>The rhetorical question 'how can we thank God enough?' (<em>tina gar eucharistian dunametha tō theō antapodounai</em>) belongs to the ancient convention of expressing indebtedness so great that reciprocity is impossible. In patron-client relationships, the greatest gifts were those that could not be repaid — creating a bond of permanent gratitude. Paul applies this to God: the joy the Thessalonians' faith produces is a gift for which no adequate thanksgiving exists.</p>",
    "10": "<p>'Night and day' (<em>nuktos kai hēmeras</em>) — the Jewish day was reckoned from evening to evening (Gen 1:5), so 'night and day' is the Jewish sequence (night first, then day). Paul's prayer life followed the Jewish fixed-hour pattern adapted for the diaspora: morning, afternoon, and evening prayers. The phrase signals constant, patterned intercession, not random supplication. 'Supply what is lacking in your faith' (<em>katartisai ta husterēmata</em>) implies the founding visit left incomplete what could only be filled by sustained teaching.</p>",
    "11": "<p>The wish-prayer form 'may our God and Father himself and our Lord Jesus clear the way' uses <em>kateuthunai</em> (straighten, direct) with a singular verb governing both 'God and Father' and 'our Lord Jesus' as joint agents of a single action. This grammatical unity has been noted as an early indicator of the high Christology that would be developed more fully in the later Pauline letters and the conciliar tradition — two persons, one singular verbal action.</p>",
    "12": "<p>The overflowing love prayer (<em>pleonasai kai perisseuai</em> — increase and overflow) uses commercial abundance language: not merely sufficient but spilling over. The direction is twofold — 'for each other and for everyone else' — moving from the inner community outward, which reflects a Jewish ethical principle: you cannot love the neighbor you do not see if you cannot first love the brother you do see (cf. 1 John 4:20 for the same logic applied differently).</p>"
  },
  "4": {
    "1": "<p>The transition 'as for other matters' (<em>loipon oun</em>) marks the shift from thanksgiving to paraenesis — the moral instruction section of the letter. Paraenesis was a recognized rhetorical category: the teacher delivering moral exhortation to a community that already knew the content, reminding rather than informing. The appeal 'as in fact you are living... do this more and more' is the standard paraenetic posture: affirm present practice, then intensify the demand. Complaining that conduct is inadequate would have been socially alienating; affirming and escalating was the approved form.</p>",
    "2": "<p>'By the authority of the Lord Jesus' (<em>dia tou kyriou Iēsou</em>) — Paul grounds the moral instructions not in his personal authority but in the Lord's commission. In the ancient world, a messenger who spoke <em>dia</em> (through, by means of) someone spoke with that person's delegated authority — like an ambassador who speaks for the emperor. The Thessalonians are receiving not Paul's ethical opinions but the Lord's directives through Paul's transmission.</p>",
    "6": "<p>'Wrong or take advantage of a brother or sister in this matter' — the phrase 'in this matter' links back to the sexual ethics of vv.3-5, though some commentators read it as a transition to business ethics (defrauding in commercial dealings). In Thessalonica's commercial environment, both applications were relevant: sexual exploitation and commercial fraud were both recognized violations of the covenant community's purity code. The warning 'the Lord will punish all those who commit such sins' invokes the divine as the ultimate enforcer of community ethics when human courts were inadequate or inaccessible.</p>",
    "7": "<p>'God did not call us to be impure but to live a holy life' — the call (<em>ekaleō</em>) language is covenantal: YHWH called Israel to holiness as the constitutive mark of election (Lev 11:44-45; 19:2). Paul applies the same covenantal logic to the Thessalonian Gentiles — their sexual ethics are not a cultural preference but a response to divine vocation. The contrast 'impurity vs. holiness' (<em>akatharsia vs. hagiasmos</em>) maps onto the Levitical purity system reapplied to the moral domain.</p>",
    "8": "<p>'Anyone who rejects this instruction does not reject a human being but God' — the logic mirrors the Deuteronomic prophetic commission: rejecting the prophet's word was rejecting the one who sent the prophet (1 Sam 8:7; Luke 10:16). Paul intensifies it by specifying 'the very God who gives you his Holy Spirit' — the Spirit's presence is the marker of the new covenant community (Ezek 36:26-27; Joel 2:28-29). Rejecting the Spirit-backed instruction severs oneself from the community constituted by that Spirit.</p>",
    "10": "<p>'All of God's family throughout Macedonia' — the kinship language of early Christianity (<em>adelphoi</em> — brothers and sisters) was not metaphorical decoration but a social claim: the community functioned like a family, with obligations of mutual support, honor, and loyalty. The extension of this family across geographic space ('throughout Macedonia') to communities the Thessalonians had never met built a trans-local network of mutual obligation — the same network Paul would later coordinate for the Jerusalem collection (1 Cor 16:1-4).</p>",
    "12": "<p>'Win the respect of outsiders' (<em>euschēmonōs peripatein pros tous exō</em>) — reputation management in an honor-shame culture was not merely social nicety but communal survival. If the community's conduct was socially disruptive (not working, depending on others, creating public disturbance), it would face hostility from civic authorities and neighbors. Paul's instruction to 'mind your own business and work with your own hands' is a deliberate counter to the social disruption caused by eschatological enthusiasm among some who had stopped working because the End was near.</p>",
    "13": "<p>The specific concern Paul addresses (those who have died before the parousia, vv. 13-18) arose because the Thessalonian community expected the parousia imminently and was distressed that some of their number had died before it arrived. This is the earliest written evidence of Christians struggling with delayed parousia and the death of community members. Paul's response does not retreat from imminent expectation but uses it to comfort: the dead have not missed the parousia — they will be raised first at the Lord's descent. The passage gave rise to later controversies about soul-sleep vs intermediate state, but Paul's primary concern is comfort (<em>parakaleite</em>, v. 18), not metaphysical precision about the intermediate state.</p>",
    "14": "<p>'We believe that Jesus died and rose again' — this is a compressed kerygmatic formula, one of the earliest credal summaries in the Pauline corpus. The verb pair 'died (<em>apethanen</em>) and rose (<em>anestē</em>)' in the aorist contrasts with the sleeping metaphor for believers in vv.13-15: Jesus' death is called death, not sleep, because his resurrection is already accomplished. The argument structure is analogy from certainty to hope: as Jesus' resurrection is certain fact, so the resurrection of those in him is logically entailed.</p>",
    "18": "<p>'Encourage one another with these words' (<em>parakalein</em> — encourage, exhort, comfort) — the eschatological teaching in vv.13-17 is explicitly given a pastoral, community function: it is to be used as mutual encouragement. This reflects the early church's practice of reading apostolic letters aloud in community gatherings (5:27) where the content would be immediately applicable. The teaching is not speculative eschatology for its own sake but grief-management theology for a community that had lost members and feared their fate.</p>"
  },
  "5": {
    "1": "<p>'About times and dates' (<em>chronōn kai kairōn</em>) — the distinction between <em>chronos</em> (calendar time, duration) and <em>kairos</em> (appointed moment, decisive time) is standard in Greek rhetoric. Jesus used the same pair in Acts 1:7 when refusing to specify the timing of the End. Paul's claim that he does not need to write about this implies the community already had teaching on the subject — the question of timing was apparently a live concern in a community anxious about their deceased members and the imminent parousia.</p>",
    "4": "<p>'You are not in darkness' — the contrast of light and darkness was used in apocalyptic literature to distinguish the elect from the world (1QS 1:9-10; Testament of Levi 19:1). Paul applies it specifically to eschatological readiness: the Day of the Lord will not surprise the Thessalonians because they belong to the era that the Day inaugurates. This is not a prediction about their emotional state but an ontological claim about their community identity — they are already living in the light of the age that is dawning.</p>",
    "6": "<p>'Let us be awake (<em>grēgorōmen</em>) and sober (<em>nēphōmen</em>)' — watchfulness was a recognized virtue in military and civic contexts: sentries were expected to remain awake on duty; citizens were expected to be alert to civic threats. <em>Nēphō</em> (sobriety) contrasted specifically with wine-induced incapacity. The pairing creates a picture of full sensory and moral alertness appropriate to soldiers on watch, an image Paul develops explicitly in v.8 with the armor metaphor.</p>",
    "7": "<p>The observation that 'those who sleep, sleep at night, and those who get drunk, get drunk at night' is not merely descriptive — it was a recognized moral typology. Nighttime was the realm of disorder, vice, and concealment; daytime was the realm of accountability, transparency, and honor. The Epicurean and Stoic schools alike treated nighttime excess as a failure of self-control (<em>enkrateia</em>) that the wise person avoided. Paul uses the cultural commonplace to reinforce the ethical logic: belonging to the day means acting as day-people, not night-people.</p>",
    "10": "<p>'Whether we are awake or asleep' — in context, 'awake and asleep' resume the language of 4:13-17 (the living and the dead), not the metaphorical sleep of v.6-7. The eschatological unity 'we may live together with him' is the pastoral point: death before the parousia does not sever one from the community or from Christ. Both the living and the dead are equally secure in their future — a claim that addresses the specific grief of the Thessalonian community.</p>",
    "11": "<p>'Build each other up' (<em>oikodomeite</em> — build, edify) is an architectural metaphor Paul uses throughout his letters for the construction of the community (1 Cor 14:3-5; Eph 4:12-16). The image would have resonated in a city with significant public building projects — Thessalonica's forum, basilicas, and temples were visible markers of Roman urban power. Paul appropriates the building metaphor for community formation, locating the significant construction in human relationships rather than civic monuments.</p>",
    "13": "<p>'Hold them in the highest regard in love because of their work' — honor (<em>hēgeisthai hyperekperissou</em> — to consider as abundantly beyond) is the operative social currency. Leaders in the early church had no formal legal authority; their influence depended entirely on the community's voluntary recognition. Paul does not tell the Thessalonians to obey their leaders but to honor them — the honor-system mechanism by which influence operated in ancient communities. The ground for honor is 'their work' (<em>ergon</em>), not their status or origin.</p>",
    "14": "<p>The threefold pastoral taxonomy — 'warn the idle' (<em>ataktous nouthetein</em>), 'encourage the disheartened' (<em>oligopsychous paramytheisthai</em>), 'help the weak' (<em>antechesthai tōn asthenōn</em>) — distinguishes three distinct types of community members requiring different responses. <em>Ataktos</em> (idle, disorderly) likely refers to the eschatological enthusiasts who had stopped working (cf. 2 Thess 3:11); the <em>oligopsychoi</em> (small-souled, disheartened) are those grieving or anxious; the <em>astheneis</em> (weak) may be those struggling with moral failure or faith. One-size-fits-all pastoral response is precisely what this verse resists.</p>",
    "15": "<p>'Nobody pays back wrong for wrong' — the prohibition of revenge was distinctive in both Jewish and early Christian ethics against the background of Mediterranean honor culture, where requiting injury was expected and failure to do so was shameful. Seneca's <em>De Ira</em> and Plutarch's essays on anger document the philosophical difficulty of moderating the retribution impulse. Jewish tradition (Lev 19:18; Prov 20:22) had long prohibited revenge; Jesus' teaching radicalized it (Matt 5:38-48). Paul assumes this shared tradition without citing it.</p>",
    "17": "<p>'Pray continually' (<em>adialeiptōs proseuchesthai</em>) — the adverb <em>adialeiptōs</em> (without ceasing, constantly) appears in Jewish prayer traditions to describe the pattern of the righteous person who maintains constant orientation toward God even outside formal prayer times. The Qumran community organized its communal life around fixed prayer hours (morning, noon, evening). Paul does not mandate specific times but urges the disposition of constant prayerful orientation — a posture that makes prayer the default mode rather than a special activity.</p>",
    "18": "<p>'Give thanks in all circumstances' — Stoic philosophy praised the sage who maintained equanimity (<em>euthymia</em>) regardless of circumstances; Paul's instruction is similar in form but different in ground: thanksgiving is not achieved by detachment but by theological conviction about God's purposes. 'For this is God's will for you in Christ Jesus' grounds the thanksgiving imperative covenantally — it is not a cultural preference but what God intends for his people. The Pauline triad 'rejoice, pray, give thanks' (vv.16-18) forms a rhythm of the Spirit-directed life.</p>",
    "20": "<p>'Do not treat prophecies with contempt' (<em>prophēteias mē exoutheneite</em>) — the Thessalonian community apparently had prophetic activity, and some members were dismissive of it. In the Corinthian correspondence Paul would elaborate the proper ordering of prophetic gifts (1 Cor 14); here the brief command suggests that either the prophetic message about the parousia was being ignored, or that charismatic speech was being suppressed in favor of order. The balance of v.20-21 — 'do not despise' but 'test all things' — is the mature apostolic position.</p>",
    "22": "<p>'Reject every kind of evil' (<em>apo pantos eidous ponērou apechesthe</em>) — <em>eidos</em> can mean 'appearance' (avoid every appearance of evil) or 'kind/form' (avoid every kind of evil). The latter is more linguistically probable in Koine Greek. The command completes the test-and-hold sequence of vv.21-22: hold what is good, release what is evil. In a community practicing prophetic discernment, the practical implication is that identified false prophecy must not merely be noted but actively rejected.</p>",
    "24": "<p>'The one who calls you is faithful, and he will do it' — the faithfulness of God (<em>pistos ho kalōn</em> — faithful is the one calling) is a covenantal anchor: YHWH's reliability in completing what he has begun is a recurring affirmation in Jewish prayer and prophecy (Deut 7:9; Isa 49:7; Lam 3:23). Paul invokes it as the ground for confidence about sanctification: the completion of the work God began at calling is guaranteed by God's own character. The Thessalonians are not responsible for achieving their own blamelessness — they are responsible for cooperating with the God who will accomplish it.</p>",
    "25": "<p>'Brothers and sisters, pray for us' — the request for reciprocal prayer reverses the normal benefactor-client structure where the greater party prays for the lesser. Paul's routine request for community prayer for the apostolic team (Rom 15:30-31; 2 Cor 1:11; Phil 1:19) models a mutuality that was unusual in the ancient world: the apostle needs what the community can give. This is not rhetorical humility but theological conviction about the body's interdependence.</p>",
    "28": "<p>'The grace of our Lord Jesus Christ be with you' — the Pauline letter closing formula replaced the standard Greek letter ending (<em>errōso</em> — farewell) with a benediction. Grace (<em>charis</em>) in the salutation (1:1) and the closing creates an inclusio: the letter is framed by the divine gift that makes the community possible. The specifically Christological attribution ('of our Lord Jesus Christ' rather than 'of God') in letter closings is consistent across the Pauline corpus (Gal 6:18; Phil 4:23; 2 Thess 3:18) and represents a fixed liturgical formula for early Christian assemblies.</p>"
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
