"""
Book Study Data — 1 Thessalonians
book_id: 1thessalonians
lang: greek

Run: python3 scripts/build-book-study-1thessalonians.py

Notes:
- Key vocabulary selected from Paul author group peaks plus 1 Thessalonians-specific terms
- The parousia section (4:13-18) uses imperial ceremonial vocabulary applied to Christ
- apantesis (meeting ceremony) is the technical term for the civic reception of a king
- harpazo (caught up) is the NT's rapture text and generates enormous theological controversy
- koimao (sleep for death) is Paul's pastoral counter to pagan grief without hope
"""

import json, os, sys

# ── boilerplate ──────────────────────────────────────────────────────────────

def load_book_study(book_id):
    path = f'data/workshop/book-study/{book_id}.json'
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def save_book_study(book_id, data):
    os.makedirs('data/workshop/book-study', exist_ok=True)
    path = f'data/workshop/book-study/{book_id}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'wrote {path} ({len(data.get("key_vocabulary", []))} vocab entries)')

def merge_book_study(existing, new_data):
    """Fill only fields not already present. Safe to re-run."""
    result = dict(existing)
    for key, val in new_data.items():
        if key not in result or not result[key]:
            result[key] = val
    return result

# ── content ──────────────────────────────────────────────────────────────────

BOOK_STUDY = {
    "bookId": "1thessalonians",

    "key_vocabulary": [
        {
            "code": "G3952",
            "lemma": "παρουσία",
            "translit": "parousia",
            "gloss": "coming",
            "significance": "παρουσία is the letter's dominant eschatological term, appearing four times (2:19; 3:13; 4:15; 5:23). In the Greco-Roman world, παρουσία was the technical term for the official visit of a king, emperor, or governor to a city — a formal, ceremonially significant arrival with civic processional protocols. Paul applies this royal term to Christ's return, claiming that the true sovereign visit that transforms all history belongs not to Caesar but to the Lord Jesus. The parousia is both the pastoral comfort for the grieving (4:13-18) and the motivating horizon for the sanctified life (3:13; 5:23)."
        },
        {
            "code": "G529",
            "lemma": "ἀπάντησις",
            "translit": "apantēsis",
            "gloss": "meeting",
            "significance": "ἀπάντησις in 4:17 ('to meet the Lord in the air') is the technical civic term for the ceremonial going-out by which citizens welcomed a visiting king. In Greek and Roman practice, when a dignitary arrived, the city's inhabitants would process outside the city gates to escort him in with honor. Paul uses this term for the believers' meeting with the descending Lord — but the direction matters: in the imperial ceremony, citizens go out to escort the king into the city. Applied to the parousia, this suggests not an ascent to heaven but a welcoming escort of the descending Christ as he comes to the earth. This reading challenges the 'rapture to heaven' interpretation of the passage."
        },
        {
            "code": "G726",
            "lemma": "ἁρπάζω",
            "translit": "harpazō",
            "gloss": "caught up",
            "significance": "ἁρπάζω ('to seize, snatch, catch away') in 4:17 — 'we will be caught up (ἁρπαγησόμεθα) together with them in the clouds to meet the Lord in the air' — is the source of the Latin <em>raptus</em> from which the English 'rapture' derives. The word denotes a powerful, sudden seizure — it is used of Paul being caught up to the third heaven (2 Cor 12:2-4) and of Philip being caught away by the Spirit (Acts 8:39). The verse describes the action God will perform at the parousia; it says nothing about whether this occurs before, during, or after a 'tribulation' — the elaborate pre/mid/post-trib rapture chronologies are constructions built on this passage and others, not conclusions the passage itself draws."
        },
        {
            "code": "G38",
            "lemma": "ἁγιασμός",
            "translit": "hagiasmos",
            "gloss": "sanctification",
            "significance": "ἁγιασμός ('sanctification, holiness') is the ethical heart of the letter. 'This is the will of God, your ἁγιασμός' (4:3) is Paul's most direct statement of God's moral purpose for believers. The context is specifically sexual ethics (4:4-8), where ἁγιασμός is contrasted with passionate lust like the Gentiles who do not know God. Thessalonica, like most Greco-Roman cities, had a culture of sexual permissiveness; the church's distinct sexual ethics was one of the most visible markers of its difference. The letter's eschatological frame reinforces the call: God will judge sexual immorality (4:6), and the coming Lord finds his people set apart (5:23)."
        },
        {
            "code": "G2837",
            "lemma": "κοιμάω",
            "translit": "koimaō",
            "gloss": "sleep",
            "significance": "κοιμάω ('to sleep') is Paul's pastoral euphemism for death in 4:13-15: 'we do not want you to be uninformed about those who are asleep (κοιμωμένων).' The metaphor was not unique to Christianity — Greek and Jewish texts used sleep for death — but Paul gives it specific content: those who sleep will be awakened by the one who died and rose. The argument in 4:14 moves from the resurrection of Jesus ('since we believe that Jesus died and rose') to the certainty of resurrection for those who sleep 'through Jesus.' The sleeping metaphor is not merely comforting language; it encodes the theology: as sleep implies waking, death implies resurrection. Paul addresses those who 'grieve as others do who have no hope' (4:13) — pagan grief without resurrection hope."
        },
        {
            "code": "G1680",
            "lemma": "ἐλπίς",
            "translit": "elpis",
            "gloss": "hope",
            "significance": "ἐλπίς appears in the letter's opening thesis (1:3) alongside faith and love: 'your work of faith and labor of love and steadfastness of ἐλπίς in our Lord Jesus Christ.' The three virtues form a temporal triad — faith looks to the past act of God, love operates in the present, hope orients toward the future parousia. ἐλπίς in 1 Thessalonians is specifically eschatological and personal: it is the hope of the Lord's coming, not a general optimism. Paul's pastoral strategy throughout is to restore ἐλπίς to the grieving: because Jesus rose, those who sleep will be brought with him (4:14), and the goal of the whole event is 'we will always be with the Lord' (4:17) — relationship, not mere resuscitation."
        },
        {
            "code": "G2347",
            "lemma": "θλῖψις",
            "translit": "thlipsis",
            "gloss": "affliction",
            "significance": "θλῖψις ('pressure, affliction, tribulation') marks the Thessalonian church's founding context: 'you received the word in much θλῖψις, with joy inspired by the Holy Spirit' (1:6). The church was under immediate persecution from its neighbors (2:14), driven by Thessalonica's civic and religious culture, which was hostile to exclusive allegiance to Jesus as Lord. Paul reads this θλῖψις not as evidence against the gospel but as confirmation of election — they became imitators of the churches of Judea and of the Lord himself (1:6; 2:14). The θλῖψις the believers face is the same pressure the prophets and the Lord faced; their endurance in it is proof of genuine faith."
        },
        {
            "code": "G3709",
            "lemma": "ὀργή",
            "translit": "orgē",
            "gloss": "wrath",
            "significance": "ὀργή ('wrath, anger') in 1 Thessalonians is consistently eschatological: it refers to God's coming judicial wrath at the end of history. Jesus is the one 'who delivers us from the ὀργή to come' (1:10), and God has not destined believers for ὀργή but for salvation (5:9). The wrath is not the church's normal experience of suffering (which is θλῖψις) but the divine judgment that falls on those who reject the gospel. The parousia is simultaneously the arrival of the one believers love and the coming of judgment for those who oppose God. Paul's comfort for the grieving Thessalonians is partly this: those who sleep in Jesus will not face the coming ὀργή but will be brought with him to be always with the Lord."
        },
        {
            "code": "G3525",
            "lemma": "νήφω",
            "translit": "nēphō",
            "gloss": "be sober",
            "significance": "νήφω ('to be sober, to be alert/vigilant') appears in 5:6, 8 as the watchfulness ethic that corresponds to the eschatological alert: 'let us not sleep, as others do, but let us keep awake (γρηγορῶμεν) and be sober (νήφωμεν).' The passage plays on two senses of 'sleep': literal sleep (night/day contrasted in 5:7) and the moral/spiritual sleep of the unready. The deliberate echo of κοιμάω in chapter 4 (sleep as death) gives the word an additional resonance — those who are spiritually alert are also those who understand death rightly as a sleep from which Christ will wake them. Sobriety in 5:8 is armored with faith, love, and hope — the same three virtues of 1:3."
        },
        {
            "code": "G4741",
            "lemma": "στηρίζω",
            "translit": "stērizō",
            "gloss": "establish",
            "significance": "στηρίζω ('to set fast, fix firmly, establish') appears in a key ecclesial moment: Paul sent Timothy 'to establish (στηρίξαι) and exhort you in your faith' (3:2), and now prays that God would 'establish (στηρίξαι) your hearts blameless in holiness before our Father at the coming of our Lord Jesus' (3:13). The word denotes the opposite of the instability that persecution and grief threaten. Timothy's mission and the letter itself serve the same function: to give the church the firm theological foundation it needs to stand under pressure. Paul's pastoral concern throughout is not merely to console but to establish — to create durable faith that holds in the θλῖψις."
        },
        {
            "code": "G80",
            "lemma": "ἀδελφός",
            "translit": "adelphos",
            "gloss": "brother",
            "significance": "ἀδελφός ('brother/sibling') is Paul's primary term of address in 1 Thessalonians, appearing approximately 19 times — by far the most frequent term of address in any Pauline letter of this length. In the Greco-Roman world, brotherhood was the closest form of voluntary social bond — more intimate than friendship, implying shared blood and shared fate. Paul's use of ἀδελφός for the entire church community (including women, by Paul's usage) signals that the church is a new family, not merely an association or club. The kinship language is theologically motivated: they are brothers and sisters because they share one Father (1:3) and one Lord. The pastoral warmth of 1 Thessalonians ('we were gentle among you, like a nursing mother taking care of her own children,' 2:7) expresses this kinship theology."
        },
        {
            "code": "G2168",
            "lemma": "εὐχαριστέω",
            "translit": "eucharisteo",
            "gloss": "give thanks",
            "significance": "εὐχαριστέω ('to give thanks') frames the letter at its opening (1:2) and its concluding exhortation (5:18: 'give thanks in all circumstances'). Uniquely in 1 Thessalonians, Paul's thanksgiving extends through most of chapters 1-3 — a length without parallel in his letters. The extended thanksgiving (1:2-3:13) is not a rhetorical preamble but a substantive account of the gospel at work in the Thessalonians' lives. Paul thanks God that the word came to them 'not only in word, but also in power and in the Holy Spirit' (1:5). εὐχαριστέω is therefore not merely a posture but a form of theological perception — seeing God's action in what appears to be ordinary human response and identifying it rightly as divine gift."
        }
    ],

    "language_notes": (
        "<p>The parousia passage (4:13-18) is structured as a formal theological argument using the Greek inferential connector <strong>ὥστε</strong> ('therefore,' 4:18): Paul begins with a grief situation (4:13), provides the theological ground (4:14 — 'since we believe Jesus died and rose'), deduces an inference (4:15 — 'this we declare to you'), and draws a pastoral conclusion (4:18 — 'therefore encourage one another with these words'). The argument's logic depends entirely on the resurrection of Jesus: if he rose, those who sleep through him will be brought with him. The eschatology is grounded in the gospel event, not in prophetic speculation.</p>"
        "<p>First Thessalonians 5:12-22 contains Paul's most concentrated imperative sequence — 14 successive imperatives in 11 verses, each brief, covering the life of the Christian community: respect leaders, warn the idle, encourage the fainthearted, help the weak, do not repay evil for evil, rejoice always, pray without ceasing, give thanks, do not quench the Spirit, do not despise prophecy, test everything. This rapid-fire format contrasts with the extended argument style of Romans and Galatians. The list is not random — it moves from community relationships (vv. 12-15) to individual spiritual posture (vv. 16-18) to communal discernment (vv. 19-22).</p>"
        "<p>The eschatological vocabulary of 4:16-17 deliberately echoes <strong>imperial ceremonial language</strong>. The 'cry of command' (κέλευσμα), the 'voice of an archangel,' and the 'sound of the trumpet of God' are the celestial equivalents of the military fanfare that heralded an emperor's arrival. The <strong>ἀπάντησις</strong> (meeting, 4:17) is the specific civic ceremony of going out to welcome the arriving sovereign. Paul's readers in a city shaped by Roman imperial ritual would have recognized the vocabulary — and recognized that Paul was describing a royal arrival that makes all imperial arrivals provisional."
        "<p>The phrase <strong>'as others do who have no hope'</strong> (4:13) alludes to the culture of grief Paul's readers would have known. Pagan epitaphs from this period frequently express hopelessness: 'I was not; I am not; I care not.' The elite philosophical consolation (Stoic or Epicurean) was to accept death with equanimity, not to grieve. Paul's pastoral response is different from both: he does not forbid grief ('grieve,' though the Greek allows a concessive reading) but grounds hope in historical event — the resurrection of Jesus. Christian grief is not the same as hopeless grief, because a resurrection has happened.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> The sleeping-and-rising language of 4:13-18 was central to early Christian refutation of pagan views of death. Justin Martyr, Tertullian, and Irenaeus cited it to argue for the resurrection of the body against Platonic spiritualism — death is sleep, implying a bodily awakening. Augustine's <em>City of God</em> engaged the passage in discussing the intermediate state: do the sleeping dead know anything? Augustine concluded a qualified 'no' for the body but held that the soul had an intermediate experience. The parousia-as-imperial-arrival imagery was noticed early — Chrysostom noted the deliberate contrast with the imperial <em>parousia</em> of an earthly king.</p>"
        "<p><strong>Reformation and post-Reformation:</strong> Luther's eschatology was shaped significantly by 1 Thessalonians. He read 'sleep' (κοιμάω) as describing the whole person — 'the whole man sleeps in death' (totus homo dormit) — a view sometimes called 'soul sleep.' Calvin disagreed, arguing that the sleeping refers only to the body while the soul is consciously with God. The debate was not merely academic: it concerned the status of the dead in Christ, prayers for the dead, and purgatory. Calvin's reading supported the Reformation rejection of purgatorial prayers; Luther's full-sleep view had different implications. Both drew on the same Pauline vocabulary.</p>"
        "<p><strong>Modern: the rapture debates:</strong> 1 Thessalonians 4:13-18 has been the central NT text for twentieth-century rapture theology, particularly the pre-tribulational rapture developed by John Nelson Darby (c. 1830) and popularized in the Scofield Reference Bible and the Left Behind series. Darby read ἁρπάζω ('caught up') as describing a secret pre-tribulation removal of believers from the earth, distinct from the public parousia of Matthew 24. Critics note that the passage describes one event with multiple elements and gives no indication of secrecy or of a 'tribulation' framework. The exegetical debate over ἀπάντησις ('meeting') — whether believers escort the descending Christ or are taken up to heaven — has intensified with better historical knowledge of the ancient civic reception ceremony.</p>"
    ),

    "reading_guide": (
        "<p>First Thessalonians is Paul's most pastoral letter — written out of affection rather than crisis, to a church he loves and fears losing through grief and persecution. The key to reading it well is the three-part framework of 1:3: <strong>faith, love, and hope</strong>. Chapters 1-3 (the extended thanksgiving) show these virtues at work in the Thessalonians' past and present: their faith received the word despite opposition, their love resulted in news spreading throughout Macedonia, and their hope sustains them. Chapters 4-5 instruct them in all three for the future: holiness is love's expression (4:9-12), and the parousia is hope's grounding (4:13-18).</p>"
        "<p>When reading 4:13-18, resist the impulse to immediately read it through the lens of rapture-theology debates. Read it first as pastoral grief care: Paul is writing to people who lost loved ones and are worried that those who died missed the resurrection and the return of Christ. His answer is simple: they have not missed it; in fact, they rise first (4:16), and the living will join them for the meeting with the Lord. The point of the entire passage is the final clause: 'and so we will always be with the Lord. Therefore encourage one another with these words' (4:17-18). The goal is personal union with the Lord, not doctrinal mapping of the end times.</p>"
        "<p>The most common misreading of 5:17 ('pray without ceasing') is to take it as a literal command for constant verbal prayer. The Greek ἀδιαλείπτως ('without interruption, constantly') is used of Paul's constant practice of mentioning the Thessalonians in his prayers (1:3) — it describes persistent orientation toward God throughout life's moments, not an impossible requirement to never stop speaking. The three closing imperatives ('rejoice always, pray without ceasing, give thanks in all circumstances,' 5:16-18) form a single integrated call to a Spirit-governed disposition, not three separate disciplines to be executed independently.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('1thessalonians')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('1thessalonians', merged)

main()
